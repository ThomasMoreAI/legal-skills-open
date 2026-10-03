---
name: prozessrecht-quellen-livecheck
title: Rechtsquellen-Livecheck
description: 'Für Rechtsquellen-Livecheck: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Prozessrecht.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/prozessrecht/skills/quellen-livecheck
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

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Prozessrecht** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.

## Fachlandkarte dieses Plugins

- `amtlicher-zpo-proz-bauleiter-eilverfahren` — Amtlicher ZPO Proz Bauleiter Eilverfahren
- `anspruchstabelle-beweislast` — Anspruchstabelle Beweislast
- `anspruchstabelle-gegenseite-interessen` — Anspruchstabelle Gegenseite Interessen
- `anwaltsgeheimnis-pruefung` — Anwaltsgeheimnis Prüfung
- `argumentationsverbesserung-red-team` — Argumentationsverbesserung RED Team
- `beweissicherung-einstweilige-verfuegung` — Beweissicherung Einstweilige Verfuegung
- `chronologie` — Chronologie
- `eilverfahren-risikoampel-und-gegenargumente` — Eilverfahren Risikoampel und Gegenargumente
- `einstweilige-verfuegung` — Einstweilige Verfuegung
- `gegenseite-mehrparteien-konflikt-und-interessen` — Gegenseite Mehrparteien Konflikt und Interessen
- `gegenseite-status-mahnbescheid-mahnschreiben` — Gegenseite Status Mahnbescheid Mahnschreiben
- `kaltstart-interview` — Kaltstart Interview
- `mahnbescheid` — Mahnbescheid
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Tragende Normen (die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Prozessrecht (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
