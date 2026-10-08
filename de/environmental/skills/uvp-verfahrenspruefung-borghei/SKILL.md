---
name: uvp-verfahrenspruefung-borghei
title: /umweltrecht:uvp-verfahrenspruefung
description: Prüfung der Umweltverträglichkeitsprüfung – UVP-Pflicht nach § 5 UVPG i. V. m. Anlage 1, Vorprüfung des Einzelfalls § 7 UVPG (allgemeine/standortbezogene), Verfahrensschritte (Scoping § 15, Untersuchungsrahmen, Beteiligung § 18, Bewertung § 25), Verbindung mit immissionsschutzrechtlichem Trägerverfahren sowie Rechtsfolgen unterbliebener oder fehlerhafter UVP nach § 4 UmwRG. Use when ein Vorhaben UVP-Pflicht auslöst, eine Vorprüfung dokumentiert werden soll oder ein Verfahrensfehler im Genehmigungsbescheid geltend gemacht wird.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/umweltrecht/skills/uvp-verfahrenspruefung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: environmental
language: de
---

# /umweltrecht:uvp-verfahrenspruefung

## Zweck

Die UVP ist ein unselbstständiger Verfahrensteil eines Trägerverfahrens (z. B. immissionsschutzrechtliche Genehmigung, wasserrechtliche Erlaubnis, Planfeststellung). Sie ist umweltrechtlich tragend, weil Verfahrensfehler nach § 4 UmwRG zur Aufhebung der Trägerentscheidung führen können – auch ohne Verletzung subjektiver Rechte. Dieser Skill prüft UVP-Pflicht, Vorprüfung, Verfahrensschritte und Verfahrensfehler-Folgen.

## Eingaben

- Vorhabentyp und Dimensionierung (Anlage 1 UVPG-Bezug)
- Standort (Schutzgebiete, kumulative Vorhaben im Umfeld)
- Stand des Trägerverfahrens (Antrag, Bescheid, Klage)
- Bereits erfolgte Vorprüfung (Datum, Ergebnis, Dokumentation § 7 Abs. 7 UVPG)

## Sub-Agent-Architektur

Researcher liefert Anlage 1-Nummer, kumulative Konstellationen (§ 10 UVPG), einschlägige BVerwG- und EuGH-Rspr. zur UVP-RL. Drafter prüft UVP-Pflicht (obligatorisch oder Vorprüfung), führt Vorprüfung durch und ordnet Verfahrensschritte ein. Reviewer prüft § 4 UmwRG-Konsequenzen, Klagebefugnis und EU-Konformität.

## Ablauf

### 1. UVP-Pflicht § 5 UVPG i. V. m. Anlage 1

| Spalte | Folge |
|---|---|
| **„X"** | UVP obligatorisch (§ 6 UVPG) |
| **„A"** | Allgemeine Vorprüfung des Einzelfalls (§ 7 Abs. 1 UVPG) |
| **„S"** | Standortbezogene Vorprüfung (§ 7 Abs. 2 UVPG) |

Kumulationsregelungen § 10 UVPG (kumulierende Vorhaben), Änderungen § 9 UVPG.

### 2. Vorprüfung des Einzelfalls § 7 UVPG

| Anforderung | Inhalt |
|---|---|
| **Überschlägige Prüfung** | Anhand Kriterien Anlage 3 UVPG (Merkmale Vorhaben, Standort, Umweltauswirkungen) |
| **Dokumentation** | § 7 Abs. 7 UVPG: nachvollziehbar, schriftlich, vor Trägerentscheidung |
| **Eingeschränkte gerichtliche Kontrolle** | § 5 Abs. 3 UmwRG: Plausibilitätskontrolle |
| **Bekanntmachung** | § 5 Abs. 2 UVPG: Feststellung der UVP-Pflicht ist bekanntzugeben |

Maßstab: BVerwG, Urt. v. 25.06.2014 – 9 A 1/13, BVerwGE 150, 92 `[unverifiziert – prüfen]`; EuGH, Urt. v. 07.11.2018 – C-461/17 (Holohan), ECLI:EU:C:2018:883 `[unverifiziert – prüfen]`.

### 3. Verfahrensschritte der förmlichen UVP

| Schritt | Norm |
|---|---|
| **Unterrichtung über voraussichtl. Untersuchungsrahmen (Scoping)** | [§ 15 UVPG](https://www.gesetze-im-internet.de/uvpg/__15.html) |
| **UVP-Bericht des Vorhabenträgers** | [§ 16 UVPG](https://www.gesetze-im-internet.de/uvpg/__16.html) |
| **Beteiligung Behörden** | [§ 17 UVPG](https://www.gesetze-im-internet.de/uvpg/__17.html) |
| **Öffentlichkeitsbeteiligung** | [§ 18 UVPG](https://www.gesetze-im-internet.de/uvpg/__18.html) |
| **Grenzüberschreitende Beteiligung** | §§ 54 ff. UVPG |
| **Zusammenfassende Darstellung und begründete Bewertung** | [§§ 24, 25 UVPG](https://www.gesetze-im-internet.de/uvpg/__24.html) |
| **Berücksichtigung in Trägerentscheidung** | § 25 Abs. 2 UVPG |

### 4. Integration in das Trägerverfahren

- Immissionsschutzrecht: § 1 Abs. 2 der 9. BImSchV bindet die Verfahren zusammen; das immissionsschutzrechtliche Genehmigungsverfahren absorbiert die UVP.
- Wasserrecht: § 11 WHG i. V. m. UVPG.
- Planfeststellung: §§ 72 ff. VwVfG.

### 5. Rechtsfolgen von Verfahrensfehlern § 4 UmwRG

| Fehler | Folge |
|---|---|
| **Vollständig unterbliebene UVP / Vorprüfung** | § 4 Abs. 1 S. 1 Nr. 1 UmwRG: absoluter Aufhebungsgrund |
| **Fehlerhafte Vorprüfung** | § 4 Abs. 1 S. 2 UmwRG: gleichgestellt |
| **Sonstige Verfahrensfehler** | § 4 Abs. 1a UmwRG: Aufhebung nur bei Beeinflussungskausalität |
| **Klagebefugnis** | § 4 Abs. 3 UmwRG: gilt auch für betroffene Einzelne; Verbandsklage § 2 UmwRG |

Maßstab: EuGH, Urt. v. 07.11.2013 – C-72/12 (Altrip), ECLI:EU:C:2013:712 `[unverifiziert – prüfen]`; BVerwG, Urt. v. 17.12.2013 – 4 A 1/13, BVerwGE 148, 353 `[unverifiziert – prüfen]`.

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute

- [§ 5 UVPG](https://www.gesetze-im-internet.de/uvpg/__5.html) (UVP-Pflicht)
- [§ 7 UVPG](https://www.gesetze-im-internet.de/uvpg/__7.html) (Vorprüfung)
- [§ 9 UVPG](https://www.gesetze-im-internet.de/uvpg/__9.html) (Änderungen)
- [§ 10 UVPG](https://www.gesetze-im-internet.de/uvpg/__10.html) (Kumulation)
- [§ 15 UVPG](https://www.gesetze-im-internet.de/uvpg/__15.html) (Scoping)
- [§ 16 UVPG](https://www.gesetze-im-internet.de/uvpg/__16.html) (UVP-Bericht)
- [§ 18 UVPG](https://www.gesetze-im-internet.de/uvpg/__18.html) (Öffentlichkeitsbeteiligung)
- [§§ 24, 25 UVPG](https://www.gesetze-im-internet.de/uvpg/__24.html) (Darstellung und Bewertung)
- [Anlage 1 UVPG](https://www.gesetze-im-internet.de/uvpg/anlage_1.html)
- [Anlage 3 UVPG](https://www.gesetze-im-internet.de/uvpg/anlage_3.html)
- [§ 4 UmwRG](https://www.gesetze-im-internet.de/umwrg/__4.html) (Verfahrensfehler)
- [§ 2 UmwRG](https://www.gesetze-im-internet.de/umwrg/__2.html) (Verbandsklage)
- [UVP-RL 2011/92/EU](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32011L0092)

### Kommentare

- Hoppe/Beckmann, UVPG, 5. Aufl. 2018, § 5 Rn. 1 ff., § 7 Rn. 1 ff.
- Sangenstedt, in: Landmann/Rohmer, Umweltrecht (Loseblatt, Stand: 2024), § 7 UVPG Rn. 50 ff.
- Fellenberg/Schiller, in: Landmann/Rohmer, § 4 UmwRG Rn. 1 ff.
- Schink, in: Schink/Reidt/Mitschang, UVPG/UmwRG, 2018, § 4 UmwRG Rn. 10 ff.

### Rechtsprechung (`[unverifiziert – prüfen in Beck-Online/juris/BVerwG-/curia-Datenbank]`)

1. BVerwG, Urt. v. 25.06.2014 – 9 A 1/13, BVerwGE 150, 92 (Vorprüfung Plausibilitätskontrolle) `[unverifiziert – prüfen]`
2. BVerwG, Urt. v. 17.12.2013 – 4 A 1/13, BVerwGE 148, 353 (§ 4 UmwRG Aufhebung) `[unverifiziert – prüfen]`
3. EuGH, Urt. v. 07.11.2013 – C-72/12 (Altrip), ECLI:EU:C:2013:712 (Verfahrensfehler / Kausalität) `[unverifiziert – prüfen]`
4. EuGH, Urt. v. 07.11.2018 – C-461/17 (Holohan), ECLI:EU:C:2018:883 (Reichweite UVP) `[unverifiziert – prüfen]`
5. EuGH, Urt. v. 15.10.2015 – C-137/14 (Kommission/Deutschland), ECLI:EU:C:2015:683 (materielle Präklusion / Klagebefugnis) `[unverifiziert – prüfen]`

## Ausgabeformat

```
GUTACHTEN — UVP-Prüfung
<Mandat-Kürzel> — <Datum>

I.   Sachverhalt
     Vorhaben: <Typ, Dimensionierung>
     Standort: <Schutzgebiete, kumulative Vorhaben>
     Trägerverfahren: <BImSchG / WHG / Planfeststellung>
     Stand: <Antrag / Bescheid / Klage>

II.  Frage(n)
     1. Besteht UVP-Pflicht?
     2. Ist die durchgeführte Vorprüfung nachvollziehbar?
     3. Welche Verfahrensschritte stehen aus?
     4. (Falls Bescheid) Welche Konsequenzen hat ein Verfahrensfehler nach § 4 UmwRG?

III. Kurzantwort
     <ein Satz>

IV.  Rechtliche Bewertung (Gutachtenstil)
     1. UVP-Pflicht § 5 UVPG
        - Anlage 1 Nr. <…>, Spalte <X / A / S>
        - § 9 Änderungen / § 10 Kumulation
     2. Vorprüfung § 7 UVPG (sofern Spalte A/S)
        - Kriterien Anlage 3
        - Dokumentationspflicht § 7 Abs. 7
        - Plausibilitätskontrolle § 5 Abs. 3 UmwRG
     3. Verfahrensschritte
        - Scoping § 15 — UVP-Bericht § 16 — Beteiligung §§ 17, 18 — Bewertung §§ 24, 25
     4. Integration in Trägerverfahren
        - § 1 Abs. 2 9. BImSchV / § 11 WHG / Planfeststellung
     5. (Falls Bescheid) Verfahrensfehler § 4 UmwRG
        - absoluter Aufhebungsgrund (§ 4 Abs. 1)
        - Kausalitätsfehler (§ 4 Abs. 1a)
        - Klagebefugnis § 4 Abs. 3, § 2 UmwRG

V.   Gesamtergebnis
     <…>

VI.  Risiken / offene Punkte
     - Kumulative Vorhaben im 5-km-Umkreis
     - FFH-Vorprüfung parallel
     - Bekanntmachung § 5 Abs. 2 UVPG

VII. Risikoeinstufung
     [🟢 / 🟡 / 🔴]

VIII. Quellenverzeichnis
     <gem. zitierweise.md>
```

## Risiken / typische Fehler

- **Vorprüfung ohne Dokumentation** § 7 Abs. 7 UVPG → § 4 UmwRG-Aufhebungsgrund.
- **Kumulation § 10 UVPG übersehen** → Vorhaben unterhalb Schwelle wird durch Nachbarvorhaben UVP-pflichtig.
- **Spalte A/S verwechselt** → falscher Prüfungsmaßstab Anlage 3.
- **§ 4 Abs. 1 UmwRG und § 4 Abs. 1a UmwRG verwechselt** → Klage scheitert an Kausalitätsfehler-Argumentation, obwohl absoluter Aufhebungsgrund vorlag.
- **EuGH-Vorgaben (Altrip, Holohan) ignoriert** → richtlinienkonforme Auslegung verfehlt.
- **Klagebefugnis Einzelner** nach § 4 Abs. 3 UmwRG nicht erkannt → Klage zu früh als unzulässig verworfen.
