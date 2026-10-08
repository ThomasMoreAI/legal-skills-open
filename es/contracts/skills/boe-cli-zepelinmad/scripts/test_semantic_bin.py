#!/usr/bin/env python3
"""
Test semantic search quality using the binary index (much faster to load).
"""

import struct
import os
import sys
import json
import math
import urllib.request

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
OPENAI_API = "https://api.openai.com/v1/embeddings"
MODEL = "text-embedding-3-small"
DIMS = 1536
BIN_PATH = os.path.expanduser("~/.boe/index-v1.bin")

def load_binary_index():
    entries = []
    with open(BIN_PATH, "rb") as f:
        magic = f.read(4)
        assert magic == b"BOEI", f"Bad magic: {magic}"
        version, dims, count = struct.unpack("<III", f.read(12))
        print(f"Index: v{version}, {dims} dims, {count} entries", file=sys.stderr)
        
        for i in range(count):
            id_len = struct.unpack("<I", f.read(4))[0]
            entry_id = f.read(id_len).decode("utf-8")
            title_len = struct.unpack("<I", f.read(4))[0]
            title = f.read(title_len).decode("utf-8")
            vec = list(struct.unpack(f"<{dims}f", f.read(dims * 4)))
            entries.append({"id": entry_id, "title": title, "vector": vec})
    
    return entries

def embed_query(text):
    payload = json.dumps({
        "model": MODEL, "input": text, "dimensions": DIMS,
    }).encode("utf-8")
    req = urllib.request.Request(OPENAI_API, data=payload, headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}",
    })
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read())
    return data["data"][0]["embedding"]

def cosine_sim(a, b):
    dot = sum(x*y for x,y in zip(a,b))
    na = math.sqrt(sum(x*x for x in a))
    nb = math.sqrt(sum(x*x for x in b))
    return dot / (na * nb) if na > 0 and nb > 0 else 0

def search(entries, query_vec, k=10):
    scored = [(cosine_sim(query_vec, e["vector"]), e["id"], e["title"]) for e in entries]
    scored.sort(reverse=True)
    return scored[:k]

TEST_QUERIES = [
    ("puedo echar a mi inquilino", "arrendamiento"),
    ("responsabilidad del administrador", "sociedades"),
    ("despido improcedente", "trabajador"),
    ("herencia y testamento", "herencia|civil|sucesión"),
    ("protección de datos", "datos|privacidad"),
    ("blanqueo de capitales", "blanqueo"),
    ("compraventa de empresa", "sociedades|mercantil"),
    ("pacto de socios", "sociedades|socios"),
    ("fusiones y adquisiciones", "fusión|estructura"),
    ("ley de sociedades de capital", "sociedades"),
    ("código civil", "civil"),
    ("estatuto de los trabajadores", "trabajador"),
    ("impuesto sobre sociedades", "impuesto|societario|tributar"),
    ("propiedad intelectual", "propiedad intelectual"),
    ("competencia desleal", "competencia"),
    ("concurso de acreedores", "concurs"),
    ("arrendamiento de vivienda", "arrendamiento"),
    ("violencia de género", "violencia"),
    ("prescripción de deudas", "prescripción|civil"),
    ("contrato de trabajo temporal", "trabajador|empleo"),
]

def main():
    if not OPENAI_API_KEY:
        print("Set OPENAI_API_KEY", file=sys.stderr)
        sys.exit(1)
    
    print("Loading binary index...", file=sys.stderr)
    entries = load_binary_index()
    print(f"Loaded {len(entries)} entries\n", file=sys.stderr)
    
    hits = 0
    total = len(TEST_QUERIES)
    
    for query, expected_kws in TEST_QUERIES:
        kws = expected_kws.lower().split("|")
        print(f"━━━ 🔍 \"{query}\" (expect: {expected_kws}) ━━━")
        
        qvec = embed_query(query)
        results = search(entries, qvec, k=5)
        
        found = False
        for i, (score, eid, title) in enumerate(results):
            match = any(kw in title.lower() for kw in kws)
            marker = " ✅" if match else ""
            if match:
                found = True
            print(f"  {i+1}. [{score:.4f}] {title[:100]}{marker}")
        
        if found:
            hits += 1
        else:
            print(f"  ❌ MISS — none of [{expected_kws}] in top 5")
        print()
    
    print(f"\n{'='*50}")
    print(f"Score: {hits}/{total} ({100*hits/total:.0f}%)")
    print(f"{'='*50}")

if __name__ == "__main__":
    main()
