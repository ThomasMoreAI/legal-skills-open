---
name: draft-bilingual-ar-en-side-by-side-sboghossian
title: Bilingual Arabic-English Side-by-Side Drafting
description: Use when a legal document must be drafted in both Arabic and English with parallel clause numbering and a controlling-language declaration. Governs layout choices (two-column table vs sequential), the RTL/LTR rendering rules, controlling-language conventions by jurisdiction (Arabic controls onshore in UAE/KSA/LB; English controls in DIFC/ADGM if stated), defined-term consistency, numeral and currency formatting, and translation quality standards for legal-register Arabic.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-bilingual-ar-en-side-by-side
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Bilingual Arabic-English Side-by-Side Drafting

## When to use this

Use this skill whenever a legal document must be produced in both Arabic and English and both versions will be legally operative. This is required or strongly expected in:
- Onshore UAE contracts involving local parties (Arabic often primary language required by courts).
- KSA contracts: Arabic is the only legally recognized version before Saudi courts.
- Lebanese commercial contracts: Arabic or French; bilingual Arabic-English common for international parties.
- Employment contracts in all GCC countries: Arabic required for labor authority filings.
- Government contracts in all MENA jurisdictions: Arabic mandatory.
- Bilingual DIFC/ADGM contracts where one party is Arabic-preferring: English controls but Arabic translation is offered for courtesy or commercial comfort.

## Layout choices

### Option A: Two-column table (preferred for shorter documents)

```
| العربية (Arabic)                        | English                                 |
|---|---|
| المادة الأولى: الأطراف                  | Article 1: Parties                      |
| [Arabic text of clause 1]               | [English text of clause 1]              |
| المادة الثانية: التعريفات               | Article 2: Definitions                  |
| [Arabic text]                           | [English text]                          |
```

- Arabic is displayed in the right column (RTL rendering); English in the left column (LTR).
- In Word/PDF: set Arabic text to right-to-left paragraph direction; use separate cells.
- Good for contracts up to ~15 pages.
- Disadvantage: tables become unwieldy for long schedules; page layout complexity in Word.

### Option B: Sequential clause-by-clause (preferred for longer documents)

Each clause appears twice: once in Arabic, then immediately below in English (or vice versa depending on convention — see below).

```
المادة الأولى: الأطراف
[Full Arabic text of Article 1]

Article 1: Parties
[Full English text of Article 1]

---

المادة الثانية: التعريفات
[Full Arabic text of Article 2]
...
```

- More legible for complex, long documents.
- Reviewers can read one language continuously.
- Numbering must be identical across the two versions.

### Convention for ordering
- **Lebanese convention**: Arabic first, English below (reflecting French/Arabic civil-law tradition where Arabic is primary).
- **DIFC/ADGM convention**: English first, Arabic below (reflecting common-law English primary).
- Confirm with the client's preference and the regulatory requirement for the specific document type.

## Controlling language — mandatory clause

Every bilingual agreement **must** contain an explicit controlling-language declaration. Without it, disputes arise over which version governs.

### UAE onshore (federal courts)
```
في حالة وجود تعارض بين النسختين العربية والإنجليزية من هذه الاتفاقية،
تسود النسخة العربية.

In the event of any conflict between the Arabic and English versions of this
Agreement, the Arabic version shall prevail.
```

### KSA
```
في حال وجود أي تعارض أو اختلاف في التفسير بين النصين العربي والإنجليزي،
يُعتمد النص العربي مرجعاً أساسياً.

In the event of any conflict or inconsistency in interpretation between the
Arabic and English texts, the Arabic text shall be the primary reference.
```

### DIFC / ADGM (English controls)
```
In the event of any conflict between the Arabic and English versions of this
Agreement, the English version shall prevail.

في حالة وجود أي تعارض بين النسختين العربية والإنجليزية من هذه الاتفاقية،
تسود النسخة الإنجليزية.
```

### Lebanon
```
في حال أي تعارض بين النصين العربي والإنجليزي لهذه الاتفاقية،
يسود النص العربي.

En cas de conflit entre les versions arabe et anglaise du présent Accord,
la version arabe prévaudra.

In the event of any conflict between the Arabic and English versions of
this Agreement, the Arabic version shall prevail.
```
(Lebanese practice sometimes incorporates a French version as well for civil-code formality.)

## Defined terms — critical rules

1. **Define once, in both languages**: each defined term must appear in both languages at its first definition.
   - English: `"Confidential Information"` (معلومات سرية)
   - Arabic: `"المعلومات السرية"` ("Confidential Information")
   - Use the Arabic term throughout the Arabic version; the English term throughout the English version.

2. **Never use English defined terms inside Arabic text**, and vice versa. This is the most common quality error in bilingual drafts.

3. **Legal concepts that do not translate directly**: some English common-law concepts (e.g., "liquidated damages," "implied warranty," "time of the essence") have no direct Arabic equivalent because they exist within a different legal tradition. In civil-law MENA jurisdictions, translate the concept by describing the underlying obligation:
   - "Liquidated damages" → تعويض اتفاقي مقدر مسبقاً (pre-agreed compensation)
   - "Implied warranty" → ضمان قانوني / ضمان ضمني
   - "Time of the essence" → الوقت هو جوهر الالتزام

## Numerals and currency

- **Arabic-Indic numerals (٠١٢٣٤٥٦٧٨٩)**: traditional in literary Arabic; used in formal contracts in KSA and LB.
- **Western Arabic numerals (0123456789)**: accepted in all MENA jurisdictions in commercial contracts; understood by all parties; less risk of transcription error.
- **Recommendation**: use Western Arabic numerals (0123456789) in both versions to eliminate discrepancy risk.
- **Currency**: always use the ISO code (USD, AED, SAR, LBP, EGP) — never the symbol ($ can be confused; ﷼ renders inconsistently across fonts). In Arabic text: write اليرو الأمريكي (USD) / الدرهم الإماراتي (AED) / الريال السعودي (SAR).
- **Amounts**: write amounts in both numerals and words in both versions:
  - English: "One Hundred Thousand United States Dollars (USD 100,000)"
  - Arabic: "مئة ألف دولار أمريكي (١٠٠،٠٠٠ دولار أمريكي)"

## Translation quality standards

Legal-register Arabic is not colloquial Arabic. The following are non-negotiable quality requirements:

| Requirement | Standard |
|---|---|
| **Register** | Formal Modern Standard Arabic (الفصحى); not Egyptian colloquial, not Gulf colloquial |
| **Legal terminology** | Use standard legal lexicon recognized by MENA bar associations; avoid calques from English |
| **Sentence structure** | Arabic contracts use noun phrases and عقود construction differently from English; do not word-for-word translate |
| **Consistency** | Same Arabic term for same English concept throughout the document |
| **Article definiteness** | العقد / الاتفاقية: use consistently; do not alternate |
| **Passive voice** | Arabic contracts often use passive voice more naturally than English |
| **Date format** | Arabic Hijri calendar (للاستخدام الرسمي في KSA) and Gregorian calendar; state both in KSA documents |

**Quality red flags** in Arabic legal drafts:
- English-origin words used without Arabic equivalents when Arabic exists.
- Mixture of formal and colloquial.
- Defined terms not matching between Arabic and English (different concept described).
- Clause numbers misaligned between the two versions.

## RTL/LTR rendering in Word

- Arabic text: set paragraph direction to RTL (Right-to-Left) in Microsoft Word.
- Headings in Arabic: use Arabic heading styles.
- Tables: Arabic column should be on the right in two-column side-by-side format.
- Page headers and footers: use separate Arabic-LTR-aware styles.
- Clause numbering: use Arabic-Indic ordinals in the Arabic version, or consistent Western numerals in both.

## Signing formalities

- In civil-law MENA jurisdictions (LB, UAE onshore, KSA): typically require a signature block in Arabic; signatories may need to initial each page.
- For KSA: Mawthq e-notarization platform accepts bilingual contracts; the Arabic version is authenticated.
- For LB: Tawqi3i e-notarization platform — see [[inst-tawqi3i-esignature-bridge]].
- For DIFC/ADGM: English signature block is sufficient; DocuSign accepted.

## Common mistakes

- **No controlling-language clause**: the single most dangerous omission in a bilingual contract.
- **Different defined terms in each version**: creates genuine legal ambiguity about the parties' intent.
- **Copy-paste numbers from English into Arabic without re-verification**: especially dangerous in financial schedules.
- **Machine translation without legal-register review**: Google Translate / DeepL produce colloquial Arabic that would embarrass parties before an Arabic-speaking judge.
- **Missing Arabic in employment contracts**: GCC labor authorities often refuse to process contracts that are English-only.

## Related skills

- [[draft-contract-skeleton-builder]]
- [[draft-boilerplate-clauses]]
- [[review-translation-quality-ar-en]]
- [[heuristic-bilingual-ar-en-mirror-clauses]]
