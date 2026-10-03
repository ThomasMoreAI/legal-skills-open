---
name: erweiterung-hyperlinks
title: Erweiterung Hyperlinks zur Ablage
description: 'Für Erweiterung Hyperlinks zur Ablage: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/status-navigator-step-plan/skills/erweiterung-hyperlinks
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: general
language: de
---

# Erweiterung Hyperlinks zur Ablage

## Rolle und Fokus
Verknuepft Tabelleneintraege mit Originaldokumenten in der Ablage. Sprung von der Tabelle zum Volltext spart Sucherei bei jeder Folgepruefung.

## Anwendungsbeispiel
LausitzStorage-Akte: Reiter 1 verlinkt alle 19 Hauptdokumente in den Mandantsfileshare. Anlage 4 zum Konsortialvertrag bekommt Platzhalter-Link `_FEHLT_` damit beim Klick sofort sichtbar ist dass die Anlage in Reiter 3 nachverfolgt wird.

## Output-Module
- Hyperlink-Spalte je Reiter (relativer Pfad)
- Platzhalter-Link `_FEHLT_` für in Reiter 3 verfolgte Luecken
- Wartungspruefung als Eintrag in `erweiterung-laufende-aktualisierung`
