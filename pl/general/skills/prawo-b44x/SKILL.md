---
name: prawo-b44x
title: Prawo (ISAP / Dziennik Ustaw)
description: 'Official Polish legal acts from the Sejm ELI API (ISAP: Dziennik Ustaw, Monitor Polski). Read the wording of a specific article of a code or statute, together with the source document and date, and a warning about amendments that entered into force later. Check whether an act is in force, find its latest consolidated text (tekst jednolity), list amendments with entry-into-force dates (including upcoming ones), and search acts by title. Shortcuts for the main codes (kp, kc, kk, kpc, ksh, kpa, vat, pit, cit, op…). Use whenever the user asks about Polish law, e.g. "co mówi art. 30 Kodeksu pracy", "okres wypowiedzenia umowy o pracę", "czy ta ustawa obowiązuje", "tekst jednolity ustawy o VAT", "kiedy wchodzą zmiany w Kodeksie pracy", "Dz.U. 2023 poz. 1465", "przepisy o pracy zdalnej".'
author: b44x
author_url: https://github.com/b44x/ai-polish-skills/tree/dev/skills/prawo
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: pl
practice: general
language: en
tags: [prawo, ustawy, kodeks, isap, dziennik-ustaw, tekst-jednolity, przepisy, eli]
sources:
- title: Output
  path: references/output.md
---

# Prawo (ISAP / Dziennik Ustaw)

Fetches Polish legal acts from the official ELI API of the Chancellery of the Sejm using
`scripts/prawo.py`. Always outputs structured JSON.

## Running the script

Run from this skill's directory (or use relative path from repo root):

| OS | Command |
|---|---|
| Linux / macOS | `python3 scripts/prawo.py <command> …` |
| Windows | `py scripts/prawo.py <command> …` (or `python`) |

Zero external dependencies required (standard library only).

## Critical: how current is the text?

The API publishes HTML only for some documents. The newest consolidated texts (teksty jednolite)
are often **PDF-only**, and the HTML of an amended act is its **original** wording from the day it
was published. `article` therefore:

1. reads the newest consolidated text that has HTML (or the act itself if it was never amended),
2. reports that document in `sourceDocument` (`ref`, `date`, `kind`),
3. lists every amendment that entered into force after that date in `amendmentsAfterSource`,
4. sets `upToDate` and `warning`.

When `upToDate` is `false`, **always** tell the user the date of the wording and that later
amendments exist, and give the PDF link of the newest consolidated text. Never present such text as
the certain current wording. For the Constitution the API has no HTML at all: give the PDF link.

## Workflow

1. **Article wording** ("co mówi art. 30 KP", "okres wypowiedzenia"):
   `python3 scripts/prawo.py article kp 30`
   - Article numbers: `30`, `22a`, `67^18` (superscript `67¹⁸` also works).
   - Quote the text, then state `sourceDocument.displayAddress` and `sourceDocument.date`.
   - If `upToDate` is false, add the `warning` in your own words and the newest PDF link.

2. **Is the act in force / latest consolidated text / upcoming changes:**
   `python3 scripts/prawo.py act kp`
   - `latestConsolidatedText` (with PDF link), `amendmentsAfterLatestConsolidatedText`,
     `upcomingAmendments` (entry into force in the future), `status`, `inForce`.

3. **Act by reference:** `act` and `article` accept a shortcut (`kp`, `vat`…), `DU/2023/1465`,
   `Dz.U. 2023 poz. 1465`, `Dz.U. 1974 nr 24 poz. 141` or an ISAP address `WDU20230001465`.
   List shortcuts with `python3 scripts/prawo.py codes` (works offline).

4. **Search by title** (acts without a shortcut):
   `python3 scripts/prawo.py search "o ochronie danych osobowych" --type Ustawa --in-force`
   - Results include amending acts ("o zmianie ustawy…"); pick the act the user means, then call `act`.

## Commands

| Command | Description | Returns |
|---|---|---|
| `article <ref> <nr> [--original]` | Wording of one article with its source and freshness | `text`, `sourceDocument`, `upToDate`, `amendmentsAfterSource`, `newerConsolidatedTextsPdfOnly`, `warning` |
| `act <ref> [--limit N]` | Status, consolidated texts, amendments and links | `status`, `inForce`, `latestConsolidatedText`, `amendmentsAfterLatestConsolidatedText`, `upcomingAmendments`, `links` |
| `search <query> [--in-force] [--type T] [--year Y] [--publisher DU\|MP] [--limit N]` | Search acts by words in the title | `results[]` with `ref`, `displayAddress`, `title`, `status` |
| `codes` | Offline list of shortcuts for the main codes and statutes | `codes[]` with `code`, `ref`, `name` |

Field reference: [references/output.md](references/output.md).

## Exit codes

JSON goes to stdout; errors go to stderr as `{"error": "...", "type": "..."}`.

| Code | Meaning | What to do |
|---|---|---|
| `0` | Success | Use the JSON output |
| `2` | Not found / not available | Act or article does not exist, or no HTML text exists (error names the PDF link) |
| `64` | Bad usage / validation | Unrecognised act reference or article number |
| `69` | Network / API error | Retry once; check internet connection |

## Rules

- This skill returns legal text, not legal advice. Do not interpret provisions as advice for the
  user's specific case; suggest a lawyer (adwokat, radca prawny) for that.
- Always cite the act and the source document, e.g. "art. 36 § 1 Kodeksu pracy (tekst jednolity
  Dz.U. 2023 poz. 1465)".
- `--original` returns the historical wording of an amended act. Use it only when the user asks
  about the original or historical text, and say so.
