---
name: anfechtung-willenserklaerung-borghei
title: /vertragsrecht:anfechtung-willenserklaerung
description: Prüfung und Erklärung der Anfechtung einer Willenserklärung – Inhalts- und Erklärungsirrtum sowie Eigenschaftsirrtum § 119 BGB, unrichtige Übermittlung § 120 BGB, arglistige Täuschung und widerrechtliche Drohung § 123 BGB, Anfechtungsfristen § 121 BGB (unverzüglich) und § 124 BGB (ein Jahr), Anfechtungserklärung § 143 BGB, Nichtigkeit ex tunc § 142 BGB und Vertrauensschadensersatz § 122 BGB. Use when eine Vertragspartei sich beim Vertragsschluss geirrt hat, getäuscht oder bedroht wurde und die Lösung vom Vertrag geprüft wird.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/vertragsrecht/skills/anfechtung-willenserklaerung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: contracts
language: de
---

# /vertragsrecht:anfechtung-willenserklaerung

## Zweck

Die Anfechtung ist der schnellste Weg aus einem Vertrag — und der am schnellsten verlorene: Beim Irrtum läuft die Frist **unverzüglich** ab Kenntnis. Dieser Skill ordnet den Sachverhalt dem richtigen Anfechtungsgrund zu, prüft die Frist **vor** allem anderen, entwirft die Anfechtungserklärung und beziffert die Gegenposition aus [§ 122 BGB](https://www.gesetze-im-internet.de/bgb/__122.html).

## Eingaben

- Angefochtene Willenserklärung: Inhalt, Datum, Empfänger, Form
- Fehlerbeschreibung: Was wollte der Erklärende, was hat er erklärt, worüber irrte er?
- Bei Täuschung: wer täuschte (Vertragspartner oder Dritter), worüber, wann entdeckt
- Bei Drohung: Drohungsinhalt, Drohender, Ende der Zwangslage
- **Zeitpunkt der Kenntnis vom Anfechtungsgrund** — der wichtigste Wert für die Fristprüfung
- Bereits erbrachte Leistungen; Vertrauensdispositionen der Gegenseite
- Alternativ verfügbare Rechtsbehelfe (Mängelrecht, c.i.c., Rücktritt) und deren Fristenstand

## Sub-Agent-Architektur

1. **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) liefert §§ 119–124, 142, 143 BGB mit URL, Kommentarstellen zum Eigenschaftsbegriff und zur Kausalität der Täuschung.
2. **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) prüft Anfechtungsgrund → Kausalität → Frist → Ausschluss → Rechtsfolge und entwirft die Anfechtungserklärung.
3. **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft insbesondere die Fristwahrung, den Zugangsnachweis und ob die Anfechtung gegenüber dem richtigen Anfechtungsgegner erklärt wurde.

## Ablauf

### 1. Fristprüfung zuerst ([§ 121 BGB](https://www.gesetze-im-internet.de/bgb/__121.html), [§ 124 BGB](https://www.gesetze-im-internet.de/bgb/__124.html))

| Anfechtungsgrund | Frist | Beginn | Höchstfrist |
|---|---|---|---|
| Irrtum §§ 119, 120 BGB | **unverzüglich** (ohne schuldhaftes Zögern) | Kenntnis des Anfechtungsgrundes | 10 Jahre ab Abgabe (§ 121 Abs. 2 BGB) |
| Arglistige Täuschung § 123 BGB | **1 Jahr** | Entdeckung der Täuschung | 10 Jahre ab Abgabe (§ 124 Abs. 3 BGB) |
| Widerrechtliche Drohung § 123 BGB | **1 Jahr** | Ende der Zwangslage | 10 Jahre ab Abgabe |

„Unverzüglich" ist **nicht sofort**, aber ohne schuldhaftes Zögern; eine Überlegungs- und Erkundigungsfrist von wenigen Tagen wird zugestanden, eine Frist von zwei Wochen ist regelmäßig zu lang `[unverifiziert – prüfen]`. Zur Fristwahrung genügt die **rechtzeitige Absendung** (§ 121 Abs. 1 S. 2 BGB), sofern die Erklärung dem Empfänger zugeht. **Ergibt die Fristprüfung, dass die Anfechtung ausgeschlossen ist, ist unmittelbar auf Mängelrecht, c.i.c. oder Rücktritt umzustellen.**

### 2. Erklärungs- und Inhaltsirrtum ([§ 119 Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__119.html))

Wer bei der Abgabe einer Willenserklärung über deren Inhalt im Irrtum war oder eine Erklärung dieses Inhalts überhaupt nicht abgeben wollte, kann die Erklärung anfechten, wenn anzunehmen ist, dass er sie bei Kenntnis der Sachlage und bei verständiger Würdigung des Falles **nicht abgegeben haben würde**.

- **Erklärungsirrtum:** Verschreiben, Vergreifen, Vertippen — der Erklärende wollte etwas anderes äußern (Tippfehler im Preis: 1.000 statt 10.000).
- **Inhaltsirrtum:** Der Erklärende wusste, was er äußert, irrte aber über die Bedeutung (*falsa demonstratio* ausgenommen — bei übereinstimmendem Verständnis gilt das Gewollte).
- **Nicht anfechtbar: der Motivirrtum.** Der Irrtum über den Beweggrund ist grundsätzlich unbeachtlich — Fehlkalkulationen des eigenen Preises („interner Kalkulationsirrtum") berechtigen nicht zur Anfechtung.

### 3. Eigenschaftsirrtum ([§ 119 Abs. 2 BGB](https://www.gesetze-im-internet.de/bgb/__119.html))

Als Irrtum über den Inhalt der Erklärung gilt auch der Irrtum über solche **Eigenschaften der Person oder der Sache**, die im Verkehr als wesentlich angesehen werden. Verkehrswesentlich sind alle wertbildenden Merkmale, die der Sache auf Dauer anhaften — **nicht** der Wert oder Preis selbst.

**🔴 Vorrang des Mängelrechts:** Nach Gefahrübergang verdrängen die §§ 434 ff. bzw. 633 ff. BGB die Anfechtung wegen eines Eigenschaftsirrtums, soweit sich der Irrtum auf eine mangelbegründende Eigenschaft bezieht — andernfalls würden Fristen und Nacherfüllungsvorrang des Mängelrechts unterlaufen. Die Anfechtung wegen **arglistiger Täuschung** nach § 123 BGB bleibt daneben stets möglich.

### 4. Unrichtige Übermittlung ([§ 120 BGB](https://www.gesetze-im-internet.de/bgb/__120.html))

Eine Willenserklärung, die durch die zur Übermittlung verwendete **Person oder Anstalt unrichtig übermittelt** worden ist, kann unter denselben Voraussetzungen angefochten werden wie eine irrtümlich abgegebene Erklärung. Erfasst ist der Erklärungsboten- und Übermittlungsfehler; **nicht** erfasst ist die eigenmächtige Abweichung eines Stellvertreters (dort §§ 164 ff., 166 BGB) und nicht der Übermittlungsfehler in der Sphäre des Empfängers.

### 5. Arglistige Täuschung ([§ 123 Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__123.html))

Wer zur Abgabe einer Willenserklärung durch **arglistige Täuschung** bestimmt worden ist, kann die Erklärung anfechten. Voraussetzungen:

1. **Täuschung** durch aktives Vorspiegeln, Entstellen oder **Verschweigen** offenbarungspflichtiger Tatsachen. Eine **Aufklärungspflicht** besteht bei Umständen, die für die Entschließung der anderen Seite erkennbar von wesentlicher Bedeutung sind und über die nach Treu und Glauben Aufklärung erwartet werden darf — bei einem Unfallwagen, einem Wasserschaden, einer verschwiegenen Vorbelastung des Grundstücks.
2. **Arglist:** Vorsatz genügt; bedingter Vorsatz reicht, insbesondere **Angaben ins Blaue hinein** ohne jede Tatsachengrundlage.
3. **Kausalität** für die Willenserklärung.
4. **Widerrechtlichkeit** — bei der Täuschung indiziert.

**Täuschung durch Dritte** (§ 123 Abs. 2 BGB): Hat ein **Dritter** die Täuschung verübt, ist die Anfechtung gegenüber dem Erklärungsempfänger nur zulässig, wenn dieser die Täuschung **kannte oder kennen musste**. Nicht „Dritter" ist, wer im Lager des Erklärungsempfängers steht (Verhandlungsgehilfe, Vertreter, eingeschalteter Makler).

**Kein Vorrang des Mängelrechts** und kein Ausschluss durch einen vereinbarten Gewährleistungsausschluss: Bei Arglist greift zudem [§ 444 BGB](https://www.gesetze-im-internet.de/bgb/__444.html).

### 6. Widerrechtliche Drohung ([§ 123 Abs. 1 Alt. 2 BGB](https://www.gesetze-im-internet.de/bgb/__123.html))

Drohung ist das Inaussichtstellen eines künftigen Übels, auf dessen Eintritt der Drohende Einfluss zu haben vorgibt. **Widerrechtlich** kann die Drohung sein wegen des Mittels, des Zwecks oder der **Zweck-Mittel-Relation** — letzteres ist der Regelfall: Die Drohung mit einer an sich zulässigen Strafanzeige ist widerrechtlich, wenn sie zur Durchsetzung eines damit in keinem inneren Zusammenhang stehenden Vertragsschlusses eingesetzt wird. Anders als bei der Täuschung kommt es **nicht** darauf an, ob ein Dritter gedroht hat.

### 7. Anfechtungserklärung ([§ 143 BGB](https://www.gesetze-im-internet.de/bgb/__143.html))

Die Anfechtung erfolgt durch **Erklärung gegenüber dem Anfechtungsgegner** — bei einem Vertrag ist das der **andere Teil** (§ 143 Abs. 2 BGB); bei einseitigen empfangsbedürftigen Erklärungen derjenige, gegenüber dem sie vorzunehmen war (§ 143 Abs. 3 BGB). Die Erklärung ist **formfrei**, empfangsbedürftig, **bedingungsfeindlich** und unwiderruflich. Das Wort „Anfechtung" muss nicht fallen, der Anfechtungswille muss aber eindeutig sein; der **Anfechtungsgrund** sollte angegeben werden, um die Fristwahrung dokumentieren zu können.

**Formulierungshilfe Anfechtungserklärung:**

> „In dem Vertrag vom [Datum] über [Gegenstand] fechte ich meine auf den Abschluss gerichtete Willenserklärung hiermit an. Ich stütze die Anfechtung auf **§ 123 Abs. 1 BGB (arglistige Täuschung)**: Sie haben mir gegenüber am [Datum] erklärt, [Angabe]. Diese Angabe war unzutreffend, wie ich am **[Datum]** erfahren habe. Bei Kenntnis des wahren Sachverhalts hätte ich den Vertrag nicht geschlossen. Die Anfechtung erfolgt innerhalb der Jahresfrist des § 124 Abs. 1 BGB. Der Vertrag ist damit nach § 142 Abs. 1 BGB **von Anfang an nichtig**. Ich fordere Sie auf, den gezahlten Betrag von [Betrag] EUR bis zum [Datum] zurückzuzahlen; die Sache halte ich Zug um Zug zur Abholung bereit."

Zusatz bei Irrtumsanfechtung: „Die Anfechtung erfolgt unverzüglich im Sinne des § 121 Abs. 1 BGB; ich habe von dem Irrtum erst am [Datum] Kenntnis erlangt."

### 8. Rechtsfolgen ([§ 142 BGB](https://www.gesetze-im-internet.de/bgb/__142.html), [§ 122 BGB](https://www.gesetze-im-internet.de/bgb/__122.html))

- **Nichtigkeit ex tunc** (§ 142 Abs. 1 BGB): Das angefochtene Rechtsgeschäft ist **als von Anfang an nichtig** anzusehen. Wer die Anfechtbarkeit kannte oder kennen musste, wird behandelt, als hätte er die Nichtigkeit gekannt (§ 142 Abs. 2 BGB).
- **Rückabwicklung** erfolgt nicht nach §§ 346 ff. BGB, sondern nach **Bereicherungsrecht** (§ 812 Abs. 1 S. 1 Alt. 1 BGB) — mit den Besonderheiten des Wertersatzes (§ 818 Abs. 2 BGB) und der **Entreicherung** (§ 818 Abs. 3 BGB), die dem Getäuschten zugutekommen kann, dem verschärft haftenden Täuschenden aber nicht (§§ 818 Abs. 4, 819 BGB).
- **Vertrauensschadensersatz** ([§ 122 BGB](https://www.gesetze-im-internet.de/bgb/__122.html)): Bei einer Anfechtung nach **§§ 119, 120 BGB** hat der Anfechtende dem Empfänger den Schaden zu ersetzen, den dieser dadurch erleidet, dass er auf die Gültigkeit der Erklärung vertraut hat — **begrenzt auf das Erfüllungsinteresse**. Der Anspruch entfällt, wenn der Geschädigte den Anfechtungsgrund kannte oder kennen musste (§ 122 Abs. 2 BGB). **Bei einer Anfechtung nach § 123 BGB besteht kein Anspruch aus § 122 BGB** — der Täuschende ist nicht schutzwürdig.
- **Bei Dauerschuldverhältnissen** (Gesellschafts- und Arbeitsverhältnisse) wird die Rückwirkung nach den Grundsätzen der fehlerhaften Gesellschaft bzw. des fehlerhaften Arbeitsverhältnisses eingeschränkt: Die Anfechtung wirkt dann nur **ex nunc** `[unverifiziert – prüfen]`.

### 9. Konkurrenzen

| Rechtsbehelf | Verhältnis zur Anfechtung |
|---|---|
| Mängelrecht §§ 437, 634 BGB | Verdrängt § 119 Abs. 2 BGB nach Gefahrübergang; § 123 BGB bleibt daneben bestehen |
| c.i.c. §§ 311 Abs. 2, 241 Abs. 2, 280 BGB | Neben § 123 BGB anwendbar; ermöglicht **Vertragsaufhebung als Schadensersatz** ohne Bindung an die Jahresfrist — siehe `/vertragsrecht:vorvertragliche-phase` |
| Rücktritt §§ 323, 326 BGB | Setzt einen wirksamen Vertrag voraus; wechselseitig ausschließend zur wirksamen Anfechtung |
| Widerruf §§ 355 ff. BGB | Selbständig, unabhängig von einem Irrtum — siehe `/vertragsrecht:verbraucherwiderruf` |
| § 138 BGB, § 134 BGB | Nichtigkeit von Anfang an ohne Erklärung — vorrangig zu prüfen |

## Quellen

### Statute

- [§ 119 BGB](https://www.gesetze-im-internet.de/bgb/__119.html), [§ 120 BGB](https://www.gesetze-im-internet.de/bgb/__120.html), [§ 121 BGB](https://www.gesetze-im-internet.de/bgb/__121.html), [§ 122 BGB](https://www.gesetze-im-internet.de/bgb/__122.html), [§ 123 BGB](https://www.gesetze-im-internet.de/bgb/__123.html), [§ 124 BGB](https://www.gesetze-im-internet.de/bgb/__124.html)
- [§ 142 BGB](https://www.gesetze-im-internet.de/bgb/__142.html), [§ 143 BGB](https://www.gesetze-im-internet.de/bgb/__143.html)
- [§ 812 BGB](https://www.gesetze-im-internet.de/bgb/__812.html), [§ 818 BGB](https://www.gesetze-im-internet.de/bgb/__818.html) (Rückabwicklung), [§ 444 BGB](https://www.gesetze-im-internet.de/bgb/__444.html)

### Kommentare

- Grüneberg, BGB, 83. Aufl. 2024, §§ 119, 123, 142 Rn. 1 ff. `[unverifiziert – Auflagenstand prüfen]`
- Armbrüster, in: MüKoBGB, 9. Aufl. 2021, § 119 Rn. 1 ff., § 123 Rn. 1 ff.
- Singer, in: Staudinger, BGB, Neubearb. 2021, § 119 Rn. 1 ff.

### Rechtsprechung

- BGH, Urt. v. 11.11.2011 – V ZR 245/10 (Offenbarungspflicht und Angaben ins Blaue hinein) `[unverifiziert – prüfen]`
- BGH, Urt. v. 07.06.1984 – IX ZR 66/83 (Unverzüglichkeit im Sinne des § 121 BGB) `[unverifiziert – prüfen]`

> Beide Aktenzeichen vor Verwendung in juris / Beck-Online prüfen. Die tragenden Aussagen folgen aus dem Gesetzeswortlaut.

## Ausgabeformat

```
ANFECHTUNG — <Vertrag / Erklärung> — <Datum>

I.    Angefochtene Erklärung          <Inhalt, Datum, Empfänger>
II.   Anfechtungsgrund                [§ 119 I Erklärung/Inhalt / § 119 II Eigenschaft
                                       / § 120 Übermittlung / § 123 Täuschung / § 123 Drohung]
III.  Kenntnis vom Grund              <TT.MM.JJJJ> — Beleg: <…>
IV.   Frist                           [§ 121 unverzüglich — Ablauf ca. <Datum>
                                       / § 124 ein Jahr — Ablauf <Datum>]
        Höchstfrist 10 Jahre:         <Datum>
        Status:                       [✅ gewahrt / 🔴 versäumt — Alternative: <…>]
V.    Kausalität                      [✅ / ❌ — Begründung]
VI.   Vorrang Mängelrecht (§ 119 II)  [🔴 gesperrt / N/A bei § 123]
VII.  Anfechtungsgegner (§ 143)       <Person> — Erklärung am <Datum>, Zugangsnachweis <…>
VIII. Rechtsfolge (§ 142)             [Nichtigkeit ex tunc / ex nunc bei Dauerschuldverhältnis]
        Rückabwicklung:               §§ 812, 818 BGB — <Beträge>
IX.   Schadensersatz (§ 122)          [<Betrag> EUR / entfällt bei § 123 / § 122 II]
X.    Konkurrierende Rechtsbehelfe    [c.i.c. / Mängelrecht / Rücktritt / Widerruf]

Gesamtbefund: [🟢 / 🟡 / 🔴]
Offene Tatsachen: <Liste — insbesondere Kenntniszeitpunkt>
```

## Risiken / typische Fehler

- **Unverzüglichkeit versäumt** — bei der Irrtumsanfechtung nach § 121 BGB entscheiden Tage; wer erst nach Rücksprache mit mehreren Beratern reagiert, ist regelmäßig zu spät.
- **Motivirrtum als Anfechtungsgrund behandelt** — der Irrtum über den Beweggrund, insbesondere der interne Kalkulationsirrtum, berechtigt nicht zur Anfechtung nach § 119 BGB.
- **Vorrang des Mängelrechts übersehen** — nach Gefahrübergang ist § 119 Abs. 2 BGB durch §§ 434 ff., 633 ff. BGB gesperrt; nur § 123 BGB bleibt.
- **Täuschung durch Dritte ohne § 123 Abs. 2 BGB geprüft** — gegenüber dem gutgläubigen Erklärungsempfänger ist die Anfechtung dann ausgeschlossen.
- **§ 122 BGB nicht bedacht** — wer wegen Irrtums anficht, schuldet dem Vertrauenden den Vertrauensschaden; die Anfechtung kann teurer sein als die Erfüllung.
- **Anfechtung gegenüber dem Falschen erklärt** — Anfechtungsgegner ist bei Verträgen der andere Teil (§ 143 Abs. 2 BGB), nicht ein Vertreter oder Makler ohne Empfangsvollmacht.
