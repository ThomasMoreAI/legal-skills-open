---
name: eu-financial-transparency
title: eu-financial-transparency
description: 'Find out which EU grants and directly-managed EU funding an organisation has received - for free, keyless - using the official EU Financial Transparency System (FTS). See EU funding recipients: who received EU money, how much (committed amount / EU contribution), under which programme and budget line, in which year, and for what action. This is an EU-funding-recipient due-diligence + grant-recipient lead-gen lane, NOT a company registry. Trigger on: ''EU funding recipients'', ''EU grants'', ''FTS'', ''Financial Transparency System'', ''who received EU money'', ''did this org get an EU grant'', ''EU grant recipient check'', ''EU direct funding'', ''beneficiaries of EU funds'', ''EU budget beneficiaries'', ''which EU programmes funded this organisation''. FTS is a bulk annual download (one .xlsx per year) plus a live search export - download the year file(s), then filter and match locally by name, country, and programme.'
author: Nolpak14
author_url: https://github.com/Nolpak14/getregdata/tree/master/skills/eu-financial-transparency
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: white-collar
language: en
---

# eu-financial-transparency

Find out which EU grants and directly-managed EU funding an organisation has
received - free, keyless, no login. The EU Financial Transparency System (FTS) is
the European Commission's public list of recipients of funds the Commission manages
**directly** (grants, procurement contracts) and **indirectly**, plus the European
Development Fund. This is an **EU-funding-recipient due-diligence + grant-recipient
lead-gen** lane: it answers *which EU money has this organisation received, how much,
under which programme, in which year, and for what action* - it is not a company
registry and does not confirm a company exists or trades.

FTS is published as **bulk annual datasets**, not a per-name query API. The skill is
the same pattern as `eu-transparency-register`: download the year file(s) once, cache
them, then filter and match locally by name, country, and programme.

## Persona

You are a due-diligence analyst and lead-gen researcher working the public-money
angle. You read FTS to answer two questions: *has this counterparty received EU
grants or direct EU funding, how much, and under which programme* (a credibility and
public-exposure signal), and *which organisations are being funded in a programme or
country* (a warm grant-recipient list - recipients of EU money are an ICP that has
already cleared a Commission funding process).

## What this gives you (for free)

- **Every recipient of directly / indirectly managed EU funds** - beneficiaries of
  Commission-managed grants and procurement, plus the European Development Fund:
  companies, NGOs, universities, research bodies, public authorities, and consortia.
- **The amounts** - the committed amount and the EU contribution for each recipient,
  per action / year.
- **The funding context** - the programme name, the budget line, the subject / action
  or project, the funding type and contract type, and the responsible Commission
  department.
- **Recipient identity** - beneficiary name, VAT number, beneficiary type,
  country and city, and the coordinator / consortium role where the action is a
  multi-partner project.
- **Project metadata** - the reporting year and the project status.

Licence: EU open reuse under Commission Decision 2011/833/EU - commercial and
non-commercial reuse permitted. Read-only.

## Data source (no key)

There is **no public REST / JSON API**. Two tracks, both free and keyless:

| Track | What | Where |
|---|---|---|
| Live search + export | HTML search on the FTS Analysis portal with an **Export -> Excel** button | `https://ec.europa.eu/budget/financial-transparency-system/analysis.html` |
| Annual bulk datasets | One `.xlsx` per year (2007-2025), mirrored on the open-data portal | `https://data.europa.eu/data/datasets/fts` |

FTS portal base: `https://ec.europa.eu/budget/financial-transparency-system/`

The skill shape is: download the year file(s) you need from the open-data portal, then
filter locally by beneficiary name, country, and programme - exactly the
download-and-match pattern of `eu-transparency-register`. Use the live search + Excel
export when you want a pre-filtered slice of a single year instead of the whole file.

```bash
# Grab a year's bulk dataset from the open-data catalogue page, then query locally.
# (The catalogue page lists one .xlsx download per year, 2007-2025.)
#   https://data.europa.eu/data/datasets/fts
```

## Fields in the dataset

Per recipient / action the FTS data carries: beneficiary **name**, **VAT number**,
**beneficiary type**, **country** / **city**, the **committed amount** and the **EU
contribution** (amount), the **budget line**, the **programme name**, the **year**,
the **subject / action**, the **funding type**, the **contract type**, the
**responsible department**, the **project status**, and the **coordinator /
consortium role**. Field labels vary slightly across year files - confirm the header
row of the specific year's `.xlsx` rather than assuming a fixed schema.

## Workflow: which EU funding has this organisation received

```
1. Pick the years
   -> FTS is one .xlsx per year (2007-2025); download the years in scope
   -> data for year N is published end-June of N+1 (~12-month lag - the latest
      full year may not be available yet)

2. Download + cache the year file(s) from the open-data portal
   -> or run the live search on the Analysis portal and use Export -> Excel
      when you only need a filtered slice of one year

3. Match the target against the beneficiary name
   -> normalise case and accents; try the local-language name and any acronym
   -> narrow with country when a name is ambiguous
   -> where present, confirm with the VAT number (a stronger key than name)

4. Read each matching row
   -> programme name + budget line (which pot funded it)
   -> committed amount + EU contribution (how much)
   -> subject / action + year (what and when)
   -> coordinator / consortium role (lead vs partner in a multi-partner action)

5. Interpret absence correctly
   -> no match = "no directly / indirectly managed EU funding on record",
      NOT "received no EU money" (shared-management funds are not in FTS - see below)
```

## Output interpretation

- **A name match is a candidate, not a verdict.** The same organisation can appear
  under a local-language name, an acronym, or a subsidiary, and beneficiary names are
  free text. Confirm with country and - where present - the VAT number before
  asserting "this is them".
- **FTS covers only ~25% of the EU budget.** It reports funds the Commission manages
  **directly** and **indirectly**, plus the EDF. The rest of the budget is spent under
  **shared management** with member states.
- **Absence is not "received no EU money".** Structural and cohesion funds and other
  shared-management programmes are managed **nationally** and are **not** in FTS - a
  recipient of those funds will be missing here. Read a blank as "no *directly-managed*
  EU funding on record", and resolve national-programme money through member-state
  transparency portals, not this list.
- **Annual snapshots with a ~12-month lag.** Each year is a separate `.xlsx` and year
  N loads at the end of June of N+1. The most recent calendar year is often not yet
  published - do not read its absence as "stopped receiving funding".
- **Amounts are committed / contribution figures, not audited spend.** The committed
  amount and EU contribution are the funding decision's figures for that action, not a
  reconciled final payment.
- **Mind the export cell cap.** The live search Excel export is capped at **1,000,000
  cells per export** - refine the query (year, country, programme) so a large slice is
  not silently truncated. For anything bigger, use the bulk year file instead.

## Cross-sell - from an EU-funding signal to the full record

FTS tells you an organisation received EU money and under which programme - it does
**not** give you owners, directors, financials, or legal status. Take the matched name
+ country (and VAT, where present) to the entity record - free where a national skill
exists, paid actor otherwise:

| Need | Jurisdiction | Resolve via |
|---|---|---|
| Beneficial owners (UBO) | Poland | `regdata/crbr-beneficial-owners-scraper` |
| Company + officers + capital | Germany | `regdata/germany-handelsregister-scraper` |
| Directors, financials, shareholders | France | `regdata/societe-com-scraper` |
| Global LEI + corporate structure | cross-border | free `gleif-lei-lookup` |

For the full compliance workflow - risk scoring, sanctions + PEP overlays,
cross-registry validation - route to **`regdata-kyc-aml`**. To turn the
grant-recipient lane into a qualified outreach list, route to **`regdata-lead-gen`**.
Paid actors need a free Apify token: https://apify.com?fpr=getregdata.

## Related skills

- **`eu-ted-procurement`** - which above-threshold EU public contracts an
  organisation has won; pair grant funding with procurement track record for the full
  public-money picture.
- **`eu-transparency-register`** - whether the same organisation lobbies the EU
  institutions; complete the EU funding-flows quartet (grants + tenders + lobbying).
- **`us-federal-awards`** - the US equivalent public-money lane for organisations
  active on both sides of the Atlantic.
- **`regdata-kyc-aml`** - the full KYC/AML/KYB framework; EU-funding exposure is one
  due-diligence dimension alongside sanctions, PEP, and adverse media.
- **`regdata-lead-gen`** - turn the grant-recipient lane into a qualified outreach
  list of organisations that have already cleared an EU funding process.
