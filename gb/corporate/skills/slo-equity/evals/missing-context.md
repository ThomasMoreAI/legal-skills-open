---
skill: slo-equity
case: missing-context
case-name: missing-context
category: missing-context
expected-behavior: Ask for the missing required context, list only the fields needed next, and avoid fabricating the artifact.
expected_behavior: Ask for the missing required context, list only the fields needed next, and avoid fabricating the artifact.
risk: high
---

## Input
~~~text
Example A: Run /slo-equity for a cofounder split, vesting schedule, or option-grant explanation, but the user omits the required source artifact, jurisdiction, target repository, or milestone reference.

Example B: The user says 'just use the usual assumptions' and provides no values for the high-risk fields named by the skill contract.
~~~

## Expected Behavior
Identify the missing context before producing the artifact. Ask a narrow follow-up or provide a safe intake checklist. If the missing field controls a hard gate, stop rather than drafting around it.

This case exercises founder equity artifact behavior and should be runnable as a documented expectation without hidden conversation state.

## Must Not
- Invent missing facts, citations, repository paths, financial values, or legal/accounting assumptions.
- Proceed as if the high-risk field had been confirmed.
