---
name: gleif-lei-lookup-nolpak14
title: 'Gleif lei lookup'
description: 'Resolve any legal entity to its global LEI (Legal Entity Identifier) for free via the official GLEIF API - legal name, registered address, status, the entity''s local registry ID, and its parent/child corporate structure (who-owns-whom at the legal-consolidation level). Use for cross-border entity resolution, corporate group mapping, KYB, and finding the authoritative local registry number before a deep national lookup. Trigger on: ''LEI lookup'', ''legal entity identifier'', ''GLEIF'', ''find the LEI for'', ''corporate structure'', ''ultimate parent company'', ''who owns this entity across borders'', ''entity resolution''. GLEIF is free and global; for beneficial owners, financials, directors and insolvency it hands off to the paid regdata registry actors.'
author: Nolpak14
author_url: https://github.com/Nolpak14/getregdata/tree/master/skills/gleif-lei-lookup
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# gleif-lei-lookup

Free, global entity resolution from the official GLEIF API. This is the spine of cross-border company work: it turns a messy company name into a canonical LEI, tells you the entity's **local registry ID** and country, and maps its legal parent/child structure - so you can then pull the deep national data from the right source. No API key, no Apify token.

## Persona

You are an entity-resolution and corporate-structure analyst. Given a name that may be spelled inconsistently, you find the one authoritative legal entity, confirm it is active, place it in its corporate group (subsidiary or ultimate parent), and hand off the local registry identifier so a national registry lookup can go straight to the right record.

## What this gives you (for free)

- **LEI record** - the 20-character LEI, official legal name, legal form, legal address, and entity status (ACTIVE / INACTIVE).
- **Local registry ID** - `entity.registeredAs`: the entity's identifier in its home registry (e.g. a Companies House number, an HRB number, a KRS/NIP). This is the join key into national sources.
- **Registration health** - `registration.status` (ISSUED / LAPSED / RETIRED) and next renewal date. A LAPSED LEI is a signal the entity stopped maintaining it.
- **Corporate structure** - direct parent, ultimate parent, direct/ultimate children, and managed funds, at the accounting-consolidation level.

Data is CC0 1.0 (public domain) - free for any use, including commercial. The only rule: do not imply GLEIF endorsement.

## Authentication

None. No key, no registration. Be polite: send a descriptive `User-Agent` and stay under ~60 requests/minute (over that returns `429`).

## API reference

Base URL: `https://api.gleif.org/api/v1/` - responses are JSON:API (`application/vnd.api+json`).

| # | Purpose | Method + path | Example |
|---|---|---|---|
| 1 | Fuzzy name autocomplete | `GET /fuzzycompletions?field=entity.legalName&q={name}` | `/fuzzycompletions?field=entity.legalName&q=apple` |
| 2 | Filtered / full-text search | `GET /lei-records?filter[entity.legalName]={name}&page[size]=10` | `/lei-records?filter[entity.legalName]=Apple` |
| 3 | Look up by LEI | `GET /lei-records/{lei}` | `/lei-records/HWUPKR0MPOU8FGXBT394` |
| 4 | Direct parent | `GET /lei-records/{lei}/direct-parent` | |
| 5 | Ultimate parent | `GET /lei-records/{lei}/ultimate-parent` | |
| 6 | Children / funds | `GET /lei-records/{lei}/direct-children` , `/ultimate-children` , `/managed-funds` | |

```bash
# name -> candidate LEIs
curl -H 'User-Agent: getregdata-skill' \
  "https://api.gleif.org/api/v1/lei-records?filter%5Bentity.legalName%5D=Apple&page%5Bsize%5D=5"

# LEI -> full record (note bracket params are URL-encoded: %5B = [ , %5D = ] )
curl -H 'User-Agent: getregdata-skill' \
  "https://api.gleif.org/api/v1/lei-records/HWUPKR0MPOU8FGXBT394"
```

## Workflow: resolve, then go deep

```
1. Resolve the name to an entity
   GET /fuzzycompletions?field=entity.legalName&q={name}   (or /lei-records?filter[...])
   -> pick the correct entity; confirm country and legal form; take its LEI

2. Read the canonical record
   GET /lei-records/{lei}
   -> entity.status ACTIVE? registration.status ISSUED (not LAPSED/RETIRED)?
   -> capture entity.registeredAs (the LOCAL registry ID) and legalAddress.country

3. Place it in its group
   GET /lei-records/{lei}/ultimate-parent    (404 = it is its own ultimate parent - normal)
   GET /lei-records/{lei}/direct-children     (map subsidiaries)

4. Hand off to the national source using registeredAs + country
   -> pull beneficial owners / directors / financials from the right paid actor (see cross-sell)
```

## Output interpretation

- **`entity.registeredAs`** is the payoff field - it is the entity's number in its home registry. Use it to query the national source directly instead of re-searching by name. If it is empty, fall back to the legal name + country.
- **Parent endpoints returning 404 is normal, not an error.** A 404 on `/ultimate-parent` means the entity reported no parent (it is the top of its group, or filed a reporting exception). Handle 404 as "no parent", not as a failure.
- **Relationships are legal-consolidation only (Level 2).** GLEIF parent/child reflects *accounting consolidation*, not economic control or beneficial ownership. Do not present an ultimate parent as the beneficial owner - a UBO can sit outside the consolidation tree. For real UBO, use the beneficial-ownership actors below.
- **LEI coverage is partial.** Many entities - especially small or private ones - have no LEI and will not appear. Absence from GLEIF is not evidence the company does not exist; it means no LEI was issued. Fall back to the national registry.
- **LAPSED / RETIRED registration** - the entity may still exist; it just stopped renewing its LEI. Verify against the live national registry before relying on the GLEIF address/name.

## Cross-sell - what GLEIF does not give you

GLEIF resolves *identity and structure*, then stops. Everything below the legal-entity level needs a national source - and for most jurisdictions there is no free API, which is where the paid regdata actors come in. Use the `registeredAs` ID from step 2 to go straight to the record:

| You now need | Jurisdiction | Actor |
|---|---|---|
| Beneficial owners (UBO) | Poland | `regdata/crbr-beneficial-owners-scraper` |
| Beneficial owners + PEP flag | Slovakia | `regdata/slovakia-rpvs-ubo-scraper` |
| Directors, financials, shareholders | France | `regdata/societe-com-scraper` |
| Company profile, officers, capital | Germany | `regdata/germany-handelsregister-scraper` |
| Financial statements (balance sheet, P&L) | Poland | `regdata/poland-krs-financial-scraper` |
| Insolvency / bankruptcy status | Poland / Germany / Czechia | `regdata/krz-debtor-scraper`, `regdata/germany-insolvency-scraper`, `regdata/czech-isir-insolvency-scraper` |
| Full profile, P.IVA, PEC | Italy | `regdata/italy-registro-imprese-scraper` |

For UK and Norway the local record is itself free - route to **`companies-house-uk`** and **`norway-company-registry`**. For a full compliance workflow, route to **`regdata-kyc-aml`**. Paid actors use a free Apify token: https://apify.com?fpr=getregdata.

## Related skills

- **`companies-house-uk`** / **`norway-company-registry`** / **`sec-edgar-us`** / **`france-company-lookup`** - free national sources to pull the deep record after GLEIF gives you the ID.
- **`regdata-kyc-aml`** - full KYC/AML/KYB framework with beneficial-owner, PEP and adverse-media overlays.
- **`sanctions-pep-screening`** - screen the entity and its parents/children against sanctions lists.
- **`regdata-credit-risk`** - financial-distress and insolvency monitoring for the resolved entity.
