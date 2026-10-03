---
name: stb-liquiditaetsvorschau-3-6-12-monate
title: Liquiditaetsvorschau 3/6/12 Monate
description: 'Für Liquiditätsvorschau 3/6/12 Monate: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/steuerrecht-anwalt-und-berater/skills/stb-liquiditaetsvorschau-3-6-12-monate
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: tax
language: de
sources:
- title: Idw s6 kernelemente
  path: references/idw-s6-kernelemente.md
- title: Wochenraster anleitung
  path: references/wochenraster-anleitung.md
---

# Liquiditaetsvorschau 3/6/12 Monate

Dieser Skill erstellt eine rollierende Liquiditaetsplanung fuer Krisenmandate. Er ist fuer Steuerberater, Sanierungsberater und Anwaelte gedacht, wenn aus BWA, OPOS, Bankdaten, Finanzierungszusagen und Massnahmenplan eine belastbare Vorschau entstehen soll.

## Normenanker

- §§ 17, 18, 19 InsO fuer Liquiditaets- und Fortbestehensbezug.
- § 15a InsO fuer Eskalation bei Insolvenzreife.
- Paragraf 102 StaRUG nur bei Jahresabschlusserstellung, offenkundigen Anhaltspunkten für einen möglichen Insolvenzgrund und vermuteter Unkenntnis des Mandanten.
- §§ 34, 69 AO fuer Steuerzahlungs- und Haftungsrisiken.
- § 43 GmbHG fuer Geschaeftsfuehrerpflichten.

## Arbeitsgang

1. Starte mit Bankbestand, freien Linien und faelligen Verbindlichkeiten.
2. Plane Einzahlungen und Auszahlungen wochenweise; unsichere Zufluesse werden gesondert markiert.
3. Trenne Regelbetrieb, Sanierungsmassnahmen und Einmaleffekte.
4. Nutze `references/wochenraster-anleitung.md`, `references/idw-s6-kernelemente.md` und die Excel-Vorlage.
5. Zeige Kipppunkte, Mindestliquiditaet und Massnahmenbedarf.

## Ergebnis

Liefere eine Wochenvorschau mit Ampel, Liquiditaetsluecke, Massnahmenliste, Annahmenprotokoll und Hinweis, welche Daten vor einer Insolvenzreifeaussage noch fehlen.
