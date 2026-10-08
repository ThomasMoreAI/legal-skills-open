---
name: stoerung-geschaeftsgrundlage-borghei
title: /vertragsrecht:stoerung-geschaeftsgrundlage
description: Prüfung der Störung der Geschäftsgrundlage nach § 313 BGB – reales und hypothetisches Element, Zumutbarkeitsprüfung, Subsidiarität gegenüber vertraglicher Risikoverteilung und Gewährleistungsrecht, Anpassungsverlangen und Rücktritt oder Kündigung nach § 313 Abs. 3 BGB sowie die vertragliche Alternative durch Force-Majeure-, Preisanpassungs- und Kostenelementeklauseln. Use when sich nach Vertragsschluss die Umstände erheblich verändert haben (Kostenexplosion, Lieferkettenstörung, Sanktionen, behördliche Anordnung) und eine Vertragsanpassung oder Lösung geprüft wird.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/vertragsrecht/skills/stoerung-geschaeftsgrundlage
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: contracts
language: de
---

# /vertragsrecht:stoerung-geschaeftsgrundlage

## Zweck

§ 313 BGB ist die Norm, auf die sich Mandanten am schnellsten berufen und die am seltensten trägt: Sie ist **subsidiär**, verlangt eine **schwerwiegende** Veränderung und führt in erster Linie nur zur **Anpassung**, nicht zur Lösung vom Vertrag. Dieser Skill prüft die Voraussetzungen streng in der richtigen Reihenfolge, formuliert das Anpassungsverlangen und zeigt die vertragsgestalterische Alternative: Force-Majeure- und Preisanpassungsklauseln, die den Fall vorweg regeln.

## Eingaben

- Vertrag: Typ, Datum, Laufzeit, Leistungsinhalt, Preisregelung (Festpreis, Gleitpreis, Indexbindung)
- Veränderter Umstand: Art, Eintrittszeitpunkt, Ausmaß (bezifferte Kostensteigerung, Lieferausfall, Hoheitsakt)
- Vorhersehbarkeit bei Vertragsschluss; Erkenntnisse aus der Vertragsverhandlung
- Vertragliche Risikoverteilung: Force-Majeure-Klausel, Preisanpassungs-, Material- oder Energiepreisklausel, Beschaffungsgarantie, Fixgeschäft
- Bereits erbrachte Leistungen, Investitionen, Restlaufzeit
- Angestrebtes Ziel: Preisanpassung, Fristverlängerung, Leistungsänderung, Beendigung

## Sub-Agent-Architektur

1. **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) liefert § 313 BGB und die vorrangigen Normen, Kommentarstellen zur Risikoverteilung und — nur soweit belegbar — Rechtsprechung mit Verifikationsmarker.
2. **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) prüft Subsidiarität → reales Element → hypothetisches Element → Zumutbarkeit → Rechtsfolge und entwirft Anpassungsverlangen oder Klauseln.
3. **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft insbesondere, ob vorrangige Rechtsbehelfe übergangen wurden und ob die Anpassung vor der Beendigung geprüft wurde.

## Ablauf

### 1. Subsidiaritätsprüfung — was geht vor?

§ 313 BGB greift **nur**, wenn kein vorrangiges Regime einschlägig ist. Prüfe in dieser Reihenfolge:

| Vorrangig | Wenn |
|---|---|
| **Vertragliche Regelung** | Force-Majeure-Klausel, Preisgleitklausel, Anordnungsrecht § 650b BGB, Rücktrittsvorbehalt — die Parteien haben das Risiko selbst verteilt |
| **Auslegung (§§ 133, 157 BGB)** | Der Vertrag enthält eine planwidrige Lücke, die ergänzend auszulegen ist |
| **Unmöglichkeit § 275 BGB** | Die Leistung ist unmöglich oder nur mit grobem Missverhältnis erbringbar (§ 275 Abs. 2 BGB) |
| **Mängelgewährleistung** | Der Umstand betrifft eine Eigenschaft der Leistung — §§ 434 ff., 633 ff. BGB verdrängen § 313 BGB |
| **Anfechtung §§ 119, 123 BGB** | Der Irrtum betraf die Vorstellung **bei** Vertragsschluss und ist Erklärungs-, Inhalts- oder Eigenschaftsirrtum |
| **Kündigung aus wichtigem Grund** | § 314 BGB bei Dauerschuldverhältnissen, § 648a BGB im Werkvertrag |

**Wer das eigene Beschaffungsrisiko übernommen hat (§ 276 Abs. 1 S. 1 BGB) oder einen Festpreis vereinbart hat, kann sich grundsätzlich nicht auf § 313 BGB berufen** — die Preisgefahr ist dann vertraglich zugewiesen. Das ist der Punkt, an dem die meisten Anpassungsverlangen scheitern.

### 2. Reales Element ([§ 313 Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__313.html))

Umstände, die zur **Grundlage des Vertrags** geworden sind, haben sich **nach Vertragsschluss schwerwiegend verändert**. Geschäftsgrundlage sind die bei Vertragsschluss zutage getretenen, dem anderen Teil erkennbaren und von ihm nicht beanstandeten Vorstellungen einer Partei vom Vorhandensein oder künftigen Eintritt bestimmter Umstände, auf denen der Geschäftswille sich aufbaut.

- Die Veränderung muss **schwerwiegend** sein. Bloße Kostensteigerungen im Rahmen des normalen unternehmerischen Risikos genügen nicht; Preissteigerungen im **niedrigen zweistelligen Prozentbereich** werden in der Kommentarliteratur regelmäßig noch dem Beschaffungsrisiko zugeordnet `[unverifiziert – prüfen]`.
- **Äquivalenzstörung** (Missverhältnis von Leistung und Gegenleistung) und **Zweckstörung** (Verwendungszweck fällt weg) sind die beiden Hauptfälle.
- **Fehlen der Geschäftsgrundlage** von Anfang an (§ 313 Abs. 2 BGB) ist dem gleichgestellt, wenn wesentliche Vorstellungen sich als falsch herausstellen.

### 3. Hypothetisches Element

Die Parteien hätten den Vertrag **nicht oder mit anderem Inhalt geschlossen**, wenn sie diese Veränderung vorausgesehen hätten. Zu prüfen ist der hypothetische Parteiwille beider Seiten — nicht nur des Belasteten. Eine Veränderung, die **vorhersehbar** war und dennoch nicht geregelt wurde, spricht regelmäßig dafür, dass das Risiko der belasteten Partei zugewiesen bleibt.

### 4. Normatives Element — Unzumutbarkeit

Einem Teil ist das **Festhalten am unveränderten Vertrag** unter Berücksichtigung aller Umstände des Einzelfalls, insbesondere der **vertraglichen oder gesetzlichen Risikoverteilung**, **nicht zuzumuten**. Abwägungskriterien:

- Wer trägt nach dem Vertrag das Beschaffungs-, Preis- oder Verwendungsrisiko?
- Existenzgefährdung oder bloße Gewinnschmälerung?
- Restlaufzeit und Möglichkeit, den Nachteil anderweitig auszugleichen?
- Hat die belastete Partei Anstrengungen zur Schadensminderung unternommen (Alternativbeschaffung, Umdisposition)?
- Wurden staatliche Hilfen oder Versicherungsleistungen in Anspruch genommen?

**Praxishinweis:** In den Verfahren zu pandemiebedingten Geschäftsschließungen hat sich durchgesetzt, dass § 313 BGB anwendbar sein kann, aber eine Einzelfallabwägung verlangt und nicht automatisch zu einer hälftigen Teilung führt `[unverifiziert – prüfen]`. Übertragen auf Energie- und Lieferkettenfälle bedeutet das: Es gibt keine Quotenautomatik.

### 5. Rechtsfolge: Anpassung, dann Beendigung ([§ 313 Abs. 3 BGB](https://www.gesetze-im-internet.de/bgb/__313.html))

**Primäre Rechtsfolge ist die Anpassung des Vertrags.** Der Anspruch geht unmittelbar auf die angepasste Leistung — es bedarf keiner Zustimmung der Gegenseite und keiner Gestaltungserklärung; im Prozess ist unmittelbar auf die angepasste Leistung zu klagen.

**Erst wenn eine Anpassung nicht möglich oder einem Teil nicht zumutbar ist**, kann der benachteiligte Teil vom Vertrag **zurücktreten**; an die Stelle des Rücktrittsrechts tritt bei **Dauerschuldverhältnissen** das Recht zur **Kündigung** (§ 313 Abs. 3 S. 2 BGB). Wer sofort kündigt, ohne die Anpassung angeboten zu haben, riskiert eine unwirksame Beendigung und Schadensersatzansprüche der Gegenseite.

**Formulierungshilfe Anpassungsverlangen:**

> „Bei Abschluss des Vertrags vom [Datum] sind beide Parteien von [Umstand, z. B. einem Marktpreis für Erdgas von X EUR/MWh] ausgegangen; dies war erkennbare Grundlage der Preisvereinbarung in Ziff. [N]. Seit [Datum] hat sich dieser Umstand auf [Y] verändert, mithin um [Z] %. Bei Kenntnis dieser Entwicklung hätten die Parteien den Vertrag nicht mit dem vereinbarten Festpreis geschlossen. Das Festhalten am unveränderten Vertrag ist uns unter Berücksichtigung der vertraglichen Risikoverteilung nicht zuzumuten, weil [konkrete Begründung, beziffert]. Wir verlangen daher gemäß **§ 313 Abs. 1 BGB die Anpassung des Vertrags** dahingehend, dass [konkreter Anpassungsvorschlag, beziffert]. Wir bitten um Rückäußerung bis zum [Datum]. Rein vorsorglich weisen wir darauf hin, dass wir bei Nichtzustandekommen einer Anpassung die Rechte aus § 313 Abs. 3 BGB prüfen werden."

### 6. Force Majeure — die vertragliche Alternative

Eine Force-Majeure-Klausel (höhere Gewalt) verlagert den Fall aus der Unsicherheit des § 313 BGB in eine vereinbarte Regelung. Sie ist im deutschen Recht **nicht gesetzlich definiert** — Reichweite und Rechtsfolgen ergeben sich allein aus der Klausel. Regelungsbedürftig sind:

1. **Definition** mit abschließendem oder beispielhaftem Katalog (Naturereignisse, Krieg, Embargo und Sanktionen, hoheitliche Maßnahmen, Epidemien, Streik bei Dritten, Cyberangriff). Klarstellen, ob **Lieferantenausfall** und **Zahlungsunfähigkeit** erfasst sind — im Zweifel sind sie es **nicht**.
2. **Voraussetzungen**: Unvorhersehbarkeit, Unvermeidbarkeit, fehlendes Vertretenmüssen, Kausalität für die Leistungsstörung.
3. **Anzeigepflicht** mit kurzer Frist und Textform; Nachweispflicht.
4. **Rechtsfolge gestuft**: Suspendierung der Leistungspflichten → Verlängerung der Fristen → Neuverhandlungspflicht → Kündigungsrecht nach Ablauf einer Höchstdauer (z. B. 90 Tage).
5. **Schadensminderungspflicht** und Wiederaufnahmepflicht.
6. Klarstellung, dass die **Zahlungspflicht** für bereits erbrachte Leistungen unberührt bleibt.

In AGB unterliegt die Klausel der Kontrolle nach §§ 307 ff. BGB; eine einseitige Befreiung nur des Verwenders benachteiligt unangemessen.

### 7. Preisanpassungs- und Kostenelementeklauseln

Die wirksamste Vorsorge gegen Kostenschocks ist eine **Preisanpassungsklausel**. Zulässigkeitsanforderungen in AGB (§ 307 Abs. 1 S. 2 BGB, Transparenzgebot; vgl. `/vertragsrecht:agb-kontrolle`):

- **Anlass, Maßstab und Umfang** der Anpassung müssen so bestimmt sein, dass die Gegenseite die Erhöhung **selbst nachrechnen** kann.
- **Kostenelementeklausel** als Standardlösung: Sie bindet den Preis an definierte Kostenbestandteile (Material, Energie, Lohn) mit ihrem jeweiligen Gewichtungsanteil und einem **objektiven, öffentlich zugänglichen Index** (z. B. Erzeugerpreisindizes des Statistischen Bundesamts). Kostensenkungen müssen **zwingend gleichermaßen weitergegeben** werden — eine nur nach oben wirkende Klausel ist unwirksam.
- **Keine Gewinnmargenerhöhung**: Die Klausel darf nur Kostensteigerungen ausgleichen, nicht die Marge verbessern.
- Bei Verbrauchern zusätzlich **Lösungsrecht** ab einer Erheblichkeitsschwelle vorsehen.

**Klauselbaustein Kostenelementeklausel (B2B):**

> „(1) Der vereinbarte Nettopreis setzt sich zusammen aus Materialkosten (Anteil 55 %), Energiekosten (15 %), Lohnkosten (20 %) und einem festen Anteil (10 %). (2) Verändert sich einer der in Absatz 1 genannten Kostenbestandteile gegenüber dem Stand bei Vertragsschluss um mehr als 5 %, gemessen am [konkret bezeichneter Index des Statistischen Bundesamts, Basisjahr], so ändert sich der Preis entsprechend dem jeweiligen Gewichtungsanteil. (3) Absatz 2 gilt für Kostensenkungen in gleicher Weise; der Verwender ist zur Weitergabe von Kostensenkungen **verpflichtet**. (4) Die Anpassung ist in Textform unter Angabe der Berechnung mitzuteilen und wirkt frühestens einen Monat nach Zugang."

## Quellen

### Statute

- [§ 313 BGB](https://www.gesetze-im-internet.de/bgb/__313.html) (Störung der Geschäftsgrundlage)
- [§ 314 BGB](https://www.gesetze-im-internet.de/bgb/__314.html) (Kündigung von Dauerschuldverhältnissen aus wichtigem Grund)
- [§ 275 BGB](https://www.gesetze-im-internet.de/bgb/__275.html), [§ 326 BGB](https://www.gesetze-im-internet.de/bgb/__326.html)
- [§ 307 BGB](https://www.gesetze-im-internet.de/bgb/__307.html) (Transparenzgebot bei Preisanpassungsklauseln), [§ 308 BGB](https://www.gesetze-im-internet.de/bgb/__308.html) Nr. 4
- [§ 315 BGB](https://www.gesetze-im-internet.de/bgb/__315.html) (Leistungsbestimmung nach billigem Ermessen), [§ 242 BGB](https://www.gesetze-im-internet.de/bgb/__242.html)

### Kommentare

- Grüneberg, BGB, 83. Aufl. 2024, § 313 Rn. 1 ff. `[unverifiziert – Auflagenstand prüfen]`
- Finkenauer, in: MüKoBGB, 9. Aufl. 2022, § 313 Rn. 1 ff.
- Wurmnest, in: MüKoBGB, 9. Aufl. 2022, § 307 Rn. 1 ff. (Preisanpassungsklauseln)

### Rechtsprechung

- BGH, Urt. v. 12.01.2022 – XII ZR 8/21 (Gewerberaummiete bei pandemiebedingter Geschäftsschließung, § 313 BGB anwendbar, Einzelfallabwägung, keine Quotenautomatik) `[unverifiziert – prüfen]`
- BGH, Urt. v. 18.07.2012 – VIII ZR 337/11 (Anforderungen an Preisanpassungsklauseln) `[unverifiziert – prüfen]`

> Beide Aktenzeichen vor Verwendung in juris / Beck-Online prüfen. Die Prozentschwellen dieses Skills sind Orientierungswerte aus der Kommentarliteratur, keine festen Grenzen.

## Ausgabeformat

```
STÖRUNG DER GESCHÄFTSGRUNDLAGE — <Vertrag> — <Datum>

I.    Subsidiaritätsprüfung           [🔴 vorrangig: <Klausel / § 275 / Gewährleistung / § 314>
                                       / ✅ § 313 eröffnet]
II.   Reales Element                  [schwerwiegende Veränderung ✅/❌ — Ausmaß: <…> %]
        Art:                          [Äquivalenzstörung / Zweckstörung / § 313 II]
III.  Hypothetisches Element          [✅ / ❌ — Vorhersehbarkeit bei Vertragsschluss]
IV.   Zumutbarkeit                    [unzumutbar ✅ / zumutbar ❌]
        Vertragliche Risikoverteilung: <Festpreis / Gleitpreis / Beschaffungsgarantie>
V.    Rechtsfolge                     [Anpassung § 313 I — Vorschlag: <beziffert>]
        Beendigung § 313 III:         [erst nachrangig — Rücktritt / Kündigung]
VI.   Vertragliche Alternative        [Force-Majeure-Klausel / Preisanpassungsklausel — Entwurf beigefügt]

Anpassungsverlangen versandt am:      <Datum> / Entwurf beigefügt
Gesamtbefund: [🟢 / 🟡 / 🔴]
Offene Tatsachen: <Liste>
```

## Risiken / typische Fehler

- **Subsidiarität übersehen** — § 313 BGB ist gesperrt, soweit die Parteien das Risiko vertraglich verteilt haben oder Gewährleistungs-, Unmöglichkeits- oder Kündigungsrecht eingreift.
- **Sofort gekündigt statt Anpassung verlangt** — § 313 Abs. 3 BGB gestattet die Beendigung nur, wenn eine Anpassung unmöglich oder unzumutbar ist; die vorschnelle Kündigung ist unwirksam und begründet eigene Haftung.
- **Festpreisvereinbarung ignoriert** — wer einen Festpreis oder eine Beschaffungsgarantie vereinbart hat, trägt das Preisrisiko und dringt mit § 313 BGB regelmäßig nicht durch.
- **Vorhersehbare Entwicklung als Störung deklariert** — war die Veränderung bei Vertragsschluss absehbar und wurde nicht geregelt, bleibt das Risiko bei der belasteten Partei.
- **Force-Majeure-Klausel ohne Lieferantenausfall** — der praktisch wichtigste Fall ist im Zweifel gerade nicht erfasst; er muss ausdrücklich benannt werden.
- **Preisanpassungsklausel nur nach oben** — eine Klausel, die Kostensenkungen nicht zwingend weitergibt, ist nach § 307 BGB unwirksam und fällt ersatzlos weg.
