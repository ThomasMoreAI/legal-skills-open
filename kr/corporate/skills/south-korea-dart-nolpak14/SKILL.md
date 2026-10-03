---
name: south-korea-dart-nolpak14
title: 'South korea dart'
description: 'Look up South Korea companies for free via the official DART OpenAPI (opendart.fss.or.kr, Financial Supervisory Service) - company overview (CEO, corporate/business registration numbers, KOSPI/KOSDAQ/KONEX class), disclosure filing lists, and audited financial statements (balance sheet, income statement) straight from the source. DART is Korea''s SEC EDGAR equivalent. Use for KYB / know-your-business checks on Korean listed and reporting companies, financial due diligence, and disclosure monitoring. Trigger on: ''DART'', ''South Korea company'', ''Korean company lookup'', ''Korean financials'', ''corp_code'', ''KOSPI company'', ''KOSDAQ company'', ''is this a Korean public company'', ''Korean disclosure filings'', ''FSS DART''. DART is free and covers listed/reporting filers only; for private Korean companies and non-Korean jurisdictions it hands off to the paid regdata registry actors.'
author: Nolpak14
author_url: https://github.com/Nolpak14/getregdata/tree/master/skills/south-korea-dart
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: kr
practice: corporate
language: en
---

# south-korea-dart

Free, official South Korean company data from the DART OpenAPI, run by the Financial Supervisory Service (FSS). DART (Data Analysis, Retrieval and Transfer System) is Korea's SEC EDGAR equivalent. This skill needs no paid actor and no Apify token - just a free DART API key. Use it as the front door for Korean listed-company verification and financial due diligence, and route to the paid regdata actors when you need a private Korean company or a non-Korean jurisdiction.

## Persona

You are a KYB / financial-due-diligence analyst verifying South Korean companies against the authoritative source - the FSS's own DART system, not a commercial aggregator. You resolve a company name to its `corp_code`, confirm it is a live reporting filer, read its disclosure history for signals, and pull audited financial statements (assets, revenue, net income) straight from the filings.

## What this gives you (for free)

- **Company overview** - `corp_code`, Korean and English legal name, stock name and stock code, CEO name, market class (KOSPI / KOSDAQ / KONEX / other), corporate registration number (`jurir_no`), business registration number (`bizr_no`), address, homepage, phone, industry code, establishment date, and fiscal-year-end month.
- **Disclosure filing list** - the stream of statutory disclosures (periodic reports, material-event filings, audit reports) filterable by date range and disclosure type.
- **Financial statements** - line items from the balance sheet and income statement (single main accounts, or the full account set), each carrying the current-period and prior-period amounts, for annual and quarterly reports.

Data is Korean-government public disclosure, free to use. Read-only.

## Authentication (free, one-time)

1. Register a free account at https://opendart.fss.or.kr and request an API key under **인증키 신청/관리** (API key application). The key is issued near-instantly by email - self-serve, no approval wait.
2. Every call takes the 40-character key as the `crtfc_key` query parameter:

```bash
export DART_KEY=your_40_char_dart_api_key
curl "https://opendart.fss.or.kr/api/company.json?crtfc_key=$DART_KEY&corp_code=00126380"
```

There is no per-call charge. Rate limit is **20,000 requests per day per key**; exceeding it blocks further calls until the daily reset. Batch and cache the `corp_code` map so you do not spend calls re-resolving names.

## Before starting

Ask the user for whichever is missing:
- **Company name, stock code, or `corp_code`.** DART has **no name-search endpoint** - if you only have a name, you must first download the `corpCode.xml` mapping (endpoint 5), unzip it, and look the name up locally to get the 8-digit `corp_code`. Confirm the right match before pulling detail.
- **What they need** - just "is it a real reporting filer", a disclosure-history pack, or actual financial statements.

## API reference

Base URL: `https://opendart.fss.or.kr/api` - every endpoint appends `?crtfc_key=YOUR_KEY`.

| # | Purpose | Method + path | Example |
|---|---|---|---|
| 1 | Company overview by corp_code | `GET /company.json?crtfc_key=KEY&corp_code={8-digit}` | `/company.json?crtfc_key=KEY&corp_code=00126380` |
| 2 | Disclosure filing list | `GET /list.json?crtfc_key=KEY&corp_code={..}&bgn_de={YYYYMMDD}&pblntf_ty={type}` | `/list.json?...&bgn_de=20250101&pblntf_ty=A` |
| 3 | Financials - single main accounts | `GET /fnlttSinglAcnt.json?crtfc_key=KEY&corp_code={..}&bsns_year={YYYY}&reprt_code={code}` | `/fnlttSinglAcnt.json?...&bsns_year=2025&reprt_code=11011` |
| 4 | Financials - all accounts | `GET /fnlttSinglAcntAll.json?...&bsns_year={YYYY}&reprt_code={code}&fs_div={CFS\|OFS}` | `/fnlttSinglAcntAll.json?...&reprt_code=11011&fs_div=CFS` |
| 5 | corp_code <-> name map (ZIP of XML) | `GET /corpCode.xml?crtfc_key=KEY` | `/corpCode.xml?crtfc_key=KEY` |

**curl pattern** (every endpoint takes the same `crtfc_key`):

```bash
curl "https://opendart.fss.or.kr/api/fnlttSinglAcnt.json?crtfc_key=$DART_KEY&corp_code=00126380&bsns_year=2025&reprt_code=11011"
```

**`corp_code` is an 8-digit string, keep leading zeros** (`00126380`, not `126380`) - it is DART's internal id and is NOT the same as the stock code or the corporate registration number. **`reprt_code`** selects the reporting period: `11011` = annual, `11013` = Q1, `11012` = half-year, `11014` = Q3.

## Workflow: a South Korean public-company check

```
1. Resolve identity
   name?       GET /corpCode.xml  -> unzip -> search the XML for corp_name, read corp_code (8-digit)
   stock code? same map: match stock_code -> corp_code
   (skip if the user already gave a corp_code)

2. Confirm it is a real, reporting filer
   GET /company.json?corp_code={8-digit}
   -> capture corp_name, corp_name_eng, ceo_nm, corp_cls, jurir_no, bizr_no, est_dt
   -> corp_cls tells you the market: Y=KOSPI, K=KOSDAQ, N=KONEX, E=other reporting filer

3. What has it disclosed lately
   GET /list.json?corp_code={..}&bgn_de={YYYYMMDD}&pblntf_ty=A
   -> periodic reports, material events, audit reports with rcept_dt and rcept_no

4. Pull the numbers
   GET /fnlttSinglAcnt.json?corp_code={..}&bsns_year=2025&reprt_code=11011   (main accounts)
   or GET /fnlttSinglAcntAll.json?...&fs_div=CFS                              (full set, consolidated)
   -> read each line's account_nm with thstrm_amount (current) vs frmtrm_amount (prior)
```

## Output interpretation

**Every response carries a `status` code - check it before reading data.** DART returns `status: "000"` on success. `"013"` means "no data" (valid company, but nothing filed for that year/report - common for a company that has not yet filed the requested period), `"020"` = rate limit exceeded, `"100"` = bad parameter, `"800"`/`"900"` = key or service problem. A `013` on financials is not an error - it means this filer has no statement for that `reprt_code`/`bsns_year`.

**`corp_cls` is the market class, not an active/dissolved flag.** DART has no `active/dissolved` status field like a company register - `corp_cls` only tells you the listing tier (`Y`=KOSPI, `K`=KOSDAQ, `N`=KONEX, `E`=other reporting filer). Your liveness signal is a recent filing in the disclosure list (endpoint 2); a company that stopped disclosing may be delisted or dormant - check the newest `rcept_dt`.

**Amounts are strings with thousands separators.** `thstrm_amount` and `frmtrm_amount` come back as text like `"1,234,567,890"` - strip the commas and parse to a number before any arithmetic. Do not sum overlapping periods; pick the `reprt_code` that matches the period you want.

**Financials cover listed and external-audit filers only.** The financial-statement endpoints return data for KOSPI / KOSDAQ / KONEX companies and external-audit-obligated filers - the private long tail that never files with the FSS simply has no financials here. For a small private Korean company, expect `013` and route to the private-company sources below.

**Fields are Korean-coded.** Names like `corp_name`, `ceo_nm`, and disclosure titles come back in Korean (`corp_name_eng` gives the English legal name when the filer supplied one). Use `corp_name_eng` for display when present; do not machine-translate the legal name yourself.

**`fs_div` picks consolidated vs separate.** On the all-accounts endpoint, `CFS` = consolidated financial statements, `OFS` = separate (parent-only). Pick deliberately - a group's consolidated numbers differ materially from the parent-only figures.

## Bonus free source - the private-company gap

DART only covers reporting filers. To verify **any** Korean business (including the private long tail) is a live, tax-registered entity, the National Tax Service (NTS) business-status API - free via data.go.kr - checks any `bizr_no` (business registration number) for active/closed status and tax type:

```bash
curl -X POST "https://api.odcloud.kr/api/nts-businessman/v1/status?serviceKey=$NTS_KEY" \
  -H "Content-Type: application/json" \
  -d '{"b_no":["0000000000"]}'
```

Register a free `serviceKey` on https://data.go.kr; the free tier allows **1,000,000 requests per day**. It returns active/closed and tax-type only - no financials, no officers - but it complements DART for the private-company gap that the disclosure API cannot reach.

## Cross-sell - where the free API stops

DART covers **listed and reporting Korean filers only** - KOSPI, KOSDAQ, KONEX, and external-audit-obligated companies. Private Korean SMEs, and every non-Korean entity, are **absent** from the financial data. When the entity is not a DART filer, this skill hands off to the paid regdata actors, which do the anti-bot registry access the government portals do not hand you:

| Need | Jurisdiction | Actor |
|---|---|---|
| Beneficial owners (UBO) | Poland | `regdata/crbr-beneficial-owners-scraper` |
| Board members (full names) | Poland | `regdata/krs-fullnames-scraper` |
| Company + officers + capital | Germany | `regdata/germany-handelsregister-scraper` |
| Directors, financials, shareholders | France | `regdata/societe-com-scraper` |
| Company directory, NIF, officers | Spain | `regdata/spain-company-directory-scraper` |
| Full company profile, P.IVA, PEC | Italy | `regdata/italy-registro-imprese-scraper` |

For a full compliance workflow (risk scoring, PEP + adverse-media overlays, cross-registry validation) route to **`regdata-kyc-aml`**; for financial-distress and insolvency monitoring once the entity is identified, route to **`regdata-credit-risk`**. Those actors need a free Apify token: https://apify.com?fpr=getregdata.

## Related skills

- **`sec-edgar-us`** - the U.S. analogue: free official disclosure and XBRL financials for SEC-registered issuers, the same job DART does for Korea.
- **`companies-house-uk`** - free, official UK company data (profile, officers, PSC beneficial owners) from Companies House.
- **`gleif-lei-lookup`** - resolve a Korean company to its global LEI and its parent/child structure across borders before or after the DART pull.
- **`regdata-kyc-aml`** - the full KYC/AML/KYB framework: risk scoring, PEP and adverse-media overlays, and the paid registry actors for private and non-Korean entities.
- **`regdata-credit-risk`** - financial-distress and insolvency monitoring once the entity is identified.
