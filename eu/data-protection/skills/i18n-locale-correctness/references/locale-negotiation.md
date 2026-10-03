# Locale negotiation and regional variants

Authoritative basis: BCP 47 (RFC 5646 language tags, RFC 4647 matching); the IANA Language Subtag Registry; CLDR 48.2 likely-subtags data via `Intl.Locale`; ECMA-402 `localeMatcher`. Verified on Node 22.19.0 / ICU 77.1, 2026-08-05.

## Tag structure

`language[-script][-region][-variant][-extension]`, matched case-insensitively but conventionally written `de-Latn-AT`: language lower-case, script title-case, region upper-case.

| Subtag | Answers | Example |
|---|---|---|
| language | which language | `de`, `zh`, `sr` |
| script | which writing system | `Hans`, `Hant`, `Latn`, `Cyrl` |
| region | which country's conventions | `AT`, `CH`, `TW` |
| extension `-u-` | Unicode preferences | `-u-co-phonebk`, `-u-ca-buddhist`, `-u-nu-arab` |

Only include a subtag that carries information. `de-Latn-AT` is noise; `de-AT` is the tag. `sr-Latn` and `sr-Cyrl` are not noise — they are the two scripts Serbian is actually written in, and CLDR defaults Serbian to Cyrillic (verified: `new Intl.Locale('sr').maximize()` is `sr-Cyrl-RS`).

Canonicalisation is available and strict:

```js
Intl.getCanonicalLocales(['DE-at','de-DE-u-co-phonebk','zh-hant-tw','EN-gb'])
// ['de-AT', 'de-DE-u-co-phonebk', 'zh-Hant-TW', 'en-GB']

Intl.getCanonicalLocales(['en_US'])   // RangeError — underscores are not BCP 47
```

Verified. POSIX-style tags (`en_US`, `de_AT.UTF-8`) come out of operating systems and out of gettext pipelines and are not valid BCP 47. Convert before they reach `Intl`.

## Likely subtags

CLDR's likely-subtags data fills in what a tag leaves out. Verified via `Intl.Locale#maximize()`:

| Input | Maximised |
|---|---|
| `de` | `de-Latn-DE` |
| `de-AT` | `de-Latn-AT` |
| `zh` | `zh-Hans-CN` |
| `zh-TW` | `zh-Hant-TW` |
| `sr` | `sr-Cyrl-RS` |
| `pt` | `pt-Latn-BR` |
| `en` | `en-Latn-US` |
| `az` | `az-Latn-AZ` |

Two things this tells you. **`zh` alone means Simplified Chinese for mainland China** — serving Traditional Chinese users a `zh` bundle gives them the wrong script. And **`pt` alone means Brazilian Portuguese**, not European Portuguese, which surprises European teams who write `pt` meaning Portugal.

`minimize()` goes the other way: `zh-Hant-TW` → `zh-TW`. Use it to shorten a tag for a URL without losing information.

## `Accept-Language`

```
Accept-Language: de-AT,de;q=0.9,en-GB;q=0.8,en;q=0.7
```

Rules for using it:

- It is a **hint from the browser's settings**, not a decision. A user on a borrowed laptop, in an office with a locked-down image, or travelling has the wrong value.
- Parse the `q` values and honour the order. A parser that takes the first tag and stops is wrong for the very users who set a preference list.
- Never geolocate by IP to pick a language. A German speaker in Vienna and an English speaker in Vienna both resolve to Austria; only one of them wants German.
- **Always offer a visible language switcher** and persist the choice (cookie or user record). Once the user has chosen, `Accept-Language` is irrelevant and must not override.

## Matching algorithms

RFC 4647 defines two, and ECMA-402 exposes the corresponding `localeMatcher` values:

- **Lookup** (`localeMatcher: 'lookup'`): truncate the requested tag from the right until something matches. `de-AT` → `de-AT`, else `de`, else the default. Deterministic, and what you want for your own message bundles.
- **Best fit** (`'best fit'`, the ECMA-402 default): implementation-defined. It may return something you did not expect, including a locale you do not have translations for.

For `Intl` formatting, `'best fit'` is usually right — you want the platform's best rendering. For **your own translation bundles**, implement lookup yourself and be explicit about the fallback chain:

```js
/**
 * @param {string[]} requested  parsed from Accept-Language, q-ordered
 * @param {string[]} available  tags you actually have bundles for
 * @param {string}   fallback   the default bundle
 */
export function negotiate(requested, available, fallback) {
  const have = new Map(available.map(t => [t.toLowerCase(), t]));
  for (const tag of requested) {
    const parts = tag.toLowerCase().split('-');
    while (parts.length) {
      const hit = have.get(parts.join('-'));
      if (hit) return hit;
      parts.pop();
    }
  }
  return fallback;
}
negotiate(['de-AT','de','en'], ['de','en','fr'], 'en');   // 'de'
negotiate(['de-AT'],           ['de-AT','de'],   'en');   // 'de-AT'
```

**Separate the two locales.** The *content* locale (which translation bundle) and the *formatting* locale (which number, date and collation conventions) are not the same choice. A user reading the German bundle in Switzerland wants German text with Swiss number formatting: bundle `de`, formatting `de-CH`. Keep two values.

## Fallback chains that actually work

```
de-AT  →  de  →  en          (message bundles)
de-AT  →  de-AT             (formatting: never fall back, Intl handles it)
```

- Fall back **only for message bundles**. Never fall back for formatting — pass the full tag to `Intl` and let ICU resolve it. Verified: `Intl.NumberFormat.supportedLocalesOf(['de-AT','de-CH'], {localeMatcher:'lookup'})` returns both.
- A missing key in a regional bundle falls through to the base language, then to the source language. A missing key must never render the key itself to a user.
- **Test the fallback path in CI.** Delete a random 10 % of keys from a locale file and confirm the page still renders sentences, not identifiers.

## `de-AT`, `de-CH` and `de-DE`

One language, three sets of conventions. All verified.

| | `de-DE` | `de-AT` | `de-CH` |
|---|---|---|---|
| January | `Januar` | **`Jänner`** | `Januar` |
| Number `1234567.89` | `1.234.567,89` | `1 234 567,89` (U+00A0) | `1’234’567.89` (U+2019) |
| Currency `1234.50` | `1.234,50 €` (symbol last) | `€ 1.234,50` (symbol **first**) | `CHF 1’234.50` |
| Short date | `15.01.26` | `15.01.26` | `15.01.26` |
| `ß` | used | used | **not used — written `ss`** |
| Currency | EUR | EUR | CHF |

The Swiss `ß` rule is orthographic, not a casing rule: Swiss Standard German writes `Strasse`, `Grüsse`, `heissen`. You cannot generate it by transforming a German string, because `Maße` (measurements) and `Masse` (mass) are different words that both become `Masse` in Swiss spelling. It has to be a separate translation file.

Note also that `de-AT` differs from `de-DE` on a long list of everyday vocabulary that a translation memory will not catch — `Jänner`/`Januar`, `Februar`/`Feber` (older AT usage), `Sackerl`/`Tüte`, `Erdäpfel`/`Kartoffeln`. If Austria is a real market, the German bundle needs an Austrian review pass, not just a locale tag.

Other regional pairs with the same shape of problem: `pt-PT`/`pt-BR` (different orthography and vocabulary), `es-ES`/`es-419` (Latin American Spanish; `419` is the UN M.49 region code), `en-GB`/`en-US`, `fr-FR`/`fr-CA`, `zh-Hans`/`zh-Hant`.

## URL strategies

| Strategy | Example | Verdict |
|---|---|---|
| Path prefix | `example.com/de-at/produkte` | **Default choice.** Crawlable, shareable, cacheable, one deployment |
| Subdomain | `de.example.com` | Works; costs certificate and cookie-scope complexity |
| ccTLD | `example.at` | Strong local signal, highest cost, ties language to country |
| Query parameter | `?lang=de` | Weak for SEO, caches badly |
| Cookie or header only | — | **Wrong.** The URL does not identify the content; a shared link opens in the wrong language |

With a path prefix:

- Use the **canonical tag** in the path (`/de-at/`, not `/at/` or `/german/`). Region-only paths break as soon as a country has two languages — Switzerland has four.
- Emit `hreflang` alternates for every locale of a page, plus `x-default`.
- Set `<html lang="de-AT">` to match the path.
- **Never auto-redirect based on `Accept-Language` or IP.** It breaks shared links, breaks crawlers, and traps the user who deliberately opened the English page. Offer a dismissible banner instead.
- Serve `Vary: Accept-Language` if content differs by header at any URL, or you will poison shared caches.

## Checkpoints

- [ ] All locale identifiers are canonical BCP 47; no underscores anywhere
- [ ] POSIX-style tags from the OS or gettext converted before reaching `Intl`
- [ ] Content locale and formatting locale are two separate values
- [ ] `Accept-Language` parsed with `q` ordering, not first-tag-wins
- [ ] An explicit user language choice persists and overrides `Accept-Language`
- [ ] No IP geolocation used to choose a language
- [ ] Message-bundle fallback chain implemented as lookup and tested with missing keys
- [ ] No fallback applied to formatting locales; full tags passed to `Intl`
- [ ] `zh` never used alone where Traditional Chinese is a market; `pt` never used alone meaning Portugal
- [ ] `de-CH` bundle is a separate file with `ss` throughout, not a transform of `de-DE`
- [ ] `de-AT` reviewed by an Austrian speaker, not assumed identical to `de-DE`
- [ ] Locale is in the URL path, using the canonical tag
- [ ] `hreflang` alternates and `x-default` emitted
- [ ] `<html lang>` matches the served locale
- [ ] No automatic redirect on `Accept-Language` or IP
- [ ] `Vary: Accept-Language` set wherever content varies by header
