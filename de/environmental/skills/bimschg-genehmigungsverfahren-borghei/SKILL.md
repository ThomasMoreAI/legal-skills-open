---
name: bimschg-genehmigungsverfahren-borghei
title: /umweltrecht:bimschg-genehmigungsverfahren
description: Vollprüfung des immissionsschutzrechtlichen Genehmigungsverfahrens – Genehmigungsbedürftigkeit nach 4. BImSchV, Wahl zwischen förmlichem (§ 10 BImSchG) und vereinfachtem Verfahren (§ 19 BImSchG), Öffentlichkeitsbeteiligung nach 9. BImSchV, materielle Voraussetzungen § 5 BImSchG sowie Auflagen und Drittschutz. Use when Vorhabenträger eine Anlagengenehmigung beantragt, ein Bescheid auf Wirksamkeit / Anfechtbarkeit geprüft werden soll oder eine nachträgliche Anordnung § 17 BImSchG droht.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/umweltrecht/skills/bimschg-genehmigungsverfahren
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: environmental
language: de
---

# /umweltrecht:bimschg-genehmigungsverfahren

## Zweck

Das immissionsschutzrechtliche Genehmigungsverfahren ist die zentrale Eingriffs- und Steuerungsschnittstelle für Industrieanlagen. Wirksam ist eine Genehmigung nur, wenn formelle Voraussetzungen (richtiges Verfahren, Öffentlichkeitsbeteiligung, Behördenkonzentration § 13 BImSchG) und materielle Voraussetzungen (§ 5 BImSchG: Schutz-, Vorsorge-, Abfallvermeidungs- und Energieeffizienzpflicht) erfüllt sind. Dieser Skill prüft beides und ordnet Drittschutz, Nachbarklage und Verbandsklage ein.

## Eingaben

- Anlagentyp und Standort (Bundesland, Außen-/Innenbereich, Schutzgebiete)
- Beabsichtigte Tätigkeit und Kapazität (Mengenangaben, Leistung, Tierzahl)
- Vorhandener Bescheid oder Antrag (sofern vorhanden)
- Nachbarschaft (Wohnbebauung, FFH/Vogelschutz, Wasserschutzgebiet)
- Bauleitplanung am Standort (B-Plan, F-Plan, § 35 BauGB)

## Sub-Agent-Architektur

Researcher liefert 4. BImSchV-Anlagennummer, einschlägige TA-Regelwerke, BVerwG- und EuGH-Rechtsprechung. Drafter erstellt das Gutachten in der Reihenfolge formell → materiell → Drittschutz und prüft Auflagen-Tenorierung. Reviewer prüft EU-Konformität (IE-RL 2010/75/EU), Schutzgebietsbetroffenheit und Klagefristen.

## Ablauf

### 1. Genehmigungsbedürftigkeit nach § 4 BImSchG i. V. m. 4. BImSchV

| Schritt | Prüfung |
|---|---|
| **Anlagenkatalog** | Subsumtion unter Anhang 1 zur [4. BImSchV](https://www.gesetze-im-internet.de/bimschv_4_2013/anhang_1.html). Spalte c) bzw. d) entscheidet über das Verfahren |
| **Mengenschwellen** | Anlagen unterhalb der Schwelle: nicht genehmigungsbedürftig, fallen unter §§ 22 ff. BImSchG (Betreiberpflichten) |
| **Errichtungsschwelle vs. Änderungsgenehmigung** | § 16 BImSchG: wesentliche Änderung erfordert eigene Genehmigung |

### 2. Wahl des Verfahrens

| Verfahren | Norm | Folge |
|---|---|---|
| **Förmlich** | [§ 10 BImSchG](https://www.gesetze-im-internet.de/bimschg/__10.html) i. V. m. [9. BImSchV](https://www.gesetze-im-internet.de/bimschv_9/) | Öffentlichkeitsbeteiligung, Erörterungstermin, UVP-Integration § 4 UVPG |
| **Vereinfacht** | [§ 19 BImSchG](https://www.gesetze-im-internet.de/bimschg/__19.html) | Ohne Öffentlichkeitsbeteiligung – nur bei Spalte c)-Anlagen |
| **Anzeige § 15 BImSchG** | Unwesentliche Änderung | Keine Genehmigung, nur Anzeige |

Maßstab Verfahrensfehler: BVerwG, Urt. v. 22.10.2015 – 7 C 15/13, NVwZ 2016, 308 `[unverifiziert – prüfen]`; EuGH, Urt. v. 15.10.2015 – C-137/14 (Kommission/Deutschland) – materielle Präklusion mit Unionsrecht unvereinbar.

### 3. Materielle Genehmigungsvoraussetzungen § 5 BImSchG

| Pflicht | Norm | Inhalt |
|---|---|---|
| **Schutzpflicht** | § 5 Abs. 1 Nr. 1 BImSchG | Keine schädlichen Umwelteinwirkungen (TA Luft, TA Lärm); **drittschützend** |
| **Vorsorgepflicht** | § 5 Abs. 1 Nr. 2 BImSchG | Stand der Technik (§ 3 Abs. 6 BImSchG), BVT-Schlussfolgerungen IE-RL; **nicht drittschützend** (h.M., a.A. teils Jarass) |
| **Abfallvermeidung** | § 5 Abs. 1 Nr. 3 BImSchG | Verwertung, sonst Beseitigung |
| **Energieeffizienz** | § 5 Abs. 1 Nr. 4 BImSchG | Effiziente Energieverwendung |

### 4. Auflagen und Nebenbestimmungen § 12 BImSchG

- Bestimmtheit § 37 VwVfG (klar abgrenzbares Tun/Dulden/Unterlassen)
- Verhältnismäßigkeit (geeignet, erforderlich, angemessen)
- Modifizierende Auflage vs. nachträgliche Anordnung § 17 BImSchG abgrenzen
- Sicherheitsleistung § 12 Abs. 1 BImSchG, soweit Rekultivierung/Stilllegungspflicht

### 5. Drittschutz und Rechtsschutz

| Anspruchssteller | Grundlage |
|---|---|
| **Nachbar** | Klage gegen Genehmigung, gestützt auf drittschützende Normen (§ 5 Abs. 1 Nr. 1 BImSchG, ggf. § 15 BauNVO Rücksichtnahmegebot) |
| **Anerkannte Umweltvereinigung** | [§ 2 UmwRG](https://www.gesetze-im-internet.de/umwrg/__2.html), erweitert auf Verfahrensfehler nach [§ 4 UmwRG](https://www.gesetze-im-internet.de/umwrg/__4.html) |
| **Vorhabenträger** | Verpflichtungsklage auf Erteilung; Untätigkeitsklage § 75 VwGO |

### 6. Nachträgliche Anordnung und Stilllegung

- [§ 17 BImSchG](https://www.gesetze-im-internet.de/bimschg/__17.html) – nachträgliche Anordnung bei nachträglich erkannten Risiken oder geänderten Anforderungen (Stand der Technik)
- [§ 20 BImSchG](https://www.gesetze-im-internet.de/bimschg/__20.html) – Betriebsuntersagung, Stilllegung, Beseitigung; Anhörung § 28 VwVfG zwingend
- [§ 21 BImSchG](https://www.gesetze-im-internet.de/bimschg/__21.html) – Widerruf

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute / Verordnungen

- [§§ 4–7 BImSchG](https://www.gesetze-im-internet.de/bimschg/__4.html) (Genehmigung)
- [§ 5 BImSchG](https://www.gesetze-im-internet.de/bimschg/__5.html) (materielle Voraussetzungen)
- [§ 10 BImSchG](https://www.gesetze-im-internet.de/bimschg/__10.html) (Öffentlichkeitsbeteiligung)
- [§ 12 BImSchG](https://www.gesetze-im-internet.de/bimschg/__12.html) (Auflagen)
- [§ 13 BImSchG](https://www.gesetze-im-internet.de/bimschg/__13.html) (Konzentrationswirkung)
- [§ 17 BImSchG](https://www.gesetze-im-internet.de/bimschg/__17.html) (nachträgliche Anordnung)
- [§ 20 BImSchG](https://www.gesetze-im-internet.de/bimschg/__20.html) (Stilllegung)
- [§§ 22 ff. BImSchG](https://www.gesetze-im-internet.de/bimschg/__22.html) (nicht genehmigungsbedürftige Anlagen)
- [4. BImSchV](https://www.gesetze-im-internet.de/bimschv_4_2013/) (Anlagenkatalog)
- [9. BImSchV](https://www.gesetze-im-internet.de/bimschv_9/) (Verfahrensverordnung)
- [TA Luft 2021](https://www.bmuv.de/gesetz/erste-allgemeine-verwaltungsvorschrift-zum-bundes-immissionsschutzgesetz)
- [TA Lärm 1998](https://www.verwaltungsvorschriften-im-internet.de/bsvwvbund_26081998_IG19980826.htm)
- [IE-RL 2010/75/EU](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32010L0075)

### Kommentare

- Jarass, BImSchG, 14. Aufl. 2022, § 4 Rn. 1 ff., § 5 Rn. 1 ff., § 10 Rn. 1 ff.
- Dietlein, in: Landmann/Rohmer, Umweltrecht (Loseblatt, Stand: 2024), § 5 BImSchG Rn. 50 ff.
- Hansmann/Röckinghausen, in: Landmann/Rohmer, § 10 BImSchG Rn. 100 ff. (Öffentlichkeitsbeteiligung)
- Storost, in: Landmann/Rohmer, § 17 BImSchG Rn. 30 ff. (nachträgliche Anordnung)

### Rechtsprechung (`[unverifiziert – prüfen in Beck-Online/juris/BVerwG-Datenbank]`)

1. BVerwG, Urt. v. 22.10.2015 – 7 C 15/13, NVwZ 2016, 308 (Stand der Technik) `[unverifiziert – prüfen]`
2. BVerwG, Urt. v. 24.10.2013 – 7 C 36/11, BVerwGE 148, 155 (Drittschutz § 5 BImSchG) `[unverifiziert – prüfen]`
3. EuGH, Urt. v. 15.10.2015 – C-137/14, ECLI:EU:C:2015:683 (materielle Präklusion / UVP-RL) `[unverifiziert – prüfen]`
4. BVerwG, Urt. v. 21.11.2018 – 7 C 17/16, NVwZ 2019, 567 (Verbandsklage / § 4 UmwRG) `[unverifiziert – prüfen]`

## Ausgabeformat

```
GUTACHTEN — Immissionsschutzrechtliche Genehmigung
<Mandat-Kürzel> — <Datum>

I.   Sachverhalt
     Anlage: <Typ, Kapazität, Standort>
     Vorhaben: <Errichtung / Änderung / Anzeige>
     Umgebung: <Wohnbebauung, Schutzgebiete>

II.  Frage(n)
     1. Ist die Anlage genehmigungsbedürftig?
     2. Welches Verfahren ist einschlägig?
     3. Liegen die materiellen Voraussetzungen § 5 BImSchG vor?
     4. Welche Drittschutz-/Verbandsklagerisiken bestehen?

III. Kurzantwort
     <ein Satz>

IV.  Rechtliche Bewertung (Gutachtenstil)
     1. Genehmigungsbedürftigkeit § 4 BImSchG i. V. m. 4. BImSchV
        - Anlagennummer: <Anhang 1 Nr. …>
        - Spalte c) / d)
     2. Verfahren
        - § 10 BImSchG / § 19 BImSchG
        - Öffentlichkeitsbeteiligung 9. BImSchV
        - UVP-Integration § 4 UVPG (Verweis auf uvp-verfahrenspruefung)
     3. Materielle Voraussetzungen § 5 BImSchG
        a) Schutzpflicht — TA Luft / TA Lärm
        b) Vorsorgepflicht — Stand der Technik / BVT
        c) Abfallvermeidung
        d) Energieeffizienz
     4. Auflagen § 12 BImSchG
        - Bestimmtheit, Verhältnismäßigkeit
     5. Drittschutz und Verbandsklage
        - Nachbarklage (drittschützende Normen)
        - § 2 UmwRG / § 4 UmwRG

V.   Gesamtergebnis
     <…>

VI.  Risiken / offene Punkte
     - Emissionsprognose ausstehend
     - FFH-Vorprüfung erforderlich?
     - Schallgutachten (TA Lärm) aktualisieren

VII. Risikoeinstufung
     [🟢 / 🟡 / 🔴]

VIII. Quellenverzeichnis
     <gem. zitierweise.md>
```

## Risiken / typische Fehler

- **Falsche Anlagennummer** in 4. BImSchV → falsches Verfahren, formelle Rechtswidrigkeit.
- **Vereinfachtes Verfahren statt förmlichem** → Verbandsklage gewinnt nach § 4 UmwRG, weil Öffentlichkeitsbeteiligung fehlt.
- **Vorsorgepflicht mit Schutzpflicht verwechselt** → Drittschutz fehlerhaft bejaht/verneint.
- **Auflagen unbestimmt** (§ 37 VwVfG) → einzelne Nebenbestimmungen anfechtbar, Hauptgenehmigung wackelt nicht zwingend, aber Vollzug scheitert.
- **Stand der Technik veraltet** → Vorsorgepflicht verletzt, nachträgliche Anordnung § 17 BImSchG droht.
- **FFH-Verträglichkeit / Artenschutz übersehen** → kein Skill-Gegenstand i. e. S., aber Genehmigung scheitert an § 34/§ 44 BNatSchG.
