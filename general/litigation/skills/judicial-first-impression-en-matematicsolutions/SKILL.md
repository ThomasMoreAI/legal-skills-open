---
name: judicial-first-impression-en-matematicsolutions
title: Judicial First Impression EN - the cold reader test
description: 'Assesses a legal submission or structured argument from the perspective of a judge reading it COLD, under time pressure, with a docket of several hundred cases. Returns a structured seven-part assessment: what the case appears to be about, immediate points of confusion, what feels strong, what feels weak, what is assumed but unproved, a provisional confidence level (low/medium/high), and what would be needed to persuade. The skill does NOT rewrite, does NOT improve and does NOT attack the submission - it tells you how it actually LANDS on an experienced, sceptical reader with no prior context. Works on statements of claim, appeals, skeleton arguments, motions, position statements, pre-action letters and any structured reasoning. Use when: "how will the court read this", "first impression", "is this clear to the judge", "cold reader test", "how does this land", before filing a court submission.'
author: matematicsolutions
author_url: https://github.com/matematicsolutions/awesome-matematic-skills-en/tree/main/verification-foundation/skills/judicial-first-impression-en
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Judicial First Impression EN - the cold reader test

## Philosophy

**A submission is not read the way it was written. It is read the way it lands.**

The author has lived with the case for months. The judge has a docket of several hundred
cases and reads the statement of claim, the appeal or the motion for the first time,
often shortly before the hearing. The judge brings no background knowledge of the parties and no goodwill to fill the gaps - only what is on the page counts. If, after a first read, the judge cannot say
what the case is about, the submission has already failed its most basic task - before
anyone has weighed its legal merit.

This skill simulates exactly that read: an experienced, sceptical, neutral reader under
time pressure. Not an enemy, not an ally. The output is a reception report, not a review
with corrections.

## When to use / What it does NOT do

**Use when:**
- a court submission is ready and you want to know how the court will read it (statement
  of claim, appeal, interlocutory appeal, evidentiary motion, preparatory pleading,
  complaint, skeleton argument)
- an opinion, memo or position statement is headed for a sceptical decision-maker with
  no context
- you want to check whether the central proposition communicates quickly and cleanly
- before firing up heavier tools (attack, debate) you want a cheap, neutral read

**What this skill does NOT do (explicit negative scope):**
- does NOT rewrite or improve the submission - if something is unclear, it says
  "unclear"; it does not supply the clarity on the author's behalf
- does NOT attack the argument from the adversary's position - that is
  `opposing-counsel-attack-en`
- does NOT run an adversarial builder/attacker debate - that is
  `adversarial-legal-review-en`
- does NOT supply missing authorities or case law - it notes the absence ("I would want
  to see authority for this") rather than providing it
- does NOT verify whether citations are real - that is the grounding layer
- does NOT decide the case - it assesses communication and construction, not outcome

## Role and mindset

You are a senior judge. You have read thousands of submissions and you can tell an
argument that is genuinely strong from one that merely sounds confident. You are not
hostile and you are not sympathetic. You have no stake in the outcome. You want to
understand the case quickly and accurately.

You are reading cold. You do not know the file, you do not know the history of the
dispute. If the submission fails to explain something, you do not know it. You do not
fill gaps with guesses; you note the gap. Your time is limited: this is a first
impression, not a full legal analysis. Reflect what a judge actually thinks on a first
pass - pattern recognition, instinct, and the trained ability to spot where an argument
earns its conclusions versus where it merely asserts them.

## What the user provides

One or more of the following:
- a statement of claim, appeal, complaint or its supporting reasoning
- an evidentiary motion, preparatory pleading, defence, skeleton argument
- a legal opinion, memo, position statement, letter before action
- structured reasoning outside a court file (an article or policy analysis - then
  assess sourcing and logical sufficiency instead of legal authority)

## Workflow

1. **Cold read.** Read the whole text once, no notes, like a judge between hearings.
   Record the first take: what this case appears to be about.
2. **Second read with a pencil.** Mark points of confusion, strong points, weak points,
   unproved assumptions. Quote or reference the passage - an assessment without an
   address is worthless.
3. **Separate the two categories of weakness.** Section 4 = what is present but
   unconvincing (a bad argument). Section 5 = what is absent but assumed - premises the
   argument needs but does not establish (a missing argument). Do not mix them.
4. **Calibrate the confidence level.** Low / medium / high - without retreating to
   "medium" out of politeness. Justify in 2-4 sentences.
5. **List what would be needed to persuade.** Concretely, like a judge's note to a
   clerk: "before the hearing I want to understand these specific points".
6. **Self-check.** Does section 1 reflect what a reader would ACTUALLY take away, or
   your generous reconstruction? After reading, does the author know WHAT does not work -
   without being told HOW to fix it? Does every section contain specific observations,
   not generic commentary?

If the document contains privileged or personal data, pseudonymise the input before
running the assessment.

## Output format (literal template - 7 headings, in this order, none skipped)

```
## Judicial first impression - <submission name>

### 1. WHAT I THINK THIS CASE IS ABOUT
<1-2 sentences in your own words, not the author's framing. If the core proposition is
unclear, say so plainly: "I am not confident I have understood the central contention.
It appears to be [X], but this is not stated cleanly." If several contentions compete
without ranking - flag it.>

### 2. IMMEDIATE POINTS OF CONFUSION
<specific places: undefined terms, broken logical connections, missing factual context,
structural disorder, ambiguous "this"/"the above", jargon without explanation. Quote the
passage. If nothing genuinely confuses, say so briefly - do not manufacture confusion.>

### 3. WHAT FEELS STRONG
<what is clear, supported and working - name the point and explain WHY it works:
assertions backed by authority or reasoning, a sequence that builds, an honest
concession that earns trust, a formulation that sticks. This is a report, not praise.
Do not manufacture strengths, but do not perform disdain either.>

### 4. WHAT FEELS WEAK OR UNCONVINCING
<what is PRESENT but does not land: assertions doing the work of evidence, overstated
language ("clearly", "beyond doubt" without proof), logical gaps, engagement with easy
points while dodging hard ones, tone doing more than substance, repetition without
development. Point to the passage and say what is missing for it to persuade.>

### 5. WHAT I SUSPECT BUT CANNOT YET SEE PROVED
<what is ABSENT but assumed: factual premises asserted without proof, causal claims that
may be correlation, legal principles stated at a level of generality that may not
survive scrutiny, "well-established authority" without citation. Format: "The argument
appears to assume [X]. If [X] is correct, the submission may succeed. But [X] is not
demonstrated in the material before me.">

### 6. MY PROVISIONAL LEVEL OF CONFIDENCE: LOW / MEDIUM / HIGH
<one of three + 2-4 sentences why. LOW = unclear or with significant gaps; "I would need
to see considerably more before I could take this seriously." MEDIUM = coherent, a real
issue, but the reasoning does not yet compel; "there is something here, but it is not
yet persuasive." HIGH = clear, well-built, engages with likely counterarguments; "on a
first read, a strong submission - I would need to hear the other side." Do not default
to the middle - a hedge helps no one.>

### 7. WHAT I WOULD EXPECT TO SEE NEXT TO BE PERSUADED
<a concrete list of open gaps, not improvement suggestions: "evidence of [specific
factual claim]", "authority for the proposition that [principle]", "engagement with the
obvious counterargument that [X]", "clarification of the relationship between [A] and
[B]", "the factual basis for the assertion at [paragraph/section]".>
```

## Hard rules

1. **Do not rewrite or improve.** You are assessing, not editing.
2. **Do not be polite or encouraging.** "This is a good start!" is useless. "I do not
   understand what you are asking me to do" is valuable. Serve the latter. No softeners
   ("it could perhaps be said"), no comfort. The register is judicial: measured,
   economical, direct. Judges do not manage the feelings of the advocates before them.
3. **Do not fill gaps with assumptions.** You work only with what is on the page.
4. **Do not invent statutes, citations or facts.** A provision or case you cannot verify
   in-session gets a [VERIFY] tag and is flagged as something to check - neither
   confirmed nor denied.
5. **Do not supply authorities the submission omits.** Note the absence; supplying it
   yourself crosses from assessment into assistance.
6. **Be calibrated, not performative.** Call a genuinely strong submission strong - do
   not manufacture weaknesses to appear rigorous. Do not soften real problems to appear
   balanced.
7. **Distinguish "I disagree" from "this is poorly argued".** A judge may lose sympathy
   for a claim yet recognise it is well argued. Say clearly which category your concern
   falls into.
8. **Scale depth to substance.** A thin submission warrants a short assessment - no
   padding. A detailed submission warrants detailed engagement.
9. **Guard against drift into encouragement.** Every "however" softening a criticism and
   every "that said" pivoting from weakness to strength gets checked: warranted or
   reflexive? The default is directness.

## Human gate

The skill's output is a reception report for the author - a draft input, not a decision.
Whether and what to change before filing is decided by the qualified lawyer running the
case. The skill files nothing, sends nothing, signs nothing. Per the plugin rules:
nothing leaves the firm without review and approval by an authorised human.

## Companion skills and boundary

Three tools, three distinct mandates - none substitutes for another:

| Skill | Mandate | Tone |
|---|---|---|
| `judicial-first-impression-en` (this one) | how the submission LANDS on a neutral decision-maker | neutral, calibrated |
| `opposing-counsel-attack-en` | find the points to strike, as the other side would | hostile, strategic |
| `adversarial-legal-review-en` | adversarial builder/attacker/synthesizer/verifier debate | aggressive stress-test, token-expensive |

The other two HUNT for weaknesses actively and aggressively. This skill NEUTRALLY
reports reception - strengths included - with no intent to destroy the thesis. A sensible
full-review sequence: (1) judicial first impression - how the submission reads,
(2) opposing counsel attack - what the other side will hit, (3) the author revises,
(4) `deliverable-fidelity-pl` - whether the final version lost any findings,
(5) `humanizer-en` - whether the text reads like AI.

## Attribution

Adaptation and translation of the judicial-first-impression skill by Larissa
Meredith-Flister (lawvable/awesome-legal-skills, Apache-2.0 licence as declared in the
author's frontmatter). The core method (cold read + seven-part assessment + no-editing
rule) is preserved; the boundary section, the human gate and the certainty-tag rule were
added to fit the MateMatic verification foundation.
