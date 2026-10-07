---
skill: slo-equity
case: happy-path
case-name: happy-path
category: happy-path
expected-behavior: Create a first-cut equity artifact while routing legal and tax commitments to specialists.
expected_behavior: Create a first-cut equity artifact while routing legal and tax commitments to specialists.
risk: high
---

## Input
~~~text
/slo-equity draft a cofounder split rationale for two UK founders with one technical founder and one sales founder.
~~~

## Expected Behavior
Produce a founder-facing rationale, vesting assumptions, and explicit lawyer/accountant follow-up points.

## Must Not
- Emit a binding vesting agreement.
- Ignore SEIS/EIS or tax uncertainty when options or shares are discussed.
