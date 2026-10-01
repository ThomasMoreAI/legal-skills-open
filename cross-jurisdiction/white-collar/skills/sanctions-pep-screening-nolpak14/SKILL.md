---
name: sanctions-pep-screening-nolpak14
title: sanctions-pep-screening
description: 'Screen a person or company against the official government sanctions lists for free - US OFAC (SDN + Consolidated), the EU Consolidated Financial Sanctions List, the UK Sanctions List, and the UN Security Council Consolidated List. Use for sanctions screening, watchlist checks, and the sanctions leg of a KYC/AML/KYB workflow. Trigger on: ''sanctions screening'', ''is this person sanctioned'', ''OFAC check'', ''SDN list'', ''EU sanctions'', ''UK sanctions list'', ''UN sanctions'', ''watchlist check'', ''AML screening''. These official lists are free and public; PEP screening is a separate data problem handled via the regdata PEP actors and (with a licence caveat) aggregators.'
author: Nolpak14
author_url: https://github.com/Nolpak14/getregdata/tree/master/skills/sanctions-pep-screening
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: white-collar
language: en
---

# sanctions-pep-screening

Screen a name against the four primary official sanctions lists, all free and
public. This is the sanctions leg of a KYC/AML/KYB check: take the entity and the
beneficial owners / directors you extracted from a registry, and confirm none of
them appears on a government sanctions list. No API key, no paid service required.

## Persona

You are an AML sanctions analyst. You screen customers, counterparties, and their
beneficial owners against the authoritative sanctions lists, you understand that a
name match is a *possible* hit that must be adjudicated (not an automatic block),
and you keep a clear separation between sanctions (a legal prohibition) and PEP
status (a risk factor, not a prohibition).

## What this gives you (for free)

- **US OFAC** - the SDN (Specially Designated Nationals) list plus the Consolidated
  (non-SDN) list. US Government work, **public domain** - free for any use.
- **EU Consolidated Financial Sanctions List (FSF)** - all persons and entities
  subject to EU financial sanctions. Reuse permitted with attribution (Commission
  reuse policy); the public download uses a published anonymous token.
- **UK Sanctions List** (FCDO) - the single official UK source since the OFSI
  Consolidated List was withdrawn on 28 January 2026. Open Government Licence v3.0.
- **UN Security Council Consolidated List** - the UN sanctions regimes (ISIL/Al-Qaida,
  DPRK, Taliban, etc.). Free, open for reference use.

Each list gives, per entry: primary name and aliases (a.k.a. / f.k.a.), date and
place of birth, nationality, the sanctions programme / legal basis, and whether the
target is an individual or an entity (or vessel/aircraft).

## Data sources (no key)

All four are direct downloads - fetch, cache, and match locally. Refresh regularly
(designations change several times a week).

| List | Format | URL |
|---|---|---|
| OFAC SDN | XML | `https://sanctionslistservice.ofac.treas.gov/api/PublicationPreview/exports/SDN.XML` |
| OFAC SDN | CSV | `https://sanctionslistservice.ofac.treas.gov/api/PublicationPreview/exports/SDN.CSV` |
| OFAC SDN (enhanced) | XML | `https://sanctionslistservice.ofac.treas.gov/api/PublicationPreview/exports/SDN_ENHANCED.XML` |
| OFAC Consolidated (non-SDN) | XML | `https://sanctionslistservice.ofac.treas.gov/api/PublicationPreview/exports/CONSOLIDATED.XML` |
| EU FSF | XML | `https://webgate.ec.europa.eu/fsd/fsf/public/files/xmlFullSanctionsList_1_1/content?token=dG9rZW4tMjAxNw` |
| EU FSF | CSV | `https://webgate.ec.europa.eu/fsd/fsf/public/files/csvFullSanctionsList_1_1/content?token=dG9rZW4tMjAxNw` |
| UK Sanctions List | CSV / XML | `https://sanctionslist.fcdo.gov.uk/docs/UK-Sanctions-List.csv` (also `.xml`) |
| UN SC Consolidated | XML | `https://scsanctions.un.org/resources/xml/en/consolidated.xml` |

```bash
# Fetch OFAC SDN (public domain) and the UN list
curl -sL -o sdn.xml "https://sanctionslistservice.ofac.treas.gov/api/PublicationPreview/exports/SDN.XML"
curl -sL -o un.xml  "https://scsanctions.un.org/resources/xml/en/consolidated.xml"
```

The EU token `dG9rZW4tMjAxNw` is base64 for "token-2017" - the EU's published public
token for the anonymous download. No login is required for the public file.

## Workflow: screen an entity and its owners

```
1. Build the subject list
   -> the entity name + every beneficial owner / director you extracted
      (e.g. from CRBR, KRS, Handelsregister, Companies House PSC)

2. Fetch / refresh the four lists (cache them; do not re-download per name)

3. Match each subject name against every list
   -> normalise case and accents; compare against primary name AND all aliases
   -> for individuals, use DOB and nationality to confirm or rule out a match

4. Adjudicate each candidate hit
   -> exact strong match on name + DOB      -> TRUE HIT: escalate, do not proceed
   -> name-only match, DOB/nationality differ -> likely false positive: document why
   -> no match on any list                    -> clear on sanctions (this run)

5. Record the screen: which lists, list versions/date, and the outcome per subject
```

## Output interpretation

- **A name match is a candidate, not a verdict.** Sanctions lists are full of common
  names and transliterations. Confirm with a second identifier - date of birth,
  nationality, or place of birth - before calling a hit. Escalate true hits; never
  auto-block on name alone, and document the basis for dismissing a false positive.
- **Screen the aliases, not just the primary name.** Every list carries a.k.a. /
  f.k.a. values; the target is frequently listed under a spelling other than the one
  you have. Transliteration variants (Arabic, Cyrillic) are the classic miss.
- **"No hit" is only as good as the screen.** Record which lists you checked and the
  date/version. A clear result against a list you downloaded weeks ago is stale -
  refresh before signing off. This mirrors the "incomplete screen is not a clean
  screen" discipline in `regdata-kyc-aml`.
- **These are sanctions lists, not PEP lists.** None of the four flags politically
  exposed persons. A subject can be entirely clear on sanctions and still be a PEP -
  that is a separate check (see below). Do not read "not sanctioned" as "not a PEP".
- **Entity vs individual.** Match a company against the entity entries and each human
  owner/officer against the individual entries; do not screen a company name against
  the individuals list and call it done.

## PEP screening - a separate problem

There is **no free official consolidated government PEP list**. Handle PEP exposure
separately:

- **Poland** - `regdata/poland-parliamentary-pep-scraper` returns Sejm members across
  terms for PEP screening.
- **Slovakia** - `regdata/slovakia-rpvs-ubo-scraper` already flags PEP status alongside
  the beneficial owner.
- **Broader coverage** - aggregators such as OpenSanctions carry a PEP dataset, **but
  mind the licence**: OpenSanctions' hosted API is paid for commercial use, and its
  bulk data is CC-BY-NC, so commercial PEP screening on OpenSanctions data needs a
  paid licence regardless of self-hosting. Do not treat it as free for business use.

## Debarment - a related but separate lane

Debarment (exclusion from public contracts) is distinct from sanctions. Two useful sources:

- **US federal** - use the `sam-gov-exclusions` skill (free SAM.gov API) for the US
  System for Award Management exclusions list.
- **World Bank / MDB debarment** - the World Bank publishes its "Listing of Ineligible
  Firms and Individuals" as a free, searchable public page
  (`worldbank.org/en/projects-operations/procurement/debarred-firms`, refreshed ~every
  3 hours). Under the 2010 Mutual Enforcement Agreement, cross-debarment also covers the
  ADB, AfDB, EBRD and IDB (each runs its own list). Note: the old keyless Socrata API is
  retired, and the OpenSanctions `worldbank_debarred` mirror is CC-BY-NC (non-commercial)
  - so for commercial use read the official public page, not the NC feed. Fields: name,
  country, ineligibility from/to dates, grounds (fraud/corruption/collusion/coercion),
  and sanction type (debarment / cross-debarment / conditional non-debarment).

Screen procurement-exposed counterparties against both alongside the sanctions lists above.

## Cross-sell - turn ownership data into a compliance check

This skill is most valuable wired onto the registry actors: extract the beneficial
owners and directors, then screen every one of them here.

| Step | Source |
|---|---|
| Extract beneficial owners (PL) | `regdata/crbr-beneficial-owners-scraper` |
| Extract beneficial owners + PEP flag (SK) | `regdata/slovakia-rpvs-ubo-scraper` |
| Extract board members (PL) | `regdata/krs-fullnames-scraper` |
| Extract officers (DE) | `regdata/germany-handelsregister-scraper` |
| Extract PSC / officers (UK, free) | `companies-house-uk` |
| PEP screening (PL Sejm) | `regdata/poland-parliamentary-pep-scraper` |
| One-call composite KYB (PL) | `regdata/poland-kyb-check` |

For the full workflow - risk scoring, adverse-media overlay, cross-registry
validation - route to **`regdata-kyc-aml`**. The registry actors use a free Apify
token: https://apify.com?fpr=getregdata.

## Related skills

- **`regdata-kyc-aml`** - the full KYC/AML/KYB framework; sanctions and PEP are two of
  its risk dimensions.
- **`companies-house-uk`** / **`gleif-lei-lookup`** / **`norway-company-registry`** /
  **`france-company-lookup`** / **`sec-edgar-us`** - free sources for the entity and
  the people to screen.
- **`regdata-credit-risk`** - insolvency and financial-distress checks on the same entity.
