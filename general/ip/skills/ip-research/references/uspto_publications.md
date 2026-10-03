# USPTO Publications

Patent and application full-text search via USPTO Patent Public Search (PPUBS).

## Client

```python
from patent_client_agents.uspto_publications import PublicSearchClient
```

No API key required. Use as an async context manager.

## Methods

### search_biblio(**kwargs) -> PublicSearchBiblioPage

Search patents and published applications.

```python
async with PublicSearchClient() as client:
    page = await client.search_biblio(query="machine learning")

    page.num_found        # total result count
    page.per_page         # results per page
    page.page             # current page number

    for doc in page.docs:
        doc.guid
        doc.publication_number
        doc.publication_date
        doc.patent_title
        doc.type              # "US-PGPUB", "USPAT", "USOCR"
        doc.assignee_names
        doc.primary_examiner
        doc.appl_id
```

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `query` | str | required | Search query (PPUBS syntax) |
| `start` | int | 0 | Result offset |
| `limit` | int | 500 | Max results (capped at 500) |
| `sort` | str | "date_publ desc" | Sort order |
| `default_operator` | str | "OR" | Default boolean operator |
| `sources` | list[str] | ["US-PGPUB", "USPAT", "USOCR"] | Databases to search |
| `expand_plurals` | bool | True | Expand plural forms |
| `british_equivalents` | bool | True | Include British spelling variants |

### get_document(guid, source) -> PublicSearchDocument

Fetch full document by GUID and source.

```python
doc = await client.get_document(guid, source="US-PGPUB")

doc.patent_title
doc.publication_number
doc.publication_date
doc.appl_id
doc.app_filing_date

# People
doc.inventors           # list[Inventor] - name, city, state, country
doc.applicants          # list[Applicant]
doc.assignees           # list[Assignee]
doc.primary_examiner
doc.legal_firm_name
doc.attorney_name

# Full text
doc.document.abstract
doc.document.description
doc.document.claims_text
doc.document.claims     # list[Claim] - parsed with dependencies
doc.document.background
doc.document.brief

# Classifications
doc.cpc_inventive       # list[CpcCode]
doc.cpc_additional      # list[CpcCode]
doc.us_class_current

# References
doc.us_references       # list[UsReference]
doc.foreign_references  # list[ForeignReference]
doc.npl_references      # list[NplReference]

# Related applications
doc.related_apps        # list[RelatedApplication]
doc.foreign_priority    # list[ForeignPriorityApplication]
```

### resolve_publication(publication_number) -> PublicSearchDocument

Look up a document by publication number (e.g., "US10123456B2", "US20200012345A1").

```python
doc = await client.resolve_publication("US10123456B2")
```

### download_pdf(document) -> bytes

Download the patent PDF as raw bytes.

```python
doc = await client.resolve_publication("US10123456B2")
pdf_bytes = await client.download_pdf(doc)
Path("patent.pdf").write_bytes(pdf_bytes)
```

### download_pdf_base64(document) -> str

Same as `download_pdf` but returns base64-encoded string.

## Convenience Functions

One-shot functions that create and close a client automatically.

```python
from patent_client_agents.uspto_publications import search, get_document, resolve_publication, download_pdf

page = await search(query="autonomous vehicle")
doc = await get_document(guid, source="USPAT")
doc = await resolve_publication("US10123456B2")
pdf = await download_pdf(publication_number="US10123456B2")  # returns PdfResponse
```

## Key Model Fields

### Claim

| Field | Type | Description |
|-------|------|-------------|
| `number` | int | Claim number |
| `limitations` | list[str] | Claim limitation text |
| `depends_on` | list[int] | Parent claim numbers |
| `text` | property | Full claim text |
| `independent` | property | True if no dependencies |

### PublicSearchBiblio (search result item)

| Field | Type | Description |
|-------|------|-------------|
| `guid` | str | Document GUID (use with `get_document`) |
| `publication_number` | str | e.g., "US10123456B2" |
| `publication_date` | date | Publication date |
| `patent_title` | str | Title |
| `type` | str | Source database |
| `assignee_names` | list[str] | Assignee names |
| `appl_id` | str | Application number |

## Search Query Syntax

Queries use PPUBS field codes. Examples:

```
"machine learning"           # full-text search
AANM/Google                  # assignee name
IN/Smith                     # inventor name
US10123456B2.pn.             # publication number
H04L.cpc.                    # CPC class
20200101->20201231.pd.       # publication date range
TTL/"neural network"         # title search
ACLM/"deep learning"         # claims search
ABST/"image recognition"     # abstract search
```
