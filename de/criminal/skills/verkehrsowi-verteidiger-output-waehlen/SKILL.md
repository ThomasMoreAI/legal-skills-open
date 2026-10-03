---
name: verkehrsowi-verteidiger-output-waehlen
title: Output wählen
description: 'Für Output wählen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: VerkehrsOWi-Verteidiger.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/verkehrsowi-verteidiger/skills/output-waehlen
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: criminal
language: de
sources:
- title: Quellenhygiene
  path: references/quellenhygiene.md
- title: Zitierweise
  path: references/zitierweise.md
---

# Output wählen

## Einsatzlage

Diese Output-Weiche für **Verkehrsowi Verteidiger** entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste oder Mandantenbrief der richtige nächste Schritt ist.

## Fachlandkarte dieses Plugins

- `abstand-quellenkarte` — Abstand Quellenkarte
- `akteneinsicht-internationaler-bezug-und-schnittstellen` — Akteneinsicht Internationaler Bezug und Schnittstellen
- `alkohol-compliance-dokumentation-und-akte` — Alkohol Compliance Dokumentation und Akte
- `alkohol-drogen-beweisverwertung` — Alkohol Drogen Beweisverwertung
- `amtsgericht-drogen-interessen-einspruch` — Amtsgericht Drogen Interessen Einspruch
- `anhoerung-verkehrsowi-einspruch-messverfahren` — Anhoerung Verkehrsowi Einspruch Messverfahren
- `bussgeldbescheid-tatbestand-beweis-und-belege` — Bussgeldbescheid Tatbestand Beweis und Belege
- `drogen-mehrparteien-konflikt-und-interessen` — Drogen Mehrparteien Konflikt und Interessen
- `einspruch-dokumentenmatrix-und-lueckenliste` — Einspruch Dokumentenmatrix und Lueckenliste
- `fahrverbot-geschwindigkeit-handy` — Fahrverbot Geschwindigkeit Handy
- `geschwindigkeit-verhandlung-vergleich-und-eskalation` — Geschwindigkeit Verhandlung Vergleich und Eskalation
- `handy-zahlen-schwellen-und-berechnung` — Handy Zahlen Schwellen und Berechnung
- `hauptverhandlung-sonderfall-messakte-messung` — Hauptverhandlung Sonderfall Messakte Messung
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Ergebnistyp bestimmen: Schriftsatz an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen, Mandantenmemo, Risikobericht, Vertragsentwurf, Entscheidungsvorlage, Behörden-Stellungnahme — was braucht der Mandant wirklich?
- Pflichtformate festlegen: Tenor / Antrag / Begründung (Anspruchsgrundlage, Tatbestand, Subsumtion, Ergebnis); konkrete Norm-Pinpoints im Verkehrsowi Verteidiger (die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen) einarbeiten.
- Adressat-Klarheit: Sprache, Detailtiefe und juristische Vorbildung des Empfängers berücksichtigen; bei Mandant ohne Vorbildung Klartext-Zusammenfassung voranstellen.
- Beweis- und Anlagenstruktur planen (chronologisch, thematisch, K- und B-Anlagen); Bezugnahmen sauber kennzeichnen.
- Quellenfußnoten und Zitierweise sichern; offene Punkte und Annahmen explizit als solche kennzeichnen.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
