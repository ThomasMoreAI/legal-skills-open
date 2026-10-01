# e-Rechnung to Austrian federal bodies

Compact by design. The broader European e-invoicing picture — EN 16931, Peppol BIS Billing, ViDA, national mandates outside Austria — belongs to the sibling `einvoicing-eu` skill. This file covers only what an Austrian supplier must do to bill the Bund.

Status as at 2026-08-05.

## The obligation

Contract partners of federal service providers must submit invoices for goods and services to the Bund **electronically, in a structured format, since 2014-01-01**. The basis is the **IKT-Konsolidierungsgesetz (IKTKonG)**; the duty extends to foreign contractors "nach Maßgabe der technischen Möglichkeit" (erechnung.gv.at, legal information section).

A PDF attached to an e-mail is **not** an e-Rechnung. § 11 Abs 2 UStG defines an electronic invoice as one issued and received in an electronic format, and only counts it as an invoice where authenticity of origin, integrity of content and legibility are assured. The federal portal additionally requires a *structured* format.

The e-Rechnung must contain at least the invoice elements named in **§ 11 Abs 1 UStG** (erechnung.gv.at). The federal channel does not relax any of them — see `rechnung-pflichtangaben.md`.

## Formats

| Format | Versions accepted by the Bund | Note |
|---|---|---|
| **ebInterface** | **4.3, 5.0, 6.0, 6.1** | 6.1 is current and recommended. 4.0, 4.1 and 4.2 have not been supported since April 2022; 3.0 and 3.02 not since January 2016 (erechnung.gv.at, ebInterface section) |
| **UBL** | Peppol BIS Billing profile | used over the Peppol network |

ebInterface is the Austrian XML invoice standard maintained by AUSTRIAPRO with the WKO. **Version 6.1 has been the current release since 2022-08-25** and remains current as at 2026-08-05 (WKO; austriapro/ebinterface-standards releases). It incorporates the requirements of EN 16931-1.

## Channels

| Channel | Use |
|---|---|
| **USP** (Unternehmensserviceportal, usp.gv.at) — upload or web form | single or occasional invoices; the web form produces a compliant document without the supplier generating XML |
| **Peppol network** | system-to-system submission via a Peppol access point |
| Web service / upload to e-Rechnung.gv.at | bulk submission |

Practical consequence for a billing product: emitting ebInterface 6.1 covers the USP path; emitting Peppol BIS Billing UBL covers the Peppol path. Do not build a third, proprietary format.

## What gets an invoice rejected

The federal receiving system validates before the invoice reaches the paying office. The recurring causes of rejection are structural, not tax-substantive:

- **missing order reference.** Federal orders carry an Auftragsreferenz / Bestellnummer that the invoice must quote. An invoice without it cannot be matched and is returned.
- **wrong recipient identification.** The receiving federal body is addressed by its own identifier in the portal, not by a free-text name.
- **schema-invalid XML.** The document must validate against the declared ebInterface or UBL schema version. Emitting 6.1 elements inside a 5.0 declaration fails.
- **PDF instead of structured data.** A PDF may accompany the structured document as a rendered view; it cannot replace it.
- **§ 11 Abs 1 UStG elements present only in the rendered view.** They must be carried in the structured fields, because the structured document is the invoice.

Capture the order reference and the recipient identifier at order intake, not at invoicing time — retrofitting them onto an already-issued invoice means a Storno and a new document, since an issued invoice is never edited (see `implementierung.md`).

## Direction of travel

The EU is moving towards structured e-invoicing and digital reporting as the default for cross-border B2B (ViDA). Austrian domestic B2B e-invoicing between private parties is **not** generally mandatory as at 2026-08-05 — the mandate covers invoicing to the Bund. [[UNVERIFIED: whether an Austrian domestic B2B e-invoicing mandate has since been enacted with a future start date — this was not confirmed against a primary source in this research pass; check the BMF and the ViDA implementation timetable before advising on a roadmap]]

Anything beyond this — EN 16931 semantic model, BT- field identifiers, Peppol identifier schemes, CIUS and extensions, other member states' mandates — is the `einvoicing-eu` skill's territory.

## Checkpoints

- [ ] Every invoice to a federal body is submitted structured, not as a PDF
- [ ] Output format is ebInterface 4.3 / 5.0 / 6.0 / 6.1 or Peppol BIS Billing UBL, nothing proprietary
- [ ] Target version pinned and recorded; ebInterface 6.1 unless a counterparty demands otherwise
- [ ] All § 11 Abs 1 UStG elements carried in the structured document, not only in a rendered view
- [ ] Recipient's Auftragsreferenz / order data captured, since the Bund rejects invoices without them
- [ ] Authenticity, integrity and legibility assured for seven years (§ 11 Abs 2 UStG) — see `aufbewahrung.md`
- [ ] Recipient consent to electronic invoicing documented for non-federal counterparties (§ 11 Abs 2 UStG)
