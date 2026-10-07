---
name: athletenvertrag
title: /sportrecht:athletenvertrag
description: Entwurf und AGB-Kontrolle von Athleten-, Spielerarbeits-, Förderungs-, Sponsoring- und Vermarktungsverträgen – §§ 305 ff. BGB Inhaltskontrolle, § 611a BGB / TzBfG Befristung, KUG §§ 22, 23 Bildnisrechte, § 1 GWB / Art. 101 AEUV Loyalty-/Exklusivklauseln (Bosman/Diarra-Linie), Doping-Klauseln und Bonusrückzahlung, DSGVO Art. 9 Gesundheits- und Trainingsdaten. Use when ein Athleten- oder Spielerarbeitsvertrag, Sponsoringvertrag, Förder- oder Vermarktungsvertrag entworfen, geprüft oder verhandelt werden soll.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/sportrecht/skills/athletenvertrag
license: Apache-2.0
version: 0.1.1
execution_mode: open
jurisdiction: de
practice: sports
language: de
---

# /sportrecht:athletenvertrag

## Zweck

Der Skill entwirft Athleten- und Spielerverträge oder prüft fremde Entwürfe gegen die einschlägigen zivil-, arbeits-, persönlichkeits-, kartell- und datenschutzrechtlichen Maßstäbe. Er liefert modulare Klauselbausteine und eine Inhaltskontrolle nach §§ 305 ff. BGB, weil Athleten- und Sponsoringverträge regelmäßig **AGB des Verbands, Vereins oder Ausrüsters** sind.

## Eingaben

- Vertragstyp: Vereinsmitgliedschaft, Spielerarbeitsvertrag, Athletenförder-/Sponsoringvertrag, Vermarktungsvertrag, Ausrüstervertrag
- Parteien (Athletin Profi/Amateur, Verein/Verband, Sponsor, Agentur)
- Laufzeit (Befristung TzBfG / unbefristet), Ausstiegsoptionen
- Vergütungsstruktur (Grundgehalt, Bonus, Sachleistungen, Bildrechtevergütung)
- Exklusivität / Loyalität / Wettbewerbsverbot
- Vermarktungs- und Bildrechte (KUG §§ 22, 23)
- Doping- und Sanktionsklauseln
- Datenverarbeitung (DSGVO Art. 9 – Gesundheits-, Trainings-, Biometrie-Daten)
- nationale / EU-Bezüge (Bosman, Diarra; Ausbildungsentschädigung)

## Sub-Agent-Architektur

Researcher liefert §§ 305–310 BGB, § 611a BGB, TzBfG, KUG, GWB, AEUV-Statute sowie BAG-, BGH- und EuGH-Rechtsprechung (Bosman, Meca-Medina, Diarra `[unverifiziert]`) und Standardliteratur (Holla, Vieweg/Steinbach Kapitel Spielervertrag; MüKoBGB §§ 305 ff.). Drafter erstellt den Vertragsentwurf mit Klauselbausteinen + Klauselkommentar in Fußnoten. Reviewer prüft AGB-Inhaltskontrolle, Klauselverbote §§ 308, 309 BGB, KUG-Konformität, kartellrechtliche Grenzen, DSGVO Art. 9, Schiedsklausel-Wirksamkeit (Pechstein-Linie).

## Ablauf

### 1. Vertragstypologie und anwendbares Recht

| Vertragstyp | Hauptrechtsrahmen |
|---|---|
| Vereinsmitgliedschaft | BGB §§ 21 ff. (e.V.); Satzung als AGB |
| Spielerarbeitsvertrag (Bundesliga) | § 611a BGB, TzBfG, AGB-Kontrolle, KSchG, EU-Grundfreiheiten (Bosman) |
| Athletenförderung (Spitzensport) | §§ 611 ff. / 631 ff. BGB; oft Mischvertrag; Stipendium-Komponente |
| Sponsoring-/Ausrüstervertrag | §§ 311 I, 535 ff./662 ff./675 BGB; KUG §§ 22, 23 |
| Vermarktungs-/Image-Rechte-Vertrag | §§ 311 BGB; KUG; ggf. UrhG (Lichtbild) |
| Agenten-/Spielervermittlervertrag | §§ 652 ff. BGB; FIFA-Spielervermittlerreglement `[unverifiziert]` |

### 2. AGB-Kontrolle §§ 305 ff. BGB

Vorformulierte Vertragsbedingungen des Verbands/Ausrüsters sind AGB (`[unverifiziert]`). Prüfung:

- **Einbeziehungskontrolle** § 305 II BGB
- **Überraschende Klauseln** § 305c BGB
- **Klauselverbote ohne Wertung § 309 BGB** (z. B. § 309 Nr. 9 BGB Bindungsdauer)
- **Klauselverbote mit Wertung § 308 BGB**
- **Transparenzgebot § 307 I 2 BGB**
- **Inhaltskontrolle § 307 I 1 BGB**: unangemessene Benachteiligung

Häufige rote Klauseln im Sportbereich:

- Einseitige Verlängerungsoption zugunsten Verein/Sponsor → § 308 Nr. 5 BGB / § 307 BGB
- Pauschalierter Schadensersatz bei Vertragsbruch ohne Gegenklausel → § 309 Nr. 5 BGB
- "Umfassende Übertragung" der Bildrechte ohne Konkretisierung → § 307 I 2 BGB Transparenz; KUG § 22
- Bonusrückzahlung bei Sperre **unabhängig vom Verschulden** → § 307 I BGB

### 3. Befristung Spielerarbeitsvertrag (TzBfG)

Spielerarbeitsverträge sind ganz überwiegend befristet. Sachgrund nach § 14 I TzBfG ist nach hM gegeben (Eigenart der Arbeitsleistung — körperliche Höchstleistung, begrenzte Karriere); BAG hat dies für Profifußball anerkannt (BAG, Urt. v. 16.01.2018 – 7 AZR 312/16, NZA 2018, 703 = NJW 2018, 1992 = SpuRt 2018, 170 — *Müller ./. 1. FSV Mainz 05*, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BAG&Datum=2018-01-16&Aktenzeichen=7%20AZR%20312/16)). Kettenbefristungen sind kritisch.

### 4. Bosman/Diarra: Ausbildungsentschädigung und Transferregeln

- EuGH, Urt. v. 15.12.1995 – **Bosman**, C-415/93, ECLI:EU:C:1995:463, NJW 1996, 505 = EuZW 1996, 82: Transferentschädigung nach Vertragsende verletzt Art. 45 AEUV (damals Art. 48 EGV); zugleich Unzulässigkeit der Ausländerklauseln ([dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=1995-12-15&Aktenzeichen=C-415/93)).
- EuGH, Urt. v. 18.07.2006 – **Meca-Medina und Majcen/Kommission**, C-519/04 P, NJW 2007, 2097 = EuZW 2006, 593 = SpuRt 2006, 195: Sportregeln unterliegen Art. 101 AEUV, wenn sie wirtschaftliche Wirkung haben; Drei-Stufen-Test (legitimer Zweck, Verhältnismäßigkeit, kohärenter Vollzug) ([dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Text=C-519/04)).
- EuGH, Urt. v. 04.10.2024 – **Diarra (FIFA ./. BZ)**, C-650/22: FIFA-Regelungen zum Status und Transfer von Spielern (RSTS) zur einseitigen Vertragsauflösung am Maßstab von Art. 45, 101 AEUV ([dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2024-10-04&Aktenzeichen=C-650/22)).

Konsequenz für Vertragsentwurf: Transferentschädigungs- und Loyalty-Klauseln am Art. 45/101 AEUV-Maßstab prüfen; § 1 GWB nationale Schranke.

### 5. Persönlichkeitsrecht und Vermarktung (KUG §§ 22, 23)

- **§ 22 KUG**: Bildnisse nur mit Einwilligung der abgebildeten Person verbreitet/zur Schau gestellt — gilt während *und nach* dem Athletenvertrag.
- **§ 23 KUG**: Ausnahmen (Bildnisse aus dem Bereich der Zeitgeschichte, Versammlungen) — abnehmender Schutz bei Spitzensportler/innen, aber höchstpersönlicher Kernbereich bleibt.
- **Vermögensrechtlicher Persönlichkeitsschutz** (BGH, Urt. v. 01.12.1999 – I ZR 49/97, BGHZ 143, 214 = NJW 2000, 2195 = GRUR 2000, 709 – *Marlene Dietrich*): die vermögenswerten Bestandteile des Persönlichkeitsrechts sind kommerziell verwertbar und vererblich; Schadensberechnung nach den drei Berechnungsarten ([dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=1999-12-01&Aktenzeichen=I%20ZR%2049/97)).

Klauselbaustein **Bildrechteübertragung**: präzise nach Medium, Territorium, Laufzeit, Verwendungszweck; bloße "umfassende" Übertragung ist intransparent und im AGB-Kontext angreifbar.

### 6. Doping-Klauseln und Bonusrückzahlung

Standardklauseln verlangen bei sportrechtlicher Sperre:

- Rückzahlung von Bonuszahlungen
- außerordentliche Kündigung des Sponsorings
- pauschalierten Schadensersatz

AGB-Kontrolle: pauschale Rückzahlung **ohne Verschuldensanknüpfung** ist mit § 307 I BGB problematisch — Athletin haftet sportrechtlich verschuldensunabhängig (WADC Art. 2.1), zivilrechtlich nur bei Verschulden (§ 276 BGB). Kombination = unangemessene Benachteiligung.

### 7. Datenschutz (DSGVO Art. 9)

Trainings-, Gesundheits-, ABP-Daten sind besondere Kategorien iSv Art. 9 I DSGVO. Verarbeitung nur auf Grundlage Art. 9 II DSGVO (insb. lit. a Einwilligung, lit. b Arbeitsrecht). Doping-Tests = unverzichtbar, gestützt auf Verbandsmitgliedschaft + Einwilligung; gleichwohl Zweckbindung, Speicherdauer, Auftragsverarbeitung (NADA / Labor) regeln.

### 8. Schiedsklausel

Wenn Schiedsklausel vorgesehen: Pechstein-Linie beachten — bei Athletenvereinbarung mit Monopolverband Inhaltskontrolle; öffentliche Verhandlung in Disziplinarsachen (EGMR `[unverifiziert]`). Bei reinem Wirtschaftsvertrag (Sponsoring) freie Wählbarkeit DIS/CAS unproblematisch.

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute

- [§§ 305–310 BGB](https://www.gesetze-im-internet.de/bgb/__305.html) (AGB-Kontrolle)
- [§ 611a BGB](https://www.gesetze-im-internet.de/bgb/__611a.html) (Arbeitsvertrag)
- [TzBfG](https://www.gesetze-im-internet.de/tzbfg/) (Befristung)
- [§ 22 KUG](https://www.gesetze-im-internet.de/kunsturhg/__22.html), [§ 23 KUG](https://www.gesetze-im-internet.de/kunsturhg/__23.html)
- [§ 1 GWB](https://www.gesetze-im-internet.de/gwb/__1.html), [§ 19 GWB](https://www.gesetze-im-internet.de/gwb/__19.html)
- [Art. 45 AEUV](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:12012E045), [Art. 101 AEUV](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:12012E101)
- [Art. 9 DSGVO](https://eur-lex.europa.eu/eli/reg/2016/679/oj) (besondere Kategorien)
- [AGG](https://www.gesetze-im-internet.de/agg/)

### Kommentare und Handbücher

- Holla, Praxishandbuch Sportrecht, X. Aufl. Jahr, Kap. Spielervertrag / Sponsoring
- Vieweg/Steinbach, Sportrecht, Loseblatt, Stand Jahr, Kap. Spielerverträge / Vermarktung
- Summerer, in: Fritzweiler/Pfister/Summerer, Praxishandbuch Sportrecht, X. Aufl. Jahr, Kap. Athletenverträge
- Wandtke/Bullinger, Praxiskommentar Urheberrecht, X. Aufl. Jahr, § 22 KUG Rn. 1 ff.
- Basedow, in: MüKoBGB, 9. Aufl. 2022, § 305 BGB Rn. 1 ff.; Wurmnest, § 307 BGB Rn. 1 ff.
- Linck, in: ErfK, 24. Aufl. 2024, § 14 TzBfG Rn. 1 ff.

### Rechtsprechung

1. EuGH, Urt. v. 15.12.1995 – Rs. C-415/93, ECLI:EU:C:1995:463, NJW 1996, 505 (*Bosman* – Art. 45 AEUV, Transferentschädigung und Ausländerklauseln), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=1995-12-15&Aktenzeichen=C-415/93)
2. EuGH, Urt. v. 18.07.2006 – Rs. C-519/04 P, NJW 2007, 2097 = SpuRt 2006, 195 (*Meca-Medina und Majcen/Kommission* – Anti-Doping-Regeln am Maßstab des Kartellrechts), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Text=C-519/04)
3. EuGH, Urt. v. 04.10.2024 – Rs. C-650/22 (*Diarra*, FIFA ./. BZ – FIFA-RSTS, Art. 45, 101 AEUV), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2024-10-04&Aktenzeichen=C-650/22)
4. BAG, Urt. v. 16.01.2018 – 7 AZR 312/16, NZA 2018, 703 = SpuRt 2018, 170 (*Müller ./. 1. FSV Mainz 05* – Befristung Profifußball, § 14 I TzBfG), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BAG&Datum=2018-01-16&Aktenzeichen=7%20AZR%20312/16)
5. BGH, Urt. v. 01.12.1999 – I ZR 49/97, BGHZ 143, 214 = GRUR 2000, 709 (*Marlene Dietrich* – vermögensrechtlicher Persönlichkeitsschutz), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=1999-12-01&Aktenzeichen=I%20ZR%2049/97)

## Ausgabeformat

```
ATHLETENVERTRAG — Entwurf / Prüfung
Parteien: <Athletin / Verein/Verband / Sponsor>
Vertragstyp: <…>

§ 1 Vertragsgegenstand
§ 2 Laufzeit und Beendigung
    – Befristung TzBfG § 14
    – außerordentliche Kündigung § 626 BGB
    – Ausstiegsklauseln (symmetrisch!)
§ 3 Vergütung
    – Grundgehalt
    – Bonus (sportlich, Vermarktung)
    – Rückzahlungsregelung mit Verschuldensanknüpfung
§ 4 Exklusivität / Loyalität
    – kartellrechtliche Grenzen § 1 GWB, Art. 101 AEUV
§ 5 Bild- und Vermarktungsrechte
    – KUG §§ 22, 23: Medium, Territorium, Laufzeit, Zweck
    – Beendigungswirkung (Rückrufrecht analog § 41 UrhG?)
§ 6 Doping
    – Loyalitätspflicht zu WADC/NADC
    – Rückzahlungs-/Sanktionsklausel verschuldensabhängig
§ 7 Datenverarbeitung
    – DSGVO Art. 9 lit. a/b; Zweckbindung; Auftragsverarbeitung
§ 8 Verschwiegenheit / Wettbewerbsverbot
§ 9 Streitbeilegung
    – Schiedsklausel (DIS/CAS) — Pechstein-Inhaltskontrolle beachten
§ 10 Schlussbestimmungen
     – salvatorische Klausel, Schriftform

——————————————————————————————————————————————

KLAUSELKOMMENTAR (intern)

1. § 2 Befristung
   - Sachgrund § 14 I Nr. 4 TzBfG (BAG, Urt. v. 16.01.2018 – 7 AZR 312/16, NZA 2018, 703)
2. § 5 Bildrechte
   - "umfassend" zu unbestimmt → § 307 I 2 BGB; präzisieren
3. § 6 Doping-Rückzahlung
   - verschuldensunabhängig = § 307 I BGB Bedenken
...

——————————————————————————————————————————————

REVIEW-CHECKLISTE
[ ] §§ 305 ff. BGB-Kontrolle aller Klauseln
[ ] Klauselverbote § 308, 309 BGB durchgegangen
[ ] KUG §§ 22, 23 in § 5 sauber spezifiziert
[ ] § 1 GWB / Art. 101 AEUV für Exklusivität geprüft
[ ] DSGVO Art. 9 in § 7 verankert
[ ] Schiedsklausel Pechstein-konform
[ ] Salvatorische Klausel ohne Klauselverbots-Heilungsfunktion

Risiken: 🟢 / 🟡 / 🔴
```

## Risiken / typische Fehler

- **"Umfassende" Bildrechteübertragung** → § 307 I 2 BGB intransparent; Athletin behält faktische Kontrolle nicht zurück.
- **Bonusrückzahlung bei Sperre verschuldensunabhängig** → § 307 I BGB; Kombination mit WADC-strict-liability ist unausgewogen.
- **Einseitige Verlängerungsoption / Ausstiegsklausel nur zugunsten Sponsor/Verein** → § 308 Nr. 5 / § 307 BGB.
- **Wettbewerbsverbot nach Vertragsende ohne Karenzentschädigung** (Spielervertrag): § 110 GewO iVm §§ 74 ff. HGB analog `[unverifiziert]`.
- **Schiedsklausel ohne Pechstein-Prüfung** in Verbands-Athletenvereinbarung → angreifbar.
- **Datenverarbeitung nicht auf Art. 9 II DSGVO gestützt** → DSGVO-Bußgeldrisiko.
- **Spielervermittlerprovision** nicht an FIFA/DFB-Regelwerk angepasst → Provision unwirksam.
- **Übersehen der Diarra-Linie** bei einseitiger Vertragsauflösung im Profifußball — kartellrechtliche / Grundfreiheits-Schranken.
