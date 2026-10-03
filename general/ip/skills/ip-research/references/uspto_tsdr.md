# USPTO TSDR

Trademark Status & Document Retrieval. Status, prosecution documents,
and mark images for U.S. trademark cases.

## Client

```python
from patent_client_agents.uspto_tsdr import TsdrClient

async with TsdrClient() as client:
    status = await client.get_status("97123456")
```

Requires `USPTO_TSDR_API_KEY`. Request a key from
[account.uspto.gov/api-manager/](https://account.uspto.gov/api-manager/)
with a free MyUSPTO account (pick the TSDR API product).

Missing key raises `ConfigurationError` at construction.

## Rate limits

| Window | General | PDF/ZIP |
|---|---|---|
| Peak (5am–10pm ET) | 60 req/min | 4 req/min |
| Off-peak | 120 req/min | 12 req/min |

The client honors `Retry-After` on 429 responses via `default_retryer`.

## Status — `get_status(serial_number)`

Returns a `TrademarkStatus` with mark text, status, dates, owners,
goods/services classes, and prosecution history.

```python
status = await client.get_status("97123456")
print(status.mark_text)
print(status.status_description, status.status_date)
print(status.filing_date, status.registration_date)

for owner in status.owners:
    print(owner.name, owner.entity_type, owner.country)

for ev in status.prosecution_history:
    print(ev.event_date, ev.event_code, ev.event_description)
```

## Documents — `get_documents(serial_number)`

```python
docs = await client.get_documents("97123456")
for d in docs:
    print(d.document_type, d.scan_date, d.url)
```

For full bytes, use `download_documents_pdf` (one PDF bundle) or
`download_documents_zip` (ZIP) — both count against the lower PDF/ZIP
rate budget.

## Image — `get_image(serial_number)`

```python
image_bytes = await client.get_image("97123456")  # JPG bytes
```

## Batch — `batch_status(serial_numbers)`

```python
multi = await client.batch_status(["97123456", "97654321", "98000001"])
for serial, status in multi.cases.items():
    print(serial, status.status_description)
```

Single round trip per call; the USPTO endpoint caps the batch size
internally — split larger lists yourself.

## Status field reference

| Field | Type | Description |
|---|---|---|
| `serial_number` | str | The serial number as filed |
| `registration_number` | str \| None | If registered |
| `mark_text` | str \| None | Literal mark text |
| `mark_type` | str \| None | Standard character, design, etc. |
| `status_code` | str \| None | TSDR numeric status code |
| `status_description` | str \| None | Human-readable status |
| `status_date` | str \| None | Date status was set |
| `filing_date` | str \| None | Application filing date |
| `registration_date` | str \| None | Grant date if registered |
| `owners` | list[Owner] | Current owners (name, address, country, entity_type) |
| `goods_services` | list[GoodsServices] | Class number, description, first-use dates |
| `prosecution_history` | list[ProsecutionEvent] | Event date, code, description |

## Caveats

- **Serial numbers are 8 digits.** Hyphens/spaces are stripped client-side.
- **Status XML is ST.96.** The client parses it into Pydantic models; the
  raw XML isn't exposed (use `get_status_html` for the HTML page).
- **`get_last_update` derives from prosecution history**, not a dedicated
  endpoint — the most recent event date wins.
