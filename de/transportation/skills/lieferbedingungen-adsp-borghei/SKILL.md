---
name: lieferbedingungen-adsp-borghei
title: /transportrecht:lieferbedingungen-adsp
description: Prüfung von Einbeziehung und Inhalt der Allgemeinen Deutschen Spediteurbedingungen (ADSp 2017) – Geltungsbereich Ziff. 2, Beauftragung Ziff. 6, Pfandrecht Ziff. 19, Haftungsbegrenzung Ziff. 23, Lagerhaltung Ziff. 24, Aufrechnungsverbot Ziff. 27. AGB-Kontrolle §§ 305 ff. BGB und § 449 HGB. Use when ein Speditionsvertrag oder Lagervertrag ADSp 2017 in Bezug nimmt und Wirksamkeit/Reichweite zu prüfen sind.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/transportrecht/skills/lieferbedingungen-adsp
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: transportation
language: de
---

# /transportrecht:lieferbedingungen-adsp

## Zweck

Der Skill prüft, ob die Allgemeinen Deutschen Spediteurbedingungen 2017 (ADSp 2017) in einen konkreten Speditions- oder Lagervertrag **wirksam einbezogen** wurden, ob ihre Klauseln der **Inhaltskontrolle** der §§ 305 ff. BGB sowie der spezialgesetzlichen Schranke des § 449 HGB standhalten, und welche Reichweite die einschlägigen Klauseln – insbesondere Haftungsbegrenzung (Ziff. 23), Lagerhaltung (Ziff. 24), Pfandrecht (Ziff. 19) und Aufrechnungsverbot (Ziff. 27) – im Streitfall haben.

Die ADSp 2017 sind **AGB der Spediteurseite** (gemeinsam empfohlen vom Bundesverband Spedition und Logistik DSLV mit Verbänden der verladenden Wirtschaft – BDI, BGA, DIHK, HDE) und **kein Gesetz**. Sie gelten nur, soweit vertraglich einbezogen.

## Eingaben

- Vertragstyp (Speditionsvertrag § 453 HGB; Lagervertrag § 467 HGB; Frachtvertrag mit Selbsteintritt § 458 HGB)
- Position des Mandanten (Spediteur, Versender/Auftraggeber, Empfänger, Versicherer)
- B2B oder B2C?
- Form und Zeitpunkt der ADSp-Bezugnahme (Auftragsbestätigung, Vertragsformular, Rahmenvertrag, kaufmännisches Bestätigungsschreiben, AGB-Aushang, E-Mail-Footer-Verweis)
- Konkrete Streitklausel (Ziff. 23 Haftung / Ziff. 24 Lager / Ziff. 19 Pfandrecht / Ziff. 27 Aufrechnungsverbot / sonst)
- Streitwert, Bruttogewicht der Sendung, Versicherung Spediteur, Vorhandensein abweichender Individualabreden (Ziff. 2.2 ADSp – Vorrang)

## Sub-Agent-Architektur

Researcher liefert ADSp-Volltext, BGB-Statute zur AGB-Kontrolle, § 449 HGB und Rechtsprechung zur ADSp-Inhaltskontrolle (BGH I. ZS) sowie Kommentar-Belegstellen (Koller, MüKoHGB, Schmidt/Bahnsen "ADSp 2017"). Drafter prüft im Gutachtenstil Einbeziehung → Inhaltskontrolle → Reichweite. Reviewer prüft Einbeziehungsvoraussetzungen (§ 305 II BGB bei Verbraucher / § 449 II HGB bei Unternehmer) und § 307-Vereinbarkeit mit den HGB-Wertungen.

## Ablauf

### 1. Einordnung des Vertrags

- [§ 453 HGB](https://www.gesetze-im-internet.de/hgb/__453.html): Speditionsvertrag – der Spediteur besorgt die Versendung des Gutes.
- [§ 458 HGB](https://www.gesetze-im-internet.de/hgb/__458.html): Selbsteintritt – tritt der Spediteur selbst als Frachtführer auf, gelten §§ 425 ff. HGB.
- [§ 459 HGB](https://www.gesetze-im-internet.de/hgb/__459.html): Fixkostenspedition – Pauschalvergütung, Frachtrecht analog.
- [§ 467 HGB](https://www.gesetze-im-internet.de/hgb/__467.html): Lagervertrag – Lagerung und Aufbewahrung gewerbsmäßig.

Die ADSp 2017 erfassen alle drei Vertragstypen, soweit einbezogen.

### 2. Einbeziehung

#### 2.1 Im B2B (Unternehmer ↔ Unternehmer) – Regelfall der ADSp

[§ 449 HGB](https://www.gesetze-im-internet.de/hgb/__449.html) ist die spezialgesetzliche Schranke für Abweichungen vom HGB-Frachtrecht. Im B2B-Verkehr gelten Erleichterungen gegenüber den allgemeinen AGB-Regeln:

- **Einbeziehung** in einen Vertrag zwischen Unternehmern erfolgt nach allgemeinen Regeln (§§ 145 ff. BGB) – ausdrücklicher Hinweis und Möglichkeit zumutbarer Kenntnisnahme genügen.
- Ein Hinweis "Es gelten die ADSp in ihrer jeweils gültigen Fassung" auf der Auftragsbestätigung des Spediteurs reicht im B2B regelmäßig aus, sofern der andere Teil widerspruchslos bleibt (kaufmännisches Schweigen).
- **§ 305 II BGB findet im B2B keine Anwendung** (§ 310 I 1 BGB) – die formellen Einbeziehungsvoraussetzungen entfallen, materielle Inhaltskontrolle nach § 307 BGB bleibt.

#### 2.2 Im B2C (Unternehmer ↔ Verbraucher)

- § 305 II BGB ist anwendbar: ausdrücklicher Hinweis **und** zumutbare Möglichkeit der Kenntnisnahme zwingend.
- Der bloße Verweis "ADSp in der jeweils gültigen Fassung" ohne Aushändigung des Textes oder Bereitstellung im Netz reicht **nicht**.
- Bei Verbraucherspediteuren sind die strengeren Klauselverbote der §§ 308, 309 BGB anwendbar.

#### 2.3 Sonderfall kaufmännisches Bestätigungsschreiben

Ein einseitiger Verweis auf ADSp im kaufmännischen Bestätigungsschreiben des Spediteurs wird Vertragsinhalt, wenn der Empfänger nicht unverzüglich widerspricht – Grundsatz des kaufmännischen Bestätigungsschreibens, gewohnheitsrechtlich.

### 3. Inhaltskontrolle nach §§ 307 ff. BGB

Auch im B2B-Verkehr ist § 307 BGB anwendbar (§ 310 I 2 BGB – Berücksichtigung der im Handelsverkehr geltenden Gewohnheiten und Gebräuche; eingeschränkte Wirkung der §§ 308, 309 BGB als Indizwirkung).

Maßstab: **Unangemessene Benachteiligung** entgegen den Geboten von Treu und Glauben; insbesondere Abweichungen vom wesentlichen Grundgedanken der gesetzlichen Regelung (§ 307 II Nr. 1 BGB).

#### 3.1 Ziff. 23 ADSp 2017 – Haftungssumme

Kernregelung:

- **Haftung des Spediteurs bei Verlust/Beschädigung auf 8,33 SZR/kg** des Rohgewichts der Sendung begrenzt (Ziff. 23.1.1) – inhaltsgleich mit § 431 HGB / Art. 23 III CMR.
- **Schadensereignis-Pauschalierung**: Haftung je Schadensereignis grundsätzlich auf 1.000.000 EUR oder 2 SZR je kg Rohgewicht der Sendung (das jeweils Höhere), insgesamt aber auf 2.000.000 EUR oder 2 SZR/kg je Schadenereignis begrenzt (Ziff. 23.1.2 ff.) `[unverifiziert – ADSp-Text-Version 2017 prüfen]`.
- **Lagerhaltung**: 35.000 EUR je Schadenfall (Ziff. 23.1.3).
- **Versicherungspflicht** des Spediteurs (Ziff. 28 ADSp): Verkehrshaftungs-Versicherung zur Deckung der ADSp-Haftung.

**§ 307 BGB-Prüfung**: Die Beschränkung auf 8,33 SZR/kg deckt sich mit der gesetzlichen Wertung des § 431 HGB; ihre AGB-rechtliche Wirksamkeit im B2B ist – soweit sie sich an § 431 HGB orientiert – grundsätzlich anerkannt. **Grenze § 435 HGB** / **Art. 29 CMR**: Die ADSp können qualifiziertes Verschulden nicht ausschließen (§ 449 I HGB iVm § 307 BGB; vgl. Ziff. 25 ADSp).

#### 3.2 Ziff. 24 ADSp 2017 – Lagerhaltung

Sonderregeln für den Lagervertrag: Inventur, Ablieferung bei Streitfällen, Eigentumsvorbehalt des Auftraggebers etc.

#### 3.3 Ziff. 19 ADSp 2017 – Pfandrecht und Sicherheiten

Erweiterung des gesetzlichen Pfandrechts (§ 464 HGB für Spediteur, § 475b HGB für Lagerhalter) auf alle Forderungen des Spediteurs aus der Geschäftsverbindung. § 307 BGB-Wertung: erweiterte AGB-Pfandrechte sind im B2B grundsätzlich zulässig, soweit sie nicht über das verkehrsübliche Maß hinausgehen.

#### 3.4 Ziff. 27 ADSp 2017 – Aufrechnungs- und Zurückbehaltungsverbot

Standardklausel: Der Auftraggeber kann mit Gegenforderungen nur aufrechnen, wenn sie **unbestritten** oder **rechtskräftig festgestellt** sind. Zurückbehaltungsrechte sind ausgeschlossen, wenn sie nicht aus demselben Vertragsverhältnis stammen.

**§ 307 BGB-Wertung**:
- B2C: § 309 Nr. 3 BGB – Aufrechnungsverbot nur für unbestrittene oder rechtskräftig festgestellte Gegenforderungen ist zulässig; Klauselverbot greift sonst.
- B2B: Indizwirkung des § 309 Nr. 3 BGB über § 307 BGB; in der Rspr. anerkannt, wenn der zulässige Aufrechnungsumfang (unbestritten / rechtskräftig) gewahrt bleibt – andernfalls unwirksam.

### 4. Vorrang individueller Vereinbarungen (Ziff. 2.2 ADSp)

Ziff. 2.2 ADSp 2017: **Individuell ausgehandelte Abreden gehen vor.** Auch in B2B-Verträgen führt § 305b BGB zum Vorrang der Individualabrede vor AGB.

### 5. Rechtsfolgen unwirksamer ADSp-Klauseln

Bei Unwirksamkeit einzelner Klauseln greifen §§ 306 BGB / § 449 III HGB (Klausel fällt weg, im Übrigen Vertrag wirksam) und an deren Stelle das **dispositive HGB-Recht** (§§ 407 ff., 453 ff., 467 ff.). Eine **geltungserhaltende Reduktion** ist ausgeschlossen.

### 6. Anwendungsmatrix

| Konstellation | Einbeziehung | Inhaltskontrolle |
|---|---|---|
| B2B-Rahmenvertrag mit ADSp-Bezug | § 449 II HGB iVm §§ 145 ff. BGB | § 307 BGB |
| B2B-Einzelauftrag, Verweis in Auftragsbestätigung | wirksam bei widerspruchslosem Handeln | § 307 BGB |
| B2C – Endkunden-Umzug, Pakettransport | § 305 II BGB – Hinweis + Kenntnisnahme | §§ 307, 308, 309 BGB |
| Internationaler Transport unter CMR | ADSp anwendbar nur, soweit CMR es zulässt (Art. 41 CMR – zwingend) | CMR-Vorrang |

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute

- [§ 305 BGB](https://www.gesetze-im-internet.de/bgb/__305.html) (Einbeziehung von AGB)
- [§ 305b BGB](https://www.gesetze-im-internet.de/bgb/__305b.html) (Vorrang Individualabrede)
- [§ 307 BGB](https://www.gesetze-im-internet.de/bgb/__307.html) (Inhaltskontrolle)
- [§ 308 BGB](https://www.gesetze-im-internet.de/bgb/__308.html) (Klauselverbote mit Wertungsmöglichkeit)
- [§ 309 BGB](https://www.gesetze-im-internet.de/bgb/__309.html) (Klauselverbote ohne Wertungsmöglichkeit, insb. Nr. 3 Aufrechnung)
- [§ 310 BGB](https://www.gesetze-im-internet.de/bgb/__310.html) (Anwendungsbereich; B2B-Modifikationen)
- [§ 449 HGB](https://www.gesetze-im-internet.de/hgb/__449.html) (Abweichende Vereinbarungen Frachtrecht)
- [§ 466 HGB](https://www.gesetze-im-internet.de/hgb/__466.html) (Abweichende Vereinbarungen Speditionsrecht)
- [§§ 453, 458, 459, 461 HGB](https://www.gesetze-im-internet.de/hgb/__453.html) (Speditionsvertrag)
- [§ 467 HGB](https://www.gesetze-im-internet.de/hgb/__467.html) (Lagervertrag)
- ADSp 2017 – Volltext (DSLV): https://www.dslv.org/dslv/web.nsf/id/li_adsp2017.html `[unverifiziert – Aktualität prüfen]`

### Kommentare

- Koller, Transportrecht, 10. Aufl. 2020, ADSp Vor Ziff. 1 ff.; Ziff. 23 Rn. 1 ff.; Ziff. 27 Rn. 1 ff. `[unverifiziert – Auflagenstand prüfen]`
- Schmidt/Bahnsen, ADSp 2017 – Kommentar, jüngste Auflage `[unverifiziert]`
- Bydlinski, in: MüKoHGB, 4. Aufl. 2020, § 449 HGB Rn. 1 ff. `[unverifiziert]`
- Basedow, in: MüKoBGB, 9. Aufl. 2022, § 310 Rn. 1 ff. (B2B-AGB-Kontrolle) `[unverifiziert]`

### Rechtsprechung (`[unverifiziert – prüfen in juris/TranspR]`)

1. BGH, Urt. v. 13.07.2006 – I ZR 245/03, TranspR 2006, 448 (ADSp – Einbeziehung im B2B durch widerspruchsloses Handeln)
2. BGH, Urt. v. 06.05.2010 – I ZR 31/08, TranspR 2010, 387 (Ziff. 23 ADSp – Schadensereignis-Begrenzung, Wirksamkeit im B2B)
3. BGH, Urt. v. 26.10.2017 – I ZR 178/16, TranspR 2018, 73 (Aufrechnungsverbot Ziff. 27 ADSp und § 307 BGB)
4. OLG Hamburg, Urt. v. 24.11.2011 – 6 U 12/11, TranspR 2012, 159 (Ziff. 19 ADSp – Pfandrechtserweiterung)

## Ausgabeformat

```
GUTACHTEN – Einbeziehung und Inhalt der ADSp 2017
Vertrag: <Speditions- / Lager- / Frachtvertrag mit Selbsteintritt>
Parteien: <Auftraggeber> ↔ <Spediteur> (<B2B / B2C>)
Streitklausel: <Ziff. 23 / 24 / 19 / 27 ADSp>
Streitwert / Schaden: <EUR>; Bruttogewicht <kg>

I. Sachverhalt
II. Frage(n)
III. Kurzantwort
     – Einbeziehung ADSp 2017: [ja / nein] – Begründung
     – Inhaltskontrolle Streitklausel § 307 BGB: [wirksam / unwirksam]
     – Reichweite im konkreten Fall: <Höchstbetrag / Aufrechnung / Pfandrecht>
     – Empfehlung: <…>

IV. Rechtliche Bewertung
    1. Vertragstyp und Anwendbarkeit ADSp
    2. Einbeziehung
       a) B2B-Maßstab § 449 II HGB / §§ 145 ff. BGB
       b) (oder) B2C-Maßstab § 305 II BGB
       c) Vorrang Individualabrede (§ 305b BGB, Ziff. 2.2 ADSp)
    3. Inhaltskontrolle § 307 BGB
       a) Ziff. 23 (Haftungssumme)
       b) Ziff. 27 (Aufrechnungsverbot) – § 309 Nr. 3 BGB-Indizwirkung
       c) ggf. weitere Klauseln
    4. Grenze § 435 HGB / Art. 29 CMR – qualifiziertes Verschulden bleibt
    5. Rechtsfolge bei Unwirksamkeit – Rückfall auf §§ 407 ff., 453 ff., 467 ff. HGB

V. Gesamtergebnis

VI. Risiken / offene Punkte
    🟢 / 🟡 / 🔴 <Einstufung mit Begründung>
    – Offene Tatsachen: Form der ADSp-Bezugnahme, Empfang durch Auftraggeber,
      Vorhandensein abweichender Individualabreden, Versicherungsdeckung

VII. Quellenverzeichnis
     – Statute (gesetze-im-internet.de)
     – ADSp-Volltext (DSLV)
     – Rspr. (BGH I ZR …, OLG …) [unverifiziert – prüfen]
     – Kommentare (Koller, Schmidt/Bahnsen, MüKoHGB)
```

## Beispiel (Auszug, Gutachtenstil)

> "Der Speditionsauftrag zwischen V (Versender, Maschinenbauunternehmen) und S (Spediteur) ist als B2B-Vertrag nach § 453 HGB zu qualifizieren. Auf die Einbeziehung der ADSp 2017 findet § 449 II HGB iVm §§ 145 ff. BGB Anwendung; § 305 II BGB ist gemäß § 310 I 1 BGB nicht einschlägig.
>
> Die E-Mail-Bestätigung des S enthält den Hinweis 'Es gelten die ADSp in ihrer jeweils gültigen Fassung'. Im B2B-Verkehr genügt ein solcher Hinweis nach h.M. zur Einbeziehung, sofern V als Kaufmann nicht widersprochen hat – BGH (I. ZS), Urt. v. 13.07.2006 – [I ZR 245/03](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=13.07.2006&Aktenzeichen=I%20ZR%20245/03). Eine Aushändigung des ADSp-Textes ist nicht erforderlich, da V als Unternehmer den Inhalt der ADSp zumutbar selbst zur Kenntnis nehmen kann.
>
> Ziff. 23.1.1 ADSp 2017 begrenzt die Haftung auf 8,33 SZR/kg Rohgewicht. Diese Wertung entspricht § 431 I HGB und ist im B2B nach § 307 BGB nicht zu beanstanden. Bei einem Maschinen-Bruttogewicht von 2.100 kg ergibt sich ein Höchstbetrag von **17.493 SZR**, umzurechnen mit dem SZR/EUR-Tageskurs am Tag der Regulierung (IWF, https://www.imf.org/external/np/fin/data/rms_five.aspx, Stand <Datum>) `[unverifiziert – Tageskurs prüfen]`.
>
> Eine Durchbrechung der Begrenzung nach § 435 HGB iVm Ziff. 25 ADSp 2017 setzt qualifiziertes Verschulden voraus; § 449 I HGB schließt eine AGB-rechtliche Ausweitung der Begrenzung auf den qualifizierten Fall aus.
>
> Das in Ziff. 27 ADSp normierte Aufrechnungsverbot ist – beschränkt auf nicht rechtskräftig festgestellte oder bestrittene Forderungen – nach BGH-Linie auch im B2B wirksam (vgl. BGH, Urt. v. 26.10.2017 – I ZR 178/16 `[unverifiziert]`). Eine Aufrechnung des V mit der streitigen Schadensersatzforderung gegen die Frachtforderung des S ist daher ausgeschlossen, solange die Forderung weder unbestritten noch rechtskräftig festgestellt ist. ..."

## Risiken / typische Fehler

- **§ 305 II BGB im B2B angewandt** – § 310 I 1 BGB übersehen.
- **Ziff. 23 ADSp pauschal als wirksam abgenickt**, ohne die Schadensereignis-Pauschalierung und die § 435 HGB-Grenze einzeln zu prüfen.
- **Ziff. 27 ADSp als generelles Aufrechnungsverbot verstanden** – § 309 Nr. 3 BGB-Indizwirkung verkannt; Grenze unbestritten/rechtskräftig zwingend.
- **CMR-Vorrang übersehen** bei grenzüberschreitenden Transporten – Art. 41 CMR macht abweichende ADSp-Klauseln zulasten der Berechtigten nichtig.
- **Vorrang Individualabrede Ziff. 2.2 ADSp / § 305b BGB übersehen**.
- **Geltungserhaltende Reduktion versucht** – ausgeschlossen; Rückfall auf dispositives HGB-Recht.
- **ADSp als "Gesetz" oder "DIN-Norm" bezeichnet** – sie sind privatrechtlich-vereinbarte AGB.
