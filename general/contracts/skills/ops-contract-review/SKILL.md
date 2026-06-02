---
name: ops-contract-review
title: Business Contract Review
description: Review business contracts for risk identification including liability clauses, IP ownership, termination terms, and payment conditions. Use this skill when the user needs a practical contract risk assessment for vendor agreements, partnership contracts, or service agreements — even if they say 'review this contract', 'what should I watch out for', 'is this agreement fair', or 'negotiate better terms'.
author: asgard-ai-platform
author_url: https://github.com/asgard-ai-platform/skills/tree/main/ops-contract-review
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Business Contract Review

## Framework

```
IRON LAW: Read the Entire Contract, Not Just the Commercial Terms

Price and scope are negotiated carefully. Liability, indemnification,
termination, and IP ownership are often accepted on autopilot.
These "back-of-contract" clauses are where the real risk lives.

A great price with unlimited liability is a terrible deal.
```

### Contract Review Checklist (Business Focus)

**1. Parties & Authority**
- Correct legal entity names (not a subsidiary you didn't intend to contract with)
- Signer has authority to bind the organization

**2. Scope & Deliverables**
- Clearly defined: what is included AND what is excluded
- Acceptance criteria: how do you determine delivery is satisfactory?
- Change order process: how are scope changes handled and priced?

**3. Payment Terms**
- Payment schedule: milestones, monthly, upon delivery
- Payment terms: net 30, net 60, upon receipt
- Late payment consequences
- Currency and exchange rate risk (for international contracts)

**4. Term & Termination**
- Contract duration: fixed term vs auto-renewal
- Termination for convenience: can either party exit? With what notice?
- Termination for cause: what constitutes a breach?
- Wind-down obligations: what happens after termination? Data return? Transition assistance?

**5. Liability & Indemnification**
- Liability cap: is there one? What's the amount? (ideally = contract value)
- Indemnification: who indemnifies whom? For what? Is it mutual or one-sided?
- Exclusions: consequential damages, lost profits — are they excluded?
- Insurance requirements: does either party need to carry insurance?

**6. Intellectual Property**
- Who owns work product created during the contract?
- Pre-existing IP: remains with original owner (ensure this is stated)
- License grants: what rights does each party get to use the other's IP?

**7. Confidentiality**
- Definition of confidential information (not too broad, not too narrow)
- Duration: how long after termination?
- Exceptions: publicly available info, independently developed, legally compelled

**8. Dispute Resolution**
- Governing law: which jurisdiction?
- Arbitration vs litigation: arbitration is faster and private, litigation is cheaper for small claims
- Venue: where are disputes heard?

### Risk Rating

| Risk Level | Characteristics | Action |
|-----------|----------------|--------|
| 🟢 Low | Market-standard terms, balanced obligations | Sign |
| 🟡 Medium | Some one-sided clauses, manageable risk | Negotiate specific clauses |
| 🔴 High | Unlimited liability, no exit, one-sided IP | Don't sign without major revisions |

## Output Format

```markdown
# Contract Review: {Agreement Type} with {Counterparty}

## Overview
- Type: {service/vendor/partnership/license}
- Value: {$X}
- Term: {duration}

## Risk Assessment
| Area | Risk | Issue | Recommendation |
|------|------|-------|---------------|
| Scope | 🟢/🟡/🔴 | {finding} | {action} |
| Payment | 🟢/🟡/🔴 | {finding} | {action} |
| Termination | 🟢/🟡/🔴 | {finding} | {action} |
| Liability | 🟢/🟡/🔴 | {finding} | {action} |
| IP | 🟢/🟡/🔴 | {finding} | {action} |
| Confidentiality | 🟢/🟡/🔴 | {finding} | {action} |

## Red Flags
1. {specific clause + why it's risky}

## Negotiation Priorities
1. {most important change to request}
2. {second priority}
3. {third priority}

## Overall Risk: 🟢/🟡/🔴
{Summary recommendation: sign / negotiate / reject}
```

## Gotchas

- **Auto-renewal without notice deadline**: Many contracts auto-renew unless you give 30-90 days' notice. Calendar the notice deadline immediately upon signing.
- **"Standard" contracts are NOT neutral**: The drafter's "standard" template protects the drafter. Everything is negotiable.
- **Verbal agreements are risky**: "They said they'd cover that" means nothing if it's not in the contract. If it's important, it must be written.
- **Force majeure scope**: Post-COVID, check what's included. Pandemic? Supply chain disruption? Government orders? Too narrow = no protection when you need it.
- **This is a business review, not legal advice**: For contracts with significant financial or legal exposure, have a licensed attorney review the final version.

## References

- For contract law fundamentals, see the law-contract skill
- For negotiation tactics, see the ops-negotiation skill
