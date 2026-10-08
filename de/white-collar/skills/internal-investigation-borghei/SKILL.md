---
name: internal-investigation-borghei
title: /wirtschafts-steuerstrafrecht:internal-investigation
description: Durchführung einer unternehmensinternen Untersuchung (Internal Investigation) – Anlass und Mandatsstruktur, Arbeitnehmerbefragung im Spannungsfeld von arbeitsvertraglicher Auskunftspflicht und dem nemo-tenetur-Grundsatz, Mitbestimmung § 87 Abs. 1 Nr. 1 und Nr. 6 BetrVG, Datenschutz nach § 26 BDSG und Art. 6 DSGVO nach der EuGH-Entscheidung zu Art. 88 DSGVO, Beschlagnahmeschutz von Untersuchungsunterlagen § 97 StPO und die Kanzleidurchsuchung, Dokumentation sowie das Verhältnis zur Selbstanzeige und zur Kooperation mit der Staatsanwaltschaft. Use when ein Compliance-Verstoß intern aufzuklären, ein Interviewprogramm aufzusetzen oder das Beschlagnahmerisiko von Untersuchungsunterlagen zu bewerten ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/wirtschafts-steuerstrafrecht/skills/internal-investigation
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: white-collar
language: de
---

# /wirtschafts-steuerstrafrecht:internal-investigation

## Zweck

Eine Internal Investigation erzeugt genau das, was die Ermittlungsbehörde sonst mühsam beschaffen müsste: geordnete, ausgewertete, belastende Unterlagen. Ihr rechtlicher Kern ist deshalb nicht die Aufklärung, sondern die Frage, **wem die Ergebnisse am Ende zur Verfügung stehen**. Dieser Skill strukturiert Mandat, Befragung, Datenverarbeitung und Dokumentation so, dass Aufklärungsinteresse, Arbeitnehmerrechte und der Beschlagnahmeschutz nach § 97 StPO bewusst gegeneinander abgewogen werden — statt sich nachträglich als Fehlentscheidung zu erweisen.

## Eingaben

- Anlass: Hinweis über das Meldesystem, Prüfungsfeststellung, Presseanfrage, behördliche Maßnahme
- Mandatsstruktur: Wer beauftragt? Gesellschaft, Aufsichtsrat, Prüfungsausschuss? Sind Organe selbst betroffen?
- Betroffene Personen und deren Stellung; laufendes Ermittlungsverfahren gegen einzelne von ihnen?
- Datenquellen: E-Mail-Postfächer, Kollaborationssysteme, Zugangs- und Telefondaten, private Endgeräte
- Besteht ein Betriebsrat? Bestehende Betriebsvereinbarungen zu IT-Systemen und Kontrollen
- Zielsetzung: interne Konsequenzen, Schadensersatz, Selbstanzeige, Kooperation mit der Staatsanwaltschaft
- Bereits ergriffene Maßnahmen (Sicherung von Daten, Suspendierungen, Kommunikation)

## Sub-Agent-Architektur

Der **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) belegt Mitbestimmungstatbestände, Datenschutzgrundlagen und die Reichweite des § 97 StPO und markiert dabei die streitigen Punkte. Der **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) entwirft Untersuchungsplan, Belehrungstexte, Interviewprotokoll-Struktur und Abschlussbericht. Der **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft Mandatsstruktur, Belehrungen, Rechtsgrundlagen der Datenverarbeitung und das Beschlagnahmerisiko der erzeugten Dokumente.

## Ablauf

### 1. Anlass und Mandatsstruktur

Die Mandatsstruktur entscheidet über den späteren Schutz der Unterlagen. Zu klären ist vor dem ersten Interview:

- **Wer ist Mandant?** Die Gesellschaft, ein Organ oder ein Ausschuss? Sind Organmitglieder selbst betroffen, ist die Beauftragung durch den Aufsichtsrat oder einen unabhängigen Ausschuss vorzugswürdig, um Interessenkonflikte zu vermeiden.
- **Verteidigungsmandat oder Untersuchungsmandat?** Nur ein auf die Verteidigung eines konkret Beschuldigten gerichtetes Mandatsverhältnis kommt für den Schutz nach § 97 StPO überhaupt in Betracht. Ein reines Aufklärungsmandat ohne Verteidigungsbezug ist deutlich schwächer geschützt.
- **Ist der Verband bereits Beschuldigter oder Nebenbeteiligter?** Vor Einleitung eines Verfahrens gegen den Verband ist die Schutzlage ungünstiger.
- **Trennung der Rollen:** Untersuchungsführung und Individualverteidigung betroffener Mitarbeiter gehören nicht in dieselbe Hand (§ 43a Abs. 4 BRAO, Verbot der Vertretung widerstreitender Interessen).

### 2. Beschlagnahmeschutz und die Kanzleidurchsuchung ([§ 97 StPO](https://www.gesetze-im-internet.de/stpo/__97.html), [§ 160a StPO](https://www.gesetze-im-internet.de/stpo/__160a.html))

**Dies ist der genuin umstrittene Kernpunkt der ganzen Materie.** § 97 Abs. 1 StPO schützt schriftliche Mitteilungen zwischen dem **Beschuldigten** und den zur Zeugnisverweigerung Berechtigten sowie Aufzeichnungen der Berufsgeheimnisträger über Mitteilungen des Beschuldigten. Der Wortlaut knüpft damit an ein bestehendes **Beschuldigtenverhältnis** an.

Das Bundesverfassungsgericht hat die Verfassungsbeschwerden gegen die Durchsuchung bei Jones Day und die Sicherstellung von Unterlagen aus internen Untersuchungen zum Dieselkomplex mit Beschlüssen vom 27.06.2018 – 2 BvR 1405/17, 2 BvR 1780/17 behandelt (verifiziert über [dejure](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=2018-06-27&Aktenzeichen=2%20BvR%201405%2F17)). Die Reichweite des Beschlagnahmeschutzes für Unterlagen aus internen Untersuchungen — insbesondere bei einem Mandatsverhältnis, das vor Einleitung eines Verfahrens gegen den Verband begründet wurde, und für Interviewprotokolle — ist damit **nicht abschließend geklärt** und bleibt in Rechtsprechung und Literatur streitig `[unverifiziert – prüfen]`.

Praktische Konsequenzen für die Anlage der Untersuchung:

- Frühzeitige Klärung, ob und wann ein Beschuldigten- oder Nebenbeteiligtenstatus begründet wird.
- **Getrennte Ablage** von Verteidigungsunterlagen und rein tatsächlichen Aufklärungsdokumenten.
- Zurückhaltung bei wörtlichen Interviewprotokollen, wo eine zusammenfassende Aufzeichnung genügt — jedes Dokument ist potenzielles Beweismittel.
- Bewusste Entscheidung darüber, welche Unterlagen beim Unternehmen und welche in der Kanzlei geführt werden; § 160a StPO und § 97 StPO wirken unterschiedlich weit.
- Kein Verlass auf einen Schutz, dessen Reichweite streitig ist: Die Untersuchung ist so zu führen, dass ihre Ergebnisse auch bei Kenntnisnahme durch die Staatsanwaltschaft vertretbar bleiben.

Für die Rechtmäßigkeitsprüfung einer bereits erfolgten Maßnahme siehe [`strafrecht/skills/durchsuchung-beschlagnahme`](../../../strafrecht/skills/durchsuchung-beschlagnahme/SKILL.md).

### 3. Arbeitnehmerbefragung und der nemo-tenetur-Grundsatz

Zwei Rechtskreise treffen aufeinander:

- **Arbeitsrechtlich** besteht eine Auskunftspflicht des Arbeitnehmers aus dem Arbeitsverhältnis (§§ 611a, 241 Abs. 2 BGB), soweit die Fragen den eigenen Aufgabenbereich betreffen. Ihre Verweigerung kann arbeitsrechtliche Folgen haben.
- **Strafprozessual** gilt der Grundsatz der Selbstbelastungsfreiheit: Niemand muss zu seiner eigenen Strafverfolgung beitragen. Eine unter dem Druck arbeitsrechtlicher Sanktionen erzwungene Selbstbelastung kann im Strafverfahren einem **Verwertungsverbot** unterliegen; die Reichweite dieses Verbots ist einzelfallabhängig und nicht abschließend geklärt `[unverifiziert – prüfen]`.

Daraus folgt der praktische Standard: **Belehrung vor jedem Interview**, dokumentiert und vom Befragten gegengezeichnet. Sie muss klarstellen, dass

1. der Interviewende die **Gesellschaft** vertritt und nicht den Befragten,
2. das Gespräch **kein** anwaltliches Mandatsverhältnis zum Befragten begründet,
3. das Unternehmen über die Verwendung der Ergebnisse **allein entscheidet** und sie an Behörden weitergeben kann,
4. der Befragte das Recht hat, einen eigenen Rechtsbeistand hinzuzuziehen,
5. eine etwaige Auskunftspflicht arbeitsrechtlicher Natur ist und keine strafprozessuale Aussagepflicht begründet.

Diese Belehrung wird auch als Aufklärung über die Rollenverteilung im Interview bezeichnet. Ihr Fehlen ist der häufigste vermeidbare Fehler und beschädigt die Verwertbarkeit der Untersuchung in beide Richtungen.

### 4. Mitbestimmung des Betriebsrats ([§ 87 BetrVG](https://www.gesetze-im-internet.de/betrvg/__87.html))

- **§ 87 Abs. 1 Nr. 1 BetrVG** — Fragen der Ordnung des Betriebs und des Verhaltens der Arbeitnehmer: Regeln über Ablauf und Verpflichtung zur Teilnahme an Befragungen, Verhaltenskodizes und Meldepflichten sind mitbestimmungspflichtig.
- **§ 87 Abs. 1 Nr. 6 BetrVG** — Einführung und Anwendung technischer Einrichtungen, die dazu **bestimmt oder geeignet** sind, das Verhalten oder die Leistung der Arbeitnehmer zu überwachen: Die Auswertung von E-Mail-Postfächern, Log-, Zugangs- und Kollaborationsdaten fällt darunter. Die Eignung zur Überwachung genügt; eine Überwachungsabsicht ist nicht erforderlich.
- Mitbestimmungsfreie Einzelfallaufklärung eines konkreten Verdachts ist von der mitbestimmungspflichtigen **generellen Regelung** abzugrenzen; die Grenze ist fließend und in jedem Einzelfall zu begründen.
- Daneben: Unterrichtungs- und Beratungsrechte (§ 80 BetrVG), Beteiligung bei personellen Maßnahmen (§§ 99, 102 BetrVG) und die Anhörung vor einer Verdachtskündigung.

Ein Verstoß gegen die Mitbestimmung führt nach der **Theorie der Wirksamkeitsvoraussetzung** dazu, dass die betroffene Maßnahme dem Arbeitnehmer gegenüber unwirksam ist; ein daraus abgeleitetes Beweisverwertungsverbot ist gesondert zu prüfen `[unverifiziert – prüfen]`.

### 5. Datenschutz — § 26 BDSG und seine Fragilität ([§ 26 BDSG](https://www.gesetze-im-internet.de/bdsg_2018/__26.html), [Art. 6 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679))

§ 26 Abs. 1 S. 2 BDSG erlaubt die Verarbeitung personenbezogener Daten zur **Aufdeckung von Straftaten**, wenn zu dokumentierende tatsächliche Anhaltspunkte den Verdacht begründen, die Verarbeitung zur Aufdeckung erforderlich ist und das schutzwürdige Interesse des Beschäftigten nicht überwiegt.

**Die Vorschrift steht nicht sicher.** Der EuGH hat mit Urteil vom 30.03.2023 – C-34/21 (Hauptpersonalrat der Lehrerinnen und Lehrer) entschieden, dass mitgliedstaatliche Regelungen zur Beschäftigtendatenverarbeitung nur dann auf die Öffnungsklausel des Art. 88 DSGVO gestützt werden können, wenn sie die dort vorgesehenen spezifischen Garantien enthalten; andernfalls bleiben allein die allgemeinen Grundlagen der DSGVO anwendbar (verifiziert über [dejure](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2023-03-30&Aktenzeichen=C-34%2F21)). Die Übertragbarkeit auf § 26 BDSG wird diskutiert; einzelne Regelungen sind bereits als unionsrechtswidrig angesehen worden `[unverifiziert – prüfen]`.

**Arbeitsanweisung daraus:** Jede Verarbeitung in der Untersuchung wird mit **zwei** Rechtsgrundlagen geführt — § 26 BDSG **und** einer eigenständigen Grundlage aus Art. 6 Abs. 1 DSGVO, in der Regel Buchst. f (berechtigte Interessen) mit dokumentierter Abwägung oder Buchst. c (rechtliche Verpflichtung). Bricht die eine weg, trägt die andere. Hinzu treten:

- **Zweckbindung und Datenminimierung** (Art. 5 DSGVO): Suchbegriffe, Zeiträume und Postfächer werden vorab festgelegt und begründet.
- **Private Kommunikation** in dienstlichen Systemen: Auswertung nur nach dokumentierter Abwägung; bei erlaubter Privatnutzung erhöhtes Risiko.
- **Betroffenenrechte** (Art. 15 DSGVO) und die Grenzen ihrer Einschränkung.
- **Auftragsverarbeitung** (Art. 28 DSGVO) mit forensischen Dienstleistern; berufsrechtlich zusätzlich § 43a Abs. 2 BRAO und § 203 StGB.
- **Löschkonzept** für die im Rahmen der Untersuchung erzeugten Datenbestände.

### 6. Interviewprotokoll — Struktur

```
INTERVIEWPROTOKOLL — Internal Investigation <Projektname>
VERTRAULICH — im Auftrag der <Gesellschaft>

I.    Rahmendaten
      Datum, Uhrzeit (Beginn / Ende), Ort / Videokonferenz
      Befragte Person: <Name, Funktion, Eintrittsdatum>
      Anwesende: <Interviewer, Protokollführer, Beistand des Befragten>

II.   Belehrung (vor Beginn erteilt und bestätigt)
      1. Die Interviewenden vertreten ausschließlich die Gesellschaft.
      2. Es entsteht KEIN Mandatsverhältnis zur befragten Person.
      3. Über die Verwendung der Ergebnisse entscheidet allein die
         Gesellschaft; eine Weitergabe an Behörden ist möglich.
      4. Die befragte Person darf einen eigenen Rechtsbeistand
         hinzuziehen; das Interview kann dafür unterbrochen werden.
      5. Eine etwaige Auskunftspflicht ist arbeitsrechtlicher Natur;
         eine strafprozessuale Aussagepflicht besteht nicht.
      Bestätigung des Befragten: ______________________

III.  Gegenstand des Gesprächs
      <Sachverhaltskomplex, ohne Wertung>

IV.   Angaben der befragten Person
      <Zusammenfassende Darstellung in indirekter Rede, chronologisch;
       wörtliche Zitate nur, wo der genaue Wortlaut erheblich ist.
       Keine Bewertungen der Interviewenden im Protokoll.>

V.    Vorgehaltene Unterlagen
      <Dokument, Datum, Fundstelle; Reaktion der befragten Person>

VI.   Offene Punkte / Folgeermittlungen

VII.  Schlussvermerk
      Das Protokoll wurde der befragten Person <vorgelesen /
      zur Durchsicht überlassen>. Änderungswünsche: <…>
      Datum, Unterschrift Protokollführer
```

### 7. Verhältnis zu Selbstanzeige und Kooperation

Ergibt die Untersuchung steuerliche Verkürzungen, ist die **strafbefreiende Selbstanzeige** nach §§ 371, 398a AO zu prüfen — dazu [`steuerrecht/skills/selbstanzeige`](../../../steuerrecht/skills/selbstanzeige/SKILL.md); zur Bewertung des Tatvorwurfs [`steuerhinterziehung-370-ao`](../steuerhinterziehung-370-ao/SKILL.md). Zwei Zeitprobleme sind zu beachten: Die Sperrgründe des § 371 Abs. 2 AO können durch die Untersuchung selbst ausgelöst werden, und die Vollständigkeit der Selbstanzeige setzt eine abgeschlossene Sachverhaltsaufklärung voraus.

Die **Kooperation mit der Staatsanwaltschaft** wirkt bußgeldmindernd bei der Zumessung nach § 17 OWiG — siehe [`unternehmenssanktion-130-owig`](../unternehmenssanktion-130-owig/SKILL.md). Sie ist jedoch keine Einbahnstraße: Herausgegebene Untersuchungsergebnisse belasten regelmäßig zugleich Mitarbeiter, deren Interessen das Unternehmen nicht vertritt. Stammt der Anlass aus einer internen Meldung, sind zusätzlich die Vertraulichkeits- und Repressalienschutzpflichten des Hinweisgeberschutzrechts einzuhalten — siehe [`hinweisgeberschutz`](../../../hinweisgeberschutz/README.md).

## Quellen

### Statute

- [§ 97 StPO](https://www.gesetze-im-internet.de/stpo/__97.html), [§ 160a StPO](https://www.gesetze-im-internet.de/stpo/__160a.html), [§ 53 StPO](https://www.gesetze-im-internet.de/stpo/__53.html), [§ 102 StPO](https://www.gesetze-im-internet.de/stpo/__102.html), [§ 103 StPO](https://www.gesetze-im-internet.de/stpo/__103.html), [§ 136 StPO](https://www.gesetze-im-internet.de/stpo/__136.html)
- [§ 87 BetrVG](https://www.gesetze-im-internet.de/betrvg/__87.html), [§ 80 BetrVG](https://www.gesetze-im-internet.de/betrvg/__80.html), [§ 102 BetrVG](https://www.gesetze-im-internet.de/betrvg/__102.html)
- [§ 26 BDSG](https://www.gesetze-im-internet.de/bdsg_2018/__26.html), [Art. 6 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679), Art. 5, 15, 28 und 88 DSGVO
- [§ 43a BRAO](https://www.gesetze-im-internet.de/brao/__43a.html), [§ 203 StGB](https://www.gesetze-im-internet.de/stgb/__203.html), [§ 241 BGB](https://www.gesetze-im-internet.de/bgb/__241.html), [§ 611a BGB](https://www.gesetze-im-internet.de/bgb/__611a.html)
- [§ 371 AO](https://www.gesetze-im-internet.de/ao_1977/__371.html), [§ 398a AO](https://www.gesetze-im-internet.de/ao_1977/__398a.html), [§ 17 OWiG](https://www.gesetze-im-internet.de/owig_1968/__17.html), [§ 30 OWiG](https://www.gesetze-im-internet.de/owig_1968/__30.html)

### Kommentare

- Schmitt, in: Meyer-Goßner / Schmitt, StPO, 67. Aufl. 2024, § 97 Rn. 1 ff. und § 160a Rn. 1 ff.
- Knierim / Rübenstahl / Tsambikakis, Internal Investigations, 2. Aufl. 2016, Kap. 1 ff.
- Wybitul, Handbuch Datenschutz im Unternehmen, 2. Aufl. 2022, Rn. 1 ff. (§ 26 BDSG nach der EuGH-Rechtsprechung)
- Fitting, BetrVG, 32. Aufl. 2024, § 87 Rn. 60 ff. (technische Einrichtungen)
- Moosmayer, Compliance, 4. Aufl. 2021, Rn. 1 ff. (Untersuchungsdesign, Kooperationsentscheidung)

### Rechtsprechung

- BVerfG, Beschl. v. 27.06.2018 – 2 BvR 1405/17, 2 BvR 1780/17 (Durchsuchung bei Jones Day, Sicherstellung von Unterlagen aus interner Untersuchung) — [dejure](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=2018-06-27&Aktenzeichen=2%20BvR%201405%2F17)
- EuGH, Urt. v. 30.03.2023 – C-34/21 (Hauptpersonalrat der Lehrerinnen und Lehrer; Anforderungen des Art. 88 DSGVO an mitgliedstaatliche Regelungen zur Beschäftigtendatenverarbeitung) — [dejure](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2023-03-30&Aktenzeichen=C-34%2F21)
- Reichweite des Beschlagnahmeschutzes nach § 97 StPO für Interviewprotokolle und Untersuchungsunterlagen vor Begründung eines Beschuldigtenstatus des Verbandes: streitig `[unverifiziert – prüfen]`
- Verwertungsverbot für unter arbeitsrechtlichem Druck erlangte selbstbelastende Angaben im Strafverfahren: einzelfallabhängig `[unverifiziert – prüfen]`
- Fortgeltung einzelner Regelungen des § 26 BDSG nach der EuGH-Rechtsprechung zu Art. 88 DSGVO `[unverifiziert – prüfen]`

## Ausgabeformat

```
INTERNAL INVESTIGATION — <Projektname> — <Datum>
VERTRAULICH — § 43a Abs. 2 BRAO / § 203 StGB

Gesamtbefund: [🟢 belastbar aufgesetzt / 🟡 nachzubessern /
               🔴 Untersuchung so nicht durchführbar]

I.    Anlass und Auftraggeber       <Meldung / Prüfung / Behörde>
      Mandant                       <Gesellschaft / Aufsichtsrat>
      Interessenkonflikt § 43a BRAO [🟢 geprüft / 🔴 vorhanden]
II.   Verfahrensstand
      Beschuldigten-/Nebenbeteiligten-
      status des Verbandes          [ja seit <…> / nein]
III.  Beschlagnahmeschutz § 97 StPO
      Mandatscharakter              [Verteidigung / reine Aufklärung]
      Ablage                        [getrennt / 🔴 vermischt]
      Risikobewertung               [🟡 streitig — 2 BvR 1405/17]
IV.   Arbeitnehmerbefragung
      Belehrung erteilt             [🟢 dokumentiert / 🔴 fehlt]
      Eigener Beistand ermöglicht   [🟢 / 🔴]
      nemo-tenetur-Konflikt         <dargestellt für <…>>
V.    Mitbestimmung
      § 87 Abs. 1 Nr. 1 BetrVG      [beteiligt / nicht einschlägig]
      § 87 Abs. 1 Nr. 6 BetrVG      [beteiligt / 🔴 offen]
      Betriebsvereinbarung          <…>
VI.   Datenschutz
      § 26 BDSG                     [herangezogen]
      Art. 6 DSGVO — zweite Grundlage[Abs. 1 Buchst. <…>, Abwägung
                                     dokumentiert]
      Zweckbindung / Suchbegriffe   <…>
      Private Kommunikation         [ausgenommen / abgewogen]
      Löschkonzept                  <…>
VII.  Dokumentation                 <Protokolle, Beweismittelkette>
VIII. Folgeentscheidungen
      Selbstanzeige §§ 371, 398a AO [zu prüfen / eingeleitet]
      Kooperation § 17 OWiG         [empfohlen / abgelehnt, Gründe]
      Hinweisgeberschutz            [Vertraulichkeit gewahrt]

Empfehlung: <…>
Nächster Schritt: <…>
```

## Risiken / typische Fehler

- **Interview ohne dokumentierte Belehrung geführt.** Ohne Aufklärung über die Rollenverteilung ist die Verwertbarkeit in beide Richtungen beschädigt und der Vorwurf der Täuschung des Befragten naheliegend.
- **Untersuchungsführung und Individualverteidigung in einer Hand** — Verstoß gegen § 43a Abs. 4 BRAO und Quelle vermeidbarer Anfechtbarkeit.
- **Beschlagnahmeschutz nach § 97 StPO als gesichert unterstellt.** Die Reichweite ist streitig; die Untersuchung ist so zu führen, dass ihre Ergebnisse auch bei Kenntnisnahme durch die Staatsanwaltschaft vertretbar bleiben.
- **Wörtliche Interviewprotokolle erstellt**, wo eine zusammenfassende Aufzeichnung genügt hätte — jedes Dokument ist potenzielles Beweismittel.
- **§ 87 Abs. 1 Nr. 6 BetrVG übersehen.** Die Auswertung von E-Mail- und Logdaten unterfällt der Mitbestimmung schon bei bloßer Eignung zur Verhaltenskontrolle.
- **Datenverarbeitung allein auf § 26 BDSG gestützt.** Nach der EuGH-Entscheidung zu Art. 88 DSGVO ist jede Verarbeitung zusätzlich auf eine eigenständige Grundlage nach Art. 6 DSGVO zu stützen und die Abwägung zu dokumentieren.
- **Private Kommunikation in dienstlichen Systemen ungeprüft ausgewertet.**
- **Selbstanzeige zu spät oder unvollständig**, weil die Untersuchung selbst einen Sperrgrund des § 371 Abs. 2 AO ausgelöst hat.
- **Kooperationsentscheidung ohne Abwägung getroffen** — herausgegebene Ergebnisse belasten regelmäßig zugleich Mitarbeiter, deren Interessen das Unternehmen nicht vertritt.
- **Vertraulichkeitspflichten des Hinweisgeberschutzes verletzt**, wenn der Anlass aus einer internen Meldung stammt.
