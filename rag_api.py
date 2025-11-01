#!/usr/bin/env python3
from fastapi import FastAPI
from pydantic import BaseModel
import faiss, numpy as np
from sentence_transformers import SentenceTransformer
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(title="SmartestFactory RAG API")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

INDEX_PATH = os.getenv("INDEX_PATH", "index/main.index")
CHUNKS_PATH = os.getenv("CHUNKS_PATH", "index/chunks.npy")
MODEL_NAME = os.getenv("MODEL_NAME", "all-MiniLM-L6-v2")

print(f"[INFO] Loading FAISS index from {INDEX_PATH}")
index = faiss.read_index(INDEX_PATH)
chunks = np.load(CHUNKS_PATH, allow_pickle=True)
model = SentenceTransformer(MODEL_NAME)

class Query(BaseModel):
    query: str
    k: int = 5

@app.post("/retrieve")
def retrieve(q: Query):
    q_emb = model.encode([q.query])
    D, I = index.search(q_emb, q.k)
    results = [chunks[i] for i in I[0]]
    return {"context": "\n\n".join(results)}

@app.get("/")
def root():
    return {"status": "ok", "message": "SmartestFactory RAG API is running."}
