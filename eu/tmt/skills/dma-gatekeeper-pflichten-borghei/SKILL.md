---
name: dma-gatekeeper-pflichten-borghei
title: /dsa-dma:dma-gatekeeper-pflichten
description: Prüfung der Torwächter-Benennung Art. 3 DMA und des Pflichtenkatalogs Art. 5 DMA und Art. 6 DMA (Verbot der Selbstbevorzugung, Datennutzung, Interoperabilität) sowie der Interoperabilität von Kommunikationsdiensten Art. 7 DMA – samt Durchsetzung. Use when ein Unternehmen prüft, ob es als Gatekeeper benannt ist oder wird, oder welche Verhaltenspflichten der DMA seinem zentralen Plattformdienst auferlegt.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/dsa-dma/skills/dma-gatekeeper-pflichten
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: tmt
language: de
---

# /dsa-dma:dma-gatekeeper-pflichten

## Zweck

Die [VO (EU) 2022/1925 (DMA)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32022R1925) unterwirft als **Torwächter (Gatekeeper)** benannte Betreiber zentraler Plattformdienste einem festen Katalog von Verhaltenspflichten. Dieser Skill prüft, ob die Benennungsschwellen nach **Art. 3 DMA** erreicht sind und welche Ge- und Verbote nach **Art. 5 DMA** und **Art. 6 DMA** den jeweiligen zentralen Plattformdienst treffen.

## Eingaben

- Art des zentralen Plattformdienstes (Suchmaschine, Marktplatz, App-Store, Betriebssystem, Browser, sozialer Dienst, Messenger, Werbedienst)
- Unternehmenskennzahlen (Umsatz/Marktkapitalisierung, aktive Endnutzer/gewerbliche Nutzer)
- Bereits erfolgte Benennung durch die EU-Kommission?
- Konkrete beanstandete Praxis (Selbstbevorzugung, Datenverknüpfung, Kopplung, Interoperabilität)

## Sub-Agent-Architektur

Drei gedankliche Rollen strukturieren die Prüfung. Ein **Benennungs-Prüfer** untersucht, ob die quantitativen und qualitativen Schwellen des Art. 3 DMA erfüllt sind oder eine Benennung bereits vorliegt. Ein **Pflichten-Mapper** ordnet dem konkreten zentralen Plattformdienst die einschlägigen Pflichten aus Art. 5 DMA (unmittelbar anwendbar) und Art. 6 DMA (gegebenenfalls konkretisierungsbedürftig) zu. Ein **Durchsetzungs-Analyst** bewertet das Bußgeldrisiko und Verfahren bei Verstößen. Der Benennungs-Prüfer übergibt an den Pflichten-Mapper erst, wenn die Gatekeeper-Eigenschaft bejaht oder unterstellt ist.

## Ablauf

### 1. Benennung als Torwächter (Art. 3 DMA)

Ein Unternehmen wird benannt, wenn es

a) erheblichen Einfluss auf den Binnenmarkt hat (Umsatz-/Marktkapitalisierungsschwelle),
b) einen zentralen Plattformdienst als wichtiges Zugangstor für gewerbliche Nutzer zu Endnutzern betreibt und
c) eine gefestigte, dauerhafte Position innehat (Nutzerschwellen über drei Jahre).

Die quantitativen Schwellen begründen eine widerlegbare Vermutung; die Kommission kann auch ohne Schwellenerreichung benennen.

### 2. Pflichten nach Art. 5 DMA

Unmittelbar geltende Ge- und Verbote, u. a.:

- **Datenverknüpfungsverbot**: keine Zusammenführung personenbezogener Daten aus dem zentralen Plattformdienst mit anderen Diensten ohne Einwilligung
- **Anti-Steering**: gewerblichen Nutzern darf nicht verboten werden, Angebote außerhalb der Plattform zu bewerben
- **Kein Verbot des Direktvertriebs** an Endnutzer außerhalb der Plattform
- keine Pflicht zur Nutzung der plattformeigenen Identifizierungs-, Bezahl- oder Browser-Engine als Kopplung
- keine Beschränkung beim Anzeigen von Beschwerden bei Behörden

### 3. Pflichten nach Art. 6 DMA

Pflichten, die einer Konkretisierung zugänglich sind, u. a.:

- **Verbot der Selbstbevorzugung** beim Ranking eigener Produkte/Dienste gegenüber Dritten (Art. 6 Abs. 5 DMA)
- **Datennutzung**: keine Verwendung nicht öffentlicher Daten gewerblicher Nutzer im Wettbewerb mit ihnen
- **Interoperabilität** und gleichberechtigter Zugang zu Betriebssystem-/Hardwarefunktionen (Art. 6 Abs. 7 DMA)
- Deinstallierbarkeit vorinstallierter Apps, Wechsel von Voreinstellungen
- Datenportabilität und Echtzeit-Datenzugang für Endnutzer und gewerbliche Nutzer

### 4. Interoperabilität von Kommunikationsdiensten (Art. 7 DMA)

Betreiber nummernunabhängiger interpersoneller Kommunikationsdienste (Messenger) müssen die **Interoperabilität der Grundfunktionen** mit Diensten anderer Anbieter auf Anfrage ermöglichen.

### 5. Durchsetzung (Art. 8, Art. 13, Art. 30 DMA)

- Compliance-Bericht und Pflicht zur wirksamen Einhaltung (Art. 8 DMA)
- Umgehungsverbot (Art. 13 DMA)
- Geldbußen bis **10 % des weltweiten Jahresumsatzes**, bei Wiederholung bis **20 %** (Art. 30 DMA)

## Risiken

- **Selbstbevorzugung** — bevorzugtes Ranking eigener Dienste verstößt gegen Art. 6 Abs. 5 DMA und ist ein zentrales Durchsetzungsthema.
- **Datenverknüpfung ohne Einwilligung** — Zusammenführung von Nutzerdaten über Dienste hinweg verletzt Art. 5 DMA.
- **Umgehungskonstruktionen** — Designtricks (Dark Patterns, Scheineinwilligung) lösen das Umgehungsverbot Art. 13 DMA aus.
- **Bußgeldrisiko** — Verstöße können bis 10 % bzw. 20 % des Weltumsatzes nach Art. 30 DMA kosten.

## Ausgabeformat

```
DMA GATEKEEPER-PRÜFUNG — <Unternehmen / Dienst> — <Datum>

I.   Zentraler Plattformdienst                 [Typ]
II.  Benennung (Art. 3 DMA)                     [erfolgt / Schwellen erfüllt / offen]
III. Pflichten Art. 5 DMA                       [einschlägig: <…>]
IV.  Pflichten Art. 6 DMA                        [einschlägig: <…>]
     Selbstbevorzugung (Art. 6 Abs. 5 DMA)      [betroffen? <…>]
     Interoperabilität (Art. 6 Abs. 7 DMA)      [betroffen? <…>]
V.   Kommunikationsdienste (Art. 7 DMA)         [betroffen? <…>]
VI.  Durchsetzungsrisiko (Art. 30 DMA)          [bis 10 % / 20 % Weltumsatz]

Empfehlung: <…>
Nächste Schritte: <…>
```

## Quellen

### Statute

- [VO (EU) 2022/1925 (DMA)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32022R1925) — Volltext
- Art. 3 DMA (Benennung), Art. 5 DMA (Pflichten), Art. 6 DMA (Pflichten), Art. 7 DMA (Interoperabilität Kommunikation), Art. 8 DMA (Einhaltung), Art. 13 DMA (Umgehungsverbot), Art. 30 DMA (Geldbußen)

### Sekundärliteratur

- Körber, DMA-Kommentar, 1. Aufl. 2024
- Bundeskartellamt, Hinweise zur Digitalwirtschaft
