---
name: biala-lista-b44x
title: Biała Lista Podatników VAT
description: Check Polish businesses and VAT status in the official Ministry of Finance White List (Biała Lista Podatników VAT). Verify active VAT payer status (Czynny / Zwolniony / Niezarejestrowany), legal company name, REGON, KRS, registered address, and settlement bank accounts by NIP or REGON. Check if a contractor's bank account is on the whitelist before making B2B transfers (critical for split payment and tax deductibility above 15,000 PLN). Reverse-lookup company by 26-digit Polish bank account number (NRB/IBAN). Validate NIP, REGON, and IBAN checksums offline. Use whenever the user asks about NIP, REGON, Biała Lista VAT, "sprawdź NIP", "sprawdź kontrahenta", "status VAT spółki", "czy numer konta jest na białej liście", or verifying a Polish invoice.
author: b44x
author_url: https://github.com/b44x/ai-polish-skills/tree/dev/skills/biala-lista
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: pl
practice: tax
language: en
tags: [biala-lista, vat, nip, regon, split-payment, podatki, faktury, rachunek-bankowy]
sources:
- title: Output
  path: references/output.md
---

# Biała Lista Podatników VAT

Fetches official Polish company and VAT status data from the Ministry of Finance (*Ministerstwo Finansów*)
using `scripts/biala_lista.py`. Always outputs structured JSON.

## Running the script

Run from this skill's directory (or use relative path from repo root):

| OS | Command |
|---|---|
| Linux / macOS | `python3 scripts/biala_lista.py <command> …` |
| Windows | `py scripts/biala_lista.py <command> …` (or `python`) |

Zero external dependencies required (standard library only).

## Workflow

1. **Identify the query type:**
   - **NIP (10 digits)**: User provides NIP or asks about a company → `python3 scripts/biala_lista.py nip <nip>`.
   - **Bank Account (26 digits)**: User wants to know who owns an account or if it's safe to pay →
     - Check specific NIP + account match: `python3 scripts/biala_lista.py check <nip> <account>`
     - Find company by account number: `python3 scripts/biala_lista.py account <account>`
   - **REGON (9 or 14 digits)**: User provides REGON → `python3 scripts/biala_lista.py regon <regon>`.
   - **Syntax verification (offline)**: User asks to validate NIP/REGON/IBAN without querying API → `python3 scripts/biala_lista.py validate <value>`.

2. **Historical or specific date:**
   - Add `--date=YYYY-MM-DD` when checking status for a past invoice or event (defaults to today).

3. **Interpret the results:**
   - `statusVat`: `"Czynny"` (active VAT payer — eligible for standard VAT deduction), `"Zwolniony"` (exempt), `"Niezarejestrowany"` (not registered).
   - `accountAssigned`: `"TAK"` (account is registered on the White List — safe for payments > 15,000 PLN) or `"NIE"`.
   - `requestId`: Always note the `requestId` when reporting verification for financial/tax records — it provides legal proof of due diligence (*należyta staranność*) under Polish tax law.

## Commands

| Command | Description | Returns |
|---|---|---|
| `nip <nip> [--date=YYYY-MM-DD]` | Look up company details & VAT status by NIP | `name`, `statusVat`, `isVatActive`, `address`, `krs`, `regon`, `accounts`, `representatives`, `requestId` |
| `check <nip> <account> [--date=YYYY-MM-DD]` | Verify if bank account is on the White List for this NIP | `accountAssigned` (`"TAK"` / `"NIE"`), `isAssigned`, `bank`, `requestId`, `requestDateTime` |
| `account <account> [--date=YYYY-MM-DD]` | Reverse-lookup company associated with a bank account | `accountFormatted`, `bank`, `subjects` list with company details |
| `regon <regon> [--date=YYYY-MM-DD]` | Look up company details by REGON (9 or 14 digits) | Same object as `nip` |
| `validate <value>` | Offline checksum validation for NIP, REGON, or NRB | `type`, `valid`, `formatted`, `bank` (if NRB), `message` |

Field reference and legal context: [references/output.md](references/output.md).

## Exit codes

JSON goes to stdout; errors go to stderr as `{"error": "...", "type": "..."}`.

| Code | Meaning | What to do |
|---|---|---|
| `0` | Success | Use the JSON output |
| `2` | Not found | Subject or account not found in the official registry |
| `64` | Validation / Bad usage | Invalid NIP/REGON/account checksum or bad arguments |
| `69` | Network / API / Rate limit | Retry once; check internet connection |

## Rules

- For B2B transfers above 15,000 PLN gross, always emphasize checking both `statusVat: "Czynny"` and `accountAssigned: "TAK"`.
- If an entity uses virtual accounts (`hasVirtualAccounts: true`), remind the user that `check <nip> <account>` should be used rather than inspecting the static `accounts` list.
- Stripping spaces, dashes, and the `PL` prefix is handled automatically by the script.
