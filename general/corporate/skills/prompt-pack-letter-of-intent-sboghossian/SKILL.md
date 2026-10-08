---
name: prompt-pack-letter-of-intent-sboghossian
title: Letter of Intent
description: Use when drafting a letter of intent (LOI) or heads of terms for a proposed acquisition, joint venture, partnership, or significant commercial transaction. Carefully distinguishes binding from non-binding provisions, outlines principal commercial terms, addresses exclusivity and confidentiality, and sets the path to definitive agreements. Applicable across MENA, GCC, EU, and common-law jurisdictions.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-letter-of-intent
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# Letter of Intent

## When to use this

Use this skill when parties to a significant transaction want to record their preliminary agreement on key terms before investing in full due diligence and definitive documentation. The LOI signals mutual commitment, provides a negotiating framework, and typically triggers exclusivity.

Triggers:
- "Draft an LOI for the acquisition of [Target]."
- "We've agreed in principle on a JV — write up the heads of terms."
- "Draft a non-binding letter of intent with an exclusivity period of 60 days."

**LOI vs MOU**: An LOI is typically more transaction-specific and shorter; an MOU is more common for collaborations and government/institutional relationships. Both serve to capture preliminary agreement. Use [[prompt-pack-memorandum-of-understanding]] if the context is a collaboration or institutional arrangement rather than a commercial transaction.

## Required inputs

| Input | Why it matters | Default |
|---|---|---|
| Transaction type | M&A / JV / strategic partnership / real estate acquisition | Ask user |
| Party A and Party B names | Identifies the parties | Ask user |
| Key commercial terms | Purchase price, ownership percentages, consideration structure | Ask user |
| Exclusivity period | Duration of exclusivity from signing | 45–60 days is typical; ask user |
| Due diligence scope | What DD is contemplated in the pre-definitive phase | Ask user |
| Governing law | Determines enforceability of binding provisions | Jurisdiction of target or DIFC/ADGM for cross-border |

## Optional inputs

- Break fee / termination fee if exclusivity is breached
- Financing condition (if buyer requires debt/equity financing to close)
- Conditions to signing definitive agreement
- Management continuity or retention requirements
- Employee consultation obligations (if regulated merger)
- Board approval conditions

## Document structure

### 1. Introduction
- Date and parties (full legal names)
- Brief description of the proposed transaction
- Statement that this LOI is intended to summarize the key terms and does not constitute a binding agreement except as expressly stated

### 2. Transaction Structure
- Type: acquisition of shares / assets / merger / JV
- Target: description of the business or asset being acquired / invested in
- Buyer / Investor / JV Parties: identity
- Consideration: purchase price or JV equity split; payment structure (cash, shares, deferred, earnout)
- Financing assumption: whether the transaction is subject to financing

### 3. Key Commercial Terms
Summarize the agreed economic terms:
- Valuation / headline price
- Payment mechanics: upfront vs staged; escrow / holdback arrangements
- Earnout conditions (if any): metric, period, calculation methodology
- Working capital adjustment mechanism
- Representations and warranties: scope expected in the definitive agreement
- Indemnification: general framework (time limits, caps, baskets)

### 4. Conditions to Signing Definitive Agreements
List conditions that must be satisfied before a definitive agreement can be signed:
- Satisfactory completion of due diligence by Buyer
- Approval by boards of directors of both parties
- Receipt of required regulatory approvals (competition/merger control, foreign investment approvals)
- Resolution of material issues identified in due diligence

### 5. Exclusivity (BINDING)
This clause is typically **binding**:
- Duration: [45 / 60 / 90] days from date of LOI
- Scope: Target and its shareholders / agents will not solicit, negotiate, or conclude an agreement with any other party regarding a competing transaction
- Extension: may be extended by mutual written agreement
- Effect of breach: Buyer may seek injunctive relief and/or a break fee

### 6. Confidentiality (BINDING)
- Cross-reference any existing NDA or state that a separate NDA is in effect
- If no NDA exists, include a standalone confidentiality clause binding on both parties
- This clause is typically **binding** even if the rest of the LOI is non-binding

### 7. Due Diligence Process
- Scope of DD: legal, financial, technical, commercial, tax, environmental, HR
- Access: Target agrees to provide reasonable access to management, documents, and data room
- Timing: DD to be completed within [X] days of LOI signing
- DD reports: Buyer to share summary findings that would require price adjustment

### 8. Path to Definitive Agreement
- Timeline: parties aim to sign a definitive agreement by [date]
- Documentation: identify the key documents to be negotiated (SPA / MFA / JV Agreement / SHA)
- Counsel: identify lead counsel for each party

### 9. Non-Binding Nature (IMPORTANT)
State clearly and prominently: "This Letter of Intent is not a binding agreement and creates no legal obligation to consummate the proposed transaction, except for the Exclusivity, Confidentiality, [Governing Law / Dispute Resolution], and [No-Solicitation] provisions, which are binding on the parties."

List each binding provision explicitly.

### 10. Governing Law and Dispute Resolution (BINDING)
- Governing law clause — critically important for cross-border LOIs
- MENA cross-border transactions: consider DIFC / ADGM law and courts for neutrality
- Dispute resolution for binding provisions: courts or expedited arbitration given time-sensitive nature of pre-closing disputes

### 11. Termination
- Either party may terminate if: conditions cannot be satisfied; material adverse change; due diligence reveals a fundamental problem
- Upon termination: confidentiality obligations survive; exclusivity ceases

## Jurisdictional notes

| Jurisdiction | Key issue |
|---|---|
| **UAE (onshore)** | An LOI creating exclusive dealing obligations may be enforceable under UAE Commercial Agency Law or Contract Law even if labeled "non-binding"; ensure the non-binding statement is explicit. |
| **KSA** | LOIs with price agreements can be construed as binding offers under Islamic law principles; take care with language. |
| **France** | Pre-contractual liability (culpa in contrahendo) is well-developed; withdrawing from negotiations after an LOI without justification can trigger damages liability. |
| **DIFC / ADGM** | Common-law approach; courts will look at objective intent to determine which provisions are binding; the explicit binding/non-binding distinction is highly effective. |
| **Cross-border** | Where parties are from different jurisdictions, specify governing law of the LOI separately from the governing law anticipated for the definitive agreement. |

**Foreign investment approvals**: MENA cross-border M&A may require MISA approval in KSA, or UAE regulatory approvals depending on the sector (banking, healthcare, telecoms). Include foreign investment approval as a closing condition.

## Common mistakes

- **Not specifying which provisions are binding**: courts in some civil-law jurisdictions will construe all provisions of a signed document as binding unless expressly excluded; the non-binding statement must be precise.
- **Unrealistic due diligence timeline**: 60-day exclusivity with 4 weeks of DD is only achievable for small/simple transactions; align the exclusivity period to the actual DD scope.
- **No break fee for exclusivity breach**: if Target solicits competing offers during exclusivity, Buyer has limited remedy without a contractual break fee.
- **Omitting regulatory approval conditions**: in GCC transactions involving foreign investment or regulated sectors, failure to include regulatory approval as a closing condition can trap the parties.

## Related skills

- [[prompt-pack-memorandum-of-understanding]]
- [[prompt-pack-merger-agreement]]
- [[prompt-pack-joint-venture-agreement]]
- [[prompt-pack-nda-strength-check]]
- [[prompt-pack-ip-due-diligence-checklist]]
