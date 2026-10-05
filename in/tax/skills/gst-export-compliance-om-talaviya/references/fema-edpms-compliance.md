# FEMA Realization, EDPMS Tracking & Rule 96B GST Refund Clawback

## 1. The Statutory FEMA Timeline (Foreign Exchange Management Act)
Under Regulation 9 of the Foreign Exchange Management (Export of Goods and Services) Regulations, 2015:
- **Statutory Window**: The full value of goods or software/services exported out of India must be realized in convertible foreign exchange and repatriated to India within **9 months** from the date of export (or invoice date for services).
- **Warehouse Exports**: Up to **15 months** for goods exported to overseas warehouses established with RBI permission.

---

## 2. The Lethal GST Rule 96B Clawback Mechanism
Under **Rule 96B of the CGST Rules, 2017 (introduced by Notification No. 16/2020-Central Tax)**:

```
┌────────────────────────────────────────────────────────────────────────┐
│                      RULE 96B REFUND RECOVERY CLOCK                    │
├────────────────────────────────────────────────────────────────────────┤
│ If export proceeds are NOT realized within the FEMA 9-month window     │
│ (or RBI-extended period):                                              │
│                                                                        │
│ 1. The exporter MUST REPAY the entire GST refund amount claimed        │
│    (whether IGST refund or unutilized ITC refund under LUT)            │
│ 2. PLUS INTEREST AT 18% p.a. under Section 50                          │
│ 3. Repayment must be made WITHIN 30 DAYS of the 9-month expiry.         │
│ 4. Failure to repay triggers attachment of bank accounts & properties  │
│    under Section 79 of the CGST Act.                                   │
└────────────────────────────────────────────────────────────────────────┘
```

*Note: If the proceeds are realized subsequently within the legally extended window, the exporter can reclaim the refunded amount by filing Form GST DRC-03 / refund application within 3 months of realization.*

---

## 3. RBI EDPMS & IDPMS Tracking System

### What is EDPMS?
The **Export Data Processing and Monitoring System (EDPMS)** is an automated portal managed by the Reserve Bank of India (RBI) that connects:
- Indian Customs (ICEGATE Shipping Bills)
- Authorized Dealer (AD) Banks (Inward Forex Remittances / IRMs)
- Exporter IEC (DGFT)

### The Caution-Listing Disaster:
1. When a Shipping Bill is filed, customs transmits the record to EDPMS.
2. When foreign payment arrives, the AD Bank generates an **Inward Remittance Message (IRM)** and settles (knocks off) the Shipping Bill on EDPMS, generating an electronic **e-BRC (electronic Bank Realization Certificate)**.
3. If a Shipping Bill remains open/unsettled beyond **9 months**, the RBI algorithm automatically flags the exporter as **Caution-Listed**.
4. **Impact of Caution-Listing**:
   - Immediate freeze on bank AD Code for customs clearance.
   - Customs EDI stops approving Let Export Orders (LEO).
   - Inward remittances get held for manual compliance scrutiny.
   - DGFT revokes export incentives (RoDTEP, RoSCTL, Duty Drawback).

---

## 4. Safeguards & Best Practices for Exporters

- [ ] **Monitor EDPMS Monthly**: Request an **EDPMS Open Shipping Bill Report** from your AD Bank every month to ensure payments were matched against the correct Shipping Bill numbers.
- [ ] **FIRC / IRM Reconciliation**: Ensure inward remittance advices clearly state the relevant **Invoice Number & Shipping Bill Number** in the SWIFT MT103 field 70 (Remittance Info).
- [ ] **File for Extension of Realization**: If the foreign buyer defaults or delays payment, formally apply for an extension to the Authorized Dealer bank **before the 9-month period expires** citing legitimate trade disputes or bankruptcy proceedings.
- [ ] **Write-Off Provisions**: If debt is irrecoverable, follow RBI Master Direction on Export of Goods and Services to process an authorized **Write-Off** through the AD bank (up to 10% self-write-off / 15% through AD bank based on track record) to clear EDPMS without triggering prosecution.
