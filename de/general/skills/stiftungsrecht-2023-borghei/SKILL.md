---
name: stiftungsrecht-2023-borghei
title: /vereins-stiftungs-gemeinnuetzigkeitsrecht:stiftungsrecht-2023
description: Errichtung, Verwaltung und Umstrukturierung der rechtsfähigen Stiftung nach dem seit 01.01.2023 bundeseinheitlichen Stiftungsrecht der §§ 80–88 BGB – Stiftungsgeschäft § 81 BGB, Anerkennung § 82 BGB, Verbrauchsstiftung, Grundstockvermögen § 83b BGB und Vermögenserhaltungsgrundsatz mit Umschichtungsgewinnen § 83c BGB, Sorgfaltsmaßstab und kodifizierte Business Judgment Rule § 84a Abs. 2 BGB, Satzungsänderung nach der Dreiteilung des § 85 BGB, Zulegung und Zusammenlegung §§ 86–86b BGB, Auflösung und Aufhebung §§ 87–87c BGB sowie das Stiftungsregister nach dem StiftRG. Use when eine Stiftung errichtet, eine Stiftungssatzung geändert, eine Zulegung oder Zusammenlegung geprüft oder die Haftung eines Stiftungsvorstands bewertet werden soll.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/vereins-stiftungs-gemeinnuetzigkeitsrecht/skills/stiftungsrecht-2023
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: general
language: de
---

# /vereins-stiftungs-gemeinnuetzigkeitsrecht:stiftungsrecht-2023

## Zweck

Zum **01.01.2023** ist das Stiftungsrecht bundeseinheitlich in den §§ 80–88 BGB geregelt worden; die zuvor maßgeblichen sechzehn Landesstiftungsgesetze gelten nur noch in Restbereichen (Aufsicht, Verfahren, kirchliche Stiftungen). Dieser Skill arbeitet mit der neuen Systematik: Errichtung, Vermögensverwaltung, Organhaftung, Satzungsänderung und Umstrukturierung.

## Eingaben

- Vorhaben: Neuerrichtung, Satzungsänderung, Zulegung/Zusammenlegung, Auflösung, Haftungsfrage
- Stiftungstyp: auf unbestimmte Zeit oder **Verbrauchsstiftung**; Errichtung unter Lebenden oder von Todes wegen
- Gewidmetes Vermögen: Höhe, Zusammensetzung, Ertragserwartung, geplante Zustiftungen
- Zweck in eigenen Worten; soll Gemeinnützigkeit angestrebt werden?
- Sitzland (maßgeblich für die zuständige Anerkennungs- und Aufsichtsbehörde und das Restlandesrecht)
- Bei Änderung: geltende Satzung, Stiftungsgeschäft im Wortlaut, dokumentierter Stifterwille, veränderte Verhältnisse
- Bei Haftungsfrage: Beschlusslage, Informationsgrundlage, Satzungsregelung zur Haftungsbeschränkung

## Sub-Agent-Architektur

1. **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) liefert §§ 80–88 BGB, das StiftRG, das einschlägige Restlandesrecht und Kommentarstellen zur Reform.
2. **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) entwirft Stiftungsgeschäft, Satzung, Anerkennungsantrag und Änderungsbeschlüsse.
3. **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft Mindestinhalt, Tragfähigkeit der Ertragsprognose, Zuordnung der Satzungsänderung zur richtigen Stufe des § 85 BGB und die Dokumentation der Business Judgment Rule.

## Ablauf

### 1. Errichtung und Stiftungsbegriff ([§ 80 BGB](https://www.gesetze-im-internet.de/bgb/__80.html))

Die Stiftung ist eine **mit einem Vermögen zur dauernden und nachhaltigen Erfüllung eines vom Stifter vorgegebenen Zwecks ausgestattete, mitgliederlose juristische Person** (§ 80 Abs. 1 S. 1 BGB). Sie wird in der Regel auf unbestimmte Zeit errichtet, kann aber als **Verbrauchsstiftung** auf bestimmte Zeit errichtet werden, innerhalb derer ihr gesamtes Vermögen zur Zweckerfüllung zu verbrauchen ist (§ 80 Abs. 1 S. 2 BGB).

Zur Entstehung sind nach § 80 Abs. 2 BGB **zwei** Akte erforderlich: das **Stiftungsgeschäft** und die **Anerkennung** durch die zuständige Behörde des Sitzlandes. Wird die Stiftung erst nach dem Tod des Stifters anerkannt, gilt sie für dessen Zuwendungen als schon vor dem Tod entstanden.

### 2. Stiftungsgeschäft ([§ 81 BGB](https://www.gesetze-im-internet.de/bgb/__81.html))

Im Stiftungsgeschäft muss der Stifter

1. der Stiftung eine **Satzung** geben, die mindestens Bestimmungen enthält über
   a) den **Zweck**, b) den **Namen**, c) den **Sitz** und d) die **Bildung des Vorstands**, und
2. ein **Vermögen widmen**, das der Stiftung zu deren eigener Verfügung zu überlassen ist.

Bei der **Verbrauchsstiftung** treten nach § 81 Abs. 2 BGB hinzu: die Festlegung der Zeit, für die die Stiftung errichtet wird, und Bestimmungen zur Vermögensverwendung, die die nachhaltige Zweckerfüllung **und** den vollständigen Verbrauch innerhalb dieser Zeit gesichert erscheinen lassen.

**Form (§ 81 Abs. 3 BGB): Schriftform**, soweit nicht andere Vorschriften strenger sind, oder Enthaltensein in einer Verfügung von Todes wegen. Enthält die Widmung ein Grundstück, greift zusätzlich § 311b BGB. Nach § 82a BGB ist der Stifter nach der Anerkennung zur Übertragung des gewidmeten Vermögens verpflichtet; Rechte, für deren Übertragung eine Abtretung genügt, gehen mit der Anerkennung **automatisch** über, sofern das Stiftungsgeschäft nichts anderes bestimmt. § 81 Abs. 4 BGB erlaubt der Behörde die Ergänzung eines lückenhaften Stiftungsgeschäfts nach dem Tod des Stifters.

### 3. Anerkennung ([§ 82 BGB](https://www.gesetze-im-internet.de/bgb/__82.html))

Die Stiftung **ist anzuerkennen** — es besteht ein gebundener Anspruch, kein Ermessen —, wenn

1. das Stiftungsgeschäft den Anforderungen des § 81 Abs. 1 bis 3 BGB genügt **und**
2. die **dauernde und nachhaltige Erfüllung des Stiftungszwecks gesichert erscheint**,

es sei denn, die Stiftung würde das **Gemeinwohl gefährden**. Bei der Verbrauchsstiftung erscheint die dauernde Erfüllung gesichert, wenn die in der Satzung bestimmte Zeit **mindestens zehn Jahre** umfasst.

Praktisch entscheidet Nummer 2: Dem Antrag ist eine **Ertragsprognose** beizufügen, die zeigt, dass die Erträge des gewidmeten Vermögens Zweckverwirklichung und Verwaltungskosten dauerhaft tragen. Ein gesetzliches Mindestkapital gibt es nicht; die Anerkennungsbehörden orientieren sich an internen Richtwerten, die je Land abweichen `[unverifiziert - beim Sitzland prüfen]`.

Die Fristen des Anerkennungs- und Registerverfahrens rechnet der deterministische Rechner:

```bash
python -m scripts.legal_calc.cli frist --ereignis 15.01.2026 --menge 1 --einheit monate --land BY
```

Er leistet **ausschließlich** die Arithmetik der §§ 187–193 BGB. **Fristbeginn und Zugang bleiben rechtliche Eingaben** — wann ein Bescheid zugegangen und welches Ereignis fristauslösend ist, bewertet der Bearbeiter.

### 4. Stiftungsvermögen und Vermögenserhaltung ([§ 83b BGB](https://www.gesetze-im-internet.de/bgb/__83b.html), [§ 83c BGB](https://www.gesetze-im-internet.de/bgb/__83c.html))

**§ 83b BGB — Zweiteilung des Vermögens.** Bei einer auf unbestimmte Zeit errichteten Stiftung besteht das Stiftungsvermögen aus **Grundstockvermögen** und **sonstigem Vermögen**; die Verbrauchsstiftung hat aufgrund ihrer Satzung nur sonstiges Vermögen. Zum Grundstockvermögen gehören das gewidmete Vermögen, **Zustiftungen** und Vermögen, das die Stiftung selbst dazu bestimmt hat. Nach § 83b Abs. 3 BGB kann der Stifter einen Teil des gewidmeten Vermögens abweichend zu sonstigem Vermögen bestimmen. § 83b Abs. 4 BGB verlangt die **getrennte Verwaltung** von fremdem Vermögen und die ausschließliche Verwendung für den Stiftungszweck.

**§ 83c BGB — Vermögenserhaltungsgrundsatz.** Das Grundstockvermögen ist **ungeschmälert zu erhalten**; der Zweck ist mit seinen **Nutzungen** zu erfüllen.

- **Umschichtungsgewinne** (§ 83c Abs. 1 S. 3 BGB): Zuwächse aus der Umschichtung des Grundstockvermögens **können** für die Zweckerfüllung verwendet werden, soweit die Satzung dies nicht ausschließt **und** die Erhaltung des Grundstockvermögens gewährleistet ist. Das ist die zentrale praktische Neuerung — sie erlaubt es, realisierte Kursgewinne auszuschütten, statt sie thesaurieren zu müssen. Die Satzung sollte dazu ausdrücklich Stellung nehmen; Schweigen führt zur Anwendung der gesetzlichen Regel, eine Umschichtungsrücklage schafft Klarheit.
- **Teilverbrauch** (§ 83c Abs. 2 BGB): Die Satzung kann den Verbrauch eines Teils des Grundstockvermögens erlauben — dann muss sie die Stiftung zugleich verpflichten, das Grundstockvermögen **in absehbarer Zeit wieder aufzustocken**.
- **§ 83c Abs. 3 BGB:** Landesrecht kann behördliche Ausnahmen auf Antrag für einen bestimmten Teil des Grundstockvermögens vorsehen.

Ob Vermögenserhaltung **nominal** oder **real** (inflationsbereinigt) geschuldet ist, sagt das Gesetz nicht ausdrücklich; die Frage ist in der Satzung zu entscheiden `[unverifiziert - prüfen]`.

### 5. Organe, Sorgfalt und Business Judgment Rule ([§ 84 BGB](https://www.gesetze-im-internet.de/bgb/__84.html), [§ 84a BGB](https://www.gesetze-im-internet.de/bgb/__84a.html))

Die Stiftung **muss einen Vorstand haben**; er führt die Geschäfte und vertritt die Stiftung als **gesetzlicher Vertreter** (§ 84 Abs. 1, 2 BGB). Bei Mehrpersonenvorstand vertritt die **Mehrheit** der Mitglieder — abweichende Regelung und Beschränkung der Vertretungsmacht mit Wirkung gegen Dritte sind nach § 84 Abs. 3 BGB in der Satzung möglich. Weitere Organe können nach § 84 Abs. 4 BGB vorgesehen werden; § 84 Abs. 5 BGB verweist auf §§ 30, 31, 42 Abs. 2 BGB.

**§ 84a BGB — Rechte und Pflichten der Organmitglieder:**

- **Abs. 1:** Es gelten die §§ 664 bis 670 BGB entsprechend; Organmitglieder sind **grundsätzlich unentgeltlich** tätig. Die Satzung kann abweichen und **auch die Haftung für Pflichtverletzungen beschränken**.
- **Abs. 2 — Sorgfalt und Business Judgment Rule:** Das Organmitglied hat die **Sorgfalt eines ordentlichen Geschäftsführers** anzuwenden. Eine Pflichtverletzung liegt **nicht** vor, wenn das Mitglied bei der Geschäftsführung unter Beachtung der gesetzlichen und satzungsgemäßen Vorgaben **vernünftigerweise annehmen durfte, auf der Grundlage angemessener Informationen zum Wohle der Stiftung zu handeln**. Damit ist die Business Judgment Rule für die Stiftung **kodifiziert** — sie ist nicht mehr nur analog aus § 93 Abs. 1 S. 2 AktG herzuleiten.
- **Abs. 3:** § 31a BGB gilt entsprechend (Haftungsprivileg bei Unentgeltlichkeit oder Vergütung bis 3.300 Euro jährlich); die Satzung kann das beschränken oder ausschließen.

**Praktische Folge:** Die Enthaftung setzt **Dokumentation** voraus. Zu jeder wesentlichen Entscheidung — insbesondere Anlageentscheidungen — gehören eine schriftlich festgehaltene Informationsgrundlage, die Abwesenheit von Sonderinteressen, ein Bezug zum Stiftungszweck und ein Protokoll. Eine **Anlagerichtlinie** ist das wirksamste Instrument, um § 84a Abs. 2 BGB im Streitfall belegen zu können. § 84b BGB regelt die Beschlussfassung (entsprechend § 32 BGB, mit Stimmverbot bei Rechtsgeschäften mit dem Organmitglied selbst), § 84c BGB behördliche Notmaßnahmen bei fehlenden Organmitgliedern.

### 6. Satzungsänderung — die Dreiteilung des [§ 85 BGB](https://www.gesetze-im-internet.de/bgb/__85.html)

| Stufe | Gegenstand | Voraussetzung |
|---|---|---|
| **§ 85 Abs. 1 BGB** | **Zweckänderung** oder erhebliche Zweckbeschränkung | Der Zweck kann nicht mehr dauernd und nachhaltig erfüllt werden **oder** er gefährdet das Gemeinwohl; zusätzlich muss die dauernde Erfüllung des neuen Zwecks gesichert erscheinen. Unter denselben Voraussetzungen ist auch die Umgestaltung in eine **Verbrauchsstiftung** zulässig |
| **§ 85 Abs. 2 BGB** | Zweckänderung in anderer Weise und **prägende Bestimmungen** der Stiftungsverfassung | Die Verhältnisse haben sich nach Errichtung **wesentlich verändert** und die Änderung ist zur Anpassung **erforderlich**. Prägend sind regelmäßig: **Name, Sitz, Art und Weise der Zweckerfüllung, Verwaltung des Grundstockvermögens** |
| **§ 85 Abs. 3 BGB** | **sonstige** Satzungsbestimmungen | Die Änderung muss **der Erfüllung des Stiftungszwecks dienen** |

**§ 85 Abs. 4 BGB — Gestaltungsmacht des Stifters:** Im Stiftungsgeschäft kann der Stifter Satzungsänderungen ausschließen oder beschränken; er kann sie den Organen auch **abweichend** von den Absätzen 1 bis 3 gestatten. Solche Öffnungsklauseln sind aber nur wirksam, wenn der Stifter **Inhalt und Ausmaß der Änderungsermächtigung hinreichend bestimmt festlegt** — eine pauschale Ermächtigung („Der Vorstand kann die Satzung ändern") ist unwirksam. Bei Neuerrichtungen gehört daher eine sorgfältig kalibrierte Änderungsklausel in das Stiftungsgeschäft; nachträglich lässt sie sich nicht mehr schaffen.

Satzungsänderungen bedürfen zusätzlich der behördlichen Genehmigung nach dem einschlägigen Verfahrensrecht; bei gemeinnützigen Stiftungen ist der Entwurf zuvor mit dem Finanzamt abzustimmen (§ 60a AO).

### 7. Zulegung, Zusammenlegung und Beendigung ([§ 86 BGB](https://www.gesetze-im-internet.de/bgb/__86.html), [§ 86a BGB](https://www.gesetze-im-internet.de/bgb/__86a.html), [§ 87 BGB](https://www.gesetze-im-internet.de/bgb/__87.html))

- **Zulegung (§ 86 BGB):** Die übertragende Stiftung überträgt ihr Vermögen **als Ganzes** auf eine bestehende übernehmende Stiftung. Voraussetzungen: wesentlich veränderte Verhältnisse, für die eine Satzungsänderung nach § 85 Abs. 2 bis 4 BGB nicht ausreicht (oder von Anfang an Auflösungsreife); **Zweckübereinstimmung im Wesentlichen**; gesicherte Fortführung durch die übernehmende Stiftung; Wahrung der Rechte von Destinatären mit satzungsmäßigen Ansprüchen.
- **Zusammenlegung (§ 86a BGB):** Mindestens zwei Stiftungen übertragen ihr Vermögen jeweils als Ganzes auf eine **neu zu errichtende** Stiftung; Voraussetzungen entsprechend.
- **Verfahren (§ 86b BGB):** durch **Vertrag** mit Genehmigung der für die übernehmende Stiftung zuständigen Behörde; bei Uneinigkeit kann die Behörde zulegen oder zusammenlegen, wobei die übernehmende Stiftung zustimmen muss.
- **Auflösung (§ 87 BGB):** Der Vorstand **soll** auflösen, wenn der Zweck endgültig nicht mehr dauernd und nachhaltig erfüllt werden kann — nicht endgültig ist das, solange eine Satzungsänderung die Stiftung wieder handlungsfähig machen kann. Die Verbrauchsstiftung ist mit Zeitablauf aufzulösen. Die Auflösung bedarf der behördlichen Genehmigung. § 87a BGB regelt die behördliche Aufhebung, § 87b BGB die Auflösung bei Insolvenz, § 87c BGB Vermögensanfall und Liquidation.

### 8. Stiftungsregister (StiftRG)

Mit der Reform wurde ein **bundesweites Stiftungsregister** beim Bundesamt für Justiz geschaffen; die Rechtsgrundlage ist das **Stiftungsregistergesetz (StiftRG)**. Vorgesehen sind eine Eintragungspflicht, **Publizitätswirkung** entsprechend § 15 HGB, öffentliche Einsehbarkeit und der Namenszusatz „e. S." bzw. „e. VS." für eingetragene (Verbrauchs-)Stiftungen.

> **⚠️ Inkrafttreten auf den 01.01.2028 verschoben (Stand 2026-07, am Gesetzestext verifiziert).** Das Stiftungsregister ist **noch nicht in Betrieb**. Die Inkraftsetzungsfußnote der amtlichen Fassung lautet:
>
> „*§ 20: Tritt gem. Art. 11 Abs. 1 Nr. 2 G v. 16.7.2021 I 2947 idF d. Art. 33 G v. 8.12.2025 I Nr. 319 am 1.1.2028 in Kraft*"
>
> Dieselbe Fußnote trägt § 18; die §§ 1 bis 18 und § 20 StiftRG sind auf gesetze-im-internet.de durchgängig als **„zukünftig in Kraft"** ausgewiesen. In Kraft ist allein **§ 19 StiftRG** (Verordnungsermächtigung), damit die Rechtsverordnung zur technischen Ausgestaltung vorbereitet werden kann.
>
> **Beratungsfolge — der häufigste Fehler in diesem Bereich:** Der ursprünglich vorgesehene Registerstart zum **01.01.2026** ist durch **Art. 33 des Gesetzes vom 08.12.2025 (BGBl. 2025 I Nr. 319)** auf den **01.01.2028** verschoben worden. Ein erheblicher Teil der Literatur, der Beratungspraxis und der Stiftungsratgeber nennt weiterhin den 01.01.2026. Wer darauf aufbaut, terminiert Eintragungspflichten, den Namenszusatz „e. S." / „e. VS." und die Publizitätswirkung **zwei Jahre zu früh**.
>
> **Bis zum 01.01.2028** gilt unverändert: Der Nachweis der Vertretungsberechtigung wird über die **Vertretungsbescheinigung der Stiftungsaufsicht** geführt; eine Registerpublizität entsprechend § 15 HGB besteht **nicht**, ein Gutglaubensschutz kann darauf also nicht gestützt werden.
>
> Die Übergangsfristen für Bestandsstiftungen und die Ausgestaltung durch Rechtsverordnung nach § 19 StiftRG bleiben `[unverifiziert - prüfen]`.

Landesrecht gilt fort für Aufsicht und Verfahren; § 88 BGB stellt klar, dass die Landesvorschriften über **kirchliche Stiftungen** unberührt bleiben.

## Quellen

### Statute

- [§ 80 BGB](https://www.gesetze-im-internet.de/bgb/__80.html), [§ 81 BGB](https://www.gesetze-im-internet.de/bgb/__81.html), [§ 82 BGB](https://www.gesetze-im-internet.de/bgb/__82.html), [§ 82a BGB](https://www.gesetze-im-internet.de/bgb/__82a.html)
- [§ 83 BGB](https://www.gesetze-im-internet.de/bgb/__83.html) (Stifterwille), [§ 83a BGB](https://www.gesetze-im-internet.de/bgb/__83a.html), [§ 83b BGB](https://www.gesetze-im-internet.de/bgb/__83b.html), [§ 83c BGB](https://www.gesetze-im-internet.de/bgb/__83c.html)
- [§ 84 BGB](https://www.gesetze-im-internet.de/bgb/__84.html), [§ 84a BGB](https://www.gesetze-im-internet.de/bgb/__84a.html), [§ 84b BGB](https://www.gesetze-im-internet.de/bgb/__84b.html), [§ 84c BGB](https://www.gesetze-im-internet.de/bgb/__84c.html)
- [§ 85 BGB](https://www.gesetze-im-internet.de/bgb/__85.html), [§ 86 BGB](https://www.gesetze-im-internet.de/bgb/__86.html), [§ 86a BGB](https://www.gesetze-im-internet.de/bgb/__86a.html), [§ 86b BGB](https://www.gesetze-im-internet.de/bgb/__86b.html)
- [§ 87 BGB](https://www.gesetze-im-internet.de/bgb/__87.html), [§ 87a BGB](https://www.gesetze-im-internet.de/bgb/__87a.html), [§ 87b BGB](https://www.gesetze-im-internet.de/bgb/__87b.html), [§ 87c BGB](https://www.gesetze-im-internet.de/bgb/__87c.html), [§ 88 BGB](https://www.gesetze-im-internet.de/bgb/__88.html)
- [Stiftungsregistergesetz (StiftRG)](https://www.gesetze-im-internet.de/stiftrg/) — §§ 1–18, 20 treten erst am **01.01.2028** in Kraft (Art. 33 G v. 08.12.2025, BGBl. 2025 I Nr. 319); in Kraft ist allein § 19 (Verordnungsermächtigung)
- [§ 31a BGB](https://www.gesetze-im-internet.de/bgb/__31a.html) (über § 84a Abs. 3 BGB), [§ 311b BGB](https://www.gesetze-im-internet.de/bgb/__311b.html)

### Kommentare

- Hüttemann/Rawert, in: Staudinger, BGB, Neubearbeitung zum Stiftungsrecht, §§ 80 ff. `[unverifiziert - Auflagenstand prüfen]`
- Weitemeyer, in: MüKoBGB, 9. Aufl. 2021, §§ 80 ff. `[unverifiziert - Auflagenstand prüfen]`
- Burgard, Gestaltungsfreiheit im Stiftungsrecht `[unverifiziert - prüfen]`

### Rechtsprechung

> Zur Reformfassung der §§ 80–88 BGB liegt noch wenig höchstrichterliche Rechtsprechung vor. Die Aussagen dieses Skills folgen daher bewusst dem **Gesetzeswortlaut** und der Kommentarliteratur; ältere Entscheidungen zum vorherigen Recht sind vor einer Übertragung auf die Neufassung ausdrücklich zu prüfen. Es werden hier **keine** Aktenzeichen zur Illustration genannt, für die kein belastbarer Fundstellenbeleg vorliegt.

## Ausgabeformat

```
STIFTUNG — <Name / Vorhaben> — <Datum>

I.    Vorhaben                      [Errichtung / Satzungsänderung / Zulegung / Auflösung / Haftung]
II.   Stiftungstyp § 80             [unbestimmte Zeit / Verbrauchsstiftung — Dauer: <…> Jahre]
III.  Stiftungsgeschäft § 81        Zweck [ ] Name [ ] Sitz [ ] Vorstandsbildung [ ]
        Verbrauchsstiftung Abs. 2:  Zeit [ ]  Verbrauchsregelung [ ]
        Form Abs. 3:                [Schriftform ✅ / Verfügung von Todes wegen / § 311b BGB]
        Gewidmetes Vermögen:        EUR <…>  Übergang § 82a: <…>
IV.   Anerkennung § 82              Ertragsprognose: [tragfähig ✅ / 🔴 unzureichend]
        Verbrauchsstiftung:         [mindestens zehn Jahre ✅/❌]
        Gemeinwohlgefährdung:       [nein / <…>]
V.    Vermögen §§ 83b, 83c          Grundstockvermögen: EUR <…>  Sonstiges: EUR <…>
        Umschichtungsgewinne:       [verwendbar / satzungsmäßig ausgeschlossen]
        Teilverbrauch Abs. 2:       [zugelassen — Aufstockungspflicht geregelt ✅/❌]
        Erhaltungsmaßstab:          [nominal / real — in Satzung geregelt ✅/❌]
VI.   Organe §§ 84, 84a             Vorstand: <…>  Vertretung: <…>
        BJR § 84a Abs. 2:           [Informationsgrundlage dokumentiert ✅ / 🔴]
        Anlagerichtlinie:           [vorhanden / empfohlen]
        Haftungsbeschränkung:       [Satzung Abs. 1 S. 3 / § 31a über Abs. 3]
VII.  Satzungsänderung § 85         Stufe: [Abs. 1 Zweck / Abs. 2 prägend / Abs. 3 sonstige]
        Voraussetzungen:            <Subsumtion>
        Stifterermächtigung Abs. 4: [vorhanden, hinreichend bestimmt ✅/❌]
        Genehmigung:                [Behörde <…>; Finanzamt § 60a AO abgestimmt ✅/❌]
VIII. Umstrukturierung              [Zulegung § 86 / Zusammenlegung § 86a — Vertrag § 86b]
IX.   Stiftungsregister             [nicht in Betrieb bis 01.01.2028 — Vertretungsbescheinigung der Stiftungsaufsicht]
        Nachweis Vertretung:        [Registerauszug / Vertretungsbescheinigung der Aufsicht]

Gesamtbefund: [🟢 / 🟡 / 🔴]
Offene Punkte: <Liste>
```

## Risiken / typische Fehler

- **Ertragsprognose zu optimistisch** — die Anerkennung nach § 82 BGB scheitert an der gesicherten dauernden Zweckerfüllung; bei der Verbrauchsstiftung zusätzlich an der Mindestdauer von zehn Jahren.
- **Grundstockvermögen angegriffen, ohne dass die Satzung es erlaubt** — Verstoß gegen § 83c Abs. 1 S. 1 BGB und Pflichtverletzung des Vorstands; ein Teilverbrauch braucht die Satzungsgrundlage **und** die Aufstockungspflicht nach Abs. 2.
- **Umschichtungsgewinne pauschal als Ertrag behandelt** — sie sind nach § 83c Abs. 1 S. 3 BGB nur verwendbar, soweit die Satzung es nicht ausschließt und die Erhaltung des Grundstockvermögens gewährleistet bleibt.
- **Satzungsänderung der falschen Stufe des § 85 BGB zugeordnet** — Name, Sitz, Art der Zweckerfüllung und Verwaltung des Grundstockvermögens sind **prägende Bestimmungen** nach Abs. 2 und brauchen wesentlich veränderte Verhältnisse, nicht nur Zweckdienlichkeit.
- **Pauschale Änderungsermächtigung im Stiftungsgeschäft** — nach § 85 Abs. 4 S. 3 BGB unwirksam, weil Inhalt und Ausmaß nicht hinreichend bestimmt sind; nachträglich lässt sich die Ermächtigung nicht mehr schaffen.
- **Business Judgment Rule ohne Dokumentation beansprucht** — § 84a Abs. 2 BGB verlangt eine **angemessene Informationsgrundlage**; ohne Protokoll und Anlagerichtlinie ist sie im Streit nicht zu belegen.
- **Zulegung ohne Zweckübereinstimmung betrieben** — § 86 Nr. 2 BGB verlangt, dass der Zweck der übertragenden Stiftung im Wesentlichen mit einem Zweck der übernehmenden übereinstimmt.
- **Registerstart auf 01.01.2026 datiert** — das Stiftungsregister startet erst am **01.01.2028** (Art. 33 G v. 08.12.2025). Ein Großteil der Literatur nennt noch 2026. Wer darauf aufbaut, terminiert Eintragungspflicht, Namenszusatz und Publizitätswirkung zwei Jahre zu früh; bis dahin trägt allein die Vertretungsbescheinigung der Stiftungsaufsicht, eine Publizitätswirkung entsprechend § 15 HGB besteht nicht.
