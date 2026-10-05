# Export Reconciliation: GSTR-1 vs. GSTR-3B vs. ICEGATE

## 1. Why Reconciliation is Essential
For both **LUT Refunds (RFD-01)** and **Automated ICEGATE Refunds**, tax authorities and customs algorithms compare three primary reporting touchpoints. A mismatch between any of these three will result in refund delays or deficiency memos:
1. **GSTR-1 Table 6A** (Invoice-level detail of Zero-Rated Supplies)
2. **GSTR-3B Table 3.1(b)** (Consolidated Outward Taxable Supplies — Zero Rated)
3. **ICEGATE Shipping Bill / Customs EDI Data**

---

## 2. Three-Way Reconciliation Matrix

```
┌────────────────────────────────────────────────────────────────────────┐
│                        THREE-WAY MATCH VERIFIER                        │
├───────────────────────┬────────────────────────┬───────────────────────┤
│ GSTR-1 (Table 6A)     │ GSTR-3B (Table 3.1b)   │ ICEGATE Shipping Bill │
├───────────────────────┼────────────────────────┼───────────────────────┤
│ • Invoice No & Date   │ • Total Taxable Value  │ • Invoice No & Date   │
│ • Shipping Bill No    │ • Total IGST Paid      │ • Shipping Bill No    │
│ • Port Code (6-digit) │                        │ • Port Code           │
│ • Taxable Value       │                        │ • FOB Value / IGST    │
│ • IGST / Cess Amount  │                        │ • Let Export Order    │
└───────────────────────┴────────────────────────┴───────────────────────┘
```

---

## 3. Common Discrepancies & Audit Traps

### A. Value Mismatches (FOB vs. CIF vs. Taxable Value)
- **The Issue**: Commercial invoice may be priced on CIF (Cost, Insurance & Freight) basis, while customs assesses export duty/value on FOB (Free On Board) basis.
- **Rule**: In GSTR-1 Table 6A, declare the **actual invoice value** (or transaction value as per Section 15 of CGST Act). Ensure the Shipping Bill clearly reflects the invoice value breakdown (FOB + Freight + Insurance).

### B. IGST Paid in GSTR-1 $\neq$ GSTR-3B Table 3.1(b)
- **The Issue**: Sum of IGST across Table 6A invoices in GSTR-1 is greater than the amount declared and paid under Table 3.1(b) in GSTR-3B.
- **Impact**: ICEGATE validates that `IGST Paid in GSTR-3B Table 3.1(b) >= IGST claimed in Table 6A`. If GSTR-3B payment is lower, the transmission is rejected.
- **Fix**: Pay differential tax through Form GST DRC-03 or rectify in the subsequent tax period.

### C. Typographical Errors in Port Code or Shipping Bill Number
- **The Issue**: 6-digit Port Code entered incorrectly (e.g., entering `INBOM` instead of specific EDI port `INBOM4` or `INNSA1`), or entering date in `YYYY-MM-DD` instead of `DD-MM-YYYY`.
- **Fix**: Amend the record in next month's GSTR-1 via **Table 9A (Amended Export Invoices)**.

---

## 4. Pre-Filing Monthly Reconciliation Checklist

Use this checklist prior to submitting GSTR-1 and GSTR-3B returns for any export period:

- [ ] **Invoice Series**: All export invoices have a distinct serial numbering sequence compliant with Rule 46 of CGST Rules.
- [ ] **Endorsement Text**: Each export invoice bears the mandatory statutory LUT / IGST declaration text.
- [ ] **Shipping Bill & Port Code Availability**: Shipping bill numbers and 6-character port codes have been received from the CHA and entered in Table 6A.
- [ ] **GSTIN Consistency**: Exporter GSTIN on the Shipping Bill matches the GSTIN filing the return exactly.
- [ ] **Value Alignment**: Taxable value and IGST amount in GSTR-1 Table 6A match line-for-line with the customs EDI data.
- [ ] **GSTR-3B Summary Match**: Sum of Table 6A taxable value and IGST matches Table 3.1(b) of GSTR-3B.
- [ ] **Currency Conversion**: Foreign currency conversions are made using the CBIC customs exchange rate notified on the date of filing the Shipping Bill.
