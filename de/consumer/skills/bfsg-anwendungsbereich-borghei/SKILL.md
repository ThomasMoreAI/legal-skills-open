---
name: bfsg-anwendungsbereich-borghei
title: /barrierefreiheit-bfsg:bfsg-anwendungsbereich
description: Anwendungsbereich des Barrierefreiheitsstärkungsgesetzes – abschließender Produktkatalog § 1 Abs. 2 BFSG und Dienstleistungskatalog § 1 Abs. 3 BFSG, Stichtag 28.06.2025, Inhaltsausnahmen § 1 Abs. 4, Kleinstunternehmensausnahme § 3 Abs. 3 iVm der Legaldefinition in § 2 Nr. 17 (weniger als zehn Beschäftigte und höchstens 2 Mio. EUR Umsatz oder Bilanzsumme), Beschränkung auf Verbraucherangebote, Übergangsbestimmungen § 38 mit der Frist 27.06.2030 und der Fünfzehnjahresgrenze für Selbstbedienungsterminals sowie die Abgrenzung zum Recht öffentlicher Stellen nach BGG und BITV 2.0. Use when zu klären ist, ob ein Produkt oder eine Dienstleistung überhaupt dem BFSG unterfällt und ab wann.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/barrierefreiheit-bfsg/skills/bfsg-anwendungsbereich
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: consumer
language: de
---

# /barrierefreiheit-bfsg:bfsg-anwendungsbereich

## Zweck

Der Skill beantwortet die Eingangsfrage jedes Barrierefreiheitsmandats: Ist das Angebot überhaupt erfasst, in welcher Rolle und ab wann. Er arbeitet die beiden **abschließenden** Kataloge des § 1 BFSG ab, prüft die Kleinstunternehmensausnahme in ihrer engen gesetzlichen Fassung und ordnet Altbestände den Übergangsbestimmungen des § 38 zu. Er grenzt außerdem das BFSG vom Recht der öffentlichen Stellen ab, das einem völlig anderen Regime folgt.

## Eingaben

- Produkt- oder Dienstleistungsbeschreibung, Vertriebsweg, Zielgruppe
- Rolle: Hersteller, Bevollmächtigter, Einführer, Händler, Dienstleistungserbringer
- Datum des Inverkehrbringens der Produkte bzw. Beginn der Dienstleistungserbringung
- Unternehmenskennzahlen: Beschäftigtenzahl, Jahresumsatz, Bilanzsumme
- Ob sich das Angebot an Verbraucher richtet oder ausschließlich an Unternehmen
- Bei Websites und Apps: Veröffentlichungsdatum von Medien, Dokumenten, Archivinhalten
- Bei Selbstbedienungsterminals: Datum der Ingebrauchnahme
- Bestehende Dienstleistungsverträge mit Datum des Vertragsschlusses

## Sub-Agent-Architektur

Der Researcher beschafft BFSG, BFSGV, die zugrunde liegende Richtlinie (EU) 2019/882 sowie die Leitlinien für Kleinstunternehmen nach § 3 Abs. 3 S. 2 BFSG und die Veröffentlichungen der Bundesfachstelle für Barrierefreiheit. Der Drafter ordnet das Angebot den Katalogen zu und rechnet die Übergangsfristen. Der Reviewer prüft, ob die Kleinstunternehmensausnahme nicht auf Produkte erstreckt wurde, ob der B2C-Bezug tatsächlich vorliegt und ob die Abgrenzung zum BGG sauber gezogen ist.

## Ablauf

### 1. Regime bestimmen — BFSG oder BGG/BITV 2.0

**Dieser Schritt steht vor allem anderen.** Beide Regelwerke betreffen digitale Barrierefreiheit, sind aber getrennt:

| Adressat | Regelwerk | Durchsetzung |
|---|---|---|
| **Private Wirtschaftsakteure**, Angebot an **Verbraucher** | [BFSG](https://www.gesetze-im-internet.de/bfsg/) + [BFSGV](https://www.gesetze-im-internet.de/bfsgv/) | Marktüberwachungsbehörden der Länder, §§ 20 ff. BFSG; Bußgeld § 37 BFSG |
| **Öffentliche Stellen** des Bundes | [BGG](https://www.gesetze-im-internet.de/bgg/) §§ 12a, 12b + [BITV 2.0](https://www.gesetze-im-internet.de/bitv_2_0/) | Überwachungsstelle des Bundes, Schlichtungsstelle § 16 BGG |
| Öffentliche Stellen der Länder | Landesbehindertengleichstellungsgesetze und Landes-BITV | Landesrecht `[unverifiziert – prüfen]` je Land |

Ein Unternehmen kann beiden Regimen unterliegen, etwa als Auftragnehmer einer öffentlichen Stelle und zugleich als Anbieter im elektronischen Geschäftsverkehr. Vertiefung: `/barrierefreiheit-bfsg:bitv-oeffentliche-stellen`.

### 2. Produktkatalog prüfen ([§ 1 Abs. 2 BFSG](https://www.gesetze-im-internet.de/bfsg/__1.html))

Das Gesetz gilt für folgende Produkte, die **nach dem 28. Juni 2025 in den Verkehr gebracht** werden — der Katalog ist **abschließend**:

1. Hardwaresysteme für Universalrechner für Verbraucher einschließlich der für sie bestimmten Betriebssysteme;
2. Selbstbedienungsterminals, nämlich Zahlungsterminals nebst zugehöriger Hard- und Software sowie – soweit zur Erbringung erfasster Dienstleistungen bestimmt – Geldautomaten, Fahrausweisautomaten, Check-in-Automaten und interaktive Informationsterminals (nicht: fest in Fahrzeuge, Luftfahrzeuge, Schiffe oder Schienenfahrzeuge eingebaute Terminals);
3. Verbraucherendgeräte mit interaktivem Leistungsumfang für Telekommunikationsdienste;
4. Verbraucherendgeräte mit interaktivem Leistungsumfang für den Zugang zu audiovisuellen Mediendiensten;
5. E-Book-Lesegeräte.

Maßgeblich ist das **Inverkehrbringen**, nicht der Verkauf an den Endkunden. Lagerbestände, die vor dem Stichtag in Verkehr gebracht wurden, bleiben erfasst von der alten Rechtslage.

### 3. Dienstleistungskatalog prüfen ([§ 1 Abs. 3 BFSG](https://www.gesetze-im-internet.de/bfsg/__1.html))

Das Gesetz gilt für folgende Dienstleistungen, die **für Verbraucher nach dem 28. Juni 2025 erbracht** werden — ebenfalls abschließend:

1. Telekommunikationsdienste, ausgenommen Übertragungsdienste für Maschine-Maschine-Kommunikation;
2. bestimmte Elemente von **Personenbeförderungsdiensten** im Luft-, Bus-, Schienen- und Schiffsverkehr — Webseiten, mobile Anwendungen, elektronische Tickets und Ticketdienste, Verkehrsinformationen einschließlich Echtzeitinformationen, interaktive Selbstbedienungsterminals im Unionsgebiet; für Stadt-, Vorort- und Regionalverkehrsdienste gelten **nur** die interaktiven Selbstbedienungsterminals (Buchst. e);
3. **Bankdienstleistungen für Verbraucher**;
4. E-Books und hierfür bestimmte Software;
5. **Dienstleistungen im elektronischen Geschäftsverkehr**.

Nr. 5 ist der praktisch wichtigste Tatbestand: Er erfasst Online-Shops und andere elektronisch geschlossene Verbraucherverträge. Ein reiner Unternehmensshop ohne Verbraucherangebot fällt heraus; eine Website ohne Vertragsschlussmöglichkeit ebenfalls — die Abgrenzung ist zu begründen und zu dokumentieren.

### 4. Inhaltsausnahmen prüfen ([§ 1 Abs. 4 BFSG](https://www.gesetze-im-internet.de/bfsg/__1.html))

Für Webseiten und mobile Anwendungen gilt das Gesetz **nicht** für:

1. aufgezeichnete zeitbasierte Medien, die **vor dem 28.06.2025** veröffentlicht wurden;
2. Dateiformate von Büro-Anwendungen, die vor dem 28.06.2025 veröffentlicht wurden;
3. Online-Karten und Kartendienste, sofern bei Navigationskarten wesentliche Informationen barrierefrei in digitaler Form bereitgestellt werden;
4. Inhalte Dritter, die der Wirtschaftsakteur weder finanziert noch entwickelt hat und die nicht seiner Kontrolle unterliegen;
5. Archivinhalte, die nach dem 28.06.2025 weder aktualisiert noch überarbeitet werden.

Die Archivausnahme (Nr. 5) verliert ihre Wirkung, sobald der Inhalt angefasst wird. Die Drittinhaltsausnahme (Nr. 4) trägt nicht für eingebundene Dienste, die der Betreiber steuert oder bezahlt.

Unberührt bleiben nach § 1 Abs. 5 BFSG die §§ 45a bis 45d und 95a bis 96 UrhG sowie die VO (EU) 2017/1563 (Marrakesch-Umsetzung).

### 5. Kleinstunternehmensausnahme prüfen ([§ 3 Abs. 3 BFSG](https://www.gesetze-im-internet.de/bfsg/__3.html))

**Der Wortlaut ist enger, als er in der Beratungspraxis zitiert wird:**

> „Absatz 1 gilt nicht für Kleinstunternehmen, die **Dienstleistungen** anbieten oder erbringen."

Konsequenzen:

- Die Ausnahme gilt **nur für Dienstleistungen**, nicht für Produkte. Ein Kleinstunternehmen, das erfasste Produkte herstellt, einführt oder vertreibt, bleibt vollständig gebunden.
- **Kleinstunternehmen** ist nach [§ 2 Nr. 17 BFSG](https://www.gesetze-im-internet.de/bfsg/__2.html) ein Unternehmen, das **weniger als zehn Personen beschäftigt** und **entweder** einen Jahresumsatz von höchstens 2 Mio. EUR erzielt **oder** dessen Jahresbilanzsumme höchstens 2 Mio. EUR beträgt. Beide Schwellen sind kumulativ mit der Beschäftigtenzahl zu prüfen.
- Für Kleinstunternehmen, die **mit Produkten befasst** sind, gelten Dokumentationserleichterungen bei § 16 Abs. 4 und § 17 Abs. 2 S. 3, 4 BFSG — die materiellen Anforderungen bleiben bestehen.
- Das BMAS erstellt Leitlinien für Kleinstunternehmen (§ 3 Abs. 3 S. 2 BFSG).

### 6. Übergangsbestimmungen rechnen ([§ 38 BFSG](https://www.gesetze-im-internet.de/bfsg/__38.html))

| Konstellation | Übergang |
|---|---|
| Dienstleistungserbringung unter Einsatz von Produkten, die **vor dem 28.06.2025** rechtmäßig eingesetzt wurden | zulässig **bis zum 27.06.2030** (§ 38 Abs. 1 S. 1) |
| **Vor dem 28.06.2025 geschlossene Verträge** über Dienstleistungen | unverändertes Fortbestehen bis zum Ablauf der vereinbarten Zeit, **längstens bis zum 27.06.2030** (§ 38 Abs. 1 S. 2) |
| **Selbstbedienungsterminals**, die vor dem 28.06.2025 rechtmäßig eingesetzt wurden | bis zum Ende der wirtschaftlichen Nutzungsdauer, **höchstens 15 Jahre ab Ingebrauchnahme** (§ 38 Abs. 2) |

Die Fünfzehnjahresfrist läuft **ab Ingebrauchnahme**, nicht ab dem Stichtag — bei Altgeräten kann sie bereits abgelaufen sein.

### 7. Ergebnis und Folgeschritte

Ist der Anwendungsbereich eröffnet, schließen sich an:

- Produkte → `/barrierefreiheit-bfsg:bfsg-produktkonformitaet`
- Dienstleistungen, insbesondere E-Commerce → `/barrierefreiheit-bfsg:bfsg-dienstleistung-ecommerce`
- Öffentliche Stellen → `/barrierefreiheit-bfsg:bitv-oeffentliche-stellen`

## Deterministische Berechnung

Die Stichtage des BFSG sind Fixdaten; zu rechnen ist die Fünfzehnjahresfrist des § 38 Abs. 2 und der Ablauf laufender Dienstleistungsverträge. Der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) macht nur die Arithmetik:

```bash
# Selbstbedienungsterminal, Ingebrauchnahme 01.09.2014: 15 Jahre
python -m scripts.legal_calc.cli frist --ereignis 01.09.2014 --menge 15 --einheit jahre --land BY

# Äußerste Grenze für Altverträge nach § 38 Abs. 1 S. 2: 27.06.2030 (Fixdatum, keine Berechnung)
```

Die wirtschaftliche Nutzungsdauer ist eine tatsächliche Feststellung und gesondert zu belegen.

## Quellen

### Statute

- [§ 1 BFSG](https://www.gesetze-im-internet.de/bfsg/__1.html), [§ 2 BFSG](https://www.gesetze-im-internet.de/bfsg/__2.html), [§ 3 BFSG](https://www.gesetze-im-internet.de/bfsg/__3.html), [§ 16 BFSG](https://www.gesetze-im-internet.de/bfsg/__16.html), [§ 17 BFSG](https://www.gesetze-im-internet.de/bfsg/__17.html), [§ 37 BFSG](https://www.gesetze-im-internet.de/bfsg/__37.html), [§ 38 BFSG](https://www.gesetze-im-internet.de/bfsg/__38.html)
- [BFSGV](https://www.gesetze-im-internet.de/bfsgv/), insbesondere [§ 1](https://www.gesetze-im-internet.de/bfsgv/__1.html), [§ 3](https://www.gesetze-im-internet.de/bfsgv/__3.html)
- Richtlinie (EU) 2019/882 (European Accessibility Act), Art. 2, 4, Anhang I — [EUR-Lex](https://eur-lex.europa.eu/eli/dir/2019/882/oj)
- [§ 12a BGG](https://www.gesetze-im-internet.de/bgg/__12a.html), [§ 12b BGG](https://www.gesetze-im-internet.de/bgg/__12b.html), [BITV 2.0](https://www.gesetze-im-internet.de/bitv_2_0/)
- [§ 45a UrhG](https://www.gesetze-im-internet.de/urhg/__45a.html) ff.; VO (EU) 2017/1563

### Kommentare und Literatur

- Ritgen/Sellmann, BFSG, Kommentar, § 1, § 3, § 38.
- Dörr/Natlacen, Barrierefreiheitsstärkungsgesetz, Praxishandbuch.
- Beiträge zum Anwendungsbereich des BFSG in K&R, MMR und ZD 2024/2025 (Fundstelle vor Verwendung prüfen) `[unverifiziert – prüfen]`
- Bundesfachstelle für Barrierefreiheit, Standardauflistung und Konformitätstabellen nach § 3 Abs. 2 BFSGV.

### Rechtsprechung

Zum BFSG liegt bislang **keine gefestigte Rechtsprechung** vor; das Gesetz ist erst seit dem 28.06.2025 anwendbar. Für die Abgrenzung des elektronischen Geschäftsverkehrs kann auf die Rechtsprechung zum Fernabsatzrecht zurückgegriffen werden; jede Entscheidung ist vor Verwendung in juris oder Beck-Online zu verifizieren `[unverifiziert – prüfen]`.

## Ausgabeformat

```
BFSG-BETROFFENHEIT — <Mandant> — <Datum>

I.   Regimezuordnung
     Adressat:                [privater Wirtschaftsakteur / öffentliche Stelle / beides]
     Maßgeblich:              [BFSG + BFSGV | BGG + BITV 2.0 | Landesrecht <X>]

II.  Rolle
     [Hersteller / Bevollmächtigter / Einführer / Händler / Dienstleistungserbringer]
     Mehrfachrolle § 12 BFSG: [ja — Herstellerpflichten / nein]

III. Produktkatalog § 1 Abs. 2
     Nr. 1–5 geprüft:         <Zuordnung oder Negativfeststellung>
     Inverkehrbringen:        <Datum>  → [erfasst / nicht erfasst]

IV.  Dienstleistungskatalog § 1 Abs. 3
     Nr. 1–5 geprüft:         <Zuordnung oder Negativfeststellung>
     Verbraucherbezug:        [ja / nein — B2B ausgenommen]
     Erbringung ab:           <Datum>  → [erfasst / nicht erfasst]

V.   Inhaltsausnahmen § 1 Abs. 4
     Nr. 1–5:                 <je Nummer: einschlägig / nicht einschlägig>

VI.  Kleinstunternehmen § 3 Abs. 3 iVm § 2 Nr. 17
     Beschäftigte < 10:       [ja / nein]
     Umsatz ≤ 2 Mio. EUR oder Bilanzsumme ≤ 2 Mio. EUR: [ja / nein]
     Ergebnis:                [Ausnahme greift — nur für Dienstleistungen / greift nicht]

VII. Übergang § 38
     Altprodukte im Diensteinsatz:   bis 27.06.2030
     Altverträge:                    bis <Datum>, längstens 27.06.2030
     Selbstbedienungsterminals:      Ingebrauchnahme <Datum> + 15 Jahre = <Datum>

VIII.Ergebnis und nächste Schritte
IX.  Risiko: 🟢 / 🟡 / 🔴 <Begründung>
X.   Quellenverzeichnis
```

## Risiken / typische Fehler

- **Kleinstunternehmensausnahme auf Produkte erstreckt.** § 3 Abs. 3 BFSG nimmt ausdrücklich nur Kleinstunternehmen aus, die **Dienstleistungen** anbieten oder erbringen.
- **Kleinstunternehmen falsch definiert.** § 2 Nr. 17 BFSG verlangt **weniger als zehn** Beschäftigte **und** eine der beiden 2-Mio.-EUR-Schwellen — nicht die allgemeine KMU-Definition.
- **Katalog als Beispielsliste behandelt.** § 1 Abs. 2 und Abs. 3 BFSG sind abschließend; was nicht aufgeführt ist, fällt nicht unter das BFSG.
- **B2B-Angebote einbezogen.** Das BFSG erfasst Dienstleistungen, die **für Verbraucher** erbracht werden.
- **Stichtag auf den Verkauf statt auf das Inverkehrbringen bezogen.**
- **Archivausnahme überdehnt.** § 1 Abs. 4 Nr. 5 BFSG trägt nur, solange der Inhalt nach dem 28.06.2025 weder aktualisiert noch überarbeitet wird.
- **BFSG und BGG/BITV 2.0 vermengt.** Adressaten, Anforderungen und Durchsetzung unterscheiden sich vollständig.
- **§ 38 Abs. 2 ab dem Stichtag gerechnet.** Die Fünfzehnjahresfrist läuft ab **Ingebrauchnahme** des Terminals.
- **Rechtsprechung erfunden.** Zum BFSG existiert kaum Judikatur; jede Entscheidung ist zu belegen oder als `[unverifiziert – prüfen]` zu kennzeichnen.
