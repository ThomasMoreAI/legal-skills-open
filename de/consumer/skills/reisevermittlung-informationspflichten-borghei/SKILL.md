---
name: reisevermittlung-informationspflichten-borghei
title: /reise-fluggastrecht:reisevermittlung-informationspflichten
description: Rollenabgrenzung und Informationspflichten im Reisevertrieb – Reiseveranstalter § 651a BGB, Reisevermittler § 651v BGB, verbundene Reiseleistungen § 651w BGB, vorvertragliche Informationspflichten nach Art. 250 EGBGB und das gesetzliche Formblatt, Haftung des Vermittlers für Buchungsfehler, Online-Buchung im Fernabsatz und der Ausschluss des Widerrufsrechts nach § 312g Abs. 2 Nr. 9 BGB, Gutscheinlösungen. Use when zu klären ist, wer Anspruchsgegner ist, ob die vorvertragliche Information ordnungsgemäß erfolgte oder ob eine online gebuchte Reise widerrufen werden kann.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/reise-fluggastrecht/skills/reisevermittlung-informationspflichten
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: consumer
language: de
---

# /reise-fluggastrecht:reisevermittlung-informationspflichten

## Zweck

Der Skill beantwortet die Vorfrage, an der die meisten Reisemandate entschieden werden, bevor über Mängel gestritten wird: **Wer haftet wofür?** Er ordnet den Vertrieb als Veranstaltung, Vermittlung oder verbundene Reiseleistung ein, prüft die vorvertraglichen Informationspflichten samt Formblatt und korrigiert den häufigsten Beratungsfehler des Gebiets — die Annahme, eine online gebuchte Reise lasse sich widerrufen.

## Eingaben

- Buchungsweg (Reisebüro, Website des Veranstalters, Online-Portal, Vergleichsportal, Telefon)
- Auftreten des Vertriebspartners: Eigenleistungsversprechen, Preisdarstellung, AGB, Impressum
- Anzahl und Art der gebuchten Reiseleistungen und ihre zeitliche Verknüpfung
- Erhaltene vorvertragliche Informationen und Formblatt
- Buchungsbestätigung, Rechnungssteller, Zahlungsempfänger
- Konkreter Buchungsfehler mit Datum und Auswirkung
- Etwaige Widerrufsbelehrung und erklärter Widerruf
- Angebotene oder akzeptierte Gutscheinlösung

## Sub-Agent-Architektur

Ein Researcher ermittelt das tatsächliche Auftreten des Vertriebspartners, beschafft Buchungsstrecke, AGB und Formblatt und ordnet die Normen zu. Ein Drafter subsumiert unter §§ 651a, 651v und 651w BGB, prüft die Informationspflichten des Art. 250 EGBGB und die Folgen ihrer Verletzung und entwirft das Anspruchsschreiben. Ein Reviewer kontrolliert die Rollenzuordnung, den Ausschluss des Widerrufsrechts und jede Fundstelle; Unbestätigtes wird mit `[unverifiziert - prüfen]` markiert.

## Ablauf

### 1. Rollenabgrenzung ([§ 651a BGB](https://www.gesetze-im-internet.de/bgb/__651a.html), [§ 651v BGB](https://www.gesetze-im-internet.de/bgb/__651v.html), [§ 651w BGB](https://www.gesetze-im-internet.de/bgb/__651w.html))

| Rolle | Merkmal | Haftung |
|---|---|---|
| **Reiseveranstalter** § 651a | verschafft eine **Gesamtheit von mindestens zwei verschiedenen Arten** von Reiseleistungen für dieselbe Reise; tritt als Erbringer der Gesamtheit auf | volle Haftung für alle Reiseleistungen nach §§ 651i ff. BGB |
| **Reisevermittler** § 651v | vermittelt einen Pauschalreisevertrag mit einem Dritten; wird nicht selbst Vertragspartner der Reise | Haftung nur für **eigenes** Verschulden (Beratung, Buchung, Information) |
| **Verbundene Reiseleistungen** § 651w | Vermittlung mehrerer Einzelverträge in bestimmter zeitlicher und organisatorischer Verknüpfung, ohne Pauschalreise zu sein | **kein** Reisevertragsrecht; nur Insolvenzsicherung und Information |

Entscheidend ist nicht die Selbstbezeichnung, sondern das **Auftreten gegenüber dem Reisenden** (§ 651a Abs. 2 BGB): Wer den Anschein erweckt, die Leistungen in eigener Verantwortung zu erbringen, ist Veranstalter — auch wenn die AGB ihn als „Vermittler" bezeichnen. Nach § 651b BGB wird ferner als Veranstalter behandelt, wer Reiseleistungen so vermittelt, dass für den Reisenden der Eindruck einer Pauschalreise entsteht.

**Praxisregel**: Bei Preisdarstellung als Gesamtpreis, einheitlicher Rechnung und einheitlicher Buchungsbestätigung spricht viel für Veranstaltereigenschaft.

### 2. Verbundene Reiseleistungen im Einzelnen ([§ 651w BGB](https://www.gesetze-im-internet.de/bgb/__651w.html))

Verbundene Reiseleistungen setzen voraus, dass der Unternehmer für den Reisenden getrennte Verträge über mindestens zwei verschiedene Arten von Reiseleistungen vermittelt und dabei entweder bei einem einzigen Besuch oder Kontakt gesonderte Auswahl und Zahlung veranlasst oder in gezielter Weise die Buchung einer weiteren Leistung bei einem anderen Unternehmer binnen 24 Stunden nach der ersten Buchungsbestätigung veranlasst.

Rechtsfolge: **kein** Anspruch aus §§ 651i ff. BGB. Der Reisende ist auf die Einzelverträge verwiesen. Der Unternehmer schuldet aber die Information nach [Art. 251 EGBGB](https://www.gesetze-im-internet.de/bgbeg/) und die Insolvenzsicherung nach § 651w Abs. 3 BGB. **Unterlässt er die vorgeschriebene Information, haftet er nach § 651w Abs. 4 BGB wie ein Reiseveranstalter** — die schärfste Sanktion des Vertriebsrechts und der wirksamste Angriffspunkt bei Online-Portalen.

### 3. Vorvertragliche Informationspflichten und Formblatt ([Art. 250 § 1 EGBGB](https://www.gesetze-im-internet.de/bgbeg/art_250__1.html), [Art. 250 § 3 EGBGB](https://www.gesetze-im-internet.de/bgbeg/art_250__3.html))

Vor Abgabe der Vertragserklärung des Reisenden ist ihm das gesetzlich vorgeschriebene **Formblatt** zu übermitteln, das ihn über die Einordnung als Pauschalreise und über seine wesentlichen Rechte unterrichtet (Art. 250 § 2 EGBGB). Zusätzlich ist über die in Art. 250 § 3 EGBGB aufgezählten Punkte zu informieren — unter anderem Reiseleistungen und Merkmale, Gesamtpreis mit Steuern und Nebenkosten, Zahlungsmodalitäten, Mindestteilnehmerzahl, Pass- und Visumerfordernisse, Rücktrittsrecht und Insolvenzsicherung.

Rechtsfolgen von Informationsmängeln:

- Nach [§ 651d BGB](https://www.gesetze-im-internet.de/bgb/__651d.html) werden die Angaben **Vertragsinhalt**; sie sind Maßstab für die geschuldete Beschaffenheit nach § 651i Abs. 2 BGB.
- Fehlt die Information über zusätzlich anfallende **Gebühren, Entgelte und sonstige Kosten**, schuldet der Reisende diese nicht.
- Informationspflichtverletzungen können Schadensersatz aus § 280 Abs. 1 BGB iVm § 241 Abs. 2 BGB und, bei Verschulden bei Vertragsschluss, § 311 Abs. 2 BGB auslösen.
- Nach Art. 250 § 6 EGBGB ist der Vertragsinhalt bei oder unverzüglich nach Vertragsschluss auf einem dauerhaften Datenträger zu übermitteln.

Die Informationspflichten treffen den **Veranstalter und den Vermittler** gemeinsam; der Vermittler kann sich nicht darauf zurückziehen, die Angaben stammten vom Veranstalter.

### 4. Haftung des Vermittlers für Buchungsfehler ([§ 651v BGB](https://www.gesetze-im-internet.de/bgb/__651v.html))

Der Reisevermittler haftet nicht für die Reiseleistungen, wohl aber für **eigene Pflichtverletzungen** aus dem Geschäftsbesorgungsvertrag mit dem Reisenden:

- **Buchungsfehler** — falsches Datum, falscher Flughafen, falsche Namensschreibweise, nicht gebuchte Zusatzleistung. § 651x BGB stellt klar, dass für technische Buchungsfehler gehaftet wird, soweit sie dem Unternehmer zuzurechnen sind.
- **Beratungsfehler** — unterlassener Hinweis auf Pass- und Visumerfordernisse, Impfvorschriften, Umsteigezeiten, Reisewarnungen, Notwendigkeit einer Reiserücktrittsversicherung.
- **Nichtweiterleitung** von Erklärungen: Nach § 651v Abs. 4 BGB gilt eine dem Vermittler gegenüber abgegebene Erklärung des Reisenden auch dem Veranstalter gegenüber als abgegeben — Mängelanzeige und Rücktritt gegenüber dem Reisebüro wirken damit.
- **Zahlungsannahme** ohne Sicherungsschein (§ 651t BGB) — der Vermittler darf Zahlungen nur unter denselben Voraussetzungen wie der Veranstalter entgegennehmen.

Der Vermittler haftet ferner nach § 651v Abs. 2 BGB für Informationspflichten, soweit sie ihn treffen.

### 5. Online-Buchung und der Ausschluss des Widerrufsrechts ([§ 312g Abs. 2 Nr. 9 BGB](https://www.gesetze-im-internet.de/bgb/__312g.html))

**Dies ist der häufigste Beratungsfehler des Reiserechts.** Ein Fernabsatzvertrag liegt bei der Online- oder Telefonbuchung regelmäßig vor. Ein Widerrufsrecht besteht aber **nicht**: § 312g Abs. 2 Nr. 9 BGB nimmt Verträge zur Erbringung von Dienstleistungen in den Bereichen Beherbergung zu anderen Zwecken als zu Wohnzwecken, Beförderung von Waren, Kraftfahrzeugvermietung, Lieferung von Speisen und Getränken sowie zur Erbringung weiterer Dienstleistungen im Zusammenhang mit Freizeitbetätigungen vom Widerrufsrecht aus, wenn der Vertrag für die Erbringung einen **spezifischen Termin oder Zeitraum** vorsieht.

Praktische Folgerungen:

- Für Flug, Hotel und Pauschalreise mit festem Termin gibt es **keinen** Widerruf. Der Ausstieg läuft ausschließlich über den **Rücktritt nach § 651h BGB** gegen Entschädigung oder, unter den dortigen Voraussetzungen, entschädigungsfrei (`/reise-fluggastrecht:reiseruecktritt-insolvenzschutz`).
- Für **außerhalb von Geschäftsräumen** geschlossene Pauschalreiseverträge sieht [§ 651i BGB](https://www.gesetze-im-internet.de/bgb/__651i.html) und der Regelungszusammenhang der §§ 651a ff. BGB Sonderfälle vor; die Reichweite eines Widerrufsrechts in dieser Konstellation ist gesondert zu prüfen `[unverifiziert - prüfen]`.
- Eine vom Unternehmer **freiwillig** erteilte Widerrufsbelehrung kann ein vertragliches Lösungsrecht begründen — das ist Auslegungsfrage und im Einzelfall zu prüfen.
- Eine „kostenlose Stornierung bis …" in den Bedingungen ist ein **vertragliches** Rücktrittsrecht, kein Widerruf; ihr Wortlaut ist maßgeblich.

### 6. Gutscheinlösungen

Wird der Vertrag rückabgewickelt, schuldet der Unternehmer **Erstattung in Geld**. Ein Gutschein ist eine Leistung an Erfüllungs statt und bedarf der **Zustimmung** des Reisenden; er kann nicht einseitig aufgedrängt werden. Vor der Annahme zu prüfen sind Insolvenzabsicherung des Gutscheins, Einlösefrist, Übertragbarkeit und die Frage, ob mit der Annahme weitergehende Ansprüche abgegolten sein sollen. Die unionsrechtliche Linie zur Erstattung im Pauschalreisebereich ergibt sich aus EuGH, Urt. v. 08.06.2023 – C-407/21, EuZW 2023, 709 ([dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2023-06-08&Aktenzeichen=C-407/21)), Reichweite im Einzelfall zu prüfen `[unverifiziert - prüfen]`.

### 7. Beweisführung und Dokumentation

Die Rollenzuordnung wird über Unterlagen entschieden, nicht über Behauptungen. Zu sichern sind: vollständige Buchungsstrecke mit Screenshots, AGB in der Fassung des Buchungstags, Impressum, Formblatt, Buchungsbestätigung, Rechnung, Zahlungsempfänger und der gesamte Schriftverkehr. Bei Online-Portalen ist die Buchungsstrecke zeitnah zu archivieren, weil sie laufend verändert wird.

## Quellen

### Statute

- [§ 651a BGB](https://www.gesetze-im-internet.de/bgb/__651a.html), [§ 651b BGB](https://www.gesetze-im-internet.de/bgb/__651b.html), [§ 651c BGB](https://www.gesetze-im-internet.de/bgb/__651c.html), [§ 651d BGB](https://www.gesetze-im-internet.de/bgb/__651d.html), [§ 651i BGB](https://www.gesetze-im-internet.de/bgb/__651i.html), [§ 651t BGB](https://www.gesetze-im-internet.de/bgb/__651t.html), [§ 651v BGB](https://www.gesetze-im-internet.de/bgb/__651v.html), [§ 651w BGB](https://www.gesetze-im-internet.de/bgb/__651w.html), [§ 651x BGB](https://www.gesetze-im-internet.de/bgb/__651x.html), [§ 651y BGB](https://www.gesetze-im-internet.de/bgb/__651y.html)
- [§ 312g BGB](https://www.gesetze-im-internet.de/bgb/__312g.html), [§ 312c BGB](https://www.gesetze-im-internet.de/bgb/__312c.html), [§ 355 BGB](https://www.gesetze-im-internet.de/bgb/__355.html)
- [§ 241 BGB](https://www.gesetze-im-internet.de/bgb/__241.html), [§ 280 BGB](https://www.gesetze-im-internet.de/bgb/__280.html), [§ 311 BGB](https://www.gesetze-im-internet.de/bgb/__311.html)
- [Art. 250 § 1 EGBGB](https://www.gesetze-im-internet.de/bgbeg/art_250__1.html), [Art. 250 § 2 EGBGB](https://www.gesetze-im-internet.de/bgbeg/art_250__2.html), [Art. 250 § 3 EGBGB](https://www.gesetze-im-internet.de/bgbeg/art_250__3.html), [Art. 250 § 6 EGBGB](https://www.gesetze-im-internet.de/bgbeg/art_250__6.html)
- [Richtlinie (EU) 2015/2302](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32015L2302), Art. 5, 6, 19

### Kommentare

- Tonner, in: MüKo-BGB, § 651a Rn. 1 ff., § 651v Rn. 1 ff., § 651w Rn. 1 ff.
- Führich, Reiserecht, Kap. Reisevermittlung und Informationspflichten.
- Steinrötter, in: BeckOGK BGB, § 651w Rn. 1 ff.
- Geib, in: BeckOK BGB, § 651v Rn. 1 ff.

### Rechtsprechung

1. EuGH, Urt. v. 08.06.2023 – Rs. C-407/21, UFC-Que choisir und CLCV, EuZW 2023, 709 = MDR 2023, 964 (Erstattung im Pauschalreiserecht nach Rücktritt; RL (EU) 2015/2302), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2023-06-08&Aktenzeichen=C-407/21)
2. EuGH, Urt. v. 12.03.2002 – Rs. C-168/00, Leitner, NJW 2002, 1255 = EuZW 2002, 339 (immaterieller Schaden; zum Schutzzweck des Pauschalreiserechts), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2002-03-12&Aktenzeichen=C-168/00)
3. Zur Abgrenzung Veranstalter / Vermittler nach dem Auftreten gegenüber dem Reisenden ist die instanzgerichtliche Praxis einzelfallbezogen zu recherchieren `[unverifiziert - prüfen]`

## Ausgabeformat

```
REISEVERMITTLUNG / INFORMATIONSPFLICHTEN — <Mandat> — <Datum>

I.   Buchungsvorgang
     Buchungsweg:             <Reisebüro / Website / Portal / Telefon>
     Vertriebspartner:        <…>       Selbstbezeichnung: <…>
     Leistungen:              <Anzahl / Arten>
     Rechnungssteller:        <…>       Zahlungsempfänger: <…>

II.  Rollenzuordnung
     Einordnung:              [Veranstalter § 651a / Vermittler § 651v /
                               verbundene Reiseleistungen § 651w]
     Maßgebliche Indizien:    <Gesamtpreis / einheitliche Bestätigung / Auftreten>
     Anspruchsgegner:         <…>

III. Informationspflichten
     Formblatt Art. 250 § 2:  [übermittelt / FEHLT]
     Angaben Art. 250 § 3:    [vollständig / Lücken: <…>]
     Dauerhafter Datenträger Art. 250 § 6: [ja / nein]
     Folge der Verletzung:    <Vertragsinhalt § 651d / Kostenfreiheit /
                               Haftung wie Veranstalter § 651w Abs. 4>

IV.  Vermittlerhaftung § 651v
     Buchungsfehler:          <…>
     Beratungsfehler:         <…>
     Erklärungszugang Abs. 4: <…>
     Zahlungsannahme § 651t:  [zulässig / unzulässig]

V.   Widerrufsrecht
     Fernabsatzvertrag:       [ja / nein]
     § 312g Abs. 2 Nr. 9 BGB: [Widerrufsrecht ausgeschlossen / ausnahmsweise offen]
     Vertragliches Lösungsrecht: <…>
     Statthafter Ausstieg:    Rücktritt § 651h BGB

VI.  Gutschein
     Angeboten:               [ja / nein]   Angenommen: [ja / nein]
     Absicherung / Frist:     <…>

VII. Risiko: 🟢 / 🟡 / 🔴 <Begründung>
VIII.Quellenverzeichnis
```

### Formulierungshilfe — Anspruchsschreiben an den Vermittler (Gerüst)

```
An <Reisebüro / Portal>

Ansprüche wegen fehlerhafter Vermittlung
Buchung <Nr.>, Reisezeitraum <von – bis>

Sehr geehrte Damen und Herren,

ich zeige die Vertretung von <Name> an.

1. Rolle
   Sie sind ausweislich <Buchungsbestätigung / Rechnung / AGB>
   als Reisevermittler iSd § 651v BGB tätig geworden.
   Vorsorglich weise ich darauf hin, dass eine Einordnung als
   Reiseveranstalter nach § 651a Abs. 2 BGB in Betracht kommt, weil
   <Gesamtpreisdarstellung / einheitliche Bestätigung / Auftreten>.

2. Pflichtverletzung
   Bei der Buchung am <Datum> haben Sie <Fehler>. Der Fehler ist
   Ihnen zuzurechnen (§§ 651v, 651x BGB iVm §§ 280 Abs. 1,
   241 Abs. 2 BGB).

3. Informationspflichten
   Das Formblatt nach Art. 250 § 2 EGBGB wurde nicht übermittelt;
   über <Punkt> nach Art. 250 § 3 EGBGB wurde nicht informiert.
   Die hierdurch entstandenen Kosten in Höhe von <…> EUR schuldet
   mein Mandant nicht.

4. Schaden
   <Position 1>: <…> EUR
   <Position 2>: <…> EUR
   Gesamt: <…> EUR

Ich fordere Sie auf, den Betrag bis zum <Datum> zu erstatten.
Ein Widerruf nach §§ 312g, 355 BGB wird ausdrücklich nicht
erklärt, da das Widerrufsrecht nach § 312g Abs. 2 Nr. 9 BGB
ausgeschlossen ist; der Anspruch stützt sich allein auf die
vorstehenden Pflichtverletzungen.
```

## Risiken / typische Fehler

- **Widerruf empfohlen.** § 312g Abs. 2 Nr. 9 BGB schließt das Widerrufsrecht für terminbezogene Reiseleistungen weitgehend aus; der Ausstieg läuft über § 651h BGB. Dies ist der häufigste Beratungsfehler des Gebiets.
- **Rolle nach der Selbstbezeichnung bestimmt.** Maßgeblich ist das Auftreten gegenüber dem Reisenden (§ 651a Abs. 2 BGB), nicht die AGB-Klausel „wir vermitteln nur".
- **Verbundene Reiseleistungen als Pauschalreise behandelt.** § 651w BGB gewährt keine Mängelrechte — dafür aber die Haftung wie ein Veranstalter, wenn die Information unterblieben ist.
- **Formblatt nicht angefordert.** Ohne Formblatt und Buchungsstrecke ist die Informationspflichtverletzung nicht beweisbar.
- **Erklärung nur an den Veranstalter gerichtet.** Nach § 651v Abs. 4 BGB wirkt die Erklärung gegenüber dem Vermittler auch gegenüber dem Veranstalter — und umgekehrt ist der Zugang beim Vermittler zu dokumentieren.
- **Gutschein vorbehaltlos angenommen.** Geschuldet ist Erstattung in Geld; die Annahme kann weitergehende Ansprüche abschneiden.
- **Buchungsstrecke nicht archiviert.** Online-Portale ändern sie laufend; ohne Screenshots vom Buchungstag ist die Rollenzuordnung kaum zu führen.
- **Aktenzeichen erfunden** — jede Entscheidung verifizieren oder als `[unverifiziert - prüfen]` kennzeichnen.
