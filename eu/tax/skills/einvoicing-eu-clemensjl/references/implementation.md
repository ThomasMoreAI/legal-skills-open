# Implementation mechanics

Rounding, totals, hybrid PDFs, renditions and test tooling. The parts that are not in any statute and still decide whether the invoice is accepted.

## Money and rounding

The standard's arithmetic rules are reproduced with their exact tolerances in `validation-errors.md`. The build rule that follows from them:

1. Compute the line net amount (BT-131) at whatever precision your pricing needs, then **round it to 2 decimals before it enters the document**. BR-DEC-* caps every monetary business term at 2 decimals (21 separate rules).
2. Sum the **rounded** line amounts into BT-106. `BR-CO-10` is an exact equality test after `round(sum(...) * 100) div 100` — summing at full precision and rounding once fails.
3. Group lines, document allowances and document charges by (VAT category, rate) to build BG-23. Each group's BT-116 is the sum of the rounded components.
4. Compute BT-117 as `BT-116 × BT-119 / 100` rounded to 2 decimals. `BR-CO-17` and each category's `-09` rule allow a **± 1 currency unit** tolerance here, and only here — it exists to absorb accumulated line-level rounding.
5. BT-110 = Σ BT-117, exactly. BT-112 = BT-109 + BT-110, exactly. BT-115 = BT-112 − BT-113 + BT-114, exactly.
6. If your ledger's total genuinely differs from BT-112 (cash rounding to 0.05, for example), use BT-114 Rounding amount (`cbc:PayableRoundingAmount`). Do not fudge BT-115.

Unit prices (BT-146) are exempt from the 2-decimal cap in the sense that they have their own decimal rules; a price of `0.0125` per unit is legitimate, and `cbc:BaseQuantity` exists so you can express `12.50 per 1000` instead. Peppol rule `PEPPOL-EN16931-R120` recomputes the line net amount as `quantity × (net price / base quantity) + line charges − line allowances`, so the base quantity must be consistent and `PEPPOL-EN16931-R130` requires the same `unitCode` on both.

Use decimal arithmetic, never binary floating point. `0.1 + 0.2` failing an exact equality test is a real cause of `BR-CO-13` failures.

## The human-readable rendition

EN 16931 does not require one. Several national regimes and every real buyer do.

- **Separate PDF alongside the XML**: acceptable in Peppol flows and in Germany. The XML remains the invoice; the PDF is a convenience copy. If they diverge, the XML wins — so generate the PDF *from* the XML, not from a parallel code path.
- **Embedded in the XML**: BG-24 `cac:AdditionalDocumentReference` with `cbc:EmbeddedDocumentBinaryObject` (base64, with `mimeCode` and `filename`). BR-52 requires BT-122 (a document reference identifier). Watch document size — access points and platforms impose limits.
- **Hybrid PDF/A-3**: the Factur-X / ZUGFeRD model, below.

Renderers exist for both syntaxes; do not hand-roll a layout. Whatever you choose, the rendition must show every Art 226 mandatory item, because for a human reader it is the invoice.

## Factur-X / ZUGFeRD: XML inside PDF/A-3

Same specification, two names. Current release **Factur-X 1.09.2 / ZUGFeRD 2.5.2, published 2026-08-04** by FNFE-MPE and FeRD jointly (fnfe-mpe.org, ferd-net.de).

Mechanics, as implemented in the reference library mustangproject (`ZUGFeRDExporterFromA3.java`) and citing the ZUGFeRD 2.1.1 Technical Supplement Part A:

| Aspect | Value |
|---|---|
| Container | PDF/A-3 (the /A-3 conformance level is what permits arbitrary embedded files) |
| Embedded XML syntax | UN/CEFACT CII D16B. Never UBL. |
| Attachment filename | `factur-x.xml` for Factur-X and ZUGFeRD ≥ 2.1; `zugferd-invoice.xml` for ZUGFeRD 2.0; `ZUGFeRD-invoice.xml` for ZUGFeRD 1.0; `xrechnung.xml` when the XRECHNUNG profile is used |
| `/AFRelationship` | `Alternative` — except for the MINIMUM and BASIC WL profiles, where it is `Data` (ZUGFeRD 2.1.1 TA Part A, 2.2.2) |
| XMP extension namespace | `urn:factur-x:pdfa:CrossIndustryDocument:invoice:1p0#`, prefix `fx` |
| MIME type of the attachment | `text/xml` |

**Profiles and their identifiers** (`ram:GuidelineSpecifiedDocumentContextParameter/ram:ID`), as implemented in mustangproject `Profiles.java`:

| Profile | Identifier | EN 16931 conformant |
|---|---|---|
| MINIMUM | `urn:factur-x.eu:1p0:minimum` | **No** |
| BASIC WL | `urn:factur-x.eu:1p0:basicwl` | **No** |
| BASIC | `urn:cen.eu:en16931:2017#compliant#urn:factur-x.eu:1p0:basic` | Yes (CIUS) |
| EN 16931 (COMFORT) | `urn:cen.eu:en16931:2017` | Yes (core) |
| EXTENDED | `urn:cen.eu:en16931:2017#conformant#urn:factur-x.eu:1p0:extended` | Conformant extension |
| EXTENDED-CTC-FR | `urn:cen.eu:en16931:2017#conformant#urn.cpro.gouv.fr:1p0:extended-ctc-fr` | Conformant extension, French CTC |
| XRECHNUNG | `urn:cen.eu:en16931:2017#compliant#urn:xeinkauf.de:kosit:xrechnung_3.0` | Yes (CIUS) |

MINIMUM and BASIC WL carry no invoice line data. They are booking aids. Their `/AFRelationship` of `Data` rather than `Alternative` is the specification saying so explicitly. Do not send them into a mandate.

Practical PDF/A-3 traps: fonts must be embedded and subset; transparency and colour profiles must satisfy PDF/A; the XMP metadata must declare both the PDF/A part and the Factur-X extension schema. Use a library (mustangproject for JVM, `factur-x` for Python, `horstoeko/zugferd` for PHP) rather than hand-assembling with a generic PDF writer — most PDF writers produce files that fail PDF/A validation silently.

## Test and validate

Run in this order. Each stage catches a different class of error.

| Stage | Tool | What it catches |
|---|---|---|
| 1. XSD | UBL 2.1 `UBL-Invoice-2.1.xsd` / CII `CrossIndustryInvoice_100pD16B.xsd` | Element order, namespaces, datatypes |
| 2. EN 16931 Schematron | Validation artefacts v1.3.16 (2026-04-13), source Schematron or the pre-compiled XSLT, both in the release ZIP | BR-*, BR-CO-*, BR-DEC-*, category rules |
| 3. CIUS Schematron | Peppol BIS Billing 3.0 rule set; XRechnung Schematron (KoSIT, `xrechnung-schematron` 2.5.0 of 2026-02-05, compatible with XRechnung 3.0.2); national artefacts | PEPPOL-EN16931-*, DE-R-*, national rules |
| 4. PDF/A-3 | veraPDF or the library's own check | Hybrid-file conformance |
| 5. Platform test endpoint | SdI test channel, KSeF test API, Chorus Pro qualification, the access point's sandbox | Platform-specific codes not expressible in Schematron |

Public validators that were reachable on 2026-08-05:

- **European Commission Interoperability Test Bed** — `https://www.itb.ec.europa.eu/invoice/upload`, validates against EN 16931 and several CIUS
- **KoSIT validator** — `https://github.com/itplr-kosit/validator`, the reference implementation used by German public authorities; run it locally in CI with the XRechnung validation configuration
- **German e-invoice validator (service-bw)** — `https://erechnungsvalidator.service-bw.de/`
- **Peppol / UBL validation (helger)** — `https://peppol.helger.com/public/menuitem-validation-ubl`
- **FNFE-MPE services** — `https://services.fnfe-mpe.org/` for Factur-X
- **ecosio document validator** — `https://ecosio.com/en/peppol-and-xml-document-validator/`

Put stages 1 to 3 in CI against a fixture set. The validation artefacts are released roughly twice a year; pin the version, and treat a version bump as a code change with its own test run.

## Building the invoice service

- Model the **semantic layer once**: an internal object keyed on BT-/BG- numbers. Serialise to UBL or CII from that. Do not maintain two hand-written templates.
- Keep the **CustomizationID as configuration per receiver**, not a constant.
- Keep the **channel behind an interface**. Peppol, SdI, KSeF and a PDP have nothing in common except "send this document and give me back a status".
- Persist the **exact bytes that were transmitted**, plus the platform's acknowledgement. That pair is your evidence under Art 233 and Art 244 (`lifecycle.md`).
- Make invoice numbering **sequential per series and gapless** (Art 226(2)). A number allocated and then discarded because validation failed is a gap you will have to explain. Allocate the number only after validation passes.
- Expect **asynchronous rejection**. SdI, KSeF and access points accept the document and reject it minutes later. A synchronous "invoice sent" UI is wrong.

## Checkpoints

- [ ] Decimal arithmetic throughout, no binary floats on money
- [ ] Line amounts rounded to 2 decimals before aggregation
- [ ] BT-114 used for genuine rounding differences instead of adjusting BT-115
- [ ] Human-readable rendition generated from the structured data, not in parallel
- [ ] Hybrid PDFs use PDF/A-3, `factur-x.xml`, `/AFRelationship Alternative`, CII inside
- [ ] MINIMUM / BASIC WL not used where an invoice is required
- [ ] XSD, EN 16931 Schematron and CIUS Schematron all in CI, version pinned
- [ ] Platform sandbox exercised before the first live invoice
- [ ] Transmitted bytes and platform acknowledgement persisted together
- [ ] Invoice number allocated only after validation succeeds
