---
name: kaufrecht-maengelhaftung-borghei
title: /vertragsrecht:kaufrecht-maengelhaftung
description: Prüfung kaufrechtlicher Mängelrechte – Sachmangel § 434 BGB (subjektive, objektive und Montageanforderungen), Rechtekatalog § 437 BGB, Nacherfüllung § 439 BGB einschließlich Aus- und Einbaukosten § 439 Abs. 3 BGB, Fristsetzung und Rücktritt § 323 BGB, Entbehrlichkeit § 440 BGB, Minderung § 441 BGB, Schadensersatz §§ 280, 281 BGB, Verjährung § 438 BGB und Beweislastumkehr § 477 BGB. Use when eine gelieferte Sache mangelhaft ist und geklärt werden soll, welches Mängelrecht in welcher Reihenfolge und bis wann geltend zu machen ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/vertragsrecht/skills/kaufrecht-maengelhaftung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: contracts
language: de
---

# /vertragsrecht:kaufrecht-maengelhaftung

## Zweck

Kaufrechtliche Mängelfälle scheitern in der Praxis selten am Mangel, sondern am **Verfahren**: keine oder zu unbestimmte Nacherfüllungsaufforderung, fehlende Fristsetzung vor dem Rücktritt, versäumte Rüge nach § 377 HGB, abgelaufene Verjährung nach § 438 BGB. Dieser Skill arbeitet den Rechtekatalog des [§ 437 BGB](https://www.gesetze-im-internet.de/bgb/__437.html) in der zwingenden Reihenfolge ab und liefert die Formulierungshilfen für Nacherfüllungsverlangen, Fristsetzung und Rücktrittserklärung.

## Eingaben

- Kaufgegenstand, Kaufpreis, Lieferdatum (Ablieferung — maßgeblich für § 438 Abs. 2 BGB)
- Parteirollen: B2C (Verbrauchsgüterkauf §§ 474 ff. BGB), B2B (beiderseitiges Handelsgeschäft → § 377 HGB), C2C
- Mangelbeschreibung, Zeitpunkt des Auftretens, Zeitpunkt der Entdeckung
- Vertragliche Beschaffenheitsvereinbarung, Prospekt-/Werbeangaben, Garantie (§ 443 BGB)
- Bereits erfolgte Erklärungen (Rüge, Nacherfüllungsverlangen, Fristsetzung — jeweils Datum und Zugang)
- Neu- oder Gebrauchtware; Einbau der Sache in eine andere Sache erfolgt?

## Sub-Agent-Architektur

1. **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) liefert Statute mit URL, Kommentarstellen (Grüneberg, MüKoBGB, BeckOK) und — nur soweit sicher belegbar — BGH-Rechtsprechung mit Verifikationsmarker.
2. **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) prüft in der Reihenfolge Mangel → Rechtekatalog → Nacherfüllung → Fristsetzung → Sekundärrechte → Verjährung und entwirft die Erklärungen.
3. **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft Fristen (§ 438 BGB, § 377 HGB), Zugangsnachweis, Bestimmtheit der Fristsetzung und Quellenmarker.

## Ablauf

### 1. Sachmangel ([§ 434 BGB](https://www.gesetze-im-internet.de/bgb/__434.html))

Seit dem 01.01.2022 gilt ein **kumulativer** Mangelbegriff: Die Sache ist nur frei von Sachmängeln, wenn sie den **subjektiven**, den **objektiven** und den **Montageanforderungen** entspricht.

- **Subjektive Anforderungen** (§ 434 Abs. 2 BGB): vereinbarte Beschaffenheit, vertraglich vorausgesetzte Verwendung, vereinbartes Zubehör und Anleitungen.
- **Objektive Anforderungen** (§ 434 Abs. 3 BGB): Eignung für die gewöhnliche Verwendung, übliche Beschaffenheit einschließlich Menge, Qualität, Haltbarkeit und Sicherheit, sowie Beschaffenheit, die der Käufer nach den öffentlichen Äußerungen des Verkäufers oder Herstellers erwarten kann.
- **Montageanforderungen** (§ 434 Abs. 4 BGB): unsachgemäße Montage durch den Verkäufer oder fehlerhafte Montageanleitung („IKEA-Klausel").
- **Negative Beschaffenheitsvereinbarung im B2C:** Eine Abweichung von den objektiven Anforderungen wirkt beim Verbrauchsgüterkauf nur, wenn der Verbraucher vor Vertragsschluss eigens davon in Kenntnis gesetzt wurde **und** die Abweichung ausdrücklich und gesondert vereinbart ist ([§ 476 Abs. 1 S. 2 BGB](https://www.gesetze-im-internet.de/bgb/__476.html)). Ein pauschales „gekauft wie gesehen" genügt nicht.

Abzugrenzen: **Rechtsmangel** ([§ 435 BGB](https://www.gesetze-im-internet.de/bgb/__435.html)); **Kenntnis des Käufers** schließt Rechte grundsätzlich aus ([§ 442 BGB](https://www.gesetze-im-internet.de/bgb/__442.html)).

### 2. Rügeobliegenheit im Handelskauf ([§ 377 HGB](https://www.gesetze-im-internet.de/hgb/__377.html))

Nur im **beiderseitigen Handelsgeschäft**: Der Käufer muss die Ware unverzüglich nach Ablieferung untersuchen und einen erkennbaren Mangel unverzüglich rügen; sonst gilt die Ware als genehmigt. Versteckte Mängel sind unverzüglich nach Entdeckung zu rügen. **Prüfe diesen Punkt vor allem anderen** — eine versäumte Rüge beendet die Prüfung im B2B.

### 3. Rechtekatalog ([§ 437 BGB](https://www.gesetze-im-internet.de/bgb/__437.html))

| Nr. | Recht | Norm | Voraussetzung |
|---|---|---|---|
| 1 | Nacherfüllung | § 439 BGB | Mangel bei Gefahrübergang |
| 2 | Rücktritt | §§ 440, 323, 326 Abs. 5 BGB | Fristsetzung fruchtlos oder entbehrlich |
| 2 | Minderung | § 441 BGB | wie Rücktritt, aber auch bei unerheblichem Mangel |
| 3 | Schadensersatz | §§ 280, 281, 283, 311a BGB | zusätzlich Vertretenmüssen § 276 BGB |
| 3 | Aufwendungsersatz | § 284 BGB | statt Schadensersatz statt der Leistung |

**Vorrang der Nacherfüllung:** Rücktritt, Minderung und Schadensersatz statt der Leistung setzen grundsätzlich eine erfolglose Fristsetzung zur Nacherfüllung voraus.

### 4. Nacherfüllung ([§ 439 BGB](https://www.gesetze-im-internet.de/bgb/__439.html))

- **Wahlrecht des Käufers** zwischen Nachbesserung und Nachlieferung (§ 439 Abs. 1 BGB). Der Verkäufer kann die gewählte Art nur bei **Unverhältnismäßigkeit** verweigern (§ 439 Abs. 4 BGB).
- **Kostentragung** (§ 439 Abs. 2 BGB): Der Verkäufer trägt Transport-, Wege-, Arbeits- und Materialkosten.
- **Aus- und Einbaukosten** ([§ 439 Abs. 3 BGB](https://www.gesetze-im-internet.de/bgb/__439.html)): Hat der Käufer die mangelhafte Sache gemäß ihrer Art und ihrem Verwendungszweck in eine andere Sache eingebaut oder an eine andere Sache angebracht, ist der Verkäufer verpflichtet, dem Käufer die **erforderlichen Aufwendungen für das Entfernen der mangelhaften und den Einbau oder das Anbringen der nachgebesserten oder gelieferten mangelfreien Sache** zu ersetzen. Der Anspruch ist **verschuldensunabhängig** und gilt auch im B2B — für den Werkunternehmer, der mangelhaftes Material verbaut hat, ist das der zentrale Regressanker.
- **Rückgewähr der mangelhaften Sache** § 439 Abs. 5 BGB; **kein Nutzungsersatz** beim Verbrauchsgüterkauf (§ 475 Abs. 3 S. 1 BGB).

**Formulierungshilfe Nacherfüllungsverlangen:**

> „Die am [Datum] gelieferte Sache [Bezeichnung] weist folgenden Mangel auf: [konkrete Beschreibung des Symptoms, nicht der Ursache]. Ich fordere Sie hiermit gemäß § 439 Abs. 1 BGB zur Nacherfüllung durch **Nachlieferung einer mangelfreien Sache** auf und setze Ihnen hierfür eine Frist bis zum **[konkretes Kalenderdatum]**. Nach fruchtlosem Ablauf dieser Frist werde ich vom Vertrag zurücktreten und Schadensersatz geltend machen."

Der Käufer muss nur das **Mangelsymptom** bezeichnen, nicht die Ursache. Die Frist muss ein konkretes Datum nennen; „umgehend" genügt nicht sicher.

### 5. Fristsetzung und Rücktritt ([§ 323 BGB](https://www.gesetze-im-internet.de/bgb/__323.html), [§ 440 BGB](https://www.gesetze-im-internet.de/bgb/__440.html))

**Entbehrlichkeit der Fristsetzung:**

- § 323 Abs. 2 Nr. 1 BGB: ernsthafte und endgültige Leistungsverweigerung
- § 323 Abs. 2 Nr. 3 BGB: besondere Umstände, die den sofortigen Rücktritt rechtfertigen (Interessenabwägung)
- § 440 S. 1 BGB: Verkäufer verweigert **beide** Arten der Nacherfüllung nach § 439 Abs. 4 BGB, die dem Käufer zustehende Nacherfüllung ist **fehlgeschlagen** oder ihm **unzumutbar**
- § 440 S. 2 BGB: Eine Nachbesserung gilt nach dem **erfolglosen zweiten Versuch** als fehlgeschlagen, wenn sich nicht aus der Art der Sache oder des Mangels etwas anderes ergibt
- § 326 Abs. 5 BGB: Nacherfüllung ist unmöglich (§ 275 BGB) — Rücktritt ohne Fristsetzung

**Ausschluss:** Rücktritt ist bei **unerheblicher** Pflichtverletzung ausgeschlossen (§ 323 Abs. 5 S. 2 BGB); die Minderung bleibt gleichwohl möglich (§ 441 Abs. 1 S. 2 BGB).

**Formulierungshilfe Rücktrittserklärung:** „Die mit Schreiben vom [Datum] gesetzte Frist zur Nacherfüllung ist am [Datum] fruchtlos abgelaufen. Ich erkläre hiermit gemäß §§ 437 Nr. 2, 440, 323 BGB den **Rücktritt** vom Kaufvertrag vom [Datum]. Ich fordere Sie auf, den Kaufpreis in Höhe von [Betrag] EUR bis zum [Datum] zu erstatten; die Sache halte ich Zug um Zug zur Abholung bereit." Der Rücktritt ist **empfangsbedürftig** (§ 349 BGB), **bedingungsfeindlich** und **nicht widerrufbar** — Zugang beweissicher gestalten.

### 6. Minderung ([§ 441 BGB](https://www.gesetze-im-internet.de/bgb/__441.html))

Gestaltungserklärung gegenüber dem Verkäufer. Berechnung nach § 441 Abs. 3 BGB:

```
geminderter Preis = Kaufpreis × (Wert der Sache im mangelhaften Zustand
                                / Wert der Sache im mangelfreien Zustand)
```

Maßgeblich ist der Zeitpunkt des Vertragsschlusses; der Wert ist erforderlichenfalls **zu schätzen**. Anders als der Rücktritt ist die Minderung auch bei **unerheblichem** Mangel eröffnet.

### 7. Schadensersatz ([§§ 280, 281 BGB](https://www.gesetze-im-internet.de/bgb/__281.html))

- **Schadensersatz statt der Leistung** § 281 BGB: Fristsetzung erforderlich, zusätzlich Vertretenmüssen (§ 280 Abs. 1 S. 2 BGB — Vermutung zulasten des Verkäufers).
- **Mangelfolgeschaden** (§ 280 Abs. 1 BGB): Schäden an anderen Rechtsgütern des Käufers — **ohne** Fristsetzung ersatzfähig.
- **Verzögerungsschaden** § 280 Abs. 2 iVm § 286 BGB — siehe `/vertragsrecht:verzug-mahnung`.
- **Aufwendungsersatz** § 284 BGB alternativ zum Schadensersatz statt der Leistung (vergebliche Aufwendungen im Vertrauen auf den Erhalt der Leistung).

### 8. Beweislastumkehr beim Verbrauchsgüterkauf ([§ 477 BGB](https://www.gesetze-im-internet.de/bgb/__477.html))

Zeigt sich innerhalb **eines Jahres seit Gefahrübergang** ein von den Anforderungen des § 434 BGB abweichender Zustand, wird vermutet, dass die Sache bereits bei Gefahrübergang mangelhaft war. Die Frist wurde zum **01.01.2022 von sechs auf zwölf Monate** verlängert; bei lebenden Tieren beträgt sie 24 Monate (§ 477 Abs. 1 S. 2 BGB). Die Vermutung greift nicht, wenn sie mit der Art der Sache oder des Mangels unvereinbar ist. **Nach Ablauf der 12 Monate trägt der Käufer die volle Beweislast** für den Mangel bei Gefahrübergang.

### 9. Verjährung ([§ 438 BGB](https://www.gesetze-im-internet.de/bgb/__438.html))

| Fall | Frist | Beginn |
|---|---|---|
| Regelfall bewegliche Sache | 2 Jahre | Ablieferung (§ 438 Abs. 2 BGB) |
| Bauwerk / Baustoff, der für ein Bauwerk verwendet wurde und dessen Mangelhaftigkeit verursacht hat | 5 Jahre | Ablieferung |
| Dingliches Herausgaberecht eines Dritten (§ 438 Abs. 1 Nr. 1 BGB) | 30 Jahre | Ablieferung |
| Arglistiges Verschweigen (§ 438 Abs. 3 BGB) | Regelverjährung §§ 195, 199 BGB | Schluss des Kenntnisjahres |

**Gebrauchtwaren im B2C:** Verkürzung auf ein Jahr nur unter den engen Voraussetzungen des § 476 Abs. 2 BGB (ausdrückliche und gesondert vereinbarte Kenntnisgabe). Detailprüfung der Fristen: `/vertragsrecht:verjaehrung-pruefung`.

## Quellen

### Statute

- [§ 434 BGB](https://www.gesetze-im-internet.de/bgb/__434.html), [§ 435 BGB](https://www.gesetze-im-internet.de/bgb/__435.html), [§ 437 BGB](https://www.gesetze-im-internet.de/bgb/__437.html), [§ 438 BGB](https://www.gesetze-im-internet.de/bgb/__438.html), [§ 439 BGB](https://www.gesetze-im-internet.de/bgb/__439.html), [§ 440 BGB](https://www.gesetze-im-internet.de/bgb/__440.html), [§ 441 BGB](https://www.gesetze-im-internet.de/bgb/__441.html), [§ 442 BGB](https://www.gesetze-im-internet.de/bgb/__442.html), [§ 443 BGB](https://www.gesetze-im-internet.de/bgb/__443.html), [§ 444 BGB](https://www.gesetze-im-internet.de/bgb/__444.html)
- [§ 323 BGB](https://www.gesetze-im-internet.de/bgb/__323.html), [§ 280 BGB](https://www.gesetze-im-internet.de/bgb/__280.html), [§ 281 BGB](https://www.gesetze-im-internet.de/bgb/__281.html), [§ 346 BGB](https://www.gesetze-im-internet.de/bgb/__346.html)
- [§ 476 BGB](https://www.gesetze-im-internet.de/bgb/__476.html), [§ 477 BGB](https://www.gesetze-im-internet.de/bgb/__477.html) (Verbrauchsgüterkauf)
- [§ 377 HGB](https://www.gesetze-im-internet.de/hgb/__377.html) (Untersuchungs- und Rügeobliegenheit)
- Warenkauf-RL (EU) 2019/771 (Umsetzung zum 01.01.2022)

### Kommentare

- Grüneberg, BGB, 83. Aufl. 2024, §§ 434, 437, 439 Rn. 1 ff. `[unverifiziert – Auflagenstand prüfen]`
- Westermann, in: MüKoBGB, 9. Aufl. 2023, § 434 Rn. 1 ff., § 439 Rn. 1 ff.
- Faust, in: BeckOK BGB, § 437 Rn. 1 ff., § 477 Rn. 1 ff. (Stand prüfen)

### Rechtsprechung

- BGH, Urt. v. 21.12.2011 – VIII ZR 70/08 (Aus- und Einbaukosten, „Parkettstäbe II") `[unverifiziert – prüfen]`
- BGH, Urt. v. 26.10.2016 – VIII ZR 240/15 (Reichweite der Beweislastumkehr § 476 BGB a.F.) `[unverifiziert – prüfen]`

> Beide Zitate sind vor Verwendung in juris / Beck-Online zu prüfen. Die Aussagen dieses Skills tragen sich bereits aus dem Gesetzeswortlaut; die Entscheidungen sind Illustration, nicht Argumentationsgrundlage.

## Ausgabeformat

```
KAUFRECHTLICHE MÄNGELHAFTUNG — <Kaufgegenstand> — <Datum>

I.    Sachmangel (§ 434)              [✅ / 🟡 / ❌]
        subjektiv / objektiv / Montage: <…>
II.   Rügeobliegenheit (§ 377 HGB)    [N/A B2C / ✅ gewahrt / ❌ versäumt]
III.  Nacherfüllung (§ 439)           [verlangt am <Datum> / offen]
        Art: <Nachbesserung / Nachlieferung>
        Aus- und Einbaukosten § 439 III: [ja / nein — Betrag]
IV.   Fristsetzung                    [gesetzt bis <Datum> / entbehrlich § 323 II / § 440]
V.    Rücktritt (§§ 437 Nr. 2, 323)   [möglich / ausgeschlossen § 323 V 2 — Begründung]
VI.   Minderung (§ 441)               [Berechnung: <…> EUR]
VII.  Schadensersatz (§§ 280, 281)    [statt der Leistung / Mangelfolgeschaden]
VIII. Beweislastumkehr (§ 477)        [greift bis <Datum> / abgelaufen]
IX.   Verjährung (§ 438)              [Ende: <TT.MM.JJJJ>]

Empfohlene nächste Erklärung: <…> bis <Datum>
Gesamtbefund: [🟢 / 🟡 / 🔴]
Offene Tatsachen: <Liste>
```

## Risiken / typische Fehler

- **Rücktritt ohne Fristsetzung** erklärt, ohne dass ein Entbehrlichkeitstatbestand (§ 323 Abs. 2 BGB, § 440 BGB) trägt — der Rücktritt geht ins Leere und der Käufer bleibt zur Kaufpreiszahlung verpflichtet.
- **§ 377 HGB übersehen** — im beiderseitigen Handelsgeschäft führt die versäumte unverzügliche Rüge zur Genehmigungsfiktion und beendet sämtliche Mängelrechte.
- **Beweislastumkehr § 477 BGB überdehnt** — sie gilt nur beim Verbrauchsgüterkauf, nur 12 Monate ab Gefahrübergang und begründet keine Vermutung, dass überhaupt ein Mangel vorliegt.
- **Aus- und Einbaukosten § 439 Abs. 3 BGB vergessen** — der Anspruch ist verschuldensunabhängig; wer ihn nur über § 280 BGB prüft, verliert ihn bei fehlendem Vertretenmüssen.
- **Verjährung § 438 BGB mit der Regelverjährung verwechselt** — zwei Jahre ab Ablieferung, nicht ab Kenntnis; die Ultimo-Regel des § 199 BGB gilt hier gerade nicht.
- **Pauschaler Gewährleistungsausschluss** im B2C-Neuwarenkauf oder trotz Arglist (§ 444 BGB) verwendet — unwirksam, mit voller Haftung als Folge.
