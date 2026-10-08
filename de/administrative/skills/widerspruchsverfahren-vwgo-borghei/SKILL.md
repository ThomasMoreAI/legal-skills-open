---
name: widerspruchsverfahren-vwgo-borghei
title: /verwaltungsrecht:widerspruchsverfahren-vwgo
description: Widerspruchsverfahren gegen Verwaltungsakte nach §§ 68 ff. VwGO. Statthaftigkeit, Form, Frist (1 Monat ab Bekanntgabe § 70 VwGO), aufschiebende Wirkung § 80 VwGO, Widerspruchsbescheid und Klagevoraussetzung. Use when ein Mandant einen belastenden Verwaltungsakt erhalten hat und Rechtsschutz im Vorverfahren begehrt.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/verwaltungsrecht/skills/widerspruchsverfahren-vwgo
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: administrative
language: de
---

# /verwaltungsrecht:widerspruchsverfahren-vwgo

## Zweck

Das Widerspruchsverfahren ist häufig Zugangsvoraussetzung zur verwaltungsgerichtlichen Klage und gleichzeitig die wirtschaftlichste Korrekturchance vor Klageweg. Frist- und Formfehler schließen ohne Wiedereinsetzung jeden weiteren Rechtsschutz aus.

## Eingaben

- Verwaltungsakt (Adressat, Behörde, Datum, Inhalt, Rechtsbehelfsbelehrung)
- Bekanntgabedatum (Zustellung mit PZU vs. einfacher Brief, vs. elektronisch)
- Hauptanliegen (Anfechtung / Verpflichtung / Feststellung)
- Verfahrensvorgeschichte (Anhörung erfolgt?)
- Eilbedürftigkeit (Vollziehbarkeit?)

## Ablauf

### 1. Statthaftigkeit ([§ 68 VwGO](https://www.gesetze-im-internet.de/vwgo/__68.html))

Widerspruch ist statthaft gegen:

- Anfechtungsklage-fähige VA (Anfechtungswiderspruch)
- Verpflichtungsklage-fähige Untätigkeits-/Ablehnungssituationen (Verpflichtungswiderspruch)

**Ausnahmen vom Vorverfahren** (Landesrecht oder § 68 Abs. 1 S. 2 VwGO):

- Bundesoberbehörden in vielen Bereichen
- Landesgesetzliche Ausnahmen (z. B. NRW hat Vorverfahren weitgehend abgeschafft)

### 2. Form ([§ 70 VwGO](https://www.gesetze-im-internet.de/vwgo/__70.html))

- **Schriftlich** oder **zur Niederschrift** bei der Behörde
- **Elektronisch** mit qualifizierter Signatur möglich
- Inhalt: Bezeichnung des angegriffenen VA, Anfechtungswillen erkennbar
- Empfehlung: Begründung (kann nachgereicht werden)

### 3. Frist ([§ 70 VwGO](https://www.gesetze-im-internet.de/vwgo/__70.html))

- **1 Monat** ab Bekanntgabe
- Bei unrichtiger Rechtsbehelfsbelehrung: **1 Jahr** (§ 58 Abs. 2 VwGO)
- Berechnung nach §§ 187 ff. BGB i.V.m. § 57 VwGO

**Wiedereinsetzung** § 60 VwGO bei unverschuldeter Versäumnis (2 Wochen ab Wegfall des Hindernisses).

### 4. Aufschiebende Wirkung ([§ 80 VwGO](https://www.gesetze-im-internet.de/vwgo/__80.html))

#### Regel: Aufschiebende Wirkung

Widerspruch hat aufschiebende Wirkung (§ 80 Abs. 1 VwGO).

#### Ausnahmen § 80 Abs. 2 VwGO

- Öffentliche Abgaben und Kosten
- Unaufschiebbare Anordnungen der Polizei
- Verwaltungsakte mit angeordneter sofortiger Vollziehung
- Sonstige bundes- oder landesgesetzliche Anordnungen

#### Rechtsschutz bei fehlender aufschiebender Wirkung

- **Antrag § 80 Abs. 4 VwGO** (Aussetzung durch Behörde)
- **Antrag § 80 Abs. 5 VwGO** (gerichtliche Aussetzung)

### 5. Aufschiebende Wirkung wiederherstellen § 80 Abs. 5 VwGO

Antrag beim Verwaltungsgericht. Voraussetzungen:

- Rechtmäßigkeitszweifel oder
- Vollziehungsinteresse-Abwägung zugunsten des Antragstellers

### 6. Widerspruchsbehörde und -bescheid

- **Ausgangsbehörde** prüft Abhilfe
- **Nächsthöhere Behörde** entscheidet bei Nichtabhilfe
- Widerspruchsbescheid mit Rechtsbehelfsbelehrung

### 7. Übergang in Klageverfahren

Klage zum Verwaltungsgericht binnen **1 Monat** ab Zustellung des Widerspruchsbescheids (§§ 74, 42 VwGO). Ausnahme: Untätigkeitsklage § 75 VwGO nach 3 Monaten ohne Bescheid.

### 8. Kosten

- Widerspruchsverfahren ist nicht zwingend kostenpflichtig (bundeslandabhängig)
- Anwaltskosten erstattbar nur bei Aufhebung / Abänderung des VA und entsprechender Erstattung

## Quellen

### Statute

- [§§ 68–73 VwGO](https://www.gesetze-im-internet.de/vwgo/__68.html) (Vorverfahren)
- [§ 80 VwGO](https://www.gesetze-im-internet.de/vwgo/__80.html) (Aufschiebende Wirkung)
- [§§ 42, 74, 75, 113 VwGO](https://www.gesetze-im-internet.de/vwgo/__42.html)
- [§§ 35, 41 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__35.html) (Verwaltungsakt, Bekanntgabe)

### Kommentare

- Kopp / Schenke, VwGO, 30. Aufl. 2024
- Stelkens / Bonk / Sachs, VwVfG, 10. Aufl. 2023
- Schoch / Schneider, VwGO (Loseblatt)

### Rechtsprechung

- BVerwG, Urt. v. 14.07.1999 – 6 C 7/98, NVwZ 2000, 70 (Widerspruchsfrist) `[unverifiziert – prüfen]`
- BVerwG, Beschl. v. 22.02.2018 – 7 B 14.17, NVwZ 2018, 813 (§ 80 Abs. 5) `[unverifiziert – prüfen]`

## Ausgabeformat

```
WIDERSPRUCHSVERFAHREN — <Mandat> — <Datum>

I.    Verwaltungsakt
      Behörde:                        <…>
      Datum / Bekanntgabe:            <…> / <…>
      Inhalt:                         <Belastung / Ablehnung>
      Rechtsbehelfsbelehrung:         [korrekt / fehlerhaft]

II.   Statthaftigkeit                 [✓ / ausgeschlossen wegen <…>]

III.  Frist
      1-Monats-Frist:                 läuft bis <Datum>
      Verlängert auf 1 Jahr:          [N/A / ja, wegen unrichtiger Belehrung]
      Wiedereinsetzung erforderlich:  [nein / ja]

IV.   Form
      Schriftlich / Niederschrift / elektronisch:  <gewählt>

V.    Aufschiebende Wirkung
      Wirkung des Widerspruchs:       [aufschiebend / sofort vollziehbar]
      Anordnung sofortige Vollziehung: [N/A / vorhanden]
      Antrag § 80 Abs. 5:             [erforderlich / nicht]

VI.   Begründung
      Rechtsgrund:                    <…>
      Tatsachenvortrag:               <…>

VII.  Folgemaßnahmen
      Klage vor VG bei Misserfolg:    Frist <Datum>

Empfehlung: <…>
```

## Risiken / typische Fehler

- **Frist verpasst** — ohne Wiedereinsetzung Bestandskraft, kein Klageweg mehr.
- **Sofortige Vollziehung übersehen** — Widerspruch hat dann keine aufschiebende Wirkung.
- **Klage statt Widerspruch erhoben, obwohl Vorverfahren statthaft** — Klage unzulässig.
- **Untätigkeitsklage zu früh erhoben** — § 75 VwGO verlangt 3 Monate.
- **Bekanntgabezeitpunkt falsch berechnet** — § 41 Abs. 2 VwVfG, 3-Tages-Fiktion bei einfacher Bekanntgabe.
- **Rechtsbehelfsbelehrung-Fehler nicht erkannt** — die 1-Jahres-Frist erkennen und nutzen.
- **§ 80 Abs. 5-Antrag mit Hauptantrag verwechselt** — der Eilantrag ist eigenständig.
