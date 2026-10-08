---
name: vollstreckungsabwehrklage-borghei
title: /prozessrecht:vollstreckungsabwehrklage
description: Rechtsbehelfe des Schuldners und Dritter gegen die Zwangsvollstreckung nach §§ 767, 771 ZPO. Materielle Einwendungen gegen den titulierten Anspruch (§ 767 ZPO), Präklusion nach Schluss der mündlichen Verhandlung (§ 767 Abs. 2 ZPO), Drittwiderspruchsklage bei die Veräußerung hinderndem Recht (§ 771 ZPO). Use when ein Schuldner materiell-rechtliche Einwendungen gegen einen Titel erhebt oder ein Dritter sich gegen den Zugriff auf seine Sache wehrt.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/prozessrecht/skills/vollstreckungsabwehrklage
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: litigation
language: de
---

# /prozessrecht:vollstreckungsabwehrklage

## Zweck

Aus einem rechtskräftigen Titel kann vollstreckt werden, auch wenn der Anspruch inzwischen erloschen ist (Erfüllung, Aufrechnung, Erlass). Die Vollstreckungsabwehrklage räumt dem Schuldner die Möglichkeit ein, solche materiellen Einwendungen geltend zu machen; die Drittwiderspruchsklage schützt Dritte, deren Eigentum gepfändet wird. Der Skill prüft die richtige Klageart und — zentral — die Präklusion: Einwendungen, die schon im Vorprozess hätten vorgebracht werden können, sind ausgeschlossen.

## Eingaben

- Art und Inhalt des Titels (Urteil, Vollstreckungsbescheid, notarielle Urkunde)
- Zeitpunkt des Schlusses der mündlichen Verhandlung im Vorprozess
- Geltend gemachte Einwendung (Erfüllung, Aufrechnung, Stundung, Verzicht) und ihr Entstehungszeitpunkt
- Wer wehrt sich: Schuldner (§ 767) oder Dritter (§ 771)
- Bei § 771: das die Veräußerung hindernde Recht (Eigentum, Anwartschaft, Sicherungseigentum)
- Stand der Zwangsvollstreckung (Pfändung erfolgt? welche Sache?)

## Sub-Agent-Architektur

Der Skill nutzt drei gedankliche Einheiten. Eine **Klageart-Einheit** ordnet den Fall ein: Wendet sich der Schuldner gegen den titulierten Anspruch selbst, ist die Vollstreckungsabwehrklage einschlägig; macht ein Dritter ein eigenes Recht an der gepfändeten Sache geltend, die Drittwiderspruchsklage. Eine **Präklusions-Einheit** prüft bei § 767 ZPO, ob die Einwendung erst nach Schluss der mündlichen Verhandlung des Vorprozesses entstanden ist — nur dann ist sie zulässig. Eine **Rechtsfolgen-Einheit** formuliert den Klageantrag (Unzulässigerklärung der Zwangsvollstreckung aus dem Titel) und prüft den Bezug zu einstweiligem Rechtsschutz (§ 769 ZPO, Einstellung der Vollstreckung). Die Einheiten arbeiten nacheinander.

## Ablauf

### 1. Vollstreckungsabwehrklage ([§ 767 ZPO](https://www.gesetze-im-internet.de/zpo/__767.html))

- Der Schuldner macht **materielle Einwendungen** gegen den durch den Titel festgestellten Anspruch geltend (§ 767 Abs. 1 ZPO).
- Typische Einwendungen: **Erfüllung**, Aufrechnung, Erlass, Stundung, Verjährungseinrede (soweit nach Titel entstanden).
- Die Klage richtet sich nicht gegen die Richtigkeit des Titels, sondern gegen seine **Vollstreckbarkeit**.

### 2. Präklusion ([§ 767 Abs. 2 ZPO](https://www.gesetze-im-internet.de/zpo/__767.html))

- Einwendungen sind **nur zulässig**, wenn die Gründe, auf denen sie beruhen, **erst nach dem Schluss der mündlichen Verhandlung** entstanden sind, in der sie spätestens hätten geltend gemacht werden müssen (§ 767 Abs. 2 ZPO).
- Bei Vollstreckungsbescheiden und Prozessvergleichen verschiebt sich der maßgebliche Zeitpunkt; bei notariellen Urkunden gilt § 767 Abs. 2 ZPO nicht.
- Zweck: Schutz der Rechtskraft; bereits abgeurteilte Einwendungen bleiben präkludiert.

### 3. Drittwiderspruchsklage ([§ 771 ZPO](https://www.gesetze-im-internet.de/zpo/__771.html))

- Behauptet ein **Dritter** ein die Veräußerung **hinderndes Recht** am Vollstreckungsgegenstand, ist der Widerspruch im Wege der Klage geltend zu machen (§ 771 Abs. 1 ZPO).
- Hinderndes Recht: **Eigentum**, Sicherungseigentum, Anwartschaftsrecht, in der Regel nicht der bloße Besitz.
- Antrag: Unzulässigerklärung der Zwangsvollstreckung in den konkreten Gegenstand.

### 4. Einstweiliger Rechtsschutz (§ 769 ZPO)

- Das Prozessgericht kann die **einstweilige Einstellung** der Zwangsvollstreckung anordnen (§ 769 ZPO), ggf. gegen Sicherheitsleistung — sonst läuft die Vollstreckung trotz Klage weiter.

## Risiken

- **Präklusion übersehen** — eine vor Schluss der mündlichen Verhandlung entstandene Einwendung ist nach § 767 Abs. 2 ZPO ausgeschlossen.
- **Falsche Klageart** — der Dritte muss § 771 ZPO wählen, nicht die Vollstreckungsabwehrklage; der Schuldner umgekehrt.
- **Einstweilige Einstellung nicht beantragt** — ohne Antrag nach § 769 ZPO wird trotz Klage weiter vollstreckt.
- **Bloßer Besitz als hinderndes Recht** — Besitz allein genügt für § 771 ZPO regelmäßig nicht; ein dingliches Recht ist erforderlich.

## Ausgabeformat

```
VOLLSTRECKUNGSRECHTSBEHELF — <Mandat> — <Datum>

An das <Prozessgericht / Gericht der Hauptsache>

Titel: <Bezeichnung, Datum, Az.>
Schluss der mündlichen Verhandlung im Vorprozess: <Datum>

I.   Klageart
     [ ] Vollstreckungsabwehrklage (§ 767 ZPO) — Schuldner
     [ ] Drittwiderspruchsklage (§ 771 ZPO) — Dritter

II.  Einwendung / Recht
     <Erfüllung / Aufrechnung / Eigentum …>
     Entstehungszeitpunkt: <Datum>

III. Präklusionsprüfung (§ 767 Abs. 2 ZPO)
     Nach Schluss der mündlichen Verhandlung entstanden? <ja/nein>

IV.  Antrag
     Die Zwangsvollstreckung aus dem Titel <…> wird für unzulässig erklärt.
     (§ 771: in den Gegenstand <…>)

V.   Einstweilige Einstellung (§ 769 ZPO)
     <Antrag, ggf. gegen Sicherheitsleistung>

<Datum>, <Unterschrift Rechtsanwalt>
```

## Quellen

### Statute

- [§ 767 ZPO](https://www.gesetze-im-internet.de/zpo/__767.html), [§ 771 ZPO](https://www.gesetze-im-internet.de/zpo/__771.html)
- [§ 769 ZPO](https://www.gesetze-im-internet.de/zpo/__769.html), [§ 775 ZPO](https://www.gesetze-im-internet.de/zpo/__775.html)

### Kommentare

- Herget, in: Zöller, ZPO, 36. Aufl. 2025, § 767 Rn. 1 ff.
- Lackmann, in: Musielak / Voit, ZPO, 22. Aufl. 2025, § 771 Rn. 1 ff.

### Rechtsprechung

- BGH, Urt. v. 14.05.2014 – VII ZR 334/12 (Präklusion, § 767 Abs. 2 ZPO) `[unverifiziert – prüfen]`
