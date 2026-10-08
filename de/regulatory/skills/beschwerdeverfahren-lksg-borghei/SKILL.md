---
name: beschwerdeverfahren-lksg-borghei
title: /lieferkettengesetz:beschwerdeverfahren-lksg
description: Einrichtung und Wirksamkeitsprüfung des Beschwerdeverfahrens nach § 8 LkSG – Verfahrensordnung, Zugänglichkeit, Vertraulichkeit und Schutz vor Benachteiligung sowie der anlassbezogene Bezug zu mittelbaren Zulieferern (§ 9 LkSG). Use when ein Beschwerdeverfahren aufgesetzt, überarbeitet oder auf seine Wirksamkeit geprüft werden soll.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/lieferkettengesetz/skills/beschwerdeverfahren-lksg
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: regulatory
language: de
---

# /lieferkettengesetz:beschwerdeverfahren-lksg

## Zweck

Das **Beschwerdeverfahren** (**§ 8 LkSG**) ist das Frühwarnsystem der Lieferkette: Es macht Risiken und Verletzungen sichtbar, die die Risikoanalyse nicht erfasst hat. Diese Skill richtet ein wirksames Verfahren ein und prüft es gegen die gesetzlichen **Wirksamkeitskriterien**. Eingehende Beschwerden über **mittelbare Zulieferer** begründen regelmäßig die „substantiierte Kenntnis" i. S. v. **§ 9 LkSG** und lösen vertiefte Prüfpflichten aus.

> **⚠️ Aktualität (Stand 2026-07) — § 8 LkSG gilt unverändert fort:** Das **BAFA** hat die Prüfung von Unternehmensberichten nach **§§ 12, 13 LkSG mit Wirkung zum 03.09.2025 vollständig eingestellt**; der Einreichungszugang **ist geschlossen**. Grundlage ist ein **Kabinettsbeschluss vom 03.09.2025 nebst Weisung an das BAFA**, mit der die Bundesregierung nach eigener Formulierung „der Gesetzesnovelle vorgreift".
>
> **Wichtige Abgrenzung:** Es handelt sich um eine **exekutive Weisung, nicht um eine Gesetzesaufhebung**. Die §§ 12, 13 LkSG stehen formal weiter im Gesetz; sie werden lediglich nicht mehr vollzogen und können mangels Einreichungsweg auch nicht erfüllt werden. Die geplante Novelle war zum Stand 07/2026 **nicht als verkündetes Gesetz nachweisbar** — Inkrafttretensstand `[unverifiziert - prüfen]`.
>
> **Für diese Skill entscheidend:** Das **Beschwerdeverfahren nach § 8 LkSG** ist von alledem **nicht betroffen** und muss weiterhin eingerichtet, öffentlich zugänglich gemacht und **mindestens jährlich** auf seine Wirksamkeit überprüft werden — ebenso wie Risikoanalyse (§ 5), Präventions-/Abhilfemaßnahmen (§§ 6, 7), interne **Dokumentation (§ 10)** sowie die behördliche **Kontrolle und Anordnungsbefugnis (§§ 14, 15)**. Der Wegfall der Berichtseinreichung nimmt dem Verfahren lediglich seinen bisherigen Veröffentlichungsanlass; die Wirksamkeitsprüfung und ihre Dokumentation sind deshalb **umso sorgfältiger intern** zu führen, weil sie im Kontrollverfahren der einzige Nachweis sind. Ordnungswidrigkeiten sollen künftig auf besonders schwere Verstöße konzentriert werden.
>
> **Fortbestehende eigenständige Kanalpflicht:** Das **HinSchG** ist vom LkSG-Berichtsstopp ohnehin nicht berührt; die dortigen Melde- und Fristenpflichten gelten unabhängig.
>
> **CSDDD-Ausblick:** Nach **Omnibus I** (Änderungs-RL (EU) 2026/470, in Kraft 18.03.2026) liegt die CSDDD-Schwelle bei **> 5.000 Beschäftigten UND > 1,5 Mrd. EUR Nettoumsatz**; Umsetzungsfrist **26.07.2028**, materielle Pflichten ab **26.07.2029**. Die alte Phasierung (6.000 / 900 Mio. EUR, 2027/2028) ist überholt; die meisten LkSG-pflichtigen Mandanten sind **nicht** CSDDD-betroffen. Ein Ausbau des Beschwerdeverfahrens auf CSDDD-Niveau lohnt nur nach positiver Schwellenprüfung `[unverifiziert - prüfen]`.

## Eingaben

- Bestehendes Hinweisgeber-/Beschwerdesystem (Schnittstelle HinSchG)
- Stakeholder-/Zuliefererstruktur, betroffene Sprachen und Regionen
- Risikoanalyse (priorisierte Risiken als Beschwerde-Schwerpunkte)
- Bisher eingegangene Beschwerden und ihre Bearbeitung

## Sub-Agent-Architektur

Ein **Design-Agent** entwirft die **Verfahrensordnung** und die Zugangswege (Kanäle, Sprachen, Niedrigschwelligkeit). Ein **Wirksamkeits-Agent** prüft das Verfahren gegen die Kriterien des § 8 LkSG (Zugänglichkeit, Vertraulichkeit, Schutz vor Benachteiligung, Unparteilichkeit). Ein **Eskalations-Agent** verknüpft eingehende Beschwerden mit der Risikoanalyse und prüft, ob eine Beschwerde substantiierte Kenntnis nach **§ 9 LkSG** auslöst. Ein **Dokumentations-Agent** sichert die Nachweise für die BAFA-Berichterstattung (§ 10 LkSG) und markiert offene Punkte mit `[unverifiziert - prüfen]`.

## Ablauf

### 1. Pflicht und Reichweite (§ 8 Abs. 1 LkSG)

- Einrichtung eines internen oder Beteiligung an einem externen **Beschwerdeverfahren**.
- Erfasst Hinweise auf menschenrechtliche/umweltbezogene Risiken und Pflichtverletzungen im **eigenen Geschäftsbereich** und entlang der **gesamten Lieferkette** (auch mittelbare Zulieferer).

### 2. Verfahrensordnung (§ 8 Abs. 2 LkSG)

- Schriftliche, öffentlich zugängliche **Verfahrensordnung** in verständlicher Sprache.
- Klarheit über Zuständigkeit, Ablauf, Fristen und Rückmeldung an die hinweisgebende Person.

### 3. Wirksamkeitskriterien (§ 8 Abs. 3, 4 LkSG)

Das Verfahren muss wirksam sein. Maßgebliche Kriterien:

- **Zugänglichkeit** — niedrigschwellig, in relevanten Sprachen, für potenziell Betroffene erreichbar.
- **Vertraulichkeit** — Wahrung der Identität, Schutz der Daten.
- **Schutz vor Benachteiligung/Bestrafung** wegen einer Beschwerde.
- **Unparteilichkeit** — die mit dem Verfahren betrauten Personen handeln unabhängig, sind nicht weisungsgebunden und zur Verschwiegenheit verpflichtet.

### 4. Bearbeitung und Abhilfe

- Eingangsbestätigung, Sachverhaltsaufklärung, Erörterung mit der hinweisgebenden Person.
- Verknüpfung mit Präventions-/Abhilfemaßnahmen (§§ 6, 7 LkSG).

### 5. Bezug zu mittelbaren Zulieferern (§ 9 LkSG)

- Eine substantiierte Beschwerde über einen **mittelbaren Zulieferer** begründet „substantiierte Kenntnis" nach **§ 9 Abs. 3 LkSG**.
- Folge: anlassbezogene Risikoanalyse, Präventionsmaßnahmen gegenüber dem Verursacher, ggf. Aktualisierung des Beschwerdeverfahrens.

### 6. Wirksamkeitsprüfung und Dokumentation

- Überprüfung der **Wirksamkeit** mindestens **jährlich** und anlassbezogen (§ 8 Abs. 5 i. V. m. § 4 Abs. 4 LkSG) — **unverändert fortbestehend**.
- Dokumentation nach **§ 10 LkSG** für die **interne** Nachweisführung, Aufbewahrung sieben Jahre.
- **Kein BAFA-Bericht mehr:** Die Berichterstattung nach §§ 12, 13 LkSG wird seit **03.09.2025** nicht mehr vollzogen, der Einreichungszugang ist geschlossen. Der Nachweis der Wirksamkeitsprüfung erfolgt daher ausschließlich intern und wird im Kontrollverfahren nach **§§ 14, 15 LkSG** auf Anforderung vorgelegt. Da kein veröffentlichter Bericht mehr als Nachweisrahmen dient, ist die Prüfungsdokumentation eigenständig prüfungsfest aufzubauen (Datum, Methodik, Prüfkriterien je § 8 Abs. 3, 4 LkSG, Befund, abgeleitete Maßnahmen).
- **Öffentliche Zugänglichkeit der Verfahrensordnung** (§ 8 Abs. 2 LkSG) bleibt davon unberührt: Sie folgt aus § 8, nicht aus der Berichtspflicht, und ist weiterhin zu gewährleisten.

## Risiken / typische Fehler

- **Wirksamkeit nur behauptet** — die **Wirksamkeit** des Verfahrens ist nicht anhand der gesetzlichen Kriterien belegt; **BAFA** verlangt einen belastbaren Nachweis.
- **Zugänglichkeit zu hoch** — Verfahren nur intern/deutschsprachig; potenziell betroffene Beschäftigte bei **mittelbare Zulieferer** im Ausland erreichen es nicht.
- **Vertraulichkeit unzureichend** — fehlender Schutz vor Benachteiligung untergräbt die **Vertraulichkeit** und schreckt Hinweisgeber ab.
- **Substantiierte Kenntnis verkannt** — eingehende Beschwerde nicht als Auslöser des § 9 LkSG behandelt.
- **Keine Verzahnung mit HinSchG** — Doppelstrukturen statt eines integrierten Kanals.
- **Keine jährliche Überprüfung** — Wirksamkeitskontrolle unterbleibt.
- **Mandant plant gegen aufgehobenes Recht** — Beschwerdeverfahren wird abgeschaltet oder nicht mehr gepflegt, weil „das LkSG abgeschafft" sei. Eingestellt ist allein die **Berichtsprüfung nach §§ 12, 13 LkSG** (03.09.2025). **§ 8 LkSG gilt unverändert fort**, ebenso §§ 5, 6, 7, 10, 14, 15. Ein abgeschaltetes Verfahren ist eine fortbestehende Pflichtverletzung.
- **„Nicht vollzogen" mit „aufgehoben" verwechselt** — Grundlage des Berichtsstopps ist eine **exekutive Weisung**, keine Gesetzesaufhebung; §§ 12, 13 LkSG stehen formal weiter im Gesetz. Die Novelle war zum Stand 07/2026 nicht als verkündetes Gesetz nachweisbar `[unverifiziert - prüfen]`.
- **Wirksamkeitsprüfung nur „für den Bericht" geführt** — ohne veröffentlichten Bericht fehlt der Nachweis vollständig. Die Prüfungsdokumentation nach § 10 LkSG ist eigenständig prüfungsfest aufzubauen; sie ist im Verfahren nach §§ 14, 15 LkSG der einzige Beleg.
- **Verfahrensordnung nicht mehr veröffentlicht** — die öffentliche Zugänglichkeit folgt aus § 8 Abs. 2 LkSG, nicht aus der Berichtspflicht, und besteht fort.
- **Auf CSDDD-Niveau ausgebaut ohne Betroffenheit** — die CSDDD-Schwelle liegt nach Omnibus I bei **> 5.000 Beschäftigten UND > 1,5 Mrd. EUR**, materielle Pflichten erst ab **26.07.2029**; die meisten LkSG-Pflichtigen sind nicht erfasst.

## Quellen

### Statute

- [LkSG](https://www.gesetze-im-internet.de/lksg/) — Volltext
- [§ 8 LkSG](https://www.gesetze-im-internet.de/lksg/__8.html), [§ 9 LkSG](https://www.gesetze-im-internet.de/lksg/__9.html), [§ 3 LkSG](https://www.gesetze-im-internet.de/lksg/__3.html), [§ 10 LkSG](https://www.gesetze-im-internet.de/lksg/__10.html), [§ 24 LkSG](https://www.gesetze-im-internet.de/lksg/__24.html)
- [§ 14 LkSG](https://www.gesetze-im-internet.de/lksg/__14.html), [§ 15 LkSG](https://www.gesetze-im-internet.de/lksg/__15.html) — behördliche Kontrolle und Anordnungen, unverändert in Kraft
- [§ 12 LkSG](https://www.gesetze-im-internet.de/lksg/__12.html), [§ 13 LkSG](https://www.gesetze-im-internet.de/lksg/__13.html) — formal in Kraft, seit **03.09.2025 nicht mehr vollzogen**; Einreichungszugang geschlossen `[unverifiziert - prüfen]`
- [HinSchG](https://www.gesetze-im-internet.de/hinschg/) — Schnittstelle Hinweisgeberschutz, vom LkSG-Berichtsstopp nicht berührt
- [Richtlinie (EU) 2024/1760 (CSDDD)](https://eur-lex.europa.eu/eli/dir/2024/1760/oj) · **Änderungs-RL (EU) 2026/470 (Omnibus I)**, Amtsblatt 26.02.2026, in Kraft 18.03.2026 — Schwelle > 5.000 Beschäftigte und > 1,5 Mrd. EUR, materielle Pflichten ab 26.07.2029; ELI-Fundstelle `[unverifiziert - prüfen]`

### BAFA / Sekundärliteratur

- [BAFA – Lieferkettengesetz](https://www.bafa.de/DE/Lieferketten/ueberblick_node.html) — Handreichung Beschwerdeverfahren; **Berichtsprüfung nach §§ 12, 13 LkSG zum 03.09.2025 eingestellt, Einreichungsportal geschlossen**
- Grabosch, LkSG, 1. Aufl. 2023

## Ausgabeformat

```
BESCHWERDEVERFAHREN (LkSG) — <Unternehmen> — <Datum>

I.    Reichweite (§ 8 LkSG)
      Erfasste Risiken / Lieferkette: <…>
II.   Verfahrensordnung
      Kanäle / Sprachen / Zuständigkeit / Fristen: <…>
III.  Wirksamkeitskriterien
      Zugänglichkeit | Vertraulichkeit | Schutz vor Benachteiligung | Unparteilichkeit
IV.   Bearbeitungsprozess
      Eingang → Aufklärung → Abhilfe (§§ 6, 7 LkSG): <…>
V.    Bezug mittelbare Zulieferer (§ 9 LkSG)
      Substantiierte Kenntnis ausgelöst? [Ja/Nein]
VI.   Wirksamkeitsprüfung & Dokumentation (§ 10 LkSG) — intern, 7 Jahre
      Datum / Methodik / Kriterien § 8 Abs. 3, 4 / Befund / Maßnahmen: <…>
      Hinweis: KEINE BAFA-Einreichung — §§ 12, 13 LkSG seit 03.09.2025
      nicht mehr vollzogen, Zugang geschlossen ([unverifiziert - prüfen])
      Vorbereitung auf BAFA-Kontrolle §§ 14, 15 LkSG: <…>
VII.  CSDDD-Schwellenprüfung (RL (EU) 2026/470)
      > 5.000 Beschäftigte? [Ja/Nein]  > 1,5 Mrd. EUR? [Ja/Nein]
      Kumulativ erfüllt: [Ja/Nein] — materielle Pflichten ab 26.07.2029

Restrisiko: <…>
Wiedervorlage: jährlich + anlassbezogen
```
