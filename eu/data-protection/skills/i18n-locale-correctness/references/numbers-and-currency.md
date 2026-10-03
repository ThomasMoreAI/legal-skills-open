# Numbers and currency

Authoritative basis: Unicode CLDR 48.2 via ECMA-402 `Intl.NumberFormat`; ISO 4217, **List One published 2026-01-01** (`six-group.com`, the ISO 4217 maintenance agency). All formatting output below was executed on Node 22.19.0 / ICU 77.1 and codepoints were read directly. Status as at 2026-08-05.

## Separators are not what you think

Verified output for `1234567.89`, with the actual separator codepoints:

| Locale | Output | Group separator | Decimal separator |
|---|---|---|---|
| `en-US` | `1,234,567.89` | `,` U+002C | `.` U+002E |
| `de-DE` | `1.234.567,89` | `.` U+002E | `,` U+002C |
| `de-AT` | `1 234 567,89` | **U+00A0 NO-BREAK SPACE** | `,` U+002C |
| `fr-FR` | `1 234 567,89` | **U+202F NARROW NO-BREAK SPACE** | `,` U+002C |
| `sv-SE` | `1 234 567,89` | U+00A0 | `,` U+002C |
| `de-CH` | `1’234’567.89` | **U+2019 RIGHT SINGLE QUOTATION MARK** | `.` U+002E |
| `it-CH` | `1’234’567.89` | U+2019 | `.` U+002E |
| `nb-NO` | `1 234 567,89` | U+00A0 | `,` U+002C |

Three things follow.

- **The Swiss separator is U+2019, not the ASCII apostrophe U+0027.** A regex written as `/'/g` does not match it. Neither does a copy-paste from a Swiss spreadsheet into a `parseFloat`.
- **Space separators are non-breaking and invisible in a diff.** `\s` in JavaScript matches U+00A0 but a hand-written `[ ]` character class does not, and U+202F is matched by `\s` only in Unicode mode.
- **`de-CH` uses a decimal point where `de-DE` uses a comma.** Same language, opposite convention.

**Group separators are not applied at four digits in every locale.** Verified: `1234` formats as `1.234` in `de-DE` and `1,234` in `en-US`, but as plain `1234` in `pl-PL`, `es-ES`, `it-IT` and `pt-PT` — CLDR's `minimumGroupingDigits` is 2 there. `useGrouping: 'min2'` reproduces this explicitly.

## Grouping systems that are not groups of three

`en-IN` and `hi-IN` group by the Indian lakh/crore system: verified, `12345678.9` formats as **`1,23,45,678.9`** — three digits, then pairs. Any code that inserts a separator every three characters produces `12,345,678.9` and reads as wrong to an Indian user.

## The minus sign

Verified: `de-DE` renders `-1` with **U+002D HYPHEN-MINUS**, `sv-SE` renders it with **U+2212 MINUS SIGN**. A string comparison against `'-'` fails for Swedish output, and a Swedish user pasting a negative figure back into your form gets a parse failure.

## Currency: symbol, position and spacing

Verified for `1234.5`:

| Locale | Currency | Output |
|---|---|---|
| `de-AT` | EUR | `€ 1.234,50` — symbol **first**, U+00A0 after it |
| `de-DE` | EUR | `1.234,50 €` — symbol **last** |
| `fr-FR` | EUR | `1 234,50 €` |
| `nl-NL` | EUR | `€ 1.234,50` |
| `en-IE` | EUR | `€1,234.50` — no space |
| `de-CH` | CHF | `CHF 1’234.50` |
| `en-US` | USD | `$1,234.50` |
| `en-GB` | GBP | `£1,234.50` |
| `pl-PL` | PLN | `1234,50 zł` |
| `cs-CZ` | CZK | `1 234,50 Kč` |
| `is-IS` | ISK | `1.235 kr.` — zero decimals |
| `en-US` | JPY | `¥1,235` (U+00A5) |
| `ja-JP` | JPY | `￥1,235` (U+FFE5 FULLWIDTH) |
| `en-US` | KWD | `KWD 1,234.500` — three decimals |

**The same locale can group differently for a bare number and for money.** Verified for `de-AT`: `Intl.NumberFormat('de-AT').format(1234567.89)` is `1 234 567,89` (U+00A0) but `Intl.NumberFormat('de-AT', {style:'currency', currency:'EUR'}).format(1234567.89)` is `€ 1.234.567,89` (period). There is no single "Austrian number format" you can extract into a constant.

Use `formatToParts` whenever you need to place the symbol yourself:

```js
new Intl.NumberFormat('de-AT', { style: 'currency', currency: 'EUR' }).formatToParts(1234.5)
// [{type:'currency',value:'€'},{type:'literal',value:' '},
//  {type:'integer',value:'1'},{type:'group',value:'.'},{type:'integer',value:'234'},
//  {type:'decimal',value:','},{type:'fraction',value:'50'}]
```

## Minor units are not always two

ISO 4217 List One (published 2026-01-01) gives, of 139 currencies with 2 minor units:

- **0 minor units:** BIF, CLP, DJF, GNF, ISK, JPY, KMF, KRW, PYG, RWF, UGX, VND, VUV, XAF, XOF, XPF
- **3 minor units:** BHD, IQD, JOD, KWD, LYD, OMR, TND
- **4 minor units:** CLF, UYW (funds codes)
- **`N.A.`:** the precious-metal and testing codes XAU, XAG, XPT, XPD, XDR, XTS, XXX and the XB* bond codes

So `amount / 100` is wrong for JPY (no division) and for KWD (divide by 1000). Read the exponent from data:

```js
function minorUnitExponent(currency) {
  return new Intl.NumberFormat('en', { style: 'currency', currency })
    .resolvedOptions().minimumFractionDigits;
}
minorUnitExponent('EUR') // 2
minorUnitExponent('JPY') // 0
minorUnitExponent('KWD') // 3
minorUnitExponent('ISK') // 0
```

Verified against the ISO 4217 list for EUR, USD, JPY, KWD, ISK, BHD, TND, CLP, VND, OMR, JOD. Note `HUF` resolves to 2 in CLDR even though Hungarian retail prices are always whole forints — CLDR's `currencyData` and ISO 4217 agree on 2 here, and the rounding convention is a business rule, not a format rule.

## Storing money

```sql
amount_minor  bigint  not null,      -- 1234 = EUR 12.34; 1234 = JPY 1234
currency      char(3) not null       -- ISO 4217 alphabetic code
```

- **Never `float` or `double`.** `0.1 + 0.2 !== 0.3` is not a rounding curiosity in an invoice, it is a reconciliation failure.
- **Never a bare `decimal` without the currency.** The scale depends on the currency, and a `decimal(10,2)` column cannot represent a Kuwaiti dinar.
- **Never sum across currencies.** A total column with mixed currencies is a bug waiting for its first Swiss customer.
- Convert to a display string only at the edge, with `Intl.NumberFormat`.

```js
export function formatMoney(amountMinor, currency, locale) {
  const exp = new Intl.NumberFormat('en', { style: 'currency', currency })
    .resolvedOptions().minimumFractionDigits;
  return new Intl.NumberFormat(locale, { style: 'currency', currency })
    .format(amountMinor / 10 ** exp);
}
formatMoney(123450, 'EUR', 'de-AT');  // '€ 1.234,50'
formatMoney(1235,   'JPY', 'ja-JP');  // '￥1,235'
formatMoney(1234500,'KWD', 'en-US');  // 'KWD 1,234.500'
```

Division by `10 ** exp` introduces a float only at the display step, where the value is already about to be rounded to that many places. For arithmetic, stay in integers.

## Parsing what the user typed

There is no `Intl.NumberFormat.parse`. You have to build it from the locale's own parts:

```js
export function parseLocaleNumber(input, locale) {
  const parts = new Intl.NumberFormat(locale).formatToParts(12345.6);
  const group   = parts.find(p => p.type === 'group')?.value   ?? '';
  const decimal = parts.find(p => p.type === 'decimal')?.value ?? '.';
  let s = input.trim()
    .replace(/[−–‒]/g, '-')          // MINUS SIGN, EN DASH, FIGURE DASH
    .replace(/[   \s]/g, '')         // NBSP, NNBSP, thin space, spaces
    .replace(/’/g, '');                        // Swiss group separator
  if (group && group !== ' ') s = s.split(group).join('');
  s = s.replace(decimal, '.');
  const n = Number(s);
  return Number.isFinite(n) ? n : NaN;
}
parseLocaleNumber('1.234,50', 'de-DE');   // 1234.5
parseLocaleNumber('1’234.50', 'de-CH');   // 1234.5
parseLocaleNumber('1 234,50', 'fr-FR');   // 1234.5
parseLocaleNumber('1,23,456.78', 'en-IN');// 123456.78
```

Two rules around this function:

- **Never `parseFloat` a user-typed amount.** `parseFloat('1,50')` returns `1`, silently undercharging by a factor of 100.
- **Accept both separators on input where they are unambiguous.** A German user typing `1234.50` almost certainly means 1234 euro 50, not 123450 cents. Accept it, then echo back the normalised value so the user can see what you understood before submitting.

`<input type="number">` uses the browser's locale for its value parsing but always exposes `.value` in the HTML number format (period decimal). It also rejects a comma outright in some locales. For money, use `type="text"` with `inputmode="decimal"` and parse it yourself.

## Percentages, units, compact form

```js
new Intl.NumberFormat('de-AT', { style: 'percent', maximumFractionDigits: 1 }).format(0.075);
// '7,5 %'   — note the space; en-US gives '7.5%'
new Intl.NumberFormat('de', { style: 'unit', unit: 'kilometer-per-hour' }).format(50); // '50 km/h'
new Intl.NumberFormat('de', { notation: 'compact' }).format(1200000);                  // '1,2 Mio.'
```

The percent sign is spaced in German and French and unspaced in English. Do not append `'%'` by hand.

## Checkpoints

- [ ] Money stored as integer minor units plus an ISO 4217 code
- [ ] No `float`, `double` or `REAL` column holds an amount
- [ ] Minor-unit exponent read from data, never assumed to be 2
- [ ] No arithmetic sums amounts across currencies
- [ ] All display formatting goes through `Intl.NumberFormat`
- [ ] No hard-coded decimal separator, group separator or currency symbol anywhere
- [ ] No hard-coded `%` concatenation
- [ ] Symbol placement taken from `formatToParts` where the layout needs it
- [ ] `parseFloat` absent from any path that reads a user-typed amount
- [ ] Input parser handles U+00A0, U+202F, U+2019 and U+2212
- [ ] Amount inputs are `type="text"` with `inputmode="decimal"`, not `type="number"`
- [ ] Parsed value echoed back to the user in normalised form before submission
- [ ] Indian grouping tested if India is a market
- [ ] A JPY and a KWD price tested end to end, including the invoice PDF
