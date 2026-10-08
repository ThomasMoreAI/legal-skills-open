---
name: stvg-haftungspruefung-borghei
title: /verkehrsrecht:stvg-haftungspruefung
description: Haftungsprüfung nach Verkehrsunfall – Halterhaftung § 7 StVG, Fahrerhaftung § 18 StVG, Quotelung § 17 StVG bei beidseitiger Betriebsgefahr, Mitverschulden § 9 StVG iVm § 254 BGB, Schadensbezifferung mit 130%-Grenze, Nutzungsausfall, Mietwagen, Schmerzensgeld. Use when nach einem Verkehrsunfall die Haftungsquote und der ersatzfähige Schaden gegen Halter, Fahrer und Pflichtversicherer (§ 115 VVG) zu prüfen sind.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/verkehrsrecht/skills/stvg-haftungspruefung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: transportation
language: de
---

# /verkehrsrecht:stvg-haftungspruefung

## Zweck

Der Skill prüft Ansprüche des Unfallgeschädigten gegen Halter (§ 7 StVG), Fahrer (§ 18 StVG) und Pflichtversicherer (§ 115 VVG) sowie die Quote nach § 17 StVG bei Beteiligung mehrerer Kraftfahrzeuge. Er beziffert den ersatzfähigen Schaden (Reparatur vs. Totalschaden, 130%-Grenze, Nutzungsausfall, Mietwagen, Schmerzensgeld) und liefert eine prozessfähige Quotenargumentation für die typischen Konstellationen (Auffahrunfall, Spurwechsel, Vorfahrtverletzung).

## Eingaben

- Unfallort, -zeit, Witterung, Sichtverhältnisse
- Beteiligte Fahrzeuge (Halter, Fahrer, Zulassung, Pflichtversicherer)
- Hergangsbeschreibung beider Seiten (ggf. Polizeibericht)
- Schadensbild (Reparaturkosten brutto/netto, Wiederbeschaffungswert, Restwert, Sachverständigengutachten)
- Personenschäden (Verletzungsbild, Heilbehandlungsdauer, Arbeitsunfähigkeit)
- Bisheriger Schriftverkehr mit Versicherer

## Sub-Agent-Architektur

Researcher liefert StVG, BGB-Schadensrecht, BGH-VI-ZS-Rechtsprechung zur Quotelung und Schadensposten sowie Hentschel/König/Dauer- und Geigel-Belegstellen. Drafter erstellt ein Haftungsgutachten in Gutachtenstil mit Quote, Schadensposition und Forderungsschreiben an den Pflichtversicherer. Reviewer prüft Quotelungsschema, 130%-Grenze, Verjährung (§§ 195, 199 BGB; § 14 StVG) und Schmerzensgeldhöhe.

## Ablauf

### 1. Anspruchsgrundlagen

Kanonische Reihenfolge:

1. **§ 7 Abs. 1 StVG** – Gefährdungshaftung des Halters „bei Betrieb" eines KfZ. Maßstab „bei Betrieb" weit (BGH-Linie: jede durch das Fahrzeug ausgelöste Gefährdung im Straßenverkehr) `[unverifiziert – prüfen in juris]`.
2. **§ 7 Abs. 2 StVG** – Haftungsausschluss nur bei höherer Gewalt (eng auszulegen; weder unabwendbares Ereignis i. S. d. § 17 III StVG noch grobes Eigenverschulden des Geschädigten genügen).
3. **§ 18 Abs. 1 StVG** – Fahrerhaftung mit Verschuldensvermutung; Entlastung durch Nachweis fehlenden Verschuldens.
4. **§ 823 Abs. 1 BGB** und **§ 823 Abs. 2 BGB** iVm einschlägiger StVO-Norm (z. B. § 4 I StVO als Schutzgesetz).
5. **§ 115 Abs. 1 S. 1 Nr. 1 VVG** – Direktanspruch gegen den Pflichtversicherer.

### 2. Quotelung § 17 StVG bei Beteiligung mehrerer KfZ

Maßstab § 17 Abs. 1, 2 StVG: Abwägung der Verursachungsbeiträge; beidseitige Betriebsgefahr ist Grundausstattung jedes KfZ. Ein „unabwendbares Ereignis" iSv § 17 Abs. 3 StVG schließt die Haftung gegenüber dem Mithalter aus, ist aber selten (Maßstab: Verhalten eines Idealfahrers).

Typische Schemata aus der OLG-Praxis `[unverifiziert – prüfen in juris/Beck-Online]`:

| Konstellation | Tendenzielle Quote (Schädiger : Geschädigter) |
|---|---|
| Auffahrunfall (kein Bremsmanöver des Vorausfahrenden ohne Grund) | 100 : 0 zulasten des Auffahrenden — Anscheinsbeweis (BGH, Urt. v. 13.12.2011 – VI ZR 177/10) `[unverifiziert]` |
| Spurwechsel mit Kollision (§ 7 V StVO) | 75–100 : 0–25 zulasten des Spurwechslers — Anscheinsbeweis |
| Vorfahrtverletzung (§ 8 StVO) | 100 : 0 zulasten des Wartepflichtigen, soweit kein Eigenverschulden des Vorfahrtberechtigten |
| Beidseitige Sorgfaltsverstöße (z. B. unaufmerksames Anfahren) | 50 : 50 |

Wichtig: Die Tabelle ersetzt nicht die Subsumtion im Einzelfall.

### 3. Mitverschulden § 9 StVG iVm § 254 BGB

Mitverschulden des Geschädigten (z. B. nicht angelegter Sicherheitsgurt, überhöhte Geschwindigkeit) mindert den Ersatzanspruch entsprechend. Maßstab: § 254 BGB. Für die Schadensentstehung **und** -höhe gesondert zu prüfen (insbesondere Schadensminderungspflicht).

### 4. Schadensposten §§ 249–254 BGB

**Sachschaden:**

- **Reparatur** (Naturalrestitution § 249 II BGB): brutto nur bei tatsächlicher Reparatur; sonst netto.
- **130%-Grenze:** Reparaturaufwand bis 130% des Wiederbeschaffungswerts (= WBW abzüglich Restwert) ist erstattungsfähig, wenn der Geschädigte das Fahrzeug **tatsächlich reparieren lässt und mindestens 6 Monate weiternutzt** (BGH, st. Rspr., u.a. BGH, Urt. v. 23.05.2017 – VI ZR 9/17, NJW 2017, 2401 `[unverifiziert – prüfen]`).
- **Totalschaden** über 130%: Wiederbeschaffungsaufwand (WBW – Restwert).
- **Sachverständigenkosten** als Teil des Schadens, soweit erforderlich (§ 249 II BGB).
- **Werkstattrisiko**: Überhöhte Werkstattrechnung kann beim Schädiger verbleiben (BGH, Urt. v. 16.01.2024 – VI ZR 38/22 u.a., NJW 2024, … `[unverifiziert – Aktenzeichen prüfen]`).
- **Mietwagenkosten** in Höhe des Normaltarifs (zzgl. unfallspezifischer Mehrkosten, ggf. Schwacke- oder Fraunhofer-Liste).
- **Nutzungsausfall** statt Mietwagen, wenn Geschädigter ohne Ersatzfahrzeug auskommt (Tabelle Sanden/Danner/Küppersbusch).
- **Wertminderung** bei jüngeren Fahrzeugen mit erheblichem Reparaturumfang.

**Personenschaden:**

- Heilbehandlungskosten, Verdienstausfall, Haushaltsführungsschaden.
- **Schmerzensgeld** § 11 StVG iVm § 253 II BGB; Bemessung an Schwere, Dauer, Folgen (Schmerzensgeldtabellen Hacks/Wellner/Häcker als Orientierungswert, `[unverifiziert – prüfen]`).

### 5. Verjährung

§ 14 StVG: 3 Jahre ab Kenntnis (§§ 195, 199 BGB-Parallelität); Hemmung durch Verhandlungen mit dem Versicherer (§ 203 BGB) und durch Rechtshängigkeit.

### 6. Forderungsschreiben an den Pflichtversicherer

- Schadensaufstellung (Sachschaden, Personenschaden) mit Belegen.
- Vorschlag zur Quote mit Begründung.
- Fristsetzung zur Regulierung (idR 4–6 Wochen ab Vorlage des Gutachtens; Verzugseintritt § 286 BGB).

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute

- [§ 7 StVG](https://www.gesetze-im-internet.de/stvg/__7.html) (Halterhaftung)
- [§ 9 StVG](https://www.gesetze-im-internet.de/stvg/__9.html) (Mitverschulden)
- [§ 11 StVG](https://www.gesetze-im-internet.de/stvg/__11.html) (immaterieller Schaden)
- [§ 17 StVG](https://www.gesetze-im-internet.de/stvg/__17.html) (Abwägung mehrere KfZ-Halter)
- [§ 18 StVG](https://www.gesetze-im-internet.de/stvg/__18.html) (Fahrerhaftung)
- [§ 823 BGB](https://www.gesetze-im-internet.de/bgb/__823.html)
- [§ 249 BGB](https://www.gesetze-im-internet.de/bgb/__249.html) (Naturalrestitution, Geldersatz)
- [§ 253 BGB](https://www.gesetze-im-internet.de/bgb/__253.html) (immaterieller Schaden)
- [§ 254 BGB](https://www.gesetze-im-internet.de/bgb/__254.html) (Mitverschulden)
- [§ 115 VVG](https://www.gesetze-im-internet.de/vvg/__115.html) (Direktanspruch)
- [PflVG](https://www.gesetze-im-internet.de/pflvg/) (Pflichtversicherungsgesetz)
- [§ 1 StVO](https://www.gesetze-im-internet.de/stvo_2013/__1.html); [§ 4 StVO](https://www.gesetze-im-internet.de/stvo_2013/__4.html); [§ 7 StVO](https://www.gesetze-im-internet.de/stvo_2013/__7.html); [§ 8 StVO](https://www.gesetze-im-internet.de/stvo_2013/__8.html)

### Kommentare

- König, in: Hentschel/König/Dauer, Straßenverkehrsrecht, 47. Aufl. 2023, § 7 StVG Rn. 1 ff., § 17 StVG Rn. 1 ff.
- Heß, in: Burmann/Heß/Hühnermann/Jahnke, Straßenverkehrsrecht, 28. Aufl. 2024, § 7 StVG Rn. 1 ff.
- Greger/Zwickel, Haftungsrecht des Straßenverkehrs, 6. Aufl. 2021, Kap. 3 Rn. 1 ff.
- Geigel, Der Haftpflichtprozess, 28. Aufl. 2020, Kap. 25 Rn. 1 ff.

### Rechtsprechung (`[unverifiziert – prüfen in juris/Beck-Online]`)

1. BGH, Urt. v. 13.12.2011 – VI ZR 177/10, NJW 2012, 608 (Anscheinsbeweis Auffahrunfall)
2. BGH, Urt. v. 23.05.2017 – VI ZR 9/17, NJW 2017, 2401 (130%-Grenze, Weiternutzung)
3. BGH, Urt. v. 16.01.2024 – VI ZR 38/22 u.a. (Werkstattrisiko)
4. BGH, Urt. v. 11.11.2014 – VI ZR 76/13, NJW 2015, 233 (Schadensminderung Mietwagenkosten)
5. OLG Hamm, Urt. v. 23.02.2018 – 9 U 124/17 (Quotelung Spurwechsel)

## Ausgabeformat

```
HAFTUNGSGUTACHTEN — Verkehrsunfall
Unfall: <Datum, Ort, beteiligte KfZ>

I.   Sachverhalt
II.  Frage(n)
III. Kurzantwort
     – Haftungsquote: <Schädiger> : <Geschädigter>
     – Ersatzanspruch dem Grunde nach: [ja / nein / quotal]

IV.  Rechtliche Bewertung
     1. Anspruch aus § 7 I StVG (Halterhaftung)
        a) „Bei Betrieb"
        b) Haftungsausschluss § 7 II StVG?
     2. Anspruch aus § 18 I StVG (Fahrerhaftung)
        Entlastungsbeweis?
     3. Anspruch aus § 823 I, II BGB
     4. Direktanspruch § 115 VVG
     5. Quotelung § 17 StVG
        a) Verursachungsbeiträge
        b) Beidseitige Betriebsgefahr
        c) Unabwendbares Ereignis § 17 III StVG?
     6. Mitverschulden § 9 StVG iVm § 254 BGB
     7. Schaden
        a) Sachschaden (Reparatur / 130% / WBA / Restwert)
        b) Nutzungsausfall / Mietwagen
        c) Sachverständigenkosten / Wertminderung / Werkstattrisiko
        d) Personenschaden (Heilbehandlung, Verdienstausfall, Haushalt)
        e) Schmerzensgeld § 11 StVG iVm § 253 II BGB

V.   Risiken / offene Punkte
     🟢 / 🟡 / 🔴 <Einstufung mit Begründung>

VI.  Forderungsschreiben (Entwurf)
     – Quote, Schadenshöhe, Fristsetzung § 286 BGB

VII. Quellenverzeichnis
```

## Beispiel (Auszug, Gutachtenstil)

> **III. Kurzantwort.** Mandant (Fahrer 1, Auffahrender) haftet dem Voraus­fahrenden (Fahrer 2) dem Grunde nach zu 100% nach §§ 7 I, 18 I StVG iVm § 115 I 1 Nr. 1 VVG; ein die Quote zugunsten von Fahrer 1 verändernder Sachverhaltsbeitrag des Vorausfahrenden ist nach Aktenlage nicht ersichtlich.
>
> **IV.5. Quotelung § 17 StVG.** Bei einem Auffahrunfall spricht der Beweis des ersten Anscheins gegen den Auffahrenden (BGH, Urt. v. 13.12.2011 – VI ZR 177/10 `[unverifiziert – prüfen]`). Dieser kann nur durch Nachweis eines atypischen Geschehensablaufs entkräftet werden, etwa ein grundloses starkes Abbremsen des Vorausfahrenden. Eine solche Atypie ist nicht ersichtlich, da der Vorausfahrende verkehrsbedingt vor einer Ampelanlage abbremste. Damit verbleibt die Haftung bei Fahrer 1.

## Risiken / typische Fehler

- **Pauschalquote ohne Subsumtion.** Quotenschemata sind Orientierungswerte, nicht Subsumtionsergebnis.
- **130%-Grenze ohne Weiternutzungsnachweis** beansprucht — der BGH verlangt tatsächliche Reparatur und mindestens 6 Monate Weiternutzung.
- **Werkstattrechnung ungeprüft eingereicht** — Schadensminderungspflicht § 254 II BGB; aber Werkstattrisiko verbleibt grds. beim Schädiger.
- **Direktanspruch § 115 VVG übersehen** — getrennte Klage gegen Versicherer und Halter erforderlich (Pflicht-Streitgenossenschaft).
- **Verjährung § 14 StVG / §§ 195, 199 BGB** vergessen; Hemmung durch Verhandlungen § 203 BGB nicht dokumentiert.
- **Mitverschulden Sicherheitsgurt** übersehen — typischer Quotenkürzungsgrund beim Personenschaden.
