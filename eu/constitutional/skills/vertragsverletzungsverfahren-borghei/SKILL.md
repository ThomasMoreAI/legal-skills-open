---
name: vertragsverletzungsverfahren-borghei
title: /europarecht:vertragsverletzungsverfahren
description: Reaktionsstrategie auf ein Vertragsverletzungsverfahren der EU-Kommission gegen die Bundesrepublik Deutschland nach Art. 258–260 AEUV – Mahnschreiben, Begründete Stellungnahme, Klage vor EuGH, Zwangsgeld/Pauschalbetrag Art. 260 II AEUV. Use when ein Bundesland oder eine Bundesbehörde ein Mahnschreiben oder eine Begründete Stellungnahme der Kommission erhalten hat oder das Risiko eines Verfahrens vorab eingeschätzt werden soll.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/europarecht/skills/vertragsverletzungsverfahren
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: constitutional
language: de
---

# /europarecht:vertragsverletzungsverfahren

## Zweck

Der Skill begleitet deutsche Behörden und ihre Berater durch die Stufen des Vertragsverletzungsverfahrens nach Art. 258–260 AEUV: Vorverfahren (Mahnschreiben → Begründete Stellungnahme) und gerichtliches Verfahren vor dem EuGH, einschließlich der Sanktionsstufe nach Art. 260 II AEUV (Pauschalbetrag und Zwangsgeld). Er liefert Fristen, Reaktionsbausteine, eine Risiko-Einschätzung und eine Skizze der internen Bund-Länder-Koordination.

## Eingaben

- Stufe des Verfahrens (informeller EU Pilot, Mahnschreiben Art. 258 AEUV, Begründete Stellungnahme, Klageerhebung, Art. 260-Folgeverfahren)
- vorgeworfener Verstoß (welche Richtlinie/Verordnung/Vertragsbestimmung, welcher konkrete Sachverhalt)
- betroffene Ebene (Bund / Bundesland / Kommune; nach Art. 23 Abs. 6 GG ggf. Innenvertretung durch Bundesrat)
- bisherige Korrespondenz mit der KOM
- politisch-rechtliche Zielsetzung (Verfahren abwenden / Klage akzeptieren / Sanktion minimieren)

## Sub-Agent-Architektur

Researcher liefert AEUV-Normen, einschlägige EuGH-Vertragsverletzungs-Rspr., KOM-Mitteilungen zur Sanktionsbemessung und Kommentarstellen. Drafter entwirft die Antwort an die KOM bzw. die interne Vorlage an BMJ/BMWK + Bundeskanzleramt und bewertet das Sanktionsrisiko. Reviewer prüft Fristen, Zuständigkeiten und Risikoeinstufung.

## Ablauf

### 1. Vorverfahren – Mahnschreiben (Art. 258 AEUV)

Mit dem Mahnschreiben ("lettre de mise en demeure", "Letter of Formal Notice") leitet die KOM das förmliche Verfahren ein. Der Mitgliedstaat erhält **idR zwei Monate** zur Stellungnahme. Inhalt der Antwort:

- Tatsachenklärung (Sachverhalt aus deutscher Sicht)
- rechtliche Gegenargumente (Unionsrechtskonformität der nationalen Norm/Praxis)
- ggf. Mitteilung bereits eingeleiteter Abhilfemaßnahmen mit Zeitplan

### 2. Vorverfahren – Begründete Stellungnahme (Art. 258 II AEUV)

Hält die KOM den Verstoß für nicht ausgeräumt, erlässt sie eine **mit Gründen versehene Stellungnahme** ("reasoned opinion") mit konkreter Frist (idR ebenfalls zwei Monate). Reagiert der Mitgliedstaat nicht ausreichend, kann die KOM Klage vor dem EuGH erheben.

### 3. Gerichtliches Verfahren (Art. 258, 259 AEUV)

Die Klage zielt auf Feststellung der Vertragsverletzung. Der EuGH urteilt **deklaratorisch**. Der Mitgliedstaat ist nach Art. 260 I AEUV verpflichtet, die sich aus dem Urteil ergebenden Maßnahmen zu ergreifen.

### 4. Sanktionsverfahren (Art. 260 II AEUV)

Kommt der Mitgliedstaat dem Urteil nicht nach, kann die KOM erneut den EuGH anrufen und Pauschalbetrag und/oder Zwangsgeld beantragen. Höhe nach KOM-Mitteilungen (zuletzt Aktualisierung 2023 — Faktoren: Schwere, Dauer, Zahlungsfähigkeit, Faktor "n").

Bei Nichtumsetzung von Richtlinien greift der **verkürzte Weg** Art. 260 III AEUV: Sanktion bereits im ersten Urteil.

### 5. Interne Koordination Bund/Länder

Nach [Art. 104a Abs. 6 GG](https://www.gesetze-im-internet.de/gg/art_104a.html) haftet **innerstaatlich** dasjenige Gemeinwesen, dessen Verstoß zur Sanktion führt (Bund/Länder, ggf. anteilig); bei länderübergreifenden Finanzkorrekturen der EU greift der dort festgelegte Verteilungsschlüssel (15/85 zwischen Bund und Ländergesamtheit, hiervon 35 % solidarisch, 50 % nach Mittelinanspruchnahme; Einzelheiten regelt das LastenausgleichsG zum Art. 104a Abs. 6 GG). Praxisrelevant: Wenn die Sanktion auf eine fehlende Länder-Umsetzung zurückgeht, trägt das betroffene Land die Last innerstaatlich.

Beteiligte: BMJ (federführend EU-Recht), BMWK / das fachzuständige Bundesministerium, Auswärtiges Amt (Verbindung zur StäV), Bundeskanzleramt, betroffenes Land.

### 6. Strategische Optionen

- **Frühe Abhilfe** vor Klage (Anpassung der Norm/Verwaltungspraxis)
- **Verhandelte Umsetzungszeitachse** mit der KOM
- **Volle Verteidigung** vor dem EuGH (selten erfolgreich, aber bei Auslegungsstreit denkbar)
- **Schadensminderung** durch glaubhafte Abhilfezusagen mit konkretem Zeitplan, um die Pauschal-/Zwangsgeldhöhe zu drücken

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Primärrecht

- [Art. 258 AEUV](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:12012E258) (Vertragsverletzungsverfahren)
- [Art. 259 AEUV](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:12012E259) (Verfahren auf Antrag eines Mitgliedstaats)
- [Art. 260 AEUV](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:12012E260) (Befolgungspflicht, Sanktionen)
- [Art. 4 Abs. 3 EUV](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:12012M004) (Unionstreue)
- [Art. 23 GG](https://www.gesetze-im-internet.de/gg/art_23.html) (Europaartikel, Mitwirkung der Länder)

### KOM-Mitteilungen

- KOM, Mitteilung "Aktualisierung der Daten zur Berechnung der Pauschalbeträge und Zwangsgelder" (jeweils aktuelle Fassung in ABl. C-Reihe; zuletzt 2023/C 2/01, [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=uriserv:OJ.C_.2023.002.01.0001.01.DEU&toc=OJ:C:2023:002:TOC))
- KOM, Mitteilung "EU-Recht: Bessere Ergebnisse durch bessere Anwendung" (2017/C 18/02), [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/ALL/?uri=CELEX:52017XC0119(01))

### Kommentare

- Cremer, in: Calliess/Ruffert, EUV/AEUV, 6. Aufl. 2022, Art. 258 AEUV Rn. 1 ff.; Art. 260 AEUV Rn. 1 ff.
- Karpenstein, in: Grabitz/Hilf/Nettesheim, Recht der EU, Stand 2024, Art. 258 AEUV Rn. 1 ff.
- Wegener, in: Streinz, EUV/AEUV, 3. Aufl. 2018, Art. 258 AEUV Rn. 1 ff.

### Rechtsprechung

1. EuGH, Urt. v. 12.07.2005 – Rs. C-304/02, Kommission/Frankreich (kombinierte Sanktion Pauschalbetrag + Zwangsgeld), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=12.07.2005&Aktenzeichen=C-304/02)
2. EuGH, Urt. v. 19.12.2012 – Rs. C-374/11, Kommission/Irland (Sanktionsbemessung), [curia.europa.eu](https://curia.europa.eu/juris/liste.jsf?num=C-374/11&language=DE)
3. EuGH, Urt. v. 16.07.2020 – Rs. C-549/18, Kommission/Rumänien (Art. 260 III AEUV bei RL-Nichtumsetzung), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=16.07.2020&Aktenzeichen=C-549/18)

## Ausgabeformat

```
INTERNE VORLAGE — Vertragsverletzungsverfahren
Adressat: <BMJ / Landesministerium>
Stufe: <Mahnschreiben / Begründete Stellungnahme / Klage / Art. 260 II>

I. Sachverhalt
II. Vorwurf der KOM (kurz)
III. Rechtliche Bewertung
    1. Tatbestand der Vertragsverletzung
    2. Rechtfertigung / Gegenargumente
    3. Sanktionsrisiko (Pauschalbetrag / Zwangsgeld)
IV. Bund-Länder-Zuständigkeit
V. Strategieoptionen
    – Option A: <Abhilfe / Zeitplan>
    – Option B: <Verteidigung>
    – Option C: <Verhandlung>
VI. Fristen und Wiedervorlage
VII. Risiken (🟢/🟡/🔴)
VIII. Quellenverzeichnis
```

## Risiken / typische Fehler

- **Antwortfrist verpasst** → KOM geht in die nächste Stufe; politisch und finanziell teuer.
- **Sachverhalt unklar** in der Antwort an KOM → KOM bleibt bei ihrer Annahme; späterer Vortrag vor EuGH ist nach **Streitgegenstandsbindung** durch die Begründete Stellungnahme begrenzt.
- **Übersehen von Art. 260 III AEUV** bei RL-Nichtumsetzung — Sanktion droht bereits im ersten Urteil.
- **Innerstaatliche Lastenverteilung** zwischen Bund und Land vorab nicht geklärt — politischer Streit nach Verurteilung.
- **Frühzeitige Abhilfezusage** ohne realistische Zeitachse — KOM zieht Verfahren nicht zurück, sondern dokumentiert Bruch.
