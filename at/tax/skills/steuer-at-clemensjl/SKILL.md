---
name: steuer-at-clemensjl
title: Steuer und Rechnungsstellung Österreich
description: Use when building or reviewing anything that issues invoices, receipts, or tax records for an Austrian business — invoice generation, receipt printing, cash register or POS integration, VAT rate tables, checkout tax logic, cross-border digital sales, accounting exports — or when asked whether an Austrian invoice or receipt is korrekt. Also use when a German or Swiss invoicing implementation is about to be reused for Austria, when a shop starts selling into another EU state or Switzerland, when a Kleinunternehmer starts or stops charging VAT, and before any billing feature goes live.
author: clemensjl
author_url: https://github.com/clemensjl/claude-skills/tree/main/skills/steuer-at
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: at
practice: tax
language: de
sources:
- title: Aufbewahrung
  path: references/aufbewahrung.md
- title: Beleg 132A
  path: references/beleg-132a.md
- title: Checklist
  path: references/checklist.md
- title: Einkommensseite
  path: references/einkommensseite.md
- title: Entscheidungsmatrix
  path: references/entscheidungsmatrix.md
- title: Erechnung Bund
  path: references/erechnung-bund.md
- title: Implementierung
  path: references/implementierung.md
- title: Intake
  path: references/intake.md
- title: Kleinunternehmer
  path: references/kleinunternehmer.md
- title: Leistungsort Grenzueberschreitend
  path: references/leistungsort-grenzueberschreitend.md
- title: Rechnung Pflichtangaben
  path: references/rechnung-pflichtangaben.md
- title: Registrierkasse
  path: references/registrierkasse.md
- title: Steuersaetze
  path: references/steuersaetze.md
---

# Steuer und Rechnungsstellung Österreich

Tax and invoicing duties as they hit software. The governing texts are UStG 1994 (`Umsatzsteuergesetz`, VAT Act), BAO (`Bundesabgabenordnung`, Federal Fiscal Code), RKSV (`Registrierkassensicherheitsverordnung`, cash register security regulation), BarUV 2015 (`Barumsatzverordnung`, cash-turnover regulation), EStG 1988 and UGB. All statute references verified against RIS, consolidated version as at 2026-08-05.

**Core principle:** Austria has **two separate document duties** that developers conflate. The **Rechnung** under § 11 UStG exists so the *recipient* can deduct input VAT and carries a fixed list of mandatory elements. The **Beleg** under § 132a BAO is a receipt every business must hand to every cash-paying customer regardless of VAT status, amount, or whether an invoice was also issued. On top sits the **Registrierkassenpflicht** under § 131b BAO with a hardware signature device and the RKSV chain — an Austrian construction with no German or Swiss equivalent. A German invoicing implementation ported to Austria is missing the Beleg duty, the QR-code signature, and the Kleinbetragsrechnung threshold, and its VAT rate table is wrong.

## Not tax advice

This skill produces implementation guidance and drafts, not a tax position. Before anything goes live:

- Anything that **determines a tax position** — whether a supply is taxable here, which rate applies to a specific product, whether Kleinunternehmer status still holds, whether an exemption is available — needs a **Steuerberater**. This skill tells you what the machine must be able to do, not what the answer is for a given business.
- Free first contact: WKO tax service (members), BMF Infocenter, FinanzOnline.
- Every generated invoice, receipt, or record template carries a visible `<!-- ENTWURF – steuerlich nicht freigegeben -->` marker until Clemens confirms sign-off. Never remove it silently.

Never drop or soften this section in output.

## Workflow

1. **Collect the facts before writing anything.** Questions in `references/intake.md`. Turnover, cash share, customer type, target countries and product type decide everything below. Unknown values become `[[FEHLT: …]]`, never a guess.
2. **Run the decision matrix** in `references/entscheidungsmatrix.md` to get the obligation set for this business.
3. **Read the reference file for each obligation before producing anything.** Never from memory — the thresholds moved in 2025 and again on 2026-01-01 and 2026-07-01.
4. **Run** `references/checklist.md` against the implementation and report findings with the section number.
5. Output the sign-off note, leave the draft marker in place.

**Output shape.** Exactly four parts, in this order:

1. the artefact (invoice/receipt template, code, or finding table) with the draft marker
2. the list of `[[FEHLT: …]]` items Clemens must supply
3. adjacent open obligations in one sentence each
4. the sign-off note

The section reference goes next to the statement it belongs to. Reference file names are working material and belong in none of the four parts.

## Decision matrix

| Situation | What applies | Reference |
|---|---|---|
| Any supply to another Unternehmer or to a juristische Person | Rechnung mandatory, § 11 Abs 1 Z 1 UStG, within 6 months | `rechnung-pflichtangaben.md` |
| Invoice total over 10 000 € to a business customer | Recipient UID mandatory, § 11 Abs 1 Z 3 lit b UStG | `rechnung-pflichtangaben.md` |
| Invoice total up to 400 € | Kleinbetragsrechnung, § 11 Abs 6 UStG | `rechnung-pflichtangaben.md` |
| Turnover under 55 000 € | Kleinunternehmerregelung, § 6 Abs 1 Z 27 UStG, no VAT on invoices | `kleinunternehmer.md` |
| Selling VAT-exempt into other EU states | EU-Kleinunternehmerregelung, Art 6a UStG, `-EX` identifier | `kleinunternehmer.md` |
| Any priced product | Rate table incl. the 4,9 % rate live since 2026-07-01 | `steuersaetze.md` |
| B2B supply to another EU state | Reverse charge § 19, ZM under Art 21 Abs 3 UStG | `leistungsort-grenzueberschreitend.md` |
| B2C digital services or distance sales into the EU | 10 000 € pan-EU threshold, then EU-OSS | `leistungsort-grenzueberschreitend.md` |
| Goods imported from outside the EU, ≤ 150 € per consignment | IOSS, § 25b UStG | `leistungsort-grenzueberschreitend.md` |
| Cash accepted (incl. card) and turnover over the thresholds | Registrierkassenpflicht § 131b BAO plus full RKSV | `registrierkasse.md` |
| Any cash payment received | Belegerteilungspflicht § 132a BAO — always, no threshold | `beleg-132a.md` |
| Invoicing a federal body | e-Rechnung via USP or PEPPOL, ebInterface or UBL | `erechnung-bund.md` |
| Storing invoices, receipts, DEP | 7-year retention § 132 BAO, readable and exportable | `aufbewahrung.md` |
| Building for small Austrian businesses generally | EAR vs Bilanzierung, Pauschalierung, SVS — orientation only | `einkommensseite.md` |
| Writing the actual code | Rounding, formatting, numbering, Storno, PDF, payload | `implementierung.md` |

## Hard rules

- **Rechnung and Beleg are different documents under different statutes.** § 11 UStG governs the invoice and exists for the recipient's Vorsteuerabzug; § 132a BAO governs the receipt and exists so the transaction is recorded. A system that issues invoices but no receipt on cash payment breaches § 132a BAO even if every invoice is perfect.
- **Card payment is a Barumsatz.** § 131b Abs 1 Z 3 and § 132a Abs 1 BAO both classify payment by Bankomat- or Kreditkarte, comparable electronic payment forms, Barschecks and vendor-issued vouchers accepted in lieu of money as cash. A card-only shop with a physical till is not outside the cash register rules.
- **The Kleinunternehmer threshold is 55 000 €, and it is an actual turnover figure.** § 6 Abs 1 Z 27 UStG, in force since 2025-01-01. The last sentence of the provision says explicitly that the calculation does not use the base of assessment under assumed tax liability — so the old net-conversion arithmetic is gone. Exceeding it by up to 10 % keeps the exemption to the end of the calendar year; beyond 10 % it ends at that moment.
- **Kleinbetragsrechnung is 400 € gross, not 250 € and not 150 €.** § 11 Abs 6 UStG. The same simplification applies to any invoice from a Kleinunternehmer regardless of amount, and is excluded for intra-EU supplies and for reverse-charge cases billed under Austrian rules.
- **The recipient UID threshold is 10 000 € gross.** § 11 Abs 1 Z 3 lit b UStG. Below it, name and address of the recipient suffice. This has no German equivalent and is regularly omitted by ported implementations.
- **Austria has four general VAT rates, not three.** 20 % standard (§ 10 Abs 1), 13 % (§ 10 Abs 3), 10 % (§ 10 Abs 2), and 4,9 % on the basic foodstuffs in Anlage 3 (§ 10 Abs 1a, BGBl. I Nr. 37/2026, in force since 2026-07-01), plus the territorial 19 % for Jungholz and Mittelberg (§ 10 Abs 4). A rate table without 4,9 % is out of date.
- **An issued invoice is never edited.** § 11 Abs 12 UStG: VAT shown that is not owed is owed on the strength of the document until the invoice is corrected towards the recipient. § 11 Abs 14: anyone who shows VAT without making a supply owes it. Corrections are separate documents with their own number, referencing the original.
- **Invoice numbers must be sequential and uniquely identifying.** § 11 Abs 1 Z 3 lit h UStG requires "eine fortlaufende Nummer mit einer oder mehreren Zahlenreihen, die zur Identifizierung der Rechnung einmalig vergeben wird". Generate it inside the same transaction that persists the invoice, never from a client-side counter.
- **Seven years, from the end of the calendar year.** § 132 Abs 1 BAO for books, records and belegs; § 11 Abs 2 UStG for invoice copies, including authenticity, integrity and legibility of electronic invoices for the full seven years.
- **Never invent a UID, a rate, a threshold, or a Kassenidentifikationsnummer.** Missing values become `[[FEHLT: …]]` in the artefact and in the report.

## False friends

Assumptions carried over from Germany or Switzerland. None of these is the Austrian position.

| Plausible wrong assumption | Actual position in Austria |
|---|---|
| Kleinbetragsrechnung up to 250 € (§ 33 UStDV, Germany) | 400 € gross, § 11 Abs 6 UStG |
| No receipt duty beyond the invoice | § 132a BAO: a Beleg for every cash payment, to every customer, no threshold, and the customer must take it out of the premises (§ 132a Abs 5) |
| TSE / technische Sicherheitseinrichtung as in the German KassenSichV | RKSV: a qualified signature/seal creation unit under eIDAS, a JWS chain, and FinanzOnline registration. Not interchangeable with a German TSE |
| Recipient VAT ID only needed for intra-EU supplies | Also needed on any domestic B2B invoice over 10 000 €, § 11 Abs 1 Z 3 lit b UStG |
| USt-IdNr., § 27a UStG | UID-Nummer, format `ATU` plus eight characters |
| Kleinunternehmer threshold 22 000 € / 25 000 € (Germany) | 55 000 €, § 6 Abs 1 Z 27 UStG |
| Reduced rate is a single 7 % / 2,6 % rate | 13 %, 10 % and 4,9 % coexist with different Anlagen |
| E-books at the standard rate | 10 %, § 10 Abs 2 Z 9 UStG, unless wholly or mainly video or music content or advertising |
| Invoice must be issued "unverzüglich" | Six months after the supply, § 11 Abs 1 Z 1 UStG; 15th of the following month for intra-EU reverse-charge services, § 11 Abs 1 Z 2 |
| Retention 10 years (Germany, § 147 AO) | Seven years, § 132 Abs 1 BAO |
| Switzerland is "almost EU" for VAT | Third country. No ZM, no OSS, no reverse charge under Art 196 MwStSystRL; Swiss import VAT and possibly Swiss VAT registration apply |

## Common mistakes

| Mistake | Why it is wrong |
|---|---|
| One `vat_rate` column with 20 / 10 | Misses 13 % and the 4,9 % rate live since 2026-07-01 |
| Invoice number derived from a timestamp or UUID | Not a `fortlaufende Nummer` under § 11 Abs 1 Z 3 lit h UStG |
| Gaps in the number series "because a draft was discarded" | Series must be explainable end to end; drafts must not consume numbers |
| Editing a sent invoice in place | § 11 Abs 12 UStG; the wrong VAT stays owed until a correction document exists |
| Rounding per line and per invoice inconsistently | Produces a Steuerbetrag that does not match Entgelt × Steuersatz; see `implementierung.md` |
| Kleinunternehmer invoice showing 0 % VAT | Wrong. The invoice shows no VAT and carries the exemption reference, § 11 Abs 6 UStG |
| Receipt without the machine-readable code once a Registrierkasse is in use | § 132a Abs 8 BAO plus § 11 RKSV |
| Startbeleg created but never verified | § 6 Abs 4 RKSV requires the check and the protocolled result |
| DEP kept only in the POS database | § 7 Abs 3 RKSV: quarterly unalterable backup to external media, retained under § 132 BAO |
| Storing only a rendered PDF | § 132 Abs 2 and 3 BAO require complete, ordered, content-identical reproduction and, on demand, export to a data carrier |
| Charging Austrian VAT on all EU B2C sales | Above 10 000 € pan-EU the place of supply moves to the customer's state, Art 3 Abs 5 and Art 3a Abs 5 UStG |

## Reference files

Each carries the statutory basis with dates, the mandatory content, a ready template or working code with `[[PLACEHOLDER]]` slots, and checkpoints.

- `references/intake.md` — intake questionnaire before the first artefact
- `references/entscheidungsmatrix.md` — business type and turnover in, obligation set out
- `references/rechnung-pflichtangaben.md` — § 11 UStG elements, thresholds, deadlines, German invoice template
- `references/kleinunternehmer.md` — § 6 Abs 1 Z 27 UStG, 2025 reform, Art 6a EU scheme, `-EX`, Regelbesteuerung
- `references/steuersaetze.md` — § 10 UStG rates including 4,9 % from 2026-07-01, digital products, e-books
- `references/leistungsort-grenzueberschreitend.md` — reverse charge, ZM, EU-OSS, IOSS, Germany and Switzerland
- `references/registrierkasse.md` — § 131b BAO, RKSV, DEP, signature chain, QR payload, FinanzOnline, Belegcheck
- `references/beleg-132a.md` — § 132a BAO Beleg content, German receipt template
- `references/erechnung-bund.md` — IKTKonG, USP and PEPPOL, ebInterface versions, boundary to `einvoicing-eu`
- `references/aufbewahrung.md` — § 132 BAO retention, electronic form, export duties for a SaaS
- `references/einkommensseite.md` — EAR vs Bilanzierung, Basispauschalierung, SVS, short with a hard pointer out
- `references/implementierung.md` — rounding, formatting, numbering under concurrency, Storno, PDF and payload
- `references/checklist.md` — pre-ship checklist producing findings, not reassurance
