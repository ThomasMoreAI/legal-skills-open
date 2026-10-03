# CanLII (Canadian courts, tribunals, and IP statutes)

Read-only access to Canadian case law and legislation.

## Module

```python
from patent_client_agents.canlii import (
    BrowseCasesInput,
    CanLIIClient,
    GetCaseInput,
    GetCitatorInput,
    GetLegislationInput,
    SubjectMatter,  # not used by CanLII itself — kept for parity
    browse_cases,
    browse_legislation,
    get_case,
    get_cited_cases,
    get_cited_legislations,
    get_citing_cases,
    get_legislation,
    list_case_databases,
    list_legislation_databases,
)
```

## Auth

Set `CANLII_API_KEY` in the environment. Free key by request through the [CanLII feedback form](https://www.canlii.org/en/feedback/feedback.html).

## browse_cases / get_case / get_cited_cases / get_citing_cases

Browse a court / tribunal database (newest first), fetch metadata for a specific case, or walk the citator. The citator endpoints are **English-only**.

```python
from patent_client_agents.canlii import BrowseCasesInput, browse_cases

# 20 most recent Federal Court IP decisions, filtered to 2024+
recent = await browse_cases(BrowseCasesInput(
    database_id="fct",
    result_count=20,
    decision_date_after="2024-01-01",
))
for c in recent.cases:
    print(c.case_id.en, c.title, c.citation)
```

```python
from patent_client_agents.canlii import GetCaseInput, get_case

dunsmuir = await get_case(GetCaseInput(database_id="csc-scc", case_id="2008scc9"))
dunsmuir.title, dunsmuir.citation, dunsmuir.decision_date, dunsmuir.docket_number
```

## get_legislation / browse_legislation

```python
from patent_client_agents.canlii import GetLegislationInput, get_legislation

patent_act = await get_legislation(GetLegislationInput(
    database_id="cas",
    legislation_id="rsc-1985-c-p-4",
))
patent_act.title, patent_act.start_date, patent_act.end_date, patent_act.repealed
```

## Common database IDs

| `database_id` | Coverage |
|---|---|
| `csc-scc` | Supreme Court of Canada |
| `fca` | Federal Court of Appeal |
| `fct` | Federal Court (patent / TM infringement) |
| `tmob-comc` | Trade-marks Opposition Board |
| `cab-cab` | Commissioner of Patents — Patent Appeal Board |
| `cas` | Federal statutes (Patent Act = `rsc-1985-c-p-4`) |
| `car` | Federal regulations |

## Limits

- HTTPS only
- Max `result_count`: 10,000 per call
- 10 MB response cap surfaces as `ApiError(status_code=413)`
- High-volume scraping warned-against; keys revocable
