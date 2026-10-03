# Google Patents

Full-text patent search and document retrieval via Google Patents scraping.

## Client

```python
from patent_client_agents.google_patents import GooglePatentsClient
```

No API key required.

## Methods

### get_patent_data(patent_number) -> PatentData

Fetch comprehensive patent metadata.

```python
async with GooglePatentsClient() as client:
    patent = await client.get_patent_data("US10123456B2")

    # Key fields
    patent.title
    patent.abstract
    patent.inventors          # List of inventor names
    patent.assignees          # List of assignee names
    patent.filing_date
    patent.publication_date
    patent.priority_date
    patent.expiration_date    # str — see ⚠ note below
    patent.expiration_estimated  # bool — True iff expiration_date is a priority+20y fallback
    patent.cpc_classifications  # List[CpcClassification]
    patent.claims             # Full claims text
    patent.description        # Full description text
    patent.citations          # List[PatentCitation]
    patent.cited_by           # List[PatentCitation]
    patent.family_members     # List[FamilyMember]
    patent.legal_events       # List[LegalEvent]
```

### search_patents(...) -> GooglePatentsSearchResponse

Search with filters.

```python
async with GooglePatentsClient() as client:
    results = await client.search_patents(
        keywords="neural network",
        assignee="Google",
        inventor="Smith",
        cpc_code="G06N",
        country="US",
        language="en",
        filing_date_from="2020-01-01",
        filing_date_to="2023-12-31",
        status="granted",  # or "pending"
        patent_type="utility",  # or "design", "plant"
        has_litigation=True,
        limit=100,
        offset=0
    )

    for result in results.results:
        result.publication_number
        result.title
        result.snippet
        result.assignee
        result.filing_date
```

### get_patent_claims(patent_number) -> list

Extract claims with structure.

```python
claims = await client.get_patent_claims("US10123456B2")
# Returns list of claim dictionaries with number, text, dependencies
```

### get_structured_claim_limitations(patent_number, claim_number) -> dict

Parse claim into limitations.

```python
limitations = await client.get_structured_claim_limitations("US10123456B2", 1)
# Returns {"preamble": "...", "limitations": ["a)", "b)", ...]}
```

### download_patent_pdf(patent_number, output_path)

Download patent PDF.

```python
await client.download_patent_pdf("US10123456B2", "/tmp/patent.pdf")
```

### get_patent_figures(patent_number) -> list

Extract figure metadata.

```python
figures = await client.get_patent_figures("US10123456B2")
# Returns list of figure URLs and captions
```

## ⚠ `expiration_date` is sometimes an estimate

Google Patents doesn't populate `expiration_date` for newly-granted patents
(typical for grants in the last ~6 months) — its structured data lacks the
field until backfilled. As an unblock, this client falls back to
`priority_date + 20 years` and sets `expiration_estimated=True`.

The estimate is approximate. It assumes the recorded priority date represents
the term-controlling effective filing date, which holds for most US utility
patents but underestimates term where only a foreign or provisional priority
is claimed.

**For accurate patent term, refine via USPTO ODP** when
`expiration_estimated` is `True`:

- Fetch the application via `UsptoOdpClient.applications.get(application_number)`
- Take `applicationFilingDate + 20 years + patentTermAdjustmentData.adjustmentTotalQuantity` days
- Walk `parentContinuityBag` for the chain-earliest non-provisional filing date
  (term runs from there for continuations and divisionals)

## Patent Number Formats

Accepts various formats:
- `US10123456B2` - US granted patent
- `US20200123456A1` - US application
- `EP1234567A1` - European
- `WO2020123456A1` - PCT
- `JP2020123456A` - Japanese
- `CN112345678A` - Chinese
