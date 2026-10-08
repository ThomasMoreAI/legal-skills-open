---
name: review-translation-quality-ar-en-sboghossian
title: Arabic ↔ English Translation Quality Review
description: Use when evaluating the legal fidelity of an Arabic-English or English-Arabic translation of a contract or legal document. Checks terminology consistency (modal verbs, defined terms, numbers, dates), Hijri-Gregorian date accuracy, party name bilingual consistency, jurisdictional standard boilerplate, Shariah/fiqh term preservation, governing-language designation, and LTR/RTL formatting. Covers MENA jurisdictions (KSA, UAE, LB, EG) with dialect and register sensitivity.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/review/review-translation-quality-ar-en
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Arabic ↔ English Translation Quality Review

## When to use this

Use when you need to assess whether an Arabic translation of an English contract (or vice versa) accurately preserves legal meaning, terminology, and structure. Poor translations create genuine enforceability risks: a court interpreting the Arabic version of a contract may reach a different result than a court reading the English version if the translation is inaccurate.

Typical triggers:
- A bilingual commercial contract where the Arabic and English versions must be aligned
- A Saudi, UAE, or Lebanese contract where Arabic is the legally controlling language
- Post-signature review to verify translation was accurate
- Enforcement context where a court may rely on the Arabic version
- Quality-control of a translated draft before it is sent to the counterparty

## Inputs

| Input | Why it matters | Default |
|---|---|---|
| Both language versions | The Arabic and English texts to compare | Required |
| Which language is governing | Determines which version controls in case of conflict | From contract; ask if not specified |
| Jurisdiction | Affects dialect register, standard boilerplate, and regulatory terminology | Required |
| Document type | NDA, MSA, employment, real estate — standard terminology differs | Infer from document |

## Review Methodology

### Check 1 — Modal Verb Translation (Obligations and Permissions)

Modal verbs carry precise legal meaning in English. Their Arabic equivalents must be accurately chosen:

| English | Correct Arabic | Common error |
|---|---|---|
| shall (mandatory obligation) | يجب أن (yajib an) | سوف (sawfa) — future tense, not mandatory obligation |
| must | يجب | same error as above |
| may (permission) | يجوز / يحق (yajūz / yaḥiqq) | قد — sometimes used but ambiguous |
| will (contractual promise) | سيقوم / يتعهد | mixing with "shall" equivalents |
| shall not / must not | لا يجوز / يُحظر | omission of prohibition |
| may not | لا يجوز | same |

A contract that translates "shall pay" as "سوف يدفع" instead of "يجب أن يدفع" weakens a mandatory obligation to a mere expectation — this can affect claims for breach.

### Check 2 — Defined Terms Consistency

In English legal drafting, defined terms are capitalized throughout the document (e.g., "Confidential Information", "Agreement", "Party"). In Arabic legal drafting:
- Defined terms are typically identified by underlining or by brackets: المعلومات السرية or [المعلومات السرية]
- The exact Arabic term chosen for a defined concept must be used consistently throughout the document

Check:
- Every defined term in the English version has a corresponding defined term in the Arabic version
- The Arabic defined term is used consistently (not varied from paragraph to paragraph)
- Numbers in the Definitions section match (if "Party A" is defined, the Arabic version should define الطرف الأول consistently)

### Check 3 — Numbers, Currencies, and Percentages

Verify:
- All numerical values match between versions (contract price, thresholds, notice periods, caps)
- Currency is correctly translated (USD → دولار أمريكي; AED → درهم إماراتي; SAR → ريال سعودي; LBP → ليرة لبنانية)
- Percentage signs are correctly placed (Arabic text reads right-to-left but percentages and numbers often appear in Western format or in Eastern Arabic numerals)
- Arabic-Indic numerals (٠١٢٣٤٥٦٧٨٩) vs Western Arabic numerals (0123456789): ensure consistency within the document; mixed use can cause ambiguity in dates and sums

### Check 4 — Hijri ↔ Gregorian Date Conversion

In Saudi Arabia and some other GCC jurisdictions, legal documents may reference both the Hijri and Gregorian calendars. Common conversion errors:

- Off-by-one-day errors due to the Hijri calendar starting at sunset the previous evening
- Incorrect conversion leading to dates that differ by months rather than days (rare but occurs with manual conversion)

Verify: any date appearing in both calendars matches after conversion (use a reliable Hijri-Gregorian conversion reference). For KSA legal documents, Hijri dates are the official reference; Gregorian dates are provided for convenience but errors in Gregorian dates typically do not affect legal validity if the Hijri date is correct.

### Check 5 — Party Names in Both Scripts

Party names must be consistent between versions:
- Full legal entity name in both scripts: Arabic name as it appears on the Commercial Registration; English name as it appears on the CR or trade license
- Consistency throughout the document: if the contract uses the Arabic entity name in one place and a transliteration in another, this creates ambiguity
- Where a party has a foreign name with no Arabic equivalent: use a consistent transliteration throughout (avoid switching between different romanization schemes or Arabic transliterations)

### Check 6 — Jurisdiction-Specific Boilerplate Register

Legal Arabic varies by jurisdiction. Standard boilerplate phrases differ between:

| Jurisdiction | Register / standard phrases |
|---|---|
| KSA | Classical legal Arabic (عربية قانونية فصحى); references to Royal Decrees, Ministerial Decisions; specific SCCA arbitration boilerplate |
| UAE | Modern standard Arabic; DED / Ministry of Economy terminology; references to Federal Decree-Laws |
| Lebanon | French-influenced Arabic (Levantine legal register); references to Code des obligations et des contrats, Code de commerce libanais |
| Egypt | Egyptian legal standard Arabic; Civil Code terminology; references to Egyptian law numbers |

A contract using Saudi legal register for a Lebanese contract, or vice versa, will appear non-standard and may cause confusion in local courts. Flag register mismatches.

### Check 7 — Shariah and Fiqh Terms

For Islamic finance and certain commercial contexts, terms from Shariah and classical fiqh must be preserved with precision:

| Term | Correct treatment | Error to avoid |
|---|---|---|
| Riba (ربا) — prohibited interest | Preserve as "riba" or "ربا" with a definition footnote | Translating as "interest" without explanation |
| Gharar (غرر) — excessive uncertainty | Preserve as "gharar" with footnote | Translating as "uncertainty" which loses the specific Shariah prohibition |
| Maysir (ميسر) — speculation/gambling | Preserve as "maysir" with footnote | Omitting or mischaracterizing |
| Murabaha (مرابحة) — cost-plus sale | Use "murabaha" in both English and Arabic versions; define in both languages | Using "markup sale" without defining the Shariah structure |
| Ijara (إجارة) — Islamic lease | Use "ijara" in both versions with definition | Translating as "lease" without noting the Islamic finance structure |
| Wakala (وكالة) — agency | Standard Arabic term; ensure it maps correctly to "agency" in English context | |

If a document involves Shariah-compliant structures, missing or incorrect terminology can affect the enforceability of the structure before a Shariah supervisory board or Islamic finance court.

### Check 8 — Governing Language Designation

For bilingual contracts, the document must clearly state which language version prevails in case of conflict:

Verify:
- Governing language clause is present in both versions
- The clause in the Arabic version correctly identifies the governing language
- The clause in the English version correctly identifies the governing language
- Both versions agree on which language prevails (a conflict in the governing-language clause itself is a critical error)

**MENA context**:
- **KSA**: Arabic is typically the legally controlling language for Saudi-law governed contracts; English version is the courtesy translation
- **UAE (onshore)**: Arabic is the official language; for contracts before UAE courts, Arabic version is used; bilingual contracts typically state "Arabic version prevails"
- **DIFC / ADGM**: English is the official language of the courts; contracts may be in English only; Arabic version is for business convenience
- **Lebanon**: both Arabic and French are official languages; contracts may designate either; Arabic is preferred for real estate

### Check 9 — LTR/RTL Formatting

Layout issues that affect legal interpretation:
- In a bilingual contract, the Arabic text is right-to-left (RTL) and the English text is left-to-right (LTR). Layout errors can cause:
  - Numbers appearing in the wrong position relative to currency symbols
  - Cross-references in Arabic pointing to the wrong article numbers
  - Tables appearing misaligned between versions

- Check that any clause cross-references in the Arabic version (see article 5.1 / انظر المادة 5.1) match the clause numbers in the English version
- Verify that defined-term references in the Arabic version use the same article/schedule numbers as the English version

## Output Format

```json
{
  "errors": [
    {
      "ar": "<Arabic text with error>",
      "en": "<English source text>",
      "issue": "<description of translation error>",
      "severity": "critical|high|medium|low",
      "suggestion": "<corrected Arabic text or guidance>"
    }
  ],
  "inconsistencies": [
    {
      "defined_term": "<term>",
      "issue": "<how Arabic term is used inconsistently>"
    }
  ],
  "style_notes": [
    "<observations on register, dialect choice, or formatting>"
  ],
  "governing_language_stated": true/false,
  "governing_language": "ar|en|null",
  "overall_fidelity": "high|adequate|poor",
  "critical_error_count": <int>
}
```

## Common Mistakes in Legal Translation

- Using "سوف" (shall/will, future tense) for mandatory obligations instead of "يجب أن" — weakens obligations
- Inconsistent defined-term translation (using three different Arabic terms for "Confidential Information" across the document)
- Forgetting to convert numbers to Eastern Arabic-Indic numerals when the document uses that format (or vice versa)
- Using Egyptian Arabic legal terminology in a Saudi-law-governed contract — wrong register for the jurisdiction
- Omitting a Hijri date where Saudi law requires it (or including an inaccurate Hijri date)
- Translating "force majeure" literally as "القوة القاهرة" in one place and as "ظروف طارئة" in another — creates two different concepts from one English term

## Limits

- This skill evaluates legal fidelity, not stylistic quality of the translation
- For Shariah finance structures, have a Shariah supervisory board member or qualified Islamic finance counsel verify the fiqh terms
- This skill cannot certify a translation as legally accurate — only identify issues to be verified and corrected by a qualified legal translator

## Related Skills

- [[review-missing-clauses]]
- [[review-signature-block-validity]]
- [[review-unusual-terms-detector]]
- [[review-nda-quick-check]]
- [[draft-bilingual-ar-en-contract]]
