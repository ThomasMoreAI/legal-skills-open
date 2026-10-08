---
name: prompt-pack-full-contract-risk-review-sboghossian
title: Full Contract Risk Review
description: Use when reviewing a commercial contract to identify legal risks, unclear clauses, missing protections, and terms that expose a named company to financial or legal liability. Produces a structured report with sections for high-risk clauses, ambiguous language, missing protections, one-sided provisions, and suggested revisions. Applicable to any commercial contract type across all jurisdictions. Trigger when a company or its counsel needs a systematic risk review before signing any significant agreement.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-full-contract-risk-review
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Full Contract Risk Review

## When to use this

Use this skill when a company needs a systematic, end-to-end legal risk review of a commercial contract before signing. This is a general-purpose review framework that applies to any contract type — supply agreements, service agreements, technology contracts, commercial leases, partnership agreements, and more.

The review is conducted from the perspective of the named company (the client) and produces a structured output that legal counsel or a business team can act on directly.

Typical triggers:
- Legal counsel reviewing a counterparty's draft contract before negotiation
- Business team member who has received a contract and needs a legal risk assessment
- Post-negotiation final check before signing
- Contract audit as part of M&A due diligence
- Annual contract portfolio review to flag contracts approaching renewal or with unusual terms

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| Contract text (full) | The document to be reviewed | Must be provided |
| Company name (the reviewing party) | Determines whose interests the review protects | Ask |
| Jurisdiction and governing law | Determines which mandatory terms apply and which clauses are enforceable | Ask |
| Contract type | Helps calibrate expectations (services, supply, license, JV, etc.) | Infer from the document; confirm if unclear |
| Business context | Why this contract matters; materiality of the deal | Ask; affects risk rating thresholds |

## Optional inputs

- Prior relationship with the counterparty (first contract vs. renewal)
- Prior version of the contract (if this is a revision)
- Any non-negotiable terms already agreed commercially
- Industry-specific regulatory requirements that affect the contract

## Review methodology

Work through the contract systematically using the following pass structure:

### Pass 1 — Structural completeness check

Confirm the contract contains all essential provisions:
- Parties (correctly named, with registered entity names, not trading names)
- Subject matter and scope (what exactly is being sold, licensed, or provided)
- Price and payment terms
- Term (start date, end date or perpetual, renewal mechanics)
- Intellectual property (ownership, license grant, restrictions)
- Confidentiality
- Representations and warranties
- Indemnification
- Limitation of liability
- Termination (for cause and for convenience)
- Governing law and dispute resolution
- Entire agreement / integration clause

Flag any of these that are absent or materially incomplete.

### Pass 2 — High-risk clause identification

Review each clause for risks to the client:

**Liability exposure**:
- Liability cap: is there one? Is it adequate? (Standard: capped at contract value or 12 months' fees — is the cap reasonable relative to the risks being assumed?)
- Consequential loss exclusion: does it apply? What is excluded (lost profits, lost data, business interruption)?
- Indemnification: what events trigger the indemnity? Is it mutual? Is it limited to third-party claims only or also direct claims?
- Insurance: is the counterparty required to maintain adequate insurance? Are required types and limits specified?

**IP and data**:
- Who owns IP created during the performance of the contract?
- Is there a broad assignment clause that transfers the client's pre-existing IP inadvertently?
- Data protection obligations: is there a data processing agreement or schedule? Does it comply with applicable PDPL/GDPR?
- Confidentiality: is the definition of "confidential information" appropriate? Are the exceptions (public domain, prior knowledge, legal obligation) included?

**Termination risk**:
- Can the counterparty terminate for convenience with short notice (e.g., 7–14 days)?
- Are there termination-for-cause provisions that could be triggered by minor technical breaches?
- Change-of-control clause: does it allow the counterparty to terminate if the client is acquired?
- What happens to IP, data, work in progress on termination? Is there a transition or wind-down period?

**Payment and financial**:
- Price escalation mechanisms: are automatic price increases permitted? Are they capped?
- Late payment interest: is the rate reasonable?
- Set-off rights: can the counterparty withhold payment for unrelated claims?
- Payment on termination: is there a termination fee that would apply? Is it proportionate?

**Operational constraints**:
- Exclusivity obligations that prevent the client from working with others in the same market
- Minimum purchase commitments with financial consequences for shortfall
- Non-compete obligations (scope, duration, geography — are they reasonable?)
- Change management: can the counterparty change the product, service, or terms unilaterally?

### Pass 3 — Ambiguity and drafting issues

Flag clauses that are unclear, ambiguous, or could be read against the client:
- Undefined terms used in key obligations
- Obligations that are qualified by "reasonable efforts" vs. "best efforts" vs. absolute obligations — know which applies to each party
- Clauses where the English text and any Arabic text diverge (in MENA bilingual contracts)
- Force majeure: is the definition appropriate? Does it cover pandemics, regulatory changes, cyber incidents? Are consequences proportionate (suspension vs. termination)?

### Pass 4 — Missing protections

Identify protections that the client should have but the draft does not include:
- Service level agreements and remedies for failure
- Business continuity and disaster recovery obligations
- Right to audit the counterparty's performance
- Step-in rights (if the counterparty is performing critical services)
- Benchmarking rights (for long-term contracts: right to compare prices against market)
- Most-favored-nation clause (if commercial parity matters)

### Pass 5 — MENA-specific review checklist

For contracts governed by or performed in MENA jurisdictions:

- **Penalty clauses**: UAE Civil Code (Art. 390), Lebanese Code of Obligations and Contracts, and Egyptian Civil Code all permit courts to reduce or increase penalty clauses to reflect actual loss; penalty clauses are not as certain as in common-law systems.
- **Interest**: In KSA (Sharia-based), conventional interest provisions may be unenforceable; use late payment compensation (indemnity for actual loss) rather than fixed interest rate.
- **Arbitration clause**: MENA courts have historically sometimes not recognized jurisdiction clauses selecting foreign courts; a well-drafted arbitration clause (specifying DIAC, DIFC-LCIA, ICC with UAE seat) is more reliable.
- **Language**: In UAE, the Arabic version of any contract governs if there is a conflict with the English version; in KSA, Arabic is the official language; ensure the Arabic version accurately reflects agreed terms.
- **Notarization (Tawtheeq)**: Some MENA jurisdictions require notarization of certain types of contracts (real estate, constitutional documents); check whether notarization is required for this contract type to be enforceable.

## Output format

Structure the review output as follows:

---

### Section A — High-risk clauses

| Clause | Issue | Risk Level | Recommended revision |
|---|---|---|---|
| Clause X.X | [Description] | High / Medium / Low | [Specific revised language or approach] |

---

### Section B — Unclear or ambiguous language

| Clause | Ambiguity identified | Recommended clarification |
|---|---|---|
| Clause X.X | [Description] | [Specific clarifying language] |

---

### Section C — Missing protections for [Company Name]

- [Description of missing protection and why it matters]
- Recommended clause: [brief description of the provision to add]

---

### Section D — Clauses that strongly favor the other party

| Clause | How it favors the other party | Negotiating position |
|---|---|---|
| Clause X.X | [Description] | [Suggested counter-position] |

---

### Section E — Suggested revisions (plain English summary)

For each significant issue, provide:
- **Current clause**: Quote the problematic language
- **Issue**: One-sentence explanation of the risk
- **Suggested revision**: Replacement language or alternative approach

---

### Top 3 risks summary

1. [Highest risk issue in one sentence]
2. [Second highest risk]
3. [Third highest risk]

---

## Jurisdictional notes

| Issue | Common-law (DIFC, UK) | Civil-law (UAE onshore, KSA, LB, EG) |
|---|---|---|
| Penalty clauses | Enforceable as liquidated damages if genuine pre-estimate of loss | Courts may adjust to reflect actual loss; severe penalties may be reduced |
| Limitation of liability | Enforceable subject to reasonableness | Enforceable but courts may override if grossly disproportionate |
| Consequential loss exclusion | Enforceable if clear | Enforceable; must be specific |
| Interest on late payment | Enforceable at contractual rate | KSA: interest may be unenforceable; use actual-loss compensation instead |
| Choice-of-law | Respected | Generally respected; mandatory local law provisions override |

## Common mistakes

- **Reviewing only the main body**: Many contracts incorporate additional documents by reference (operations manual, service specifications, data processing agreement); these must also be reviewed.
- **Ignoring governing law**: The same clause can be enforceable in one jurisdiction and void in another; always anchor the review to the specific governing law.
- **Accepting "standard" as non-negotiable**: Counterparties describe unfavorable terms as "our standard template"; everything is negotiable; identify which issues are dealbreakers and which are preferences.
- **Not checking for the entire agreement clause**: An entire agreement clause prevents reliance on pre-contractual representations; if the client was promised something that is not in the written contract, it will not be enforceable.
- **Failing to check the dispute resolution clause**: A dispute resolution clause in a foreign jurisdiction or requiring litigation in a difficult enforcement jurisdiction (such as Lebanon for commercial disputes) can make the agreement commercially worthless for recovery purposes.

## Related skills

- [[prompt-pack-disclosure-letter]]
- [[prompt-pack-distribution-agreement]]
- [[prompt-pack-franchise-agreement]]
- [[prompt-pack-employment-contract-compliance-review]]
