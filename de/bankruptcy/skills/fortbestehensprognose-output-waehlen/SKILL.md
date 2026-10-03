---
name: fortbestehensprognose-output-waehlen
title: Output wählen
description: 'Für Output wählen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Fortbestehensprognose.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/fortbestehensprognose/skills/output-waehlen
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: bankruptcy
language: de
sources:
- title: Quellenhygiene
  path: references/quellenhygiene.md
- title: Zitierweise
  path: references/zitierweise.md
---

# Output wählen

## Einsatzlage

Diese Output-Weiche für **Fortbestehensprognose** entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste oder Mandantenbrief der richtige nächste Schritt ist.

## Fachlandkarte dieses Plugins

- `annahmen-behoerden-gericht-und-registerweg` — Annahmen Behoerden Gericht und Registerweg
- `annahmen-belastbarkeit-plausibilisieren` — Annahmen Belastbarkeit Plausibilisieren
- `annahmen-sammeln-bilanzieller-status` — Annahmen Sammeln Bilanzieller Status
- `ausloesendes-ereignis-erfassen` — Ausloesendes Ereignis Erfassen
- `bilanzieller-status-aufnehmen` — Bilanzieller Status Aufnehmen
- `bilanzstatus-risikoampel-und-gegenargumente` — Bilanzstatus Risikoampel und Gegenargumente
- `comfortletter-sonderfall-edge` — Comfortletter Sonderfall Edge
- `comfortletter-weich-erzeugen` — Comfortletter Weich Erzeugen
- `eskalation-sonderfall-und-edge-case` — Eskalation Sonderfall und Edge Case
- `fbp-bankenkommunikation-waiver-integrierte` — FBP Bankenkommunikation Waiver Integrierte
- `fbp-integrierte-planung-bauleiter` — FBP Integrierte Planung Bauleiter
- `fbp-stresstest-szenarien-leitfaden` — FBP Stresstest Szenarien Leitfaden
- `fbp-zahlungsunfaehigkeit` — FBP Zahlungsunfaehigkeit
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Ergebnistyp bestimmen: Schriftsatz an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen, Mandantenmemo, Risikobericht, Vertragsentwurf, Entscheidungsvorlage, Behörden-Stellungnahme — was braucht der Mandant wirklich?
- Pflichtformate festlegen: Tenor / Antrag / Begründung (Anspruchsgrundlage, Tatbestand, Subsumtion, Ergebnis); konkrete Norm-Pinpoints im Fortbestehensprognose (InsO, StaRUG, § 19 Abs) einarbeiten.
- Adressat-Klarheit: Sprache, Detailtiefe und juristische Vorbildung des Empfängers berücksichtigen; bei Mandant ohne Vorbildung Klartext-Zusammenfassung voranstellen.
- Beweis- und Anlagenstruktur planen (chronologisch, thematisch, K- und B-Anlagen); Bezugnahmen sauber kennzeichnen.
- Quellenfußnoten und Zitierweise sichern; offene Punkte und Annahmen explizit als solche kennzeichnen.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
