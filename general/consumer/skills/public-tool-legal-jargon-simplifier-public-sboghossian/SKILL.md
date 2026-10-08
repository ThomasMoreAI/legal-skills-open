---
name: public-tool-legal-jargon-simplifier-public-sboghossian
title: Legal Jargon Simplifier (Public Tool)
description: Use when a user pastes any legal text — a contract clause, statute excerpt, court ruling, consent form, or offer letter — and needs a plain-English translation at approximately a 6th-grade reading level. Preserves numerical figures and party names exactly, footnotes complex doctrines (force majeure, indemnity, warranty), and adds a one-line "real-world meaning" per paragraph. The primary expression of Louis's "comfort UI" vision for legal accessibility. Works across all jurisdictions and document types.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/public-tool/public-tool-legal-jargon-simplifier-public
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: consumer
language: en
---

# Legal Jargon Simplifier (Public Tool)

## What it does

The Legal Jargon Simplifier converts dense legal text into plain, direct language that any literate adult can understand. Unlike the Contract Summarizer (which produces a structured breakdown), the Jargon Simplifier does a clause-by-clause translation — preserving the structure and sequence of the original text, just replacing the legalese.

Input: Any legal text — contract clause, statute section, letter from a lawyer, court order, privacy policy, consent form, employee offer letter, lease clause.

Output: A rewritten version of the same text, paragraph by paragraph, with:
- Plain-English rewrite of each paragraph
- One-line "real-world meaning" annotation below each paragraph
- Footnotes for any legal doctrine that cannot be plainly translated (force majeure, indemnity, estoppel, etc.)
- All numbers, party names, and defined terms preserved exactly

---

## Translation rules

### Mandatory replacements

| Original phrase | Plain-English replacement |
|---|---|
| "Notwithstanding the foregoing" | "Even though we just said [X], ..." or "Regardless of what came before, ..." |
| "Heretofore" | Rewrite the sentence without this word — it means "before this time / agreement" |
| "Hereinafter" | Replace with "called" or just use the name; e.g., "called the Company" |
| "Wherein" | Rewrite — usually means "in which" or "where" |
| "In perpetuity" | "Forever" |
| "Forthwith" | "Immediately" |
| "Whereas" (recital context) | "Background: ..." |
| "Shall" (obligation) | "Must" |
| "May" (permission) | "Can" |
| "Inter alia" | "Among other things" |
| "Mutatis mutandis" | "With the necessary changes" (add footnote explaining the doctrine) |
| "Force majeure" | Keep term; add footnote: "A legal doctrine that excuses a party from performing when extraordinary events outside their control — like a war, earthquake, or pandemic — make performance impossible." |
| "Indemnify and hold harmless" | "Pay for any losses and protect [the other party] from legal claims" |
| "Warranty" | "A guarantee that [X is true]" |
| "Representation" | "A statement of fact [Party] is making as of today" |
| "Covenant" | "A promise to [do / not do something]" |
| "Liquidated damages" | Keep term; add footnote: "A pre-agreed dollar amount both parties accept as fair compensation if a specific breach happens — instead of having to prove the actual loss." |
| "Time is of the essence" | "Meeting every deadline in this agreement is critical; missing a deadline is a serious breach." |
| "Entire agreement" | "This document is the complete agreement between the parties. Earlier conversations, emails, or promises that aren't written here don't count." |

### Preserve exactly (no substitution)

- All numerical figures (amounts, percentages, dates, durations)
- Party names and defined terms (preserve in the same form as the original; if a defined term is used, also explain what the term means the first time it appears)
- Statute and regulation names (do not paraphrase; explain what the statute governs in a footnote)
- Proper nouns (place names, institution names)

### "Real-world meaning" annotation

After each plain-English paragraph, add a one-sentence annotation in italic that explains what this paragraph means for the reader in practical terms:

> *Real-world meaning: If you miss a payment by more than 5 days, the company can charge you extra interest on the overdue amount — so pay on time.*

---

## Use cases

| User | Document type | What they gain |
|---|---|---|
| Consumer | Terms of service for an app | Understands what data is collected and how; knows cancellation rights |
| Tenant | Residential or commercial lease | Understands repair obligations, break clauses, and penalty triggers |
| Patient | Medical consent form | Understands risks, alternatives, and their right to withdraw consent |
| Employee | Job offer letter | Understands base salary vs. total comp, non-compete scope, and termination terms |
| Small business owner | Supplier contract | Understands payment obligations, liability exposure, and IP rights |
| Student | Academic integrity policy | Understands what constitutes a violation and the consequences |

---

## Behavior rules

- **Do not summarize.** The Jargon Simplifier translates — it rewrites the existing text in plain language. The Contract Summarizer summarizes; this tool translates. Preserve paragraph structure and sequence.
- **Do not omit content.** Every paragraph of the input must produce a plain-language equivalent; do not silently skip provisions because they are complex.
- **Footnotes for genuinely untranslatable doctrines.** Some legal concepts do not have a one-for-one plain English equivalent (equity, estoppel, piercing the corporate veil). Keep the term, add a footnote, and explain the concept in 2–3 sentences.
- **No legal advice.** The simplifier explains what the text says; it does not evaluate whether the terms are fair, legal, or advisable. Always include: *"This plain-language version is for informational purposes only and does not constitute legal advice."*
- **Maintain Arabic ↔ English awareness.** If the input is in Arabic, route to [[public-tool-legal-translator-ar-en-public]] for translation before simplification. If the input is English but refers to Arabic-law concepts (e.g., a Sharia-compliant contract), footnote the Islamic finance / law terms (riba, gharar, murabaha, ijara).

---

## Output format

For each paragraph of the original:

```
[Original legal text — preserved in quote block for reference]

Plain English: [Rewritten paragraph in plain language]

Real-world meaning: [One-sentence practical implication in italics]
```

For footnoted terms, use a numbered footnote list at the end of the output.

---

## Why this tool matters

This is Louis's most direct expression of the "comfort" product vision: the idea that legal documents should not be a source of anxiety. By removing the intimidation factor of legalese, the tool democratizes access to legal information — and creates a strong emotional connection with users who have previously felt excluded from understanding documents they were expected to sign.

This tool pairs with the Contract Summarizer (high-level overview) and the Statute Explainer (detailed statutory analysis) to create a full plain-language legal research suite.

---

## Failure modes

| Failure mode | Response |
|---|---|
| Input is in Arabic | Route to [[public-tool-legal-translator-ar-en-public]] first; then simplify the English translation |
| Input is not a legal document (e.g., a news article) | Alert the user; still attempt simplification of the text if it contains legal terminology |
| Input is extremely long (> 20 pages) | Apply [[ref-long-documents-50pp]] chunked processing; process in sections |
| Input contains extensive mathematical formulas (loan amortization, complex financial models) | Translate the surrounding text; for formulas, add a plain-language explanation of what the formula calculates rather than rewriting the formula itself |

---

## Related skills

- [[public-tool-contract-summarizer-public]]
- [[public-tool-statute-explainer-public]]
- [[public-tool-legal-translator-ar-en-public]]
- [[public-tool-case-summarizer-public]]
- [[ref-long-documents-50pp]]
