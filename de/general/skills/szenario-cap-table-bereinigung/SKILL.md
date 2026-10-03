---
name: szenario-cap-table-bereinigung
title: Szenario Cap Table Bereinigung
description: 'Für Szenario Cap Table Bereinigung: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/status-navigator-step-plan/skills/szenario-cap-table-bereinigung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: general
language: de
---

# Szenario Cap Table Bereinigung

## Rolle und Fokus
Bereinigung mehrerer widerspruechlicher Cap Tables. Status-Navigator vergleicht Cap Tables miteinander und mit den zugrundeliegenden Vertraegen.

## Anwendungsbeispiel
LausitzStorage Cap-Table-Bereinigung: drei Versionen (siehe `diskrepanzen-aufdecken`) zeigen die NordCap-Schwankung 48/51/48 %. Prüfung ergibt: keine Wandlung dokumentiert; v2 stammt aus NordCap-Datenraum und enthielt einen Tippfehler bei Konsortium Stadtwerke-Cottbus-Anteil; v3 ist die fehlerbereinigte Investor-Update-Version. Empfehlung Soll-Cap-Table = v3 mit Vermerk.

## Output-Module
- Soll-Cap-Table mit Quellnachweis je Zeile
- Abweichungs-Memo zu den abweichenden Versionen
- Querverweis an Skill `dokumententyp-beschluesse` bei vermuteter Wandlung
