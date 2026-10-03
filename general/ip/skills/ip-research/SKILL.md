---
name: ip-research
title: IP Research
description: 'IP data research tools for patents, trademarks, and related USPTO/EPO/JPO records. Use when: - Looking up patents by number (US, EP, WO, JP, etc.) - Searching patent databases by keyword, assignee, inventor, or classification - Getting patent family, citation, or legal status information - Checking USPTO application status, file wrapper, PTAB proceedings, or petitions - Searching office action rejections and cited references - Looking up MPEP or TMEP sections, or CPC classifications - Searching Canadian case law / IP statutes via CanLII (Federal Court, FCA, SCC, TMOB, Patent Appeal Board, Patent Act, Trademarks Act) - Searching official Canadian Federal Court case files and recorded dockets by party - Monitoring China SPC IP Court scheduled hearings and semiconductor-related court materials - Searching global IP statutes / treaties via WIPO Lex (~200 jurisdictions) - Finding patent or trademark assignments / ownership history - Fetching USPTO publication full-text data - Checking
  U.S. trademark status, prosecution documents, or mark images (TSDR) - Searching the U.S. trademark register (TESS) by wordmark, owner, or goods/services - Federal Circuit (CAFC) appellate opinions and PTAB/district/ITC appeals - USITC Section 337 patent enforcement investigations (EDIS) and tariff codes (HTS) - U.S. Copyright Office registrations and recorded documents (transfers, assignments)'
author: parkerhancock
author_url: https://github.com/parkerhancock/patent-client-agents/tree/main/src/patent_client_agents/skills/ip_research
license: Apache-2.0
version: 0.1.1
execution_mode: open
jurisdiction: general
practice: ip
language: en
sources:
- title: Cache
  path: references/cache.md
- title: Cafc
  path: references/cafc.md
- title: Canada federal court
  path: references/canada-federal-court.md
- title: Canlii
  path: references/canlii.md
- title: China spc ip court
  path: references/china-spc-ip-court.md
- title: Copyright
  path: references/copyright.md
- title: Cpc
  path: references/cpc.md
- title: Epo ops
  path: references/epo_ops.md
- title: Euipo
  path: references/euipo.md
- title: Google patents
  path: references/google_patents.md
- title: Japan ip high court
  path: references/japan-ip-high-court.md
- title: Jpo
  path: references/jpo.md
- title: Mpep
  path: references/mpep.md
- title: Tmep
  path: references/tmep.md
- title: Usitc
  path: references/usitc.md
- title: Uspto applications
  path: references/uspto_applications.md
- title: Uspto assignments
  path: references/uspto_assignments.md
- title: Uspto bulkdata
  path: references/uspto_bulkdata.md
- title: Uspto odp
  path: references/uspto_odp.md
- title: Uspto office actions
  path: references/uspto_office_actions.md
- title: Uspto petitions
  path: references/uspto_petitions.md
- title: Uspto publications
  path: references/uspto_publications.md
- title: Uspto tmsearch
  path: references/uspto_tmsearch.md
- title: Uspto trademark assignments
  path: references/uspto_trademark_assignments.md
- title: Uspto tsdr
  path: references/uspto_tsdr.md
- title: Wipo lex
  path: references/wipo_lex.md
---

# IP Research

Async Python clients for patent and IP data. All clients use `async with` context
managers. All shared scaffolding (HTTP, cache, retry, errors) lives in
`mcp_data_core`, provided by the separate `mcp-data-core` package.

## Routing

| Task | Client / Module | Reference |
|------|-----------------|-----------|
| Patent lookup / search by keywords | `google_patents.GooglePatentsClient` | [google_patents.md](references/google_patents.md) |
| USPTO application status + file wrapper | `uspto_odp.ApplicationsClient` | [uspto_odp.md](references/uspto_odp.md) |
| USPTO application high-level API | `patent_client_agents.uspto_applications` | [uspto_applications.md](references/uspto_applications.md) |
| USPTO PTAB (IPR/PGR/CBM, ex parte appeals, interferences) | `uspto_odp.PtabTrialsClient` / `PtabAppealsClient` / `PtabInterferencesClient` | [uspto_odp.md](references/uspto_odp.md) |
| USPTO petitions | `uspto_odp.PetitionsClient` or `patent_client_agents.uspto_petitions` | [uspto_petitions.md](references/uspto_petitions.md) |
| USPTO bulk data products | `uspto_odp.BulkDataClient` or `patent_client_agents.uspto_bulkdata` | [uspto_bulkdata.md](references/uspto_bulkdata.md) |
| USPTO assignments | `uspto_assignments.AssignmentCenterClient` | [uspto_assignments.md](references/uspto_assignments.md) |
| USPTO publications (PPUBS) full-text | `uspto_publications.PublicSearchClient` | [uspto_publications.md](references/uspto_publications.md) |
| USPTO office actions | `patent_client_agents.uspto_office_actions` | [uspto_office_actions.md](references/uspto_office_actions.md) |
| USPTO trademark status / documents (TSDR) | `uspto_tsdr.TsdrClient` | [uspto_tsdr.md](references/uspto_tsdr.md) |
| USPTO trademark search (TESS — live trademark register) | `uspto_tmsearch.TmsearchClient` | [uspto_tmsearch.md](references/uspto_tmsearch.md) |
| USPTO trademark assignments | `uspto_trademark_assignments.TrademarkAssignmentClient` | [uspto_trademark_assignments.md](references/uspto_trademark_assignments.md) |
| EPO bibliographic / family / legal events | `epo_ops.EpoOpsClient` | [epo_ops.md](references/epo_ops.md) |
| JPO application status | `jpo.JpoClient` | [jpo.md](references/jpo.md) |
| MPEP search + section lookup | `patent_client_agents.mpep` | [mpep.md](references/mpep.md) |
| TMEP search + section lookup | `patent_client_agents.tmep` | [tmep.md](references/tmep.md) |
| CPC lookup / search / mapping | `patent_client_agents.cpc` | [cpc.md](references/cpc.md) |
| Canadian case law + IP statutes (FC / FCA / SCC / TMOB / Patent Appeal Board) | `patent_client_agents.canlii` | [canlii.md](references/canlii.md) |
| Canadian Federal Court party search + live dockets | `patent_client_agents.canada_federal_court` | [canada-federal-court.md](references/canada-federal-court.md) |
| China SPC IP Court scheduled hearings + site search | `patent_client_agents.china_spc_ip_court` | [china-spc-ip-court.md](references/china-spc-ip-court.md) |
| Global IP statutes via WIPO Lex (~200 jurisdictions) | `patent_client_agents.wipo_lex` | [wipo_lex.md](references/wipo_lex.md) |
| EU Trade Marks (EUTM register, ~2.3M marks) | `patent_client_agents.euipo_trademarks` | [euipo.md](references/euipo.md) |
| EU Registered Community Designs (~1.5M designs) | `patent_client_agents.euipo_designs` | [euipo.md](references/euipo.md) |
| Federal Circuit (CAFC) opinions — appellate patent law | `patent_client_agents.cafc` | [cafc.md](references/cafc.md) |
| USITC Section 337 patent enforcement (EDIS), DataWeb trade stats, HTS, IDS IP investigations | `patent_client_agents.usitc` | [usitc.md](references/usitc.md) |
| US Copyright Office — registrations, recorded transfers | `patent_client_agents.copyright` | [copyright.md](references/copyright.md) |

## Quick Examples

### Lookup patent by number

```python
from patent_client_agents.google_patents import GooglePatentsClient

async with GooglePatentsClient() as client:
    patent = await client.get_patent_data("US10123456B2")
```

### Search USPTO applications

```python
from patent_client_agents.uspto_odp import ApplicationsClient

async with ApplicationsClient() as client:  # Requires USPTO_ODP_API_KEY
    results = await client.search(query="inventionTitle:laser", limit=25)
    for record in results.applicationBag:
        print(record.applicationNumberText, record.filingDate)
```

### Find PTAB proceedings

```python
from patent_client_agents.uspto_odp import PtabTrialsClient

async with PtabTrialsClient() as client:
    proceedings = await client.search_proceedings(query="patent:US10123456")
```

### Look up MPEP section

```python
from patent_client_agents.mpep import SearchInput, search

response = await search(SearchInput(query="obviousness rejection", per_page=10))
for hit in response.hits:
    print(hit.section_id, hit.title)
```

### Check trademark status (TSDR)

```python
from patent_client_agents.uspto_tsdr import TsdrClient

async with TsdrClient() as client:  # Requires USPTO_TSDR_API_KEY
    status = await client.get_status("97123456")
    print(status.mark_text, status.status_description)
```

### Look up TMEP section

```python
from patent_client_agents.tmep import get_section

section = await get_section("1207.01(a)")
print(section.title)
```

### Resolve a CPC symbol

```python
from patent_client_agents.cpc import retrieve_cpc

entry = await retrieve_cpc(symbol="H04L63/08", ancestors=True)
```

### Search Canadian IP case law (CanLII)

```python
from patent_client_agents.canlii import BrowseCasesInput, browse_cases

# 20 most recent Federal Court IP decisions
recent = await browse_cases(BrowseCasesInput(
    database_id="fct",
    result_count=20,
    decision_date_after="2024-01-01",
))
```

### Search Canadian Federal Court patent dockets

```python
from patent_client_agents.canada_federal_court import CanadaFederalCourtClient

async with CanadaFederalCourtClient() as client:
    cases = await client.search_party_cases("Pfizer", patent_only=True)
    docket = await client.list_docket_entries(cases.cases[0].court_number)
```

The Court does not publish an official open/closed field. Treat
`likely_pending` / `likely_closed` as conservative docket-text inferences and
`unknown` as unresolved, not as evidence that no case is pending.

### Monitor China SPC IP Court hearings

```python
from patent_client_agents.china_spc_ip_court import ChinaSpcIpCourtClient

async with ChinaSpcIpCourtClient() as client:
    index = await client.list_hearing_index(page=1)
    notice = await client.get_hearing_notice(index.notices[0].notice_id)
    chip_material = await client.search_site("芯片")
```

Hearing notices are pending-hearing signals, not complete dockets. They often
omit case and patent numbers, and the official site may be unreachable from
some foreign DNS or cloud-egress environments.

### Fetch a global IP statute via WIPO Lex

```python
from patent_client_agents.wipo_lex import (
    SearchLegislationInput, SubjectMatter, search_legislation, get_legislation,
)

# Find Canadian patent statutes, then pull the Patent Act detail with PDFs
hits = await search_legislation(SearchLegislationInput(
    country_codes=["CA"], subject_matter=[SubjectMatter.PATENTS],
))
detail = await get_legislation(hits.hits[0].legislation_id)
```

## Error Handling

All clients raise typed exceptions from `mcp_data_core.exceptions`. `ApiError`
and its subclasses include a path to the log file in their string representation
so agents can inspect stacktraces without keeping them in context.

```python
from mcp_data_core.exceptions import (
    McpDataCoreError,
    NotFoundError,
    RateLimitError,
)

try:
    async with GooglePatentsClient() as client:
        patent = await client.get_patent_data("US99999999")
except NotFoundError as e:
    print(e)  # "... (HTTP 404, details: ~/.cache/patent_client_agents/patent_client_agents.log)"
except RateLimitError as e:
    if e.retry_after:
        await asyncio.sleep(e.retry_after)
except McpDataCoreError as e:
    print(e)  # Fallback for any other typed error
```

**Exception hierarchy** (from `mcp_data_core.exceptions`):

| Exception | When |
|-----------|------|
| `NotFoundError` | Resource not found (404) |
| `RateLimitError` | Rate limit exceeded (429); `retry_after` set if server supplied it |
| `AuthenticationError` | Bad or missing API credentials (401/403) |
| `ServerError` | Remote API 5xx |
| `ApiError` | Other HTTP errors (base for all HTTP-level errors; appends log path) |
| `ParseError` | Failed to parse response data |
| `ConfigurationError` | Missing API key / invalid config |
| `ValidationError` | Invalid input; also inherits `ValueError` |
| `McpDataCoreError` | Base for all typed errors |

**Log file:** `~/.cache/patent_client_agents/patent_client_agents.log` — full tracebacks, request/response
details, debug info. Read this when concise error messages aren't enough.

## Environment Variables

| Variable | Required For |
|----------|--------------|
| `USPTO_ODP_API_KEY` | All USPTO ODP clients (Applications, PTAB, BulkData, Petitions, Office Actions) |
| `USPTO_TSDR_API_KEY` | TSDR (trademark status / documents / images) |
| `EPO_OPS_API_KEY` | EPO OPS, CPC (CPC uses EPO OPS under the hood) |
| `EPO_OPS_API_SECRET` | EPO OPS, CPC |
| `JPO_API_USERNAME` | JPO client |
| `JPO_API_PASSWORD` | JPO client |
| `CANLII_API_KEY` | CanLII (Canadian courts + IP statutes); free key by request |

USPTO Publications, USPTO Assignments, USPTO Trademark Assignments,
Google Patents, MPEP, TMEP, Canada Federal Court case files, China SPC IP
Court hearing notices, Japan IP High Court patent and utility-model case lists, and WIPO Lex
require no API key.

## Cache Management

All clients cache HTTP responses to `~/.cache/patent_client_agents/` using `hishel` with a
SQLite backend and WAL pragmas. See [cache.md](references/cache.md) for TTL,
invalidation, and statistics APIs.

## Issue Reporting

**Source**: [parkerhancock/patent-client-agents](https://github.com/parkerhancock/patent-client-agents)

Report bugs with version, minimal reproduction code, and relevant API response
if applicable.

## References

- [google_patents.md](references/google_patents.md) — Full-text search, patent documents, citations
- [uspto_odp.md](references/uspto_odp.md) — Applications, PTAB, bulk data, petitions
- [uspto_applications.md](references/uspto_applications.md) — High-level applications API
- [uspto_petitions.md](references/uspto_petitions.md) — Petition decisions
- [uspto_bulkdata.md](references/uspto_bulkdata.md) — Bulk data product catalog
- [uspto_office_actions.md](references/uspto_office_actions.md) — Office action analytics
- [uspto_assignments.md](references/uspto_assignments.md) — Patent assignment/ownership lookup
- [uspto_publications.md](references/uspto_publications.md) — PPUBS full-text
- [uspto_tsdr.md](references/uspto_tsdr.md) — Trademark Status & Document Retrieval
- [uspto_trademark_assignments.md](references/uspto_trademark_assignments.md) — Trademark ownership transfers
- [epo_ops.md](references/epo_ops.md) — EPO bibliographic, family, legal status
- [jpo.md](references/jpo.md) — Japan Patent Office
- [japan-ip-high-court.md](references/japan-ip-high-court.md) — Japan IP High Court pending and closed patent and utility-model case lists
- [mpep.md](references/mpep.md) — Manual of Patent Examining Procedure
- [tmep.md](references/tmep.md) — Trademark Manual of Examining Procedure
- [cpc.md](references/cpc.md) — CPC classification lookup
- [cache.md](references/cache.md) — Cache management
