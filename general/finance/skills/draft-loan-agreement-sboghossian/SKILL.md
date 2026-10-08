---
name: draft-loan-agreement-sboghossian
title: Loan Agreement / Facility Agreement
description: Use when drafting a loan agreement or facility agreement between a lender and borrower for a commercial or corporate financing. Covers facility type, interest mechanics (including Sharia-compliant structures for KSA), covenants, events of default, security cross-references, and key lender/borrower negotiation points. Handles LMA-style common-law agreements (DIFC/ADGM) and civil-law structures (LB, UAE onshore). Triggers on "loan agreement", "facility agreement", "credit agreement", "term loan", "revolving credit", or Islamic finance equivalents (murabaha, ijara, tawarruq).
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-loan-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: finance
language: en
---

# Loan Agreement / Facility Agreement

## When to use this

Use this skill when a lender (bank, private credit, bilateral, or syndicated) is extending credit to a borrower (corporate or individual). This skill covers the full loan agreement from facility type through representations, covenants, events of default, and governing law.

Distinct uses:
- **Bilateral term loan**: one lender, one borrower, single drawdown
- **Revolving credit facility**: multiple drawdowns up to a cap; repayable and re-drawable
- **Syndicated facility**: multiple lenders acting through an agent (LMA-style); much more complex — this skill gives the core; engage banking counsel for syndicated structures
- **Islamic financing**: KSA and other GCC clients frequently prefer Sharia-compliant structures — see Jurisdictional notes below

For a simple short-term promissory obligation, use [[draft-promissory-note]] instead.

## Required inputs

| Input | Why it matters | Default |
|-------|---------------|---------|
| Lender + Borrower (+ Guarantor(s)) | Parties; guarantor(s) require separate guarantee instrument | — must supply |
| Principal amount + currency | Defines the facility size | — must supply |
| Interest rate + payment schedule | Core economic terms; specify EIBOR/SAIBOR/SOFR + margin or fixed rate | EIBOR + margin (UAE); SAIBOR + margin (KSA) |
| Tenor (term) | Duration of the loan | 3-5 years for term loans |
| Repayment structure | Bullet / amortizing / balloon | — must specify |
| Security | None / pledge of assets / mortgage / guarantee | None unless specified |
| Governing law | Law of the agreement | DIFC or UAE law for UAE deals |

## Document structure

### 1. Definitions
Core definitions: Drawdown Date, Availability Period, Interest Period, Interest Payment Date, Repayment Date, Margin, Reference Rate, Mandatory Costs, Market Disruption Event, Event of Default, MAC (Material Adverse Change/Effect), Finance Document, Security Document.

### 2. The Facility
- Type: term loan / revolving credit facility / multi-currency facility
- Amount: the committed amount; if revolving, the maximum outstanding at any time
- Purpose: state the specific permitted use of proceeds (working capital, acquisition, refinancing, construction) — enables the lender to monitor and, in some cases, restrict misuse
- Availability period: window during which the Borrower may draw down

### 3. Conditions Precedent
What must be delivered and satisfied before the first drawdown:
- Corporate authorization documents (board resolutions, constitutional documents, good-standing certificates)
- Finance documents duly signed
- Security documents perfected
- Legal opinions from counsel to each party
- No-event-of-default certificate from Borrower
- For acquisition facilities: evidence of acquisition completion or conditionality
- KYC/AML documentation (see [[draft-kyc-procedure]])

### 4. Drawdown mechanics
- Drawdown notice: form, timing (typically 3-5 business days before drawdown date), irrevocability
- Conditions to each drawdown (for revolving): representations and warranties true; no event of default
- Minimum drawdown amount
- Banking days and cut-off times for same-day value

### 5. Interest
- **Reference rate**: EIBOR (UAE), SAIBOR (KSA), SOFR (USD), EURIBOR (EUR), SONIA (GBP) + Margin; reset at start of each Interest Period (1, 3, or 6 months typically)
- **Market disruption provision**: if the Reference Rate is unavailable (IBOR transition), the lender may quote a replacement rate; include ISDA fallback language or specific contractual fallback
- **Default interest**: on overdue amounts, reference rate + margin + penalty spread (typically 2-3%)
- **Interest payment dates**: monthly, quarterly, or semi-annual in arrears

### 6. Repayment
- **Schedule**: attach a full amortization schedule as an exhibit; or for revolving, state final maturity date
- **Bullet repayment**: entire principal at maturity — simple but creates refinancing risk
- **Amortizing**: principal repaid in equal (or unequal) scheduled installments
- **Balloon**: partial amortization during term, large final payment at maturity
- **Voluntary prepayment**: right to prepay; notice period (typically 5-10 business days); prepayment premium (breakage costs for fixed-rate; sometimes a penalty for early repayment in first X years)
- **Mandatory prepayment events**: receipt of insurance proceeds (above threshold), asset disposal proceeds (above threshold), equity issuance (excess cash sweep), change of control

### 7. Fees
- **Arrangement fee**: one-time upfront; typically 0.5-2% of facility amount
- **Commitment fee**: on undrawn commitment for revolving facilities; accrues daily; typically 25-50% of Margin
- **Agency fee**: annual; payable to the facility agent in syndicated deals
- **Prepayment fee** / breakage costs: covers the lender's cost of unwinding hedges

### 8. Representations and warranties
Borrower represents and warrants (on signing and on each drawdown):
- Corporate status: duly incorporated, validly existing, authorized to borrow
- Power and authority: board resolutions obtained, no constitutional limitation
- No conflict: execution does not violate constitutional documents, material agreements, or applicable law
- Solvency: not insolvent; no pending insolvency proceedings
- Financial statements: most recent audited financials fairly presented; no material adverse change since date of financials
- No material litigation: no proceedings pending that would have a material adverse effect
- Tax compliance: all taxes filed and paid; no disputed tax claims of material amount
- Environmental: no material environmental liabilities (if relevant)
- Anti-corruption: no violation of applicable anti-bribery laws (FCPA, UK Bribery Act, local equivalents)
- Sanctions: not a Sanctioned Person; proceeds not used for sanctioned activities

### 9. Covenants
**Affirmative covenants** (Borrower must do):
- Deliver annual audited financial statements within 90/120 days of fiscal year end
- Deliver quarterly management accounts within 45/60 days of quarter end
- Notify Lender of any Event of Default (or potential Event of Default) promptly
- Maintain insurance
- Comply with all applicable laws and authorizations
- Maintain and operate the business in its ordinary course

**Negative covenants** (Borrower must not without Lender's consent):
- Incur additional financial indebtedness above a defined threshold
- Create any additional security (negative pledge)
- Dispose of material assets above a defined threshold
- Make acquisitions above a defined threshold
- Pay dividends while in default, or subject to a leverage test
- Change the nature of its business materially
- Make changes to constitutional documents affecting Lender's rights

**Financial covenants** (tested quarterly or semi-annually):
- **Debt Service Coverage Ratio (DSCR)**: operating cash flow / debt service ≥ [1.20:1] or similar
- **Leverage ratio**: net debt / EBITDA ≤ [3.5:1] or similar
- **Interest coverage ratio**: EBITDA / interest expense ≥ [3.0:1] or similar
- Define each component carefully (EBITDA: add-backs; net debt: include/exclude shareholder loans)
- Equity cure: right for Borrower's shareholders to inject equity to cure a financial covenant breach (typically limited to 2 cures in the loan term)

### 10. Events of Default
Standard events triggering lender's acceleration rights:
1. **Non-payment**: failure to pay any sum when due (sometimes with a 3-5 day grace period)
2. **Financial covenant breach**: failing a financial covenant test
3. **Other covenant breach**: breach of any other obligation; 30-day cure period
4. **Misrepresentation**: any representation or warranty was false when made
5. **Cross-default**: default under any other financial indebtedness above a defined threshold
6. **Insolvency events**: filing, voluntary or involuntary; appointment of receiver or administrator; composition with creditors
7. **Enforcement of security**: any creditor enforces security against Borrower's assets
8. **Material adverse change (MAC)**: a change that materially adversely affects Borrower's ability to perform
9. **Change of control**: if control of Borrower changes without Lender's consent
10. **Unlawfulness**: it becomes unlawful for any Finance Party to perform its obligations

**Acceleration**: on Event of Default, Lender may declare the facility immediately due and payable, and enforce any security. Specify whether acceleration is automatic (on insolvency) or at Lender's election.

### 11. Security
Cross-reference to security documents (pledges, mortgages, guarantees) separately drafted. State:
- What security is given by which party over which assets
- When security is required to be perfected
- Cross-acceleration between loan and security documents

### 12. Governing law and dispute resolution
- DIFC/ADGM: full LMA-style documentation; English law; DIFC Courts or LCIA arbitration at DIFC
- UAE federal: UAE Commercial Transactions Law; onshore court proceedings or DIAC arbitration
- KSA: Sharia-compliant structure required for Islamic banks; Saudi law; SCCA or Saudi Commercial Court
- LB: Lebanese law; Beirut Court of Commerce; or ICC arbitration (common for international bank loans to Lebanese borrowers)

## Jurisdictional notes — Islamic finance (KSA, GCC)

Where Sharia compliance is required, the interest-bearing structure must be replaced:

| Structure | Description | Best for |
|-----------|-------------|---------|
| **Murabaha** | Bank purchases the asset and resells to client at cost-plus (disclosed margin); profit is the bank's return | Asset finance, trade finance |
| **Ijara** | Bank purchases asset and leases it to client; client makes lease payments; option to purchase at end of lease | Equipment, real estate, project finance |
| **Tawarruq** (commodity murabaha) | Synthetic structure using commodity sale chain to generate cash; widely used for unsecured financing | Working capital, personal finance |
| **Mudaraba** | Capital-provider and entrepreneur share profits per agreed ratio; losses borne by capital-provider | Investment partnerships |
| **Musharaka** | Joint ownership / equity participation; profits and losses shared | Project equity, real estate |

Islamic finance documents do not include an "interest rate" — they reference a "profit rate" or "rental rate." Avoid characterizing returns as interest in KSA-governed instruments.

Note: UAE federal interest law — Commercial Transactions Law (Federal Law 18/1993 as amended) regulates commercial interest; usury provisions limit excessive rates. EIBOR-linked commercial rates have generally been accepted. Verify with local counsel for current position.

## Key lender / borrower negotiation axes

| Point | Lender prefers | Borrower prefers |
|-------|---------------|-----------------|
| Financial covenant tightness | Tight ratios, frequent testing | Loose ratios, semi-annual testing, equity cure |
| Negative covenant thresholds | Low thresholds (more control) | High thresholds (operational flexibility) |
| MAC definition | Broad, subjective | Narrow, objective, specific events only |
| Cross-default trigger | Any default on any indebtedness | Only acceleration by another creditor, above threshold |
| Acceleration | Automatic on all events | At lender's election on all events except insolvency |
| Prepayment premium | Hard no-call for 2-3 years | None; free to prepay anytime |
| Margin ratchet | Fixed margin | Margin decreases as leverage improves |

## Common mistakes

- Incomplete or ambiguous EBITDA definition (add-backs create inflated covenant headroom)
- Vague MAC clause — borrowers use "objective test" arguments to dispute MAC determinations; lenders want subjective
- Missing cross-default threshold — a USD 50k default in a subsidiary triggering a USD 100m facility is commercially unreasonable
- Omitting the equity-cure mechanism when the borrower has private equity backers
- Not specifying which law governs each Security Document separately (security perfection is jurisdiction-specific)

## Related skills

- [[draft-guarantee]]
- [[draft-security-agreement]]
- [[draft-promissory-note]]
- [[review-financial-covenants]]
- [[draft-kyc-procedure]]
