---
name: verkehr-infrastrukturrecht-output-waehlen
title: Output wählen
description: 'Für Output wählen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Verkehrs- und Infrastrukturrecht.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/verkehr-infrastrukturrecht/skills/output-waehlen
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: transportation
language: de
sources:
- title: Quellenhygiene
  path: references/quellenhygiene.md
- title: Zitierweise
  path: references/zitierweise.md
---

# Output wählen

## Einsatzlage

Diese Output-Weiche für **Verkehr Infrastrukturrecht** entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste oder Mandantenbrief der richtige nächste Schritt ist.

## Fachlandkarte dieses Plugins

- `anschluss-router` — Anschluss Router
- `autonomous-driving` — Autonomous Driving
- `autonomous-driving-interessen-grossprojekt` — Autonomous Driving Interessen Grossprojekt
- `autonomous-driving-strassenrecht` — Autonomous Driving Strassenrecht
- `buergerentscheid-strassenbahn-spezial` — Buergerentscheid Strassenbahn Spezial
- `driving-mehrparteien-konflikt-und-interessen` — Driving Mehrparteien Konflikt und Interessen
- `foerderung-vergabe-ladeinfrastruktur` — Foerderung Vergabe Ladeinfrastruktur
- `grossprojekt-zahlen-schwellen-und-berechnung` — Grossprojekt Zahlen Schwellen und Berechnung
- `infrastruktur-foerderung-nachhaltige` — Infrastruktur Foerderung Nachhaltige
- `infrastrukturrecht-intake-ladeinfrastruktur` — Infrastrukturrecht Intake Ladeinfrastruktur
- `intake-mandantenkommunikation-entscheidungsvorlage` — Intake Mandantenkommunikation Entscheidungsvorlage
- `ladeinfrastruktur` — Ladeinfrastruktur
- `ladeinfrastruktur-behoerden-gericht-und-registerweg` — Ladeinfrastruktur Behoerden Gericht und Registerweg
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Ergebnistyp bestimmen: Schriftsatz an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen, Mandantenmemo, Risikobericht, Vertragsentwurf, Entscheidungsvorlage, Behörden-Stellungnahme — was braucht der Mandant wirklich?
- Pflichtformate festlegen: Tenor / Antrag / Begründung (Anspruchsgrundlage, Tatbestand, Subsumtion, Ergebnis); konkrete Norm-Pinpoints im Verkehr Infrastrukturrecht (die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen) einarbeiten.
- Adressat-Klarheit: Sprache, Detailtiefe und juristische Vorbildung des Empfängers berücksichtigen; bei Mandant ohne Vorbildung Klartext-Zusammenfassung voranstellen.
- Beweis- und Anlagenstruktur planen (chronologisch, thematisch, K- und B-Anlagen); Bezugnahmen sauber kennzeichnen.
- Quellenfußnoten und Zitierweise sichern; offene Punkte und Annahmen explizit als solche kennzeichnen.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
