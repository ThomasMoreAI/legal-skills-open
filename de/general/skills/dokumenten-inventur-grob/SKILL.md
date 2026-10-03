---
name: dokumenten-inventur-grob
title: Dokumenten-Inventur grob
description: 'Für Dokumenten-Inventur grob: ordnet Akte, Belege und Lücken; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/status-navigator-step-plan/skills/dokumenten-inventur-grob
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: general
language: de
---

# Dokumenten-Inventur grob

## Rolle und Fokus
Erste Sichtung: Dateiname, Dateityp, Dateigroesse, sichtbares Datum. Noch keine inhaltliche Prüfung — Bestandsaufnahme als Ausgangspunkt für die feinere Einordnung.

## Anwendungsbeispiel
LausitzStorage-Mandat: 80 PDFs aus drei Quellen (Datenraum NordCap, Mandantenpostfach, eigene Akte). Grobinventur findet 6 Duplikate (unterschiedliche Versionen des Pachtvertrags), 3 Dateien ohne lesbare Unterschriftsseite, 1 leere Anlage 4 zum Konsortialvertrag.

## Output-Module
- Roh-Inventur als CSV/Excel-Importzeile für Reiter 1
- Duplikatsliste mit Empfehlung welche Version fuehrend ist
- Lesbarkeits-Mangelliste (Nachforderung im Datenraum)
