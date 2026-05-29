# budget-and-fee-manager

**Plugin:** LPM Core  
**Skill number:** 7 of 19  
**Status:** v1 complete — Phase 1 passed, Phase 2 ready

---

## What it does

Builds and monitors fee budgets across the full matter lifecycle.

At matter setup, it translates agreed scope into a phase-based fee estimate — broken down by workstream and jurisdiction, with contingency calculated and justified, and AFA structures (fixed fee, capped fee, phased fixed fees) set up for monitoring from day one.

In flight, it runs WIP reviews: actual spend assessed against budget using a proportionality test (spend relative to progress, not just spend relative to budget), variance explained at root cause level, and forecast-to-complete calculated as a range rather than a point estimate.

When spend has outpaced delivery, it models the options: absorb, recover via fee adjustment, or a hybrid. When scope changes are confirmed by scope-change-controller, it models the financial impact and drafts the fee adjustment communication.

---

## What it does not do

- **Operational billing execution** — that is billing-cycle-manager (Skill 8). Monthly billing prep, LC invoice review, client billing queries, and allocation schedules are out of scope for this skill.
- **Status report financial summary** — status-report-drafter (Skill 1) presents the financial section of the status report. This skill produces the underlying analysis that status-report-drafter consumes. The skills are designed to be used together, not as alternatives.
- **Scope change assessment** — scope-change-controller (Skill 3) determines whether work is in or out of scope. This skill models the financial impact of confirmed OOS work. It does not make the in/out determination.

---

## Primary input scenarios

1. **Budget build at matter setup** — partner asks for a fee estimate (by email, in a call, or at a kickoff). The scope may be fully defined or partially described. This skill produces a structured, phase-based estimate rather than a headline number with no working.

2. **Month-end WIP review** — actual spend is available (pasted from the WIP system, uploaded as a spreadsheet, or described in text). This skill runs the proportionality test, explains variance, and produces a forecast-to-complete.

3. **Realisation alert** — spend is running materially ahead of progress and the partner needs options. This skill assesses recoverability and presents three options (absorb, recover, hybrid) with financial impact quantified.

4. **AFA tracking** — matter runs on a fixed fee, capped fee, or other alternative fee arrangement. This skill tracks burn against the agreed fee at each review, calculates the decision trigger (the point at which options must be exercised, before the cap is breached), and presents options.

5. **Fee adjustment for confirmed OOS** — scope-change-controller has assessed and documented an out-of-scope change. This skill models the financial impact and drafts the internal memo and client-facing fee adjustment letter.

---

## Inputs

- Scope description: email, scoping brief, or matter-intake-scoping output
- WIP data: pasted text, uploaded Excel/CSV, or described figures
- Scope change notice from scope-change-controller (Mode 5)
- Agreed fee or cap amount for AFA matters (Mode 4)
- Team structure and fee earner grade/rate information
- AFA preference and commercial context where relevant

---

## Outputs

All outputs are produced as `.docx` files by default. Skill outputs are matter records and belong in the matter folder.

| Mode | Primary output | Secondary output |
|---|---|---|
| Mode 1 — Budget build | Phase-based budget table with contingency | CSV budget export |
| Mode 2 — WIP review | WIP review table + variance commentary | CSV WIP export |
| Mode 3 — Realisation alert | One-page options memo for partner decision | — |
| Mode 4 — AFA tracking | AFA tracking table + narrative block | — |
| Mode 5 — Fee adjustment | Internal memo + client-facing letter | Updated budget comparison table |

---

## Cross-skill handoffs

| Direction | Partner skill | What passes |
|---|---|---|
| Receives from | matter-intake-scoping | Scope baseline and jurisdiction list → Mode 1 input |
| Receives from | scope-change-controller | Confirmed OOS notice → Mode 5 trigger |
| Receives from | risk-and-issues-manager | Breached financial assumption (RAID log) → Mode 5 trigger |
| Sends to | status-report-drafter | WIP table and FTC range → financial summary section |
| Sends to | scope-change-controller | Variance commentary identifying scope-driven overrun → OOS assessment |
| Sends to | billing-cycle-manager | Confirmed WIP position and write-off decisions → billing prep |

---

## Design notes

**Proportionality over absolute variance.** The central analytical move in this skill is comparing spend percentage to progress percentage, not spend percentage to 100%. A workstream at 85% of budget is not a problem if 90% of the work is done. It is a significant problem if 50% of the work is done. The proportionality test forces this comparison explicitly for every workstream, every review.

**FTC as a range, not a point.** Forecast-to-complete is produced as a range (lower bound if remaining work completes as scoped; upper bound if current burn rate continues). A point estimate implies precision that is not available at mid-matter. The range is more honest and more useful for partner decision-making.

**Scepticism as methodology.** Underspend and near-completion self-reports both require specific confirmation before being accepted at face value. The skill encodes these scepticism checks as explicit steps, not optional judgments.

**AFA monitoring from day one.** On AFA matters, the monitoring question changes: not "are we over budget?" but "have we consumed more of the agreed fee than we have delivered of the agreed work?" The skill applies this test automatically on any matter identified as AFA at setup.

---

## Source references

- Linton, *Legal Project Management* (2014) — Chapter 4: Matter Costing. Analogous, bottom-up, and parametric estimating; contingency assessment; forecasting and variance analysis.
- CLOC, *LPM for Legal Teams* (2017) — Stage 2 (Planning): budget elements. Stage 3 (Execution): fee budget to actuals monitoring.
- International law firm LPM practice (2018) — weekly fee reporting by workstream and market; burn rate monitoring.
- Seed material: `budget-and-fee-manager-seed-material-from-status-report-build.md` — financial methodology cut from status-report-drafter build (3 March 2026). All core analytical principles originate here.
