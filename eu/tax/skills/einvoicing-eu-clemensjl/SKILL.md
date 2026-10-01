---
name: einvoicing-eu-clemensjl
title: Structured e-invoicing in Europe
description: Use when building, sending, receiving or validating structured electronic invoices in Europe — EN 16931, UBL 2.1, UN/CEFACT CII, Peppol BIS Billing, Factur-X/ZUGFeRD, XRechnung, FatturaPA, KSeF, RO e-Factura, myDATA — or when asked whether an invoicing feature satisfies a national e-invoicing mandate. Also use when a PDF is about to be described as an e-invoice, when a product starts invoicing into a second EU country, when a validator or a tax platform rejects an invoice, when a credit note or cancellation has to be modelled, and before wiring up any invoice transmission channel.
author: clemensjl
author_url: https://github.com/clemensjl/claude-skills/tree/main/skills/einvoicing-eu
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: tax
language: en
sources:
- title: Checklist
  path: references/checklist.md
- title: Countries Mandates
  path: references/countries-mandates.md
- title: Countries Other
  path: references/countries-other.md
- title: Country Matrix
  path: references/country-matrix.md
- title: En16931
  path: references/en16931.md
- title: Eu Law
  path: references/eu-law.md
- title: Identifiers
  path: references/identifiers.md
- title: Implementation
  path: references/implementation.md
- title: Intake
  path: references/intake.md
- title: Lifecycle
  path: references/lifecycle.md
- title: Peppol
  path: references/peppol.md
- title: Syntax Examples
  path: references/syntax-examples.md
- title: Validation Errors
  path: references/validation-errors.md
- title: Vat Content
  path: references/vat-content.md
---

# Structured e-invoicing in Europe

Building, sending and receiving machine-processable invoices under EN 16931, Directive 2014/55/EU, the VAT Directive 2006/112/EC as amended by Council Directive (EU) 2025/516 (ViDA), and the national mandates layered on top. Written for a developer who has to make invoicing work inside a product, not for an accountant. Status as at 2026-08-05.

**Core principle:** an e-invoice is not a PDF. Under Art 2(1) of Directive 2014/55/EU and Art 217 of Directive 2006/112/EC as replaced by ViDA, an electronic invoice is a dataset "issued, transmitted and received in a structured electronic format which allows for its automated and electronic processing". An emailed PDF is not one, and under § 14 Abs 1 Satz 4 UStG it is expressly a *sonstige Rechnung*. The correct mental model has four independent layers: **one semantic core** (EN 16931 business terms BT-/BG-), **two permitted syntaxes** (UBL 2.1, UN/CEFACT CII D16B), **many national CIUS and extensions** (XRechnung, Peppol BIS Billing, RO_CIUS, Factur-X profiles), and **separate transmission channels** (Peppol AS4, SdI, KSeF, French *plateformes agréées*, SPV). Getting the syntax right and the CIUS wrong is the standard failure: the file is well-formed UBL, passes the XSD, and is rejected by the receiving country.

## Not tax or legal advice

This skill produces implementation artefacts and findings, not advice on a taxpayer's obligations.

- Whether a specific entity is inside a mandate, from which date, and at which turnover threshold is a question for a tax adviser in that country. The skill maps the rule; it does not classify the business.
- Anything that goes into production and carries VAT figures — invoice content, exemption wording, retention, correction procedure — gets signed off by the tax adviser responsible for the entity before the first live invoice.
- Every generated invoice template, mapping table or country statement carries `<!-- ENTWURF – steuerlich nicht freigegeben -->` until that sign-off is confirmed. Never remove the marker silently.
- The mandatory published legal texts of a website (Impressum, privacy notice, terms) are out of scope — those belong to the `legal-*` skills. The boundary: this skill covers the invoice document and its transport, not what the shop page says.

Never drop or soften this section in the output.

## Workflow

1. **Intake before any code.** Without the answers in `references/intake.md`, every format and channel decision is a guess. Country of establishment, countries of customers, B2G/B2B/B2C, turnover band and existing ERP decide everything downstream.
2. **Decide the layer stack** using the matrix below: semantic profile → syntax → CIUS/customization ID → channel.
3. **Read the reference file for each layer before producing anything.** The element names, code lists and rule IDs are too specific to recall — a wrong `cbc:` path or a wrong EAS code fails silently at the access point.
4. **Validate before sending.** Schema, then EN 16931 Schematron, then the CIUS Schematron, then the country platform's own test endpoint. `references/validation-errors.md` maps the rule IDs that reject most first attempts.
5. **Run `references/checklist.md`** and report findings with rule ID and fix.

**Output shape.** Exactly four parts, in this order:

1. the artefact — mapping, XML, code, or the finding table — carrying the draft marker
2. the list of `[[MISSING: …]]` values the user must supply
3. adjacent open items in one sentence each (archiving, credit notes, second country, human-readable rendition)
4. the sign-off note

Cite the norm, rule ID or specification version next to the claim it supports. Reference file names are working material and belong in none of the four parts.

## Decision matrix

| Situation | What applies | Reference |
|---|---|---|
| Any structured invoice anywhere in the EU | EN 16931-1:2017 semantic model, BT-/BG- terms, BR- rules | `en16931.md` |
| Choosing between UBL and CII, or writing the XML | CEN/TS 16931-3-2 (UBL 2.1), CEN/TS 16931-3-3 (CII D16B) | `syntax-examples.md` |
| Selling to an EU public authority | Directive 2014/55/EU — the authority must receive, you are not forced to issue | `eu-law.md` |
| Planning for 2028–2035 | ViDA: Council Directive (EU) 2025/516, Reg (EU) 2025/517, Impl Reg (EU) 2025/518 | `eu-law.md` |
| Deciding what fields must appear on the invoice at all | Art 226, 226a, 226b, 229, 233 of Directive 2006/112/EC | `vat-content.md` |
| "Which country needs what" in ten seconds | Per-country lookup table | `country-matrix.md` |
| Italy, France, Germany, Spain, Poland | Full national regime, dates, channel, identifiers | `countries-mandates.md` |
| Belgium, Romania, Hungary, Portugal, Greece, Nordics, NL, CH, UK | Full national regime, dates, channel, identifiers | `countries-other.md` |
| Sending or receiving over the Peppol network | Peppol BIS Billing 3.0.20, AS4, SMP/SML, service providers | `peppol.md` |
| Filling in party, address, routing and code-list fields | EAS, ISO 6523 ICD, GLN, Leitweg-ID, codice destinatario, UNTDID 1001, Rec 20, UNCL5305, VATEX | `identifiers.md` |
| A validator returned a rule ID | Rule ID → cause → fix | `validation-errors.md` |
| Rounding, totals, PDF/A-3 embedding, human-readable rendition, test tooling | Implementation mechanics | `implementation.md` |
| Credit note, correction, cancelling a transmitted invoice, archiving | Post-issuance lifecycle | `lifecycle.md` |

## Hard rules

- **A PDF is not an e-invoice, and neither is a PDF with XML next to it in the same email.** Art 217 of Directive 2006/112/EC as replaced by ViDA and Art 2(1) of Directive 2014/55/EU require a structured format allowing automated processing. Only a hybrid file where the XML is *embedded* in a PDF/A-3 (Factur-X / ZUGFeRD) counts, and then the XML is the invoice — the visual layer is a rendition.
- **The XSD is not the validation.** UBL 2.1 and CII D16B schemas accept files that EN 16931 rejects. Conformance means passing the EN 16931 Schematron (validation artefacts v1.3.16, released 2026-04-13, github.com/ConnectingEurope/eInvoicing-EN16931) *and* the CIUS Schematron of the target country. Never report "valid" on the basis of a schema check.
- **`cbc:CustomizationID` (BT-24) is the contract, not decoration.** `urn:cen.eu:en16931:2017` is plain EN 16931; Peppol BIS Billing 3.0 requires exactly `urn:cen.eu:en16931:2017#compliant#urn:fdc:peppol.eu:2017:poacc:billing:3.0` (docs.peppol.eu). Sending a Peppol invoice with the plain EN 16931 identifier is rejected at the access point. Never guess this string — copy it from the target specification.
- **Two ZUGFeRD/Factur-X profiles are not invoices.** MINIMUM (`urn:factur-x.eu:1p0:minimum`) and BASIC WL (`urn:factur-x.eu:1p0:basicwl`) carry no line data and are not EN 16931 conformant; only BASIC, EN 16931 and EXTENDED are (fnfe-mpe.org, Factur-X 1.09.2 / ZUGFeRD 2.5.2, released 2026-08-04). They are booking aids, not something to send into a mandate.
- **The buyer no longer has to agree.** Art 232 of Directive 2006/112/EC as amended by ViDA (Council Directive (EU) 2025/516, Art 1 point 3) lets a Member State that mandates domestic e-invoicing dispense with recipient acceptance, applicable from **14 April 2025**. Advice that "you need the customer's consent for an e-invoice" is pre-ViDA and wrong wherever a domestic mandate exists.
- **A qualified electronic signature is not required by EU VAT law, anywhere.** Art 229 of Directive 2006/112/EC: "Member States shall not require invoices to be signed." Art 233(1) as replaced by Directive 2010/45/EU lets each taxable person choose *any business controls creating a reliable audit trail*; the advanced signature and EDI in Art 233(2) are examples, not requirements. Portugal's PDF-signature rule is a national procedural rule about non-structured PDFs, not a counter-example to this.
- **The receipt obligation and the issuing obligation are different dates.** Germany: receipt obligatory since 2025-01-01, issuing phased via § 27 Abs 38 UStG to 2027-01-01 and 2028-01-01. France: receipt for all before issuing for most. Never state one mandate date per country.
- **Never invent an identifier, code or threshold.** EAS scheme codes, codice destinatario, Leitweg-ID, KSeF numbers, turnover thresholds and go-live dates are either verified against the authority's own page or written as `[[MISSING: …]]`. A plausible wrong EAS code routes the invoice to nobody and fails silently.
- **The Peppol MD5/CNAME lookup is dead, not deprecated.** Since 2025-11-01 participant resolution uses `strip-trailing(base32(sha256(lowercase(value))),"=")` under a U-NAPTR record with service name `Meta:SMP`; the legacy `B-<md5hex>` CNAME records now return NXDOMAIN (*Peppol CNAME to NAPTR Migration Process* v1.0.0). The SML zone is also moving to `participant.sml.prod.tech.peppol.org` — access points must have switched by 2026-08-31. Any tutorial showing MD5 is describing a broken client.
- **Cancelling a transmitted invoice is usually impossible.** Once SdI, KSeF or SPV has accepted the document, the correction is a new document (Italy TD04 credit note; Poland *faktura korygująca* — the buyer-issued *nota korygująca* was abolished on 2026-02-01). Building a "void invoice" button without a country check produces an unreconcilable ledger.

## False friends

Assumptions that are plausible, widespread in English-language material, and wrong.

| Plausible assumption | Actual position |
|---|---|
| "E-invoicing" means emailing a PDF | Structured format required: Art 2(1) Dir 2014/55/EU, Art 217 Dir 2006/112/EC as replaced by ViDA |
| Directive 2014/55/EU forces every supplier to issue e-invoices | It obliges contracting authorities to **receive and process** (Art 7). Issuing obligations come from national law, not from this directive |
| EN 16931 is a file format | It is a semantic data model. The file formats are UBL 2.1 and CII D16B, listed in the Annex to Commission Implementing Decision (EU) 2017/1870 of 16.10.2017 |
| Peppol is a format | Peppol is a network plus a CIUS. "Peppol BIS Billing 3.0" is the CIUS; AS4 is the transport |
| You join Peppol by registering on a website | You send through a certified Peppol Service Provider. Direct network access requires accreditation, a signed Service Provider Agreement and an OpenPeppol-issued PKI certificate |
| PINT replaces Peppol BIS Billing 3.0 in Europe on a known date | No European migration date is published, and no "BIS Billing 4.0" exists in the identifier registry. PINT is a *template* for national specifications; its base CustomizationID is abstract and never valid in a document |
| A participant listed in the Peppol Directory is reachable | The Directory is an opt-in index and goes stale. Reachability is the SML NAPTR lookup plus the SMP call |
| Hungary mandates e-invoicing | Hungary mandates **reporting** (RTIR / Online Számla). The invoice itself may still be paper; only a data extract goes to NAV |
| ZUGFeRD is German and Factur-X is French, so they differ | Same specification, published jointly by FeRD and FNFE-MPE. Factur-X 1.09.2 = ZUGFeRD 2.5.2, both released 2026-08-04 |
| German invoices must be kept 10 years | **8 years.** § 14b Abs 1 Satz 1 UStG says "acht Jahre"; § 147 Abs 3 AO puts Buchungsbelege at 8. The 10-year figure now covers books and financial statements only |
| There is an EU-wide retention period | Art 247(1) of Directive 2006/112/EC leaves the period to each Member State. Any single number quoted as "the EU period" is wrong |
| France routes B2B invoices through the PPF, and the platforms are called PDP | The PPF was dropped as a free exchange platform in October 2024 — it is now only the *annuaire* and a data concentrator. "PDP" became "**plateforme agréée (PA)**", codified in CGI art. 289 bis by LOI n° 2026-103 du 19 février 2026 |
| Belgium's Hermes converter catches parties who cannot receive | Decommissioned 2025-12-31; the domain no longer resolves |
| Spain's Verifactu starts in 2026, and Verifactu is the B2B e-invoicing mandate | Real Decreto-ley 15/2025 moved it to **2027-01-01** (corporate) and **2027-07-01** (others). Verifactu is a billing-*software* and record-keeping regime; the B2B invoice-exchange mandate is Crea y Crece under RD 238/2026, whose clock has not started |
| One national mandate date per country | Receipt, issuing and reporting have separate dates, and issuing is usually phased by turnover |
| A US or UK invoicing template can be localised with a VAT number field | Art 226 mandatory content plus national additions plus a CIUS is a different data model, not a field |

## Common mistakes

| Mistake | Why it is wrong |
|---|---|
| Validating with the XSD only | EN 16931 conformance lives in Schematron; the XSD passes non-conformant files |
| Summing line amounts at full precision and rounding once at the end | BR-CO-10 and BR-CO-17 compare rounded values; per-line rounding to two decimals is required |
| One `cac:TaxTotal` per invoice with a single rate | BR-CO-18 requires a VAT breakdown group (BG-23) per rate/category combination |
| VAT category `E` (exempt) without an exemption reason | BR-E-10 requires exemption reason code or text; the same applies to AE, G, IC, O |
| Reverse charge without the buyer VAT identifier | BR-AE-02 requires seller and buyer identifiers together |
| Using `9906`/`9907` for Italian parties | Superseded — the current EAS codes are `0211` (Partita IVA) and `0210` (Codice Fiscale) |
| Putting the Leitweg-ID in a party identifier | It is the Buyer reference BT-10 (`cbc:BuyerReference`); EAS `0204` exists but the routing value belongs in BT-10 |
| Treating the codice destinatario as optional for Italian B2C | It is `0000000` for consumers and `XXXXXXX` for foreign counterparties — both mandatory values, not blanks |
| Emitting a negative invoice instead of a credit note | Type code 380 with negative totals fails BR rules; use 381 in a CreditNote document |
| Storing only the PDF rendition | Art 244–247 Dir 2006/112/EC: the invoice that must be stored is the structured original |
| Hard-coding a single country's rules into the invoice service | Each additional country adds a CIUS and a channel, not a config flag |
| Building a direct AS4 connector to "save the access point fee" | Accreditation, PKI and specification-release compliance are the real cost; the fee is not |

## Reference files

- `references/intake.md` — questions to answer before any format or channel decision
- `references/en16931.md` — semantic model, BT-/BG- structure, mandatory vs conditional, validation artefacts
- `references/syntax-examples.md` — worked minimal invoice in UBL 2.1 and in CII D16B with verified element names
- `references/eu-law.md` — Directive 2014/55/EU, Implementing Decision 2017/1870, ViDA package and every date
- `references/vat-content.md` — Art 226/226a/226b/229/233 content rules, reverse charge, intra-Community, small business
- `references/country-matrix.md` — per-country lookup: format, syntax, channel, mandate status, identifier scheme
- `references/countries-mandates.md` — Italy, France, Germany, Spain, Poland in detail
- `references/countries-other.md` — Belgium, Romania, Hungary, Portugal, Greece, Nordics, NL, CH, UK
- `references/peppol.md` — network model, BIS Billing 3.0, identifiers, SMP/SML, connecting via a service provider
- `references/identifiers.md` — EAS, ISO 6523 ICD, national routing IDs, UNTDID 1001, Rec 20, UNCL5305, VATEX
- `references/validation-errors.md` — rule ID → cause → fix for the errors that reject first attempts
- `references/implementation.md` — rounding, totals, PDF/A-3 embedding, renditions, test validators
- `references/lifecycle.md` — credit notes, corrections, cancellation per country, archiving, integrity
- `references/checklist.md` — pre-go-live check with rule and norm references
