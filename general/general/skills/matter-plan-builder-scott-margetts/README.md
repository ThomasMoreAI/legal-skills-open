# matter-plan-builder

Convert agreed scope into a structured matter plan the team can actually execute against. Phases, workstreams, milestones, dependencies, owner assignments, matter setup — plus the maintenance architecture that keeps the plan current throughout execution.

## What this skill does

A plan that exists only in the partner's head is not a plan. It is an intention. The function of this skill is to make the plan explicit: assign ownership, sequence the work, flag dependencies, and produce an output every other LPM discipline can reference.

The skill operates in five modes scaled to matter complexity and planning stage:

**Mode 1 — Full plan.** Scope to complete plan. Matter plan plus workstream plans for every workstream. Default for matters of moderate complexity with a defined team. Produces matter setup recommendations alongside the plan.

**Mode 2 — Matter plan only.** Phases, workstreams, milestones, and owners. Workstream plans are the responsibility of workstream leads — the skill produces the matter plan and the template they should follow. Designed for large multi-jurisdiction programmes where full workstream planning at the centre is impractical.

**Mode 3 — Workstream plan.** A single workstream or jurisdiction in task-level detail. For the workstream lead to own and maintain.

**Mode 4 — Rolling wave.** Plan the current phase in full detail; stub subsequent phases at milestones only. Used when full scope is not yet defined — common in regulatory matters, complex transactions where Phase 2 scope depends on a Phase 1 determination, and large programmes early in mobilisation.

**Mode 5 — Plan update from correspondence.** The most frequently needed mode in practice. Accepts emails, call notes, or meeting notes and proposes updates to the existing plan as a confirmation list. The LPM confirms, dismisses, or edits each item. The updated plan is produced as a new version on confirmation.

**Mode 5 exists because the alternative — asking lawyers to update the plan directly — does not work.** Lawyers do not update plans. The information exists in their emails and in their heads. The LPM's job is to extract it from those sources. Mode 5 removes the manual extraction step: Claude reads the correspondence, proposes the updates, and the LPM's role shifts from data entry to judgment.

## Relationship with other LPM Core skills

This skill sits in the middle of the LPM Core architecture. It consumes scope from matter-intake-scoping and produces the baseline everything downstream references:

**matter-intake-scoping** → scope summary feeds the plan directly. Mode 2 output fields map to plan inputs by design — inclusions to workstream scope, exclusions to OOS flags, constraints to phase duration limits, milestones to the matter plan milestone list.

**scope-change-controller** → the completed plan is the scope baseline scope-change-controller manages throughout the matter. Approved scope changes flow back as Mode 5 triggers, producing a versioned plan update.

**timeline-generator** → the dependency-flagged task list (with FS/FF/SS/SF tags) is the primary input to timeline-generator for critical path calculation and what-if analysis.

**status-report-drafter** → the milestone register is the reporting baseline. Progress is reported against milestones, not task completion percentages.

**risk-and-issues-manager** → information dependencies and plan assumptions are RAID log seed entries on matter opening.

## Inputs

- Scope summary from matter-intake-scoping (structured, field-mapped)
- Engagement letter, heads of terms, or equivalent scope description
- Team roster (or confirmation that names are TBC — the skill asks before proceeding)
- Prior plans for comparable matters (optional, used as planning precedent)
- In M365 connected mode: SharePoint documents, prior matter plans, Outlook kickoff correspondence

## Outputs

All outputs produced as .docx. Every plan is accompanied by a structured data export (CSV) for SharePoint List import — this is what makes Mode 5 updates and connected-mode monitoring possible.

- Matter plan (.docx): matter plan, workstream plans per workstream, matter setup recommendations, RAID log opening entries, communication schedule, cross-skill handoff prompts
- Structured data export (.csv): all task and milestone entries with full field set
- Plan version history: every update produces a new versioned file — v1.0, v1.1, etc. Prior versions are retained as the matter audit trail
- Workstream lead template (Mode 2): the format leads must follow for their workstream plans

## Standard task fields

Every task entry in every plan contains 13 fields:

Unique ID (matter-scoped, stable, never reassigned) | Task ID (human-readable, within-plan reference) | Task Summary | Task Description | Owner | Due Date | Duration (days) | Predecessor(s) | Dependency Type (FS/FF/SS/SF) | Milestone | Status | Progress Notes | Task Code

A plan entry that omits any of these fields cannot drive execution, status reporting, or escalation. It is a list, not a plan.

## The matter setup decision

Matter setup is part of this skill — not a billing admin task delegated after the plan is complete. How the matter is configured in the billing system (single matter vs phased structure, task code design, billing instruction) directly determines what data you can extract later. Getting it wrong at setup costs the project throughout its lifetime. This skill produces matter setup recommendations alongside the plan and distributes a billing instruction at kickoff.

## Structured data export and SharePoint List

Every plan output includes a CSV export with the full task and milestone field set. This is the SharePoint List schema — firms deploying this skill should configure the List at matter setup using the structured export from the initial plan build.

A plan that exists only as a Word document cannot be updated by Claude. A plan in a SharePoint List can. The structured export is what bridges them.

## Cross-skill handoffs

- **From matter-intake-scoping:** Mode 2/3 scope summary — consumed via field mapping table in Step 1
- **From scope-change-controller:** Approved scope changes trigger Mode 5; plan versioned on confirmation
- **To timeline-generator:** Dependency-flagged task list with FS/FF/SS/SF tags
- **To scope-change-controller:** Completed plan passed as scope baseline
- **To status-report-drafter:** Milestone register and workstream structure as reporting baseline
- **To risk-and-issues-manager:** Information dependencies and assumptions as RAID log seed entries
- **To billing-cycle-manager:** Task code structure and billing instruction

## M365 connected mode

When the M365 MCP connector is enabled (Claude Team/Enterprise), this skill can search SharePoint for prior matter plans of the same type, pull scope summaries and engagement letters, search Outlook for kickoff correspondence, create kickoff calendar invites from the matter plan, and push approved tasks and milestones to Planner or Teams for live tracking.

Without the connector: provide scope summaries, prior plans, and correspondence by pasting or uploading directly.

---

*LPM Core Plugin — Skill 2 of 14 | LegalOps Consulting Limited | Apache 2.0*
