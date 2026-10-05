---
name: krs-b44x
title: Krajowy Rejestr Sądowy (KRS)
description: 'Fetch official company and foundation records from Krajowy Rejestr Sądowy (KRS) via the Ministry of Justice API. Retrieve company legal status, board members (zarząd), supervisory council (rada nadzorcza), commercial proxies (prokurenci), share capital, registered address, NIP, REGON, and exact legal representation rules (sposób reprezentacji: kto może podpisywać umowy). Checks both commercial companies (Rejestr Przedsiębiorców P: Sp. z o.o., S.A., P.S.A.) and non-profits (Rejestr Stowarzyszeń/Fundacji S). Automatically pads KRS numbers to 10 digits. Use whenever the user asks about KRS, "kto może podpisać umowę", "sprawdź spółkę w KRS", "odpis KRS", "zarząd spółki", "kapitał zakładowy", or "reprezentacja spółki".'
author: b44x
author_url: https://github.com/b44x/ai-polish-skills/tree/dev/skills/krs
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: pl
practice: corporate
language: en
tags: [krs, spolki, zarzad, reprezentacja, prawo, umowy, rejestr-sadowy]
sources:
- title: Output
  path: references/output.md
---

# Krajowy Rejestr Sądowy (KRS)

Fetches official registration records, corporate representation rules, and board composition
from the Polish Ministry of Justice (*Ministerstwo Sprawiedliwości*) using `scripts/krs.py`. Always outputs structured JSON.

## Running the script

Run from this skill's directory (or use relative path from repo root):

| OS | Command |
|---|---|
| Linux / macOS | `python3 scripts/krs.py <command> …` |
| Windows | `py scripts/krs.py <command> …` (or `python`) |

Zero external dependencies required (standard library only).

## Workflow

1. **Company Summary & Verification:**
   - User provides a KRS number (with or without leading zeros, e.g. `6865` or `0000006865`):
     `python3 scripts/krs.py info <krs>`
   - The script automatically pads the number to 10 digits and queries the Entrepreneurs register (`P`), falling back to Associations/Foundations (`S`).
   - Report company name, legal form, registered seat/address, share capital, and active status.

2. **Contract Signing Authority (Representation Check):**
   - User asks "who can sign a contract for company X?" or wants to verify a signature:
     `python3 scripts/krs.py repr <krs>`
   - Carefully review `sposobReprezentacji` (e.g. single board member vs. two members acting jointly vs. member + proxy).
   - List the active board members (`zarzad`) and proxies (`prokurenci`).

3. **Full Extract (Historical):**
   - When the user needs the complete record or past changes:
     `python3 scripts/krs.py full <krs> --history`

## Commands

| Command | Description | Returns |
|---|---|---|
| `info <krs> [--rejestr P\|S]` | Structured digest of company/foundation data | `nazwa`, `formaPrawna`, `nip`, `regon`, `adres`, `kapitalZakladowy`, `sposobReprezentacji`, `zarzad`, `prokurenci`, `radaNadzorcza`, `czyWLikwidacji` |
| `repr <krs> [--rejestr P\|S]` | Representation formula and authorized signatories | `sposobReprezentacji`, `zarzad`, `prokurenci` |
| `full <krs> [--history]` | Complete raw JSON extract from Ministry of Justice | Full OdpisAktualny or OdpisPelny |

Field reference: [references/output.md](references/output.md).

## Exit codes

JSON goes to stdout; errors go to stderr as `{"error": "...", "type": "..."}`.

| Code | Meaning | What to do |
|---|---|---|
| `0` | Success | Use the JSON output |
| `2` | Not found | KRS number not found in register P or S |
| `64` | Bad usage | Invalid KRS format (must be 1-10 digits) |
| `69` | Network / KRS server error | Retry once; check internet connection |

## Rules

- Always verify the representation method (`sposobReprezentacji`) before confirming who can legally bind the company.
- Never invent board members or proxy holders not present in the official KRS extract.
