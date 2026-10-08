---
name: heuristic-bilingual-ar-en-mirror-clauses-sboghossian
title: Bilingual AR-EN Mirror Clauses
description: Use when drafting or reviewing bilingual Arabic-English legal documents across MENA jurisdictions. Enforces the rule that every clause must mirror one-to-one between both language versions — same clause numbers, same legal effect, consistent defined terms, matching numerals. Also requires a controlling-language statement. Applies to all document types filed with MENA courts or government authorities where Arabic is an official language of the proceedings.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/heuristic/heuristic-bilingual-ar-en-mirror-clauses
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Bilingual AR-EN Mirror Clauses

## When this applies

This heuristic is activated whenever:
- A document is being drafted in both Arabic and English.
- A unilingual document is being translated for filing, registration, or execution in a MENA jurisdiction.
- A bilingual document is being reviewed for enforceability or translation fidelity.

Arabic is an official or required language for court filings, government registrations, and notarized instruments in all MENA jurisdictions. Documents submitted to UAE courts, KSA courts, Lebanese courts, and Egyptian courts must be in Arabic (or submitted with an Arabic translation). Discrepancies between language versions are a litigation risk.

## The core rule

**Every clause in the Arabic version must mirror every clause in the English version, one-to-one:**

1. **Same clause numbering**: Article 1 in English = المادة 1 in Arabic.
2. **Same legal effect**: the substantive obligation, right, condition, or exception in each clause must be identical across both versions. A clause that creates a 30-day notice period in English must create a 30-day notice period in Arabic.
3. **Consistent defined terms**: a term defined as "the Provider" in English must be defined with a single, consistent Arabic equivalent throughout. Do not use two different Arabic terms for the same English defined term.
4. **Matching numerals and currency**: numbers and amounts must be identical. Decide upfront whether to use Western Arabic numerals (0–9) or Eastern Arabic numerals (٠–٩); choose one and apply consistently. Currency must use international ISO codes (USD, AED, SAR, LBP), not symbols, in RTL text.
5. **Controlling language statement**: the document must end with a clause stating which language version prevails in the event of inconsistency.

## Document layout patterns

### Pattern 1 — Stacked (most common for formal instruments)

Full Arabic text follows full English text (or vice versa), with clear language-version headings. Same clause structure in both halves.

```
## Article 1. Definitions
In this Agreement, the following terms have the meanings ascribed to them below…

---

## المادة 1. التعريفات
في هذه الاتفاقية، تحمل المصطلحات التالية المعاني المحددة لها أدناه…
```

### Pattern 2 — Side-by-side table (suitable for shorter documents)

| Article | English | Arabic |
|---|---|---|
| 1. Definitions | In this Agreement… | في هذه الاتفاقية… |
| 2. Services | The Provider shall… | يلتزم مزود الخدمة بـ… |
| 3. Payment | Client shall pay… | يلتزم العميل بسداد… |

Side-by-side format is useful for review and comparison but is less common in formal execution copies because Arabic right-to-left text flows poorly in table cells on some platforms.

## Controlling language clause

The document must contain an explicit statement of which language version controls. Standard formulations:

**English controls (common for international commercial agreements):**
> *"In the event of any inconsistency between the English and Arabic versions of this Agreement, the English version shall prevail."*

> *"في حالة وجود أي تعارض بين النسخة الإنجليزية والعربية من هذه الاتفاقية، تسود النسخة الإنجليزية."*

**Arabic controls (required or preferred for KSA instruments, court filings, government contracts in most MENA jurisdictions):**
> *"في حالة وجود أي تعارض بين النسختين العربية والإنجليزية من هذه الاتفاقية، تسود النسخة العربية."*

**Warning on KSA and UAE government contracts**: many standard government contract templates in KSA and UAE specify that the Arabic text controls. If the parties have negotiated different terms in the English version but the Arabic text controls, the English negotiations are unenforceable.

## Critical failure modes

| Failure | Risk |
|---|---|
| One version has more detail than the other | The extra clause may be unenforceable; a court applying the controlling language will ignore the other version's additions |
| Defined terms defined differently across languages | Ambiguity in the entire agreement; may require expert evidence to resolve |
| Numerals in different scripts | Creates apparent discrepancy; potentially allows a party to argue different amounts |
| Currency symbols vs codes in RTL text | ISO codes render correctly in RTL; symbols ($ £) may render in unexpected positions |
| No controlling language statement | Court has discretion to apply either version; increases litigation risk |
| Colloquial Arabic instead of legal-register Arabic | Reduces enforceability in formal proceedings; may undermine the document's legal character |

## Translation quality

Use only legal-register Modern Standard Arabic (MSA) for formal legal documents. Colloquial Arabic (Levantine, Gulf) is not appropriate for contracts, court submissions, or government filings.

For court filings and government instruments: use a sworn or officially certified translator (see [[heuristic-translation-certified-vs-sworn]]). AI translation is not acceptable as the basis for an executed legal document — it may be used as a starting draft for human review only.

After AI-assisted bilingual drafting, run [[review-translation-quality-ar-en]] to catch:
- Inconsistent defined terms.
- Reversed or omitted obligations.
- Numeral and date discrepancies.
- Missing clause mirrors.

## Jurisdiction-specific notes

| Jurisdiction | Language requirement |
|---|---|
| UAE federal courts | Arabic required for all filings; English contracts accepted with certified Arabic translation |
| DIFC / ADGM | English is the court language; Arabic not required for DIFC/ADGM-governed agreements, but Arabic versions are often negotiated |
| KSA | Arabic required for all official purposes; bilingual contracts common in cross-border deals; Arabic controls by default |
| Lebanon | Arabic required for court filings; commercial contracts may be in either language; courts may request translation |
| Egypt | Arabic required for filings; foreign-language contracts enforceable but must be translated for official use |

## Related skills

- [[draft-bilingual-ar-en-side-by-side]]
- [[output-bilingual-formatting]]
- [[heuristic-translation-certified-vs-sworn]]
- [[review-translation-quality-ar-en]]
- [[heuristic-notarization-apostille-requirements]]
