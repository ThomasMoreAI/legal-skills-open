# daily-briefing

**Plugin:** LPM Core
**Repo:** Private (LPMHub)
**Licence:** Apache-2.0

## What this skill does

Produces a portfolio-level morning briefing for an LPM running two or more active matters. Reads email, call notes, and matter state across the portfolio and produces a triage surface structured around deliverables (what is due, when, to whom), issues (current problems requiring action), and risks (plausible future problems requiring monitoring). The output is a working document for the LPM's own consumption — not a status report, not for distribution.

The discipline the skill encodes is cross-matter ranking. An LPM running a portfolio does not read their matters sequentially. They rank across the book — an external deadline today on a Green matter beats a Red matter in steady state. RAG is a trailing indicator of matter health; daily urgency is a leading indicator of today's action requirement. The skill makes that ranking discipline explicit and reproducible.

The practical effect: deliverables are ranked across the portfolio by urgency and impact, not grouped by matter. Cross-matter patterns (partner load pressure, fee-structure exposure, scope expansion waves) are surfaced only because the skill is looking across the book. A stack of individual matter reports would never surface them.

## Modes

| Mode | Name | When to use |
|---|---|---|
| 1 | Portfolio briefing | Default. "Run my daily briefing" across 2+ matters. No specific timeframe. |
| 2 | Single-matter routing | User pastes single-matter input. Routes to `matter-drill-down`. Does not produce a briefing. |
| 3 | Monday sweep | "Monday sweep", "weekend catchup". Adds Weekend Developments and Week-Ahead Calendar Overlay. |
| 4 | Ad-hoc timeframe | "What's landed in the last 48 hours?" Bounds content to a specified window. |

## What it doesn't do

This skill surfaces signals that trigger other skills. It does not do their work.

| If you need this | Use this skill instead |
|---|---|
| Single-matter working view or handoff briefing | `matter-drill-down` |
| Status report for a partner or client audience | `status-report-drafter` |
| RAID log update or decision extraction | `risk-and-issues-manager` |
| Scope change assessment or OOS documentation | `scope-change-controller` |
| Budget variance analysis or forecast-to-complete | `budget-and-fee-manager` |
| Stakeholder communication plan | `stakeholder-comms-planner` |

## Inputs

- Portfolio roster — matter names, identifiers, lead partner, lead LPM, RAG, fee model, WIP. Required before producing any briefing. If not provided and cannot be inferred, the skill asks once.
- Correspondence across two or more matters — emails, call notes, meeting summaries. Pasted or retrieved via M365 connected mode.
- Source tags (`[FROM LC]`, `[INTERNAL]`, `[CLIENT]`) if applied by the user. Preserved in attribution.

## Outputs

All outputs produced as `.docx` files. These are LPM working documents — they belong in the briefing folder, not the chat window.

| Mode | Output |
|---|---|
| Mode 1 | Portfolio briefing: summary, deliverables ranked across matters (max 8), issues, risks, cross-matter patterns, partner attention items, matter mini-briefings (sized to weight), reading list (max 5), handoffs. |
| Mode 2 | No output. Routes to `matter-drill-down` with the exact routing message. |
| Mode 3 | Mode 1 template plus Weekend Developments and Week-Ahead Calendar Overlay sections. |
| Mode 4 | Mode 1 template bounded to the specified timeframe. |

## Usage notes

**Cross-matter ranking.** Deliverables are ranked across the portfolio, not grouped by matter. A Green matter with an external deadline today appears above a Red matter in steady state. This is the core discipline.

**Restraint on quiet matters.** A matter in steady state with nothing live gets 1–2 lines in the mini-briefing section and no appearance in Deliverables, Issues, or Risks. The skill does not pad quiet matters to normalise length. If a matter is silent in the input, its only permitted content is a one-line mini-briefing stating "no substantive update this period's inputs". Fabricating content for silent matters is a skill failure.

**Attribution.** When a named individual has produced substantive operational judgment — a fee-variance analysis, a scope-framing recommendation, a tactical observation — the briefing attributes it by name. Generic attribution to "the team" is the failure mode.

**Cross-matter patterns.** The skill actively checks for named patterns: partner load pressure, LPM load pressure, fee-structure exposure wave, scope expansion wave, shared-client overlap, regulatory-driven disruption. Each pattern is named as a dynamic, not just a list of items.

**Information gap flag.** When three or more matters on the portfolio roster are silent in the input, the Summary names this as a portfolio-level signal: the briefing is partial, not comprehensive.

## M365 connected mode

Connected mode enables the skill to query Outlook for matter folders, retrieve correspondence in the specified timeframe, and produce the briefing without user paste. Mode 3 supports scheduled invocation via the monday-sweep Routine. All modes operate fully on pasted input — connected mode is an efficiency enhancement, not a prerequisite.

## Skills this one works with

| Direction | Skill | Relationship |
|---|---|---|
| Routes to | `matter-drill-down` | Single-matter zoom-in from portfolio context |
| Triggers | `status-report-drafter` | Status report for distribution on a specific matter |
| Triggers | `scope-change-controller` | Scope signal requiring formal assessment |
| Triggers | `risk-and-issues-manager` | RAID update required |
| Triggers | `budget-and-fee-manager` | Budget variance analysis or forecast-to-complete |
| Triggers | `local-counsel-manager` | LC non-response or escalation |
| Triggers | `resource-planner` | Resource or capacity conflict |
| Triggers | `stakeholder-comms-planner` | Stakeholder comms plan update |

`daily-briefing` is the highest-level LPM skill. It consumes nothing from other skills; it surfaces triggers that invoke them.

## Design principles applied

This skill applies the [LPM Core Plugin design principles](../README.md), including:

- **Cross-matter ranking** — deliverables ranked across the portfolio by urgency and impact, not grouped by matter
- **Document output by default** — briefings are .docx working documents, produced on invocation without conditional offers
- **Restraint on empty state** — silent matters get one line; empty sections are stated plainly; no padding to normalise length
- **Attribution to named individuals** — substantive analysis attributed by name, not generalised to "the team"
- **Automate capture, surface for confirmation** — in connected mode, the skill retrieves and structures; the LPM confirms and acts
- **LPM vs attorney boundary** — surfaces items requiring attorney judgment but does not offer legal analysis

## Licence

Apache 2.0. See [LICENSE](../../LICENSE).
