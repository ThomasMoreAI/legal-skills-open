# US Copyright Office

Search and retrieve records from the US Copyright Office's Copyright Public Records System (CPRS): registrations (post‑1978 + digitized card catalog) and recorded documents (transfers, assignments, licenses). No API key required. HTTP/2 is required and handled automatically.

## Module

```python
from patent_client_agents.copyright import (
    CopyrightClient,
    CopyrightRecord,
    SearchResponse,
)
```

## search(query, field, page, page_size, sort_order)

Search across all fields, titles, or claimant names. Returns a `SearchResponse` with `metadata`, `histogram` facets, and `records`.

```python
from patent_client_agents.copyright import CopyrightClient

async with CopyrightClient() as client:
    response = await client.search("Mickey Mouse")
    for record in response.records:
        print(record.copyright_number_for_display, record.title_of_work)
```

Valid `field` values: `"keyword"` (default — all fields), `"title"`, `"name"` (claimant).

## search_by_title(title) / search_by_name(name)

Convenience wrappers that pin `field`.

```python
gatsby = await client.search_by_title("The Great Gatsby")
disney = await client.search_by_name("Disney", page_size=25)
```

## get_record(public_records_id)

Look up a single record by its public records ID. There's no dedicated detail endpoint; this performs a filtered search.

```python
detail = await client.get_record("voyager_67890")
if detail is not None:
    print(detail.registration_status, detail.first_published_date)
```

## Record shape

`CopyrightRecord` (selected fields):

| Field | Notes |
|---|---|
| `public_records_id` | Stable identifier (e.g. `voyager_12345`, `card_catalog_CC...`) |
| `title_of_work` | List of titles |
| `registration_number` | List of registration numbers (e.g. `TX 1234567`) |
| `type_of_record` | `registration` or `recordation` |
| `registration_status` | `published`, `unpublished` |
| `claimant` / `claimants` | Owner names |
| `type_of_work` | `text`, `motion_picture`, `sound_recording`, etc. |
| `system_of_origin` | `voyager` (post‑1978) or `card_catalog` (pre‑1978 backfile) |
| `application_date` / `first_published_date` / `fee_date` / `deposit_received_date` | Lifecycle dates |
| `link_to_image_url` | LOC tile-server URLs for digitized card-catalog cards |

Some fields arrive as scalars instead of arrays (e.g. SR‑prefix sound recordings with one registration number); the model coerces to one‑element lists.

## Stability and ToS

- Undocumented API; response shape has been stable through CPRS migrations.
- No documented rate limits; the client uses the shared SQLite cache so re-fetches don't hit the server.
- HTTP/2 is required — the server returns HTTP 500 on HTTP/1.1. The client handles this automatically.
- All records are public; redistribution is governed by US copyright law (records themselves are government data; the works they describe are usually not).
