---
name: skill-iamshouvikmitra
title: Indian Court Data with bharat-courts
description: Access Indian court data — find judgments, search cases, download orders, get cause lists, and query the historical archive (1950–present, 25 HCs + SCI). Use `Judgments().find(...)` as the default for "find a judgment" questions — it picks archive vs live for you. Fall back to portal-specific clients (`HCServicesClient`, `DistrictCourtClient`, etc.) only when you need a portal-only feature (cause list, live case status, district drill-down).
author: iamshouvikmitra
author_url: https://github.com/iamshouvikmitra/bharat-courts/tree/main/src/bharat_courts/skill
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: in
practice: litigation
language: en
---

# Indian Court Data with bharat-courts

Async Python SDK. Three things to know:

1. **`Judgments` facade** (recommended default) — one `find(...)` call, routes between archive and live transparently, returns a uniform `Judgment` list. Use this first.
2. **Live clients** (`HCServicesClient`, `DistrictCourtClient`, `CalcuttaHCClient`, `JudgmentSearchClient`, `SCIClient`) — for portal-specific features the facade doesn't expose: case status, cause lists, district-court drill-down, current orders. CAPTCHA-gated, rate-limited.
3. **`ArchiveClient`** — direct access to the AWS Open Data buckets. The facade calls this for you; reach for it directly only if you need archive-specific operations like `iter_judgments` (bulk streaming) or `prefetch_sci_year` (pre-warming).

## Choosing the right tool

**For "find a judgment" — always start with `Judgments.find()`.** It handles the common cases and routes correctly. Only drop down to the portal clients for what they uniquely offer.

| User question | Use this |
|---|---|
| "Find judgments by Justice X in 2020" | **`Judgments().find(judge="X", year=2020)`** |
| "Get the PDF of judgment with CNR Y" | **`Judgments().find(cnr="Y")` + `fetch_pdf`** |
| "Cases mentioning right to privacy" | **`Judgments().find(text="right to privacy")`** (routes to live full-text) |
| "All Delhi HC writ petitions in 2020 mentioning Tata" | **`Judgments().find(text="tata", court="delhi", year=2020)`** (mixed → archive title match) |
| Bulk pull "all 18k Delhi 2020 judgments" | `ArchiveClient.iter_judgments` (facade doesn't stream) |
| "What's the status of case X right now?" / "Next hearing?" | `HCServicesClient.case_status` / `DistrictCourtClient.case_status` |
| "Download the cause list for tomorrow" | `HCServicesClient.cause_list` |
| "Get the latest orders in case X" | `HCServicesClient.court_orders` / `CalcuttaHCClient.search_orders` |
| "Recent Supreme Court judgments this week" | `SCIClient.list_recent_judgments` |

**Freshness gap**: the archive updates bi-monthly (SCI) and quarterly (HC). Anything decided in the last 2–3 months may not be there yet. If `find()` with structured filters returns nothing for a recent year, re-try with `source="live"` or fall back to the live clients, and tell the user about the gap.

## Installation

```bash
pip install bharat-courts[ocr]       # RECOMMENDED — ddddocr CAPTCHA solving, no auth needed
pip install bharat-courts[archive]   # historical archive support (DuckDB)
pip install bharat-courts[onnx]      # ONNX CAPTCHA model — requires HF_TOKEN
pip install bharat-courts[all]       # everything
```

For the federated `Judgments` facade, install **both** `[archive]` and `[ocr]` so it can use either backend.

## Quick Start — Federated find (the default)

```python
import asyncio
from bharat_courts import Judgments


async def main():
    async with Judgments() as j:
        # 1. Structured filters → archive (no CAPTCHA, partition-pruned)
        for r in await j.find(judge="chandrachud", year=(2018, 2024), court="sci", limit=10):
            print(f"{r.decision_date}  {r.case_id}  {r.title}")

        # 2. Free-text → live (only it does full-body search)
        for r in await j.find(text="right to privacy", limit=5):
            print(f"{r.decision_date}  {r.title}  [{r.source}]")

        # 3. CNR alone — prefix routes to the right bucket, instant
        result = await j.find(cnr="DLHC010230802020")
        if result:
            pdf_bytes = await j.fetch_pdf(result[0])
            with open("judgment.pdf", "wb") as f:
                f.write(pdf_bytes)

        # 4. Force a backend if you need to (e.g. only-live for recent cases)
        recent = await j.find(text="bail", source="live", limit=5)


asyncio.run(main())
```

Routing decisions (auto mode):

| What you pass | Backend | Why |
|---|---|---|
| `cnr=` set | archive | Prefix → court → partition; instant |
| `text=` only | live | Only the live portal does full-body text search |
| structured only (`judge`, `party`, `year`, `court`, `citation`) | archive | Partition-pruned, no CAPTCHA |
| `text=` + structured | archive | `text` folds into a title-substring match (party slot) |
| nothing | raises `ValueError` | Give at least one filter |

Each returned `Judgment` carries `.source = "archive"` or `"live"` so you can tell where it came from.

`fetch_pdf(judgment_or_cnr)` works for archive judgments and for CNR strings whose prefix maps to a known court. For **live** `Judgment` objects it raises `NotImplementedError` — the live PDF download needs the original `JudgmentResult` instance (for session continuity); use `JudgmentSearchClient.download_pdf(judgment_result, court_type)` directly in that case.

## Quick Start — High Courts

```python
import asyncio
from bharat_courts import get_court, HCServicesClient
from bharat_courts.captcha.ocr import OCRCaptchaSolver


async def main():
    court = get_court("delhi")  # or "bombay", "calcutta", etc.
    solver = OCRCaptchaSolver()

    async with HCServicesClient(captcha_solver=solver) as client:
        # Search by party name (year is mandatory)
        cases = await client.case_status_by_party(court, party_name="state", year="2024")

        # Search by case number
        cases = await client.case_status(court, case_type="134", case_number="1", year="2024")

        # Get cause list PDFs
        pdfs = await client.cause_list(court, civil=True)

        # Get court orders
        orders = await client.court_orders(court, case_type="134", case_number="1", year="2024")

        # List benches and case types (no CAPTCHA needed)
        benches = await client.list_benches(court)
        case_types = await client.list_case_types(court)


asyncio.run(main())
```

## Quick Start — District Courts

District courts use a 4-level hierarchy: State → District → Court Complex → Establishment. Discover courts dynamically, then search.

```python
from bharat_courts import DistrictCourtClient
from bharat_courts.captcha.ocr import OCRCaptchaSolver
from bharat_courts.districtcourts.parser import parse_complex_value


async def main():
    solver = OCRCaptchaSolver()

    async with DistrictCourtClient(captcha_solver=solver) as client:
        # 1. Discover the court hierarchy
        states = await client.list_states()  # {"8": "Bihar", "7": "Delhi", ...}
        districts = await client.list_districts("8")  # {"1": "Patna", "35": "Gaya", ...}
        complexes = await client.list_complexes(
            "8", "1"
        )  # {"1080010@2,3,4@Y": "Civil Court, Patna Sadar", ...}

        # 2. Parse the complex value to get the code and check if establishment is needed
        complex_val = list(complexes.keys())[0]
        complex_code, est_codes, needs_est = parse_complex_value(complex_val)
        est_code = est_codes[0] if needs_est else ""

        # 3. List case types (no CAPTCHA)
        case_types = await client.list_case_types("8", "1", complex_code, est_code)

        # 4. Search by party name (CAPTCHA auto-retried)
        cases = await client.case_status_by_party(
            state_code="8",
            dist_code="1",
            court_complex_code=complex_code,
            est_code=est_code,
            party_name="kumar",
            year="2024",
        )
        for case in cases:
            print(f"{case.case_number}: {case.petitioner} vs {case.respondent}")

        # 5. Search by case number
        cases = await client.case_status(
            state_code="8",
            dist_code="1",
            court_complex_code=complex_code,
            est_code=est_code,
            case_type="1",
            case_number="100",
            year="2024",
        )

        # 6. Get court orders
        orders = await client.court_orders(
            state_code="8",
            dist_code="1",
            court_complex_code=complex_code,
            est_code=est_code,
            case_type="1",
            case_number="100",
            year="2024",
        )

        # 7. Get cause list
        entries = await client.cause_list(
            state_code="8",
            dist_code="1",
            court_complex_code=complex_code,
            est_code=est_code,
            civil=True,
        )


asyncio.run(main())
```

## Judgment Search Portal

Search High Court judgments by keyword on judgments.ecourts.gov.in.

```python
from bharat_courts import JudgmentSearchClient
from bharat_courts.captcha.ocr import OCRCaptchaSolver


async def main():
    solver = OCRCaptchaSolver()

    async with JudgmentSearchClient(captcha_solver=solver) as client:
        # Single page search
        result = await client.search("right to privacy", search_opt="ALL", court_type="2")
        for j in result.items:
            print(f"{j.title} — {j.judgment_date}")

        # Paginate through all results
        async for page in client.search_all("right to privacy", search_opt="ALL"):
            for j in page.items:
                print(j.title)

        # Download PDFs
        result = await client.search("constitution")
        result.items = [await client.download_pdf(j) for j in result.items]

        # Batch download with automatic session reset every 25 downloads
        judgments = await client.download_pdfs(result.items, batch_size=25)


asyncio.run(main())
```

## Calcutta High Court (Direct)

Search orders/judgments directly on calcuttahighcourt.gov.in — has better PDF coverage than eCourts for Calcutta HC cases from September 2020 onwards.

```python
from bharat_courts import CalcuttaHCClient


async def main():
    async with CalcuttaHCClient() as client:
        # Search by case number
        orders = await client.search_orders(
            case_type="12",  # WPA
            case_number="12886",
            year="2024",
            establishment="appellate",  # or "original", "jalpaiguri", "portblair"
        )
        for order in orders:
            print(f"{order.order_date} | {order.judge} | {order.neutral_citation}")
            if order.pdf_url:
                pdf = await client.download_order_pdf(order.pdf_url)


asyncio.run(main())
```

### CalcuttaHCClient Methods

| Method | CAPTCHA | Returns | Description |
|--------|---------|---------|-------------|
| `search_orders(*, case_type, case_number, year, establishment="appellate", max_captcha_attempts=3)` | Yes | `list[CaseOrder]` | Search orders by case number |
| `download_order_pdf(pdf_url)` | No | `bytes` | Download order PDF |

`establishment` values: `"appellate"`, `"original"`, `"jalpaiguri"`, `"portblair"`.

## Quick Start — Historical Archive (AWS Open Data)

`ArchiveClient` reads the public S3 buckets maintained by Dattam Labs — SCI judgments from 1950 and 25 HCs, all CC-BY-4.0. **No CAPTCHA, no rate limits, no AWS account needed.** Requires `pip install bharat-courts[archive]`.

Use the archive whenever the user wants historical research, bulk PDF retrieval, or a judgment with a known CNR. For "current status" / "next hearing" / "cause list" questions, use the live clients above.

```python
from bharat_courts import ArchiveClient


async def main():
    async with ArchiveClient() as client:
        # 1. Search by judge + year range (partition-pruned in DuckDB)
        results = await client.search(
            court="sci",
            judge="chandrachud",
            year=(2018, 2024),
            limit=20,
        )
        for j in results:
            print(f"{j.decision_date}  {j.case_id}  {j.title}")
            print(f"  {j.citation}  outcome: {j.disposal_nature}")

        # 2. CNR lookup — court is auto-inferred from the 4-letter CNR prefix
        results = await client.search(cnr="DLHC010230802020")

        # 3. Bulk streaming — get every Delhi 2020 judgment without huge limits
        count = 0
        async for j in client.iter_judgments(court="delhi", year=2020, batch_size=500):
            count += 1
            # process(j)

        # 4. Fetch the PDF — pass a CNR string or a Judgment
        pdf_bytes = await client.fetch_pdf("DLHC010230802020")
        with open("judgment.pdf", "wb") as f:
            f.write(pdf_bytes)

        # 5. SCI supports regional-language PDFs
        hindi = await client.fetch_pdf("ESCR010000301950", language="hindi")


asyncio.run(main())
```

### ArchiveClient Methods

| Method | Returns | Description |
|---|---|---|
| `search(*, court=None, year=None, judge=None, party=None, citation=None, cnr=None, limit=50)` | `list[Judgment]` | One-shot search across both buckets (or just one if `court` is given). CNR-only queries auto-route via the prefix. |
| `iter_judgments(*, court=None, year=None, judge=None, party=None, citation=None, cnr=None, batch_size=500, max_results=None)` | `AsyncIterator[Judgment]` | Stream pages via LIMIT/OFFSET with a stable sort. Use for >50 rows. |
| `fetch_pdf(judgment_or_cnr, *, language="english")` | `bytes` | PDF bytes. Pass a `Judgment` to skip the lookup, or a CNR string. SCI supports `language="hindi" \| "tamil" \| "gujarati" \| …` |
| `prefetch_sci_year(year, language="english")` | `str` (local path) | Pre-warm a SCI year tar before a batch of fetches |
| `count(*, court=None, year=None)` | `dict[str, int]` | Per-bucket row counts |
| `cache_info()` | `dict` | `cache_dir`, `files`, `bytes`, `max_bytes` |

### ArchiveClient gotchas to communicate to the user

- **Freshness**: SCI updates bi-monthly, HC quarterly. For a case decided last month, try the live `JudgmentSearchClient` or `HCServicesClient` first.
- **No party search on HC**: HC parquet doesn't have separate `petitioner`/`respondent` columns. `party=` matches against the title only for HC. SCI works as expected.
- **No citation search on HC**: same reason — `citation=` is silently ignored for HC.
- **PDF cache lives on disk** at `~/.cache/bharat-courts/archive/` (5 GiB cap by default; override with `BHARAT_COURTS_ARCHIVE_CACHE_MAX_GB`). First SCI fetch in a year downloads a ~40–500 MB tar; subsequent fetches in the same year are essentially free.
- **License**: CC-BY-4.0 — when redistributing, attribute Dattam Labs / eCourts.

### Judgments facade methods (use this first)

| Method | Returns | Description |
|---|---|---|
| `find(*, text=None, court=None, year=None, judge=None, party=None, citation=None, cnr=None, source="auto", limit=50)` | `list[Judgment]` | Federated search; picks archive vs live by query shape (see routing table above). |
| `fetch_pdf(judgment_or_cnr, *, language="english")` | `bytes` | PDF for archive judgments and CNR strings. Raises `NotImplementedError` for live `Judgment` objects (use `JudgmentSearchClient.download_pdf` for those). |
| `live_to_judgment(jr)` | `Judgment` | Module-level helper if you're calling the live client directly and want the unified shape. |

### CNR-prefix helper

`bharat_courts.infer_court_from_cnr(cnr)` resolves a CNR's first 4 letters to a `Court`. Use it if you're routing CNRs across both live and archive clients yourself.

```python
from bharat_courts import infer_court_from_cnr

infer_court_from_cnr("DLHC010230802020")  # → Court(code="delhi")
infer_court_from_cnr("ESCR010000301950")  # → SUPREME_COURT
infer_court_from_cnr("HCBM020056322016")  # → Bombay (note: legacy prefix)
infer_court_from_cnr("WBCHCJ0008142019")  # → Calcutta
infer_court_from_cnr("garbage")  # → None (never raises)
```

## Available High Courts

Use `get_court(code)` with any of these codes:

| Code | Court | State Code |
|------|-------|------------|
| `delhi` | Delhi High Court | 26 |
| `bombay` | Bombay High Court | 1 |
| `calcutta` | Calcutta High Court | 16 |
| `madras` | Madras High Court | 10 |
| `allahabad` | Allahabad High Court | 13 |
| `karnataka` | Karnataka High Court | 3 |
| `kerala` | Kerala High Court | 4 |
| `gujarat` | Gujarat High Court | 17 |
| `punjab` | Punjab & Haryana High Court | 22 |
| `rajasthan` | Rajasthan High Court | 9 |
| `telangana` | Telangana High Court | 29 |
| `andhra` | Andhra Pradesh High Court | 2 |
| `patna` | Patna High Court | 8 |
| `gauhati` | Gauhati High Court | 6 |
| `orissa` | Orissa High Court | 11 |
| `mp` | Madhya Pradesh High Court | 23 |
| `jharkhand` | Jharkhand High Court | 7 |
| `chhattisgarh` | Chhattisgarh High Court | 18 |
| `himachal` | Himachal Pradesh High Court | 5 |
| `uttarakhand` | Uttarakhand High Court | 15 |
| `jammu` | J&K High Court | 12 |
| `manipur` | Manipur High Court | 25 |
| `meghalaya` | Meghalaya High Court | 21 |
| `sikkim` | Sikkim High Court | 24 |
| `tripura` | Tripura High Court | 20 |
| `sci` | Supreme Court of India | 0 |

## HCServicesClient Methods

| Method | CAPTCHA | Returns | Description |
|--------|---------|---------|-------------|
| `list_benches(court)` | No | `dict[str, str]` | Available benches |
| `list_case_types(court, *, bench_code="1")` | No | `dict[str, str]` | Case type codes for a bench |
| `case_status(court, *, case_type, case_number, year, bench_code="1")` | Yes | `list[CaseInfo]` | Search by case number |
| `case_status_by_party(court, *, party_name, year, bench_code="1", status_filter="Both")` | Yes | `list[CaseInfo]` | Search by party name |
| `court_orders(court, *, case_type, case_number, year, bench_code="1")` | Yes | `list[CaseOrder]` | Get orders for a case |
| `cause_list(court, *, civil=True, bench_code="1", causelist_date="")` | Yes | `list[CauseListPDF]` | Cause list PDFs (date format: DD-MM-YYYY) |
| `download_order_pdf(pdf_url)` | No | `bytes` | Download order PDF |

## JudgmentSearchClient Methods

| Method | CAPTCHA | Returns | Description |
|--------|---------|---------|-------------|
| `search(search_text, *, page=1, search_opt="PHRASE", court_type="2", max_captcha_attempts=3)` | Yes | `SearchResult` | Search judgments by keyword |
| `search_all(search_text, *, search_opt="PHRASE", court_type="2", max_captcha_attempts=3)` | Yes | `AsyncIterator[SearchResult]` | Paginate all results (auto re-auth on session expiry) |
| `download_pdf(judgment)` | No | `JudgmentResult` | Download PDF for a single judgment (sets `pdf_bytes` in place) |
| `download_pdfs(judgments, *, batch_size=25)` | No | `list[JudgmentResult]` | Batch download with auto session reset |

`search_opt` values: `"PHRASE"` (exact phrase), `"ANY"` (any word), `"ALL"` (all words).
`court_type` values: `"2"` (High Courts), `"3"` (Supreme Court Reports).

## DistrictCourtClient Methods

All search methods require `state_code`, `dist_code`, `court_complex_code`, and `est_code` (use the discovery methods to find these).

| Method | CAPTCHA | Returns | Description |
|--------|---------|---------|-------------|
| `list_states()` | No | `dict[str, str]` | All 36 states/UTs with codes |
| `list_districts(state_code)` | No | `dict[str, str]` | Districts for a state |
| `list_complexes(state_code, dist_code)` | No | `dict[str, str]` | Court complexes (value format: `code@ests@flag`) |
| `list_establishments(state_code, dist_code, complex_code)` | No | `dict[str, str]` | Establishments (when flag=Y) |
| `list_case_types(state_code, dist_code, complex_code, est_code="")` | No | `dict[str, str]` | Case type codes |
| `case_status(*, state_code, dist_code, court_complex_code, est_code="", case_type, case_number, year)` | Yes | `list[CaseInfo]` | Search by case number |
| `case_status_by_party(*, state_code, dist_code, court_complex_code, est_code="", party_name, year, status_filter="Both")` | Yes | `list[CaseInfo]` | Search by party name |
| `court_orders(*, state_code, dist_code, court_complex_code, est_code="", case_type, case_number, year)` | Yes | `list[CaseOrder]` | Get orders for a case |
| `cause_list(*, state_code, dist_code, court_complex_code, est_code="", court_no="", causelist_date="", civil=True)` | Yes | `list[CauseListEntry]` | Cause list entries |

Use `parse_complex_value(value)` from `bharat_courts.districtcourts.parser` to extract `(complex_code, est_codes, needs_establishment)` from the complex dropdown values.

## Data Models

All models support `to_dict()` and `to_json()` for serialization.

- **CaseInfo**: `case_number`, `case_type`, `cnr_number`, `filing_number`, `registration_number`, `registration_date`, `petitioner`, `respondent`, `status`, `court_name`, `judges`, `next_hearing_date`
- **CaseOrder**: `order_date`, `order_type`, `judge`, `pdf_url`, `pdf_bytes`, `order_text`
- **CauseListPDF**: `serial_number`, `bench`, `cause_list_type`, `pdf_url` (HC Services — one PDF per bench)
- **CauseListEntry**: `serial_number`, `case_number`, `case_type`, `petitioner`, `respondent`, `advocate_petitioner`, `advocate_respondent`, `court_number`, `judge`, `listing_date`, `item_number` (District Courts — structured entries)
- **JudgmentResult**: `title`, `court_name`, `case_number`, `judgment_date`, `judges`, `pdf_url`, `pdf_bytes`, `citation`, `bench_type`, `source_url`, `source_id`, `metadata` (used by `JudgmentSearchClient` / `SCIClient`)
- **Judgment**: `cnr`, `case_id`, `title`, `court` (resolved `Court`), `court_name_raw`, `bench`, `court_code`, `judges`, `author_judge`, `decision_date`, `date_of_registration`, `petitioner`, `respondent`, `citation`, `disposal_nature`, `description`, `pdf_path`, `available_languages`, `pdf_exists`, `source`, `year` (used by `ArchiveClient` — unified across SCI + HC schemas; fields not applicable to a given source are `None`)
- **SearchResult**: `items`, `total_count`, `page`, `page_size`, `has_next`, `total_pages` (paginated container)

## CAPTCHA Handling

Both HC Services and District Courts use Securimage CAPTCHAs. Two auto-solvers are available:

```python
# Option 1: ddddocr (pip install bharat-courts[ocr])
from bharat_courts.captcha.ocr import OCRCaptchaSolver

solver = OCRCaptchaSolver()  # ~60% accuracy, auto-retry with fresh sessions

# Option 2: ONNX model (pip install bharat-courts[onnx])
# REQUIRES HF_TOKEN env var — the model is downloaded from HuggingFace
# Get a token at https://huggingface.co/settings/tokens
# export HF_TOKEN=hf_...
from bharat_courts.captcha.onnx import ONNXCaptchaSolver

solver = ONNXCaptchaSolver()  # lighter, uses onnxruntime, needs HF auth

# Option 3: Manual input
from bharat_courts.captcha.manual import ManualCaptchaSolver

solver = ManualCaptchaSolver()  # prompts on stdin

# Option 4: Custom solver
from bharat_courts.captcha.base import CaptchaSolver


class MySolver(CaptchaSolver):
    async def solve(self, image_bytes: bytes) -> str:
        return "solved_text"
```

## Important Notes

- All methods are async — use `asyncio.run()` or `await`
- **Default CAPTCHA solver is OCRCaptchaSolver (ddddocr)** — no explicit solver needed if `bharat-courts[ocr]` is installed. Clients auto-detect the best available solver.
- **ONNXCaptchaSolver requires `HF_TOKEN`** — the ONNX model is hosted on HuggingFace which requires authentication. Set `export HF_TOKEN=hf_...` before use. Prefer OCRCaptchaSolver unless you have a specific reason to use ONNX.
- CAPTCHA is pinned to PHP session — the library creates fresh sessions on each retry automatically
- `year` is mandatory for party name search (server returns ERROR_VAL if empty)
- Case type codes are numeric and vary by court — discover via `list_case_types()`
- Rate limiting is built in (default 1 second between requests)
- District courts require dynamic court discovery (state → district → complex → establishment) unlike High Courts which use static `get_court()` codes
- JudgmentSearchClient only supports keyword search — there is no search by party name, CNR, or case number on the judgments portal
- Some order PDFs may not be uploaded on eCourts even when the case exists — `court_orders()` will return the URL but the PDF download may return an error from the server
- **Default to `Judgments.find()` for judgment searches**. It picks archive vs live for you based on the query — no need to reason about which to call. Use the portal-specific clients only when you need their portal-only features (cause lists, case status, district drill-down).
- **Archive freshness gap**: `ArchiveClient` data lags by 2–3 months (SCI bi-monthly, HC quarterly). When a user asks about a recent judgment and the facade's archive route returns nothing, retry with `source="live"` or fall back to `JudgmentSearchClient` / `HCServicesClient`, and mention the freshness gap.
- **Prefer archive over live for historical / bulk queries**: live judgment search is CAPTCHA-gated and rate-limited; archive `iter_judgments` can stream tens of thousands of judgments in seconds with no portal load.
- **Archive PDFs cache on disk**: first SCI PDF in a year triggers a 40–500 MB tar download. Subsequent fetches in that year are essentially free. Warn the user before kicking off many SCI fetches across many years.
