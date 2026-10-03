# MPEP (Manual of Patent Examining Procedure)

Search and retrieve sections of the USPTO MPEP. No API key required.

## Backend

`MpepClient` reads from a local SQLite/FTS5 corpus, not live USPTO.
The corpus must exist before the first call — the wheel ships the
builder, not the data:

```bash
patent-client-agents-build-mpep-corpus \
    --output ~/.cache/patent_client_agents/mpep.db
```

Runtime locates the corpus via `MPEP_CORPUS_PATH` env var, then
`~/.cache/patent_client_agents/mpep.db`. If neither exists, calls raise
`patent_client_agents.mpep.corpus.CorpusUnavailable`.

## Module

```python
from patent_client_agents.mpep import SearchInput, SectionInput, search, get_section, list_versions
```

## search(params: SearchInput)

Full-text search across the MPEP.

```python
from patent_client_agents.mpep import SearchInput, search

response = await search(SearchInput(
    query="obviousness rejection",
    per_page=10,
    page=1,
))

for hit in response.hits:
    print(hit.section_id, hit.title, hit.snippet)

response.total       # total matches
response.page
response.per_page
```

## get_section(params: SectionInput)

Retrieve the full text of a section by identifier.

```python
from patent_client_agents.mpep import SectionInput, get_section

section = await get_section(SectionInput(section_id="2141", version="latest"))
section.title
section.html
section.plaintext
```

## list_versions()

List available MPEP revisions (R-10.2019, R-11.2023, etc.).

```python
versions = await list_versions()
for v in versions:
    print(v.label, v.published_date, v.is_current)
```

## Conventions

- Section identifiers: `"2106"`, `"2141"`, `"608.01(n)"`, etc.
- Passing a `client=` argument to any function reuses an existing `MpepClient`;
  otherwise one is created per call and closed on exit.
