---
name: draft-guarantee-sboghossian
title: Guarantee (Surety / Personal)
description: Use when drafting a guarantee (surety or personal) whereby a guarantor undertakes to satisfy the obligations of a principal debtor to a beneficiary. Covers the two main structures (demand guarantee vs. conditional surety), mandatory clauses, MENA-specific nuances (KSA Sharia kafala vs. commercial guarantee, UAE Commercial Code Federal Law 18/1993, DIFC/ADGM common-law demand guarantees, LB civil-law aval), independence from the underlying transaction, and the distinction between a guarantee and a standby letter of credit.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-guarantee
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: finance
language: en
---

# Guarantee (Surety / Personal)

## When to use this

A guarantee is a secondary obligation: the guarantor undertakes to pay or perform if the principal debtor fails to do so. Guarantees arise in:

- **Trade finance**: supplier / buyer relationships (bank guarantee for payment).
- **Construction / EPC**: contractor performance guarantees to employer; advance-payment guarantees.
- **Finance facilities**: shareholders / parent companies providing personal or corporate guarantees to lenders.
- **Lease agreements**: parent company guarantee for subsidiary tenant.
- **Government / procurement**: tender bond; performance bond; retention bond.
- **Debt restructuring**: guarantor arrangements modified as part of workout.

**Before drafting, determine which structure is needed:**
1. **Demand guarantee (on-demand / autonomous)**: guarantor pays on written demand, without the beneficiary needing to prove the underlying default. Common in trade finance and construction.
2. **Conditional guarantee (surety)**: guarantor's liability is contingent on actual default by the principal debtor. More protective of the guarantor; allows defenses from the underlying contract.

## Required inputs

| Input | Why it matters | Default |
|-------|----------------|---------|
| Guarantor (name, entity type, jurisdiction) | Determines capacity to guarantee and Sharia compliance in MENA | — |
| Beneficiary (party in whose favour guarantee is issued) | Must be specified; demand must be by the beneficiary or its successor | — |
| Principal debtor (party whose obligations are guaranteed) | Underlying obligation reference | — |
| Underlying obligation reference | Describes what is guaranteed (specific contract, facility, amount) | Schedule A |
| Maximum liability amount (cap) | Controls guarantor's exposure; almost always negotiated | — |
| Duration / expiry date | Guarantee expires on the stated date unless the demand has been made | — |
| Demand mechanics | What triggers payment obligation: written demand; certified default | Demand: written demand form |
| Governing law | Critical for independence doctrine and defenses | English law (demand guarantees) |

## Document structure

### 1. Recitals
Identify the underlying transaction (e.g., "the Principal has entered into a Construction Contract dated [date] with the Beneficiary for [project description]"). The guarantee secures the Principal's performance under that contract.

### 2. Guarantee declaration
> "[Demand guarantee]: In consideration of the Beneficiary entering into the [Underlying Contract] with the Principal, the Guarantor hereby irrevocably and unconditionally undertakes to pay to the Beneficiary on demand any sum up to the Maximum Amount."

> "[Conditional surety]: The Guarantor hereby guarantees to the Beneficiary the due and punctual performance by the Principal of all obligations under the [Underlying Contract]. In the event that the Principal fails to perform any such obligation, the Guarantor shall, upon written demand by the Beneficiary (which demand must certify the Principal's default), perform or procure performance, or pay to the Beneficiary all sums due."

### 3. Payment mechanics

**On-demand guarantee:**
- Written demand to Guarantor at the notice address.
- Demand must state the amount claimed and confirm that the Principal is in default (or simply demand payment — the level of certification required is a key negotiating point).
- Payment within [3 / 5] Business Days of valid demand.

**Conditional guarantee:**
- Beneficiary must first make demand on the Principal (or demonstrate demand was futile).
- Demand to Guarantor must certify: (a) the nature of the Principal's default; (b) that demand has been made on the Principal; (c) that the default has not been remedied.
- Payment within [10 / 15] Business Days of valid demand.

### 4. Maximum liability
> "The Guarantor's aggregate liability under this Guarantee shall not exceed [amount] ('Maximum Amount'). Any payment by the Guarantor shall reduce the Maximum Amount by the amount of such payment."

Address: whether the Maximum Amount is reduced by demand payments (reducing guarantee) or remains fixed (revolving up to Maximum Amount).

### 5. Expiry and release
> "This Guarantee shall expire on [date] ('Expiry Date'). Any demand must be received by the Guarantor at its address for notices on or before the Expiry Date. If no demand has been made on or before the Expiry Date, this Guarantee shall automatically lapse and the Guarantor shall have no further liability hereunder."

Include an **automatic-extension obligation** for construction performance guarantees: if the underlying contract is extended, the Guarantor must extend the guarantee on [X] days' notice or the Beneficiary may call the guarantee.

### 6. Continuing guarantee
> "This Guarantee is a continuing security and shall not be discharged or affected by: (a) any variation, amendment, extension, or supplemental agreement to the Underlying Contract; (b) any granting of time or indulgence to the Principal; (c) the taking, releasing, or failure to perfect any other security; (d) any composition or arrangement with the Principal."

This clause ensures the guarantee survives variations and accommodations that might otherwise discharge a guarantor at common law.

### 7. Guarantor waivers (for demand guarantees)
Standard waivers to ensure the guarantee is truly on-demand:
- Waiver of right to require the Beneficiary to first proceed against the Principal or any other security.
- Waiver of right to set off any obligations of the Beneficiary against payment obligations under the guarantee.
- Waiver of right to subrogation until the Beneficiary has been paid in full.
- Waiver of the defense of failure of consideration, illegality of the Underlying Contract, or any other defense of the Principal.

### 8. Counter-indemnity
A separate document between the Principal and the Guarantor: the Principal indemnifies the Guarantor for any amounts paid out under the guarantee. Address: right of reimbursement; security provided by Principal to Guarantor; subrogation rights.

### 9. Set-off restrictions
> "The Guarantor shall not be entitled to exercise any right of set-off, counterclaim, or deduction against any sum due from it under this Guarantee."

### 10. Governing law and dispute resolution
For international demand guarantees: English law or the law of the beneficiary's jurisdiction. For MENA: DIFC/ADGM courts or ICC/DIAC arbitration provide more predictable enforcement than onshore courts in some jurisdictions.

## Jurisdictional notes

### KSA — Sharia compliance
Under Sharia principles as applied by Saudi courts:
- **Kafala (كفالة)**: Islamic law recognizes kafala (suretyship) as a security mechanism. A kafala is an accessory obligation — it is tied to the underlying obligation (not independent/autonomous).
- **Autonomous demand guarantees**: commercial courts increasingly recognize demand guarantees in trade finance contexts, particularly where governed by foreign law. However, pure autonomy (payment regardless of underlying contract validity) is more doctrinally difficult under Sharia.
- **Practice**: major Saudi banks issue standard-form demand guarantees (SAIBOR, SAMBA, etc.) that are widely accepted; structure the guarantee using a bank-guarantee format rather than a purely contractual guarantee for maximum enforceability.
- **No interest**: guarantee documentation must not include interest for overdue amounts (substitute with agreed compensation or service charge compliant with Sharia).

### UAE — Federal Law 18/1993 (Commercial Code)
- Articles 1068–1084 govern guarantees and suretyship.
- Demand guarantees are recognized; UAE courts have developed a body of practice accepting on-demand guarantees in commercial/construction contexts.
- **Fraud exception**: UAE courts will not enforce a demand guarantee if the underlying transaction is shown to be fraudulent — this is a narrower exception than in some civil-law systems.
- **DIFC / ADGM**: full common-law on-demand guarantees; DIFC Courts enforce without the civil-law accessory doctrine.

### DIFC and ADGM
- Full English common-law framework.
- Demand guarantees are enforceable without civil-law accessory requirements.
- Standard English-law autonomous guarantee form (following Meritz Fire & Marine Insurance case principles) applicable.
- DIFC Courts have issued judgments confirming independence doctrine.

### Lebanon — Civil-law framework
- Lebanese Civil Code (Articles 1056–1111) governs suretyship (cautionnement).
- Suretyship is accessory by default: surety may raise defenses of the principal debtor.
- The **aval** (specific form of guarantee for bills of exchange / promissory notes under Code of Commerce) is more independent.
- For MENA-standard demand guarantees in LB: use a governing law clause selecting English law or DIFC law; Lebanese courts will generally apply the chosen law.
- Lebanese banking-sector guarantee instruments: local banks issue standard bank guarantees; use those forms for construction/trade contexts.

### France
- French Civil Code reforms (Ordonnance 2021-1193) changed the suretyship regime.
- Personal guarantees by individuals must include specific form requirements and limitation of scope — do not exceed the debtor's assets and income.
- Disproportionality rule: a guarantee that is manifestly disproportionate to the guarantor's assets is unenforceable.
- For corporate guarantees: standard commercial practice; no form requirements beyond writing.

## Guarantee vs. letter of credit

These instruments are often confused:

| Feature | Guarantee | Standby Letter of Credit |
|---|---|---|
| Governing rules | Contract / local law | UCP 600 (documentary) or ISP 98 (standby) |
| Demand documentary requirements | Typically simple written demand | Documents specified in the credit |
| Issuer | Can be any party | Must be a bank |
| Assignment | Difficult without consent | Assignment governed by LC terms |
| Jurisdiction | Chosen-law governed | Bank's jurisdiction + UCP 600/ISP 98 |

For trade finance where the instrument will be presented through banking channels, use a standby letter of credit (SBLC) governed by ISP 98 rather than a pure contractual guarantee.

## Common mistakes

1. **Ambiguous demand trigger** — a demand guarantee that requires the beneficiary to "certify the default" is not truly on-demand; define the threshold precisely.
2. **No automatic-extension clause for construction** — if the construction program overruns, the performance guarantee may expire before practical completion; include a mandatory extension or demand mechanic.
3. **Personal guarantee without cap** — uncapped personal guarantees expose individuals to unlimited liability; always cap personal guarantees.
4. **No waiver of defenses** — if the guarantor can raise defenses from the underlying contract, the guarantee is not truly autonomous; include the standard waivers.
5. **Guarantor's jurisdiction not considered** — a guarantor based in KSA providing a guarantee under English law may face enforcement challenges; ensure the guarantee is executed under conditions that allow enforcement in the guarantor's jurisdiction.
6. **Counter-indemnity not drafted** — if the guarantor pays out, it has no documented right of recovery against the principal unless a counter-indemnity is in place.

## Related skills

- [[draft-loan-agreement]] — underlying credit facility that the guarantee secures
- [[draft-debt-restructuring]] — restructuring of underlying obligations, including guarantee modifications
- [[draft-fidic-amendment]] — construction performance securities referenced in FIDIC PC
- [[review-financial-covenants]] — guarantee obligation as part of a broader facilities covenant package
- [[kb-banking-mena]] — banking and finance law reference for MENA jurisdictions
