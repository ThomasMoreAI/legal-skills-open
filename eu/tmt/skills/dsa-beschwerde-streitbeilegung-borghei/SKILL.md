---
name: dsa-beschwerde-streitbeilegung-borghei
title: /dsa-dma:dsa-beschwerde-streitbeilegung
description: Rechtsbehelfe gegen Inhaltsmoderation nach DSA – internes Beschwerdemanagementsystem Art. 20 DSA, außergerichtliche Streitbeilegung Art. 21 DSA, vorrangige Bearbeitung von Meldungen vertrauenswürdiger Hinweisgeber Art. 22 DSA. Use when ein Nutzer gegen eine Moderationsentscheidung vorgehen will oder eine Plattform ihr Beschwerde- und Streitbeilegungssystem DSA-konform aufsetzen muss.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/dsa-dma/skills/dsa-beschwerde-streitbeilegung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: tmt
language: de
---

# /dsa-dma:dsa-beschwerde-streitbeilegung

## Zweck

Gegen Moderationsentscheidungen (Sperrung, Löschung, Demonetarisierung, Account-Sperre) gibt die [VO (EU) 2022/2065](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32022R2065) ein gestuftes Rechtsbehelfssystem: internes Beschwerdemanagement (**Art. 20 DSA**), zertifizierte außergerichtliche Streitbeilegung (**Art. 21 DSA**) und der vorrangige Status vertrauenswürdiger Hinweisgeber (**Art. 22 DSA**). Dieser Skill prüft, ob diese Mechanismen vorhanden, fristgerecht und korrekt ausgestaltet sind.

## Eingaben

- Art der angegriffenen Entscheidung (Inhalts- oder Accountmaßnahme)
- Adressat (Nutzer / Geschäftsanwender / Meldender)
- Bestehendes internes Beschwerdesystem (Fristen, Kostenfreiheit, menschliche Prüfung)
- Bereits durchlaufene Stufen
- Beteiligung eines vertrauenswürdigen Hinweisgebers?

## Sub-Agent-Architektur

Drei gedankliche Rollen arbeiten zusammen. Ein **Beschwerde-Prüfer** untersucht, ob das interne System nach Art. 20 DSA besteht und die formalen Anforderungen (sechs Monate Frist, Kostenfreiheit, nicht ausschließlich automatisierte Entscheidung) erfüllt. Ein **Streitbeilegungs-Lotse** prüft den Weg zur zertifizierten außergerichtlichen Stelle nach Art. 21 DSA samt Kostenfolge. Ein **Hinweisgeber-Analyst** klärt, ob eine Meldung von einem vertrauenswürdigen Hinweisgeber nach Art. 22 DSA stammt und deshalb vorrangig zu behandeln war. Die Rollen werden sequentiell durchlaufen; der Beschwerde-Prüfer übergibt an den Streitbeilegungs-Lotsen erst, wenn die interne Stufe ausgeschöpft oder ergebnislos ist.

## Ablauf

### 1. Internes Beschwerdemanagementsystem (Art. 20 DSA)

Online-Plattformen müssen Nutzern ein **wirksames internes Beschwerdemanagementsystem** bieten:

- elektronisch und **kostenlos** zugänglich
- Beschwerde mindestens **sechs Monate** nach der Entscheidung möglich
- gegen Entscheidungen über rechtswidrige Inhalte und AGB-Verstöße sowie über Account- und Monetarisierungsmaßnahmen
- Bearbeitung zeitnah, diskriminierungsfrei, sorgfältig, frei von Willkür
- Entscheidung **nicht ausschließlich automatisiert** (Art. 20 Abs. 6 DSA)
- begründete Mitteilung an den Beschwerdeführer samt Hinweis auf Art. 21 DSA

### 2. Außergerichtliche Streitbeilegung (Art. 21 DSA)

Nutzer können eine **zertifizierte außergerichtliche Streitbeilegungsstelle** anrufen:

- Zertifizierung durch den Koordinator für digitale Dienste (DSC)
- Verfahren ist nicht bindend, ersetzt nicht den Gerichtsweg
- **Kostenfolge**: Obsiegt der Nutzer, trägt die Plattform die angemessenen Kosten; obsiegt die Plattform, trägt der Nutzer nur bei Bösgläubigkeit
- Plattform muss in gutem Glauben mitwirken

### 3. Vertrauenswürdige Hinweisgeber (Art. 22 DSA)

Meldungen von **vertrauenswürdigen Hinweisgebern** (trusted flaggers) sind **vorrangig und unverzüglich** zu bearbeiten:

- Status wird vom DSC zuerkannt an Stellen mit besonderer Sachkenntnis, Unabhängigkeit von Plattformen und sorgfältiger Arbeitsweise
- bei Missbrauch (häufig unbegründete Meldungen) kann der Status ausgesetzt werden
- die Plattform muss ein Verfahren gegen Missbrauch nach Art. 23 DSA vorhalten

### 4. Verzahnung mit der Begründung (Art. 17 DSA)

Jede Stufe setzt voraus, dass die ursprüngliche Maßnahme eine Begründung nach **Art. 17 DSA** erhalten hat — sie liefert den Prüfungsgegenstand für Beschwerde und Streitbeilegung.

## Risiken

- **Fristverkürzung** — wird die Beschwerde kürzer als sechs Monate zugelassen, verstößt dies gegen Art. 20 DSA.
- **Rein automatisierte Beschwerdeentscheidung** — Art. 20 Abs. 6 DSA verlangt menschliche Beteiligung; vollautomatische Ablehnung ist unzulässig.
- **Trusted Flagger nachrangig behandelt** — Verstoß gegen die Vorrangpflicht des Art. 22 DSA.
- **Streitbeilegung blockiert** — Verweigerung der Mitwirkung oder Kostenüberwälzung entgegen Art. 21 DSA.

## Ausgabeformat

```
DSA RECHTSBEHELFS-PRÜFUNG — <Plattform> — <Datum>

I.   Angegriffene Maßnahme                       [Inhalt / Account / Monetarisierung]
II.  Internes System (Art. 20 DSA)               [vorhanden / Mängel: <…>]
     Frist 6 Monate                              [ja / nein]
     Menschliche Prüfung (Art. 20 Abs. 6 DSA)    [ja / nein]
III. Außergerichtliche Streitbeilegung (Art. 21 DSA)  [möglich — Stelle / Kostenfolge]
IV.  Vertrauenswürdiger Hinweisgeber (Art. 22 DSA)    [ja — vorrangig? / nein]
V.   Begründung vorhanden (Art. 17 DSA)          [ja / nein]

Empfehlung: <…>
Nächste Schritte: <…>
```

## Quellen

### Statute

- [VO (EU) 2022/2065 (DSA)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32022R2065) — Volltext
- Art. 17 DSA (Begründung), Art. 20 DSA (internes Beschwerdemanagement), Art. 21 DSA (außergerichtliche Streitbeilegung), Art. 22 DSA (vertrauenswürdige Hinweisgeber), Art. 23 DSA (Maßnahmen gegen Missbrauch)

### Sekundärliteratur

- Spindler/Schmitz, DSA-Kommentar, 1. Aufl. 2024
- BeckOK DSA (Online)
