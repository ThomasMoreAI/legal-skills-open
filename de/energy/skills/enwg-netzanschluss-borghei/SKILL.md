---
name: enwg-netzanschluss-borghei
title: /energierecht:enwg-netzanschluss
description: Prüfung des Anschluss- und Versorgungsanspruchs nach §§ 17, 18 EnWG und des vorrangigen EEG-Anschlussregimes nach §§ 8, 10, 12 EEG inkl. Konfliktfälle (Kapazitätsmangel, Netzausbaupflicht), Anschlusszusage, Realisierungsplan und BNetzA-Beschlussverfahren nach §§ 31 ff. EnWG. Use when ein Anschlussbegehren (insb. EEG-Anlage) durch den Netzbetreiber verzögert, verweigert oder mit unzulässigen Auflagen versehen wird.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/energierecht/skills/enwg-netzanschluss
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: energy
language: de
---

# /energierecht:enwg-netzanschluss

## Zweck

Der Skill prüft, ob ein Anschlussbegehren – insbesondere für EEG-Anlagen – durchsetzbar ist, identifiziert das einschlägige Anschlussregime (allgemeiner Anspruch nach §§ 17, 18 EnWG vs. vorrangiger EEG-Anschluss nach §§ 8 ff. EEG), und bereitet die Argumentation gegenüber dem Netzbetreiber sowie ein etwaiges BNetzA-Beschlussverfahren (§§ 31 ff. EnWG) vor. Er adressiert die typischen Streitpunkte: Netzverknüpfungspunkt, Kapazitätsmangel, Kostentragung, Realisierungsfristen.

## Eingaben

- Anlagentyp und Leistung (PV, Wind, Biomasse, Speicher; kW/MW)
- Netzebene (Niederspannung, Mittelspannung, Hochspannung, Höchstspannung)
- Netzbetreiber (VNB / ÜNB) und bisheriger Schriftwechsel (Antrag, Anschlusszusage, Verweigerung)
- behaupteter Grund einer Verzögerung oder Verweigerung (insb. Kapazitätsmangel, technische Anforderungen)
- BImSchG-Genehmigungsstatus (bei Wind und Großanlagen)
- Position des Mandanten: Anlagenbetreiber, Letztverbraucher, Lieferant

## Sub-Agent-Architektur

Researcher liefert §§ 17, 18 EnWG, §§ 8, 10, 12 EEG, NAV/NDAV-Stellen, BNetzA-Festlegungen sowie BGH-KZR- und OLG-Düsseldorf-Rechtsprechung. Drafter erstellt im Gutachtenstil die Anspruchsprüfung, formuliert das Anschluss-/Auskunftsersuchen an den Netzbetreiber und bereitet den BNetzA-Antrag nach § 31 EnWG vor. Reviewer prüft, ob das Anschlussregime korrekt abgegrenzt ist, BImSchG-Genehmigung adressiert ist und Beschwerde-/Anhörungspflichten (§ 67 EnWG, § 75 EnWG) berücksichtigt sind.

## Ablauf

### 1. Abgrenzung des Anschlussregimes

Vor jeder Prüfung klären, welches Regime einschlägig ist:

| Sachverhalt | Regime | Norm |
|---|---|---|
| Letztverbraucher Niederspannung | Allgemeine Anschlusspflicht | § 18 EnWG iVm NAV |
| Letztverbraucher Mittel-/Hochspannung | Diskriminierungsfreier Netzzugang | § 17 EnWG; §§ 20 ff. EnWG |
| Anlage zur Erzeugung erneuerbarer Energie / KWK | Vorrangiger Anschluss nach EEG/KWKG | §§ 8, 10 EEG; § 3 KWKG |

Bei EEG-Anlagen gilt das **EEG-Regime vorrangig**: kürzester Netzverknüpfungspunkt, vorrangiger Anschluss, Abnahme- und Übertragungspflicht (§§ 8, 10 EEG), Netzausbaupflicht nach § 12 EEG.

### 2. Anspruchsvoraussetzungen nach §§ 17, 18 EnWG

§ 18 EnWG begründet den allgemeinen Anschlusspflichten gegenüber dem Grundversorger im Niederspannungsnetz. § 17 EnWG begründet einen diskriminierungsfreien Anschluss- und Netzzugangsanspruch im Übrigen. Voraussetzungen:

- **Anschlussfähigkeit** des Netzes (technisch und wirtschaftlich zumutbar)
- **Diskriminierungsfreiheit** (keine sachfremde Ungleichbehandlung)
- **Entgeltrahmen** nach StromNEV/GasNEV / NAV / NDAV

Ausnahmen / Verweigerungsgründe sind in § 17 Abs. 2 EnWG abschließend geregelt; die Darlegungs- und Beweislast trägt der Netzbetreiber.

### 3. Vorrangiger Anschluss nach §§ 8 ff. EEG

Der Netzbetreiber ist verpflichtet, eine EEG-Anlage **unverzüglich und vorrangig** an den **technisch geeigneten Netzverknüpfungspunkt** mit dem **kürzesten Entfernungsweg** anzuschließen (§ 8 Abs. 1 EEG). Die Kosten des **Anschlusses** trägt der Anlagenbetreiber bis zum Verknüpfungspunkt; die Kosten des **Netzausbaus** trägt der Netzbetreiber (§ 16 EEG, § 12 EEG).

Zentrale Verfahrenspflichten des Netzbetreibers (§ 8 Abs. 5, 6 EEG):

- **Zeitplan** für den Anschluss innerhalb von 8 Wochen nach Antrag
- **Konkretes Anschlussangebot** mit Netzverknüpfungspunkt und Kostenschätzung
- Bei Streit über den Verknüpfungspunkt: Pflicht zur Erstellung einer **Vergleichsberechnung** auf Verlangen des Betreibers

### 4. Konfliktfall Kapazitätsmangel

Wendet der Netzbetreiber Kapazitätsmangel ein, ist zu unterscheiden:

- **§ 12 EEG (Netzausbaupflicht)** – der Netzbetreiber muss sein Netz **optimieren, verstärken und ausbauen**, soweit dies wirtschaftlich zumutbar ist. Eine Anschlussverweigerung wegen fehlender Kapazität setzt voraus, dass auch der Ausbau wirtschaftlich unzumutbar wäre.
- **§ 11 EnWG (Sicherheit und Zuverlässigkeit)** – betrifft den Betrieb, nicht den Anschluss; rechtfertigt keine generelle Anschlussverweigerung.
- **Einspeisemanagement nach § 13 EnWG / § 14 EEG** ist die mildere Maßnahme gegenüber der Anschlussverweigerung.

Die h.M. (vgl. **Frenz/Müggenborg**, EEG, § 12 Rn. 1 ff. `[unverifiziert]`) versteht § 12 EEG als spezialgesetzliche Konkretisierung des § 11 EnWG für EEG-Anlagen.

### 5. Anschlusszusage und Realisierungsplan

- Anschlusszusage als verbindliches Angebot des Netzbetreibers; Annahme durch den Anlagenbetreiber begründet einen Anschlussvertrag.
- Realisierungsfristen nach § 27a EEG (Pönalen bei Nichtinbetriebnahme nach Zuschlag).
- BImSchG-Genehmigungsbedürftigkeit bei Wind/Großanlagen ist Vorfrage; ohne bestandskräftige (oder zumindest sofort vollziehbare) Genehmigung idR kein durchsetzbarer Anschlussanspruch.

### 6. BNetzA-Beschlussverfahren §§ 31 ff. EnWG

Bei Streit über Anschluss, Netzzugang, Netzentgelte oder Verweigerung steht das **Beschlussverfahren** der BNetzA offen (§ 31 EnWG). Der Antrag enthält:

- Tatsachenvortrag mit Belegen (Schriftwechsel, Anschlussantrag, Verweigerungsbegründung)
- konkreter Antrag (z. B. Anordnung des Anschlusses, Festsetzung des Netzverknüpfungspunktes)
- Begründung mit Anspruchsgrundlage
- Anhörungsrecht aller Beteiligten (§ 67 EnWG)

Gegen den Beschluss ist **Beschwerde zum OLG Düsseldorf** binnen eines Monats statthaft (§ 75 EnWG).

Alternativ bei Verbrauchersachen: **Schlichtungsstelle Energie** (§ 111b EnWG) als außergerichtliches Schlichtungsverfahren.

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute und Verordnungen

- [§ 1 EnWG](https://www.gesetze-im-internet.de/enwg_2005/__1.html) (Zwecke)
- [§ 17 EnWG](https://www.gesetze-im-internet.de/enwg_2005/__17.html) (Netzanschluss, Diskriminierungsverbot)
- [§ 18 EnWG](https://www.gesetze-im-internet.de/enwg_2005/__18.html) (Allgemeine Anschlusspflicht)
- [§§ 20–35 EnWG](https://www.gesetze-im-internet.de/enwg_2005/) (Netzzugang)
- [§ 31 EnWG](https://www.gesetze-im-internet.de/enwg_2005/__31.html) (BNetzA-Beschlussverfahren)
- [§ 67 EnWG](https://www.gesetze-im-internet.de/enwg_2005/__67.html) (Anhörung)
- [§ 75 EnWG](https://www.gesetze-im-internet.de/enwg_2005/__75.html) (Beschwerde zum OLG Düsseldorf)
- [§ 8 EEG](https://www.gesetze-im-internet.de/eeg_2014/__8.html) (Anschluss EEG-Anlagen)
- [§ 10 EEG](https://www.gesetze-im-internet.de/eeg_2014/__10.html) (Abnahme, Übertragung, Verteilung)
- [§ 12 EEG](https://www.gesetze-im-internet.de/eeg_2014/__12.html) (Netzausbaupflicht)
- [§ 16 EEG](https://www.gesetze-im-internet.de/eeg_2014/__16.html) (Kostentragung Anschluss/Ausbau)
- [NAV](https://www.gesetze-im-internet.de/nav/) (Niederspannungsanschlussverordnung)
- [NDAV](https://www.gesetze-im-internet.de/ndav/) (Niederdruckanschlussverordnung)
- EU: [RL (EU) 2019/944](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019L0944) (Strombinnenmarkt-RL), [VO (EU) 2019/943](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019R0943) (Strombinnenmarkt-VO), [RED III](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32023L2413) (RL (EU) 2023/2413)

### Kommentare

- Hartmann, in: Säcker, BerlKomm Energierecht, 4. Aufl. 2019, § 17 EnWG Rn. 1 ff. `[unverifiziert]`
- Salje, in: Theobald/Kühling, Energierecht (Loseblatt, Stand 2024), § 8 EEG Rn. 1 ff. `[unverifiziert]`
- Britz/Hellermann/Hermes, EnWG, 3. Aufl. 2015, § 17 Rn. 1 ff. `[unverifiziert]`
- Müggenborg, in: Frenz/Müggenborg, EEG, 6. Aufl. 2023, § 12 Rn. 1 ff. `[unverifiziert]`

### Rechtsprechung und Behördenpraxis (`[unverifiziert – prüfen in juris / bundesnetzagentur.de]`)

1. BGH, Urt. v. 18.11.2008 – KZR 17/07, RdE 2009, 184 (Anschluss EEG-Anlage, kürzester Verknüpfungspunkt) — in dejure.org weder unter Datum + Aktenzeichen noch über die Aktenzeichen-Suche auffindbar; Senatszuordnung (KZR statt VIII ZR) und Fundstelle sind vor jeder Verwendung zu prüfen `[unverifiziert – Aktenzeichen nicht belegbar]`
2. OLG Düsseldorf, Beschl. v. – VI-3 Kart Az. (Beschwerde gegen BNetzA-Beschluss zum Netzanschluss) `[unverifiziert]`
3. BNetzA, Festlegung BK6 zu Anschluss- und Verteilfragen `[unverifiziert]`

## Ausgabeformat

```
GUTACHTEN — Netzanschluss nach EnWG / EEG
Anlage: <Typ, Leistung, Standort (anonymisiert)>
Netzbetreiber: <VNB/ÜNB>

I. Sachverhalt (knapp)
II. Frage(n)
III. Kurzantwort
    – Anschlussanspruch: [ja / nein / nur nach Ausbau]
    – Empfehlung: [BNetzA-Antrag / Schlichtungsstelle / Anschlussvertrag prüfen]

IV. Rechtliche Bewertung
    1. Anschlussregime
       (allgemein § 18 EnWG / Netzzugang § 17 EnWG / EEG-vorrangig §§ 8 ff. EEG)
    2. Anspruchsvoraussetzungen
       a) Anschlussfähigkeit / Diskriminierungsfreiheit
       b) Netzverknüpfungspunkt (kürzester Entfernungsweg)
       c) Kostentragung Anschluss vs. Ausbau (§ 16 EEG)
    3. Konfliktpunkt
       a) Kapazitätsmangel – Netzausbaupflicht § 12 EEG vs. § 11 EnWG
       b) Einspeisemanagement als mildere Maßnahme
       c) BImSchG-Genehmigungsstatus als Vorfrage
    4. Verfahren
       a) Anschluss- und Auskunftsersuchen an Netzbetreiber
       b) BNetzA-Beschlussverfahren § 31 EnWG, Anhörung § 67 EnWG
       c) Beschwerde OLG Düsseldorf § 75 EnWG (Frist: 1 Monat)
       d) ggf. Schlichtungsstelle Energie § 111b EnWG

V. Entwurf
    a) Schreiben an Netzbetreiber (Frist, Anspruchsgrundlage, Beweisangebote)
    b) ggf. Antrag § 31 EnWG (Tatsachen → Antrag → Begründung)

VI. Risiken / offene Punkte
    🟢 / 🟡 / 🔴 <Einstufung mit Begründung>
    Offene Tatsachen: IBN-Datum, BImSchG-Status, Kapazitätsnachweis VNB

VII. Quellenverzeichnis
```

## Beispiel (Gutachtenstil, gekürzt)

> **Sachverhalt.** Die Mandantin plant eine Freiflächen-PV-Anlage mit 12 MWp im Mittelspannungsnetz. Der VNB hat den Anschluss unter Verweis auf fehlende Kapazität verweigert und auf eine Wartezeit von 36 Monaten verwiesen.
>
> **Anspruchsgrundlage.** Der Anschlussanspruch folgt aus § 8 Abs. 1 EEG: Der Netzbetreiber ist verpflichtet, eine EEG-Anlage unverzüglich und vorrangig am technisch geeigneten Verknüpfungspunkt anzuschließen. § 17 EnWG ist daneben nicht eröffnet, da § 8 EEG lex specialis ist (vgl. Müggenborg, in: Frenz/Müggenborg, EEG, 6. Aufl. 2023, § 8 Rn. 1 ff. `[unverifiziert]`).
>
> **Kapazitätsmangel.** Der Einwand fehlender Kapazität rechtfertigt für sich genommen keine Anschlussverweigerung. § 12 EEG begründet eine Netzausbaupflicht des Netzbetreibers, soweit der Ausbau wirtschaftlich zumutbar ist. § 11 EnWG (Sicherheit, Zuverlässigkeit) betrifft den Netzbetrieb, nicht den Anschluss. Die Darlegungs- und Beweislast für die wirtschaftliche Unzumutbarkeit trägt der Netzbetreiber.
>
> **Ergebnis.** Anschlussanspruch dem Grunde nach 🟢. Empfehlung: schriftliche Aufforderung zur Vorlage einer Kapazitäts- und Ausbauberechnung binnen vier Wochen; bei Verweigerung Antrag auf Beschlussverfahren nach § 31 EnWG bei der BK6 der BNetzA. Beschwerde zum OLG Düsseldorf nach § 75 EnWG bleibt vorbehalten (Frist: 1 Monat ab Zustellung des Beschlusses). 🟡 hinsichtlich Realisierungszeitpunkt, da Netzausbau erfahrungsgemäß 12–24 Monate Verfahrensdauer beansprucht.

## Risiken / typische Fehler

- **Falsches Anschlussregime gewählt** (§ 17 EnWG statt § 8 EEG) – Anspruchsgrundlage greift zu kurz, Vorranganspruch geht verloren.
- **Netzverknüpfungspunkt unkritisch übernommen** – ohne Vergleichsberechnung nach § 8 Abs. 5, 6 EEG drohen unnötige Anschlusskosten.
- **Kapazitätsmangel ungeprüft akzeptiert** – Netzausbaupflicht § 12 EEG bleibt unbeachtet.
- **BImSchG-Genehmigung nicht geklärt** – ohne (sofort vollziehbare) Genehmigung kein durchsetzbarer Anschluss bei Wind/Großanlagen.
- **Beschwerdefrist § 75 Abs. 4 EnWG (1 Monat) versäumt** – BNetzA-Beschluss wird bestandskräftig.
- **Vermischung mit Energiekartellrecht** (§§ 19, 29 GWB iVm § 30 EnWG) – gehört in das Plugin `kartellrecht`, hier nur Hinweis-Schnittstelle.
