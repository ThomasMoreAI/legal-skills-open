---
name: pledge-agreement-securities
title: Pledge Agreement (Securities)
description: Drafts perfected-security-interest Pledge Agreements for securities collateral under UCC Article 9. Use when drafting securities pledge agreements, stock pledge documents, collateral assignments, or security interest grants in investment property securing loans or credit facilities.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/pledge-agreement-securities
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: finance
language: en
tags: [agreement, drafting, transactional]
---

# Pledge Agreement (Securities)

Grants a perfected security interest in certificated or uncertificated securities to secure a loan, credit facility, or other obligation. Covers collateral description, perfection mechanics, covenants, and UCC Art. 9 remedies.

## Prerequisites

Collect before drafting:

1. **Credit documents** — credit agreement or note (principal, rate, maturity)
2. **Party details** — legal names, entity types, formation jurisdictions, addresses, signing authority
3. **Securities details** — issuer, type (common/preferred/bonds), share count or principal amount, certificate numbers, CUSIPs, account numbers, intermediary info
4. **Existing encumbrances** — prior liens, shareholder agreements, transfer restrictions, ROFR
5. **Related security package** — guarantees, intercreditor agreements, other collateral docs

## Document Structure

| Section | Key Contents |
|---|---|
| Title & Preamble | Execution date; full party identification; representative capacity if agent |
| Recitals | Reference underlying obligation; state principal/commitment; note pledge required under credit docs |
| Definitions | "Pledged Securities," "Secured Obligations" (all principal, interest, fees, indemnities, extensions, refinancings), "Collateral," "Event of Default" |
| Collateral Description | Per collateral checklist below |
| Grant of Security Interest | Continuing first-priority security interest in all Collateral to secure Secured Obligations |
| Perfection & Delivery | Method-specific mechanics per perfection table |
| Representations & Warranties | Per R&W checklist |
| Covenants | Affirmative + negative; voting/distribution rights; LTV/margin maintenance |
| Events of Default | Payment default; rep breach; covenant breach; cross-default; bankruptcy; material collateral value decline; delisting |
| Remedies | UCC Art. 9 disposition; commercially reasonable sale; proceeds waterfall; credit bidding; deficiency |
| Valuation & Substitution | Methodology; substitution conditions; simultaneous exchange |
| Release & Termination | Full release on payment; partial release at LTV thresholds; return certificates; file UCC-3s |
| General Provisions | Governing law; notices; amendments; severability; integration; indemnification |
| Signature Blocks | Entity name, signatory name/title, date; notarial certificates if needed |

## Collateral Checklist

- [ ] Security type (common stock, preferred, bonds, debentures, notes)
- [ ] Issuer full legal name
- [ ] Number of shares or principal amount
- [ ] Certificate numbers (certificated) or account number (uncertificated)
- [ ] CUSIP / ISIN identifiers
- [ ] Class or series designation
- [ ] Securities intermediary name/address (if book-entry)
- [ ] All proceeds, dividends, distributions, interest, redemption proceeds, subscription rights, stock splits, liquidation proceeds

## Perfection Mechanics

| Collateral Type | Method | UCC Basis | Actions |
|---|---|---|---|
| Certificated | Possession | § 9-313 | Deliver certificates + blank stock/bond powers to pledgee/custodian |
| Uncertificated (intermediary-held) | Control | § 9-106, § 9-314 | Tri-party control agreement: intermediary complies with pledgee entitlement orders without pledgor consent |
| Uncertificated (direct) | Registration | § 8-301(b) | Register pledge on issuer's books; obtain issuer consent |
| Protective filing | Filing | § 9-310 | UCC-1 financing statement (advisable even if possession/control achieved) |

## R&W Checklist

- [ ] Good, marketable title free of liens (except permitted liens)
- [ ] Full authority to pledge; all organizational approvals obtained
- [ ] No violation of law, charter, bylaws, or shareholder agreement
- [ ] Securities duly authorized, validly issued, fully paid, non-assessable (equity)
- [ ] No third-party ROFR, preemptive rights, or co-sale rights triggered
- [ ] Securities law compliance (pledge exempt from registration or registered)
- [ ] No pending litigation affecting pledged securities
- [ ] Information about securities is accurate and complete

## Covenant Framework

**Affirmative:** Maintain securities in good standing; pay taxes/assessments; defend security interest; deliver periodic valuations (market close for listed, independent appraisal for unlisted); notify pledgee of material events.

**Negative:** No sale/transfer/disposition without consent; no additional liens; no amendment of issuer organizational documents impairing collateral value.

**Voting & Distributions (bifurcated):**
- Pre-default: pledgor retains voting rights and receives dividends
- Post-default: all voting and economic rights shift to pledgee

**LTV / Margin Maintenance:** Specify LTV ratio and valuation methodology; cure by pledging additional securities or paying down principal within [X] business days; uncured breach triggers Event of Default.

## Remedies Framework

Upon Event of Default, pledgee may:
- Exercise all UCC Art. 9 secured-party remedies
- Sell at public or private sale on commercially reasonable terms
- Apply proceeds: (i) enforcement costs → (ii) Secured Obligations → (iii) surplus to pledgor
- Credit bid at any sale; exercise all voting/governance rights
- Collect deficiency from pledgor [unless non-recourse]
- Notice: [10] days before disposition deemed reasonable; pledgor may redeem by paying Secured Obligations in full plus expenses before disposition

## Pitfalls & Checks

- **Match perfection to collateral type** — possession for certificated, control for intermediary-held; UCC Art. 9 compliance is non-negotiable
- **Cross-check defined terms** across pledge and all related credit documents (party names, obligation definitions, default triggers)
- **Securities law restrictions** — confirm pledge does not trigger registration; address Rule 144 and contractual lock-ups
- **Control agreement timing** — specify deadline and consequence if intermediary refuses or delays
- **Never waive commercial reasonableness** of disposition (UCC § 9-610)
- **Closely held securities** — add issuer acknowledgment/consent; require independent appraisal for valuation
- **Multi-lender deals** — clarify agent authority, lien-sharing, intercreditor coordination
- **Choice-of-law** — UCC §§ 9-301 to 9-307 may override contractual selection for perfection
- **Do not waive** pledgor's redemption right or statutory notice requirements beyond UCC limits
- **Mark uncertain citations** with `[VERIFY]` — especially state-specific UCC variations
