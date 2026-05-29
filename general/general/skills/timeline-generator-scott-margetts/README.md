# timeline-generator

**Part of the LPM Core Plugin for Claude**

Build a dependency network and critical path from a matter plan. Produce an interactive visual timeline. Model what happens to programme completion when things take longer than planned.

---

## What it does

Takes the task list from your matter plan — with dependency types (FS/FF/SS) and duration estimates — and calculates which tasks are on the critical path, which have float, and what happens to programme completion when something slips.

Four modes:

**Mode 1 — Baseline build.** At matter setup, build the dependency network, identify the critical path and near-critical tasks, produce an interactive HTML Gantt. Forward or back scheduling — if the client has a fixed completion deadline, the skill works backwards through the network to derive the required start date for each task, and immediately flags if the programme is already in deficit.

**Mode 2 — What-if analysis.** Mid-matter: model a proposed delay and get the full cascade impact. Which tasks move, which milestones slip, does the critical path change, what does the client need to know? Produces draft client notification and affected local counsel communications. Offers recovery options (crash, fast-track, defer) for the LPM and partner to consider.

**Mode 3 — Baseline update.** Confirm a change, version the baseline (minor increment for schedule adjustments, major for structural changes), produce a comparison table of original vs revised dates for affected tasks only. Triggers cross-skill handoffs.

**Mode 4 — Workstream or jurisdiction view.** Extract a filtered timeline for a single workstream or jurisdiction — for local counsel communications, partner workstream updates, or any situation where the full programme network is too much. Float values are inherited from the full network, not recalculated on the subset. Upstream constraints and downstream milestones are shown with distinct visual treatment so the recipient understands their gating without seeing the full programme.

---

## Dependency types

**FF (Finish-to-Finish) — the dominant pattern in parallel execution work.** Two workstreams run simultaneously; the constraint controls when they finish relative to each other. Example: dividend resolution completes Monday; share transfer must complete by Thursday. Both run in parallel from the start — the FF+3d lag controls when the transfer closes. Shown in the Gantt as a bracket connecting the finish points of the two bars, with the lag value labelled.

**FS (Finish-to-Start) — hard legal sequencing requirements.** One task cannot start until another is fully complete. Germany entity registration must complete before Netherlands dissolution can begin — there is no parallel execution possible because the legal validity of the downstream step depends on the upstream step being complete. Also used with lag for regulatory windows: filing submitted → [30 WD lag] → determination received → successor starts.

**SS (Start-to-Start).** Two workstreams must launch in coordinated sequence but can then proceed independently.

---

## When to use it

- Building the initial matter timeline from a kickoff plan
- Client has a fixed completion date — is it achievable, and what date do we need to start?
- German counsel says the regulatory window is 12 weeks, not 8 — what moves?
- A near-critical task has slipped — has it taken over the critical path?
- Confirming a delay and updating the programme baseline
- Local counsel asks for their timeline — produce a Germany-only or Employment-only view

---

## Inputs

**Minimum viable input:** Task ID, Duration (working days), Predecessor(s), Dependency type (FS/FF/SS), and a start date or fixed end date.

**Preferred input:** The structured CSV export from matter-plan-builder — this provides the full 13-field task schema with all dependency data pre-formatted.

**For Mode 2:** The existing baseline (as a file or pasted) plus the proposed change in plain language. Paste the email — the skill identifies the affected task and models the cascade.

**For Mode 4:** The full baseline plus the workstream or jurisdiction name to filter on.

---

## Visual output

The primary output is an interactive HTML canvas Gantt rendered inline in Claude — not a text table, not Mermaid. It produces better output than PowerPoint or Excel for timeline visualisation and can be screenshotted directly for status reports or client decks.

The Gantt includes:
- Red bars for critical path tasks, green for non-critical
- Float shown as a faded bar extension with the value in days labelled
- FF dependencies shown as a bracket between finish points with the lag labelled — not an arrow
- FS dependencies as directional arrows
- Milestone diamonds at programme completion and phase gates
- What-if slider for real-time cascade modelling where a regulatory window sits on the critical path
- In Mode 4: grey bars for upstream constraints, distinct milestone markers for downstream programme gates

---

## Key behaviours

**Float is inherited, not recalculated.** In workstream views (Mode 4), float values always come from the full network calculation. A task that is critical in the full programme is critical in a filtered view — the filter does not create float that doesn't exist.

**Back-scheduling flag.** When a fixed completion date is provided, the skill flags immediately if the required start date is in the past — the programme is in deficit before it begins.

**Regulatory lag — three scenarios.** When a lag represents an external determination window, the skill confirms whether it is a hard minimum or an expected duration. For expected durations, it produces three scenarios: best case, expected, and +50% — the analysis needed to have the deadline risk conversation with the client before the window opens.

**Lag convention.** Lag counts forward from the working day after predecessor EF. FS lag 5 WD from EF Wednesday 7 May → successor ES = Wednesday 14 May.

**Critical path structure change.** When a what-if analysis shifts the critical path from one sequence to another, the cascade impact table shows CP status change per task — New critical / Remains critical / Now near-critical / Unchanged — so the LPM knows where to redirect monitoring attention, not just how much things have moved.

**Versioning.** Minor increment (v1.0 → v1.1) for schedule adjustments. Major increment (v1.0 → v2.0) for structural changes — new phases, workstreams added or removed.

---

## Cross-skill handoffs

**Consumes:**
- matter-plan-builder structured export (dependency-tagged task and milestone list) — handoff prompt: "Build a dependency network and critical path from this plan"
- risk-and-issues-manager RAID breach notifications — an assumption breach on an information dependency is a Mode 2 trigger

**Feeds:**
- status-report-drafter: revised milestone dates → updated reporting baseline
- scope-change-controller: if programme recovery requires scope changes → scope signal
- matter-plan-builder: if Mode 2 confirms plan structure changes → Mode 5 plan update trigger
- risk-and-issues-manager: confirmed delays logged as Issues; compressible lag assumptions logged as Risks
- stakeholder-comms-planner: revised milestone dates and Mode 2 draft communications

---

## M365 Connected Mode (Claude Team / Enterprise)

When the M365 connector is enabled:
- Pulls the matter plan directly from SharePoint — no upload needed
- Monitors Outlook for emails signalling timeline changes, surfacing them as Mode 2 triggers
- Updates milestone dates in SharePoint Lists or Planner when Mode 3 is confirmed
- Drafts client notifications in Outlook draft mode for partner review

---

## Part of the LPM Core Plugin

The LPM Core Plugin encodes the operational methodology that applies to any legal matter. Timeline-generator sits at the technical centre: every other skill either produces data that feeds this skill or consumes the timeline data it produces.

**Skills that feed this one:** matter-plan-builder, risk-and-issues-manager
**Skills that consume this one:** status-report-drafter, scope-change-controller, matter-plan-builder (Mode 5), stakeholder-comms-planner, risk-and-issues-manager

Full plugin: [github.com/legalopsconsulting/lpm-skills](https://github.com/legalopsconsulting/lpm-skills)

---

*LegalOps Consulting Limited. Apache 2.0.*
