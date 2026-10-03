---
name: i18n-locale-correctness
title: Locale correctness for data that users type
description: Use when building or reviewing forms, validators, formatters, database schemas or search that touch names, addresses, postcodes, phone numbers, dates, times, numbers, currency, sorting or casing for users outside the United States. Also use when a regex, a two-field name split, a `state` column, a `toUpperCase()` call or an `MM/DD/YYYY` format is about to be written, when a US or English-language tutorial is being adapted for a European product, or before a product ships to a second country.
author: clemensjl
author_url: https://github.com/clemensjl/claude-skills/tree/main/skills/i18n-locale-correctness
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: data-protection
language: en
sources:
- title: Addresses
  path: references/addresses.md
- title: Checklist
  path: references/checklist.md
- title: Collation and search
  path: references/collation-and-search.md
- title: Dates and times
  path: references/dates-and-times.md
- title: Form fields
  path: references/form-fields.md
- title: Identifiers
  path: references/identifiers.md
- title: Intake
  path: references/intake.md
- title: Locale negotiation
  path: references/locale-negotiation.md
- title: Messages and plurals
  path: references/messages-and-plurals.md
- title: Names
  path: references/names.md
- title: Numbers and currency
  path: references/numbers-and-currency.md
- title: Phone numbers
  path: references/phone-numbers.md
- title: Test data
  path: references/test-data.md
- title: Text handling
  path: references/text-handling.md
---

# Locale correctness for data that users type

Rules for getting locale-dependent data right in software. The governing sources are Unicode CLDR (48.2, released 2026-03-17, `cldr.unicode.org/index/downloads`), UTS #35 (LDML, including Part 8 Person Names and the MessageFormat 2.0 spec), the Unicode Standard 17.0.0 (2025-09-09), the IANA time zone database (2026c, released 2026-07-08, `iana.org/time-zones`), ISO 8601, ISO 4217 (List One published 2026-01-01), ISO 13616 (IBAN), ITU-T E.164 (02/2026), the HTML Living Standard autofill section, and ECMA-402 (`Intl`). Status as at 2026-08-05.

**Core principle:** almost every field a developer treats as universal is a US convention with a regex attached. "First name / last name", `state`, a five-digit zip, a ten-digit phone, `MM/DD/YYYY`, a period as decimal separator and `toUpperCase()` are each an assumption that breaks in a real market. The rule this skill enforces: **never validate what you can normalise, never split what you can store whole, never hard-code what CLDR already knows.** A field that rejects a valid user is a worse bug than a field that accepts a messy one — the messy one can be cleaned later, the rejected user is gone.

## Limits

This skill decides data shape and formatting, not law, not tax, not payment settlement.

- It does **not** decide whether you may collect a field. Lawfulness, consent and retention are `legal-at` / `legal-eu` territory. This skill only says how the field must be shaped once you have decided to collect it.
- It does **not** confirm that an identifier belongs to a real entity. A passing checksum proves the format, never the existence, the ownership or the tax status. Registration status is a live registry lookup (VIES, Firmenbuch, Companies House) and, for VAT liability, an accountant's call.
- It does **not** replace a payments integration. An IBAN that passes mod-97 can still be closed, wrong-currency or not reachable via SEPA.
- Every per-country table and every validator produced here is a **snapshot of upstream data**. Ship it with `<!-- LOCALE SNAPSHOT 2026-08-05 — regenerate from CLDR / IANA / IBAN Registry before release -->` and never remove the marker silently. Postcode ranges, VAT formats, phone metadata and time zone rules all change on their own schedule; libphonenumber alone published v9.0.30 through v9.0.36 between 2026-05-07 and 2026-07-31 (`github.com/google/libphonenumber/releases`).

## Workflow

1. **Run the intake first.** `references/intake.md`. Which markets, which scripts, which fields, what already exists in the database. Without the answers every table below is guesswork, and the wrong answer is silently wrong.
2. **Pick the rows from the decision matrix** that this change actually touches. Do not audit the whole product.
3. **Read the reference file before writing any code or any table.** The per-locale specifics are too fine-grained to recall — `de-AT` and `de-DE` disagree on the group separator, Ireland requires no field at all, and Italy keeps its trunk zero.
4. **Run `references/test-data.md` against the implementation.** Every value in it breaks a naive version. A change that has not been run against it is not reviewed.
5. **Walk `references/checklist.md`** before ship and report findings, not reassurance.

**Output shape.** Four parts, in this order:

1. the artefact — schema, validator, formatter, form spec or finding table — carrying the snapshot marker
2. the `[[MISSING: …]]` list of values only the user can supply (target markets, existing column types, ICU availability on the runtime)
3. adjacent open items in one sentence each — the fields this change touched that are still wrong
4. the data-freshness note naming the upstream version each table came from

Never fill a `[[MISSING: …]]` with a plausible value. A guessed market list produces a validator that rejects real customers.

## Decision matrix

| Situation | What applies | Reference |
|---|---|---|
| Signup, profile or checkout form with name fields | CLDR person name model, single required full-name field | `names.md` |
| Address form, shipping form, invoice address | libaddressinput `fmt`/`require`, HTML autofill tokens | `addresses.md`, `form-fields.md` |
| Postcode validation or a postcode column | Per-country pattern, optional by default | `addresses.md` |
| Phone input, SMS, 2FA, WhatsApp | E.164 storage, libphonenumber parsing | `phone-numbers.md` |
| IBAN, BIC, VAT ID, company or tax number | ISO 13616 mod-97, ISO 7064, VIES, national checksums | `identifiers.md` |
| Any timestamp, scheduling, recurring events, calendars | ISO 8601 / RFC 3339 storage, IANA zone ids, Temporal | `dates-and-times.md` |
| Prices, totals, quantities, percentages, invoices | ISO 4217 minor units, integer storage, `Intl.NumberFormat` | `numbers-and-currency.md` |
| Any sorted list, autocomplete, dedupe, uniqueness index | UCA, `Intl.Collator`, Postgres collations, NFC | `collation-and-search.md` |
| Length limits, truncation, avatars, RTL content, CJK layout | Grapheme clusters, `Intl.Segmenter`, bidi isolates | `text-handling.md` |
| Any user-visible string with a number or a variable in it | CLDR plural categories, MessageFormat 2.0 | `messages-and-plurals.md` |
| Choosing which locale to serve, URL design, `Accept-Language` | BCP 47, lookup vs filtering, fallback chains | `locale-negotiation.md` |
| Reviewing an existing implementation | Breaking values, then the checklist | `test-data.md`, `checklist.md` |

## Hard rules

- **Never regex-validate a phone number.** Parse it with libphonenumber metadata and store E.164. Google ships metadata roughly every one to three weeks (v9.0.30 on 2026-05-07 through v9.0.36 on 2026-07-31); any regex you write is stale before it merges. ITU-T E.164 (02/2026) is a numbering plan, not a syntax you can match.
- **Never make family name mandatory and never split a name the user gave you whole.** `full_name` is the required column; `given`/`surname` are optional derived hints. CLDR's person name model (UTS #35 Part 8) has seven fields — `title`, `given`, `given2`, `surname`, `surname2`, `generation`, `credentials` — plus modifiers, precisely because two fields do not fit.
- **Never call `toUpperCase()` or `toLowerCase()` on text a human typed.** Verified on Node 22 / ICU 77: `'TITLE'.toLocaleLowerCase('tr')` is `"tıtle"`, so a Turkish-locale lowercase of a username breaks equality; `'ß'.toUpperCase()` is `"SS"`, so uppercasing changes string length. Use `Intl.Collator` for comparison and leave display casing to the user.
- **Never sort user-visible strings with `Array.prototype.sort()`.** It compares UTF-16 code units. Verified: the default sort orders `["Apfel","Bär","Ost","Zug","Zürich","Äpfel","Öl"]` — every accented word dumped after `Z`. `Intl.Collator('de')` gives `["Apfel","Äpfel","Bär","Öl","Ost","Zug","Zürich"]`.
- **Never store a local time without its IANA zone id, and never substitute an offset for a zone.** Verified for `Europe/Vienna`: 2026-10-25 02:30 local occurs twice (once at +02:00, once at +01:00) and 2026-03-29 02:30 local never occurs. An offset column cannot express either. `Etc/GMT+1` is UTC−01:00, not +01:00 — the POSIX sign is inverted (verified via `Intl.DateTimeFormat` `timeZoneName: 'longOffset'`).
- **Never store money as a float and never assume two decimal places.** ISO 4217 List One (published 2026-01-01, `six-group.com`) gives 0 minor units for JPY, KRW, ISK, CLP, VND, XAF, XOF, XPF and others, and 3 for KWD, BHD, OMR, JOD, TND, IQD, LYD. Store an integer in minor units plus the ISO 4217 code, and read the exponent from data.
- **Never mark postcode or state required by default.** Google's libaddressinput metadata gives Ireland (`IE`) no `require` string at all, and gives Hong Kong (`HK`) and the UAE (`AE`) no postcode field at all; Austria, Germany, the Netherlands and the UK have no administrative-area field. `require` is per country and is the only thing that decides this.
- **Never build a sentence by concatenating translated fragments, and never branch on `count === 1`.** CLDR defines up to six plural categories; verified via `Intl.PluralRules`, Arabic and Welsh use all of `zero`, `one`, `two`, `few`, `many`, `other`, Polish and Czech use `one`, `few`, `many`, `other`, and Japanese uses only `other`. One message per sentence, with the placeholder inside it.
- **Never strip a leading zero from a phone number and never store the trunk prefix.** In most of Europe the leading `0` is a national trunk prefix that is dropped in E.164, but it is not noise — it is the marker that tells the parser the number is in national format. Let libphonenumber decide; hand-stripping breaks Italy, where the fixed-line `0` is part of the number and survives after `+39`.
- **Never hard-code a decimal separator, a group separator or a currency symbol position.** Verified: `de-AT` formats a bare number with U+00A0 as group separator (`1 234 567,89`) but the same amount as currency with `.` (`€ 1.234.567,89`), while `de-DE` puts the symbol last (`1.234.567,89 €`) and `de-CH` groups with U+2019 RIGHT SINGLE QUOTATION MARK. Use `Intl.NumberFormat` and `formatToParts`.

## False friends

Each of these is plausible, is in a widely-copied tutorial or a US-authored library README, and is wrong.

| Plausible assumption | Actual position |
|---|---|
| "Everyone has a first name and a last name" (comes from US form conventions and from `given-name`/`family-name` autofill tokens) | Single-name people exist (Indonesian, Icelandic patronymic systems partly, many South Indian names), Spanish and Portuguese speakers carry two surnames, Hungarian and East Asian names put family name first. The HTML spec itself hedges: `family-name` is "in *some* Western cultures". |
| "`address-level1` means state" | The HTML Living Standard defines `address-level1` as "the broadest administrative level" — the US state, the Swiss canton, **the UK post town**. It is not a state field, and most European countries do not use it at all. |
| "A postcode is five digits" (US ZIP) | NL is `1234 AB`, CA is `A1A 1A1`, GB is `EC1Y 8SY` with a significant space, IE is `A65 F4E2`, PL is `00-950`, PT is `2725-079`, and HK and AE have none. |
| "The EU has one VAT number format" | Formats differ per Member State and Greece is `EL`, not `GR`, in VIES. Northern Ireland is `XI`. Verified live against the VIES REST API on 2026-08-05. |
| "VIES tells me the company name" | Verified live 2026-08-05: `IE6388047V` returned `GOOGLE IRELAND LIMITED` with an address; `DE811569869` returned `valid: true` with `name` and `address` both `"---"`. Germany deliberately returns no name. |
| "`new Date('2026-03-05')` is midnight local" | It is midnight **UTC**. `new Date('2026-03-05T00:00')` is midnight **local**. Verified in `Europe/Vienna`: the second parses to `2026-03-04T23:00:00.000Z`. A date-only string and a date-time string take different code paths in ECMA-262. |
| "A time zone is an offset" | `+01:00` describes one instant in one place. `Europe/Vienna` describes the rules. Storing the offset loses the ability to compute the next occurrence of a recurring 09:00 meeting across a DST boundary. |
| "German is German" | `de-AT` writes `Jänner` for January where `de-DE` and `de-CH` write `Januar` (verified via `Intl.DateTimeFormat`); Switzerland and Liechtenstein do not use `ß` at all, writing `ss`; the three locales use three different number formats. |
| "`citext` gives me case-insensitive columns" | The PostgreSQL 18 documentation states citext "is not truly case-insensitive in the terms defined by the Unicode standard" and recommends nondeterministic ICU collations instead. |
| "The EU ODR platform link belongs in the footer" | Out of scope here and dead anyway — see `legal-at` / `legal-eu`. Mentioned only so it is not reintroduced while editing a checkout flow. |

## Common mistakes

| Mistake | Why it is wrong |
|---|---|
| `VARCHAR(50)` on a name column | Counts bytes or UTF-16 units, not graphemes; a name in Devanagari or with combining marks is truncated mid-character |
| `email.toLowerCase()` before comparison | Locale-dependent (`tr` turns `I` into `ı`); the local part of an address is case-sensitive per RFC 5321 |
| `UNIQUE` index on a name or handle without a normalisation form | `é` as U+00E9 and as `e` + U+0301 are different byte sequences and both pass; verified `'é' === 'é'` is `false` |
| A separate `house_number` column | Germany and Austria put the number after the street, France and the UK before it, and numbers carry letters and additions (`12a`, `12/3`, `12 bis`) |
| `MM/DD/YYYY` anywhere | Ambiguous with `DD/MM/YYYY` for every day of the month below 13; use `Intl.DateTimeFormat` for display and ISO 8601 for storage and for anything machine-read |
| `parseFloat(userInput)` on a price | Returns `1` for the German input `1,50`; silently undercharges by a factor of 100 |
| Fixed-width buttons sized against English | German and French run materially longer than English; the string has to be allowed to wrap or the layout breaks in exactly the locale you cannot read |
| Sorting a dropdown of countries once, server-side | The correct order depends on the viewer's locale, not on the data |
| `week % 52` or `getDay() === 0` for "start of week" | ISO weeks start Monday with `minimalDays: 4`; verified `weekInfo` gives `firstDay: 7, minimalDays: 1` for `en-US` and `firstDay: 5` for `dv-MV` |
| Storing a phone number as entered plus a country column | Two sources of truth that drift; store one E.164 string and derive the display format |

## Reference files

Each carries its upstream version, the rule, working code and a `## Checkpoints` list.

- `references/intake.md` — questions to answer before any schema or validator is written
- `references/names.md` — the CLDR person name model, database shape, display ordering, casing, transliteration
- `references/addresses.md` — per-country field order, `fmt`/`require` data, postcode patterns, countries without postcodes
- `references/form-fields.md` — HTML autofill tokens, per-country form specification, input modes, labels
- `references/phone-numbers.md` — E.164 storage, libphonenumber parsing and formatting, trunk prefixes, type detection limits
- `references/identifiers.md` — IBAN mod-97, BIC, VAT formats and VIES, national company and tax identifiers with checksums
- `references/dates-and-times.md` — ISO 8601 storage, IANA zones, DST edge cases, week numbering, calendars, Temporal
- `references/numbers-and-currency.md` — separators, grouping systems, minor units, integer money, `Intl.NumberFormat`
- `references/collation-and-search.md` — `Intl.Collator`, per-language ordering, normalisation, Postgres collations, accent-insensitive search
- `references/text-handling.md` — graphemes vs code points vs bytes, length limits, truncation, bidi isolates, CJK line breaking
- `references/messages-and-plurals.md` — CLDR plural categories, MessageFormat 2.0, gender, text expansion
- `references/locale-negotiation.md` — BCP 47, `Accept-Language`, fallback chains, URL strategies, `de-AT`/`de-CH`/`de-DE`
- `references/test-data.md` — values that break naive implementations, with the expected correct behaviour
- `references/checklist.md` — pre-ship review producing a findings table
