#!/usr/bin/env python3
"""
Test different embedding improvement strategies for BOE CLI semantic search.

Strategies:
1. BASELINE: raw title embedding, raw query embedding (current)
2. ENRICHED TITLES: embed "rango: título" instead of just título  
3. QUERY EXPANSION: add "legislación española sobre:" prefix to queries
4. HYBRID: cosine sim + BM25-like keyword score combined
5. INSTRUCTION PREFIX: use "search_query:" / "search_document:" style prefixes
"""

import struct, os, sys, json, math, re, urllib.request
import numpy as np
from collections import Counter

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
OPENAI_API = "https://api.openai.com/v1/embeddings"
MODEL = "text-embedding-3-small"
DIMS = 1536
BIN_PATH = os.path.expanduser("~/.boe/index-v1.bin")

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

def embed_texts(texts):
    """Embed multiple texts in one API call."""
    payload = json.dumps({"model": MODEL, "input": texts, "dimensions": DIMS}).encode()
    req = urllib.request.Request(OPENAI_API, data=payload, headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}",
    })
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.loads(resp.read())
    sorted_data = sorted(data["data"], key=lambda x: x["index"])
    return [np.array(d["embedding"], dtype=np.float32) for d in sorted_data]

def embed_query(text):
    return embed_texts([text])[0]

def cosine_search(matrix, query_vec, k=10):
    qn = query_vec / (np.linalg.norm(query_vec) or 1)
    scores = matrix @ qn
    top_k = np.argsort(scores)[::-1][:k]
    return [(float(scores[i]), i) for i in top_k]

# ===== BM25-like keyword scoring =====
def tokenize(text):
    return re.findall(r'[a-záéíóúüñ]+', text.lower())

def bm25_score(query_tokens, doc_tokens, avg_dl, k1=1.5, b=0.75):
    dl = len(doc_tokens)
    doc_tf = Counter(doc_tokens)
    score = 0.0
    for qt in query_tokens:
        tf = doc_tf.get(qt, 0)
        if tf > 0:
            idf = 1.0  # simplified, all terms equally important
            num = tf * (k1 + 1)
            den = tf + k1 * (1 - b + b * dl / avg_dl)
            score += idf * num / den
    return score

def hybrid_search(matrix, titles, query_vec, query_text, k=10, alpha=0.7):
    """Combine cosine similarity (alpha) with BM25-like keyword score (1-alpha)."""
    qn = query_vec / (np.linalg.norm(query_vec) or 1)
    cos_scores = matrix @ qn
    
    query_tokens = tokenize(query_text)
    title_tokens_list = [tokenize(t) for t in titles]
    avg_dl = np.mean([len(t) for t in title_tokens_list])
    
    bm25_scores = np.array([bm25_score(query_tokens, tt, avg_dl) for tt in title_tokens_list])
    
    # Normalize both to [0,1]
    if cos_scores.max() > cos_scores.min():
        cos_norm = (cos_scores - cos_scores.min()) / (cos_scores.max() - cos_scores.min())
    else:
        cos_norm = cos_scores
    
    if bm25_scores.max() > 0:
        bm25_norm = bm25_scores / bm25_scores.max()
    else:
        bm25_norm = bm25_scores
    
    combined = alpha * cos_norm + (1 - alpha) * bm25_norm
    top_k = np.argsort(combined)[::-1][:k]
    return [(float(combined[i]), i) for i in top_k]

# ===== Query expansion =====
QUERY_PREFIXES = {
    "legal": "Legislación española, ley, real decreto sobre: ",
    "search": "Buscar norma jurídica española relacionada con: ",
}

# ===== Test queries =====
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

def evaluate(search_fn, label, ids, titles, matrix):
    hits = 0
    for query, expected_kws in TEST_QUERIES:
        kws = [k.lower() for k in expected_kws.split("|")]
        results = search_fn(query)
        found = any(
            any(kw in titles[idx].lower() for kw in kws)
            for _, idx in results[:5]
        )
        if found:
            hits += 1
    score = hits / len(TEST_QUERIES) * 100
    print(f"  {label}: {hits}/{len(TEST_QUERIES)} ({score:.0f}%)")
    return hits

def main():
    if not OPENAI_API_KEY:
        print("Set OPENAI_API_KEY", file=sys.stderr); sys.exit(1)
    
    print("Loading index...", file=sys.stderr)
    ids, titles, matrix = load_binary_index()
    print(f"Loaded {len(ids)} entries\n", file=sys.stderr)
    
    # Cache query embeddings to minimize API calls
    all_queries = [q for q, _ in TEST_QUERIES]
    
    print("=" * 60)
    print("STRATEGY COMPARISON — BOE Semantic Search")
    print("=" * 60)
    
    # 1. BASELINE: raw query
    print("\n📊 Embedding queries (baseline)...", file=sys.stderr)
    baseline_vecs = {q: embed_query(q) for q in all_queries}
    evaluate(
        lambda q: cosine_search(matrix, baseline_vecs[q], k=5),
        "BASELINE (raw query → cosine)", ids, titles, matrix
    )
    
    # 2. QUERY PREFIX: "Legislación española sobre:"
    print("📊 Embedding queries (with legal prefix)...", file=sys.stderr)
    prefix = "Legislación española, norma jurídica sobre: "
    prefixed_vecs = {q: embed_query(prefix + q) for q in all_queries}
    evaluate(
        lambda q: cosine_search(matrix, prefixed_vecs[q], k=5),
        "LEGAL PREFIX (prefix + query → cosine)", ids, titles, matrix
    )
    
    # 3. QUERY PREFIX v2: "Buscar ley o real decreto sobre:"
    print("📊 Embedding queries (with search prefix)...", file=sys.stderr)
    prefix2 = "Buscar ley, real decreto, o norma legal española que regule: "
    prefixed2_vecs = {q: embed_query(prefix2 + q) for q in all_queries}
    evaluate(
        lambda q: cosine_search(matrix, prefixed2_vecs[q], k=5),
        "SEARCH PREFIX (search prefix + query → cosine)", ids, titles, matrix
    )
    
    # 4. HYBRID: cosine + BM25
    print("📊 Testing hybrid search (cosine + BM25)...", file=sys.stderr)
    for alpha in [0.8, 0.7, 0.6, 0.5]:
        evaluate(
            lambda q, a=alpha: hybrid_search(matrix, titles, baseline_vecs[q], q, k=5, alpha=a),
            f"HYBRID (α={alpha:.1f} cosine + {1-alpha:.1f} BM25)", ids, titles, matrix
        )
    
    # 5. HYBRID + PREFIX
    print("📊 Testing hybrid + prefix...", file=sys.stderr)
    evaluate(
        lambda q: hybrid_search(matrix, titles, prefixed_vecs[q], q, k=5, alpha=0.7),
        "HYBRID + LEGAL PREFIX (α=0.7)", ids, titles, matrix
    )
    evaluate(
        lambda q: hybrid_search(matrix, titles, prefixed2_vecs[q], q, k=5, alpha=0.7),
        "HYBRID + SEARCH PREFIX (α=0.7)", ids, titles, matrix
    )

    # 6. Show the hardest queries - what STILL fails
    print("\n\n" + "=" * 60)
    print("DETAILED FAILURES — Best strategy results")
    print("=" * 60)
    
    for query, expected_kws in TEST_QUERIES:
        kws = [k.lower() for k in expected_kws.split("|")]
        results = hybrid_search(matrix, titles, prefixed_vecs[query], query, k=5, alpha=0.7)
        found = any(any(kw in titles[idx].lower() for kw in kws) for _, idx in results[:5])
        if not found:
            print(f"\n❌ \"{query}\" (expect: {expected_kws})")
            for rank, (score, idx) in enumerate(results[:5]):
                print(f"   {rank+1}. [{score:.4f}] {titles[idx][:100]}")

if __name__ == "__main__":
    main()
