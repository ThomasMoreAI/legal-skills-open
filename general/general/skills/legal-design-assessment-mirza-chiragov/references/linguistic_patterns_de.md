# Deutsche Sprachmuster — Referenz

Loaded when the audit reaches Step 3 and the document language is German.

This file inventories the patterns that German-language legal-design practice (nach Fischer-Dieskau, Eichhoff-Cyrus, Lerch, Roelcke, Wagner, sowie der Bürgernahen Verwaltungssprache der Bundesregierung) treats as legal-design debt. Detect, count, score — do not rewrite.

The patterns apply to standard juristisches Hochdeutsch. Austrian and Swiss German legal drafting share the baseline; specific divergences are noted in the **Regionale Besonderheiten** section.

## Zu erkennende Muster

### 1. Behördensprache / juristische Floskeln

Wörter und Wendungen, die im Rechtsdeutsch überleben, ohne eine juristische Funktion zu erfüllen. Jede Verwendung zählen.

- **Hier-/Da-Wörter.** *hiermit, hierdurch, hieraus, hierfür, hierauf, hierin, hierzu, hierüber, hierunter, davon, daran, darauf, daraus, dafür, dazu, darüber, darunter* — als unnötige Konjunktionsersatzwörter. (Manche sind unverzichtbar, z. B. *daran* in *daran erinnern*; nur die rein floskelhafte Verwendung kennzeichnen.)
- **Anaphorische Archaismen.** *vorgenannt, vorbenannt, vorbezeichnet, vorstehend, vorerwähnt, obig, obenstehend, vorliegend, gegenständlich* (österr.), *betreffend* als Adjektiv.
- **Floskelhafte Substantive.** *Vorgang, Sachverhalt* (als universaler Platzhalter), *Maßgabe, Maßnahme* (sofern als Inhaltsplatzhalter verwendet).
- **Verstärkungspartikeln ohne Funktion.** *grundsätzlich, im Wesentlichen, in der Regel, gegebenenfalls, soweit, sofern, etwaig.* Jedes davon ist im Einzelfall berechtigt; **hohe Dichte** ist ein verlässliches Signal für defensives Drafting ohne Substanz.
- **Höflichkeitsfloskeln in Vertragstexten.** *gerne, sehr geehrt, in Anbetracht* — verlegen wirkend in Verträgen außerhalb von Präambeln.
- **Lateinische und französische Reststücke außerhalb fester Termini.** *ipso iure, ex nunc, ex tunc, mutatis mutandis* — die echten Termini bleiben; nur Verwendung als Schmuck kennzeichnen.

**Zählung.** Floskeldichte = (Treffer) / (Gesamtwortzahl) × 1.000.

| Dichte (pro 1.000 Wörter) | Stufe |
| --- | --- |
| 0–3 | Grün |
| 4–7 | Gelb |
| 8–12 | Bernstein |
| 13+ | Rot |

### 2. Substantivierung (Nominalstil)

Das prägnanteste Merkmal der deutschen Rechtssprache. Die Umwandlung von Verben in Nominalphrasen zwingt den Leser, das eigentliche Geschehen zu rekonstruieren.

Signale (zählen):

- Nomen auf *-ung, -heit, -keit, -nis, -tum* nach leeren Verben wie *vornehmen, durchführen, erfolgen, vorliegen, gegeben sein, in Anspruch nehmen, zur Anwendung bringen, in Kraft setzen, zur Verfügung stellen, in Anwendung kommen, zur Zahlung bringen*.

  Beispiele: *die Vornahme der Kündigung, die Durchführung der Zahlung, die Inanspruchnahme des Rechts, die Zurverfügungstellung der Räumlichkeiten, das In-Kraft-Setzen.*

- **Funktionsverbgefüge** (FVG) — sprachwissenschaftlich definiert: Verbindung von semantisch verblasstem Verb mit einem Nomen, das den eigentlichen Verbinhalt trägt. Die klassische Liste:

  *zur Anwendung bringen / kommen* (anwenden); *in Anwendung bringen* (anwenden); *zur Durchführung gelangen* (durchgeführt werden); *Ausdruck verleihen* (ausdrücken); *Beachtung schenken* (beachten); *Entscheidung treffen* (entscheiden); *Erwägung ziehen* (erwägen); *Geltung verschaffen* (gelten); *Hilfe leisten* (helfen); *in Erfahrung bringen* (erfahren); *in Frage kommen / stehen* (möglich sein); *in Kraft treten / setzen* (gelten / inkrafttreten); *in Rechnung stellen* (berechnen); *Kenntnis nehmen / erlangen* (erfahren); *Nutzen ziehen* (nutzen); *Rücksicht nehmen* (berücksichtigen); *unter Beweis stellen* (beweisen); *zum Abschluss bringen* (abschließen); *zur Anzeige bringen* (anzeigen); *zur Auszahlung bringen* (auszahlen); *zur Kenntnis bringen* (mitteilen).

  Jedes FVG zählen.

Dichte = (FVG + nominalstil-typische Konstruktionen) / (Gesamtwortzahl) × 1.000.

| Dichte (pro 1.000 Wörter) | Stufe |
| --- | --- |
| 0–6 | Grün |
| 7–12 | Gelb |
| 13–18 | Bernstein |
| 19+ | Rot |

### 3. Passivkonstruktionen

Das Deutsche unterscheidet:

- **Vorgangspassiv** (*werden* + Partizip II): *wird gekündigt, wurde mitgeteilt.*
- **Zustandspassiv** (*sein* + Partizip II): *ist gekündigt, ist eingeräumt.*
- **Modale Passivkonstruktionen** (*sein* + zu + Infinitiv; *sich lassen* + Infinitiv): *ist zu kündigen, lässt sich vereinbaren.*

Alle drei Formen zählen. Die modale *sein-zu-*Konstruktion ist besonders charakteristisch für juristische Texte und sollte separat gezählt werden, weil sie die deontische Modalität (*muss*, *darf*) verschleiert.

Passivdichte = (Vorgangspassiv + Zustandspassiv + modale Passiva) / (finite Verben) × 100.

| Passivdichte | Stufe |
| --- | --- |
| 0–15% | Grün |
| 16–25% | Gelb |
| 26–35% | Bernstein |
| 36%+ | Rot |

Für B2B-Verträge zwischen erfahrenen Vertragsparteien jeden Schwellenwert um 5 Punkte erhöhen.

### 4. Satzlänge und Schachtelsätze

Schachtelsätze sind das prominenteste Identifikationsmerkmal des deutschen Behörden- und Rechtsstils. Mehrfache Einschübe vor dem Hauptverb und nachgestellte Relativsätze über mehrere Ebenen sind verlässliche Signale.

Berechnen:

- Durchschnittliche Satzlänge (Wörter).
- Median.
- Sätze über 30 Wörter ("lange Sätze").
- Sätze über 50 Wörter ("sehr lange Sätze").
- Längster Satz mit Fundort.

| Durchschnittliche Satzlänge | Stufe |
| --- | --- |
| 0–15 | Grün |
| 16–22 | Gelb |
| 23–32 | Bernstein |
| 33+ | Rot |

**Zusatzanalyse "Klammerstellung":** Im Deutschen wird der Hauptsatz oft durch die Verbklammer geprägt (*Der Mieter hat … zu erbringen*). Wenn zwischen dem ersten und dem letzten Teil der Klammer mehr als 20 Wörter stehen, gilt der Satz unabhängig von seiner Gesamtlänge als überlastet — separat kennzeichnen.

### 5. Komposita-Länge

Das Deutsche bildet beliebig lange Komposita. Über die normale Wortbildung hinaus ist die juristische Hyperkomposition (*Grundstücksverkehrsgenehmigungszuständigkeitsübertragungsverordnung* — kein erfundenes Beispiel) ein Lesbarkeitsproblem.

Zählen Komposita mit:

- 4+ Bestandteilen.
- Über 25 Buchstaben.

| Komposita mit 4+ Bestandteilen pro 1.000 Wörter | Stufe |
| --- | --- |
| 0–3 | Grün |
| 4–7 | Gelb |
| 8–12 | Bernstein |
| 13+ | Rot |

### 6. Doppelte Verneinung und gestaffelte Konditionale

*"Keine Partei darf, soweit es ihr nicht unzumutbar wäre, die Mitteilung nicht in einer dem Vertrag entsprechenden Weise unterlassen."*

Erkennen:

- *nicht un-* (negierte Negation als Hedge).
- *nicht … es sei denn …*
- *niemand darf … außer …*

Eine Kette pro 1.000 Wörter = Gelb. Zwei oder mehr = Bernstein. Dreifache verschachtelte Verneinung = Rot.

### 7. Pleonastische und schwerfällige Wendungen

Wo das kürzere Wort denselben Inhalt trägt:

- *zum Zwecke + Gen.* → für / um zu.
- *im Hinblick auf* → für / wegen.
- *unter Berücksichtigung* → angesichts (kontextabhängig).
- *im Zuge* → bei / während.
- *seitens / vonseiten* → von.
- *im Sinne des* → nach.
- *gemäß / nach Maßgabe* → nach (kontextabhängig — *gemäß* ist oft als juristischer Terminus zu erhalten).
- *insoweit* → soweit (kontextabhängig).
- *insofern* → soweit.
- *im Übrigen* → sonst (sofern stilistisch tragbar).
- *erforderlichenfalls* → wenn nötig.
- *zwecks* → für / um zu.

Zählen, in der Schlussliste der Aufmerksamkeitspunkte aufführen.

### 8. Querverweisdichte

Interne Verweise zählen: "im Sinne des § 5 dieser AGB", "vorbehaltlich Ziffer 7", "gemäß Anlage B".

| Querverweise pro 1.000 Wörter | Stufe |
| --- | --- |
| 0–6 | Grün |
| 7–12 | Gelb |
| 13–20 | Bernstein |
| 21+ | Rot |

Besonders kennzeichnen:
- Verweisketten (Verweis auf eine Klausel, die ihrerseits verweist).
- Verweise auf nicht beigefügte Anlagen.

## Punktwert für die Säule "Sprachmuster" (Deutsch)

Die acht Subscores zu gleichen Teilen auf 0–100 mappen:

1. Floskeldichte
2. Substantivierungsdichte
3. Passivdichte
4. Satzlänge (Durchschnitt)
5. Komposita-Länge
6. Doppelte Verneinungen
7. Pleonastische Wendungen
8. Querverweisdichte

Konversion pro Subscore:

- Grün → 90.
- Gelb → 70.
- Bernstein → 45.
- Rot → 20.

Säulenscore = gerundeter Mittelwert.

## Regionale Besonderheiten

- **Deutschland.** § 305–310 BGB legen den Maßstab für AGB-Recht fest; juristische Klauseln, die nach diesen Vorschriften unwirksam wären, gehören in die Säule "Versteckte Bedingungen" oder "Gesetzeswiederholung" — nicht in die Sprachmuster.
- **Österreich.** Eigenständiges Vokabular: *Erkenntnis* statt *Urteil* (Verwaltungsrecht), *Pönale* statt *Vertragsstrafe*, *Vorlagebeschluss* statt *Vorlagebeschluss* (terminologisch identisch, aber häufiger). KSchG anstelle des deutschen AGG-Maßstabs.
- **Schweiz (Deutschschweiz).** OR (Obligationenrecht) statt BGB; *ß* wird durchgängig zu *ss*. Standarddeutsch in der Schweizer Rechtssprache enthält Helvetismen (*allfällig* anstelle *etwaig*, *anbegehren*, *vorgenommen werden* in spezifischer Bedeutung).
- **Liechtenstein.** PGR (Personen- und Gesellschaftsrecht) eigenes Konstrukt; ansonsten österreichisch geprägt.

## Quellen

- Fischer-Dieskau, J. et al. *Bürgernahe Verwaltungssprache* (Bundesinnenministerium, jeweils aktuelle Fassung).
- Eichhoff-Cyrus, K. & Antos, G. (Hrsg.). *Verständlichkeit als Bürgerrecht?*
- Lerch, K. D. (Hrsg.). *Recht verstehen — Verständlichkeit, Missverständlichkeit und Unverständlichkeit von Recht.*
- Roelcke, T. *Fachsprachen.*
- Wagner, H. *Die deutsche Verwaltungssprache der Gegenwart.*
- Daum, U. *Rechtssprache — eine genormte Fachsprache?*

Diese Quellen stützen die Norm; nicht im Bericht zitieren, außer auf Wunsch.
