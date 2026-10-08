---
name: prompt-pack-share-purchase-agreement-sboghossian
title: Share Purchase Agreement
description: Use when a buyer is acquiring shares in a target company from selling shareholders, requiring a full share purchase agreement covering purchase price mechanics, representations and warranties, indemnification, conditions precedent, and closing mechanics. MENA-specific guidance covers UAE Commercial Companies Law requirements, DIFC/ADGM share transfer mechanics, KSA foreign investment approval requirements, notarization and regulatory filing obligations, and the treatment of civil-law limitations on warranty and indemnity structures.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-share-purchase-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# Share Purchase Agreement

## When to use this

Use this skill when:
- A buyer (corporate or individual) is acquiring 100% or a majority/minority stake in a private company through a share purchase.
- A partial stake acquisition requires documentation of share transfer mechanics, price adjustment, and seller representations.
- An M&A transaction has progressed to term sheet stage and a full SPA is needed.
- A private equity fund is executing an investment or exit transaction.

**Distinguish from:** An asset purchase agreement (acquires specific assets, not shares); a shareholders' agreement (governs ongoing governance after acquisition); a term sheet (non-binding commercial heads of terms).

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| **Buyer and seller identities** | Determines applicable foreign investment restrictions, regulatory approvals, and withholding tax | Ask |
| **Target company** | Name, jurisdiction, entity type, licensed activities | Ask |
| **Stake being acquired** | 100% / majority / minority; number and class of shares | Ask |
| **Purchase price structure** | Fixed; locked box; completion accounts; earn-out | Ask; this is the most commercially sensitive provision |
| **Key representations and warranties** | The seller's knowledge base; disclosure letter concept | Ask about the target's sector and any known issues |
| **Jurisdiction** | Determines regulatory approvals, share transfer formalities, stamp duty | Ask |

## Optional inputs

- **W&I insurance** — Warranty and Indemnity insurance is increasingly used in MENA M&A; affects how rep/warranty obligations are structured.
- **Escrow / holdback** — portion of price held in escrow to cover warranty claims; mechanics must be specified.
- **Earn-out provisions** — if part of the consideration is contingent on post-closing performance, a detailed earn-out schedule is needed.
- **Management equity rollover** — if management retains a stake, the SPA must address their continuing shareholder rights.

## Document structure

1. **Definitions and interpretation**
   - Comprehensive definitions section covering: Business Day, Closing, Closing Date, Condition, Consideration, Disclosure Letter, Encumbrance, Locked Box Date, Locked Box Accounts, Material Adverse Change (MAC), Purchase Price, Shares, Target Group, W&I Policy.

2. **Agreement to sell and purchase**
   - Seller agrees to sell and Buyer agrees to purchase [number] shares (representing [%] of the issued share capital of the Target) free from all Encumbrances, together with all rights attaching to those shares as at the Closing Date (including the right to all dividends declared after Closing).
   - State that seller has full title and authority to sell and transfer the shares.

3. **Purchase price and price adjustment mechanism**

   *Option A — Fixed price:*
   - Consideration of [AMOUNT] payable at Closing.
   - No post-closing adjustment.

   *Option B — Completion accounts:*
   - Estimated price at Closing based on a target working capital / net debt figure.
   - Post-closing completion accounts prepared within [60/90] days; adjustment (upward or downward) based on actual vs. target.
   - Dispute mechanism for completion accounts: accountant expert determination.

   *Option C — Locked box:*
   - Price fixed by reference to agreed balance sheet at the locked box date.
   - Protections against value leakage between locked box date and Closing (no dividends, no related-party payments, no unusual capex).
   - Interest runs on the purchase price from the locked box date.

   *Option D — Earn-out:*
   - Initial consideration at Closing.
   - Contingent earn-out payment based on post-closing EBITDA/revenue/KPI for [1/2/3 years].
   - Buyer's conduct obligations during earn-out period (operate business in ordinary course; not take actions to depress earn-out metrics).

4. **Conditions precedent**
   - List of conditions that must be satisfied before Closing is obligatory:
     - **Regulatory approvals:** UAE CBUAE/SCA/MOHRE consent if applicable; KSA SAGIA/MISA foreign investment approval; competition authority clearance if thresholds met; sector-specific licenses (DFSA, FSRA, VARA).
     - **Third-party consents:** key commercial contracts with change-of-control clauses; landlord consents.
     - **Seller warranties still accurate** at Closing date.
     - **No Material Adverse Change** having occurred.
   - Long stop date: if conditions not satisfied by [date], either party may terminate.
   - Obligation to use reasonable/best endeavors to satisfy conditions.

5. **Pre-closing obligations**
   - Seller's conduct of business obligations between signing and Closing: operate in the ordinary course; no material new contracts; no disposal of assets; no changes to employee compensation above a threshold.
   - Buyer's access rights during the pre-closing period (limited; sellers resist broad access before Closing in MENA practice).

6. **Closing mechanics**
   - Date and place of Closing.
   - Closing deliverables — Seller:
     - Share transfer form(s) executed and stamped (where applicable).
     - Resignation letters of departing directors.
     - Signed board/shareholder resolutions approving the transfer (see Jurisdictional notes for specific requirements).
     - Disclosure Letter countersigned.
     - Power of attorney (if Seller is acting through an attorney).
   - Closing deliverables — Buyer:
     - Payment of the purchase price by wire transfer.
     - New director appointment letters / board resolutions.
   - Simultaneity: all Closing deliverables must be exchanged simultaneously (not sequential).

7. **Representations and warranties (Seller)**
   - **Title warranties:** Seller owns the shares free and clear; no liens, pledges, or encumbrances; no options or rights of first refusal in favor of third parties outstanding.
   - **Capacity and authority:** Seller has capacity; no regulatory restriction on sale.
   - **Corporate warranties (Target):**
     - Incorporation and good standing; licenses current and valid.
     - Accounts: Last audited accounts fairly present the financial position; no material deterioration since accounts date.
     - No undisclosed liabilities.
     - Compliance with applicable laws (tax, employment, environmental, sector-specific).
     - No material litigation or regulatory proceedings pending or threatened.
     - Employees: list of employees; no undisclosed disputes; employment contracts compliant with applicable labor law.
     - IP: Target owns or has valid licenses for all IP used in the business; no infringement claims.
     - Real property: title, lease status.
     - Tax: all tax returns filed; no outstanding tax assessments or disputes; EOSG accruals (UAE/KSA) fully provisioned.
   - **Disclosure Letter:** qualifications to the warranties set out in the Disclosure Letter; Seller is only liable for warranty claims to the extent not disclosed.

8. **Indemnification**
   - **General indemnity:** Seller indemnifies Buyer against losses arising from breach of warranty or covenant.
   - **Specific indemnities:** tax indemnity (pre-closing tax liabilities); environmental indemnity (pre-closing contamination); pension indemnity (pre-closing pension deficits); litigation indemnity (known disputes).
   - **Limitations:**
     - De minimis: individual claims must exceed [USD 25,000 / AED 100,000].
     - Basket/deductible: aggregate claims must exceed [0.5% / 1%] of purchase price before Seller liable; either a "first dollar" (true deductible) or "excess" basket.
     - Cap: aggregate indemnity liability capped at [15–20%] of purchase price (except for fraud and fundamental warranties: title, capacity, tax — capped at 100%).
     - Time limits: general warranties — [18 months / 2 years] from Closing; tax warranties — [7 years / applicable limitation period]; fundamental warranties — 10 years.
   - **MENA note:** W&I insurance is available in MENA M&A transactions (primarily Dubai-based risks); if used, adjust the indemnity structure so most warranty claims are directed against the W&I policy rather than the Seller.

9. **Post-closing obligations**
   - Seller and Buyer each undertake to take all steps to complete the transfer formalities in the relevant company registry.
   - Non-compete by Seller (for an agreed period; see Jurisdictional notes on enforceability).
   - Transitional services agreement: if Seller provides transitional services to Target post-Closing.

10. **General provisions** — confidentiality, announcements (coordinated press release), governing law, dispute resolution, entire agreement, assignment (Buyer may assign to an affiliate; Seller may not assign).

## Jurisdictional notes

### UAE — onshore LLC
- UAE Federal Decree-Law No. 32 of 2021 on Commercial Companies: LLC share transfers require an amendment to the Memorandum of Association (MOA) notarized before a UAE notary public.
- Register the updated MOA with the Department of Economic Development (DED) or relevant emirate commercial register within 30 days.
- Foreign ownership: 100% foreign ownership is permitted in most sectors following 2020 reforms; some sectors (defense, telecom, media) retain restrictions.
- MOHRE approval: certain regulated activities require MOHRE or sector regulator consent on change of control.

### DIFC
- DIFC Companies Law (DIFC Law No. 5 of 2018): share transfers effected by completing a standard stock transfer form; update the register of members within the company.
- No stamp duty on share transfers in DIFC.
- DFSA: if Target is a DFSA-licensed entity, a change in ownership above a threshold requires DFSA prior approval.

### KSA
- MISA approval required for foreign investors acquiring stakes in Saudi companies; specific approval timelines and foreign investment restrictions apply per sector.
- Share transfers in an LLC require amending the articles of association before a Saudi notary.
- CMA approval required for acquisitions in listed companies or acquisition of a 10%+ stake in a listed company.
- Arabic language: all transfer documents, amended articles, and regulatory filings must be in Arabic.

### Lebanon
- Share transfers in SAL require: board approval; amendment of articles; registration with the Companies Register (Registre du Commerce).
- Capital controls (since 2019): restrictions on certain cross-border transfers; dollar payments into Lebanon face practical banking constraints.

### Egypt
- Share transfer in an SAE or LLC: notarized transfer deed; update at GAFI (General Authority for Investment and Free Zones) or Companies Registry.
- Foreign investment: GAFI-registered companies may freely transfer shares to foreign buyers in most sectors; strategic sectors require approval.

## Drafting standards

- The representations and warranties are the commercial heart of the transaction; work through them systematically against the target company's actual business.
- The Disclosure Letter is as important as the SPA itself; ensure the Seller provides a comprehensive disclosure letter to cap warranty exposure.
- For MENA civil-law jurisdictions: the indemnification structure (specific indemnity + warranty claim) maps onto civil-law damages concepts but may need to be adapted; avoid US-style rescission rights unless the transaction truly warrants them.
- Limitation of liability provisions for warranties: MENA civil law does not restrict indemnity caps as heavily as some common-law courts; commercial parties have reasonable freedom to set these.

## Common mistakes

- **No EOSG provisioning warranty.** In UAE and KSA transactions, sellers must warrant that EOSG for all employees has been fully accrued; failure to do so creates hidden liability.
- **Conditions not linked to a long stop date.** Without a long stop date, the SPA can hang open indefinitely while regulatory approvals are awaited; include a long stop and force-majeure-style MAC-out provisions.
- **Earn-out mechanics without conduct protections.** An earn-out is worthless to the seller without meaningful restrictions on the buyer's post-closing conduct of the business.
- **Share transfer formalities underestimated.** In UAE LLC and KSA transactions, the notarization and registry filing requirements add time and cost; plan for 2–4 weeks for these steps post-Closing.

## Related skills

- [[prompt-pack-shareholders-agreement]]
- [[prompt-pack-shareholder-agreement-key-terms]]
- [[prompt-pack-shareholders-resolution]]
- [[prompt-pack-standard-nda]]
- [[heuristic-always-state-jurisdiction-first]]
