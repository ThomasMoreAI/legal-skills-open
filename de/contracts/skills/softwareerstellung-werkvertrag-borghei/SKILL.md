---
name: softwareerstellung-werkvertrag-borghei
title: /it-recht:softwareerstellung-werkvertrag
description: 'Prüfung von Verträgen über die Erstellung von Individualsoftware als Werkvertrag (§ 631 BGB): Beschaffenheit (§ 633 BGB), Abnahme (§ 640 BGB), Mängelrechte (§ 634 BGB), Lasten-/Pflichtenheft und agile Entwicklung (Scrum). Use when ein Vertrag über die Programmierung individueller Software gestaltet oder gestritten wird.'
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/it-recht/skills/softwareerstellung-werkvertrag
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: contracts
language: de
---

# /it-recht:softwareerstellung-werkvertrag

## Zweck

Die Erstellung von Individualsoftware ist regelmäßig Werkvertrag: Geschuldet ist ein Erfolg — die funktionsfähige, vereinbarte Software —, nicht bloßes Tätigwerden. Dieser Skill bestimmt das Pflichtenprogramm, prüft Abnahme und Mängelrechte und ordnet agile Vorgehensmodelle (Scrum) rechtlich ein. Ziel ist es, Vergütungs-, Abnahme- und Gewährleistungsrisiken früh sichtbar zu machen.

## Eingaben

- Vertragsrolle (Auftraggeber / Auftragnehmer)
- Vorgehensmodell (klassisch nach Pflichtenheft / agil nach Scrum)
- Lasten- und Pflichtenheft oder Product Backlog
- Abnahme- und Vergütungsregelung (Festpreis / Time & Material / Sprints)
- Streitstand (Verzug, Mängel, Abnahmeverweigerung, Kündigung)

## Sub-Agent-Architektur

Die Bearbeitung folgt drei nacheinander tätigen Rollen. Ein **Leistungssoll-Agent** rekonstruiert aus Lastenheft, Pflichtenheft und Backlog die geschuldete Beschaffenheit nach § 633 BGB — der wichtigste Schritt, weil ohne klares Soll kein Mangel feststellbar ist. Ein **Abnahme-Agent** prüft, ob, wann und in welcher Form abgenommen wurde, da die Abnahme nach § 640 BGB Verjährung, Beweislast und Vergütungsfälligkeit auslöst. Ein **Gewährleistungs-Agent** ordnet schließlich die Mängelrechte des § 634 BGB zu und bewertet die Erfolgsaussichten. Bei agilen Projekten ergänzt ein Querschnittsblick, wie sich iterative Anforderungsänderungen auf das Leistungssoll auswirken. Übergeben werden nur strukturierte Befunde; Grundlage bleibt die Vertragsdokumentation.

## Ablauf

### 1. Vertragstyp und Leistungssoll

Individualsoftware-Erstellung ist Werkvertrag nach § 631 BGB. Die geschuldete Beschaffenheit ergibt sich nach § 633 BGB vorrangig aus der Vereinbarung. Maßgebliches Dokument ist das **Pflichtenheft** (Umsetzungssicht des Auftragnehmers) auf Grundlage des **Lastenhefts** (Anforderungssicht des Auftraggebers). Fehlt eine Beschaffenheitsvereinbarung, gilt die Eignung zur gewöhnlichen bzw. vertraglich vorausgesetzten Verwendung.

### 2. Agile Entwicklung (Scrum)

Auch **agile Entwicklung** nach **Scrum** bleibt im Kern werkvertraglich, wenn ein funktionsfähiges Ergebnis geschuldet ist; das Leistungssoll wird hier iterativ über Product Backlog und Sprint-Abnahmen konkretisiert. Wird hingegen nur die Bereitstellung von Entwicklerkapazität (Time & Material) geschuldet, kann ein Dienstvertrag vorliegen. Zu regeln sind Definition of Done, Umgang mit Change Requests und Teilabnahmen je Sprint/Inkrement.

### 3. Abnahme (§ 640 BGB)

Die **Abnahme** nach § 640 BGB ist die körperliche Entgegennahme verbunden mit der Billigung als im Wesentlichen vertragsgemäß. Sie bewirkt: Fälligkeit der Vergütung, Übergang der Beweislast für Mängel auf den Auftraggeber, Beginn der Verjährung und Verlust von Rechten wegen bekannter, nicht vorbehaltener Mängel. Eine fiktive Abnahme nach § 640 Abs. 2 BGB kann eintreten, wenn der Auftraggeber das Werk trotz Aufforderung nicht binnen angemessener Frist abnimmt, ohne einen Mangel zu benennen.

### 4. Mängelrechte (§ 634 BGB)

Bei Mängeln stehen dem Auftraggeber die Rechte aus § 634 BGB zu: Nacherfüllung (§ 635 BGB), Selbstvornahme, Rücktritt oder Minderung sowie Schadensersatz. Vorrangig ist regelmäßig die Nacherfüllung mit Fristsetzung. Eine formularmäßige Verkürzung der Mängelrechte ist an §§ 307 ff. BGB zu messen.

## Risiken

- **Abnahme** ungeregelt oder konkludent erfolgt — Auftraggeber verliert unbemerkt Rechte und trägt fortan die Mängel-Beweislast (§ 640 BGB).
- **Pflichtenheft** fehlt oder ist unvollständig — ohne klares Leistungssoll nach § 633 BGB lässt sich kein Mangel begründen; Streit über „geschuldet oder Change Request".
- **agile** Projekte ohne Definition of Done und Change-Request-Prozess — schleichende Ausweitung des Solls, Festpreis wird unkalkulierbar.
- **Scrum** als Vorwand für unklare Vergütung — Abgrenzung Werk-/Dienstvertrag offen, Erfolgshaftung streitig.
- Festpreis ohne Mehrvergütungsregelung bei nachträglichen Anforderungen — Auftragnehmer trägt das Mengenrisiko.

## Ausgabeformat

```
SOFTWAREERSTELLUNG — WERKVERTRAGSPRÜFUNG — <Projekt> — <Datum>

I.   Vertragstyp                       [Werkvertrag § 631 BGB / Dienstvertrag]
     Vorgehensmodell:                  [klassisch / agil — Scrum]
II.  Leistungssoll (§ 633 BGB)         [Lastenheft + Pflichtenheft vorhanden? ✓/❌]
III. Abnahme (§ 640 BGB)               [erfolgt / verweigert / fiktiv]
     Folgen (Vergütung, Beweislast):   <…>
IV.  Mängelrechte (§ 634 BGB)          [Nacherfüllung / Rücktritt / Minderung / SE]
     Fristsetzung erfolgt:             [✓ / ❌]
V.   Vergütung / Change Requests       [Festpreis / T&M — Mehrvergütung geregelt?]

Empfehlung:                            <…>
```

## Quellen

- [§ 631 BGB](https://www.gesetze-im-internet.de/bgb/__631.html), [§ 633 BGB](https://www.gesetze-im-internet.de/bgb/__633.html)
- [§ 634 BGB](https://www.gesetze-im-internet.de/bgb/__634.html), [§ 635 BGB](https://www.gesetze-im-internet.de/bgb/__635.html), [§ 640 BGB](https://www.gesetze-im-internet.de/bgb/__640.html)
- [§§ 307 ff. BGB](https://www.gesetze-im-internet.de/bgb/__307.html) (AGB-Kontrolle von Gewährleistungsklauseln)
