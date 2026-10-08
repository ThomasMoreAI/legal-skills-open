---
name: reiseruecktritt-insolvenzschutz-borghei
title: /reise-fluggastrecht:reiseruecktritt-insolvenzschutz
description: Rücktritt vor Reisebeginn und Absicherung der Vorauszahlungen – Rücktrittsrecht des Reisenden § 651h Abs. 1 BGB, Entschädigungspauschalen § 651h Abs. 2 BGB und ihre AGB-Kontrolle, kostenfreier Rücktritt bei unvermeidbaren außergewöhnlichen Umständen § 651h Abs. 3 BGB, Rücktritt des Veranstalters § 651h Abs. 4 BGB, Umbuchung, Preiserhöhung § 651f BGB mit der 8-Prozent-Grenze und dem Kündigungsrecht § 651g BGB, Insolvenzabsicherung § 651r BGB und Sicherungsschein § 651s BGB, Reisesicherungsfonds. Use when ein Reisender vor Reisebeginn zurücktreten will, eine Preiserhöhung oder Vertragsänderung erhält oder die Insolvenzsicherung des Veranstalters zu prüfen ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/reise-fluggastrecht/skills/reiseruecktritt-insolvenzschutz
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: consumer
language: de
---

# /reise-fluggastrecht:reiseruecktritt-insolvenzschutz

## Zweck

Der Skill klärt die teuerste Frage vor Reisebeginn: Kostet der Rücktritt eine Entschädigung — oder ist er nach § 651h Abs. 3 BGB kostenfrei? Er prüft daneben Preiserhöhung und Vertragsänderung als eigenständige Ausstiegswege und sichert die Absicherung der Vorauszahlungen über Sicherungsschein und Insolvenzschutz. Die Kasuistik zu den unvermeidbaren außergewöhnlichen Umständen ist streitig; der Skill markiert sie entsprechend, statt Scheinsicherheit zu erzeugen.

## Eingaben

- Reiseveranstalter, Buchungsnummer, Buchungsdatum, Reisezeitraum, Gesamtreisepreis
- Reiseziel und geplante Reiseroute
- Reisebedingungen mit Staffel der Entschädigungspauschalen
- Anlass des Rücktritts mit Datum, Quelle und Reichweite (behördliche Warnung, Ereignis vor Ort, persönlicher Grund)
- Etwaige Preiserhöhung oder Vertragsänderung mit Datum, Höhe und Begründung
- Geleistete Anzahlungen und vorliegender Sicherungsschein
- Reiserücktrittsversicherung vorhanden?

## Sub-Agent-Architektur

Ein Researcher bestimmt den Vertragstyp, beschafft die Reisebedingungen und sammelt Normen sowie EuGH- und BGH-Rechtsprechung zum Rücktrittsrecht. Ein Drafter trennt den Rücktritt gegen Entschädigung von dem kostenfreien Rücktritt, bestimmt den Prognosezeitpunkt und entwirft die Rücktrittserklärung. Ein Reviewer prüft die Fristen, die AGB-Kontrolle der Pauschalen, den Sicherungsschein und jede Fundstelle; Streitiges wird mit `[unverifiziert - prüfen]` markiert.

## Ablauf

### 1. Vertragstyp und Rücktrittsrecht ([§ 651h BGB](https://www.gesetze-im-internet.de/bgb/__651h.html))

Zunächst ist zu klären, ob ein Pauschalreisevertrag nach [§ 651a BGB](https://www.gesetze-im-internet.de/bgb/__651a.html) vorliegt; nur dann greift § 651h BGB. Bei verbundenen Reiseleistungen ([§ 651w BGB](https://www.gesetze-im-internet.de/bgb/__651w.html)) und bei Einzelbuchungen richtet sich der Ausstieg nach dem jeweiligen Einzelvertrag und dessen Bedingungen.

Der Reisende kann nach § 651h Abs. 1 BGB **jederzeit vor Reisebeginn** vom Vertrag zurücktreten (§ 651h Abs. 1 S. 1 BGB) — ein Grund ist nicht erforderlich. Die Erklärung ist empfangsbedürftig; der **Zugang** ist zu dokumentieren, weil sich die Höhe der Entschädigung nach dem Zeitpunkt des Zugangs richtet.

### 2. Entschädigung und Pauschalen ([§ 651h Abs. 2 BGB](https://www.gesetze-im-internet.de/bgb/__651h.html))

Der Veranstalter verliert den Anspruch auf den Reisepreis, kann aber eine **angemessene Entschädigung** verlangen (§ 651h Abs. 1 S. 3 BGB). Ihre Höhe bestimmt sich nach dem Reisepreis abzüglich ersparter Aufwendungen und abzüglich dessen, was durch anderweitige Verwendung der Reiseleistungen erworben wird.

Nach § 651h Abs. 2 BGB dürfen im Vertrag **angemessene Entschädigungspauschalen** festgelegt werden, gestaffelt nach dem Zeitraum zwischen Rücktritt und Reisebeginn sowie nach den erwarteten Ersparnissen und Erwerben. Zwei Konsequenzen:

- Die Pauschale ist an § 651h Abs. 2 BGB und an der AGB-Kontrolle der [§§ 307 ff. BGB](https://www.gesetze-im-internet.de/bgb/__307.html) zu messen. Eine Staffel, die die realistischen Ersparnisse ersichtlich ignoriert, ist angreifbar.
- Der Reisende kann nach § 651h Abs. 2 S. 2 BGB **nachweisen**, dass dem Veranstalter kein oder ein wesentlich geringerer Schaden entstanden ist. Diese Gegenrechnung wird in der Praxis fast nie geführt und ist der wirksamste Hebel gegen hohe Pauschalen.

### 3. Kostenfreier Rücktritt bei unvermeidbaren außergewöhnlichen Umständen ([§ 651h Abs. 3 BGB](https://www.gesetze-im-internet.de/bgb/__651h.html))

Der Reisende kann **ohne Entschädigung** zurücktreten, wenn am Bestimmungsort oder in dessen unmittelbarer Nähe **unvermeidbare, außergewöhnliche Umstände** auftreten, die die Durchführung der Pauschalreise oder die Beförderung von Personen an den Bestimmungsort **erheblich beeinträchtigen**. Umstände sind unvermeidbar und außergewöhnlich, wenn sie nicht der Kontrolle der Partei unterliegen, die sich darauf beruft, und sich ihre Folgen auch dann nicht hätten vermeiden lassen, wenn alle zumutbaren Vorkehrungen getroffen worden wären.

Prüfungsschritte:

1. **Ort**: am Bestimmungsort oder in dessen unmittelbarer Nähe — nicht am Wohnort des Reisenden. Rein persönliche Gründe (Krankheit, beruflicher Grund) fallen **nicht** unter Abs. 3; dafür ist die Reiserücktrittsversicherung da.
2. **Prognosezeitpunkt**: maßgeblich ist die Sachlage im Zeitpunkt des Rücktritts, bezogen auf den geplanten Reisezeitraum. Ein späterer Wegfall der Lage schadet nicht; ein bloßes Unbehagen genügt nicht.
3. **Erhebliche Beeinträchtigung**: erforderlich ist eine konkrete, ins Gewicht fallende Betroffenheit der gebuchten Leistungen oder der Anreise.
4. **Behördliche Reisewarnungen** sind ein starkes Indiz, aber nicht mehr — sie ersetzen die Einzelfallprüfung nicht `[unverifiziert - prüfen]`.

Die **Pandemie-Kasuistik** ist einschlägig und in wesentlichen Punkten streitig geblieben: Reichweite von Reisewarnungen, Behandlung von Quarantäne- und Testpflichten, Zeitpunkt der Prognose, Zulässigkeit von Gutscheinlösungen. Der EuGH hat für den Pauschalreisebereich klargestellt, dass die Erstattung in Geld geschuldet ist und die nationale Gutscheinpraxis daran zu messen war (EuGH, Urt. v. 08.06.2023 – C-407/21, EuZW 2023, 709) ([dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2023-06-08&Aktenzeichen=C-407/21)), Reichweite im Einzelfall zu prüfen `[unverifiziert - prüfen]`.

Nach Abs. 3 S. 2 hat der Veranstalter die geleisteten Zahlungen unverzüglich, spätestens innerhalb von 14 Tagen nach dem Rücktritt, zu erstatten.

### 4. Rücktritt des Veranstalters ([§ 651h Abs. 4 BGB](https://www.gesetze-im-internet.de/bgb/__651h.html))

Der Veranstalter kann vor Reisebeginn zurücktreten, wenn die Mindestteilnehmerzahl nicht erreicht wird (unter den dort genannten Ankündigungs- und Fristbedingungen) oder wenn unvermeidbare außergewöhnliche Umstände ihn an der Durchführung hindern. Er hat dann den Reisepreis unverzüglich, spätestens binnen 14 Tagen, zu erstatten; ein Anspruch auf Entschädigung steht ihm nicht zu. Schadensersatzansprüche des Reisenden entfallen in diesen Fällen.

### 5. Preiserhöhung und die 8-Prozent-Grenze ([§ 651f BGB](https://www.gesetze-im-internet.de/bgb/__651f.html))

Eine Preiserhöhung ist nur wirksam, wenn der Vertrag sie ausdrücklich vorsieht, den Reisenden zugleich auf eine entsprechende **Preissenkung** verpflichtet und die Berechnung der Anpassung angibt. Zulässige Anknüpfungspunkte sind Beförderungskosten, Steuern und Abgaben sowie Wechselkurse. Die Erhöhung ist dem Reisenden **klar und verständlich** in Textform mitzuteilen, und zwar spätestens 20 Tage vor Reisebeginn.

**Übersteigt die Erhöhung 8 % des Reisepreises**, kann der Veranstalter sie nicht einseitig durchsetzen; er kann sie dem Reisenden nur nach [§ 651g BGB](https://www.gesetze-im-internet.de/bgb/__651g.html) als **erhebliche Vertragsänderung** anbieten. Der Reisende kann dann innerhalb der gesetzten angemessenen Frist das Angebot annehmen, eine angebotene Ersatzreise wählen oder **kostenfrei vom Vertrag zurücktreten**. Schweigen gilt nach der gesetzlichen Konstruktion als Annahme nur, wenn der Veranstalter ordnungsgemäß belehrt hat — die Belehrung ist deshalb stets zu prüfen.

Dasselbe Regime gilt für sonstige erhebliche Vertragsänderungen (Hotelwechsel in geringere Kategorie, wesentliche Änderung der Reisezeiten, Zielortwechsel).

### 6. Umbuchung ([§ 651e BGB](https://www.gesetze-im-internet.de/bgb/__651e.html))

Ein gesetzlicher Anspruch auf Umbuchung besteht nicht; die Umbuchung ist eine einvernehmliche Vertragsänderung, für die die Reisebedingungen regelmäßig ein Entgelt vorsehen. Gesetzlich geregelt ist dagegen die **Übertragung des Vertrags auf einen Dritten** nach § 651e BGB: Der Reisende kann innerhalb einer angemessenen Frist vor Reisebeginn erklären, dass ein Dritter in den Vertrag eintritt; Veranstalter und eintretender Dritter haften als Gesamtschuldner für Reisepreis und Mehrkosten. Das ist häufig die günstigere Alternative zum Rücktritt.

### 7. Insolvenzabsicherung und Sicherungsschein ([§ 651r BGB](https://www.gesetze-im-internet.de/bgb/__651r.html), [§ 651s BGB](https://www.gesetze-im-internet.de/bgb/__651s.html))

Der Veranstalter muss sicherstellen, dass dem Reisenden der gezahlte Reisepreis erstattet wird, soweit Reiseleistungen infolge seiner **Insolvenz** ausfallen, und dass notwendige Aufwendungen für die Rückbeförderung erstattet werden. Die Absicherung erfolgt durch Absicherungsvertrag mit einem Kundengeldabsicherer oder — für umsatzstarke Veranstalter — über den **Reisesicherungsfonds** nach dem RSFG `[unverifiziert - prüfen]`.

- **Sicherungsschein** (§ 651s BGB): Der Veranstalter hat dem Reisenden die Absicherung durch unmittelbaren Anspruch gegen den Absicherer zu verschaffen und ihm einen Sicherungsschein zu übergeben.
- **Zahlungssperre** ([§ 651t BGB](https://www.gesetze-im-internet.de/bgb/__651t.html)): Zahlungen auf den Reisepreis vor Beendigung der Reise darf der Veranstalter nur fordern oder annehmen, wenn die Absicherung besteht und dem Reisenden der Sicherungsschein übergeben ist. **Ohne Sicherungsschein keine Anzahlung** — dies ist der praktisch wichtigste Prüfpunkt bei kleinen und ausländischen Veranstaltern.
- Vermittler dürfen nach § 651t BGB Zahlungen nur unter denselben Voraussetzungen entgegennehmen.

## Quellen

### Statute

- [§ 651a BGB](https://www.gesetze-im-internet.de/bgb/__651a.html), [§ 651e BGB](https://www.gesetze-im-internet.de/bgb/__651e.html), [§ 651f BGB](https://www.gesetze-im-internet.de/bgb/__651f.html), [§ 651g BGB](https://www.gesetze-im-internet.de/bgb/__651g.html), [§ 651h BGB](https://www.gesetze-im-internet.de/bgb/__651h.html), [§ 651r BGB](https://www.gesetze-im-internet.de/bgb/__651r.html), [§ 651s BGB](https://www.gesetze-im-internet.de/bgb/__651s.html), [§ 651t BGB](https://www.gesetze-im-internet.de/bgb/__651t.html), [§ 651w BGB](https://www.gesetze-im-internet.de/bgb/__651w.html), [§ 651y BGB](https://www.gesetze-im-internet.de/bgb/__651y.html)
- [§ 307 BGB](https://www.gesetze-im-internet.de/bgb/__307.html), [§ 308 BGB](https://www.gesetze-im-internet.de/bgb/__308.html), [§ 309 BGB](https://www.gesetze-im-internet.de/bgb/__309.html)
- [Art. 250 § 6 EGBGB](https://www.gesetze-im-internet.de/bgbeg/art_250__6.html)
- [Richtlinie (EU) 2015/2302](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32015L2302), Art. 12, 17
- Reisesicherungsfondsgesetz (RSFG) `[unverifiziert - prüfen]`

### Kommentare

- Tonner, in: MüKo-BGB, § 651h Rn. 1 ff., § 651r Rn. 1 ff.
- Führich, Reiserecht, Kap. Rücktritt und Insolvenzsicherung.
- Steinrötter, in: BeckOGK BGB, § 651h Rn. 1 ff.
- Geib, in: BeckOK BGB, § 651f Rn. 1 ff.

### Rechtsprechung

1. EuGH, Urt. v. 08.06.2023 – Rs. C-407/21, UFC-Que choisir und CLCV, EuZW 2023, 709 = MDR 2023, 964 (Rücktritt wegen unvermeidbarer außergewöhnlicher Umstände in der COVID-19-Pandemie; Erstattung statt Gutschein, RL (EU) 2015/2302), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2023-06-08&Aktenzeichen=C-407/21)
2. EuGH, Urt. v. 08.06.2023 – Rs. C-49/22, Austrian Airlines (Rückholflug), NJW 2023, 2629 = EuZW 2023, 815 — die Entscheidung ergeht zur **Fluggastrechte-VO (EG) 261/2004**, nicht zum Pauschalreiserecht: ein konsularisch organisierter Repatriierungsflug ist keine anderweitige Beförderung iSd Art. 8 Abs. 1 lit. b, die Unterstützungspflichten des Art. 8 entfallen aber auch in Krisenlagen nicht. Für die Rücktritts- und Erstattungsfragen des § 651h BGB nur mittelbar heranzuziehen, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2023-06-08&Aktenzeichen=C-49/22)
3. Zur Auslegung des § 651h Abs. 3 BGB in Pandemie- und Krisenlagen ist die instanzgerichtliche und höchstrichterliche Praxis einzelfallbezogen zu recherchieren `[unverifiziert - prüfen]`

## Ausgabeformat

```
REISERÜCKTRITT / INSOLVENZSCHUTZ — <Mandat> — <Datum>

I.   Vertrag
     Veranstalter:            <…>       Buchungsnr.: <…>
     Gebucht am:              <Datum>   Reisezeitraum: <von – bis>
     Reisepreis:              <Betrag> EUR   Anzahlung: <Betrag> EUR
     Vertragstyp:             [Pauschalreise § 651a / verbunden § 651w]

II.  Anlass
     Ereignis:                <…>       Datum / Quelle: <…>
     Ort:                     [Bestimmungsort / unmittelbare Nähe / anderswo]
     Persönlicher Grund:      [ja — § 651h Abs. 3 nicht einschlägig / nein]

III. Rücktritt
     Variante:                [Abs. 1 gegen Entschädigung / Abs. 3 kostenfrei]
     Zugang der Erklärung:    <Datum>   ← maßgeblich für die Staffel
     Pauschale laut Bedingungen: <%>  = <Betrag> EUR
     Gegenrechnung § 651h Abs. 2 S. 2: <ersparte Aufwendungen / anderweitiger Erwerb>
     Erstattung Abs. 3 S. 2:  binnen 14 Tagen, spätestens <Datum>

IV.  Alternativen
     Preiserhöhung § 651f:    <%> — über 8 %? [ja → § 651g / nein]
     Vertragsänderung § 651g: [Rücktrittsrecht kostenfrei / Ersatzreise]
     Übertragung § 651e:      [geprüft / nicht möglich]

V.   Absicherung
     Sicherungsschein § 651s: [vorliegend / FEHLT]
     Zahlungssperre § 651t:   [beachtet / verletzt]
     Absicherer / Fonds:      <…>

VI.  Risiko: 🟢 / 🟡 / 🔴 <Begründung>
VII. Quellenverzeichnis
```

### Formulierungshilfe — Rücktrittserklärung (Gerüst)

```
An <Reiseveranstalter>

Rücktritt vom Pauschalreisevertrag
Buchungsnr. <…>, Reisezeitraum <von – bis>

Sehr geehrte Damen und Herren,

namens und in Vollmacht der Reisenden erkläre ich hiermit den
Rücktritt vom o. g. Pauschalreisevertrag.

1. Der Rücktritt erfolgt nach § 651h Abs. 3 BGB und damit
   entschädigungsfrei. Am Bestimmungsort <Ort> bzw. in dessen
   unmittelbarer Nähe bestehen seit dem <Datum> folgende
   unvermeidbare, außergewöhnliche Umstände: <…>
   (Nachweis: <Quelle, Datum>). Diese beeinträchtigen die
   Durchführung der Reise erheblich, weil <…>.

2. Ein Anspruch auf Entschädigung steht Ihnen daher nach
   § 651h Abs. 3 S. 1 BGB nicht zu. Ich fordere Sie auf, die
   geleisteten Zahlungen in Höhe von <…> EUR unverzüglich,
   spätestens binnen 14 Tagen nach Zugang dieses Schreibens
   (§ 651h Abs. 3 S. 2 BGB), also bis zum <Datum>, auf das Konto
   <…> zu erstatten.

3. Rein vorsorglich und ohne Anerkennung einer Rechtspflicht:
   Sollten Sie gleichwohl eine Entschädigung nach § 651h Abs. 2 BGB
   fordern, weise ich bereits jetzt darauf hin, dass die in Ihren
   Reisebedingungen vorgesehene Pauschale von <…> % die tatsächlich
   ersparten Aufwendungen und den anderweitigen Erwerb ersichtlich
   nicht abbildet; der Nachweis nach § 651h Abs. 2 S. 2 BGB bleibt
   ausdrücklich vorbehalten.

4. Ein Gutschein wird nicht akzeptiert; geschuldet ist Erstattung
   in Geld.
```

## Risiken / typische Fehler

- **Persönlichen Grund unter § 651h Abs. 3 BGB subsumiert.** Krankheit, beruflicher Anlass oder Angst sind keine Umstände am Bestimmungsort; dafür greift allein die Reiserücktrittsversicherung.
- **Prognosezeitpunkt verschoben.** Maßgeblich ist die Lage im Zeitpunkt des Rücktritts, bezogen auf den Reisezeitraum — nicht die spätere Entwicklung.
- **Zugang der Rücktrittserklärung nicht dokumentiert.** Die Höhe der Entschädigungspauschale hängt vom Zugangszeitpunkt ab.
- **Pauschale ungeprüft gezahlt.** Der Nachweis nach § 651h Abs. 2 S. 2 BGB und die AGB-Kontrolle nach §§ 307 ff. BGB werden fast nie geführt.
- **8-Prozent-Grenze übersehen.** Eine Preiserhöhung über 8 % kann nicht einseitig durchgesetzt werden und eröffnet den kostenfreien Rücktritt nach § 651g BGB.
- **Anzahlung ohne Sicherungsschein geleistet.** § 651t BGB verbietet die Entgegennahme; ohne Sicherungsschein ist das Geld im Insolvenzfall gefährdet.
- **Gutschein akzeptiert.** Geschuldet ist die Erstattung in Geld; eine Gutscheinlösung ist freiwillig.
- **Aktenzeichen erfunden** — jede Entscheidung verifizieren oder als `[unverifiziert - prüfen]` kennzeichnen.
