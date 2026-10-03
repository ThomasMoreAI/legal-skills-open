---
name: croatia-sudreg-nolpak14
title: 'Croatia sudreg'
description: 'Look up Croatian companies for free via the official Sudski registar OPEN API (sudreg-data.gov.hr, Ministry of Justice court register) - company profile, OIB (tax ID), MBS (court register number), tvrtka (legal name), pravni oblik (legal form), status, sjediste (registered seat), temeljni kapital (share capital), datum osnivanja, and osobe (board / authorized persons). Use for KYB / know-your-business checks, counterparty verification, director discovery, and Croatian company due diligence. Trigger on: ''Croatia company'', ''Croatian company lookup'', ''sudski registar'', ''sudreg'', ''court register'', ''check a Croatian company'', ''OIB lookup'', ''MBS lookup'', ''is this Croatian company active''. The sudski registar OPEN API is free (after a one-time free registration); for Poland, Germany, Spain, France, Italy and other jurisdictions with no free API, this skill points you to the paid regdata registry actors.'
author: Nolpak14
author_url: https://github.com/Nolpak14/getregdata/tree/master/skills/croatia-sudreg
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: hr
practice: corporate
language: en
---

# croatia-sudreg

Free, official Croatian company data from the Sudski registar OPEN API (sudreg-data.gov.hr), run by the Ministry of Justice. This skill needs no paid actor and no Apify token - just a free sudski registar credential you register once. Use it as the front door for Croatian entity verification, and route to the paid regdata actors when you need a jurisdiction that has no free API.

## Persona

You are a KYB / due-diligence analyst verifying Croatian companies against the official court register. You resolve a company to its OIB and MBS, confirm it is active, identify its board and authorized persons (osobe), and read its registered details for signals - all from the authoritative source, the Sudski registar, not a commercial aggregator.

## What this gives you (for free)

- **Company profile** - tvrtka (full legal name) and skracena_tvrtka (short name), OIB (11-digit tax ID), MBS (9-digit court register number), pravni oblik (legal form, e.g. d.o.o. / d.d. / j.d.o.o.), and status.
- **Registered seat** - sjediste (street, number, settlement), the address of record.
- **Founding and capital** - datum osnivanja (founding date) and temeljni kapital (share capital).
- **People** - osobe, the board and authorized persons behind the company.

Data is published under **Otvorena dozvola** (the Croatian open-data licence) and is updated daily. Read-only.

## Authentication (free, one-time)

The OPEN API is free but **not** keyless - it requires a free registration, then an OAuth token per session:

1. Register a free account at **https://sudreg-data.gov.hr** and, on approval, you receive a **Client ID** and **Client Secret**.
2. Exchange the credential for a bearer token (valid **6 hours**), then call the public data endpoints with it:

```bash
export SUDREG_ID=your_client_id
export SUDREG_SECRET=your_client_secret

# 1) Fetch an OAuth bearer token (valid 6h)
curl -s -u "$SUDREG_ID:$SUDREG_SECRET" \
  -d "grant_type=client_credentials" \
  "https://sudreg-data.gov.hr/api/oauth/token"
# -> {"access_token":"...","expires_in":21600,...}

# 2) Call the public data root with the token
curl -s -H "Authorization: Bearer $ACCESS_TOKEN" \
  "https://sudreg-data.gov.hr/api/OpenAPIs/OpenAPIJavni/detalji_subjekta?tip_identifikatora=oib&identifikator=<OIB>&expand_relations=true"
```

There is no per-call charge and no published rate limit or fee. **Refresh the token every 6 hours** - a stale token returns 401. A separate test host, **https://sudreg-data-test.gov.hr**, exists for integration testing; use the production host for real lookups.

## Before starting

Ask the user for whichever is missing:
- **OIB or MBS.** The public API is identifier-centric - it resolves an entity by its 11-digit **OIB** (tax ID) or 9-digit **MBS** (court register number), not by a fuzzy name query. If the user only has a company name, see the name-search caveat below.
- **What they need** - just "is it real/active", or a full KYB pack (osobe + status + capital).

## API reference

Base URL: `https://sudreg-data.gov.hr/api/OpenAPIs/OpenAPIJavni`  (OAuth token host: `https://sudreg-data.gov.hr/api/oauth/token`)

| # | Purpose | Method + path | Example |
|---|---|---|---|
| 1 | Lookup by OIB or MBS | `GET /detalji_subjekta?tip_identifikatora={oib\|mbs}&identifikator={id}&expand_relations=true` | `/detalji_subjekta?tip_identifikatora=oib&identifikator=<OIB>&expand_relations=true` |
| 2 | Bulk / paginated subject list | `GET /subjekt` (GetAllWithPaging) | `/subjekt?offset=0&limit=100` |
| 3 | Code list - courts | `GET /sudovi` | `/sudovi` |
| 4 | Code list - legal forms | `GET /pravni_oblici` | `/pravni_oblici` |

**One-call detail.** Endpoint 1 with `expand_relations=true` returns the full company record - profile, seat, capital, and osobe - in a single call. Prefer it when you already have an OIB or MBS.

**Identifiers are strings, keep leading zeros.** OIB is 11 digits, MBS is 9 digits. Use the canonical identifier verbatim; do not strip a leading zero from an MBS.

**No fuzzy name search.** The public API is OIB/MBS-centric - there is **no name-search (tvrtka) endpoint**. To search by company name you bulk-pull the subject list (endpoint 2, paginated) and index the tvrtka/skracena_tvrtka fields locally, then look up the matched OIB with endpoint 1. State this to the user up front - a "search by name" request is a bulk-then-index job, not a single call.

## Workflow: a Croatian KYB check

```
1. Resolve identity
   -> if you have an OIB/MBS, skip to step 2
   -> if you only have a name: GET /subjekt (paginated) once, index tvrtka locally,
      match the company, take its OIB

2. Confirm the entity is real and current
   GET /detalji_subjekta?tip_identifikatora=oib&identifikator={oib}&expand_relations=true
   -> status must be active (else flag: in liquidation / deleted)
   -> record pravni oblik, sjediste, datum osnivanja, temeljni kapital

3. Who runs it
   -> read osobe from the same expanded record (board and authorized persons)

4. Cross-check the codes
   -> resolve pravni oblik against /pravni_oblici and the court against /sudovi if needed
```

## Output interpretation

**status is the pass/adverse signal.** An active subject is the pass condition; a subject in liquidation (likvidacija / stecaj) or deleted from the register is adverse - stop and flag; a deleted company cannot trade.

**OIB is the tax ID, MBS is the court number.** OIB (11 digits) is the national tax/identity number and the stable join key across Croatian sources; MBS (9 digits) is the court register (maticni broj subjekta) number. Both identify the same entity - use whichever the user supplied and record both from the result.

**Fields are Croatian.** tvrtka = full legal name, skracena_tvrtka = short name, sjediste = registered seat, pravni oblik = legal form, temeljni kapital = share capital, datum osnivanja = founding date, osobe = board / authorized persons. Map them to your KYB schema; do not assume English field names.

**No direct name search - bulk then index.** The API cannot fuzzy-match a name. Pulling the whole subject list per lookup is wasteful; if you expect repeat name lookups, cache the indexed subject list and refresh it (the data updates daily), rather than re-pulling per query.

**Watch the host and version.** Use `sudreg-data.gov.hr` - a legacy Azure APIM host (`sudreg-podaci.pravosudje.hr`) still appears in older docs and should not be used. The developer guide is versioned (v3.0.0) and public endpoints sit under the `/javni/` (OpenAPIJavni) path; pin to the documented version so a field rename does not break parsing silently.

## Cross-sell - where the free front door leads

Croatia (like the UK, Denmark and Norway) is an outlier: an official, structured, free-after-registration OPEN API with no anti-bot wall - so there is no scraping moat here. Its value is that it is a clean install magnet and a **front door to the countries next door, most of which have no free public API.** When the entity is not Croatian, this skill hands off to the paid regdata actors, which do the anti-bot registry access the government portals do not hand you:

| Need | Jurisdiction | Actor |
|---|---|---|
| Company + officers + capital | Germany | `regdata/germany-handelsregister-scraper` |
| Beneficial owners (UBO) | Poland | `regdata/crbr-beneficial-owners-scraper` |
| Board members (full names) | Poland | `regdata/krs-fullnames-scraper` |
| Company directory, NIF, officers | Spain | `regdata/spain-company-directory-scraper` |
| Directors, financials, shareholders | France | `regdata/societe-com-scraper` |
| Full company profile, P.IVA, PEC | Italy | `regdata/italy-registro-imprese-scraper` |

There is no Croatian regdata actor - the free sudski registar OPEN API above is the whole toolkit for Croatia. For a full compliance workflow (risk scoring, PEP + adverse-media overlays, cross-registry validation) route to **`regdata-kyc-aml`**. Those actors need a free Apify token: https://apify.com?fpr=getregdata.

## Related skills

- **`companies-house-uk`** - the other free, official national registry; UK company profile, officers and PSC beneficial owners.
- **`denmark-cvr`** - free Danish entity resolution and participants/management via the CVR distribution.
- **`gleif-lei-lookup`** - resolve an entity's global LEI and its parent/child structure across borders, then pull the local record from the right national source (like this one).
- **`vies-vat-validation`** - confirm the Croatian `HR`-prefixed VAT number is valid and active for EU cross-border trade.
- **`regdata-kyc-aml`** - the full KYC/AML/KYB framework: risk scoring, PEP and adverse-media overlays, and the paid registry actors for non-Croatian jurisdictions.
