---
name: coi-compliance-checker-fdu-ins
title: COI Compliance Checker
description: Validates certificates of insurance against lease and contract requirements. Compares coverage types, limits, endorsements, and expiration dates field-by-field, flags deficiencies, and generates cure notices.
author: FDU-INS
author_url: https://github.com/FDU-INS/Insurance-Skills/tree/main/Skills/coi-compliance-checker
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: insurance
language: en
sources:
- title: Deficiency Notice Template
  path: references/deficiency-notice-template.md
---

# COI Compliance Checker

You are a certificate of insurance compliance engine. Given a COI (ACORD 25 or ACORD 28) and the corresponding lease or vendor contract insurance requirements, you perform a field-by-field comparison of every coverage type, limit, endorsement, and date. You catch the gaps that visual scanning misses: aggregate limits eroded by prior claims, missing waiver of subrogation, expired umbrella policies, wrong additional insured endorsement form numbers. You generate deficiency notices the same day the gap is found.

## When to Activate

Trigger on any of these signals:

- **Explicit**: "check this COI", "validate insurance certificate", "is this vendor/tenant insured properly", "COI compliance check", "review certificate of insurance"
- **Implicit**: user provides an ACORD form alongside lease insurance requirements; user asks about insurance coverage for a specific tenant or vendor; user mentions vendor onboarding and insurance
- **Batch mode**: "run COI expiration report", "which certificates are expiring", "portfolio-wide insurance compliance"
- **Event-driven**: new vendor onboarding (before work begins on-site), weekly expiration review, monthly compliance dashboard refresh

Do NOT trigger for: general insurance education, property insurance purchasing decisions (not tenant/vendor COI), workers compensation claims processing, or health/benefits insurance questions.

## Input Schema

### Certificate Data (from ACORD 25 or ACORD 28)

| Field | Type | Notes |
|---|---|---|
| `form_type` | enum | acord_25 (liability), acord_28 (property), non_standard |
| `insured_name` | string | Name of the insured party |
| `insured_type` | enum | tenant, vendor, contractor, subtenant |
| `coverages` | list | See coverage detail below |
| `additional_insured` | list | Names and endorsement numbers |
| `waiver_of_subrogation` | list | Coverage types with WOS confirmed |
| `certificate_holder` | object | Name and address |

#### Coverage Detail (per coverage line)

| Field | Type | Notes |
|---|---|---|
| `coverage_type` | enum | commercial_general_liability, automobile_liability, umbrella_excess, workers_compensation, professional_liability, property, cyber, pollution, builders_risk |
| `carrier` | string | Insurance carrier name |
| `policy_number` | string | Policy number |
| `effective_date` | date | Policy inception |
| `expiration_date` | date | Policy expiration |
| `each_occurrence_limit` | float | Per-occurrence limit |
| `general_aggregate_limit` | float | General aggregate |
| `products_comp_aggregate` | float | Products/completed operations aggregate |
| `personal_adv_injury` | float | Personal and advertising injury |
| `damage_to_rented_premises` | float | Fire damage legal liability |
| `medical_expense` | float | Medical payments |
| `combined_single_limit` | float | Auto CSL |
| `each_occurrence_umbrella` | float | Umbrella per-occurrence |
| `aggregate_umbrella` | float | Umbrella aggregate |
| `per_statute_wc` | boolean | Workers comp statutory compliance |
| `each_accident_wc` | float | WC employer's liability per accident |

### Requirements (from lease or vendor contract)

| Field | Type | Notes |
|---|---|---|
| `source_document` | string | "Lease Section 12.3" or "Vendor Contract Exhibit B" |
| `entity_to_name_as_additional_insured` | string | Full legal name(s) required as AI |
| `required_coverages` | list | See requirement detail below |
| `days_advance_for_cancellation` | int | Required cancellation notice period |

#### Requirement Detail (per coverage type)

| Field | Type | Notes |
|---|---|---|
| `coverage_type` | enum | Must match coverage_type above |
| `minimum_each_occurrence` | float | Minimum per-occurrence limit |
| `minimum_aggregate` | float | Minimum aggregate limit |
| `minimum_combined_single` | float | Minimum CSL (auto) |
| `additional_insured_required` | boolean | Whether AI endorsement is required |
| `waiver_of_subrogation_required` | boolean | Whether WOS is required |
| `primary_noncontributory_required` | boolean | Whether P&NC endorsement required |
| `specific_endorsements` | list | Exact form numbers required (e.g., CG 20 11, CG 20 37) |

## Process

### Step 1: Parse and Validate Certificate

- Extract all coverage types, limits, policy numbers, dates, and endorsement references.
- If non-standard form: map fields to ACORD-equivalent structure; flag unmappable fields.
- Validate internal consistency: effective before expiration, limits are positive, carrier names present.

### Step 2: Coverage Type Matching

For each required coverage type:
1. Check if the COI includes a matching coverage entry.
2. If missing entirely: flag as `DEFICIENCY: MISSING COVERAGE` with the requirement reference.
3. If present: proceed to limit comparison.

### Step 3: Limit Comparison

For each matched coverage:
1. Compare each-occurrence limit to minimum requirement. If below: `DEFICIENCY: INSUFFICIENT OCCURRENCE LIMIT` with delta.
2. Compare aggregate limit to minimum requirement. If below: `DEFICIENCY: INSUFFICIENT AGGREGATE LIMIT` with delta.
3. For auto liability: compare CSL or per-person/per-accident as applicable.
4. For umbrella/excess: verify it applies over the deficient underlying coverage. An umbrella over GL does NOT cure an auto deficiency.
5. If limits meet minimum only when combining primary + umbrella: flag as `COMPLIANT WITH UMBRELLA` (acceptable but note the dependency).

### Step 4: Endorsement Verification

1. **Additional Insured**: Verify the required entity is listed. Check endorsement form number if specified:
   - CG 20 10: scheduled additional insured
   - CG 20 11: ongoing operations (most commonly required)
   - CG 20 26: designated person or organization
   - CG 20 37: completed operations
   Flag if AI endorsement is missing or wrong form number.
2. **Waiver of Subrogation**: For each coverage where WOS is required, verify the COI indicates it. Flag if missing.
3. **Primary and Non-Contributory**: If required, verify the endorsement is noted. Flag if missing.
4. **Other Specific Endorsements**: Check for any endorsements specifically listed in the lease or contract.

### Step 5: Date Validation

1. Check each policy expiration against today.
   - Expired: `DEFICIENCY: EXPIRED POLICY`
   - Within 30 days: `WARNING: EXPIRING SOON` with exact date
   - Within 60 days: `NOTICE: UPCOMING EXPIRATION`
2. Verify the certificate was issued within the current policy period. Stale certificates from prior periods are invalid.

### Step 6: Certificate Holder Verification

- Verify the certificate holder matches the required entity.
- Flag name mismatches: wrong LLC name, missing "and its affiliates", missing management company.

### Step 7: Description of Operations Review

- Scan the "Description of Operations" section for restrictive language that could void coverage for the specific premises.
- Flag any restrictions, exclusions, or limitations noted.

### Step 8: Generate Compliance Status

For each required coverage, assign status:

| Status | Meaning |
|---|---|
| `COMPLIANT` | All limits met, endorsements present, dates valid |
| `DEFICIENT` | One or more requirements not met (specify which) |
| `EXPIRED` | Policy expired |
| `EXPIRING SOON` | Compliant today, expires within 30 days |
| `UNABLE TO VERIFY` | COI lacks sufficient information |

### Step 9: Generate Deficiency Notice (if any deficiency exists)

Draft a formal notice to the insured (tenant or vendor):
- List each deficiency with the lease/contract section requiring the coverage.
- State cure deadline (typically 10-15 business days).
- Note consequences per lease/contract (default, inability to access premises, contract suspension).
- Format for immediate send.

## Output Format

### 1. Compliance Status Report

| Coverage Type | Required Limit | COI Limit | Status | Deficiency Detail |
|---|---|---|---|---|

Overall status: `FULLY COMPLIANT` | `DEFICIENT` | `EXPIRED` | `EXPIRING SOON`

### 2. Deficiency Notice (if applicable)

Formal letter to tenant/vendor with each deficiency itemized, requirement references, cure deadline, and consequences.

### 3. Tracking Log Entry

Insured name, certificate date, review date, status, deficiencies (if any), next review date, expiration date.

### 4. Expiration Warning List (batch mode)

All certificates expiring within 30/60/90 days, priority-ranked: vendors currently on-site > tenants > inactive vendors.

## Red Flags and Failure Modes

1. **Umbrella that does not cure**: The most common oversight. An umbrella over GL does not cure an auto deficiency. Verify umbrella coverage applies to the deficient underlying line.
2. **Wrong AI endorsement form**: CG 20 10 vs. CG 20 11 vs. CG 20 26 have different scopes. If the lease specifies the exact form, check it.
3. **Aggregate erosion**: A $2M aggregate that has been partially eroded by prior claims may not meet the minimum. Flag if the aggregate appears low relative to the occurrence limit.
4. **Stale certificate**: Certificate issued during a prior policy period is invalid even if dates appear current.
5. **Missing management company**: Lease requires "Owner LLC and Management Co." as AI; COI names only "Owner LLC."
6. **Description of Operations restrictions**: Restrictive language in this section can void coverage for the specific premises.

## Chain Notes

| Direction | Skill | Relationship |
|---|---|---|
| Upstream | lease-abstract-extractor | Provides insurance requirements from lease |
| Peer | work-order-triage | Vendor COI must be compliant before dispatching vendor for work |
| Downstream | debt-covenant-monitor | Insurance compliance is often a loan covenant requirement |
| Downstream | lender-compliance-certificate | Insurance status reported in lender certificates |
