---
name: legal-risks-everyone-needs-a-copilot
title: Legal Risk Analysis Skill
description: Financial exposure analysis for contracts. Use for risk registers, severity and probability analysis, worst-case exposure, cumulative exposure, and prioritized mitigation recommendations.
author: Everyone-Needs-A-Copilot
author_url: https://github.com/Everyone-Needs-A-Copilot/codex-copilot/tree/main/packs/writing-legal/skills/legal-risks
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: contracts
language: en
---

# Legal Risk Analysis Skill

A contract is a set of contingent financial obligations. Risk analysis answers: what could go wrong, how likely is it, and how much would it cost? That is the information you need to decide whether to sign, negotiate, or walk away.

---

## Risk Severity Levels

| Level | Definition | Response |
|-------|-----------|----------|
| **Critical** | Could threaten firm viability or exceed total contract value | Walk-away unless resolved |
| **High** | Significant financial exposure (>50% of contract value) | Must negotiate before signing |
| **Medium** | Meaningful exposure (10-50% of contract value) | Negotiate; accept with mitigation if not resolved |
| **Low** | Limited exposure (<10% of contract value) | Track; accept risk if not negotiable |

---

## Risk Analysis Framework

For each identified risk:

1. **Risk name**: Short, specific label (e.g., "Unlimited indemnification for third-party claims")
2. **Clause reference**: Section number in the contract
3. **Severity**: Critical / High / Medium / Low
4. **Probability**: What is the realistic likelihood this risk materializes? (High / Medium / Low)
5. **Financial exposure**: Worst-case dollar estimate. Use contract value as the baseline.
6. **Trigger conditions**: What specific events would cause this risk to materialize?
7. **Mitigation**: What would reduce this risk to acceptable levels?

---

## Financial Exposure Estimation

Use these benchmarks relative to contract value (CV):

| Risk Type | Typical Worst-Case Exposure |
|-----------|----------------------------|
| Unlimited indemnification | Theoretically unlimited; model as 3-10x CV |
| IP assignment (methodology lost) | Hard to quantify; treat as Critical: revenue at risk from all future engagements using this methodology |
| No termination for convenience payment | Lost revenue: estimated % of contract remaining at time of T4C |
| Payment terms missing | Delayed revenue: cash flow impact plus collection cost |
| No liability cap | Default to unlimited; model as 3-5x CV |
| CORA disclosure of trade secrets | Revenue at risk if competitors access methodology |
| Misclassified contractor | Back taxes, penalties: typically 25-40% of wages paid |
| No acceptance criteria | Scope creep cost: 20-50% of contract value (industry average) |
| Annual certification missed (perjury level) | Criminal and civil exposure; escalate to human counsel |

---

## Risk Categories

Analyze every contract across these categories:

### Financial Risk
- Payment terms: When does money flow in?
- Liability caps: What is the ceiling on exposure?
- Indemnification obligations: What must ENAC pay if something goes wrong?
- Fee adjustments: Can the client reduce fees after contract execution?

### Operational Risk
- Scope creep: Can the client expand scope without a change order?
- Termination: How easily can the client exit the contract, and what does ENAC receive?
- Acceptance: Can the client refuse deliverables and withhold payment?
- Subcontractor flow-down: Does ENAC bear liability for subcontractor failures?

### Intellectual Property Risk
- Methodology transfer: Does ENAC lose ownership of its methodology?
- Trade secret exposure: Can ENAC's confidential information be disclosed?
- Derivative IP: Who owns improvements to ENAC's tools discovered during the engagement?

### Compliance Risk
- Certification obligations: What must ENAC certify, and what are the penalties for error?
- Accessibility obligations: Are WCAG requirements feasible within the budget?
- Data handling: What are the consequences of a data breach or PII mishandling?
- AI Act obligations: Is there exposure for undisclosed or non-compliant AI use?

### Relationship Risk
- Termination for cause: How easily can the client terminate for cause and under what standards?
- Dispute resolution: What is the cost and timeline of resolving a dispute?
- Reputational: Does the contract create obligations that could embarrass ENAC if disclosed via CORA?

---

## Cumulative Risk Profile

After analyzing individual risks, calculate the cumulative exposure:

1. **Expected value:** Sum of (probability × worst-case exposure) for all identified risks
2. **Tail risk:** Sum of worst-case exposure for Critical and High risks only
3. **Risk-adjusted contract value:** Contract value minus expected loss value

If tail risk exceeds contract value: this contract should not be signed as-is.

---

## Output Structure

1. **Critical Risks**: Numbered list, each with: clause, severity, probability, financial exposure, trigger, required mitigation
2. **High Risks**: Same format
3. **Medium Risks**: Same format
4. **Low Risks**: Summary only
5. **Cumulative Risk Profile**: Expected value, tail risk, risk-adjusted contract value
6. **Recommendation**: Sign / Negotiate specific items / Walk away

---

## Anti-Generic Rules

- NEVER present risk as "possible" without estimating probability
- NEVER omit financial exposure estimates: force a range if uncertain
- NEVER let IP assignment risk fall below Critical without confirming a Background IP carve-out exists
- NEVER calculate cumulative risk without including IP risk even if it is hard to quantify
- NEVER recommend signing a contract with tail risk exceeding contract value without human counsel review
