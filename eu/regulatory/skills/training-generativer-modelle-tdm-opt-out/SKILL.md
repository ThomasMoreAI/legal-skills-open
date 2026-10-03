---
name: training-generativer-modelle-tdm-opt-out
title: 'Training generativer Modelle: TDM und Opt-out'
description: 'Für Training generativer Modelle: TDM und Opt-out: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/ki-vo-ai-act-pruefer/skills/training-generativer-modelle-tdm-opt-out
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: regulatory
language: de
---

# Training generativer Modelle: TDM und Opt-out

## Prüfansatz

Ordne jede Trainingsquelle nach Rechtepfad: eigene Daten, lizenzierte Daten, Webdatenabruf, Kundenupload, Open-Data, wissenschaftlicher Datensatz, Datenbank. Danach wird geprüft, ob TDM erlaubt ist, ob ein Opt-out greift und ob Output-Reproduktion droht.

## Normenanker

- UrhG § 44b: Text und Data Mining allgemein; Rechtevorbehalt muss maschinenlesbar sein, soweit online verfügbar.
- UrhG § 60d: TDM für wissenschaftliche Forschung.
- UrhG §§ 87a ff.: Datenbankherstellerrecht.
- VO (EU) 2024/1689 Art. 53: Pflichten für Anbieter von GPAI-Modellen, insbesondere Urheberrechtsstrategie und Trainingszusammenfassung.
- DSGVO Art. 5, 6, 9, 14, 17, 21 bei personenbezogenen Trainingsdaten.

## Arbeitsprodukt

Erzeuge eine Quellenmatrix mit URL/Datensatz, Lizenz, Opt-out-Signal, Abrufwerkzeuge-Entscheidung, Sperrprotokoll, Datenbankrisiko, personenbezogenem Risiko und Output-Filter. Kein „fair use“-Argument als deutsches/europäisches Recht ausgeben.
