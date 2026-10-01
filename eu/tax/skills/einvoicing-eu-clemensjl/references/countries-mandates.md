# Italy, France, Germany, Spain, Poland

The five regimes that account for most European e-invoicing work. Status as at 2026-08-05. Each moved in the last eighteen months; re-verify dates before a go-live decision.

---

## Italy — FatturaPA via SdI

The oldest full clearance model in the EU and the one every other design is compared against.

| | |
|---|---|
| Format | **FatturaPA**, a national XML. Not UBL, not CII, **not an EN 16931 syntax** |
| Schema | `Schema_VFPR12` v1.2.3; technical specifications **v1.9.1**, published 2026-03-31, usable from **2026-05-15** (replacing v1.9 in force since 2025-04-01) — agenziaentrate.gov.it |
| Channel | **Sistema di Interscambio (SdI)** — web service, SFTP, PEC or portal |
| B2G | Mandatory since June 2014 (central), all public entities from 2015-03-31 |
| B2B and B2C | Mandatory since **2019-01-01** |
| Routing | `CodiceDestinatario`, exactly 7 characters, or a PEC address |
| Corrections | Nota di credito **TD04** under art. 26 DPR 633/1972. An SdI-accepted invoice cannot be cancelled |
| Archiving | *Conservazione a norma*, art. 39 DPR 633/1972 — a regulated process, not a copy. AE provides a free service via *Fatture e Corrispettivi* |

**Codice destinatario values that are not optional:** `0000000` for a consumer or a recipient with no channel — the consumer then retrieves the invoice from their *area riservata* with SPID/CIE/CNS, and the issuer must additionally hand over a copy in analogue or electronic form, which is fully valid for tax purposes. `XXXXXXX` (seven capital X) for foreign counterparties.

**The esterometro is gone.** The separate cross-border transaction report was abolished on **2022-07-01**; cross-border data now flows through SdI itself — outbound invoices addressed to `XXXXXXX`, inbound via self-billing/integration documents. AE Circolare n. 26/E of 2022-07-13 is the reference. Document types named in AE material: **TD18** (intra-EU purchases, reverse charge), **TD22** and **TD23** (VAT-warehouse extraction), **TD04** (credit note).

`[[UNVERIFIED: the complete TD01–TD29 document-type table. Only TD04, TD18, TD22 and TD23 appear verbatim in Agenzia delle Entrate material. Read Allegato A of the v1.9.1 technical specifications before publishing a full table.]]`

Changes in v1.9.1 worth knowing: new check code `00327` (VAT-group fiscal-code consistency); new `AltriDatiGestionali` string `ESENZSPORT`; accreditation now via CSR upload; maximum codici destinatario per accredited channel raised from 100 to 300.

Italy is one of the Member States covered by the ViDA **2035** convergence deadline — SdI and FatturaPA survive until then, and must align with the EU model by 2035-01-01.

---

## France — Factur-X / CII via plateformes agréées

The reform whose architecture changed after it was designed. Get the current model right; almost all English-language material predates October 2024.

| | |
|---|---|
| Formats (*socle*) | **Factur-X** (PDF/A-3 with embedded CII), **UBL 2.1**, **UN/CEFACT CII D16B** — all EN 16931 conformant, per arrêté du 14 décembre 2023 |
| French extension | **EXT-FR-FE**; Factur-X profile **EXTENDED-CTC-FR**, identifier `urn:cen.eu:en16931:2017#conformant#urn.cpro.gouv.fr:1p0:extended-ctc-fr` |
| Channel | **Plateformes agréées (PA)** — private accredited platforms. ~137 immatriculées as at 2026-06-24 (DGFiP observatory); the official list is at impots.gouv.fr |
| PPF | Reduced to two functions: the **annuaire** (central directory of VAT-taxable entities and their receiving platform) and the **concentrateur de données**. It is **not** a free exchange platform |
| B2G | Chorus Pro, separate and unchanged |
| Routing | SIREN / SIRET plus a **code de routage**, resolved via the PPF annuaire. Peppol EAS `0225` = FR:CTC (AIFE), plus `0002` SIRENE, `0009` SIRET, `9957` FR:VAT |

**Terminology changed.** "PDP — plateforme de dématérialisation partenaire" became "**PA — plateforme agréée**". The administration switched wording on 2025-07-30; it was codified in **CGI art. 289 bis** by **LOI n° 2026-103 du 19 février 2026, art. 123** (loi de finances pour 2026), in force 2026-02-21. Code and documentation still saying PDP are describing the same thing under the previous name.

**The dates stand.**

| Date | Obligation |
|---|---|
| **2026-09-01** | **Reception** for all French VAT-taxable businesses, no exception. **Issuing + e-reporting** for grandes entreprises and ETI |
| **2027-09-01** | **Issuing + e-reporting** for PME and TPE/micro |

Size categories per art. 3 décret n° 2022-1299 of 2022-10-07, assessed on the last closed fiscal year: GE ≥ 5 000 employees or > 1.5 bn EUR turnover; ETI 250–4 999 and < 1.5 bn EUR; PME < 250 and ≤ 50 M EUR.

The postponement amendment adopted in commission on 2025-03-24 was **deleted by government amendment on 2025-04-11**, and LOI n° 2026-403 du 26 mai 2026 (simplification) contains nothing on e-invoicing. On 2026-07-11 the minister confirmed entry into force on 1 September and announced a *tolérance*: **no sanctions at start-up for good-faith businesses experiencing difficulty** (presse.economie.gouv.fr).

**e-reporting runs alongside e-invoicing** and is a separate obligation: transaction data (B2C France as daily aggregate; exports, intra-EU supplies, services to foreign clients, intra-EU acquisitions and reverse-charge invoice by invoice) plus payment data for services and VAT on encashment. Frequency depends on the VAT regime — réel normal mensuel: three *décadaires* (20th, 30th, 10th) plus monthly payment data by the 10th; RSI: monthly, 25th–30th; franchise en base: bimonthly, 25th–30th.

**Penalties:** 50 EUR per non-electronic invoice, capped at 15 000 EUR/year; 500 EUR per missing e-reporting transmission, capped at 15 000 EUR/year; 500 EUR then 1 000 EUR per quarter for having no approved platform.

**DGFiP became Peppol Authority for France on 2025-07-08.** In practice the French CTC network is run as a Peppol domain: the PA act as access points, DGFiP sets the Peppol Authority Specific Requirements for French service providers, and taxpayers connect through a PA rather than directly.

Archiving: 6 years fiscal (LPF art. L102 B), 10 years commercial (C. com. art. L123-22) — 10 is the operative floor. **The PA is not required to archive**; the duty stays with the company, in the original format.

`[[UNVERIFIED: an exhaustive official list of French CTC CustomizationID strings. Only two are confirmed in the wild — the EXTENDED-CTC-FR identifier above and urn.cpro.gouv.fr:1p0:einvoicingextract#base. The full set is in the DGFiP dossier de spécifications externes annexes.]]`

---

## Germany — § 14 UStG, XRechnung and ZUGFeRD

The largest market, and the one where the receipt obligation already bites while the issuing obligation does not.

**The statute.** § 14 Abs 1 UStG as amended by the Wachstumschancengesetz, in force since 2025-01-01:

- Satz 3: an *elektronische Rechnung* is "eine Rechnung, die in einem strukturierten elektronischen Format ausgestellt, übermittelt und empfangen wird und eine elektronische Verarbeitung ermöglicht".
- Satz 4: a *sonstige Rechnung* is "eine Rechnung, die in einem anderen elektronischen Format oder auf Papier übermittelt wird". A PDF is a *sonstige Rechnung*.
- Satz 6: the structured format must either comply with the EN 16931 standard under Directive 2014/55/EU (Nr 1) or be an agreed format from which the required information can be correctly and completely extracted into the standard format (Nr 2) — the EDI opening.
- § 14 Abs 3: Echtheit der Herkunft, Unversehrtheit des Inhalts and Lesbarkeit are assured by the taxable person, expressly including by an **innerbetriebliches Kontrollverfahren** creating a reliable audit trail. A qualified electronic signature is **one option**, not a requirement.

**Receipt is already obligatory.** Since **2025-01-01** every domestic entrepreneur must be able to receive an EN 16931 e-invoice from another domestic entrepreneur. There is no transitional rule for receipt. Practically, an email inbox capable of accepting the XML satisfies this.

**Issuing is phased**, via § 27 Abs 38 UStG:

| § 27 Abs 38 | Effect |
|---|---|
| Nr 1 | For supplies until **2026-12-31**: paper, or an electronic format not meeting § 14 Abs 1 Satz 6, **with the recipient's consent** |
| Nr 2 | Extended to **2027-12-31** where the **issuing** entrepreneur's *Gesamtumsatz* (§ 19 Abs 2) in the preceding calendar year was **not more than 800 000 EUR** |
| Nr 3 | EDI under Commission Recommendation 94/820/EG until **2027-12-31**, with the recipient's consent |

So: issuers above the 800 000 EUR threshold must issue structured e-invoices from **2027-01-01**; everyone else from **2028-01-01**. The threshold is measured on the issuer, not the recipient, and on the previous calendar year.

**Formats.**

- **XRechnung** — the German CIUS of EN 16931. Current version **3.0.2**, published 2024-06-20. Still current as at 2026-08-05: the KoSIT Schematron release **2.5.0** of 2026-02-05 is described as "compatible with XRechnung 3.0.2". Supports both UBL and CII.
- **ZUGFeRD** — the hybrid PDF/A-3 format, identical to French Factur-X. Current version **2.5.2 / Factur-X 1.09.2**, released **2026-08-04** by FeRD and FNFE-MPE jointly.
- **Peppol BIS Billing 3.0** is accepted by federal authorities.

**Which ZUGFeRD profiles count.** ZUGFeRD is recognised **from version 2.0.1 upwards, except MINIMUM and BASIC WL**. Those two carry no complete set of VAT-mandatory data in the structured part — BASIC WL has no invoice lines at all — are not EN 16931 conformant, and are attached to the PDF with `/AFRelationship` `Data` rather than `Alternative` precisely because they are not an alternative representation of the invoice. FeRD, the standard's own body, states for both: *"In Deutschland nach UStG als vollständige Rechnung anerkannt: Nein"*, classing them as *eine Buchungshilfe* (ferd-net.de ZUGFeRD FAQ). BASIC, EN 16931 (COMFORT) and EXTENDED are conformant.

**BMF guidance.** The Anwendungsschreiben of **2024-10-15**, Aktenzeichen **III C 2 - S 7287-a/23/10001 :007**, and its successor of **2025-10-15**, Aktenzeichen **III C 2 - S 7287-a/00019/007/243**. There is no third letter; the BMF **FAQ** "Fragen und Antworten zur Einführung der obligatorischen E-Rechnung zum 1. Januar 2025" was last updated **2026-03-23**. `[[UNVERIFIED: bundesfinanzministerium.de is bot-walled; both dates and Aktenzeichen are corroborated by four independent secondary sources each, but the BMF text itself was not read]]`

The 2025-10-15 letter distinguishes three error classes with different consequences: **Formatfehler** (breach EN 16931 syntax — the document is then not an E-Rechnung at all), **Verstöße gegen Business Rules** (VAT-relevant only where they touch a UStG requirement), and **inhaltliche Fehler** (a mandatory § 14 / § 14a UStG item missing). It also requires all VAT-mandatory data to sit **in the structured part**, with no external links and no non-embedded attachments, and confirms that for a hybrid invoice **the XML is führend** — a material divergence between XML and PDF risks a second invoice under § 14c UStG.

**Leitweg-ID.** The routing identifier for German public-sector receivers, specified in the KoSIT *Leitweg-ID Format-Spezifikation* v2.0.2 of 2021-07-28. Three parts joined by a hyphen `-` (U+002D): **Grobadressierung** (mandatory, numeric, 2 to 12 digits), **Feinadressierung** (optional, up to 30 characters, A–Z case-insensitive and 0–9), **Prüfziffer** (mandatory, exactly 2 digits). Total length 5 to 46 characters. Grobadressierung is composed of a 2-digit Bundesland or Bund code (01 SH … 16 TH, **99 Bund**), an optional 1-digit Regierungsbezirk or federal Ordnungskennzahl, an optional 2-digit Landkreis, and an optional 3-, 4- or 7-digit Gemeinde element.

The check digit is **ISO/IEC 7064:2003 Modulo 97-10** — the IBAN algorithm. Strip the hyphens, replace each letter by its alphabet position starting at **A = 10 … Z = 35**, append `00`, take mod 97, subtract from 98. The spec's own worked example: Grobadressierung `04011000`, Feinadressierung `1234512345` → `04011000123451234500 mod 97 = 92`, `98 − 92 = 06` → **`04011000-1234512345-06`**. To validate: strip hyphens, translate letters, divide by 97 — remainder **1** means valid. The spec recommends starting the Feinadressierung with a letter, because the hyphen is excluded from the calculation and a misplaced hyphen would otherwise go undetected.

It goes in **BT-10**, `cbc:BuyerReference` / `ram:BuyerReference` — not in a party identifier. It has been in the ISO/IEC 6523 ICD list since 2019-09-30 with value **0204**, so the Peppol receiver identifier for a German authority is `0204:<Leitweg-ID>`. Federal prefixes: **991** unmittelbare Bundesverwaltung, **992/993** mittelbare Bundesverwaltung. Never construct one — it is assigned by the receiving authority.

**Channels — the ZRE is gone.** The Zentrale Rechnungseingangsplattform des Bundes was **switched off and consolidated into the OZG-RE on 2025-09-19** (ref.xrechnung.bund.de, e-rechnung-bund.de). Since then the federal administration receives through **one** platform. OZG-RE offers exactly four channels: **Weberfassung, Upload, E-Mail and Peppol**. Registration is mandatory and free. **Peppol is optional**, not required — the official FAQ presents it as an additional channel for high-volume senders. Germany's Peppol Authority is **KoSIT**.

Legal basis for the federal B2G side is the **ERechV**: § 3 (electronic form binding, with an exception for *Direktaufträge* up to 1 000 EUR net), § 4 (data model — **XRechnung** in its then-current version; other formats only if EN 16931 compliant, which admits the ZUGFeRD XRECHNUNG profile), § 5 (content), § 6 (processing).

**XRechnung 4.0 is announced without a date.** KoSIT/XStandards Einkauf (news of 2026-03-17) expect a release "bis Mitte-Ende 2026", based on **EN 16931-1:2026**, with a preview possible shortly after the EU standard is published but not production-ready. **No valid-from date has been published — do not state one.** There is no 3.1.

**A national B2B Meldesystem is planned but not legislated.** The BMF convened business representatives on 2025-05-07; the stated target is a start "frühestens gleichzeitig mit dem Start des EU-weiten Meldesystems … ab 1. Juli 2030". Any figure of 2028 for the German reporting system is unsupported — the 2027 and 2028 dates that are solid are the *issuing* obligations under § 27 Abs 38 UStG.

**Retention is 8 years, not 10.** § 14b Abs 1 Satz 1 UStG: the entrepreneur must keep a copy of every invoice issued and every invoice received "**acht Jahre**", the period running from the end of the calendar year in which the invoice was issued. § 147 Abs 3 AO matches — Buchungsbelege 8 years, books and financial statements 10, other records 6. A private recipient of property-related services under § 14 Abs 2 Satz 2 Nr 3 keeps the invoice 2 years. § 14b Abs 2 UStG requires domestic storage **unless** the electronic storage guarantees full remote access (Online-Zugriff), download and use, in which case storage elsewhere in the EU is permitted — with notification of the storage location to the Finanzamt.

The transitional rule is **§ 27 Abs 40 UStG**: the 8-year period applies to every invoice whose retention period had **not yet expired on 2024-12-31** — nothing already time-barred is revived. Satz 2 defers the change by one year, to records whose period had not expired on 2026-01-01, for institutions under § 1 Abs 1b KWG (including branches under § 53 KWG), undertakings supervised under § 1 Abs 1 VAG, and Wertpapierinstitute under § 2 Abs 1 WpIG.

`[[MISSING: the current BMF-Schreiben on the E-Rechnung — date and Aktenzeichen of the original (2024-10-15) and of the 2025 follow-up, and whether a 2026 update exists]]`

---

## Spain — two separate regimes, often confused

Spain runs a **software and record-keeping regime** (Verifactu) and an **invoice-exchange mandate** (Crea y Crece) in parallel. They are not the same thing and have different dates.

### Verifactu / SIF

A requirement on the **billing software**, not on the invoice format. The invoice may remain a PDF or paper; it gains a QR code and, in Verifactu mode, a legend.

| Obligation | Date |
|---|---|
| SIF producers: only compliant products may be marketed | **2025-07-29** |
| Taxpayers subject to Impuesto sobre Sociedades | **2027-01-01** |
| All other obligados (autónomos, IRPF) | **2027-07-01** |

The chain of instruments: RD 1007/2023 → RD 254/2025 (which set 2026-01-01 / 2026-07-01) → **Real Decreto-ley 15/2025 de 2 de diciembre** (BOE-A-2025-24446, published 2025-12-03, convalidated 2025-12-11), which moved both dates to 2027. The consolidated BOE text reads *"antes del 1 de enero de 2027"* and *"antes del 1 de julio de 2027"*. Anything citing 2026 is superseded.

Technical requirements (Orden HAC/1177/2024, in force 2024-10-29): a *registro de alta* and a *registro de anulación* per invoice, XML in UTF-8, **hash chaining** — each record embeds the first 64 characters of the previous record's *huella*; a **QR code** (art. 21) encoding the AEAT verification URL plus NIF, series and number, date and total; and, in Verifactu mode only, the **legend** (art. 20) `VERI*FACTU` or *"Factura verificable en la sede electrónica de la AEAT"*. Two modes: Verifactu (records sent to AEAT on issuance, no e-signature needed) or non-Verifactu (records kept locally, signed, with an event log).

Taxpayers under **SII**, and those in the Basque territories and Navarra, are outside Verifactu.

### Crea y Crece B2B mandate

**The reglamento is approved: Real Decreto 238/2026 de 25 de marzo**, BOE núm. 79 of 2026-03-31 (BOE-A-2026-7295), in force 2026-04-20.

- **Formats (art. 7.1): CII, UBL, EDIFACT and Facturae** — all four, per EN 16931. Not Facturae-only. The AEAT public solution uses UBL.
- **Phasing is anchored to a still-unpublished orden ministerial** specifying the *solución pública*: 12 months after its publication for turnover above 8 M EUR, 24 months for everyone else. The orden had **not been published as at 2026-08-05** (draft consulted 2026-04-16 to 2026-05-08), so the practical start is around mid-2027 and mid-2028.
- **Invoice status reporting (art. 10) is mandatory**: commercial acceptance/rejection and full payment, reported within **4 working days**. Firms below 8 M EUR are voluntary for the first 12 months (DT tercera); firms above 8 M EUR must attach a legible PDF for the first 12 months (DT segunda).
- The AEAT public solution is free and voluntary to use, but is a **mandatory repository** — every invoice or a copy lands there.
- Excluded: *facturas simplificadas* unless qualified, electricity and organised gas market operators, IATA clearing houses.

### B2G and the foral regimes

B2G under Ley 25/2013 since 2015-01-15, format **Facturae 3.2.2** (XAdES-signed), entry point **FACe**. Administrations may exclude invoices at or below 5 000 EUR — an option, not a uniform rule. B2G routing needs three mandatory **DIR3** codes: Oficina Contable, Órgano Gestor, Unidad Tramitadora. **FACeB2B** is still operating but RD 238/2026 DT primera gives public-works subcontractors 24 months from the orden to migrate.

**TicketBAI / Batuz** are separate foral regimes and Verifactu does not apply there: Gipuzkoa mandatory from 2022-07-01, Araba from 2022-04-01, **Bizkaia Batuz (TicketBAI + LROE model 240) fully mandatory for all from 2026-01-01**. Navarra has no TicketBAI and its own system is in preparation — `[[UNVERIFIED: no official Navarra date found; vendor citations of "Orden Foral 199E/2025" are a mis-citation]]`.

Peppol EAS for Spain: `9920` (ES:VAT). Spain has no Peppol mandate.

---

## Poland — KSeF

Live and mandatory. The 2024 postponement is history.

| Date | Obligation |
|---|---|
| **2026-02-01** | Issuing mandatory for taxpayers whose **2024** sales including VAT exceeded **PLN 200 m**. **Receiving via KSeF mandatory for all taxpayers** from this date |
| **2026-04-01** | Issuing mandatory for all remaining taxpayers, except those with monthly gross sales at or below **PLN 10 000** |
| **2027-01-01** | The PLN 10 000 exemption expires; transitional reliefs (offline issuing, paper alternatives, cash-register invoices, penalty waiver) also expire at end-2026 |

Legal basis: **Ustawa z 5 sierpnia 2025 r. (Dz.U. 2025 poz. 1203)**, which superseded the 2024 postponement, plus **Rozporządzenie MF z 12 grudnia 2025 r. (Dz.U. 2025 poz. 1815)**. Earlier acts: Dz.U. 2023 poz. 1598, Dz.U. 2024 poz. 852. Source: ksef.podatki.gov.pl.

| | |
|---|---|
| Format | Logical structure **FA(3)**, published 2025-06-25, binding from 2026-02-01, replacing FA(2). Also **FA_RR(1)** for VAT-RR |
| API | **KSeF 2.0**, path `/v2`. Production `https://api.ksef.mf.gov.pl`, plus `api-demo` and `api-test` environments. Quote "API 2.0, `/v2`" rather than a point release — the build string moves |
| Identifiers | Taxpayers by **NIP**. Every accepted invoice receives a system-assigned **numer KSeF**; batches get a *zbiorczy identyfikator* |
| Out of scope | **B2C** — invoices to natural persons not in business do not go through KSeF. Also foreign entities without a Polish seat or fixed establishment, OSS/IOSS, international road passenger transport, the art. 113a SME scheme, toll and ticket invoices, and self-billing without a Polish NIP. B2G invoices sent via PEF receive a KSeF number and count as structured |
| Corrections | Seller-issued **faktura korygująca** through KSeF, referencing the original KSeF number. The buyer-issued **nota korygująca** was **abolished on 2026-02-01**, inside and outside KSeF |

**Special issuing modes** exist for outages and are part of the design, not an edge case: `offline24` (art. 106nda), scheduled-maintenance `offline` (art. 106nh), `awaria` (art. 106nf) and *awaria całkowita*, each with QR-code marking on the document. `[[UNVERIFIED: the post-hoc upload deadline for each mode]]`

`[[UNVERIFIED: the KSeF storage period — 10 years is reported by secondary sources only and does not discharge the taxpayer's own bookkeeping retention]]`

## Checkpoints

- [ ] Correct instrument identified per country: format, syntax, channel, and whether it is clearance, reporting or exchange
- [ ] The date that binds *this* entity established, not the country's earliest date
- [ ] Receipt obligation checked separately from issuing obligation
- [ ] Turnover threshold applied to the correct party and the correct year
- [ ] Routing identifier obtained from the counterparty or the authority, never constructed
- [ ] Correction mechanism implemented per country
- [ ] Every `[[UNVERIFIED]]` and `[[MISSING]]` above resolved before advising on that point
