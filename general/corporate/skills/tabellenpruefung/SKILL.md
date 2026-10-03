---
name: tabellenpruefung
title: Tabellenpruefung Gesellschaftsrecht
description: 'Für Tabellenprüfung Gesellschaftsrecht: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Tatbestands- oder Anspruchsmatrix.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/gesellschaftsrecht/skills/tabellenpruefung
license: Apache-2.0
version: 0.1.1
execution_mode: open
jurisdiction: general
practice: corporate
language: de
sources:
- title: Excel output
  path: references/excel-output.md
- title: Gsheets output
  path: references/gsheets-output.md
- title: Ma diligence columns
  path: references/ma-diligence-columns.md
---

# Tabellenpruefung Gesellschaftsrecht

Dieser Skill verwandelt gesellschaftsrechtliche Unterlagen in eine belastbare Prueftabelle. Er ist richtig, wenn viele Dokumente gleichzeitig ausgewertet werden muessen: Satzung, Gesellschafterliste, Cap Table, Beteiligungsvertrag, Wandeldarlehen, SHA, Registerauszug, Beiratsprotokoll, DD-Ordner oder Closing-Checkliste.

## Normenanker

- Paragraf 13, 15, 16, 35, 40 GmbHG fuer GmbH-Status, Anteilsuebertragung und Gesellschafterliste.
- Paragraf 53, 54 GmbHG fuer Satzungsaenderung und Kapitalmassnahmen.
- Paragraf 705 ff. BGB fuer Personengesellschaftsbezug nach MoPeG.
- Paragraf 15, 161 HGB fuer Registerpublizitaet und KG-Strukturen.
- Paragraf 311 ff., 241 Abs. 2, 280 BGB fuer vorvertragliche und vertragliche Pflichten in Transaktionsunterlagen.

## Arbeitsgang

1. Bestimme die Tabellenspalten nach dem Pruefziel: Beteiligungsquote, Stimmrecht, Verwässerung, Vesting, Drag/Tag, Liquidation Preference, Consent Matter, Registerstand, Closing Deliverable.
2. Erfasse jede Datei als eigene Zeile und jede rechtliche Datenfrage als eigene Spalte.
3. Jede Zelle bekommt entweder ein kurzes Quellenzitat mit Fundstelle oder den Status `nicht gefunden`.
4. Nutze die Referenzen in `references/` fuer Excel-, Google-Sheets- und M&A-Spaltenschemata.

## Ergebnis

Liefere eine Tabelle mit Ampelstatus, Quellenbeleg, Pruefvermerk und naechstem Schritt. Keine Schlussfolgerung ohne Zelle und Quelle.
