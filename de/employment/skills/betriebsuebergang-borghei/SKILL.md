---
name: betriebsuebergang-borghei
title: /arbeitsrecht:betriebsuebergang
description: Betriebsübergang nach § 613a BGB – Tatbestand des Übergangs einer wirtschaftlichen Einheit durch Rechtsgeschäft, Eintritt in die Rechte und Pflichten § 613a Abs. 1 S. 1 BGB, Transformation und einjährige Veränderungssperre § 613a Abs. 1 S. 2–4 BGB, gesamtschuldnerische Nachhaftung des Veräußerers § 613a Abs. 2 BGB, Kündigungsverbot wegen des Übergangs § 613a Abs. 4 BGB, Unterrichtung in Textform § 613a Abs. 5 BGB und der von der Rechtsprechung entwickelte Katalog, Widerspruchsrecht binnen eines Monats § 613a Abs. 6 BGB, Richtlinie 2001/23/EG. Use when ein Asset Deal, Outsourcing, Betriebsteilübergang oder Rückübertragung ansteht oder wenn ein Unterrichtungsschreiben auf Fehler geprüft wird.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/arbeitsrecht/skills/betriebsuebergang
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: employment
language: de
---

# /arbeitsrecht:betriebsuebergang

## Zweck

§ 613a BGB ist die Norm, an der Transaktionen scheitern, nachdem sie abgeschlossen wurden. Der Grund ist fast immer derselbe: ein fehlerhaftes Unterrichtungsschreiben, das die **Monatsfrist des § 613a Abs. 6 BGB nicht in Gang setzt** und den Arbeitnehmern damit ein zeitlich unbefristetes Widerspruchsrecht belässt. Dieser Skill prüft den Tatbestand, erstellt das Unterrichtungsschreiben entlang des von der Rechtsprechung entwickelten Katalogs und bewertet Widerspruchsrisiken.

## Eingaben

- Transaktionsform: Asset Deal / Outsourcing / Insourcing / Funktionsnachfolge / Umwandlung nach UmwG / Share Deal
- Übergehende Betriebsmittel: materiell (Maschinen, Immobilien, Warenlager) und immateriell (Kundenstamm, Know-how, Marken)
- Betriebsprägung: **betriebsmittelgeprägt** oder **betriebsmittelarm / personalgeprägt**?
- Wird die Hauptbelegschaft nach Zahl und Sachkunde übernommen?
- Anwendbare Tarifverträge und Betriebsvereinbarungen bei Veräußerer und Erwerber; Tarifbindung des Erwerbers
- Betriebsratsstrukturen; geplante Betriebsänderung (§§ 111 ff. BetrVG)?
- Geplanter Übergangsstichtag und Adressatenliste

## Sub-Agent-Architektur

1. **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) liefert § 613a BGB mit URL, die Richtlinie 2001/23/EG und die EuGH-/BAG-Linien zum Tatbestand und zum Unterrichtungsinhalt.
2. **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) erstellt das Unterrichtungsschreiben und den Zeitplan.
3. **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft den Katalog Punkt für Punkt, Adressaten, Form und Fristauslösung.

## Ablauf

### 1. Tatbestand ([§ 613a Abs. 1 S. 1 BGB](https://www.gesetze-im-internet.de/bgb/__613a.html))

Erforderlich ist der Übergang eines **Betriebs oder Betriebsteils** auf einen anderen Inhaber **durch Rechtsgeschäft**. Unionsrechtlich (Richtlinie 2001/23/EG) ist der Begriff als Übergang einer **wirtschaftlichen Einheit unter Wahrung ihrer Identität** auszulegen — einer organisierten Gesamtheit von Personen und Sachen zur Ausübung einer wirtschaftlichen Tätigkeit mit eigenem Zweck.

Die Identitätswahrung wird nach einer **Gesamtwürdigung** aller Umstände beurteilt (EuGH, Urt. v. 18.03.1986 – Rs. 24/85, *Spijkers*, und Folgeentscheidungen; [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=18.03.1986&Aktenzeichen=24/85)). Die Kriterien:

1. Art des betreffenden Unternehmens oder Betriebs,
2. Übergang materieller Betriebsmittel,
3. Wert der immateriellen Aktiva im Zeitpunkt des Übergangs,
4. Übernahme der Hauptbelegschaft,
5. Übergang der Kundschaft,
6. Grad der Ähnlichkeit der Tätigkeiten vor und nach dem Übergang,
7. Dauer einer etwaigen Unterbrechung der Tätigkeit.

**Entscheidend ist die Gewichtung nach Betriebstyp:**

- Bei **betriebsmittelgeprägten** Betrieben (Produktion, Logistik mit Fuhrpark) kommt es maßgeblich auf die Übernahme der sächlichen Betriebsmittel an; die Belegschaftsübernahme ist nachrangig.
- Bei **betriebsmittelarmen, personalgeprägten** Tätigkeiten (Reinigung, Bewachung, Callcenter, Pflege) genügt die Übernahme eines **nach Zahl und Sachkunde wesentlichen Teils der Belegschaft**; ohne sie liegt kein Übergang vor — die bloße **Funktionsnachfolge** (Auftragsnachfolge ohne Personal- und Mittelübernahme) reicht nicht.

**Kein Betriebsübergang** ist der **Share Deal**: Der Vertragsarbeitgeber bleibt dieselbe juristische Person, nur ihre Gesellschafter wechseln. § 613a BGB ist nicht anwendbar — was in der Praxis der wichtigste Gestaltungshebel zur Vermeidung von Widerspruchsrisiken ist.

### 2. Rechtsfolgen für die Arbeitsverhältnisse

- **Eintritt** in alle Rechte und Pflichten der im Zeitpunkt des Übergangs bestehenden Arbeitsverhältnisse (§ 613a Abs. 1 S. 1 BGB) — einschließlich Urlaubsansprüchen, Arbeitszeitkonten, Betriebszugehörigkeit, Zusagen der betrieblichen Altersversorgung.
- **Transformation** (§ 613a Abs. 1 S. 2 BGB): Kollektivrechtlich geregelte Rechte und Pflichten werden Inhalt des Arbeitsverhältnisses und dürfen **ein Jahr** lang nicht zum Nachteil des Arbeitnehmers geändert werden.
- **Ausnahmen** (§ 613a Abs. 1 S. 3, 4 BGB): Die Veränderungssperre gilt nicht, wenn beim Erwerber ein anderer Tarifvertrag oder eine andere Betriebsvereinbarung gilt (Ablösung), oder wenn die Anwendung eines anderen Tarifvertrags bei fehlender beiderseitiger Tarifbindung vereinbart wird.
- Gelten beim Erwerber **kongruente Kollektivnormen**, gehen sie den transformierten Inhalten vor — die Prüfung der Tarifbindung des Erwerbers gehört daher an den Anfang jeder Transaktionsberatung.

### 3. Haftung ([§ 613a Abs. 2 BGB](https://www.gesetze-im-internet.de/bgb/__613a.html))

Der bisherige Arbeitgeber haftet **als Gesamtschuldner** neben dem Erwerber für Verpflichtungen, die **vor** dem Übergang entstanden sind und **binnen eines Jahres** danach fällig werden. Werden sie erst nach dem Übergang fällig, haftet er nur zeitanteilig für den vor dem Übergang abgelaufenen Teil des Bemessungszeitraums. § 613a Abs. 3 BGB nimmt Umwandlungsfälle mit Erlöschen des Rechtsträgers aus.

Praxisfolge für den Unternehmenskaufvertrag: Freistellungsregelungen zwischen Veräußerer und Erwerber wirken nur im Innenverhältnis; der Arbeitnehmer kann sich an beide halten.

### 4. Kündigungsverbot ([§ 613a Abs. 4 BGB](https://www.gesetze-im-internet.de/bgb/__613a.html))

Die Kündigung **wegen** des Übergangs ist unwirksam — durch den Veräußerer wie durch den Erwerber. Kündigungen aus **anderen** Gründen bleiben zulässig (S. 2).

Die Abgrenzung entscheidet über die Wirksamkeit ganzer Restrukturierungen:

- **Unwirksam:** Kündigung, deren tragender Beweggrund der Übergang ist — etwa um den Betrieb „schlank" zu übergeben oder weil der Erwerber die Übernahme nur zu reduzierter Belegschaft wünscht.
- **Zulässig:** Kündigung aufgrund eines eigenständigen **Sanierungs- oder Erwerberkonzepts**, das im Zeitpunkt der Kündigung bereits greifbare Formen angenommen hat und unabhängig vom Übergang durchgeführt worden wäre.
- Der **Erwerberkonzept-Nachweis** ist streng: bloße Absichtserklärungen genügen nicht, verlangt sind ein verbindlicher Plan mit Zeitschiene und Maßnahmen (st. Rspr. des BAG zu § 613a Abs. 4 BGB `[unverifiziert – prüfen]`).

Der Rüge des Verstoßes gegen § 613a Abs. 4 BGB steht die 3-Wochen-Frist des § 4 KSchG entgegen — nach Fristablauf greift § 7 KSchG auch hier.

### 5. Unterrichtung ([§ 613a Abs. 5 BGB](https://www.gesetze-im-internet.de/bgb/__613a.html))

Veräußerer **oder** Erwerber haben die betroffenen Arbeitnehmer **vor** dem Übergang **in Textform** zu unterrichten über:

1. den Zeitpunkt oder den geplanten Zeitpunkt des Übergangs,
2. den Grund für den Übergang,
3. die rechtlichen, wirtschaftlichen und sozialen Folgen des Übergangs für die Arbeitnehmer,
4. die hinsichtlich der Arbeitnehmer in Aussicht genommenen Maßnahmen.

Die Rechtsprechung hat diese vier Ziffern zu einem **Katalog** konkretisiert; das Schreiben muss den Arbeitnehmer in die Lage versetzen, eine informierte Entscheidung über den Widerspruch zu treffen. Als Mindestinhalte gelten (grundlegend BAG, Urt. v. 13.07.2006 – 8 AZR 305/05, BAGE 119, 91 = NZA 2006, 1268; [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BAG&Datum=13.07.2006&Aktenzeichen=8%20AZR%20305/05) — danach setzt weder eine unterbliebene noch eine fehlerhafte Unterrichtung die Widerspruchsfrist des § 613a Abs. 6 BGB in Lauf):

| Punkt | Inhalt |
|---|---|
| Identität des Erwerbers | Firma, Rechtsform, Sitz, Registernummer — nicht nur ein Kürzel |
| Übergangsgegenstand | Welche Einheit geht über, welche Arbeitsverhältnisse sind betroffen |
| Rechtsgrund | Asset Deal, Umwandlung, Pachtende — mit Datum des Vertrages |
| Eintritt in die Arbeitsverhältnisse | Verweis auf § 613a Abs. 1 S. 1 BGB, Fortgeltung von Betriebszugehörigkeit und Vertragsinhalt |
| Kollektivrechtliche Folgen | Welche Tarifverträge und Betriebsvereinbarungen gelten künftig; Transformation und Veränderungssperre; ablösende Regelungen beim Erwerber |
| Betriebliche Altersversorgung | Fortbestand der Zusage, Durchführungsweg, Versorgungsträger, Einstandspflicht |
| Haftungsverteilung | Darstellung des § 613a Abs. 2 BGB — Gesamtschuld und zeitanteilige Haftung, in verständlicher Sprache |
| Geplante Maßnahmen | Restrukturierungen, Standortverlagerungen, Interessenausgleich, Sozialplan — auch wenn sie erst geplant sind |
| Kündigungsschutz | § 613a Abs. 4 BGB und der Fortbestand des allgemeinen Kündigungsschutzes |
| Widerspruchsrecht | Frist, Form, Adressat und die **Folgen** eines Widerspruchs |

**Kritischster Punkt — die Folgen des Widerspruchs:** Das Schreiben muss darauf hinweisen, dass der widersprechende Arbeitnehmer beim Veräußerer verbleibt und dort mangels Beschäftigungsmöglichkeit regelmäßig eine betriebsbedingte Kündigung zu erwarten hat. Ein Schreiben, das den Widerspruch als risikofreie Option darstellt, ist fehlerhaft.

**Rechtsfolge eines Fehlers:** Die Monatsfrist des § 613a Abs. 6 BGB wird **nicht in Gang gesetzt**. Das Widerspruchsrecht besteht dann fort — begrenzt allein durch **Verwirkung**, die Zeit- und Umstandsmoment voraussetzt. Widersprüche Jahre nach dem Übergang sind auf dieser Grundlage möglich und in der Praxis der Hauptschaden fehlerhafter Unterrichtungen.

### 6. Widerspruchsrecht ([§ 613a Abs. 6 BGB](https://www.gesetze-im-internet.de/bgb/__613a.html))

- Frist: **ein Monat nach Zugang der Unterrichtung** nach Absatz 5.
- Form: **schriftlich** (§ 126 BGB) — Textform genügt hier **nicht**, obwohl die Unterrichtung selbst in Textform erfolgen darf. Diese Asymmetrie ist im Gesetz angelegt und wird regelmäßig übersehen.
- Adressat: bisheriger Arbeitgeber **oder** neuer Inhaber, nach Wahl des Arbeitnehmers.
- Wirkung: Das Arbeitsverhältnis geht nicht über, sondern besteht mit dem Veräußerer fort — rückwirkend auf den Übergangszeitpunkt.

### 7. Formulierungshilfe — Unterrichtungsschreiben (Auszug)

```
<Veräußerer> und <Erwerber>

Unterrichtung über einen Betriebsübergang nach § 613a Abs. 5 BGB

Sehr geehrte(r) Frau/Herr <Name>,

wir unterrichten Sie hiermit gemeinsam darüber, dass der
Betriebsteil <Bezeichnung> mit Wirkung zum <Datum> auf die
<Firma, Rechtsform, Sitz, Handelsregister und Registernummer>
übergeht.

1. Zeitpunkt und Gegenstand des Übergangs
   <Stichtag; welche Einheit; Ihre Zugehörigkeit zu dieser Einheit>

2. Grund des Übergangs
   <Unternehmenskaufvertrag vom <Datum> / Pachtende /
    Ausgliederung nach UmwG; wirtschaftlicher Hintergrund>

3. Rechtliche Folgen
   Der Erwerber tritt nach § 613a Abs. 1 S. 1 BGB in alle Rechte
   und Pflichten aus Ihrem Arbeitsverhältnis ein. Ihr
   Arbeitsvertrag, Ihre Betriebszugehörigkeit seit <Datum>, Ihre
   Vergütung und Ihr Urlaubsanspruch bleiben unverändert.
   <Kollektivrecht: welche Tarifverträge und Betriebsvereinbarungen
    künftig gelten; Transformation nach § 613a Abs. 1 S. 2 BGB und
    einjährige Veränderungssperre; ablösende Regelungen>
   <Betriebliche Altersversorgung: Zusage, Durchführungsweg,
    Versorgungsträger>
   Für Verpflichtungen, die vor dem Übergang entstanden sind und
   innerhalb eines Jahres danach fällig werden, haftet der
   bisherige Arbeitgeber nach § 613a Abs. 2 BGB neben dem
   Erwerber als Gesamtschuldner.
   Eine Kündigung wegen des Übergangs ist nach § 613a Abs. 4 BGB
   unwirksam. Ihr allgemeiner Kündigungsschutz bleibt unberührt.

4. Wirtschaftliche und soziale Folgen
   <Arbeitsort, Arbeitszeit, Vorgesetztenstruktur, Sozial-
    leistungen, betriebliche Übungen>

5. In Aussicht genommene Maßnahmen
   <Restrukturierungen, Verlagerungen, Interessenausgleich /
    Sozialplan — oder ausdrücklich: "Maßnahmen sind derzeit
    nicht geplant.">

6. Ihr Widerspruchsrecht
   Sie können dem Übergang Ihres Arbeitsverhältnisses innerhalb
   eines Monats nach Zugang dieses Schreibens schriftlich
   widersprechen (§ 613a Abs. 6 BGB). Der Widerspruch kann
   gegenüber dem bisherigen Arbeitgeber oder dem neuen Inhaber
   erklärt werden. Er bedarf der Schriftform; eine E-Mail
   genügt nicht.

   Folgen eines Widerspruchs: Ihr Arbeitsverhältnis geht nicht
   über, sondern besteht mit <Veräußerer> fort. Da der
   Betriebsteil dort nach dem Übergang nicht fortgeführt wird
   und ein anderer Arbeitsplatz voraussichtlich nicht zur
   Verfügung steht, ist mit einer betriebsbedingten Kündigung
   zu rechnen.

<Ort, Datum>   <Unterschrift Veräußerer>   <Unterschrift Erwerber>
```

## Quellen

### Statute

- [§ 613a BGB](https://www.gesetze-im-internet.de/bgb/__613a.html), [§ 126 BGB](https://www.gesetze-im-internet.de/bgb/__126.html), [§ 242 BGB](https://www.gesetze-im-internet.de/bgb/__242.html) (Verwirkung), [§ 623 BGB](https://www.gesetze-im-internet.de/bgb/__623.html)
- [§ 4 KSchG](https://www.gesetze-im-internet.de/kschg/__4.html), [§ 7 KSchG](https://www.gesetze-im-internet.de/kschg/__7.html), [§ 1 KSchG](https://www.gesetze-im-internet.de/kschg/__1.html)
- [§ 111 BetrVG](https://www.gesetze-im-internet.de/betrvg/__111.html), [§ 112 BetrVG](https://www.gesetze-im-internet.de/betrvg/__112.html), [§ 102 BetrVG](https://www.gesetze-im-internet.de/betrvg/__102.html)
- Richtlinie 2001/23/EG des Rates vom 12.03.2001 (Wahrung von Ansprüchen bei Übergang von Unternehmen)

### Kommentare

- Preis, in: ErfK, 24. Aufl. 2024, § 613a BGB Rn. 1 ff.
- Müller-Glöge, in: MüKoBGB, 9. Aufl. 2023, § 613a Rn. 1 ff.
- Willemsen, in: HWK, 11. Aufl. 2024, § 613a BGB Rn. 200 ff. (Unterrichtung)
- Steffan, in: APS, 6. Aufl. 2021, § 613a BGB Rn. 150 ff. (Kündigungsverbot)

### Rechtsprechung

- EuGH, Urt. v. 18.03.1986 – Rs. 24/85, *Spijkers* (Wahrung der Identität der wirtschaftlichen Einheit; Gesamtwürdigung aller Umstände, keine isolierte Betrachtung einzelner Kriterien), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=18.03.1986&Aktenzeichen=24/85)
- EuGH-Rspr. zu betriebsmittelarmen Tätigkeiten (Übernahme eines nach Zahl und Sachkunde wesentlichen Teils der Belegschaft) `[unverifiziert – prüfen]`
- BAG, Urt. v. 13.07.2006 – 8 AZR 305/05, BAGE 119, 91 = NZA 2006, 1268 (inhaltliche Anforderungen an die Unterrichtung nach § 613a Abs. 5 BGB; Widerspruchsfrist läuft ohne ordnungsgemäße Unterrichtung nicht an), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BAG&Datum=13.07.2006&Aktenzeichen=8%20AZR%20305/05)
- st. Rspr. des BAG zur Verwirkung des Widerspruchsrechts bei fehlerhafter Unterrichtung (Zeit- und Umstandsmoment) `[unverifiziert – prüfen]`
- st. Rspr. des BAG zu § 613a Abs. 4 BGB und zum Erwerberkonzept `[unverifiziert – prüfen]`

> Aktenzeichen sind vor Verwendung in juris, Beck-Online, [curia.europa.eu](https://curia.europa.eu) oder der [BAG-Entscheidungsdatenbank](https://www.bundesarbeitsgericht.de/entscheidungen/) zu ermitteln.

## Ausgabeformat

```
BETRIEBSÜBERGANG § 613a BGB — <Mandat-ID> — <Datum>
VERTRAULICH — MANDATSGEHEIMNIS — § 43a Abs. 2 BRAO

Gesamtbefund: [🟢 Übergang liegt vor, Verfahren sauber /
               🟡 Nachbesserung Unterrichtung / 🔴 Widerspruchsrisiko offen]

I.    Transaktionsform                   [Asset Deal / Share Deal /
                                          Outsourcing / UmwG]
II.   Tatbestand § 613a Abs. 1 S. 1
      Betriebstyp:                       [betriebsmittelgeprägt /
                                          personalgeprägt]
      Gesamtwürdigung:                   <Kriterien 1–7 mit Gewichtung>
      Ergebnis:                          [Übergang / bloße Funktionsnachfolge]
III.  Betroffene Arbeitsverhältnisse      <N>  Liste als Anlage
IV.   Kollektivrecht
      Beim Veräußerer:                   <TV / BV>
      Beim Erwerber:                     <TV / BV>
      Transformation § 613a I 2:         [greift / abgelöst nach S. 3]
V.    Haftung § 613a Abs. 2               <Verpflichtungen, Fälligkeiten>
VI.   Kündigungen im Umfeld               [keine / <N> — Erwerberkonzept:
                                          🟢 belegt / 🔴 nicht belegt]
VII.  Unterrichtung § 613a Abs. 5
      Form Textform:                      [🟢 / 🔴]
      Katalogpunkte vollständig:          [🟢 / 🔴 fehlt: <…>]
      Folgen des Widerspruchs dargestellt:[🟢 / 🔴]
      Zugang:                             <Datum, Nachweis>
VIII. Widerspruchsfrist § 613a Abs. 6     Ende: <Datum>
      Fristauslösung wirksam:             [🟢 / 🔴 → unbefristetes
                                           Widerspruchsrecht]
IX.   Widersprüche eingegangen            <N>  Folgemaßnahmen: <…>
X.    Beteiligung des Betriebsrats        §§ 111, 112 BetrVG  [N/A / läuft]

Offene Tatsachenfragen: <…>
Empfehlung: <…>
```

## Risiken / typische Fehler

- **Unterrichtungsschreiben unvollständig** — die Monatsfrist läuft nicht an; das Widerspruchsrecht bleibt bis zur Verwirkung bestehen. Der teuerste Fehler der gesamten Norm.
- **Folgen des Widerspruchs beschönigt** — wer den Widerspruch als folgenlose Option darstellt, macht das Schreiben fehlerhaft.
- **Erwerber nur mit Kürzel bezeichnet** — erforderlich sind Firma, Rechtsform, Sitz und Registerdaten.
- **Haftungsverteilung nach § 613a Abs. 2 BGB nicht erläutert** — gehört zu den rechtlichen Folgen nach Abs. 5 Nr. 3.
- **Widerspruch in Textform akzeptiert** — § 613a Abs. 6 BGB verlangt Schriftform; umgekehrt genügt für die Unterrichtung Textform. Die Asymmetrie ist gewollt.
- **Kündigung wegen des Übergangs als „betriebsbedingt" etikettiert** — ohne belegtes Erwerberkonzept greift § 613a Abs. 4 BGB.
- **Funktionsnachfolge mit Betriebsübergang verwechselt** — die bloße Übernahme eines Auftrags ohne Personal und Betriebsmittel löst § 613a BGB nicht aus.
- **Share Deal als Betriebsübergang behandelt** — der Vertragsarbeitgeber bleibt identisch; § 613a BGB ist nicht anwendbar.
- **Tarifbindung des Erwerbers nicht geprüft** — kongruente Kollektivnormen beim Erwerber lösen die transformierten Inhalte ab und verändern die Unterrichtungspflicht.
- **Unterrichtung erst nach dem Stichtag versandt** — § 613a Abs. 5 BGB verlangt die Unterrichtung **vor** dem Übergang.
