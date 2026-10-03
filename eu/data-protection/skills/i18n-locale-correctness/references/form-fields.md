# Form fields and autofill

Authoritative basis: HTML Living Standard, autofill section (`html.spec.whatwg.org/multipage/form-control-infrastructure.html#autofill`), fetched 2026-08-05. Address field sets from libaddressinput (see `addresses.md`).

## The complete autofill token set that matters here

Quoted meanings are the spec's own wording.

| Token | Spec meaning | Use it for |
|---|---|---|
| `name` | "Full name" | the single name field — **default choice** |
| `given-name` | "Given name (in some Western cultures, also known as the first name)" | only when you store both parts |
| `additional-name` | "Additional names (in some Western cultures, also known as middle names)" | rarely |
| `family-name` | "Family name (in some Western cultures, also known as the last name or surname)" | only when you store both parts |
| `honorific-prefix` | "Prefix or title (e.g. 'Mr.', 'Ms.', 'Dr.', 'Mille')" | optional, free text |
| `honorific-suffix` | "Suffix (e.g. 'Jr.', 'B.Sc.', 'MBASW', 'II')" | optional, free text |
| `nickname` | "a typically short name used instead of the full name" | preferred name |
| `organization` | "Company name corresponding to the person, address, or contact information" | B2B |
| `organization-title` | "Job title" | |
| `street-address` | "Street address (multiple lines, newlines preserved)" | a single `<textarea>` |
| `address-line1/2/3` | "Street address (one line per field)" / continuation | separate inputs |
| `address-level1` | "The broadest administrative level in the address … in the US, this would be the state; in Switzerland it would be the canton; in the UK, the post town" | **not** a state field |
| `address-level2` | "in the countries with two administrative levels, this would typically be the city, town, village, or other locality" | city, usually |
| `address-level3` / `address-level4` | third and "most fine-grained" administrative levels | CN, BR, IN, KR |
| `country` | "Country code" (ISO 3166-1 alpha-2) | the hidden/value field |
| `country-name` | "Country name" | the visible label if separate |
| `postal-code` | "Postal code, post code, ZIP code, CEDEX code" | |
| `tel` | "Full telephone number, including country code" | **the one to use** |
| `tel-country-code` / `tel-national` / `tel-area-code` / `tel-local` / `tel-extension` | components | only if you split, which you should not |
| `email` | "Email address" | |
| `bday` / `bday-day` / `bday-month` / `bday-year` | birthday and its parts | |
| `language` | "Preferred language" (BCP 47) | |
| `transaction-currency` | "The currency that the user would prefer the transaction to use" | ISO 4217 code |

Hint tokens `shipping` and `billing` prefix an address token (`autocomplete="shipping postal-code"`). The `section-*` prefix scopes a group when a page has two of the same address: `autocomplete="section-invoice billing address-line1"`.

**The `address-level1` trap.** Because the spec ties level 1 to "the broadest administrative level", the same token means the US state, the Swiss canton and the UK post town. A form that labels `address-level1` "State" and requires it is wrong in every country that is not the US. Take requiredness from libaddressinput's `require` string, take the label from `*_name_type`, and use the token only so the browser can fill it.

## Address form order per country

Country selector first. Everything below it re-renders when the country changes, including labels, requiredness and the postcode pattern. Order the visible fields in the country's own postal order — a European user who meets `City / State / ZIP` in that order recognises a US form and distrusts the checkout.

| Country | Visible order below name | Required | Level-1 label |
|---|---|---|---|
| AT, DE | street + number, postcode, city | street, postcode, city | *(no field)* |
| CH | street + number, postcode, city | street, postcode, city | *(no field; canton is not postal)* |
| FR | street, postcode, city (upper-case) | street, postcode, city | *(no field)* |
| NL | postcode, house number, then street + city (derived) | street, postcode, city | *(no field)* |
| BE, DK, NO, SE, FI, PL, CZ, PT | street + number, postcode, city | street, postcode, city | *(no field)* |
| GB | address lines, post town, postcode | lines, post town, postcode | Post town |
| IE | address lines, townland, town, county, Eircode | *(none required)* | County |
| IT, ES | street, postcode, city, province | street, postcode, city, province | Province / Provincia |
| HU | postcode, city, street + number | all three | *(no field)* |
| US | street, city, state, ZIP | all four | State |
| CA | street, city, province, postal code | all four | Province |
| AU | street, suburb, state, postcode | all four | State |
| JP | postcode, prefecture, address, name last | postcode, prefecture, address | Prefecture |
| IN | street, city, PIN, state | all four | State |
| HK | area, district, address | area, address | Area |
| AE | address, emirate | address, emirate | Emirate |
| SG | address, postal code | both | *(no city field)* |

## Input attributes that matter

```html
<!-- Country: always first, always a select of ISO codes with localised labels -->
<label for="country">Country</label>
<select id="country" name="country" autocomplete="country" required>
  <!-- value = ISO 3166-1 alpha-2; label = Intl.DisplayNames(uiLocale, {type:'region'}) -->
</select>

<!-- Name: one field -->
<input name="name" autocomplete="name" type="text" maxlength="200" required>

<!-- Street: free text, number position is the user's business -->
<input name="address_line1" autocomplete="address-line1" type="text" maxlength="200" required>
<input name="address_line2" autocomplete="address-line2" type="text" maxlength="200">

<!-- Postcode: text input, never type=number -->
<input name="postal_code" autocomplete="postal-code" type="text"
       inputmode="text" autocapitalize="characters" maxlength="12">

<!-- Phone: one field, international -->
<input name="phone" autocomplete="tel" type="tel" inputmode="tel" maxlength="32">

<!-- Email -->
<input name="email" autocomplete="email" type="email" inputmode="email"
       autocapitalize="none" autocorrect="off" spellcheck="false">
```

Rules behind those attributes:

- **`type="number"` is never right for a postcode.** It strips leading zeros (Norway's `0025` becomes `25`), refuses letters (Canada, the UK, the Netherlands, Ireland) and shows a spinner on a value that is not a quantity. Use `type="text"`.
- **`inputmode="numeric"` only for countries whose `zip` regex is digits-only**, and switch it when the country changes. A Dutch user on `inputmode="numeric"` cannot type the letters.
- **`autocapitalize="characters"`** helps for GB, CA, IE, NL postcodes; `autocapitalize="none"` is mandatory on email.
- **`maxlength` counts UTF-16 code units in the browser**, so set it generously (200 for a name or a street) and enforce the real limit server-side in grapheme clusters — see `text-handling.md`.
- **No `pattern` attribute on name, street or city.** A `pattern` is a client-side rejection, and every character class you write will exclude a real user's apostrophe, hyphen, particle or script.
- **`pattern` on postcode is acceptable** only if it is generated from the selected country's `zip` value and is removed when the country has none.

## Validation posture

Normalise, then check, then warn — in that order, and only reject on the last.

```js
// Postcode: normalise before validating. Never reject formatting.
function normalisePostalCode(raw, country) {
  let s = raw.trim().toUpperCase().replace(/\s+/g, ' ');
  if (country === 'GB' || country === 'IE') {
    s = s.replace(/\s/g, '');
    s = s.slice(0, -3) + ' ' + s.slice(-3);          // inward code is always 3 chars
  }
  if (country === 'NL') s = s.replace(/^(\d{4})\s*([A-Z]{2})$/, '$1 $2');
  if (country === 'CA') s = s.replace(/^([A-Z]\d[A-Z])\s*(\d[A-Z]\d)$/, '$1 $2');
  if (country === 'PL') s = s.replace(/^(\d{2})[-\s]?(\d{3})$/, '$1-$2');
  if (country === 'PT') s = s.replace(/^(\d{4})[-\s]?(\d{3})$/, '$1-$2');
  if (country === 'CZ') s = s.replace(/^(\d{3})\s?(\d{2})$/, '$1 $2');
  return s;
}

// Then, and only then, test against the country pattern — as a warning, not a block,
// unless the value is going to a carrier API that will reject the shipment.
function postalCodeLooksWrong(value, meta) {
  if (!meta.zip) return false;                        // country has no postcode
  return !new RegExp(`^(?:${meta.zip})$`).test(value);
}
```

A soft warning ("This does not look like an Austrian postcode — is it right?") with the submit button still enabled catches typos without locking out the edge case your data does not know about. Hard rejection is justified only where a downstream system will fail on the value anyway.

## Error messages

Name the field by its local term and say what was expected, not that the input was "invalid":

- Bad: "Invalid ZIP code."
- Good (AT): "Die PLZ besteht aus 4 Ziffern, z. B. 1010." / "An Austrian postcode has 4 digits, for example 1010."
- Good (GB): "A UK postcode looks like EC1Y 8SY."

Error text goes through the message pipeline like any other string — see `messages-and-plurals.md`. Never build it by concatenating "Invalid " + fieldName.

## Checkpoints

- [ ] Country selector is the first field and drives labels, order, requiredness and patterns
- [ ] Country option labels come from `Intl.DisplayNames`, sorted with `Intl.Collator` for the UI locale
- [ ] One `autocomplete="name"` field; `given-name`/`family-name` only where both are stored
- [ ] `address-level1` is never labelled "State" outside the countries that use one
- [ ] Requiredness taken from libaddressinput `require`, not from a hard-coded list
- [ ] No postcode field rendered for HK, AE and the other no-postcode countries
- [ ] Postcode input is `type="text"`, with `inputmode` switched per country
- [ ] No `pattern` attribute on name, street, city or organisation
- [ ] Phone is one `autocomplete="tel"` field, not a country-code dropdown plus a number box
- [ ] Email input has `autocapitalize="none"` and `spellcheck="false"`
- [ ] `maxlength` values are generous and the real limit is enforced server-side in graphemes
- [ ] Postcode normalised before validation, and validation failure warns rather than blocks unless a downstream system requires it
- [ ] Error messages name the local field term and give a valid example
- [ ] Form tested by filling it with the browser's stored address for each target country
