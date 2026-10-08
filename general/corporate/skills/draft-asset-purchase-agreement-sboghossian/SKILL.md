---
name: draft-asset-purchase-agreement-sboghossian
title: Draft — Asset Purchase Agreement
description: Use when asked to draft an Asset Purchase Agreement (APA) for an M&A transaction structured as an asset deal rather than a share deal. Covers the asset/liability split mechanics, purchase price allocation, contract assignment, employee transfer (TUPE/ARD and MENA equivalents), IP recordation, and jurisdictional nuances for UAE, KSA, Lebanon, DIFC, ADGM, EU, and US. P0 priority — asset deal structure has major tax and liability consequences.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-asset-purchase-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# Draft — Asset Purchase Agreement

## When to use this

Use this skill when a buyer and seller are structuring an acquisition as an asset deal — the buyer purchases specific identified assets (and assumes only specified liabilities) rather than acquiring the target company as a whole entity.

### Asset deal vs share deal — the fundamental choice

| Dimension | Asset deal | Share deal |
|---|---|---|
| What buyer gets | Specific listed assets only | Entire entity (all assets and liabilities) |
| Liability exposure | Buyer chooses which liabilities to assume | Buyer inherits all historic liabilities |
| Tax basis | Fresh start — stepped-up basis on acquired assets | Carried-over historic tax basis |
| Transfer complexity | High — each asset class needs separate transfer mechanics | Low — shares transfer by simple agreement |
| Third-party consents | Required for most contracts and licenses | Not required (change of control clauses aside) |
| Employment | Buyer hires; TUPE/ARD or equivalent applies | Employees transfer with entity |
| Stamp duty / transfer taxes | Varies by asset class and jurisdiction | Often single transaction; may be lower |

**When asset deal is preferred**: distressed assets (leaving liabilities behind), regulatory licenses not transferable at entity level, clean slate on tax, targeted acquisition of specific assets only.

## Required inputs

| Input | Notes |
|---|---|
| Buyer and Seller (full legal details) | Including registration numbers and signing authority |
| Assets to be acquired (granular list) | Real estate, equipment, IP, contracts, inventory, receivables, goodwill, permits, data |
| Excluded assets | Assets explicitly remaining with Seller |
| Assumed liabilities | Specific liabilities Buyer agrees to take on |
| Excluded liabilities | All other liabilities remain with Seller |
| Purchase price | Fixed vs variable (earn-out); currency; payment mechanism |
| Purchase price allocation | Across asset categories — tax-critical |
| Employee transfer mechanism | Which employees; on what terms; TUPE or equivalent |
| Governing law and seat | Determines tax treatment, transfer formalities, and enforcement |

## Document structure

### 1. Definitions
Define all asset categories by reference to a schedule. Define "Acquired Assets," "Excluded Assets," "Assumed Liabilities," "Excluded Liabilities," "Closing Date," "Business Day," etc.

### 2. Sale and purchase of assets
The core operative clause:
> "Subject to the terms and conditions of this Agreement, at Closing, Seller hereby sells, transfers, conveys, assigns, and delivers to Buyer, and Buyer hereby purchases and acquires from Seller, all of Seller's right, title, and interest in and to the Acquired Assets, free and clear of all Encumbrances other than Permitted Encumbrances."

### 3. The asset schedules

**Schedule 1 — Acquired Assets (granular)**
- **Real estate**: legal description of each property; title reference; zoning classification.
- **Tangible personal property**: equipment list (serial numbers for high-value items); inventory as of Closing (valued at cost or lower of cost and net realizable value).
- **Intellectual property**: patents (listed by jurisdiction, number, expiry), trademarks (registered and unregistered; classes; jurisdictions), copyrights, trade secrets, domain names, software source code, data.
- **Contracts**: list of assigned contracts with counterparty name, date, subject; note which require consent.
- **Accounts receivable**: outstanding as of Closing.
- **Permits and licenses**: list; note which are transferable vs non-transferable.
- **Books and records**: customer lists, technical documentation, financial records relating to the business.
- **Goodwill**: description of the business being transferred.

**Schedule 2 — Excluded Assets**
- Cash and cash equivalents.
- Intercompany receivables.
- Any specific assets the seller retains.
- Tax refunds relating to pre-closing periods.
- Certain named contracts (if seller retains them).

**Schedule 3 — Assumed Liabilities**
- Specific trade payables (listed).
- Employee liabilities from and after Closing.
- Liabilities under assigned contracts arising from and after Closing.
- Identified warranty obligations for post-Closing sales.

**Schedule 4 — Excluded Liabilities**
> "All liabilities other than the Assumed Liabilities are Excluded Liabilities, including without limitation: (a) any taxes of Seller for pre-Closing periods; (b) any litigation, claims, or regulatory proceedings arising from pre-Closing events; (c) any undisclosed liabilities; (d) any employee liabilities relating to pre-Closing periods..."

### 4. Purchase price
- **Fixed price**: state currency and amount.
- **Adjustments**: working capital adjustment mechanism (target, peg, methodology); earn-out provisions.
- **Closing payment**: wire transfer on Closing Date; escrow portion (typically 10–15% for 12–24 months).
- **Purchase price allocation**: each asset category receives a portion of the total price — this allocation drives the tax treatment for both parties. Methodology must be agreed in the agreement; form filing required in US (Form 8594 under IRC Section 1060); similar requirements in other jurisdictions.

### 5. Representations and warranties of Seller
- **Organization and authority**: Seller is duly organized; has authority to sell.
- **Title to assets**: Seller has good and marketable title; assets are free and clear of encumbrances.
- **Condition of assets**: tangible assets in good working order, except as disclosed in schedules.
- **IP ownership**: Seller owns or has valid licenses to all IP; no third-party infringement claims pending.
- **Material contracts**: listed contracts are valid and binding; no material breaches; no consent required except as disclosed.
- **Assigned contracts — assignability**: each listed contract is assignable without consent, or the required consents have been obtained.
- **Employees**: list of transferring employees; no undisclosed employment liabilities; no pending claims.
- **Compliance with law**: no material violations.
- **Taxes**: all taxes paid current through Closing; no undisclosed tax liabilities.
- **Litigation**: no pending litigation relating to the Acquired Assets.
- **Financial statements**: where a carve-out business, financial statements are fairly presented.

### 6. Representations and warranties of Buyer
- Organization and authority.
- Financing available.
- No governmental approval required (other than disclosed).

### 7. Covenants
- **Pre-closing covenants**: Seller operates the business in ordinary course; no material transactions outside ordinary course without Buyer consent; Seller maintains assets; Seller obtains required consents.
- **Buyer access**: Seller grants Buyer access to books, records, and employees for confirmatory due diligence.
- **Confidentiality**: both parties during negotiation.
- **Post-closing covenants**: Seller provides transition services; Seller assists with IP recordation filings; non-compete / non-solicit (Seller and key principals — see enforceability notes).

### 8. Conditions to Closing
- **Conditions to both parties**: no legal prohibition on Closing; no MAC.
- **Conditions to Buyer's obligations**: representations and warranties true at Closing; covenants performed; material consents obtained; no material adverse change (MAC).
- **Conditions to Seller's obligations**: representations and warranties of Buyer true; Buyer's covenants performed; Purchase Price delivered.

### 9. Closing mechanics
- **Date and location**: specified or determinable.
- **Seller's deliverables at Closing**:
  - Bill(s) of sale for tangible assets.
  - IP assignment agreements (recordable form).
  - Real estate deeds or transfers.
  - Contract assignment and assumption agreements for each assigned contract.
  - Officer's certificate as to representations, warranties, and covenants.
  - Resignation letters of departing officers/directors.
- **Buyer's deliverables at Closing**:
  - Purchase price wire transfer.
  - Assumption agreement for Assumed Liabilities.
  - Officer's certificate.

### 10. Indemnification
- **Seller indemnifies Buyer** for: breaches of representations and warranties; Excluded Liabilities; failure to perform covenants.
- **Buyer indemnifies Seller** for: breaches of Buyer reps/warranties; Assumed Liabilities; Buyer's failure to perform post-Closing.
- **Cap and deductible**: rep/warranty claims typically capped at 10–25% of purchase price; deductible / basket (1–2% of purchase price). Fundamental reps (title, authority, taxes) often uncapped.
- **Survival period**: reps and warranties survive for 12–24 months post-Closing (longer for IP, employment, taxes, fundamental reps).
- **Indemnification as exclusive remedy**: typical; carve out for fraud and willful misconduct.

## Employee transfer

### EU (TUPE / ARD)
- Transfer of Undertakings (Protection of Employment) Directive / Acquired Rights Directive: employees transfer automatically on same terms; Seller must inform and consult employee representatives.
- Buyer cannot change terms and conditions materially for a period post-transfer.

### MENA jurisdictions
- **UAE (Federal Decree-Law 33/2021)**: employer change is technically a new employment contract; best practice is for Buyer to offer equivalent terms; Seller must settle all end-of-service gratuity accrued to Closing; Buyer's gratuity clock starts at Closing.
- **KSA (Labour Law)**: similar — new employer contract; seller settles all GOSI and gratuity obligations pre-closing; transfer agreement.
- **LB**: employer transfer requires Labor Ministry notification; employee has right to terminate with full indemnity if materially disadvantaged.
- **Practical approach**: identify transferring employees; Seller terminates with settlement (EOSB paid); Buyer hires on new (equivalent) terms.

## IP transfer and recordation

- **Patents**: assignment agreements must be recorded with each relevant national IP office (USPTO, EUIPO, GCC Patent Office, national offices).
- **Trademarks**: trademark assignment recorded with each relevant office; fee per class per jurisdiction.
- **Domain names**: WHOIS transfer via registrar; administrative process.
- **Software**: copyright assignment; escrow of source code if mission-critical.
- **Data**: data transfer must comply with applicable data protection law (GDPR, UAE PDPL, Saudi PDPL); customer data requires legal basis for transfer.

## Jurisdictional notes

### UAE
- Real estate transfer: requires land department registration (DLD for Dubai; relevant emirate authority elsewhere); transfer tax / fees apply.
- IP transfer: registered with Ministry of Economy (trademarks); WIPO for international marks via Madrid Protocol.

### KSA
- Real estate: transfer via Notary Public and Real Estate General Authority; stamp duty.
- Business transfer: notification to Ministry of Commerce; some sectors require MISA approval.

### DIFC / ADGM
- Clean common-law asset sale; no additional registry filings beyond standard IP and real estate.
- Asset sale by a DIFC/ADGM entity may require DIFC/ADGM Court or Registrar notification if part of a business wind-down.

### US
- **Form 8594** (Asset Acquisition Statement under IRC Section 1060): both parties must file with their tax returns; the allocation must agree.
- **Bulk sales**: some US states require bulk-sale notice to Seller's creditors; check applicable state law.
- **HSR filing**: if the deal size and parties exceed Hart-Scott-Rodino thresholds, pre-closing antitrust filing required.

## Common mistakes

- **Vague asset list**: the APA is only as good as Schedule 1; ambiguity about what transfers is the source of most post-closing disputes.
- **Forgotten contract consents**: many commercial contracts have anti-assignment clauses; failure to obtain consent means the contract does not legally transfer and the Buyer has no rights under it.
- **IP not recorded**: legal ownership of IP transfers upon signing, but priority against third parties requires recordation; missing this window can result in loss of rights.
- **Employee gratuity not settled**: leaving EOSB accruals unsettled at Closing creates Excluded Liability disputes.
- **No MAC definition**: without a defined MAC standard, Buyer has no clear right to walk away if the business deteriorates between signing and Closing.

## Related skills

- [[draft-contract-skeleton-builder]]
- [[draft-boilerplate-clauses]]
- [[draft-board-resolution]]
- [[review-contract-general]]
- [[draft-bilingual-ar-en-side-by-side]]
