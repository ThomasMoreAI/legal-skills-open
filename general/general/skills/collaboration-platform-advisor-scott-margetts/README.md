# collaboration-platform-advisor

**Plugin:** LPM Core Plugin (Skill 13 of 14)
**Part of:** [LPM Skills for Claude](https://github.com/legalopsconsulting/lpm-skills)

---

## What this skill does

Designs and governs legal matter collaboration platforms — their structure, workflows, dashboards, data quality, and adoption. Works with M365 (SharePoint, Teams, Power Automate) as the reference implementation and produces outputs in platform-agnostic terms so an LPM can brief IT or build simple automations directly.

The skill encodes methodology, not tool configuration. Law firm platform failures are almost never technical — they are design and adoption failures. A platform too complex for a partner to navigate in 90 seconds will not be used. A dashboard requiring manual data entry will have stale data. This skill is built to prevent those failures.

## Usage notes (v1)

**Mode 2 — automation briefing:** Works best when you name the specific workflow you want to automate. Example: *"Brief me on automating the weekly LC acknowledgment chase"* produces a populated automation brief. Generic prompts like *"what can I automate?"* may produce general AI assistant advice rather than the M365-scoped brief format. If this happens, restate the request naming the specific workflow and platform.

**Mode 3 — dashboard design:** Produces a dashboard specification document — not a built dashboard, HTML artifact, or interactive tool. The specification is what you hand to IT or use to configure SharePoint. If you need something interactive built, use the specification as the brief for that build.

---



| Mode | When to use |
|---|---|
| **Mode 1 — Site setup and architecture** | New matter or programme — design the site structure before building it |
| **Mode 2 — Workflow identification and automation briefing** | Identify which workflows to automate and produce IT-briefable descriptions |
| **Mode 3 — Dashboard and reporting design** | Design dashboards by audience — partner, client, LPM |
| **Mode 4 — Data quality and adoption** | Platform data has degraded or nobody is using the platform |

---

## What it doesn't do

- **DMS configuration** — iManage, NetDocuments, and similar document management systems require IT involvement and firm-specific expertise. This skill designs the collaboration layer, not the DMS.
- **Power Automate development** — Mode 2 produces automation briefs in plain English for IT developers. It does not write Power Automate flows.
- **Client-facing configuration** — any element visible to the client requires partner review before activation. This skill designs and proposes; the partner approves.

---

## Key design principles encoded

**Over-engineering kills adoption.** Every element of a matter site should survive: "If this doesn't exist, what specifically goes wrong?" If the answer is "nothing much," cut it.

**Data entry must be a side effect, not a separate task.** Any platform requiring a team member to navigate to a site and enter data will have stale data within two weeks.

**Design for the partner first.** The partner dashboard shows 5 metrics. Everyone else gets more. Design for the reader with the least time and lowest platform tolerance.

**The platform either becomes the system of record or it fails.** Parallel operation (email plus platform) produces two sources of truth and neither reliable.

**Adoption is a design failure, not a training failure.** If the platform is embedded in existing workflows, training is a 15-minute orientation.

---

## Outputs

All outputs produced as `.docx` files.

| Mode | Primary output |
|---|---|
| Mode 1 | Site architecture document — document library structure, list schemas, channel design, permissions |
| Mode 2 | Automation brief per workflow — trigger, condition, action, data source, owner |
| Mode 3 | Dashboard specification per audience — views, data sources, refresh cadence, access |
| Mode 4 | Adoption intervention plan — root cause, named actions, owner, metric |

---

## Skills this one works with

| Skill | Relationship |
|---|---|
| matter-intake-scoping | Scope and stakeholder map → site architecture inputs |
| matter-plan-builder | Task list structure → matter plan SharePoint List schema |
| stakeholder-comms-planner | Stakeholder register → dashboard audience and permissions |
| local-counsel-manager | LC tracker structure → LC tracker list schema and automation |
| status-report-drafter | Platform data and list exports → structured status report inputs |
| timeline-generator | Matter plan list CSV → Gantt and critical path inputs |
| continuous-improvement-engine | Platform adoption failures → Mode 1 lesson capture triggers |

---

## License

Apache 2.0. See [LICENSE](../../LICENSE).
