---
name: draft-term-sheet-acquisition-sboghossian
title: Acquisition Term Sheet
description: Use when drafting a non-binding term sheet for a full or majority-stake acquisition — setting out the transaction structure, purchase price mechanics (cash, earn-out, escrow), conditions precedent, representations and warranties scope, exclusivity period, and break provisions. Covers the principal negotiation axes (purchase price structure, escrow %, MAC definition, R&W cap) and the follow-on document chain to the definitive SPA. Addresses MENA-specific regulatory approval and foreign investment considerations.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-term-sheet-acquisition
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# Acquisition Term Sheet

An acquisition term sheet (also called a Letter of Intent or LOI) is the first formal document in an M&A process — it aligns Buyer and Seller on the material commercial terms before either side incurs the cost of a full due diligence exercise and definitive documentation. The binding/non-binding distinction is critical: if drafted carelessly, certain provisions can unintentionally bind the parties.

## When to use this

- Following initial commercial negotiations where both parties have reached substantive agreement on headline terms
- As a prerequisite to commencing due diligence (particularly when access to confidential information is to be shared)
- As the foundation document for the definitive Share Purchase Agreement or Asset Purchase Agreement
- As a pre-cursor to regulatory filings where regulators require a signed LOI before reviewing an application

## Required inputs

| Input | Why it matters | Default |
|---|---|---|
| Buyer + Seller (full legal names and capacities) | Determines who is bound by the binding provisions | Must provide |
| Target company (name, jurisdiction) | Subject matter of the transaction | Must provide |
| Transaction structure | Share purchase / asset purchase / merger / reorganization | Must specify — affects tax treatment and regulatory requirements significantly |
| Consideration | Amount and structure (cash / shares / mix / earn-out) | Must specify |
| Closing conditions | What must happen before the deal closes | Regulatory approval + due diligence satisfactory + no MAC at minimum |
| No-shop / exclusivity period | Duration and scope | 30–60 days standard |
| Confidentiality | Is a separate NDA in place? If not, include here | Binding; mutual |

## Optional inputs

- Reverse break fee (if Buyer walks without cause)
- Target break fee (if Seller accepts a competing offer during exclusivity)
- Management retention terms (if key employees are critical)
- Earn-out high-level mechanics (if earn-out is part of the consideration)
- Governing law for the term sheet itself (binding provisions)

## Document Structure

### 1. Parties and Purpose
One paragraph identifying Buyer, Seller, and Target; purpose: the parties wish to record the principal terms upon which Buyer proposes to acquire [Target] from Seller. State that the term sheet is subject to the satisfactory completion of due diligence and execution of definitive documentation.

### 2. Transaction Structure

Specify clearly whether this is:
- **Share purchase**: Buyer acquires legal and beneficial title to all/majority of the shares; Target company survives with all its history (liabilities included)
- **Asset purchase**: Buyer acquires specified assets and liabilities; Target remains as an entity but without the acquired assets; cleaner liability picture but more complex to structure
- **Merger**: legal amalgamation; typically requires regulatory process; less common in MENA

The choice has major tax consequences:
- Share purchase: no transfer of assets for VAT purposes; stamp duty / transfer taxes on the shares
- Asset purchase: VAT may apply to the transfer of business assets; potential for asset stepped-up basis (favorable for Buyer)
- In UAE onshore and KSA, obtaining professional tax advice before committing to structure is essential given VAT (5% UAE; 15% KSA) and corporate tax implications

### 3. Purchase Price and Payment Mechanics

| Component | Description | Notes |
|---|---|---|
| Cash at close | Payment on the closing date in cleared funds | Wire to designated account in cleared funds |
| Deferred consideration | Amount payable after closing on agreed terms | Secured? Unsecured? | 
| Earn-out | Performance-contingent amount tied to Target's post-closing results | Define metrics, measurement period, and cap |
| Escrow | Portion of purchase price held by escrow agent for a period post-close | Typically 10–15% for 12–24 months as recourse for warranty claims |
| Working capital adjustment | Price adjusted post-close to reflect actual vs target working capital | Define working capital for purposes of adjustment; provide sample calculation |

### 4. Working Capital Adjustment Mechanism

If a working capital adjustment is included:
- Define "Working Capital" precisely (current assets minus current liabilities; specify what is and is not included)
- Set a target working capital amount (based on historical average)
- Process: Seller prepares an estimated working capital statement at close; Buyer prepares a final working capital statement within 60 days post-close; disputes to an independent accountant
- Adjustment: if actual working capital > target, Buyer pays the excess; if actual < target, Seller returns the shortfall

### 5. Conditions Precedent

List conditions that must be satisfied before the parties are obliged to close. Common conditions:
- Regulatory approvals: competition clearance (if applicable), FDI/foreign investment approval, sector-specific regulatory approvals (KSA CMA, UAE CBUAE/TDRA/ADGM FSA depending on sector)
- Third-party consents: material contracts with change-of-control provisions that require consent to assignment
- Shareholder approvals: if Seller's corporate constitution requires shareholder approval for the disposal
- Due diligence: satisfactory completion of Buyer's due diligence (due diligence condition should be either removed or defined with a materiality threshold — an open-ended "satisfactory due diligence" condition creates a subjective out)
- No Material Adverse Change (MAC): definition matters enormously; typical MENA practice:
  - MAC = a change that has or would reasonably be expected to have a material adverse effect on the Target's business, financial condition, or results of operations
  - Carve-outs: general economic conditions, industry-wide events, changes in law, pandemic-related events (heavily negotiated post-COVID)
- Employee retention: key employees have signed offer letters for continued employment post-close

### 6. Representations and Warranties Scope (High-Level)

State at a high level that Seller will make customary representations and warranties in the SPA covering:
- Title and authority
- Financial statements accuracy
- Absence of undisclosed liabilities
- Compliance with law
- Material contracts and no material breach
- Intellectual property ownership
- Employment — no undisclosed severance commitments
- Tax — returns filed; no outstanding disputes
- No material litigation

The detail will be set out in the SPA; the term sheet signals the scope and the indemnification framework.

### 7. Indemnification Framework

| Parameter | Indicative range | Notes |
|---|---|---|
| R&W cap (general) | 10–30% of consideration | Stated as a % range; exact % negotiated in SPA |
| R&W cap (fundamental) | 100% or full consideration | Title, capacity, fraud |
| Aggregate basket | 0.5–1.5% of consideration | Threshold before claims can be brought |
| Survival — general warranties | 18–36 months from close | |
| Survival — tax warranties | 7 years from close | Matches most MENA limitation periods for tax |

### 8. Restrictive Covenants on Seller

- Non-compete: Seller and key individuals shall not compete for [2 years] in [geographic scope]; confirm this is appropriate for the jurisdiction
- Non-solicitation: no poaching of Target's customers or key employees for [2 years]
- Seller should confirm that these covenants, combined with any existing employment restrictions, are enforceable under the governing law

### 9. Key Employee Retention

If Buyer is relying on specific management to continue, state:
- Key employees to be identified and offer letters executed before close
- Retention period and terms (salary, benefits, equity rollover)
- Whether key employee retention is a condition precedent to closing

### 10. Termination Rights

| Right | Trigger | Consequence |
|---|---|---|
| Either party — longstop date | If closing has not occurred by [date] | Terminates term sheet; expenses remain allocated per below |
| Buyer — MAC | Material adverse change in Target | Buyer may terminate; no break fee |
| Buyer — due diligence failure | Materially adverse due diligence finding (if DD condition included) | Buyer may terminate; no break fee |
| Seller — competing offer | Seller accepts a competing offer during exclusivity | Seller pays break fee if applicable |

### 11. Exclusivity / No-Shop Period

Duration: 30–60 days from execution of the term sheet.

Scope: Seller shall not, and shall procure that Target and its representatives shall not, directly or indirectly: (a) solicit, initiate, or encourage any competing acquisition proposal; (b) provide information to any third party in connection with a competing proposal; or (c) enter into discussions or negotiations regarding a competing proposal.

This is the most commercially important binding provision in the term sheet.

### 12. Expenses and Break Fee

- Each party bears its own costs in connection with the transaction (standard)
- Break fee (if agreed): payable by [Seller/Buyer] if [trigger condition] occurs; amount typically 1–3% of the purchase price
- Reverse break fee (payable by Buyer for regulatory failure or financing failure): more common in public M&A; negotiate in private deals where regulatory approval is uncertain

### 13. Binding vs Non-Binding Provisions

**Non-binding**: all transaction terms (structure, price, conditions, warranties scope, restrictive covenants) — these are subject to negotiation and definitization in the SPA.

**Binding**: the following are legally binding from execution:
- Exclusivity / no-shop (critical)
- Confidentiality
- Break fee provisions (if included)
- Governing law for the term sheet itself
- Expenses allocation

State this clearly: "Sections [X] (Exclusivity), [Y] (Confidentiality), and [Z] (Expenses) are intended to be legally binding. All other provisions of this Term Sheet are non-binding and subject to negotiation and execution of definitive documentation."

### 14. Governing Law and Dispute Resolution

The binding provisions of the term sheet (exclusivity, confidentiality) should specify a governing law and a dispute resolution mechanism. Arbitration is preferred for MENA cross-border transactions.

## MENA-Specific Considerations

### Regulatory approval timelines
MENA regulatory approvals can be significant:
- UAE competition authority (CECO) notification: if merger notification thresholds are met
- Sector-specific: ADGM FSA, DIFC FSA, UAE TDRA, KSA CMA — each has its own process and timeline (typically 30–90 days minimum)
- Foreign ownership approvals (ADIO in Abu Dhabi, MISA in KSA): particularly for sensitive sectors
- Build realistic closing timelines; experienced MENA M&A counsel should advise on regulatory risk early

### No-shop: Arabic-language contract
If the Seller is a KSA or UAE onshore entity and the term sheet is in English only, confirm that the binding no-shop and confidentiality provisions will be enforceable. Consider having the binding provisions clause included in both English and Arabic with a consistency statement.

## Document Follow-Up Chain

```
Term Sheet (signed)
    ↓
Due Diligence (financial, legal, tax, technical)
    ↓
Disclosure Schedule preparation (Seller)
    ↓
Definitive SPA (see [[draft-share-purchase-agreement]])
    ↓
Ancillary documents (escrow agreement, transitional services, employment offers)
    ↓
Regulatory filings and approvals
    ↓
Closing
```

## Related skills

- [[draft-share-purchase-agreement]]
- [[draft-asset-purchase-agreement]]
- [[draft-nda-mutual]]
- [[draft-shareholders-agreement]]
- [[review-spa-buyer-side]]
