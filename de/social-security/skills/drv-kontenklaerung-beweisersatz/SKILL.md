---
name: drv-kontenklaerung-beweisersatz
title: DRV Kontenklärung Beweisersatz
description: 'Für DRV Kontenklärung Beweisersatz: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Beweislast- und Substantiierungsmatrix.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/rentenpruefer/skills/drv-kontenklaerung-beweisersatz
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: social-security
language: de
---

# DRV Kontenklärung Beweisersatz

## Direktstart

Liefere eine Beweislandkarte. Ziel ist nicht, „Unterlagen fehlen“ festzustellen, sondern den besten Ersatzbeleg zu finden.

## Beweislandkarte

| fehlende Zeit | Primärbeleg | Ersatzbeleg | Risiko |
| --- | --- | --- | --- |
| Beschäftigung | Arbeitgebermeldung | Entgeltabrechnung, Krankenkasse, Steuer | mittel |
| Ausbildung | Schulbescheinigung | Archiv, Zeugnis, Immatrikulation | niedrig bis mittel |
| Pflege | Pflegekasse | Pflegebescheid, Angehörigenerklärung | mittel |
| Ausland | Trägerbescheinigung | Arbeitsbuch, Übersetzung, Konsulat | hoch |

## Normanker

- SGB VI Paragraf 149: Kontenklärung.
- SGB X Paragraf 20 und 21: Amtsermittlung und Beweismittel.
- SGG Paragraf 103: Sachaufklärung im Gerichtsverfahren.

## Output

Formuliere ein Anschreiben an die DRV mit Zeitraum, Sachverhalt, vorhandenen Anlagen und Antrag auf Benennung weiterer Nachweise. Danach folgt eine Prioritätenliste für den Mandanten.
