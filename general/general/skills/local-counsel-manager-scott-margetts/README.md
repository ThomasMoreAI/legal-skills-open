# local-counsel-manager

**Plugin:** LPM Core Plugin (Skill 11 of 14)
**Part of:** [LPM Skills for Claude](https://github.com/legalopsconsulting/lpm-skills)
**Status:** Phase 2 complete

---

## What this skill does

Manages the external local counsel lifecycle on multi-jurisdiction legal matters — from firm selection and engagement setup through instruction management, performance monitoring, scope enforcement, and relationship escalation.

The skill is built around a simple insight: most LC problems are instruction failures, not capability failures. LC firms interpret ambiguity as authorisation. Gaps in scope letters become scope creep. Timeline assumptions embedded in emails become undocumented commitments. This skill is designed to prevent those failures — and to manage them efficiently when they occur.

---

## Modes

| Mode | When to use |
|---|---|
| **Mode 1 — Selection and setup** | Selecting LC for a jurisdiction, setting up a new engagement |
| **Mode 2 — Instruction design** | Drafting or amending LC instructions |
| **Mode 3 — Performance monitoring** | Managing the check-in cadence, tracking response health, escalating underperformance |
| **Mode 4 — Scope enforcement and escalation** | LC signals overreach; billing anomalies referred from invoice review; relationship-level issues |

---

## Usage notes (v1)

**Mode 4 — pasted emails:** When pasting an email directly from an LC contact, prefix it with `[FROM LC]` before pasting. This tells the skill the email is incoming LC correspondence, not an outbound draft for review. Without the tag, describe the situation in your own words: *"Our German LC has emailed saying they need to revise their fee estimate — here is their email."*

**Mode 3 — escalation drafts:** The skill produces the email draft for the current escalation stage (Day 3, Day 5, or Day 7 — whichever applies) plus the full escalation path as a named action table. Invoke the skill again for each subsequent stage.

---

## What it doesn't do

- **LC invoice review and disbursement treatment** — handled by [billing-cycle-manager](../billing-cycle-manager/). This skill designs the engagement architecture that invoice review depends on. The two skills are interdependent.
- **Legal quality assessment of LC advice** — attorney function. This skill manages the operational relationship, not the legal content.
- **Conflict screening** — attorney and risk function. This skill ensures the process is followed; it does not run the clearance.

---

## Inputs

- Matter scope description or matter-intake-scoping output
- LC instruction letter (for Modes 2–4)
- LC correspondence — prefix pasted emails with `[FROM LC]` for reliable Mode 4 routing
- Matter timeline and milestone list
- Fee basis and budget allocation for the LC engagement

---

## Outputs

All outputs produced as `.docx` files. Matter records belong in the matter folder.

| Mode | Primary output |
|---|---|
| Mode 1 | Selection recommendation memo |
| Mode 2 | Instruction letter (formal, ready to issue); instruction amendments |
| Mode 3 | Email draft for current escalation stage; escalation path action table; check-in cadence recommendation |
| Mode 4 | Scope response letter; attorney action table; relationship escalation briefing note |

---

## Design principles applied

This skill applies the [LPM Core Plugin design principles](../README.md), including:

- **Email-first input** — LC correspondence is the primary input across all modes
- **Document output by default** — instruction letters and scope response letters are contractual documents, not chat output
- **Automate capture, surface for confirmation** — the skill drafts the output; the LPM confirms before sending
- **Embed in existing workflows** — instruction amendments, escalation emails, and scope responses integrate with Outlook and the matter folder structure
- **LPM vs attorney boundary** — the skill designs and enforces the engagement architecture; attorneys own legal quality and relationship conversations at partnership level
- **Template skeleton for document outputs** — instruction letter, scope response letter, and escalation emails are structured templates the skill populates, not outputs the skill decides whether to produce

---

## Skills this one works with

| Skill | Relationship |
|---|---|
| matter-intake-scoping | Jurisdiction list and scope baseline → LC selection and instruction design |
| scope-change-controller | OOS change records → instruction amendments |
| billing-cycle-manager | LC invoice anomalies → scope enforcement and relationship escalation |
| matter-plan-builder | LC milestones and dependencies → check-in cadence |
| timeline-generator | Cascaded deadline changes → instruction amendments |
| stakeholder-comms-planner | LC firm registration as external stakeholders |
| status-report-drafter | LC performance issues → risks and issues section |

---

## License

Apache 2.0. See [LICENSE](../../LICENSE).

---

## What this skill does

Manages the external local counsel lifecycle on multi-jurisdiction legal matters — from firm selection and engagement setup through instruction management, performance monitoring, scope enforcement, and relationship escalation.

The skill is built around a simple insight: most LC problems are instruction failures, not capability failures. LC firms interpret ambiguity as authorisation. Gaps in scope letters become scope creep. Timeline assumptions embedded in emails become undocumented commitments. This skill is designed to prevent those failures — and to manage them efficiently when they occur.

---

## Modes

| Mode | When to use |
|---|---|
| **Mode 1 — Selection and setup** | Selecting LC for a jurisdiction, setting up a new engagement |
| **Mode 2 — Instruction design** | Drafting or amending LC instructions |
| **Mode 3 — Performance monitoring** | Managing the check-in cadence, tracking response health, escalating underperformance |
| **Mode 4 — Scope enforcement and escalation** | LC signals overreach; billing anomalies referred from invoice review; relationship-level issues |

---

## What it doesn't do

- **LC invoice review and disbursement treatment** — handled by [billing-cycle-manager](../billing-cycle-manager/). This skill designs the engagement architecture that invoice review depends on. The two skills are interdependent.
- **Legal quality assessment of LC advice** — attorney function. This skill manages the operational relationship, not the legal content.
- **Conflict screening** — attorney and risk function. This skill ensures the process is followed; it does not run the clearance.

---

## Inputs

- Matter scope description or matter-intake-scoping output
- LC instruction letter (for Modes 2–4)
- LC correspondence (emails, invoice extracts, scope queries)
- Matter timeline and milestone list
- Fee basis and budget allocation for the LC engagement

---

## Outputs

All outputs produced as `.docx` files. Matter records belong in the matter folder.

| Mode | Primary output |
|---|---|
| Mode 1 | Selection recommendation memo |
| Mode 2 | Instruction letter (formal, ready to issue); instruction amendments |
| Mode 3 | Check-in cadence schedule; LC network tracker (`.docx` + CSV export) |
| Mode 4 | Scope response letter; relationship escalation briefing note |

---

## Design principles applied

This skill applies the [LPM Core Plugin design principles](../README.md), including:

- **Email-first input** — LC correspondence is the primary input across all modes
- **Document output by default** — instruction letters and scope response letters are contractual documents, not chat output
- **Automate capture, surface for confirmation** — the skill drafts the output; the LPM confirms before sending
- **Embed in existing workflows** — instruction amendments, escalation emails, and scope responses integrate with Outlook and the matter folder structure
- **LPM vs attorney boundary** — the skill designs and enforces the engagement architecture; attorneys own legal quality and relationship conversations at partnership level

---

## Skills this one works with

| Skill | Relationship |
|---|---|
| matter-intake-scoping | Jurisdiction list and scope baseline → LC selection and instruction design |
| scope-change-controller | OOS change records → instruction amendments |
| billing-cycle-manager | LC invoice anomalies → scope enforcement and relationship escalation |
| matter-plan-builder | LC milestones and dependencies → check-in cadence |
| timeline-generator | Cascaded deadline changes → instruction amendments |
| stakeholder-comms-planner | LC firm registration as external stakeholders |
| status-report-drafter | LC performance issues → risks and issues section |

---

## License

Apache 2.0. See [LICENSE](../../LICENSE).
