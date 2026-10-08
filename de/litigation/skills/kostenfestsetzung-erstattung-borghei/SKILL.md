---
name: kostenfestsetzung-erstattung-borghei
title: /kostenrecht-rvg:kostenfestsetzung-erstattung
description: Kostenerstattung im Zivilprozess – Kostengrundentscheidung §§ 91 bis 101 ZPO einschließlich Erledigung § 91a ZPO, Teilunterliegen § 92 ZPO und sofortigem Anerkenntnis § 93 ZPO, Notwendigkeit der Kosten § 91 Abs. 1 ZPO, Reisekosten und mehrere Anwälte, Kostenfestsetzungsverfahren §§ 103 bis 107 ZPO, Erinnerung und sofortige Beschwerde § 104 Abs. 3 ZPO, Kostenausgleichung § 106 ZPO sowie Streitwertbeschwerde § 68 GKG, mit deterministischer Gegenrechnung über scripts/legal_calc. Use when ein Kostenfestsetzungsantrag zu stellen, eine gegnerische Kostenrechnung zu prüfen oder ein Festsetzungsbeschluss anzugreifen ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/kostenrecht-rvg/skills/kostenfestsetzung-erstattung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: litigation
language: de
---

# /kostenrecht-rvg:kostenfestsetzung-erstattung

## Zweck

Die Kostenerstattung läuft in zwei streng getrennten Stufen ab: Das Prozessgericht entscheidet **dem Grunde nach**, wer die Kosten trägt; der Rechtspfleger setzt **der Höhe nach** fest, welche Beträge erstattungsfähig sind. Wer beide Ebenen vermengt, verliert im Festsetzungsverfahren mit Einwänden, die in die Kostengrundentscheidung gehört hätten. Dieser Skill erstellt den Kostenfestsetzungsantrag, prüft eine gegnerische Aufstellung auf Notwendigkeit und benennt den richtigen Rechtsbehelf.

## Eingaben

- Kostengrundentscheidung: Tenor im Wortlaut, Datum, Rechtskraft oder vorläufige Vollstreckbarkeit
- Festgesetzter Streitwert (§ 63 GKG) und ob dagegen vorgegangen wird
- Eigene und gegnerische Kostenpositionen mit VV-Nummern
- Sitz der Partei und des Prozessbevollmächtigten (Reisekostenfrage)
- Anwaltswechsel, Verkehrsanwalt, Terminsvertreter im Verfahren?
- Vorsteuerabzugsberechtigung der erstattungsberechtigten Partei
- Bei Quotelung: die genauen Quoten für die Ausgleichung nach § 106 ZPO

## Sub-Agent-Architektur

Der **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) ordnet den Kostentenor der einschlägigen Norm zu (§§ 91 bis 101 ZPO) und belegt die Erstattungsfähigkeit der einzelnen Positionen. Der **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) erstellt den Kostenfestsetzungsantrag nebst Aufstellung und Erklärung zum Vorsteuerabzug. Der **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft Fristen der Rechtsbehelfe, Beschwerdewert und die Übereinstimmung von Tenor und Quote.

## Ablauf

### 1. Kostengrundentscheidung lesen ([§ 91 ZPO](https://www.gesetze-im-internet.de/zpo/__91.html))

Die unterliegende Partei trägt die Kosten des Rechtsstreits, insbesondere die dem Gegner erwachsenen Kosten, **soweit sie zur zweckentsprechenden Rechtsverfolgung oder Rechtsverteidigung notwendig waren**. Sonderfälle:

| Konstellation | Norm | Folge |
|---|---|---|
| Teilweises Obsiegen | [§ 92 ZPO](https://www.gesetze-im-internet.de/zpo/__92.html) | Quotelung oder Aufhebung gegeneinander |
| Sofortiges Anerkenntnis ohne Klageanlass | [§ 93 ZPO](https://www.gesetze-im-internet.de/zpo/__93.html) | Kläger trägt die Kosten |
| Übereinstimmende Erledigungserklärung | [§ 91a ZPO](https://www.gesetze-im-internet.de/zpo/__91a.html) | Entscheidung nach billigem Ermessen |
| Klagerücknahme | [§ 269 Abs. 3 ZPO](https://www.gesetze-im-internet.de/zpo/__269.html) | Kläger trägt die Kosten |
| Erfolgloses Angriffsmittel | [§ 96 ZPO](https://www.gesetze-im-internet.de/zpo/__96.html) | Kosten auch dem Obsiegenden auferlegbar |
| Streitgenossen | [§ 100 ZPO](https://www.gesetze-im-internet.de/zpo/__100.html) | nach Kopfteilen, ggf. Haftungsanteile |
| Nebenintervention | [§ 101 ZPO](https://www.gesetze-im-internet.de/zpo/__101.html) | Kosten des Streithelfers |

Der Tenor ist **wörtlich** in den Antrag zu übernehmen. Eine Quote von „4/5 zu 1/5" wird nicht umgerechnet, sondern in die Ausgleichung eingestellt.

### 2. Notwendigkeit der einzelnen Positionen prüfen (§ 91 Abs. 1 S. 1, Abs. 2 ZPO)

- **Anwaltsgebühren** sind nach § 91 Abs. 2 S. 1 ZPO **stets** in Höhe der gesetzlichen Vergütung zu erstatten; eine Vergütungsvereinbarung geht darüber hinaus zu Lasten der eigenen Partei.
- **Reisekosten** eines nicht am Ort des Prozessgerichts und nicht am Wohnort der Partei ansässigen Anwalts sind nur erstattungsfähig, soweit die Zuziehung **notwendig** war (§ 91 Abs. 2 S. 1 Hs. 2 ZPO). Maßstab ist, ob eine vernünftige Partei die Mehrkosten aufgewandt hätte.
- **Mehrere Rechtsanwälte:** Kosten sind nur insoweit zu erstatten, als sie die Kosten **eines** Rechtsanwalts nicht übersteigen oder in der Person des Anwalts ein Wechsel notwendig wurde (§ 91 Abs. 2 S. 2 ZPO). Terminsvertreter sind bis zur Höhe der ersparten Reisekosten erstattungsfähig.
- **Reisekosten der Partei** zum Termin sind erstattungsfähig, soweit ihr persönliches Erscheinen angeordnet war oder sachlich geboten erschien.
- **Umsatzsteuer** nur, wenn die Partei zum Vorsteuerabzug **nicht** berechtigt ist; darüber ist nach [§ 104 Abs. 2 S. 3 ZPO](https://www.gesetze-im-internet.de/zpo/__104.html) eine Erklärung abzugeben, die die Glaubhaftmachung ersetzt.

### 3. Kostenfestsetzungsantrag stellen ([§ 103 ZPO](https://www.gesetze-im-internet.de/zpo/__103.html))

Der Anspruch wird aufgrund eines zur Zwangsvollstreckung geeigneten Titels geltend gemacht. Antrag und Kostenaufstellung sind bei dem Gericht des ersten Rechtszuges einzureichen; zuständig ist funktionell der **Rechtspfleger** (§ 21 Nr. 1 RPflG).

```
An das Landgericht <Ort>
— Rechtspfleger —
Az. <…>

In dem Rechtsstreit <Kläger> ./. <Beklagter>

beantrage ich namens der <obsiegenden Partei>, die von der
<erstattungspflichtigen Partei> zu erstattenden Kosten gemäß dem
Urteil vom <Datum> (Kostentenor: <wörtlich>) wie folgt festzusetzen:

Gegenstandswert: <…> EUR

I.    1,3 Verfahrensgebühr        VV 3100        <…> EUR
II.   1,2 Terminsgebühr           VV 3104        <…> EUR
III.  Post-/Telekommunikations-
      pauschale                   VV 7002         <…> EUR
IV.   Reisekosten Termin vom <…>  VV 7003 ff.     <…> EUR
V.    Gerichtskostenvorschuss     KV 1210         <…> EUR
                                               ---------
      Zwischensumme                              <…> EUR
VI.   19 % Umsatzsteuer           VV 7008         <…> EUR
                                               =========
      Gesamt                                     <…> EUR

Es wird beantragt, den festgesetzten Betrag gemäß § 104 Abs. 1 S. 2
ZPO ab Eingang dieses Antrags mit fünf Prozentpunkten über dem
Basiszinssatz zu verzinsen.

Erklärung nach § 104 Abs. 2 S. 3 ZPO: Die Antragstellerin ist zum
Vorsteuerabzug nicht berechtigt.

<Ort, Datum, Unterschrift>
```

### 4. Festsetzungsverfahren und Verzinsung ([§ 104 ZPO](https://www.gesetze-im-internet.de/zpo/__104.html))

Der festgesetzte Betrag ist auf Antrag **ab Eingang des Festsetzungsantrags** mit fünf Prozentpunkten über dem Basiszinssatz zu verzinsen (§ 104 Abs. 1 S. 2 ZPO). Der Zinsantrag ist ausdrücklich zu stellen — er wird nicht von Amts wegen tituliert. Der Beschluss ist Vollstreckungstitel nach § 794 Abs. 1 Nr. 2 ZPO.

Eine **vereinfachte Festsetzung** auf dem Urteil sieht [§ 105 ZPO](https://www.gesetze-im-internet.de/zpo/__105.html) vor, wenn der Antrag vor Ablauf der Einlegungsfrist gestellt wird.

### 5. Kostenausgleichung bei Quotelung ([§ 106 ZPO](https://www.gesetze-im-internet.de/zpo/__106.html))

Sind die Kosten ganz oder teilweise **verhältnismäßig geteilt**, hat jede Partei ihre Kosten binnen der gesetzten Frist anzumelden; das Gericht **verrechnet** die beiderseitigen Aufstellungen und setzt nur den Saldo fest. Die Ausgleichung erfolgt über die Gesamtkosten beider Seiten, nicht über die Differenz der Anwaltsrechnungen. Wer die Frist versäumt, wird mit seinen Positionen präkludiert.

### 6. Rechtsbehelfe ([§ 104 Abs. 3 ZPO](https://www.gesetze-im-internet.de/zpo/__104.html))

- Gegen die Entscheidung des Rechtspflegers ist die **sofortige Beschwerde** statthaft (§ 104 Abs. 3 S. 1 ZPO i.V.m. §§ 567 ff. ZPO). Notfrist: **zwei Wochen** ab Zustellung ([§ 569 Abs. 1 ZPO](https://www.gesetze-im-internet.de/zpo/__569.html)).
- Der Wert des Beschwerdegegenstands muss **200 EUR übersteigen** ([§ 567 Abs. 2 ZPO](https://www.gesetze-im-internet.de/zpo/__567.html)).
- Wird der Beschwerdewert nicht erreicht, bleibt die **Erinnerung** nach § 11 Abs. 2 RPflG.
- [§ 107 ZPO](https://www.gesetze-im-internet.de/zpo/__107.html) erlaubt die **Änderung** des Festsetzungsbeschlusses, wenn der Streitwert nachträglich anderweitig festgesetzt wird — der praktisch wichtigste Weg, eine auf falschem Wert beruhende Festsetzung zu korrigieren.

### 7. Streitwertbeschwerde ([§ 68 GKG](https://www.gesetze-im-internet.de/gkg_2004/__68.html))

Gegen die Streitwertfestsetzung nach [§ 63 GKG](https://www.gesetze-im-internet.de/gkg_2004/__63.html) ist die Beschwerde statthaft, wenn der Wert des Beschwerdegegenstands **200 EUR übersteigt** oder das Gericht sie zugelassen hat. Sie ist binnen **sechs Monaten** nach Rechtskraft der Hauptsacheentscheidung oder anderweitiger Erledigung einzulegen. Der Rechtsanwalt kann sie nach [§ 32 Abs. 2 RVG](https://www.gesetze-im-internet.de/rvg/__32.html) **aus eigenem Recht** einlegen — ein eigenständiger Hebel, wenn der Mandant an einem niedrigen Wert interessiert ist.

## Deterministische Berechnung

Der Rechner rechnet die erstattungsfähigen Beträge nach; **welche Positionen notwendig im Sinne des § 91 Abs. 1 ZPO sind, entscheidet er nicht** — das bleibt die juristische Wertung, die den Kern des Festsetzungsstreits ausmacht. Ebenso ist der Gegenstandswert Eingabe.

```bash
# Erstattungsfähige Anwaltskosten der obsiegenden Partei, Streitwert 18.000 EUR
python -m scripts.legal_calc.cli rvg --wert 18000 --posten verfahren termin
```

```
RVG-Berechnung (Gegenstandswert 18,000.00 EUR, Tabelle Stand 2025-06-01)
  1,0-Gebühr: 817.00 EUR
  Verfahrensgebühr VV 3100 (1.3): 1,062.10 EUR
  Terminsgebühr VV 3104 (1.2): 980.40 EUR
  Zwischensumme Gebühren: 2,042.50 EUR
  Auslagenpauschale VV 7002: 20.00 EUR
  Netto: 2,062.50 EUR
  USt VV 7008 (19%): 391.88 EUR
  Gesamt (brutto): 2,454.38 EUR
```

```bash
# Hinzuzurechnender Gerichtskostenvorschuss (KV 1210, 3,0)
python -m scripts.legal_calc.cli gkg --wert 18000 --faktor 3.0
```

```
GKG-Berechnung (Streitwert 18,000.00 EUR, Tabelle Stand 2025-06-01)
  1,0-Gebühr: 374.50 EUR
  Verfahrensgebühr erste Instanz (KV 1210) (3): 1,123.50 EUR
  (Gerichtsgebühren sind nicht umsatzsteuerpflichtig.)
```

Die ausgegebene Zeile `Tabelle Stand 2025-06-01` nennt die **Version der hinterlegten Gebührentabelle**. Sie ist vor jeder Einreichung gegen die aktuelle Anlage 2 zu § 13 RVG und zu § 34 GKG zu prüfen; nach einer Kostenrechtsänderung liefert eine nicht aktualisierte Tabelle stillschweigend falsche Beträge. Bei Vorsteuerabzugsberechtigung ist die USt-Position aus der Aufstellung zu streichen.

## Quellen

### Statute

- [§ 91 ZPO](https://www.gesetze-im-internet.de/zpo/__91.html), [§ 91a ZPO](https://www.gesetze-im-internet.de/zpo/__91a.html), [§ 92 ZPO](https://www.gesetze-im-internet.de/zpo/__92.html), [§ 93 ZPO](https://www.gesetze-im-internet.de/zpo/__93.html), [§ 96 ZPO](https://www.gesetze-im-internet.de/zpo/__96.html), [§ 100 ZPO](https://www.gesetze-im-internet.de/zpo/__100.html), [§ 101 ZPO](https://www.gesetze-im-internet.de/zpo/__101.html)
- [§ 103 ZPO](https://www.gesetze-im-internet.de/zpo/__103.html), [§ 104 ZPO](https://www.gesetze-im-internet.de/zpo/__104.html), [§ 105 ZPO](https://www.gesetze-im-internet.de/zpo/__105.html), [§ 106 ZPO](https://www.gesetze-im-internet.de/zpo/__106.html), [§ 107 ZPO](https://www.gesetze-im-internet.de/zpo/__107.html), [§ 567 ZPO](https://www.gesetze-im-internet.de/zpo/__567.html), [§ 569 ZPO](https://www.gesetze-im-internet.de/zpo/__569.html)
- [§ 63 GKG](https://www.gesetze-im-internet.de/gkg_2004/__63.html), [§ 68 GKG](https://www.gesetze-im-internet.de/gkg_2004/__68.html), [§ 32 RVG](https://www.gesetze-im-internet.de/rvg/__32.html), [§ 33 RVG](https://www.gesetze-im-internet.de/rvg/__33.html)

### Kommentare

- Herget, in: Zöller, ZPO, 35. Aufl. 2024, § 91 Rn. 1 ff. (Notwendigkeit der Kosten)
- Schulz, in: MüKoZPO, 6. Aufl. 2020, § 104 Rn. 1 ff. (Festsetzungsverfahren, Verzinsung)
- Hartmann / Toussaint, Kostenrecht, 54. Aufl. 2024, § 68 GKG Rn. 1 ff.
- Schneider / Volpert / Fölsch, Gesamtes Kostenrecht, 3. Aufl. 2021, § 106 ZPO Rn. 1 ff. (Ausgleichung)

### Rechtsprechung

- Rechtsprechung zur Erstattungsfähigkeit der Reisekosten eines auswärtigen Prozessbevollmächtigten nach § 91 Abs. 2 ZPO `[unverifiziert – prüfen]`
- Rechtsprechung zur Erstattungsfähigkeit der Kosten eines Terminsvertreters bis zur Höhe ersparter Reisekosten `[unverifiziert – prüfen]`

> Fundstellen sind vor Verwendung in juris, Beck-Online oder AGS/RVGreport zu ermitteln.

## Ausgabeformat

```
KOSTENFESTSETZUNG — <Az.> — <Datum>
VERTRAULICH — MANDATSGEHEIMNIS — § 43a Abs. 2 BRAO

I.    Kostengrundentscheidung      <Tenor wörtlich>
      Rechtsgrundlage              [§ 91 / § 92 / § 91a / § 93 ZPO]
      Rechtskraft / Vollstreckbark.[✅ / offen]
II.   Streitwert                   <…> EUR  [§ 63 GKG, Beschluss vom <…>]
      Streitwertbeschwerde § 68 GKG[nicht veranlasst / geboten, Frist <…>]
III.  Erstattungsfähige Positionen
      Anwaltsgebühren              <…> EUR  [§ 91 Abs. 2 S. 1 ZPO]
      Reisekosten                  <…> EUR  [notwendig: ja/nein]
      Mehrere Anwälte              [🟢 / 🔴 § 91 Abs. 2 S. 2 ZPO]
      Gerichtskostenvorschuss      <…> EUR
      Umsatzsteuer                 [erstattungsfähig / Vorsteuerabzug]
IV.   Ausgleichung § 106 ZPO       [N/A / Quote <…>, Saldo <…> EUR]
V.    Zinsantrag § 104 Abs. 1 S. 2 [gestellt / 🔴 fehlt]
VI.   Rechtsbehelf                 [sofortige Beschwerde § 104 Abs. 3 ZPO /
                                    Erinnerung § 11 Abs. 2 RPflG]
      Frist                        <Datum>  Beschwerdewert: <…> EUR

Tabellenstand geprüft: [ja, am <Datum> / 🔴 offen]
Empfehlung: <…>
```

## Risiken / typische Fehler

- **Einwände gegen die Kostengrundentscheidung im Festsetzungsverfahren** vorgetragen. Der Rechtspfleger ist an den Tenor gebunden; wer die Quote angreifen will, muss das Rechtsmittel gegen die Hauptsacheentscheidung führen.
- **Zinsantrag nach § 104 Abs. 1 S. 2 ZPO nicht gestellt.** Die Verzinsung ab Antragseingang wird nicht von Amts wegen tituliert.
- **Erklärung zum Vorsteuerabzug fehlt** — die Umsatzsteuer wird dann nicht festgesetzt (§ 104 Abs. 2 S. 3 ZPO).
- **Reisekosten ungeprüft angesetzt.** Bei auswärtigem Prozessbevollmächtigtem ist die Notwendigkeit der Zuziehung gesondert darzulegen.
- **Anmeldefrist bei der Ausgleichung nach § 106 ZPO versäumt** — die eigenen Positionen fallen dann aus der Verrechnung heraus.
- **Beschwerdewert von 200 EUR nicht erreicht** und dennoch sofortige Beschwerde eingelegt statt Erinnerung nach § 11 Abs. 2 RPflG.
- **Streitwertbeschwerde § 68 GKG verfristet** — die Sechs-Monats-Frist ab Rechtskraft der Hauptsache wird regelmäßig übersehen; § 32 Abs. 2 RVG gibt dem Anwalt ein eigenes Beschwerderecht.
- **Falscher Streitwert bestandskräftig geworden**, ohne § 107 ZPO zu nutzen — die Änderung des Festsetzungsbeschlusses nach nachträglicher Wertfestsetzung ist der einzige verbleibende Weg.
- **Kosten mehrerer Anwälte voll angesetzt** entgegen § 91 Abs. 2 S. 2 ZPO.
