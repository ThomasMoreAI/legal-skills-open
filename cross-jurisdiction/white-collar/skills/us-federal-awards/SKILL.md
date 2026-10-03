---
name: us-federal-awards
title: 'Us federal awards'
description: 'Search U.S. federal spending for free via the official USAspending.gov API - find which US federal contracts and grants a company has received, who receives US government money, award amounts and awarding agencies, recipient UEI/DUNS lookup, and federal awards by NAICS/PSC or period. Use for KYB / due-diligence credibility signals (which US federal contracts or grants has this company won) and for government-contractor lead generation. Trigger on: ''USAspending'', ''US federal contracts'', ''federal awards'', ''government awards'', ''government grants'', ''who receives US government money'', ''federal contractor lookup'', ''find US government contracts'', ''recipient UEI lookup'', ''which federal grants did this company get'', ''DUNS lookup''. USAspending is free and keyless; to resolve the recipient''s corporate record it routes to the free registry skills and the paid regdata actors.'
author: Nolpak14
author_url: https://github.com/Nolpak14/getregdata/tree/master/skills/us-federal-awards
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: white-collar
language: en
---

# us-federal-awards

Free, official U.S. federal spending data from the USAspending.gov API - the U.S. Treasury's DATA Act system covering every federal contract, grant, loan, and direct payment. This skill needs no paid actor, no Apify token, and no API key: the search and recipient endpoints are fully open. Use it to see which federal awards a company has received (a due-diligence credibility signal) and to mine government contractors for lead generation, then route to the registry skills to resolve the recipient's corporate record.

## Persona

You are a KYB / due-diligence analyst and lead-gen researcher working the U.S. federal-spending angle. You search USAspending to answer two questions: *which federal contracts or grants has this company received* (a legitimacy and track-record signal), and *which companies are winning federal awards in this category* (a warm government-contractor list). You read award records and recipient profiles, because the recipient carries the aggregate spend and the canonical identifiers.

## What this gives you (for free)

- **Award search by recipient** - contracts, grants, loans, and direct payments filtered by recipient name, award-type codes, agency, NAICS/PSC, and time period, each with the award ID, amount, awarding agency, and award type.
- **Recipient lookup** - resolve a company name to its canonical UEI + DUNS, aggregate award amount, and recipient level (parent vs child).
- **Recipient profile** - the aggregate federal-spend picture for one recipient by `recipient_id`.
- **Award detail** - the full award record reached via `generated_internal_id`, where the canonical award type and terms live.

Data is U.S. government work in the public domain - free reuse, no licence fee. Read-only.

## Authentication

None - no key, no registration. Both `GET` and `POST` return clean `200`s. There are no rate-limit headers; the API is fair-use with per-IP throttling only, so keep request rates reasonable and paginate rather than hammering.

```bash
curl -X POST "https://api.usaspending.gov/api/v2/recipient/duns/" \
  -H "Content-Type: application/json" \
  -d '{"keyword":"Lockheed","limit":50}'
```

## Before starting

Ask the user for whichever is missing:
- **Which lane** - the *recipient* lane (which awards a named company has received -> search by `recipient_search_text`, then confirm via the recipient endpoint) or the *category / lead-gen* lane (who is winning awards in a NAICS/PSC or agency -> filter by those plus a time period).
- **The identifier** - a company name (fuzzy recipient match), and/or the award-type codes, agency, NAICS/PSC, and a date window to keep result sets manageable.

## API reference

Base URL: `https://api.usaspending.gov/api/v2/` - portal `https://www.usaspending.gov` - docs `https://api.usaspending.gov/docs/endpoints`

| # | Purpose | Method + path | Notes |
|---|---|---|---|
| 1 | Search awards by recipient | `POST /search/spending_by_award/` | JSON body: `filters` (object), `fields` (array), `page`, `limit` (<=100) |
| 2 | Recipient lookup | `POST /recipient/duns/` | JSON body: `keyword`, `limit` -> UEI, DUNS, name, aggregate amount, recipient_level |
| 3 | Recipient profile | `GET /recipient/{recipient_id}/` | aggregate federal-spend picture for one recipient |

**Filters go in a POST body object, not query params.** Award-type codes select the spend category: contracts `A,B,C,D`; grants `02,03,04,05`; loans `07,08`; direct payments `06,10`; other `09,11`. `recipient_search_text` is a fuzzy name match. `time_period` is an array of `{start_date, end_date}`. Selectable `fields` include `Award ID`, `Recipient Name`, `recipient_id`, `Award Amount`, `Awarding Agency`, `Award Type`, plus NAICS/PSC, period-of-performance dates, and place-of-performance.

```bash
# Recipient lane: awards received by a named company
curl -X POST "https://api.usaspending.gov/api/v2/search/spending_by_award/" \
  -H "Content-Type: application/json" \
  -d '{"filters":{"recipient_search_text":["Lockheed Martin"],
        "award_type_codes":["A","B","C","D"],
        "time_period":[{"start_date":"2020-01-01","end_date":"2026-01-01"}]},
       "fields":["Award ID","Recipient Name","Award Amount","Awarding Agency","Award Type","recipient_id"],
       "page":1,"limit":100}'
```

## Workflow: which US federal awards has this company received

```
1. Pick the lane
   recipient lane -> recipient_search_text (which awards a named company received)
   category lane  -> award_type_codes + NAICS/PSC + agency (who is winning in a category)

2. Resolve the recipient
   POST /recipient/duns/  {"keyword":"COMPANY","limit":50}
   -> canonical name, UEI + DUNS, aggregate amount, recipient_level, recipient_id
   -> pick the right variant before trusting a name (see Output interpretation)

3. Search the awards
   POST /search/spending_by_award/  with filters + fields + page=1, limit=100
   -> set award_type_codes to the spend categories you want
   -> window by time_period to keep the set manageable

4. Paginate + read
   walk pages via page/limit until you have the awards you need
   -> each row: Award ID, Award Amount, Awarding Agency, Award Type
   -> for the canonical award record, follow generated_internal_id to award detail

5. Resolve the recipient's corporate record
   take Recipient Name + UEI -> the registry skills to confirm the legal entity
```

## Output interpretation

**`recipient_search_text` is fuzzy - dedupe the recipient.** The name match is loose, and one company appears under many spellings, suffixes, and UEIs (parent vs subsidiary). Resolve to a canonical recipient via `POST /recipient/duns/` and its `recipient_level` before asserting "this company received X" - do not sum awards across name variants without confirming they are the same entity.

**Award Type can be null in aggregate search.** The `Award Type` field in `spending_by_award/` results is sometimes empty. For the canonical type and terms, follow `generated_internal_id` to the award-detail record, or read the recipient endpoint - do not treat a null in the search row as "type unknown for the award".

**Award-type codes decide what you see.** A search only returns the spend categories in `award_type_codes`. Contracts (`A,B,C,D`) and grants (`02,03,04,05`) are different result sets - if you filter to contracts only, a company's federal grants will not appear, and vice versa. Include every category you care about, or run the lanes separately.

**USAspending is federal only.** It covers federal contracts, grants, loans, and direct payments - not state, county, or municipal spending, and not private commercial contracts. Absence from USAspending is not evidence a company has no public-sector work, only that it has no *federal* awards on record.

**Pagination caps at 100 per page.** `limit` maxes at 100 in `spending_by_award/`; walk `page` for the full set, and window by `time_period` for a prolific recipient so you do not silently truncate a long award history.

## Cross-sell - from a federal award to the full record

USAspending tells you a company received federal money and its UEI/DUNS - it does **not** give you directors, owners, financials, or legal status. Use the recipient name + UEI to pull the actual company record - free where a national skill exists, paid actor otherwise:

| Need | Jurisdiction | Resolve via |
|---|---|---|
| U.S. public filer + financials | USA | free `sec-edgar-us` |
| Private California company records | USA (California) | `regdata/california-sos-business-scraper` |
| UCC liens / secured filings | USA (California) | `regdata/california-ucc-lien-scraper` |
| Beneficial owners (UBO) | Poland | `regdata/crbr-beneficial-owners-scraper` |
| Company + officers + capital | Germany | `regdata/germany-handelsregister-scraper` |
| Directors, financials, shareholders | France | `regdata/societe-com-scraper` |

To screen a federal recipient for **debarment or suspension**, pair this with **`sam-gov-exclusions`** - a company on the SAM.gov exclusions list should not be receiving new federal awards. For the EU side of a company's government exposure, route to **`eu-ted-procurement`** (EU public tenders and contract awards). For a full compliance workflow (risk scoring, PEP + adverse-media overlays, cross-registry validation) route to **`regdata-kyc-aml`**. To turn the government-contractor lane into an outreach list, route to **`regdata-lead-gen`**. Paid actors need a free Apify token: https://apify.com?fpr=getregdata.

## Related skills

- **`eu-ted-procurement`** - the EU counterpart: free above-threshold EU public tenders and contract-award notices, for a company's non-U.S. government exposure.
- **`sam-gov-exclusions`** - screen a federal recipient against the SAM.gov debarment / suspension list before trusting an award history.
- **`sec-edgar-us`** - free U.S. public-company filings and financials once a federal recipient turns out to be an SEC filer.
- **`regdata-kyc-aml`** - the full KYC/AML/KYB framework: risk scoring, PEP and adverse-media overlays, and the paid registry actors that resolve the recipient.
- **`regdata-lead-gen`** - turn the government-contractor / federal-award lane into a qualified outreach list.
