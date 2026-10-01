# Intake — facts to establish first

Answer before producing any invoice, receipt, rate table or cash-register logic. Missing answers become `[[FEHLT: …]]` in the artefact and in the report. Never guess a turnover figure, a UID, or a product classification — each one changes the obligation set.

## Legal entity and registration

1. Legal form — Einzelunternehmen, OG, KG, GmbH, FlexKapG, Verein, or a natural person without a business?
2. Exact name or Firma as entered in the Firmenbuch, in that spelling. This is what goes on every invoice under § 11 Abs 1 Z 3 lit a UStG.
3. Geographic address of the place of business.
4. Steuernummer and, if issued, **UID-Nummer** (format `ATU` plus eight characters). Kleinunternehmer usually have none unless they applied for one.
5. Firmenbuchnummer and Firmenbuchgericht, if registered — needed on business letters under § 14 UGB, and invoices count as business letters.
6. Is a Steuerberater engaged? Who signs off on tax positions?

## Turnover and VAT status

7. Turnover (Umsätze nach § 1 Abs 1 Z 1 und 2 UStG) in the previous calendar year, and expected this year. Decides Kleinunternehmer status (55 000 €, § 6 Abs 1 Z 27 UStG) and the Voranmeldungszeitraum (100 000 €, § 21 Abs 2 UStG).
8. Kleinunternehmer, or regular taxation? If Kleinunternehmer: has a **Regelbesteuerungsantrag** under § 6 Abs 3 UStG been filed, and in which year? It binds for at least five calendar years.
9. Is the EU-Kleinunternehmerregelung under Art 6a UStG in use, and for which member states? Has a Kleinunternehmer-Identifikationsnummer with the `-EX` suffix been issued?
10. Ist-Besteuerung (§ 17 UStG, tax on payments received) or Soll-Besteuerung (on invoice)? This changes when the liability arises, not the invoice content.

## Customers and products

11. B2C, B2B, or both? A single system serving both must handle the 10 000 € recipient-UID rule and reverse charge.
12. What is sold — goods, digital contents, digital services, on-site services, subscriptions, mixed baskets?
13. Which VAT rate applies to each product or product group, and on what basis? Anlage 1 (10 %), Anlage 2 (13 %), Anlage 3 (4,9 %), or the standard 20 %. **This classification is a tax position — it needs the Steuerberater, not the model.**
14. Are there VAT-exempt supplies in the catalogue (§ 6 UStG)? Which exemption, and does it exclude input VAT deduction?
15. Do prices in the shop display gross or net? For consumers, gross is required (PrAG, § 5 Abs 2 ECG).

## Cross-border

16. Which countries do customers buy from? Austria only, other EU states, third countries?
17. Total value of intra-EU B2C distance sales and B2C telecom/broadcasting/electronic services in the previous and current calendar year — the 10 000 € pan-EU threshold under Art 3 Abs 5 and Art 3a Abs 5 UStG.
18. Is EU-OSS registered? Is IOSS registered (consignments up to 150 €, § 25b UStG)?
19. Intra-EU B2B supplies of goods or services? Then Zusammenfassende Meldung under Art 21 Abs 3 UStG.
20. Sales into Switzerland or other third countries? Is there a Swiss VAT registration or a fiscal representative?
21. Does the business receive supplies from foreign providers (hosting, SaaS, ads)? Then § 19 Abs 1 second sentence reverse charge applies on the input side.

## Cash and point of sale

22. Are cash payments received at all — including card, contactless, vendor vouchers? § 131b Abs 1 Z 3 BAO treats all of these as Barumsatz.
23. Annual turnover per Betrieb, and Barumsätze per Betrieb. Thresholds: 15 000 € turnover **and** 7 500 € Barumsätze, § 131b Abs 1 Z 2 BAO.
24. Is a Registrierkasse already in operation? Which system, which Kassenidentifikationsnummer, which signature provider (VDA)?
25. Is a signature/seal creation unit procured and registered in FinanzOnline (§§ 15, 16 RKSV)?
26. Does any exemption apply — outdoor/door-to-door turnover up to 45 000 € (§ 131 Abs 4 Z 1 lit a BAO), Hütten, Buschenschank up to 14 days, small association canteen up to 52 days, vending machines up to 20 € per item, online shop without direct cash (§§ 2–6 BarUV 2015)?
27. Are supplies made away from the business premises (mobile service, delivery)? § 7 BarUV 2015 allows delayed entry, but the Beleg must still be handed over immediately.

## Records and systems

28. Where are invoices, receipts and the Datenerfassungsprotokoll stored? For how long? Can they be exported to a data carrier on demand (§ 132 Abs 3 BAO)?
29. Which accounting or ERP system consumes the data, and in which format?
30. Are invoices sent to federal bodies (Bund)? Then e-Rechnung via USP or PEPPOL is mandatory.
31. Who may cancel or correct an issued document, and is that action logged?
32. Is the system multi-tenant? A Registrierkasse shared by several Unternehmer needs a separate certificate and a separate DEP per Unternehmer (§ 5 Abs 6 RKSV).

## Checkpoints

- [ ] Turnover figures for previous and current year obtained, not estimated
- [ ] VAT status (Kleinunternehmer / regular) confirmed in writing
- [ ] UID present or explicitly absent, recorded as `[[FEHLT: UID-Nummer]]` if unknown
- [ ] Rate classification per product group signed off by a Steuerberater
- [ ] Cash-turnover figures separated from total turnover
- [ ] Cross-border thresholds checked against actual figures, not intent
- [ ] Retention location and export path for records identified
- [ ] Named person responsible for tax sign-off recorded
