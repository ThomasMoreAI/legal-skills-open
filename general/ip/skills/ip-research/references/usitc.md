# USITC (EDIS, DataWeb, HTS, IDS)

US International Trade Commission data. The patent-relevant slice is **EDIS Section 337** investigations — patent owners enforce against imported infringing goods at the ITC. The connector also exposes DataWeb trade statistics, HTS tariff codes, and the IDS IP investigation index.

## Auth quick reference

| Sub-surface | Env var | Public? | How to obtain |
|---|---|---|---|
| EDIS | `USITC_EDIS_TOKEN` | No (JWT, ~2 wk) | [edis.usitc.gov](https://edis.usitc.gov) → API Token Generator |
| DataWeb | `USITC_DATAWEB_TOKEN` | No | [dataweb.usitc.gov](https://dataweb.usitc.gov) account page |
| HTS | — | Yes | None |
| IDS | — | Yes | None |

EDIS rejects unauthenticated downloads even for public documents. `EdisClient.require_auth()` raises a clear `AuthenticationError` pointing at the mint URL.

## Module

```python
from patent_client_agents.usitc import (
    DataWebClient,
    EdisClient,
    HtsClient,
    IdsClient,
)
from patent_client_agents.usitc.client import build_dataweb_query
```

## EDIS — patent enforcement at the ITC

`EdisClient` is the workhorse for Section 337 work.

### list_investigations

```python
async with EdisClient() as client:
    investigations = await client.list_investigations(
        investigation_number="337-TA-1380",  # exact lookup
    )
    # Or by type/status:
    active_337 = await client.list_investigations(
        investigationType="Sec 337",
        investigationStatus="Active",
    )
```

### list_documents

```python
docs = await client.list_documents(
    investigationNumber="337-TA-1380",
    documentType="Order",           # must be full string, not partial
    securityLevel="Public",         # or "Confidential"/"Limited"
    pageNumber=1,                   # 100 per page
)
```

### list_attachments + download_attachment

```python
attachments = await client.list_attachments(document_id=docs[0].id)
for att in attachments:
    result = await client.download_attachment(docs[0].id, att.id)
    # result.content_base64 — base64 bytes
    # result.filename, result.content_type
```

Attachments are huge — exhibits routinely hit hundreds of MB. The bulk‑download MCP tool caps at 25 per call.

## DataWeb — trade statistics

```python
query = build_dataweb_query(
    trade_type="Import",            # also Export, GenImp, TotExp, Balance, ForeignExp, ImpExp
    classification="HTS",           # also SITC, NAIC, SIC, QUICK, EXPERT
    years=["2023", "2024"],
    data_metrics=["CONS_CUSTOMS_VALUE"],
    commodities=["8542"],           # None = all commodities at the chosen granularity
    granularity="6",                # HTS digit level: 2/4/6/8/10
    aggregate_countries=False,      # break out by country
    aggregate_commodities=False,    # break out by HTS code
    scale="1",                      # 1 / 1000 / 1000000
    timeline="Annual",              # or "Monthly"
)

async with DataWebClient() as client:
    report = await client.run_report(query)
```

Returns tabular data — column headers + row values.

## HTS — Harmonized Tariff Schedule

```python
async with HtsClient() as client:
    results = await client.search(keyword="semiconductor")
    range_export = await client.export_range(start="8542.10", end="8542.99")
```

## IDS — IP investigation index

```python
async with IdsClient() as client:
    investigations = await client.list_investigations()
```

Upstream returns ~4000 records as a single 11 MB blob — the `list_ids_investigations` MCP tool drops `participants` / `staff_contacts` arrays by default (they're ~85% of payload size) and applies pagination/substring filters.

## Common workflows

- **"What's the docket for 337-TA-1380?"** → `list_investigations(investigation_number="337-TA-1380")` for the metadata, then `list_documents(investigationNumber="337-TA-1380", pageNumber=…)` to walk the docket.
- **"Find all PTAB-style Orders in a §337"** → `list_documents(investigationNumber=…, documentType="Order")`.
- **"Bulk-download all Public exhibits filed in Q1"** → MCP `download_usitc_investigation_documents` with `document_types=["Brief Filed With ALJ"]` and a date range.
- **"Patent litigants in semiconductors"** → `IdsClient.list_investigations()` then filter by `title_contains="semiconductor"`.

## Date filtering and pagination

EDIS doesn't return a total document count. When date filters are set, the connector pages all results from EDIS (up to 30 pages of 100 = 3000 docs), applies the date filter client-side, and paginates the filtered set — which is why the MCP tool reports a `total_matched` field.

## Stability and ToS

- EDIS, DataWeb, and HTS APIs are documented but periodically refactored; the client decodes JWT `exp` to surface expired EDIS tokens before Akamai 503s the request.
- IDS payload has been growing — keep an eye on the 11 MB blob if response times degrade.
- All ITC content is public; redistribution follows standard US gov-data terms. EDIS attachments may include third-party material whose underlying rights belong to the filer.
