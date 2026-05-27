---
name: coi-compliance-review
title: CRE Insurance Certificate Compliance Review
description: Reviews CRE insurance certificates (ACORD 25) and endorsements against Access Agreement insurance requirements, producing a pass/fail compliance determination with broker-ready deficiency instructions. Verifies coverage limits, Additional Insured status, primary/non-contributory language, waiver of subrogation, umbrella alignment, and carrier qualifications. Use when reviewing COIs, ACORD forms, vendor or contractor insurance, site access insurance, or Additional Insured endorsements in commercial real estate transactions.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/coi-compliance-review
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: insurance
language: en
tags: [analysis, checklist, transactional]
---

# CRE Insurance Certificate Compliance Review

Reviews ACORD 25 certificates and endorsements against a CRE Access Agreement's insurance requirements, producing a defensible compliance determination with deficiency instructions.

## Prerequisites

1. **Access Agreement** — executed or signature-ready, with all exhibits, insurance schedules, riders, and property rules
2. **All COIs** — ACORD 25 (CGL); separate forms for auto, WC/EL, umbrella/excess, professional, pollution, builder's risk as required
3. **Endorsements** — Additional Insured (e.g., CG 20 10, CG 20 37), primary/non-contributory, waiver of subrogation
4. **Recipient details** — insurer/broker contacts; exact legal name of accessing party and all required Indemnitees
5. **Project scope** — work description, access dates, locations, heightened-risk activities (hot work, roofing, structural, environmental, confined space)

If endorsements are required but not provided, pause and request them. If user insists, issue a **preliminary conditional review** with unverified conclusions clearly labeled.

## Quick Start

1. Build a verification matrix from the insurance clause (Step 1)
2. Run the ACORD 25 internal checklist (Step 2)
3. Verify Additional Insured endorsements (Step 3)
4. Verify Primary & Non-Contributory endorsements (Step 4)
5. Check ancillary requirements — waivers, limits, carrier rating, cancellation, SIR (Step 5)
6. Issue compliance determination with deficiency instructions (Step 6)

## Output Structure

### Step 1 — Build Verification Matrix

Extract all insurance clause requirements into testable items before reviewing any COI:

| Requirement | Contractual Standard | Evidence Required |
|---|---|---|
| CGL form | Occurrence (not claims-made) | COI policy type field |
| CGL per-occurrence | $[X] | COI limits box |
| CGL general aggregate | $[X] | COI limits box |
| Products/Completed Ops agg | $[X] | COI limits box |
| Aggregate basis | Per project / Per location / Policy | COI "Limits Apply Per" field |
| Auto CSL | $[X] / "Any Auto" | COI auto section |
| WC / EL | Statutory; $[X] each accident/disease | COI WC/EL section |
| Umbrella/Excess | $[X] over scheduled underlying | Umbrella COI + declarations |
| Additional Insured — ongoing | [Exact entity names] | CG 20 10 or equivalent |
| Additional Insured — completed ops | [Exact entity names] | CG 20 37 or equivalent |
| Primary & Non-Contributory | When required by contract | PNC endorsement |
| Waiver of Subrogation | CGL / WC / Auto | Per-line endorsements |
| Carrier rating | AM Best A- VII or better | Broker attestation |
| Cancellation notice | [X] days | Endorsement or covenant |
| Deductible / SIR cap | $[X] max | Declarations or broker letter |

Flag ambiguous clause language (e.g., "as acceptable to Owner") for client confirmation before issuing a determination.

### Step 2 — ACORD 25 Internal Review

- [ ] Named Insured matches Recipient's exact legal name and entity suffix
- [ ] Producer contact information present
- [ ] Policy dates cover entire access period (+ completed ops tail if required)
- [ ] CGL form type: **Occurrence** (claims-made = non-compliant absent contract exception)
- [ ] CGL per-occurrence, general aggregate, products/completed ops aggregate meet minimums
- [ ] "Limits Apply Per" matches contract (Policy vs. Per Project vs. Per Location)
- [ ] Auto: "Any Auto" or required symbols; CSL meets minimum
- [ ] WC: Statutory box checked; EL limits meet minimums; proprietor/officer exclusions noted
- [ ] Umbrella/Excess: present, limits confirmed, form type noted
- [ ] Description of Operations: no suspicious exclusions (geographic carve-outs, Labor Law exclusions)
- [ ] "Certificate Holder" not treated as equivalent to "Additional Insured"

> COI is an informational snapshot only. It does not amend, extend, or alter policy coverage. All compliance conclusions depend on underlying endorsements.

### Step 3 — Additional Insured Verification

Required evidence: actual endorsement (blanket or scheduled), not COI checkbox alone.

| Check | Standard |
|---|---|
| Endorsement type | Blanket ("when required by written contract") or scheduled with exact entity names |
| Ongoing operations | ISO CG 20 10 04 13 or equivalent |
| Completed operations | ISO CG 20 37 04 13 or equivalent — required if contract demands it |
| AI scope | "Caused in whole or in part" vs. vicarious-only — quote operative language |
| Entity name match | Exact match including entity suffix (LLC, LP, Inc.) and affiliate/lender extensions |
| Umbrella AI | Confirm umbrella extends AI; otherwise AI coverage capped at CGL limits |

Sample deficiency language:
> "The COI indicates AI status; however, the Agreement requires Owner, Manager, and Lender as Additional Insureds for ongoing and completed operations. Provide copies of AI endorsements (ISO CG 20 10 and CG 20 37 or equivalents) confirming AI status for both phases and each entity listed in Section __ of the Agreement."

### Step 4 — Primary & Non-Contributory Verification

- [ ] Contract requires P&NC — confirmed in writing?
- [ ] **Endorsement provided** confirming P&NC when required by written contract?
- [ ] Endorsement scope: ongoing ops only, or completed ops as well?
- [ ] Umbrella "other insurance" clause does not override P&NC at CGL level?

Without a P&NC endorsement, client's insurer may be forced to contribute — treat as **non-compliant**.

### Step 5 — Ancillary Requirements

**Waiver of Subrogation** — verify endorsement per line (CGL, WC, Auto). COI checkmark alone is insufficient; WC waiver typically requires a specific form.

**Limits** — combined CGL + umbrella must meet contract total minimum. Confirm umbrella underlying schedule includes CGL, auto, and EL. Verify products/completed ops aggregate.

**Carrier rating** — AM Best minimum per contract (typically A- VII). COI does not show ratings; require broker attestation. Flag for re-verification on renewal.

**Cancellation notice** — modern ACORD 25 does not guarantee insurer-to-holder notice. Require contractual covenant to notify; flag as soft control only.

**Deductibles / SIR** — COI does not reliably show deductibles. If contract caps SIR, require declarations page or broker letter. Large SIR means Recipient self-insures first layer; flag credit risk.

### Step 6 — Compliance Determination

```text
COMPLIANCE STATUS: [COMPLIANT / NON-COMPLIANT / CONDITIONALLY COMPLIANT]

SUMMARY: [1-2 sentence bottom line]

REQUIREMENT-BY-REQUIREMENT FINDINGS:
[Table: Requirement | Status | Evidence | Gap/Action]

DEFICIENCIES (broker-ready):
1. [Specific item — exact entity name, exact limit, exact form needed]

ESCALATION RECOMMENDATION: [Yes/No — reason]

ACCESS RECOMMENDATION:
- Compliant: Access may proceed.
- Non-compliant / Conditional: Access not recommended until resolved. If business grants access, document as exception and identify mitigations.

ATTORNEY REVIEW REQUIRED: Draft risk-control assessment, not a coverage opinion. Confirm with supervising attorney and broker before reliance.
```

**Escalate to coverage counsel when:**
- Recipient cannot produce required endorsements
- Endorsement language materially narrower than contract requirement
- Carrier rating below contractual minimum
- Heightened-risk work (NY construction, hazmat, structural)
- Insurance terms internally inconsistent

## Guidelines

- **COI does not equal policy.** Never confirm coverage without endorsement-level evidence for AI, P&NC, and waiver of subrogation
- **Entity names:** exact match required — punctuation, suffix, affiliates. Mismatch = AI coverage gap
- **Completed ops:** separately confirm; many blanket AI endorsements cover ongoing operations only
- **Claims-made CGL:** non-compliant for CRE access absent explicit contract exception
- **Umbrella:** verify AI status and underlying schedule; "follows form" is not self-proving
- **Privilege:** label output "Privileged and Confidential" if directed by supervising attorney
- **[VERIFY]** any case citations or statutory interpretations not confirmed by contemporaneous research

**Jurisdiction flags — escalate to local counsel:**

| State | Issue |
|---|---|
| New York | Labor Law §§ 240/241 strict liability; check for "Action Over," "Labor Law," or "Heights" exclusions; NY Ins. Law § 3426 cancellation rules |
| Texas | Insurance Code Ch. 151 anti-indemnity may limit AI enforceability in construction contracts |
| California | Civil Code § 2782 limits risk-shifting for owner's active negligence in construction |
| Florida | Fla. Stat. § 627.4137 claimant rights to certified policy copies |

Do not assert universal rules on COI legal effect, P&NC enforceability, or anti-indemnity statutes across jurisdictions.

## Troubleshooting

- **Endorsements missing but COI shows AI checkbox:** COI checkbox is informational only. Request actual endorsement copies before issuing a compliant determination.
- **Entity name mismatch:** Even minor discrepancies (e.g., "LLC" vs. "L.L.C.") can void AI coverage. Flag for correction.
- **Umbrella "follows form" without AI confirmation:** Do not assume umbrella extends AI. Request umbrella declarations or endorsement confirming AI status.
- **Contract requires completed ops AI but only CG 20 10 provided:** CG 20 10 covers ongoing operations only. Request CG 20 37 or equivalent for completed operations.
- **User insists on determination without endorsements:** Issue as "Conditionally Compliant" with each unverified item explicitly labeled as unconfirmed.
