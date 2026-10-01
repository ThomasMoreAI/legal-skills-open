---
name: providerhaftung-borghei
title: /it-recht:providerhaftung
description: 'Prüfung der Verantwortlichkeit von Diensteanbietern für fremde/nutzergenerierte Inhalte: beschränkte Verantwortlichkeit (§ 7 DDG i. V. m. Art. 4–8 DSA), Hosting (Art. 6 DSA), keine allgemeine Überwachungspflicht (Art. 8 DSA), Sperranspruch (§ 8 DDG), Auskunft (§ 10 DDG), Störerhaftung und Notice-and-Takedown. Use when die Haftung eines Host- oder Access-Providers für Drittinhalte zu beurteilen ist.'
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/it-recht/skills/providerhaftung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: tmt
language: de
---

# /it-recht:providerhaftung

## Zweck

Seit dem 14.05.2024 hat das Digitale-Dienste-Gesetz (DDG) das TMG abgelöst; die materiellen Haftungsprivilegien für Diensteanbieter ergeben sich nun aus dem unmittelbar geltenden Digital Services Act (DSA, VO (EU) 2022/2065), auf den § 7 DDG verweist. Dieser Skill ordnet einen Anbieter der richtigen Kategorie zu, prüft, ob das Haftungsprivileg greift, und bestimmt verbleibende Unterlassungs-, Sperr- und Auskunftspflichten für fremde, nutzergenerierte Inhalte.

## Eingaben

- Rolle des Anbieters (Access-Provider, Caching, Host-Provider, eigene Inhalte)
- Art des beanstandeten Inhalts (Persönlichkeitsrechtsverletzung, Urheberrecht, strafbarer Inhalt)
- Kenntnisstand des Anbieters und Zeitpunkt der Kenntniserlangung
- Vorliegen einer Meldung/Beanstandung (Notice) und Reaktion darauf
- Begehrtes Ziel (Schadensersatz, Unterlassung/Sperrung, Auskunft)

## Sub-Agent-Architektur

Die Prüfung verteilt sich auf drei Rollen. Ein **Einordnungs-Agent** bestimmt die Diensteanbieter-Kategorie nach Art. 4–6 DSA, denn nur danach richtet sich das einschlägige Privileg; verwechselt man Access- und Host-Provider, kippt das gesamte Ergebnis. Ein **Privilegierungs-Agent** prüft sodann, ob die Voraussetzungen des Privilegs (insbesondere fehlende Kenntnis nach Art. 6 DSA) noch vorliegen oder durch eine Meldung entfallen sind. Ein **Pflichten-Agent** ermittelt schließlich die trotz Privileg bestehenden Pflichten — Sperrung nach § 8 DDG, Auskunft nach § 10 DDG, Unterlassung aus Störerhaftung — und die Grenze der fehlenden allgemeinen Überwachungspflicht (Art. 8 DSA). Übergeben werden nur Befunde; Basis ist der konkrete Sachverhalt, kein angenommener Standardfall.

## Ablauf

### 1. Beschränkte Verantwortlichkeit (§ 7 DDG)

§ 7 DDG erklärt die Art. 4 bis 8 DSA für alle Diensteanbieter anwendbar, unabhängig von Entgelt. Für **eigene** Inhalte haftet der Anbieter dagegen uneingeschränkt nach den allgemeinen Gesetzen.

### 2. Kategorisierung und Privileg

- **Access-Provider** (reine Durchleitung, Art. 4 DSA): haftet nicht, wenn er die Übermittlung nicht veranlasst, den Adressaten nicht auswählt und die Information nicht verändert.
- **Caching** (Art. 5 DSA): privilegiert bei zeitlich begrenzter Zwischenspeicherung unter den dortigen Bedingungen.
- **Host-Provider** (Speicherung fremder Informationen, Art. 6 DSA): haftet nicht, solange er keine Kenntnis von der rechtswidrigen Information hat; ab Kenntnis muss er unverzüglich entfernen oder sperren (**Notice-and-Takedown**). Das Melde- und Abhilfeverfahren ist in Art. 16 DSA ausgestaltet.

### 3. Keine allgemeine Überwachungspflicht (Art. 8 DSA)

Anbieter trifft keine allgemeine Pflicht, die übermittelten oder gespeicherten Informationen zu überwachen oder aktiv nach rechtswidrigen Tätigkeiten zu forschen (Art. 8 DSA). Spezifische Prüfpflichten nach konkretem Hinweis bleiben hiervon unberührt.

### 4. Störerhaftung, Sperr- und Auskunftsanspruch

Auch bei greifendem Haftungsprivileg kann der Anbieter als mittelbarer Verletzer auf **Unterlassung** in Anspruch genommen werden (Störerhaftung), wenn er zumutbare Prüfpflichten verletzt; § 8 DDG normiert hierzu — beschränkt auf die Verletzung von Rechten des geistigen Eigentums — einen Anspruch auf Sperrung gegen den Access-Provider. § 10 DDG regelt das Auskunftsverlangen der nach Landesrecht zuständigen Behörde. Das Privileg schließt Schadensersatz aus, nicht aber den in die Zukunft gerichteten Beseitigungs-/Unterlassungsanspruch.

### 5. Schnittstelle zum DSA

Der DSA gilt als Verordnung unmittelbar; das DDG flankiert ihn (Durchsetzung, Koordinierungsstelle bei der Bundesnetzagentur, Bußgeld). Für sehr große Plattformen (VLOPs) treten zusätzliche Sorgfaltspflichten hinzu.

## Risiken

- **Überwachungspflicht** fälschlich angenommen — eine allgemeine Überwachung ist nach Art. 8 DSA gerade nicht geschuldet; umgekehrt darf nach konkretem Hinweis die spezifische Prüfung nicht unterbleiben.
- **Notice-and-Takedown** verzögert umgesetzt — nach Kenntnis (Art. 6 DSA) entfällt das Privileg; Schadensersatzhaftung droht.
- **Störerhaftung** übersehen — das Haftungsprivileg schützt nicht vor Unterlassung/Sperrung nach § 8 DDG; ein „Wir sind doch nur Host" trägt insoweit nicht.
- **Kenntnis** unsauber dokumentiert — der Zeitpunkt der Kenntniserlangung entscheidet über das Entfallen des Privilegs; fehlende Dokumentation kehrt die Beweissituation um.
- Veraltete TMG-Zitate (§§ 7–10 TMG) statt § 7 DDG / Art. 4–8 DSA — überholtes Recht, falsche Normkette.

## Ausgabeformat

```
PROVIDERHAFTUNG — <Anbieter / Inhalt> — <Datum>

I.   Inhalt                           [eigener / fremder, nutzergenerierter Inhalt]
II.  Kategorie                        [Access (Art. 4) / Caching (Art. 5) / Host (Art. 6)]
III. Haftungsprivileg (§ 7 DDG)       [greift / entfallen — Grund]
     Kenntnis seit:                   <Datum / Meldung>
IV.  Notice-and-Takedown              [rechtzeitig / verspätet]
V.   Überwachungspflicht (Art. 8 DSA) [keine allgemeine — spezifische Prüfpflicht?]
VI.  Sekundäransprüche                [Störerhaftung/Sperrung § 8 DDG / Auskunft § 10 DDG]

Ergebnis (Schadensersatz / Unterlassung): <…>
```

## Quellen

- [§ 7 DDG](https://www.gesetze-im-internet.de/ddg/__7.html), [§ 8 DDG](https://www.gesetze-im-internet.de/ddg/__8.html), [§ 10 DDG](https://www.gesetze-im-internet.de/ddg/__10.html)
- [Art. 4 DSA](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32022R2065), Art. 5 DSA, [Art. 6 DSA](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32022R2065), [Art. 8 DSA](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32022R2065), Art. 16 DSA
- DDG (Digitale-Dienste-Gesetz) als TMG-Nachfolger seit 14.05.2024: [gesetze-im-internet.de/ddg](https://www.gesetze-im-internet.de/ddg/)
