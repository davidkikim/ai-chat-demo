import sqlite3
import numpy as np
from openai import OpenAI

client = OpenAI()

def cosine_similarity(a, b):
    a, b = np.array(a), np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def retrieve_relevant_chunks(query, k=3):
    conn = sqlite3.connect("vectors.db")
    db = conn.cursor()

    # Embed query
    q_emb = client.embeddings.create(
        model="text-embedding-3-small",
        input=query
    ).data[0].embedding

    # Fetch chunks
    db.execute("") # TODO: Fetch all chunks and embeddings
    rows = db.fetchall()

    scored = []
    for content, blob in rows:
        emb = np.frombuffer(blob, dtype=np.float32)
        
        score = "" # TODO: Compute cosine similarity between q_emb and emb
        # TODO: Append (score, content) to scored

    scored.sort(reverse=True)
    return [c for _, c in scored[:k]]

def answer_question(query):
    chunks = "" # TODO: retrieve relevant chunks
    context = "" # TODO: combine chunks into context

    prompt = f"""
    Use ONLY the information in the context below to answer the question.

    Context:
    {context}

    Question: {query}
    """

    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return resp.choices[0].message["content"]
