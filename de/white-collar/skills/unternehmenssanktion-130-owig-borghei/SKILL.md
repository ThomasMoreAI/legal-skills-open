---
name: unternehmenssanktion-130-owig-borghei
title: /wirtschafts-steuerstrafrecht:unternehmenssanktion-130-owig
description: Sanktionierung von Unternehmen nach dem OWiG – Aufsichtspflichtverletzung § 130 OWiG mit Anknüpfungspflicht, erforderlichen Aufsichtsmaßnahmen und Kausalitätserfordernis, Verbandsgeldbuße § 30 OWiG mit Anknüpfungstat, Adressatenkreis, Bußgeldrahmen von bis zu zehn Millionen Euro bei vorsätzlicher Straftat und fünf Millionen Euro bei Fahrlässigkeit, Zumessung § 17 OWiG mit Compliance als Zumessungsfaktor, Abschöpfung des wirtschaftlichen Vorteils und Einziehung sowie Rechtsnachfolge § 30 Abs. 2a OWiG. Use when ein Bußgeldrisiko des Unternehmens nach einer Mitarbeitertat zu bewerten, eine Compliance-Organisation als Entlastung darzustellen oder eine Verbandsgeldbuße abzuwehren ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/wirtschafts-steuerstrafrecht/skills/unternehmenssanktion-130-owig
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: white-collar
language: de
---

# /wirtschafts-steuerstrafrecht:unternehmenssanktion-130-owig

## Zweck

Das deutsche Recht kennt keine Unternehmensstrafe. Es kennt aber mit §§ 30, 130 OWiG ein Sanktionsinstrument, das über Bußgeld, Abschöpfung und Einziehung wirtschaftlich erheblich zuschlagen kann — und dessen Anwendung fast immer an derselben Frage hängt: War die Aufsicht so organisiert, dass die Zuwiderhandlung wesentlich erschwert war? Dieser Skill bewertet das Bußgeldrisiko nach einer Mitarbeitertat, arbeitet die Entlastung durch eine funktionierende Compliance-Organisation heraus und beziffert das Abschöpfungsrisiko.

**Gesetzgebungsstand, ehrlich benannt:** Ein Verbandssanktionengesetz ist wiederholt vorgeschlagen und **nicht in Kraft getreten**. §§ 30, 130 OWiG sind und bleiben das geltende Recht. Aussagen über anhängige oder angekündigte Reformvorhaben sind `[unverifiziert – prüfen]` und vor jeder Verwendung am aktuellen Gesetzgebungsstand zu überprüfen.

## Eingaben

- Die Anknüpfungstat: Straftat oder Ordnungswidrigkeit, Zeitpunkt, handelnde Person
- Stellung der handelnden Person: Organ, Vorstand, vertretungsberechtigter Gesellschafter, Generalbevollmächtigter, Prokurist, Person in leitender Stellung, einfacher Mitarbeiter
- Betriebsbezogene Pflicht, deren Verletzung im Raum steht
- Bestehende Aufsichtsorganisation: Zuständigkeiten, Delegation, Schulungen, Kontrollen, Hinweisgebersystem, Dokumentation
- Wirtschaftlicher Vorteil aus der Tat, brutto und netto
- Kooperationsverhalten: Selbstanzeige, Internal Investigation, Herausgabe von Unterlagen
- Umwandlungs- oder Übernahmevorgänge nach der Tat (Rechtsnachfolge)

## Sub-Agent-Architektur

Der **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) ordnet die Anknüpfungstat zu und belegt Adressatenkreis und Bußgeldrahmen. Der **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) stellt die Aufsichtsorganisation gegen die Anforderungen des § 130 OWiG und entwirft die Stellungnahme an die Bußgeldbehörde. Der **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft, ob Kausalität, Zumessung und Abschöpfung getrennt behandelt sind und ob die Aussage zum Gesetzgebungsstand korrekt markiert ist.

## Ablauf

### 1. Aufsichtspflichtverletzung ([§ 130 OWiG](https://www.gesetze-im-internet.de/owig_1968/__130.html))

Ordnungswidrig handelt, wer als **Inhaber eines Betriebes oder Unternehmens** vorsätzlich oder fahrlässig die Aufsichtsmaßnahmen unterlässt, die erforderlich sind, um in dem Betrieb Zuwiderhandlungen gegen Pflichten zu verhindern, die den Inhaber treffen und deren Verletzung mit Strafe oder Geldbuße bedroht ist. Vier Prüfungspunkte:

1. **Betriebsbezogene Inhaberpflicht** — die verletzte Pflicht muss den Inhaber treffen, nicht nur den Handelnden persönlich.
2. **Unterlassene erforderliche Aufsichtsmaßnahmen** — zu ihnen gehören ausdrücklich die **Bestellung, sorgfältige Auswahl und Überwachung von Aufsichtspersonen** (§ 130 Abs. 1 S. 2 OWiG). Delegation entlastet nur bei sorgfältiger Auswahl, Einweisung und fortlaufender Überwachung.
3. **Zuwiderhandlung**, die bei gehöriger Aufsicht **verhindert oder wesentlich erschwert** worden wäre — ein abgeschwächtes Kausalitätserfordernis, das die Behörde dennoch darlegen muss.
4. **Vorsatz oder Fahrlässigkeit** hinsichtlich der Aufsichtspflichtverletzung.

Bußgeldrahmen nach § 130 Abs. 3 OWiG: bis zu **einer Million Euro**, wenn die Pflichtverletzung mit Strafe bedroht ist; ist sie nur mit Geldbuße bedroht, bestimmt sich das Höchstmaß nach dem für die Pflichtverletzung angedrohten Höchstmaß.

§ 130 OWiG ist der **Auffangtatbestand**: Er greift, wenn dem Leitungspersonal die Beteiligung an der Haupttat nicht nachzuweisen ist, und schafft damit erst die Anknüpfungstat für § 30 OWiG.

### 2. Verbandsgeldbuße ([§ 30 OWiG](https://www.gesetze-im-internet.de/owig_1968/__30.html))

Gegen eine juristische Person oder Personenvereinigung kann eine Geldbuße festgesetzt werden, wenn eine der in § 30 Abs. 1 Nr. 1 bis 5 OWiG genannten Personen eine Straftat oder Ordnungswidrigkeit begangen hat, durch die **Pflichten des Verbandes verletzt** worden sind oder der Verband **bereichert** wurde oder werden sollte.

**Adressatenkreis der Anknüpfungstat** (§ 30 Abs. 1 OWiG): vertretungsberechtigtes Organ oder Mitglied eines solchen Organs, Vorstand eines nicht rechtsfähigen Vereins, vertretungsberechtigter Gesellschafter, Generalbevollmächtigter, Prokurist oder Handlungsbevollmächtigter in leitender Stellung sowie sonstige **Personen in leitender Stellung**, zu der auch die Überwachung der Betriebsführung gehört. Die Tat eines einfachen Mitarbeiters genügt **nicht** — dann führt der Weg über § 130 OWiG, dessen Verletzung durch das Leitungspersonal selbst die Anknüpfungstat bildet.

**Bußgeldrahmen** (§ 30 Abs. 2 OWiG):

| Anknüpfungstat | Höchstmaß |
|---|---|
| Vorsätzliche Straftat | bis zu **zehn Millionen Euro** |
| Fahrlässige Straftat | bis zu **fünf Millionen Euro** |
| Ordnungswidrigkeit | Höchstmaß der für die Ordnungswidrigkeit angedrohten Geldbuße, das sich verzehnfachen kann |

Nach § 30 Abs. 4 OWiG kann die Geldbuße **selbständig** festgesetzt werden, wenn wegen der Anknüpfungstat ein Straf- oder Bußgeldverfahren nicht eingeleitet oder eingestellt wird. Nach § 30 Abs. 5 OWiG schließen sich Verbandsgeldbuße und Einziehung gegen denselben Verband wegen derselben Tat wechselseitig aus.

### 3. Zumessung und Abschöpfung ([§ 17 OWiG](https://www.gesetze-im-internet.de/owig_1968/__17.html))

Grundlage der Zumessung sind die Bedeutung der Ordnungswidrigkeit und der Vorwurf, der den Täter trifft; die wirtschaftlichen Verhältnisse kommen hinzu. Die Geldbuße hat **zwei Komponenten**:

- die **Ahndungskomponente** — die eigentliche Sanktion, und
- die **Abschöpfungskomponente** — nach § 17 Abs. 4 OWiG soll die Geldbuße den wirtschaftlichen Vorteil übersteigen, den der Täter aus der Ordnungswidrigkeit gezogen hat; reicht das gesetzliche Höchstmaß dafür nicht aus, darf es überschritten werden.

Daneben steht die **Einziehung** nach [§ 29a OWiG](https://www.gesetze-im-internet.de/owig_1968/__29a.html) bzw. bei Straftaten nach §§ 73 ff. StGB. Die Abgrenzung ist praktisch bedeutsam: § 30 Abs. 5 OWiG verbietet die Doppelbelastung, aber die Behörde wählt den für sie günstigeren Weg.

### 4. Compliance als Zumessungsfaktor

Eine funktionierende Compliance-Organisation wirkt auf **drei** Ebenen, die getrennt zu argumentieren sind:

1. **Tatbestandsebene § 130 OWiG:** Waren die erforderlichen Aufsichtsmaßnahmen getroffen, entfällt die Aufsichtspflichtverletzung — und damit fällt die Anknüpfungstat für § 30 OWiG weg. Das ist die stärkste, aber auch anspruchsvollste Verteidigung.
2. **Zumessungsebene § 17 OWiG:** Ein vor der Tat eingerichtetes und wirksames Compliance-Management-System sowie dessen Nachbesserung nach Aufdeckung wirken bußgeldmindernd `[unverifiziert – prüfen]`.
3. **Verfahrensebene:** Kooperation, Aufklärungsbeitrag und Schadenswiedergutmachung wirken auf Einstellungsbereitschaft und Höhe.

Entscheidend ist die **Dokumentation**: Ein CMS, dessen Wirksamkeit nicht belegt ist — Schulungsnachweise, Kontrollberichte, Eskalationen, Sanktionierung erkannter Verstöße —, wird in der Praxis nicht als Entlastung anerkannt. Ein System, das Verstöße dokumentiert, aber folgenlos lässt, verschlechtert die Position.

### 5. Rechtsnachfolge ([§ 30 Abs. 2a OWiG](https://www.gesetze-im-internet.de/owig_1968/__30.html))

Die Geldbuße kann auch gegen den **Rechtsnachfolger** festgesetzt werden; im Fall der Gesamtrechtsnachfolge und der partiellen Gesamtrechtsnachfolge durch Aufspaltung ist die Festsetzung auf den **Wert des übernommenen Vermögens** begrenzt. Das macht das Bußgeldrisiko zum Prüfungspunkt jeder Due Diligence: Ein Verschmelzungs- oder Spaltungsvorgang beendet das Risiko nicht, und die Freistellungsklausel im Kaufvertrag wirkt nur im Innenverhältnis.

### 6. Formulierungshilfe — Stellungnahme an die Bußgeldbehörde

```
An die <Bußgeldbehörde / Staatsanwaltschaft>
Az. <…>

In dem Ordnungswidrigkeitenverfahren gegen die <Firma>
wegen des Vorwurfs nach §§ 30, 130 OWiG

I.   Sachverhalt aus Sicht des Unternehmens
     <Chronologie der Zuwiderhandlung, Aufdeckung, Reaktion.>

II.  Zur Anknüpfungstat (§ 30 Abs. 1 OWiG)
     Der Handelnde war <Funktion>. Eine Stellung im Sinne des
     § 30 Abs. 1 Nr. 1 bis 5 OWiG lag nicht vor; insbesondere war
     ihm die Überwachung der Betriebsführung nicht übertragen.

III. Zur Aufsichtspflicht (§ 130 Abs. 1 OWiG)
     Die erforderlichen Aufsichtsmaßnahmen waren getroffen:
     1. Bestellung: <Compliance-Funktion, Bestellungsurkunde vom …>
     2. Sorgfältige Auswahl: <Qualifikation, Auswahlverfahren>
     3. Überwachung: <Kontrollplan, Berichte vom …>
     4. Schulung: <Nachweise, Teilnehmerlisten>
     5. Sanktionierung erkannter Verstöße: <Beispiele>
     Die Zuwiderhandlung wäre auch bei weitergehender Aufsicht
     nicht verhindert oder wesentlich erschwert worden, weil
     <kollusives Zusammenwirken / Umgehung der Kontrollen>.

IV.  Zur Zumessung (§ 17 OWiG)
     Ein wirtschaftlicher Vorteil ist dem Unternehmen nicht
     zugeflossen; hilfsweise beträgt er <…> EUR (Anlage <…>).
     Das CMS bestand bereits vor der Tat und wurde nach
     Aufdeckung um <…> ergänzt.

V.   Zur Einziehung
     § 30 Abs. 5 OWiG schließt die Nebeneinanderfestsetzung von
     Verbandsgeldbuße und Einziehung gegen dasselbe Unternehmen
     wegen derselben Tat aus.

VI.  Anträge
     1. Einstellung des Verfahrens.
     2. Hilfsweise: Absehen von einer Verbandsgeldbuße.
     3. Akteneinsicht.

<Ort, Datum, Unterschrift>
```

## Quellen

### Statute

- [§ 30 OWiG](https://www.gesetze-im-internet.de/owig_1968/__30.html), [§ 130 OWiG](https://www.gesetze-im-internet.de/owig_1968/__130.html), [§ 17 OWiG](https://www.gesetze-im-internet.de/owig_1968/__17.html), [§ 29a OWiG](https://www.gesetze-im-internet.de/owig_1968/__29a.html), [§ 47 OWiG](https://www.gesetze-im-internet.de/owig_1968/__47.html) (Opportunitätsprinzip)
- [§ 9 OWiG](https://www.gesetze-im-internet.de/owig_1968/__9.html) (Handeln für einen anderen), [§ 14 StGB](https://www.gesetze-im-internet.de/stgb/__14.html)
- [§ 73 StGB](https://www.gesetze-im-internet.de/stgb/__73.html) ff. (Einziehung bei Straftaten), [§ 111e StPO](https://www.gesetze-im-internet.de/stpo/__111e.html) (Vermögensarrest)
- [§ 43 GmbHG](https://www.gesetze-im-internet.de/gmbhg/__43.html), [§ 93 AktG](https://www.gesetze-im-internet.de/aktg/__93.html), [§ 91 Abs. 2 AktG](https://www.gesetze-im-internet.de/aktg/__91.html) (Überwachungssystem als gesellschaftsrechtliche Flanke)

### Kommentare

- Rogall, in: Karlsruher Kommentar zum OWiG, 5. Aufl. 2018, § 130 Rn. 1 ff. und § 30 Rn. 1 ff.
- Gürtler, in: Göhler, OWiG, 18. Aufl. 2021, § 130 Rn. 1 ff.
- Beck, in: Graf, BeckOK OWiG, § 30 Rn. 1 ff. (Adressatenkreis, Rechtsnachfolge)
- Moosmayer, Compliance, 4. Aufl. 2021, Rn. 1 ff. (Anforderungen an ein wirksames CMS)

### Rechtsprechung

- Rechtsprechung zur bußgeldmindernden Berücksichtigung eines vor der Tat eingerichteten und nach Aufdeckung nachgebesserten Compliance-Management-Systems `[unverifiziert – prüfen]`
- Rechtsprechung zu den Anforderungen an die Darlegung, dass die Zuwiderhandlung bei gehöriger Aufsicht verhindert oder wesentlich erschwert worden wäre `[unverifiziert – prüfen]`
- Gesetzgebungsstand zum Verbandssanktionengesetz: wiederholt vorgeschlagen, nicht in Kraft getreten `[unverifiziert – prüfen]`

> Fundstellen sind vor Verwendung in juris oder Beck-Online zu ermitteln. In diesem Skill wird bewusst keine Entscheidung benannt, die nicht extern verifiziert wurde.

## Ausgabeformat

```
UNTERNEHMENSSANKTION §§ 30, 130 OWiG — <Az.> — <Datum>
VERTRAULICH — § 43a Abs. 2 BRAO

Gesamtbefund: [🟢 kein Bußgeldrisiko / 🟡 Zumessung verhandelbar /
               🔴 Verbandsgeldbuße wahrscheinlich]

I.    Anknüpfungstat § 30 Abs. 1     <Straftat / Ordnungswidrigkeit>
      Handelnde Person               <Funktion>
      Leitungsstellung Nr. 1–5       [🟢 nein / 🔴 ja]
      Pflichtverletzung des Verbands [ja / nein]  Bereicherung [ja / nein]
II.   Aufsichtspflicht § 130 OWiG
      Betriebsbezogene Inhaberpflicht <…>
      Bestellung                     [🟢 belegt / 🔴 offen]
      Sorgfältige Auswahl            [🟢 / 🔴]
      Überwachung                    [🟢 / 🔴]
      Kausalität (verhindert oder
      wesentlich erschwert)          [bestritten / eingeräumt]
III.  Bußgeldrahmen
      § 130 Abs. 3 OWiG              bis 1 Mio. EUR / abgeleitet
      § 30 Abs. 2 OWiG               [10 Mio. vorsätzlich /
                                      5 Mio. fahrlässig / OWi-Rahmen]
IV.   Zumessung § 17 OWiG
      Ahndungskomponente             <…> EUR
      Abschöpfung § 17 Abs. 4 OWiG   <…> EUR  [wirtschaftl. Vorteil]
      CMS vor der Tat                [belegt durch <…>]
      Nachbesserung nach Aufdeckung  [<…>]
      Kooperation                    [<…>]
V.    Einziehung                     [§ 29a OWiG / §§ 73 ff. StGB]
      § 30 Abs. 5 OWiG               [Doppelbelastung ausgeschlossen]
VI.   Rechtsnachfolge § 30 Abs. 2a   [N/A / begrenzt auf übernommenes
                                      Vermögen]
VII.  Gesetzgebungsstand             §§ 30, 130 OWiG geltendes Recht;
                                     Verbandssanktionengesetz nicht
                                     in Kraft getreten
                                     [unverifiziert – prüfen]

Empfehlung: <…>
Nächster Schritt: <Stellungnahme / Akteneinsicht / CMS-Nachweis>
```

## Risiken / typische Fehler

- **Anknüpfungstat nicht geprüft.** § 30 OWiG setzt eine Tat aus dem Kreis des Abs. 1 Nr. 1 bis 5 voraus; die Tat eines einfachen Mitarbeiters genügt nur mittelbar über eine Aufsichtspflichtverletzung des Leitungspersonals.
- **CMS behauptet, aber nicht belegt.** Ohne Schulungsnachweise, Kontrollberichte, Eskalationsdokumentation und Sanktionierung erkannter Verstöße wird die Compliance-Organisation weder auf Tatbestands- noch auf Zumessungsebene anerkannt.
- **Delegation als vollständige Entlastung behandelt** — § 130 Abs. 1 S. 2 OWiG verlangt Bestellung, sorgfältige Auswahl **und** Überwachung.
- **Kausalitätserfordernis nicht angegriffen.** Dass die Zuwiderhandlung bei gehöriger Aufsicht verhindert oder wesentlich erschwert worden wäre, muss die Behörde darlegen; kollusives Zusammenwirken und Umgehung der Kontrollen sind Gegenargumente.
- **Abschöpfungskomponente übersehen.** Nach § 17 Abs. 4 OWiG darf das gesetzliche Höchstmaß überschritten werden, soweit der wirtschaftliche Vorteil das erfordert — das Risiko ist nicht auf zehn Millionen Euro begrenzt.
- **§ 30 Abs. 5 OWiG nicht geltend gemacht**, sodass Verbandsgeldbuße und Einziehung nebeneinander in Ansatz gebracht werden.
- **Rechtsnachfolge nach § 30 Abs. 2a OWiG in der Transaktion nicht geprüft** — Umwandlungen beenden das Bußgeldrisiko nicht.
- **Reformerwartung als geltendes Recht dargestellt.** Ein Verbandssanktionengesetz ist nicht in Kraft getreten; jede Aussage über den Gesetzgebungsstand ist zu markieren und zu prüfen.
- **Selbstbelastungsrisiko der Kooperation nicht bedacht** — Ergebnisse einer Internal Investigation können zugleich Beweismittel gegen das Unternehmen sein.
