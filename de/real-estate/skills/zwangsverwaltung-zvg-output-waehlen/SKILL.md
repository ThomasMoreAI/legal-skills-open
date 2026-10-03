---
name: zwangsverwaltung-zvg-output-waehlen
title: Output wählen
description: 'Für Output wählen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: ZVG-Zwangsverwaltung - Verwalter-Cockpit.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/zwangsverwaltung-zvg/skills/output-waehlen
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: real-estate
language: de
sources:
- title: Quellenhygiene
  path: references/quellenhygiene.md
- title: Zitierweise
  path: references/zitierweise.md
---

# Output wählen

## Einsatzlage

Diese Output-Weiche für **Zwangsverwaltung Zvg** entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste oder Mandantenbrief der richtige nächste Schritt ist.

## Fachlandkarte dieses Plugins

- `aktenanlage-objektcockpit` — Aktenanlage Objektcockpit
- `berichte-beschlagnahme-mietverwaltung-besitz` — Berichte Beschlagnahme Mietverwaltung Besitz
- `berichtswesen-besitzuebernahme-bestellung` — Berichtswesen Besitzuebernahme Bestellung
- `beschlagnahme-fristen-form-und-zustaendigkeit` — Beschlagnahme Fristen Form und Zustaendigkeit
- `beschlagnahme-mietverwaltung-start` — Beschlagnahme Mietverwaltung Start
- `beschlagnahme-oeffentliche-lasten` — Beschlagnahme Oeffentliche Lasten
- `besitz-dokumentenmatrix-und-lueckenliste` — Besitz Dokumentenmatrix und Lueckenliste
- `besitzuebernahme` — Besitzuebernahme
- `bestellung-beschlagnahme` — Bestellung Beschlagnahme
- `betriebskosten-hausgeld-bieterangebot` — Betriebskosten Hausgeld Bieterangebot
- `bieterangebot-bewertung` — Bieterangebot Bewertung
- `bieterangebote-mieten-oeffentliche` — Bieterangebote Mieten Oeffentliche
- `gate-fehlerkatalog` — Gate Fehlerkatalog
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Ergebnistyp bestimmen: Schriftsatz an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen, Mandantenmemo, Risikobericht, Vertragsentwurf, Entscheidungsvorlage, Behörden-Stellungnahme — was braucht der Mandant wirklich?
- Pflichtformate festlegen: Tenor / Antrag / Begründung (Anspruchsgrundlage, Tatbestand, Subsumtion, Ergebnis); konkrete Norm-Pinpoints im Zwangsverwaltung Zvg (ZVG) einarbeiten.
- Adressat-Klarheit: Sprache, Detailtiefe und juristische Vorbildung des Empfängers berücksichtigen; bei Mandant ohne Vorbildung Klartext-Zusammenfassung voranstellen.
- Beweis- und Anlagenstruktur planen (chronologisch, thematisch, K- und B-Anlagen); Bezugnahmen sauber kennzeichnen.
- Quellenfußnoten und Zitierweise sichern; offene Punkte und Annahmen explizit als solche kennzeichnen.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
