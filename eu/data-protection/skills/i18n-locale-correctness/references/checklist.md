# Pre-ship checklist

Run before a product reaches its second country, and before any change that touches a field in the decision matrix. Every finding is reported with the file, the line and the rule it breaks — not as general advice. Findings that are mechanically detectable are detected mechanically, not judged by reading.

## Mechanical sweep first

These six greps produce most findings in a few minutes. Run them over the whole repository including tests, seed data, email templates, PDF generators and export jobs.

```bash
# 1. Case folding without a locale
rg -n "\.toLowerCase\(\)|\.toUpperCase\(\)" --glob '!**/node_modules/**'

# 2. Unlocalised sorting and comparison
rg -n "\.sort\(\s*\)|localeCompare\([^,)]*\)" --glob '!**/node_modules/**'

# 3. Hand-rolled validation of things that must not be regex-validated
rg -n "phone.*(RegExp|test\(|pattern)|\\\\d\{5\}|\\\\d\{10\}|zip.*RegExp" -i

# 4. Float money and naive parsing
rg -n "parseFloat|Number\(.*(price|amount|total)|float|double|REAL" -i

# 5. Hard-coded formats and separators
rg -n "MM/DD|DD/MM|YYYY-MM-DD'|toFixed\(2\)|/100|'\\\\\.'|replace\(/,/g"

# 6. US-shaped schema and copy
rg -n "\bstate\b|\bzip\b|first_?name|last_?name|middle_?name" -i
```

Each hit is a finding until proved otherwise.

## Names

- [ ] `full_name` exists and is the only mandatory name field
- [ ] No `NOT NULL` on any surname column; existing placeholder rows counted
- [ ] Form uses one `autocomplete="name"` input with no `pattern` and no ASCII restriction
- [ ] No case transformation applied to a name anywhere
- [ ] Name comparison uses `Intl.Collator`, not case folding
- [ ] Initials and avatars use `Intl.Segmenter`, not `charAt(0)`
- [ ] Names normalised to NFC before storage and before any uniqueness check

## Addresses

- [ ] Country is the first field and drives the rest of the form
- [ ] Field set, order, labels and requiredness come from per-country data
- [ ] Postcode column is `text`; postcode field is hidden where the country has none
- [ ] Ireland is not required to supply a postcode
- [ ] Administrative-area field hidden for AT, DE, CH, NL, GB, FR, BE, PL, CZ, Nordics
- [ ] No `house_number` column; street is free-text lines
- [ ] Postcodes normalised on input, not rejected on formatting
- [ ] Country stored as ISO 3166-1 alpha-2
- [ ] Postal rendering collapses empty lines
- [ ] Address metadata snapshot dated and scheduled for regeneration

## Phone numbers

- [ ] No phone regex anywhere
- [ ] One E.164 `text` column; no formatted or national copy
- [ ] Parsing uses libphonenumber `/max` metadata
- [ ] `defaultCountry` derived explicitly and documented
- [ ] Italian landline round-trips with its leading zero
- [ ] SMS not gated on `getType()`
- [ ] Single `type="tel"` field, no country dropdown
- [ ] libphonenumber version pinned and on an update schedule

## Identifiers

- [ ] IBAN validated with mod-97 **and** the per-country length table, in a column of ≥ 34 characters
- [ ] BIC not mandatory for SEPA
- [ ] VAT numbers checked against VIES, not a regex
- [ ] Greece sent as `EL`, Northern Ireland as `XI`
- [ ] Missing `name`/`address` in a VIES response not treated as failure
- [ ] `valid: null` plus an error wrapper treated as retry, not invalid
- [ ] VIES outage falls back to a cached result rather than blocking checkout
- [ ] Consultation evidence (`requestDate`, identifier) stored
- [ ] No IBAN or tax number in application logs
- [ ] No checksum pass presented to the user as "verified"

## Dates and times

- [ ] Instants, calendar dates and future local events in three different column types
- [ ] Every scheduled event stores an IANA zone id, never an offset
- [ ] Non-existent and ambiguous local times handled with a documented rule
- [ ] Recurring jobs idempotent across both DST transitions
- [ ] No `new Date(string)` except on a full ISO instant with an offset
- [ ] First day of week and weekend from `Intl.Locale#weekInfo`
- [ ] Dates formatted in a single `Intl.DateTimeFormat` call, never assembled
- [ ] `de-AT` renders `Jänner`; no shared German month-name array
- [ ] No `Etc/GMT±n` in any picker
- [ ] Half-hour and quarter-hour offsets tested
- [ ] tzdata version recorded per runtime and on an update schedule

## Numbers and currency

- [ ] Money stored as integer minor units plus an ISO 4217 code
- [ ] No float column holds an amount
- [ ] Minor-unit exponent read from data, never assumed to be 2
- [ ] No arithmetic across currencies
- [ ] All display through `Intl.NumberFormat`; no hard-coded separators or symbols
- [ ] `parseFloat` absent from any path reading a typed amount
- [ ] Input parser handles U+00A0, U+202F, U+2019, U+2212
- [ ] Amount inputs are `type="text"` with `inputmode="decimal"`
- [ ] A JPY and a KWD price tested end to end including the invoice PDF

## Collation and search

- [ ] No bare `.sort()` on user-visible strings; collator constructed once per sort
- [ ] Collator uses the viewer's locale
- [ ] `resolvedOptions().collation` checked wherever `-u-co-` is used
- [ ] Swedish and Danish ordering tested
- [ ] Phonebook collation used for German name indexes
- [ ] Uniqueness indexes on normalised columns or nondeterministic collations
- [ ] `citext` not in use
- [ ] PostgreSQL collation provider is `icu`; collation version recorded
- [ ] `LIKE`/regex paths kept off nondeterministic-collation columns

## Text

- [ ] User-facing length limits counted in grapheme clusters
- [ ] No `slice`/`substring` used to truncate visible text
- [ ] Word counts and excerpts use `Intl.Segmenter`, not `split(' ')`
- [ ] `<html lang>` correct; per-element `lang` on embedded other-language content
- [ ] `dir="rtl"` and `<bdi>` or `dir="auto"` around interpolated user values
- [ ] Plain-text interpolations wrapped in U+2068 / U+2069
- [ ] CSS uses logical properties; no bare `left`/`right` in layout
- [ ] `line-break`/`word-break` set per language; no global `word-break: break-all`

## Messages

- [ ] No `count === 1 ? a : b`
- [ ] No sentence assembled from concatenated fragments
- [ ] Every message key semantic and carrying a translator description
- [ ] Gendered messages have a usable neutral catch-all; gender never inferred
- [ ] Numbers, dates and currency formatted before entering a message
- [ ] No HTML fragments passed through the translation layer
- [ ] No fixed widths on controls carrying translated text; no text inside images
- [ ] Pseudo-localisation runs in CI

## Locale negotiation

- [ ] All identifiers canonical BCP 47; no underscores
- [ ] Content locale and formatting locale kept separate
- [ ] `Accept-Language` parsed with `q` ordering; explicit user choice wins and persists
- [ ] No IP geolocation used to choose a language
- [ ] Bundle fallback tested with deliberately missing keys
- [ ] `zh` not used alone where Traditional Chinese is a market; `pt` not used alone meaning Portugal
- [ ] `de-CH` is a separate bundle with `ss`; `de-AT` reviewed by an Austrian speaker
- [ ] Locale in the URL path using the canonical tag; `hreflang` and `x-default` emitted
- [ ] No automatic redirect on `Accept-Language` or IP; `Vary: Accept-Language` set

## Platform

- [ ] Full ICU present on every runtime (`process.versions.icu`, `Intl.DateTimeFormat.supportedLocalesOf(['de-AT'])`)
- [ ] Database, browser, server and OS tzdata versions recorded and not silently divergent
- [ ] CLDR/ICU version recorded; formatting snapshots in tests are version-tagged so an ICU upgrade fails loudly rather than silently changing output

## Test data

- [ ] Every value in `test-data.md` exercised through the real form, the real export and the real PDF
- [ ] Snapshot tests do not lock in `en-US` output as the expected value

## Findings format

Report as a table, most severe first:

| Severity | Location | Rule | Finding | Fix |
|---|---|---|---|---|
| critical / high / medium | file:line or URL | the rule from this skill | what is wrong | the concrete change |

**Critical** means a real user in a target market cannot complete a core flow, or money or time is stored wrongly: a `NOT NULL` surname column, a phone or postcode regex that rejects a valid value, float money, a scheduled event without a zone, an integer postcode column, or a name column that truncates mid-grapheme. Everything else is high or medium.

Close the report with the data-freshness note: which CLDR, ICU, tzdata, IBAN Registry and libphonenumber versions the findings were produced against, and the date.
