@app.post("/context-only")
def context_only(q: Query):
    q_emb = model.encode([q.query])
    D, I = index.search(q_emb, q.k)
    results = [chunks[i] for i in I[0]]
    return {"context": "\n\n".join(results)}
