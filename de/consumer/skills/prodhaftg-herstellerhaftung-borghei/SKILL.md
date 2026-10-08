---
name: prodhaftg-herstellerhaftung-borghei
title: /produktrecht:prodhaftg-herstellerhaftung
description: Parallele Anspruchsprüfung verschuldensunabhängige Herstellerhaftung nach §§ 1, 3 ProdHaftG und Produzentenhaftung § 823 I BGB mit Fehlertypologie (Konstruktion, Fabrikation, Instruktion, Produktbeobachtung) und BGH-Beweislastumkehr „Hühnerpest"; einschließlich Weichenstellung zum neuen Produkthaftungsrecht der RL (EU) 2024/2853 (Stichtag Inverkehrbringen 08.12.2026, Software als Produkt, Wegfall der 85-Mio.-EUR-Höchstgrenze). Use when ein Verbraucher durch ein fehlerhaftes Produkt geschädigt wurde oder ein Hersteller die Haftungsexposition für einen Schadensfall einschätzen muss.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/produktrecht/skills/prodhaftg-herstellerhaftung
license: Apache-2.0
version: 0.1.1
execution_mode: open
jurisdiction: de
practice: consumer
language: de
---

# /produktrecht:prodhaftg-herstellerhaftung

## Zweck

Der Skill prüft Ansprüche aus einem Produktschaden **parallel** auf beiden tragenden Anspruchsgrundlagen: verschuldensunabhängige Gefährdungshaftung des Herstellers nach § 1 ProdHaftG und deliktische Produzentenhaftung nach § 823 I BGB mit der von BGH „Hühnerpest" entwickelten Beweislastumkehr nach Risikosphären. Er ordnet das fehlerhafte Verhalten in die etablierte Fehlertypologie ein und adressiert Haftungsbeschränkungen, Mitverschulden und Verjährung.

> **⚠️ Aktualität (Stand 2026-07): Das ProdHaftG von 1989 wird vollständig aufgehoben und ersetzt.** Grundlage ist die **Richtlinie (EU) 2024/2853** (in Kraft seit **08.12.2024**, Umsetzungsfrist **09.12.2026**). Deutscher Gesetzgebungsstand: RefE **11.09.2025** → RegE Dezember 2025 (**BT-Drs. 21/4297**) → **1. Lesung im Bundestag am 04.03.2026** → derzeit im **Rechtsausschuss**. Das Ablösegesetz soll am Tag der Aufhebung des ProdHaftG 1989 in Kraft treten. **Das Verfahren ist noch nicht abgeschlossen; Inkrafttreten und Endfassung sind plausibel, aber nicht gesichert** `[unverifiziert - prüfen]`.
>
> **Stichtag und Übergangsrecht — zuerst zu klären:** Produkte, die **bis einschließlich 08.12.2026** in Verkehr gebracht oder in Betrieb genommen wurden, bleiben **dem bisherigen Recht** unterworfen. Für sie gilt der gesamte nachstehende Prüfungsaufbau unverändert weiter — und zwar wegen § 13 ProdHaftG (10 Jahre ab Inverkehrbringen) **noch bis in das Jahr 2036**. Beide Regime laufen daher über ein Jahrzehnt parallel; die Weichenstellung ist allein das Inverkehrbringungsdatum.
>
> **Materielle Änderungen des neuen Rechts:**
>
> | Punkt | Bisher (ProdHaftG 1989) | Neu (RL (EU) 2024/2853) |
> |---|---|---|
> | Produktbegriff | bewegliche Sache, Elektrizität | **Software erfasst — auch SaaS, Cloud und KI-Systeme**, unabhängig von der Verkörperung; ferner digitale Bauunterlagen und verbundene Dienste |
> | Haftungshöchstgrenze | 85 Mio. EUR (§ 10) | **abgeschafft** |
> | Ersatzfähiger Schaden | Personen- und privater Sachschaden | zusätzlich **Datenverlust/-korruption** und **medizinisch anerkannte psychische Beeinträchtigung** |
> | Haftungsadressaten | Hersteller, Quasi-Hersteller, Importeur | **erweitert** (u. a. Bevollmächtigte, Fulfilment-Dienstleister, Plattformen, Anbieter wesentlicher Software-Änderungen) |
> | Beweislast | Geschädigter trägt Fehler + Kausalität | **Offenlegungspflicht (Art. 9)** sowie **widerlegliche Vermutungen** zu Fehlerhaftigkeit und Kausalität |
>
> Die Nummerierung der Paragraphen des Ablösegesetzes ist noch nicht endgültig; im Mandat ist auf die Richtlinienartikel abzustellen `[unverifiziert - prüfen]`.

## Eingaben

- Schadensbild (Personenschaden, Sachschaden privat / gewerblich, Vermögensschaden)
- Produkt (Bezeichnung, Charge, **Inverkehrbringdatum — Stichtag 08.12.2026**, Zielnutzer)
- Software-, Cloud- oder KI-Anteil des Produkts; nachträgliche wesentliche Änderungen/Updates
- Hersteller / Importeur / Quasi-Hersteller (§ 4 ProdHaftG)
- mutmaßlicher Fehlertyp (Konstruktion, Fabrikation, Instruktion, Produktbeobachtung)
- Sachverhalt zur Kausalität (Schadenshergang, Beweislage)
- Position des Mandanten: Geschädigte / Hersteller / Versicherer

## Sub-Agent-Architektur

Researcher liefert ProdHaftG-Statute, § 823 BGB, BGH-Leitentscheidungen („Hühnerpest", „Honda", „Pflegebetten") sowie Kommentarstellen (Foerste/Graf von Westphalen, Kullmann, MüKoBGB Wagner). Drafter erstellt parallele Anspruchsprüfung in Gutachtenstil mit Fehlerzuordnung und Schadensbegründung. Reviewer prüft zuerst die **Regime-Weichenstellung nach dem Stichtag 08.12.2026** (Nr. 7), sodann Fristen (§§ 12, 13 ProdHaftG, §§ 195, 199 BGB), Personenschadens-Blocker und Vollständigkeit der Beweislastdiskussion.

## Ablauf

### 1. Anspruch nach § 1 ProdHaftG

Tatbestand:

- **Produkt** iSv § 2 ProdHaftG (jede bewegliche Sache; Strom; nicht: unverarbeitete landwirtschaftliche Erzeugnisse a. F., heute generell erfasst)
- **Fehler** iSv § 3 ProdHaftG: „Sicherheit, die unter Berücksichtigung aller Umstände, insbesondere der Darbietung, des billigerweise zu erwartenden Gebrauchs und des Zeitpunkts des Inverkehrbringens, berechtigterweise erwartet werden kann"
- **Inverkehrbringen** durch Hersteller iSv § 4 ProdHaftG (Endhersteller, Teilhersteller, Quasi-Hersteller durch Markenanbringung, Importeur in den EWR)
- **Personenschaden** oder **privater Sachschaden** (§ 1 I ProdHaftG; gewerbliche Sachschäden ausgeschlossen)
- **Kausalität** Fehler → Schaden
- **Selbstbehalt** § 11: 500 EUR bei Sachschaden
- **Höchstbetrag** § 10: 85 Mio. EUR bei Personenschäden derselben Serie — **nur für Produkte, die bis einschließlich 08.12.2026 in Verkehr gebracht wurden**; für spätere Produkte ist die Höchstgrenze ersatzlos abgeschafft (dazu Nr. 7)

Haftungsausschlüsse § 1 II ProdHaftG: Inverkehrbringen ohne wirtschaftlichen Zweck, Fehler erst nach Inverkehrbringen entstanden, Stand der Wissenschaft und Technik unerkennbar (Entwicklungsrisiko, § 1 II Nr. 5).

### 2. Anspruch nach § 823 I BGB (Produzentenhaftung)

Verletzung der Verkehrssicherungspflichten des Herstellers; Beweislastumkehr nach Risikosphären (BGH, Urt. v. 26.11.1968 – VI ZR 212/66, **BGHZ 51, 91 „Hühnerpest"** `[unverifiziert – prüfen in juris]`): Steht ein Produktfehler im Bereich der vom Hersteller beherrschbaren Risikosphäre fest, muss der Hersteller darlegen und beweisen, dass ihn kein Verschulden trifft.

Verkehrssicherungspflichten:

1. **Konstruktionspflicht** – fehlerfreie Konzeption der Baureihe nach dem maßgeblichen Stand der Wissenschaft und Technik im Inverkehrbringzeitpunkt
2. **Fabrikationspflicht** – Qualitätssicherung; Verantwortlichkeit auch für „Ausreißer"
3. **Instruktionspflicht** – Warn- und Gebrauchshinweise, abgestuft nach Adressatenkreis (Fachverkehr / Verbraucher / besonders schutzbedürftige Gruppen)
4. **Produktbeobachtungspflicht** – nach Inverkehrbringen Beobachtung des Produkts in der Praxis und Reaktion auf später erkannte Risiken (BGH, **„Pflegebetten"** – Urt. v. 16.12.2008 – VI ZR 170/07 `[unverifiziert – prüfen]`)

Vorteil gegenüber ProdHaftG: kein 500-EUR-Selbstbehalt, kein 85-Mio.-Höchstbetrag, Schmerzensgeld § 253 II BGB, Anspruchsverjährung erst 30 Jahre absolut (§ 199 II BGB bei Verletzung Leben/Körper/Gesundheit), Produktbeobachtungsfehler nur hier erfasst.

### 3. Fehlertypologie

| Typ | Anker | Beweisrichtung |
|---|---|---|
| **Konstruktionsfehler** | gesamte Baureihe; Stand W&T im Inverkehrbringzeitpunkt | Beweislastumkehr greift; Entwicklungsrisiko § 1 II Nr. 5 ProdHaftG als Einrede |
| **Fabrikationsfehler** | einzelner „Ausreißer"; Abweichung von Konstruktion | Beweislastumkehr greift; Hersteller haftet trotz organisatorisch optimaler Qualitätssicherung |
| **Instruktionsfehler** | unzureichende Warn-, Gebrauchs- oder Wartungshinweise | objektive Gefahr für den durchschnittlichen Nutzer; nicht: Selbstverständlichkeiten |
| **Produktbeobachtungsfehler** | nachträgliche Reaktionspflicht | nur § 823 BGB, **nicht** ProdHaftG; Reaktionsstufung (Warnung → Empfehlung → Rückruf) |

### 4. Mitverschulden und Schaden

- **Mitverschulden** § 6 ProdHaftG iVm § 254 BGB (Verbrauchserwartung; unsachgemäßer Gebrauch)
- **Schadensumfang**: § 7 ProdHaftG verweist auf §§ 249 ff. BGB; Schmerzensgeld nach § 253 II BGB seit Schuldrechtsmodernisierung 2002 (vorherige „PHG-Lücke" entfallen, § 8 ProdHaftG a. F.)
- **Gesamtschuld** § 5 ProdHaftG / § 840 BGB bei mehreren Herstellern

### 5. Fristen

- **§ 12 ProdHaftG**: Verjährung **3 Jahre** ab Kenntnis von Schaden, Fehler und Person des Ersatzpflichtigen
- **§ 13 ProdHaftG**: **Erlöschen** der Ansprüche **10 Jahre** ab Inverkehrbringen des konkreten Produkts (absolute Grenze)
- **§§ 195, 199 BGB** für Deliktsansprüche: 3 Jahre ab Jahresende der Kenntnis; Höchstfristen § 199 II BGB (30 Jahre bei Personenschaden), § 199 III BGB (10 Jahre ab Anspruchsentstehung bzw. 30 Jahre ab schädigender Handlung)

### 6. Versicherungsbezug

Bei Personenschaden: **Information des Produkthaftpflichtversicherers** prüfen (Obliegenheit aus dem Versicherungsvertrag; verspätete Anzeige kann Deckung gefährden).

### 7. Übergangsrecht — Weichenstellung nach Inverkehrbringungsdatum

Dieser Schritt ist in jedem Mandat **vor** der Prüfung nach Nr. 1 vorzunehmen; er bestimmt das anwendbare Regime.

**a) Stichtagsprüfung.** Maßgeblich ist allein, wann das **konkrete** Produkt in Verkehr gebracht oder in Betrieb genommen wurde:

| Inverkehrbringen | Regime |
|---|---|
| **bis einschließlich 08.12.2026** | **ProdHaftG 1989** — Prüfung nach Nr. 1–6 unverändert; wegen § 13 ProdHaftG relevant bis ca. 2036 |
| **ab 09.12.2026** | **neues Produkthaftungsrecht** nach RL (EU) 2024/2853 / Ablösegesetz `[unverifiziert - prüfen]` |

Bei **Serien** ist chargen- bzw. stückbezogen zu differenzieren; ein Serienprodukt kann beiderseits des Stichtags liegen. Bei **Software** ist zusätzlich zu prüfen, ob eine **wesentliche Änderung** (Update, Modellwechsel) nach dem Stichtag ein neues Inverkehrbringen darstellt — dann greift das neue Recht auch für ursprünglich älteren Code.

**b) Prüfpunkte für das neue Regime.** Fällt das Produkt darunter, sind gegenüber Nr. 1 zu ändern: Produktbegriff (Software/SaaS/KI erfasst), keine Haftungshöchstgrenze, erweiterter Schadensbegriff (Datenverlust, medizinisch anerkannte psychische Beeinträchtigung), erweiterter Adressatenkreis, Offenlegungspflicht (Art. 9) und Beweiserleichterungen zugunsten der Geschädigten.

**c) Beratungsaufträge auf Herstellerseite** — unabhängig vom konkreten Schadensfall zu adressieren:

1. **Software- und KI-Portfolio neu bewerten.** Jedes Produkt mit Software-, SaaS-, Cloud- oder KI-Anteil ist darauf zu prüfen, ob es ab dem Stichtag der **verschuldensunabhängigen** Haftung unterfällt — auch reine Softwareprodukte ohne körperlichen Träger.
2. **Versicherungsdeckung gegen den Wegfall der Höchstgrenze prüfen.** Produkthaftpflicht- und D&O-Policen sind häufig auf die 85-Mio.-EUR-Logik kalibriert; Deckungssummen, Serienschadenklauseln und Software-Ausschlüsse sind neu zu verhandeln.
3. **Prozess für Offenlegungsanordnungen (Art. 9) aufsetzen.** Beweismittelsicherung, Zuständigkeiten, Fristen sowie der Schutz von Geschäftsgeheimnissen sind vorab zu regeln — die Anordnung trifft das Unternehmen sonst unvorbereitet.
4. **Lieferanten- und Rückgriffsklauseln aktualisieren.** Freistellungs-, Haftungs- und Versicherungsklauseln in Zuliefer- und Softwareverträgen sind an den erweiterten Adressatenkreis und den Wegfall der Höchstgrenze anzupassen; Altverträge laufen sonst gegen eine unbegrenzte Innenhaftung.

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute

- [§ 1 ProdHaftG](https://www.gesetze-im-internet.de/prodhaftg/__1.html) (Haftung)
- [§ 2 ProdHaftG](https://www.gesetze-im-internet.de/prodhaftg/__2.html) (Produkt)
- [§ 3 ProdHaftG](https://www.gesetze-im-internet.de/prodhaftg/__3.html) (Fehler)
- [§ 4 ProdHaftG](https://www.gesetze-im-internet.de/prodhaftg/__4.html) (Hersteller)
- [§ 6 ProdHaftG](https://www.gesetze-im-internet.de/prodhaftg/__6.html) (Mitverschulden)
- [§ 10 ProdHaftG](https://www.gesetze-im-internet.de/prodhaftg/__10.html) (Höchstbetrag)
- [§ 11 ProdHaftG](https://www.gesetze-im-internet.de/prodhaftg/__11.html) (Selbstbeteiligung)
- [§ 12 ProdHaftG](https://www.gesetze-im-internet.de/prodhaftg/__12.html) (Verjährung)
- [§ 13 ProdHaftG](https://www.gesetze-im-internet.de/prodhaftg/__13.html) (Erlöschen)
- [§ 15 ProdHaftG](https://www.gesetze-im-internet.de/prodhaftg/__15.html) (andere Haftung; Anspruchskonkurrenz)
- [§ 823 BGB](https://www.gesetze-im-internet.de/bgb/__823.html) (Schadensersatzpflicht)
- [§ 253 BGB](https://www.gesetze-im-internet.de/bgb/__253.html) (Schmerzensgeld)
- [§ 254 BGB](https://www.gesetze-im-internet.de/bgb/__254.html) (Mitverschulden)
- [§§ 195, 199 BGB](https://www.gesetze-im-internet.de/bgb/__199.html) (Verjährung)
- [RL 85/374/EWG](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:31985L0374) (Produkthaftungs-RL 1985, Grundlage des ProdHaftG 1989 — **aufgehoben mit Wirkung zum 09.12.2026**)
- [RL (EU) 2024/2853](https://eur-lex.europa.eu/eli/dir/2024/2853/oj) (neue Produkthaftungsrichtlinie; in Kraft 08.12.2024, Umsetzungsfrist 09.12.2026) — insbes. Produktbegriff, Wegfall der Höchstgrenze, Art. 9 (Offenlegung), Beweisvermutungen
- **BT-Drs. 21/4297** — Regierungsentwurf eines Gesetzes zur Umsetzung der RL (EU) 2024/2853 (1. Lesung 04.03.2026, Rechtsausschuss). Endfassung und Paragraphennummerierung offen `[unverifiziert - prüfen]`

### Kommentare

- Foerste, in: Foerste/Graf von Westphalen, Produkthaftungshandbuch, 4. Aufl. 2024, § 24 Rn. 1 ff. (Fehlerbegriff) `[unverifiziert – Aufl./Jahr prüfen]`
- Kullmann, ProdHaftG, 7. Aufl. 2018, § 3 Rn. 1 ff. `[unverifiziert – Aufl. prüfen]`
- Wagner, in: MüKoBGB, 9. Aufl. 2024, § 823 Rn. 800 ff. (Produzentenhaftung)
- Spindler, in: BeckOK BGB, Stand 2024, § 823 Rn. 500 ff. (Produktrisiken)
- Grüneberg/Sprau, in: Palandt/Grüneberg, BGB, 83. Aufl. 2024, § 823 Rn. 167 ff. `[unverifiziert – Aufl. prüfen]`

### Rechtsprechung (`[unverifiziert – prüfen in juris/Beck-Online]`)

1. BGH, Urt. v. 26.11.1968 – VI ZR 212/66, BGHZ 51, 91 („Hühnerpest", Beweislastumkehr nach Risikosphären)
2. BGH, Urt. v. 17.03.1981 – VI ZR 191/79, BGHZ 80, 186 („Honda", Konstruktionsfehler)
3. BGH, Urt. v. 16.12.2008 – VI ZR 170/07, NJW 2009, 1080 („Pflegebetten", Produktbeobachtung und Reaktionsstufung)
4. BGH, Urt. v. 09.05.1995 – VI ZR 158/94, BGHZ 129, 353 (Instruktionspflicht bei Verbraucherprodukten)
5. EuGH, Urt. v. 05.03.2015 – C-503/13, C-504/13, ECLI:EU:C:2015:148 (Boston Scientific, Fehlerbegriff bei Medizinprodukten potenziellen Defekts)

## Ausgabeformat

```
GUTACHTEN — Herstellerhaftung Produktschaden
Mandat: <Geschädigte / Hersteller / Versicherer>
Produkt: <Bezeichnung, Charge, Inverkehrbringdatum>

0. Regime-Weichenstellung (Stichtag 08.12.2026)
   – Inverkehrbringen: <Datum>
   – Anwendbares Recht: [ProdHaftG 1989 / neues Recht RL (EU) 2024/2853]
   – Software-/KI-Anteil, wesentliche Änderung nach Stichtag: <…>

I. Sachverhalt (knapp)
II. Frage(n)
III. Kurzantwort
     – ProdHaftG: [Anspruch (+/-) / Höhe]
     – § 823 BGB: [Anspruch (+/-) / Höhe + Schmerzensgeld]

IV. Rechtliche Bewertung
    1. Anspruch aus § 1 ProdHaftG
       a) Produkt (§ 2)
       b) Fehler (§ 3) — Fehlertyp:
          ☐ Konstruktion ☐ Fabrikation ☐ Instruktion
       c) Inverkehrbringen durch Hersteller (§ 4)
       d) Schaden und Kausalität
       e) Haftungsbeschränkungen
          – Selbstbehalt § 11 (500 EUR Sachschaden)
          – Höchstbetrag § 10 (85 Mio. EUR Serie)
       f) Mitverschulden § 6 iVm § 254 BGB
    2. Anspruch aus § 823 I BGB (Produzentenhaftung)
       a) Verkehrssicherungspflichten und Pflichtverletzung
          ☐ Konstruktion ☐ Fabrikation ☐ Instruktion ☐ Produktbeobachtung
       b) Beweislastumkehr nach BGH „Hühnerpest"
       c) Schaden inkl. Schmerzensgeld § 253 II BGB
    3. Anspruchskonkurrenz § 15 II ProdHaftG
    4. Fristen
       – § 12 ProdHaftG (3 J ab Kenntnis)
       – § 13 ProdHaftG (10 J Erlöschen ab Inverkehrbringen)
       – §§ 195, 199 BGB (Delikt)

V. Risiken / offene Punkte
    🟢 / 🟡 / 🔴 <Einstufung mit Begründung>
    – Tatsachen offen: <…>
    – Versicherer-Information: <…>

VI. Quellenverzeichnis
```

## Risiken / typische Fehler

- **Anspruchsgrundlagen nur alternativ geprüft.** ProdHaftG und § 823 BGB stehen nebeneinander (§ 15 II ProdHaftG); Verzicht auf § 823 BGB nimmt der Geschädigten Schmerzensgeld und unbegrenzte Haftungssumme.
- **Fehlertyp nicht benannt.** Die Beweisrichtung und der Entwicklungsrisiko-Einwand § 1 II Nr. 5 ProdHaftG hängen vom Fehlertyp ab.
- **Produktbeobachtungspflicht in ProdHaftG verortet.** Sie ist nur § 823 BGB.
- **§ 12 / § 13 ProdHaftG verwechselt.** § 12 ist Verjährung (3 J ab Kenntnis); § 13 ist absolute Erlöschens-Frist (10 J ab Inverkehrbringen) — unabhängig von Kenntnis.
- **Quasi-Hersteller** (§ 4 I 2 ProdHaftG, Markenanbringung) und **Importeur** (§ 4 II ProdHaftG, Einfuhr in den EWR) übersehen — relevant, wenn der Endhersteller außerhalb des EWR sitzt.
- **Schmerzensgeld nur über § 8 ProdHaftG a. F. argumentiert.** Seit 2002 läuft Schmerzensgeld primär über § 253 II BGB.
- **Versicherer-Information vergessen** — Deckungsrisiko aus Produkthaftpflichtversicherung.
- **Stichtag 08.12.2026 nicht geprüft** — BLOCKER. Ohne die Weichenstellung nach dem Inverkehrbringungsdatum (Nr. 7) wird das falsche Haftungsregime geprüft. Beide Regime laufen wegen § 13 ProdHaftG **über ein Jahrzehnt parallel**; „das ProdHaftG gilt" ist ab 09.12.2026 nur noch für Altprodukte richtig.
- **85-Mio.-EUR-Höchstgrenze auf Neuprodukte angewandt** — die Grenze des § 10 ProdHaftG ist im neuen Recht **ersatzlos abgeschafft**. Haftungsprognosen, Rückstellungen und Deckungssummen, die auf ihr aufbauen, sind für Produkte ab dem Stichtag wertlos.
- **Software als „kein Produkt" abgetan** — nach RL (EU) 2024/2853 ist Software **unabhängig von der Verkörperung** Produkt, einschließlich SaaS, Cloud-Diensten und KI-Systemen. Die verbreitete Auskunft, reine Software unterfalle nicht der verschuldensunabhängigen Haftung, ist ab dem Stichtag falsch.
- **Erweiterten Schadensbegriff übersehen** — Datenverlust und medizinisch anerkannte psychische Beeinträchtigung sind im neuen Recht ersatzfähig; nach ProdHaftG 1989 waren sie es nicht.
- **Offenlegungspflicht (Art. 9) und Beweisvermutungen nicht eingeplant** — die Beweislastarchitektur verschiebt sich zugunsten der Geschädigten. Auf Herstellerseite fehlt regelmäßig ein Prozess für die Reaktion auf eine gerichtliche Offenlegungsanordnung samt Schutz von Geschäftsgeheimnissen.
- **Endfassung als gesichert behandelt** — das Umsetzungsgesetz (BT-Drs. 21/4297) ist noch im Rechtsausschuss. Paragraphennummern des künftigen Gesetzes dürfen **nicht** in mandantengerichtete Ausgaben übernommen werden; zu zitieren sind die Richtlinienartikel. `[unverifiziert - prüfen]`
