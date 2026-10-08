---
name: draft-licensing-agreement-sboghossian
title: Licensing Agreement (General IP & Commercial)
description: Use when drafting a general IP or commercial licensing agreement covering patents, trademarks, copyright, or software, across multiple jurisdictions. Covers grant scope, exclusivity, territory, royalty mechanics, quality control requirements (trademark), infringement rights, improvements, indemnity, term, and post-termination obligations. Includes MENA-specific issues — SAIP registration, gharar constraints in KSA, commercial agency characterization risk, and DIFC/ADGM common-law conventions. Triggers on "draft", "ip", "licensing", "commercial license", or "royalty agreement".
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-licensing-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: ip
language: en
---

# Licensing Agreement (General IP & Commercial)

## When to use this

Use this skill for general commercial and IP licensing across all asset types — patents, trademarks, copyrights, trade secrets, and know-how. It covers the full drafting lifecycle from grant-clause architecture through royalty mechanics, quality control, infringement enforcement, and termination.

For software-specific licensing (SaaS, enterprise software, named-user, perpetual), prefer [[draft-licensing-agreement-software]]. For a heavily negotiated IP licensing deal with royalty audit provisions, milestone payments, and prosecution control, see [[draft-ip-licensing]].

## Core sections

### 1. Definitions
Every licensing agreement lives and dies by its definitions. Define precisely:

- **Licensed IP**: enumerated asset-by-asset — patent numbers, trademark registrations, copyright works, trade secret descriptions; avoid "and all related IP" catch-all provisions without specificity
- **Territory**: geographic scope; "worldwide" is valid but creates enforcement complexity
- **Field of Use**: industry, application, customer type, or channel through which the licensee may exploit the IP; field restrictions allow the licensor to license other fields to other parties
- **Net Sales**: the royalty base — define gross revenue, then enumerate permitted deductions (returns capped at a percentage, freight, documented taxes, early-payment discounts up to a defined cap)
- **Sublicensee**: any party to whom the licensee grants sublicenses; flow-down obligations
- **Affiliate**: may the licensee include affiliates within its licensed rights without separate approval?

### 2. Grant of license
The grant clause is the core of the document. It must specify:
- **Scope of rights**: which acts are permitted? (make, use, sell, offer for sale, import, reproduce, distribute, sublicense, prepare derivative works) — tailor to the IP type
- **Exclusivity**: choose one:
  - *Exclusive* — licensor grants no other licenses in field/territory, and itself is excluded
  - *Sole* — licensor grants no other licenses, but licensor retains the right to exploit itself
  - *Non-exclusive* — licensor may license others concurrently
- **Sublicensing rights**: yes/no; if yes, specify conditions (licensor's prior written approval, flow-down of all obligations, licensor audit rights over sublicensees)
- **No implied license**: state expressly that no rights are granted except those expressly enumerated

### 3. Royalty mechanics
- **Running royalty**: percentage of Net Sales (typically 3-10% depending on IP type and market)
- **Minimum annual royalty (MAR)**: guarantees the licensor a floor; if licensee does not hit sales targets, the MAR becomes payable regardless
- **Milestone payments**: on first commercial sale, on reaching defined revenue thresholds, on geographic expansion
- **Lump-sum upfront payment**: in exchange for reduced royalty or as a technology-access fee
- **Payment schedule**: quarterly reporting and payment within 30 days of quarter end
- **Late payment interest**: typically at the higher of (a) central bank rate + 3% and (b) contractual rate
- **Currency**: specify the reporting and payment currency and the applicable exchange rate (central bank mid-market rate on payment date recommended)

### 4. Reporting and audit rights
- Licensee submits quarterly royalty reports showing calculation of Net Sales and royalties
- Licensor may audit Licensee's records annually, on 30-day written notice
- Records kept for 3 years post-payment period
- If audit reveals underpayment exceeding 5% of amounts due, Licensee bears audit cost and pays deficiency with interest

### 5. Improvements
The most contentious clause in long-running licensing relationships:
- **Background IP**: each party's pre-existing IP; neither party acquires rights to the other's background IP beyond what is expressly licensed
- **Foreground IP**: IP developed during the license relationship
  - *Licensee improvements on Licensed IP*: two options — (a) automatically assigned to Licensor (Licensor takes all), or (b) Licensee owns, with a non-exclusive grant-back license to Licensor
  - *Grant-back caution*: exclusive grantbacks can violate competition law in the EU (TTBER analysis required)
- **Jointly developed IP**: ownership percentage, management rights, licensing rights need express agreement

### 6. Quality control (trademarks)
For any trademark license, quality control is not optional — it is legally essential.

A trademark licensor who fails to maintain quality control over the licensed mark risks "naked-license" invalidity: the mark may lose its protection because the licensor has abandoned control. Required provisions:
- Licensor's right to inspect samples, manufacturing processes, and marketing materials
- Quality standards schedule (as an exhibit)
- Right to approve use of the mark in new channels or new markets
- Licensee's obligation to notify Licensor of any change to product formulation, quality, or manufacturing process
- Licensor's right to terminate immediately upon persistent failure to meet standards

### 7. Infringement against third parties
- Notification: Licensee must promptly notify Licensor of any known or suspected third-party infringement
- Enforcement rights: Licensor typically retains primary enforcement rights; exclusive licensee may have standing to sue (jurisdiction-specific)
- Cost and recovery: specify who bears enforcement costs; specify how recovered damages are split
- Step-in: if Licensor elects not to enforce, does Licensee have the right to enforce at Licensee's cost (with Licensor's name if needed for standing)?
- Defense: if a third party sues the Licensee for infringement by the Licensed IP, which party bears defense costs?

### 8. Warranties
- Licensor warrants: ownership of the Licensed IP, no conflicting licenses, no pending third-party challenges, no governmental orders restricting the license
- Licensor typically does NOT warrant non-infringement of third-party rights (expensive; difficult to verify)
- Licensee warrants: duly organized, has authority, will comply with applicable laws, will not use the IP beyond the licensed scope

### 9. Indemnification
See [[review-indemnification-balance]] for balance analysis.
- Licensor indemnifies Licensee against third-party claims that the Licensed IP infringes a third party's IP rights (capped at royalties paid in prior 12 months, typically)
- Licensee indemnifies Licensor against claims arising from Licensee's modifications, use beyond scope, breach of quality standards, product liability arising from Licensee's products

### 10. Term and termination
- **Fixed term** with auto-renewal absent notice, or fixed term with option to renew
- **Termination for cause**: material breach with 30-60 day cure period
- **Termination for non-payment**: 15-day cure period
- **Insolvency termination**: automatic or at Licensor's election on Licensee's insolvency filing
- **Anti-challenge clause**: Licensor terminates if Licensee challenges validity of Licensed IP — valid in some jurisdictions; void in EU under TTBER (cannot prohibit validity challenges); verify per applicable law

### 11. Post-termination obligations
- Licensee immediately ceases all use of Licensed IP
- Sell-off period: 90-180 days for existing inventory bearing Licensed IP (usually allowed)
- Return or destroy all Confidential Information and Licensed Materials; provide certification
- Royalties accrue through end of sell-off period
- Surviving provisions: audit rights (for 3 years), confidentiality, indemnification, governing law

### 12. Governing law and dispute resolution
- Arbitration recommended for cross-border deals; specify seat, rules (DIAC, ICC, LCIA, ADGM Arbitration Centre), and language
- Expert determination for royalty-calculation disputes as a faster, cheaper alternative to arbitration

## MENA-specific issues

**KSA / Sharia constraint on gharar (unacceptable uncertainty)**
Royalty bases and rates must be determinable at the time of contracting. Open-ended royalty formulas keyed to future uncertain events (e.g., a percentage of "future profits not yet calculable") can be challenged on gharar grounds. Structure uncertain milestone payments as conditional fixed sums rather than floating percentages where possible.

**SAIP (Saudi Authority for Intellectual Property) registration**
Trademark and patent licenses in KSA should be recorded with SAIP to be enforceable against third parties. Without registration, the license binds the parties contractually but does not provide priority against subsequent licensees or assignees.

**UAE commercial agency risk**
In UAE, an exclusive territorial license where the licensee "promotes" the licensor's products in UAE may be characterized as a commercial agency under Federal Law 3/1987. Commercial agents enjoy strong statutory protections including automatic contract renewal and compensation on termination. To avoid this:
- Ensure the licensee is exploiting IP rights, not merely acting as a promoter or representative
- Avoid language that suggests the licensee acts "on behalf of" the licensor
- Include an express exclusion of commercial agency

**ADGM / DIFC**
Standard English-law IP licensing principles apply; common-law courts; arbitration at DIAC or ADGM Arbitration Centre. DIFC IP Law No. 4 of 2019 governs registered and unregistered IP in DIFC.

**EU Technology Transfer Block Exemption Regulation (TTBER) Reg. 316/2014**
Applies to technology licensing agreements (patents, know-how, software) between competitors and non-competitors. Hardcore restrictions include price-fixing on sublicensees and market allocation. Exclusive grantbacks and no-challenge clauses require specific antitrust analysis.

## Drafting standards

- No `[INSERT X]` placeholders unless a template was explicitly requested. Supply clearly-labeled defaults and list them at the top of the output.
- Every definition that differs from common usage must be expressly defined.
- Deliver a document with complete boilerplate (notices, entire agreement, severability, no waiver, counterparts — see [[draft-boilerplate-clauses]]).

## Common mistakes

- Failing to register the trademark license (UAE, KSA, LB, EG) — renders it unenforceable against third parties
- Quality-control provisions missing from trademark licenses — naked-license invalidity risk
- Undefined Net Sales — every deduction left undefined will be taken
- No minimum royalty — licensee sits on the license without commercializing, blocking the licensor from licensing others
- Anti-challenge clause without checking applicable law (void in EU; valid in some others)

## Related skills

- [[draft-ip-licensing]]
- [[draft-licensing-agreement-software]]
- [[draft-ip-assignment]]
- [[review-indemnification-balance]]
- [[draft-nda-mutual]]
