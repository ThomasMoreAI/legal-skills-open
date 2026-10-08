---
name: prospektpflicht-pruefung-borghei
title: /kapitalmarktrecht:prospektpflicht-pruefung
description: Prüfung der Prospektpflicht nach VO (EU) 2017/1129 iVm WpPG – Trigger Art. 3 (öffentliches Angebot / Zulassung), Ausnahmenkatalog Art. 1 IV, Schwellenwert § 3 WpPG (8 Mio. EUR, Wertpapier-Informationsblatt), Inhaltsanforderungen Art. 6–8, BaFin-Billigung Art. 20 (10/20/30 Werktage), Nachtragspflicht Art. 23, Prospekthaftung §§ 9–11 WpPG. Use when ein Emittent ein öffentliches Angebot oder die Zulassung zum regulierten Markt plant oder Prospekthaftungs-Ansprüche zu beurteilen sind.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/kapitalmarktrecht/skills/prospektpflicht-pruefung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: capital-markets
language: de
---

# /kapitalmarktrecht:prospektpflicht-pruefung

## Zweck

Der Skill prüft, ob für eine geplante Emission oder Zulassung ein **Wertpapierprospekt** nach der unmittelbar anwendbaren **Prospekt-VO (EU) 2017/1129** erforderlich ist, identifiziert einschlägige **Ausnahmen** (Art. 1 IV, § 3 WpPG mit Wertpapier-Informationsblatt) und unterstützt bei Aufbau und Risikofaktoren-Katalog. Er adressiert das **BaFin-Billigungsverfahren** (Art. 20 Prospekt-VO) sowie die **Prospekthaftung** nach §§ 9–11 WpPG.

## Eingaben

- Emittent (Rechtsform, Sitz, Bilanzkennzahlen, EU-Heimatstaat iSv Art. 2 lit. m Prospekt-VO)
- Wertpapiergattung (Aktie, Schuldverschreibung, Wandelanleihe, Hybridkapital)
- Vorhaben: öffentliches Angebot, Zulassung zum regulierten Markt (Prime Standard, General Standard, Scale ist Freiverkehr), Privatplatzierung
- Volumen, Mindeststückelung, Anlegerkreis (qualifizierte / nicht-qualifizierte Anleger)
- Zeitachse (geplanter Pricing-Termin, Listing)
- bestehende Finanzinformationen (geprüfte Konzernabschlüsse, Zwischenabschluss)

## Sub-Agent-Architektur

Researcher liefert Prospekt-VO-Artikel, WpPG-Normen, BaFin-Prospektpraxis, ESMA-Risikofaktoren-Leitlinien (ESMA31-62-1293), BGH-Rspr. zur Prospekthaftung (Telekom III). Drafter erstellt Prospekt-Outline und Risikofaktorenkatalog spezifisch für den Emittenten. Reviewer prüft Schwellenwertlogik, Billigungsfristen-Kalender und Haftungsrahmen.

## Ablauf

### 1. Trigger der Prospektpflicht (Art. 3 Prospekt-VO)

Ein Prospekt ist erforderlich für:
- **(a) ein öffentliches Angebot** von Wertpapieren in der Union (Art. 3 I), und/oder
- **(b) die Zulassung zum Handel an einem geregelten Markt** mit Sitz oder Tätigkeit in der Union (Art. 3 III).

**Öffentliches Angebot** = Mitteilung an Personen, die ausreichende Informationen enthält, um über Kauf/Zeichnung zu entscheiden (Art. 2 lit. d Prospekt-VO).

### 2. Ausnahmen vom Prospektzwang

#### a) Art. 1 IV Prospekt-VO (öffentliches Angebot)

| lit. | Ausnahme |
|---|---|
| a | Angebot ausschließlich an **qualifizierte Anleger** (Art. 2 lit. e iVm MiFID II) |
| b | Angebot an **weniger als 150 nicht-qualifizierte Anleger pro EWR-Staat** |
| c | Mindeststückelung **≥ 100.000 EUR** je Anleger |
| d | Mindestnominalbetrag der Wertpapiere **≥ 100.000 EUR** |
| e | Gesamtgegenwert in der Union **unter 1 Mio. EUR** in 12 Monaten |
| i | Mitarbeiter-/Organmitgliederprogramme (mit Informationsdokument) |

#### b) Art. 1 V Prospekt-VO (Zulassung zum regulierten Markt; "regulierter Markt" iSv MiFID II)

Z. B. Aktien, die für weniger als 20 % der Aktien derselben Gattung in 12 Monaten zugelassen werden (Art. 1 V lit. a).

#### c) § 3 WpPG – nationale Schwellenausnahme bis 8 Mio. EUR

Deutschland macht von der Mitgliedstaatenoption nach Art. 3 II Prospekt-VO Gebrauch (Schwellenwert bis 8 Mio. EUR Gesamtgegenwert in 12 Monaten). Statt Prospekt muss ein **Wertpapier-Informationsblatt (WIB)** nach § 4 WpPG erstellt und der BaFin **mindestens 4 Werktage vor öffentlichem Angebot** hinterlegt werden. Vertriebsweg eingeschränkt (Anlageberatung mit Geeignetheitsprüfung oder Einzelanlagebetragsgrenzen).

### 3. Inhalt des Prospekts (Art. 6 ff. Prospekt-VO)

- **Mindestinhalt:** wesentliche Informationen über den Emittenten und die angebotenen/zugelassenen Wertpapiere; Risikofaktoren; Finanzinformationen (geprüfte Konzernabschlüsse der letzten 2 oder 3 Jahre je nach Schema; ggf. ungeprüfter Zwischenabschluss); Geschäftsmodell; Management; Aktionärsstruktur; Mittelverwendung; rechtliche Verhältnisse.
- **Risikofaktoren (Art. 16):** spezifisch für den Emittenten und das Wertpapier; **wesentlich** (Eintrittswahrscheinlichkeit + Auswirkungsschwere); kategorienweise gruppiert, in der Reihenfolge der Wesentlichkeit. ESMA-Guidelines on Risk Factors (ESMA31-62-1293) sind verbindliche Auslegung.
- **Zusammenfassung (Art. 7 Prospekt-VO):** kurze, allgemeinverständliche Darstellung; **max. 7 DIN A4-Seiten**; standardisierte Reihenfolge (Einleitung, Wertpapier, Emittent, zentrale Risiken, Angebot).
- **Basisprospekt (Art. 8):** für Programme nicht-dividendenberechtigter Wertpapiere; Endgültige Bedingungen je Einzelemission.
- **Verantwortlichkeit (Art. 11 Prospekt-VO):** Emittent / Anbieter / Person, die Zulassung beantragt; ggf. Garant. Namentliche Benennung im Prospekt.

### 4. BaFin-Billigung (Art. 20 Prospekt-VO)

| Konstellation | BaFin-Frist |
|---|---|
| Folgeprospekt eines bekannten Emittenten | **10 Werktage** ab Antrag (Art. 20 II UAbs. 1) |
| Regulärer Prospekt | **20 Werktage** ab Antrag |
| Erstemittent ("Initial Public Offer" / erstmaliger Prospekt) | **20 Werktage**, verlängert auf eine zusätzliche Prüfschleife — in der Praxis **bis zu 30 Werktage** Gesamtdauer |
| Nachfrage / Nachreichungen | Fristverlängerung um 10 WT je Iteration |

Eine **Nachtragspflicht (Art. 23 Prospekt-VO)** entsteht, wenn nach Billigung und vor endgültigem Schluss des öffentlichen Angebots oder Beginn des Handels neue wesentliche Umstände oder wesentliche Unrichtigkeiten bekannt werden. Nachtrag muss von BaFin gebilligt werden; Anleger haben Widerrufsrecht (Art. 23 II — 2 Werktage nach Veröffentlichung des Nachtrags).

### 5. Prospekthaftung (§§ 9–11 WpPG)

- **§ 9 WpPG (Außenhaftung):** Erwerber kann von Verantwortlichen (Emittent, Anbieter, Garant, Personen, die Verantwortung übernommen haben) Rückgängigmachung des Erwerbs (Übernahme der Wertpapiere gegen Erstattung des Erwerbspreises zuzüglich Kosten) bzw. Differenzschaden verlangen, wenn der Prospekt unrichtig oder unvollständig ist und die fehlerhafte Aussage für den Erwerb erheblich war.
- **§ 10 WpPG (Verschulden):** Haftung entfällt, wenn Verantwortlicher die Unrichtigkeit nicht kannte und die Unkenntnis nicht auf grober Fahrlässigkeit beruht.
- **§ 11 WpPG (Verjährung):** Anspruch verjährt **innerhalb eines Jahres** ab Kenntnis von Unrichtigkeit / Unvollständigkeit, spätestens **drei Jahre** nach Veröffentlichung des Prospekts.
- **Allgemeine Anspruchsgrundlagen** daneben: § 826 BGB (sittenwidrige Schädigung), § 823 II BGB iVm § 264a StGB (Kapitalanlagebetrug) — insb. für graue Kapitalmarktprodukte außerhalb WpPG.

### 6. Abgrenzung zu KAGB und VermAnlG

- **Investmentvermögen** iSv § 1 I KAGB (insb. Publikumsfonds): KAGB-Verkaufsprospekt + wesentliche Anlegerinformationen (PRIIPs-KID) statt Prospekt-VO.
- **Vermögensanlagen außerhalb Wertpapier** (insb. Nachrang-Darlehen, Genussrechte, partiarische Darlehen): **VermAnlG** mit VermögensanlagenInformationsblatt (VIB) und ggf. Verkaufsprospekt.
- **Schwarmfinanzierungsdienstleister:** VO (EU) 2020/1503 — eigene Regime.

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Unmittelbar anwendbares Unionsrecht

- [VO (EU) 2017/1129 (Prospekt-VO)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32017R1129) – Art. 1, 3, 6, 7, 8, 11, 16, 20, 23
- DelegierteVO (EU) 2019/980 (Format und Inhalt)
- ESMA Guidelines on Risk Factors under the Prospectus Regulation (ESMA31-62-1293)

### Deutsches Recht

- [WpPG](https://www.gesetze-im-internet.de/wppg/) – §§ 3 (Schwellenausnahme + WIB), 4 (Wertpapier-Informationsblatt), 9–11 (Prospekthaftung)
- [KAGB](https://www.gesetze-im-internet.de/kagb/) – §§ 1, 162 ff.
- [VermAnlG](https://www.gesetze-im-internet.de/vermanlg/) – Vermögensanlagen außerhalb Wertpapier
- BaFin Merkblatt zur Prospektprüfung / Wertpapier-Informationsblatt

### Kommentare

- Groß, Kapitalmarktrecht, 7. Aufl. 2022, § 6 WpPG / Prospekt-VO.
- Habersack, in: Habersack/Mülbert/Schlitt, Hdb. der Kapitalmarktinformation, 4. Aufl. 2024, § 13 Rn. 1 ff. (Prospekthaftung).
- Versteegen, in: Habersack/Mülbert/Schlitt, Unternehmensfinanzierung am Kapitalmarkt, 4. Aufl. 2024, § 7 Rn. 1 ff. (Prospekt-VO).
- Schwark/Zimmer, KapMRK, 5. Aufl. 2020, Art. 3 Prospekt-VO Rn. 1 ff.

### Rechtsprechung (`[unverifiziert – prüfen in juris/BGH-Datenbank]`)

1. BGH, Urt. v. 31.05.2011 – II ZR 141/09, BGHZ 190, 7 (Telekom III – Prospekthaftung)
2. BGH, Urt. v. 21.10.2014 – XI ZB 12/12, BGHZ 203, 1 (Musterverfahren KapMuG, Prospekthaftung Telekom)
3. BGH-Linie zur grauen Kapitalmarkthaftung (§ 826 BGB) – diverse Entscheidungen
4. BaFin-Verwaltungspraxis zur Schwellenausnahme § 3 WpPG (Merkblätter und Q&As)

## Ausgabeformat

```
GUTACHTEN — Prospektpflicht und Prospekthaftung
Emittent: <anonymisiert>  |  Vorhaben: <IPO / Privatplatzierung / Anleihe>

I. Sachverhalt (knapp)
II. Frage(n)
III. Kurzantwort
     – Prospektpflicht: [ja / Ausnahme Art. 1 IV lit. … / § 3 WpPG-WIB]
     – Empfehlung: [Vollprospekt / WIB / Privatplatzierungs-Vermerk]

IV. Rechtliche Bewertung
    1. Trigger der Prospektpflicht (Art. 3 Prospekt-VO)
    2. Ausnahmenkatalog
       a) Art. 1 IV Prospekt-VO
       b) § 3 WpPG (8 Mio. EUR-Schwelle, WIB)
    3. Inhalt und Risikofaktoren (Art. 6, 7, 16)
    4. BaFin-Billigung (Art. 20) – Fristenplan
    5. Nachtragspflicht (Art. 23)
    6. Prospekthaftung §§ 9–11 WpPG

V. Prospekt-Outline (optional)
   1. Zusammenfassung (max. 7 Seiten)
   2. Risikofaktoren (spezifisch, in Wesentlichkeitsreihenfolge)
   3. Angaben zum Emittenten
   4. Angaben zu den Wertpapieren
   5. Finanzinformationen
   6. Angebot / Zulassung
   7. Verantwortlichkeitserklärung

VI. Fristtabelle
    - BaFin-Billigung 10 / 20 / 30 WT (Art. 20 Prospekt-VO)
    - WIB-Hinterlegung 4 WT vor Angebot (§ 4 WpPG)
    - Nachtrag Widerrufsrecht 2 WT (Art. 23 II)
    - Prospekthaftung Verjährung 1 Jahr / 3 Jahre (§ 11 WpPG)

VII. Risiken / offene Punkte
     🟢 / 🟡 / 🔴 <Einstufung mit Begründung>

VIII. Quellenverzeichnis
```

## Risiken / typische Fehler

- **Falsche Annahme einer Privatplatzierungs-Ausnahme**, weil unter 150 Anleger pro EWR-Staat: ohne saubere Anlegerregister-Dokumentation greift die Ausnahme nicht.
- **§ 3 WpPG-Schwelle überschritten**, wenn Folgeemissionen im 12-Monats-Zeitraum nicht zusammengerechnet werden.
- **Risikofaktoren generisch** (z. B. "allgemeines Marktrisiko") — ESMA-Guidelines verlangen Emittenten-Spezifität; BaFin verlangt Nachbesserung, verzögert Billigung.
- **Nachtragspflicht (Art. 23) verkannt** zwischen Billigung und Pricing/Listing — Folge: Haftungs-Exposition, Widerrufsrechte.
- **Verantwortlichkeitserklärung unklar**: Welche Personen unterzeichnen Art. 11? Vorstand des Emittenten? Garant? Konsortialführerinnen sind grds. nicht Prospektverantwortliche, können aber nach allg. Recht haften.
- **Abgrenzung KAGB / VermAnlG** verkannt — bei Investmentvermögen statt Prospekt-VO ist KAGB-Vertriebsregime einschlägig.
- **Anlage-/Bankberatungspflichten nach WpHG §§ 63 ff.** beim Vertrieb – Querverweis Plugin `bankrecht` (Geeignetheitsprüfung) und MiFID-II-Anker.
