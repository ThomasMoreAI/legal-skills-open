---
name: prompt-pack-supply-agreement-sboghossian
title: Supply Agreement
description: Use when a supplier and buyer need to draft a supply agreement governing the purchase and delivery of goods or materials, covering product specifications, pricing, ordering procedures, delivery terms, quality standards, warranties, rejection rights, and force majeure. MENA-specific guidance covers UAE sale of goods principles under the Civil Transactions Law, DIFC contract law, CISG applicability in MENA contexts, Incoterms 2020 selection, and Arabic-language documentation for enforcement.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-supply-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Supply Agreement

## When to use this

Use this skill when:
- A supplier of goods (raw materials, manufactured products, commodities, finished consumer goods) needs a master supply agreement with a buyer covering an ongoing supply relationship.
- A buyer wants to establish a framework agreement with a supplier that will govern multiple purchase orders over time.
- An international supply chain arrangement needs documentation that covers cross-border delivery terms, quality controls, and dispute resolution.
- A company is entering a supply arrangement in a MENA market and needs to navigate local import regulations, certification requirements, and payment mechanisms.

**Distinguish from:** A services agreement (use [[prompt-pack-service-agreement]]) for performance of services; a reseller agreement (use [[prompt-pack-reseller-agreement]]) for re-sale of purchased goods to third parties.

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| **Supplier name and jurisdiction** | Determines applicable export/import obligations and governing law | Ask |
| **Buyer name and jurisdiction** | Determines applicable import obligations and governing law | Ask |
| **Description of goods** | Must be sufficiently specific to be enforceable; reference a product specification schedule | Ask |
| **Pricing mechanism** | Fixed price / indexed price / formula-based | Ask |
| **Delivery terms (Incoterms)** | Determines when title and risk pass; who pays freight and insurance | Ask; if unknown, default to DDP (Delivered Duty Paid) for simplicity or DAP; specify Incoterms 2020 |
| **Jurisdiction / governing law** | Determines implied terms for goods quality, remedies for defective goods | Ask |

## Optional inputs

- **Exclusivity** — whether the buyer commits to purchasing exclusively from this supplier, or whether the supplier commits to supply exclusively to this buyer in a territory.
- **Minimum purchase commitments / take-or-pay** — whether the buyer must purchase a minimum quantity per period.
- **Price adjustment mechanisms** — CPI indexation, raw material cost pass-through, periodic renegotiation.
- **Sustainability / ESG requirements** — increasingly required by multinational buyers; supplier code of conduct, audit rights.
- **Force majeure** — specific force majeure events relevant to the supply chain (pandemic, port closures, sanctions).

## Document structure

1. **Definitions**
   - Goods, Products, Specifications, Purchase Order, Order Acknowledgment, Delivery Date, Delivery Location, Incoterms, Defective Goods, Warranty Period.

2. **Supply obligation**
   - Supplier agrees to supply the Goods to the Buyer in accordance with the terms of this Agreement and each Purchase Order.
   - Buyer agrees to purchase and pay for the Goods ordered under accepted Purchase Orders.
   - If exclusivity: "During the Term, [Buyer/Supplier] shall [purchase exclusively from / supply exclusively to] [the other party] in [territory/product category]."

3. **Specifications**
   - Goods must conform to the Specifications set out in Schedule 1.
   - Changes to Specifications: require written agreement and may affect price.
   - Technical standards: reference any applicable ISO, CE, ESMA, SASO, or other standards the goods must meet (see Jurisdictional notes for MENA certification requirements).
   - Custom development: if goods are manufactured to the buyer's design, include IP ownership and tooling cost provisions.

4. **Ordering process**
   - Purchase Orders: the buyer issues Purchase Orders in writing (form in Schedule 2).
   - Order acknowledgment: supplier must accept or reject within [3/5] business days.
   - Order binding: a Purchase Order is binding on both parties only upon the supplier's written acceptance (Order Acknowledgment).
   - Forecasts: rolling [3/6/12]-month forecasts provided by the buyer; binding only for the first [1] month.
   - Minimum order quantities: [specify or state N/A].

5. **Pricing**
   - Price: as set out in the Price Schedule (Schedule 3), or as confirmed in each accepted Purchase Order.
   - Price changes: supplier may change prices for new orders with [60/90 days'] written notice; pending orders are at the price at time of order.
   - Volume discounts: [specify tiers if applicable].
   - Taxes: prices exclusive of VAT; buyer responsible for applicable import duties, VAT, and customs charges.
   - Price escalation: [CPI escalation clause / raw material cost-passthrough formula / fixed for the term].

6. **Payment terms**
   - Payment on [net 30/45/60] days from invoice date.
   - Invoice date: on or after delivery / on shipment.
   - Currency: [USD / AED / SAR / EUR].
   - Late payment: interest at [rate]% per annum from due date (check KSA position on conventional interest).
   - Disputed invoices: buyer must raise dispute within [10] business days of invoice; pay undisputed portion; dispute resolved per dispute resolution clause.
   - Letter of credit (L/C): for international supply arrangements, consider whether an L/C is appropriate (protects seller against buyer default).

7. **Delivery**
   - Incoterms: [DAP / DDP / FCA / CIF] [Location] (Incoterms 2020).
   - Delivery date: as agreed in each Purchase Order.
   - Lead time: supplier must maintain a lead time of [X weeks/months] for standard orders.
   - Early delivery: subject to buyer's acceptance.
   - Late delivery: [specify consequences: liquidated damages at [X% per week] / right to cancel specific order / right to procure from alternative supplier and charge supplier the difference].
   - Title and risk: transfer per the agreed Incoterms.

8. **Inspection and acceptance**
   - Buyer has [10/15] business days from delivery to inspect the Goods.
   - Rejection: buyer must notify supplier in writing specifying the defect within the inspection period; failure to reject within the period = deemed acceptance.
   - Non-conforming goods: supplier must [repair, replace, or issue a credit note] within [X] business days.
   - Hidden defects: if a defect is not reasonably discoverable on inspection, buyer may reject within a reasonable period of discovery.

9. **Quality warranties**
   - Supplier warrants that all Goods delivered will:
     - Conform to the Specifications.
     - Be free from material defects in materials and workmanship.
     - Comply with applicable laws and standards in the jurisdiction of delivery.
     - Not infringe any third-party IP rights.
   - Warranty period: [12/24] months from delivery (or [6/12] months from use in production, whichever is earlier, for industrial goods).
   - Warranty remedies: repair or replacement at supplier's election; or refund if repair/replacement is not possible within [30] days.
   - Disclaimer: no other warranty is given; implied warranties of merchantability and fitness for purpose excluded to the extent permitted by applicable law.

10. **Product liability and indemnification**
    - Supplier indemnifies buyer against third-party claims arising from defects in the Goods (death, personal injury, property damage).
    - Carve-out: no indemnity for defects caused by buyer's modification, misuse, or incorporation into a product against supplier's written recommendations.
    - Buyer indemnifies supplier for claims arising from buyer's own product defects or misuse.

11. **Recalls and safety**
    - If a safety issue is discovered: the party discovering it must notify the other immediately.
    - Voluntary recall: parties cooperate; costs allocated based on which party's defect caused the recall.
    - Regulatory recall: mandatory recall by a government authority; immediate compliance required; costs allocated per cause.

12. **Force majeure**
    - Events: war, pandemic, natural disaster, government order, strike, port closure, sanctions.
    - Trigger: supplier gives notice within [5] business days of the force majeure event; obligations are suspended.
    - Duration: if force majeure continues beyond [60/90] days, either party may terminate the affected Purchase Orders and (if extended materially) the Agreement.
    - Not covered: price increases, financial difficulty, foreseeable supply chain disruptions.

13. **Confidentiality**
    - Standard mutual confidentiality for pricing, specifications, customer information.
    - Buyer's specifications are confidential; supplier may not use them for other customers.

14. **Term and termination**
    - Initial term: [1/2/3] years.
    - Renewal: automatic unless either party gives [90 days'] notice of non-renewal.
    - Termination for cause: material breach (including consistent late delivery, persistent quality failures); insolvency.
    - Termination for convenience: [90/180 days'] notice; buyer must pay for goods already ordered under accepted Purchase Orders.
    - Effect: outstanding Purchase Orders completed or cancelled per agreement.

15. **Governing law and dispute resolution**
    - Governing law.
    - Arbitration / litigation per preference.

## Jurisdictional notes

### UAE — onshore (UAE Civil Transactions Law Arts. 524+ on Sale)
- UAE CTL governs sale of goods for UAE-based transactions; implied warranties of conformity and fitness for purpose are recognized.
- Inspection and rejection period: under UAE law, the buyer must inspect goods on delivery and raise defects promptly; delayed inspection may waive the right to reject.
- CISG: UAE is a signatory to the UN Convention on Contracts for the International Sale of Goods (CISG); the CISG applies to international sale of goods contracts between parties in different Contracting States unless excluded. Most commercial lawyers expressly exclude the CISG for clarity ("The parties exclude the application of the UN Convention on Contracts for the International Sale of Goods").
- Product certification: ESMA (Emirates Authority for Standardization and Metrology) certification required for many consumer and industrial products imported into UAE; ensure the supplier's goods have required ESMA approval.

### KSA
- SASO (Saudi Standards, Metrology and Quality Organization): mandatory product certification for many goods imported into KSA; supplier must confirm SASO compliance.
- Halal certification: required for food products; consider as a warranty in the Specifications.
- Interest on late payment: avoid conventional interest; rephrase as a penalty or delay compensation clause.

### DIFC / ADGM
- DIFC Contract Law governs; CISG exclusion recommended.
- Standard common-law sale of goods principles.

### Lebanon / Egypt
- Civil Code sale of goods provisions apply.
- CISG applies to international sales (both are Contracting States) unless excluded.

### EU / UK
- EU: Sale of Goods Directive (2019/771 for B2C; 2019/770 for digital goods); general contract law for B2B.
- UK: Sale of Goods Act 1979 and Supply of Goods and Services Act 1982 for implied terms; mostly freely negotiated in B2B contracts.
- CISG: UK is not a Contracting State (post-Brexit); EU member states are.

## Drafting standards

- Attach the Specifications as a detailed Schedule 1 — the more precise the specification (including testing standards, tolerance levels, packaging requirements), the less room for dispute.
- Incoterms selection: always specify the version (Incoterms 2020); specify the named place precisely ("DAP, Port of Jebel Ali, UAE — Incoterms 2020").
- For long-term supply agreements: include a price review mechanism; fixed prices over a 5-year term with rising raw material costs will strain the relationship.
- Liquidated damages for late delivery: calibrate to actual loss; an excessive LD clause may be reduced by a court/tribunal (UAE CTL Art. 390; DIFC Contract Law).

## Common mistakes

- **No Incoterms specified.** When delivery terms are vague ("delivery to buyer's warehouse"), disputes arise about who bears the freight cost and when risk passes.
- **CISG not excluded.** If both parties are in CISG Contracting States and the agreement is silent on the CISG, it may apply and override certain negotiated provisions.
- **No minimum order quantity or take-or-pay.** Without purchase commitments, the supplier bears the risk of excess inventory and unused capacity; commercial agreements should allocate this risk.
- **Warranty period not pegged to actual use.** A warranty period from delivery date may expire before the goods are put into use; consider an alternative trigger (installation date, first use date).

## Related skills

- [[prompt-pack-service-agreement]]
- [[prompt-pack-reseller-agreement]]
- [[prompt-pack-standard-nda]]
- [[prompt-pack-settlement-agreement]]
- [[heuristic-always-state-jurisdiction-first]]
- [[heuristic-no-us-style-boilerplate-in-civil-law-jx]]
