---
name: gst-notice-interpreter
title: GST Notice Interpreter — Master Skill
description: Master orchestrator skill for the GST Notice Responder. Load this skill first for ANY GST notice. It reads the notice, identifies the type, loads the relevant section/rule skills, and directs the agent to draft a reply strategy.
author: roneya
author_url: https://github.com/roneya/Gst-Agent/tree/main/.claude/skills/gst-notice-interpreter
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: in
practice: tax
language: en
---

# GST Notice Interpreter — Master Skill

**Built by Rohan Vidhate**
Project: GST Notice Responder — Claude Plugin

---

## What This Skill Does

This is the **entry point** for every GST notice query. When a user pastes or uploads a GST notice, this skill:

1. **Identifies** the notice type (ASMT-10, DRC-01 SCN, audit, etc.)
2. **Extracts** key metadata (GSTIN, period, section cited, demand amount)
3. **Routes** to the correct section/rule skill files
4. **Directs** the reply strategy

---

## Step 1 — Extract These Fields from Every Notice

When a notice is shared, always extract:

| Field | Where to look |
|---|---|
| **Notice type / form** | Header of notice (ASMT-10, DRC-01, etc.) |
| **Section cited** | "Under Section ___" |
| **GSTIN** | Top of notice |
| **State code** | First 2 digits of GSTIN (e.g., GSTIN 27AABC... → state code 27) |
| **Tax period** | "For the period ___ to ___" |
| **Financial year** | Derive from tax period |
| **Demand amount** | Quantified in notice or DRC-01 summary |
| **Due date for reply** | "Within ___ days" |
| **Issuing officer** | Name, designation, jurisdiction |
| **DIN** | 20-digit number on notice |
| **Allegations** | List each discrepancy / allegation separately |

After extracting the GSTIN, immediately run **Step 1B** below before proceeding.

---

## Step 1B — State Code Detection and Overlay Loading

Extract the first 2 digits of the GSTIN. Match to the state code table and load the appropriate overlay:

| State code | State / UT | Action |
|---|---|---|
| **27** | **Maharashtra** | ✅ Default — Step 3F (Maharashtra Legal Audit) runs automatically for every notice |
| **29** | **Karnataka** | Load `legal-archive/karnataka-sgst-overlay.md` — state-specific AAR, trade circulars, e-way bill, and sector rules apply |
| 01 | Jammu & Kashmir | ⚠ No state overlay — apply CGST Act defaults; flag to user |
| 02 | Himachal Pradesh | ⚠ No state overlay |
| 03 | Punjab | ⚠ No state overlay |
| 04 | Chandigarh (UT) | ⚠ No state overlay |
| 05 | Uttarakhand | ⚠ No state overlay |
| 06 | Haryana | ⚠ No state overlay |
| 07 | Delhi | ⚠ No state overlay |
| 08 | Rajasthan | ⚠ No state overlay |
| 09 | Uttar Pradesh | ⚠ No state overlay |
| 10 | Bihar | ⚠ No state overlay |
| 18 | Assam | ⚠ No state overlay |
| 19 | West Bengal | ⚠ No state overlay |
| 21 | Odisha | ⚠ No state overlay |
| 23 | Madhya Pradesh | ⚠ No state overlay |
| **24** | **Gujarat** | Load `legal-archive/gujarat-sgst-overlay.md` — state-specific GHC rulings, trade circulars, and aggressive E-way bill enforcement apply |
| 30 | Goa | ⚠ No state overlay |
| 32 | Kerala | ⚠ No state overlay |
| 33 | Tamil Nadu | ⚠ No state overlay |
| 36 | Telangana | ⚠ No state overlay |
| 37 | Andhra Pradesh | ⚠ No state overlay |

**When state code is NOT 27 or 29:**
> ⚠ **State overlay not available for [State Name] (code [XX]).** This analysis applies the CGST Act and central rules. State-specific SGST rules, trade circulars, and local AAR rulings for [State Name] are NOT covered — the user should separately verify any state-specific obligations or deviations before filing.
> Skip Step 3F (Maharashtra Legal Audit).

**When state code is 27:** Run Step 3F as normal.

**When state code is 29 (Karnataka):** Load `legal-archive/karnataka-sgst-overlay.md`. Skip Step 3F (Maharashtra-specific). Apply Karnataka-specific DIN prefix, AAR, and trade circular notes from the overlay.

**GSTIN from a Central Registration (97xx / 99xx):** These are non-PAN entities (e.g., government bodies). Apply CGST rules only; no state overlay needed.

---

## Step 2 — Identify Notice Type and Load Skill

| If the notice says… | Notice type | Load skill |
|---|---|---|
| ASMT-10 / Section 61 | Scrutiny of returns | `section-61.md` + `rule-99.md` |
| ASMT-13 / best judgement | Best judgement assessment | `asmt-13-bja.md` + `section-62.md` |
| ADT-01 / Section 65 | GST audit notice | `adt-01-audit.md` + `section-65.md` |
| DRC-01A / pre-SCN intimation (FY 2023-24 or earlier) | Pre-SCN intimation — §73/§74 track | `drc-01a-intimation.md` + `section-73.md` |
| DRC-01A / pre-SCN intimation (FY 2024-25 onwards) | Pre-SCN intimation — §74A unified track | `drc-01a-intimation.md` + `section-74a.md` |
| DRC-01 + Section 73 | Non-fraud SCN (up to FY 2023-24) | `section-73.md` + `rule-142.md` |
| DRC-01 + Section 74 | Fraud SCN (up to FY 2023-24) — **run §74→§73 reclassification check in Step 3B automatically** | `section-74.md` + `rule-142.md` + if RECLASSIFICATION_RECOMMENDED: `gst-common-defences/section74-to-73-reclassification.md` |
| DRC-01 + Section 74A | Unified SCN (FY 2024-25 onwards) | `section-74a.md` + `rule-142.md` |
| DRC-01 using §73/§74 for FY 2024-25+ demand | Wrong section — §74A must apply | `section-74a.md` + `drc-06-reply.md` (ground: jurisdictional error) |
| DRC-01 covering **multiple FYs spanning FY 2023-24 → FY 2024-25** | Multi-section demand — **mandatory FY segregation** (see Mixed FY Procedure) — file single DRC-06 in two parts: Part A (§73/§74) + Part B (§74A) | `section-73.md` + `section-74a.md` + `rule-142.md` + `drc-06-reply.md` |
| DRC-07 / adjudication order | Final order — accept or appeal | `drc-07-order.md` + `section-107.md` |
| ITC mismatch allegation | ITC eligibility dispute | `section-16.md` + `section-17.md` |
| Motor vehicle / food / CSR | Blocked credits | `section-17.md` + `blocked-credit-section-17.md` |
| Merger / demerger / amalgamation / sale of business ITC transfer dispute — ITC-02 not filed, proportionality disputed, going concern vs asset sale, §17(5) blocked credits transferred | §18(3) ITC transfer on business restructuring | `cgst-act-reference/section-18.md` + `section-17.md` |
| New registration ITC claim / composition-to-regular switch ITC-01 dispute / ITC reversal demand on becoming exempt or opting composition scheme | §18(1)/(2)/(4) registration change ITC | `cgst-act-reference/section-18.md` + `section-16.md` |
| Job work goods not returned within time limit / §143 time limit breach / ITC-04 non-filing / deemed supply on challan date / sequential job work / goods lost or destroyed at job worker / §19(5) re-availment dispute | §19 job work ITC — non-return deemed supply | `cgst-act-reference/section-19.md` + `cgst-act-reference/section-73.md` |
| Fake ITC / bogus supplier | Fraud ITC allegation | `section-74.md` + `fake-itc-section74.md` + `rule-86a.md` |
| Rule 86A / ITC blocking | ITC ledger blocked | `rule-86a.md` + `section-83.md` |
| Interest demand | Interest computation | `section-50.md` + `interest-calculator.md` |
| ASMT-10 + ITC | Scrutiny + ITC | `section-61.md` + `section-16.md` |
| GSTR-3A / non-filer notice | Non-filing notice | `gstr-3a-non-filer.md` + `gst-thresholds/SKILL.md` |
| Late fee demand / §47 late fee order / §128 waiver / amnesty scheme eligibility / NIL return rate dispute | Late fee — §47 computation and waiver strategy | `cgst-act-reference/section-47.md` + `gst-notice-types/gstr-3a-non-filer.md` |
| REG-03 / registration query | Registration query | `reg-03-reg-17.md` + `reg-04-reply.md` |
| REG-17 / registration cancellation | Cancellation SCN | `reg-03-reg-17.md` + `reg-18-reply.md` |
| REG-31 / GSTIN suspended | Suspension of registration | `reg-31-suspension.md` |
| REG-19 / cancellation order received | Cancellation order — revocation or appeal | `gst-notice-types/reg-19-cancellation-order.md` + `reg-21-revocation.md` + `section-107.md` |
| RFD-06 / refund rejected | Refund rejection order | `rfd-06-rejection.md` + `section-107.md` |
| Section 70 / summons | Summons to appear | `section-70.md` + `summons-section-70.md` |
| Section 83 / bank attachment | Provisional attachment | `section-83.md` + `provisional-attachment-section-83.md` |
| MOV-01 / MOV-02 / MOV-03 / goods intercepted / goods detained | Goods in transit — inspection and detention stage | `gst-notice-types/mov-01-03-detention.md` |
| MOV-09 / goods in transit | Goods seized / penalty order issued | `mov-09-goods-transit.md` + `gst-notice-types/mov-01-03-detention.md` (if pre-seizure context needed) |
| ENQ-01 / unregistered enquiry | Enquiry to unregistered person | `enq-01-enquiry.md` + `section-70.md` |
| Turnover mismatch allegation | GSTR-1 vs GSTR-3B dispute | `gstr1-gstr3b-mismatch.md` + `section-73.md` |
| GSTR-9 vs GSTR-3B mismatch | Annual return mismatch | `gstr9-gstr3b-mismatch.md` |
| Place of supply dispute | IGST vs CGST/SGST wrong head | `place-of-supply-dispute.md` |
| Export of services POS disputed / Indian liaison office alleged as recipient / five conditions challenged / OIDAR Indian consumer / §77 CGST wrong-head refund / §19 IGST wrong-head refund | Export place-of-supply dispute — export status and wrong-head remedy | `gst-common-defences/export-pos-dispute.md` + `gst-common-defences/place-of-supply-dispute.md` |
| Valuation / MRP / related party | Valuation dispute | `valuation-dispute.md` + `section-73.md` |
| RCM not paid | Reverse charge default | `rcm-non-payment.md` + `section-73.md` |
| Export refund / LUT | Zero-rated supply refund | `section-54.md` + `export-refund-lut.md` + `rfd-01-refund-application.md` |
| Inverted duty refund | IDS refund | `section-54.md` + `inverted-duty-refund.md` + `rfd-01-refund-application.md` |
| Refund application procedure / RFD-01 filing / unjust enrichment / refund category eligibility / document checklist for refund | Refund procedure — RFD-01 under §54 | `cgst-rules-reference/rule-89.md` + `cgst-act-reference/section-54.md` |
| GSTAT / HC appeal / stay | Litigation strategy | `gstat-hc-appeal-strategy.md` + `gstat-appeal-strategy.md` + `section-107.md` + `section-112.md` |
| Filing GSTAT second appeal / APL-05 template needed / pre-deposit for GSTAT | APL-05 second appeal — filing template and pre-deposit | `gst-reply-templates/apl-05-gstat.md` + `gst-litigation/gstat-hc-appeal-strategy.md` |
| §66 special audit direction / ASMT-15 | Special audit by CA/CMA | `cgst-act-reference/section-66.md` + `gst-notice-types/section-66-special-audit.md` |
| §67 / inspection / search / seizure | Inspection and search — officer powers | `cgst-act-reference/section-67.md` |
| §68 / e-way bill enforcement / goods in movement | E-way bill interception — goods in movement | `cgst-act-reference/section-68.md` + `gst-notice-types/mov-01-03-detention.md` |
| MOV-07 / MOV-08 / confiscation notice / confiscation order | Confiscation of goods or conveyance | `cgst-act-reference/section-130.md` + `cgst-act-reference/section-129.md` + `cgst-act-reference/section-107.md` |
| DRC-01B / ITC mismatch intimation (Rule 88D) | ITC mismatch — GSTR-2B auto-intimation | `gst-notice-types/drc-01b-itc-mismatch.md` + `gst-common-defences/itc-mismatch.md` + `cgst-rules-reference/rule-36-4.md` |
| DRC-01C / liability mismatch intimation (Rule 88C) | Outward liability mismatch — GSTR-1/IFF vs GSTR-3B | `gst-notice-types/drc-01c-liability-mismatch.md` + `gst-common-defences/gstr1-gstr3b-mismatch.md` |
| DRC-01 SCN — mixed §73 + §74 grounds | Multi-ground SCN — dual fraud/non-fraud allegations | `gst-notice-types/drc-01-multi-ground.md` + `gst-common-defences/section73-74-74a-comparison.md` + `gst-common-defences/section74-to-73-reclassification.md` |
| ASMT-14 / audit findings memo | GST audit findings — accept or contest | `gst-notice-types/asmt-14-audit-memo.md` + `cgst-act-reference/section-65.md` + `gst-reply-templates/drc-03-voluntary-payment.md` |
| GSTR-10 / final return notice | Post-cancellation final return compliance | `gst-notice-types/gstr-10-final-return.md` |
| CMP-05 / composition violation notice | Composition scheme breach — threshold / ECO bar | `gst-notice-types/cmp-05-composition-violation.md` |
| §51 TDS deductor / GSTR-7 non-filing / TDS mismatch | TDS deductor compliance notice | `gst-notice-types/tds-gstr7-mismatch.md` |
| §76 / tax collected from customers but not deposited | Tax collected not deposited — strict liability | `cgst-act-reference/section-76.md` + `gst-notice-types/drc-01-scn.md` |
| §79 / recovery notice / bank garnishment / third-party notice | Recovery of tax post-DRC-07 order | `cgst-act-reference/section-79.md` + `gst-notice-types/drc-07-order.md` |
| §92 / director personal liability notice | Director personal liability for company GST dues | `cgst-act-reference/section-92.md` + `gst-notice-types/drc-01-scn.md` |
| Time of supply dispute / wrong period / late invoice / RCM 60-day rule / advance payment | Time of supply — §12 goods / §13 services | `cgst-act-reference/section-12-13.md` + `cgst-act-reference/section-50.md` |
| Tax invoice defect / invoice timing dispute / receipt voucher not issued / self-invoice missing for RCM / wrong document type (tax invoice vs bill of supply) | Tax invoice compliance — §31 obligations | `cgst-act-reference/section-31.md` + `cgst-act-reference/section-73.md` |
| Export refund IGST route / shipping bill refund stalled / GSTR-1 vs shipping bill mismatch / refund withheld / EGM not filed | IGST export refund — shipping bill as deemed RFD-01 | `cgst-rules-reference/rule-96.md` + `cgst-act-reference/section-54.md` + `gst-reply-templates/rfd-01-refund-application.md` |
| Rule 42/43 / ITC reversal demand / §17(2) audit — mixed-use inputs or capital goods | ITC reversal for mixed-use inputs or capital goods | `cgst-rules-reference/rule-42-43.md` + `gst-common-defences/blocked-credit-section-17.md` |
| §16(4) ITC time-bar / §16(5) relief | ITC time-bar dispute — FY deadline | `gst-common-defences/section-16-4-itc-time-bar.md` + `cgst-act-reference/section-16.md` |
| SCN time-bar argument / Covid limitation extension / SC suo motu SMWP(C) 3/2020 / FY 2019-20 or FY 2020-21 SCN deadline recalculation | Covid-19 SC limitation extension applied to GST §73/§74 SCN deadlines | `gst-common-defences/covid-limitation-extension.md` + `gst-calculators/limitation-checker.md` + `cgst-act-reference/section-73.md` |
| §9(3) RCM rate / service schedule lookup | Reverse charge rate — GTA / legal / security | `cgst-act-reference/section-9-3-rcm-schedule.md` + `gst-common-defences/rcm-non-payment.md` |
| §7 / Schedule I / Schedule II / Schedule III / scope of supply dispute | Scope of supply — deemed supply / goods vs services / exclusions | `cgst-act-reference/section-7-schedule-2.md` |
| §52 / ECO TCS dispute / e-commerce operator TCS | ECO TCS obligations and supplier credit | `cgst-act-reference/section-52.md` + `industries/e-commerce-ondc.md` |
| Corporate guarantee / Rule 28(2) / holding-subsidiary guarantee | Corporate guarantee GST demand | `gst-common-defences/corporate-guarantee.md` + `cgst-act-reference/section-15.md` |
| Wrong-head tax refund / IGST paid instead of CGST+SGST | Wrong-head refund — §77 | `gst-refunds/section-77-wrong-head.md` + `gst-common-defences/place-of-supply-dispute.md` |
| DRC-07 order received — preparing APL-01 first appeal | Pre-APL-01 action — pre-deposit, stay, documents, §79 defence | `gst-common-defences/pre-litigation-checklist.md` + `gst-reply-templates/apl-01-appeal.md` + `cgst-act-reference/section-79.md` |
| Advance ruling query / ARA-01 application | Advance ruling — AAR / AAAR | `gst-litigation/advance-ruling-ara-01.md` |
| ISD non-compliance / mandatory ISD SCN / HO not registered as ISD / GSTR-6 not filed / ISD distribution formula error / blocked credit distributed / wrong tax head in ISD invoice (post Apr-2025) | ISD — §20 mandatory distribution from April 2025 | `cgst-act-reference/section-20-isd.md` + `gst-notice-types/drc-01-scn.md` |
| HSN code mismatch / rate mismatch / wrong HSN chapter / composite supply misclassified / exemption notification conditions disputed | HSN classification / rate dispute — DRC-01 SCN | `gst-notice-types/hsn-classification-notice.md` + `gst-common-defences/section74-to-73-reclassification.md` |
| GSTR-2B ITC not reflecting / IMS action required / Accept-Reject-Pending reconciliation / supplier not filed / §16(4) time-bar on ITC | Monthly IMS/GSTR-2B reconciliation | `gst-internal-audit/gstr-2b-recon-guide.md` + `cgst-rules-reference/rule-36-4.md` + `gst-common-defences/section-16-4-itc-time-bar.md` |

---

## Step 3 — Run the Notice Checklist

For every notice, check these before drafting the reply:

### A. Jurisdiction check
- Is the officer from the correct ward/circle for this GSTIN?
- Is the GSTIN in the notice correct?

### B. DIN check
- Is there a 20-digit DIN on the notice?
- **MANDATORY TOOL CALL**: Call `validate_din` with the DIN, state code, and notice date.
- If tool returns `is_valid: false` → notice is invalid per CBIC Circular 128/47/2019; use the tool's `error_reason` as the ground.

### C. Limitation & Bundling Check
- **MANDATORY TOOL CALL**: Call `calculate_limitation_date` with the Financial Year and Section.
- Compare the tool's `scn_deadline` to the notice issue date.
- If notice date > `scn_deadline` → **PRIORITY GROUND: Time-Barred**.
- **Bunched SCN Detection (v3.0 Intelligence)**: 
    - Does the notice cover multiple FYs spanning both pre- and post-FY 2024-25?
    - If YES → **PRIORITY GROUND: Jurisdictional Overreach**. 
    - *Ground:* "The SCN is bunched across the §74A transition boundary. Demands for FY 2024-25 onwards cannot be bunched with earlier years as the statutory limitation and penalty structures differ fundamentally. This constitutes a jurisdictional overreach per Bombay HC trends."

### D. Reply deadline check
- When was the notice served?
- How many days remain for reply?
- If less than 7 days → immediately flag urgency to user

### E. Fraud allegation check
- Does the notice use words like: fraud, willful misstatement, suppression, deliberately, intentionally, evade?
- If yes AND demand is FY 2023-24 or earlier → §74 fraud track (minimum 100% penalty)
- If yes AND demand is FY 2024-25 onwards → §74A unified track — penalty differs by fraud/non-fraud track:
  - **Non-fraud track** (no fraud/suppression language in SCN):
    - Pre-SCN voluntary payment: NIL penalty → SCN not served
    - Within 60 days of SCN: NIL penalty → proceedings close (extended from 30 days under §73)
    - After adjudication order: 10% of tax (or ₹10,000, whichever higher)
  - **Fraud track** (SCN uses fraud / suppression / willful misstatement language):
    - Pre-SCN voluntary payment: 15% penalty
    - Within 60 days of SCN: 25% penalty → proceedings close
    - Within 60 days of order: 50% penalty → proceedings close (50% is the ceiling — no higher surcharge)
  - For full penalty table and settlement decision tree → load `section-74a.md`
- If no → §73 or §74A non-fraud track applies (NIL penalty within 60-day SCN window for §74A; 10% at order stage)

### F. Maharashtra Legal Audit (run for every Maharashtra GSTIN — state code 27)

Open a `<maharashtra_legal_audit>` block internally before drafting any reply strategy. Work through each point:

```xml
<maharashtra_legal_audit>

  <bombay_hc_check>
    **BOMBAY HC FIRST RULE**: Is there a Bombay HC ruling directly on the allegation?
    - If YES → cite it as the **PRIMARY BINDING AUTHORITY**.
    - If it conflicts with another HC (e.g., Delhi/Karnataka) → explicitly state: "Bombay HC ruling is binding on Maharashtra officers; other HC rulings are persuasive only."
    - If NO → cite the next-strongest HC (Karnataka → Gujarat → Madras → Allahabad).
  </bombay_hc_check>

  <trade_circular_check>
    Does any Maharashtra Trade Circular (issued by the Maharashtra GST Commissioner
    under §168 SGST Act) address the allegation?
    Key circulars to check:
    - Circular 7T/2023 — ITC mismatch procedure (GSTR-2A/2B vs GSTR-3B) — applies to FY 2017-18 and 2018-19 only; aligns with CBIC Circular 183/15/2022-GST
    - Circular 5T/2022 — Scrutiny of returns procedure (ASMT-10) — guidelines for FY 2017-18 and 2018-19; B2B/B2C misreporting; CA certificate for ITC differences > ₹2.5 lakh
    - Circular 11T/2023 — GSTR-3B Table 4 — ITC reversal and ineligible ITC reporting; uniform reporting across taxpayers per 47th GST Council recommendations
    - Circular 3T/2021 — Maharashtra Settlement of Arrears of Tax, Interest, Penalty or Late Fee (legacy pre-GST and early GST arrears)
    If a relevant Trade Circular exists → cite it alongside the CBIC circular.
    State officers follow Maharashtra Trade Circulars more strictly than CBIC circulars.
  </trade_circular_check>

  <amnesty_check>
    Is the demand for a period before FY 2020-21?
    If YES → check whether an active Maharashtra Settlement of Arrears / Amnesty Scheme
    covers this demand type. Amnesty typically offers:
    - Full waiver of interest and penalty
    - Payment of tax only (sometimes at reduced rate)
    Compare amnesty outflow vs. litigation cost before recommending "contest."
    Flag: "Maharashtra Amnesty may apply — verify current scheme before filing DRC-06."
  </amnesty_check>

  <commissionerate_check>
    Is the notice from MahaGST (State GST — GSTIN prefix 27, state officer) or
    CGST (Central commissionerate — Mumbai-I, Mumbai-II, Pune, Thane, Navi Mumbai)?
    This determines:
    - Correct reply recipient (State Tax Officer vs Central Superintendent)
    - Correct appellate forum (Commissioner Appeals SGST vs Commissioner Appeals CGST)
    - Whether Maharashtra Trade Circulars bind the officer (MahaGST yes; CGST no)
  </commissionerate_check>

</maharashtra_legal_audit>
```

Output a one-paragraph **Maharashtra Legal Audit Summary** as the first item in the reply strategy.

---

## Step 3B — MANDATORY PROCEDURAL AUDIT (Run Before Any Merit Analysis)

> **This block is non-negotiable.** Before computing any tax, interest, or penalty amount, or loading any defence playbook, run this audit in full. A single procedural kill can make the entire merits analysis unnecessary.

Open a `<procedural_audit>` block internally and complete all three checks:

```xml
<procedural_audit>

  <din_validity>
    PURPOSE: A notice without a valid DIN is void ab initio (CBIC Circular 128/47/2019).
    **MANDATORY TOOL CALL**: Call `validate_din` with extracted DIN, state code, and notice date.
    Output: Use the JSON result from the tool.
    If tool returns `is_valid: false` → "Notice invalid. [Tool's error_reason]. Raise as FIRST ground in reply."
    Output: DIN_STATUS = VALID | INVALID | ABSENT
  </din_validity>

  <section_74a_threshold>
    PURPOSE: §74A(1) proviso bars issuing a notice if the aggregate demand for the FY is below ₹1,000.
    Applicable ONLY for §74A demands (FY 2024-25+). For §73/§74 demands → mark N/A and skip.
    Checks to run:
    1. Is this a §74A demand (FY 2024-25 onwards)? If NO → THRESHOLD_STATUS = N/A; skip this check.
    2. What is the aggregate demand for the financial year? (Sum all grounds and all tax heads)
    3. If total < ₹1,000 → notice is void ab initio.
       Ground: "The aggregate demand for FY [___] is ₹[___], which is below the ₹1,000 statutory
       minimum under §74A(1) proviso. No notice can be issued below this threshold. The notice is
       void and must be dropped."
    4. If total ≥ ₹1,000 → threshold satisfied; proceed.
    Output: THRESHOLD_STATUS = VOID (< ₹1,000) | VALID (≥ ₹1,000) | N/A (§73/§74 demand)
    If VOID → flag as PRIORITY GROUND — RAISE FIRST IN REPLY, before all other grounds.
  </section_74a_threshold>

  <section_reclassification>
    PURPOSE: §74 demands a 100% penalty; §73 demands only 10%. Reclassifying saves the client
    the full penalty amount. Officers frequently invoke §74 lazily without establishing fraud.
    Run this test:
    1. Does the notice contain the words: fraud, willful misstatement, suppression, deliberately,
       intentionally, evade, collusion? → Count occurrences.
    2. If fraud words are present but NO specific facts are pleaded to support fraud (e.g., officer
       just copies the statutory language without case-specific reasoning) → §74 is unsustainable.
       Authority: Devi Enterprises v. CGST (Delhi HC), K.P. Sugandha Ltd. v. State (Allahabad HC).
    3. If demand is for mismatch, short payment, ITC reversal, or non-payment WITHOUT any allegation
       of intent → §73 must be applied, not §74.
    §74A-SPECIFIC NOTE: If demand is for FY 2024-25 onwards and officer cited §74A:
    - §74→§73 reclassification does NOT apply (§74A is a unified provision with no fraud/non-fraud split)
    - Instead check: Did officer wrongly apply §73/§74 for a FY 2024-25+ demand? That is a jurisdictional error
    - For mixed FY demands: each FY must be separately assessed under the correct section
    Output: SECTION_APPLIED = §73 | §74 | §74A | WRONG_SECTION_FOR_FY | RECLASSIFICATION_RECOMMENDED
    If RECLASSIFICATION_RECOMMENDED →
      1. Load `gst-common-defences/section74-to-73-reclassification.md` immediately for the full playbook.
      2. Insert as a PRIORITY standalone ground (before merit analysis): "The invocation of §74 is
         without jurisdiction. The facts disclose, at best, a §73 demand. Penalty must be capped at 10%."
      3. In Step 4 output, add a RECLASSIFICATION ALERT block:
         "⚠️ RECLASSIFICATION ALERT: §74 invoked without sufficient fraud pleading.
          Reclassification to §73 saves 90% of penalty (100% → 10%). Load section74-to-73-reclassification.md."
  </section_reclassification>

  <speaking_order_check>
    PURPOSE: A non-speaking order (template notice with no case-specific reasoning) can be
    challenged before the High Court on grounds of violation of natural justice / Article 14.
    Checks to run:
    1. Does the notice/order cite specific facts about THIS taxpayer (dates, invoice numbers,
       amounts, supplier names)? If NO → it is a template/non-speaking order.
    2. Does the notice explain WHY those specific facts constitute a violation? If NO → no application
       of mind; order is vulnerable.
    3. Was an opportunity of personal hearing offered before the order? If NO → natural justice
       violated (§75(4) CGST Act mandates hearing before adverse order if requested).
    4. Is this an assessment order (not just an SCN)? If it is a final order without addressing the
       taxpayer's reply → it is void for non-consideration of evidence.
    Output: ORDER_TYPE = SPEAKING | NON_SPEAKING | UNKNOWN
    If NON_SPEAKING → add ground: "The notice/order is a non-speaking order. No application of mind
    is evident from the facts. The order is liable to be quashed on principles of natural justice."
    Bombay HC authority: Bansal Buildwell v. UoI; Vodafone Idea Ltd. v. DGGI.
  </speaking_order_check>

  <officer_persona_check>
    PURPOSE: Different issuing authorities have different litigation "styles." Identifying the
    persona helps tailor the tone and defensive depth of the reply.
    Checks to run:
    1. **DGGI / Anti-Evasion / Intelligence:** High-conflict. Persona = "Enforcer."
       - Focus: Retraction of statements, Article 20(3) (self-incrimination), coercion.
       - Requirement: Load `gst-litigation/gstat-hc-appeal-strategy.md` immediately.
    2. **Audit Commissionerate (ADT-01):** Investigative. Persona = "Examiner."
       - Focus: Documentation trail, reconciliation, circular compliance.
       - Requirement: Use the `evidentiary-weight-matrix.md` for ALL document lists.
    3. **Ward Officer / Jurisdictional STO:** Compliance-driven. Persona = "Administrator."
       - Focus: Technical glitches, bona fide errors, time-bar, §73 vs §74.
       - Requirement: Prioritize "Pay and Close" or "Standard technicality" arguments.
    Output: OFFICER_PERSONA = ENFORCER | EXAMINER | ADMINISTRATOR
  </officer_persona_check>

  </procedural_audit>

  ```

  Output a **Procedural Audit Summary** with one line per check and a clear verdict before proceeding to Step 4. If any check returns a kill ground, highlight it in bold as **PRIORITY GROUND — RAISE FIRST IN REPLY**.

  ---

## Step 3C — §74A SCN Handler (Run Only When §74A Demand Identified)

> **Trigger:** Skip this section entirely if demand is for FY 2023-24 or earlier (§73/§74 track). Run in full for any FY 2024-25+ demand.

### Four Critical §74A Differences from §73/§74

**1. Fraud/non-fraud determines penalty, not the notice form**
Under §74A the officer uses the same DRC-01 regardless of whether fraud is alleged. The distinction matters only for penalty. If the SCN is ambiguous about which track applies, challenge it immediately:
- Ground: "The SCN does not specify whether the fraud or non-fraud penalty track applies. The taxpayer is entitled to know the applicable penalty track before filing a meaningful reply under §75(4)."

**2. Burden of proof for fraud track**
To invoke the fraud penalty track under §74A, the officer must positively establish deliberate concealment, wilful misstatement, or suppression of facts with intent to evade. Generic fraud boilerplate without case-specific facts is unsustainable under §74A — apply the same challenge strategy as §74 reclassification (see `section74-to-73-reclassification.md`). Reclassifying to non-fraud track drops the penalty from 50% to 10% at order stage.
[ASK USER: supply §74A Explanation 2 statutory text on suppression definition + any Bombay HC ruling specifically on §74A burden of proof for fraud track]

**3. 60-day payment window — use the full window strategically**
Under §74A(8)(ii), non-fraud taxpayers pay tax + interest with ZERO penalty if paid within 60 days of the SCN (vs 30 days under §73). Advise the client:
- Do NOT rush to pay. Use the full 60 days to gather GSTR-2B reconciliation, supplier payment confirmations, and evaluate contest viability.
- If decision is to pay and close → target Day 55 (5-day buffer for portal processing).
- The 60-day window runs from **SCN service date**, not the issue date — verify registered email/portal service.

**4. Pre-deposit for appeal against §74A order**
When a DRC-07 is issued under §74A and the client wants to file APL-01 under §107:
[ASK USER: confirm the pre-deposit percentage under §107 for a DRC-07 order issued under §74A — is it the same 10% (§73) / 25% (§74) as the old regime, or a new rate specific to §74A?]

---

### Mixed FY Demand — Mandatory Procedure

When a single SCN covers FYs straddling FY 2023-24 and FY 2024-25:

1. **Segregate by FY** — List the demand amount for each FY separately.
2. **Apply the correct section per FY:**
   - FY 2017-18 to FY 2023-24 → §73 or §74 (as cited in SCN)
   - FY 2024-25 onwards → §74A (mandatory regardless of what the SCN cites)
3. **If officer applied §73/§74 to a FY 2024-25+ demand** → jurisdictional error → priority ground:
   "The demand for FY 2024-25 cannot be assessed under §73/§74. §74A is the exclusive provision for FY 2024-25 onwards. The SCN is without jurisdiction for FY 2024-25 demand."
4. **Reply structure:** File a single DRC-06 but structure it in two parts — Part A (FY 2023-24 and earlier, §73/§74 submissions) and Part B (FY 2024-25+, §74A submissions).

---

### §74A DRC-06 Reply Pre-Filing Checklist

- [ ] SCN specifies fraud or non-fraud track? If ambiguous → challenge on natural justice first.
- [ ] ₹1,000 minimum threshold met? If not → raise threshold defect as Ground 1.
- [ ] Is 60-day payment window still open? (Compute from SCN **service** date, not issue date.)
- [ ] Are all FYs correctly assessed under the right section? Flag jurisdictional error for FY 2024-25+ if §73/§74 cited.
- [ ] Bombay HC checked for §74A-specific rulings?

---

---
## Step 3D — Heuristic Risk-Scoring Engine (v3.1 Intelligence)

Before finalizing the strategy, compute a 1–10 Risk Score for the notice:

```xml
<risk_scoring_engine>
  <logic>
    1. BASE_SCORE = 1
    2. QUANTUM: 
       - If Demand < ₹10L → +0
       - If Demand ₹10L - ₹50L → +1
       - If Demand ₹50L - ₹1Cr → +2
       - If Demand > ₹1Cr → +3
    3. FRAUD:
       - If §74 or §74A Fraud Track is invoked → +3
    4. URGENCY:
       - If Reply Deadline < 7 days → +2
    5. PROCEDURAL_MITIGATOR:
       - If DIN is MISSING → -3
       - If Demand is clearly TIME-BARRED → -3
       (Note: Risk score cannot drop below 1)
  </logic>

  <score_interpretation>
    - 1-3: LOW (Routine compliance matter)
    - 4-6: MEDIUM (Financial impact; merit defence needed)
    - 7-8: HIGH (High stakes; fraud allegations or large quantum)
    - 9-10: CRITICAL (Immediate risk of recovery or registration block)
  </score_interpretation>
</risk_scoring_engine>
```

Inject the score into the **Step 5 — Notice Summary** output under the Preliminary Flags.

---

## Step 4 — Produce the Reply Strategy

  After loading the relevant skills, output:

  ```
  NOTICE SUMMARY
  --------------
  Form: [ASMT-10 / DRC-01 / etc.]
  Section: [61 / 73 / 74 / 74A]
  Period: [FY ____]
  GSTIN: [___]
  Demand: ₹[___] tax + ₹[___] interest + ₹[___] penalty
  Reply due: [date] ([X] days remaining)
  DIN: [present / MISSING — notice invalid]

  PRELIMINARY FLAGS
  -----------------
  ☐ Limitation expired? [Yes/No + deadline date]
  ☐ DIN present? [Yes/No]
  ☐ Fraud alleged? [Yes/No]
  ☐ Jurisdiction correct? [Yes/No]

  ALLEGATION BREAKDOWN
  --------------------
  1. [Allegation 1]: [Brief — accept / dispute / partially accept]
  2. [Allegation 2]: [Brief]
  ...

  MAHARASHTRA LEGAL AUDIT
  -----------------------
  Bombay HC authority: [case name if found / "None — use [next HC]"]
  Trade Circular: [Circular number + key point / "None found"]
  Amnesty applicable: [Yes — check current scheme / No — post-2020 demand]
  Commissionerate: [MahaGST (state) / CGST — [commissionerate name]]

  OFFICER PERSONA & TONE
  ----------------------
  Persona identified: [Enforcer / Examiner / Administrator]
  Strategy tone: [Aggressive-Legal / Evidence-Heavy / Compliance-Cooperative]

  EVIDENTIARY WEIGHT STRATEGY
  ---------------------------
  (Rank the documents the user MUST provide for this specific notice)
  1. [High Weight Doc 1] (Weight: 10/10) - [Purpose]
  2. [High Weight Doc 2] (Weight: 9/10) - [Purpose]
  3. [Medium Weight Doc 1] (Weight: 7/10) - [Purpose]

  RECOMMENDED STRATEGY
  --------------------
  [Pay / Contest / Partial pay + contest]
  [Key legal grounds]
  [Skills to load for full defence: section-XX.md, etc.]


REPLY FORM TO USE
-----------------
[ASMT-11 (for §61) / DRC-06 (for §73/74/74A)]
```

---
## Step 4B — Pre-Finalisation Verification Gate

**Before outputting any reply strategy or draft, complete this checklist. Do not skip any item.**

```
VERIFICATION GATE
-----------------
☐ DIN validated via tool?         [Call validate_din — result: valid/invalid]
☐ Limitation checked via tool?    [Call calculate_limitation_date — result: valid/barred]
☐ Interest/Penalty computed?       [Call calculate_interest / calculate_penalty as needed]
☐ Reply deadline?                  [___ days remaining — if <7 days, prepend URGENT FLAG]
☐ Correct section identified?      [§61 / §73 / §74 / §74A / other]
...
☐ Fraud track or non-fraud?        [Non-fraud (10%/NIL penalty) / Fraud (up to 100%/50%)]
☐ Penalty window identified?       [Pre-SCN NIL / 30d §73 / 60d §74A / post-order]
☐ §74A threshold check?            [Demand ≥ ₹1,000 for FY? / N/A (§73/§74 demand)]
☐ Mixed FY demand detected?        [Yes — segregated, correct section per FY / No]
☐ Bombay HC case cited?            [Yes — [case name] / No — cite next strongest HC]
☐ Maharashtra Trade Circular?      [Relevant circular noted / None found]
☐ Amnesty check (pre-FY 2020-21)?  [Applicable — flag for client / Not applicable]
☐ Commissionerate identified?      [MahaGST (state) / CGST — [name]]
☐ All allegations addressed?       [Yes — [count] allegations, all covered / Missing: ___]
☐ Reply template selected?         [ASMT-11 / DRC-06 / APL-01 / other]

If any box is unchecked → complete that step before proceeding.
```

**Bombay HC First Rule:**
When citing case law for a Maharashtra GSTIN (state code 27):
- Bombay HC ruling = cite as **primary binding authority** on Maharashtra officers
- Delhi HC / other HC ruling that conflicts = cite as **persuasive only; Bombay HC binding**
- Explicitly state the conflict: *"Note: Delhi HC held [X] but Bombay HC held [Y] — Bombay HC is binding on Maharashtra officers."*

---

## Step 5 — Extract Structured Notice Summary (Always Output This)

After reading any notice, always produce this block before any strategy or reply:

```
╔══════════════════════════════════════════════════════════════╗
║                    NOTICE SUMMARY                            ║
╠══════════════════════════════════════════════════════════════╣
║ Form          : [ASMT-10 / DRC-01 / REG-17 / MOV-09 / etc.] ║
║ Section       : [61 / 73 / 74 / 74A / 29 / 70 / 83 / etc.]  ║
║ GSTIN         : [15-digit number]                            ║
║ Taxpayer name : [Legal name]                                 ║
║ Period        : [MM/YYYY to MM/YYYY]  FY: [XXXX-XX]         ║
║ Tax demand    : ₹[___] (IGST/CGST/SGST/Cess breakup if any) ║
║ Interest      : ₹[___]                                       ║
║ Penalty       : ₹[___]                                       ║
║ Total demand  : ₹[___]                                       ║
║ DIN           : [20-digit / MISSING]                         ║
║ Issuing officer: [Name, Designation, Jurisdiction]           ║
║ Notice date   : [DD-MM-YYYY]                                 ║
║ Reply deadline: [DD-MM-YYYY] ([X] days remaining)            ║
╠══════════════════════════════════════════════════════════════╣
║                  PRELIMINARY FLAGS                           ║
╠══════════════════════════════════════════════════════════════╣
║ ⚠ Risk Score         : [X]/10 ([LOW/MEDIUM/HIGH/CRITICAL])   ║
║ ⚠ DIN missing?       [YES — notice invalid / NO]            ║
║ ⚠ Limitation expired? [YES ✅ strongest ground / NO / CHECK] ║
║ ⚠ Fraud alleged?     [YES — §74/74A fraud track / NO]       ║
║ ⚠ Jurisdiction OK?   [YES / QUERY — verify ward/circle]     ║
║ ⚠ Hearing given?     [YES / NO — §75(4) right violated]     ║
║ ⚠ Urgency level:     [HIGH (<7 days) / MEDIUM / LOW]        ║
╠══════════════════════════════════════════════════════════════╣
║               ALLEGATION BREAKDOWN                           ║
╠══════════════════════════════════════════════════════════════╣
║ 1. [Allegation 1] — [DISPUTE / ACCEPT / PARTIAL]            ║
║ 2. [Allegation 2] — [DISPUTE / ACCEPT / PARTIAL]            ║
║ ...                                                          ║
╠══════════════════════════════════════════════════════════════╣
║                RECOMMENDED STRATEGY                          ║
╠══════════════════════════════════════════════════════════════╣
║ Action        : [PAY / CONTEST / PAY-PART + CONTEST]        ║
║ Reply form    : [ASMT-11 / DRC-06 / REG-18 / REG-21 / etc.] ║
║ Skills to load: [list skill files]                           ║
╚══════════════════════════════════════════════════════════════╝
```

---

## Golden Pairs — Quality Benchmark

Before finalising any reply, check if a Golden Pair exists for this notice type in `samples/`. If it does, your response should match or exceed its depth, structure, and citation quality.

| Sample | Notice type | Key lesson |
|---|---|---|
| `samples/sample-01-asmt10-itc-mismatch.md` | ASMT-10 §61 | ITC timing lag defence + Maharashtra Trade Circular 7T/2023 |
| `samples/sample-02-drc01-time-barred.md` | DRC-01 §73 | Time-bar as sole ground — do NOT go into merits |
| `samples/sample-03-drc01-section74-fraud-defence.md` | DRC-01 §74 | Fraud reclassification + 24% interest rate challenge |

---

## Related Skills — Full Index

### Statutory provisions
- `cgst-act-reference/section-7-schedule-2.md` — Scope of supply — Schedule I deemed supply, Schedule II goods vs services, Schedule III exclusions
- `cgst-act-reference/section-9-3-rcm-schedule.md` — §9(3) RCM rate schedule — GTA, legal, security, import of services
- `cgst-act-reference/section-12-13.md` — Time of supply — §12 goods, §13 services, RCM 60-day rule, vouchers, rate change
- `cgst-act-reference/section-15.md` — Valuation of supply — transaction value, inclusions, discounts, related-party Rules 27–31
- `cgst-act-reference/section-16.md` — ITC eligibility
- `cgst-act-reference/section-17.md` — Blocked credits
- `cgst-act-reference/section-18.md` — ITC on change of constitution: §18(1) new registration / composition-to-regular ITC-01, §18(3) merger/demerger/sale ITC transfer via ITC-02, §18(4) ITC reversal on exemption/composition switch
- `cgst-act-reference/section-19.md` — ITC on job work: §19(1)/(2) inputs 1-year limit, §19(3)/(4) capital goods 3-year limit, deemed supply on challan date if not returned, §19(5) re-availment after payment
- `cgst-act-reference/section-25.md` — Registration thresholds, mandatory categories (§24), multiple GSTIN per PAN, casual/non-resident taxable person, REG-03/REG-17 backdrop
- `cgst-act-reference/section-20-isd.md` — Input Service Distributor — mandatory ISD from April 2025, GSTR-6, distribution formula, C₁=(t₁/T)×C, §17(5) exclusion before distribution
- `cgst-act-reference/section-31.md` — Tax invoice — when to issue, invoice types (tax invoice/bill of supply/receipt voucher/self-invoice), mandatory fields, timing disputes
- `cgst-act-reference/section-29.md` — Cancellation of registration — voluntary §29(1) vs suo motu §29(2), liability survival
- `cgst-act-reference/section-30.md` — Revocation of cancellation — 90-day window, mandatory grant
- `cgst-act-reference/section-47.md` — Late fees for delayed return filing — §47 GSTR-1/3B/9 rates, NIL-return rate, §128 waiver, amnesty schemes
- `cgst-act-reference/section-50.md` — Interest
- `cgst-act-reference/section-52.md` — ECO TCS — ECO obligations, GSTR-8, supplier credit, §9(5) override
- `cgst-act-reference/section-54.md` — Refunds — 2-year limit, RFD forms, relevant date
- `cgst-act-reference/section-61.md` — Scrutiny of returns
- `cgst-act-reference/section-62.md` — Best judgement assessment
- `cgst-act-reference/section-65.md` — GST audit by officers
- `cgst-act-reference/section-66.md` — Special audit by CA/CMA — Commissioner direction, ASMT-15, taxpayer rights
- `cgst-act-reference/section-67.md` — Inspection, search and seizure — authorisation, panchnama, taxpayer rights
- `cgst-act-reference/section-68.md` — Inspection of goods in movement — e-way bill enforcement, MOV forms sequence
- `cgst-act-reference/section-70.md` — Power to summon
- `cgst-act-reference/section-73.md` — Non-fraud demand (up to FY 2023-24)
- `cgst-act-reference/section-74.md` — Fraud demand (up to FY 2023-24)
- `cgst-act-reference/section-74a.md` — Unified demand (FY 2024-25+)
- `cgst-act-reference/section-75.md` — General provisions — hearing rights, speaking order
- `cgst-act-reference/section-76.md` — Tax collected but not deposited — strict liability, GSTR-1/3B gap demand
- `cgst-act-reference/section-79.md` — Recovery of tax — bank garnishment, third-party notice, distress/sale
- `cgst-act-reference/section-83.md` — Provisional attachment — bank/property
- `cgst-act-reference/section-92.md` — Director personal liability for company GST dues — §92 conditions, non-executive defence
- `cgst-act-reference/section-107.md` — Appeal to Appellate Authority

### Procedural rules
- `cgst-rules-reference/rule-21a.md` — Suspension of registration — grounds, representation, revocation
- `cgst-rules-reference/rule-23.md` — Revocation of cancellation — 90-day window, extensions, REG-21
- `cgst-rules-reference/rule-36-4.md` — ITC restriction to GSTR-2B
- `cgst-rules-reference/rule-86a.md` — ITC blocking — challenge and restoration
- `cgst-rules-reference/rule-42-43.md` — ITC reversal for inputs/services (Rule 42) and capital goods (Rule 43 Tc/Tm/Tr/Te)
- `cgst-rules-reference/rule-89.md` — Refund application procedure under §54 — RFD-01 eligible categories, unjust enrichment, document checklist, RFD-02 through PMT-03 forms sequence
- `cgst-rules-reference/rule-99.md` — ASMT-10/11/12 procedure
- `cgst-rules-reference/rule-142.md` — DRC forms — full demand lifecycle

### Notice types
- `gst-notice-types/adt-01-audit.md` — ADT-01 audit notice
- `gst-notice-types/asmt-10-scrutiny.md` — ASMT-10 scrutiny notice
- `gst-notice-types/asmt-13-bja.md` — ASMT-13 best judgement assessment
- `gst-notice-types/drc-01-scn.md` — DRC-01 Show Cause Notice
- `gst-notice-types/drc-01a-intimation.md` — DRC-01A pre-SCN intimation
- `gst-notice-types/drc-07-order.md` — DRC-07 adjudication order
- `gst-notice-types/enq-01-enquiry.md` — ENQ-01 enquiry to unregistered persons
- `gst-notice-types/gstr-3a-non-filer.md` — GSTR-3A non-filer notice
- `gst-notice-types/mov-09-goods-transit.md` — MOV-09 goods in transit penalty
- `gst-notice-types/provisional-attachment-section-83.md` — §83 bank/property attachment
- `gst-notice-types/rfd-06-rejection.md` — RFD-06 refund rejection
- `gst-notice-types/reg-03-reg-17.md` — REG-03 query + REG-17 cancellation SCN
- `gst-notice-types/asmt-14-audit-memo.md` — ASMT-14 audit findings memo — accept vs contest
- `gst-notice-types/cmp-05-composition-violation.md` — CMP-05 composition violation — threshold breach, ECO bar, demand
- `gst-notice-types/drc-01b-itc-mismatch.md` — DRC-01B ITC mismatch intimation (Rule 88D)
- `gst-notice-types/drc-01c-liability-mismatch.md` — DRC-01C liability mismatch intimation (Rule 88C)
- `gst-notice-types/drc-01-multi-ground.md` — Multi-ground DRC-01 — mixed §73+§74 grounds in one SCN
- `gst-notice-types/gstr-10-final-return.md` — GSTR-10 final return — post-cancellation ITC reversal
- `gst-notice-types/mov-01-03-detention.md` — MOV-01/02/03 goods detention — inspection and detention stage
- `gst-notice-types/reg-19-cancellation-order.md` — REG-19 cancellation order — revocation path, APL-01 appeal
- `gst-notice-types/reg-31-suspension.md` — REG-31 GSTIN suspension
- `gst-notice-types/section-66-special-audit.md` — §66 special audit direction — ASMT-15, CA/CMA handling
- `gst-notice-types/summons-section-70.md` — §70 summons handling
- `gst-notice-types/tds-gstr7-mismatch.md` — §51 TDS deductor notice — GSTR-7 non-filing, short-deduction
- `gst-notice-types/hsn-classification-notice.md` — HSN classification / rate mismatch DRC-01 — classification principles hierarchy, §73 vs §74 track, officer rebuttals, pay vs contest decision tree

### Defence playbooks
- `gst-common-defences/blocked-credit-section-17.md` — §17(5) blocked ITC
- `gst-common-defences/fake-itc-section74.md` — Fake ITC / fraud allegation
- `gst-common-defences/gstr1-gstr3b-mismatch.md` — Turnover mismatch defence
- `gst-common-defences/gstr9-gstr3b-mismatch.md` — Annual return mismatch defence
- `gst-common-defences/itc-mismatch.md` — GSTR-2A/2B mismatch defence
- `gst-common-defences/place-of-supply-dispute.md` — IGST vs CGST/SGST misclassification
- `gst-common-defences/corporate-guarantee.md` — Rule 28(2) corporate guarantee — 1% deemed value, nil-value election
- `gst-common-defences/evidentiary-weight-matrix.md` — Cross-skill evidence strength table — 1–10 scoring for all document types
- `gst-common-defences/pre-litigation-checklist.md` — DRC-07 → APL-01 action checklist — pre-deposit, stay application, §79 defence
- `gst-common-defences/rcm-non-payment.md` — RCM non-payment defence
- `gst-common-defences/section-16-4-itc-time-bar.md` — §16(4) vs §16(5) ITC time-bar — FY-wise deadline table, Scenario A–D matrix
- `gst-common-defences/section73-74-74a-comparison.md` — §73 vs §74 vs §74A demand track comparison — FY applicability, limitation, penalty
- `gst-common-defences/section74-to-73-reclassification.md` — §74→§73 reclassification strategy — penalty saving 100%→10%
- `gst-common-defences/export-pos-dispute.md` — Export POS disputes — five export-of-services conditions, §13 IGST POS, OIDAR issues, Indian branch allegation, §77/§19 wrong-head remedy
- `gst-common-defences/valuation-dispute.md` — §15 valuation dispute

### Reply templates
- `gst-reply-templates/apl-01-appeal.md` — APL-01 appeal template
- `gst-reply-templates/apl-05-gstat.md` — APL-05 GSTAT second appeal template — pre-deposit (20% additional = 30% total), grounds, stay prayer
- `gst-reply-templates/asmt-11-reply.md` — ASMT-11 scrutiny reply
- `gst-reply-templates/asmt-13-reply.md` — ASMT-13 §62(2) withdrawal covering letter
- `gst-reply-templates/asmt-14-reply.md` — ASMT-14 audit findings memo reply
- `gst-reply-templates/drc-01a-reply.md` — DRC-01A pre-SCN intimation written representation
- `gst-reply-templates/drc-03-voluntary-payment.md` — DRC-03 voluntary payment letter
- `gst-reply-templates/drc-06-reply.md` — DRC-06 SCN reply template
- `gst-reply-templates/rfd-01-refund-application.md` — RFD-01 refund application
- `gst-reply-templates/reg-04-reply.md` — REG-04 registration query reply
- `gst-reply-templates/mov-09-reply.md` — MOV-09 reply — pre-payment representation, bond/release letter
- `gst-reply-templates/reg-18-reply.md` — REG-18 cancellation SCN reply
- `gst-reply-templates/reg-21-revocation.md` — REG-21 revocation of cancellation

### Calculators
- `gst-calculators/combined-demand-calculator.md` — Tax + §50 interest + penalty in one output; all 3 sections
- `gst-calculators/gstr-4-composition-return.md` — CMP-08 quarterly + GSTR-4 annual return for composition taxpayers
- `gst-calculators/gstr-9-annual-return.md` — GSTR-9/9C annual return — table-wise guide, common errors
- `gst-calculators/interest-calculator.md` — §50 interest with case law
- `gst-calculators/limitation-checker.md` — Limitation period checker with case law
- `gst-calculators/penalty-calculator.md` — §73/74/74A penalty with case law

### Refund strategy
- `gst-refunds/export-refund-lut.md` — Zero-rated export refund
- `gst-refunds/inverted-duty-refund.md` — Inverted duty structure refund
- `gst-refunds/section-77-wrong-head.md` — §77 wrong-head refund — IGST↔CGST+SGST, RFD-01, interest waiver
- `cgst-rules-reference/rule-96.md` — IGST export refund — shipping bill as deemed RFD-01, auto-credit via Customs, withholding conditions, GSTR-1/shipping bill mismatch

### Industries
- `industries/agriculture.md` — Agriculture and agro-processing — exempt produce, agri-input dealers, cold chain, agri-service RCM
- `industries/automobile-auto-ancillary.md` — Automobile / Auto-Ancillary — §17(5)(a) demo car ITC, EV rates, warranty GST, margin scheme
- `industries/bfsi-financial-services.md` — BFSI — banks/NBFCs/insurance Rule 42 reversal, exempt vs taxable, POS disputes
- `industries/chemical-specialty.md` — Chemical / Specialty Chemicals — HSN Ch.28–29 classification, captive power ITC, R&D credit
- `industries/contract-labour.md` — Contract Labour / Manpower Supply — Schedule III employer-employee exclusion, RCM security, §17(5)(b)
- `industries/e-commerce-ondc.md` — E-commerce / ONDC — §52 TCS mechanics, ECO vs seller obligations, mandatory registration
- `industries/education-sector.md` — Education — approved curriculum exemption, coaching taxability, hostel threshold, EdTech
- `industries/employee-perquisites.md` — Employee Perquisites — canteen §17(5)(b) exception, ESOP exclusion, club membership ITC block
- `industries/food-fmcg.md` — Food Processing / FMCG — branded vs unbranded disputes, coupons/cashbacks §15(3), cold chain ITC
- `industries/gems-jewellery.md` — Gems and Jewellery — Rule 32(5) old gold margin, karigar ITC, SEEPZ export, hallmarking
- `industries/healthcare-ayurveda.md` — AYUSH / Yoga / Naturopathy — AYUSH product HSN, wellness taxability, Panchakarma distinction
- `industries/hospitality-hotels.md` — Hospitality / Hotels — accommodation rates, restaurant GST, banquet ITC, ISD chains
- `industries/it-saas-exports.md` — IT / SaaS exports — zero-rated, LUT, POS disputes, FEMA compliance, OIDAR
- `industries/logistics-gta.md` — GTA — §9(3) RCM vs forward charge, consignment note, ITC disputes
- `industries/manufacturing-midc.md` — Manufacturing / MIDC — job work, MIDC lease, composition exclusion, RCM obligations
- `industries/media-entertainment-ott.md` — Media / Entertainment / OTT — streaming OIDAR, film production, advertising, online gaming
- `industries/mining-minerals.md` — Mining / Minerals — royalty RCM post-MADA, HSN classification, DMF/NMET, overburden removal
- `industries/non-profit-ngo.md` — Non-profit / NGO / Section 8 — donation vs consideration, exempt activities, ITC reversal
- `industries/online-gaming.md` — Online Gaming — 28% on full deposit from Oct-2023, pre-Oct defence, OIDAR, fantasy sports
- `industries/petroleum-oil-gas.md` — Petroleum / Oil and Gas — excluded products outside GST, LPG/lubricants inside, Rule 42 reversal
- `industries/pharma-healthcare.md` — Pharma / Healthcare — hospital exemption, drug valuation, clinical trials, diagnostic labs
- `industries/real-estate-tdr-fsi.md` — Real Estate / JDA / TDR-FSI — JDA RCM, TDR types, §17(5) blocked ITC, MahaRERA
- `industries/solar-renewable.md` — Solar / Renewable Energy — EPC works contract rate, government project 12%, import IGST
- `industries/steel-metals.md` — Steel / Metals — HSN Ch.72/73 classification, scrap ITC, job work §143, captive power ITC
- `industries/textile-apparel.md` — Textile / Apparel — IDS refund, job work §143, HSN classification, Bhiwandi/Ichalkaranji
- `industries/works-contract-construction.md` — Works Contract / Construction — §17(5)(c)/(d) ITC block, plant and machinery exception

### Litigation
- `gst-litigation/advance-ruling-ara-01.md` — ARA-01 advance ruling procedure — AAR vs AAAR, binding effect, Maharashtra AAR
- `gst-litigation/gstat-appeal-strategy.md` — GSTAT APL-05 drafting guidance and pre-deposit logic
- `gst-litigation/gstat-hc-appeal-strategy.md` — GSTAT + HC writ + stay applications

### Internal audit
- `gst-internal-audit/client-onboarding.md` — New client due diligence — 7-phase checklist, 6-dimension risk matrix
- `gst-internal-audit/compliance-calendar.md` — Monthly/quarterly return deadlines, late fees, ITC cutoffs
- `gst-internal-audit/demand-lifecycle-tracker.md` — End-to-end demand timeline — DRC-01A → SCN → DRC-07 → APL-01 → GSTAT
- `gst-internal-audit/gstr-2b-recon-guide.md` — Monthly IMS/GSTR-2B reconciliation — Accept/Reject/Pending actions, mismatch types, §16(4) time-bar check, supplier chase protocol
- `gst-internal-audit/ims-action-matrix.md` — IMS action matrix — Accept / Reject / Pending decisions
- `gst-internal-audit/itc-risk-profiler.md` — Supplier risk scoring — 5-dimension matrix, Green→Black risk bands
- `gst-internal-audit/pre-filing-checker.md` — Pre-GSTR-3B checklist — GSTR-2B recon, blocked credits, RCM dues
- `gst-internal-audit/quick-diagnosis-triage.md` — First-read triage — notice form → skill routing + urgency weight table
- `gst-internal-audit/r1-3b-reconciler.md` — GSTR-1 vs GSTR-3B reconciliation — 6-type variance classification

### Legal archive
- `legal-archive/budget-amendment-tracker.md` — Finance Act 2022–2025 amendments and impact matrix
- `legal-archive/cbic-circular-index.md` — Searchable CBIC circular index — 10 topic categories
- `legal-archive/karnataka-sgst-overlay.md` — Karnataka SGST state-specific overlay (state code 29)
- `legal-archive/maharashtra-trade-circulars.md` — Maharashtra GST Trade Circular index — 8 categories
- `legal-archive/template-state-overlay.md` — Template for new jurisdictional state overlays

### Thresholds & limits
- `gst-thresholds/SKILL.md` — Penalty rates, limitation periods, interest rates
