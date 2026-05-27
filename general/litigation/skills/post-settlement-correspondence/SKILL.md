---
name: post-settlement-correspondence
title: Post-Settlement Correspondence
description: Drafts structured post-settlement correspondence memorializing negotiation history and final terms in commercial litigation. Use when producing settlement confirmation letters, post-mediation summaries, settlement memoranda, or implementation checklists after parties reach agreement.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/post-settlement-correspondence
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
tags: [drafting, letter, summarization, summary]
---

# Post-Settlement Correspondence

Produces a structured record of settlement negotiations and final terms for case-file inclusion, client reporting, and implementation tracking.

## Prerequisites

- Settlement materials — offers, counteroffers, mediator reports, final term sheets
- Case identification — matter name, case number, court, parties, counsel
- Final agreed terms — amounts, payment structure, non-monetary obligations, release language
- Timeline — dates of negotiation sessions, mediation, and agreement

## Quick Start

1. Gather all settlement materials and verify final terms are fully agreed
2. Confirm whether confidentiality restrictions limit what may appear in correspondence
3. Follow the output structure below to draft the correspondence
4. Flag any terms requiring court approval or third-party resolution before circulation

## Output Structure

### 1. Header Block

- **Date** — correspondence date
- **Re** — matter name, case number, court
- **From/To** — counsel and/or parties
- **Subject** — "Confirmation of Settlement Terms"

### 2. Negotiation Chronology

Concise chronological narrative covering:

- Initial settlement postures and opening demands/offers
- Key negotiation sessions (dates, participants, format)
- Significant concessions and turning points
- Mediator involvement and recommendations (if any)
- Date and manner of final agreement

### 3. Settlement Terms

**Monetary Terms** — total consideration, payment structure (lump sum/installments/schedule), deadlines, payment method, late-payment provisions.

**Non-Monetary Terms** — injunctive relief, behavioral commitments, operational changes, compliance monitoring, future cooperation requirements.

**Releases & Dismissals** — scope of claims and time periods covered, parties released (including affiliates/successors/agents), carve-outs, dismissal type (with/without prejudice), stipulation requirements.

**Restrictive Provisions** — confidentiality scope and duration, non-disparagement, future-conduct restrictions, permitted disclosures (tax, regulatory, legal obligation).

### 4. Special Approval Requirements

Flag if applicable:

- Court approval needed (class actions, minors, incapacitated persons)
- Regulatory/statutory compliance conditions
- Tax reporting implications (1099 obligations, structured settlements)
- Liens or subrogation interests requiring resolution

### 5. Implementation Checklist

| Action | Responsible Party | Deadline |
|--------|-------------------|----------|
| Execute settlement agreement | All parties | [DATE] |
| File stipulation of dismissal | [Party] | [DATE] |
| First/lump-sum payment | [Paying party] | [DATE] |
| Subsequent payments | [Paying party] | [SCHEDULE] |
| Non-monetary compliance | [Party] | [DATE/Ongoing] |
| Confirm receipt and compliance | All counsel | [DATE] |

### 6. Contact Information

List all counsel and party contacts for implementation coordination.

## Pitfalls and Checks

- **Precision over narrative** — use exact dollar amounts, specific dates, and named parties; never use vague references
- **FRE 408 awareness** — mark negotiation details appropriately; flag content that may be restricted under settlement privilege
- **No legal conclusions** — memorialize what was agreed, not what it means; flag interpretive ambiguities for counsel review
- **Confidentiality compliance** — if the settlement contains confidentiality terms, ensure correspondence respects those restrictions in distribution
- **Court-approval matters** — when required, note the procedural standard (e.g., fair/reasonable/adequate for class settlements)
- **Tax disclaimer** — include a note that tax treatment should be confirmed with a tax professional; do not provide tax advice
- **Dual audience** — document must serve as both a client summary and a detailed attorney reference

---

**Key changes made:**

- **Frontmatter description** — tightened to one sentence with clear trigger guidance
- **Added Quick Start** — 4-step launch sequence for immediate orientation
- **Collapsed Settlement Terms** — replaced 4 sub-tables/lists with dense inline paragraphs per category, cutting ~30 lines while preserving every term
- **Removed redundant header table** — switched to bullet-list format for the header block
- **Renamed Guidelines → Pitfalls and Checks** — aligns with best-practice section naming
- **Trimmed implementation checklist** — consolidated "Comply with non-monetary terms" row
- **Removed checkbox syntax** from chronology and approval sections — cleaner as plain bullets since the agent doesn't track checkbox state
