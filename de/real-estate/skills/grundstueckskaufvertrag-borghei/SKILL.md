---
name: grundstueckskaufvertrag-borghei
title: /immobilien-grundbuchrecht:grundstueckskaufvertrag
description: Gestaltung und Prüfung des Grundstückskaufvertrags – Beurkundungszwang § 311b Abs. 1 BGB und Vollständigkeitsgrundsatz, Belehrungs- und Vorlesepflicht § 17 BeurkG nebst Zwei-Wochen-Frist § 17 Abs. 2a BeurkG, Auflassung § 925 BGB und Auflassungsvormerkung §§ 883, 885 BGB, Fälligkeitsvoraussetzungen der Kaufpreiszahlung, Lastenfreistellung und Belastungsvollmacht, Gefahr-, Nutzen- und Lastenwechsel §§ 446, 103 BGB, Sachmängelhaftung §§ 434, 442, 444 BGB und die Grenzen des Ausschlusses 'gekauft wie besichtigt'. Use when ein Grundstücks- oder Wohnungskaufvertrag entworfen, ein Notarentwurf für Käufer oder Verkäufer geprüft oder eine gescheiterte Abwicklung aufgearbeitet wird.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/immobilien-grundbuchrecht/skills/grundstueckskaufvertrag
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: real-estate
language: de
---

# /immobilien-grundbuchrecht:grundstueckskaufvertrag

## Zweck

Der Grundstückskaufvertrag ist die formstrengste Alltagsurkunde des deutschen Zivilrechts: Ohne notarielle Beurkundung ist er nichtig, und jede nicht mitbeurkundete Nebenabrede zieht den gesamten Vertrag in die Nichtigkeit. Zugleich ist er ein Zahlungs- und Sicherungsmechanismus — der Käufer soll erst zahlen, wenn er das Eigentum sicher erhält, der Verkäufer soll erst übereignen, wenn er das Geld sicher hat. Dieser Skill entwirft und prüft den Vertrag entlang beider Achsen: Wirksamkeit (Form, Belehrung, Bestimmtheit) und Abwicklungssicherheit (Vormerkung, Fälligkeit, Lastenfreistellung).

## Eingaben

- **Perspektive**: Verkäufer-Entwurf / Käufer-Prüfung eines Notarentwurfs / Aufarbeitung einer gestörten Abwicklung
- **Kaufgegenstand**: Grundbuchblatt, Gemarkung, Flur, Flurstück, Größe; bei Wohnungseigentum Miteigentumsanteil und Sondereigentumseinheit
- **Kaufpreis**, Aufteilung auf Grundstück / Gebäude / mitverkauftes Inventar, Finanzierung des Käufers
- **Grundbuchstand** in Abteilung I, II und III (Belastungen, Rechte, Grundschulden)
- Beteiligte: natürliche Personen, Gesellschaften (bei GbR: **Eintragung im Gesellschaftsregister**), Erbengemeinschaft, Betreute, Minderjährige
- **Vorkaufsrechte**, Genehmigungserfordernisse (Grundstücksverkehrsgesetz, Sanierungsrecht, Umlegung, WEG-Verwalterzustimmung)
- Bekannte **Mängel**, durchgeführte Untersuchungen, Zusagen im Exposé oder in der Besichtigung
- Ist der Käufer **Verbraucher** und der Verkäufer Unternehmer (§ 17 Abs. 2a S. 2 Nr. 2 BeurkG)?

## Sub-Agent-Architektur

1. **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) beschafft BGB-, BeurkG- und GBO-Normen mit URL, die Kommentarstellen (Grüneberg, MüKoBGB, Winkler BeurkG) und die BGH-Linien zu Arglist und Beschaffenheitsvereinbarung.
2. **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) erstellt Vertragsentwurf oder Prüfvermerk mit Fälligkeitskaskade und Fristenplan.
3. **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft Beurkundungsvollständigkeit, Vormerkungsschutz, Lastenfreistellung und Belehrungsdokumentation.

## Ablauf

### 1. Beurkundungszwang und Vollständigkeitsgrundsatz ([§ 311b Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__311b.html))

Ein Vertrag, durch den sich ein Teil verpflichtet, das Eigentum an einem Grundstück zu übertragen oder zu erwerben, bedarf der **notariellen Beurkundung**. Erfasst ist die **gesamte Vereinbarung**: Alles, was nach dem Willen der Parteien Teil des Geschäfts sein soll, muss in die Urkunde — Maklerabreden, Inventarlisten, Renovierungszusagen, Rückkaufsrechte, Zahlungsmodalitäten. Eine ausgelagerte Nebenabrede macht **den ganzen Vertrag** formnichtig (§ 125 BGB), nicht nur die Abrede.

Praxisfalle **Kaufpreisunterverbriefung**: Wird ein niedrigerer als der tatsächlich gewollte Kaufpreis beurkundet, ist der beurkundete Vertrag als Scheingeschäft nichtig (§ 117 Abs. 1 BGB) und der wirklich gewollte formnichtig. Heilung tritt erst mit **Auflassung und Eintragung** ein (§ 311b Abs. 1 S. 2 BGB) — bis dahin trägt jede Seite das volle Rückabwicklungsrisiko.

### 2. Belehrungspflicht und Zwei-Wochen-Frist ([§ 17 BeurkG](https://www.gesetze-im-internet.de/beurkg/__17.html))

Der Notar hat den Willen der Beteiligten zu erforschen, den Sachverhalt zu klären, über die **rechtliche Tragweite** zu belehren und die Erklärungen klar und unzweideutig wiederzugeben; Zweifel und Belehrungen sind in der Urkunde zu vermerken. Bei Verbraucherverträgen soll der Beteiligte, der Verbraucher ist, den Entwurf **zwei Wochen vor der Beurkundung** erhalten (§ 17 Abs. 2a S. 2 Nr. 2 BeurkG). Die Frist ist eine Soll-Vorschrift: Ihre Verletzung macht den Vertrag **nicht unwirksam**, kann aber Amtshaftung und Schadensersatz auslösen und ist im Streit über Übereilungsschutz ein starkes Argument. Der Notar ist **unparteiisch** — er vertritt keine Seite; die Interessenwahrnehmung des Käufers oder Verkäufers ist Anwaltsaufgabe.

### 3. Auflassung ([§ 925 BGB](https://www.gesetze-im-internet.de/bgb/__925.html))

Die Auflassung ist die dingliche Einigung über den Eigentumsübergang; sie muss bei **gleichzeitiger Anwesenheit beider Teile** vor dem Notar erklärt werden und ist **bedingungs- und befristungsfeindlich** (§ 925 Abs. 2 BGB). Deshalb wird sie in der Praxis zwar mitbeurkundet, aber der Notar wird angewiesen, den **Eintragungsantrag erst nach Kaufpreiszahlung** zu stellen. Diese Notaranweisung — nicht eine Bedingung der Auflassung — ist der eigentliche Sicherungsmechanismus zugunsten des Verkäufers. Der Eigentumsübergang tritt erst mit **Einigung und Eintragung** ein ([§ 873 BGB](https://www.gesetze-im-internet.de/bgb/__873.html)).

### 4. Auflassungsvormerkung ([§ 883 BGB](https://www.gesetze-im-internet.de/bgb/__883.html), [§ 885 BGB](https://www.gesetze-im-internet.de/bgb/__885.html))

Die Vormerkung sichert den schuldrechtlichen Übereignungsanspruch des Käufers dinglich: Spätere Verfügungen des Verkäufers sind dem Vormerkungsberechtigten gegenüber **relativ unwirksam** (§ 883 Abs. 2 BGB), und der Rang des künftigen Rechts richtet sich nach der Vormerkung (§ 883 Abs. 3 BGB). Sie wird auf **Bewilligung** des Verkäufers oder aufgrund einstweiliger Verfügung eingetragen (§ 885 Abs. 1 BGB). Praktisch gilt: **Kein Kaufpreis ohne eingetragene Vormerkung.** Die Vormerkung schützt den Käufer auch in der Insolvenz des Verkäufers und gegen Zwischenverfügungen sowie Zwangsversteigerungsvermerke.

### 5. Fälligkeitsvoraussetzungen der Kaufpreiszahlung

Der Kaufpreis wird nicht mit Vertragsschluss fällig, sondern erst, wenn der Notar dem Käufer die **Fälligkeitsmitteilung** erteilt. Die Kaskade lautet:

1. **Auflassungsvormerkung** rangrichtig eingetragen (nur mit im Vertrag zugelassenen Vorbelastungen),
2. **Lastenfreistellungsunterlagen** der abzulösenden Gläubiger liegen dem Notar vor,
3. erforderliche **Genehmigungen und Zeugnisse** liegen vor (Verwalterzustimmung, Vorkaufsrechtsverzicht der Gemeinde nach § 28 BauGB, betreuungs- oder familiengerichtliche Genehmigung),
4. keine sonstigen Eintragungshindernisse.

Fehlt eine Stufe, ist der Kaufpreis **nicht fällig**; eine gleichwohl erklärte Mahnung setzt keinen Verzug in Gang.

### 6. Lastenfreistellung und Belastungsvollmacht

**Lastenfreistellung:** In Abteilung III eingetragene Grundschulden des Verkäufers werden aus dem Kaufpreis abgelöst. Der Notar holt die **Löschungsbewilligung** unter Treuhandauflage ein und zahlt den Ablösebetrag direkt an die Gläubigerbank; nur der Restbetrag geht an den Verkäufer. Nicht valutierende Grundschulden sind gesondert zu behandeln — der Verkäufer hat einen Rückgewähranspruch.

**Belastungsvollmacht:** Der Käufer braucht das Grundstück als Kreditsicherheit, bevor er Eigentümer ist. Der Verkäufer bevollmächtigt ihn daher, das Grundstück schon vor Eigentumsumschreibung mit Grundpfandrechten zu belasten — begrenzt auf die Kaufpreisfinanzierung, mit **Zweckerklärung zugunsten des Verkäufers** (Sicherung nur des Kaufpreisteils) und der Auflage, die Valuta ausschließlich auf das Notaranderkonto oder direkt an den Verkäufer zu leiten. Eine Belastungsvollmacht ohne diese Zweckbindung ist ein schwerer Gestaltungsfehler. Vertiefung: `/immobilien-grundbuchrecht:grundschuld-sicherungsrecht`.

### 7. Gefahr-, Nutzen- und Lastenwechsel ([§ 446 BGB](https://www.gesetze-im-internet.de/bgb/__446.html))

Mit der **Übergabe** geht die Gefahr des zufälligen Untergangs und der zufälligen Verschlechterung auf den Käufer über; von der Übergabe an gebühren ihm die Nutzungen und trägt er die Lasten ([§ 103 BGB](https://www.gesetze-im-internet.de/bgb/__103.html)). In der Praxis wird der Besitzübergang vertraglich auf den Tag der **vollständigen Kaufpreiszahlung** gelegt und dort zugleich der Übergang von Nutzungen, Lasten, Verkehrssicherungspflicht und Versicherungen geregelt. Bei vermieteten Objekten gilt zusätzlich **Kauf bricht nicht Miete** ([§ 566 BGB](https://www.gesetze-im-internet.de/bgb/__566.html)); Mietkautionen und Betriebskostenvorauszahlungen sind gesondert abzurechnen.

### 8. Sachmängelhaftung und der Ausschluss "gekauft wie besichtigt" ([§ 434 BGB](https://www.gesetze-im-internet.de/bgb/__434.html), [§ 444 BGB](https://www.gesetze-im-internet.de/bgb/__444.html))

Der Gewährleistungsausschluss ist beim Gebrauchtimmobilienkauf Standard, aber er hat drei harte Grenzen:

- **Arglist** ([§ 444 BGB](https://www.gesetze-im-internet.de/bgb/__444.html)): Wer einen offenbarungspflichtigen Mangel verschweigt, kann sich auf den Ausschluss nicht berufen. Offenbarungspflichtig sind insbesondere Umstände, die der Käufer bei einer Besichtigung nicht erkennen kann und die für seinen Entschluss erkennbar erheblich sind — fehlende Baugenehmigung, Feuchtigkeitsschäden hinter Verkleidungen, Altlasten, Schwammbefall. Eine **fehlende Baugenehmigung** ist ein Sachmangel; maßgeblich ist die Genehmigungsbedürftigkeit im Zeitpunkt des Gefahrübergangs (BGH, Urt. v. 12.04.2013 – V ZR 266/11 — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2013-04-12&Aktenzeichen=V%20ZR%20266/11). Werden Kellerräume als Wohnraum angepriesen, obwohl die baurechtliche Genehmigung fehlt, liegt eine arglistige Täuschung nach § 123 Abs. 1 BGB vor (BGH, Urt. v. 27.06.2014 – V ZR 55/13 — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2014-06-27&Aktenzeichen=V%20ZR%2055/13).
- **Beschaffenheitsgarantie und Beschaffenheitsvereinbarung**: Eine ausdrücklich zugesagte Eigenschaft ("Dach 2019 neu gedeckt", "Wohnfläche 142 m²") geht dem allgemeinen Ausschluss vor. Formel: Der Ausschluss erfasst nie eine vereinbarte Beschaffenheit.
- **Kenntnis des Käufers** ([§ 442 BGB](https://www.gesetze-im-internet.de/bgb/__442.html)): Bei Kenntnis entfallen die Rechte ohnehin; bei grob fahrlässiger Unkenntnis nur, wenn der Verkäufer nicht arglistig gehandelt oder eine Garantie übernommen hat.

Die Klausel "gekauft wie besichtigt" ist damit **kein Freibrief**: Sie deckt nur das, was bei einer Besichtigung erkennbar war, und niemals arglistig Verschwiegenes.

## Deterministische Berechnung

Der Geschäftswert des Grundstückskaufvertrags ist der Kaufpreis; er steuert Notarkosten (GNotKG), Anwaltsgebühren und im Streitfall die Gerichtskosten. Der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) macht **nur die Arithmetik** — die Bestimmung des Geschäftswerts, die Bewertung mitverkauften Inventars und die Frage, welcher Gebührensatz anfällt, bleiben juristische Eingaben. Ein **GNotKG-Modul ist nicht implementiert**; Notarkosten sind gegen KV GNotKG von Hand zu ermitteln.

```bash
# Anwaltsgebühren für die Begleitung eines Kaufvertrags über 450.000 EUR
python -m scripts.legal_calc.cli rvg --wert 450000 --posten geschaeft

# Gerichtskosten erster Instanz bei Streit über die Kaufpreisrückzahlung
python -m scripts.legal_calc.cli gkg --wert 450000 --faktor 3.0

# Zwei-Wochen-Frist § 17 Abs. 2a BeurkG: Entwurf am 15.01.2026 zugeleitet
python -m scripts.legal_calc.cli frist --ereignis 15.01.2026 --menge 2 --einheit wochen --land BY
```

`--json` liefert die Rechenschritte samt Normzitat. Die RVG-/GKG-Tabellen tragen ein `stand`-Feld; vor Verwendung gegen die aktuelle Anlage 2 prüfen.

## Quellen

### Statute

- [§ 311b BGB](https://www.gesetze-im-internet.de/bgb/__311b.html) (Beurkundungszwang), [§ 125 BGB](https://www.gesetze-im-internet.de/bgb/__125.html), [§ 117 BGB](https://www.gesetze-im-internet.de/bgb/__117.html)
- [§ 873 BGB](https://www.gesetze-im-internet.de/bgb/__873.html), [§ 925 BGB](https://www.gesetze-im-internet.de/bgb/__925.html) (Auflassung), [§ 883 BGB](https://www.gesetze-im-internet.de/bgb/__883.html), [§ 885 BGB](https://www.gesetze-im-internet.de/bgb/__885.html) (Vormerkung)
- [§ 434 BGB](https://www.gesetze-im-internet.de/bgb/__434.html), [§ 442 BGB](https://www.gesetze-im-internet.de/bgb/__442.html), [§ 444 BGB](https://www.gesetze-im-internet.de/bgb/__444.html), [§ 446 BGB](https://www.gesetze-im-internet.de/bgb/__446.html), [§ 103 BGB](https://www.gesetze-im-internet.de/bgb/__103.html), [§ 566 BGB](https://www.gesetze-im-internet.de/bgb/__566.html)
- [§ 17 BeurkG](https://www.gesetze-im-internet.de/beurkg/__17.html) (Belehrungspflicht), [§ 13 GBO](https://www.gesetze-im-internet.de/gbo/__13.html), [§ 19 GBO](https://www.gesetze-im-internet.de/gbo/__19.html)

### Kommentare

- Grüneberg, in: Grüneberg, BGB, 84. Aufl. 2025, § 311b Rn. 1 ff.; § 444 Rn. 1 ff.
- Ruhwinkel, in: MüKoBGB, 9. Aufl. 2023, § 311b Rn. 1 ff.
- Kanzleiter, in: MüKoBGB, 9. Aufl. 2023, § 925 Rn. 1 ff.
- Winkler, BeurkG, 20. Aufl. 2022, § 17 Rn. 1 ff.

### Rechtsprechung

- BGH, Urt. v. 12.04.2013 – V ZR 266/11 (fehlende Baugenehmigung als Sachmangel; Gefahrübergang; arglistiges Verschweigen) — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2013-04-12&Aktenzeichen=V%20ZR%20266/11
- BGH, Urt. v. 27.06.2014 – V ZR 55/13 (Anfechtung wegen arglistiger Täuschung; Anpreisung von Kellerräumen als Wohnraum ohne Genehmigung; Beweislast) — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2014-06-27&Aktenzeichen=V%20ZR%2055/13
- Zum Vollständigkeitsgrundsatz des § 311b Abs. 1 BGB und zur Formnichtigkeit ausgelagerter Nebenabreden ist die einschlägige BGH-Rechtsprechung heranzuziehen `[unverifiziert - prüfen]`. Kein Aktenzeichen ohne eigene Verifikation in juris / Beck-Online übernehmen.

## Formulierungshilfe — Auflassungsvormerkung, Fälligkeit, Gewährleistung

```
§ __ Auflassungsvormerkung
Zur Sicherung des Anspruchs des Käufers auf Übertragung des Eigentums
bewilligt der Verkäufer und beantragen die Beteiligten die Eintragung einer
Auflassungsvormerkung gemäß § 883 BGB zugunsten des Käufers im Grundbuch
von <Gemarkung>, Blatt <Nr.>, Abteilung II, im Rang nach den in dieser
Urkunde ausdrücklich zugelassenen Belastungen und im Übrigen an erster
Rangstelle. Der Notar wird angewiesen, die Löschung der Vormerkung zu
beantragen, sobald der Käufer als Eigentümer eingetragen ist.

§ __ Fälligkeit des Kaufpreises
Der Kaufpreis ist binnen zehn Tagen nach Zugang der Mitteilung des Notars
fällig, dass
  a) die Auflassungsvormerkung rangrichtig eingetragen ist,
  b) die Unterlagen zur Lastenfreistellung der nicht übernommenen Rechte
     in Abteilung II und III beim Notar vorliegen,
  c) etwa erforderliche Genehmigungen und Vorkaufsrechtszeugnisse
     (§ 28 BauGB, Verwalterzustimmung) vorliegen,
  d) keine sonstigen Eintragungshindernisse bestehen.

§ __ Auflassung und Anweisung an den Notar
Die Beteiligten sind sich über den Eigentumsübergang einig (Auflassung) und
bewilligen und beantragen die Eintragung des Käufers als Eigentümer. Der
Notar wird angewiesen, von der Auflassung erst Gebrauch zu machen und den
Eintragungsantrag erst zu stellen, wenn der Verkäufer den vollständigen
Kaufpreiseingang bestätigt hat oder der Käufer die Zahlung nachweist.

§ __ Sachmängel
Der Kaufgegenstand wird verkauft, wie er steht und liegt; Ansprüche und
Rechte des Käufers wegen Sachmängeln sind ausgeschlossen. Der Ausschluss
gilt nicht für Arglist (§ 444 BGB), für Schäden aus der Verletzung des
Lebens, des Körpers oder der Gesundheit sowie für die nachstehend
vereinbarte Beschaffenheit: <Aufzählung>. Der Verkäufer erklärt, dass ihm
über die in dieser Urkunde genannten hinaus keine verborgenen Mängel,
Altlasten oder Abweichungen von der Baugenehmigung bekannt sind.
```

## Ausgabeformat

```
GRUNDSTÜCKSKAUFVERTRAG — <Entwurf / Prüfung> — <Mandat-ID> — <Datum>

I.    Perspektive / Kaufgegenstand   <Grundbuch, Gemarkung, Flurstück>
II.   Beurkundungszwang § 311b       [✅ / ❌]
      - Vollständigkeit aller Abreden [✅ / ⚠️ Nebenabrede außerhalb]
      - Kaufpreis vollständig verbrieft [✅ / 🔴 Unterverbriefung]
III.  Belehrung § 17 BeurkG          [✅ / ⚠️]
      - Zwei-Wochen-Frist Abs. 2a    Entwurf am <Datum>, Beurkundung <Datum>
IV.   Auflassung § 925 BGB           [beurkundet / offen]
      - Notaranweisung Kaufpreis     [✅ / ❌]
V.    Auflassungsvormerkung §§ 883, 885  Rang: <…>   [✅ / offen]
VI.   Fälligkeitsvoraussetzungen     a) <…> b) <…> c) <…> d) <…>
VII.  Lastenfreistellung             Abt. II: <…>  Abt. III: <…>
      Belastungsvollmacht            [zweckgebunden ✅ / 🔴 ungebunden]
VIII. Gefahr-/Nutzen-/Lastenwechsel  Stichtag: <Datum>   § 446 BGB
      Mietverhältnisse § 566 BGB     [N/A / Kaution + Betriebskosten]
IX.   Sachmängel                     Ausschluss [✅]  Grenzen: Arglist § 444,
      vereinbarte Beschaffenheit     <Aufzählung>
X.    Geschäftswert / Kosten         <Wert> — RVG/GKG s. Berechnung
XI.   Offene Punkte / Genehmigungen  <…>

Ergebnis: <versandfertig / nachbessern / nicht unterschriftsreif>
Risiko Rückabwicklung: [🟢 / 🟡 / 🔴]
```

## Risiken / typische Fehler

- **Nebenabrede außerhalb der Urkunde** — Maklerabrede, Inventarliste oder Renovierungszusage nicht mitbeurkundet; Folge ist die Nichtigkeit des **gesamten** Vertrags nach § 125 BGB, nicht nur der Abrede.
- **Kaufpreisunterverbriefung** — beurkundeter Vertrag als Scheingeschäft nichtig, gewollter Vertrag formnichtig; Heilung erst mit Auflassung und Eintragung.
- **Kaufpreiszahlung ohne eingetragene Vormerkung** — der Käufer zahlt ungesichert und trägt das volle Insolvenz- und Zwischenverfügungsrisiko des Verkäufers.
- **Belastungsvollmacht ohne Zweckbindung** — der Käufer kann das noch fremde Grundstück über den Kaufpreis hinaus belasten; die Valuta muss zwingend an Notar oder Verkäufer fließen.
- **Auflassung bedingt gestellt** — § 925 Abs. 2 BGB ist bedingungsfeindlich; die Sicherung erfolgt über die Notaranweisung, nicht über eine Bedingung.
- **Gewährleistungsausschluss überschätzt** — "gekauft wie besichtigt" hilft nicht bei Arglist (§ 444 BGB), nicht bei vereinbarter Beschaffenheit und nicht bei fehlender Baugenehmigung.
- **Gefahr- und Lastenwechsel nicht mit der Übergabe synchronisiert** — Versicherungen, Verkehrssicherungspflicht und Betriebskosten laufen auseinander; bei vermieteten Objekten Kaution und Vorauszahlungen vergessen.
- **Genehmigungen übersehen** — Vorkaufsrecht der Gemeinde (§ 28 BauGB), WEG-Verwalterzustimmung, betreuungs- oder familiengerichtliche Genehmigung; ohne sie ist der Kaufpreis nicht fällig.
