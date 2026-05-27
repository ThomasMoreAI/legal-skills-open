---
name: invasive-testing-consent-letter
title: Invasive Testing Consent Letter (Phase II)
description: Drafts a Phase II invasive testing consent letter that limits scope, locations, timing, data control, restoration, security, and risk allocation under an existing access, due diligence, or purchase and sale agreement. Use this skill when a counterparty requests soil borings, test pits, groundwater wells, soil vapor sampling, or other intrusive ESA activities. Trigger on keywords including "Phase II," "invasive testing," "environmental site assessment," "ESA," "borings," "test pits," "monitoring wells," "restoration bond," "PLL insurance," "access agreement," "consent letter," "IDW handling," or "environmental due diligence." Even if the user just says "they want to do borings on the site" or "draft consent for Phase II," use this skill.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/invasive-testing-consent-letter
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: environmental
language: en
tags: [drafting, letter, regulatory, transactional]
---

# Invasive Testing Consent Letter (Phase II)

## Why This Skill Exists

When a buyer or tenant requests Phase II environmental testing, the property owner must grant narrowly scoped, conditional consent — not open-ended access. Without careful drafting, grantor loses control over what methods are used, where borings go, how data is shared with regulators, how the site is restored, and who bears liability for contamination discovered or caused during testing. A poorly drafted consent letter can create unintended regulatory reporting obligations, leave the site physically damaged, or waive protections in the underlying agreement.

This skill produces a consent letter that converts a work plan into enforceable limits while preserving the main agreement's protections.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

Ask every time unless the user says "use defaults" or "just draft." Gather:

1. **Main agreement identity** — name, date, parties, defined terms, and notice mechanics
2. **Property description** — address or legal description
3. **Recipient's written request and work plan** — proposed methods, locations, depths, number of borings/wells
4. **H&S plan and restoration plan** — from recipient's consultant
5. **Site plan/survey** — with proposed locations and utility information
6. **Contractor/consultant identities** — qualifications and licenses if required
7. **Insurance certificates and endorsements** — as required by main agreement
8. **Proposed schedule and restoration security** — bond/LOC/escrow terms

**If the user doesn't respond**, apply and clearly label these defaults: consent limited to work plan as submitted; standard restoration security required; no regulatory disclosure without prior consultation; same-day stabilization required.

---

## Step 1: Identify Agreement Framework and Defined Terms

- Identify the main agreement, parties, property, and all defined terms
- Incorporate by reference and state no amendment except as expressly stated
- Confirm notice addresses and execution mechanics from the main agreement
- Verify whether the main agreement already addresses invasive testing consent or requires specific conditions

---

## Step 2: Define Authorized Work with Numeric Caps

Grant limited, conditional consent for "Authorized Work" only. Never grant "Phase II testing" broadly — enumerate methods, counts, and limits:

- Number of borings/test pits/wells
- Maximum diameter and depth per boring
- Sampling methods (e.g., direct-push, hollow-stem auger)
- Number and type of samples
- Explicit exclusions (no monitoring wells, no pavement cutting, no vegetation removal unless specified)
- No-go zones (within X feet of utilities, structures, or sensitive areas)

Align revocation/suspension rights with the main agreement.

---

## Step 3: Fix Locations, Timing, and Access Logistics

**Locations:**
- Reference Exhibit A with coordinates or fixed references
- Define relocation radius requiring written approval (e.g., >10 feet)
- Identify no-go zones on site plan

**Timing and Access:**
- Work window (start and end dates)
- Permitted hours
- Notice requirement (business days before entry)
- Site conduct rules, escort requirements, staging areas
- Utility locate compliance (one-call + private utility clearance)

---

## Step 4: Allocate Reporting, Data Control, and Regulatory Notice

- All logs and lab data delivered within [X] business days
- No disclosure to any government authority or third party without Grantor's prior written consent except as required by law
- Provide [X] business days' consultation period before any required regulatory report
- Note statutory exceptions to non-disclosure obligations
- Address split sample rights
- Specify data ownership and confidentiality obligations

---

## Step 5: Specify Restoration, IDW Handling, and Security

**Restoration:**
- Same-day safety stabilization required
- Final restoration to pre-existing condition within [X] days
- Restoration standards and acceptance criteria

**Investigation-Derived Waste (IDW):**
- Recipient responsible for handling and disposal in compliance with law [VERIFY generator designation rules by state]
- Property must be left lien-free

**Restoration Security:**
- Amount, form (bond/LOC/escrow), deliverable before entry
- Clear draw mechanics: Grantor may draw after [X] days' notice for reasonable restoration costs
- Release conditions after satisfactory restoration

---

## Step 6: Reaffirm Indemnity, Insurance, and Conditions Precedent

- Indemnity and insurance provisions in main agreement apply to Authorized Work and all contractors
- PLL (Pollution Legal Liability) coverage with specified limits required [VERIFY availability and standard terms]
- As-is entry — avoid admissions about site conditions or utility accuracy
- No-representation language regarding subsurface conditions

**Conditions precedent to entry:** Consent effective only upon receipt of signed acceptance, insurance certificates, restoration security, and utility locate confirmation.

---

## Step 7: Produce the Consent Letter

### Template Skeleton

```text
[Date]

Re: Limited Consent for Invasive Testing at [Property]

Pursuant to Section [__] of [Agreement Name] dated [__] (the "Agreement")
between [Grantor] and [Recipient], Grantor grants Recipient limited consent
to perform only the "Authorized Work" described below. Capitalized terms not
defined here have the meanings in the Agreement. Except as expressly stated,
the Agreement remains in full force.

Authorized Work: [number] soil borings, max diameter [__], max depth [__],
method [__], samples [__]. No monitoring wells, test pits, pavement cutting,
vegetation removal, or work within [__] feet of utilities or structures.

Locations: Only at Exhibit A. Relocation > [__] feet requires written approval.

Timing/Access: Work Window [start–end]. Hours [__]. [__] business days'
notice. Site rules, escorts, and staging areas apply.

Utilities/Safety: Recipient must comply with applicable one-call requirements
and private utility clearance. Recipient proceeds at its sole risk.

Reporting/Data: Deliver all logs and lab data within [__] business days. No
disclosure to any government authority or third party without Grantor's prior
written consent except as required by law. Provide [__] business days'
consultation before any required report.

Restoration/IDW: Same-day stabilization. Final restoration within [__] days.
Recipient responsible for IDW handling and disposal in compliance with law
[VERIFY]. Property must be left lien-free.

Security: Provide restoration security in amount $[__], form [__], deliverable
before entry. Grantor may draw after [__] days' notice for reasonable
restoration costs.

Indemnity/Insurance: Indemnity and insurance in Agreement Section [__] apply
to Authorized Work and all contractors. PLL coverage with limits $[__]
required [VERIFY].

Conditions Precedent: Consent effective only upon receipt of signed acceptance,
insurance, security, and locate confirmation.

[Signature blocks for Grantor, Recipient, Consultant acknowledgment]
```

### Mandatory Front Matter

At the top of every output, include:
1. **Assumptions Used** — main agreement terms relied on, scope of authorized work, security terms
2. **Open Items / Needed Inputs** — missing work plans, insurance details, state-specific requirements

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

After delivering the initial draft, ask:

1. Does the Authorized Work scope match the actual work plan submitted?
2. Are the no-go zones and relocation limits appropriate for the site?
3. Should restoration security amount be adjusted based on site conditions or work complexity?
4. Are there state-specific regulatory reporting obligations that need to be addressed?

---

## Quality Audit

Before finalizing, verify:

- Consent is limited to enumerated Authorized Work — no broad "Phase II" grant
- All numeric caps match the actual work plan (borings, depths, diameters)
- Exhibit A locations are specific and verifiable
- Restoration security has clear draw mechanics and timeline
- Data control clause includes consultation period before regulatory disclosure
- IDW handling responsibility is assigned with statutory compliance requirement
- Indemnity reaffirmation does not narrow existing protections
- Conditions precedent are complete (insurance, security, locate, signed acceptance)
- Defined terms match the main agreement exactly
- No admissions about site conditions or utility accuracy
- All state-specific requirements flagged with [VERIFY]
- Lien prevention and release obligations included

---

## Guidelines

- Use the exact defined terms, notice addresses, and execution mechanics from the main agreement
- Never grant "Phase II testing" broadly; enumerate methods, counts, and limits
- Do not incorporate a work plan "as modified in the field" without written approval controls
- Avoid admissions about site conditions or utility accuracy; use "as-is" and no-representation language
- Include a consultation period for regulatory reporting and note statutory exceptions
- Mark regulatory citations and ASTM standard versions with `[VERIFY]` if not confirmed
- State-specific rules for one-call, well abandonment, reporting, and liens require counsel confirmation
- If required inputs are missing, issue a conditional consent that withholds entry until delivered
- **Anti-hallucination**: Do not invent environmental regulations, ASTM standards, or state-specific requirements. Flag all unverified regulatory citations with `[VERIFY]`
- **Attorney review required**: All output requires licensed attorney review before execution or delivery
