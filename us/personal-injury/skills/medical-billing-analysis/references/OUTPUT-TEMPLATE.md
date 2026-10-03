# Output Template — Medical Billing Analysis Memo

The deliverable structure for Step 8 of the parent SKILL.md. Section order is fixed; sections are populated even when contents are short ("None identified" or "Not obtained — see Open Items"). Do not reorder.

---

## Privilege Header (top of every output)

> **ATTORNEY WORK PRODUCT — PRIVILEGED & CONFIDENTIAL**
> Prepared at the direction of counsel in anticipation of litigation. Draft analysis requiring attorney review. Do not distribute outside the legal team.

---

## Citation Format

- Standard form: `[doc-label, p. N, Bates XXXXXX]`
- If unbated: `[doc-label, p. N]` and add a row in Open Items requesting Bates.
- Block-quote (≥ 25 words) provider language with citation immediately after the closing quote mark.
- For EOB cells: `[EOB doc-label, claim # ___, line ___]`.

## Fact / Assumption / Opinion Tags

In Causation Analysis, Reasonableness Review, and Red Flags rows, prefix each substantive sentence or row with one of:

- `[F]` — fact directly stated in the cited record.
- `[A]` — assumption made (must appear in the Assumptions table).
- `[O]` — opinion (treater, IME, or expert) — must be quoted with citation.

Where the line is purely structural (a header, a totals row), tags are unnecessary.

---

## Section 1 — Case Header

| Field | Value |
|---|---|
| Case Caption | [Plaintiff] v. [Defendant] |
| File / Matter Number | |
| Jurisdiction | |
| Date of Incident | |
| Patient DOB | |
| Date of Report | |
| Version | v0.1 / v1.0 etc. |
| Prepared By | |
| Reviewed By (attorney) | (blank until reviewed) |

## Section 2 — Documents Reviewed

Table of every record set considered:

| # | Document Label | Source / Provider | Date Range | Bates Range | Format | Notes |
|---|---|---|---|---|---|---|

Use the same `doc-label` values throughout the rest of the memo for citations.

## Section 3 — Assumptions & Limitations

| # | Assumption | Basis | Effect if Wrong |
|---|---|---|---|

Examples:
- "Itemized bills accurately reflect provider charges as billed" — basis: provided by counsel — effect: undermines arithmetic and reasonableness analyses.
- "Jurisdiction is [State]; billed-vs-paid rule per [VERIFY] applies" — basis: counsel direction — effect: changes recoverable measure.

## Section 4 — Open Items

Records or data requested but not received, in priority order:

| # | Item | Why It Matters | Status / Date Requested |
|---|---|---|---|

Do not make findings about a category whose underlying records are listed here as missing.

## Section 5 — Document Inventory

Use the categorization from SKILL.md Step 1:

| Category | Provider/Facility | Date Range | Records Obtained (Yes/Partial/No) | Bates Range |
|---|---|---|---|---|

Categories: emergency/acute, inpatient/surgical, outpatient/specialist, diagnostic imaging, therapy (PT/OT/chiro), behavioral health, pharmacy, DME, billing/financial, IME/peer review, lien notices.

## Section 6 — Medical Timeline

If a `medical-record-chronology` deliverable exists for this case, reference it: `See [chronology doc-label] for full date-ordered narrative.` Otherwise, produce a summary timeline (date | provider | visit type | key event/finding) — not a substitute for a full chronology.

## Section 7 — Billing Analysis Table

The line-item heart of the memo. Every charge appears as one row.

| Date | Provider | Facility | CPT/HCPCS | Modifier | ICD-10 | Description | Billed | Allowed | Paid | Adjustment | Patient Resp. | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|---|

Reconciliation row per provider:

| Provider | Σ Billed | Σ Paid | Σ Adjustments | Σ Patient Resp. | Σ Outstanding | Reconciles? (Y/N) |

Any "N" must be flagged in Section 11.

## Section 8 — Category Summary

| Category | Σ Billed | Σ Paid | Σ Outstanding | Notes |
|---|---|---|---|---|
| Emergency/acute | | | | |
| Inpatient/surgical | | | | |
| Diagnostic imaging | | | | |
| Therapy (PT/OT/chiro) | | | | |
| Behavioral health | | | | |
| Pharmacy | | | | |
| DME | | | | |
| Future care (if supported) | | | | |
| **Total** | | | | |

## Section 9 — Reasonableness Review

Per the methodology in `REASONABLENESS-METHODOLOGY.md`. One row per major service:

| Service | CPT/HCPCS | Billed | Paid | MPFS Reference (locality, CY) | FAIR Health 50th / 80th / 90th (geozip) | Notes |
|---|---|---|---|---|---|---|

If no benchmark was retrieved: "Benchmark not obtained — recommend billing-expert review." Do not estimate.

LOP-billed rows must be tagged in the Notes column: `LOP — see RF-12`.

## Section 10 — Causation Analysis

Two subsections:

### 10.1 Treating Physician Statements

Block-quote each contemporaneous causation statement, with citation. Tag each `[O]`. Do not paraphrase or summarize causation language.

### 10.2 IME / Peer-Review Statements

Same format, separately listed. Highlight any direct contradiction with a treater.

### 10.3 Pre-Incident Considerations

Identify same-body-part prior care from records. Tag `[F]`. State whether the chart distinguishes aggravation from new injury, and quote where it does. Where it does not, mark `[A: distinction not addressed in record]` and surface as RF-26.

## Section 11 — Red Flags Table

Use IDs from `RED-FLAGS-CATALOG.md`. One row per finding:

| ID | Name | Detail | Source | Suggested Attorney Action | Severity |
|---|---|---|---|---|---|

Sorted by Severity (H → M → L), then by ID. If no flags: "No flags identified within scope of records reviewed; see Open Items for missing records."

## Section 12 — Collateral-Source & Lien Interfaces

Identification only — does NOT resolve.

| Lienholder / Source | Type | Amount Asserted (if known) | Notice Status | Hand-off |
|---|---|---|---|---|

Hand-off column: `→ lien-resolution-summary` for any item to be worked.

## Section 13 — Expert Needs

Recommendations for retained experts:

- Billing expert (CPC/CCS/CPMA): Y/N — reasoning.
- Medical specialist (specify field): Y/N — reasoning.
- Life care planner: Y/N — reasoning.
- Vocational expert: Y/N — reasoning.
- Other: specify.

## Section 14 — Jurisdictional Flags

Carry forward every `[VERIFY]` item from SKILL.md's Jurisdictional Flags section that bears on this case. Counsel resolves; do not opine.

| Flag | Question for Counsel | Effect on Analysis |
|---|---|---|

## Section 15 — Attorney Review Required

Fixed boilerplate (do not paraphrase):

> This analysis is attorney work product requiring review and is not a final opinion on liability, damages, or causation in law. All figures derive from the documentation listed in Section 2 and the assumptions stated in Section 3. Jurisdictional rules flagged `[VERIFY]` must be confirmed by counsel before reliance. The skill that produced this draft does not constitute billing-expert testimony, medical-expert testimony, or legal advice.

---

## Pre-Delivery Checks (run before sending)

- [ ] Privilege header present.
- [ ] Every section populated or marked "None / Not obtained" with reason.
- [ ] Every row in Sections 7, 9, 11 has a Source citation.
- [ ] Every figure in Section 7 reconciles per provider in the reconciliation row.
- [ ] Every assumption used in Sections 9–10 appears in Section 3.
- [ ] Every Red Flag ID exists in `RED-FLAGS-CATALOG.md` (or is marked `[NEW PATTERN]`).
- [ ] Every lien holder in Section 12 is also reflected in Section 7's Patient Resp./Outstanding columns where applicable.
- [ ] All `[VERIFY]` items from SKILL.md's jurisdictional list are surfaced in Section 14.
- [ ] Section 15 boilerplate present, verbatim.
