# billing-cycle-manager

**Plugin:** LPM Core  
**Skill number:** 8 of 19  
**Status:** v1 built — Phase 1 testing in progress

---

## What it does

Handles the operational execution of the billing cycle across five modes: monthly bill preparation, local counsel invoice review and disbursement treatment, client billing query response, cashflow modelling, and leverage and burn analysis.

This is the execution layer. Budget-and-fee-manager produces the financial analysis — WIP proportionality, variance commentary, FTC ranges. Billing-cycle-manager acts on it operationally: what gets billed this month, how LC fees are treated, how to respond when the client pushes back, whether the cashflow position is sustainable, and whether the staffing mix is going to land the matter within budget.

---

## What it does not do

- **Financial analysis and variance commentary** — that is budget-and-fee-manager (Skill 7). This skill receives the WIP position and acts on it; it does not re-run the proportionality analysis.
- **Scope change assessment** — scope-change-controller (Skill 3) determines whether disputed work is in or out of scope. This skill uses that determination to defend or resolve client billing queries.
- **LC lifecycle management** — local-counsel-manager (Skill 11) handles LC selection, engagement terms, performance monitoring, and relationship escalation. This skill reviews individual LC invoices against agreed terms; relationship-level issues escalate to local-counsel-manager.

---

## Primary input scenarios

1. **End-of-month bill prep** — WIP available, partner wants a billing instruction. What gets billed, what gets deferred, what gets written down.

2. **LC invoice arrives** — review against budget and scope, determine disbursement treatment (pass-through, direct billing, or deferred), approve or query line items.

3. **Client challenges an invoice** — reconstruct the position, determine whether to defend, adjust, or write off, draft the response.

4. **Cashflow modelling** — LC invoices due on short terms, client receipts on long terms. Model the funding gap, identify peak exposure, propose management actions.

5. **Leverage and burn analysis** — actual staffing mix against budget assumptions, predicted total cost at current pace, margin trajectory.

---

## Inputs

- WIP data by matter/phase/fee-earner (pasted, uploaded CSV/Excel, or described)
- LC invoices (uploaded, pasted, or described)
- LC engagement letter or scope summary
- Client billing query (email or described)
- Time recorded by grade (for leverage analysis)
- Expected client billing amounts and payment terms (for cashflow modelling)
- Fee basis and AFA structure where applicable

---

## Outputs

All outputs produced as `.docx` files by default. Billing documents are matter records — they belong in the matter folder.

| Mode | Primary output | Secondary output |
|---|---|---|
| Mode 1 — Bill prep | Billing instruction table | CSV billing export |
| Mode 2 — LC invoice review | Approved/queried amounts + disbursement treatment | LC query letter (if required) |
| Mode 3 — Client billing query | Query response draft | Internal position memo |
| Mode 4 — Cashflow modelling | Funding gap table (weekly/monthly) | Management actions list |
| Mode 5 — Leverage and burn | Leverage table + gearing note | Predicted total cost range |

---

## Cross-skill handoffs

| Direction | Partner skill | What passes |
|---|---|---|
| Receives from | budget-and-fee-manager | WIP review table and confirmed write-off positions → Mode 1 inputs |
| Receives from | scope-change-controller | Scope baseline → Mode 3 defence for informally-requested work |
| Receives from | matter-intake-scoping | LC engagement terms → Mode 2 review reference |
| Sends to | budget-and-fee-manager | Confirmed billing amounts and write-offs → realisation update |
| Sends to | local-counsel-manager | LC invoice anomalies unresolved by query → relationship escalation |
| Sends to | status-report-drafter | Billing cycle summary → financial section of next status report |

---

## Design notes

**The disbursement treatment decision is operational, not administrative.** Whether LC fees are passed through, billed direct, or deferred has cash, relationship, and VAT implications. The skill encodes the three-option framework and the default (Option A — pass-through) with explicit conditions for when the alternatives are appropriate.

**Cashflow modelling is a first-class output, not a flag.** The structural mismatch between LC payment terms (30–45 days) and client payment terms (60–180 days) is predictable and recurring. On a multi-jurisdiction programme with material LC fees, the peak funding gap can be significant. The skill models it with a weekly/monthly funding gap table and produces specific management actions, not generic advice.

**Leverage analysis connects billing execution to budget forecasting.** If actual gearing is materially different from the budget assumption, the predicted total cost changes — regardless of whether total hours are on track. A partner-heavy matter is more expensive than the budget assumed; a junior-heavy matter may produce rework that drives its own cost overrun. The leverage table makes this visible before it becomes a write-off problem.

**Write-down discipline is methodology, not administration.** The skill encodes write-down as a management decision requiring named reasons and partner authorisation — not a correction to make the numbers tidy. The write-down that avoids a difficult conversation today creates a realisation problem that is harder to explain at matter close.

---

## Source references

- Linton, *Legal Project Management* (2014) — Chapter 4 (Matter Costing: billing execution, write-offs); Chapter 1 (Matter Closure: finalise invoices, close matter cost centre).
- Levy, *Legal Project Management* (2015) — write-off causes; billing discipline; client communication on fees.
- CLOC, *LPM for Legal Teams* (2017) — Stage 2: billing guidelines sign-off with outside counsel. Stage 3: compliance with billing guidelines, timely billing.
- Seed material: `budget-and-fee-manager-seed-material-from-status-report-build.md` — source system context (SAP, Aderant, Elite; LC invoices tracked separately); financial disclosure sequencing.
