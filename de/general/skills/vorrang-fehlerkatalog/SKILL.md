---
name: vorrang-fehlerkatalog
title: Vorrang Fehlerkatalog
description: 'Für Vorrang Fehlerkatalog: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/methodenlehre-buergerliches-recht/skills/vorrang-fehlerkatalog
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: general
language: de
sources:
- title: Quellenhygiene
  path: references/quellenhygiene.md
---

# Vorrang Fehlerkatalog

## Zweck

Dieser Fehlerkatalog prüft Arbeitsergebnisse für **Methodenlehre Bürgerliches Recht** vor Abgabe, Versand oder Mandantenfreigabe gegen die im Sachgebiet typischen Fehlerquellen — jeweils mit Symptom, Diagnose und Heilung.

## Fehlerkatalog

### 1. Schlüsseldokument fehlt oder veraltet (Norm-/Gesetzestext)

- **Symptom:** Schlüsseldokument fehlt oder veraltet (Norm-/Gesetzestext)
- **Diagnose:** Arbeit mit Entwurfs- oder Altfassung statt der maßgeblichen Version
- **Heilung:** Versionsstand und Datum jedes Dokuments prüfen; maßgebliche Fassung in der Akte markieren

### 2. Normzitat ohne Fassungsprüfung (BGB)

- **Symptom:** Normzitat ohne Fassungsprüfung (BGB)
- **Diagnose:** Zitierte Norm wurde geändert, verschoben oder aufgehoben
- **Heilung:** Vor Abgabe jeden Paragraphen gegen gesetze-im-internet.de prüfen; Übergangsvorschriften beachten

### 3. Rechtsprechung aus Modellwissen zitiert

- **Symptom:** Rechtsprechung aus Modellwissen zitiert
- **Diagnose:** Aktenzeichen oder Fundstelle nicht live verifiziert — Risiko halluzinierter Zitate
- **Heilung:** Jede Entscheidung mit Gericht, Datum, Az und frei prüfbarer Quelle gegenchecken; sonst als Prüfpunkt markieren

### 4. Mandantengeheimnis bei Tool-Einsatz verletzt

- **Symptom:** Mandantengeheimnis bei Tool-Einsatz verletzt
- **Diagnose:** Klartext-Mandantendaten in Werkzeug ohne Auftragsverarbeitungsvertrag
- **Heilung:** Vor Upload anonymisieren oder AVV-gedeckte Umgebung nutzen (§ 43a Abs. 2 BRAO, § 203 StGB)

## Ausgabe

Roter/gelber/grüner Befund je Fehlerachse; jeder rote Punkt mit konkreter Korrektur und verbleibendem Restrisiko. Quellenhygiene nach `references/quellenhygiene.md`.
