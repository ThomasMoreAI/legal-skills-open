---
name: casp-zulassung-uebergang-borghei
title: /krypto-mikar:casp-zulassung-uebergang
description: Zulassung als Anbieter von Kryptowerte-Dienstleistungen und deutsches Übergangsrecht – Zulassungserfordernis Art. 59 VO (EU) 2023/1114, Erbringung durch bestimmte Finanzunternehmen mit Anzeige nach Art. 60, Antrag Art. 62 und Prüfung Art. 63, Unternehmensführung Art. 68, sichere Aufbewahrung von Kundenwerten Art. 70, Verwahrdienstleistung Art. 75, unionsrechtliches Übergangsrecht Art. 143 Abs. 3 bis zum 01.07.2026 mit ausdrücklicher Verkürzungsbefugnis der Mitgliedstaaten und die deutsche Verkürzung in § 50 Abs. 2 Nr. 3 KMAG auf den Ablauf des 31.12.2025, vereinfachtes Verfahren § 50 Abs. 3 KMAG, Anzeigepflicht § 50 Abs. 4 KMAG, digitale operationale Resilienz § 26 KMAG sowie Einschreiten gegen unerlaubte Geschäfte § 9 KMAG. Use when eine CASP-Zulassung zu beantragen, ein Bestandsgeschäft zu überführen oder ein Vorwurf unerlaubter Geschäfte abzuwehren ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/krypto-mikar/skills/casp-zulassung-uebergang
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: finance
language: de
---

# /krypto-mikar:casp-zulassung-uebergang

## Zweck

Der Skill klärt, ob und wie ein Unternehmen Kryptowerte-Dienstleistungen erbringen darf — und beantwortet die Frage, die in Deutschland 2026 die meisten Mandate auslöst: **Wie lange durfte Bestandsgeschäft ohne MiCAR-Zulassung weiterlaufen?** Die Antwort weicht vom Unionsrecht ab, weil Deutschland die Übergangsfrist verkürzt hat.

## Eingaben

- Erbrachte Dienstleistungen: Verwahrung, Betrieb einer Handelsplattform, Tausch, Ausführung, Platzierung, Annahme und Übermittlung von Aufträgen, Beratung, Portfolioverwaltung, Transfer
- Bestehende Erlaubnisse: KWG, WpIG, ZAG, BörsG, KAGB
- Seit wann die Tätigkeit erbracht wird; Stand am 29.12.2024
- Ob und wann ein Zulassungsantrag gestellt wurde und wie das Verfahren steht
- Gesellschaftsrechtliche Struktur, Geschäftsleitung, Eigenmittel
- Verwahrmodell für Kundenwerte und Trennung vom Eigenvermögen
- Ob die BaFin bereits Maßnahmen angekündigt oder erlassen hat

## Sub-Agent-Architektur

Der Researcher beschafft MiCAR Titel V, Art. 143, das KMAG einschließlich § 50 und die BaFin-Verlautbarungen zum Zulassungs- und zum vereinfachten Verfahren. Der Drafter erstellt die Zulassungs- oder Überleitungsstrategie. Der Reviewer prüft vor allem eines: dass **nicht** mit der unionsrechtlichen Frist des Art. 143 Abs. 3 gerechnet wird, wo § 50 Abs. 2 Nr. 3 KMAG früher endet.

## Ablauf

### 1. Dienstleistung und Zulassungserfordernis bestimmen (Art. 59 MiCAR)

Kryptowerte-Dienstleistungen dürfen nur erbracht werden von

- **Art. 59 Abs. 1 Buchst. a** — juristischen Personen mit **Zulassung als Anbieter von Kryptowerte-Dienstleistungen** nach Art. 63, oder
- **Art. 59 Abs. 1 Buchst. b** — bestimmten **Finanzunternehmen**, die nach **Art. 60** lediglich eine **Anzeige** erstatten, soweit die Dienstleistung von ihrer bestehenden Erlaubnis gedeckt ist.

Die Unterscheidung entscheidet über Verfahren, Dauer und Kosten: Kreditinstitute, Wertpapierfirmen, E-Geld-Institute, Zahlungsinstitute, OGAW- und AIF-Verwaltungsgesellschaften sowie Marktbetreiber können unter den Voraussetzungen des Art. 60 den **Anzeigeweg** gehen; alle übrigen benötigen die **Vollzulassung**.

Das Antragsverfahren richtet sich nach **Art. 62**, die Prüfung und die Entscheidung nach **Art. 63**; Fristen und Vollständigkeitsanforderungen sind dort geregelt und im konkreten Verfahren am Wortlaut nachzuhalten `[unverifiziert – prüfen]`.

### 2. Das deutsche Übergangsrecht — die entscheidende Abweichung

**Unionsrecht (Art. 143 Abs. 3 MiCAR):** Anbieter, die ihre Dienste nach geltendem Recht **vor dem 30.12.2024** erbracht haben, dürfen damit **bis zum 1. Juli 2026** fortfahren — oder bis zur Entscheidung nach Art. 63, je nachdem, was **zuerst** eintritt. Ausdrücklich vorgesehen ist, dass die **Mitgliedstaaten** die Übergangsregelung **nicht in Anspruch nehmen oder ihre Geltungsdauer verkürzen** können.

**Deutschland hat verkürzt.** [§ 50 KMAG](https://www.gesetze-im-internet.de/kmag/__50.html) ordnet an:

- **Abs. 1** — Unternehmen mit einer Erlaubnis nach § 32 KWG, § 15 WpIG, § 11 Abs. 1 ZAG, als Börsenträger nach § 4 BörsG in den Fällen des § 2 Abs. 12 KWG oder als OGAW- bzw. AIF-Kapitalverwaltungsgesellschaft nach § 20 Abs. 1 KAGB, die am **29.12.2024** im Einklang mit geltendem Recht Tätigkeiten in Bezug auf Kryptowerte erbringen durften, dürfen diese Tätigkeit **unter Fortgeltung der aufsichtlichen Rechtslage vom 29.12.2024** weiter erbringen; die Erlaubnis gilt insoweit als fortbestehend.
- **Abs. 2** — Diese fortbestehende Erlaubnis **erlischt**
  1. in den Fällen des Art. 59 Abs. 1 Buchst. a mit **Bestandskraft** der Entscheidung im Zulassungsverfahren nach Art. 63 oder im vereinfachten Verfahren nach Abs. 3,
  2. in den Fällen des Art. 59 Abs. 1 Buchst. b mit Ablauf der jeweils einschlägigen Frist nach Art. 60, oder
  3. **spätestens mit Ablauf des 31. Dezember 2025**.

> **Wer in Deutschland mit dem 1. Juli 2026 rechnet, rechnet sechs Monate falsch.** Die deutsche Übergangsfrist endete nach § 50 Abs. 2 Nr. 3 KMAG bereits am **31.12.2025**. Wer seither ohne Zulassung oder ohne wirksame Anzeige tätig ist, betreibt **unerlaubte Geschäfte** mit den Folgen der §§ 9, 10 KMAG.

- **Abs. 3** — **Vereinfachtes Verfahren**: Unternehmen nach Abs. 1 Nr. 1 (KWG-Erlaubnis) können es beschreiten; Unternehmen nach Abs. 1 Nr. 2 (WpIG-Erlaubnis), soweit sie nicht unter Art. 60 fallen. Die Zulassung **ist zu verweigern**, wenn die Voraussetzungen des Titels V nicht erfüllt sind; die BaFin kann sie **unter Auflagen** erteilen, die sich im Rahmen des Verordnungszwecks halten müssen.
- **Abs. 4** — Unternehmen, die nach Art. 143 Abs. 3 MiCAR bislang **erlaubnisfreie** Tätigkeiten erbracht haben, hatten ihre Tätigkeit der BaFin **bis zum 1. August 2024 formlos anzuzeigen**.
- **Abs. 5** — Verordnungsermächtigung des BMF im Benehmen mit der Deutschen Bundesbank.

### 3. Folgen fehlender Zulassung ([§ 9](https://www.gesetze-im-internet.de/kmag/__9.html), [§ 10 KMAG](https://www.gesetze-im-internet.de/kmag/__10.html))

Die BaFin kann die **sofortige Einstellung des Geschäftsbetriebs** und die **unverzügliche Abwicklung** anordnen — gegenüber dem Unternehmen, **seinen Gesellschaftern und den Mitgliedern seiner Organe**. Maßnahmen nach dem KMAG sind nach [§ 5 KMAG](https://www.gesetze-im-internet.de/kmag/__5.html) **sofort vollziehbar**; ein Rechtsbehelf hat keine aufschiebende Wirkung.

Hinzu treten die **Straf- und Bußgeldvorschriften** der [§§ 46](https://www.gesetze-im-internet.de/kmag/__46.html), [47 KMAG](https://www.gesetze-im-internet.de/kmag/__47.html) sowie zivilrechtliche Folgen gegenüber Kunden. Die Abwicklungsanordnung trifft in der Praxis die Verfügungsgewalt über Kundenbestände und ist deshalb existenzgefährdend — sie ist der Grund, warum die Überleitung nicht aufgeschoben werden darf.

### 4. Laufende Pflichten nach Zulassung

| Norm | Pflicht |
|---|---|
| **Art. 68** | Regelungen zur **Unternehmensführung** — Geschäftsleitung, Eignung, Organisation, Interessenkonflikte |
| **Art. 70** | **Sichere Aufbewahrung** der Kryptowerte und Geldbeträge von Kunden — Trennung vom Eigenvermögen |
| **Art. 75** | Besondere Anforderungen an die **Verwahrung und Verwaltung** von Kryptowerten für Kunden |
| **[§ 26 KMAG](https://www.gesetze-im-internet.de/kmag/__26.html)** | **Digitale operationale Resilienz** — Schnittstelle zu DORA (`/dora:ikt-drittparteienrisiko`) |
| **[§§ 20, 21 KMAG](https://www.gesetze-im-internet.de/kmag/__20.html)** | Auskünfte und Prüfungen; Anzeige- und Meldewesen |
| **[§§ 22 bis 25 KMAG](https://www.gesetze-im-internet.de/kmag/__22.html)** | Maßnahmen gegenüber Organen, Abberufung, Übernahme von Instituten |
| **[§§ 37 bis 40 KMAG](https://www.gesetze-im-internet.de/kmag/__37.html)** | Rechnungslegung, Jahresabschluss, Abschlussprüfer |
| **[§§ 41 bis 45 KMAG](https://www.gesetze-im-internet.de/kmag/__41.html)** | Eigenmittel, organisatorische Mängel, einstweilige Maßnahmen, Insolvenz, Aussonderung verwahrter Kryptowerte |

**§ 45 KMAG** — Zuordnung verwahrter Kryptowerte und Kosten der Aussonderung — ist die insolvenzrechtliche Kernnorm für Kundenbestände und in jedem Verwahrmandat zu prüfen.

## Deterministische Berechnung

Die Übergangsfristen sind der Kern dieses Skills. Der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) macht nur die Arithmetik — welche Frist gilt, ist die juristische Frage:

```bash
# Deutsche Höchstgrenze § 50 Abs. 2 Nr. 3 KMAG: Ablauf des 31.12.2025 (Fixdatum).
# NICHT der 01.07.2026 aus Art. 143 Abs. 3 MiCAR - Deutschland hat verkuerzt.

# Dauer unerlaubter Tätigkeit seit Fristablauf, für die Risikobewertung
python -m scripts.legal_calc.cli frist --ereignis 31.12.2025 --menge 12 --einheit monate --land HE

# Verfolgungsverjährung einer Ordnungswidrigkeit nach § 47 KMAG iVm § 31 OWiG
python -m scripts.legal_calc.cli frist --ereignis 31.12.2025 --menge 3 --einheit jahre --land HE

# Rechtsbehelfsfrist gegen eine Maßnahme der BaFin (ohne aufschiebende Wirkung, § 5 KMAG)
python -m scripts.legal_calc.cli frist --ereignis 15.09.2026 --menge 1 --einheit monate --land HE
```

## Quellen

### Rechtsakte

- Verordnung (EU) 2023/1114 (MiCAR), Art. 59, 60, 62, 63, 68, 70, 75, 143 — [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2023/1114/oj)
- [KMAG](https://www.gesetze-im-internet.de/kmag/) – [§ 5](https://www.gesetze-im-internet.de/kmag/__5.html), [§ 9](https://www.gesetze-im-internet.de/kmag/__9.html), [§ 10](https://www.gesetze-im-internet.de/kmag/__10.html), [§ 20](https://www.gesetze-im-internet.de/kmag/__20.html), [§ 26](https://www.gesetze-im-internet.de/kmag/__26.html), [§ 45](https://www.gesetze-im-internet.de/kmag/__45.html), [§ 46](https://www.gesetze-im-internet.de/kmag/__46.html), [§ 47](https://www.gesetze-im-internet.de/kmag/__47.html), [§ 50 KMAG](https://www.gesetze-im-internet.de/kmag/__50.html)
- [§ 32 KWG](https://www.gesetze-im-internet.de/kredwg/__32.html), [§ 15 WpIG](https://www.gesetze-im-internet.de/wpig/__15.html), [§ 11 ZAG](https://www.gesetze-im-internet.de/zag_2018/__11.html), [§ 20 KAGB](https://www.gesetze-im-internet.de/kagb/__20.html)
- Verordnung (EU) 2022/2554 (DORA) — [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2022/2554/oj)
- [§ 31 OWiG](https://www.gesetze-im-internet.de/owig_1968/__31.html)

### Kommentare und Literatur

- Maume/Maute, MiCAR, Kommentar, Titel V `[unverifiziert – prüfen]`
- Kommentierungen zum KMAG (Erscheinungsstand prüfen) `[unverifiziert – prüfen]`
- BaFin, Merkblätter zum Zulassungsverfahren nach der MiCAR und zum vereinfachten Verfahren nach § 50 Abs. 3 KMAG.
- Boos/Fischer/Schulte-Mattler, KWG, § 32 (unerlaubte Geschäfte als Vergleichsmaßstab).

### Rechtsprechung

Zur MiCAR und zum KMAG liegt **keine** gefestigte Rechtsprechung vor. Zur Anordnung der Einstellung und Abwicklung unerlaubter Geschäfte besteht Judikatur zu § 37 KWG, die als Auslegungshilfe dienen kann; jede konkrete Entscheidung ist vor Verwendung in juris oder Beck-Online zu verifizieren; ohne Beleg gilt sie als `[unverifiziert – prüfen]`.

## Ausgabeformat

```
CASP-ZULASSUNG / ÜBERGANG — <Mandant> — <Datum>

I.   Dienstleistungen
     Erbracht:                <Verwahrung / Handelsplattform / Tausch / Ausführung / Beratung / …>
     Seit:                    <Datum>   Stand am 29.12.2024: <…>

II.  Weg zur Erlaubnis
     Art. 59 Abs. 1 Buchst. a — Vollzulassung Art. 62, 63: [einschlägig / nein]
     Art. 59 Abs. 1 Buchst. b — Anzeige nach Art. 60:      [einschlägig / nein]
     Bestehende Erlaubnis:    <§ 32 KWG / § 15 WpIG / § 11 ZAG / § 4 BörsG / § 20 KAGB>
     Vereinfachtes Verfahren § 50 Abs. 3 KMAG: [offen / nicht eröffnet]

III. Übergangsrecht — KRITISCH
     Art. 143 Abs. 3 MiCAR:   01.07.2026 (unionsrechtlich)
     § 50 Abs. 2 Nr. 3 KMAG:  Ablauf des 31.12.2025 — DEUTSCHLAND HAT VERKÜRZT
     Maßgeblich:              31.12.2025
     Erlöschensgrund Abs. 2:  [Nr. 1 Bestandskraft / Nr. 2 Frist Art. 60 / Nr. 3 Fixdatum]
     Anzeige Abs. 4 (bis 01.08.2024): [erstattet / versäumt]
     Status seit Fristablauf: [zugelassen / unerlaubt tätig seit <Datum>]

IV.  Risiko unerlaubter Geschäfte
     § 9 KMAG:                Einstellung und Abwicklung; auch gegen Gesellschafter und Organe
     § 5 KMAG:                sofort vollziehbar — kein Suspensiveffekt
     §§ 46, 47 KMAG:          <Straf- bzw. Bußgeldrisiko>
     Kundenbestände:          <Verfügungsgewalt, Aussonderung § 45 KMAG>

V.   Laufende Pflichten nach Zulassung
     Art. 68 Unternehmensführung | Art. 70 sichere Aufbewahrung | Art. 75 Verwahrung
     § 26 KMAG digitale operationale Resilienz (DORA-Schnittstelle)
     §§ 20, 21, 37–45 KMAG

VI.  Maßnahmenplan
     Sofort | 30 Tage | 90 Tage mit Verantwortlichkeit

VII. Risiko: 🟢 / 🟡 / 🔴 <Begründung>
VIII.Quellenverzeichnis
```

## Risiken / typische Fehler

- **Mit dem 01.07.2026 aus Art. 143 Abs. 3 MiCAR gerechnet.** Deutschland hat die Übergangsfrist ausgeübt und verkürzt: § 50 Abs. 2 Nr. 3 KMAG lässt die fortbestehende Erlaubnis **spätestens mit Ablauf des 31.12.2025** erlöschen.
- **Übergangsrecht auf Unternehmen ohne die in § 50 Abs. 1 genannten Erlaubnisse erstreckt.** Der Katalog ist abschließend.
- **Anzeigeweg des Art. 60 unterstellt**, obwohl die Dienstleistung nicht von der bestehenden Erlaubnis gedeckt ist.
- **Anzeige nach § 50 Abs. 4 KMAG (bis 01.08.2024) übersehen**, wenn zuvor erlaubnisfreie Tätigkeiten erbracht wurden.
- **Aufschiebende Wirkung des Rechtsbehelfs angenommen.** § 5 KMAG ordnet die sofortige Vollziehbarkeit an.
- **Persönliche Adressierbarkeit nach § 9 KMAG unterschätzt** — die Anordnung erfasst Gesellschafter und Organmitglieder.
- **Kundenbestände nicht getrennt.** Art. 70 und Art. 75 MiCAR sowie § 45 KMAG entscheiden über die Aussonderung in der Insolvenz.
- **DORA-Schnittstelle ausgeblendet** (§ 26 KMAG).
- **Rechtsprechung erfunden.** Zu MiCAR und KMAG gibt es sie noch nicht; jede Entscheidung ist zu belegen oder als `[unverifiziert – prüfen]` zu kennzeichnen.
