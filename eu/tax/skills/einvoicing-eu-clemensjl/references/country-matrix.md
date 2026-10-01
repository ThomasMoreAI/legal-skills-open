# Per-country lookup

Scan this, then read the country's section in `countries-mandates.md` or `countries-other.md` before deciding anything. Status as at **2026-08-05**. Dates move; the entry that decides a go-live gets re-verified against the authority's own page.

Column meanings: **Model** — *clearance* (the authority receives and validates the invoice before or as it reaches the buyer), *reporting* (the invoice travels normally, data is reported separately), *exchange* (a format and channel obligation with no authority in the path). **Mandate** — the issuing obligation unless stated otherwise.

## The EU / EEA

| Country | Format | Syntax | Channel | Model | Mandate status and dates | Routing identifier |
|---|---|---|---|---|---|---|
| **Austria** | ebInterface 4.3/5/6, Peppol BIS Billing 3.0 | ebInterface XML, UBL 2.1, CII | USP / e-Rechnung.gv.at, Peppol | exchange | **B2G only**, central government since 2020-04-18 (IKT-Konsolidierungsgesetz § 5, BVergG 2018 § 368). **No B2B mandate** | Peppol EAS `9914` (ATU) or `9915` |
| **Belgium** | EN 16931, no national CIUS | UBL 2.1 (Peppol BIS Billing 3.0) | **Peppol** by default | exchange | **B2B live since 2026-01-01**; penalties enforced from 2026-04-01 after a Q1 grace period. B2G since 2024-03-01 for contracts > 3 000 EUR | Peppol EAS `0208` (KBO/BCE) |
| **Denmark** | OIOUBL 2.1 (national CIUS), Peppol BIS 3. **OIOUBL 3.0 cancelled 2026-01-14**; migration to Peppol BIS 4 planned 2027–2029 | UBL 2.1 | **NemHandel** (now on Peppol eDelivery), Peppol | exchange | **B2G receipt since 2019-04-18.** **No B2B invoicing mandate**, but Bogføringsloven (lov nr. 700 af 24.05.2022) requires the *system* to send, receive and store e-invoices: FY from 2024-07-01, 2025-01-01, and **2026-01-01** for personally owned businesses above DKK 300 000 turnover in two consecutive years | CVR, P-number, SE-number or GLN/EAN; Peppol EAS `0184`, `0198`, `0096` |
| **Finland** | Finvoice 3.0, TEAPPSXML 3.0, Peppol BIS Billing 3.0 — all EN 16931 conformant | UBL 2.1 or CII | Peppol, bank operator networks, Handi for central government | exchange | **B2G receipt since 2019-04-01.** **No send-side mandate.** Act **241/2019 § 4**, applying from **2020-04-01**, gives a business the **right to demand** a structured e-invoice from its supplier | OVT-tunnus + välittäjätunnus; Peppol EAS `0216` (FI:OVT2) |
| **France** | Factur-X, UBL, CII (*socle*); extension EXT-FR-FE | CII D16B, UBL 2.1 | **Plateformes agréées (PA)**; PPF = annuaire + data concentrator only | clearance-adjacent (CTC via PA) + e-reporting | **Receipt for all 2026-09-01.** Issuing + e-reporting: GE and ETI **2026-09-01**, PME/TPE **2027-09-01**. Tolerance on sanctions at start-up | SIREN/SIRET + code de routage via the PPF annuaire; Peppol EAS `0225`, `0009`, `0002`, `9957` |
| **Germany** | XRechnung 3.0.2 (CIUS), ZUGFeRD 2.5.2, Peppol BIS Billing 3.0 | UBL 2.1 or CII D16B | **OZG-RE** (the ZRE was switched off 2025-09-19): Weberfassung, Upload, e-mail, Peppol | exchange | **Receipt obligatory since 2025-01-01.** Issuing: **2027-01-01** for issuers with prior-year turnover above 800 000 EUR, **2028-01-01** for all (§ 27 Abs 38 UStG). EDI transitional ends 2027-12-31 | Leitweg-ID in **BT-10** for public sector; Peppol EAS `0204`, `9930` |
| **Greece** | myDATA XML (B2B mandate); EN 16931 + Peppol BIS 3.0 (B2G) | national XML; UBL 2.1 for B2G | Certified provider (ΥΠΑΗΕΣ), *timologio*, myDATAapp → myDATA; Peppol + ΚΕΔ for B2G | reporting → clearance-like (provider authentication, ΜΑΡΚ returned) | **B2B phase 1 2026-03-02** (FY2023 revenue > 1 M EUR), **phase 2 2026-10-01** (all). B2G fully since 2025-09-01 above 2 500 EUR. An ERP alone is not an accepted issuance channel | ΑΦΜ; Peppol EAS `9933` |
| **Hungary** | — (invoice format is free) | — | RTIR / Online Számla, `invoiceData.xsd` v3.0 | **reporting only** | **No e-invoicing mandate.** Data reporting on every invoice since 2021-01-04; immediate for software-issued invoices | Hungarian tax number; first 8 digits of a domestic customer's tax number on the invoice |
| **Ireland** | EN 16931, Peppol BIS Billing 3.0 with sector CIUS | UBL 2.1 | Peppol | exchange | **B2G receipt only** (SI 258/2019). **No B2B mandate**; ViDA 2030 is the planning horizon | Peppol EAS `9935` |
| **Italy** | **FatturaPA** — national XML, not an EN 16931 syntax | national XML, schema `Schema_VFPR12` v1.2.3, technical spec v1.9.1 from 2026-05-15 | **SdI** | **clearance** | **B2G since 2014/2015, B2B and B2C since 2019-01-01.** Esterometro abolished 2022-07-01 — cross-border data flows through SdI | `CodiceDestinatario`, 7 chars (`0000000` consumer, `XXXXXXX` foreign) or PEC; Peppol EAS `0211`, `0210`, `0201`, `0202` |
| **Netherlands** | NLCIUS / SI-UBL 2.0, Peppol BIS 3.0, UBL-OHNL, SETU | UBL 2.1 | Peppol, Digipoort, supplier portal | exchange | **B2G receipt since 2019-11-01**; central-government suppliers send electronically since 2017-01-01. **No B2B mandate, none scheduled** — voluntary, buyer's consent required | Peppol EAS `0106` (KVK), `0190` (OINO) |
| **Norway** | EHF Fakturering 3.0 = Peppol BIS Billing 3.0. The 2027 statute says only *elektronisk fakturaformat* | UBL 2.1 | Peppol; **ELMA** is the national SMP (~360 000 receivers) | exchange | **B2G receipt since 2019-04-02.** **B2B is now law** — lov 19. juni 2026 nr. 39, new bokføringsloven § 10: **issuing from 2027-01-01**, receiving + digital bookkeeping from **2030-01-01** | Organisasjonsnummer; Peppol EAS `0192` |
| **Poland** | **FA(3)** logical structure (also FA_RR(1)) | national XML | **KSeF**, API 2.0 `/v2` | **clearance** | **Receipt for all since 2026-02-01.** Issuing: 2026-02-01 above PLN 200 m 2024 sales, **2026-04-01** all others, PLN 10 000/month exemption ends 2027-01-01. B2C out of scope | NIP; system-assigned *numer KSeF* per invoice; Peppol EAS `9945` |
| **Portugal** | CIUS-PT (B2G); no B2B format mandate | UBL 2.1 primary, CII | FE-AP (eSPap), Peppol; e-Fatura + SAF-T for reporting | reporting (certified software) | **No general B2B mandate.** B2G: large enterprises since 2021-01-01, **SMEs and public co-contractors 2027-01-01**. **PDF tolerance ends 2026-12-31**; from 2027-01-01 an e-invoice needs a qualified signature/seal or EDI | Peppol EAS `9946`; ATCUD + QR on the document |
| **Romania** | **RO_CIUS**, validation artefacts v1.0.8 | UBL 2.1 or CII | **SPV** / RO e-Factura API | **clearance** | **B2G 2022-07-01, B2B 2024-07-01, B2C 2025-01-01.** Transmission within **5 working days** since 2026-01-01 (OUG 89/2025) | CUI/CIF; CNP for individuals from 2026; Peppol EAS `9947` |
| **Spain** | Verifactu: no format mandate. Crea y Crece: CII, UBL, EDIFACT, Facturae. B2G: Facturae 3.2.2 | varies | AEAT (Verifactu records); AEAT public solution + private exchange (Crea y Crece); FACe (B2G) | reporting (Verifactu) + exchange (Crea y Crece) | **Verifactu 2027-01-01** (corporate) / **2027-07-01** (others). **Crea y Crece**: RD 238/2026 in force 2026-04-20 but the clock starts on an orden ministerial **not yet published**; then +12 months above 8 M EUR, +24 months for the rest. B2G since 2015-01-15 | DIR3 codes (B2G); Peppol EAS `9920`. Basque Country and Navarra run separate foral regimes |
| **Sweden** | Peppol BIS Billing 3.0 used as-is, no national CIUS | UBL 2.1 | Peppol; no central platform, access points per authority | exchange | **B2G receipt since 2019-04-01** (lag 2018:1277). **No B2B mandate.** Inquiry under Dir. 2026:9 of 2026-02-05 to examine domestic reporting, **reporting by 2027-11-30** | Organisationsnummer; Peppol EAS `0007` |

## Non-EU contrast cases

| Country | Format | Syntax | Channel | Model | Mandate status | Routing identifier |
|---|---|---|---|---|---|---|
| **Switzerland** | No mandated XML syntax verified; structured dataset via a named service provider, or PDF by e-mail | — | Six named service providers; eBill (SIX) for B2C-style presentment | exchange | **Federal administration only**: Bundesrat decision of 2014-10-08, in force 2016-01-01, for contract values above **CHF 5 000**. **No B2B mandate.** Outside EU law entirely; no Swiss Peppol Authority | Provider-issued Teilnehmernummer; Peppol EAS `0183`, `9927` exist |
| **United Kingdom** | BS EN 16931-1:2017 for public sector; Peppol named as the core network for the coming mandate | UBL 2.1 in practice | Peppol; SCCL is the Peppol Authority for NHS England | exchange | **No mandate in force.** Public bodies must accept EN 16931 invoices under **Procurement Act 2023 s. 67** (PCR 2015 reg 113A revoked 2025-02-24). Budget 2025 announced a **mandate for all VAT invoices from 2029**; roadmap due at Budget 2026 | Peppol participant ID; scheme for the 2029 mandate not fixed |

## What each country forces you to build

| Country | Syntax work | Channel work | Extra subsystem |
|---|---|---|---|
| Austria, Ireland, Netherlands, Sweden, Finland, Norway | none beyond EN 16931 | one Peppol access point | — |
| Belgium | none — Peppol BIS as-is | one Peppol access point | credit-note flow over Peppol; Invoice Response handling |
| Denmark | OIOUBL 2.1 mapping alongside Peppol BIS | NemHandel or Peppol | bookkeeping-system capability under Bogføringsloven |
| Germany | XRechnung CIUS; optionally a ZUGFeRD hybrid writer | Peppol and/or OZG-RE | Leitweg-ID handling in BT-10; 8-year archive |
| France | Factur-X (CII) plus UBL/CII | a plateforme agréée integration | **e-reporting** — a second, separate data stream |
| Italy | FatturaPA — a whole second document model | SdI adapter with async receipts | conservazione a norma; TD document type logic |
| Poland | FA(3) — a whole second document model | KSeF 2.0 API, plus offline/awaria modes | KSeF number persistence; correction-only workflow |
| Romania | RO_CIUS on UBL | SPV API | 5-working-day transmission SLA |
| Spain | Facturae for B2G; CII/UBL for Crea y Crece | AEAT record submission; FACe; later the public solution | **Verifactu** hash chain, QR and event log — a software regime, not a format |
| Portugal | CIUS-PT for B2G only | eSPap or Peppol | ATCUD + QR + SAF-T monthly submission; certified software |
| Greece | myDATA XML | a certified provider — an ERP alone is not accepted | ΜΑΡΚ persistence; QR on the rendition |
| Hungary | none — the invoice format is free | none | RTIR reporting client, immediate submission |
| Switzerland, United Kingdom | none today | provider or Peppol by agreement | watch the UK 2029 mandate roadmap |

## What changed recently

Items that invalidate documentation written before 2026. Each is sourced in the country's own section.

- France: the PPF stopped being an exchange platform (October 2024); "PDP" became **plateforme agréée** in the loi de finances pour 2026.
- Spain: Verifactu moved from 2026 to **2027** by Real Decreto-ley 15/2025.
- Belgium: the **Hermes** converter was decommissioned on 2025-12-31.
- Germany: the **ZRE was switched off on 2025-09-19** and folded into OZG-RE; invoice retention is **8 years**, not 10.
- Poland: the buyer-issued **nota korygująca was abolished on 2026-02-01**.
- Denmark: **OIOUBL 3.0 was cancelled** on 2026-01-14 in favour of Peppol BIS 4.
- Norway: a **B2B mandate became law** (lov 19. juni 2026 nr. 39) — issuing from 2027-01-01.
- United Kingdom: a **mandate for all VAT invoices from 2029** was announced at Budget 2025; PCR 2015 reg 113A was revoked and replaced by Procurement Act 2023 s. 67.
- Peppol: the **MD5/CNAME participant lookup is dead**; the SML zone is moving to `participant.sml.prod.tech.peppol.org`.

## How to read this quickly

- **Clearance** countries (Italy, Poland, Romania) put the tax authority in the transmission path. You cannot send the invoice to the buyer without the platform, and you cannot un-send it. Build the platform adapter first.
- **Reporting** countries (Hungary, Portugal, Spain-Verifactu, Greece-myDATA) leave the invoice alone and demand a separate data stream. The invoicing feature and the reporting feature are two projects.
- **Exchange** countries (Belgium, Germany, Austria, Ireland, the Nordics, the Netherlands) only constrain format and channel. This is the cheapest case, and Peppol usually covers it.
- **Receipt obligations arrive before issuing obligations** in Germany (2025-01-01), France (2026-09-01) and Poland (2026-02-01). A product that only issues invoices is still exposed.
- **Two countries have no e-invoicing mandate but are frequently listed as if they did**: Hungary (reporting only) and Portugal (certified software plus reporting, no B2B exchange mandate).
- **ViDA fixes the horizon**: cross-border B2B must be EN 16931 from **2030-07-01**; Member States with pre-existing domestic systems — Italy, Hungary, Spain, Greece among them — must converge by **2035-01-01**.

## Checkpoints

- [ ] Every country the business invoices into has a row that is fully filled for that business's segment
- [ ] Model column drives the architecture decision before the format column does
- [ ] Receipt obligation checked separately from issuing
- [ ] The date that binds *this* entity recorded, not the country's earliest date
- [ ] Every `[[MISSING]]` above resolved before advising on that country
- [ ] Row re-verified against the authority's own page within the last month before a go-live
