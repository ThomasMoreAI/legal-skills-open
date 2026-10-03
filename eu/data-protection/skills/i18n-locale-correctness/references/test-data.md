# Test data that breaks naive implementations

Every value here was executed on Node 22.19.0 / ICU 77.1 on 2026-08-05 and every "wrong" column is the actual observed output of the naive implementation. Run the whole set through any form, validator, formatter, export and PDF before shipping. A field that has not been tested against these has not been reviewed.

## Names

| Value | Breaks | Correct behaviour |
|---|---|---|
| `Sukarno` | a `NOT NULL` family-name column | accepted as a complete name in `full_name` |
| `Gabriel García Márquez` | truncation to one surname, and initials-by-last-word | both surnames kept; initials `GG` |
| `Vincent van Gogh` | initials `VV`; alphabetisation under V | initials `VG`; Dutch index files under G |
| `Nagy Péter` | assuming the last token is the family name | stored whole; not reordered for display |
| `Anna Jónsdóttir` | assuming a shared family name across a household | patronymic; Icelandic indexes sort by given name |
| `İrem Yıldız` | `toLowerCase()` on a name | stored and compared as typed |
| `Jean-Luc O'Brien-Müller` | a `pattern="[A-Za-z ]+"` | accepted |
| `நிர்மலா` | `slice(0, 3)` for initials — splits a grapheme | `Intl.Segmenter` gives 1 cluster for `நி` |
| `👤 Test` | a `VARCHAR(n)` sized in bytes | length counted in graphemes |
| `Maria Weiß` | `toUpperCase()` — becomes `WEISS`, length 5 → 6 | no case transformation applied |

## Casing

| Input | Naive output | Why it is wrong |
|---|---|---|
| `'TITLE'.toLocaleLowerCase('tr')` | `'tıtle'` | not equal to `'title'`; breaks key lookups on Turkish-locale machines |
| `'istanbul'.toLocaleUpperCase('tr')` | `'İSTANBUL'` | correct Turkish, but not `'ISTANBUL'` |
| `'ß'.toUpperCase()` | `'SS'` | length 1 → 2, overflows a tight column |
| `'ﬁ'.toUpperCase()` | `'FI'` | ligature expands |
| `'ı'.toUpperCase()` | `'I'` | dotless i is lost and does not round-trip |

## Sorting

| Input list | `Array.sort()` (wrong) | Correct collator |
|---|---|---|
| `Zürich, Zug, Äpfel, Apfel, Öl, Ost, Bär` | `Apfel, Bär, Ost, Zug, Zürich, Äpfel, Öl` | `de`: `Apfel, Äpfel, Bär, Öl, Ost, Zug, Zürich` |
| `Ängel, Zebra, Ost, Öl, Åke, Apa` | — | `sv`: `Apa, Ost, Zebra, Åke, Ängel, Öl` |
| `Aalborg, Zoo, Æble, Øst, Århus, Bo` | — | `da`: `Bo, Zoo, Æble, Øst, Aalborg, Århus` |
| `Müller, Mueller, Muller, Mulder` | — | `de-DE`: `Mueller, Mulder, Muller, Müller`; `de-DE-u-co-phonebk`: `Mueller, Müller, Mulder, Muller` |
| `file10, file9, file1` | `file1, file10, file9` | `{numeric:true}`: `file1, file9, file10` |

## Normalisation

| Input | Naive result | Correct |
|---|---|---|
| `'é'` (U+00E9) vs `'é'` (`e` + U+0301) | `===` is `false`; lengths 1 and 2 | equal after `.normalize('NFC')` |
| A filename uploaded from macOS | NFD; does not match the NFC copy in the database | normalise on ingest |
| `'ﬁle'.normalize('NFKC')` | `'file'` | fine for a search key, destructive as storage |

## Addresses

| Value | Breaks | Correct behaviour |
|---|---|---|
| Irish address with no Eircode and no street number | a required-postcode form | accepted; `IE` has no `require` fields |
| `A65 F4E2` | `^\d{5}$` and `type="number"` | accepted as text |
| `0025` (Norway) | an integer postcode column | leading zero preserved |
| `1234 AB` (NL) | `inputmode="numeric"` | letters typeable |
| `EC1Y 8SY` without the space | rejection | normalised to `EC1Y 8SY` |
| `H3Z 2Y7` (Canada) | a numeric pattern | accepted |
| Hong Kong address | a required postcode field | postcode field not rendered |
| UAE address | a required city field | emirate rendered instead |
| `Hauptstraße 12/3, 1010 Wien` | a parsed `house_number` column | free-text address line |
| `12 bis rue de la Paix` | `^\d+$` on a house number | free-text address line |
| Hungarian address | street-then-city order | city above street |
| Japanese address | name-first layout | `〒` postcode first, name last |

## Phone numbers

| Value | Breaks | Correct behaviour |
|---|---|---|
| `+43 664 1234567` | `^\d{10}$` | parses to `+436641234567` |
| `0664 1234567` with `defaultCountry: 'AT'` | a parser that strips the leading zero blindly | same E.164 result |
| `+39 06 12345678` (Rome landline) | "drop the zero after the country code" | zero **retained**: `+390612345678` |
| `+1 415 555 2671` | `getType()` treated as a mobile gate | returns `FIXED_LINE_OR_MOBILE`; SMS still offered |
| `+44 20 7946 0958` | a fixed-length assumption | parses |
| `(0) 664 123 4567` | client-side stripping of brackets before parsing | passed to the parser as typed |

## Identifiers

| Value | Expected |
|---|---|
| `AT61 1904 3002 3457 3201` | valid IBAN (20 chars, mod-97 = 1) |
| `MT84MALT011000012345MTLCAST001S` | valid, 31 characters — a `VARCHAR(22)` column truncates it |
| `NO9386011117947` | valid, 15 characters — the shortest |
| `DE89370400440532013001` | invalid (last digit mutated) |
| `IE6388047V` via VIES | `valid: true`, `name: "GOOGLE IRELAND LIMITED"` |
| `DE811569869` via VIES | `valid: true`, `name: "---"` — **not** a failure |
| `GR` sent as the VIES country code | rejected; must be `EL` |
| A VIES burst | `{"errorWrappers":[{"error":"MS_MAX_CONCURRENT_REQ"}]}`, `valid: null` — retry, not invalid |
| `51 824 753 556` | valid ABN (mod-89) |
| `CHE-116.281.710` | valid Swiss UID (mod-11) |

## Numbers and currency

| Value | Naive result | Correct |
|---|---|---|
| `parseFloat('1.234,50')` | `1.234` | `1234.50` via a locale-aware parser |
| `parseFloat('1,50')` | `1` | `1.50` |
| `'1’234.50'` (de-CH) | `NaN` after stripping `'` (U+0027) | the separator is U+2019 |
| `'1 234,50'` (fr-FR) | fails a `\s` strip in non-Unicode mode | separator is U+202F |
| `'−1234'` (sv-SE output) | `Number('−1234')` is `NaN` | minus is U+2212, not U+002D |
| JPY `1235` | `amount / 100` → `12.35` | 0 minor units; `1235` |
| KWD `1234500` | `amount / 100` → `12345.00` | 3 minor units; `1234.500` |
| ISK `1235` | two decimals shown | `1.235 kr.` |
| `1234` in `pl-PL` | `1.234` | `1234` — `minimumGroupingDigits` is 2 |
| `12345678.9` in `en-IN` | `12,345,678.9` | `1,23,45,678.9` |
| `0.075` as a percent in `de-AT` | `7,5%` | `7,5 %` — with a space |

## Dates and times

| Value | Naive result | Correct |
|---|---|---|
| `new Date('2026-03-05T00:00')` in `Europe/Vienna` | `.toISOString()` is `2026-03-04T23:00:00.000Z` — the previous day | a date-time string without an offset is parsed as **local**, a date-only string as **UTC**; calendar dates never round-trip through `Date` |
| `2026-03-29T02:30` in `Europe/Vienna` | silently shifted | **does not exist**; must be rejected or explicitly resolved |
| `2026-10-25T02:30` in `Europe/Vienna` | one of two instants, chosen arbitrarily | **ambiguous**; occurs at +02:00 and at +01:00 |
| `Etc/GMT+1` | assumed to be UTC+01:00 | it is **UTC−01:00** |
| `Asia/Kathmandu` | integer-hour offset assumption | +05:45 |
| `Pacific/Chatham` | as above | +12:45 |
| `2026-01-15` in `de-AT` | `15. Januar 2026` | `15. Jänner 2026` |
| `2026-01-15` in `ru`, day + month | `15 январь` from a month array | `15 января` — genitive |
| `2026-01-15` in `th-TH` | year `2026` | `15 มกราคม 2569` — Buddhist era |
| `weekInfo` for `en-US` | Monday-first calendar | `firstDay: 7`, `minimalDays: 1` |
| `weekInfo` for `fa-IR` | Sunday or Monday first | `firstDay: 6`, `weekend: [5]` |
| `2026-02-29` | accepted by a naive validator | 2026 is not a leap year |

## Plurals and messages

| Case | Naive result | Correct |
|---|---|---|
| Russian, `count = 21` | plural form (`≠ 1`) | category `one` |
| Polish, `count = 22` | plural form | category `few` |
| Arabic, `count = 0` | plural form | category `zero` |
| Arabic, `count = 2` | plural form | category `two` |
| Japanese, any count | two strings maintained | one form (`other`) |
| English ordinal `11` | `11st` from `n % 10` | `11th` — category `other` |

## Text

| Value | Naive result | Correct |
|---|---|---|
| `'👨‍👩‍👧‍👦👍🏽abc'.slice(0, 3)` | `'👨‍'` — broken cluster | `Intl.Segmenter` truncation gives `'👨‍👩‍👧‍👦👍🏽a…'` |
| `'👨‍👩‍👧‍👦'.length` | `11` | 1 grapheme cluster, 25 UTF-8 bytes |
| `'🇦🇹'.length` | `4` | 1 grapheme cluster |
| `'ภาษาไทยไม่มีช่องว่าง'.split(' ')` | one token | 5 words via `Intl.Segmenter` |
| `'Dr. Smith went home.'` split on `. ` | breaks after `Dr.` | sentence segmentation keeps it together |
| `'File: שלום (2026)'` | punctuation reorders visually | wrap the Hebrew in `<bdi>` or U+2068/U+2069 |

## A minimal fixture

```json
{
  "names": ["Sukarno", "Gabriel García Márquez", "Vincent van Gogh",
            "Nagy Péter", "İrem Yıldız", "நிர்மலா", "Maria Weiß"],
  "addresses": [
    {"country":"IE","line1":"Ballyduff","locality":"Tullamore","admin":"Co. Offaly"},
    {"country":"AT","line1":"Hauptstraße 12/3","postal":"1010","locality":"Wien"},
    {"country":"NO","line1":"Karl Johans gate 1","postal":"0025","locality":"Oslo"},
    {"country":"NL","line1":"Damrak 1","postal":"1012 LG","locality":"Amsterdam"},
    {"country":"GB","line1":"1 Fleet Street","locality":"London","postal":"EC1Y 8SY"},
    {"country":"HK","admin":"Hong Kong Island","locality":"Central","line1":"1 Queen's Road"}
  ],
  "phones": ["+43 664 1234567", "+39 06 12345678", "+1 415 555 2671"],
  "ibans": ["AT611904300234573201", "MT84MALT011000012345MTLCAST001S", "NO9386011117947"],
  "money": [{"minor":1235,"currency":"JPY"}, {"minor":1234500,"currency":"KWD"},
            {"minor":123450,"currency":"EUR"}],
  "instants": ["2026-03-29T01:00:00Z", "2026-10-25T00:30:00Z", "2026-10-25T01:30:00Z"],
  "localTimes": [{"local":"2026-03-29T02:30","zone":"Europe/Vienna"},
                 {"local":"2026-10-25T02:30","zone":"Europe/Vienna"}],
  "counts": {"ru":[1,2,5,21], "pl":[2,5,22], "ar":[0,1,2,3,11,100]}
}
```

## Checkpoints

- [ ] Every name in the list submitted through the real signup form and rendered back
- [ ] Every address submitted, stored, re-rendered and printed on an invoice or label
- [ ] Every phone number parsed, stored and re-displayed
- [ ] Every IBAN validated; the 31-character Maltese one confirmed to survive the column
- [ ] The German VAT number confirmed not to be treated as a lookup failure
- [ ] Every money value formatted for at least three locales and checked against the minor-unit table
- [ ] Both DST edge times exercised through the scheduling path
- [ ] Sorting checked against the German, Swedish and Danish expected orders
- [ ] Plural counts checked for Russian 21, Polish 22 and Arabic 0/2
- [ ] Emoji and Tamil truncation checked in every place text is shortened
- [ ] Thai text run through the word-count or excerpt feature
- [ ] Hebrew value rendered inside an English sentence, in HTML and in a plain-text email
