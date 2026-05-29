---
name: matter-plan-builder-scott-margetts
title: Matter Plan Builder
description: 'Convert agreed scope into a structured matter plan — phases, workstreams, milestones, dependencies, owner assignments, and matter setup decisions. Use when planning a new matter, running a kickoff, building a workstream plan, structuring phases, setting up task codes, or producing a plan to drive status reporting. Trigger on: ''build a plan'', ''matter plan'', ''project plan'', ''what are the phases'', ''workstream plan'', ''how do we sequence this'', ''who owns what'', ''task codes'', ''matter setup'', ''workstream plan'', ''matter plan'', ''rolling wave'', ''plan the next phase'', ''what comes first'', ''kickoff agenda''.'
author: Scott Margetts
author_url: https://lawve.ai/en/skills/matter-plan-builder-scott-margetts
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Matter Plan Builder

## Purpose

Convert agreed scope into a structured matter plan the team can execute against. A plan that exists only in the partner's head is not a plan — it is an intention. The function of this skill is to make the plan explicit, assign ownership, sequence the work, and produce an output that every other LPM discipline can reference.

This skill takes the output of matter-intake-scoping (or an equivalent scope description) and produces the planning layer. scope-change-controller manages that plan as the baseline throughout the matter. status-report-drafter reports progress against it. timeline-generator adds dependency logic and critical path visualisation.

**The matter setup decision is part of this skill.** How the matter is configured in the billing system — single matter vs phased structure, task codes, matter numbers — directly affects whether the data collected is useful for reporting, billing, and future scoping. Getting it wrong at setup costs the project throughout its lifetime. This is not a billing admin task. It is a strategic planning decision that must be made before time starts being recorded.

---

## Operating Modes

### Mode 1 — Full plan (most matters)
Scope to complete plan. Matter plan (phases, workstreams, milestones, key dependencies, owners) plus workstream plans for each workstream. Produces matter setup recommendations alongside the plan. Default mode for matters of moderate complexity with a defined team.

**Mode 1 produces a workstream plan for every workstream without exception.** If there are five workstreams, five workstream plans are produced. Do not produce the first workstream and note that others "follow the same format" — produce them all. Mode 2 is the correct mode when a matter plan without workstream detail is needed. If a user invokes Mode 1 on a matter with many workstreams and full workstream plans would be disproportionate, ask whether Mode 2 is more appropriate before proceeding.

### Mode 2 — Matter plan only (large programmes)
Phases, workstreams, high-level milestones, and owners only. Workstream plans are the responsibility of workstream leads — this skill produces the matter plan and the template workstream leads should follow. Produces the dependency-flagged plan for timeline-generator.

### Mode 3 — Workstream plan (workstream detail)
A single workstream or jurisdiction plan built in detail. Input: the matter plan (or equivalent) plus the workstream scope. Output: task-level plan with sequencing, dependencies, durations, and owners. Designed for the workstream lead to own and maintain.

### Mode 4 — Rolling wave
For matters where full scope is not yet defined. Plan the current phase in full detail. Produce a stub plan for subsequent phases — milestones only, no task detail. Flag the trigger points at which the next phase needs to be planned in detail. The stub is a placeholder, not a commitment — mark it as such.

### Mode 5 — Plan update from correspondence
The most frequently needed mode in practice. Accepts emails, call notes, or meeting notes and proposes updates to the existing plan — status changes, progress notes, due date revisions, new blockers, completed tasks. The LPM reviews and confirms; they do not create the updates manually.

This mode exists because the alternative — asking lawyers to update the plan directly — does not work. Lawyers do not update plans. The information exists in their emails and in their heads. The LPM's job is to extract it from those sources without creating a manual data-entry burden that takes longer than the matter itself.

Input: existing plan (uploaded as file or pasted) + correspondence since last update. Output: proposed plan changes, presented as a confirmation list. The LPM confirms, dismisses, or edits each proposed change. The updated plan is produced as a new version (.docx and structured export) on confirmation.

In connected mode, this mode can be triggered automatically — Claude monitors matter correspondence and surfaces proposed updates without waiting for the LPM to initiate.

---

## Step-by-Step Process

### Step 1: Confirm the scope baseline
Read all provided materials. Identify whether a structured scope summary exists (from matter-intake-scoping Mode 2/3) or whether scope must be reconstructed from the input. If reconstructing: identify matter type, client objectives, key deliverables, jurisdictions involved, and known constraints. Flag scope gaps before proceeding — a plan built on incomplete scope will need rebuilding.

If scope is thin, surface the gaps: what do we need to know before we can build this plan? List them explicitly. Do not produce a plan that buries assumptions without flagging them.

**Before producing any plan output, confirm owner names.** A plan distributed at kickoff with "[SA name]" placeholders throughout is not a usable plan — it is a draft. If owner names have not been provided in the input, stop and ask before producing any output: "To assign ownership correctly, I need the names of the leads for each workstream. Please confirm: [list workstreams identified from scope]. If names are not yet confirmed, say so and I will produce the plan with [TBC — confirm before distributing] placeholders and flag it as DRAFT."

Do not proceed to plan output until the user has responded — either with names, or with an explicit instruction to proceed with TBC placeholders. Do not silently infer that placeholders are acceptable because the user said they don't know who's doing what. The user must make that call explicitly.

**Consuming matter-intake-scoping Mode 2 output:**
When a Mode 2 scope summary from matter-intake-scoping is provided, map its fields directly to plan inputs — do not treat it as generic prose to be reinterpreted:

| matter-intake-scoping field | Maps to plan input |
|---|---|
| Inclusions | Workstream scope and deliverables — what each workstream must produce |
| Exclusions | Explicit out-of-scope items — flag in plan notes to prevent drift |
| Assumptions | RAID log A-entries on matter opening; also populate dependency register where assumptions are information dependencies |
| Constraints | Phase duration limits, resource constraints, fixed external dates |
| Milestones | Matter plan milestone list starting point — validate against phase pattern before finalising |
| Fee basis | Matter setup recommendations — phased vs single matter, whether fee structure requires phase-level tracking |
| LPM involvement definition | Communication schedule and plan maintenance responsibilities |

If any of these fields are absent from the scope summary, flag the gap before producing the plan.

### Step 2: Identify phases and workstreams
Break the matter into phases (sequential stages with defined entry/exit criteria) and workstreams (parallel lines of work that run across phases). These are different dimensions of the same plan.

**Phases** are time-based and sequential. Movement between phases should be a deliberate decision — a phase gate — not just elapsed time. Phase gates are moments where the partner (and sometimes the client) confirms: the prior phase work is complete to the required standard, the conditions for the next phase are met, and the team is authorised to proceed. Common phase patterns by matter type are in the domain knowledge section below.

**Workstreams** are function-based and often parallel: Corporate, Tax, Employment, Real Estate, Regulatory, Finance. On multi-jurisdiction matters, workstreams may be replicated per jurisdiction (Germany Corporate, Netherlands Corporate) or structured as a single cross-border workstream with jurisdiction leads beneath it. The right structure depends on whether jurisdictions are executing the same work in parallel or different work that converges.

The matter plan is the intersection: which workstreams are active in which phases, what each produces, and who owns it.

### Step 3: Identify milestones and dependencies
Milestones are binary — done or not done. Not "75% complete." Not "progressing well." A milestone marks the completion of something significant: regulatory filing submitted, DD report issued, transaction documents agreed, execution complete. Every milestone must have a named owner and a target date.

Flag dependencies explicitly. Three types matter in legal work:

**Predecessor dependencies** — X cannot start until Y is complete. These are the critical path candidates. Tag them by type for timeline-generator: FS (Finish-to-Start), FF (Finish-to-Finish), SS (Start-to-Start), SF (Start-to-Finish). The most common in legal work is FS — one thing must finish before the next can start. FF and SS arise most often in multi-jurisdiction matters where parallel workstreams must reach a milestone together before converging.

**Shared resource dependencies** — X and Y both require the same person at the same time. Surface these at planning stage. Resource-planner handles the detailed analysis; this skill flags the conflict.

**Information dependencies** — X cannot proceed without confirmation from an external party: a regulatory body, the counterparty, a tax authority, a client internal team. These are the most dangerous because their duration is outside the firm's control. For every information dependency: who is providing it, what is the expected lead time, and what is the downstream impact if delayed by two weeks / four weeks.

### Step 4: Assign owners
Every workstream needs a single named owner. Not "the London team" — a person. Not "local counsel" — a named firm and, where known, a named individual. Ownership without accountability is a workstream that will drift.

Below the workstream owner: identify whether each workstream has sufficient resource at the right level. Gearing matters — a workstream staffed only with senior associates will be expensive and slow on routine tasks; a workstream with no senior resource will escalate everything. Flag gearing concerns; resource-planner handles the detailed analysis.

### Step 5: Build matter setup recommendations
Document the matter configuration before the plan is finalised. This is easiest to get right at setup and hardest to fix once the matter is running.

**Single matter or phased structure?**
A single matter with one code simplifies billing for straightforward work. Phased matters allow phase-level financial tracking and phase-gate cost controls — essential where client approval is required before proceeding, or where the fee arrangement changes between phases.

**Task code design:**
Task codes determine what data you can extract. Design them to match the reporting the matter will require:
- If status reports have a row per workstream, each workstream needs a code
- If the budget was built by jurisdiction, each jurisdiction needs a code
- If there will be a phase-gate cost discussion with the client, each phase needs a code
- If there will be a local counsel cost comparison at close, each external firm needs a code

The most common failure: generic codes (e.g. "Corporate," "Tax") when the matter has identifiable sub-workstreams. The data becomes too aggregated to be useful for anything except the total figure.

**Billing instruction:**
Once task codes are agreed, produce a one-paragraph billing instruction specifying which code covers which work. Distribute at kickoff. Without it, each timekeeper guesses, and data quality degrades within the first billing cycle.

### Step 6: Produce the plan
Produce outputs in sequence: matter plan first, workstream plans per workstream, then matter setup recommendations. Each is a standalone output for the relevant audience.

**Matter plan format:**
- Phase summary: phase name, entry criteria, exit criteria, duration estimate, owner, key milestones
- Workstream summary: workstream, owner, active phases, key deliverables, dependencies flagged by type
- Dependency register: dependency, type (predecessor / resource / information), dependent task, blocking task, owner, impact if delayed

**Workstream plan format (per workstream):**

Task table — required columns in this order. Do not omit any column, even if a field is empty:

| Unique ID | Task ID | Task Summary | Task Description | Owner | Due Date | Duration (days) | Predecessor(s) | Dep Type | Milestone | Status | Progress Notes | Task Code |

- **Unique ID:** [MatterCode]-T-[sequential number, matter-scoped, never reused] — e.g. 88234-T-001, 88234-T-002. Continues across all workstreams — Corporate tasks might be 88234-T-001 to 88234-T-012, Employment 88234-T-013 to 88234-T-019. Do not restart numbering per workstream.
- **Task ID:** Human-readable within-plan reference (e.g. WS1-T01) — used in the document for readability and predecessor references.
- **Due Date:** Specific calendar date. Not a phase reference. Not "Week 3." A date.
- **Predecessor(s):** Task ID (human-readable) or "None" — never leave blank.
- **Progress Notes:** Leave blank if not started — but the column must be present.

Milestone list: Unique ID | Milestone ID | Milestone Description | Owner | Target Date | Predecessor Task(s) | Phase Gate? | RAG

Open items: assumptions, outstanding information requests, external confirmations needed.

**Kickoff agenda (produce on request):**
Draft from the matter plan: scope confirmation, workstream introductions, milestone walk-through, dependency flags, matter setup briefing (task codes and billing instruction), escalation path, next review date.

---

## Domain Knowledge — Matter Type Phase Patterns

Starting points, not prescriptions. The value is in documenting how this matter's phases differ from the standard pattern and why.

**Corporate transaction (M&A, carve-out, disposal):**
Preparation → Due Diligence → Negotiation → Signing → Regulatory / Conditions Precedent → Completion → Post-Completion

Phase gates: DD report sign-off before negotiation commences; board/client approval before signing; CP satisfaction confirmation before completion is scheduled. Post-completion actions (filings, registrations, notifications) are frequently under-planned — they have no revenue attached and get de-prioritised. Plan them explicitly.

**Corporate reorganisation (multi-jurisdiction):**
Scoping / Structure Design → Sequencing → Jurisdiction-Level Execution → Completion / Registration Confirmations → Post-Completion (strike-offs, deregistrations, final filings)

Key dependency pattern: jurisdictions that must complete before others can begin are the structural critical path. This is not a scheduling preference — it is a legal sequencing requirement. Identify the dependency chain early and pass it to timeline-generator as hard FS dependencies. The reorg-step-plan-builder skill in the LPM for M&A plugin provides detailed methodology for this matter type.

Phase gates: structure design sign-off before execution commences; prerequisite jurisdiction completions before dependent jurisdictions begin; final registration confirmations before post-completion actions start.

**Litigation / arbitration:**
Pleadings → Disclosure / Discovery → Evidence → Hearing → Post-Hearing / Enforcement

Information dependency pattern: third-party disclosure, expert availability, and hearing dates are all outside the firm's control. Plan what is within the firm's control in detail; flag the external dependencies explicitly with duration ranges.

Phase gates: strategy confirmation before pleadings filed; disclosure strategy agreed before document review commences; evidence strategy confirmed before witness statements prepared.

**Regulatory (licensing, authorisation):**
Assessment → Application Preparation → Submission → Regulatory Review Period → Determination → Implementation

The regulatory review period is an information dependency of unknown duration. It blocks some downstream activities entirely and others only partially. At planning stage: identify what can run in parallel during review, what is blocked until determination, and the minimum / expected / maximum duration range.

**Finance / capital markets:**
Mandate / Structuring → Documentation → Due Diligence → Marketing / Roadshow → Signing → Settlement / Closing

Phase gates: documentation agreed before marketing commences; DD confirmed before final terms are set. Timeline compression is the dominant pressure in capital markets work — the plan must be built to accommodate acceleration without losing track of what has been skipped or deferred.

---

## Domain Knowledge — Common Planning Failures

**The plan is built but never distributed.** The partner approves it, the LPM files it, the team never sees it. A plan nobody knows about has no effect on behaviour. Distribute at kickoff. Reference at every status call. Update when scope changes.

**Milestones are confused with activities.** "Draft SPA" is an activity. "SPA agreed and execution-ready" is a milestone. Status reports against activities produce noise; against milestones, signal. Every workstream should have at least one milestone per reporting period. If it doesn't, the workstream has no meaningful status to report.

**Dependencies are identified but not managed.** A dependency register that isn't reviewed is documentation, not management. Review at every status call: which predecessors are at risk, which information requests are outstanding, which external confirmations haven't arrived. The predecessor that slips without anyone noticing is the one that shifts the critical path.

**Rolling wave planning is treated as failure.** It isn't. On complex matters, detailed planning beyond the current phase is often premature. The rolling wave approach is disciplined: plan the current phase in detail, stub the next, set a trigger milestone for when the next phase gets planned. The stub is not a failure — it is an acknowledgment that premature planning is as dangerous as no planning.

**Matter setup is delegated to billing admin.** The configuration decision must be made by the LPM or partner before the matter opens. Once time is being recorded, reconfiguring codes strands historical data. The billing team executes the configuration. The LPM designs it.

**Workstream owners are organisations, not people.** "Local counsel — Germany" is not an owner. When a workstream slips and escalation is needed, a name is needed.

**The plan isn't updated when scope changes.** scope-change-controller manages scope changes. But a change that doesn't flow through to the plan produces a plan that no longer reflects what the team is doing. When scope-change-controller logs an approved change, assess whether the plan needs updating — and update it.

**Workstream plans are submitted but never read against each other.** On large programmes, the central LPM receives workstream workstream plans but never reviews them cross-workstream. The critical path crosses workstream boundaries; no individual workstream lead sees it. The central LPM holds the cross-workstream view — identifying where workstream milestones create programme-level dependencies is the primary planning value-add.

**Plan maintenance falls entirely to the LPM.** This is the dominant failure mode in practice. Lawyers do not update task plans — not because they are negligent, but because updating a SharePoint List or Excel tracker is not how legal work gets communicated. Legal work gets communicated in email. The information required to keep the plan current exists in the correspondence; extracting it and entering it into a structured format is a manual translation task that the LPM performs for the entire matter. On a 12-month cross-border reorg with 40+ active workstreams, this is hundreds of hours of work that adds no analytical value — it is transcription.

The consequence is data degradation. Tasks show "In progress" for weeks because nobody updated them to "Complete." Due dates drift because the LPM didn't catch the date change buried in a jurisdiction email. Progress notes become stale. The plan stops reflecting reality. Status reports built from the plan become unreliable. The partner loses confidence in the reporting. The investment in planning is retrospectively judged as wasted effort.

The solution is not to ask lawyers to update the plan more diligently. It is to remove the manual extraction step entirely. Mode 5 exists for this reason: Claude reads the correspondence, proposes the updates, and the LPM confirms. The LPM's role shifts from data entry to judgment — which is where their value actually lies. In connected mode, this operates continuously: the plan is always one confirmation away from being current.

---

## Standard Plan Fields

These are the minimum required fields for each plan component. A plan entry that omits any of these fields cannot be used to drive execution, status reporting, or escalation — it is a list, not a plan.

### Workstream header (one per workstream)
| Field | Purpose |
|---|---|
| Unique ID | Stable matter-scoped identifier assigned on creation and never changed — e.g. [MatterCode]-WS-001. Used by other skills to reference this workstream in RAID entries, scope change notices, and status reports |
| Workstream name | Consistent label used across all plan documents and status reports |
| Owner (named individual) | Accountable for workstream delivery — one person, not a team or firm |
| Phase(s) active | Which phases this workstream operates in |
| Task code | The billing code all time in this workstream is recorded against |
| Escalation contact | Who the owner escalates to if a workstream issue cannot be resolved at owner level |

### Task entry (one per task)
| Field | Purpose |
|---|---|
| Unique ID | Stable matter-scoped identifier assigned on creation and never changed — e.g. [MatterCode]-T-001. Used by other skills to reference this task in RAID entries, scope change notices, and status updates. Never reassigned even if the task is moved, renamed, or restructured. |
| Task ID | Human-readable reference code (e.g. WS1-T01) for use within the plan document |
| Task summary | Single-line label — verb + noun ("Prepare tax opinion", "Submit regulatory filing") |
| Task description | Multi-line detail — what is being done, what the output is, any constraints or instructions |
| Workstream | Which workstream this task belongs to — must match the workstream header label exactly |
| Phase | Which phase this task falls in — must match the phase name in the matter plan |
| Milestone | Which milestone this task contributes to — links task-level execution to milestone-level reporting |
| Owner | Named individual responsible for completion |
| Due date | Target completion date — specific date, not a phase reference |
| Duration estimate | Working days — not calendar days unless explicitly stated. Even rough estimates surface planning gaps. |
| Predecessor(s) | Task ID(s) that must complete before this task can start — required for critical path calculation |
| Dependency type | FS / FF / SS / SF — for timeline-generator |
| Status | Not started / In progress / Complete / Blocked |
| Progress notes | Free text — current position, blockers, next action. Updated at each status review. |
| Task code | Billing code for time recorded against this task |

### Milestone entry (one per milestone)
| Field | Purpose |
|---|---|
| Unique ID | Stable matter-scoped identifier assigned on creation and never changed — e.g. [MatterCode]-M-001. Used by other skills to reference this milestone in timeline-generator, status reports, and phase gate records |
| Milestone ID | Human-readable reference code (e.g. WS1-M01) for use within the plan document |
| Milestone description | Binary statement of completion — "X submitted", "Y agreed", "Z registered" |
| Owner | Named individual responsible for confirming completion |
| Target date | Specific date, not a phase reference |
| Predecessor task(s) | Task IDs that must complete for this milestone to be reached |
| RAG status | Green / Amber / Red — assessed at each status review |
| Phase gate? | Yes / No — whether completion of this milestone triggers a phase gate decision |

### Dependency entry (one per flagged dependency)
| Field | Purpose |
|---|---|
| Dependency ID | Short reference code |
| Type | Predecessor / Resource / Information |
| Blocking item | What must complete or be received |
| Dependent item | What cannot proceed until the blocking item resolves |
| Owner of blocking item | Who is responsible for the blocking item (may be external) |
| Expected resolution date | Target date for the blocking item to resolve |
| Impact if delayed 2 weeks | Programme-level impact — which milestones move, by how much |
| Impact if delayed 4 weeks | Programme-level impact at greater delay |

A dependency register with no "impact if delayed" column is not a risk management tool. It is a list of things that might go wrong with no assessment of how wrong.

---

## Communication Rhythm

The plan must include the meeting and reporting cadence — not as a stakeholder-comms-planner output, but as plan infrastructure. A plan with no review cadence baked in goes stale immediately and is never formally maintained.

**Standard cadence elements to include in every plan:**

**Status call (internal):** Frequency (weekly / fortnightly), attendees (workstream owners minimum), purpose (milestone progress against plan, dependency review, escalation triage). The plan is reviewed at this call — not just discussed. If the plan is not on screen, it is not being managed.

**Client reporting:** Frequency (weekly / monthly / milestone-triggered), format (status report from status-report-drafter), owner of report preparation.

**Phase gate review:** Scheduled at the start of each phase for the end of the current phase. Owner: partner and LPM. Purpose: confirm phase completion criteria are met, authorise progression. Not a status call — a decision point.

**Plan review:** Frequency (monthly on most matters, fortnightly on fast-moving ones). Purpose: assess whether the plan still reflects the scope, flag tasks that have drifted from the plan, update estimates. Owner: LPM. The output of a plan review is either a confirmed plan or an updated plan — not a verbal reassurance that "things are on track."

**Billing review:** Frequency (monthly, aligned with billing cycle). Purpose: review WIP against task codes, identify time recorded to wrong codes, confirm task code allocations for upcoming work. Owner: LPM with billing-cycle-manager.

Add a summary communication schedule to the matter plan document: meeting type, frequency, owner, linked plan output.

---

## Output Format

All outputs produced as .docx unless the user explicitly requests otherwise. These are matter records — they belong in the matter folder.

Every output includes the identifier block:
```
Client: [Name]          Client number: [Number]
Matter: [Name]          Matter number: [Number]
Plan version: [v1.0]    Prepared by: [LPM name]    Date: [Date]
```

Flag rolling wave stubs clearly: **[ROLLING WAVE — [phase name] to be planned in detail at: [trigger milestone]]**

**Structured data export:**
Every plan output is accompanied by a structured data export (CSV or JSON) containing all task and milestone entries with their full field set. This is the input format for a SharePoint List or equivalent system of record. The .docx is for human distribution and reference. The structured export is for machine-readable tracking — it is what makes Mode 5 updates, connected-mode monitoring, and cross-skill data exchange possible.

A plan that exists only as a Word document cannot be updated by Claude. A plan that exists as a SharePoint List can. The standard fields defined in this skill are the SharePoint List schema. Firms deploying this skill should configure the List at matter setup using the structured export from the initial plan build.

Plan versioning: every output is stamped with a version number (v1.0, v1.1, etc.) and date. The prior version is retained. Never overwrite a plan version — the version history is the audit trail of how the matter evolved.

**Every plan output must include all of the following. Do not produce a plan without these elements:**

1. Identifier block (Client, Matter, version, LPM, date)
2. Matter plan (phases, workstream summary, milestone register, dependency register)
3. Communication schedule
4. Matter setup recommendations (task codes, billing instruction)
5. Workstream plan for every workstream — all required columns present (see Step 6)
6. RAID log opening entries
7. Cross-skill handoff prompts (see Cross-Skill Handoffs section) — produce these at the end of every plan output as a named section: "Next Steps — Cross-Skill Handoffs"
8. Structured data export (CSV) — task and milestone entries with all fields. Produce inline as a labelled section if a file cannot be attached.

Items 7 and 8 are not optional extras. A plan with no handoff prompts leaves the LPM to remember which other skills need to be triggered. A plan with no structured export cannot be updated by Claude.

---

## Cross-Skill Handoffs

- **From matter-intake-scoping:** Scope summary (Mode 2/3 output) is the primary input. Scope is set; this skill operationalises it. Consume using the field mapping in Step 1.
- **From scope-change-controller:** When an approved scope change is passed in, treat it as a Mode 5 trigger. Read the change notice, identify which plan components are affected (tasks, milestones, owners, dependencies, phases), propose updates as a confirmation list, and produce an updated plan version on confirmation. A scope change that does not flow through to the plan produces drift — the plan stops reflecting what the team is actually doing. Version the output: if the current plan is v1.2, the post-change plan is v1.3.
- **To timeline-generator:** Dependency-flagged task list and milestone list with dependency type tags (FS/FF/SS/SF). Pass with: "Build a dependency network and critical path from this plan."
- **To scope-change-controller:** Completed plan is the scope baseline. Pass with: "Set up scope baseline — here is the agreed matter plan."
- **To status-report-drafter:** Milestone list and workstream structure are the reporting baseline. status-report-drafter reports progress against milestones, not task completion percentages.
- **To stakeholder-comms-planner:** Workstream owners, phase cadence, and milestone schedule inform communication rhythm design.
- **To resource-planner:** Workstream resource requirements and gearing concerns flagged in the plan.
- **To billing-cycle-manager:** Matter setup recommendations — task codes, phase structure, billing instruction.
- **To risk-and-issues-manager:** Information dependencies and plan assumptions are inputs for the RAID log. Pass as A-entries (Assumptions) and R-entries (Risks) on matter opening.

---

**Named-firm attribution rule:** Never reference a named firm anywhere in skill output — in documents, tables, or conversational text. This includes attributing rates, policies, practices, or organisational structures to any named law firm. The skill does not know any firm's actual structure, rates, or policies. Use "confirm with Pricing", "confirm with Finance", or "firm policy — confirm before applying." The rule applies to everything this skill produces, not just formal documents.

---

## M365 Connected Mode (Optional)

**Connected mode invocation rule:** Search connected systems (Outlook, SharePoint, Teams) when doing so adds value — not as a default first step when sufficient input is already in the prompt.

- **Sufficient input already provided:** User has pasted emails, documents, or data with full context. Engage with what is there. Do not search first — it adds friction without adding information.
- **Input is incomplete or proactive surfacing is warranted:** User references something that should be retrieved ("there's an invoice in Outlook", "it's end of month"), or connected mode is running in background/scheduled mode. Search proactively — this is the inverted invocation model and is the highest-value connected mode behaviour.

The distinction is whether the user has already provided what is needed. If yes, work with it. If no, or if proactive surfacing serves the LPM, search.

When the M365 MCP connector is enabled (Claude Team/Enterprise), this skill can:
- Search SharePoint for prior matter plans of the same type to use as planning precedent
- Pull scope summaries and engagement letters from SharePoint to inform the session
- Search Outlook for kickoff correspondence to identify planning decisions already made
- Create a kickoff calendar invite in Outlook with agenda drafted from the matter plan
- Push approved tasks and milestones to Planner or Teams for live tracking post-kickoff

Without the connector: provide scope summary, prior plans, and relevant correspondence by pasting text or uploading files directly.
