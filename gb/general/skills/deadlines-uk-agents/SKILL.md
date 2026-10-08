---
name: deadlines-uk-agents
title: /legal-clinic-uk:deadlines
description: Track UK clinic case deadlines — add, cross-case rollup report, update, complete, close. Warns at configurable thresholds (default 14/7/3/1 days); overdue items stay flagged until resolved. The operational record for a clinic workload. Use when a student or supervisor needs to add a deadline, ask what's due this week, get a deadline report, or update a case deadline. Includes plausibility bands for England & Wales (Employment Tribunal 3-month rule, Limitation Act 1980, CPR response deadlines) and pointers for Scotland and NI.
author: uk-agents
author_url: https://github.com/uk-agents/uk-legal-plugins/tree/main/legal-clinic-uk/skills/deadlines
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: general
language: en
---

# /legal-clinic-uk:deadlines

1. Load `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/CLAUDE.md` → jurisdiction, practice areas, warning-day cadence.
2. Use the workflow below.
3. Route by flag:
   - `--add`: capture case, type, description, due date, source, owner. Write to `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/deadlines.yaml`. Check for duplicates first.
   - `--report` (default): cross-case rollup — overdue, next 3d, next 7d, next 14d; by owner; by practice area; unassigned flags.
   - `--update [id]`: modify fields; log note with date.
   - `--complete [id]`: mark done; confirm with student that work is actually filed/submitted.
   - `--close [id]`: close-without-completing; require rationale in notes.
4. Confirm any write before committing.

---

# Deadlines

## Purpose

A UK law school clinic's biggest operational risk is a missed deadline. Students carry multiple cases, work part-time, and turn over every term. The Employment Tribunal's 3-months-less-one-day rule is one of the strictest limitation periods in UK law — and it is unforgiving. The supervising solicitor or barrister is professionally responsible if a deadline is missed. This skill is the central operational record.

## Load context

- `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/CLAUDE.md` → jurisdiction (E&W / Scotland / NI), practice areas, deadline warning days (default 14/7/3/1), supervising solicitor/barrister
- `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/deadlines.yaml` — the ledger

**Jurisdiction assumption.** Deadline calculations and warning thresholds assume the jurisdiction set in CLAUDE.md. Limitation periods, computation-of-time rules, and court/tribunal practice vary materially between E&W, Scotland, and Northern Ireland, and between different courts and tribunals. Confirm every deadline against the governing rule with your supervisor before relying on it.

**Employment Tribunal special note.** The 3-months-less-one-day rule (`[LIMITATION-ACT-1980]`-equivalent in employment law: Employment Rights Act 1996 s 111(2) for unfair dismissal; Equality Act 2010 s 123 for discrimination) is strict and jurisdiction-specific. ACAS early conciliation pauses (does not extend) the limitation period — the ACAS certificate issue date and expiry date must be recorded alongside the deadline. Students must NOT calculate ET deadlines unassisted — they must confirm with the supervising solicitor/barrister and check current ACAS guidance.

## Modes

Flag: `--add | --report | --update | --complete | --close` (default: report)

### `--add` — log a new deadline

**Inputs:**
- Case ID + name (which case)
- Practice area
- Type (filing / hearing / tribunal / limitation / et-claim / et-preliminary / appeal / mandatory-reconsideration / response / notice / other)
- Description — one line of what's due
- Due date (and time if applicable — ET hearings have specific times)
- Source — where the deadline came from (tribunal case management order, statute: Employment Rights Act 1996 s 111(2), Limitation Act 1980 s 5, ACAS EC certificate number [XXXXX] issued [date] expiring [date], etc.)
- Owner student — the student responsible

The skill generates an `id` slug automatically: `[case]-[short-desc]-[YYYY-MM]`.

**Extraction from other skills:** when `/legal-clinic-uk:client-intake`, `/legal-clinic-uk:draft`, or `/legal-clinic-uk:status` surface a deadline in their output, they should hand off to this skill with pre-populated fields. Student confirms and adds.

**Pre-add check:** if a deadline with the same case_id + type + due_date already exists, flag as likely duplicate and ask before adding.

**Plausibility sanity band.** After the student enters a due date, apply a rough plausibility check against typical ranges for the filing type, and flag if the date falls far outside. This is scaffolding to catch gross errors in the student's own math, not an alternative to computing against the rule.

**Bands are jurisdiction-keyed.** Load the band file for this clinic's jurisdiction from `references/plausibility-bands/{jurisdiction}.md` where `{jurisdiction}` is derived from the jurisdiction set in `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/CLAUDE.md`. The legal-clinic-uk plugin ships `references/plausibility-bands/EW.md` (England & Wales — fully populated) as the primary band file. For Scotland and NI, see the jurisdiction notes in EW.md.

**Hard stop at cold-start if the band file is missing.** If `references/plausibility-bands/EW.md` does not exist, do NOT silently run without plausibility checks. Tell the supervisor:

> "I don't have deadline plausibility checks configured — the sanity band file is missing. I can still track deadlines (add, report, update, complete, close), but I cannot sanity-check them against typical ranges. Until the band file is available, every deadline I accept will carry `warnings: no-plausibility-band` and your review should treat dates as unchecked."

**Sanity check logic:**

1. Load the bands table for this clinic's jurisdiction from `references/plausibility-bands/EW.md` (or the applicable jurisdiction file).
2. After the student enters `due:`, compare to triggering-event date + typical range for that `type:` (if a typical range exists in the loaded band file for the filing type).
3. If inside the range, write the entry. Say nothing — the band exists to catch errors, not to congratulate correct math.
4. If outside the range by a material margin, stop before writing and say:
   > The date you entered falls outside the typical range for [type] in [jurisdiction]. [Type] deadlines for [filing type] typically fall ~[range] after [triggering event]. Your entry: [date], which is [N] days from [triggering event]. Re-check your calculation against [cited rule from the band file] and the jurisdiction's computation-of-time rule. If your calculation is correct (ACAS early conciliation pause, different triggering event, any extension granted), confirm and I will add the entry as-is.
5. If no band is known for this `type:`, write the entry and note in the `warnings:` field that no plausibility band applies.
6. If the band file is missing, every entry is written with `warnings: no-plausibility-band`.

**The skill does not compute.** If the student enters `[VERIFY]` in the `due:` field, write the entry with `due: [VERIFY]` — the sanity band runs only when the student supplies a concrete date. The computation stays with the student and supervisor.

### `--report` (default) — cross-case rollup

Read `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/deadlines.yaml`. Produce:

```markdown
# Deadline Report — [today]

**Active deadlines:** [N]
**Overdue:** [N] ⚠️
**Due this week (next 7 days):** [N]

---

## ⚠️ Overdue (flagged for immediate attention)

| ID | Case | Type | Due | Owner | Days overdue |
|---|---|---|---|---|---|

## 🔴 Due today / next 3 days

| ID | Case | Type | Due | Owner |
|---|---|---|---|---|

## 🟡 Due in 4-7 days

| ID | Case | Type | Due | Owner |
|---|---|---|---|---|

## 🟢 Due in 8-14 days

[list]

## Beyond 14 days

[count only — expand with `/legal-clinic-uk:deadlines --report --horizon=30` for details]

---

## By owner student (workload distribution)

| Student | Overdue | Next 7d | Next 14d | Total active |
|---|---|---|---|---|

## By practice area

[same table, grouped by area]

## Unassigned deadlines

[list — flag if any active deadline has no owner_student]

## ⚠️ ET deadlines without ACAS EC details

[list any ET-type deadlines where source field does not include ACAS certificate info — supervisor should verify these urgently]
```

### `--update` — modify an existing deadline

Common updates: due date changed (tribunal continuance), owner changed (reassignment), ACAS early conciliation certificate details added, notes added.

Every update writes a dated note inline; history is visible in the entry.

### `--complete` — mark done

- Sets `status: completed`, `completed_date: [today]`.
- Confirms with the student that the actual work is done and filed/submitted.
- Removes from active reports but stays in the yaml.

### `--close` — close without completing

For deadlines that no longer apply — case settled, claim withdrawn, client dropped the matter. Requires a `notes:` entry explaining why.

## Warning cadence

Per `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/CLAUDE.md` deadline warning days. Default 14, 7, 3, 1.

Warnings don't auto-surface — this plugin has no scheduled/agent behaviour. But any time `/legal-clinic-uk:deadlines` is invoked (or `/legal-clinic-uk:status`, which routes to this skill for deadline checks), the report pulls forward anything hitting a warning threshold.

If a deadline passes its due date without being marked complete, it moves to `status: overdue` and stays there in every report until explicitly resolved. Overdue deadlines do not auto-close.

## Integration

- **`/legal-clinic-uk:client-intake`:** when intake surfaces a timeline urgency (ET claim window, possession hearing, mandatory reconsideration deadline), offer to `/legal-clinic-uk:deadlines --add` with pre-populated fields.
- **`/legal-clinic-uk:draft`:** when a filing draft references a deadline (ET1 window, response deadline, appeal period), offer to add.
- **`/legal-clinic-uk:status`:** the status skill reads `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/deadlines.yaml` for the relevant case and includes upcoming deadlines in its output.
- **`/legal-clinic-uk:semester-handoff`:** reads deadlines.yaml to identify all active deadlines across departing-student cases; each handoff memo carries the deadlines forward.
- **`/legal-clinic-uk:supervisor-review-queue` (if formal review enabled):** deadlines near their cutoff get priority in the review queue.

## What this skill does not do

- **Calculate deadlines from triggering events.** If a client was dismissed today and the ET1 is due in 3 months less one day per Employment Rights Act 1996 s 111(2), the skill doesn't do that math — the student and supervisor do it, using the rule and the ACAS early conciliation position, and log the resulting date.
- **Handle ACAS early conciliation automatically.** The student and supervisor must confirm the ACAS EC certificate issue and expiry dates and factor them into the ET deadline calculation. The skill records what the supervisor and student confirm; it does not integrate with ACAS.
- **File or serve anything.** The skill tracks dates; filing happens outside the plugin.
- **Auto-notify.** No scheduled notifications. The report surfaces warnings when invoked.
- **Override local rules or tribunal orders.** If the student logs a due date that contradicts local rules or a specific tribunal direction, the skill doesn't catch it. Another reason to log with `[VERIFY: confirm against applicable rule / tribunal order]` for any non-routine deadline.
