---
name: klageschrift-zivilprozess-borghei
title: /prozessrecht:klageschrift-zivilprozess
description: Entwurf einer prozessual sauberen Klageschrift im Zivilprozess nach §§ 253 ff. ZPO. Streitgegenstand (zweigliedriger Begriff), Sachvortrag mit Substantiierung, Beweisantritt, sachliche und örtliche Zuständigkeit, Klagearten (Leistungs-, Feststellungs-, Gestaltungsklage), Streitwert. Use when eine Zivilklage entworfen wird oder eine Klageschrift auf prozessuale Mängel geprüft wird.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/prozessrecht/skills/klageschrift-zivilprozess
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: litigation
language: de
---

# /prozessrecht:klageschrift-zivilprozess

## Zweck

Eine Klageschrift entscheidet den Prozess vor der ersten mündlichen Verhandlung. Fehler bei Streitgegenstand, Bestimmtheit des Antrags oder unzureichendem Sachvortrag führen zu Klageabweisung als unzulässig oder unbegründet (Schlussurteil ohne Beweisaufnahme). Dieser Skill stellt die Sollbruchstellen ab.

## Eingaben

- Sachverhalt (anonymisiert) mit Vertrag, Verletzungshandlung, Schadensbild
- Parteien (Name, Anschrift, Rechtsform, gesetzliche Vertretung)
- Anspruchsgrundlage (vertraglich / deliktisch / Bereicherung — Reihenfolge siehe `references/methodik.md`)
- Streitwert
- Beweismittel (Urkunden, Zeugen, Sachverständige)
- Gerichtsstand-Ueberlegungen (Wahlrecht?)

## Ablauf

### 1. Formale Voraussetzungen ([§ 253 ZPO](https://www.gesetze-im-internet.de/zpo/__253.html))

#### Mussinhalt § 253 Abs. 2 ZPO

- **Parteien** (mit gesetzlichen Vertretern)
- **Gericht**
- **Bestimmter Antrag** (Leistungsklage: was und wie viel; Feststellungsklage: was; Gestaltungsklage: was)
- **Anspruchsgrund** (Lebenssachverhalt, der den Anspruch trägt)

#### Sollinhalt § 253 Abs. 4 ZPO

- Beweismittel zu jedem behaupteten Tatsachen
- Wert des Streitgegenstands

### 2. Streitgegenstand (zweigliedriger Begriff)

- **Antrag** + **Lebenssachverhalt** (BGH, st. Rspr.)
- Aus identischem Sachverhalt können mehrere Ansprüche fließen (Anspruchskonkurrenz); aber ein Streitgegenstand.
- Klageänderung § 263 ZPO bei nachträglicher Änderung.

### 3. Sachliche und örtliche Zuständigkeit

#### Sachlich (GVG)

- Amtsgericht: bis 5.000 EUR Streitwert; Mietsachen Wohnraum; Familien- und Betreuungssachen (vor FG bzw. Familiengericht).
- Landgericht: über 5.000 EUR; ausschließlich u. a. § 71 GVG (Pressezivilsachen).

#### Örtlich (§§ 12 ff. ZPO)

- Allgemeiner Gerichtsstand am Wohnsitz / Sitz des Beklagten (§§ 12, 17).
- Besondere Gerichtsstände: § 29 (Vertragserfüllungsort), § 32 (Tatort bei Delikt), § 23 (Vermögensgerichtsstand).
- Verbrauchergerichtsstand § 29c ZPO bei Haustürgeschäften.
- Internationale Zuständigkeit: Brüssel Ia-VO (VO (EU) 1215/2012) und Rom I/II.

### 4. Klagearten

- **Leistungsklage** § 253 ZPO – Zahlung, Lieferung, Unterlassung.
- **Feststellungsklage** § 256 ZPO – Bestehen / Nichtbestehen eines Rechtsverhältnisses. **Feststellungsinteresse erforderlich.**
- **Gestaltungsklage** – z. B. Anfechtungsklage § 246 AktG.
- **Stufenklage** § 254 ZPO – Auskunft + bezifferte Leistung (häufig im Familien- und Erbrecht).

### 5. Substantiierungslast

- Vortrag muss **schlüssig** sein: jeder einzelne Tatbestandsteil mit Tatsachen unterlegt.
- Beweismittel **bei jeder streitigen** Tatsache angeben.
- Pauschalvorträge („alles übliche") sind unschlüssig.

### 6. Streitwert

[§§ 3 ff. ZPO](https://www.gesetze-im-internet.de/zpo/__3.html) und Kostengesetze:

- Hauptforderung in voller Höhe.
- Nebenforderungen / Kosten erhöhen nicht.
- Bei Feststellungsklagen: 80 % des Leistungswerts (BGH-Rspr.).

### 7. Anlagen und Beweisangebot

- Urkunden im Original / beglaubigt mit Anlage-Bezeichnung (K 1, K 2 …).
- Zeugen mit ladungsfähiger Anschrift.
- Sachverständige nur, wenn Tatsachenfragen ein Fachwissen erfordern.
- Beweis durch Augenschein oder Parteivernehmung selten primär.

## Quellen

### Statute

- [§ 253 ZPO](https://www.gesetze-im-internet.de/zpo/__253.html), [§ 256 ZPO](https://www.gesetze-im-internet.de/zpo/__256.html), [§ 263 ZPO](https://www.gesetze-im-internet.de/zpo/__263.html)
- [§ 12 ZPO](https://www.gesetze-im-internet.de/zpo/__12.html), [§ 17 ZPO](https://www.gesetze-im-internet.de/zpo/__17.html), [§ 29 ZPO](https://www.gesetze-im-internet.de/zpo/__29.html), [§ 32 ZPO](https://www.gesetze-im-internet.de/zpo/__32.html)
- [GVG](https://www.gesetze-im-internet.de/gvg/)
- [Brüssel Ia-VO](https://eur-lex.europa.eu/eli/reg/2012/1215/oj)

### Kommentare

- Foerste, in: Musielak / Voit, ZPO, 22. Aufl. 2025, § 253 Rn. 1 ff.
- Greger, in: Zöller, ZPO, 36. Aufl. 2025, § 253 Rn. 1 ff.
- Vollkommer, NJW 2024, 1 ff. (Aufsatz zur Substantiierung)

### Rechtsprechung

- BGH, Urt. v. 11.05.2017 – I ZR 60/16, NJW 2018, 235 (Streitgegenstand zweigliedrig) `[unverifiziert – prüfen]`
- BGH, Urt. v. 23.06.2005 – VII ZR 197/03, NJW 2005, 2615 (Substantiierung) `[unverifiziert – prüfen]`

## Ausgabeformat

```
KLAGESCHRIFT-ENTWURF — <Mandat> — <Datum>

An das <Gericht>
Aktenzeichen: noch nicht vergeben

In der Sache
  <Kläger>, Anschrift, gesetzliche Vertretung
  Prozessbevollmächtigte: <Kanzlei>
gegen
  <Beklagter>, Anschrift
wegen <Streitgegenstand kurz>

Streitwert: <EUR>

Antrag:
  <bestimmter Antrag — Leistung / Feststellung / Gestaltung>

Begründung:
  I.   Sachverhalt
       <substantiierter Vortrag, gegliedert nach Tatsachen-Komplex>
  II.  Rechtliche Würdigung
       1. Anspruch aus <Norm>
          a) Tatbestand
          b) Subsumtion
       (Anspruchsgrundlagen in kanonischer Reihenfolge)
  III. Zuständigkeit
       Sachlich: <…>
       Örtlich:  <…>
  IV.  Beweismittel
       Urkunden: Anlage K 1, K 2, …
       Zeugen:   <Name, ladungsfähige Anschrift>
       Sachverständiger: <Themenstellung>

Anlagen: K 1 bis K <N>

<Datum>, <Unterschrift Rechtsanwalt>
```

## Risiken / typische Fehler

- **Unbestimmter Antrag** — „Zahlung der Schadensersatzansprüche" reicht nicht; konkrete Summe.
- **Mehrere Streitgegenstände vermengt** — saubere Trennung notwendig (Hilfsanträge).
- **Anspruchsgrundlagen-Reihenfolge ignoriert** — Vertrag vor Delikt etc.
- **Pauschalvortrag** — jede Tatsache muss konkret sein, sonst unschlüssig.
- **Beweisangebot fehlt** — eine streitige Tatsache ohne Beweisantritt ist nicht bewiesen.
- **Falsches Gericht** — örtliche Zuständigkeit verbindlich prüfen.
- **Brüssel Ia / Rom I/II übersehen** bei Auslandsbezug.
- **Stufenklage statt Leistungsklage** wenn die Stufenklage besser passt (Auskunft + bezifferte Klage).
