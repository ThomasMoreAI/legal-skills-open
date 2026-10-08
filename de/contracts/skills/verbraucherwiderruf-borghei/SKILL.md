---
name: verbraucherwiderruf-borghei
title: /vertragsrecht:verbraucherwiderruf
description: Prüfung und Gestaltung des Verbraucherwiderrufsrechts – Widerrufsrecht bei Fernabsatz und außerhalb von Geschäftsräumen § 312g BGB, Widerrufsfrist § 355 BGB, Fristbeginn und Erlöschen § 356 BGB, Rechtsfolgen §§ 357, 357a BGB einschließlich Wertersatz, Informationspflichten und Muster-Widerrufsbelehrung nach Art. 246a EGBGB sowie Verträge über digitale Produkte §§ 327 ff. BGB. Use when zu klären ist, ob ein Verbraucher widerrufen kann, bis wann die Frist läuft, ob die Belehrung wirksam ist und wie rückabzuwickeln ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/vertragsrecht/skills/verbraucherwiderruf
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: contracts
language: de
---

# /vertragsrecht:verbraucherwiderruf

## Zweck

Das Widerrufsrecht ist der schärfste Hebel des Verbrauchervertragsrechts: Eine fehlerhafte Belehrung lässt die 14-Tage-Frist **nicht anlaufen** und hält den Vertrag bis zur gesetzlichen Höchstfrist widerruflich. Dieser Skill prüft in einer Kette — Verbrauchervertrag? Vertriebsform? Ausnahmetatbestand? Belehrung ordnungsgemäß? Frist abgelaufen? — und berechnet die Rechtsfolgen einschließlich Wertersatz.

## Eingaben

- Parteirollen: Unternehmer (§ 14 BGB) und Verbraucher (§ 13 BGB) — bei gemischter Nutzung überwiegender Zweck
- Vertriebsform: Fernabsatzvertrag (§ 312c BGB), außerhalb von Geschäftsräumen geschlossener Vertrag (§ 312b BGB), Präsenzgeschäft
- Vertragsgegenstand: Ware, Dienstleistung, digitale Inhalte, digitale Dienstleistung, Finanzdienstleistung, Bauvertrag
- Datum des Vertragsschlusses, Datum der Warenlieferung, Datum und Form der Widerrufsbelehrung
- Bereits erfolgte Leistungen, Nutzung der Ware, ausdrückliches Verlangen des vorzeitigen Leistungsbeginns
- Widerrufserklärung: Datum, Form, Inhalt

## Sub-Agent-Architektur

1. **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) liefert Statute (BGB, EGBGB) mit URL, EU-Rechtsgrundlagen (Verbraucherrechte-RL 2011/83/EU, Digitale-Inhalte-RL (EU) 2019/770) und Kommentarstellen.
2. **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) prüft Anwendungsbereich → Ausnahmen → Belehrung → Fristlauf → Rechtsfolgen und entwirft Belehrungstext oder Widerrufsschreiben.
3. **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft Fristberechnung gegen den Rechner, Textformerfordernisse und Vollständigkeit der Pflichtangaben nach Art. 246a EGBGB.

## Ablauf

### 1. Anwendungsbereich ([§ 312 BGB](https://www.gesetze-im-internet.de/bgb/__312.html))

Voraussetzung ist ein **Verbrauchervertrag** nach § 310 Abs. 3 BGB: Unternehmer (§ 14 BGB) auf der einen, Verbraucher (§ 13 BGB) auf der anderen Seite, gerichtet auf eine **entgeltliche Leistung**. Prüfe die Bereichsausnahmen des § 312 Abs. 2–6 BGB (u.a. notariell beurkundete Verträge, bestimmte Miet- und Reiseverträge, Verträge über Gesundheitsdienstleistungen).

- **Fernabsatzvertrag** ([§ 312c BGB](https://www.gesetze-im-internet.de/bgb/__312c.html)): ausschließliche Verwendung von Fernkommunikationsmitteln bei Vertragsanbahnung **und** Vertragsschluss, im Rahmen eines für den Fernabsatz organisierten Vertriebs- oder Dienstleistungssystems.
- **Außerhalb von Geschäftsräumen geschlossener Vertrag** ([§ 312b BGB](https://www.gesetze-im-internet.de/bgb/__312b.html)): gleichzeitige körperliche Anwesenheit außerhalb der Geschäftsräume, Vertragsanbahnung dort mit anschließendem Abschluss in den Geschäftsräumen, oder Abschluss auf einem vom Unternehmer organisierten Ausflug. Der klassische Haustürfall — praktisch relevant auch bei Messeständen und beim Handwerkerbesuch.

**Beide Vertriebsformen führen zum selben Widerrufsrecht, unterscheiden sich aber im Ausnahmekatalog und beim Wertersatz für vorzeitig begonnene Dienstleistungen.**

### 2. Widerrufsrecht und Ausnahmen ([§ 312g BGB](https://www.gesetze-im-internet.de/bgb/__312g.html))

Bei außerhalb von Geschäftsräumen geschlossenen Verträgen und bei Fernabsatzverträgen steht dem Verbraucher ein Widerrufsrecht nach § 355 BGB zu. Der **Ausnahmekatalog des § 312g Abs. 2 BGB** ist eng auszulegen; praxisrelevant:

| Nr. | Ausnahme |
|---|---|
| 1 | Waren nach Kundenspezifikation angefertigt oder eindeutig auf persönliche Bedürfnisse zugeschnitten |
| 2 | Schnell verderbliche Waren oder Waren mit kurzem Verfallsdatum |
| 3 | Versiegelte Waren, die aus Gründen des Gesundheitsschutzes oder der Hygiene nicht zur Rückgabe geeignet sind, wenn die Versiegelung entfernt wurde |
| 6 | Ton- oder Videoaufnahmen und Computersoftware in versiegelter Packung, wenn die Versiegelung entfernt wurde |
| 9 | Dienstleistungen im Zusammenhang mit Freizeitbetätigungen zu einem bestimmten Zeitpunkt |
| 13 | Verträge über die Lieferung von Waren, die nach der Lieferung untrennbar mit anderen Gütern vermischt wurden |

Nicht im Katalog: die bloße **Ingebrauchnahme** einer Ware. Wer benutzt hat, verliert das Widerrufsrecht nicht — er schuldet allenfalls Wertersatz (Ziff. 6).

### 3. Widerrufsfrist ([§ 355 BGB](https://www.gesetze-im-internet.de/bgb/__355.html))

Die Frist beträgt **14 Tage**, wenn nichts anderes bestimmt ist (§ 355 Abs. 2 S. 1 BGB). Der Widerruf erfolgt durch **eindeutige Erklärung** gegenüber dem Unternehmer; eine Begründung ist nicht erforderlich, die **kommentarlose Rücksendung genügt nicht**. Zur Fristwahrung genügt die **rechtzeitige Absendung** (§ 355 Abs. 1 S. 5 BGB) — anders als sonst kommt es nicht auf den Zugang an. Die Beweislast für die rechtzeitige Absendung trägt der Verbraucher.

### 4. Fristbeginn und Erlöschen ([§ 356 BGB](https://www.gesetze-im-internet.de/bgb/__356.html))

| Vertragsgegenstand | Fristbeginn |
|---|---|
| Dienstleistung, digitale Inhalte gegen Zahlung | Vertragsschluss |
| Kaufvertrag über Waren | Erhalt der Ware durch den Verbraucher oder einen benannten Dritten (§ 356 Abs. 2 Nr. 1 BGB) |
| Mehrere Waren in einer Bestellung, getrennt geliefert | Erhalt der **letzten** Ware |
| Ware in mehreren Teilsendungen | Erhalt der **letzten** Teilsendung |
| Regelmäßige Lieferung über festgelegten Zeitraum | Erhalt der **ersten** Ware |

**In keinem Fall beginnt die Frist, bevor der Unternehmer den Verbraucher ordnungsgemäß über sein Widerrufsrecht unterrichtet hat** (§ 356 Abs. 3 S. 1 BGB). Fehlt oder fehlerhaft ist die Belehrung, erlischt das Widerrufsrecht bei Waren und Dienstleistungen spätestens **zwölf Monate und 14 Tage** nach dem regulären Fristbeginn (§ 356 Abs. 3 S. 2 BGB). Bei **Finanzdienstleistungen** gilt diese Höchstfrist nicht — dort besteht das Widerrufsrecht bei fehlerhafter Belehrung fort („ewiges Widerrufsrecht").

### 5. Informationspflichten und Muster-Widerrufsbelehrung ([Art. 246a EGBGB](https://www.gesetze-im-internet.de/bgbeg/art_246a__1.html))

Der Unternehmer schuldet vor Vertragsschluss die Informationen nach **Art. 246a § 1 EGBGB** (wesentliche Eigenschaften, Gesamtpreis, Lieferkosten, Identität und Anschrift, Laufzeit, Kündigungsbedingungen) und **bei bestehendem Widerrufsrecht** zusätzlich Bedingungen, Fristen und Verfahren für die Ausübung, das **Muster-Widerrufsformular** sowie den Hinweis auf die Kostentragung für die Rücksendung.

**Muster-Widerrufsbelehrung (Anlage 1 zu Art. 246a § 1 Abs. 2 S. 2 EGBGB):** Verwendet der Unternehmer das amtliche Muster zutreffend ausgefüllt und in **Textform** (§ 126b BGB), genügt er seiner Belehrungspflicht (**Gesetzlichkeitsfiktion**). Jede eigene Formulierung trägt das volle Risiko der Fehlerhaftigkeit — **von Abweichungen ist dringend abzuraten**. Kernbestandteile:

> „Sie haben das Recht, binnen vierzehn Tagen ohne Angabe von Gründen diesen Vertrag zu widerrufen. Die Widerrufsfrist beträgt vierzehn Tage ab dem Tag, an dem Sie oder ein von Ihnen benannter Dritter, der nicht der Beförderer ist, die Waren in Besitz genommen haben bzw. hat. Um Ihr Widerrufsrecht auszuüben, müssen Sie uns ([Name, Anschrift, Telefonnummer, E-Mail-Adresse des Unternehmers]) mittels einer eindeutigen Erklärung (z. B. ein mit der Post versandter Brief oder E-Mail) über Ihren Entschluss, diesen Vertrag zu widerrufen, informieren. […] Zur Wahrung der Widerrufsfrist reicht es aus, dass Sie die Mitteilung über die Ausübung des Widerrufsrechts vor Ablauf der Widerrufsfrist absenden."

Typische Belehrungsfehler: fehlende **Telefonnummer**, fehlendes Muster-Widerrufsformular, keine Angabe zur Rücksendekostentragung, Belehrung nur in den AGB ohne Textform-Übermittlung, unzutreffender Fristbeginn bei Teillieferungen.

### 6. Rechtsfolgen und Wertersatz ([§ 357 BGB](https://www.gesetze-im-internet.de/bgb/__357.html), [§ 357a BGB](https://www.gesetze-im-internet.de/bgb/__357a.html))

- **Rückgewähr binnen 14 Tagen** beiderseits (§ 357 Abs. 1 BGB). Der Unternehmer kann die Rückzahlung verweigern, bis er die Waren zurückerhalten hat oder der Verbraucher den Absendenachweis erbracht hat (§ 357 Abs. 4 BGB).
- **Rücksendekosten** trägt der Verbraucher, wenn der Unternehmer ihn darüber unterrichtet hat (§ 357 Abs. 6 BGB).
- **Erstattung** hat über dasselbe Zahlungsmittel zu erfolgen, das der Verbraucher eingesetzt hat (§ 357 Abs. 3 BGB).
- **Wertersatz für Waren** ([§ 357a Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__357a.html)): nur für einen **Wertverlust**, der auf einen Umgang mit den Waren zurückzuführen ist, der zur Prüfung ihrer Beschaffenheit, Eigenschaften und Funktionsweise **nicht notwendig** war — und nur, wenn der Unternehmer ordnungsgemäß belehrt hat. Maßstab ist das, was im Ladengeschäft möglich gewesen wäre.
- **Wertersatz für Dienstleistungen** (§ 357a Abs. 2 BGB): nur wenn der Verbraucher den **vorzeitigen Beginn ausdrücklich verlangt** hat — bei außerhalb von Geschäftsräumen geschlossenen Verträgen auf einem dauerhaften Datenträger — und der Unternehmer ordnungsgemäß belehrt hat. Bemessung nach dem vereinbarten Gesamtpreis anteilig zur erbrachten Leistung.

### 7. Digitale Produkte ([§§ 327 ff. BGB](https://www.gesetze-im-internet.de/bgb/__327.html))

Für Verbraucherverträge über **digitale Produkte** (digitale Inhalte und digitale Dienstleistungen) gelten seit dem 01.01.2022 die §§ 327–327u BGB mit eigenem Mangelbegriff (Produktmerkmale § 327e BGB), einer **Aktualisierungspflicht** (§ 327f BGB) und einem Vorrang der Nacherfüllung (§ 327l BGB). Das Widerrufsrecht bleibt daneben anwendbar. Wichtig:

- **Bezahlen mit Daten:** Die §§ 327 ff. BGB erfassen auch Verträge, bei denen der Verbraucher personenbezogene Daten bereitstellt (§ 327 Abs. 3 BGB).
- **Wertersatzausschluss** ([§ 357a Abs. 3 BGB](https://www.gesetze-im-internet.de/bgb/__357a.html)): Bei Verträgen über digitale Inhalte schuldet der Verbraucher **keinen Wertersatz**, wenn er nicht ausdrücklich zugestimmt hat, dass der Unternehmer vor Ablauf der Widerrufsfrist mit der Vertragserfüllung beginnt, wenn er seine Kenntnis vom Erlöschen des Widerrufsrechts nicht bestätigt hat oder wenn der Unternehmer die Bestätigung nach § 312f BGB nicht übermittelt hat.
- **Erlöschen** des Widerrufsrechts bei digitalen Inhalten nach § 356 Abs. 5 BGB unter denselben drei Bedingungen (ausdrückliche Zustimmung, Kenntnisbestätigung, Vertragsbestätigung).

## Deterministische Berechnung

Der Fristlauf ist eine **rechtliche Wertung** (welches Ereignis, ob die Belehrung ordnungsgemäß war). Die Tagesarithmetik nach §§ 187–193 BGB rechnet der deterministische Rechner (siehe [`../../references/rechner.md`](../../references/rechner.md)):

```bash
python -m scripts.legal_calc.cli frist --ereignis 15.01.2026 --menge 2 --einheit wochen --land BY
```

Für die Höchstfrist bei fehlerhafter Belehrung (§ 356 Abs. 3 S. 2 BGB) wird derselbe Aufruf mit `--menge 12 --einheit monate` auf denselben Ereignistag angesetzt und anschließend die 14-Tage-Frist angeschlossen. **Der Rechner entscheidet nicht, ob belehrt wurde oder wann die Ware zugegangen ist — beides ist Eingabe und muss belegt sein.**

## Quellen

### Statute

- [§ 312 BGB](https://www.gesetze-im-internet.de/bgb/__312.html), [§ 312b BGB](https://www.gesetze-im-internet.de/bgb/__312b.html), [§ 312c BGB](https://www.gesetze-im-internet.de/bgb/__312c.html), [§ 312g BGB](https://www.gesetze-im-internet.de/bgb/__312g.html)
- [§ 355 BGB](https://www.gesetze-im-internet.de/bgb/__355.html), [§ 356 BGB](https://www.gesetze-im-internet.de/bgb/__356.html), [§ 357 BGB](https://www.gesetze-im-internet.de/bgb/__357.html), [§ 357a BGB](https://www.gesetze-im-internet.de/bgb/__357a.html)
- [§ 327 BGB](https://www.gesetze-im-internet.de/bgb/__327.html) ff. (Verträge über digitale Produkte), [§ 327c BGB](https://www.gesetze-im-internet.de/bgb/__327c.html)
- [Art. 246a § 1 EGBGB](https://www.gesetze-im-internet.de/bgbeg/art_246a__1.html) (Informationspflichten, Muster-Widerrufsbelehrung Anlage 1)
- RL 2011/83/EU (Verbraucherrechte-RL); RL (EU) 2019/770 (Digitale-Inhalte-RL)

### Kommentare

- Grüneberg, BGB, 83. Aufl. 2024, §§ 312g, 355, 357 Rn. 1 ff. `[unverifiziert – Auflagenstand prüfen]`
- Wendehorst, in: MüKoBGB, 9. Aufl. 2022, § 312g Rn. 1 ff., §§ 327 ff. Rn. 1 ff.
- Müller-Christmann, in: BeckOK BGB, § 355 Rn. 1 ff., § 356 Rn. 1 ff. (Stand prüfen)

### Rechtsprechung

- EuGH, Urt. v. 23.01.2019 – C-430/17 („Walbusch Walter Busch", Belehrungspflichten bei begrenztem Darstellungsraum) `[unverifiziert – prüfen]`
- BGH, Urt. v. 03.11.2010 – VIII ZR 337/09 (Wertersatz bei Ingebrauchnahme im Fernabsatz) `[unverifiziert – prüfen]`

> Beide Fundstellen vor Verwendung in juris / Beck-Online bzw. curia.europa.eu prüfen.

## Ausgabeformat

```
VERBRAUCHERWIDERRUF — <Vertrag> — <Datum>

I.    Verbrauchervertrag (§§ 13, 14)  [✅ / ❌ — Begründung]
II.   Vertriebsform                   [Fernabsatz § 312c / außerhalb Geschäftsräumen § 312b / Präsenz]
III.  Widerrufsrecht (§ 312g I)       [✅ / ❌ Ausnahme § 312g II Nr. <…>]
IV.   Belehrung                       [ordnungsgemäß / fehlerhaft — Mangel: <…>]
        Muster Anlage 1 verwendet:    [ja / nein]
        Textform § 126b:              [ja / nein]
V.    Fristbeginn (§ 356)             <TT.MM.JJJJ> — Anknüpfung: <…>
VI.   Fristende (§ 355 II)            <TT.MM.JJJJ>
        Rechner-Beleg:                <Ausgabe legal_calc frist>
        Höchstfrist § 356 III 2:      <TT.MM.JJJJ> / N/A Finanzdienstleistung
VII.  Widerruf erklärt                [am <Datum>, Form, rechtzeitig abgesandt ✅/❌]
VIII. Rückgewähr (§ 357)              [Beträge, Rücksendekosten, Zurückbehaltung § 357 IV]
IX.   Wertersatz (§ 357a)             [Waren / Dienstleistung / digitale Inhalte — <…> EUR / ausgeschlossen]
X.    Digitale Produkte (§§ 327 ff.)  [N/A / einschlägig — Erlöschen § 356 V]

Gesamtbefund: [🟢 / 🟡 / 🔴]
Offene Tatsachen: <Liste>
```

## Risiken / typische Fehler

- **Belehrung vom Muster abgewichen** — die Gesetzlichkeitsfiktion der Anlage 1 zu Art. 246a § 1 EGBGB entfällt, die Frist läuft nicht an und der Vertrag bleibt bis zur Höchstfrist widerruflich.
- **Fristbeginn bei Teillieferungen falsch angesetzt** — maßgeblich ist der Erhalt der **letzten** Ware bzw. Teilsendung (§ 356 Abs. 2 Nr. 1 BGB), nicht der ersten.
- **Widerrufsrecht wegen Ingebrauchnahme verneint** — Benutzung lässt das Widerrufsrecht unberührt; sie kann allenfalls Wertersatz nach § 357a Abs. 1 BGB auslösen.
- **Wertersatz für vorzeitig begonnene Dienstleistung verlangt** ohne ausdrückliches Verlangen des Verbrauchers und ordnungsgemäße Belehrung — der Anspruch entfällt vollständig (§ 357a Abs. 2 BGB).
- **Höchstfrist auf Finanzdienstleistungen angewendet** — dort greift § 356 Abs. 3 S. 2 BGB nicht; das Widerrufsrecht besteht bei fehlerhafter Belehrung fort.
- **Ausnahmekatalog § 312g Abs. 2 BGB überdehnt** — insbesondere „nach Kundenspezifikation angefertigt" greift nicht schon bei bloßer Auswahl aus Konfiguratoroptionen ohne individuelle Fertigung.
