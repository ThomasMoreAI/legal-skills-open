---
name: vereinsgruendung-satzung-borghei
title: /vereins-stiftungs-gemeinnuetzigkeitsrecht:vereinsgruendung-satzung
description: Gründung des eingetragenen Vereins und Gestaltung der Satzung – Abgrenzung Idealverein § 21 BGB zum wirtschaftlichen Verein § 22 BGB einschließlich Nebenzweckprivileg, Mindest- und Sollinhalt der Satzung §§ 57, 58 BGB, Mindestmitgliederzahl § 56 BGB, Anmeldung zum Vereinsregister §§ 59, 60 BGB in öffentlich beglaubigter Form § 77 BGB, Vorstand und Vertretungsmacht § 26 BGB, besonderer Vertreter § 30 BGB, Mitgliederversammlung §§ 32, 36, 37 BGB mit hybrider und virtueller Versammlung, Beschlussmängel, Satzungsänderung §§ 33, 71 BGB sowie die Haftungsprivilegien §§ 31a, 31b BGB. Use when ein Verein gegründet, eine Satzung entworfen oder geändert, eine Registeranmeldung vorbereitet oder ein Vereinsbeschluss auf Mängel geprüft werden soll.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/vereins-stiftungs-gemeinnuetzigkeitsrecht/skills/vereinsgruendung-satzung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: general
language: de
---

# /vereins-stiftungs-gemeinnuetzigkeitsrecht:vereinsgruendung-satzung

## Zweck

Rund 615.000 eingetragene Vereine machen das Vereinsrecht zum meistgenutzten Organisationsrecht Deutschlands — und zum am häufigsten fehlerhaft angewandten. Dieser Skill baut die Satzung so, dass sie **registerfest** ist, führt die Anmeldung durch §§ 59, 77 BGB und prüft Beschlüsse auf Mängel. Soll der Verein gemeinnützig sein, ist die Satzung zusätzlich gegen `/vereins-stiftungs-gemeinnuetzigkeitsrecht:gemeinnuetzigkeit-ao` zu spiegeln.

## Eingaben

- Zweck des Vereins in eigenen Worten und die geplanten Tätigkeiten zur Zweckverwirklichung
- Geplante wirtschaftliche Aktivitäten: Art, geschätzter Umfang, Verhältnis zum Idealzweck
- Zahl der Gründungsmitglieder (mindestens sieben, § 56 BGB), Name und Sitz
- Gewünschte Organstruktur: Vorstandsgröße, Vertretungsregelung, weitere Organe, Beirat, Abteilungen
- Soll Gemeinnützigkeit angestrebt werden? Dann Mustersatzung Anlage 1 zu § 60 AO zwingend mitdenken
- Bei Änderung: geltende Satzungsfassung, Beschlussprotokoll, Registerstand
- Bei Beschlussstreit: Einladung, Tagesordnung, Teilnehmerliste, Abstimmungsergebnis, Protokoll

## Sub-Agent-Architektur

1. **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) liefert §§ 21–79 BGB, die Registerpraxis zur Eintragungsfähigkeit und Kommentarstellen zum Nebenzweckprivileg.
2. **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) entwirft Satzung, Gründungsprotokoll und Registeranmeldung und formuliert Änderungsbeschlüsse.
3. **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft Mindestinhalt, Form der Anmeldung, Widerspruchsfreiheit zwischen Satzung und Mustersatzung und die Einhaltung der Einladungsregeln.

## Ablauf

### 1. Idealverein oder wirtschaftlicher Verein ([§ 21 BGB](https://www.gesetze-im-internet.de/bgb/__21.html), [§ 22 BGB](https://www.gesetze-im-internet.de/bgb/__22.html))

- **§ 21 BGB:** Ein Verein, dessen Zweck **nicht** auf einen wirtschaftlichen Geschäftsbetrieb gerichtet ist, erlangt Rechtsfähigkeit durch **Eintragung** in das Vereinsregister des zuständigen Amtsgerichts.
- **§ 22 BGB:** Ein Verein mit wirtschaftlichem Zweck erlangt Rechtsfähigkeit — mangels besonderer bundesgesetzlicher Vorschriften — nur durch **staatliche Verleihung** durch das Sitzland. Das ist ein Ausnahmeweg; die Verleihung wird nur erteilt, wenn dem Verein die Nutzung der handelsrechtlichen Rechtsformen (GmbH, Genossenschaft) unzumutbar ist.

**Nebenzweckprivileg.** Entscheidend ist der **Hauptzweck**, nicht jede Betätigung. Ein Idealverein darf einen wirtschaftlichen Geschäftsbetrieb unterhalten, solange dieser dem ideellen Hauptzweck **untergeordnet** ist und ihm **dient** — Vereinsgaststätte, Bandenwerbung, Trikotsponsoring, Merchandising, Vereinsfeste. Die Grenze ist überschritten, wenn der Geschäftsbetrieb nach Umfang und Bedeutung das Bild des Vereins prägt und der ideelle Zweck zur Hülle wird. Registergerichte prüfen das bei der Eintragung und können nach § 60 BGB zurückweisen; bei nachträglichem Umschlagen droht die Amtslöschung.

> **Praxishinweis:** Wächst der Geschäftsbetrieb, ist die Ausgliederung in eine Tochtergesellschaft (typisch: gemeinnützige GmbH) der saubere Weg — sie schützt zugleich die Gemeinnützigkeit des Vereins und begrenzt die Haftung.

### 2. Satzungsinhalt ([§ 57 BGB](https://www.gesetze-im-internet.de/bgb/__57.html), [§ 58 BGB](https://www.gesetze-im-internet.de/bgb/__58.html))

**Mindestinhalt (§ 57 Abs. 1 BGB) — ohne ihn keine Eintragung:**

1. **Zweck** des Vereins
2. **Name** des Vereins — er soll sich nach § 57 Abs. 2 BGB von den Namen der am selben Ort bestehenden eingetragenen Vereine deutlich unterscheiden
3. **Sitz** des Vereins
4. die Angabe, dass der Verein **eingetragen werden soll**

**Sollinhalt (§ 58 BGB) — in der Praxis ebenfalls zwingend, weil das Registergericht sonst beanstandet:**

1. Eintritt und Austritt der Mitglieder
2. ob und welche **Beiträge** zu leisten sind
3. Bildung des **Vorstands**
4. Voraussetzungen der **Einberufung** der Mitgliederversammlung, **Form der Berufung** und **Beurkundung der Beschlüsse**

**Satzungsbausteine (Gerüst):** § 1 Name, Sitz, Geschäftsjahr — § 2 Zweck und Art der Zweckverwirklichung — § 3 Gemeinnützigkeit (Bausteine nach Anlage 1 zu § 60 AO, falls angestrebt) — § 4 Erwerb der Mitgliedschaft — § 5 Beendigung der Mitgliedschaft (Austritt, Ausschluss mit rechtlichem Gehör und Rechtsbehelf zur Mitgliederversammlung, Streichung) — § 6 Beiträge — § 7 Organe — § 8 Vorstand: Zusammensetzung, Bestellung, Amtsdauer, **Vertretungsmacht**, Beschlussfassung — § 9 Mitgliederversammlung: Einberufungsfrist und -form, Tagesordnung, Beschlussfähigkeit, Mehrheiten, Protokoll — § 10 Satzungsänderung und Zweckänderung — § 11 Auflösung und Vermögensanfall.

### 3. Vorstand und Vertretungsmacht ([§ 26 BGB](https://www.gesetze-im-internet.de/bgb/__26.html), [§ 30 BGB](https://www.gesetze-im-internet.de/bgb/__30.html))

Der Verein **muss** einen Vorstand haben; dieser vertritt ihn gerichtlich und außergerichtlich und hat die Stellung eines **gesetzlichen Vertreters** (§ 26 Abs. 1 BGB). Besteht der Vorstand aus mehreren Personen, vertritt nach § 26 Abs. 2 S. 1 BGB die **Mehrheit** der Vorstandsmitglieder — eine Regel, die fast nie gewollt ist und daher in der Satzung ersetzt gehört:

> „Der Vorstand im Sinne des § 26 BGB besteht aus [dem/der Vorsitzenden, dem/der stellvertretenden Vorsitzenden und dem/der Schatzmeister/in]. **Je zwei Vorstandsmitglieder vertreten den Verein gemeinsam.** Der Umfang der Vertretungsmacht ist mit Wirkung gegen Dritte dahin beschränkt, dass für Rechtsgeschäfte mit einem Gegenstandswert von mehr als EUR [Betrag] die vorherige Zustimmung der Mitgliederversammlung erforderlich ist."

Die Beschränkung der Vertretungsmacht wirkt nach § 26 Abs. 1 S. 3 BGB **gegen Dritte nur, wenn sie in der Satzung steht** und eingetragen ist — eine bloße Geschäftsordnung genügt nicht. **Besondere Vertreter** nach § 30 BGB können für abgegrenzte Geschäftskreise (Abteilungsleitung, Geschäftsstelle) satzungsmäßig bestellt werden; ihre Vertretungsmacht erstreckt sich im Zweifel auf alle Geschäfte, die der zugewiesene Geschäftskreis gewöhnlich mit sich bringt. Jede Vorstandsänderung ist nach § 67 BGB zur Eintragung anzumelden.

### 4. Mitgliederversammlung und Beschlussmängel ([§ 32 BGB](https://www.gesetze-im-internet.de/bgb/__32.html), [§ 36 BGB](https://www.gesetze-im-internet.de/bgb/__36.html), [§ 37 BGB](https://www.gesetze-im-internet.de/bgb/__37.html))

- **§ 32 Abs. 1 BGB:** Die Angelegenheiten des Vereins werden durch Beschluss in der Mitgliederversammlung geordnet. Zur Gültigkeit ist erforderlich, dass der **Gegenstand bei der Berufung bezeichnet** wird; es entscheidet die **Mehrheit der abgegebenen Stimmen**.
- **§ 32 Abs. 2 BGB:** Bei der Berufung kann eine **hybride Versammlung** vorgesehen werden; die Mitglieder können beschließen, dass künftige Versammlungen auch als **virtuelle Versammlungen** einberufen werden können. In der Berufung ist anzugeben, wie die Rechte elektronisch ausgeübt werden.
- **§ 32 Abs. 3 BGB:** Ohne Versammlung ist ein Beschluss gültig, wenn **alle** Mitglieder in **Textform** zustimmen.
- **§ 36 BGB:** Einberufung in den satzungsmäßig bestimmten Fällen und wenn das Vereinsinteresse es erfordert.
- **§ 37 BGB — Minderheitenrecht:** Auf Verlangen des satzungsmäßig bestimmten Teils, mangels Bestimmung des **zehnten Teils** der Mitglieder, schriftlich unter Angabe von Zweck und Gründen. Wird dem nicht entsprochen, kann das Amtsgericht die Antragsteller zur Berufung ermächtigen.

**Beschlussmängel:** Das Vereinsrecht kennt **kein** dem Aktienrecht entsprechendes Anfechtungssystem. Fehlerhafte Beschlüsse sind grundsätzlich **nichtig**; der Mangel wird durch **Feststellungsklage nach § 256 ZPO** geltend gemacht — ohne gesetzliche Frist, aber begrenzt durch Verwirkung. Typische Mängel: Ladungsfrist oder Ladungsform verfehlt, **Tagesordnungspunkt nicht angekündigt** (§ 32 Abs. 1 S. 2 BGB), Nichtmitglieder mitgestimmt, Stimmverbot bei Interessenkonflikt (§ 34 BGB) missachtet, falsche Mehrheit angewandt. Ein Satzungsbeschluss, der ohne Ankündigung gefasst wird, ist unwirksam — auch wenn alle Anwesenden zustimmen.

Die Berechnung der Ladungs- und Rechtsbehelfsfristen übernimmt der deterministische Rechner:

```bash
python -m scripts.legal_calc.cli frist --ereignis 15.01.2026 --menge 1 --einheit monate --land BY
```

Er leistet **ausschließlich** die Arithmetik der §§ 187–193 BGB. **Fristbeginn und Zugang bleiben rechtliche Eingaben** — ob die Einladung ordnungsgemäß und wem sie wann zugegangen ist, bewertet der Bearbeiter.

### 5. Satzungsänderung ([§ 33 BGB](https://www.gesetze-im-internet.de/bgb/__33.html), [§ 71 BGB](https://www.gesetze-im-internet.de/bgb/__71.html))

- **§ 33 Abs. 1 S. 1 BGB:** Satzungsänderung mit **Dreiviertelmehrheit der abgegebenen Stimmen**.
- **§ 33 Abs. 1 S. 2 BGB:** Zur **Zweckänderung** ist die Zustimmung **aller Mitglieder** erforderlich; die Zustimmung der nicht Erschienenen muss in **Textform** erfolgen. Die Satzung kann davon nicht wirksam nach unten abweichen, soweit es um den Zweck im engeren Sinne geht `[unverifiziert - prüfen]`.
- **§ 71 Abs. 1 BGB:** Die Änderung wird erst mit **Eintragung** wirksam. Der Anmeldung sind eine Abschrift des Beschlusses **und der vollständige Wortlaut** der Satzung beizufügen; der Wortlaut muss mit dem Beschluss und den zuletzt eingereichten Fassungen übereinstimmen.

Bei gemeinnützigen Vereinen ist **jede** Satzungsänderung vor dem Beschluss mit dem Finanzamt abzustimmen und nach der Eintragung dorthin zu übersenden — sonst droht der Verlust der Feststellung nach § 60a AO.

### 6. Anmeldung zum Vereinsregister ([§ 59 BGB](https://www.gesetze-im-internet.de/bgb/__59.html), [§ 60 BGB](https://www.gesetze-im-internet.de/bgb/__60.html), [§ 77 BGB](https://www.gesetze-im-internet.de/bgb/__77.html))

1. **§ 56 BGB:** Die Eintragung soll nur erfolgen, wenn die Mitgliederzahl **mindestens sieben** beträgt.
2. **§ 59 BGB:** Der **Vorstand** meldet den Verein zur Eintragung an. Beizufügen sind Abschriften der Satzung und der Urkunden über die Bestellung des Vorstands. Die Satzung soll von mindestens **sieben Mitgliedern unterzeichnet** sein und den **Tag der Errichtung** enthalten.
3. **§ 77 Abs. 1 BGB:** Die Anmeldung ist von Vorstandsmitgliedern **mittels öffentlich beglaubigter Erklärung** abzugeben — also mit notarieller Unterschriftsbeglaubigung, nicht privatschriftlich. Nach § 77 Abs. 2 BGB ist die öffentliche Beglaubigung **mittels Videokommunikation** nach § 40a BeurkG zulässig.
4. **§ 60 BGB:** Genügt die Anmeldung den Erfordernissen der §§ 56 bis 59 BGB nicht, weist das Amtsgericht sie **unter Angabe der Gründe** zurück.
5. Nach § 64 BGB werden Name, Sitz, Tag der Errichtung der Satzung sowie die Vorstandsmitglieder und ihre Vertretungsmacht eingetragen. § 78 BGB erlaubt Zwangsgeld gegen Vorstandsmitglieder, die Anmeldepflichten (§§ 67, 71, 74, 76 BGB) verletzen.

### 7. Haftungsprivilegien ([§ 31a BGB](https://www.gesetze-im-internet.de/bgb/__31a.html), [§ 31b BGB](https://www.gesetze-im-internet.de/bgb/__31b.html))

- **§ 31a Abs. 1 BGB:** Organmitglieder und besondere Vertreter, die **unentgeltlich** tätig sind oder eine Vergütung von **nicht mehr als 3.300 Euro jährlich** erhalten, haften dem Verein und den Mitgliedern nur für **Vorsatz und grobe Fahrlässigkeit**. Die **Beweislast** für Vorsatz oder grobe Fahrlässigkeit trägt der Verein bzw. das Mitglied.
- **§ 31a Abs. 2 BGB:** Gegenüber Dritten haften sie zwar nach allgemeinen Regeln, können aber vom Verein **Freistellung** verlangen — außer bei Vorsatz und grober Fahrlässigkeit.
- **§ 31b BGB** überträgt beides auf **Vereinsmitglieder**, die satzungsgemäße Aufgaben wahrnehmen.
- Nach § 31 BGB haftet der Verein für Schäden, die der Vorstand oder ein anderer verfassungsmäßig berufener Vertreter in Ausführung der ihm zustehenden Verrichtungen einem Dritten zufügt.

**Nicht privilegiert** sind die steuerlichen und sozialversicherungsrechtlichen Vertreterhaftungen: § 69 AO in Verbindung mit § 34 AO (nicht abgeführte Lohn- und Umsatzsteuer) und § 823 Abs. 2 BGB in Verbindung mit § 266a StGB (vorenthaltene Arbeitnehmerbeiträge) greifen unabhängig von §§ 31a, 31b BGB. Eine Vereins-D&O-Versicherung ist bei nennenswertem Vermögen oder Personal dringend zu empfehlen.

## Quellen

### Statute

- [§ 21 BGB](https://www.gesetze-im-internet.de/bgb/__21.html), [§ 22 BGB](https://www.gesetze-im-internet.de/bgb/__22.html) (Idealverein, wirtschaftlicher Verein)
- [§ 26 BGB](https://www.gesetze-im-internet.de/bgb/__26.html), [§ 30 BGB](https://www.gesetze-im-internet.de/bgb/__30.html), [§ 31 BGB](https://www.gesetze-im-internet.de/bgb/__31.html)
- [§ 31a BGB](https://www.gesetze-im-internet.de/bgb/__31a.html), [§ 31b BGB](https://www.gesetze-im-internet.de/bgb/__31b.html) (Haftungsprivilegien)
- [§ 32 BGB](https://www.gesetze-im-internet.de/bgb/__32.html), [§ 33 BGB](https://www.gesetze-im-internet.de/bgb/__33.html), [§ 36 BGB](https://www.gesetze-im-internet.de/bgb/__36.html), [§ 37 BGB](https://www.gesetze-im-internet.de/bgb/__37.html), [§ 41 BGB](https://www.gesetze-im-internet.de/bgb/__41.html)
- [§ 56 BGB](https://www.gesetze-im-internet.de/bgb/__56.html), [§ 57 BGB](https://www.gesetze-im-internet.de/bgb/__57.html), [§ 58 BGB](https://www.gesetze-im-internet.de/bgb/__58.html), [§ 59 BGB](https://www.gesetze-im-internet.de/bgb/__59.html), [§ 60 BGB](https://www.gesetze-im-internet.de/bgb/__60.html), [§ 64 BGB](https://www.gesetze-im-internet.de/bgb/__64.html)
- [§ 67 BGB](https://www.gesetze-im-internet.de/bgb/__67.html), [§ 71 BGB](https://www.gesetze-im-internet.de/bgb/__71.html), [§ 77 BGB](https://www.gesetze-im-internet.de/bgb/__77.html), [§ 78 BGB](https://www.gesetze-im-internet.de/bgb/__78.html)
- [§ 69 AO](https://www.gesetze-im-internet.de/ao_1977/__69.html), [§ 266a StGB](https://www.gesetze-im-internet.de/stgb/__266a.html), [§ 256 ZPO](https://www.gesetze-im-internet.de/zpo/__256.html)

### Kommentare

- Leuschner, in: MüKoBGB, 9. Aufl. 2021, § 21 Rn. 1 ff. (Nebenzweckprivileg), § 26 Rn. 1 ff. `[unverifiziert - Auflagenstand prüfen]`
- Ellenberger, in: Grüneberg, BGB, 83. Aufl. 2024, §§ 21–79 `[unverifiziert - Auflagenstand prüfen]`
- Sauter/Schweyer/Waldner, Der eingetragene Verein, 21. Aufl. 2021 `[unverifiziert - Auflagenstand prüfen]`

### Rechtsprechung

- BGH, Beschl. v. 16.05.2017 – II ZB 7/16 (Nebenzweckprivileg, Eintragungsfähigkeit von Kita-Trägervereinen) `[unverifiziert - prüfen]`

> Aktenzeichen vor Verwendung in juris / Beck-Online prüfen. Die tragenden Aussagen dieses Skills folgen unmittelbar aus dem Wortlaut der §§ 21–79 BGB.

## Ausgabeformat

```
VEREIN — <Name> — <Datum>

I.    Typzuordnung                  [Idealverein § 21 BGB / wirtschaftlicher Verein § 22 BGB]
        Nebenzweckprivileg:         [gewahrt ✅ / 🔴 Geschäftsbetrieb prägend — <…>]
II.   Satzung
        Mindestinhalt § 57:         Zweck [✅] Name [✅] Sitz [✅] Eintragungswille [✅]
        Sollinhalt § 58:            Ein-/Austritt [ ] Beiträge [ ] Vorstand [ ] Einberufung [ ]
        Gemeinnützigkeit:           [angestrebt — Anlage 1 zu § 60 AO eingearbeitet ✅/❌]
III.  Vorstand § 26                 Zusammensetzung: <…>
        Vertretungsregelung:        [Einzel / Je zwei gemeinsam / gesetzl. Mehrheit]
        Beschränkung Abs. 1 S. 3:   [in Satzung ✅ / nur Geschäftsordnung 🔴]
        Besondere Vertreter § 30:   [ja — Geschäftskreis: <…> / nein]
IV.   Mitgliederversammlung         Ladungsfrist: <…>  Form: <…>
        Hybrid/virtuell § 32 II:    [vorgesehen / nein]
        Beschlussfassung:           <Mehrheiten>
V.    Satzungsänderung              § 33 Abs. 1 S. 1: [3/4 der abgegebenen Stimmen]
        Zweckänderung:              [Zustimmung aller Mitglieder erforderlich]
        Wirksamkeit § 71:           [erst mit Eintragung — angemeldet am <…>]
VI.   Registeranmeldung             Mitgliederzahl § 56: <…>
        Form § 77:                  [öffentlich beglaubigt ✅ / 🔴 privatschriftlich]
        Anlagen § 59 Abs. 2:        [Satzung / Bestellungsurkunden]
VII.  Beschlussmängel               [keine / Mangel: <…> — Feststellungsklage § 256 ZPO]
VIII. Haftung                       §§ 31a, 31b BGB: [privilegiert — Vergütung ≤ 3.300 EUR ✅/❌]
        Nicht privilegiert:         [§ 69 AO / § 266a StGB]  D&O: [vorhanden / empfohlen]

Gesamtbefund: [🟢 / 🟡 / 🔴]
Offene Punkte: <Liste>
```

## Risiken / typische Fehler

- **Wirtschaftlicher Geschäftsbetrieb prägt den Verein** — das Nebenzweckprivileg trägt nicht mehr; es drohen Zurückweisung der Anmeldung nach § 60 BGB oder Amtslöschung. Ausgliederung in eine Tochtergesellschaft prüfen.
- **Vertretungsregelung nur in der Geschäftsordnung** — eine Beschränkung der Vertretungsmacht wirkt nach § 26 Abs. 1 S. 3 BGB gegen Dritte nur, wenn sie in der Satzung steht und eingetragen ist.
- **Anmeldung privatschriftlich eingereicht** — § 77 BGB verlangt öffentlich beglaubigte Erklärung; die Beglaubigung per Videokommunikation nach § 40a BeurkG ist zulässig.
- **Tagesordnungspunkt nicht angekündigt** — der Beschluss ist nach § 32 Abs. 1 S. 2 BGB unwirksam, auch bei einstimmiger Annahme durch die Anwesenden.
- **Zweckänderung mit Dreiviertelmehrheit beschlossen** — § 33 Abs. 1 S. 2 BGB verlangt die Zustimmung **aller** Mitglieder, die der Abwesenden in Textform.
- **Satzungsänderung vor Eintragung angewandt** — sie wird nach § 71 Abs. 1 BGB erst mit der Eintragung wirksam; darauf gestützte Beschlüsse sind fehlerhaft.
- **Satzungsänderung ohne Abstimmung mit dem Finanzamt** — bei gemeinnützigen Vereinen droht der Verlust der Feststellung nach § 60a AO.
- **Auf §§ 31a, 31b BGB als Rundumschutz vertraut** — § 69 AO und § 266a StGB greifen unabhängig davon; nicht abgeführte Lohnsteuer und Sozialbeiträge treffen den Vorstand persönlich.
