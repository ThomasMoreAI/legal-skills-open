# Automatic IGST Refund on Export of Goods via ICEGATE

## 1. Overview & Statutory Mechanism (Rule 96)
Under **Rule 96 of the CGST Rules, 2017**, when goods are exported on payment of IGST:
- The **Shipping Bill** filed by the exporter is itself deemed to be an application for refund of integrated tax once:
  1. The person in charge of the conveyance files an **Export General Manifest (EGM)** or Departure Manifest with the departure date.
  2. The exporter furnishes a valid return in **Form GSTR-1** (specifically Table 6A) and **Form GSTR-3B** with full tax payment.

---

## 2. CRITICAL BARRIER: The Rule 96(10) Prohibition Trap
Before selecting the IGST-Paid export track, verify whether the exporter has availed any of the following benefits:
- Import of inputs under **Advance Authorisation (AA)** or **DFIA** (Notification No. 78/2017-Customs or 79/2017-Customs).
- Procurement from **Export Oriented Units (EOU)**.
- Domestic inputs purchased at concessional **0.1% GST** (Notification No. 40/2017-Central Tax or 41/2017-Integrated Tax).

> [!CAUTION]
> **STATUTORY BARRIER**: If ANY of the above benefits were availed on inputs, the exporter is **PROHIBITED under Rule 96(10)** from exporting on payment of IGST and receiving automated refunds. Attempting to claim IGST refunds will result in full refund recovery with **18% interest and penalty under Section 74**. Such exporters MUST export under **Letter of Undertaking (LUT)** without paying IGST.

---

## 3. The Rule 96B Mandatory Repayment Clock
Under **Rule 96B of the CGST Rules, 2017**:
- If foreign exchange proceeds from the export are not realized within the **FEMA statutory period (9 months from export date)**, the exporter **MUST REPAY the entire IGST refund amount + 18% interest within 30 days** of the 9-month expiration.
- Failure to repay triggers recovery proceedings under Section 79 (bank account attachment).

---

## 4. Essential Prerequisites for Automated Payout
To avoid processing freezes, ensure these four data points match across customs and GST systems:

```
┌───────────────────────────┐      ┌───────────────────────────┐
│     GSTN Portal (GSTR-1)  │      │     ICEGATE Customs EDI   │
├───────────────────────────┤      ├───────────────────────────┤
│ • Invoice Number & Date   │ <==> │ • Invoice Number & Date   │
│ • Port Code (6 Char)      │ <==> │ • Port Code (e.g. INNSA1) │
│ • Shipping Bill Number    │ <==> │ • Shipping Bill Number    │
│ • Shipping Bill Date      │ <==> │ • Shipping Bill Date      │
│ • IGST & Cess Paid Amount │ <==> │ • IGST Declared on SB     │
└───────────────────────────┘      └───────────────────────────┘
```

---

## 5. Bank Account & AD Code Validation on ICEGATE
- Ensure the Authorized Dealer (AD) Code and Bank Account are **registered and validated on ICEGATE (Customs EDI)**.
- If the bank account status shows "PFMS Rejected" or "Invalid Account", the refund scroll cannot credit funds.

---

## 6. ICEGATE Error Code Matrix & Instant Fixes

| Error Code | Error Description | Root Cause | Immediate Resolution / Fix |
| :--- | :--- | :--- | :--- |
| **SB000** | Successfully Matched | Perfect match between GSTN and ICEGATE. | Scroll generated; funds credited to bank account within 2–5 business days. |
| **SB001** | Invalid Status / EGM Not Filed | EGM has not been filed by the airline/shipping line. | Contact shipping line / Custom House Agent (CHA) to file/update EGM. |
| **SB002** | EGM Error | Gateway EGM mismatch or wrong container number in manifest. | Request CHA to submit an EGM amendment to Customs. |
| **SB003** | GSTIN Mismatch | GSTIN declared on Shipping Bill differs from GSTR-1. | File an amendment request with the Assistant Commissioner of Customs at port of export. |
| **SB004** | Record Already Exists | Duplicate invoice record transmitted by GSTN. | Inform ICEGATE helpdesk; usually auto-resolves on next scroll cycle. |
| **SB005** | Invoice Number / Port Code Mismatch | Invoice number, date, or port code in Table 6A of GSTR-1 differs from Shipping Bill. | Amend Table 6A using **Table 9A (Amended Export Invoices)** in the next GSTR-1 return. |
| **SB006** | Gateway Port Mismatch | Cargo moved from ICD to Gateway Port, but Gateway Port details are missing/mismatched. | Approach CHA to file Gateway EGM integration report. |

---

## 7. Mandatory Invoice Endorsement for IGST Paid Exports

```text
"SUPPLY MEANT FOR EXPORT/SUPPLY TO SEZ UNIT OR SEZ DEVELOPER FOR AUTHORISED OPERATIONS ON PAYMENT OF INTEGRATED TAX"
```
