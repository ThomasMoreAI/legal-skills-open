# European Company Registers

Look up a company's financials and register data from Germany, France, Poland and the UK, without paying a data provider. It's a set of small command-line scripts and an [agent skill](#use-it-as-a-claude--llm-skill) for Claude (or any LLM): revenue, balance sheet and earnings from the official filings, plus managing directors, share capital and legal form straight from the register.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Node.js](https://img.shields.io/badge/Node.js-≥18-339933?logo=node.js&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white)
![No paid API](https://img.shields.io/badge/paid%20data%20API-not%20required-brightgreen)

I kept seeing company names I wanted to size up (how much revenue, are they actually big) and I hated going to the Bundesanzeiger by hand every time. So I wrote scrapers for the official registers and had them return clean JSON. It grew from one German script into four countries.

## Coverage

| Country | Source | What you get | Needs |
|---|---|---|---|
| 🇩🇪 Germany | Unternehmensregister + Bundesanzeiger | Financials: revenue, total assets, equity, earnings, P&L lines, employees, per fiscal year (including GJ 2022+ after DiRUG) plus the full report text | `claude` CLI; stealth browser for GJ 2022+ |
| 🇩🇪 Germany | Handelsregister (handelsregister.de) | Register content: managing directors / board, share capital, legal form, registered seat, purpose, Prokura, former names | stealth browser + `pdftotext` |
| 🇫🇷 France | INPI / RNE (`recherche-entreprises.api.gouv.fr`) | Revenue and net result per year, officers (dirigeants), full metadata | nothing (free, no key) |
| 🇵🇱 Poland | KRS (Ministry of Justice) | Legal form, NIP/REGON, seat, share capital, purpose (PKD), board, list of filed annual statements | nothing (key-free); stealth browser for name search |
| 🇬🇧 UK | Companies House | Company profile, officers, filing history, balance-sheet metadata | free API key |

Austria, Spain and the Netherlands are paid-only, so they're not covered.

## Why I bothered

The commercial company-data APIs (D&B, Orbis, North Data and friends) charge real money for information that is public by law. The official registers give it away for free. The catch is that each one buries it behind something different: a CAPTCHA here, a session-bound encrypted payload there, a JSF state machine, an anti-bot wall, a PDF. This repo does that annoying work once and hands you JSON.

Two parts of the German path took real effort:

It gets the DiRUG split right. Since the DiRUG reform, annual accounts for fiscal years that start after 31 December 2021 are no longer published in the Bundesanzeiger. They moved to the Unternehmensregister. A Bundesanzeiger-only scraper is therefore about three years out of date. This one queries both sources at the same time and sends each fiscal year to whichever source actually holds it.

It reads the numbers for free, with an LLM. German accounts sit behind a CAPTCHA on the older years and a "Ich bin ein Mensch" checkbox on the newer ones. There's no paywall, only friction. So Claude Haiku reads the CAPTCHA image and Claude Sonnet pulls the figures out of the German report text. No paid financial-data API, no OCR service.

## Quick start

```bash
git clone https://github.com/tfbecker/european-company-registers.git
cd european-company-registers
REG="$PWD/scripts"

# Germany: list a company's filings (fast, no key, no CAPTCHA)
node "$REG/de-combined.js" search "Pergolux"

# Germany: extract the actual figures for the newest years
node "$REG/de-combined.js" report "Pergolux"

# Germany: register content (directors, share capital, legal form)
node "$REG/de-handelsregister.js" search "Holz-Richter"

# France: real revenue and officers, free, no key
node "$REG/fr-inpi.js" analyze "Carrefour"

# Poland: by KRS number
node "$REG/pl-krs.js" company 0000019193

# UK: Companies House (needs a free key, see Setup)
node "$REG/gb-companies-house.js" search "Tesco"
```

Everything prints JSON to stdout.

## Germany: financials (Unternehmensregister + Bundesanzeiger)

This is the main path. Both sources are queried at once, and the listing step never hits a CAPTCHA.

```bash
node "$REG/de-combined.js" search  "Pergolux"              # newest report only  (~0.4 s, default)
node "$REG/de-combined.js" search  "Pergolux" --all        # all reports, both sources
node "$REG/de-combined.js" report  "Pergolux"              # search once, then extract every free year's figures
node "$REG/de-combined.js" analyze "Pergolux" --year 2021  # one specific year's figures
```

Use `report` when you want numbers across several years. It searches once and extracts the newest N years (5 by default) in one process, routing each year to its source. Don't loop `analyze` per year.

Listing output from `search` (this is a real response):

```json
{
  "country": "de",
  "searched_name": "Pergolux",
  "found": true,
  "companies": [
    {
      "name": "Pergolux GmbH",
      "location": "Fulda",
      "euid": "DEM1301.HRB8398",
      "register": "HRB 8398",
      "court": "Fulda",
      "state": "Hessen",
      "newest_fiscal_year": "2024",
      "reports": [
        { "fiscal_year": "2024",
          "report_name": "Jahresabschluss zum Geschäftsjahr vom 01.01.2024 bis zum 31.12.2024",
          "date": "2026-04-27", "sources": ["unternehmensregister"] }
      ]
    }
  ]
}
```

The figures output from `report` and `analyze` carries a `financial_data` object per year:

```jsonc
{
  "fiscal_year": "2021",
  "revenue": 1216000000,
  "total_assets": 892000000,
  "equity": 410000000,
  "liabilities": 482000000,
  "earnings": 63000000,
  "operating_result": 71000000,
  "personnel_expenses": 148000000,
  "employees": 1240,
  "is_group_report": false,
  "currency": "EUR"
}
```

The full report text (Jahresabschluss, Lagebericht, Anhang) also gets saved to `./register-texts/` by default. That's the qualitative stuff the numbers miss: strategy, outlook, risks, ownership, related parties. See [`SKILL.md`](SKILL.md) for every flag.

## Germany: register content (Handelsregister)

Not financials, the register entry itself: legal form, seat, purpose, share capital, and the people.

```bash
node "$REG/de-handelsregister.js" search  "Holz-Richter"
node "$REG/de-handelsregister.js" details "Holz-Richter GmbH" --hrb 37497 --court Köln
```

`details` downloads the Aktueller Abdruck (AD), runs `pdftotext`, and parses it into structured JSON: `share_capital`, `managing_directors[]` (with birth dates), `prokura[]`, `legal_form`, `purpose`, `seat`. Match a company by its HRB, not by result position, because the order isn't stable. handelsregister.de throttles document downloads, so retry `details` after a short cooldown.

## France: INPI / RNE

Free, no key. Real revenue (`ca`) and net result per year plus the officers, from the open financial-ratios dataset.

```bash
node "$REG/fr-inpi.js" analyze "Carrefour"   # a name (best match) or a SIREN
```

```json
{
  "company_name": "CARREFOUR",
  "country": "fr",
  "registration_id": "652014051",
  "found": true,
  "officers": [
    { "name": "ALEXANDRE BOMPARD",
      "role": "Président du conseil d'administration et directeur général",
      "birth_year": "1972" }
  ]
}
```

An optional free `INPI_API_TOKEN` adds balance-sheet depth (total assets, equity). Revenue works without it.

## Poland: KRS

The official Ministry-of-Justice API by KRS number is the reliable core:

```bash
node "$REG/pl-krs.js" company 0000019193   # by KRS
node "$REG/pl-krs.js" nip     5252344078   # tax id to KRS
node "$REG/pl-krs.js" search  "CD PROJEKT" # name search (stealth browser, Incapsula-protected)
```

You get legal form, NIP/REGON, seat, share capital, purpose (PKD), the board (names GDPR-masked), and the list of filed annual statements with periods, dates and a repository link.

## UK: Companies House

```bash
node "$REG/gb-companies-house.js" search   "Tesco"
node "$REG/gb-companies-house.js" company  00445790
node "$REG/gb-companies-house.js" filings  00445790
```

Company profile, officers and filing history through the free Companies House API. Parsed balance-sheet figures need XBRL, which isn't done yet (see [`ROADMAP.md`](ROADMAP.md)).

## Use it as a Claude / LLM skill

The repo doubles as an [Agent Skill](https://docs.claude.com/en/docs/claude-code/skills). [`SKILL.md`](SKILL.md) carries the frontmatter and usage so an agent knows when and how to call each script. Drop the repo into your skills directory:

```bash
git clone https://github.com/tfbecker/european-company-registers.git ~/.claude/skills/european-company-registers
```

Then ask in plain language: *"What was Pergolux's revenue over the last three years, and who are the managing directors?"* The agent runs the right scripts and reads the JSON back. The scripts are ordinary CLIs, so they also work fine from your own code, a cron job, or any other LLM tool-calling loop.

## Requirements and setup

Node.js 18+ and Python 3.9+. There's no `npm install` and no build step, since the scripts only use the standard library.

German financials need a logged-in [`claude` CLI](https://docs.claude.com/en/docs/claude-code) for the CAPTCHA vision and the figure extraction. It's auto-detected, or set `CLAUDE_BIN`. Those two steps are Claude-specific for now (see [`ROADMAP.md`](ROADMAP.md) for making the extractor model-agnostic).

The browser-driven paths (DE Handelsregister, DE GJ 2022+ documents, PL name search) need a stealth Chromium that exposes `from cloakbrowser import launch` (a Playwright `Browser`). Point `COMPANY_REGISTERS_BROWSER` at the directory that provides it. The HTTP-only paths (DE Bundesanzeiger up to 2021, FR, UK, PL-by-number) need no browser.

The Handelsregister `details` parser needs `pdftotext` (poppler).

API keys are only needed for the UK (required) and France (optional). Set them as env vars, or copy `config/keys.example.json` to `config/keys.json` (git-ignored):

```json
{ "COMPANIES_HOUSE_API_KEY": "get-a-free-key-at-developer.company-information.service.gov.uk",
  "INPI_API_TOKEN": "optional-free-token-for-french-balance-sheet-depth" }
```

Germany and Poland need no API key.

## Responsible use

These are public registers and the data is public by law, but the portals still have terms of use and rate limits. Query politely, cache what you get (the tool saves report text so you don't refetch), and don't hammer the sites. The Handelsregister path already backs off when it's throttled. You're responsible for how you use the data, and GDPR applies to personal data such as directors' names. This project isn't affiliated with any register operator.

## Roadmap

[`ROADMAP.md`](ROADMAP.md) has the open items: UK XBRL figure parsing, Polish e-sprawozdania (JPK) extraction, INPI balance-sheet depth, and a model-agnostic extractor.

## License

[MIT](LICENSE), Felix Becker.

---
---

# 🇩🇪 Europäische Handelsregister für LLMs

Firmen-Finanzdaten und Registerinhalte aus Deutschland, Frankreich, Polen und UK abfragen, ohne einen teuren Datenanbieter. Ein paar kleine Kommandozeilen-Skripte und ein Agent Skill für Claude (oder jedes andere LLM): Umsatz, Bilanz und Jahresüberschuss aus den offiziellen Jahresabschlüssen, dazu Geschäftsführer, Stammkapital und Rechtsform direkt aus dem Register.

Ich wollte ständig wissen, wie groß eine Firma ist, deren Namen ich irgendwo aufschnappe, und hatte keine Lust, jedes Mal von Hand in den Bundesanzeiger zu gehen. Also habe ich Scraper für die amtlichen Register geschrieben, die sauberes JSON zurückgeben. Aus einem deutschen Skript wurden vier Länder.

## Abdeckung

| Land | Quelle | Was du bekommst | Braucht |
|---|---|---|---|
| 🇩🇪 Deutschland | Unternehmensregister + Bundesanzeiger | Finanzdaten: Umsatz, Bilanzsumme, Eigenkapital, Jahresüberschuss, GuV-Posten, Mitarbeiter, je Geschäftsjahr (inkl. GJ 2022+ nach DiRUG) plus voller Berichtstext | `claude` CLI; Stealth-Browser für GJ 2022+ |
| 🇩🇪 Deutschland | Handelsregister (handelsregister.de) | Registerinhalt: Geschäftsführer/Vorstand, Stammkapital, Rechtsform, Sitz, Gegenstand, Prokura, frühere Namen | Stealth-Browser + `pdftotext` |
| 🇫🇷 Frankreich | INPI / RNE | Umsatz und Jahresergebnis je Jahr, Organe (dirigeants), Metadaten | nichts (kostenlos) |
| 🇵🇱 Polen | KRS (Justizministerium) | Rechtsform, NIP/REGON, Sitz, Stammkapital, Gegenstand (PKD), Vorstand, Liste der Jahresabschlüsse | nichts (kostenlos) |
| 🇬🇧 UK | Companies House | Firmenprofil, Organe, Filing-History, Bilanz-Metadaten | kostenloser API-Key |

Österreich, Spanien und die Niederlande sind nur kostenpflichtig zu haben und deshalb nicht dabei.

## Worum es geht

Die kommerziellen Firmendaten-Anbieter verlangen viel Geld für Informationen, die von Gesetzes wegen öffentlich sind. Die amtlichen Register geben sie kostenlos heraus, verstecken sie aber jeweils hinter etwas anderem: CAPTCHA, sitzungsgebundene verschlüsselte Payloads, JSF-Zustandsmaschinen, Bot-Schutz, PDFs. Dieses Repo macht diese Arbeit einmal und liefert dir JSON.

Zwei Dinge am deutschen Pfad waren echte Arbeit:

Der DiRUG-Bruch. Seit der DiRUG-Reform werden Jahresabschlüsse für Geschäftsjahre, die nach dem 31.12.2021 beginnen, nicht mehr im Bundesanzeiger veröffentlicht, sondern im Unternehmensregister. Ein reiner Bundesanzeiger-Scraper ist dadurch rund drei Jahre veraltet. Dieses Tool fragt beide Quellen parallel ab und routet jedes Geschäftsjahr zur richtigen.

Die Zahlen kostenlos auslesen, per LLM. Die Abschlüsse liegen hinter einem CAPTCHA (ältere Jahre) oder einer "Ich bin ein Mensch"-Checkbox (neuere Jahre), keine Bezahlschranke, nur Reibung. Claude Haiku liest das CAPTCHA-Bild, Claude Sonnet holt die Zahlen aus dem deutschen Berichtstext. Keine kostenpflichtige Finanz-API, kein OCR-Dienst.

## Schnellstart

```bash
git clone https://github.com/tfbecker/european-company-registers.git
cd european-company-registers
REG="$PWD/scripts"

node "$REG/de-combined.js" search  "Pergolux"     # Jahresabschlüsse auflisten (schnell, ohne Key)
node "$REG/de-combined.js" report  "Pergolux"     # Umsatz/Bilanz der letzten Jahre auslesen
node "$REG/de-handelsregister.js" search "Holz-Richter"   # Geschäftsführer, Stammkapital, Rechtsform
node "$REG/fr-inpi.js" analyze "Carrefour"        # FR: Umsatz und Organe, kostenlos
```

## Als Claude / LLM Skill nutzen

Das Repo ist zugleich ein [Agent Skill](https://docs.claude.com/en/docs/claude-code/skills). [`SKILL.md`](SKILL.md) enthält das Frontmatter samt Nutzung, damit ein Agent weiß, wann und wie er die Skripte aufruft.

```bash
git clone https://github.com/tfbecker/european-company-registers.git ~/.claude/skills/european-company-registers
```

Dann in normaler Sprache fragen: *"Wie hoch war der Umsatz der Pergolux GmbH in den letzten drei Jahren, und wer sind die Geschäftsführer?"* Der Agent ruft die passenden Skripte auf und liest das JSON zurück.

## Voraussetzungen

Node.js 18+ und Python 3.9+, kein `npm install`, kein Build. Deutsche Finanzdaten brauchen eine eingeloggte `claude` CLI (für CAPTCHA-Vision und Extraktion). Die Browser-Pfade (Handelsregister, GJ 2022+, PL-Namenssuche) brauchen einen Stealth-Chromium (`COMPANY_REGISTERS_BROWSER` setzen). Die HTTP-Pfade (Bundesanzeiger bis 2021, FR, UK, PL per Nummer) nicht. API-Keys nur für UK (nötig) und Frankreich (optional). Deutschland und Polen brauchen keinen Key.

## Rechtliches

Die Register sind öffentlich, aber die Portale haben Nutzungsbedingungen und Rate-Limits. Fair abfragen, Ergebnisse cachen, die Seiten nicht überlasten. Für die Nutzung der Daten bist du selbst verantwortlich, und die DSGVO gilt für personenbezogene Daten wie Geschäftsführernamen. Das Projekt steht in keiner Verbindung zu den Registerbetreibern.

## Lizenz

[MIT](LICENSE), Felix Becker.
