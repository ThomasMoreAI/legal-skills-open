---
name: energieeffizienzpflicht-borghei
title: /energierecht:energieeffizienzpflicht
description: Überblicksprüfung der Energieeffizienzpflichten für Unternehmen – EnMS-/UMS-Pflicht nach § 8 EnEfG ab Endenergieverbrauch >7,5 GWh/a, Energieaudit-Pflicht für Nicht-KMU alle 4 Jahre nach § 8 EDL-G, Veröffentlichungs- und Umsetzungspflichten wesentlicher Effizienzmaßnahmen, Schnittstellen GEG (Gebäude) und CSRD/ESRS E1 (Berichterstattung). Use when ein Unternehmen seine Pflichten nach EnEfG/EDL-G erstmals oder turnusmäßig überprüft oder ein BAFA-Nachweis vorbereitet werden muss.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/energierecht/skills/energieeffizienzpflicht
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: energy
language: de
---

# /energierecht:energieeffizienzpflicht

## Zweck

Der Skill liefert eine **Übersicht** über die in einem Unternehmen einschlägigen Energieeffizienzpflichten und ordnet sie den richtigen Adressatenkreisen zu: Energiemanagementsystem (EnMS) bzw. Umweltmanagementsystem (UMS) nach § 8 EnEfG, Energieaudit nach § 8 EDL-G, Veröffentlichung wesentlicher Effizienzmaßnahmen, Schnittstelle GEG/CSRD. Er bereitet die Nachweisführung gegenüber dem BAFA vor.

> **⚠️ Aktualität (Stand 2026-07) — die 65 %-Regel für Heizungen ist aufgehoben:** Der Deutsche Bundestag hat das **Gebäudemodernisierungsgesetz (GModG)** am **10.07.2026** in namentlicher Abstimmung mit **323 : 271** Stimmen beschlossen. Das Gesetz **streicht §§ 71, 71b–71p und § 72 GEG**. Die Pflicht, dass jede neu eingebaute Heizung zu mindestens **65 % mit erneuerbaren Energien** betrieben werden muss, **besteht nicht mehr**.
>
> | Alt (bis GModG) | Neu (GModG) |
> |---|---|
> | § 71 GEG: 65 % erneuerbare Energien je Heizung | gestrichen — **freie Heizungswahl ab November 2026** |
> | §§ 71b–71p GEG: Erfüllungsoptionen, Übergangs- und Härtefallregeln | gestrichen |
> | § 72 GEG: Betriebsverbote/Austauschpflichten | gestrichen |
> | — | **Bio-Anteilspflicht („Bio-Treppe") ab 01.01.2029** für weiter betriebene Gas-/Ölheizungen |
> | — | **Quote für grünes Gas / grünes Heizöl ab 2028** |
> | — | **Klimaneutralität aller Heizbrennstoffe bis 2045** |
>
> **Neuer Anknüpfungspunkt auf Gebäudeebene ist die kommunale Wärmeplanung nach dem WPG**, nicht mehr eine bundeseinheitliche Prozentvorgabe: Kommunen mit **mehr als 100.000 Einwohnern** haben den Wärmeplan bis **30.06.2026** vorzulegen, kleinere Kommunen bis **30.06.2028**. Ob und welche Anforderungen an einen Heizungstausch gestellt werden, ist deshalb **standortbezogen** anhand des jeweiligen kommunalen Wärmeplans (Gebiet für Wärmenetz / Wasserstoffnetz / dezentrale Versorgung) zu ermitteln.
>
> Weitergeltend bleiben die **Anforderungen an den Primärenergiebedarf** und die **Energieausweis-Pflichten (§§ 79 ff. GEG)**. Das **EnEfG** und das **EDL-G** sind von der Novelle **nicht** betroffen. Das genaue **Inkrafttreten** (erwartet Ende Juli / Anfang August 2026) und die BGBl.-Fundstelle sind `[unverifiziert - prüfen]`; Verkündung war zum Stand 07/2026 nicht belegbar.

## Eingaben

- Unternehmensgröße (MA, Umsatz, Bilanzsumme – für KMU-Einstufung nach Empfehlung 2003/361/EG)
- Endenergieverbrauch des Unternehmens (GWh/a, gemittelt über drei Jahre)
- bestehende Zertifizierungen (ISO 50001, EMAS, ISO 14001)
- Konzernstruktur (verbundene Unternehmen für KMU-Berechnung)
- bisherige Energieaudits (Datum, Auditor, BAFA-Meldung)
- CSRD-Berichtspflicht (ja / nein / ab welchem Geschäftsjahr)
- Standort(e) der Betriebsgebäude und **Stand der kommunalen Wärmeplanung (WPG)** je Standort (Wärmeplan vorgelegt? ausgewiesenes Gebiet?)

## Sub-Agent-Architektur

Researcher liefert §§ 8, 12 EnEfG, § 8 EDL-G, KMU-Empfehlung 2003/361/EG, EU-Energieeffizienz-Richtlinie (RL (EU) 2023/1791), GEG-Schnittstellen sowie BAFA-Merkblätter und CSRD/ESRS-E1-Bezüge. Drafter erstellt im Behörden-/Memo-Stil eine Pflicht-Matrix mit konkretem To-Do und Nachweis-Anlagen. Reviewer prüft Schwellenwerte, Fristen und Sanktionsrisiken nach § 12 EnEfG / § 8 EDL-G.

## Ablauf

### 1. KMU-Einstufung als Vorfrage

Maßstab: **Empfehlung 2003/361/EG der Kommission** vom 06.05.2003. KMU = weniger als 250 Beschäftigte **und** (Umsatz ≤ 50 Mio. EUR **oder** Bilanzsumme ≤ 43 Mio. EUR), unter Einbeziehung **verbundener** und **Partnerunternehmen**.

Nicht-KMU sind **immer** auditpflichtig nach § 8 EDL-G (alle 4 Jahre), unabhängig von ihrem Energieverbrauch.

### 2. Energieaudit-Pflicht nach § 8 EDL-G

| Tatbestandsmerkmal | Inhalt |
|---|---|
| Adressat | Nicht-KMU iSd Empfehlung 2003/361/EG |
| Pflicht | Energieaudit nach DIN EN 16247-1 |
| Turnus | alle 4 Jahre |
| Befreiung | Wenn EnMS nach ISO 50001 oder UMS nach EMAS zertifiziert ist (§ 8 Abs. 3 EDL-G) |
| Nachweis | Meldung an BAFA über das Online-Portal; Aufbewahrung der Audit-Unterlagen |
| Sanktion | Bußgeld bis zu 50.000 EUR pro Verstoß (§ 12 EDL-G) `[unverifiziert – Höhe in aktueller Fassung prüfen]` |

### 3. EnMS-/UMS-Pflicht nach § 8 EnEfG

Mit Inkrafttreten des **Energieeffizienzgesetzes (EnEfG)** zum 18.11.2023 trifft Unternehmen mit einem **durchschnittlichen jährlichen Endenergieverbrauch > 7,5 GWh** in den vorangegangenen drei Kalenderjahren die Pflicht zur Einrichtung eines

- **Energiemanagementsystems** nach DIN EN ISO 50001 **oder**
- **Umweltmanagementsystems** nach EMAS-VO (VO (EG) 1221/2009).

Pflichtenkatalog (§ 8 Abs. 3, 4 EnEfG):

- Erfassung der Energieflüsse
- Identifikation der wesentlichen Energieverbraucher
- Bewertung wirtschaftlich zumutbarer Maßnahmen zur Endenergieeinsparung
- Veröffentlichung der durchführbaren Maßnahmen und der Umsetzungspläne

**Frist** für die Einrichtung: in der Regel 20 Monate ab Überschreitung der Schwelle bzw. Inkrafttreten `[unverifiziert – Übergangsfristen in aktueller Fassung prüfen]`.

### 4. Pflicht zur Umsetzung wesentlicher Maßnahmen

§ 9 EnEfG verpflichtet erfasste Unternehmen, **wesentliche Energieeffizienzmaßnahmen** zu erstellen, durch einen unabhängigen Auditor / einen Energiemanager bestätigen zu lassen und zu **veröffentlichen**. Es besteht **keine** unmittelbare Umsetzungspflicht, aber eine Begründungspflicht bei Nichtumsetzung wirtschaftlich zumutbarer Maßnahmen.

### 5. Schnittstelle GEG / kommunale Wärmeplanung (Gebäudeenergie)

Das **Gebäudeenergiegesetz (GEG)** regelt die Gebäudeeffizienz für Neubau und Bestand. Nach dem **GModG** (Bundestag 10.07.2026) gilt:

- **Anforderungen an den Primärenergiebedarf** — unverändert weitergeltend.
- **Energieausweis-Pflichten (§§ 79 ff. GEG)** — unverändert weitergeltend.
- **Keine 65 %-Vorgabe mehr für neue Heizungen.** §§ 71, 71b–71p und § 72 GEG sind gestrichen; ab **November 2026** gilt freie Heizungswahl. Gas- und Ölheizungen dürfen weiter eingebaut und betrieben werden.
- Stattdessen greifen **brennstoffseitige** Pflichten: **Bio-Anteil („Bio-Treppe") ab 01.01.2029**, **Quote für grünes Gas / grünes Heizöl ab 2028**, **Klimaneutralität aller Heizbrennstoffe bis 2045** `[unverifiziert - prüfen]` hinsichtlich der Ausgestaltung in der verkündeten Fassung.

**Prüfungsreihenfolge auf Gebäudeebene (neu):**

1. Standort bestimmen → zuständige Kommune.
2. **Kommunalen Wärmeplan nach dem WPG** abfragen: Frist **30.06.2026** für Kommunen > 100.000 Einwohner, **30.06.2028** für kleinere Kommunen.
3. Ausgewiesenes Gebiet feststellen (Wärmenetz / Wasserstoffnetz / dezentrale Versorgung) und daraus die konkreten Anforderungen und Anschlussperspektiven ableiten.
4. Erst danach die Investitionsentscheidung (Heizungstausch, Nah-/Fernwärmeanschluss, Wärmepumpe) treffen.

Die Schnittstelle zum EnEfG/EDL-G ist **kumulativ**, nicht alternativ: EnEfG/EDL-G erfasst den Unternehmensverbrauch insgesamt, GEG/WPG die Gebäudehülle, die Anlagentechnik und die standortbezogene Wärmeversorgung. **EnEfG und EDL-G sind vom GModG nicht berührt.**

### 6. Schnittstelle CSRD / ESRS E1

Unternehmen im Anwendungsbereich der Corporate Sustainability Reporting Directive (CSRD, RL (EU) 2022/2464) berichten nach dem Standard **ESRS E1 (Climate Change)**. Die ESRS-E1-Datenpunkte (Energieverbrauch nach Quellen, Energieintensität) überschneiden sich substanziell mit den Daten, die für ein EnMS / Energieaudit erhoben werden. **Empfehlung**: integrierte Datenerfassung, um Doppelarbeit zu vermeiden – die zwingenden Pflichten der jeweiligen Regimes bleiben aber eigenständig.

### 7. Befreiungs- und Erleichterungstatbestände

- ISO 50001 / EMAS befreit von Audit-Pflicht nach § 8 EDL-G (Abs. 3)
- vereinfachte Auditverfahren für Unternehmen unterhalb bestimmter Verbrauchsschwellen (§ 8 Abs. 4 EDL-G) `[unverifiziert – aktuelle Fassung prüfen]`
- KMU ist nicht audit-, aber gleichwohl ggf. anderen sektorspezifischen Pflichten unterworfen

### 8. Nachweisführung gegenüber BAFA

- Online-Portal des BAFA (Bundesamt für Wirtschaft und Ausfuhrkontrolle)
- Stichprobenkontrollen
- Aufbewahrung der Audit-Berichte / EnMS-Zertifikate für mindestens 10 Jahre
- Bei Verstoß: Anhörung, Bußgeldbescheid, Beschwerde nach OWiG-Vorschriften

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute und Verordnungen

- [§ 8 EnEfG](https://www.gesetze-im-internet.de/enefg/__8.html) (EnMS-/UMS-Pflicht ab 7,5 GWh/a)
- [§ 9 EnEfG](https://www.gesetze-im-internet.de/enefg/__9.html) (Wesentliche Effizienzmaßnahmen, Veröffentlichung)
- [§ 12 EnEfG](https://www.gesetze-im-internet.de/enefg/__12.html) (Bußgeldvorschriften)
- [§ 8 EDL-G](https://www.gesetze-im-internet.de/edl-g/__8.html) (Energieaudit für Nicht-KMU)
- [§ 12 EDL-G](https://www.gesetze-im-internet.de/edl-g/__12.html) (Bußgeldvorschriften)
- [GEG](https://www.gesetze-im-internet.de/geg/) (Gebäudeenergiegesetz, insb. §§ 79 ff. Energieausweis; **§§ 71, 71b–71p, 72 durch das GModG gestrichen**)
- Gebäudemodernisierungsgesetz (GModG), Beschluss des Bundestages vom **10.07.2026** (namentliche Abstimmung 323 : 271) — BGBl.-Fundstelle und Inkrafttreten `[unverifiziert - prüfen]`
- [WPG (Wärmeplanungsgesetz)](https://www.gesetze-im-internet.de/wpg/) (kommunale Wärmeplanung; Fristen 30.06.2026 / 30.06.2028)
- EU: [Empfehlung 2003/361/EG](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32003H0361) (KMU-Definition)
- EU: [RL (EU) 2023/1791](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32023L1791) (Energieeffizienz-RL Neufassung, EED)
- EU: [RL (EU) 2022/2464](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32022L2464) (CSRD)
- ESRS E1 (Climate Change), VO (EU) 2023/2772 `[unverifiziert]`

### Kommentare

- Reshöft/Schäfermeier, in: Theobald/Kühling, Energierecht (Loseblatt, Stand 2024), § 8 EDL-G Rn. 1 ff. `[unverifiziert]`
- Kommentierungen zum EnEfG sind noch im Aufbau; einschlägig ist die BAFA-Praxis und das BMWK-Merkblatt zum EnEfG `[unverifiziert]`

### Rechtsprechung und Behördenpraxis (`[unverifiziert – prüfen]`)

1. BAFA, Merkblatt zum Energieaudit nach EDL-G, Stand 2024 `[unverifiziert]`
2. BMWK, FAQ zum EnEfG, Stand 2024 `[unverifiziert]`
3. EuGH-Entscheidungen zur EED (RL 2012/27/EU, jetzt 2023/1791) – soweit auf die deutsche Umsetzung übertragbar `[unverifiziert]`

## Ausgabeformat

```
ÜBERSICHT — Energieeffizienzpflichten
Unternehmen: <anonymisiert>
KMU-Status: [ja / nein] (Begründung: MA, Umsatz, Bilanzsumme, Verbund)
Endenergieverbrauch (3-Jahres-Schnitt): <GWh/a>

I. Sachverhalt (knapp)
II. Pflicht-Matrix

   | Pflicht                     | Anwendbar? | Frist        | Nachweis    |
   |-----------------------------|-----------|--------------|-------------|
   | Energieaudit § 8 EDL-G      | ja/nein   | alle 4 Jahre | BAFA-Portal |
   | EnMS/UMS § 8 EnEfG          | ja/nein   | <Frist>      | Zertifikat  |
   | Wesentl. Maßnahmen § 9 EnEfG| ja/nein   | <Frist>      | Veröffentl. |
   | GEG (Gebäude)               | ja/nein   | ─            | Energieausw.|
   | Kommunaler Wärmeplan (WPG)  | ja/nein   | 30.06.2026 / 30.06.2028 | Wärmeplan Kommune |
   | CSRD / ESRS E1              | ja/nein   | ab GJ JJJJ   | Lagebericht |

   Hinweis: Die 65 %-Vorgabe des § 71 GEG ist durch das GModG (10.07.2026) gestrichen —
   nicht mehr prüfen. Maßgeblich ist der kommunale Wärmeplan am Standort.

III. Empfehlung
    – konkretes To-Do (Reihenfolge)
    – Befreiungstatbestände (ISO 50001 / EMAS)
    – integrierte Datenerfassung zur Vermeidung von Doppelarbeit

IV. Risiken / offene Punkte
    🟢 / 🟡 / 🔴 <Einstufung mit Begründung, insb. Sanktionsrisiko §§ 12 EnEfG, 12 EDL-G>

V. Quellenverzeichnis
```

## Beispiel (Memo-Stil, gekürzt)

> **Sachverhalt.** Mittelständisches Industrieunternehmen, ca. 600 Mitarbeitende, ca. 9 GWh/a Endenergieverbrauch (3-Jahres-Mittel), kein verbundenes Großunternehmen.
>
> **KMU-Status.** Mit 600 Beschäftigten kein KMU iSd Empfehlung 2003/361/EG (Schwelle: < 250 MA).
>
> **Energieaudit § 8 EDL-G.** Pflicht alle 4 Jahre, da Nicht-KMU. Befreit, wenn ISO 50001 oder EMAS implementiert sind (§ 8 Abs. 3 EDL-G).
>
> **EnMS/UMS § 8 EnEfG.** Pflicht zur Einrichtung eines EnMS nach ISO 50001 oder UMS nach EMAS, da der Endenergieverbrauch von 9 GWh/a die Schwelle von 7,5 GWh/a überschreitet. Frist: regelmäßig 20 Monate ab Überschreitung der Schwelle bzw. Inkrafttreten EnEfG `[unverifiziert – aktuelle Fassung prüfen]`.
>
> **Wesentliche Maßnahmen § 9 EnEfG.** Identifikation, Begutachtung, Veröffentlichung; Umsetzungspflicht nur, soweit wirtschaftlich zumutbar.
>
> **GEG-Schnittstelle.** Eigenständig zu prüfen (Energieausweis, Primärenergiebedarf). Für einen anstehenden Heizungstausch gilt **nicht mehr** die 65 %-Vorgabe des § 71 GEG — diese ist durch das GModG vom 10.07.2026 gestrichen. Maßgeblich ist der **kommunale Wärmeplan nach dem WPG** am Betriebsstandort; ist die Kommune > 100.000 Einwohner, lag der Plan zum 30.06.2026 vor und ist abzufragen. Brennstoffseitig sind Bio-Quote ab 2029 und Klimaneutralität bis 2045 einzupreisen `[unverifiziert - prüfen]`.
>
> **CSRD-Schnittstelle.** Falls die Mandantin in den Anwendungsbereich fällt, ESRS-E1-Datenpunkte integriert mit EnMS-Erhebung erheben.
>
> **Empfehlung.** Schrittfolge: (1) ISO 50001 implementieren → erfüllt sowohl EnEfG-EnMS- als auch EDL-G-Audit-Pflicht; (2) Audit-Bericht / Zertifikat über BAFA-Portal anzeigen; (3) wesentliche Maßnahmen veröffentlichen; (4) Datenharmonisierung mit CSRD-Berichterstattung. Risikoeinstufung 🟡 wegen Frist- und Sanktionsrisiko nach § 12 EnEfG `[unverifiziert – Höhe in aktueller Fassung prüfen]`.

## Risiken / typische Fehler

- **KMU-Status falsch berechnet** – verbundene Unternehmen / Partnerunternehmen nicht einbezogen, dadurch fälschlich KMU-Status angenommen.
- **EnEfG-Schwelle (7,5 GWh/a) gegen EDL-G-Audit-Schwelle vermischt** – das EDL-G knüpft an den Nicht-KMU-Status an, nicht an einen Energieverbrauch.
- **ISO 50001 / EMAS-Befreiung übersehen** – Doppelaufwand.
- **CSRD-Daten unabhängig vom EnMS erhoben** – Doppelarbeit, Inkonsistenzen zwischen Lagebericht und BAFA-Meldung.
- **Übergangsfristen EnEfG** unkritisch übernommen – die Geltung der 20-Monats-Frist ist bei jeder Anwendung mit `[unverifiziert – aktuelle Fassung prüfen]` zu kennzeichnen.
- **Sanktionshöhen** aus älterer Fassung übernommen – § 12 EnEfG / § 12 EDL-G in aktueller Bekanntmachung prüfen.
- **Mandant plant gegen aufgehobenes Recht (65 %-Regel)** – die schwerwiegendste Fehlerquelle: Beratung oder Investitionsplanung auf Basis des **gestrichenen § 71 GEG**. Die 65 %-Vorgabe für neue Heizungen existiert seit dem GModG (Bundestag 10.07.2026) nicht mehr; §§ 71, 71b–71p, 72 GEG sind entfallen. Wer sie weiter anwendet, erzeugt unnötige Investitionen und falsche Fördererwartungen.
- **Kommunalen Wärmeplan nicht abgefragt** – die Gebäudeebene knüpft nun standortbezogen an den Wärmeplan nach dem **WPG** an (Frist 30.06.2026 bei > 100.000 Einwohnern, sonst 30.06.2028). Ohne Abfrage lässt sich die Anschluss- und Investitionsperspektive nicht beurteilen.
- **Brennstoffpflichten übersehen** – die Entlastung ist nur anlagenseitig: **Bio-Anteilspflicht ab 01.01.2029**, Quote für grünes Gas/Heizöl ab 2028 und Klimaneutralität bis 2045 bleiben Kostentreiber einer weiterbetriebenen Gas-/Ölheizung.
- **GModG-Reichweite überdehnt** – das GModG ändert das **GEG**, nicht das **EnEfG** oder das **EDL-G**. EnMS-Pflicht (§ 8 EnEfG) und Audit-Pflicht (§ 8 EDL-G) bestehen unverändert fort.
- **Inkrafttreten als gesichert dargestellt** – Verkündung und Inkrafttretensdatum des GModG waren zum Stand 07/2026 nicht belegbar und sind mit `[unverifiziert - prüfen]` zu kennzeichnen.
