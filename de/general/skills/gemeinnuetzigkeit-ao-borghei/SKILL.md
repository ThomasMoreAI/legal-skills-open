---
name: gemeinnuetzigkeit-ao-borghei
title: /vereins-stiftungs-gemeinnuetzigkeitsrecht:gemeinnuetzigkeit-ao
description: Prüfung und Sicherung der Steuerbegünstigung nach §§ 51–68 AO – steuerbegünstigte Zwecke § 52 AO, Selbstlosigkeit § 55 AO mit zeitnaher Mittelverwendung § 55 Abs. 1 Nr. 5 AO und Rücklagen § 62 AO, Ausschließlichkeit § 56 AO, Unmittelbarkeit § 57 AO einschließlich planmäßigem Zusammenwirken, formstrenge Mustersatzung nach Anlage 1 zu § 60 AO, gesonderte Feststellung der Satzungsmäßigkeit § 60a AO, Vier-Sphären-Systematik mit Zweckbetrieb §§ 65–68 AO und Besteuerungsgrenze § 64 Abs. 3 AO, Mittelweitergabe § 58 Nr. 1 AO sowie Vermögensbindung und rückwirkende Nachversteuerung § 61 Abs. 3 AO. Use when eine Satzung auf Gemeinnützigkeit geprüft, eine Feststellung nach § 60a AO beantragt, eine Sphärenzuordnung vorgenommen oder der drohende Entzug der Gemeinnützigkeit abgewehrt werden soll.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/vereins-stiftungs-gemeinnuetzigkeitsrecht/skills/gemeinnuetzigkeit-ao
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: general
language: de
---

# /vereins-stiftungs-gemeinnuetzigkeitsrecht:gemeinnuetzigkeit-ao

## Zweck

Die Steuerbegünstigung ist kein Status, sondern ein **fortlaufender Zustand**: Sie hängt an der Satzung **und** an der tatsächlichen Geschäftsführung. Dieser Skill prüft beides — er stellt die Satzung formstreng gegen die **Mustersatzung Anlage 1 zu § 60 AO**, ordnet jede Einnahme einer der **vier Sphären** zu und sichert die zeitnahe Mittelverwendung.

## Eingaben

- Körperschaft: Verein, Stiftung, gGmbH; Gründungsjahr; bisheriger Status (Feststellung § 60a AO, Freistellungsbescheid, Anlage zum Körperschaftsteuerbescheid)
- Satzung im geltenden Wortlaut, insbesondere Zweck-, Selbstlosigkeits- und Vermögensbindungsklausel
- Tatsächliche Tätigkeiten mit Einnahmen und Ausgaben, gegliedert nach Tätigkeitsart
- Jährliche Gesamteinnahmen und Einnahmen aus wirtschaftlichen Geschäftsbetrieben (jeweils einschließlich Umsatzsteuer)
- Mittelbestand, Zufluss- und Verwendungsjahre; gebildete Rücklagen mit Zweck und Bildungsjahr
- Geplante Kooperationen und Mittelweitergaben an andere Körperschaften
- Anlass: Neugründung, Satzungsänderung, Betriebsprüfung, angekündigter Entzug

## Sub-Agent-Architektur

1. **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) liefert §§ 51–68 AO, die Anlage 1 zu § 60 AO im Wortlaut und den AEAO als Verwaltungsauffassung.
2. **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) erstellt Satzungsentwurf, Sphärenzuordnung, Mittelverwendungsrechnung und Antrag nach § 60a AO.
3. **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft die Satzung Wort für Wort gegen die Mustersatzung, die Rücklagenbildung gegen § 62 AO und die Fristen der Mittelverwendung.

## Ablauf

### 1. Steuerbegünstigte Zwecke ([§ 52 AO](https://www.gesetze-im-internet.de/ao_1977/__52.html))

Gemeinnützig sind Zwecke, die darauf gerichtet sind, die **Allgemeinheit** auf materiellem, geistigem oder sittlichem Gebiet **selbstlos zu fördern**. § 52 Abs. 2 AO enthält einen **abschließenden Katalog** der anerkannten Zwecke (Wissenschaft und Forschung, Religion, öffentliches Gesundheitswesen, Jugend- und Altenhilfe, Kunst und Kultur, Denkmalschutz, Erziehung und Bildung, Naturschutz, Wohlfahrtswesen, Sport, Tierschutz u. a.); nur über die Öffnungsklausel des § 52 Abs. 2 S. 2 AO kann ein weiterer Zweck für gemeinnützig erklärt werden.

**Keine Förderung der Allgemeinheit** liegt vor, wenn der Kreis der Geförderten fest abgeschlossen ist (Belegschaft eines Unternehmens, Angehörige einer Familie) oder infolge hoher Aufnahmegebühren und Beiträge dauernd klein bleibt. Neben § 52 AO stehen **mildtätige** Zwecke (§ 53 AO — Unterstützung bedürftiger Personen) und **kirchliche** Zwecke (§ 54 AO); die Satzung muss die verfolgte Kategorie ausdrücklich benennen.

### 2. Selbstlosigkeit und zeitnahe Mittelverwendung ([§ 55 AO](https://www.gesetze-im-internet.de/ao_1977/__55.html))

Selbstlos ist die Förderung, wenn nicht in erster Linie eigenwirtschaftliche Zwecke verfolgt werden und kumulativ:

1. **Nr. 1 — Mittelverwendungsgebot:** Mittel nur für satzungsmäßige Zwecke; **keine Gewinnanteile oder sonstigen Zuwendungen an Mitglieder** in dieser Eigenschaft; kein Einsatz für die Unterstützung politischer Parteien.
2. **Nr. 2:** Mitglieder erhalten bei Ausscheiden oder Auflösung nicht mehr als eingezahlte Kapitalanteile und den gemeinen Wert geleisteter Sacheinlagen.
3. **Nr. 3 — Begünstigungsverbot:** keine Begünstigung durch zweckfremde Ausgaben oder **unverhältnismäßig hohe Vergütungen**. Vorstandsvergütungen brauchen eine Satzungsgrundlage und einen Fremdvergleich; „unverhältnismäßig hoch" wird an der Obergrenze marktüblicher Vergleichsvergütungen gemessen `[unverifiziert - prüfen]`.
4. **Nr. 4 — Vermögensbindung:** Bei Auflösung oder Wegfall des bisherigen Zwecks darf das Vermögen nur für steuerbegünstigte Zwecke verwendet werden.
5. **Nr. 5 — zeitnahe Mittelverwendung:** Mittel sind **vorbehaltlich des § 62 AO** grundsätzlich zeitnah zu verwenden. Zeitnah ist die Verwendung, wenn die Mittel **spätestens in den auf den Zufluss folgenden zwei Kalender- oder Wirtschaftsjahren** für die satzungsmäßigen Zwecke verwendet werden. **Ausnahme (§ 55 Abs. 1 Nr. 5 S. 4 AO): Satz 1 gilt nicht für Körperschaften mit jährlichen Einnahmen von nicht mehr als 100.000 Euro** — kleine Körperschaften sind von der zeitnahen Mittelverwendung befreit.

**Mittelverwendungsrechnung.** Die Einhaltung ist jahrgangsweise nachzuweisen: Zufluss je Jahr, Verwendung je Jahr, Restbestand mit Verfallsjahr. Ein bloßer Kassenbestand ohne Zuordnung ist der häufigste Beanstandungsgrund in der Betriebsprüfung.

Die Zwei-Jahres-Frist und die Rücklagenfristen rechnet der deterministische Rechner:

```bash
python -m scripts.legal_calc.cli frist --ereignis 15.01.2026 --menge 1 --einheit monate --land BY
```

Er leistet **ausschließlich** die Arithmetik der §§ 187–193 BGB. **Fristbeginn und Zugang bleiben rechtliche Eingaben** — welches Jahr als Zuflussjahr gilt und wann ein Bescheid zugegangen ist, bewertet der Bearbeiter.

### 3. Rücklagen ([§ 62 AO](https://www.gesetze-im-internet.de/ao_1977/__62.html))

| Rücklage | Norm | Voraussetzung und Grenze |
|---|---|---|
| **Zweckgebundene (Projekt-)Rücklage** | § 62 Abs. 1 Nr. 1 AO | Für konkrete, zeitlich bestimmte Vorhaben |
| **Wiederbeschaffungsrücklage** | § 62 Abs. 1 Nr. 2 AO | Für die beabsichtigte Wiederbeschaffung erforderlicher Wirtschaftsgüter; Höhe bemisst sich nach der regulären AfA des zu ersetzenden Guts, höhere Zuführung ist nachzuweisen |
| **Freie Rücklage** | § 62 Abs. 1 Nr. 3 AO | Höchstens **ein Drittel des Überschusses aus der Vermögensverwaltung** und darüber hinaus höchstens **10 Prozent der sonstigen zeitnah zu verwendenden Mittel**; ein nicht ausgeschöpfter Höchstbetrag kann in den **folgenden zwei Jahren** nachgeholt werden |
| **Beteiligungsrücklage** | § 62 Abs. 1 Nr. 4 AO | Zum Erwerb von Gesellschaftsrechten zur Erhaltung der prozentualen Beteiligung; mindert die freie Rücklage |

**§ 62 Abs. 2 AO:** Die Bildung hat **innerhalb der Frist des § 55 Abs. 1 Nr. 5 S. 3 AO** zu erfolgen. Rücklagen nach Nr. 1, 2 und 4 sind **unverzüglich aufzulösen**, sobald der Bildungsgrund entfallen ist; die frei gewordenen Mittel unterliegen erneut der Zwei-Jahres-Frist.

**§ 62 Abs. 3 AO — nicht zeitnah zu verwendende Zuführungen:** Zuwendungen von Todes wegen ohne Verwendungsauflage, Zuwendungen mit ausdrücklicher Vermögenswidmung, Zuwendungen aufgrund eines Spendenaufrufs zur Vermögensaufstockung sowie Sachzuwendungen, die ihrer Natur nach zum Vermögen gehören. **§ 62 Abs. 4 AO:** Eine Stiftung kann im Errichtungsjahr und in den **drei folgenden Kalenderjahren** Überschüsse aus der Vermögensverwaltung und Gewinne aus wirtschaftlichen Geschäftsbetrieben ganz oder teilweise ihrem Vermögen zuführen.

### 4. Ausschließlichkeit und Unmittelbarkeit ([§ 56 AO](https://www.gesetze-im-internet.de/ao_1977/__56.html), [§ 57 AO](https://www.gesetze-im-internet.de/ao_1977/__57.html))

- **§ 56 AO — Ausschließlichkeit:** Die Körperschaft darf **nur** ihre steuerbegünstigten satzungsmäßigen Zwecke verfolgen. Ein steuerpflichtiger wirtschaftlicher Geschäftsbetrieb ist unschädlich, solange er der Mittelbeschaffung dient und nicht zum Selbstzweck wird.
- **§ 57 Abs. 1 AO — Unmittelbarkeit:** Die Zwecke sind selbst zu verwirklichen; **Hilfspersonen** sind zulässig, wenn deren Wirken nach den rechtlichen und tatsächlichen Beziehungen wie eigenes Wirken anzusehen ist (Weisungsrecht und Kontrolle vertraglich absichern).
- **§ 57 Abs. 2 AO:** Dachverbände, in denen steuerbegünstigte Körperschaften zusammengefasst sind, stehen unmittelbar tätigen Körperschaften gleich.
- **§ 57 Abs. 3 AO — planmäßiges Zusammenwirken (seit 2021):** Eine Körperschaft handelt auch dann unmittelbar, wenn sie **satzungsgemäß durch planmäßiges Zusammenwirken** mit mindestens einer weiteren Körperschaft, die im Übrigen die Voraussetzungen der §§ 51 bis 68 AO erfüllt, einen steuerbegünstigten Zweck verwirklicht. Für die Zweckbetriebseigenschaft sind die Tätigkeiten der zusammenwirkenden Körperschaften **zusammenzufassen**. Damit können arbeitsteilige Konzernstrukturen (Service-, Wäscherei-, IT- oder Personalgesellschaften) steuerbegünstigt betrieben werden. **Voraussetzung:** Das Zusammenwirken und die Partnerkörperschaften müssen **in der Satzung** benannt sein — fehlt die Satzungsgrundlage, greift § 57 Abs. 3 AO nicht.
- **§ 57 Abs. 4 AO:** Auch das ausschließliche Halten und Verwalten von Anteilen an steuerbegünstigten Kapitalgesellschaften ist unmittelbare Zweckverfolgung (Holdingprivileg).

### 5. Mustersatzung ([§ 60 AO](https://www.gesetze-im-internet.de/ao_1977/__60.html) und [Anlage 1 zu § 60 AO](https://www.gesetze-im-internet.de/ao_1977/anlage_1.html))

**§ 60 Abs. 1 S. 1 AO:** Satzungszwecke und die Art ihrer Verwirklichung müssen so genau bestimmt sein, dass sich aus der Satzung prüfen lässt, ob die Voraussetzungen vorliegen. **§ 60 Abs. 1 S. 2 AO: Die Satzung muss die in der Anlage 1 bezeichneten Festlegungen enthalten.** Die Mustersatzung ist damit **formstreng** — die Finanzverwaltung verlangt die Aufnahme der Festlegungen dem Inhalt nach vollständig; das Weglassen eines einzigen Bausteins führt zur Ablehnung der Feststellung nach § 60a AO. **§ 60 Abs. 2 AO:** Die Satzung muss den Erfordernissen bei Körperschaft- und Gewerbesteuer **während des ganzen Veranlagungszeitraums** entsprechen — eine unterjährige Heilung wirkt nicht zurück.

**Bausteine der Anlage 1 zu § 60 AO — Gerüst mit Ausfüllhinweisen:**

> **§ 1** — „Der/Die … (Körperschaft) mit Sitz in … verfolgt **ausschließlich und unmittelbar** – gemeinnützige – mildtätige – kirchliche – Zwecke (nicht verfolgte Zwecke streichen) im Sinne des Abschnitts ‚Steuerbegünstigte Zwecke' der Abgabenordnung. Zweck der Körperschaft ist … Der Satzungszweck wird verwirklicht insbesondere durch …"
>
> → Der **Zweck** und die **Art der Verwirklichung** sind getrennt und konkret zu benennen; „Förderung des Gemeinwohls" genügt nicht.
>
> **§ 2** — „Die Körperschaft ist **selbstlos** tätig; sie verfolgt nicht in erster Linie eigenwirtschaftliche Zwecke."
>
> **§ 3** — „**Mittel der Körperschaft dürfen nur für die satzungsmäßigen Zwecke verwendet werden.** Die Mitglieder erhalten keine Zuwendungen aus Mitteln der Körperschaft."
>
> → Bei Kapitalgesellschaften zusätzlich: keine Gewinnanteile und sonstigen Zuwendungen an Gesellschafter; Rückgewähr bei Ausscheiden nur bis zu eingezahlten Kapitalanteilen und dem gemeinen Wert der Sacheinlagen.
>
> **§ 4** — „Es darf **keine Person** durch Ausgaben, die dem Zweck der Körperschaft fremd sind, oder durch **unverhältnismäßig hohe Vergütungen** begünstigt werden."
>
> **§ 5 (Vermögensbindung)** — „Bei Auflösung oder Aufhebung der Körperschaft oder bei Wegfall steuerbegünstigter Zwecke fällt das Vermögen an … (Bezeichnung einer juristischen Person des öffentlichen Rechts oder einer anderen steuerbegünstigten Körperschaft), die es unmittelbar und ausschließlich für gemeinnützige, mildtätige oder kirchliche Zwecke zu verwenden hat."
>
> → Alternativ nach Anlage 1 die Anfallvariante mit **Angabe eines bestimmten Zwecks**. Die Klausel muss nach § 61 Abs. 1 AO so genau sein, dass sich anhand der Satzung prüfen lässt, ob der Verwendungszweck steuerbegünstigt ist. Ein bloßes „für gemeinnützige Zwecke" ohne Empfänger oder bestimmten Zweck genügt **nicht**.

### 6. Feststellung der Satzungsmäßigkeit ([§ 60a AO](https://www.gesetze-im-internet.de/ao_1977/__60a.html))

Die Einhaltung der satzungsmäßigen Voraussetzungen wird **gesondert festgestellt** — auf **Antrag** der Körperschaft oder von Amts wegen bei der Veranlagung, wenn noch keine Feststellung erfolgt ist (§ 60a Abs. 2 AO). Die Feststellung ist für die Besteuerung bindend und ist die Grundlage dafür, Zuwendungsbestätigungen auszustellen.

- **Abs. 3:** Die Bindungswirkung entfällt ab dem Zeitpunkt, in dem die zugrunde liegenden Rechtsvorschriften aufgehoben oder geändert werden.
- **Abs. 4:** Ändern sich die für die Feststellung erheblichen **Verhältnisse**, ist die Feststellung mit Wirkung vom Zeitpunkt der Änderung **aufzuheben** — deshalb ist **jede** Satzungsänderung vor dem Beschluss mit dem Finanzamt abzustimmen und danach einzureichen.
- **Abs. 5:** Materielle Fehler des Feststellungsbescheids können mit Wirkung ab dem Kalenderjahr beseitigt werden, das auf die Bekanntgabe der Aufhebung folgt.
- **Abs. 6:** Liegen bis zum Erlass des erstmaligen Körperschaftsteuer- oder Freistellungsbescheids Erkenntnisse vor, dass die **tatsächliche Geschäftsführung** gegen die satzungsmäßigen Voraussetzungen verstößt, ist die Feststellung **abzulehnen**; Entsprechendes gilt für die Aufhebung bestehender Feststellungen.

Die Feststellung nach § 60a AO betrifft **nur die Satzung**. Die tatsächliche Geschäftsführung wird nach § 63 AO gesondert geprüft — regelmäßig im Rahmen der turnusmäßigen Veranlagung und der Betriebsprüfung (`/steuerrecht:aussenpruefung-betriebspruefung`).

### 7. Vier-Sphären-Systematik

| Sphäre | Inhalt | Ertragsteuer | Umsatzsteuer (Grundregel) |
|---|---|---|---|
| **1. Ideeller Bereich** | Mitgliedsbeiträge, echte Spenden, Zuschüsse ohne Leistungsaustausch | steuerfrei | nicht steuerbar (kein Leistungsaustausch) |
| **2. Vermögensverwaltung** | Zinsen, Dividenden, Vermietung und Verpachtung, Kapitalanlagen (§ 14 S. 3 AO) | steuerfrei | regelmäßig steuerfrei oder ermäßigt |
| **3. Zweckbetrieb** (§§ 65–68 AO) | Wirtschaftlicher Geschäftsbetrieb, der den Zweck **selbst** verwirklicht | steuerfrei | regelmäßig ermäßigter Steuersatz |
| **4. Steuerpflichtiger wirtschaftlicher Geschäftsbetrieb** (§ 64 AO) | Gaststätte, Verkauf, Werbung, gesellige Veranstaltungen | **steuerpflichtig** | Regelsteuersatz |

**Zweckbetrieb — § 65 AO (Generalklausel), kumulativ:**
1. Der Betrieb dient in seiner Gesamtrichtung dazu, die steuerbegünstigten Zwecke **zu verwirklichen**;
2. die Zwecke können **nur** durch einen solchen Geschäftsbetrieb erreicht werden;
3. der Betrieb tritt zu nicht begünstigten Betrieben derselben oder ähnlicher Art **nicht in größerem Umfang in Wettbewerb**, als es zur Zweckerfüllung unvermeidbar ist.

§§ 66–68 AO enthalten **Sonderzweckbetriebe** kraft Gesetzes: Einrichtungen der Wohlfahrtspflege (§ 66 AO), Krankenhäuser (§ 67 AO), sportliche Veranstaltungen mit Zweckbetriebsgrenze (§ 67a AO) sowie den Katalog des § 68 AO (Alten- und Pflegeheime, Kindergärten, Werkstätten für behinderte Menschen, Kulturbetriebe, Volkshochschulen u. a.). Bei planmäßigem Zusammenwirken nach § 57 Abs. 3 AO sind die Tätigkeiten der beteiligten Körperschaften für die Zweckbetriebsprüfung **zusammenzufassen**.

**§ 64 AO — Besteuerungsgrenze.** Nach § 64 Abs. 2 AO werden mehrere steuerpflichtige wirtschaftliche Geschäftsbetriebe als **ein** Betrieb behandelt (Saldierung von Gewinnen und Verlusten). Nach **§ 64 Abs. 3 AO** unterliegen die Besteuerungsgrundlagen **nicht** der Körperschaft- und Gewerbesteuer, wenn die Einnahmen einschließlich Umsatzsteuer aus wirtschaftlichen Geschäftsbetrieben, die keine Zweckbetriebe sind, insgesamt **50.000 Euro im Jahr nicht übersteigen**.

> **Hinweis zur Betragsgrenze:** Der amtliche Wortlaut des § 64 Abs. 3 AO auf gesetze-im-internet.de nennt **50 000 Euro**. Ältere Literatur und Musterunterlagen nennen noch 45.000 Euro (bzw. davor 35.000 Euro). **Vor jeder Auskunft die aktuell geltende Fassung prüfen** — die Grenze ist mehrfach angehoben worden.

§ 64 Abs. 4 AO behandelt die Aufspaltung in mehrere Körperschaften zur mehrfachen Inanspruchnahme der Grenze als **Gestaltungsmissbrauch** nach § 42 AO. § 64 Abs. 5 und 6 AO erlauben Gewinnschätzungen (Altmaterialverwertung; pauschal 15 Prozent der Einnahmen bei Werbung im Zusammenhang mit der steuerbegünstigten Tätigkeit, Totalisatorbetrieben und der zweiten Fraktionierungsstufe der Blutspendedienste).

### 8. Mittelweitergabe ([§ 58 AO](https://www.gesetze-im-internet.de/ao_1977/__58.html)) und Entzug ([§ 61 AO](https://www.gesetze-im-internet.de/ao_1977/__61.html))

**§ 58 Nr. 1 AO** erlaubt die **Mittelweitergabe** an andere Körperschaften und an juristische Personen des öffentlichen Rechts zur Verwendung für steuerbegünstigte Zwecke. Bedingungen: Empfänger des privaten Rechts müssen **selbst steuerbegünstigt** sein; soll die Mittelweitergabe die **einzige** Art der Zweckverwirklichung sein, ist sie **in der Satzung als Art der Zweckverwirklichung zu benennen**. Weitere Unschädlichkeitstatbestände: Vermögensausstattung anderer Körperschaften mit Grenzen (Nr. 3), Überlassung von Arbeitskräften (Nr. 4) und Räumen (Nr. 5), Stifterunterhalt bis zu einem Drittel des Einkommens (Nr. 6), untergeordnete gesellige Zusammenkünfte (Nr. 7), bezahlter Sport neben unbezahltem (Nr. 8), Photovoltaikanlagen (Nr. 11).

**§ 61 AO — Vermögensbindung und Nachversteuerung.** Nach Abs. 1 liegt eine ausreichende Vermögensbindung nur vor, wenn der Verwendungszweck in der Satzung so genau bestimmt ist, dass sich die Steuerbegünstigung anhand der Satzung prüfen lässt. **§ 61 Abs. 3 AO — Grundsatz der Vermögensbindung:** Wird die Bestimmung über die Vermögensbindung nachträglich so geändert, dass sie den Anforderungen des § 55 Abs. 1 Nr. 4 AO nicht mehr entspricht, gilt sie **von Anfang an als steuerlich nicht ausreichend**; § 175 Abs. 1 S. 1 Nr. 2 AO ist mit der Maßgabe anzuwenden, dass Steuerbescheide für Steuern erlassen, aufgehoben oder geändert werden können, die **innerhalb der letzten zehn Kalenderjahre** vor der Änderung entstanden sind. Das ist die schärfste Sanktion des Gemeinnützigkeitsrechts: eine rückwirkende Nachversteuerung über zehn Jahre.

## Quellen

### Statute

- [§ 52 AO](https://www.gesetze-im-internet.de/ao_1977/__52.html), [§ 53 AO](https://www.gesetze-im-internet.de/ao_1977/__53.html), [§ 54 AO](https://www.gesetze-im-internet.de/ao_1977/__54.html)
- [§ 55 AO](https://www.gesetze-im-internet.de/ao_1977/__55.html), [§ 56 AO](https://www.gesetze-im-internet.de/ao_1977/__56.html), [§ 57 AO](https://www.gesetze-im-internet.de/ao_1977/__57.html), [§ 58 AO](https://www.gesetze-im-internet.de/ao_1977/__58.html)
- [§ 60 AO](https://www.gesetze-im-internet.de/ao_1977/__60.html), [Anlage 1 zu § 60 AO](https://www.gesetze-im-internet.de/ao_1977/anlage_1.html), [§ 60a AO](https://www.gesetze-im-internet.de/ao_1977/__60a.html)
- [§ 61 AO](https://www.gesetze-im-internet.de/ao_1977/__61.html), [§ 62 AO](https://www.gesetze-im-internet.de/ao_1977/__62.html), [§ 63 AO](https://www.gesetze-im-internet.de/ao_1977/__63.html), [§ 64 AO](https://www.gesetze-im-internet.de/ao_1977/__64.html)
- [§ 65 AO](https://www.gesetze-im-internet.de/ao_1977/__65.html), [§ 66 AO](https://www.gesetze-im-internet.de/ao_1977/__66.html), [§ 67 AO](https://www.gesetze-im-internet.de/ao_1977/__67.html), [§ 67a AO](https://www.gesetze-im-internet.de/ao_1977/__67a.html), [§ 68 AO](https://www.gesetze-im-internet.de/ao_1977/__68.html)
- [§ 14 AO](https://www.gesetze-im-internet.de/ao_1977/__14.html) (wirtschaftlicher Geschäftsbetrieb), [§ 42 AO](https://www.gesetze-im-internet.de/ao_1977/__42.html), [§ 175 AO](https://www.gesetze-im-internet.de/ao_1977/__175.html)
- [§ 5 Abs. 1 Nr. 9 KStG](https://www.gesetze-im-internet.de/kstg_1977/__5.html) (Steuerbefreiung), [§ 12 UStG](https://www.gesetze-im-internet.de/ustg_1980/__12.html) (ermäßigter Satz)

### Kommentare

- Hüttemann, Gemeinnützigkeits- und Spendenrecht, 5. Aufl. 2021 `[unverifiziert - Auflagenstand prüfen]`
- Seer, in: Tipke/Kruse, AO/FGO, §§ 51 ff. AO `[unverifiziert - Auflagenstand prüfen]`
- **Anwendungserlass zur Abgabenordnung (AEAO)** zu §§ 51–68 AO — Verwaltungsauffassung, für die Finanzämter bindend, für Gerichte nicht. Fassung und Randziffern `[unverifiziert - prüfen]`

### Rechtsprechung

> Die tragenden Aussagen dieses Skills folgen unmittelbar aus dem Wortlaut der §§ 51–68 AO und der Anlage 1 zu § 60 AO, die oben verlinkt sind. Zur Auslegung einzelner Merkmale (Wettbewerbsklausel des § 65 Nr. 3 AO, unverhältnismäßig hohe Vergütungen nach § 55 Abs. 1 Nr. 3 AO) ist die BFH-Rechtsprechung **fallbezogen in juris oder Beck-Online** zu recherchieren; hier werden **keine** Aktenzeichen ohne belastbaren Fundstellenbeleg genannt.

## Ausgabeformat

```
GEMEINNÜTZIGKEITS-PRÜFUNG — <Körperschaft> — <Datum>

I.    Zweck § 52 AO                 [Katalognummer <…> / mildtätig § 53 / kirchlich § 54]
        Förderung der Allgemeinheit: [✅ / 🔴 abgeschlossener Personenkreis]
II.   Selbstlosigkeit § 55 AO       Nr. 1 [ ] Nr. 2 [ ] Nr. 3 [ ] Nr. 4 [ ] Nr. 5 [ ]
        Vergütungen:                [fremdüblich / 🔴 unverhältnismäßig]
III.  Zeitnahe Mittelverwendung     Zufluss <Jahr>: EUR <…> → zu verwenden bis <Jahr>
        Rechnung geführt:           [✅ / 🔴]
        Befreiung § 55 I Nr. 5 S. 4: [Einnahmen ≤ 100.000 EUR: ja / nein]
IV.   Rücklagen § 62 AO             frei (Nr. 3): EUR <…>  [1/3 VV + 10 % ✅/❌]
                                    zweckgebunden (Nr. 1): EUR <…> — Vorhaben <…>
                                    Wiederbeschaffung (Nr. 2): EUR <…>
        Auflösungspflicht Abs. 2:   [keine / fällig für <…>]
V.    Ausschließlichkeit § 56       [✅ / 🔴]
      Unmittelbarkeit § 57          [selbst / Hilfsperson Abs. 1 / Zusammenwirken Abs. 3]
        Satzungsgrundlage Abs. 3:   [Partner benannt ✅ / 🔴 fehlt]
VI.   Satzung § 60 + Anlage 1       § 1 [ ] § 2 [ ] § 3 [ ] § 4 [ ] § 5 [ ]
        Zweck + Art der Verwirkl.:  [konkret ✅ / 🔴 zu allgemein]
        Vermögensbindung § 61 I:    [bestimmt ✅ / 🔴]
VII.  Feststellung § 60a AO         [vorhanden vom <…> / beantragt / abgelehnt]
        Satzungsänderung:           [mit FA abgestimmt ✅/❌ — Aufhebung nach Abs. 4 droht?]
VIII. Vier Sphären
        1 Ideell:                   EUR <…>
        2 Vermögensverwaltung:      EUR <…>
        3 Zweckbetrieb §§ 65–68:    EUR <…>  Norm: <…>
        4 Wirtschaftl. Gesch.betr.: EUR <…>  [Besteuerungsgrenze § 64 Abs. 3 AO: über/unter]
IX.   Mittelweitergabe § 58 Nr. 1   [Empfänger steuerbegünstigt ✅/❌; Satzungsnennung erforderlich?]
X.    Risiko Entzug § 61 Abs. 3 AO  [🟢 / 🟡 / 🔴 — Nachversteuerung bis zu 10 Jahre]

Gesamtbefund: [🟢 / 🟡 / 🔴]
Sofortmaßnahmen: <Liste>
```

## Risiken / typische Fehler

- **Mustersatzung nur sinngemäß übernommen** — § 60 Abs. 1 S. 2 AO verlangt die Festlegungen der Anlage 1; ein fehlender Baustein führt zur Ablehnung der Feststellung nach § 60a AO.
- **Vermögensbindungsklausel zu unbestimmt** — „für gemeinnützige Zwecke" ohne Empfänger oder bestimmten Zweck genügt § 61 Abs. 1 AO nicht.
- **Vermögensbindung nachträglich geändert** — § 61 Abs. 3 AO lässt die Klausel **von Anfang an** als unzureichend gelten und eröffnet die Nachversteuerung für zehn Kalenderjahre.
- **Zeitnahe Mittelverwendung nicht nachgewiesen** — ohne jahrgangsweise Mittelverwendungsrechnung ist der Verstoß in der Betriebsprüfung nicht zu widerlegen; die Frist beträgt zwei Kalender- oder Wirtschaftsjahre nach dem Zufluss.
- **Freie Rücklage über den Höchstbetrag gebildet** — § 62 Abs. 1 Nr. 3 AO begrenzt auf ein Drittel des Überschusses aus der Vermögensverwaltung zuzüglich 10 Prozent der sonstigen zeitnah zu verwendenden Mittel.
- **Zweckbetrieb angenommen, ohne § 65 AO durchzuprüfen** — alle drei Voraussetzungen sind kumulativ; die Wettbewerbsklausel der Nr. 3 wird am häufigsten übersehen.
- **Besteuerungsgrenze mit einem veralteten Betrag gerechnet** — § 64 Abs. 3 AO ist mehrfach angehoben worden; die geltende Fassung ist vor jeder Auskunft zu prüfen.
- **Aufspaltung zur mehrfachen Nutzung der Besteuerungsgrenze** — § 64 Abs. 4 AO wertet das ausdrücklich als Gestaltungsmissbrauch nach § 42 AO.
- **Planmäßiges Zusammenwirken ohne Satzungsgrundlage** — § 57 Abs. 3 AO greift nur, wenn das Zusammenwirken und die Partnerkörperschaften in der Satzung benannt sind.
- **Satzungsänderung ohne Abstimmung mit dem Finanzamt beschlossen** — nach § 60a Abs. 4 AO ist die Feststellung mit Wirkung vom Zeitpunkt der Änderung aufzuheben.
