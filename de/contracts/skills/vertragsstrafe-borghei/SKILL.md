---
name: vertragsstrafe-borghei
title: /vertragsrecht:vertragsstrafe
description: Gestaltung und Prüfung von Vertragsstrafeklauseln nach §§ 339–345 BGB – Verwirkung § 339 BGB, Strafe für Nichterfüllung § 340 BGB und für nicht gehörige Erfüllung § 341 BGB mit Vorbehaltserfordernis, Herabsetzung durch das Gericht § 343 BGB und deren Ausschluss für Kaufleute § 348 HGB, AGB-Grenzen nach § 309 Nr. 6 BGB und § 307 BGB sowie die Ermessensstrafe nach Hamburger Brauch. Use when eine Vertragsstrafe vereinbart, verwirkt oder auf Wirksamkeit und Höhe geprüft werden soll.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/vertragsrecht/skills/vertragsstrafe
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: contracts
language: de
---

# /vertragsrecht:vertragsstrafe

## Zweck

Die Vertragsstrafe erfüllt zwei Funktionen zugleich: Sie übt **Erfüllungsdruck** aus und erleichtert die **Schadensliquidation** ohne Einzelnachweis. Beides macht sie in AGB angreifbar. Dieser Skill prüft Verwirkung, Höhe und Wirksamkeit einer Vertragsstrafeklausel und liefert Klauselbausteine, die der Inhaltskontrolle standhalten — einschließlich der Ermessensstrafe nach **Hamburger Brauch**, die in Unterlassungserklärungen der Standardweg ist.

## Eingaben

- Vertragstyp und Parteirollen (B2C, B2B, beiderseitiges Handelsgeschäft)
- Gesicherte Pflicht: Fertigstellungstermin, Wettbewerbsverbot, Geheimhaltung, Unterlassung, Abnahmepflicht
- Klauselwortlaut (Auslöser, Höhe, Obergrenze, Verschuldenserfordernis, Anrechnungsregel)
- Vorformuliert (AGB, §§ 305 ff. BGB) oder individuell ausgehandelt (§ 305 Abs. 1 S. 3 BGB)
- Bei bereits eingetretenem Verstoß: Datum, Dauer, Anzahl der Verstöße, Verschulden, entstandener Schaden
- Wurde die Leistung angenommen? Wurde der Vorbehalt nach § 341 Abs. 3 BGB erklärt?

## Sub-Agent-Architektur

1. **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) liefert die Statute mit URL, die AGB-rechtlichen Maßstäbe und Kommentarstellen zu Angemessenheitsgrenzen.
2. **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) prüft Wirksamkeit → Verwirkung → Vorbehalt → Höhe → Herabsetzung und entwirft die Klausel bzw. das Zahlungsverlangen.
3. **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft AGB-Kontrolle, Obergrenzen, Verschuldenserfordernis und den Vorbehalt bei Annahme.

## Ablauf

### 1. Verwirkung der Vertragsstrafe ([§ 339 BGB](https://www.gesetze-im-internet.de/bgb/__339.html))

Verspricht der Schuldner dem Gläubiger für den Fall, dass er seine Verbindlichkeit nicht oder nicht in gehöriger Weise erfüllt, die Zahlung einer Geldsumme als Strafe, so ist die Strafe **verwirkt, wenn er in Verzug kommt**. Besteht die geschuldete Leistung in einem **Unterlassen**, tritt die Verwirkung mit der **Zuwiderhandlung** ein (§ 339 S. 2 BGB).

Daraus folgt für Handlungspflichten: **Verzug ist Voraussetzung** — also Fälligkeit, Mahnung oder Entbehrlichkeit (§ 286 BGB) und **Vertretenmüssen** (§ 286 Abs. 4 BGB). Eine verschuldensunabhängige Vertragsstrafe ist in AGB nach § 307 BGB unwirksam. Details zum Verzugseintritt: `/vertragsrecht:verzug-mahnung`.

### 2. Strafe für Nichterfüllung ([§ 340 BGB](https://www.gesetze-im-internet.de/bgb/__340.html))

Hat der Schuldner die Strafe für den Fall versprochen, dass er seine Verbindlichkeit **nicht erfüllt**, kann der Gläubiger die verwirkte Strafe **statt der Erfüllung** verlangen; erklärt er dem Schuldner, dass er die Strafe verlange, ist der Anspruch auf Erfüllung ausgeschlossen. Steht dem Gläubiger ein Anspruch auf **Schadensersatz wegen Nichterfüllung** zu, kann er die verwirkte Strafe als **Mindestbetrag** des Schadens verlangen; die Geltendmachung eines weiteren Schadens ist nicht ausgeschlossen.

### 3. Strafe für nicht gehörige Erfüllung ([§ 341 BGB](https://www.gesetze-im-internet.de/bgb/__341.html))

Der praktisch wichtigste Fall — Verzögerung oder Schlechterfüllung. Der Gläubiger kann die verwirkte Strafe **neben der Erfüllung** verlangen. Auch hier gilt die Strafe als Mindestbetrag des Schadens (§ 341 Abs. 2 iVm § 340 Abs. 2 BGB).

**🔴 Vorbehalt bei der Annahme ([§ 341 Abs. 3 BGB](https://www.gesetze-im-internet.de/bgb/__341.html)):** Nimmt der Gläubiger die Erfüllung an, kann er die Strafe nur verlangen, wenn er sich **das Recht dazu bei der Annahme vorbehält**. Wer eine verspätete Bauleistung vorbehaltlos abnimmt, verliert die Vertragsstrafe endgültig — dieser Punkt ist der häufigste Anspruchsverlust in der Praxis. Der Vorbehalt ist im **Abnahmeprotokoll** ausdrücklich aufzunehmen.

### 4. Herabsetzung durch das Gericht ([§ 343 BGB](https://www.gesetze-im-internet.de/bgb/__343.html))

Ist eine verwirkte Strafe **unverhältnismäßig hoch**, kann sie auf Antrag des Schuldners durch Urteil auf den angemessenen Betrag herabgesetzt werden. Bei der Beurteilung ist **jedes berechtigte Interesse des Gläubigers**, nicht bloß das Vermögensinteresse, in Betracht zu ziehen. Nach der **Entrichtung** der Strafe ist die Herabsetzung ausgeschlossen (§ 343 Abs. 1 S. 3 BGB) — der Schuldner sollte daher nur **unter Vorbehalt** zahlen.

**Ausschluss für Kaufleute ([§ 348 HGB](https://www.gesetze-im-internet.de/hgb/__348.html)):** Eine Vertragsstrafe, die von einem **Kaufmann im Betriebe seines Handelsgewerbes** versprochen worden ist, kann **nicht** auf Grund des § 343 BGB herabgesetzt werden. Der kaufmännische Schuldner ist damit auf die allgemeinen Grenzen verwiesen: **AGB-Kontrolle** nach §§ 307 ff. BGB und **Sittenwidrigkeit** nach § 138 BGB. Genau deshalb verlagert sich der Streit im B2B vollständig auf die Wirksamkeit der Klausel.

### 5. AGB-Kontrolle ([§ 309 Nr. 6 BGB](https://www.gesetze-im-internet.de/bgb/__309.html))

**Klauselverbot ohne Wertungsmöglichkeit:** Unwirksam ist in AGB eine Bestimmung, durch die dem Verwender für den Fall der **Nichtabnahme oder verspäteten Abnahme** der Leistung, des **Zahlungsverzugs** oder für den Fall, dass der andere Vertragsteil sich **vom Vertrag löst**, die Zahlung einer Vertragsstrafe versprochen wird.

Im **B2B** gilt § 309 Nr. 6 BGB nicht unmittelbar, hat aber **Indizwirkung** über § 310 Abs. 1 S. 2 BGB. Zusätzlich prüft § 307 BGB stets mit:

| Prüfpunkt | Anforderung |
|---|---|
| Verschulden | Klausel muss Vertretenmüssen voraussetzen; verschuldensunabhängige Strafe unwirksam |
| Obergrenze | Bei Bauverträgen ist eine Gesamtobergrenze der verzugsbezogenen Vertragsstrafe erforderlich; als Grenze wird verbreitet ein Wert um **5 % der Auftragssumme** genannt `[unverifiziert – prüfen]` |
| Tagessatz | Verzugsstrafen je Werktag müssen in der Höhe angemessen bleiben; Tagessätze deutlich oberhalb von **0,2–0,3 % der Auftragssumme** gelten als angreifbar `[unverifiziert – prüfen]` |
| Anrechnung | Anrechnung auf den Schadensersatz muss erhalten bleiben (§ 340 Abs. 2 BGB) |
| Transparenz | Auslöser, Bemessungsgrundlage und Obergrenze müssen klar bestimmt sein (§ 307 Abs. 1 S. 2 BGB) |

**Keine geltungserhaltende Reduktion:** Eine überhöhte Vertragsstrafeklausel in AGB wird **nicht** auf das zulässige Maß zurückgeführt, sondern fällt ersatzlos weg (§ 306 Abs. 2 BGB). Der Verwender steht dann ohne jede Vertragsstrafe da — anders als beim Individualvertrag, wo § 343 BGB nur herabsetzt. Details: `/vertragsrecht:agb-kontrolle`.

**Klauselbaustein Verzugsvertragsstrafe (B2B, Werkvertrag):**

> „Überschreitet der Auftragnehmer den vereinbarten Fertigstellungstermin aus einem von ihm zu vertretenden Grund, schuldet er eine Vertragsstrafe in Höhe von **0,2 % der Netto-Auftragssumme je Werktag** der Überschreitung, **insgesamt jedoch höchstens 5 % der Netto-Auftragssumme**. Die Vertragsstrafe wird auf einen Schadensersatzanspruch des Auftraggebers wegen des Verzugs **angerechnet**. Der Auftraggeber behält sich die Geltendmachung der Vertragsstrafe bei Abnahme ausdrücklich vor (§ 341 Abs. 3 BGB)."

**Negativbeispiel und Neufassung:**

| Unwirksame Fassung | Fehler | Neufassung |
|---|---|---|
| „Bei Terminüberschreitung zahlt der Auftragnehmer 1 % der Auftragssumme je Kalendertag." | Kein Verschulden, keine Obergrenze, Kalendertage statt Werktage, Tagessatz überhöht | „…je **Werktag** der von ihm **zu vertretenden** Überschreitung 0,2 %, **insgesamt höchstens 5 %**…" |
| „Die Vertragsstrafe wird neben dem Schadensersatz geschuldet." | Anrechnung nach § 340 Abs. 2 BGB abbedungen | „Die Vertragsstrafe wird auf einen Schadensersatzanspruch **angerechnet**." |
| „Bei Lösung vom Vertrag schuldet der Kunde eine Vertragsstrafe von 20 % des Auftragswerts." | Verstoß gegen § 309 Nr. 6 BGB (B2C) | Ersatzlos streichen; stattdessen Schadenspauschale nach § 309 Nr. 5 BGB mit Gegenbeweisvorbehalt |

### 6. Hamburger Brauch — Vertragsstrafe nach billigem Ermessen

In **strafbewehrten Unterlassungserklärungen** wird die Vertragsstrafe regelmäßig nicht beziffert, sondern nach dem **Hamburger Brauch** ausgestaltet: Die Höhe bestimmt der Gläubiger im Einzelfall nach **billigem Ermessen** ([§ 315 BGB](https://www.gesetze-im-internet.de/bgb/__315.html)); die Angemessenheit ist im Streitfall **vom Gericht vollständig überprüfbar** (§ 315 Abs. 3 BGB).

Vorteile: Die Klausel vermeidet den Streit über eine im Voraus zu hoch oder zu niedrig bezifferte Strafe und ist deshalb der AGB-Kontrolle weniger ausgesetzt. Sie beseitigt zugleich für den Schuldner das Risiko, dass eine feste Strafe bei einem Bagatellverstoß greift.

**Klauselbaustein Hamburger Brauch:**

> „Der Schuldner verpflichtet sich, es bei Meidung einer für jeden Fall der Zuwiderhandlung fälligen **Vertragsstrafe, deren Höhe der Gläubiger nach billigem Ermessen bestimmt und deren Angemessenheit im Streitfall vom zuständigen Gericht zu überprüfen ist**, zu unterlassen, [konkrete Handlung]."

Ergänzend ist zu regeln, ob mehrere Verstöße als **einheitliche Zuwiderhandlung** zusammengefasst werden („Fortsetzungszusammenhang") — ohne eine solche Regelung kann sich die Strafe bei Dauerhandlungen vervielfachen.

### 7. Abgrenzung und flankierende Regelungen

- **Pauschalierter Schadensersatz** ist keine Vertragsstrafe: Er ersetzt nur den Nachweis der Schadenshöhe, übt keinen Erfüllungsdruck aus. In AGB verlangt § 309 Nr. 5 BGB, dass die Pauschale den gewöhnlichen Schadensverlauf nicht übersteigt **und** der Gegenseite der Nachweis eines geringeren Schadens ausdrücklich gestattet wird. **Fehlt dieser Vorbehalt, ist die Klausel unwirksam.**
- **Unwirksames Strafversprechen** ([§ 344 BGB](https://www.gesetze-im-internet.de/bgb/__344.html)): Ist die versprochene Leistung unwirksam, so ist auch das Strafversprechen unwirksam — die Vertragsstrafe kann keine nichtige Hauptpflicht absichern.
- **Beweislast** ([§ 345 BGB](https://www.gesetze-im-internet.de/bgb/__345.html)): Bestreitet der Schuldner die Verwirkung, weil er seine Verbindlichkeit erfüllt habe, so hat **er** die Erfüllung zu beweisen, sofern nicht die geschuldete Leistung in einem Unterlassen besteht.
- **Andere Leistung als Strafe** (§ 342 BGB): Auch eine nicht in Geld bestehende Leistung kann Vertragsstrafe sein.

## Quellen

### Statute

- [§ 339 BGB](https://www.gesetze-im-internet.de/bgb/__339.html), [§ 340 BGB](https://www.gesetze-im-internet.de/bgb/__340.html), [§ 341 BGB](https://www.gesetze-im-internet.de/bgb/__341.html), [§ 343 BGB](https://www.gesetze-im-internet.de/bgb/__343.html), [§ 344 BGB](https://www.gesetze-im-internet.de/bgb/__344.html), [§ 345 BGB](https://www.gesetze-im-internet.de/bgb/__345.html)
- [§ 307 BGB](https://www.gesetze-im-internet.de/bgb/__307.html), [§ 309 BGB](https://www.gesetze-im-internet.de/bgb/__309.html) (Nr. 5, Nr. 6), [§ 315 BGB](https://www.gesetze-im-internet.de/bgb/__315.html), [§ 286 BGB](https://www.gesetze-im-internet.de/bgb/__286.html)
- [§ 348 HGB](https://www.gesetze-im-internet.de/hgb/__348.html)

### Kommentare

- Grüneberg, BGB, 83. Aufl. 2024, §§ 339–345 Rn. 1 ff. `[unverifiziert – Auflagenstand prüfen]`
- Gottwald, in: MüKoBGB, 9. Aufl. 2022, § 339 Rn. 1 ff., § 343 Rn. 1 ff.
- Wurmnest, in: MüKoBGB, 9. Aufl. 2022, § 309 Nr. 6 Rn. 1 ff.

### Rechtsprechung

- BGH, Urt. v. 23.01.2003 – VII ZR 210/01 (Obergrenze der Vertragsstrafe im Bauvertrag) `[unverifiziert – prüfen]`
- BGH, Urt. v. 20.01.2016 – VIII ZR 26/15 (Vertragsstrafe in AGB, Angemessenheit) `[unverifiziert – prüfen]`

> Beide Aktenzeichen und die genannten Prozentgrenzen vor Verwendung in juris / Beck-Online prüfen — die Grenzwerte sind einzelfall- und branchenabhängig.

## Ausgabeformat

```
VERTRAGSSTRAFE — <Vertrag / Klausel> — <Datum>

I.    Gesicherte Pflicht              [Termin / Unterlassung / Geheimhaltung / Wettbewerb]
II.   Klauselart                      [AGB §§ 305 ff. / Individualvereinbarung]
III.  Verwirkung (§ 339)              [✅ Verzug bzw. Zuwiderhandlung / ❌ — Begründung]
        Vertretenmüssen:              [✅ / ❌]
IV.   Anspruchsrichtung               [§ 340 statt Erfüllung / § 341 neben Erfüllung]
V.    Vorbehalt bei Annahme (§ 341 III) [✅ erklärt am <Datum> / 🔴 fehlt — Anspruch verloren]
VI.   AGB-Kontrolle                   [§ 309 Nr. 6 / § 307 — Befund]
        Obergrenze:                   <…> % der Auftragssumme
        Tagessatz:                    <…> %
        Anrechnung § 340 II:          [✅ / ❌]
VII.  Herabsetzung (§ 343)            [möglich / ausgeschlossen § 348 HGB / bereits entrichtet]
VIII. Hamburger Brauch                [verwendet — § 315 BGB / beziffert]
IX.   Betrag                          <…> EUR (Berechnung: <…>)

Gesamtbefund: [🟢 / 🟡 / 🔴]
Offene Tatsachen: <Liste>
```

## Risiken / typische Fehler

- **Vorbehalt bei der Annahme vergessen** — wer die Leistung vorbehaltlos annimmt, verliert die Vertragsstrafe für nicht gehörige Erfüllung endgültig (§ 341 Abs. 3 BGB).
- **Vertragsstrafe ohne Obergrenze** in AGB vereinbart — unwirksam nach § 307 BGB; wegen des Verbots der geltungserhaltenden Reduktion entfällt die Strafe vollständig.
- **Verschuldensunabhängige Vertragsstrafe** formuliert — § 339 BGB setzt Verzug und damit Vertretenmüssen voraus; die Klausel ist in AGB unwirksam.
- **§ 348 HGB übersehen** — beim kaufmännischen Schuldner scheidet die Herabsetzung nach § 343 BGB aus; die Verteidigung muss über AGB-Kontrolle und § 138 BGB laufen.
- **Vertragsstrafe entrichtet ohne Vorbehalt** — nach der Entrichtung ist die Herabsetzung nach § 343 Abs. 1 S. 3 BGB ausgeschlossen.
- **Pauschalierten Schadensersatz mit Vertragsstrafe verwechselt** — § 309 Nr. 5 BGB verlangt den ausdrücklichen Vorbehalt des Nachweises eines geringeren Schadens; ohne ihn ist die Klausel unwirksam.
