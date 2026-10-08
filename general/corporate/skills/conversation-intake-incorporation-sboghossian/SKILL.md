---
name: conversation-intake-incorporation-sboghossian
title: Intake — Incorporation
description: Use when a user wants to incorporate a new legal entity and Claude must gather the structuring inputs before routing to a jurisdiction-specific incorporation workflow. Triggers on requests to "set up a company", "incorporate", "register a startup", or select a jurisdiction for a new business. Covers MENA free zones and onshore (UAE, DIFC, ADGM, KSA, LB), Delaware, Singapore, and other common holding-company destinations.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/conversation/conversation-intake-incorporation
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# Intake — Incorporation

## When this applies

Activate when a user wants to form a new legal entity — startup, SPV, holding company, professional services firm, or branch. This skill collects the structuring information needed before routing to the appropriate jurisdiction-specific incorporation workflow. Do not route prematurely: the wrong entity type in the wrong jurisdiction is expensive to unwind.

## Behavior

Multi-turn intake. Capture the eight fields below. Where the user has given partial information, extract what is present and ask only for what is missing. Where jurisdiction has not been chosen, surface the key comparison and help the user decide (see jurisdiction guidance below) before proceeding.

## Required fields

### 1. Founders and shareholders

- Full names and nationalities of all founders.
- Equity split between them (pre-option-pool percentages).
- Contribution type per founder: cash, in-kind assets (IP, equipment), or services/sweat equity. Civil-law jurisdictions (LB, KSA, EG) require capital to be paid-up in cash or independently valued in-kind assets; sweat-equity shares have restricted treatment.
- Beneficial ownership: if any founder holds through a trust or holding entity, flag this — most MENA jurisdictions now mandate Ultimate Beneficial Owner (UBO) disclosure at company registry level.

### 2. Business activity

What will the company do? This is not a formality: license categories in UAE free zones, KSA Ministry of Investment (MISA), and LB Ministry of Finance tie the permitted activities to the legal form and sometimes require special approvals (e.g., financial services, healthcare, legal services, media each have a separate regulatory layer).

### 3. Jurisdiction choice

Help the user decide if they have not. Key trade-offs:

| Jurisdiction | Best for | Key constraint |
|---|---|---|
| UAE onshore (mainland) | Local market access, government contracts | Local service agent historically required (now majority foreign ownership possible in most sectors post-2021 Commercial Companies Law) |
| DIFC | VC-backed tech, finance, common-law regime, English language | Must operate as a financial services firm or holding company; operating companies need a DIFC nexus |
| ADGM | Crypto / digital assets, regulated fintech, family offices | ADGM Financial Services Regulatory Authority (FSRA) licensing required for regulated activities |
| UAE Free Zone (various: DMCC, DAFZA, JAFZA, etc.) | Trade, holding, import-export | Cannot do business directly on UAE mainland without a mainland agent |
| KSA | Saudi-facing businesses; Vision 2030 sectors | 100% foreign ownership now possible in most sectors via MISA license; Saudization (Nitaqat) applies |
| Lebanon (SAL / SARL) | Established LB firms, real-estate holding | Currency risk; restricted capital movement; USD banking complex |
| Delaware (C-Corp) | US VC-backed startups intending US IPO or US investors | US tax obligations; often paired with MENA operating subsidiary |
| Singapore (Pte Ltd) | Asia-Pacific nexus, Southeast Asia expansion | Good for SaaS/fintech with Asia investor base |

**Critical**: jurisdiction choice has long-term implications; re-domicile (transfer of domicile / continuation) is technically possible in DIFC and ADGM but operationally expensive. Encourage the user to commit before drafting.

### 4. Entity type

| Type | Typical use |
|---|---|
| LLC / SARL / Limited Liability Company | Most startups and SMEs; simpler governance; limited liability for members |
| JSC / SAE (Joint Stock Company) | Larger businesses; fundraising via share issuance; required for IPO |
| Partnership (general or limited) | Professional services (law firms, accounting firms) |
| Free Zone Entity (FZE = sole member; FZCO / FZ-LLC = multi-member) | UAE free zones |
| Branch | Foreign company maintaining presence without separate legal personality |
| SPV / Holding company | Asset isolation, fund structures |

### 5. Capital structure

- Initial share capital (confirm whether it must be paid up at incorporation — KSA: SAR 500,000 minimum for LLC; UAE: generally no minimum post-2021 for many activities; DIFC: USD 1 minimum for a company limited by shares).
- Share classes: common/ordinary only, or preferred shares for investors?
- If fundraising is planned: will there be convertible notes before a priced round? Note that civil-law jurisdictions do not have a native "SAFE" or convertible note instrument — must be structured as a shareholder loan with conversion mechanics.
- Employee option pool size (pre-money or post-money placement affects founder dilution math).

### 6. Office space and tenancy

Most jurisdictions require proof of registered office at incorporation. Free zones provide flexi-desk options. UAE mainland requires a physical office or approved virtual office for certain activities. KSA requires a physical commercial address.

### 7. Bank account and initial funding

Bank account opening can take 4–12 weeks in the GCC. Start the process as early as possible. FATF-linked MENA jurisdictions face enhanced due diligence from correspondent banks — confirm source of funds documentation is ready.

### 8. Tax structure

- Is this a standalone entity or part of a group? Does the group need a holding structure for IP or for dividend repatriation?
- UAE Corporate Tax: 9% applies to taxable income above AED 375,000 (effective June 2023 — verify current threshold). Free zone entities may qualify for the 0% qualified free zone person regime.
- KSA Corporate Tax: 20% on foreign shareholder share of profits; Zakat on Saudi shareholder share.
- LB: 17% corporate tax on profits.
- Group structures with IP holding in low-tax jurisdictions must comply with BEPS substance requirements.

## Critical flags — always surface these

- **Jurisdiction is sticky**: re-domicile is expensive; get it right first.
- **Founder agreement + vesting before incorporation** (if multi-founder): vesting protects the company if a co-founder exits early. Do not incorporate without this if there are two or more founders.
- **IP assignment from founders at day 1**: any IP created by a founder before incorporation must be formally assigned to the new entity. Failure to do so leaves IP ownership in legal limbo and is a standard VC due diligence red flag.
- **Bank account lead time**: budget 6–12 weeks for a UAE or KSA business account. Enterprise banking is worse.
- **Beneficial ownership disclosure**: mandatory across GCC, LB, and EU jurisdictions. UBO registers are increasingly public or regulator-accessible.

## Output

At the end of intake, produce:

1. A structured intake summary confirming all eight fields and any outstanding items.
2. A jurisdiction recommendation with one-paragraph rationale if the user is undecided.
3. A routing instruction to [[workflow-startup-incorporation-pack]] for the document deliverables checklist, and to [[draft-shareholders-agreement]] if the multi-founder/investor structure warrants one.

## Do not

- Recommend a specific jurisdiction without understanding the business activity — the activity may be restricted or require a special license that overrides the optimal structure.
- Skip the IP assignment flag for tech companies — it is invariably a problem at Series A due diligence.
- Apply Delaware or UK incorporation templates to MENA jurisdictions — governance requirements (quorum, board composition, reserved matters) differ materially.

## Related skills

- [[research-jurisdiction-comparison]]
- [[workflow-startup-incorporation-pack]]
- [[draft-shareholders-agreement]]
- [[draft-founders-agreement]]
- [[conversation-intake-shareholders-agreement]]
- [[kb-corporate-law-mena]]
- [[draft-ip-assignment-agreement]]
