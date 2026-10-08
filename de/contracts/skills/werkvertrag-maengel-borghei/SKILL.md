---
name: werkvertrag-maengel-borghei
title: /vertragsrecht:werkvertrag-maengel
description: Prüfung werkvertraglicher Mängelrechte und Beendigungsrechte nach §§ 631–650v BGB – Abnahme § 640 BGB einschließlich fiktiver Abnahme § 640 Abs. 2 BGB, Rechtekatalog § 634 BGB, Selbstvornahme und Vorschuss § 637 BGB, Verjährung § 634a BGB, freie Kündigung § 648 BGB und Kündigung aus wichtigem Grund § 648a BGB sowie Verbraucherbauvertrag §§ 650i ff. BGB mit Widerrufsrecht § 650l BGB. Use when ein Werk mangelhaft ist, die Abnahme streitig ist oder ein Werk- oder Bauvertrag vorzeitig beendet werden soll.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/vertragsrecht/skills/werkvertrag-maengel
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: contracts
language: de
---

# /vertragsrecht:werkvertrag-maengel

## Zweck

Im Werkvertragsrecht entscheidet ein einziger Zeitpunkt fast alles: die **Abnahme**. Sie bewirkt Fälligkeit der Vergütung, Gefahrübergang, Beweislastumkehr zulasten des Bestellers und Verjährungsbeginn. Dieser Skill bestimmt zuerst den Abnahmestatus — einschließlich der oft übersehenen **fiktiven Abnahme** nach [§ 640 Abs. 2 BGB](https://www.gesetze-im-internet.de/bgb/__640.html) — und arbeitet dann den Rechtekatalog des [§ 634 BGB](https://www.gesetze-im-internet.de/bgb/__634.html) sowie die Beendigungsrechte ab.

## Eingaben

- Vertragstyp: allgemeiner Werkvertrag, Bauvertrag (§§ 650a ff. BGB), Verbraucherbauvertrag (§§ 650i ff. BGB), Architekten-/Ingenieurvertrag (§§ 650p ff. BGB), Bauträgervertrag (§§ 650u, 650v BGB); VOB/B einbezogen?
- Leistungsbeschreibung, Vergütung (Pauschale / Einheitspreise / Stundenlohn), Fertigstellungstermin
- Abnahmestatus: förmliche Abnahme, konkludente Abnahme, Abnahmeverweigerung, Fertigstellungsanzeige mit Datum
- Mangelbeschreibung; Wesentlichkeit; Vorbehalt bei Abnahme erklärt?
- Bereits gesetzte Fristen, Zahlungen, Abschlagszahlungen (§ 632a BGB), Sicherheiten
- Bei Beendigungsabsicht: Kündigungsgrund, bereits erbrachte Leistungen, ersparte Aufwendungen

## Sub-Agent-Architektur

1. **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) liefert Statute (BGB Werkvertragsrecht, ggf. VOB/B als AGB), Kommentarstellen (Messerschmidt/Voit, Kniffka/Koeble, MüKoBGB) und Rechtsprechung mit Verifikationsmarker.
2. **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) prüft Abnahme → Mangel → Rechtekatalog → Fristsetzung → Sekundärrechte → Verjährung → Beendigung und entwirft Mängelrüge, Fristsetzung und Kündigung.
3. **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft Abnahmewirkungen, Verjährung § 634a BGB, Schriftform der Kündigung (§ 650h BGB) und Quellenmarker.

## Ablauf

### 1. Vertragstypologie und anwendbares Regime ([§ 631 BGB](https://www.gesetze-im-internet.de/bgb/__631.html))

Der Werkvertrag schuldet einen **Erfolg**, nicht bloß ein Tätigwerden — Abgrenzung zum Dienstvertrag (§ 611 BGB) und zum Kaufvertrag mit Montageverpflichtung. Prüfe der Reihe nach, ob eines der Sonderregime greift:

- **Bauvertrag** §§ 650a ff. BGB: Herstellung, Wiederherstellung, Beseitigung oder Umbau eines Bauwerks — mit Anordnungsrecht § 650b BGB, Vergütungsanpassung § 650c BGB, Zustandsfeststellung § 650g BGB, **Schriftform der Kündigung § 650h BGB**.
- **Verbraucherbauvertrag** §§ 650i ff. BGB (siehe Ziff. 7).
- **Architekten- und Ingenieurvertrag** §§ 650p ff. BGB mit Zielfindungsphase und Sonderkündigungsrecht § 650r BGB.
- **VOB/B**: gilt nur bei wirksamer Einbeziehung; gegenüber Verbrauchern ist die VOB/B als Ganzes der Inhaltskontrolle nach §§ 307 ff. BGB unterworfen.

### 2. Abnahme ([§ 640 BGB](https://www.gesetze-im-internet.de/bgb/__640.html))

Der Besteller ist verpflichtet, das **vertragsgemäß hergestellte** Werk abzunehmen. Er darf die Abnahme wegen **unwesentlicher** Mängel nicht verweigern (§ 640 Abs. 1 S. 2 BGB).

Wirkungen der Abnahme:

- Fälligkeit der Vergütung ([§ 641 Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__641.html))
- Gefahrübergang (§ 644 BGB)
- **Umkehr der Beweislast** für die Mangelfreiheit auf den Besteller
- Beginn der Verjährung der Mängelansprüche (§ 634a Abs. 2 BGB)
- Verlust der Mängelrechte bei vorbehaltloser Abnahme trotz Kenntnis des Mangels (§ 640 Abs. 3 BGB) — **Vorbehalt bei der Abnahme protokollieren**

### 3. Fiktive Abnahme ([§ 640 Abs. 2 BGB](https://www.gesetze-im-internet.de/bgb/__640.html))

Als abgenommen gilt ein Werk auch dann, wenn der Unternehmer dem Besteller nach Fertigstellung des Werks eine **angemessene Frist zur Abnahme** gesetzt hat und der Besteller die Abnahme nicht innerhalb dieser Frist **unter Angabe mindestens eines Mangels** verweigert hat.

- Ist der Besteller ein **Verbraucher**, treten die Wirkungen der fiktiven Abnahme nur ein, wenn der Unternehmer ihn zusammen mit der Aufforderung zur Abnahme auf die Folgen einer nicht erklärten oder ohne Angabe von Mängeln verweigerten Abnahme **in Textform hingewiesen** hat (§ 640 Abs. 2 S. 2 BGB).
- Für den Unternehmer ist das der schnellste Weg zur Fälligkeit; für den Besteller die häufigste Falle. **Ein einziger benannter Mangel genügt**, um die Fiktion zu verhindern — er muss nicht wesentlich und nicht berechtigt sein.

**Formulierungshilfe (Unternehmerseite):** „Die Leistungen aus dem Vertrag vom [Datum] sind seit dem [Datum] fertiggestellt. Ich fordere Sie hiermit zur Abnahme bis zum **[Datum]** auf. **Hinweis nach § 640 Abs. 2 S. 2 BGB:** Erklären Sie die Abnahme nicht bis zum genannten Datum und verweigern Sie sie nicht unter Angabe mindestens eines Mangels, gilt das Werk mit Fristablauf als abgenommen."

### 4. Rechtekatalog bei Mängeln ([§ 634 BGB](https://www.gesetze-im-internet.de/bgb/__634.html))

| Nr. | Recht | Norm |
|---|---|---|
| 1 | Nacherfüllung | § 635 BGB — **Wahlrecht des Unternehmers** zwischen Beseitigung und Neuherstellung |
| 2 | Selbstvornahme und Aufwendungsersatz | § 637 BGB |
| 3 | Rücktritt / Minderung | §§ 636, 323, 326 Abs. 5 BGB / § 638 BGB |
| 4 | Schadensersatz / Aufwendungsersatz | §§ 280, 281, 283, 311a BGB / § 284 BGB |

Unterschied zum Kaufrecht beachten: Das **Wahlrecht bei der Nacherfüllung steht dem Unternehmer zu** (§ 635 Abs. 1 BGB), nicht dem Besteller. Ein Mangel liegt vor, wenn das Werk nicht die vereinbarte Beschaffenheit hat oder sich nicht für die vorausgesetzte bzw. gewöhnliche Verwendung eignet (§ 633 BGB); dazu zählen auch die **anerkannten Regeln der Technik**.

### 5. Selbstvornahme und Vorschuss ([§ 637 BGB](https://www.gesetze-im-internet.de/bgb/__637.html))

Nach **fruchtlosem Ablauf einer angemessenen Frist** zur Nacherfüllung kann der Besteller den Mangel selbst beseitigen und Ersatz der erforderlichen Aufwendungen verlangen (§ 637 Abs. 1 BGB). Entbehrlich ist die Frist bei berechtigter Verweigerung der Nacherfüllung durch den Unternehmer sowie in den Fällen des § 636 BGB.

**Praktisch entscheidend ist § 637 Abs. 3 BGB: Vorschussanspruch.** Der Besteller kann von dem Unternehmer für die zur Beseitigung des Mangels erforderlichen Aufwendungen **Vorschuss** verlangen. Er muss die Sanierung also nicht vorfinanzieren. Über den Vorschuss ist nach Durchführung **abzurechnen**; nicht verbrauchte Beträge sind zurückzuzahlen.

### 6. Verjährung ([§ 634a BGB](https://www.gesetze-im-internet.de/bgb/__634a.html))

| Werk | Frist | Beginn |
|---|---|---|
| Bauwerk; Planungs- oder Überwachungsleistung hierfür | 5 Jahre | Abnahme |
| Werk, dessen Erfolg in der Herstellung/Wartung/Veränderung einer Sache oder in Planungsleistungen dafür besteht | 2 Jahre | Abnahme |
| Sonstige Werke (z. B. unkörperliche Erfolge) | Regelverjährung §§ 195, 199 BGB | Schluss des Kenntnisjahres |
| Arglistiges Verschweigen | Regelverjährung, mindestens aber die o.g. Frist | § 634a Abs. 3 BGB |

**Ohne Abnahme beginnt die Verjährung nicht** — der Unternehmer kann Jahre später noch in Anspruch genommen werden, wenn er die Abnahme nie herbeigeführt hat.

### 7. Verbraucherbauvertrag ([§§ 650i ff. BGB](https://www.gesetze-im-internet.de/bgb/__650i.html))

Verbraucherbauvertrag ist der Vertrag, durch den der Unternehmer von einem Verbraucher zum Bau eines **neuen Gebäudes** oder zu **erheblichen Umbaumaßnahmen** an einem bestehenden Gebäude verpflichtet wird. Pflichten des Unternehmers:

- **Baubeschreibung** in Textform vor Vertragsschluss (§ 650j BGB iVm Art. 249 EGBGB), mit verbindlichen Angaben zum Fertigstellungszeitpunkt (§ 650k Abs. 3 BGB)
- **Textform** des Vertrags (§ 650i Abs. 2 BGB)
- **Abschlagszahlungen** höchstens 90 % der Gesamtvergütung (§ 650m Abs. 1 BGB), Sicherheit für rechtzeitige Herstellung 5 % (§ 650m Abs. 2 BGB)
- **Herausgabe von Unterlagen** § 650n BGB

**Widerrufsrecht ([§ 650l BGB](https://www.gesetze-im-internet.de/bgb/__650l.html)):** Dem Verbraucher steht ein Widerrufsrecht nach § 355 BGB zu, es sei denn, der Vertrag wurde **notariell beurkundet**. Der Unternehmer muss über das Widerrufsrecht nach Art. 249 § 3 EGBGB belehren. Die Frist beträgt 14 Tage; ohne ordnungsgemäße Belehrung verlängert sie sich — Berechnung über `/vertragsrecht:verbraucherwiderruf`. Die §§ 650i ff. BGB sind **nicht abdingbar** (§ 650o BGB).

### 8. Beendigung: freie Kündigung ([§ 648 BGB](https://www.gesetze-im-internet.de/bgb/__648.html))

Der Besteller kann bis zur Vollendung des Werks **jederzeit und ohne Grund** kündigen. Rechtsfolge: Der Unternehmer behält den Anspruch auf die **vereinbarte Vergütung**, muss sich aber anrechnen lassen, was er infolge der Aufhebung des Vertrags an Aufwendungen erspart oder durch anderweitige Verwendung seiner Arbeitskraft erwirbt oder böswillig zu erwerben unterlässt. Es wird **vermutet**, dass ihm 5 % der auf den noch nicht erbrachten Teil der Werkleistung entfallenden Vergütung zustehen (§ 648 S. 3 BGB). Der Unternehmer muss die ersparten Aufwendungen **prüffähig abrechnen**.

### 9. Beendigung: Kündigung aus wichtigem Grund ([§ 648a BGB](https://www.gesetze-im-internet.de/bgb/__648a.html))

Beide Vertragsteile können aus wichtigem Grund ohne Einhaltung einer Kündigungsfrist kündigen, wenn dem kündigenden Teil die Fortsetzung des Vertragsverhältnisses bis zur Fertigstellung unzumutbar ist. Möglich ist auch die **Teilkündigung** eines abgrenzbaren Teils des Werks (§ 648a Abs. 2 BGB). Nach der Kündigung kann jeder Teil eine **gemeinsame Leistungsstandfeststellung** verlangen (§ 648a Abs. 4 BGB); verweigert eine Partei die Mitwirkung, trifft sie die Beweislast für den Leistungsstand. Der Unternehmer kann nur die Vergütung für die **bis zur Kündigung erbrachten** Leistungen verlangen (§ 648a Abs. 5 BGB).

**Bei Bauverträgen bedarf die Kündigung der schriftlichen Form ([§ 650h BGB](https://www.gesetze-im-internet.de/bgb/__650h.html))** — Textform oder E-Mail genügt nicht.

## Quellen

### Statute

- [§ 631 BGB](https://www.gesetze-im-internet.de/bgb/__631.html), [§ 632a BGB](https://www.gesetze-im-internet.de/bgb/__632a.html), [§ 634 BGB](https://www.gesetze-im-internet.de/bgb/__634.html), [§ 634a BGB](https://www.gesetze-im-internet.de/bgb/__634a.html), [§ 637 BGB](https://www.gesetze-im-internet.de/bgb/__637.html), [§ 640 BGB](https://www.gesetze-im-internet.de/bgb/__640.html), [§ 641 BGB](https://www.gesetze-im-internet.de/bgb/__641.html)
- [§ 648 BGB](https://www.gesetze-im-internet.de/bgb/__648.html), [§ 648a BGB](https://www.gesetze-im-internet.de/bgb/__648a.html)
- [§ 650i BGB](https://www.gesetze-im-internet.de/bgb/__650i.html), [§ 650l BGB](https://www.gesetze-im-internet.de/bgb/__650l.html), [§ 650u BGB](https://www.gesetze-im-internet.de/bgb/__650u.html), [§ 650v BGB](https://www.gesetze-im-internet.de/bgb/__650v.html)
- [§ 323 BGB](https://www.gesetze-im-internet.de/bgb/__323.html), [§ 280 BGB](https://www.gesetze-im-internet.de/bgb/__280.html)

### Kommentare

- Busche, in: MüKoBGB, 9. Aufl. 2023, §§ 631, 640, 648 Rn. 1 ff. `[unverifiziert – Auflagenstand prüfen]`
- Messerschmidt/Voit, Privates Baurecht, 4. Aufl. 2022, § 640 BGB Rn. 1 ff.
- Kniffka/Koeble/Jurgeleit/Sacher, Kompendium des Baurechts, 5. Aufl. 2020, Teil 4 (Abnahme) und Teil 6 (Mängelrechte)

### Rechtsprechung

- BGH, Urt. v. 22.02.2018 – VII ZR 46/17 (kein „fiktiver" Mangelbeseitigungsaufwand als Schadensersatz im Werkvertrag) `[unverifiziert – prüfen]`
- BGH, Urt. v. 25.02.2016 – VII ZR 49/15 (Vorschussanspruch § 637 Abs. 3 BGB, Abrechnungspflicht) `[unverifiziert – prüfen]`

> Beide Aktenzeichen sind vor Verwendung in juris / Beck-Online zu verifizieren. Die tragenden Aussagen dieses Skills folgen aus dem Gesetzeswortlaut.

## Ausgabeformat

```
WERKVERTRAG / MÄNGEL — <Bauvorhaben / Werk> — <Datum>

I.    Vertragstyp                      [Werkvertrag / Bauvertrag / Verbraucherbauvertrag / Architektenvertrag]
        VOB/B einbezogen:              [ja / nein]
II.   Abnahme (§ 640)                  [erfolgt am <Datum> / verweigert / fiktiv § 640 II]
        Vorbehalt erklärt:             [ja / nein — Folge § 640 III]
III.  Mangel (§ 633)                   [✅ / 🟡 / ❌ — Beschreibung]
IV.   Nacherfüllung (§ 635)            [verlangt am <Datum>, Frist bis <Datum>]
V.    Selbstvornahme (§ 637)           [möglich / Vorschuss § 637 III: <Betrag> EUR]
VI.   Rücktritt / Minderung            [§§ 636, 323 / § 638 — Betrag]
VII.  Schadensersatz (§§ 280, 281)     [dem Grunde nach / Höhe]
VIII. Verjährung (§ 634a)              [2 / 5 Jahre — Ende: <TT.MM.JJJJ>]
IX.   Verbraucherbauvertrag            [N/A / §§ 650i ff. — Widerruf § 650l bis <Datum>]
X.    Beendigung                       [§ 648 frei / § 648a wichtiger Grund / keine]
        Schriftform § 650h beachtet:   [ja / nein / N/A]

Empfohlene nächste Erklärung: <…> bis <Datum>
Gesamtbefund: [🟢 / 🟡 / 🔴]
Offene Tatsachen: <Liste>
```

## Risiken / typische Fehler

- **Fiktive Abnahme übersehen** — der Besteller lässt die Abnahmefrist verstreichen, ohne mindestens einen Mangel zu benennen; damit wird die Vergütung fällig und die Beweislast kippt (§ 640 Abs. 2 BGB).
- **Vorbehalt bei der Abnahme vergessen** — wer ein Werk trotz Kenntnis eines Mangels vorbehaltlos abnimmt, verliert Nacherfüllung, Rücktritt, Minderung und Schadensersatz (§ 640 Abs. 3 BGB).
- **Wahlrecht bei der Nacherfüllung verwechselt** — im Werkvertrag wählt der **Unternehmer** die Art der Nacherfüllung (§ 635 Abs. 1 BGB), anders als im Kaufrecht.
- **Vorschuss § 637 Abs. 3 BGB nicht geltend gemacht** — der Besteller finanziert die Sanierung unnötig vor und trägt das Insolvenzrisiko des Unternehmers.
- **Kündigung eines Bauvertrags per E-Mail** — § 650h BGB verlangt Schriftform; die Kündigung ist sonst formnichtig (§ 125 BGB).
- **Verjährung § 634a BGB falsch angeknüpft** — sie beginnt mit der Abnahme, nicht mit der Fertigstellung; ohne Abnahme läuft sie überhaupt nicht.
- **Verbraucherbauvertrag ohne Widerrufsbelehrung** geschlossen — die Widerrufsfrist des § 650l BGB läuft dann nicht an, der Verbraucher kann noch lange widerrufen.
