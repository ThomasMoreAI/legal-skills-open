---
name: praeventions-abhilfemassnahmen-borghei
title: /lieferkettengesetz:praeventions-abhilfemassnahmen
description: Ableitung und Priorisierung angemessener Präventionsmaßnahmen (§ 6 LkSG) und Abhilfemaßnahmen (§ 7 LkSG) im eigenen Geschäftsbereich und bei unmittelbaren Zulieferern, ausgehend von der Risikoanalyse (§ 5 LkSG) und dem Angemessenheitsmaßstab (§ 3 LkSG). Use when nach einer Risikoanalyse konkrete Präventions- oder Abhilfemaßnahmen festzulegen oder ein eingetretener Verstoß abzustellen ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/lieferkettengesetz/skills/praeventions-abhilfemassnahmen
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: regulatory
language: de
---

# /lieferkettengesetz:praeventions-abhilfemassnahmen

## Zweck

Nach der Risikoanalyse verlangt das LkSG **Handeln**: angemessene **Präventionsmaßnahmen** (**§ 6 LkSG**) zur Verhinderung von Risiken und **Abhilfemaßnahmen** (**§ 7 LkSG**) bei bereits eingetretenen oder unmittelbar bevorstehenden Verletzungen. Maßstab ist stets die **Angemessenheit** (**§ 3 LkSG**). Diese Skill leitet aus den priorisierten Risiken die richtigen Maßnahmen ab, ordnet sie der zutreffenden Stufe (eigener Geschäftsbereich / unmittelbarer Zulieferer) zu und dokumentiert ihre Wirksamkeit.

> **⚠️ Aktualität (Stand 2026-07) — §§ 6, 7 LkSG gelten unverändert fort:** Das **BAFA** hat die Prüfung von Unternehmensberichten nach **§§ 12, 13 LkSG mit Wirkung zum 03.09.2025 vollständig eingestellt**; der Einreichungszugang **ist geschlossen**. Grundlage ist ein **Kabinettsbeschluss vom 03.09.2025 nebst Weisung an das BAFA**, mit der die Bundesregierung nach eigener Formulierung „der Gesetzesnovelle vorgreift".
>
> **Wichtige Abgrenzung:** Es handelt sich um eine **exekutive Weisung, nicht um eine Gesetzesaufhebung**. Die §§ 12, 13 LkSG stehen formal weiter im Gesetz; sie werden lediglich nicht mehr vollzogen und können mangels Einreichungsweg auch nicht erfüllt werden. Die geplante Novelle war zum Stand 07/2026 **nicht als verkündetes Gesetz nachweisbar** — Inkrafttretensstand `[unverifiziert - prüfen]`.
>
> **Für diese Skill entscheidend:** **Präventions- und Abhilfemaßnahmen nach §§ 6, 7 LkSG bestehen unverändert fort** — ebenso Risikoanalyse (§ 5), Beschwerdeverfahren (§ 8), interne **Dokumentation (§ 10)** sowie die behördliche **Kontrolle und Anordnungsbefugnis (§§ 14, 15)**. Der Wegfall der Berichtseinreichung entlastet **nicht** von der Handlungspflicht; er verlagert den Nachweis lediglich vollständig in die interne Dokumentation, die das BAFA im Kontrollverfahren anfordern kann. Ordnungswidrigkeiten sollen künftig auf besonders schwere Verstöße konzentriert werden — die Abhilfeverstöße nach § 24 Abs. 1 Nr. 6, Nr. 7 lit. a LkSG gehören gerade dazu.
>
> **CSDDD-Ausblick:** Nach **Omnibus I** (Änderungs-RL (EU) 2026/470, in Kraft 18.03.2026) liegt die CSDDD-Schwelle bei **> 5.000 Beschäftigten UND > 1,5 Mrd. EUR Nettoumsatz**; Umsetzungsfrist **26.07.2028**, materielle Pflichten ab **26.07.2029**. Die alte Phasierung (6.000 / 900 Mio. EUR, 2027/2028) ist überholt. Für die meisten LkSG-pflichtigen Mandanten bedeutet das: **keine** CSDDD-Betroffenheit — die Maßnahmenarchitektur ist auf das LkSG auszurichten, nicht vorsorglich auf die CSDDD hochzuskalieren. Ein Mapping auf **Art. 8–11 CSDDD** lohnt nur bei positiver Schwellenprüfung `[unverifiziert - prüfen]`.

## Eingaben

- Ergebnis der Risikoanalyse nach § 5 LkSG (priorisierte Risiken)
- Grundsatzerklärung zur Menschenrechtsstrategie (falls vorhanden)
- Betroffene Standorte / unmittelbare Zulieferer
- Bestehende Verträge, Einkaufspraktiken, Audit-Ergebnisse
- Eingegangene Beschwerden / Hinweise (Schnittstelle § 8 LkSG)

## Sub-Agent-Architektur

Ein **Strategie-Agent** überführt die priorisierten Risiken in die **Grundsatzerklärung** und leitet die menschenrechts- und umweltbezogenen Erwartungen an Beschäftigte und Zulieferer ab. Ein **Präventions-Agent** entwirft Maßnahmen je Stufe (eigener Geschäftsbereich, unmittelbarer Zulieferer): Beschaffungsstrategie, vertragliche Zusicherungen, Schulungen, risikobasierte Kontrollen. Ein **Abhilfe-Agent** prüft bei eingetretenen Verletzungen den Maßnahmenpfad nach § 7 LkSG und unterscheidet inländischen eigenen Geschäftsbereich (zwingende Beendigung) von Zulieferer-Konstellationen (Minimierungs-/Beendigungskonzept). Ein **Angemessenheits-Agent** wägt jede Maßnahme gegen die Kriterien des § 3 LkSG ab und markiert offene Punkte mit `[unverifiziert - prüfen]`.

## Ablauf

### 1. Angemessenheitsmaßstab (§ 3 LkSG)

Die **Angemessenheit** richtet sich nach: Art und Umfang der Geschäftstätigkeit, Einflussvermögen, typischerweise zu erwartender Schwere und Umkehrbarkeit der Verletzung, Wahrscheinlichkeit und Art des Verursachungsbeitrags.

### 2. Präventionsmaßnahmen im eigenen Geschäftsbereich (§ 6 Abs. 1, 3 LkSG)

- Abgabe einer **Grundsatzerklärung** zur Menschenrechtsstrategie durch die Unternehmensleitung (§ 6 Abs. 2 LkSG).
- Umsetzung der Strategie in den relevanten Geschäftsabläufen.
- Geeignete Beschaffungsstrategien und Einkaufspraktiken.
- Schulungen und risikobasierte Kontrollmaßnahmen.

### 3. Präventionsmaßnahmen beim unmittelbaren Zulieferer (§ 6 Abs. 4 LkSG)

Beim **unmittelbaren Zulieferer**:

- Berücksichtigung menschenrechtsbezogener Erwartungen bei der Auswahl,
- vertragliche Zusicherung der Einhaltung und deren Weitergabe in der Kette,
- Vereinbarung von Kontrollmechanismen (Audits) und deren Durchführung.

### 4. Abhilfemaßnahmen (§ 7 LkSG)

- Bei eingetretener oder unmittelbar bevorstehender Verletzung: **unverzüglich** angemessene **Abhilfemaßnahmen**.
- **Eigener Geschäftsbereich im Inland:** Maßnahmen müssen zur **Beendigung** der Verletzung führen.
- **Unmittelbarer Zulieferer:** wenn Beendigung kurzfristig nicht möglich — Konzept mit Zeitplan zur Beendigung/Minimierung; ultima ratio Abbruch der Geschäftsbeziehung (§ 7 Abs. 3 LkSG) nur bei schwerwiegenden Verstößen und erfolglosen Maßnahmen.

### 5. Priorisierung und Wirksamkeitskontrolle

- **Priorisierung** der Maßnahmen nach Angemessenheit und Einflussvermögen.
- Wirksamkeit der Präventions- und Abhilfemaßnahmen **mindestens jährlich** und anlassbezogen überprüfen (§ 6 Abs. 5, § 7 Abs. 4 LkSG).

### 6. Dokumentation

- Maßnahmen, Begründung der Angemessenheit und Wirksamkeitsprüfung dokumentieren (**§ 10 LkSG**, Aufbewahrung sieben Jahre).
- **Kein BAFA-Bericht mehr:** Die Berichtspflicht nach §§ 12, 13 LkSG wird seit **03.09.2025** nicht mehr vollzogen, der Einreichungszugang ist geschlossen. Der Nachweis der Maßnahmen erfolgt daher **ausschließlich intern** nach § 10 LkSG — und wird im Kontrollverfahren nach **§§ 14, 15 LkSG** auf Anforderung des BAFA vorgelegt. Die Dokumentationsanforderungen sinken dadurch **nicht**, sie steigen faktisch, weil kein veröffentlichter Bericht mehr als Nachweisrahmen dient.
- **Vertragliche Zusicherungen und Datenanfragen begrenzen:** Nach Omnibus I dürfen kleinere Geschäftspartner Datenanfragen zurückweisen, die die gesetzliche Obergrenze überschreiten (Wertschöpfungsketten-Cap). Lieferantenfragebögen, Self-Assessments und Auditumfänge sind entsprechend zu dimensionieren; überzogene Anfragen sind nicht durchsetzbar.

## Risiken / typische Fehler

- **Angemessenheit nicht begründet** — Maßnahme ohne nachvollziehbare Abwägung der **Angemessenheit** nach § 3 LkSG; in einem BAFA-Verfahren angreifbar.
- **Stufe verwechselt** — Maßnahmen gegen mittelbare Zulieferer statt gegen den **unmittelbarer Zulieferer**; § 6 erfasst primär den eigenen Geschäftsbereich und unmittelbare Zulieferer.
- **Abhilfemaßnahmen verspätet** — **Abhilfemaßnahmen** nicht unverzüglich oder im Inland ohne Beendigungswirkung ergriffen.
- **Vorschneller Abbruch** — Geschäftsbeziehung abgebrochen, statt zunächst ein Beendigungskonzept zu versuchen (Abbruch ist ultima ratio).
- **Wirksamkeit nicht geprüft** — keine jährliche/anlassbezogene Überprüfung; **BAFA** verlangt belastbaren Nachweis.
- **Grundsatzerklärung fehlt** — keine von der Leitung verabschiedete Menschenrechtsstrategie.
- **Mandant plant gegen aufgehobenes Recht** — Maßnahmenprogramm wird ausgesetzt oder zurückgefahren, weil „das LkSG abgeschafft" sei. Eingestellt ist allein die **Berichtsprüfung nach §§ 12, 13 LkSG** (03.09.2025). **§§ 6 und 7 LkSG gelten unverändert fort**, ebenso §§ 5, 8, 10, 14, 15. Wer Präventions- und Abhilfemaßnahmen einstellt, verletzt fortbestehende Pflichten mit dem höchsten Bußgeldrisiko (§ 24 Abs. 1 Nr. 6, Nr. 7 lit. a LkSG, bis 2 % des weltweiten Jahresumsatzes).
- **„Nicht vollzogen" mit „aufgehoben" verwechselt** — Grundlage des Berichtsstopps ist eine **exekutive Weisung**, keine Gesetzesaufhebung; §§ 12, 13 LkSG stehen formal weiter im Gesetz. Die Novelle war zum Stand 07/2026 nicht als verkündetes Gesetz nachweisbar `[unverifiziert - prüfen]`.
- **Nachweis am BAFA-Bericht ausgerichtet** — Maßnahmen werden „berichtsfähig" statt prüfungsfest dokumentiert. Ohne veröffentlichten Bericht ist allein die **Dokumentation nach § 10 LkSG** der Nachweis im Kontrollverfahren nach §§ 14, 15 LkSG.
- **Vorsorglich auf CSDDD-Niveau hochskaliert** — die CSDDD-Schwelle liegt nach Omnibus I bei **> 5.000 Beschäftigten UND > 1,5 Mrd. EUR**, materielle Pflichten erst ab **26.07.2029**. Die meisten LkSG-pflichtigen Unternehmen sind **nicht** betroffen; ein CSDDD-Programm ohne positive Schwellenprüfung erzeugt Kosten ohne Rechtsgrund.
- **Datenanfragen über den Wertschöpfungsketten-Cap hinaus** — kleinere Zulieferer dürfen überzogene Anfragen zurückweisen; darauf gestützte Präventionskonzepte sind nicht durchsetzbar.

## Quellen

### Statute

- [LkSG](https://www.gesetze-im-internet.de/lksg/) — Volltext
- [§ 3 LkSG](https://www.gesetze-im-internet.de/lksg/__3.html), [§ 5 LkSG](https://www.gesetze-im-internet.de/lksg/__5.html), [§ 6 LkSG](https://www.gesetze-im-internet.de/lksg/__6.html), [§ 7 LkSG](https://www.gesetze-im-internet.de/lksg/__7.html), [§ 10 LkSG](https://www.gesetze-im-internet.de/lksg/__10.html), [§ 24 LkSG](https://www.gesetze-im-internet.de/lksg/__24.html)
- [§ 14 LkSG](https://www.gesetze-im-internet.de/lksg/__14.html), [§ 15 LkSG](https://www.gesetze-im-internet.de/lksg/__15.html) — behördliche Kontrolle und Anordnungen, unverändert in Kraft
- [§ 12 LkSG](https://www.gesetze-im-internet.de/lksg/__12.html), [§ 13 LkSG](https://www.gesetze-im-internet.de/lksg/__13.html) — formal in Kraft, seit **03.09.2025 nicht mehr vollzogen**; Einreichungszugang geschlossen `[unverifiziert - prüfen]`
- [Richtlinie (EU) 2024/1760 (CSDDD)](https://eur-lex.europa.eu/eli/dir/2024/1760/oj) · **Änderungs-RL (EU) 2026/470 (Omnibus I)**, Amtsblatt 26.02.2026, in Kraft 18.03.2026 — Schwelle > 5.000 Beschäftigte und > 1,5 Mrd. EUR, materielle Pflichten ab 26.07.2029; ELI-Fundstelle `[unverifiziert - prüfen]`

### BAFA / Sekundärliteratur

- [BAFA – Lieferkettengesetz](https://www.bafa.de/DE/Lieferketten/ueberblick_node.html) — Handreichungen zu Präventions- und Abhilfemaßnahmen; **Berichtsprüfung nach §§ 12, 13 LkSG zum 03.09.2025 eingestellt, Einreichungsportal geschlossen**
- Grabosch, LkSG, 1. Aufl. 2023; Hembach, BeckOK LkSG (aktualisiert)

## Ausgabeformat

```
PRÄVENTION & ABHILFE (LkSG) — <Unternehmen> — <Datum>

I.    Angemessenheitsmaßstab (§ 3 LkSG)
      Einflussvermögen / Schwere / Wahrscheinlichkeit / Beitrag: <…>
II.   Grundsatzerklärung
      Prioritäre Risiken / Erwartungen: <…>
III.  Prävention eigener Geschäftsbereich (§ 6 LkSG)
      Maßnahmen: <…>
IV.   Prävention unmittelbarer Zulieferer (§ 6 LkSG)
      Vertrag / Audit / Schulung: <…>
V.    Abhilfe (§ 7 LkSG)
      Verletzung eingetreten? [Ja/Nein]
      Inland eigener Geschäftsbereich → Beendigung: <…>
      Zulieferer → Konzept/Zeitplan / ultima ratio Abbruch: <…>
VI.   Priorisierung & Wirksamkeitskontrolle
      <…>
VII.  Dokumentation (§ 10 LkSG) — interne Nachweisführung, 7 Jahre
      Hinweis: KEINE BAFA-Einreichung — §§ 12, 13 LkSG seit 03.09.2025
      nicht mehr vollzogen, Zugang geschlossen ([unverifiziert - prüfen])
      Vorbereitung auf BAFA-Kontrolle §§ 14, 15 LkSG: <…>
VIII. CSDDD-Schwellenprüfung (RL (EU) 2026/470)
      > 5.000 Beschäftigte? [Ja/Nein]  > 1,5 Mrd. EUR? [Ja/Nein]
      Kumulativ erfüllt: [Ja/Nein] — materielle Pflichten ab 26.07.2029
      Nur bei „Ja": Mapping auf Art. 8–11 CSDDD

Restrisiko: <…>
Wiedervorlage: jährlich + anlassbezogen
```
