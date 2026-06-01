---
name: fp-check
title: False Positive Check — MANDATORY Pre-Submission Verification
description: Systematic false positive elimination for security findings. 6-gate verification, 13-item checklist, devil's advocate questioning. MANDATORY before any CVE submission.
author: ByamB4
author_url: https://github.com/ByamB4/find-cve-agent/tree/main/skills/fp-check
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# False Positive Check — MANDATORY Pre-Submission Verification

## When to Use

Before ANY finding is submitted. No exceptions. This is the final gate.

## When NOT to Use

- Finding or hunting for bugs (use Hunter workflow instead)
- General code review for style/performance
- Feature development or non-security tasks

## Rationalizations to Reject

| Rationalization | Why It Is Wrong | Action |
|---|---|---|
| "This pattern looks dangerous" | Pattern recognition is not analysis | Trace actual data flow |
| "Similar code was vulnerable elsewhere" | Each context differs | Verify this specific instance |
| "This is clearly critical" | LLMs are biased toward seeing bugs | Complete devil's advocate |
| "Skipping verification for efficiency" | No partial analysis allowed | Run all gates |

## Step 0: Restate the Claim

Restate the vulnerability in one precise sentence. If you cannot, it's likely false.

- **What**: exact vulnerability type and root cause
- **Where**: file:line of the sink
- **How**: data flow from attacker input to sink
- **Impact**: concrete security consequence
- **Who**: attacker privilege level required
- **Bug class**: consult references/bug-class-verification.md

Half of false positives collapse at this step — the claim doesn't make coherent sense.

## Route: Standard vs Deep

**Standard** — clear claim, single component, well-understood bug class, no concurrency.
**Deep** — ambiguous claim, cross-component flow, race conditions, logic bugs, or standard was inconclusive.

Start with Standard. It has built-in escalation checkpoints.

## 6-Gate Review — ALL Must Pass

### Gate 1: Process Completeness
- [ ] Source identified (where attacker input enters)
- [ ] Sink identified (where dangerous operation occurs)
- [ ] Complete data flow traced source to sink
- [ ] All transformations/validations documented

### Gate 2: Reachability
- [ ] Attacker can reach the vulnerable endpoint
- [ ] Attacker controls the data that reaches the sink
- [ ] No auth barrier blocks access (or bypass is part of finding)
- [ ] Input is not sanitized before reaching sink

### Gate 3: Real Impact
- [ ] Exploitation produces real security consequences
- [ ] Impact exceeds what attacker could already do at their privilege level
- [ ] Behavior is NOT documented/intended design
- [ ] Impact manifests in observable behavior

### Gate 4: PoC Validation
- [ ] PoC runs successfully against latest version
- [ ] PoC succeeds 3/3 times (fail 3x = FALSE POSITIVE, no exceptions)
- [ ] Evidence matches claimed impact exactly
- [ ] Default configuration only

### Gate 5: Math / Bounds
- [ ] For DoS: growth rate is actually exponential/quadratic (not linear)
- [ ] For overflow: values actually exceed the boundary
- [ ] For ReDoS: backtracking is catastrophic (>1s for reasonable input)
- [ ] For bombs: expansion ratio is dangerous (>100x)

### Gate 6: Environment
- [ ] Runtime does NOT block this at a lower level
- [ ] Framework middleware does NOT sanitize automatically
- [ ] OS-level protections do NOT prevent exploitation
- [ ] Default security headers do NOT mitigate

## 13-Item False Positive Checklist

| # | Check | If YES |
|---|-------|--------|
| 1 | README warns against untrusted input? | Gray area — document it |
| 2 | Documented/intended behavior? | FALSE POSITIVE |
| 3 | Library handles this gracefully? | FALSE POSITIVE |
| 4 | Alpha/beta/pre-release? | Unlikely to get CVE |
| 5 | JSON.parse does the same? | Show REAL crash beyond JSON.parse |
| 6 | OOM crash or caught RangeError? | RangeError = lower severity |
| 7 | Requires admin privileges? | Check if access is genuinely new |
| 8 | Exact version already patched? | DUPLICATE |
| 9 | Framework sanitizes at middleware? | FALSE POSITIVE |
| 10 | Runtime blocks this? | FALSE POSITIVE |
| 11 | >10 prior CVEs on this project? | Over-audited — proceed with caution |
| 12 | Different package with similar name? | Verify exact package |
| 13 | Only works with non-default config? | Severity drops significantly |

## Devil's Advocate — 7 Questions

1. Am I seeing a vulnerability because the pattern "looks dangerous"?
2. Am I incorrectly assuming attacker control over trusted data?
3. **Am I hallucinating this?** LLMs are biased toward seeing bugs everywhere.
4. Am I dismissing complexity that makes exploitation impractical?
5. Am I inventing mitigations I haven't verified in source code?
6. Am I conflating "unsafe-looking code" with "exploitable vulnerability"?
7. Would a senior security researcher at Trail of Bits agree this is real?

## Verdict Format

```
VERDICT: TRUE POSITIVE / FALSE POSITIVE / NEEDS MORE INFO

Gates passed: X/6
Checklist flags: [list any concerns]
Devil's advocate: [key doubt and resolution]
Evidence: [concrete proof]
Confidence: HIGH / MEDIUM / LOW
```

## References

- [Standard Verification](references/standard-verification.md)
- [Deep Verification](references/deep-verification.md)
- [Gate Reviews](references/gate-reviews.md)
- [Bug-Class Verification](references/bug-class-verification.md)
- [False Positive Patterns](references/false-positive-patterns.md)
- [Evidence Templates](references/evidence-templates.md)
