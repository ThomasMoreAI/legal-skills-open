---
name: rechtsberatungsstelle-quellen-livecheck
title: Rechtsquellen-Livecheck
description: 'Für Rechtsquellen-Livecheck: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Plugin für die studentische Rechtsberatungsstelle.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/rechtsberatungsstelle/skills/quellen-livecheck
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

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Rechtsberatungsstelle** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.

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

- Tragende Normen (RDG) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Rechtsberatungsstelle (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
