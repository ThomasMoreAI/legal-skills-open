# Intake

Answer before choosing a format, a syntax or a channel. Unanswered items become `[[MISSING: …]]` in the artefact and in the report — never a guess. A wrong answer here produces a rebuild, not a patch.

## Who is issuing

1. Country of establishment of the issuing entity. If more than one establishment, which one intervenes in the supply (this decides which national mandate applies).
2. Legal form and legal name exactly as registered; commercial register number and register court.
3. VAT identification number, with country prefix. If none: on what basis (small business scheme, non-taxable activity, not yet registered)?
4. National tax number distinct from the VAT identifier, where the country has one (Germany `Steuernummer`, Italy `Codice Fiscale`, France SIREN/SIRET, Spain NIF, Poland NIP).
5. Prior-year turnover band. Almost every mandate phases by turnover — Germany 800 000 EUR, Spain 8 M EUR, Greece 1 M EUR, France by *grande entreprise / ETI / PME / TPE*, Poland PLN 200 m.
6. Is the entity registered for VAT in countries other than its establishment? Where, and with a fiscal representative?

## Who is receiving

7. Countries of the customers, split by volume. This is the list that decides how many CIUS and channels have to be built.
8. B2G, B2B, B2C — for each country. The three have different obligations and often different channels.
9. For B2G: which authorities, and do they publish a routing identifier (Leitweg-ID, DIR3 codes, Chorus Pro service code, iPA code)?
10. Are any customers consumers? B2C is out of scope of most B2B mandates but in scope in Italy and in Greek retail reporting.
11. Do customers already receive on Peppol? Check `directory.peppol.eu` before assuming they do not.
12. Do any customers dictate a format or a portal (large retailers, automotive, public utilities)? A customer portal is a third channel, not a variant of the others.

## What is being invoiced

13. Goods, services, digital services, subscriptions, mixed?
14. VAT treatment per revenue stream: standard rate, reduced rate, exempt with reference, reverse charge, intra-Community supply, export, out of scope, margin scheme.
15. Cross-border intra-EU supplies of goods (Art 138)? These carry the 10-day issuance deadline from 2030 and mandatory BT-80 today.
16. Prepayments, deposits, instalments, construction progress billing? These need specific document type codes.
17. Self-billing (the customer issues in your name)? Type code 389, and reporting deadlines differ under ViDA Art 271b.
18. Multi-currency? Which currency for VAT accounting (BT-6 / BT-111)?
19. Line-level detail available, or only totals? MINIMUM and BASIC WL profiles exist because some senders have no line data — but they are not valid invoices.

## The existing stack

20. What system currently produces the invoice — ERP, billing SaaS, custom code, spreadsheet? Which one owns the invoice number series?
21. Is invoice numbering already sequential and gapless per series (Art 226(2))?
22. Does anything already generate a PDF? Where does its layout come from, and can it be regenerated from structured data?
23. Payment provider and reconciliation flow — does the payment reference already match the invoice number?
24. Where are invoices archived today, in what format, for how long, and who can produce them on request?
25. Is there an existing EDI relationship (EDIFACT INVOIC, X12, a VAN)? Germany's § 27 Abs 38 Nr 3 UStG transitional for EDI ends 2027-12-31.

## Constraints

26. Target go-live date, against the mandate dates in `country-matrix.md`.
27. Build, buy or connect? An access point provider or an invoicing platform is usually cheaper than a direct network connection (`peppol.md`).
28. Who signs off the VAT treatment — internal finance, external tax adviser, both? Name the person; the skill's output is not a substitute.
29. Volume per month, per country. Below a few hundred invoices a month, a provider's UI plus API beats building.
30. Does the product need to *receive* invoices as well as issue them? Receipt obligations often bite earlier than issuing obligations.

## Compliance posture

31. Retention period the business already applies, and on what basis.
32. How is integrity and authenticity currently assured (Art 233(1))? Is the business control documented, or is this the first time anyone has asked?
33. Any existing tax audit findings on invoicing?
34. Is a credit note / correction flow already implemented, and does it create a new document or edit the original? Editing an issued invoice is not acceptable in any European regime.

## Triggers that reopen the intake

Re-run the relevant questions whenever one of these happens. Each of them silently invalidates an earlier decision.

35. A first customer in a country not previously on the list — a new CIUS and possibly a new channel, not a config change.
36. Turnover crossing a mandate threshold in the previous calendar year. Germany's 800 000 EUR test is applied to the issuer's prior-year *Gesamtumsatz*, so the obligation can arrive without anything in the product changing.
37. A new revenue stream with a different VAT treatment — the first reverse-charge or intra-Community sale adds mandatory fields.
38. A specification release: EN 16931 validation artefacts (roughly April and October), Peppol BIS Billing (roughly May and November, each with a mandatory-use date), a national schema version.
39. A change of establishment, a new fixed establishment, or a new foreign VAT registration.
40. Starting to receive invoices as well as issue them, or the counterparty's platform changing.
41. Any national date moving. Several moved in the last eighteen months; treat every stored date as needing re-verification before a go-live.

## Output of the intake

A single table before any code:

| Country | B2G/B2B/B2C | Format + CIUS | Syntax | Channel | Mandate date that binds this entity | Identifier scheme | Sign-off owner |
|---|---|---|---|---|---|---|---|

Every cell either filled from `country-matrix.md` and the country reference files, or marked `[[MISSING: …]]`. A row with a `[[MISSING]]` in the mandate-date column is a row nobody may start building against.

## Checkpoints

- [ ] Every question answered or explicitly marked missing
- [ ] Turnover band established for each mandate that phases by turnover
- [ ] Customer countries listed with volumes, not just "Europe"
- [ ] Peppol reachability of major customers checked in the Peppol Directory
- [ ] Existing invoice number series confirmed sequential and gapless
- [ ] Named human owner for VAT sign-off
- [ ] Receipt obligations checked separately from issuing obligations
