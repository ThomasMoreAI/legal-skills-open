---
name: betriebsratsanhoerung-borghei
title: /arbeitsrecht:betriebsratsanhoerung
description: Ordnungsgemäße Anhörung des Betriebsrats vor jeder Kündigung nach § 102 BetrVG – Entwurf des Anhörungsschreibens, Grundsatz der subjektiven Determination, Wochenfrist § 102 Abs. 2 S. 1 BetrVG (ordentlich) und Drei-Tages-Frist § 102 Abs. 2 S. 3 BetrVG (außerordentlich), Unwirksamkeitsfolge § 102 Abs. 1 S. 3 BetrVG, Widerspruchsgründe § 102 Abs. 3 BetrVG und Weiterbeschäftigungsanspruch § 102 Abs. 5 BetrVG, Fehlerkatalog. Use when ein Arbeitgeber mit Betriebsrat eine Kündigung vorbereitet oder ein Arbeitnehmervertreter die Anhörung auf Fehler prüft.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/arbeitsrecht/skills/betriebsratsanhoerung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: employment
language: de
---

# /arbeitsrecht:betriebsratsanhoerung

## Zweck

Die Anhörung nach [§ 102 BetrVG](https://www.gesetze-im-internet.de/betrvg/__102.html) ist der am leichtesten zu gewinnende und am häufigsten verlorene Punkt im Kündigungsschutzprozess. Sie kostet den Arbeitgeber eine Woche und ein sorgfältiges Schreiben; ihr Fehlen kostet ihn den Prozess, unabhängig davon, wie gut der Kündigungsgrund ist (§ 102 Abs. 1 S. 3 BetrVG). Dieser Skill erstellt das Anhörungsschreiben und prüft eine bereits erfolgte Anhörung gegen den Fehlerkatalog.

## Eingaben

- Existiert ein Betriebsrat im **kündigungsrelevanten Betrieb**? (nicht: im Unternehmen)
- Kündigungsart: ordentlich / außerordentlich / Verdachtskündigung / Änderungskündigung
- Personalien und Sozialdaten des Arbeitnehmers
- Kündigungsgründe **in der Fassung, in der sie den Kündigungsentschluss tatsächlich getragen haben**
- Bei betriebsbedingter Kündigung: Auswahlkriterien und Vergleichsgruppe
- Bereits erfolgte Anhörung? Datum, Empfänger, Zustellnachweis, Reaktion des BR

## Sub-Agent-Architektur

1. **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) liefert § 102 BetrVG mit URL, Kommentarstellen (APS, Fitting, ErfK) und die BAG-Linien zur subjektiven Determination.
2. **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) erstellt Anhörungsschreiben und Aktenvermerk zum Fristlauf.
3. **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft Vollständigkeit, Adressat, Fristberechnung und Dokumentation.

## Ablauf

### 1. Anhörungspflicht dem Grunde nach ([§ 102 Abs. 1 BetrVG](https://www.gesetze-im-internet.de/betrvg/__102.html))

Der Betriebsrat ist **vor jeder Kündigung** zu hören. Erfasst sind ausnahmslos:

- ordentliche und außerordentliche Kündigungen,
- Kündigungen in der Wartezeit (§ 1 Abs. 1 KSchG) und im Kleinbetrieb,
- Änderungskündigungen,
- Tat- **und** Verdachtskündigung — bei beabsichtigter Verdachtskündigung ist auch zum Verdacht anzuhören, sonst kann die Kündigung nicht auf ihn gestützt werden.

Nicht erfasst: Aufhebungsvertrag, Anfechtung, Fristablauf einer Befristung, Eigenkündigung des Arbeitnehmers.

**Adressat** ist der Betriebsratsvorsitzende oder im Verhinderungsfall sein Stellvertreter (§ 26 Abs. 2 BetrVG). Die Anhörung eines einfachen BR-Mitglieds genügt nicht.

### 2. Grundsatz der subjektiven Determination

Der Arbeitgeber muss dem Betriebsrat **die Gründe mitteilen, die aus seiner Sicht den Kündigungsentschluss tragen** — nicht mehr, aber auch nicht weniger. Der Umfang der Anhörung ist damit subjektiv determiniert (st. Rspr. des BAG zu § 102 BetrVG `[unverifiziert – prüfen]`).

Zwei Konsequenzen, die in der Praxis regelmäßig verwechselt werden:

1. **Nachschieben von Gründen ist ausgeschlossen.** Gründe, die dem Betriebsrat nicht mitgeteilt wurden, können im Prozess nicht zur Rechtfertigung der Kündigung herangezogen werden. Sollen sie verwertet werden, ist erneut anzuhören und ggf. erneut zu kündigen.
2. **Bewusst unvollständige Anhörung = fehlerhafte Anhörung.** Verschweigt der Arbeitgeber ihm bekannte, für den Arbeitnehmer entlastende Umstände, ist die Anhörung unwirksam. Objektiv unrichtige Angaben schaden dagegen nur, wenn der Arbeitgeber die Unrichtigkeit kannte oder sie bewusst irreführend darstellte.

Faustregel für den Entwurf: **Der Betriebsrat muss ohne eigene Nachforschung beurteilen können, ob er Bedenken erheben oder widersprechen will.** Schlagworte („Arbeitsverweigerung", „Umstrukturierung") genügen dafür nie.

### 3. Notwendiger Inhalt des Anhörungsschreibens

| Block | Inhalt |
|---|---|
| Person | Name, Geburtsdatum, Familienstand, Unterhaltspflichten, Eintrittsdatum, Funktion, Schwerbehinderung, Sonderkündigungsschutz |
| Kündigungsart | ordentlich / außerordentlich; bei ao. hilfsweise ordentlich → **beides** ausdrücklich benennen |
| Termin | Kündigungsfrist und Kündigungstermin, mit Berechnungsgrundlage (§ 622 BGB oder TV) |
| Gründe | Konkreter Sachverhalt: Datum, Ort, Verhalten, Zeugen; bei betriebsbedingter Kündigung: unternehmerische Entscheidung, Wegfall des Arbeitsplatzes, fehlende Weiterbeschäftigungsmöglichkeit |
| Sozialauswahl | Vergleichsgruppe, Kriterien, Gewichtung, Ergebnis (bei betriebsbedingter Kündigung) |
| Vorgeschichte | Abmahnungen mit Datum und Gegenstand; Anhörung des AN bei Verdachtskündigung |

### 4. Formulierungshilfe — Anhörungsschreiben

```
An den Betriebsrat
z. Hd. des Vorsitzenden, Herrn/Frau <Name>

Anhörung zur beabsichtigten ordentlichen Kündigung
gemäß § 102 Abs. 1 BetrVG

Sehr geehrte(r) Herr/Frau <Name>,

wir beabsichtigen, das Arbeitsverhältnis mit dem folgenden
Arbeitnehmer zu kündigen, und hören den Betriebsrat hierzu an.

I.   Angaben zur Person
     Name, Vorname:        <…>
     Geburtsdatum:         <…>
     Familienstand:        <…>, <N> unterhaltsberechtigte Kinder
     Eintrittsdatum:       <…>
     Tätigkeit / Abteilung:<…>
     Schwerbehinderung:    <ja, GdB <N>, Zustimmung Inklusionsamt vom
                            <Datum> / nein>
     Betriebsratsmandat:   <nein / ja — dann § 15 KSchG, § 103 BetrVG>

II.  Art der Kündigung
     Ordentliche Kündigung unter Einhaltung der Frist von
     <N> Monaten zum Monatsende gemäß § 622 Abs. 2 Nr. <N> BGB,
     mithin zum <Datum>.

III. Kündigungsgründe
     <Chronologische, konkrete Tatsachenschilderung mit Datum,
      Ort, Beteiligten und Zeugen. Keine Wertungen ohne die
      zugrunde liegenden Tatsachen. Bei verhaltensbedingter
      Kündigung: Abmahnungen mit Datum, Gegenstand und
      Aushändigungsnachweis auflisten. Bei betriebsbedingter
      Kündigung: unternehmerische Entscheidung, Zeitpunkt,
      Wegfall des Arbeitsplatzes, geprüfte und ausgeschlossene
      Weiterbeschäftigungsmöglichkeiten.>

IV.  Sozialauswahl (nur bei betriebsbedingter Kündigung)
     Vergleichsgruppe: <Bezeichnung, N Arbeitnehmer>
     Herangezogene Kriterien: Betriebszugehörigkeit, Lebensalter,
     Unterhaltspflichten, Schwerbehinderung.
     Auswahlergebnis: <…>  (Übersicht als Anlage 1 beigefügt)

V.   Stellungnahme
     Wir bitten um Stellungnahme innerhalb der Frist des
     § 102 Abs. 2 S. 1 BetrVG, also bis zum <Datum>.

Anlagen: <Sozialauswahlübersicht, Abmahnungen>

<Ort, Datum, Unterschrift des Kündigungsberechtigten>

Empfangsbestätigung Betriebsrat:
  Übergeben am <Datum>, <Uhrzeit>, an <Name, Funktion>
  Unterschrift: ____________________
```

### 5. Fristen ([§ 102 Abs. 2 BetrVG](https://www.gesetze-im-internet.de/betrvg/__102.html))

- **Ordentliche Kündigung:** Bedenken sind **spätestens innerhalb einer Woche** schriftlich unter Angabe der Gründe mitzuteilen. Schweigen gilt als Zustimmung (§ 102 Abs. 2 S. 2 BetrVG).
- **Außerordentliche Kündigung:** Bedenken unverzüglich, **spätestens innerhalb von drei Tagen** (§ 102 Abs. 2 S. 3 BetrVG).
- Die Kündigung darf erst **nach** Fristablauf oder nach abschließender Stellungnahme des Betriebsrats ausgesprochen werden. Eine vor Fristablauf erklärte Kündigung ist unwirksam — es sei denn, der Betriebsrat hat sich abschließend und erkennbar endgültig geäußert.
- Bei außerordentlicher Kündigung kollidiert die Anhörungsfrist mit der **2-Wochen-Frist des § 626 Abs. 2 BGB**: Die Anhörung hemmt diese Frist nicht. Der Arbeitgeber muss die Anhörung so früh einleiten, dass er nach Ablauf der drei Tage noch innerhalb der zwei Wochen kündigen kann.

### 6. Reaktion des Betriebsrats

| Reaktion | Rechtsfolge |
|---|---|
| Zustimmung / Schweigen | Kündigung nach Fristablauf möglich |
| **Bedenken** (§ 102 Abs. 2 BetrVG) | Kein Vetorecht; Kündigung möglich |
| **Widerspruch** (§ 102 Abs. 3 BetrVG) | Kündigung möglich, aber Abschrift der Stellungnahme ist dem AN mit der Kündigung zuzuleiten (§ 102 Abs. 4 BetrVG); Weiterbeschäftigungsanspruch § 102 Abs. 5 BetrVG |
| Zustimmungserfordernis nach § 103 BetrVG | Bei ao. Kündigung von Mandatsträgern: ohne Zustimmung bzw. deren Ersetzung durch das ArbG ist die Kündigung unwirksam |

Der Widerspruch ist nur beachtlich, wenn er auf einen der **fünf abschließenden Gründe** des § 102 Abs. 3 Nr. 1–5 BetrVG gestützt und innerhalb der Wochenfrist schriftlich erklärt wird: unzureichende Sozialauswahl, Verstoß gegen eine Auswahlrichtlinie (§ 95 BetrVG), Weiterbeschäftigung an anderem Arbeitsplatz, Weiterbeschäftigung nach Umschulung/Fortbildung, Weiterbeschäftigung zu geänderten Bedingungen mit Einverständnis des AN.

### 7. Fehlerkatalog — Prüfraster für die Gegenseite

1. Anhörung überhaupt erfolgt? Nachweis (Empfangsbestätigung, Zeuge)?
2. Adressat: Vorsitzender oder Stellvertreter (§ 26 Abs. 2 BetrVG)?
3. Sozialdaten vollständig und richtig?
4. Kündigungsart und -termin benannt? Bei „außerordentlich, hilfsweise ordentlich" **beide** Varianten?
5. Kündigungsgründe konkret statt schlagwortartig?
6. Bei betriebsbedingter Kündigung: Sozialauswahl dargestellt?
7. Bei Verdachtskündigung: zum **Verdacht** angehört, nicht nur zur Tat?
8. Entlastende, dem AG bekannte Umstände mitgeteilt?
9. Frist abgewartet (1 Woche / 3 Tage)?
10. Kündigung nach Abschluss des Verfahrens ausgesprochen, nicht vorher datiert?

Jeder bejahte Fehler in 1–9 führt zur Unwirksamkeit der Kündigung nach § 102 Abs. 1 S. 3 BetrVG — **aber nur, wenn er innerhalb der 3-Wochen-Frist des § 4 KSchG gerügt wird** (§ 7 KSchG).

## Deterministische Berechnung

Die Wochenfrist des § 102 Abs. 2 S. 1 BetrVG ist eine Ereignisfrist ([§ 187 Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__187.html)): Der Tag des Zugangs der Anhörung beim Betriebsrat zählt nicht mit. Der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) übernimmt **nur die Arithmetik**; ob und wann die Anhörung dem Vorsitzenden zugegangen ist und ob sie inhaltlich vollständig war, bleibt juristische Wertung.

```bash
# Anhörungsschreiben am 03.03.2026 dem BR-Vorsitzenden übergeben,
# ordentliche Kündigung → Wochenfrist § 102 Abs. 2 S. 1 BetrVG
python -m scripts.legal_calc.cli frist --ereignis 03.03.2026 --menge 1 --einheit wochen --land NW

# Außerordentliche Kündigung → 3 Tage, § 102 Abs. 2 S. 3 BetrVG
python -m scripts.legal_calc.cli frist --ereignis 03.03.2026 --menge 3 --einheit tage --land NW

# Gegenprobe: 2-Wochen-Frist § 626 Abs. 2 BGB ab Kenntnis vom Kündigungsgrund
python -m scripts.legal_calc.cli frist --ereignis 27.02.2026 --menge 2 --einheit wochen --land NW
```

Frühestens am Tag **nach** Fristablauf darf die Kündigung ausgesprochen werden. Das errechnete Datum ist in die Fristenakte einzutragen, das Kündigungsschreiben erst danach zu datieren und zuzustellen.

## Quellen

### Statute

- [§ 102 BetrVG](https://www.gesetze-im-internet.de/betrvg/__102.html), [§ 103 BetrVG](https://www.gesetze-im-internet.de/betrvg/__103.html), [§ 99 BetrVG](https://www.gesetze-im-internet.de/betrvg/__99.html)
- [§ 1 KSchG](https://www.gesetze-im-internet.de/kschg/__1.html), [§ 4 KSchG](https://www.gesetze-im-internet.de/kschg/__4.html), [§ 7 KSchG](https://www.gesetze-im-internet.de/kschg/__7.html), [§ 15 KSchG](https://www.gesetze-im-internet.de/kschg/__15.html)
- [§ 622 BGB](https://www.gesetze-im-internet.de/bgb/__622.html), [§ 626 BGB](https://www.gesetze-im-internet.de/bgb/__626.html), [§ 187 BGB](https://www.gesetze-im-internet.de/bgb/__187.html)

### Kommentare

- Becker / Wolff, in: APS, 6. Aufl. 2021, § 102 BetrVG Rn. 12 ff.
- Kania, in: ErfK, 24. Aufl. 2024, § 102 BetrVG Rn. 1 ff.
- Fitting, BetrVG, 32. Aufl. 2024, § 102 Rn. 20 ff. (subjektive Determination)
- Etzel, in: KR, 13. Aufl. 2022, § 102 BetrVG Rn. 60 ff. (Nachschieben von Gründen)

### Rechtsprechung

- st. Rspr. des BAG zu § 102 BetrVG (Grundsatz der subjektiven Determination) `[unverifiziert – prüfen]`
- st. Rspr. des BAG zu § 102 Abs. 1 S. 3 BetrVG (bewusst unvollständige Anhörung ist keine Anhörung) `[unverifiziert – prüfen]`
- st. Rspr. des BAG zur Verdachtskündigung (gesonderte Anhörung zum Verdacht erforderlich) `[unverifiziert – prüfen]`

> Aktenzeichen sind vor der Verwendung in juris, Beck-Online oder der [BAG-Entscheidungsdatenbank](https://www.bundesarbeitsgericht.de/entscheidungen/) zu ermitteln.

## Ausgabeformat

```
BR-ANHÖRUNG § 102 BetrVG — <Mandat-ID> — <Datum>
VERTRAULICH — MANDATSGEHEIMNIS — § 43a Abs. 2 BRAO

Gesamtbefund: [🟢 ordnungsgemäß / 🟡 nachbesserbar / 🔴 unwirksam]

I.    Anhörungspflicht                 [besteht / N/A kein BR]
II.   Adressat                         <Name, Funktion>  [🟢 / 🔴]
III.  Inhaltliche Vollständigkeit
      Sozialdaten                      [🟢 / 🔴 fehlt: <…>]
      Kündigungsart und -termin        [🟢 / 🔴]
      Kündigungsgründe konkret         [🟢 / 🔴 schlagwortartig]
      Sozialauswahl (bei bb)           [🟢 / 🔴 / N/A]
      Entlastende Umstände             [🟢 mitgeteilt / 🔴 verschwiegen]
IV.   Fristlauf
      Zugang beim BR:                  <Datum, Uhrzeit, Nachweis>
      Fristende:                       <Datum>  [scripts/legal_calc]
      Frühester Kündigungstermin:      <Datum>
V.    Reaktion des BR                  [Schweigen / Bedenken / Widerspruch
                                        § 102 Abs. 3 Nr. <N>]
VI.   Folge des Widerspruchs           [Abschrift beigefügt? Weiter-
                                        beschäftigung § 102 Abs. 5 BetrVG]
VII.  Fehlerkatalog                    <Nr. der bejahten Fehler>

Dokumentation zur Personalakte: <Empfangsbestätigung, Anlagen>
Empfehlung: <…>
```

## Risiken / typische Fehler

- **Kündigung vor Fristablauf ausgesprochen** — die häufigste Unwirksamkeitsursache. Nur eine abschließende, erkennbar endgültige Stellungnahme des Betriebsrats verkürzt die Frist.
- **Schlagwortartige Kündigungsgründe** („Minderleistung", „Vertrauensverlust") ohne Tatsachenunterbau — die Anhörung ist dann inhaltlich unvollständig.
- **Nachschieben von Kündigungsgründen** im Prozess, die dem Betriebsrat nie mitgeteilt wurden — nach dem Grundsatz der subjektiven Determination unverwertbar.
- **Anhörung an ein einfaches BR-Mitglied** statt an den Vorsitzenden oder dessen Stellvertreter (§ 26 Abs. 2 BetrVG).
- **Bei „außerordentlich, hilfsweise ordentlich" nur zur außerordentlichen Kündigung angehört** — die hilfsweise ordentliche Kündigung ist dann unwirksam.
- **Verdachtskündigung ohne Anhörung zum Verdacht** — der Verdacht kann im Prozess nicht als eigenständiger Kündigungsgrund herangezogen werden.
- **Kollision mit § 626 Abs. 2 BGB übersehen** — die Anhörungsfrist hemmt die 2-Wochen-Frist nicht.
- **Kein Zugangsnachweis** — ohne Empfangsbestätigung oder Zeugen ist der Fristlauf im Prozess nicht beweisbar.
- **Widerspruch des BR ignoriert** — die Abschrift der Stellungnahme ist dem Arbeitnehmer mit der Kündigung zuzuleiten (§ 102 Abs. 4 BetrVG).
