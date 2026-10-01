---
name: design-aml-compliance-program-jeffreytse
title: Design AML Compliance Program
description: Use when a financial institution or money-services business needs an anti-money-laundering compliance program — building it around the specific pillars required under the Bank Secrecy Act (written policies, a designated compliance officer, ongoing training, independent testing, and customer due diligence), rather than a generic fraud-prevention policy with no BSA-specific structure.
author: jeffreytse
author_url: https://github.com/jeffreytse/grimoire-core/tree/main/skills/finance/corporate/skills/design-aml-compliance-program
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: white-collar
language: en
tags: [finance, corporate, aml-compliance, bank-secrecy-act, customer-due-diligence, financial-crime]
---

# Design AML Compliance Program

Build an anti-money-laundering compliance program around the specific pillars required under the Bank Secrecy Act — written policies, a designated compliance officer, ongoing training, independent testing, and customer due diligence — rather than a generic fraud-prevention policy with no BSA-specific structure.

## Why This Is Best Practice

**Adopted by:** The Bank Secrecy Act and its implementing regulations require covered financial institutions to maintain a compliance program built around specific defined pillars, and the Federal Financial Institutions Examination Council's BSA/AML Examination Manual is the reference standard examiners use to assess program adequacy across the US banking and financial services sector — making these specific pillars the universal structural baseline for AML programs at regulated institutions.
**Impact:** FinCEN's 2016 Customer Due Diligence Rule specifically added a fifth required pillar (ongoing customer due diligence, including beneficial ownership identification) after examiners and enforcement actions documented that programs lacking structured, risk-based customer due diligence — relying only on account-opening identification with no ongoing monitoring — were failing to detect money laundering conducted through legitimate-looking accounts after onboarding.
**Why best:** Money laundering typically doesn't announce itself at account opening — it emerges through transaction patterns and relationships that develop over time, which is exactly why the BSA's pillar structure requires ongoing due diligence and independent testing, not merely a one-time customer verification at onboarding; a program built around all five pillars is what actually catches this evolving risk, as opposed to a static, account-opening-only compliance check.

Sources: Bank Secrecy Act, 31 U.S.C. § 5311 et seq.; Financial Crimes Enforcement Network (FinCEN), "Customer Due Diligence Requirements for Financial Institutions," 31 CFR 1010.230 (2016); Federal Financial Institutions Examination Council (FFIEC), Bank Secrecy Act/Anti-Money Laundering Examination Manual

## Steps

### Step 1: Develop written policies and procedures covering the institution's specific risk profile

Develop written AML policies and procedures tailored to the institution's specific products, customer base, and geographic footprint — a generic template not calibrated to the institution's actual risk profile tends to under-address the institution's genuine highest-risk areas.

### Step 2: Designate a compliance officer with sufficient authority and resources

Designate a specific BSA/AML compliance officer with clearly defined authority and adequate resources to administer the program day to day, since a designated-in-name-only compliance officer without genuine authority or resourcing undermines the program regardless of how well the written policies are drafted.

### Step 3: Provide ongoing, role-calibrated employee training

Provide AML training to relevant employees on an ongoing basis, calibrated to their specific role's exposure to money laundering risk — frontline staff handling customer transactions require different, more operational training than back-office staff with no direct customer contact.

### Step 4: Implement risk-based customer due diligence, including beneficial ownership identification

Implement customer due diligence at onboarding and on an ongoing basis, including identifying beneficial owners of legal entity customers per FinCEN's 2016 rule, and calibrate the depth of due diligence to each customer relationship's specific money-laundering risk profile.

### Step 5: Conduct independent testing of the program on a regular cycle

Conduct independent testing of the AML program — by internal audit or an external party independent of the compliance function itself — on a regular cycle, verifying the program's actual operation matches its written design, since this fifth pillar specifically catches gaps between documented policy and actual practice that self-assessment by the compliance function alone might miss.

## Rules

- Build the program around all five BSA-required pillars (policies, designated officer, training, independent testing, customer due diligence) — not an ad hoc structure missing any of these specific components.
- Calibrate written policies and customer due diligence depth to the institution's actual, specific risk profile — not a generic template applied uniformly.
- Ensure the designated compliance officer has genuine authority and adequate resources, not a nominal designation alone.
- Conduct customer due diligence on an ongoing basis, including beneficial ownership identification, not only at initial account opening.

## Examples

**Ongoing due diligence catching evolving risk:** A customer's transaction pattern shifts significantly after account opening, developing characteristics consistent with potential structuring activity. The institution's ongoing (not just at-onboarding) due diligence process flags this pattern change for review — a risk a program relying solely on initial account-opening verification would have missed entirely.

**Independent testing surfacing a training gap:** An institution's periodic independent AML program testing reveals that frontline staff at several branches were not completing required training on schedule, despite the written policy specifying this requirement — a gap between documented policy and actual practice the independent testing pillar specifically exists to catch.

## Common Mistakes

- **Building a compliance program missing one of the five required pillars** — each pillar addresses a distinct failure mode, and omitting any one (most commonly, independent testing or ongoing due diligence) leaves a specific, documented gap.
- **Applying a generic AML policy template without calibrating it to the institution's actual customer base, products, and geography** — this tends to under-address the institution's genuine highest-risk areas.
- **Limiting customer due diligence to account opening, with no ongoing monitoring** — money laundering risk often emerges through post-onboarding transaction patterns, which is exactly what ongoing due diligence is designed to catch.
- **Designating a compliance officer without genuine authority or adequate resources** — a nominal designation doesn't substitute for the actual capacity to administer the program effectively.

## When NOT to Use

- For an organization not covered by the Bank Secrecy Act's applicability (not a financial institution, money-services business, or other covered entity) — confirm actual BSA coverage before assuming this specific program structure applies.
- As a substitute for the institution's separate sanctions compliance program — AML and sanctions compliance are related but distinct regulatory requirements, often addressed by complementary but separate program elements (see `design-sanctions-compliance-program`).
- For determining whether specific past transaction activity actually constituted money laundering or a reportable suspicious activity — that determination requires case-specific analysis, not this program-design practice.

> **Finance disclaimer:** This skill encodes professional best practices for educational purposes. It is not financial advice. Consult a licensed financial advisor before making investment decisions.
