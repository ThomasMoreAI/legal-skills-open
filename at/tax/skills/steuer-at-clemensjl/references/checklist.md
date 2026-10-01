# Pre-ship checklist

Run before a billing, receipt or POS feature goes live. Every finding is reported with the section number and the location in the code or the document — not as a general remark. Findings that can be checked mechanically are checked mechanically, never judged from intent.

## Mechanical checks first

These four take minutes and produce most of the findings.

1. **Issue one invoice of each shape** — domestic B2B under 10 000 €, domestic B2B over 10 000 €, Kleinbetragsrechnung at exactly 400,00 € and at 400,01 €, intra-EU reverse charge, Kleinunternehmer — and diff each rendered document against the element list in `rechnung-pflichtangaben.md`.
2. **Grep the codebase and every template** for: `250` and `150` near "Kleinbetrag", `TSE`, `KassenSichV`, `§ 14 UStG` used as an invoice provision, `USt-IdNr`, `Widerruf`, `19 %` and `7 %` in a domestic rate table, `ROUND_HALF_EVEN`, `float` or `double` on a money field, `numeric(3,2)` on a rate column, `SEQUENCE` on an invoice number.
3. **Issue two documents concurrently** (two parallel requests) and check that the numbers are consecutive with no gap and no duplicate, and — where a Registrierkasse is involved — that the two receipts do not share a predecessor in the chain.
4. **Roll back a transaction after number allocation** and confirm no number was consumed.

## Invoice — § 11 UStG

- [ ] All eleven elements of § 11 Abs 1 Z 3 present on the standard template
- [ ] Supplier name and address exactly as registered (lit a)
- [ ] Recipient name and address (lit b)
- [ ] Recipient UID enforced above 10 000 € invoice total for B2B (lit b, second sentence)
- [ ] Quantity and commercially usual description, not an internal SKU alone (lit c)
- [ ] Supply date or period as a field distinct from the issue date (lit d)
- [ ] Entgelt and rate per rate block, and a reference to any exemption (lit e)
- [ ] Tax amount per rate block; EUR amount or conversion method on foreign-currency invoices (lit f)
- [ ] Issue date (lit g)
- [ ] Sequential, uniquely identifying number (lit h)
- [ ] Supplier UID where domestic deduction-carrying supplies are made (lit i)
- [ ] Six-month issuing deadline enforced (§ 11 Abs 1 Z 1)
- [ ] 15th-of-following-month deadline enforced for intra-EU reverse-charge services (§ 11 Abs 1 Z 2, Abs 1a)
- [ ] Advance payments handled: final invoice deducts invoiced part-payments and their tax (§ 11 Abs 1 Z 4)
- [ ] Kleinbetragsrechnung path triggers at 400 € gross, shows sum plus rate, and is disabled for intra-EU and reverse-charge cases (§ 11 Abs 6)
- [ ] Reverse-charge invoices carry recipient UID plus liability reference and **no** VAT amount (§ 11 Abs 1a)
- [ ] Self-billing Gutschrift, if supported, meets all four conditions of § 11 Abs 8 and is labelled as a Gutschrift

## VAT status and rates

- [ ] Kleinunternehmer threshold constant is 55 000 €, on actual turnover (§ 6 Abs 1 Z 27)
- [ ] Running turnover evaluated per transaction, with the 10 % band to 60 500 € handled correctly
- [ ] Kleinunternehmer invoices show no VAT and no 0 % line, and carry the exemption reference
- [ ] Verzicht under § 6 Abs 3 stored with an effective-from date and a five-year lock
- [ ] Rate table holds 20, 13, 10 and **4,9**, keyed by supply date (§ 10 UStG, BGBl. I Nr. 37/2026 from 2026-07-01)
- [ ] Rate precedence Abs 1a → Abs 2 → Abs 3 implemented
- [ ] Electronic publications at 10 % with the video/music/advertising carve-out (§ 10 Abs 2 Z 9)
- [ ] Applied rate persisted on the line item, never recomputed for historic documents
- [ ] Product-to-rate mapping signed off by a Steuerberater, with the date recorded

## Cash register — § 131b BAO and RKSV

- [ ] Thresholds evaluated per Betrieb: 15 000 € turnover **and** 7 500 € Barumsätze
- [ ] Card, contactless and vendor vouchers counted as Barumsatz (§ 131b Abs 1 Z 3)
- [ ] Start date computed as the fourth month after the Voranmeldungszeitraum of first breach
- [ ] Exemption logic uses 45 000 €, not 30 000 € (§ 131 Abs 4 Z 1, in force 2026-01-01)
- [ ] Kassenidentifikationsnummer unique within the undertaking (§ 5 Abs 4 RKSV)
- [ ] Separate certificate and separate DEP per Unternehmer on shared terminals (§ 5 Abs 6 RKSV)
- [ ] Signature payload built in § 9 Abs 2 Z 1–7 order, joined with `_`, prefixed `_RKA_`
- [ ] Five amount buckets present, including `Betrag-Satz-Besonders` (19 %, 4,9 %) per Anlage as amended by BGBl. II Nr. 134/2026
- [ ] `Beleg-Datum-Uhrzeit` ISO 8601 without time zone, Austrian local time
- [ ] Chaining uses the previous receipt's JWS result; Kassen-ID for the first Barumsatz
- [ ] Concurrency lock guarantees correct chaining (Anlage Z 4, Z 11)
- [ ] Trainingsbuchungen excluded from the Umsatzzähler (§ 8 Abs 1)
- [ ] Storno- and Trainingsbelege signed, labelled in the code and on the receipt (§§ 9 Abs 1, 10 Abs 3, 11 Abs 3)
- [ ] Machine-readable code carries items 1–8 with the receipt's own signature value (§ 10 Abs 2)
- [ ] Signature value re-encoded BASE64-URL → standard BASE64 before assembling the code (Anlage Z 12)
- [ ] OCR fallback uses BASE32 in OCR-A where no QR code can be printed (§ 11 Abs 2, Anlage Z 14)
- [ ] Startbeleg created, registered in FinanzOnline within one week, verified, result protocolled and retained (§§ 6, 16)
- [ ] Monatsbeleg at every month end as a signed zero-amount Barumsatz (§ 8 Abs 2)
- [ ] Jahresbeleg printed, checked and retained; check completed by 15 February of the following year (§ 8 Abs 3)
- [ ] Schlussbeleg on planned decommissioning (§ 17 Abs 8)
- [ ] DEP backed up at least quarterly to external media, unalterably (§ 7 Abs 3)
- [ ] DEP export to the Anlage Z 3 JSON structure works on demand, preserving order and chaining (§ 7 Abs 5)
- [ ] Failure path writes `Sicherheitseinrichtung ausgefallen` into the JWS third element and onto the receipt, and produces the Sammelbeleg on recovery (§ 17 Abs 4)
- [ ] Failures and decommissioning reported through FinanzOnline (§ 17 Abs 1, 2, 6)
- [ ] Certificate carries the Ordnungsbegriff and OID `1.2.40.0.10.1.11.1` (§ 15 Abs 2, Anlage Z 16)
- [ ] AES Benutzerschlüssel reported in FinanzOnline and stored securely (§ 16 Abs 1)

## Receipt — § 132a BAO

- [ ] A Beleg is issued on every cash payment, with no amount threshold
- [ ] Electronic receipts available to the payer immediately after payment (§ 132a Abs 1)
- [ ] All five items of § 132a Abs 3 present
- [ ] Receipt number series sequential and identifying the transaction
- [ ] Duplicate created in the same operation and retained (§ 132a Abs 6)
- [ ] The UI does not default to "no receipt" — § 132a Abs 5 obliges the customer to take it
- [ ] Where a Registrierkasse is in use, the § 11 RKSV additions appear on the receipt (§ 132a Abs 8)

## Cross-border

- [ ] Customer UID validated through the confirmation procedure, result stored with a timestamp
- [ ] Recurring subscriptions re-verify the UID
- [ ] ZM generated per Voranmeldungszeitraum, due at the end of the first following month (Art 21 Abs 3)
- [ ] One combined running total for the 10 000 € threshold across goods and digital services (Art 3 Abs 5, Art 3a Abs 5)
- [ ] Threshold evaluated per transaction; destination rate applied from the breach onwards
- [ ] Waiver of the threshold, if declared, locked for two calendar years
- [ ] Customer-location evidence collected for B2C digital services
- [ ] IOSS limited to consignments of intrinsic value up to 150 € (§ 25b, § 3 Abs 8a)
- [ ] Deemed-supplier status decided and documented for platform functions (§ 3 Abs 3a)
- [ ] Third-country sales carry export evidence, not a reverse-charge note
- [ ] No German or Swiss provisions cited anywhere in Austrian documents or code comments

## Records

- [ ] Retention computed from the end of the calendar year, seven years (§ 132 Abs 1)
- [ ] Legal-hold flag blocks deletion regardless of expiry
- [ ] Archive complete, ordered, content-identical, available at any time (§ 132 Abs 2)
- [ ] Export to a data carrier produces a legible, ordered set with a manifest (§ 132 Abs 3)
- [ ] Structured record retained, not only the rendered PDF
- [ ] Hash recorded at issue; storage immutable or object-locked
- [ ] Electronic invoices: authenticity, integrity, legibility evidenced for seven years (§ 11 Abs 2 UStG)
- [ ] Recipient consent to electronic invoicing recorded
- [ ] Tenant data export and deletion behaviour documented contractually

## Implementation hygiene

- [ ] No float or double on any money or rate field
- [ ] `ROUND_HALF_UP` throughout
- [ ] One rounding order applied identically on invoice, receipt and export
- [ ] Gross-priced flows derive tax as `gross − net`
- [ ] Numbers allocated in the persisting transaction from a locked counter row, not a `SEQUENCE`
- [ ] Drafts consume no numbers; no client-side allocation
- [ ] Any gap in a series has a written, retained explanation
- [ ] Issued documents append-only; corrections are separate numbered documents
- [ ] `de-AT` formatting in rendered output; canonical forms in RKSV payload and structured e-invoices
- [ ] PDF rendered from the persisted structured record, fonts embedded

## e-Rechnung to the Bund

- [ ] Structured format, not PDF; ebInterface 4.3/5.0/6.0/6.1 or Peppol BIS Billing UBL
- [ ] All § 11 Abs 1 UStG elements present in the structured document
- [ ] Order reference and recipient data captured

## Sign-off

- [ ] Every `[[FEHLT: …]]` resolved or reported as open
- [ ] Every `[[UNVERIFIED: …]]` in the reference material checked against a primary source before it reaches a shipped figure
- [ ] Draft marker still present on every generated document until tax sign-off is confirmed
- [ ] Named Steuerberater has signed off on the rate mapping, the VAT status and the cash-register classification

## Result format

Report findings as a table, worst first:

| Severity | Location | Provision | Finding | Fix |
|---|---|---|---|---|
| critical / high / medium | file:line or document | § | what is missing or wrong | concrete step |

**Critical** means the recipient loses the Vorsteuerabzug, tax is owed on the strength of a document, a statutory record cannot be produced on audit, or a mandatory device duty is unmet. That covers: a missing mandatory element on a B2B invoice, VAT shown that is not owed, an unexplainable gap in the number series, a broken or unstored signature chain, a missing Beleg on cash payment, a DEP that cannot be exported, and records deleted before seven years.
