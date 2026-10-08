---
name: prompt-pack-convert-law-into-checklist-sboghossian
title: Convert Law Into Checklist
description: Use when a lawyer or compliance professional needs to convert a legal provision, regulation, or statute into a practical, actionable compliance checklist for business use. The output enables non-lawyers to self-assess compliance without re-reading the underlying law. Applicable to any legal instrument and any jurisdiction; particularly useful for MENA regulations (UAE, KSA, LB, EG, DIFC/ADGM) that are frequently updated and not always available in accessible English-language summaries.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-convert-law-into-checklist
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Convert Law Into Checklist

Compliance checklists are the bridge between legal analysis and operational action. A checklist converted from a legal provision tells the finance team, HR department, or operations manager exactly what they need to do — without requiring them to interpret the law themselves.

## When to use this

- A new law or regulation has come into force and the compliance team needs a self-assessment tool.
- The legal team is advising a client on compliance with a specific provision and wants to give them a structured action list rather than a memo.
- A business is conducting an internal compliance audit and needs structured questions to test each obligation.
- An in-house team is onboarding a new business line and needs compliance checklists for the relevant regulatory framework.
- The company operates in multiple MENA jurisdictions and needs parallel checklists to compare obligations across jurisdictions.
- A due diligence exercise requires testing compliance with a specific legal framework.

## Required inputs

| Input | Why it matters | Sensible default |
|---|---|---|
| The legal provision or document to be converted | The source text | User pastes the provision, or names the law and article |
| Jurisdiction | The law is jurisdiction-specific; the checklist must reflect the applicable rules | Ask the user |
| Target audience for the checklist | Determines technical depth and language | Ask the user: compliance officer / finance / HR / all-staff |
| Entity type being assessed | Some obligations apply only to certain entity types (regulated firms, large employers, publicly listed companies) | Ask the user |

## Optional inputs

- Whether the checklist should include the underlying legal reference for each item (recommended for legal use; may be omitted for operational all-staff checklists).
- Whether deadlines should be included in the checklist or in a separate timeline.
- Whether the checklist should distinguish between obligations already met and those requiring action.
- Whether a "consequence of non-compliance" column should be included (recommended for high-stakes checklists).

## Methodology

### Step 1 — Parse the provision into discrete obligations

Read the provision and identify each distinct obligation:
- Who must act? (Subject of the obligation.)
- What must they do? (The required action.)
- When? (Deadline, frequency, or trigger event.)
- How? (Prescribed method or form, if specified.)
- To whom / with whom? (Regulatory authority, counterparty, internal function.)

One obligation = one checklist item. Do not combine separate obligations.

### Step 2 — Classify each obligation

| Obligation type | Description |
|---|---|
| Affirmative duty | Must do something (register, file, appoint, train) |
| Prohibition | Must not do something |
| Conditional | Must do something if a trigger event occurs |
| Threshold | Obligations change at a specified size/volume/risk threshold |
| Periodic | Must do something regularly (annually, quarterly, on each transaction) |

### Step 3 — Draft each checklist item

Format each item as an actionable question or statement:

**Format A — Yes/No question (for audit checklists):**
"Has the company registered with [Authority] as required under [Law/Article]? [ ] Yes / [ ] No / [ ] N/A"

**Format B — Action statement (for compliance programs):**
"[ ] Register with [Authority] by [Date] if [condition applies]. Responsible: [Role]. Reference: [Law/Article]."

**Format C — Status table (for assessment reports):**

| # | Obligation | Legal reference | Status (Compliant / Gap / N/A) | Action required | Owner | Deadline |
|---|---|---|---|---|---|---|
| 1 | Appoint a Data Protection Officer | UAE PDPL Art. 12 | Gap | Identify and appoint a DPO | Legal / HR | [Date] |
| 2 | Register data processing activities | UAE PDPL Art. 5 | Compliant | — | — | — |

### Step 4 — Add explanatory notes where needed

For provisions that are ambiguous or that require judgment (e.g., "reasonable measures," "material breach," "significant risk"), add a short explanatory note:
- "What counts as 'significant' is not defined in the law; consult legal counsel if in doubt."
- "This obligation applies only if the company processes data of more than [threshold] data subjects."

### Step 5 — Review completeness

After drafting, re-read the original provision to confirm:
- No obligation has been missed.
- No threshold or exception has been omitted that would change a "must do" to "need not do."
- The checklist reflects the current version of the law (confirm with local counsel if any amendments are possible).

## Checklist design principles

**Be binary:** Each item should be answerable Yes/No or Compliant/Non-Compliant. Ambiguous items cannot be audited.

**One item per obligation:** If a provision has three sub-clauses, write three checklist items.

**Include the reference:** Always cite the article or provision number. This lets users go back to the source if needed.

**Deadline first for time-sensitive obligations:** If an item has a deadline, put the deadline at the start of the item — deadlines are the most commonly missed compliance trigger.

**Tailor the consequence column to the risk level:** For high-risk obligations (criminal penalties, license revocation), state the consequence explicitly in the checklist. It focuses minds.

## MENA compliance context

When converting MENA laws, note:
- **Arabic is the official language** in UAE onshore, KSA, LB, and EG. English translations are unofficial; if the checklist is for operational use, the English translation must be verified against the Arabic source.
- **Amendment risk:** MENA regulatory instruments are frequently amended by Ministerial Decisions, Cabinet Resolutions, or Central Bank circulars. State the version of the law the checklist is based on and recommend periodic review.
- **DIFC/ADGM:** Legislation is in English; the DFSA and FSRA publish guidance documents that are a necessary complement to the primary rules.
- **KSA:** Compliance obligations for foreign-owned entities may be more onerous than for Saudi-owned entities (Nitaqat, transfer pricing, customs). Distinguish.

**Common MENA compliance frameworks for which this skill is most useful:**
- UAE Federal Corporate Tax Law (UAE CT)
- UAE VAT Law and Executive Regulations
- UAE Personal Data Protection Law (PDPL)
- UAE AML Law (Federal Decree-Law No. 20 of 2018)
- KSA Zakat, Tax and Customs Authority (ZATCA) regulations
- KSA AML Law
- DIFC Data Protection Law and DFSA Rulebook
- ADGM Financial Services and Markets Regulations
- Lebanon AML Law No. 318 of 2001
- Egypt Data Protection Law (Law No. 151 of 2020)
- GCC VAT Unified Agreement

## Common mistakes

- Writing a narrative summary instead of discrete checklist items — summaries cannot be audited or assigned.
- Omitting exceptions and safe harbours — these are often the items the client most needs to know about.
- Creating a checklist from a summary of the law rather than the law itself — secondary sources introduce errors.
- Not stating the law version and date — a checklist based on an amended provision gives wrong guidance.
- Making items too vague ("comply with data protection law") — a checklist item must be specific enough to be testable.

## Related skills

- [[prompt-pack-complex-law-simple-summary]]
- [[prompt-pack-convert-complex-document-into-key-points]]
- [[prompt-pack-data-retention-policy]]
- [[prompt-pack-data-subject-access-request-procedure]]
- [[prompt-pack-cross-border-data-transfer-assessment]]
