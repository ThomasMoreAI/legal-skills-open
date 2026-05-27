---
name: insurance-certificate-compliance-check
title: Insurance Certificate Compliance Check
description: 'Performs contract-driven compliance review of insurance certificates and endorsements against CRE/site-access and vendor agreement requirements. Produces pass/fail/conditional determinations, deficit lists, and broker-ready remediation instructions. Use when reviewing COI packets, ACORD 25 forms, or endorsements for additional insured, primary and non-contributory, waiver of subrogation, completed operations, umbrella alignment, limits adequacy, or insurer rating compliance. Trigger terms: COI, ACORD, additional insured, certificate holder, cancellation notice.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/insurance-certificate-compliance-check
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: insurance
language: en
---

# Insurance Certificate Compliance Check

Compares Access Agreement insurance requirements to COI and endorsement evidence to produce a defensible compliance determination with actionable deficit remediation.

## Prerequisites

1. Access Agreement (final) with insurance clause, exhibits, and amendments
2. COIs for all required lines: CGL, auto, WC/EL, umbrella, specialty
3. Endorsement copies: AI, completed-ops AI, primary/non-contributory, waiver of subrogation, umbrella schedule
4. Recipient legal names, required AI entities, project scope
5. Access dates, locations, post-completion carry-forward period
6. Governing law / jurisdiction
7. Delivery recipients and privilege instructions

## Quick Start

1. Extract all insurance requirements from the agreement into a requirements matrix
2. Run COI baseline checks against each requirement
3. Verify endorsement-level evidence for every core element — COI text alone is non-binding
4. Assess risk and coverage-structure gaps
5. Apply jurisdiction-specific considerations
6. Output compliance determination with deficit list

## Workflow

### Step 1: Build Requirements Matrix

Extract from agreement into normalized rows:

| Category | Extract | Normalize to |
|---|---|---|
| Coverage types | CGL, auto, WC/EL, umbrella, specialty | `[line]: [form/limits/scope]` |
| Limits | Occurrence, aggregate, products-completed, per location/project | Numeric minimums + frequency |
| AI scope | Named entities and affiliates | Exact legal names + ongoing/completed |
| Priority terms | Primary/non-contributory | Which policies/lines |
| Waiver of subrogation | Which lines require waiver | CGL/WC/auto/property |
| Notice/ratings | Cancellation notice, AM Best, insurer status | Required evidence |
| Special clauses | Exclusions, endorsements by form number | Must be checked |

Flag vague clauses (`acceptable`, `sufficient`, `as required by owner`) as **Attorney Clarification Required**.

### Step 2: COI Baseline Checks

These are information-only — not proof of coverage:

1. Named insured matches recipient entity exactly (name + suffix + related entity logic)
2. Policy period covers access window
3. Required coverages and limits appear in correct fields
4. Occurrence vs claims-made confirmed
5. Aggregate designations align (`per occurrence`, `per location`, `per project`)
6. Producer/broker contact present
7. Red flags: expired/expiring policies, wrong entity, missing policy numbers

If incomplete, set `Conditionally Compliant` and list missing documents.

### Step 3: Endorsement Verification

COI text alone is non-binding. Require endorsement-level evidence for each:

| Element | Required | Common failure |
|---|---|---|
| Additional insured | Endorsement naming exact entities | Blanket AI with entity mismatch |
| Completed-ops AI | Separate completed-ops endorsement | Only ongoing AI provided |
| Primary/non-contributory | PNC clause/endorsement for AI | PNC on COI only |
| Umbrella alignment | AI/PNC in underlying + umbrella schedule | No schedule showing extension |
| Waiver of subrogation | Endorsement on required lines | Narrative in COI only |
| Cancellation notice | Enforceable mechanism documented | Reliance on ACORD boilerplate only |

### Step 4: Risk and Coverage-Structure Checks

1. Verify minimum limits vs exposed values per line and project
2. Compute combined limits where umbrella augments GL/auto/EL
3. Check for coverage-exclusion conflicts (geographic, type-of-work, access-specific)
4. Review deductibles/SIR if high-risk or large retention (from declarations/broker attestation)
5. Confirm insurer rating with explicit evidence

### Step 5: Jurisdiction Adaptation

Apply `[VERIFY]` to all jurisdiction-specific conclusions:

- **New York**: Construction gravity-risk and labor-law exclusions `[VERIFY]`
- **Texas**: Anti-indemnity impact on AI enforcement `[VERIFY]`
- **California**: Active-negligence/AI enforceability constraints `[VERIFY]`
- **Florida**: Policy disclosure and insurer-info rights `[VERIFY]`

If governing law is uncertain, mark all jurisdictional conclusions as **requires legal verification**.

### Step 6: Output

```
Result: [Compliant | Conditionally Compliant | Non-Compliant]
Jurisdiction: [state]
Coverage period tested: [start] to [end]
Review confidence: [High | Medium | Low]

Requirements Matrix:
- Requirement | Evidence | Status | Finding | Deficiency
- ...

Escalation: [In-house counsel / Risk manager / Coverage counsel]
Access decision: [Recommend allow / conditional / deny pending docs]
```

Use entity-name exactness and numeric precision (`$1,000,000 each occurrence`, `CG 20 37`).

## Critical Guardrails

- COI statements are documentary indication, not contractual proof
- Never state "fully covered" without endorsement/policy support
- `Certificate holder` ≠ `additional insured` — never conflate
- Never infer AI scope from checkbox or Description of Operations alone
- For each deficit, provide precise broker instruction: exact endorsement form/edition and deadline
- Track status as `confirmed`, `indicated-not-verified`, or `not shown`
- This is a **risk-control assessment**, not a coverage legal opinion
- Include attorney review requirement before operational reliance
- If access allowed with unresolved deficits, document written exception and mitigation
- If anti-indemnity/statutory effects drive outcome, escalate immediately
- Use `[VERIFY]` on all uncited or uncertain authority claims
