---
name: dsa-statement-of-reasons-borghei
title: /dsa-dma:dsa-statement-of-reasons
description: Erstellung eines DSA-konformen 'Statement of Reasons' nach Art. 17 DSA bei Inhaltsmoderations-Entscheidungen (Sperrung, Löschung, Demonetarisierung, Account-Sperre) – Inhaltsanforderungen, Bezug zu Allgemeinen Geschäftsbedingungen, Rechtsbehelfsbelehrung, DSA-Transparenzdatenbank. Use when ein Hosting-Anbieter oder eine Online-Plattform eine Inhalts-Restriktion gegenüber einem Nutzer kommuniziert.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/dsa-dma/skills/dsa-statement-of-reasons
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: tmt
language: de
---

# /dsa-dma:dsa-statement-of-reasons

## Zweck

Art. 17 DSA verlangt, dass Plattformen jede Moderationsentscheidung **klar und konkret begründen**. Pauschal-Sperren ("Verstoß gegen unsere AGB") sind unzureichend. Die Begründungen werden zentral in der **DSA-Transparenzdatenbank** veröffentlicht — Mängel sind öffentlich nachvollziehbar.

## Eingaben

- Art der Restriktion (Entfernung, Sperrung, Demonetarisierung, Reichweitenbeschränkung, Account-Sperre)
- Adressat (Nutzer / Geschäftsanwender)
- Anlass (eigene AGB-Verletzung / rechtswidriger Inhalt nach nationalem Recht / Trusted-Flagger-Meldung)
- Automatisierung (algorithmisch / menschlich)
- Gerichtliche oder behördliche Anordnung (Art. 9 DSA) zugrunde liegend?

## Ablauf

### 1. Anwendungsbereich (Art. 17 Abs. 1 DSA)

Pflicht greift bei **Beschränkungen** im Hinblick auf:

a) Sichtbarkeit konkreter Inhalte (Entfernung, Sperrung, Reichweitenherabsetzung)
b) Monetarisierung
c) Erbringung des Dienstes (Account-Sperre, -Beendigung)
d) Nutzerkonto (vorübergehend / dauerhaft)

Adressat ist der **betroffene Nutzer**, sofern bekannt.

### 2. Pflichtinhalte (Art. 17 Abs. 3 DSA)

Jede Begründung muss enthalten:

a) Art der Beschränkung und territorialer Geltungsbereich
b) Tatsachen und Umstände, auf denen die Entscheidung beruht (insb. ob die Information aus einer Notice nach Art. 16 oder einer eigenen Erkennung stammt)
c) Ggf. Nutzung automatisierter Mittel — auch bei eigener Erkennung
d) Bei rechtswidrigem Inhalt: Verweis auf einschlägige Rechtsgrundlage
e) Bei AGB-Verstoß: Verweis auf einschlägige Klausel + Begründung
f) Information über Rechtsbehelfsmöglichkeiten — Internal Complaint Handling (Art. 20), Outof-court Dispute Settlement (Art. 21), Gerichtsweg

### 3. Form

- **Klar und verständlich** (Art. 17 Abs. 3)
- **In der Sprache** des Empfängers — soweit angemessen
- **Vor oder bei Wirksamwerden** der Maßnahme

### 4. DSA-Transparenzdatenbank (Art. 24 Abs. 5 DSA)

Jeder Statement of Reasons wird an die zentrale **DSA Transparency Database** der EU-Kommission gemeldet, mit folgenden Pflichtfeldern:

- Identifizierungscode der Entscheidung
- Mitgliedstaat
- Plattformkategorie
- Restriktionstyp
- Begründung
- Verwendung automatisierter Mittel

### 5. Ausnahmen

- **Gerichtliche/behördliche Anordnungen** (Art. 9 DSA) — Sonderregime; Anordnungsempfänger wird (anstelle des Nutzers) primär adressiert.
- **Manifest illegale Inhalte** auf Grundlage gerichtlicher Anordnung — kein Statement of Reasons gegenüber dem Nutzer erforderlich, wenn die Anordnung das ausdrücklich verbietet.

### 6. Rechtsbehelf (Art. 20 DSA)

Plattformen müssen ein **internes Beschwerdemanagementsystem** anbieten:

- mind. **6 Monate** nach Entscheidung
- kostenlos
- entschieden durch nicht ausschließlich automatisierte Mittel
- Information über Out-of-court Dispute Settlement (Art. 21)

## Quellen

### Statute

- [VO (EU) 2022/2065 (DSA)](https://eur-lex.europa.eu/eli/reg/2022/2065/oj) — Volltext
- [Art. 9](https://eur-lex.europa.eu/eli/reg/2022/2065/oj) (Anordnungen), [Art. 16](https://eur-lex.europa.eu/eli/reg/2022/2065/oj) (Notice-and-Action), [Art. 17](https://eur-lex.europa.eu/eli/reg/2022/2065/oj) (Statement of Reasons), [Art. 20](https://eur-lex.europa.eu/eli/reg/2022/2065/oj), [Art. 21](https://eur-lex.europa.eu/eli/reg/2022/2065/oj), [Art. 22](https://eur-lex.europa.eu/eli/reg/2022/2065/oj), [Art. 24 Abs. 5](https://eur-lex.europa.eu/eli/reg/2022/2065/oj)

### Sekundärliteratur

- Spindler/Schmitz, DSA-Kommentar, 1. Aufl. 2024
- BeckOK DSA (Online)

### Soft-Law

- [DSA Transparency Database](https://transparency.dsa.ec.europa.eu/) — öffentliche Datenbank, Schemata + Felddefinitionen
- EU-Kommission, Leitlinien zur Anwendung von Art. 17 DSA

## Ausgabeformat

```
DSA STATEMENT OF REASONS — Entscheidungs-ID — <Datum>

An: <Nutzer/Geschäftsanwender>

Sie erhalten dieses Schreiben gemäß Art. 17 DSA. Wir haben am
<Datum> die folgende Maßnahme getroffen:

  Art der Beschränkung: <Entfernung / Sperrung / Demonetarisierung / …>
  Territorialer Geltungsbereich: <…>
  Betroffener Inhalt / Dienst: <ID / URL>

Begründung:
  Tatsachen und Umstände: <…>
  [Notice nach Art. 16 / eigene Erkennung]
  Verwendung automatisierter Mittel: [ja / nein, Beschreibung]
  Rechtsgrundlage / AGB-Klausel: <konkret>
  Auslegung: <…>

Rechtsbehelfsbelehrung:
  Internes Beschwerdemanagement nach Art. 20 DSA — Frist 6 Monate
  Außergerichtliche Streitbeilegung nach Art. 21 DSA — zertifizierte Stellen siehe DSC
  Gerichtsweg unberührt

Übermittlung an DSA Transparency Database: <ID>
Datum der Wirksamkeit: <…>
```

## Risiken / typische Fehler

- **Pauschalbegründung** („Verstoß gegen unsere AGB") ohne konkrete Klausel — verstößt gegen Art. 17 Abs. 3 lit. e.
- **Automatisierte Mittel nicht offengelegt** — Verstoß gegen Art. 17 Abs. 3 lit. c.
- **Rechtsbehelfsbelehrung fehlt oder unvollständig**.
- **DSA Transparency Database-Meldung vergessen** — Art. 24 Abs. 5 ist Pflicht, nicht nur das Schreiben an den Nutzer.
- **Sprachwahl ungeeignet** — Begründung in einer Sprache, die der Nutzer nicht versteht.
- **Bei Gerichtsanordnung Statement abgegeben, obwohl untersagt** — kann Untersuchungsverlauf gefährden.
