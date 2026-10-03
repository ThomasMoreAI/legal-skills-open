---
name: pralr-normenbibliothek
title: PrALR-Norm auffinden
description: Findet eine bestimmte PrALR-Norm anhand von Teil, Titel, Paragraf oder enger Sachfrage. Lädt nur den einschlägigen Bibliotheksabschnitt und prüft dessen Systemstelle.
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/preussisches-allgemeines-landrecht-pralr/skills/pralr-normenbibliothek
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: general
language: de
sources:
- title: Band teil titel navigation
  path: references/band-teil-titel-navigation.md
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
- title: Index
  path: references/index.md
- title: Pralr 006 systematik einleitung teile titel
  path: references/pralr-006-systematik-einleitung-teile-titel.md
- title: Pralr 043 band teil titel navigation
  path: references/pralr-043-band-teil-titel-navigation.md
- title: Pralr neu 001 normnavigator jede pralr norm karte erschliessen
  path: references/pralr-neu-001-normnavigator-jede-pralr-norm-karte-erschliessen.md
- title: Pralr normenbibliothek
  path: references/pralr-normenbibliothek.md
- title: Systematik einleitung teile titel
  path: references/systematik-einleitung-teile-titel.md
---

# PrALR-Norm auffinden

## 1. Zweck und Anwendungsfall

Findet eine bestimmte PrALR-Norm anhand von Teil, Titel, Paragraf oder enger Sachfrage. Lädt nur den einschlägigen Bibliotheksabschnitt und prüft dessen Systemstelle.

## 2. Eingaben

Gesuchte Regel, Teil und Titel soweit bekannt, Suchwörter, vorgelegter Textzeuge. Vorhandenes Material zuerst lesen. Nur eine entscheidende Lücke gebündelt nachfragen; ungesicherte Angaben sichtbar offenlassen.

## 3. Ablauf

### 3.1. Fachprüfung

Inhaltsverzeichnis und Seitenbild vor Dateinamen auswerten. Bandzählung nicht mit Teilzählung gleichsetzen. Bibliothekskarten sind Arbeitshilfen, keine verifizierten Gesetzestexte; die im Auftrag entscheidende Norm samt Nachbarvorschriften separat lesen.

### 3.2. Zeit- und Geltungsgrenze

Maßstab sind Ort, Zeit und konkrete Fassung des historischen Falls. Heutiges Recht nur bei ausdrücklich verlangtem Vergleich oder einer tatsächlichen Anschlussfrage gesondert prüfen. Kein festes Gegenwartsjahr und kein allgemeiner BGB-Normenradar. Normtext, damalige Anwendungspraxis und spätere Rezeption getrennt ausweisen.

### 3.3. Vertiefung bei Bedarf

Die folgenden Materialien sind bewahrte frühere Arbeitsentwürfe, keine zusätzlichen auswählbaren Skills und keine geprüften Primärquellen. Nur die zur konkreten Teilfrage passende Datei laden, nicht alle Fassungen vorsorglich. Fachfremde Normenradare wurden entfernt; verbliebene Altzitate, Fristen und Falllösungen müssen vor Verwendung verifiziert werden.

Für die vorhandenen Normkarten den [Bereichsindex](references/index.md) öffnen und ausschließlich den passenden Abschnitt der dort verlinkten Bereichsdatei lesen. Der Bestand wurde nicht vollständig fachlich verifiziert; eine dortige Fundstelle bleibt bis zur Primärtextprüfung ein Suchhinweis.

- Bei Fragen zu „Navigation im Band“: [Fachmaterial](references/band-teil-titel-navigation.md).
- Bei Fragen zu „Navigation im Band“: [ergänzende Fassung 2](references/pralr-043-band-teil-titel-navigation.md).
- Bei Fragen zu „Systematik“: [Fachmaterial](references/pralr-006-systematik-einleitung-teile-titel.md).
- Bei Fragen zu „Systematik“: [ergänzende Fassung 2](references/systematik-einleitung-teile-titel.md).
- Bei Fragen zu „Normnavigator jede PrALR-Norm als Karte erschließen“: [Fachmaterial](references/pralr-neu-001-normnavigator-jede-pralr-norm-karte-erschliessen.md).
- Bei Fragen zu „1. Normen des Preußischen Allgemeinen Landrechts erschließen“: [Fachmaterial](references/pralr-normenbibliothek.md).

## 4. Quellenpflicht

[Zitierweise](../../../references/zitierweise.md) und [historischer Quellenprüfvermerk](../../references/historische-quellenpruefung.md) beachten. Ausgabe, Teil, Titel, Paragraf und konkrete Fundstelle nennen. Für tragende Wörter Seitenbild und Transkription abgleichen; ohne verfügbares Seitenbild den begrenzten Textzeugenstatus offenlegen. Nur neu oder entscheidend verwendete historische Primärstellen gezielt prüfen, keine sachfremde Aktualitätsrecherche erzwingen. Literatur nur aus bereitgestelltem oder tatsächlich verifiziertem Text verwenden.

## 5. Ausgabeformat

Das verlangte Arbeitsprodukt in vollständigen, ausformulierten Sätzen liefern; keine Skelette, Halbsätze oder reine Stichwortausgabe. Gesicherten Textbefund, historische Bewertung, Gegenbefund und offene Quelle erkennbar trennen. Tabellen nur für echte Vergleiche oder Belege verwenden. Formatierte Dokumente: Times New Roman 11 pt, ausschließlich dezimale Gliederung mit Leerzeilen; bei Markdown als Exporthinweis nennen.

## 6. Beispiel

Eine Erbrechtsfrage nicht allein wegen eines alten Dateinamens Titel 17 zuordnen: Erwerbsgrund, Verfügung und gemeinschaftlicher Nachlass verlangen unterschiedliche Suchstellen.
