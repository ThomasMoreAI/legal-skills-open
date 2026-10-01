# Internal data protection duties

These obligations are not published on the website. They are what a supervisory authority asks for first, and their absence is the most common finding in a German DPA audit. Status as at 05.08.2026.

## Datenschutzbeauftragter — § 38 BDSG

**§ 38 Abs 1 Satz 1 BDSG:** a non-public body must appoint a Datenschutzbeauftragter where it **regularly employs at least 20 persons permanently in the automated processing of personal data**.

The threshold was **raised from 10 to 20** by the Zweites Datenschutz-Anpassungs- und Umsetzungsgesetz EU. Any text still citing 10 is out of date.

Counting: heads, not full-time equivalents. Working students, part-timers, freelancers integrated into the workflow and Geschäftsführer count if they work with personal data on a computer — which in practice means anyone using e-mail or a CRM.

**§ 38 Abs 1 Satz 2 BDSG:** irrespective of headcount, an appointment is mandatory where the body

- carries out processing subject to a Datenschutz-Folgenabschätzung under Art 35 DSGVO, or
- processes personal data commercially for the purpose of transfer, of anonymised transfer, or for market or opinion research.

Art 37 Abs 1 DSGVO applies on top: public authority, core activity involving regular and systematic monitoring on a large scale, or large-scale processing of Art 9 or Art 10 data.

Where appointed, the contact details go into the Datenschutzerklärung (Art 13 Abs 1 lit b DSGVO) and are notified to the competent supervisory authority (Art 37 Abs 7 DSGVO). Where not appointed, do not write "Datenschutzbeauftragter: Herr X" for a person who is merely the internal contact — that is a misstatement with liability attached.

## Verzeichnis von Verarbeitungstätigkeiten — Art 30 DSGVO

Mandatory content per Art 30 Abs 1 DSGVO: controller and contact, purposes, categories of data subjects and data, categories of recipients including third-country recipients, third-country transfers with safeguards, erasure deadlines, general description of the technical and organisational measures.

The Art 30 Abs 5 exemption for bodies with fewer than 250 employees almost never applies: it falls away where processing is not occasional, where it risks the rights of data subjects, or where Art 9 or Art 10 data are involved. A webshop or a newsletter is not occasional. Assume the register is required.

Format is free. A spreadsheet with one row per processing operation and the columns above is sufficient and is what authorities send their questionnaires against.

## Auftragsverarbeitung — Art 28 DSGVO

Every processor needs a written or electronic contract with the content of Art 28 Abs 3 DSGVO. Typical processors that get forgotten: hoster, CDN, backup provider, mail-delivery service, newsletter tool, analytics, error tracking, ticketing system, cloud storage, external bookkeeping where it touches personal data.

Not processors, and therefore wrongly papered with an AVV: payment service providers acting as independent controllers, tax advisers, banks, postal and parcel carriers as far as they perform the carriage contract. Joint controllership under Art 26 DSGVO needs its own agreement and a published summary of the essentials.

Sub-processors require the general or specific authorisation under Art 28 Abs 2 DSGVO plus notice of changes.

## Technische und organisatorische Maßnahmen — Art 32 DSGVO

Document per system: access control, encryption in transit and at rest, pseudonymisation, backup and restore with a tested restore, logging, patch process, role and rights concept, offboarding, physical security. § 64 BDSG contains a detailed measures catalogue for the law-enforcement regime; it is useful as a checklist even where it does not directly apply.

## Datenpanne — Art 33, Art 34 DSGVO

- Notification to the competent supervisory authority within **72 hours** of becoming aware, unless the breach is unlikely to result in a risk (Art 33 Abs 1 DSGVO). The competent authority is the **Landesdatenschutzbehörde** of the place of establishment; most run an online reporting form.
- Notification to the data subjects without undue delay where the breach is likely to result in a **high** risk (Art 34 Abs 1 DSGVO).
- Internal documentation of every breach including those not notified (Art 33 Abs 5 DSGVO).

Have the process written down before it is needed: who decides, who notifies, which form, where the log lives. 72 hours includes weekends.

## Datenschutz-Folgenabschätzung — Art 35 DSGVO

Required where processing is likely to result in a high risk. The German DPAs publish a **Muss-Liste** of processing operations always requiring a DSFA under Art 35 Abs 4 DSGVO; the lists are published per Land and differ slightly. Typical triggers relevant to online projects: extensive profiling, large-scale tracking across services, biometric identification, processing of Art 9 data at scale, systematic monitoring of publicly accessible areas.

## Löschkonzept

Retention periods that override the erasure obligation: § 147 AO (accounting records, invoices) and § 257 HGB (Handelsbücher, Geschäftsbriefe). **The period is per document class, not a single number.** Both statutes, read on gesetze-im-internet.de on 05.08.2026:

| Document class | Period | Provision |
|---|---|---|
| Bücher, Aufzeichnungen, Inventare, Jahresabschlüsse, Lageberichte, Eröffnungsbilanz and the related Arbeitsanweisungen | **10 years** | § 147 Abs 3 iVm Abs 1 Nr 1 AO; § 257 Abs 4 iVm Abs 1 Nr 1 HGB |
| Zollunterlagen under Art 15 Abs 1 and Art 163 UZK | **10 years** | § 147 Abs 3 iVm Abs 1 Nr 4a AO |
| **Buchungsbelege** — the class that actually turns up in an erasure request | **8 years** | § 147 Abs 3 iVm Abs 1 Nr 4 AO; § 257 Abs 4 iVm Abs 1 Nr 4 HGB |
| Received and sent Handels- und Geschäftsbriefe, and all other Abs 1 material | **6 years** | § 147 Abs 3 AO; § 257 Abs 4 HGB |

§ 147 Abs 3 Satz 1 AO verbatim: *"Die in Absatz 1 Nummer 1 und 4a aufgeführten Unterlagen sind zehn Jahre, die in Absatz 1 Nummer 4 aufgeführten Unterlagen acht Jahre und die sonstigen in Absatz 1 aufgeführten Unterlagen sechs Jahre aufzubewahren"*. § 257 Abs 4 HGB is drafted identically.

Two traps that produce wrong numbers in real texts:

- **Buchungsbelege are eight years, not ten.** The shortening applies from 01.01.2025 to every document whose period had not yet expired on 31.12.2024 (Art 97 § 19a Abs 2 EGAO). Invoices likewise: § 14b Abs 1 Satz 1 UStG says *acht Jahre*, running from the end of the calendar year of issue. A privacy notice still promising ten years for invoices is over-retaining and says so in writing.
- **Financial-sector exception.** Credit institutions (§ 1 Abs 1b KWG), undertakings supervised under § 1 Abs 1 VAG and securities institutions (§ 2 Abs 1 WpIG) keep applying the version in force on 31.12.2024, i.e. **ten years** for Buchungsbelege (Art 97 § 19a Abs 3 EGAO).
- **Never copy the German number into an Austrian text.** Austria is seven years throughout (§ 132 Abs 1 BAO, § 212 Abs 1 UGB).

## Template — Verarbeitungsverzeichnis row

One row per processing operation. Columns follow Art 30 Abs 1 DSGVO literally so that a DPA questionnaire can be answered by copying.

| Field | Value |
|---|---|
| Bezeichnung der Verarbeitung | `[[e.g. Newsletterversand]]` |
| Verantwortlicher, Kontakt | `[[Firma, Anschrift, E-Mail]]` |
| Datenschutzbeauftragter | `[[contact — or: nicht bestellt, § 38 Abs. 1 BDSG nicht erfüllt]]` |
| Zweck | `[[purpose]]` |
| Rechtsgrundlage | `[[Art. 6 Abs. 1 lit. … DSGVO]]` |
| Kategorien betroffener Personen | `[[e.g. Newsletter-Abonnenten]]` |
| Kategorien personenbezogener Daten | `[[e.g. E-Mail-Adresse, Anmeldezeitpunkt, IP]]` |
| Kategorien von Empfängern | `[[processor, with role]]` |
| Drittlandübermittlung | `[[country and instrument — or: keine]]` |
| Löschfrist | `[[period or criterion]]` |
| TOM (allgemeine Beschreibung) | `[[reference to the TOM document]]` |

## Template — internal breach log entry

```text
<!-- ENTWURF – juristisch nicht freigegeben -->
Vorfall-ID:                [[id]]
Bekannt geworden am/um:    [[date, time]] — 72-Stunden-Frist endet [[date, time]]
Beschreibung:              [[what happened]]
Kategorien Betroffener:    [[categories]] · Ungefähre Zahl: [[number]]
Kategorien der Daten:      [[categories]] · Ungefähre Zahl der Datensätze: [[number]]
Wahrscheinliche Folgen:    [[assessment]]
Ergriffene Maßnahmen:      [[containment, mitigation]]
Risikobewertung:           kein Risiko / Risiko / hohes Risiko — Begründung: [[reason]]
Meldung Aufsichtsbehörde:  ja/nein (Art. 33 DSGVO) — [[authority, date, reference]]
Benachrichtigung Betroffene: ja/nein (Art. 34 DSGVO) — [[date, channel, wording]]
Dokumentiert nach Art. 33 Abs. 5 DSGVO durch: [[name, date]]
```

## Two roles that get mislabelled

- **Joint controllership, Art 26 DSGVO.** Where purposes and means are determined jointly — social plugins, some analytics configurations, joint campaigns — an Art 26 arrangement is needed and its essence must be made available to data subjects. An AVV is the wrong instrument and does not cure the gap.
- **Representative in the Union, Art 27 DSGVO.** A controller established outside the EU that offers goods or services to persons in the EU must designate a representative in writing in a member state where those persons are, and name it in the privacy notice. German subsidiaries of foreign groups regularly omit this.

## Checkpoints

- [ ] Headcount counted against the § 38 Abs 1 BDSG threshold of 20, result documented
- [ ] § 38 Abs 1 Satz 2 BDSG triggers checked independently of headcount
- [ ] Where appointed: DPO notified to the supervisory authority and named in the Datenschutzerklärung
- [ ] Verarbeitungsverzeichnis exists and covers every processing operation in the public declaration
- [ ] AVV in place for every processor; nothing papered as an AVV that is really joint or independent controllership
- [ ] Third-country transfers backed by an instrument and a documented assessment
- [ ] TOM documented per system, restore tested at least once
- [ ] Breach process written down with named roles, the correct Landesbehörde and its reporting form
- [ ] DSFA screening performed against the competent DPA's Muss-Liste
- [ ] Erasure concept exists and reconciles the retention periods with Art 17 DSGVO
