---
name: urlaubsanspruch-borghei
title: /arbeitsrecht:urlaubsanspruch
description: Urlaubsansprüche nach dem BUrlG – Entstehung und Wartezeit §§ 1, 4 BUrlG, gesetzlicher Mindesturlaub § 3 BUrlG in Werktagen und die Umrechnung bei abweichender Verteilung der Arbeitszeit, Festlegung und Übertragung § 7 Abs. 3 BUrlG, Abgeltung bei Beendigung § 7 Abs. 4 BUrlG, Verfall nur nach Erfüllung der arbeitgeberseitigen Hinweis- und Aufforderungsobliegenheit, Verjährung des Urlaubsanspruchs, Erkrankung im Urlaub § 9 BUrlG, 15-Monats-Frist bei durchgehender Langzeiterkrankung, Teilurlaub § 5 BUrlG, Abgrenzung von gesetzlichem und vertraglichem Mehrurlaub. Use when Urlaubsansprüche zu berechnen, Verfall oder Verjährung zu prüfen oder Abgeltungsansprüche nach Beendigung geltend zu machen sind.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/arbeitsrecht/skills/urlaubsanspruch
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: employment
language: de
---

# /arbeitsrecht:urlaubsanspruch

## Zweck

Das BUrlG ist ein kurzes Gesetz, dessen praktisch wichtigste Regeln nicht darin stehen. Verfall, Verjährung und die 15-Monats-Frist bei Langzeiterkrankung sind Produkte des Zusammenspiels von EuGH und BAG — mit dem Ergebnis, dass Urlaub aus lange zurückliegenden Jahren in erheblichem Umfang fortbestehen kann, wenn der Arbeitgeber seine Obliegenheiten versäumt hat. Dieser Skill berechnet den Anspruch, prüft den Verfall und beziffert die Abgeltung.

## Eingaben

- Beschäftigungsdauer, Eintrittsdatum, ggf. Beendigungsdatum und -grund
- Vertraglich, tariflich oder betrieblich vereinbarter Urlaub — mit dem entscheidenden Punkt: Ist der **Mehrurlaub vom gesetzlichen Urlaub eigenständig geregelt**?
- Verteilung der Arbeitszeit: Zahl der Arbeitstage pro Woche, Änderungen im Jahresverlauf, Teilzeit
- Genommene Urlaubstage je Kalenderjahr, dokumentierte Anträge und Ablehnungen
- Arbeitsunfähigkeitszeiten mit Beginn und Ende; durchgehende Langzeiterkrankung?
- **Hat der Arbeitgeber jährlich individuell aufgefordert und auf den Verfall hingewiesen?** Wenn ja: Datum, Form, Nachweis
- Ruhenstatbestände: Elternzeit ([§ 17 BEEG](https://www.gesetze-im-internet.de/beeg/__17.html)), Pflegezeit, Sabbatical, Bezug von Krankengeld

## Sub-Agent-Architektur

1. **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) liefert BUrlG-Normen mit URL, die Richtlinie 2003/88/EG und die EuGH-/BAG-Linien zu Verfall, Verjährung und Langzeiterkrankung.
2. **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) erstellt die Urlaubskontenaufstellung, das Hinweisschreiben oder die Zahlungsklage.
3. **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft Umrechnung, Verfallsvoraussetzungen, Ausschlussfristen und Bezifferung.

## Ablauf

### 1. Entstehung und Umfang ([§ 1 BUrlG](https://www.gesetze-im-internet.de/burlg/__1.html), [§ 3 BUrlG](https://www.gesetze-im-internet.de/burlg/__3.html))

Jeder Arbeitnehmer hat in jedem Kalenderjahr Anspruch auf bezahlten Erholungsurlaub. Der gesetzliche Mindesturlaub beträgt **jährlich mindestens 24 Werktage** (§ 3 Abs. 1 BUrlG); Werktage sind alle Kalendertage außer Sonn- und gesetzlichen Feiertagen (§ 3 Abs. 2 BUrlG) — also die **Sechs-Tage-Woche** als gesetzlicher Referenzmaßstab.

**Umrechnung** bei abweichender Verteilung:

```
Urlaubstage = 24 × (Arbeitstage pro Woche / 6)

5-Tage-Woche:   24 × 5/6 = 20 Tage
4-Tage-Woche:   24 × 4/6 = 16 Tage
3-Tage-Woche:   24 × 3/6 = 12 Tage
```

Bei **unterjähriger Änderung** der Verteilung ist der Anspruch für jeden Zeitabschnitt getrennt umzurechnen; eine nachträgliche Kürzung bereits entstandenen Urlaubs wegen eines Wechsels in Teilzeit ist unionsrechtlich unzulässig `[unverifiziert – prüfen]`.

**Wartezeit** ([§ 4 BUrlG](https://www.gesetze-im-internet.de/burlg/__4.html)): Der volle Urlaubsanspruch entsteht erstmals nach sechsmonatigem Bestehen des Arbeitsverhältnisses. Vorher und in den Fällen des [§ 5 BUrlG](https://www.gesetze-im-internet.de/burlg/__5.html) besteht **Teilurlaub** von einem Zwölftel je vollem Beschäftigungsmonat; Bruchteile von mindestens einem halben Tag sind aufzurunden (§ 5 Abs. 2 BUrlG).

**Unabdingbarkeit** ([§ 13 BUrlG](https://www.gesetze-im-internet.de/burlg/__13.html)): Von den §§ 1, 2, 3 Abs. 1 BUrlG kann nicht zuungunsten des Arbeitnehmers abgewichen werden.

### 2. Die zentrale Weichenstellung: gesetzlicher Urlaub oder Mehrurlaub

Alle nachfolgenden Regeln zu Verfall, Verjährung und Langzeiterkrankung sind **unionsrechtlich determiniert** und gelten daher zwingend nur für die **vier Wochen** des Art. 7 der Richtlinie 2003/88/EG (= 20 Tage bei Fünf-Tage-Woche).

Für den **übergesetzlichen Mehrurlaub** können die Parteien eigenständige Regeln vereinbaren — abweichende Verfallfristen, Abgeltungsausschluss, Kürzung bei Krankheit. Voraussetzung ist allerdings, dass sich aus Vertrag oder Tarifvertrag ein **hinreichend deutlicher Wille** zur eigenständigen Regelung ergibt; im Zweifel gilt für den Mehrurlaub dasselbe Regime wie für den gesetzlichen Urlaub (st. Rspr. des BAG zur Abgrenzung von gesetzlichem Urlaub und Mehrurlaub `[unverifiziert – prüfen]`).

Praktische Konsequenz für die Vertragsgestaltung: Wer Mehrurlaub gewährt, sollte ihn ausdrücklich als solchen bezeichnen und die abweichenden Regeln explizit machen.

### 3. Festlegung, Übertragung und Verfall ([§ 7 BUrlG](https://www.gesetze-im-internet.de/burlg/__7.html))

Nach dem Gesetzeswortlaut ist der Urlaub **im laufenden Kalenderjahr** zu gewähren und zu nehmen; eine Übertragung ist nur bei dringenden betrieblichen oder in der Person liegenden Gründen statthaft und führt zum Verfall am **31. März** des Folgejahres (§ 7 Abs. 3 BUrlG).

Dieser automatische Verfall gilt so **nicht mehr**. Nach der unionsrechtlich geprägten Rechtsprechung verfällt der gesetzliche Urlaub am Jahresende oder zum 31. März nur, wenn der Arbeitgeber zuvor seine **Mitwirkungsobliegenheiten** erfüllt hat (EuGH, Urt. v. 06.11.2018 – C-619/16, *Kreuziger*, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=06.11.2018&Aktenzeichen=C-619/16), und C-684/16, *Max-Planck-Gesellschaft/Shimizu*, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=06.11.2018&Aktenzeichen=C-684/16); umgesetzt durch BAG, Urt. v. 19.02.2019 – 9 AZR 541/15, NZA 2019, 982, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BAG&Datum=19.02.2019&Aktenzeichen=9%20AZR%20541/15)). Erforderlich sind kumulativ:

1. eine **individuelle** Mitteilung an den einzelnen Arbeitnehmer — kein Aushang, kein Intranet-Rundschreiben,
2. Angabe der **konkreten Zahl** der noch offenen Urlaubstage,
3. **Aufforderung**, den Urlaub zu nehmen,
4. **Hinweis** darauf, dass der Urlaub andernfalls am Ende des Kalenderjahres bzw. des Übertragungszeitraums **verfällt**,
5. **rechtzeitig** im laufenden Kalenderjahr, so dass der Urlaub noch genommen werden kann.

Die **Darlegungs- und Beweislast** für die Erfüllung dieser Obliegenheiten trägt der Arbeitgeber. Ohne dokumentierten Nachweis kumuliert der Urlaub über Jahre.

**Formulierungshilfe — Hinweisschreiben:**

```
An <Name>, Personalnummer <…>
Betreff: Ihr Urlaubsanspruch <Jahr> — Aufforderung und Hinweis
         auf den Verfall

Sehr geehrte(r) Frau/Herr <Name>,

zum <Datum> haben Sie von Ihrem Urlaubsanspruch für das
Kalenderjahr <Jahr> noch <N> Urlaubstage nicht genommen.
Davon entfallen <N> Tage auf den gesetzlichen Mindesturlaub
und <N> Tage auf den vertraglichen Mehrurlaub.

Wir fordern Sie hiermit auf, diesen Urlaub im laufenden
Kalenderjahr zu beantragen und zu nehmen. Bitte stimmen Sie
die Lage mit Ihrer Führungskraft ab.

Wir weisen Sie ausdrücklich darauf hin, dass Ihr Urlaub mit
Ablauf des 31.12.<Jahr> verfällt, wenn Sie ihn nicht bis dahin
nehmen. Nur wenn dringende betriebliche oder in Ihrer Person
liegende Gründe der Inanspruchnahme entgegenstehen, wird der
Urlaub auf die ersten drei Monate des Folgejahres übertragen
und verfällt dann mit Ablauf des 31.03.<Folgejahr>.

<Ort, Datum, Unterschrift>
Zur Kenntnis genommen: ____________________  (Datum)
```

Der Rücklauf ist zur Personalakte zu nehmen — das Schreiben ist das Beweismittel, ohne das der Verfall nicht eintritt.

### 4. Verjährung

Der Urlaubsanspruch unterliegt der Regelverjährung von drei Jahren ([§ 195 BGB](https://www.gesetze-im-internet.de/bgb/__195.html)). Die Verjährungsfrist beginnt jedoch **nicht** mit dem Schluss des Urlaubsjahres, sondern erst mit dem Schluss des Jahres, in dem der Arbeitgeber seine Hinweis- und Aufforderungsobliegenheiten **erfüllt** hat und der Urlaub gleichwohl nicht genommen wurde (BAG, Urt. v. 20.12.2022 – 9 AZR 266/20, NZA 2023, 683; [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BAG&Datum=20.12.2022&Aktenzeichen=9%20AZR%20266/20)).

Praxisfolge: Bei einem Arbeitgeber, der nie belehrt hat, ist der Anspruch weder verfallen noch verjährt — er kumuliert bis zur Beendigung des Arbeitsverhältnisses und schlägt dann in einen Abgeltungsanspruch um. Der Abgeltungsanspruch selbst ist ein reiner Geldanspruch und verjährt ab seiner Entstehung mit der Beendigung nach §§ 195, 199 BGB; er unterliegt zudem **arbeitsvertraglichen und tariflichen Ausschlussfristen**.

### 5. Krankheit

- **Erkrankung während des Urlaubs** ([§ 9 BUrlG](https://www.gesetze-im-internet.de/burlg/__9.html)): Durch ärztliches Zeugnis nachgewiesene Tage der Arbeitsunfähigkeit werden **nicht** auf den Jahresurlaub angerechnet. Die Tage sind gutzuschreiben; der Arbeitnehmer darf den Urlaub allerdings nicht eigenmächtig verlängern.
- **Urlaub bei durchgehender Arbeitsunfähigkeit:** Der Anspruch entsteht auch während der Erkrankung; er ist nur nicht erfüllbar. Der Arbeitgeber kann seine Hinweisobliegenheit hier nicht erfüllen, weil der Urlaub tatsächlich nicht genommen werden kann.
- **15-Monats-Frist:** Ist der Arbeitnehmer durchgehend arbeitsunfähig und deshalb an der Inanspruchnahme gehindert, verfällt der gesetzliche Urlaubsanspruch **15 Monate nach Ablauf des Urlaubsjahres** — für das Urlaubsjahr 2024 also mit Ablauf des **31.03.2026** (EuGH, Urt. v. 22.11.2011 – C-214/10, *KHS/Schulte*; [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=22.11.2011&Aktenzeichen=C-214/10); umgesetzt in st. Rspr. des BAG `[unverifiziert – prüfen]`).
- **Wichtige Einschränkung:** Diese 15-Monats-Frist greift nur, wenn der Arbeitnehmer **durchgehend** arbeitsunfähig war. War er im Urlaubsjahr zeitweise arbeitsfähig, hätte er den Urlaub teilweise nehmen können; dann bleibt es beim Erfordernis der Hinweisobliegenheit, und ohne deren Erfüllung tritt kein Verfall ein `[unverifiziert – prüfen]`.

### 6. Abgeltung ([§ 7 Abs. 4 BUrlG](https://www.gesetze-im-internet.de/burlg/__7.html))

Kann der Urlaub wegen Beendigung des Arbeitsverhältnisses ganz oder teilweise nicht mehr gewährt werden, ist er **abzugelten**. Merkmale:

- Der Abgeltungsanspruch entsteht **erst mit der Beendigung** und ist ein reiner Geldanspruch.
- Eine Abgeltung im **laufenden** Arbeitsverhältnis ist unzulässig; sie erfüllt den Urlaubsanspruch nicht.
- Der Anspruch ist **vererblich**: Endet das Arbeitsverhältnis durch Tod des Arbeitnehmers, steht der Abgeltungsanspruch den Erben zu (EuGH, Urt. v. 06.11.2018 – C-569/16 und C-570/16, *Bauer* und *Willmeroth*; [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=06.11.2018&Aktenzeichen=C-569/16)).
- Bemessung nach [§ 11 BUrlG](https://www.gesetze-im-internet.de/burlg/__11.html): durchschnittlicher Arbeitsverdienst der letzten **13 Wochen** vor Urlaubsbeginn, ohne zusätzlich für Überstunden gezahltes Entgelt.

**Berechnungsformel:**

```
Urlaubsentgelt je Tag = (Bruttoentgelt der letzten 13 Wochen)
                        ÷ (Arbeitstage in diesen 13 Wochen)

Abgeltung = Urlaubsentgelt je Tag × offene Urlaubstage
```

- **Freistellung:** Eine Freistellung erfüllt den Urlaubsanspruch nur, wenn sie **unwiderruflich** erfolgt und der Urlaub konkret bezeichnet ist. Die verbreitete Formel „unter Anrechnung sämtlicher Urlaubsansprüche" bei widerruflicher Freistellung erfüllt den Anspruch **nicht**.
- **Kürzung bei Elternzeit:** Nach § 17 Abs. 1 BEEG kann der Arbeitgeber den Urlaub für jeden vollen Kalendermonat der Elternzeit um ein Zwölftel kürzen — durch **ausdrückliche Erklärung** und nur, solange das Arbeitsverhältnis besteht.

## Quellen

### Statute

- [§ 1 BUrlG](https://www.gesetze-im-internet.de/burlg/__1.html), [§ 3 BUrlG](https://www.gesetze-im-internet.de/burlg/__3.html), [§ 7 BUrlG](https://www.gesetze-im-internet.de/burlg/__7.html), [§ 9 BUrlG](https://www.gesetze-im-internet.de/burlg/__9.html), [§ 11 BUrlG](https://www.gesetze-im-internet.de/burlg/__11.html), [§ 13 BUrlG](https://www.gesetze-im-internet.de/burlg/__13.html)
- [§ 195 BGB](https://www.gesetze-im-internet.de/bgb/__195.html), [§ 199 BGB](https://www.gesetze-im-internet.de/bgb/__199.html)
- [§ 17 BEEG](https://www.gesetze-im-internet.de/beeg/__17.html)
- Richtlinie 2003/88/EG über bestimmte Aspekte der Arbeitszeitgestaltung, insbesondere Art. 7; Art. 31 Abs. 2 GRCh

### Kommentare

- Gallner, in: ErfK, 24. Aufl. 2024, § 7 BUrlG Rn. 1 ff.
- Neumann / Fenski / Kühn, BUrlG, 12. Aufl. 2021, § 7 Rn. 1 ff.
- Arnold / Zeh, Urlaubsrecht, 2. Aufl. 2023, Kap. 5 (Verfall und Verjährung)
- Düwell, in: BeckOK Arbeitsrecht, § 7 BUrlG Rn. 40 ff.

### Rechtsprechung

- EuGH, Urt. v. 06.11.2018 – C-619/16, *Kreuziger* (Art. 7 RL 2003/88/EG; kein automatischer Verfall allein wegen unterbliebenen Urlaubsantrags), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=06.11.2018&Aktenzeichen=C-619/16)
- EuGH, Urt. v. 06.11.2018 – C-684/16, *Max-Planck-Gesellschaft/Shimizu* (Art. 7 RL 2003/88/EG i.V.m. der Grundrechtecharta; Arbeitgeber muss klar und rechtzeitig über den drohenden Verfall aufklären), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=06.11.2018&Aktenzeichen=C-684/16)
- BAG, Urt. v. 19.02.2019 – 9 AZR 541/15, NZA 2019, 982 (Umsetzung der Mitwirkungsobliegenheiten zu § 7 BUrlG: individuelle Aufforderung, Angabe der Tage, Verfallhinweis), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BAG&Datum=19.02.2019&Aktenzeichen=9%20AZR%20541/15)
- BAG, Urt. v. 20.12.2022 – 9 AZR 266/20, NZA 2023, 683 (Verjährung des Urlaubsanspruchs; Verjährungsbeginn erst nach Erfüllung der Obliegenheiten), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BAG&Datum=20.12.2022&Aktenzeichen=9%20AZR%20266/20)
- EuGH, Urt. v. 22.11.2011 – C-214/10, *KHS/Schulte* (zeitliche Begrenzung der Ansammlung bei Langzeiterkrankung; Übertragungszeitraum von 15 Monaten unionsrechtlich zulässig), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=22.11.2011&Aktenzeichen=C-214/10)
- EuGH, Urt. v. 06.11.2018 – C-569/16 und C-570/16, *Bauer* und *Willmeroth* (Vererblichkeit des Urlaubsabgeltungsanspruchs), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=06.11.2018&Aktenzeichen=C-569/16)
- st. Rspr. des BAG zur Abgrenzung von gesetzlichem Urlaub und vertraglichem Mehrurlaub `[unverifiziert – prüfen]`

> Aktenzeichen und Rechtssachennummern sind vor Verwendung in juris, Beck-Online, [curia.europa.eu](https://curia.europa.eu) oder der [BAG-Entscheidungsdatenbank](https://www.bundesarbeitsgericht.de/entscheidungen/) zu ermitteln.

## Ausgabeformat

```
URLAUBSANSPRUCH — <Mandat-ID> — <Datum>
VERTRAULICH — MANDATSGEHEIMNIS — § 43a Abs. 2 BRAO

Gesamtbefund: [🟢 Ansprüche erfüllt / 🟡 offene Tage / 🔴 kumulierter
               Altbestand]

I.    Vertragsdaten                   Eintritt <Datum>, Austritt <Datum>
      Arbeitstage/Woche:              <N>   Umrechnung: 24 × N/6 = <N> Tage
      Vertraglicher Urlaub:           <N> Tage
      davon gesetzlich / Mehrurlaub:  <N> / <N>
      Mehrurlaub eigenständig geregelt: [🟢 ja — Klausel <…> / 🔴 nein]
II.   Urlaubskonto
      Jahr | Anspruch | genommen | offen | Hinweis erteilt? | Status
      2023 |    30    |    18    |  12   |  🔴 nein         | fortbestehend
      2024 |    30    |    22    |   8   |  🔴 nein         | fortbestehend
      2025 |    30    |    25    |   5   |  🟢 12.10.2025   | verfallen
III.  Krankheitszeiten                <Zeiträume>
      Durchgehende AU:                [ja / nein]
      15-Monats-Frist                 Jahr <J> → Verfall am 31.03.<J+2>
IV.   Erkrankung im Urlaub § 9 BUrlG  <N> Tage gutzuschreiben
V.    Elternzeitkürzung § 17 BEEG     [N/A / erklärt am <Datum>, <N> Zwölftel]
VI.   Verjährung §§ 195, 199 BGB      [nicht angelaufen / Ablauf <Datum>]
VII.  Ausschlussfristen               [keine / Stufe 1 bis <Datum>]
VIII. Abgeltung § 7 Abs. 4 BUrlG
      Offene Tage gesamt:             <N>
      Urlaubsentgelt je Tag (§ 11):   <Betrag>
      Abgeltungsbetrag:               <Betrag> brutto
IX.   Freistellungserklärung          [unwiderruflich — erfüllt /
                                       widerruflich — erfüllt NICHT]

Offene Tatsachenfragen: <Nachweis der Hinweisschreiben?>
Empfehlung: <…>
```

## Risiken / typische Fehler

- **Automatischer Verfall zum 31.03. angenommen** — ohne erfüllte Hinweis- und Aufforderungsobliegenheit verfällt der gesetzliche Urlaub nicht; der Altbestand kumuliert.
- **Hinweis nur per Aushang oder Rundmail erteilt** — erforderlich ist die **individuelle** Mitteilung mit konkreter Tageszahl.
- **Kein Nachweis der Hinweisschreiben** — die Beweislast trägt der Arbeitgeber; ohne Rücklauf zur Personalakte ist der Verfall nicht darlegbar.
- **Verjährung ab dem Urlaubsjahr gerechnet** — die Frist läuft erst nach Erfüllung der Obliegenheiten an.
- **15-Monats-Frist auf Fälle ohne durchgehende Arbeitsunfähigkeit angewandt** — bei zeitweiser Arbeitsfähigkeit bleibt es beim Obliegenheitsmaßstab.
- **Mehrurlaub nicht eigenständig geregelt** — dann gilt für ihn das gesamte unionsrechtliche Regime, einschließlich Verfallschutz und Abgeltung.
- **Widerrufliche Freistellung „unter Anrechnung des Urlaubs"** — erfüllt den Urlaubsanspruch nicht; die Tage bleiben offen und sind abzugelten.
- **Abgeltung im laufenden Arbeitsverhältnis vereinbart** — unzulässig; der Urlaubsanspruch bleibt bestehen, die Zahlung wird zur Zusatzleistung.
- **Elternzeitkürzung nach Beendigung erklärt** — die Kürzung nach § 17 Abs. 1 BEEG setzt ein bestehendes Arbeitsverhältnis voraus.
- **Umrechnung bei Teilzeitwechsel rückwirkend vorgenommen** — bereits entstandener Urlaub darf nicht nachträglich gekürzt werden.
- **Ausschlussfristen beim Abgeltungsanspruch übersehen** — der Geldanspruch unterliegt anders als der Urlaubsanspruch selbst regelmäßig den vertraglichen Verfallklauseln.
