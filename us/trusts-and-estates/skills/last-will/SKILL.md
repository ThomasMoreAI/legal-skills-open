---
name: last-will
title: Last Will and Testament
description: Drafts a state-compliant Last Will and Testament covering declarations, revocation of prior instruments, specific bequests, residuary disposition, guardian nominations, fiduciary appointments, and execution formalities. Conducts structured intake on family structure, asset inventory, fiduciary nominees, and existing estate plan documents. Coordinates with trusts, beneficiary designations, and non-probate transfers. Use when drafting wills, testamentary documents, pour-over wills, codicils, or estate planning instruments involving testamentary dispositions.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/last-will
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: trusts-and-estates
language: en
tags: [agreement, drafting, transactional]
---

# Last Will and Testament

Drafts a state-compliant Last Will and Testament reflecting the testator's intent, coordinated with their broader estate plan.

## Prerequisites

1. **Testator identity** — full legal name, residence (city, county, state), testamentary capacity confirmation
2. **Family structure** — spouse, prior marriages, all children (biological, adopted, step), minors, prenup/postnup
3. **Fiduciary nominees** — executor + alternate; guardian(s) + alternate(s) if minor children
4. **Asset inventory** — real property, personal property, business interests, digital assets
5. **Existing estate plan** — prior wills, trusts, beneficiary designations, joint tenancies, POD/TOD accounts
6. **State of domicile** — determines execution formalities, spousal rights, probate code

## Checkpoint A: Intake (Mandatory)

Gather all items below unless user says "use defaults" or provides equivalent detail.

| Category | Required Information |
|---|---|
| **Testator** | Full legal name, DOB, address (city/county/state), capacity confirmation |
| **Marital status** | Current spouse name, prior marriages, prenup/postnup existence |
| **Children** | Full names, DOBs, minor status, biological/adopted/step, intentional exclusions |
| **Executor** | Primary + alternate (full name, relationship), bond waiver preference |
| **Guardian** | Person + estate (if different), alternates, upbringing instructions |
| **Specific bequests** | Item description, beneficiary name/relationship, contingent beneficiary |
| **Residuary estate** | Primary beneficiaries + percentages, contingent beneficiaries, per stirpes vs. per capita |
| **Debts/taxes** | Residuary vs. apportionment; tax payment directives |
| **Existing plans** | Revocable trusts, life insurance, retirement designations, joint tenancies |

Search any uploaded documents (prior wills, trust agreements, family records) to extract details and ensure consistency. If materials are missing, flag explicitly and proceed with labeled assumptions.

## Output Structure

### Article I — Declarations & Revocation
- Testator identification, domicile, testamentary capacity statement
- Explicit revocation of all prior wills and codicils
- Family identification (spouse, children by name)

### Article II — Debt, Expense & Tax Payment
- Direction to pay debts, funeral expenses, administration costs
- Source of payment (residuary estate unless otherwise directed)
- Estate tax payment directive (residuary vs. apportionment)

### Article III — Specific Bequests
Per bequest: beneficiary full legal name + relationship, precise property description, contingent beneficiary, ademption language if appropriate.

### Article IV — Residuary Estate
- Primary distribution (beneficiaries + percentages)
- Contingent distribution if primary beneficiaries predecease
- Per stirpes or per capita election
- Ultimate contingency (heirs-at-law or named charity)

### Article V — Guardian Nominations (if minor children)
- Guardian of person — primary + alternate
- Guardian of estate — primary + alternate (if different)
- Reasons for selection (strengthens against challenge)
- Upbringing instructions (education, religion, care)

### Article VI — Fiduciary Appointments
- Personal representative — primary + alternate
- Bond waiver provision (if elected)
- Powers: sell/lease property, continue/liquidate businesses, tax elections, distribute in kind, invest assets, reference state probate code statutory powers

### Article VII — Administrative & Protective Provisions
- **Survivorship clause** — 30–60 day survival requirement
- **No-contest clause** — if requested (enforceability varies by state)
- **Severability clause**
- **Simultaneous death provision**

### Article VIII — Attestation & Execution
- Attestation clause per state execution requirements
- Signature blocks: testator, witnesses (2 or 3 per state law), notary
- **Self-proving affidavit** — include statutory language for testator's state

## State-Specific Compliance

| Issue | Check |
|---|---|
| **Witness count** | 2 in most states; 3 in some — verify for domicile state |
| **Self-proving affidavit** | Statutory form varies — use exact required language |
| **Community property** | AZ, CA, ID, LA, NV, NM, TX, WA, WI — characterize separate vs. community |
| **Elective share** | Non-CP states — surviving spouse can claim statutory share |
| **Pretermitted heirs** | After-born/after-adopted children — include or explicitly exclude |
| **UPC adoption** | Check if state follows Uniform Probate Code or has unique rules |
| **No-contest enforceability** | Some states void in terrorem clauses if contest brought with probable cause |
| **Electronic/holographic wills** | State-specific validity; draft for formal execution unless instructed otherwise |

## Checkpoint B: Post-Draft Alignment (Mandatory)

After delivering draft, confirm:

1. Does the distribution scheme match testator's intent (specific bequests + residuary)?
2. Are fiduciary appointments and guardian nominations correct?
3. Are there any intentional omissions that need explicit exclusion language?
4. Does the will coordinate correctly with existing non-probate transfers?

If no response, recommend next refinement based on stated objectives and proceed if authorized.

## Guidelines

- Coordinate will with all non-probate transfers (trusts, beneficiary designations, joint tenancies, POD/TOD) to avoid conflicts
- If revocable living trust exists, use pour-over will structure
- Never name the notary as a beneficiary
- Flag intentional disinheritance with explicit exclusion language to reduce contest risk
- Include execution instructions (signing order, witness requirements, notarization)
- Mark any state-specific statutory citations with `[VERIFY]` if exact code section is uncertain
- Do not fabricate statutory citations, witness requirements, or execution formalities
- **Attorney review required** — include disclaimer and execution-readiness statement in final output

---

Key changes from the original:

- **Added Checkpoint A/B pattern** — matches the `advance-health-care-directive` reference skill with mandatory intake dialog and post-draft alignment confirmation
- **Expanded description** with trigger keywords (pour-over wills, codicils, testamentary dispositions)
- **Compressed Article III** from a multi-bullet subsection into a single dense line
- **Compressed Article VI powers** from a nested sub-list into a single inline list
- **Removed redundant Client Intake Checklist** — the intake table now lives under Checkpoint A, eliminating the duplication between Prerequisites and the old checklist
- **Removed "advise on storage"** guideline (opinion, not drafting instruction)
- **Added fabrication guardrail and attorney-review line** to Guidelines, consistent with the reference skills

Please approve the file write permission so I can save this to disk.
