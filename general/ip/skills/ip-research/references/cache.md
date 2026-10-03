# Cache Management

All clients cache HTTP responses to `~/.cache/patent_client_agents/`.

## Configuration

### TTL (Time-To-Live)

Set default expiration for cache entries:

```python
from patent_client_agents.google_patents import GooglePatentsClient

async with GooglePatentsClient(ttl_seconds=3600) as client:  # 1 hour TTL
    patent = await client.get_patent_data("US10123456B2")
```

Default: Uses HTTP cache headers from server.

### Disable Caching

```python
async with GooglePatentsClient(use_cache=False) as client:
    patent = await client.get_patent_data("US10123456B2")  # Always fetches
```

## Cache APIs

All clients expose these methods when caching is enabled:

### cache_stats() -> CacheStats

Get cache statistics.

```python
async with GooglePatentsClient() as client:
    # Make some requests...

    stats = await client.cache_stats()
    stats.hits           # Number of cache hits
    stats.misses         # Number of cache misses
    stats.hit_rate       # Hit rate percentage (0-100)
    stats.entry_count    # Number of cached entries
    stats.size_bytes     # Cache size in bytes
    stats.size_mb        # Cache size in MB
    stats.database_path  # Path to cache database
```

### cache_clear() -> int

Clear all cached entries. Returns count of entries cleared.

```python
cleared = await client.cache_clear()
print(f"Cleared {cleared} entries")
```

### cache_clear_expired(max_age) -> int

Clear entries older than max_age.

```python
from datetime import timedelta

# Clear entries older than 1 hour
cleared = await client.cache_clear_expired(max_age=timedelta(hours=1))

# Clear entries older than 7 days
cleared = await client.cache_clear_expired(max_age=timedelta(days=7))
```

Default max_age: TTL if set, otherwise 24 hours.

### cache_invalidate(pattern) -> int

Invalidate entries matching a URL regex pattern.

```python
# Invalidate all Google Patents entries
cleared = await client.cache_invalidate(r"patents\.google\.com")

# Invalidate specific patent
cleared = await client.cache_invalidate(r"US10123456")

# Invalidate all search results
cleared = await client.cache_invalidate(r"/search\?")
```

### cache_enabled -> bool

Check if caching is enabled.

```python
if client.cache_enabled:
    stats = await client.cache_stats()
```

## Cache Files

Each client has its own cache database:

```
~/.cache/patent_client_agents/
├── google_patents.db
├── uspto_odp.db
├── uspto_publications.db
├── uspto_assignments.db
├── epo_ops.db
└── jpo.db
```

To clear all caches: `rm -rf ~/.cache/patent_client_agents/`
