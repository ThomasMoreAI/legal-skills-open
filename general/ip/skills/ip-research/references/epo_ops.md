# EPO OPS

European Patent Office Open Patent Services API.

**Required**: `EPO_OPS_API_KEY` and `EPO_OPS_API_SECRET` environment variables.

## Client

```python
from patent_client_agents.epo_ops import EpoOpsClient, client_from_env

# From environment variables
async with client_from_env() as client:
    ...

# Or explicit credentials
async with EpoOpsClient(api_key="...", api_secret="...") as client:
    ...
```

## Methods

### search_published(query, range) -> SearchResponse

Search published documents using CQL.

```python
async with client_from_env() as client:
    results = await client.search_published(
        query='ta="machine learning" and pd>=2020',
        range="1-25"
    )

    for doc in results.documents:
        doc.doc_number
        doc.country
        doc.kind
        doc.family_id
```

### search_families(query, range) -> SearchResponse

Search grouped by patent family.

```python
results = await client.search_families(
    query='applicant="Google"',
    range="1-25"
)
```

### fetch_biblio(doc_id) -> BiblioResponse

Get bibliographic data.

```python
biblio = await client.fetch_biblio("EP1234567A1")
biblio.title
biblio.abstract
biblio.applicants
biblio.inventors
biblio.classifications
biblio.priorities
biblio.publication_date
biblio.filing_date
```

### fetch_citations(number) -> CitationResponse

Get backward citations recorded in EPO bibliographic data. Patent citations
include a canonical `docdb` identifier when available. Search-report category,
cited phase, relevant claims, passages, and non-patent literature are retained.

```python
citations = await client.fetch_citations(number="EP1234567A1")
for citation in citations.citations:
    citation.patent_document
    citation.non_patent_literature
    citation.categories
    citation.relevant_claims
    citation.passages
```

### fetch_equivalents(number) -> EquivalentsResponse

Get simple-family publications carrying the same technical disclosure. This is
distinct from the broader priority-linked INPADOC family returned by
`fetch_family`.

```python
equivalents = await client.fetch_equivalents(number="EP1234567A1")
for publication in equivalents.equivalents:
    publication.country
    publication.doc_number
    publication.kind
```

### fetch_fulltext(doc_id, part) -> FullTextResponse

Get claims or description.

```python
# Get claims
claims = await client.fetch_fulltext("EP1234567A1", "claims")
for claim in claims.claims:
    claim.number
    claim.text
    claim.dependencies

# Get description
desc = await client.fetch_fulltext("EP1234567A1", "description")
desc.text
```

### fetch_family(doc_id) -> FamilyResponse

Get patent family members.

```python
family = await client.fetch_family("EP1234567A1")
for member in family.members:
    member.doc_number
    member.country
    member.kind
    member.publication_date
```

### fetch_legal_events(doc_id) -> LegalEventsResponse

Get legal status history.

```python
events = await client.fetch_legal_events("EP1234567A1")
for event in events.events:
    event.code
    event.description
    event.date
```

### fetch_register_events(number) -> RegisterEventsResponse

Get dossier events from the European Patent Register. These are distinct from
the worldwide INPADOC legal events returned by `fetch_legal_events`.

```python
record = await client.fetch_register_events(number="EP1000000")
for event in record.events:
    event.event_date
    event.event_code
    event.description
```

### fetch_register_procedural_steps(number) -> RegisterProceduralStepsResponse

Get the structured procedural chronology for a European patent application.

```python
record = await client.fetch_register_procedural_steps(number="EP1000000")
for step in record.procedural_steps:
    step.phase
    step.step_code
    step.dates
```

### download_pdf(doc_id) -> PdfDownloadResponse

Download patent PDF.

```python
pdf = await client.download_pdf("EP1234567A1")
pdf.content_base64  # Base64-encoded PDF
```

### retrieve_cpc(cpc_code) -> CpcRetrievalResponse

Get CPC classification details.

```python
cpc = await client.retrieve_cpc("G06N3/08")
cpc.title
cpc.definition
```

### search_cpc(query) -> CpcSearchResponse

Search CPC classifications.

```python
results = await client.search_cpc("neural network")
```

## MCP jurisdiction recipes

The canonical `search_epo` MCP tool accepts `jurisdiction="CN"`, `"DE"`, or
`"KR"`. It combines the selected publication-country clause with the caller's
CQL query. Use the existing `get_epo_biblio`, `get_epo_family`, and
`get_epo_legal_events` tools on returned publication numbers.

## CQL Query Syntax

EPO uses Common Query Language:

```
# Title/abstract search
ta="machine learning"

# Applicant
applicant="Google"

# Inventor
inventor="Smith"

# Publication date
pd>=2020 and pd<=2023

# Classification
cpc="G06N"

# Combined
ta="neural" and applicant="IBM" and pd>=2020

# Chinese publications
ta="battery" and pn=CN
```

## Rate Limits

EPO OPS has quota limits:
- **Traffic light**: Check response headers for quota status
- **Weekly quota**: Resets Sunday midnight CET
- **Throttling**: Automatic backoff on 429 responses
