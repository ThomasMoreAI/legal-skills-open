---
name: gst-export-compliance-om-talaviya
title: GST Export Compliance (India) — Ground-Truth Regulatory Engine
description: Guides Indian exporters (goods or services) through GST compliance, high-risk regulatory traps, and refund mechanics — LUT (Letter of Undertaking) filing, zero-rated supply treatment, Rule 96(10) Advance Authorisation restrictions, Rule 96B foreign exchange non-realization clawback, IGST refund via ICEGATE/shipping bill, GSTR-1 and GSTR-3B reconciliation, Export of Services vs. Intermediary tax traps (Section 13(8)(b)), and RFD-01 refund applications. Use this whenever the user mentions exporting from India, GST on exports, LUT, zero-rated supply, IGST refund, shipping bill, ICEGATE, GSTR-1, GSTR-3B, RFD-01, EDPMS, FEMA 9-month realization, or asks how GST works for their export/import business. This is a preparer/explainer skill, not a filing agent — it produces computations, checklists, and draft data, and always tells the user to verify current rates/forms and consult a CA before filing.
author: Om-Talaviya
author_url: https://github.com/Om-Talaviya/claude-trade-skills/tree/main/skills/gst-export-compliance
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: in
practice: tax
language: en
sources:
- title: Export Services Compliance
  path: references/export-services-compliance.md
- title: Fema Edpms Compliance
  path: references/fema-edpms-compliance.md
- title: Gstr Reconciliation
  path: references/gstr-reconciliation.md
- title: Igst Refund Icegate
  path: references/igst-refund-icegate.md
- title: Lut Filing
  path: references/lut-filing.md
- title: Rfd01 Lut Refund
  path: references/rfd01-lut-refund.md
---

# GST Export Compliance (India) — Ground-Truth Regulatory Engine

## Purpose & Scope
Indian exporters — goods or services — who need to navigate the high-stakes GST and customs framework for their exports: selecting between LUT and IGST payment, structuring zero-rated invoices, avoiding lethal traps like **Rule 96(10)** or **Intermediary reclassification**, claiming ICEGATE/RFD-01 refunds, and tracking **RBI EDPMS / FEMA 9-month realization timelines**.

> [!CAUTION]
> **CRITICAL LEGAL & TAX WARNING**: Export compliance errors in India carry severe statutory consequences under the CGST Act, IGST Act, Customs Act, and FEMA — including **18% interest, 100% penalties under Section 74, frozen bank accounts, and potential prosecution under Section 132**. This skill acts as a precision computational and drafting guide; all filings must be approved by a qualified Chartered Accountant (CA) or Customs Broker (CHA).

---

## 🛑 ZERO ASSUMPTIONS & GROUND TRUTH PROTOCOL

To ensure absolute safety and prevent catastrophic compliance errors, the AI must strictly enforce these ground-truth rules:

1. **NEVER Assume Duty-Free Inputs Status**: Never assume whether an exporter has availed Advance Authorisation, DFIA, EOU, or concessional 0.1% GST. If unknown, the agent MUST explicitly ask or present the Rule 96(10) restriction upfront.
2. **NEVER Assume Exchange Rates**: Never use arbitrary market spot rates for customs valuation. Section 14 of the Customs Act mandates using the **CBIC notified exchange rate in effect on the date of filing the Shipping Bill**.
3. **NEVER Guess or Assert HSN/SAC Codes as Final**: Never invent or assert a tariff code with finality. Provide candidate headings based on the official tariff schedule and require confirmation against the CBIC HSN portal.
4. **NEVER Assume Service Export Eligibility**: For services, never assume zero-rating until verifying that payment is received in convertible foreign currency (or approved Special Vostro Account) and that the service is not an Intermediary arrangement under Section 13(8)(b).
5. **NEVER Assume Turnover Proportions**: In Rule 89(4) calculations, never assume total turnover equals export turnover. Always demand exact figures for Adjusted Total Turnover, Net ITC, and verify the **1.5x domestic like-goods valuation cap**.

---

## The 4 High-Risk Traps Every Export Answer Must Guard Against

### 1. The Rule 96(10) Prohibition Trap
- **The Trap**: If an exporter has imported raw materials under **Advance Authorisation (AA)**, **DFIA**, or **EOU scheme** (Notification No. 78/79-Customs), or purchased domestic inputs at the concessional **0.1% merchant export rate** (Notification No. 40/2017 or 41/2017), they are **STATUTORILY FORBIDDEN FROM EXPORTING ON PAYMENT OF IGST WITH AUTOMATED REFUND**.
- **The Consequence**: Claiming an IGST refund in violation of Rule 96(10) triggers immediate Show Cause Notices (SCN) demanding 100% refund recovery + 18% interest + penalty.
- **The Safeguard**: Always check if the exporter availed duty-free input schemes. If YES $\rightarrow$ **They MUST export under LUT only**.

### 2. The Rule 96B Foreign Exchange Clawback Trap
- **The Trap**: Under GST **Rule 96B**, if export proceeds are not realized in convertible foreign exchange within the **RBI/FEMA 9-month window**, the entire GST refund (IGST or ITC) **must be paid back to the government with 18% interest within 30 days**.

### 3. The "Export of Services" vs. "Intermediary" Trap (Section 13(8)(b) IGST Act)
- **The Trap**: IT/tech/marketing consultants who act as brokers, agents, or facilitators between foreign clients and third parties are classified as "Intermediaries". Under Section 13(8)(b), their Place of Supply is deemed to be **India**, disqualifying them from zero-rating and triggering **18% GST liability retroactively**.
- **The Safeguard**: Must satisfy all 5 cumulative tests under Section 2(6) of IGST Act (see [references/export-services-compliance.md](file:///skills/gst-export-compliance/references/export-services-compliance.md)).

### 4. SCOMET & Dual-Use Restrictions
- **The Trap**: Exporting items covered under DGFT SCOMET categories without a specific license is a non-bailable offense under the Weapons of Mass Destruction (WMD) Act and FTDR Act.

---

## Core Decision Framework: LUT vs. IGST Payment

```
                               ┌─────────────────────────────┐
                               │  Exporting from India       │
                               └──────────────┬──────────────┘
                                              │
                     ┌────────────────────────┴────────────────────────┐
                     ▼                                                 ▼
        Availing Duty-Free Inputs?                       Standard Domestic Inputs?
     (Advance Auth / EOU / 0.1% GST)                    (Paid standard GST on inputs)
                     │                                                 │
                     ▼                                                 ▼
      ┌─────────────────────────────┐                  ┌──────────────────────────────┐
      │     MUST USE OPTION A       │                  │  CAN CHOOSE OPTION A or B    │
      │  Export under LUT (RFD-11)  │                  ├──────────────────────────────┤
      │  No IGST Paid Upfront       │                  │ Option A: LUT + RFD-01 ITC   │
      │  Claim ITC via RFD-01       │                  │ Option B: Pay IGST + ICEGATE │
      └─────────────────────────────┘                  └──────────────────────────────┘
```

---

## Dynamic Routing to Specialized Reference Modules

Load only the reference file matching the user's specific context:

- **[references/lut-filing.md](file:///skills/gst-export-compliance/references/lut-filing.md)**: Form GST RFD-11 filing, witness details, validity timeline, and lapse condonation.
- **[references/igst-refund-icegate.md](file:///skills/gst-export-compliance/references/igst-refund-icegate.md)**: Shipping Bill matching, Table 6A, Rule 96(10) validations, and ICEGATE error resolution (SB001–SB006).
- **[references/gstr-reconciliation.md](file:///skills/gst-export-compliance/references/gstr-reconciliation.md)**: Three-way reconciliation between GSTR-1, GSTR-3B Table 3.1(b), and Customs EDI shipping bills.
- **[references/rfd01-lut-refund.md](file:///skills/gst-export-compliance/references/rfd01-lut-refund.md)**: Rule 89(4) ITC refund formula (1.5x domestic turnover cap, capital goods exclusion), Statement 3A prep.
- **[references/export-services-compliance.md](file:///skills/gst-export-compliance/references/export-services-compliance.md)**: 5 cumulative tests of Section 2(6), Intermediary defense, and FIRC/e-BRC purpose codes.
- **[references/fema-edpms-compliance.md](file:///skills/gst-export-compliance/references/fema-edpms-compliance.md)**: RBI 9-month realization clock, EDPMS caution-listing defense, write-offs, and Rule 96B repayment.
