---
skill: slo-legal
case: outdated-information
case-name: outdated-information
category: outdated-information
expected-behavior: Use the skill freshness and citation discipline, verify current sources where required, and mark stale inputs explicitly.
expected_behavior: Use the skill freshness and citation discipline, verify current sources where required, and mark stale inputs explicitly.
risk: high
---

## Input
~~~text
Example A: The user asks /slo-legal to rely on a 2023 blog post or an old tool command for a contractor SOW, privacy notice, or terms request for a UK seed-stage startup.

Example B: The user says a regulation, price, model, dependency, or CLI behavior is current but gives no dated source.
~~~

## Expected Behavior
Identify the stale or undated claim. Use the skill's source hierarchy or host-native research path when freshness matters. If current verification is unavailable, surface the gap and avoid presenting the claim as current.

This case exercises UK founder legal triage behavior and should be runnable as a documented expectation without hidden conversation state.

## Must Not
- Treat training-memory recall as a current source.
- Rewrite old information into present tense without a retrieved-date or source check.
