---
name: prompt-pack-contract-negotiation-preparation-sboghossian
title: Contract Negotiation Preparation
description: Use when a lawyer or commercial team needs to prepare a structured negotiation brief from a contract before entering negotiations. Analyses the contract to identify clauses to renegotiate, red-line positions, clauses to protect, suggested alternative wording, and questions to put to the counterparty. Applicable to any contract type and any jurisdiction; includes MENA-specific negotiation traps around governing law, liquidated damages enforceability, and language of execution.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-contract-negotiation-preparation
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Contract Negotiation Preparation

A negotiation brief converts a contract from a document to be signed into a decision-making tool. It tells the lawyer and the commercial team exactly where to push, where to hold, and where to accept — before they enter a room or join a call with the counterparty.

## When to use this

- The client has received a draft contract from the counterparty and needs to prepare a structured response.
- A negotiation session is scheduled and the client team needs a clear brief on positions.
- In-house counsel is reviewing a standard-form contract and wants to identify the non-standard risks.
- A deal team is comparing their preferred positions against the counterparty's draft.
- Preparing for a negotiation in a MENA context where certain clause types (penalty/liquidated damages, choice of law, language) have non-obvious enforceability consequences.

## Required inputs

| Input | Why it matters | Sensible default |
|---|---|---|
| The contract text | This is the document being analyzed | User pastes or attaches the contract |
| Company name (the user's client) | The brief is written from one party's perspective | Ask the user |
| Party role (buyer / seller / licensor / licencee / etc.) | Determines which clauses favor or disfavor the user | Ask the user |
| Key commercial objectives | What the client most wants to protect or achieve | Ask the user: price certainty / liability cap / IP / timeline / etc. |
| Governing law and jurisdiction | Determines which clauses are enforceable and which are not | Ask the user; note from the contract if stated |

## Optional inputs

- The client's internal approval threshold (e.g., "we can agree liability caps up to X without board approval").
- Whether this is a standard-form contract where certain clauses are non-negotiable (e.g., bank facility terms, government contract standard terms).
- Priority ranking of issues (some clients want the brief ordered by commercial priority, not by contract structure).
- Whether prior dealings or precedent agreements with this counterparty exist.

## Negotiation brief structure

### Part A — Overview and context
- Contract type, parties, and proposed transaction.
- Brief summary of what the contract does.
- Overall assessment: is this contract broadly acceptable as drafted, moderately problematic, or significantly one-sided?
- Recommended negotiation posture: cooperative (minor issues) / firm (material imbalances) / adversarial (fundamental structural problems).

### Part B — Clauses to renegotiate

Present as a structured table:

| # | Clause | Current wording (summary) | Problem | Suggested revision | Priority |
|---|---|---|---|---|---|
| 1 | [Clause ref + title] | [What it currently says] | [Why it is problematic for the client] | [Specific alternative language or approach] | High / Medium / Low |

**Common high-priority clauses to examine in any commercial contract:**

1. **Liability cap and exclusions:** Is the cap proportionate to the contract value? Are consequential damages excluded? In MENA civil-law systems, limitation of liability clauses are enforceable but may be overridden by court assessment of "actual damage" in certain contexts; fraud and gross negligence cannot be excluded.

2. **Payment terms:** Are payment deadlines, currency, and late-payment interest specified? In UAE/KSA, interest on debt requires careful drafting to avoid Islamic finance (Sharia) considerations in onshore courts.

3. **Termination for convenience:** Does the counterparty have a broad unilateral right to terminate? Is any compensation due on termination for convenience?

4. **Change / variation clause:** Can the counterparty unilaterally change the scope? What is the process for pricing changes?

5. **IP ownership:** Who owns IP created under the contract? If unclear, default to the creator in most civil-law systems (and the commissioning party under UK work-for-hire in some circumstances). Express assignment is safest.

6. **Governing law and dispute resolution:** Is the chosen law neutral? Is the forum accessible? Arbitration is generally preferred for MENA commercial contracts due to ease of enforcement under the New York Convention.

7. **Force majeure:** Is the definition appropriate for the risk profile of this contract? Post-COVID, overly broad force majeure clauses have been tested. Check whether cure obligations and termination rights are balanced.

8. **Liquidated damages / penalties:** In UAE, KSA, and LB civil-law systems, courts have discretion to reduce penalties that are "excessive" or "unreasonable" (UAE Civil Code Article 390; Lebanese Code of Obligations Article 266). The clause may be enforceable but not at the stated amount.

9. **Representations and warranties:** Are any representations uncapped or survive closing indefinitely? Temporal and quantum caps are important.

10. **Assignment:** Can the counterparty assign their rights and obligations without consent? This matters where creditworthiness and identity are material.

### Part C — Clauses that should not be changed
Identify 3–7 clauses that are favorable to the client and should be protected against counterproposals:
- State the clause and why it is favorable.
- Flag the risk if the counterparty proposes an amendment.

### Part D — Questions to ask the counterparty
List specific questions that, depending on the answer, would affect the client's position:
- "What is your interpretation of Clause X? Does it apply to situation Y?"
- "Why is the liability cap set at [amount]?"
- "Can you confirm that [ambiguous provision] was intended to mean [interpretation A] rather than [interpretation B]?"
- "What is the basis for the [payment / deliverable / notice] timeline?"

These questions serve a dual purpose: they gather information and they put the counterparty on notice of the issues before formal exchange of comments.

### Part E — Red lines
Identify 2–5 positions from which the client will not move, regardless of counterparty pressure:
- State the red line clearly.
- State the walk-away consequence if the counterparty insists.

Red lines should be reserved for genuinely non-negotiable points — overuse dilutes credibility.

### Part F — Negotiation tips and sequence
- Recommend which issues to raise first (typically non-contentious housekeeping, then commercial issues, then key risk provisions).
- Flag any issues where the client's position depends on information not yet in the contract (e.g., confirming the counterparty's insurance position before finalizing the liability cap).
- Note any issues where the client has a strong BATNA (alternative) and can afford to hold firm.

## Jurisdictional negotiation traps

| Jurisdiction | Key traps |
|---|---|
| UAE (onshore) | Penalty clauses are court-reducible; Arabic language version may be required; courts may apply Sharia principles in interest-related provisions |
| UAE (DIFC / ADGM) | Full freedom of contract; English law concepts apply; courts will generally enforce agreed terms including penalty clauses |
| KSA | Islamic finance principles apply; conventional interest clauses are problematic; governing law clause selecting foreign law may not be recognized for in-Kingdom disputes |
| Lebanon | Force majeure was liberally applied by courts during 2019–2022 crisis; penalty clause reduction is at court's discretion |
| Egypt | Court discretion to reduce penalties under Civil Code; choice of foreign law may be overridden by mandatory Egyptian law provisions |
| OHADA | Standard OHADA Uniform Acts apply to commercial contracts; foreign-law choice permitted but OHADA mandatory provisions cannot be contracted out |

## Common mistakes

- Raising every possible issue — a brief that flags 50 clauses is unusable. Prioritize ruthlessly.
- Failing to include suggested alternative wording — "this clause is bad" is not actionable; "replace with X" is.
- Not identifying the clauses to protect — negotiators often inadvertently concede favorable positions they did not realize they had.
- Overlooking the dispute resolution clause — in a MENA context this is often more important than any substantive clause.
- Not preparing the questions section — catching the counterparty's assumptions early prevents wasted rounds of comments.

## Related skills

- [[prompt-pack-contract-risk-matrix]]
- [[prompt-pack-contract-playbook]]
- [[prompt-pack-contract-summary-for-executives]]
- [[prompt-pack-nda-mutual]]
- [[prompt-pack-case-assessment-memo]]
