---
name: prompt-pack-asset-purchase-agreement-sboghossian
title: Asset Purchase Agreement
description: Use when drafting an asset purchase agreement (APA) for a buyer to acquire specific assets or a business unit from a seller, rather than shares. Corporate M&A practice area; covers asset schedules, assumed/excluded liabilities, employee transfer obligations, contract assignment, purchase price allocation, and transition services — with MENA-specific attention to asset transfer mechanics, regulatory consents, and employment law considerations.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-asset-purchase-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# Asset Purchase Agreement

## When to use this

Use this skill when structuring and drafting an **asset purchase agreement** (APA) — a transaction in which the buyer acquires specific assets (and possibly assumes specific liabilities) rather than the entire legal entity. 

Asset purchase vs. share purchase: the key distinction is that in an asset purchase, the buyer chooses which assets to take and which liabilities to assume. Unassumed liabilities remain with the seller (subject to successor-liability doctrines in some jurisdictions). This makes asset purchases attractive when the target has unknown or contingent liabilities.

Relevant for:
- Acquiring a business unit or division without the parent entity
- Distressed asset sales (assets only, no legacy liabilities)
- Carve-outs from larger group transactions
- Acquiring specific IP, real estate, or equipment portfolios

---

## Prompt template

> Draft an asset purchase agreement for [Buyer] to acquire [describe assets/business unit] from [Seller]. Include asset schedules, excluded liabilities, employee transfers, contract assignments, purchase price allocation, and transition services.

Use [[conversation-clarifying-questions]] to elicit `[bracketed]` inputs before drafting.

---

## Required inputs

| Input | Why it matters |
|-------|---------------|
| Buyer and Seller names and jurisdictions | Determines governing law options; employment transfer obligations |
| Description of assets to be acquired | The heart of the APA — must be exhaustively defined |
| Description of assumed liabilities (if any) | What the buyer is taking on; critical for deal economics |
| Purchase price and payment structure | Fixed; earnout; deferred; escrow |
| Employee transfer approach | TUPE/equivalent transfer of undertakings obligations apply in many jurisdictions |
| Jurisdictions where assets are located | Multi-country asset transfers require local transfer formalities in each jurisdiction |
| Regulatory approvals required | Competition clearance; sector-specific approvals; foreign investment review |

---

## Optional inputs

- Transition services agreement requirement (will Seller continue to provide services post-closing?)
- IP licensing back to Seller (if Seller retains business that uses the IP being transferred)
- Real estate (owned vs. leased; assignment vs. new lease)
- Existing contracts to be assigned (consent requirements)
- Inventory and tangible assets (physical count at closing)

---

## Document structure

### 1. Parties and recitals
- Full legal names and jurisdiction of incorporation
- Recital: brief description of the business/assets being sold and the purpose of the transaction

### 2. Defined terms
Define with precision:
- **Acquired Assets**: the complete list (cross-reference to Schedule 1)
- **Excluded Assets**: expressly identify what is not being transferred (critical — ambiguity creates disputes)
- **Assumed Liabilities**: the specific liabilities the buyer is assuming (cross-reference to Schedule 2)
- **Excluded Liabilities**: everything not in Schedule 2 stays with Seller
- **Transferred Employees**: the employees whose employment transfers with the business

### 3. Purchase and sale of assets

#### 3.1 Assets schedule (Schedule 1)
An exhaustive, itemized schedule is essential. Categories:
- Tangible assets (plant, equipment, vehicles, inventory — attach inventory list as sub-schedule)
- Real estate (owned property — title deeds; leased property — lease assignments or new leases)
- Intellectual property (patents, trademarks, copyrights, trade secrets, domain names — attach IP schedule with registration details)
- Contracts (assigned contracts — attach list with counterparty, key terms, assignment consent status)
- IT systems and software licenses
- Goodwill (if transferring the business as a going concern)
- Regulatory licenses and permits (if transferable)
- Books and records relating to the acquired business

#### 3.2 Excluded assets (Schedule 3)
State clearly. Commonly excluded:
- Cash and cash equivalents
- Accounts receivable arising before the closing date
- Tax refunds and credits
- Corporate records of Seller relating to excluded operations
- Assets used by both the divesting business and Seller's retained business (address through transition services or IP license-back)

### 4. Assumed and excluded liabilities

#### 4.1 Assumed liabilities (Schedule 2)
Be specific. Commonly assumed:
- Obligations under assigned contracts arising after closing
- Liabilities to transferred employees arising after closing
- Accounts payable arising in the ordinary course of the acquired business before closing (if agreed)

#### 4.2 Excluded liabilities
All liabilities not expressly in Schedule 2 remain with Seller. Express the exclusion in general terms AND list specifically:
- Pre-closing tax liabilities
- Product liability claims arising from pre-closing sales
- Environmental liabilities (pre-closing contamination — significant in industrial asset sales)
- Employment claims arising from pre-closing acts
- Any litigation relating to the acquired business pre-closing

### 5. Purchase price

- **Amount**: clearly stated in currency; if earnout component, define the metrics, calculation methodology, payment timing, and dispute resolution
- **Allocation**: how is the price allocated among asset classes? Critical for tax — buyer and seller often have conflicting interests on allocation; sometimes a price allocation agreement is required
- **Escrow**: common for representations and warranties claims; define amount, duration, release conditions, and dispute mechanism
- **Adjustments**: net working capital adjustment at closing (target NWC + adjustment mechanism); inventory adjustment; earn-out

### 6. Representations and warranties

The seller makes representations about the assets, liabilities, and the acquired business. Key categories:
- Title to assets (seller has good title; assets are free of encumbrances)
- Condition of tangible assets (sufficient for the purposes for which they are used)
- IP (no known infringement; registrations current; no licenses that restrict buyer's use)
- Contracts (assigned contracts are valid; no defaults; no consent required [or consents will be obtained])
- Employees (list of employees is accurate; no undisclosed employment claims)
- Environmental (no known contamination; no pending environmental proceedings)
- Tax (no tax liens on assets; all taxes relating to the assets have been paid)
- No undisclosed liabilities assumed

Buyer's representations: authority to enter the APA; financing secured (if required).

### 7. Employee transfers

This is heavily jurisdiction-dependent:

| Jurisdiction | Employee transfer rule |
|-------------|----------------------|
| UAE (onshore) | No automatic TUPE equivalent; employment contracts must be re-signed with new employer; old employer must pay gratuity accrued to date of transfer; new employer starts gratuity fresh (unless parties agree to transfer gratuity liability) |
| DIFC | DIFC Employment Law: no automatic transfer; new contracts required; pay out DEWS/DIFC EWS benefits or agree to transfer |
| KSA | No TUPE equivalent; new contracts with new employer required; GOSI (social insurance) transfers manually; accrued employee rights with old employer must be settled |
| Lebanon | Labour Code: technically no automatic TUPE; practice varies; consider NSSF (social security) transfer implications |
| EU / UK | Transfer of Undertakings (Protection of Employment) Regulations (TUPE) — automatic transfer with existing terms and conditions; information and consultation obligations |
| France | Code du travail Art. L1224-1: automatic transfer of employment on transfer of a going concern |

In jurisdictions without automatic transfer: the APA must specify that Seller will terminate employees and pay all accrued entitlements, and Buyer will offer new employment to agreed employees. Agreed employees who decline the offer: Seller's responsibility.

### 8. Contract assignment

- Contracts that require third-party consent to assign: identify in the schedule; agreement to obtain consents before closing; what happens if consent is not obtained (closing condition? price reduction? carve-out?)
- Regulatory licenses: some licenses are personal and cannot be assigned; Buyer must re-apply (regulatory condition precedent)
- IP licenses: check the license agreement for assignment restrictions

### 9. Purchase price allocation

Different asset classes attract different tax treatment in most jurisdictions. Tax authorities may challenge allocations that are inconsistent with fair market values. Common allocation issues:
- Goodwill: tax treatment varies; in UAE (no corporate income tax on most businesses), allocation to goodwill may be neutral; in KSA or Egypt, allocation matters
- IP: IP allocated a high value may attract transfer pricing scrutiny if intra-group
- Inventory: allocated at cost vs. net realizable value
- Regulatory licenses: allocation value drives the stamp duty / registration fee in some jurisdictions (Egypt, Lebanon)

Consider attaching a purchase price allocation schedule as part of the APA, with both parties agreeing to use the same allocation for tax reporting.

### 10. Closing conditions and mechanics

- **Closing conditions**: regulatory approvals (competition, foreign investment, sector-specific); third-party consents for material contracts; no material adverse change; representations true at closing
- **Closing deliverables**: asset transfer instruments (bill of sale; IP assignment deeds; lease assignments; real estate transfer instruments per local law); officer's certificate; good-standing certificate; board resolution
- **Simultaneous exchange and completion** vs. **sign-now close-later**: if regulatory approvals are required, there will be a gap between signing and closing; deal protection (interim covenants, MAC definition) becomes critical

### 11. Transition services agreement
Where the Seller will continue to provide services to Buyer for a period post-closing (IT, finance, HR, logistics):
- Term (typically 6–24 months)
- Scope of services (detailed service schedule)
- Service levels
- Fees (cost-plus or market rates)
- Termination on notice

This is often a separate agreement but referenced in the APA.

### 12. Indemnification

- Seller indemnifies Buyer for: Excluded Liabilities; breaches of Seller representations; pre-closing tax liabilities
- Buyer indemnifies Seller for: Assumed Liabilities; Buyer's post-closing conduct
- Survival: representations survive closing for a defined period (typically 18–24 months for general reps; longer for title, tax, IP, environmental)
- Indemnification cap and basket (deductible): standard in M&A; negotiate based on deal size

### 13. Governing law and dispute resolution

Typically: the law of the Seller's or Buyer's jurisdiction or a neutral jurisdiction (DIFC, ADGM, English law). Arbitration clause recommended for cross-border transactions — see [[prompt-pack-arbitration-agreement-clause]].

---

## Jurisdictional notes

### UAE
Asset transfers in the UAE require specific transfer formalities depending on the asset type:
- Tangible assets: bill of sale; for registered assets (vehicles, equipment), re-registration at relevant authority
- Real estate: transfer through Dubai Land Department / Abu Dhabi DARI (mandatory form + fee + NOC from Seller's bank)
- Trademarks and IP: assignment deeds filed with MOCCAE / SAIP / relevant office
- Branches and commercial registrations: the business registration is personal to the Seller entity; Buyer must register its own entity

### KSA
- Asset transfers require registration with MISA (SAGIA) if foreign investment is involved
- Real estate: transfers via Real Estate Registry at Ministry of Justice
- Saudization (Nitaqat) obligations: if the business unit employs below the required Saudization percentage, this is an inherited regulatory issue — address in representations and conditions precedent

### Lebanon
- Real estate transfers: mandatory registration with the Real Estate Cadastre (Cadastre)
- Stamp duty: contracts above a threshold must be stamped (Ministry of Finance fee)
- Commercial registration: separate filing required for any assignment of the commercial registration or trade name

### Egypt
- Asset transfers: registration requirements vary by asset type
- Real Estate Registration Authority for property
- Company assets sold as a going concern may require GAFI approval if the acquiring entity is foreign
- Stamp duty applies to many commercial contracts

---

## Common mistakes

- Excluded liabilities list too vague — "all pre-closing liabilities" without specifics creates disputes; environmental liabilities and employment claims are frequently contested
- No consent condition for material contracts — buying a business without the key customer contract because consent was assumed and not obtained
- Employee transfer handled informally — no written record of which employees are transferring and on what terms
- No earnout dispute mechanism — earnout payments are one of the most litigated APA provisions
- Failure to allocate IP rights properly — particularly trade secrets and know-how, which have no formal registration to transfer

---

## Related skills

- [[prompt-pack-arbitration-agreement-clause]] — dispute resolution for the APA
- [[prompt-pack-agreement-legal-draft-review]] — reviewing an APA presented by the counterparty
- [[heuristic-always-state-jurisdiction-first]] — jurisdiction determines transfer formalities
- [[heuristic-no-us-style-boilerplate-in-civil-law-jx]] — adapt US-style APA for MENA civil law jurisdictions
- [[kb-corporate-mna-mena]] — MENA M&A regulatory and law reference
