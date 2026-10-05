# Export of Services Compliance & The "Intermediary" Tax Trap (India)

## 1. Statutory Definition of "Export of Services" (Section 2(6) of IGST Act)
For any service provided to a foreign client to qualify as a **Zero-Rated Export of Service**, ALL FIVE conditions must be met cumulatively. If even ONE condition fails, the supply is treated as a **taxable domestic supply liable to 18% IGST**:

```
┌────────────────────────────────────────────────────────────────────────┐
│             5 CUMULATIVE CONDITIONS UNDER SECTION 2(6)                 │
├────────────────────────────────────────────────────────────────────────┤
│ 1. Supplier of service is located in India.                            │
│ 2. Recipient of service is located outside India.                      │
│ 3. Place of Supply of the service is outside India (Section 13).       │
│ 4. Payment received in CONVERTIBLE FOREIGN EXCHANGE or in Indian       │
│    Rupees via RBI-approved Special Rupee Vostro Account (SRVA).        │
│ 5. Supplier and recipient are NOT merely establishments of a distinct │
│    person (e.g. Indian branch billing its foreign head office).        │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. The Lethal "Intermediary" Trap (Section 13(8)(b) IGST Act)

### What is an Intermediary?
Under Section 2(13) of the IGST Act, an **"Intermediary"** means a broker, agent, or any other person who arranges or facilitates the supply of goods or services between two or more persons, but does not include a person who supplies such goods or services on his own account.

### The Fatal Trap:
- For general services (software development, SaaS, design, engineering, consulting), the Place of Supply under Section 13(2) is the **Location of the Recipient (Outside India)** $\rightarrow$ **0% GST under LUT**.
- For **Intermediary Services** (business development agents, lead generation, commissioning agents, marketing facilitators for foreign sellers), Section 13(8)(b) mandates that the **Place of Supply is the LOCATION OF THE SUPPLIER (India)**!
- **Consequence**: Even if you bill an entity in the USA and receive US Dollars into your Indian bank account, tax authorities will classify you as an intermediary, deny zero-rating, and demand **18% GST on gross receipts with 18% interest + 100% penalty** under Section 74.

### How to Protect Against Intermediary Classification:
- **Principal-to-Principal Basis**: Service agreement must explicitly state that services are provided on your own account (as principal) and not as an agent/broker arranging sales.
- **Direct Sub-contracting vs. Facilitation**: Provide the deliverable directly (e.g., custom code, research reports, creative assets) rather than introducing the foreign client to 3rd party vendors.
- **CBIC Circular No. 159/15/2021-GST**: Study and cite the circular clarifying that backend IT/support services provided on own account do not constitute intermediary services.

---

## 3. Foreign Currency Realization Rules (Convertible Forex vs. INR)
- **Payment Mode**: Must be received in **convertible foreign currency** (USD, EUR, GBP, JPY, etc.) or INR through approved Vostro Accounts.
- **Payment Gateways (Stripe, PayPal, Payoneer)**:
  - If using payment aggregators, ensure you obtain the **Foreign Inward Remittance Statement (FIRS) / FIRC / NOC Purpose Code Certificate** from the processing bank confirming foreign inward receipt.
  - Domestic payments received in INR from a foreign company's Indian subsidiary/entity DO NOT qualify as export of services.

---

## 4. Documentation Checklist for Export of Services

- [ ] Valid **Letter of Undertaking (LUT)** for the financial year.
- [ ] **Master Services Agreement (MSA) / Statement of Work (SOW)** proving principal-to-principal engagement.
- [ ] Export Invoice in foreign currency (or equivalent INR) with mandatory LUT endorsement.
- [ ] **FIRC / FIRS / e-BRC** with statutory RBI Purpose Code (e.g., `P0802` for Software Implementation, `P0803` for Data Processing).
- [ ] GSTR-1 Table 6A entry & GSTR-3B Table 3.1(b) reporting.
