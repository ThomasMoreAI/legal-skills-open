---
name: intrastate-offering
title: Intrastate Offering Compliance (Rule 147/147A)
description: Produces a compliance memo and execution plan for U.S. intrastate securities offerings under Rule 147 or Rule 147A with state registration by qualification. Covers safe harbor selection, doing-business tests, residency verification, advertising controls, resale restrictions, integration analysis, and blue sky registration. Trigger when the user mentions intrastate offering, Rule 147, Rule 147A, registration by qualification, single-state offering, Section 3(a)(11), state-only fundraising, in-state investor requirements, resale restriction legends, or says "we're only raising in one state."
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/intrastate-offering
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: securities
language: en
---

# Intrastate Offering Compliance (Rule 147/147A)

One out-of-state sale destroys the exemption — potentially retroactively for all investors. Unlike Rule 506, no NSMIA preemption exists; the issuer must also satisfy full state registration. This skill prevents the common failures: inadequate residency verification, uncontrolled advertising reach, failed doing-business tests, and integration with concurrent offerings.

## Intake (Mandatory)

Gather before drafting unless the user says "use defaults" or "just draft":

1. **Issuer details** — state of formation, principal office, org chart
2. **Operations by state** — revenues, assets, employees, locations; current financials
3. **Offering terms** — security type, size, pricing, use of proceeds, escrow, commissions
4. **Draft materials** — term sheet, offering document, subscription agreement, marketing copy
5. **Distribution plan** — channels, internet use
6. **Residency verification process** — online/offline workflow, document retention
7. **Prior and planned offerings** — types, dates, investor pools (6-month look-back/forward)
8. **State blue sky rules** — registration forms, examiner guidance, filing requirements

**Defaults if no response:** Rule 147A; registration by qualification; standard residency documentation. Label all defaults.

## Step 1: Select Safe Harbor (Rule 147 vs. 147A)

| Factor | Rule 147 [VERIFY] | Rule 147A [VERIFY] | Decision |
|---|---|---|---|
| Issuer formation | Must be in offering state | Out-of-state OK | Formed elsewhere → 147A |
| Principal place of business | Required | Required | Document "nerve center" |
| General solicitation | Restricted | Permitted with legends | Broad internet → 147A |
| Offers to out-of-state | Risky | OK if sales in-state only | Confirm offer definition |

Verify current text: 17 CFR 230.147, 230.147A, 230.152; Securities Act §§ 3(a)(11), 5, 17(a) [VERIFY].

## Step 2: Analyze Doing-Business Tests

All four must be met. Document evidence for each:

| Test [VERIFY] | Threshold | Evidence |
|---|---|---|
| Revenue | ≥ 80% in-state | Revenue by customer/location |
| Assets | ≥ 80% in-state | Balance sheet, fixed asset register |
| Proceeds | ≥ 80% used in-state | Use-of-proceeds budget and tracking |
| Employees | Majority in-state | Payroll and headcount by state |

## Step 3: Build Residency Verification Protocol

| Investor Type | Standard [VERIFY] | Minimum Documents |
|---|---|---|
| Individual | Principal residence in state | Driver license + utility bill or tax record |
| Entity | Principal place of business in state | Operating agreement + business address proof |
| Entity formed for offering | Look-through to owners | Residency docs for all beneficial owners |

- Require documentary proof before subscription acceptance; retain in investor file
- IP checks and online gating are supplemental only — not sufficient alone
- Apply look-through for entities formed to purchase the securities

## Step 4: Advertising and Offer Controls

- Place legends on all materials and landing pages
- Gate access to offering materials by state before disclosure
- No paid ads targeting beyond the offering state
- Train all personnel: no discussions with non-residents
- Preserve copies of all ads, targeting settings, and gating records

## Step 5: Resale Restrictions and Transfer Controls

- Restricted period: six months from issuer sale [VERIFY]
- Restrictive legends on certificates or book-entry statements
- Stop-transfer instructions to transfer agent or internal ledger
- Require approval of any transfer during restricted period

**Legend template:**

> THESE SECURITIES HAVE NOT BEEN REGISTERED UNDER THE SECURITIES ACT OF 1933. FOR A PERIOD OF SIX MONTHS FROM THE DATE OF SALE BY THE ISSUER, ANY RESALE MUST BE MADE ONLY TO PERSONS RESIDENT WITHIN THE STATE OF [STATE]. ANY TRANSFER IN VIOLATION OF THIS RESTRICTION IS VOID.

**Subscription representation template:**

> Subscriber represents that Subscriber's principal residence (or principal place of business) is in the State of [STATE], and agrees to provide documentation reasonably requested to confirm residency. Subscriber acknowledges the securities are restricted and may not be transferred to non-residents during the applicable restricted period.

## Step 6: Integration Risk and State Registration

**Integration analysis:**

| Item | Risk | Mitigation |
|---|---|---|
| Recent offerings | Integration with intrastate | Rule 152 framework and spacing [VERIFY] |
| Concurrent offerings | Confusing investor pools | Separate materials and investor lists |
| General solicitation elsewhere | Contaminates intrastate | Pause or segregate campaigns |

**State registration by qualification:**
- Confirm registration path under state law [VERIFY]
- Assemble forms, consents to service, filing fees
- Confirm financial statement and audit requirements [VERIFY]
- Address merit review: escrow, commissions, pricing, dilution
- Align offering document, state forms, and marketing materials
- Pre-clear advertising if required [VERIFY]

## Step 7: Deliverables

1. **Compliance memo** — rule selection, eligibility, residency controls, advertising controls, resale restrictions, integration analysis
2. **Execution checklist** for issuer and counsel
3. **Legend and subscription representations**
4. **State registration filing checklist**
5. **Assumptions, open items, and risk flags**

Every output must begin with:
- **Assumptions** — rule selected, doing-business test results, residency standard
- **Open Items** — missing financials, unresolved state requirements, [VERIFY] items

**Contingencies:** Reject non-resident subscriptions and document; if residency error discovered, consult counsel immediately; if controls are unenforceable, recommend alternative exemptions.

## Post-Draft Alignment (Mandatory)

After delivering, ask:
1. Are doing-business calculations confirmed against current financials?
2. Is the advertising/distribution plan finalized?
3. Should residency verification be tested with a sample workflow?
4. Are there concurrent or recent offerings needing integration analysis?

## Checks and Pitfalls

**Quality gate — verify before finalizing:**
- Safe harbor selection documented with rationale
- All four doing-business tests analyzed with evidence
- Residency protocol requires documentary proof
- Legend language matches correct rule and state
- Advertising controls enforceable for planned channels
- Integration analysis covers 6-month look-back and look-forward
- State registration path confirmed with forms and fees
- Subscription representations match legend language
- All citations verified or flagged [VERIFY]
- Assumptions and open items listed prominently

**Rules:**
- Output is not legal advice; attorney review required before use
- Mark unverified rule text, thresholds, or dates with `[VERIFY]`
- Resolve federal vs. state conflicts in favor of the more restrictive rule
- If controls cannot be enforced, recommend a different exemption
- Maintain single source of truth across forms, disclosures, and marketing
- Flag broker-dealer or finder compensation for separate review
- Do not fabricate rule thresholds, state requirements, or registration procedures — every citation must be verified or flagged
- Treat confidentiality and truthfulness as mandatory (Model Rules 1.1, 1.3, 1.6, 3.3, 4.1) [VERIFY]
