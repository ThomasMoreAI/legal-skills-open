---
name: executive-employment-agreement
title: Executive Employment Agreement
description: Drafts U.S. executive employment agreements covering compensation, equity, severance, and restrictive covenants tailored to jurisdictional enforceability. Use when drafting C-suite or senior executive employment agreements, executive offer conversions, or negotiated employment terms involving severance, change in control, equity vesting, non-compete, or non-solicit provisions.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/executive-employment-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: employment
language: en
---

# Executive Employment Agreement

Produces a negotiation-ready executive employment agreement aligned to term sheet, board approvals, and jurisdictional enforceability.

## Quick Start

Gather these inputs before drafting:

1. **Parties** — entity name, type, address; executive name and address
2. **Role** — title, reporting line, location, start date
3. **Compensation** — base salary, bonus, equity, benefits, perquisites, expenses
4. **Term and termination** — at-will vs. fixed; Cause/Good Reason definitions; notice/cure; severance; CIC treatment
5. **Governing law** — jurisdiction, dispute forum
6. **Equity plan** — plan name, award type, vesting schedule, award agreement
7. **Restrictive covenants** — jurisdictional limits, consideration, permitted scope

Flag any missing items before drafting.

## Core Workflow

1. **Extract terms** from supplied documents; list gaps
2. **Draft** using section order below with required defined terms
3. **Populate** compensation, termination, and covenant tables
4. **Run enforceability checks** — at-will consistency, covenant enforceability, 409A exposure
5. **Finalize** with signature blocks and notice addresses

### Section Order

1. Parties; Effective Date
2. Position; Duties; Reporting
3. Term; At-Will or Fixed Term
4. Compensation
5. Bonus and Incentive Compensation
6. Equity Awards
7. Benefits and Perquisites
8. Expenses and Reimbursements
9. Termination and Severance
10. Restrictive Covenants
11. Confidentiality; IP Assignment
12. Dispute Resolution; Governing Law
13. Miscellaneous (Notices, Assignment, Waiver, Entire Agreement, Severability, Counterparts, 409A)
14. Signatures

### Required Defined Terms

| Term | Content |
|---|---|
| "Company" | Full legal name and entity type |
| "Executive" | Full legal name |
| "Effective Date" | Specific date |
| "Cause" | Enumerated triggers; notice/cure if applicable |
| "Good Reason" | Enumerated triggers; notice/cure |
| "Disability" | Plan reference or time-based standard |
| "Change in Control" | Equity plan definition or standalone |
| "Confidential Information" | Scope and exclusions |
| "Restricted Period" | Covenant duration |

### Compensation Capture

| Item | Required Fields |
|---|---|
| Base Salary | Annual amount; cadence |
| Sign-On Bonus | Amount; timing; clawback |
| Annual Bonus | Target; metrics; discretion; timing |
| Equity Award | Type; size; vesting; cliff; exercise price; plan ref |
| Benefits | Health; retirement; life/STD/LTD; PTO |
| Perquisites | Car; club; relocation; financial planning |
| Expenses | Standard; documentation; policy ref |

### Termination Matrix

| Trigger | Severance | Benefits | Equity |
|---|---|---|---|
| Without Cause | Salary multiple; pro-rated bonus | COBRA/employer-paid | Acceleration if negotiated |
| For Cause | Accrued only | Accrued only | Forfeit or per plan |
| Good Reason | Same as Without Cause | Same as Without Cause | Same as Without Cause |
| Voluntary | Accrued only | Accrued only | Per plan |
| Death/Disability | Per negotiated policy | Per plan | Per plan |

### Restrictive Covenants

For each covenant (non-compete, employee non-solicit, customer non-solicit, non-disparagement), specify: duration, geographic scope, activity scope, consideration, and enforcement notes.

### Dispute Resolution

| Option | Required Inputs |
|---|---|
| Arbitration | Provider, locale, rules, cost allocation, fee shifting |
| Litigation | Venue, jurisdiction, jury waiver |
| Mediation | Timing, provider, cost split |

### Mandatory Clauses

- Entire agreement; written amendments
- Severability and reformation (especially covenants)
- Assignment: permitted for Company, prohibited for Executive
- Notice method and addresses
- Withholding and tax compliance
- Section 409A compliance or exemption
- Injunctive relief for covenant breaches
- Counterparts and electronic signatures

## Pitfalls

- **At-will conflicts** — if at-will, state explicitly; ensure severance language does not create an implied term.
- **Missing terms** — flag and request specifics; never guess business terms or use placeholders.
- **Non-compete enforceability** — heavily jurisdiction-dependent; mark with `[VERIFY]` if state law is uncertain.
- **Equity conflicts** — defer to equity plan and award agreement; do not create conflicting terms.
- **409A exposure** — include safe-harbor language for any deferred compensation; use `[VERIFY]` for public issuers.
- **Severance conditions** — always condition on execution of release and continued covenant compliance.
- **Cause/Good Reason alignment** — match definitions to negotiated notice and cure periods.
- **Governing law consistency** — align with restrictive covenant enforceability strategy.

---

Key changes from the original:

- **Removed `tags`** — not part of the Agent Skills spec; only `name` and `description` are required frontmatter
- **Tightened description** — removed "Trigger keywords:" label; wove discovery terms naturally into the description
- **Restructured body** — follows the recommended Overview / Quick Start / Core Workflow / Pitfalls pattern
- **Consolidated Prerequisites into Quick Start** — same info, fewer tokens
- **Trimmed Termination Matrix** — removed Definition and Notice/Cure columns (redundant with the defined terms table)
- **Replaced empty Restrictive Covenant table** — the original had blank cells; replaced with a concise prose instruction
- **Renamed Guidelines to Pitfalls** — matches best-practice section naming; trimmed the "use consistent defined terms" guideline (obvious for any drafter)
- **Reduced from 127 to ~107 lines** — more token-efficient while preserving all domain accuracy and legal intent
