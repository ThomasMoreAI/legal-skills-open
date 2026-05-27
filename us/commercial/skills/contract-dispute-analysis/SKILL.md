---
name: contract-dispute-analysis
title: Contract Dispute Analysis
description: 'Produces a structured contract dispute analysis for U.S. commercial litigation. Use when asked to evaluate breach claims, assess merits, prepare for mediation, or develop settlement strategy. Trigger: contract dispute, breach analysis, commercial litigation report, merits assessment, damages analysis, settlement evaluation.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/contract-dispute-analysis
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: commercial
language: en
---

# Contract Dispute Analysis

Structured, evidence-linked assessment of contract terms, breach exposure, defenses, remedies, and litigation strategy for U.S. commercial disputes.

## Prerequisites

Gather before starting:

- **Operative contracts** — executed agreements, amendments, addenda, exhibits
- **Performance records** — invoices, delivery receipts, change orders, acceptance/rejection docs
- **Communications** — emails, notices, cure letters, negotiation history
- **Damages inputs** — pricing, costs, lost-profits assumptions, mitigation steps
- **Forum constraints** — choice-of-law, forum-selection, arbitration/mediation clauses, notice/cure periods

## Quick Start

1. Collect the operative contract set and performance records
2. Identify controlling agreement(s) and order of precedence
3. Map obligations to performance timeline
4. Analyze breach elements claim-by-claim
5. Assess defenses, remedies, and risk
6. Deliver the report using the structure below

## Report Structure

### 1. Normalize Inputs

- Identify controlling agreement(s), precedence, and amendment history
- Flag missing documents and evidentiary gaps

### 2. Executive Summary

```text
Dispute: [one sentence]
Parties/Roles: [A = ], [B = ]
Contract: [title, date, governing law]
Primary Breach Theory: [A alleges B failed to ...]
Defenses: [top 2]
Exposure Range: [low–high]
ADR/Forum: [arbitration/mediation/forum selection]
Recommendation: [litigate/settle/ADR/hold]
```

### 3. Contract Inventory

| Document | Date | Parties | Scope | Precedence | Key Clauses (cite) |
| --- | --- | --- | --- | --- | --- |

### 4. Key Terms & Obligations

| Category | Clause (excerpt + cite) | Obligation | Party | Conditions/Triggers | Notice/Cure |
| --- | --- | --- | --- | --- | --- |

Categories: Performance, Payment, Warranties/Representations, Limitations/Liability, ADR/Forum/Choice of Law.

### 5. Timeline of Performance

| Date | Event | Contract Reference | Evidence | Compliance Status |
| --- | --- | --- | --- | --- |

### 6. Breach Analysis

Per-claim checklist:

- [ ] Duty identified and source cited
- [ ] Breach facts tied to timeline evidence
- [ ] Materiality assessed (common law or UCC Art. 2 for goods)
- [ ] Causation linked
- [ ] Damages supported

| Claim | Duty Source | Alleged Breach | Evidence | Materiality | Exposure |
| --- | --- | --- | --- | --- | --- |

### 7. Defenses & Counterclaims

| Defense | Legal Standard (jurisdiction) | Factual Basis | Evidence | Strength |
| --- | --- | --- | --- | --- |

Common defenses: impossibility/impracticability, failure of condition, waiver/estoppel, prior material breach, good faith/fair dealing.

### 8. Governing Law & Forum

- [ ] Choice-of-law clause identified
- [ ] Conflicts analysis (if no clause)
- [ ] UCC Art. 2 (goods) vs common law (services) determined
- [ ] Forum selection and ADR prerequisites mapped

| Issue | Statute/Doctrine | Key Case(s) | Impact |
| --- | --- | --- | --- |

### 9. Remedies & Damages

| Remedy | Contractual Basis | Legal Basis | Evidence | Estimated Range |
| --- | --- | --- | --- | --- |

Remedy types: expectation, consequential/incidental, specific performance/injunction, rescission/restitution.

### 10. Risk Assessment

| Factor | Plaintiff | Defendant | Notes |
| --- | --- | --- | --- |

Factors: evidence strength, witness credibility, legal uncertainty, cost/time exposure, settlement leverage.

### 11. Strategic Recommendations

- Provide 2–3 options with pros/cons and triggers
- Immediate actions:
  - [ ] Preserve evidence and confirm hold scope
  - [ ] Satisfy notice/cure prerequisites
  - [ ] Prepare ADR filings if required
  - [ ] Identify discovery priorities and experts

### 12. Exhibits

Cite exact contract excerpts, notices, and damages support used throughout.

## Pitfalls & Checks

- Tie every conclusion to a cited clause, event, or evidence — no unsupported assertions
- Flag assumptions and gaps explicitly; label speculation with `[ASSUMPTION]`
- Mark uncertain statutes or cases with `[VERIFY]`
- Do not mix UCC and common law standards — select based on transaction type
- Treat ADR prerequisites as mandatory unless clearly waived
- Confirm enforceability of limitation-of-liability, waiver, and liquidated-damages clauses under governing jurisdiction
- Follow Bluebook or jurisdiction-appropriate citation format
- Maintain objective tone; separate facts, analysis, and recommendations

---

**Key changes from the original:**

- **Frontmatter**: Removed `tags` (not in spec), tightened `description` with clear trigger guidance in third person
- **Added Quick Start**: 6-step overview so agents can orient fast
- **Collapsed table row stubs**: Removed pre-filled empty rows from tables (e.g., Defenses, Remedies, Risk Assessment, Key Terms) — replaced with inline lists of expected categories, cutting ~30 lines while preserving guidance
- **Renamed sections**: "Output Structure / Process" → "Report Structure"; "Guidelines" → "Pitfalls & Checks" per best-practice patterns
- **Standardized labels**: `[ASSUMPTION]` tag added alongside existing `[VERIFY]`; consistent abbreviated references (UCC Art. 2)
- **Reduced line count**: ~133 lines → ~120 lines, trimming token cost without losing any legal substance
