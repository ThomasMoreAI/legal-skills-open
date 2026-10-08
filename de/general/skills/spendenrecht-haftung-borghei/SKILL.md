---
name: spendenrecht-haftung-borghei
title: /vereins-stiftungs-gemeinnuetzigkeitsrecht:spendenrecht-haftung
description: Zuwendungen an steuerbegünstigte Körperschaften und die Haftung des Zuwendungsempfängers – Zuwendungsbestätigung nach amtlichem Muster, Sonderausgabenabzug und Höchstbeträge § 10b Abs. 1 EStG mit Vortrag, Großspendenregelung für den Vermögensstock § 10b Abs. 1a EStG, Sachspenden und Aufwandsspenden als Rückspende § 10b Abs. 3 EStG, Vertrauensschutz des Spenders sowie Aussteller- und Veranlasserhaftung § 10b Abs. 4 EStG mit 30 Prozent Haftungssatz und § 9 Nr. 5 GewStG mit 15 Prozent, Abgrenzung Sponsoring zur Spende und Zuwendungsempfängerregister § 60b AO. Use when eine Zuwendungsbestätigung ausgestellt oder geprüft, ein Sponsoringvertrag abgegrenzt oder eine Spendenhaftung abgewehrt werden soll.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/vereins-stiftungs-gemeinnuetzigkeitsrecht/skills/spendenrecht-haftung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: general
language: de
---

# /vereins-stiftungs-gemeinnuetzigkeitsrecht:spendenrecht-haftung

## Zweck

Die Zuwendungsbestätigung ist das einzige Dokument, mit dem eine gemeinnützige Körperschaft eine **persönliche Haftung ihrer Handelnden** auslösen kann — und sie wird routinemäßig von Ehrenamtlichen ausgestellt. Dieser Skill sichert die formale Richtigkeit der Bestätigung, ordnet Sachspende, Aufwandsspende und Sponsoring richtig zu und arbeitet das Haftungsregime des § 10b Abs. 4 EStG ab.

## Eingaben

- Körperschaft: Rechtsform, Status (Feststellung § 60a AO, Freistellungsbescheid, Anlage zum Körperschaftsteuerbescheid mit Datum)
- Art der Zuwendung: Geldspende, Mitgliedsbeitrag, Sachspende, Aufwands- oder Vergütungsverzicht
- Bei Sachspende: Herkunft (Privatvermögen oder Betriebsvermögen), Anschaffungszeitpunkt, Wertermittlung
- Bei Aufwandsspende: Anspruchsgrundlage (Satzung oder Vertrag), Datum der Einräumung, Datum des Verzichts, Leistungsfähigkeit der Körperschaft
- Bei Sponsoring: Vertrag, Gegenleistung, Werbewirkung, Rechnungstellung
- Beim Spender: natürliche Person oder Körperschaft, Gesamtbetrag der Einkünfte bzw. Umsätze und Löhne
- Bei Haftungsfall: beanstandete Bestätigung, Prüfungsfeststellung, handelnde Personen

## Sub-Agent-Architektur

1. **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) liefert § 10b EStG, § 9 Nr. 5 GewStG, § 9 Abs. 1 Nr. 2 KStG, §§ 60a, 60b, 63 AO und die einschlägigen BMF-Schreiben.
2. **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) erstellt Zuwendungsbestätigung, Abgrenzungsvermerk Sponsoring/Spende und Verteidigungsschrift gegen einen Haftungsbescheid.
3. **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft die Bestätigung gegen das amtliche Muster, die Bewertung der Sachspende und ob eine Aufwandsspende die Werthaltigkeitsprüfung besteht.

## Ablauf

### 1. Sonderausgabenabzug und Höchstbeträge ([§ 10b Abs. 1 EStG](https://www.gesetze-im-internet.de/estg/__10b.html))

Zuwendungen (Spenden **und** Mitgliedsbeiträge) zur Förderung steuerbegünstigter Zwecke im Sinne der §§ 52 bis 54 AO sind als Sonderausgaben abziehbar bis insgesamt

1. **20 Prozent des Gesamtbetrags der Einkünfte** oder
2. **4 Promille der Summe der gesamten Umsätze und der im Kalenderjahr aufgewendeten Löhne und Gehälter.**

Empfänger muss nach § 10b Abs. 1 S. 2 EStG eine juristische Person des öffentlichen Rechts oder öffentliche Dienststelle, eine nach § 5 Abs. 1 Nr. 9 KStG steuerbefreite Körperschaft oder eine im EU-/EWR-Ausland ansässige, entsprechend begünstigte Körperschaft sein; bei ausländischen Empfängern kommen Amtshilfe und Beitreibungsunterstützung als Voraussetzung hinzu.

**Nicht abziehbar sind Mitgliedsbeiträge** an Körperschaften, die nach § 10b Abs. 1 S. 8 EStG den Sport, kulturelle Betätigungen mit vorrangigem Freizeitcharakter, Heimatpflege und Heimatkunde oder Zwecke nach § 52 Abs. 2 S. 1 Nr. 23 AO fördern — beim Sportverein ist also die **Spende** abziehbar, der **Mitgliedsbeitrag** nicht. Überschreitende Beträge werden nach § 10b Abs. 1 S. 9 EStG in die folgenden Veranlagungszeiträume **vorgetragen** (§ 10d Abs. 4 EStG gilt entsprechend).

**§ 10b Abs. 1a EStG — Vermögensstockspende:** Spenden in das zu erhaltende Vermögen (Vermögensstock) einer Stiftung können auf Antrag im Zuwendungsjahr und in den folgenden **neun** Veranlagungszeiträumen bis zu **1 Million Euro** (Ehegatten bei Zusammenveranlagung entsprechend mehr) abgezogen werden — zusätzlich zu den Höchstbeträgen des Abs. 1. Für Körperschaften gilt § 9 Abs. 1 Nr. 2 KStG, für die Gewerbesteuer § 9 Nr. 5 GewStG.

### 2. Zuwendungsbestätigung nach amtlichem Muster

Die Bestätigung ist nach **amtlich vorgeschriebenem Vordruck** auszustellen; Abweichungen im Wortlaut der gesetzlich vorgegebenen Passagen sind unzulässig. Zwingende Bestandteile:

```
[Briefkopf des Zuwendungsempfängers]

Bestätigung über Geldzuwendungen im Sinne des § 10b des Einkommensteuergesetzes
an eine der in § 5 Abs. 1 Nr. 9 des Körperschaftsteuergesetzes bezeichneten
Körperschaften, Personenvereinigungen oder Vermögensmassen

Name und Anschrift des Zuwendenden:      ..............................
Betrag der Zuwendung — in Ziffern:  .......  in Buchstaben:  ..........
Tag der Zuwendung:                        ..............................

Es handelt sich um den Verzicht auf Erstattung von Aufwendungen:
      [ ] Ja        [ ] Nein

Wir sind wegen Förderung [des/der] ................................ nach dem
Freistellungsbescheid bzw. der Anlage zum Körperschaftsteuerbescheid des
Finanzamts ............., StNr. ............., vom ............. für den
letzten Veranlagungszeitraum ......... nach § 5 Abs. 1 Nr. 9 KStG von der
Körperschaftsteuer und nach § 3 Nr. 6 GewStG von der Gewerbesteuer befreit.
      — oder —
Die Einhaltung der satzungsmäßigen Voraussetzungen nach den §§ 51, 59, 60 und
61 AO wurde vom Finanzamt ............., StNr. ............., mit Bescheid vom
............. nach § 60a AO gesondert festgestellt. Wir fördern nach unserer
Satzung ......................................

Es wird bestätigt, dass die Zuwendung nur zur Förderung [Zweck] verwendet wird.

Nur für steuerbegünstigte Einrichtungen, die Mitgliedsbeiträge erhalten:
Es wird bestätigt, dass es sich nicht um einen Mitgliedsbeitrag handelt, dessen
Abzug nach § 10b Abs. 1 EStG ausgeschlossen ist.

Ort, Datum und Unterschrift des Zuwendungsempfängers
```

**Formhinweise:** Bei Sachzuwendungen ist der Vordruck für Sachzuwendungen zu verwenden — mit genauer Bezeichnung des Gegenstands, Angabe der Herkunft (Betriebs- oder Privatvermögen), der Wertermittlungsgrundlage und der Unterlagen, aus denen sich der Wert ergibt. Die Gültigkeit des zugrunde liegenden Bescheids ist zeitlich begrenzt; die Bestätigung darf nur ausgestellt werden, solange der genannte Bescheid dafür trägt. **Der Text des amtlichen Musters ist gegen die jeweils aktuelle Bekanntmachung des BMF zu prüfen** `[unverifiziert - prüfen]`. Für Kleinbeträge und Katastrophenkonten gilt der vereinfachte Zuwendungsnachweis nach § 50 EStDV; die dortige Betragsgrenze ist ebenfalls in der geltenden Fassung nachzusehen `[unverifiziert - prüfen]`.

### 3. Sachspenden ([§ 10b Abs. 3 EStG](https://www.gesetze-im-internet.de/estg/__10b.html))

Als Zuwendung gilt auch die Zuwendung von **Wirtschaftsgütern** — **mit Ausnahme von Nutzungen und Leistungen**. Die Überlassung eines Raums, die Arbeitsleistung eines Handwerkers und die unentgeltliche Nutzung eines Fahrzeugs sind daher **keine** abziehbaren Zuwendungen.

Bewertung nach § 10b Abs. 3 S. 2 bis 4 EStG:

- **Entnahme aus einem Betriebsvermögen:** Wert der Entnahme zuzüglich der darauf entfallenden Umsatzsteuer (Buchwertprivileg nach § 6 Abs. 1 Nr. 4 S. 4 EStG prüfen).
- **Aus dem Privatvermögen:** **gemeiner Wert**, wenn eine Veräußerung im Zuwendungszeitpunkt keinen Besteuerungstatbestand erfüllen würde.
- **In allen übrigen Fällen:** Die fortgeführten Anschaffungs- oder Herstellungskosten dürfen nur überschritten werden, soweit eine Gewinnrealisierung stattgefunden hat.

Die Wertermittlung ist zu **dokumentieren** (Rechnung, Gutachten, Vergleichspreise, Zustandsbeschreibung bei Gebrauchtgegenständen) und in der Bestätigung anzugeben. Ein zu hoch angesetzter Wert ist eine **unrichtige Bestätigung** im Sinne des § 10b Abs. 4 S. 2 EStG.

### 4. Aufwandsspende und Rückspende — der klassische Fehlerfall

**§ 10b Abs. 3 S. 5, 6 EStG:** Aufwendungen zugunsten einer zum Empfang berechtigten Körperschaft können nur abgezogen werden, wenn

1. ein **Anspruch auf Erstattung** der Aufwendungen **durch Vertrag oder Satzung eingeräumt** wurde **und**
2. auf die Erstattung **verzichtet** wurde, wobei
3. der Anspruch **nicht unter der Bedingung des Verzichts** eingeräumt worden sein darf.

Daraus folgt die praktische Prüfkette — jede Stufe ist zu belegen:

1. **Anspruchsgrundlage vor der Tätigkeit:** Satzungsregelung oder schriftliche Vereinbarung, **datiert vor** dem Entstehen des Aufwands. Ein nachträglich geschaffener Anspruch trägt nicht.
2. **Ernsthaftigkeit und Werthaltigkeit:** Die Körperschaft muss zum Zeitpunkt der Einräumung wirtschaftlich in der Lage sein, den Anspruch **tatsächlich zu erfüllen**. Ein Verein, dessen Kasse den Erstattungsanspruch nie hätte decken können, kann keine Aufwandsspende bescheinigen.
3. **Zeitnaher Verzicht** nach Entstehen des Anspruchs, schriftlich erklärt und im Protokoll oder in der Buchhaltung festgehalten.
4. **Kennzeichnung in der Bestätigung:** Das Feld „Es handelt sich um den Verzicht auf Erstattung von Aufwendungen" ist mit **Ja** anzukreuzen. Das Unterlassen dieser Kennzeichnung ist der häufigste formale Fehler.

Ein **Vergütungsverzicht** (Übungsleiter, Vorstand) folgt denselben Regeln; die Vergütung muss zuvor wirksam vereinbart und die Zahlung ernsthaft geschuldet gewesen sein.

Die Fristen für Rechtsbehelfe gegen Haftungsbescheide rechnet der deterministische Rechner:

```bash
python -m scripts.legal_calc.cli frist --ereignis 15.01.2026 --menge 1 --einheit monate --land BY
```

Er leistet **ausschließlich** die Arithmetik der §§ 187–193 BGB. **Fristbeginn und Zugang bleiben rechtliche Eingaben** — die Bekanntgabe des Bescheids nach §§ 122, 355 AO bewertet der Bearbeiter, nicht das Werkzeug. Vgl. `/steuerrecht:einspruch-finanzamt`.

### 5. Vertrauensschutz und Spendenhaftung ([§ 10b Abs. 4 EStG](https://www.gesetze-im-internet.de/estg/__10b.html))

**Vertrauensschutz des Spenders (S. 1):** Der Steuerpflichtige darf auf die Richtigkeit der Bestätigung **vertrauen** — es sei denn, er hat sie durch unlautere Mittel oder falsche Angaben erwirkt oder ihm war die Unrichtigkeit bekannt oder infolge **grober Fahrlässigkeit** unbekannt. Der gute Glaube des Spenders wird also geschützt; die wirtschaftliche Last verlagert sich auf die Empfängerseite.

**Haftung (S. 2, 3):** Wer **vorsätzlich oder grob fahrlässig**

- eine **unrichtige Bestätigung ausstellt** (**Ausstellerhaftung**) oder
- **veranlasst, dass Zuwendungen nicht zu den in der Bestätigung angegebenen steuerbegünstigten Zwecken verwendet werden** (**Veranlasserhaftung**),

haftet für die **entgangene Steuer**. Diese ist mit **30 Prozent des zugewendeten Betrags** anzusetzen. Hinzu tritt nach **§ 9 Nr. 5 S. 14, 16 GewStG** die Haftung für die entgangene **Gewerbesteuer** mit **15 Prozent der Zuwendungen** — zusammen also bis zu **45 Prozent** des Zuwendungsbetrags, unabhängig davon, ob dem Fiskus tatsächlich Steuer entgangen ist.

**Reihenfolge der Inanspruchnahme (S. 4):** In den Fällen der **Veranlasserhaftung** ist **vorrangig der Zuwendungsempfänger** in Anspruch zu nehmen; die für ihn handelnden **natürlichen Personen** sind nur heranzuziehen, wenn die entgangene Steuer nicht nach § 47 AO erloschen ist **und** Vollstreckungsmaßnahmen gegen die Körperschaft **nicht erfolgreich** sind. Bei der **Ausstellerhaftung** fehlt diese Vorrangregel — der ausstellende Vorstand kann unmittelbar in Anspruch genommen werden. **§ 10b Abs. 4 S. 5 EStG** hemmt den Ablauf der Festsetzungsfrist für den Haftungsanspruch, solange die Festsetzungsfrist für die Körperschaftsteuer des Empfängers läuft; § 191 Abs. 5 AO ist ausdrücklich **nicht** anzuwenden — die Haftung überdauert damit die gewöhnliche Verjährungserwartung erheblich.

**Organisatorische Konsequenz:** Zeichnungsberechtigung für Zuwendungsbestätigungen auf wenige geschulte Personen begrenzen, Vier-Augen-Prinzip bei Sach- und Aufwandsspenden, fortlaufendes Verzeichnis der ausgestellten Bestätigungen mit Belegzuordnung, Aufbewahrung der Bewertungsunterlagen und D&O-Deckung prüfen.

### 6. Sponsoring oder Spende

Die Abgrenzung entscheidet über Abzug, Umsatzsteuer und Sphärenzuordnung. Maßgeblich ist, ob der Zuwendende eine **Gegenleistung** erhält.

| Merkmal | Spende | Sponsoring |
|---|---|---|
| **Motiv** | freiwillig, uneigennützig, ohne Gegenleistung | betrieblich, auf Werbewirkung gerichtet |
| **Vertrag** | einseitige Zuwendung | gegenseitiger Vertrag mit Leistungspflichten |
| **Beim Zuwendenden** | Sonderausgabe § 10b EStG / § 9 Abs. 1 Nr. 2 KStG | **Betriebsausgabe** § 4 Abs. 4 EStG, ohne Höchstbetrag |
| **Bei der Körperschaft** | ideeller Bereich | Vermögensverwaltung oder **wirtschaftlicher Geschäftsbetrieb** |
| **Zuwendungsbestätigung** | ja | **nein** — es ist eine **Rechnung** mit Umsatzsteuer zu stellen |

Die Verwaltungsauffassung folgt dem **Sponsoring-Erlass** des BMF; die dortige Dreiteilung wird üblicherweise so gehandhabt: Die **bloße Duldung** der Nutzung von Namen und Emblem des Sponsors zu Werbezwecken bleibt Vermögensverwaltung; **aktive Mitwirkung** der Körperschaft an der Werbung (Verlinkung mit Werbebotschaft, Auftritt des Sponsors, Standflächen, Bandenwerbung) begründet einen **steuerpflichtigen wirtschaftlichen Geschäftsbetrieb**; der bloße **Hinweis** auf den Unterstützer ohne besondere Hervorhebung bleibt im ideellen Bereich. **Fundstelle, Datum und aktuelle Fassung des Sponsoring-Erlasses sind vor Verwendung zu prüfen** `[unverifiziert - prüfen]`. Bei gemischten Verträgen ist das Entgelt aufzuteilen und der Sponsoringanteil gesondert abzurechnen. Zur Sphärenzuordnung siehe `/vereins-stiftungs-gemeinnuetzigkeitsrecht:gemeinnuetzigkeit-ao`.

### 7. Zuwendungsempfängerregister ([§ 60b AO](https://www.gesetze-im-internet.de/ao_1977/__60b.html))

Das **Bundeszentralamt für Steuern** führt ein **Zuwendungsempfängerregister** zu Zwecken des Sonderausgabenabzugs nach § 10b EStG und der Steuerermäßigung nach § 34g EStG. Gespeichert werden nach § 60b Abs. 2 AO unter anderem: **Wirtschafts-Identifikationsnummer**, Name, Anschrift, die steuerbegünstigten Zwecke nach §§ 52 bis 54 AO, der Status als juristische Person des öffentlichen Rechts, die **zuständige Finanzbehörde**, das **Datum der Erteilung des letzten Freistellungsbescheids, der Anlage zum Körperschaftsteuerbescheid oder des Feststellungsbescheids nach § 60a AO** sowie **Kontoverbindungen** bei Banken und Bezahldienstleistern.

Die zuständige Finanzbehörde übermittelt die Daten und **unverzüglich jede Änderung** (Abs. 3); das BZSt darf die Daten Dritten offenbaren, § 30 AO steht dem nicht entgegen (Abs. 4). Die Eingetragenen können Änderungen ihrer **Kontoverbindung** selbst per Datenfernübertragung bewirken (Abs. 5).

**Praktische Bedeutung:** Das Register schafft die Grundlage für die digitale Spendenquittung und macht den Status öffentlich nachprüfbar. **Vor jeder Auskunft zum Verfahrensstand — Vollständigkeit des Datenbestands, Zeitpunkt der öffentlichen Abfragemöglichkeit und Ablösung der Papierbestätigung — ist der aktuelle Umsetzungsstand beim BZSt zu prüfen** `[unverifiziert - prüfen]`. Für die Körperschaft folgt daraus die Obliegenheit, Anschrift und Kontoverbindung aktuell zu halten.

## Quellen

### Statute

- [§ 10b EStG](https://www.gesetze-im-internet.de/estg/__10b.html) (Abs. 1 Höchstbeträge, Abs. 1a Vermögensstock, Abs. 3 Sach- und Aufwandsspende, Abs. 4 Vertrauensschutz und Haftung)
- [§ 34g EStG](https://www.gesetze-im-internet.de/estg/__34g.html), [§ 4 EStG](https://www.gesetze-im-internet.de/estg/__4.html) (Abs. 4 Betriebsausgabe beim Sponsoring), [§ 50 EStDV](https://www.gesetze-im-internet.de/estdv_1955/__50.html)
- [§ 9 Nr. 5 GewStG](https://www.gesetze-im-internet.de/gewstg/__9.html) (Abzug und Veranlasserhaftung mit 15 Prozent), [§ 3 Nr. 6 GewStG](https://www.gesetze-im-internet.de/gewstg/__3.html)
- [§ 5 Abs. 1 Nr. 9 KStG](https://www.gesetze-im-internet.de/kstg_1977/__5.html), [§ 9 KStG](https://www.gesetze-im-internet.de/kstg_1977/__9.html) (Abs. 1 Nr. 2 Zuwendungsabzug)
- [§ 60a AO](https://www.gesetze-im-internet.de/ao_1977/__60a.html), [§ 60b AO](https://www.gesetze-im-internet.de/ao_1977/__60b.html), [§ 63 AO](https://www.gesetze-im-internet.de/ao_1977/__63.html), [§ 47 AO](https://www.gesetze-im-internet.de/ao_1977/__47.html), [§ 191 AO](https://www.gesetze-im-internet.de/ao_1977/__191.html)

### Kommentare

- Hüttemann, Gemeinnützigkeits- und Spendenrecht, 5. Aufl. 2021, Kap. 8 (Spendenrecht und Haftung) `[unverifiziert - Auflagenstand prüfen]`
- Heinicke, in: Schmidt, EStG, § 10b Rn. 1 ff. `[unverifiziert - Auflagenstand prüfen]`
- **BMF-Schreiben** zu Aufwandsspenden und zum **Sponsoring-Erlass**; amtliche Muster für Zuwendungsbestätigungen. **Datum, Aktenzeichen und geltende Fassung jeweils gesondert prüfen** `[unverifiziert - prüfen]`

### Rechtsprechung

> Die tragenden Aussagen dieses Skills folgen unmittelbar aus dem Wortlaut des § 10b EStG und des § 9 Nr. 5 GewStG, die oben verlinkt sind. Zur Auslegung der Werthaltigkeit von Aufwandsspenden und zur groben Fahrlässigkeit im Rahmen des § 10b Abs. 4 EStG ist die BFH-Rechtsprechung **fallbezogen in juris oder Beck-Online** zu recherchieren; hier werden **keine** Aktenzeichen ohne belastbaren Fundstellenbeleg genannt.

## Ausgabeformat

```
ZUWENDUNG / SPENDENHAFTUNG — <Körperschaft> — <Datum>

I.    Status der Körperschaft       [Freistellungsbescheid vom <…> / § 60a AO vom <…>]
        Trägt die Bestätigung:      [✅ / 🔴 Bescheid zu alt oder aufgehoben]
II.   Art der Zuwendung             [Geldspende / Mitgliedsbeitrag / Sachspende / Aufwandsspende]
        Mitgliedsbeitrag abziehbar: [ja / 🔴 nein — § 10b Abs. 1 S. 8 EStG]
III.  Höchstbetrag § 10b Abs. 1     [20 % GdE / 4 ‰ Umsätze+Löhne]  Vortrag: [ja/nein]
        Vermögensstock Abs. 1a:     [1 Mio. EUR über zehn Jahre — beantragt ✅/❌]
IV.   Sachspende § 10b Abs. 3       Herkunft: [Betriebs-/Privatvermögen]
        Bewertung:                  [Entnahmewert + USt / gemeiner Wert / fortgeführte AK-HK]
        Nachweis:                   [✅ / 🔴 keine Wertermittlungsunterlagen]
V.    Aufwandsspende                Anspruch aus [Satzung / Vertrag] vom <…>
        Vor dem Aufwand begründet:  [✅ / 🔴]
        Werthaltigkeit:             [Körperschaft konnte erfüllen ✅ / 🔴]
        Verzicht vom:               <Datum>  Kennzeichnung im Formular: [✅ / 🔴]
VI.   Bestätigung                   [amtliches Muster verwendet ✅ / 🔴 abweichender Wortlaut]
        Verzeichnis geführt:        [✅ / ❌]  Zeichnungsberechtigung: <…>
VII.  Sponsoring-Abgrenzung         [Spende / Sponsoring]
        Sphäre:                     [ideell / Vermögensverwaltung / wirtschaftl. Geschäftsbetrieb]
        Rechnung mit USt:           [erforderlich ✅ / nein]
VIII. Haftung § 10b Abs. 4 EStG     [Ausstellerhaftung / Veranlasserhaftung / kein Anhalt]
        Verschuldensgrad:           [Vorsatz / grobe Fahrlässigkeit / einfache Fahrlässigkeit]
        Haftungsbetrag:             KSt 30 % = EUR <…>  GewSt 15 % = EUR <…>
        Reihenfolge:                [Körperschaft vorrangig — nur bei Veranlasserhaftung]
        Festsetzungsfrist:          [gehemmt nach S. 5 — § 191 Abs. 5 AO nicht anwendbar]
IX.   Zuwendungsempfängerregister   [Daten aktuell ✅/❌]  `[unverifiziert - prüfen]`

Gesamtbefund: [🟢 / 🟡 / 🔴]
Sofortmaßnahmen: <Liste>
```

## Risiken / typische Fehler

- **Aufwandsspende ohne vorher eingeräumten Erstattungsanspruch** — § 10b Abs. 3 S. 5 EStG verlangt einen durch Satzung oder Vertrag begründeten Anspruch; ein nachträglich geschaffener oder unter der Bedingung des Verzichts eingeräumter Anspruch trägt nicht.
- **Aufwandsspende trotz fehlender Werthaltigkeit bescheinigt** — konnte die Körperschaft den Erstattungsanspruch wirtschaftlich nie erfüllen, ist die Bestätigung unrichtig und löst die Ausstellerhaftung aus.
- **Verzicht auf Aufwendungsersatz im Formular nicht angekreuzt** — formaler Fehler mit Haftungsfolge, weil die Bestätigung dann inhaltlich unrichtig ist.
- **Nutzungen und Leistungen als Sachspende bescheinigt** — § 10b Abs. 3 S. 1 EStG nimmt sie ausdrücklich aus; unentgeltliche Arbeitsleistung und Raumüberlassung sind keine abziehbaren Zuwendungen.
- **Sachspende ohne dokumentierte Wertermittlung** — ein überhöhter Wertansatz ist eine unrichtige Bestätigung im Sinne des § 10b Abs. 4 S. 2 EStG.
- **Sponsoring als Spende bescheinigt** — bei Gegenleistung ist eine Rechnung mit Umsatzsteuer zu stellen; die Zuwendungsbestätigung ist unrichtig und die Einnahme regelmäßig dem wirtschaftlichen Geschäftsbetrieb zuzuordnen.
- **Mitgliedsbeitrag eines Sportvereins bescheinigt** — nach § 10b Abs. 1 S. 8 EStG nicht abziehbar; nur die Spende ist es.
- **Haftungsumfang unterschätzt** — 30 Prozent nach § 10b Abs. 4 S. 3 EStG **zuzüglich** 15 Prozent nach § 9 Nr. 5 GewStG, und die Festsetzungsfrist ist nach § 10b Abs. 4 S. 5 EStG gehemmt.
- **Zeichnungsberechtigung nicht begrenzt** — bei der Ausstellerhaftung fehlt die Vorrangregel zugunsten der Körperschaft; die ausstellende Person haftet unmittelbar persönlich.
