---
name: ausfuhr-dual-use-pruefung-borghei
title: /aussenwirtschaft-zoll-sanktionen:ausfuhr-dual-use-pruefung
description: 4-Stufen-Prüfung der Ausfuhrgenehmigungspflicht nach VO (EU) 2021/821 – Güterklassifikation Anhang I, Einzelgenehmigung bzw. EU-Allgemeine Genehmigungen IIa–IIg, Catch-all Art. 4 (militärische Endverwendung) und Art. 5 (Cyber-Surveillance), BAFA-Antrag ELAN-K2 mit Endverbleibsdokumentation. Use when ein deutscher Exporteur Güter in ein Drittland liefern will und Listung, Genehmigungspflicht oder Catch-all-Risiko prüfen muss; berücksichtigt Vorrang länderspezifischer Sanktions-VOen (Russland VO 833/2014, Iran VO 267/2012, DVRK VO 2017/1509 u.a.).
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/aussenwirtschaft-zoll-sanktionen/skills/ausfuhr-dual-use-pruefung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: trade
language: de
---

# /aussenwirtschaft-zoll-sanktionen:ausfuhr-dual-use-pruefung

## Zweck

Der Skill strukturiert die ausfuhrkontrollrechtliche Prüfung eines konkreten Ausfuhrvorhabens nach der EU-Dual-Use-VO (VO (EU) 2021/821) in vier Stufen: Güterklassifikation, Listungs-/Genehmigungsfolge, Catch-all-Risiko, Antragsverfahren beim BAFA. Er stellt den Vorrang länderspezifischer Sanktions-VOen klar und liefert dem internen Exportkontroll-Beauftragten und dem zugelassenen Anwalt eine reproduzierbare Entscheidungsgrundlage.

## Eingaben

- Gut: Bezeichnung, technische Spezifikation, Verwendungszweck (zivil/dual/militärisch), Kennwerte (z.B. Genauigkeit, Frequenz, Material, Rechenleistung, Verschlüsselungsstandard)
- Ausfuhrland (Drittland; bei Verbringung in andere EU-Mitgliedstaaten: gesonderter Prüfungsrahmen)
- Endverwender und Endverwendung („End-Use Statement"); ggf. Endverbleibserklärung (EVE/EUC) verfügbar
- Vermittler / Spediteur / Routing (Transitländer, insbesondere Risikoländer)
- Bekannte Listungs-Hinweise: Anhang I VO 2021/821 (Kategorien 0–9), Anlage AL der AWV
- Hinweise auf Sanktionsbezug (Russland, Iran, Syrien, DVRK, Belarus, Myanmar etc.)
- Ggf. vorhandene Genehmigungen / Nullbescheide / vZTA-Klassifizierung

## Sub-Agent-Architektur

Researcher liefert die einschlägigen Statute (VO 2021/821, AWG/AWV, ggf. länderspezifische Sanktions-VOen), BAFA-Merkblätter, EuGH-Rspr. und Kommentarstellen (Friedrich/Lieser, Hocke/Sachs/Pelz, Krenzler/Herrmann/Niestedt). Drafter führt die 4-Stufen-Prüfung im Gutachtenstil durch und entwirft ggf. Begleitschreiben zum BAFA-Antrag (ELAN-K2). Reviewer prüft Sanktions-Vorrang, EU-AGG-Anwendbarkeit, Catch-all-Subjektivelement und Strafbarkeitsrisiko § 18 AWG.

## Ablauf

### 1. Stufe 1 – Sanktions- und Embargo-Vorprüfung

**Vor** jeder Dual-Use-Prüfung klären: Liegt ein länderspezifisches Embargo vor? Sanktions-VOen sind regelmäßig strenger und vorrangig:

- **Russland:** VO (EU) 833/2014, 269/2014, 692/2014 (Krim/Donezk/Luhansk); umfangreiche Güterembargos (z.B. Anhänge VII, X, XXIII)
- **Iran:** VO (EU) 267/2012 (Atom-/Proliferations-bezogen)
- **Syrien:** VO (EU) 36/2012
- **DVRK:** VO (EU) 2017/1509
- **Belarus:** VO (EG) 765/2006
- **Myanmar:** VO (EU) 401/2013

Bei sanktionsbezogenem Risiko → Übergang zum Skill `sanktionslisten-screening` **und** Fortsetzung der Dual-Use-Prüfung; das eine schließt das andere nicht aus.

### 2. Stufe 2 – Güterklassifikation (Anhang I VO 2021/821 / Anlage AL)

Prüfung in folgender Reihenfolge:

1. **Anhang I VO (EU) 2021/821** – Güterliste in zehn Kategorien (Kat. 0 Kernmaterial, Kat. 1 Werkstoffe/Chemikalien/Mikroorganismen, Kat. 2 Werkstoffbearbeitung, Kat. 3 Elektronik, Kat. 4 Rechner, Kat. 5 Telekommunikation/Informationssicherheit, Kat. 6 Sensoren/Laser, Kat. 7 Luftfahrt/Navigation, Kat. 8 Meerestechnik, Kat. 9 Luft-/Raumfahrt/Antrieb).
2. **Anlage AL der AWV, Teil I A** – nationale deutsche Güterliste (zusätzliche Genehmigungspflichten über die EU-Liste hinaus).
3. **Anlage AL Teil I B** – Güter mit Spezifikation für Dual-Use, gemeinsam mit Teil I A nur deutsche Spezifika.

Erfasse die Listenposition (z. B. „1A002", „3A001a3b") und den genauen Spezifikations-Cluster. Wenn das Gut technisch knapp unterhalb der Schwelle liegt, **dokumentieren**: bewusste Listungsumgehung kann subjektiv § 18 AWG erfüllen.

### 3. Stufe 3 – Genehmigungsfolge

**Wenn gelistet (Anhang I oder Anlage AL):** Ausfuhrgenehmigung erforderlich (Art. 3 VO 2021/821; §§ 8 ff. AWV). Prüfen, ob eine EU-Allgemeine Genehmigung greift (Anhänge II VO 2021/821):

| EU-AGG | Anhang | Reichweite |
|---|---|---|
| EU001 | IIa | Ausfuhr in „weiße Liste": USA, CA, AU, JP, NZ, NO, CH, IS, UK, LI (Stand: regelmäßig zu verifizieren) |
| EU002 | IIb | Bestimmte Güter Ausfuhr nach AR/BR/CL/IN/MX/SG/ZA/TR (eingeschränkter Katalog) |
| EU003 | IIc | Ausfuhr nach Reparatur / Ersatz |
| EU004 | IId | Vorübergehende Ausfuhr (Ausstellung, Wartung) |
| EU005 | IIe | Telekommunikation |
| EU006 | IIf | Chemikalien |
| EU007 | IIg | Konzerninterne Ausfuhr von Software/Technologie |

Voraussetzungen jeder EU-AGG: Registrierungspflicht beim BAFA, Berichtspflichten, Ausschluss bei militärischer Endverwendung oder Sanktionsbezug.

**Wenn keine EU-AGG greift:** Einzel- oder Sammelgenehmigung beim BAFA über ELAN-K2 beantragen. Bearbeitungsdauer üblicherweise **10–12 Wochen**, bei Iran/Russland/sensitiven Gütern länger. Pflichtdokumente: Endverbleibserklärung (EUC), technische Spezifikation, ggf. Endverwender-Compliance-Erklärung.

### 4. Stufe 4 – Catch-all

**Auch bei nicht gelisteten Gütern** gilt eine Genehmigungspflicht, wenn ein Catch-all-Tatbestand greift:

- **Art. 4 Abs. 1 VO 2021/821** – militärische Endverwendung in einem Waffenembargoland oder vom BAFA mitgeteilt
- **Art. 4 Abs. 2 VO 2021/821** – Bestimmung für militärische Endverwender (Anhang Embargoländerliste)
- **Art. 5 VO 2021/821** – Cyber-Surveillance-Güter mit Risiko schwerwiegender Menschenrechtsverletzungen
- **§ 9 AWV** – nationaler Catch-all (Kriegswaffen-/Kernsprengkörper-/Trägertechnologie-Verwendung)

Subjektives Element: **„Kenntnis"** **oder** **Unterrichtung durch die zuständige Behörde** (BAFA). Bei begründetem Verdacht: BAFA-Auskunftsverfahren / „Nullbescheid"-Anfrage.

### 5. BAFA-Antrag

Antragsweg: **ELAN-K2** (Elektronisches Antrags-, Lizenz- und Auskunftssystem). Inhalt:

- Antragsteller (Ausführer iSv Art. 2 Nr. 3 VO 2021/821)
- Empfänger und Endverwender (Klarnamen, Adresse)
- Gut (Bezeichnung, technische Spezifikation, Listenposition)
- Wert, Menge, beabsichtigter Versandzeitpunkt
- Endverwendung
- **Endverbleibserklärung** (EUC) als Anlage
- bei sensitiven Gütern: Compliance-Programm-Nachweis, Innerbetriebliches Exportkontroll-Programm (ICP)

Wartepflicht: **kein Versand vor schriftlicher Genehmigung** (§§ 8, 9 AWV). Verstoß: § 18 Abs. 1 AWG, Freiheitsstrafe **bis 5 Jahre**, gewerbsmäßig **bis 15 Jahre**, fahrlässig Geldbuße § 19 AWG.

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Primär- und Sekundärrecht

- [VO (EU) 2021/821 (Dual-Use-VO)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32021R0821)
- [Art. 215 AEUV (Sanktionsrechtsgrundlage)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:12012E215)
- [AWG](https://www.gesetze-im-internet.de/awg_2013/) – insb. §§ 4, 8, 17–19
- [AWV](https://www.gesetze-im-internet.de/awv_2013/) – Teil 5, Anlage AL
- [KrWaffG](https://www.gesetze-im-internet.de/krwaffkontrg/) – insb. § 18
- ggf. länderspezifische Sanktions-VO mit Anhängen (Russland: VO 833/2014, 269/2014; Iran: VO 267/2012; DVRK: VO 2017/1509)

### Behördliche Quellen

- BAFA, Merkblatt „Ausfuhrkontrolle und Wirtschaft" (jeweils aktuelle Fassung)
- BAFA-Handbuch Exportkontrolle
- ELAN-K2-Antragsverfahren (bafa.de)

### Kommentare

- Hocke, in: Hocke/Sachs/Pelz, AWG/AWV, Stand 2024, § 4 AWG Rn. 1 ff.
- Wolffgang/Niestedt, in: Krenzler/Herrmann/Niestedt, EU-Außenwirtschafts- und Zollrecht, Stand 2024, VO 2021/821 Art. 3 Rn. 1 ff.
- Friedrich/Lieser, Außenwirtschaftsrecht, 1. Aufl. 2023, Kap. zu Dual-Use.

### Rechtsprechung (`[unverifiziert – prüfen in curia.europa.eu / juris]`, soweit markiert)

1. EuGH, Urt. v. 28.03.2017 – Rs. C-72/15, Rosneft, ECLI:EU:C:2017:236 (Gültigkeit und Auslegung der Russland-Maßnahmen, Reichweite VO 833/2014; Zuständigkeit des EuGH für GASP-gestützte Sanktionen), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2017-03-28&Aktenzeichen=C-72/15)
2. EuGH, Urt. v. 29.03.2011 – verb. Rs. C-201/09 P, C-216/09 P, ArcelorMittal Luxembourg/Kommission — die Entscheidung existiert unter diesem Datum und Aktenzeichen, betrifft aber **Kartellrecht (Trägerkartell, Art. 65 EGKS, Zuständigkeit der Kommission nach Auslaufen des EGKS-Vertrags)** und hat keinen exportkontrollrechtlichen Gegenstand; die Angabe „zur Anwendung des Unionsrechts" trägt in diesem Kontext nicht `[unverifiziert – Einschlägigkeit für die Ausfuhrkontrolle prüfen oder Zitat streichen]`, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2011-03-29&Aktenzeichen=C-201/09)
3. BGH, Urt. zu § 34 AWG a.F. / § 18 AWG (Dual-Use-Strafverfahren) — ohne Aktenzeichen und Datum nicht recherchierbar `[unverifiziert – prüfen]`

## Ausgabeformat

```
GUTACHTEN — Ausfuhrgenehmigungspflicht nach VO (EU) 2021/821
Vorhaben: <Gut, Empfänger, Drittland>
Stand: <Datum>

I. Sachverhalt
   - Gut (techn. Spezifikation):
   - Endverwender / Endverwendung:
   - Drittland / Routing:
   - Sanktionsbezug (vorab):

II. Kurzantwort
    Ampel: 🟢 / 🟡 / 🔴
    Empfehlung: <Versand zulässig / Antrag erforderlich / BLOCKER>

III. Rechtliche Bewertung
     1. Stufe 1 – Sanktions-/Embargo-Vorprüfung
        - länderspezifische VO: <ja/nein, welche>
     2. Stufe 2 – Güterklassifikation
        - Anhang I VO 2021/821: <Listenposition oder „nicht gelistet">
        - Anlage AL AWV: <Position oder „nicht gelistet">
     3. Stufe 3 – Genehmigungsfolge
        - Einzel-/Sammelgenehmigung erforderlich? <ja/nein>
        - EU-AGG anwendbar? <EU00X oder „nein">
     4. Stufe 4 – Catch-all
        - Art. 4 VO 2021/821 (militärische Endverwendung): <Prüfung>
        - Art. 5 VO 2021/821 (Cyber-Surveillance): <Prüfung>
        - § 9 AWV (nationaler Catch-all): <Prüfung>

IV. Antragsweg (falls erforderlich)
    - BAFA ELAN-K2, Bearbeitungsdauer ca. 10–12 Wochen
    - Pflichtdokumente: EUC, technische Spezifikation, ICP
    - Wartepflicht: kein Versand vor schriftlicher Genehmigung

V. Risiken / offene Punkte
   - Endverbleibsklärung
   - Strafbarkeitsrisiko § 18 AWG (Freiheitsstrafe bis 5 / 15 Jahre)
   - Wiedervorlage: <Datum>

VI. Quellenverzeichnis
```

## Risiken / typische Fehler

- **Sanktions-Vorrang übersehen.** Russland-/Iran-/DVRK-Bezug muss vor Dual-Use-Prüfung adressiert werden; länderspezifische VO ist regelmäßig strenger.
- **Catch-all nicht geprüft.** „Nicht gelistet" heißt nicht „genehmigungsfrei". Art. 4/5 VO 2021/821 und § 9 AWV bei jedem Vorhaben mitprüfen.
- **EU-AGG ohne Registrierung genutzt.** EU-AGGs erfordern Registrierung beim BAFA und Berichtspflichten; ungemeldete Nutzung ist ordnungswidrig.
- **Versand vor Genehmigung.** „Wir warten erstmal nicht ab" → § 18 Abs. 1 AWG, Freiheitsstrafe bis 5 Jahre (gewerbsmäßig bis 15 Jahre).
- **EUC ohne Verifizierung der Echtheit.** BAFA prüft Endverbleibsdokumentation; gefälschte EUC können Strafbarkeit auf Ausführer durchschlagen lassen.
- **Technische Spezifikation knapp unterhalb der Listungsschwelle.** Dokumentieren, sonst Verdacht bewusster Listungsumgehung.
- **Bezug auf US-Recht** (EAR, „Reexport") als verbindlich behandeln — US-Recht ist parallel zu prüfen, aber **keine deutsche Rechtsgrundlage**; Verweis auf US-Counsel.
