# After issuance: corrections, credit notes, archiving, integrity

The half of the problem that gets built last and causes the audit findings.

## The rule that governs everything here

**An issued invoice is never edited.** Art 219 of Directive 2006/112/EC: "Any document or message that amends and refers specifically and unambiguously to the initial invoice shall be treated as an invoice." The correction is a new document, itself an invoice, itself subject to Art 226 and to the same format and channel obligations as the original.

Once a document has been accepted by a clearance platform (Italian SdI, Polish KSeF, Romanian SPV, Greek myDATA), it cannot be withdrawn. Product designs with a "void invoice" button are wrong everywhere; they are catastrophically wrong in clearance countries, where the tax authority already holds the document.

## Credit note versus corrected invoice

Two different instruments. Choosing the wrong one produces a ledger that does not reconcile.

| Instrument | When | EN 16931 modelling |
|---|---|---|
| **Credit note** | The amount owed is reduced — return, discount, partial cancellation, full reversal | UBL: root element `CreditNote`, `cbc:CreditNoteTypeCode` = `381`, lines are `cac:CreditNoteLine` with `cbc:CreditedQuantity`. CII: same `rsm:CrossIndustryInvoice` root, `ram:TypeCode` = `381`. Amounts positive; the document type carries the sign. |
| **Corrected invoice** | The original was wrong in substance and is replaced | `cbc:InvoiceTypeCode` = `384`, with BG-3 Preceding Invoice reference (BT-25 = the original invoice number, BT-26 = its issue date). German rule DE-R-026 warns if BG-3 is missing with type 384; Art 226(16) makes it mandatory content from 2030-07-01. |
| **Negative invoice** | Never | Type 380 with negative totals fails the arithmetic and category rules and is not accepted by clearance platforms. |

Both must reference the original unambiguously (Art 219). Both must go through the same channel as the original.

## Country-specific correction rules

| Country | Mechanism | Notes |
|---|---|---|
| **Italy** | Nota di credito, document type **TD04**, under art. 26 DPR 633/1972 | An SdI-accepted invoice cannot be cancelled. TD04 is transmitted through SdI like any other document. |
| **Poland** | **Faktura korygująca**, issued by the seller through KSeF, referencing the original KSeF number | The buyer-issued **nota korygująca** was **abolished on 2026-02-01**, inside and outside KSeF. Code that offers a buyer-side correction note is now wrong. |
| **France** | **Avoir** (credit note) or **facture rectificative**, itself an e-invoice through a plateforme agréée | The transmitted invoice is frozen. Four mandatory lifecycle statuses exist: 200 *déposée*, 213 *rejetée*, 210 *refusée*, 212 *encaissée*. |
| **Spain** | **Factura rectificativa** (RD 1619/2012 art. 15) in a dedicated series, *por diferencias* or *por sustitución* | Under Verifactu: rectification types R1–R5 with `TipoRectificativa` I (diferencias) or S (sustitución), plus a **registro de anulación** and a *Subsanación* flag. Records are never deleted — the hash chain must stay intact. |
| **Belgium** | Credit note in the same format and channel as the original | No void mechanism. A misdirected invoice is booked and corrected by credit note. Rejection is signalled with the Peppol **Invoice Response** status `RE`. A 2026 credit note against a 2025 paper/PDF invoice may stay unstructured if the customer agrees. |
| **Greece** | Credit note type **5.1** (associated — must reference the original ΜΑΡΚ) or **5.2** (unassociated) | Cancellation uses the myDATA `CancelInvoice` method referencing the original ΜΑΡΚ; myDATA issues a **separate cancellation ΜΑΡΚ**. The original is neither deleted nor resubmitted. `[[UNVERIFIED: the current correction-window wording under A.1138/2020 as amended]]` |
| **Hungary** | Reported through the same RTIR channel: a modifying invoice via the `invoiceData` correction chain, or annulment of an erroneous *submission* via `invoiceAnnulment.xsd` | Annulment fixes a bad data submission; a wrong invoice is fixed by reporting a modifying invoice. Two different things. |
| **Romania** | Credit note transmitted through RO e-Factura like any other invoice | Same 5-working-day transmission deadline as originals since 2026-01-01 (OUG 89/2025). |

## Archiving

### The EU frame

- **Art 244**: every taxable person must store copies of invoices issued and all invoices received.
- **Art 245**: the taxpayer chooses the place of storage, provided the invoices are made available to the authorities without undue delay. Member States may require notification of a storage place outside their territory, and may require domestic storage where electronic storage does not guarantee full online access.
- **Art 246**: authenticity of origin, integrity of content and legibility must be guaranteed **throughout the storage period**, not only at issue.
- **Art 247(1)**: **each Member State determines the retention period.** There is no EU-wide number. Any source quoting one is wrong.
- **Art 247(2)**: Member States may require storage **in the original form in which the invoice was sent** — paper as paper, electronic as electronic. This is why archiving only the PDF rendition of an XML invoice is a defect.

### Retention periods

Verify against the entity's own tax adviser before relying on any of these; several are the general commercial-law period rather than a VAT-specific one, and the longer of the two binds.

| Country | Period | Basis |
|---|---|---|
| Belgium | **7 years** from 1 January of the year following the date of issue; 15 or 25 years for immovable business assets | Art 60 VAT Code (Circulars AAF 02/2013, AGFisc 14/2014). Must be kept in Belgium **unless** kept electronically with guaranteed full online access from Belgium. |
| France | **6 years** fiscal, **10 years** commercial — 10 is the operative floor | LPF art. L102 B; C. com. art. L123-22. The *plateforme agréée* is **not** required to archive; the duty stays with the company, in the original format. |
| Spain | **4 years** tax prescription, **6 years** commercial from the last book entry — 6 is the practical minimum; longer for investment goods and carried-forward losses | LGT art. 66; C. de Comercio art. 30. Verifactu records: same period as the invoice copies (Orden HAC/1177/2024 art. 8). |
| Portugal | **10 years** | DL 28/2019 art. 19 ff.; art. 52 CIVA. Storage anywhere in the **EU** with guaranteed online access for the AT; **outside the EU requires prior AT authorisation**. |
| Greece | **5 years** from the end of the fiscal year; **10 years** where the limitation period is extended; **20 years** in tax-evasion cases | Art 7 Law 4308/2014 |
| Hungary | **8 years** | Section 169 of the Accounting Act `[[UNVERIFIED: not confirmed against a NAV page]]` |
| Italy | *Conservazione a norma* is mandatory for issuer and recipient — a regulated process under the CAD, not a file copy. The Agenzia delle Entrate offers a free conservazione service through *Fatture e Corrispettivi* | Art 39 DPR 633/1972. `[[UNVERIFIED: the commonly quoted 10-year period and any qualified signature/time-stamp requirement — the AE page states neither]]` |
| Poland | KSeF itself stores accepted invoices `[[UNVERIFIED: the 10-year figure is from secondary sources only]]`. This does not discharge the taxpayer's own bookkeeping retention. | |
| Romania | Legea contabilității 82/1991 and OMFP 2634/2015; the archive artefact is the **ANAF-signed XML** | `[[UNVERIFIED: retention period not confirmed from a primary source]]` |
| Germany | **8 years** — "ein Doppel der Rechnung … sowie alle Rechnungen, die er erhalten … **acht Jahre** aufzubewahren", running from the end of the calendar year in which the invoice was issued. § 147 Abs 3 AO matches: Buchungsbelege 8 years (books, financial statements 10; other records 6). A private recipient of construction services under § 14 Abs 2 Satz 2 Nr 3 keeps 2 years | § 14b Abs 1 UStG, § 147 Abs 3 AO. Storage must be domestic, **unless** electronic storage guarantees full remote access, download and use — then storage elsewhere in the EU is allowed, with notification of the storage location to the Finanzamt (§ 14b Abs 2 UStG) |
| Switzerland | **10 years** | OR Art 958f |

### What to archive

Not the PDF. Archive, as one linked set:

1. the **exact bytes transmitted** — the XML, or the PDF/A-3 container for hybrid invoices
2. the **platform acknowledgement** — SdI receipt, KSeF number, ANAF signature, access point MDN/receipt, Peppol Invoice Response
3. the **validation result** at time of issue
4. the **human-readable rendition**, if one was produced and sent

Together these are the audit trail Art 233(1) asks for. Individually none of them is.

## Integrity and authenticity — and the signature myth

- **Art 229**: "Member States shall not require invoices to be signed." This is unambiguous and has not been amended.
- **Art 233(1)** as replaced by Directive 2010/45/EU: each taxable person determines how to ensure authenticity of origin, integrity of content and legibility; "this may be achieved by **any business controls which create a reliable audit trail** between an invoice and a supply of goods or services."
- **Art 233(2)**: an advanced electronic signature based on a qualified certificate, and EDI under Recommendation 1994/820/EC, are listed as **examples** of technologies that achieve this. Not requirements.

So: **no EU country requires a qualified electronic signature on a structured e-invoice.** What does exist, and gets misreported as a signature requirement:

- **Portugal**: for invoices that are *not* structured — PDFs — DL 28/2019 art. 12 requires a qualified electronic signature or seal, or EDI. The PDF tolerance has been extended repeatedly; the current end date is **2026-12-31** (Lei n.º 73-A/2025, Orçamento do Estado para 2026), after which a PDF invoice needs a qualified signature or seal. This is a rule about PDFs, not about EN 16931 invoices.
- **Spain**: **Facturae** for B2G must be **XAdES**-signed. That is a national format requirement for a national B2G channel, not an EU VAT requirement, and it does not extend to the Crea y Crece B2B formats (CII, UBL, EDIFACT, Facturae).
- **Italy**: the SdI applies a signature/receipt on acceptance. Supplier-side signature is not required for ordinary B2B FatturaPA.
- **Spain, non-Verifactu mode**: the SIF must sign records locally and keep an event log — a requirement on the *software*, not on the invoice.

A "business control creating a reliable audit trail" in practice: the invoice can be traced to an order and a delivery; the numbering is sequential and gapless; the transmitted bytes and the platform acknowledgement are stored together; access is restricted and logged. Write this down. An undocumented control is not a control.

## Checkpoints

- [ ] No code path edits an issued invoice
- [ ] Credit note and corrected invoice implemented as separate document types, with the correct type code
- [ ] Every correction references the original (BT-25 / BT-26 or the platform's own reference)
- [ ] Corrections go through the same channel as the original
- [ ] Country-specific mechanism used, not a generic credit note (TD04, faktura korygująca, factura rectificativa, avoir)
- [ ] No buyer-side correction note for Poland
- [ ] Original transmitted bytes archived, not the rendition
- [ ] Platform acknowledgement archived with the document
- [ ] Retention period confirmed per country with the tax adviser, longest applicable period used
- [ ] Storage location checked against the country's online-access condition
- [ ] Integrity control documented in writing
- [ ] No signature requirement asserted without naming the national rule that creates it
