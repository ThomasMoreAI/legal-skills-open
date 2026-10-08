---
name: pflichtteil-pruefung-borghei
title: /erbrecht:pflichtteil-pruefung
description: Prüfung und Berechnung des Pflichtteils im deutschen Erbrecht – Pflichtteilsanspruch § 2303 BGB, Pflichtteilsquote (halber gesetzlicher Erbteil), Nachlassbewertung § 2311 BGB, Zusatz- und Ergänzungsansprüche §§ 2305, 2325 BGB, Auskunftsanspruch § 2314 BGB, Verjährung § 2332 BGB. Use when ein enterbter Pflichtteilsberechtigter seinen Anspruch geltend macht oder ein Erbe ein Pflichtteilsverlangen prüft.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/erbrecht/skills/pflichtteil-pruefung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: trusts-and-estates
language: de
---

# /erbrecht:pflichtteil-pruefung

## Zweck

Der Pflichtteil sichert den nächsten Angehörigen eine Mindestbeteiligung am Nachlass, auch wenn der Erblasser sie testamentarisch enterbt hat. Er ist kein Erbteil, sondern ein **schuldrechtlicher Geldanspruch** gegen den oder die Erben. Streit entsteht typischerweise über die Höhe (Nachlassbewertung), über lebzeitige Schenkungen (Ergänzung) und über die Verjährung. Dieser Skill prüft Berechtigung, Quote und Berechnung systematisch und deckt die häufig übersehenen Zusatz- und Ergänzungsansprüche ab.

## Eingaben

- Erblasser (Todeszeitpunkt, letzter Wohnsitz)
- Verwandtschaftsverhältnis des Anspruchstellers (Abkömmling / Elternteil / Ehegatte)
- Güterstand des Erblassers (Zugewinngemeinschaft / Gütertrennung / Gütergemeinschaft)
- Nachlasswert (Aktiva und Passiva zum Todestag)
- Schenkungen des Erblassers in den letzten 10 Jahren (Empfänger, Datum, Wert)
- Testament / Erbvertrag und Inhalt der Enterbung oder Beschränkung
- Erbverzichts- oder Pflichtteilsverzichtsverträge

## Sub-Agent-Architektur

Die Prüfung läuft über drei kooperierende Rollen. Der **Researcher** ermittelt den Sachverhalt: Verwandtschaftsverhältnis, gesetzliche Erbquote, Güterstand, Nachlassbestand zum Stichtag und sämtliche relevanten Schenkungen der letzten zehn Jahre. Der **Drafter** berechnet daraus die Pflichtteilsquote (halber gesetzlicher Erbteil), den Nachlasswert nach § 2311 BGB, etwaige Ergänzungs- und Zusatzansprüche und formuliert den Auskunfts- und Zahlungsanspruch. Der **Reviewer** kontrolliert Bewertungsstichtag, Abschmelzung der Schenkungen, Verjährungslauf und ob ein Entziehungs- oder Verzichtsgrund den Anspruch entfallen lässt; er kennzeichnet jede nicht gesichert verifizierte Rechtsprechung mit `[unverifiziert – prüfen]`.

## Ablauf

### 1. Pflichtteilsberechtigung ([§ 2303 BGB](https://www.gesetze-im-internet.de/bgb/__2303.html))

Pflichtteilsberechtigte sind abschließend:

- **Abkömmlinge** des Erblassers (Kinder, bei deren Wegfall Enkel — Repräsentationsprinzip),
- die **Eltern** des Erblassers (nur wenn keine Abkömmlinge vorhanden sind),
- der **Ehegatte** (bzw. eingetragene Lebenspartner).

Voraussetzung: Die Person ist durch Verfügung von Todes wegen von der Erbfolge **ausgeschlossen** (enterbt). Geschwister, Lebensgefährten und entferntere Verwandte sind **nicht** pflichtteilsberechtigt. Der Anspruch richtet sich als Geldforderung gegen den Erben.

### 2. Pflichtteilsquote = halber gesetzlicher Erbteil

Die **Pflichtteilsquote** beträgt die **Hälfte des gesetzlichen Erbteils** (§ 2303 Abs. 1 S. 2 BGB). Sie wird in zwei Schritten ermittelt:

1. Gesetzlichen Erbteil nach §§ 1924 ff. BGB bestimmen — abhängig von der Zahl der Miterben und vom Güterstand.
2. Diesen Erbteil **halbieren**.

Beim Ehegatten ist der Güterstand entscheidend: In der Zugewinngemeinschaft erhöht sich der gesetzliche Erbteil pauschal um ein Viertel (§ 1371 Abs. 1 BGB); für die Pflichtteilsquote ist von diesem **erhöhten** gesetzlichen Erbteil auszugehen (großer Pflichtteil), sofern der Ehegatte nicht Erbe oder Vermächtnisnehmer wird.

> Beispiel: Alleiniger Sohn, der Erblasser hinterlässt keinen Ehegatten. Gesetzlicher Erbteil = 1/1. Pflichtteilsquote = 1/2.

### 3. Nachlasswert und Bewertungsstichtag ([§ 2311 BGB](https://www.gesetze-im-internet.de/bgb/__2311.html))

- Maßgeblich ist der **Bestand und Wert des Nachlasses zur Zeit des Erbfalls** (Todestag) — nicht der Wert bei späterer Auseinandersetzung.
- Anzusetzen ist der **objektive Verkehrswert** (gemeiner Wert); Wertangaben des Erblassers sind unbeachtlich.
- Vom Aktivnachlass sind die **Nachlassverbindlichkeiten** (Erblasserschulden, Beerdigungskosten, Erbfallschulden) abzuziehen.
- Soweit nötig, ist der Wert durch **Schätzung** zu ermitteln (Sachverständigengutachten bei Immobilien / Unternehmen).
- Der Pflichtteil ergibt sich als: **Pflichtteilsquote × bereinigter Nachlasswert**.

### 4. Pflichtteilsergänzung bei Schenkungen ([§ 2325 BGB](https://www.gesetze-im-internet.de/bgb/__2325.html))

Hat der Erblasser zu Lebzeiten verschenkt, kann der Berechtigte den Betrag verlangen, um den sich der Pflichtteil erhöht, wenn die Schenkung dem Nachlass hinzugerechnet wird (**Pflichtteilsergänzung**).

- **Abschmelzung (Pro-rata-Regel, § 2325 Abs. 3 BGB):** Die Schenkung wird im ersten Jahr vor dem Erbfall voll, danach für jedes weitere Jahr um **1/10 weniger** berücksichtigt. Nach **10 Jahren** bleibt die Schenkung unberücksichtigt.

| Jahre vor dem Erbfall | berücksichtigter Anteil |
|---|---|
| im 1. Jahr | 10/10 (100 %) |
| im 2. Jahr | 9/10 |
| im 3. Jahr | 8/10 |
| … | … |
| im 10. Jahr | 1/10 |
| ab 10 Jahre | 0 |

- **Ehegatten-Sonderfall:** Bei Schenkungen an den Ehegatten beginnt die Frist nicht vor Auflösung der Ehe (§ 2325 Abs. 3 S. 3 BGB) — die Abschmelzung läuft also bei fortbestehender Ehe nicht.
- **Bewertung:** Verbrauchbare Sachen mit dem Wert zur Zeit der Schenkung; sonst Niederstwertprinzip (Wert zur Zeit des Erbfalls, höchstens jedoch zur Zeit der Schenkung).

### 5. Zusatzpflichtteil ([§ 2305 BGB](https://www.gesetze-im-internet.de/bgb/__2305.html))

Ist der Berechtigte zwar als Erbe eingesetzt, aber mit einem Erbteil, der **kleiner als die Hälfte des gesetzlichen Erbteils** ist, schuldet ihm der Erbe den Unterschiedsbetrag zwischen hinterlassenem Erbteil und Pflichtteilsquote als **Zusatzpflichtteil**. Beschränkungen und Beschwerden (z. B. Teilungsanordnungen) bleiben bei der Wertberechnung außer Betracht.

### 6. Auskunftsanspruch ([§ 2314 BGB](https://www.gesetze-im-internet.de/bgb/__2314.html))

Der nicht zum Erben berufene Pflichtteilsberechtigte kann vom Erben verlangen:

- **Auskunft über den Bestand des Nachlasses** (geordnetes Bestandsverzeichnis),
- auf Verlangen Hinzuziehung bei der Aufnahme und notarielle Aufnahme des Verzeichnisses,
- **Wertermittlung** der Nachlassgegenstände (Sachverständiger).

Der Auskunftsanspruch umfasst auch ergänzungspflichtige Schenkungen. Kosten trägt der Nachlass. Praktisch geht dem Zahlungsanspruch regelmäßig eine **Stufenklage** (Auskunft → Wertermittlung → Zahlung) voraus.

### 7. Verjährung ([§ 2332 BGB](https://www.gesetze-im-internet.de/bgb/__2332.html))

- Pflichtteils- und Pflichtteilsergänzungsansprüche unterliegen der **Regelverjährung** von **3 Jahren** ([§ 195 BGB](https://www.gesetze-im-internet.de/bgb/__195.html)), beginnend mit dem Schluss des Jahres, in dem der Berechtigte von Erbfall und beeinträchtigender Verfügung Kenntnis erlangt ([§ 199 Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__199.html)).
- § 2332 BGB regelt nur noch den **Sonderfall** des Anspruchs gegen den Beschenkten (§ 2329 BGB): Verjährung beginnt mit dem Erbfall, ohne Rücksicht auf Kenntnis.
- **Höchstfrist:** kenntnisunabhängig spätestens 30 Jahre ab Erbfall (§ 199 Abs. 3a BGB).

### 8. Pflichtteilsentziehung ([§ 2333 BGB](https://www.gesetze-im-internet.de/bgb/__2333.html))

Der Erblasser kann einem Abkömmling den Pflichtteil **entziehen**, wenn dieser u. a.

- dem Erblasser, dem Ehegatten oder einem nahestehenden Menschen **nach dem Leben trachtet**,
- sich eines **schweren vorsätzlichen Vergehens** gegen diese Personen schuldig macht,
- die gesetzliche **Unterhaltspflicht** böswillig verletzt oder
- wegen einer vorsätzlichen Straftat zu **mindestens einem Jahr Freiheitsstrafe** ohne Bewährung verurteilt wird und die Teilhabe am Nachlass unzumutbar ist.

Der **Entziehungsgrund muss im Testament konkret angegeben** werden und im Zeitpunkt der Errichtung bestehen (§ 2336 BGB). Die Beweislast trägt, wer aus der Entziehung Rechte herleitet.

## Quellen

### Statute

- [§ 2303 BGB](https://www.gesetze-im-internet.de/bgb/__2303.html) (Pflichtteilsberechtigte; Höhe)
- [§ 2305 BGB](https://www.gesetze-im-internet.de/bgb/__2305.html) (Zusatzpflichtteil)
- [§ 2311 BGB](https://www.gesetze-im-internet.de/bgb/__2311.html) (Wert des Nachlasses)
- [§ 2314 BGB](https://www.gesetze-im-internet.de/bgb/__2314.html) (Auskunftspflicht des Erben)
- [§ 2325 BGB](https://www.gesetze-im-internet.de/bgb/__2325.html) (Pflichtteilsergänzung bei Schenkungen)
- [§ 2329 BGB](https://www.gesetze-im-internet.de/bgb/__2329.html) (Anspruch gegen den Beschenkten)
- [§ 2332 BGB](https://www.gesetze-im-internet.de/bgb/__2332.html) (Verjährung) i. V. m. [§§ 195, 199 BGB](https://www.gesetze-im-internet.de/bgb/__195.html)
- [§ 2333 BGB](https://www.gesetze-im-internet.de/bgb/__2333.html), [§ 2336 BGB](https://www.gesetze-im-internet.de/bgb/__2336.html) (Pflichtteilsentziehung)
- [§ 1371 BGB](https://www.gesetze-im-internet.de/bgb/__1371.html) (Zugewinnausgleich im Todesfall)

### Kommentare

- Lange, in: MüKoBGB, 9. Aufl. 2022, § 2303 Rn. 1 ff.
- Müller-Engels, in: Burandt / Rojahn, Erbrecht, 4. Aufl. 2022, § 2325
- Damrau / Tanck, Praxiskommentar Erbrecht, § 2325 (Abschmelzung)

### Rechtsprechung

- BGH, Urt. v. 23.05.2012 – IV ZR 250/11, NJW 2012, 2730 (Pflichtteilsergänzung, Abschmelzung) `[unverifiziert – prüfen]`
- BGH, Urt. v. 08.07.1993 – IX ZR 116/92 (Auskunft § 2314) `[unverifiziert – prüfen]`

## Risiken / typische Fehler

- **Pflichtteilsergänzung § 2325 BGB übersehen** — lebzeitige Schenkungen der letzten 10 Jahre erhöhen den Anspruch; Abschmelzung beachten.
- **Ehegatten-Schenkung falsch abgeschmolzen** — bei fortbestehender Ehe läuft die 10-Jahres-Frist nicht.
- **Falscher Bewertungsstichtag** — maßgeblich ist der Todestag (§ 2311 BGB), nicht der Zeitpunkt der Auseinandersetzung.
- **Verjährung § 2332 / §§ 195, 199 BGB verpasst** — 3 Jahre ab Schluss des Kenntnisjahres.
- **Güterstand ignoriert** — beim Ehegatten ändert § 1371 BGB die gesetzliche Erbquote und damit die Pflichtteilsquote.
- **Zusatzpflichtteil § 2305 BGB nicht geltend gemacht** — zu gering bedachter Miterbe hat Anspruch auf den Differenzbetrag.
- **Pflichtteilsentziehung § 2333 BGB ohne Grundangabe** — Entziehung ohne konkret im Testament benannten Grund ist unwirksam.

## Ausgabeformat

```
PFLICHTTEIL-PRÜFUNG — <Mandat / Erbfall> — <Datum>

I.    Pflichtteilsberechtigung § 2303    [Abkömmling / Eltern / Ehegatte — ja / nein]
II.   Gesetzlicher Erbteil               <Quote, Güterstand § 1371 berücksichtigt>
      Pflichtteilsquote                   <= halber gesetzlicher Erbteil>
III.  Nachlasswert § 2311 (Stichtag Tod)
      Aktiva / Passiva:                   <…>
      Bereinigter Nachlasswert:           <EUR>
      Bewertungsstichtag:                 [Todestag ✓]
IV.   Pflichtteil (Quote × Wert):         <EUR>
V.    Pflichtteilsergänzung § 2325
      Schenkungen < 10 Jahre:             <Liste, Datum, Wert>
      Abschmelzung:                        [n/10 je Schenkung]
      Ergänzungsbetrag:                    <EUR>
VI.   Zusatzpflichtteil § 2305            [anwendbar / nicht]
VII.  Auskunftsanspruch § 2314            [geltend gemacht / Stufenklage]
VIII. Verjährung § 2332 / §§ 195, 199     [läuft bis … / verjährt]
IX.   Entziehung / Verzicht § 2333        [Grund benannt? / kein Grund]

Gesamtanspruch:  <EUR>
Empfehlung: <Auskunftsstufe / Zahlungsverlangen / Verteidigung des Erben>
```
