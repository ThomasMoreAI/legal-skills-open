---
name: handelsvertretervertrag-borghei
title: /handelsrecht:handelsvertretervertrag
description: Entwurf und Prüfung eines Handelsvertretervertrags nach §§ 84 ff. HGB inkl. Abgrenzung zu Vertragshändler/Kommissionsagent/Franchisenehmer, Provisionsregelung §§ 87 ff. HGB, Kündigung § 89 HGB, Ausgleichsanspruch § 89b HGB und nachvertragliches Wettbewerbsverbot § 90a HGB. Use when ein Unternehmer einen Vertriebsvertrag aufsetzt, ein Handelsvertreter seinen Ausgleichsanspruch beziffert oder die Beendigung eines Vertragsverhältnisses ansteht.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/handelsrecht/skills/handelsvertretervertrag
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: commercial
language: de
---

# /handelsrecht:handelsvertretervertrag

## Zweck

Der Skill unterstützt beim **Entwurf** und der **Prüfung** eines Handelsvertretervertrags nach §§ 84 ff. HGB. Schwerpunkt sind die typischen Streitpunkte: Abgrenzung zu anderen Vertriebsformen, Provisionsanspruch (Stamm-, Folge-, Bezirksprovision), Kündigung mit gestaffelten Fristen, **Ausgleichsanspruch § 89b HGB** (Berechnung, Höchstgrenze, Ausschlussgründe, Ausschlussfrist) sowie das nachvertragliche Wettbewerbsverbot § 90a HGB mit Karenzentschädigung. Bezug zur Handelsvertreter-Richtlinie 86/653/EWG wird berücksichtigt.

## Eingaben

- Vertragsparteien (Unternehmer / Handelsvertreter, Rechtsform, Niederlassungen)
- Vertragsgegenstand (Produktportfolio, geografisches Gebiet, Branche)
- gewollte Vertriebsform (Handelsvertreter / Vertragshändler / Kommissionsagent / Franchise)
- Provisionsmodell (Satz, Bemessungsgrundlage, Bezirksvertretung ja/nein, Folgeprovisionen)
- Vertragsdauer und Beendigungsabsicht (ordentliche/außerordentliche Kündigung, Eigen-/Fremdkündigung)
- bei § 89b-Berechnung: Provisionseinnahmen der letzten 5 Jahre, Anteil Neukunden, Anteil intensivierte Altkunden, Abwanderungsquote
- Auslandsbezug (EU/Nicht-EU; Rechtswahl)

## Sub-Agent-Architektur

Researcher liefert §§ 84–92c HGB, EU-RL 86/653/EWG, BGH-Rspr. zur § 89b-Berechnung, EuGH-Linie (Ingmar, Turgay Semen, Quenon) und Standardkommentare (Hopt, Emde, MüKoHGB, Röhricht/Graf von Westphalen). Drafter erstellt den Vertragsentwurf bzw. das Memo mit § 89b-Berechnung in fünf Stufen. Reviewer prüft Unabdingbarkeit, Ausschlussfristen, AGB-Kontrolle und Karenzentschädigung.

## Ablauf

### 1. Abgrenzung der Vertriebsform

| Vertriebsform | Kernmerkmal | Rechtsgrundlage |
|---|---|---|
| **Handelsvertreter** | selbständig, ständig betraut, im fremden Namen und auf fremde Rechnung vermittelt/abschließt | §§ 84 ff. HGB |
| **Vertragshändler** | kauft im eigenen Namen, verkauft auf eigene Rechnung; vertraglich eingebunden | analog § 89b HGB nur bei handelsvertreterähnlicher Einbindung, st. Rspr. `[unverifiziert]` |
| **Kommissionsagent** | im eigenen Namen, auf fremde Rechnung | §§ 383 ff. HGB |
| **Franchisenehmer** | nutzt fremdes Geschäftsmodell, eigene Rechnung | Innominat-Vertrag; § 89b HGB analog möglich `[unverifiziert]` |

Der **Status** ergibt sich nach der **tatsächlichen Vertragsdurchführung**, nicht aus der Bezeichnung im Vertrag (Hopt, Baumbach/Hopt HGB, § 84 Rn. 6).

### 2. Pflichten der Parteien

- **Handelsvertreter** (§ 86 HGB): Interessenwahrungspflicht, Bemühungspflicht, Berichtspflicht, Verschwiegenheit (§ 90 HGB).
- **Unternehmer** (§ 86a HGB): Überlassung der erforderlichen Unterlagen, Information über Annahme/Ablehnung der Geschäfte und Nichtausführung, Provisionsabrechnung (§ 87c HGB) – diese Pflichten sind **zwingend** zum Schutz des Handelsvertreters.

### 3. Provisionsanspruch §§ 87 ff. HGB

- **§ 87 Abs. 1 HGB:** Provision für während der Vertragsdauer abgeschlossene Geschäfte, die auf Tätigkeit des Handelsvertreters zurückgehen.
- **§ 87 Abs. 2 HGB Bezirksvertreter:** Provision auch für Geschäfte, die **ohne Mitwirkung** zustande kommen, wenn der Handelsvertreter die Bezirks-/Kundenkreis-Alleinvertretung hat.
- **§ 87 Abs. 3 HGB Folgegeschäfte:** Provision auch für Folgegeschäfte mit denselben Kunden, soweit diese auf die ursprüngliche Tätigkeit zurückgehen.
- **§ 87a HGB:** Entstehungs- und Fälligkeitszeitpunkt, Wegfall bei Nichtausführung durch Unternehmer aus von ihm zu vertretenden Gründen.
- **§ 87c HGB Abrechnung:** monatlich (vertraglich verlängerbar bis 3 Monate), Buchauszugsanspruch.

### 4. Vertragsbeendigung § 89 HGB

Kündigungsfristen (jeweils zum Monatsende, § 89 Abs. 1 HGB):

| Vertragsdauer | Frist |
|---|---|
| im 1. Jahr | 1 Monat |
| im 2. Jahr | 2 Monate |
| ab 3. Jahr | 3 Monate |
| ab 5. Jahr | 6 Monate |

Außerordentliche Kündigung aus wichtigem Grund nach **§ 89a HGB** ist **unabdingbar**.

### 5. Ausgleichsanspruch § 89b HGB – fünfstufige Berechnung

§ 89b HGB ist die **wirtschaftlich wichtigste Norm** des Plugins. Berechnung gestuft (st. Rspr. BGH `[unverifiziert – prüfen in juris]`; vgl. Hopt, Baumbach/Hopt HGB, § 89b Rn. 30 ff.; nach EuGH Turgay Semen, C-348/07 `[unverifiziert]` darf die nationale Berechnung nicht hinter der RL zurückbleiben):

**Stufe 1 – Provisionsverluste des Handelsvertreters**
Der Handelsvertreter verliert Provisionen für künftige Folgegeschäfte mit von ihm geworbenen Stamm-/Neukunden.

- Provisionseinnahmen aus diesen Kunden im letzten Vertragsjahr
- Prognosezeitraum idR 3–5 Jahre (Branchenüblichkeit)
- jährliche Abwanderungsquote (z. B. 20 %)
- Abzinsung (z. B. nach Hoffmann-Tabelle oder vereinfacht)

**Stufe 2 – Unternehmervorteile**
Anhaltende Vorteile des Unternehmers aus den geworbenen Kundenbeziehungen nach Vertragsende.

- Annahme: Unternehmervorteil deckt sich grundsätzlich mit den Provisionsverlusten (BGH `[unverifiziert]`), kann aber bei Sogwirkung der Marke gemindert sein.

**Stufe 3 – Billigkeitsprüfung (§ 89b Abs. 1 Nr. 2 HGB)**
Korrekturen aus:

- Sogwirkung der Marke (mindernd)
- Karenzentschädigung aus § 90a HGB (mindernd, da bereits gezahlt)
- Alter, Versorgungssituation, Branchenüblichkeit
- Vertragstreue, Kooperationsverhalten

**Stufe 4 – Höchstgrenze (§ 89b Abs. 2 HGB)**
Begrenzung auf eine durchschnittliche Jahresprovision der letzten fünf Jahre (bzw. der kürzeren Vertragsdauer).

**Stufe 5 – Ausschluss (§ 89b Abs. 3 HGB)**
Kein Anspruch, wenn:

- Handelsvertreter selbst gekündigt hat **ohne** vom Unternehmer veranlassten Anlass und ohne dass Alter/Krankheit eine Fortsetzung unzumutbar machte
- Unternehmer aus wichtigem, vom Handelsvertreter zu vertretendem Grund gekündigt hat
- Vertragsübernahme durch Dritten mit Zustimmung des Handelsvertreters

**Vereinfachte Formel als Kontrollrechnung:**

```
Ausgleich = min(
  Stufe 1 (Provisionsverluste, abgezinst)
    × Billigkeitsfaktor (Stufe 3),
  Stufe 4 (eine Jahresprovision Ø 5 Jahre)
)
```

**Ausschlussfrist § 89b Abs. 4 S. 2 HGB:** Anspruch erlischt, wenn nicht **innerhalb eines Jahres nach Beendigung** des Vertragsverhältnisses geltend gemacht. Der Anspruch ist im Voraus **unabdingbar** (§ 89b Abs. 4 S. 1 HGB) – Klauseln, die ihn ausschließen oder beschneiden, sind unwirksam. Nach EuGH-Linie (Ingmar, C-381/98 `[unverifiziert]`) gilt das auch bei Rechtswahl Nicht-EU, wenn der Handelsvertreter in der EU tätig wird.

### 6. Nachvertragliches Wettbewerbsverbot § 90a HGB

Wirksam nur bei (kumulativ):

- **Schriftform** mit Aushändigung der unterzeichneten Urkunde an den Handelsvertreter
- **Höchstdauer 2 Jahre** nach Vertragsende
- Beschränkung auf Bezirk/Kundenkreis und Gegenstände, mit denen der Handelsvertreter befasst war
- **Karenzentschädigung** als angemessener Ausgleich

Verzicht durch den Unternehmer ist bis Vertragsende möglich, befreit aber von der Pflicht zur Karenzentschädigung erst sechs Monate nach Zugang der Verzichtserklärung.

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute

- [§ 84 HGB](https://www.gesetze-im-internet.de/hgb/__84.html) (Begriff Handelsvertreter)
- [§ 86 HGB](https://www.gesetze-im-internet.de/hgb/__86.html) (Pflichten Handelsvertreter), [§ 86a HGB](https://www.gesetze-im-internet.de/hgb/__86a.html) (Pflichten Unternehmer)
- [§ 87 HGB](https://www.gesetze-im-internet.de/hgb/__87.html) (Provision), [§ 87a HGB](https://www.gesetze-im-internet.de/hgb/__87a.html) (Fälligkeit), [§ 87c HGB](https://www.gesetze-im-internet.de/hgb/__87c.html) (Abrechnung, Buchauszug)
- [§ 89 HGB](https://www.gesetze-im-internet.de/hgb/__89.html) (Kündigung), [§ 89a HGB](https://www.gesetze-im-internet.de/hgb/__89a.html) (außerordentliche Kündigung)
- [§ 89b HGB](https://www.gesetze-im-internet.de/hgb/__89b.html) (Ausgleichsanspruch)
- [§ 90 HGB](https://www.gesetze-im-internet.de/hgb/__90.html) (Verschwiegenheit), [§ 90a HGB](https://www.gesetze-im-internet.de/hgb/__90a.html) (nachvertragliches Wettbewerbsverbot)
- [RL 86/653/EWG](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:31986L0653) (Handelsvertreter-Richtlinie)

### Kommentare

- Hopt, in: Baumbach/Hopt HGB, 42. Aufl. 2023, § 84 Rn. 1 ff., § 89b Rn. 1 ff.
- Emde, in: Staub HGB, 6. Aufl. 2022, § 89b Rn. 1 ff.
- Ströbl, in: MüKoHGB, 5. Aufl. 2021, §§ 84 ff. HGB Rn. 1 ff.
- Löwisch, in: EBJS HGB, 4. Aufl. 2020, § 89b Rn. 1 ff.
- Thume, in: Röhricht/Graf von Westphalen/Haas, HGB, 5. Aufl. 2019, § 89b Rn. 1 ff.

### Rechtsprechung (`[unverifiziert – prüfen in juris / curia.europa.eu]`)

1. EuGH, Urt. v. 09.11.2000 – Rs. C-381/98, Ingmar (Unabdingbarkeit § 89b bei EU-Tätigkeit)
2. EuGH, Urt. v. 26.03.2009 – Rs. C-348/07, Turgay Semen (Berechnung darf RL nicht unterschreiten)
3. EuGH, Urt. v. 03.12.2015 – Rs. C-338/14, Quenon (Verhältnis Ausgleich/Schadensersatz)
4. BGH, Urt. v. 21.06.2018 – VII ZR 13/17 (Berechnung Ausgleichsanspruch)
5. BGH, Urt. v. 23.11.2011 – VIII ZR 203/10 (Vertragshändler-Analogie)

## Ausgabeformat

```
GUTACHTEN / VERTRAGSENTWURF — Handelsvertretervertrag
Parteien: <anonymisiert>

I. Sachverhalt (knapp)
II. Frage(n) / Zielsetzung
III. Kurzantwort
IV. Rechtliche Bewertung
    1. Vertriebsform und Abgrenzung
    2. Pflichten und Provision
    3. Vertragsbeendigung § 89 HGB
    4. Ausgleichsanspruch § 89b HGB – Berechnung
       Stufe 1  Provisionsverluste:     <EUR>
       Stufe 2  Unternehmervorteile:    <EUR>
       Stufe 3  Billigkeit:             Faktor <…>
       Stufe 4  Höchstgrenze (Ø 5 J.):  <EUR>
       Stufe 5  Ausschlussgründe?       <ja/nein>
       Ergebnis:                        <EUR>
    5. Nachvertragliches Wettbewerbsverbot § 90a HGB
V. Vertragsentwurf (sofern beauftragt) – Klauseln nummeriert
VI. Risiken / offene Punkte
    🟢 / 🟡 / 🔴 <Einstufung mit Begründung>
    – Ausschlussfrist § 89b Abs. 4 HGB (1 Jahr) – Wiedervorlage
VII. Quellenverzeichnis
```

## Beispiel (Auszug § 89b-Berechnung)

> "Der Handelsvertreter hat im letzten Vertragsjahr 120.000 EUR Provision aus den von ihm geworbenen Neukunden erzielt. Bei einem Prognosezeitraum von vier Jahren, einer Abwanderungsquote von 20 % p.a. und einer Abzinsung von 5 % ergibt Stufe 1 rund 290.000 EUR. Unternehmervorteile entsprechen nach BGH-Linie diesem Wert. Die Billigkeitsprüfung führt aufgrund starker Sogwirkung der Marke (Marktanteil > 40 %) zu einer Minderung um 30 %, also rund 200.000 EUR. Die Höchstgrenze nach § 89b Abs. 2 HGB (eine Jahresprovision Ø der letzten fünf Jahre = 150.000 EUR) ist niedriger und wird daher Endbetrag: 150.000 EUR. Ausschlussgründe nach § 89b Abs. 3 HGB liegen nicht vor (ordentliche Kündigung durch den Unternehmer). Hinweis: § 89b Abs. 4 S. 2 HGB – Anspruch ist innerhalb von einem Jahr nach Vertragsende geltend zu machen."

## Risiken / typische Fehler

- **Ausschlussfrist § 89b Abs. 4 S. 2 HGB versäumt.** Ein Jahr nach Vertragsende ist der Anspruch verfallen. Wiedervorlage zwingend.
- **Klauseln, die § 89b HGB im Voraus ausschließen** – unwirksam (§ 89b Abs. 4 S. 1 HGB); auch eine Rechtswahl Nicht-EU schützt nicht (Ingmar).
- **§ 90a HGB ohne Karenzentschädigung** vereinbart – unwirksames Wettbewerbsverbot.
- **Buchauszugsanspruch § 87c Abs. 2 HGB übersehen** – wesentliches Druckmittel des Handelsvertreters.
- **Bezeichnung "Handelsvertreter" im Vertrag** trotz tatsächlicher Vertragshändler-Stellung – Status folgt der Vertragsdurchführung.
- **Sogwirkung der Marke** im Billigkeits-Stufe nicht berücksichtigt – führt zu überhöhter Anspruchshöhe und Klagerisiko.
