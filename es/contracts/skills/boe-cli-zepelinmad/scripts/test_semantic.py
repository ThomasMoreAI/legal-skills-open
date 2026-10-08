#!/usr/bin/env python3
"""
Test semantic search quality for BOE CLI.
Runs queries and shows top results with scores.
"""

import json
import os
import sys
import urllib.request
import math

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
OPENAI_API = "https://api.openai.com/v1/embeddings"
MODEL = "text-embedding-3-small"
INDEX_PATH = os.path.expanduser("~/.boe/index-v1.json")

def load_index():
    print("Loading index...", file=sys.stderr)
    with open(INDEX_PATH) as f:
        return json.load(f)

def embed_query(text):
    payload = json.dumps({
        "model": MODEL,
        "input": text,
        "dimensions": 1536,
    }).encode("utf-8")
    req = urllib.request.Request(
        OPENAI_API,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {OPENAI_API_KEY}",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read())
    return data["data"][0]["embedding"]

def cosine_sim(a, b):
    dot = sum(x*y for x,y in zip(a,b))
    na = math.sqrt(sum(x*x for x in a))
    nb = math.sqrt(sum(x*x for x in b))
    if na == 0 or nb == 0:
        return 0
    return dot / (na * nb)

def search(index, query_vec, k=10):
    results = []
    for e in index["entries"]:
        score = cosine_sim(query_vec, e["vector"])
        results.append((score, e["id"], e["title"]))
    results.sort(reverse=True)
    return results[:k]

# Test queries: (query, expected_law_keyword)
TEST_QUERIES = [
    # Natural language queries (the hard ones)
    ("puedo echar a mi inquilino", "arrendamiento"),
    ("responsabilidad del administrador de una empresa", "sociedades"),
    ("cuánto tiempo tengo para reclamar una deuda", "prescripción"),
    ("derechos del trabajador despedido", "trabajador"),
    ("herencia y testamento", "herencia"),
    ("protección de datos personales", "datos"),
    ("divorcio y custodia de hijos", "divorcio"),
    ("impuestos de una sociedad", "impuesto"),
    ("blanqueo de capitales", "blanqueo"),
    ("compraventa de empresa", "sociedades"),
    
    # Legal concepts
    ("due diligence en M&A", "sociedades"),
    ("pacto de socios", "sociedades"),
    ("fusiones y adquisiciones", "fusión"),
    ("cláusula de no competencia", "competencia"),
    ("resolución de contratos", "contrato"),
    
    # Specific areas
    ("ley de sociedades de capital", "sociedades"),
    ("código civil", "civil"),
    ("estatuto de los trabajadores", "trabajador"),
    ("ley general tributaria", "tributaria"),
    ("ley de propiedad intelectual", "propiedad intelectual"),
]

def main():
    if not OPENAI_API_KEY:
        print("Set OPENAI_API_KEY", file=sys.stderr)
        sys.exit(1)
    
    idx = load_index()
    print(f"Index: {idx['count']} entries, model: {idx['model']}\n")
    
    for query, expected in TEST_QUERIES:
        print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"🔍 Query: \"{query}\"")
        print(f"   Expected: contains \"{expected}\"")
        
        qvec = embed_query(query)
        results = search(idx, qvec, k=5)
        
        found = False
        for i, (score, id, title) in enumerate(results):
            marker = ""
            if expected.lower() in title.lower():
                marker = " ✅"
                found = True
            print(f"   {i+1}. [{score:.4f}] {title[:90]}{marker}")
        
        if not found:
            print(f"   ❌ Expected keyword \"{expected}\" NOT in top 5")
        print()

if __name__ == "__main__":
    main()
