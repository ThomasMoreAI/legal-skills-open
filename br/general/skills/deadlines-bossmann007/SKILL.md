---
name: deadlines-bossmann007
title: /deadlines
description: Track case deadlines — add, cross-case rollup report, update, complete, close. Warns at configurable thresholds (default 14/7/3/1 days); overdue items stay flagged until resolved. The operational record for a clinic workload. Use when a student or supervisor needs to add a deadline, ask what's due this week, get a deadline report, or update a case deadline.
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/legal-clinic/skills/deadlines
license: Apache-2.0
version: 0.1.1
execution_mode: open
jurisdiction: br
practice: general
language: en
sources:
- title: Br
  path: references/plausibility-bands/BR.md
---

# /deadlines

1. Load `~/.claude/plugins/config/claude-for-legal/legal-clinic/CLAUDE.md` → jurisdiction, practice areas, warning-day cadence.
2. Use the workflow below.
3. Route by flag:
   - `--add`: capture case, type, description, due date, source, owner. Write to `~/.claude/plugins/config/claude-for-legal/legal-clinic/deadlines.yaml`. Check for duplicates first.
   - `--report` (default): cross-case rollup — overdue, next 3d, next 7d, next 14d; by owner; by practice area; unassigned flags.
   - `--update [id]`: modify fields; log note with date.
   - `--complete [id]`: mark done; confirm with student that work is actually filed/submitted.
   - `--close [id]`: close-without-completing; require rationale in notes.
4. Confirm any write before committing.

---

# Deadlines

## Purpose

A clinic's biggest operational risk is a missed deadline. Students carry multiple cases, work part-time, turn over every semester. Deadlines that live only in individual students' heads get dropped at handoff, get forgotten during finals week, get missed when a student unexpectedly withdraws from the clinic. This skill is the central operational record.

The supervising attorney is on the hook if a deadline is missed. The skill is calibrated to that stakes level — warnings fire early, overdue items stay visible until explicitly resolved, handoffs (via `/semester-handoff`) pull the deadline list forward to the next student.

## Load context

- `~/.claude/plugins/config/claude-for-legal/legal-clinic/CLAUDE.md` → jurisdiction, practice areas, deadline warning days (default 14/7/3/1), supervising attorneys
- `~/.claude/plugins/config/claude-for-legal/legal-clinic/deadlines.yaml` — the ledger

**Jurisdiction assumption.** Deadline calculations and warning thresholds assume the jurisdiction set in CLAUDE.md. Deadlines, tolling rules, computation-of-time rules, and local court practices vary materially by jurisdiction and by specific court. If a matter involves a different state, a specific court's local rules, or a federal vs. state forum question, confirm the deadline against the governing rule with your supervisor before relying on it.

## Modes

Flag: `--add | --report | --update | --complete | --close` (default: report)

### `--add` — log a new deadline

**Inputs:**
- Case ID + name (which case)
- Practice area
- Type (filing / hearing / statute-of-limitations / discovery / cure-period / response / notice / other)
- Description — one line of what's due
- Due date (and time + timezone if applicable)
- Source — where the deadline came from (court order served 2026-04-20, statute 8 USC § 1229a, cure period in contract §7)
- Owner student — the student responsible

The skill generates an `id` slug automatically: `[case]-[short-desc]-[YYYY-MM]`.

**Extraction from other skills:** when `/client-intake`, `/draft`, or `/status` surface a deadline in their output, they should hand off to this skill with pre-populated fields. Student confirms and adds.

**Pre-add check:** if a deadline with the same case_id + type + due_date already exists, flag as likely duplicate and ask before adding.

**Plausibility sanity band.** After the student enters a due date, do NOT compute or verify — but apply a rough plausibility check against typical ranges for the filing type, and flag the student if the date falls far outside. This is scaffolding to catch gross errors in the student's own math, not an alternative to computing against the rule.

**Bands are federais, não estado a estado.** Diferente dos EUA, processo civil brasileiro é federal (CPC/2015) — não há variação de estado para estado nos prazos processuais. Load `references/plausibility-bands/BR.md`, que cobre cível (CPC/2015), Juizados Especiais (Lei 9.099/1995), Locação (Lei 8.245/1991), Trabalhista (CLT) e prescrição (Código Civil) num único arquivo. Confirme apenas foro/comarca e regras locais de tribunal (regimento interno), que podem afetar prazo administrativo mas não a regra processual em si.

**Hard stop if the band file is missing.** If `references/plausibility-bands/BR.md` does not exist, do NOT silently run without plausibility checks. Tell the supervisor:

> "Não encontro `references/plausibility-bands/BR.md` — os arquivos de checagem de plausibilidade não estão presentes. Ainda consigo rastrear prazos (add, report, update, complete, close), mas não consigo fazer a checagem de plausibilidade contra faixas típicas. Todo prazo aceito carregará `warnings: no-plausibility-band` e sua revisão deve tratar as datas como não checadas até o arquivo ser restaurado."

**Sanity check logic:**

1. Load the bands table from `references/plausibility-bands/BR.md` (federal, single file — no per-state variation for civil procedure).
2. After the student enters `due:`, compare to triggering-event date + typical range for that `type:` (if a typical range exists in the loaded band file for the filing type).
3. If inside the range, write the entry. Say nothing — the band exists to catch errors, not to congratulate correct math.
4. If outside the range by a material margin, stop before writing and say:
   > The date you entered falls outside the typical range for [type] in [jurisdiction]. [Type] deadlines for [filing type] typically fall ~[range] after [triggering event]. Your entry: [date], which is [N] days from [triggering event]. Re-check your calculation against [cited rule from the band file] and the jurisdiction's computation-of-time rule. If your calculation is correct (local rule exception, atypical triggering event, tolling, waiver), confirm and I will add the entry as-is. Otherwise, recompute and re-run `/deadlines --add`.
5. If no band is known for this `type:` (unusual filing, non-standard deadline), do not sanity-check — write the entry and note in the `warnings:` field that no plausibility band applies.
6. If the band file is missing entirely for this jurisdiction, the hard stop above applies at cold-start; in steady-state (supervisor acknowledged the gap and proceeded), every entry is written with `warnings: no-plausibility-band`.

**The skill does not compute.** If the student enters `[VERIFY]` in the `due:` field because they haven't done the math yet, write the entry with `due: [VERIFY]` — the sanity band runs only when the student supplies a concrete date. The computation stays with the student and supervisor.

### `--report` (default) — cross-case rollup

Read `~/.claude/plugins/config/claude-for-legal/legal-clinic/deadlines.yaml`. Produce:

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

[count only — expand with `/deadlines --report --horizon=30` for details]

---

## By owner student (workload distribution)

| Student | Overdue | Next 7d | Next 14d | Total active |
|---|---|---|---|---|

## By practice area

[same table, grouped by area]

## Unassigned deadlines

[list — flag if any active deadline has no owner_student]
```

### `--update` — modify an existing deadline

Common updates: due date changed (court continuance), owner changed (reassignment), notes added.

Every update writes a dated note inline; history is visible in the entry.

### `--complete` — mark done

- Sets `status: completed`, `completed_date: [today]`.
- Confirms with the student that the actual work is done and filed/submitted.
- Removes from active reports but stays in the yaml.

### `--close` — close without completing

For deadlines that no longer apply — case settled, motion withdrawn, client dropped the matter. Requires a `notes:` entry explaining why.

## Warning cadence

Per `~/.claude/plugins/config/claude-for-legal/legal-clinic/CLAUDE.md` deadline warning days. Default 14, 7, 3, 1.

Warnings don't auto-surface — this plugin has no scheduled/agent behavior. But any time `/deadlines` is invoked (or `/status`, which routes to this skill for deadline checks), the report pulls forward anything hitting a warning threshold.

If a deadline passes its due date without being marked complete, it moves to `status: overdue` and stays there in every report until explicitly resolved. Overdue deadlines do not auto-close.

## Integration

- **`/client-intake`:** when intake surfaces a timeline urgency (eviction notice date, asylum filing deadline, hearing date), offer to `/deadlines --add` with pre-populated fields.
- **`/draft`:** when a filing draft references a deadline (answer due, objection window), offer to add.
- **`/status`:** the status skill reads `~/.claude/plugins/config/claude-for-legal/legal-clinic/deadlines.yaml` for the relevant case and includes upcoming deadlines in its output.
- **`/semester-handoff`:** reads deadlines.yaml to identify all active deadlines across departing-student cases; each handoff memo carries the deadlines forward.
- **`/supervisor-review-queue` (if formal review enabled):** deadlines near their cutoff get priority in the review queue.

## What this skill does not do

- **Calculate deadlines from triggering events.** If a complaint was served today and the answer is due in 21 days per local rules, the skill doesn't do that math — the student does, using the rule, and logs the resulting date. (Doing the math autonomously creates a liability the skill shouldn't own; rules vary by jurisdiction and court.)
- **File or serve anything.** The skill tracks dates; filing happens outside the plugin.
- **Auto-notify.** No scheduled notifications. The report surfaces warnings when invoked; it doesn't push. A scheduled cron could be added later but would need explicit professor opt-in per clinic.
- **Override local rules.** If the student logs a due date that contradicts local rules, the skill doesn't catch it. Another reason to calendar with `[VERIFY: confirm against local rule]` for any non-routine deadline.
