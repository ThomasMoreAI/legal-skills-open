---
name: supervisor-review-queue-uk-agents
title: /legal-clinic-uk:supervisor-review-queue
description: Supervising solicitor/barrister review queue — student output waits here for supervisor approval before going to clients or courts/tribunals. Only active if "formal review queue" supervision style was chosen at setup; otherwise dormant. Use when the supervisor wants to see what's waiting for review, approve, edit-then-approve, or return an item. The queue is also an SRA/BSB supervision compliance record.
author: uk-agents
author_url: https://github.com/uk-agents/uk-legal-plugins/tree/main/legal-clinic-uk/skills/supervisor-review-queue
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: criminal
language: en
---

# /legal-clinic-uk:supervisor-review-queue

1. Check `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/CLAUDE.md` → supervision style. If NOT "formal review queue": explain the clinic is set up for [flags/lighter-touch], no formal queue exists, and how to switch.
2. Use the workflow below.
3. Default: show what's waiting, by urgency, by student.
4. Actions: approve / edit-then-approve / return with note. All logged.

```
/legal-clinic-uk:supervisor-review-queue
```

```
/legal-clinic-uk:supervisor-review-queue --approve Q-003
```

```
/legal-clinic-uk:supervisor-review-queue --return Q-004 "Check the ET1 grounds — the protected disclosure argument needs more detail on the qualifying disclosure under ERA 1996 s 43B"
```

---

# Supervisor Review Queue (Optional)

## Purpose

Some UK law school clinics want a formal gate: student drafts, supervisor reviews, output releases. Others find that too prescriptive — they supervise through case rounds and one-on-ones, not through a queue.

**This skill is only active if `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/CLAUDE.md` → Supervision style is "formal review queue."** Otherwise it's dormant.

Whether to use a formal review workflow is genuinely an open question for clinic adoption. It depends on student experience level, caseload, and how the supervisor already runs supervision. The supervisor decides at setup and can change it later.

**SRA/BSB compliance record.** Under the SRA Code of Conduct 2019 and BSB Handbook, the supervising solicitor or barrister is responsible for work done by students acting under their supervision. The review queue log is a record that a licensed supervising solicitor or barrister reviewed student work before it went to a client or was filed with a court or tribunal. That record matters for the clinic's own compliance and for student evaluation. `[SRA-CODE]` `[BSB-HANDBOOK]`

## Load context

`~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/CLAUDE.md` → supervision style. If NOT "formal review queue": respond with "The clinic is set up for [flags/lighter-touch] supervision — there's no formal queue. [Supervisor] reviews through [the clinic's existing structure]. To switch to a formal queue, edit CLAUDE.md → Supervision style."

If formal queue IS enabled → read flag triggers and proceed.

## The queue

Lives at `skills/supervisor-review-queue/references/review-queue.yaml`. Each entry:

```yaml
- id: Q-001
  type: "draft"  # intake | draft | memo | status | client-letter
  client: "[name or ID]"
  student: "[name]"
  submitted: [timestamp]
  flags:
    - rule: "Tribunal filing"
      detail: "ET1 narrative — always queued"
  content_path: "[path to the document]"
  status: "pending"  # pending | approved | edited-approved | returned
```

## Modes

### What's waiting

```markdown
## Review Queue — [date]

**Pending:** [N] | **Oldest:** [N] hours

### 🔴 Deadline-sensitive
| ID | Type | Client | Student | Why flagged | Waiting |
|---|---|---|---|---|---|

### Standard
[same table]

### By student
[Breakdown — spot patterns: who's queueing a lot, who might need a check-in]
```

### Review an item

Show full content + why it was flagged + student notes.

### Approve / edit-then-approve / return

- **Approve:** Status → approved, student notified, logged. The approval log records that the supervising solicitor/barrister reviewed and approved the student work product.
- **Edit then approve:** Supervisor edits inline, approved version is the edited one, original preserved in log so student sees the diff (teaching moment). This is the highest-value supervision interaction — the student sees exactly what the supervisor changed and why.
- **Return:** With a note. Student revises and resubmits.

## Logging

Every action logged at `skills/supervisor-review-queue/references/review-queue.yaml`. Format: `[id] [action] [supervisor] [date] [note if return]`.

Approval logs are clinic records — they document that a licensed supervising solicitor or barrister reviewed student work before it went to a client or court or tribunal. That matters for:
- The clinic's SRA/BSB supervision compliance
- Student evaluation and progression
- Professional negligence (professional indemnity) purposes — a contemporaneous record of supervision is the clinic's first line of defence if a client alleges the work was not properly supervised

## Teaching signal

The queue is also data. Pattern in returns ("Student X keeps missing the limitation period calculation check") is a coaching conversation. Pattern in edits ("Everyone's ET1 narratives are too long and unfocused") is a `/legal-clinic-uk:ramp` update for next term.

## What this skill does NOT do

- **Run unless the supervisor chose it.** It's one of three supervision models, not the only one.
- **Auto-approve.** The supervising solicitor or barrister approves. This cannot be delegated to a student or automated.
- **Replace the clinic's existing supervision structure.** It's a gate for work product, not a substitute for case rounds, one-on-ones, or watching students in action.
- **Satisfy SRA/BSB supervision obligations by itself.** The queue is a tool for one part of the supervision model — compliance depends on the overall structure the supervisor has set up, not on whether a queue exists.
