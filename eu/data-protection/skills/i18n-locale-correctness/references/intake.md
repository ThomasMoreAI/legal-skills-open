# Intake

Answer before writing any schema, validator or formatter. Unanswered questions become `[[MISSING: …]]` in the artefact and in the report — never a plausible default. A guessed market list produces a validator that rejects real customers, and the rejection is silent.

## Markets and users

1. Which countries do you **ship to, bill in, or accept signups from** today? List ISO 3166-1 alpha-2 codes. "Europe" is not an answer — Ireland, Switzerland and Hungary each break a different assumption.
2. Which countries are on the twelve-month roadmap? Field shape is cheap to widen now and expensive to widen after launch.
3. Which **languages** does the interface offer, as BCP 47 tags? Distinguish `de` from `de-AT` and `de-CH` — see `locale-negotiation.md`.
4. Do users write in a **non-Latin script** (Cyrillic, Greek, Arabic, Hebrew, CJK, Devanagari)? Right-to-left languages (Arabic, Hebrew, Persian, Urdu) change layout, not just strings.
5. Is the audience **consumer, business, or both**? Business flows add VAT identification numbers, company registration numbers and invoice addresses that differ from delivery addresses.

## Existing data

6. What is already in the database? Column names, types and lengths for: name fields, address fields, postcode, phone, country, locale, currency, money amounts, timestamps.
7. Are money amounts stored as `float`, `decimal`, or integer minor units? Anything other than integer minor units is a defect to schedule — see `numbers-and-currency.md`.
8. Are timestamps stored as `timestamptz`, `timestamp`, epoch integer, or a string? Is there a separate IANA zone column for anything the user scheduled?
9. Is there a **mandatory** `last_name` / `family_name` column? Is it `NOT NULL`? How many rows currently hold a placeholder (`.`, `-`, `n/a`, a repeated first name)? That count is the size of the existing bug.
10. Are there `UNIQUE` indexes on user-typed text (handle, slug, company name, email)? Under which collation, and is any Unicode normalisation applied before insert?
11. Which columns are currently validated by a regex? List each regex verbatim. Phone and postcode regexes are the usual findings.

## Fields in scope

12. Which of these does the change touch: name, address, postcode, phone, email, date of birth, appointment time, price, tax identifier, bank details, free text, search?
13. For each: is it **displayed**, **searched**, **sorted**, **exported**, or **sent to a third party** (payment provider, carrier, tax authority)? Each of those imposes a different format constraint on the same value.
14. Is anything printed on a physical label or an invoice? Postal formatting rules apply, and they differ from screen formatting.

## Runtime and platform

15. Which runtimes render or compare these values — browser, Node, Deno, JVM, .NET, Python, Postgres, a mobile app?
16. Is **full ICU** available on every one of them? Node built with `small-icu` supports only English and silently formats everything as `en-US`. Check with `process.versions.icu` and `Intl.DateTimeFormat.supportedLocalesOf(['de-AT'])`. Docker slim images are the usual culprit.
17. Which database, which version, which server encoding and which default collation? For PostgreSQL, is the ICU provider available (`SELECT * FROM pg_collation WHERE collprovider = 'i'`)?
18. Is there a translation pipeline already (ICU MessageFormat, gettext, a TMS)? Which message format do the files use?
19. Does the frontend build ship CLDR data itself (`@formatjs/intl-*`, `full-icu`), or does it rely on the platform?

## Identifiers and money

20. Do you collect **IBAN**? For payout, direct debit, or display? Do you also collect BIC?
21. Do you collect a **VAT identification number**? Do you validate it against VIES at signup, at checkout, or never? Do you store the VIES consultation number as evidence?
22. Do you collect a national **company registration number** (Firmenbuchnummer, HRB, SIREN, Companies House number)? Is it displayed on an invoice?
23. Which **currencies** can an amount be denominated in? Is there ever more than one currency in a single total?
24. Are prices shown to consumers gross (tax-inclusive) or net? This decides rounding order, which decides whether totals reconcile.

## Time

25. Does anything **schedule** — appointments, reminders, recurring events, cutoffs, business hours, SLAs? If yes, the user's IANA zone must be stored, not the offset.
26. Do any of those recur across a DST boundary? A weekly 09:00 slot in `Europe/Vienna` is a different UTC instant in January and in July.
27. Does anything depend on a **week number** or a "start of week"? ISO and US week numbering disagree — see `dates-and-times.md`.
28. Is any date a **calendar date** without a time (birthday, invoice date, contract start)? Those must never be stored as an instant.

## Search and sorting

29. Which lists are sorted for a human to read? Which are sorted for a machine?
30. Is search expected to be **accent-insensitive** (`Muller` finds `Müller`), **case-insensitive**, or both? Is it expected to work in both directions?
31. Are there autocomplete or typeahead endpoints over user-typed text?

## Third parties that constrain the shape

32. Which downstream systems receive these values — payment provider, carrier, accounting system, CRM, tax authority, email service?
33. Does any of them impose a **narrower** shape than the correct one (an ASCII-only name field, a mandatory two-field split, a US-style state code, a fixed postcode length)? Name each constraint and which field it touches.
34. Where a downstream constraint conflicts with the correct shape, the correct shape wins in your database and the narrow shape is derived at the integration boundary. Confirm that is how it is built, or record it as a defect.

## Output of this intake

Produce a table before writing anything:

| Field | Markets | Displayed | Searched | Sorted | Exported to | Current type | Correct type |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

Anything without an answer is `[[MISSING: …]]`.

## Checkpoints

- [ ] Target market list is explicit ISO 3166-1 alpha-2 codes, not a region name
- [ ] Interface languages listed as BCP 47 tags, with region subtags where they matter
- [ ] Every existing regex on a user-typed field written out verbatim
- [ ] Count of placeholder values in any mandatory family-name column obtained
- [ ] Money storage type confirmed as integer minor units, or flagged as a defect
- [ ] Full ICU confirmed present on every runtime that formats or compares
- [ ] Database collation and provider recorded
- [ ] For every scheduling feature, confirmed whether an IANA zone is stored
- [ ] Field table produced with one row per field in scope
- [ ] Every unanswered question carried forward as `[[MISSING: …]]`
