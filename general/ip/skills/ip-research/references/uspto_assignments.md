# USPTO Assignments

Patent assignment and ownership data via the USPTO Assignment Center.

## Client

```python
from patent_client_agents.uspto_assignments import AssignmentCenterClient
```

No API key required.

## search

```python
async def search(
    *,
    query: str,
    by: Literal[
        "assignee", "assignor", "correspondent",
        "application_number", "patent_number", "publication_number",
        "reel_frame", "international_registration_number", "pct_number",
    ],
    exact: bool = False,
    executed_between: tuple[date, date] | None = None,
    conveyance: str | None = None,
    offset: int = 0,
    limit: int | None = None,
) -> SearchResults
```

Single entry point covering every search axis. `SearchResults` is
list-like (`for r in result`, `len(result)`, `result[0]`) and exposes
`records`, `total`, `truncated`.

### Examples

```python
from datetime import date
from patent_client_agents.uspto_assignments import AssignmentCenterClient

async with AssignmentCenterClient() as client:
    # By application
    result = await client.search(query="16136935", by="application_number")

    # By patent
    result = await client.search(query="10123456", by="patent_number")

    # By assignee with date range and conveyance filter
    result = await client.search(
        query="Google",
        by="assignee",
        executed_between=(date(2024, 1, 1), date(2024, 12, 31)),
        conveyance="SECURITY",
        limit=100,
    )
    for record in result:
        print(record.reel_frame, record.conveyance, record.assignees)
    if result.truncated:
        print(f"Capped at {len(result)} of {result.total}+ — narrow query")

    # By reel/frame
    result = await client.search(query="12345/0678", by="reel_frame")
```

## AssignmentRecord Fields

| Field | Type | Description |
|-------|------|-------------|
| `reel_frame` | str | Reel/frame as `"REEL/FRAME"` |
| `reel_number`, `frame_number` | int | Component numbers |
| `conveyance` | str \| None | Type of conveyance (e.g. `"ASSIGNMENT OF ASSIGNORS INTEREST"`) |
| `conveyance_code` | int \| None | Numeric conveyance code |
| `assignor_execution_date` | str \| None | Earliest assignor execution date |
| `assignors` | list[`Assignor`] | Previous owners (each with `assignor_name`, `execution_date`) |
| `assignees` | list[str] | New owners (bare name strings on this endpoint) |
| `correspondent_name` | str \| None | Correspondent of record |
| `properties` | list[`Property`] | Patents/applications covered by the recordation |
| `number_of_properties` | int | Convenience count |

`Property` exposes `patent_number`, `application_number`, `filing_date`,
`publication_number`, `invention_title`, `inventors`, etc.

## Caveats

- **USPTO 10k cap.** Very-broad queries (e.g. `assignee="[Company]"`) return
  at most ~10,000 records. `result.truncated` is `True` when this happens;
  narrow with `executed_between`, `conveyance`, or a more specific query.
- **Order is server-default and unsortable.** USPTO accepts `sortBy` but
  ignores it. Order is stable across calls within the same query.
- **Only `executed_between` works as a date filter.** USPTO ignores
  recordation, mail, and receipt date filters.

## Conveyance Types

Common values in `conveyance`:

- `ASSIGNMENT OF ASSIGNORS INTEREST` — standard assignment
- `SECURITY AGREEMENT` / `RELEASE BY SECURED PARTY` — security interests
- `MERGER` / `CHANGE OF NAME` — corporate changes
- `LICENSE` — license grants
