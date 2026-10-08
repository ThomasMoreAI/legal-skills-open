---
name: workflow-investment-round-closing-pack-sboghossian
title: Investment Round Closing Pack
description: Use when closing an equity financing round — seed, Series A, or later stage — requiring the full suite of closing documents (SPA, Investors' Rights Agreement, Voting Agreement, ROFR/Co-Sale, Amended Articles, cap table, board resolutions, legal opinion, side letters). Covers the full closing workflow from signed term sheet through wire transfer and post-closing filings, with MENA-specific considerations for DIFC, ADGM, UAE, and KSA financing rounds.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/workflow/workflow-investment-round-closing-pack
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# Investment Round Closing Pack

## Purpose

This workflow orchestrates the documentation and process for closing an equity financing round. It is designed for company counsel (representing the startup) and investor counsel (representing the lead investor or syndicate). The workflow runs from a signed term sheet through all closing documents to final closing and post-closing obligations.

---

## Inputs

| Input | Required | Notes |
|-------|---------|-------|
| Signed term sheet | Yes | The foundation — all closing documents implement the term sheet |
| Company jurisdiction | Yes | DIFC, ADGM, UAE mainland, Delaware, etc. |
| Round type and amount | Yes | Seed, Series A, Bridge, etc.; total raise |
| Number of investors | Yes | Lead plus co-investors; each may require separate sub-documents |
| Current cap table | Yes | Pre-money; fully diluted including option pool |
| Lead investor entity details | Yes | For SPA parties, investor questionnaire |
| Special terms / side letters | If applicable | MFN, specific rights, observer seats |
| Company counsel and investor counsel | Yes | Coordinate document ownership |

---

## Closing Document Set

### Core Documents (All Rounds)

| # | Document | Purpose | Owner |
|---|----------|---------|-------|
| 1 | **Term Sheet** (executed) | [[draft-term-sheet-vc]] | Pre-closing; foundation |
| 2 | **Stock Purchase Agreement (SPA)** | [[draft-share-purchase-agreement]] adapted for new share issuance — purchase price, reps & warranties, conditions to closing | Company counsel draft |
| 3 | **Investors' Rights Agreement (IRA)** | Information rights (monthly financials, annual audit), registration rights, pro-rata participation, board observer rights | Company counsel draft |
| 4 | **Voting Agreement** | Board composition rights; drag-along provisions; exit triggers; protective provisions | Company counsel draft |
| 5 | **Right of First Refusal & Co-Sale Agreement** | ROFR on share transfers; co-sale right for investors to participate in founder share sales | Company counsel draft |
| 6 | **Amended & Restated Articles of Association** | Bakes all preferred share rights, protective provisions, and drag-along into the constitutional documents | Company counsel draft |
| 7 | **Amended & Restated Shareholders' Agreement** | [[draft-shareholders-agreement]] updated — incorporates new investor rights | Company counsel draft |
| 8 | **Disclosure Schedule** | Company's itemized carve-outs from the reps & warranties in the SPA | Company counsel compiles |
| 9 | **Cap Table** | Pre-money and post-money; fully diluted including options, warrants, SAFEs converting, new shares | Company CFO / counsel |
| 10 | **Board Resolutions** | Authorizing the round: new share issuance, execution of agreements, director appointments | Company secretary |
| 11 | **Stockholder Consents** | Required approvals from existing shareholders (typically: to amend articles, adopt voting agreement) | Company secretary |
| 12 | **Investor Questionnaire** | Confirms accredited/sophisticated investor status; AML/KYC representations | Investor completes |
| 13 | **Subscription Agreements** | Per-investor document confirming each investor's commitment and purchase details | Each investor |
| 14 | **Legal Opinion** | Company counsel opinion on: company authority to enter agreements; valid authorization; no conflicts | Company counsel |
| 15 | **Side Letters** | Investor-specific provisions (MFN, reporting rights variations, co-investment rights) | Per investor; company counsel |
| 16 | **Stock Certificates / Book Entries** | Evidence of new share issuance | Company secretary |
| 17 | **W-9 / BO Declarations** | Tax forms (for US entities); Beneficial Ownership declarations (for AML compliance in DIFC/ADGM/UAE) | Each investor |

### Additional Documents for Later-Stage Rounds (Series A+)

- **Registration Rights Agreement** (separate from IRA in larger rounds)
- **Management Rights Letter** (required by some US pension fund LPs to maintain ERISA exemption)
- **D&O Insurance binding** — if not already in place, typically required by institutional investors
- **Employment agreements for key founders** — investors often require locked-in employment terms as a condition

---

## Workflow Steps

### Step 1: Term Sheet Signed → Due Diligence (Weeks 1–3)

- Run [[workflow-full-due-diligence-pack]] in parallel with document drafting
- Identify any DD issues that require pre-closing remediation or specific indemnities
- Investors will not close if material DD issues are open

### Step 2: Definitive Agreement Drafting (Weeks 2–6)

Timeline: 4–6 weeks for standard rounds; 8–10 weeks for complex or multi-jurisdictional

1. Company counsel circulates first drafts of SPA, IRA, Voting Agreement, ROFR/Co-Sale
2. Lead investor counsel marks up and returns
3. Negotiation on key points:
   - Reps & warranties scope and survival period
   - Indemnification triggers and caps
   - Closing conditions (financing threshold, key-person conditions)
   - Board composition and protective provisions
   - Option pool (pre- vs. post-money; size)
4. Final agreed forms sent for execution

### Step 3: Disclosure Schedule Preparation (Parallel with Step 2)

- Company prepares the disclosure schedule — carve-outs from SPA representations
- Categories: corporate (pending litigation, IP encumbrances, related-party transactions, compliance gaps)
- A thorough disclosure schedule protects the company from rep breach claims; an inadequate one creates post-closing liability

### Step 4: Pre-Closing Mechanics (Week 5–6)

- All parties sign signature pages (wet or electronic — jurisdiction-specific rules)
- Board approvals held; resolutions signed
- Stockholder consents collected (deadlines: check Articles for any meeting/notice requirements)
- Investor questionnaires and AML/KYC documentation collected and cleared
- Beneficial ownership declarations filed where required (DIFC, ADGM, UAE mainland)

### Step 5: Closing Day

| Action | Responsibility | Timing |
|--------|--------------|--------|
| Confirm all signature pages collected | Coordinating counsel | Before wire |
| Confirm AML/KYC cleared for all investors | Compliance / counsel | Before wire |
| Investor wire transfer | Lead investor (then co-investors) | Closing day |
| Confirm wire receipt | Company CFO | Same day |
| Release escrow of signature pages (if used) | Escrow agent / counsel | On wire confirmation |
| Director appointments effective | Company secretary | On closing |
| Cap table updated | Company secretary / CFO | Same day or next business day |

### Step 6: Post-Closing (Weeks 1–4 after closing)

| Action | Deadline |
|--------|---------|
| Securities filing (Form D for US; foreign equivalents for non-US) | 15 days after first sale (US Form D); varies by jurisdiction |
| UBO/beneficial ownership declarations filed with relevant authority | Per jurisdiction timeline — DIFC: 14 days; UAE mainland: per Commercial Companies Law |
| Investor onboarding: investor portal access, reporting calendar, contact directory | 2 weeks post-close |
| Stock certificates / book-entry records issued | 2 weeks post-close |
| Post-closing actions calendar created | Week 1 post-close |
| D&O insurance policy confirmed in place | Week 1 post-close |
| 83(b) election filed (US only, if applicable) | 30 days from share issuance — critical and non-extendable |

---

## MENA-Specific Considerations

### DIFC

- DIFC companies are incorporated under DIFC Companies Law (DIFC Law No. 5 of 2018)
- English law governs; DIFC Courts have jurisdiction for any disputes
- DIFC Registrar of Companies must be notified of: share allotments (within 14 days), director changes, significant changes to the Articles
- UBO register maintained with DIFC Registrar; all UBOs holding 25%+ must be registered
- No securities regulatory approval required for private placement to sophisticated investors in DIFC

### ADGM

- ADGM Companies Regulations 2015; English law
- ADGM Registration Authority notified of allotments and constitutional changes
- Same UBO requirements as DIFC
- FSRA licensing may be required if the company conducts regulated financial services activities

### UAE Mainland

- Federal Law No. 32 of 2021 (Commercial Companies Law as amended) governs
- Foreign ownership: new law allows 100% foreign ownership in most sectors for companies incorporated under the new law; verify for specific sectors
- Share allotments must be registered with the relevant emirate's Economic Department
- Notarization: changes to Articles of Association may require notarization (attestation / Tawtheeq) — check with the Economic Department

### KSA

- Saudi Companies Law governs
- Foreign investment through an LLC or JSC requires MISA (Ministry of Investment) licensing
- Share transfers and new issuances must be registered with the Ministry of Commerce
- SAMA approval required if the company operates in any licensed financial services activity
- Sharia-compliant preferred share structures: standard liquidation preferences and dividend priority features may need review for Sharia compliance if any investor requires it

---

## Closing Checklist (Master)

- [ ] All definitive agreements fully negotiated and in agreed form
- [ ] All signature pages collected (wet or electronic; confirm validity in jurisdiction)
- [ ] Board resolutions executed
- [ ] Stockholder consents collected (or meeting held with quorum)
- [ ] Investor questionnaires and AML/KYC documentation complete and cleared
- [ ] Beneficial ownership declarations prepared
- [ ] Wire confirmations received from all investors
- [ ] Stock certificates / book-entry records issued or prepared
- [ ] Cap table updated and circulated
- [ ] Director appointments confirmed effective
- [ ] Disclosure schedule finalized and attached to SPA
- [ ] Post-closing actions calendar created with responsible parties and deadlines
- [ ] Tax forms collected (W-9, etc.) from all investors
- [ ] D&O insurance in place

---

## Critical Risk Points

| Risk | Description | Mitigation |
|------|-------------|-----------|
| Securities law compliance | Offering new securities without required exemption | Confirm applicable private placement exemption; file Form D or local equivalent |
| AML investor screening | Closing with a sanctioned or PEP investor | Full AML/KYC screen including OFAC, EU, UN sanctions check before close |
| Fiduciary duty / conflict | Director voting on a deal where they are conflicted as an investor | Declare conflict; recuse from board vote on the round |
| Option pool math | Option pool created pre-money dilutes founders more than post-money | Model the impact; negotiate whether the new pool is pre- or post-money |
| 83(b) election | Missing the 30-day window for US founders with unvested stock | Calendar immediately after share issuance; no extension possible |
| UBO filing deadline | Missing mandatory UBO filing | Calendar from day of incorporation or allotment |

---

## Related Skills

- [[draft-term-sheet-vc]]
- [[draft-shareholders-agreement]]
- [[draft-share-purchase-agreement]]
- [[workflow-startup-incorporation-pack]]
- [[workflow-full-due-diligence-pack]]
- [[wiki-vc-startups]]
