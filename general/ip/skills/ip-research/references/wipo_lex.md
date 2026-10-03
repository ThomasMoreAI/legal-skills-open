# WIPO Lex (global IP statute database)

Search and retrieve IP laws, regulations, treaties, and judgments curated by WIPO across ~200 jurisdictions in six UN languages. No API key required.

v0.9 scope is the **legislation** collection (search + per-entry detail with downloadable file links). Treaties and judgments share the same URL shape and are planned follow-ups.

## Module

```python
from patent_client_agents.wipo_lex import (
    GetLegislationInput,
    SearchLegislationInput,
    SubjectMatter,
    TypeOfText,
    WipoLexClient,
    get_legislation,
    search_legislation,
)
```

## search_legislation(params: SearchLegislationInput)

Search the legislation collection. Returns hits with `legislation_id` + display title. Use `get_legislation` to follow the ID into the detail page.

```python
from patent_client_agents.wipo_lex import (
    SearchLegislationInput, SubjectMatter, TypeOfText, search_legislation,
)

# Canadian main patent laws
results = await search_legislation(SearchLegislationInput(
    country_codes=["CA"],
    subject_matter=[SubjectMatter.PATENTS],
    type_of_text=[TypeOfText.MAIN_IP_LAWS],
))
for hit in results.hits:
    print(hit.legislation_id, hit.title)
```

## get_legislation(params: GetLegislationInput | str | int)

Fetch metadata + downloadable file links for a single entry. The bare-ID form is supported as a convenience.

```python
from patent_client_agents.wipo_lex import get_legislation

# Canadian Patent Act
detail = await get_legislation("23293")
detail.title, detail.jurisdiction, detail.summary
for f in detail.files:
    print(f.label, f.mime_type, f.url)
```

## Filter codes

`SubjectMatter`:

| Code | Subject |
|---|---|
| 1 | Patents |
| 2 | Utility Models |
| 3 | Industrial Designs |
| 4 | Trademarks |
| 5 | Geographical Indications |
| 9 | Trade Secrets |
| 10 | Plant Variety Protection |
| 11 | Copyright |
| 12 | Enforcement |

Full list of 21 codes on `patent_client_agents.wipo_lex.SubjectMatter`.

`TypeOfText`:

| Code | Type |
|---|---|
| 205 | Main IP Laws |
| 207 | Implementing Rules |
| 210 | IP-related Laws |
| 213 | Framework Laws |
| 214 | Other Texts |
| 215 | National IP Strategy |

## Common examples

```python
# Trade-secret statutes globally
trade_secrets = await search_legislation(
    SearchLegislationInput(subject_matter=[SubjectMatter.TRADE_SECRETS])
)

# UK IP enforcement
uk_enforce = await search_legislation(SearchLegislationInput(
    country_codes=["GB"],
    subject_matter=[SubjectMatter.ENFORCEMENT],
))

# Pull the 35 U.S.C. PDF link
us_patents = await get_legislation("21466")
print(us_patents.files[0].url)  # https://wipolex-res.wipo.int/.../us...en.pdf
```

## Stability and ToS

- HTML-parsed surface (no documented WIPO JSON API); parser keys on OpenGraph meta tags + file-extension substring matching.
- No documented numeric rate limits; client uses a polite User-Agent and caches aggressively.
- All content is curated by WIPO and translated into the six UN languages; the native text always controls.
