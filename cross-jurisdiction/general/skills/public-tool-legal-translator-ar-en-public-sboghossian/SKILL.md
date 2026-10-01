---
name: public-tool-legal-translator-ar-en-public-sboghossian
title: Legal Translator — Arabic ↔ English (Public Tool)
description: Use when a user needs to translate legal text between Arabic and English with legal-fidelity — preserving defined terms, using proper legal Arabic terminology, handling Hijri/Gregorian date conversion, maintaining bilingual contract structure, and flagging doctrines that lack direct equivalents. A key differentiator for the MENA market vs. generic translation tools. Free up to 2 pages; sign-in for longer documents.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/public-tool/public-tool-legal-translator-ar-en-public
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: general
language: en
---

# Legal Translator — Arabic ↔ English (Public Tool)

## What it does

The Legal Translator provides bidirectional Arabic ↔ English translation of legal text with legal fidelity — meaning it does not merely translate words, it translates legal meaning. Generic translation tools (Google Translate, DeepL) produce grammatically plausible but legally incorrect results for contract language; this tool is calibrated to the specific conventions of legal Arabic (Fus'ha used in contracts and statutes) and legal English.

This tool is a key differentiator for Louis in the MENA market, where bilingual contracts are the standard in UAE, KSA, Lebanon, Qatar, and Egypt, and where English-language legal tools (Harvey, Westlaw AI, Casetext) do not serve the Arabic-language dimension of legal work.

---

## Capabilities

### 1. Legal term preservation

Defined terms in a contract must be translated consistently throughout the document. The tool:
- Identifies defined terms on first occurrence (both the Arabic and English versions)
- Creates a consistent translation glossary for the document
- Does not substitute a synonym for a defined term that appears again later

### 2. Proper legal Arabic usage

Generic translation tools often use colloquial Arabic or grammatically valid but legally incorrect formulations. Key distinctions:

| Concept | Correct legal Arabic | Common generic translation error |
|---|---|---|
| "The Party acknowledges and agrees" | يُقر ويوافق | يعد ويوافق (wrong — "يعد" means "counts as") |
| "Subject to" | وفقاً لـ / مع مراعاة | بموجب (can be correct but contextually varies) |
| "Force majeure" | القوة القاهرة | There is no single Arabic equivalent; use القوة القاهرة and define in the contract |
| "Indemnification" | التعويض والإعفاء من المسؤولية | Generic: التعويض (which is compensation, not the full indemnification concept) |
| "Governing law" | القانون الحاكم / القانون الواجب التطبيق | Sometimes rendered as "القانون المعمول به" — acceptable but less precise |
| "Whereas" (recitals) | إذ إن / حيث إن | بما أن (acceptable but less formal) |

### 3. Numerical, currency, and date handling

- **Numbers:** Preserve exact figures; do not convert; note the Arabic numeral / Western numeral convention used in the original
- **Currency:** Preserve the original currency designation (AED, SAR, USD, LBP, EGP); add the Arabic/English equivalent on first occurrence
- **Dates:** Convert Hijri ↔ Gregorian as annotated footnotes where the original uses Hijri dates; format: "[Hijri date] (corresponding to [Gregorian date])"
- **Arabic number format:** Arabic contracts sometimes use Eastern Arabic numerals (٢٠٢٦); translate to Western Arabic numerals (2026) in the English version and vice versa

### 4. Bilingual contract structure

Many UAE and KSA contracts are printed with Arabic on one side of the page and English on the other (parallel columns or facing pages). The tool:
- Preserves this parallel structure in output
- Maintains clause / article numbering alignment between the two language versions
- Flags any clause that appears in one language version but not the other (a gap that creates legal risk)

### 5. Doctrine flagging — concepts that don't translate directly

Some legal concepts have no direct equivalent across the two legal traditions. The tool flags these rather than silently translating:

| Doctrine | Translation challenge |
|---|---|
| "Equity" (English law) | No direct Arabic equivalent; translate as "العدالة والإنصاف" (justice and fairness) but flag that this is not a term of art in civil-law systems |
| "Common law" | القانون العرفي / القانون الإنجليزي depending on context; always footnote |
| "Trust" (fiduciary trust) | Arabic civil law has no trust concept; Sharia law has the waqf (وقف) as an analogous but distinct institution; always footnote |
| "Riba" (Islamic prohibition on interest) | Translate as "usury / interest-bearing transactions" in English but add footnote explaining the Sharia prohibition and its commercial implications |
| "Gharar" | "Uncertainty / excessive ambiguity in a contract" — footnote that this is a distinct Sharia concept; contracts that contain excessive gharar may be unenforceable under Islamic jurisprudence |
| "Ma'sum" | "Protected / inviolable" — a Sharia term; context-specific translation |
| "Ijara" | "Lease/hire contract" — but add footnote: in Islamic finance, ijara is a specific Sharia-compliant leasing structure distinct from a conventional lease |
| "Murabaha" | "Cost-plus-profit sale" — footnote: Islamic finance instrument; must be explained in English |

---

## Usage limits

| Tier | Limit | Features |
|---|---|---|
| Free (no login) | 2 pages per translation | Full output; watermarked PDF |
| Registered (free account) | 10 pages per translation | No watermark; glossary export; saved history |
| Pro | Unlimited; 150+ pages | Batch; API; custom glossary; legal review flag integration |

---

## Behavior rules

- **Legal fidelity over fluency.** A legally accurate translation that reads slightly formally is preferable to a fluent translation that changes meaning. When in doubt, preserve the source text's legal structure.
- **Always footnote ambiguous translations.** If a word or phrase could have two or more defensible legal translations, translate with the most probable interpretation and add a footnote flagging the alternative and why it matters.
- **Do not paraphrase statutes.** When translating a referenced statute (e.g., "Federal Decree-Law No. 45/2021"), preserve the formal name; add the official Arabic or English name in parentheses on first occurrence.
- **Governing language clause.** Many bilingual contracts state that one language version governs in case of conflict. Flag this clause prominently at the top of the translation output and remind the user which version controls.
- **No legal advice.** The translation is a tool; it does not evaluate whether the terms comply with applicable law or are enforceable.

---

## Why Arabic legal translation requires specialization

Generic AI translation tools were trained predominantly on non-legal text. Legal Arabic (Fus'ha / Modern Standard Arabic used in contracts and statutes) differs from conversational Arabic in:
- Vocabulary: legal contracts use formal Fus'ha terms not commonly encountered in training data
- Structure: Arabic contract sentences are often constructed with the verb at the beginning; the sentence structure must be re-ordered for English, not merely translated word-for-word
- Number agreement: Arabic has dual forms (مثنى) and complex plural rules; mistranslations of number can change a key obligation
- Gendered nouns: Arabic nouns have grammatical gender; legal translation must be consistent

For MENA practitioners, a translation error in a governing-law clause, a defined term, or a payment obligation can create a material legal risk. This tool addresses that gap.

---

## Failure modes

| Failure mode | Response |
|---|---|
| Input text is a dialect (not formal legal Arabic) | Translate with a note flagging that the text appears to be in dialect form; output may be less reliable for legal fidelity |
| Mixed-language document (some clauses in Arabic, some in English) | Translate only the Arabic portions to English (or vice versa) and preserve the bilingual structure |
| Handwritten Arabic text (scanned document) | Apply OCR with Arabic character recognition; flag quality concerns |
| Dialect-specific terms (Lebanese, Egyptian, Gulf) | Note the dialectal origin and provide the standard legal Arabic equivalent with explanation |

---

## Related skills

- [[public-tool-legal-jargon-simplifier-public]]
- [[public-tool-contract-summarizer-public]]
- [[public-tool-statute-explainer-public]]
- [[kb-mena-legal-drafting]]
