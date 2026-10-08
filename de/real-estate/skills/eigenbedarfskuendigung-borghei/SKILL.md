---
name: eigenbedarfskuendigung-borghei
title: /mietrecht:eigenbedarfskuendigung
description: Wirksamkeitsprüfung einer Eigenbedarfskündigung im Wohnraummietrecht – berechtigtes Interesse und begünstigter Personenkreis § 573 Abs. 2 Nr. 2 BGB, Begründungspflicht § 573 Abs. 3 BGB, Kündigungsfristen § 573c BGB, Widerspruch und Sozialklausel § 574 BGB, Schadensersatz bei vorgetäuschtem Eigenbedarf. Use when ein Vermieter eine Eigenbedarfskündigung gestaltet oder ein Mieter eine erhaltene Kündigung auf Wirksamkeit und Härtefall prüft.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/mietrecht/skills/eigenbedarfskuendigung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: real-estate
language: de
---

# /mietrecht:eigenbedarfskuendigung

## Zweck

Die Eigenbedarfskündigung ist die praktisch häufigste ordentliche Kündigung des Vermieters — und zugleich die fehleranfälligste. Eine ordentliche Kündigung von Wohnraum setzt ein **berechtigtes Interesse** voraus ([§ 573 Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__573.html)); fehlt es oder ist die Begründung unzureichend, ist die Kündigung unwirksam und das Mietverhältnis läuft weiter. Wer Eigenbedarf nur **vortäuscht**, haftet dem Mieter zudem auf Schadensersatz. Diese Skill prüft die Wirksamkeit aus beiden Perspektiven und beziffert das Schadensersatzrisiko.

## Eingaben

- Kündigungsschreiben (Wortlaut der angegebenen Gründe)
- Begünstigte Person und ihr Verhältnis zum Vermieter (Verwandtschaft, Haushaltszugehörigkeit)
- Konkreter Nutzungswunsch (Wer, wofür, ab wann, warum gerade diese Wohnung)
- Mietdauer / Beginn des Mietverhältnisses (für Kündigungsfrist und Härteabwägung)
- Persönliche Lage des Mieters (Alter, Gesundheit, Verwurzelung — für Sozialklausel)

## Sub-Agent-Architektur

Die Prüfung wird in Prosa von spezialisierten Schritten getragen, nicht von einem `agents`-Block. Ein **Tatbestands-Prüfer** klärt das berechtigte Interesse und den begünstigten Personenkreis, ein **Form-Prüfer** kontrolliert Begründung und Frist, ein **Schutz-Prüfer** bewertet Widerspruch, Sozialklausel und Härtefall, und ein **Missbrauchs-Prüfer** untersucht Anzeichen für vorgetäuschten Eigenbedarf samt Schadensersatzfolge. Die Einzelergebnisse fasst der Ablauf zu einem Gesamturteil zusammen.

## Ablauf

### 1. Berechtigtes Interesse / konkreter Eigenbedarf ([§ 573 Abs. 1, Abs. 2 Nr. 2 BGB](https://www.gesetze-im-internet.de/bgb/__573.html))

Die ordentliche Kündigung ist nur bei berechtigtem Interesse zulässig (Abs. 1). Eigenbedarf liegt vor, wenn der Vermieter die Wohnung **für sich, seine Familienangehörigen oder Angehörige seines Haushalts benötigt** (Abs. 2 Nr. 2). Erforderlich ist ein **konkreter, ernsthafter, vernünftiger und nachvollziehbarer** Nutzungswunsch — nicht bloß ein vorgeschobener oder noch ungewisser. Zu prüfen: Wer soll einziehen, zu welchem Zweck, warum gerade diese Wohnung.

### 2. Begünstigter Personenkreis ([§ 573 Abs. 2 Nr. 2 BGB](https://www.gesetze-im-internet.de/bgb/__573.html))

Der **begünstigter Personenkreis** ist auf den Vermieter selbst, seine Familienangehörigen und die Angehörigen seines Haushalts begrenzt. Privilegierte Familienangehörige sind insbesondere Kinder, Eltern, Geschwister und Enkel; bei entfernteren Verwandten ist eine konkrete soziale Bindung darzulegen. Die im Test genannte **Tochter** zählt unproblematisch zum privilegierten Kreis. Personen außerhalb dieses Kreises tragen keinen Eigenbedarf.

### 3. Form und Begründung ([§ 573 Abs. 3 BGB](https://www.gesetze-im-internet.de/bgb/__573.html), § 568 BGB)

Die Kündigung bedarf der **Schriftform** (§ 568 Abs. 1 BGB). Die Gründe des berechtigten Interesses sind nach **§ 573 Abs. 3 BGB im Kündigungsschreiben anzugeben**. Die **Begründung** muss die begünstigte Person und das Nutzungsinteresse so konkret bezeichnen, dass der Mieter sie auf Plausibilität prüfen kann. Das bloße Stichwort „Eigenbedarf" ohne nähere Angaben — wie im Test — genügt **nicht** und macht die Kündigung formell unwirksam.

### 4. Kündigungsfrist ([§ 573c BGB](https://www.gesetze-im-internet.de/bgb/__573c.html))

Es gelten die gesetzlichen Fristen des **§ 573c BGB**: Grundfrist **drei Monate**; sie verlängert sich auf **sechs Monate nach fünf Jahren** und auf **neun Monate nach acht Jahren** Überlassungsdauer. Maßgeblich ist der Zugang spätestens am dritten Werktag eines Monats zum Ablauf des übernächsten Monats. Bei einer langjährigen Mieterin ist regelmäßig die Neun-Monats-Frist einschlägig.

### 5. Widerspruch und Sozialklausel ([§ 574 BGB](https://www.gesetze-im-internet.de/bgb/__574.html))

Auch eine formell wirksame Kündigung kann am **Widerspruch** des Mieters scheitern. Die **Sozialklausel** des **§ 574 BGB** gibt dem Mieter das Recht, der Kündigung zu widersprechen und die **Fortsetzung des Mietverhältnisses** zu verlangen, wenn die Beendigung für ihn, seine Familie oder einen Haushaltsangehörigen eine **Härte** bedeutet, die auch unter Würdigung der berechtigten Interessen des Vermieters nicht zu rechtfertigen ist. Der Widerspruch ist form- und fristgebunden (§ 574b BGB: schriftlich, spätestens zwei Monate vor Beendigung). Ein **Härtefall** kommt namentlich bei hohem Alter, Krankheit, Gebrechlichkeit, langer Mietdauer oder fehlendem angemessenen Ersatzwohnraum in Betracht — die **80-jährige Mieterin** des Tests ist ein typischer Anwendungsfall. Rechtsfolge: Fortsetzung auf bestimmte oder unbestimmte Zeit (§ 574a BGB).

### 6. Rechtsmissbrauch / vorgetäuschter Eigenbedarf + Schadensersatz

Die Kündigung ist rechtsmissbräuchlich und unwirksam, wenn der Eigenbedarf nur vorgeschoben ist. Stellt sich nach Auszug heraus, dass der behauptete Bedarf nie bestand, liegt ein **vorgetäuschter Eigenbedarf** vor: Der Vermieter haftet dem Mieter auf **Schadensersatz** nach § 280 Abs. 1 BGB (Umzugs-, Makler-, Mehrkosten). Leitentscheidung: **BGH, Urt. v. 10.06.2015 – VIII ZR 99/14** ([dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2015-06-10&Aktenzeichen=VIII%20ZR%2099/14)). Fällt der Eigenbedarf vor Ablauf der Kündigungsfrist weg, trifft den Vermieter eine gesteigerte Mitteilungs- und Darlegungslast (BGH – VIII ZR 44/16 `[unverifiziert - prüfen]`). Indizien für Vortäuschung: fehlender tatsächlicher Einzug, alsbaldige Weitervermietung oder Verkauf, wechselnde Begründungen.

### 7. Ergebnis

Zusammenführung: Liegt ein konkreter Eigenbedarf für eine privilegierte Person vor, ist die Form gewahrt und die Frist eingehalten — und greift kein durchgreifender Härtefall? Erst wenn alle Stufen bestehen, ist die Kündigung wirksam und durchsetzbar.

## Risiken

- **Begründung zu pauschal** (nur Stichwort „Eigenbedarf") → formell unwirksam, § 573 Abs. 3 BGB.
- **Begünstigte Person außerhalb des privilegierten Kreises** → kein Eigenbedarf.
- **Kündigungsfrist nach § 573c BGB falsch berechnet** (Staffelung 3/6/9 Monate übersehen) → Beendigungszeitpunkt unwirksam.
- **Härtefall / Sozialklausel unterschätzt** → Mieter erzwingt Fortsetzung nach § 574 BGB.
- **Vorgetäuschter Eigenbedarf** → Unwirksamkeit *und* Schadensersatz (BGH, Urt. v. 10.06.2015 – VIII ZR 99/14, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=10.06.2015&Aktenzeichen=VIII%20ZR%2099/14)).
- **Wegfall des Eigenbedarfs während der Frist nicht mitgeteilt** → Schadensersatzrisiko.

## Quellen

### Statute

- [§ 573 BGB](https://www.gesetze-im-internet.de/bgb/__573.html), [§ 573c BGB](https://www.gesetze-im-internet.de/bgb/__573c.html), [§ 574 BGB](https://www.gesetze-im-internet.de/bgb/__574.html)

### Rechtsprechung

- BGH, Urt. v. 10.06.2015 – VIII ZR 99/14, NJW 2015, 2324 = NZM 2015, 532 (Schadensersatz bei vorgetäuschtem Eigenbedarf, § 280 Abs. 1 BGB), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=10.06.2015&Aktenzeichen=VIII%20ZR%2099/14)
- BGH – VIII ZR 44/16 `[unverifiziert - prüfen]` (gesteigerte Darlegungslast bei Wegfall des Eigenbedarfs)

## Ausgabeformat

```
EIGENBEDARFSKÜNDIGUNG — Prüfung — <Mandat-ID> — <Datum>

I.   Berechtigtes Interesse / Eigenbedarf (§ 573 Abs. 2 Nr. 2)   [✅ / ❌]
II.  Begünstigter Personenkreis                                  [privilegiert / nein]
III. Form + Begründung (§ 573 Abs. 3)                            [✅ / ⚠️ / ❌]
IV.  Kündigungsfrist (§ 573c)                                    [3 / 6 / 9 Monate] → Ende <Datum>
V.   Widerspruch / Sozialklausel / Härtefall (§ 574)             [kein / möglich / durchgreifend]
VI.  Rechtsmissbrauch / vorgetäuschter Eigenbedarf               [kein Anhalt / Indizien]
     Schadensersatzrisiko (§ 280, VIII ZR 99/14)                 [🟢 / 🟡 / 🔴]

Ergebnis: <wirksam / unwirksam / schwebend>
Empfehlung: <…>
```
