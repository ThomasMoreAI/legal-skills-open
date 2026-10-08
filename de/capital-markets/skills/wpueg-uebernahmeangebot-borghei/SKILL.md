---
name: wpueg-uebernahmeangebot-borghei
title: /kapitalmarktrecht:wpueg-uebernahmeangebot
description: Prüfung des Pflichtangebots nach WpÜG bei Kontrollerwerb (30 % Stimmrechte, § 29 II WpÜG) – Acting in concert (§ 30 Zurechnung), Veröffentlichungspflicht § 35, Angebotsunterlage § 11 mit BaFin-Prüfung 10 Werktage, Mindestpreis § 31 iVm WpÜG-AngVO, Annahmefrist § 16 (4–10 Wochen) plus Zaunkönig 2 Wochen, Verhaltenspflichten Zielgesellschaft § 33, Stellungnahme § 27, Befreiung § 37, Squeeze-out §§ 39a/b ab 95 %. Use when Bieter Kontrolle über eine börsennotierte Zielgesellschaft erwirbt oder Zielgesellschaft auf ein Angebot reagiert.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/kapitalmarktrecht/skills/wpueg-uebernahmeangebot
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: capital-markets
language: de
---

# /kapitalmarktrecht:wpueg-uebernahmeangebot

## Zweck

Der Skill prüft, ob ein Übernahmevorhaben ein **Pflichtangebot nach §§ 35, 29 WpÜG** auslöst, dimensioniert den **Mindestpreis** nach § 31 WpÜG iVm WpÜG-AngVO, unterstützt bei der **Angebotsunterlage** und ihrer **BaFin-Prüfung (§§ 11, 14)** sowie bei der **Stellungnahme der Zielgesellschaft (§ 27 WpÜG)**. Er adressiert das **Verbot von Verteidigungsmaßnahmen ohne HV-Ermächtigung (§ 33)**, mögliche **Befreiungstatbestände (§ 37 WpÜG iVm WpÜG-BefreiV)** sowie den **Squeeze-out (§§ 39a/39b)** ab 95 % Stimmrechtsanteil.

## Eingaben

- Zielgesellschaft (Sitz in Inland; börsennotiert iSv § 2 III WpÜG; Handel am regulierten Markt oder organisierten Markt iSv § 2 VII WpÜG)
- Bieter (Person, Rechtsform, derzeitige Beteiligung, Konzernstruktur)
- Erwerbsvorhaben (Aktienkaufvertrag, Block Trade, Stimmbindungsvereinbarung, Ankerinvestor-Vertrag)
- Stimmrechtsanteil **vor** und **prognostiziert nach** Vollzug
- Mitwirkende Parteien (Acting-in-concert-Kandidaten: Co-Investoren, abgestimmt handelnde Aktionäre)
- Vorerwerbe in den letzten 6 Monaten (Mindestpreis-Berechnung § 4 WpÜG-AngVO)
- Zielsetzung Mandat: Bieter-Beratung / Zielgesellschaft-Beratung / Befreiungsantrag / Squeeze-out

## Sub-Agent-Architektur

Researcher liefert WpÜG-Normen, WpÜG-AngVO, WpÜG-BefreiV, BGH/OLG-Frankfurt-Rspr. (WpÜG-Senat), BaFin-Verwaltungspraxis. Drafter erstellt im Bieter-Mandat einen Angebotsunterlagen-Outline und ggf. Befreiungsantrag, im Ziel-Mandat eine § 27-Stellungnahme. Reviewer prüft Pflichtangebot-Schwellen, Mindestpreis-Berechnung und Frist-Kalender.

## Ablauf

### 1. Anwendungsbereich (§§ 1, 2 WpÜG)

WpÜG gilt für Angebote zum Erwerb von Wertpapieren einer **Zielgesellschaft** (Sitz im Inland; Aktien zum Handel auf einem organisierten Markt iSv § 2 VII WpÜG zugelassen — regulierter Markt im Inland oder anderer EWR-Staat). Drei Angebotstypen:

| Typ | Norm |
|---|---|
| Freiwilliges Erwerbsangebot | §§ 10 ff. WpÜG |
| Übernahmeangebot (Ziel: Kontrolle) | §§ 29 ff. WpÜG |
| Pflichtangebot (nach Kontrollerwerb) | §§ 35 ff. WpÜG |

### 2. Kontrolle und Pflichtangebot (§§ 29 II, 35 WpÜG)

**Kontrolle = Halten von mindestens 30 % der Stimmrechte** an der Zielgesellschaft (§ 29 II WpÜG).

**Folge des Kontrollerwerbs:**
- Veröffentlichung der Erlangung der Kontrolle innerhalb von **7 Kalendertagen** (§ 35 I 1 WpÜG).
- Übermittlung der Angebotsunterlage an BaFin innerhalb von **4 Wochen** nach Veröffentlichung (§ 35 II 1 WpÜG).

### 3. Acting in concert / Zurechnung (§ 30 WpÜG)

Bei der Stimmrechtsberechnung werden zugerechnet:

| § 30 I Nr. | Zurechnungstatbestand |
|---|---|
| 1 | Tochterunternehmen iSv § 290 HGB |
| 2 | Treuhänder |
| 3 | Verpfändete Aktien (Pfandnehmer) |
| 4 | Nießbrauch |
| 5 | Erwerbsberechtigung aus Optionen |
| 6 | Hinterlegte / verwahrte Aktien |

§ 30 II WpÜG (**Acting in concert**): Aktien Dritter werden zugerechnet, wenn sich der Bieter mit ihnen **über die Ausübung von Stimmrechten** oder in **sonstiger Weise abstimmt**, um eine **Veränderung der unternehmerischen Ausrichtung** der Zielgesellschaft zu bewirken. Einzelfälle: Stimmbindungsvereinbarungen, Konsortialverträge, Investorenvereinbarungen mit konkreten Strategie-Vorgaben. **Reine Einzelfall-Absprachen** (z. B. einmalige Stimmabsprache zu einem HV-Punkt) genügen nach BGH **nicht** (BGH, **WMF**, Urt. v. 18.09.2006 – II ZR 137/05 `[unverifiziert]`; BGH, **Postbank**, Urt. v. 29.07.2014 – II ZR 353/12 `[unverifiziert]`).

### 4. Angebotsunterlage und BaFin-Prüfung (§§ 11, 14 WpÜG)

- **§ 11 WpÜG:** Pflichtangaben — Bieter, Zielgesellschaft, Gegenleistung, Mindestpreis-Berechnung, Annahmefrist, Bedingungen, Finanzierungsbestätigung (§ 13 WpÜG), Absichten des Bieters hinsichtlich Geschäftspolitik / Mitarbeiter / Sitz (§ 11 II Nr. 2 WpÜG).
- **§ 14 II WpÜG:** BaFin prüft binnen **10 Werktagen** ab Eingang; bei Beanstandungen Untersagung oder Nachreichungs-Aufforderung. Nach positiver Prüfung Veröffentlichung der Angebotsunterlage **unverzüglich** und Beginn der Annahmefrist.

### 5. Mindestpreis (§ 31 WpÜG iVm WpÜG-AngVO)

Bei Pflicht- und Übernahmeangeboten muss die Gegenleistung mindestens dem **höheren** der beiden folgenden Beträge entsprechen:

| § WpÜG-AngVO | Maßstab |
|---|---|
| § 4 (Vorerwerbs-Preis) | **Höchster** vom Bieter (oder mit ihm acting in concert) **innerhalb der letzten 6 Monate vor Veröffentlichung** der Angebotsentscheidung bezahlter Preis |
| § 5 (gewichteter Durchschnittskurs) | **3-Monats-Durchschnittskurs** vor Veröffentlichung gem. § 35 I oder § 10 I WpÜG (bei Pflichtangebot: Bezugszeitpunkt § 35 I), gewichtet nach Umsätzen |

Mindestens 5 % der Gegenleistung sind in **Geldleistung** (EUR) zu erbringen, wenn Bieter in den letzten 6 Monaten Aktien gegen Geld erworben hat (§ 31 III WpÜG).

**Nacherwerbe (§ 31 IV WpÜG):** Erwirbt der Bieter nach Veröffentlichung **innerhalb von 1 Jahr** nach Ablauf der Annahmefrist Aktien zu einem höheren Preis, schuldet er den Differenzbetrag den Angebotsannehmern.

### 6. Annahmefrist (§ 16 WpÜG)

- **§ 16 I WpÜG:** Annahmefrist **4 bis 10 Wochen** nach Veröffentlichung der Angebotsunterlage.
- **§ 16 II WpÜG (Zaunkönig-Frist):** Nach Bekanntgabe des Annahmestands läuft eine **weitere Annahmefrist von 2 Wochen** für die noch nicht annehmenden Aktionäre.
- Verlängerung bei konkurrierendem Angebot (§ 22 WpÜG) oder bei Änderung des Angebots (§ 21 III WpÜG).

### 7. Verhaltenspflichten Zielgesellschaft (§§ 27, 33 WpÜG)

- **§ 27 WpÜG (Stellungnahme):** Vorstand und Aufsichtsrat der Zielgesellschaft geben unverzüglich nach Übermittlung der Angebotsunterlage eine **begründete Stellungnahme** zum Angebot ab. Inhalt nach § 27 I 2: Art und Höhe der Gegenleistung, voraussichtliche Folgen für Gesellschaft/Mitarbeiter/Standorte, Absichten Bieter, Eigeninteressen Vorstand/AR.
- **§ 33 WpÜG (Verteidigungsverbot):** Nach Veröffentlichung der Angebotsentscheidung und bis zur Veröffentlichung des Ergebnisses darf der Vorstand der Zielgesellschaft **keine Handlungen vornehmen, die den Angebotserfolg verhindern könnten**, außer
  - Maßnahmen ordnungsgemäßer Geschäftsführung
  - mit Zustimmung des AR oder durch HV-Ermächtigung (§ 33 II), oder
  - Suche nach konkurrierenden Bietern (White Knight).

### 8. Befreiung (§ 37 WpÜG iVm WpÜG-BefreiV)

Antrag des Bieters an die BaFin **vor** Kontrollerwerb oder unverzüglich danach. Tatbestände insbes. § 9 WpÜG-BefreiV: konzerninterne Umstrukturierung, Sanierungsfälle, Erwerb durch Treuhänder, Erbgang. BaFin entscheidet im Ermessen.

### 9. Squeeze-out und Andienungsrecht (§§ 39a, 39b WpÜG)

- **§ 39a WpÜG:** Bieter, der nach einem Übernahmeangebot **mindestens 95 % der stimmberechtigten Aktien** hält, kann binnen **3 Monaten** nach Ablauf der Annahmefrist beim LG Frankfurt am Main den Antrag auf Übertragung der restlichen Aktien stellen. Maßstab: Angebotspreis gilt als angemessen, wenn Bieter mindestens 90 % der Annahmequote erreicht hat (§ 39a III 3 WpÜG).
- **§ 39b WpÜG:** Verbleibende Aktionäre können nach Maßgabe der gleichen Schwelle (95 %) Andienung verlangen.
- **Alternativ:** Aktienrechtlicher Squeeze-out nach §§ 327a–327f AktG (Schwelle 95 %, Barabfindung gerichtlich überprüfbar).

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute

- [WpÜG](https://www.gesetze-im-internet.de/wp_g/) – §§ 10–14, 16, 21, 22, 27, 29, 30, 31, 33, 35, 37, 39a, 39b
- [WpÜG-AngVO](https://www.gesetze-im-internet.de/wp_gangebv/) – §§ 4 (Vorerwerbs-Preis), 5 (Durchschnittskurs)
- [WpÜG-BefreiV](https://www.gesetze-im-internet.de/wp_gbefreiv/) – Befreiungstatbestände
- [§§ 21–23 AktG](https://www.gesetze-im-internet.de/aktg/__21.html) (Mitteilungspflichten – mit WpHG § 33 abgestimmt)
- [§§ 327a–327f AktG](https://www.gesetze-im-internet.de/aktg/__327a.html) (aktienrechtlicher Squeeze-out)

### Kommentare

- Angerer/Geibel/Süßmann, WpÜG, 4. Aufl. 2022, §§ 29, 30, 31, 35.
- Steinmeyer, WpÜG, 4. Aufl. 2019, §§ 29 ff.
- Schwark/Zimmer, KapMRK, 5. Aufl. 2020, §§ 29 ff. WpÜG.
- Krause/Pötzsch, in: Assmann/Pötzsch/Schneider, WpÜG, 4. Aufl. 2024, § 30 Rn. 1 ff.

### Rechtsprechung (`[unverifiziert – prüfen in juris/BaFin-Website/BGH]`)

1. BGH, Urt. v. 18.09.2006 – II ZR 137/05, BGHZ 169, 98 (WMF – Acting in concert)
2. BGH, Urt. v. 29.07.2014 – II ZR 353/12, ZIP 2014, 1932 (Postbank-Übernahme – Mindestpreis und Zurechnung)
3. OLG Frankfurt (WpÜG-Senat), diverse Beschlüsse zu Befreiungsanträgen und Mindestpreis
4. BaFin-Verwaltungspraxis zu § 37 WpÜG / WpÜG-BefreiV

## Ausgabeformat

```
GUTACHTEN — WpÜG Pflicht-/Übernahmeangebot
Zielgesellschaft: <anonymisiert>  |  Bieter: <anonymisiert>

I. Sachverhalt (knapp)
II. Frage(n)
III. Kurzantwort
     – Pflichtangebot ausgelöst: [ja / nein / nur bei Acting in concert]
     – Mindestpreis: <EUR pro Aktie>
     – Empfehlung: [Angebotsunterlage / Befreiungsantrag § 37 / keine Maßnahme]

IV. Rechtliche Bewertung
    1. Anwendungsbereich WpÜG (§§ 1, 2)
    2. Kontrollschwelle § 29 II WpÜG
       a) Direkter Stimmrechtserwerb
       b) Zurechnung § 30 I WpÜG
       c) Acting in concert § 30 II WpÜG (WMF/Postbank-Linie)
    3. Veröffentlichungspflicht § 35 WpÜG
    4. Angebotsunterlage §§ 11, 14 — BaFin-Prüfung 10 WT
    5. Mindestpreis § 31 WpÜG iVm §§ 4, 5 WpÜG-AngVO
       a) Vorerwerbe (6 Monate)
       b) 3-Monats-Durchschnittskurs
       c) Geldleistung 5 % (§ 31 III)
       d) Nacherwerbe (§ 31 IV, 1 Jahr)
    6. Annahmefrist § 16 (4–10 Wo + Zaunkönig 2 Wo)
    7. Verhaltenspflichten Zielgesellschaft §§ 27, 33
    8. Befreiungstatbestände § 37 WpÜG / WpÜG-BefreiV
    9. Squeeze-out § 39a (95 %)

V. Entwurf Pflichtangebot-Skizze / § 27-Stellungnahme (optional)

VI. Fristtabelle
    - Veröffentlichung Kontrollerwerb: 7 Kalendertage (§ 35 I 1)
    - Übermittlung Angebotsunterlage: 4 Wochen (§ 35 II 1)
    - BaFin-Prüfung: 10 Werktage (§ 14 II)
    - Annahmefrist: 4–10 Wochen (§ 16 I)
    - Zaunkönig-Frist: + 2 Wochen (§ 16 II)
    - Nacherwerb-Differenz: 1 Jahr ab Ende Annahmefrist (§ 31 IV)
    - Squeeze-out-Antrag: 3 Monate (§ 39a)

VII. Risiken / offene Punkte
     🟢 / 🟡 / 🔴 <Einstufung mit Begründung>

VIII. Quellenverzeichnis
```

## Risiken / typische Fehler

- **Acting-in-concert-Zurechnung unterschätzt**: Stimmbindungsvereinbarung + abgestimmtes Vorgehen zur Unternehmenspolitik genügt; auch mehrfache Einzelabsprachen können nach Gesamtbild Konzert begründen (Postbank-Linie).
- **Mindestpreis zu niedrig** angesetzt, weil Vorerwerbe konzernverbundener Erwerber außerhalb des Bieter-Lagerblatts übersehen wurden — § 31 iVm § 30 WpÜG.
- **Pflichtangebot-Umgehung ohne Befreiungsantrag** (§ 37 WpÜG) — BLOCKER: Sanktion und zivilrechtliche Folgen (Stimmrechtsverlust § 59 WpÜG).
- **§ 33-Verstoß**: Vorstand der Zielgesellschaft trifft Verteidigungsmaßnahmen (z. B. Veräußerung Crown Jewels, Kapitalerhöhung) ohne HV-Ermächtigung oder AR-Zustimmung.
- **Stellungnahme § 27 ohne Eigeninteressenoffenlegung** (Vorstands-/AR-Anteile, Vergütungspakete bei Change of Control) — Pflichtinhalt nach § 27 I 2 Nr. 4.
- **Squeeze-out-Schwelle (95 %)** verfehlt — Andienungsrecht § 39b nicht aktiviert; alternativ aktienrechtlicher Squeeze-out §§ 327a ff. AktG mit Spruchverfahren.
- **Verwechslung Stimmrechtsmeldung WpHG ↔ WpÜG-Kontrolle**: WpHG-Schwellen (3/5/10/15/20/25/30/50/75 %) sind reine Transparenzpflichten, WpÜG-30-%-Schwelle löst materielle Angebotspflicht aus.
