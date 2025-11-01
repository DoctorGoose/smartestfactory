#!/usr/bin/env python3
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import faiss, numpy as np, os
from sentence_transformers import SentenceTransformer

# -------------------------------------------------------
# App setup
# -------------------------------------------------------
app = FastAPI(title="SmartestFactory RAG API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# -------------------------------------------------------
# Load index and model
# -------------------------------------------------------
INDEX_PATH = os.getenv("INDEX_PATH", "index/main.index")
CHUNKS_PATH = os.getenv("CHUNKS_PATH", "index/chunks.npy")
MODEL_NAME = os.getenv("MODEL_NAME", "all-MiniLM-L6-v2")

print(f"[INFO] Loading FAISS index from {INDEX_PATH}")
index = faiss.read_index(INDEX_PATH)
chunks = np.load(CHUNKS_PATH, allow_pickle=True)
model = SentenceTransformer(MODEL_NAME)

# -------------------------------------------------------
# Schema
# -------------------------------------------------------
class Query(BaseModel):
    query: str
    k: int = 5

# -------------------------------------------------------
# Routes
# -------------------------------------------------------
@app.get("/")
def root():
    return {"status": "ok", "message": "SmartestFactory RAG API is running."}

@app.post("/retrieve")
def retrieve(q: Query):
    q_emb = model.encode([q.query])
    D, I = index.search(q_emb, q.k)
    results = [chunks[i] for i in I[0]]
    return {
        "query": q.query,
        "retrieved_docs": results,
        "context": "\n\n".join(results)
    }

@app.get("/")
def root():
    return {"status": "ok", "message": "SmartestFactory RAG API is running."}

# -------------------------------------------------------
# Serve OpenAPI schema for ChatGPT tool
# -------------------------------------------------------
from fastapi.responses import FileResponse

@app.get("/openapi.yaml", include_in_schema=False)
def get_openapi_yaml():
    """Serve the OpenAPI schema for ChatGPT to use."""
    return FileResponse("openapi.yaml", media_type="text/yaml")

