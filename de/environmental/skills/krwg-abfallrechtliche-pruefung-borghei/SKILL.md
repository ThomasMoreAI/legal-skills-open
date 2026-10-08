---
name: krwg-abfallrechtliche-pruefung-borghei
title: /umweltrecht:krwg-abfallrechtliche-pruefung
description: Abfallrechtliche Prüfung nach KrWG – Abfallbegriff § 3 (objektiv/subjektiv), Abfallhierarchie § 6, Getrennthaltungsgebot § 14, Produktverantwortung §§ 23 ff., Überlassungspflicht § 17, Anzeige- und Erlaubnispflicht §§ 53/54, behördliche Überwachung und Sanktionen § 47. Use when ein Betrieb Abfälle einstuft, eine Anordnung der Abfallbehörde erhalten hat oder Anzeige-/Erlaubnispflichten geprüft werden müssen.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/umweltrecht/skills/krwg-abfallrechtliche-pruefung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: environmental
language: de
---

# /umweltrecht:krwg-abfallrechtliche-pruefung

## Zweck

Das KrWG steuert den Lebenszyklus von Abfall — Vermeidung, Verwertung, Beseitigung — und legt Pflichten für Erzeuger, Besitzer, Beförderer, Händler und Entsorger fest. Wirksam ist eine abfallrechtliche Maßnahme nur, wenn der Abfallbegriff (§ 3 KrWG) korrekt erfüllt ist und die Stufe der Abfallhierarchie (§ 6 KrWG) richtig zugeordnet wurde. Dieser Skill prüft die Einstufung, Pflichtenkette und etwaige Anordnungen.

## Eingaben

- Stoffliche Beschreibung des Materials (Herkunft, Zusammensetzung, Aggregatzustand)
- Verwendungszweck und Zukunft des Materials
- Rolle des Mandanten (Erzeuger, Besitzer, Beförderer, Sammler, Händler, Entsorger)
- Etwaiger Anordnungs- oder Bußgeldbescheid
- Anzeige- / Erlaubnislage (Nummer, Datum, Behörde)

## Sub-Agent-Architektur

Researcher liefert KrWG-Normen, AbfRRL-Bezug, einschlägige BVerwG-/EuGH-Rspr. zum Abfall-/Nebenproduktbegriff. Drafter prüft Abfallbegriff vor Hierarchie vor Pflicht; bei Anordnung: Ermächtigungsgrundlage § 47 KrWG, Tatbestand, Ermessen, Verhältnismäßigkeit. Reviewer prüft Anhörung § 28 VwVfG, Anzeige-/Erlaubnis-Konstellation und Sanktionen.

## Ablauf

### 1. Abfallbegriff § 3 KrWG

| Tatbestand | Norm | Prüfung |
|---|---|---|
| **Stoff oder Gegenstand** | § 3 Abs. 1 S. 1 KrWG | körperlich abgrenzbar |
| **Entledigung** | § 3 Abs. 2–4 KrWG | objektiv (Zuführung zu Verwertung/Beseitigung, Wegfall ursprüngl. Verwendung) oder subjektiv (Entledigungswille) |
| **Nebenprodukt** | § 4 KrWG | vier kumulative Voraussetzungen: weitere Verwendung sicher, ohne weitere Verarbeitung, integraler Bestandteil Herstellungsprozess, rechtmäßig |
| **Ende der Abfalleigenschaft** | § 5 KrWG | Verwertungsverfahren durchlaufen + Marktbedingungen erfüllt |

Maßstab: EuGH, Urt. v. 15.06.2000 – C-418/97 und C-419/97 (ARCO Chemie), Slg. 2000, I-4475 `[unverifiziert – prüfen]`.

### 2. Abfallhierarchie § 6 KrWG

| Stufe | Inhalt |
|---|---|
| 1. Vermeidung | § 7 i. V. m. § 13 KrWG |
| 2. Vorbereitung zur Wiederverwendung | § 3 Abs. 24 KrWG |
| 3. Recycling | stofflich |
| 4. Sonstige Verwertung | thermisch, Verfüllung |
| 5. Beseitigung | Deponie, Verbrennung ohne Energierückgewinnung |

Abweichung nur nach § 6 Abs. 2 KrWG (Lebenszyklusbetrachtung).

### 3. Getrennthaltungsgebot § 14 KrWG

- Pflicht zur getrennten Sammlung, soweit erforderlich und technisch/wirtschaftlich zumutbar
- Ausnahmen § 9 Abs. 3 KrWG (Vermischungsverbot mit gefährlichen Abfällen → § 9 KrWG)
- Gewerbeabfallverordnung (GewAbfV) konkretisiert für gewerbliche Siedlungsabfälle

### 4. Pflichten der Akteure

| Akteur | Pflicht |
|---|---|
| **Erzeuger/Besitzer** | [§ 7 KrWG](https://www.gesetze-im-internet.de/krwg/__7.html) Verwertung, [§ 15 KrWG](https://www.gesetze-im-internet.de/krwg/__15.html) Beseitigung |
| **Überlassung an ÖrE** | [§ 17 KrWG](https://www.gesetze-im-internet.de/krwg/__17.html) bei Haushalten und gewerblichen Siedlungsabfällen |
| **Beförderer/Sammler/Händler/Makler** | [§§ 53, 54 KrWG](https://www.gesetze-im-internet.de/krwg/__53.html) Anzeige- bzw. Erlaubnispflicht; gefährliche Abfälle: Erlaubnis |
| **Produktverantwortung** | [§§ 23–25 KrWG](https://www.gesetze-im-internet.de/krwg/__23.html) plus VerpackG, ElektroG, BattG |
| **Entsorgungsfachbetrieb** | [§ 56 KrWG](https://www.gesetze-im-internet.de/krwg/__56.html), Zertifizierung |

### 5. Behördliche Überwachung und Anordnung § 47 KrWG

- **Ermächtigungsgrundlage** § 47 Abs. 1 KrWG für Anordnungen zur Erfüllung der KrWG-Pflichten
- **Tatbestand**: Verstoß gegen KrWG-Pflicht (z. B. § 14 Getrennthaltung, § 17 Überlassung)
- **Ermessen**: § 40 VwVfG, Verhältnismäßigkeit (geeignet, erforderlich, angemessen)
- **Anhörung**: § 28 VwVfG zwingend
- **Sofortvollzug** § 80 Abs. 2 Nr. 4 VwGO: gesondertes besonderes öffentliches Interesse, schriftlich zu begründen

### 6. Sanktionen

- Bußgeld [§ 69 KrWG](https://www.gesetze-im-internet.de/krwg/__69.html) bis 100.000 EUR (bei vorsätzlichen Verstößen gegen § 17 KrWG-Überlassungspflicht)
- Strafbarkeit § 326 StGB (unerlaubter Umgang mit Abfällen)

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute

- [§ 3 KrWG](https://www.gesetze-im-internet.de/krwg/__3.html) (Abfallbegriff)
- [§ 4 KrWG](https://www.gesetze-im-internet.de/krwg/__4.html) (Nebenprodukt)
- [§ 5 KrWG](https://www.gesetze-im-internet.de/krwg/__5.html) (Ende der Abfalleigenschaft)
- [§ 6 KrWG](https://www.gesetze-im-internet.de/krwg/__6.html) (Abfallhierarchie)
- [§ 7 KrWG](https://www.gesetze-im-internet.de/krwg/__7.html) (Grundpflichten Verwertung)
- [§ 14 KrWG](https://www.gesetze-im-internet.de/krwg/__14.html) (Getrennthaltung)
- [§ 17 KrWG](https://www.gesetze-im-internet.de/krwg/__17.html) (Überlassungspflicht)
- [§§ 23–25 KrWG](https://www.gesetze-im-internet.de/krwg/__23.html) (Produktverantwortung)
- [§ 47 KrWG](https://www.gesetze-im-internet.de/krwg/__47.html) (Überwachung / Anordnung)
- [§§ 53, 54 KrWG](https://www.gesetze-im-internet.de/krwg/__53.html) (Anzeige / Erlaubnis)
- [§ 69 KrWG](https://www.gesetze-im-internet.de/krwg/__69.html) (Bußgeld)
- [GewAbfV](https://www.gesetze-im-internet.de/gewabfv_2017/)
- [AbfRRL 2008/98/EG](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32008L0098)

### Kommentare

- Schink/Versteyl, KrWG, 2. Aufl. 2016, § 3 Rn. 1 ff., § 6 Rn. 1 ff., § 14 Rn. 1 ff.
- Petersen/Doumet, in: Landmann/Rohmer, Umweltrecht (Loseblatt, Stand: 2024), § 3 KrWG Rn. 50 ff.
- Versteyl, in: Versteyl/Mann/Schomerus, KrWG, 4. Aufl. 2019, § 47 Rn. 10 ff. (Anordnungsbefugnis)
- Frenz, KrWG, 2017, § 17 Rn. 1 ff. (Überlassungspflicht)

### Rechtsprechung (`[unverifiziert – prüfen in Beck-Online/juris]`)

1. EuGH, Urt. v. 15.06.2000 – C-418/97 und C-419/97 (ARCO Chemie), Slg. 2000, I-4475 (Entledigungsbegriff) `[unverifiziert – prüfen]`
2. EuGH, Urt. v. 18.04.2002 – C-9/00 (Palin Granit), Slg. 2002, I-3533 (Nebenprodukt) `[unverifiziert – prüfen]`
3. BVerwG, Urt. v. 01.12.2005 – 10 C 4/04, NVwZ 2006, 589 (subjektiver Abfallbegriff) `[unverifiziert – prüfen]`
4. BVerwG, Urt. v. 18.06.2009 – 7 C 16/08, NVwZ 2009, 1432 (Überlassungspflicht § 17) `[unverifiziert – prüfen]`

## Ausgabeformat

```
GUTACHTEN — Abfallrechtliche Prüfung
<Mandat-Kürzel> — <Datum>

I.   Sachverhalt
     Material: <…>
     Rolle: <Erzeuger / Besitzer / Beförderer / Händler / Entsorger>
     Anordnung / Bescheid: <Datum, Az., Behörde>

II.  Frage(n)
     1. Liegt Abfall i. S. d. § 3 KrWG vor? Oder Nebenprodukt § 4?
     2. Welche Hierarchiestufe § 6 KrWG ist einschlägig?
     3. Welche Pflichten treffen den Mandanten?
     4. (Falls Bescheid) Ist die Anordnung nach § 47 KrWG rechtmäßig?

III. Kurzantwort
     <ein Satz>

IV.  Rechtliche Bewertung (Gutachtenstil)
     1. Abfallbegriff § 3 KrWG
        - objektive Entledigung
        - subjektive Entledigung
        - Abgrenzung Nebenprodukt § 4 KrWG (vier Kriterien)
     2. Abfallhierarchie § 6 KrWG
        - Einordnung; Abweichung § 6 Abs. 2
     3. Pflichten
        - § 7 / § 14 / § 17 KrWG
        - Anzeige § 53 / Erlaubnis § 54
        - Produktverantwortung §§ 23 ff. (soweit einschlägig)
     4. (Falls Bescheid) Anordnung § 47 KrWG
        - Ermächtigungsgrundlage
        - Tatbestand
        - Ermessen § 40 VwVfG
        - Verhältnismäßigkeit
        - Anhörung § 28 VwVfG
        - Sofortvollzug § 80 Abs. 2 Nr. 4 VwGO

V.   Gesamtergebnis
     <…>

VI.  Risiken / offene Punkte
     - Analytik des Materials (Schadstoffe, Gefährlichkeit)
     - Sanktionsrisiko § 69 KrWG / § 326 StGB
     - Klage- / Widerspruchsfrist

VII. Risikoeinstufung
     [🟢 / 🟡 / 🔴]

VIII. Quellenverzeichnis
     <gem. zitierweise.md>
```

## Risiken / typische Fehler

- **Nebenprodukt vorschnell bejaht** → wenn auch nur eine der vier Voraussetzungen § 4 KrWG fehlt, bleibt Abfall.
- **Hierarchiestufe „Verwertung" pauschal angenommen** ohne § 6 Abs. 2 KrWG-Begründung → Ermessensfehler.
- **Überlassungspflicht § 17 KrWG** für gewerbliche Siedlungsabfälle übersehen → Bußgeld.
- **Anhörung § 28 VwVfG vor Anordnung** fehlt → formelle Rechtswidrigkeit.
- **Sofortvollzug § 80 Abs. 2 Nr. 4 VwGO** ohne tragende Begründung → Antrag nach § 80 Abs. 5 VwGO erfolgreich.
- **Ende der Abfalleigenschaft § 5 KrWG** ohne durchlaufenes Verwertungsverfahren behauptet → unwirksam.
