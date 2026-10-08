---
name: mieterhoehung-558-bgb-borghei
title: /mietrecht:mieterhoehung-558-bgb
description: 'Mieterhöhung auf die ortsübliche Vergleichsmiete nach § 558 BGB – aus beiden Perspektiven: Vermieter-Entwurf und Mieter-Wirksamkeitsprüfung. Wartezeit und Jahressperre § 558 Abs. 1 BGB, ortsübliche Vergleichsmiete § 558 Abs. 2 BGB, Kappungsgrenze § 558 Abs. 3 BGB, Begründungsmittel § 558a BGB (Mietspiegel, Sachverständigengutachten, drei Vergleichswohnungen, Mietdatenbank), qualifizierter Mietspiegel §§ 558c–558e BGB, Zustimmungs- und Klagefrist § 558b BGB, Abgrenzung zur Modernisierungsmieterhöhung § 559 BGB, Mietpreisbremse §§ 556d ff. BGB. Use when ein Vermieter ein Mieterhöhungsverlangen gestaltet oder ein Mieter ein empfangenes Verlangen auf Wirksamkeit, Höhe und Fristen prüft.'
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/mietrecht/skills/mieterhoehung-558-bgb
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: real-estate
language: de
---

# /mietrecht:mieterhoehung-558-bgb

## Zweck

Die Mieterhöhung auf die ortsübliche Vergleichsmiete ist formstreng und zweiseitig: Dasselbe Prüfprogramm entscheidet darüber, ob der Vermieter ein durchsetzbares Verlangen in der Hand hält und ob der Mieter zustimmen muss. Ein formfehlerhaftes Verlangen ist **unwirksam** — die Zustimmungspflicht entsteht nicht, die Überlegungsfrist läuft nicht an, und der Vermieter verliert im Ergebnis mindestens ein Jahr. Diese Skill führt beide Perspektiven durch dieselbe Prüfkaskade und beziffert am Ende den tatsächlich zulässigen Erhöhungsbetrag.

## Eingaben

- **Perspektive**: Vermieter-Entwurf oder Mieter-Prüfung eines empfangenen Verlangens
- Das **Verlangen** im Wortlaut (bei Mieter-Prüfung), Datum des **Zugangs**, Form (Brief / E-Mail / Textform)
- **Aktuelle Nettokaltmiete** und Datum der **letzten Mieterhöhung** bzw. des Mietbeginns
- Wohnungsfläche, Wohnlage, Baujahr, Ausstattung, energetische Beschaffenheit
- **Begründungsmittel**: Mietspiegel der Gemeinde / Sachverständigengutachten / drei Vergleichswohnungen / Mietdatenbank
- Frühere Erhöhungen der letzten drei Jahre (für die Kappungsgrenze)
- Ist der Ort **Mietpreisbremsen-Gebiet** ([§ 556d BGB](https://www.gesetze-im-internet.de/bgb/__556d.html), landesrechtliche Verordnung)?

## Sub-Agent-Architektur

Die Prüfung wird in Prosa von spezialisierten Schritten getragen; einen `agents`-Block trägt diese Skill bewusst nicht (mietrecht-Konvention). Ein **Form-Prüfer** beurteilt zuerst allein die Wirksamkeit des Verlangens — Textform, Adressierung, Begründungsmittel, Bestimmtheit — ohne jeden Blick auf die Höhe. Erst wenn das Verlangen formwirksam ist, bewertet ein **Materiell-Prüfer** die geforderte Miete an ortsüblicher Vergleichsmiete und Kappungsgrenze. Ein **Fristen-Prüfer** kontrolliert Jahressperre, 15-Monats-Frist, Überlegungs- und Klagefrist. Ein **Abgrenzungs-Prüfer** untersucht quer, ob in Wahrheit eine Modernisierungsmieterhöhung nach § 559 BGB vorliegt, die einem anderen Regime folgt. Die häufigste Fehlerquelle — Vermengung von Form- und Begründetheitsfrage — wird durch diese Trennung strukturell ausgeschlossen.

## Ablauf

### 0. Perspektive bestimmen (Vermieter-Entwurf / Mieter-Prüfung)

Der Prüfstoff ist identisch, die Blickrichtung nicht. **Vermieter-Entwurf:** Die Schritte 1–7 werden als Gestaltungsvorgaben gelesen — jeder Punkt ist eine Anforderung, die der Entwurf erfüllen muss, bevor er das Haus verlässt. Ergebnis ist ein versandfertiges Verlangen plus Fristenkalender. **Mieter-Prüfung:** Dieselben Schritte werden als Angriffspunkte gelesen — jeder Punkt ist ein möglicher Unwirksamkeitsgrund. Ergebnis ist eine Zustimmungsempfehlung (voll / teilweise / verweigern) plus Klagerisikoeinschätzung. Bei der Mieter-Prüfung gilt die strikte Reihenfolge Form vor Höhe: Ist das Verlangen formunwirksam, ist die Höhe gar nicht mehr zu prüfen. Bei der Vermieter-Perspektive gilt umgekehrt, dass die Höhe früh feststehen sollte, weil sie die Wahl des Begründungsmittels steuert.

### 1. Wartezeit und Jahressperre ([§ 558 Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__558.html))

Der Vermieter kann die Zustimmung zu einer Mieterhöhung verlangen, wenn die Miete zum Zeitpunkt des **Wirksamwerdens** der Erhöhung **seit 15 Monaten unverändert** ist (15-Monats-Frist). Das Verlangen selbst darf frühestens **12 Monate** nach der letzten Mieterhöhung zugehen (**Jahressperrfrist**). Beide Fristen sind zu trennen: Die Jahressperre betrifft den Zugang, die 15-Monats-Frist die Wirksamkeit. Erhöhungen nach §§ 559–560 BGB (Modernisierung, Betriebskosten) bleiben bei der Berechnung außer Betracht. Liegt die letzte Erhöhung weniger als ein Jahr zurück, ist das Verlangen **verfrüht und unwirksam**.

### 2. Ortsübliche Vergleichsmiete ([§ 558 Abs. 2 BGB](https://www.gesetze-im-internet.de/bgb/__558.html))

Maßgeblich sind die Entgelte, die in der Gemeinde oder einer vergleichbaren Gemeinde für **nicht preisgebundenen Wohnraum vergleichbarer Art, Größe, Ausstattung, Beschaffenheit und Lage einschließlich der energetischen Ausstattung und Beschaffenheit** in den letzten **sechs Jahren** vereinbart oder geändert worden sind. Praktisch wird die geforderte Miete gegen den einschlägigen Mietspiegelwert plausibilisiert: richtiges Feld, richtige Spanne, gültige Fassung. Für die Flächenangabe ist die **tatsächliche** Wohnfläche maßgeblich, nicht die vertraglich genannte (BGH, Urt. v. 18.11.2015 – VIII ZR 266/14, https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2015-11-18&Aktenzeichen=VIII%20ZR%20266/14). Liegt die Forderung oberhalb der Spanne, ist sie der Höhe nach unbegründet, soweit sie die ortsübliche Vergleichsmiete übersteigt.

### 3. Kappungsgrenze ([§ 558 Abs. 3 BGB](https://www.gesetze-im-internet.de/bgb/__558.html))

Unabhängig von der ortsüblichen Vergleichsmiete darf sich die Miete **innerhalb von drei Jahren um höchstens 20 %** erhöhen. In Gebieten mit gefährdeter Wohnungsversorgung gilt per landesrechtlicher Verordnung eine abgesenkte **Kappungsgrenze von 15 %**. Berechnung: Ausgangswert ist die Miete drei Jahre vor dem Wirksamwerden der Erhöhung; zwischenzeitliche Erhöhungen nach § 558 BGB werden **kumuliert angerechnet**. Erhöhungen nach §§ 559–560 BGB bleiben außer Ansatz. Übersteigt die Forderung die Kappungsgrenze, ist sie nur **bis zur Grenze** wirksam; der überschießende Teil entfällt, kann aber später erneut verlangt werden.

### 4. Begründungsmittel ([§ 558a BGB](https://www.gesetze-im-internet.de/bgb/__558a.html))

Das Verlangen ist zu **begründen**; eines der vier gesetzlichen Mittel genügt, es muss aber **bestimmt** sein:

1. **Mietspiegel** der Gemeinde — einfach oder qualifiziert ([§ 558d BGB](https://www.gesetze-im-internet.de/bgb/__558d.html)). Bei Bezugnahme müssen das einschlägige Feld und die Spanne benannt und die Wohnung konkret eingeordnet werden; ein pauschaler Verweis auf „den Mietspiegel" genügt **nicht**. Beim qualifizierten Mietspiegel greift die Vermutung des § 558d Abs. 3 BGB; sie entfällt, wenn der Mietspiegel nicht nach zwei Jahren angepasst wurde (§ 558d Abs. 2 BGB).
2. **Sachverständigengutachten** eines öffentlich bestellten oder anerkannt qualifizierten Sachverständigen — mit nachvollziehbarer Herleitung, nicht nur Ergebnis.
3. **Drei Vergleichswohnungen** mit Lage, Größe, Ausstattung und konkreter Vergleichsmiete — so bestimmt, dass der Mieter sie auffinden und nachprüfen kann.
4. **Mietdatenbank** ([§ 558e BGB](https://www.gesetze-im-internet.de/bgb/__558e.html)).

> Fehlt eine zulässige Begründung oder ist sie zu unbestimmt, ist das Verlangen **unwirksam** — eine Zustimmungspflicht entsteht nicht.

### 5. Form und Adressierung ([§ 558a Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__558a.html), [§ 126b BGB](https://www.gesetze-im-internet.de/bgb/__126b.html))

- **Textform** nach § 126b BGB: lesbare Erklärung auf dauerhaftem Datenträger, Person des Erklärenden genannt. E-Mail genügt; ein mündlicher Hinweis nicht.
- **Von allen Vermietern an alle Mieter**: Ein Verlangen an nur einen von mehreren Mietern ist unwirksam. Bei Vertretung ist die Vollmacht beizufügen (§ 174 BGB), sonst droht Zurückweisung.
- **Bestimmtheit der Forderung**: alte Miete, neue Miete, Differenz und Zeitpunkt des Wirksamwerdens ausdrücklich benennen.
- Empfehlung: Zugang durch Einwurf-Einschreiben oder Boten mit Zeugnis nachweisbar machen.

### 6. Zustimmungsfrist und Zustimmungsklage ([§ 558b BGB](https://www.gesetze-im-internet.de/bgb/__558b.html))

Der Mieter hat bis zum **Ablauf des zweiten Kalendermonats nach Zugang** Zeit zur Zustimmung (**Überlegungsfrist**). Stimmt er zu, schuldet er die erhöhte Miete **ab Beginn des dritten Kalendermonats** nach Zugang. Verweigert er oder schweigt er, kann der Vermieter **innerhalb von drei weiteren Monaten** auf Zustimmung klagen (§ 558b Abs. 2 S. 2 BGB); versäumt er diese **Klagefrist**, muss er das gesamte Verfahren neu beginnen. Ist das Verlangen nur **teilweise** begründet, sollte der Mieter in Höhe des wirksamen Teils zustimmen, um insoweit eine Klage zu vermeiden.

### 7. Abgrenzung zur Modernisierungsmieterhöhung ([§ 559 BGB](https://www.gesetze-im-internet.de/bgb/__559.html))

Eine Erhöhung nach § 559 BGB folgt einem **anderen Regime**: Sie stützt sich auf durchgeführte Modernisierungsmaßnahmen, wirkt als **einseitige Gestaltungserklärung ohne Zustimmung** des Mieters, kennt eine eigene Kappung (§ 559 Abs. 3a BGB) und ist nicht an die ortsübliche Vergleichsmiete gebunden. Prüfe, ob das Schreiben tatsächlich ein Verlangen nach § 558 BGB ist oder verdeckt eine Modernisierungsmieterhöhung enthält. Die Vermischung beider Wege in einem Schreiben oder das Einrechnen modernisierungsbedingter Beträge in ein § 558-Verlangen ist fehlerhaft und gesondert zu rügen. Vertiefung: `/mietrecht:modernisierung-559-bgb`.

### 8. Mietpreisbremse und zulässiger Erhöhungsbetrag ([§ 556d BGB](https://www.gesetze-im-internet.de/bgb/__556d.html))

In Gebieten der Mietpreisbremse gilt § 558 BGB weiter; die Begrenzung auf die ortsübliche Vergleichsmiete zzgl. 10 % betrifft die **Wiedervermietung**, nicht die laufende Erhöhung. Prüfe aber, ob die Ausgangsmiete selbst nach §§ 556d ff. BGB überhöht und gerügt ist — dann ist die gerügte, abgesenkte Miete Ausgangswert. Vertiefung: `/mietrecht:mietpreisbremse`.

**Zulässiger Erhöhungsbetrag** — abschließende Rechnung: das **Minimum** aus (a) ortsüblicher Vergleichsmiete und (b) Ausgangsmiete zuzüglich Kappungsgrenze. Die Forderung wird gegen diesen Wert gespiegelt; die Differenz ist der unbegründete Teil.

## Deterministische Berechnung

Die Fristen des § 558 BGB sind Ereignisfristen nach [§ 187 Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__187.html); das Fristende verschiebt sich nach [§ 193 BGB](https://www.gesetze-im-internet.de/bgb/__193.html) auf den nächsten Werktag. Der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) macht **nur die Arithmetik** — der Zugangszeitpunkt und das Datum der letzten Erhöhung bleiben juristische Eingaben und sind gesondert nachzuweisen.

```bash
# 15-Monats-Frist: letzte Erhöhung wirksam ab 01.01.2025
python -m scripts.legal_calc.cli frist --ereignis 01.01.2025 --menge 15 --einheit monate --land BY

# Jahressperrfrist § 558 Abs. 1 S. 2 BGB: frühester Zugang eines neuen Verlangens
python -m scripts.legal_calc.cli frist --ereignis 01.01.2025 --menge 12 --einheit monate --land BY

# Überlegungsfrist § 558b Abs. 2 BGB: Zugang 15.01.2026, Ende zweiter Kalendermonat
python -m scripts.legal_calc.cli frist --ereignis 15.01.2026 --menge 3 --einheit monate --land BY

# Klagefrist des Vermieters: 3 Monate ab Ablauf der Überlegungsfrist
python -m scripts.legal_calc.cli frist --ereignis 31.03.2026 --menge 3 --einheit monate --land BY
```

`--json` liefert die Rechenschritte samt Normzitat maschinenlesbar. Die Überlegungsfrist des § 558b BGB ist eine **Kalendermonatsfrist**, keine reine Monatsfrist — das Rechnerergebnis ist gegen den Wortlaut („Ablauf des zweiten Kalendermonats nach Zugang") gegenzuprüfen.

## Quellen

### Statute

- [§ 558 BGB](https://www.gesetze-im-internet.de/bgb/__558.html), [§ 558a BGB](https://www.gesetze-im-internet.de/bgb/__558a.html), [§ 558b BGB](https://www.gesetze-im-internet.de/bgb/__558b.html), [§ 558c BGB](https://www.gesetze-im-internet.de/bgb/__558c.html), [§ 558d BGB](https://www.gesetze-im-internet.de/bgb/__558d.html), [§ 558e BGB](https://www.gesetze-im-internet.de/bgb/__558e.html)
- [§ 559 BGB](https://www.gesetze-im-internet.de/bgb/__559.html) (Modernisierungsmieterhöhung), [§ 556d BGB](https://www.gesetze-im-internet.de/bgb/__556d.html) (Mietpreisbremse)
- [§ 126b BGB](https://www.gesetze-im-internet.de/bgb/__126b.html) (Textform), [§ 174 BGB](https://www.gesetze-im-internet.de/bgb/__174.html) (Vollmachtsvorlage)
- [§ 187 BGB](https://www.gesetze-im-internet.de/bgb/__187.html), [§ 188 BGB](https://www.gesetze-im-internet.de/bgb/__188.html), [§ 193 BGB](https://www.gesetze-im-internet.de/bgb/__193.html) (Fristberechnung)

### Kommentare

- Börstinghaus, in: Schmidt-Futterer, Mietrecht, 15. Aufl. 2023, § 558 BGB Rn. 1 ff.
- Eisenschmid, in: Schmidt-Futterer, Mietrecht, 15. Aufl. 2023, § 558a BGB Rn. 1 ff.
- Artz, in: MüKoBGB, 9. Aufl. 2023, § 558 Rn. 1 ff.; § 558a Rn. 1 ff.
- Weidenkaff, in: Grüneberg, BGB, 84. Aufl. 2025, § 558 Rn. 1 ff.

### Rechtsprechung

- BGH, Urt. v. 18.11.2015 – VIII ZR 266/14 (Mieterhöhung bei Wohnflächenabweichung; tatsächliche Fläche maßgeblich, Kappungsgrenze bleibt) — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2015-11-18&Aktenzeichen=VIII%20ZR%20266/14
- BGH, Urt. v. 23.06.2010 – VIII ZR 256/09 (konkludente Wohnflächenvereinbarung) — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2010-06-23&Aktenzeichen=VIII%20ZR%20256/09
- Zur Begründungstiefe und Bestimmtheit der drei Vergleichswohnungen ist die einschlägige BGH-Rechtsprechung heranzuziehen `[unverifiziert - prüfen]`. Kein Aktenzeichen ohne eigene Verifikation in juris / Beck-Online übernehmen.

## Formulierungshilfe — Mieterhöhungsverlangen (§§ 558, 558a BGB)

```
Sehr geehrte Frau …, sehr geehrter Herr …,

hiermit verlange ich Ihre Zustimmung zur Erhöhung der Nettokaltmiete für die
von Ihnen gemietete Wohnung <Anschrift, Lage im Haus>.

Die derzeitige Nettokaltmiete beträgt <Betrag> EUR monatlich. Sie ist seit
dem <Datum> unverändert. Ich verlange die Zustimmung zur Erhöhung auf
<Betrag> EUR monatlich, mithin um <Differenz> EUR.

Zur Begründung nehme ich Bezug auf den Mietspiegel der Stadt <Ort> in der
Fassung vom <Datum>. Die Wohnung ist dort in das Feld <Feld> einzuordnen
(Baujahr <…>, Wohnfläche <…> m², Ausstattung <…>, Lage <…>). Die Spanne
dieses Feldes reicht von <…> EUR/m² bis <…> EUR/m²; der Mittelwert beträgt
<…> EUR/m². Die verlangte Miete liegt mit <…> EUR/m² innerhalb der Spanne.

Die Kappungsgrenze des § 558 Abs. 3 BGB ist gewahrt: Die Miete betrug am
<Datum, drei Jahre zuvor> <Betrag> EUR; die Erhöhung beträgt <…> % und liegt
damit unter <20 % / 15 %>.

Sie können der Erhöhung bis zum Ablauf des zweiten Kalendermonats nach
Zugang dieses Schreibens zustimmen. Die erhöhte Miete ist ab dem <Datum>
zu zahlen.

Mit freundlichen Grüßen
```

## Ausgabeformat

```
MIETERHÖHUNG § 558 BGB — <Vermieter-Entwurf / Mieter-Prüfung> — <Mandat-ID> — <Datum>

I.    Perspektive                      [Vermieter-Entwurf / Mieter-Prüfung]
II.   Form (§ 558a Abs. 1, § 126b)     [✅ / ❌]
      - Textform                       [✅ / ❌]
      - Alle Vermieter / alle Mieter   [✅ / ❌]
      - Bestimmtheit der Forderung     [✅ / ⚠️]
III.  Begründungsmittel (§ 558a)       [Mietspiegel / Gutachten / 3 Wohnungen / Datenbank]
      Bestimmtheit                     [✅ / ⚠️ / ❌]
IV.   Fristen
      - Jahressperre (12 Monate)       [✅ / ❌]
      - 15-Monats-Frist                [✅ / ❌]  Wirksam ab: <Datum>
      - Überlegungsfrist Ende          <Datum>
      - Klagefrist Vermieter Ende      <Datum>
V.    Ortsübliche Vergleichsmiete      Mietspiegelwert: <Wert>
                                       Forderung: <Wert>   [innerhalb / darüber]
VI.   Kappungsgrenze (§ 558 Abs. 3)    Ausgang + <20 % / 15 %> = <Wert>
                                       Forderung: <Wert>   [✅ / überschießend <Differenz>]
VII.  Abgrenzung § 559 BGB             [N/A / Verdacht — gesondert prüfen]
VIII. Mietpreisbremse (§§ 556d ff.)    [N/A / Ausgangsmiete gerügt]
IX.   Zulässiger Erhöhungsbetrag       <Min(Vergleichsmiete, Kappungsgrenze)>
      Empfehlung                       [versandfertig / nachbessern] bzw.
                                       [Zustimmung voll / teilweise <Wert> / verweigern]

Ergebnis: <wirksam / teilweise wirksam / unwirksam>
Risiko Zustimmungsklage: [🟢 / 🟡 / 🔴]
```

## Risiken / typische Fehler

- **Form vor Höhe verwechselt** — ein formunwirksames Verlangen ist insgesamt unwirksam; die Höhe ist dann gar nicht mehr zu prüfen.
- **Jahressperre und 15-Monats-Frist vermengt** — die eine betrifft den Zugang, die andere die Wirksamkeit; ein verfrühtes Verlangen ist unwirksam und kostet eine volle neue Wartezeit.
- **Begründungsmittel zu unbestimmt** — pauschaler Verweis auf „den Mietspiegel" ohne Einordnung der Wohnung oder Vergleichswohnungen ohne auffindbare Adresse genügen nicht.
- **Kappungsgrenze falsch berechnet** — Drei-Jahres-Zeitraum falsch angesetzt, kumulierte Vorerhöhungen vergessen oder die abgesenkte 15-%-Grenze übersehen.
- **Mietspiegel nicht aktuell** — ohne Anpassung nach zwei Jahren (§ 558d Abs. 2 BGB) entfällt die Vermutungswirkung des qualifizierten Mietspiegels.
- **Verlangen an nur einen von mehreren Mietern** oder ohne Vollmachtsvorlage (§ 174 BGB) → unwirksam bzw. zurückweisbar.
- **Modernisierung als Vergleichsmieterhöhung getarnt** — § 559 BGB folgt eigenen Regeln; Vermischung ist zu rügen.
- **Teilzustimmung verpasst** — bei nur teilweiser Begründetheit die Zustimmung in wirksamer Höhe versäumt und dadurch unnötiges Klagerisiko geschaffen.
- **Klagefrist § 558b Abs. 2 S. 2 BGB versäumt** — das gesamte Verlangen muss neu aufgesetzt werden.
