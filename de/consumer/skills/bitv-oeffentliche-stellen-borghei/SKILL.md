---
name: bitv-oeffentliche-stellen-borghei
title: /barrierefreiheit-bfsg:bitv-oeffentliche-stellen
description: Digitale Barrierefreiheit öffentlicher Stellen – Gestaltungspflicht § 12a BGG für Websites, mobile Anwendungen, Intranet und elektronisch unterstützte Verwaltungsabläufe, Ausnahme bei unverhältnismäßiger Belastung § 12a Abs. 6, Erklärung zur Barrierefreiheit § 12b BGG mit Benennung nicht barrierefreier Inhalte, Feedback-Mechanismus und Hinweis auf die Schlichtung nebst Monatsfrist für Antworten, anzuwendende Standards § 3 BITV 2.0 mit Anlage 2, Erläuterungen in Deutscher Gebärdensprache und Leichter Sprache § 4 BITV 2.0, Erklärung § 7 und Überwachungsverfahren § 8 BITV 2.0, Durchsetzung über § 16 BGG und die Verbandsklage § 15 BGG sowie die Abgrenzung zum BFSG. Use when eine Behörde, ein Sozialversicherungsträger oder ein öffentlicher Auftragnehmer Websites, Apps oder Fachverfahren barrierefrei gestalten muss.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/barrierefreiheit-bfsg/skills/bitv-oeffentliche-stellen
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: consumer
language: de
---

# /barrierefreiheit-bfsg:bitv-oeffentliche-stellen

## Zweck

Der Skill deckt das zweite, vom BFSG getrennte Barrierefreiheitsregime ab: die Pflichten öffentlicher Stellen nach dem BGG und der BITV 2.0 in Umsetzung der Richtlinie (EU) 2016/2102. Er bestimmt zuerst, ob Bundes- oder Landesrecht gilt, prüft die Gestaltungspflicht und ihre Ausnahmen, kontrolliert die Erklärung zur Barrierefreiheit auf ihre drei Pflichtbestandteile und benennt Überwachungs- und Durchsetzungswege.

## Eingaben

- Träger: Bund, Land, Kommune, Körperschaft, Beliehener, öffentlicher Auftragnehmer
- Betroffenes Angebot: Website, mobile Anwendung, Intranet, elektronisch unterstützter Verwaltungsablauf, Fachverfahren, grafische Programmoberfläche
- Veröffentlichungsdatum des Angebots
- Vorhandene Erklärung zur Barrierefreiheit und ihr Fundort
- Prüfbericht oder Selbstbewertung nach BITV 2.0
- Eingegangene Mitteilungen über Barrieren und deren Eingangsdatum
- Bei Beschaffung: Vergabeunterlagen und Leistungsbeschreibung

## Sub-Agent-Architektur

Der Researcher beschafft BGG, BITV 2.0 samt Anlage 2, die Richtlinie (EU) 2016/2102, die Landesbehindertengleichstellungsgesetze und Landes-BITV sowie die Veröffentlichungen der Überwachungsstelle des Bundes für Barrierefreiheit von Informationstechnik. Der Drafter erstellt die Befundmatrix und entwirft die Erklärung zur Barrierefreiheit oder die Reaktion auf eine Mitteilung. Der Reviewer prüft die Bund-Länder-Zuordnung, die Vollständigkeit der Erklärung und die Einhaltung der Monatsfrist des § 12b Abs. 4 BGG.

## Ablauf

### 1. Anwendbares Recht bestimmen — Bund oder Land

**Dieser Schritt steht vor allem anderen.** Die Richtlinie (EU) 2016/2102 ist im Bund und in allen sechzehn Ländern getrennt umgesetzt worden:

| Träger | Materielles Recht | Verordnungsebene | Durchsetzung |
|---|---|---|---|
| **Öffentliche Stellen des Bundes** | [§§ 12 bis 12d BGG](https://www.gesetze-im-internet.de/bgg/__12a.html) | [BITV 2.0](https://www.gesetze-im-internet.de/bitv_2_0/) | Überwachungsstelle des Bundes; Schlichtungsstelle [§ 16 BGG](https://www.gesetze-im-internet.de/bgg/__16.html) |
| **Länder, Kommunen, landesunmittelbare Körperschaften** | Landesbehindertengleichstellungsgesetz | Landes-BITV | Landesüberwachungs- und Landesschlichtungsstelle `[unverifiziert – prüfen]` je Land |
| **Private Wirtschaftsakteure gegenüber Verbrauchern** | [BFSG](https://www.gesetze-im-internet.de/bfsg/) + BFSGV | — | Marktüberwachungsbehörden der Länder |

Ein pauschaler Verweis auf „die BITV" ist unzulässig, wenn der Träger dem Landesrecht unterliegt. Die konkrete Landesnorm ist zu benennen.

Nach **§ 12a Abs. 5 BGG** gelten die Pflichten des Abschnitts 2a **nicht** für Websites und mobile Anwendungen öffentlicher Stellen nach § 12 S. 1 Nr. 2 und 3, die keine für die Öffentlichkeit wesentlichen Dienstleistungen und keine speziell auf Menschen mit Behinderungen ausgerichteten Dienstleistungen anbieten.

### 2. Gestaltungspflicht bestimmen ([§ 12a BGG](https://www.gesetze-im-internet.de/bgg/__12a.html))

Öffentliche Stellen des Bundes gestalten **barrierefrei**:

- Websites und mobile Anwendungen, **einschließlich der für die Beschäftigten bestimmten Angebote im Intranet** (Abs. 1 S. 1);
- schrittweise, spätestens bis zum **23.06.2021**, ihre **elektronisch unterstützten Verwaltungsabläufe** einschließlich elektronischer Vorgangsbearbeitung und Aktenführung (Abs. 1 S. 2);
- die **grafischen Programmoberflächen** (Abs. 1 S. 3).

Die Gestaltung erfolgt nach Maßgabe der auf § 12d BGG gestützten Verordnung, im Übrigen nach den **anerkannten Regeln der Technik** (Abs. 2). Bei **Neuanschaffungen, Erweiterungen und Überarbeitungen** ist die Barrierefreiheit bereits bei Planung, Entwicklung, **Ausschreibung und Beschaffung** zu berücksichtigen (Abs. 3) — die Schnittstelle zum Vergaberecht (`/vergaberecht:vergabeunterlagen-leistungsbeschreibung` bzw. die einschlägige Vergabeskill).

Nach **Abs. 6** kann ausnahmsweise abgesehen werden, soweit die barrierefreie Gestaltung die Stelle **unverhältnismäßig belasten** würde. Die Ausnahme ist zu begründen und in der Erklärung nach § 12b offenzulegen — sie ist keine stillschweigende Option.

### 3. Anzuwendende Standards ([§ 3 BITV 2.0](https://www.gesetze-im-internet.de/bitv_2_0/__3.html))

Die BITV 2.0 verweist auf die im Amtsblatt der EU gelisteten harmonisierten Normen; maßgeblich ist **EN 301 549** in der jeweils gelisteten Fassung, ergänzt um die **Anlage 2** zur BITV 2.0 `[unverifiziert – prüfen]` hinsichtlich des aktuellen Fassungsstands. Hinzu treten:

- **[§ 4 BITV 2.0](https://www.gesetze-im-internet.de/bitv_2_0/__4.html)** — Erläuterungen in **Deutscher Gebärdensprache** und in **Leichter Sprache** auf der Startseite: Informationen zum Inhalt, Hinweise zur Navigation und Hinweise auf weitere im Auftritt vorhandene Informationen in Gebärdensprache und Leichter Sprache. Diese Pflicht hat **kein Gegenstück im BFSG** und wird bei Übertragung von Privatprojekten regelmäßig übersehen.
- **[§ 6 BITV 2.0](https://www.gesetze-im-internet.de/bitv_2_0/__6.html)** — Beratung und Unterstützung durch die Bundesfachstelle für Barrierefreiheit.
- **[§ 10 BITV 2.0](https://www.gesetze-im-internet.de/bitv_2_0/__10.html)** — Folgenabschätzung.

### 4. Erklärung zur Barrierefreiheit prüfen ([§ 12b BGG](https://www.gesetze-im-internet.de/bgg/__12b.html), [§ 7 BITV 2.0](https://www.gesetze-im-internet.de/bitv_2_0/__7.html))

Die Erklärung ist zu veröffentlichen und muss **drei** Bestandteile enthalten:

1. Für den Fall, dass ausnahmsweise keine vollständige Barrierefreiheit erreicht ist:
   - a) **Benennung der nicht vollständig barrierefreien Inhalte**,
   - b) **Gründe** für die nicht barrierefreie Gestaltung,
   - c) gegebenenfalls **Hinweis auf barrierefreie Alternativen**;
2. eine **unmittelbar zugängliche, barrierefrei gestaltete elektronische Kontaktmöglichkeit**, um Barrieren mitzuteilen und Informationen zur Umsetzung zu erfragen (Feedback-Mechanismus);
3. einen **Hinweis auf das Schlichtungsverfahren nach § 16 BGG**, der die Möglichkeit erläutert **und** zur Schlichtungsstelle verlinkt.

**§ 12b Abs. 4 BGG**: Auf Mitteilungen und Anfragen, die aufgrund der Erklärung übermittelt werden, ist **spätestens innerhalb eines Monats** zu antworten. Die Frist ist zu terminieren und zu dokumentieren.

Die Veröffentlichungsstichtage des § 12b Abs. 3 BGG (23.09.2019, 23.09.2020, 23.06.2021) sind sämtlich verstrichen; ein Fehlen der Erklärung ist heute stets ein Verstoß.

### 5. Überwachung und Berichterstattung ([§ 8](https://www.gesetze-im-internet.de/bitv_2_0/__8.html), [§ 9 BITV 2.0](https://www.gesetze-im-internet.de/bitv_2_0/__9.html))

Die Überwachungsstelle des Bundes prüft Websites und mobile Anwendungen nach dem in § 8 BITV 2.0 vorgesehenen Verfahren im Einklang mit dem Durchführungsbeschluss (EU) 2018/1524; die Ergebnisse fließen in die Berichterstattung an die Kommission nach § 9 BITV 2.0 ein. Für die Praxis folgt daraus: Der Prüfbericht der Überwachungsstelle ist der maßgebliche Befund, an dem sich Nachbesserungspflichten ausrichten.

### 6. Durchsetzung

- **Feedback und Antwort** nach § 12b Abs. 2 Nr. 2, Abs. 4 BGG — Monatsfrist.
- **Schlichtung** nach [§ 16 BGG](https://www.gesetze-im-internet.de/bgg/__16.html) vor der Schlichtungsstelle beim Beauftragten der Bundesregierung für die Belange von Menschen mit Behinderungen; das Verfahren ist außergerichtlich und für die antragstellende Person kostenfrei.
- **Verbandsklage** nach [§ 15 BGG](https://www.gesetze-im-internet.de/bgg/__15.html) durch anerkannte Verbände; sie ist gegenüber der Individualklage subsidiär ausgestaltet und setzt die vorherige Durchführung des Schlichtungsverfahrens voraus `[unverifiziert – prüfen]` hinsichtlich der konkreten Verfahrensvoraussetzungen.
- **Verwaltungsrechtsweg** für Ansprüche gegen die öffentliche Stelle (§ 40 VwGO); bei Beschaffungen zusätzlich der Nachprüfungsantrag nach §§ 155 ff. GWB, wenn die Barrierefreiheit vergaberechtlich verankert war.

Ein **Bußgeldtatbestand** wie § 37 BFSG existiert im BGG **nicht**. Der Druck entsteht über Überwachung, Schlichtung, Verbandsklage und – bei Beschaffungen – über das Vergaberecht.

### 7. Abgrenzung zum BFSG

| | BGG / BITV 2.0 | BFSG / BFSGV |
|---|---|---|
| Adressat | öffentliche Stellen | private Wirtschaftsakteure gegenüber Verbrauchern |
| Umfang | Websites, Apps, Intranet, Verwaltungsabläufe, Programmoberflächen | abschließende Produkt- und Dienstleistungskataloge |
| Besonderheiten | Gebärdensprache und Leichte Sprache (§ 4 BITV 2.0) | CE-Kennzeichnung und Konformitätserklärung für Produkte |
| Erklärung | Erklärung zur Barrierefreiheit § 12b BGG | Informationen nach Anlage 3 Nr. 1 BFSG |
| Sanktion | keine Geldbuße; Schlichtung, Verbandsklage, Überwachung | Geldbuße bis 100.000 EUR, Marktüberwachung |

Ein Unternehmen, das für eine Behörde entwickelt und zugleich Verbrauchern anbietet, unterliegt **beiden** Regimen; die Pflichten sind getrennt zu erfüllen.

## Deterministische Berechnung

Zu rechnen ist vor allem die Monatsfrist des § 12b Abs. 4 BGG. Der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) macht nur die Arithmetik:

```bash
# Antwortfrist § 12b Abs. 4 BGG: 1 Monat ab Eingang der Mitteilung am 03.04.2026
python -m scripts.legal_calc.cli frist --ereignis 03.04.2026 --menge 1 --einheit monate --land BE

# Widerspruchs- bzw. Klagefrist im Verwaltungsrechtsweg
python -m scripts.legal_calc.cli frist --ereignis 03.04.2026 --menge 1 --einheit monate --land BE
```

## Quellen

### Statute

- [§ 12a BGG](https://www.gesetze-im-internet.de/bgg/__12a.html), [§ 12b BGG](https://www.gesetze-im-internet.de/bgg/__12b.html), [§ 15 BGG](https://www.gesetze-im-internet.de/bgg/__15.html), [§ 16 BGG](https://www.gesetze-im-internet.de/bgg/__16.html)
- [BITV 2.0](https://www.gesetze-im-internet.de/bitv_2_0/) – [§ 2](https://www.gesetze-im-internet.de/bitv_2_0/__2.html), [§ 3](https://www.gesetze-im-internet.de/bitv_2_0/__3.html), [§ 4](https://www.gesetze-im-internet.de/bitv_2_0/__4.html), [§ 6](https://www.gesetze-im-internet.de/bitv_2_0/__6.html), [§ 7](https://www.gesetze-im-internet.de/bitv_2_0/__7.html), [§ 8](https://www.gesetze-im-internet.de/bitv_2_0/__8.html), [§ 9](https://www.gesetze-im-internet.de/bitv_2_0/__9.html), [§ 10](https://www.gesetze-im-internet.de/bitv_2_0/__10.html); Anlage 2
- Richtlinie (EU) 2016/2102 (Web-Barrierefreiheits-Richtlinie) — [EUR-Lex](https://eur-lex.europa.eu/eli/dir/2016/2102/oj); Durchführungsbeschluss (EU) 2018/1524
- Landesbehindertengleichstellungsgesetze und Landes-BITV (jeweils konkret zu zitieren) `[unverifiziert – prüfen]`
- [§ 40 VwGO](https://www.gesetze-im-internet.de/vwgo/__40.html); §§ 155 ff. GWB

### Kommentare und Literatur

- Ritgen/Sellmann, BFSG, Kommentar, Einleitung (Abgrenzung BGG/BFSG).
- Welti/Groskreutz, Behindertengleichstellungsrecht, Kommentar zu §§ 12a ff. BGG.
- Überwachungsstelle des Bundes für Barrierefreiheit von Informationstechnik, Prüfverfahren und Berichte.
- Bundesfachstelle für Barrierefreiheit, Leitfäden zur BITV 2.0.

### Rechtsprechung

Zur BITV 2.0 und zu §§ 12a ff. BGG existiert nur vereinzelte verwaltungsgerichtliche Judikatur. Jede Entscheidung ist vor Verwendung in juris oder Beck-Online zu verifizieren `[unverifiziert – prüfen]`. Für die verwaltungsverfahrensrechtliche Flankierung ist auf die allgemeine Rechtsprechung zu §§ 28, 39, 40 VwVfG zurückzugreifen.

## Ausgabeformat

```
BITV-/BGG-PRÜFUNG — <Stelle / Angebot> — <Datum>

I.   Anwendbares Recht
     Träger:                  <Bund / Land <X> / Kommune in <X> / Beliehener>
     Maßgeblich:              [§§ 12a ff. BGG + BITV 2.0 | LBGG <X> + Landes-BITV]
     Ausnahme § 12a Abs. 5:   [einschlägig / nicht einschlägig]

II.  Gestaltungspflicht § 12a BGG
     Website / App:           <Status>
     Intranet:                <Status>
     Verwaltungsabläufe, Vorgangsbearbeitung, Aktenführung: <Status>
     Grafische Programmoberflächen: <Status>
     Beschaffung Abs. 3:      [berücksichtigt / nicht berücksichtigt]
     Unverhältnismäßigkeit Abs. 6: [geltend gemacht — begründet? / nein]

III. Standards
     EN 301 549 / Anlage 2 BITV 2.0: <Befundmatrix je Anforderung>
     § 4 BITV 2.0 Gebärdensprache:   [vorhanden / fehlt]
     § 4 BITV 2.0 Leichte Sprache:   [vorhanden / fehlt]

IV.  Erklärung zur Barrierefreiheit § 12b BGG
     1a) nicht barrierefreie Inhalte benannt:   [ja / nein]
     1b) Gründe angegeben:                      [ja / nein]
     1c) Hinweis auf Alternativen:              [ja / entbehrlich]
     2)  barrierefreier Feedback-Mechanismus:   [ja / nein]
     3)  Hinweis auf Schlichtung § 16 BGG mit Link: [ja / nein]
     Aktualität und Fundort:                    <…>

V.   Eingegangene Mitteilungen
     Eingang <Datum> → Antwortfrist § 12b Abs. 4 BGG endet am <Datum>

VI.  Überwachung und Durchsetzung
     Prüfbericht der Überwachungsstelle:  <Stand>
     Schlichtung § 16 BGG:                <Stand>
     Verbandsklage § 15 BGG:              <Voraussetzungen>
     Verwaltungsrechtsweg:                <…>
     Hinweis: kein Bußgeldtatbestand im BGG

VII. Maßnahmenplan mit Fristen und Verantwortlichkeiten
VIII.Risiko: 🟢 / 🟡 / 🔴 <Begründung>
IX.  Quellenverzeichnis
```

## Risiken / typische Fehler

- **Bundes- und Landesrecht vermengt.** Die BITV 2.0 gilt für öffentliche Stellen des Bundes; für Länder und Kommunen gelten Landesbehindertengleichstellungsgesetz und Landes-BITV, die konkret zu zitieren sind.
- **BFSG-Maßstab auf eine Behörde angewandt.** Adressaten, Anforderungen, Erklärungspflichten und Sanktionen unterscheiden sich vollständig.
- **§ 4 BITV 2.0 übersehen.** Erläuterungen in Deutscher Gebärdensprache und in Leichter Sprache haben kein Gegenstück im BFSG und fehlen deshalb in aus dem Privatsektor übernommenen Konzepten fast immer.
- **Intranet und Fachverfahren ausgeklammert.** § 12a Abs. 1 BGG erfasst ausdrücklich auch Beschäftigtenangebote, Vorgangsbearbeitung, Aktenführung und grafische Programmoberflächen.
- **Erklärung ohne Feedback-Mechanismus oder ohne Schlichtungslink.** Alle drei Bestandteile des § 12b Abs. 2 BGG sind Pflicht.
- **Monatsfrist des § 12b Abs. 4 BGG nicht terminiert.**
- **Unverhältnismäßigkeit nach § 12a Abs. 6 BGG stillschweigend in Anspruch genommen**, statt sie zu begründen und in der Erklärung offenzulegen.
- **Barrierefreiheit erst nach der Vergabe adressiert.** § 12a Abs. 3 BGG verlangt die Berücksichtigung bereits in Ausschreibung und Beschaffung.
- **Bußgeld angedroht.** Das BGG kennt keinen § 37 BFSG entsprechenden Tatbestand.
- **Rechtsprechung erfunden.** Judikatur zu §§ 12a ff. BGG ist spärlich; jede Entscheidung ist zu belegen oder als `[unverifiziert – prüfen]` zu kennzeichnen.
