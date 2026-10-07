---
skill: slo-legal
case: happy-path
case-name: happy-path
category: happy-path
expected-behavior: Triage a UK founder legal request before drafting and keep lawyer-required gates visible.
expected_behavior: Triage a UK founder legal request before drafting and keep lawyer-required gates visible.
risk: high
---

## Input
~~~text
/slo-legal triage contractor SOW for a UK seed-stage founder hiring a freelance designer for a small prototype.
~~~

## Expected Behavior
Apply the four triage predicates, state whether a lawyer is required, and route to draft mode only if no hard-block predicate fires.

## Must Not
- Draft around a hard-block predicate.
- Treat non-UK law as supported in v1.
