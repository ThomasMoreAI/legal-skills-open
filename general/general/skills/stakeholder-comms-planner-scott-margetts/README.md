# stakeholder-comms-planner

**Plugin:** LPM Core  
**Skill number:** 9 of 19  
**Status:** v1 built — Phase 1 testing in progress

---

## What it does

Designs and maintains the communication architecture for legal matters across four modes: stakeholder mapping, communication plan design, reporting hierarchy design for large programmes, and mid-matter comms updates when the stakeholder landscape changes.

The central problem: on complex matters, communication structures evolve rather than being designed. The wrong people get too much information, the right people too little, and nobody intended it that way. This skill makes the design explicit at matter setup — stakeholder register, reporting streams, cadence, hierarchy — and keeps it maintained through the matter lifecycle.

---

## What it does not do

- **Status reporting** — status-report-drafter (Skill 1) produces the reports. This skill designs who receives them, at what frequency, and in what format. The two skills are designed to be used together: stakeholder-comms-planner at setup, status-report-drafter at each reporting cycle.
- **Resource planning** — team structure and staffing decisions are handled by resource-planner (Skill 10). This skill captures who the team members are as stakeholders and what they need to receive; it does not design the team itself.
- **Local counsel management** — LC communication cadence and instruction format are handled by local-counsel-manager (Skill 11). This skill captures LC leads as stakeholders in the communication plan.

---

## Primary input scenarios

1. **New matter setup** — identify all stakeholders, classify by influence and interest, assign communication roles, design the reporting rhythm for both internal and client-facing streams.

2. **Multi-jurisdiction programme** — build a three-tier reporting hierarchy (jurisdiction → regional → programme → client), define escalation thresholds, and resolve the HQ vs regions contact problem before it causes relationship damage.

3. **Stakeholder landscape change** — a key contact has changed, the client has restructured, or a new workstream has been added. Update the communication plan without starting from scratch.

4. **Partner asks how to structure client communication** — design a reporting rhythm that meets the client's information needs, fits the partner's availability, and reduces ad hoc communication from the client.

---

## Inputs

- Matter description and known parties (client contacts, internal team, third parties)
- Client organisational structure (who reports to whom on the client side)
- Reporting preferences and constraints (partner availability, client reporting windows, board meeting schedules)
- Matter timeline and phase structure (from matter-plan-builder if available)
- Description of stakeholder landscape changes (for Mode 4)

---

## Outputs

All outputs produced as `.docx` files by default. Stakeholder registers and communication plans are matter records — they belong in the matter folder.

| Mode | Primary output | Secondary output |
|---|---|---|
| Mode 1 — Stakeholder mapping | Stakeholder register | CSV export for SharePoint tracking |
| Mode 2 — Communication plan | Communication schedule + stream design | CSV export |
| Mode 3 — Reporting hierarchy | Hierarchy diagram + tier descriptions + escalation thresholds | — |
| Mode 4 — Mid-matter update | Updated stakeholder register + revised communication plan | Change summary |

**Note on sensitivity:** Stakeholder register sensitivities and influence/interest classifications are internal analytical tools. They must never appear in client-facing documents.

---

## Cross-skill handoffs

| Direction | Partner skill | What passes |
|---|---|---|
| Receives from | matter-intake-scoping | Stakeholder list and client org structure → Mode 1 input |
| Receives from | matter-plan-builder | Phase structure and milestone schedule → Mode 2 cadence design |
| Sends to | status-report-drafter | Who receives which report format and at what frequency |
| Sends to | timeline-generator | Communication milestones as fixed-date constraints |
| Sends to | scope-change-controller | Who has authority to approve scope changes |
| Sends to | billing-cycle-manager | Billing contact and financial communication cadence |

---

## Design notes

**Power/interest framework.** Stakeholders are classified by their power to influence the matter outcome and their interest in its progress — not by their seniority. A junior in-house contact with daily operational involvement may warrant more intensive communication management than a C-suite executive who has delegated the matter entirely.

**Two streams, designed separately.** Internal reporting (management by exception — what requires partner attention) and client-facing reporting (managed confidence — demonstrating competent progress management) have different purposes and different standards. The most common communication failure is treating them as the same stream.

**The HQ vs regions problem.** On cross-border matters with multiple client-side contacts, conflicting communication hierarchies cause inconsistent information reaching different parts of the client organisation. This skill names the problem explicitly at setup and produces a clear resolution: one named primary contact per reporting stream, agreed with the partner before the first update goes out.

**Cadence is a design decision.** The right reporting frequency depends on matter phase, risk level, client preference, and decision density — not on what the last matter did. This skill prompts those questions at setup rather than defaulting to a standard template.

---

## Source references

- Linton, *Legal Project Management* (2014) — Chapter 8 (Stakeholder and Client Communication): power/interest grid, stakeholder matrix, communication plan structure, RASIC roles.
- CLOC, *LPM for Legal Teams* (2017) — Stage 2/3: communication cadence, reporting metrics, outside counsel billing guidelines.
- Belfast LPM Large Projects presentation (Oct 2019) — project hierarchy, client reporting, internal reporting, HQ vs regions case study.
