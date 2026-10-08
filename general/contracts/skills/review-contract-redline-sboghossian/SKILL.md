---
name: review-contract-redline-sboghossian
title: Contract Redline (Track Changes with Rationale)
description: 'Use when a lawyer or party needs a contract reviewed with proposed track-change-style edits and written rationale per change — covering clause-by-clause analysis, risk flagging, and negotiation strategy. Requires the user to specify which side they represent and their negotiating priorities. Produces an executive summary of top risks, section-by-section redlines with severity ratings (critical / negotiate / nice-to-have), missing clauses, fallback positions, and open questions. MENA-aware: flags MENA-specific enforceability traps (penalty clauses, governing-law, notarization, Shari''a-compliance, MENA mandatory employment rules).'
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/review/review-contract-redline
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Contract Redline (Track Changes with Rationale)

Clause-by-clause review of a contract with proposed redlines, written rationale per change, and negotiation strategy. The output is structured to be directly usable by a lawyer managing a negotiation: each proposed change is graded by severity so the lawyer knows which battles to fight.

## When to use this

- You have received a contract from a counterparty and need to identify risks and propose changes
- You are preparing a first draft for counterparty review and want to stress-test your own draft
- A client needs a plain-language explanation of what a contract requires of them, alongside the red flags
- You are advising on the negotiating position — what must change, what can be traded, what is acceptable

## Required inputs from user

| Input | Why it matters |
|-------|---------------|
| **Document content** | The contract to be reviewed (full text or attachment) — required |
| **Which side you represent** | Determines what constitutes a favorable vs unfavorable clause (buyer/seller, employer/employee, licensor/licensee, lender/borrower, etc.) |
| **Priorities** | Cost reduction / risk minimization / speed to close / IP protection — informs which battles to fight and which to concede |
| **Counterparty leverage** | Is this a take-it-or-leave-it form (bank standard, software EULA, landlord form)? Or is there real negotiating room? |
| **Jurisdiction context** | Which law governs? Which court/arbitration forum? Determines enforceability analysis |

If the user provides only the document without identifying their side or jurisdiction, ask before proceeding — an unanchored review creates risk.

## Output format

### 1. Executive summary

3–5 bullet points covering:
- **Top risks**: the most significant legal, financial, or operational exposures in the current draft
- **Top proposed changes**: the most important redlines (those marked Critical)
- **Deal-breaker positions**: clauses the user's side should not accept under any circumstances
- **Overall assessment**: is this contract market-standard, heavily skewed toward the counterparty, or balanced?

### 2. Section-by-section redlines

For each clause that needs change, produce:

```
### [Clause number] — [Clause heading]

**Current text**:
> [Verbatim current text of the clause, or the problematic portion]

**Proposed text**:
> [Revised text showing the change — additions in bold or marked, deletions struck through in plain text notation]

**Rationale**: [1–2 sentences explaining why this change is needed and what risk it addresses]

**Severity**: 🔴 Critical (must change) / 🟡 Negotiate (important but tradeable) / 🟢 Nice-to-have

**Fallback position**: [If the ideal text is rejected, what is the minimum acceptable formulation?]
```

**Severity definitions**:
- 🔴 **Critical**: the current text creates a material legal, financial, or regulatory risk that cannot be left unaddressed. Examples: unlimited liability; automatic renewal with no termination right; IP assignment that strips all rights; governing law clause that would render arbitration unenforceable.
- 🟡 **Negotiate**: the current text is unfavorable but not fatal. Worth pushing; be prepared to trade against something the counterparty wants. Examples: notice periods; payment terms; representation scope; audit rights.
- 🟢 **Nice-to-have**: minor clarifications or standard protective language that would improve the contract but whose absence creates no significant risk.

**Do not redline boilerplate just because it is not in your preferred form.** Fights cost goodwill. Only propose changes that matter.

### 3. Missing clauses

List important clauses absent from the document. For each:
- Clause type (limitation of liability, indemnification, IP ownership, force majeure, termination for convenience, confidentiality, governing law, dispute resolution, data protection, etc.)
- Why it matters for the user's position
- Suggested insertion (or note that the user's position is better without it)

### 4. Open questions

Items requiring further input from the user, the counterparty, or legal counsel before the redline can be completed:
- Factual matters unclear from the document ("what is the intended delivery date?")
- Business terms not yet agreed ("what is the agreed price?")
- Jurisdiction-specific issues requiring qualified local advice

## Heuristics for redline quality

### Fight the right battles
Every proposed change costs negotiating capital. Prioritize:
1. Liability cap and indemnification — this is where the most financial value is at risk
2. IP ownership and licensing scope — permanent and very difficult to unwind post-signing
3. Termination rights — inability to exit a bad contract is a long-term operational risk
4. Dispute resolution mechanism — choice of forum and governing law determines enforceability
5. Representations and warranties — scope and duration of seller's/provider's liability

Do not burn capital on:
- Cosmetic grammar or formatting changes
- Standard boilerplate that is accepted market practice
- Minor notice provisions unless they actually create a risk

### Side-aware analysis
- **Buyer / client / licensee**: focus on liability caps, IP scope, service level commitments, exit rights, and limitation of representations
- **Seller / provider / licensor**: focus on payment terms, exclusions from liability, IP ownership, customer data handling, and limitation of warranties
- **Employer**: focus on IP assignment scope, non-compete enforceability, confidentiality, and termination grounds
- **Employee**: focus on compensation clarity, EOSB compliance (MENA), non-compete proportionality, notice periods, and benefit terms

For employment-specific review, see [[review-employment-contract-employee-side]] or [[review-employment-contract-employer-side]].

## MENA enforceability flags

Always check for these traps when the governing law is MENA:

### UAE (onshore)
- **Penalty clauses**: UAE Civil Transactions Law allows courts to adjust contractual penalties to actual damage, even if the parties agreed otherwise (Article 390). A penalty clause that departs significantly from actual loss may be reduced by a court.
- **Notarization / Tawqi3i**: certain contracts (employment contracts, real estate, power of attorney) must be notarized in the UAE to be enforceable. An un-notarized employment contract may not be valid.
- **Governing law**: for employment contracts, UAE Labor Law (FDL 33/2021) applies as mandatory law regardless of chosen governing law, if the employee works in UAE.
- **Witness requirements**: some contracts under Islamic influence may require witnesses.

### KSA
- **Interest (riba)**: interest-bearing provisions in contracts governed by Saudi law are not enforceable under Sharia principles. Restructure as service fees, murabaha, or other Sharia-compliant instruments.
- **Exclusion of Sharia**: choice-of-law clauses purporting to exclude Sharia entirely will not be honored by Saudi courts.
- **Non-compete duration**: maximum 2 years under Labor Law; courts may reduce scope-heavy restrictions.

### DIFC / ADGM
- Generally enforcement-friendly common-law environment; most commercial clauses are enforceable as written. Flag:
  - Penalty clauses: the "penalty rule" applies (unenforceable if a genuine pre-estimate of loss is absent) but DIFC courts have narrowed this following UK Supreme Court authority.
  - Exclusion clauses: tested against reasonableness under DIFC Contract Law.

### Lebanon
- Contracts under Lebanese law are generally enforced as written; however, the practical ability to enforce through Lebanese courts is severely compromised post-2019.
- Arbitration clauses (LCIA, ICC) with a non-Lebanese seat are strongly recommended for high-value Lebanon-nexus contracts.

### Cross-border governing law
- Review [[review-governing-law-conflict]] when the contract has parties or performance in multiple jurisdictions — the chosen governing law may not respect mandatory rules of the jurisdiction of performance.

## Word plugin surface

When the user is in the Word plugin, redline output must be track-change-compatible:
- No markdown bullet characters
- Changes marked as: `~~deleted text~~` for deletions; `**inserted text**` for insertions
- Each redline followed by a bracketed rationale: `[Rationale: ...]`

## Related skills

- [[review-definitions-consistency]]
- [[review-cross-reference-integrity]]
- [[review-governing-law-conflict]]
- [[review-dispute-resolution-mechanism-fit]]
- [[review-employment-contract-employee-side]]
- [[review-employment-contract-employer-side]]
