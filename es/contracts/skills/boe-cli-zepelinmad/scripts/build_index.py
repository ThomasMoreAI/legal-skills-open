#!/usr/bin/env python3
"""
Build semantic search index for BOE CLI.
Downloads all consolidated legislation titles and generates embeddings.
"""

import json
import os
import struct
import sys
import time
import urllib.request
import urllib.error

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
BOE_API = "https://www.boe.es/datosabiertos/api/legislacion-consolidada"
OPENAI_API = "https://api.openai.com/v1/embeddings"
MODEL = "text-embedding-3-small"
DIMENSIONS = 1536
BATCH_SIZE = 100  # OpenAI supports up to 2048 inputs per batch
PAGE_SIZE = 50
INDEX_DIR = os.path.expanduser("~/.boe")
INDEX_PATH = os.path.join(INDEX_DIR, "index-v1.json")  # JSON for portability

def fetch_page(offset):
    """Fetch a page of legislation from BOE API."""
    url = f"{BOE_API}?limit={PAGE_SIZE}&offset={offset}"
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read())
            return data.get("data", [])
    except Exception as e:
        print(f"  ⚠️  Error at offset {offset}: {e}", file=sys.stderr)
        return []

def fetch_all_titles():
    """Download all legislation entries from BOE API."""
    entries = []
    offset = 0
    print("📥 Descargando títulos del BOE...")
    
    while True:
        page = fetch_page(offset)
        if not page:
            break
        
        for item in page:
            entries.append({
                "id": item.get("identificador", ""),
                "title": item.get("titulo", ""),
                "rango": item.get("rango", {}).get("texto", "") if isinstance(item.get("rango"), dict) else "",
                "date": item.get("fecha_publicacion", ""),
                "vigente": item.get("vigencia_agotada", "N") != "S",
            })
        
        offset += PAGE_SIZE
        if offset % 500 == 0:
            print(f"  ... {offset} entries downloaded")
        
        # Small delay to be nice to the API
        time.sleep(0.1)
    
    print(f"✅ {len(entries)} entries downloaded")
    return entries

def embed_batch(texts):
    """Embed a batch of texts using OpenAI API."""
    payload = json.dumps({
        "model": MODEL,
        "input": texts,
        "dimensions": DIMENSIONS,
    }).encode("utf-8")
    
    req = urllib.request.Request(
        OPENAI_API,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {OPENAI_API_KEY}",
        },
    )
    
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.loads(resp.read())
    
    # Sort by index to maintain order
    embeddings = sorted(data["data"], key=lambda x: x["index"])
    return [e["embedding"] for e in embeddings]

def embed_all(entries):
    """Generate embeddings for all entries in batches."""
    print(f"\n🧠 Generando embeddings ({MODEL}, {DIMENSIONS} dims)...")
    print(f"   {len(entries)} títulos, {(len(entries) + BATCH_SIZE - 1) // BATCH_SIZE} batches")
    
    total_tokens = 0
    
    for i in range(0, len(entries), BATCH_SIZE):
        batch = entries[i:i + BATCH_SIZE]
        texts = [e["title"] for e in batch]
        
        try:
            vectors = embed_batch(texts)
            for j, vec in enumerate(vectors):
                entries[i + j]["vector"] = vec
            
            done = min(i + BATCH_SIZE, len(entries))
            print(f"  ... {done}/{len(entries)} embedded")
            
        except urllib.error.HTTPError as e:
            body = e.read().decode()
            print(f"  ⚠️  Error at batch {i}: {e.code} {body[:200]}", file=sys.stderr)
            # Retry once after delay
            time.sleep(5)
            try:
                vectors = embed_batch(texts)
                for j, vec in enumerate(vectors):
                    entries[i + j]["vector"] = vec
                print(f"  ... {min(i + BATCH_SIZE, len(entries))}/{len(entries)} embedded (retry OK)")
            except Exception as e2:
                print(f"  ❌ Retry failed: {e2}", file=sys.stderr)
                # Mark these entries as failed
                for j in range(len(batch)):
                    entries[i + j]["vector"] = None
        
        # Rate limiting: max 3000 RPM for embedding API
        time.sleep(0.3)
    
    # Count successes
    success = sum(1 for e in entries if e.get("vector") is not None)
    print(f"✅ {success}/{len(entries)} embeddings generated")
    return entries

def save_index(entries):
    """Save the index to disk."""
    os.makedirs(INDEX_DIR, exist_ok=True)
    
    # Filter out failed embeddings
    valid = [e for e in entries if e.get("vector") is not None]
    
    index = {
        "model": MODEL,
        "dimensions": DIMENSIONS,
        "created_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "count": len(valid),
        "entries": valid,
    }
    
    # Save as JSON (readable, portable)
    with open(INDEX_PATH, "w") as f:
        json.dump(index, f, separators=(",", ":"))  # compact
    
    size_mb = os.path.getsize(INDEX_PATH) / (1024 * 1024)
    print(f"\n💾 Index saved to {INDEX_PATH} ({size_mb:.1f} MB)")
    print(f"   {len(valid)} entries, {DIMENSIONS} dimensions")
    
    # Also save a binary version for Go (much smaller)
    bin_path = os.path.join(INDEX_DIR, "index-v1.bin")
    save_binary_index(valid, bin_path)

def save_binary_index(entries, path):
    """Save a compact binary index for Go consumption.
    
    Format:
    - Header: 4 bytes magic "BOEI", 4 bytes version, 4 bytes dimensions, 4 bytes count
    - For each entry:
      - 4 bytes id_len, id_bytes
      - 4 bytes title_len, title_bytes
      - dimensions * 4 bytes (float32 vector)
    """
    with open(path, "wb") as f:
        # Header
        f.write(b"BOEI")  # magic
        f.write(struct.pack("<I", 1))  # version
        f.write(struct.pack("<I", DIMENSIONS))  # dimensions
        f.write(struct.pack("<I", len(entries)))  # count
        
        for e in entries:
            # ID
            id_bytes = e["id"].encode("utf-8")
            f.write(struct.pack("<I", len(id_bytes)))
            f.write(id_bytes)
            
            # Title
            title_bytes = e["title"].encode("utf-8")
            f.write(struct.pack("<I", len(title_bytes)))
            f.write(title_bytes)
            
            # Vector (float32)
            vec = e["vector"]
            f.write(struct.pack(f"<{len(vec)}f", *vec))
    
    size_mb = os.path.getsize(path) / (1024 * 1024)
    print(f"💾 Binary index saved to {path} ({size_mb:.1f} MB)")

def main():
    if not OPENAI_API_KEY:
        print("❌ Set OPENAI_API_KEY environment variable", file=sys.stderr)
        sys.exit(1)
    
    print("🏛️  BOE Semantic Index Builder")
    print(f"   Model: {MODEL} ({DIMENSIONS} dims)")
    print()
    
    # Step 1: Download all titles
    entries = fetch_all_titles()
    if not entries:
        print("❌ No entries downloaded", file=sys.stderr)
        sys.exit(1)
    
    # Step 2: Generate embeddings
    entries = embed_all(entries)
    
    # Step 3: Save index
    save_index(entries)
    
    print("\n🎉 Done!")

if __name__ == "__main__":
    main()
