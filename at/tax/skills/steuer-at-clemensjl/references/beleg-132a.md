# Beleg — the receipt duty under § 132a BAO

Basis: § 132a BAO, consolidated version as at 2026-08-05 (RIS). This duty is independent of the invoice duty in § 11 UStG and of the Registrierkassenpflicht in § 131b BAO. It exists even where no Registrierkasse is required, where the business is a Kleinunternehmer, and where the amount is one euro.

## Who must issue, and when

> "Unternehmer (§ 2 Abs. 1 UStG 1994) haben unbeschadet anderer gesetzlicher Vorschriften **dem die Barzahlung Leistenden einen Beleg über empfangene Barzahlungen** für Lieferungen und sonstige Leistungen (§ 1 Abs. 1 Z 1 UStG 1994) zu erteilen." — § 132a Abs 1 BAO

- **Every Unternehmer** in the § 2 Abs 1 UStG sense. VAT status is irrelevant.
- **Every cash payment received.** No de minimis threshold.
- "unbeschadet anderer gesetzlicher Vorschriften" — the § 11 UStG invoice does not discharge this duty and this duty does not discharge that one, though one document can satisfy both if it carries both sets of content.

**What counts as Barzahlung** (§ 132a Abs 1, third and fourth sentences): payment by Bankomat- or Kreditkarte or other comparable electronic payment forms; Barschecks; and vouchers, bons or gift tokens issued by the Unternehmer and accepted by them in lieu of money.

**Electronic receipts are allowed**: "Als Beleg gilt auch ein entsprechender elektronischer Beleg, welcher unmittelbar nach erfolgter Zahlung für den Zugriff durch den die Barzahlung Leistenden verfügbar ist." Immediately available for access by the payer — a receipt e-mailed the next morning does not qualify.

In an Organschaft the duty may be discharged by the Organgesellschaft; in a Unternehmereinheit by one of the associated partnerships (§ 132a Abs 2).

## Mandatory content — § 132a Abs 3

1. an **unambiguous designation** of the supplying Unternehmer (or of the person entitled under Abs 2 to issue instead)
2. a **sequential number with one or more number series, assigned once to identify the Geschäftsvorfall**
3. the **date of issue** of the receipt
4. the **quantity and commercially usual description** of the goods, or the type and extent of the services
5. the **amount of the cash payment** — it suffices that the amount is arithmetically derivable from the data on the receipt

Note the differences from § 11 UStG: the Beleg needs **no recipient**, **no VAT split**, and **no tax rate**. But its sequential number identifies the *transaction*, not the *invoice*, and it is a separate series from the invoice numbers unless one document serves both purposes.

§ 132a Abs 4 allows items 1 and 4 to be expressed by symbols or key numbers where their unambiguous determination is assured from the receipt or from other records held by the supplier, and allows the item 4 data to sit in other records held by the supplier or by a business recipient, provided the receipt refers to them.

## The customer's own duty

> "Der Leistungsempfänger oder der an dessen Stelle die Gegenleistung ganz oder teilweise erbringende Dritte hat den Beleg **entgegenzunehmen und bis außerhalb der Geschäftsräumlichkeiten mitzunehmen**." — § 132a Abs 5 BAO

The customer must take the receipt and carry it out of the premises. A UI that offers "no receipt needed" as a default, or that discards the receipt on the customer's behalf, is building around a statutory duty of the customer. Offer the electronic receipt instead.

## Duplicate and retention — § 132a Abs 6

- a carbon copy, or in the same operation another duplicate, must be made and kept
- storage on data carriers counts as a duplicate **if the transactions are captured at the latest simultaneously with the creation of the receipt**
- the retention duty covers the duplicates and the Abs 4 records, **begins with the creation of the receipt, and runs seven years from the end of the calendar year in which the receipt was issued**
- the duplicate is part of the belegs belonging to the books and records

§ 132a Abs 7 waives the number, the date and the duplicate for entitlement documents such as tickets and travel documents where complete capture is assured.

## Extra content once a Registrierkasse is in use

§ 132a Abs 8 BAO: where an electronic cash register or recording system under § 131b is used, the receipt must carry **further data** serving traceability of the individual transaction and identification of the issuing Unternehmer. Those data are set out in § 11 RKSV — Kassenidentifikationsnummer, date and time of issue, amount split by rate, and the content of the machine-readable code. See `registrierkasse.md`.

## Template — Beleg without Registrierkasse (German, as issued)

```text
<!-- ENTWURF – steuerlich nicht freigegeben -->
[[Firma / eindeutige Bezeichnung des Unternehmers]]
[[Straße Nr.]], [[PLZ Ort]]

BELEG

Belegnummer:  [[B-2026-004711]]
Belegdatum:   [[TT.MM.JJJJ]]

[[Menge]]  [[handelsübliche Bezeichnung der Ware / Art und Umfang der Leistung]]

Barzahlungsbetrag: [[24,90 €]]
```

## Template — Beleg with Registrierkasse under the RKSV

```text
<!-- ENTWURF – steuerlich nicht freigegeben -->
[[Firma / eindeutige Bezeichnung des Unternehmers]]
[[Straße Nr.]], [[PLZ Ort]]

Kassenidentifikationsnummer: [[KASSE-01]]
Belegnummer:  [[B-2026-004711]]
Datum/Uhrzeit: [[TT.MM.JJJJ hh:mm:ss]]

[[Menge]]  [[handelsübliche Bezeichnung]]        [[12,45 €]]
[[Menge]]  [[handelsübliche Bezeichnung]]        [[12,45 €]]

Satz Normal 20 %          [[20,75 €]]
Satz Ermäßigt-1 10 %       [[4,15 €]]
Satz Ermäßigt-2 13 %       [[0,00 €]]
Satz Null                  [[0,00 €]]
Satz Besonders             [[0,00 €]]
Summe                     [[24,90 €]]

[ QR-Code mit dem maschinenlesbaren Code nach § 10 Abs 2 RKSV ]
```

For a training or cancellation booking, add the express label:

```text
TRAININGSBUCHUNG          (bzw. STORNOBUCHUNG)
```

## Checkpoints

- [ ] A Beleg is issued on **every** cash payment, including card, contactless and voucher redemption
- [ ] No amount threshold gates the receipt
- [ ] Electronic receipts are available to the payer immediately after payment, not later
- [ ] All five § 132a Abs 3 items present
- [ ] Receipt numbers form a sequential series identifying the transaction, separate from invoice numbers where the documents differ
- [ ] Duplicate created in the same operation and retained seven years from the end of the issue year
- [ ] Where a Registrierkasse is in use, the § 11 RKSV additions are present including the machine-readable code
- [ ] Training and cancellation receipts expressly labelled
- [ ] The UI does not offer or default to "no receipt" — § 132a Abs 5 obliges the customer to take it
- [ ] Exemption under §§ 1 to 6 BarUV, if relied on, documented with the provision and the figures
