---
name: world-bank-contracts
title: World bank contracts
description: 'Search World Bank-financed contracts and projects for free via the official World Bank Search API - find which World Bank contracts a company has won, who won World Bank contracts, contract-award amounts and winning suppliers, development-finance projects by country/sector, and awards by supplier country. Use for KYB / due-diligence credibility signals (which World Bank contracts has this company won) and for development-finance supplier lead generation. Trigger on: ''World Bank contracts'', ''World Bank projects'', ''development finance'', ''contract awards'', ''who won World Bank contracts'', ''World Bank supplier lookup'', ''World Bank-financed contract'', ''which World Bank contracts did this company win'', ''World Bank procurement'', ''IBRD/IDA contract''. The World Bank Search API is free and keyless; to resolve the winning company it routes to the free registry skills and the paid regdata actors.'
author: Nolpak14
author_url: https://github.com/Nolpak14/getregdata/tree/master/skills/world-bank-contracts
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: cross-jurisdiction
practice: white-collar
language: en
---

# world-bank-contracts

Free, official World Bank data from the World Bank Search API - the public search layer over the Bank's operations, covering every IBRD/IDA project and the contract awards financed under them. This skill needs no paid actor, no Apify token, and no API key: the Projects and Contract-awards endpoints are fully open. Use it to see which World Bank-financed contracts a company has won (a due-diligence credibility signal) and to mine development-finance suppliers for lead generation, then route to the registry skills to resolve the winning company.

## Persona

You are a KYB / due-diligence analyst and lead-gen researcher working the development-finance angle. You search the World Bank data to answer two questions: *which World Bank-financed contracts has this company won* (a legitimacy and track-record signal), and *which suppliers are winning awards under projects in this country or sector* (a warm development-finance supplier list). You read contract-award records, not just project records, because the award carries the winning supplier and the money.

## What this gives you (for free)

- **Contract-award search by supplier** - the money endpoint: free-text supplier match plus filters on supplier country and project, each award carrying the winning supplier's name, the awarded amount, the procurement method, and the parent project.
- **Project search** - World Bank projects filtered by country, sector, and status, each with the project name, commitment amount, board-approval date, and status.
- **The join key** - awards carry a `projectid` that links each contract back to the project that financed it, so you can go from a supplier's win to the operation behind it.
- **Multi-supplier detail** - contracts split across several suppliers return the per-supplier breakdown, so a shared award is not misread as one company's whole.

Licence: CC BY 4.0 (attribution). Read-only.

## Authentication

None - no key, no registration. Both endpoints return clean `200`s over plain `GET`. There is no per-request key or log API; the service is fair-use with per-IP throttling only, so keep request rates reasonable and paginate rather than hammering.

```bash
curl "https://search.worldbank.org/api/contractdata?format=json&qterm=Siemens&rows=20"
```

## Before starting

Ask the user for whichever is missing:
- **Which lane** - the *supplier* lane (which contracts a named company has won -> `contractdata` with `qterm` on the supplier name) or the *project / lead-gen* lane (who is winning under operations in a country or sector -> `projects` filtered by `countryshortname` + `sector1`, then the awards under those projects).
- **The identifier** - a company name (fuzzy supplier match via `qterm`), and/or a supplier country, a `projectid`, a country, and a sector to keep result sets manageable.

## API reference

Base URL: `https://search.worldbank.org/api` - portal `https://projects.worldbank.org` - both endpoints live on the same host.

| # | Purpose | Method + path | Notes |
|---|---|---|---|
| 1 | Contract awards by supplier | `GET /contractdata` | query params: `format=json`, `qterm` (free-text supplier), `supplier_countryshortname`, `projectid`, `rows`, `os` -> `{total, ...}` |
| 2 | Projects by country/sector/status | `GET /v2/projects` | query params: `format=json`, `countryshortname`, `sector1`, `rows`, `os` -> `{total, projects{}}` |

**Filters go in query params, not a body.** `qterm` is a fuzzy free-text match against supplier records - it is the supplier lane's entry point. Narrow it with `supplier_countryshortname` (the supplier's country) or `projectid` (awards under one operation). On the projects endpoint, filter by `countryshortname`, `sector1`, and project status. Paginate with `rows` (page size) and `os` (offset); a single request caps at **1000 rows**, so walk `os` for anything larger.

```bash
# Supplier lane: contract awards won by a named company
curl "https://search.worldbank.org/api/contractdata?format=json&qterm=Siemens&rows=20"

# Project lane: active operations in one country
curl "https://search.worldbank.org/api/v2/projects?format=json&countryshortname=Kenya&rows=20"
```

## Workflow: which World Bank contracts has this company won

```
1. Pick the lane
   supplier lane -> contractdata?qterm=COMPANY (the award carries the winner)
   project lane  -> v2/projects?countryshortname=...&sector1=... (who is winning under operations)

2. Search the awards
   GET /contractdata?format=json&qterm=COMPANY&rows=1000
   -> narrow with supplier_countryshortname to disambiguate a common name
   -> each award: supp_name[], total_contr_amnt, procu_meth_text, projectid

3. Read the award
   supp_name[] aligns index-wise with supplier_contr_amount[]
   -> for a multi-supplier contract, read the per-supplier split, not just the total
   -> procurement_group_desc tells you Goods vs Consultant Services

4. Join back to the project
   take projectid -> GET /v2/projects?format=json&id=PROJECTID
   -> project_name, countryname, sector1, curr_total_commitment, boardapprovaldate

5. Paginate + resolve the supplier
   walk os/rows until you have every award (1000-row cap per request)
   -> take supp_name + supplier_countryshortname -> the registry skills to confirm the entity
```

## Output interpretation

**`qterm` is fuzzy - dedupe the supplier.** The match is loose free text, and one company appears under many spellings, local suffixes, and subsidiary names across countries. Narrow with `supplier_countryshortname` and treat a name hit as a candidate, then resolve it to a legal entity via the registry skills before asserting "this company won X" - do not sum awards across name variants without confirming they are the same entity.

**Multi-supplier awards are parallel arrays.** A contract split across several suppliers returns `supp_name[]` and `supplier_contr_amount[]` as arrays that align index-wise (with a nested `suppinfo[]` per supplier). The value one company received is its element of `supplier_contr_amount[]`, not `total_contr_amnt` - reading the total as one supplier's share overstates its win on shared contracts.

**Projects and awards are two separate endpoints.** `contractdata` carries the supplier and the money; `v2/projects` carries the operation, its commitment, and its status. Neither returns the other's payload - join them on `projectid`. A project record is not proof any specific supplier was paid, and an award is not a full picture of the operation behind it.

**This is development-finance only.** It covers contracts financed under World Bank (IBRD/IDA) operations - not the company's commercial contracts, and not other multilateral lenders' procurement. Absence here is not evidence a company has no public-sector work, only that it has no *World Bank-financed* awards on record.

**Do not build on the old finances.worldbank.org host.** The legacy `finances.worldbank.org` Socrata/SODA path is dead - it 302-redirects to the `financesone.worldbank.org` SPA and its `/resource/*.json` endpoints 404. Use `search.worldbank.org` for both projects and contract awards; anything pointing at `finances*.worldbank.org` will silently fail.

**Paginate - 1000 rows max per request.** A single call returns at most 1000 rows; the response `total` tells you the full count. For a prolific supplier or a large country, walk `os` in steps of `rows` until you have covered `total`, or you will silently truncate a long award history.

## Cross-sell - from a World Bank award to the full record

The World Bank data tells you a company won a development-financed contract and which country the supplier is in - it does **not** give you directors, owners, financials, or legal status. Use the supplier name + supplier country to pull the actual company record - free where a national skill exists, paid actor otherwise:

| Need | Jurisdiction | Resolve via |
|---|---|---|
| Beneficial owners (UBO) | Poland | `regdata/crbr-beneficial-owners-scraper` |
| Company + officers + capital | Germany | `regdata/germany-handelsregister-scraper` |
| Directors, financials, shareholders | France | `regdata/societe-com-scraper` |
| Company directory, NIF, officers | Spain | `regdata/spain-company-directory-scraper` |
| U.S. public filer + financials | USA | free `sec-edgar-us` |
| Global LEI + parent/child structure | Cross-border | free `gleif-lei-lookup` |

For the EU and U.S. sides of a company's government exposure, route to **`eu-ted-procurement`** (above-threshold EU public tenders and awards) and **`us-federal-awards`** (U.S. federal contracts and grants) - together these three are the global public-procurement lanes. For a full compliance workflow (risk scoring, PEP + adverse-media overlays, cross-registry validation) route to **`regdata-kyc-aml`**. To turn the development-finance supplier lane into an outreach list, route to **`regdata-lead-gen`**. Paid actors need a free Apify token: https://apify.com?fpr=getregdata.

## Related skills

- **`eu-ted-procurement`** - the EU lane: free above-threshold EU public tenders and contract-award notices, for a company's EU government exposure.
- **`us-federal-awards`** - the U.S. lane: free federal contracts and grants from USAspending, for a company's U.S. government exposure.
- **`regdata-kyc-aml`** - the full KYC/AML/KYB framework: risk scoring, PEP and adverse-media overlays, and the paid registry actors that resolve the supplier.
- **`regdata-lead-gen`** - turn the development-finance supplier / project lane into a qualified outreach list.
- **`gleif-lei-lookup`** - resolve a winning supplier to its global LEI and parent/child structure across borders.

## More on getregdata.com

- All skills and paid registry coverage: https://getregdata.com/skills/ and https://getregdata.com/registries/
