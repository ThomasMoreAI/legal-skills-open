---
name: jveg-kostenpruefer-output-waehlen
title: Output wählen
description: 'Für Output wählen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: JVEG-Kostenprüfer.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/jveg-kostenpruefer/skills/output-waehlen
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: litigation
language: de
sources:
- title: Quellenhygiene
  path: references/quellenhygiene.md
- title: Zitierweise
  path: references/zitierweise.md
---

# Output wählen

## Einsatzlage

Diese Output-Weiche für **Jveg Kostenpruefer** entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste oder Mandantenbrief der richtige nächste Schritt ist.

## Fachlandkarte dieses Plugins

- `aktenstripper` — Aktenstripper
- `anspruchsberechtigung-antragsgenerator` — Anspruchsberechtigung Antragsgenerator
- `antragsgenerator` — Antragsgenerator
- `belegfeste-formular-portal-und-einreichung` — Belegfeste Formular Portal und Einreichung
- `beschwerde-dolmetscher-sonderfall` — Beschwerde Dolmetscher Sonderfall
- `dolmetscher-sonderfall-und-edge-case` — Dolmetscher Sonderfall und Edge Case
- `dolmetscher-uebersetzer` — Dolmetscher Übersetzer
- `dolmetscher-uebersetzer-fahrtkosten` — Dolmetscher Übersetzer Fahrtkosten
- `dolmetscherkosten-zahlen-schwellen-und-berechnung` — Dolmetscherkosten Zahlen Schwellen und Berechnung
- `fahrtkosten` — Fahrtkosten
- `fahrtkosten-festsetzung-interessen` — Fahrtkosten Festsetzung Interessen
- `festsetzung-beschwerde` — Festsetzung Beschwerde
- `festsetzung-mehrparteien-konflikt-und-interessen` — Festsetzung Mehrparteien Konflikt und Interessen
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Ergebnistyp bestimmen: Schriftsatz an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen, Mandantenmemo, Risikobericht, Vertragsentwurf, Entscheidungsvorlage, Behörden-Stellungnahme — was braucht der Mandant wirklich?
- Pflichtformate festlegen: Tenor / Antrag / Begründung (Anspruchsgrundlage, Tatbestand, Subsumtion, Ergebnis); konkrete Norm-Pinpoints im Jveg Kostenpruefer (JVEG) einarbeiten.
- Adressat-Klarheit: Sprache, Detailtiefe und juristische Vorbildung des Empfängers berücksichtigen; bei Mandant ohne Vorbildung Klartext-Zusammenfassung voranstellen.
- Beweis- und Anlagenstruktur planen (chronologisch, thematisch, K- und B-Anlagen); Bezugnahmen sauber kennzeichnen.
- Quellenfußnoten und Zitierweise sichern; offene Punkte und Annahmen explizit als solche kennzeichnen.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
