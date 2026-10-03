# TMEP (Trademark Manual of Examining Procedure)

Search and retrieve sections of the USPTO TMEP. No API key required.

## Backend

`TmepClient` reads from a local SQLite/FTS5 corpus, not live USPTO.
The corpus must exist before the first call — the wheel ships the
builder, not the data:

```bash
patent-client-agents-build-tmep-corpus \
    --output ~/.cache/patent_client_agents/tmep.db
```

Runtime locates the corpus via `TMEP_CORPUS_PATH` env var, then
`~/.cache/patent_client_agents/tmep.db`. If neither exists, calls raise
`patent_client_agents.tmep.corpus.CorpusUnavailable`.

## Module

```python
from patent_client_agents.tmep import (
    TmepClient,
    SearchInput,
    SectionInput,
    search,
    get_section,
    list_versions,
)
```

## search(params: SearchInput)

Full-text search across the TMEP.

```python
from patent_client_agents.tmep import SearchInput, search

response = await search(SearchInput(
    query="likelihood of confusion 2(d)",
    per_page=10,
    page=1,
))

for hit in response.hits:
    print(hit.section_id, hit.title, hit.snippet)

response.total
response.page
response.per_page
```

## get_section(params: SectionInput | str)

Retrieve the full text of a section by identifier.

```python
from patent_client_agents.tmep import SectionInput, get_section

# Pass a SectionInput
section = await get_section(SectionInput(section_id="1207.01(a)"))

# Or just the section number as a string
section = await get_section("1207")

section.title
section.html
section.plaintext
```

## list_versions()

List available TMEP editions.

```python
versions = await list_versions()
for v in versions:
    print(v.label, v.published_date, v.is_current)
```

## Conventions

- Section identifiers: `"1207"`, `"1207.01(a)"`, `"904.03(i)"`, etc.
- Passing a `client=` argument to any function reuses an existing
  `TmepClient`; otherwise one is created per call and closed on exit.

## Commonly cited sections

| Section | Topic |
|---|---|
| 1207 | Likelihood of confusion (§ 2(d)) refusal |
| 1209 | Refusal on basis of descriptiveness |
| 1212 | Acquired distinctiveness (§ 2(f)) |
| 1213 | Disclaimers |
| 1402 | Identification and classification of goods/services |
| 904 | Specimens |
