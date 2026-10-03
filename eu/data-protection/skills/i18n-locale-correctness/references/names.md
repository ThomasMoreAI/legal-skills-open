# Personal names

Authoritative basis: UTS #35 Part 8 "Person Names" (LDML), version 48.2 (`unicode.org/reports/tr35/tr35-personNames.html`). Person name formatting entered CLDR as a tech preview in CLDR 42 and left tech preview in **CLDR 43, released 2023-04-12** (`cldr.unicode.org/downloads/cldr-43`: "Person Name Formatting was in Tech Preview … It has now advanced out of Tech Preview and can be used in production"). Status as at 2026-08-05.

**There is no `Intl.PersonName`.** Verified on Node 22 / ICU 77: `Object.getOwnPropertyNames(Intl)` returns `getCanonicalLocales, supportedValuesOf, DateTimeFormat, NumberFormat, Collator, PluralRules, RelativeTimeFormat, ListFormat, Locale, DisplayNames, Segmenter`. CLDR holds the data; to use it you need ICU4J, ICU4X, or a library that reads CLDR's `personNames` data directly. Until then, do the simple correct thing described below rather than a clever wrong thing.

## What actually varies

- **Number of names.** Single-name people are common (Indonesia, parts of South India, Myanmar, Afghanistan). A `NOT NULL` surname column forces them to type `.` or their given name twice, and then your mail merge greets them by a full stop.
- **Number of surnames.** Spanish naming carries two (paternal then maternal: *García Márquez*); Portuguese carries two in the other order (maternal then paternal: *Silva Santos*) and often more. Neither is a middle name. Truncating to one loses the one people are actually called by — and which one that is differs between Spain and Portugal.
- **Order.** Hungarian writes family name first natively (*Nagy Péter*). Chinese, Japanese, Korean and Vietnamese write family name first. Some of those users invert their names when writing in Latin script and some do not, and you cannot tell which from the string.
- **Patronymics.** Icelandic names are patronymic, not family names: *Jón Einarsson*'s daughter is *Anna Jónsdóttir*, and the Icelandic phone book sorts by given name. Russian, Ukrainian and Bulgarian carry a middle patronymic (*Ivanovich*, *Petrivna*) that is neither a given name nor a family name, and dropping it makes formal address impossible.
- **Particles.** Dutch *tussenvoegsels* (`van`, `de`, `van der`, `'t`), German `von`/`zu`, French `de`/`du`, Italian `di`/`della`, Portuguese `dos`/`da`. In the Netherlands the particle is **excluded** from alphabetical sorting (*Vincent van Gogh* files under G) but **included** when the surname stands alone at the start of a sentence, and it is capitalised in that position (`Van Gogh`) and lowercased after a given name (`van Gogh`). CLDR models this with the `-prefix` and `-core` modifiers on `surname`.
- **Casing.** `toUpperCase()` is not a name transformation. `'ß'.toUpperCase()` is `"SS"` — verified, and it changes the string length. `'ı'.toUpperCase()` is `"I"`, losing the Turkish dotless i. `McDonald`, `van der Berg`, `O'Brien`, `d'Alembert` and `LaFontaine` each defeat naive title-casing.
- **Script.** A user may hold a name in a native script and a transliteration, and both are correct. Store both if you need both; never overwrite one with the other.

## Database shape

```sql
-- required, exactly as the user typed it
full_name            text        not null,

-- optional hints, only if you have a real use for them; never NOT NULL
given_name           text,
family_name          text,

-- optional, for correspondence; do not derive it, ask for it
preferred_name       text,

-- optional, only where a form of address is genuinely needed
salutation           text,

-- the script/locale the name was entered in, for correct display and collation
name_locale          text,       -- BCP 47, e.g. 'hu-HU', 'ja-JP'

-- optional second representation; never a replacement for full_name
full_name_latin      text
```

Rules that follow from this shape:

- `full_name` is the only mandatory field. Everything else is nullable and stays nullable.
- Never reconstruct `full_name` by concatenating `given_name` and `family_name`. The user gave you the whole string; store the whole string.
- Never index or deduplicate on `family_name`. Use `full_name` under a nondeterministic collation — see `collation-and-search.md`.
- If you must have separate fields (a carrier API, a payment scheme, a boarding pass), collect them **in addition to** `full_name`, label them by what the downstream system means, and let them be blank.
- Do not add a `middle_name` column. The HTML autofill token is `additional-name` and the spec itself says "in some Western cultures, also known as middle names".

## Form fields

One field, labelled *Name* (or *Full name*), `autocomplete="name"`, no `pattern`, no length limit below 100 characters, and no client-side rejection of spaces, apostrophes, hyphens or non-ASCII letters.

```html
<label for="name">Name</label>
<input id="name" name="name" type="text" autocomplete="name"
       maxlength="200" autocapitalize="words" spellcheck="false" required>
```

If a second field is genuinely needed downstream, add it below and mark it optional:

```html
<label for="pref">What should we call you? <span>(optional)</span></label>
<input id="pref" name="preferred_name" type="text" autocomplete="nickname" maxlength="100">
```

Do not use `autocomplete="given-name"` / `"family-name"` unless you are actually storing both; a browser filling a single `name` field from `given-name` produces half a name.

## Display ordering

The order in which you show a name depends on the **display context**, not on the name's origin. CLDR's `personName` patterns take four parameters (UTS #35 Part 8):

| Parameter | Values | Use |
|---|---|---|
| `order` | `givenFirst`, `surnameFirst`, `sorting` | `sorting` is the form used in an alphabetised list |
| `length` | `long`, `medium`, `short` | how many fields to include |
| `usage` | `addressing`, `referring`, `monogram` | speaking to the person vs about them vs an avatar |
| `formality` | `formal`, `informal` | title and full surname vs preferred name |

CLDR name fields: `title`, `given`, `given2`, `surname`, `surname2`, `generation`, `credentials`, with modifiers `-informal`, `-prefix`, `-core`, `-allCaps`, `-initialCap`, `-initial`, `-monogram`, `-retain`, `-genitive`, `-vocative`.

Without an ICU binding, the honest implementation:

```js
// Display: never reorder. Show what the user typed.
const display = user.full_name;

// Sorting: use a collator on the whole string, and say so in the UI header
// ("sorted by name"), rather than claiming "sorted by surname" you cannot deliver.
rows.sort(new Intl.Collator(uiLocale, { sensitivity: 'base' })
            .compare.bind(null));

// Monogram / avatar: take grapheme clusters, not code units.
function initials(fullName, locale = 'en') {
  const seg = new Intl.Segmenter(locale, { granularity: 'grapheme' });
  return fullName
    .split(/\s+/)
    .filter(Boolean)
    .filter(w => !/^(van|von|der|den|de|du|di|della|dos|da|del|la|le|of|bin|binti|ibn|al)$/i.test(w))
    .slice(0, 2)
    .map(w => [...seg.segment(w)][0].segment)
    .join('');
}
// initials('Vincent van Gogh')  -> 'VG'
// initials('María García Márquez') -> 'MG'
// initials('நிர்மலா')            -> 'நி'   (one grapheme, two code units)
```

Verified: `'நி'.length === 2` but `[...new Intl.Segmenter('en',{granularity:'grapheme'}).segment('நி')].length === 1`. Slicing by `.length` splits the character.

## Casing and comparison

```js
// WRONG — locale-dependent, and it mangles ß and Turkish i
if (a.toLowerCase() === b.toLowerCase()) { /* ... */ }

// RIGHT — case- and accent-insensitive comparison without mutating the string
const loose = new Intl.Collator(undefined, { sensitivity: 'base' });
if (loose.compare(a, b) === 0) { /* ... */ }
```

Verified failures of the wrong version: `'TITLE'.toLocaleLowerCase('tr')` is `"tıtle"`; `'istanbul'.toLocaleUpperCase('tr')` is `"İSTANBUL"`; `'ß'.toUpperCase()` is `"SS"`; `'ﬁ'.toUpperCase()` is `"FI"` (one code point becomes two).

Before storing a name for uniqueness or comparison, normalise to NFC — see `collation-and-search.md`. Verified: `'é' === 'é'` is `false` when one is U+00E9 and the other is `e` + U+0301, but both `.normalize('NFC')` to the same string.

## Transliteration

Transliteration is lossy and directional. `Müller` → `Mueller` is correct German practice; `Müller` → `Muller` is correct ICAO machine-readable-zone practice; the two are not interchangeable, and neither round-trips. If a downstream system (an airline, a payment scheme, a government form) requires ASCII, generate the ASCII form for that system only, store it in its own column, and never show it back to the user as their name.

## Checkpoints

- [ ] `full_name` exists, is the only required name column, and holds the string as typed
- [ ] No `NOT NULL` on any surname or family-name column
- [ ] No `middle_name` column; if a second given name is needed it is `additional-name`
- [ ] Existing placeholder rows in a mandatory surname column counted and reported
- [ ] Form uses one field with `autocomplete="name"`, no `pattern`, no ASCII restriction
- [ ] Maximum length is at least 100 characters and counts graphemes, not bytes
- [ ] No `toUpperCase()` / `toLowerCase()` applied to a name anywhere in the codebase
- [ ] Name comparison uses `Intl.Collator` with an explicit `sensitivity`, not case folding
- [ ] Names normalised to NFC before any uniqueness check
- [ ] Initials/monogram code uses `Intl.Segmenter` and skips particles
- [ ] Sorted lists use a collator for the viewer's locale, and the UI does not claim surname ordering it cannot deliver
- [ ] Any ASCII transliteration lives in its own column and is never displayed as the user's name
