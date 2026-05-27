---
name: plan-of-liquidation-and-dissolution
title: Plan of Liquidation and Dissolution
description: Drafts a U.S. corporate Plan of Liquidation and Dissolution for voluntary wind-downs. Triggers when inputs mention liquidation, voluntary dissolution, winding up, dissolution resolution, creditor claims period, Form 966, or shareholder distribution calculations. Use after board and shareholder authorization is complete.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/plan-of-liquidation-and-dissolution
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
tags: [agreement, drafting, transactional]
---

# Plan of Liquidation and Dissolution

Produces a governance-compliant dissolution plan covering approval history, creditor notice, claims administration, liquidation sequencing, distribution mechanics, tax clearance, and state termination filings.

## Quick Start

Gather before drafting:

1. **Entity docs** — charter, bylaws, shareholder agreement, state of incorporation.
2. **Board resolution** — date, quorum, vote counts, authorization language.
3. **Shareholder vote** — consents or meeting results with class-vote handling if applicable.
4. **Financials** — stock ledger (class/rank), asset/liability schedules, pending litigation, tax status.
5. **Filing requirements** — state secretary of state forms/fees/waiting periods, Form 966 deadline.
6. **Creditor communications plan** — known creditor list, publication channel for unknown creditors.

## Core Workflow

### 1. Build Entity & Jurisdiction Matrix

| Item | Inputs | Controls |
|---|---|---|
| Entity identity | Legal name, formation state, tax ID, principal office | Mirror formation records exactly |
| Timeline | Target adoption, creditor response, filing dates | State-compliant intervals [VERIFY] |
| Approvals | Board + shareholder actions, class vote mechanics | Include vote tallies and rights analysis |
| Creditor admin | Known/unknown creditor list, claim deadlines, reserves | Align notice language with statute [VERIFY] |
| Distribution | Liabilities stack, reserves, preference classes | Document liquidation preference and conversion formula |
| Tax package | EIN, filing history, state tax IDs | Integrate Form 966 and final tax obligations |

### 2. Draft Sections (Fixed Order)

1. **Preamble & Recitals** — corporate identity, statutory basis, date, reasoned basis.
2. **Authorization** — board meeting/consent details, shareholder vote by class, exhibit references.
3. **Notice & Claims** — delivery methods, deadlines, publication terms, claim form language.
4. **Winding Up** — contract closure, litigation handling, asset conversion strategy.
5. **Priority Payments** — expense waterfall: liquidation costs → wages → taxes → secured → unsecured → contingencies. Include reservation schedule.
6. **Shareholder Distribution** — class-based preference, pro rata mechanics, in-kind vs. cash, per-share calculation worksheet.
7. **Tax & Compliance** — Form 966 filing, final returns, state/federal clearances, record retention.
8. **Dissolution Filings** — Articles/Certificate of Dissolution, signature authority, filing checklist.
9. **Execution** — effective date, cure period, officer certification, signature blocks.

### 3. Deliverables Checklist

- `[ ]` Date-stamped preamble and recitals
- `[ ]` Governance evidence paragraph for each required threshold
- `[ ]` Creditor notice log template and publication proof list
- `[ ]` Reserve memo (disputed, environmental/contingent, tax exposure)
- `[ ]` Distribution worksheet by share class
- `[ ]` State filing exhibit index with filing copies
- `[ ]` Post-filing action list with retention and audit handling

## Pitfalls & Checks

- Define "dissolved," "wound up," and "terminated" separately — never interchange without definition.
- Preserve board/shareholder decision chronology as enforceable fact paragraphs.
- Never state creditors are "waived" without documented statutory or consent basis.
- Unknown creditors: use published notice period exactly as permitted by state law [VERIFY].
- Include separate class distribution schedule whenever preferred rights exist, even if zero-value.
- Add statutory references only after jurisdiction verification [VERIFY].
- Nonprofit wind-down: route residual assets to qualified tax-exempt recipients per governing tax law [VERIFY].
- Retain closing papers and tax support for statutory period (typically 3–7 years; confirm exact duration).
