---
name: ruecktritt-schadensersatz-borghei
title: /vertragsrecht:ruecktritt-schadensersatz
description: Prüfung von Rücktritt und Schadensersatz wegen Leistungsstörung – Schadensersatz statt der Leistung §§ 280, 281 BGB, Unmöglichkeit §§ 275, 283, 326 BGB, Rücktritt nach Fristsetzung § 323 BGB und Entbehrlichkeit § 323 Abs. 2 BGB, Nebeneinander von Rücktritt und Schadensersatz § 325 BGB sowie Rückabwicklung mit Nutzungs- und Wertersatz §§ 346, 347 BGB. Use when eine Vertragspartei nicht, zu spät oder schlecht leistet und geklärt werden soll, ob eine Nachfrist zu setzen ist und welche Sekundärrechte in welcher Kombination bestehen.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/vertragsrecht/skills/ruecktritt-schadensersatz
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: contracts
language: de
---

# /vertragsrecht:ruecktritt-schadensersatz

## Zweck

Das Leistungsstörungsrecht der §§ 280 ff. BGB ist ein Weichensystem: Fast jeder Sekundäranspruch hängt davon ab, ob eine **Nachfrist** gesetzt wurde oder entbehrlich war. Dieser Skill bestimmt zuerst die Störungsart (Unmöglichkeit, Verzögerung, Schlechtleistung, Nebenpflichtverletzung), setzt dann die richtige Weiche und liefert die Formulierungshilfen für Nachfristschreiben und Rücktrittserklärung samt Rückabwicklungsbilanz.

## Eingaben

- Vertrag (Typ, Datum, geschuldete Leistung, Gegenleistung, Termine)
- Störungsart: Nichtleistung, Verspätung, Schlechtleistung, Verletzung einer Rücksichtnahmepflicht (§ 241 Abs. 2 BGB)
- Bereits gesetzte Fristen (Datum, Wortlaut, Zugang) und Reaktion der Gegenseite
- Vertretenmüssen: Verschulden, Übernahme einer Garantie, Beschaffungsrisiko (§ 276 BGB)
- Bereits erbrachte Leistungen, gezogene Nutzungen, Verschlechterung oder Untergang des Leistungsgegenstands
- Bezifferter Schaden und Belege; Mitverschulden (§ 254 BGB)

## Sub-Agent-Architektur

1. **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) liefert Statute mit URL, Kommentarstellen (Grüneberg, MüKoBGB, Staudinger) und nur belegbare Rechtsprechung mit Verifikationsmarker.
2. **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) prüft Störungsart → Fristsetzung/Entbehrlichkeit → Rücktritt → Schadensersatz → Rückabwicklung und entwirft die Erklärungen.
3. **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft Bestimmtheit und Angemessenheit der Frist, Zugangsnachweis, Erheblichkeitsschwelle und Verjährung.

## Ablauf

### 1. Störungsart bestimmen ([§ 280 BGB](https://www.gesetze-im-internet.de/bgb/__280.html))

§ 280 Abs. 1 BGB ist die **Grundnorm**: Verletzt der Schuldner eine Pflicht aus dem Schuldverhältnis, kann der Gläubiger Ersatz des hierdurch entstehenden Schadens verlangen; das Vertretenmüssen wird **vermutet** (§ 280 Abs. 1 S. 2 BGB). Von dort verzweigt die Prüfung:

| Störung | Schadensersatz | Rücktritt |
|---|---|---|
| Nichtleistung trotz Möglichkeit | §§ 280 Abs. 1, 3, 281 BGB (Fristsetzung) | § 323 BGB (Fristsetzung) |
| Unmöglichkeit (§ 275 BGB) | §§ 280 Abs. 1, 3, 283 BGB; anfänglich: § 311a Abs. 2 BGB | § 326 Abs. 5 BGB — **ohne** Fristsetzung |
| Verzögerung (Verzugsschaden) | § 280 Abs. 1, 2 iVm § 286 BGB | § 323 BGB |
| Schlechtleistung | §§ 437, 634 BGB (Sonderrecht) iVm §§ 280, 281 BGB | §§ 437 Nr. 2, 634 Nr. 3 iVm § 323 BGB |
| Verletzung § 241 Abs. 2 BGB | § 280 Abs. 1 BGB; § 282 BGB bei Unzumutbarkeit | § 324 BGB |

### 2. Unmöglichkeit ([§ 275 BGB](https://www.gesetze-im-internet.de/bgb/__275.html))

Der Anspruch auf Leistung ist ausgeschlossen, soweit die Leistung für den Schuldner oder für jedermann **unmöglich** ist (§ 275 Abs. 1 BGB). Hinzu treten die Einreden der **faktischen Unmöglichkeit** wegen grobem Missverhältnis (§ 275 Abs. 2 BGB) und der **persönlichen Unzumutbarkeit** (§ 275 Abs. 3 BGB) — beide muss der Schuldner erheben.

Rechtsfolgen: Der Gegenleistungsanspruch entfällt automatisch ([§ 326 Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__326.html)); bereits Geleistetes ist nach § 326 Abs. 4 BGB zurückzugewähren. Ein **Rücktritt ist ohne Fristsetzung** möglich (§ 326 Abs. 5 BGB) und bleibt sinnvoll, wenn der Gläubiger die Rückabwicklung nach §§ 346 ff. BGB will. Schadensersatz statt der Leistung richtet sich nach [§ 283 BGB](https://www.gesetze-im-internet.de/bgb/__283.html) (nachträgliche) bzw. § 311a Abs. 2 BGB (anfängliche Unmöglichkeit).

### 3. Nachfristsetzung ([§ 281 BGB](https://www.gesetze-im-internet.de/bgb/__281.html), [§ 323 BGB](https://www.gesetze-im-internet.de/bgb/__323.html))

Beide Normen verlangen dieselbe **Fristsetzung**: eine bestimmte, ernsthafte Aufforderung zur Leistung mit angemessener Frist. Anforderungen:

- **Bestimmtheit:** konkretes Kalenderdatum („bis zum 05.08.2026"), nicht „umgehend" oder „kurzfristig".
- **Angemessenheit:** so bemessen, dass der Schuldner eine bereits begonnene Leistung fertigstellen kann. Eine **zu kurze** Frist ist nicht unwirksam, sondern setzt eine **angemessene** Frist in Lauf.
- **Keine Ablehnungsandrohung erforderlich** — anders als nach altem Recht. Ein Hinweis auf die beabsichtigten Folgen ist gleichwohl empfehlenswert.

**Formulierungshilfe Nachfristschreiben:**

> „Aus dem Vertrag vom [Datum] schulden Sie [Leistung]. Die Leistung ist seit dem [Datum] fällig; sie ist bis heute nicht erbracht. Ich fordere Sie hiermit auf, die geschuldete Leistung bis zum **[konkretes Kalenderdatum]** vollständig zu erbringen. Nach fruchtlosem Ablauf dieser Frist werde ich vom Vertrag zurücktreten (§ 323 BGB) und Schadensersatz statt der Leistung verlangen (§ 281 BGB). Weitergehende Ansprüche, insbesondere auf Ersatz des Verzögerungsschadens, bleiben vorbehalten."

Die **Deterministische Berechnung** des Fristendes erfolgt über den Rechner (siehe Abschnitt am Ende).

### 4. Entbehrlichkeit der Fristsetzung ([§ 323 Abs. 2 BGB](https://www.gesetze-im-internet.de/bgb/__323.html))

Die Fristsetzung ist entbehrlich, wenn

- der Schuldner die Leistung **ernsthaft und endgültig verweigert** (§ 323 Abs. 2 Nr. 1 BGB) — hohe Schwelle, bloßes Bestreiten oder Verhandeln genügt nicht;
- der Schuldner die Leistung zu einem im Vertrag bestimmten Termin nicht erbringt und der Gläubiger im Vertrag den **Fortbestand seines Leistungsinteresses an die Rechtzeitigkeit gebunden** hat (§ 323 Abs. 2 Nr. 2 BGB — relatives Fixgeschäft);
- **besondere Umstände** unter Abwägung der beiderseitigen Interessen den sofortigen Rücktritt rechtfertigen (§ 323 Abs. 2 Nr. 3 BGB).

Parallel dazu § 281 Abs. 2 BGB für den Schadensersatz. Bei Schlechtleistung tritt § 440 BGB (Kauf) bzw. § 636 BGB (Werkvertrag) hinzu. **Wer sich auf Entbehrlichkeit stützt, trägt dafür die Darlegungs- und Beweislast** — im Zweifel ist die Frist zu setzen; sie kostet nichts als Zeit.

### 5. Rücktrittserklärung und Ausschluss ([§ 349 BGB](https://www.gesetze-im-internet.de/bgb/__349.html))

Der Rücktritt erfolgt durch **empfangsbedürftige Willenserklärung** gegenüber dem anderen Teil. Er ist bedingungsfeindlich und unwiderruflich.

Ausschlussgründe:

- **Unerhebliche Pflichtverletzung** (§ 323 Abs. 5 S. 2 BGB) — bei behebbaren Sachmängeln orientiert sich die Praxis an einem Mangelbeseitigungsaufwand von rund 5 % des Kaufpreises als Richtwert `[unverifiziert – prüfen]`.
- **Überwiegende oder alleinige Verantwortlichkeit des Gläubigers** (§ 323 Abs. 6 BGB).
- Teilleistung: Rücktritt vom ganzen Vertrag nur bei fehlendem Interesse an der Teilleistung (§ 323 Abs. 5 S. 1 BGB).

### 6. Rücktritt und Schadensersatz nebeneinander ([§ 325 BGB](https://www.gesetze-im-internet.de/bgb/__325.html))

Das Recht, bei einem gegenseitigen Vertrag Schadensersatz zu verlangen, wird durch den Rücktritt **nicht ausgeschlossen**. Der Gläubiger kann also zurücktreten **und** Schadensersatz statt der Leistung verlangen. Berechnet wird der Schaden dann nach der **Surrogationsmethode** oder der **Differenzmethode**; doppelte Kompensation ist ausgeschlossen — der bereits über die Rückabwicklung erlangte Vorteil ist anzurechnen.

### 7. Rückabwicklung ([§ 346 BGB](https://www.gesetze-im-internet.de/bgb/__346.html))

Die empfangenen Leistungen sind **Zug um Zug** zurückzugewähren und die gezogenen **Nutzungen herauszugeben** (§ 346 Abs. 1 BGB).

**Wertersatz statt Rückgewähr** (§ 346 Abs. 2 BGB), wenn

1. die Rückgewähr nach der Natur des Erlangten ausgeschlossen ist (Dienstleistungen, Gebrauchsvorteile),
2. der Gegenstand verbraucht, veräußert, belastet, verarbeitet oder umgestaltet wurde,
3. der Gegenstand sich verschlechtert hat oder untergegangen ist — außer bei bestimmungsgemäßer Ingebrauchnahme.

Maßstab ist die im Vertrag bestimmte **Gegenleistung**. **Nutzungsersatz** bei Gebrauchsgegenständen wird regelmäßig nach der linearen Formel berechnet:

```
Nutzungsentschädigung = Bruttopreis × gefahrene / genutzte Einheiten
                        / voraussichtliche Gesamtnutzungsdauer
```

**Wegfall der Wertersatzpflicht** (§ 346 Abs. 3 BGB): u.a. wenn sich der Mangel erst bei der Verarbeitung gezeigt hat, der Gläubiger die Verschlechterung zu vertreten hat, oder — beim gesetzlichen Rücktrittsrecht — der Berechtigte diejenige Sorgfalt beachtet hat, die er in eigenen Angelegenheiten anzuwenden pflegt (§ 346 Abs. 3 S. 1 Nr. 3 BGB). Bei Verletzung der Pflichten aus § 346 BGB haftet der Rücktrittsgegner nach [§ 347 BGB](https://www.gesetze-im-internet.de/bgb/__347.html) auf schuldhaft nicht gezogene Nutzungen.

### 8. Schadensberechnung und Grenzen

- **Differenzmethode:** Der Gläubiger gibt die eigene Gegenleistung nicht hin und verlangt die Differenz zwischen dem Wert der ausgebliebenen Leistung und der ersparten Gegenleistung.
- **Surrogationsmethode:** Der Gläubiger erbringt die Gegenleistung und verlangt den vollen Wert der ausgebliebenen Leistung.
- **Deckungsgeschäft:** Mehrkosten eines konkreten Deckungskaufs sind ersatzfähig, soweit er marktüblich und unverzüglich erfolgt (§ 254 Abs. 2 BGB — Schadensminderungspflicht).
- **Entgangener Gewinn** § 252 BGB; **Aufwendungsersatz** § 284 BGB als Alternative bei nicht nachweisbarem Gewinn.
- **Mitverschulden** § 254 BGB und Vorteilsausgleichung stets prüfen.

## Deterministische Berechnung

Die Angemessenheit einer Nachfrist ist eine **rechtliche Wertung** und bleibt Eingabe. Das Fristende ist reine Arithmetik nach §§ 187–193 BGB und wird deterministisch berechnet (siehe [`../../references/rechner.md`](../../references/rechner.md)):

```bash
python -m scripts.legal_calc.cli frist --ereignis 15.01.2026 --menge 2 --einheit wochen --land BY
```

Der Rechner gibt Fristbeginn, Fristende und die Rechenschritte mit Normzitat aus — einschließlich der Verschiebung auf den nächsten Werktag nach § 193 BGB, die bei Fristen zugunsten des Schuldners regelmäßig übersehen wird. Das Bundesland (`--land`) ist anzugeben, weil die gesetzlichen Feiertage landesrechtlich bestimmt sind. **Welches Ereignis den Fristlauf auslöst — Zugang des Nachfristschreibens, nicht dessen Absendung — bleibt juristische Wertung und muss als `--ereignis` korrekt eingegeben werden.**

## Quellen

### Statute

- [§ 275 BGB](https://www.gesetze-im-internet.de/bgb/__275.html), [§ 280 BGB](https://www.gesetze-im-internet.de/bgb/__280.html), [§ 281 BGB](https://www.gesetze-im-internet.de/bgb/__281.html), [§ 283 BGB](https://www.gesetze-im-internet.de/bgb/__283.html), [§ 284 BGB](https://www.gesetze-im-internet.de/bgb/__284.html), [§ 286 BGB](https://www.gesetze-im-internet.de/bgb/__286.html)
- [§ 323 BGB](https://www.gesetze-im-internet.de/bgb/__323.html), [§ 324 BGB](https://www.gesetze-im-internet.de/bgb/__324.html), [§ 325 BGB](https://www.gesetze-im-internet.de/bgb/__325.html), [§ 326 BGB](https://www.gesetze-im-internet.de/bgb/__326.html)
- [§ 346 BGB](https://www.gesetze-im-internet.de/bgb/__346.html), [§ 347 BGB](https://www.gesetze-im-internet.de/bgb/__347.html), [§ 348 BGB](https://www.gesetze-im-internet.de/bgb/__348.html), [§ 349 BGB](https://www.gesetze-im-internet.de/bgb/__349.html)
- [§ 249 BGB](https://www.gesetze-im-internet.de/bgb/__249.html), [§ 252 BGB](https://www.gesetze-im-internet.de/bgb/__252.html), [§ 254 BGB](https://www.gesetze-im-internet.de/bgb/__254.html), [§ 276 BGB](https://www.gesetze-im-internet.de/bgb/__276.html)

### Kommentare

- Grüneberg, BGB, 83. Aufl. 2024, §§ 281, 323, 346 Rn. 1 ff. `[unverifiziert – Auflagenstand prüfen]`
- Ernst, in: MüKoBGB, 9. Aufl. 2022, § 323 Rn. 1 ff., § 325 Rn. 1 ff.
- Gaier, in: MüKoBGB, 9. Aufl. 2022, § 346 Rn. 1 ff. (Rückabwicklung, Wertersatz)

### Rechtsprechung

- BGH, Urt. v. 28.05.2014 – VIII ZR 94/13 (Erheblichkeitsschwelle § 323 Abs. 5 S. 2 BGB, Richtwert 5 %) `[unverifiziert – prüfen]`
- BGH, Urt. v. 12.08.2009 – VIII ZR 254/08 (zu kurze Frist setzt angemessene Frist in Lauf) `[unverifiziert – prüfen]`

> Beide Aktenzeichen vor Verwendung in juris / Beck-Online prüfen. Die tragenden Aussagen folgen aus dem Gesetzeswortlaut.

## Ausgabeformat

```
RÜCKTRITT / SCHADENSERSATZ — <Vertrag> — <Datum>

I.    Störungsart                     [Unmöglichkeit / Nichtleistung / Verzug / Schlechtleistung / § 241 II]
II.   Fristsetzung                    [gesetzt am <Datum>, Ablauf <Datum> / entbehrlich § 323 II Nr. <…>]
        Rechner-Beleg:                <Ausgabe legal_calc frist>
III.  Vertretenmüssen (§ 276)         [✅ vermutet / widerlegt — Begründung]
IV.   Rücktritt (§ 323)               [möglich / ausgeschlossen § 323 V 2, § 323 VI]
        Erklärung erfolgt am:         <Datum, Zugangsnachweis>
V.    Schadensersatz                  [§ 281 statt der Leistung / § 280 II, 286 Verzug / § 283 / § 311a II]
        Methode:                      [Differenz / Surrogation]
        Betrag:                       <…> EUR
VI.   Nebeneinander (§ 325)           [beides geltend gemacht — Anrechnung: <…>]
VII.  Rückabwicklung (§§ 346, 347)    [Rückgewähr / Wertersatz § 346 II — <…> EUR]
        Nutzungsersatz:               <Berechnung>
VIII. Mitverschulden (§ 254)          [N/A / Quote <…> %]
IX.   Verjährung                      [§§ 195, 199 / § 438 / § 634a — Ende <TT.MM.JJJJ>]

Gesamtbefund: [🟢 / 🟡 / 🔴]
Offene Tatsachen: <Liste>
```

## Risiken / typische Fehler

- **Rücktritt ohne wirksame Fristsetzung** — die häufigste Ursache dafür, dass der Rücktritt ins Leere geht und der Erklärende selbst in Annahmeverzug oder Zahlungsverzug gerät.
- **Frist ohne konkretes Kalenderdatum** („umgehend", „kurzfristig") — Bestimmtheit fehlt, der Fristlauf beginnt nicht.
- **Entbehrlichkeit vorschnell angenommen** — bloßes Bestreiten der Mangelhaftigkeit ist noch keine ernsthafte und endgültige Leistungsverweigerung nach § 323 Abs. 2 Nr. 1 BGB.
- **§ 325 BGB übersehen** — Rücktritt und Schadensersatz schließen einander nicht aus; wer nur zurücktritt, verschenkt den Ersatz des Nichterfüllungsschadens.
- **Nutzungsersatz nicht angerechnet** — bei der Rückabwicklung nach §§ 346, 347 BGB sind gezogene Nutzungen herauszugeben; die Bilanz fällt sonst falsch aus.
- **Fristende frei geschätzt statt gerechnet** — §§ 187–193 BGB mit Feiertagsverschiebung über `scripts/legal_calc` bestimmen, sonst droht eine um Tage verfehlte Rücktrittserklärung.
