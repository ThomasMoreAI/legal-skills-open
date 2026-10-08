---
name: untreue-betrug-wirtschaftsstrafrecht-borghei
title: /wirtschafts-steuerstrafrecht:untreue-betrug-wirtschaftsstrafrecht
description: Prüfung der zentralen Vermögensdelikte des Wirtschaftsstrafrechts – Untreue § 266 StGB mit Missbrauchs- und Treubruchstatbestand, Vermögensbetreuungspflicht und der verfassungsrechtlichen Pflicht zur Präzisierung des Vermögensnachteils, Betrug § 263 StGB in den Erscheinungsformen des Eingehungs- und Erfüllungsbetrugs, Vorenthalten und Veruntreuen von Arbeitsentgelt § 266a StGB als typische Geschäftsführerhaftung, Bestechlichkeit und Bestechung im geschäftlichen Verkehr § 299 StGB sowie die Vermögensabschöpfung nach §§ 73 ff. StGB. Use when ein wirtschaftsstrafrechtlicher Vorwurf gegen Organe oder Mitarbeiter zu bewerten, eine Verteidigungsstrategie zu entwickeln oder das Abschöpfungsrisiko zu beziffern ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/wirtschafts-steuerstrafrecht/skills/untreue-betrug-wirtschaftsstrafrecht
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: white-collar
language: de
---

# /wirtschafts-steuerstrafrecht:untreue-betrug-wirtschaftsstrafrecht

## Zweck

Die Untreue ist der weiteste Tatbestand des deutschen Wirtschaftsstrafrechts und deshalb der am häufigsten überdehnte. Dieser Skill prüft § 266 StGB entlang der vom Bundesverfassungsgericht geforderten Präzisierung, grenzt ihn vom Betrug ab, behandelt die für GmbH-Geschäftsführer wiederkehrende Strafbarkeit nach § 266a StGB und beziffert das Abschöpfungsrisiko nach §§ 73 ff. StGB — das in der Praxis häufig schwerer wiegt als die Strafe selbst.

## Eingaben

- Rolle des Beschuldigten: Organ, Prokurist, Mitarbeiter, externer Berater
- Grundlage einer etwaigen Vermögensbetreuungspflicht: Gesetz, Anstellungsvertrag, Geschäftsordnung, Gesellschafterbeschluss
- Die konkrete Vermögensverfügung mit Datum, Betrag und Empfänger
- Zustimmung der Gesellschafter? Bei der GmbH: Einverständnis aller Gesellschafter erteilt?
- Gegenleistung und deren Werthaltigkeit im Zeitpunkt der Verfügung
- Bei § 266a StGB: Fälligkeitszeitpunkte der Sozialversicherungsbeiträge, Liquiditätslage, Insolvenzreife
- Bei § 299 StGB: Vorteil, Bevorzugung, Wettbewerbsbezug, Kenntnis des Geschäftsherrn
- Erlangtes Etwas für die Abschöpfung: Brutto- oder Nettobetrachtung, Aufwendungen

## Sub-Agent-Architektur

Der **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) belegt Tatbestandsmerkmale und Pflichtenquellen und trennt gesicherte von umstrittener Dogmatik. Der **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) subsumiert im Gutachtenstil und entwirft Einlassung oder Verteidigungsschrift. Der **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft insbesondere, ob der Vermögensnachteil beziffert und nicht nur behauptet wird, und ob die Abschöpfung vollständig adressiert ist.

## Ablauf

### 1. Untreue — die beiden Tatbestände ([§ 266 StGB](https://www.gesetze-im-internet.de/stgb/__266.html))

| Variante | Voraussetzung |
|---|---|
| **Missbrauchstatbestand** | Befugnis, über fremdes Vermögen zu verfügen oder einen anderen zu verpflichten, durch Gesetz, behördlichen Auftrag oder Rechtsgeschäft — und deren Missbrauch im Außenverhältnis |
| **Treubruchstatbestand** | Verletzung der kraft Gesetzes, behördlichen Auftrags, Rechtsgeschäfts oder Treueverhältnisses obliegenden **Vermögensbetreuungspflicht** |

Die **Vermögensbetreuungspflicht** ist das entscheidende einschränkende Merkmal: Erforderlich ist eine Pflicht, fremde Vermögensinteressen von einiger Bedeutung wahrzunehmen, mit Selbständigkeit und Bewegungsspielraum. Eine bloße vertragliche Nebenpflicht genügt nicht. Bei Organen ergibt sie sich aus der Organstellung selbst.

### 2. Vermögensnachteil und die verfassungsrechtliche Präzisierungspflicht

Der Nachteil ist nach dem **Prinzip der Gesamtsaldierung** zu ermitteln: Vermögenslage vor und nach der Verfügung. Das Bundesverfassungsgericht hat § 266 StGB in seiner Entscheidung vom 23.06.2010 – 2 BvR 2559/08, 2 BvR 105/09, 2 BvR 491/09 zwar als mit Art. 103 Abs. 2 GG vereinbar angesehen, dies aber an eine **restriktive, präzisierende Auslegung** geknüpft: Der Nachteil ist eigenständig festzustellen und der Höhe nach zu **beziffern**; er darf nicht mit der Pflichtverletzung gleichgesetzt werden (verifiziert über [dejure](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=2010-06-23&Aktenzeichen=2%20BvR%202559%2F08)).

Praktische Folge für die Verteidigung: Fehlt in Anklage oder Urteil eine nachvollziehbare Bezifferung — etwa bei „Risikogeschäften", schwarzen Kassen oder Kompensationsargumenten —, ist das ein eigenständiger Angriffspunkt. Erforderlichenfalls ist die Bezifferung durch einen Sachverständigen zu ermitteln.

### 3. Einverständnis und Grenzen bei der GmbH

Die Zustimmung des Vermögensinhabers schließt die Pflichtwidrigkeit aus. Bei der GmbH ist das Einverständnis **aller** Gesellschafter grundsätzlich beachtlich — es wirkt jedoch **nicht**, soweit dadurch das zur Erhaltung des Stammkapitals erforderliche Vermögen angegriffen ([§ 30 GmbHG](https://www.gesetze-im-internet.de/gmbhg/__30.html)) oder die Existenz der Gesellschaft gefährdet wird. Das ist die praktisch wichtigste Grenze der Konzern- und Gesellschafterweisung `[unverifiziert – prüfen]`.

### 4. Betrug — Eingehungs- und Erfüllungsbetrug ([§ 263 StGB](https://www.gesetze-im-internet.de/stgb/__263.html))

Prüfungskette: Täuschung → Irrtum → Vermögensverfügung → Vermögensschaden, dazu Vorsatz, Bereicherungsabsicht und Stoffgleichheit.

- **Eingehungsbetrug:** Der Schaden tritt bereits mit Vertragsschluss ein, wenn der Anspruch des Getäuschten wirtschaftlich weniger wert ist als seine eigene Verpflichtung. Maßgeblich ist der Vergleich der beiderseitigen Ansprüche im Zeitpunkt des Vertragsschlusses (Gefährdungsschaden, der zu beziffern ist).
- **Erfüllungsbetrug:** Der Schaden entsteht erst bei der Leistungserbringung, weil die erbrachte Leistung hinter dem Vereinbarten zurückbleibt.

Die Abgrenzung entscheidet über Vollendungszeitpunkt, Verjährungsbeginn und Schadenshöhe. Bei Anlage-, Kredit- und Subventionsvorgängen ist zusätzlich der Kreditbetrug ([§ 265b StGB](https://www.gesetze-im-internet.de/stgb/__265b.html)) und der Subventionsbetrug ([§ 264 StGB](https://www.gesetze-im-internet.de/stgb/__264.html)) zu prüfen, die als abstrakte Gefährdungsdelikte keinen Schaden voraussetzen.

### 5. Vorenthalten von Arbeitsentgelt ([§ 266a StGB](https://www.gesetze-im-internet.de/stgb/__266a.html))

Der praktisch häufigste Vorwurf gegen GmbH-Geschäftsführer. Kernstruktur:

- **Abs. 1:** Vorenthalten der **Arbeitnehmeranteile** zur Sozialversicherung — ein echtes Unterlassungsdelikt, das allein an die Nichtabführung bei Fälligkeit anknüpft. Ein Schaden ist nicht erforderlich, ein Vorteil des Täters ebenfalls nicht.
- **Abs. 2:** Arbeitgeberanteile, aber nur bei unrichtigen Angaben oder pflichtwidrigem In-Unkenntnis-Lassen.
- **Abs. 6:** Strafbefreiung bzw. Absehen von Strafe bei rechtzeitiger Mitteilung an die Einzugsstelle über die Nichtzahlung und die Gründe.

Die zentrale Verteidigungslinie ist die **Unmöglichkeit** der Zahlung: Wer bei Fälligkeit über keine liquiden Mittel verfügte, kann die Abführungspflicht nicht verletzen — allerdings trifft den Geschäftsführer nach der Rechtsprechung eine vorgelagerte Pflicht, im Vorfeld der Fälligkeit für die Abführung der Arbeitnehmeranteile Sorge zu tragen und sie gegenüber anderen Zahlungen vorrangig zu behandeln `[unverifiziert – prüfen]`. In der Insolvenzsituation kollidiert das mit den Massesicherungspflichten; die Auflösung dieses Konflikts ist einzelfallabhängig darzustellen.

### 6. Bestechlichkeit und Bestechung im geschäftlichen Verkehr ([§ 299 StGB](https://www.gesetze-im-internet.de/stgb/__299.html))

Zwei Modelle nebeneinander:

- **Wettbewerbsmodell** (Abs. 1 Nr. 1, Abs. 2 Nr. 1): Vorteil als Gegenleistung für eine **unlautere Bevorzugung** beim Bezug von Waren oder Dienstleistungen.
- **Geschäftsherrenmodell** (Abs. 1 Nr. 2, Abs. 2 Nr. 2): Vorteil als Gegenleistung dafür, dass bei dem Bezug eine **Pflicht gegenüber dem Unternehmen verletzt** wird — hier ist das Einverständnis des Geschäftsherrn tatbestandsausschließend, was die Compliance-Freigabe zum entscheidenden Punkt macht.

Besonders schwere Fälle regelt [§ 300 StGB](https://www.gesetze-im-internet.de/stgb/__300.html). Bei Amtsträgern greifen stattdessen §§ 331 ff. StGB mit deutlich niedrigeren Schwellen.

### 7. Vermögensabschöpfung ([§ 73 StGB](https://www.gesetze-im-internet.de/stgb/__73.html) ff.)

Die Einziehung des Taterlangten ist **zwingend** und steht nicht im Ermessen des Gerichts. Struktur:

- **§ 73 StGB:** Einziehung dessen, was der Täter **durch oder für die Tat erlangt** hat.
- **[§ 73b StGB](https://www.gesetze-im-internet.de/stgb/__73b.html):** Einziehung bei **anderen** — insbesondere bei der Gesellschaft, für die der Täter gehandelt hat. Das ist der Grund, weshalb Abschöpfung auch dort droht, wo das Unternehmen selbst nicht Beschuldigter ist.
- **[§ 73c StGB](https://www.gesetze-im-internet.de/stgb/__73c.html):** Einziehung des Wertes von Taterträgen, wenn der Gegenstand nicht mehr vorhanden ist.
- **[§ 73d StGB](https://www.gesetze-im-internet.de/stgb/__73d.html):** **Bruttoprinzip** — abzuziehen sind nur Aufwendungen, die nicht für die Begehung der Tat aufgewendet wurden. Der Unterschied zwischen Brutto- und Nettobetrachtung entscheidet über Beträge, die die Strafe wirtschaftlich weit übersteigen können.
- **[§ 73e StGB](https://www.gesetze-im-internet.de/stgb/__73e.html):** Ausschluss, soweit der Anspruch des Verletzten erloschen ist — die Schadenswiedergutmachung ist deshalb zugleich Abschöpfungsverteidigung.
- Vorläufige Sicherung über den Vermögensarrest ([§ 111e StPO](https://www.gesetze-im-internet.de/stpo/__111e.html)), der regelmäßig vor der Anklage kommt und das Unternehmen sofort trifft.

### 8. Formulierungshilfe — Verteidigungsschrift zum Vermögensnachteil

```
An die Staatsanwaltschaft <Ort> — Schwerpunktabteilung Wirtschaft
Az. <…>

In dem Ermittlungsverfahren gegen <Mandant> wegen Untreue

I.   Zur Vermögensbetreuungspflicht
     Eine Pflicht im Sinne des § 266 StGB folgt aus <Organstellung /
     Anstellungsvertrag §…>, beschränkt sich jedoch auf <…>.
     Für den beanstandeten Vorgang bestand kein Bewegungsspielraum,
     sondern eine gebundene Weisungslage.

II.  Zur Pflichtverletzung
     Die Entscheidung lag im Rahmen des unternehmerischen
     Ermessens: Sie beruhte auf angemessener Information, erfolgte
     im Unternehmensinteresse und ohne Sonderinteresse.

III. Zum Vermögensnachteil — Bezifferung
     Der Nachteil ist nach dem Grundsatz der Gesamtsaldierung
     eigenständig festzustellen und zu beziffern. Die Verfügung vom
     <Datum> über <…> EUR stand eine Gegenleistung im Wert von
     <…> EUR gegenüber (Anlage <…>). Ein Nachteil ist danach nicht
     dargetan; die bloße Pflichtverletzung ersetzt seine
     Feststellung nicht.

IV.  Zur Einziehung §§ 73 ff. StGB
     Ein Erlangen durch oder für die Tat liegt beim Beschuldigten
     nicht vor. Soweit auf § 73b StGB gegenüber der Gesellschaft
     abgestellt wird, ist § 73e StGB zu beachten: Der Anspruch des
     Verletzten ist durch Zahlung vom <Datum> erloschen.

V.   Anträge
     1. Einstellung nach § 170 Abs. 2 StPO.
     2. Aufhebung des Vermögensarrests nach § 111e StPO.
     3. Beiziehung des Gutachtens <…> zur Werthaltigkeit.

<Ort, Datum, Unterschrift — Rechtsanwalt, Strafverteidiger>
```

## Quellen

### Statute

- [§ 263 StGB](https://www.gesetze-im-internet.de/stgb/__263.html), [§ 264 StGB](https://www.gesetze-im-internet.de/stgb/__264.html), [§ 265b StGB](https://www.gesetze-im-internet.de/stgb/__265b.html), [§ 266 StGB](https://www.gesetze-im-internet.de/stgb/__266.html), [§ 266a StGB](https://www.gesetze-im-internet.de/stgb/__266a.html), [§ 299 StGB](https://www.gesetze-im-internet.de/stgb/__299.html), [§ 300 StGB](https://www.gesetze-im-internet.de/stgb/__300.html)
- [§ 73 StGB](https://www.gesetze-im-internet.de/stgb/__73.html), [§ 73b StGB](https://www.gesetze-im-internet.de/stgb/__73b.html), [§ 73c StGB](https://www.gesetze-im-internet.de/stgb/__73c.html), [§ 73d StGB](https://www.gesetze-im-internet.de/stgb/__73d.html), [§ 73e StGB](https://www.gesetze-im-internet.de/stgb/__73e.html), [§ 111e StPO](https://www.gesetze-im-internet.de/stpo/__111e.html)
- [§ 30 GmbHG](https://www.gesetze-im-internet.de/gmbhg/__30.html), [§ 43 GmbHG](https://www.gesetze-im-internet.de/gmbhg/__43.html), [§ 93 AktG](https://www.gesetze-im-internet.de/aktg/__93.html) (Business Judgment Rule als Maßstab der Pflichtverletzung), [Art. 103 Abs. 2 GG](https://www.gesetze-im-internet.de/gg/art_103.html)

### Kommentare

- Dierlamm, in: MüKoStGB, 4. Aufl. 2022, § 266 Rn. 1 ff. (Vermögensbetreuungspflicht)
- Perron, in: Schönke / Schröder, StGB, 30. Aufl. 2019, § 266 Rn. 1 ff. und § 263 Rn. 1 ff.
- Radtke, in: MüKoStGB, 4. Aufl. 2022, § 266a Rn. 1 ff. (Unmöglichkeit, Vorrang der Arbeitnehmeranteile)
- Saliger, in: Satzger / Schluckebier / Widmaier, StGB, 6. Aufl. 2024, § 266 Rn. 1 ff.
- Köhler, in: Meyer-Goßner / Schmitt, StPO, 67. Aufl. 2024, § 111e Rn. 1 ff. (Vermögensarrest)

### Rechtsprechung

- BVerfG, Beschl. v. 23.06.2010 – 2 BvR 2559/08, 2 BvR 105/09, 2 BvR 491/09 (Vereinbarkeit des § 266 StGB mit Art. 103 Abs. 2 GG bei restriktiver, präzisierender Auslegung; eigenständige Feststellung und Bezifferung des Vermögensnachteils) — [dejure](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=2010-06-23&Aktenzeichen=2%20BvR%202559%2F08)
- Rechtsprechung zur Grenze des Gesellschaftereinverständnisses bei Existenzgefährdung und Stammkapitalangriff `[unverifiziert – prüfen]`
- Rechtsprechung zur vorgelagerten Pflicht des Geschäftsführers, die Abführung der Arbeitnehmeranteile sicherzustellen `[unverifiziert – prüfen]`

> Nicht extern verifizierte Fundstellen sind vor Verwendung in juris oder Beck-Online zu ermitteln.

## Ausgabeformat

```
WIRTSCHAFTSSTRAFRECHT — <Az.> — <Datum>
VERTRAULICH — STRAFVERTEIDIGUNG — § 43a Abs. 2 BRAO

Gesamtbefund: [🟢 Einstellung erreichbar / 🟡 Verhandlungslösung /
               🔴 Anklage wahrscheinlich]

I.    Delikte                      [§ 266 / § 263 / § 266a / § 299 StGB]
II.   Untreue § 266 StGB
      Variante                     [Missbrauch / Treubruch]
      Vermögensbetreuungspflicht   <Quelle>  [🟢 / 🔴 nicht dargetan]
      Pflichtverletzung            <…>  [unternehmerisches Ermessen?]
      Einverständnis               [N/A / alle Gesellschafter /
                                    🔴 Grenze § 30 GmbHG]
      Vermögensnachteil beziffert  <…> EUR  [🟢 / 🔴 nur behauptet]
III.  Betrug § 263 StGB            [Eingehungs- / Erfüllungsbetrug]
      Schaden im Zeitpunkt         <Vertragsschluss / Erfüllung>
IV.   § 266a StGB
      Fälligkeitszeitpunkte        <…>
      Liquidität bei Fälligkeit    [vorhanden / 🔴 nicht vorhanden]
      Mitteilung § 266a Abs. 6     [erfolgt am <…> / unterblieben]
V.    § 299 StGB                   [Wettbewerbs- / Geschäftsherrenmodell]
      Einverständnis Geschäftsherr [ja → tatbestandsausschließend / nein]
VI.   Vermögensabschöpfung
      Erlangtes Etwas              <…> EUR  [Bruttoprinzip § 73d StGB]
      Adressat                     [Täter § 73 / Gesellschaft § 73b StGB]
      § 73e StGB                   [Anspruch des Verletzten erloschen?]
      Vermögensarrest § 111e StPO  [angeordnet am <…>]
VII.  Verjährung                   <§ 78 StGB, Beginn, Ergebnis>

Empfehlung: <…>
Nächster Schritt: <Akteneinsicht / Einlassung / Wiedergutmachung>
```

## Risiken / typische Fehler

- **Vermögensnachteil nicht beziffert**, sondern aus der Pflichtverletzung geschlossen — das verfehlt die vom Bundesverfassungsgericht geforderte eigenständige Feststellung und ist der stärkste Angriffspunkt gegen einen Untreuevorwurf.
- **Vermögensbetreuungspflicht zu weit angenommen.** Eine vertragliche Nebenpflicht ohne Selbständigkeit und Bewegungsspielraum begründet keine Pflicht im Sinne des § 266 StGB.
- **Gesellschaftereinverständnis ungeprüft als Rechtfertigung behandelt** — die Grenze des § 30 GmbHG und der Existenzgefährdung wird übersehen.
- **Eingehungs- und Erfüllungsbetrug nicht getrennt** — Vollendungszeitpunkt, Verjährungsbeginn und Schadenshöhe hängen daran.
- **§ 266a StGB als Vermögensdelikt behandelt.** Abs. 1 ist ein echtes Unterlassungsdelikt; ein Schaden oder Vorteil ist nicht erforderlich.
- **Mitteilung nach § 266a Abs. 6 StGB unterlassen**, obwohl die Zahlungsunfähigkeit bekannt war — die Strafbefreiungsmöglichkeit verfällt ungenutzt.
- **Kollision von Abführungspflicht und Massesicherungspflicht in der Krise nicht dargestellt.**
- **Vermögensabschöpfung erst nach der Anklage bedacht.** Der Vermögensarrest nach § 111e StPO trifft das Unternehmen regelmäßig vorher; § 73e StGB und die Schadenswiedergutmachung sind früh zu adressieren.
- **Bruttoprinzip des § 73d StGB unterschätzt** — die Einziehung kann die wirtschaftliche Hauptsanktion sein und die Strafe deutlich übersteigen.
- **§ 299 StGB nur nach dem Wettbewerbsmodell geprüft**, obwohl das Geschäftsherrenmodell einschlägig ist, bei dem das Einverständnis des Unternehmens tatbestandsausschließend wirkt.
