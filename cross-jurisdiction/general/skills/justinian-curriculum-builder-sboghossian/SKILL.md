---
name: justinian-curriculum-builder-sboghossian
title: Justinian — Curriculum Builder
description: Use when a user wants a personalized legal-education curriculum — a structured, week-by-week study plan calibrated to their level (1L through bar candidate), target jurisdiction, practice area interests, specific weaknesses, and available time. Produces a complete learning plan with readings, practice problems, simulated exam scheduling, and progress-tracking milestones. Covers all MENA and secondary jurisdictions; P0 priority.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/justinian/justinian-curriculum-builder
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: general
language: en
---

# Justinian — Curriculum Builder

## When to use this

Invoke when a user says any of the following:
- "I need a study plan for [exam or subject]"
- "Build me a curriculum for the bar"
- "I want to learn [practice area] — where do I start?"
- "I have [X] months before my exam — what should I study?"
- "I'm weak on [subject] — what's the right order to study?"

Also invoke proactively when a user selects a bar exam prep skill and hasn't yet generated a study plan.

## Required inputs

| Input | Why it matters | Default if missing |
|---|---|---|
| **Level** | Determines complexity and assumed prior knowledge | Ask: "1L, 2L, 3L, LLM, or bar candidate?" |
| **Target jurisdiction** | Determines which legal system and exam rules apply | Ask: "Which country/jurisdiction are you preparing for?" |
| **Target exam or goal** | Determines the endpoint and working backward from it | Ask: "Are you preparing for a specific exam, or building foundational knowledge?" |
| **Time available** | Months remaining and hours per week | Ask: "When is your exam / target date, and how many hours per week can you study?" |
| **Specific weaknesses** | Allows weighting toward problem areas | Optional — ask after initial plan is generated: "Any subjects you're already weak on?" |

## Curriculum components

Every curriculum contains five components, scaled to the user's level and time:

### 1. Core doctrinal subjects

Jurisdiction-specific mapping:

| Jurisdiction | Core subjects |
|---|---|
| Lebanon (LB) | COC (obligations), Commercial Code, Penal Code, Civil Procedure, Personal Status, Labor Law |
| UAE | Civil Code, Companies Law, Labor Law (FDL 33/2021), Criminal Procedure, Personal Status, Arbitration |
| KSA | Sharia foundations (fiqh al-muamalat), Companies Law 2022, Labor Law, Civil Procedure, AML, PDPL |
| France (FR) | Code civil, Code de commerce, Code pénal, Procédure civile, Droit du travail, Droit européen |
| UK (SQE) | FLK1 subjects (Contracts, Torts, Civ Pro, Const Law, Business), FLK2 subjects (Property, Wills, Trusts, Criminal) |
| US (UBE) | MBE 7 (Civ Pro, Const Law, Contracts, Crim Law, Evidence, Property, Torts) + MEE extras |
| Multi-jurisdiction | GCC harmonized principles, Islamic commercial law, OHADA for Francophone Africa |

### 2. Practice-area depth

If the user has a specialization interest (M&A, labor, real estate, criminal, family), add a targeted module:

- **Corporate / M&A**: company formation, share transfers, due diligence, SPA drafting
- **Labor**: employment contracts, termination, non-compete, EOSG calculations
- **Real estate**: property acquisition, lease structures, mortgage/pledge
- **Criminal defense**: procedure, evidence, sentencing, ethics of criminal representation
- **Family**: personal status, divorce, custody, inheritance — jurisdiction-specific confessional/civil split

### 3. Skills training

Every curriculum includes:

- **IRAC writing**: structured analysis practice — issue, rule, application, conclusion (see the IRAC coach)
- **Legal writing**: memo drafting, professional correspondence
- **Oral argument**: for bar exams with oral components (LB, KSA, UAE, FR grand oral)
- **Drafting**: sample contracts in the user's practice area (see [[justinian-flashcards-from-statute]] for statute mastery)

### 4. Bar exam preparation

For bar candidates: insert exam-specific practice blocks:

- **Flashcard cycles** (see [[justinian-flashcards-from-statute]]): at least 20–30 minutes daily
- **Timed question practice** (see [[justinian-exam-time-management-coach]]): weekly timed simulations
- **Simulated exams**: at least 2 full practice exams before the real thing
- **Weak-area remediation**: after each simulation, identify the 2–3 weakest subjects and schedule a remediation block

### 5. Practical exposure

- **Case law reading**: 2–3 landmark cases per subject per week (Socratic analysis via [[justinian-case-explainer-socratic]])
- **Real-world application**: analyze a real contract or judgment in the user's target practice area
- **Issue-spotting drills**: 3–5 fact patterns per week with self-grading rubric

## Output format

### Weekly curriculum structure

Each week is structured as:

```
Week [N]: [Subject focus]

Topics:
- [Topic 1]: readings + key articles/provisions to master
- [Topic 2]: readings + key articles/provisions to master

Practice:
- Flashcard review: [deck] — 30 minutes
- IRAC practice: [fact pattern] — answer and self-grade
- MCQ drill (if applicable): [N] questions on [subject]

Simulated exam: [if applicable — full or partial]

Progress check: After this week, you should be able to [outcome statement]
```

### Adaptive adjustments

- After each simulated exam, compare results to the expected score trajectory
- If a subject is consistently weak across two exams: add a remediation block (2–3 days dedicated to that subject)
- If the user is ahead of schedule: compress remaining coverage and increase practice exam frequency
- If the user is behind: reprioritize by exam weight (e.g., for MBE: Contracts + Torts + Evidence are ~38% of questions; prioritize these)

## Example plan output (bar candidate, 6 months, UAE bar)

```
Month 1 — Foundations
Week 1–2: UAE Civil Code (obligations and contracts)
Week 3–4: Companies Law FDL 32/2021 (formation, management, liquidation)

Month 2 — Labor and Employment
Week 1–2: Labor Law FDL 33/2021 — all key provisions
Week 3–4: Practice essays on employment termination; EOSG calculations

Month 3 — Procedure and Criminal
Week 1–2: Civil Procedure FDL 42/2022
Week 3–4: Penal Code + Criminal Procedure + Cybercrimes Law

Month 4 — Special topics
Week 1–2: Arbitration Law FDL 6/2018 + DIAC Rules
Week 3: AML + PDPL
Week 4: Personal Status (Muslim and non-Muslim tracks)

Month 5 — Intensive practice
Weeks 1–2: Full simulated exam 1 + remediation
Weeks 3–4: Subject-specific remediation + oral practice

Month 6 — Final preparation
Week 1–2: Full simulated exam 2
Week 3: Weak-area final push
Week 4: Light review only; rest; oral delivery practice
```

## Related skills

- [[justinian-flashcards-from-statute]]
- [[justinian-case-explainer-socratic]]
- [[justinian-exam-time-management-coach]]
- [[justinian-bar-exam-prep-lb]]
- [[justinian-bar-exam-prep-ksa]]
- [[justinian-bar-exam-prep-uae]]
- [[justinian-bar-exam-prep-fr-crfpa]]
- [[justinian-bar-exam-prep-uk-sqe]]
- [[justinian-bar-exam-prep-us-bar]]
