---
name: verbandsklage-zulaessigkeit-borghei
title: /verbandsklage-vdug:verbandsklage-zulaessigkeit
description: Zulässigkeit der Verbandsklage nach dem VDuG – Klagearten § 1 Abs. 1 (Abhilfeklage und Musterfeststellungsklage), Gleichstellung kleiner Unternehmen mit Verbrauchern § 1 Abs. 2 (weniger als zehn Beschäftigte und höchstens 2 Mio. EUR Umsatz oder Bilanz), klageberechtigte Stellen § 2 mit der Fünf-Prozent-Grenze für Unternehmenszuwendungen und der unwiderleglichen Vermutung für überwiegend öffentlich geförderte Verbraucherzentralen, ausschließliche OLG-Zuständigkeit am allgemeinen Gerichtsstand des Unternehmers § 3, Verbraucherquorum von mindestens 50 Betroffenen § 4 Abs. 1, Verbot und Offenlegung der Drittfinanzierung § 4 Abs. 2, 3, Offenlegung von Beweismitteln § 6, Streitgenossenschaft § 7 und Sperrwirkung der Verbandsklage § 8. Use when eine Verbandsklage erhoben, abgewehrt oder auf ihre Zulässigkeit geprüft werden soll.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/verbandsklage-vdug/skills/verbandsklage-zulaessigkeit
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: litigation
language: de
---

# /verbandsklage-vdug:verbandsklage-zulaessigkeit

## Zweck

Der Skill prüft die Zulässigkeit einer Verbandsklage nach dem [VDuG](https://www.gesetze-im-internet.de/vdug/) — aus Sicht der klageberechtigten Stelle wie aus Sicht des beklagten Unternehmens. Er arbeitet die Zulässigkeitshürden in der Reihenfolge ab, in der sie die Praxis entscheiden: Klageberechtigung, Quorum, Finanzierung, Zuständigkeit, Sperrwirkung. Die Finanzierungsrüge ist dabei der schärfste Verteidigungsansatz des Gebiets.

## Eingaben

- Klageschrift oder Klageentwurf mit Angabe der Klageart
- Klagende Stelle: Eintragung nach § 4 UKlaG oder Verzeichnis der Kommission nach Art. 5 Abs. 1 S. 4 RL (EU) 2020/1828
- Mittelherkunft der klagenden Stelle; Anteil von Unternehmenszuwendungen; Prozessfinanzierer und dessen Vereinbarung
- Zahl und Zuschnitt der betroffenen Verbraucher; ob kleine Unternehmen darunter sind
- Allgemeiner Gerichtsstand des beklagten Unternehmers
- Ob bereits eine Verbandsklage, ein KapMuG-Musterverfahren oder Individualklagen zum selben Lebenssachverhalt anhängig sind

## Sub-Agent-Architektur

Der Researcher beschafft VDuG, UKlaG, RL (EU) 2020/1828, das Verbandsklageregister des Bundesamts für Justiz und die noch junge OLG- und BGH-Rechtsprechung. Der Drafter prüft die Zulässigkeit Punkt für Punkt und entwirft Klage oder Zulässigkeitsrüge. Der Reviewer kontrolliert Quorum, Finanzierungsoffenlegung und Sperrwirkung und verhindert, dass eine Individualklage-Argumentation in ein Kollektivverfahren übertragen wird.

## Ablauf

### 1. Klageart und Anwendungsbereich bestimmen ([§ 1 VDuG](https://www.gesetze-im-internet.de/vdug/__1.html))

Das VDuG kennt **zwei** Verbandsklagen in bürgerlichen Rechtsstreitigkeiten, die Ansprüche und Rechtsverhältnisse einer **Vielzahl von Verbrauchern** gegen einen Unternehmer betreffen:

| Klageart | Ziel | Vertiefung |
|---|---|---|
| **Abhilfeklage** (§§ 14 ff.) | Verurteilung des Unternehmers zur **Leistung an die betroffenen Verbraucher**, auch als kollektiver Gesamtbetrag | `/verbandsklage-vdug:abhilfeklage-vdug` |
| **Musterfeststellungsklage** (§ 41) | Feststellung des Vorliegens oder Nichtvorliegens tatsächlicher und rechtlicher Voraussetzungen (**Feststellungsziele**) | `/verbandsklage-vdug:musterfeststellungsklage-vdug` |

Zwei Weichenstellungen, die früh zu treffen sind:

- **§ 1 Abs. 2** — **Kleine Unternehmen gelten als Verbraucher**: weniger als zehn Beschäftigte **und** Jahresumsatz oder Jahresbilanz von höchstens 2 Mio. EUR. Der persönliche Anwendungsbereich ist damit weiter als der Verbraucherbegriff des [§ 13 BGB](https://www.gesetze-im-internet.de/bgb/__13.html).
- **§ 1 Abs. 3** — Ein eröffnetes **KapMuG**-Musterverfahren zum selben Lebenssachverhalt steht der Verbandsklage **nicht** entgegen. Beide Regime können nebeneinander laufen.

### 2. Klageberechtigung prüfen ([§ 2 VDuG](https://www.gesetze-im-internet.de/vdug/__2.html))

Klageberechtigt sind **nur**:

1. **Qualifizierte Verbraucherverbände**, die
   - a) in der Liste nach [§ 4 UKlaG](https://www.gesetze-im-internet.de/uklag/__4.html) eingetragen sind **und**
   - b) **nicht mehr als 5 Prozent** ihrer finanziellen Mittel durch Zuwendungen von Unternehmen beziehen;
2. **qualifizierte Einrichtungen aus anderen Mitgliedstaaten**, die im Verzeichnis der Kommission nach Art. 5 Abs. 1 S. 4 RL (EU) 2020/1828 eingetragen sind.

Verfahrensrechtlich flankiert:

- **§ 2 Abs. 2** — Bestehen **ernsthafte Zweifel** an der Fünf-Prozent-Grenze, **verlangt das Gericht** vom Kläger die Offenlegung seiner finanziellen Mittel. Der Beklagte muss die Zweifel also nur säen, nicht beweisen.
- **§ 2 Abs. 3** — Für **Verbraucherzentralen und andere überwiegend mit öffentlichen Mitteln geförderte** Verbraucherverbände wird die Einhaltung **unwiderleglich vermutet**. Gegen sie läuft die Rüge ins Leere.

### 3. Zuständigkeit bestimmen ([§ 3 VDuG](https://www.gesetze-im-internet.de/vdug/__3.html))

Ausschließlich sachlich und örtlich zuständig ist das **Oberlandesgericht**, in dessen Bezirk sich der **allgemeine Gerichtsstand des Unternehmers** befindet. Es gibt keine erste Instanz beim Landgericht.

Zu beachten:

- **Abs. 2** — Unionsrechtliche und unmittelbar anwendbare völkerrechtliche Zuständigkeitsregeln gehen vor (insbesondere die Brüssel-Ia-VO bei Auslandsbezug).
- **Abs. 3** — Die Länder können die Verbandsklagen bei **einem** OLG oder beim Obersten Landesgericht konzentrieren. Die einschlägige Landesverordnung ist konkret zu prüfen `[unverifiziert – prüfen]` je Land.

### 4. Verbraucherquorum prüfen ([§ 4 Abs. 1 VDuG](https://www.gesetze-im-internet.de/vdug/__4.html))

Die Verbandsklage ist nur zulässig, wenn die klageberechtigte Stelle **nachvollziehbar darlegt**, dass

- bei der **Abhilfeklage** Ansprüche von **mindestens 50 Verbrauchern** betroffen sein **können**, oder
- bei der **Musterfeststellungsklage** die Ansprüche oder Rechtsverhältnisse von **mindestens 50 Verbrauchern** von den Feststellungszielen abhängen **können**.

Maßstab ist die **Darlegung**, nicht der Beweis, und das Quorum knüpft an ein **Können**, nicht an eine feststehende Betroffenheit. Bei gemeinschaftlicher Klage nach § 7 Abs. 1 ist die **Gesamtzahl** der betroffenen Verbraucher maßgeblich.

### 5. Finanzierung prüfen ([§ 4 Abs. 2, 3 VDuG](https://www.gesetze-im-internet.de/vdug/__4.html)) — der schärfste Angriffspunkt

Die Verbandsklage ist **unzulässig**, wenn sie von einem Dritten finanziert wird,

1. der ein **Wettbewerber** des verklagten Unternehmers ist,
2. der vom verklagten Unternehmer **abhängig** ist,
3. dem ein wirtschaftlicher Anteil an der zu erbringenden Leistung von **mehr als 10 Prozent** versprochen ist, oder
4. von dem zu erwarten ist, dass er die **Prozessführung** der klageberechtigten Stelle — **einschließlich Entscheidungen über Vergleiche** — zu Lasten der Verbraucher **beeinflussen** wird.

**Offenlegungspflicht (Abs. 3):** Mit Klageeinreichung ist die **Herkunft der Mittel** offenzulegen; bei Drittfinanzierung zusätzlich die **mit dem Finanzierer getroffenen Vereinbarungen**. Das gilt auch, wenn die Finanzierung **erst nach Klageeinreichung** hinzutritt.

Die Zehn-Prozent-Grenze der Nr. 3 trifft marktübliche Erfolgsbeteiligungen von Prozessfinanzierern unmittelbar und ist deshalb in jedem Mandat zu rechnen, nicht zu schätzen.

### 6. Weitere Zulässigkeitsfragen

- **[§ 5 VDuG](https://www.gesetze-im-internet.de/vdug/__5.html)** — Anforderungen an die Klageschrift.
- **[§ 6 VDuG](https://www.gesetze-im-internet.de/vdug/__6.html)** — **Offenlegung von Beweismitteln** nebst Androhung und Festsetzung von Ordnungsmitteln. Das ist ein im deutschen Zivilprozess ungewöhnliches Instrument und **keine** US-Discovery; die Anordnung setzt einen konkreten, auf bestimmte Beweismittel bezogenen Antrag voraus (vgl. `CONVENTIONS.md` zum Verbot von Discovery-Argumenten).
- **[§ 7 VDuG](https://www.gesetze-im-internet.de/vdug/__7.html)** — Streitgenossenschaft mehrerer klageberechtigter Stellen.
- **[§ 8 VDuG](https://www.gesetze-im-internet.de/vdug/__8.html)** — **Sperrwirkung**: Ab **Anhängigkeit** einer Verbandsklage kann gegen denselben Unternehmer keine weitere Verbandsklage erhoben werden, die denselben Lebenssachverhalt und dieselben Ansprüche oder Feststellungsziele betrifft. Die Sperre **entfällt**, sobald die Verbandsklage **ohne Entscheidung in der Sache** endet.
- **[§ 13 VDuG](https://www.gesetze-im-internet.de/vdug/__13.html)** — Im Übrigen gilt die ZPO ergänzend.

### 7. Vergleich ([§ 9](https://www.gesetze-im-internet.de/vdug/__9.html), [§ 10 VDuG](https://www.gesetze-im-internet.de/vdug/__10.html))

Der gerichtliche Vergleich bedarf der **Genehmigung durch das Gericht**; angemeldete Verbraucher können nach § 10 aus dem Vergleich **austreten**. Die Austrittsquote ist für die Vergleichsplanung des Unternehmens die zentrale Kennzahl und in jeder Vergleichsempfehlung zu adressieren.

## Deterministische Berechnung

Zu rechnen sind die Fristen des Verfahrens und die Zehn-Prozent-Schwelle der Drittfinanzierung. Der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) macht nur die Arithmetik:

```bash
# Anmeldefrist § 46 Abs. 1 VDuG: 3 Wochen nach Schluss der mündlichen Verhandlung
# (§ 193 BGB ist ausdrücklich NICHT anwendbar - kein Aufschub auf den nächsten Werktag)
python -m scripts.legal_calc.cli frist --ereignis 14.03.2026 --menge 3 --einheit wochen --land BY --kein-rollover

# Gerichtskosten Musterfeststellungsklage: Streitwert nach § 48 Abs. 1 S. 2 GKG höchstens
# 250.000 EUR - ein höheres Forderungsvolumen (z.B. 2,5 Mio. EUR) wird gekappt;
# Gebührensatz 4,0 nach KV GKG Nr. 1212 (erster Rechtszug vor dem OLG)
python -m scripts.legal_calc.cli gkg --wert 250000 --faktor 4.0

# Gerichtskosten Abhilfeklage: Streitwert nach § 48 Abs. 1 S. 3 GKG höchstens
# 300.000 EUR - ein höheres Forderungsvolumen (z.B. 2,5 Mio. EUR) wird gekappt;
# Gebührensatz 4,0 nach KV GKG Nr. 1212
python -m scripts.legal_calc.cli gkg --wert 300000 --faktor 4.0
```

Ob eine Erfolgsbeteiligung „mehr als 10 Prozent" iSd § 4 Abs. 2 Nr. 3 VDuG ausmacht, ist auf die konkrete Vereinbarung zu rechnen und zu belegen.

## Quellen

### Statute

- [§ 1](https://www.gesetze-im-internet.de/vdug/__1.html), [§ 2](https://www.gesetze-im-internet.de/vdug/__2.html), [§ 3](https://www.gesetze-im-internet.de/vdug/__3.html), [§ 4 VDuG](https://www.gesetze-im-internet.de/vdug/__4.html), [§ 5](https://www.gesetze-im-internet.de/vdug/__5.html), [§ 6](https://www.gesetze-im-internet.de/vdug/__6.html), [§ 7](https://www.gesetze-im-internet.de/vdug/__7.html), [§ 8](https://www.gesetze-im-internet.de/vdug/__8.html), [§ 9](https://www.gesetze-im-internet.de/vdug/__9.html), [§ 10](https://www.gesetze-im-internet.de/vdug/__10.html), [§ 11](https://www.gesetze-im-internet.de/vdug/__11.html), [§ 13](https://www.gesetze-im-internet.de/vdug/__13.html), [§ 46 VDuG](https://www.gesetze-im-internet.de/vdug/__46.html)
- [§ 4 UKlaG](https://www.gesetze-im-internet.de/uklag/__4.html), [§ 13 BGB](https://www.gesetze-im-internet.de/bgb/__13.html), [§ 193 BGB](https://www.gesetze-im-internet.de/bgb/__193.html)
- Richtlinie (EU) 2020/1828 über Verbandsklagen — [EUR-Lex](https://eur-lex.europa.eu/eli/dir/2020/1828/oj)
- [KapMuG](https://www.gesetze-im-internet.de/kapmug_2012/); Brüssel-Ia-VO (EU) 1215/2012

### Kommentare und Literatur

- Röthemeyer, VDuG, Kommentar, §§ 1–8.
- Nordholtz/Mekat, Musterfeststellungsklage und Verbandsklage, Praxishandbuch.
- Meller-Hannich, Verbandsklagen und kollektiver Rechtsschutz, Beiträge in NJW/ZIP 2024–2026 (Fundstelle vor Verwendung prüfen) `[unverifiziert – prüfen]`
- Musielak/Voit und Zöller, ZPO (ergänzende Anwendung nach § 13 VDuG).

### Rechtsprechung

Das VDuG ist seit dem 13.10.2023 in Kraft; eine gefestigte höchstrichterliche Rechtsprechung existiert **noch nicht**. Erste obergerichtliche Entscheidungen zu Zulässigkeit und Reichweite ergehen seit 2025/2026 — unter anderem zur Verbandsklage wegen Datenschutzverstößen. Jede konkrete Entscheidung ist vor Verwendung in juris, Beck-Online oder über das Verbandsklageregister des Bundesamts für Justiz zu verifizieren; ohne Beleg gilt sie als `[unverifiziert – prüfen]`.

## Ausgabeformat

```
VERBANDSKLAGE — ZULÄSSIGKEIT — <Mandat> — <Datum>

I.   Klageart und Anwendungsbereich
     Klageart:                [Abhilfeklage § 14 / Musterfeststellungsklage § 41]
     Betroffene:              <Verbraucher / auch kleine Unternehmen § 1 Abs. 2>
     KapMuG parallel:         [ja — unschädlich § 1 Abs. 3 / nein]

II.  Klageberechtigung § 2
     Stelle:                  <…>
     UKlaG-Liste § 4:         [eingetragen / nicht eingetragen]
     5-%-Grenze Abs. 1 Nr. 1 lit. b: [eingehalten / zweifelhaft — Offenlegung nach Abs. 2 verlangen]
     Vermutung Abs. 3:        [greift — Rüge aussichtslos / greift nicht]

III. Zuständigkeit § 3
     Allgemeiner Gerichtsstand des Unternehmers: <Ort>
     Zuständiges OLG:         <…>   Landeskonzentration Abs. 3: [geprüft]

IV.  Quorum § 4 Abs. 1
     Dargelegte Betroffene:   <Zahl>   Schwelle 50: [erreicht / nicht erreicht]
     Darlegung nachvollziehbar: [ja / nein — Rüge]

V.   Finanzierung § 4 Abs. 2, 3
     Offenlegung mit Klageeinreichung: [erfolgt / fehlt — Rüge]
     Drittfinanzierer:        <…>
     Nr. 1 Wettbewerber:      [ja / nein]     Nr. 2 Abhängigkeit: [ja / nein]
     Nr. 3 Anteil > 10 %:     <Prozentsatz>   Nr. 4 Einflussnahme: [zu erwarten / nein]
     Ergebnis:                [zulässig / unzulässig]

VI.  Sperrwirkung § 8
     Frühere Verbandsklage:   [anhängig seit <Datum> — gesperrt / keine]
     Entfallen der Sperre:    [Beendigung ohne Sachentscheidung / nein]

VII. Beweismittel und Vergleich
     § 6 Offenlegungsantrag:  <konkret bezeichnete Beweismittel>
     Vergleichsstrategie §§ 9, 10: <Austrittsrisiko>

VIII.Ergebnis und Empfehlung
IX.  Risiko: 🟢 / 🟡 / 🔴 <Begründung>
X.   Quellenverzeichnis
```

## Risiken / typische Fehler

- **Landgericht angerufen.** § 3 Abs. 1 VDuG begründet die **ausschließliche** Zuständigkeit des Oberlandesgerichts; eine Landeskonzentration nach Abs. 3 ist zusätzlich zu prüfen.
- **Finanzierungsrüge nicht erhoben.** § 4 Abs. 2 VDuG macht die Klage bei verbotener Drittfinanzierung **unzulässig**; die Offenlegungspflicht des Abs. 3 gilt auch für später hinzutretende Finanzierung.
- **Fünf-Prozent-Rüge gegen eine Verbraucherzentrale gerichtet.** § 2 Abs. 3 VDuG stellt eine **unwiderlegliche** Vermutung auf.
- **Quorum als Beweisfrage behandelt.** § 4 Abs. 1 VDuG verlangt nachvollziehbare **Darlegung**, dass mindestens 50 Verbraucher betroffen sein **können**.
- **Kleine Unternehmen übersehen.** § 1 Abs. 2 VDuG stellt sie Verbrauchern gleich und erweitert damit Quorum und Anmeldungskreis.
- **Sperrwirkung mit Rechtshängigkeit verwechselt.** § 8 VDuG knüpft an die **Anhängigkeit** an.
- **§ 6 VDuG als Discovery ausgelegt.** Die Offenlegung setzt einen konkret bezeichneten Beweismittelantrag voraus; US-Discovery bleibt unzulässig.
- **KapMuG-Verfahren als Sperre behandelt** — § 1 Abs. 3 VDuG sagt das Gegenteil.
- **Rechtsprechung erfunden.** Das VDuG ist jung; jede Entscheidung ist zu belegen oder als `[unverifiziert – prüfen]` zu kennzeichnen.
