# Plurals, gender and message formatting

Authoritative basis: CLDR 48.2 plural rules via `Intl.PluralRules`; UTS #35 Part 9, MessageFormat 2.0 (`unicode.org/reports/tr35/tr35-messageFormat.html`, version 48.2, published as a **stable** document — "This is a stable document and may be used as reference material or cited as a normative reference by other specifications"). Verified on Node 22.19.0 / ICU 77.1, 2026-08-05.

## Plural categories are not two

CLDR defines six categories: `zero`, `one`, `two`, `few`, `many`, `other`. Which of them a language uses is data, not intuition. Verified with `new Intl.PluralRules(locale).resolvedOptions().pluralCategories`:

| Locale | Categories |
|---|---|
| `ja` | `other` — one form only |
| `en`, `de` | `one`, `other` |
| `fr` | `one`, `many`, `other` |
| `ro` | `one`, `few`, `other` |
| `sl` | `one`, `two`, `few`, `other` |
| `pl`, `ru`, `cs`, `lt` | `one`, `few`, `many`, `other` |
| `ar`, `cy` | `zero`, `one`, `two`, `few`, `many`, `other` — all six |

And the selection is not what an English speaker guesses. Verified:

```js
[1, 2, 5, 21].map(n => new Intl.PluralRules('ru').select(n))
// ['one', 'few', 'many', 'one']            ← 21 is 'one' in Russian

[2, 5, 22].map(n => new Intl.PluralRules('pl').select(n))
// ['few', 'many', 'few']

[0, 1, 2, 3, 11, 100].map(n => new Intl.PluralRules('ar').select(n))
// ['zero', 'one', 'two', 'few', 'many', 'other']
```

So `count === 1 ? singular : plural` is wrong for Russian at 21, wrong for Polish at 22, wrong for Arabic at 0, 2, 3, 11 and 100, and produces a redundant second string for Japanese. `count === 0` special-casing is a separate English habit that fights the `zero` category where it exists.

**Ordinals are a separate rule set.** Verified: `new Intl.PluralRules('en', { type: 'ordinal' })` selects `one`, `two`, `few`, `other`, `other` for 1, 2, 3, 4, 11 — that is `1st`, `2nd`, `3rd`, `4th`, `11th`. A suffix table indexed by `n % 10` gets `11th` wrong.

## Never concatenate

```js
// WRONG — three separate strings; word order, plural form and gender are all lost
t('You have') + ' ' + count + ' ' + (count === 1 ? t('message') : t('messages'));

// WRONG — the translator sees a fragment with no context
`${t('deleted')} ${itemName}`;
```

German puts the verb at the end. Japanese puts the object before the verb. Arabic reverses the whole phrase. A translator handed `"You have"` and `"messages"` as separate strings cannot produce a correct sentence in any of them, and no amount of care at the call site fixes it.

**One message per sentence, with the placeholders inside it.** The unit of translation is a complete utterance in a known context.

## MessageFormat 2.0

MF2 is a stable Unicode specification (UTS #35 Part 9, version 48.2). Its syntax:

```
.input {$count :number}
.match $count
one {{You have {$count} notification.}}
*   {{You have {$count} notifications.}}
```

- `.input` declares and annotates a variable (here as a number, which makes the plural selector available).
- `.match` opens a selector.
- Each variant's key is a plural category, and `*` is the mandatory catch-all.
- The pattern body is delimited by `{{ … }}`.

A Polish translation of the same message simply supplies more variants:

```
.input {$count :number}
.match $count
one  {{Masz {$count} powiadomienie.}}
few  {{Masz {$count} powiadomienia.}}
many {{Masz {$count} powiadomień.}}
*    {{Masz {$count} powiadomienia.}}
```

The source string never changes. That is the whole point: the message file for each locale carries as many variants as that language needs, and the calling code passes `{ count }` and nothing else.

Legacy ICU MessageFormat 1 syntax (`{count, plural, one {…} other {…}}`) remains what most tooling emits today. `[[UNVERIFIED: the state of MF2 support in specific runtimes and TMS products as at 2026-08-05 — check your library before migrating]]`. If your pipeline is on MF1, keep it; the rule that matters is one message per sentence with a plural selector, not which syntax expresses it.

## Selecting a plural form without a message library

```js
const pr = new Intl.PluralRules(locale);
const forms = {                       // supplied per locale by the translation file
  one:  'Sie haben {count} Nachricht.',
  other:'Sie haben {count} Nachrichten.',
};
const template = forms[pr.select(count)] ?? forms.other;
const text = template.replace('{count}', new Intl.NumberFormat(locale).format(count));
```

Two details that get skipped: the fallback to `other` is mandatory because a locale file may not carry every category, and the number itself must go through `Intl.NumberFormat` — otherwise `1234` appears as `1234` in a German sentence where the rest of the UI shows `1.234`.

## Gender and grammatical agreement

`Intl.PluralRules` does not handle gender. Where a message's wording depends on the gender of a subject, the message file needs a selector on a gender variable, and the caller must supply it:

```
.match $userGender
feminine {{{$name} hat ihre Bestellung storniert.}}
masculine {{{$name} hat seine Bestellung storniert.}}
*        {{{$name} hat die Bestellung storniert.}}
```

Two rules:

- **The catch-all must be a real, usable sentence**, not a masculine default. It is the form used for unknown, unspecified and non-binary values, and in most languages a neutral rephrasing exists.
- **Never derive gender from a name or from a title.** Ask, allow "prefer not to say", and make the neutral form good enough that nobody has to answer.

Beyond gender, many languages inflect the interpolated value itself. Slavic month names change case with context (see `dates-and-times.md`); Slavic and Baltic given names decline. CLDR's person-name data carries `-genitive` and `-vocative` modifiers for exactly this. If a message needs an inflected form, it needs a separate message, not a clever runtime transformation.

## Text expansion

Translations are longer than English, and the difference lands on fixed-width controls.

- German and French are the usual offenders in a European product: compounds and articles both add length, and German compounds cannot be hyphenated by the browser without a correct `lang` attribute.
- The shortest strings expand the most in relative terms — a button labelled `Save` becomes `Speichern`, `Enregistrer`, `Guardar cambios`.
- `[[UNVERIFIED: specific expansion percentage tables (the "+30% for German" figure) — treat them as folklore and test with real translations instead]]`

Practical rules that do not depend on a percentage:

- No fixed widths on buttons, tabs, labels or table headers. Let content size them, with a `min-width` for touch targets.
- No text baked into images.
- No layouts that break when a label wraps to two lines — test with the longest translation you have.
- Test with a pseudo-locale that doubles string length and adds accents, so the failure shows up before translation, not after.

## Working with the message catalogue

- **Keys are semantic, not literal.** `checkout.button.submit`, not `Zahlungspflichtig bestellen`. A literal key changes when the English copy changes and orphans every translation.
- **Every message carries a description for the translator.** "Button label at the end of the checkout flow. Must express that the order is binding." Without it the translator guesses, and a one-word string has no context at all.
- **Never interpolate HTML into a translated string** as a fragment. Pass the whole marked-up message and let the renderer substitute components, so the translator can move the link inside the sentence.
- **Numbers, dates and currency go through `Intl`**, then into the message as an already-formatted string. Never format them inside the translation file.
- **Pseudo-localise in CI.** A build that renders `[Šàvé çhàngéš————]` catches untranslated strings, concatenation and fixed widths in one pass.

## Checkpoints

- [ ] No `count === 1 ? a : b` anywhere; plural selection goes through `Intl.PluralRules` or the message format
- [ ] Every message with a count has variants for all categories the target locale uses, plus a catch-all
- [ ] Ordinal suffixes use `type: 'ordinal'`, not `n % 10`
- [ ] No sentence assembled by concatenating translated fragments
- [ ] One message per complete sentence, with placeholders inside it
- [ ] Every message key is semantic and carries a translator description
- [ ] Gendered messages have a usable neutral catch-all and gender is asked, never inferred
- [ ] Numbers, dates and currency formatted with `Intl` before entering a message
- [ ] No HTML fragments passed through the translation layer
- [ ] No fixed widths on controls carrying translated text
- [ ] No text rendered inside images
- [ ] Pseudo-localisation runs in CI and the build is checked against it
- [ ] Layout tested with the longest available translation, not with English
