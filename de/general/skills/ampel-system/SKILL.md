---
name: ampel-system
title: Ampelsystem für Status
description: 'Für Ampelsystem für Status: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/status-navigator-step-plan/skills/ampel-system
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: general
language: de
---

# Ampelsystem für Status

## Rolle und Fokus
Dreistufige Ampel (gruen/gelb/rot) als bedingte Formatierung in der Excel-Arbeitsmappe und als Farbtag in Padlet-Karten. Verdichtet komplexe Statuslagen auf einen Blick.

## Anwendungsbeispiel
LausitzStorage-Akte Stand 02.06.2026: 4 rote Eintraege (Drawstop NordCap, Anlage 4 Konsortialvertrag fehlt, Zugangsnachweis LEAG-Kuendigungsdrohung unklar, Avalstatus 50Hertz unbestaetigt), 7 gelbe (drei Cap-Table-Versionen mit Abweichungen, zwei Unterschriften fragwuerdig, ein Gesellschafterbeschluss inhaltlich unklar, Drawstop-Schreiben unklar zugegangen), Rest gruen.

## Output-Module
- Bedingte-Formatierung-Regeln je Reiter (Hintergrundfarbe auf Status-Spalte)
- Restzeit-Ampel im Fristen-Reiter mit Schwellen 30/8 Tage
- Ampel-Konsistenz-Prüfung zwischen Reiter 2 und 3
