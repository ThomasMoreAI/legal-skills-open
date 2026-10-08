#!/usr/bin/env python3
"""
Test enriched title embeddings vs baseline.
Instead of embedding just the raw title, we embed:
  "Legislación española. {rango}. {título simplificado}"
This gives the embedding model more context about what the document IS.
"""

import struct, os, sys, json, math, re, urllib.request
import numpy as np

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
OPENAI_API = "https://api.openai.com/v1/embeddings"
MODEL = "text-embedding-3-small"
DIMS = 1536
JSON_PATH = os.path.expanduser("~/.boe/index-v1.json")
BIN_PATH = os.path.expanduser("~/.boe/index-v1.bin")

def load_json_index_metadata():
    """Load just metadata from JSON (rango, vigente) - we need this for enrichment."""
    print("Loading JSON index for metadata...", file=sys.stderr)
    with open(JSON_PATH) as f:
        idx = json.load(f)
    meta = {}
    for e in idx["entries"]:
        meta[e["id"]] = {
            "rango": e.get("rango", ""),
            "vigente": e.get("vigente", True),
        }
    return meta

def load_binary_index():
    ids, titles, vectors = [], [], []
    with open(BIN_PATH, "rb") as f:
        magic = f.read(4)
        assert magic == b"BOEI"
        version, dims, count = struct.unpack("<III", f.read(12))
        for _ in range(count):
            id_len = struct.unpack("<I", f.read(4))[0]
            ids.append(f.read(id_len).decode("utf-8"))
            title_len = struct.unpack("<I", f.read(4))[0]
            titles.append(f.read(title_len).decode("utf-8"))
            vec = np.frombuffer(f.read(dims * 4), dtype=np.float32).copy()
            vectors.append(vec)
    matrix = np.stack(vectors)
    norms = np.linalg.norm(matrix, axis=1, keepdims=True)
    norms[norms == 0] = 1
    matrix = matrix / norms
    return ids, titles, matrix

def embed_batch(texts, batch_size=100):
    """Embed texts in batches."""
    all_vecs = []
    for i in range(0, len(texts), batch_size):
        batch = texts[i:i+batch_size]
        payload = json.dumps({"model": MODEL, "input": batch, "dimensions": DIMS}).encode()
        req = urllib.request.Request(OPENAI_API, data=payload, headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {OPENAI_API_KEY}",
        })
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.loads(resp.read())
        sorted_data = sorted(data["data"], key=lambda x: x["index"])
        all_vecs.extend([np.array(d["embedding"], dtype=np.float32) for d in sorted_data])
        print(f"  Embedded {min(i+batch_size, len(texts))}/{len(texts)}", file=sys.stderr)
    return all_vecs

def simplify_title(title):
    """Remove date/number noise from title to get just the subject."""
    # Remove "de X de mes de año" patterns
    t = re.sub(r',?\s*de\s+\d+\s+de\s+\w+\s+de\s+\d{4}', '', title)
    # Remove "número/año" patterns
    t = re.sub(r'\s+\d+/\d{4}', '', t)
    return t.strip()

def extract_subject(title):
    """Extract the 'sobre qué' from the title - the part after 'por el/la que' or 'de' + subject."""
    # Try to find "por el que se..." or "por la que se..."
    m = re.search(r'por (?:el|la) que\s+(.*)', title, re.IGNORECASE)
    if m:
        return m.group(1)[:200]
    # Try "sobre..."
    m = re.search(r'sobre\s+(.*)', title, re.IGNORECASE)
    if m:
        return m.group(1)[:200]
    # Try content after first comma
    parts = title.split(',', 2)
    if len(parts) > 1:
        return parts[-1].strip()[:200]
    return title[:200]

def cosine_search(matrix, query_vec, k=5):
    qn = query_vec / (np.linalg.norm(query_vec) or 1)
    scores = matrix @ qn
    top_k = np.argsort(scores)[::-1][:k]
    return [(float(scores[i]), i) for i in top_k]

TEST_QUERIES = [
    ("puedo echar a mi inquilino", "arrendamiento|inquilino|vivienda|alquiler"),
    ("responsabilidad del administrador", "sociedades|administrador"),
    ("despido improcedente", "trabajador|empleo|estatuto"),
    ("herencia y testamento", "herencia|civil|sucesión|código civil"),
    ("compraventa de empresa", "sociedades|mercantil|modificaciones estructurales"),
    ("pacto de socios", "sociedades|socios|capital"),
    ("fusiones y adquisiciones", "fusión|estructura|modificaciones"),
    ("prescripción de deudas", "prescripción|civil|código"),
    ("contrato de trabajo temporal", "trabajador|empleo|estatuto"),
    ("qué pasa si no pago impuestos", "tributar|general tributaria|sancion"),
    ("puedo montar un negocio online", "comercio electrónico|emprendedor|sociedad"),
    ("cláusula de no competencia", "competencia|laboral|trabajador"),
    ("protección de datos", "datos|privacidad|protección"),
    ("blanqueo de capitales", "blanqueo|prevención"),
    ("ley de sociedades de capital", "sociedades de capital"),
]

def evaluate(search_fn, label, titles):
    hits = 0
    for query, expected_kws in TEST_QUERIES:
        kws = [k.lower() for k in expected_kws.split("|")]
        results = search_fn(query)
        found = any(
            any(kw in titles[idx].lower() for kw in kws)
            for _, idx in results[:5]
        )
        if found: hits += 1
    score = hits / len(TEST_QUERIES) * 100
    print(f"  {label}: {hits}/{len(TEST_QUERIES)} ({score:.0f}%)")
    return hits

def main():
    if not OPENAI_API_KEY:
        print("Set OPENAI_API_KEY", file=sys.stderr); sys.exit(1)

    ids, titles, matrix = load_binary_index()
    print(f"Loaded {len(ids)} entries", file=sys.stderr)
    
    # Baseline with legal prefix
    prefix = "Legislación española, ley, real decreto sobre: "
    query_vecs = {}
    for q, _ in TEST_QUERIES:
        payload = json.dumps({"model": MODEL, "input": prefix + q, "dimensions": DIMS}).encode()
        req = urllib.request.Request(OPENAI_API, data=payload, headers={
            "Content-Type": "application/json", "Authorization": f"Bearer {OPENAI_API_KEY}",
        })
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read())
        query_vecs[q] = np.array(data["data"][0]["embedding"], dtype=np.float32)
    
    print("\n" + "=" * 60)
    print("STRATEGY COMPARISON")
    print("=" * 60)
    
    # Baseline (existing index + prefixed queries)
    evaluate(
        lambda q: cosine_search(matrix, query_vecs[q]),
        "BASELINE + LEGAL PREFIX (current index)", titles
    )
    
    # Now test: what if we re-embed a SAMPLE of titles with enrichment?
    # Take the titles that appear in failed queries + random sample
    # Actually, let's test with a small enriched re-embed
    
    # Strategy: embed "subject extracted from title" alongside full title
    print("\n📊 Testing subject extraction...", file=sys.stderr)
    sample_indices = list(range(min(500, len(titles))))  # first 500 for speed
    
    # Enrichment approach: embed subject + rango instead of full title
    enriched_texts = []
    for i in sample_indices:
        subject = extract_subject(titles[i])
        enriched_texts.append(f"Legislación española. {subject}")
    
    print(f"Re-embedding {len(enriched_texts)} enriched titles...", file=sys.stderr)
    enriched_vecs = embed_batch(enriched_texts)
    enriched_matrix = np.stack(enriched_vecs)
    norms = np.linalg.norm(enriched_matrix, axis=1, keepdims=True)
    norms[norms == 0] = 1
    enriched_matrix = enriched_matrix / norms
    
    # Compare scores for sample
    print("\n📊 Score distribution comparison (sample of 500):", file=sys.stderr)
    sample_titles = [titles[i] for i in sample_indices]
    
    for query, expected_kws in TEST_QUERIES[:5]:
        qvec = query_vecs[query]
        
        # Baseline scores
        qn = qvec / (np.linalg.norm(qvec) or 1)
        base_scores = (matrix[sample_indices] @ qn)
        enr_scores = (enriched_matrix @ qn)
        
        kws = [k.lower() for k in expected_kws.split("|")]
        
        print(f"\n  Query: \"{query}\"")
        print(f"  {'Title':<60} {'Base':>6} {'Enrich':>6}")
        
        # Show top 3 from each
        base_top = np.argsort(base_scores)[::-1][:3]
        enr_top = np.argsort(enr_scores)[::-1][:3]
        
        shown = set()
        for idx in list(base_top) + list(enr_top):
            if idx in shown: continue
            shown.add(idx)
            t = sample_titles[idx][:55]
            match = " ✅" if any(kw in sample_titles[idx].lower() for kw in kws) else ""
            print(f"  {t:<60} {base_scores[idx]:.4f} {enr_scores[idx]:.4f}{match}")

if __name__ == "__main__":
    main()
