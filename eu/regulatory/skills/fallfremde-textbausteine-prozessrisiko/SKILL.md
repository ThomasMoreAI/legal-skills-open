---
name: fallfremde-textbausteine-prozessrisiko
title: Fallfremde Textbausteine
description: 'Für Fallfremde Textbausteine: erstellt Entwurf mit Antrag, Beweis und Anlagen; Ergebnis: Schriftsatz mit Begründungs- und Anlagenlogik.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/ki-vo-ai-act-pruefer/skills/fallfremde-textbausteine-prozessrisiko
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: regulatory
language: de
---

# Fallfremde Textbausteine

## Warum dieser Skill wichtig ist

KI-gestützte Textarbeit produziert manchmal flüssige, aber fremde Inhalte: anderer Fall, falsche Behörde, unpassender Tatvorwurf, erfundene Anlage, falscher Streitgegenstand. Im Prozess kann das die Glaubwürdigkeit zerstören und berufsrechtliche Folgefragen auslösen.

## Norm- und Prozessanker

- ZPO § 138 für Wahrheitspflicht und Erklärungslast im Zivilprozess; ZPO §§ 130, 130a für formale Schriftsatzanforderungen.
- StPO/OWiG und VwGO/SGG/FGO jeweils gesondert prüfen: falsche Tatsachen können je nach Verfahren andere Folgen haben.
- BRAO § 43a, BORA und Mandatsvertrag für anwaltliche Sorgfalt, Verschwiegenheit und Verantwortung.
- StGB §§ 153 ff., 164, 263 nur als Warnanker bei bewusst falschen Angaben, falscher Verdächtigung oder Täuschung.
- Datenschutz/Geheimnisschutz prüfen, wenn fremde Mandatsdaten in den Textbaustein geraten sind.

## Suchmuster

Prüfe gezielt:

- Namen, Firmen, Orte, Gerichte, Behörden.
- Aktenzeichen und Geschäftsnummern.
- Datumslogik und Fristen.
- Anlagenbezeichnungen und Anlagenreihenfolge.
- Beträge, Kontonummern, Vertragsdaten, Bescheidnummern.
- Rechtsgebietssprünge: Strafrecht im Zivilprozess, Mietrecht im Datenschutzfall, falsche Verfahrensordnung.

## Ampel

- **Grün:** Aktenbezug eindeutig.
- **Gelb:** plausibel, aber nicht belegt.
- **Rot:** fremd, erfunden, widersprüchlich oder gefährlich.
