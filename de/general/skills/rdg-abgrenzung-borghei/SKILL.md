---
name: rdg-abgrenzung-borghei
title: /berufsrecht-anwaltschaft:rdg-abgrenzung
description: 'Abgrenzung erlaubter Rechtsdienstleistungen Nicht-Anwälte nach RDG – Anwaltsmonopol §§ 1, 3 RDG, Nebenleistung § 5 RDG (Schwerpunkt-Test), Inkassodienstleistung § 10 RDG (registrierte Personen), Behörden § 6, Verbraucherzentralen § 8; Folge unerlaubter RDL: § 134 BGB-Nichtigkeit und § 3a UWG-Rechtsbruch. Use when ein Legal-Tech-Startup, eine Inkasso-Plattform oder ein Nicht-Anwalt-Berater die RDG-Grenze prüfen muss, oder ein Anwalt einen Wettbewerber wegen unerlaubter Rechtsdienstleistung abmahnen will.'
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/berufsrecht-anwaltschaft/skills/rdg-abgrenzung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: general
language: de
---

# /berufsrecht-anwaltschaft:rdg-abgrenzung

## Zweck

Der Skill ordnet ein Geschäftsmodell entlang des RDG ein: Liegt überhaupt eine Rechtsdienstleistung iSd § 2 RDG vor? Greift das Anwaltsmonopol (§ 3 RDG), oder rechtfertigt sich die Tätigkeit als Nebenleistung (§ 5 RDG), Inkassodienstleistung (§ 10 RDG) oder durch einen anderen Erlaubnistatbestand? Er erfasst die für Legal-Tech-Plattformen einschlägige BGH-Linie (wenigermiete.de, financialright/lexfox, weitere Inkasso-Erweiterung) und ordnet die zivil-/wettbewerbsrechtlichen Folgen unerlaubter RDL ein.

## Eingaben

- Geschäftsmodell des Anbieters (Anwalt? Inkassodienstleister? Steuerberater? Versicherungsmakler? Verbraucherzentrale? Plattformbetreiber?)
- konkrete Leistung (rechtliche Prüfung, Schreiben an Gegner, Klage-Vorbereitung, Vergleichsverhandlung)
- Vertragsstruktur (Erfolgshonorar? Forderungsabtretung? Treuhandmodell?)
- Zielgruppe (Verbraucher / Gewerbliche)
- ggf. Registrierung im Rechtsdienstleistungsregister § 10 RDG
- Anlass: Gründung / Anpassung Geschäftsmodell / Abmahnung / Klage gegen Anbieter / Verteidigung

## Sub-Agent-Architektur

Researcher liefert RDG-Statute, BGH-Linie zu Inkasso-Reichweite (wenigermiete.de, financialright/lexfox, smartlaw `[unverifiziert]`), BVerfG-Linie (Tarifkollektion, Bestimmtheit), Standardkommentare (Deckenbrock/Henssler, Krenzler) sowie OLG-Rspr. zu § 5 RDG-Nebenleistung. Drafter prüft schrittweise § 2 → § 3 → Erlaubnistatbestände → Folgen unerlaubter RDL. Reviewer kontrolliert den Schwerpunkt-Test bei § 5 RDG, die Registrierung bei § 10 RDG und die parallelen Folgen § 134 BGB und § 3a UWG.

## Ablauf

### 1. Anwendungsbereich — Rechtsdienstleistung iSv § 2 RDG

Eine Rechtsdienstleistung ist nach § 2 Abs. 1 RDG **jede Tätigkeit in konkreten fremden Angelegenheiten, sobald sie eine rechtliche Prüfung des Einzelfalls erfordert**. Drei Tatbestandsmerkmale:

1. **Konkrete Angelegenheit** — kein bloßes Allgemein-Informationsangebot
2. **Fremde Angelegenheit** — nicht Selbstvertretung
3. **Rechtliche Prüfung des Einzelfalls** — Subsumtions- oder Beurteilungsleistung, nicht reine Schema-Anwendung

§ 2 Abs. 2 RDG ergänzt: **Inkassodienstleistung** ist die Einziehung fremder oder zum Zweck der Einziehung abgetretener Forderungen, wenn die Forderungseinziehung als eigenständiges Geschäft betrieben wird.

§ 2 Abs. 3 RDG **Negativabgrenzung** — keine RDL sind u. a. allgemeine Aufklärung, die wissenschaftliche Erörterung, Mediation ohne rechtliche Regelungsvorschläge.

### 2. Erlaubnisvorbehalt § 3 RDG

Außergerichtliche RDL ist nur zulässig, soweit sie durch das RDG oder andere Gesetze erlaubt ist. Anwälte sind durch §§ 1, 3 BRAO umfassend erlaubt (Anwaltsmonopol).

### 3. Erlaubnistatbestände für Nicht-Anwälte

#### a) Nebenleistung § 5 RDG — **Schwerpunkt-Test**

Erlaubt ist die RDL als Nebenleistung zu einer Haupttätigkeit, wenn sie

- zum Berufs- oder Tätigkeitsbild gehört,
- nach Inhalt und Umfang **untergeordnet** ist und
- ohne rechtliche Vorprüfung nicht sachgerecht erbracht werden könnte.

Klassische Beispiele: Steuerberater bei steuerlicher Mandatsführung; Versicherungsmakler bei Schadenregulierung; Architekten bei Bauverträgen. **Schwerpunkt-Test** (h.M.): Macht die rechtliche Beratung den Kern des Auftrags aus oder ist sie tatsächlich nur dienend? Bei Zweifeln → unerlaubte RDL.

#### b) Inkassodienstleistung § 10 RDG

Wer Inkassodienstleistungen (§ 2 Abs. 2 RDG) erbringt, muss sich im **Rechtsdienstleistungsregister** registrieren lassen (§ 10 Abs. 1 Nr. 1 RDG); persönliche und sachliche Eignung sind nachzuweisen.

**BGH-Linie Legal-Tech** (`[unverifiziert – prüfen in juris]`):

- **BGH, Urt. v. 27.11.2019 – VIII ZR 285/18, BGHZ 224, 89 = NJW 2020, 208** ([dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=27.11.2019&Aktenzeichen=VIII%20ZR%20285/18)) (wenigermiete.de / LexFox): Geschäftsmodell der Forderungsabtretung und gerichtsexterner Geltendmachung von Mietsenkungs- bzw. Mietpreisbremse-Ansprüchen ist als Inkassodienstleistung iSv § 10 RDG zulässig — weite Auslegung des Inkasso-Begriffs.
- **BGH, Urt. v. 13.06.2022 – VIa ZR 418/21** u. ä. (financialright / sammelinkasso `[unverifiziert]`): Ausdehnung auch auf gebündelte Schadensersatzforderungen unter engen Voraussetzungen.
- Grenze: vollständige Übernahme einer typisch anwaltlichen Tätigkeit (insb. Klageerhebung im eigenen Namen) bleibt RDG-widrig.

#### c) Weitere Erlaubnistatbestände

- **§ 6 RDG** — Behörden im Rahmen ihrer Aufgaben
- **§ 7 RDG** — Berufsvereinigungen für ihre Mitglieder
- **§ 8 RDG** — Verbraucherzentralen
- **§ 9 RDG** — registrierte Rentenberater, Rechtsdienstleister für ausländisches Recht

### 4. Folgen unerlaubter Rechtsdienstleistung

- **§ 134 BGB-Nichtigkeit** des zugrunde liegenden Vertrags (Mandats- oder Forderungsabtretungsvertrag), wenn das RDG-Verbot Verbotsgesetz iSv § 134 BGB ist. h.M.: ja (Deckenbrock/Henssler, RDG, 5. Aufl. 2023, § 3 Rn. 1 ff. `[unverifiziert]`).
- **§ 3a UWG-Rechtsbruch** — Mitbewerber (Anwälte, registrierte Inkassodienstleister) können Unterlassung und Schadensersatz verlangen.
- **Ordnungswidrigkeit § 20 RDG** — Bußgeld bis 5.000 €.
- **Berufsrechtlich** für Anwälte, die mit unerlaubt agierenden Anbietern kooperieren: Beihilfe-Risiko und Verstoß gegen § 43b BRAO.
- **Strafrechtlich** in extremen Fällen § 263 StGB (Betrug), wenn Kunde über Erlaubtheit getäuscht wird.

### 5. Verfassungsrechtlicher Maßstab

Art. 12 GG schützt die Berufsfreiheit. Das RDG-Verbot wirkt als objektive Berufsausübungsregelung; das BVerfG verlangt eine schutzgutorientierte Auslegung (Rechtssuchenden-Schutz, Funktionsfähigkeit der Rechtspflege). Die Tarifkollektions-Rspr. des BVerfG `[unverifiziert]` hat den Spielraum für Legal-Tech-Modelle insbesondere im Verbraucherinkasso erweitert.

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute

- [§ 1 RDG](https://www.gesetze-im-internet.de/rdg/__1.html) (Anwendungsbereich)
- [§ 2 RDG](https://www.gesetze-im-internet.de/rdg/__2.html) (Begriff der RDL)
- [§ 3 RDG](https://www.gesetze-im-internet.de/rdg/__3.html) (Erlaubnisvorbehalt)
- [§ 5 RDG](https://www.gesetze-im-internet.de/rdg/__5.html) (Nebenleistung)
- [§ 6 RDG](https://www.gesetze-im-internet.de/rdg/__6.html) (Behörden)
- [§ 8 RDG](https://www.gesetze-im-internet.de/rdg/__8.html) (Verbraucherzentralen)
- [§ 10 RDG](https://www.gesetze-im-internet.de/rdg/__10.html) (Inkassodienstleister)
- [§ 20 RDG](https://www.gesetze-im-internet.de/rdg/__20.html) (Ordnungswidrigkeit)
- [§§ 1, 3 BRAO](https://www.gesetze-im-internet.de/brao/__1.html) (Anwaltsmonopol)
- [§ 134 BGB](https://www.gesetze-im-internet.de/bgb/__134.html) (Verstoß gegen gesetzliches Verbot)
- [§ 3a UWG](https://www.gesetze-im-internet.de/uwg_2004/__3a.html) (Rechtsbruchtatbestand)
- [Art. 12 GG](https://www.gesetze-im-internet.de/gg/art_12.html) (Berufsfreiheit)

### Kommentare

- Deckenbrock, in: Deckenbrock/Henssler, RDG, 5. Aufl. 2023, § 2 Rn. 1 ff., § 5 Rn. 1 ff., § 10 Rn. 1 ff.
- Krenzler, RDG, 3. Aufl. 2024, § 2 Rn. 1 ff.
- Henssler, in: Henssler/Prütting, BRAO, 6. Aufl. 2024, § 3 RDG Rn. 1 ff.

### Rechtsprechung (`[unverifiziert – prüfen in juris/Beck-Online]`)

1. BGH, Urt. v. 27.11.2019 – VIII ZR 285/18, NJW 2020, 208 (wenigermiete.de — weite Auslegung Inkassobegriff)
2. BGH, Urt. v. 13.06.2022 – VIa ZR 418/21 (financialright / Sammelinkasso, weitere Klärung Grenze) `[unverifiziert]`
3. BGH, Urt. v. 13.10.2022 – I ZR 35/21 (smartlaw — Rechtsdokumenten-Generator) `[unverifiziert]`
4. BVerfG, Beschl. v. 20.02.2002 – 1 BvR 423/99, BVerfGE 105, 252 (Tarifkollektion) `[unverifiziert]`
5. BGH, Urt. v. 14.01.2016 – I ZR 107/14, GRUR 2016, 820 (Nebenleistung § 5 RDG — Schwerpunkt) `[unverifiziert]`

## Ausgabeformat

```
GUTACHTEN — RDG-Abgrenzung
Anbieter: <…>          Datum: <TT.MM.JJJJ>

I. Sachverhalt
   - Geschäftsmodell, Leistungsbeschreibung
   - Vertragsstruktur, Vergütungsmodell
   - Zielgruppe

II. Frage(n)
III. Kurzantwort
    – Tätigkeit: erlaubt / unerlaubt / grenzwertig
    – Empfehlung: Status / Anpassung / Registrierung

IV. Rechtliche Bewertung
    1. Liegt eine RDL iSv § 2 RDG vor?
       a) Konkrete Angelegenheit
       b) Fremde Angelegenheit
       c) Rechtliche Prüfung im Einzelfall
    2. Erlaubnisvorbehalt § 3 RDG
    3. Erlaubnistatbestände
       a) Anwaltsmonopol §§ 1, 3 BRAO
       b) Nebenleistung § 5 RDG — Schwerpunkt-Test
       c) Inkassodienstleistung § 10 RDG — Registrierung
       d) Sonstige (§§ 6, 7, 8, 9 RDG)
    4. Vergleich mit BGH-Legal-Tech-Linie
       (wenigermiete.de / financialright / smartlaw)
    5. Folgen unerlaubter RDL
       – § 134 BGB-Nichtigkeit
       – § 3a UWG-Rechtsbruch (Unterlassung, Schadensersatz)
       – § 20 RDG-Bußgeld
       – Berufsrechtl. Beihilfe-Risiko kooperierender Anwälte

V. Empfehlung
   – konkrete Handlungsschritte (Modellanpassung, Registrierung,
     anwaltliche Kooperation strukturieren)

VI. Risikoeinstufung
    🟢 / 🟡 / 🔴 mit Begründung

VII. Quellenverzeichnis
```

## Beispiel (Auszug Gutachtenstil)

**Sachverhalt:** Startup S betreibt eine Online-Plattform, die Verbrauchern Fluggastrechte nach VO (EG) 261/2004 durchsetzt: automatisierte Anspruchsprüfung, Forderungsabtretung an S, außergerichtliche Geltendmachung gegenüber Airlines, Klageeinreichung über Partner-Anwälte. Vergütung: 30 % Provision im Erfolgsfall.

**Bewertung:** Die Tätigkeit erfüllt § 2 Abs. 1 RDG (konkrete fremde Angelegenheit, rechtliche Einzelfallprüfung der VO-Voraussetzungen). Es handelt sich der Sache nach um eine **Inkassodienstleistung** iSv § 2 Abs. 2 RDG, weil S die Forderung abtreten lässt und sie im eigenen Namen einzieht. Nach der BGH-Linie wenigermiete.de (BGH, Urt. v. 27.11.2019 – VIII ZR 285/18, NJW 2020, 208 `[unverifiziert]`) ist der Inkasso-Begriff weit zu verstehen; das Modell ist zulässig, **sofern S im Rechtsdienstleistungsregister nach § 10 RDG registriert ist**. Die gerichtliche Geltendmachung muss jedoch über zugelassene Anwälte erfolgen, da S insoweit nicht selbst prozessführungsbefugt ist. Ohne § 10-Registrierung: § 134 BGB-Nichtigkeit der Abtretungsverträge und § 3a UWG-Unterlassungsanspruch durch konkurrierende registrierte Inkassodienstleister oder Anwälte.

**Ergebnis:** 🟡 — Modell zulässig **bei Registrierung**; ohne Registrierung 🔴.

## Risiken / typische Fehler

- **§ 5 RDG-Nebenleistung als Auffangtatbestand** missverstehen — der Schwerpunkt-Test ist eng, h.M. lehnt extensive Auslegung ab.
- **§ 10 RDG-Registrierung als bloßer Formalakt** behandelt — fehlende Registrierung führt zu Nichtigkeit nach § 134 BGB.
- **BGH wenigermiete.de übertragen** auf Modelle, die nicht das Inkasso-Muster (Forderungsabtretung, eigene Einziehung) abbilden — etwa reine Rechtsberatungs- oder Klagevertretungsplattformen.
- **Anwaltskooperation als „Compliance-Pflaster"** — der Anbieter darf gegenüber dem Kunden nicht selbst die rechtliche Beratung erbringen, wenn er nicht Anwalt oder § 10-Inkassodienstleister ist; Beihilfe-Risiko § 3 RDG.
- **§ 3a UWG-Anspruch übersehen** — Wettbewerber haben starke Unterlassungs-/Schadensersatzansprüche, auch ohne Eingreifen der Aufsicht.
- **Datenschutzrechtliche Parallelfragen** (Art. 6 DSGVO, Art. 28 AVV) als RDG-Frage verharmlost — gehören in eigenen Compliance-Strang.
