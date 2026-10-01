# EU law: Directive 2014/55/EU and the ViDA package

Two instruments, two different jobs. 2014/55/EU created the standard and forced public bodies to accept it. ViDA makes structured invoicing the default for VAT purposes and removes the legal obstacles Member States used to need derogations for. Status as at 2026-08-05.

## Directive 2014/55/EU — e-invoicing in public procurement

Directive 2014/55/EU of the European Parliament and of the Council of 16 April 2014, OJ L 133, 6.5.2014, p. 1.

- **Art 2(1)** — "'electronic invoice' means an invoice that has been issued, transmitted and received in a structured electronic format which allows for its automatic and electronic processing."
- **Art 6** — lists the elements of the core invoice model: process and invoice identifiers, invoice period, seller and buyer information, payee and tax representative details, contract reference, delivery details, payment instructions, allowance or charge details, line item details, invoice totals, VAT breakdown.
- **Art 7** — Member States shall ensure that **contracting authorities and contracting entities receive and process** electronic invoices which comply with the European standard and any syntax on the published list. This is the whole obligation. **It does not oblige suppliers to issue e-invoices.** Every supplier-side obligation in Europe comes from national law, not from this directive.
- **Art 11** — transposition. The core obligation applies **18 months after publication of the reference of the standard**, i.e. from **2019-04-18**; Member States could defer application for **sub-central** contracting authorities and entities by a further 12 months, i.e. to **2020-04-18**.

Text as reproduced at legislation.gov.uk/eudr/2014/55.

**Commission Implementing Decision (EU) 2017/1870 of 16 October 2017** published the reference of `EN 16931-1:2017` and the list of syntaxes `CEN/TS 16931-2:2017`. The Annex lists exactly two syntaxes:

1. UN/CEFACT Cross Industry Invoice XML message as specified in XML Schemas 16B (SCRDM — CII)
2. UBL invoice and credit note messages as defined in ISO/IEC 19845:2015

## ViDA — VAT in the Digital Age

Adopted **11 March 2025**, published in the OJ **25 March 2025**, in force **14 April 2025** (taxation-customs.ec.europa.eu/taxation/vat/vat-digital-age-vida_en). Three instruments:

| Instrument | Subject |
|---|---|
| Council Directive (EU) 2025/516 | Amends Directive 2006/112/EC (the VAT Directive) |
| Council Regulation (EU) 2025/517 | Amends Regulation (EU) No 904/2010 (administrative cooperation) |
| Council Implementing Regulation (EU) 2025/518 | Amends Implementing Regulation (EU) No 282/2011 |

The directive is layered: Articles 1 to 5 each amend the VAT Directive with a different application date, set by Article 6 (Transposition). Quotations below are from the official OJ text (CELEX 32025L0516).

### From 14 April 2025 — Article 1

Two amendments, which Member States **may** apply from 14 April 2025 (Art 6(1)):

- New second paragraph of **Art 218**: "By way of derogation from the first paragraph of this Article, Member States may, in accordance with the conditions they lay down, require taxable persons established within their territory to issue electronic invoices for supplies of goods and services within their territory, other than those referred to in Article 262."
- New paragraph of **Art 232**: "By way of derogation from the first paragraph of this Article, Member States which exercise the option set out in Article 218, second paragraph, may provide that the use of electronic invoices issued by taxable persons established within their territory is not to be subject to the acceptance of the recipient established in their territory."

**Practical effect.** A Member State may impose a domestic B2B e-invoicing mandate without an Art 395 Council derogation, and may switch off the buyer-acceptance requirement, from 14 April 2025. This is why Belgium, Germany, Poland and others no longer need a Council Implementing Decision, and why existing derogations (e.g. Romania's Council Implementing Decision (EU) 2023/1553) matter less than their end dates suggest.

### From 1 January 2027 — Article 2

Clarifications for OSS/IOSS users and the deemed-supplier rule for imported goods (Art 14a). Not e-invoicing.

### From 1 July 2028 — Article 3

Platform economy (deemed supplier for short-term accommodation and passenger road transport — Member States may defer this specific point to 1 January 2030, Art 6(3)) and single VAT registration.

### From 1 July 2029 — Article 4

Deletion of Art 243(3) and Art 262(2).

### From 1 July 2030 — Article 5, the substantive e-invoicing reform

- **Art 217 replaced**: "'electronic invoice' means an invoice that contains the information required by this Directive, and which, at least in relation to the data referred to in Articles 262 and 271b, has been issued, transmitted and received in a structured electronic format which allows for its automated and electronic processing."
- **Art 218 replaced**:
  - 218(2): "For the purposes of this Directive, invoices shall be issued as electronic invoices. However, Member States may accept documents or messages on paper or in electronic formats other than electronic invoices for transactions not subject to the reporting obligations laid down in Chapter 6." — structured e-invoicing becomes the default.
  - 218(3): "Electronic invoices shall comply with the European standard on electronic invoicing and the list of its syntaxes pursuant to Directive 2014/55/EU… Member States may allow the use of other standards for electronic invoices relating to supplies of goods and services within their territory, other than those referred to in Article 262." — EN 16931 is mandatory for cross-border; national formats survive only domestically.
- **Art 222 first paragraph replaced**: for supplies under Art 138 (intra-Community supplies of goods) and for supplies where VAT is payable by the customer under Arts 194–197, "an invoice shall be issued no later than **10 days following the chargeable event**". Same 10 days from receipt of a payment on account.
- **Art 223 replaced**: summary invoices remain permitted where VAT on all the listed supplies becomes chargeable in the same calendar month; for Art 222 transactions the summary invoice must be issued no later than 10 days after the end of that month. Member States may exclude summary invoices in fraud-sensitive sectors.
- **Art 226 amended**: point (11a) now requires the mention "Reverse charge" and, for Art 197 supplies, additionally "triangular transaction". Two new mandatory points: **(16)** for a corrective invoice under Art 219, the sequential number of the corrected invoice; **(17)** the bank account numbers or virtual account numbers of the supplier, or other identifiers unambiguously identifying the accounts into which the invoice can be paid.
- **Art 232 replaced**: an e-invoice complying with the European standard "shall not be subject to acceptance by the recipient" when issued to a taxable person or non-taxable legal person. Other standards and other electronic formats remain subject to acceptance, unless the Member State has used the Art 218(3) option.
- **Art 271a / 271b — Digital Reporting Requirements.** Data is transmitted per individual transaction **at the time the invoice is issued or should have been issued**; where the acquirer self-bills, no later than **5 days** after issue; buyer-side reporting, where a Member State requires it, no later than **5 days** after the invoice is received. Recapitulative statements under Art 262 are replaced by this transaction-level reporting.
- **Art 168** may be conditioned by Member States on the customer holding a compliant e-invoice — input VAT deduction can be made to depend on the structured document.

### 1 January 2035 — the convergence deadline

Art 6(5) second subparagraph: Member States that on 1 January 2024 already had a domestic digital real-time transaction-based reporting obligation, or an Art 395 authorisation for one, or national legislation adopted before that date providing for one, must apply the new Art 218 and Arts 271a/271b rules **by 1 January 2035** as regards domestic e-invoicing and reporting. This is the clause that lets Italy (SdI), Hungary (RTIR), Spain (SII) and others keep their national systems for another decade.

### Transposition deadlines (Art 6)

| Article of ViDA | Publish national law by | Apply from |
|---|---|---|
| Art 1 (domestic mandate freedom) | — (optional) | 14 April 2025 |
| Art 2 | 31 December 2026 | 1 January 2027 |
| Art 3 | 30 June 2028 | 1 July 2028 (Art 3 point (1): between 1 July 2028 and 1 January 2030) |
| Art 4 | 30 June 2029 | 1 July 2029 |
| Art 5 (e-invoicing + DRR) | 30 June 2030 | 1 July 2030; 1 January 2035 for pre-existing domestic systems |

## What this means for a build

- Do not design around buyer acceptance. Design around "the target country's channel accepts this document".
- Do not treat 2030 as far away for cross-border B2B: the EN 16931 requirement in Art 218(3) means any national format you build now for cross-border invoicing has a hard end date.
- Art 226 points (16) and (17) mean your data model needs a *corrected invoice number* field and a *payment account identifier* field before 2030. Both already exist in EN 16931 (BT-25 preceding invoice reference, BT-84 payment account identifier) — the change is that they become mandatory, not that they are new.

## Checkpoints

- [ ] Any claim that "the customer must consent to e-invoices" checked against Art 232 as amended and the target country's mandate
- [ ] Any claim that Directive 2014/55/EU forces issuing removed
- [ ] Cross-border B2B roadmap accounts for Art 218(3) from 1 July 2030
- [ ] Data model carries BT-25 (preceding invoice reference) and BT-84 (payment account identifier)
- [ ] Intra-Community supplies issue within 10 days of the chargeable event (Art 222 from 2030)
- [ ] Any national format relied on for cross-border traffic has a migration plan to EN 16931
