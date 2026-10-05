---
name: exam-forecast-uk-agents
title: /law-student-uk:exam-forecast
description: Analyse past exams from the same lecturer to surface patterns — subject weighting, recurring issue-spot traps, favoured hypo types, policy-vs-doctrine mix — and forecast likely emphases for the upcoming exam. Use when the user says "what's on the exam", "analyse past exams", "predict the exam", or shares past exams.
author: uk-agents
author_url: https://github.com/uk-agents/uk-legal-plugins/tree/main/law-student-uk/skills/exam-forecast
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: general
language: en
---

# /law-student-uk:exam-forecast

1. Load `~/.claude/plugins/config/uk-legal-plugins/law-student-uk/CLAUDE.md` → module, lecturer, exam format, syllabus.
2. Apply the workflow below.
3. Intake past exams (PDF, paste, or paths). Confirm sample size.
4. Analyse each past exam: format, subject coverage, question style, fact-pattern density, recurring traps.
5. Cross-exam pattern analysis — what's stable, what varies.
6. Combine with current syllabus to produce forecast: subject weights, format, hobby horses, study emphasis.
7. Write `~/.claude/plugins/config/uk-legal-plugins/law-student-uk/exam-forecasts/[module]/forecast-[YYYY-MM-DD].md`. Framed as weighting heuristic, not prediction.

---

## Purpose

Every lecturer's exam has fingerprints. The same hypo structures recur. The same traps come back. The same subject ratios repeat. Students who have prior exams study smarter; students who don't, study harder. This skill analyses the prior exams you have and surfaces the patterns.

Not magic. A forecast, not a prediction. The skill cannot tell you what's on the exam — it can tell you what's been on past exams and what's likely to recur based on syllabus coverage.

## UK exam context

UK law school exams typically fall into three main types:
- **Problem questions (hypos):** "Advise A" / "Discuss the liability of X" — apply law to facts using IRAC/CILAC structure.
- **Essay questions:** "Critically evaluate..." / "To what extent..." — analytical or normative discussion of doctrine or policy.
- **Mixed format:** a combination of problem questions and essays, often with element of choice.
- **SQE1-style:** multiple-choice, single-best-answer (if module is SQE1 prep).
- **Open book vs. closed book:** note the format — closed-book exams reward rule-recall; open-book exams reward issue-spotting and application.

The forecast should identify which format type the lecturer has historically used.

## Confidence discipline

- Pattern analysis (what subjects appeared, how many questions per topic, how often policy vs. rule-application) — confident where the exams are clearly in front of me.
- Inference about likely emphasis on upcoming exam — `[UNCERTAIN]` is the default; these are forecasts, not certainties. Explicitly frame as "based on the [N] past exams you shared, [topic] appeared in [M]. Your upcoming exam may emphasise it, or the lecturer may rotate — use this as a weighting for review time, not a prediction."
- If only 1-2 past exams are available, say so explicitly — any pattern inferred from 1 exam is noise.
- If the lecturer is new (no past exams available), skill can't forecast. Say so; fall back to syllabus-based "these are the subjects covered" only.

## Load context

- `~/.claude/plugins/config/uk-legal-plugins/law-student-uk/CLAUDE.md` → current modules, exam formats, syllabus if captured
- User-provided past exams (PDF, pasted text, paths)
- Optional: module guide for the current module (for "what's been covered to date")

**If the uploaded past exams have a lecturer's name, use it to match patterns** (same-lecturer exams are the highest-signal input). **If not, match on subject and structure.** Don't ask the user to type in the lecturer's name — use what's in the materials.

## Workflow

### Step 1: Intake

- Which module are we forecasting for?
- How many past exams from this lecturer are available?
- Are they from the same module, or different modules by the same lecturer?
- Are any of them the open-book / closed-book / different-format variants, vs. the typical format for your upcoming exam?
- Module guide for your current module?

If fewer than 3 past exams: flag as thin sample. Pattern inference is weaker.
If exams are across different modules: some patterns transfer (question style, policy vs. doctrine ratio); subject-specific patterns don't.

### Step 2: Read each past exam

For each past exam:

- Format (number of questions, length, time limit, open/closed book, choice offered)
- Subject coverage (which topics tested, in what proportion)
- Question style (issue-spotter problem question, single-issue deep, policy essay, short-answer, mix)
- Fact pattern density (fact-heavy hypos, sparse facts with doctrinal focus, or policy prompts with no facts)
- Recurring traps (e.g., lecturer always hides the consideration issue in an otherwise-clean Contracts fact pattern; lecturer always asks about the exception rather than the rule)
- Policy vs. doctrine ratio
- Whether case names are expected in answers (some UK lecturers mark up for OSCOLA citation accuracy)
- Unusual structures (moot scenario, open research exercise, coursework-vs-exam)

### Step 3: Cross-exam pattern analysis

Roll up what's consistent across exams:

**Stable patterns (appeared in most/all past exams):**
- Subject weights (e.g., "offer and acceptance and consideration account for 30% of exam questions consistently")
- Question style (e.g., "always one long issue-spotter problem + one policy essay")
- Lecturer hobby horses (e.g., "always tests promissory estoppel even when it's a minor topic in class")

**Variable patterns (appeared in some but not all):**
- Policy essays (e.g., "appeared in 2 of 4 past exams — usually when the semester covered a policy-heavy topic late")
- Open-book vs. closed-book differences
- Whether questions require specific case citation (OSCOLA) or just rule statements

**Absent patterns worth noting:**
- Topics covered in class that have NEVER been tested in past exams — don't skip these, but don't weight them heavily either
- Topics tested in past exams that aren't in your current syllabus — probably not coming back

### Step 4: Forecast for the upcoming exam

**Header — required, first line of the forecast, both in-chat and in the saved file.** Per plugin config `## Outputs`, every study output carries the verbatim study-notes header. The forecast is a study output. Do not omit, rephrase, or relocate the header:

```
STUDY NOTES — NOT LEGAL ADVICE
```

Combine pattern analysis with current syllabus:

```markdown
STUDY NOTES — NOT LEGAL ADVICE

# Exam Forecast — [module / lecturer] — [date]

**Past exams analysed:** [N]
**Sample confidence:** [thin (<3) / moderate (3-5) / strong (6+)]
**Caveats:** [e.g., "one of the past exams was an open-book resit; your upcoming is closed-book. Pattern transfer is partial."]

---

## Subject weighting (historical)

| Topic | Past exam weight (avg) | In current syllabus? | Forecast weight |
|---|---|---|---|
| [topic 1] | [%] | [yes/partial/no] | [heavier / stable / lighter] |

## Question-style forecast

- **Format likely:** [X problem questions + Y essays, or similar; choice of N from M]
- **Fact-pattern density:** [fact-heavy / sparse / mixed]
- **Call style:** [one broad call / multiple specific calls / bullet sub-parts]
- **Citation expected:** [OSCOLA case citation expected in answers / rules only]

## Lecturer hobby horses to watch

- [topic A] — appeared in [M of N] past exams. Weighted 3-5x its syllabus share.
- [topic B] — [pattern]
- [trap pattern] — e.g., "always hides promissory estoppel in an otherwise-clean Contracts question"

## Topics covered this term but rarely tested

[list — don't skip, but don't over-weight]

## Study emphasis recommendation

Based on past exam patterns AND current syllabus coverage:

**Heavy:** [topics likely to anchor the exam — 40-50% of study time]
**Moderate:** [supporting topics — 30-40%]
**Sanity check:** [topics covered but historically under-represented — 10-20%, just in case]

## [UNCERTAIN — framing]

This forecast is derived from [N] past exams. Lecturers vary. Lecturers rotate topics. Topics that were emphasised in past years can be de-emphasised when the syllabus shifts or when a new case is decided. Treat this as a weighting heuristic for study time, not a prediction. The exam will include surprises.
```

### Step 5: Output location

Write to `~/.claude/plugins/config/uk-legal-plugins/law-student-uk/exam-forecasts/[module]/forecast-[YYYY-MM-DD].md`. Versioned — if the student gets another past exam mid-term, re-run and append.

## Integration

- **outline-builder:** forecast weights feed into outline depth decisions — weight depth on heavy topics
- **flashcards:** forecast-heavy topics get more cards generated
- **bar-prep-questions:** for SQE1 prep modules, exam-forecast can analyse the SRA's published practice papers rather than lecturer-specific past exams
- **irac-practice:** use forecast topics as the subject areas for IRAC/CILAC practice hypos

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customise the options to what this skill just produced. The tree is the output; the student picks.

## What this skill does not do

- **Predict specific questions.** Past exams show patterns; they don't show you tomorrow's prompt.
- **Work without past exams.** If you don't have prior exams from this lecturer, the skill can't forecast — it falls back to "here's what the syllabus covers, study that."
- **Replace studying everything on the syllabus.** Forecast is weighting, not elimination. Skipping a topic because it's historically under-represented is how students get burned.
- **Account for changes you don't know about.** If the lecturer has shifted focus this year (e.g., emphasised a new leading case — say, a new Supreme Court decision — in lectures), the skill doesn't see that unless you tell it.
- **Work reliably with 1-2 past exams.** Thin sample. Flag as such.
