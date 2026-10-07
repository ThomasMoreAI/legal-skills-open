---
name: output-scoring-en-matematicsolutions
title: Output scoring - a scorecard before you send
description: 'Scores the quality of an AI legal output before it goes out, in two layers: objective (mechanically checkable - do the citations exist, are the provisions and dockets real) and subjective (LLM-as-judge on a 1-5 rubric: legal correctness, completeness, clarity, jurisdiction fit, grounding/anti-hallucination). Returns a scorecard and a decision: send / revise / full verification. A layer above the deliverable - it does not write, it scores. Jurisdiction-neutral. Pairs with reviewer-en, adversarial-legal-review-en and legal-syllogism-en. Use when: "score this output", "is this ready to send", "quality of this legal answer", "scorecard for the deliverable", "rubric check" - before sending an opinion, memo, or brief.'
author: matematicsolutions
author_url: https://github.com/matematicsolutions/awesome-matematic-skills-en/tree/main/verification-foundation/skills/output-scoring-en
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Output scoring - a scorecard before you send

## Philosophy

**Before you send it, score it - and keep what is checkable apart from what must be judged.** An AI
output can read smoothly and still be wrong. This skill scores it in two layers: objective (facts you
can verify mechanically) and subjective (quality you have to judge against an explicit rubric).
Mixing the two is where false confidence comes from - "sounds right" is not "the citations check out".

It **scores**; it does not write or send. The decision is the lawyer's; the scorecard is the basis.

## Layer 1 - objective (mechanically checkable)

Delegate, do not guess:
- **Citations and provisions** - do they exist in the source verbatim; were they all caught.
- **Dockets / identifiers** - real and correctly written.
- **Completeness** - did any RED finding drop out of the summary.

The objective result is binary per item: matches / does not. Even one mismatched citation means the
output is not ready, whatever the subjective score.

## Layer 2 - subjective (1-5 rubric, LLM-as-judge)

Score each dimension 1-5 with a one-sentence reason:

| Dimension | 1 | 5 |
|---|---|---|
| Legal correctness | thesis wrong or unsupported | thesis sound and grounded in the rule |
| Completeness | omits material issues | covers everything material to the question |
| Clarity | muddled, inconsistent | precise, readable for the reader |
| Jurisdiction fit | confuses systems/rules | correct for the governing law |
| Grounding (anti-hallucination) | claims with no basis | every claim has a basis |

### UNCERTAIN instead of a number - a first-class score

When the judge has no basis for a number, it does not invent one. Instead of a forced 3 it
writes **UNCERTAIN**, with a subcategory and a note on what evidence is missing:

- **INSUFFICIENT_EVIDENCE** - the score cannot be given without material that is not in the
  session (the judgment the output relies on, the contract it refers to). Write down WHAT is
  missing and where to get it.
- **SOURCE_AMBIGUOUS** - the material is there but does not settle the point (an ambiguous
  clause, conflicting passages, a question that admits two readings). Write down WHERE the
  ambiguity sits.

Hard rules:
- UNCERTAIN does not enter the average and must never be quietly turned into a 3. A forced
  middle score is exactly the silence about uncertainty this skill exists to catch.
- UNCERTAIN in Legal correctness or Grounding -> decision capped at **Full verification**.
- UNCERTAIN in any other dimension -> decision capped at **Revise**.

"AI that knows what it does not know" as a field on the scorecard, not a claim about it.

## Decision

- **Send** - Layer 1 clean, no UNCERTAIN, subjective average >= 4, no dimension < 3.
- **Revise** - Layer 1 clean but a dimension scores 2-3 (name it), or UNCERTAIN outside
  the critical dimensions.
- **Full verification** - Layer 1 has a mismatch, a dimension = 1, or UNCERTAIN in Legal
  correctness / Grounding -> route to grounding / adversarial review.

## Re-scoring - monotonicity and anchors

A score card is often issued twice: once on the first pass, once after revisions. The second
pass is where scores quietly rise, because the author now knows the charges and can argue
around them. Two hard rules.

**Monotonicity.** A re-score may lower the decision at any time, for any reason. Raising it
requires **new evidence**, not new argument. New evidence means Layer 1 re-run with a
different result, or material that was not in the session before (the judgment finally
supplied, the contract finally attached). "On reflection this is good enough" is not
evidence and does not move the score.

**Anchors.** While any of the following is open, the decision cannot rise above **Full
verification**, whatever the subjective average says:

- a citation, provision or docket number that does not match the source in Layer 1,
- a RED finding dropped from the summary,
- UNCERTAIN in Legal correctness or Grounding.

Only re-running the tool that set an anchor can clear it. A judge's opinion cannot. Same rule
`agentic-risk-asi-pl` applies to finding severity: direct evidence is not negotiable.

Record every blocked attempt to raise the score. Seeing who tried to move the verdict, and on
what argument, is often worth more than the verdict.

## Output format

```
LAYER 1 (objective): citations OK/X | provisions OK/X | dockets OK/X | completeness OK/X
LAYER 2 (1-5 rubric):
  Legal correctness: 4 - <reason>
  Completeness: 3 - <...>
  Clarity: 5 - <...>
  Jurisdiction fit: UNCERTAIN (INSUFFICIENT_EVIDENCE) - the output rests on a judgment whose
    text is not in the session; missing: the reasoning as handed down
  Grounding: 4 - <...>
  Average: 4.0 (from 4 numeric dimensions; UNCERTAIN outside the average)
ANCHORS: none (or: citation [2019] UKSC 12 unmatched - decision capped at Full verification)
DECISION: Revise (Completeness 3 - limitation period not addressed)
```

On a re-score, add one line:

```
RE-SCORE #2: Revise -> Revise. Raise to Send rejected: argument only, Layer 1 not re-run.
```

## Limits

- The subjective score is the model's judgement against a rubric, not an oracle - at high stakes the
  final call is the lawyer's, and the scorecard is evidence of due diligence.
- Layer 1 does not replace the tools it calls - it aggregates them into one decision.
- It scores the output; it does not create or fix it.

## Attribution

Two-layer method (objective matching + a subjective LLM-as-judge rubric on a 1-5 scale) based on
**DISC-Law-Eval** from DISC-LawLLM (Fudan DISC Lab), Apache-2.0. Exam data and judge model dropped;
rubric dimensions, thresholds and framing are MateMatic's own. MateMatic interpretation, not the
position of any bar or regulator.

<!-- shared-rules:begin (generated from ../../SHARED-RULES.md by scripts/shared-rules-sync.py - do not edit here) -->
## Shared rules of the verification-foundation plugin

These rules apply to every skill in this plugin, including where the skill itself is silent. They are copied into each skill, so they hold whether you install the whole plugin or a single skill.

### Five layers of protection (before any disclaimer)

1. **Source verification** - provisions and case law from databases, not the model's memory.
2. **Confidence class** - every legal claim marked: verified / check / do not use.
3. **Premise check** - facts from the user are tested before analysis.
4. **Explicit negative scope** - each skill states what it does NOT do.
5. **Human gate** - a qualified person reviews and approves the output.

If an error would pass without being stopped by layers 1-5, the fault is in the skill. Fix the tool, do not add a note. "This is not legal advice" stops no error and transfers no responsibility.

### Confidence tags

- **Verified** - source checked in this session, with a full identifier: `(GDPR Art. 6)`, `(Case C-311/18, CJEU)`.
- **Check** - plausible, unverified: `[check on EUR-Lex]`.
- **Do not use** - an invented case number or provision. Omit it, never fabricate.

The tag sits next to the line it concerns. A case number that exists is not enough - check the content.

### Human gate

Nothing is sent, filed, signed or published before a qualified person checks and approves it. A skill output is a draft, not a finished document.

### Scope

The verification foundation is jurisdiction-neutral - the method, not the substance of any one legal system. It connects to no external source (no MCP connectors) and makes no outbound calls of its own; what you type still goes to your configured model (see https://github.com/matematicsolutions/awesome-matematic-skills-en/blob/main/TRUST.md). Substance comes from separate plugins (eu-law-sources). Deep national law (e.g. Polish case law) lives in the Polish marketplace, by design.
<!-- shared-rules:end -->
