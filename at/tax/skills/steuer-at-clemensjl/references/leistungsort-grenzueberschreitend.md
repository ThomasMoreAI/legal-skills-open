# Place of supply and cross-border sales

Basis: § 3a, § 19, § 25a, § 25b UStG 1994 and Art 3, Art 3a, Art 21, Art 25a of the Binnenmarktregelung (Anhang zum UStG), consolidated versions as at 2026-08-05 (RIS). Status as at 2026-08-05.

## B2B services — reverse charge under § 19 Abs 1

> "Bei sonstigen Leistungen … und bei Werklieferungen wird die Steuer vom Empfänger der Leistung geschuldet, wenn — der leistende Unternehmer im Inland weder sein Unternehmen betreibt noch eine an der Leistungserbringung beteiligte Betriebsstätte hat und — der Leistungsempfänger Unternehmer im Sinne des § 3a Abs. 5 Z 1 und 2 ist oder eine juristische Person des öffentlichen Rechts ist, die Nichtunternehmer im Sinne des § 3a Abs. 5 Z 3 ist. Der leistende Unternehmer haftet für diese Steuer." — § 19 Abs 1 UStG

Excluded from that shift: paid use of federal roads, the services named in § 3a Abs 11a, and the letting of property.

Invoice consequences (§ 11 Abs 1a UStG):

- state the **recipient's UID**
- **refer to the recipient's tax liability**
- do **not** show a separate tax amount
- issue by the **15th day of the month following** the month of supply (§ 11 Abs 1 Z 2 for supplies in the rest of the Community; § 11 Abs 1a last sentence for domestic-rules cases)
- **simplified invoicing under § 11 Abs 6 is excluded** in these cases

Wording used in practice on the outgoing invoice:

```text
<!-- ENTWURF – steuerlich nicht freigegeben -->
Steuerschuldnerschaft des Leistungsempfängers (Reverse Charge).
Die Umsatzsteuer wird vom Leistungsempfänger geschuldet.
UID-Nummer des Leistungsempfängers: [[XX________]]
```

Domestic reverse-charge cases also exist and are easy to miss when building for a trade: Bauleistungen (§ 19 Abs 1a), secured goods and retention-of-title deliveries (§ 19 Abs 1b), and the further Abs 1c to 1e cases.

**Verify the customer's UID before treating a sale as B2B.** The supplier is liable under § 19 Abs 1 last sentence. Use the confirmation procedure (Stufe 2, via FinanzOnline or the EU VIES service), store the confirmation result with a timestamp, and re-verify for recurring subscriptions.

## Zusammenfassende Meldung — Art 21 Abs 3 UStG

Required for intra-Community supplies of goods, consignment-stock movements under Art 3 Abs 2, and services supplied in the rest of the Community for which the recipient owes the tax under Art 196 of Directive 2006/112/EG.

| Voranmeldungszeitraum | ZM period | Deadline |
|---|---|---|
| calendar month (§ 21 Abs 1) | calendar month | end of the following calendar month |
| calendar quarter (§ 21 Abs 2, prior-year turnover ≤ 100 000 €) | calendar quarter | end of the month following the quarter |

Content (Art 21 Abs 6): the customer's UID issued in another member state, and per customer the sum of the tax bases. Filing the ZM is a **substantive condition** of the intra-Community supply exemption — Art 7 Abs 1 Z 5 makes the exemption dependent on the ZM having been filed, or the omission having been properly justified.

Note the deadline mismatch that trips up schedulers: the **UVA** is due on the 15th of the *second* following month (§ 21 Abs 1), the **ZM** at the end of the *first* following month (Art 21 Abs 3). The ZM is the earlier deadline.

## B2C into the EU — the 10 000 € threshold

Two provisions with the same figure and one combined test:

- **Art 3 Abs 5 UStG** — intra-Community distance sales of goods
- **Art 3a Abs 5 Z 1 UStG** — telecommunications, broadcasting and electronically supplied services to non-business customers

The place of supply stays in Austria while all of the following hold: the supplier operates from one member state and has no establishment outside it; the goods go to / the customer sits in another member state; and the **combined total of both categories did not exceed 10 000 € in the previous calendar year and has not yet in the current one**.

Once the combined total is exceeded, the place of supply moves to the customer's member state for that transaction and everything after it. The supplier may also waive the threshold voluntarily; the waiver **binds for at least two calendar years** (Art 3 Abs 6, Art 3a Abs 5 Z 2).

Implementation consequences:

- track **one** running total across goods distance sales and B2C digital services, not two
- evaluate it **per transaction**; the switch happens mid-order-run
- from the switch, the applicable rate is the **destination country's** rate, so a rate table for one country is not enough
- collect and retain the evidence of customer location required by the EU rules

## EU-OSS and IOSS

| Scheme | Basis | Covers | Threshold |
|---|---|---|---|
| **EU-OSS** (One-Stop-Shop) | Art 25a UStG | intra-Community distance sales and B2C services taxed in other member states | none of its own; used once the 10 000 € threshold is passed or waived |
| **Non-EU scheme** | § 25a UStG | third-country suppliers of services to non-business customers in the Community | — |
| **IOSS** (Import-One-Stop-Shop) | § 25b UStG | distance sales of imported goods where the **intrinsic value per consignment does not exceed 150 €** (§ 3 Abs 3a Z 1, § 3 Abs 8a) | 150 € per consignment |

Electronic interfaces (marketplaces, platforms, portals) that facilitate such supplies are treated as having received and supplied the goods themselves — § 3 Abs 3a Z 1 for imports up to 150 € per consignment, Z 2 for intra-Community supplies by non-established suppliers. A platform product must know whether it is the deemed supplier.

An OSS registration does **not** remove the duty to issue invoices under Austrian rules where § 11 Abs 1 requires one, and does not remove the ZM duty for B2B supplies.

## Selling into Germany

Germany is a member state. Same machinery as above:

- **B2B goods**: intra-Community supply, exempt if the Art 7 conditions are met, recipient UID on the invoice, ZM filed.
- **B2B services**: reverse charge under the German implementation of Art 196; Austrian invoice with recipient UID and the liability reference, issued by the 15th of the following month.
- **B2C**: Austrian VAT until the combined 10 000 € threshold is passed, then German rates (currently 19 % / 7 % — [[UNVERIFIED: German rate values as at 2026-08-05 were not checked against a German primary source in this research pass; verify before shipping a German rate table]]) declared through EU-OSS.
- Do **not** copy German invoice rules back onto the Austrian invoice. The Austrian invoice follows § 11 UStG.

## Selling into Switzerland

Switzerland is a **third country** (§ 1 Abs 3 UStG: Drittlandsgebiet is everything that is not Gemeinschaftsgebiet).

- No ZM. No OSS. No Art 196 reverse charge.
- Outbound goods are an **Ausfuhrlieferung** under § 7 UStG, exempt if the export evidence requirements are met. Keep the export documentation; it is the condition of the exemption, not a formality.
- **§ 11 Abs 1 Z 2 last paragraph** still imposes an invoicing duty where the Austrian business supplies from a domestic establishment to another Unternehmer or to a juristische Person in the third country.
- Swiss import VAT and, above the Swiss registration threshold, **Swiss VAT registration** and possibly a Swiss fiscal representative may apply. That is Swiss law and outside this skill — a Swiss adviser decides it.
- B2C digital services to Swiss consumers are outside the Austrian scope but inside the Swiss scope. Assume nothing.

Boundary: legal texts a Swiss-facing site must publish belong to the `legal-ch` skill, not here.

## Checkpoints

- [ ] Customer UID validated through the confirmation procedure before B2B treatment, with the result stored and timestamped
- [ ] Reverse-charge invoices carry recipient UID plus the liability reference and no VAT amount
- [ ] Kleinbetragsrechnung path disabled for reverse-charge and intra-Community cases
- [ ] Intra-EU reverse-charge services invoiced by the 15th of the following month
- [ ] ZM generated per Voranmeldungszeitraum and due at the end of the *first* following month
- [ ] One combined running total for the 10 000 € threshold across goods and digital services
- [ ] Threshold evaluated per transaction, with the destination rate applied from the breach onwards
- [ ] Threshold waiver, if declared, locked for two calendar years
- [ ] Customer-location evidence collected and retained for B2C digital services
- [ ] IOSS path limited to consignments with intrinsic value up to 150 €
- [ ] Deemed-supplier status decided and documented for any marketplace or platform function
- [ ] Third-country sales carry export evidence, not a reverse-charge note
