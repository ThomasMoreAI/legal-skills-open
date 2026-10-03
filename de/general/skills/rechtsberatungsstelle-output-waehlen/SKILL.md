---
name: rechtsberatungsstelle-output-waehlen
title: Output wählen
description: 'Für Output wählen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Plugin für die studentische Rechtsberatungsstelle.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/rechtsberatungsstelle/skills/output-waehlen
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: general
language: de
sources:
- title: Quellenhygiene
  path: references/quellenhygiene.md
- title: Zitierweise
  path: references/zitierweise.md
---

# Output wählen

## Einsatzlage

Diese Output-Weiche für **Rechtsberatungsstelle** entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste oder Mandantenbrief der richtige nächste Schritt ist.

## Fachlandkarte dieses Plugins

- `anlaufstellen-beweislast-anleiter-bono` — Anlaufstellen Beweislast Anleiter Bono
- `anleiter-formular-portal-und-einreichung` — Anleiter Formular Portal und Einreichung
- `anleiter-pruefwarteschlange` — Anleiter Prüfwarteschlange
- `anpassen` — Anpassen
- `anschluss-router` — Anschluss Router
- `bono-erstpruefung-und-mandatsziel` — Bono Erstpruefung und Mandatsziel
- `briefe-erstberatung-rdg-konform` — Briefe Erstberatung RDG Konform
- `einarbeitung` — Einarbeitung
- `einfache-sprache-briefe` — Einfache Sprache Briefe
- `entwurf-einarbeitung-einfache-sprache` — Entwurf Einarbeitung Einfache Sprache
- `erstberatung-rdg-grenzen-und-triage` — Erstberatung RDG Grenzen und Triage
- `erzeugung-leitfaden-erstellen-mandanten` — Erzeugung Leitfaden Erstellen Mandanten
- `fristen-fristenkontrolle-rdg` — Fristen Fristenkontrolle RDG
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Ergebnistyp bestimmen: Schriftsatz an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen, Mandantenmemo, Risikobericht, Vertragsentwurf, Entscheidungsvorlage, Behörden-Stellungnahme — was braucht der Mandant wirklich?
- Pflichtformate festlegen: Tenor / Antrag / Begründung (Anspruchsgrundlage, Tatbestand, Subsumtion, Ergebnis); konkrete Norm-Pinpoints im Rechtsberatungsstelle (RDG) einarbeiten.
- Adressat-Klarheit: Sprache, Detailtiefe und juristische Vorbildung des Empfängers berücksichtigen; bei Mandant ohne Vorbildung Klartext-Zusammenfassung voranstellen.
- Beweis- und Anlagenstruktur planen (chronologisch, thematisch, K- und B-Anlagen); Bezugnahmen sauber kennzeichnen.
- Quellenfußnoten und Zitierweise sichern; offene Punkte und Annahmen explizit als solche kennzeichnen.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
