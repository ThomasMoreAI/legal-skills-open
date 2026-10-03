---
name: eu-ted-procurement
title: eu-ted-procurement
description: 'Search EU public-procurement notices for free via the official TED (Tenders Electronic Daily) Search API - find who won an EU public contract, which above-threshold tenders a company has been awarded, contract-award notices with the winning contractor + value, and open tenders by CPV code, buyer, or country. Use for KYB / due-diligence credibility signals (which EU public contracts has this company won) and for government-buyer lead generation. Trigger on: ''EU tenders'', ''TED'', ''Tenders Electronic Daily'', ''public procurement'', ''contract awards'', ''who won an EU contract'', ''EU public contract search'', ''find government tenders'', ''contract-award notice'', ''which tenders did this company win'', ''CPV code search''. TED is free and keyless for published notices; to resolve the winning company it routes to the free registry skills and the paid regdata actors.'
author: Nolpak14
author_url: https://github.com/Nolpak14/getregdata/tree/master/skills/eu-ted-procurement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: white-collar
language: en
---

# eu-ted-procurement

Free, official EU public-procurement data from the TED (Tenders Electronic Daily) Search API - the EU's supplement journal of above-threshold public tenders. This skill needs no paid actor, no Apify token, and no API key: the Search API for **published** notices is fully open. Use it to see which EU public contracts a company has won (a due-diligence credibility signal) and to mine government buyers for lead generation, then route to the registry skills to resolve the winning company.

## Persona

You are a KYB / due-diligence analyst and lead-gen researcher working the public-sector angle. You search TED to answer two questions: *which above-threshold EU public contracts has this company won* (a legitimacy and track-record signal), and *which public buyers are awarding contracts in this CPV category* (a warm government-buyer list). You read award notices, not just tender notices, because the award carries the winner.

## What this gives you (for free)

- **Notice search** - full-text and field-based expert search across every published TED notice, filterable by CPV classification, buyer, winning organisation, country, publication date, and notice type.
- **Contract-award notices** - the KYB-useful payload: the winning contractor's name + country, the awarded value, the buyer, and the CPV of what was bought.
- **Contract (tender) notices** - open above-threshold tenders with buyer, CPV, estimated value, and submission deadline - the lead-gen and bid-tracking payload.
- **Notice detail** - the full notice retrieved by publication number in XML, PDF, or HTML.

Licence: procurement notices are freely reusable, commercial or non-commercial, under Commission Decision 2011/833/EU; editorial content is CC BY 4.0 (attribution). Read-only.

## Authentication

None for published notices - no key, no registration. Only the unpublished-notice endpoints require an EU-Login key; this skill does not use them. Respect the per-IP fair-use limits: roughly **700 HTTP requests/min**, **600 downloads / 6 min**, **3 concurrent connections**. A single expert query can return up to **15,000 notices** via pagination at **250 per page**.

```bash
curl -X POST "https://api.ted.europa.eu/v3/notices/search" \
  -H "Content-Type: application/json" \
  -d '{"query":"notice-type=\"contract-award\" AND organisation-name=\"ACME\"",
       "fields":["publication-number","notice-type","buyer-name","organisation-name"],
       "page":1,"limit":50}'
```

## Before starting

Ask the user for whichever is missing:
- **Which lane** - the *winner* lane (which contracts a named company has won -> filter to award notices by `organisation-name`) or the *buyer / open-tender* lane (who is buying in a CPV category -> filter by `classification-cpv` + `place-of-performance`).
- **The identifier** - a company name (the contractor/winner), a CPV code, a buyer name, and/or a country + date window to keep result sets under the 15k cap.

## API reference

Base URL: `https://api.ted.europa.eu` - docs `https://docs.ted.europa.eu/api/latest/` - Swagger `https://api.ted.europa.eu/swagger-ui/index.html` - portal `https://developer.ted.europa.eu`

| # | Purpose | Method + path | Notes |
|---|---|---|---|
| 1 | Search notices | `POST /v3/notices/search` | JSON body: `query` (expert-search string), `fields` (array), `page`, `limit` (<=250), `scope` |
| 2 | Get one notice | `GET ted.europa.eu/en/notice/{publication-number}/{format}` | `{format}` = `xml`, `pdf`, or `html` |

**Expert-query syntax is field-based.** Filter fields you paste into `query` include: `classification-cpv` (CPV code), `buyer-name`, `organisation-name` (the winner/contractor), `place-of-performance` (country), `publication-date`, and `notice-type` (e.g. `contract-award`). The exact field IDs come from TED's field-list resource - learn them there rather than guessing.

**Build the query in the UI, paste it into the API.** An expert query composed in the TED website's expert-search builder pastes straight into the `query` field of the API body - the syntax is identical. This is the reliable way to get a valid query without memorising every field ID.

```bash
# Winner lane: contract-award notices won by a named company
curl -X POST "https://api.ted.europa.eu/v3/notices/search" \
  -H "Content-Type: application/json" \
  -d '{"query":"notice-type=\"contract-award\" AND organisation-name=\"COMPANY NAME\"",
       "fields":["publication-number","buyer-name","organisation-name","classification-cpv","publication-date"],
       "page":1,"limit":250}'
```

## Workflow: which EU contracts has this company won

```
1. Pick the lane
   winner lane -> notice-type = contract-award (award carries the winner)
   buyer lane  -> classification-cpv + place-of-performance (open tenders / who is buying)

2. Build the expert query
   compose it in the TED website expert-search builder, copy the query string
   -> paste into the POST /v3/notices/search body as "query"
   -> set "fields" to only what you need (keeps responses small)

3. Search + paginate
   POST /v3/notices/search  with page=1, limit=250
   -> if the set is large, window by publication-date and/or country to stay under 15k
   -> walk pages until you have the notices you need

4. Read the award
   each award notice -> winner/contractor name + country, awarded value, buyer, CPV
   -> for the full notice, GET the publication-number as xml / pdf / html

5. Resolve the winner
   take organisation-name + country -> the registry skills to confirm the legal entity
```

## Output interpretation

**Only award notices carry the winner.** A `contract` (tender) notice announces an *open* tender - buyer, CPV, deadline, estimated value - but no contractor. The winning company appears only on the `contract-award` notice. If you are doing KYB on a supplier, filter `notice-type` to awards; if you are doing lead-gen on open bids, filter to contract notices.

**TED is above-threshold only.** TED publishes EU public tenders **above** the EU thresholds. A company's smaller, below-threshold, or purely national contracts will not appear - absence from TED is not evidence a supplier has no public-sector work, only that it has no *above-threshold EU* awards on record.

**Estimated value != awarded value.** The tender notice's estimated value is the buyer's pre-award budget; the award notice's value is what was actually awarded. Use the award-notice figure for track-record and the tender-notice figure only for pipeline sizing.

**Name matching is fuzzy - confirm the entity.** `organisation-name` is free text as the buyer typed it; the same company can appear under spelling variants, local suffixes, or a subsidiary's name. Treat a name hit as a candidate, then resolve it to a legal entity via the registry skills before asserting "this company won X".

**Mind the 15k cap and the two schemas.** A single query returns at most 15,000 notices - window by date/country to avoid silently truncating a big result set. Notices also come in two schemas (modern eForms vs the legacy TED-XML), so field availability differs by notice age; do not assume every field is present on older notices.

## Cross-sell - from a TED award to the full record

TED tells you a company won a public contract and which country the buyer + winner are in - it does **not** give you directors, owners, financials, or legal status. Use the winner's `organisation-name` + country to pull the actual company record - free where a national skill exists, paid actor otherwise:

| Need | Jurisdiction | Resolve via |
|---|---|---|
| Beneficial owners (UBO) | Poland | `regdata/crbr-beneficial-owners-scraper` |
| Company + officers + capital | Germany | `regdata/germany-handelsregister-scraper` |
| Directors, financials, shareholders | France | `regdata/societe-com-scraper` |
| Company directory, NIF, officers | Spain | `regdata/spain-company-directory-scraper` |
| Company + officers | Italy | `regdata/italy-registro-imprese-scraper` |
| U.S. public filer + financials | USA | free `sec-edgar-us` |

To resolve the winner to its global LEI and corporate structure across borders, route to **`gleif-lei-lookup`**. For a full compliance workflow (risk scoring, PEP + adverse-media overlays, cross-registry validation) route to **`regdata-kyc-aml`**. To turn the government-buyer lane into an outreach list, route to **`regdata-lead-gen`**. Paid actors need a free Apify token: https://apify.com?fpr=getregdata.

## Related skills

- **`sec-edgar-us`** - free U.S. public-company filings and financials once a TED winner turns out to be a U.S. filer.
- **`gleif-lei-lookup`** - resolve a winning contractor to its global LEI and parent/child structure across borders.
- **`regdata-kyc-aml`** - the full KYC/AML/KYB framework: risk scoring, PEP and adverse-media overlays, and the paid registry actors that resolve the winner.
- **`regdata-lead-gen`** - turn the government-buyer / open-tender lane into a qualified outreach list.
- **`vies-vat-validation`** - validate the winning contractor's EU VAT as the cheapest first verification step before pulling its registry record.
