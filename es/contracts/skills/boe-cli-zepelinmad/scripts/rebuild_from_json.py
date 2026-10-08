#!/usr/bin/env python3
"""
Rebuild enriched index from existing JSON index (skip BOE API download).
"""

import json, os, struct, sys, time, urllib.request, urllib.error, re

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
OPENAI_API = "https://api.openai.com/v1/embeddings"
MODEL = "text-embedding-3-small"
DIMENSIONS = 1536
BATCH_SIZE = 100
INDEX_DIR = os.path.expanduser("~/.boe")

# Import enrichment data
sys.path.insert(0, os.path.dirname(__file__))
from build_enriched_index import LAW_DESCRIPTIONS, enrich_title

def embed_batch(texts):
    payload = json.dumps({"model": MODEL, "input": texts, "dimensions": DIMENSIONS}).encode()
    req = urllib.request.Request(OPENAI_API, data=payload, headers={
        "Content-Type": "application/json", "Authorization": f"Bearer {OPENAI_API_KEY}",
    })
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.loads(resp.read())
    return [e["embedding"] for e in sorted(data["data"], key=lambda x: x["index"])]

def main():
    if not OPENAI_API_KEY:
        print("❌ Set OPENAI_API_KEY", file=sys.stderr); sys.exit(1)
    
    # Load existing JSON index (has all entries)
    json_path = os.path.join(INDEX_DIR, "index-v1.json")
    print(f"📥 Loading existing index from {json_path}...")
    with open(json_path) as f:
        idx = json.load(f)
    
    entries = idx["entries"]
    print(f"   {len(entries)} entries loaded")
    
    # Enrich
    print(f"\n📝 Enriching titles ({len(LAW_DESCRIPTIONS)} manual descriptions)...")
    enriched_texts = []
    manual = 0
    for e in entries:
        enriched = enrich_title(e)
        enriched_texts.append(enriched)
        if e["id"] in LAW_DESCRIPTIONS:
            manual += 1
    print(f"   {manual} manually described")
    
    # Show examples
    for eid in ["BOE-A-1995-25444", "BOE-A-2010-10544", "BOE-A-1889-4763"]:
        for i, e in enumerate(entries):
            if e["id"] == eid:
                print(f"\n  [{eid}]")
                print(f"  Original: {e['title'][:90]}...")
                print(f"  Enriched: {enriched_texts[i][:150]}...")
                break
    
    # Re-embed with enriched texts
    print(f"\n🧠 Generating enriched embeddings...")
    total = len(entries)
    for i in range(0, total, BATCH_SIZE):
        batch = enriched_texts[i:i+BATCH_SIZE]
        try:
            vectors = embed_batch(batch)
            for j, vec in enumerate(vectors):
                entries[i+j]["vector"] = vec
        except urllib.error.HTTPError as e:
            print(f"  ⚠️ Error batch {i}: {e.code}", file=sys.stderr)
            time.sleep(5)
            try:
                vectors = embed_batch(batch)
                for j, vec in enumerate(vectors):
                    entries[i+j]["vector"] = vec
            except:
                for j in range(len(batch)):
                    entries[i+j]["vector"] = None
        
        done = min(i+BATCH_SIZE, total)
        if done % 1000 == 0 or done == total:
            print(f"  ... {done}/{total}")
        time.sleep(0.3)
    
    # Save v2 binary
    valid = [e for e in entries if e.get("vector") is not None]
    bin_path = os.path.join(INDEX_DIR, "index-v2.bin")
    with open(bin_path, "wb") as f:
        f.write(b"BOEI")
        f.write(struct.pack("<I", 2))  # version 2
        f.write(struct.pack("<I", DIMENSIONS))
        f.write(struct.pack("<I", len(valid)))
        for e in valid:
            id_b = e["id"].encode()
            f.write(struct.pack("<I", len(id_b)))
            f.write(id_b)
            t_b = e["title"].encode()
            f.write(struct.pack("<I", len(t_b)))
            f.write(t_b)
            f.write(struct.pack(f"<{DIMENSIONS}f", *e["vector"]))
    
    sz = os.path.getsize(bin_path) / (1024*1024)
    print(f"\n💾 Saved {bin_path} ({sz:.1f} MB, {len(valid)} entries)")
    print("🎉 Done!")

if __name__ == "__main__":
    main()
