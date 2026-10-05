---
name: study-plan-uk-agents
title: /law-student-uk:study-plan
description: Build or update a long-term SQE or exam prep study plan — phases, subjects weighted by weakness, daily session schedule, adaptive to session history in study-plan.yaml. Use when the user says "build a study plan", "plan my SQE prep", "plan my revision", "schedule my studying", or "how should I study for [X]".
author: uk-agents
author_url: https://github.com/uk-agents/uk-legal-plugins/tree/main/law-student-uk/skills/study-plan
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: general
language: en
---

# /law-student-uk:study-plan

1. Load `~/.claude/plugins/config/uk-legal-plugins/law-student-uk/CLAUDE.md` → qualification route, exam format, exam date, weak subjects, target study hours/day, prep course.
2. Load `~/.claude/plugins/config/uk-legal-plugins/law-student-uk/study-plan.yaml` if it exists.
3. Apply the framework below.
4. Route by flag:
   - `--build` (default if no plan exists): walk the inputs gate (exam, subjects, hours/week, days off, methods). Build the phase structure + daily schedule for the first two weeks. Write `study-plan.yaml`.
   - `--update` (default if plan exists): re-read `session_history`, adjust subject priorities and weekly_hours, fill in the next stretch of daily schedule.
   - `--status`: what's scheduled today / this week, score trend, subjects slipping, next scheduled session per subject.
   - `--cram`: force cram mode — 80/20 high-yield prioritisation, daily MCQ volume, taper last 2-3 days.
5. Before writing: summarise the plan in prose and confirm with the student. Adjust based on their answer.
6. Always sanity-check hours/week against the student's stated life constraints. Over-ambitious plans fail.

---

## Purpose

Sitting down to revise and not knowing what to revise is how weeks disappear. This skill builds a plan — weeks to exam, sessions per day, subjects per week, session types — and then adapts as the student actually does the sessions. It is a living plan, not a calendar export.

It also gives downstream skills (bar-prep-questions, flashcards, drill, irac-practice) a shared schedule to honour, so the student isn't asked "what do you want to study today" every time they open a session.

## Confidence discipline

A plan is opinion, not doctrine. The skill states clearly what's an estimate:

- **Time-per-topic estimates** are general guidance (based on typical SQE prep course weightings from BPP, BARBRI UK, Kaplan, ULaw). Flag them as estimates — the student's real pace will differ.
- **Subject weightings** are derived from the student's own reported weak subjects and session history. Confident.
- **High-yield-topic prioritisation in cram mode** is based on SRA's published SQE1 assessment weightings and historical patterns from published SQE materials. Flag any "this is definitely on the exam" claim as `[UNCERTAIN — past frequency is not a prediction]`.

## Load context

`~/.claude/plugins/config/uk-legal-plugins/law-student-uk/CLAUDE.md`:
- Qualification route, exam format, exam date
- Current modules (for LLB/GDL use)
- Weak subjects
- Prep course (BPP / BARBRI UK / Kaplan / ULaw / self / N/A)
- Target study hours/day

`~/.claude/plugins/config/uk-legal-plugins/law-student-uk/study-plan.yaml` if it exists — extend, don't overwrite.

## Workflow

### Step 1: What are we planning for

> What are we building a plan for?
>
> 1. **SQE1 FLK1** — 180 multiple-choice questions, English law
> 2. **SQE1 FLK2** — 180 multiple-choice questions, English law (property-heavy)
> 3. **SQE2** — skills assessments: client interview, legal research, legal writing, advocacy, case analysis
> 4. **LLB finals** — module exams (tell me which modules and their dates)
> 5. **BPTC** — Bar vocational skills components (tell me which)
> 6. **DPLP / Scots qualification** — Scottish professional legal practice diploma
> 7. **General term revision** — covering current modules

For SQE1/SQE2: read the exam date from the practice profile, confirm. If no date captured, ask.
For LLB finals: ask for the term-end date and exam schedule as the anchor.
For general revision: ask for the term-end date.

### Step 2: Inputs — one at a time, wait for each

**Ask and wait.** Do not bulk all questions into one prompt and move on.

- **Exam date:** confirmed? (If SQE1: FLK1 or FLK2? They are separate sittings.)
- **Subjects to cover:** for SQE1 FLK1: confirm against SRA's FLK1 subject list (Business Law and Practice, Dispute Resolution, Contract, Tort, Legal System E&W, Constitutional/Admin, EU Law, Human Rights). For FLK2: Property Practice, Wills and Intestacy, Probate, Solicitors Accounts, Land Law, Trusts, Criminal Law and Practice. For LLB/GDL, the module guide subjects. Confirm with student — "any subject I should add or drop?"
- **Strongest subjects:** least priority. Still reviewed, not drilled heavily.
- **Weakest subjects:** most priority. Get more sessions.
- **Hours per week available:** realistic, not aspirational.
- **Life-context sanity check — force it.** After the student gives a number, ask (one question at a time — do not skip):

  > You said [N] hours per week. Before I build this, tell me what else is in your week — job (hours/week), family (kids, caregiving), commute, workout, therapy, clinic placement, anything meaningful. The plan should fit your life, not the other way around. A plan you can't follow is worse than a lighter plan you can.

  Wait for the answer. Then sanity-check the stated hours against their reported load.

  If the student declines to share life context ("just build it"), respect that — but add a `confidence_flags` entry: "Life-context check declined; plan assumes [N] hours/week is sustainable. Revisit at end of week 2 if adherence is below [X]%."

- **Preferred study methods:** multi-select. SQE1 MCQ practice / essay/problem questions / flashcards / outlining / drilling / re-reading. Weight the schedule toward the methods they say they'll actually do.
- **Days off per week:** rest days matter. Plans that schedule 7/7 days fail in week 3.

### Step 2.5: Supplement vs. replace (prep-course users)

If `~/.claude/plugins/config/uk-legal-plugins/law-student-uk/CLAUDE.md` → `Prep course` is **BPP**, **BARBRI UK**, **Kaplan**, **ULaw**, or any other structured prep course (i.e., NOT `self` or `N/A`), the student already has a prep-course calendar. This skill's plan must choose one of two roles:

Ask, one question, wait:

> Your profile says you're on [BPP / BARBRI UK / Kaplan / ULaw]. They publish a day-by-day revision calendar. Two ways this plan can work — pick one:
>
> 1. **Supplement.** The prep course is your primary curriculum. This plan fills gaps: extra MCQ drilling on your weak subjects, targeted essay practice, flashcard loops on the topics you're missing. I won't rebuild the prep-course calendar; I'll layer on top of it.
> 2. **Replace.** You're not following the prep-course calendar. I'll build the whole plan — subjects, hours, phases, schedule — and you drop the prep-course calendar.
>
> Don't pick both. Running two full curricula against each other is how students burn out in week 4.

Wait for the answer. Record it in the yaml as `prep_course_mode: supplement | replace`.

### Step 3: Build the schedule

Calculate weeks-to-exam from today's date. Then:

**Normal mode (4+ weeks out):**
- Split weeks into phases:
  - **Learning phase** (first ~60% of time): one subject per ~3-5 days, mixing outlining/reading with flashcards and a few MCQ questions on fresh material.
  - **Drilling phase** (next ~30%): more MCQ volume (especially SQE1), more essay practice, simulated conditions, all subjects in rotation.
  - **Review phase** (last ~10%): focused on weakest subtopics from session_history, full practice papers, light review of strong areas.
- Weight subjects by weakness: weak subjects get ~2x the hours of strong subjects.
- Schedule day-by-day: which subject, which method, how long. Leave slack for the student's actual life.

**Cram mode (< 4 weeks out):**
- Flag it: "You're less than four weeks out. This is cram mode — the plan prioritises high-yield topics over full coverage. You will leave gaps. That's the tradeoff at this point."
- 80/20 prioritisation: the SQE1 subjects with the highest question weighting per the SRA's assessment specification get the lion's share.
- Daily schedule: MCQ blocks every day (volume matters now for SQE1), essay/problem question practice every other day (for LLB), one simulated sitting per week.
- Sleep and taper the last 2-3 days. Do not schedule hard drilling the day before the exam. This is real — candidates who cram through the night before perform worse.

### Step 4: Write it

Write to `~/.claude/plugins/config/uk-legal-plugins/law-student-uk/study-plan.yaml`:

```yaml
plan_type: sqe1-flk1  # or sqe1-flk2 / sqe2 / llb-finals / bptc / dplp / term-revision
exam_date: 2026-11-10
qualification_route: SQE
jurisdiction: E&W
created: 2026-05-18
last_updated: 2026-05-18
weeks_to_exam: 25
hours_per_week: 20
days_per_week: 5
mode: normal  # or cram
prep_course_mode: supplement  # or replace / n/a
phases:
  - name: learning
    start: 2026-05-18
    end: 2026-07-15
    focus: outlining, flashcards, introductory MCQ
  - name: drilling
    start: 2026-07-16
    end: 2026-10-20
    focus: MCQ volume, essay practice, simulated conditions
  - name: review
    start: 2026-10-21
    end: 2026-11-09
    focus: weak-subtopic review, full practice sittings
subjects:
  land-law:
    priority: high  # weak
    weekly_hours: 4
    methods: [sqe1-mcq, flashcards]
  trusts:
    priority: medium
    weekly_hours: 3
    methods: [sqe1-mcq, outline-review]
  # etc.
schedule:
  - date: 2026-05-18
    day: Monday
    sessions:
      - subject: Land Law
        method: outline-review
        duration_min: 90
      - subject: Land Law
        method: sqe1-mcq
        duration_min: 60
        n_questions: 25
  # etc.
session_history: []  # appended by bar-prep-questions, flashcards, drill, irac as sessions complete
```

### Step 5: Confirm with the student

**Header — required on every in-chat presentation and on any separate prose-format plan document written alongside the YAML.** The first line must be the verbatim header from plugin config `## Outputs`:

```
STUDY NOTES — NOT LEGAL ADVICE
```

Summarise the plan in prose (not raw YAML) before saving, with the header on top:

> STUDY NOTES — NOT LEGAL ADVICE
>
> Here's what I built. [X] weeks to [SQE1 FLK1 / LLB finals / etc.]. [Y] hours/week across [Z] days. Weak subjects (Land Law, Trusts) get 2x the hours. Three phases: learning through [date], drilling through [date], review the last [N] days. I've scheduled the first two weeks day-by-day. Beyond that it's allocated by week — I'll fill in the daily schedule as you complete sessions, so the plan adapts to where you actually are.
>
> Does this feel right? Too ambitious? Too light? Missing a subject?

Adjust based on the answer. Then write.

## Adapting the plan

After each session (via bar-prep-questions, flashcards, drill, irac-practice), the corresponding skill appends to `session_history`:

```yaml
session_history:
  - date: 2026-05-18
    subject: Land Law
    type: sqe1-mcq
    n_questions: 10
    score: 6
    weak_subtopics: [overriding-interests, leasehold-covenants]
```

On the next `/law-student-uk:study-plan --update` run (or when any skill detects the plan is stale):
- Subjects with consistently low scores get promoted in `priority` and `weekly_hours`.
- Weak subtopics within a subject get flagged for the next scheduled session on that subject.
- If the student is falling behind (scheduled sessions not appearing in history), adjust: either compress coverage or note the gap and ask.
- If the student is ahead, open up time for deeper weak-subject drilling.

## Modes

`--build` (default) — fresh plan
`--update` — re-read session_history and adjust weightings, fill in upcoming daily schedule
`--status` — what's on deck today / this week, what's the score trend, what's slipping
`--cram` — force cram mode even if more than 4 weeks out (user override)

## Integration

- `/law-student-uk:session <subject> <n>` writes results to this plan's `session_history`.
- `/law-student-uk:bar-prep-questions` reads the plan to know which subject is scheduled for today.
- `/law-student-uk:flashcards` can `--session <n>` and results land in the plan.
- `/law-student-uk:socratic-drill` and `/law-student-uk:irac-practice` session completions also append.

## What this skill does not do

- **Guarantee you pass.** The plan is a scaffold. The work is on you.
- **Predict the SQE or any exam.** Cram mode uses historical subject frequency; high-yield ≠ guaranteed-tested.
- **Replace your prep course schedule.** If you're on BPP/BARBRI UK/Kaplan/ULaw, this plan can supplement — don't run two full curricula against each other. Use one as primary.
- **Schedule your life.** Hours available is what you tell me. If you overstate, the plan will break in week 2. Be honest.
