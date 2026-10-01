# Belgium, Romania, Hungary, Portugal, Greece, Nordics, Netherlands, Switzerland, UK

Status as at 2026-08-05. For Italy, France, Germany, Spain and Poland see `countries-mandates.md`.

---

## Belgium — Peppol by default

The cleanest design in Europe: EN 16931 over Peppol, no national CIUS, no clearance platform.

**The B2B mandate took effect on schedule on 2026-01-01.** Legal basis: law of 2024-02-06 (numac 2024001635) inserting **art. 53 §2bis CTVA**, with the implementing Royal Decree of 2025-07-08 (numac 2025005169). Source: einvoice.belgium.be.

- Format: a structured invoice conforming to **EN 16931**, in **Peppol BIS Billing 3.0**, over the **Peppol four-corner network by default**. Parties may agree another format and channel provided it complies with EN 16931. **No Belgian CIUS.**
- Grace period, not a postponement: no penalties for offences committed 2026-01-01 to 2026-03-31 where the business acted "in a timely and reasonable manner". Full enforcement since **2026-04-01**.
- Self-billing tolerance runs until **2026-06-30** where the software vendor is actively implementing the functionality.
- **In scope:** all Belgian-established VAT taxable persons, including the small-enterprise franchise (≤ 25 000 EUR) and VAT units, and Belgian fixed establishments of foreign entities.
- **No duty to send:** bankrupt taxpayers, Art 44-only exempt persons, non-established persons without a fixed establishment, and flat-rate (*forfaitaire*) taxpayers until 2028-01-01. **No duty to receive:** Art 44-only exempt, non-established. **B2C is out entirely.**
- **Hermes is dead.** The converter for parties unable to receive structured invoices was decommissioned on 2025-12-31, consultation-only until 2026-03-31, and its domain no longer resolves. Material describing Hermes as a fallback is out of date.
- Routing: **EAS `0208`** (BE:EN), the KBO/BCE enterprise number, required. Lookup as `0208:<BCE>`. `9925` (BE:VAT) still exists in the code list and may be used additionally by agreement but is not the primary Belgian identifier. `0193` (UBL.BE) is deprecated with removal on 2026-07-07. Peppol Authority: **FPS BOSA**.
- B2G: Mercurius, Peppol BIS Billing 3.0, mandatory for all public contracts published from 2024-03-01 — but **contracts at or below 3 000 EUR excluding VAT remain exempt** (RD of 2022-03-09).
- Corrections: a credit note is itself a structured e-invoice in the same format and channel. No void mechanism. Rejection is signalled with the Peppol **Invoice Response** status `RE`. A 2026 credit note against a 2025 unstructured invoice may stay unstructured if the customer agrees.
- Penalties: 1 500 / 3 000 / 5 000 EUR for first, second and subsequent offences (RD of 2025-07-08), enforced from 2026-04-01. General invoicing irregularities remain under art. 70 CTVA (50–5 000 EUR).
- Archiving: **7 years** from 1 January of the year following issue (art. 60 VAT Code); 15 or 25 years for immovable business assets. Must be kept in Belgium **unless** kept electronically with guaranteed full online access from Belgium — cloud hosting abroad is acceptable on that condition.
- Incentives: **120 % increased cost deduction** for sole traders and small companies on recurring e-invoicing costs, taxable periods 2024–2027; capitalised one-off software purchases excluded. Digital investment deduction raised to 20 % from 2025-01-01.

A domestic **e-reporting** phase around **2028** is a coalition-agreement target, Peppol-based (five-corner), intended to replace the annual client listing. The official FAQ still states it "has yet to be transposed into Belgian law" — **no adopted law, no statutory date**. ViDA sets the outer limit of 2030-07-01 for intra-EU digital reporting.

---

## Romania — RO e-Factura

Full clearance, and the widest scope in the EU: B2G, B2B and B2C.

| | |
|---|---|
| Format | **RO_CIUS**, a national CIUS of EN 16931 over **UBL 2.1** (Invoice-2 / CreditNote-2) or UN/CEFACT CII. Validation artefacts version **1.0.8** |
| Channel | **SPV** (Spațiul Privat Virtual) / RO e-Factura API |
| B2G | Mandatory since **2022-07-01** (Legea 139/2022) |
| B2B reporting | 2024-01-01 to 2024-06-30 — transmit all issued invoices regardless of recipient registration (Legea 296/2023, art. LIX) |
| B2B clearance | Mandatory since **2024-07-01** |
| B2C | Mandatory since **2025-01-01** (penalty grace to 2025-03-31) |
| Since 2026-01-01 | Transmission deadline unified at **5 working days** from issue (previously 5 calendar days), via **OUG 89/2025**, Monitorul Oficial nr. 1203 of 2025-12-24. Scope extended to invoices to non-established but Romanian-VAT-registered buyers; individuals identified by **CNP** enter scope |
| Identifiers | **CUI/CIF** for businesses, **CNP** for individuals from 2026 |
| Corrections | Credit note transmitted through RO e-Factura like any other document, same 5-working-day deadline |

**RO e-Transport** is a separate ANAF system monitoring road transport of high-fiscal-risk goods, keyed on a **UIT code**. It is not part of e-Factura, though both feed the pre-filled **RO e-TVA** return alongside SAF-T. `[[UNVERIFIED: e-Transport thresholds, goods list and the 2026-01-01 tightening — Romanian trade press only]]`

The EU derogation was **Council Implementing Decision (EU) 2023/1553 of 2023-07-25**, derogating from Arts 218 and 232 of Directive 2006/112/EC. No extension decision was found and none is needed: ViDA removed the Art 218/232 barrier as of **2025-04-14**.

`[[UNVERIFIED: penalties — reported as RON 5 000–10 000 (large), 2 500–5 000 (medium), 1 000–2 500 (small/individuals) for late transmission and 15 % of invoice value for not issuing through the platform, applying to issuer and recipient. Not confirmed against the OUG text.]]`
`[[UNVERIFIED: retention period. Legea contabilității 82/1991 and OMFP 2634/2015 govern; the archive artefact is the ANAF-signed XML. No primary-source period confirmed.]]`

---

## Hungary — RTIR is reporting, not e-invoicing

**Hungary is routinely listed as a B2B e-invoicing country. It is not.** There is no obligation to *issue* an electronic invoice — B2B, B2C or B2G. The obligation is to *report invoice data* to NAV in XML after the invoice is issued in whatever form. The invoice itself may legally be paper.

The practical difference: no clearance, no state-run exchange of the invoice document, no delivery routing. The buyer receives the invoice through normal channels; NAV receives a data extract.

| | |
|---|---|
| System | RTIR / Online Számla |
| Schema | `invoiceData.xsd` **version 3.0** ("Magyar Online Számla Rendszer invoiceData XML séma, NAV Informatikai Intézet, v3.0 2020/11/23"), interface specification "Online Szamla_Interfesz specifikacio_HU_v3.0". Mandatory since **2021-01-04**; no 3.1 or 4.0 found. Source: github.com/nav-gov-hu/Online-Invoice |
| Scope | Since 2021-01-04, every invoice subject to the Hungarian VAT Act's invoicing rules — including B2C, exports, intra-EU supplies and invoices to foreign VAT payers |
| Deadlines | Software-issued invoices: **immediately and automatically on issue**, without human intervention. Manual or pre-printed invoices: within **4 calendar days**, reduced to the **same calendar day** where passed-on VAT is **HUF 500 000 or more** |
| Identifier | Hungarian tax number. The **first 8 digits** of a domestic taxable customer's tax number must appear on the invoice (mandatory since 2020-07-01) and drive the reporting obligation |
| Corrections | Reported through the same channel: modifying invoices via the correction chain in `invoiceData`, and annulment of an erroneous **submission** via `invoiceAnnulment.xsd`. Annulment corrects a bad data submission; a wrong invoice is fixed by reporting a modifying invoice |
| Retention | `[[UNVERIFIED: 8 years under Section 169 of the Accounting Act — not confirmed against a NAV page]]` |

Hungary is covered by the ViDA **2035** convergence deadline.

---

## Portugal — certified software, ATCUD, QR, SAF-T

**No general B2B e-invoicing mandate.** No clearance platform, no Peppol B2B obligation. Control runs through certified software plus e-Fatura / SAF-T plus ATCUD and QR code.

- **PDF tolerance ends 2026-12-31.** *"até 31 de dezembro de 2026, as faturas em PDF continuam a ser consideradas faturas eletrónicas para todos os efeitos previstos na legislação fiscal"* — **Lei n.º 73-A/2025 de 30 de dezembro** (Orçamento do Estado para 2026). From **2027-01-01** an electronic invoice requires a **qualified electronic signature or qualified electronic seal, or EDI** (art. 12 DL 28/2019). This is a rule about PDFs, not about EN 16931 invoices. `[[UNVERIFIED: the article number within Lei 73-A/2025 — reported as art. 95, single-sourced]]`
- **B2G phasing:** large enterprises since **2021-01-01**. **Micro, small and medium enterprises and public entities acting as co-contractors: 2027-01-01** — as at today they are still exempt. The *dispensa* under DL 111-B/2017 was extended again by Lei 73-A/2025 through 2026-12-31.
- Format: **CIUS-PT**, the Portuguese CIUS of EN 16931 (Portaria n.º 289/2019 de 5 de setembro), syntaxes **UBL 2.1** (primary) and CII. Platform **FE-AP**, run by **eSPap**, not compulsory to use; channels are web service, AS2 or manual upload. **eSPap is the Portuguese Peppol Authority.** `[[UNVERIFIED: the CIUS-PT CustomizationID string, and whether a version newer than v1.1.0 of 2019-09-27 exists]]`
- **ATCUD**, mandatory since **2023-01-01**: the AT-assigned series validation code, a hyphen, and the sequential document number within the series. The validation code is uppercase alphanumeric excluding `0` and `1`, minimum 8 characters. Printed as `ATCUD:TES123TE-4561`; only the value goes into the QR and SAF-T. Basis: DL 28/2019 plus Portaria 195/2020.
- **QR code**: specification in Portaria n.º 195/2020 de 13 de agosto, required for documents issued by certified software, effectively enforced from **2022-01-01**. The ATCUD sits immediately above the QR.
- **SAF-T (PT)**: billing SAF-T **version 1.04_01** (Portaria 302/2016), monthly e-Fatura communication **by the 5th** of the following month. **SAF-T de contabilidade has not started** — postponed again by the 2026 budget to tax periods from **2027**, first delivered in **2028**.
- **Certified software** mandatory where prior-year turnover exceeded **50 000 EUR**, and for anyone using invoicing software regardless of turnover; also catches non-established suppliers with a Portuguese VAT registration.
- Routing: Peppol EAS `9946` (PT:VAT).
- Archiving: **10 years** (DL 28/2019 art. 19 ff.; art. 52 CIVA). Storage anywhere in the **EU** with guaranteed online access for the AT; **outside the EU requires prior AT authorisation**.

---

## Greece — myDATA plus a phased B2B mandate

A CTC reporting model with provider-side authentication rather than authority clearance.

**The B2B mandate is in two phases and phase 1 already slipped once.**

| Phase | Date | Who |
|---|---|---|
| Phase 1 | **2026-03-02** (postponed from 2026-02-02 by Decision A.1044/2026 of 2026-02-17) | Entities with FY2023 gross revenue above **1 000 000 EUR** |
| Grace | 2026-03-02 to 2026-05-03 | Other issuance methods tolerated if the Electronic Data Issue Initiation Declaration was filed by 2026-03-02 |
| Phase 2 | **2026-10-01** | **All remaining obliged entities, no turnover floor** |
| Grace | 2026-10-01 to 2026-12-31 | |

Legal basis: art. 14 Law 4308/2014 as amended by art. 239 of Law 5222/2025; implementing decisions **A.1128/2025** and **A.1129/2025** of 2025-09-16. Scope: domestic B2B, B2B with **non-EU** counterparties, and B2G. Excluded: retail/B2C, non-established VAT-registered businesses, intra-EU B2B (optional). Recipients must accept e-invoices from phase 1. Penalties: 50 % of the transaction VAT, or 500 EUR (single-entry) / 1 000 EUR (double-entry) per audit for non-VATable entities.

EU derogation: **Council Implementing Decision (EU) 2025/502**, derogating from Arts 218 and 232 of Directive 2006/112/EC, published in the OJ 2025-03-13, applying **2025-07-01 to 2027-12-31**. `[[UNVERIFIED: read via mirrors only — the OJ text itself was not retrieved]]`

- **Format:** the B2B mandate uses the **national myDATA XML** (AADE `InvoicesDoc` XSD), technical specification **v2.0.1 (March 2026)**; v2.0.2 is in sandbox with no production date. Since v1.0.12 a provider-issued invoice can be retrieved via `downloadingInvoiceUrl` in three representations: `/pdf`, `/myDATA` and **`/EN16931`**. B2G uses **EN 16931 + Peppol BIS Billing 3.0** with a Greek Peppol CIUS (JMD 63446/2021). `[[UNVERIFIED: the Greek CIUS CustomizationID string — do not assume one]]`
- **An ERP alone is not an acceptable issuance channel** under the mandate. The AADE FAQ is explicit that business management software (commercial/accounting, ERP) does not constitute an acceptable way of issuing invoices. Permitted issuance: a certified provider (ΥΠΑΗΕΣ), *timologio*, or *myDATAapp*. An ERP remains valid for myDATA *transmission*. 32 certified providers as at 2026-08-04.
- **ΜΑΡΚ**: myDATA returns a 14-digit unique registration number per document. A QR code on the visual document has been mandatory since 2024-01-01.
- **B2G**: phased 2023-09-12 → 2024-01-01 (central government suppliers) → 2024-06-01 (all other contracting authorities); from **2025-09-01** mandatory for all General Government expenditure above 2 500 EUR. Channel: supplier → provider or Peppol access point → Peppol → the **ΚΕΔ** national node → contracting authority. Peppol Authority: GSIS/ΓΓΠΣΨΔ `[[UNVERIFIED: confirmed only via search-index snippets]]`
- **B2C**: no e-invoicing obligation; retail flows to myDATA via ΦΗΜ/POS in real time. **Digital delivery notes** phase B was restructured: B1 on 2026-10-12, B2 on 2027-01-01 (previously 2026-05-01).
- Routing: ΑΦΜ; Peppol EAS `9933` (GR:VAT).
- Corrections: credit note type **5.1** (associated, referencing the original ΜΑΡΚ) or **5.2** (unassociated). Cancellation uses the myDATA `CancelInvoice` method referencing the original ΜΑΡΚ; a separate cancellation ΜΑΡΚ is issued and the original is neither deleted nor resubmitted.
- Archiving: **5 years** from the end of the fiscal year (art. 7 Law 4308/2014), **10 years** where the limitation period is extended, **20 years** in tax-evasion cases.
- Incentives: art. 71Θ Law 4172/2013 (procedure A.1129/2025) — 100 % enhanced depreciation of e-invoicing equipment and software plus 100 % enhanced deduction of production, transmission and archiving costs for the first 12 months, from tax year 2025. The declaration had to be filed at least 2 months before the mandatory date, so both windows have closed (2025-12-01 for phase 1, 2026-08-03 for phase 2). **The "reduced statute of limitation" incentive belongs to the old voluntary art. 71ΣΤ scheme for tax years 2020–2022 and is not part of the current package** — several vendor pages conflate the two.

Greece is covered by the ViDA **2035** convergence deadline.

---

## Nordics and the Netherlands — Peppol everywhere, no B2B mandate

Four countries that were doing structured invoicing before the EU standard existed and converged on Peppol. All four are **exchange** regimes: no clearance, no reporting platform, no national CIUS worth building around except Denmark's OIOUBL. Source for the B2G positions: the European Commission country factsheets, last updated 2025-08-14.

- **Denmark.** B2G receipt since **2019-04-18** (Bekendtgørelse nr. 346 af 15/03/2019). In production today: **OIOUBL 2.1** (the national CIUS on UBL 2.1) and **Peppol BIS 3** over **NemHandel**, which now runs on Peppol eDelivery. **OIOUBL 3.0 was cancelled**: Erhvervsstyrelsen published "OIOUBL 3.0 aflyses" on 2026-01-14, and a consultation concluded on 2026-05-27 in favour of *"harmonisering mod ét fælles format baseret på Peppol BIS 4"*, with a concept phase May–December 2026, specification in 2027 and migration 2027–2029. Any migration plan still quoting OIOUBL 3.0 dates is stale. There is **no B2B invoicing mandate**, but **Bogføringsloven (lov nr. 700 af 24.05.2022)** forces the *capability*: the bookkeeping system must send, receive and store e-invoices and connect to NemHandel and Peppol. Rollout for financial years from **2024-07-01** (årsregnskabslov filers with registered standard systems), **2025-01-01** (extended system requirements) and **2026-01-01** for personally owned businesses and associations outside årsregnskabsloven with net turnover above **DKK 300 000 in two consecutive years**. Routing by CVR, P-number, SE-number or GLN/EAN; Peppol EAS `0184`, `0198`, `0096`. Retention **5 years** from the end of the financial year (bogføringsloven § 12). `[[UNVERIFIED: reported Peppol BIS 4 mandatory date of November 2028 and OIOUBL 2.1 retirement in May 2029 — single secondary source, not confirmed on nemhandel.dk]]`
- **Norway — a B2B mandate is now law.** B2G receipt since **2019-04-02** (FOR-2019-04-01-444), format **EHF Fakturering 3.0**, which is identical to Peppol BIS Billing 3.0. **ELMA**, run by DFØ, is the national SMP with roughly 360 000 registered receivers, which makes Norway the easiest country in Europe to reach over Peppol. The 2025 consultation became **Prop. 44 L (2025–2026)**, adopted as **Lovvedtak 52 (2025–2026)** and sanctioned as **lov 19. juni 2026 nr. 39**. New bokføringsloven § 10 second paragraph: *"Dokumentasjon for salg av varer og tjenester til andre bokføringspliktige skal utstedes i elektronisk fakturaformat."* Lovdata's consolidated act puts **§§ 10 and 13 in force 2027-01-01** and **§ 7 in force 2030-01-01** — issuing mandatory from **2027-01-01**, receiving plus digital bookkeeping from **2030-01-01**. **The statute does not name EHF**; it says only *elektronisk fakturaformat* and delegates the format to regulation. Routing by organisasjonsnummer, Peppol EAS `0192`. Retention 5 years primary / 3.5 years secondary (bokføringsloven § 13); from 2027 e-invoices must be kept in their original format. `[[UNVERIFIED: the 2030 leg's exemptions — sole proprietors below NOK 50 000 turnover, non-bookkeeping-liable parties, consumer invoices — from a secondary source only]]`
- **Sweden.** B2G receipt since **2019-04-01** under **lag (2018:1277)**. Peppol BIS Billing 3.0 used as-is, **no national CIUS**, no central platform — each authority uses an access point. **No B2B mandate.** The step that exists is committee directive **Dir. 2026:9, "Moderniserad och brottsförebyggande hantering av mervärdesskatt"**, adopted 2026-02-05, tasking an inquiry with adapting Swedish law to the EU e-invoicing and digital-reporting rules and examining extension to domestic transactions, **reporting by 2027-11-30**. Skatteverket has said it is positive towards mandatory domestic transaction-based reporting. There is **no 2025 DIGG/Skatteverket report recommending a mandate** — what exists is a 2023 joint *hemställan* asking for an inquiry and a 2025 usage survey. Routing by organisationsnummer, Peppol EAS `0007`. Retention **7 years** after the end of the calendar year in which the financial year closed (bokföringslagen 7 kap. 2 §).
- **Finland.** **Laki hankintayksiköiden ja elinkeinonharjoittajien sähköisestä laskutuksesta 241/2019**, implementing Directive 2014/55/EU; in force **2019-04-01** for central government and joint procurement units, with **§ 4 — the right to demand a machine-readable e-invoice conforming to the European standard — applying from 2020-04-01** to other contracting entities and to private businesses. This is a **right to demand, not an obligation to send**; there is no B2B or B2G send-side mandate. Formats: **Finvoice 3.0** (Finanssiala) and **TEAPPSXML 3.0** (Tietoevry) nationally, plus UBL 2.1, CII and Peppol BIS Billing 3.0; central-government invoices flow through the Handi service. Routing: the *verkkolaskuosoite* is an **OVT-tunnus**, always paired with a *välittäjätunnus*; Peppol EAS `0216` (FI:OVT2), issuing agency TIEKE. Since 2024-04-01 Finnish organisations on Peppol must use the ISO 6523-conformant OVT. Peppol Authority: Valtiokonttori. Retention: kirjanpitolaki 1336/1997 — **6 years** for *tositteet* from the end of the calendar year in which the financial period ended, **10 years** for books and financial statements. `[[UNVERIFIED: the EUR 10 000 turnover threshold for exercising the § 4 right appears only in the EC factsheet and was not corroborated on a Finnish source]]`
- **Netherlands.** B2G receipt since **2019-11-01** (law of 2017-12-20 amending the Aanbestedingswet 2012); suppliers to central government have had to send electronically since 2017-01-01. Formats: **NLCIUS / SI-UBL 2.0**, Peppol BIS 3.0, UBL-OHNL, plus SETU (HR-XML) for temporary staff. Platforms: Peppol, **Digipoort** for central government, and a supplier portal. **No B2B mandate, none legislated or scheduled** — voluntary and, absent a mandate, still subject to the buyer's consent under Art 232. The only forward item is ViDA cross-border from 2030-07-01. Routing: Peppol EAS `0106` (NL:KVK) and `0190` (NL:OINO). Retention **7 years**, **10 years** for immovable property.

## Austria and Ireland — B2G receipt only

- **Austria.** B2G since **2020-04-18** for central government entities under IKT-Konsolidierungsgesetz § 5 and BVergG 2018 § 368; sub-central authorities may opt in. Accepted formats: **ebInterface 4.3, 5 and 6**, UBL 2.1 and CII; channels are the USP business service portal, e-Rechnung.gv.at, and Peppol for foreign suppliers. **No B2B mandate.** Peppol EAS `9914` (ATU VAT number) or `9915`.
- **Ireland.** SI 258/2019 transposed Directive 2014/55/EU on 2019-06-12: public authorities must receive and process EN 16931 invoices above EU procurement thresholds; suppliers are **not** obliged to issue. Peppol BIS Billing 3.0 with sector-specific CIUS for local government, central government (NSSO) and education (ETBs). **No B2B mandate**; ViDA 2030 is the planning horizon. Peppol EAS `9935`.

## Switzerland — outside the regime entirely

Not EU, not EEA, so neither Directive 2014/55/EU nor ViDA applies, and there is **no Swiss Peppol Authority**. EN 16931 and Peppol are used privately where the parties agree, not because anything requires them.

- **B2G is mandatory by a Federal Council decision, not by statute.** On **2014-10-08** the Bundesrat decided to oblige suppliers of the federal administration to submit electronic invoices where the contract value exceeds **CHF 5 000**, in force from **2016-01-01**. *Kleinbeschaffungen* are exempt. `[[UNVERIFIED: a VöB/BöB ordinance article as the legal basis — every official page attributes the rule to the Bundesrat decision plus the AGB Bund, not to an ordinance]]`
- Delivery: a structured dataset through one of the named service providers (PostFinance, Swisscom, ABACUS, io-market, PENTAG, StepCom) or **PDF by email**. PDF via a service-provider portal was discontinued on 2023-06-30. `[[UNVERIFIED: no mandated XML syntax could be found on any admin.ch page. Claims that the Bund requires EN 16931 or Peppol BIS UBL are uncorroborated. eCH-0217 is **not** the federal e-invoice format — it is the E-MWST specification for filing VAT returns]]`
- **B2B is entirely voluntary.** **eBill** (SIX) is a bill-presentment-and-payment network delivering into online banking; it references neither EN 16931 nor Peppol. **swissDIGIN** is a neutral industry forum run by GS1 Switzerland.
- Invoice content: **MWSTG Art 26 (SR 641.20)** — the Swiss analogue of Art 226, and a different list. Do not reuse an EU content model without mapping it.
- Retention: **OR Art 958f (SR 220) — ten years** from the end of the financial year for books, accounting vouchers, the Geschäftsbericht and the Revisionsbericht, implemented by **GeBüV (SR 221.431)**: Art 3 integrity, Art 4 documentation kept as long as the records, **Art 9** — alterable media are permitted only with a digital signature, a timestamp and a documented procedure. This is one of the few places in Europe where a signature genuinely is required, and it is a bookkeeping rule about storage media, not an invoice rule.
- Routing: Peppol EAS `0183` (IDE/UIDB) and `9927` (CH VAT) exist. `[[UNVERIFIED: no national routing scheme for the federal administration was confirmed — the EFV describes a provider-issued Teilnehmernummer plus the eDirectory.ch participant directory]]`

## United Kingdom — no mandate today, one announced for 2029

- **No domestic e-invoicing mandate is in force as at 2026-08-05.** The HMRC/DBT consultation "Promoting electronic invoicing across UK businesses and the public sector" ran **2025-02-13 to 2025-05-07** (342 responses); the **government response was published 2025-11-26**, confirming a **decentralised four-corner model**, no real-time reporting at launch, and broad respondent support for Peppol and EN 16931, with a design collaboration phase from January 2026.
- **Budget 2025 announced mandatory e-invoicing for all VAT invoices from 2029**, with a roadmap to be published at Budget 2026. The **"Tax update 2026: simplification, modernisation and fairness summary"** of **2026-06-23** states that *"the electronic procurement system Peppol will be the core interoperability network for e-invoicing in the UK"*. That page gives no commencement date, does not name EN 16931 or Peppol BIS 3.0, and does not delimit B2B versus B2G scope. `[[UNVERIFIED: any specific 2029 commencement day, syntax list or identifier scheme — none is on a gov.uk page; the Budget 2026 roadmap is the next source]]`
- **The public-sector rule moved.** The Public Procurement (Electronic Invoices etc.) Regulations 2019 are **SI 2019/624**; they inserted regs 113A/113B into PCR 2015. **Reg 113A was revoked on 2025-02-24** by Procurement Act 2023 s.127(2), Sch. 11 para. 5. The live obligation is now **Procurement Act 2023 s. 67** — an implied, non-excludable contract term requiring a contracting authority to accept and process undisputed electronic invoices complying with **BS EN 16931-1:2017** in a syntax listed in **PD CEN/TS 16931-2:2017**. Cite s. 67, not the 2019 SI.
- **NHS England** requires Peppol: the 2014 NHS eProcurement Strategy mandated GS1 and Peppol through the NHS Standard Contract, and NHS England states that suppliers must submit all invoices via a Peppol-compliant e-invoicing system. The Peppol Authority for England is **Supply Chain Coordination Ltd (SCCL)**, an NHS body — there is no whole-of-government UK Peppol Authority, and none for Scotland, Wales or Northern Ireland.
- Retention: **VAT Act 1994 Sch. 11 para. 6** — records preserved for "such period **not exceeding 6 years** as they may specify in writing". Six years is HMRC's ceiling, not a flat statutory rule.

## Checkpoints

- [ ] Correct classification per country: clearance, reporting, or exchange-only
- [ ] Reporting-only countries (Hungary) not treated as e-invoicing mandates
- [ ] Grace periods distinguished from postponements (Belgium, Greece, France)
- [ ] Superseded infrastructure not relied on (Belgian Hermes, French PPF as an exchange platform)
- [ ] Scope exclusions checked before assuming an entity is in
- [ ] Correction mechanism implemented per country
- [ ] Retention period and storage-location condition confirmed per country
- [ ] Every `[[UNVERIFIED]]` and `[[MISSING]]` above resolved before advising on that point
