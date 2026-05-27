---
name: pfs-analyzer
title: PFS Analyzer
description: Extracts and reconciles medical provider, wage-loss, and insurance/lien data from personal injury plaintiff fact sheets and initial disclosures against builder draft responses. Use when the user mentions PFS analysis, medical provider reconciliation, wage loss audit, insurance lien tracking, PI discovery reconciliation, builder response validation, MDL plaintiff data extraction, FRCP 26(a)(1) disclosures, treatment chronologies, or specials spreadsheets.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/pfs-analyzer
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: personal-injury
language: en
---

# PFS Analyzer

Extracts structured data from PI plaintiff fact sheets and initial disclosures, reconciles against draft builder responses, and produces an issues memo with variance flags and full source traceability.

All output requires attorney review before service or filing.

## Quick Start

1. Gather source documents (PFS, provider lists, wage docs, insurance disclosures, builder draft)
2. Extract providers, employers, and insurance/lien entities with source citations
3. Reconcile extractions against builder draft — flag all variances
4. Deliver builder-ready output + lawyer-facing issues memo

## Intake Checklist

Ask every time unless user says "use defaults" or "just draft":

1. **PFS / Initial Disclosures** — executed PFS, FRCP 26(a)(1) packet, or MDL CMO form
2. **Medical provider list** — specials spreadsheet, treatment chronology, HIPAA auth list
3. **Wage loss package** — employer verification, pay stubs, W-2s, tax returns
4. **Insurance disclosures** — EOBs, PIP/MedPay, lien letters, subrogation notices, Medicare/Medicaid status
5. **Client intake notes** — internal questionnaires with details possibly omitted from PFS
6. **Draft builder responses** — discovery responses to validate
7. **Forum/jurisdiction** — federal vs. state court
8. **Key context** — DOI, prior injury history, date range, cash-pay/LOP/workers' comp, pharmacy list, employment gaps >6 months

**Defaults** (if user doesn't respond): federal court, FRCP 26(a)(1) framework, all available docs, partial output if incomplete.

If any source is missing, label output **"Partial"** and identify what is absent.

## Core Workflow

### 1. Build Extraction Map

Every extracted data point must include:

| Field | Format |
|---|---|
| Source document | "Doc 1, p. 4" or Bates range |
| Verbatim text | Exact wording from source |
| Confidence | **High** (explicit with address + dates) / **Medium** (listed, missing details) / **Low** (inferred, needs verification) |

Rules:
- Untraceable facts must not be presented as extracted data
- Preserve spelling in `verbatim_name`; create separate `normalized_name`
- Never silently correct spelling, expand abbreviations, or merge duplicate-looking entities
- Distinguish treatment facility from billing entity

### 2. Extract Medical Providers

Per provider, capture: name (verbatim + normalized), type (hospital/clinic/physician/PT/imaging/pharmacy/lab/ambulance), address/phone/fax, service dates, NPI, records/bills status, category (injury-related / pre-existing / billing-lien), source citation.

Rules:
- Pre-DOI treatment → "Prior/Pre-existing" (never omit)
- Separate radiology reads, pathology, facility fees as distinct billing entities
- Referrals are not treatment encounters
- Do not collapse multiple locations of a provider network
- Flag potential non-retained treating experts
- Include pharmacies, PTs, imaging, labs — not only physicians

### 3. Extract Employment & Wage Loss

Per employer, capture: legal name (+ DBA), address/contacts, job title/schedule/pay rate (exact phrasing), start/end dates, wage documentation, injury impact (first missed date, total days, PTO, return status), benefits applied for (STD/LTD/SSDI/workers' comp).

Rules:
- Preserve vague references as "reported estimate per disclosure"
- Distinguish employer from worksite (staffing agencies)
- Capture self-employment separately
- Flag mitigation issues and employment gaps

### 4. Extract Insurance, Liens & Prior Claims

Per entity, capture: insurer/lienholder name (verbatim), plan type, member/group/claim/policy IDs (distinguish each), named insured, contact info, lien status (asserted/pending/final + amount), source citation.

Rules:
- Extract only what documents contain — never guess limits, coverage, or validity
- Letter of protection is not an insurance lien
- Silent on Medicare → flag: "Confirm Medicare beneficiary status and SSDI; may trigger MSP reporting"
- Capture prior accidents/claims/settlements; flag for builder consistency

### 5. Reconcile Against Builder Draft

Three-dimension diff:

| Dimension | Check | Flag |
|---|---|---|
| Completeness | Entity-by-entity | "Missing in builder" / "New — confirm supplementation" |
| Consistency | Names, dates, amounts | "Spelling mismatch" / "Date conflict" / "Amount discrepancy" |
| Characterization | Builder vs. disclosure | "Overstates" / "Understates" |

Priority levels:
- **RED ALERT** — Document contradictions (e.g., PFS says not working but records reference work). Requires attorney intervention before service.
- **HIGH** — Undisclosed prior accidents, missing providers, inconsistent injury mechanism
- **MEDIUM** — Spelling variations, missing addresses, incomplete date ranges
- **LOW** — Formatting issues, optional fields unpopulated

Rules:
- Never silently overwrite builder data
- Distinguish "disclosed but not produced" from "entirely undisclosed"
- Do not override intentional attorney scope narrowing — flag and defer
- Note FRCP 26(e) supplementation timing (state analogs may be stricter)

### 6. Deliver Output

**A. Builder-Ready Output**: Separate `verbatim_name`/`normalized_name`, include `source_citation` and `confidence` per record, match builder schema, include reservation language.

**B. Issues Memo** (label: DRAFT — Attorney Work Product / For Counsel Review Only):
1. Client follow-up questions
2. Supplementation needs with timing
3. Defense focus areas and impeachment vectors
4. Red flags with recommended action
5. Entity verification results (NPI checks)
6. Privilege flags — exclude attorney-client communications from extraction

## Post-Draft Check

Ask after delivering initial output:
1. Are RED ALERT/HIGH flags accurate — known explanations to incorporate?
2. Providers/employers client mentioned but absent from disclosures?
3. Generate supplementation timeline from identified gaps?
4. Builder schema match confirmed?

Default: address RED ALERT items first.

## Quality Checklist

- [ ] Every field has source citation or labeled "client to confirm"
- [ ] Forum-specific law references match actual jurisdiction
- [ ] Provider names checked against CMS NPI Registry; unverifiable names flagged
- [ ] Treatment dates consistent with DOI; pre-DOI marked "Prior"
- [ ] Date formats consistent; no false precision from estimates
- [ ] Identifiers transcribed accurately; OCR-sourced values flagged
- [ ] All provider types included (pharmacies, PTs, imaging, labs)
- [ ] No omission construable as concealment (adversarial review)
- [ ] Builder output matches schema constraints
- [ ] All variances shown — nothing silently overwritten

## Compliance Guardrails

- **ABA 1.1/1.3**: Attorney must verify; LLM extraction does not satisfy competence/diligence
- **Model Rule 1.6**: Mask identifiers in memo (last four only); full values in secure builder fields
- **Model Rules 3.3/3.4/4.1**: Distinguish documented facts from reported estimates; never assert completeness if record is incomplete
- **FRCP 37**: Incomplete provider lists are common sanctions targets
- **HIPAA**: All extracted data is PHI; handle per firm protocols
- **Conflicts**: Multiple potential claimants → flag for Model Rule 1.7 screening
- **Anti-hallucination**: Every data point traceable to source; never invent names, dates, identifiers; unverified citations must be flagged

## Jurisdiction Notes

- **Federal MDL**: Follow CMO-mandated PFS headers exactly; non-compliance risks dismissal
- **California**: CCP governs; plaintiff verification form required
- **Florida**: Align with Form 1.977 interrogatories (10-year history) [VERIFY]
- **Texas**: Map to Rule 194 Required Disclosure categories [VERIFY]
- **State auth forms**: Flag "state-specific medical authorization — attorney to confirm"
