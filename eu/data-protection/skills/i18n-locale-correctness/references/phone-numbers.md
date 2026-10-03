# Phone numbers

Authoritative basis: ITU-T Recommendation E.164, current in-force edition **(02/2026)**, "The international public telecommunication numbering plan" (`itu.int/rec/T-REC-E.164/en`, checked 2026-08-05). Implementation: Google libphonenumber, current release **v9.0.36 (2026-07-31)** (`github.com/google/libphonenumber/releases`); JavaScript ports `libphonenumber-js` 1.13.10 and `google-libphonenumber` 3.2.46 (npm, checked 2026-08-05).

## Why regex validation is always wrong

libphonenumber released v9.0.30 (2026-05-07), v9.0.31, v9.0.32, v9.0.33, v9.0.34, v9.0.35 and v9.0.36 (2026-07-31) in under three months, and the project describes these as "mostly metadata changes". Number ranges open, close and move between operators continuously. A regex is a frozen copy of that metadata; it is out of date on the day it is written and nobody ever updates it.

The regexes that get written are also wrong on their own terms:

- `^\d{10}$` — a US assumption. German numbers run from 7 to 13 national digits, Austrian mobile numbers vary by operator block, and Italian numbers keep a leading zero.
- `^\+?[0-9]{7,15}$` — accepts `+9999999999999` and rejects every number a human typed with spaces, brackets or a hyphen.
- Stripping all non-digits before validating throws away the `+` that told you the number was international.

E.164 defines a numbering plan with a maximum of 15 digits after the country code prefix. It does not define a syntax you can pattern-match, because whether a given 15-or-fewer-digit string is assigned is a metadata question.

## Storage

One column. E.164, digits and one leading `+`, no spaces, no punctuation.

```sql
phone_e164        text,             -- '+436641234567'
phone_country     char(2),          -- 'AT' — derived, for display formatting only
phone_verified_at timestamptz
```

Never store the user's typed string alongside the E.164 form as a second source of truth; they drift. Never store the national format — you cannot reconstruct the country from it. Never store a separate country-code column as the input mechanism; derive it after parsing.

## Parsing and formatting

```js
import {
  parsePhoneNumberWithError,
  ParseError,
} from 'libphonenumber-js/max';   // /max carries the type-detection patterns

/**
 * @param {string} raw          whatever the user typed
 * @param {string} defaultCountry ISO 3166-1 alpha-2, from the address form or IP
 */
export function normalisePhone(raw, defaultCountry) {
  try {
    const n = parsePhoneNumberWithError(raw, defaultCountry);
    if (!n.isValid()) return { ok: false, reason: 'NOT_VALID' };
    return {
      ok: true,
      e164: n.number,                    // '+436641234567'  <- store this
      country: n.country,                // 'AT'
      national: n.formatNational(),      // '0664 1234567'   <- show this to a local
      international: n.formatInternational(), // '+43 664 1234567'
      type: n.getType(),                 // 'MOBILE' | 'FIXED_LINE' | ... | undefined
      uri: n.getURI(),                   // 'tel:+436641234567'
    };
  } catch (e) {
    if (e instanceof ParseError) return { ok: false, reason: e.message };
    throw e;
  }
}
```

`ParseError` messages are enumerated: `NOT_A_NUMBER` (no digits, or only a `+`), `INVALID_COUNTRY` (no such country code, or a national-format number with no `defaultCountry`), `TOO_SHORT`, `TOO_LONG` (national number over 17 digits, or input over 250 characters).

**Metadata bundles.** `libphonenumber-js` defaults to `min` metadata (~80 kB) which validates **length only**. `/max` adds ~65 kB and the per-type patterns. `/mobile` carries only mobile patterns. With `min`, `getType()` returns `undefined` for most countries and `isValidPhoneNumber('+6589555555')` returns `true` where `/max` correctly returns `false`. If you validate or detect type, you need `/max`; there is no correct configuration in which `min` does either job.

**Display.** Format at render time from the stored E.164 value, using the viewer's context: national format for a viewer in the same country, international format otherwise. Never store the formatted string.

## Trunk prefixes and the leading zero

In most of Europe a national number is dialled with a leading `0` — the trunk prefix. It is not part of the number in E.164 and is dropped: Austrian `0664 1234567` is `+43 664 1234567`. It is also **not noise**: it is the signal that tells the parser the string is in national rather than international format. Hand-stripping every leading zero before parsing destroys that signal.

**Italy is the exception.** Italian fixed-line numbers retain the leading `0` after the country code: Rome numbers are `+39 06 …`, not `+39 6 …`. Italian mobile numbers have no leading zero. A hand-rolled "strip the leading zero after the country code" rule silently corrupts every Italian landline. Let libphonenumber handle it; that is what the metadata is for.

Other cases the metadata already knows and you would not: Russia and Kazakhstan use `8` as the trunk prefix, not `0`; the NANP (`+1`) uses `1`; several countries have no trunk prefix at all.

## Type detection and its limits

`getType()` returns one of `MOBILE`, `FIXED_LINE`, `FIXED_LINE_OR_MOBILE`, `PREMIUM_RATE`, `TOLL_FREE`, `SHARED_COST`, `VOIP`, `PERSONAL_NUMBER`, `PAGER`, `UAN`, `VOICEMAIL`, or `undefined`.

Three limits, all of which matter if you gate SMS on the answer:

1. **`FIXED_LINE_OR_MOBILE` is the honest answer for whole countries.** In the NANP the ranges overlap and no metadata can separate them. Treating that value as "not mobile" blocks every US and Canadian user from SMS.
2. **Number portability defeats range-based detection.** A number ported from a fixed-line block to a mobile operator still looks fixed-line in the metadata.
3. **`undefined` is not "invalid".** With `min` metadata it is the normal result. Do not branch on it as a failure.

The reliable test that a number can receive SMS is to send one. Use type detection to order the UI (offer SMS first when the type is `MOBILE`), never to forbid a channel.

## Input UX

One field, `type="tel"`, `autocomplete="tel"`, `inputmode="tel"`. No separate country-code dropdown: it doubles the failure modes (the user pastes a full international number into the national box, or picks the wrong flag) and browsers autofill `tel` as one string.

```html
<label for="phone">Phone number</label>
<input id="phone" name="phone" type="tel" autocomplete="tel" inputmode="tel"
       maxlength="32" placeholder="+43 664 1234567">
<p id="phone-hint">Include the country code, or we will assume Austria.</p>
```

- Accept and preserve spaces, brackets, hyphens, dots and a leading `+` in the input. Strip nothing client-side.
- Derive `defaultCountry` from the address form's country field if one exists, otherwise from the user's locale region subtag, otherwise ask. Never guess it silently and then reject the result.
- Format as-you-type only with `AsYouType` from the same library; a hand-written formatter fights the user's cursor.
- Never validate on `blur` before the user has finished; validate on submit.

## What to do with an invalid number

If the field is optional (most cases), store nothing and move on. If the number is required for delivery or for 2FA, tell the user what was understood:

> "We read this as +43 664 1234 — that is shorter than an Austrian mobile number. Please check it."

Do not say "invalid phone number". The user knows their own number is valid; the message has to say what your parser thought it saw.

## Checkpoints

- [ ] No regex anywhere in the codebase validates a phone number
- [ ] Exactly one column stores the number, in E.164, as `text`
- [ ] No column stores a national or formatted phone string
- [ ] Parsing uses libphonenumber with `/max` metadata wherever validation or type detection happens
- [ ] `defaultCountry` is derived explicitly and its source is documented
- [ ] Leading zeros are never stripped by hand before parsing
- [ ] An Italian fixed-line number round-trips correctly (`+39 06 …` keeps its zero)
- [ ] Display formatting happens at render time from the stored E.164 value
- [ ] SMS eligibility is not gated on `getType()`; `FIXED_LINE_OR_MOBILE` and `undefined` are not treated as failures
- [ ] Input is a single `type="tel"` field with `autocomplete="tel"`, no country dropdown
- [ ] Input accepts spaces, brackets, hyphens and `+` without client-side stripping
- [ ] Error messages echo what the parser understood
- [ ] libphonenumber version pinned and on a scheduled update, given the one-to-three-week metadata cadence
