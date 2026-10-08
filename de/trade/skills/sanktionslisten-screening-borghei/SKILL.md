---
name: sanktionslisten-screening-borghei
title: /aussenwirtschaft-zoll-sanktionen:sanktionslisten-screening
description: Treffer-Workflow zum Sanktionslisten-Screening nach EU-Sanktions-VOen (konsolidierte EU-Liste auf Basis VO (EU) 269/2014, 2580/2001, 881/2002, 833/2014, 2017/1509 u.a.) – Bereitstellungsverbot Art. 2, False-positive-Bewertung, Frostung von Geldern und wirtschaftlichen Ressourcen, Meldung an BMWK/Bundesbank/Zoll, Schnittstelle GwG-KYC (§§ 10 ff. GwG). Use when ein Geschäftspartner-Screening oder ein laufendes Re-Screening einen möglichen Treffer auf einer EU- oder nationalen Sanktionsliste ergibt.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/aussenwirtschaft-zoll-sanktionen/skills/sanktionslisten-screening
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: trade
language: de
---

# /aussenwirtschaft-zoll-sanktionen:sanktionslisten-screening

## Zweck

Der Skill strukturiert die rechtliche Bewertung eines möglichen Treffers auf einer EU-Sanktionsliste, von der False-positive-Prüfung über die Frostung bis zur Meldepflicht an die zuständigen Behörden. Er adressiert das Bereitstellungsverbot (direkt/indirekt), den Begriff der „wirtschaftlichen Ressource" und die Schnittstelle zum Geldwäscherecht (KYC nach §§ 10 ff. GwG). Strafbarkeit nach § 18 AWG ist zwingend mitzudenken.

## Eingaben

- Trefferdaten: Name, Geburtsdatum, Geburtsort, Staatsangehörigkeit, ggf. Anschrift, ggf. Funktion
- Quelle des Treffers: Screening-Tool, Liste (konsolidierte EU-Liste, nationale Liste, ggf. UK OFSI, US SDN), Stand-Datum
- Geschäftskontext: Onboarding / laufende Beziehung / einzelner Zahlungsvorgang / Lieferung
- bisherige Berührung mit Geldern/wirtschaftlichen Ressourcen des potenziell Gelisteten (eingefrorene Konten, ausstehende Lieferungen, Beteiligungen)
- konzernale Verflechtung (Mehrheitsbeteiligung / Kontrolle iSv Sanktions-VO)

## Sub-Agent-Architektur

Researcher liefert die einschlägige Sanktions-VO (mit Stand-Datum), Listeneintrag, EuGH-/EuG-Rspr. zu Listing/Bereitstellungsverbot (Kadi, Rosneft) und Kommentarstellen. Drafter führt False-positive-Bewertung, Bereitstellungsverbots-Prüfung und Meldeentwurf durch. Reviewer prüft, ob BLOCKER-Hinweis (§ 18 AWG) gesetzt ist, Frostung dokumentiert und Meldepflichten beachtet sind.

## Ablauf

### 1. Treffer-Erstbewertung – False-positive vs. echter Treffer

Vergleich mehrerer Identifikatoren mit dem Listeneintrag:

| Identifikator | Mindeststandard |
|---|---|
| Name (einschl. Aliase, Transliteration) | Standardmatch |
| Geburtsdatum / Geburtsort | Pflichtabgleich |
| Staatsangehörigkeit | Pflichtabgleich |
| Anschrift | Pflichtabgleich, soweit verfügbar |
| Pass-/Personalausweisnummer | wenn in Liste vermerkt |
| Funktion / Position | bei PEPs / politisch Exponierten |

Ergebnis: **False positive** (dokumentieren, Akte schließen, kein Versand der Meldung) — **Verdachtslage** (weitere Sachverhaltsklärung) — **echter Treffer** (Stopp + Frostung + Meldung).

Hinweis: Sanktionslisten werden **häufig wöchentlich** aktualisiert. Bewertung immer mit **Stand-Datum** der Liste protokollieren.

### 2. Bereitstellungsverbot

Die einschlägige Sanktions-VO enthält typischerweise in Art. 2 ein doppeltes Verbot:

1. **Einfrierungsgebot** für sämtliche Gelder und wirtschaftlichen Ressourcen, die dem Gelisteten **gehören, im Eigentum stehen, in Besitz sind oder unter Kontrolle stehen**.
2. **Bereitstellungsverbot** – Gelder oder wirtschaftliche Ressourcen dürfen dem Gelisteten **weder direkt noch indirekt** zur Verfügung gestellt werden oder zugutekommen.

„Indirekt" ist weit auszulegen: Erfasst sind insbesondere Kontroll- und Mehrheitsbeteiligungs-Konstellationen — Faustregel der EU-Kommission: **> 50% Beteiligung** oder **tatsächliche Kontrolle** durch einen Gelisteten löst die Beschränkungen auch beim nicht selbst gelisteten Vehikel aus (EU-Kommission, FAQ zu Russland-Sanktionen `[unverifiziert – prüfen]`).

„Wirtschaftliche Ressource" ist **jeder** Vermögensgegenstand außer Geld, der zu Geld oder Gütern werden kann (Art. 1 Buchst. d typischer Sanktions-VOen).

### 3. Frostung und sofortiger Geschäftsstopp

Bei echtem Treffer:

- **Sofortiger Stopp** jeglicher Bereitstellung (Lieferungen, Zahlungen, Dienstleistungen)
- **Einfrieren** aller dem Gelisteten zustehenden Werte
- **Keine Auflösung** bestehender Vertragsbeziehungen ohne behördliche Genehmigung — Auflösung kann mittelbar Bereitstellung sein
- **Dokumentation** der Maßnahme, Zugriffsbeschränkung im internen System

### 4. Meldepflichten

| Anlass | Adressat | Rechtsgrundlage |
|---|---|---|
| Frostung von Geldern | Deutsche Bundesbank (Geldverkehr, Auslandszahlungsverkehr) | typisch Art. 8 jeweilige Sanktions-VO + AWV |
| Frostung wirtschaftlicher Ressourcen | BAFA | typisch Art. 8 jeweilige Sanktions-VO |
| Außenhandelsbezug, Ausfuhr/Einfuhr | Generalzolldirektion / örtl. Hauptzollamt | AWG / AWV / UZK |
| Geldwäsche-Verdacht | FIU (Zoll) | § 43 GwG |
| Listentreffer mit Strafbarkeitsverdacht (§ 18 AWG) | Staatsanwaltschaft | StPO |

**Frist:** Unverzüglich, idR ohne schuldhaftes Zögern (§ 121 BGB analog) und mit allen verfügbaren Informationen.

### 5. Onboarding-Pflichten und Re-Screening

- Beim Onboarding eines neuen Geschäftspartners (B2B/Endkunde/Vermittler): Screening auf der konsolidierten EU-Liste **vor** Vertragsschluss / Zahlungsausführung.
- Laufendes **Re-Screening** mindestens bei jeder Listenaktualisierung, sensitive Branchen (Banken, Versicherer, Exporteure mit Sanktionsbezug) **täglich**.
- **Risikobasierter Ansatz** (§ 10 Abs. 2 GwG): Frequenz und Tiefe abhängig von Branche, Drittland, Transaktionsvolumen, PEP-Status.
- Bei wirtschaftlich Berechtigtem (uBO, § 3 GwG): Screening auf uBO-Ebene.

### 6. Schnittstelle GwG (KYC) und § 261 StGB

Sanktionslistentreffer überlappen häufig mit:

- **Pflichten nach §§ 10 ff. GwG** (allg./verstärkte Sorgfaltspflichten), § 15 GwG (verstärkte Sorgfalt bei Hochrisikodrittländern)
- **§ 261 StGB** (Geldwäsche-Tatbestand) bei Transfers, die mittelbar gelisteten Personen zugutekommen
- bei Banken zusätzlich KWG-Aufsichtsrecht (BaFin)

→ ggf. parallele Anwendung des Skills `geldwaesche-aml-kyc`.

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Primär- und Sekundärrecht

- [Art. 215 AEUV](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:12012E215)
- [VO (EU) 269/2014 (Russland, persönliche Listung)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0269)
- [VO (EU) 833/2014 (Russland, sektorale Sanktionen)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0833)
- [VO (EG) 2580/2001 (Terrorismus)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32001R2580)
- [VO (EG) 881/2002 (Al-Qaida)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32002R0881)
- [VO (EU) 267/2012 (Iran)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32012R0267)
- [VO (EU) 2017/1509 (DVRK)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32017R1509)
- [AWG](https://www.gesetze-im-internet.de/awg_2013/) – insb. § 18
- [AWV](https://www.gesetze-im-internet.de/awv_2013/) – Meldepflichten
- [GwG](https://www.gesetze-im-internet.de/gwg_2017/) – §§ 10 ff.

### Behördliche Quellen

- Konsolidierte EU-Sanktionsliste (Financial Sanctions File / EU Sanctions Map sanctionsmap.eu), Stand: `<Datum eintragen>`
- BAFA-Merkblatt „Finanzsanktionen"
- Deutsche Bundesbank, Merkblatt „Finanzsanktionen / Embargos"
- BMWK-Hinweise zu länderspezifischen Maßnahmen

### Kommentare

- Pelz, in: Hocke/Sachs/Pelz, AWG/AWV, Stand 2024, § 18 AWG Rn. 1 ff.
- Hindelang, in: Krenzler/Herrmann/Niestedt, EU-Außenwirtschafts- und Zollrecht, Stand 2024, VO 269/2014 Rn. 1 ff.
- Pelz, AW-Prax (laufende Jahrgänge) – Russland-Sanktionen.

### Rechtsprechung

1. EuGH, Urt. v. 03.09.2008 – verb. Rs. C-402/05 P, C-415/05 P, Kadi und Al Barakaat International Foundation/Rat und Kommission („Kadi I"), ECLI:EU:C:2008:461 (Verfahrensrechte gelisteter Personen; Vorrang unionsrechtlicher Grundrechte gegenüber der Umsetzung von UN-Resolutionen), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2008-09-03&Aktenzeichen=C-402/05)
2. EuGH, Urt. v. 18.07.2013 – verb. Rs. C-584/10 P, C-593/10 P, C-595/10 P, Kommission u.a./Kadi („Kadi II"), ECLI:EU:C:2013:518 (umfassende Rechtmäßigkeitskontrolle des Listings, Begründungs- und Anhörungspflicht), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2013-07-18&Aktenzeichen=C-584/10)
3. EuGH, Urt. v. 28.03.2017 – Rs. C-72/15, Rosneft, ECLI:EU:C:2017:236 (Zuständigkeit des EuGH für die Überprüfung von GASP-gestützten Sanktionen; Gültigkeit und Auslegung der Russland-Maßnahmen), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2017-03-28&Aktenzeichen=C-72/15)

## Ausgabeformat

```
COMPLIANCE-MEMO — Sanktionslisten-Treffer
Geschäftspartner: <intern. Kennung, nicht Klarname>
Stand der Liste: <Datum>

I. Trefferdaten
   - Name / Aliase:
   - Geburtsdatum / -ort / Staatsangehörigkeit:
   - Adressabgleich:
   - Liste / Eintrag-Nr. / Sanktions-VO:

II. Erstbewertung
    [ ] False positive — Begründung
    [ ] Verdacht — weitere Klärung
    [X] echter Treffer — Stopp + Frostung + Meldung
    Ampel: 🟢 / 🟡 / 🔴

III. Rechtliche Bewertung
     1. Anwendbare Sanktions-VO (mit Stand der Konsolidierung)
     2. Bereitstellungsverbot Art. 2
        - direkt:
        - indirekt (Kontroll-/Mehrheitsbeteiligung > 50 %):
        - wirtschaftliche Ressource:
     3. Frostung – Reichweite (Konten, Lieferungen, Dienstleistungen)
     4. Meldepflichten
        - Bundesbank (Geldverkehr): <ja/nein, bis wann>
        - BAFA (wirtschaftliche Ressourcen): <ja/nein>
        - Zoll/Generalzolldirektion: <ja/nein>
        - FIU (GwG-Verdacht): <ja/nein>
     5. Strafbarkeitsrisiko § 18 AWG
        (Freiheitsstrafe bis 5 Jahre, gewerbsmäßig bis 15 Jahre)

IV. Sofortmaßnahmen
    - Stopp aller Bereitstellungen
    - Frostung dokumentiert
    - Meldungen versandt

V. Wiedervorlage / Re-Screening
   - bei jeder Listenaktualisierung
   - nächste Prüfung: <Datum>

VI. Quellenverzeichnis
```

## Risiken / typische Fehler

- **False-positive zu schnell „abgehakt"** ohne dokumentierten Mehr-Identifikator-Abgleich → bei echtem Treffer keine Exkulpation.
- **Indirekte Bereitstellung übersehen.** Zahlung an unscheinbares Vehikel, hinter dem ein Gelisteter zu > 50 % steht, ist ebenso untersagt.
- **„Wirtschaftliche Ressource" zu eng verstanden.** Maschinen, Lieferungen, Software-Lizenzen, IP-Rechte sind wirtschaftliche Ressourcen.
- **Meldung an Bundesbank vergessen.** Auch wenn keine Auszahlung erfolgt, ist die Frostung meldepflichtig.
- **Liste nicht aktuell.** Trefferprüfung gegen Liste vom Vormonat ist wertlos; immer Tagesaktualität (oder Wochenaktualität bei Standard-Branchen).
- **Vertragsauflösung „aus dem Bauch heraus"** kann eine indirekte Bereitstellung darstellen — vorher Behördenanfrage.
- **US-SDN-Liste als deutsche Rechtsgrundlage** behandelt — falsch. US-Listen sind außerhalb der EU geltend; relevant ist die konsolidierte EU-Liste plus nationale Maßnahmen. US-Listen lediglich als zusätzlicher Risikohinweis.
- **§ 18 AWG-Hinweis fehlt im Memo.** Strafbarkeit muss klar benannt sein, um Geschäftsleitung in die Pflicht zu nehmen.
