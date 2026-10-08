# Semantic Search Design — BOE CLI

## Overview

Add vector similarity search so any natural language query finds relevant legislation,
even when there's no keyword overlap with the title.

Example: "¿puedo echar a mi inquilino?" → Ley de Arrendamientos Urbanos

## Architecture

```
┌──────────────────────────────────────────────────┐
│                  BOE CLI (Go)                     │
│                                                   │
│  User Query → [1] Aliases → [2] Fuzzy → [3] API  │
│                         ↓ (if no match)           │
│              [4] Semantic Search                   │
│                   ↓                                │
│         Embed query via HTTP                       │
│         Cosine similarity vs index                 │
│         Return top-K titles                        │
└──────────┬───────────────────────────────────────┘
           │
           ▼
┌─────────────────────────┐
│  Embedding Index File    │
│  (~12K entries)          │
│                          │
│  Format: binary/gob      │
│  - ID: string            │
│  - Title: string         │
│  - Vector: []float32     │
│  (~12K × 1536 dims       │
│   = ~71 MB float32       │
│   or ~18 MB int8 quant)  │
└─────────────────────────┘

┌─────────────────────────┐
│  Embedding API           │
│  (at query time only)    │
│                          │
│  Options:                │
│  A) OpenAI API directly  │
│  B) Firmwork AI Gateway  │
│  C) Local model (onnx)   │
└─────────────────────────┘
```

## Index Building (one-time, CLI command)

```bash
# Build the index by downloading all titles and embedding them
boe index build --api-key $OPENAI_API_KEY

# Or with a custom endpoint (Firmwork AI Gateway)
boe index build --endpoint https://api.firmwork.ai/v1 --api-key $KEY --model text-embedding-3-small

# Index stored at: ~/.boe/semantic-index.gob (or .bin)
```

### Build Process

1. Paginate through BOE API: `GET /legislacion-consolidada?limit=50&offset=N`
2. Collect all ~12,228 entries: `{id, titulo, rango, fecha, vigencia_agotada}`
3. Batch embed titles via OpenAI API (50/batch, ~245 batches)
4. Write index file to `~/.boe/semantic-index.gob`

### Cost Estimate

- ~12K titles, avg ~100 chars each = ~1.2M chars = ~300K tokens
- OpenAI text-embedding-3-small: $0.02/1M tokens
- **Total: ~$0.006** (less than 1 cent!)
- Build time: ~5 min (API rate limits)

## Query Time

```
User: "puedo echar a mi inquilino"
  ↓
[1-3] No alias/fuzzy/API match
  ↓
[4] Embed query string → 1536-dim vector
  ↓
Cosine similarity against 12K stored vectors
  ↓
Top 10 results by similarity score
  ↓
Merge with title/texto API results, rerank
```

### Query Embedding Options

**Option A: OpenAI API (recommended for start)**
- Requires API key (env var or config file)
- ~100ms latency per query
- $0.00002 per query (negligible)

**Option B: Firmwork AI Gateway**
- Route through Firmwork's OpenAI-compatible proxy
- Same latency/cost, but centralized key management

**Option C: Local ONNX model (no API dependency)**
- Bundle a small embedding model (e.g., all-MiniLM-L6-v2, ~80MB)
- Run inference locally via ONNX Runtime Go bindings
- 0 cost, ~50ms latency, but larger binary
- Could offer as optional: `boe index build --local`

## Go Implementation Plan

### New files

```
internal/semantic/
├── index.go          # Index struct, Load/Save, Search
├── embed.go          # Embedding API client (OpenAI-compatible)
├── cosine.go         # Cosine similarity, top-K
└── build.go          # Index builder (paginate BOE + batch embed)

cmd/
├── index.go          # `boe index build` / `boe index info` commands
```

### Key types

```go
// IndexEntry is a single law in the semantic index
type IndexEntry struct {
    ID      string
    Title   string
    Rango   string
    Date    string
    Vigente bool
    Vector  []float32  // embedding vector
}

// SemanticIndex is the searchable index
type SemanticIndex struct {
    Model      string        // e.g. "text-embedding-3-small"
    Dimensions int           // e.g. 1536
    CreatedAt  time.Time
    Entries    []IndexEntry
}

// Search returns top-K results by cosine similarity
func (idx *SemanticIndex) Search(queryVector []float32, k int) []SearchResult
```

### Index file format

Use Go's `encoding/gob` for the index file. Simple, fast, Go-native.
Alternative: flatbuffers or protobuf for cross-language compatibility.

Store at: `~/.boe/index-v1.gob` (versioned for future schema changes)

## Integration with SmartSearch

```go
func (c *Client) SmartSearch(query string, limit int) ([]SearchResultItem, string, error) {
    // Steps 1-5: aliases, synonyms, fuzzy, partial, field syntax (existing)
    
    // Step 6: Semantic search (if index loaded and API key available)
    if c.semanticIndex != nil && c.embeddingEndpoint != "" {
        queryVec, err := c.embedQuery(query)
        if err == nil {
            semanticResults := c.semanticIndex.Search(queryVec, limit)
            // Convert to SearchResultItem, merge with title/texto results
            // Semantic results get Score bonus of +70
        }
    }
    
    // Steps 7+: title search, texto search, merge, rerank (existing)
}
```

## Configuration

```toml
# ~/.boe/config.toml (optional)
[embedding]
endpoint = "https://api.openai.com/v1"  # or Firmwork gateway
model = "text-embedding-3-small"
# api_key via env var OPENAI_API_KEY or BOE_EMBEDDING_KEY
```

## Distribution

The semantic index is NOT bundled in the Go binary (it's 18-71 MB).
Instead:

1. User installs `boe` (Go binary, <10 MB)
2. User runs `boe index build` to generate index locally
3. Index cached at `~/.boe/index-v1.gob`
4. Optional: host pre-built index on GitHub Releases for quick download
   `boe index download` — fetches latest pre-built index

## Performance

- Index load: ~200ms (12K entries from gob)
- Query embedding: ~100ms (API call)
- Cosine similarity search: <5ms (12K × 1536 brute force)
- **Total semantic search: ~300ms** (acceptable for CLI)

For comparison:
- Alias lookup: <1ms
- Fuzzy match: ~5ms
- BOE API search: ~500ms

## Incremental Updates

```bash
# Update index with new/changed laws since last build
boe index update

# Check index age
boe index info
```

Compare local index timestamp with BOE API's latest publication date.
Only re-embed entries that changed.

## Security

- API keys stored in env vars or `~/.boe/config.toml` (chmod 600)
- Index file contains only public BOE data (no secrets)
- Embedding API calls contain only law titles (public info)

## Future: Full-Text Semantic Search

Phase 2 could embed article text (not just titles), enabling:
- "artículo sobre responsabilidad del administrador" → LSC art. 236
- "prescripción de acciones tributarias" → LGT art. 66

This would require a much larger index (~100K+ chunks) and likely
a vector DB (sqlite-vec, Qdrant, or similar).

---

*Estimated implementation time: 2-3 days for basic semantic search*
*Cost: <$0.01 for initial index build*
