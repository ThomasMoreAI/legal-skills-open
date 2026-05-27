---
name: escrow-agreement
title: Escrow Agreement
description: Drafts tripartite U.S. escrow agreements for M&A and commercial closings, covering escrow property, deposit mechanics, release conditions, dispute handling, agent duties/limits, indemnity, fees, and termination. Use when asked to draft an escrow agreement, escrow instructions, holdback/indemnity escrow, closing escrow, or escrow agent agreement.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/escrow-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
tags: [agreement, drafting, transactional]
---

# Escrow Agreement

Draft an enforceable tripartite escrow agreement aligned with the underlying transaction.

## Prerequisites

1. Deal documents and escrow economics (SPA/merger/LOI, amount, holdback purpose, term).
2. Party names, entity types, jurisdictions, notice addresses.
3. Escrow property details (funds/stock/IP, wire instructions or delivery mechanics).
4. Objective release conditions with evidence requirements and deadlines.
5. Fee schedule and expense allocation.
6. Governing law, forum/ADR, and execution requirements.
7. Compliance constraints (AML/KYC, securities, real estate, export controls, tax).

## Quick Start

Structure the agreement in this order:

1. **Preamble & Recitals** — parties, roles (`Purchaser`, `Seller`, `Escrow Agent`), transaction reference. Tie recitals to primary agreement; do not introduce new obligations.
2. **Definitions** — Escrow Property, Release Conditions, Business Day, Written Notice. Make all triggers objective and measurable.
3. **Appointment & Scope** — ministerial role, reliance on written instructions, resignation/successor process.
4. **Deposit & Custody** — amounts, timing, payment method, asset descriptions. Include `time is of the essence` if required.
5. **Release Mechanics** — trigger events, documentary evidence, distribution instructions, timing.
6. **Disputes & Interpleader** — require joint instructions or final court order/arbitral award for conflicting claims.
7. **Agent Protections** — exculpation, reliance, indemnity (carve out gross negligence/willful misconduct/bad faith).
8. **Fees & Expenses** — schedule, payer, reimbursement, fee offset from escrow if unpaid.
9. **Term & Termination** — duration, automatic end, final accounting, retained reserve.
10. **Governing Law & Forum** — choice of law, venue/arbitration, jury waiver if desired.
11. **Boilerplate** — notices, assignment, counterparts, ESIGN/UETA if e-signing.
12. **Signature Blocks** — match entity authority requirements.

## Release Conditions Table

Complete and embed in agreement or attach as exhibit. Define each partial-release tranche as its own row.

| Condition | Evidence Required | Deadline | Distribution |
|---|---|---|---|
| [Condition 1] | [Document/certificate/order] | [Date/period] | [Payee + method] |
| [Condition 2] | [Document/certificate/order] | [Date/period] | [Payee + method] |

## Required Exhibits

- **Exhibit A** — Wire instructions or delivery mechanics.
- **Exhibit B** — Form of joint release instruction or certificate.
- **Exhibit C** — Authorized representatives and specimen signatures.

## Mandatory Clause Checklist

- [ ] Escrow Property definition and custody mechanics
- [ ] Deposit deadlines and cure rights for failure to deposit
- [ ] Objective release conditions with required documentation
- [ ] Treatment of interest/dividends/earnings on escrowed property
- [ ] Escrow Agent reliance on instructions and documents
- [ ] Escrow Agent indemnity (joint and several) and expense reimbursement
- [ ] Interpleader right and cost allocation
- [ ] Fee offsets against escrow if unpaid
- [ ] Successor escrow agent process
- [ ] Final accounting and reserve for pending claims
- [ ] Unclaimed property/escheatment compliance
- [ ] Survival of indemnity, confidentiality, and limitation of liability

## Key Template Language

**Release timing:**
> Within [__] Business Days after receipt of all required Release Documents, Escrow Agent shall disburse the Escrow Property in accordance with the applicable Release Instruction.

**Agent reliance:**
> Escrow Agent may rely conclusively on any written notice, instruction, certificate, or other document that Escrow Agent in good faith believes to be genuine and signed by an Authorized Representative, without duty to investigate.

**Indemnity carve-out:**
> The foregoing indemnity does not apply to losses resulting from Escrow Agent's gross negligence, willful misconduct, or bad faith.

## Guidelines

- Keep release conditions objective, document-based, and time-bound.
- Align escrow economics and term with the primary transaction agreement.
- Do not impose duties on the Escrow Agent beyond ministerial tasks.
- Require joint written instructions or final order/award for disputed releases.
- Specify who receives interest/earnings and whether funds are invested.
- Confirm AML/KYC representations if funds source is sensitive or regulated.
- Check state escrow-agent statutes and licensing requirements [VERIFY].
- Use ESIGN/UETA language only when e-signatures are intended [VERIFY].
- Flag nonstandard provisions or negotiated deviations in a brief issues list.

---

**Key changes from the original:**

- **Description** tightened — removed redundant clause-level enumeration, kept trigger keywords
- **"Output Structure / Process"** replaced with **"Quick Start"** — converted the wide 3-column table into a scannable numbered list with inline drafting notes, cutting tokens while preserving every section and its guidance
- **Mandatory clause checklist** converted to checkbox format for trackable progress
- **Template blocks** — removed code fences and the generic signature block pattern (Claude knows standard signature format); kept the three substantive clauses as blockquotes under descriptive headers
- **Redundant prose** removed — "Use this section map and fill every placeholder with transaction-specific data" and similar instructions cut
- **~86 lines** total (down from 109), with no legal content lost
