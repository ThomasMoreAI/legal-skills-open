---
name: red-team-beamtenrecht
title: Red Team Beamtenrecht
description: 'Für Red Team Beamtenrecht: prüft Ergebnis, Beweislast und Gegenposition; Ergebnis: Gegenprüfung mit Beweis- und Fristencheck.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/beamtenrecht/skills/red-team-beamtenrecht
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: administrative
language: de
---

# Red Team Beamtenrecht

## Pflichtfragen

- Welcher Status liegt vor: Beamter, Richter, Bewerber, Anwärter, Tarifbeschäftigter, Wahlbeamter oder Mischfall?
- Welcher Dienstherr und welches Bundesland sind betroffen?
- Gibt es einen Bescheid, eine Beurteilung, eine Ausschreibung, einen Auswahlvermerk oder eine Verfügung mit Datum und Zugang?
- Welche Frist läuft und welches Ergebnis soll erreicht werden?
- Welche Unterlagen fehlen noch: Personalakte, Beurteilungsbeiträge, amtsärztliches Gutachten, Berechnungsblatt, Beteiligungsvermerk?

## Prüfprogramm

1. **Status und Rechtsquelle:** Bundesrecht, Landesrecht oder Richterrecht trennen; Normen live gegen amtliche Quellen prüfen.
2. **Eingriff und Ziel:** Verwaltungsakt, dienstliche Weisung, Auswahlentscheidung, Realakt oder bloße Kommunikation einordnen.
3. **Materielle Prüfung:** Tatbestand, Ermessen, Beteiligung, Begründung, Gleichbehandlung, Fürsorge und Verhältnismäßigkeit prüfen.
4. **Verfahren:** Anhörung, Akteneinsicht, Frist, Widerspruch, Klageart, Eilrechtsschutz und Glaubhaftmachung klären.
5. **Output:** Eine klare Handlungsempfehlung, einen Entwurf oder eine Risikomatrix erzeugen.
