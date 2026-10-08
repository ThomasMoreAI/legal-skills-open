---
name: untervermietung-borghei
title: /mietrecht:untervermietung
description: Untervermietung und Gebrauchsüberlassung an Dritte im Wohnraummietrecht – Erlaubnisvorbehalt § 540 BGB und Sonderkündigungsrecht des Mieters, Anspruch auf Gestattung der Teiluntervermietung bei berechtigtem Interesse § 553 Abs. 1 BGB, Untermietzuschlag § 553 Abs. 2 BGB, Abgrenzung zur Aufnahme von Angehörigen und Besuchern, Kurzzeitvermietung und Zweckentfremdung, Abmahnung und Kündigung bei unerlaubter Gebrauchsüberlassung §§ 543 Abs. 2 Nr. 2, 573 Abs. 2 Nr. 1 BGB, Rückgabeanspruch gegen den Untermieter § 546 Abs. 2 BGB. Use when eine Untermieterlaubnis beantragt, erteilt, verweigert oder eine unerlaubte Gebrauchsüberlassung sanktioniert wird.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/mietrecht/skills/untervermietung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: real-estate
language: de
---

# /mietrecht:untervermietung

## Zweck

Zwischen Erlaubnisvorbehalt und Gestattungsanspruch liegt der ganze Streit: § 540 BGB verbietet die Gebrauchsüberlassung ohne Erlaubnis, § 553 BGB gibt dem Mieter unter Voraussetzungen einen **Anspruch** auf sie. Wer die Erlaubnis zu Unrecht verweigert, haftet auf Schadensersatz; wer ohne Erlaubnis untervermietet, riskiert die Kündigung. Diese Skill bestimmt die Grenze, beziffert den Untermietzuschlag und behandelt die Sanktionen beider Richtungen.

## Eingaben

- **Mietvertrag**: Klauseln zur Gebrauchsüberlassung, Personenzahl, Nutzungsvorgaben
- **Vorhaben**: Teil- oder Vollüberlassung, Zahl der Räume, Zeitraum, Person des Dritten
- **Berechtigtes Interesse**: Anlass (Einkommensverlust, Auslandsaufenthalt, Partnerzuzug, Pflege)
- **Wohnungsgröße** und aktuelle Belegung (für die Überbelegungsgrenze)
- **Erlaubnisantrag**: Wortlaut, Datum, benannte Person, Reaktion des Vermieters
- Bei Kurzzeitvermietung: landesrechtliches **Zweckentfremdungsrecht**, Registrierungspflichten
- Bei Sanktion: Abmahnungen, Dauer und Umfang der unerlaubten Überlassung, Mieteinnahmen

## Sub-Agent-Architektur

Die Prüfung wird in Prosa von spezialisierten Schritten getragen; einen `agents`-Block trägt diese Skill bewusst nicht (mietrecht-Konvention). Ein **Tatbestands-Prüfer** klärt zuerst, ob überhaupt eine erlaubnispflichtige Gebrauchsüberlassung vorliegt — die Aufnahme naher Angehöriger ist es nicht. Ein **Anspruchs-Prüfer** bewertet das berechtigte Interesse nach § 553 Abs. 1 BGB und die Verweigerungsgründe. Ein **Zuschlags-Rechner** bestimmt die Zumutbarkeitsgrenze und den angemessenen Untermietzuschlag. Ein **Sanktions-Prüfer** baut Abmahnung und Kündigung auf und prüft parallel den Anspruch gegen den Untermieter. Ein **Öffentlich-rechtlicher Prüfer** behandelt Zweckentfremdung und Registrierungspflichten.

## Ablauf

### 1. Erlaubnispflichtige Gebrauchsüberlassung ([§ 540 Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__540.html))

Der Mieter ist ohne **Erlaubnis des Vermieters** nicht berechtigt, den Gebrauch der Mietsache einem Dritten zu überlassen, insbesondere sie **weiter zu vermieten**. Verweigert der Vermieter die Erlaubnis, kann der Mieter das Mietverhältnis **außerordentlich mit der gesetzlichen Frist kündigen**, sofern nicht in der Person des Dritten ein wichtiger Grund vorliegt (§ 540 Abs. 1 S. 2 BGB) — ein oft übersehenes Sonderkündigungsrecht.

**Keine** erlaubnispflichtige Gebrauchsüberlassung sind:

- die Aufnahme des **Ehegatten oder eingetragenen Lebenspartners** sowie **minderjähriger Kinder**,
- **Besuch** von üblicher Dauer (Richtwert: bis etwa sechs Wochen),
- die Aufnahme von **Pflegepersonal**, soweit zur Betreuung erforderlich.

Erlaubnispflichtig sind dagegen der Zuzug des **nichtehelichen Lebensgefährten**, die Aufnahme volljähriger Kinder in nennenswertem Umfang und jede entgeltliche Untervermietung. Für Verschulden des Untermieters haftet der Mieter nach **§ 540 Abs. 2 BGB** wie für eigenes.

### 2. Anspruch auf Gestattung der Teiluntervermietung ([§ 553 Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__553.html))

Entsteht für den Mieter **nach Abschluss des Mietvertrags** ein **berechtigtes Interesse**, einen **Teil** des Wohnraums einem Dritten zum Gebrauch zu überlassen, so kann er von dem Vermieter die **Erlaubnis verlangen**. Voraussetzungen:

- **Nachträgliche** Entstehung des Interesses — ein bereits bei Vertragsschluss bestehender Plan genügt nicht.
- **Berechtigtes Interesse** — jedes vernünftige, nachvollziehbare persönliche oder wirtschaftliche Interesse: Einkommensverlust, Wunsch nach Kostenentlastung, Zuzug eines Partners, Pflegebedarf, längerer **Auslandsaufenthalt** unter Beibehaltung des Lebensmittelpunkts in der Wohnung (BGH, Urt. v. 11.06.2014 – VIII ZR 349/13, https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2014-06-11&Aktenzeichen=VIII%20ZR%20349/13).
- **Nur ein Teil** des Wohnraums — der Mieter muss den **Gewahrsam** an der Wohnung behalten; ein Zimmer, das er weiter nutzt oder für seine Sachen behält, genügt. Die vollständige Überlassung fällt nicht unter § 553 BGB.

**Verweigerungsgründe (Abs. 1 S. 2):** Der Anspruch besteht nicht, wenn in der Person des Dritten ein **wichtiger Grund** vorliegt (etwa vorheriges Fehlverhalten im Haus), der Wohnraum **übermäßig belegt** würde oder dem Vermieter die Überlassung aus **sonstigen Gründen** nicht zugemutet werden kann. Der Vermieter darf die Person des Untermieters erfahren; ein Anspruch auf umfassende Auskunft über dessen Vermögensverhältnisse besteht nicht.

**Rechtsfolge unberechtigter Verweigerung:** Der Mieter kann die Erlaubnis einklagen und Schadensersatz nach § 280 Abs. 1 BGB verlangen — in Höhe der entgangenen Untermiete.

### 3. Untermietzuschlag ([§ 553 Abs. 2 BGB](https://www.gesetze-im-internet.de/bgb/__553.html))

Ist dem Vermieter die Überlassung nur bei einer **angemessenen Erhöhung der Miete zuzumuten**, kann er die Erlaubnis davon abhängig machen. Der Zuschlag ist keine Beteiligung an der Untermiete, sondern ein Ausgleich für die **Mehrbelastung** — höhere Abnutzung, gestiegene verbrauchsabhängige Kosten, erhöhtes Risiko. Er ist der Höhe nach zu **begründen**; pauschale Prozentsätze der Untermiete oder der Hauptmiete sind angreifbar. Als Orientierung dienen die tatsächliche Mehrbelastung und, wo einschlägig, die Zuschlagsregelungen des preisgebundenen Wohnraums. Zu beachten: Der Zuschlag ist **keine Mieterhöhung nach § 558 BGB** und unterliegt weder Kappungsgrenze noch Wartezeit; er entfällt mit Ende der Untervermietung.

### 4. Kurzzeitvermietung und Zweckentfremdung

Die **gewerbliche Kurzzeitvermietung** über Plattformen ist regelmäßig **nicht** von einer allgemeinen Untermieterlaubnis gedeckt — sie hat eine andere Qualität als die Überlassung an einen bestimmten Untermieter und bedarf einer gesonderten, ausdrücklichen Gestattung. Hinzu treten **öffentlich-rechtliche** Schranken: Zahlreiche Länder und Gemeinden haben **Zweckentfremdungsverbote** mit Genehmigungs- und Registrierungspflichten erlassen; Verstöße sind bußgeldbewehrt und begründen zugleich eine Vertragsverletzung gegenüber dem Vermieter. Das einschlägige Landes- und Ortsrecht ist gesondert zu prüfen.

### 5. Sanktionen bei unerlaubter Gebrauchsüberlassung

**Abmahnung und Unterlassung:** Der Vermieter kann Unterlassung verlangen und muss vor einer Kündigung regelmäßig **abmahnen** ([§ 543 Abs. 3 BGB](https://www.gesetze-im-internet.de/bgb/__543.html)). Die Abmahnung muss die beanstandete Überlassung konkret bezeichnen und eine Frist zur Beendigung setzen.

**Fristlose Kündigung** ([§ 543 Abs. 2 S. 1 Nr. 2 BGB](https://www.gesetze-im-internet.de/bgb/__543.html)): Sie setzt eine **erhebliche** Rechtsverletzung voraus. Erforderlich ist eine Gesamtabwägung; die unerlaubte Überlassung eines einzelnen Zimmers, auf die ein Gestattungsanspruch nach § 553 BGB bestanden hätte, trägt sie regelmäßig **nicht**. Anders bei vollständiger, gewerblicher oder dauerhafter Überlassung trotz Abmahnung.

**Ordentliche Kündigung** ([§ 573 Abs. 2 Nr. 1 BGB](https://www.gesetze-im-internet.de/bgb/__573.html)): schuldhafte, nicht unerhebliche Vertragsverletzung — die praktisch belastbarere Variante; hilfsweise stets mitzuerklären. Vertiefung: `/mietrecht:fristlose-kuendigung-543`.

**Herausgabe der Untermiete?** Ein Anspruch des Vermieters auf Auskehr der erzielten Untermiete besteht grundsätzlich **nicht**; in Betracht kommt allenfalls Schadensersatz bei nachweisbarem Schaden.

### 6. Ansprüche gegen den Untermieter ([§ 546 Abs. 2 BGB](https://www.gesetze-im-internet.de/bgb/__546.html))

Zwischen Vermieter und Untermieter besteht **kein Vertragsverhältnis**. Nach Beendigung des Hauptmietverhältnisses kann der Vermieter die Rückgabe jedoch **unmittelbar vom Dritten** verlangen (§ 546 Abs. 2 BGB); daneben tritt der Herausgabeanspruch aus [§ 985 BGB](https://www.gesetze-im-internet.de/bgb/__985.html). Der Untermieter ist im Räumungsprozess **mitzuverklagen** — ein Titel nur gegen den Hauptmieter ist gegen ihn nicht vollstreckbar; § 940a Abs. 2 ZPO hilft nur bei Besitzerlangung ohne Kenntnis des Vermieters. Das **Untermietverhältnis** endet nicht automatisch mit dem Hauptmietverhältnis; der Untermieter behält Ansprüche gegen den Hauptmieter. Vertiefung: `/mietrecht:raeumungsklage`.

## Quellen

### Statute

- [§ 540 BGB](https://www.gesetze-im-internet.de/bgb/__540.html), [§ 553 BGB](https://www.gesetze-im-internet.de/bgb/__553.html), [§ 546 BGB](https://www.gesetze-im-internet.de/bgb/__546.html), [§ 985 BGB](https://www.gesetze-im-internet.de/bgb/__985.html)
- [§ 543 BGB](https://www.gesetze-im-internet.de/bgb/__543.html), [§ 573 BGB](https://www.gesetze-im-internet.de/bgb/__573.html), [§ 280 BGB](https://www.gesetze-im-internet.de/bgb/__280.html), [§ 558 BGB](https://www.gesetze-im-internet.de/bgb/__558.html)
- [§ 940a ZPO](https://www.gesetze-im-internet.de/zpo/__940a.html); landesrechtliche Zweckentfremdungsverbotsgesetze und kommunale Satzungen (gesondert zu prüfen)

### Kommentare

- Blank, in: Schmidt-Futterer, Mietrecht, 15. Aufl. 2023, § 553 BGB Rn. 1 ff.
- Bieber, in: MüKoBGB, 9. Aufl. 2023, § 540 Rn. 1 ff.; § 553 Rn. 1 ff.
- Weidenkaff, in: Grüneberg, BGB, 84. Aufl. 2025, § 553 Rn. 1 ff.

### Rechtsprechung

- BGH, Urt. v. 11.06.2014 – VIII ZR 349/13 (berechtigtes Interesse an Untervermietung bei längerem Auslandsaufenthalt; Schadensersatz bei pflichtwidriger Verweigerung der Erlaubnis) — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2014-06-11&Aktenzeichen=VIII%20ZR%20349/13
- Zur Bemessung des Untermietzuschlags nach § 553 Abs. 2 BGB ist die einschlägige Rechtsprechung heranzuziehen `[unverifiziert - prüfen]`.
- Zur Erheblichkeitsschwelle des § 543 Abs. 2 S. 1 Nr. 2 BGB bei unerlaubter Untervermietung eines einzelnen Zimmers ist die einschlägige BGH-Rechtsprechung heranzuziehen `[unverifiziert - prüfen]`.

## Formulierungshilfe — Antrag auf Untermieterlaubnis (§ 553 Abs. 1 BGB)

```
Sehr geehrte Damen und Herren,

hiermit beantrage ich gemäß § 553 Abs. 1 BGB die Erlaubnis, einen Teil der
von mir gemieteten Wohnung <Anschrift> unterzuvermieten.

1. Berechtigtes Interesse: Seit <Datum> <konkreter Anlass: Reduzierung
   meines Einkommens durch …, berufsbedingter Auslandsaufenthalt vom
   <Datum> bis <Datum>, Zuzug meiner Partnerin>. Dieses Interesse ist erst
   nach Abschluss des Mietvertrags entstanden.
2. Umfang: Überlassen werden soll ausschließlich das Zimmer <…> mit
   <…> m². Die übrigen Räume nutze ich weiterhin selbst; meine Möbel und
   persönlichen Gegenstände verbleiben in der Wohnung. Ich behalte den
   Gewahrsam und meinen Lebensmittelpunkt in der Wohnung.
3. Person des Untermieters: <Name, Geburtsdatum, derzeitige Anschrift,
   Beruf>. Gründe, die in seiner Person einen wichtigen Grund im Sinne des
   § 553 Abs. 1 S. 2 BGB darstellen könnten, liegen nicht vor.
4. Belegung: Die Wohnung ist mit <…> m² für <…> Personen ausreichend
   groß; eine Überbelegung tritt nicht ein.
5. Untermietzuschlag: Soweit Ihnen die Überlassung nur gegen eine
   angemessene Erhöhung der Miete zuzumuten ist, bitte ich um Mitteilung
   und konkrete Begründung des Zuschlags nach § 553 Abs. 2 BGB.

Ich bitte um Ihre Erlaubnis bis zum <Datum>. Auf mein Recht, die Erlaubnis
gerichtlich durchzusetzen und Schadensersatz in Höhe der entgangenen
Untermiete geltend zu machen, weise ich vorsorglich hin.

Mit freundlichen Grüßen
```

## Ausgabeformat

```
UNTERVERMIETUNG §§ 540, 553 BGB — Prüfung — <Mandat-ID> — <Datum>

I.    Erlaubnispflicht (§ 540 Abs. 1)     [ja / nein — Ehegatte, Kind, Besuch, Pflege]
II.   Umfang                              [Teil der Wohnung / vollständig]
      Gewahrsam des Mieters bleibt        [✅ / ❌ → § 553 BGB nicht anwendbar]
III.  Berechtigtes Interesse (§ 553 Abs. 1) <Anlass>
      Nachträglich entstanden             [✅ / ❌]
IV.   Verweigerungsgründe (§ 553 Abs. 1 S. 2)
      - Wichtiger Grund in der Person     [nein / ja <…>]
      - Übermäßige Belegung               [nein / ja]
      - Sonstige Unzumutbarkeit           [nein / ja <…>]
V.    Untermietzuschlag (§ 553 Abs. 2)    <Betrag>  [begründet / pauschal ⚠️]
VI.   Kurzzeitvermietung / Zweckentfremdung [N/A / Genehmigung erforderlich /
                                             Registrierungspflicht]
VII.  Sanktionen bei unerlaubter Überlassung
      - Abmahnung (§ 543 Abs. 3)          [erfolgt / erforderlich]
      - Fristlos (§ 543 Abs. 2 Nr. 2)     [Erheblichkeit ✅ / ❌]
      - Ordentlich (§ 573 Abs. 2 Nr. 1)   [tragfähig / nicht]
      - Herausgabe der Untermiete         [kein Anspruch]
VIII. Untermieter                          [mitzuverklagen — § 546 Abs. 2, § 985 BGB]
IX.   Sonderkündigungsrecht des Mieters    [§ 540 Abs. 1 S. 2 BGB — Frist <…>]

Ergebnis: <Erlaubnis geschuldet / verweigerbar / Kündigung tragfähig>
Risiko: [🟢 / 🟡 / 🔴]
```

## Risiken / typische Fehler

- **Erlaubnis ohne Grund verweigert** — der Mieter kann sie einklagen und Schadensersatz in Höhe der entgangenen Untermiete verlangen (§ 280 Abs. 1 BGB).
- **§ 553 BGB auf vollständige Überlassung angewendet** — der Anspruch besteht nur für einen **Teil** des Wohnraums; bei Vollüberlassung bleibt es beim Erlaubnisvorbehalt des § 540 BGB.
- **Interesse bestand schon bei Vertragsschluss** — dann kein Anspruch nach § 553 Abs. 1 BGB.
- **Untermietzuschlag pauschal bemessen** — der Zuschlag muss die konkrete Mehrbelastung abbilden und begründet werden; er ist keine Beteiligung an der Untermiete.
- **Kurzzeitvermietung als Untervermietung behandelt** — sie ist von einer allgemeinen Erlaubnis nicht gedeckt und kann zusätzlich zweckentfremdungsrechtlich verboten sein.
- **Fristlose Kündigung ohne Abmahnung** — bei § 543 Abs. 2 S. 1 Nr. 2 BGB ist die Abmahnung anders als beim Zahlungsverzug regelmäßig erforderlich.
- **Erheblichkeitsschwelle überschätzt** — bestand ein Gestattungsanspruch nach § 553 BGB, trägt die unerlaubte Überlassung eines Zimmers die fristlose Kündigung regelmäßig nicht.
- **Untermieter nicht mitverklagt** — der Räumungstitel gegen den Hauptmieter ist gegen ihn nicht vollstreckbar.
- **Sonderkündigungsrecht des Mieters übersehen** — § 540 Abs. 1 S. 2 BGB gibt ihm bei Verweigerung ein außerordentliches Kündigungsrecht mit gesetzlicher Frist.
