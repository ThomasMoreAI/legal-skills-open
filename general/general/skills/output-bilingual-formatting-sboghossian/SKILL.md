---
name: output-bilingual-formatting-sboghossian
title: Bilingual Formatting (Arabic–English)
description: Use when formatting a legal document, contract, or analysis that must appear in both Arabic and English — either as a two-column layout (for DOCX/PDF export) or as stacked bilingual sections (for chat/markdown). Covers RTL/LTR handling, Arabic punctuation rules, currency and numeral conventions, and the required controlling-language statement. Essential for MENA-jurisdiction drafting in the UAE, KSA, Lebanon, and Egypt.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/output/output-bilingual-formatting
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Bilingual Formatting (Arabic–English)

## When to use this

Use this skill whenever a legal output must be produced in both Arabic and English. This is not optional in many MENA contexts — it is a legal requirement:

- **UAE**: federal contracts involving government entities must be in Arabic. Many commercial contracts include both languages to serve Arabic-speaking and English-speaking parties.
- **KSA**: Arabic is the official language of contracts in Saudi Arabia. English versions are often provided for international parties.
- **Lebanon**: contracts may be in Arabic, French, or English; bilingual documents often include Arabic + French or Arabic + English.
- **Egypt**: official language is Arabic; bilingual is common in international commercial practice.
- **DIFC / ADGM**: English is the official language; Arabic is not required but may be provided for client-facing documents.

## Format options

### Option A — Two-column table (best for DOCX and PDF export)

Use a full-width table with two equal columns. Left column: English. Right column: Arabic.

```
| English                          | عربي                              |
|----------------------------------|-----------------------------------|
| Article 1. Definitions           | المادة 1. التعريفات               |
| "Agreement" means this contract  | "الاتفاقية" تعني هذا العقد        |
```

**Requirements for two-column layout:**
- Set the right column's text direction to RTL in the document properties.
- Ensure the Arabic column uses a Unicode-compatible Arabic font (e.g., Traditional Arabic, Scheherazade, or Arial for Arabic on Windows).
- Article numbers appear in both columns — use Western Arabic digits (1, 2, 3) in both columns as they render correctly in bidirectional text.

**When to use**: formal contracts intended for printing or PDF distribution. Preferred by UAE government entities and international law firms.

### Option B — Stacked bilingual (better for chat / markdown / web)

For each clause, display the English text first, then the Arabic translation immediately below it, under a mirrored heading:

```markdown
## Article 1. Definitions

"Agreement" means this Non-Disclosure Agreement dated [date].

## المادة 1. التعريفات

"الاتفاقية" تعني اتفاقية عدم الإفصاح هذه المؤرخة في [التاريخ].
```

**When to use**: chat output, markdown rendering, inline review, or any context where a two-column table is not supported.

## RTL handling

### Numerals
Use **Western Arabic digits** (1, 2, 3 — not Eastern Arabic ١، ٢، ٣) in bilingual legal documents. Reasons:
- They are unambiguous across both text directions.
- They are standard practice in UAE and KSA commercial contracts.
- They avoid bidirectional rendering bugs in most word processors.

Exception: if the client or jurisdiction specifically requires Eastern Arabic digits (common in some KSA government documents), follow the client's instruction.

### Currency
Use **ISO currency codes** (AED, SAR, LBP, EGP, USD) rather than currency symbols. Symbols (especially $) render inconsistently in RTL contexts:
- AED is unambiguous; "د.إ" (the Arabic abbreviation) may render incorrectly in some environments.
- Write amounts as: "AED 100,000 (one hundred thousand UAE Dirhams / مئة ألف درهم إماراتي)"

### Punctuation
Arabic uses different punctuation characters. In the Arabic column/section, use:
- Arabic comma: `،` (U+060C) instead of `,`
- Arabic semicolon: `؛` (U+061B) instead of `;`
- Arabic question mark: `؟` (U+061F) instead of `?`
- Arabic period: `.` (same as English — standard practice in formal legal Arabic)

Do not mix Arabic and Western punctuation within the same Arabic paragraph.

### Parenthetical definitions
Arabic legal style often places the defined term in both languages:
> "المقاول" (أو "الطرف الثاني") يعني...

This is correct practice; preserve it in translations.

## Controlling-language statement

Every bilingual document must include a controlling-language clause. Place it:
- At the end of the preamble (before Article 1), or
- As a standalone article (often Article 2 or "Interpretation")

Standard formulation:
> *In the event of any conflict between the Arabic and English versions of this Agreement, the **[Arabic / English]** version shall prevail.*

> *في حالة وجود أي تعارض بين النسختين العربية والإنجليزية من هذه الاتفاقية، تسود النسخة **[العربية / الإنجليزية]**.*

**Which language controls:**
- UAE government contracts: Arabic controls.
- DIFC/ADGM: English controls (the governing law is English common law).
- Private commercial contracts: choose based on the dominant party's language and governing law. If governing law is UAE federal law, Arabic should control. If governing law is DIFC law or English law, English should control.
- When in doubt: use English controls, but flag this for the supervising lawyer to confirm.

## Common mistakes

| Mistake | Consequence | Correct approach |
|---------|-------------|-----------------|
| Inconsistent translation of defined terms | Term has two different meanings in the two language versions — creates ambiguity in dispute | Create a bilingual glossary of defined terms and apply consistently |
| Omitting the controlling-language clause | A court cannot determine which version governs in a conflict | Always include it |
| Using a machine translation without legal review | Arabic legal vocabulary is distinct from everyday Arabic; machine translation produces non-standard terms | Have a legally trained Arabic translator review the Arabic text |
| Mixing Eastern and Western Arabic numerals | Creates inconsistency and potential misreading of amounts | Standardize to Western Arabic digits throughout |
| Different article numbering in each version | Clauses cannot be cross-referenced | Number identically in both columns/sections |

## Related skills

- [[draft-bilingual-ar-en-side-by-side]] — the drafting skill for producing new bilingual contracts
- [[heuristic-bilingual-ar-en-mirror-clauses]] — clause-level mirroring heuristics for bilingual review
- [[output-docx-export-style]] — document structure rules for DOCX export that pairs with two-column bilingual layout
- [[output-client-letter-style]] — when the bilingual output is a client communication rather than a contract
