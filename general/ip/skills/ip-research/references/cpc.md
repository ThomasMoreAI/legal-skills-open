# CPC Classification

Cooperative Patent Classification lookups, keyword search, and cross-scheme
mapping. Backed by EPO OPS, so requires `EPO_OPS_API_KEY` + `EPO_OPS_API_SECRET`.

## Module

```python
from patent_client_agents.cpc import retrieve_cpc, search_cpc, map_classification, fetch_media
```

## retrieve_cpc(symbol, *, depth=None, ancestors=False, navigation=False)

Look up a CPC entry.

```python
from patent_client_agents.cpc import retrieve_cpc

entry = await retrieve_cpc(symbol="H04L63/08", ancestors=True)
entry.symbol        # "H04L63/08"
entry.title         # "... for supporting authentication of entities..."
entry.ancestors     # populated when ancestors=True
```

- `depth`: levels of descendants to include (int or `"all"`)
- `ancestors`: include ancestor chain
- `navigation`: include navigation tree

## search_cpc(query, *, limit=25)

Free-text search across CPC titles.

```python
results = await search_cpc(query="neural network", limit=10)
for hit in results.entries:
    print(hit.symbol, hit.title)
```

## map_classification(symbol, *, to="IPC")

Map CPC ↔ IPC / ECLA.

```python
mapping = await map_classification(symbol="H04L63/08", to="IPC")
```

## fetch_media(media_id, *, accept="image/png")

Download figures or diagrams referenced from CPC entries.

## fetch_biblio_cpci(...)

Fetch biblio data using CPC-indexed classification metadata.

See `patent_client_agents.cpc.api` docstrings for full signatures.
