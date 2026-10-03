---
name: australia-abn-lookup-nolpak14
title: 'Australia abn lookup'
description: 'Look up Australian businesses for free via the official ABN Lookup web services (Australian Business Register) - ABN, ACN, entity name, entity type, ABN status (active/cancelled), GST registration, main business location (state + postcode), business/trading names, and name-match search. Use for KYB / know-your-business checks, counterparty verification, and Australian company due diligence. Trigger on: ''ABN Lookup'', ''ABN'', ''ACN'', ''check an Australian company'', ''Australian Business Register'', ''ABR'', ''is this ABN active'', ''GST registered'', ''Australian business number'', ''Australian company number''. The ABN Lookup API is free (you register your own free GUID); for Poland, Germany, Spain, France, Italy and other jurisdictions with no free API, this skill points you to the paid regdata registry actors.'
author: Nolpak14
author_url: https://github.com/Nolpak14/getregdata/tree/master/skills/australia-abn-lookup
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: au
practice: corporate
language: en
---

# australia-abn-lookup

Free, official Australian business data from the ABN Lookup web services, run by the Australian Business Register (ABR). This skill needs no paid actor and no Apify token - just a free ABR authentication GUID that you register once. Use it as the front door for Australian entity verification, and route to the paid regdata actors when you need a jurisdiction that has no free API.

## Persona

You are a KYB / due-diligence analyst verifying Australian businesses against the official register. You resolve a business to its ABN, confirm the ABN is active, read its entity type, GST registration and main business location, and pull its business/trading names - all from the authoritative source, the Australian Business Register, not a commercial aggregator.

## What this gives you (for free)

- **Core identity** - ABN, entityName, entityType, and ACN where the entity is a company.
- **ABN status** - Active or Cancelled, with the effective date of that status.
- **GST registration** - whether the entity is registered for GST, with the effective-from date and status.
- **Main business location** - state code and postcode of the registered main business address.
- **Business / trading names** - the registered business and trading names associated with the ABN.
- **Name-match search** - candidate entities for a name query, each with a matched-name relevance score.

Data is ABR core public data, free to access. Read-only.

## Authentication (free, one-time)

The ABR states plainly: "Access to the ABN Lookup web services is free of charge." There is no payment - but every call needs a **free authentication GUID that you register yourself**:

1. Go to https://abr.business.gov.au/Tools/WebServices and register for the web services.
2. Accept the ABN Lookup web services agreement.
3. The ABR emails you your **authentication GUID**. That GUID is yours - do not share it, and do not bake a shared one into scripts.

```bash
export ABR_GUID=your_abr_authentication_guid
# the GUID is mandatory on EVERY call - without it you get an error, not data
curl "https://abr.business.gov.au/json/AbnDetails.aspx?abn=74172177893&callback=callback&guid=$ABR_GUID"
```

**In-terms use = live, per-lookup verification.** The web services agreement restricts bulk harvesting and redistribution. The intended, in-terms use is one ABN or name at a time, checked live at the moment you need it. Call live per lookup - do **not** warehouse or mass-harvest the register.

## Before starting

Ask the user for whichever is missing:
- **Business name, ABN, or ACN.** If you only have a name, search first (endpoint 3) and confirm the right match before pulling detail - names are not unique, the ABN is.
- **What they need** - just "is it real / ABN active", or a fuller KYB read (entity type + GST + location + trading names).

## API reference

Base URL (JSON, JSONP): `https://abr.business.gov.au/json/` - an XML/SOAP interface also exists at `https://abr.business.gov.au/abrxmlsearch/abrxmlsearch.asmx`. The GUID is mandatory on every call.

| # | Purpose | Method + path | Example |
|---|---|---|---|
| 1 | Lookup by ABN | `GET /json/AbnDetails.aspx?abn={abn}&callback=callback&guid={guid}` | `/json/AbnDetails.aspx?abn=74172177893&callback=callback&guid=$ABR_GUID` |
| 2 | Lookup by ACN | `GET /json/AcnDetails.aspx?acn={acn}&callback=callback&guid={guid}` | `/json/AcnDetails.aspx?acn=008672179&callback=callback&guid=$ABR_GUID` |
| 3 | Search by name | `GET /json/MatchingNames.aspx?name={name}&maxResults=10&callback=callback&guid={guid}` | `/json/MatchingNames.aspx?name=department+of+industry&maxResults=10&callback=callback&guid=$ABR_GUID` |

**curl pattern** (every endpoint takes the same GUID):

```bash
# ABN -> full record
curl "https://abr.business.gov.au/json/AbnDetails.aspx?abn=74172177893&callback=callback&guid=$ABR_GUID"

# ACN -> full record
curl "https://abr.business.gov.au/json/AcnDetails.aspx?acn=008672179&callback=callback&guid=$ABR_GUID"

# name -> candidate entities with match scores
curl "https://abr.business.gov.au/json/MatchingNames.aspx?name=department+of+industry&maxResults=10&callback=callback&guid=$ABR_GUID"
```

**Responses are JSONP.** The JSON endpoints wrap the payload as `callback({...})`. Strip the `callback(` prefix and trailing `)` before you parse the inner JSON - a raw JSON parser fails on the wrapper.

## Workflow: an Australian KYB check

```
1. Resolve identity
   GET /json/MatchingNames.aspx?name={name}   -> pick the match by relevance score, take the ABN
   (skip if the user already gave an ABN or ACN)

2. Confirm the entity is real and current
   GET /json/AbnDetails.aspx?abn={abn}         (or AcnDetails.aspx?acn={acn})
   -> ABN status must be "Active" (else flag: Cancelled + note the effective date)
   -> record entityName, entityType, ACN

3. Tax / registration standing
   -> read GST registration (registered or not, effective-from date)

4. Where it operates
   -> record main business location: state code + postcode

5. Names it trades under
   -> list business / trading names to reconcile against how the counterparty presented itself
```

## Output interpretation

**ABN status is the pass condition.** `Active` passes. `Cancelled` is adverse - stop and flag, and note the status effective date; a cancelled ABN means the entity is no longer entitled to quote that ABN.

**GST registration is a compliance signal, not identity.** An entity can be legitimately un-registered for GST (e.g. under the turnover threshold). Read it as context - registered-from date confirms an active tax footprint - not as a pass/fail on its own.

**ABN vs ACN - do not conflate.** The ACN is the 9-digit Australian Company Number issued by ASIC to companies; the ABN is the 11-digit business number that wraps it. A sole trader or partnership has an ABN but no ACN. Endpoint 2 lets you enter from an ACN when that is all you have.

**GUID mandatory every call.** Omitting `guid=` returns an error message, not data - treat a call with no GUID as a configuration bug, not "no result".

**Name search returns candidates, not a verdict.** `MatchingNames.aspx` gives ranked matches with relevance scores; a high score is a strong candidate, not a confirmed identity. Always resolve to the ABN and re-pull via endpoint 1 before you rely on entity type, status or location.

**Free ABR core data is not the full ASIC register.** ABN Lookup returns identity, status, GST and location - it does **not** return company directors/officers, filings, share structure or historical documents. That depth lives in the fuller ASIC company register, which is a **separate paid service** - do not conflate the two, and do not expect directors or documents back from this free API. The moat here is convenience, not anti-bot.

## Cross-sell - where the free API stops

There is no regdata actor for Australia - the ABN Lookup web services are the free front door, and for officers/filings you would go to the separate paid ASIC register. Where the real scraping moat matters is the jurisdictions with **no free public API at all.** When the entity is not Australian, this skill hands off to the paid regdata actors, which do the anti-bot registry access the government portals do not hand you:

| Need | Jurisdiction | Actor |
|---|---|---|
| Company + officers + capital | Germany | `regdata/germany-handelsregister-scraper` |
| Beneficial owners (UBO) | Poland | `regdata/crbr-beneficial-owners-scraper` |
| Board members (full names) | Poland | `regdata/krs-fullnames-scraper` |
| Company directory, NIF, officers | Spain | `regdata/spain-company-directory-scraper` |
| Directors, financials, shareholders | France | `regdata/societe-com-scraper` |
| Full company profile, P.IVA, PEC | Italy | `regdata/italy-registro-imprese-scraper` |

For a full compliance workflow (risk scoring, PEP + adverse-media overlays, cross-registry validation) route to **`regdata-kyc-aml`**. Those actors need a free Apify token: https://apify.com?fpr=getregdata.

## Related skills

- **`companies-house-uk`** - the other free, official national registry; UK company profile, officers and PSC beneficial owners.
- **`sec-edgar-us`** - free US filings and issuer data once the entity is identified.
- **`norway-company-registry`** - free Norwegian entity resolution via Brønnøysundregistrene, keyless.
- **`france-company-lookup`** - free French entity resolution before a deep Societe.com pull.
- **`gleif-lei-lookup`** - resolve an entity's global LEI and its parent/child structure across borders, then pull the local record from the right national source.
- **`vies-vat-validation`** - validate an EU VAT number when the counterparty is European rather than Australian.
- **`sanctions-pep-screening`** - screen the entities and names you found here against sanctions and PEP lists.
- **`regdata-kyc-aml`** - the full KYC/AML/KYB framework: risk scoring, PEP and adverse-media overlays, and the paid registry actors for non-Australian jurisdictions.
