# Rechnung — mandatory elements under § 11 UStG

Basis: § 11 UStG 1994, consolidated version as at 2026-08-05 (RIS). A `Rechnung` is any document with which an Unternehmer settles a supply, whatever it is called in commercial usage (§ 11 Abs 2). The elements exist so the recipient can deduct input VAT under § 12 UStG; a defective invoice costs the recipient the deduction, not the issuer the sale.

## When an invoice must be issued

| Situation | Duty | Deadline |
|---|---|---|
| Supply to another Unternehmer for their business, or to a juristische Person that is not an Unternehmer | Mandatory, § 11 Abs 1 Z 1 | within 6 months of the supply |
| Taxable Werklieferung or Werkleistung on a property, to a non-business customer | Mandatory, § 11 Abs 1 Z 1 | within 6 months |
| Supply to a private consumer, otherwise | Optional (right, not duty), § 11 Abs 1 Z 1 | — |
| Service in another member state where the recipient owes the tax under Art 196 MwStSystRL | Mandatory, § 11 Abs 1 Z 2 | by the **15th day of the month following** the month of supply |
| Einfuhr-Versandhandel under § 3 Abs 8a in the § 25b cases | Mandatory, § 11 Abs 1 Z 2a | — |
| Advance payment received before the supply | Rules apply analogously, § 11 Abs 1 Z 4 | final invoice must deduct the invoiced part-payments and their VAT |

## The mandatory element list — § 11 Abs 1 Z 3

| # | Element | Provision |
|---|---|---|
| a | Name and address of the supplying Unternehmer | lit a |
| b | Name and address of the recipient | lit b |
| b+ | **Recipient's UID, if the invoice total exceeds 10 000 €**, the supplier has a domestic Wohnsitz/Sitz, gewöhnlicher Aufenthalt or Betriebsstätte, and the supply is to another Unternehmer for their business | lit b, second sentence |
| c | Quantity and commercially usual description of the goods, or type and extent of the service | lit c |
| d | Date of supply, or the period over which the service extends. For periodically settled supplies the settlement period suffices if it does not exceed one calendar month | lit d |
| e | The Entgelt (net consideration, § 4) and the applicable tax rate; where exempt, a reference to the exemption | lit e |
| f | The tax amount attributable to that Entgelt. Non-EUR invoices must additionally show the tax amount in EUR using a conversion method per § 20 Abs 6, or state the method used | lit f |
| g | Date of issue | lit g |
| h | A sequential number with one or more number series, assigned once to identify the invoice | lit h |
| i | The supplier's own UID, where the supplier makes domestic supplies carrying a right to input VAT deduction | lit i |

`Abs 3`: for the name and address entries any designation suffices that permits unambiguous identification of the parties.

## Reverse charge — § 11 Abs 1a

Where the recipient owes the tax under § 19 Abs 1 second sentence, Abs 1a, 1b, 1c, 1d or 1e:

- the **recipient's UID** must appear, and
- the invoice must **refer to the recipient's tax liability**, and
- the rule on separate tax disclosure does **not** apply — no VAT amount is shown.

For a domestic-rules invoice for a § 3a Abs 6 service where the recipient owes the tax under § 19 Abs 1 second sentence, the issuing deadline is the 15th of the following month.

## Kleinbetragsrechnung — § 11 Abs 6

Applies where the **invoice total does not exceed 400 €**, or the invoice is issued by an Unternehmer using the Kleinunternehmer exemption in § 6 Abs 1 Z 27 (then regardless of amount). Besides the date of issue only these are needed:

1. name and address of the supplying Unternehmer
2. quantity and commercially usual description / type and extent of the service
3. date of supply or the period
4. **Entgelt and tax amount in one sum**
5. the tax rate

Excluded: where Abs 1 requires an invoice for supplies carried out in the rest of the Community, and in the § 19 Abs 1 second sentence and § 19 Abs 1c cases where invoicing follows Austrian rules. There, simplified invoicing is not available.

Note the consequence for software: a Kleinbetragsrechnung shows a **gross figure and a rate**, not a net/VAT split, and carries **no invoice number** and **no recipient**. Many templates add these anyway, which is harmless — but a template that omits the rate is defective.

## What a defective invoice costs

- The **recipient** loses the Vorsteuerabzug under § 12 Abs 1 Z 1 lit a UStG, which requires tax separately shown "in einer Rechnung (§ 11)". A missing mandatory element is the classic reason a deduction is denied on audit.
- The **issuer** who shows a tax amount not owed on the supply **owes it on the strength of the document** until the invoice is corrected towards the recipient (§ 11 Abs 12). On correction, § 16 Abs 1 applies analogously.
- Anyone who shows a tax amount separately without making a supply, or without being an Unternehmer, **owes that amount** (§ 11 Abs 14).

## Copies and retention

§ 11 Abs 2: a copy or duplicate must be made and kept for **seven years**; the same applies to documents referred to in the invoice. § 132 Abs 2 BAO applies to those copies. For electronic invoices, **authenticity of origin, integrity of content and legibility must be assured for seven years**. An electronic invoice counts as an invoice only if the recipient agrees to that form.

## Template — standard invoice (German, as issued)

```text
<!-- ENTWURF – steuerlich nicht freigegeben -->
[[Firma laut Firmenbuch]]
[[Straße Nr.]], [[PLZ Ort]], Österreich
UID-Nummer: [[ATU________]]
Firmenbuchnummer: [[FN ______]], Firmenbuchgericht: [[Landesgericht …]]

RECHNUNG

Rechnungsnummer:   [[2026-000123]]
Rechnungsdatum:    [[TT.MM.JJJJ]]
Leistungsdatum:    [[TT.MM.JJJJ]]        (oder: Leistungszeitraum [[TT.MM.JJJJ – TT.MM.JJJJ]])

Rechnungsempfänger:
[[Name / Firma]]
[[Straße Nr.]]
[[PLZ Ort]], [[Land]]
UID-Nummer: [[ATU________]]        (Pflicht ab Gesamtbetrag über 10.000 €, § 11 Abs 1 Z 3 lit b UStG)

Pos.  Menge  Bezeichnung                 Einzelpreis netto   Betrag netto   USt-Satz
1     [[2]]  [[handelsübliche Bezeichnung]]  [[1.000,00 €]]   [[2.000,00 €]]   20 %
2     [[1]]  [[handelsübliche Bezeichnung]]    [[100,00 €]]     [[100,00 €]]   10 %

Summe netto 20 %                 [[2.000,00 €]]
Umsatzsteuer 20 %                  [[400,00 €]]
Summe netto 10 %                   [[100,00 €]]
Umsatzsteuer 10 %                   [[10,00 €]]
------------------------------------------------
Gesamtbetrag netto               [[2.100,00 €]]
Umsatzsteuer gesamt                [[410,00 €]]
Rechnungsbetrag brutto           [[2.510,00 €]]

Zahlbar bis [[TT.MM.JJJJ]] auf [[IBAN]], [[BIC]], Verwendungszweck [[Rechnungsnummer]].
```

## Template — Kleinbetragsrechnung up to 400 €

```text
<!-- ENTWURF – steuerlich nicht freigegeben -->
[[Firma]], [[Straße Nr.]], [[PLZ Ort]]

Datum: [[TT.MM.JJJJ]]
Leistungsdatum: [[TT.MM.JJJJ]]

[[Menge]] [[handelsübliche Bezeichnung]]

Gesamtbetrag inkl. USt: [[240,00 €]]
Steuersatz: 20 %
```

## Template — reverse charge to an EU business customer

```text
<!-- ENTWURF – steuerlich nicht freigegeben -->
... (alle Angaben nach § 11 Abs 1 Z 3, ohne gesonderten Steuerausweis) ...

UID-Nummer des Leistungsempfängers: [[DE________]]

Steuerschuldnerschaft des Leistungsempfängers (Reverse Charge).
Die Umsatzsteuer wird vom Leistungsempfänger geschuldet.
```

## Checkpoints

- [ ] All eleven elements of § 11 Abs 1 Z 3 present on the standard template
- [ ] Recipient UID field appears and is enforced once the invoice total exceeds 10 000 €
- [ ] Own UID printed whenever the business makes deduction-carrying domestic supplies
- [ ] Supply date or period is a separate field from the issue date
- [ ] Kleinbetragsrechnung path triggers at 400 € gross and shows sum plus rate, not a net/VAT split
- [ ] Kleinbetragsrechnung path is disabled for intra-EU supplies and for reverse-charge invoices under Austrian rules
- [ ] Reverse-charge template shows recipient UID and the liability reference, and no VAT amount
- [ ] Foreign-currency invoices additionally show the tax amount in EUR or the conversion method
- [ ] Six-month issuing deadline enforced; 15th-of-following-month deadline enforced for intra-EU reverse-charge services
- [ ] Invoice copies retained seven years with integrity and legibility assured
- [ ] All `[[…]]` placeholders resolved or reported as open
