---
name: draft-share-purchase-agreement-sboghossian
title: Share Purchase Agreement (SPA)
description: Use when drafting a share purchase agreement (SPA) for a sale of shares in a private company, whether in a simple bilateral transaction or a structured M&A deal with earn-outs, escrow, and multiple parties. Covers the full SPA structure including representations and warranties, indemnification caps and baskets, conditions precedent, pre-closing covenants, and tax provisions. Addresses MENA-specific considerations including foreign ownership rules, regulatory approvals, and civil-law vs common-law warranty regime differences.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-share-purchase-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# Share Purchase Agreement (SPA)

A share purchase agreement transfers legal and beneficial ownership of shares from seller(s) to buyer(s). Unlike an asset deal, the buyer acquires the target company with all its history — including undisclosed liabilities — making the representations, warranties, disclosure process, and indemnification regime the most commercially sensitive elements of any SPA.

## When to use this

- Acquisition of a controlling or minority stake in a private company
- Management buyout or buy-in
- Private equity investment structured as a share acquisition
- Secondary sale by a financial investor
- Acquisition of a MENA subsidiary by a foreign strategic buyer
- Part of a wider group reorganization

## Required inputs

| Input | Why it matters | Default |
|---|---|---|
| Seller(s) — names, ownership percentages | Determines who signs, who warrants, and who receives proceeds | Must provide |
| Buyer(s) | Identifies the acquiring entity; affects regulatory approval requirements | Must provide |
| Target company | Full legal name, registration number, jurisdiction | Must provide |
| Shares being sold — number, class, % of capital | The subject matter of the agreement | Must provide |
| Consideration structure | Cash / shares / mix / earn-out; affects tax treatment and mechanics | Must provide |
| Closing mechanism | Simultaneous sign-close or signing-to-closing gap with conditions precedent | Simultaneous unless regulatory or third-party approvals required |
| Governing law | Affects warranty construction, limitation periods, implied terms | DIFC / English law for cross-border MENA deals; Delaware for US-side |

## Optional inputs

- Representations and warranties insurance (W&I insurance) — changes indemnification structure
- Earn-out metrics and calculation methodology
- Escrow amount, period, and release conditions
- Management retention arrangements
- Transition services agreement (TSA) parameters

## Document Structure

### 1. Definitions and Interpretation
Define all key terms. Note that civil-law jurisdictions (LB, UAE onshore) may interpret "best efforts" differently from common-law. Defined terms should include: Business Day, Material Adverse Change, Closing Date, Completion, Consideration, Earn-Out, Fundamental Warranties, Locked Box Date (if applicable).

### 2. Sale and Purchase
The operative transfer clause: Seller sells; Buyer buys; Consideration is the purchase price. Include:
- Share description (share certificates, class, number)
- Free of all encumbrances (important warranty — title is clean)
- Consideration mechanics:
  - **Cash at close**: straightforward; needs wire instructions and escrow mechanics
  - **Locked box**: price fixed at a historical balance sheet date; Seller warrants no "leakage" between the locked box date and closing; simpler for Seller
  - **Working capital adjustment**: price adjusted post-close to reflect actual working capital at close vs agreed target; more complex; standard in US/UK deals
  - **Earn-out**: deferred portion tied to post-closing performance (revenue, EBITDA, milestones); requires careful drafting of earn-out covenants to prevent Buyer from deliberately depressing earn-out metrics

### 3. Conditions Precedent
Conditions the closing depends on:
- Regulatory approvals (competition clearance, foreign investment approval — UAE CBUAE, ADGM FSA, KSA CMA, etc.)
- Third-party consents (material contracts with change-of-control clauses)
- Shareholder approvals (if target is a large company)
- Employee key-man retention
- Due diligence sign-off (if closing is not simultaneous with signing)
- No Material Adverse Change (MAC) — define MAC carefully: MENA courts may interpret it narrowly unless specifically defined

### 4. Pre-Closing Covenants
From signing to closing:
- Operate in the ordinary course of business (negative covenants: no new material contracts, no capital expenditure above threshold, no new indebtedness, no M&A, no change to key terms of employment)
- No leakage (in locked-box structure): no dividends, management charges, transactions with related parties outside agreed parameters
- Provide access for Buyer's due diligence confirmation
- Notify Buyer of any MAC event

### 5. Closing Actions
Simultaneous deliveries at closing:
- Seller delivers: share certificates (or transfer form), resignation letters from directors, board resolution approving transfer, statutory books
- Buyer delivers: wire transfer confirmation / completion payment, executed ancillary documents

### 6. Representations and Warranties

The warranty schedule is the most negotiated element. Organize by category:

| Category | Key warranties | Typical survival |
|---|---|---|
| Fundamental | Title to shares (no liens), capacity, authority, no conflict with third-party rights | Uncapped or full consideration cap; survives until statute of limitations |
| Corporate | Valid existence, no insolvency proceedings, articles / bylaws compliance | 24–36 months |
| Financial statements | True and fair; prepared in accordance with applicable GAAP/IFRS; no undisclosed liabilities | 24–36 months |
| Tax | No outstanding tax disputes; returns filed correctly; no unpaid tax liabilities; transfer pricing arrangements at arm's length | 7 years (aligns with most MENA tax limitation periods) |
| Intellectual property | Ownership of IP; no infringement of third-party IP; IP agreements current and enforceable | 36 months |
| Employees | No outstanding employment disputes; EOSG/EOSA fully provided; no undisclosed severance commitments | 24 months |
| Material contracts | Listed and current; no breach; no change-of-control triggers | 24 months |
| Real estate | Good title or valid leasehold; no undisclosed encumbrances | 36 months |
| Litigation | Disclosed litigation and regulatory proceedings only; no undisclosed threatened claims | 24 months |
| Compliance / regulatory | No sanctions violations; no bribery (FCPA / UK Bribery Act / KSA Anti-Bribery Law applicable) | 36 months |
| Environmental | No material environmental liability | 36–60 months |

### 7. Disclosure Schedule
The Seller's right to qualify warranties. The Disclosure Schedule is structured to track the warranty schedule clause by clause, with specific disclosures against each warranty. General disclosures (constructive knowledge of public records) are common in UK deals but resisted by Buyer's counsel. See [[draft-schedule-annex-builder]] for disclosure schedule structure.

### 8. Indemnification

| Parameter | Typical range | Notes |
|---|---|---|
| General indemnification cap | 10–25% of consideration | Below fundamental warranties cap |
| Fundamental warranties cap | 100% of consideration or uncapped | Fraud, title, capacity |
| Tax indemnity cap | Full consideration or uncapped | Tax indemnity is often separate from general warranties |
| De minimis per claim | 0.1–0.25% of consideration | Claims below this threshold not brought |
| Aggregate basket / threshold | 0.5–1.5% of consideration | Seller only liable once aggregate losses exceed this (tipping basket) or only for excess above (retention basket) |
| General warranty survival | 18–36 months from close | From closing date |
| Tax warranty survival | 7 years | Matches most applicable limitation periods |
| Fundamental warranty survival | Statute of limitations | 10–15 years in civil-law systems |

### 9. Specific Indemnities
Known issues identified in due diligence (pending litigation, regulatory investigations, environmental cleanup, unresolved tax disputes) are ring-fenced as specific indemnities outside the general warranty cap and basket.

### 10. Tax
- Pre-closing taxes: Seller responsible for all taxes for periods ending before closing
- Post-closing taxes: Buyer responsible
- Straddle periods: apportioned based on the period before and after the closing date
- Transfer taxes on the share acquisition (stamp duty, registration fees): Buyer typically bears

### 11. Restrictive Covenants on Seller
- Non-compete: Seller shall not engage in a competing business; typically 2 years; geographic scope tied to where the Target operates
- Non-solicitation of employees and customers: 2 years
- Carve-outs: passive investment (<3–5%), employment by a competitor that was pre-existing

### 12. Termination Rights
- Mutual: any time before closing by written agreement
- Material Adverse Change: Buyer may terminate if MAC occurs and is not waived
- Regulatory failure: if conditions precedent not satisfied by longstop date
- Material breach: if a party materially breaches its representations or pre-closing covenants and the breach is not cured within a notice period

### 13. Governing Law and Dispute Resolution
- Arbitration preferred for cross-border transactions (DIAC, ADGM, LCIA, ICC)
- For DIFC / ADGM deals: DIFC/ADGM courts or ADGM Small Claims have good enforcement track records
- Choice of law: English law standard for DIFC/ADGM; KSA law for domestic KSA deals; Lebanese law for LB deals

### 14. Boilerplate
Entire agreement, amendment, assignment (Buyer may assign to an acquisition vehicle; Seller may not assign warranty claims), waiver, severability, notices, costs (each party bears own costs), counterparts.

## MENA-Specific Considerations

### Foreign ownership restrictions
- **UAE**: Federal Decree-Law 26/2020 increased FDI permissible to 100% ownership in most sectors; strategic sectors (defense, banking, insurance, media, telecom) require CBUAE / UAE Cabinet approval
- **KSA**: Foreign Investment Law and the National Investment Strategy permit FDI in most sectors; specific sectors (oil production, real estate in Mecca/Medina, security) restricted; MISA approval required
- **LB**: Foreign ownership in Lebanese companies is generally permitted; restrictions in media, real estate (special rules apply)

### Arabic language and civil notarization
- In UAE-onshore, KSA, and Lebanon, the SPA or its certified translation may need to be notarized (Tawqi3i) for registration at the relevant commercial registry. A share transfer must be registered with the relevant Ministry of Economy or commercial registry to be effective against third parties.
- DIFC / ADGM: no Arabic requirement; English document; registration with DIFC / ADGM registrar of companies.

### No common-law rep & warranty insurance market in MENA onshore
W&I insurance is available for transactions governed by DIFC / ADGM / English law and handled through London or Dubai market. For UAE onshore and KSA transactions, W&I insurance is developing but not yet fully market standard.

## Common Mistakes

- **Signing without completing the disclosure schedule** — incomplete disclosure leaves Seller with full warranty exposure
- **Earn-out covenants too thin** — Buyer can depress earn-out by changing accounting policies or allocating overhead; need detailed earn-out covenants and independent calculation rights
- **Working capital definition disagreement at closing** — definition of working capital (current assets minus current liabilities; what is included/excluded) should be agreed at signing with a sample calculation
- **Missing change-of-control consents** — material contracts may terminate automatically or give the counterparty a termination right on a change of control; these must be identified in due diligence and consents obtained before closing
- **Tax — permanent establishment created by acquisition process** — Buyer's due diligence team operating in a jurisdiction can inadvertently create a PE; manage carefully
- **Ignoring EOSG/EOSA provisions** — in MENA acquisitions, the target company's EOSG/EOSA liability for employees is a real financial liability; verify whether it is fully provisioned on the balance sheet or separately funded

## Related skills

- [[draft-term-sheet-acquisition]]
- [[draft-shareholders-agreement]]
- [[draft-schedule-annex-builder]]
- [[draft-asset-purchase-agreement]]
- [[review-spa-buyer-side]]
- [[review-spa-seller-side]]
