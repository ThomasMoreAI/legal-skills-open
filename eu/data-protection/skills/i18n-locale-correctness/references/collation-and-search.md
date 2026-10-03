# Collation, casing and search

Authoritative basis: the Unicode Collation Algorithm (UTS #10) via CLDR 48.2 and ECMA-402 `Intl.Collator`; the Unicode Standard 17.0.0 (2025-09-09) for normalisation; PostgreSQL 18.4 documentation (`postgresql.org/docs/current/collation.html`, `.../citext.html`). All behaviour verified on Node 22.19.0 / ICU 77.1, 2026-08-05.

## `Array.prototype.sort()` is wrong for anything a human reads

It compares UTF-16 code units. Verified:

```js
['Zürich','Zug','Äpfel','Apfel','Öl','Ost','Bär'].sort()
// ['Apfel','Bär','Ost','Zug','Zürich','Äpfel','Öl']   ← accented words dumped after Z

[...].sort(new Intl.Collator('de').compare)
// ['Apfel','Äpfel','Bär','Öl','Ost','Zug','Zürich']   ← correct
```

Every accented character sits above U+007A in code-unit order, so every accented word sorts after every unaccented one. The bug is invisible in an English test fixture and obvious to the first German user.

## The same letters sort differently per language

Verified with the same input list:

| Input | `Intl.Collator('de')` | `Intl.Collator('sv')` |
|---|---|---|
| `Ängel, Zebra, Ost, Öl, Åke, Apa` | `Åke, Ängel, Apa, Öl, Ost, Zebra` | `Apa, Ost, Zebra, Åke, Ängel, Öl` |

German treats `Ä` and `Ö` as variants of `A` and `O`. **Swedish treats `Å`, `Ä`, `Ö` as three distinct letters that come after `Z`.** Sorting a Swedish customer list with a German collator puts every `Öberg` in the wrong place.

Danish is stranger still. Verified `Intl.Collator('da')` on `Aalborg, Zoo, Æble, Øst, Århus, Bo`:

```
Bo, Zoo, Æble, Øst, Aalborg, Århus
```

`Aa` is collated as `Å`, so `Aalborg` sorts **after** `Øst`, at the very end of the alphabet. No amount of `localeCompare` without a locale argument produces this.

## German phonebook versus dictionary ordering

Two standard German collations disagree, and both are correct in their context. Verified on `Müller, Mueller, Muller, Mulder`:

| Collation | Result |
|---|---|
| `de-DE` (default, dictionary) | `Mueller, Mulder, Muller, Müller` |
| `de-DE-u-co-phonebk` (phonebook) | `Mueller, Müller, Mulder, Muller` |

Dictionary order treats `ü` as `u` with a secondary difference, so `Müller` files near `Muller`. Phonebook order treats `ü` as `ue`, so `Müller` files with `Mueller` — which is what a person looking up a name in an index expects. Use `phonebk` for name indexes and address books; use the default elsewhere.

```js
new Intl.Collator('de-DE-u-co-phonebk').resolvedOptions().collation  // 'phonebk'
```

**Not every `-u-co-` value is honoured.** `Intl.supportedValuesOf('collation')` on ICU 77 returns exactly `compat, dict, emoji, eor, phonebk, phonetic, pinyin, searchjl, stroke, trad, unihan, zhuyin`. Verified silently ignored (resolving to `default`): `de-u-co-search`, `de-u-co-standard`, `zh-u-co-pinyin` (pinyin is already the `zh` default), `sv-u-co-standard`. Honoured: `de-DE-u-co-phonebk` → `phonebk`, `zh-u-co-stroke` → `stroke`, `es-u-co-trad` → `trad`. **`search` and `standard` are explicitly not requestable through the extension** — always check `resolvedOptions().collation` rather than assuming your tag took effect.

## Collator options that matter

```js
new Intl.Collator(locale, {
  sensitivity: 'base',   // 'base' | 'accent' | 'case' | 'variant' (default)
  numeric: true,         // 'file9' before 'file10'
  caseFirst: 'false',    // 'upper' | 'lower' | 'false'
  ignorePunctuation: false,
})
```

Verified behaviour:

| Option | Effect |
|---|---|
| `sensitivity: 'base'` | `compare('resume','résumé') === 0` and `compare('a','A') === 0` — accent- **and** case-insensitive |
| `sensitivity: 'accent'` | `compare('resume','résumé') === -1`, case still ignored |
| `numeric: true` | `['file10','file9','file1']` → `['file1','file9','file10']`; without it, `['file1','file10','file9']` |
| `caseFirst: 'upper'` (de) | `['a','A','b','B']` → `['A','a','B','b']` |

Construct the collator **once** and reuse it. Constructing one per comparison inside a sort makes an O(n log n) sort O(n log n) collator constructions, which is the usual cause of "sorting is slow with Intl".

```js
const collator = new Intl.Collator(uiLocale, { sensitivity: 'base', numeric: true });
rows.sort((a, b) => collator.compare(a.name, b.name));
```

`String.prototype.localeCompare(b, locales, options)` takes the same options and is fine for a one-off comparison; it is the wrong tool inside a sort for the same performance reason.

## Casing is a trap, not a normalisation

Verified:

| Expression | Result | Consequence |
|---|---|---|
| `'I'.toLocaleLowerCase('tr')` | `'ı'` (U+0131 DOTLESS I) | a Turkish-locale lowercase breaks every ASCII equality check |
| `'i'.toLocaleUpperCase('tr')` | `'İ'` (U+0130 I WITH DOT ABOVE) | |
| `'TITLE'.toLocaleLowerCase('tr')` | `'tıtle'` | `'TITLE'.toLowerCase() === 'title'` is `true`, the Turkish form is not |
| `'istanbul'.toLocaleUpperCase('tr')` | `'İSTANBUL'` | correct Turkish, wrong for an ASCII comparison |
| `'ß'.toUpperCase()` | `'SS'` | length 1 → 2; a `VARCHAR` can overflow on uppercase |
| `'ẞ'.toLowerCase()` | `'ß'` | U+1E9E round-trips, U+00DF does not |
| `'ﬁ'.toUpperCase()` | `'FI'` | ligature expands |

The classic production bug: a config key or a CSS class is lowercased with the OS locale set to Turkish, `"TITLE"` becomes `"tıtle"`, and a lookup fails on a machine you cannot reproduce. **Never call `toLowerCase()`/`toUpperCase()` without an explicit locale, and prefer not calling them at all** — use `Intl.Collator` with `sensitivity: 'base'` for comparison and leave the string alone.

Where you genuinely need a canonical form for a machine key, use `toLocaleLowerCase('und')` or, better, keep the original and compare with a collator.

Swiss and Liechtenstein German has no `ß` at all — `ss` is written in every position. That is an orthography difference, not a casing one; see `locale-negotiation.md`.

## Normalisation

Verified: `'é'` as U+00E9 and `'é'` as `e` + U+0301 are **not** `===`, have `.length` 1 and 2, and are equal after `.normalize('NFC')`.

Rules:

- **Normalise to NFC on input**, before storing, before hashing, before any uniqueness check. NFC is the form the web expects; the W3C's character-model guidance and CLDR both treat it as the default.
- Do **not** apply NFKC or NFKD to user content. They are compatibility forms and are lossy: verified, `'ﬁ'.normalize('NFKC')` is `'fi'`, `'①'.normalize('NFKC')` is `'1'`, `'ｱ'.normalize('NFKC')` is `'ア'`. Useful for building a search key, destructive for storing a name.
- macOS filesystems hand you NFD; most other sources hand you NFC. A file uploaded from a Mac and one uploaded from Windows can have byte-different names for the same visible string.

```js
const canonical = input.normalize('NFC');            // store this
const searchKey = input.normalize('NFKD')            // derive this, separately
  .replace(/\p{Diacritic}/gu, '')
  .toLocaleLowerCase('und');
```

## Accent-insensitive search

Two implementations, depending on where the search runs.

**In application code**, use a collator:

```js
const loose = new Intl.Collator(locale, { sensitivity: 'base' });
const matches = rows.filter(r => loose.compare(r.name, query) === 0);
```

That works for equality. For prefix or substring matching, `Intl.Collator` gives you no `startsWith`, so build a folded search column instead (the `searchKey` above) and index that. Keep the original for display; never show the folded form.

**In PostgreSQL 18**, use a nondeterministic ICU collation rather than `lower()` or `unaccent()`:

```sql
CREATE COLLATION case_insensitive
  (provider = icu, locale = 'und-u-ks-level2', deterministic = false);

CREATE COLLATION ignore_accent_case
  (provider = icu, locale = 'und-u-ks-level1', deterministic = false);

CREATE TABLE customer (
  id    bigserial primary key,
  name  text COLLATE ignore_accent_case not null
);
```

ICU collation attributes in the locale string: `ks` (strength, `level1`–`identic`, default `level3`), `ka` (`noignore` | `shifted`, for punctuation), `kf` (`upper` | `lower` | `false`, case ordering), `kn` (`true` | `false`, numeric).

Documented restrictions of nondeterministic collations (PostgreSQL 18.4): a performance penalty; B-tree deduplication is unavailable; "some pattern matching operations are not possible" — `LIKE` and regex operators do not work against a nondeterministic collation, so keep a separate deterministic column or an expression index for those.

**Do not reach for `citext`.** The PostgreSQL 18 documentation says so itself: "Consider using nondeterministic collations … instead of this module. They can be used for case-insensitive comparisons, accent-insensitive comparisons, and other combinations, and they handle more Unicode special cases correctly." Its stated defects: case folding "depends on the LC_CTYPE setting of your database … It is not truly case-insensitive in the terms defined by the Unicode standard"; it copies and lower-cases on every comparison; and "the approach of lower-casing strings for comparison does not handle some Unicode special cases correctly, for example when one upper-case letter has two lower-case letter equivalents".

Also: the database's default collation is fixed at database creation and a libc collation can change its ordering under you on a glibc upgrade, silently corrupting B-tree indexes. Prefer the ICU provider and record the collation version.

## Sorting a country or language dropdown

The order depends on the viewer, not the data:

```js
const dn = new Intl.DisplayNames([uiLocale], { type: 'region' });
const collator = new Intl.Collator(uiLocale);
const options = codes
  .map(code => ({ code, label: dn.of(code) }))
  .sort((a, b) => collator.compare(a.label, b.label));
```

Verified: `new Intl.DisplayNames(['de'], {type:'region'}).of('AT')` is `'Österreich'`, which a German collator files under O and a Swedish one after Z.

## Checkpoints

- [ ] No `Array.prototype.sort()` without a comparator on user-visible strings
- [ ] Collator constructed once per sort, not once per comparison
- [ ] Collator locale is the **viewer's** locale, not the data's
- [ ] `resolvedOptions().collation` checked wherever a `-u-co-` tag is used
- [ ] Name indexes and address books use `de-*-u-co-phonebk` where German is a market
- [ ] Swedish and Danish sorting tested with `Å`, `Ä`, `Ö`, `Æ`, `Ø` and a name beginning `Aa`
- [ ] No `toLowerCase()` / `toUpperCase()` without an explicit locale anywhere in the codebase
- [ ] No case folding used as a comparison mechanism; collators used instead
- [ ] All user text normalised to NFC before storage and before any uniqueness check
- [ ] NFKC/NFKD used only to derive a search key, never to store content
- [ ] Uniqueness indexes on user text sit on a normalised column or a nondeterministic collation
- [ ] `citext` not used; nondeterministic ICU collations used instead
- [ ] PostgreSQL collation provider is `icu` and the collation version is recorded
- [ ] `LIKE`/regex paths kept off nondeterministic-collation columns
- [ ] Country and language dropdowns sorted per viewer locale, not stored pre-sorted
