---
name: companies-office-nz-thecolab-ai
title: Companies Office NZ
description: Search and inspect New Zealand Companies Register records through read-only public website endpoints. Use when the task involves NZ company lookup by name, company number, or NZBN; company status, incorporation date, entity type; director names and appointment dates; shareholder allocations and percentages; registered addresses; filing history and public documents; or any company governance data not covered by the NZBN Register skill. No login, API key, or account required. Read-only.
author: thecolab-ai
author_url: https://github.com/thecolab-ai/.skills/tree/main/skills/companies-office-nz
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: nz
practice: corporate
language: en
sources:
- title: Api Notes
  path: references/api-notes.md
- title: Source Notes
  path: references/source-notes.md
---

# Companies Office NZ

## Goal

Query rich public Companies Register data through a deterministic no-login Python CLI. Covers company identity, registered addresses, current and historical directors, shareholder allocations, and the complete filing/document history.

## Use this when

- A user asks to find an NZ company by name, number, or NZBN
- A workflow needs director names, appointment dates, or residential cities
- A user wants shareholder allocations and ownership percentages
- A workflow needs the full filing history or document list for a company
- A user asks about a company's registered office, address for service, or contact details from the register
- A task requires company number, incorporation date, status, or entity type

## Do not use this for

- Private or suppressed register data
- Authenticated actions: director appointments, shareholder updates, annual return filing
- Paid company extract purchase (CompanyExtract fee document)
- PPSR / Personal Property Securities Register — this is a separate register at ppsr.companiesoffice.govt.nz
- GST numbers, industry classifications, trading names, or Australian Business Numbers — use `nzbn-register` for these
- Non-company entities (trusts, partnerships, incorporated societies) — limited support
- Bulk scraping or full-register replication

## Preferred workflow

1. `search <name>` to find the company number
2. `entity <number>` for summary + addresses
3. `directors <number>` and `shareholders <number>` for governance data
4. `documents <number>` for filing history
5. Or use `full <number>` to get everything in one call
6. Use `--json` for agent chaining; `--output md` for reports

## CLI

Run with:

```bash
python3 skills/companies-office-nz/scripts/cli.py <command> [flags]
```

### Commands

**`search <query> [--limit N] [--start N] [--json] [--output md]`**

Search by company name, company number, or NZBN text.

```bash
python3 skills/companies-office-nz/scripts/cli.py search "Holt Group"
python3 skills/companies-office-nz/scripts/cli.py search "xero" --limit 5 --json
python3 skills/companies-office-nz/scripts/cli.py search 1830488 --json
```

**`entity <company_number> [--nzbn <nzbn>] [--json] [--output md]`**

Company summary and addresses. Pass `--nzbn` to look up by NZBN.

```bash
python3 skills/companies-office-nz/scripts/cli.py entity 1830488
python3 skills/companies-office-nz/scripts/cli.py entity --nzbn 9429034042984 --json
```

**`directors <company_number> [--json] [--output md]`**

Current and historical directors, appointment dates, residential addresses (public).

```bash
python3 skills/companies-office-nz/scripts/cli.py directors 1830488
python3 skills/companies-office-nz/scripts/cli.py directors 973228 --json
```

**`shareholders <company_number> [--json] [--output md]`**

Shareholder allocations, percentages, holder names and addresses.

```bash
python3 skills/companies-office-nz/scripts/cli.py shareholders 1830488
python3 skills/companies-office-nz/scripts/cli.py shareholders 9400535 --json
```

**`documents <company_number> [--limit N] [--start N] [--json] [--output md]`**

Filing history and document list. Includes document URLs for public attachments.

```bash
python3 skills/companies-office-nz/scripts/cli.py documents 1830488 --limit 20
python3 skills/companies-office-nz/scripts/cli.py documents 973228 --json
```

**`full <company_number> [--doc-limit N] [--json] [--output md]`**

All of the above in one call: entity summary + directors + shareholders + recent documents.

```bash
python3 skills/companies-office-nz/scripts/cli.py full 973228
python3 skills/companies-office-nz/scripts/cli.py full 1830488 --doc-limit 20 --json
python3 skills/companies-office-nz/scripts/cli.py full 1830488 --output md
```

## Resources

- CLI entrypoint: `scripts/cli.py`
- Live smoke test: `scripts/smoke_test.py`
- API and stability notes: `references/api-notes.md`

## Related skills

- `nzbn-register` — NZBN Register: trading names, GST numbers, industry classifications, ABN, and broader entity identity for all NZ entity types. Complement this skill when you need GST or trading name data.
- `nz-pricewatch` — not related, different domain

## Notes

- No API key, OAuth token, username, password, or browser session required
- Director and shareholder data is HTML-parsed from the public register pages (the equivalent JSON service endpoints require an authenticated session)
- Director residential addresses are shown as registered on the public register — some may be suppressed by the company
- Listed companies (extensive shareholding flag) show only the top shareholder parcels; contact the company for a full register
- Charges and security interests (PPSR) are on a separate register; this skill does not cover them
- NZBN field is not returned by the entity detail endpoint — it is available in search results; use `search <nzbn>` to resolve
- Documents with a `drmKey` have a public download URL included in output; others are listed without a URL
- Keep queries small and respectful; this is an unofficial use of the website's own proxy
