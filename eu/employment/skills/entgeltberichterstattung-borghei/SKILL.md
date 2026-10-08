---
name: entgeltberichterstattung-borghei
title: /entgelttransparenz-eu:entgeltberichterstattung
description: Entgeltberichterstattung und gemeinsame Entgeltbewertung – sieben Berichtsinhalte nach Art. 9 Abs. 1 RL (EU) 2023/970 einschließlich Entgeltgefälle bei ergänzenden und variablen Bestandteilen, Median-Gefälle, Anteil der Beschäftigten mit variablen Bestandteilen, Verteilung über die Entgeltquartile und Gefälle je Arbeitnehmergruppe, gestaffelte Schwellen und Stichtage nach Art. 9 Abs. 2 bis 4 (ab 250 Beschäftigten jährlich ab 07.06.2027, 150 bis 249 dreijährlich ab 07.06.2027, 100 bis 149 dreijährlich ab 07.06.2031), Unterstützung kleinerer Arbeitgeber Art. 11, gemeinsame Entgeltbewertung Art. 10 bei mindestens 5 Prozent ungerechtfertigtem Gefälle in einer Arbeitnehmergruppe ohne Korrektur binnen sechs Monaten sowie das Verhältnis zum Entgeltbericht nach §§ 21, 22 EntgTranspG und zum betrieblichen Prüfverfahren §§ 17 bis 20 EntgTranspG. Use when Berichtspflichten vorzubereiten, Datenmodelle aufzubauen oder eine gemeinsame Entgeltbewertung durchzuführen ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/entgelttransparenz-eu/skills/entgeltberichterstattung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: employment
language: de
---

# /entgelttransparenz-eu:entgeltberichterstattung

## Zweck

Der Skill bereitet die Berichtspflichten vor, deren erster Stichtag der **07.06.2027** ist — und deren Datengrundlage **jetzt** aufgebaut werden muss, weil berichtet wird über das **vorangehende Kalenderjahr**. Er liefert die sieben Kennzahlen, die Schwellen- und Fristenmatrix und den Auslöser der gemeinsamen Entgeltbewertung.

## Eingaben

- Beschäftigtenzahl (Berechnungsmethode und Stichtag), Konzernstruktur, Betriebe
- Entgeltdaten: Grundentgelt, ergänzende und variable Bestandteile, Zulagen, Sachbezüge
- Gruppenbildung: Arbeitnehmergruppen gleicher oder gleichwertiger Arbeit
- Bestehende Berichte nach §§ 21, 22 EntgTranspG und Ergebnisse betrieblicher Prüfverfahren
- Vorhandene Systeme (HR, Payroll) und deren Auswertbarkeit nach Geschlecht und Gruppe
- Ob ein Umsetzungsgesetz verkündet ist und welche Überwachungsstelle benannt wurde

## Sub-Agent-Architektur

Der Researcher beschafft die RL (EU) 2023/970, das EntgTranspG und den Umsetzungsstand einschließlich der benannten Überwachungsstelle. Der Drafter baut die Kennzahlendefinition, die Gruppenbildung und den Zeitplan. Der Reviewer prüft Schwellen, Stichtage und ob die 5-Prozent-Schwelle des Art. 10 mit der Sechsmonatsfrist korrekt verknüpft ist.

> **Rechtsstand.** Die Berichtspflichten des Art. 9 setzen nationale Umsetzung voraus — Meldeweg, Überwachungsstelle und Sanktionen bestimmt der deutsche Gesetzgeber. Die Umsetzungsfrist lief am **07.06.2026** ab; ein Umsetzungsgesetz ist vor jeder Verwendung gegen das Bundesgesetzblatt zu prüfen `[unverifiziert – prüfen]` (`/entgelttransparenz-eu:entgelttransparenz-umsetzungsstand`).

## Ablauf

### 1. Die sieben Berichtsinhalte (Art. 9 Abs. 1 RL (EU) 2023/970)

Arbeitgeber stellen zu ihrer Organisation folgende Informationen bereit:

| Buchst. | Kennzahl |
|---|---|
| a | das **geschlechtsspezifische Entgeltgefälle** |
| b | das geschlechtsspezifische Entgeltgefälle bei **ergänzenden oder variablen Bestandteilen** |
| c | das **mittlere** geschlechtsspezifische Entgeltgefälle (Median) |
| d | das mittlere geschlechtsspezifische Entgeltgefälle bei ergänzenden oder variablen Bestandteilen |
| e | der **Anteil** der Arbeitnehmerinnen und Arbeitnehmer, die ergänzende oder variable Bestandteile erhalten |
| f | der Anteil der Arbeitnehmerinnen und Arbeitnehmer in **jedem Entgeltquartil** |
| g | das Entgeltgefälle **je Gruppe** von Arbeitnehmern, aufgeschlüsselt nach normalem Grundlohn oder -gehalt sowie nach ergänzenden oder variablen Bestandteilen |

Buchst. g ist der operativ anspruchsvollste Punkt: Er verlangt eine belastbare **Gruppenbildung** nach gleicher oder gleichwertiger Arbeit — und genau diese Gruppen lösen später Art. 10 aus.

### 2. Schwellen und Stichtage (Art. 9 Abs. 2 bis 4)

| Beschäftigte | Erstmals | Turnus |
|---|---|---|
| **250 oder mehr** | bis zum **7. Juni 2027** | **jährlich**, jeweils für das vorangehende Kalenderjahr |
| **150 bis 249** | bis zum **7. Juni 2027** | **alle drei Jahre** |
| **100 bis 149** | bis zum **7. Juni 2031** | **alle drei Jahre** |
| unter 100 | keine Pflicht nach Art. 9; **Art. 11** sieht Unterstützung für Arbeitgeber mit weniger als 250 Arbeitnehmern vor | — |

**Rückwirkende Datenlast:** Wer 2027 über das Kalenderjahr 2026 berichtet, braucht die Daten **für 2026** — also für ein Jahr, das bei Beratungsbeginn bereits läuft oder abgelaufen ist. Die Datenaufbereitung ist deshalb die dringlichste Maßnahme, unabhängig vom Stand der deutschen Umsetzung.

### 3. Gemeinsame Entgeltbewertung (Art. 10 RL (EU) 2023/970)

Arbeitgeber, die den Berichtspflichten des Art. 9 unterliegen, nehmen **in Zusammenarbeit mit den Arbeitnehmervertretern** eine **gemeinsame Entgeltbewertung** vor, wenn **alle drei** Bedingungen erfüllt sind:

- a) Aus der Berichterstattung ergibt sich ein Unterschied der **durchschnittlichen Entgelthöhe** von Arbeitnehmerinnen und Arbeitnehmern von **mindestens 5 Prozent** in **einer Gruppe** von Arbeitnehmern;
- b) der Arbeitgeber hat diesen Unterschied **nicht auf der Grundlage objektiver, geschlechtsneutraler Kriterien gerechtfertigt**;
- c) der Arbeitgeber hat den ungerechtfertigten Unterschied **nicht innerhalb von sechs Monaten** nach dem Tag der Berichterstattung **korrigiert**.

**Die Sechsmonatsfrist ist das eigentliche Steuerungsinstrument:** Zwischen Bericht und Auslösung der gemeinsamen Bewertung liegt ein Halbjahr, in dem der Arbeitgeber entweder **rechtfertigen** oder **korrigieren** kann. Beides ist zu dokumentieren — die Rechtfertigung wird später zum Beweismittel im Prozess (`/entgelttransparenz-eu:entgeltdiskriminierung-durchsetzung`).

Die Bewertung dient dazu, ungerechtfertigte Unterschiede **festzustellen, zu korrigieren und zu verhindern**, und umfasst nach Art. 10 Abs. 2 unter anderem:

- a) eine **Analyse des Anteils** der Arbeitnehmerinnen und Arbeitnehmer in jeder Gruppe;
- b) Informationen über die **durchschnittlichen Entgelthöhen** sowie über ergänzende oder variable Bestandteile je Gruppe;
- c) weitere in Art. 10 Abs. 2 benannte Elemente einschließlich der Maßnahmen zur Behebung.

### 4. Verhältnis zum geltenden deutschen Recht

| Instrument | Norm | Verhältnis |
|---|---|---|
| **Bericht zur Gleichstellung und Entgeltgleichheit** | [§§ 21, 22 EntgTranspG](https://www.gesetze-im-internet.de/entgtranspg/__21.html) — lageberichtspflichtige Arbeitgeber mit in der Regel mehr als 500 Beschäftigten | anderer Adressatenkreis, andere Inhalte; wird durch die Umsetzung überformt |
| **Betriebliches Prüfverfahren** | [§§ 17 bis 20 EntgTranspG](https://www.gesetze-im-internet.de/entgtranspg/__17.html) — Aufforderung an private Arbeitgeber mit mehr als 500 Beschäftigten, freiwillig zu prüfen | inhaltlich der Vorläufer der gemeinsamen Entgeltbewertung, aber **freiwillig** |

Die Richtlinie macht aus dem freiwilligen Prüfverfahren eine **bedingte Pflicht** und senkt die Schwelle deutlich. Wer heute ein Prüfverfahren nach §§ 17 ff. EntgTranspG betreibt, baut damit die Grundlage für Art. 10 auf.

### 5. Datenmodell und Governance

Praktisch entscheidet die Datenqualität. Aufzubauen sind:

1. **Geschlechtsmerkmal** je Beschäftigtem, datenschutzkonform (Art. 12 RL, DSGVO);
2. **Entgeltbestandteile** getrennt: Grundentgelt, variable und ergänzende Bestandteile, Sachbezüge;
3. **Vollzeitäquivalente** zur Vergleichbarkeit von Teilzeit;
4. **Gruppenbildung** nach gleicher oder gleichwertiger Arbeit anhand objektiver Kriterien (Art. 4: Kompetenzen, Belastungen, Verantwortung, Arbeitsbedingungen);
5. **Quartilsbildung** über die Gesamtbelegschaft;
6. **Dokumentation der Rechtfertigungen** für jeden Unterschied ab 5 Prozent.

**Art. 12** begrenzt die Verwendung personenbezogener Daten auf den Zweck des gleichen Entgelts; die Veröffentlichung darf keine Rückschlüsse auf einzelne Beschäftigte erlauben. Bei sehr kleinen Gruppen ist die Aggregation zu prüfen.

### 6. Mitbestimmung

Die gemeinsame Entgeltbewertung erfolgt **in Zusammenarbeit mit den Arbeitnehmervertretern** (Art. 10 Abs. 1); Art. 13 stärkt den sozialen Dialog. National flankieren [§ 80 Abs. 1 Nr. 2a, Abs. 2 BetrVG](https://www.gesetze-im-internet.de/betrvg/__80.html) und [§ 13 EntgTranspG](https://www.gesetze-im-internet.de/entgtranspg/__13.html). Einführung und Betrieb der Auswertungssysteme können Mitbestimmungsrechte nach [§ 87 Abs. 1 Nr. 6 BetrVG](https://www.gesetze-im-internet.de/betrvg/__87.html) auslösen — das ist vor dem Systemaufbau zu klären, nicht danach.

## Deterministische Berechnung

Der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) macht nur die Arithmetik; die Kennzahlen selbst werden im HR-System berechnet:

```bash
# Art. 10 Abs. 1 lit. c: 6 Monate ab Tag der Berichterstattung am 07.06.2027
python -m scripts.legal_calc.cli frist --ereignis 07.06.2027 --menge 6 --einheit monate --land BY

# Dreijahresturnus für Arbeitgeber mit 150 bis 249 Beschäftigten ab 07.06.2027
python -m scripts.legal_calc.cli frist --ereignis 07.06.2027 --menge 3 --einheit jahre --land BY

# Vorlauf: Datenjahr 2026 endet - Aufbereitungsfrist bis zum ersten Bericht
python -m scripts.legal_calc.cli frist --ereignis 31.12.2026 --menge 5 --einheit monate --land BY
```

Ob ein Entgeltunterschied „auf objektiven, geschlechtsneutralen Kriterien" beruht, ist eine juristische Wertung und gesondert zu begründen.

## Quellen

### Rechtsakte

- Richtlinie (EU) 2023/970, Art. 4, 9, 10, 11, 12, 13, 29 — [EUR-Lex](https://eur-lex.europa.eu/eli/dir/2023/970/oj)
- [EntgTranspG](https://www.gesetze-im-internet.de/entgtranspg/) – [§ 17 EntgTranspG](https://www.gesetze-im-internet.de/entgtranspg/__17.html), [§ 18](https://www.gesetze-im-internet.de/entgtranspg/__18.html), [§ 19](https://www.gesetze-im-internet.de/entgtranspg/__19.html), [§ 20](https://www.gesetze-im-internet.de/entgtranspg/__20.html), [§ 21 EntgTranspG](https://www.gesetze-im-internet.de/entgtranspg/__21.html), [§ 22 EntgTranspG](https://www.gesetze-im-internet.de/entgtranspg/__22.html)
- [§ 80 BetrVG](https://www.gesetze-im-internet.de/betrvg/__80.html), [§ 87 BetrVG](https://www.gesetze-im-internet.de/betrvg/__87.html)
- Verordnung (EU) 2016/679 (DSGVO), Art. 5, 6, 9 — [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
- Art. 157 AEUV — [EUR-Lex](https://eur-lex.europa.eu/eli/treaty/tfeu_2012/oj)

### Kommentare und Literatur

- ErfK und HWK zum EntgTranspG, §§ 17 ff., 21 f.
- Fitting, BetrVG, §§ 80, 87 Abs. 1 Nr. 6.
- Beiträge zur Berichterstattung nach Art. 9 und zur gemeinsamen Entgeltbewertung in NZA, RdA und BB 2024–2026 (Fundstelle prüfen) `[unverifiziert – prüfen]`

### Rechtsprechung

Zur Berichterstattung nach Art. 9 und zur gemeinsamen Entgeltbewertung nach Art. 10 liegt **keine** Judikatur vor. Zur Mitbestimmung bei der Einführung technischer Auswertungssysteme besteht gefestigte BAG-Rechtsprechung zu § 87 Abs. 1 Nr. 6 BetrVG; jede konkrete Entscheidung ist vor Verwendung zu verifizieren `[unverifiziert – prüfen]`.

## Ausgabeformat

```
ENTGELTBERICHTERSTATTUNG — <Arbeitgeber> — <Datum>

I.   Rechtsstand
     Umsetzungsgesetz:        [nicht verkündet — Art. 9 setzt Umsetzung voraus / verkündet am <Datum>]
     Überwachungsstelle:      <benannt / offen>

II.  Einordnung
     Beschäftigte:            <Zahl>   Berechnungsmethode: <…>
     Kategorie Art. 9:        [≥ 250 jährlich / 150–249 dreijährlich / 100–149 ab 2031 / < 100 keine]
     Erster Stichtag:         <07.06.2027 / 07.06.2031>
     Datenjahr:               <vorangehendes Kalenderjahr>

III. Kennzahlen Art. 9 Abs. 1
     a) Entgeltgefälle:                        <…>
     b) Gefälle variable/ergänzende Bestandteile: <…>
     c) Median-Gefälle:                        <…>
     d) Median-Gefälle variabel/ergänzend:     <…>
     e) Anteil mit variablen Bestandteilen:    <…>
     f) Anteil je Entgeltquartil:              <…>
     g) Gefälle je Arbeitnehmergruppe:         <…>
     Datenlücken:                              <…>

IV.  Gruppenbildung
     Kriterien (Art. 4): Kompetenzen | Belastungen | Verantwortung | Arbeitsbedingungen
     Gruppen:                 <Liste>
     Sehr kleine Gruppen:     <Aggregation / Datenschutz Art. 12>

V.   Gemeinsame Entgeltbewertung Art. 10
     Gruppe mit ≥ 5 % Unterschied:   <…>
     Rechtfertigung (lit. b):        [dokumentiert / offen]
     Korrekturfrist (lit. c):        6 Monate ab <Datum> → bis <Datum>
     Auslösung:                      [ja — Bewertung mit Arbeitnehmervertretern / nein]

VI.  Verhältnis zum EntgTranspG
     §§ 21, 22 Bericht:       [pflichtig / nicht pflichtig]
     §§ 17 ff. Prüfverfahren: [durchgeführt / nicht durchgeführt]

VII. Mitbestimmung
     § 80 BetrVG / § 13 EntgTranspG: <…>
     § 87 Abs. 1 Nr. 6 BetrVG bei Systemeinführung: [geprüft]

VIII.Fahrplan
     Sofort: Datenmodell | Q4 2026: Datenjahr abschließen | Q1 2027: Kennzahlen | 07.06.2027: Bericht

IX.  Risiko: 🟢 / 🟡 / 🔴 <Begründung>
X.   Quellenverzeichnis
```

## Risiken / typische Fehler

- **Erst 2027 mit der Datenaufbereitung begonnen.** Berichtet wird über das **vorangehende Kalenderjahr** — die Daten für 2026 müssen 2026 entstehen.
- **Nur das Grundentgelt ausgewertet.** Art. 9 Abs. 1 verlangt ausdrücklich auch **ergänzende und variable** Bestandteile sowie den Anteil der Beschäftigten, die sie erhalten.
- **Median und Durchschnitt verwechselt.** Buchst. a und c bzw. b und d verlangen beides nebeneinander.
- **Quartilsverteilung vergessen** (Buchst. f).
- **Gruppenbildung nach Stellenbezeichnung statt nach Gleichwertigkeit** — Maßstab ist Art. 4.
- **5-Prozent-Schwelle auf den Gesamtbetrieb bezogen.** Art. 10 Abs. 1 lit. a knüpft an **eine Gruppe** an.
- **Sechsmonatsfrist des Art. 10 Abs. 1 lit. c übersehen** — sie ist das Fenster für Rechtfertigung oder Korrektur.
- **Rechtfertigung nicht dokumentiert.** Sie ist später das zentrale Beweismittel gegen die Beweislastumkehr.
- **Mitbestimmung erst nach dem Systemaufbau geprüft** (§ 87 Abs. 1 Nr. 6 BetrVG).
- **Datenschutz ausgeblendet.** Art. 12 RL und die DSGVO begrenzen Verwendung und Veröffentlichungstiefe.
- **Rechtsprechung erfunden.** Zu Art. 9 und 10 gibt es keine; jede Entscheidung ist zu belegen oder als `[unverifiziert – prüfen]` zu kennzeichnen.
