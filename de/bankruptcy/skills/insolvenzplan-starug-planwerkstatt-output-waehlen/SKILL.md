---
name: insolvenzplan-starug-planwerkstatt-output-waehlen
title: Output wählen
description: 'Für Output wählen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Insolvenzplan- und StaRUG-Planwerkstatt.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/insolvenzplan-starug-planwerkstatt/skills/output-waehlen
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

Diese Output-Weiche für **Insolvenzplan Starug Planwerkstatt** entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste oder Mandantenbrief der richtige nächste Schritt ist.

## Fachlandkarte dieses Plugins

- `abstimmung-anlagen-interessen-cram` — Abstimmung Anlagen Interessen Cram
- `abstimmung-mehrheiten-anlagenpaket` — Abstimmung Mehrheiten Anlagenpaket
- `anlagen-mehrparteien-konflikt-und-interessen` — Anlagen Mehrparteien Konflikt und Interessen
- `anlagenpaket` — Anlagenpaket
- `asset-deals-im-plan-grundstuecke-marken-kundendaten` — Asset Deals im Plan Grundstuecke Marken Kundendaten
- `cram-formular-portal-und-einreichung` — Cram Formular Portal und Einreichung
- `cramdown-obstruktion-datenraum-register` — Cramdown Obstruktion Datenraum Register
- `darstellender-quellenkarte` — Darstellender Quellenkarte
- `darstellender-teil` — Darstellender Teil
- `datenraum-register` — Datenraum Register
- `down-red-gestaltender-gruppen` — Down RED Gestaltender Gruppen
- `gerichtliche-schritte-kommandocenter` — Gerichtliche Schritte Kommandocenter
- `gestaltender-teil` — Gestaltender Teil
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Ergebnistyp bestimmen: Schriftsatz an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen, Mandantenmemo, Risikobericht, Vertragsentwurf, Entscheidungsvorlage, Behörden-Stellungnahme — was braucht der Mandant wirklich?
- Pflichtformate festlegen: Tenor / Antrag / Begründung (Anspruchsgrundlage, Tatbestand, Subsumtion, Ergebnis); konkrete Norm-Pinpoints im Insolvenzplan Starug Planwerkstatt (StaRUG) einarbeiten.
- Adressat-Klarheit: Sprache, Detailtiefe und juristische Vorbildung des Empfängers berücksichtigen; bei Mandant ohne Vorbildung Klartext-Zusammenfassung voranstellen.
- Beweis- und Anlagenstruktur planen (chronologisch, thematisch, K- und B-Anlagen); Bezugnahmen sauber kennzeichnen.
- Quellenfußnoten und Zitierweise sichern; offene Punkte und Annahmen explizit als solche kennzeichnen.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
