---
name: workflow-startup-incorporation-pack-sboghossian
title: Startup Incorporation Pack
description: Use when incorporating a new startup — producing the full foundational document set (Articles of Association, Shareholders' Agreement, Founders' Agreement, vesting schedules, IP assignment, ESOP, board resolutions, NDA templates, privacy policy, bank account kit) and guiding the jurisdiction selection decision across DIFC, ADGM, UAE-onshore, KSA, Delaware, and Singapore. Covers MENA-specific registration steps (Qiwa, MOHRE, NSSF) and critical first-90-days actions (IP assignment, 83(b) election, option pool).
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/workflow/workflow-startup-incorporation-pack
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# Startup Incorporation Pack

## Purpose

This workflow orchestrates the complete incorporation and foundational legal setup for a new startup. It produces all core documents, guides the jurisdiction selection decision, walks through government registrations, and flags the critical actions that must happen within the first 90 days (missing them creates expensive remediation problems later).

---

## Inputs

| Input | Required | Notes |
|-------|---------|-------|
| Founder name(s) and nationalities | Yes | Nationalities affect which jurisdictions are practically accessible |
| Business description | Yes | What the company does; its product and target market |
| Target markets | Yes | Where the company will operate and sell |
| Intended investment path | Yes | VC-backed? Bootstrap? Government grant? Determines jurisdiction priority |
| Number of co-founders and proposed equity split | Yes | Drives shareholders' agreement and vesting |
| Any existing IP to be contributed | If applicable | Must be formally assigned to the company |
| Desired name(s) | Yes | Name clearance check needed before proceeding |
| Budget for incorporation | Recommended | Government fees, legal fees, registered office costs vary significantly |

---

## Logic — Step 1: Jurisdiction Selection

This is the most consequential first decision. Load [[research-jurisdiction-comparison]] for a full analysis. Summary:

### Jurisdiction Comparison Matrix

| Jurisdiction | Best for | Legal system | VC ecosystem | Cost | Foreign ownership |
|-------------|---------|-------------|-------------|------|-----------------|
| **DIFC (Dubai)** | Tech startups; fintech; any VC-backed startup | English law (DIFC Contract Law, Companies Law) | Strong; many VCs present; standard USD cap tables | Moderate-high annual fees | 100% foreign |
| **ADGM (Abu Dhabi)** | Digital assets; crypto; asset management; fintech | English law (ADGM Companies Regulations) | Growing; Abu Dhabi government support | Similar to DIFC | 100% foreign |
| **Delaware (US)** | US-bound startups; YC companies; US VCs required | Delaware General Corporation Law | Essential for US VCs | Low initial cost; annual franchise tax | 100% foreign |
| **Singapore** | ASEAN market access; alternative to HK | Singapore Companies Act; English law | Strong ecosystem | Moderate | 100% foreign (in most sectors) |
| **UAE mainland** | UAE market-focused; government contracts; retail | UAE Federal Companies Law | Improving but less VC-native | Low to moderate | Varies by sector; liberalization progressing |
| **KSA (LLC)** | KSA market-focused; Vision 2030 sectors | Saudi Companies Law; Sharia overlay | Growing; SVC, Sanabil active | Moderate; MISA required | 100% with MISA license (most sectors) |
| **Lebanon** | Cost-efficiency; local market; talent access | Lebanese Commercial Code | Very limited post-2019 crisis | Very low | 100% (most sectors) |

**Decision heuristic:**
- Planning to raise from international VCs → DIFC first (English law, enforceability, familiar to investors); Delaware if US VC only
- Digital assets / crypto → ADGM (most progressive regulatory framework in MENA for virtual assets)
- KSA market only → KSA LLC; pair with a DIFC holding company for IP and international activities
- Bootstrapped / local-only → UAE mainland or KSA depending on target market
- Lebanon-based team → DIFC or ADGM holding company + Lebanon branch/subsidiary for operations

---

## Logic — Step 2: Name Reservation and Clearance

Before any document drafting:

1. **Availability check** in target jurisdiction's company registry
2. **Trademark clearance search** — check the name is not registered by a third party in relevant Nice classes and jurisdictions (run [[wiki-research]] on trademark clearance methodology if needed)
3. **Domain availability** — check .com and relevant country-code domains
4. **Social media handle availability**

If name conflicts exist, resolve before proceeding — late-stage name changes are expensive.

---

## Logic — Step 3: Document Drafting

All documents drafted in parallel, by the same team. Document set varies slightly by jurisdiction:

### Universal Documents (All Jurisdictions)

#### 1. Articles of Association — [[draft-articles-of-association]]

The constitutional document. Must cover:
- Company name, registered office, objects
- Share capital and classes of shares (ordinary shares at founding; preferred shares added at VC round)
- Directors' appointment, powers, and removal
- General meeting procedures and voting rights
- Dividend distribution rights
- Transfer restrictions (ROFR, drag-along, tag-along)
- Liquidation waterfall

**MENA-specific**: Articles in UAE, KSA, and LB must be filed in Arabic (or bilingual with Arabic text controlling for government purposes); DIFC and ADGM allow English-only.

#### 2. Shareholders' Agreement — [[draft-shareholders-agreement]]

Governs the relationship between all shareholders (founders + future investors):
- Governance: board composition; reserved matters requiring shareholder approval
- Transfer restrictions: right of first refusal; drag-along; tag-along
- Exit mechanics: IPO, trade sale, secondary sale
- Dividend policy
- Deadlock resolution
- IP ownership (company owns all; no founder can claim individual IP)

Keep this document short at founding (founders only); it will be replaced at the first institutional VC round.

#### 3. Founders' Agreement — [[draft-founders-agreement]]

Between the founders specifically. Addresses:
- Equity split and vesting schedules
- Founder roles and responsibilities
- Decision-making authority during founding period
- What happens if a founder leaves (good leaver / bad leaver)
- IP assignment confirmation
- Binding non-compete and non-solicit during and for 12–24 months after departure

The Founders' Agreement is often superseded by or incorporated into the Shareholders' Agreement; use it as a bridge document pre-legal incorporation.

#### 4. Vesting Schedules — [[draft-vesting-schedule]]

Standard: 4-year vest with 1-year cliff.
- **Cliff**: no shares vest in the first 12 months; if a founder leaves in year 1, they take nothing
- **Monthly vesting after cliff**: remaining 75% vests monthly over months 13–48
- **Acceleration**: single-trigger (change of control alone) is less common and investor-disfavored; double-trigger (change of control + involuntary termination) is standard
- **Reverse vesting**: technically, the founder takes all shares at founding but the company has a right to repurchase unvested shares at cost if the founder departs

**MENA note**: reverse vesting is mechanically more complex in civil law jurisdictions where share buybacks have specific procedures; take legal advice on the mechanics in the chosen jurisdiction.

#### 5. IP Assignment from Founders — [[draft-ip-assignment]]

Critical and often missed:
- Each founder assigns all IP created before the company's incorporation that is relevant to the business
- Each founder assigns all IP created during the founding period before employment agreements are in place
- Consideration: nominal (e.g., $1 or 1 AED); does not need to be market value at this stage
- Must be signed before any VC due diligence — IP ownership gaps are a common DD red flag

#### 6. Employee Stock Option Plan (ESOP)

- Reserve 10–15% of fully diluted shares for ESOP at founding
- Adopt the plan document and rules at the first board meeting
- DIFC and ADGM have established ESOP frameworks
- UAE mainland ESOP enforceability is less settled — take jurisdiction-specific advice
- The ESOP pool is typically created pre-money at the VC's request; founders bear the dilution

#### 7. Initial Board Resolutions — [[draft-board-resolution]]

At the first board meeting:
- Appoint directors
- Authorize bank account opening (specify signatories)
- Accept founder IP assignments
- Adopt the ESOP plan
- Issue founder shares (with vesting, per the Shareholders' Agreement)
- Authorize execution of the Shareholders' Agreement and all foundational documents

#### 8. NDA Template — [[draft-nda-mutual]]

Standard mutual NDA for early discussions with:
- Potential employees (before offer letters)
- Early partners, customers, suppliers
- Potential investors (before sharing detailed financial/product information)

Have a signed NDA in place before sharing the pitch deck and financials with anyone outside the founding team.

#### 9. Consulting Agreements — [[draft-consulting-agreement]]

For founders who are not yet full-time employees:
- Defines the scope of services, compensation (often equity or deferred cash)
- Contains IP assignment clause (critical: independent contractors' work product does not automatically belong to the company in most jurisdictions)
- Includes confidentiality and non-solicitation

#### 10. Privacy Policy + Terms of Service

For any product with users:
- [[draft-privacy-policy]] — GDPR/PDPL compliant; tailored to the data being collected
- [[draft-terms-of-service]] — governs user relationship with the platform
- Must be live before any user data is collected; in UAE and KSA, data cannot be collected without a compliant privacy notice

---

## Logic — Step 4: Government Registration

### DIFC Registration Process

1. Select company type: Private Company Limited by Shares (Ltd.) is standard for startups
2. Name reservation via DIFC Registrar portal
3. Submit incorporation application: Articles, shareholder details, director details, registered address
4. Pay incorporation fees (annual license fee starts from approximately USD 1,500–3,000 depending on business activity)
5. Obtain Certificate of Incorporation
6. Open bank account (requires Certificate of Incorporation + corporate docs + KYC for all directors/shareholders/UBOs)
7. Apply for business license for the specific regulated activity (if fintech or financial services: DFSA authorization required separately)

### ADGM Registration Process

Similar to DIFC:
1. Company type: typically Private Limited Company (PLC)
2. ADGM Registration Authority submission
3. Annual license fees
4. FSRA authorization required for regulated financial services activities

### UAE Mainland

1. Trade license from the relevant emirate's Department of Economic Development (DED — Dubai; ADDC — Abu Dhabi; etc.)
2. Notarize Articles of Association (MOA — Memorandum of Association required in UAE mainland)
3. Lease agreement for business address (required before license issuance)
4. Register with relevant ministry for specific sector (if applicable)
5. Open bank account

### KSA

1. Obtain MISA (Ministry of Investment) foreign investment license — specifies permitted activities
2. Name reservation at Ministry of Commerce
3. Notarize company documents
4. Register with Ministry of Commerce; obtain Commercial Registration (CR) certificate
5. Register with General Authority of Zakat and Tax (GAZT) for VAT and corporate tax
6. Register with GOSI (for employees)
7. Register on Qiwa platform

### Lebanon

1. Register with Register of Commerce at Court of First Instance
2. Publish in Official Gazette
3. Register with NSSF (employees)
4. Register with tax authority (Direction des Finances)
5. Obtain sector-specific licenses if needed

---

## Logic — Step 5: Bank Account Opening

Bank account opening is often the most time-consuming step. Prepare:
- Certificate of Incorporation
- Memorandum and Articles of Association
- Board resolution authorizing bank account + specifying signatories
- KYC for all directors, shareholders, and UBOs (passport copies, proof of address, utility bills)
- Beneficial ownership declaration

**MENA bank account timelines:**
- UAE (major banks): 2–6 weeks; some banks are slower for new companies with no trading history
- KSA: 4–8 weeks; SAMA-regulated banks have strict KYC
- DIFC: faster with DIFC-familiar banks (ENBD, HSBC, Mashreq DIFC branch)
- Lebanon: highly variable given banking sector restrictions since 2019

---

## Critical First-90-Days Checklist

| Action | Deadline | Why critical |
|--------|---------|-------------|
| Founder IP assignments executed | Day 1 | VC due diligence standard; gaps are expensive to fix |
| 83(b) election filed (US founders with unvested stock) | 30 days from share issuance | Non-extendable IRS deadline; missing = massive tax event |
| Option pool reserved and plan documents adopted | 30 days | Must exist before first employee hire with equity |
| Board minutes for initial decisions | Day 1 | Governance record; needed for bank account, tax registration, future rounds |
| Bank account open and operational | 30–45 days | Cannot pay vendors, employees, or receive payment without it |
| VAT registration (UAE/KSA if revenues expected >threshold) | Before first taxable supply | UAE VAT threshold: AED 375,000 mandatory; AED 187,500 voluntary |
| Employment contracts for all working founders | Day 1 | Defines IP ownership; governs the founder relationship with the company |
| Privacy policy + ToS live | Before any user data collected | Legal requirement under PDPL / GDPR |
| NDA template signed with first advisors and investors | Before sharing financial/technical information | Protects trade secrets |

---

## Skill Orchestration

This workflow loads multiple drafting skills simultaneously:

[[draft-articles-of-association]] · [[draft-shareholders-agreement]] · [[draft-founders-agreement]] · [[draft-vesting-schedule]] · [[draft-ip-assignment]] · [[draft-board-resolution]] · [[draft-nda-mutual]] · [[draft-consulting-agreement]] · [[draft-privacy-policy]] · [[draft-terms-of-service]]

All generated with [[draft-contract-skeleton-builder]] as the master scaffolding.

---

## Related Skills

- [[draft-articles-of-association]]
- [[draft-shareholders-agreement]]
- [[draft-founders-agreement]]
- [[draft-vesting-schedule]]
- [[draft-ip-assignment]]
- [[draft-board-resolution]]
- [[draft-nda-mutual]]
- [[draft-privacy-policy]]
- [[research-jurisdiction-comparison]]
- [[workflow-investment-round-closing-pack]]
- [[workflow-hire-employee-pack]]
- [[wiki-startup]]
- [[wiki-vc-startups]]
