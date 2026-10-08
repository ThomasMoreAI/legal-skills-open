---
name: vorvertragliche-phase-borghei
title: /vertragsrecht:vorvertragliche-phase
description: Gestaltung und Haftungsprüfung der vorvertraglichen Phase – vorvertragliches Schuldverhältnis § 311 Abs. 2 BGB, Rücksichtnahme- und Aufklärungspflichten § 241 Abs. 2 BGB, culpa in contrahendo (c.i.c.) nach § 280 Abs. 1 BGB mit Vertragsaufhebung als Schadensersatz, Geheimhaltungsvereinbarung (NDA) mit GeschGehG-Bezug, Letter of Intent und Term Sheet sowie Exklusivitätsvereinbarung und Break-up Fee. Use when Verhandlungen aufgenommen, abgebrochen oder eine Vorfeldvereinbarung entworfen oder auf Bindungswirkung geprüft werden soll.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/vertragsrecht/skills/vorvertragliche-phase
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: contracts
language: de
---

# /vertragsrecht:vorvertragliche-phase

## Zweck

Vor dem Vertrag entsteht bereits ein **Schuldverhältnis mit Pflichten** ([§ 311 Abs. 2 BGB](https://www.gesetze-im-internet.de/bgb/__311.html)) — und mit ihm Haftung für Aufklärungsfehler und Verhandlungsabbruch. Zugleich werden hier die Instrumente gesetzt, die den späteren Deal steuern: NDA, Letter of Intent, Term Sheet, Exklusivität, Break-up Fee. Dieser Skill klärt, **welche dieser Dokumente binden**, und prüft die Haftung aus **culpa in contrahendo (c.i.c. — Verschulden bei Vertragsanbahnung)**.

## Eingaben

- Verhandlungsstand: erste Kontaktaufnahme, Due Diligence, ausverhandelte Eckpunkte, Signing bevorstehend
- Vorhandene Vorfelddokumente: NDA, LOI, Term Sheet, Exklusivitätsvereinbarung, Prozessbrief — jeweils Wortlaut und Datum
- Getätigte Aufwendungen: Berater-, Gutachter-, Finanzierungskosten; abgelehnte Alternativangebote
- Bei Abbruch: wer hat abgebrochen, wann, mit welcher Begründung, welcher Vertrauenstatbestand wurde zuvor gesetzt
- Bei Aufklärungsvorwurf: welche Information, wem bekannt, Erkennbarkeit der Bedeutung für die Gegenseite
- Formbedürftigkeit des Zielvertrags (§ 311b BGB Grundstück, § 15 GmbHG Geschäftsanteile)

## Sub-Agent-Architektur

1. **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) liefert §§ 241, 280, 311 BGB, das GeschGehG und Kommentarstellen zu Aufklärungspflichten und Abbruchhaftung.
2. **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) prüft Schuldverhältnis → Pflichtverletzung → Vertretenmüssen → Schaden → Kausalität und entwirft NDA, LOI oder Exklusivitätsklausel.
3. **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft insbesondere, ob ein LOI ungewollt Bindungswirkung entfaltet, ob die Formfrage beachtet wurde und ob die Break-up Fee der AGB-Kontrolle standhält.

## Ablauf

### 1. Vorvertragliches Schuldverhältnis ([§ 311 Abs. 2 BGB](https://www.gesetze-im-internet.de/bgb/__311.html))

Ein Schuldverhältnis mit Pflichten nach § 241 Abs. 2 BGB entsteht bereits durch

1. die **Aufnahme von Vertragsverhandlungen**,
2. die **Anbahnung eines Vertrags**, bei welcher der eine Teil im Hinblick auf eine etwaige rechtsgeschäftliche Beziehung dem anderen die Möglichkeit zur Einwirkung auf seine Rechte, Rechtsgüter und Interessen gewährt oder ihm diese anvertraut, oder
3. **ähnliche geschäftliche Kontakte**.

**Dritthaftung (§ 311 Abs. 3 BGB):** Ein solches Schuldverhältnis kann auch zu Personen entstehen, die nicht selbst Vertragspartei werden sollen — insbesondere wenn der Dritte in **besonderem Maße Vertrauen** für sich in Anspruch nimmt und dadurch die Vertragsverhandlungen erheblich beeinflusst (Sachwalter- und Prospekthaftung, Beratung durch Wirtschaftsprüfer oder Geschäftsführer in eigener Sache).

### 2. Pflichteninhalt ([§ 241 Abs. 2 BGB](https://www.gesetze-im-internet.de/bgb/__241.html))

Das Schuldverhältnis kann nach seinem Inhalt jeden Teil zur **Rücksicht auf die Rechte, Rechtsgüter und Interessen des anderen Teils** verpflichten. Daraus folgen in der Anbahnungsphase:

- **Aufklärungspflichten** über Umstände, die für den Vertragsentschluss der anderen Seite erkennbar von wesentlicher Bedeutung sind und über die nach Treu und Glauben Aufklärung erwartet werden darf. Es gibt **keine allgemeine Aufklärungspflicht** — jede Partei hat sich grundsätzlich selbst zu informieren. Die Pflicht verdichtet sich bei Wissensvorsprung, erkennbarer Fehlvorstellung der Gegenseite und existenzieller Bedeutung des Umstands.
- **Wahrheitspflicht** bei erteilten Auskünften: Wer Angaben macht, muss sie richtig und vollständig machen, auch wenn er nicht zur Auskunft verpflichtet war.
- **Schutzpflichten** hinsichtlich Rechtsgütern (klassisch: Verkehrssicherung im Ladenlokal).
- **Verschwiegenheit** über offenbarte Interna, auch ohne NDA.
- **Loyalitätspflicht**: keine Verhandlung mit dem alleinigen Zweck, Informationen abzuschöpfen.

### 3. c.i.c. — Haftung dem Grunde nach ([§ 280 Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__280.html))

Anspruchsgrundlage ist **§ 280 Abs. 1 iVm §§ 311 Abs. 2, 241 Abs. 2 BGB**. Prüfungsschema:

1. **Vorvertragliches Schuldverhältnis** (§ 311 Abs. 2 BGB)
2. **Pflichtverletzung** (§ 241 Abs. 2 BGB)
3. **Vertretenmüssen** — **vermutet** (§ 280 Abs. 1 S. 2 BGB); Zurechnung des Verhandlungsgehilfen nach § 278 BGB
4. **Schaden** und **Kausalität**

**Rechtsfolge — Vertrauensschaden (negatives Interesse):** Der Geschädigte ist so zu stellen, wie er ohne die Pflichtverletzung stünde. Ersatzfähig sind vergebliche Aufwendungen, entgangene Vorteile aus einem abgelehnten Alternativgeschäft und Mehrkosten eines Deckungsgeschäfts.

**🔴 Vertragsaufhebung als Schadensersatz:** Wurde ein Vertrag aufgrund der Pflichtverletzung geschlossen, kann der Geschädigte im Wege der **Naturalrestitution** (§ 249 Abs. 1 BGB) die **Aufhebung des Vertrags** verlangen — auch dann, wenn der Schaden nicht in Geld messbar ist, sondern in der Bindung an einen ungewollten Vertrag besteht. Praktisch bedeutsam, weil die c.i.c. **nicht an die Jahresfrist des § 124 BGB** gebunden ist: Sie verjährt nach §§ 195, 199 BGB in drei Jahren ab Schluss des Kenntnisjahres. Die c.i.c. steht **neben** der Anfechtung wegen arglistiger Täuschung (`/vertragsrecht:anfechtung-willenserklaerung`). Für **fahrlässige** Fehlinformationen über die Sachbeschaffenheit wird sie hingegen nach Gefahrübergang durch das Mängelrecht der §§ 434 ff., 633 ff. BGB verdrängt `[unverifiziert – prüfen]`.

### 4. Haftung für Verhandlungsabbruch

**Grundsatz: Abschlussfreiheit.** Bis zum Vertragsschluss darf jede Partei die Verhandlungen abbrechen — auch ohne Grund und auch kurz vor der Unterschrift. Haftung entsteht nur ausnahmsweise, wenn

1. eine Partei beim anderen Teil das **berechtigte Vertrauen** erweckt hat, der Vertrag werde mit Sicherheit zustande kommen, **und**
2. sie die Verhandlungen anschließend **ohne triftigen Grund** abbricht.

Der Ersatz umfasst den **Vertrauensschaden**, nicht das Erfüllungsinteresse — der Abbrechende wird nicht zum Vertragsschluss gezwungen.

**Sonderfall Formbedürftigkeit:** Bei formbedürftigen Verträgen (§ 311b Abs. 1 BGB Grundstück, § 15 Abs. 3, 4 GmbHG Geschäftsanteile) ist eine Abbruchhaftung nur bei **Vorsatz oder besonders schwerwiegender Treuepflichtverletzung** anzuerkennen — andernfalls würde der Formzwang mittelbar ausgehebelt `[unverifiziert – prüfen]`.

### 5. Geheimhaltungsvereinbarung (NDA)

Die Verschwiegenheitspflicht folgt bereits aus § 241 Abs. 2 BGB, ist aber in Umfang und Beweisbarkeit unsicher. Ein NDA regelt:

1. **Definition der vertraulichen Information** — besser negativ abgegrenzt (Ausnahmen: bereits bekannt, öffentlich zugänglich, unabhängig entwickelt, rechtmäßig von Dritten erhalten) als durch Positivkatalog; **Kennzeichnungspflicht** nur vereinbaren, wenn sie praktisch einhaltbar ist.
2. **Zweckbindung** — Nutzung ausschließlich zur Evaluierung der Transaktion.
3. **Zulässiger Empfängerkreis** (need-to-know), Weitergabe an Berater mit Weitergabe der Pflichten.
4. **Gesetzliche Offenlegungspflichten** ausnehmen (Behörden, Gerichte) mit vorheriger Unterrichtungspflicht.
5. **Laufzeit** der Vereinbarung und **Nachwirkungsdauer** der Pflichten (üblich: 2–5 Jahre nach Ende der Verhandlungen) — getrennt regeln.
6. **Rückgabe und Löschung** einschließlich Backup-Ausnahme.
7. **Vertragsstrafe** — ohne sie ist der Verstoß praktisch nicht sanktionierbar, weil der Schaden kaum bezifferbar ist. Ausgestaltung nach `/vertragsrecht:vertragsstrafe`, im Zweifel nach Hamburger Brauch.
8. **Bezug zum GeschGehG:** Der Schutz als Geschäftsgeheimnis nach § 2 Nr. 1 GeschGehG setzt **angemessene Geheimhaltungsmaßnahmen** voraus. Ein abgeschlossenes NDA ist genau eine solche Maßnahme — es sichert damit zugleich die gesetzlichen Ansprüche aus §§ 6 ff. GeschGehG. **Ohne NDA droht der Verlust des gesetzlichen Geheimnisschutzes.**

### 6. Letter of Intent und Term Sheet — Bindungswirkung

Ein LOI oder Term Sheet ist **kein einheitlicher Rechtstyp**. Die Bindungswirkung bestimmt sich allein nach dem Inhalt und wird nach §§ 133, 157 BGB ausgelegt — die Überschrift „unverbindlich" schützt nicht, wenn der Text Leistungspflichten begründet. Drei Bausteine sind zu trennen:

| Baustein | Bindung | Beispiel |
|---|---|---|
| **Absichtserklärung** | keine Bindung, aber verstärktes Vertrauen — erhöht das c.i.c.-Risiko beim Abbruch | „Die Parteien beabsichtigen, bis zum [Datum] einen Kaufvertrag zu schließen." |
| **Eckpunkte (Term Sheet)** | grundsätzlich keine Bindung, **aber Vorvertragsgefahr**, wenn alle essentialia negotii geregelt sind und Bindungswille erkennbar ist | Kaufpreis, Kaufgegenstand, Closing-Bedingungen |
| **Verbindliche Nebenabreden** | **volle Bindung** — hier liegt der ernst gemeinte Regelungsgehalt | Vertraulichkeit, Exklusivität, Kostentragung, Rechtswahl, Gerichtsstand, Break-up Fee |

**Klauselbaustein Bindungsvorbehalt:**

> „Dieses Term Sheet begründet **keine Verpflichtung zum Abschluss** des darin beschriebenen Vertrags. Eine rechtsgeschäftliche Bindung tritt ausschließlich durch den Abschluss eines gesonderten, [notariell beurkundeten] Vertrags ein. **Rechtsverbindlich sind allein die Ziffern [N] (Vertraulichkeit), [N] (Exklusivität), [N] (Kostentragung), [N] (Rechtswahl) und [N] (Gerichtsstand).** Ein Anspruch auf Ersatz von Aufwendungen wegen des Abbruchs der Verhandlungen besteht vorbehaltlich vorsätzlichen Verhaltens nicht."

**Formfalle:** Wird im LOI eine bereits bindende Verpflichtung zur Übertragung eines Grundstücks oder eines GmbH-Geschäftsanteils begründet, ist der LOI **insgesamt formbedürftig** und ohne Beurkundung nichtig (§ 125 BGB).

### 7. Exklusivität und Break-up Fee

**Exklusivitätsvereinbarung** (No-Shop): Der Verkäufer verpflichtet sich, für einen befristeten Zeitraum nicht mit Dritten zu verhandeln. Erforderlich sind **klare Befristung**, Definition der untersagten Handlungen (auch: Entgegennahme unaufgeforderter Angebote — No-Talk), Ausnahme für gesetzliche und organschaftliche Pflichten und eine **Sanktion**, üblicherweise eine Vertragsstrafe. Ohne Sanktion ist die Klausel praktisch wirkungslos, da der Schaden nicht bezifferbar ist.

**Break-up Fee:** Pauschaler Aufwendungsersatz für den Fall, dass die Transaktion aus definierten Gründen scheitert.

- **Rechtsnatur klarstellen:** pauschalierter Aufwendungsersatz (dann Nachweis eines geringeren Schadens gestatten) oder Vertragsstrafe (dann §§ 339 ff. BGB, § 343 BGB, § 348 HGB).
- **Auslösetatbestände abschließend** definieren — typisch: Abbruch durch den Verkäufer, Verkauf an einen Dritten, Nichtvorlage vereinbarter Unterlagen. **Nicht** auslösen sollte das Scheitern aus Gründen, die keine Partei zu vertreten hat.
- **Höhe:** an den tatsächlich zu erwartenden Transaktionskosten orientieren. Eine Break-up Fee, die den Verkäufer faktisch zum Abschluss zwingt, ist als mittelbarer Abschlusszwang bei formbedürftigen Verträgen bedenklich und kann nach § 138 BGB oder — in AGB — nach § 307 BGB unwirksam sein `[unverifiziert – prüfen]`.
- **AGB-Kontrolle** beachten, wenn die Klausel vorformuliert gestellt wird (`/vertragsrecht:agb-kontrolle`).

## Quellen

### Statute

- [§ 311 BGB](https://www.gesetze-im-internet.de/bgb/__311.html) (Abs. 2 c.i.c., Abs. 3 Dritthaftung), [§ 241 BGB](https://www.gesetze-im-internet.de/bgb/__241.html), [§ 280 BGB](https://www.gesetze-im-internet.de/bgb/__280.html), [§ 278 BGB](https://www.gesetze-im-internet.de/bgb/__278.html)
- [§ 249 BGB](https://www.gesetze-im-internet.de/bgb/__249.html) (Naturalrestitution, Vertragsaufhebung), [§ 242 BGB](https://www.gesetze-im-internet.de/bgb/__242.html)
- [§ 311b BGB](https://www.gesetze-im-internet.de/bgb/__311b.html) (Form bei Grundstücksverträgen), [§ 125 BGB](https://www.gesetze-im-internet.de/bgb/__125.html)
- [§ 195 BGB](https://www.gesetze-im-internet.de/bgb/__195.html), [§ 199 BGB](https://www.gesetze-im-internet.de/bgb/__199.html) (Verjährung der c.i.c.-Ansprüche)
- [§ 2 GeschGehG](https://www.gesetze-im-internet.de/geschgehg/__2.html) (Begriff des Geschäftsgeheimnisses, angemessene Geheimhaltungsmaßnahmen)

### Kommentare

- Grüneberg, BGB, 83. Aufl. 2024, § 311 Rn. 11 ff. (c.i.c.), § 241 Rn. 6 ff. `[unverifiziert – Auflagenstand prüfen]`
- Emmerich, in: MüKoBGB, 9. Aufl. 2022, § 311 Rn. 38 ff. (Verhandlungsabbruch, Aufklärungspflichten)
- Bachmann, in: MüKoBGB, 9. Aufl. 2022, § 241 Rn. 1 ff.

### Rechtsprechung

- BGH, Urt. v. 26.09.1997 – V ZR 29/96 (Abbruchhaftung bei formbedürftigen Verträgen) `[unverifiziert – prüfen]`
- BGH, Urt. v. 06.04.2001 – V ZR 394/99 (Vertragsaufhebung als Schadensersatz aus c.i.c.) `[unverifiziert – prüfen]`

> Beide Aktenzeichen vor Verwendung in juris / Beck-Online prüfen. Die tragenden Aussagen dieses Skills folgen aus dem Gesetzeswortlaut und der Kommentarliteratur.

## Ausgabeformat

```
VORVERTRAGLICHE PHASE — <Transaktion / Mandat> — <Datum>

I.    Verhandlungsstand               <Phase, Beteiligte, Zeitachse>
II.   Vorvertragliches Schuldverhältnis (§ 311 II) [✅ ab <Datum> / Dritthaftung § 311 III]
III.  Pflichtverletzung (§ 241 II)    [Aufklärung / Wahrheit / Vertraulichkeit / Loyalität — <…>]
IV.   Vertretenmüssen                 [vermutet § 280 I 2 / § 278 Zurechnung]
V.    Schaden                         [Vertrauensschaden: <Betrag> / Vertragsaufhebung § 249]
VI.   Verhandlungsabbruch             [zulässig / haftungsbegründend — Vertrauenstatbestand: <…>]
        Formbedürftiger Zielvertrag:  [ja — nur bei Vorsatz / nein]
VII.  NDA                             [vorhanden / Entwurf — Nachwirkung <…> Jahre, Vertragsstrafe ✅/❌]
        GeschGehG-Bezug:              [angemessene Geheimhaltungsmaßnahme ✅/❌]
VIII. LOI / Term Sheet                [Bindungswirkung: keine / teilweise — verbindliche Ziffern: <…>]
        Formfalle § 311b:             [geprüft ✅ / 🔴 Risiko]
IX.   Exklusivität                    [Laufzeit bis <Datum>, Sanktion: <…>]
X.    Break-up Fee                    [<Betrag> — Rechtsnatur: Aufwendungsersatz / Vertragsstrafe]
XI.   Verjährung                      [§§ 195, 199 — Ende <TT.MM.JJJJ>]

Gesamtbefund: [🟢 / 🟡 / 🔴]
Offene Tatsachen: <Liste>
```

## Risiken / typische Fehler

- **LOI mit ungewollter Bindungswirkung** — die Überschrift „unverbindlich" trägt nicht, wenn der Text Leistungspflichten begründet; verbindliche und unverbindliche Teile sind ausdrücklich zu trennen.
- **Formbedürftigkeit im Vorfeld übersehen** — enthält ein LOI eine bindende Verpflichtung zur Übertragung eines Grundstücks oder GmbH-Anteils, ist er ohne notarielle Beurkundung insgesamt nichtig (§§ 311b BGB, 125 BGB).
- **Abbruchhaftung überschätzt** — der Grundsatz ist die Abschlussfreiheit; Haftung setzt einen erweckten Vertrauenstatbestand **und** einen Abbruch ohne triftigen Grund voraus.
- **NDA ohne Vertragsstrafe** — der Verstoß bleibt praktisch sanktionslos, weil der Schaden nicht bezifferbar ist; zugleich fehlt eine wirksame Sanktion für den Nachweis angemessener Geheimhaltungsmaßnahmen.
- **Keine Nachwirkungsdauer im NDA vereinbart** — endet die Vereinbarung mit Abbruch der Verhandlungen, entfällt der Schutz genau dann, wenn er gebraucht wird.
- **Break-up Fee als faktischer Abschlusszwang** — bei formbedürftigen Verträgen und in AGB angreifbar (§§ 138, 307 BGB); Höhe an den tatsächlichen Transaktionskosten orientieren.
- **c.i.c. neben dem Mängelrecht geltend gemacht** — für fahrlässige Angaben über die Sachbeschaffenheit ist die c.i.c. nach Gefahrübergang gesperrt; nur Arglist trägt.
