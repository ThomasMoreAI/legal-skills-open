#!/usr/bin/env python3
"""Test semantic search quality using numpy for fast cosine sim."""

import struct, os, sys, json, urllib.request
import numpy as np

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
OPENAI_API = "https://api.openai.com/v1/embeddings"
MODEL = "text-embedding-3-small"
DIMS = 1536
BIN_PATH = os.path.expanduser(sys.argv[1] if len(sys.argv) > 1 else "~/.boe/index-v1.bin")

def load_binary_index():
    ids, titles, vectors = [], [], []
    with open(BIN_PATH, "rb") as f:
        magic = f.read(4)
        assert magic == b"BOEI"
        version, dims, count = struct.unpack("<III", f.read(12))
        print(f"Index: {count} entries, {dims} dims", file=sys.stderr)
        for _ in range(count):
            id_len = struct.unpack("<I", f.read(4))[0]
            ids.append(f.read(id_len).decode())
            title_len = struct.unpack("<I", f.read(4))[0]
            titles.append(f.read(title_len).decode())
            vectors.append(struct.unpack(f"<{dims}f", f.read(dims * 4)))
    mat = np.array(vectors, dtype=np.float32)
    # Normalize for fast cosine via dot product
    norms = np.linalg.norm(mat, axis=1, keepdims=True)
    norms[norms == 0] = 1
    mat = mat / norms
    return ids, titles, mat

def embed_query(text):
    payload = json.dumps({"model": MODEL, "input": text, "dimensions": DIMS}).encode()
    req = urllib.request.Request(OPENAI_API, data=payload, headers={
        "Content-Type": "application/json", "Authorization": f"Bearer {OPENAI_API_KEY}",
    })
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read())
    vec = np.array(data["data"][0]["embedding"], dtype=np.float32)
    return vec / np.linalg.norm(vec)

def search(mat, query_vec, k=10):
    scores = mat @ query_vec  # dot product on normalized = cosine
    top_k = np.argsort(scores)[-k:][::-1]
    return [(scores[i], i) for i in top_k]

TEST_QUERIES = [
    ("puedo echar a mi inquilino", "arrendamiento|alquiler|vivienda"),
    ("responsabilidad del administrador de una empresa", "sociedades|administrador"),
    ("despido improcedente", "trabajador|estatuto|empleo"),
    ("herencia y testamento", "herencia|civil|sucesión|código civil"),
    ("protección de datos personales", "datos|privacidad|protección"),
    ("blanqueo de capitales", "blanqueo|prevención"),
    ("compraventa de empresa", "sociedades|mercantil|estructura|modificaciones"),
    ("pacto de socios", "sociedades|socios|capital"),
    ("fusiones y adquisiciones", "fusión|estructura|modific"),
    ("ley de sociedades de capital", "sociedades de capital"),
    ("código civil", "código civil"),
    ("estatuto de los trabajadores", "trabajador"),
    ("impuesto sobre sociedades", "impuesto|societario|tributar"),
    ("propiedad intelectual", "propiedad intelectual"),
    ("competencia desleal", "competencia"),
    ("concurso de acreedores", "concurs"),
    ("arrendamiento de vivienda", "arrendamiento"),
    ("violencia de género", "violencia"),
    ("prescripción de deudas", "prescripción|civil"),
    ("contrato de trabajo temporal", "trabajador|empleo|contrat"),
    # Harder natural language
    ("me han robado y quiero denunciar", "penal|código penal"),
    ("montar una sociedad limitada", "sociedades|mercantil"),
    ("cuánto pago de impuestos como autónomo", "autónomo|tributar|IRPF|renta"),
    ("derechos del consumidor", "consumidor|defensa"),
    ("me quiero divorciar", "divorcio|civil|matrimon"),
]

def main():
    if not OPENAI_API_KEY:
        print("Set OPENAI_API_KEY", file=sys.stderr); sys.exit(1)
    
    ids, titles, mat = load_binary_index()
    
    hits = 0
    for query, expected_kws in TEST_QUERIES:
        kws = [k.lower() for k in expected_kws.split("|")]
        print(f"━━━ 🔍 \"{query}\" ━━━")
        
        qvec = embed_query(query)
        results = search(mat, qvec, k=7)
        
        found = False
        for rank, (score, idx) in enumerate(results):
            match = any(kw in titles[idx].lower() for kw in kws)
            if match: found = True
            marker = " ✅" if match else ""
            print(f"  {rank+1}. [{score:.4f}] {ids[idx]}: {titles[idx][:95]}{marker}")
        
        if found: hits += 1
        else: print(f"  ❌ MISS")
        print()
    
    print(f"\n{'='*50}")
    print(f"SCORE: {hits}/{len(TEST_QUERIES)} ({100*hits/len(TEST_QUERIES):.0f}%)")

if __name__ == "__main__":
    main()
