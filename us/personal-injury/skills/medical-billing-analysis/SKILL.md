---
name: medical-billing-analysis
title: Medical Billing Analysis
description: 'Produces a litigation-ready analysis of medical bills and supporting records for personal injury, medical-malpractice, workers''-compensation, and disability cases. Validates CPT/HCPCS/ICD-10 codes against documentation, applies a per-charge causation screen, runs a UCR/FAIR Health/MPFS reasonableness review, surfaces unbundling, upcoding, duplicate and phantom billing, flags letter-of-protection inflation, identifies collateral-source and lien interfaces, and outputs a memo whose every finding cites document, page, and Bates. Trigger on: medical billing analysis, medical bill audit, billing reasonableness review, UCR review, CPT/ICD code review, NCCI/unbundling/upcoding review, billed vs. paid analysis, letter of protection (LOP) analysis, collateral source review, chargemaster markup, causation chain, IME rebuttal prep, demand-package billing exhibit, mediation statement billing section, lien interface identification.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/medical-billing-analysis
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: personal-injury
language: en
tags: [litigation, analysis, summary]
---

# Medical Billing Analysis

A medical-billing analysis is simultaneously the spine of the damages case and a future exhibit at deposition, mediation, and trial. A defective analysis (invented UCR figures, missed unbundling, undocumented charges treated as valid, pre-existing same-body-part treatment not flagged, lien holders not identified) either understates the case or hands opposing counsel impeachment material. This skill produces a memo where every charge is reconciled, every code is checked against the chart, every finding cites document/page/Bates, every red flag carries a stable taxonomy ID, and every jurisdictional assumption is surfaced for counsel.

The skill is **billing-side**: it does not value the case, draft the demand, build the full chronology, or resolve liens. It hands those off to sibling skills.

---

## Related skills

- `medical-record-chronology` — full date-ordered treatment narrative; consume it, do not rebuild
- `medical-treatment-summary` — narrative course of treatment
- `damages-calculator` — valuation, multipliers, present value; this skill feeds it the billing-side line items
- `lien-resolution-summary` — Medicare/Medicaid/ERISA/hospital liens; identify here, resolve there
- `ime-report-analysis`, `expert-medical-record-omissions` — defense-side rebuttal prep
- `pi-demand-summary`, `demand-letter`, `mediation-statement` — downstream consumers
- `hipaa-release` — verify authorization scope before requesting records

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

Ask every time unless the user says "use defaults" or "just draft." Record gaps explicitly; do not silently proceed.

**Required**

1. **Incident facts** — date, mechanism, body parts claimed, jurisdiction, liability posture
2. **HIPAA release scope** — what records are authorized; whether 42 C.F.R. Part 2 SUD records are in scope
3. **Medical records** — every provider (ER, inpatient/operative, imaging, PT/OT/chiro, pain management, behavioral health, pharmacy, DME)
4. **Itemized bills at CPT/HCPCS level** — UB-04 for facilities, CMS-1500 for professionals; not totals
5. **EOBs** — for every claim (billed / allowed / paid / adjustment / patient responsibility)
6. **Lien statements** — Medicare (CMS conditional payment letter), Medicaid, ERISA plan, hospital/provider, workers' comp, VA/Tricare
7. **Pre-incident records** — same body parts, baseline function, medications

**As applicable**

8. **Letters of protection** — flag every LOP-billed line for RF-12 review
9. **IME or peer-review reports**
10. **Life care plan** — if future medicals at issue

**Defaults if user does not respond** (label every default in the output):
- Analyze chronologically; carry billed and paid as separate columns
- Flag treatment gaps > 30 days
- Apply three-prong causation screen per charge (temporality, consistency, medical necessity)
- Flag every jurisdictional rule `[VERIFY]`

**Missing-material policy.** Proceed with what's available. List missing categories in Section 4 (Open Items) of the output. Do not produce reasonableness or causation conclusions on a provider whose itemized bill is absent — name the gap and stop.

---

## Workflow

### Step 1 — Build Document Inventory & Bates-Map

Classify each document, assign a short stable `doc-label`, record Bates range and OCR status. Use the categories listed in `references/OUTPUT-TEMPLATE.md` Section 5. The `doc-label` carries through every citation in the memo.

### Step 2 — Reconcile Billing Arithmetic

For each provider, verify: **billed = paid + contractual adjustments + patient responsibility + outstanding balance**. Record the per-provider reconciliation row (Section 7 of the output). Any failure to reconcile is itself a flag — identify the underlying cause (RF-04 duplicate, RF-05 phantom, an unrecorded adjustment, or a data-entry error) and record it. Do not paper over a delta; show it.

### Step 3 — Validate Codes (CPT / HCPCS / ICD-10)

Per charge, check that:
- The code is valid for the date of service (CPT/HCPCS year, ICD-10-CM specificity).
- The code descriptor matches what the chart documents (procedure verb, anatomy, components).
- The diagnosis on the claim supports the procedure billed.
- Modifiers (`-25`, `-59`, X-modifiers, `-26`, `-TC`, `-50`, `-RT`/`-LT`, `-51`, `-22`) are used correctly.

Detailed mechanics, modifier-misuse catalog, NCCI/MUE framing, and DRG considerations: see [references/CODE-VALIDATION.md](references/CODE-VALIDATION.md). Never assert a code-text mapping from memory; cite the AMA codebook or CMS file, or label `[VERIFY: billing expert]`.

### Step 4 — Apply Causation Screen (per charge)

Three prongs, all required, applied to every billed line item:
- **Temporality** — treatment began promptly for the complained-of body parts
- **Consistency** — complaints documented throughout the course of care
- **Medical necessity** — care relates to the diagnosis and the mechanism of injury

Failures get tagged "potentially contested — attorney review" in Section 7's Notes column and surface as red flags (RF-23 through RF-28 as applicable). The causation screen is the same screen used by `damages-calculator` Step 2 — keep terminology aligned.

### Step 5 — Run Reasonableness Review

Produce a benchmark **range**, not a single "reasonable amount." Use FAIR Health, MPFS, state WC fee schedules, and the case's own EOB allowed amounts. Geographic adjustment (geozip/locality) matters. Letter-of-protection lines get extra scrutiny.

Methodology, source list, percentile presentation, billed-vs-paid integration, and "when to recommend a billing expert" thresholds: see [references/REASONABLENESS-METHODOLOGY.md](references/REASONABLENESS-METHODOLOGY.md). Never quote a benchmark figure that was not actually retrieved; if no benchmark was run, say so and recommend a billing expert.

### Step 6 — Flag Red Flags (taxonomy IDs)

Use the stable IDs in [references/RED-FLAGS-CATALOG.md](references/RED-FLAGS-CATALOG.md). Categories: billing integrity (RF-01–RF-10), reasonableness (RF-11–RF-14), referral patterns (RF-15–RF-17), documentation (RF-18–RF-22), causation (RF-23–RF-28), IME/peer-review (RF-29–RF-31), liens/collateral source (RF-32–RF-35).

Each row in Section 11 of the output: ID | Name | Detail | Source | Suggested Attorney Action | Severity (H/M/L). Sort H → M → L. If a finding doesn't match any ID, mark it `[NEW PATTERN — review needed]` rather than inventing a permanent ID.

### Step 7 — Identify Collateral-Source / Lien Interfaces

Identify lien holders (Medicare, Medicaid, ERISA plan, hospital/provider, workers' comp, VA/Tricare), record amounts asserted and notice status, and **hand off** to `lien-resolution-summary`. Do not negotiate, reduce, or resolve. Surface the billed-vs-paid jurisdictional rule for counsel; do not pick the measure unilaterally.

### Step 8 — Produce Final Report

Follow [references/OUTPUT-TEMPLATE.md](references/OUTPUT-TEMPLATE.md) section by section. Run the Pre-Delivery Checks at the bottom of that file before declaring the draft complete. The privilege header, citation format (`[doc-label, p. N, Bates XXXXXX]`), and the `[F]`/`[A]`/`[O]` tagging convention are non-negotiable.

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

After delivering the draft, ask:

1. Additional providers or itemized bills still outstanding?
2. Client explanation for any treatment gap > 30 days, or for pre-existing same-body-part care?
3. Billed-vs-paid measure for this jurisdiction — which does counsel want presented as primary?
4. Specific causation disputes (IME contrary opinions) requiring deeper analysis?

If no response: recommend obtaining the missing provider's itemized bills (highest-value gap) and flag the billed-vs-paid jurisdiction question as the next decision. Proceed with the draft as authorized.

---

## Quality Audit

- [ ] Every finding cites document, page, and Bates (or is explicitly labeled unbated and listed in Open Items)
- [ ] Per-provider billing arithmetic reconciled in Section 7; deltas shown, not hidden
- [ ] CPT/HCPCS codes validated against documentation; modifier use checked per [references/CODE-VALIDATION.md](references/CODE-VALIDATION.md)
- [ ] ICD-10-CM diagnoses match billed procedures; specificity and 7th-character encounter type checked
- [ ] Causation screen applied to every charge; failures flagged with the appropriate RF-23–RF-28 ID
- [ ] Reasonableness benchmark source named (FAIR Health, MPFS, state WC, EOB allowed amounts) and tagged `[VERIFY]`
- [ ] Billed and paid carried as separate columns until counsel selects the primary measure
- [ ] LOP-billed line items individually tagged; RF-12 considered for each
- [ ] Red flags use stable IDs from [references/RED-FLAGS-CATALOG.md](references/RED-FLAGS-CATALOG.md), sorted H → M → L
- [ ] Pre-existing same-body-part treatment distinguished from incident-related; RF-26 surfaced if not addressed
- [ ] IME / peer-review opinions cataloged separately from treating physician findings
- [ ] Lien holders identified in Section 12 only; not resolved (handed to `lien-resolution-summary`)
- [ ] Jurisdictional rules flagged `[VERIFY]` (billed-vs-paid, hospital lien statute, statutory caps, No Surprises Act)
- [ ] Missing records listed in Section 4 (Open Items); no findings made on absent records
- [ ] No invented codes, FAIR Health percentiles, NCCI edit pairs, MPFS rates, verdict figures, or citations
- [ ] Privilege header present; Section 15 attorney-review boilerplate present verbatim

---

## Jurisdictional Flags

A short reference for the agent or paralegal to surface in Section 14. Not a substitute for counsel research. Every entry tagged `[VERIFY]`.

- **California** — paid-only measure for past medical specials per *Howell v. Hamilton Meats & Provisions, Inc.*, 52 Cal. 4th 541 (2011) `[VERIFY current law]`
- **Collateral-source-rule jurisdictions (e.g., New York)** — billed amounts may be admissible as evidence of value; collateral payments cannot be used to reduce `[VERIFY current law in jurisdiction]`
- **Reasonable-value jurisdictions** — present billed, paid, and a UCR benchmark band; let the fact-finder decide `[VERIFY current law]`
- **Medicare Secondary Payer** — 42 U.S.C. § 1395y(b); Section 111 reporting; CMS conditional payment letter required before settlement when patient is a Medicare beneficiary `[VERIFY current CMS process]`
- **ERISA plan reimbursement** — *US Airways, Inc. v. McCutchen*, 569 U.S. 88 (2013); *FMC Corp. v. Holliday*, 498 U.S. 52 (1990); made-whole and common-fund doctrines generally do not apply against self-funded ERISA plans `[VERIFY plan language]`
- **Hospital lien statutes** — many states cap or reduce; cite the specific state statute and check perfection requirements `[VERIFY statute]`
- **No Surprises Act (federal, 2022 effective)** — balance-billing protections for emergency services and out-of-network providers at in-network facilities `[VERIFY current regs]`
- **Letter of protection admissibility** — many jurisdictions allow impeachment on referral source, factoring, and collection patterns; some recent appellate developments `[VERIFY current law in jurisdiction]`
- **Per diem / multiplier limits and statutory damages caps** — vary by state and case type `[VERIFY]` (consult `damages-calculator`)

---

## Anti-Hallucination Rules

- Never invent CPT/HCPCS/ICD-10 codes, modifier meanings, or NCCI edit pairs
- Never quote a FAIR Health percentile, MPFS rate, or hospital posted price not actually retrieved (cite URL/file/date or label "benchmark not obtained")
- Never quote a causation statement that is not in the cited record
- Tag every legal citation `[VERIFY]` unless it appears verbatim in a sibling skill in this repo
- Distinguish fact (`[F]`), assumption (`[A]`), and opinion (`[O]`) in Sections 9–11 of the output

---

## What This Skill Does NOT Do

- Does not value the case (use `damages-calculator`)
- Does not resolve, negotiate, or satisfy liens (use `lien-resolution-summary`)
- Does not produce expert testimony — billing experts (CPC/CCS/CPMA) and medical experts are required for admissibility on contested issues
- Does not opine on ultimate legal conclusions (liability, damages amount, causation in law)
- Does not draft the demand letter, mediation statement, or trial exhibit list (use the named sibling skills)
- Does not replace attorney review of the final memo

---

## Attorney Review Required

This skill produces attorney work product. The memo derives entirely from documentation listed in its Section 2 and assumptions stated in its Section 3. Jurisdictional rules flagged `[VERIFY]` must be confirmed by counsel before reliance. No output of this skill may be sent outside the legal team without attorney review and approval.
