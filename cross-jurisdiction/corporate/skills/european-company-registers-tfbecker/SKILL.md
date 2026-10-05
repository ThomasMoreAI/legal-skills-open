---
name: european-company-registers-tfbecker
title: European Company Registers
description: 'Search public company registers across Europe for financial data (revenue, assets, earnings) AND structured register data (managing directors, share capital, purpose, legal form). Use when researching company financials, verifying leads, or enriching B2B data. Germany combines the Unternehmensregister (unternehmensregister.de) AND the Bundesanzeiger in parallel for Jahresabschlüsse (GJ 2022+ post-DiRUG lives only in the Unternehmensregister), PLUS a Handelsregister (handelsregister.de) path for the structured register content, Geschäftsführer/Vorstand, Stammkapital, Sitz, Gegenstand, Prokura, Rechtsform, former names. France (free revenue + officers), Poland (KRS by name/number/NIP + filing history), UK. Trigger on: Unternehmensregister, Handelsregister, Bundesanzeiger, HRB, Geschäftsführer, Stammkapital, Gesellschafter, Jahresabschluss, Bilanz, Umsatz, KRS, SIREN, company financials.'
author: tfbecker
author_url: https://github.com/tfbecker/european-company-registers
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: corporate
language: en
---

# European Company Registers

Find financial data (revenue, assets, earnings) and register metadata for European companies.

## Running the scripts

Pure Node.js + Python, no build step. Point `REG` at this repo's `scripts/` directory (works
from any working directory):

```bash
REG="/path/to/european-company-registers/scripts"   # or ./scripts from the repo root
```

## Germany, the main path (Unternehmensregister + Bundesanzeiger)

Both sources are queried **in parallel**; listing is **CAPTCHA-free**. Commands:

```bash
node "$REG/de-combined.js" search  "Pergolux"                 # newest report only  (~0.4 s, default)
node "$REG/de-combined.js" search  "Pergolux" --all-ur        # all UR reports      (~0.5 s)
node "$REG/de-combined.js" search  "Pergolux" --all           # + Bundesanzeiger    (~1 s)
node "$REG/de-combined.js" report  "Pergolux"                 # ONE search + extract every free year's figures
node "$REG/de-combined.js" analyze "Pergolux" --year 2021     # one year's figures
```

**Pick the command by intent:**
- **"which years / how much revenue / analyse over all years"** → `report`. It searches once, then
  extracts the figures for the newest N years (default 5) in one process, routing each year to its
  source automatically. This is the efficient path, **don't loop `analyze` per year**.
- **just the listing** → `search` (add `--all-ur` for all years, `--all` to also confirm via Bundesanzeiger).
- **one specific year's figures** → `analyze --year YYYY`.

Flags: `--max-extract N` (report: how many newest years to extract, default 5) · `--years 2024,2023`
(only these) · `--no-ur` (skip the slow browser step; GJ 2022+ then listed only) · `--deep` (paginate
the UR, only for a fuzzy/surname search spanning many companies; a precise name is complete on 1 page) ·
`--index N` (pick the Nth company) · `-v` (keep raw payloads) · `--text-dir <dir>` / `--inline-text` /
`--no-save-text` (full report text is saved to `./register-texts/` by default, see *Full report text* below).

### Why two sources (DiRUG)

Publication of Jahresabschlüsse for fiscal years **beginning after 31.12.2021** moved from the
Bundesanzeiger to the Unternehmensregister. So **GJ 2022+ lives only in the Unternehmensregister**;
a Bundesanzeiger-only scrape is ~3 years stale. The UR listing is a superset (both sources, tagged
`sources`), so it drives the listing; the Bundesanzeiger adds the report URLs whose figures the
CAPTCHA+LLM extractor reads **for free**.

### Figure extraction, both sources, all years (no paywall)

- **Listing** (`search`) never touches a CAPTCHA.
- **GJ ≤2021 (Bundesanzeiger)**, HTTP path; the report's image CAPTCHA is read by **Claude Haiku**
  (vision), the text extracted by **Claude Sonnet**. Fast-ish (~20 s/year).
- **GJ 2022+ (Unternehmensregister)**, the published Jahresabschluss is **free** but behind a
  "Ich bin ein Mensch" checkbox (Friendly-Captcha, no payment/login). `ur_fetch_document.py` drives
  a **stealth browser** to solve the checkbox and read the text, then the LLM extracts the figures.
  Slower (~15-20 s/year + one browser launch); `report` does all UR years in **one** browser session
  and extracts them **concurrently**. Use `--no-ur` to skip it.
- Only *deposited* (`hinterlegte`) statements of tiny companies are fee-based, those stay listed-only.

Needs a logged-in `claude` CLI (auto-detected, or set `CLAUDE_BIN`) and, for GJ 2022+, a stealth
browser (see *Requirements* in the README; override its location with `COMPANY_REGISTERS_BROWSER`
and its Python with `UR_PYTHON`). Never exports `ANTHROPIC_API_KEY` / `ANTHROPIC_BASE_URL`. Model
overrides: `BA_CAPTCHA_MODEL`, `BA_EXTRACT_MODEL`.

Per-year `status` in `report`: `extracted` · `listed_only` (beyond `--max-extract`) ·
`gated_skipped` (`--no-ur`) · `extraction_failed`.

### Full report text, scraped AND saved by default

`report`/`analyze` don't just distill figures, they **keep the full document text** (the whole
Jahresabschluss / Lagebericht / Anhang scraped from either source, the same text the extractor reads)
so nothing has to be re-scraped later. By **default** each extracted year is written to one UTF-8
`.txt` file (with a short provenance header) under **`./register-texts/`**:

```
register-texts/<Court>_<Register>_GJ<Year>_<source>.txt
# e.g. Bad-Oeynhausen_HRB-7371_GJ2024_unternehmensregister.txt
```

Each extracted year in the JSON then carries `report_chars` and `report_text_file`; the top level of
a `report` result adds `text_dir` and `saved_text_count`.

- `--text-dir <dir>`, where to write (default `./register-texts`; env `REGISTER_TEXT_DIR`).
- `--inline-text`, also embed the full text in the JSON as `report_text` (heavy; off by default).
- `--no-save-text`, figures only, don't write files.

The saved text carries the qualitative content the figures can't: **Lagebericht** (strategy, outlook,
risks, only larger companies file one), **Anhang** (Beteiligungen/ownership, related parties, a
Gewinnabführungsvertrag, contingent liabilities). For Kleinstkapitalgesellschaften it's essentially
just the bare balance sheet. `search` never fetches documents, so it writes nothing.

### Output

`search` → companies with `euid`, `register`/`register_number` (HRB), `court`, `state`, and `reports[]`
of `{fiscal_year, report_name, date, sources, free_extract}` (encrypted payloads stripped unless `-v`).
`report`/`analyze` → per year `financial_data`: `revenue, total_assets, earnings, equity, liabilities,
inventory, receivables, cash, fixed_assets, gross_profit, material_expenses, personnel_expenses,
operating_result, employees, fiscal_year, is_group_report, currency`. Plus, per extracted year,
`report_chars` + `report_text_file` (and `report_text` with `--inline-text`); see *Full report text* above.

## Germany, Handelsregister (structured register content)

Separate from the Jahresabschluss path above. Gives the **register content**, not financials:
Rechtsform, Sitz + Geschäftsanschrift, Gegenstand, Stamm-/Grundkapital, Vertretungsregelung,
**Geschäftsführer / Vorstand**, Prokura, and former names. Free since the DiRUG reform (AD).

```bash
node "$REG/de-handelsregister.js" search  "Holz-Richter"                       # register entries: name, HRB, court, seat, status, former names
node "$REG/de-handelsregister.js" details "Holz-Richter GmbH" --hrb 37497 --court Köln   # AD → structured JSON
```

- `search` drives handelsregister.de (stealth browser; the site is a stateful JSF app, no
  bot-protection) and returns the matching register rows, **always match a company by its HRB**,
  never a fixed position (the result order isn't stable).
- `details` downloads the AD ("Aktueller Abdruck"), runs `pdftotext`, and parses the standard
  numbered sections into JSON (`share_capital`, `managing_directors[]` with birth dates, `prokura[]`,
  `legal_form`, `purpose`, `seat`, …).
- **Rate limit:** handelsregister.de throttles *document* retrieval, after a few AD downloads in a
  short window it routes to an error page (the helper retries, then returns `reason:"throttled"`).
  `search` is not throttled. Retry `details` after a short cooldown.
- Needs the stealth browser (override its Python with `CLOAK_PYTHON`) and `pdftotext` (poppler).

## Other countries

```bash
node "$REG/gb-companies-house.js" search "Tesco"        # UK , company / filings <number> also (needs key)
node "$REG/fr-inpi.js"            analyze "Carrefour"   # FR , analyze accepts a name OR a <siren>
node "$REG/pl-krs.js"             search  "CD PROJEKT"  # PL , company <krs> · nip <nip> · analyze <krs|nip>
# Or the unified dispatcher (de routes to de-combined.js):
node "$REG/search.js" --country fr --name "Carrefour"
```

- **France (INPI/RNE)**, `recherche-entreprises.api.gouv.fr`, **free, no key**. Returns real
  **revenue** (`ca`) + **earnings** (`resultat_net`) per year and the **officers** (`dirigeants`)
  for the many companies in the open financial-ratios dataset, plus full metadata. `analyze` takes a
  name (picks the best-matching real entity) or a SIREN. An optional free `INPI_API_TOKEN` adds
  balance-sheet depth (total assets/equity); revenue works without it.
- **Poland (KRS)**, the official Ministry-of-Justice API by **KRS number** is the reliable core
  (`company <krs>` / `analyze <krs>`): name, legal form, NIP/REGON, seat, **share capital**, purpose
  (PKD), management board (names GDPR-masked), and the **filed annual-statement list** (periods +
  dates). `nip <nip>` resolves a tax id → KRS via the MF whitelist. `search "name"` uses the stealth
  browser (the portal is Incapsula-protected) and returns tagged `{krs, name, city, register}`
  candidates → then `analyze <krs>`. Figure extraction from the e-sprawozdania (JPK XML) is
  session-gated and not implemented; the filing list + repository link are returned.
- **UK (Companies House)**, free API, balance-sheet metadata; needs `COMPANIES_HOUSE_API_KEY`.
  Parsed financial figures require XBRL (not implemented, see ROADMAP.md).

**Not supported (paid only):** Austria, Spain, Netherlands.

## Setup (non-German keys)

Keys are read from environment variables, or a local `config/keys.json` (git-ignored). Never hardcode.

```json
{ "COMPANIES_HOUSE_API_KEY": "…",   // UK, free at developer.company-information.service.gov.uk
  "INPI_API_TOKEN": "…" }           // France, optional (basic search works without)
```

Poland needs no key. Germany needs no key beyond the logged-in `claude` CLI.
