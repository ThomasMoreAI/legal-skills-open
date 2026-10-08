---
name: beschuldigtenvernehmung-borghei
title: /strafrecht:beschuldigtenvernehmung
description: Prüfung der Beschuldigtenvernehmung – Belehrung über Schweigerecht und Verteidigerkonsultation § 136 StPO, verbotene Vernehmungsmethoden und Verwertungsverbot § 136a StPO, polizeiliche Vernehmung im Ermittlungsverfahren § 163a StPO. Use when ein Belehrungsfehler oder eine verbotene Vernehmungsmethode auf ein Beweisverwertungsverbot zu prüfen ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/strafrecht/skills/beschuldigtenvernehmung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: criminal
language: de
---

# /strafrecht:beschuldigtenvernehmung

## Zweck

Die Aussage des Beschuldigten ist nur verwertbar, wenn die Vernehmung **ordnungsgemäß** war. Dieser Skill prüft die **Belehrung** nach [§ 136 StPO](https://www.gesetze-im-internet.de/stpo/__136.html) (Schweigerecht, Verteidigerkonsultation), das Verbot bestimmter Methoden nach [§ 136a StPO](https://www.gesetze-im-internet.de/stpo/__136a.html) und die Übertragung dieser Garantien auf die polizeiliche Vernehmung ([§ 163a StPO](https://www.gesetze-im-internet.de/stpo/__163a.html)). Im Mittelpunkt steht die Frage, ob ein **Belehrungsfehler** oder eine verbotene Methode zu einem **Beweisverwertungsverbot** führt.

## Eingaben

- Wer hat vernommen (Polizei / StA / Richter)?
- Wurde belehrt? Wortlaut/Protokoll vorhanden?
- Wurde auf das **Schweigerecht** und die **Verteidigerkonsultation** hingewiesen?
- Hat der Beschuldigte einen Verteidiger verlangt? Reaktion?
- Anhaltspunkte für Täuschung, Drohung, Zwang, Ermüdung?
- Wurde der Aussage in der Hauptverhandlung widersprochen?

## Sub-Agent-Architektur

Der **Researcher** ordnet den Ablauf den Vorgaben der §§ 136, 136a, 163a StPO zu und verifiziert jede Norm gegen gesetze-im-internet.de; konkrete BGH-Aktenzeichen werden nicht erfunden, sondern generisch beschrieben oder mit `[unverifiziert – prüfen]` markiert. Der **Drafter** formuliert die Widerspruchsbegründung bzw. den Verwertungswiderspruch und arbeitet Belehrungsfehler und Methodenverbot heraus. Der **Reviewer** prüft gegenläufig, ob die Belehrung vollständig war, ob ein Verwertungsverbot greift und ob rechtzeitig widersprochen wurde.

## Ablauf

### 1. Belehrung ([§ 136 Abs. 1 StPO](https://www.gesetze-im-internet.de/stpo/__136.html))

Zu Beginn der Vernehmung ist zu eröffnen, welche Tat vorgeworfen wird, und zu belehren über:

- das **Schweigerecht** — es steht dem Beschuldigten frei, sich zur Sache zu äußern oder nicht auszusagen;
- das Recht, **jederzeit, auch vor der Vernehmung, einen Verteidiger zu befragen** (Verteidigerkonsultation);
- das Recht, Beweiserhebungen zu beantragen, und auf Hinweise zur Pflichtverteidigung.

**Belehrungsfehler**: Unterbleibt die Belehrung über Schweigerecht oder Verteidigerkonsultation, ist die Aussage grundsätzlich unverwertbar (qualifizierte Belehrung bei früherem Fehler beachten).

### 2. Verbotene Vernehmungsmethoden ([§ 136a StPO](https://www.gesetze-im-internet.de/stpo/__136a.html))

Verboten sind u. a. **Misshandlung, Ermüdung, körperlicher Eingriff, Verabreichung von Mitteln, Quälerei, Täuschung, Hypnose, Zwang und Drohung** mit unzulässiger Maßnahme sowie das Versprechen gesetzlich nicht vorgesehener Vorteile.

### 3. Verwertungsverbot ([§ 136a Abs. 3 StPO](https://www.gesetze-im-internet.de/stpo/__136a.html))

Aussagen, die unter Verstoß gegen die Verbote des § 136a StPO zustande kamen, dürfen **auch mit Zustimmung des Beschuldigten nicht verwertet** werden — **unverzichtbares (absolutes) Beweisverwertungsverbot** (§ 136a Abs. 3 S. 2 StPO). Davon zu unterscheiden ist das aus Belehrungsfehlern folgende, von einem **rechtzeitigen Widerspruch** abhängige Verwertungsverbot.

### 4. Polizeiliche Vernehmung ([§ 163a StPO](https://www.gesetze-im-internet.de/stpo/__163a.html))

- § 163a StPO überträgt die Garantien (Belehrung, Methodenverbote) auf die **polizeiliche Vernehmung** im Ermittlungsverfahren (§ 163a Abs. 3, 4 StPO).
- Das Recht, sich eines Verteidigers zu bedienen, folgt ergänzend aus [§ 137 StPO](https://www.gesetze-im-internet.de/stpo/__137.html).

### 5. Widerspruch / Rechtsfolge

- Bei aus Belehrungsfehlern folgenden Verwertungsverboten: **rechtzeitiger Widerspruch** bis zu dem in § 257 StPO bezeichneten Zeitpunkt (Widerspruchslösung; gefestigte Rechtsprechung nur mit Fundstelle, sonst `[unverifiziert – prüfen]`).
- Fernwirkung gesondert prüfen (umstritten).

## Risiken

- **Belehrungsfehler** (kein Hinweis auf Schweigerecht/Verteidigerkonsultation) → Verwertungsverbot, aber nur bei Widerspruch.
- **Verbotene Vernehmungsmethoden** (Täuschung, Drohung, Ermüdung) → absolutes Verwertungsverbot nach § 136a Abs. 3 StPO.
- **Widerspruch** versäumt → Aussage trotz Belehrungsfehler verwertbar.
- Verlangen nach Verteidiger missachtet (faktische Vereitelung der Verteidigerkonsultation).

## Ausgabeformat

```
BESCHULDIGTENVERNEHMUNG — <Az.> — <Datum>
VERTRAULICH — STRAFVERTEIDIGUNG

I.    Vernehmende Stelle              <Polizei / StA / Richter>   [§ 163a StPO]
II.   Belehrung                       [§ 136 StPO]
      Schweigerecht:                  [✅ / ❌]
      Verteidigerkonsultation:        [✅ / ❌]
III.  Vernehmungsmethoden             [§ 136a StPO]
      Täuschung/Drohung/Zwang:        [keine / 🔴 vorhanden]
IV.   Verwertungsverbot
      § 136a Abs. 3 (absolut):        [nein / 🔴 ja]
      Belehrungsfehler (Widerspruch): [n. a. / rechtzeitig / versäumt]

Empfehlung: <…>
Nächster Schritt: <Verwertungswiderspruch bis § 257 StPO>
```

## Quellen

- [§ 136 StPO](https://www.gesetze-im-internet.de/stpo/__136.html), [§ 136a StPO](https://www.gesetze-im-internet.de/stpo/__136a.html), [§ 163a StPO](https://www.gesetze-im-internet.de/stpo/__163a.html), [§ 137 StPO](https://www.gesetze-im-internet.de/stpo/__137.html)
- Meyer-Goßner / Schmitt, StPO, 67. Aufl. 2024, § 136 Rn. 1 ff., § 136a Rn. 1 ff.
- BGH-Rechtsprechung zur Widerspruchslösung und qualifizierten Belehrung: `[unverifiziert – prüfen]`
