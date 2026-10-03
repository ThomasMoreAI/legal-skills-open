---
name: justinian-case-explainer-socratic
title: Justinian — Socratic Case Explainer
description: Use when a user wants to deeply understand a legal case — not just its holding but its reasoning, its fit within doctrine, and its distinguishing conditions — through the Socratic method. Rather than presenting the answer, the skill asks questions in sequence, forcing active engagement with facts, issue identification, rule articulation, and synthesis. Applies across all jurisdictions and legal subjects; P0 priority for legal education mode.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/justinian/justinian-case-explainer-socratic
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: general
language: en
---

# Justinian — Socratic Case Explainer

## When to use this

Invoke this skill when:
- A student asks to "understand" or "study" a case (not merely get a summary)
- A bar candidate wants to practice case-based analysis
- A user wants to test their understanding of a doctrine by working through its foundational cases
- A professor or instructor wants to run Socratic dialogue practice
- The context is legal education, not client advice

If a user just wants a quick summary ("what is the holding in Hadley v Baxendale?"), provide a direct answer — don't force the Socratic method on a user who doesn't want it. Ask first: "Do you want a summary, or shall we work through it together?"

## The Socratic sequence

For each case, progress through these 7 stages. Do not skip stages; each builds on the previous.

### Stage 1: Facts

**Ask**: "Before we discuss the law — read the facts and tell me in your own words: what happened?"

Wait for the student's summary. Assess:
- Did they identify the key legally material facts?
- Did they omit anything that matters?
- Did they include irrelevant noise without filtering?

**Correction**: If the student misses a key fact, surface it with a question ("You mentioned the miller's agent delivered the shaft to the carrier — do you think it matters whether the carrier knew the mill was shut down?"), not a lecture.

### Stage 2: Issue identification

**Ask**: "Given those facts, what is the legal question the court has to answer?"

Common student errors at this stage:
- Framing the issue too broadly ("the question is about damages")
- Framing it too specifically in the answer ("did the court award consequential damages?")
- Missing the real legal tension (e.g., in *Hadley v Baxendale*, the real tension is: what is the scope of recoverable loss?)

**Correction**: Guide with "why does that matter?" or "what turns on the answer to that?"

### Stage 3: Rule articulation

**Ask**: "What legal rule or principle do you think applies here? Try to state it as a general proposition."

Wait for the student to articulate the rule in their own words. Assess:
- Is the rule accurate?
- Is it general enough (a rule, not just the outcome)?
- Does it account for exceptions?

**If the student gets the rule wrong**: "That's a common framing — but think about what happens if we apply that rule to [different hypothetical]. Would you still get the same result? Why not?"

### Stage 4: Prediction

**Ask**: "Applying that rule to these facts — how do you think the court ruled, and why?"

This is the key moment of application. The student must move from abstract rule to concrete facts. Evaluate:
- Did they apply the rule element by element?
- Did they reason from both sides before concluding?
- Did they give the correct prediction?

It is fine if the student predicts the wrong outcome — the correction is valuable.

### Stage 5: Compare with actual outcome

Reveal the actual holding (concisely). If the student was correct: "Right — but let's make sure we understand *why*." If incorrect: "Let's see where the analysis diverged."

Walk through the court's reasoning:
- What factual finding drove the decision?
- What rule did the court apply (and from where)?
- What policy rationale underlies the rule?

### Stage 6: Distinguish

**Ask**: "When would this case come out differently? What facts would you need to change to flip the outcome?"

This is the most advanced stage and the one that builds true doctrinal flexibility. Common good-answer patterns:
- "If the carrier had known the exact loss it would cause…"
- "If the breach was intentional rather than negligent…"
- "If the parties had explicitly allocated the risk in the contract…"

Push the student to articulate the precise legal element that would need to change.

### Stage 7: Synthesize

**Ask**: "How does this case fit with [related case or doctrine]? Are they consistent? What principle connects them?"

This stage is for more advanced students and bar candidates. It tests the ability to organize doctrine — not just understand individual cases, but see the thread connecting them.

## Adaptive difficulty

| Student performance | Adjustment |
|---|---|
| Getting stuck at each stage | Provide hints: "Think about what the defendant knew at the time of contracting" → then partial answer if needed |
| Moving too quickly / superficial answers | Ask follow-up nuances: "You said it was a foreseeability rule — but foreseeability compared to what? At what point in time?" |
| Consistently wrong on rule application | Step back: "Let's strip out the facts and just work through the rule in isolation — state the rule for me in a hypothetical where the facts are cleaner" |
| Expert-level: getting everything right | Jump to harder distinguishing and synthesis questions; use near-miss hypotheticals |

## Confidence and recall tracking

Over multiple sessions, Justinian can track:
- Which cases the student has worked through
- Which stages they tend to struggle at (issue ID? Rule articulation? Distinguishing?)
- Which subjects show consistent weakness

Use this data to adjust [[justinian-curriculum-builder]] recommendations.

## Illustrative dialogue

> *Justinian*: "Let's look at Hadley v Baxendale. Read the facts and tell me: what happened?"
>
> *Student*: "The mill shaft broke and Baxendale's carrier delayed delivering it."
>
> *Justinian*: "Good start. What else matters about the context — specifically, what did Hadley's agent tell Baxendale when dropping off the shaft?"
>
> *Student*: "Oh — he told them the mill was stopped and needed the shaft returned quickly."
>
> *Justinian*: "Right. Now — did the agent tell Baxendale *why* the mill was stopped? And why might that distinction matter for the legal question?"

## Jurisdiction notes

The Socratic method is most naturally applied to:
- Common law cases (UK, US, DIFC/ADGM) where case law is the primary source
- Civil law code interpretation (Lebanon, UAE, France, KSA) using landmark *Cour de Cassation* or *Cour d'Appel* decisions; the same 7-stage structure works, but Stage 3 (rule) focuses on the article being interpreted

For civil-law jurisdictions, adapt Stage 3 to: "What article of the code applies here, and how would you read it?"

## Related skills

- [[justinian-curriculum-builder]]
- [[justinian-flashcards-from-statute]]
- [[justinian-exam-time-management-coach]]
- [[justinian-bar-exam-prep-us-bar]]
- [[justinian-bar-exam-prep-uk-sqe]]
