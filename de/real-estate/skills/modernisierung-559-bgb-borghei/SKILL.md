---
name: modernisierung-559-bgb-borghei
title: /mietrecht:modernisierung-559-bgb
description: Modernisierung und Modernisierungsmieterhöhung im Wohnraummietrecht – Begriff der Modernisierungsmaßnahme § 555b BGB, Modernisierungsankündigung § 555c BGB, Duldungspflicht und Härteeinwand § 555d BGB, Aufwendungsersatz § 555a Abs. 3 BGB, Sonderkündigungsrecht § 555e BGB, Mieterhöhung nach § 559 BGB mit 8-%-Umlage, Kappung § 559 Abs. 3a BGB und Härteeinwand § 559 Abs. 4 BGB, Abgrenzung Erhaltung / Modernisierung, Verhältnis zu § 558 BGB. Use when ein Vermieter eine Modernisierung ankündigt oder umlegt oder ein Mieter Ankündigung, Duldungspflicht und Modernisierungsmieterhöhung prüft.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/mietrecht/skills/modernisierung-559-bgb
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: real-estate
language: de
---

# /mietrecht:modernisierung-559-bgb

## Zweck

Die Modernisierungsmieterhöhung ist das dauerhafteste Instrument des Vermieters — sie ist nicht an die ortsübliche Vergleichsmiete gebunden und wirkt einseitig ohne Zustimmung des Mieters. Genau deshalb ist sie an ein dichtes Verfahren gebunden: Ankündigung, Duldung, Härteprüfung, Umlage. Diese Skill führt durch die gesamte Kette von §§ 555a–555f BGB bis § 559b BGB und trennt scharf zwischen **Erhaltungsaufwand** (nicht umlagefähig) und **Modernisierung** (umlagefähig). Sie ist das Gegenstück zu `/mietrecht:mieterhoehung-558-bgb`: Dieselbe Wohnung, zwei völlig verschiedene Erhöhungsregime.

## Eingaben

- **Maßnahmenbeschreibung**: Was wird gebaut, an welchem Bauteil, mit welchem Ziel
- **Kostenaufstellung** getrennt nach Modernisierungs- und Erhaltungsanteil
- **Ankündigungsschreiben** (Wortlaut, Zugangsdatum) bzw. Entwurf
- **Bauzeitraum**, voraussichtlicher Beginn und Dauer, Umfang der Beeinträchtigung
- **Aktuelle Nettokaltmiete** und Wohnfläche (für die 8-%-Umlage und die Kappung)
- Frühere Erhöhungen nach § 559 BGB in den letzten sechs Jahren
- **Persönliche Lage des Mieters** (Alter, Gesundheit, Einkommen — für Härteeinwand)
- Öffentliche Fördermittel / Zuschüsse (§ 559a BGB — Anrechnung)

## Sub-Agent-Architektur

Die Prüfung wird in Prosa von spezialisierten Schritten getragen; einen `agents`-Block trägt diese Skill bewusst nicht (mietrecht-Konvention). Ein **Qualifikations-Prüfer** ordnet jede einzelne Baumaßnahme dem Katalog des § 555b BGB zu oder verwirft sie als Erhaltungsaufwand — dieser Schritt entscheidet über die gesamte Umlage. Ein **Verfahrens-Prüfer** kontrolliert Ankündigung, Fristen und Duldungsverlangen. Ein **Härte-Prüfer** bewertet den doppelten Härteeinwand: baubezogen nach § 555d Abs. 2 BGB und wirtschaftlich nach § 559 Abs. 4 BGB. Ein **Rechen-Prüfer** ermittelt die umlagefähige Jahresmiete und spiegelt sie gegen die Kappung des § 559 Abs. 3a BGB. Die Trennung ist erforderlich, weil ein Fehler in der Qualifikation den gesamten Rechenweg wertlos macht.

## Ablauf

### 1. Qualifikation der Maßnahme ([§ 555b BGB](https://www.gesetze-im-internet.de/bgb/__555b.html))

Modernisierungsmaßnahmen sind bauliche Veränderungen, durch die

1. **Endenergie nachhaltig eingespart** wird (energetische Modernisierung, Nr. 1),
2. nicht erneuerbare Primärenergie eingespart oder das Klima nachhaltig geschützt wird (Nr. 2),
3. der **Wasserverbrauch** nachhaltig reduziert wird (Nr. 3),
4. der **Gebrauchswert der Mietsache nachhaltig erhöht** wird (Nr. 4),
5. die **allgemeinen Wohnverhältnisse** dauerhaft verbessert werden (Nr. 5),
6. sie aufgrund von Umständen durchgeführt werden, die der Vermieter nicht zu vertreten hat (Nr. 6),
7. **neuer Wohnraum geschaffen** wird (Nr. 7).

### 2. Abgrenzung Erhaltung / Modernisierung ([§ 555a BGB](https://www.gesetze-im-internet.de/bgb/__555a.html))

**Erhaltungsmaßnahmen** halten den vertragsgemäßen Zustand aufrecht oder stellen ihn wieder her. Sie sind vom Mieter zu dulden, aber **nicht umlagefähig** — der Vermieter schuldet sie ohnehin aus § 535 Abs. 1 S. 2 BGB. Bei kombinierten Maßnahmen (typisch: Austausch einer 30 Jahre alten Heizung gegen eine Wärmepumpe) ist der **Erhaltungsanteil herauszurechnen** ([§ 559 Abs. 2 BGB](https://www.gesetze-im-internet.de/bgb/__559.html)); üblich ist eine Schätzung des ersparten Instandsetzungsaufwands. Wer den Erhaltungsanteil nicht ausweist, riskiert die Unwirksamkeit der gesamten Erhöhungserklärung. Aufwendungsersatz des Mieters für Erhaltungsaufwand: § 555a Abs. 3 BGB.

### 3. Modernisierungsankündigung ([§ 555c BGB](https://www.gesetze-im-internet.de/bgb/__555c.html))

Der Vermieter hat die Maßnahme **spätestens drei Monate vor Beginn** in **Textform** anzukündigen. Inhalt nach § 555c Abs. 1 S. 2 BGB:

- **Art und voraussichtlicher Umfang** der Maßnahme in wesentlichen Zügen,
- **voraussichtlicher Beginn und voraussichtliche Dauer**,
- **Betrag der zu erwartenden Mieterhöhung** sowie die voraussichtlichen künftigen **Betriebskosten**.

Die Ankündigung darf nach § 555c Abs. 3 BGB auf anerkannte Pauschalwerte Bezug nehmen. Ohne ordnungsgemäße Ankündigung entsteht **keine Duldungspflicht**; zudem verschiebt sich die Wirkung einer späteren Mieterhöhung um sechs Monate nach hinten ([§ 559b Abs. 2 S. 2 BGB](https://www.gesetze-im-internet.de/bgb/__559b.html)).

### 4. Duldungspflicht und baubezogener Härteeinwand ([§ 555d BGB](https://www.gesetze-im-internet.de/bgb/__555d.html))

Der Mieter hat Modernisierungsmaßnahmen zu **dulden** (§ 555d Abs. 1 BGB). Die Duldungspflicht entfällt, wenn die Maßnahme für ihn, seine Familie oder einen Haushaltsangehörigen eine **Härte** bedeutet, die auch unter Würdigung der berechtigten Interessen des Vermieters und der Belange der Energieeinsparung und des Klimaschutzes nicht zu rechtfertigen ist (Abs. 2). Der Einwand ist **bis zum Ablauf des Monats nach Zugang der Ankündigung in Textform** mitzuteilen (Abs. 3); danach ist er präkludiert, sofern der Mieter die Verspätung nicht nicht zu vertreten hat (Abs. 4). Wichtig: Die **zu erwartende Mieterhöhung** ist in dieser Stufe **nicht** zu berücksichtigen (Abs. 2 S. 2) — sie gehört in § 559 Abs. 4 BGB.

### 5. Sonderkündigungsrecht des Mieters ([§ 555e BGB](https://www.gesetze-im-internet.de/bgb/__555e.html))

Nach Zugang der Ankündigung kann der Mieter das Mietverhältnis **bis zum Ablauf des Monats, der auf den Zugang folgt, zum Ablauf des übernächsten Monats** außerordentlich kündigen. Kündigt er, findet die Maßnahme in seiner Wohnung nicht statt.

### 6. Mieterhöhung nach Modernisierung ([§ 559 BGB](https://www.gesetze-im-internet.de/bgb/__559.html))

Der Vermieter kann die jährliche Miete um **8 % der für die Wohnung aufgewendeten Kosten** erhöhen (§ 559 Abs. 1 BGB). Rechenweg:

1. Gesamtkosten der Maßnahme feststellen.
2. **Erhaltungsanteil abziehen** (§ 559 Abs. 2 BGB).
3. **Drittmittel / Förderung abziehen** ([§ 559a BGB](https://www.gesetze-im-internet.de/bgb/__559a.html)); zinsverbilligte Darlehen anteilig.
4. Auf die einzelne Wohnung **umlegen** (regelmäßig nach Wohnfläche).
5. × 8 % = jährlicher Erhöhungsbetrag; ÷ 12 = monatlicher Erhöhungsbetrag.

### 7. Kappung ([§ 559 Abs. 3a BGB](https://www.gesetze-im-internet.de/bgb/__559.html))

Die monatliche Miete darf sich innerhalb von **sechs Jahren** — Erhöhungen nach §§ 558, 560 BGB nicht eingerechnet — um **nicht mehr als 3 EUR je Quadratmeter Wohnfläche** erhöhen. Liegt die monatliche Ausgangsmiete unter **7 EUR/m²**, beträgt die Grenze **2 EUR je Quadratmeter**. Diese Kappung wirkt unabhängig von der 8-%-Rechnung und ist der praktisch wichtigste Deckel.

### 8. Wirtschaftlicher Härteeinwand ([§ 559 Abs. 4 BGB](https://www.gesetze-im-internet.de/bgb/__559.html))

Die Erhöhung ist ausgeschlossen, soweit sie auch unter Würdigung der berechtigten Interessen des Vermieters für den Mieter eine **wirtschaftliche Härte** bedeuten würde. Der Einwand ist **bis zum Ablauf des Monats nach Zugang der Erhöhungserklärung in Textform** zu erheben (§ 559b Abs. 4 i.V.m. § 555d Abs. 3–5 BGB). Er greift nicht, wenn die Mietsache lediglich in einen allgemein üblichen Zustand versetzt wurde oder die Maßnahme auf Umständen beruht, die der Vermieter nicht zu vertreten hat (Abs. 5).

### 9. Erhöhungserklärung ([§ 559b BGB](https://www.gesetze-im-internet.de/bgb/__559b.html))

Die Erklärung ist in **Textform** abzugeben und die Erhöhung aufgrund der entstandenen Kosten zu **berechnen und zu erläutern**. Sie ist eine **einseitige Gestaltungserklärung** — eine Zustimmung des Mieters ist nicht erforderlich. Die erhöhte Miete ist mit Beginn des **dritten Monats nach Zugang** zu zahlen. Fehlt oder war die Ankündigung fehlerhaft bzw. überschreitet die tatsächliche Erhöhung die angekündigte um mehr als 10 %, verschiebt sich der Zeitpunkt um **sechs Monate** (§ 559b Abs. 2 S. 2 BGB).

### 10. Verhältnis zu § 558 BGB

§ 559 BGB und § 558 BGB stehen **nebeneinander**, dürfen aber nicht in einem Schreiben vermischt werden. Erhöhungen nach § 559 BGB bleiben bei der Kappungsgrenze des § 558 Abs. 3 BGB und bei der 15-Monats-Frist außer Betracht. Umgekehrt darf modernisierungsbedingter Aufwand nicht in ein Vergleichsmietenverlangen eingerechnet werden. Wer beide Wege beschreiten will, muss zwei getrennte Erklärungen abgeben. Gegenstück: `/mietrecht:mieterhoehung-558-bgb`.

## Quellen

### Statute

- [§ 555a BGB](https://www.gesetze-im-internet.de/bgb/__555a.html), [§ 555b BGB](https://www.gesetze-im-internet.de/bgb/__555b.html), [§ 555c BGB](https://www.gesetze-im-internet.de/bgb/__555c.html), [§ 555d BGB](https://www.gesetze-im-internet.de/bgb/__555d.html), [§ 555e BGB](https://www.gesetze-im-internet.de/bgb/__555e.html), [§ 555f BGB](https://www.gesetze-im-internet.de/bgb/__555f.html)
- [§ 559 BGB](https://www.gesetze-im-internet.de/bgb/__559.html), [§ 559a BGB](https://www.gesetze-im-internet.de/bgb/__559a.html), [§ 559b BGB](https://www.gesetze-im-internet.de/bgb/__559b.html)
- [§ 535 BGB](https://www.gesetze-im-internet.de/bgb/__535.html), [§ 558 BGB](https://www.gesetze-im-internet.de/bgb/__558.html), [§ 536 BGB](https://www.gesetze-im-internet.de/bgb/__536.html) (Minderung während der Bauphase)

### Kommentare

- Eisenschmid, in: Schmidt-Futterer, Mietrecht, 15. Aufl. 2023, § 555b BGB Rn. 1 ff.
- Börstinghaus, in: Schmidt-Futterer, Mietrecht, 15. Aufl. 2023, § 559 BGB Rn. 1 ff.
- Artz, in: MüKoBGB, 9. Aufl. 2023, § 555c Rn. 1 ff.; § 559 Rn. 1 ff.
- Weidenkaff, in: Grüneberg, BGB, 84. Aufl. 2025, § 559 Rn. 1 ff.

### Rechtsprechung

- BGH, Urt. v. 18.11.2015 – VIII ZR 266/14 (maßgeblich ist die tatsächliche Wohnfläche — auch für die flächenbezogene Umlage) — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2015-11-18&Aktenzeichen=VIII%20ZR%20266/14
- Zur Abgrenzung von Erhaltungsaufwand und Modernisierung sowie zur Schätzung des Instandsetzungsanteils ist die einschlägige BGH-Rechtsprechung heranzuziehen `[unverifiziert - prüfen]`.
- Zu den Anforderungen an die Erläuterung der Kostenberechnung nach § 559b Abs. 1 S. 2 BGB ist die einschlägige BGH-Rechtsprechung heranzuziehen `[unverifiziert - prüfen]`. Kein Aktenzeichen ohne eigene Verifikation übernehmen.

## Formulierungshilfe — Modernisierungsankündigung (§ 555c BGB)

```
Sehr geehrte Frau …, sehr geehrter Herr …,

hiermit kündige ich Ihnen gemäß § 555c BGB folgende Modernisierungsmaßnahme
an der von Ihnen gemieteten Wohnung <Anschrift> an.

1. Art und Umfang: <z. B. Anbringung eines Wärmedämmverbundsystems an der
   Außenfassade, Dämmstärke <…> cm; Austausch der Fenster gegen
   Dreifachverglasung (Uw <…> W/m²K)>. Es handelt sich um eine Maßnahme
   nach § 555b Nr. 1 BGB (nachhaltige Einsparung von Endenergie).
2. Voraussichtlicher Beginn: <Datum>. Voraussichtliche Dauer: <…> Wochen.
   Beeinträchtigungen: <Gerüst, Arbeiten werktags 8–17 Uhr, …>.
3. Voraussichtliche Mieterhöhung: <Betrag> EUR monatlich. Sie errechnet sich
   aus umlagefähigen Kosten von <…> EUR (nach Abzug des Erhaltungsanteils
   von <…> EUR und der Fördermittel von <…> EUR), 8 % hiervon, umgelegt auf
   Ihre Wohnfläche von <…> m².
4. Voraussichtliche künftige Betriebskosten: <Angabe, insbesondere erwartete
   Einsparung bei den Heizkosten>.

Sie können bis zum Ablauf des auf den Zugang folgenden Monats in Textform
Härtegründe nach § 555d Abs. 2 BGB geltend machen. Auf Ihr Sonderkündigungs-
recht nach § 555e BGB weise ich hin.

Mit freundlichen Grüßen
```

## Ausgabeformat

```
MODERNISIERUNG / § 559 BGB — Prüfung — <Mandat-ID> — <Datum>

I.    Qualifikation (§ 555b)            [Nr. 1 / 2 / 3 / 4 / 5 / 6 / 7 — je Maßnahme]
II.   Abgrenzung Erhaltung              Gesamtkosten:      <Betrag>
                                        ./. Erhaltungsanteil: <Betrag>
                                        ./. Drittmittel (§ 559a): <Betrag>
                                        = umlagefähig:     <Betrag>
III.  Ankündigung (§ 555c)              [✅ / ⚠️ / ❌]
      - Textform, 3 Monate vorher       [✅ / ❌]
      - Art, Umfang, Dauer              [✅ / ⚠️]
      - Erhöhungsbetrag + Betriebskosten [✅ / ⚠️]
IV.   Duldungspflicht (§ 555d)          [besteht / entfällt]
      Härteeinwand baubezogen           [nicht erhoben / fristgerecht / verspätet]
V.    Sonderkündigungsrecht (§ 555e)    Frist Ende: <Datum>
VI.   Erhöhungsbetrag (§ 559 Abs. 1)    8 % von <Betrag> = <Jahresbetrag>
                                        monatlich: <Betrag>
VII.  Kappung (§ 559 Abs. 3a)           Grenze: <3 EUR/m² bzw. 2 EUR/m²>
                                        [eingehalten / überschritten um <Betrag>]
VIII. Wirtschaftliche Härte (§ 559 Abs. 4) [kein / möglich / durchgreifend]
IX.   Erklärung (§ 559b)                Wirksam ab: <Datum>  [+6 Monate? ja/nein]
X.    Verhältnis zu § 558 BGB           [getrennte Erklärung / Vermischung — Rüge]

Ergebnis: <wirksam / teilweise / unwirksam>
Risiko: [🟢 / 🟡 / 🔴]
```

## Risiken / typische Fehler

- **Erhaltungsanteil nicht herausgerechnet** — der häufigste Fehler; führt regelmäßig zur Unwirksamkeit der gesamten Erhöhungserklärung, nicht nur zur Kürzung.
- **Ankündigung unvollständig oder zu spät** — ohne wirksame Ankündigung keine Duldungspflicht und Verschiebung der Mieterhöhung um sechs Monate (§ 559b Abs. 2 S. 2 BGB).
- **Kappung § 559 Abs. 3a BGB übersehen** — die 3-EUR- bzw. 2-EUR-Grenze wirkt unabhängig von der 8-%-Rechnung und wird bei niedrigen Ausgangsmieten regelmäßig zuerst erreicht.
- **Härteeinwände verwechselt** — der baubezogene Einwand des § 555d Abs. 2 BGB berücksichtigt die Mieterhöhung ausdrücklich nicht; der wirtschaftliche Einwand des § 559 Abs. 4 BGB ist gesondert und fristgebunden zu erheben.
- **Härteeinwand-Frist versäumt** — Präklusion nach § 555d Abs. 3 BGB bzw. § 559b Abs. 4 BGB.
- **Fördermittel nicht angerechnet** (§ 559a BGB) — Erhöhung überhöht.
- **§ 558 und § 559 vermischt** — in einem Schreiben kombiniert oder Modernisierungskosten in ein Vergleichsmietenverlangen eingerechnet.
- **Minderung während der Bauphase übersehen** — erhebliche Beeinträchtigungen können nach § 536 BGB die Miete mindern; nur bei energetischer Modernisierung greift die dreimonatige Sperre des § 536 Abs. 1a BGB.
