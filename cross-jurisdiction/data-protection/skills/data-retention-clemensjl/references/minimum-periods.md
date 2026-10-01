# Statutory minimum retention periods

The floor, per jurisdiction. Verified against the official consolidated text where the source was reachable; everything else is marked. Status as at 05.08.2026.

These are the periods a controller must **not** fall below. They say nothing about how much longer data may be kept — that ceiling comes from Art 5(1)(e). Determine the jurisdiction from the place of establishment and the tax residence, never from where the server is.

**All periods below run from the end of a calendar year, not from `created_at`.** Building the job on row-creation timestamps under-retains by up to twelve months.

## Germany

| Record | Period | Citation |
|---|---|---|
| Bücher, Aufzeichnungen, Inventare, Jahresabschlüsse, Lageberichte, Eröffnungsbilanz; customs records | 10 years | § 147 Abs 3 S 1 iVm Abs 1 Nr 1, 4a AO |
| **Buchungsbelege** (accounting vouchers) | **8 years** | § 147 Abs 3 S 1 iVm Abs 1 Nr 4 AO |
| Handels- und Geschäftsbriefe, sonstige Unterlagen | 6 years | § 147 Abs 3 S 1 iVm Abs 1 Nr 2, 3, 5 AO |
| Same split under commercial law | 10 / 8 / 6 years | § 257 Abs 4 HGB |
| Invoices (issued and received) | 8 years | § 14b Abs 1 UStG |

§ 147 Abs 3 S 1 AO verbatim: *"Die in Absatz 1 Nummer 1 und 4a aufgeführten Unterlagen sind zehn Jahre, die in Absatz 1 Nummer 4 aufgeführten Unterlagen acht Jahre und die sonstigen in Absatz 1 aufgeführten Unterlagen sechs Jahre aufzubewahren"*.

Start of the period, § 147 Abs 4 AO: end of the calendar year in which the last entry was made, the inventory or annual accounts were drawn up, the commercial letter was sent or received, or **the Buchungsbeleg came into existence**. § 257 Abs 5 HGB is identical. § 14b Abs 1 UStG runs from the end of the calendar year in which the invoice was issued.

Shorter periods under non-tax statutes do not shorten the tax period (§ 147 Abs 3 S 2 AO).

**The 2025 change.** The eight-year period applies from 01.01.2025 to every document whose period under the version in force until 31.12.2024 had not yet expired (Art 97 § 19a Abs 2 EGAO). So vouchers from 2018 onward were still live on 01.01.2025 and moved from ten years to eight; anything older stayed expired.

**The supervised-entity carve-out.** Art 97 § 19a Abs 3 EGAO: for taxpayers that are institutions within § 1 Abs 1b KWG (including branches under § 53 KWG), undertakings supervised under § 1 Abs 1 VAG, or securities institutions under § 2 Abs 1 WpIG, § 147 Abs 3 S 1 AO **in its 31.12.2024 version** applies — i.e. ten years for Buchungsbelege. § 257 Abs 4 HGB carries the same exception for banks, insurers and securities institutions. If the intake says "regulated financial entity", do not apply the eight-year number.

## Austria

| Record | Period | Citation |
|---|---|---|
| Bücher, Aufzeichnungen and the associated Belege | 7 years | § 132 Abs 1 BAO |
| Bücher, Inventare, Eröffnungsbilanzen, Jahresabschlüsse, Lageberichte, Konzernabschlüsse, received and sent Geschäftsbriefe, Buchungsbelege | 7 years | § 212 Abs 1 UGB |

§ 132 Abs 1 BAO: seven years, *"darüber hinaus sind sie noch so lange aufzubewahren, als sie für die Abgabenerhebung betreffende anhängige Verfahren von Bedeutung sind"*. § 212 Abs 1 UGB carries the parallel extension for pending court or administrative proceedings in which the undertaking is a party.

Start, § 212 Abs 2 UGB: end of the calendar year for which the last entry was made, the inventory drawn up, the annual accounts adopted, or the business letter sent or received.

Electronic storage is permitted where complete, ordered, content-identical and true-to-original reproduction is guaranteed for the whole period (§ 132 Abs 2 BAO).

The **open-ended extension for pending proceedings** is the practical trap: it cannot be expressed as a fixed number and must be implemented as a litigation hold that suspends the job, not as a longer constant.

## France

Verified against entreprendre.service-public.gouv.fr (official government guidance), fiche F10029.

| Record | Period | Citation |
|---|---|---|
| Livres et registres comptables (livre journal, grand livre, livre d'inventaire) | 10 years from the close of the financial year | Code de commerce, art. L123-22 |
| Pièces justificatives (bon de commande, de livraison, facture client et fournisseur) | 10 years from the close of the financial year | Code de commerce, art. L123-22 |
| Fiscal supporting documents | 6 years from the last recorded transaction or the date of the document, whichever is later; extended to 10 years for undeclared activity or fraud | Livre des procédures fiscales, art. L102 B |
| Commercial contracts, invoices, commercial correspondence | 5 years | Code de commerce, art. L110-4 |
| Bulletins de paie (employer copy) | 5 years | Code du travail, art. L3243-1 to L3243-5 |
| Registre unique du personnel entries | 5 years after the employee leaves | Code du travail |

The 10-year accounting duty and the 6-year fiscal duty overlap rather than replace each other; the schedule takes the longer of the two per element.

## Italy

| Record | Period | Citation |
|---|---|---|
| Scritture contabili, invoices received, letters and telegrams received, copies of invoices, letters and telegrams sent | 10 years from the date of the last entry | art. 2220 Codice Civile |

*"Le scritture devono essere conservate per dieci anni dalla data dell'ultima registrazione."* Storage on digital imaging media is permitted where the records remain legible and correspond to the originals.

**The tax rule has no fixed number and overrides the civil one.** Art. 22 comma 2 DPR 600/1973, consolidated text read on normattiva.it 05.08.2026: *"Le scritture contabili obbligatorie ai sensi del presente decreto, di altre leggi tributarie, del codice civile o di leggi speciali devono essere conservate fino a quando non siano definiti gli accertamenti relativi al corrispondente periodo d'imposta **anche oltre il termine stabilito dall'articolo 2220 del codice civile** o da altre leggi tributarie."*

Consequences for a retention schedule:

- **Ten years is a floor, not a ceiling.** Where an assessment for the corresponding tax period is still open, the duty runs on past the art. 2220 CC period. A schema that hard-codes 10 years and deletes will destroy records the taxpayer is still obliged to hold.
- Model this as a **legal hold keyed to the tax period**, not as a longer fixed number. The same comma lets the court hearing a dispute limit the duty to the records relevant to that dispute — so the hold is scopeable, but only by a court.
- Comma 3 extends the same deadline to the originals of letters, telegrams and invoices **received**, and copies of those sent, kept in order **per affare**.
- Comma 2 also requires that mechanographic and electronic media be kept until the accounting data on them has been printed into the statutory books and registers.

`[[UNVERIFIED: the conservazione sostitutiva period for electronic invoices routed through the Sistema di Interscambio — verify against Agenzia delle Entrate guidance]]`

## United Kingdom

| Record | Period | Citation |
|---|---|---|
| Accounting records, **private** company | 3 years from the date on which they are made | Companies Act 2006, s 388(4)(a) |
| Accounting records, **public** company | 6 years from the date on which they are made | Companies Act 2006, s 388(4)(b) |

s 388(4) verbatim: *"Accounting records that a company is required by section 386 to keep must be preserved by it — (a) in the case of a private company, for three years from the date on which they are made; (b) in the case of a public company, for six years from the date on which they are made."* Subject to insolvency rules under s 411 Insolvency Act 1986 (s 388(5)).

Note that s 388 runs from the date the record was made, not from a year-end — the only major jurisdiction in this file that does.

`[[UNVERIFIED: HMRC periods — Corporation Tax (FA 1998 Sch 18 para 21), Self Assessment for the self-employed, VAT records under the VAT Regulations 1995, and PAYE records. gov.uk and ico.org.uk return 403 to automated fetches; verify each against the HMRC manual before publishing a number]]`

`[[UNVERIFIED: whether the Data (Use and Access) Act 2025 altered anything in the UK GDPR erasure or storage-limitation provisions]]`

## Switzerland

Verified 05.08.2026 against the fedlex PDF/A of the consolidated texts (the HTML pages are JavaScript-only; the `filestore/…/pdf-a/…pdf` path serves the real text).

| Record | Period | Provision |
|---|---|---|
| Geschäftsbücher, Buchungsbelege, Geschäftsbericht, Revisionsbericht | **10 years**, running **from the end of the financial year** | Art 958f Abs 1 OR |
| VAT: Geschäftsbücher, Belege, Geschäftspapiere and other records | **until absolute Verjährung of the tax claim** (Art 42 Abs 6 MWSTG), Art 958f OR expressly reserved | Art 70 Abs 2 MWSTG |
| Records needed for Einlageentsteuerung and Eigenverbrauch of **immovable** property | **20 years** | Art 70 Abs 3 MWSTG, referring to Art 31 Abs 3 and 32 Abs 2 |

Art 958f Abs 1 OR verbatim: *"Die Geschäftsbücher und die Buchungsbelege sowie der Geschäftsbericht und der Revisionsbericht sind während zehn Jahren aufzubewahren. Die Aufbewahrungsfrist beginnt mit dem Ablauf des Geschäftsjahres."*

Three details that decide the implementation:

- **The clock starts at the end of the financial year, not at the document date.** A retention job keyed on `created_at + 10y` deletes early for anything created in the first months of a financial year.
- **Geschäftsbericht and Revisionsbericht must be kept in written and signed form** (Art 958f Abs 2 OR). Electronic-only is not compliant for those two, unlike the books and vouchers, which Abs 3 expressly allows on paper, electronically or in a comparable way — provided the correspondence with the underlying transactions is assured and they can be made legible again at any time.
- **The 20-year property window is not a "longer period" in the abstract** — it attaches to the documents needed for the input-tax and own-use calculations on immovable property, so it is a per-document-class flag, not a per-entity setting.

## United States

Federal tax, verified against irs.gov "How long should I keep records":

| Situation | Period |
|---|---|
| Default | 3 years |
| Claim for credit or refund after filing | later of 3 years from filing or 2 years from paying the tax |
| Income understated by more than 25% of gross income shown | 6 years |
| Claim for a loss from worthless securities or bad-debt deduction | 7 years |
| No return filed, or fraudulent return | indefinite |
| Employment tax records | at least 4 years after the tax becomes due or is paid, whichever is later |

The IRS frames all of these as running to the expiry of the period of limitations for the return, not as fixed retention rules.

`[[UNVERIFIED: FLSA payroll records — 3 years under 29 CFR 516.5 and 2 years for supplementary basic records under 29 CFR 516.6. ecfr.gov and dol.gov both refuse automated fetches; verify before publishing]]`

`[[UNVERIFIED: SEC Rule 17a-4 electronic recordkeeping tiers and the 2022 amendment introducing the audit-trail alternative to WORM]]`

`[[UNVERIFIED: HIPAA § 164.316(b)(2)(i) six-year documentation retention — note that this covers HIPAA documentation, not medical records, which are governed by state law]]`

`[[UNVERIFIED: CCPA/CPRA retention-disclosure duty under Cal. Civ. Code § 1798.100(a)(3) and the deletion right under § 1798.105, including the exception where retention is required by law]]`

## Australia

`[[UNVERIFIED: Corporations Act 2001 (Cth) s 286 — financial records retained 7 years after the transactions covered by the records are completed. legislation.gov.au and austlii both return 403 to automated fetches; verify against the Federal Register of Legislation before stating it]]`

`[[UNVERIFIED: the ATO five-year general record-keeping rule and the point it runs from]]`

`[[UNVERIFIED: employee records under the Fair Work Regulations 2009 (commonly cited as 7 years)]]`

`[[UNVERIFIED: APP 11.2 (Privacy Act 1988) duty to destroy or de-identify personal information no longer needed, and any change under the Privacy and Other Legislation Amendment Act 2024]]`

## Invoices specifically

Invoices attract their own rule in several jurisdictions and it does not always match the general accounting period:

| Jurisdiction | Invoice period | Citation |
|---|---|---|
| Germany | 8 years from end of the year of issue | § 14b Abs 1 UStG |
| Austria | 7 years (as Belege) | § 132 Abs 1 BAO, § 212 Abs 1 UGB |
| France | 10 years as pièce justificative; 5 years as commercial document | C. com. L123-22, L110-4 |
| Italy | 10 years from last entry | art. 2220 CC |

## Checkpoints

- [ ] Jurisdiction determined from establishment and tax residence, not server location
- [ ] Supervised-entity status checked before applying the German 8-year period
- [ ] Period start implemented as end-of-calendar-year, not `created_at` (except UK s 388)
- [ ] Pending-proceedings extension (§ 132 BAO, § 212 UGB) implemented as a litigation hold
- [ ] Invoice-specific period applied where it differs from the general accounting period
- [ ] Every `[[UNVERIFIED: …]]` in this file resolved against the primary source before a number reaches a published schedule
- [ ] Tax adviser has confirmed the applicable set for this entity
