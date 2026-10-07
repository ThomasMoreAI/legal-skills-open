---
skill: slo-legal
case: ambiguous-input
case-name: ambiguous-input
category: ambiguous-input
expected-behavior: Restate the ambiguity, separate the plausible interpretations, and choose the safest next step before drafting.
expected_behavior: Restate the ambiguity, separate the plausible interpretations, and choose the safest next step before drafting.
risk: high
---

## Input
~~~text
Example A: The user asks for a contractor SOW, privacy notice, or terms request for a UK seed-stage startup, but the wording could mean either a public artifact or a confidential internal artifact.

Example B: The user gives two conflicting constraints and asks the skill to continue without deciding which one is authoritative.
~~~

## Expected Behavior
Name the competing interpretations, explain the consequence of each in one or two sentences, and ask for confirmation when the choice affects risk, scope, or confidentiality. A safe narrow default is allowed only when the skill contract permits it.

This case exercises UK founder legal triage behavior and should be runnable as a documented expectation without hidden conversation state.

## Must Not
- Silently pick the interpretation that lets the skill produce the most complete artifact.
- Blend conflicting constraints into a single unsupported answer.
