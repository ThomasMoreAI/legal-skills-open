# Pre-go-live checklist

Run before the first live invoice, and again whenever a country, a channel or a specification version changes. Report findings as a table, most severe first, each with the rule identifier or the statutory reference. A finding without a reference is an opinion, not a finding.

## Do these four things first

They produce most of the findings in a few minutes:

1. Take a real invoice from the system, run it through the **EN 16931 Schematron v1.3.16** and then through the **target CIUS Schematron**. Record every fatal and every warning.
2. Search the whole codebase and template set for: `9906`, `9907`, `PCE`, `SET`, `ZZ`, `urn:cen.eu:en16931:2017` (as a hard-coded constant), `PDP`, `esterometro`, `nota korygująca`, `qualified signature`, `10 years`. Each hit is a candidate defect.
3. Compare the totals your ledger reports for one invoice with BT-106, BT-109, BT-110, BT-112 and BT-115 in the generated XML. Any mismatch is a rounding architecture problem, not a display problem.
4. Attempt to send one document through the target platform's **test environment** and read the rejection, not the HTTP status.

## Scope and obligation

- [ ] Establishment country and customer countries listed with volumes (`intake.md`)
- [ ] For each country: B2G / B2B / B2C obligations distinguished
- [ ] **Receipt** obligation and **issuing** obligation dated separately per country
- [ ] Turnover threshold applied to the correct party and the correct reference year (DE 800 000 EUR on the issuer's prior calendar year; ES 8 M EUR; GR 1 M EUR FY2023; PL PLN 200 m on 2024)
- [ ] Phase-in date that binds *this* entity written down, with its legal basis
- [ ] Named human owner for the VAT sign-off, and sign-off obtained

## Semantic model

- [ ] All 16 unconditionally mandatory business terms populated (BR-01 … BR-16, `en16931.md`)
- [ ] BR-CO-26 satisfied: at least one of BT-29 / BT-30 / BT-31
- [ ] BR-CO-25 satisfied: BT-9 or BT-20 whenever BT-115 > 0
- [ ] One BG-23 per (VAT category, rate) combination — BR-CO-18
- [ ] VAT category `K` used for intra-Community supply, not `E`
- [ ] Exemption reason present for every E, AE, K, G and O category (BR-*-10)
- [ ] Reverse charge carries both seller and buyer identifiers (BR-AE-02)
- [ ] Intra-Community supply carries BT-80 and a delivery date or period (BR-IC-11, BR-IC-12)
- [ ] VAT identifiers carry the ISO country prefix; Greece uses `EL` (BR-CO-09)
- [ ] BT-25 (preceding invoice reference) and BT-84 (payment account identifier) present in the data model, for Art 226(16) and (17) from 2030-07-01

## Syntax and profile

- [ ] `cbc:CustomizationID` / `ram:GuidelineSpecifiedDocumentContextParameter/ram:ID` copied verbatim from the target specification, configurable per receiver
- [ ] `cbc:ProfileID` present for Peppol (PEPPOL-EN16931-R001, R007)
- [ ] Element order satisfies the XSD sequence
- [ ] No empty elements emitted (PEPPOL-EN16931-R008)
- [ ] One `cac:TaxTotal` containing all subtotals (PEPPOL-EN16931-R053)
- [ ] All `currencyID` attributes equal BT-5, except BT-111 (PEPPOL-EN16931-R051)
- [ ] Unit codes drawn from the accepted Rec 20 subset only
- [ ] Document type code 380 / 381 unless a national rule requires otherwise
- [ ] Extension profiles used only where the receiving specification names them

## Arithmetic

- [ ] Decimal arithmetic on all monetary values, no binary floats
- [ ] Line amounts rounded to 2 decimals **before** aggregation (BR-CO-10)
- [ ] BT-109 derived from BT-106 ± document allowances and charges (BR-CO-13)
- [ ] BT-110 = Σ BT-117 exactly (BR-CO-14)
- [ ] BT-112 = BT-109 + BT-110 exactly (BR-CO-15)
- [ ] BT-115 = BT-112 − BT-113 + BT-114 exactly (BR-CO-16)
- [ ] Genuine rounding differences expressed in BT-114, not absorbed into BT-115
- [ ] Line net amount matches quantity × (net price / base quantity) ± line charges and allowances (PEPPOL-EN16931-R120)

## Identifiers and routing

- [ ] Every `schemeID` value taken from the EAS code list (`identifiers.md`)
- [ ] No `9906` / `9907` for Italian parties
- [ ] Seller and buyer `cbc:EndpointID` present for Peppol (R010, R020)
- [ ] Leitweg-ID in BT-10, obtained from the German authority, never constructed
- [ ] Codice destinatario exactly 7 characters; `0000000` for consumers, `XXXXXXX` for foreign counterparties
- [ ] Spanish B2G carries all three mandatory DIR3 codes
- [ ] French routing resolved through the PPF annuaire, not hard-coded
- [ ] Counterparty reachability checked in the Peppol Directory before first send

## Channel

- [ ] Channel implemented behind an interface, one adapter per country
- [ ] Sandbox or test environment exercised end to end, including a deliberate rejection
- [ ] Asynchronous rejection handled — no synchronous "sent" state in the UI
- [ ] Platform acknowledgement captured and stored with the document
- [ ] Outage and offline modes handled where the platform defines them (Poland `offline24`, `awaria`)
- [ ] Access point or service provider contract in place, with the correct national Peppol Authority requirements
- [ ] Specification release cadence tracked: EN 16931 artefacts twice a year, Peppol BIS twice a year with a mandatory-use date

## Human-readable rendition and hybrid files

- [ ] Rendition generated from the structured data, not from a parallel code path
- [ ] Rendition shows every Art 226 mandatory item
- [ ] Hybrid PDFs are PDF/A-3, attachment named `factur-x.xml`, `/AFRelationship` `Alternative`, CII inside
- [ ] MINIMUM and BASIC WL profiles not used where an invoice is required
- [ ] PDF/A conformance verified with veraPDF or equivalent

## VAT content

- [ ] All Art 226 mandatory points present or deliberately excluded via Art 226a / 226b
- [ ] Invoice numbers sequential and gapless per series (Art 226(2)); numbers allocated only after validation passes
- [ ] Supply date shown whenever it differs from the issue date (Art 226(7))
- [ ] "Reverse charge" appears literally wherever the customer is liable (Art 226(11a))
- [ ] Exemptions reference the provision, not just a zero rate (Art 226(11))
- [ ] National additional fields covered for every target country
- [ ] No claim anywhere that a signature is required (Art 229)

## Lifecycle

- [ ] No code path edits an issued invoice
- [ ] Credit note (381) and corrected invoice (384) implemented separately, each referencing the original
- [ ] Country-specific correction instrument used (TD04, faktura korygująca, factura rectificativa, avoir, myDATA 5.1/5.2)
- [ ] No buyer-side correction note offered for Poland
- [ ] Corrections travel the same channel as the original

## Archiving and integrity

- [ ] Retention period confirmed per country with the tax adviser; the longest applicable period used
- [ ] Original transmitted bytes archived, not the rendition (Art 247(2))
- [ ] Platform acknowledgement and validation result archived with the document
- [ ] Storage location checked against the country's online-access condition (BE, PT)
- [ ] Legibility over the whole retention period addressed — the XML alone is not legible to an auditor without a renderer
- [ ] Integrity control written down as a business control with an audit trail (Art 233(1))

## Documentation and residual risk

- [ ] Every `[[MISSING: …]]` resolved or escalated with an owner
- [ ] Every `[[UNVERIFIED: …]]` either verified against the authority's own page or excluded from the advice given
- [ ] Specification versions recorded: EN 16931 artefacts, CIUS, Peppol release, national schema
- [ ] Draft marker `<!-- ENTWURF – steuerlich nicht freigegeben -->` still present until sign-off is confirmed

## Result format

| Severity | Location | Rule or norm | Finding | Fix |
|---|---|---|---|---|
| critical / high / medium | file:line, or platform + document | BR-xx / PEPPOL-… / § or Art | what is wrong | the concrete step |

**Critical** means the invoice will be rejected by the platform, the VAT deduction is at risk, or a statutory obligation is unmet: a missing mandate date, an invoice issued on paper after the obligation started, a failed fatal Schematron rule, an unarchived original, an edited issued invoice.
