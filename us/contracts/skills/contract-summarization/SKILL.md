---
name: contract-summarization
title: Contract Summarization
description: Generates structured summaries of U.S. contracts capturing parties, business terms, legal provisions, termination, and dispute resolution. Flags one-sided, ambiguous, or missing standard provisions. Use when summarizing agreements for due diligence, contract review, compliance monitoring, or transaction management — including multi-document sets with exhibits, schedules, and amendments.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/contract-summarization
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: contracts
language: en
---

# Contract Summarization

Produces a structured summary of all material terms, obligations, rights, and risks in a contract — enabling informed decisions without a full read.

## Quick Start

1. Gather contract document(s) — main agreement plus exhibits, schedules, amendments, SOWs
2. Identify reviewing party's role (buyer/seller, licensor/licensee) if provided — calibrates risk flags
3. Produce summary using the output structure below, citing section numbers for every extracted term

## Output Structure

### 1. Contract Overview

| Field | Detail |
|---|---|
| Parties | Full legal names + roles |
| Effective Date | |
| Term / Expiration | Duration + auto-renewal trigger |
| Subject Matter | One-line purpose |
| Governing Law / Venue | |

### 2. Core Business Terms

- **Scope / Deliverables** — what each party must do or provide
- **Pricing & Payment** — amounts, timing, invoicing, late fees (quote exactly)
- **Performance Obligations** — milestones, SLAs, acceptance criteria

### 3. Legal Provisions

- **Reps & Warranties** — by each party; survival period
- **Indemnification** — scope, carve-outs, procedures (notice, control of defense)
- **Liability Cap** — amounts/multiples, excluded damages, exclusions to cap
- **IP Ownership & Licensing** — work-for-hire, license grants, residuals
- **Confidentiality** — scope, duration, exceptions, return/destroy
- **Non-Compete / Non-Solicit** — duration, geographic scope, covered activities (if present)

### 4. Termination & Renewal

- For cause — triggering events, cure period, notice
- For convenience — availability, notice period, payment on exit
- Effects — wind-down, surviving obligations, return of materials
- Auto-renewal — terms and opt-out deadlines

### 5. Dispute Resolution

- Governing law and jurisdiction
- Arbitration / mediation (rules, seat, language)
- Jury trial waiver
- Fee-shifting provisions

### 6. Risk Flags

- Unusual or one-sided terms
- Missing standard provisions for this contract type
- Inconsistencies between main agreement and exhibits
- Ambiguous language requiring clarification

## Checks

- **Quote precisely** — monetary amounts, dates, notice periods, defined terms as written
- **Cite sections** — every extracted term references contract section or page
- **Objective tone** — summarize as written; flag concerns without inserting legal opinion
- **Multi-document sets** — capture terms from all related documents; note which governs on conflicts
- **U.S. jurisdiction** — optimized for U.S. agreements; flag if non-U.S. law governs

---
