---
name: insurance-certificate-compliance
title: CRE Insurance Certificate Compliance Review
description: Produces requirement-by-requirement CRE insurance certificate compliance reviews by analyzing ACORD 25 certificates and endorsements against Access Agreement terms. Use when the user mentions COI review, insurance compliance, ACORD 25 analysis, Additional Insured verification, primary/non-contributory status, waiver of subrogation, vendor insurance audit, CGL compliance, umbrella follow-form, broker-ready deficiency instructions, certificate holder vs. additional insured, AI endorsements (CG 20 10, CG 20 37), or carrier rating checks.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/insurance-certificate-compliance
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: insurance
language: en
---

# CRE Insurance Certificate Compliance Review

Analyzes ACORD 25 certificates and endorsement copies against Access Agreement insurance requirements. Produces a compliance determination with broker-ready corrective instructions.

**Cardinal rule**: A COI is an informational snapshot only — it does not amend, extend, or alter coverage.

## Intake

Gather before drafting (unless user says "use defaults" or "just draft"):

1. **Executed Access Agreement** — all exhibits, insurance schedules, riders
2. **Certificates of insurance** — ACORD 25; separate forms for auto, WC, umbrella, professional, pollution
3. **Endorsement copies** — AI (CG 20 10, CG 20 37), primary/non-contributory, waiver of subrogation
4. **Broker contact details**
5. **Project description** — scope, dates, locations, hazard level

**Defaults if no response**: Review against standard CGL/auto/WC/umbrella; flag missing endorsements as non-compliant; produce deficiency instructions for all gaps.

If endorsements are missing, request them. If user insists on proceeding, label the review as **preliminary** with all conclusions conditional.

## Step 1: Build Verification Matrix

Extract the Agreement's insurance clause into testable requirements:

| Category | What to extract |
|---|---|
| Coverage lines | CGL, auto, WC/EL, umbrella/excess, professional, pollution, cyber |
| Limits | Per-occurrence, general aggregate, products/completed-ops aggregate, CSL, EL |
| Aggregate structure | Per-project, per-location, or policy-level |
| Additional Insured entities | Exact legal names with entity suffixes (owner, manager, lender, affiliates) |
| AI scope | Ongoing only vs. ongoing + completed operations |
| Required endorsement forms | Specific ISO form numbers or "or equivalent" |
| Primary & non-contributory | Required on which lines |
| Waiver of subrogation | Required on which lines |
| Carrier rating | AM Best minimum (typically A- VII) |
| Cancellation notice | Days' notice, to whom |
| Deductible/SIR caps | Maximum amounts |
| Occurrence vs. claims-made | Which lines must be occurrence form |

**Pitfalls**: Missing completed-operations AI requirement; entity name mismatches (e.g., "ABC Management" vs. "ABC Management, LLC"); assuming umbrella follows form without proof.

## Step 2: Review ACORD 25

| Field | Verify |
|---|---|
| Named Insured | Matches Recipient entity exactly (legal name + suffix) |
| Policy dates | Spans entire access period |
| CGL form type | "Occurrence" if contract requires it |
| CGL limits | Per-occurrence, general aggregate, products/completed-ops |
| Aggregate applies per | Project/location if required (not just "Policy") |
| Auto | "Any Auto" or required symbols; CSL meets minimum |
| WC/EL | Statutory WC; EL limits; no excluded officers performing work |
| Umbrella/Excess | Limits stack to contract total; follows form to required lines |
| Certificate Holder | Being listed as Certificate Holder does NOT grant AI status |

## Step 3: Verify Additional Insured Status

1. Confirm exact AI entities required (including affiliates language)
2. Determine endorsement type:
   - **Blanket** ("when required by written contract") — needs executed contract + endorsement copy
   - **Scheduled** (named entities) — confirm schedule lists correct names
3. Verify scope:
   - Ongoing only (CG 20 10) vs. ongoing + completed (CG 20 10 + CG 20 37)
   - "Caused in whole or in part" vs. vicarious liability only — varies by edition
4. **No endorsement copies = non-compliant** — issue deficiency notice requesting AI endorsements for entities listed in the Agreement

## Step 4: Verify Remaining Requirements

**Primary & Non-Contributory**:
- Separate from AI status — AI does not automatically mean primary
- COI narrative alone insufficient; require endorsement or policy provision
- Confirm not overridden by umbrella "other insurance" clause

| Requirement | Verification |
|---|---|
| Waiver of subrogation | Endorsement on each required line — COI checkbox insufficient |
| Umbrella AI | Confirm umbrella recognizes AI status; request declarations + endorsement |
| Carrier rating | AM Best confirmation or broker attestation |
| Cancellation notice | ACORD 25 standard language confers no notice rights; require endorsement |
| Deductible/SIR | Request declarations or broker letter; flag credit risk for large SIRs |
| Description of Operations | Check for exclusionary language (geographic limits, activity exclusions) |

## Step 5: Produce Compliance Determination

```
INSURANCE COMPLIANCE REVIEW
[Privileged and Confidential — Attorney-Client Communication]

Project: [Name/Address]
Recipient: [Entity]
Agreement Date: [Date]
Review Date: [Date]
Assumptions Used: [list]
Open Items / Needed Inputs: [list]

DETERMINATION: [Compliant / Non-Compliant / Conditionally Compliant]

REQUIREMENT-BY-REQUIREMENT ANALYSIS:
| # | Requirement | Contract Ref | Status | Evidence | Deficiency |
|---|---|---|---|---|---|
| 1 | CGL $1M occ / $2M agg | §[X] | Compliant | COI shows matching limits | — |
| 2 | AI - ongoing + completed ops | §[X] | Non-Compliant | No endorsement provided | Provide CG 20 10 + CG 20 37 |

BROKER INSTRUCTIONS:
[Numbered corrective actions with exact document requests]

ESCALATION ITEMS:
[Issues requiring attorney or coverage counsel review]
```

**Drafting rules**: Use "unable to verify" not "coverage will be denied." Distinguish: "confirmed" / "indicated but not verified" / "not shown — non-compliant."

## Jurisdiction Flags

| Jurisdiction | Issue | Action |
|---|---|---|
| **New York** | Labor Law §§240/241 strict liability (gravity injuries) | Check for "Labor Law"/"Heights"/"Action Over" exclusions; escalate to coverage counsel |
| **Texas** | Anti-Indemnity Act (Ins. Code Ch. 151) | Flag if access involves construction/alteration/repair |
| **California** | Civil Code §2782 limits risk-shifting (active negligence) | Confirm indemnity + AI requirements are consistent |
| **Florida** | Fla. Stat. §627.4137 claimant rights | Note if potential claim identified |

Flag state-law issues for local counsel. Do not assert universal rules about certificate legal effect.

## Post-Draft Checklist

After delivering the review, ask:

1. Does the determination match your understanding of coverage posture?
2. Additional entities to verify as AI?
3. Any deficiencies to escalate to coverage counsel instead of broker?
4. Follow-up check needed after broker cures?

## Quality Audit

Before finalizing:

- [ ] Every Agreement requirement mapped to a testable check
- [ ] Requirement table complete with status for each coverage line
- [ ] Entity names compared character-by-character (LLC, Inc., LP suffixes)
- [ ] No compliance finding based solely on COI without endorsement verification
- [ ] Broker instructions are specific (not generic "provide adequate coverage")
- [ ] Jurisdiction flags included where applicable
- [ ] Assumptions and open items listed prominently
- [ ] Every assertion traceable to a document or labeled as assumption
- [ ] Disclaimer: not a coverage opinion; requires licensed attorney review

## Guardrails

- **COI ≠ coverage**: Never approve compliance based solely on a certificate
- **Entity names must match exactly** — mismatches defeat AI coverage at claim time
- **No coverage opinions**: Compare contract requirements to documentary evidence only
- **Privilege**: Confirm with supervising attorney; third-party sharing may waive privilege
- **Anti-hallucination**: Do not invent policy terms or coverage conclusions; use `[VERIFY]` for unconfirmed details
- **Attorney review required**: Every deliverable must disclaim that it requires licensed attorney review before reliance
