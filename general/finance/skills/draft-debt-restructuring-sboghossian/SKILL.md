---
name: draft-debt-restructuring-sboghossian
title: Debt Restructuring Agreement
description: Use when drafting a debt restructuring agreement between a distressed borrower and one or more creditors — covering extension of maturities, interest-rate renegotiation, debt-to-equity conversion, haircuts, standstill provisions, and inter-creditor arrangements. Relevant pre-insolvency, during distressed M&A, or in workout contexts across MENA (UAE, KSA, LB), DIFC, ADGM, UK, and EU. Should be paired with insolvency-law review and financial modeling of recovery scenarios.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-debt-restructuring
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: finance
language: en
---

# Debt Restructuring Agreement

## When to use this

A debt restructuring agreement is the master document governing a consensual reorganization of a borrower's obligations when those obligations cannot be met on their original terms. Trigger scenarios:

- Borrower is in default (or imminent default) under one or more facilities and seeks to avoid insolvency proceedings.
- Lenders want a controlled workout rather than accelerating and forcing a distressed sale.
- Multiple creditors need to coordinate their positions (bilateral restructuring vs. multi-creditor inter-creditor arrangement).
- A distressed M&A transaction requires the target's debt to be restructured as a condition of closing.
- Post-acquisition integration of a leveraged buyout under financial stress.

**When not to use this skill alone:** if insolvency proceedings are already commenced, the restructuring agreement must operate within the formal framework (DIFC Insolvency Law, UAE Federal Bankruptcy Law 9/2016, UK Insolvency Act 1986, etc.) — involve local insolvency counsel and note that automatic stays, set-off rights, and super-priority may apply.

## Required inputs

| Input | Why it matters | Default |
|-------|----------------|---------|
| Borrower identity + group structure | Defines who is bound; subsidiary guarantors may need to accede | — |
| List of existing debt facilities (lender, outstanding principal, currency, maturity, security) | The instrument cannot restructure what it does not identify with precision | — |
| Creditor group composition | Bilateral vs. syndicated; bank vs. bond; secured vs. unsecured | — |
| Proposed restructured terms (per facility or per class) | The commercial deal drives all drafting choices | — |
| Security package (existing and new/amended) | Perfection requirements differ by jurisdiction | — |
| Governing law of existing facilities | Restructuring agreement typically matches; multi-jurisdiction often uses English law | English law (common) |
| Inter-creditor status (if multi-creditor) | Priority ranking, voting thresholds, enforcement standstill | — |

## Optional inputs

- Third-party professional advisor (financial advisor / independent business review) report
- Lock-up agreement (binding commitment from majority creditors to support the restructuring)
- New money facility terms (DIP-style financing in formal proceedings)
- Management incentive plan changes
- Regulatory / MENA central-bank notifications required

## Document structure

### 1. Recitals
Identify the borrower, the original credit facilities (by reference to facility agreements), the current outstanding amounts, and the commercial background for the restructuring.

### 2. Definitions
Define "Existing Facilities", "Restructured Terms", "Effective Date", "Longstop Date", "Majority Creditors" (voting threshold), "Standstill Period", "Restructuring Conditions", "Inter-Creditor Agreement" (if separate).

### 3. Restructured terms — per facility / per class
For each facility, set out the new agreed terms:

**Extension of maturity**
- New maturity date.
- Amortization schedule (bullet vs. term).
- Payment-in-kind (PIK) toggle option if any.

**Interest renegotiation**
- Rate change (fixed ↔ floating; margin compression; PIK interest option).
- Capitalisation of arrears (often converted to principal).

**Debt-to-equity conversion**
- Conversion amount.
- Valuation basis for equity issued.
- Dilution mechanics; cap table post-conversion.
- Regulatory approvals (change-of-control, foreign ownership limits in MENA).

**Haircuts / write-downs**
- Amount forgiven per creditor.
- Condition on which haircut is permanent vs. contingent (clawback on recovery above threshold).

### 4. Security package
- Confirmation, amendment, or enhancement of existing security.
- New security (pledges, mortgages, assignments).
- Release of security on pre-conditions (satisfaction of certain conditions).
- Perfection steps required in each jurisdiction.

### 5. Standstill provisions
- Period during which creditors agree not to accelerate, enforce security, or commence insolvency proceedings.
- Events ending standstill early (material breach, false representations, further defaults).
- Permitted actions during standstill (routine operations, protective registrations).

### 6. Inter-creditor provisions (or reference to separate ICA)
- Priority ranking: super-senior / senior secured / senior unsecured / subordinated.
- Voting thresholds for material amendments (typically 66.67% or 75% by value).
- Payment waterfall during standstill.
- Enforcement instructions: who controls enforcement of security; directing creditor.
- Anti-embarrassment: restrictions on creditor transfers during standstill.

### 7. Conditions precedent to effectiveness
- Receipt of all required consents and regulatory approvals.
- Execution by minimum threshold of creditors.
- Delivery of updated security perfection evidence.
- Independent business review (if required).

### 8. Representations and warranties (borrower)
- Financial statements are true and fair.
- No undisclosed liabilities.
- No insolvency events.
- No material adverse change since last accounts.

### 9. Undertakings (borrower during standstill and post-restructuring)
- Financial covenants (leverage, DSCR, liquidity).
- Information undertakings (monthly management accounts, audited annual financials).
- Positive covenants: maintain insurance, pay taxes, preserve assets.
- Negative covenants: no new debt, no asset disposals above threshold, no related-party transactions.
- Change-of-control trigger.

### 10. Events of default / termination triggers
List events that end the standstill or accelerate restructured debt:
- Non-payment under restructured terms.
- Breach of undertakings (with grace period).
- Insolvency of borrower or key guarantors.
- Material misrepresentation.
- Cross-default to other indebtedness above threshold.

### 11. Closing mechanics
- Longstop date.
- Escrow of documents pending satisfaction of conditions.
- Simultaneous vs. sequential closing for multi-facility deals.

### 12. Governing law and dispute resolution
- Choice of governing law; arbitration clause (DIAC, LCIA, ICC common for MENA).
- Service of process in each relevant jurisdiction.

## Jurisdictional notes

| Jurisdiction | Key framework | Critical traps |
|---|---|---|
| **UAE (onshore)** | Federal Bankruptcy Law 9/2016 (financial restructuring, preventive composition, bankruptcy) | MENA restructurings often avoid onshore UAE courts due to perceived creditor-unfriendly outcomes; DIFC/ADGM with English-law governing instruments preferred for international deals |
| **DIFC** | DIFC Insolvency Law (DIFC Law 1/2019); DIFC Courts enforce English-style commercial agreements | DIFC insolvency proceedings can be recognized onshore via DIFC-UAE judicial protocol |
| **ADGM** | ADGM Insolvency Regulations 2015 (modeled on UK); ADGM Courts | ADGM receivership and administration available; strong creditor tools |
| **KSA** | Bankruptcy Law (Royal Decree M/50 2018) — financial restructuring unit (FRU), liquidation, reorganization | Foreign ownership/debt-to-equity conversion in strategic sectors requires MISA and other approvals |
| **Lebanon** | Financial restructuring historically court-supervised under Commercial Code; banking sector moratorium 2019-onwards creates unique complexity | LB bank exposures subject to BDL and banking-sector-specific restructuring frameworks; seek specialist counsel |
| **UK** | Scheme of arrangement (Companies Act 2006), restructuring plan (CIGA 2020), CVA | Cross-class cramdown available under restructuring plan; widely used for MENA issuers with UK holding co |
| **France** | Procédure de conciliation, sauvegarde, redressement judiciaire | French law protects debtors significantly; foreign creditors may prefer English-law governed instruments |

## Common mistakes

1. **Failure to identify all debt** — an undisclosed facility that did not accede to the standstill can accelerate and file for insolvency, unraveling the consensual restructuring.
2. **Ambiguous inter-creditor priority** — disputes over enforcement priority are the primary source of restructuring litigation; every tranche needs explicit ranking.
3. **Missing regulatory approvals** — debt-to-equity conversions in MENA may require foreign-ownership approvals (MISA, ADIB, UAE Cabinet), competition approvals, and sector-specific regulator consents.
4. **Inadequate perfection of new security** — security created in the restructuring must be perfected per local law (UAE/KSA mortgage registration, Lebanon pledge law); unperfected security is valueless against third parties.
5. **Standstill enforcement gap** — without a lock-up agreement signed before the standstill, a minority creditor can breach the standstill before it becomes effective.
6. **Sharia finance structures** — murabaha and ijara facilities cannot be restructured using conventional interest-renegotiation mechanics; a Sharia-compliant restructuring supplement is required.

## Related skills

- [[draft-loan-agreement]] — underlying facility agreement that the restructuring amends
- [[draft-guarantee]] — guarantor arrangements often modified as part of restructuring
- [[draft-share-purchase-agreement]] — if debt-to-equity conversion is the restructuring mechanism
- [[review-financial-covenants]] — analysis of existing covenant package before proposing amendments
- [[kb-insolvency-mena]] — insolvency law knowledge pack for UAE, KSA, and LB
