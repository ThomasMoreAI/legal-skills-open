---
name: entgelttransparenz-borghei
title: /arbeitsrecht:entgelttransparenz
description: Entgelttransparenz und Entgeltgleichheit im Übergang von nationalem zu europäischem Recht – geltendes deutsches Recht nach dem EntgTranspG (individueller Auskunftsanspruch §§ 10 ff., Reichweite § 12, betriebliches Prüfverfahren §§ 17 ff., Berichtspflicht §§ 21 f.) und die ab dem 08.06.2026 wirkende Richtlinie (EU) 2023/970 (Entgelttransparenz vor der Einstellung, Verbot der Frage nach der Entgelthistorie, Auskunftsanspruch ohne Schwellenwert, Gender-Pay-Gap-Berichterstattung ab 100/150/250 Beschäftigten, gemeinsame Entgeltbewertung bei einem ungeklärten Gefälle von mindestens 5 %, Beweislastumkehr), unmittelbare Wirkung gegenüber staatlichen Stellen und richtlinienkonforme Auslegung im Privatsektor. Use when ein Arbeitgeber die Umsetzung der Entgelttransparenzrichtlinie vorbereitet, ein Auskunftsverlangen beantwortet oder eine Entgeltgleichheitsklage bewertet wird.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/arbeitsrecht/skills/entgelttransparenz
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: employment
language: de
---

# /arbeitsrecht:entgelttransparenz

## Zweck

Dies ist ein Mandat, das man nicht abwarten kann. Deutschland hat die Umsetzungsfrist der Richtlinie (EU) 2023/970 zum **07.06.2026 versäumt**; die Pflichten der Richtlinie greifen gleichwohl ab dem **08.06.2026**. Für öffentliche Arbeitgeber bedeutet das unmittelbare Anwendbarkeit, für private Arbeitgeber richtlinienkonforme Auslegung des EntgTranspG und erheblichen Druck aus Betriebsrat und Öffentlichkeit — und für **alle** Arbeitgeber ab 150 Beschäftigten, dass die Datenerhebung für den ersten Bericht **jetzt** laufen muss, weil dieser bereits das Kalenderjahr 2026 abbildet.

## Eingaben

- Beschäftigtenzahl (Schwellen 100 / 150 / 250) und Rechtsform: **privater** oder **öffentlicher** Arbeitgeber / sonstige staatliche Stelle
- Bestehende Entgeltstruktur: Tarifbindung, Entgeltgruppen, Stellenarchitektur, Bewertungssystem
- Existiert eine dokumentierte **Arbeitsbewertung** für die Bestimmung „gleichwertiger Arbeit"? (Der Langläufer des Projekts)
- Vorhandene Entgeltdaten nach Geschlecht: Median, arithmetisches Mittel, variable Bestandteile, Quartile
- Bisherige Auskunftsverlangen nach §§ 10 ff. EntgTranspG und deren Beantwortung
- Stellenausschreibungspraxis: Werden Entgeltspannen genannt? Wird nach dem bisherigen Gehalt gefragt?
- Betriebsrat vorhanden? (§ 13 EntgTranspG i.V.m. § 80 Abs. 1 Nr. 2a BetrVG)

## Sub-Agent-Architektur

1. **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) liefert EntgTranspG-Normen mit URL, den Text der Richtlinie (EU) 2023/970 und den aktuellen Stand des deutschen Gesetzgebungsverfahrens.
2. **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) erstellt Auskunftsantwort, Gap-Analyse-Struktur oder Umsetzungs-Roadmap.
3. **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft Schwellenzuordnung, Datenschutz, Fristen und die Trennung zwischen geltendem und künftigem Recht.

## Ablauf

### 1. Geltendes deutsches Recht: der Auskunftsanspruch ([§ 10 EntgTranspG](https://www.gesetze-im-internet.de/entgtranspg/__10.html))

Beschäftigte haben zur Überprüfung des Entgeltgleichheitsgebots einen Auskunftsanspruch nach Maßgabe der §§ 11 bis 16 EntgTranspG. Sie müssen dazu **in zumutbarer Weise eine gleiche oder gleichwertige Tätigkeit (Vergleichstätigkeit) benennen** und können Auskunft zum durchschnittlichen monatlichen Bruttoentgelt sowie zu **bis zu zwei** einzelnen Entgeltbestandteilen verlangen. Das Verlangen erfolgt in **Textform**; eine Wiederholung ist vor Ablauf von zwei Jahren nur bei wesentlicher Veränderung der Voraussetzungen möglich (§ 10 Abs. 2 EntgTranspG).

Inhalt der Auskunft ([§ 11 EntgTranspG](https://www.gesetze-im-internet.de/entgtranspg/__11.html)): Kriterien und Verfahren der Entgeltfindung sowie das **Vergleichsentgelt** als auf Vollzeitäquivalente hochgerechneter **statistischer Median** des durchschnittlichen monatlichen Bruttoentgelts des jeweils anderen Geschlechts. Bei tarifgebundenen und tarifanwendenden Arbeitgebern genügt für die Kriterien der Verweis auf die tarifliche Regelung.

**Zwei Begrenzungen des geltenden Rechts** ([§ 12 EntgTranspG](https://www.gesetze-im-internet.de/entgtranspg/__12.html)) — beides Punkte, die unter der Richtlinie entfallen:

1. Der Anspruch besteht nur in **Betrieben mit in der Regel mehr als 200 Beschäftigten** bei demselben Arbeitgeber (§ 12 Abs. 1 EntgTranspG).
2. Das Vergleichsentgelt ist **nicht anzugeben**, wenn die Vergleichstätigkeit von **weniger als sechs Beschäftigten** des jeweils anderen Geschlechts ausgeübt wird (§ 12 Abs. 3 S. 2 EntgTranspG). Diese Sechs-Personen-Schwelle ist in der Praxis der Grund, warum ein erheblicher Teil aller Auskunftsverlangen ohne verwertbares Ergebnis endet.

Ergänzend: [§ 13 EntgTranspG](https://www.gesetze-im-internet.de/entgtranspg/__13.html) (Aufgaben und Rechte des Betriebsrats, Einsichtsrecht des Betriebsausschusses in die Bruttoentgeltlisten), [§ 14 EntgTranspG](https://www.gesetze-im-internet.de/entgtranspg/__14.html) (Verfahren bei tarifgebundenen Arbeitgebern), [§ 15 EntgTranspG](https://www.gesetze-im-internet.de/entgtranspg/__15.html) (Verfahren bei nicht tarifgebundenen Arbeitgebern), §§ 17 ff. (freiwilliges betriebliches Prüfverfahren), [§ 21 EntgTranspG](https://www.gesetze-im-internet.de/entgtranspg/__21.html) und [§ 22 EntgTranspG](https://www.gesetze-im-internet.de/entgtranspg/__22.html) (Bericht zur Gleichstellung und Entgeltgleichheit für lageberichtspflichtige Arbeitgeber ab 500 Beschäftigten).

### 2. Richtlinie (EU) 2023/970 — Status und Zeitachse

| Datum | Ereignis |
|---|---|
| 07.06.2026 | **Umsetzungsfrist der Richtlinie — von Deutschland versäumt** |
| 08.06.2026 | Pflichten der Richtlinie greifen unionsrechtlich, unabhängig vom Stand der deutschen Umsetzung |
| 07.06.2027 | **Erster Gender-Pay-Gap-Bericht für Arbeitgeber ab 150 Beschäftigten — berichtet wird das Kalenderjahr 2026** |

**Stand des deutschen Verfahrens** `[unverifiziert – prüfen]`: Der für Januar 2026 angekündigte Referentenentwurf des BMBFSFJ ist bis heute (Stand dieses Skills: 21.07.2026) **nicht veröffentlicht**. Das Ministerium peilt ein Inkrafttreten nunmehr **Anfang 2027** an; Berichtspflichten und die neuen Auskunftsansprüche sollen danach erst **ab Juni 2028** anwendbar sein. Diese Zeitplanung ist politisch und nicht rechtsverbindlich — sie ist vor jeder Beratung gegen den aktuellen Stand auf den Seiten des BMBFSFJ und des Bundestages zu verifizieren.

### 3. Die entscheidende Weichenstellung: öffentlicher oder privater Arbeitgeber

**Unmittelbare vertikale Wirkung.** Eine nicht fristgerecht umgesetzte Richtlinie kann sich der Einzelne gegenüber dem **Staat** unmittelbar berufen, soweit ihre Bestimmungen inhaltlich unbedingt und hinreichend genau sind. Adressat ist dabei der Staat in einem weiten, funktionalen Sinn: Gebietskörperschaften, Anstalten und Körperschaften des öffentlichen Rechts, aber auch **privatrechtlich organisierte Einrichtungen, die unter staatlicher Aufsicht eine im öffentlichen Interesse liegende Aufgabe wahrnehmen und dafür mit besonderen Rechten ausgestattet sind** (st. Rspr. des EuGH zur unmittelbaren Wirkung von Richtlinien gegenüber staatlichen Stellen, Rechtssachen *Marshall* und *Foster* `[unverifiziert – prüfen]`).

**Praxispunkt, der in kaum einer Mandantenpräsentation steht:** Öffentliche Arbeitgeber und andere staatliche Stellen sind daher ab dem **08.06.2026** an die hinreichend bestimmten Vorgaben der Richtlinie **unmittelbar gebunden** — insbesondere an die Entgeltangabe in Stellenausschreibungen, das Verbot der Frage nach der Entgelthistorie und den erweiterten Auskunftsanspruch. Kommunale Kliniken, Verkehrs- und Versorgungsbetriebe in privater Rechtsform, Sparkassen, öffentlich-rechtliche Rundfunkanstalten und Hochschulen sind hier gesondert zu prüfen.

**Private Arbeitgeber** unterliegen **keiner** unmittelbaren Wirkung — eine horizontale Direktwirkung zwischen Privaten gibt es nicht. Sie sind gleichwohl nicht unbetroffen:

- **Richtlinienkonforme Auslegung** des bestehenden EntgTranspG und des § 3 Abs. 1 AGG im Rahmen der Auslegungsspielräume;
- Art. 157 AEUV (Entgeltgleichheit) gilt unmittelbar auch zwischen Privaten und trägt den materiellen Gleichbehandlungsanspruch bereits heute;
- **Staatshaftung** nach den *Francovich*-Grundsätzen gegen die Bundesrepublik bei Schäden aus der verspäteten Umsetzung `[unverifiziert – prüfen]`;
- betriebsverfassungsrechtlicher und reputationeller Druck ab dem 08.06.2026.

### 4. Materielle Pflichten der Richtlinie

**Vor der Einstellung:**

- Bewerber erhalten Angaben zum **Einstiegsentgelt oder dessen Spanne** — in der Ausschreibung oder vor dem Vorstellungsgespräch.
- **Verbot der Frage nach der Entgelthistorie**: Der Arbeitgeber darf Bewerber nicht nach ihrem bisherigen oder aktuellen Entgelt fragen. Das ist die operativ am schnellsten wirksame Änderung; Bewerbungsformulare, Recruiting-Software und Interviewleitfäden sind entsprechend anzupassen.
- Diskriminierungsfreie Stellenbezeichnungen und Auswahlverfahren.

**Im laufenden Arbeitsverhältnis:**

- **Auskunftsanspruch ohne Schwellenwert**: Beschäftigte können ihr individuelles Entgeltniveau und die **nach Geschlecht aufgeschlüsselten Durchschnittsentgelte** für Gruppen mit gleicher oder gleichwertiger Arbeit verlangen — unabhängig von der Größe des Arbeitgebers und ohne die Sechs-Personen-Schwelle des § 12 Abs. 3 EntgTranspG. Der Arbeitgeber informiert jährlich über das Bestehen dieses Rechts.
- **Transparenz der Entgeltfindung**: Kriterien für Entgelt, Entgeltniveaus und Entgeltentwicklung müssen objektiv, geschlechtsneutral und zugänglich sein.
- **Verbot von Verschwiegenheitsklauseln** über das eigene Entgelt.

**Berichtspflichten (Gender-Pay-Gap-Reporting), gestaffelt nach Beschäftigtenzahl:**

| Beschäftigte | Erster Bericht | Turnus |
|---|---|---|
| ab 250 | 07.06.2027 (für 2026) | jährlich |
| 150 – 249 | 07.06.2027 (für 2026) | alle drei Jahre |
| 100 – 149 | 07.06.2031 | alle drei Jahre |
| unter 100 | keine Pflicht | — |

Berichtsinhalte: geschlechtsspezifisches Entgeltgefälle insgesamt, bei variablen Bestandteilen, im Median, Anteil der Geschlechter je Quartil sowie das Gefälle je Kategorie von Beschäftigten mit gleicher oder gleichwertiger Arbeit.

**Gemeinsame Entgeltbewertung (joint pay assessment):** Ergibt der Bericht in einer Kategorie ein Entgeltgefälle von **mindestens 5 %**, das der Arbeitgeber nicht durch objektive, geschlechtsneutrale Kriterien rechtfertigen kann, und wird es **nicht innerhalb von sechs Monaten behoben**, ist gemeinsam mit den Arbeitnehmervertretungen eine Entgeltbewertung durchzuführen — mit Analyse, Begründung und Abhilfemaßnahmen.

**Durchsetzung:** Beweislastumkehr zulasten des Arbeitgebers, Anspruch auf vollständige Entschädigung einschließlich Nachzahlung, Sanktionen der Mitgliedstaaten, Klagebefugnis von Verbänden und Arbeitnehmervertretungen.

### 5. Der Langläufer: „gleichwertige Arbeit" und die Stellenarchitektur

Alle Berichts- und Bewertungspflichten setzen voraus, dass der Arbeitgeber seine Tätigkeiten in **Kategorien gleicher und gleichwertiger Arbeit** einteilen kann. Die Richtlinie verlangt dafür objektive, geschlechtsneutrale Kriterien, mindestens: **Qualifikation, Belastung, Verantwortung und Arbeitsbedingungen**.

Das ist kein Reporting-, sondern ein **Organisationsprojekt** mit typischerweise sechs bis zwölf Monaten Vorlauf: Tätigkeitsprofile erheben, Kriterien gewichten, Stellen bewerten, Ergebnisse validieren, mit Betriebsrat und Tarifpartnern abstimmen. Wer erst nach Vorliegen des deutschen Umsetzungsgesetzes beginnt, kann den Bericht für 2026 nicht mehr belastbar erstellen — die Daten sind dann nicht mehr rückwirkend erhebbar.

**Roadmap ab heute:**

```
Sofort        Job-Architektur / Bewertungssystem aufsetzen; Entgeltdaten
              2026 vollständig und geschlechtsdifferenziert erfassen
Sofort        Frage nach der Entgelthistorie aus Formularen, ATS und
              Interviewleitfäden entfernen
Sofort        Entgeltspannen in Ausschreibungen einführen (Pflicht für
              staatliche Stellen ab 08.06.2026; für private Arbeitgeber
              Vorbereitung und Marktstandard)
Q3–Q4 2026    Erste Gap-Analyse als Probelauf; Kategorien validieren;
              Rechtfertigungsgründe je Kategorie dokumentieren
Q1 2027       Bericht für 2026 erstellen; bei Gefälle ≥ 5 % die
              Sechsmonatsfrist zur Abhilfe einplanen
07.06.2027    Berichtsstichtag (≥ 150 Beschäftigte)
laufend       Umsetzungsgesetz verfolgen; Fristen nachziehen
```

## Quellen

### Statute

- [§ 10 EntgTranspG](https://www.gesetze-im-internet.de/entgtranspg/__10.html), [§ 11 EntgTranspG](https://www.gesetze-im-internet.de/entgtranspg/__11.html), [§ 12 EntgTranspG](https://www.gesetze-im-internet.de/entgtranspg/__12.html), [§ 13 EntgTranspG](https://www.gesetze-im-internet.de/entgtranspg/__13.html), [§ 14 EntgTranspG](https://www.gesetze-im-internet.de/entgtranspg/__14.html), [§ 15 EntgTranspG](https://www.gesetze-im-internet.de/entgtranspg/__15.html), [§ 21 EntgTranspG](https://www.gesetze-im-internet.de/entgtranspg/__21.html), [§ 22 EntgTranspG](https://www.gesetze-im-internet.de/entgtranspg/__22.html)
- [§ 1 AGG](https://www.gesetze-im-internet.de/agg/__1.html), [§ 3 AGG](https://www.gesetze-im-internet.de/agg/__3.html), [§ 7 AGG](https://www.gesetze-im-internet.de/agg/__7.html), [§ 15 AGG](https://www.gesetze-im-internet.de/agg/__15.html), [§ 22 AGG](https://www.gesetze-im-internet.de/agg/__22.html)
- [§ 80 BetrVG](https://www.gesetze-im-internet.de/betrvg/__80.html), [§ 99 BetrVG](https://www.gesetze-im-internet.de/betrvg/__99.html)
- **Richtlinie (EU) 2023/970** des Europäischen Parlaments und des Rates vom 10.05.2023 zur Stärkung der Anwendung des Grundsatzes des gleichen Entgelts für Männer und Frauen bei gleicher oder gleichwertiger Arbeit durch Entgelttransparenz und Durchsetzungsmechanismen ([EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32023L0970))
- Art. 157 AEUV; Richtlinie 2006/54/EG

### Kommentare

- Franzen, in: ErfK, 24. Aufl. 2024, EntgTranspG Rn. 1 ff.
- Bauer / Romero, EntgTranspG, Kommentar, 2. Aufl. 2021
- Thüsing, in: MüKoBGB, 9. Aufl. 2023, § 3 AGG Rn. 1 ff. (mittelbare Entgeltdiskriminierung)

### Rechtsprechung

- st. Rspr. des EuGH zur unmittelbaren Wirkung nicht umgesetzter Richtlinien gegenüber staatlichen Stellen (Rechtssachen *Marshall* und *Foster*) `[unverifiziert – prüfen]`
- st. Rspr. des EuGH zur Staatshaftung bei verspäteter Richtlinienumsetzung (Rechtssache *Francovich*) `[unverifiziert – prüfen]`
- st. Rspr. des BAG zu §§ 10 ff. EntgTranspG (Auskunft über den Median als Indiz im Sinne des § 22 AGG) `[unverifiziert – prüfen]`
- EuGH-Rspr. zu Art. 157 AEUV und zur unmittelbaren Anwendbarkeit des Entgeltgleichheitsgrundsatzes auch zwischen Privaten `[unverifiziert – prüfen]`

> Der **deutsche Umsetzungszeitplan** und der Stand des Referentenentwurfs sind vor jeder Mandatsberatung gegen die Veröffentlichungen des BMBFSFJ und des Bundestages zu verifizieren; die hier genannten Termine des nationalen Verfahrens sind mit `[unverifiziert – prüfen]` markiert. Der Richtlinientext selbst ist über EUR-Lex verifiziert.

## Ausgabeformat

```
ENTGELTTRANSPARENZ — <Mandat-ID> — <Datum>
VERTRAULICH — MANDATSGEHEIMNIS — § 43a Abs. 2 BRAO

⚠️ RECHTSLAGE IM ÜBERGANG
    Umsetzungsfrist RL (EU) 2023/970:  07.06.2026 — versäumt
    Unionsrechtliche Wirkung ab:       08.06.2026
    Deutsches Umsetzungsgesetz:        ausstehend [unverifiziert – prüfen]

I.    Arbeitgeberstatus              [privat / öffentlich / staatliche
                                      Stelle im funktionalen Sinn]
      Unmittelbare Wirkung:          [🔴 ja, ab 08.06.2026 / nein]
II.   Beschäftigtenzahl              <N>   Schwellen: 100 / 150 / 250
      Berichtspflicht:               [keine / ab 07.06.2027 / ab 07.06.2031]
      Turnus:                        [jährlich / dreijährlich]
III.  Geltendes Recht EntgTranspG
      § 12 Abs. 1 (> 200 Beschäftigte):    [erfüllt / nicht erfüllt]
      Offene Auskunftsverlangen:            <N>
      Sechs-Personen-Schwelle § 12 III 2:   [greift / greift nicht]
IV.   Job-Architektur / gleichwertige Arbeit
      Bewertungssystem vorhanden:    [🟢 / 🔴 — Projektstart erforderlich]
      Kriterien:                     Qualifikation, Belastung,
                                     Verantwortung, Arbeitsbedingungen
V.    Datenlage 2026                 [🟢 vollständig / 🔴 Lücken: <…>]
VI.   Gap-Analyse (Probelauf)
      Gesamtgefälle:                 <%>
      Median:                        <%>
      Variable Bestandteile:         <%>
      Kategorien mit Gefälle ≥ 5 %:  <Liste>
      Rechtfertigung dokumentiert:   [🟢 / 🔴]
      Sechsmonatsfrist zur Abhilfe:  <Datum>  → sonst gemeinsame
                                     Entgeltbewertung
VII.  Recruiting-Prozess
      Entgeltspanne in Ausschreibung:[🟢 / 🔴]
      Frage nach Entgelthistorie:    [🔴 noch vorhanden in <System> /
                                      entfernt am <Datum>]
      Verschwiegenheitsklauseln:     [🔴 vorhanden / entfernt]
VIII. Betriebsrat § 13 EntgTranspG   [eingebunden / nicht eingebunden]
IX.   Risiko                         [🟢 / 🟡 / 🔴]
      Beweislastumkehr, Nachzahlungs- und Entschädigungsrisiko

Offene Verifizierungen:
  - Stand des Referentenentwurfs BMBFSFJ prüfen
Empfehlung / Roadmap: <…>
```

## Risiken / typische Fehler

- **Auf das deutsche Umsetzungsgesetz gewartet** — der erste Bericht deckt das Kalenderjahr **2026** ab; wer 2027 mit der Datenerhebung beginnt, kann ihn nicht mehr belastbar erstellen.
- **Unmittelbare Wirkung gegenüber staatlichen Stellen übersehen** — kommunale Gesellschaften, Sparkassen, Kliniken und Hochschulen in privater Rechtsform sind gesondert zu prüfen; die Rechtsform allein entscheidet nicht.
- **Horizontale Direktwirkung angenommen** — gegenüber privaten Arbeitgebern gibt es sie nicht; der Anspruch stützt sich dort auf Art. 157 AEUV, das AGG und richtlinienkonforme Auslegung.
- **Sechs-Personen-Schwelle des § 12 Abs. 3 S. 2 EntgTranspG fortgeschrieben** — sie entfällt unter der Richtlinie; die Auskunft ist dann unabhängig von der Größe der Vergleichsgruppe und ohne Schwellenwert des Arbeitgebers zu erteilen.
- **Frage nach der Entgelthistorie im Bewerbungsprozess belassen** — sie ist unter der Richtlinie untersagt und in Bewerbungsformularen sowie Recruiting-Systemen der am leichtesten zu übersehende Verstoß.
- **Job-Architektur unterschätzt** — die Bestimmung „gleichwertiger Arbeit" ist der Langläufer des Projekts, nicht das Reporting.
- **5-%-Schwelle als Bagatellgrenze missverstanden** — sie löst bei fehlender Rechtfertigung und ausbleibender Abhilfe binnen sechs Monaten die gemeinsame Entgeltbewertung aus.
- **Beweislastumkehr nicht eingepreist** — der Arbeitgeber muss die Rechtfertigung je Kategorie **dokumentiert** vorhalten; nachträgliche Erklärungen tragen nicht.
- **Deutschen Zeitplan als gesichert dargestellt** — Inkrafttreten Anfang 2027 und Anwendung der Berichtspflichten ab Juni 2028 sind Planungsstände des Ministeriums, kein geltendes Recht.
