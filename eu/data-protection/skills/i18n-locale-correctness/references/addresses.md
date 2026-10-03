# Addresses and postcodes

Authoritative basis: Google's libaddressinput address metadata, served at `https://www.gstatic.com/chrome/autofill/libaddressinput/chromium-i18n/ssl-address/data/<CC>` (the older `chromium-i18n.appspot.com` host now 302-redirects there). All `fmt`, `require` and `zip` values below were fetched from that endpoint on 2026-08-05. The HTML Living Standard autofill section (`html.spec.whatwg.org/multipage/form-control-infrastructure.html#autofill`) defines the field tokens.

## The metadata format

| Key | Meaning |
|---|---|
| `fmt` | Postal layout. `%N` name, `%O` organisation, `%A` street address, `%D` dependent locality, `%C` locality/city, `%S` administrative area, `%Z` postcode, `%n` line break |
| `require` | Letters for the fields that are **mandatory**. `A` street, `C` locality, `S` admin area, `Z` postcode, `N` name |
| `zip` | Regex for the postcode, anchored implicitly |
| `upper` | Fields the postal service wants upper-cased |
| `postprefix` | Prefix printed before the postcode (`CH-`, `SE-`, `FI-`) |
| `*_name_type` | What to **label** the field in that country |

`require` is the only thing that decides whether a field is mandatory. Do not decide it yourself.

## Per-country data, verified 2026-08-05

| CC | `fmt` | `require` | `zip` | Example | Notes |
|---|---|---|---|---|---|
| AT | `%O%n%N%n%A%n%Z %C` | `ACZ` | `\d{4}` | 1010 | no admin area; PLZ before city |
| DE | `%N%n%O%n%A%n%Z %C` | `ACZ` | `\d{5}` | 53225 | no admin area |
| CH | `%O%n%N%n%A%nCH-%Z %C` | `ACZ` | `\d{4}` | 1211 | `postprefix: CH-`; cantons not used postally |
| FR | `%O%n%N%n%A%n%Z %C` | `ACZ` | `\d{2} ?\d{3}` | 33380 | `upper: CX` — city upper-cased |
| GB | `%N%n%O%n%A%n%C%n%Z` | `ACZ` | see below | EC1Y 8SY | `locality_name_type: post_town`; `upper: CZ` |
| IE | `%N%n%O%n%A%n%D%n%C%n%S%n%Z` | *(absent)* | `[\dA-Z]{3} ?[\dA-Z]{4}` | A65 F4E2 | **no required fields at all**; `zip_name_type: eircode`, `state_name_type: county`, `sublocality_name_type: townland` |
| NL | `%O%n%N%n%A%n%Z %C` | `ACZ` | `[1-9]\d{3} ?(?:[A-RT-Z][A-Z]\|S[BCE-RT-Z])` | 1234 AB | letter pairs `SA`, `SD`, `SS` excluded |
| BE | `%O%n%N%n%A%n%Z %C` | `ACZ` | `\d{4}` | 1000 | |
| IT | `%N%n%O%n%A%n%Z %C %S` | `ACSZ` | `\d{5}` | 00144 | province **required**, two-letter code after city |
| ES | `%N%n%O%n%A%n%Z %C %S` | `ACSZ` | `\d{5}` | 28039 | province required |
| PT | `%N%n%O%n%A%n%Z %C` | `ACZ` | `\d{4}-\d{3}` | 2725-079 | hyphen is part of the code |
| PL | `%N%n%O%n%A%n%Z %C` | `ACZ` | `\d{2}-\d{3}` | 00-950 | |
| CZ | `%N%n%O%n%A%n%Z %C` | `ACZ` | `\d{3} ?\d{2}` | 100 00 | space inside the code |
| SE | `%O%n%N%n%A%nSE-%Z %C` | `ACZ` | `\d{3} ?\d{2}` | 114 55 | `postprefix: SE-`; `locality_name_type: post_town` |
| DK | `%N%n%O%n%A%n%Z %C` | `ACZ` | `\d{4}` | 1566 | |
| NO | `%N%n%O%n%A%n%Z %C` | `ACZ` | `\d{4}` | 0025 | leading zero significant |
| FI | `%O%n%N%n%A%nFI-%Z %C` | `ACZ` | `\d{5}` | 00550 | `postprefix: FI-` |
| HU | `%N%n%O%n%C%n%A%n%Z` | `ACZ` | `\d{4}` | 1037 | **city before street, postcode last** |
| US | `%N%n%O%n%A%n%C, %S %Z` | `ACSZ` | `(\d{5})(?:[ \-](\d{4}))?` | 22162-1010 | state required |
| CA | `%N%n%O%n%A%n%C %S %Z` | `ACSZ` | `[ABCEGHJKLMNPRSTVXY]\d[ABCEGHJ-NPRSTV-Z] ?\d[ABCEGHJ-NPRSTV-Z]\d` | H3Z 2Y7 | D, F, I, O, Q, U never used; W, Z not first |
| JP | `〒%Z%n%S%n%A%n%O%n%N` | `ASZ` | `\d{3}-?\d{4}` | 154-0023 | postcode **first**, name **last**; `state_name_type: prefecture` |
| AU | `%O%n%N%n%A%n%C %S %Z` | `ACSZ` | `\d{4}` | 2060 | `locality_name_type: suburb` |
| NZ | `%N%n%O%n%A%n%D%n%C %Z` | `ACDZ` | `\d{4}` | 6001 | dependent locality **required** |
| HK | `%S%n%C%n%A%n%O%n%N` | `AS` | *(none)* | — | **no postcode**; `state_name_type: area`, `locality_name_type: district` |
| AE | `%N%n%O%n%A%n%S` | `AS` | *(none)* | — | **no postcode**; `state_name_type: emirate` |
| SG | `%N%n%O%n%A%nSINGAPORE %Z` | `AZ` | `\d{6}` | 546080 | **no city field** |
| IN | `%N%n%O%n%A%n%T%n%F%n%L%n%C %Z%n%S` | `ACSZ` | `\d{6}` | 110034 | `zip_name_type: pin` |
| BR | `%O%n%N%n%A%n%D%n%C-%S%n%Z` | `ASCZ` | `\d{5}-?\d{3}` | 40301-110 | `sublocality_name_type: neighborhood` |
| MX | `%N%n%O%n%A%n%D%n%Z %C, %S` | `ACSZ` | `\d{5}` | 02860 | postcode before city |
| CN | `%Z%n%S%C%D%n%A%n%O%n%N` | `ACSZ` | `\d{6}` | 266033 | largest-to-smallest ordering |
| KR | `%S %C%D%n%A%n%O%n%N%n%Z` | `ACSZ` | `\d{5}` | 03051 | postcode last, name before it |

Read across the table: the postcode comes before the city in DACH, France, Poland and the Nordics; after the city in the UK, Ireland and Korea; first on the whole address in Japan and China; and does not exist in Hong Kong or the UAE. Hungary puts the city above the street. Japan, China and Korea reverse the whole block.

## Countries with no postal code

libaddressinput omits the `zip` key entirely for these, which is the machine-readable form of "do not require one": Hong Kong, Macau, United Arab Emirates, Qatar, Panama, Angola, Antigua and Barbuda, Aruba, Bahamas, Belize, Benin, Bolivia, Botswana, Burkina Faso, Burundi, Cameroon, Central African Republic, Chad, Comoros, Republic of the Congo, Côte d'Ivoire, Djibouti, Dominica, Equatorial Guinea, Eritrea, Fiji, Gambia, Ghana, Grenada, Guyana, Kiribati, Libya, Malawi, Mali, Mauritania, Nauru, Niue, Rwanda, Saint Kitts and Nevis, Saint Lucia, Samoa, São Tomé and Príncipe, Seychelles, Sierra Leone, Solomon Islands, Somalia, Suriname, Syria, Tanzania, Timor-Leste, Togo, Tokelau, Tonga, Tuvalu, Uganda, Vanuatu, Yemen, Zimbabwe. `[[UNVERIFIED: this list was assembled from libaddressinput's absent-`zip` set; fetch each `data/<CC>` before relying on the tail of it]]`

A postcode field must therefore be **conditionally rendered and conditionally required**, driven by the country selection.

## Postcodes that are not just numbers

**United Kingdom.** Outward code (area + district) plus inward code (sector + unit), separated by a space that is significant: `EC1Y 8SY`, `M2 5BQ`, `DN16 9AA`. The outward code is one or two letters plus one or two digits, optionally with a trailing letter (`W1A`, `EC1A`). The inward code is always digit + two letters, and those two letters never include C, I, K, M, O or V. Special cases exist: `GIR 0AA` (Girobank) and `BFPO 1234` (British Forces). The libaddressinput regex enumerates every valid area code and is the practical validator:

```
GIR ?0AA|(?:(?:AB|AL|B|BA|BB|BD|BF|BH|BL|BN|BR|BS|BT|BX|CA|CB|CF|CH|CM|CO|CR|CT|CV|CW|DA|DD|DE|DG|DH|DL|DN|DT|DY|E|EC|EH|EN|EX|FK|FY|G|GL|GY|GU|HA|HD|HG|HP|HR|HS|HU|HX|IG|IM|IP|IV|JE|KA|KT|KW|KY|L|LA|LD|LE|LL|LN|LS|LU|M|ME|MK|ML|N|NE|NG|NN|NP|NR|NW|OL|OX|PA|PE|PH|PL|PO|PR|RG|RH|RM|S|SA|SE|SG|SK|SL|SM|SN|SO|SP|SR|SS|ST|SW|SY|TA|TD|TF|TN|TQ|TR|TS|TW|UB|W|WA|WC|WD|WF|WN|WR|WS|WV|YO|ZE)(?:\d[\dA-Z]? ?\d[ABD-HJLN-UW-Z]{2}))|BFPO ?\d{1,4}
```

Normalise on input: upper-case, collapse whitespace, then insert a single space before the last three characters. Do not reject an input that lacks the space.

**Ireland.** Eircode: seven characters, a three-character routing key identifying the post town plus a four-character unique identifier, conventionally written with a space (`A65 F4E2`). The letter `O` is excluded to avoid confusion with zero (`eircode.ie`). Eircodes were rolled out from 2015 across roughly 2.2 million addresses with new ones assigned monthly, but libaddressinput gives Ireland **no `require` string at all** — a valid Irish address may consist of a townland and a county with no street number and no postcode. Do not require Eircode.

**Netherlands.** Four digits (never starting with 0) plus two letters: `1234 AB`. The combinations `SA`, `SD` and `SS` are excluded. Postcode plus house number uniquely identifies a Dutch address, which is why Dutch checkouts ask for those two fields and derive street and city — that is the expected UX there and a street field asked first reads as broken.

**Canada.** `A1A 1A1`, alternating letter and digit. The letters D, F, I, O, Q and U are never used anywhere; W and Z are never the first character. The first character encodes the province, so a postcode and a province field can contradict each other and the postcode is the reliable one.

**Portugal, Poland, Czechia.** The separator is part of the format: `2725-079`, `00-950`, `100 00`. Strip it on input, re-insert it on output; do not store the user's punctuation.

## Storage shape

```sql
country            char(2)  not null,          -- ISO 3166-1 alpha-2, drives everything else
address_line1      text     not null,
address_line2      text,
address_line3      text,
locality           text,                       -- city / post town / suburb
dependent_locality text,                       -- neighbourhood / townland / district
administrative_area text,                      -- state / province / prefecture / county
postal_code        text,                       -- text, never integer: 0025 and A65 F4E2
sorting_code       text,                       -- FR CEDEX and similar
organization       text,
recipient          text     not null           -- the full name; see names.md
```

- `postal_code` is `text`. An integer column silently destroys the Norwegian `0025` and cannot hold `A65 F4E2` at all.
- There is **no** `house_number` column and no `street_name` column. Germany, Austria, the Netherlands, Sweden, Italy, Spain and Poland put the number after the street; France, the UK, Ireland, the US, Canada and Australia put it before. Numbers carry letters and additions: `12a`, `12/3`, `12 bis`, `12-14`. Free-text address lines hold all of it; parsed columns do not.
- `administrative_area` is nullable. Only `IT`, `ES`, `US`, `CA`, `AU`, `JP`, `BR`, `MX`, `CN`, `KR`, `IN`, `HK`, `AE` (from the `S` in `require` above) need it among the countries listed.
- Store one country code, not a country name. Names are localised; codes are not.

## Rendering a postal address

```js
// Format an address for postal use from libaddressinput `fmt`.
// data: { N, O, A, D, C, S, Z, sortingCode }
function formatPostal(fmt, data, { upper = '', postprefix = '' } = {}) {
  const v = k => {
    let s = data[k] ?? '';
    if (upper.includes(k)) s = s.toLocaleUpperCase('und');   // postal, not display
    return s;
  };
  return fmt
    .split('%n')
    .map(line => line.replace(/%([NOADCSZX])/g, (_, k) => v(k)).trim())
    .map(line => line.replace(/\s{2,}/g, ' ').replace(/^[,\s]+|[,\s]+$/g, ''))
    .filter(Boolean)
    .join('\n');
}

// AT: "%O%n%N%n%A%n%Z %C"
formatPostal('%O%n%N%n%A%n%Z %C',
  { N: 'Anna Berger', A: 'Hauptstraße 12/3', Z: '1010', C: 'Wien' });
// Anna Berger
// Hauptstraße 12/3
// 1010 Wien
```

Empty fields must collapse the whole line, not leave a blank one. The `%Z %C` pattern must not leave a leading space when the postcode is absent — hence the trim and the collapse.

## Checkpoints

- [ ] Country is the first field in the form and re-renders the rest of it
- [ ] Field set, field order and labels come from per-country data, not from one hard-coded layout
- [ ] Postcode field is hidden for countries whose metadata has no `zip` key
- [ ] Postcode is `text` in the database, never a numeric type
- [ ] Postcode requiredness comes from `require`, and Ireland is not forced to supply one
- [ ] Administrative-area field is hidden for AT, DE, CH, NL, GB, FR, BE, PL, CZ and the Nordics
- [ ] No separate `house_number` column; street address is free-text lines
- [ ] UK postcode normalised (upper-case, single space before the last three characters) rather than rejected
- [ ] Dutch checkout offers postcode + house number lookup, not a street-first form
- [ ] Labels use the country's own term: post town (GB), Eircode/county (IE), prefecture (JP), suburb (AU), PIN (IN), emirate (AE)
- [ ] Country stored as ISO 3166-1 alpha-2, not a display name
- [ ] Postal rendering collapses empty lines and leaves no stray separators
- [ ] Address metadata snapshot dated, with a task to regenerate it before release
