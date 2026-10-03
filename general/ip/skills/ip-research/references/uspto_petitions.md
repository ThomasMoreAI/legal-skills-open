# USPTO Petitions

Petition decisions via USPTO ODP. Requires `USPTO_ODP_API_KEY`.

## Module

```python
from patent_client_agents.uspto_petitions import (
    search_petitions,
    get_petition,
    download_petitions,
)
```

Low-level access is also available via
`patent_client_agents.uspto_odp.PetitionsClient`.

## search_petitions(q, ...)

```python
result = await search_petitions(
    q="petitionDecision:granted",
    fields=["petitionIdentifier", "petitionDecisionDate", "petitionType"],
    limit=25,
)
for record in result.petitionBag:
    print(record.petitionIdentifier, record.petitionDecisionDate)
```

## get_petition(petition_identifier)

```python
petition = await get_petition("P20230001")
```

## download_petitions(identifiers)

Bulk-fetch petition decision documents. Returns a list of records with
`downloadURI`s / inline content per the API schema.

See docstrings on `patent_client_agents.uspto_petitions.api` for the full parameter
list (filter/sort/pagination).
