---
name: gesellschaftsrecht-quellen-livecheck
title: Rechtsquellen-Livecheck
description: 'Für Rechtsquellen-Livecheck: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Gesellschaftsrecht.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/gesellschaftsrecht/skills/quellen-livecheck
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: corporate
language: de
sources:
- title: Quellenhygiene
  path: references/quellenhygiene.md
- title: Zitierweise
  path: references/zitierweise.md
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Gesellschaftsrecht** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.

## Fachlandkarte dieses Plugins

- `agio-und-kapitalruecklage` — Agio und Kapitalruecklage
- `anmeldungen-verhandlung-vergleich-und-eskalation` — Anmeldungen Verhandlung Vergleich und Eskalation
- `anpassen` — Anpassen
- `mandat-triage-gesellschaftsrecht` — 1. Gesellschaftsrechtlichen Auftrag bearbeiten
- `arbeitsbereich-mandantenentscheidung` — Arbeitsbereich Mandantenentscheidung
- `aufsichtsrat-protokoll` — Aufsichtsrat Protokoll
- `beirat-abgrenzung-aufsichtsrat` — Beirat Abgrenzung Aufsichtsrat
- `beirat-amtszeit-und-rotation` — Beirat Amtszeit und Rotation
- `beirat-bank-und-sanierung` — Beirat Bank und Sanierung
- `beirat-beratungsfunktion-beschlussfassung` — Beirat Beratungsfunktion Beschlussfassung
- `beirat-beschlussfassung` — Beirat Beschlussfassung
- `beirat-beschlussmaengel` — Beirat Beschlussmaengel
- `beirat-bestellung-und-abberufung` — Beirat Bestellung und Abberufung
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Tragende Normen (die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Gesellschaftsrecht (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
