---
name: grundbuchverfahren-borghei
title: /immobilien-grundbuchrecht:grundbuchverfahren
description: Grundbuchverfahren nach der GBO – Eintragungsantrag § 13 GBO, formelles Konsensprinzip und Eintragungsbewilligung § 19 GBO, Nachweisform § 29 GBO, Voreintragungsgrundsatz § 39 GBO und die MoPeG-Falle des § 47 Abs. 2 GBO für die eingetragene GbR, Rangverhältnisse §§ 879–881 BGB einschließlich Rangvorbehalt und Rangänderung, Eintragungsfähigkeit, Grundbuchberichtigung § 22 GBO, Amtswiderspruch § 53 GBO und Widerspruch § 899 BGB, Zwischenverfügung § 18 GBO sowie Beschwerde § 71 GBO. Use when ein Grundbuchantrag vorbereitet, eine Zwischenverfügung oder Zurückweisung des Grundbuchamts beantwortet oder eine unrichtige Eintragung berichtigt werden soll.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/immobilien-grundbuchrecht/skills/grundbuchverfahren
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: real-estate
language: de
---

# /immobilien-grundbuchrecht:grundbuchverfahren

## Zweck

Das Grundbuchamt prüft nicht, ob die Beteiligten materiell recht haben — es prüft, ob ihm die **formellen** Voraussetzungen in der gesetzlich vorgeschriebenen Form nachgewiesen sind. Wer diesen Unterschied nicht sauber trennt, produziert Zwischenverfügungen, verliert Rang und blockiert die Kaufpreisfälligkeit. Dieser Skill stellt den eintragungsfähigen Antrag zusammen, prüft ihn gegen die Formalprüfung des Grundbuchamts und ordnet die Rechtsbehelfe gegen Zwischenverfügung und Zurückweisung ein.

## Eingaben

- **Beantragte Eintragung**: Eigentumswechsel, Vormerkung, Grundschuld, Dienstbarkeit, Nießbrauch, Löschung, Berichtigung, Widerspruch
- **Grundbuchblatt**: Amtsgericht, Grundbuchbezirk, Blattnummer, Bestandsverzeichnis und Abteilungen I–III im aktuellen Auszug
- **Beteiligte** und ihre Rechtsform: natürliche Person, GmbH/AG (Handelsregisterauszug), **eGbR (Gesellschaftsregister)**, Erbengemeinschaft, Betreuter, Minderjähriger
- Vorliegende **Erklärungen**: Bewilligung, Auflassung, Löschungsbewilligung, Rangrücktritt — jeweils in welcher Form
- Nachweise: Erbschein / Europäisches Nachlasszeugnis / notarielles Testament mit Eröffnungsprotokoll, Vollmachten, Genehmigungen
- Bereits ergangene **Zwischenverfügung** oder Zurückweisung mit Datum des Zugangs
- Gewünschter **Rang** und bereits eingetragene Rechte

## Sub-Agent-Architektur

1. **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) beschafft GBO, GBV, BGB-Sachenrecht und MoPeG-Folgeregelungen mit URL sowie die Kommentarstellen (Demharter, Schöner/Stöber, Bauer/Schaub).
2. **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) formuliert Antrag, Bewilligung und gegebenenfalls Beschwerdeschrift.
3. **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft Form § 29 GBO, Voreintragung, Rangangaben und Beschwerdefristen.

## Ablauf

### 1. Eintragungsantrag ([§ 13 GBO](https://www.gesetze-im-internet.de/gbo/__13.html))

Eine Eintragung erfolgt grundsätzlich nur **auf Antrag**. Antragsberechtigt ist, wessen Recht von der Eintragung betroffen wird, und derjenige, zu dessen Gunsten die Eintragung erfolgen soll; der Notar gilt bei beurkundeten Erklärungen als ermächtigt (§ 15 GBV). Maßgeblich für den **Rang** ist der Zeitpunkt des Eingangs beim Grundbuchamt — der Antrag ist deshalb mit Uhrzeit zu registrieren. Der Antrag kann bedingt gestellt werden, soweit die Bedingung im Grundbuchverfahren selbst liegt (etwa: Eintragung nur bei bestimmtem Rang); im Übrigen ist er bedingungsfeindlich.

### 2. Formelles Konsensprinzip ([§ 19 GBO](https://www.gesetze-im-internet.de/gbo/__19.html))

Eine Eintragung erfolgt, wenn derjenige sie **bewilligt**, dessen Recht von ihr betroffen wird. Das Grundbuchamt prüft **nicht** die materielle Einigung, sondern allein die Bewilligung des Betroffenen — das ist das **formelle Konsensprinzip**. Ausnahme ist der Eigentumswechsel: Hier verlangt [§ 20 GBO](https://www.gesetze-im-internet.de/gbo/__20.html) zusätzlich den Nachweis der **Auflassung**, also der materiellen Einigung (materielles Konsensprinzip). Die Bewilligung ist eine einseitige, dem Grundbuchamt gegenüber abzugebende Verfahrenserklärung; sie ist **bedingungsfeindlich** und grundsätzlich unwiderruflich, sobald sie beim Grundbuchamt eingegangen ist.

### 3. Form der Nachweise ([§ 29 GBO](https://www.gesetze-im-internet.de/gbo/__29.html))

Eintragungen erfolgen nur, wenn die erforderlichen Erklärungen durch **öffentliche oder öffentlich beglaubigte Urkunden** nachgewiesen sind; andere Voraussetzungen sind, soweit sie nicht offenkundig sind, ebenfalls in dieser Form zu belegen. Praktisch heißt das: Beglaubigung der Unterschrift genügt für die Bewilligung, für die Auflassung ist Beurkundung erforderlich. Vertretungsmacht wird durch beglaubigte Vollmacht, Handelsregisterauszug oder — bei der GbR — durch den Gesellschaftsregisterauszug nachgewiesen. Eine privatschriftliche Erklärung ist im Grundbuchverfahren **wertlos**, so eindeutig sie inhaltlich sein mag.

### 4. Voreintragungsgrundsatz und die MoPeG-Falle ([§ 39 GBO](https://www.gesetze-im-internet.de/gbo/__39.html), [§ 47 Abs. 2 GBO](https://www.gesetze-im-internet.de/gbo/__47.html))

Eine Eintragung soll nur erfolgen, wenn der **Betroffene selbst als Berechtigter eingetragen ist** (§ 39 Abs. 1 GBO). Wer verfügen will, muss also zuvor im Grundbuch stehen; Ausnahmen gelten für die Erbfolge nach [§ 40 GBO](https://www.gesetze-im-internet.de/gbo/__40.html), wenn der Erbe das Recht überträgt oder aufhebt.

**Seit dem 01.01.2024 (MoPeG) gilt für die Gesellschaft bürgerlichen Rechts eine zweite, eigenständige Hürde:** Nach § 47 Abs. 2 GBO soll für eine Gesellschaft bürgerlichen Rechts ein Recht nur eingetragen werden, wenn sie **im Gesellschaftsregister eingetragen** ist. Das ist die zentrale Transaktionsfalle der Gegenwart:

- Eine GbR, die vor 2024 als Eigentümerin mit ihren Gesellschaftern im Grundbuch steht, kann **nicht wirksam verfügen**, ohne sich zuvor als **eGbR** im Gesellschaftsregister eintragen und im Grundbuch entsprechend berichtigen zu lassen.
- Betroffen sind auch der **Erwerb** durch eine GbR, die Bestellung einer Grundschuld, die Bewilligung einer Vormerkung und jede Löschung.
- Zeitplanung: Die Registeranmeldung ist notariell zu beglaubigen und braucht Vorlauf. Wird sie erst beim Beurkundungstermin bemerkt, verzögert sich die gesamte Abwicklung um Wochen.
- Prüfroutine: Steht auf einer Seite des Geschäfts eine GbR, ist **vor Terminierung** zu klären, ob sie bereits eGbR mit Registernummer ist.

### 5. Eintragungsfähigkeit und Bestimmtheit

Eingetragen werden können nur **dingliche Rechte und gesetzlich zugelassene Vermerke** — nicht schuldrechtliche Abreden. Eintragungsfähig sind insbesondere Eigentum, Erbbaurecht, Dienstbarkeiten, Nießbrauch, Reallast, Vorkaufsrecht, Hypothek, Grund- und Rentenschuld, Vormerkung, Widerspruch, Verfügungsbeschränkungen. Nicht eintragungsfähig sind etwa Mietverträge, Nutzungsabreden ohne dinglichen Gehalt oder Zahlungspflichten. Der Inhalt muss **bestimmt** sein; zur Ergänzung darf auf die Eintragungsbewilligung Bezug genommen werden ([§ 874 BGB](https://www.gesetze-im-internet.de/bgb/__874.html)), der wesentliche Rechtsinhalt muss aber aus dem Grundbuch selbst hervorgehen.

### 6. Rangverhältnisse ([§ 879 BGB](https://www.gesetze-im-internet.de/bgb/__879.html), [§ 880 BGB](https://www.gesetze-im-internet.de/bgb/__880.html), [§ 881 BGB](https://www.gesetze-im-internet.de/bgb/__881.html))

Das Rangverhältnis mehrerer Rechte in **derselben Abteilung** bestimmt sich nach der Reihenfolge der Eintragungen, bei Eintragungen in **verschiedenen Abteilungen** nach dem Datum; bei gleichem Datum haben die Rechte gleichen Rang (§ 879 Abs. 1 BGB). Abweichende Rangbestimmungen sind zulässig, müssen aber eingetragen werden (§ 879 Abs. 3 BGB).

- **Rangänderung** (§ 880 BGB): Einigung der beteiligten Berechtigten und Eintragung; steht ein Zwischenrecht entgegen, bleibt dessen Rang unberührt. Ist das zurücktretende Recht eine Hypothek oder Grundschuld, ist die Zustimmung des Eigentümers erforderlich.
- **Rangvorbehalt** (§ 881 BGB): Der Eigentümer behält sich bei der Belastung vor, ein anderes, dem Umfang nach bestimmtes Recht mit dem Rang vor dem eingetragenen Recht einzutragen. Ohne Eintragung des Vorbehalts wirkt er nicht.

### 7. Grundbuchberichtigung ([§ 22 GBO](https://www.gesetze-im-internet.de/gbo/__22.html)) und Widerspruch ([§ 899 BGB](https://www.gesetze-im-internet.de/bgb/__899.html))

Ist das Grundbuch **unrichtig** — die Buchlage weicht von der materiellen Rechtslage ab —, wird es entweder mit Bewilligung des Betroffenen oder durch **Unrichtigkeitsnachweis** in der Form des § 29 GBO berichtigt (§ 22 Abs. 1 GBO). Typischer Fall ist die Erbfolge: Nachweis durch Erbschein oder durch notarielles Testament nebst Eröffnungsniederschrift.

Solange die Berichtigung nicht erfolgt ist, sichert der **Widerspruch** nach § 899 BGB: Er zerstört den **öffentlichen Glauben** des Grundbuchs ([§ 892 BGB](https://www.gesetze-im-internet.de/bgb/__892.html)) und verhindert damit den gutgläubigen Erwerb durch Dritte. Er wird auf Bewilligung des Betroffenen oder aufgrund **einstweiliger Verfügung** eingetragen — ein Verfügungsgrund muss dafür nicht glaubhaft gemacht werden. Erkennt das Grundbuchamt, dass es unter Verletzung gesetzlicher Vorschriften eine unrichtige Eintragung vorgenommen hat, trägt es von Amts wegen einen **Amtswiderspruch** nach [§ 53 GBO](https://www.gesetze-im-internet.de/gbo/__53.html) ein.

### 8. Zwischenverfügung und Beschwerde ([§ 18 GBO](https://www.gesetze-im-internet.de/gbo/__18.html), [§ 71 GBO](https://www.gesetze-im-internet.de/gbo/__71.html))

Steht dem Antrag ein **behebbares Hindernis** entgegen, weist das Grundbuchamt den Antrag nicht sofort zurück, sondern erlässt eine **Zwischenverfügung** mit Fristsetzung; wird das Hindernis fristgerecht behoben, bleibt der **ursprüngliche Rang** erhalten (§ 18 Abs. 1 GBO). Das ist der Grund, weshalb eine Zwischenverfügung ernst zu nehmen und die Frist zu notieren ist. Unzulässig ist eine Zwischenverfügung, mit der ein von Anfang an fehlendes materielles Erfordernis nachgeschoben werden soll — dann ist zurückzuweisen.

Gegen Entscheidungen des Grundbuchamts findet die **Beschwerde** zum Oberlandesgericht statt (§ 71 Abs. 1 GBO); sie ist **nicht fristgebunden**, gegen erfolgte Eintragungen aber nur mit dem Ziel eines Amtswiderspruchs oder einer Amtslöschung zulässig (§ 71 Abs. 2 GBO). Das Grundbuchamt kann abhelfen ([§ 75 GBO](https://www.gesetze-im-internet.de/gbo/__75.html)). Gegen die Zwischenverfügung ist die Beschwerde statthaft; parallel sollte das Hindernis vorsorglich behoben werden, um den Rang nicht zu gefährden.

## Deterministische Berechnung

Die vom Grundbuchamt gesetzten Fristen der Zwischenverfügung sind **Ereignisfristen** nach [§ 187 Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__187.html); das Fristende verschiebt sich nach [§ 193 BGB](https://www.gesetze-im-internet.de/bgb/__193.html) auf den nächsten Werktag. Der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) macht **nur die Arithmetik** — der Zugang der Zwischenverfügung ist juristische Eingabe und gesondert nachzuweisen.

```bash
# Frist einer Zwischenverfügung § 18 GBO: Zugang 15.01.2026, vier Wochen
python -m scripts.legal_calc.cli frist --ereignis 15.01.2026 --menge 4 --einheit wochen --land BY

# Vorlauf für die Anmeldung zum Gesellschaftsregister vor dem Beurkundungstermin
python -m scripts.legal_calc.cli frist --ereignis 15.01.2026 --menge 2 --einheit wochen --land BY
```

`--json` liefert die Rechenschritte samt Normzitat. **Grundbuchkosten** richten sich nach dem GNotKG; ein GNotKG-Modul ist **nicht implementiert** — die Gebühren sind gegen KV GNotKG von Hand zu ermitteln.

## Quellen

### Statute

- [§ 13 GBO](https://www.gesetze-im-internet.de/gbo/__13.html), [§ 18 GBO](https://www.gesetze-im-internet.de/gbo/__18.html), [§ 19 GBO](https://www.gesetze-im-internet.de/gbo/__19.html), [§ 20 GBO](https://www.gesetze-im-internet.de/gbo/__20.html), [§ 22 GBO](https://www.gesetze-im-internet.de/gbo/__22.html), [§ 29 GBO](https://www.gesetze-im-internet.de/gbo/__29.html)
- [§ 39 GBO](https://www.gesetze-im-internet.de/gbo/__39.html), [§ 40 GBO](https://www.gesetze-im-internet.de/gbo/__40.html), [§ 47 GBO](https://www.gesetze-im-internet.de/gbo/__47.html), [§ 53 GBO](https://www.gesetze-im-internet.de/gbo/__53.html), [§ 71 GBO](https://www.gesetze-im-internet.de/gbo/__71.html), [§ 75 GBO](https://www.gesetze-im-internet.de/gbo/__75.html)
- [§ 874 BGB](https://www.gesetze-im-internet.de/bgb/__874.html), [§ 879 BGB](https://www.gesetze-im-internet.de/bgb/__879.html), [§ 880 BGB](https://www.gesetze-im-internet.de/bgb/__880.html), [§ 881 BGB](https://www.gesetze-im-internet.de/bgb/__881.html), [§ 892 BGB](https://www.gesetze-im-internet.de/bgb/__892.html), [§ 899 BGB](https://www.gesetze-im-internet.de/bgb/__899.html)
- [§ 707 BGB](https://www.gesetze-im-internet.de/bgb/__707.html) (Gesellschaftsregister der eGbR, MoPeG)

### Kommentare

- Demharter, GBO, 33. Aufl. 2023, § 19 Rn. 1 ff.; § 29 Rn. 1 ff.; § 39 Rn. 1 ff.
- Schöner/Stöber, Grundbuchrecht, 16. Aufl. 2020, Rn. 1 ff. (Antrag, Bewilligung, Rang)
- Bauer/Schaub, GBO, 5. Aufl. 2023, § 47 Rn. 1 ff. (GbR nach MoPeG)
- Kohler, in: MüKoBGB, 9. Aufl. 2023, § 879 Rn. 1 ff.; § 899 Rn. 1 ff.

### Rechtsprechung

- Zur Reichweite des Voreintragungsgrundsatzes und zur Behandlung der GbR im Grundbuch nach dem MoPeG bildet sich die obergerichtliche Rechtsprechung erst seit dem 01.01.2024 heraus; einschlägige OLG-Beschlüsse sind vor Verwendung in juris zu recherchieren `[unverifiziert - prüfen]`.
- Zur Unzulässigkeit einer Zwischenverfügung, die ein von Anfang an fehlendes materielles Erfordernis nachschieben soll, ist die einschlägige BGH- und OLG-Rechtsprechung heranzuziehen `[unverifiziert - prüfen]`. Kein Aktenzeichen ohne eigene Verifikation in juris / Beck-Online übernehmen.

## Formulierungshilfe — Grundbuchantrag und Widerspruchsantrag

```
An das Amtsgericht <Ort> — Grundbuchamt —
Grundbuch von <Gemarkung>, Blatt <Nr.>

Namens und in Vollmacht der Beteiligten beantrage ich:

1. In Abteilung II einzutragen: Auflassungsvormerkung gemäß § 883 BGB
   für <Käufer, Name, Geburtsdatum>, im Rang nach <…> und im Übrigen an
   erster Rangstelle.

2. In Abteilung III einzutragen: Grundschuld ohne Brief über
   <Betrag> EUR nebst <…> % Jahreszinsen für <Gläubigerin>.

3. In Abteilung I den Eigentumswechsel auf <Käufer> einzutragen.

Die Eintragungsbewilligungen der Betroffenen sowie die Auflassung sind in
der beigefügten notariellen Urkunde vom <Datum>, UR-Nr. <…>, enthalten
(§§ 19, 20 GBO). Die Form des § 29 GBO ist gewahrt.

Der Voreintragungsgrundsatz des § 39 GBO ist gewahrt; die veräußernde
Gesellschaft ist seit dem <Datum> unter <Registergericht, GsR <Nr.>> im
Gesellschaftsregister eingetragen (§ 47 Abs. 2 GBO). Ein aktueller
Registerausdruck liegt bei.

Die Anträge zu 1. bis 3. werden in dieser Reihenfolge und nur gemeinsam
gestellt; Teilvollzug wird ausdrücklich nicht beantragt.
```

```
Antrag auf Eintragung eines Widerspruchs (§ 899 BGB)

Das Grundbuch ist unrichtig, weil <Darstellung der materiellen Rechtslage>.
Zur Erhaltung des Rechts der Antragstellerin und zur Verhinderung eines
gutgläubigen Erwerbs Dritter (§ 892 BGB) wird beantragt, gegen die
Richtigkeit der Eintragung in Abteilung <…> lfd. Nr. <…> einen Widerspruch
zugunsten der Antragstellerin einzutragen. Die Bewilligung des Betroffenen
liegt vor / wird durch einstweilige Verfügung des Landgerichts <Ort> vom
<Datum>, Az. <…>, ersetzt.
```

## Ausgabeformat

```
GRUNDBUCHVERFAHREN — <Antrag / Zwischenverfügung / Berichtigung> — <Datum>

I.    Grundbuch / Beteiligte      <AG, Gemarkung, Blatt>
II.   Beantragte Eintragung       <Art, Abteilung, Inhalt>
III.  Antrag § 13 GBO             [✅]  Eingang / Rangzeitpunkt: <Datum, Uhrzeit>
IV.   Bewilligung § 19 GBO        [✅ / ❌]   Auflassung § 20 GBO [✅ / N/A]
V.    Form § 29 GBO               [öffentlich / beglaubigt / 🔴 privatschriftlich]
      - Vertretungsnachweis       [HR-Auszug / GsR-Auszug / Vollmacht]
VI.   Voreintragung § 39 GBO      [✅ / ❌]
      eGbR § 47 Abs. 2 GBO        [nicht einschlägig / eingetragen GsR <Nr.>
                                   / 🔴 GbR nicht registriert — Termin schieben]
VII.  Eintragungsfähigkeit        [✅ / ❌ schuldrechtlich]  Bestimmtheit [✅ / ⚠️]
VIII. Rang §§ 879–881 BGB         Gewünscht: <…>  Zwischenrechte: <…>
      Rangvorbehalt / Rangänderung [N/A / eingetragen]
IX.   Berichtigung § 22 GBO       [N/A / Bewilligung / Unrichtigkeitsnachweis]
      Widerspruch § 899 BGB       [N/A / beantragt / Amtswiderspruch § 53 GBO]
X.    Zwischenverfügung § 18 GBO  Zugang <Datum>  Frist bis <Datum>
      Beschwerde § 71 GBO         [nicht erforderlich / eingelegt am <Datum>]

Ergebnis: <eintragungsreif / Hindernis behebbar / nicht eintragungsfähig>
Rangrisiko: [🟢 / 🟡 / 🔴]
```

## Risiken / typische Fehler

- **GbR ohne Eintragung im Gesellschaftsregister** — seit dem 01.01.2024 sperrt § 47 Abs. 2 GBO jede Eintragung; wird das erst im Beurkundungstermin bemerkt, kippt der gesamte Zeitplan.
- **Voreintragungsgrundsatz übersehen** — der Verfügende steht noch nicht im Grundbuch; ohne den Ausnahmefall des § 40 GBO ist zuerst zu berichtigen.
- **Form des § 29 GBO verfehlt** — privatschriftliche Bewilligung, unbeglaubigte Vollmacht oder veralteter Registerauszug; inhaltlich richtig, verfahrensrechtlich wertlos.
- **Formelles und materielles Konsensprinzip verwechselt** — das Grundbuchamt prüft die Bewilligung, beim Eigentumswechsel zusätzlich die Auflassung, aber nie den Kaufvertrag.
- **Rang nicht ausdrücklich bestimmt** — ohne Rangangabe entscheidet die Eingangsreihenfolge; ein Rangvorbehalt wirkt nur, wenn er eingetragen ist.
- **Frist der Zwischenverfügung versäumt** — mit der Zurückweisung geht der ursprüngliche Rangzeitpunkt verloren; die Beschwerde nach § 71 GBO heilt das nicht rückwirkend.
- **Widerspruch zu spät** — bis zur Eintragung des Widerspruchs bleibt der gutgläubige Erwerb nach § 892 BGB möglich; der Berichtigungsantrag allein sperrt ihn nicht.
