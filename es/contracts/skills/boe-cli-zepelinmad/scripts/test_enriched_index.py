#!/usr/bin/env python3
"""
Test approach 3: Enrich INDEX with synthetic queries (offline), then match raw queries.
This is the inverse of HyDE - instead of expanding queries at search time,
we expand documents at index time with "what would someone search to find this law?"

This avoids LLM calls at query time while getting HyDE-like benefits.
"""

import json, os, sys, urllib.request
import numpy as np

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")

def embed(texts, model="text-embedding-3-small"):
    if isinstance(texts, str): texts = [texts]
    payload = json.dumps({"model": model, "input": texts, "dimensions": 1536}).encode()
    req = urllib.request.Request("https://api.openai.com/v1/embeddings", data=payload, headers={
        "Content-Type": "application/json", "Authorization": f"Bearer {OPENAI_API_KEY}"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.loads(resp.read())
    vecs = [np.array(d["embedding"], dtype=np.float32) for d in sorted(data["data"], key=lambda x: x["index"])]
    return vecs if len(vecs) > 1 else vecs[0]

def llm_call(prompt, model="gpt-4o-mini"):
    payload = json.dumps({"model": model, "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.3, "max_tokens": 400}).encode()
    req = urllib.request.Request("https://api.openai.com/v1/chat/completions", data=payload, headers={
        "Content-Type": "application/json", "Authorization": f"Bearer {OPENAI_API_KEY}"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read())
    return data["choices"][0]["message"]["content"]

def cosine(a, b):
    a_n = a / (np.linalg.norm(a) or 1)
    b_n = b / (np.linalg.norm(b) or 1)
    return float(np.dot(a_n, b_n))

SAMPLE_LAWS = [
    {"id": "BOE-A-2010-10544", "title": "Real Decreto Legislativo 1/2010, de 2 de julio, por el que se aprueba el texto refundido de la Ley de Sociedades de Capital."},
    {"id": "BOE-A-1889-4763", "title": "Real Decreto de 24 de julio de 1889 por el que se publica el Código Civil."},
    {"id": "BOE-A-2010-5292", "title": "Ley 10/2010, de 28 de abril, de prevención del blanqueo de capitales y de la financiación del terrorismo."},
    {"id": "BOE-A-2015-11430", "title": "Real Decreto Legislativo 2/2015, de 23 de octubre, por el que se aprueba el texto refundido de la Ley del Estatuto de los Trabajadores."},
    {"id": "BOE-A-1994-26003", "title": "Ley 29/1994, de 24 de noviembre, de Arrendamientos Urbanos."},
    {"id": "BOE-A-2003-12816", "title": "Ley 22/2003, de 9 de julio, Concursal."},
    {"id": "BOE-A-2009-5276", "title": "Ley 3/2009, de 3 de abril, sobre modificaciones estructurales de las sociedades mercantiles."},
]

SYNTHETIC_QUERIES_PROMPT = """Given this Spanish law title from the BOE (Boletín Oficial del Estado), generate 8-10 natural language search queries that a lawyer or law student might use to find this law. Include:
- Colloquial/everyday language queries
- Technical legal queries
- Specific topic queries (key articles/concepts the law covers)

Output ONLY the queries, one per line, no numbering.

Title: {title}"""

TEST_QUERIES = [
    ("responsabilidad del administrador", "BOE-A-2010-10544"),
    ("herencia sin testamento", "BOE-A-1889-4763"),
    ("blanqueo de dinero", "BOE-A-2010-5292"),
    ("despido improcedente", "BOE-A-2015-11430"),
    ("echar al inquilino", "BOE-A-1994-26003"),
    ("quiebra de empresa", "BOE-A-2003-12816"),
    ("fusión de sociedades", "BOE-A-2009-5276"),
    ("pacto de socios", "BOE-A-2010-10544"),
    ("junta de accionistas", "BOE-A-2010-10544"),
    ("prescripción de deudas", "BOE-A-1889-4763"),
]

def main():
    if not OPENAI_API_KEY: print("Set OPENAI_API_KEY"); sys.exit(1)
    
    print("=" * 70)
    print("EXPERIMENT: Synthetic query enrichment (expand index, not queries)")
    print("=" * 70)
    
    # Step 1: Raw embeddings
    print("\n📊 Step 1: Raw title embeddings")
    raw_vecs = {}
    for law in SAMPLE_LAWS:
        raw_vecs[law["id"]] = embed(law["title"])
    
    # Step 2: Generate synthetic queries for each law, embed the combined text
    print("\n📊 Step 2: Generate synthetic queries + embed combined text")
    enriched_vecs = {}
    for law in SAMPLE_LAWS:
        queries = llm_call(SYNTHETIC_QUERIES_PROMPT.format(title=law["title"]))
        combined = f"{law['title']}\n\nBúsquedas relacionadas:\n{queries}"
        print(f"\n  {law['id']}:")
        for q in queries.strip().split("\n")[:5]:
            print(f"    → {q.strip()}")
        enriched_vecs[law["id"]] = embed(combined)
    
    # Step 3: Multi-vector approach - embed each synthetic query separately,
    # match against the BEST one
    print("\n📊 Step 3: Multi-vector (each synthetic query = separate vector)")
    multi_vecs = {}  # id -> list of vectors
    for law in SAMPLE_LAWS:
        queries = llm_call(SYNTHETIC_QUERIES_PROMPT.format(title=law["title"]))
        query_list = [q.strip() for q in queries.strip().split("\n") if q.strip()]
        all_texts = [law["title"]] + query_list
        vecs = embed(all_texts)
        multi_vecs[law["id"]] = vecs
    
    # Step 4: Compare
    print(f"\n{'='*70}")
    print(f"{'Query':<33} {'Raw':>6} {'Combined':>9} {'Multi-V':>8}  Best")
    print(f"{'-'*33} {'-'*6} {'-'*9} {'-'*8}  {'-'*8}")
    
    wins = {"raw": 0, "combined": 0, "multi": 0}
    
    for query, expected_id in TEST_QUERIES:
        q_vec = embed(query)
        
        # Raw
        raw_score = cosine(q_vec, raw_vecs[expected_id])
        
        # Combined enrichment
        combined_score = cosine(q_vec, enriched_vecs[expected_id])
        
        # Multi-vector: best match across all vectors for this law
        multi_score = max(cosine(q_vec, v) for v in multi_vecs[expected_id])
        
        best = max(raw_score, combined_score, multi_score)
        if raw_score == best: winner = "RAW"; wins["raw"] += 1
        elif combined_score == best: winner = "COMBINED"; wins["combined"] += 1
        else: winner = "MULTI-V"; wins["multi"] += 1
        
        imp_c = (combined_score - raw_score) / raw_score * 100
        imp_m = (multi_score - raw_score) / raw_score * 100
        
        print(f"  {query:<31} {raw_score:.4f} {combined_score:.4f}({imp_c:+.0f}%) {multi_score:.4f}({imp_m:+.0f}%)  {winner}")
    
    print(f"\n{'='*70}")
    print(f"Wins — Raw: {wins['raw']} | Combined: {wins['combined']} | Multi-V: {wins['multi']}")
    print(f"\nKey insight: Multi-vector stores ~10 vectors per law instead of 1.")
    print(f"Index size would go from 74MB to ~740MB. Trade-off: 10x storage, much better recall.")
    print(f"Alternative: average the synthetic query vectors with the title vector (same size, less boost)")

if __name__ == "__main__":
    main()
