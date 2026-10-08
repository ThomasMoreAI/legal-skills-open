---
name: kritis-anwendungsbereich-registrierung-borghei
title: /kritis-resilienz:kritis-anwendungsbereich-registrierung
description: Anwendungsbereich und Registrierung nach dem KRITIS-Dachgesetz – zehn Sektoren § 4 Abs. 1 (Energie, Transport und Verkehr, Finanzwesen, Sozialversicherung, Gesundheit, Wasser, Ernährung, IT und Telekommunikation, Weltraum, Siedlungsabfallentsorgung), Bereichsausnahmen § 4 Abs. 2 insbesondere für DORA-Finanzunternehmen nach Art. 2 Abs. 2 VO (EU) 2022/2554 sowie für IT/TK und Siedlungsabfallentsorgung, Erheblichkeitsschwellen § 5 mit Verordnungsermächtigung, Registrierungspflicht § 8 binnen drei Monaten ab dem Zeitpunkt, zu dem eine Anlage als kritische Anlage gilt, über die gemeinsame Registrierungsmöglichkeit von BSI und BBK, zentrale Anlaufstelle und sektorspezifisch zuständige Behörden § 3, kritische Einrichtungen von besonderer europäischer Bedeutung § 9 und Ausnahmebescheid § 22. Use when zu klären ist, ob ein Betreiber unter das KRITIS-Dachgesetz fällt und bis wann er sich registrieren muss.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/kritis-resilienz/skills/kritis-anwendungsbereich-registrierung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: cybersecurity
language: de
---

# /kritis-resilienz:kritis-anwendungsbereich-registrierung

## Zweck

Der Skill beantwortet die Eingangsfrage jedes KRITIS-Mandats: Ist der Betreiber erfasst, für welche Anlage, ab wann — und wer ist die zuständige Behörde. Er trennt dabei sauber, was in der Praxis dauernd vermengt wird: das **KRITIS-Dachgesetz** schützt die **physische Resilienz** kritischer Anlagen, während NIS2 und das BSIG die **Cybersicherheit** regeln. Beide Registrierungen bestehen nebeneinander.

## Eingaben

- Betreiber, Rechtsform, Konzernstruktur
- Anlage(n): Art, Standort, erbrachte kritische Dienstleistung, Versorgungsgrad
- Sektor und ggf. Branche nach § 4 Abs. 1
- Ob der Betreiber Finanzunternehmen iSd Art. 2 Abs. 2 VO (EU) 2022/2554 ist oder DORA über § 1a Abs. 2a KWG bzw. § 293 Abs. 5 VAG anwendbar ist
- Zeitpunkt, ab dem die Schwellenwerte erstmals überschritten wurden
- Bestehende Registrierungen beim BSI (NIS2/BSIG) und beim BBK
- Ob eine Einrichtung von besonderer Bedeutung für Europa nach § 9 in Betracht kommt

## Sub-Agent-Architektur

Der Researcher beschafft KRITIS-DachG, die Rechtsverordnung nach § 5 Abs. 1, die RL (EU) 2022/2557, das BSIG und die Verlautbarungen von BBK und BSI. Der Drafter ordnet Anlage und Sektor zu, rechnet die Registrierungsfrist und entwirft die Registrierung. Der Reviewer prüft die Bereichsausnahmen des § 4 Abs. 2, die Zuständigkeit nach § 3 Abs. 2 und ob die NIS2-Registrierung nicht mit der KRITIS-Registrierung verwechselt wurde.

## Ablauf

### 1. Regime trennen — KRITIS-DachG oder BSIG/NIS2

**Dieser Schritt steht vor allem anderen.**

| Frage | Regime | Behörde |
|---|---|---|
| **Physische** Resilienz kritischer Anlagen (Sabotage, Naturgefahren, technisches Versagen, Zutritt, Notfallorganisation, Wiederherstellung) | **[KRITIS-Dachgesetz](https://www.gesetze-im-internet.de/kritisdachg/)** in Umsetzung der RL (EU) 2022/2557 | **BBK** als zentrale Anlaufstelle, sektorspezifisch weitere Behörden |
| **Cybersicherheit**, Risikomanagement, IT-Vorfälle | **BSIG / NIS2** | **BSI** |
| **IKT-Risiko** von Finanzunternehmen | **DORA**, VO (EU) 2022/2554 | BaFin, `/dora:ikt-drittparteienrisiko` |

Ein Betreiber kann **beiden** deutschen Regimen unterliegen und muss sich dann **zweimal** registrieren — beim BSI und beim BBK. Die gemeinsame Registrierungsmöglichkeit nach § 8 Abs. 1 ist eine technische Erleichterung, keine Zusammenlegung der Pflichten.

### 2. Sektor bestimmen ([§ 4 Abs. 1 KRITISDachG](https://www.gesetze-im-internet.de/kritisdachg/__4.html))

Das Gesetz gilt für Betreiber kritischer Anlagen in **zehn** Sektoren:

1. Energie · 2. Transport und Verkehr · 3. Finanzwesen · 4. Leistungen der Sozialversicherung sowie Grundsicherung für Arbeitsuchende · 5. Gesundheitswesen · 6. Wasser · 7. Ernährung · 8. Informationstechnik und Telekommunikation · 9. **Weltraum** · 10. Siedlungsabfallentsorgung.

### 3. Bereichsausnahmen prüfen ([§ 4 Abs. 2 KRITISDachG](https://www.gesetze-im-internet.de/kritisdachg/__4.html)) — der wichtigste Filter

§ 3 Abs. 8, die §§ 9, 10, 12 bis 16, 18, 19 Abs. 2 sowie §§ 20, 21 Abs. 6 gelten **nicht** für:

| Nr. | Ausgenommen | Reichweite |
|---|---|---|
| 1 | **Finanzunternehmen** nach Art. 2 Abs. 2 VO (EU) 2022/2554 sowie Unternehmen, für die DORA über **§ 1a Abs. 2a KWG** oder **§ 293 Abs. 5 VAG** gilt | vollständige Ausnahme von den genannten Vorschriften |
| 2 | Betreiber im Sektor **Informationstechnik und Telekommunikation** | vollständig |
| 3 | Betreiber im Sektor **Siedlungsabfallentsorgung** | **mit Ausnahme des § 12** (Risikoanalyse bleibt) |
| 4 | Betreiber im Sektor **Sozialversicherung und Grundsicherung** | mit Ausnahme des § 1 |

**Praxisfolge:** Ein DORA-pflichtiges Kreditinstitut ist zwar Betreiber im Sektor Finanzwesen, unterliegt aber weder den Resilienzpflichten des § 13 noch der Vorfallmeldung des § 18 noch der Geschäftsleiterpflicht des § 20. Die **Registrierungspflicht des § 8 bleibt** jedoch bestehen — sie steht nicht im Ausnahmekatalog. Wer die Ausnahme pauschal auf „das ganze Gesetz" erstreckt, versäumt die Registrierung.

### 4. Erheblichkeit der Anlage bestimmen ([§ 5 KRITISDachG](https://www.gesetze-im-internet.de/kritisdachg/__5.html))

Eine Anlage ist kritisch, wenn sie für die Erbringung einer kritischen Dienstleistung **erheblich** ist. Die konkreten Schwellenwerte — Versorgungsgrad, Kategorien, Bemessungsgrößen — ergeben sich aus der **Rechtsverordnung nach § 5 Abs. 1 S. 1**; sie ist im Einzelfall heranzuziehen und mit Fassungsstand zu zitieren `[unverifiziert – prüfen]`.

Ergänzend: **[§ 6](https://www.gesetze-im-internet.de/kritisdachg/__6.html)** (sonstige Resilienzregelungen), **[§ 7](https://www.gesetze-im-internet.de/kritisdachg/__7.html)** (Einrichtungen der Bundesverwaltung).

### 5. Registrieren ([§ 8 KRITISDachG](https://www.gesetze-im-internet.de/kritisdachg/__8.html))

Der Betreiber ist verpflichtet, **spätestens drei Monate, nachdem eine Anlage als kritische Anlage gilt**, dem **BBK** über die **gemeinsam von BSI und BBK eingerichtete Registrierungsmöglichkeit** zu übermitteln:

1. Name des Betreibers einschließlich Rechtsform und ggf. Handelsregisternummer,
2. Anschrift und aktuelle Kontaktdaten einschließlich E-Mail-Adresse und Telefonnummer,
3. Name oder referenzierbare Bezeichnung der kritischen Anlage,
4. Sektor und ggf. Branche sowie die kritische Dienstleistung, für deren Erbringung die Anlage erheblich ist,
5. soweit einschlägig die Kategorie der Anlage und deren Werte zum Versorgungsgrad,
6. weitere in § 8 Abs. 1 benannte Angaben.

Die Frist knüpft an den **Geltungszeitpunkt** an — den Moment, in dem die Anlage die Schwelle erstmals erreicht —, **nicht** an die Kenntnis des Betreibers und nicht an ein behördliches Schreiben. Verstöße sind nach [§ 24 Abs. 1 Nr. 1 KRITISDachG](https://www.gesetze-im-internet.de/kritisdachg/__24.html) bußgeldbewehrt.

### 6. Zuständige Behörde bestimmen ([§ 3 KRITISDachG](https://www.gesetze-im-internet.de/kritisdachg/__3.html))

- **Abs. 1** — Das **Bundesamt für Bevölkerungsschutz und Katastrophenhilfe (BBK)** ist **zentrale Anlaufstelle** iSd Art. 9 Abs. 2 RL (EU) 2022/2557.
- **Abs. 2** — Zuständige Behörde ist je nach kritischer Dienstleistung unter anderem:
  - das **BMI** für Dienstleistungen von Einrichtungen der Bundesverwaltung,
  - die **Bundesnetzagentur** für Strom-, Erdgas- und Wasserstoffversorgung sowie den Betrieb öffentlicher Telekommunikationsnetze und -dienste,
  - das **BMWE** für die Mineralölversorgung,
  - die **Generaldirektion Wasserstraßen und Schifffahrt** für See- und Binnenschifffahrt bezogen auf bundeseigene Wasserstraßeninfrastruktur,
  - weitere in § 3 Abs. 2 benannte Stellen.

Die Zuordnung ist im Mandat konkret zu treffen; eine pauschale Nennung „des BBK" trägt nur für die Anlaufstellenfunktion und die Registrierung.

### 7. Einrichtungen von besonderer europäischer Bedeutung ([§ 9](https://www.gesetze-im-internet.de/kritisdachg/__9.html), [§ 10 KRITISDachG](https://www.gesetze-im-internet.de/kritisdachg/__10.html))

Erbringt eine Einrichtung dieselbe oder eine gleichartige kritische Dienstleistung in oder für **mindestens sechs Mitgliedstaaten**, greifen die besonderen Vorschriften des § 9 sowie die **Beratungsmission** nach § 10. Die Schwelle ist konzernweit zu prüfen und gegen den Verordnungstext abzugleichen `[unverifiziert – prüfen]`.

**[§ 22](https://www.gesetze-im-internet.de/kritisdachg/__22.html)** eröffnet einen **Ausnahmebescheid** — der einzige Weg, sich einzelnen Pflichten förmlich zu entziehen; er ist zu beantragen und zu begründen, nicht zu unterstellen.

## Deterministische Berechnung

Die Dreimonatsfrist des § 8 Abs. 1 ist die zentrale Frist dieses Skills. Der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) macht nur die Arithmetik — der **Geltungszeitpunkt** ist eine Tatsachenfeststellung und gesondert zu belegen:

```bash
# § 8 Abs. 1 KRITISDachG: 3 Monate ab dem Zeitpunkt, zu dem die Anlage als kritisch gilt
python -m scripts.legal_calc.cli frist --ereignis 17.04.2026 --menge 3 --einheit monate --land BY

# Widerspruchs- bzw. Klagefrist gegen eine Anordnung nach § 16
python -m scripts.legal_calc.cli frist --ereignis 02.06.2026 --menge 1 --einheit monate --land BY
```

## Quellen

### Statute

- [§ 1](https://www.gesetze-im-internet.de/kritisdachg/__1.html), [§ 2](https://www.gesetze-im-internet.de/kritisdachg/__2.html), [§ 3](https://www.gesetze-im-internet.de/kritisdachg/__3.html), [§ 4 KRITISDachG](https://www.gesetze-im-internet.de/kritisdachg/__4.html), [§ 5](https://www.gesetze-im-internet.de/kritisdachg/__5.html), [§ 6](https://www.gesetze-im-internet.de/kritisdachg/__6.html), [§ 7](https://www.gesetze-im-internet.de/kritisdachg/__7.html), [§ 8](https://www.gesetze-im-internet.de/kritisdachg/__8.html), [§ 9](https://www.gesetze-im-internet.de/kritisdachg/__9.html), [§ 10](https://www.gesetze-im-internet.de/kritisdachg/__10.html), [§ 22](https://www.gesetze-im-internet.de/kritisdachg/__22.html), [§ 24 KRITISDachG](https://www.gesetze-im-internet.de/kritisdachg/__24.html)
- Richtlinie (EU) 2022/2557 (CER-Richtlinie), Art. 9 — [EUR-Lex](https://eur-lex.europa.eu/eli/dir/2022/2557/oj)
- Verordnung (EU) 2022/2554 (DORA), Art. 2 Abs. 2 — [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2022/2554/oj)
- [BSIG](https://www.gesetze-im-internet.de/bsig_2009/); Richtlinie (EU) 2022/2555 (NIS2)
- [§ 1a KWG](https://www.gesetze-im-internet.de/kredwg/__1a.html), [§ 293 VAG](https://www.gesetze-im-internet.de/vag_2016/__293.html)
- Rechtsverordnung nach § 5 Abs. 1 KRITISDachG (Schwellenwerte) `[unverifiziert – prüfen]`

### Kommentare und Literatur

- Kommentierungen zum KRITIS-Dachgesetz und zur CER-Richtlinie (Erscheinungsstand 2025/2026 prüfen) `[unverifiziert – prüfen]`
- Gitter/Kipker, IT-Sicherheitsrecht (zur Abgrenzung BSIG / KRITIS-DachG).
- Verlautbarungen des BBK und des BSI zur gemeinsamen Registrierung.

### Rechtsprechung

Das KRITIS-Dachgesetz ist erst 2026 in Kraft getreten; **Rechtsprechung existiert nicht**. Für die verwaltungsrechtliche Flankierung ist auf die allgemeine Judikatur zu §§ 28, 35, 40 VwVfG und zum BSIG zurückzugreifen; jede Entscheidung ist vor Verwendung zu verifizieren `[unverifiziert – prüfen]`.

## Ausgabeformat

```
KRITIS-BETROFFENHEIT — <Betreiber> — <Datum>

I.   Regimezuordnung
     Physische Resilienz:     KRITIS-DachG [ja / nein]
     Cybersicherheit:         BSIG/NIS2    [ja / nein]  → getrennte BSI-Registrierung
     DORA:                    [ja — § 4 Abs. 2 Nr. 1 / nein]

II.  Sektor und Anlage § 4 Abs. 1
     Sektor:                  <Nr. 1–10>   Branche: <…>
     Kritische Dienstleistung:<…>
     Anlage:                  <Bezeichnung, Standort>

III. Bereichsausnahmen § 4 Abs. 2
     Nr. 1 DORA-Finanzunternehmen: [ja / nein]
     Nr. 2 IT/TK:                  [ja / nein]
     Nr. 3 Siedlungsabfall:        [ja — § 12 bleibt / nein]
     Nr. 4 Sozialversicherung:     [ja — § 1 bleibt / nein]
     Ausgenommene Vorschriften:    <§§ 9, 10, 12–16, 18, 19 Abs. 2, 20, 21 Abs. 6 …>
     ACHTUNG: § 8 (Registrierung) ist NICHT ausgenommen

IV.  Erheblichkeit § 5
     Schwellenwert der RVO:   <…>   Erreicht am: <Datum>
     Geltungszeitpunkt:       <Datum>

V.   Registrierung § 8
     Frist (3 Monate) endet:  <Datum>
     Angaben Nr. 1–6:         <Vollständigkeitscheck>
     Status:                  [erfolgt am <Datum> / offen]
     Bußgeldrisiko § 24 Abs. 1 Nr. 1: bis 100.000 EUR

VI.  Zuständigkeit § 3
     Zentrale Anlaufstelle:   BBK
     Sektorbehörde Abs. 2:    <BNetzA / BMI / BMWE / GDWS / …>

VII. Besondere europäische Bedeutung § 9
     Sechs oder mehr Mitgliedstaaten: [ja — §§ 9, 10 / nein]
     Ausnahmebescheid § 22:   [beantragt / nicht einschlägig]

VIII.Risiko: 🟢 / 🟡 / 🔴 <Begründung>
IX.  Quellenverzeichnis
```

## Risiken / typische Fehler

- **KRITIS-DachG und BSIG/NIS2 verwechselt.** Das Dachgesetz regelt die **physische** Resilienz; die Cybersicherheit bleibt beim BSIG. Beide Registrierungen sind getrennt zu erfüllen.
- **Bereichsausnahme des § 4 Abs. 2 auf das ganze Gesetz erstreckt.** Sie erfasst einen **benannten Katalog** von Vorschriften — die **Registrierungspflicht des § 8 gehört nicht dazu**.
- **DORA-Ausnahme ohne Prüfung von § 1a Abs. 2a KWG und § 293 Abs. 5 VAG angenommen.**
- **Dreimonatsfrist ab Behördenschreiben gerechnet.** § 8 Abs. 1 knüpft an den **Geltungszeitpunkt** der Anlage an.
- **Schwellenwerte aus dem Gedächtnis zitiert** statt aus der Rechtsverordnung nach § 5 Abs. 1.
- **Sektorbehörde pauschal als BBK benannt.** Das BBK ist zentrale Anlaufstelle; zuständig sind nach § 3 Abs. 2 je nach Dienstleistung BNetzA, BMI, BMWE, GDWS und weitere.
- **Weltraum und Siedlungsabfallentsorgung übersehen** — beide sind eigene Sektoren des § 4 Abs. 1.
- **Ausnahmebescheid § 22 unterstellt**, statt ihn zu beantragen und zu begründen.
- **Rechtsprechung erfunden.** Zum KRITIS-DachG gibt es keine; jede Entscheidung ist zu belegen oder als `[unverifiziert – prüfen]` zu kennzeichnen.
