# Identifiers and code lists

The layer that fails silently. A wrong VAT number is rejected loudly; a wrong EAS scheme code routes the invoice to nobody. All code values below are reproduced from the Peppol BIS Billing 3.0 code lists (November 2025 release, docs.peppol.eu/poacc/billing/3.0/codelist/), which are the maintained subsets of the underlying UN/CEFACT and ISO lists.

## EAS — Electronic Address Scheme (BT-34 / BT-49, `schemeID` on `cbc:EndpointID`)

The EAS code list is derived from ISO 6523 ICD plus Peppol-assigned values in the 9xxx range. It identifies *what kind of identifier* the electronic address is. It is not the country code and not the identifier itself.

Codes you will actually need:

| EAS | Scheme | Typical use |
|---|---|---|
| `0007` | Organisationsnummer | Swedish legal entities |
| `0009` | SIRET-CODE | France, establishment-level |
| `0037` | LY-tunnus | Finland |
| `0060` | D-U-N-S Number | global |
| `0088` | EAN Location Code | GLN, the classic Peppol identifier |
| `0106` | Vereniging van Kamers van Koophandel en Fabrieken in Nederland Scheme | Dutch KvK |
| `0130` | Directorates of the European Commission | EU institutions |
| `0151` | Australian Business Number (ABN) | Australia |
| `0183` | Numéro d'identification suisse des entreprises (IDE), Swiss UIDB | Switzerland |
| `0184` | DIGSTORG | Denmark (CVR under the Danish digital agency scheme) |
| `0192` | Enhetsregisteret ved Brønnøysundregisterne | Norway |
| `0193` | UBL.BE party identifier | Belgium |
| `0195` | Singapore UEN identifier | Singapore |
| `0196` | Kennitala | Iceland |
| `0198` | ERSTORG | Denmark |
| `0199` | Legal Entity Identifier (LEI) | global |
| `0201` | Codice Univoco Unità Organizzativa iPA | Italian public bodies |
| `0202` | Indirizzo di Posta Elettronica Certificata | Italian PEC address |
| `0204` | Leitweg-ID | German public sector |
| `0208` | Numéro d'entreprise / ondernemingsnummer / Unternehmensnummer | Belgium (CBE/KBO) |
| `0209` | GS1 identification keys | global |
| `0210` | CODICE FISCALE | Italy |
| `0211` | PARTITA IVA | Italy |
| `0212` | Finnish Organization Identifier | Finland |
| `0213` | Finnish Organization Value Add Tax Identifier | Finland |
| `0216` | OVTcode | Finland |
| `0217` | Netherlands Chamber of Commerce and Industry establishment number | Netherlands |
| `0221` | Registered number of the qualified invoice issuer | Japan |
| `0230` | National e-Invoicing Framework | Malaysia |
| `0235` | UAE Tax Identification Number (TIN) | United Arab Emirates |
| `0240` | Répertoire des personnes morales | France |
| `0245` | Tax identification number (DIČ) | Slovakia |
| `9910` | Hungary VAT number | Hungary |
| `9914` | Österreichische Umsatzsteuer-Identifikationsnummer | Austria |
| `9920` | Agencia Española de Administración Tributaria | Spain |
| `9925` … `9953` | Country VAT numbers | BE 9925, BG 9926, CH 9927, CY 9928, CZ 9929, DE 9930, EE 9931, GB 9932, GR 9933, HR 9934, IE 9935, LT 9937, LU 9938, LV 9939, MT 9943, NL 9944, PL 9945, PT 9946, RO 9947, SI 9949, SK 9950 |
| `9957` | French VAT number | France |
| `9959` | Employer Identification Number (EIN, USA) | United States |

Traps:

- **Italy: `9906` and `9907` are gone.** The current codes are `0211` (Partita IVA) and `0210` (Codice Fiscale). Code that still emits `9906` was written before the list was revised and routes nowhere.
- **The list is maintained and entries get removed.** In eDEC code list v9.7 (2026-07-02), `0193` (UBL.BE) carries removal date **2026-07-07** and is replaced by `0208`; `9954` (NL:OIN) was removed on 2026-03-31; `9909` (NO:VAT), `9912` (EU:VAT), `9916` (AT:CID) and `9917` (IS:KT) are long-standing deprecations. Re-read the code list at each Peppol release rather than vendoring a copy.
- **The EAS goes in the `schemeID` attribute, the value in the element text.** `<cbc:EndpointID schemeID="0088">7300010000001</cbc:EndpointID>`. Writing `0088:7300010000001` into the element text is wrong; the colon form is the *participant identifier* used at the transport layer, not in the invoice.
- **EAS is not ICD.** The EAS list qualifies the *electronic address* (BT-34 seller, BT-49 buyer — `cbc:EndpointID`). The ISO 6523 ICD list qualifies *party identifiers*: `cac:PartyIdentification/cbc:ID/@schemeID` (BT-29) and `cac:PartyLegalEntity/cbc:CompanyID/@schemeID` (BT-30). The numbers overlap because Peppol built EAS on ICD, but the two lists are maintained separately and diverge. Peppol publishes them as separate code lists (`codelist/eas/` and `codelist/ICD/`).
- `0088` is the GLN. A GLN is a 13-digit GS1 location number with a check digit; it is not the company's VAT number and cannot be derived from it.

## National routing identifiers

| Country | Identifier | Format | Where it goes |
|---|---|---|---|
| Germany (public sector) | Leitweg-ID | Coarse address, optional fine address, check digit, separated by `-`; assigned by the receiving authority | BT-10, `cbc:BuyerReference` / `ram:BuyerReference`. **Not** a party identifier. EAS `0204` exists for transport-layer addressing. |
| Italy | Codice destinatario | Exactly 7 characters. `0000000` = consumer or no channel; `XXXXXXX` = foreign counterparty. Alternative: a PEC address. | FatturaPA `<CodiceDestinatario>` / `<PECDestinatario>`, not an EN 16931 field |
| France | SIRET (14 digits) / SIREN (9 digits) | SIRET identifies the establishment, SIREN the legal entity | EAS `0009` for SIRET; Chorus Pro service code additionally identifies the receiving department |
| Belgium | Ondernemingsnummer / numéro d'entreprise | 10 digits | EAS `0208` |
| Denmark | CVR / EAN-lokationsnummer | 8 digits / 13 digits | EAS `0184` or `0198`; public bodies are addressed by EAN/GLN `0088` |
| Norway | Organisasjonsnummer | 9 digits | EAS `0192` |
| Poland | NIP | 10 digits | KSeF addresses by NIP; the platform assigns a *numer KSeF* to each accepted invoice |
| Romania | CUI/CIF (businesses), CNP (individuals from 2026) | — | RO e-Factura via SPV |
| Hungary | Adószám (tax number) | First 8 digits of a domestic taxable customer's tax number must appear on the invoice | RTIR reporting, not routing |

## UNTDID 1001 — document type code (BT-3)

`cbc:InvoiceTypeCode` / `ram:TypeCode`. The Peppol subset for invoices:

`71` Request for payment · `80` Debit note related to goods or services · `82` Metered services invoice · `84` Debit note related to financial adjustments · `102` Tax notification · `218` Final payment request based on completion of work · `219` Payment request for completed units · `326` Partial invoice · `331` Commercial invoice which includes a packing list · **`380` Commercial invoice** · `382` Commission note · `383` Debit note · **`384` Corrected invoice** · `386` Prepayment invoice · `388` Tax invoice · **`389` Self-billed invoice** · `393` Factored invoice · `395` Consignment invoice · `553` Forwarder's invoice discrepancy report · `575` Insurer's invoice · `623` Forwarder's invoice · `780` Freight invoice · `817` Claim notification · `870` Consular invoice · `875` Partial construction invoice · `876` Partial final construction invoice · `877` Final construction invoice

Credit note subset (`cbc:CreditNoteTypeCode`, or `ram:TypeCode` in CII):

`81` Credit note related to goods or services · `83` Credit note related to financial adjustments · **`381` Credit note** · `396` Factored credit note · `532` Forwarder's credit note

Use `380` for a normal invoice and `381` for a normal credit note. `384` (Corrected invoice) triggers a preceding-invoice reference requirement in national CIUS (German rule DE-R-026 warns when BG-3 is absent with type 384). `875`/`876`/`877` exist because German construction invoicing needs them — do not use them elsewhere.

## UNCL5305 — VAT category code (BT-95 / BT-102 / BT-118 / BT-151)

| Code | Meaning | Rate must be | Exemption reason |
|---|---|---|---|
| `S` | Standard rate | > 0 | must be absent (BR-S-10) |
| `Z` | Zero rated goods | 0 | must be absent (BR-Z-10) |
| `E` | Exempt from Tax | 0 | required (BR-E-10) |
| `AE` | VAT Reverse Charge | 0 | required, meaning "Reverse charge" (BR-AE-10) |
| `K` | VAT exempt for EEA intra-community supply of goods and services | 0 | required, meaning "Intra-community supply" (BR-IC-10) |
| `G` | Free export item, VAT not charged | 0 | required, meaning "Export outside the EU" (BR-G-10) |
| `O` | Services outside scope of tax | absent entirely | required (BR-O-10); no seller or buyer VAT identifier allowed (BR-O-02) |
| `L` | Canary Islands general indirect tax | — | Spain (IGIC) |
| `M` | Tax for production, services and importation in Ceuta and Melilla | — | Spain (IPSI) |
| `B` | Transferred (VAT), In Italy | — | Italy split payment |

`K` is intra-Community supply, not `E`. Confusing the two is the single most common VAT-category error, because "exempt" is how the supply is described in plain language.

## VATEX — VAT exemption reason codes (BT-121)

Two families. The EU-directive family (`VATEX-EU-132…`, `VATEX-EU-143…`, `VATEX-EU-148…`, `VATEX-EU-151…`, `VATEX-EU-159`, `VATEX-EU-309`) cites the article of Directive 2006/112/EC. The category-support family is what you use for the standard cases:

| Code | Use with category | Meaning |
|---|---|---|
| `VATEX-EU-AE` | `AE` | Reverse charge (supports BR-AE-10) |
| `VATEX-EU-IC` | `K` | Intra-Community supply (supports BR-IC-10) |
| `VATEX-EU-G` | `G` | Export outside the EU (supports BR-G-10) |
| `VATEX-EU-O` | `O` | Not subject to VAT (supports BR-O-10) |
| `VATEX-EU-D`, `-F`, `-I`, `-J` | `E` | Second-hand transport means, second-hand goods, works of art, collectors' items — margin schemes |
| `VATEX-EU-79-C` | `E` | Repayment of expenditures under Art 79(c) |

France adds a national family (`VATEX-FR-FRANCHISE` for the *franchise en base*, `VATEX-FR-CNWVAT` for domestic credit notes without VAT, and `VATEX-FR-CGI261…` for Code Général des Impôts exemptions). Do not use French codes outside France.

## UNECE Recommendation 20 — unit of measure (BT-130, BT-150)

The `unitCode` attribute. Code list name: "Recommendation 20, including Recommendation 21 codes — prefixed with X".

`C62` one · `H87` piece · `EA` each · `DAY` day · `HUR` hour · `MIN` minute [unit of time] · `MON` month · `ANN` year · `KGM` kilogram · `GRM` gram · `LTR` litre · `MTR` metre · `KMT` kilometre · `MTK` square metre · `MTQ` cubic metre · `KWH` kilowatt hour · `NAR` number of articles

`PCE`, `SET` and `ZZ` are **not** in the Peppol subset — using them fails validation. For "one unit of an unspecified thing" use `C62`; `H87` (piece) and `EA` (each) are also valid and are preferred by some national CIUS. Do not use `ZZ` as a fallback.

## UNCL4461 — payment means (BT-81)

The values that matter: `10` In cash · `20` Cheque · `30` Credit transfer · `31` Debit transfer · `42` Payment to bank account · `48` Bank card · `49` Direct debit · `54` Credit card · `55` Debit card · `58` SEPA credit transfer · `59` SEPA direct debit · `68` Online payment service · `97` Clearing between partners · `ZZZ` Mutually defined.

`30` is the safe default for a bank transfer. `58` is more precise inside SEPA and triggers Peppol rule BR-61 (a payment account identifier BT-84 must then be present).

## Checkpoints

- [ ] Every `schemeID` value taken from the EAS list, not invented or copied from a different list
- [ ] No `9906` / `9907` for Italian parties
- [ ] Leitweg-ID in BT-10, not in a party identifier
- [ ] Codice destinatario present and exactly 7 characters, `0000000` for consumers
- [ ] VAT category `K` used for intra-Community supply, not `E`
- [ ] Every non-`S`, non-`Z` category carries a VATEX code or exemption text
- [ ] Unit codes restricted to the Rec 20 subset the target CIUS accepts
- [ ] Document type code 380/381 unless a national rule requires another value
