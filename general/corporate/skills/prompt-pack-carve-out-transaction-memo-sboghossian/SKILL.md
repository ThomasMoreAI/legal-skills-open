---
name: prompt-pack-carve-out-transaction-memo-sboghossian
title: Carve-Out Transaction Memo
description: Use when a lawyer or corporate advisor needs to draft a strategy memo for a parent company planning to carve out and divest a business unit. Covers legal entity restructuring, separation of shared services, IP and contract assignments, employee transfers, tax structuring, and regulatory approvals. Relevant across MENA (UAE, KSA, LB, EG), DIFC/ADGM, EU, and UK jurisdictions where carve-out complexity varies significantly between civil-law and common-law frameworks.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-carve-out-transaction-memo
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# Carve-Out Transaction Memo

A carve-out is structurally among the most complex M&A transactions: the seller must simultaneously create a stand-alone business and execute a sale. This skill produces a strategy memo that advisors use to plan and sequence the full lifecycle of a carve-out, from pre-signing separation through post-closing transition.

## When to use this

- A parent company is selling a division, subsidiary, or product line and needs a written strategy memo for board, management, or deal team alignment.
- The legal team needs to identify and sequence all legal workstreams before signing a term sheet.
- A buyer wants to understand the legal complexity of a proposed carve-out target before committing to a price.
- The deal team is preparing for regulatory filings or competition clearances that require a clear separation narrative.

## Required inputs

| Input | Why it matters | Sensible default |
|---|---|---|
| Parent company name and jurisdiction of incorporation | Determines governing law for the separation steps | Ask the user |
| Business unit being carved out | Defines perimeter of the transaction | Ask the user |
| Target closing structure (asset deal vs. share deal) | Determines whether entity creation is needed pre-signing | Ask the user; default to share deal if an entity already exists |
| Governing jurisdictions (countries of operation) | Drives regulatory approvals, employee transfer rules, and tax structuring | Ask the user |
| Indicative deal value or size band | Shapes regulatory thresholds (merger control, FDI) | Not required for memo structure, but note it if known |
| Target timeline to signing / closing | Reveals whether pre-signing separation steps are feasible | Ask the user |

## Optional inputs

- Identity of buyer (financial vs. strategic) — shapes exclusivity and TSA negotiating posture.
- Existing third-party contracts in the business unit — flags assignment consent requirements.
- Shared IT / HR / finance systems — defines scope of Transitional Services Agreement (TSA).
- Current employee headcount by jurisdiction — required for TUPE / equivalent worker-transfer analysis.
- Regulatory licenses held by the business unit — some licenses do not transfer; new applications may be needed.

## Memo structure

A carve-out strategy memo for a corporate partner should be structured as follows:

### 1. Transaction overview
- Description of the business unit, its legal and operational perimeter, and the proposed deal structure (asset vs. share deal, with or without a NewCo).
- Key transaction milestones: pre-signing separation, signing, regulatory clearances, closing, TSA period.

### 2. Legal entity restructuring
- Whether the business unit sits in a dedicated legal entity or must first be carved into one (contribution en nature / hive-down).
- Steps to create a NewCo, including capitalization, directors/managers, and registration timeline in each jurisdiction.
- In civil-law jurisdictions (UAE federal, KSA, LB, EG), note that hive-downs may require notarized asset-contribution agreements and court or ministry approval; allow 6–12 weeks.
- In DIFC/ADGM, a common law Share Sale Agreement can be executed quickly but the DIFC Registrar must approve transfers of shares in DIFC entities.

### 3. Separation of shared services
- Identify shared functions: finance, HR, IT, legal, procurement, real estate.
- Scope the Transitional Services Agreement (TSA): which services the parent provides post-closing, at what cost, for how long (typically 12–24 months).
- Identify reverse TSA services the carved-out business provides back to the parent.
- Note any "stranded costs" the parent will bear after separation.

### 4. IP and contract assignments
- Map all IP (patents, trademarks, software, domain names, trade secrets) used by the business unit: owned outright, licensed in from parent, or licensed to third parties.
- Identify which licenses require third-party consent to assign. Counterparty consent rights are common; budget time and negotiation leverage.
- In MENA, trademark registrations are territorial — registration in UAE does not cover KSA; confirm status in each country of operation.
- Draft an IP assignment or license-back agreement where the parent retains IP that the carved-out business will still need.

### 5. Employee transfers
- In jurisdictions with automatic transfer protections (UAE Labor Law, KSA Labor Law, Lebanese Labor Code, DIFC Employment Law, EU TUPE equivalent):
  - Identify employees by entity, location, and contract type.
  - Flag employees on Saudi Nitaqat quotas, UAE Emiratization requirements, or Lebanese labor ministry registrations — transfers may require regulatory notification.
  - Draft employee notification letters; some jurisdictions require individual consent.
  - Allocate pension / end-of-service gratuity (ESG) liability: MENA jurisdictions impose statutory ESG obligations; allocate accrued ESG to the seller through closing date.

### 6. Tax structuring
- Assess the cleanest legal route to achieve the desired tax outcome:
  - Asset deal: may trigger VAT (UAE 5%, KSA 15%, EG 14%), stamp duty (LB), and transfer taxes. Some jurisdictions have exemptions for going-concern transfers.
  - Share deal: often more tax-efficient for the seller; buyer gets no step-up in asset base.
  - Holding company interposition: check CFC rules and withholding tax on dividends/royalties in each jurisdiction.
- Identify any internal restructuring steps needed before signing to achieve the optimal structure; timing relative to fiscal year-end matters.
- Flag deferred tax liabilities embedded in the carved-out entity.

### 7. Regulatory considerations
- **Merger control:** Assess filing thresholds in all countries of operation. GCC countries (UAE, KSA) have national competition authorities. EG has the Egyptian Competition Authority. Identify multi-jurisdictional filings that could extend timeline.
- **Foreign investment screening:** UAE, KSA, and EG have FDI restrictions in certain sectors. Identify any restricted sectors and whether ministerial approvals are needed.
- **Sector-specific licenses:** Banking, insurance, telecoms, and healthcare licenses in MENA typically do not transfer with a share deal and require fresh applications or change-of-control notifications.
- **Antitrust / competition:** If the buyer is a competitor, prepare a competition assessment early; information-barrier protocols (clean team) may be required pre-signing.

### 8. Key risks and mitigations

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Third-party consent to contract assignment refused | Medium | High | Early outreach; negotiate deal-specific carve-outs in SPA |
| Regulatory approval delay | Medium | High | Parallel-path filings; long-stop date in SPA |
| Employee objections or claims | Medium | Medium | Clear communications plan; ESG accrual indemnity |
| IP ownership gap discovered | Low | High | IP audit at outset; clean-room protocol |
| TSA disputes post-closing | Medium | Medium | Detailed TSA with service-level metrics and exit-assist obligations |

### 9. Recommended workstreams and timeline
Provide a phased timeline:
- **Phase 1 (Pre-signing, weeks 1–8):** Legal entity analysis, IP audit, employee mapping, regulatory pre-assessment, TSA scoping.
- **Phase 2 (Signing to closing, weeks 8–24+):** Regulatory filings, employee consultations/notifications, contract assignment requests, NewCo formation.
- **Phase 3 (Post-closing, months 1–24):** TSA management, IP migration, system cutover, stranded-cost wind-down.

## Jurisdictional notes

| Jurisdiction | Key carve-out traps |
|---|---|
| UAE (onshore) | Hive-down requires MoE approval; Emiratization quotas transfer with employees; VAT grouping must be updated |
| UAE (DIFC) | DIFC Registrar approval for share transfers; Employment Law Art. 59 on business transfers |
| KSA | Saudization (Nitaqat) carries over; Ministry of Commerce approval for LLC share transfers to foreigners |
| Lebanon | Stamp duty on asset transfers; end-of-service indemnity under Labor Code must be ring-fenced |
| Egypt | Investment Authority (GAFI) involvement for certain FDI structures; VAT at 14% on asset transfers |
| EU/UK | TUPE or equivalent mandatory; automatic transfer of contracts and employees |
| OHADA | Fonds de commerce transfer requires publication and 10-day creditor opposition period |

## Drafting standards

- No `[INSERT X]` placeholders in the final memo — call out all open items as numbered action points with responsible party and deadline.
- Cite governing law by reference to the named statute or decree-law; do not invent article numbers.
- Use plain language for executive summary sections; reserve technical language for legal workstream annexes.
- State assumptions prominently at the top of the memo.

## Common mistakes

- Treating a carve-out as a simple share sale — the separation workstream is as important as the transaction documents.
- Ignoring statutory ESG / end-of-service gratuity accruals, which can be a material liability in MENA.
- Failing to assess license transferability early enough to avoid deal-breaking delays.
- Underestimating TSA complexity — under-scoped TSAs are the leading cause of post-closing disputes in carve-outs.
- Overlooking the interplay between Nitaqat/Emiratization and post-closing headcount changes.

## Related skills

- [[prompt-pack-due-diligence-checklist]]
- [[prompt-pack-share-purchase-agreement]]
- [[prompt-pack-business-transfer-agreement]]
- [[prompt-pack-employees-transfer-tupe]]
- [[prompt-pack-transitional-services-agreement]]
