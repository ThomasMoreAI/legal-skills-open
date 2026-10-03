---
name: historische-behauptungen-pruefen
title: Historische Behauptungen prüfen
description: Prüft PrALR-Aussagen auf falsche Fundstellen, Rückprojektionen und unbelegte Rezeptionslinien. Liefert einen begründeten Korrekturvermerk zu einer vorgelegten These.
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/preussisches-allgemeines-landrecht-pralr/skills/historische-behauptungen-pruefen
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: general
language: de
sources:
- title: Methodik keine anachronismen
  path: references/methodik-keine-anachronismen.md
- title: Pralr 032 methodik keine anachronismen
  path: references/pralr-032-methodik-keine-anachronismen.md
- title: Pralr 047 red team falsche pralr behauptungen
  path: references/pralr-047-red-team-falsche-pralr-behauptungen.md
- title: Red team falsche behauptungen
  path: references/red-team-falsche-behauptungen.md
---

# Historische Behauptungen prüfen

## 1. Zweck und Anwendungsfall

Prüft PrALR-Aussagen auf falsche Fundstellen, Rückprojektionen und unbelegte Rezeptionslinien. Liefert einen begründeten Korrekturvermerk zu einer vorgelegten These.

## 2. Eingaben

Behaupteter Satz, Fundstelle, historischer Kontext und gegebenenfalls Vergleichsnorm. Vorhandenes Material zuerst lesen. Nur eine entscheidende Lücke gebündelt nachfragen; ungesicherte Angaben sichtbar offenlassen.

## 3. Ablauf

### 3.1. Fachprüfung

Behauptung in überprüfbare Teilthesen zerlegen. Wortlaut, Systemstelle, Geltung und tatsächliche Praxis getrennt prüfen. Ähnlichkeit ist kein Rezeptionsnachweis; ein heutiger Begriff ersetzt keine historische Tatbestandsprüfung. Nur belegbare Fehler korrigieren, den Rest als offen kennzeichnen.

### 3.2. Zeit- und Geltungsgrenze

Maßstab sind Ort, Zeit und konkrete Fassung des historischen Falls. Heutiges Recht nur bei ausdrücklich verlangtem Vergleich oder einer tatsächlichen Anschlussfrage gesondert prüfen. Kein festes Gegenwartsjahr und kein allgemeiner BGB-Normenradar. Normtext, damalige Anwendungspraxis und spätere Rezeption getrennt ausweisen.

### 3.3. Vertiefung bei Bedarf

Die folgenden Materialien sind bewahrte frühere Arbeitsentwürfe, keine zusätzlichen auswählbaren Skills und keine geprüften Primärquellen. Nur die zur konkreten Teilfrage passende Datei laden, nicht alle Fassungen vorsorglich. Fachfremde Normenradare wurden entfernt; verbliebene Altzitate, Fristen und Falllösungen müssen vor Verwendung verifiziert werden.

- Bei Fragen zu „Keine Anachronismen“: [Fachmaterial](references/methodik-keine-anachronismen.md).
- Bei Fragen zu „Keine Anachronismen“: [ergänzende Fassung 2](references/pralr-032-methodik-keine-anachronismen.md).
- Bei Fragen zu „Red-Team“: [Fachmaterial](references/pralr-047-red-team-falsche-pralr-behauptungen.md).
- Bei Fragen zu „Red-Team“: [ergänzende Fassung 2](references/red-team-falsche-behauptungen.md).

## 4. Quellenpflicht

[Zitierweise](../../../references/zitierweise.md) und [historischer Quellenprüfvermerk](../../references/historische-quellenpruefung.md) beachten. Ausgabe, Teil, Titel, Paragraf und konkrete Fundstelle nennen. Für tragende Wörter Seitenbild und Transkription abgleichen; ohne verfügbares Seitenbild den begrenzten Textzeugenstatus offenlegen. Nur neu oder entscheidend verwendete historische Primärstellen gezielt prüfen, keine sachfremde Aktualitätsrecherche erzwingen. Literatur nur aus bereitgestelltem oder tatsächlich verifiziertem Text verwenden.

## 5. Ausgabeformat

Das verlangte Arbeitsprodukt in vollständigen, ausformulierten Sätzen liefern; keine Skelette, Halbsätze oder reine Stichwortausgabe. Gesicherten Textbefund, historische Bewertung, Gegenbefund und offene Quelle erkennbar trennen. Tabellen nur für echte Vergleiche oder Belege verwenden. Formatierte Dokumente: Times New Roman 11 pt, ausschließlich dezimale Gliederung mit Leerzeilen; bei Markdown als Exporthinweis nennen.

## 6. Beispiel

Die These, jeder Grenzübertritt habe 1794 versklavte Menschen sofort befreit, wird gegen die Ausnahmen in Teil 2 Titel 5 geprüft.
