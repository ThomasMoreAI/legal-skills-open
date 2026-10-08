---
name: jahresbericht-1863-bgb-borghei
title: /betreuungsrecht:jahresbericht-1863-bgb
description: 'Jahresbericht des Betreuers an das Betreuungsgericht nach § 1863 BGB (Reform 2023). Pflichtinhalt: Bericht über persönliche Verhältnisse der betreuten Person, Vermögensentwicklung, geplante Maßnahmen. Pflichtbestandteile, Vorlagefrist, Abgrenzung zur Rechnungslegung § 1865 BGB. Use when ein beruflicher Betreuer den Jahresbericht erstellt oder die Vollständigkeit eines vorliegenden Berichts überprüft wird.'
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/betreuungsrecht/skills/jahresbericht-1863-bgb
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: family
language: de
---

# /betreuungsrecht:jahresbericht-1863-bgb

## Zweck

Der Jahresbericht nach der Betreuungsrechtsreform 2023 (§ 1863 BGB) ist das zentrale Steuerungsdokument der gerichtlichen Aufsicht. Eine unvollständige oder verspätete Vorlage kann zu Anordnungen, im Wiederholungsfall zur Aufhebung der Betreuung führen. Dieser Skill strukturiert den Bericht entlang der Pflichtinhalte.

## Eingaben

- Aufgabenkreis der Betreuung (Vermögenssorge, Gesundheitssorge, Aufenthaltsbestimmung, etc.)
- Berichtszeitraum (in der Regel 12 Monate)
- Persönliche Lebenssituation der betreuten Person
- Wesentliche Maßnahmen im Berichtszeitraum
- Vermögensentwicklung (Konten, Verträge, Forderungen)
- Geplante Maßnahmen im Folgezeitraum

## Ablauf

### 1. Pflichtinhalt § 1863 Abs. 1 BGB

Der Bericht enthält:

1. **Angaben zur Person**, einschließlich gesundheitlicher und sozialer Situation
2. **Bericht über die persönlichen Verhältnisse** und über die Erledigung der Aufgaben des Betreuers
3. **Bericht über das Vermögen**, einschließlich Veränderungen seit dem letzten Bericht
4. **Mitteilung künftiger Maßnahmen**

Der Bericht ist **schriftlich** vorzulegen.

### 2. Pflichten in der Vermögenssorge

Bei Aufgabenkreis Vermögenssorge zusätzlich:

#### a) Bestands-Aufstellung

- Stand Konten (Giro, Sparbuch, Wertpapierdepot)
- Forderungen / Verbindlichkeiten
- Immobilienbesitz und etwaige Belastungen
- Sonstiges Vermögen

#### b) Vermögensverzeichnis (§ 1835 BGB)

Zu Beginn der Betreuung, danach bei wesentlichen Änderungen.

#### c) Rechnungslegung (§ 1865 BGB)

Jährlich vorzulegen, Einnahmen und Ausgaben. **Separat vom Jahresbericht!**

### 3. Genehmigungspflichtige Geschäfte

Im Berichtszeitraum durchgeführte oder geplante Maßnahmen, die Genehmigung erfordern (§§ 1848 ff. BGB):

- **§ 1848 BGB** (Grundstücksgeschäfte)
- **§ 1849 BGB** (Erbschaft annehmen / ausschlagen)
- **§ 1850 BGB** (Schenkungen aus dem Vermögen)
- **§ 1851 BGB** (Aufgabe von Sicherheiten)
- **§ 1831 BGB** (Geschäfte über Wohnraum)
- **§ 1832 BGB** (Anlage von Geld)

### 4. Vorlagepflicht

- **Jährlich** bei laufender Betreuung (§ 1863 Abs. 2 BGB)
- **Sofort** bei Beendigung (Schlussbericht) (§ 1872 BGB)
- Versäumnis führt zu gerichtlichem Hinweis, gegebenenfalls Zwangsgeld

### 5. Verzahnung mit anderen Pflichten

- **Mitteilungspflicht** nach § 1864 BGB (außergewöhnliche Ereignisse)
- **Anhörungsrecht** der betreuten Person (§ 1862 BGB)
- **Berücksichtigung der Wünsche und Vorstellungen** der betreuten Person (§ 1821 BGB — Reform 2023)

### 6. Form und Sprache

- Klare, sachliche Sprache
- Vermeidung medizinisch-stigmatisierender Begriffe
- Konkret mit Daten und Beträgen
- Anlagen: Belege zu wesentlichen Punkten

### 7. Datenschutz

DSGVO-konforme Verarbeitung. Bericht ist intern beim Gericht, aber:

- Recht der betreuten Person auf Auskunft (Art. 15 DSGVO)
- Vorsicht bei Angaben Dritter (gesundheitliche, finanzielle Lage der Angehörigen)

## Quellen

### Statute (Reform 2023)

- [§ 1863 BGB](https://www.gesetze-im-internet.de/bgb/__1863.html) (Jahresbericht)
- [§ 1865 BGB](https://www.gesetze-im-internet.de/bgb/__1865.html) (Rechnungslegung)
- [§ 1835 BGB](https://www.gesetze-im-internet.de/bgb/__1835.html) (Vermögensverzeichnis)
- [§§ 1848, 1849, 1850, 1851 BGB](https://www.gesetze-im-internet.de/bgb/__1848.html) (Genehmigungspflicht)
- [§ 1831, § 1832 BGB](https://www.gesetze-im-internet.de/bgb/__1831.html)
- [§ 1862 BGB](https://www.gesetze-im-internet.de/bgb/__1862.html) (Anhörung)
- [§ 1864 BGB](https://www.gesetze-im-internet.de/bgb/__1864.html) (Mitteilung)
- [§ 1872 BGB](https://www.gesetze-im-internet.de/bgb/__1872.html) (Schlussbericht)
- [BtOG (Betreuungsorganisationsgesetz)](https://www.gesetze-im-internet.de/btog/)

### Kommentare

- Brückner / Müller, in: Jürgens / Marschner, BtR, 8. Aufl. 2024
- Diener / Frank, in: Damrau / Zimmermann, Betreuung und Vorsorge

### Soft Law

- BMJ-Hinweise zur Betreuungsrechtsreform 2023
- DAV-Stellungnahme zur Reform

## Ausgabeformat

```
JAHRESBERICHT § 1863 BGB — Betreuung <Name> — Berichtszeitraum <…>

I.    Angaben zur Person
      Gesundheitliche Situation:      <…>
      Wohn- und Lebenssituation:      <…>
      Soziale Kontakte:               <…>

II.   Bericht über persönliche Verhältnisse
      Wesentliche Veränderungen:      <…>
      Eigene Wünsche der Person § 1821 BGB:  <…>

III.  Bericht über die Erledigung der Aufgaben
      Aufgabenkreis 1 (z. B. Vermögenssorge):  <Maßnahmen>
      Aufgabenkreis 2 (z. B. Gesundheitssorge): <Maßnahmen>

IV.   Vermögensbericht (bei Vermögenssorge)
      Konten:                         <Übersicht>
      Vermögensveränderungen:         <…>
      Anlagen:                        <…>
      Genehmigungspflichtige Geschäfte (§§ 1848 ff.): <…>

V.    Geplante Maßnahmen im Folgezeitraum
      <…>

Berichtsstelle, Datum, Unterschrift
```

## Risiken / typische Fehler

- **Bericht und Rechnungslegung vermischt** — getrennte Pflichten.
- **Eigener Wille der betreuten Person fehlt** — Reform 2023 verlangt aktive Berücksichtigung (§ 1821 BGB).
- **Genehmigungspflichtige Geschäfte unerwähnt** — ist Aufsichtsfehler des Gerichts vorprogrammiert.
- **Stigmatisierende Sprache** — DSGVO und Würde der Person.
- **Schlussbericht bei Beendigung vergessen** — § 1872 BGB Pflicht.
- **Verspätung** — gerichtliches Zwangsgeld, im Wiederholungsfall Aufhebung der Bestellung.
