---
name: justinian-exam-time-management-coach
title: Justinian — Exam Time Management Coach
description: Use when a student or bar candidate needs specific guidance on pacing, time allocation, and exam strategy for timed legal examinations — MBE, MEE, MPT, CRFPA note de synthèse, KSA bar, UAE bar, SQE1/SQE2, or Lebanese concours. Provides per-exam pacing rules, skip-and-return strategy, last-minute sweep checklist, anxiety management cues, and builds a personal pacing log over practice sessions. Covers all exam jurisdictions.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/justinian/justinian-exam-time-management-coach
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: general
language: en
---

# Justinian — Exam Time Management Coach

## When to use this

Invoke when a user says:
- "I keep running out of time on [exam]"
- "How should I pace myself for the MBE / MEE / CRFPA?"
- "I freeze up mid-exam — what should I do?"
- "How much time should I spend on each question?"
- "I have 10 minutes left and 20 questions — what do I do?"

This skill addresses the *process* of taking timed legal exams — not the substantive law. It pairs with [[justinian-curriculum-builder]] for the study plan and [[justinian-case-explainer-socratic]] for content.

## Per-exam pacing guide

### MBE (US Bar — 200 MCQs, 6 hours)

| Phase | Allocation | Target per question |
|---|---|---|
| Morning session (100 questions) | 3 hours = 180 minutes | **1 min 48 sec** per question |
| Afternoon session (100 questions) | 3 hours = 180 minutes | **1 min 48 sec** per question |

**Pacing rules**:
- Hard limit: do not spend more than 2 minutes 30 seconds on any single question
- At the 90-minute mark in each session: you should be on question 50 (±3)
- At the 150-minute mark: question 83 (±3)
- Use all remaining time for flagged questions; never submit early

**Skip-and-return strategy**:
- If a question takes more than ~90 seconds with no clear answer: mark your best guess, flag it, move on
- Return to flagged questions after completing all 100 — a later question sometimes unlocks a flagged one
- On return: if your first instinct was strong, trust it; change only if you have a clear reason

### MEE (US Bar — 6 essays, 3 hours = 30 min each)

| Phase | Time | Activity |
|---|---|---|
| Reading the prompt | 3–4 min | Identify issues; don't start writing yet |
| Outlining | 3–4 min | Map your IRAC structure; bullet points only |
| Writing | 20–22 min | Execute the outline; prioritize issues by weight |
| Review | 2 min | Check for any missed issues; correct obvious errors |

**Common pacing error**: spending 15+ minutes on issue 1 and rushing through issues 2 and 3. Graders award points per issue identified — a partial answer on 4 issues often beats a complete answer on 2 issues.

### MPT (US Bar — 2 tasks, 90 min each)

| Phase | Time | Activity |
|---|---|---|
| Read the task memo | 5 min | Understand the output document required and the task constraints |
| Skim the library | 10 min | Identify relevant authorities; mark key paragraphs |
| Read the file | 10 min | Identify relevant facts; mark key items |
| Draft outline | 10 min | Structure your output document |
| Write | 50 min | Execute; use the library and file actively |
| Review | 5 min | Check task compliance; ensure format matches the requested document |

**Key rule**: the MPT tests document-drafting under time pressure. The first 25 minutes (reading + outlining) are just as important as the writing phase.

### CRFPA Note de Synthèse (France — 5 hours)

| Phase | Time | Activity |
|---|---|---|
| Read through the dossier | 45–60 min | Read all documents; annotate; identify the common theme |
| Develop the plan | 30–45 min | Two-part structure; test it against the dossier; don't start writing until the plan is solid |
| Draft introduction | 15 min | Problem statement; plan announcement (annonce du plan) |
| Draft Part I | 45–60 min | Two sub-parts; integrate document references |
| Draft Part II | 45–60 min | Two sub-parts; integrate document references |
| Draft conclusion | 10–15 min | Brief synthesis; no new ideas |
| Review | 20–30 min | Check: are all documents represented? Is the plan balanced? Proofread |

**The planning trap**: candidates who start writing without a solid plan spend 4 hours producing an unstructured synthesis. The 30–45 minutes spent on planning repays itself 3–4x in writing speed.

### SQE1 FLK (UK — ~180 MCQs, ~4 hours)

| Target | Metric |
|---|---|
| Average per question | ~1 min 20 sec |
| Hard limit per question | 90 seconds |
| Checkpoint at 60 minutes | Should be on question ~45 |
| Checkpoint at 2 hours | Should be on question ~90 |

Strategy mirrors MBE: flag and skip; return at the end. Trust first instincts; change only with specific reason.

### KSA / UAE Bar (Arabic-language written exams)

Arabic legal writing takes more time than English for most candidates. Adjust:
- Read question in full before planning answer (Arabic legal grammar sometimes buries the precise issue)
- Plan in Arabic bullet points before writing formal prose
- For MCQs: translate ambiguous terms explicitly before applying the rule

General pacing rule: similar to other bar exams — 1.5–2 minutes per MCQ; 25–30 minutes per essay question.

### Lebanese Concours (written + oral)

**Written**: Standard IRAC essays; 20–25 minutes per question; use any remaining time to add statutory citations
**Oral**: 3–5 minutes of preparation time is typically available; use it to structure your argument as: issue → rule (statute) → application → conclusion

## The last-15-minutes sweep

For any MCQ-heavy exam:

1. Are all questions answered? (No blanks — there is no negative marking on most bar exams)
2. Revisit flagged questions: use the 15 minutes to resolve as many as possible
3. For unresolvable flags: use the elimination technique — eliminate clearly wrong answers, then pick between the remaining 2
4. Do not change answers that you are confident about; change only flagged answers where you've found new clarity

## Anxiety management

**The breath reset**: if you feel panic rising mid-exam, stop for 15 seconds. Breathe in (4 seconds), hold (4), out (4). One cycle is sufficient to reset the cortisol response enough to continue.

**The cognitive override**: "I know this material. I have prepared. This question is testing what I know." Say this as a deliberate override to the "I don't know this" catastrophizing spiral.

**Physical preparation** (night before and morning of):
- Sleep 7+ hours — memory consolidation depends on it
- No all-night studying; cramming on exam eve degrades performance
- Eat before the exam; hunger is a cognitive load
- Bring permitted items (water, approved calculator if allowed); verify the exam's permitted items in advance

## Personal pacing log

Over multiple practice sets, Justinian tracks:
- Average time per question by subject (which subjects take you longer?)
- Accuracy on first-attempt vs revisited questions (are your instincts reliable?)
- Score trajectory per practice session
- Pacing profile: are you consistently running out of time, or are you finishing with time to spare?

Use the log to calibrate: if Contract questions take you 2+ minutes on average, dedicate an extra week to Contracts fluency.

## Related skills

- [[justinian-curriculum-builder]]
- [[justinian-bar-exam-prep-us-bar]]
- [[justinian-bar-exam-prep-uk-sqe]]
- [[justinian-bar-exam-prep-fr-crfpa]]
- [[justinian-bar-exam-prep-ksa]]
- [[justinian-bar-exam-prep-uae]]
- [[justinian-bar-exam-prep-lb]]
