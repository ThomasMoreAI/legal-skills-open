---
name: marktbeherrschung-bewertung-borghei
title: /kartellrecht:marktbeherrschung-bewertung
description: Prüfung einer Marktbeherrschung und eines Missbrauchs nach §§ 18, 19, 19a, 20 GWB / Art. 102 AEUV – Marktabgrenzung sachlich/räumlich/zeitlich (Bedarfsmarktkonzept, SSNIP-Test), Marktanteilsvermutung § 18 IV GWB, Behinderungs- und Ausbeutungsmissbrauch, strukturmarktrelevante Plattformen § 19a GWB, relative Marktmacht § 20 GWB, objektive Rechtfertigung. Use when ein Mandant ein marktstarkes Unternehmen ist oder einem solchen ausgesetzt ist und sein Verhalten auf Missbrauch geprüft werden soll.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/kartellrecht/skills/marktbeherrschung-bewertung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: antitrust
language: de
---

# /kartellrecht:marktbeherrschung-bewertung

## Zweck

Der Skill prüft, ob ein Unternehmen marktbeherrschend iSv § 18 GWB bzw. Art. 102 AEUV ist und ob ein konkretes Verhalten einen **Missbrauch** darstellt — Behinderungs-, Ausbeutungs- oder Diskriminierungsmissbrauch sowie Sondertatbestände § 19 II Nr. 1–5 GWB. Er erfasst zugleich die jüngeren Verschärfungen für digitale Plattformen über § 19a GWB (überragende marktübergreifende Bedeutung) und die relative Marktmacht § 20 GWB ggü. kleinen und mittleren Unternehmen. Maßstab ist Marktabgrenzung → Marktstellung → Missbrauchstatbestand → objektive Rechtfertigung.

## Eingaben

- Verhaltensbeschreibung (Ausbeutung — Preise/Konditionen; Behinderung — Lieferverweigerung, Zugangsverweigerung, Kampfpreis, Marge-Squeeze, Kopplung, Bündelung, Self-Preferencing; Diskriminierung; Anzapfen)
- betroffenes Unternehmen und Marktstellung (Marktanteil, Umsätze, Marktstrukturindikatoren)
- abgegrenzter sachlicher / räumlicher Markt (sofern verfügbar)
- ggf. Hinweise auf BKartA-Verfahren / KOM-Verfahren / § 19a-Adressatschaft
- Position des Mandanten: marktstarkes Unternehmen, das sich rechtfertigen muss, oder geschädigtes Unternehmen

## Sub-Agent-Architektur

Researcher liefert §§ 18, 19, 19a, 20, 21 GWB, Art. 102 AEUV, KOM-Markt-Mitteilung, EuGH-Leitentscheidungen (Hoffmann-La Roche, United Brands, AKZO, Deutsche Telekom, Intel, Google Shopping), BGH-Kartellsenat-Rspr. und BKartA-Beschlüsse (Facebook, Amazon, Apple, Google, Meta § 19a). Drafter prüft Markt → Marktstellung → Missbrauch → Rechtfertigung. Reviewer prüft saubere Marktabgrenzung, korrekte Marktanteilsvermutung, vollständige Tatbestandsprüfung und Rechtfertigungs-Analyse.

## Ablauf

### 1. Marktabgrenzung

- **Sachlich**: Bedarfsmarktkonzept — funktionelle Austauschbarkeit aus Sicht der Marktgegenseite. SSNIP-Test als ökonomische Hilfsmethode (hypothetische Preiserhöhung 5–10 %).
- **Räumlich**: Gebiet, in dem die Wettbewerbsbedingungen hinreichend homogen sind (national, regional, EWR, weltweit; bei digitalen Märkten häufig EWR).
- **Zeitlich**: ggf. Saisonalität, Produktlebenszyklus, Innovationsmärkte.

Maßstab: KOM, Bekanntmachung über die Definition des relevanten Marktes (ABl. 1997 C 372/5; [Neufassung 2024 (C/2024/1645)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=OJ:C_202401645)).

### 2. Marktbeherrschende Stellung

- **§ 18 I GWB**: keine Wettbewerber, kein wesentlicher Wettbewerb, oder überragende Marktstellung; **§ 18 III** Kriterien (Marktanteil, Finanzkraft, Zugang zu Beschaffungs-/Absatzmärkten, Verflechtungen, Markteintrittsschranken, tatsächlicher/potenzieller Wettbewerb).
- **Marktanteilsvermutung § 18 IV GWB**: **≥ 40 %** bei einem Unternehmen; **gemeinsame** Marktbeherrschung bei **≥ 50 %** dreier oder weniger Unternehmen bzw. ≥ 2/3 fünfer oder weniger Unternehmen (§ 18 VI).
- **§ 18 IIIa GWB**: Multi-sided-Markets-Kriterien (Netzwerkeffekte, parallele Nutzung mehrerer Dienste, Skalenvorteile aus Datenzugang, Innovationsdruck).
- **§ 19a GWB**: das BKartA stellt durch Verfügung **überragende marktübergreifende Bedeutung** fest (Voraussetzung Adressat-Eigenschaft); danach kann das BKartA bestimmte Verhaltensweisen (Self-Preferencing, Behinderung Mehrkanalvertrieb, datengetriebene Vorteile, Konditionen für Vorinstallation, Behinderung Interoperabilität) untersagen, ohne klassische Marktabgrenzung im Einzelfall durchführen zu müssen. [Verfahren seit 2022](https://www.bundeskartellamt.de/DE/DigitalWirtschaft/VerfahrenGegenGrosseDigitalkonzerne/verfahrengegengrossedigitalkonzerne_node.html) gegen Amazon, Apple, Google/Alphabet, Meta.
- **§ 20 GWB** (relative oder überlegene Marktmacht): Schutz von kleinen und mittleren Unternehmen, die von einem Anbieter/Nachfrager abhängig sind; gleichgestellt mit Marktbeherrschern für Diskriminierungs- und Behinderungsverbot.
- **§ 21 GWB**: Boykott- und Druckausübungsverbot.

### 3. Missbrauchstatbestände § 19 GWB / Art. 102 AEUV

| Kategorie | Beispiele | § 19 II GWB | Art. 102 AEUV |
|---|---|---|---|
| Behinderungs- / Diskriminierungsmissbrauch | Lieferverweigerung, Zugangsverweigerung zu Essential Facility, Kampfpreis, Marge-Squeeze, Self-Preferencing | Nr. 1 | lit. b, c |
| Ausbeutungsmissbrauch | überhöhte Preise / unangemessene Konditionen (Vergleichsmarktanalyse) | Nr. 2 | lit. a |
| Diskriminierungsverbot | Ungleichbehandlung ohne sachlichen Grund | Nr. 3 | lit. c |
| Essential Facility / Netzzugang | Verweigerung des Zugangs zu unverzichtbarer Infrastruktur | Nr. 4 | (über lit. b und Bronner-Linie) |
| Anzapfverbot | unangemessenes Verlangen von Vorteilen ohne sachliche Rechtfertigung | Nr. 5 | (nicht direkt) |

Spezialthemen:

- **Kampfpreis** (predatory pricing): AKZO-Schwelle — Preis unter durchschnittlich variablen Kosten = vermutet missbräuchlich; zwischen variabler und durchschnittlich vermeidbarer/Gesamtkosten = bei Verdrängungsabsicht missbräuchlich (EuGH, Urt. v. 03.07.1991 – Rs. C-62/86, AKZO Chemie ./. Kommission, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=1991-07-03&Aktenzeichen=C-62/86)).
- **Marge-Squeeze**: vertikal integriertes Unternehmen mit Marktbeherrschung im Vorleistungsmarkt setzt Vorleistungspreise so, dass eigener Endkundenpreis für Wettbewerber unrentabel wird (EuGH, Urt. v. 14.10.2010 – C-280/08 P, Deutsche Telekom ./. Kommission, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2010-10-14&Aktenzeichen=C-280/08)).
- **Treuerabatte / loyalitätsfördernde Rabatte**: Intel-Rechtsprechung — Effekt-Analyse erforderlich (EuGH, Urt. v. 06.09.2017 – C-413/14 P, Intel ./. Kommission, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2017-09-06&Aktenzeichen=C-413/14)).
- **Self-Preferencing** durch Plattformen: Google Shopping (EuG, Urt. v. 10.11.2021 – T-612/17, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuG&Datum=2021-11-10&Aktenzeichen=T-612/17); im Rechtsmittel bestätigt durch EuGH, Urt. v. 10.09.2024 – C-48/22 P, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2024-09-10&Aktenzeichen=C-48/22)); zusätzlich § 19a Nr. 1 GWB.
- **Daten- und Konditionenmissbrauch**: BKartA-Verfahren Facebook ([B6-22/16](https://www.bundeskartellamt.de/SharedDocs/Entscheidung/DE/Entscheidungen/Missbrauchsaufsicht/2019/B6-22-16.html)); BGH-Bestätigung; EuGH, Urt. v. 04.07.2023 – C-252/21, Meta Platforms u.a., [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2023-07-04&Aktenzeichen=C-252/21).

### 4. Objektive Rechtfertigung und Effizienzverteidigung

Auch missbräuchlich erscheinendes Verhalten kann gerechtfertigt sein durch:

- **objektive Rechtfertigung** (z. B. Sicherheit, Qualität, Gesundheit, IP-Rechte) — Verhältnismäßigkeit erforderlich;
- **Effizienzeinwand** (analog Art. 101 III AEUV-Kriterien; vom marktbeherrschenden Unternehmen zu belegen; in der Praxis Erfolg selten).

### 5. Rechtsfolgen

- BKartA: Untersagungsverfügung § 32 GWB, Abstellungsverfügung, Verpflichtungszusagen § 32b GWB, Bußgeld § 81 GWB bis 10 % Konzernumsatz.
- KOM: Verfügung Art. 7 VO 1/2003, Bußgeld Art. 23 VO 1/2003.
- Privater Rechtsweg: Unterlassung, Beseitigung, Schadensersatz §§ 33–33h GWB; gesamtschuldnerische Haftung § 33d; Passing-on § 33e; Verjährung § 33h.
- Zivilprozess: spezialisierte Kartellsenate (Düsseldorf, München); örtliche Konzentration §§ 87 ff. GWB iVm Landesverordnungen.

### 6. Verhältnis zu DMA und sektorspezifischem Recht

- **DMA** (VO (EU) 2022/1925): gesonderte Verhaltenspflichten für Gatekeeper — Plugin `dsa-dma`; das DMA-Recht ist neben Art. 102 AEUV / § 19a GWB anwendbar, ersetzt diese nicht.
- **Telekommunikation/Energie**: TKG, EnWG mit Vorrang sektorspezifischer Regulierung in bestimmten Konstellationen.

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute

- [§ 18 GWB](https://www.gesetze-im-internet.de/gwb/__18.html) (Marktbeherrschung, Vermutungen)
- [§ 19 GWB](https://www.gesetze-im-internet.de/gwb/__19.html) (Missbrauchstatbestände)
- [§ 19a GWB](https://www.gesetze-im-internet.de/gwb/__19a.html) (strukturmarktrelevante Unternehmen)
- [§ 20 GWB](https://www.gesetze-im-internet.de/gwb/__20.html) (relative Marktmacht, Anzapfverbot)
- [§ 21 GWB](https://www.gesetze-im-internet.de/gwb/__21.html) (Boykottverbot)
- [§§ 32, 32b GWB](https://www.gesetze-im-internet.de/gwb/__32.html) (Abstellungs-/Verpflichtungsverfügung)
- [§§ 33–33h GWB](https://www.gesetze-im-internet.de/gwb/__33.html) (private Durchsetzung)
- [§ 81 GWB](https://www.gesetze-im-internet.de/gwb/__81.html) (Bußgeldrahmen)
- [Art. 102 AEUV](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:12012E102)
- [VO (EG) Nr. 1/2003](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32003R0001)

### Kommentare

- Fuchs, in: Immenga/Mestmäcker, Wettbewerbsrecht GWB, 6. Aufl. 2020, § 18 Rn. 1 ff. `[unverifiziert – Auflagenstand]`
- Markert, in: Immenga/Mestmäcker, Wettbewerbsrecht GWB, 6. Aufl. 2020, § 19 Rn. 1 ff. `[unverifiziert – Auflagenstand]`
- Eufinger, in: Loewenheim/Meessen/Riesenkampff, Kartellrecht, 4. Aufl. 2020, § 19a GWB Rn. 1 ff. `[unverifiziert]`
- Eilmansberger/Bien, in: Münchener Kommentar Wettbewerbsrecht, 3. Aufl. 2020, Art. 102 AEUV Rn. 1 ff. `[unverifiziert]`

### Rechtsprechung und Behördenpraxis (`[unverifiziert – prüfen in juris/EuGH-Datenbank/BKartA-Website]`)

1. EuGH, Urt. v. 13.02.1979 – Rs. 85/76, Hoffmann-La Roche (Behinderungsbegriff)
2. EuGH, Urt. v. 14.02.1978 – Rs. 27/76, United Brands (Marktabgrenzung Bananen)
3. EuGH, Urt. v. 03.07.1991 – Rs. C-62/86, AKZO Chemie ./. Kommission (Kampfpreis-Test; Preise unter durchschnittlichen variablen Kosten), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=1991-07-03&Aktenzeichen=C-62/86)
4. EuGH, Urt. v. 14.10.2010 – C-280/08 P, Deutsche Telekom ./. Kommission (Marge-Squeeze auf den Festnetzmärkten), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2010-10-14&Aktenzeichen=C-280/08)
5. EuGH, Urt. v. 06.09.2017 – C-413/14 P, Intel ./. Kommission (Treuerabatte; Verdrängungseignung ist zu prüfen, wenn substantiiert bestritten), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2017-09-06&Aktenzeichen=C-413/14)
6. EuG, Urt. v. 10.11.2021 – T-612/17, Google und Alphabet ./. Kommission (Google Shopping — Self-Preferencing), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuG&Datum=2021-11-10&Aktenzeichen=T-612/17); im Rechtsmittel bestätigt durch EuGH, Urt. v. 10.09.2024 – C-48/22 P, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2024-09-10&Aktenzeichen=C-48/22)
7. EuGH, Urt. v. 04.07.2023 – C-252/21, Meta Platforms u.a. (nationale Kartellbehörde darf DSGVO-Verstöße im Missbrauchsverfahren inzident prüfen), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2023-07-04&Aktenzeichen=C-252/21)
8. BGH, Beschl. v. 23.06.2020 – [KVR 69/19, Facebook](https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bgh&Art=en&client=12&pos=0&anz=1&Blank=1.pdf&nr=109506) (vorläufiges Verfahren)
9. BGH, Beschl. v. 23.04.2024 – KVB 56/22, Amazon (Feststellung der überragenden marktübergreifenden Bedeutung nach § 19a I GWB), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2024-04-23&Aktenzeichen=KVB%2056/22)
10. BKartA, Beschl. v. 06.02.2019 – [B6-22/16, Facebook](https://www.bundeskartellamt.de/SharedDocs/Entscheidung/DE/Entscheidungen/Missbrauchsaufsicht/2019/B6-22-16.html) (Konditionenmissbrauch)
11. BKartA, [Verfügungen 2022 ff.](https://www.bundeskartellamt.de/DE/DigitalWirtschaft/VerfahrenGegenGrosseDigitalkonzerne/verfahrengegengrossedigitalkonzerne_node.html) gegen Amazon, Apple, Google, Meta zu § 19a

## Ausgabeformat

```
GUTACHTEN – Marktbeherrschung und Missbrauch §§ 18, 19 GWB / Art. 102 AEUV
Unternehmen: <Name (anonymisiert)>
Verhalten: <Bezeichnung>
Stand: <Datum>

I. Sachverhalt
II. Frage(n)
III. Kurzantwort

IV. Rechtliche Bewertung
    1. Marktabgrenzung
       a) sachlich (Bedarfsmarktkonzept, SSNIP)
       b) räumlich
       c) zeitlich
    2. Marktbeherrschende / marktstarke Stellung
       a) § 18 I/III GWB
       b) Marktanteilsvermutung § 18 IV GWB
       c) ggf. § 18 IIIa GWB (Plattform-Kriterien)
       d) ggf. § 19a GWB (Adressat? Feststellungsverfahren BKartA)
       e) ggf. § 20 GWB (relative Marktmacht)
    3. Missbrauchstatbestand
       a) Behinderung / Ausbeutung / Diskriminierung / Essential Facility / Anzapfverbot
       b) Spezialtatbestände (Kampfpreis, Marge-Squeeze, Self-Preferencing, Konditionenmissbrauch)
    4. Objektive Rechtfertigung / Effizienzverteidigung
    5. Rechtsfolgen
       - Untersagungsverfügung / Verpflichtungszusagen
       - Bußgeld § 81 GWB / Art. 23 VO 1/2003
       - Schadensersatz §§ 33 ff. GWB

V. Risikoeinstufung
   🟢 / 🟡 / 🔴 <Einstufung mit Begründung>

VI. Empfehlung
    - Verhaltensanpassung / Compliance-Maßnahmen
    - Verpflichtungszusagen § 32b GWB / Art. 9 VO 1/2003
    - Schutzschrift / Reaktion auf Auskunftsverlangen

VII. Quellenverzeichnis
```

## Beispiel (Auszug, Gutachtenstil)

> Die Plattform P bevorzugt im Ranking ihre Eigenangebote gegenüber gleichartigen Drittangeboten. Sachlich relevanter Markt ist nach dem Bedarfsmarktkonzept der Markt für Online-Marktplatzdienste für Endkunden im EWR; Indizien für eine eigenständige Marktdefinition gegenüber stationärem Handel liefert die KOM-Praxis (vgl. EuG, [T-612/17, Google Shopping](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex:62017TJ0612)). Mit einem Marktanteil von > 40 % besteht die Vermutung des § 18 IV GWB. Das BKartA hat zudem mit Verfügung v. ... `[unverifiziert]` festgestellt, dass die Adressatin Unternehmen mit überragender marktübergreifender Bedeutung iSv § 19a I GWB ist; die Schwelle des § 19a II Nr. 1 lit. a GWB (Begünstigung eigener Angebote bei der Vermittlung) ist auf die beschriebene Praxis anwendbar. Eine **objektive Rechtfertigung** durch Plattformqualität oder Schutz vor minderwertigen Angeboten greift nur dann, wenn das Self-Preferencing-Verhalten **verhältnismäßig** ist; ein vollständiges Ausblenden gleichartiger Drittangebote in den prominenten Ranking-Slots überschreitet diese Grenze. Risiko: 🔴 — Untersagungsverfügung mit Bußgeldrahmen bis 10 % Konzernumsatz (§ 81 II GWB) sowie Schadensersatzklagen geschädigter Händler (§§ 33–33h GWB, Bindungswirkung § 33b GWB). ...

## Risiken / typische Fehler

- **Marktabgrenzung zu großzügig** ("globaler digitaler Werbemarkt") — verfehlt das Bedarfsmarktkonzept.
- **§ 19a GWB ohne formelle Feststellungsverfügung** des BKartA angenommen — Voraussetzung ist die Feststellungsverfügung gegenüber dem konkreten Adressaten.
- **§ 20 GWB** mit § 18 GWB verwechselt — § 20 schützt KMU vor relativen Marktmächten, ohne Marktbeherrschung iSv § 18.
- **Effizienzverteidigung** als pauschales Plädoyer — der Belegumfang muss konkret sein, Beweislast liegt beim marktbeherrschenden Unternehmen.
- **Anzapfverbot § 19 II Nr. 5 GWB** (LEH-Konstellationen) übersehen.
- **Verhältnis zum DMA** verkannt — DMA-Pflichten stehen parallel und werden im Plugin `dsa-dma` behandelt.
- **Bindungswirkung § 33b GWB** und **Verjährung § 33h GWB** in nachgelagerten Schadensersatzklagen vergessen.
