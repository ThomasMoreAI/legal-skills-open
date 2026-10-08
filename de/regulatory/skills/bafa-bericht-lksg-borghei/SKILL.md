---
name: bafa-bericht-lksg-borghei
title: /lieferkettengesetz:bafa-bericht-lksg
description: Erfüllung der Dokumentationspflicht (§ 10 LkSG) und Berichtspflicht (§ 12 LkSG) sowie Vorbereitung auf die BAFA-Kontrolle und Anordnungen (§§ 14, 15 LkSG) und das Bußgeldrisiko (§ 24 LkSG), mit Ausblick auf die CSDDD-Schnittstelle. Use when ein Unternehmen seine Dokumentation/Berichterstattung an die BAFA aufsetzt oder sich auf eine behördliche Kontrolle oder ein Bußgeldverfahren vorbereitet.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/lieferkettengesetz/skills/bafa-bericht-lksg
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: regulatory
language: de
---

# /lieferkettengesetz:bafa-bericht-lksg

## Zweck

Diese Skill bündelt die **Nachweis- und Durchsetzungsebene** des LkSG: die interne **Dokumentationspflicht** (**§ 10 LkSG**), die **Berichtspflicht** gegenüber dem BAFA (**§ 12 LkSG**), die behördliche Kontrolle und **Anordnungen** (**§§ 14, 15 LkSG**) sowie das **Bußgeld** (**§ 24 LkSG**). Sie ordnet die Pflichten dem aktuellen Rechtsstand zu und bereitet auf eine **BAFA**-Kontrolle vor.

> **⚠️ Aktualität (Stand 2026-07) — Berichtseinreichung faktisch eingestellt:** Das **BAFA** hat die Prüfung von Unternehmensberichten nach **§§ 12, 13 LkSG mit Wirkung zum 03.09.2025 vollständig eingestellt**; die Einreichung über den dafür vorgesehenen BAFA-Zugang **ist nicht mehr möglich**. Grundlage ist ein **Kabinettsbeschluss vom 03.09.2025 nebst Weisung an das BAFA**, mit der die Bundesregierung nach eigener Formulierung „der Gesetzesnovelle vorgreift".
>
> **Wichtige Abgrenzung:** Es handelt sich um eine **exekutive Weisung, nicht um eine Gesetzesaufhebung**. Die §§ 12, 13 LkSG stehen formal weiter im Gesetz; sie werden lediglich nicht mehr vollzogen und können mangels Einreichungsweg auch nicht erfüllt werden. Die geplante Novelle (Streichung, teils rückwirkend diskutiert) war zum Stand 07/2026 **nicht als verkündetes Gesetz nachweisbar** — Inkrafttretensstand `[unverifiziert - prüfen]`.
>
> **Unverändert fortbestehend:** Risikoanalyse (§ 5), Präventions- und Abhilfemaßnahmen (§§ 6, 7), **Beschwerdeverfahren** (§ 8), interne **Dokumentation** (§ 10) sowie die behördliche **Kontrolle** und **Anordnungsbefugnis** (§§ 14, 15). Ordnungswidrigkeiten sollen künftig auf besonders schwere Verstöße konzentriert werden.
>
> **Ablösung:** Das LkSG wird durch die **CSDDD**-Umsetzung abgelöst — Umsetzungsfrist **26.07.2028**, materielle Pflichten ab **26.07.2029** (Fassung nach Omnibus I). Mandanten sollten die bestehenden LkSG-Kontrollen bereits jetzt auf Art. 8–11 CSDDD mappen.

## Eingaben

- Risikoanalyse, Präventions-/Abhilfemaßnahmen, Beschwerdeverfahren (Vorgewerke)
- Bisherige Dokumentation und (frühere) BAFA-Berichte
- Anfragen/Auskunftsersuchen oder Anordnungen des BAFA
- Umsatzkennzahlen (für Bußgeldbemessung § 24 Abs. 3 LkSG)

## Sub-Agent-Architektur

Ein **Dokumentations-Agent** stellt die fortlaufende interne Dokumentation nach § 10 Abs. 1 LkSG zusammen (Risikoanalyse, Maßnahmen, Wirksamkeitsprüfungen, Beschwerden) und sichert die siebenjährige Aufbewahrung. Ein **Berichts-Agent** prüft, ob und in welcher Form eine **Berichtspflicht** nach § 12 LkSG noch besteht (Novelle beachten). Ein **Aufsichts-Agent** bereitet auf die **BAFA**-Kontrolle nach §§ 14, 15 LkSG vor und prüft Auskunfts-, Duldungs- und Mitwirkungspflichten. Ein **Sanktions-Agent** bewertet das **Bußgeld**risiko nach § 24 LkSG und die CSDDD-Schnittstelle und markiert Unsicheres mit `[unverifiziert - prüfen]`.

## Ablauf

### 1. Dokumentationspflicht (§ 10 Abs. 1 LkSG)

- Fortlaufende, interne **Dokumentationspflicht** über die Erfüllung der Sorgfaltspflichten.
- Inhalt: Risikoanalyse, Grundsatzerklärung, Präventions-/Abhilfemaßnahmen, Beschwerdeverfahren, Wirksamkeitsprüfungen.
- Aufbewahrung **mindestens sieben Jahre**.

### 2. Berichtspflicht (§ 12 LkSG)

- Ursprünglich: jährlicher Bericht über die Erfüllung der Sorgfaltspflichten, Veröffentlichung und Einreichung beim **BAFA** binnen vier Monaten nach Schluss des Geschäftsjahres.
- **Aktuell (ab 03.09.2025):** Das BAFA **prüft keine Berichte mehr und nimmt keine entgegen**; der Einreichungszugang ist geschlossen. Eine Einreichung ist damit weder möglich noch gefordert.
- **Beratungsfolge:** Mandanten ist **nicht** zu einer Einreichung zu raten. Empfohlen wird stattdessen, den Berichtsinhalt als **interne Dokumentation nach § 10 LkSG** vorzuhalten — erstens weil § 10 fortgilt, zweitens weil die CSDDD-Berichtslinie darauf aufsetzt. Ein bereits erstellter Bericht ist nicht wertlos, sondern wird zur Dokumentationsgrundlage.
- **Nicht als Aufhebung darstellen:** Solange die Novelle nicht verkündet ist, bleibt die Norm formal bestehen. Gegenüber Mandanten ist zwischen *nicht vollzogen* und *aufgehoben* zu unterscheiden `[unverifiziert - prüfen]`.

### 3. Behördliche Kontrolle (§ 14 LkSG)

- Das **BAFA** wird von Amts wegen oder auf Antrag tätig (**§ 14 LkSG**).
- Auskunftsersuchen, Betretensrechte, Herausgabe von Unterlagen; Duldungs- und Mitwirkungspflichten des Unternehmens.

### 4. Anordnungen und Maßnahmen (§ 15 LkSG)

- Das BAFA kann **Anordnungen** und Maßnahmen treffen, um Verstöße festzustellen, zu beseitigen und zu verhindern (**§ 15 LkSG**).
- Unternehmen muss angemessene Maßnahmen vorlegen; Durchsetzung ggf. mit Zwangsgeld (§ 23 LkSG).

### 5. Bußgeld (§ 24 LkSG)

- **§ 24 LkSG** sanktioniert Pflichtverletzungen mit **Bußgeld** bis **800.000 EUR** (z. B. unterlassene Abhilfemaßnahme), gestaffelt bis **500.000 EUR** und **100.000 EUR**.
- Bei durchschnittlichem Jahresumsatz **> 400 Mio. EUR** Geldbuße bis **2 % des weltweiten durchschnittlichen Jahresumsatzes** (§ 24 Abs. 3 LkSG) — beschränkt auf bestimmte Abhilfeverstöße.
- Nebenfolge: möglicher Ausschluss von der Vergabe öffentlicher Aufträge (§ 22 LkSG).

### 6. CSDDD-Schnittstelle

- Die **CSDDD** (Richtlinie (EU) 2024/1760) wird das LkSG ablösen/überlagern (zivilrechtliche Haftung, Klimaplan, breitere Wertschöpfungskette).
- **Stand nach Omnibus I** (Änderungs-RL (EU) 2026/470, in Kraft 18.03.2026): Anwendungsschwelle auf **> 5.000 Beschäftigte UND > 1,5 Mrd. EUR Nettoumsatz** angehoben; **Umsetzungsfrist 26.07.2028**, materielle Sorgfaltspflichten ab **26.07.2029**.
- **Praxisfolge:** Ein großer Teil der bisher adressierten Unternehmen fällt aus dem CSDDD-Anwendungsbereich heraus. Die Schwellenprüfung ist daher **neu durchzuführen** — die alte LkSG-Schwelle (1.000 Beschäftigte) sagt über die CSDDD-Betroffenheit nichts aus.
- Mapping der bestehenden LkSG-Kontrollen auf **Art. 8–11 CSDDD** empfohlen `[unverifiziert - prüfen]`.

## Risiken / typische Fehler

- **Bußgeld unterschätzt** — das **Bußgeld** nach § 24 LkSG kann umsatzbezogen (2 %) ausfallen; Abhilfeverstöße wiegen schwer.
- **Berichtspflicht falsch eingeschätzt** — Bericht nach altem Stand eingereicht oder versäumt, obwohl die Pflicht durch die Novelle gestrichen wird; Stand `[unverifiziert - prüfen]`.
- **BAFA-Kontrolle unvorbereitet** — Mitwirkungs- und Auskunftspflichten gegenüber dem **BAFA** unterschätzt; Anordnungen nach §§ 14, 15 LkSG nicht fristgerecht befolgt.
- **Dokumentation lückenhaft** — die Dokumentation ist beweispflichtig; Lücken gehen zu Lasten des Unternehmens.
- **CSDDD-Vorbereitung versäumt** — die **CSDDD** verschärft Pflichten und Haftung; späte Datenbasis ist riskant.
- **Aufbewahrungsfrist verkürzt** — Sieben-Jahres-Frist nicht eingehalten.

## Quellen

### Statute

- [LkSG](https://www.gesetze-im-internet.de/lksg/) — Volltext
- [§ 10 LkSG](https://www.gesetze-im-internet.de/lksg/__10.html), [§ 12 LkSG](https://www.gesetze-im-internet.de/lksg/__12.html), [§ 14 LkSG](https://www.gesetze-im-internet.de/lksg/__14.html), [§ 15 LkSG](https://www.gesetze-im-internet.de/lksg/__15.html), [§ 24 LkSG](https://www.gesetze-im-internet.de/lksg/__24.html)
- [Richtlinie (EU) 2024/1760 (CSDDD)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024L1760) · Änderungs-RL (EU) 2026/470 (Omnibus I) `[unverifiziert - prüfen]`

### BAFA

- [BAFA – Lieferkettengesetz](https://www.bafa.de/DE/Lieferketten/ueberblick_node.html) — Kontrolle, Anordnungen, Bußgeldverfahren

## Ausgabeformat

```
BAFA-DOKUMENTATION & DURCHSETZUNG (LkSG) — <Unternehmen> — <Datum>

I.    Dokumentation (§ 10 LkSG)
      Inhalt / Aufbewahrung 7 Jahre: <…>
II.   Berichtspflicht (§ 12 LkSG)
      Status: [gestrichen lt. Novelle / zu prüfen]  ([unverifiziert - prüfen])
III.  Behördliche Kontrolle (§ 14 LkSG)
      Auskunfts-/Mitwirkungspflichten: <…>
IV.   Anordnungen (§ 15 LkSG)
      Vorliegende Anordnung / Reaktion: <…>
V.    Bußgeldrisiko (§ 24 LkSG)
      Tatbestand | Rahmen (800k/500k/100k/2 %): <…>
      Vergabeausschluss (§ 22 LkSG): <…>
VI.   CSDDD-Ausblick
      <… [unverifiziert - prüfen]>

Restrisiko: <…>
Wiedervorlage: jährlich + bei BAFA-Anfrage
```
