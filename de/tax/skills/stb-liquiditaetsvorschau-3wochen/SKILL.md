---
name: stb-liquiditaetsvorschau-3wochen
title: Drei-Wochen-Liquiditaetsvorschau
description: 'Für Drei-Wochen-Liquiditätsvorschau: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/steuerrecht-anwalt-und-berater/skills/stb-liquiditaetsvorschau-3wochen
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: tax
language: de
---

# Drei-Wochen-Liquiditaetsvorschau

Dieser Skill ist die schnelle Krisenampel fuer akute Zahlungsengpaesse. Er ersetzt kein vollstaendiges Gutachten, zeigt aber, ob sofort eine vertiefte Insolvenzreifepruefung, Geschaeftsfuehrerwarnung oder Sanierungsmassnahme erforderlich ist.

## Normenanker

- § 17 InsO fuer Zahlungsunfaehigkeit.
- § 15a InsO fuer Antragspflicht bei juristischen Personen.
- § 64 GmbHG a.F. nur fuer Altfaelle; aktuell § 15b InsO fuer Zahlungen nach Insolvenzreife.
- §§ 34, 69 AO fuer Steuerrueckstaende.
- § 266a StGB fuer Arbeitnehmeranteile zur Sozialversicherung.

## Arbeitsgang

1. Erfasse faellige Verbindlichkeiten und binnen drei Wochen faellig werdende Posten.
2. Erfasse liquide Mittel, freie Linien und sichere Zahlungseingaenge.
3. Unsichere Forderungen, Stundungsbitten und erwartete Gesellschafterbeitraege werden nicht als sicherer Zufluss behandelt.
4. Nutze `werkzeuge/` nur zur Berechnung; die rechtliche Bewertung bleibt gesondert.

## Ergebnis

Gib eine Drei-Wochen-Ampel mit Liquiditaetsluecke, kritischen Faelligkeiten, fehlenden Nachweisen und konkretem Eskalationssatz fuer Mandant oder Geschaeftsfuehrung aus.
