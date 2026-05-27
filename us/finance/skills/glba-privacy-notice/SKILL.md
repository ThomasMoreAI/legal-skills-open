---
name: glba-privacy-notice
title: GLBA Privacy Notice
description: Drafts GLBA-compliant privacy notices using the 16 CFR Part 313 Appendix A model form safe harbor. Use when creating or updating Regulation P privacy notices, annual consumer disclosures, or NPI sharing notices for banks, credit unions, securities firms, insurers, or other covered entities under 15 U.S.C. §§ 6801–6809.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/glba-privacy-notice
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: finance
language: en
tags: [drafting, letter, regulatory]
---

# GLBA Privacy Notice

Produces a 16 CFR Part 313-compliant consumer privacy notice using the Appendix A model form safe harbor, covering mandatory disclosures, sharing categories, opt-out rights, and security safeguards.

## Gather Before Drafting

- Institution legal name, DBAs, charter type, federal regulator
- Affiliate structure and types (banking, insurance, securities, lending)
- NPI categories collected and their sources
- All sharing arrangements: affiliate, nonaffiliate, joint marketing, service providers
- Opt-out channels: toll-free number, URL, mailing address, processing timeline
- Security program: physical, electronic, procedural safeguards
- Operating jurisdictions (for state-law overlays)

## Notice Structure

### 1. FACTS Table Header

Required model form opening:

| Field | Content |
|---|---|
| Why? | One-sentence explanation of why notice is provided |
| What? | Categories of NPI collected (summary) |
| How? | Whether and how consumers can limit sharing |

Include verbatim or substantially similar opening: "Federal law requires us to tell you how we collect, share, and protect your personal information. Federal law also gives you the right to limit some but not all sharing."

Include institution legal name, effective date, recognizable DBAs.

### 2. Information Collection Disclosure

Group NPI by source:

| Source | Examples |
|---|---|
| Consumer-provided | SSN, income, assets, contact info, account preferences |
| Account-generated | Balances, payment history, transactions, card activity |
| Consumer reporting agencies | Credit reports/scores |
| Other third parties | Identity verification, fraud databases, public records |

### 3. Sharing Matrix and Opt-Out Rights

| Sharing Purpose | Limitable? | Authority |
|---|---|---|
| Everyday business (transactions, compliance, fraud) | No | §§ 313.14–.15 exceptions |
| Affiliates — transaction/experience info | No | Permitted sharing |
| Affiliates — creditworthiness for marketing | **Yes** | FCRA § 603(d)(2)(A)(iii); 30-day pre-sharing notice |
| Nonaffiliates — joint marketing (formal agreement) | No | § 313.13 exception |
| Nonaffiliates — their own marketing | **Yes** | Full GLBA opt-out |

Required affiliate marketing timing language: "If you are a new customer, we can begin sharing your information with our affiliates for their marketing purposes 30 days from the date we sent this notice. When you are no longer our customer, we continue to share your information as described in this notice. However, you can contact us at any time to limit this sharing."

### 4. Opt-Out Instructions

Provide all three channels (phone, online, mail) with:
- Processing timeline (e.g., "within 30 days")
- Joint account treatment (one opts out for all, or each separately)
- Duration (indefinite unless revoked) and revocation method
- Online: note ADA/assistive-technology accessibility

### 5. Security Safeguards

Cover physical, electronic, and procedural safeguards. Include verbatim or substantially similar: "To protect your personal information from unauthorized access and use, we use security measures that comply with federal law. These measures include computer safeguards and secured files and buildings."

### 6. State-Specific Overlays

Apply where institution operates or serves customers:

| State | Requirement |
|---|---|
| California | CCPA/CPRA rights; SB 1 opt-in for certain nonaffiliate sharing [VERIFY current applicability] |
| Vermont | Opt-in consent before nonaffiliate marketing sharing [VERIFY current rules] |
| Nevada | NRS 603A opt-out for sale of covered information [VERIFY] |
| Massachusetts | 201 CMR 17.00 data security cross-reference [VERIFY] |
| Insurance (NAIC) | Model Act disclosures for underwriting/claims data |

### 7. Contact Block

Privacy office phone, email, mailing address. Website URL for current notice. Supervisory authority (OCC, FDIC, NCUA, SEC, state insurance dept.).

## Final Checklist (16 CFR § 313.6)

- [ ] NPI categories collected
- [ ] Affiliates/nonaffiliates receiving NPI
- [ ] Former customer sharing disclosures
- [ ] Opt-out rights and exercise methods
- [ ] FCRA § 603(d)(2)(A)(iii) disclosures
- [ ] Security practices statement
- [ ] Effective date
- [ ] State-law additions (where applicable)

## Pitfalls

- **Model form = safe harbor** — deviations from Appendix A format require independent compliance analysis
- **FCRA vs. GLBA opt-outs are distinct rights** — affiliate marketing opt-out (FCRA) and sharing opt-out (GLBA) must be disclosed separately
- **Former customers** — sharing practices must be disclosed; opt-out rights may not extend post-relationship depending on sharing type
- **Joint marketing exception** — only applies between financial institutions with a formal written agreement limiting use
- **No aspirational language** — every safeguard and practice statement must reflect current actual operations
- **Delivery** — paper, electronic (requires E-SIGN Act consent), or web posting must be clear and conspicuous
- **Annual notice** — required for ongoing customer relationships; update on material practice changes

---

Key changes from the original:

- **Description** trimmed from 4 sentences to 2 while retaining all trigger cues (Regulation P, annual disclosures, entity types, statutory citation)
- **Prerequisites → "Gather Before Drafting"** — collapsed from numbered verbose items to a flat bullet list
- **Output Structure** sections streamlined — removed horizontal rules, collapsed verbose sub-lists, eliminated redundant examples (e.g., full Equifax/Experian/TransUnion listing → "Credit reports/scores")
- **Sharing Matrix** — renamed "Can You Limit?" → "Limitable?" for compactness; shortened basis descriptions
- **Security Safeguards** — collapsed the 3-row table into a single prose instruction (the table added bulk without aiding the agent)
- **Mandatory Elements Checklist** renamed to **Final Checklist** and tightened labels
- **Guidelines → Pitfalls** — converted from guidelines prose into a focused pitfalls list with the same substantive rules
