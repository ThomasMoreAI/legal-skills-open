# resource-planner

**Plugin:** LPM Core  
**Skill number:** 10 of 19  
**Status:** v1 built — Phase 1 testing in progress

---

## What it does

Designs matter team structures, identifies gearing problems, plans team continuity, and models resource conflicts across matters. Works with what is actually available — time entries, stated team structures, known absences, specific named conflicts — and produces analysis and options for the partner.

Law firm resourcing is fluid. Partners staff based on availability, relationships, and workload signals that are informal and lagging. This skill does not produce authoritative resource plans or resolve conflicts. It models the situation, surfaces the financial and delivery implications, and structures the decisions the partner needs to make.

---

## What it does not do

- **Make staffing decisions** — the partner allocates people to matters. This skill models and flags.
- **Access live rate or WIP data** — rates must be provided as input or sourced from the matter budget. Live system data requires a practice management MCP connector (see M365 section in SKILL.md — future capability).
- **Question staffing rationale** — the skill surfaces cost and delivery implications of the actual grade mix. It does not ask why the team is structured the way it is.
- **Resolve professional responsibility questions** — conflicts screening, supervision obligations, and qualification requirements are attorney territory.

---

## Primary input scenarios

1. **Matter setup** — translate scope into a required grade mix, compare to the proposed team, identify gaps.

2. **Mid-matter gearing review** — actual time entries reveal the team is working at the wrong level. Model the cost implications and flag the pattern.

3. **Team member unavailable** — leave, departure, conflict, illness. Assess impact on active workstreams, produce cover options, identify decisions required.

4. **Competing demand across matters** — a specific person is over-allocated. Model the conflict, identify what gives, produce options for the partner.

---

## Inputs

- Matter scope description or matter-intake-scoping output
- Proposed team (grades and names if known)
- Time recorded by grade (pasted, uploaded CSV, or described)
- Matter budget and gearing assumption (from budget-and-fee-manager if available)
- Rate data — from matter budget, system of record, or stated by user (indicative ranges used as fallback)
- Named absences, departure dates, or competing matter demands
- Capacity signals — "who has capacity?" email threads, calendar description, WIP description

---

## Outputs

All outputs produced as `.docx` files by default.

| Mode | Primary output | Secondary output |
|---|---|---|
| Mode 1 — Gearing model | Team structure table with grade/hours/cost by phase | CSV export |
| Mode 2 — Gearing review | Actual vs budget gearing table + variance commentary | CSV export |
| Mode 3 — Continuity planning | Impact assessment + cover options + handover requirements | Decision list for partner |
| Mode 4 — Competing demand | Conflict map + options with trade-offs | Decision list for partner |

---

## A note on rate data

This skill cannot pull billing rates from the practice management system. Rates should be provided from the matter budget (budget-and-fee-manager output) or stated directly. Indicative market ranges are used as fallback only and must be confirmed with Pricing before any client-facing use. A future practice management MCP connector would enable live rate and WIP data — see SKILL.md for detail.

---

## Cross-skill handoffs

| Direction | Partner skill | What passes |
|---|---|---|
| Receives from | matter-intake-scoping | Scope complexity assessment → Mode 1 gearing model |
| Receives from | matter-plan-builder | Phase/task structure → grade-by-phase breakdown |
| Receives from | budget-and-fee-manager | Budget gearing assumption + rates → Mode 2 baseline |
| Receives from | timeline-generator | Milestone dates → continuity planning urgency assessment |
| Sends to | budget-and-fee-manager | Gearing deviation → reforecast trigger |
| Sends to | billing-cycle-manager | Actual grade mix → leverage and burn analysis |
| Sends to | status-report-drafter | Resource constraints affecting delivery → risks section |

---

## Design notes

**Resourcing reality is encoded in the skill.** The skill explicitly acknowledges that law firm capacity data is informal, lagging, and self-reported. It ranks input signals by reliability (calendar > time entries > email responses > WIP) and flags data vintage in every capacity analysis. This prevents the model from presenting a stale picture as a definitive one.

**Practice management integration is a named future path.** A custom MCP server pointed at SAP, Aderant, Elite, or equivalent would deliver live rate and WIP data. The skill methodology is identical — the data quality improves. This is documented in the M365 Connected Mode section as a v2 integration path.

**The delegation test is the core analytical move.** For each block of work: could this be done to adequate quality by someone one grade below the current person? If yes, that is a delegation opportunity with a cost implication. If the grade doesn't exist on the team, that is a resourcing gap.

---

## Source references

- Linton, *Legal Project Management* (2014) — Chapter 7 (Human Resource Allocation and Management); Chapter 1 (Matter Resourcing and People Management as a core LPM discipline).
- CLOC, *LPM for Legal Teams* (2017) — Stage 2: resource allocation and staffing profile.
- Competency Framework Draft — caseload management, prioritisation, delegation, pinch point escalation.
- Belfast LPM Large Projects (Oct 2019) — gearing efficiency, overflow resource planning.
- Lambreth / LawVision (2022) — resource utilisation, alternative staffing, optimising resource allocation.
