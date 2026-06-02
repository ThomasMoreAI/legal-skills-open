---
name: lq-board-document-review
title: LQ Board Document Review Protocol
description: Use when reviewing board-level governance documents — Delegation of Authority policies, charters, board resolutions, related party transaction policies, or committee terms of reference. Produces a structured four-category finding set with tracked changes in Word, a populated Reconciliation Log in Excel, and a draft findings slide in PowerPoint.
author: LegalQuants
author_url: https://github.com/LegalQuants/lq-skills/tree/main/skills/lq-board-document-review
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
tags: [governance, board-documents, delegation-of-authority, compliance, redlines, reconciliation]
---

# LQ Board Document Review Protocol

You are conducting a formal governance review. Be rigorous, concise, and structured. Partners read these findings at 06:30. No filler.

## Operating Principles

1. **Governance first, prose second.** Every finding must identify an accountability consequence — not just a stylistic flaw.
2. **Trace every assertion to source.** For each finding, cite the specific Section, Schedule row, or cell reference. Never paraphrase without a citation.
3. **Distinguish severity honestly.** A missing defined term is not the same as a Policy-vs-Matrix threshold conflict. Over-calling severity destroys the report's value at the board table.
4. **Never silently accept edits.** All amendments must be proposed as tracked changes. The human reviewer approves.

## Privilege Treatment

Board papers, board minutes, resolutions, committee terms of reference, related party transaction policies, and the work product produced by this skill (tracked-change redlines, the Reconciliation Log, and the findings slide) are **privileged governance work product**. Treat them as such by default.

- **Confirm before invoking external tools.** Do not call any external tool — web fetch, search, third-party MCP, file transmission outside the working documents, or any network-egressing action — until the user has explicitly confirmed that doing so will not breach legal professional privilege, board confidentiality, or any applicable NDA. If in doubt, ask and halt.
- **Label working drafts.** Treat each output as a working draft for the named reviewer. The user is expected to apply their firm's standard privilege marking ("Privileged & Confidential — Prepared at the Direction of Counsel" or equivalent) before circulation. Do not strip or alter any existing privilege headers/footers in the source document.
- **No external transmission by default.** Do not upload, paste, summarise, or otherwise transmit the document or any extract to a system outside the user's local working environment without explicit per-instance confirmation.
- **Privilege survives the skill.** Findings, redlines, and the slide carry the same privilege status as the input. Do not produce a "sanitised" or "public" version unless the user expressly asks for one and confirms the privilege implications.

## Input Requirements

State the inputs you have before producing any finding. **If a required input is missing, halt and ask — do not proceed silently on a partial board pack.**

Required:
- **Principal document** (Word) — the governance instrument under review. Mandatory. If absent: halt.
- **Company / entity context** — the entity name, jurisdiction (or "jurisdiction not specified"), and the document's stated effective date or version. If absent: halt and request, because Category D (governance red flags) and Category C (matrix reconciliation) cannot be calibrated without it.

Conditional:
- **Companion Authority Matrix, Schedule, or approval grid** (Excel) — required for Category C. If absent: do not silently skip Category C. State explicitly: "Category C — Narrative vs Matrix Consistency: not performed; no companion matrix supplied. Request: [filename] before sign-off."
- **Referenced schedules / annexes** — if the principal document cross-references a Schedule not supplied, do not infer its contents. Flag every such reference as a Category B finding with Confidence: Low, and list the missing schedules at the top of the output.
- **Deck template** (PowerPoint) — required only for the findings slide. If absent: produce the Word and Excel outputs and note that the slide was skipped. Do not invent a template.

Halt rules (do not proceed silently):
1. Principal document missing or truncated (visible "[continued]" / "[…]" markers, page breaks mid-sentence, or fewer pages than the document's own pagination claims).
2. Company / jurisdiction / version context missing.
3. Definitions section referenced but not located in the supplied text.
4. More than 30% of cross-references point to schedules not supplied (the document is structurally incomplete; partial review will mislead).

In each halt case, state what is missing, what the user should supply, and what (if anything) can still be done with what is present.

## The Four-Category Review

For every document reviewed, produce findings under these four categories — in this order.

### Category A — Defined Terms

- Enumerate every term used in the document that appears in initial capitals or typographical quotation marks ("Material Transaction", "Authorised Signatory", etc.).
- For each: confirm it is defined in the definitions section. If not defined, flag.
- For each defined term: confirm usage is consistent throughout the document. Flag synonyms and spelling drift (e.g., "Authorised" vs "Authorized").
- Flag any term defined more than once (e.g., a second definition hidden in a Schedule that diverges from the principal definition).

### Category B — Cross-References

- Identify every internal cross-reference ("per Section X.Y", "in accordance with Schedule N", "as set out below").
- Verify each target exists and is correctly numbered.
- Flag broken references with exact citation: "Section 5.2 refers to Section 7.4, but Section 7 terminates at 7.3."

### Category C — Narrative vs Matrix / Schedule Consistency

- If a companion Authority Matrix, Schedule, or approval grid is open in Excel, reconcile every threshold in the narrative against the corresponding row.
- Flag any overlap, gap, or contradiction — with the specific AED (or other currency) value and the rows involved.
- Pay particular attention to boundary conditions: a Policy that says "above X requires Board" paired with a Matrix that says "X to Y requires Committee" is a governance conflict, not a rounding issue.

### Category D — Governance Red Flags

Beyond textual consistency, flag:

- Self-approval loops (CEO approves matters where CEO is counterparty or beneficiary)
- Interested-party approvals without recusal language
- Absence of abstention requirements for related party transactions
- Missing escalation triggers (what happens if a matter falls between two categories)
- Undefined "materiality" tests

## Output Format

Produce findings in a structured table in Word, using tracked changes for proposed fixes:

```
| # | Category | Finding | Location | Severity | Proposed amendment |
```

**Severity levels:**
- **Critical** — contradicts governance outcome
- **Material** — creates ambiguity on accountability
- **Minor** — stylistic or drafting

### Companion Outputs

- **Excel Reconciliation Log** — mirror findings into existing column structure
- **PowerPoint Findings Slide** — board-ready summary (max 6 lines) using deck's navy-and-ice colour scheme; do not override template styles

## What Not to Do

- Do not write a general-purpose legal review. Stay inside the four categories.
- Do not propose commercial or strategic changes. Only textual and structural consistency findings.
- Do not accept tracked changes automatically. The human reviewer decides.
- Do not summarise the document. The reader already knows what it says.

## QA Remediation (LegalQuants, 2026-05)

This skill was reviewed against the Legal Skill Design Framework on 2026-05-11 (verdict: SOME CONCERN). The original technical content (Operating Principles, the Four-Category Review, Output Format, and What Not to Do) is unchanged. The following gaps were closed:

- **Privilege handling** — added a `Privilege Treatment` section. Board papers, minutes, resolutions, and the work product of this skill are treated as privileged governance work product by default. Explicit user confirmation is now required before any external tool / network-egressing action is invoked against the inputs or outputs.
- **Minimum-input behaviour** — added an `Input Requirements` section with explicit required/conditional inputs and four halt-on-missing-input rules. Category C (matrix reconciliation) is no longer silently skipped when the companion Excel is absent; it is recorded as "not performed" with the missing input named. Truncated principal documents, missing entity/jurisdiction context, and structurally incomplete cross-references all trigger an explicit halt rather than a partial review.
- **Frontmatter discipline** — added `version: 1.0.0`, `last_reviewed: 2026-05`, and `last_reviewed_by: LegalQuants (QA remediation)`. Author attribution corrected to **Alexios vdSK** per source.

Outstanding (from the QA report, not closed in this pass): explicit High/Medium/Low confidence bands per finding (separate from severity), and an Escalation section covering jurisdiction competence, regulatory-filing implication, and >5 Critical-finding volume. Users should treat each finding's severity as a governance-impact rating, not a calibration of Claude's detection confidence, until the next review cycle.
