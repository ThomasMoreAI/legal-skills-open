---
name: erweiterung-sicherheiten-reiter
title: Erweiterung Sicherheiten-Reiter
description: 'Für Erweiterung Sicherheiten-Reiter: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/status-navigator-step-plan/skills/erweiterung-sicherheiten-reiter
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: general
language: de
---

# Erweiterung Sicherheiten-Reiter

## Rolle und Fokus
Optionaler Reiter Sicherheiten. Übersicht aller bestellten Sicherheiten mit Status der Bestellung und Verwertbarkeit. Keine Wirksamkeitspruefung — die bleibt anwaltlich.

## Anwendungsbeispiel
LausitzStorage Sicherheiten: Grundschuld 80 Mio EUR zu Gunsten NordCap (Eintragung beantragt 28.04.2026, Vollzugsmitteilung steht aus), Verpfaendung der Anteile (Pfandvertrag vom 14.03.2026, Zustellung an Gesellschaft 16.03.2026), Avale ILB zu Gunsten LEAG (Status ausgegeben, Avalvolumen 8 Mio EUR) und zu Gunsten 50Hertz (Status unbestaetigt — siehe Reiter 3).

## Output-Module
- Sicherheiten-Reiter mit Spalten Sicherheit, Besicherter Vertrag, Status, Datum
- Avalstatus-Subtabelle (gesondert wegen Avalbestaetigungs-Pflicht)
- Querverweise an Reiter 3 wo Sicherheit fehlt oder Status unklar
