# Canada Federal Court case files and dockets

Official party search and recorded-entry data from the Federal Court's public Court Files service. No credentials are required.

```python
from patent_client_agents.canada_federal_court import CanadaFederalCourtClient

async with CanadaFederalCourtClient() as client:
    cases = await client.search_party_cases(
        "Pfizer",
        patent_only=True,
        limit=25,
    )
    case = await client.get_case(cases.cases[0].court_number)
    docket = await client.list_docket_entries(case.case.court_number)
```

Use this connector for party-to-case discovery and docket history. Use CanLII for published decisions and citator work.

The official search response does not contain an open/closed status or reliable plaintiff/defendant roles for every party. Status assessments are conservative inferences from explicit recent docket language and always carry `inferred=True`. `unknown` means the docket text is inconclusive.
