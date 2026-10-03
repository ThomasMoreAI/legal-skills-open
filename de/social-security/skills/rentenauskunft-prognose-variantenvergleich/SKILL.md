---
name: rentenauskunft-prognose-variantenvergleich
title: Rentenauskunft Prognose Variantenvergleich
description: 'Für Rentenauskunft Prognose Variantenvergleich: entwickelt Ziel, Vergleich und Eskalation; Ergebnis: Verhandlungs- oder Eskalationslinie.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/rentenpruefer/skills/rentenauskunft-prognose-variantenvergleich
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: social-security
language: de
---

# Rentenauskunft Prognose Variantenvergleich

## Direktstart

Erkläre zuerst, was sicher ist und was nur Prognose ist. Danach folgt ein Variantenvergleich.

## Prüffelder

1. Versicherte Zeiten: anerkannt, ungeklärt, streitig.
2. Entgeltpunkte: Vergangenheit, laufendes Jahr, Prognose.
3. Rentenart: Regelaltersrente, vorzeitige Altersrente, Schwerbehinderung, Erwerbsminderung.
4. Abschlag und Zugangsfaktor.
5. Nettothemen: KVdR, Pflegeversicherung, Steuer, Betriebsrente.

## Visualisierung

| Punkt | sicher | unsicher | zu prüfen |
| --- | --- | --- | --- |
| Wartezeit | aus Bescheid oder Verlauf | fehlende Monate | Kontenklärung |
| Rentenhöhe | bisher erworben | künftiges Entgelt | neue Auskunft |
| Beginn | gesetzlicher Pfad | Gesundheits- oder Beschäftigungswechsel | Variantenplan |

## Normanker

- SGB VI Paragraf 109: Renteninformation und Rentenauskunft.
- SGB VI Paragraf 149: Versicherungsverlauf.

## Output

Schreibe so, dass der Mandant eine Entscheidung treffen kann: „Wenn Sie zum [Datum] gehen, ist der Hauptpreis [Wirkung]. Wenn Sie warten, verbessert sich [Punkt]. Offen bleibt [Beleg].“
