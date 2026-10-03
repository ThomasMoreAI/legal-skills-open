# Text: length, truncation, direction, line breaking

Authoritative basis: the Unicode Standard 17.0.0 (2025-09-09); UAX #29 (text segmentation) via `Intl.Segmenter`; UAX #9 (bidirectional algorithm); CSS Text Level 3 for line breaking. Verified on Node 22.19.0 / ICU 77.1, 2026-08-05.

## Three different lengths

The same visible character has three different lengths and every one of them is used somewhere in your stack.

| String | Bytes (UTF-8) | UTF-16 units (`.length`) | Grapheme clusters |
|---|---|---|---|
| `a` | 1 | 1 | 1 |
| `ä` | 2 | 1 | 1 |
| `日` | 3 | 1 | 1 |
| `👍🏽` | 8 | 4 | 1 |
| `👨‍👩‍👧‍👦` | 25 | 11 | 1 |
| `🇦🇹` | 8 | 4 | 1 |
| `நி` | — | 2 | 1 |
| `ȩ́` (e + 2 combining) | — | 3 | 1 |

All verified. Which one applies:

- **Bytes** — database column limits (`VARCHAR(n)` in some engines), HTTP headers, cookie sizes, filesystem name limits.
- **UTF-16 units** — JavaScript `.length`, `maxlength` in HTML, `slice`, `substring`, and most regex offsets.
- **Grapheme clusters** — what the user counts. This is the only correct unit for a "maximum 50 characters" rule shown to a human.

A `VARCHAR(50)` on a name column means 50 bytes in some engines and 50 characters in others, and in neither case does it mean what the label "50 characters" tells the user.

## Truncation

Naive slicing splits characters. Verified: `'👨‍👩‍👧‍👦👍🏽abc'.slice(0, 3)` produces `'👨‍'` — half a family plus a zero-width joiner, which renders as a lone man emoji or a replacement box.

```js
export function truncateGraphemes(str, max, locale = 'en') {
  const seg = new Intl.Segmenter(locale, { granularity: 'grapheme' });
  const out = [];
  for (const { segment } of seg.segment(str)) {
    if (out.length >= max) return out.join('') + '…';
    out.push(segment);
  }
  return out.join('');
}
truncateGraphemes('👨‍👩‍👧‍👦👍🏽abc', 3);  // '👨‍👩‍👧‍👦👍🏽a…'
```

`Intl.Segmenter` is available in all current browsers and in Node 13+; verified present on Node 22 (`typeof Intl.Segmenter === 'function'`). There is no reason to ship a hand-written grapheme regex.

Prefer CSS for visual truncation (`text-overflow: ellipsis`) — it truncates at the rendered width, which is what actually matters, and it does not corrupt the underlying string.

## Length validation

```js
const graphemeCount = (s, locale = 'en') =>
  [...new Intl.Segmenter(locale, { granularity: 'grapheme' }).segment(s)].length;
```

- Validate the **grapheme count** against the limit you show the user.
- Size the **column** by bytes with generous headroom: a 50-grapheme limit can be 200+ bytes in Devanagari or with emoji. Prefer `text` over `VARCHAR(n)` where the engine allows it.
- Never use `maxlength` as the real limit; it counts UTF-16 units and can cut a name mid-character. Set it high and enforce the grapheme count server-side.

## Word and sentence segmentation

Thai, Lao, Khmer, Burmese, Japanese and Chinese do not put spaces between words. `str.split(' ')` returns one token for an entire Thai sentence. Verified:

```js
[...new Intl.Segmenter('th', { granularity: 'word' }).segment('ภาษาไทยไม่มีช่องว่าง')]
  .filter(s => s.isWordLike).map(s => s.segment)
// ['ภาษา','ไทย','ไม่มี','ช่อง','ว่าง']

[...new Intl.Segmenter('ja', { granularity: 'word' }).segment('日本語のテキストです')]
  .filter(s => s.isWordLike).map(s => s.segment)
// ['日本語','の','テキスト','です']
```

Consequences: a word-count feature, a "first N words" excerpt, a search tokeniser and a reading-time estimate are all wrong for a quarter of the world if they split on whitespace. Sentence granularity also handles abbreviations — verified, `'Dr. Smith went home. He slept.'` segments into `['Dr. ', 'Smith went home. ', 'He slept.']` rather than breaking after `Dr.`.

## Bidirectional text

Arabic, Hebrew, Persian and Urdu run right to left. The Unicode bidirectional algorithm resolves direction from the characters themselves, which means an interpolated variable can reorder the text around it. A file name in Hebrew inserted into an English sentence can push the trailing punctuation to the wrong end of the line.

Two fixes, both required:

**In HTML**, mark the direction and isolate the interpolation:

```html
<html lang="ar" dir="rtl">

<!-- an interpolated value of unknown direction -->
<p>File: <bdi>{{ filename }}</bdi> (2026)</p>
```

`<bdi>` isolates the enclosed run so it cannot affect the surrounding order. `dir="auto"` on an input or a cell does the same for user-entered content. Never set `dir` once on `<body>` and assume it covers user data.

**In plain strings** (emails, PDFs, SMS, log lines) use the isolate characters: U+2068 FIRST STRONG ISOLATE before, U+2069 POP DIRECTIONAL ISOLATE after. Verified codepoints.

```js
const FSI = '⁨', PDI = '⁩';
const line = `File: ${FSI}${userValue}${PDI} (2026)`;
```

Do **not** use the deprecated embedding characters U+202A–U+202E; the isolates are the current mechanism and they nest correctly.

Layout, not just text: in an RTL locale the whole interface mirrors. Use CSS logical properties (`margin-inline-start`, `padding-inline-end`, `inset-inline-start`, `border-start-start-radius`) rather than `left`/`right`, and `text-align: start`/`end` rather than `left`/`right`. Icons that indicate direction (back arrows, progress) mirror; icons that depict objects (a clock, a logo) do not.

## CJK line breaking

Chinese, Japanese and Korean text wraps between characters, not at spaces, and the rules about which characters may start or end a line are non-trivial (a line may not start with a closing bracket or a small kana, may not end with an opening bracket).

```css
:lang(ja), :lang(zh) {
  line-break: strict;        /* apply the full kinsoku rules */
  overflow-wrap: normal;
}
:lang(ko) {
  word-break: keep-all;      /* Korean has spaces; do not break inside a word */
  overflow-wrap: break-word;
}
```

- `line-break: strict | normal | loose | anywhere` controls how aggressively CJK breaks are taken.
- `word-break: keep-all` is specifically for Korean, which does use spaces but whose eojeol should not be split.
- Never apply `word-break: break-all` globally to "fix overflow". It breaks Latin words mid-syllable and produces unreadable German compounds.
- `hyphens: auto` with a correct `lang` attribute is the right fix for long German compounds; it needs the language declared to load the right hyphenation dictionary.

## The `lang` attribute

Set `lang` on `<html>` and on any element whose content is in another language. It drives hyphenation, line breaking, font selection (a Han character renders differently in `zh-Hans`, `zh-Hant` and `ja`), quotation marks, and screen-reader voice selection. An unset or wrong `lang` produces the wrong glyph shapes for CJK and the wrong pronunciation for every assistive technology.

```html
<html lang="de-AT">
  …
  <blockquote lang="fr">…</blockquote>
```

## Checkpoints

- [ ] User-facing length limits counted in grapheme clusters via `Intl.Segmenter`
- [ ] Database columns sized in bytes with headroom, or `text`
- [ ] No `slice`/`substring`/`substr` used to truncate user-visible text
- [ ] `maxlength` set generously and not treated as the real limit
- [ ] Word counts, excerpts and tokenisers use `Intl.Segmenter` word granularity, not `split(' ')`
- [ ] Thai or Japanese text tested through any word-splitting feature
- [ ] `<html lang>` set correctly and per-element `lang` used for embedded other-language content
- [ ] `dir="rtl"` set for RTL locales and `<bdi>` or `dir="auto"` around every interpolated user value
- [ ] Plain-text interpolations wrapped in U+2068 / U+2069, not the deprecated embedding characters
- [ ] CSS uses logical properties throughout; no bare `left`/`right` in layout
- [ ] Directional icons mirror in RTL; object icons do not
- [ ] `line-break`/`word-break` set per language; no global `word-break: break-all`
- [ ] `hyphens: auto` enabled where German or another compounding language is a target
