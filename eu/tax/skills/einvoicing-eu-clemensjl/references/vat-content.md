# VAT content rules on the invoice itself

EN 16931 says what the file may contain. Directive 2006/112/EC says what the invoice must say. The two overlap but do not coincide: a Schematron-valid invoice can still be a defective VAT invoice, and a VAT-correct invoice can fail Schematron. Build against both.

Article text below is the operative wording of Directive 2006/112/EC as amended by Directive 2010/45/EU (applicable from 2013-01-01), with the ViDA changes applying from 2030-07-01 flagged.

## Art 226 — mandatory content of a full invoice

Only the following details are required for VAT purposes:

1. the date of issue
2. a sequential number, based on one or more series, which uniquely identifies the invoice
3. the VAT identification number referred to in Art 214 under which the taxable person supplied the goods or services
4. the customer's VAT identification number under which the customer received a supply in respect of which he is liable for payment of VAT, or received a supply as referred to in Art 138
5. the full name and address of the taxable person and of the customer
6. the quantity and nature of the goods supplied or the extent and nature of the services rendered
7. the date on which the supply was made or completed, or the date of the payment on account, in so far as that date can be determined and differs from the date of issue
8. the taxable amount per rate or exemption, the unit price exclusive of VAT and any discounts or rebates if not included in the unit price
9. the VAT rate applied
10. the VAT amount payable, except where a special arrangement excludes that detail
11. in the case of an exemption or where the customer is liable for payment of VAT, reference to the applicable provision of this Directive, or to the corresponding national provision, or any other reference indicating that the supply is exempt or subject to the reverse charge procedure
   - **(11a)** where the customer is liable for the payment of the VAT, the mention "Reverse charge"; from 2030-07-01 ViDA adds: and for an Art 197 supply of goods, additionally the mention "triangular transaction"
12. new means of transport: the characteristics identified in Art 2(2)(b)
13. travel agents' margin scheme: reference to Art 306 or the national provision
14. second-hand goods, works of art, collectors' items and antiques: reference to Art 313, 326 or 333 or the national provision
15. where the person liable is a tax representative under Art 204: that representative's VAT identification number, full name and address

**Added by ViDA from 2030-07-01:**

16. in the case of a corrective invoice as referred to in Art 219, the sequential number which identifies the corrected invoice
17. the bank account numbers or numbers of virtual accounts of the supplier, or any other identifiers which unambiguously identify the accounts into which the recipients can pay the invoice

Points 16 and 17 map to existing EN 16931 terms: BT-25 (Preceding Invoice reference, `cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID`) and BT-84 (Payment account identifier, `cac:PayeeFinancialAccount/cbc:ID`). No new fields — but they become mandatory.

## Art 226a — simplification for non-established suppliers

Where the invoice is issued by a taxable person not established in the Member State where the tax is due (or whose establishment does not intervene under Art 192a), supplying to a customer liable for the VAT, the supplier **may omit points (8), (9) and (10)** and instead state, by reference to the quantity or extent and nature of what was supplied, the taxable amount.

In EN 16931 terms: unit price, rate and VAT amount may be dropped in that specific reverse-charge scenario. Note that the Schematron does not know this — `BR-AE-05` still requires a rate of 0 on the line. Model reverse charge with category `AE` and rate `0`, not by omitting the rate.

## Art 226b — simplified invoices

For simplified invoices under Art 220a and Art 221(1) and (2), Member States shall require at least:

- (a) the date of issue
- (b) identification of the taxable person supplying the goods or services
- (c) identification of the type of goods or services supplied
- (d) the VAT amount payable or the information needed to calculate it
- (e) where the document amends an earlier invoice under Art 219, specific and unambiguous reference to that initial invoice and the specific details being amended

They may not require details other than those in Arts 226, 227 and 230. A simplified invoice is still an invoice — but EN 16931 has no simplified profile, so a structured simplified invoice is a full core invoice with few fields populated, and will still have to satisfy BR-01 to BR-16.

## Art 229 — no signature

"Member States shall not require invoices to be signed."

This is the source rule that kills the perennial claim that a qualified electronic signature is required for e-invoices in the EU. It is not. See Art 233 below.

## Art 233 — authenticity, integrity, legibility

As replaced by Directive 2010/45/EU:

- 233(1): "The authenticity of the origin, the integrity of the content and the legibility of an invoice, whether on paper or in electronic form, shall be ensured from the point in time of issue until the end of the period for storage of the invoice. Each taxable person shall determine the way to ensure the authenticity of the origin, the integrity of the content and the legibility of the invoice. **This may be achieved by any business controls which create a reliable audit trail between an invoice and a supply of goods or services.**"
- 233(2): "Other than by way of the type of business controls described in paragraph 1, **the following are examples** of technologies that ensure the authenticity of the origin and the integrity of the content" — (a) an advanced electronic signature based on a qualified certificate and created by a secure signature creation device; (b) EDI under Commission Recommendation 1994/820/EC.

Signatures and EDI are examples, not requirements. Germany implements this literally in § 14 Abs 3 UStG via the *innerbetriebliches Kontrollverfahren*.

Where a national platform signs documents (Italian SdI, Romanian ANAF), the signature is applied by the authority as part of clearance and is evidence of the platform's acceptance — it is not a supplier obligation arising from Art 233.

## Art 219 — corrective documents

"Any document or message that amends and refers specifically and unambiguously to the initial invoice shall be treated as an invoice." A credit note is an invoice for these purposes and must itself satisfy Art 226 (through Art 226b if simplified).

## Art 222 — issuance deadlines

Current rule: for intra-Community supplies under Art 138 and for supplies where the customer is liable under Arts 194–197, the invoice must be issued no later than the fifteenth day of the month following that in which the chargeable event occurred. **From 2030-07-01 ViDA replaces this with 10 days following the chargeable event** (and 10 days from receipt of a payment on account). This shortens the window from up to 45 days to 10.

## Art 230 — currency

Amounts may be in any currency provided the VAT payable or to be adjusted is expressed in the national currency of the Member State, using the Art 91 conversion mechanism. In EN 16931 this is BT-6 (VAT accounting currency code) plus BT-111 (Invoice total VAT amount in accounting currency) — the one legitimate exception to "one currency per document".

## The wording that must literally appear

| Situation | Required mention | EN 16931 modelling |
|---|---|---|
| Customer liable for VAT | "Reverse charge" (Art 226(11a)) | Category `AE`, rate 0, exemption reason `VATEX-EU-AE` or the literal text |
| Art 197 triangulation, from 2030 | additionally "triangular transaction" | Free text in BT-120 or a note |
| Intra-Community supply of goods (Art 138) | reference to the exemption (Art 226(11)) | Category `K`, rate 0, `VATEX-EU-IC`; buyer VAT identifier mandatory (BR-IC-02); delivery date or period and deliver-to country mandatory (BR-IC-11, BR-IC-12) |
| Export outside the EU | reference to the exemption | Category `G`, rate 0, `VATEX-EU-G` |
| Travel agents' margin scheme | reference to Art 306 | Free text; the standard has no dedicated term |
| Margin scheme, second-hand goods | reference to Art 313 / 326 / 333 | Category `E` with `VATEX-EU-F`, `-I` or `-J` |
| Small business scheme | reference to the national exemption | Category `E` plus the national reason. Austria: *Kleinunternehmerregelung* under § 6 Abs 1 Z 27 UStG. Germany: § 19 UStG. France: `VATEX-FR-FRANCHISE`. The SME scheme itself was reformed EU-wide by Council Directive (EU) 2020/285 applying from 2025-01-01 — check the current national threshold with the tax adviser, never state one from memory |

## National law adds fields

Art 227 lets Member States require the customer's VAT identification number in cases beyond Art 226(4). Art 273 lets them impose further obligations to ensure correct collection. In practice this produces national additions that no EU-level list contains:

- Germany: `Steuernummer` or `USt-IdNr.` of the supplier; construction and building-cleaning services require an explicit reverse-charge note under § 13b UStG
- Italy: `Codice Fiscale`, `Regime Fiscale` code, `Tipo Documento` (TD code), split payment marker
- Portugal: ATCUD and QR code on the printed representation
- Spain: the `VERI*FACTU` legend and QR code where the SIF regime applies
- Poland: KSeF number after acceptance
- France: SIREN of both parties, and the mention *"Autoliquidation"* for domestic reverse charge

None of these are EN 16931 core terms. They arrive via the national CIUS or the national format, which is why `country-matrix.md` exists.

## Checkpoints

- [ ] All 15 (from 2030: 17) Art 226 points either populated or deliberately excluded via Art 226a/226b
- [ ] Sequential number is genuinely sequential and unique per series (Art 226(2))
- [ ] Supply date present whenever it differs from the issue date (Art 226(7))
- [ ] "Reverse charge" appears literally wherever the customer is liable
- [ ] Exemptions carry a reference to the provision, not just a zero rate
- [ ] No claim anywhere that a signature is required (Art 229)
- [ ] Integrity approach documented as a business control with an audit trail (Art 233(1))
- [ ] National additional fields for every target country identified before build, not after rejection
