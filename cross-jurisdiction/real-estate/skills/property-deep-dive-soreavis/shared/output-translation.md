# Output translation — `--lang` and `--lang-scope`

The skill emits its reports in English by default. Operators who serve non-English audiences (a French buyer reading a Greek property brief; a Japanese investor reading a Portugal brief) can request a translation of all or part of the output via two flags.

**Canonical truth**: English remains the source of truth — the anti-hallucination contract is verified against English-language sources and English-language renderings. Translations are **additional artifacts** emitted alongside or in place of English per operator choice. **The translation never re-translates the foreign-language preservation tokens** (per `shared/foreign-language-preservation.md`); native statute / regulator / document names stay in their original form.

---

## Flags

```
--lang=<iso639-1>            target language for translation (e.g. en, es, fr, de, it, pt, nl, ja, ko, zh, ar, he)
--lang-scope=<level>         translation scope; default = `detailed` when --lang is provided
```

### Examples

```
/property-deep-dive Lisboa 1100-001 --tax --home-tax --lang=ja --lang-scope=detailed
  → Japanese-language report (detailed scope), English remains canonical

/property-deep-dive Adriers 86430 --price --tax --lang=es --lang-scope=summary
  → English report + Spanish summary section appended (executive summary only)

/property-deep-dive 12 Rue de la Paix, 75002 Paris --all --lang=zh --lang-scope=bilingual
  → Side-by-side English | Chinese rendering

/property-deep-dive Berlin Mitte 10115 --visa --home-tax --lang=ko
  → Korean report (default scope: detailed)
```

---

## Scope levels (`--lang-scope=`)

Seven levels, ordered roughly by translation cost (cheapest first):

### `headings-only`
- Translate section headers + verdict bands (🟢/🟡/🟠/🔴 + one-line verdict).
- Body stays in English.
- Use case: a non-EN reader navigates to the right section in their language, then reads the body in EN.
- Token cost: ~3-5% of full translation.

### `summary`
- Translate the BLUF / executive summary (top-of-section verdict + 2-3 key facts).
- Body stays in English.
- Use case: a non-EN decision-maker reads the headline-level verdict in their language; their advisor reads the details in EN.
- Token cost: ~10% of full translation.

### `verdicts`
- Translate every verdict-band line + its one-line rationale.
- Skip methodology, tables, URLs, source-attribution.
- Use case: "should I walk away or proceed" reading.
- Token cost: ~15% of full translation.

### `detailed` (DEFAULT when `--lang` is given)
- Translate main findings + verdicts + tables.
- Skip methodology / anti-hallucination scaffolding / native-term preservation glosses / primary URLs.
- Native statutes / regulators / document forms stay in their original form (per preservation policy).
- Use case: full report for a non-EN buyer who wants substance without scaffolding.
- Token cost: ~70% of full translation.

### `full`
- Translate everything EXCEPT:
  - Primary-source URLs (always preserved in original)
  - Native legal terms / statute names / regulator names (per preservation policy)
  - ISO codes / country codes / currency ISO codes
- Use case: handoff to a local lawyer who wants every word translated.
- Token cost: ~95% of full translation.

### `bilingual`
- Emit BOTH English AND target language, either:
  - Two-column side-by-side (preferred for short reports)
  - Sequential blocks: ENGLISH section, then translated section, then next English section
- Use case: bilingual handoff (operator → local attorney; documentation for both parties).
- Token cost: ~180% of full translation (both languages emitted).

### `glossary-only`
- Emit just a **native-term → target-language explanation appendix** at the end of the EN report.
- The body stays in English.
- Use case: an EN-reader who wants to look up the native terms in their language (e.g., reading a Portugal brief in EN but needs to explain the Portuguese terms to a Brazilian colleague).
- Token cost: ~5-10% of full translation.

---

## Priority language pairs

Ranked by foreign-buyer cohort size (from the `--home-tax` research). The skill should provide highest-quality translation for these targets:

| ISO 639-1 | Language | Primary cohort | Notes |
|---|---|---|---|
| `es` | Spanish | LATAM + EU + 55M+ residents in ES | Use **es-ES** for European buyers; **es-419** for LATAM if specified |
| `fr` | French | EU + LATAM + Africa | Default to **fr-FR**; Quebec terms differ slightly |
| `de` | German | DACH (DE/AT/CH) | Note Swiss German vocabulary differences (e.g., Velo vs Fahrrad) |
| `it` | Italian | Italian residents + diaspora | Standard Italian (no regional variants in scope) |
| `pt` | Portuguese | Brazil + Portugal | Use **pt-BR** vs **pt-PT** if specified; default pt-PT for EU contexts |
| `nl` | Dutch | NL + BE Flemish | |
| `ja` | Japanese | Japan | Use polite/formal register (です/ます); native statute names in 漢字 |
| `ko` | Korean | South Korea | Use formal register (합쇼체); native statute names in 한자 / 한글 |
| `zh` | Chinese | CN + TW + HK + SG | Default to **zh-Hans** (simplified) for CN/SG; **zh-Hant** for TW/HK if specified |
| `ar` | Arabic | GCC + MENA | Modern Standard Arabic (MSA); right-to-left rendering required |
| `he` | Hebrew | Israel + Olim cohort | Native Modern Hebrew; right-to-left rendering required |

For any other ISO 639-1 code, the skill attempts best-effort translation but Confidence drops to MEDIUM.

---

## Native-term preservation (CRITICAL)

The translation MUST follow `shared/foreign-language-preservation.md`:

**A translated report keeps the original-language native term verbatim. The translation gloss adapts to the target language.**

### Example — Jersey playbook translated to German (`--lang=de --lang-scope=detailed`)

```
ORIGINAL (EN):
The High-Value Resident regime (HVR / 2(1)(e)) requires £250k/yr minimum tax under
the Control of Housing and Work (Jersey) Law 2012. Property thresholds: £3.5m for
houses, £1.75m for apartments.

CORRECT TRANSLATION (DE):
Das High-Value-Resident-Regime (HVR / 2(1)(e)) erfordert mindestens £250 Tsd./Jahr
an Steuern gemäß dem `Control of Housing and Work (Jersey) Law 2012`. Immobilien-
Schwellenwerte: £3,5 Mio. für Häuser, £1,75 Mio. für Wohnungen.

WRONG TRANSLATION (DE):
Das Hochwertige-Einwohner-Regime erfordert mindestens £250.000 pro Jahr an
Steuern gemäß dem Gesetz über Wohnungswesen und Arbeit (Jersey) 2012.
```

The wrong version translates the statute's name. A German-speaking reader trying to look up the act on `jerseylaw.je` will not find "Gesetz über Wohnungswesen und Arbeit" — only `Control of Housing and Work (Jersey) Law 2012` exists in the registry.

### Example — Greenland playbook translated to Spanish (`--lang=es`)

```
ORIGINAL (EN):
The `Inatsisartutlov nr. 78 af 21. november 2025 om erhvervelse af adkomst eller
brugsret til fast ejendom` (Greenlandic Parliament Act No. 78 of 21 November 2025
on the acquisition of ownership or right of use of real property) is the operative
foreign-buyer statute, effective 1 January 2026.

CORRECT TRANSLATION (ES):
La `Inatsisartutlov nr. 78 af 21. november 2025 om erhvervelse af adkomst eller
brugsret til fast ejendom` (Ley nº 78 de 21 de noviembre de 2025 del Parlamento
Groenlandés sobre adquisición de propiedad o derecho de uso de bienes inmuebles)
es la ley operativa para compradores extranjeros, vigente desde el 1 de enero
de 2026.
```

The native (Greenlandic-Danish) statute name is preserved verbatim; the Spanish translation is provided as the gloss in parentheses.

---

## Output format

### Default emission (no `--lang`)

```
[English report]
```

### `--lang=<lang>` without scope (default `detailed`)

```
[Translated report in target language, native terms preserved per policy]
[Footer: "Source-of-truth: English. Translation is non-canonical artifact."]
```

### `--lang=<lang> --lang-scope=bilingual`

```
[EN section 1]   |   [translated section 1]
[EN section 2]   |   [translated section 2]
...
```

OR (if narrow terminal):

```
=== English ===
[EN section 1]
=== <Target language> ===
[translated section 1]
=== English ===
[EN section 2]
=== <Target language> ===
[translated section 2]
```

### `--lang=<lang> --lang-scope=glossary-only`

```
[English report]

## Glossary (<target language>)

| Native term | EN gloss | <Target language> gloss |
|---|---|---|
| `Code civil Art. 682` | French Civil Code Article 682 | <target translation> |
| `Naalakkersuisut` | Government of Greenland | <target translation> |
| ...
```

---

## Confidence + translation quality

The skill's output Confidence tier (HIGH / MEDIUM / LOW) reflects the **English** report's underlying primary-source quality. Translation introduces a second axis:

- **Translation accuracy**: HIGH for the priority language pairs above; MEDIUM for other ISO 639-1 codes; LOW if the operator requests a language the skill cannot reliably handle (e.g., low-resource languages).
- **Preservation compliance**: HIGH if every native term is preserved per the policy; MEDIUM if some are translated; the translation fails the contract if a single statute / regulator name is rendered into the target language without the native original.

The translated report's footer must include:
- Source-of-truth declaration: "Canonical English report at <path>; translation is non-canonical."
- Translation date stamp.
- Confidence tier for translation accuracy + preservation compliance.

---

## Anti-hallucination integration

The translation must NOT introduce claims absent from the English source. Specifically:

1. **No invented facts** during translation — if the EN report says "£250k/yr minimum tax" and the translator can't render "/yr" cleanly in the target language, the translator picks an equivalent ("£250k jährlich" / "£250 000 par an") rather than inventing context.
2. **No paraphrase that changes meaning** — direct quotes stay literal; statute names stay verbatim.
3. **No translation of numbers** — `£3.5m` becomes `£3,5 Mio.` (German thousand-separator) but not `~3.5 million pounds` (which loses precision).
4. **No removal of confidence labels / verify flags** — every `verify at <URL>` flag and `Confidence: MEDIUM` label in the EN source must appear in the translation.

---

## Implementation

The translation is performed **in-prompt by Claude at output time**, not via an external API. This:

- Preserves the anti-hallucination context (Claude has seen the source data + applies the policy).
- Avoids external-API dependencies (no DeepL/Google-Translate keys required).
- Costs more tokens but keeps the policy enforceable.

The operator-chosen target language is appended to the output-mode instructions; the skill emits the report directly in the requested language.

---

## Examples

### Example 1 — French buyer reads Greek property brief (summary in French)

```
/property-deep-dive Athens 10556 --tax --home-tax --lang=fr --lang-scope=summary
```

→ Full English report + French executive-summary section appended (the BLUF + top verdicts).

### Example 2 — Bilingual handoff for German lawyer

```
/property-deep-dive 12 Rue de la Paix, 75002 Paris --notary --finance --lang=de --lang-scope=bilingual
```

→ Side-by-side English | German, with French statute names (Code civil, Loi 65-557, etc.) preserved verbatim in both columns.

### Example 3 — Japanese investor wants full Portuguese-rules translation

```
/property-deep-dive Lisboa 1100-001 --all --lang=ja --lang-scope=full
```

→ Full Japanese-language report. Portuguese statute names (Código Civil, AT-IRS, etc.) preserved verbatim with Japanese glosses in parentheses. Primary URLs unchanged.

### Example 4 — English-reader wants glossary of Greenlandic terms

```
/property-deep-dive Nuuk 3900 --foreign-buyer --notary --lang=es --lang-scope=glossary-only
```

→ Full English report. Glossary appendix in Spanish: each Greenlandic + Danish native term mapped to its Spanish explanation.

---

## What's NOT supported

- **Translating the source data itself** — the skill reads source materials in their native language; the translation layer only translates the OUTPUT.
- **Multi-target translation in one call** — one `--lang` per invocation. For two target languages, run twice.
- **Translation of native legal terms** — per preservation policy, native statute / regulator / document names stay in their original form.
- **Real-time language detection of the input** — the operator must specify `--lang`; auto-detection would risk hallucination.

---

## Status

Last refreshed: 2026-05-27.
**Confidence**: HIGH (feature spec; implementation deferred until first operator request).
Translation is opt-in; no behavioural change to existing English-default emission.
