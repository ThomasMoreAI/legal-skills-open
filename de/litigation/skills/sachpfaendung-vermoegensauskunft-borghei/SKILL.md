---
name: sachpfaendung-vermoegensauskunft-borghei
title: /zwangsvollstreckung:sachpfaendung-vermoegensauskunft
description: Zugriff auf bewegliche Sachen und Aufklärung der Vermögenslage – Sachpfändung §§ 803 ff. ZPO mit Pfändungspfandrecht und Verwertung, unpfändbare Sachen § 811 ZPO und Austauschpfändung § 811a ZPO, Taschenpfändung § 808 ZPO, Vermögensauskunft § 802c ZPO nebst Vermögensverzeichnis, Fremdauskünfte § 802l ZPO, Haftbefehl § 802g ZPO, Eintragung in das Schuldnerverzeichnis § 882b ZPO und Löschung § 882e ZPO sowie die Drittwiderspruchsklage § 771 ZPO. Use when ein Gerichtsvollzieherauftrag vorbereitet, eine Vermögensauskunft erzwungen oder abgegeben, eine Pfändung unpfändbarer Sachen gerügt oder das Eigentum eines Dritten an gepfändeten Sachen verteidigt wird.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/zwangsvollstreckung/skills/sachpfaendung-vermoegensauskunft
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: litigation
language: de
---

# /zwangsvollstreckung:sachpfaendung-vermoegensauskunft

## Zweck

Die Sachpfändung bringt selten Geld — sie bringt **Information**. Wirtschaftlich liegt der Wert des Gerichtsvollzieherauftrags in der Vermögensauskunft, in den Fremdauskünften und in dem Druck, den die Eintragung im Schuldnerverzeichnis erzeugt. Wer den Auftrag als reinen Verwertungsversuch begreift, verschenkt genau den Teil, der die Anschlussvollstreckung überhaupt erst möglich macht. Dieser Skill baut den Auftrag als Aufklärungs- und Zugriffsinstrument, prüft auf Schuldnerseite die Pfändungsverbote und ordnet die Drittwiderspruchsklage ein.

## Eingaben

- **Titel, Klausel, Zustellung** — geprüft nach `/zwangsvollstreckung:vollstreckungsvoraussetzungen`
- **Forderungsaufstellung** mit Hauptforderung, Zinsen, Kosten und Teilzahlungen
- Bekannte **Anschrift** des Schuldners; bei Firmen die ladungsfähige Anschrift und die Vertretungsverhältnisse
- Bekannte **Vermögensgegenstände**: Fahrzeug (mit Kennzeichen), Wertgegenstände, Bargeld, Geschäftsausstattung
- Bereits vorliegende **Vermögensauskunft**: Datum, Inhalt, Sperrfrist
- Auf Schuldnerseite: Angaben zu **Berufsausübung**, Haushalt, Unterhaltsberechtigten, Behinderung
- Bei Drittwiderspruch: **Eigentumsnachweis** des Dritten (Kaufvertrag, Sicherungsübereignung, Leasingvertrag, Eigentumsvorbehalt)

## Sub-Agent-Architektur

1. **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) beschafft §§ 802a–882h ZPO mit URL sowie Kommentarstellen (Zöller, Musielak/Voit, Kindl/Meller-Hannich) und die Rechtsprechung zu § 811 ZPO.
2. **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) erstellt Gerichtsvollzieherauftrag, Erinnerung oder Drittwiderspruchsklage.
3. **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft Pfändungsverbote, Sperrfristen, Haftbefehlsvoraussetzungen und die Zuordnung des Rechtsbehelfs.

## Ablauf

### 1. Sachpfändung ([§ 803 ZPO](https://www.gesetze-im-internet.de/zpo/__803.html), [§ 808 ZPO](https://www.gesetze-im-internet.de/zpo/__808.html))

Die Zwangsvollstreckung in bewegliche Sachen erfolgt durch **Pfändung** des Gerichtsvollziehers. Sie begründet ein **Pfändungspfandrecht** (§ 804 ZPO) mit dem Rang seiner Entstehung; mehrere Pfändungen stehen im Verhältnis der Priorität. Der Gerichtsvollzieher pfändet Sachen, die sich im **Gewahrsam des Schuldners** befinden, indem er sie in Besitz nimmt oder — bei Belassung im Gewahrsam — durch Anlegen des Pfandsiegels kenntlich macht (§ 808 ZPO). Bargeld, Kostbarkeiten und Wertpapiere nimmt er stets an sich.

Zwei gesetzliche Schranken begrenzen den Zugriff:

- **Verbot der Überpfändung** (§ 803 Abs. 1 S. 2 ZPO): Nicht mehr pfänden, als zur Befriedigung des Gläubigers und zur Deckung der Kosten erforderlich ist.
- **Verbot der zwecklosen Pfändung** (§ 803 Abs. 2 ZPO): Die Pfändung unterbleibt, wenn kein Überschuss über die Kosten der Vollstreckung zu erwarten ist. Das ist der Grund, weshalb Gebrauchtmöbel und Elektronik praktisch nie gepfändet werden.

Sachen im Gewahrsam **Dritter** dürfen nur gepfändet werden, wenn der Dritte zur Herausgabe bereit ist (§ 809 ZPO). Die Verwertung erfolgt durch **öffentliche Versteigerung** oder freihändigen Verkauf (§§ 814, 817, 825 ZPO); Wohnungsdurchsuchungen bedürfen ohne Einwilligung einer richterlichen **Durchsuchungsanordnung** ([§ 758a ZPO](https://www.gesetze-im-internet.de/zpo/__758a.html)).

### 2. Unpfändbare Sachen ([§ 811 ZPO](https://www.gesetze-im-internet.de/zpo/__811.html))

§ 811 ZPO schützt die Führung eines bescheidenen Haushalts und die Erwerbstätigkeit. Unpfändbar sind unter anderem:

- Sachen des persönlichen Gebrauchs und des **Haushalts**, insbesondere Kleidung, Wäsche, Betten, Haus- und Küchengerät, soweit der Schuldner ihrer zu einer bescheidenen Lebens- und Haushaltsführung bedarf,
- Gegenstände, die zur Fortsetzung der **Erwerbstätigkeit** erforderlich sind (Werkzeug, Berufskleidung, bei Angewiesenheit auch das Fahrzeug),
- Sachen zur **Berufsausbildung**, zum Gottesdienst, Erinnerungsstücke und Ehrenzeichen,
- Hilfsmittel, die wegen **Körperverletzung oder Behinderung** benötigt werden,
- Haustiere im häuslichen Bereich, die nicht zu Erwerbszwecken gehalten werden,
- Nahrungs-, Feuerungs- und Beleuchtungsmittel bzw. Geldbeträge für einen bestimmten Zeitraum.

Maßstab ist stets die **Erforderlichkeit im konkreten Fall**, nicht eine abstrakte Liste. Wird eine unpfändbare Sache gleichwohl gepfändet, ist die Pfändung mit der **Erinnerung** nach [§ 766 ZPO](https://www.gesetze-im-internet.de/zpo/__766.html) anzugreifen — nicht mit der Vollstreckungsabwehrklage.

### 3. Austauschpfändung ([§ 811a ZPO](https://www.gesetze-im-internet.de/zpo/__811a.html))

Die Pfändung einer nach § 811 ZPO unpfändbaren Sache kann zugelassen werden, wenn der Gläubiger dem Schuldner **Ersatz** für ein Ersatzstück oder den zu dessen Beschaffung erforderlichen **Geldbetrag** überlässt und der Wert der Sache erheblich über dem Ersatz liegt. Zuständig ist das **Vollstreckungsgericht** auf Antrag des Gläubigers; der Gerichtsvollzieher darf die Austauschpfändung nur aufgrund dieser Anordnung vornehmen. Typischer Fall ist das hochwertige Fahrzeug eines Berufspendlers, das durch einen Gebrauchtwagen einfacher Klasse ersetzt wird. Praktisch selten, aber das einzige Mittel gegen bewusst in unpfändbare Gegenstände verlagertes Vermögen.

### 4. Vermögensauskunft ([§ 802c ZPO](https://www.gesetze-im-internet.de/zpo/__802c.html))

Der Schuldner hat auf Verlangen des Gläubigers Auskunft über sein Vermögen zu erteilen und ein **Vermögensverzeichnis** vorzulegen. Anzugeben sind sämtliche Vermögensgegenstände einschließlich Forderungen gegen Dritte mit Grund und Beweismitteln sowie — für die Anfechtbarkeit relevant — die entgeltlichen Veräußerungen an nahestehende Personen der letzten zwei Jahre und die unentgeltlichen Leistungen der letzten vier Jahre. Der Schuldner hat die **Richtigkeit und Vollständigkeit** an Eides statt zu versichern; die falsche Versicherung ist nach § 156 StGB strafbar.

- **Ladung** durch den Gerichtsvollzieher mit einer Frist von mindestens zwei Wochen ([§ 802f ZPO](https://www.gesetze-im-internet.de/zpo/__802f.html)); der Schuldner kann die Forderung innerhalb dieser Frist noch begleichen.
- **Sperrfrist** (§ 802d ZPO): Hat der Schuldner die Auskunft innerhalb der letzten **zwei Jahre** abgegeben, ist eine erneute Abgabe nur bei glaubhaft gemachter wesentlicher Verbesserung der Vermögenslage zu verlangen. Dem neuen Gläubiger wird stattdessen das hinterlegte Vermögensverzeichnis übermittelt.
- **Fremdauskünfte** ([§ 802l ZPO](https://www.gesetze-im-internet.de/zpo/__802l.html)): Bei fruchtloser oder unterbliebener Auskunft und einer Forderung ab der gesetzlichen Mindesthöhe darf der Gerichtsvollzieher Auskünfte einholen — beim Rentenversicherungsträger zum Arbeitgeber, beim Bundeszentralamt für Steuern zu Kontenstammdaten, beim Kraftfahrt-Bundesamt zu Fahrzeugen. Das ist in der Praxis der wertvollste Ertrag des gesamten Auftrags, weil er die anschließende Forderungspfändung erst ermöglicht: `/zwangsvollstreckung:forderungspfaendung`.

### 5. Haftbefehl ([§ 802g ZPO](https://www.gesetze-im-internet.de/zpo/__802g.html))

Erscheint der Schuldner zum Termin **unentschuldigt nicht** oder verweigert er die Abgabe der Vermögensauskunft ohne Grund, ordnet das Gericht auf Antrag des Gläubigers zur Erzwingung der Abgabe **Haft** an. Der Haftbefehl wird dem Gerichtsvollzieher zur Verhaftung übergeben; die Haft dauert höchstens **sechs Monate** und endet, sobald die Auskunft erteilt ist ([§ 802j ZPO](https://www.gesetze-im-internet.de/zpo/__802j.html)). Der Haftbefehl ist **Beugemittel**, keine Strafe — er dient allein der Erzwingung. Gegen ihn ist die sofortige Beschwerde statthaft ([§ 793 ZPO](https://www.gesetze-im-internet.de/zpo/__793.html)); der Vollstreckungsschutz nach [§ 765a ZPO](https://www.gesetze-im-internet.de/zpo/__765a.html) bleibt daneben anwendbar.

### 6. Schuldnerverzeichnis ([§ 882b ZPO](https://www.gesetze-im-internet.de/zpo/__882b.html), [§ 882e ZPO](https://www.gesetze-im-internet.de/zpo/__882e.html))

Das zentrale Vollstreckungsgericht führt ein **Schuldnerverzeichnis**. Einzutragen ist der Schuldner, wenn er die Vermögensauskunft nicht abgegeben hat, wenn eine Befriedigung nach dem Inhalt des Vermögensverzeichnisses **offensichtlich nicht möglich** wäre oder wenn er nicht innerhalb eines Monats nach Abgabe die Forderung vollständig befriedigt hat. Eingetragen werden Name, Geburtsdatum, Anschrift, Aktenzeichen und Eintragungsgrund. Die **Löschung** erfolgt von Amts wegen nach Ablauf von **drei Jahren** seit dem Tag der Eintragungsanordnung oder vorher auf Antrag bei Nachweis der vollständigen Befriedigung (§ 882e ZPO).

Wirtschaftlich ist die Eintragung das schärfste Druckmittel überhaupt: Auskunfteien werten das Verzeichnis aus, Kredit, Mietvertrag und Mobilfunkvertrag werden praktisch unmöglich. Für den Schuldner ist deshalb die Zahlung binnen der Monatsfrist die entscheidende Weichenstellung.

### 7. Drittwiderspruchsklage ([§ 771 ZPO](https://www.gesetze-im-internet.de/zpo/__771.html))

Behauptet ein Dritter, ihm stehe an dem gepfändeten Gegenstand ein **die Veräußerung hinderndes Recht** zu, erhebt er Klage beim Prozessgericht des Vollstreckungsorts. Anerkannt sind insbesondere Eigentum, Anwartschaftsrecht des Vorbehaltskäufers, Sicherungseigentum (nach h.M. mit Einschränkungen) und der Besitz des Nießbrauchers; **nicht** genügt ein bloß schuldrechtlicher Anspruch. Die Klage ist eine **prozessuale Gestaltungsklage** mit dem Ziel, die Zwangsvollstreckung in den Gegenstand für unzulässig zu erklären; einstweiliger Rechtsschutz erfolgt über [§ 769 ZPO](https://www.gesetze-im-internet.de/zpo/__769.html) analog. Häufigster Praxisfall ist die Pfändung geleaster oder unter Eigentumsvorbehalt gelieferter Maschinen und Fahrzeuge in Geschäftsräumen. Vertiefung mit Abgrenzung zur Vollstreckungsabwehrklage: `/prozessrecht:vollstreckungsabwehrklage`.

## Deterministische Berechnung

Die beizutreibende Summe und die Verfahrensfristen sind Arithmetik; der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) macht **nur diese**. Ob eine Sache erforderlich im Sinne des § 811 ZPO ist, ob die Sperrfrist des § 802d ZPO greift und ob eine wesentliche Verbesserung der Vermögenslage glaubhaft gemacht ist, bleiben juristische Wertungen.

```bash
# Ladungsfrist zur Vermögensauskunft § 802f ZPO (mindestens zwei Wochen)
python -m scripts.legal_calc.cli frist --ereignis 15.01.2026 --menge 2 --einheit wochen --land BY

# Monatsfrist bis zur Eintragung ins Schuldnerverzeichnis § 882c ZPO
python -m scripts.legal_calc.cli frist --ereignis 15.01.2026 --menge 1 --einheit monate --land BY

# Zwei-Jahres-Sperrfrist der Vermögensauskunft § 802d ZPO
python -m scripts.legal_calc.cli frist --ereignis 15.01.2024 --menge 24 --einheit monate --land BY

# Verzugszinsen auf die zugrunde liegende Forderung
python -m scripts.legal_calc.cli verzugszinsen --betrag 4200 \
    --verzug-ab 01.02.2026 --bis 21.07.2026 --basiszins 01.01.2026:1.10
```

`--json` liefert die Rechenschritte samt Normzitat. **Nicht berechenbar** sind die Wertgrenzen des § 802l ZPO und der Schätzwert gepfändeter Sachen — beides ist der geltenden Fassung der Norm bzw. der Schätzung des Gerichtsvollziehers zu entnehmen.

## Quellen

### Statute

- [§ 802c ZPO](https://www.gesetze-im-internet.de/zpo/__802c.html), [§ 802d ZPO](https://www.gesetze-im-internet.de/zpo/__802d.html), [§ 802f ZPO](https://www.gesetze-im-internet.de/zpo/__802f.html), [§ 802g ZPO](https://www.gesetze-im-internet.de/zpo/__802g.html), [§ 802j ZPO](https://www.gesetze-im-internet.de/zpo/__802j.html), [§ 802l ZPO](https://www.gesetze-im-internet.de/zpo/__802l.html)
- [§ 803 ZPO](https://www.gesetze-im-internet.de/zpo/__803.html), [§ 804 ZPO](https://www.gesetze-im-internet.de/zpo/__804.html), [§ 808 ZPO](https://www.gesetze-im-internet.de/zpo/__808.html), [§ 809 ZPO](https://www.gesetze-im-internet.de/zpo/__809.html), [§ 811 ZPO](https://www.gesetze-im-internet.de/zpo/__811.html), [§ 811a ZPO](https://www.gesetze-im-internet.de/zpo/__811a.html), [§ 814 ZPO](https://www.gesetze-im-internet.de/zpo/__814.html), [§ 825 ZPO](https://www.gesetze-im-internet.de/zpo/__825.html), [§ 758a ZPO](https://www.gesetze-im-internet.de/zpo/__758a.html)
- [§ 766 ZPO](https://www.gesetze-im-internet.de/zpo/__766.html), [§ 769 ZPO](https://www.gesetze-im-internet.de/zpo/__769.html), [§ 771 ZPO](https://www.gesetze-im-internet.de/zpo/__771.html), [§ 793 ZPO](https://www.gesetze-im-internet.de/zpo/__793.html), [§ 765a ZPO](https://www.gesetze-im-internet.de/zpo/__765a.html)
- [§ 882b ZPO](https://www.gesetze-im-internet.de/zpo/__882b.html), [§ 882c ZPO](https://www.gesetze-im-internet.de/zpo/__882c.html), [§ 882e ZPO](https://www.gesetze-im-internet.de/zpo/__882e.html); [§ 156 StGB](https://www.gesetze-im-internet.de/stgb/__156.html)

### Kommentare

- Seibel, in: Zöller, ZPO, 35. Aufl. 2024, § 802c Rn. 1 ff.; § 811 Rn. 1 ff.
- Flockenhaus, in: Musielak/Voit, ZPO, 21. Aufl. 2024, § 811 Rn. 1 ff.; § 811a Rn. 1 ff.
- Kindl/Meller-Hannich, Gesamtes Recht der Zwangsvollstreckung, 4. Aufl. 2021, § 802c ZPO Rn. 1 ff.
- Lackmann, Zwangsvollstreckungsrecht, 12. Aufl. 2021, Rn. 1 ff. (Sachvollstreckung, Drittwiderspruch)

### Rechtsprechung

- Zur Auslegung der Erforderlichkeit im Rahmen des § 811 ZPO, insbesondere zum Fahrzeug des auf Mobilität angewiesenen Schuldners, ist die einschlägige BGH- und LG-Rechtsprechung heranzuziehen `[unverifiziert - prüfen]`.
- Zur Reichweite des die Veräußerung hindernden Rechts nach § 771 ZPO bei Sicherungseigentum und Eigentumsvorbehalt ist die st. Rspr. des BGH heranzuziehen `[unverifiziert - prüfen]`.
- Zu den Voraussetzungen der erneuten Vermögensauskunft innerhalb der Sperrfrist des § 802d ZPO ist die einschlägige BGH-Rechtsprechung heranzuziehen `[unverifiziert - prüfen]`. Kein Aktenzeichen ohne eigene Verifikation in juris / Beck-Online übernehmen.

## Formulierungshilfe — Gerichtsvollzieherauftrag, Erinnerung, Drittwiderspruch

```
An den Gerichtsvollzieher bei dem Amtsgericht <Ort>

Vollstreckungsauftrag (Modul: Sachpfändung, Vermögensauskunft,
Fremdauskünfte)

Gläubigerin: <…>    Schuldner: <…>, geb. <…>, wohnhaft <…>
Titel: <…> nebst vollstreckbarer Ausfertigung, zugestellt am <Datum>
Gesamtforderung: <Betrag> EUR (Haupt <…>, Zinsen <…>, Kosten <…>)

Beauftragt wird:
1. die gütliche Erledigung zu versuchen (§ 802b ZPO); einer
   Ratenzahlung wird nur bei monatlich mindestens <Betrag> EUR zugestimmt;
2. die Pfändung beweglicher Sachen (§§ 803, 808 ZPO), insbesondere des
   Fahrzeugs <Marke, Kennzeichen>; die Pfändungsverbote des § 811 ZPO sind
   zu beachten;
3. die Abnahme der Vermögensauskunft (§ 802c ZPO) und die Ladung hierzu;
4. bei fruchtloser oder unterbliebener Auskunft die Einholung der
   Fremdauskünfte nach § 802l ZPO (Rentenversicherung, Bundeszentralamt
   für Steuern, Kraftfahrt-Bundesamt);
5. bei unentschuldigtem Ausbleiben die Beantragung eines Haftbefehls
   (§ 802g ZPO).

Die Übermittlung eines bereits hinterlegten Vermögensverzeichnisses nach
§ 802d Abs. 1 S. 2 ZPO wird ausdrücklich beantragt.
```

```
Erinnerung nach § 766 ZPO gegen die Pfändung unpfändbarer Sachen

Namens des Schuldners wende ich mich gegen die Pfändung vom <Datum>,
soweit sie folgende Gegenstände erfasst: <Aufzählung>.

Der Pkw <Marke, Kennzeichen> ist nach § 811 Abs. 1 Nr. 5 ZPO unpfändbar.
Der Schuldner ist als <Beruf> auf das Fahrzeug angewiesen; der
Arbeitsort ist mit öffentlichen Verkehrsmitteln nicht in zumutbarer Zeit
erreichbar (Anlage). Die Waschmaschine dient der bescheidenen
Haushaltsführung eines Vier-Personen-Haushalts.

Es wird beantragt, die Pfändung insoweit aufzuheben und die
Zwangsvollstreckung bis zur Entscheidung einstweilen einzustellen.
```

```
Drittwiderspruchsklage (§ 771 ZPO)

Es wird beantragt, die Zwangsvollstreckung der Beklagten aus dem Titel
<…> in die am <Datum> vom Gerichtsvollzieher <…> gepfändete Maschine
<Typ, Seriennummer> für unzulässig zu erklären.

Die Klägerin ist Eigentümerin der Maschine. Sie hat sie der Schuldnerin
mit Vertrag vom <Datum> unter Eigentumsvorbehalt geliefert; der Kaufpreis
ist nur zu <…> % gezahlt (Anlagen K1–K3). Damit steht der Klägerin ein
die Veräußerung hinderndes Recht zu.
```

## Ausgabeformat

```
SACHPFÄNDUNG / VERMÖGENSAUSKUNFT — <Gläubiger / Schuldner / Dritter> — <Datum>

I.    Vollstreckungsvoraussetzungen  Titel/Klausel/Zustellung [✅ / ❌]
II.   Forderung                      Haupt <…> + Zinsen <…> + Kosten <…>
III.  Sachpfändung §§ 803, 808 ZPO   Gegenstände: <…>
      - Überpfändung § 803 I 2       [✅ / 🔴]
      - Zwecklosigkeit § 803 II      [Verwertungsüberschuss zu erwarten?]
      - Gewahrsam Dritter § 809      [N/A / Herausgabebereitschaft]
      - Durchsuchung § 758a ZPO      [Einwilligung / Anordnung]
IV.   Unpfändbare Sachen § 811 ZPO   Betroffen: <…>
      Rechtsbehelf                   Erinnerung § 766 ZPO, Frist: —
V.    Austauschpfändung § 811a ZPO   [N/A / Antrag beim Vollstreckungsgericht]
VI.   Vermögensauskunft § 802c ZPO   Ladung <Datum>, Termin <Datum>
      - Sperrfrist § 802d ZPO        letzte Auskunft <Datum>, frei ab <Datum>
      - Vermögensverzeichnis         [angefordert / vorliegend]
      - Fremdauskünfte § 802l ZPO    [beantragt: RV / BZSt / KBA]
VII.  Haftbefehl § 802g ZPO          [N/A / beantragt / erlassen am <Datum>]
      Höchstdauer                    sechs Monate, § 802j ZPO
VIII. Schuldnerverzeichnis § 882b    [keine Eintragung / Eintragung <Datum>]
      Löschung § 882e ZPO            drei Jahre, Ende: <Datum>
IX.   Drittwiderspruch § 771 ZPO     [N/A / Recht des Dritten: <…>]
      Einstweiliger Rechtsschutz     § 769 ZPO analog
X.    Fristen / Zinsen               s. Deterministische Berechnung

Ergebnis: <auftragsreif / Pfändung teilweise aufzuheben / Klage geboten>
Risiko: [🟢 / 🟡 / 🔴]
```

## Risiken / typische Fehler

- **Auftrag nur auf Sachpfändung gerichtet** — der wirtschaftliche Wert liegt in Vermögensauskunft und Fremdauskünften nach § 802l ZPO; ohne diese Module bleibt der Auftrag meist fruchtlos.
- **Unpfändbare Sachen gepfändet** — § 811 ZPO schützt Haushaltsführung und Erwerbstätigkeit; der Angriff erfolgt mit der Erinnerung § 766 ZPO, nicht mit der Vollstreckungsabwehrklage.
- **Austauschpfändung ohne Anordnung** — der Gerichtsvollzieher darf nach § 811a ZPO nur aufgrund einer Anordnung des Vollstreckungsgerichts austauschpfänden.
- **Sperrfrist § 802d ZPO übersehen** — innerhalb von zwei Jahren wird nur das hinterlegte Vermögensverzeichnis übermittelt; eine erneute Abgabe setzt die glaubhaft gemachte Verbesserung der Vermögenslage voraus.
- **Haftbefehl als Strafe missverstanden** — § 802g ZPO ist Beugemittel; die Haft endet mit Abgabe der Auskunft, und § 765a ZPO bleibt daneben anwendbar.
- **Monatsfrist bis zur Eintragung ins Schuldnerverzeichnis verstreichen lassen** — die Eintragung wirkt drei Jahre und schneidet Kredit, Miete und Verträge ab; die Zahlung binnen Monatsfrist ist die entscheidende Weichenstellung.
- **Drittwiderspruch auf schuldrechtlichen Anspruch gestützt** — § 771 ZPO verlangt ein die Veräußerung hinderndes Recht; ein bloßer Herausgabeanspruch aus Vertrag genügt nicht.
