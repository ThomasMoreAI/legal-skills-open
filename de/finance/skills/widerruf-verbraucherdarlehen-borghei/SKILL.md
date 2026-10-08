---
name: widerruf-verbraucherdarlehen-borghei
title: /bankrecht:widerruf-verbraucherdarlehen
description: Prüfung des Widerrufs eines Verbraucherdarlehensvertrags § 491 BGB. Pflichtangaben § 492 BGB i.V.m. Art. 247 EGBGB, Widerrufsrecht § 495 BGB i.V.m. § 355 BGB, Fristbeginn § 356b BGB, Rückabwicklung § 357b BGB; fehlerhafte Widerrufsinformation („Widerrufsjoker"). Use when ein Verbraucher den Widerruf eines Darlehensvertrags erwägt oder die Wirksamkeit einer Widerrufsbelehrung geprüft wird.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/bankrecht/skills/widerruf-verbraucherdarlehen
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: finance
language: de
---

# /bankrecht:widerruf-verbraucherdarlehen

## Zweck

Bei fehlerhaften Pflichtangaben oder fehlerhafter Widerrufsinformation beginnt die 14-tägige Widerrufsfrist nicht zu laufen — der Vertrag bleibt für den Verbraucher unter Umständen jahrelang widerruflich („Widerrufsjoker"). Dieser Skill prüft, ob ein Widerruf nach § 495 BGB noch möglich ist, welche Rechtsfolgen die Rückabwicklung nach § 357b BGB auslöst und welche Angriffspunkte die Widerrufsinformation bietet.

## Eingaben

- Vertragstyp (Allgemein-Verbraucherdarlehen, Immobiliar-Verbraucherdarlehen, verbundenes Geschäft)
- Datum des Vertragsschlusses (maßgebend für die anwendbare Fassung)
- Darlehensbetrag, Sollzinssatz, effektiver Jahreszins, Laufzeit
- Vollständige Widerrufsinformation/Widerrufsbelehrung im Vertragstext
- Vorhandensein und Wortlaut der Pflichtangaben (Art. 247 EGBGB)
- Bereits geleistete Zahlungen, ggf. Verbundgeschäft

## Sub-Agent-Architektur

Der **Researcher** verifiziert die einschlägige Fassung der §§ 491 ff. BGB zum Vertragsdatum, bestätigt jeden Paragraphen über gesetze-im-internet.de und recherchiert einschlägige BGH-/EuGH-Rechtsprechung zur Widerrufsinformation; ungesicherte Aktenzeichen werden als `[unverifiziert – prüfen]` markiert. Der **Drafter** ordnet die Vertragsklauseln den gesetzlichen Pflichtangaben zu und entwirft die Widerrufsprüfung entlang des Ablaufs. Der **Reviewer** prüft, ob der Fristbeginn nach § 356b BGB korrekt hergeleitet ist, ob Kausalität und Rechtsfolgen vollständig adressiert sind und ob keine Tatsachen erfunden wurden.

## Ablauf

### 1. Anwendungsbereich (§ 491 BGB)

[§ 491 BGB](https://www.gesetze-im-internet.de/bgb/__491.html): Verbraucherdarlehensvertrag, wenn Unternehmer (§ 14 BGB) an Verbraucher (§ 13 BGB) ein entgeltliches Darlehen über mehr als 200 EUR gewährt. Abgrenzung Allgemein- vs. Immobiliar-Verbraucherdarlehen (§ 491 Abs. 3 BGB), da Fristbegrenzung und Pflichtangaben abweichen.

### 2. Pflichtangaben (§ 492 BGB i.V.m. Art. 247 EGBGB)

[§ 492 BGB](https://www.gesetze-im-internet.de/bgb/__492.html) verlangt Schriftform und die in [Art. 247 EGBGB](https://www.gesetze-im-internet.de/bgbeg/art_247.html) aufgeführten **Pflichtangaben**. Prüfraster:

- Nettodarlehensbetrag, Sollzinssatz, effektiver Jahreszins
- Vertragslaufzeit, Anzahl/Höhe/Fälligkeit der Raten
- Verzugszinssatz und Art der Anpassung
- Hinweis auf Verzugsfolgen und außergerichtliche Beschwerdeverfahren
- Berechnungsmethode der Vorfälligkeitsentschädigung
- **Widerrufsinformation** (siehe Ziff. 3)

Fehlende oder fehlerhafte Pflichtangabe → Frist beginnt nicht (§ 356b BGB).

### 3. Widerrufsrecht (§ 495 BGB i.V.m. § 355 BGB)

[§ 495 BGB](https://www.gesetze-im-internet.de/bgb/__495.html) gewährt dem Darlehensnehmer das Widerrufsrecht nach [§ 355 BGB](https://www.gesetze-im-internet.de/bgb/__355.html):

- **Frist:** 14 Tage
- **Fristbeginn:** erst nach Erhalt aller Pflichtangaben und ordnungsgemäßer Widerrufsinformation ([§ 356b BGB](https://www.gesetze-im-internet.de/bgb/__356b.html))
- **Form:** Widerrufserklärung formfrei, keine Begründung
- **Kausalitäts-/Gesetzlichkeitsfiktion:** Verwendung des amtlichen Musters (Art. 247 § 6 Abs. 2 EGBGB) schützt den Darlehensgeber; jede Abweichung öffnet den „Widerrufsjoker".

### 4. Prüfung der Widerrufsinformation

- Klarheit und Verständlichkeit des Fristbeginns („Kaskadenverweis" — EuGH-kritisch)
- Vollständige Pflichtangaben-Auflistung als Voraussetzung des Fristlaufs
- Korrekte Angaben zu Wertersatz und Rückzahlungspflichten
- Bei Immobiliar-Verbraucherdarlehen: absolute Erlöschensgrenze (§ 356b Abs. 2 S. 4 BGB)

### 5. Rechtsfolgen (§ 357b BGB)

[§ 357b BGB](https://www.gesetze-im-internet.de/bgb/__357b.html): Rückgewährschuldverhältnis. Darlehensnehmer zahlt Nettodarlehen zurück und schuldet den vereinbarten Sollzins bis zur Rückzahlung; bei Immobiliardarlehen kann ein geringerer Gebrauchsvorteil nachgewiesen werden. Verbundene Verträge (§ 358 BGB) werden mit-rückabgewickelt.

## Risiken / typische Fehler

- **Fehlerhafte Widerrufsinformation übersehen** — der „Widerrufsjoker" verlängert die Frist faktisch unbegrenzt; ungeprüfte Übernahme des Bankformulars verschenkt die Verteidigung.
- **Pflichtangaben nur formal abgehakt** — eine einzige fehlerhafte Pflichtangabe hindert den Fristbeginn nach § 356b BGB.
- **Fristbeginn falsch berechnet** — Verwechslung von Vertragsschluss und Erhalt der Pflichtangaben.
- **Rückabwicklung unterschätzt** — Sollzinspflicht und Nutzungsersatz nach § 357b BGB können den wirtschaftlichen Vorteil aufzehren; Verbundgeschäft nach § 358 BGB nicht mitbedacht.
- **Verwirkung/Rechtsmissbrauch ignoriert** — bei lange zurückliegenden Darlehen prüft die Rechtsprechung Verwirkung; ungesicherte Aktenzeichen sind als `[unverifiziert – prüfen]` zu kennzeichnen.

## Quellen

- [§ 491 BGB](https://www.gesetze-im-internet.de/bgb/__491.html), [§ 492 BGB](https://www.gesetze-im-internet.de/bgb/__492.html), [§ 495 BGB](https://www.gesetze-im-internet.de/bgb/__495.html)
- [§ 355 BGB](https://www.gesetze-im-internet.de/bgb/__355.html), [§ 356b BGB](https://www.gesetze-im-internet.de/bgb/__356b.html), [§ 357b BGB](https://www.gesetze-im-internet.de/bgb/__357b.html)
- [Art. 247 EGBGB](https://www.gesetze-im-internet.de/bgbeg/art_247.html)
- EuGH, Urt. v. 26.03.2020 – C-66/19 (Kaskadenverweis) `[unverifiziert – prüfen]`
- BGH, Urt. v. 27.02.2018 – XI ZR 160/17 `[unverifiziert – prüfen]`

## Ausgabeformat

```
WIDERRUF VERBRAUCHERDARLEHEN — <Mandat> — <Datum>

I.    Anwendungsbereich § 491 BGB        [Allgemein / Immobiliar / Verbund]
II.   Pflichtangaben § 492 / Art. 247 EGBGB
      Vollständigkeit:                    [✓ / ⚠️ Liste fehlender Angaben]
III.  Widerrufsinformation
      Muster verwendet:                   [✓ / 🔴 abweichend → Widerrufsjoker]
      Fristbeginn § 356b BGB:             [in Lauf gesetzt / nicht begonnen]
IV.   Widerrufsrecht § 495 i.V.m. § 355 BGB
      Widerruf noch möglich:              [ja / nein / „ewig"]
V.    Rechtsfolgen § 357b BGB
      Rückzahlung / Sollzins / Nutzungen: <…>
      Verbundgeschäft § 358 BGB:          [N/A / mit-rückabwickeln]

Empfehlung: <…>
```
