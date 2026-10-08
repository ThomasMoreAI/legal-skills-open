---
name: mietpreisbremse-borghei
title: /mietrecht:mietpreisbremse
description: Mietpreisbremse bei Wiedervermietung von Wohnraum – zulässige Miethöhe § 556d BGB (ortsübliche Vergleichsmiete zzgl. 10 %) und Landesverordnung, Ausnahmen für Neubau und umfassende Modernisierung § 556f BGB, Vormiete und modernisierte Wohnung § 556e BGB, vorvertragliche Auskunftspflicht § 556g Abs. 1a BGB, qualifizierte Rüge und Rückforderung § 556g Abs. 2 BGB, Unwirksamkeit abweichender Vereinbarungen § 556g Abs. 1 BGB. Use when eine Neuvertragsmiete auf Zulässigkeit geprüft, eine Rüge erhoben oder überzahlte Miete zurückgefordert wird.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/mietrecht/skills/mietpreisbremse
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: real-estate
language: de
---

# /mietrecht:mietpreisbremse

## Zweck

Die Mietpreisbremse begrenzt die Miete bei **Wiedervermietung** — nicht die laufende Erhöhung. Sie wirkt nicht automatisch: Der Mieter muss **rügen**, und erst ab der Rüge entsteht der Rückforderungsanspruch für die Zukunft; für die Vergangenheit hilft nur die Auskunftsverletzung des Vermieters. Diese Skill bestimmt die zulässige Miete, prüft die vier Ausnahmetatbestände und formuliert die qualifizierte Rüge.

## Eingaben

- **Mietvertrag**: Datum des Vertragsschlusses, vereinbarte Nettokaltmiete, Wohnfläche, Mietbeginn
- **Belegenheit**: Gilt für den Ort eine **Landesverordnung** nach § 556d Abs. 2 BGB? Seit wann, bis wann?
- **Ortsübliche Vergleichsmiete**: Mietspiegelwert, Feld, Spanne, Fassung
- **Vormiete**: Höhe der zuletzt vor Vertragsschluss geschuldeten Miete und Zeitpunkt
- **Bauzustand**: Erstnutzung nach dem 01.10.2014? Umfassende Modernisierung? Modernisierung in den letzten drei Jahren?
- **Auskunft** des Vermieters nach § 556g Abs. 1a BGB: erteilt, wann, in welcher Form
- Bisher gezahlte Mieten (für die Rückforderung)

## Sub-Agent-Architektur

Die Prüfung wird in Prosa von spezialisierten Schritten getragen; einen `agents`-Block trägt diese Skill bewusst nicht (mietrecht-Konvention). Ein **Anwendungsbereichs-Prüfer** klärt zuerst, ob überhaupt eine wirksame Landesverordnung für den Ort und den Vertragszeitraum gilt — daran scheitern in der Praxis die meisten Fälle. Ein **Ausnahme-Prüfer** arbeitet die Tatbestände der §§ 556e, 556f BGB ab, weil sie die zulässige Miete vollständig verschieben. Ein **Rechen-Prüfer** ermittelt die zulässige Miete und den Überzahlungsbetrag. Ein **Rüge-Prüfer** formuliert die qualifizierte Rüge und bestimmt den Beginn des Rückforderungszeitraums.

## Ablauf

### 1. Anwendungsbereich ([§ 556d BGB](https://www.gesetze-im-internet.de/bgb/__556d.html))

Wird ein Mietvertrag über Wohnraum abgeschlossen, der in einem durch **Rechtsverordnung der Landesregierung** bestimmten Gebiet mit **angespanntem Wohnungsmarkt** liegt, darf die Miete zu Beginn des Mietverhältnisses die **ortsübliche Vergleichsmiete höchstens um 10 %** übersteigen. Zu prüfen ist:

- Existiert für den Ort eine **wirksame Verordnung**? Sie muss begründet sein und ist zeitlich befristet; mehrere Landesverordnungen sind wegen fehlender Begründung für unwirksam erklärt worden.
- Fällt der **Vertragsschluss** in den Geltungszeitraum? Maßgeblich ist der Vertragsschluss, nicht der Mietbeginn.
- Handelt es sich um **Wohnraum**? Gewerberaum, Wohnraum zum vorübergehenden Gebrauch, möblierter Wohnraum in der Vermieterwohnung und Werkmietwohnungen sind ausgenommen (§ 549 Abs. 2 BGB).

Die Verfassungsmäßigkeit der Regelung ist geklärt: BVerfG, Beschl. v. 18.07.2019 – 1 BvL 1/18 u.a., https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=2019-07-18&Aktenzeichen=1%20BvL%201/18.

### 2. Ortsübliche Vergleichsmiete als Bezugsgröße

Die ortsübliche Vergleichsmiete bestimmt sich nach **§ 558 Abs. 2 BGB**: Entgelte für nicht preisgebundenen Wohnraum vergleichbarer Art, Größe, Ausstattung, Beschaffenheit und Lage einschließlich der energetischen Ausstattung, vereinbart oder geändert in den letzten **sechs Jahren**. Praktisch wird der **Mietspiegel** herangezogen; die Wohnung ist konkret in Feld und Spanne einzuordnen. Die zulässige Miete beträgt diesen Wert **zuzüglich 10 %**. Vertiefung zur Ermittlung: `/mietrecht:mieterhoehung-558-bgb`.

### 3. Vormiete und vorangegangene Modernisierung ([§ 556e BGB](https://www.gesetze-im-internet.de/bgb/__556e.html))

**Abs. 1 — Vormiete:** War die zuletzt geschuldete Miete (**Vormiete**) höher als die nach § 556d Abs. 1 BGB zulässige Miete, darf eine Miete bis zur Höhe der Vormiete vereinbart werden. Unberücksichtigt bleiben Mietminderungen sowie Erhöhungen, die innerhalb des letzten Jahres vor Beendigung des Vormietverhältnisses vereinbart wurden.

**Abs. 2 — Modernisierung in den letzten drei Jahren:** Hat der Vermieter in den letzten drei Jahren vor Beginn des Mietverhältnisses **modernisiert** (§ 555b BGB), darf er die zulässige Miete um den Betrag erhöhen, der sich bei einer Modernisierungsmieterhöhung nach §§ 559–559b BGB ergäbe. Vertiefung: `/mietrecht:modernisierung-559-bgb`.

### 4. Ausnahmen ([§ 556f BGB](https://www.gesetze-im-internet.de/bgb/__556f.html))

Die Mietpreisbremse gilt **nicht**

- für Wohnraum, der **nach dem 01.10.2014 erstmals genutzt und vermietet** wird (**Neubauprivileg**, S. 1) — und zwar dauerhaft, auch für jede spätere Wiedervermietung;
- für die **erste Vermietung nach umfassender Modernisierung** (S. 2). „Umfassend" verlangt nach h.M. einen Aufwand von etwa **einem Drittel** des für einen vergleichbaren Neubau erforderlichen Betrags und eine Qualität, die einem Neubau nahekommt; bloße Renovierung genügt nicht.

Die Darlegungs- und Beweislast für die Ausnahmen trägt der **Vermieter**.

### 5. Vorvertragliche Auskunftspflicht ([§ 556g Abs. 1a BGB](https://www.gesetze-im-internet.de/bgb/__556g.html))

Der Vermieter hat den Mieter **unaufgefordert und in Textform vor Abgabe von dessen Vertragserklärung** darüber zu informieren, wenn er sich auf eine der folgenden Konstellationen berufen will:

1. **Vormiete** (§ 556e Abs. 1 BGB) — Höhe der Vormiete,
2. **Modernisierung in den letzten drei Jahren** (§ 556e Abs. 2 BGB),
3. **Neubau** nach dem 01.10.2014 (§ 556f S. 1 BGB),
4. **umfassende Modernisierung** (§ 556f S. 2 BGB).

**Sanktion:** Erteilt der Vermieter die Auskunft nicht, kann er sich auf die betreffende Ausnahme **nicht berufen**. Holt er sie nach, kann er sich erst **zwei Jahre nach Nachholung** darauf berufen (Abs. 1a S. 2, 3). Das macht die Auskunftspflicht zum wirksamsten Hebel des Mieters.

### 6. Rüge und Rückforderung ([§ 556g Abs. 1, Abs. 2 BGB](https://www.gesetze-im-internet.de/bgb/__556g.html))

Eine zum Nachteil des Mieters abweichende Vereinbarung ist **unwirksam** (Abs. 1 S. 1); zu viel gezahlte Miete ist nach den Vorschriften über die **ungerechtfertigte Bereicherung** herauszugeben (Abs. 1 S. 3). Der Mieter kann die Rückzahlung jedoch erst verlangen, **nachdem er einen Verstoß gerügt hat**; die Rüge muss die **Tatsachen enthalten, auf denen die Beanstandung beruht** (**qualifizierte Rüge**, Abs. 2). Die Rüge wirkt **ex nunc** — zurückgefordert werden kann nur die nach Zugang der Rüge fällig gewordene Miete. Für Zeiträume davor kommt ein Anspruch nur in Betracht, soweit der Vermieter seine Auskunftspflicht nach Abs. 1a verletzt hat. Ergänzend besteht ein **Auskunftsanspruch** nach Abs. 3 über die für die zulässige Miethöhe maßgeblichen Tatsachen.

### 7. Durchsetzung und Abtretung

Der Rückforderungsanspruch kann an **registrierte Inkassodienstleister** abgetreten werden; deren Geschäftsmodell ist mit dem RDG vereinbar (BGH, Urt. v. 27.11.2019 – VIII ZR 285/18, https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2019-11-27&Aktenzeichen=VIII%20ZR%20285/18). Die Verjährung richtet sich nach den §§ 195, 199 BGB (drei Jahre ab Schluss des Jahres der Entstehung und Kenntnis). Die Rüge sollte daher früh und beweisbar zugehen. **Keine Kündigungsgefahr:** Die Rüge ist Rechtsausübung; eine darauf gestützte Kündigung wäre unwirksam und begründete Schadensersatzansprüche.

## Quellen

### Statute

- [§ 556d BGB](https://www.gesetze-im-internet.de/bgb/__556d.html), [§ 556e BGB](https://www.gesetze-im-internet.de/bgb/__556e.html), [§ 556f BGB](https://www.gesetze-im-internet.de/bgb/__556f.html), [§ 556g BGB](https://www.gesetze-im-internet.de/bgb/__556g.html)
- [§ 558 BGB](https://www.gesetze-im-internet.de/bgb/__558.html) (ortsübliche Vergleichsmiete), [§ 559 BGB](https://www.gesetze-im-internet.de/bgb/__559.html), [§ 555b BGB](https://www.gesetze-im-internet.de/bgb/__555b.html)
- [§ 549 BGB](https://www.gesetze-im-internet.de/bgb/__549.html) (Ausnahmen vom Wohnraummietrecht), [§ 812 BGB](https://www.gesetze-im-internet.de/bgb/__812.html), [§ 195 BGB](https://www.gesetze-im-internet.de/bgb/__195.html), [§ 199 BGB](https://www.gesetze-im-internet.de/bgb/__199.html)

### Kommentare

- Börstinghaus, in: Schmidt-Futterer, Mietrecht, 15. Aufl. 2023, § 556d BGB Rn. 1 ff.; § 556g BGB Rn. 1 ff.
- Artz, in: MüKoBGB, 9. Aufl. 2023, § 556d Rn. 1 ff.; § 556f Rn. 1 ff.
- Weidenkaff, in: Grüneberg, BGB, 84. Aufl. 2025, § 556d Rn. 1 ff.

### Rechtsprechung

- BVerfG, Beschl. v. 18.07.2019 – 1 BvL 1/18 u.a. (Mietpreisbremse verfassungsgemäß) — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=2019-07-18&Aktenzeichen=1%20BvL%201/18
- BGH, Urt. v. 27.11.2019 – VIII ZR 285/18 (Abtretung an registrierten Inkassodienstleister; Vereinbarkeit mit dem RDG) — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2019-11-27&Aktenzeichen=VIII%20ZR%20285/18
- Zur Auslegung der „umfassenden Modernisierung" nach § 556f S. 2 BGB und zur Drittel-Grenze ist die einschlägige Rechtsprechung heranzuziehen `[unverifiziert - prüfen]`.

## Formulierungshilfe — Qualifizierte Rüge (§ 556g Abs. 2 BGB)

```
Sehr geehrte Damen und Herren,

hiermit rüge ich gemäß § 556g Abs. 2 BGB einen Verstoß gegen die
Vorschriften über die zulässige Miethöhe bei Mietbeginn (§§ 556d ff. BGB)
und stütze die Rüge auf folgende Tatsachen:

1. Die Wohnung <Anschrift, Lage im Haus> liegt im Geltungsbereich der
   <Bezeichnung der Landesverordnung> vom <Datum>, in Kraft seit <Datum>.
   Der Mietvertrag wurde am <Datum> geschlossen und damit im
   Geltungszeitraum.
2. Die vereinbarte Nettokaltmiete beträgt <Betrag> EUR für <…> m², mithin
   <…> EUR/m².
3. Nach dem Mietspiegel der Stadt <Ort> (Fassung <Datum>) ist die Wohnung
   in das Feld <…> einzuordnen (Baujahr <…>, Ausstattung <…>, Lage <…>).
   Der einschlägige Wert beträgt <…> EUR/m². Zuzüglich 10 % ergibt sich
   eine zulässige Miete von <…> EUR/m², mithin <Betrag> EUR monatlich.
4. Die vereinbarte Miete übersteigt die zulässige Miete damit um
   <Betrag> EUR monatlich.
5. Eine Auskunft nach § 556g Abs. 1a BGB haben Sie vor meiner
   Vertragserklärung nicht erteilt. Auf die Ausnahmen der §§ 556e, 556f BGB
   können Sie sich daher nicht berufen.

Ich fordere Sie auf, die Miete ab dem <Datum> auf <Betrag> EUR zu
reduzieren und die ab Zugang dieser Rüge überzahlten Beträge nach
§ 556g Abs. 1 S. 3 BGB zurückzuzahlen. Ferner verlange ich Auskunft nach
§ 556g Abs. 3 BGB über die für die zulässige Miethöhe maßgeblichen
Tatsachen.

Frist: <Datum>

Mit freundlichen Grüßen
```

## Ausgabeformat

```
MIETPREISBREMSE §§ 556d ff. BGB — Prüfung — <Mandat-ID> — <Datum>

I.    Anwendungsbereich
      - Landesverordnung                 <Bezeichnung, Geltung von–bis>  [wirksam / zweifelhaft]
      - Vertragsschluss im Zeitraum      [✅ / ❌]
      - Wohnraum (§ 549 BGB)             [✅ / Ausnahme]
II.   Zulässige Miete (§ 556d Abs. 1)    Vergleichsmiete: <…> EUR/m²
                                         + 10 % = <…> EUR/m² → <Betrag> EUR
III.  Vereinbarte Miete                  <Betrag> EUR    Differenz: <Betrag> EUR
IV.   Ausnahmen
      - Vormiete (§ 556e Abs. 1)         [N/A / <Betrag>]
      - Modernisierung 3 Jahre (§ 556e Abs. 2) [N/A / Zuschlag <Betrag>]
      - Neubau ab 01.10.2014 (§ 556f S. 1)     [N/A / greift → Prüfung endet]
      - Umfassende Modernisierung (§ 556f S. 2) [N/A / greift / streitig]
V.    Auskunft (§ 556g Abs. 1a)          [erteilt am <Datum> / nicht erteilt]
      Folge                              [Berufung auf Ausnahme möglich /
                                          ausgeschlossen / erst ab <Datum +2 J.>]
VI.   Rüge (§ 556g Abs. 2)               [erhoben am <Datum> / zu erheben]
      Qualifiziert (Tatsachen benannt)   [✅ / ⚠️]
VII.  Rückforderung                      ab <Datum>: <Betrag> EUR
      Verjährung §§ 195, 199 BGB         Ende: <Datum>
VIII. Auskunftsanspruch (§ 556g Abs. 3)  [geltend gemacht / offen]

Ergebnis: <Miete überhöht um … / zulässig>
Risiko: [🟢 / 🟡 / 🔴]
```

## Risiken / typische Fehler

- **Landesverordnung nicht geprüft** — mehrere Verordnungen sind wegen fehlender oder verspäteter Begründung für unwirksam erklärt worden; ohne wirksame Verordnung greift die Mietpreisbremse nicht.
- **Rüge nicht qualifiziert** — ohne Angabe der tragenden Tatsachen beginnt der Rückforderungszeitraum nicht zu laufen.
- **Rückwirkung überschätzt** — die Rüge wirkt ex nunc; für die Vergangenheit hilft nur die Verletzung der Auskunftspflicht nach § 556g Abs. 1a BGB.
- **Neubauprivileg übersehen** — für Wohnraum mit erstmaliger Nutzung und Vermietung nach dem 01.10.2014 gilt die Mietpreisbremse dauerhaft nicht, auch bei späteren Wiedervermietungen.
- **Vormiete falsch angesetzt** — Erhöhungen im letzten Jahr vor Beendigung des Vormietverhältnisses und Minderungen bleiben außer Betracht.
- **Mietpreisbremse mit § 558 BGB verwechselt** — sie begrenzt die Miete bei Wiedervermietung, nicht die laufende Erhöhung auf die ortsübliche Vergleichsmiete.
- **Verjährung übersehen** — der Bereicherungsanspruch verjährt in drei Jahren nach §§ 195, 199 BGB.
