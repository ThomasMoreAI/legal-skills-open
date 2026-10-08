#!/usr/bin/env python3
"""
Test: title enrichment vs raw titles for semantic search.
Compare three approaches:
1. Raw title embeddings (current)
2. Enriched title embeddings (title + LLM-generated keywords/description)
3. HyDE: query-side expansion (generate hypothetical title, embed that)
"""

import json, os, sys, urllib.request, math
import numpy as np

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")

def embed(texts, model="text-embedding-3-small"):
    """Embed one or more texts."""
    if isinstance(texts, str):
        texts = [texts]
    payload = json.dumps({"model": model, "input": texts, "dimensions": 1536}).encode()
    req = urllib.request.Request("https://api.openai.com/v1/embeddings", data=payload, headers={
        "Content-Type": "application/json", "Authorization": f"Bearer {OPENAI_API_KEY}"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.loads(resp.read())
    vecs = [np.array(d["embedding"], dtype=np.float32) for d in sorted(data["data"], key=lambda x: x["index"])]
    return vecs if len(vecs) > 1 else vecs[0]

def llm_call(prompt, model="gpt-4o-mini"):
    """Quick LLM call."""
    payload = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0,
        "max_tokens": 300,
    }).encode()
    req = urllib.request.Request("https://api.openai.com/v1/chat/completions", data=payload, headers={
        "Content-Type": "application/json", "Authorization": f"Bearer {OPENAI_API_KEY}"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read())
    return data["choices"][0]["message"]["content"]

def cosine(a, b):
    a_n = a / (np.linalg.norm(a) or 1)
    b_n = b / (np.linalg.norm(b) or 1)
    return float(np.dot(a_n, b_n))

# A few sample laws to test enrichment
SAMPLE_LAWS = [
    {
        "id": "BOE-A-2010-10544",
        "title": "Real Decreto Legislativo 1/2010, de 2 de julio, por el que se aprueba el texto refundido de la Ley de Sociedades de Capital.",
    },
    {
        "id": "BOE-A-1889-4763", 
        "title": "Real Decreto de 24 de julio de 1889 por el que se publica el Código Civil.",
    },
    {
        "id": "BOE-A-2010-5292",
        "title": "Ley 10/2010, de 28 de abril, de prevención del blanqueo de capitales y de la financiación del terrorismo.",
    },
    {
        "id": "BOE-A-2015-11430",
        "title": "Real Decreto Legislativo 2/2015, de 23 de octubre, por el que se aprueba el texto refundido de la Ley del Estatuto de los Trabajadores.",
    },
    {
        "id": "BOE-A-1994-26003",
        "title": "Ley 29/1994, de 24 de noviembre, de Arrendamientos Urbanos.",
    },
    {
        "id": "BOE-A-2003-12816",
        "title": "Ley 22/2003, de 9 de julio, Concursal.",
    },
    {
        "id": "BOE-A-2009-5276",
        "title": "Ley 3/2009, de 3 de abril, sobre modificaciones estructurales de las sociedades mercantiles.",
    },
]

# Conceptual queries that should match the above laws
TEST_QUERIES = [
    ("responsabilidad del administrador", "BOE-A-2010-10544"),  # LSC
    ("herencia sin testamento", "BOE-A-1889-4763"),  # CC
    ("blanqueo de dinero", "BOE-A-2010-5292"),
    ("despido improcedente", "BOE-A-2015-11430"),  # ET
    ("echar al inquilino", "BOE-A-1994-26003"),  # LAU
    ("quiebra de empresa", "BOE-A-2003-12816"),  # Concursal
    ("fusión de sociedades", "BOE-A-2009-5276"),  # Modificaciones estructurales
    ("pacto de socios", "BOE-A-2010-10544"),  # LSC
    ("junta de accionistas", "BOE-A-2010-10544"),  # LSC
    ("prescripción de deudas", "BOE-A-1889-4763"),  # CC
]

ENRICHMENT_PROMPT = """Given this Spanish law title, generate a brief description of what this law covers, including key topics, articles, and common search terms someone might use to find it. Output ONLY the enrichment text (no title repetition), in Spanish, max 2 sentences.

Title: {title}

Enrichment:"""

HYDE_PROMPT = """The user is searching for a Spanish law. Given their query, generate the TITLE of the most relevant Spanish law as it would appear in the BOE (Boletín Oficial del Estado). Output ONLY the hypothetical title, nothing else.

Query: {query}

Hypothetical BOE title:"""

def main():
    if not OPENAI_API_KEY:
        print("Set OPENAI_API_KEY"); sys.exit(1)
    
    print("=" * 60)
    print("EXPERIMENT: Improving semantic search for short law titles")
    print("=" * 60)
    
    # Step 1: Embed raw titles
    print("\n📊 Approach 1: Raw title embeddings (current)")
    raw_vecs = {}
    raw_titles = [law["title"] for law in SAMPLE_LAWS]
    vecs = embed(raw_titles)
    for law, vec in zip(SAMPLE_LAWS, vecs):
        raw_vecs[law["id"]] = vec
    
    # Step 2: Enrich titles with LLM, then embed
    print("\n📊 Approach 2: LLM-enriched title embeddings")
    enriched_vecs = {}
    for law in SAMPLE_LAWS:
        enrichment = llm_call(ENRICHMENT_PROMPT.format(title=law["title"]))
        enriched_text = f"{law['title']} — {enrichment}"
        print(f"  {law['id']}: +{len(enrichment)} chars")
        enriched_vecs[law["id"]] = embed(enriched_text)
    
    # Step 3: Test queries
    print(f"\n{'='*60}")
    print(f"{'Query':<35} {'Raw':>6} {'Enriched':>9} {'HyDE':>6}  Winner")
    print(f"{'-'*35} {'-'*6} {'-'*9} {'-'*6}  {'-'*8}")
    
    raw_wins, enriched_wins, hyde_wins = 0, 0, 0
    
    for query, expected_id in TEST_QUERIES:
        # Raw similarity
        q_vec = embed(query)
        raw_score = cosine(q_vec, raw_vecs[expected_id])
        
        # Enriched similarity
        enriched_score = cosine(q_vec, enriched_vecs[expected_id])
        
        # HyDE: expand query into hypothetical title
        hypo_title = llm_call(HYDE_PROMPT.format(query=query))
        hyde_vec = embed(hypo_title)
        hyde_score = cosine(hyde_vec, raw_vecs[expected_id])
        
        best = max(raw_score, enriched_score, hyde_score)
        winner = "RAW" if raw_score == best else ("ENRICH" if enriched_score == best else "HyDE")
        if raw_score == best: raw_wins += 1
        elif enriched_score == best: enriched_wins += 1
        else: hyde_wins += 1
        
        improvement_e = ((enriched_score - raw_score) / raw_score * 100)
        improvement_h = ((hyde_score - raw_score) / raw_score * 100)
        
        print(f"  {query:<33} {raw_score:.4f} {enriched_score:.4f}({improvement_e:+.0f}%) {hyde_score:.4f}({improvement_h:+.0f}%)  {winner}")
    
    print(f"\n{'='*60}")
    print(f"Wins — Raw: {raw_wins} | Enriched: {enriched_wins} | HyDE: {hyde_wins}")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
