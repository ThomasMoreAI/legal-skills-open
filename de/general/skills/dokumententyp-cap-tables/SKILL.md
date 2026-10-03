---
name: dokumententyp-cap-tables
title: Dokumententyp Cap Tables
description: 'Für Dokumententyp Cap Tables: ordnet Akte, Belege und Lücken; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/status-navigator-step-plan/skills/dokumententyp-cap-tables
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: general
language: de
---

# Dokumententyp Cap Tables

## Rolle und Fokus
Erkennt Cap Tables in beliebigem Format (Excel, PDF, eingebettete Tabellen). Erfasst Stichdatum, Gesellschafter, Anteile. Vorbereitung für Konsistenzvergleich mehrerer Versionen.

## Anwendungsbeispiel
LausitzStorage: drei Cap-Table-Versionen liegen vor. v1 (31.12.2025, von Mandantin), v2 (30.04.2026, von NordCap-Datenraum), v3 (Mai 2026, aus Investor-Update). Vergleich liefert die in `diskrepanzen-aufdecken` aufgenommene 48/51/48-Abweichung.

## Output-Module
- Versionsregister mit Stichdatum, Quelle, Status
- Normalisierte Cap-Table als Vorlage für den Konsistenzvergleich
- Querliste an `szenario-cap-table-bereinigung` wenn Abweichungen materiell
