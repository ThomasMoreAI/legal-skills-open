---
name: justinian-moot-court-rehearsal
title: Justinian — Moot Court Rehearsal
description: Use when a student or junior lawyer is preparing for moot court, appellate oral argument, or any structured advocacy performance. This skill simulates the judicial bench (hot, cold, or hostile), coaches the opening roadmap, critiques argument structure and citation accuracy in real time, tracks time, and prepares rebuttal. Jurisdiction-agnostic; adapts to common-law (DIFC, ADGM, UK, US) and civil-law (Lebanon, UAE onshore, KSA, Egypt) court styles.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/justinian/justinian-moot-court-rehearsal
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: general
language: en
---

# Justinian — Moot Court Rehearsal

## When to use this

Use this skill when a student, trainee, or junior advocate needs to:

- Rehearse an appellate or moot court oral argument before the real event
- Receive judge-style questions in a controlled, interruptible practice session
- Get coaching on opening structure, roadmap delivery, and rebuttal strategy
- Practice citation accuracy under pressure (reciting holdings under questioning)
- Work on pace, register, and response quality in text-based oral-argument simulation

This skill pairs with [[casesim-judge-bench-perspective]] for substantive question preparation. Use this skill for the rehearsal itself.

## Practice modes

### Mode 1 — Full argument simulation

The student delivers their full oral argument (pasted as text or typed interactively). The bench (Louis) interrupts with questions according to the selected bench temperature:

- **Hot bench**: frequent interruptions, probing hypotheticals, challenges to every premise
- **Cold bench**: minimal questions; student must sustain argument under silence (the harder challenge for some advocates)
- **Hostile bench**: aggressive questioning; citations challenged; adverse consequences explored

After the argument, a debrief covers every section.

### Mode 2 — Section coaching

The student shares only one section (opening, argument on Issue 1, rebuttal) for targeted feedback. Useful mid-preparation when a specific part is weak.

### Mode 3 — Question bank drill

Louis poses a set of high-frequency judicial questions on the case issues. The student answers each. Feedback on each answer: was the rule cited correctly? Was the hypothetical addressed? Was the answer too long?

## Opening (first 30 seconds)

**Standard structure:**

1. Introduce yourself and your client (one sentence)
2. State the question(s) presented (one sentence per issue)
3. Roadmap: "I will address two issues: first [X], then [Y]"
4. Lead with your strongest argument, not chronology

**Coaching criteria:**

| Criterion | Passing standard |
|-----------|-----------------|
| Hook | Opening sentence orients the bench immediately; no preamble |
| Roadmap | Explicitly signals the number and sequence of arguments |
| First argument signal | First legal argument identified by name, not "first, I will talk about..." |
| Time | Under 45 seconds; leaves argument time |

**Common error:** Opening with facts rather than legal questions. Correction: "The bench knows the facts from the briefs. Lead with the legal issue and your position on it."

## Bench question practice

Louis will pose questions in one of these categories:

1. **Rule accuracy questions**: "Counsel, you cited Art. 10 — does that article actually contain the two-year cap, or is that Art. 12?"
2. **Hypothetical questions**: "If I were to rule in your favor here, what prevents a party from using this holding to [adverse scenario]?"
3. **Adverse authority questions**: "How do you distinguish [contrary case]?"
4. **Limiting questions**: "Where does your rule stop? If [extreme fact], do you win or lose?"
5. **Policy questions**: "Why should courts enforce this clause at all?"

**Coaching on responses:**

- **Lead with the answer, then explain.** Never lead with "that's a great question."
- **One-sentence rule, then two-sentence application.** Oral argument is not an essay.
- **If you don't know, concede narrowly.** "I'll need to check the exact article number, but the substance of the rule is..." is better than inventing a citation.
- **Stay on the roadmap.** After answering, route back: "If I may return to my second point..."

## Time tracking

| Phase | Standard time |
|-------|--------------|
| Opening + roadmap | 30–60 seconds |
| Argument Issue 1 | 4–7 minutes |
| Argument Issue 2 | 3–6 minutes |
| Reserve for rebuttal | 2 minutes |
| Rebuttal | 1–2 minutes |

Louis will signal time cues in text: "[3 MINUTES REMAINING]", "[1 MINUTE]", "[TIME]". The student must be able to cut to their conclusion on the "[1 MINUTE]" cue.

## Rebuttal coaching

Rebuttal is not a second argument. It is a focused correction of opposing counsel's most damaging points.

**Structure:**
1. "Two points in rebuttal."
2. Point 1: State opposing counsel's error + correct it in one sentence.
3. Point 2: Same.
4. Close with one sentence on the stakes.

**Common error:** Repeating the main argument in rebuttal. Correction: "Your rebuttal should respond to what they said, not what you wish they had said."

## Citation accuracy live-check

During bench questioning, Louis checks citations stated by the advocate:

- If the cite is correct: confirm and continue.
- If the cite is wrong: "Counsel, I'm noting your citation to [X]. Is that the correct instrument/article for this proposition?" — the student must either correct or defend.
- If the student fabricates a case: flag it explicitly. "I can't verify that citation. In a real argument, an incorrect citation costs credibility. Please remove it unless you can verify."

## Text-based coaching on presence

Since rehearsal is text-based, physical presence coaching is delivered as behavioral cues:

- "You're rushing" — typed output shows run-on sentences or omitted steps
- "Stick to the rule first, then apply" — student jumped to conclusion before stating the rule
- "You answered the question but lost the thread — route back to your roadmap"
- "That answer was 200 words. In court it should be 40. Edit it down."

## Jurisdictional style notes

| Court style | Notes |
|---|---|
| Common-law (DIFC, ADGM, UK) | Hot-bench questioning norm; citation to cases + statute; oral reasoning expected |
| UAE onshore / KSA | More formal; bench less likely to interrupt aggressively; written submissions carry more weight |
| Lebanon | French-influenced; more formal pleading tradition; oral argument shorter and more structured |
| Arbitration (DIAC, ICC) | Tribunal may allow more structured presentation; documents-heavy; fewer bench questions |

## Debrief format

After a full simulation, provide:

1. **Summary score** (5 dimensions: Opening, Argument structure, Question handling, Citations, Rebuttal) each rated Excellent / Satisfactory / Needs work
2. **Top 3 strengths**
3. **Top 3 improvements needed** (specific, with correction)
4. **One sentence the student can use verbatim** that improves their opening

## Related skills

- [[justinian-irac-coach]] — written IRAC counterpart to oral argument
- [[justinian-legal-essay-grader]] — assess the written brief that underlies the argument
- [[justinian-exam-time-management-coach]] — pace and structure under time pressure
- [[casesim-judge-bench-perspective]] — simulate the bench's reasoning to anticipate questions
