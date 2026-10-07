---
name: eu-transparency-register-nolpak14
title: EU transparency register
description: 'Check whether a company or organisation lobbies the EU institutions - for free, keyless - using the official EU Transparency Register. Find registered interest representatives (lobbyists), which EU legislative files an organisation lobbies on, how much it declares spending on EU lobbying, how many lobbyists it fields, and whether it holds European Parliament access badges. This is an influence / reputational / ESG due-diligence lane, NOT a company registry. Trigger on: ''EU lobbying'', ''transparency register'', ''interest representatives'', ''EU lobby register'', ''influence due diligence'', ''does this company lobby the EU'', ''EU lobbying spend'', ''interest representative check'', ''European Parliament access badge'', ''who lobbies Brussels''. The register is a bulk daily XML dump - download once, then filter and match locally by name, country, and category.'
author: Nolpak14
author_url: https://github.com/Nolpak14/getregdata/tree/master/skills/eu-transparency-register
license: MIT
version: 0.1.2
execution_mode: open
jurisdiction: eu
practice: regulatory
language: en
---

# eu-transparency-register

Check whether a company, NGO, consultancy, or trade association lobbies the EU
institutions - free, keyless, no login. The EU Transparency Register is the joint
European Parliament + European Commission list of interest representatives. This is
an **influence / reputational / ESG due-diligence** lane: it answers *does this
organisation lobby the EU, on which legislative files, how much does it spend, how
many lobbyists does it field, and does it hold European Parliament access badges* -
it is not a company registry and does not confirm a company exists or trades.

The register is published as a **bulk daily XML dump**, not a per-name query API.
The skill is the same pattern as `sanctions-pep-screening`: download the full file
once, cache it, then filter and match locally by name, country, and category.

## Persona

You are an integrity / ESG / reputational due-diligence analyst. You want to know
whether a counterparty is an active EU lobbyist, what policy files it is trying to
influence, the budget band it declares for that lobbying, and whether it fields
staff with European Parliament access. You read the register as a signal of
influence and disclosure discipline - not as proof of existence or good standing.

## What this gives you (for free)

- **Every registered interest representative** - organisations that have declared
  they seek to influence EU policy: consultancies, in-house corporate lobbyists,
  NGOs, trade and business associations, think-tanks, law firms, and others.
- **Lobbying subject matter** - the organisation's stated goals and interests, the
  levels of interest (EU / national / regional), the EU legislative proposals it is
  engaged on, and its communication activities.
- **Lobbying footprint** - the number of persons involved in lobbying (headcount and
  FTE) and the number of European Parliament accreditation badges held.
- **Self-declared cost / financial data** - the annual lobbying budget bands and
  related financial blocks the organisation reported.
- **Identity and category** - identification code, name / original name / acronym,
  registration category, entity form, head-office country and address, website, and
  registration + last-update dates.

Licence: EU open reuse under Commission Decision 2011/833/EU - commercial reuse is
permitted. Read-only.

## Data source (no key)

One direct download - fetch, cache, and query locally. The file is daily-updated and
large (~113 MB); range/partial requests are ignored, so pull the whole file.

| Resource | Format | URL |
|---|---|---|
| Full register (daily) | XML | `https://ec.europa.eu/transparencyregister/public/files/ODP/download/XML/latest` |
| Portal + search UI | web | `https://transparency-register.europa.eu` |
| Open-data catalogue mirror | page | `https://data.europa.eu/data/datasets/transparency-register` |

```bash
# Download the full register once, then work against the local copy
curl -sL -o transparency-register.xml \
  "https://ec.europa.eu/transparencyregister/public/files/ODP/download/XML/latest"
```

There is **no public REST query API** - all filtering by name, country, or category
is client-side after ingesting the dump. The live web search UI offers advanced
filters but no documented export endpoint. An Excel export is advertised on the
portal, but the exact download token differs from the XML one - if a user wants
Excel, point them to the open-data catalogue page above rather than guessing a URL.

## Fields in the XML

Per registered organisation the dump carries: `identificationCode`, `name` /
`originalName` / `acronym`, `registrationCategory` (consultancy / company / NGO /
trade association / think-tank / other), `entityForm`, `headOffice` (country, city,
postCode, address, phone), `webSiteURL`, `registrationDate` / `lastUpdateDate`,
`goals`, `interests` / `levelsOfInterest`, `EULegislativeProposals`,
`communicationActivities`, `members` / `membersFTE` (persons involved in lobbying),
`EPAccreditedNumber` (European Parliament access badges), `isMemberOf`, plus the
self-declared financial / lobbying-cost blocks.

## Workflow: does this organisation lobby the EU

```
1. Download + cache the full XML dump (refresh when your copy is stale;
   the file updates daily and organisations join / drop off)

2. Match the target name against name / originalName / acronym
   -> normalise case and accents; try the local-language name and the acronym
   -> narrow with headOffice country when a name is ambiguous

3. Read the profile of each candidate
   -> registrationCategory + entityForm (what kind of lobbyist it is)
   -> goals / interests / EULegislativeProposals (what it lobbies on)
   -> members / membersFTE + EPAccreditedNumber (how big its footprint is)
   -> the self-declared lobbying-cost band (how much it spends)

4. Interpret absence correctly
   -> no match = "does not lobby the EU institutions" (or lobbies unregistered),
      NOT "this organisation does not exist"

5. Record the finding: register date/version, the matched code, the category,
   the declared spend band, and the EP badge count
```

## Output interpretation

- **A name match is a candidate, not a verdict.** The same group can appear under a
  local-language name, an acronym, or a subsidiary. Confirm with head-office country
  and the identification code before asserting "this is them".
- **Absence means "does not lobby the EU", not "does not exist".** Only organisations
  that seek to influence EU institutions register here. A company entirely missing
  from the register may simply not lobby Brussels - resolve existence and standing
  through a company registry, not this list.
- **Lobbying-cost figures are self-declared budget bands.** The financial data is the
  organisation's own reported estimate, often as a range, not an audited figure. Read
  it as a disclosed order of magnitude, not a precise spend.
- **EU-institution scope only.** The register covers lobbying of the EU institutions.
  National and regional lobbying (member-state parliaments, agencies) is out of scope
  and lives in separate national transparency registers where they exist.
- **Meetings data is a separate dataset.** The Commission's "meetings with
  Commissioners / senior officials" records are published separately and join to the
  register on organisation name (fuzzy), not on a shared key - do not assume the dump
  contains meeting logs.

## Cross-sell - from a lobbying signal to the full record

The register tells you an organisation lobbies the EU and on what - it does **not**
give you owners, directors, financials, or legal status. Take the matched name +
head-office country to the entity record - free where a national skill exists, paid
actor otherwise:

| Need | Jurisdiction | Resolve via |
|---|---|---|
| Beneficial owners (UBO) | Poland | `regdata/crbr-beneficial-owners-scraper` |
| Company + officers + capital | Germany | `regdata/germany-handelsregister-scraper` |
| Directors, financials, shareholders | France | `regdata/societe-com-scraper` |
| Global LEI + corporate structure | cross-border | free `gleif-lei-lookup` |

For the full compliance workflow - risk scoring, sanctions + PEP overlays,
cross-registry validation - route to **`regdata-kyc-aml`**. To pair the lobbying
signal with public-money exposure (does this organisation also win EU public
contracts) route to **`eu-ted-procurement`**. Paid actors need a free Apify token:
https://apify.com?fpr=getregdata.

## Related skills

- **`eu-ted-procurement`** - does this organisation also win above-threshold EU
  public contracts; pair lobbying influence with public-money exposure.
- **`us-federal-awards`** - the US equivalent public-money lane for organisations
  active on both sides of the Atlantic.
- **`gleif-lei-lookup`** - resolve a matched lobbyist to its global LEI and
  parent/child structure across borders.
- **`regdata-kyc-aml`** - the full KYC/AML/KYB framework; lobbying influence is one
  reputational dimension alongside sanctions, PEP, and adverse media.
- **`sanctions-pep-screening`** - screen the organisation and its owners/officers
  against the official sanctions lists, using the same download-and-match pattern.

## More on getregdata.com

- All skills and paid registry coverage: https://getregdata.com/skills/ and https://getregdata.com/registries/
