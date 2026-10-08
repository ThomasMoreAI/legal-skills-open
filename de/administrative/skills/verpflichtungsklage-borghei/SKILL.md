---
name: verpflichtungsklage-borghei
title: /verwaltungsrecht:verpflichtungsklage
description: Verpflichtungsklage auf Erlass eines abgelehnten oder unterlassenen Verwaltungsakts. Klagebefugnis § 42 VwGO, Vorverfahren § 68 VwGO, Klagefrist § 74 VwGO, Verpflichtungs- und Bescheidungsurteil § 113 VwGO. Use when ein Mandant einen Anspruch auf Erlass eines Verwaltungsakts durchsetzen will.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/verwaltungsrecht/skills/verpflichtungsklage
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: administrative
language: de
---

# /verwaltungsrecht:verpflichtungsklage

## Zweck

Die Verpflichtungsklage richtet sich auf den Erlass eines beantragten, aber abgelehnten oder unterlassenen Verwaltungsakts. Sie ist die Klageart des Bürgers, der eine Begünstigung (Genehmigung, Erlaubnis, Leistung) begehrt. Die Skill trennt Versagungsgegenklage (Ablehnung liegt vor) und Untätigkeitsklage (Behörde schweigt) und ermittelt, ob das Gericht durchverpflichten kann oder nur zur Neubescheidung verpflichtet.

## Eingaben

- Begehrter Verwaltungsakt (Art der Begünstigung)
- Antrag bei der Behörde (Datum, Inhalt)
- Behördenreaktion (Ablehnungsbescheid mit Datum / keine Reaktion)
- Widerspruchsverfahren (durchgeführt? Widerspruchsbescheid?)
- Anspruchsgrundlage (gebundene Entscheidung oder Ermessen?)
- Sachverhalt vollständig ermittelt (Spruchreife?)

## Sub-Agent-Architektur

Drei gedankliche Rollen arbeiten nacheinander. Ein Zulässigkeits-Prüfer klärt Statthaftigkeit (Versagungsgegen- vs. Untätigkeitsklage), Klagebefugnis, Vorverfahren und Frist. Ein Begründetheits-Prüfer untersucht die Anspruchsgrundlage, ihren Tatbestand und die Rechtsfolge und entscheidet, ob Spruchreife besteht oder nur ein Bescheidungsurteil ergeht. Ein Verifizierer kontrolliert jede Norm gegen gesetze-im-internet.de und jede Entscheidung gegen das reale Aktenzeichen; Unbestätigtes wird mit `[unverifiziert - prüfen]` markiert oder weggelassen. Kein erfundenes Aktenzeichen.

## Ablauf

### 1. Statthaftigkeit ([§ 42 VwGO](https://www.gesetze-im-internet.de/vwgo/__42.html))

Die Verpflichtungsklage (§ 42 Abs. 1 Alt. 2 VwGO) ist statthaft, wenn der Erlass eines abgelehnten oder unterlassenen VA begehrt wird. Zwei Formen: **Versagungsgegenklage** (gegen einen Ablehnungsbescheid) und **Untätigkeitsklage** (§ 75 VwGO, Behörde entscheidet ohne zureichenden Grund nicht in angemessener Frist, i.d.R. drei Monate).

### 2. Klagebefugnis ([§ 42 VwGO](https://www.gesetze-im-internet.de/vwgo/__42.html))

§ 42 Abs. 2 VwGO: Der Kläger muss geltend machen, durch die Ablehnung oder Unterlassung in eigenen Rechten verletzt zu sein, also einen möglichen Anspruch auf den VA haben.

### 3. Vorverfahren ([§ 68 VwGO](https://www.gesetze-im-internet.de/vwgo/__68.html))

Auch die Verpflichtungsklage setzt nach § 68 Abs. 2 VwGO grundsätzlich ein erfolglos durchgeführtes Vorverfahren voraus. Ausnahmen wie bei der Anfechtungsklage. Bei der Untätigkeitsklage entfällt das Erfordernis nach § 75 VwGO.

### 4. Klagefrist ([§ 74 VwGO](https://www.gesetze-im-internet.de/vwgo/__74.html))

Für die Versagungsgegenklage gilt nach § 74 Abs. 2 VwGO die Monatsfrist des Abs. 1 ab Zustellung des Widerspruchsbescheids. Fehlerhafte Rechtsbehelfsbelehrung: Jahresfrist § 58 Abs. 2 VwGO. Die Untätigkeitsklage (§ 75 VwGO) ist nicht fristgebunden, aber frühestens nach drei Monaten zulässig.

### 5. Begründetheit ([§ 113 VwGO](https://www.gesetze-im-internet.de/vwgo/__113.html))

Maßstab § 113 Abs. 5 VwGO. Die Klage ist begründet, soweit die Ablehnung oder Unterlassung rechtswidrig und der Kläger dadurch in seinen Rechten verletzt ist, d.h. einen Anspruch auf den VA hat.

- **Anspruchsgrundlage** ermitteln
- **Tatbestandsvoraussetzungen** erfüllt?
- **Rechtsfolge**: gebundene Entscheidung oder Ermessen / Beurteilungsspielraum?

### 6. Spruchreife vs. Bescheidungsurteil ([§ 113 VwGO](https://www.gesetze-im-internet.de/vwgo/__113.html))

- **Spruchreife** (§ 113 Abs. 5 S. 1 VwGO): Bei gebundener Entscheidung und vollständig ermitteltem Sachverhalt verpflichtet das Gericht die Behörde zum Erlass des VA (Verpflichtungsurteil).
- **Bescheidungsurteil** (§ 113 Abs. 5 S. 2 VwGO): Bei Ermessen, Beurteilungsspielraum oder fehlender Spruchreife verpflichtet das Gericht nur, den Kläger unter Beachtung der Rechtsauffassung des Gerichts neu zu bescheiden.

### 7. Maßgeblicher Zeitpunkt

Bei der Verpflichtungsklage ist regelmäßig die Sach- und Rechtslage im Zeitpunkt der letzten mündlichen Verhandlung maßgeblich.

## Risiken

- **Untätigkeitsklage zu früh** — vor Ablauf der Sperrfrist des § 75 VwGO (i.d.R. drei Monate) unzulässig.
- **Falsche Klageart** — bloße Anfechtung des Ablehnungsbescheids verschafft den begehrten VA nicht; nötig ist die Verpflichtungsklage.
- **Spruchreife falsch eingeschätzt** — bei Ermessen kann nur Bescheidung verlangt werden (§ 113 Abs. 5 S. 2 VwGO), nicht Durchverpflichtung.
- **Klagefrist der Versagungsgegenklage verpasst** — Bestandskraft der Ablehnung (§ 74 VwGO).
- **Klagebefugnis fehlt** — ohne möglichen Anspruch keine Verpflichtungsklage (§ 42 Abs. 2 VwGO).
- **Aktenzeichen erfunden** — jede Entscheidung verifizieren oder als `[unverifiziert - prüfen]` kennzeichnen.

## Ausgabeformat

```
VERPFLICHTUNGSKLAGE — <Mandat> — <Datum>

I.   Begehren
     Begehrter VA:            <Genehmigung / Leistung / …>
     Behördenreaktion:        [Ablehnung am <Datum> / keine Reaktion]
     Form:                    [Versagungsgegenklage / Untätigkeitsklage § 75]

II.  Zulässigkeit
     Statthaftigkeit (§ 42):  [✓ Verpflichtungsklage]
     Klagebefugnis:           [✓ / fraglich]
     Vorverfahren (§ 68):     [durchgeführt / entbehrlich]
     Klagefrist (§ 74):       [läuft bis <Datum> / N/A bei § 75]

III. Begründetheit (§ 113 Abs. 5)
     Anspruchsgrundlage:      <…>
     Tatbestand erfüllt:      [ja / nein]
     Rechtsfolge:             [gebunden / Ermessen]
     Spruchreife:             [ja → Verpflichtung / nein → Bescheidung]

Ergebnis: <Erfolgsaussicht>
Empfehlung: <…>
```
