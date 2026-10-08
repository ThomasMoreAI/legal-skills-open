---
name: selbststaendiges-beweisverfahren-borghei
title: /prozessrecht:selbststaendiges-beweisverfahren
description: Selbständiges Beweisverfahren zur Beweissicherung vor oder außerhalb des Prozesses nach §§ 485 ff. ZPO. Zulässigkeit (§ 485 ZPO), Inhalt des Antrags (§ 487 ZPO), gerichtliches Verfahren (§ 490 ZPO), Verwertung im Hauptprozess (§ 493 ZPO). Häufig in Bausachen zur Sicherung von Mängelfeststellungen. Use when Beweise (Zeuge, Augenschein, Sachverständigengutachten) vor Verlust oder vor Klageerhebung gesichert werden sollen.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/prozessrecht/skills/selbststaendiges-beweisverfahren
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: litigation
language: de
---

# /prozessrecht:selbststaendiges-beweisverfahren

## Zweck

Das selbständige Beweisverfahren sichert Beweise, bevor sie verloren gehen, oder klärt vor einem Prozess Tatsachen (etwa Bauschäden), um einen Rechtsstreit zu vermeiden oder vorzubereiten. Der Skill prüft Zulässigkeit, Antragsinhalt und die spätere Verwertbarkeit des Ergebnisses im Hauptprozess. Fehler beim Antrag — etwa eine unzureichende Bezeichnung der Tatsachen oder des Gegners — machen das gesicherte Gutachten im späteren Prozess wertlos.

## Eingaben

- Streitgegenstand und Zweck der Beweissicherung (Mangel, Schadensbild, Zustand)
- Beweismittel: Augenschein, Zeugenvernehmung, Sachverständigengutachten
- Gegner (Bezeichnung, Anschrift) oder Begründung, warum noch unbekannt (§ 494 ZPO)
- Anhängigkeit eines Hauptprozesses (ja/nein) — entscheidet über die Zuständigkeit
- Sicherungsgrund: Verlustgefahr oder rechtliches Interesse
- Konkrete Beweisfragen / Begutachtungsthemen

## Sub-Agent-Architektur

Der Skill gliedert die Prüfung in drei Einheiten. Eine **Zulässigkeits-Einheit** prüft, ob ein Zulässigkeitsgrund nach § 485 ZPO vorliegt (Einverständnis des Gegners, Verlustgefahr oder rechtliches Interesse an der schriftlichen Begutachtung). Eine **Antrags-Einheit** formuliert den Antrag mit den Pflichtangaben des § 487 ZPO — Gegner, zu beweisende Tatsachen, Beweismittel und Glaubhaftmachung — und achtet auf die Bestimmtheit der Beweisfragen. Eine **Verwertungs-Einheit** stellt sicher, dass das Ergebnis nach § 493 ZPO im Hauptprozess wie eine dortige Beweisaufnahme genutzt werden kann (Parteiidentität, Tatsachenidentität). Die Einheiten arbeiten nacheinander und übergeben ihre Ergebnisse an das Ausgabeformat.

## Ablauf

### 1. Zulässigkeit ([§ 485 ZPO](https://www.gesetze-im-internet.de/zpo/__485.html))

- Während oder außerhalb eines Streitverfahrens auf Antrag, wenn der **Gegner zustimmt** oder zu besorgen ist, dass das **Beweismittel verloren** geht oder seine Benutzung erschwert wird (§ 485 Abs. 1 ZPO).
- Ohne anhängigen Rechtsstreit kann die schriftliche **Begutachtung durch einen Sachverständigen** verlangt werden, wenn ein **rechtliches Interesse** besteht (§ 485 Abs. 2 ZPO) — Zustand einer Sache, Ursache eines Schadens/Mangels, Aufwand der Beseitigung.

### 2. Inhalt des Antrags ([§ 487 ZPO](https://www.gesetze-im-internet.de/zpo/__487.html))

Der Antrag muss enthalten (§ 487 ZPO):

1. Bezeichnung des **Gegners**,
2. Bezeichnung der **zu beweisenden Tatsachen**,
3. Benennung der **Zeugen** oder Bezeichnung der anderen Beweismittel,
4. **Glaubhaftmachung** der die Zulässigkeit und Zuständigkeit begründenden Tatsachen.

### 3. Zuständigkeit (§ 486 ZPO)

- Bei anhängigem Rechtsstreit: das **Prozessgericht**.
- Sonst: das Gericht, bei dem die Hauptsache anhängig zu machen wäre, oder bei Dringlichkeit das Amtsgericht am Ort der Beweisaufnahme.

### 4. Verfahren ([§ 490 ZPO](https://www.gesetze-im-internet.de/zpo/__490.html))

- Das Gericht entscheidet über den Antrag durch **Beschluss** (§ 490 Abs. 1 ZPO).
- Der **Beweisbeschluss** bezeichnet die zu vernehmenden Zeugen, den Sachverständigen und die Tatsachen (§ 490 Abs. 2 ZPO).

### 5. Verwertung im Hauptprozess ([§ 493 ZPO](https://www.gesetze-im-internet.de/zpo/__493.html))

- Beruft sich eine Partei im Hauptprozess auf die selbständig erhobenen Beweise, stehen sie einer **Beweisaufnahme vor dem Prozessgericht gleich** (§ 493 Abs. 1 ZPO).
- Voraussetzung: **Parteiidentität** und **Identität der Beweisfrage**.
- Frist zur Klageerhebung auf Antrag (§ 494a ZPO); sonst Kostenlast.

## Risiken

- **Tatsachen unzureichend bezeichnet** — pauschale Beweisfragen nach § 487 ZPO machen das Gutachten im Hauptprozess wertlos.
- **Falscher Gegner** — fehlende Parteiidentität schließt die Verwertung nach § 493 ZPO aus.
- **Zulässigkeitsgrund fehlt** — ohne Verlustgefahr oder rechtliches Interesse (§ 485 ZPO) ist der Antrag unzulässig.
- **Fristsetzung zur Klageerhebung übersehen** — der Gegner kann nach § 494a ZPO eine Frist erzwingen; sonst Kostenrisiko.

## Ausgabeformat

```
SELBSTÄNDIGES BEWEISVERFAHREN — <Mandat> — <Datum>

An das <Gericht>

Antragsteller: <Name, Anschrift>
Antragsgegner: <Name, Anschrift>

I.   Zulässigkeit (§ 485 ZPO)
     Grund: [ ] Einverständnis  [ ] Verlustgefahr  [ ] rechtliches Interesse
     <Begründung>

II.  Antrag (§ 487 ZPO)
     1. Gegner: <…>
     2. Zu beweisende Tatsachen: <Mängel / Zustand / Ursache>
     3. Beweismittel: [ ] Augenschein  [ ] Zeuge  [ ] Sachverständigengutachten
     4. Glaubhaftmachung: <Anlagen>

III. Beweisfragen
     1. <…>
     2. <…>

IV.  Verwertung im Hauptprozess (§ 493 ZPO)
     Parteiidentität: <…>   Identität der Beweisfrage: <…>

Hinweis: Fristsetzung zur Klageerhebung möglich (§ 494a ZPO).
<Datum>, <Unterschrift Rechtsanwalt>
```

## Quellen

### Statute

- [§ 485 ZPO](https://www.gesetze-im-internet.de/zpo/__485.html), [§ 487 ZPO](https://www.gesetze-im-internet.de/zpo/__487.html), [§ 490 ZPO](https://www.gesetze-im-internet.de/zpo/__490.html), [§ 493 ZPO](https://www.gesetze-im-internet.de/zpo/__493.html)
- [§ 486 ZPO](https://www.gesetze-im-internet.de/zpo/__486.html), [§ 494a ZPO](https://www.gesetze-im-internet.de/zpo/__494a.html)

### Kommentare

- Herget, in: Zöller, ZPO, 36. Aufl. 2025, § 485 Rn. 1 ff.
- Werner / Pastor, Der Bauprozess, 18. Aufl. 2024, Rn. 70 ff. (selbständiges Beweisverfahren in Bausachen)

### Rechtsprechung

- BGH, Beschl. v. 16.09.2004 – III ZB 33/04 (Verwertung, § 493 ZPO) `[unverifiziert – prüfen]`
