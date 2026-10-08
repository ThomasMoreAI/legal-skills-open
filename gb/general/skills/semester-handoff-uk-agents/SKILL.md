---
name: semester-handoff-uk-agents
title: /legal-clinic-uk:semester-handoff
description: End-of-term UK clinic case handoff memos — the mirror of /legal-clinic-uk:ramp. Produces per-case transition memos and a cohort summary so the departing cohort hands work to the incoming cohort cleanly. Reads deadlines, client-comms, and case history. Use when the supervisor or departing students need to wrap up the term, build transition memos, or offboard a graduating/withdrawing student.
author: uk-agents
author_url: https://github.com/uk-agents/uk-legal-plugins/tree/main/legal-clinic-uk/skills/semester-handoff
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: general
language: en
---

# /legal-clinic-uk:semester-handoff

1. Load `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/CLAUDE.md` → clinic profile, term dates, supervision style.
2. Load `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/deadlines.yaml` and `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/client-comms/[case-id]/log.md` per case.
3. Use the workflow below.
4. Take active-case list as input (ask if clinic doesn't have a central list). Map outgoing → incoming owners.
5. Generate per-case handoff memo → `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/handoffs/[term]/[case_id].md`.
6. Generate cohort summary → `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/handoffs/[term]/_summary.md`.
7. Route per supervision model — formal queue / configurable flags / lighter-touch.

---

# Semester (Term) Handoff

## Purpose

Every term, UK law school clinics lose their entire workforce and rebuild. `/legal-clinic-uk:ramp` solves half the problem — it onboards the new cohort. This skill solves the other half: it offboards the departing cohort by producing handoff memos that capture what the next student needs to know about every active case.

Without this, case knowledge walks out the door with the student. The new student starts from the case file and intake summary, which is never enough. Two weeks are wasted re-learning the case. The client experiences the re-learning as a regression — calls go unanswered, questions already answered get asked again.

In a UK law school clinic context there is also a supervision gap risk: if a case transitions without the supervising solicitor or barrister being aware of the full picture, the supervision coverage for that case may break down between terms. This skill makes that risk visible and manageable.

## Audience

Supervising solicitor/barrister or departing students. The supervisor runs it to orchestrate the full cohort offboarding; individual students can run it on their own cases if they're transitioning mid-term (end of placement, withdrawal).

## Load context

- `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/CLAUDE.md` → clinic profile, term, practice areas, supervision style
- `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/deadlines.yaml` → all active deadlines, grouped by case
- `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/client-comms/[case-id]/log.md` (per case) → communications history
- Case files / intake summaries the clinic maintains
- Student roster — who owns what going into the handoff

## Workflow

### Step 1: Identify cases and owners

- Pull all active cases (from intake records + `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/deadlines.yaml` case_ids + client-comms folders)
- For each case: who's the current owner student? Are they staying or leaving?
- Map: outgoing owner → incoming owner (if known; otherwise mark "TBD — supervisor to assign")

If the clinic doesn't maintain a central active-case list, the skill needs one input: a list of active cases. Ask for it. Don't guess.

### Step 2: Per-case handoff memo

For each case:

```markdown
# Case Handoff — [case name] — [term ending]

**Case ID:** [case_id]
**Practice area:** [area]
**Outgoing student:** [name]
**Incoming student:** [name or "TBD"]
**Supervising solicitor / barrister:** [name, SRA/BSB authorisation number]
**Client:** [name or client ID]

---

## Where we are

[One paragraph: current posture. What's been done, what's pending, where the case is heading. If the case is at a natural pause point or between filings, say so.]

## Pending deadlines

*Pulled from `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/deadlines.yaml`. Incoming student's first job is to confirm these are accurate and owned.*

| Due | Type | Description | Notes |
|---|---|---|---|
| [date] | [type] | [one-line] | [if tight: "URGENT — due within [N] days of term start"] |

**ET deadlines: confirm ACAS early conciliation status with supervisor before assuming the deadline in this record is current.**

## What's been done

- [Key actions this term: intake, filings, hearings, letters, tribunal attendance]
- [Documents produced — with pointers to where they live]

## What's open

- [Decisions pending: e.g., "client hasn't decided whether to accept settlement offer"]
- [Research gaps: e.g., "need to confirm whether [jurisdiction] allows [remedy]"]
- [Open communications: e.g., "awaiting response from respondent's solicitors"]

## Client relationship

- [How often has the student been in touch? Phone, email, in-person, interpreter needed?]
- [Any relationship context the next student should know: language preference, vulnerabilities, circumstances affecting scheduling]
- [Upcoming planned contact or appointments]

## Documents drafted / filed

*Pointers, not content.*

- [Date] [Document type] — [path or file reference] — [status: filed / drafted / in review queue / approved by supervisor]

## Communications history summary

*From `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/client-comms/[case-id]/log.md`. Three-line summary here; incoming student reads the full log.*

[Short summary of recent contact patterns — e.g., "4 phone calls since intake, interpreter used for Somali, client prefers morning calls. Last contact: 2026-04-15, confirmed address for tribunal notice."]

## Supervisor's flags for incoming student

*Added by supervisor before the handoff memo goes to the incoming student.*

[flags, or "none"]

## First-week priorities for incoming student

1. [Specific — e.g., "Call [client] within 48 hours of taking the case. Introduce yourself and confirm you've received the case file."]
2. [Deadline-driven — e.g., "ET1 limitation period runs out [date]. Confirm ACAS early conciliation position with [Supervisor] before doing anything else."]
3. [Knowledge-gap — e.g., "Read outgoing student's memo on the housing possession defence before the 10/10 hearing."]

---

**Handoff prepared by:** [outgoing student]
**Date:** [YYYY-MM-DD]
**Reviewed by:** [supervising solicitor/barrister, if applicable per supervision model]
```

### Step 3: Cohort summary

After all per-case memos, produce `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/handoffs/[term]/_summary.md`:

```markdown
# Cohort Handoff Summary — [term ending]

**Departing students:** [N]
**Incoming students:** [N]
**Active cases transitioning:** [N]
**Cases closing at term end (no transition):** [N]

---

## Transitions

| Case | Outgoing | Incoming | Practice area | Urgency |
|---|---|---|---|---|
| [case_id] | [name] | [name or TBD] | [area] | [standard / deadline within 2 weeks / urgent] |

## Unassigned

[cases whose incoming student is "TBD" — supervisor assigns before next term]

## Deadlines within 30 days of term start

[pulled from deadlines.yaml — these are the cases the new cohort hits running]

## Notes for supervisor

- [Any case that raised concern about student performance, flagged for closer supervision]
- [Any case with a safeguarding note that the incoming student must be briefed on]
- [Any case where the outgoing student is willing to stay on consult — e.g., final-year student who wants to mentor the 2nd-year taking over]
- [Patterns across handoffs — e.g., "three of six cases have active deadlines in first 14 days; consider front-loading ramp exercises on those practice areas"]
```

### Step 4: Supervisor review

Closing a case or transitioning it to a new student is a consequential action. The gate is the supervision workflow in `## Supervision style` in `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/CLAUDE.md`. Case-closing memos always get supervisor sign-off before the case is marked closed, regardless of supervision-style choice. `[SRA-CODE]` `[BSB-HANDBOOK]`

Per supervision style:

- **Formal review queue:** every handoff memo goes into the review queue before release to the incoming student. Supervisor approves, edits, or returns.
- **Configurable flags:** memos carry "CHECK WITH [SUPERVISOR] BEFORE RELYING" — supervisor reviews informally, student responsible for checking in.
- **Lighter-touch:** memos carry standard AI-assisted label; supervisor reviews through existing structure. Case-closing memos still route to the supervisor before closure.

### Step 5: Hand off

Once reviewed, handoff memos live at `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/handoffs/[term]/[case_id].md`. The incoming student reads them during their `/legal-clinic-uk:ramp` run at the start of next term — `/legal-clinic-uk:ramp` should surface the memos for cases the new student is assigned.

## Integration

- **`/legal-clinic-uk:ramp`:** at the start of next term, reads `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/handoffs/[most-recent-term]/` and surfaces per-case memos for the cases each new student is taking on.
- **`/legal-clinic-uk:deadlines`:** feeds the pending-deadlines section of each memo.
- **`/legal-clinic-uk:client-comms-log`:** feeds the communications history summary.
- **`/legal-clinic-uk:supervisor-review-queue` (if formal review enabled):** handoff memos route here for supervisor approval.

## What this skill does not do

- **Close cases.** Handoff is for cases transitioning to the next cohort. Cases closing at term end should get a final internal status memo (`/legal-clinic-uk:status internal`) for the file and be marked closed in the handoff document.
- **Assign incoming students.** The supervisor assigns. The skill records what the assignment is; it doesn't pick.
- **Generate handoffs from scratch without clinic data.** Needs the active case list as input.
- **Replace a conversation.** The written memo is the record. The outgoing student should also have a conversation with the incoming student where feasible — the memo captures facts; a conversation captures judgment and relationship context the memo can't.
