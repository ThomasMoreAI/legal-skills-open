---
name: register-gutachten-klage
title: Output Register/Gutachten/Klage
description: 'Für Output Register/Gutachten/Klage: erstellt Entwurf mit Antrag, Beweis und Anlagen; Ergebnis: Schriftsatz mit Begründungs- und Anlagenlogik.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/handelsrecht-hgb/skills/register-gutachten-klage
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: commercial
language: de
---

# Output Register/Gutachten/Klage

## Sofortstart

1. Kläre Rolle, Ziel, Gegner, Frist, Dokumente und gewünschtes Arbeitsprodukt.
2. Zerlege den Fall in Tatsachen, Normen, Streitpunkte, Beweisfragen und methodische Wertungen.
3. Liefere zuerst eine Kurzantwort mit Risikoampel, danach den Prüfpfad.
4. Schlage nach jedem Zwischenergebnis zwei bis fünf passende Anschluss-Skills aus demselben Plugin vor.

## Rechts- und Quellenanker

HGB amtlich prüfen: https://www.gesetze-im-internet.de/hgb/. Je nach Thema außerdem BGB, FamFG, HRV, BeurkG, GmbHG, AktG und EU-/internationales Recht live gegenprüfen.

## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.
