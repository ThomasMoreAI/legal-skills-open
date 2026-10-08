---
name: rvg-gebuehrenberechnung-borghei
title: /kostenrecht-rvg:rvg-gebuehrenberechnung
description: Berechnung der gesetzlichen Anwaltsvergütung nach dem RVG – Gegenstandswert §§ 22, 23 RVG i.V.m. §§ 3 ff. ZPO, Wertgebühr § 13 RVG und Anlage 2, Geschäftsgebühr VV 2300 im Rahmen 0,5 bis 2,5 mit Schwellengebühr 1,3 und den Bemessungskriterien des § 14 RVG, Verfahrensgebühr VV 3100, Terminsgebühr VV 3104, Einigungsgebühr VV 1000/1003, Anrechnung nach Vorbem. 3 Abs. 4 VV, Auslagen VV 7000 bis 7002 und Umsatzsteuer VV 7008, mit deterministischer Berechnung über scripts/legal_calc. Use when eine Kostennote, ein Kostenvoranschlag oder eine Gegenkontrolle einer fremden Gebührenrechnung zu erstellen ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/kostenrecht-rvg/skills/rvg-gebuehrenberechnung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: litigation
language: de
---

# /kostenrecht-rvg:rvg-gebuehrenberechnung

## Zweck

Die Gebührenrechnung ist der Teil des Mandats, in dem ein Rechenfehler unmittelbar Geld kostet und ein Wertfehler den gesamten Ansatz verschiebt. Dieser Skill trennt die beiden Ebenen sauber: Der **Gegenstandswert** und die **Rahmengebührenbestimmung nach § 14 RVG** sind juristische Wertungen und bleiben Eingabe; die Tabellenlookups und die Arithmetik übernimmt der deterministische Rechner. Ergebnis ist eine prüffähige Kostennote nach § 10 RVG oder die Gegenkontrolle einer fremden Rechnung.

## Eingaben

- Angelegenheit: außergerichtlich, gerichtlich (Instanz), oder beides nacheinander
- Gegenstand und bezifferter Wert; bei unbezifferten Ansprüchen die Schätzgrundlagen
- Mehrere Gegenstände in derselben Angelegenheit? (§ 22 Abs. 1 RVG — Zusammenrechnung)
- Umfang und Schwierigkeit der Tätigkeit, Bedeutung der Sache, Einkommens- und Vermögensverhältnisse, besonderes Haftungsrisiko (§ 14 Abs. 1 RVG)
- Ist eine außergerichtliche Geschäftsgebühr angefallen, die anzurechnen ist? (Vorbem. 3 Abs. 4 VV)
- Vergleich geschlossen? Gegenstand bereits anhängig? (VV 1000 vs. VV 1003)
- Auslagen: Kopien, Reisen, Post; Vorsteuerabzugsberechtigung des Mandanten
- Besteht eine Vergütungsvereinbarung? Dann greift dieser Skill nur als Vergleichsmaßstab

## Sub-Agent-Architektur

Der **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) ordnet den Gegenstand der einschlägigen Wertvorschrift zu (§ 23 RVG mit Verweis auf GKG/FamGKG, hilfsweise § 23 Abs. 3 RVG) und belegt die Gebührentatbestände aus dem VV RVG. Der **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) bestimmt die Rahmengebühr nach § 14 RVG mit Begründung, ruft den Rechner auf und formuliert die Kostennote. Der **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft Wertansatz, Anrechnung, Abgeltungsbereich (§ 15 RVG) und die Formanforderungen des § 10 RVG.

## Ablauf

### 1. Gegenstandswert bestimmen ([§ 22 RVG](https://www.gesetze-im-internet.de/rvg/__22.html), [§ 23 RVG](https://www.gesetze-im-internet.de/rvg/__23.html))

§ 23 Abs. 1 RVG verweist für gerichtliche Verfahren auf die **Wertvorschriften des Gerichtskostenrechts** — also §§ 39 ff. GKG, die ihrerseits über [§ 48 Abs. 1 GKG](https://www.gesetze-im-internet.de/gkg_2004/__48.html) auf §§ 3 bis 9 ZPO zurückverweisen. Die Kette lautet damit: RVG → GKG → ZPO.

| Konstellation | Norm | Wert |
|---|---|---|
| Bezifferte Zahlungsklage | [§ 3 ZPO](https://www.gesetze-im-internet.de/zpo/__3.html) | Nennbetrag der Hauptforderung |
| Zinsen, Kosten, Früchte als Nebenforderung | [§ 4 Abs. 1 ZPO](https://www.gesetze-im-internet.de/zpo/__4.html) | bleiben außer Ansatz |
| Wiederkehrende Leistungen | [§ 9 ZPO](https://www.gesetze-im-internet.de/zpo/__9.html) | 3,5-facher Jahreswert |
| Miet- und Pachtverhältnisse | [§ 41 GKG](https://www.gesetze-im-internet.de/gkg_2004/__41.html) | idR Jahresentgelt, gedeckelt |
| Nichtvermögensrechtliche Gegenstände | § 23 Abs. 3 S. 2 RVG | nach billigem Ermessen, Auffangwert 5.000 EUR |

§ 22 Abs. 1 RVG: In **derselben Angelegenheit** werden die Werte mehrerer Gegenstände **zusammengerechnet**. Ob eine oder mehrere Angelegenheiten vorliegen, richtet sich nach §§ 15, 16 bis 18 RVG und ist die wertmäßig folgenreichste Vorfrage der ganzen Rechnung.

### 2. Wertgebühr aus Anlage 2 ableiten ([§ 13 RVG](https://www.gesetze-im-internet.de/rvg/__13.html))

Die 1,0-Gebühr wird aus [Anlage 2 zu § 13 RVG](https://www.gesetze-im-internet.de/rvg/anlage_2.html) abgelesen. Zwei Regeln, die in Handrechnungen regelmäßig falsch angewandt werden:

1. **Aufrundung auf die angefangene Wertstufe.** Ein Gegenstandswert von 10.001 EUR fällt bereits in die nächste Stufe.
2. **Oberhalb der höchsten tabellierten Stufe** gilt ein fester Zuschlag je angefangene 50.000 EUR (§ 13 Abs. 1 S. 3 RVG). Die Mindestgebühr beträgt 15 EUR (§ 13 Abs. 2 RVG).

### 3. Gebührentatbestände zuordnen ([VV RVG](https://www.gesetze-im-internet.de/rvg/anlage_1.html))

| VV-Nr. | Gebühr | Satz |
|---|---|---|
| 2300 | Geschäftsgebühr (außergerichtlich) | Rahmen **0,5 bis 2,5**, Schwellengebühr 1,3 |
| 3100 | Verfahrensgebühr erste Instanz | 1,3 |
| 3101 | Verfahrensgebühr bei vorzeitiger Beendigung | 0,8 |
| 3104 | Terminsgebühr | 1,2 |
| 1000 | Einigungsgebühr, Gegenstand nicht anhängig | 1,5 |
| 1003 | Einigungsgebühr, Gegenstand anhängig | 1,0 |

### 4. Rahmengebühr VV 2300 nach § 14 RVG bestimmen ([§ 14 RVG](https://www.gesetze-im-internet.de/rvg/__14.html))

Die Geschäftsgebühr VV 2300 ist eine **Rahmengebühr**. Der Anwalt bestimmt sie nach billigem Ermessen unter Berücksichtigung aller Umstände, **vor allem** des Umfangs und der Schwierigkeit der anwaltlichen Tätigkeit, der Bedeutung der Angelegenheit, der Einkommens- und Vermögensverhältnisse des Auftraggebers sowie eines besonderen Haftungsrisikos (§ 14 Abs. 1 S. 1, 3 RVG).

Die **Schwellengebühr** nach Anm. zu VV 2300 begrenzt das Ermessen: Eine Gebühr von **mehr als 1,3** kann nur gefordert werden, wenn die Tätigkeit **umfangreich oder schwierig** war. Das ist keine Regelvermutung für 1,3, sondern eine Sperre nach oben — bei einfach gelagerten Sachen ist ein Satz unter 1,3 zu bestimmen.

Ist die Bestimmung unbillig, ist sie für den Dritten nicht verbindlich (§ 14 Abs. 1 S. 4 RVG). Die Rechtsprechung räumt dem Anwalt einen **Toleranzrahmen** ein; erst dessen Überschreitung macht die Bestimmung unbillig `[unverifiziert – prüfen]`. Die Begründung des gewählten Satzes gehört in die Handakte, nicht erst in den Gebührenprozess.

### 5. Anrechnung der Geschäftsgebühr (Vorbem. 3 Abs. 4 VV RVG)

Geht dem Rechtsstreit eine außergerichtliche Tätigkeit voraus, wird die Geschäftsgebühr VV 2300 **zur Hälfte, höchstens mit 0,75**, auf die Verfahrensgebühr VV 3100 angerechnet. Angerechnet wird auf die Verfahrensgebühr, nicht umgekehrt — die außergerichtliche Gebühr bleibt in voller Höhe verdient.

Im Verhältnis zu **Dritten** (Gegner, Staatskasse, Rechtsschutzversicherer) gilt [§ 15a RVG](https://www.gesetze-im-internet.de/rvg/__15a.html): Der Dritte kann sich auf die Anrechnung nur berufen, soweit er beide Gebühren schuldet, wegen eines der Ansprüche ein Vollstreckungstitel besteht oder beide Gebühren im selben Verfahren geltend gemacht werden.

### 6. Auslagen und Umsatzsteuer ([VV Teil 7](https://www.gesetze-im-internet.de/rvg/anlage_1.html))

- **VV 7000** Dokumentenpauschale: gestaffelt je Seite (erste 50 Seiten höher, weitere Seiten niedriger); Beträge gegen die aktuelle Fassung des VV prüfen.
- **VV 7002** Post- und Telekommunikationspauschale: **20 % der Gebühren, höchstens 20 EUR** je Angelegenheit. Alternativ konkrete Abrechnung nach VV 7001.
- **VV 7003 bis 7006** Reisekosten: Kilometersatz bei eigenem Kraftfahrzeug, sonst tatsächliche Kosten, dazu Tage- und Abwesenheitsgeld sowie Übernachtungskosten.
- **VV 7008** Umsatzsteuer auf Gebühren und Auslagen, derzeit 19 %. Bei vorsteuerabzugsberechtigten Mandanten ist die USt wirtschaftlich neutral, im Kostenfestsetzungsverfahren aber nach § 104 Abs. 2 S. 3 ZPO gesondert zu erklären.

### 7. Kostennote erstellen ([§ 10 RVG](https://www.gesetze-im-internet.de/rvg/__10.html))

Der Anwalt kann die Vergütung nur aufgrund einer von ihm **unterzeichneten und dem Auftraggeber mitgeteilten Berechnung** einfordern. Die Berechnung muss die Beträge der einzelnen Gebühren und Auslagen, die Vorschüsse, eine kurze Bezeichnung des Gebührentatbestands, die Bezeichnung der Auslagen sowie die angewandten Nummern des Vergütungsverzeichnisses und bei Wertgebühren auch den Gegenstandswert enthalten.

```
KOSTENNOTE  —  Rechnung Nr. <…>  —  <Datum>
In Sachen <Mandant> ./. <Gegner>, Az. <…>

Gegenstandswert: <…> EUR (§ 23 Abs. 1 RVG i.V.m. § 48 GKG, § 3 ZPO)

I.   1,3 Verfahrensgebühr   VV 3100        <…> EUR
II.  1,2 Terminsgebühr      VV 3104        <…> EUR
III. 1,0 Einigungsgebühr    VV 1003        <…> EUR
IV.  abzüglich Anrechnung   Vorbem. 3
     Abs. 4 VV (0,65 aus <Wert>)          –<…> EUR
V.   Post-/Telekommunikations-
     pauschale              VV 7002         <…> EUR
VI.  Dokumentenpauschale    VV 7000         <…> EUR
                                          ---------
     Zwischensumme netto                    <…> EUR
VII. 19 % Umsatzsteuer      VV 7008         <…> EUR
                                          =========
     Gesamtbetrag                           <…> EUR
     abzüglich Vorschuss vom <Datum>       –<…> EUR
     Restforderung, fällig gemäß § 8 RVG    <…> EUR

Begründung des Gebührensatzes (§ 14 RVG): <Umfang, Schwierigkeit,
Bedeutung, Einkommens- und Vermögensverhältnisse, Haftungsrisiko>

<Ort, Datum>            <Unterschrift, Rechtsanwältin/Rechtsanwalt>
```

## Deterministische Berechnung

Der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) übernimmt **ausschließlich** den Tabellenlookup nach Anlage 2 zu § 13 RVG und die Arithmetik (Gebührensatz mal 1,0-Gebühr, Auslagenpauschale VV 7002, Umsatzsteuer VV 7008). **Der Gegenstandswert und die Bestimmung der Rahmengebühr nach § 14 RVG bleiben juristische Wertungen** und gehen als Eingabe in den Rechner ein — sie werden von ihm weder geprüft noch ersetzt.

```bash
# Gerichtliches Verfahren erster Instanz, Gegenstandswert 10.000 EUR
python -m scripts.legal_calc.cli rvg --wert 10000 --posten verfahren termin
```

```
RVG-Berechnung (Gegenstandswert 10,000.00 EUR, Tabelle Stand 2025-06-01)
  1,0-Gebühr: 652.00 EUR
  Verfahrensgebühr VV 3100 (1.3): 847.60 EUR
  Terminsgebühr VV 3104 (1.2): 782.40 EUR
  Zwischensumme Gebühren: 1,630.00 EUR
  Auslagenpauschale VV 7002: 20.00 EUR
  Netto: 1,650.00 EUR
  USt VV 7008 (19%): 313.50 EUR
  Gesamt (brutto): 1,963.50 EUR
```

```bash
# Außergerichtliche Geschäftsgebühr VV 2300 zum Schwellensatz 1,3
python -m scripts.legal_calc.cli rvg --wert 10000 --posten geschaeft
```

```
RVG-Berechnung (Gegenstandswert 10,000.00 EUR, Tabelle Stand 2025-06-01)
  1,0-Gebühr: 652.00 EUR
  Geschäftsgebühr VV 2300 (1.3): 847.60 EUR
  Zwischensumme Gebühren: 847.60 EUR
  Auslagenpauschale VV 7002: 20.00 EUR
  Netto: 867.60 EUR
  USt VV 7008 (19%): 164.84 EUR
  Gesamt (brutto): 1,032.44 EUR
```

```bash
# Verfahren mit Vergleich über einen bereits anhängigen Gegenstand
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

Der Rechner gibt mit `Tabelle Stand 2025-06-01` die **Version der hinterlegten Gebührentabelle** aus. Die Beträge der Anlage 2 ändern sich durch Gesetz (zuletzt KostBRÄG 2025). **Vor jeder mandantengerichteten Verwendung ist der Stand gegen die aktuelle Fassung der Anlage 2 zu prüfen**; eine veraltete Tabelle liefert stillschweigend falsche Beträge. Die Anrechnung nach Vorbem. 3 Abs. 4 VV bildet der Rechner nicht ab — sie ist als negative Position von Hand einzustellen.

## Quellen

### Statute

- [§ 2 RVG](https://www.gesetze-im-internet.de/rvg/__2.html), [§ 8 RVG](https://www.gesetze-im-internet.de/rvg/__8.html), [§ 10 RVG](https://www.gesetze-im-internet.de/rvg/__10.html), [§ 13 RVG](https://www.gesetze-im-internet.de/rvg/__13.html), [§ 14 RVG](https://www.gesetze-im-internet.de/rvg/__14.html), [§ 15 RVG](https://www.gesetze-im-internet.de/rvg/__15.html), [§ 15a RVG](https://www.gesetze-im-internet.de/rvg/__15a.html), [§ 22 RVG](https://www.gesetze-im-internet.de/rvg/__22.html), [§ 23 RVG](https://www.gesetze-im-internet.de/rvg/__23.html)
- [Anlage 1 (VV RVG)](https://www.gesetze-im-internet.de/rvg/anlage_1.html), [Anlage 2 (Gebührentabelle)](https://www.gesetze-im-internet.de/rvg/anlage_2.html)
- [§ 3 ZPO](https://www.gesetze-im-internet.de/zpo/__3.html), [§ 4 ZPO](https://www.gesetze-im-internet.de/zpo/__4.html), [§ 9 ZPO](https://www.gesetze-im-internet.de/zpo/__9.html), [§ 48 GKG](https://www.gesetze-im-internet.de/gkg_2004/__48.html), [§ 41 GKG](https://www.gesetze-im-internet.de/gkg_2004/__41.html)

### Kommentare

- Gerold / Schmidt, RVG, 26. Aufl. 2023, § 14 Rn. 1 ff. (Bemessung der Rahmengebühr)
- Mayer / Kroiß, RVG, 8. Aufl. 2021, VV 2300 Rn. 10 ff. (Schwellengebühr)
- Hartmann / Toussaint, Kostenrecht, 54. Aufl. 2024, § 13 RVG Rn. 1 ff.
- Schneider / Volpert / Fölsch, Gesamtes Kostenrecht, 3. Aufl. 2021, Vorbem. 3 Abs. 4 VV Rn. 1 ff. (Anrechnung)

### Rechtsprechung

- Rechtsprechung zum Toleranzrahmen bei der Bestimmung der Rahmengebühr nach § 14 RVG `[unverifiziert – prüfen]`
- Rechtsprechung zu den Anforderungen an „umfangreich oder schwierig" bei der Überschreitung der Schwellengebühr VV 2300 `[unverifiziert – prüfen]`

> Aktenzeichen und Fundstellen sind vor Verwendung in juris, Beck-Online oder AGS/RVGreport zu ermitteln. In diesem Skill wird bewusst keine Entscheidung benannt, die nicht extern verifiziert wurde.

## Ausgabeformat

```
RVG-BERECHNUNG — <Mandat-ID> — <Datum>
VERTRAULICH — MANDATSGEHEIMNIS — § 43a Abs. 2 BRAO

I.    Angelegenheit                 [außergerichtlich / gerichtlich / beides]
      Abgrenzung § 15 RVG           <eine / mehrere Angelegenheiten>
II.   Gegenstandswert               <…> EUR
      Rechtsgrundlage               § 23 RVG i.V.m. <§ 48 GKG, § 3 ZPO>
      Zusammenrechnung § 22 RVG     [ja: <Gegenstände> / nein]
III.  1,0-Gebühr (Anlage 2)         <…> EUR   [Tabelle Stand <…>]
IV.   Gebührenpositionen
      VV 2300 Geschäftsgebühr       <Satz> = <…> EUR  [§ 14 RVG-Begründung]
      VV 3100 Verfahrensgebühr      1,3   = <…> EUR
      VV 3104 Terminsgebühr         1,2   = <…> EUR
      VV 1000/1003 Einigungsgebühr  <Satz> = <…> EUR
V.    Anrechnung Vorbem. 3 Abs. 4  –<…> EUR   [§ 15a RVG gegenüber Dritten]
VI.   Auslagen                      VV 7000 <…> / VV 7002 <…> EUR
VII.  Umsatzsteuer VV 7008          <…> EUR   [Vorsteuerabzug: ja/nein]
VIII. Gesamt / Restforderung        <…> EUR   [Fälligkeit § 8 RVG]

Tabellenstand geprüft gegen Anlage 2: [ja, am <Datum> / 🔴 offen]
Offene Wertungsfragen: <Gegenstandswert, § 14 RVG-Satz>
```

## Risiken / typische Fehler

- **Gegenstandswert ungeprüft aus der Klageschrift übernommen.** Der Wert ist eigenständig nach § 23 RVG zu bestimmen; die vorläufige Streitwertangabe des Gerichts bindet den Anwalt nicht.
- **Angelegenheit falsch abgegrenzt.** Werden mehrere Gegenstände zu Unrecht als getrennte Angelegenheiten abgerechnet, ist die Rechnung überhöht; § 15 RVG und die Zusammenrechnung nach § 22 Abs. 1 RVG sind vorrangig zu prüfen.
- **Schwellengebühr 1,3 als Regelsatz behandelt.** VV 2300 ist eine Rahmengebühr von 0,5 bis 2,5; ein Satz über 1,3 setzt eine umfangreiche oder schwierige Tätigkeit voraus, ein einfacher Fall rechtfertigt weniger.
- **§ 14 RVG-Begründung fehlt.** Ohne dokumentierte Bemessungserwägungen ist der Satz im Gebührenprozess und in der Kostenfestsetzung nicht zu halten.
- **Anrechnung nach Vorbem. 3 Abs. 4 VV vergessen** oder in die falsche Richtung vorgenommen — angerechnet wird die Geschäftsgebühr auf die Verfahrensgebühr, zur Hälfte und höchstens mit 0,75.
- **§ 15a RVG übersehen.** Gegenüber dem erstattungspflichtigen Gegner wirkt die Anrechnung nur unter den dort genannten Voraussetzungen.
- **Veraltete Gebührentabelle.** Der Rechner nennt den `Stand` der hinterlegten Tabelle; wird er nicht gegen die aktuelle Anlage 2 geprüft, wird falsch abgerechnet.
- **Auslagenpauschale VV 7002 über 20 EUR angesetzt** oder je Gebühr statt je Angelegenheit berechnet.
- **Kostennote ohne die Angaben des § 10 RVG.** Ohne unterzeichnete, vollständige Berechnung ist die Vergütung nicht einforderbar.
