# USPTO Trademark Search (TESS)

Search the live USPTO trademark register: wordmark, owner, goods/services description, serial number, registration number, design code. This is the *search* surface; for current-status lookups by serial number use TSDR (`uspto_tsdr.md`), and for ownership history use trademark assignments (`uspto_trademark_assignments.md`).

## Auth — AWS WAF token

USPTO TESS sits behind AWS WAF. The client needs an `aws-waf-token` cookie (~4 day lifetime) plus Chrome TLS impersonation. Two paths:

1. **In-process (Playwright)** — `pip install 'patent-client-agents[tmsearch]' && playwright install chromium`. Client mints + caches tokens automatically.
2. **Bring your own** — set `PCA_WAF_TOKEN_JSON` to inline JSON or `PCA_WAF_TOKEN_PATH` to a JSON file containing `{"token": "...", "expires": <unix_ts>, "acquired": "..."}`.

Default cache path: `~/.cache/patent_client_agents/waf_token.json`. Legacy env vars `LAW_TOOLS_WAF_TOKEN_JSON`/`WAF_TOKEN_PATH` and legacy cache `~/.law-tools/waf_token.json` honored for one release.

If neither a cached token nor Playwright is available, `TmsearchClient.__aenter__` raises `ConfigurationError` with a message pointing at both options.

## Module

```python
from patent_client_agents.uspto_tmsearch import (
    TmsearchClient,
    TrademarkSearchResponse,
    TrademarkSearchResult,
)
```

## search_wordmark(wordmark, live_only=False, size=100, from_=0)

```python
async with TmsearchClient() as client:
    results = await client.search_wordmark("APPLE", live_only=True)
    for tm in results.results:
        print(tm.serial_number, tm.wordmark, tm.status_live, tm.primary_owner)
```

## search_owner(owner_name, live_only=False, size=100, from_=0)

```python
results = await client.search_owner("Apple Inc.", live_only=True)
```

## search_goods_services(terms, live_only=False, size=100, from_=0)

```python
shoes = await client.search_goods_services("running shoes", live_only=True)
```

## get_by_serial(serial_number) / get_by_registration(registration_number)

Single-record lookup. Returns `TrademarkSearchResult | None`.

```python
detail = await client.get_by_serial("97123456")
if detail is not None:
    print(detail.wordmark, detail.registration_date)
```

## search(...) — multi-criteria

```python
hits = await client.search(
    wordmark="APPLE",
    owner="Apple Inc",
    live_only=True,
    status="live",     # or "dead" / "all"
    size=100,
)
```

At least one search criterion is required (else `ValueError`).

## search_all(...) — auto-paginated

```python
all_apple = await client.search_all(
    wordmark="APPLE",
    live_only=True,
    batch_size=500,    # max 500 per request
    max_results=2000,  # cap
)
```

Walks pages until empty or cap, then returns the combined `list[TrademarkSearchResult]`. Caps internally at `from_=10000` to avoid Elasticsearch's deep-pagination penalty.

## Result shape

`TrademarkSearchResult` (selected fields):

| Field | Notes |
|---|---|
| `serial_number` | USPTO serial (8-digit) |
| `registration_number` | If registered |
| `wordmark` | Stylized as filed |
| `status_live` / `is_live` | Boolean |
| `owner_name` (list) | Multiple owners possible |
| `primary_owner` | First entry in `owner_name` |
| `attorney` | Filing attorney |
| `filed_date` / `registration_date` / `abandon_date` / `cancel_date` | Lifecycle dates |
| `goods_and_services` (list) | Goods/services descriptions |
| `drawing_code` + `drawing_code_description` | TESS drawing code |
| `current_basis` (list) | Filing basis (1(a), 1(b), 44(d), etc.) |
| `international_class` (list) | Nice classes |
| `us_class` (list) | US classes |
| `design_code` (list) + `design_code_description` (list) | Vienna codes |
| `mark_description` (list) | Per-application mark descriptions |
| `disclaimer` | Disclaimed text |
| `assignment_recorded` | Bool |

## Common workflows

- **"Is this mark live?"** — `get_by_serial(serial)` then check `is_live`.
- **"All Apple Inc. trademarks"** — `search_owner("Apple Inc.", live_only=True)` or `search_all(owner="Apple Inc.", live_only=True)`.
- **"Marks covering software in class 9"** — `search_goods_services("computer software")` then filter by `international_class`.
- **"How many marks for 'INVISIBLE'?"** — `search_wordmark("INVISIBLE")` and read `total`.

## Stability and ToS

- The TESS API is undocumented; the AWS WAF challenge mechanism is the fragile bit. If AWS changes the challenge.js or USPTO swaps WAF providers, Playwright would need to follow.
- WAF tokens are bound to the User-Agent + TLS fingerprint that solved the challenge. The client always sends a canonical Chrome 120 UA and curl_cffi `chrome120` TLS impersonation. Don't override either.
- All TESS records are public; redistribution is fine for ordinary research/diligence use.
