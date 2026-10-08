---
name: workflow-contract-redline-20min-sboghossian
title: Contract Redline in 20 Minutes
description: Use when a user needs to review and redline a contract under time pressure, producing a structured redline and executive-summary memo within approximately 20 minutes. Works for NDAs, MSAs, leases, employment contracts, and SPAs. Orchestrates triage, risk-flagging, systematic clause review, and memo drafting in a disciplined time-boxed sequence, with MENA-specific risk flags integrated into the review pass.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/workflow/workflow-contract-redline-20min
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Contract Redline in 20 Minutes

## Purpose

A disciplined 20-minute workflow for producing a review-quality contract redline and accompanying memo. Designed for in-house counsel and outside counsel who need a deliverable quickly — not a shallow skim but a structured, prioritized review that surfaces material risk and provides actionable redlines.

---

## Inputs

| Input | Required | Notes |
|-------|---------|-------|
| Contract document | Yes | Paste text or describe the contract |
| User's side | Yes | Buyer/seller, employer/employee, licensor/licensee, tenant/landlord |
| Contract type | Yes | NDA, MSA, SPA, lease, employment, consulting, etc. |
| Jurisdiction | Yes | Governing law — determines applicable defaults and non-waivable rules |
| Priority issues | Recommended | Any specific clauses or risks to prioritize |
| Materiality threshold | Optional | Deal size / risk tolerance context |

---

## Logic — Time-Boxed Steps

### Minutes 0–2: Setup and Orientation

Before reviewing a single clause:

1. **Identify contract type.** The review methodology differs materially by type:
   - NDA → focus on definition of confidential information, exclusions, term, return/destruction, residuals clause
   - MSA → focus on liability cap, indemnification balance, IP ownership, termination, data processing
   - Employment → focus on non-compete scope, IP assignment, termination triggers, equity vesting
   - Lease → focus on rent escalation, break clauses, repair obligations, use clause, registration
   - SPA → focus on reps & warranties, conditions, MAC clause, indemnification, escrow

2. **Identify your side.** The analysis is side-specific:
   - Seller in an SPA → push for clean reps, short survival, low escrow
   - Buyer in an SPA → push for broad reps, long survival, full indemnification
   - Employee → push for broad good-reason triggers, equity acceleration, non-compete limits
   - Employer → push for IP assignment, garden leave, enforceable non-compete

3. **Identify jurisdiction and load applicable defaults.** Key MENA defaults that differ from US/UK:
   - UAE: Federal Decree-Law 33/2021 provides minimum employment rights; cannot waive by contract
   - KSA: Sharia principles; prohibition on penalty clauses that function as interest (riba)
   - LB: Labor Code Art 50 — employer must pay indemnity for termination without cause regardless of contract
   - DIFC: DIFC Contract Law (English-law influenced); DIFC Employment Law
   - Civil law jurisdictions generally: concepts like force majeure are statutory, not purely contractual

4. **Load applicable review skills.** Relevant supplementary skills:
   - [[review-contract-redline]] · [[review-missing-clauses]] · [[review-risk-flagging]] · [[review-unusual-terms-detector]]

---

### Minutes 2–7: Triage Pass

Run two parallel sweeps:

**Sweep A — Missing clauses** ([[review-missing-clauses]])**:**

What should be in this contract that is not? Common missing clauses by type:

| Contract type | Clauses often absent in counterparty drafts |
|--------------|-------------------------------------------|
| NDA | Residuals clause (if tech company); return/destruction obligation; specific exclusions for publicly available info |
| MSA | Data processing agreement / GDPR/PDPL provisions; source code escrow for SaaS; SLA with meaningful credits |
| Employment | IP assignment scope; specific non-compete geographic/temporal limits; good reason triggers for executive resignation |
| SPA | MAC (Material Adverse Change) definition; locked box vs. completion accounts mechanism; specific indemnities for known issues |
| Lease | Break clause; service charge audit rights; assignment/subletting rights; dilapidations protocol |

**Sweep B — Atypical / high-risk clauses** ([[review-risk-flagging]])**:**

Flag anything that deviates materially from market standard:
- Uncapped liability
- Broad indemnification for indirect/consequential damages
- Automatic renewal without notice
- One-sided termination rights
- IP assignment that sweeps in pre-existing IP
- Penalty clause that may be unenforceable (especially in civil law jurisdictions)
- Jurisdiction clause naming a forum with uncertain enforcement

---

### Minutes 7–17: Systematic Redline Pass

Work through the Top-5 value clauses first, then secondary clauses:

**Top-5 priority clauses (always):**

| # | Clause | What to redline |
|---|--------|----------------|
| 1 | Liability cap | Ensure cap is proportionate to contract value (e.g., 12 months fees); confirm cap excludes fraud, gross negligence |
| 2 | Indemnification | Narrow indemnity triggers; mutual indemnity; cap indemnity obligations at a defined maximum; exclude consequential/indirect losses |
| 3 | IP ownership | Confirm IP created under the contract is correctly allocated; check that pre-existing IP is licensed, not assigned |
| 4 | Termination | Ensure adequate notice periods; check termination-for-convenience clause from your side; check cure periods for termination for cause |
| 5 | Dispute resolution | Confirm jurisdiction is convenient; confirm arbitration clause is complete (seat, rules, language, number of arbitrators) |

**Per-clause redline format:**

For each clause with an issue:
```
Clause: [clause number and heading]
Current text: [quote the key problematic passage]
Issue: [1-sentence description of the risk or problem]
Severity: HIGH / MEDIUM / LOW
Proposed text: [the specific replacement or addition]
Rationale: [1-sentence why this is better]
```

**MENA-specific watch points during the redline pass:**

- **Penalty clauses**: in UAE, KSA, and LB civil law, courts may reduce disproportionate penalties to actual damages — label any liquidated damages provision with a MENA-enforceability note
- **Choice of law and courts**: if the counterparty insists on local UAE mainland courts, note that enforcement of judgments against foreign parties or in foreign jurisdictions requires separate proceedings; DIFC/ADGM arbitration is more internationally enforceable (New York Convention)
- **Language**: contracts in KSA and UAE should address which language version controls; Arabic text controls for government contracts and may be required for labor contracts
- **Notarization**: MENA civil law employment contracts and some commercial agreements require notarization (Tawqi3i / Tawtheeq) for full enforceability against third parties — check if required
- **Non-compete enforceability**: KSA courts generally enforce reasonable non-competes; UAE courts have inconsistent track record; LB courts apply strict proportionality; avoid absolute prohibitions

---

### Minutes 17–19: Polish and Prioritization

1. **Reorder redlines by severity**: HIGH issues first (blocking / must-fix), MEDIUM (push hard in negotiation), LOW (nice to have, concede if needed)
2. **Add fallback positions**: for each HIGH issue, state your ideal redline AND an acceptable fallback if counterparty resists
3. **Add open questions**: issues requiring client input or further information (e.g., "confirm whether any existing IP should be carved out of the IP assignment")
4. **Add a 3-sentence BLUF** (Bottom Line Up Front) for the executive summary

---

### Minutes 19–20: Output Assembly

Produce two deliverables:

**Deliverable 1 — Executive Summary Memo** (see [[output-executive-summary-first]])**:**

```
MEMO: [Contract name] Review
Date: [Date]
Prepared for: [Client/matter name]
Side: [User's position]
Governing law: [Jurisdiction]

BLUF: [3 sentences summarizing the overall risk level and the 1-2 most critical issues]

TOP ISSUES:
1. [Highest severity issue — clause, problem, proposed fix]
2. [Second severity issue]
3. [Third severity issue]
...

OPEN QUESTIONS:
- [Item requiring client input]

RECOMMENDATION: [Sign as-is / counter-redline / reject / escalate]
```

**Deliverable 2 — Redline Document** (if requested)**:**
- Track-change format if a document editor is available
- Or a numbered list of proposed clause substitutions with current text → proposed text

---

## Quality Bar

A 20-minute redline is not a full legal opinion. It is:
- Appropriate for: routine commercial contracts; repeat counterparties with familiar terms; in-house teams with good institutional knowledge
- Not appropriate for: first-time novel transaction structures; very high-value deals with complex representations; regulatory approval transactions

For complex matters, this workflow provides a first-pass risk map to guide deeper analysis, not a final work product.

---

## Why This Matters

The 20-minute redline workflow is a high-leverage legal skill: it turns unstructured review into a repeatable, auditable process. The time constraint forces prioritization (what matters most?) and the deliverable format forces clear communication to non-lawyer stakeholders.

---

## Related Skills

- [[review-contract-redline]]
- [[review-missing-clauses]]
- [[review-risk-flagging]]
- [[review-unusual-terms-detector]]
- [[output-executive-summary-first]]
- [[workflow-nda-triage-red-yellow-green]]
