# USPTO Applications (high-level API)

Function-level wrappers over `uspto_odp.ApplicationsClient` for patent
application lookups, file wrappers, family graphs, and PTAB proceedings.
Requires `USPTO_ODP_API_KEY`.

## Module

```python
from patent_client_agents.uspto_applications import (
    search_applications,
    get_application,
    list_documents,
    get_family,
    search_trial_proceedings,
    get_trial_proceeding,
    search_trial_decisions,
    get_trial_decisions_by_trial,
    search_trial_documents,
    get_trial_documents_by_trial,
)
```

## Applications

### search_applications(q, ...)

```python
result = await search_applications(
    q="inventionTitle:laser",
    fields=["applicationNumberText", "filingDate"],
    sort="filingDate desc",
    limit=25,
    offset=0,
)
```

### get_application(application_number)

```python
app = await get_application("16123456")
```

### list_documents(application_number)

Returns the file wrapper (prosecution history) documents.

```python
docs = await list_documents("16123456")
for doc in docs.documentBag:
    print(doc.documentCode, doc.officialDate, doc.directionCategory)
```

### get_family(application_number)

Returns parent/child continuity and foreign priority as a graph.

```python
family = await get_family("16123456")
family.nodes
family.edges
```

## PTAB Proceedings (trials)

### search_trial_proceedings / get_trial_proceeding
### search_trial_decisions / get_trial_decisions_by_trial
### search_trial_documents / get_trial_documents_by_trial

Thin wrappers over `uspto_odp.PtabTrialsClient`. See [uspto_odp.md](uspto_odp.md)
for the underlying filter/sort schema.

## Passing a client

All functions accept an optional `client=` parameter to reuse a single
`ApplicationsClient` across calls:

```python
from patent_client_agents.uspto_odp import ApplicationsClient

async with ApplicationsClient() as client:
    app = await get_application("16123456", client=client)
    docs = await list_documents("16123456", client=client)
```
