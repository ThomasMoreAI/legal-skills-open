---
name: obliegenheitsverletzung-vvg-borghei
title: /versicherungsrecht:obliegenheitsverletzung-vvg
description: 'Prüfung der Rechtsfolgen einer vorvertraglichen Anzeigepflichtverletzung §§ 19–22 VVG (Rücktritt, Kündigung, Vertragsanpassung, Arglistanfechtung) und einer vertraglichen Obliegenheitsverletzung § 28 VVG (Leistungsfreiheit, Quotelung, Kausalitätsgegenbeweis), jeweils inkl. Belehrungserfordernis (§ 19 Abs. 5, § 28 Abs. 4 VVG) und Fristen (§ 21 Abs. 1 VVG: 1 Monat; § 124 BGB: 1/10 Jahre). Use when ein Versicherer auf Anzeigepflicht- oder Obliegenheitsverletzung gestützt Rücktritt, Kündigung oder Leistungsfreiheit erklärt.'
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/versicherungsrecht/skills/obliegenheitsverletzung-vvg
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: insurance
language: de
---

# /versicherungsrecht:obliegenheitsverletzung-vvg

## Zweck

Der Skill prüft, ob der Versicherer wirksam Rechtsfolgen aus einer **vorvertraglichen Anzeigepflichtverletzung** (§§ 19 ff. VVG) oder einer **vertraglichen Obliegenheitsverletzung** (§§ 28 ff. VVG) herleiten kann. Die Belehrungspflichten (§ 19 Abs. 5, § 28 Abs. 4 VVG) sind regelmäßig die Sollbruchstelle. Daneben prüft der Skill Fristen (§ 21 Abs. 1 VVG: ein Monat; § 21 Abs. 3 VVG: 5 / 10 Jahre; § 124 BGB: 1 / 10 Jahre) sowie den Kausalitätsgegenbeweis § 28 Abs. 3 VVG und die Quotelung § 28 Abs. 2 Satz 2 VVG.

## Eingaben

- Versicherungssparte und Versicherungsschein-Nr.
- Antragsdaten, Antragsfragen im Wortlaut, Antwortverhalten des VN
- Belehrungstext und drucktechnische Gestaltung (§ 19 Abs. 5, § 28 Abs. 4 VVG)
- Zeitpunkt der Kenntnis des Versicherers von der Pflichtverletzung
- Schreiben des Versicherers (Rücktritt / Kündigung / Vertragsanpassung / Anfechtung / Leistungsablehnung)
- bei Versicherungsfall: Ablauf, Kausalitätsfragen, Verschuldensgrad des VN

## Sub-Agent-Architektur

Researcher liefert VVG-/BGB-Statute, BGH IV. ZS-Rspr. zu Belehrungserfordernis und Quotelung sowie Kommentarstellen (Prölss/Martin, MüKoVVG, BeckOK VVG, Bruck/Möller). Drafter prüft Tatbestand, Belehrung, Frist und Rechtsfolge im Gutachtenstil, entwirft Replik gegen Rücktritt / Kündigung / Leistungsablehnung. Reviewer prüft Fristenkalender (§ 21 VVG, § 124 BGB, §§ 195, 199 BGB), Belehrungsanforderungen und ob die VVG-2008-Rechtslage durchgehalten ist (insb. keine Anwendung des § 6 VVG aF Alles-oder-Nichts).

## Ablauf

### 1. Abgrenzung: vorvertraglich vs. vertraglich

| Phase | Norm | Folge |
|---|---|---|
| **Vor Vertragsschluss** | §§ 19–22 VVG | Rücktritt, Kündigung, Vertragsanpassung, Arglistanfechtung |
| **Während Vertragslaufzeit** | § 28 VVG | Leistungsfreiheit (Vorsatz / grobe Fahrlässigkeit / Quotelung) |
| **Im Versicherungsfall** | §§ 28, 31 VVG | wie § 28; § 31 Auskunftspflicht |

### 2. Vorvertragliche Anzeigepflicht §§ 19–22 VVG

**Tatbestand § 19 Abs. 1 VVG**: VN hat bis zur Abgabe seiner Vertragserklärung die ihm bekannten Gefahrumstände, nach denen der Versicherer **in Textform** gefragt hat und die für die Übernahmeentscheidung erheblich sind, anzuzeigen.

**Voraussetzungen wirksamer Rechtsausübung durch Versicherer:**

1. **Pflichtverletzung** — VN hat eine konkrete Antragsfrage in Textform unrichtig oder unvollständig beantwortet
2. **Verschulden** — Vorsatz / grobe Fahrlässigkeit / einfache Fahrlässigkeit (s. Rechtsfolgenstaffel)
3. **Belehrung in Textform** § 19 Abs. 5 VVG, durch gesonderte Mitteilung, drucktechnisch hervorgehoben, inhaltlich korrekt
4. **Frist § 21 Abs. 1 Satz 1 VVG: ein Monat** ab Kenntnis des Versicherers von der Pflichtverletzung; die Frist beginnt mit positiver Kenntnis
5. **Ausschlussfrist § 21 Abs. 3 VVG**: 5 Jahre ab Vertragsschluss; bei Arglist 10 Jahre

**Rechtsfolgenstaffel:**

| Verschulden | Rechtsfolge |
|---|---|
| Vorsatz | Rücktritt § 19 Abs. 2 (rückwirkend; keine Leistung) |
| grobe Fahrlässigkeit | Rücktritt § 19 Abs. 2; aber Kausalitätsgegenbeweis § 21 Abs. 2 möglich; ggf. Vertragsanpassung Abs. 4 |
| einfache Fahrlässigkeit | nur Kündigung § 19 Abs. 3 (ex nunc); keine Leistungsfreiheit; ggf. Vertragsanpassung Abs. 4 |
| schuldlos | nur Kündigung § 19 Abs. 3; Vertragsanpassung Abs. 4 |
| **Arglist** | **Anfechtung § 22 VVG iVm § 123 BGB**; Frist § 124 BGB: 1 Jahr ab Kenntnis / 10 Jahre |

**Belehrung § 19 Abs. 5 VVG**: ohne ordnungsgemäße Belehrung in Textform sind Rücktritt, Kündigung und Vertragsanpassung ausgeschlossen. BGH IV. ZS verlangt drucktechnisch hervorgehobene, gesonderte Belehrung (`[unverifiziert – prüfen]`).

**Vertragsanpassung § 19 Abs. 4 VVG**: hätte Versicherer den Vertrag zu anderen Bedingungen geschlossen, kann er einseitig anpassen (Risikoausschluss / höhere Prämie); bei groben Fahrlässigkeit/Vorsatz Vorrang vor Rücktritt nur, wenn Versicherer dies wählt.

### 3. Vertragliche Obliegenheit § 28 VVG

**Voraussetzungen Leistungsfreiheit:**

1. **Vertragliche Obliegenheit** — wirksam in den AVB vereinbart; halbzwingend nach § 32 VVG (Abweichungen zu Lasten des VN unwirksam)
2. **Verletzung** der Obliegenheit
3. **Verschulden** des VN:
   - **Vorsatz** → volle Leistungsfreiheit § 28 Abs. 2 Satz 1
   - **grobe Fahrlässigkeit** → **Quotelung nach Schwere des Verschuldens** § 28 Abs. 2 Satz 2 (nicht mehr Alles-oder-Nichts wie § 6 VVG aF)
   - einfache Fahrlässigkeit / kein Verschulden → keine Leistungsfreiheit
4. **Belehrung in Textform § 28 Abs. 4 VVG**: bei Auskunfts- / Aufklärungsobliegenheiten nach Eintritt des Versicherungsfalls; ohne Belehrung keine Leistungsfreiheit
5. **Kein Kausalitätsgegenbeweis § 28 Abs. 3 VVG**: VN kann nachweisen, dass die Pflichtverletzung weder für Feststellung des Versicherungsfalls noch für Feststellung / Umfang der Leistung kausal war; Ausnahme: bei arglistiger Pflichtverletzung greift der Gegenbeweis nicht

**Quotelung** § 28 Abs. 2 Satz 2 VVG: Kürzung im Verhältnis zur Schwere des Verschuldens. Praktische Spannweite: 25–75 %; volle 100 % nur bei "grober Fahrlässigkeit im Grenzbereich zum Vorsatz" und arglistähnlichem Verhalten (BGH IV. ZS `[unverifiziert – prüfen]`).

### 4. Auskunftspflicht im Versicherungsfall § 31 VVG

VN hat dem Versicherer auf Verlangen jede Auskunft zu erteilen, die zur Feststellung des Versicherungsfalls oder des Umfangs der Leistungspflicht erforderlich ist. Rechtsfolge bei Verstoß: § 28 VVG (Leistungsfreiheit / Quotelung) bei entsprechender vertraglicher Obliegenheit und ordnungsgemäßer Belehrung.

### 5. Arglistanfechtung § 22 VVG iVm § 123 BGB

§ 22 VVG stellt klar, dass das Recht des Versicherers zur Anfechtung wegen arglistiger Täuschung **neben** §§ 19 ff. VVG besteht.

Voraussetzungen § 123 BGB: arglistige Täuschung (Vorspiegeln / Verschweigen entgegen Aufklärungspflicht) — Frist § 124 BGB: **1 Jahr ab Kenntnis** der Täuschung; spätestens **10 Jahre** ab Vertragsschluss. Anfechtungserklärung wirkt ex tunc (§ 142 BGB) — Vertrag wird von Anfang an nichtig; aber Prämien für die Zeit bis zur Anfechtung sind dem Versicherer zu belassen (§ 39 VVG analog / § 40 VVG bei Anfechtung wegen arglistiger Täuschung).

### 6. Prüfung im Beratungs- oder Klagekontext

- Hat VN die Antragsfrage **in Textform** beantwortet? (Telefonische Erfassung durch Vermittler — Frage genau prüfen, wer Erklärungsempfänger war, § 70 VVG zu Wissen des Vermittlers)
- Wurde der VN **in Textform belehrt**, gesondert und drucktechnisch hervorgehoben?
- Hat Versicherer die **Monatsfrist § 21 Abs. 1 VVG** ab Kenntnis gewahrt? Konkretes Datum der Kenntnis?
- Greift bei grober Fahrlässigkeit **Kausalitätsgegenbeweis § 21 Abs. 2 / § 28 Abs. 3 VVG**?
- Stuft der Versicherer das Verhalten zutreffend ein (Vorsatz / grobe Fahrlässigkeit / einfache Fahrlässigkeit)?

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute

- [§ 19 VVG](https://www.gesetze-im-internet.de/vvg_2008/__19.html) (Anzeigepflicht, Belehrung Abs. 5)
- [§ 20 VVG](https://www.gesetze-im-internet.de/vvg_2008/__20.html) (Vertreter des Versicherungsnehmers)
- [§ 21 VVG](https://www.gesetze-im-internet.de/vvg_2008/__21.html) (Ausübung der Rechte; Monatsfrist Abs. 1; Kausalität Abs. 2; Ausschlussfrist Abs. 3)
- [§ 22 VVG](https://www.gesetze-im-internet.de/vvg_2008/__22.html) (Arglistanfechtung)
- [§ 28 VVG](https://www.gesetze-im-internet.de/vvg_2008/__28.html) (Obliegenheitsverletzung, Quotelung, Kausalitätsgegenbeweis, Belehrung)
- [§ 31 VVG](https://www.gesetze-im-internet.de/vvg_2008/__31.html) (Auskunftspflicht)
- [§ 32 VVG](https://www.gesetze-im-internet.de/vvg_2008/__32.html) (Halbzwingender Charakter)
- [§ 40 VVG](https://www.gesetze-im-internet.de/vvg_2008/__40.html) (Prämienanteil bei Anfechtung)
- [§ 123 BGB](https://www.gesetze-im-internet.de/bgb/__123.html) (Arglistige Täuschung)
- [§ 124 BGB](https://www.gesetze-im-internet.de/bgb/__124.html) (Anfechtungsfrist)
- [§ 142 BGB](https://www.gesetze-im-internet.de/bgb/__142.html) (Wirkung der Anfechtung)

### Kommentare

- Armbrüster, in: Prölss/Martin, VVG, 32. Aufl. 2024, § 19 VVG Rn. 1 ff., § 28 VVG Rn. 1 ff.
- Looschelders, in: MüKoVVG, 3. Aufl. 2024, § 19 VVG, § 28 VVG Rn. 1 ff.
- Marlow/Spuhl, in: BeckOK VVG, Stand 2024, § 19 VVG, § 28 VVG.
- Knappmann, in: Bruck/Möller, VVG, 9. Aufl., § 19 VVG.

### Rechtsprechung (`[unverifiziert – prüfen in juris/Beck-Online/openjur]`)

1. BGH, Urt. v. 12.03.2014 – IV ZR 306/13, VersR 2014, 565 (Anforderungen an Belehrung § 19 Abs. 5 VVG) (https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=12.03.2014&Aktenzeichen=IV+ZR+306/13)
2. BGH, Urt. v. 11.05.2011 – IV ZR 148/09, VersR 2011, 909 (Quotelung bei grober Fahrlässigkeit, § 28 Abs. 2 Satz 2 VVG) (https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=11.05.2011&Aktenzeichen=IV+ZR+148/09)
3. BGH, Urt. v. 02.04.2014 – IV ZR 124/13, VersR 2014, 699 (Belehrungspflicht § 28 Abs. 4 VVG) (https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=02.04.2014&Aktenzeichen=IV+ZR+124/13)
4. BGH, Urt. v. 24.11.2010 – IV ZR 252/08, VersR 2011, 337 (Arglistanfechtung § 22 VVG) (https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=24.11.2010&Aktenzeichen=IV+ZR+252/08)

## Ausgabeformat

```
GUTACHTEN — Anzeigepflicht / Obliegenheit
Versicherer: <…>  Versicherungsschein-Nr.: <…>
Schreiben des Versicherers vom <Datum>

I. Sachverhalt (knapp)

II. Frage
    Sind Rücktritt / Kündigung / Anpassung / Anfechtung / Leistungsfreiheit
    wirksam erklärt?

III. Kurzantwort
     Wirksamkeit: [ja / nein / teilweise]
     Risiko der Versichererposition: 🟢 / 🟡 / 🔴

IV. Rechtliche Bewertung
    1. Einschlägige Norm
       a) §§ 19–22 VVG (vorvertraglich), oder
       b) § 28 VVG (vertraglich), oder
       c) § 22 VVG iVm § 123 BGB (Arglist)
    2. Tatbestand
       a) Pflichtverletzung — konkrete Frage / Obliegenheit
       b) Verschulden — Vorsatz / grobe Fahrlässigkeit / einfache Fahrl.
    3. Belehrung
       a) § 19 Abs. 5 / § 28 Abs. 4 VVG
       b) Textform, gesondert, drucktechnisch hervorgehoben?
    4. Frist
       a) § 21 Abs. 1 VVG (1 Monat ab Kenntnis)
       b) § 21 Abs. 3 VVG (5 / 10 Jahre)
       c) § 124 BGB (1 / 10 Jahre)
    5. Rechtsfolge
       a) Rücktritt / Kündigung / Vertragsanpassung / Anfechtung
       b) Leistungsfreiheit, ggf. Quotelung § 28 Abs. 2 Satz 2 VVG
    6. Kausalitätsgegenbeweis § 21 Abs. 2 / § 28 Abs. 3 VVG

V. Ergebnis und Empfehlung

VI. Fristenkalender und Risiken
    – Verjährung §§ 195, 199 BGB
    – Anfechtungsfrist § 124 BGB
    – Klagefrist (keine § 12 VVG aF mehr — seit 2008 entfallen)

VII. Quellenverzeichnis
```

## Beispiel

Berufsunfähigkeitsversicherung. Antrag Mai 2021. Versicherer hat im Antrag in Textform nach Behandlungen in den letzten fünf Jahren gefragt. VN hat eine orthopädische Behandlung 2018 (Bandscheibenvorfall, drei Termine) nicht angegeben. Leistungsantrag September 2024 wegen BU. Versicherer erklärt im November 2024 Rücktritt nach § 19 Abs. 2 VVG mit Verweis auf nicht angegebene Behandlung; Kenntnis vom Vorfall hat Versicherer aus Arztanfrage vom 30.09.2024.

**Tatbestand**: Pflichtverletzung wohl gegeben (Frage in Textform, Antwort unrichtig); Verschulden bei drei Terminen wegen Bandscheibe regelmäßig zumindest grobe Fahrlässigkeit, mglw. Vorsatz.

**Belehrung § 19 Abs. 5 VVG**: konkreten Belehrungstext und drucktechnische Hervorhebung im Antragsformular prüfen. Wenn Belehrung nicht gesondert oder nicht drucktechnisch hervorgehoben — Rücktritt ausgeschlossen. **Erste Verteidigungslinie.**

**Frist § 21 Abs. 1 VVG**: Kenntnis 30.09.2024, Rücktritt November 2024 — innerhalb eines Monats? Wenn Rücktritt z. B. 05.11.2024, ist Monatsfrist überschritten — **🔴 Rücktritt ausgeschlossen**. Konkretes Datum prüfen. Zweite Verteidigungslinie.

**Kausalitätsgegenbeweis § 21 Abs. 2 VVG**: bei grober Fahrlässigkeit kann VN beweisen, dass die nicht angezeigte Behandlung weder zum Vertragsschluss (Versicherer hätte trotzdem zu denselben Bedingungen abgeschlossen) noch zum Leistungsfall (BU beruht auf anderer Ursache) kausal war. Schwierig bei BU mit Rückenbezug.

**Arglistanfechtung § 22 VVG iVm § 123 BGB**: vom Versicherer subsidiär möglich; Frist § 124 BGB 1 Jahr ab Kenntnis.

**Empfehlung**: Belehrung und Frist sind die zwei Sollbruchstellen. Replik gegen Rücktritt mit Konzentration auf Belehrungsmangel und Fristüberschreitung. Risiko 🟡.

## Risiken / typische Fehler

- **Belehrung nicht konkret geprüft** — pauschale Annahme "Belehrung wird schon ordnungsgemäß sein" ist unzulässig.
- **Monatsfrist § 21 Abs. 1 VVG übersehen** — bei Fristüberschreitung sind Rücktritt, Kündigung und Vertragsanpassung ausgeschlossen.
- **Quotelung als Alles-oder-Nichts** behandelt — § 6 VVG aF gilt nicht mehr; § 28 Abs. 2 Satz 2 VVG verlangt verhältnismäßige Kürzung.
- **Kausalitätsgegenbeweis § 28 Abs. 3 / § 21 Abs. 2 VVG übersehen**.
- **Arglist und grobe Fahrlässigkeit gleichgesetzt** — bei Arglist kein Kausalitätsgegenbeweis, Frist § 124 BGB statt § 21 Abs. 1 VVG.
- **Wissen des Vermittlers § 70 VVG** nicht geprüft, wenn Antrag durch Vertreter aufgenommen wurde.
- **VVG aF zitiert** (§ 16 ff. VVG aF) für Verträge nach 01.01.2008.
