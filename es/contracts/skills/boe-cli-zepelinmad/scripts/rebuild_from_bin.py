#!/usr/bin/env python3
"""
Rebuild enriched index from existing BINARY index (fast load, skip JSON).
Reads v1 binary, enriches titles, re-embeds, saves as v2.
"""

import os, struct, sys, json, time, urllib.request, urllib.error

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
OPENAI_API = "https://api.openai.com/v1/embeddings"
MODEL = "text-embedding-3-small"
DIMS = 1536
BATCH_SIZE = 100
INDEX_DIR = os.path.expanduser("~/.boe")
BIN_V1 = os.path.join(INDEX_DIR, "index-v1.bin")
BIN_V2 = os.path.join(INDEX_DIR, "index-v2.bin")

sys.path.insert(0, os.path.dirname(__file__))
from build_enriched_index import LAW_DESCRIPTIONS, enrich_title

def load_binary_entries(path):
    """Load entries from binary index (skip vectors — we'll re-embed)."""
    entries = []
    with open(path, "rb") as f:
        magic = f.read(4)
        assert magic == b"BOEI", f"Bad magic: {magic}"
        version, dims, count = struct.unpack("<III", f.read(12))
        print(f"  Reading v{version}: {count} entries, {dims} dims")
        for _ in range(count):
            id_len = struct.unpack("<I", f.read(4))[0]
            eid = f.read(id_len).decode()
            title_len = struct.unpack("<I", f.read(4))[0]
            title = f.read(title_len).decode()
            f.seek(dims * 4, 1)  # SKIP vector — we don't need it
            entries.append({"id": eid, "title": title})
    return entries

def embed_batch(texts):
    payload = json.dumps({"model": MODEL, "input": texts, "dimensions": DIMS}).encode()
    req = urllib.request.Request(OPENAI_API, data=payload, headers={
        "Content-Type": "application/json", "Authorization": f"Bearer {OPENAI_API_KEY}",
    })
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.loads(resp.read())
    return [e["embedding"] for e in sorted(data["data"], key=lambda x: x["index"])]

def main():
    if not OPENAI_API_KEY:
        print("❌ Set OPENAI_API_KEY", file=sys.stderr); sys.exit(1)
    
    print("🏛️  BOE Enriched Index Builder v2 (from binary)")
    
    # Load entries (fast — skips vectors)
    print(f"📥 Loading entries from {BIN_V1}...")
    entries = load_binary_entries(BIN_V1)
    print(f"   {len(entries)} entries loaded\n")
    
    # Enrich
    print(f"📝 Enriching ({len(LAW_DESCRIPTIONS)} manual descriptions)...")
    enriched = []
    manual = 0
    for e in entries:
        txt = enrich_title(e)
        enriched.append(txt)
        if e["id"] in LAW_DESCRIPTIONS:
            manual += 1
    print(f"   {manual} with rich descriptions\n")
    
    # Examples
    for eid in ["BOE-A-1995-25444", "BOE-A-2010-10544", "BOE-A-1889-4763"]:
        for i, e in enumerate(entries):
            if e["id"] == eid:
                print(f"  [{eid}]")
                print(f"  → {enriched[i][:150]}...\n")
                break
    
    # Re-embed
    print(f"🧠 Embedding {len(entries)} enriched texts...")
    vectors = [None] * len(entries)
    for i in range(0, len(entries), BATCH_SIZE):
        batch = enriched[i:i+BATCH_SIZE]
        retries = 0
        while retries < 3:
            try:
                vecs = embed_batch(batch)
                for j, v in enumerate(vecs):
                    vectors[i+j] = v
                break
            except Exception as ex:
                retries += 1
                print(f"  ⚠️ Batch {i} error (retry {retries}): {ex}", file=sys.stderr)
                time.sleep(2 * retries)
        
        done = min(i+BATCH_SIZE, len(entries))
        if done % 500 == 0 or done == len(entries):
            print(f"  ... {done}/{len(entries)}")
        time.sleep(0.25)
    
    valid_count = sum(1 for v in vectors if v is not None)
    print(f"✅ {valid_count}/{len(entries)} embedded\n")
    
    # Save v2
    print(f"💾 Saving to {BIN_V2}...")
    with open(BIN_V2, "wb") as f:
        f.write(b"BOEI")
        f.write(struct.pack("<I", 2))
        f.write(struct.pack("<I", DIMS))
        # Count valid
        valid_entries = [(entries[i], vectors[i]) for i in range(len(entries)) if vectors[i] is not None]
        f.write(struct.pack("<I", len(valid_entries)))
        for e, vec in valid_entries:
            id_b = e["id"].encode()
            f.write(struct.pack("<I", len(id_b)))
            f.write(id_b)
            t_b = e["title"].encode()
            f.write(struct.pack("<I", len(t_b)))
            f.write(t_b)
            f.write(struct.pack(f"<{DIMS}f", *vec))
    
    sz = os.path.getsize(BIN_V2) / (1024*1024)
    print(f"   {sz:.1f} MB, {len(valid_entries)} entries")
    print("\n🎉 Done! Now test:")
    print(f"   python3 scripts/test_semantic_np.py --index {BIN_V2}")

if __name__ == "__main__":
    main()
