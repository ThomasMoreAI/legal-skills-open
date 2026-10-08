---
name: prompt-pack-contract-risk-matrix-sboghossian
title: Contract Risk Matrix
description: Use when a lawyer needs to review a contract and produce a structured risk matrix categorising each clause by risk level (low/medium/high/critical), with clause reference, risk description, potential impact, likelihood, and recommended mitigation. The output is a decision-support tool for clients and deal teams. Applicable to all contract types and jurisdictions; MENA-aware for UAE, KSA, LB, EG, DIFC/ADGM enforcement realities.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-contract-risk-matrix
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Contract Risk Matrix

A contract risk matrix is the most efficient way to communicate contract risk to a client or deal team that cannot read the full document. It surfaces what matters, in order of severity, with enough context to make a decision. A good matrix is used; a poor one is filed and ignored.

## When to use this

- A client has received a counterparty draft and wants to know the risks before negotiating.
- The deal team needs a one-page risk overview for a senior approval meeting.
- In-house counsel is reviewing a high-volume contract type and wants a consistent risk-scoring methodology.
- Pre-signing, to confirm that all high/critical risks have been mitigated or accepted by the appropriate authority.
- Post-contract, during execution, to monitor which risk clauses are most likely to become live issues.

## Required inputs

| Input | Why it matters | Sensible default |
|---|---|---|
| Contract text | The document to be reviewed | User attaches or pastes the contract |
| Reviewing party name and role | Risk is always assessed from one party's perspective | Ask the user |
| Contract type and commercial context | Shapes which clauses are most important and the baseline risk tolerance | Ask the user |
| Jurisdiction and governing law | Affects enforceability of key provisions | Ask the user; note from contract if stated |

## Optional inputs

- Risk scoring methodology preference (standard low/medium/high/critical or numerical 1–5).
- Specific clauses of particular concern to the client (to prioritize).
- Whether the matrix should include recommended red-line wording.
- Whether the output will be shared with non-lawyers (affects technical depth).

## Review methodology

### Step 1 — Read the contract in full
Before scoring, read the entire contract to understand the commercial structure, identify interdependencies between clauses, and detect any unusual or non-standard provisions.

### Step 2 — Identify all material clauses
For a standard commercial contract, material clauses include at minimum:
- Payment terms and financial provisions
- Liability cap and exclusions
- Indemnification
- Representations and warranties (and survival)
- Termination rights (for cause and for convenience)
- IP ownership and assignment
- Confidentiality
- Governing law and dispute resolution
- Force majeure
- Assignment and change of control
- Data protection and security
- Regulatory compliance
- Non-compete / non-solicitation (if present)
- Liquidated damages / penalties (if present)
- Audit rights

### Step 3 — Score each clause

**Risk levels:**

| Level | Definition | Typical action |
|---|---|---|
| **Critical** | Clause creates a fundamental exposure — unlimited liability, one-sided termination with no remedy, loss of core IP, or an unenforceable obligation on the reviewing party | Do not sign without resolving; escalate immediately |
| **High** | Significant legal or commercial exposure that materially affects the value or risk profile of the deal | Negotiate before signing; document if accepted |
| **Medium** | Clause is unfavorable but manageable; risk is bounded or mitigatable in practice | Attempt to negotiate; if unsuccessful, flag to business with mitigation steps |
| **Low** | Clause is standard or mildly unfavorable; risk is negligible relative to the deal | Accept; no action required |

**Scoring factors:**
- **Impact:** What is the worst-case financial / legal / reputational consequence if this clause is triggered?
- **Likelihood:** How probable is the triggering scenario given the nature of the contract and counterparty?
- **Controllability:** Can the reviewing party mitigate this risk operationally (e.g., by performance practices) even if the contract cannot be changed?

### Step 4 — Draft the matrix

Format the risk matrix as a table:

| # | Clause ref | Clause title | Risk description | Impact | Likelihood | Risk level | Recommended mitigation |
|---|---|---|---|---|---|---|---|
| 1 | Clause 12 | Liability cap | Cap is set at 50% of one month's fees — grossly inadequate given 24-month contract value | Critical | High if breach | Critical | Renegotiate cap to at least 12 months' fees; add carve-outs for IP and data breaches |
| 2 | Clause 8.3 | Termination for convenience | Counterparty can terminate on 7 days' notice; reviewing party requires 60 days' notice | High | Medium | High | Seek symmetrical notice periods or compensation for early termination |
| ... | ... | ... | ... | ... | ... | ... | ... |

### Step 5 — Executive summary
Add a brief (half-page maximum) executive summary above the matrix:
- Number of Critical / High / Medium / Low risks identified.
- The 2–3 most important risks in plain language.
- Overall deal recommendation: acceptable as drafted / negotiate before signing / do not sign until key issues resolved.
- Any showstoppers that require board or senior sign-off.

## Risk categories and common patterns

**Financial risk clauses:**
- Uncapped liability or unlimited indemnification
- Payment terms that do not match cash-flow requirements
- Price escalation clauses that are one-sided
- Currency risk exposure with no hedging provision

**Operational risk clauses:**
- Service level obligations with punitive penalties
- Delivery obligations the client cannot meet without specific counterparty cooperation
- Acceptance testing provisions that are subjective

**Legal / regulatory risk clauses:**
- Choice of law that is hostile or uncertain (e.g., KSA or LB law chosen for a MENA deal where the reviewing party has no local counsel)
- Arbitration clauses with an inconvenient seat or expensive institution
- Representations that are wider than the party can honestly make
- Mandatory regulatory compliance clauses that require actions outside the party's control

**IP risk clauses:**
- Broad IP assignment to the counterparty of all work product and pre-existing IP
- No IP warranty from the counterparty (IP infringement by the counterparty becomes the reviewing party's problem)
- License back provisions that are narrower than the business needs

**Relationship risk clauses:**
- Exclusivity obligations that prevent the reviewing party from working with competitors
- Non-solicitation of employees that is broader than needed
- Publicity and press release rights given to the counterparty without approval

## Jurisdictional calibration notes

| Jurisdiction | Risk calibration adjustments |
|---|---|
| UAE (onshore) | Liquidated damages clauses: courts may reduce to actual damage (Civil Code Art. 390) — mark as "uncertain enforcement" rather than "critical risk removed." Interest clauses: may be unenforceable in full at interest rates above the legal limit. Arabic language version governs if Arabic and English versions conflict. |
| UAE (DIFC / ADGM) | Full freedom of contract; penalty clauses enforceable; English law concepts apply. Courts are experienced and efficient. |
| KSA | Choice-of-law selecting foreign law may not be enforced for in-Kingdom disputes. Zakat and withholding tax implications of payment structures. Dispute resolution through commercial courts (Riyadh) or Saudi arbitration preferred. |
| Lebanon | Penalty clause reduction at court's discretion. Force majeure interpreted liberally since 2019 economic crisis. Enforcement of foreign judgments requires exequatur. |
| Egypt | Courts can reduce penalties. Dispute resolution: Egyptian law arbitration (CRCICA) preferred for enforcement. |

## Output format

Deliver:
1. **Executive summary** (half page, in plain language).
2. **Risk matrix table** (all material clauses scored).
3. **Critical and high risks detail sheet** (one paragraph per Critical/High risk explaining the issue and the recommended redline or mitigation in more detail).
4. **Suggested redlines** (optional — for each Critical and High risk, the specific contract language change recommended).

## Limits

- A risk matrix is not a substitute for full contract review advice. It is a structured summary of the review.
- Risk scoring is inherently subjective; the matrix should state the reviewer's assumptions.
- A matrix produced before commercial context is provided may mis-score risks that are normal in a particular industry or relationship type.
- For regulated contracts (DFSA/ADGM Financial Services contracts, RERA property contracts), specialized regulatory review is required alongside the risk matrix.

## Related skills

- [[prompt-pack-contract-negotiation-preparation]]
- [[prompt-pack-contract-playbook]]
- [[prompt-pack-contract-summary-for-executives]]
- [[prompt-pack-case-assessment-memo]]
- [[prompt-pack-due-diligence-checklist]]
