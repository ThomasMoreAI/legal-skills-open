---
name: hgb-frachtfuehrerhaftung-borghei
title: /transportrecht:hgb-frachtfuehrerhaftung
description: Prüfung der Frachtführerhaftung nach §§ 425 ff. HGB – Obhutshaftung, Haftungsausschlüsse §§ 426–427, Haftungsbegrenzung § 431 (8,33 SZR/kg), Durchbruch bei qualifiziertem Verschulden § 435, Schadensanzeige § 438 und Verjährung § 439. Use when im innerdeutschen Straßengüterverkehr Verlust, Beschädigung oder Lieferfristüberschreitung eingetreten ist und Haftung sowie Höchstbetrag zu prüfen sind.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/transportrecht/skills/hgb-frachtfuehrerhaftung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: transportation
language: de
---

# /transportrecht:hgb-frachtfuehrerhaftung

## Zweck

Der Skill prüft die Haftung des Frachtführers nach §§ 425 ff. HGB für Verlust, Beschädigung und Lieferfristüberschreitung. Er adressiert die Obhutshaftung, die allgemeinen und besonderen Haftungsausschlüsse, die Haftungsbegrenzung nach § 431 HGB (8,33 Rechnungseinheiten pro Kilogramm Bruttogewicht) und deren Durchbrechung bei qualifiziertem Verschulden (§ 435 HGB). Der Skill stellt zudem die Rechtzeitigkeit der Schadensanzeige (§ 438 HGB) und den Stand der Verjährung (§ 439 HGB) systematisch dar.

## Eingaben

- Beförderungsweg (Versendungs- und Ablieferungsort, innerdeutsch)
- Versender, Frachtführer, Empfänger (Parteienrollen)
- Frachtbriefangaben (sofern vorhanden) und Übergabezeitpunkt
- Gut: Art, Verpackung, Bruttogewicht (kg) je Sendungsposition, Warenwert
- Schadensbild (Verlust ganz/teilweise, Beschädigung, Lieferfristüberschreitung) und Schadensereignis (Datum, Ort, äußere Umstände)
- Zeitpunkt und Form der Schadensanzeige des Empfängers
- Position des Mandanten: Versender, Empfänger, Frachtführer oder Transportversicherer (Regress nach § 86 VVG)

## Sub-Agent-Architektur

Researcher liefert HGB-Statute, BGH-I-ZS- und OLG-Rechtsprechung zu § 425, § 431, § 435 und § 438 sowie Kommentarstellen (Koller, MüKoHGB). Drafter prüft im Gutachtenstil die Anspruchsgrundlage, rechnet den Höchstbetrag nach 8,33 SZR/kg auf Basis des angegebenen Bruttogewichts durch und stellt den Fristenkalender. Reviewer prüft, ob alle Tatfristen § 438 HGB datiert sind, die Verjährung § 439 HGB präzise berechnet ist und der SZR-Tageskurs mit Datum gekennzeichnet wurde.

## Ablauf

### 1. Anwendungsbereich

- [§ 407 HGB](https://www.gesetze-im-internet.de/hgb/__407.html): Frachtvertrag – entgeltliche Beförderung von Gütern zu Lande oder auf Binnengewässern.
- Bei grenzüberschreitendem Straßentransport tritt CMR vorrangig hinzu (Art. 1 CMR) – dann ist Skill `cmr-grenzueberschreitender-transport` einschlägig.
- Spediteurseite mit Selbsteintritt (§ 458 HGB) oder Fixkostenspedition (§ 459 HGB) → Frachtrecht anwendbar.

### 2. Obhutshaftung § 425 HGB

[§ 425 HGB](https://www.gesetze-im-internet.de/hgb/__425.html): Der Frachtführer haftet für Schäden, die durch Verlust oder Beschädigung des Gutes in der Zeit von der Übernahme zur Beförderung bis zur Ablieferung oder durch Überschreitung der Lieferfrist entstehen. Es handelt sich um eine **Obhutshaftung** ohne Verschuldenserfordernis im Tatbestand – der Frachtführer haftet für jeden Schaden im Obhutszeitraum, sofern er nicht einen Befreiungstatbestand führt.

### 3. Allgemeine Haftungsausschlüsse § 426 HGB

[§ 426 HGB](https://www.gesetze-im-internet.de/hgb/__426.html): Befreiung, wenn der Verlust, die Beschädigung oder die Lieferfristüberschreitung auf Umständen beruht, die der Frachtführer auch bei größter Sorgfalt nicht vermeiden und deren Folgen er nicht abwenden konnte. **Beweislast: Frachtführer.** Maßstab ist nicht "höhere Gewalt", sondern unvermeidbares Ereignis – strenger als § 276 BGB.

### 4. Besondere Haftungsausschlüsse § 427 HGB

[§ 427 HGB](https://www.gesetze-im-internet.de/hgb/__427.html) – Privilegierte Risiken (haftungsbefreiend bei Anscheinsbeweis):

1. vereinbarte oder übliche Verwendung offener, nicht mit Decken versehener Fahrzeuge
2. ungenügende Verpackung durch den Absender
3. Behandlung, Verladen oder Entladen durch Absender/Empfänger
4. natürliche Beschaffenheit von Gütern (Bruch, Rost, Schwund)
5. mangelhafte oder fehlende Kennzeichnung
6. Beförderung lebender Tiere
7. besondere Gefahren bei vereinbarter Containertransport-Art (Abs. 2)

Bei Anhaltspunkten für eine dieser Gefahrenquellen wird **vermutet**, dass der Schaden daraus entstanden ist; der Anspruchsteller muss dann den Gegenbeweis führen.

### 5. Haftung für andere Personen § 428 HGB

[§ 428 HGB](https://www.gesetze-im-internet.de/hgb/__428.html): Der Frachtführer haftet für seine Leute und für andere Personen, deren er sich bei der Ausführung der Beförderung bedient (Subunternehmer), wie für eigenes Verschulden. Kein § 831 BGB-Entlastungsbeweis.

### 6. Haftungsumfang § 429 HGB / Schadensermittlung § 430 HGB

[§ 429 HGB](https://www.gesetze-im-internet.de/hgb/__429.html): Wertersatz – der Wert des Gutes am Ort und zur Zeit der Übernahme, in der Regel Marktpreis (Abs. 3). Fracht, Zölle und sonstige Kosten sind zu erstatten, soweit sie durch den Schaden anfallen (§ 432 HGB).

[§ 430 HGB](https://www.gesetze-im-internet.de/hgb/__430.html): Schadensermittlung bei Beschädigung – Differenz zwischen Wert in unbeschädigtem und beschädigtem Zustand.

### 7. Haftungshöchstbetrag § 431 HGB

[§ 431 HGB](https://www.gesetze-im-internet.de/hgb/__431.html): Bei Verlust oder Beschädigung ist die Haftung auf einen Betrag von **8,33 Rechnungseinheiten** für jedes Kilogramm des Rohgewichts der Sendung begrenzt (Abs. 1). Rechnungseinheit ist das **Sonderziehungsrecht (SZR/SDR)** des Internationalen Währungsfonds (Abs. 4).

**Berechnung:**

```
Höchstbetrag (SZR) = 8,33 × Bruttogewicht der verlorenen/beschädigten Sendung (kg)
EUR-Wert           = Höchstbetrag × SZR/EUR-Tageskurs (IWF, Tag der Regulierung)
```

Aktuelle SZR-Kurse: https://www.imf.org/external/np/fin/data/rms_five.aspx – Tageskurs **mit Datum** zitieren `[unverifiziert – Tageskurs prüfen]`.

Bei Lieferfristüberschreitung: Haftung begrenzt auf das Dreifache der Fracht (§ 431 III HGB).

§ 449 HGB: Abweichende Vereinbarungen sind grundsätzlich zulässig, im B2C und teilweise im B2B aber AGB-rechtlich kontrolliert.

### 8. Wegfall der Haftungsbegrenzungen § 435 HGB

[§ 435 HGB](https://www.gesetze-im-internet.de/hgb/__435.html): Die in §§ 431, 433 HGB vorgesehenen Haftungsbefreiungen und -begrenzungen gelten **nicht**, wenn der Schaden auf einer Handlung oder Unterlassung beruht, die der Frachtführer oder eine der in § 428 genannten Personen **vorsätzlich** oder **leichtfertig und in dem Bewusstsein, dass ein Schaden mit Wahrscheinlichkeit eintreten werde**, begangen hat.

Die BGH-Rspr. zu Organisationsverschulden (fehlende Schnittstellenkontrollen, Diebstahlsicherung, Subunternehmerüberwachung) führt regelmäßig zur Durchbrechung – BGH (I. ZS), zB Urt. v. 25.03.2004 – [I ZR 205/01](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=25.03.2004&Aktenzeichen=I%20ZR%20205/01); Urt. v. 15.11.2007 – I ZR 24/05 `[unverifiziert]`.

Folgen:
- volle Haftung ohne 8,33-SZR-Begrenzung
- 3-Jahres-Verjährung (§ 439 I 2 HGB)
- Wegfall der Tatfristfolge nach § 438 III HGB (str.; Koller aaO)

### 9. Schadensanzeige § 438 HGB – Tatfristen

[§ 438 HGB](https://www.gesetze-im-internet.de/hgb/__438.html):

| Schaden | Anzeigefrist | Folge bei Versäumnis |
|---|---|---|
| **Äußerlich erkennbar** | spätestens bei Ablieferung (§ 438 I HGB) | Vermutung ordnungsgemäßer Ablieferung (Beweislastumkehr zulasten Empfänger) |
| **Äußerlich nicht erkennbar (verborgen)** | binnen **7 Werktagen** ab Ablieferung, schriftlich (§ 438 II HGB) | dito |
| **Lieferfristüberschreitung** | binnen **21 Tagen** ab Ablieferung, schriftlich (§ 438 III HGB) | Anspruchsausschluss (str.: ggf. nur bei nicht-qualifiziertem Verschulden) |

Es handelt sich um **Tatfristen**, nicht um Verjährungsfristen. Versäumung führt nicht zum Erlöschen des Anspruchs (außer in § 438 III HGB), sondern zur Beweisbelastung des Empfängers.

### 10. Verjährung § 439 HGB

[§ 439 HGB](https://www.gesetze-im-internet.de/hgb/__439.html):

| Verschulden | Frist | Beginn |
|---|---|---|
| **Regelfall** | 1 Jahr | Tag der Ablieferung; bei vollständigem Verlust: Ablauf von 30 Tagen nach vereinbarter Lieferfrist oder, mangels solcher, 60 Tagen nach Übernahme (§ 439 II HGB) |
| **Qualifiziertes Verschulden** § 435 HGB | 3 Jahre | dito |

Hemmung: § 439 III HGB – schriftliche Reklamation hemmt die Verjährung bis zur schriftlichen Zurückweisung; daneben § 203 BGB (Verhandlungshemmung).

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute

- [§ 407 HGB](https://www.gesetze-im-internet.de/hgb/__407.html) (Frachtvertrag)
- [§ 411 HGB](https://www.gesetze-im-internet.de/hgb/__411.html) (Verpackungspflicht)
- [§ 412 HGB](https://www.gesetze-im-internet.de/hgb/__412.html) (Verladen, Entladen)
- [§ 414 HGB](https://www.gesetze-im-internet.de/hgb/__414.html) (Haftung des Absenders)
- [§ 425 HGB](https://www.gesetze-im-internet.de/hgb/__425.html) (Obhutshaftung)
- [§ 426 HGB](https://www.gesetze-im-internet.de/hgb/__426.html) (haftungsausschließende Gründe)
- [§ 427 HGB](https://www.gesetze-im-internet.de/hgb/__427.html) (besondere Haftungsausschlüsse)
- [§ 428 HGB](https://www.gesetze-im-internet.de/hgb/__428.html) (Haftung für andere Personen)
- [§ 429 HGB](https://www.gesetze-im-internet.de/hgb/__429.html) (Wertersatz bei Verlust)
- [§ 430 HGB](https://www.gesetze-im-internet.de/hgb/__430.html) (Schadensermittlung)
- [§ 431 HGB](https://www.gesetze-im-internet.de/hgb/__431.html) (Haftungshöchstbetrag 8,33 SZR/kg)
- [§ 435 HGB](https://www.gesetze-im-internet.de/hgb/__435.html) (Wegfall Haftungsbegrenzung bei qual. Verschulden)
- [§ 438 HGB](https://www.gesetze-im-internet.de/hgb/__438.html) (Schadensanzeige – 0/7/21 Tage)
- [§ 439 HGB](https://www.gesetze-im-internet.de/hgb/__439.html) (Verjährung – 1/3 Jahre)
- [§ 449 HGB](https://www.gesetze-im-internet.de/hgb/__449.html) (Abweichende Vereinbarungen)
- SZR-Tageskurs: https://www.imf.org/external/np/fin/data/rms_five.aspx

### Kommentare

- Koller, Transportrecht, 10. Aufl. 2020, § 425 HGB Rn. 1 ff.; § 431 HGB Rn. 1 ff.; § 435 HGB Rn. 1 ff.; § 438 HGB Rn. 1 ff.; § 439 HGB Rn. 1 ff. `[unverifiziert – Auflagenstand prüfen]`
- Schaffert, in: MüKoHGB, 4. Aufl. 2020, § 425 Rn. 1 ff. `[unverifiziert – Auflagenstand prüfen]`
- Herber/Eckardt, in: MüKoHGB, 4. Aufl. 2020, § 435 Rn. 1 ff. `[unverifiziert]`

### Rechtsprechung (`[unverifiziert – prüfen in juris/TranspR]`)

1. BGH, Urt. v. 25.03.2004 – I ZR 205/01, TranspR 2004, 309 (Organisationsverschulden, Schnittstellenkontrolle)
2. BGH, Urt. v. 15.11.2007 – I ZR 24/05, TranspR 2008, 117 (Leichtfertigkeit Subunternehmer)
3. BGH, Urt. v. 13.11.2013 – I ZR 78/12, TranspR 2014, 146 (Bruttogewichts-Bezug § 431 HGB)
4. OLG Düsseldorf, Urt. v. 12.10.2011 – I-18 U 110/10, TranspR 2012, 109 (Diebstahl auf ungesichertem Parkplatz)

## Ausgabeformat

```
GUTACHTEN – HGB-Frachtführerhaftung
Beförderung: <Versender → Empfänger>, <Datum Übernahme>, <Datum Ablieferung>
Gut: <Art>, Bruttogewicht <kg>, Warenwert <EUR>
Schaden: <Verlust / Beschädigung / Verspätung>, <EUR>

I. Sachverhalt
II. Frage(n)
III. Kurzantwort
     – Haftung dem Grunde nach: [ja / nein]
     – Höchstbetrag (8,33 SZR × kg): <SZR>, EUR-Gegenwert zum <Datum>
       Tageskurs SZR/EUR <Quelle, Datum>
     – Durchbruch § 435 HGB: [vorliegend / fernliegend]
     – Tatfristen § 438 HGB: [gewahrt / versäumt am <Datum>]
     – Verjährung § 439 HGB: läuft ab am <Datum>
     – Empfehlung: <…>

IV. Rechtliche Bewertung
    1. Anspruchsgrundlage § 425 HGB
    2. Obhutszeitraum und Schadensereignis
    3. Haftungsausschlüsse §§ 426, 427 HGB
       a) Unvermeidbarkeit § 426 HGB?
       b) Privilegierte Gefahren § 427 HGB?
    4. Haftung für andere Personen § 428 HGB
    5. Haftungsumfang §§ 429, 430 HGB
    6. Haftungshöchstbetrag § 431 HGB
       Berechnung: 8,33 SZR × <kg> = <SZR>
                   × Tageskurs SZR/EUR <Datum> = <EUR>
    7. Durchbruch § 435 HGB
       a) Vorsatz?
       b) Leichtfertigkeit + Bewusstsein des wahrscheinlichen Schadenseintritts?
       c) Organisationsverschulden?
    8. Schadensanzeige § 438 HGB
       – sichtbar / verborgen / Verspätung?
       – Anzeigedatum: <Datum>; Frist gewahrt: [ja / nein]
    9. Verjährung § 439 HGB
       – Regel- oder 3-Jahres-Frist?
       – Beginn: <Datum>; Ablauf: <Datum>
       – Hemmung § 439 III HGB / § 203 BGB?

V. Gesamtergebnis

VI. Risiken / offene Punkte
    🟢 / 🟡 / 🔴 <Einstufung mit Begründung>
    – Offene Tatsachen: Bruttogewicht je Sendungsposition, Frachtbriefvermerk,
      Schadensanzeigedatum, Schnittstellenprotokoll Frachtführer

VII. Quellenverzeichnis
     – Statute (gesetze-im-internet.de)
     – Rspr. (BGH I ZR …, OLG …) [unverifiziert – prüfen]
     – Kommentare (Koller, MüKoHGB)
     – SZR-Tageskurs IWF, abgerufen am <Datum>
```

## Beispiel (Auszug, Gutachtenstil)

> "Der Frachtführer F haftet dem Versender V dem Grunde nach nach § 425 Abs. 1 HGB für den Verlust dreier Paletten im Obhutszeitraum zwischen Übernahme am 12.03. und Ablieferung am 14.03. F könnte sich auf § 426 HGB berufen. Dafür müsste F nachweisen, dass der Schaden auf Umständen beruht, die auch bei größter Sorgfalt nicht zu vermeiden waren. Der bloße Hinweis 'Diebstahl auf bewachtem Parkplatz' genügt diesem Maßstab nicht; nach BGH (I. ZS, Urt. v. 25.03.2004 – [I ZR 205/01](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=25.03.2004&Aktenzeichen=I%20ZR%20205/01)) ist eine konkrete Darlegung der Sicherungsmaßnahmen erforderlich. F dürfte daher haften.
>
> Der Höchstbetrag nach § 431 Abs. 1 HGB beträgt 8,33 SZR pro kg Rohgewicht. Bei einem Bruttogewicht der drei verlorenen Paletten von 790 kg ergibt das einen Höchstbetrag von **6.580,7 SZR**. Der EUR-Gegenwert ist nach dem Tageskurs SZR/EUR am Tag der Regulierung umzurechnen (IWF-Kurs unter https://www.imf.org/external/np/fin/data/rms_five.aspx, Stand <Datum einsetzen>) `[unverifiziert – Tageskurs prüfen]`.
>
> Ein Durchbruch dieser Begrenzung nach § 435 HGB setzt Vorsatz oder Leichtfertigkeit mit dem Bewusstsein voraus, dass ein Schaden mit Wahrscheinlichkeit eintreten werde. Ob das hier vorliegt, hängt insbesondere von Schnittstellenkontrollen und Diebstahlsicherung des F ab; ohne Schnittstellenprotokoll kommt sekundäre Darlegungslast in Betracht. ..."

## Risiken / typische Fehler

- **Fixer EUR-Wert für 8,33 SZR ohne Datum** – verfälscht die Höhe, da SZR/EUR tagesabhängig schwankt. Stattdessen Methode + Tageskurs mit Datumsangabe.
- **§ 435 HGB-Subsumtion oberflächlich** – pauschal "Organisationsverschulden" reicht nicht; Schnittstellenkontrolle, Sicherung, Subunternehmerüberwachung sind konkret zu prüfen.
- **§ 438 III HGB und Verspätung verwechselt** – nur die Verspätungsanzeige ist Anspruchsausschluss, nicht die Verlust-/Beschädigungsanzeige.
- **Verjährung § 439 II HGB falsch berechnet** bei vollständigem Verlust (30 / 60-Tage-Fiktion übersehen).
- **Wertangabe im Frachtbrief übersehen** – § 449 HGB / § 431 HGB: vereinbarte höhere Haftungsobergrenze möglich.
- **CMR statt HGB anwendbar übersehen**, sobald die Strecke grenzüberschreitend ist.
