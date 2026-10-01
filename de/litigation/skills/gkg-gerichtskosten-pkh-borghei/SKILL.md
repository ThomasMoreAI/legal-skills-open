---
name: gkg-gerichtskosten-pkh-borghei
title: /kostenrecht-rvg:gkg-gerichtskosten-pkh
description: Gerichtskosten und Prozesskostenhilfe – Wertgebühr § 34 GKG mit Anlage 2, Verfahrenssätze des Kostenverzeichnisses (KV 1210 mit 3,0 in erster Instanz, Ermäßigung auf 1,0 nach KV 1211 bei Klagerücknahme, Anerkenntnis oder Vergleich, KV 1220 Berufung), Vorschusspflicht § 12 GKG, Streitwertfestsetzung §§ 63, 68 GKG sowie Prozess- und Verfahrenskostenhilfe §§ 114 ff. ZPO mit Erfolgsaussicht und Mutwilligkeit § 114 ZPO, einzusetzendem Einkommen und Vermögen § 115 ZPO, Ratenzahlung, Überprüfungsverfahren § 120a ZPO und Aufhebung § 124 ZPO. Use when die Kostenlast eines Verfahrens vorab zu beziffern oder ein PKH- beziehungsweise VKH-Antrag vorzubereiten und gegen Aufhebungsrisiken zu sichern ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/kostenrecht-rvg/skills/gkg-gerichtskosten-pkh
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: litigation
language: de
---

# /kostenrecht-rvg:gkg-gerichtskosten-pkh

## Zweck

Vor jeder Klage stehen zwei Fragen, die den Mandanten mehr interessieren als die Rechtslage: Was kostet das Verfahren, und wer trägt das Risiko? Dieser Skill beziffert die Gerichtskosten nach GKG deterministisch, zeigt die Ermäßigungswege bei früher Verfahrensbeendigung und bereitet den PKH- oder VKH-Antrag so vor, dass er weder an der Erfolgsaussicht noch an einer unvollständigen Erklärung scheitert — und dass die Bewilligung die Überprüfung nach § 120a ZPO übersteht.

## Eingaben

- Streitwert und dessen Herleitung (§§ 39 ff. GKG i.V.m. §§ 3 ff. ZPO)
- Instanz und Verfahrensart; Familiensache? (dann FamGKG statt GKG, VKH statt PKH)
- Realistische Prognose zur Verfahrensbeendigung (streitiges Urteil, Vergleich, Rücknahme, Anerkenntnis)
- Für PKH: Einkommen aller Art, Unterhaltspflichten, Wohnkosten, besondere Belastungen, Vermögen einschließlich Schonvermögen
- Erfolgsaussicht: die tragenden Tatsachen und Beweismittel, nicht nur das Ergebnis
- Bereits gestellte PKH-Anträge, laufende Ratenzahlungen, frühere Aufhebungen
- Rechtsschutzversicherung vorhanden? (schließt Bedürftigkeit regelmäßig aus)

## Sub-Agent-Architektur

Der **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) ordnet Verfahren und Gebührentatbestand der richtigen KV-Nummer zu und belegt die PKH-Voraussetzungen aus §§ 114 ff. ZPO. Der **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) erstellt die Kostenprognose und den PKH-Antrag nebst Erklärung. Der **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft Vollständigkeit der Erklärung, Belehrung über § 120a ZPO und die Aufhebungsrisiken nach § 124 ZPO.

## Ablauf

### 1. Wertgebühr nach GKG ([§ 34 GKG](https://www.gesetze-im-internet.de/gkg_2004/__34.html))

Die 1,0-Gebühr ergibt sich aus [Anlage 2 zu § 34 GKG](https://www.gesetze-im-internet.de/gkg_2004/anlage_2.html). Wie im RVG wird auf die **angefangene Wertstufe aufgerundet**; oberhalb der höchsten Stufe gilt ein fester Zuschlag je angefangene 50.000 EUR (§ 34 Abs. 1 S. 3 GKG). Der Streitwert selbst folgt [§ 48 GKG](https://www.gesetze-im-internet.de/gkg_2004/__48.html) i.V.m. §§ 3 ff. ZPO; mehrere Ansprüche werden nach [§ 39 GKG](https://www.gesetze-im-internet.de/gkg_2004/__39.html) zusammengerechnet, höchstens bis 30 Mio. EUR.

### 2. Verfahrenssatz aus dem Kostenverzeichnis ([KV GKG](https://www.gesetze-im-internet.de/gkg_2004/anlage_1.html))

| KV-Nr. | Verfahren | Satz |
|---|---|---|
| 1210 | Bürgerliche Rechtsstreitigkeit erster Instanz | 3,0 |
| 1211 | Ermäßigung bei früher Verfahrensbeendigung | 1,0 |
| 1220 | Berufung | 4,0 |
| 1222 | Ermäßigung im Berufungsverfahren | 1,0 |
| 1230 | Revision | 5,0 |

Die **Ermäßigung nach KV 1211** greift, wenn das Verfahren ohne streitiges Urteil endet — insbesondere bei **Klagerücknahme** vor Schluss der mündlichen Verhandlung, bei **Anerkenntnis-, Verzichts- oder Versäumnisurteil** und bei **gerichtlichem Vergleich** über den gesamten Streitgegenstand. Wirtschaftlich bedeutet das eine Reduktion der Gerichtsgebühr auf ein Drittel; sie ist deshalb bei jeder Vergleichsverhandlung als eigener Verhandlungswert einzustellen. Ein Vergleich, der nur einen Teil des Streitgegenstands erfasst, ermäßigt nicht.

### 3. Vorschuss und Fälligkeit ([§ 12 GKG](https://www.gesetze-im-internet.de/gkg_2004/__12.html))

In bürgerlichen Rechtsstreitigkeiten soll die Klage **erst nach Zahlung der Verfahrensgebühr zugestellt** werden. Praktische Folge: Die volle 3,0-Gebühr ist vorzuschießen, auch wenn am Ende nach KV 1211 nur 1,0 anfällt; der Überschuss wird erstattet. Kostenschuldner ist nach [§ 22 GKG](https://www.gesetze-im-internet.de/gkg_2004/__22.html) zunächst der Antragsteller, daneben nach [§ 29 GKG](https://www.gesetze-im-internet.de/gkg_2004/__29.html) der Übernahmeschuldner aufgrund der Kostengrundentscheidung. Wird PKH bewilligt, entfällt die Vorschusspflicht ([§ 122 Abs. 1 Nr. 1 ZPO](https://www.gesetze-im-internet.de/zpo/__122.html)).

### 4. Streitwertfestsetzung ([§ 63 GKG](https://www.gesetze-im-internet.de/gkg_2004/__63.html), [§ 68 GKG](https://www.gesetze-im-internet.de/gkg_2004/__68.html))

Das Gericht setzt den Wert zunächst **vorläufig** für die Zuständigkeit und die Gebührenerhebung fest, endgültig nach Erledigung. Gegen die endgültige Festsetzung ist die Beschwerde statthaft, wenn der Wert des Beschwerdegegenstands **200 EUR übersteigt**; Frist: sechs Monate nach Rechtskraft oder anderweitiger Erledigung. Der Rechtsanwalt kann sie nach § 32 Abs. 2 RVG aus eigenem Recht einlegen.

### 5. PKH-Voraussetzungen ([§ 114 ZPO](https://www.gesetze-im-internet.de/zpo/__114.html))

Drei Voraussetzungen, kumulativ:

1. **Bedürftigkeit** — die Partei kann die Kosten nach ihren persönlichen und wirtschaftlichen Verhältnissen nicht, nur zum Teil oder nur in Raten aufbringen.
2. **Hinreichende Aussicht auf Erfolg** — der Standpunkt muss vertretbar erscheinen und die Beweisführung möglich sein. Es findet **keine Vorwegnahme der Beweiswürdigung** statt; schwierige, ungeklärte Rechtsfragen dürfen nicht im PKH-Verfahren entschieden werden.
3. **Keine Mutwilligkeit** — mutwillig ist die Rechtsverfolgung nach § 114 Abs. 2 ZPO, wenn eine Partei, die keine PKH beansprucht, bei verständiger Würdigung **von ihr absehen würde** oder ihr Recht auf einfacherem Weg verfolgen könnte.

In Familiensachen tritt an die Stelle der PKH die **Verfahrenskostenhilfe (VKH)** nach [§ 76 FamFG](https://www.gesetze-im-internet.de/famfg/__76.html), der auf die §§ 114 ff. ZPO verweist.

### 6. Einzusetzendes Einkommen und Vermögen ([§ 115 ZPO](https://www.gesetze-im-internet.de/zpo/__115.html))

Vom Einkommen sind abzusetzen: die Beträge nach § 82 Abs. 2 SGB XII, ein Erwerbstätigenfreibetrag, Freibeträge für die Partei selbst und für unterhaltsberechtigte Personen, Kosten für Unterkunft und Heizung sowie weitere Beträge bei besonderer Belastung.

Aus dem verbleibenden einzusetzenden Einkommen werden **Monatsraten** festgesetzt: grundsätzlich die Hälfte des einzusetzenden Einkommens; bei einem einzusetzenden Einkommen über 600 EUR beträgt die Rate 300 EUR zuzüglich des übersteigenden Betrags. Es werden **höchstens 48 Monatsraten** festgesetzt (§ 115 Abs. 2 ZPO). PKH wird **nicht bewilligt**, wenn die Kosten der Prozessführung vier Monatsraten und die aus dem Vermögen aufzubringenden Teilbeträge voraussichtlich nicht übersteigen (§ 115 Abs. 4 ZPO). Das **Vermögen** ist einzusetzen, soweit dies zumutbar ist; § 90 SGB XII (Schonvermögen, selbstgenutztes Hausgrundstück) gilt entsprechend.

### 7. Antrag, Bewilligung, Beiordnung ([§ 117 ZPO](https://www.gesetze-im-internet.de/zpo/__117.html), [§ 121 ZPO](https://www.gesetze-im-internet.de/zpo/__121.html))

Der Antrag ist bei dem Prozessgericht zu stellen; beizufügen ist die **Erklärung über die persönlichen und wirtschaftlichen Verhältnisse** auf dem amtlichen Vordruck nebst Belegen. Die Bewilligung erfolgt für **jeden Rechtszug gesondert** ([§ 119 ZPO](https://www.gesetze-im-internet.de/zpo/__119.html)). Im Anwaltsprozess wird ein Rechtsanwalt beigeordnet; der beigeordnete Anwalt rechnet nach [§ 49 RVG](https://www.gesetze-im-internet.de/rvg/__49.html) gegen die Staatskasse ab und kann von der Partei keine weitere Vergütung fordern ([§ 122 Abs. 1 Nr. 3 ZPO](https://www.gesetze-im-internet.de/zpo/__122.html)).

```
An das Amtsgericht <Ort>

Antrag auf Bewilligung von Prozesskostenhilfe
gemäß §§ 114 ff. ZPO unter Beiordnung eines Rechtsanwalts

In Sachen <Antragstellerin> ./. <Antragsgegner>

I.   Es wird beantragt, der Antragstellerin für die beabsichtigte
     Klage Prozesskostenhilfe zu bewilligen und ihr die
     Unterzeichnende gemäß § 121 Abs. 1 ZPO beizuordnen.

II.  Beabsichtigte Rechtsverfolgung
     Streitgegenstand: <…>, Streitwert: <…> EUR
     Klageentwurf ist als Anlage 1 beigefügt.

III. Hinreichende Erfolgsaussicht (§ 114 Abs. 1 S. 1 ZPO)
     <Tatsachenvortrag mit Beweisantritt; die Beweiswürdigung wird
      nicht vorweggenommen, es genügt die Vertretbarkeit des
      Standpunkts.>

IV.  Keine Mutwilligkeit (§ 114 Abs. 2 ZPO)
     <Darlegung, dass eine selbstzahlende Partei ebenso vorgehen
      würde; einfacherer Weg nicht ersichtlich.>

V.   Persönliche und wirtschaftliche Verhältnisse
     Erklärung auf amtlichem Vordruck nebst Belegen als Anlage 2.
     Einkommen: <…>  Abzüge nach § 115 Abs. 1 ZPO: <…>
     Einzusetzendes Einkommen: <…>  Rate: <…> EUR
     Vermögen: <…>  Schonvermögen § 90 SGB XII: <…>

VI.  Die Antragstellerin ist über ihre Pflicht nach § 120a Abs. 2
     ZPO belehrt worden, wesentliche Verbesserungen ihrer
     wirtschaftlichen Verhältnisse und jeden Anschriftenwechsel
     unaufgefordert und unverzüglich mitzuteilen.

<Ort, Datum, Unterschrift>
```

### 8. Überprüfung und Aufhebung ([§ 120a ZPO](https://www.gesetze-im-internet.de/zpo/__120a.html), [§ 124 ZPO](https://www.gesetze-im-internet.de/zpo/__124.html))

Das Gericht kann die Bewilligung **bis zum Ablauf von vier Jahren** nach rechtskräftigem Abschluss oder sonstiger Beendigung des Verfahrens überprüfen und die Zahlungsbestimmung ändern. Die Partei muss eine **wesentliche Verbesserung** ihrer Verhältnisse sowie jede Anschriftenänderung **unaufgefordert** mitteilen (§ 120a Abs. 2 ZPO).

Die Bewilligung ist nach § 124 ZPO aufzuheben, wenn die Partei über die Voraussetzungen unrichtige Angaben gemacht, die Erklärungspflicht nach § 120a Abs. 2 ZPO verletzt, absichtlich oder aus grober Nachlässigkeit unrichtige Angaben gemacht oder mit der Zahlung von **mehr als drei Monatsraten** in Rückstand geraten ist. Folge ist die rückwirkende Kostenhaftung — der praktisch häufigste Grund, aus dem ein PKH-Mandat für den Mandanten teuer endet.

## Deterministische Berechnung

Der Rechner erledigt den Tabellenlookup nach Anlage 2 zu § 34 GKG und die Multiplikation mit dem Verfahrenssatz. **Der Streitwert ist juristische Wertung und Eingabe**; ebenso die Prognose, ob KV 1211 greifen wird. Die Bedürftigkeitsrechnung nach § 115 ZPO bildet der Rechner nicht ab — sie ist auf dem amtlichen Vordruck zu entwickeln.

```bash
# Bürgerliche Rechtsstreitigkeit erster Instanz, Streitwert 10.000 EUR
python -m scripts.legal_calc.cli gkg --wert 10000 --faktor 3.0
```

```
GKG-Berechnung (Streitwert 10,000.00 EUR, Tabelle Stand 2025-06-01)
  1,0-Gebühr: 283.00 EUR
  Verfahrensgebühr erste Instanz (KV 1210) (3): 849.00 EUR
  (Gerichtsgebühren sind nicht umsatzsteuerpflichtig.)
```

```bash
# Gegenprobe: Ermäßigung nach KV 1211 (Vergleich, Rücknahme, Anerkenntnis)
python -m scripts.legal_calc.cli gkg --wert 10000 --faktor 1.0
```

```
GKG-Berechnung (Streitwert 10,000.00 EUR, Tabelle Stand 2025-06-01)
  1,0-Gebühr: 283.00 EUR
  Verfahrensgebühr erste Instanz (KV 1210) (1): 283.00 EUR
  (Gerichtsgebühren sind nicht umsatzsteuerpflichtig.)
```

```bash
# Höherer Wert, gleiche Gegenüberstellung — Grundlage der Vergleichsempfehlung
python -m scripts.legal_calc.cli gkg --wert 25000 --faktor 3.0
```

```
GKG-Berechnung (Streitwert 25,000.00 EUR, Tabelle Stand 2025-06-01)
  1,0-Gebühr: 435.50 EUR
  Verfahrensgebühr erste Instanz (KV 1210) (3): 1,306.50 EUR
  (Gerichtsgebühren sind nicht umsatzsteuerpflichtig.)
```

Für die Gesamtkostenprognose ist die Anwaltsvergütung beider Seiten hinzuzurechnen:

```bash
python -m scripts.legal_calc.cli rvg --wert 25000 --posten verfahren termin einigung-anhaengig
```

```
RVG-Berechnung (Gegenstandswert 25,000.00 EUR, Tabelle Stand 2025-06-01)
  1,0-Gebühr: 927.00 EUR
  Verfahrensgebühr VV 3100 (1.3): 1,205.10 EUR
  Terminsgebühr VV 3104 (1.2): 1,112.40 EUR
  Einigungsgebühr VV 1003 (1): 927.00 EUR
  Zwischensumme Gebühren: 3,244.50 EUR
  Auslagenpauschale VV 7002: 20.00 EUR
  Netto: 3,264.50 EUR
  USt VV 7008 (19%): 620.25 EUR
  Gesamt (brutto): 3,884.75 EUR
```

Der Faktor ist nach KV GKG **explizit** zu setzen; der Rechner leitet die Ermäßigung nicht selbst her. Die Zeile `Tabelle Stand 2025-06-01` nennt die Version der hinterlegten Gebührentabelle. Sie ist vor jeder mandantengerichteten Kostenprognose gegen die aktuelle Anlage 2 zu § 34 GKG zu prüfen; nach einer Kostenrechtsänderung rechnet eine nicht aktualisierte Tabelle stillschweigend falsch.

## Quellen

### Statute

- [§ 12 GKG](https://www.gesetze-im-internet.de/gkg_2004/__12.html), [§ 22 GKG](https://www.gesetze-im-internet.de/gkg_2004/__22.html), [§ 29 GKG](https://www.gesetze-im-internet.de/gkg_2004/__29.html), [§ 34 GKG](https://www.gesetze-im-internet.de/gkg_2004/__34.html), [§ 39 GKG](https://www.gesetze-im-internet.de/gkg_2004/__39.html), [§ 48 GKG](https://www.gesetze-im-internet.de/gkg_2004/__48.html), [§ 63 GKG](https://www.gesetze-im-internet.de/gkg_2004/__63.html), [§ 68 GKG](https://www.gesetze-im-internet.de/gkg_2004/__68.html), [Anlage 1 (KV GKG)](https://www.gesetze-im-internet.de/gkg_2004/anlage_1.html), [Anlage 2](https://www.gesetze-im-internet.de/gkg_2004/anlage_2.html)
- [§ 114 ZPO](https://www.gesetze-im-internet.de/zpo/__114.html), [§ 115 ZPO](https://www.gesetze-im-internet.de/zpo/__115.html), [§ 116 ZPO](https://www.gesetze-im-internet.de/zpo/__116.html), [§ 117 ZPO](https://www.gesetze-im-internet.de/zpo/__117.html), [§ 119 ZPO](https://www.gesetze-im-internet.de/zpo/__119.html), [§ 120a ZPO](https://www.gesetze-im-internet.de/zpo/__120a.html), [§ 121 ZPO](https://www.gesetze-im-internet.de/zpo/__121.html), [§ 122 ZPO](https://www.gesetze-im-internet.de/zpo/__122.html), [§ 124 ZPO](https://www.gesetze-im-internet.de/zpo/__124.html)
- [§ 76 FamFG](https://www.gesetze-im-internet.de/famfg/__76.html), [§ 49 RVG](https://www.gesetze-im-internet.de/rvg/__49.html), [§ 90 SGB XII](https://www.gesetze-im-internet.de/sgb_12/__90.html)

### Kommentare

- Hartmann / Toussaint, Kostenrecht, 54. Aufl. 2024, § 34 GKG Rn. 1 ff. und KV 1211 Rn. 1 ff.
- Geimer, in: Zöller, ZPO, 35. Aufl. 2024, § 114 Rn. 19 ff. (Erfolgsaussicht, Mutwilligkeit)
- Wache, in: MüKoZPO, 6. Aufl. 2020, § 115 Rn. 1 ff. (einzusetzendes Einkommen)
- Schneider / Volpert / Fölsch, Gesamtes Kostenrecht, 3. Aufl. 2021, § 120a ZPO Rn. 1 ff.

### Rechtsprechung

- Rechtsprechung zum Verbot der Vorwegnahme der Beweiswürdigung im PKH-Bewilligungsverfahren `[unverifiziert – prüfen]`
- Rechtsprechung zur Reichweite der Ermäßigung nach KV 1211 bei nur teilweiser Verfahrensbeendigung `[unverifiziert – prüfen]`

> Fundstellen sind vor Verwendung in juris, Beck-Online oder AGS/RVGreport zu ermitteln.

## Ausgabeformat

```
GERICHTSKOSTEN / PKH — <Mandat-ID> — <Datum>
VERTRAULICH — MANDATSGEHEIMNIS — § 43a Abs. 2 BRAO

I.    Streitwert                    <…> EUR  [§ 48 GKG, §§ 3 ff. ZPO]
II.   Gerichtskosten
      1,0-Gebühr (Anlage 2 GKG)     <…> EUR  [Tabelle Stand <…>]
      Verfahrenssatz                [KV 1210 3,0 / KV 1220 4,0]
      Gerichtsgebühr                <…> EUR
      Ermäßigung KV 1211            [möglich bei <Vergleich / Rücknahme /
                                     Anerkenntnis> → <…> EUR]
      Vorschuss § 12 GKG            <…> EUR  [fällig vor Zustellung]
III.  Gesamtkostenrisiko            eigene RA <…> / gegn. RA <…> /
                                    Gericht <…> = <…> EUR
IV.   PKH / VKH
      Erfolgsaussicht § 114 ZPO     [🟢 hinreichend / 🔴 zweifelhaft]
      Mutwilligkeit § 114 Abs. 2    [🟢 nein / 🔴 ja]
      Einzusetzendes Einkommen      <…> EUR  [§ 115 Abs. 1 ZPO]
      Rate / Ratenzahl              <…> EUR x <…>  [max. 48 Monatsraten]
      Vermögen § 115 Abs. 3 ZPO     <…>  [Schonvermögen § 90 SGB XII]
      Bewilligungssperre Abs. 4     [ja: Kosten < 4 Monatsraten / nein]
      Beiordnung § 121 ZPO          [beantragt]
V.    Belehrung § 120a Abs. 2 ZPO   [erteilt am <Datum>]
      Aufhebungsrisiken § 124 ZPO   <…>

Tabellenstand geprüft: [ja, am <Datum> / 🔴 offen]
Empfehlung: <…>
```

## Risiken / typische Fehler

- **Ermäßigung nach KV 1211 in der Vergleichsverhandlung nicht beziffert.** Der Kostenvorteil einer frühen Beendigung ist ein eigenständiges Verhandlungsargument und gehört in die Prognose.
- **Teilvergleich als vollständige Erledigung behandelt** — die Ermäßigung setzt die Beendigung des gesamten Verfahrens voraus.
- **Vorschuss § 12 GKG nicht eingeplant.** Die Klage wird bis zur Zahlung nicht zugestellt; bei drohender Verjährung ist das ein Fristrisiko.
- **PKH-Antrag ohne Klageentwurf und ohne Beweisantritt** — die Erfolgsaussicht nach § 114 Abs. 1 S. 1 ZPO ist dann nicht prüfbar.
- **Vorwegnahme der Beweiswürdigung** durch das Gericht hingenommen, statt sie zu rügen.
- **Erklärung über die persönlichen und wirtschaftlichen Verhältnisse unvollständig oder ohne Belege** — führt zur Zurückweisung und später zur Aufhebung nach § 124 ZPO.
- **Belehrung nach § 120a Abs. 2 ZPO unterlassen.** Die Mitteilungspflicht bei wesentlicher Verbesserung und bei Anschriftenwechsel besteht vier Jahre über das Verfahrensende hinaus; ihre Verletzung führt zur Aufhebung.
- **Rückstand mit mehr als drei Monatsraten** übersehen — § 124 Abs. 1 Nr. 5 ZPO, rückwirkende Kostenhaftung.
- **Rechtsschutzversicherung nicht abgefragt** — sie schließt die Bedürftigkeit regelmäßig aus und macht den PKH-Antrag mutwillig.
- **Veraltete Gebührentabelle** verwendet, ohne den ausgegebenen `Stand` gegen die aktuelle Anlage 2 zu prüfen.
