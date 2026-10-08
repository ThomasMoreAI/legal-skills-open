---
name: sozialauswahl-borghei
title: /arbeitsrecht:sozialauswahl
description: Durchführung und Angriff der Sozialauswahl bei betriebsbedingter Kündigung nach § 1 Abs. 3 KSchG – Bildung der Vergleichsgruppe (horizontale Vergleichbarkeit, Direktionsrecht § 106 GewO), die vier gesetzlichen Kriterien und ihre Gewichtung im Punkteschema, Herausnahme von Leistungsträgern § 1 Abs. 3 S. 2 KSchG, Auskunftsanspruch des Arbeitnehmers § 1 Abs. 3 S. 1 Hs. 2 KSchG, abgestufte Darlegungs- und Beweislast § 1 Abs. 3 S. 3 KSchG, Auswahlrichtlinie und Namensliste § 1 Abs. 4, 5 KSchG. Use when ein Arbeitgeber die Auswahlentscheidung dokumentationsfest treffen muss oder ein Arbeitnehmer die Sozialauswahl im Kündigungsschutzprozess angreift.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/arbeitsrecht/skills/sozialauswahl
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: employment
language: de
---

# /arbeitsrecht:sozialauswahl

## Zweck

Die betriebsbedingte Kündigung scheitert im Prozess selten am Wegfall des Arbeitsplatzes und fast immer an der Sozialauswahl. Der Grund ist ein struktureller: Die unternehmerische Entscheidung ist gerichtlich nur auf Willkür überprüfbar, die Auswahlentscheidung dagegen voll. Dieser Skill bildet die Vergleichsgruppe, bewertet die vier Kriterien und erzeugt eine Auswahldokumentation, die einer Kammerverhandlung standhält.

## Eingaben

- Vergleichsgruppen-Rohdaten je Arbeitnehmer: Eintrittsdatum, Geburtsdatum, Unterhaltspflichten (Lohnsteuerkarte / Zahl der Kinder, Ehegatte), GdB
- Tätigkeitsbeschreibungen und arbeitsvertragliche Versetzungsklauseln
- Betriebszuschnitt: Welcher Betrieb, welche Standorte? (Sozialauswahl ist **betriebsbezogen**, nicht unternehmensbezogen)
- Sonderkündigungsschutz einzelner Arbeitnehmer
- Existiert eine Auswahlrichtlinie nach § 95 BetrVG oder ein Interessenausgleich mit Namensliste?
- Auf Arbeitnehmerseite: Wurde bereits Auskunft nach § 1 Abs. 3 S. 1 Hs. 2 KSchG verlangt?

## Sub-Agent-Architektur

1. **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) liefert § 1 KSchG mit URL, Kommentarstellen zur Vergleichsgruppenbildung und die BAG-Linien zu Punkteschema und Leistungsträgerausnahme.
2. **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) erzeugt Vergleichsgruppenmatrix, Punktetabelle und Auswahlvermerk.
3. **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft Gruppenzuschnitt, Gewichtung, Herausnahmen und die Vollständigkeit der Dokumentation.

## Ablauf

### 1. Vorfrage: Ist die Sozialauswahl überhaupt eröffnet? ([§ 1 Abs. 3 KSchG](https://www.gesetze-im-internet.de/kschg/__1.html))

Die Sozialauswahl greift nur, wenn (a) das KSchG anwendbar ist ([§ 23 KSchG](https://www.gesetze-im-internet.de/kschg/__23.html), § 1 Abs. 1 KSchG), (b) **dringende betriebliche Erfordernisse** vorliegen und (c) mehr als ein Arbeitnehmer für die Kündigung in Betracht kommt. Bei personen- oder verhaltensbedingten Kündigungen findet keine Sozialauswahl statt.

### 2. Bildung der Vergleichsgruppe

Vergleichbar sind Arbeitnehmer, die **austauschbar** sind. Drei Filter, in dieser Reihenfolge:

1. **Betriebsbezogenheit.** Verglichen wird nur innerhalb desselben Betriebs. Ein Arbeitnehmer eines anderen Betriebs desselben Unternehmens ist nicht einzubeziehen — auch wenn er dieselbe Tätigkeit ausübt.
2. **Horizontale Vergleichbarkeit.** Verglichen wird nur auf derselben Ebene der Betriebshierarchie. Eine Kündigung „nach unten" auf eine geringerwertige Position ist keine Sozialauswahl (dort greift allenfalls die Änderungskündigung).
3. **Arbeitsvertragliche Austauschbarkeit.** Entscheidend ist, ob der Arbeitgeber den Arbeitnehmer kraft **Direktionsrecht** ([§ 106 GewO](https://www.gesetze-im-internet.de/gewo/__106.html)) einseitig auf den anderen Arbeitsplatz versetzen könnte. Wer nur mit Vertragsänderung versetzt werden könnte, ist nicht vergleichbar.

Ergänzend: **Qualifikatorische Austauschbarkeit** setzt voraus, dass der Arbeitnehmer die andere Tätigkeit nach kurzer Einarbeitungszeit ausüben kann — die Praxis arbeitet mit einer Orientierungsgröße von etwa drei Monaten; sie ist keine gesetzliche Grenze, sondern Einzelfallwertung.

**Nicht in die Auswahl einzubeziehen** sind ferner Arbeitnehmer, deren Kündigung ohnehin ausgeschlossen ist (Sonderkündigungsschutz nach § 15 KSchG, § 17 MuSchG, § 18 BEEG, § 168 SGB IX) sowie Arbeitnehmer in der Wartezeit des § 1 Abs. 1 KSchG — Letztere sind vorrangig zu kündigen, da sie keinen Kündigungsschutz genießen.

### 3. Die vier gesetzlichen Kriterien

§ 1 Abs. 3 S. 1 KSchG nennt **abschließend**:

| Kriterium | Bewertungslogik |
|---|---|
| Dauer der Betriebszugehörigkeit | Ab Eintrittsdatum; Vorbeschäftigungen bei Rechtsvorgängern nach § 613a BGB zählen mit |
| Lebensalter | Ambivalent: hohes Alter erhöht die Schutzwürdigkeit (Arbeitsmarktchancen), kann sie bei Rentennähe aber wieder senken |
| Unterhaltspflichten | Zahl der tatsächlich unterhaltsberechtigten Personen; Lohnsteuermerkmale sind Indiz, nicht Beweis |
| Schwerbehinderung | GdB ≥ 50 bzw. Gleichstellung; **zusätzlich** zum Zustimmungserfordernis des § 168 SGB IX |

Weitere Umstände (Betriebstreue in Krisenzeiten, Vermögensverhältnisse, Doppelverdienereigenschaft des Ehegatten) dürfen **nicht** berücksichtigt werden. Der Katalog ist seit 2004 abschließend.

### 4. Punkteschema

Ein gesetzliches Punkteschema gibt es **nicht**. Zulässig — und für die Beweisführung dringend zu empfehlen — ist ein selbst gesetztes Schema, das alle vier Kriterien angemessen berücksichtigt und keines dominieren lässt. Verbreitetes Muster:

```
Betriebszugehörigkeit    1 Punkt je vollem Jahr
                         (ggf. ab dem 11. Jahr 2 Punkte)
Lebensalter              1 Punkt je Lebensjahr ab dem 20. Lebensjahr,
                         gedeckelt bei <N> Punkten
Unterhaltspflichten      8 Punkte je unterhaltsberechtigtem Kind
                         4 Punkte für den unterhaltsberechtigten Ehegatten
Schwerbehinderung        5 Punkte bei GdB 50,
                         + 1 Punkt je 10 weiteren GdB-Punkten
```

Das Schema darf die **abschließende Einzelfallwürdigung nicht ersetzen**: Es ist eine Vorauswahl; ein knappes Punkteergebnis ist durch eine Schlussabwägung zu plausibilisieren. Wird das Schema durch **Auswahlrichtlinie** nach [§ 95 BetrVG](https://www.gesetze-im-internet.de/betrvg/__95.html) i.V.m. § 1 Abs. 4 KSchG vereinbart, ist die Gewichtung gerichtlich nur noch auf **grobe Fehlerhaftigkeit** überprüfbar — ein erheblicher prozessualer Vorteil für den Arbeitgeber.

Dasselbe gilt für die **Namensliste** in einem Interessenausgleich (§ 1 Abs. 5 KSchG): Vermutung der Betriebsbedingtheit und Prüfung der Sozialauswahl nur auf grobe Fehlerhaftigkeit.

### 5. Herausnahme von Leistungsträgern ([§ 1 Abs. 3 S. 2 KSchG](https://www.gesetze-im-internet.de/kschg/__1.html))

Nicht einzubeziehen sind Arbeitnehmer, deren Weiterbeschäftigung **insbesondere wegen ihrer Kenntnisse, Fähigkeiten und Leistungen oder zur Sicherung einer ausgewogenen Personalstruktur** im berechtigten betrieblichen Interesse liegt.

Prüfungsmaßstab in der Praxis:

- Der Arbeitgeber muss das betriebliche Interesse **konkret und arbeitsplatzbezogen** darlegen — pauschale Leistungsbewertungen genügen nicht.
- Es ist eine **Abwägung** zwischen dem betrieblichen Interesse und der Schutzwürdigkeit des verdrängten Arbeitnehmers vorzunehmen; je sozial schutzwürdiger dieser ist, desto gewichtiger muss das Interesse sein.
- „Ausgewogene Personalstruktur" rechtfertigt insbesondere die **Altersgruppenbildung**: Die Auswahl wird innerhalb proportional gebildeter Altersgruppen durchgeführt, um die vorhandene Altersstruktur zu erhalten. Das ist unionsrechtlich an Art. 6 RL 2000/78/EG bzw. § 10 AGG zu messen (st. Rspr. des BAG zur Altersgruppenbildung `[unverifiziert – prüfen]`).

Die Herausnahme ist die **Ausnahme**. Wird ein erheblicher Teil der Vergleichsgruppe herausgenommen, kippt die Auswahl regelmäßig.

### 6. Auskunftsanspruch des Arbeitnehmers ([§ 1 Abs. 3 S. 1 Hs. 2 KSchG](https://www.gesetze-im-internet.de/kschg/__1.html))

Auf Verlangen hat der Arbeitgeber dem Arbeitnehmer die Gründe anzugeben, die zu der getroffenen sozialen Auswahl geführt haben. Der Anspruch ist **außergerichtlich** geltend zu machen und richtet sich auf die Auswahlüberlegungen: Zuschnitt der Vergleichsgruppe, herangezogene Kriterien und deren Gewichtung, Ergebnis im Verhältnis zu den Vergleichspersonen.

**Prozessuale Hebelwirkung:** Verweigert der Arbeitgeber die Auskunft oder erteilt sie unvollständig, wirkt sich das auf die abgestufte Darlegungslast aus — der Arbeitnehmer genügt seiner Darlegungslast dann bereits mit der pauschalen Rüge, die Sozialauswahl sei fehlerhaft, und der Arbeitgeber muss die Auswahl vollständig offenlegen (st. Rspr. des BAG zur abgestuften Darlegungslast bei § 1 Abs. 3 KSchG `[unverifiziert – prüfen]`).

**Formulierungshilfe — Auskunftsverlangen:**

```
<Arbeitgeber>

Kündigung vom <Datum>; Auskunftsverlangen nach § 1 Abs. 3 S. 1
Hs. 2 KSchG

Sehr geehrte Damen und Herren,

namens meiner Mandantschaft verlange ich Auskunft über die Gründe,
die zu der getroffenen sozialen Auswahl geführt haben. Die Auskunft
möge insbesondere umfassen:

  1. den Zuschnitt der Vergleichsgruppe unter Angabe aller
     einbezogenen Arbeitnehmer (anonymisiert nach Personalnummer)
     und der Kriterien der Gruppenbildung,
  2. die vier Sozialdaten je Vergleichsperson (Betriebszugehörigkeit,
     Lebensalter, Unterhaltspflichten, Schwerbehinderung),
  3. das angewandte Punkteschema und dessen Gewichtung,
  4. die Namen und Gründe etwaiger Herausnahmen nach
     § 1 Abs. 3 S. 2 KSchG,
  5. eine etwaige Auswahlrichtlinie nach § 95 BetrVG.

Ich bitte um Erteilung bis zum <Datum>. Die Klagefrist des
§ 4 KSchG bleibt hiervon unberührt; die Klage wird fristwahrend
erhoben.

Mit freundlichen Grüßen
```

### 7. Darlegungs- und Beweislast ([§ 1 Abs. 3 S. 3 KSchG](https://www.gesetze-im-internet.de/kschg/__1.html))

Der **Arbeitnehmer** hat die Tatsachen zu beweisen, die die Kündigung als sozial ungerechtfertigt im Sinne des § 1 Abs. 3 S. 1 KSchG erscheinen lassen. Praktisch wird das durch die Abstufung entschärft:

1. Arbeitnehmer rügt die Sozialauswahl und verlangt Auskunft.
2. Arbeitgeber legt Vergleichsgruppe, Kriterien und Gewichtung offen.
3. Arbeitnehmer benennt konkret die Person, die aus seiner Sicht sozial weniger schutzwürdig ist, und trägt deren Sozialdaten vor.
4. Arbeitgeber führt den Gegenbeweis oder begründet die Herausnahme.

Für die **Herausnahme nach § 1 Abs. 3 S. 2 KSchG** trägt der Arbeitgeber von vornherein die volle Darlegungs- und Beweislast.

## Quellen

### Statute

- [§ 1 KSchG](https://www.gesetze-im-internet.de/kschg/__1.html), [§ 15 KSchG](https://www.gesetze-im-internet.de/kschg/__15.html), [§ 23 KSchG](https://www.gesetze-im-internet.de/kschg/__23.html)
- [§ 102 BetrVG](https://www.gesetze-im-internet.de/betrvg/__102.html), [§ 95 BetrVG](https://www.gesetze-im-internet.de/betrvg/__95.html), [§ 111 BetrVG](https://www.gesetze-im-internet.de/betrvg/__111.html)
- [§ 106 GewO](https://www.gesetze-im-internet.de/gewo/__106.html)
- [§ 613a BGB](https://www.gesetze-im-internet.de/bgb/__613a.html)
- [§ 168 SGB IX](https://www.gesetze-im-internet.de/sgb_9_2018/__168.html), [§ 10 AGG](https://www.gesetze-im-internet.de/agg/__10.html)

### Kommentare

- Linck, in: ErfK, 24. Aufl. 2024, § 1 KSchG Rn. 100 ff. (Sozialauswahl)
- Dörner / Vossen, in: KR, 13. Aufl. 2022, § 1 KSchG Rn. 350 ff.
- Kiel, in: APS, 6. Aufl. 2021, § 1 KSchG Rn. 700 ff. (Leistungsträger, Altersgruppen)
- Berkowsky, Die betriebsbedingte Kündigung, 7. Aufl. 2022, § 6 Rn. 1 ff.

### Rechtsprechung

- st. Rspr. des BAG zu § 1 Abs. 3 KSchG (arbeitsvertragsbezogene Vergleichbarkeit nach dem Direktionsrecht) `[unverifiziert – prüfen]`
- st. Rspr. des BAG zu § 1 Abs. 3 S. 2 KSchG (restriktive Handhabung der Leistungsträgerherausnahme, Abwägungserfordernis) `[unverifiziert – prüfen]`
- st. Rspr. des BAG zur Altersgruppenbildung und ihrer Vereinbarkeit mit § 10 AGG `[unverifiziert – prüfen]`
- st. Rspr. des BAG zur abgestuften Darlegungslast bei § 1 Abs. 3 KSchG `[unverifiziert – prüfen]`

> Aktenzeichen sind vor Verwendung in juris, Beck-Online oder der [BAG-Entscheidungsdatenbank](https://www.bundesarbeitsgericht.de/entscheidungen/) zu ermitteln.

## Ausgabeformat

```
SOZIALAUSWAHL § 1 Abs. 3 KSchG — <Mandat-ID> — <Datum>
VERTRAULICH — MANDATSGEHEIMNIS — § 43a Abs. 2 BRAO

Gesamtbefund: [🟢 tragfähig / 🟡 nachbesserungsbedürftig / 🔴 fehlerhaft]

I.    Eröffnung der Sozialauswahl        [🟢 / N/A]
II.   Betrieb                            <Bezeichnung, Standort>
III.  Vergleichsgruppe
      Kriterium der Gruppenbildung:      <Tätigkeit, Hierarchieebene>
      Austauschbarkeit § 106 GewO:       <Begründung>
      Einbezogen:                        <N> Arbeitnehmer
      Ausgeschlossen (Sonderschutz):     <N>  Gründe: <…>
      Ausgeschlossen (Wartezeit § 1 I):  <N>
IV.   Punkteschema                       <Gewichtung je Kriterium>
      Grundlage:                         [frei gesetzt / Auswahlrichtlinie
                                          § 95 BetrVG / Namensliste § 1 V]
V.    Auswahlmatrix
      Pers.-Nr. | BZ | Alter | Unterhalt | GdB | Punkte | Rang
      <…>
VI.   Herausnahmen § 1 Abs. 3 S. 2       <Pers.-Nr., konkretes betriebliches
                                          Interesse, Abwägung>
VII.  Auswahlergebnis                    Zu kündigen: <Pers.-Nr.>
VIII. Schlussabwägung                    <Plausibilisierung bei knappem
                                          Punkteabstand>
IX.   Auskunftsanspruch § 1 III 1 Hs. 2  [nicht verlangt / erteilt am <Datum>]

Dokumentation zur Personalakte: Auswahlvermerk vom <Datum>
Offene Tatsachenfragen: <…>
Empfehlung: <…>
```

## Risiken / typische Fehler

- **Vergleichsgruppe zu eng gezogen** — der häufigste Angriffspunkt. Wer die Gruppe auf „Team Nord" beschränkt, obwohl das Direktionsrecht eine Versetzung in „Team Süd" erlaubt, verliert die Auswahl.
- **Vergleichsgruppe unternehmensweit statt betriebsbezogen** gebildet — die Sozialauswahl ist betriebsbezogen; das andere Extrem ist ebenso fehlerhaft.
- **Punkteschema als abschließende Entscheidung** behandelt — die Einzelfallwürdigung bei knappen Abständen fehlt dann.
- **Leistungsträgerherausnahme pauschal begründet** („Herr X ist unser bester Mitarbeiter") — § 1 Abs. 3 S. 2 KSchG verlangt konkreten, arbeitsplatzbezogenen Vortrag und eine Abwägung.
- **Sachfremde Kriterien einbezogen** (Einkommen des Ehegatten, Vermögen, Krankheitstage) — der Katalog des § 1 Abs. 3 S. 1 KSchG ist abschließend.
- **Wartezeit-Arbeitnehmer in die Auswahl einbezogen** — sie genießen keinen Kündigungsschutz und sind vorrangig zu kündigen.
- **Auskunftsanspruch nicht oder unvollständig erfüllt** — verschiebt die Darlegungslast zulasten des Arbeitgebers.
- **Keine Auswahldokumentation zum Zeitpunkt der Entscheidung** — nachträglich erstellte Matrizen sind im Kammertermin wenig wert; nach Ablauf der Frist des § 4 KSchG ist praktisch nichts mehr nachzurüsten.
- **Altersgruppenbildung ohne Proportionalitätsnachweis** — ohne Darlegung der vorhandenen und der zu erhaltenden Altersstruktur droht der AGG-Verstoß.
