---
name: dienstliche-beurteilung-borghei
title: /beamten-disziplinarrecht:dienstliche-beurteilung
description: Angriff auf eine dienstliche Beurteilung – Beurteilungsrichtlinien als Verwaltungsvorschrift, Beurteilungsspielraum und die vier Kategorien eingeschränkter gerichtlicher Kontrolle (Verfahrensfehler, unrichtiger Sachverhalt, sachfremde Erwägungen, Verkennung allgemeingültiger Wertmaßstäbe), Regel- und Anlassbeurteilung, Quotierung und Richtwerte, Plausibilisierungspflicht des Dienstherrn, Gegenvorstellung und Widerspruch, Klage auf Neubeurteilung nach § 113 Abs. 5 S. 2 VwGO. Use when eine Regel- oder Anlassbeurteilung angegriffen werden soll, weil sie fehlerhaft zustande gekommen oder nicht plausibel begründet ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/beamten-disziplinarrecht/skills/dienstliche-beurteilung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: administrative
language: de
---

# /beamten-disziplinarrecht:dienstliche-beurteilung

## Zweck

Die dienstliche Beurteilung ist die Währung des Beförderungswettbewerbs: Wer sie nicht angreift, verliert den Konkurrentenstreit, bevor er beginnt. Der Skill prüft die Beurteilung entlang der vier gerichtlich überprüfbaren Fehlerkategorien, erzwingt die Plausibilisierung durch den Dienstherrn und entwirft Gegenvorstellung, Widerspruch und Klage auf Neubeurteilung. Er stellt zugleich klar, was **nicht** erreichbar ist: eine bestimmte Note.

## Eingaben

- Dienstherr (Bund / Land / Kommune) und Statusamt
- Beurteilungsart (Regelbeurteilung / Anlassbeurteilung) und Beurteilungszeitraum
- Beurteilungstext mit Einzelmerkmalen und Gesamturteil
- Vorbeurteilung(en) mit Note und Zeitraum
- Einschlägige Beurteilungsrichtlinie mit Notenskala und Richtwerten
- Beurteiler, Zweitbeurteiler, Beurteilungsbeitragende und deren Erkenntnisquellen
- Eröffnungs- und Besprechungsdatum, Vermerke über das Beurteilungsgespräch
- Anhängige oder bevorstehende Auswahlverfahren

## Sub-Agent-Architektur

Ein Researcher beschafft die geltende Beurteilungsrichtlinie, die Laufbahnverordnung des jeweiligen Dienstherrn und die Rechtsprechung des 2. Senats des BVerwG zu Beurteilungsspielraum, Richtwerten und Plausibilisierung. Ein Drafter ordnet jeden Einwand genau einer der vier Fehlerkategorien zu und entwirft Gegenvorstellung, Widerspruch oder Klageschrift. Ein Reviewer kontrolliert, dass kein Angriff auf die Bewertung als solche geführt wird, dass der Antrag auf **Neubeurteilung** und nicht auf eine Note gerichtet ist und dass jede Fundstelle belegt ist; nicht bestätigte Entscheidungen werden mit `[unverifiziert - prüfen]` markiert.

## Ablauf

### 1. Anwendbares Recht bestimmen ([§ 21 BBG](https://www.gesetze-im-internet.de/bbg_2009/__21.html))

**Erster Schritt, ohne Ausnahme.**

| Dienstherr | Gesetzliche Grundlage | Untergesetzliches Regelwerk |
|---|---|---|
| Bund | [§ 21 BBG](https://www.gesetze-im-internet.de/bbg_2009/__21.html) | BLV (insbesondere §§ 48 ff.), Beurteilungsrichtlinie der Behörde |
| Land, Kommune | Landesbeamtengesetz iVm [§ 9 BeamtStG](https://www.gesetze-im-internet.de/beamtstg/__9.html) | Landeslaufbahnverordnung, landesrechtliche Beurteilungsrichtlinie |

Die **Beurteilungsrichtlinie ist keine Rechtsnorm**, sondern eine Verwaltungsvorschrift. Sie bindet den Dienstherrn über Art. 3 Abs. 1 GG durch **Selbstbindung der Verwaltung**: Maßgeblich ist, wie er sie tatsächlich und einheitlich anwendet. Eine Abweichung von der eigenen ständigen Praxis ist deshalb ein selbständiger Angriffspunkt.

### 2. Beurteilungsart und Anlass ([Art. 33 Abs. 2 GG](https://www.gesetze-im-internet.de/gg/art_33.html))

- **Regelbeurteilung** — turnusmäßig zum Stichtag für alle Angehörigen einer Vergleichsgruppe; sie erzeugt die Vergleichbarkeit, auf der die Auswahl beruht.
- **Anlassbeurteilung** — aus konkretem Anlass, insbesondere wenn die Regelbeurteilung für ein laufendes Auswahlverfahren nicht mehr hinreichend aktuell ist. Sie muss sich in das System der Regelbeurteilungen einfügen und darf es nicht unterlaufen.

Fehlerbild: Anlassbeurteilungen, die nur für einzelne Bewerber erstellt werden und dadurch die Vergleichsgruppe sprengen.

### 3. Beurteilungsspielraum und Kontrolldichte ([§ 114 VwGO](https://www.gesetze-im-internet.de/vwgo/__114.html))

Die Beurteilung ist ein **persönlichkeitsbedingtes Werturteil**. Die verwaltungsgerichtliche Kontrolle ist deshalb **eingeschränkt** und beschränkt sich auf vier Kategorien:

1. **Verfahrensfehler** — Zuständigkeit des Beurteilers, Einhaltung der Richtlinie, Beteiligung, Eröffnung und Besprechung, fehlende oder unzureichende Beurteilungsbeiträge.
2. **Unrichtiger Sachverhalt** — die Beurteilung beruht auf falschen Tatsachen (Aufgabenzuschnitt, Zeiträume, Abwesenheiten, Vorfälle).
3. **Sachfremde Erwägungen** — Erwägungen außerhalb von Eignung, Befähigung und Leistung (Alter, Geschlecht, Teilzeit, Personalratstätigkeit, Krankheit, Elternzeit).
4. **Verkennung allgemeingültiger Wertmaßstäbe** — die Bewertung verlässt den Rahmen dessen, was nach der Richtlinie und dem allgemeinen Sprachgebrauch noch vertretbar ist; insbesondere Widerspruch zwischen Einzelmerkmalen und Gesamturteil.

**Nicht** überprüfbar ist die Bewertung als solche. Ein Vortrag der Form „ich verdiene eine bessere Note" ist unschlüssig; er muss in eine der vier Kategorien übersetzt werden.

### 4. Richtwerte und Quotierung ([§ 21 BBG](https://www.gesetze-im-internet.de/bbg_2009/__21.html))

Richtwerte für die Vergabe der Spitzennoten sind zulässig; sie dienen der Vergleichbarkeit und wirken der Noteninflation entgegen. Sie dürfen aber die Einzelfallgerechtigkeit nicht verdrängen: Die Note muss aus der Leistung folgen, nicht aus der Quote. Führt die Quote dazu, dass eine an sich gerechtfertigte Note versagt wird, ist die Beurteilung fehlerhaft. Voraussetzung jeder Quotierung ist eine hinreichend große und homogene **Vergleichsgruppe** (BVerwG, Urt. v. 24.11.2005 – 2 C 34.04, BVerwGE 124, 356 = NVwZ 2006, 465).

Fehlerbild: Quote auf eine Vergleichsgruppe von wenigen Personen angewandt; Vergleichsgruppe nach Dienststellen statt nach Statusämtern gebildet.

### 5. Plausibilisierungspflicht des Dienstherrn ([Art. 19 Abs. 4 GG](https://www.gesetze-im-internet.de/gg/art_19.html))

Das Gesamturteil ist aus den Einzelmerkmalen **herzuleiten und zu begründen**; eine bloße Aufsummierung oder Wiederholung der Notenstufe genügt nicht. Werden die Einzelbewertungen bestritten, muss der Dienstherr sie **plausibel machen** — im Beurteilungsgespräch, spätestens im Widerspruchs- oder Klageverfahren, notfalls durch Konkretisierung der zugrunde liegenden Tatsachen. Gelingt die Plausibilisierung nicht, ist die Beurteilung aufzuheben (BVerwG, Urt. v. 17.09.2015 – 2 C 27.14, BVerwGE 153, 48 = NVwZ 2016, 1262; BVerwG, Urt. v. 01.03.2018 – 2 A 10.17, BVerwGE 161, 240 = NVwZ 2019, 75).

Praktische Konsequenz: **Substantiiert bestreiten** ist die wirksamste Angriffsform. Je konkreter der Beamte einzelne Merkmale angreift, desto konkreter muss der Dienstherr antworten.

### 6. Absenkung gegenüber der Vorbeurteilung

Eine deutliche Absenkung bei unverändertem Aufgabenzuschnitt und unveränderter Leistung ist **begründungsbedürftig**. Der Dienstherr muss darlegen, worauf die Verschlechterung beruht — geänderter Maßstab, geänderte Vergleichsgruppe, geänderte Leistung. Das bloße Berufen auf eine „geänderte Beurteilungspraxis" trägt nur, wenn die Änderung dokumentiert und einheitlich vollzogen ist.

### 7. Gegenvorstellung, Widerspruch, Klage ([§ 113 VwGO](https://www.gesetze-im-internet.de/vwgo/__113.html))

- **Gegenvorstellung** — formloser, fristfreier Rechtsbehelf beim Beurteiler. Sie ist der schnellste Weg, die Plausibilisierung auszulösen, und sollte stets zuerst eingelegt werden. Sie hemmt **keine** Frist.
- **Widerspruch** — statthaft, soweit das Landes- oder Bundesrecht ein Vorverfahren vorsieht ([§ 68 VwGO](https://www.gesetze-im-internet.de/vwgo/__68.html)); Frist nach [§ 70 VwGO](https://www.gesetze-im-internet.de/vwgo/__70.html). Da die Beurteilung nach h.M. **kein Verwaltungsakt** ist, ist die Rechtsbehelfslage uneinheitlich; die landesrechtliche Ausgestaltung ist zu prüfen `[unverifiziert - prüfen]`.
- **Klage** — allgemeine Leistungsklage auf Aufhebung der Beurteilung und Erstellung einer neuen Beurteilung unter Beachtung der Rechtsauffassung des Gerichts. Der Rechtsgedanke des [§ 113 Abs. 5 S. 2 VwGO](https://www.gesetze-im-internet.de/vwgo/__113.html) gilt entsprechend: Das Gericht setzt **keine Note** fest; es verpflichtet zur Neubeurteilung.
- **Eilrechtsschutz**: Steht ein Auswahlverfahren an, ist parallel der Antrag nach § 123 VwGO gegen die Besetzung zu stellen — siehe `/beamten-disziplinarrecht:konkurrentenstreit`. Die Beurteilungsklage allein hält keine Stelle frei.

## Quellen

### Statute

- [§ 21 BBG](https://www.gesetze-im-internet.de/bbg_2009/__21.html), [§ 9 BBG](https://www.gesetze-im-internet.de/bbg_2009/__9.html)
- [§ 9 BeamtStG](https://www.gesetze-im-internet.de/beamtstg/__9.html), [§ 45 BeamtStG](https://www.gesetze-im-internet.de/beamtstg/__45.html)
- [Art. 33 GG](https://www.gesetze-im-internet.de/gg/art_33.html), [Art. 19 GG](https://www.gesetze-im-internet.de/gg/art_19.html), [Art. 3 GG](https://www.gesetze-im-internet.de/gg/art_3.html)
- [§ 68 VwGO](https://www.gesetze-im-internet.de/vwgo/__68.html), [§ 70 VwGO](https://www.gesetze-im-internet.de/vwgo/__70.html), [§ 113 VwGO](https://www.gesetze-im-internet.de/vwgo/__113.html), [§ 114 VwGO](https://www.gesetze-im-internet.de/vwgo/__114.html), [§ 123 VwGO](https://www.gesetze-im-internet.de/vwgo/__123.html)
- BLV und landesrechtliche Laufbahnverordnungen sowie die jeweilige Beurteilungsrichtlinie `[unverifiziert - prüfen]`

### Kommentare

- Schnellenbach/Bodanowitz, Beamtenrecht in der Praxis, Kap. Dienstliche Beurteilung.
- Battis, BBG, § 21 Rn. 1 ff.
- Plog/Wiedow, BBG, § 21 Rn. 1 ff.
- von Roetteken, in: von Roetteken/Rothländer, BeamtStG, § 9 Rn. 1 ff.
- Kopp/Schenke, VwGO, § 114 Rn. 1 ff.

### Rechtsprechung

1. BVerwG, Urt. v. 17.09.2015 – 2 C 27.14, BVerwGE 153, 48 = NVwZ 2016, 1262 (Herleitung und Plausibilisierung des Gesamturteils) ([dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerwG&Datum=2015-09-17&Aktenzeichen=2%20C%2027.14))
2. BVerwG, Urt. v. 01.03.2018 – 2 A 10.17, BVerwGE 161, 240 = NVwZ 2019, 75 (Anforderungen an die Begründung der Beurteilung) ([dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerwG&Datum=2018-03-01&Aktenzeichen=2%20A%2010.17))
3. BVerwG, Urt. v. 24.11.2005 – 2 C 34.04, BVerwGE 124, 356 = NVwZ 2006, 465 (Richtwerte und Vergleichsgruppe) ([dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerwG&Datum=2005-11-24&Aktenzeichen=2%20C%2034.04))
4. Zur landesrechtlichen Statthaftigkeit des Widerspruchs gegen Beurteilungen ist die Rechtsprechung des zuständigen OVG heranzuziehen `[unverifiziert - prüfen]`

## Ausgabeformat

```
DIENSTLICHE BEURTEILUNG — <Mandat> — <Datum>

I.   Anwendbares Recht
     Dienstherr:              <Bund / Land <X> / Kommune>
     Grundlage:               <§ 21 BBG + BLV | LBG <X> + LaufbahnVO>
     Richtlinie:              <Bezeichnung / Stand>

II.  Beurteilung
     Art:                     [Regelbeurteilung / Anlassbeurteilung]
     Zeitraum:                <von – bis>
     Gesamturteil:            <Note>   Vorbeurteilung: <Note>
     Beurteiler:              <…>      Zweitbeurteiler: <…>
     Eröffnet am:             <Datum>  Besprechung: [ja / nein]

III. Fehlerprüfung
     1. Verfahrensfehler:              [+ / –] <…>
     2. Unrichtiger Sachverhalt:       [+ / –] <…>
     3. Sachfremde Erwägungen:         [+ / –] <…>
     4. Allgemeingültige Wertmaßstäbe: [+ / –] <…>
     Richtwerte / Quotierung:          <Vergleichsgruppe, Größe, Anwendung>
     Plausibilisierung:                [erfolgt / verweigert / unzureichend]
     Absenkung ggü. Vorbeurteilung:    [begründet / unbegründet]

IV.  Rechtsbehelfe
     Gegenvorstellung:        [empfohlen — fristfrei]
     Widerspruch:             [statthaft? / Frist bis <Datum>]
     Klage:                   Antrag auf Neubeurteilung, VG <Ort>
     Paralleles Auswahlverfahren: [§ 123 VwGO erforderlich / nein]

V.   Risiko: 🟢 / 🟡 / 🔴 <Begründung>
VI.  Quellenverzeichnis
```

### Formulierungshilfe — Gegenvorstellung (Gerüst)

```
An <Beurteilerin / Beurteiler>
Gegenvorstellung gegen die dienstliche Beurteilung vom <Datum>

Sehr geehrte Frau / sehr geehrter Herr <…>,

gegen die mir am <Datum> eröffnete Beurteilung erhebe ich
Gegenvorstellung und bitte um Überprüfung und Neufassung.

1. Verfahren
   Ein Beurteilungsbeitrag der/des <Vorgesetzten> für den Zeitraum
   <…> liegt nicht vor, obwohl Ziffer <N> der Beurteilungsrichtlinie
   ihn vorsieht.

2. Sachverhalt
   Die Beurteilung geht davon aus, dass ich <…>. Tatsächlich <…>
   (Nachweis: <Vorgang / Vermerk / Zeugin>).

3. Herleitung des Gesamturteils
   Von <N> Einzelmerkmalen sind <M> mit <Note> bewertet. Das
   Gesamturteil <Note> ist daraus nicht hergeleitet; die Begründung
   wiederholt lediglich die Notenstufe. Ich bitte um Darlegung, auf
   welchen Tatsachen die Bewertung der Merkmale <…> beruht.

4. Vergleich zur Vorbeurteilung
   Bei unverändertem Aufgabenzuschnitt ist die Gesamtnote gegenüber
   der Beurteilung vom <Datum> um <N> Stufen abgesenkt worden. Ich
   bitte um Mitteilung, worauf die Absenkung beruht.

Ich rege ein Gespräch nach Ziffer <N> der Richtlinie an und behalte
mir weitere Rechtsbehelfe ausdrücklich vor.
```

## Risiken / typische Fehler

- **Angriff auf die Bewertung als solche.** „Ich verdiene eine bessere Note" ist unschlüssig; jeder Einwand muss einer der vier Fehlerkategorien zugeordnet werden.
- **Antrag auf eine bestimmte Note.** Das Gericht verpflichtet nur zur Neubeurteilung unter Beachtung seiner Rechtsauffassung.
- **Beurteilungsrichtlinie nicht beschafft.** Ohne die Richtlinie lassen sich weder Verfahrensfehler noch Abweichungen von der Selbstbindung darlegen.
- **Pauschales Bestreiten.** Die Plausibilisierungspflicht des Dienstherrn wird nur durch **substantiiertes** Bestreiten einzelner Merkmale ausgelöst.
- **Nur die Beurteilung angegriffen, das Auswahlverfahren nicht.** Die Beurteilungsklage hält keine Stelle frei; ohne parallelen Antrag nach § 123 VwGO wird die Stelle besetzt.
- **Quotierung ungeprüft hingenommen.** Richtwerte setzen eine hinreichend große und homogene Vergleichsgruppe voraus.
- **Aktenzeichen erfunden** — jede Entscheidung verifizieren oder als `[unverifiziert - prüfen]` kennzeichnen.
