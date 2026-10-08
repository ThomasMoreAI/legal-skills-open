---
name: mietmangel-minderung-borghei
title: /mietrecht:mietmangel-minderung
description: Mietmangel und Mietminderung im Wohnraummietrecht – Mangelbegriff und kraft Gesetzes eintretende Minderung § 536 BGB, Ausschluss bei Kenntnis § 536b BGB, Schadensersatz und Selbstvornahme mit Aufwendungsersatz § 536a BGB, Mängelanzeige und Anzeigeobliegenheit § 536c BGB, Zurückbehaltungsrecht § 320 BGB, Symptomtheorie und Darlegungslast, Minderungsquote und Bezugsgröße Bruttomiete. Use when ein Mieter wegen eines Mangels mindern, Mängelbeseitigung verlangen oder Schadensersatz geltend machen will oder ein Vermieter eine Minderung prüft.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/mietrecht/skills/mietmangel-minderung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: real-estate
language: de
---

# /mietrecht:mietmangel-minderung

## Zweck

Die Minderung tritt **kraft Gesetzes** ein — sie muss nicht erklärt werden. Genau das erzeugt die typische Fehlkonstellation: Der Mieter mindert zu hoch oder ohne Anzeige, gerät in Zahlungsrückstand und verliert die Wohnung. Diese Skill bestimmt den Mangel, die Bezugsgröße, die Quote und die Grenzen der Minderung, ordnet Zurückbehaltungsrecht und Selbstvornahme ein und formuliert die Mängelanzeige, an der in der Praxis fast alles hängt.

## Eingaben

- **Mangelbeschreibung**: Erscheinungsbild, betroffene Räume, Beginn, Dauer, Intensität, Jahreszeit
- **Mietvertrag**: vereinbarte Beschaffenheit, Wohnflächenangabe, Zustand bei Übergabe
- **Bruttomiete** (Grundmiete + Vorauszahlungen) — Bezugsgröße der Minderung
- **Mängelanzeige**: Datum, Form, Zugangsnachweis, Reaktion des Vermieters
- Ob der Mangel bei Vertragsschluss **bekannt** oder grob fahrlässig unbekannt war
- Ob bereits **gemindert** wurde und in welcher Höhe; Zahlungsstand
- Bei Selbstvornahme: Kostenbelege, Zustand des Verzugs

## Sub-Agent-Architektur

Die Prüfung wird in Prosa von spezialisierten Schritten getragen; einen `agents`-Block trägt diese Skill bewusst nicht (mietrecht-Konvention). Ein **Mangel-Prüfer** bestimmt die vertraglich geschuldete Sollbeschaffenheit und stellt die Abweichung fest — ohne Sollbeschaffenheit gibt es keinen Mangel. Ein **Anzeige-Prüfer** kontrolliert Mängelanzeige, Zugang und die Folgen ihrer Unterlassung nach § 536c Abs. 2 BGB. Ein **Quoten-Rechner** bestimmt Bezugsgröße, Zeitraum und Höhe der Minderung. Ein **Sekundäranspruchs-Prüfer** untersucht Schadensersatz, Aufwendungsersatz, Selbstvornahme und Zurückbehaltungsrecht. Ein **Risiko-Prüfer** spiegelt die vorgenommene Minderung gegen die Kündigungsschwelle des § 543 Abs. 2 Nr. 3 BGB.

## Ablauf

### 1. Mangelbegriff und Sollbeschaffenheit ([§ 536 Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__536.html))

Ein **Sachmangel** liegt vor, wenn die Mietsache zur Zeit der Überlassung mit einem Fehler behaftet ist, der ihre **Tauglichkeit zum vertragsgemäßen Gebrauch aufhebt oder mindert**, oder wenn ein solcher Fehler später entsteht. Maßstab ist die **vertraglich vereinbarte Sollbeschaffenheit**; fehlt eine ausdrückliche Vereinbarung, ist auf den bei Vertragsschluss üblichen Standard der Baualtersklasse abzustellen. Eine **unerhebliche** Minderung der Tauglichkeit bleibt außer Betracht (§ 536 Abs. 1 S. 3 BGB). Auch das **Fehlen einer zugesicherten Eigenschaft** (Abs. 2) und **Rechtsmängel** (§ 536 Abs. 3 BGB) sind erfasst. Eine Wohnflächenunterschreitung von **mehr als 10 %** ist ein Mangel (BGH, Urt. v. 24.03.2004 – VIII ZR 295/03, https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2004-03-24&Aktenzeichen=VIII%20ZR%20295/03); eine Flächenvereinbarung kann auch konkludent zustande kommen (BGH, Urt. v. 23.06.2010 – VIII ZR 256/09, https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2010-06-23&Aktenzeichen=VIII%20ZR%20256/09).

### 2. Symptomtheorie und Darlegungslast

Nach der **Symptomtheorie** genügt der Mieter seiner Darlegungslast, wenn er das **Mangelsymptom** — die konkrete Beeinträchtigung nach Ort, Zeit und Intensität — beschreibt. Er muss weder die **Ursache** benennen noch die Verantwortlichkeit zuordnen; das ist Sache des Vermieters und gegebenenfalls des Sachverständigen. Ein Mangelbeseitigungsverlangen ist daher nicht deshalb unschlüssig, weil der Mieter die bautechnische Ursache nicht kennt. Praktisch: Symptomprotokoll führen (Datum, Uhrzeit, Raum, Messwert, Foto), nicht nach der Ursache spekulieren.

### 3. Minderung kraft Gesetzes ([§ 536 Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__536.html))

Die Miete ist für die Dauer des Mangels **kraft Gesetzes gemindert** — es bedarf keiner Erklärung und keiner Fristsetzung. Bezugsgröße ist die **Bruttomiete** einschließlich Betriebskostenvorauszahlungen. Die Minderung wirkt ab **Auftreten** des Mangels, nicht erst ab der Anzeige — verspätete Anzeige führt aber über § 536c Abs. 2 BGB zum Verlust. Rückwirkend zu viel gezahlte Miete kann nach [§ 812 BGB](https://www.gesetze-im-internet.de/bgb/__812.html) zurückgefordert werden. Bei **energetischer Modernisierung** ist die Minderung für **drei Monate ausgeschlossen** (§ 536 Abs. 1a BGB).

### 4. Minderungsquote

Die Quote bemisst sich nach dem **Verhältnis des Gebrauchswerts der mangelhaften zur mangelfreien Sache**. Sie ist tatrichterlich zu schätzen ([§ 287 ZPO](https://www.gesetze-im-internet.de/zpo/__287.html)); sogenannte Minderungstabellen sind **Orientierungshilfen ohne Bindungswirkung** und dürfen nie ungeprüft übernommen werden. Zu berücksichtigen sind:

- **Umfang** (betroffene Fläche im Verhältnis zur Gesamtfläche),
- **Intensität** (vollständiger Ausfall oder bloße Beeinträchtigung),
- **Dauer und Zeitraum** (Heizungsausfall im Januar wiegt schwerer als im Juli),
- **Nutzungsart** des betroffenen Raums (Wohn-/Schlafzimmer vs. Abstellraum).

Die Quote ist **zeitanteilig** anzusetzen, wenn der Mangel nicht den ganzen Monat bestand.

### 5. Ausschluss der Minderung ([§ 536b BGB](https://www.gesetze-im-internet.de/bgb/__536b.html), § 536 Abs. 1a BGB)

Kennt der Mieter den Mangel **bei Vertragsschluss**, stehen ihm die Rechte aus §§ 536, 536a BGB nicht zu. Bleibt ihm der Mangel infolge **grober Fahrlässigkeit** unbekannt, gilt dasselbe, sofern der Vermieter den Mangel nicht arglistig verschwiegen hat. Nimmt der Mieter die Sache in **Kenntnis des Mangels vorbehaltlos an**, stehen ihm die Rechte ebenfalls nicht zu (§ 536b S. 2 BGB) — daher bei Übergabe stets **Vorbehalt erklären und protokollieren**. Ein vertraglicher Ausschluss der Minderung ist im Wohnraummietrecht nach [§ 536 Abs. 4 BGB](https://www.gesetze-im-internet.de/bgb/__536.html) **unwirksam**.

### 6. Mängelanzeige ([§ 536c BGB](https://www.gesetze-im-internet.de/bgb/__536c.html))

Zeigt sich im Laufe der Mietzeit ein Mangel oder wird eine Maßnahme zum Schutz der Mietsache erforderlich, hat der Mieter dies dem Vermieter **unverzüglich anzuzeigen**. Unterlässt er die Anzeige, ist er dem Vermieter zum **Ersatz des daraus entstehenden Schadens** verpflichtet (Abs. 2 S. 1) und **verliert** — soweit der Vermieter infolge der Unterlassung nicht abhelfen konnte — die Rechte auf Minderung, Schadensersatz und fristlose Kündigung (Abs. 2 S. 2). Die Anzeige ist formfrei, sollte aber in **Textform mit Zugangsnachweis** erfolgen.

### 7. Schadensersatz und Selbstvornahme ([§ 536a BGB](https://www.gesetze-im-internet.de/bgb/__536a.html))

**Schadensersatz (Abs. 1):** Der Vermieter haftet für anfängliche Mängel **verschuldensunabhängig** (Garantiehaftung), für später entstandene Mängel nur bei **Vertretenmüssen** und für die Nichtbeseitigung ab Verzug. Ersatzfähig sind etwa Schäden an eingebrachten Sachen, Gesundheitsschäden, Mehrkosten für Ersatzunterkunft.

**Aufwendungsersatz und Selbstvornahme (Abs. 2):** Der Mieter kann den Mangel **selbst beseitigen und Ersatz der erforderlichen Aufwendungen** verlangen, wenn

- der Vermieter mit der Beseitigung **in Verzug** ist (Nr. 1) — dafür ist eine **Fristsetzung** erforderlich, oder
- die umgehende Beseitigung zur **Erhaltung oder Wiederherstellung des Bestands** der Mietsache notwendig ist (Nr. 2) — Notmaßnahme, keine Fristsetzung nötig.

Wer ohne Verzug und ohne Notlage selbst beauftragt, bleibt auf den Kosten sitzen. Ein **Vorschuss** auf die Beseitigungskosten kann verlangt werden.

### 8. Zurückbehaltungsrecht ([§ 320 BGB](https://www.gesetze-im-internet.de/bgb/__320.html))

Neben der Minderung kann der Mieter einen weiteren Teil der Miete **zurückbehalten**, um Druck auf die Mangelbeseitigung auszuüben. Das Zurückbehaltungsrecht ist **vorübergehend** — der zurückbehaltene Betrag ist nach Beseitigung des Mangels **nachzuzahlen**, anders als der geminderte Betrag. Die Höhe muss **verhältnismäßig** sein; als grobe Orientierung gilt das Drei- bis Fünffache des Minderungsbetrags. Das Recht entfällt, sobald der Mangel beseitigt ist, und ist nicht auf Zeiträume vor der Anzeige anwendbar.

### 9. Risiko der Überminderung ([§ 543 Abs. 2 S. 1 Nr. 3 BGB](https://www.gesetze-im-internet.de/bgb/__543.html))

Mindert der Mieter zu hoch, entsteht ein **Zahlungsrückstand**; erreicht er die Schwelle des § 543 Abs. 2 S. 1 Nr. 3 BGB, droht die fristlose Kündigung. Ein unverschuldeter Rechtsirrtum über die Quote entlastet nur ausnahmsweise. Empfehlung in Zweifelsfällen: **unter Vorbehalt zahlen** und den Minderungsbetrag anschließend nach § 812 BGB zurückfordern — das trennt die Streitfrage von der Bestandsfrage. Vertiefung: `/mietrecht:fristlose-kuendigung-543`.

## Quellen

### Statute

- [§ 535 BGB](https://www.gesetze-im-internet.de/bgb/__535.html), [§ 536 BGB](https://www.gesetze-im-internet.de/bgb/__536.html), [§ 536a BGB](https://www.gesetze-im-internet.de/bgb/__536a.html), [§ 536b BGB](https://www.gesetze-im-internet.de/bgb/__536b.html), [§ 536c BGB](https://www.gesetze-im-internet.de/bgb/__536c.html)
- [§ 320 BGB](https://www.gesetze-im-internet.de/bgb/__320.html), [§ 812 BGB](https://www.gesetze-im-internet.de/bgb/__812.html), [§ 543 BGB](https://www.gesetze-im-internet.de/bgb/__543.html)
- [§ 287 ZPO](https://www.gesetze-im-internet.de/zpo/__287.html) (Schätzung der Quote)

### Kommentare

- Eisenschmid, in: Schmidt-Futterer, Mietrecht, 15. Aufl. 2023, § 536 BGB Rn. 1 ff.
- Bieber, in: MüKoBGB, 9. Aufl. 2023, § 536 Rn. 1 ff.; § 536a Rn. 1 ff.
- Weidenkaff, in: Grüneberg, BGB, 84. Aufl. 2025, § 536 Rn. 1 ff.

### Rechtsprechung

- BGH, Urt. v. 24.03.2004 – VIII ZR 295/03 (Minderung bei Wohnflächenunterschreitung von mehr als 10 %) — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2004-03-24&Aktenzeichen=VIII%20ZR%20295/03
- BGH, Urt. v. 23.06.2010 – VIII ZR 256/09 (konkludente Wohnflächenvereinbarung) — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2010-06-23&Aktenzeichen=VIII%20ZR%20256/09
- Zur Symptomtheorie und zu den Anforderungen an die Darlegung des Mangelsymptoms ist die einschlägige BGH-Rechtsprechung heranzuziehen `[unverifiziert - prüfen]`.
- Zur Höhe angemessener Minderungsquoten existiert keine bindende Rechtsprechung; Minderungstabellen sind unverbindlich `[unverifiziert - prüfen]`.

## Formulierungshilfe — Mängelanzeige mit Minderungsankündigung

```
Einschreiben / E-Mail mit Lesebestätigung

Sehr geehrte Damen und Herren,

hiermit zeige ich gemäß § 536c Abs. 1 BGB folgenden Mangel der von mir
gemieteten Wohnung <Anschrift, Lage im Haus> an:

Seit dem <Datum> zeigt sich in <Raum> an der <Wand/Decke, Himmelsrichtung>
auf einer Fläche von etwa <…> m² <Beschreibung: dunkle Flecken,
Schimmelbildung, abplatzender Putz>. Die Raumtemperatur beträgt trotz
voll aufgedrehter Heizkörper lediglich <…> °C; die relative Luftfeuchte
liegt bei <…> %. Der Raum ist als <Schlafzimmer> nur eingeschränkt
nutzbar. Fotos vom <Datum> sind beigefügt.

Ich fordere Sie auf, den Mangel bis zum <Datum — angemessene Frist>
zu beseitigen. Nach fruchtlosem Fristablauf werde ich von meinen Rechten
aus § 536a Abs. 2 Nr. 1 BGB Gebrauch machen.

Für die Dauer des Mangels ist die Miete gemäß § 536 Abs. 1 BGB kraft
Gesetzes gemindert. Ich werde ab dem <Monat> eine um <…> % der Bruttomiete
geminderte Miete zahlen und behalte darüber hinaus gemäß § 320 BGB
vorläufig einen Betrag von <…> EUR monatlich zurück; dieser Betrag wird
nach Mangelbeseitigung nachgezahlt.

Zur Terminabstimmung für eine Besichtigung stehe ich zur Verfügung.

Mit freundlichen Grüßen
```

## Ausgabeformat

```
MIETMANGEL / MINDERUNG — Prüfung — <Mandat-ID> — <Datum>

I.    Sollbeschaffenheit                 <vereinbart / üblicher Standard Baujahr …>
II.   Mangel (§ 536 Abs. 1)              [ja / nein / unerheblich]
      Symptombeschreibung                <Ort, Zeit, Intensität>
III.  Ausschlussgründe (§ 536b)          [keine / Kenntnis / grobe Fahrlässigkeit /
                                          vorbehaltlose Annahme]
      Sperre § 536 Abs. 1a (energet.)    [N/A / läuft bis <Datum>]
IV.   Mängelanzeige (§ 536c)             [erfolgt am <Datum> / unterlassen ⚠️]
      Rechtsverlust Abs. 2 S. 2          [nein / ja — Umfang <…>]
V.    Minderung
      Bezugsgröße (Bruttomiete)          <Betrag>
      Quote                              <…> %   Zeitraum: <von> – <bis>
      Minderungsbetrag gesamt            <Betrag>
      Rückforderung § 812 BGB            <Betrag>
VI.   Zurückbehaltungsrecht (§ 320)      <Betrag> monatlich  [nachzahlbar]
VII.  Sekundäransprüche (§ 536a)
      - Schadensersatz Abs. 1            [ja <Betrag> / nein]
      - Selbstvornahme Abs. 2            [Nr. 1 Verzug / Nr. 2 Notmaßnahme / nein]
      - Vorschussanspruch                [ja <Betrag> / nein]
VIII. Kündigungsrisiko (§ 543 Abs. 2 Nr. 3) [🟢 / 🟡 / 🔴]

Ergebnis: <…>
Empfehlung: <Minderung / Zahlung unter Vorbehalt / Beseitigungsklage>
```

## Risiken / typische Fehler

- **Zu hoch gemindert** — der Differenzbetrag ist Zahlungsrückstand und kann die fristlose Kündigung nach § 543 Abs. 2 S. 1 Nr. 3 BGB auslösen; in Zweifelsfällen unter Vorbehalt zahlen.
- **Von der Nettomiete gemindert** — Bezugsgröße ist die **Bruttomiete** einschließlich Vorauszahlungen.
- **Mängelanzeige unterlassen oder nicht nachweisbar** — Rechtsverlust nach § 536c Abs. 2 S. 2 BGB und Schadensersatzpflicht des Mieters.
- **Minderungstabelle ungeprüft übernommen** — die Quote ist einzelfallbezogen zu schätzen; Tabellenwerte binden kein Gericht.
- **Selbstvornahme ohne Verzug** — ohne Fristsetzung und ohne Notlage besteht kein Aufwendungsersatzanspruch nach § 536a Abs. 2 BGB.
- **Vorbehalt bei Übergabe versäumt** — vorbehaltlose Annahme in Kenntnis des Mangels führt zum Rechtsverlust nach § 536b S. 2 BGB.
- **Zurückbehaltung und Minderung verwechselt** — der zurückbehaltene Betrag ist nach Beseitigung nachzuzahlen, der geminderte nicht.
- **Ursachenforschung statt Symptombeschreibung** — die Symptomtheorie verlangt gerade keine Ursachenangabe; wer sich auf eine falsche Ursache festlegt, schwächt den eigenen Vortrag.
