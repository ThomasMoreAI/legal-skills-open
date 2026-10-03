---
name: frist-eilversand-schiedsverfahren-anlagenband
title: Frist, Eilversand und Anlagenband im Schiedsverfahren
description: 'Für Frist, Eilversand und Anlagenband im Schiedsverfahren: prüft Frist, Form, Zuständigkeit und Eilbedarf; Ergebnis: Fristen- und Risikoampel.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/anlagen-zu-schriftsaetzen/skills/frist-eilversand-schiedsverfahren-anlagenband
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: litigation
language: de
---

# Frist, Eilversand und Anlagenband im Schiedsverfahren

## Arbeitsauftrag

Bereite einen Anlagenversand unter Zeitdruck so vor, dass Gericht, Schiedsgericht, Gegner und Mandant dieselbe belastbare Anlagenlogik erhalten. Der Skill ist für Eilfälle gedacht: Frist läuft, Anlagenband ist groß, Nummerierung muss sitzen.

## Normen- und Regelanker

- ZPO §§ 130a, 130d, 131, 253, 296: elektronische Einreichung, Anlagenbezug, Klageinhalt, Verspätung.
- ZPO §§ 1025 ff. bei Schiedsverfahren; konkrete DIS-/ICC-/LCIA-/ad-hoc-Regeln zusätzlich prüfen.
- BGB §§ 187-193 für Fristberechnung; Zustellungs- und Empfangsnachweise aktenfest dokumentieren.
- ERVV/ERVB und beA-Vorgaben: Dateiformat, Signatur, Größenbeschränkung, Containerverbot beachten.
- Berufsrechtlich BRAO § 43a/BORA § 2 bei vertraulichen Anlagen und Schwärzungen.

## Ausgabe

Erzeuge Versandcheckliste, Anlagenindex, Dateinamenkonvention, Schwärzungsvermerk, Versandweg, Nachweis der Übermittlung und Notfallplan bei Upload-/Größenfehlern.
