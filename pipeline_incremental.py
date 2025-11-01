#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Incremental multimodal document indexing pipeline.

Features:
  • Recursively scan `data/` for supported file types (JSONL, PDF, TXT, MD).
  • Parse, clean, chunk, and embed only new or modified documents.
  • Merge embeddings into an existing FAISS index (incrementally).
  • Maintain a metadata ledger (`meta.json`) tracking file hashes and chunk counts.

Usage:
  python pipeline_incremental.py --data-dir data --index-dir index
"""

import os
import re
import json
import time
import hashlib
from pathlib import Path
from typing import List, Dict

import numpy as np
from rich.console import Console
from rich.progress import Progress, BarColumn, TimeRemainingColumn, TimeElapsedColumn
import torch
import faiss
from tqdm import tqdm
from sentence_transformers import SentenceTransformer
from PyPDF2 import PdfReader


# --------------------------
# Utilities
# --------------------------

def sha1_file(path: Path) -> str:
    """Compute file SHA1 for change detection."""
    h = hashlib.sha1()
    with open(path, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()


def clean_text(text: str) -> str:
    """Minimal cleanup for wiki / text content."""
    text = re.sub(r"\{\{.*?\}\}", "", text, flags=re.S)
    text = re.sub(r"<ref.*?>.*?</ref>", "", text, flags=re.S)
    text = re.sub(r"==+.*?==+", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def chunk_text(text: str, max_tokens: int = 512, overlap: int = 64) -> List[str]:
    words = text.split()
    chunks = []
    step = max_tokens - overlap
    for i in range(0, len(words), step):
        chunk = " ".join(words[i : i + max_tokens])
        chunks.append(chunk)
        if i + max_tokens >= len(words):
            break
    return chunks


def load_jsonl(path: Path) -> List[str]:
    texts = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            rec = json.loads(line)
            if "wikitext" in rec:
                txt = clean_text(rec["wikitext"])
                if txt:
                    texts.append(txt)
    return texts


def load_pdf(path: Path) -> List[str]:
    text = ""
    reader = PdfReader(path)
    for page in reader.pages:
        text += page.extract_text() or ""
        text += "\n\n"
    return [clean_text(text)]


def load_textfile(path: Path) -> List[str]:
    text = path.read_text("utf-8", errors="ignore")
    return [clean_text(text)]


# --------------------------
# Index Manager
# --------------------------


class IncrementalIndexer:
    def __init__(self, data_dir: str, index_dir: str, model_name: str = "all-MiniLM-L6-v2"):
        self.console = Console()
        self.data_dir = Path(data_dir)
        self.index_dir = Path(index_dir)
        self.model_name = model_name
        self.index_path = self.index_dir / "main.index"
        self.chunks_path = self.index_dir / "chunks.npy"
        self.meta_path = self.index_dir / "meta.json"

        # --- Auto GPU detection ---
        if torch.cuda.is_available():
            self.device = "cuda"
            self.gpu_name = torch.cuda.get_device_name(0)
            self.console.print(f"[bold green]✓ GPU detected:[/bold green] {self.gpu_name}")
        else:
            self.device = "cpu"
            self.console.print("[yellow]⚠ No GPU detected, using CPU.[/yellow]")

        self.model = SentenceTransformer(model_name, device=self.device)

        # Setup dirs and state
        self.index_dir.mkdir(parents=True, exist_ok=True)
        self.meta = self._load_meta()
        self.index, self.chunks = self._load_index()

    def _load_meta(self) -> Dict:
        if self.meta_path.exists():
            return json.loads(self.meta_path.read_text("utf-8"))
        return {"files": {}}

    def _save_meta(self):
        self.meta_path.write_text(json.dumps(self.meta, indent=2, ensure_ascii=False), "utf-8")

    def _load_index(self):
        if self.index_path.exists() and self.chunks_path.exists():
            index = faiss.read_index(str(self.index_path))
            chunks = np.load(self.chunks_path, allow_pickle=True).tolist()
        else:
            index = None
            chunks = []
        return index, chunks

    def _save_index(self):
        faiss.write_index(self.index, str(self.index_path))
        np.save(self.chunks_path, np.array(self.chunks, dtype=object))
        self._save_meta()

    def scan_files(self) -> List[Path]:
        exts = [".jsonl", ".pdf", ".txt", ".md"]
        return [p for p in self.data_dir.rglob("*") if p.suffix.lower() in exts]

    def get_new_or_changed(self) -> List[Path]:
        files = self.scan_files()
        to_update = []
        for f in files:
            sha = sha1_file(f)
            old = self.meta["files"].get(str(f))
            if not old or old["sha1"] != sha:
                to_update.append(f)
        return to_update

    def process_file(self, path: Path) -> List[str]:
        ext = path.suffix.lower()
        if ext == ".jsonl":
            texts = load_jsonl(path)
        elif ext == ".pdf":
            texts = load_pdf(path)
        elif ext in (".txt", ".md"):
            texts = load_textfile(path)
        else:
            return []
        chunks = []
        for t in texts:
            chunks.extend(chunk_text(t))
        return chunks

    def add_embeddings(self, chunks: List[str]):
        if not chunks:
            return
        start = time.time()
        with Progress(
            "[progress.description]{task.description}",
            BarColumn(),
            "[progress.percentage]{task.percentage:>3.0f}%",
            TimeElapsedColumn(),
            TimeRemainingColumn(),
            console=self.console,
        ) as progress:
            task = progress.add_task(f"[cyan]Embedding {len(chunks)} chunks", total=len(chunks))
            embeddings = []
            batch_size = 64 if self.device == "cuda" else 16
            for i in range(0, len(chunks), batch_size):
                batch = chunks[i:i+batch_size]
                emb = self.model.encode(batch, convert_to_numpy=True, show_progress_bar=False)
                embeddings.append(emb)
                progress.advance(task, len(batch))
            embeddings = np.vstack(embeddings)

        elapsed = time.time() - start
        rate = len(chunks) / elapsed
        self.console.print(f"[green]✓ Embedded {len(chunks)} chunks in {elapsed:.1f}s "
                           f"({rate:.1f} chunks/sec)[/green]")

        dim = embeddings.shape[1]
        if self.index is None:
            self.index = faiss.IndexFlatL2(dim)
        self.index.add(embeddings)
        self.chunks.extend(chunks)

    def update(self):
        self.console.print(f"[bold cyan]Scanning {self.data_dir} for new or modified files...[/bold cyan]")
        targets = self.get_new_or_changed()
        if not targets:
            self.console.print("[bold green]✓ Index is already up to date.[/bold green]")
            return

        self.console.print(f"[bold yellow]Found {len(targets)} new/modified file(s).[/bold yellow]\n")

        for f in targets:
            self.console.rule(f"[blue]{f.name}[/blue]")
            sha = sha1_file(f)
            chunks = self.process_file(f)
            if chunks:
                self.add_embeddings(chunks)
                self.meta["files"][str(f)] = {"sha1": sha, "chunks": len(chunks), "timestamp": time.time()}

        self._save_index()
        self.console.print(f"[bold green]✓ Index updated. Total chunks: {len(self.chunks)}[/bold green]")

    def query(self, query: str, k: int = 5):
        if self.index is None:
            self.console.print("[red]No index loaded.[/red]")
            return
        q_emb = self.model.encode([query])
        D, I = self.index.search(q_emb, k)
        self.console.rule(f"[bold cyan]Results for: {query}[/bold cyan]")
        for rank, idx in enumerate(I[0]):
            self.console.print(f"[bold magenta]Rank {rank+1}[/bold magenta] • Score: {D[0][rank]:.4f}")
            self.console.print(self.chunks[idx][:400] + "...\n")


# --------------------------
# Entry point
# --------------------------

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Incremental multimodal document indexer.")
    parser.add_argument("--data-dir", default="data")
    parser.add_argument("--index-dir", default="index")
    parser.add_argument("--query", default=None, help="Optional search query")
    args = parser.parse_args()

    indexer = IncrementalIndexer(args.data_dir, args.index_dir)
    indexer.update()

    if args.query:
        indexer.query(args.query)
