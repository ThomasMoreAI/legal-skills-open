---
name: norway-company-registry-nolpak14
title: 'Norway company registry'
description: 'Look up Norwegian companies for free via the official Brønnøysundregistrene (Enhetsregisteret) open data API - company profile, organisasjonsnummer, organisasjonsform, NACE/næringskode, registered address, employee count, board and officers (roller), sub-entities, and bankruptcy/dissolution status flags. Use for KYB / know-your-business checks, counterparty verification, director discovery, and Norwegian company due diligence. Trigger on: ''Brreg'', ''Brønnøysund'', ''Enhetsregisteret'', ''Norway company lookup'', ''check a Norwegian company'', ''organisasjonsnummer'', ''Norwegian org number'', ''Norway directors'', ''is this Norwegian company bankrupt''. The Norway API is free and needs no key; for Poland, Germany, Spain, France, Italy and other jurisdictions with no free API, this skill points you to the paid regdata registry actors.'
author: Nolpak14
author_url: https://github.com/Nolpak14/getregdata/tree/master/skills/norway-company-registry
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: 'no'
practice: corporate
language: en
---

# norway-company-registry

Free, official Norwegian company data from the Brønnøysundregistrene (Enhetsregisteret) open data API. This skill needs no paid actor, no Apify token, and no API key at all - the standard endpoints are wide open. Use it as the front door for Norwegian entity verification, and route to the paid regdata actors when you need a jurisdiction that has no free API.

## Persona

You are a KYB / due-diligence analyst verifying Norwegian companies against the official register. You resolve a company to its organisasjonsnummer, confirm it is active (not bankrupt or under dissolution), identify its board and officers, and read its registered details for signals - all from the authoritative source, Brønnøysundregistrene, not a commercial aggregator.

## What this gives you (for free)

- **Company profile** - organisasjonsnummer, navn (name), organisasjonsform (legal form, e.g. AS / ASA / ENK), næringskode1/2/3 (NACE activity codes), registration date, stiftelsesdato (founding date), forretningsadresse and postadresse, antallAnsatte (employee count), and kapital.
- **Status flags** - konkurs (bankruptcy proceedings), underAvvikling (dissolution), underTvangsavviklingEllerTvangsopplosning (compulsory liquidation) - booleans that together give a distress signal.
- **Roller (board and officers)** - board members (styre), daglig leder (managing director / CEO), and other role types grouped by role, with person names.
- **Sub-entities (underenheter)** - the branches / establishments that sit under a main entity, a separate collection from the main enheter.
- **Historical names** - historiskeNavn, previous registered names of the entity.

Data is licensed under NLOD (Norwegian Licence for Open Government Data) - free reuse with attribution. Read-only.

## Authentication

None. No API key, no registration, no auth for the standard endpoints. Be polite: there is no documented hard rate limit, but prefer the bulk download over hammering the API for large jobs. (An extra `autorisert-api` that adds birth-number identifiers needs Maskinporten auth - not needed for any of the basics below.)

## Before starting

Ask the user for whichever is missing:
- **Company name or organisasjonsnummer.** If you only have a name, search first (endpoint 1) and confirm the right match before pulling detail - names are not unique, org numbers are.
- **What they need** - just "is it real/active/bankrupt", or a full KYB pack (roller + sub-entities + status).

## API reference

Base URL: `https://data.brreg.no/enhetsregisteret/api` - responses are HAL+JSON.

| # | Purpose | Method + path | Example |
|---|---|---|---|
| 1 | Search companies by name | `GET /enheter?navn={name}&size=20` | `/enheter?navn=equinor` |
| 2 | Single entity by org number | `GET /enheter/{orgnr}` | `/enheter/923609016` |
| 3 | Roles / board / officers | `GET /enheter/{orgnr}/roller` | `/enheter/923609016/roller` |
| 4 | Sub-entities (branches) | `GET /underenheter?overordnetEnhet={orgnr}` | `/underenheter?overordnetEnhet=923609016` |
| 5 | Single sub-entity | `GET /underenheter/{orgnr}` | `/underenheter/{orgnr}` |
| 6 | Bulk download (all entities) | `GET /enheter/lastned` (also `/lastned/csv`, `/lastned/regneark`) | `/enheter/lastned` |

**curl pattern** (no auth header needed on any standard endpoint):

```bash
# name -> candidate entities
curl "https://data.brreg.no/enhetsregisteret/api/enheter?navn=equinor"

# org number -> full record  (Equinor ASA = 923609016)
curl "https://data.brreg.no/enhetsregisteret/api/enheter/923609016"

# org number -> board and officers
curl "https://data.brreg.no/enhetsregisteret/api/enheter/923609016/roller"
```

**Organisasjonsnummer is a 9-digit string** - use the canonical `organisasjonsnummer` from search (endpoint 1) verbatim in endpoints 2-5.

## Workflow: a Norwegian KYB check

```
1. Resolve identity
   GET /enheter?navn={name}   -> read _embedded.enheter[], pick the match, take organisasjonsnummer
   (skip if the user already gave an org number)

2. Confirm the entity is real and current
   GET /enheter/{orgnr}
   -> konkurs / underAvvikling / underTvangsavviklingEllerTvangsopplosning must all be false
   -> record organisasjonsform, næringskode1, registration date, forretningsadresse, antallAnsatte

3. Who runs it
   GET /enheter/{orgnr}/roller
   -> read the styre (board) group and daglig leder for the people in control

4. Its footprint
   GET /underenheter?overordnetEnhet={orgnr}
   -> list branches / establishments (a separate collection from enheter)

5. Distress signals
   -> any of the three status booleans true = flag; konkurs true means bankruptcy proceedings
```

## Output interpretation

**Status flags are booleans, not dates.** `konkurs: true` = bankruptcy proceedings are open. `underAvvikling: true` = voluntary dissolution. `underTvangsavviklingEllerTvangsopplosning: true` = compulsory liquidation. All three false is the pass condition; combine konkurs with underAvvikling for a full "distressed" read. For the *detail* of an insolvency proceeding (case dates, creditors) brreg gives you only the flag - route to the regdata credit-risk actors.

**Pagination is Spring HATEOAS.** A list response wraps results in `_embedded.enheter[]` (or `_embedded.underenheter[]`), with a `page` object (`size`, `totalElements`, `totalPages`, `number`) and a `_links.next` to walk. Default page size is 20; pass `size=` to widen. The **maximum reachable result set is 10,000 records per query** - narrow the filter rather than paging past it.

**underenheter are a SEPARATE collection from enheter.** Branches and establishments do not appear inside the main entity record - you must query the `/underenheter` endpoint. A main entity with no `/enheter` hit may still exist as an underenhet, and vice versa.

**roller is nested per org number.** There is no cheap bulk roles feed; each entity's board and officers come from its own `/roller` call. (A full `/roller/totalbestand` dump exists but is a very large file - do not pull it for a single check.)

**næringskode is NACE.** `næringskode1` is the primary activity code (with `næringskode2` / `næringskode3` as secondary). Use it to confirm the entity does the business the counterparty claims.

## Cross-sell - where the free front door leads

Norway (like the UK) is an outlier: a genuinely free, official, structured API with no anti-bot wall - so there is no scraping moat here. Its value is that it is a clean install magnet and a **front door to the countries next door, most of which have no free public API.** When the entity is not Norwegian, this skill hands off to the paid regdata actors, which do the anti-bot registry access the government portals do not hand you:

| Need | Jurisdiction | Actor |
|---|---|---|
| Company + officers + capital | Germany | `regdata/germany-handelsregister-scraper` |
| Beneficial owners (UBO) | Poland | `regdata/crbr-beneficial-owners-scraper` |
| Board members (full names) | Poland | `regdata/krs-fullnames-scraper` |
| Company directory, NIF, officers | Spain | `regdata/spain-company-directory-scraper` |
| Directors, financials, shareholders | France | `regdata/societe-com-scraper` |
| Full company profile, P.IVA, PEC | Italy | `regdata/italy-registro-imprese-scraper` |

Brreg's konkurs flag is a basic bankruptcy boolean; for detailed insolvency proceedings elsewhere use the **`regdata-credit-risk`** actors. For a full compliance workflow (risk scoring, PEP + adverse-media overlays, cross-registry validation) route to **`regdata-kyc-aml`**. Those actors need a free Apify token: https://apify.com?fpr=getregdata.

## Related skills

- **`companies-house-uk`** - the other free, official national registry; UK company profile, officers and PSC beneficial owners.
- **`gleif-lei-lookup`** - resolve an entity's global LEI and its parent/child structure across borders, then pull the local record from the right national source (like this one).
- **`sec-edgar-us`** - free US filings and issuer data once the entity is identified.
- **`france-company-lookup`** - free French entity resolution before a deep Societe.com pull.
- **`sanctions-pep-screening`** - screen the board members and officers you found here against sanctions and PEP lists.
- **`regdata-kyc-aml`** - the full KYC/AML/KYB framework: risk scoring, PEP and adverse-media overlays, and the paid registry actors for non-Norwegian jurisdictions.
- **`regdata-credit-risk`** - insolvency and financial-distress monitoring once the entity is identified.
