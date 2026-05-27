---
name: witness-prep-session
title: Deposition Witness Preparation
description: Runs ethics-compliant deposition witness-prep workflows for US civil litigation. Use when preparing party, fact, expert, or 30(b)(6) witnesses for deposition, including mock cross-examination, exhibit review, vulnerability mapping, day-of logistics, and post-deposition debrief. Covers intake through deposition day under FRCP 30.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/witness-prep-session
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Deposition Witness Preparation

Ethics-compliant witness-prep workflow from intake through deposition day. Scope is limited to memory-refresh and communication coaching — never script answers or feed facts.

## Quick Start

Gather before first session:

- Deposition notice/subpoena with date, time, site
- Witness identity, role, type (party / fact / expert / 30(b)(6))
- Notice scope: topics, exhibit requests, known objections or court orders
- Prior statements, productions, disclosures, privilege boundaries
- Case theories, weaknesses, and key adverse topics
- Venue rules (FRCP 30 or state analogue)

## Intake Packet

```
Case:
Venue:
Depo date:
Witness name / role / type:
Risk topics:
Known documents:
Known contradictions:
Prior testimony sources:
Privilege-sensitive areas:
30(b)(6) topics (if applicable):
Session length constraints:
```

## Session Model

| Profile | Sessions | Structure |
|---|---|---|
| Straightforward fact witness | 1 | 4–6 h consolidated |
| Standard matter (default) | 2 | 2×(2–4 h), 1–7 day gap |
| Complex or anxious witness | 3 | 2–3 h each, targeted coaching |
| 30(b)(6) corporate rep | 2–3 | Topic-by-topic for each noticed topic |
| High-volume documents | 2–3 | Add dedicated exhibit walkthrough |

## Core Workflow

### 1. Orientation and Document Review (Session 1)

- Set expectations: truth-only, no guessing, admit uncertainty
- Explain deposition mechanics: oath, transcript, objections, court reporter
- Establish behavioral rules: wait for full question, clarify if unclear, answer only what is asked, pause before answering, say "I don't know / recall" when true
- Walk all core documents; record familiarity in a tracking table:

```
Doc | Role (Author/Recipient/Ref) | Significance | Witness Understanding | Risks
```

- Map each topic: why it matters, what witness recalls, high-risk subtopics
- Assign homework: review flagged docs, note concerns

### 2. Mock Examination (Session 2)

- Recheck anxiety, document review completion, new recollections
- Run mock exam with real exhibits and escalating pressure: warm-up, topic exploration, document confrontation, detail probing, commitment questions, impeachment setups
- Coach live on common problems:

| Problem | Correction |
|---|---|
| Answers before question finishes | "Wait for the full question." |
| Volunteers extra facts | "Answer only what was asked." |
| Speculates | "Say you don't know if that's true." |
| Defensive tone | "Stay calm, short, direct." |

- Drill objection handling: objections are counsel's job; witness continues answering unless instructed to stop

### 3. Day-of Support

- 30-min pre-deposition check: stress level, final questions, logistics
- During deposition: narrow non-coaching objections only, break strategy without substantive coaching, monitor fatigue
- Post-deposition: emotional debrief only — no factual deconstruction until transcript review

## Deliverables

- **Witness Preparation Memo**: sessions held, docs reviewed, topics with risk ratings, vulnerable areas and mitigation, ethics compliance confirmation
- **Document Review List**: table of all reviewed documents with familiarity status
- **Topic Readiness Table**: strength, limitations, evidence anchors per topic
- **Day-of Checklist**: arrival, attire, exhibits, videographer, breaks, lunch
- **Problem Areas Summary**: anticipated vulnerabilities, fallback strategies, rehabilitation viability

## Ethics Guardrails

- Preparation must stay within truth-telling coaching and recollection refresh
- Use vulnerability mapping to prioritize difficult topics, not to script answers
- Document all prep decisions for file hygiene and credibility
- Never feed facts the witness does not independently know
- Never suggest conforming testimony or tone-harmonizing language to match other evidence
- Never discuss privileged strategy beyond authorized scope
- Legal anchors: ABA Formal Opinion 508 (2023) [VERIFY]; FRCP 30(c), 30(d) [VERIFY]; adapt to state analogue where federal rules do not govern
- Prefer state-specific deposition customs over generic defaults for video setup, breaks, and privilege assertions

## Related Skills

- `deposition-deponent-coaching` — behavioral coaching techniques
- `deposition-ethics-boundaries` — ethical limits on witness prep
- `deposition-objection-reference` — objection forms and preservation
- `deposition-30b6-corporate-rep` — corporate designee preparation
- `deposition-expert-witness` — expert-specific prep considerations

---

Key changes from the original:

- **Frontmatter**: Removed `tags` (not in spec), tightened `description` to third-person with clear trigger guidance
- **Structure**: Reorganized into Quick Start → Intake Packet → Session Model → Core Workflow → Deliverables → Ethics Guardrails → Related Skills
- **Conciseness**: Collapsed the 10-item prerequisites into a focused Quick Start list; merged the numbered "Output Structure / Process" sections into a clean 3-step Core Workflow; consolidated deliverables into a single bullet list instead of mixed code blocks and prose
- **Ethics**: Elevated guidelines into a dedicated "Ethics Guardrails" section for visibility; converted do/don't prose into direct imperative statements
- **Related skills**: Changed `@` references to backtick-quoted skill names per cross-referencing conventions
- **Line count**: Reduced from 131 to ~100 lines while preserving all domain-critical content
