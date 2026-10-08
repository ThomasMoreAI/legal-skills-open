---
name: asset-deal-betriebsuebergang-borghei
title: /m-a-transaktionsrecht:asset-deal-betriebsuebergang
description: Strukturierung des Asset Deals (Unternehmenskauf durch Einzelrechtsnachfolge) – sachenrechtlicher Bestimmtheitsgrundsatz bei der Übertragung des Assetkreises, Vertragsübernahme nur mit Zustimmung des Vertragspartners, Betriebsübergang § 613a BGB als zwingende Rechtsfolge, Firmenfortführungshaftung § 25 Abs. 1 HGB mit dem Enthaftungsvermerk § 25 Abs. 2 HGB, Betriebsübernehmerhaftung § 75 AO, Geschäftsveräußerung im Ganzen § 1 Abs. 1a UStG und Grunderwerbsteuer bei Grundstücken im Assetkreis. Use when zwischen Share Deal und Asset Deal entschieden, ein Asset-Kaufvertrag entworfen oder die Haftungs- und Steuerfolgen einer Betriebsübernahme geprüft werden sollen.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/m-a-transaktionsrecht/skills/asset-deal-betriebsuebergang
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: corporate
language: de
---

# /m-a-transaktionsrecht:asset-deal-betriebsuebergang

## Zweck

Der Asset Deal überträgt das Unternehmen als Summe einzelner Vermögensgegenstände. Er erlaubt die gezielte Auswahl dessen, was übergeht — und produziert genau daraus seine typischen Fehler: vergessene Gegenstände, unwirksame Vertragsübernahmen und Haftungstatbestände, die unabhängig vom Parteiwillen eingreifen. Dieser Skill baut den Assetkreis, sichert die Übertragung und arbeitet die **gesetzlich zwingenden Haftungsfolgen** ab.

## Eingaben

- Zielobjekt: Betrieb, Betriebsteil oder einzelne Vermögensgegenstände; Verkäufer und dessen Rechtsform
- Motiv für den Asset Deal: Verlustvorträge, Altlastenabschneidung, Erwerb aus der Insolvenz, steuerliche Abschreibungsbasis (Step-up)
- Assetliste: Sachanlagen, Vorräte, Forderungen, Schutzrechte, Software, Domains, Kundenstamm, Verträge
- Grundstücke im Assetkreis? Eigentum oder Miete/Pacht?
- Arbeitnehmerbestand, Betriebsrat, Tarifbindung
- Firmenfortführung geplant? Bisherige Firma, Registerstand
- Steuerhistorie und offene Betriebssteuern; Insolvenznähe des Verkäufers

## Sub-Agent-Architektur

1. **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) liefert §§ 25, 27 HGB, § 613a BGB, § 75 AO, § 1 Abs. 1a UStG und die Kommentarliteratur zum Bestimmtheitsgrundsatz.
2. **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) entwirft Assetliste, Übertragungsklauseln, Vertragsübernahmemechanik und Haftungsfreistellungen.
3. **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft die Bestimmtheit jeder Übertragung, die Zustimmungslage bei Verträgen, den Enthaftungsvermerk und die Vollständigkeit der Steuerklauseln.

## Ablauf

### 1. Strukturentscheidung Share Deal oder Asset Deal

| Kriterium | Share Deal | Asset Deal |
|---|---|---|
| **Übertragung** | Ein Rechtsgeschäft über die Anteile | Einzelrechtsnachfolge je Gegenstand |
| **Verträge** | laufen unverändert weiter (Change-of-Control beachten) | nur mit Zustimmung des Vertragspartners |
| **Altverbindlichkeiten** | bleiben in der Gesellschaft | bleiben grundsätzlich beim Verkäufer — **aber** §§ 25 HGB, 75 AO, 613a BGB |
| **Form** | notariell (§ 15 Abs. 3, 4 GmbHG) | formfrei, **es sei denn** Grundstück (§ 311b BGB) oder GmbH-Anteil im Assetkreis |
| **Steuerlich** | keine Abschreibungsbasis beim Käufer | Step-up auf die erworbenen Wirtschaftsgüter |
| **Aufwand** | gering im Vollzug | hoch: Inventarisierung, Zustimmungen, Umschreibungen |

**Formfalle:** Enthält der Assetkreis ein Grundstück, ist der **gesamte** Asset-Kaufvertrag nach § 311b Abs. 1 BGB beurkundungsbedürftig. Gleiches gilt bei einem GmbH-Geschäftsanteil im Assetkreis (§ 15 Abs. 3, 4 GmbHG).

### 2. Bestimmtheitsgrundsatz und Übertragungstechnik

Die Übertragung erfolgt für jeden Gegenstand nach den für ihn geltenden Regeln: bewegliche Sachen nach §§ 929 ff. BGB, Forderungen durch Abtretung nach § 398 BGB, Grundstücke durch Auflassung und Eintragung nach §§ 873, 925 BGB, Schutzrechte nach den jeweiligen Sondergesetzen mit Registerumschreibung.

Sachenrechtlich gilt der **Bestimmtheitsgrundsatz**: Jeder übertragene Gegenstand muss im Zeitpunkt der Übertragung für einen Dritten **eindeutig identifizierbar** sein. Eine Klausel „sämtliches Anlagevermögen" genügt nur, wenn eine Anlage die Gegenstände abschließend auflistet oder ein objektives Abgrenzungskriterium (räumlich: „alle in der Halle B befindlichen Maschinen"; buchhalterisch: „alle im Anlagenverzeichnis Anlage 3.1 mit Stand [Datum] geführten Gegenstände") die Bestimmbarkeit sichert. Bei Vorräten wird zusätzlich das Übergabesurrogat gewählt (§ 930 BGB Besitzkonstitut, § 931 BGB Abtretung des Herausgabeanspruchs bei Lagerung beim Dritten).

**Auffangklausel** — hilfreich, aber kein Ersatz für die Liste:

> „Übertragen werden ferner alle sonstigen Gegenstände, die dem Betrieb [Bezeichnung] am Stichtag dienen und in den Anlagen [N] nicht ausdrücklich als zurückbehalten aufgeführt sind, soweit sie dem Käufer nach dem Vertragszweck zustehen sollen. Der Verkäufer ist verpflichtet, an der Übertragung nachträglich festgestellter Gegenstände mitzuwirken (Nachübertragungspflicht)."

Zu prüfen: **Eigentumsvorbehalte** und Sicherungsübereignungen an Vorräten und Maschinen, **Globalzession** von Forderungen zugunsten der Hausbank, Leasing- statt Eigentumsposition, Lizenz- statt Inhaberschaft an Software.

### 3. Vertragsübernahme

Verträge gehen **nicht automatisch** über. Die dreiseitige Vertragsübernahme setzt die **Zustimmung des Vertragspartners** voraus (§§ 414, 415 BGB analog); ohne sie bleibt der Verkäufer Vertragspartei. Praktisch:

1. **Konsentliste** erstellen und nach Wesentlichkeit priorisieren; die wichtigsten Zustimmungen werden **Closing-Bedingung**.
2. **Innenverhältnis-Lösung** als Rückfallebene, wo die Zustimmung nicht rechtzeitig zu erlangen ist: Der Verkäufer hält den Vertrag im Außenverhältnis, der Käufer trägt wirtschaftlich Chancen und Lasten und stellt frei. Nur Übergangslösung — sie hilft nicht bei personenbezogenen Genehmigungen.
3. **Öffentlich-rechtliche Genehmigungen** sind regelmäßig anlagen- oder personenbezogen und nicht übertragbar; Neubeantragung einplanen.
4. **Dauerschuldverhältnisse** mit Kündigungsrecht bei Betriebsübergang prüfen (Miete, Leasing, Lizenz).

### 4. Betriebsübergang ([§ 613a BGB](https://www.gesetze-im-internet.de/bgb/__613a.html))

Geht ein **Betrieb oder Betriebsteil** durch Rechtsgeschäft auf einen anderen Inhaber über, tritt der Erwerber **kraft Gesetzes** in die Rechte und Pflichten der bestehenden Arbeitsverhältnisse ein. Das ist **zwingend** und nicht abdingbar — der Assetkreis lässt sich nicht so schneiden, dass die Belegschaft zurückbleibt, wenn die wirtschaftliche Einheit ihre Identität wahrt.

Für die vollständige Prüfung — Tatbestand der wirtschaftlichen Einheit, Unterrichtungsschreiben nach § 613a Abs. 5 BGB, Widerspruchsrecht und Monatsfrist nach Abs. 6, Kündigungsverbot nach Abs. 4, Fortgeltung von Kollektivnormen nach Abs. 1 S. 2 ff. — gilt: **`/arbeitsrecht:betriebsuebergang`**. Dieser Skill dupliziert das nicht.

Für den Asset Deal relevant bleiben drei Schnittstellen:

- Der Übergang ist **Kalkulationsfaktor**: Personalkosten, Pensionsverpflichtungen und Nachhaftung nach § 613a Abs. 2 BGB gehören in die Kaufpreisbildung.
- Das **Unterrichtungsschreiben** ist gemeinsam von Verkäufer und Erwerber zu verantworten; ein fehlerhaftes Schreiben setzt die Monatsfrist des Abs. 6 nicht in Lauf und lässt das Widerspruchsrecht praktisch unbefristet offen.
- **Widersprechende Arbeitnehmer** bleiben beim Verkäufer — das kann dessen Kalkulation zerstören und ist vertraglich (Freistellung, Kaufpreisanpassung) zu adressieren.

Die Berechnung der Monatsfrist übernimmt der deterministische Rechner:

```bash
python -m scripts.legal_calc.cli frist --ereignis 15.01.2026 --menge 1 --einheit monate --land BY
```

Er rechnet **ausschließlich** die Arithmetik der §§ 187–193 BGB. **Fristbeginn und Zugang bleiben rechtliche Eingaben** — ob die Unterrichtung ordnungsgemäß und wem sie wann zugegangen ist, entscheidet der Bearbeiter.

### 5. Firmenfortführungshaftung ([§ 25 HGB](https://www.gesetze-im-internet.de/hgb/__25.html))

**§ 25 Abs. 1 S. 1 HGB:** Wer ein unter Lebenden erworbenes **Handelsgeschäft** unter der **bisherigen Firma** fortführt — mit oder ohne Nachfolgezusatz —, haftet für **alle im Betrieb des Geschäfts begründeten Verbindlichkeiten** des früheren Inhabers. Die Haftung ist unbeschränkt und trifft den Erwerber unabhängig davon, ob er die Verbindlichkeit kannte. Nach § 25 Abs. 1 S. 2 HGB gelten zugleich die Forderungen den Schuldnern gegenüber als übergegangen, wenn der bisherige Inhaber in die Firmenfortführung eingewilligt hat.

**§ 25 Abs. 2 HGB — Enthaftungsvermerk:** Eine abweichende Vereinbarung ist gegenüber Dritten **nur wirksam**, wenn sie

1. **in das Handelsregister eingetragen und bekanntgemacht** wurde **oder**
2. vom Erwerber oder Veräußerer dem Dritten **mitgeteilt** wurde.

Der Haftungsausschluss im Kaufvertrag allein wirkt also **nur im Innenverhältnis**. Der Registervermerk ist **unverzüglich** und möglichst zeitgleich mit dem Vollzug anzumelden — eine spätere Eintragung schützt nicht rückwirkend gegenüber Gläubigern, die zuvor gutgläubig waren `[unverifiziert - prüfen]`.

**§ 25 Abs. 3 HGB:** Wird die Firma **nicht** fortgeführt, haftet der Erwerber nur bei besonderem Verpflichtungsgrund — insbesondere bei handelsüblicher Bekanntmachung der Schuldübernahme. Die einfachste Vermeidungsstrategie ist daher die **Firmenneubildung**. Bei Erwerb aus der Insolvenzmasse wird § 25 HGB nach h.M. teleologisch reduziert `[unverifiziert - prüfen]`.

### 6. Steuerliche Haftungs- und Folgetatbestände

**§ 75 AO — Betriebsübernehmerhaftung:** Wird ein Unternehmen oder ein gesondert geführter Betrieb **im Ganzen übereignet**, haftet der Erwerber für **betriebsbedingte Steuern** (Gewerbe- und Umsatzsteuer, nicht Einkommen-/Körperschaftsteuer des Veräußerers) und für **Steuerabzugsbeträge** (insbesondere Lohnsteuer). Doppelte Begrenzung:

- **zeitlich:** nur Steuern, die seit dem Beginn des letzten vor der Übereignung liegenden Kalenderjahres entstanden sind und die **bis zum Ablauf eines Jahres nach Anmeldung des Betriebs durch den Erwerber** festgesetzt oder angemeldet werden;
- **gegenständlich:** Haftung beschränkt auf den **Bestand des übernommenen Vermögens**.

§ 75 Abs. 2 AO nimmt Erwerbe aus einer **Insolvenzmasse** und im Vollstreckungsverfahren aus. Praktisch: Unbedenklichkeitsbescheinigung des Finanzamts einholen, Steuerfreistellung vereinbaren, Escrow-Betrag bis zum Ablauf der Jahresfrist zurückbehalten. Vgl. `/steuerrecht:aussenpruefung-betriebspruefung`.

**§ 1 Abs. 1a UStG — Geschäftsveräußerung im Ganzen:** Umsätze im Rahmen einer Geschäftsveräußerung an einen anderen Unternehmer für dessen Unternehmen **unterliegen nicht der Umsatzsteuer**; der Erwerber tritt an die Stelle des Veräußerers (Fortführung der Berichtigungszeiträume nach § 15a UStG). Voraussetzung ist die Übereignung eines Unternehmens oder gesondert geführten Betriebs **im Ganzen** und die Fortführung durch den Erwerber. Weil die Einordnung fehleranfällig ist, gehört in den Vertrag eine **Umsatzsteuerklausel**: Feststellung der Parteien, dass eine Geschäftsveräußerung im Ganzen vorliegt, Verpflichtung zur Rechnungsberichtigung mit gesondertem Steuerausweis für den Fall der abweichenden Beurteilung durch die Finanzverwaltung, Zahlungspflicht der Umsatzsteuer Zug um Zug gegen berichtigte Rechnung und Verzinsungsregelung. Eine verbindliche Auskunft nach § 89 Abs. 2 AO ist bei Zweifeln der sichere Weg.

**Grunderwerbsteuer:** Befindet sich ein **Grundstück** im Assetkreis, löst die Übertragung Grunderwerbsteuer nach § 1 Abs. 1 Nr. 1 GrEStG aus — anders als beim Share Deal, bei dem nur die Ergänzungstatbestände greifen. Zu regeln sind Steuerträgerschaft (gesetzlich sind beide Beteiligte Gesamtschuldner nach § 13 GrEStG), Bemessungsgrundlage, Anzeigepflichten nach §§ 18, 19 GrEStG und die **Unbedenklichkeitsbescheinigung** nach § 22 GrEStG als Voraussetzung der Grundbuchumschreibung. Der Steuersatz ist landesrechtlich unterschiedlich und im Einzelfall zu prüfen `[unverifiziert - prüfen]`.

## Quellen

### Statute

- [§ 613a BGB](https://www.gesetze-im-internet.de/bgb/__613a.html) (Betriebsübergang — vertiefte Prüfung in `/arbeitsrecht:betriebsuebergang`)
- [§ 25 HGB](https://www.gesetze-im-internet.de/hgb/__25.html) (Abs. 1 Firmenfortführungshaftung, Abs. 2 Enthaftungsvermerk, Abs. 3 ohne Firmenfortführung), [§ 27 HGB](https://www.gesetze-im-internet.de/hgb/__27.html)
- [§ 75 AO](https://www.gesetze-im-internet.de/ao_1977/__75.html) (Haftung des Betriebsübernehmers), [§ 89 AO](https://www.gesetze-im-internet.de/ao_1977/__89.html) (verbindliche Auskunft)
- [§ 1 UStG](https://www.gesetze-im-internet.de/ustg_1980/__1.html) (Abs. 1a Geschäftsveräußerung im Ganzen), [§ 15a UStG](https://www.gesetze-im-internet.de/ustg_1980/__15a.html)
- [§ 1 GrEStG](https://www.gesetze-im-internet.de/grestg_1983/__1.html), [§ 13 GrEStG](https://www.gesetze-im-internet.de/grestg_1983/__13.html), [§ 22 GrEStG](https://www.gesetze-im-internet.de/grestg_1983/__22.html)
- [§ 311b BGB](https://www.gesetze-im-internet.de/bgb/__311b.html), [§ 398 BGB](https://www.gesetze-im-internet.de/bgb/__398.html), [§ 929 BGB](https://www.gesetze-im-internet.de/bgb/__929.html), [§ 930 BGB](https://www.gesetze-im-internet.de/bgb/__930.html)

### Kommentare

- Hopt, in: Baumbach/Hopt, HGB, 42. Aufl. 2023, § 25 Rn. 1 ff. (Firmenfortführung, Enthaftung) `[unverifiziert - Auflagenstand prüfen]`
- Loose, in: Tipke/Kruse, AO/FGO, § 75 AO Rn. 1 ff. `[unverifiziert - Auflagenstand prüfen]`
- Beisel/Klumpp, Der Unternehmenskauf, 8. Aufl. 2022, Kap. 6 (Asset Deal) `[unverifiziert - Auflagenstand prüfen]`

### Rechtsprechung

- BGH, Urt. v. 28.11.2005 – II ZR 355/03 (§ 25 HGB, Fortführung der Firma) `[unverifiziert - prüfen]`
- BFH, Urt. v. 18.01.2012 – XI R 27/08 (Geschäftsveräußerung im Ganzen, § 1 Abs. 1a UStG) `[unverifiziert - prüfen]`

> Aktenzeichen vor Verwendung in juris / Beck-Online prüfen. Die tragenden Aussagen folgen aus dem Wortlaut der §§ 25 HGB, 75 AO, 1 Abs. 1a UStG und 613a BGB.

## Ausgabeformat

```
ASSET DEAL — <Betrieb / Verkäufer> — <Datum>

I.    Strukturwahl                  [Asset Deal — Motiv: <…>]
        Form:                       [formfrei / 🔴 § 311b BGB Grundstück / § 15 GmbHG Anteil]
II.   Assetkreis                    Anlagen: <Nr.>  Vorräte: <Nr.>  Forderungen: <Nr.>
                                    IP/Software: <Nr.>  Grundstücke: <Nr.>
        Bestimmtheit:               [✅ je Position / 🔴 Sammelbezeichnung ohne Anlage]
        Drittrechte:                [EV / Sicherungsübereignung / Globalzession — <…>]
        Zurückbehaltene Gegenstände: <Liste>
III.  Verträge                      Konsentliste: [x von y eingeholt]
        Closing-Bedingung:          <wesentliche Verträge>
        Innenverhältnis-Lösung:     [für: <…>]
        Genehmigungen:              [übertragbar / Neubeantragung — <…>]
IV.   § 613a BGB                    [Betriebsübergang: ja / nein / Teilbetrieb]
        Detailprüfung:              → /arbeitsrecht:betriebsuebergang
        Unterrichtung Abs. 5:       [Entwurf ✅/❌]  Widerspruchsfrist Abs. 6: <Datum>
        Kalkulation:                [Personalkosten, Pensionen, Nachhaftung Abs. 2 eingepreist ✅/❌]
V.    § 25 HGB                      Firmenfortführung: [ja / nein]
        Enthaftungsvermerk Abs. 2:  [angemeldet am <…> / 🔴 fehlt]
        Alternative:                [Firmenneubildung]
VI.   § 75 AO                       Haftungsrisiko: <Zeitraum, geschätzte Höhe>
        Absicherung:                [Unbedenklichkeitsbescheinigung / Escrow bis <Datum>]
VII.  Umsatzsteuer                  [§ 1 Abs. 1a UStG bejaht / zweifelhaft]
        USt-Klausel im Vertrag:     [✅ / ❌]  Verbindliche Auskunft § 89 AO: [ja / nein]
VIII. Grunderwerbsteuer             [einschlägig — Bemessungsgrundlage <…>, Träger: <…>]
        Anzeige §§ 18, 19 GrEStG:   [Frist <…>]  Unbedenklichkeitsbescheinigung § 22: [<…>]

Gesamtbefund: [🟢 / 🟡 / 🔴]
Offene Punkte: <Liste>
```

## Risiken / typische Fehler

- **Sammelbezeichnung statt bestimmter Assetliste** — die Übertragung scheitert am Bestimmtheitsgrundsatz; einzelne Gegenstände bleiben beim Verkäufer und fallen in dessen Insolvenzmasse.
- **Enthaftungsvermerk nach § 25 Abs. 2 HGB nicht angemeldet** — der vertragliche Haftungsausschluss wirkt nur im Innenverhältnis; im Außenverhältnis haftet der Erwerber für sämtliche Altverbindlichkeiten.
- **§ 613a BGB durch Vertragsgestaltung ausgeschlossen** — die Rechtsfolge ist zwingend und tritt unabhängig vom Parteiwillen ein, sobald die wirtschaftliche Einheit ihre Identität wahrt.
- **Widerspruchsrecht der Arbeitnehmer nicht eingepreist** — widersprechende Arbeitnehmer bleiben beim Verkäufer; ein fehlerhaftes Unterrichtungsschreiben setzt die Monatsfrist gar nicht erst in Lauf.
- **§ 75 AO übersehen** — der Erwerber haftet für betriebsbedingte Steuern und Lohnsteuer des Vorjahreszeitraums; ohne Unbedenklichkeitsbescheinigung und Escrow ist das ungesichert.
- **Geschäftsveräußerung im Ganzen unterstellt, ohne die Voraussetzungen zu prüfen** — bei abweichender Beurteilung schuldet der Verkäufer Umsatzsteuer, und ohne Vertragsklausel fehlt dem Käufer der Anspruch auf die berichtigte Rechnung mit Vorsteuerabzug.
- **Grundstück im Assetkreis nicht bemerkt** — der gesamte Vertrag wird nach § 311b BGB beurkundungsbedürftig und ist ohne Beurkundung nichtig; zusätzlich fällt Grunderwerbsteuer an.
- **Zustimmung zur Vertragsübernahme nicht eingeholt** — der Verkäufer bleibt Vertragspartei, der Käufer hat keinen Anspruch gegen den Vertragspartner, und Change-of-Control-Kündigungsrechte laufen ins Leere oder gerade nicht.
