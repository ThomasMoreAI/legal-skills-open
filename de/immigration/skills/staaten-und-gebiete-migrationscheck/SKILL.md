---
name: staaten-und-gebiete-migrationscheck
title: 1. Staaten- und Gebietscheck gezielt durchführen
description: Erschließt den passenden Staaten- oder Gebietscheck für migrationsrechtliche Fragen zu Herkunft, Transit, Urkunden, Visum, Schutz, Passbeschaffung, Rückführung und Aufenthalt.
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/fachanwalt-migrationsrecht/skills/staaten-und-gebiete-migrationscheck
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: immigration
language: de
sources:
- title: Bereich 01
  path: references/bereich-01.md
- title: Bereich 02
  path: references/bereich-02.md
- title: Bereich 03
  path: references/bereich-03.md
- title: Bereich 04
  path: references/bereich-04.md
- title: Bereich 05
  path: references/bereich-05.md
- title: Bereich 06
  path: references/bereich-06.md
- title: Bereich 07
  path: references/bereich-07.md
- title: Bereich 08
  path: references/bereich-08.md
- title: Bereich 09
  path: references/bereich-09.md
- title: Bereich 10
  path: references/bereich-10.md
- title: Bereich 11
  path: references/bereich-11.md
- title: Bereich 12
  path: references/bereich-12.md
- title: Bereich 13
  path: references/bereich-13.md
- title: Bereich 14
  path: references/bereich-14.md
- title: Bereich 15
  path: references/bereich-15.md
- title: Bereich 16
  path: references/bereich-16.md
- title: Bereich 17
  path: references/bereich-17.md
- title: Index
  path: references/index.md
---

# 1. Staaten- und Gebietscheck gezielt durchführen

## 1.1 Zweck und Anwendungsfall

Dieser Skill verbindet einen konkret genannten Staat oder ein Gebiet mit dem migrationsrechtlichen Fachworkflow. Die hinterlegten Arbeitskarten strukturieren Dokumente, Aufenthaltsrecht, Schutzrecht, Rückführung und Strategie; sie enthalten keine verlässliche aktuelle Tatsachenlage zum jeweiligen Staat.

## 1.2 Eingaben

Benötigt werden die Beziehung zum Staat oder Gebiet, derzeitiger Aufenthaltsort und Status, Verfahrensziel, Fristlage, vorhandene Urkunden sowie die konkrete Länder-, Sicherheits- oder Behördenfrage. Bereits vorhandene Aktenstücke werden nach Metadaten erfasst; zunächst werden höchstens fünf tragende Unterlagen geöffnet.

## 1.3 Ablauf

1. Öffne den [Bereichsindex](references/index.md) und bestimme anhand des bisherigen Staatenslugs genau eine Bereichsdatei.
2. Suche dort nach dem exakten `Suchbegriff` und lies nur die zugehörige Arbeitskarte bis zur nächsten Überschrift.
3. Trenne Identität und Urkunden, deutschen Aufenthaltstitel, unionsrechtliche Freizügigkeit, internationalen Schutz, Dublin- oder GEAS-Bezug, Passbeschaffung und Rückführung.
4. Verifiziere jede aktuelle Länder-, Sicherheits-, Botschafts- oder Behördenaussage anhand einer datierten, überprüfbaren Primärquelle. Die Arbeitskarte ersetzt keinen aktuellen Länderbericht.
5. Übergib das Ergebnis an genau einen passenden Fachskill, etwa für Anhörung, Schutzgrund, Familiennachzug, Erwerbsmigration, Einbürgerung, Ausweisung oder Abschiebungsabwehr.

## 1.4 Quellen- und Beweisregel

Nenne Quelle, Herausgeber, Datum, betroffene Region und konkrete Aussage. Trenne allgemeine Lage von individueller Betroffenheit und kennzeichne Übersetzungs-, Echtheits- oder Beschaffungsfragen bei Urkunden. Rechtsprechung wird nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und überprüfbarer Quelle verwendet.

## 1.5 Ausgabeformat

Liefere einen Staatenvermerk mit Status und Ziel, Dokumentenlage, aktueller Quellenlage, individueller Betroffenheit, Frist, Beweisbedarf, stärkster Gegenposition und nächstem Arbeitsprodukt. Beginne bei Eilbedarf mit Frist und Sicherungsmaßnahme.

## 1.6 Beispiel

Bei einem Afghanistan-Bezug wird die Arbeitskarte über `staat-afghanistan-migrationscheck` gefunden. Danach werden nur die konkrete Urkunden-, Schutz- oder Rückführungsfrage und die dazu aktuellen Quellen bearbeitet; andere Staatenkarten bleiben geschlossen.
