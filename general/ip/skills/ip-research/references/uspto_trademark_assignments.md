# USPTO Trademark Assignments

Trademark ownership-transfer records via the USPTO Assignment Center.

## Client

```python
from patent_client_agents.uspto_trademark_assignments import TrademarkAssignmentClient
```

No API key required.

## Search axes

```python
async with TrademarkAssignmentClient() as client:
    # By assignee (party acquiring rights)
    records = await client.search_by_assignee("Apple Inc", limit=100)

    # By assignor (party transferring rights)
    records = await client.search_by_assignor("Samsung", limit=50)

    # By serial number
    records = await client.search_by_serial("97123456")

    # By registration number
    records = await client.search_by_registration("5123456")

    # By reel/frame (direct recordation lookup)
    records = await client.search_by_reel_frame("9006/0093")
```

Each method returns `list[TrademarkAssignmentRecord]`.

## Generic search

```python
records = await client.search(
    criteria=[
        {"property": "Apple Inc", "searchBy": "assigneeName"},
    ],
    start_row=1,
    limit=100,
)
```

For paginated walks across all rows:

```python
all_rows = await client.search_all(by="assignee", query="Apple Inc")
```

## TrademarkAssignmentRecord Fields

| Field | Type | Description |
|---|---|---|
| `reel_number` | int | Reel number |
| `frame_number` | str | Frame number |
| `reel_frame` | str | Computed `"<reel>/<frame>"` |
| `assignor_execution_date` | str \| None | Earliest assignor execution date |
| `correspondent_name` | str \| None | Correspondent of record |
| `domestic_representative` | str \| None | Domestic representative |
| `assignors` | list[`Assignor`] | Previous owners (`assignor_name`, `execution_date`) |
| `assignees` | list[str] | New owners (bare name strings) |
| `number_of_properties` | int | Count of `properties` |
| `properties` | list[`TrademarkProperty`] | Affected marks: serial/registration, mark text, dates, current owner |

## Caveats

- **Pagination:** `start_row` is 1-based; `limit` is capped at 1000 per
  request. Use `search_all` for unbounded result sets.
- **Reel/frame format** is `"<reel>/<frame>"` — the frame component is a
  zero-padded string (e.g. `"9006/0093"`), not an integer.
