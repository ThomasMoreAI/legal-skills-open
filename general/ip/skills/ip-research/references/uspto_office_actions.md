# USPTO Office Actions

Analytics and full-text over USPTO office action (OA) data. Requires
`USPTO_ODP_API_KEY`.

## Client

```python
from patent_client_agents.uspto_office_actions import OfficeActionClient
```

## Methods

### search_rejections(...)

Search rejections by statute (§102, §103, §112), art unit, examiner, date
range, etc.

```python
async with OfficeActionClient() as client:
    response = await client.search_rejections(
        filters=[{"statute": "103"}],
        limit=25,
    )
    for row in response.rejectionBag:
        print(row.applicationNumberText, row.rejectionCode, row.mailDate)
```

### search_citations(...)

Search cited prior art references across OAs.

```python
response = await client.search_citations(
    query="US10123456",
    limit=25,
)
```

### search_office_action_text(...)

Full-text search across OA body text.

```python
response = await client.search_office_action_text(
    query="claims 1-5 rejected under 35 U.S.C. 103",
)
```

### search_enriched_citations(...)

Enriched citation data combining OA rejections with cited-reference metadata.

## Response Models

- `RejectionSearchResponse` → `rejectionBag: list[OfficeActionRejection]`
- `CitationSearchResponse` → `citationBag: list[OfficeActionCitation]`
- `OfficeActionTextSearchResponse` → `textBag: list[OfficeActionText]`
- `EnrichedCitationSearchResponse` → `citationBag: list[EnrichedCitation]`

See `patent_client_agents.uspto_office_actions.models` for field definitions.
