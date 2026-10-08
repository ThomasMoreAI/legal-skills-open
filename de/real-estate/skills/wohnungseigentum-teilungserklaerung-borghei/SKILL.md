---
name: wohnungseigentum-teilungserklaerung-borghei
title: /immobilien-grundbuchrecht:wohnungseigentum-teilungserklaerung
description: Begründung von Wohnungseigentum und Gestaltung der Teilungserklärung – vertragliche Einräumung § 3 WEG gegenüber Teilung durch den Alleineigentümer § 8 WEG, Inhalt der Teilungserklärung und Gemeinschaftsordnung, Abgrenzung von Sondereigentum und Gemeinschaftseigentum § 5 WEG einschließlich der zwingend gemeinschaftlichen Bestandteile, Sondernutzungsrechte und ihre Verdinglichung § 10 Abs. 3 WEG, Aufteilungsplan und Abgeschlossenheitsbescheinigung § 7 WEG, Grundbuchvollzug und Änderung der Gemeinschaftsordnung. Use when eine Teilungserklärung entworfen oder geprüft, die Zuordnung eines Bauteils zu Sonder- oder Gemeinschaftseigentum geklärt oder eine Gemeinschaftsordnung geändert werden soll.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/immobilien-grundbuchrecht/skills/wohnungseigentum-teilungserklaerung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: real-estate
language: de
---

# /immobilien-grundbuchrecht:wohnungseigentum-teilungserklaerung

## Zweck

Die Teilungserklärung ist die Verfassung einer Wohnungseigentümergemeinschaft: Sie entscheidet auf Jahrzehnte, wem welches Bauteil gehört, wer welche Kosten trägt und welche Mehrheiten künftig nötig sind. Fehler darin sind später nur mit **Zustimmung aller** oder über eine gerichtlich erzwungene Anpassung zu korrigieren — deshalb liegt der gesamte Aufwand in der Gestaltung, nicht in der Reparatur. Dieser Skill entwirft und prüft Teilungserklärung, Gemeinschaftsordnung und Sondernutzungsrechte bis zur Grundbuchreife.

> **Abgrenzung:** Der laufende Betrieb der Gemeinschaft liegt im Plugin `wohnungseigentumsrecht`. Für Beschlussanfechtung siehe `/wohnungseigentumsrecht:beschlussanfechtung`, für die Jahresabrechnung `/wohnungseigentumsrecht:hausgeldabrechnung`, für Umbauten `/wohnungseigentumsrecht:bauliche-veraenderung`. Dieser Skill behandelt ausschließlich die **Begründungs- und Gestaltungsebene**.

## Eingaben

- **Weg der Begründung**: vertragliche Einräumung durch Miteigentümer (§ 3 WEG) oder Teilung durch den Alleineigentümer (§ 8 WEG)
- **Grundstück** und Grundbuchstand; bestehende Belastungen in Abteilung II und III und deren Gläubiger
- **Bauliche Situation**: Anzahl und Lage der Einheiten, Keller, Stellplätze, Dachboden, Gewerbeeinheiten
- **Aufteilungsplan** und Stand der **Abgeschlossenheitsbescheinigung**
- Gewünschte **Miteigentumsanteile** und deren Bezugsgröße (Wohnfläche, Verkehrswert)
- Geplante **Sondernutzungsrechte** (Gartenflächen, Stellplätze, Terrassen, Kellerräume)
- Regelungswünsche für die **Gemeinschaftsordnung**: Kostenverteilung, Nutzungsbeschränkungen, Verwalterbefugnisse, Öffnungsklausel
- Bei Änderung: geltende Fassung, gewünschte Änderung, Zustimmungsbereitschaft, dinglich Berechtigte

## Sub-Agent-Architektur

1. **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) beschafft WEG in der Fassung des WEMoG, GBO und Kommentarstellen (Bärmann, Jennißen, Hügel/Elzer) sowie die BGH-Linien zur Sondereigentumsfähigkeit.
2. **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) formuliert Teilungserklärung, Gemeinschaftsordnung und Grundbuchanträge.
3. **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft Abgeschlossenheit, Zuordnung, Verdinglichung der Sondernutzungsrechte und Zustimmungserfordernisse.

## Ablauf

### 1. Begründungsweg: § 3 WEG oder § 8 WEG ([§ 3 WEG](https://www.gesetze-im-internet.de/woeigg/__3.html), [§ 8 WEG](https://www.gesetze-im-internet.de/woeigg/__8.html))

- **§ 3 WEG — vertragliche Einräumung:** Mehrere Miteigentümer räumen sich durch **Vertrag** wechselseitig Sondereigentum an bestimmten Wohnungen ein. Erforderlich ist die Einigung aller Miteigentümer; Form und Vollzug folgen dem Grundbuchverfahren (§§ 4, 7 WEG). Typisch bei Baugemeinschaften und bei nachträglicher Aufteilung unter Geschwistern.
- **§ 8 WEG — Teilung durch den Eigentümer:** Der **Alleineigentümer** teilt das Grundstück durch **einseitige Erklärung gegenüber dem Grundbuchamt** in Miteigentumsanteile, mit denen jeweils Sondereigentum verbunden ist. Das ist der Regelweg des Bauträgers, weil er ohne Mitwirkung Dritter funktioniert. Die Erklärung bedarf keiner Beurkundung, wohl aber der Form des [§ 29 GBO](https://www.gesetze-im-internet.de/gbo/__29.html); in der Praxis wird beurkundet, weil die Gemeinschaftsordnung mitgeregelt wird.

Wesentlich für beide Wege: Das Wohnungseigentum entsteht erst mit **Anlegung der Wohnungsgrundbücher** ([§ 7 WEG](https://www.gesetze-im-internet.de/woeigg/__7.html)). Nach § 8 Abs. 1 WEG kann seit dem WEMoG auch Sondereigentum an **außerhalb des Gebäudes liegenden Teilen des Grundstücks** begründet werden (Stellplätze, Terrassen, Gartenanteile) — das verdrängt in vielen Fällen das früher notwendige Sondernutzungsrecht.

### 2. Teilungserklärung und Gemeinschaftsordnung

Die **Teilungserklärung** im engeren Sinn enthält den sachenrechtlichen Teil: Bildung der Miteigentumsanteile, Zuordnung des Sondereigentums, Bezugnahme auf Aufteilungsplan und Abgeschlossenheitsbescheinigung, Grundbuchanträge.

Die **Gemeinschaftsordnung** ist der schuldrechtlich-organisatorische Teil, der durch Eintragung **Inhalt des Sondereigentums** wird ([§ 10 Abs. 3 WEG](https://www.gesetze-im-internet.de/woeigg/__10.html)) und damit gegen Sondernachfolger wirkt. Sie regelt insbesondere:

- **Kostenverteilung** abweichend vom gesetzlichen Maßstab der Miteigentumsanteile ([§ 16 Abs. 2 WEG](https://www.gesetze-im-internet.de/woeigg/__16.html)),
- **Nutzungsbeschränkungen** (Wohnnutzung, Gewerbeverbot, Tierhaltung, kurzzeitige Vermietung),
- **Instandhaltungspflichten** einzelner Eigentümer für Bauteile des Gemeinschaftseigentums (Fenster, Balkone) — nur wirksam, wenn Kostentragung und Pflicht klar zugewiesen sind,
- **Stimmrechtsprinzip** (Kopf-, Objekt- oder Wertprinzip),
- **Öffnungsklausel**: die praktisch wichtigste Regelung überhaupt, weil sie die spätere Änderung mit qualifizierter Mehrheit statt Allstimmigkeit ermöglicht.

Auslegungsgrundsatz: Die Gemeinschaftsordnung wird als Grundbuchinhalt **objektiv-normativ** ausgelegt — maßgeblich ist der Wortlaut und Sinn, wie er sich für einen unbefangenen Betrachter als nächstliegende Bedeutung ergibt; Umstände außerhalb der Eintragung und der Bezugsurkunde bleiben außer Betracht.

### 3. Sondereigentum und Gemeinschaftseigentum ([§ 5 WEG](https://www.gesetze-im-internet.de/woeigg/__5.html))

**Sondereigentumsfähig** sind die in § 5 Abs. 1 WEG genannten Räume sowie die zu ihnen gehörenden Bestandteile, die verändert, beseitigt oder eingefügt werden können, **ohne** das Gemeinschaftseigentum oder ein auf Sondereigentum beruhendes Recht eines anderen Wohnungseigentümers zu beeinträchtigen und ohne die äußere Gestalt des Gebäudes zu verändern.

**Zwingend Gemeinschaftseigentum** (§ 5 Abs. 2 WEG) sind Teile, die für den **Bestand oder die Sicherheit** des Gebäudes erforderlich sind, sowie Anlagen und Einrichtungen, die dem **gemeinschaftlichen Gebrauch** dienen — auch wenn sie im Bereich einer Sondereigentumseinheit liegen. Eine anderslautende Zuweisung in der Teilungserklärung ist insoweit **unwirksam**. Dazu zählen tragende Wände und Decken, Fundament, Dach, Fassade, Treppenhaus, Versorgungsleitungen bis zur Abzweigung sowie Fenster einschließlich Rahmen.

Die Kerntestfrage lautet daher stets: **Kann das Bauteil entfernt werden, ohne Bestand, Sicherheit oder äußere Gestalt zu berühren?** Beispiel aus der Rechtsprechung: Bei einer Doppelstockgarage erstreckt sich das Sondereigentum auf die dazugehörige Hebeanlage (BGH, Urt. v. 21.10.2011 – V ZR 75/11 — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2011-10-21&Aktenzeichen=V%20ZR%2075/11). Nach § 5 Abs. 4 WEG können Vereinbarungen über das Verhältnis der Wohnungseigentümer zum Inhalt des Sondereigentums gemacht werden.

### 4. Sondernutzungsrechte

Ein **Sondernutzungsrecht** schließt die übrigen Eigentümer vom Gebrauch eines Teils des **Gemeinschaftseigentums** aus, ohne dass Sondereigentum entsteht. Es ist kein dingliches Recht eigener Art, sondern eine Vereinbarung, die durch **Eintragung im Grundbuch** nach § 10 Abs. 3 WEG gegen Sondernachfolger wirkt — ohne Eintragung bindet sie nur die derzeitigen Eigentümer. Gestaltungsregeln:

- Der Gegenstand muss **eindeutig bestimmt** sein: Verweis auf eine im Aufteilungsplan oder einem beigefügten Lageplan schraffierte, nummerierte Fläche.
- Die **Kostentragung** für die zugewiesene Fläche ist ausdrücklich zu regeln; sonst bleibt es beim gesetzlichen Verteilungsschlüssel und der Berechtigte nutzt auf Kosten aller.
- Bei Teilung nach § 8 WEG behält sich der teilende Eigentümer regelmäßig vor, Sondernutzungsrechte **später zuzuweisen** (Zuweisungsvorbehalt); dieser Vorbehalt muss eingetragen sein.
- Seit dem WEMoG ist zu prüfen, ob statt eines Sondernutzungsrechts **echtes Sondereigentum** an der Außenfläche nach § 3 Abs. 1 S. 2 WEG begründet werden kann — das ist rechtssicherer und beleihungsfreundlicher.

### 5. Aufteilungsplan und Abgeschlossenheitsbescheinigung ([§ 7 WEG](https://www.gesetze-im-internet.de/woeigg/__7.html))

Zur Anlegung der Wohnungsgrundbücher sind der Eintragungsbewilligung beizufügen: ein **Aufteilungsplan** — eine von der Baubehörde mit Unterschrift und Siegel versehene Bauzeichnung, aus der die Aufteilung des Gebäudes sowie die Lage und Größe der im Sondereigentum und der im gemeinschaftlichen Eigentum stehenden Gebäudeteile ersichtlich sind — und die **Abgeschlossenheitsbescheinigung** der Baubehörde. Alle zu derselben Einheit gehörenden Räume sind mit **derselben Nummer** zu kennzeichnen; die Nummerierung muss mit der Teilungserklärung übereinstimmen. Weicht der tatsächliche Bau vom Aufteilungsplan ab, entsteht Sondereigentum nur in dem Umfang, in dem sich Plan und Bau decken — die Folge sind "Luftgrundbücher" und jahrelange Streitigkeiten. Die Abgeschlossenheitsbescheinigung ist eine **baurechtliche**, keine wohnungseigentumsrechtliche Prüfung; sie ersetzt keine Baugenehmigung für eine geänderte Nutzung.

### 6. Änderung der Gemeinschaftsordnung

Weil die Gemeinschaftsordnung Inhalt des Sondereigentums ist, erfordert ihre Änderung im Grundsatz eine **Vereinbarung aller Wohnungseigentümer** und deren **Eintragung** im Grundbuch; zusätzlich ist die Zustimmung **dinglich Berechtigter** (Grundpfandgläubiger) einzuholen, soweit deren Rechte beeinträchtigt werden. Drei Erleichterungen:

1. **Öffnungsklausel** in der Gemeinschaftsordnung: ermöglicht die Änderung durch Beschluss mit der dort bestimmten Mehrheit. Ein solcher Beschluss wirkt gegen Sondernachfolger auch ohne Eintragung ([§ 10 Abs. 3 WEG](https://www.gesetze-im-internet.de/woeigg/__10.html)); zur Klarheit sollte er dennoch eingetragen werden.
2. **Gesetzliche Beschlusskompetenzen** seit dem WEMoG, insbesondere zur Kostenverteilung im Einzelfall (§ 16 Abs. 2 S. 2 WEG) und zu baulichen Veränderungen (§ 20 WEG).
3. **Anspruch auf Anpassung** nach [§ 10 Abs. 2 WEG](https://www.gesetze-im-internet.de/woeigg/__10.html): Jeder Wohnungseigentümer kann eine vom Gesetz abweichende Vereinbarung oder deren Anpassung verlangen, soweit ein Festhalten aus schwerwiegenden Gründen unter Berücksichtigung aller Umstände unbillig erscheint. Das ist eine **hohe Schwelle** und kein Werkzeug für bloß unpraktische Regelungen.

Ein Beschluss ohne Beschlusskompetenz ist **nichtig**, nicht nur anfechtbar — der Unterschied entscheidet, ob die Monatsfrist des Anfechtungsrechts überhaupt eine Rolle spielt. Vertiefung: `/wohnungseigentumsrecht:beschlussanfechtung`.

## Deterministische Berechnung

Der Geschäftswert einer Teilungserklärung und die Kosten eines Streits über die Anpassung der Gemeinschaftsordnung sind Arithmetik; der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) macht **nur diese**. Die Bestimmung des Geschäftswerts nach § 49 GNotKG bzw. des Streitwerts in WEG-Sachen bleibt juristische Eingabe. Ein **GNotKG-Modul ist nicht implementiert**; Notarkosten sind gegen KV GNotKG von Hand zu ermitteln.

```bash
# Kosten eines Verfahrens über die Anpassung der Gemeinschaftsordnung
python -m scripts.legal_calc.cli rvg --wert 25000 --posten verfahren termin
python -m scripts.legal_calc.cli gkg --wert 25000 --faktor 3.0

# Monatsfrist der Beschlussanfechtung ab Beschlussfassung (§ 45 WEG)
python -m scripts.legal_calc.cli frist --ereignis 15.01.2026 --menge 1 --einheit monate --land BY
```

`--json` liefert die Rechenschritte samt Normzitat. Die RVG-/GKG-Tabellen tragen ein `stand`-Feld; vor Verwendung gegen die aktuelle Anlage 2 prüfen.

## Quellen

### Statute

- [§ 1 WEG](https://www.gesetze-im-internet.de/woeigg/__1.html), [§ 3 WEG](https://www.gesetze-im-internet.de/woeigg/__3.html), [§ 5 WEG](https://www.gesetze-im-internet.de/woeigg/__5.html), [§ 7 WEG](https://www.gesetze-im-internet.de/woeigg/__7.html), [§ 8 WEG](https://www.gesetze-im-internet.de/woeigg/__8.html)
- [§ 10 WEG](https://www.gesetze-im-internet.de/woeigg/__10.html) (Vereinbarungen, Anpassung, Wirkung gegen Sondernachfolger), [§ 16 WEG](https://www.gesetze-im-internet.de/woeigg/__16.html), [§ 20 WEG](https://www.gesetze-im-internet.de/woeigg/__20.html)
- [§ 29 GBO](https://www.gesetze-im-internet.de/gbo/__29.html), [§ 13 GBO](https://www.gesetze-im-internet.de/gbo/__13.html), [§ 19 GBO](https://www.gesetze-im-internet.de/gbo/__19.html)

### Kommentare

- Armbrüster, in: Bärmann, WEG, 15. Aufl. 2023, § 5 Rn. 1 ff.; § 8 Rn. 1 ff.
- Hügel, in: Hügel/Elzer, WEG, 3. Aufl. 2021, § 3 Rn. 1 ff.; § 7 Rn. 1 ff.
- Schultzky, in: Jennißen, WEG, 8. Aufl. 2024, § 10 Rn. 1 ff.
- Schöner/Stöber, Grundbuchrecht, 16. Aufl. 2020, Rn. 1 ff. (Wohnungsgrundbuch)

### Rechtsprechung

- BGH, Urt. v. 21.10.2011 – V ZR 75/11 (Erstreckung des Sondereigentums an einer Doppelstockgarage auf die dazugehörige Hebeanlage; §§ 3 Abs. 2 S. 2, 5 Abs. 2 WEG) — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2011-10-21&Aktenzeichen=V%20ZR%2075/11
- Zur objektiv-normativen Auslegung der Gemeinschaftsordnung nach ihrer nächstliegenden Bedeutung für einen unbefangenen Betrachter ist die st. Rspr. des BGH heranzuziehen `[unverifiziert - prüfen]`.
- Zu Abweichungen zwischen Aufteilungsplan und tatsächlicher Bauausführung und zu den Folgen für die Entstehung des Sondereigentums ist die einschlägige BGH-Rechtsprechung heranzuziehen `[unverifiziert - prüfen]`. Kein Aktenzeichen ohne eigene Verifikation in juris / Beck-Online übernehmen.

## Formulierungshilfe — Teilungserklärung § 8 WEG

```
Teilungserklärung und Gemeinschaftsordnung

I. Teilung (§ 8 WEG)
Der Eigentümer teilt das Eigentum an dem Grundstück <Gemarkung, Flur,
Flurstück>, eingetragen im Grundbuch von <…>, Blatt <…>, gemäß § 8 WEG in
folgende Miteigentumsanteile, mit denen jeweils Sondereigentum verbunden ist:

  1. <…>/1.000 Miteigentumsanteil, verbunden mit dem Sondereigentum an der
     Wohnung Nr. 1 im Erdgeschoss nebst Kellerraum Nr. 1, im Aufteilungsplan
     jeweils mit "1" bezeichnet;
  2. <…>/1.000 Miteigentumsanteil, verbunden mit dem Sondereigentum an der
     Wohnung Nr. 2 …

II. Aufteilungsplan und Abgeschlossenheit (§ 7 WEG)
Auf den beigefügten, von der Bauaufsichtsbehörde <…> mit Unterschrift und
Siegel versehenen Aufteilungsplan vom <Datum> und die
Abgeschlossenheitsbescheinigung vom <Datum> wird Bezug genommen. Alle zu
derselben Einheit gehörenden Räume tragen dieselbe Nummer.

III. Sondernutzungsrechte
Dem jeweiligen Eigentümer der Einheit Nr. 1 wird das alleinige und
ausschließliche Recht zur Nutzung der im beigefügten Lageplan grün
schraffierten, mit "SNR 1" bezeichneten Gartenfläche eingeräumt; die übrigen
Wohnungseigentümer sind insoweit vom Mitgebrauch ausgeschlossen. Die Kosten
der Unterhaltung, Pflege und Verkehrssicherung dieser Fläche trägt der
Berechtigte allein. Die Eintragung dieser Vereinbarung als Inhalt des
Sondereigentums (§ 10 Abs. 3 WEG) wird bewilligt und beantragt.

IV. Öffnungsklausel
Die Wohnungseigentümer können Vereinbarungen dieser Gemeinschaftsordnung mit
einer Mehrheit von zwei Dritteln aller stimmberechtigten Wohnungseigentümer
und der Hälfte aller Miteigentumsanteile ändern; ausgenommen sind Eingriffe
in die Zuordnung von Sondereigentum, in Sondernutzungsrechte und in das
Verhältnis der Miteigentumsanteile.

V. Grundbuchanträge
Es wird bewilligt und beantragt, für jeden vorgenannten Miteigentumsanteil
ein besonderes Wohnungsgrundbuchblatt anzulegen und die vorstehenden
Vereinbarungen als Inhalt des Sondereigentums einzutragen.
```

## Ausgabeformat

```
TEILUNGSERKLÄRUNG / WEG-BEGRÜNDUNG — <Entwurf / Prüfung / Änderung> — <Datum>

I.    Begründungsweg              [§ 3 WEG Vertrag / § 8 WEG einseitig]
II.   Miteigentumsanteile         Summe = 1.000/1.000 [✅ / ❌]
      Bezugsgröße                 <Wohnfläche / Verkehrswert>
III.  Zuordnung § 5 WEG
      - Sondereigentumsfähig      <Aufzählung>
      - Zwingend Gemeinschaft     Dach, Fassade, tragende Teile, Fenster …
      - Fehlzuweisungen           [keine / 🔴 unwirksam: <…>]
IV.   Sondernutzungsrechte        Gegenstand bestimmt [✅ / ⚠️]
      Eintragung § 10 Abs. 3 WEG  [✅ / 🔴 nur schuldrechtlich]
      Kostentragung geregelt      [✅ / ❌]
      Alternative Sondereigentum  [geprüft / nicht geprüft]
V.    Aufteilungsplan § 7 WEG     Siegel + Unterschrift [✅ / ❌]
      Abgeschlossenheit           vom <Datum>
      Nummerierung deckungsgleich [✅ / 🔴 Abweichung Bau/Plan]
VI.   Gemeinschaftsordnung
      - Kostenverteilung § 16     <Schlüssel>
      - Nutzungsbeschränkungen    <…>
      - Stimmprinzip              [Kopf / Objekt / Wert]
      - Öffnungsklausel           [✅ vorhanden / 🔴 fehlt]
VII.  Änderung                    [Vereinbarung aller / Öffnungsklausel /
                                   § 10 Abs. 2 WEG Anpassung]
      Zustimmung dinglich Ber.    [erforderlich / erteilt / offen]
VIII. Querverweise                /wohnungseigentumsrecht:beschlussanfechtung,
                                  :hausgeldabrechnung, :bauliche-veraenderung
IX.   Kosten                      s. Deterministische Berechnung

Ergebnis: <grundbuchreif / nachbessern / nicht vollzugsfähig>
Risiko: [🟢 / 🟡 / 🔴]
```

## Risiken / typische Fehler

- **Zwingendes Gemeinschaftseigentum zum Sondereigentum erklärt** — Dach, Fassade, tragende Wände und Fenster sind nach § 5 Abs. 2 WEG nicht sondereigentumsfähig; die Zuweisung ist unwirksam und die Kostenregelung läuft leer.
- **Sondernutzungsrecht nicht eingetragen** — ohne Eintragung nach § 10 Abs. 3 WEG bindet es keinen Sondernachfolger; der Erwerber der Nachbareinheit kann den Garten mitbenutzen.
- **Sondernutzungsfläche nicht eindeutig bestimmt** — ohne schraffierten, nummerierten Plan ist das Recht nicht vollzugsfähig und im Streit nicht durchsetzbar.
- **Abweichung zwischen Aufteilungsplan und Bauausführung** — Sondereigentum entsteht nur, soweit Plan und Bau sich decken; die Folge sind Luftgrundbücher und Nachtragsurkunden.
- **Keine Öffnungsklausel aufgenommen** — jede spätere Änderung erfordert die Zustimmung aller Eigentümer und der dinglich Berechtigten; § 10 Abs. 2 WEG hilft nur bei schwerwiegenden Gründen.
- **Instandhaltungspflicht ohne Kostenzuweisung** — die Übertragung der Pflicht für Fenster oder Balkone auf den einzelnen Eigentümer ohne klare Kostenregelung erzeugt Dauerstreit.
- **Beschlusskompetenz verwechselt** — ein Beschluss, der eine Vereinbarung ohne Öffnungsklausel ändert, ist nichtig und nicht bloß anfechtbar; die Anfechtungsfrist ist dann irrelevant.
