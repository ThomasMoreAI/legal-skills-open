---
name: entgeltdiskriminierung-durchsetzung-borghei
title: /entgelttransparenz-eu:entgeltdiskriminierung-durchsetzung
description: Durchsetzung des Entgeltgleichheitsanspruchs – Rechtsschutz Art. 14 und Verbandsverfahren Art. 15 RL (EU) 2023/970, Schadensersatz Art. 16 mit vollständigem Ausgleich einschließlich Nachzahlung und Boni, sonstige Abhilfemaßnahmen Art. 17, Verlagerung der Beweislast Art. 18 Abs. 1 und die verschärfte Vollumkehr nach Abs. 2 bei Verletzung der Transparenzpflichten der Art. 5, 6, 7, 9 und 10 mit dem engen Gegenbeweis offensichtlich unbeabsichtigter und geringfügiger Verstöße, Nachweis gleichwertiger Arbeit Art. 19, Zugang zu Beweismitteln Art. 20, Verjährung von mindestens drei Jahren ab Kenntnis Art. 21, Verfahrenskosten Art. 22, Sanktionen Art. 23 und Viktimisierungsschutz Art. 25 sowie das Zusammenspiel mit Art. 157 AEUV, § 3 und § 7 EntgTranspG, § 15 AGG und § 612a BGB. Use when ein Entgeltgleichheitsanspruch geltend gemacht oder abgewehrt werden soll.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/entgelttransparenz-eu/skills/entgeltdiskriminierung-durchsetzung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: employment
language: de
---

# /entgelttransparenz-eu:entgeltdiskriminierung-durchsetzung

## Zweck

Der Skill führt den Entgeltgleichheitsanspruch durch den Prozess — aus Kläger- wie aus Beklagtensicht. Sein Kern ist die **Beweislast**: Art. 18 Abs. 2 RL (EU) 2023/970 kehrt sie vollständig um, wenn der Arbeitgeber seine Transparenzpflichten verletzt hat. Damit wird jede versäumte Auskunft, jeder fehlende Bericht und jede unterlassene Entgeltbewertung zum prozessualen Nachteil.

## Eingaben

- Anspruchsteller: Tätigkeit, Entgelt, Eintrittsdatum, Vergleichspersonen
- Behauptete Vergleichstätigkeit und die dafür sprechenden objektiven Kriterien
- Entgeltdifferenz: Grundentgelt, variable und ergänzende Bestandteile, Zeitraum
- Erfüllungsstand der Transparenzpflichten des Arbeitgebers: Art. 5, 6, 7, 9, 10 bzw. §§ 10 ff. EntgTranspG
- Erteilte oder verweigerte Auskünfte mit Datum
- Ob eine gemeinsame Entgeltbewertung ausgelöst wurde und was sie ergab
- Ob Repressalien nach dem Verlangen erfolgt sind
- Trägerschaft des Arbeitgebers (privat oder staatlich)

## Sub-Agent-Architektur

Der Researcher beschafft die RL (EU) 2023/970, Art. 157 AEUV, EntgTranspG, AGG und die BAG-Rechtsprechung zur Entgeltgleichheit und zur Darlegungslast. Der Drafter baut die Anspruchsprüfung und die Beweislastkette auf. Der Reviewer prüft, ob die Beweislastumkehr richtig verortet ist, ob die Verjährung gerechnet wurde und ob nicht Richtlinienrecht unbesehen gegen einen privaten Arbeitgeber angewandt wird.

## Ablauf

### 1. Anspruchsgrundlagen ordnen

| Grundlage | Wirkung | Anmerkung |
|---|---|---|
| **Art. 157 AEUV** | unmittelbar, **auch zwischen Privaten** | trägt den Anspruch auf gleiches Entgelt unabhängig von jeder Umsetzung |
| **[§ 3](https://www.gesetze-im-internet.de/entgtranspg/__3.html), [§ 7 EntgTranspG](https://www.gesetze-im-internet.de/entgtranspg/__7.html)** | Verbot der Entgeltbenachteiligung; Anspruch auf gleiches Entgelt | geltendes deutsches Recht, richtlinienkonform auszulegen |
| **[§ 15 AGG](https://www.gesetze-im-internet.de/agg/__15.html)** | Schadensersatz und Entschädigung | Ausschlussfrist des [§ 15 Abs. 4 AGG](https://www.gesetze-im-internet.de/agg/__15.html) beachten |
| **RL (EU) 2023/970 Art. 16, 18** | vollständiger Ausgleich, Beweislast | horizontal **nicht** unmittelbar; gegenüber staatlichen Arbeitgebern ggf. schon |
| **[§ 612a BGB](https://www.gesetze-im-internet.de/bgb/__612a.html)** | Maßregelungsverbot | flankiert Art. 25 (Viktimisierung) |

Der Anspruch auf **Nachzahlung** folgt aus Art. 157 AEUV iVm dem Arbeitsvertrag bzw. § 3, § 7 EntgTranspG; er ist auf **Anpassung nach oben** gerichtet.

### 2. Gleichwertigkeit darlegen (Art. 4, Art. 19 RL (EU) 2023/970)

Maßstab sind **objektive, geschlechtsneutrale Kriterien**: **Kompetenzen, Belastungen, Verantwortung und Arbeitsbedingungen** sowie gegebenenfalls weitere relevante Faktoren. **Art. 19** verpflichtet die Mitgliedstaaten, den Nachweis gleicher oder gleichwertiger Arbeit zu erleichtern; die Vergleichsperson muss nicht zwingend zeitgleich beschäftigt sein, soweit das nationale Recht dies zulässt — die konkrete Ausgestaltung ist der Umsetzung vorbehalten `[unverifiziert – prüfen]`.

Praktisch trägt der Vortrag, der die Tätigkeit **anhand der vier Kriterien zerlegt** und je Kriterium die Vergleichbarkeit begründet — nicht der Verweis auf dieselbe Stellenbezeichnung oder dieselbe Entgeltgruppe.

### 3. Beweislast — der Hebel des Verfahrens (Art. 18 RL (EU) 2023/970)

**Abs. 1 — Regelfall:** Machen Arbeitnehmer, die sich in ihren Rechten verletzt halten, **Tatsachen glaubhaft**, die eine unmittelbare oder mittelbare Diskriminierung **vermuten lassen**, muss die **beklagte Partei nachweisen**, dass keine Entgeltdiskriminierung vorliegt. Das entspricht der Struktur des [§ 22 AGG](https://www.gesetze-im-internet.de/agg/__22.html).

**Abs. 2 — die Verschärfung:** In Verfahren über mutmaßliche Entgeltdiskriminierung, **in denen der Arbeitgeber die Transparenzpflichten der Art. 5, 6, 7, 9 und 10 nicht erfüllt hat**, muss **der Arbeitgeber nachweisen**, dass keine Diskriminierung vorliegt — **ohne** dass der Arbeitnehmer zuvor Indizien glaubhaft machen müsste.

**Die einzige Ausnahme:** Unterabs. 1 findet keine Anwendung, wenn der Arbeitgeber nachweist, dass der Verstoß gegen die Art. 5, 6, 7, 9 und 10 **offensichtlich unbeabsichtigt und geringfügig** war. Beide Merkmale müssen kumulativ vorliegen, und die Beweislast dafür trägt der Arbeitgeber.

**Abs. 3** erlaubt den Mitgliedstaaten eine für den Arbeitnehmer **günstigere** Beweislastregelung.

**Beratungsfolge für Arbeitgeber:** Die Transparenzpflichten sind kein Selbstzweck, sondern die Versicherung gegen die Vollumkehr. Eine nicht beantwortete Auskunft nach Art. 7, eine ausgelassene Berichterstattung nach Art. 9 oder eine unterlassene gemeinsame Entgeltbewertung nach Art. 10 verlagert im Prozess die gesamte Beweislast.

**Beratungsfolge für Arbeitnehmer:** Vor der Klage wird stets zuerst das **Auskunftsverlangen** gestellt (`/entgelttransparenz-eu:entgelt-auskunftsanspruch`) — die Antwort oder deren Ausbleiben bestimmt die Beweislage.

### 4. Zugang zu Beweismitteln (Art. 20 RL (EU) 2023/970)

Gerichte müssen anordnen können, dass die beklagte Partei **relevante Beweismittel** vorlegt, die sich in ihrer Verfügungsgewalt befinden — einschließlich vertraulicher Informationen unter geeigneten Schutzmaßnahmen. Das ist im deutschen Zivilprozess über §§ 142, 144 ZPO abzubilden und **keine** US-Discovery: Der Antrag muss die Beweismittel konkret bezeichnen (vgl. `CONVENTIONS.md`).

### 5. Rechtsfolgen (Art. 16, 17, 23 RL (EU) 2023/970)

- **Art. 16 — Schadensersatz:** Anspruch auf **vollständigen Ausgleich**; er umfasst insbesondere die **Nachzahlung** des vorenthaltenen Entgelts und der damit verbundenen **Boni oder Sachleistungen**, den Ersatz entgangener Chancen und immaterieller Schäden. Eine **Höchstgrenze** ist unzulässig.
- **Art. 17 — sonstige Abhilfemaßnahmen:** Unterlassung, Feststellung und strukturelle Maßnahmen.
- **Art. 23 — Sanktionen:** wirksam, verhältnismäßig und abschreckend; die Ausgestaltung obliegt dem nationalen Gesetzgeber.
- **§ 15 AGG** bleibt daneben anwendbar — mit der **Zweimonatsfrist** des § 15 Abs. 4 AGG, die im Mandat sofort zu notieren ist.

### 6. Verjährung (Art. 21 RL (EU) 2023/970)

- Die Verjährungsfrist **beginnt nicht, bevor die klagende Partei Kenntnis vom Verstoß hat** oder vernünftigerweise haben musste;
- die Mitgliedstaaten können bestimmen, dass sie nicht beginnt, solange der Verstoß **fortdauert**, oder erst mit **Beendigung des Arbeitsverhältnisses**;
- sie darf **nicht kürzer als drei Jahre** sein;
- sie wird **gehemmt oder unterbrochen**, sobald die klagende Partei den Arbeitgeber über eine Beschwerde in Kenntnis setzt oder ein Verfahren anstrengt (Abs. 2);
- Abs. 3: Die Vorschrift gilt **nicht** für Vorschriften über das **Erlöschen** von Ansprüchen — **tarifliche und vertragliche Ausschlussfristen** bleiben also gesondert zu prüfen.

Solange keine Umsetzung vorliegt, gilt national die Regelverjährung der [§§ 195, 199 BGB](https://www.gesetze-im-internet.de/bgb/__195.html) — drei Jahre ab Schluss des Jahres der Entstehung und Kenntnis —, ausgelegt im Licht des Art. 21.

### 7. Verfahrenskosten und Viktimisierung (Art. 22, 25 RL (EU) 2023/970)

- **Art. 22** — Kostenregelungen, die obsiegenden Klägern die Kosten erstatten und unterlegene Kläger unter bestimmten Voraussetzungen entlasten. Im deutschen Arbeitsgerichtsverfahren erster Instanz trägt nach [§ 12a ArbGG](https://www.gesetze-im-internet.de/arbgg/__12a.html) ohnehin jede Partei ihre Anwaltskosten selbst.
- **Art. 25** — Schutz vor **Viktimisierung** und ungünstigerer Behandlung; national flankiert durch [§ 612a BGB](https://www.gesetze-im-internet.de/bgb/__612a.html) und [§ 16 AGG](https://www.gesetze-im-internet.de/agg/__16.html).
- **Art. 15** — Verfahren im Namen oder zur Unterstützung von Arbeitnehmern durch Arbeitnehmervertreter oder Gleichbehandlungsstellen; **Art. 28** — Rolle der Gleichbehandlungsstellen.

## Deterministische Berechnung

Der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) macht nur die Arithmetik:

```bash
# Regelverjährung §§ 195, 199 BGB für den Nachzahlungsanspruch
python -m scripts.legal_calc.cli verjaehrung --entstehung 31.01.2024 --kenntnis 12.09.2026

# Mindestverjährung Art. 21 Abs. 1: nicht kürzer als drei Jahre ab Kenntnis
python -m scripts.legal_calc.cli frist --ereignis 12.09.2026 --menge 3 --einheit jahre --land BY

# Ausschlussfrist § 15 Abs. 4 AGG: 2 Monate ab Kenntnis der Benachteiligung
python -m scripts.legal_calc.cli frist --ereignis 12.09.2026 --menge 2 --einheit monate --land BY

# Tarifliche oder vertragliche Ausschlussfrist - Art. 21 Abs. 3 lässt sie unberührt
python -m scripts.legal_calc.cli frist --ereignis 12.09.2026 --menge 3 --einheit monate --land BY
```

## Quellen

### Rechtsakte

- Richtlinie (EU) 2023/970, Art. 4, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 28 — [EUR-Lex](https://eur-lex.europa.eu/eli/dir/2023/970/oj)
- Art. 157 AEUV — [EUR-Lex](https://eur-lex.europa.eu/eli/treaty/tfeu_2012/oj); Richtlinie 2006/54/EG — [EUR-Lex](https://eur-lex.europa.eu/eli/dir/2006/54/oj)
- [§ 3](https://www.gesetze-im-internet.de/entgtranspg/__3.html), [§ 7](https://www.gesetze-im-internet.de/entgtranspg/__7.html), [§ 10 EntgTranspG](https://www.gesetze-im-internet.de/entgtranspg/__10.html)
- [§ 15 AGG](https://www.gesetze-im-internet.de/agg/__15.html), [§ 16 AGG](https://www.gesetze-im-internet.de/agg/__16.html), [§ 22 AGG](https://www.gesetze-im-internet.de/agg/__22.html)
- [§ 195 BGB](https://www.gesetze-im-internet.de/bgb/__195.html), [§ 199 BGB](https://www.gesetze-im-internet.de/bgb/__199.html), [§ 612a BGB](https://www.gesetze-im-internet.de/bgb/__612a.html)
- [§ 12a ArbGG](https://www.gesetze-im-internet.de/arbgg/__12a.html); [§ 142 ZPO](https://www.gesetze-im-internet.de/zpo/__142.html), [§ 144 ZPO](https://www.gesetze-im-internet.de/zpo/__144.html)

### Kommentare und Literatur

- ErfK und HWK zu Art. 157 AEUV, EntgTranspG und AGG.
- BeckOK ArbR zu § 22 AGG (Darlegungs- und Beweislast).
- Beiträge zur Beweislastumkehr nach Art. 18 RL (EU) 2023/970 in NZA und RdA 2024–2026 (Fundstelle prüfen) `[unverifiziert – prüfen]`

### Rechtsprechung

Zur Entgeltgleichheit, zur Vergleichbarkeit von Tätigkeiten und zur Darlegungslast nach § 22 AGG besteht **gefestigte** Rechtsprechung des BAG und des EuGH; zur RL (EU) 2023/970 selbst liegt noch keine Judikatur vor. Jede konkrete Entscheidung ist vor Verwendung in juris, Beck-Online, curia.europa.eu oder auf bundesarbeitsgericht.de zu verifizieren; ohne Beleg gilt sie als `[unverifiziert – prüfen]`.

## Ausgabeformat

```
ENTGELTGLEICHHEIT — DURCHSETZUNG — <Mandat> — <Datum>

I.   Anspruchsgrundlagen
     Art. 157 AEUV:           <trägt unabhängig von der Umsetzung>
     § 3, § 7 EntgTranspG:    <…>
     § 15 AGG:                <Entschädigung / Schadensersatz>
     Richtlinie unmittelbar:  [nur bei staatlichem Arbeitgeber]

II.  Gleichwertigkeit (Art. 4, 19)
     Kompetenzen:             <…>
     Belastungen:             <…>
     Verantwortung:           <…>
     Arbeitsbedingungen:      <…>
     Vergleichsperson(en):    <…>
     Ergebnis:                [gleich / gleichwertig / nicht vergleichbar]

III. Entgeltdifferenz
     Grundentgelt:            <…>
     Variable/ergänzende Bestandteile: <…>
     Zeitraum:                <…>   Gesamtbetrag: <…>

IV.  Beweislast Art. 18
     Transparenzpflichten Art. 5, 6, 7, 9, 10 erfüllt? <je Norm>
     → Abs. 1 (Indizien nötig) oder Abs. 2 (Vollumkehr): <Ergebnis>
     Ausnahme Abs. 2 UAbs. 2:  [offensichtlich unbeabsichtigt UND geringfügig? — Beweis beim AG]
     Zugang zu Beweismitteln Art. 20 / §§ 142, 144 ZPO: <konkret bezeichnete Unterlagen>

V.   Rechtsfolgen
     Nachzahlung:             <Betrag>
     Boni / Sachleistungen:   <…>
     Immaterieller Schaden:   <…>
     Keine Höchstgrenze (Art. 16): <…>
     Sonstige Maßnahmen Art. 17:   <…>

VI.  Fristen
     Verjährung §§ 195, 199 BGB:      bis <Datum>
     Art. 21: mindestens 3 Jahre ab Kenntnis, Hemmung ab Beschwerde
     § 15 Abs. 4 AGG:                 2 Monate — bis <Datum>
     Tarifliche/vertragliche Ausschlussfrist (Art. 21 Abs. 3 unberührt): bis <Datum>

VII. Flankierung
     Viktimisierung Art. 25 / § 612a BGB / § 16 AGG: <…>
     Unterstützung Art. 15 / Gleichbehandlungsstelle Art. 28: <…>
     Kosten Art. 22 / § 12a ArbGG:    <…>

VIII.Risiko: 🟢 / 🟡 / 🔴 <Begründung>
IX.  Quellenverzeichnis
```

## Risiken / typische Fehler

- **Beweislastumkehr des Art. 18 Abs. 2 gegen einen privaten Arbeitgeber unmittelbar angewandt.** Ohne Umsetzung fehlt die horizontale Wirkung; national ist über § 22 AGG und die richtlinienkonforme Auslegung zu argumentieren.
- **Transparenzpflichtverletzung nicht ausgewertet.** Sie ist der Auslöser der Vollumkehr — und der wichtigste Vortrag der Klägerseite.
- **Ausnahme des Art. 18 Abs. 2 UAbs. 2 zu weit gelesen.** Erforderlich ist **kumulativ** offensichtlich unbeabsichtigt **und** geringfügig, und der Arbeitgeber trägt dafür die Beweislast.
- **Ausschlussfrist des § 15 Abs. 4 AGG versäumt** — zwei Monate, unabhängig von der Verjährung.
- **Tarifliche Ausschlussfristen übersehen.** Art. 21 Abs. 3 lässt Erlöschensvorschriften ausdrücklich unberührt.
- **Nur das Grundentgelt eingeklagt.** Art. 16 erfasst auch Boni und Sachleistungen; eine Höchstgrenze ist unzulässig.
- **Gleichwertigkeit über die Entgeltgruppe begründet** statt über die vier Kriterien des Art. 4.
- **Art. 20 als Discovery ausgelegt.** Der Vorlageantrag muss die Beweismittel konkret bezeichnen (§§ 142, 144 ZPO).
- **Viktimisierungsschutz vergessen**, obwohl nach dem Auskunftsverlangen Nachteile eingetreten sind.
- **Rechtsprechung erfunden.** Jede Entscheidung ist zu belegen oder als `[unverifiziert – prüfen]` zu kennzeichnen.
