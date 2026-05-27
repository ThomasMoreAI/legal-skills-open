---
name: deposition-questioning-techniques
title: Deposition Questioning Techniques
description: Generates deposition question sequences using six core examination techniques (Funnel, Boxing-In, Looping, Three C's impeachment, evasive witness handling, admission ladders). Use when preparing deposition outlines, building question sequences for specific topics, impeaching with prior inconsistent statements, or controlling evasive witnesses.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/deposition-questioning-techniques
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
tags: [analysis, checklist, drafting]
---

# Deposition Questioning Techniques

Reference and question-sequence generator for six core deposition examination techniques.

## Prerequisites

- Identify **examination goal** per topic (discover, lock in, impeach, build admissions, control)
- Gather available documents and any prior inconsistent statements
- Have a topic outline ready — this skill converts outlines into question sequences

## Technique Selection

| Goal | Technique | Question Type |
|------|-----------|---------------|
| Learn new information | Funnel Method | Open → Targeted → Closed |
| Lock in / exhaust testimony | FWD Close | Closed, exhaustive |
| Maintain control | Looping | Closed, using witness's words |
| Impeach prior statement | Three C's | Commit → Credit → Confront |
| Build inescapable admission | Admission Ladder | Short leading, one fact each |
| Handle evasive witness | Redirect + Looping | Yes/No redirect, repeat |

## Technique 1: Funnel Method

**Open → Targeted (6Ws+H) → Closed lock-in**

1. **Open** — "Tell me about… / Describe… / Walk me through…" then stop. Use silence. Do not interrupt.
2. **Targeted** — Apply Who / What / When / Where / Why / Which / How to each thread from the narrative.
3. **FWD Close** — Before leaving any topic:
   - **F**: "Any **fact** about [topic] you haven't told me?"
   - **W**: "Anyone with **knowledge** you haven't mentioned?"
   - **D**: "Any **document** you haven't identified?"
   - "Is that everything? Are you sure?"

FWD close prevents witnesses from surfacing new information later and supports fabrication arguments for late-disclosed evidence.

## Technique 2: Boxing-In

Eliminate alternative explanations *before* confronting with damaging evidence.

**Sequence: Commit → Close escapes → Confront**

Example:
- Commit: "The decision was based solely on qualifications, correct?" / "Not on age or any protected characteristic?"
- Close escapes: "That was your understanding at the time?" / "Nobody told you something different?" / "You communicated it was qualifications-based?"
- Confront: "Showing you Exhibit 5, your email: 'We need to bring in some younger energy.' Did I read that correctly?"

## Technique 3: Looping

Embed a word or phrase from the witness's prior answer into the next question.

Example: A: "Various performance concerns." → Q: "These 'performance concerns' — who raised them first?" → A: "Janet." → Q: "When Janet raised these 'performance concerns,' what specifically did she say?"

Uses witness's own words (harder to dispute), forces precision, prevents evasion. With documents, quote the document language and loop it forward.

## Technique 4: Three C's Impeachment

### Commit
Lock witness into current testimony: "You testified X, correct?" / "You're certain?" / "Clear memory?"

### Credit
Build reliability of the prior statement:
- **Prior deposition**: under oath, counsel present, could clarify, no reason to lie, memory fresher
- **Witness-authored document**: witness wrote it, near event date, fresh memory, intended accuracy

### Confront
**You read the prior statement aloud. Do not let the witness read it.**

"Let me read from your deposition, page 47, lines 8-12. Question: 'Who was at the meeting?' Answer: 'Myself, Sarah, Tom, and Bill Johnson.' Did I read that correctly?"

**After confrontation**: do not ask witness to explain the inconsistency, ask which version is true, or invite rehabilitation. Move on. Let the inconsistency stand for argument.

## Technique 5: Evasive Witnesses

| Problem | Response |
|---------|----------|
| Non-responsive | "My question was [X]. Can you answer that specific question?" |
| Narrative instead of answer | "Let me ask a yes-or-no question: [rephrase]." |
| "I don't recall" | "Do you *deny* that occurred?" → "So it may have happened — you just don't remember?" |
| Won't answer without docs | Establish no independent recollection, then show document to refresh |
| Argumentative / speeches | "Are you finished? Let me ask my question again: [repeat]." |

Do not argue, show frustration, or repeat identical questions. Use the record: "The transcript will reflect your answer."

## Technique 6: Admission Ladder

Stack undeniable facts until the conclusion is inescapable.

**Rules:**
- One fact per question — never compound
- Keep questions short
- Anchor to documents ("According to this email, [fact], correct?") or prior testimony
- Do NOT ask "why" — opens explanation; save for argument

Example (establishing pre-termination knowledge of complaint): "Ms. Smith worked in your department?" → "You were her supervisor?" → "She filed a harassment complaint in January 2024?" → "HR notified you?" → "You read that email dated January 15?" → "Ms. Smith was terminated February 1?" → "So when you made that decision, you knew about her complaint?"

## Generating Sequences

Provide these inputs to generate a question sequence:
- **Topic** being examined
- **Goal** (discover / lock in / impeach / build admission)
- **Expected witness testimony**
- **Available documents**
- **Prior inconsistent statements** (source, date, substance)

Output includes: question sequence with technique applied, document introduction points, anticipated answers and follow-ups, escape routes to close.

## Checks

- FRE 607, 611, 613 govern impeachment and examination form [VERIFY jurisdiction-specific rules for state depositions]
- Deposition objections generally limited to form — witness must still answer
- "Asked and answered" is not a valid deposition objection in most federal courts [VERIFY local rules]
- Preserve the record: state exhibits by number, read quoted language into the transcript
- Related skills: `deposition-preparation`, `deposition-objection-reference`, `deposition-30b6-corporate-rep`, `deposition-expert-witness`
