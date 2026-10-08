---
name: gewerbeerlaubnis-34-gewo-borghei
title: /gewerberecht:gewerbeerlaubnis-34-gewo
description: Erlaubnispflichtige Gewerbe der GewO – Bewachungsgewerbe § 34a mit Sachkundeprüfung vor der IHK, Immobilienmakler, Darlehensvermittler, Bauträger, Baubetreuer und Wohnimmobilienverwalter § 34c mit den Versagungsgründen Unzuverlässigkeit (Regelvermutung bei Verurteilung wegen Vermögensdelikten in den letzten fünf Jahren), ungeordneten Vermögensverhältnissen (Regelvermutung bei Insolvenzeröffnung oder Eintragung nach § 882b ZPO) und fehlender Berufshaftpflichtversicherung für Wohnimmobilienverwalter, Weiterbildungspflicht von 20 Stunden in drei Kalenderjahren § 34c Abs. 2a, Pflichten nach der MaBV, Versicherungsvermittler § 34d, Finanzanlagenvermittler § 34f, Immobiliardarlehensvermittler § 34i sowie Rücknahme und Widerruf nach §§ 48, 49 VwVfG mit der Sperrwirkung des § 35 Abs. 8 GewO. Use when eine Erlaubnis zu beantragen, zu verteidigen oder ihr Widerruf abzuwehren ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/gewerberecht/skills/gewerbeerlaubnis-34-gewo
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: administrative
language: de
---

# /gewerberecht:gewerbeerlaubnis-34-gewo

## Zweck

Der Skill bearbeitet die erlaubnispflichtigen Gewerbe des Titels II der GewO: Er ordnet die Tätigkeit der richtigen Erlaubnisnorm zu, prüft die Versagungsgründe einschließlich der gesetzlichen Regelvermutungen, kontrolliert die begleitenden Pflichten — Sachkunde, Versicherung, Weiterbildung, MaBV — und behandelt Rücknahme und Widerruf, die bei erlaubnispflichtigen Gewerben an die Stelle der Untersagung nach § 35 GewO treten.

## Eingaben

- Tätigkeitsbeschreibung und Vertragsmuster; beabsichtigter Umfang
- Rechtsform und Person der Betriebsleiter bzw. vertretungsberechtigten Personen
- Vorstrafen und laufende Verfahren; Auszug aus dem Gewerbezentralregister
- Vermögenslage: Insolvenzverfahren, Eintragung nach § 26 Abs. 2 InsO oder § 882b ZPO, Vollstreckungsmaßnahmen
- Sachkundenachweise, Berufshaftpflichtversicherung, Weiterbildungsnachweise
- Bei Bestandserlaubnis: Erteilungsdatum, Auflagen, Prüfberichte nach der MaBV
- Bei behördlichem Verfahren: Anhörungs-, Rücknahme- oder Widerrufsbescheid

## Sub-Agent-Architektur

Der Researcher beschafft die Erlaubnisnormen, die zugehörigen Verordnungen (MaBV, BewachV, FinVermV, VersVermV) und die Rechtsprechung zu Zuverlässigkeit und Vermögensverhältnissen. Der Drafter ordnet die Tätigkeit zu, prüft Versagungsgründe und Nebenpflichten und entwirft Antrag oder Rechtsbehelf. Der Reviewer kontrolliert, ob die richtige Erlaubnisnorm gewählt wurde, ob Regelvermutungen zutreffend widerlegt werden und ob bei Bestandserlaubnissen § 35 Abs. 8 GewO beachtet ist.

## Ablauf

### 1. Erlaubnisnorm bestimmen

**Die Zuordnung entscheidet über Behörde, Voraussetzungen und Nebenpflichten.**

| Tätigkeit | Norm | Zuständigkeit |
|---|---|---|
| Bewachung von Leben oder Eigentum fremder Personen | [§ 34a GewO](https://www.gesetze-im-internet.de/gewo/__34a.html) | zuständige Behörde nach Landesrecht |
| Vermittlung oder Nachweis von Verträgen über Grundstücke, grundstücksgleiche Rechte, gewerbliche Räume oder Wohnräume (**Immobilienmakler**) | [§ 34c Abs. 1 S. 1 Nr. 1 GewO](https://www.gesetze-im-internet.de/gewo/__34c.html) | zuständige Behörde |
| Vermittlung oder Nachweis von **Darlehensverträgen** außerhalb des § 34i | § 34c Abs. 1 S. 1 Nr. 2 GewO | zuständige Behörde |
| **Bauträger** (im eigenen Namen für eigene oder fremde Rechnung unter Verwendung von Vermögenswerten Dritter) und **Baubetreuer** | § 34c Abs. 1 S. 1 Nr. 3 GewO | zuständige Behörde |
| **Wohnimmobilienverwalter** (Verwaltung gemeinschaftlichen Eigentums iSd § 1 Abs. 2, 3, 5, 6 WEG oder von Mietverhältnissen über Wohnraum iSd § 549 BGB für Dritte) | § 34c Abs. 1 S. 1 Nr. 4 GewO | zuständige Behörde |
| Versicherungsvermittler und Versicherungsberater | [§ 34d GewO](https://www.gesetze-im-internet.de/gewo/__34d.html) | **Industrie- und Handelskammer** |
| Finanzanlagenvermittler | [§ 34f GewO](https://www.gesetze-im-internet.de/gewo/__34f.html) | zuständige Behörde |
| Honorar-Finanzanlagenberater | [§ 34h GewO](https://www.gesetze-im-internet.de/gewo/__34h.html) | zuständige Behörde |
| Immobiliardarlehensvermittler | [§ 34i GewO](https://www.gesetze-im-internet.de/gewo/__34i.html) | zuständige Behörde |

Vorgelagert ist stets die Abgrenzung nach [§ 6 GewO](https://www.gesetze-im-internet.de/gewo/__6.html): Rechtsanwälte, Patentanwälte, Notare, Wirtschaftsprüfer, Steuerberater, Heilberufe und weitere dort genannte Tätigkeiten unterfallen der GewO nicht. Ebenso ist die Abgrenzung zu erlaubnispflichtigen Tätigkeiten nach KWG, WpIG, ZAG und KAGB zu prüfen — § 34f GewO knüpft ausdrücklich an die Bereichsausnahmen des § 2 Abs. 6 S. 1 Nr. 8 KWG und des § 3 Abs. 1 S. 1 Nr. 11 WpIG an.

Die Erlaubnis kann nach § 34c Abs. 1 S. 2 und § 34a Abs. 1 S. 2 GewO **inhaltlich beschränkt und mit Auflagen** versehen werden, soweit dies zum Schutz der Allgemeinheit oder der Auftraggeber erforderlich ist — auch nachträglich.

### 2. Versagungsgründe des § 34c Abs. 2 GewO prüfen

Die Erlaubnis **ist zu versagen**, wenn einer der drei Gründe vorliegt — gebundene Entscheidung:

**Nr. 1 — Unzuverlässigkeit.** Tatsachen rechtfertigen die Annahme, dass der Antragsteller oder eine mit der Leitung des Betriebes oder einer Zweigniederlassung beauftragte Person die erforderliche Zuverlässigkeit nicht besitzt. **Gesetzliche Regelvermutung**: Die erforderliche Zuverlässigkeit besitzt **in der Regel nicht**, wer in den **letzten fünf Jahren vor Antragstellung** rechtskräftig verurteilt wurde wegen

- eines **Verbrechens** oder
- **Diebstahls, Unterschlagung, Erpressung, Betruges, Untreue, Geldwäsche, Urkundenfälschung, Hehlerei, Wuchers** oder einer **Insolvenzstraftat**.

Die Vermutung ist widerlegbar; die Widerlegung erfordert konkreten Vortrag zu Tat, Zeitablauf, Bewährung und geänderten Lebensumständen. Verwertungsverbote des BZRG sind zu beachten.

**Nr. 2 — Ungeordnete Vermögensverhältnisse.** **Regelvermutung**, wenn über das Vermögen des Antragstellers das **Insolvenzverfahren eröffnet** wurde oder er in das vom Vollstreckungsgericht geführte Verzeichnis nach [§ 26 Abs. 2 InsO](https://www.gesetze-im-internet.de/inso/__26.html) oder [§ 882b ZPO](https://www.gesetze-im-internet.de/zpo/__882b.html) eingetragen ist. Auch diese Vermutung ist widerlegbar — etwa durch bestätigten Insolvenzplan, angekündigte oder erteilte Restschuldbefreiung oder ein tragfähiges Entschuldungskonzept.

**Nr. 3 — Fehlende Berufshaftpflichtversicherung** beim **Wohnimmobilienverwalter** (Abs. 1 S. 1 Nr. 4).

Für das **Bewachungsgewerbe** tritt nach § 34a Abs. 1 S. 3 Nr. 3 GewO als eigenständiger Versagungsgrund die fehlende **Sachkundeprüfung vor der Industrie- und Handelskammer** hinzu; die weiteren Anforderungen des § 34a — insbesondere Zuverlässigkeitsüberprüfung des eingesetzten Wachpersonals und Bewacherregister — sind gesondert zu prüfen.

### 3. Laufende Pflichten prüfen

- **Weiterbildung (§ 34c Abs. 2a GewO)**: Gewerbetreibende nach Abs. 1 S. 1 Nr. 4 — Wohnimmobilienverwalter — sind verpflichtet, sich im Umfang von **20 Stunden innerhalb von drei Kalenderjahren** weiterzubilden; dasselbe gilt für unmittelbar mitwirkende Beschäftigte. Der erste Weiterbildungszeitraum beginnt am **1. Januar des Kalenderjahres**, in dem die Erlaubnis erteilt oder die weiterbildungspflichtige Tätigkeit aufgenommen wurde. Der Nachweis kann durch eine angemessene Zahl aufsichtsführender, vertretungsbefugter Beschäftigter erbracht werden.
- **MaBV** — Die [Verordnung über die Pflichten der Immobilienmakler, Darlehensvermittler, Bauträger, Baubetreuer und Wohnimmobilienverwalter](https://www.gesetze-im-internet.de/gewo_34cdv/) konkretisiert die Berufspflichten: Sicherheitsleistung und Versicherung, getrennte Vermögensverwaltung, Anzeige- und Buchführungspflichten sowie – bei Bauträgern – die Voraussetzungen für die Entgegennahme von Vermögenswerten und der Zahlungsplan. Verstöße sind bußgeldbewehrt und begründen zugleich Zweifel an der Zuverlässigkeit.
- **Prüfungspflicht**: Der Gewerbetreibende hat auf eigene Kosten die Einhaltung der MaBV-Pflichten prüfen zu lassen und den Prüfungsbericht vorzulegen; der Umfang richtet sich nach der Verordnung `[unverifiziert – prüfen]` hinsichtlich der aktuellen Fassung.
- **Registerpflichten**: Für Versicherungs- und Finanzanlagenvermittler besteht die Eintragung im Vermittlerregister; für das Bewachungsgewerbe das Bewacherregister.

### 4. Rücknahme und Widerruf statt Untersagung

**Dies ist der praktisch wichtigste Unterschied zum Skill `gewerbeuntersagung-35-gewo`.** Nach [§ 35 Abs. 8 S. 1 GewO](https://www.gesetze-im-internet.de/gewo/__35.html) sind die Absätze 1 bis 7a **nicht anzuwenden**, soweit eine erteilte Zulassung wegen Unzuverlässigkeit zurückgenommen oder widerrufen werden kann. Bei erlaubnispflichtigen Gewerben ist daher zu prüfen:

| Instrument | Norm | Voraussetzung |
|---|---|---|
| **Rücknahme** | [§ 48 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__48.html) | Erlaubnis war **von Anfang an rechtswidrig** — etwa weil ein Versagungsgrund bereits bei Erteilung vorlag; Vertrauensschutz und Jahresfrist des § 48 Abs. 4 VwVfG beachten |
| **Widerruf** | [§ 49 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__49.html) | Nachträglicher Eintritt von Tatsachen, die zur Versagung berechtigt hätten (§ 49 Abs. 2 S. 1 Nr. 3 VwVfG); Jahresfrist nach § 49 Abs. 2 S. 2 iVm § 48 Abs. 4 VwVfG |
| Spezialgesetzliche Aufhebung | z. B. § 34d Abs. 5, § 34f iVm den jeweiligen Absätzen | vorrangig, soweit vorhanden `[unverifiziert – prüfen]` je Norm |

Die **Jahresfrist des § 48 Abs. 4 VwVfG** — analog anwendbar über § 49 Abs. 2 S. 2 VwVfG — beginnt mit der vollständigen Kenntnis der Behörde von den Tatsachen und ist der wirksamste formale Angriffspunkt. Sie ist in jedem Mandat zu prüfen und zu berechnen.

Neben der Aufhebung der Erlaubnis kommt die **Untersagung des Betriebs ohne Zulassung** nach [§ 15 Abs. 2 GewO](https://www.gesetze-im-internet.de/gewo/__15.html) in Betracht, wenn ohne die erforderliche Erlaubnis gearbeitet wird (`/gewerberecht:gewerbeanzeige-reisegewerbe`).

### 5. Verfahren und Rechtsschutz

- **Anhörung** nach [§ 28 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__28.html); **Begründung** nach [§ 39 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__39.html), insbesondere zur Ermessensausübung bei Rücknahme und Widerruf.
- **Verpflichtungsklage** auf Erteilung der Erlaubnis nach [§ 42 Abs. 1 Alt. 2 VwGO](https://www.gesetze-im-internet.de/vwgo/__42.html); bei gebundener Entscheidung Verpflichtungs-, sonst Bescheidungsurteil nach § 113 Abs. 5 VwGO.
- **Anfechtungsklage** gegen Rücknahme oder Widerruf; Fristen nach §§ 70, 74 VwGO.
- **Sofortvollzug** nach § 80 Abs. 2 S. 1 Nr. 4 VwGO mit Begründungserfordernis nach § 80 Abs. 3 VwGO; Rechtsbehelf § 80 Abs. 5 VwGO.
- **Bußgeld und Strafbarkeit**: Tätigkeit ohne erforderliche Erlaubnis ist nach [§ 144 GewO](https://www.gesetze-im-internet.de/gewo/__144.html) bußgeldbewehrt; das Bewachungsgewerbe kennt in § 34a Abs. 1 zusätzliche Anforderungen, deren Verletzung eigenständig sanktioniert ist.

## Deterministische Berechnung

Der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) macht nur die Arithmetik; der Fristbeginn bleibt juristische Eingabe:

```bash
# Fünfjahreszeitraum der Regelvermutung § 34c Abs. 2 Nr. 1 GewO, Antrag am 01.04.2026
python -m scripts.legal_calc.cli frist --ereignis 01.04.2021 --menge 5 --einheit jahre --land BY

# Jahresfrist § 48 Abs. 4 VwVfG ab vollständiger Kenntnis der Behörde am 15.09.2025
python -m scripts.legal_calc.cli frist --ereignis 15.09.2025 --menge 1 --einheit jahre --land BY

# Weiterbildungszeitraum § 34c Abs. 2a GewO: drei Kalenderjahre ab 01.01.2026
python -m scripts.legal_calc.cli frist --ereignis 01.01.2026 --menge 3 --einheit jahre --land BY

# Widerspruchsfrist § 70 VwGO
python -m scripts.legal_calc.cli frist --ereignis 20.05.2026 --menge 1 --einheit monate --land BY
```

## Quellen

### Statute

- [§ 6 GewO](https://www.gesetze-im-internet.de/gewo/__6.html), [§ 15 GewO](https://www.gesetze-im-internet.de/gewo/__15.html), [§ 34a GewO](https://www.gesetze-im-internet.de/gewo/__34a.html), [§ 34c GewO](https://www.gesetze-im-internet.de/gewo/__34c.html), [§ 34d GewO](https://www.gesetze-im-internet.de/gewo/__34d.html), [§ 34f GewO](https://www.gesetze-im-internet.de/gewo/__34f.html), [§ 34h GewO](https://www.gesetze-im-internet.de/gewo/__34h.html), [§ 34i GewO](https://www.gesetze-im-internet.de/gewo/__34i.html), [§ 35 GewO](https://www.gesetze-im-internet.de/gewo/__35.html), [§ 144 GewO](https://www.gesetze-im-internet.de/gewo/__144.html)
- [MaBV](https://www.gesetze-im-internet.de/gewo_34cdv/) — [§ 2](https://www.gesetze-im-internet.de/gewo_34cdv/__2.html), [§ 7](https://www.gesetze-im-internet.de/gewo_34cdv/__7.html), [§ 15b](https://www.gesetze-im-internet.de/gewo_34cdv/__15b.html)
- [§ 48 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__48.html), [§ 49 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__49.html), [§ 28 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__28.html), [§ 39 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__39.html)
- [§ 42 VwGO](https://www.gesetze-im-internet.de/vwgo/__42.html), [§ 70 VwGO](https://www.gesetze-im-internet.de/vwgo/__70.html), [§ 74 VwGO](https://www.gesetze-im-internet.de/vwgo/__74.html), [§ 80 VwGO](https://www.gesetze-im-internet.de/vwgo/__80.html), [§ 113 VwGO](https://www.gesetze-im-internet.de/vwgo/__113.html)
- [§ 26 InsO](https://www.gesetze-im-internet.de/inso/__26.html), [§ 882b ZPO](https://www.gesetze-im-internet.de/zpo/__882b.html), [§ 549 BGB](https://www.gesetze-im-internet.de/bgb/__549.html), [§ 1 WEG](https://www.gesetze-im-internet.de/woeigg/__1.html)
- [BZRG](https://www.gesetze-im-internet.de/bzrg/); BewachV, FinVermV, VersVermV `[unverifiziert – prüfen]` hinsichtlich der jeweils geltenden Fassung

### Kommentare

- Landmann/Rohmer, GewO, §§ 34a, 34c, 34f.
- Pielow, GewO, § 34c.
- Ennuschat/Wank/Winkler, GewO, § 34c, § 35.
- Marcks, MaBV (Kommentar zur Makler- und Bauträgerverordnung).
- Kopp/Ramsauer, VwVfG, §§ 48, 49.

### Rechtsprechung

Zur Zuverlässigkeit nach § 34c GewO, zur Widerlegung der Regelvermutungen und zur Jahresfrist des § 48 Abs. 4 VwVfG besteht gefestigte Rechtsprechung des BVerwG und der Oberverwaltungsgerichte. Jede konkrete Entscheidung ist vor Verwendung in juris, Beck-Online oder auf bverwg.de zu verifizieren; ohne Beleg gilt sie als `[unverifiziert – prüfen]`.

## Ausgabeformat

```
GEWERBEERLAUBNIS — <Mandat> — <Datum>

I.   Zuordnung
     Tätigkeit:               <…>
     Erlaubnisnorm:           <§ 34a / 34c Abs. 1 S. 1 Nr. … / 34d / 34f / 34i GewO>
     Zuständigkeit:           <Behörde / IHK>
     Abgrenzung § 6 GewO:     [nicht einschlägig / freier Beruf]
     Abgrenzung KWG/WpIG/KAGB: <…>

II.  Versagungsgründe
     Zuverlässigkeit § 34c Abs. 2 Nr. 1:
       Regelvermutung (5 Jahre, Katalogtaten): [greift — Widerlegung: … / greift nicht]
       Betriebsleiter geprüft:                  [ja / nein]
     Vermögensverhältnisse Nr. 2:
       Insolvenz / § 882b ZPO / § 26 Abs. 2 InsO: [eingetragen — Widerlegung: … / nein]
     Berufshaftpflicht Nr. 3 (Verwalter):       [nachgewiesen / fehlt]
     Sachkunde § 34a Abs. 1 S. 3 Nr. 3:         [nachgewiesen / fehlt]

III. Laufende Pflichten
     Weiterbildung § 34c Abs. 2a: 20 Stunden / 3 Kalenderjahre; Zeitraum <…> bis <…>
     MaBV-Pflichten:          <Sicherheitsleistung / getrennte Vermögensverwaltung / Prüfbericht>
     Registerpflichten:       <Vermittlerregister / Bewacherregister>
     Auflagen:                <…>

IV.  Bestandserlaubnis: Aufhebung
     § 35 Abs. 8 GewO:        Untersagung gesperrt — maßgeblich sind §§ 48, 49 VwVfG
     Rücknahme § 48 VwVfG:    [Erlaubnis anfänglich rechtswidrig? / nein]
     Widerruf § 49 Abs. 2 S. 1 Nr. 3 VwVfG: [nachträgliche Tatsachen / nein]
     Jahresfrist § 48 Abs. 4 VwVfG: Kenntnis am <Datum> → Frist bis <Datum>
     Vertrauensschutz:        <…>

V.   Verfahren und Rechtsschutz
     Anhörung § 28 VwVfG:     [erfolgt / unterblieben]
     Begründung § 39 VwVfG:   [tragfähig / formelhaft]
     Rechtsbehelf:            <Verpflichtungs- / Anfechtungsklage>, Frist bis <Datum>
     Sofortvollzug:           [angeordnet — § 80 Abs. 3 VwGO tragfähig? / nein]
     Bußgeldrisiko § 144 GewO: <…>

VI.  Risiko: 🟢 / 🟡 / 🔴 <Begründung>
VII. Quellenverzeichnis
```

## Risiken / typische Fehler

- **§ 35 GewO statt §§ 48, 49 VwVfG geprüft.** Bei erlaubnispflichtigen Gewerben sperrt § 35 Abs. 8 GewO die Untersagung; maßgeblich sind Rücknahme und Widerruf.
- **Jahresfrist des § 48 Abs. 4 VwVfG nicht geprüft.** Sie ist der wirksamste formale Angriffspunkt gegen Rücknahme und Widerruf.
- **Regelvermutungen als unwiderlegbar behandelt.** § 34c Abs. 2 Nr. 1 und Nr. 2 GewO formulieren Regelvermutungen; die Widerlegung erfordert konkreten Vortrag.
- **Fünfjahreszeitraum falsch gerechnet.** Er läuft rückwärts ab **Antragstellung**, nicht ab Behördenentscheidung.
- **Betriebsleiter und vertretungsberechtigte Personen nicht geprüft.** § 34c Abs. 2 Nr. 1 GewO erfasst sie ausdrücklich.
- **Falsche Erlaubnisnorm gewählt.** Die Zuordnung zwischen § 34c Nr. 1 bis 4, § 34d, § 34f und § 34i entscheidet über Zuständigkeit und Nebenpflichten; für Versicherungsvermittler ist die IHK zuständig.
- **Abgrenzung zum Aufsichtsrecht übersehen.** § 34f GewO gilt nur im Umfang der Bereichsausnahmen des KWG und des WpIG; darüber hinaus ist die BaFin-Erlaubnis erforderlich.
- **Berufshaftpflicht und Weiterbildung des Wohnimmobilienverwalters vergessen.** § 34c Abs. 2 Nr. 3 und Abs. 2a GewO sind eigenständige Pflichten mit eigenem Fristenlauf.
- **MaBV-Pflichten als bloße Formalie behandelt.** Ihre Verletzung ist bußgeldbewehrt und trägt zur Unzuverlässigkeitsprognose bei.
- **Rechtsprechung erfunden.** Jede Entscheidung ist zu belegen oder als `[unverifiziert – prüfen]` zu kennzeichnen.
