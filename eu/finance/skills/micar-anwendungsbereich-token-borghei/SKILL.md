---
name: micar-anwendungsbereich-token-borghei
title: /krypto-mikar:micar-anwendungsbereich-token
description: Anwendungsbereich der MiCAR und Einordnung von Kryptowerten – Gegenstand und Geltungsbereich Art. 1, 2 VO (EU) 2023/1114 mit den Bereichsausnahmen des Art. 2 Abs. 3 und 4, Legaldefinition des Kryptowerts Art. 3 Abs. 1 Nr. 5 und die drei Klassen vermögenswertreferenzierte Token, E-Geld-Token und sonstige Kryptowerte, Abgrenzung zu Finanzinstrumenten nach MiFID II und zum Erlaubnisregime von KWG, WpIG, KAGB und ZAG, Durchführung durch das KMAG § 1 mit dem Ausschluss der in Art. 2 Abs. 3, 4 genannten Kryptowerte, Aufgaben und Befugnisse der BaFin §§ 3, 4 KMAG, sofortige Vollziehbarkeit § 5 KMAG sowie das Einschreiten gegen unerlaubte Geschäfte § 9 KMAG. Use when zu klären ist, ob ein Token der MiCAR unterfällt, welcher Klasse er angehört und welches Erlaubnisregime gilt.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/krypto-mikar/skills/micar-anwendungsbereich-token
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: finance
language: de
---

# /krypto-mikar:micar-anwendungsbereich-token

## Zweck

Der Skill beantwortet die Eingangsfrage jedes Kryptomandats: Ist der Token ein Kryptowert im Sinne der MiCAR, welcher Klasse gehört er an — und ist er womöglich gar kein MiCAR-Fall, sondern ein **Finanzinstrument** unter MiFID II und damit ein Fall für KWG und WpIG. Die Fehleinordnung an dieser Stelle zieht das gesamte weitere Regime falsch.

## Eingaben

- Tokenbeschreibung: Funktion, Rechte des Inhabers, Wertbezug, Emissionsmechanik
- Whitepaper, Term Sheet, Smart-Contract-Dokumentation
- Wertreferenz: an eine amtliche Währung, an einen Korb, an sonstige Werte oder keine
- Rücktauschrecht und dessen Ausgestaltung
- Emittent: Sitz, Rechtsform, bestehende Erlaubnisse
- Vertriebsweg und Zielmarkt; ob ein öffentliches Angebot oder eine Handelszulassung geplant ist
- Ob der Token in einem geschlossenen Netzwerk, als Bonuspunkt oder als NFT ausgestaltet ist

## Sub-Agent-Architektur

Der Researcher beschafft die MiCAR, das KMAG, die einschlägigen Aufsichtsgesetze und die Verlautbarungen von BaFin, EBA und ESMA. Der Drafter nimmt die Einordnung anhand der Definitionen des Art. 3 vor und begründet sie merkmalsweise. Der Reviewer prüft insbesondere die Abgrenzung zum Finanzinstrument und ob eine Bereichsausnahme des Art. 2 Abs. 3, 4 vorschnell bejaht wurde.

## Ablauf

### 1. Vorrangfrage: Finanzinstrument oder Kryptowert

**Dieser Schritt steht vor allem anderen.** Die MiCAR gilt **nicht** für Kryptowerte, die als **Finanzinstrumente** im Sinne der MiFID II einzuordnen sind — für sie gelten Wertpapier- und Bankaufsichtsrecht. Die Prüfreihenfolge lautet deshalb:

| Frage | Regime |
|---|---|
| Verkörpert der Token ein **Finanzinstrument** (Aktie, Schuldverschreibung, Derivat, Anteil an einem Organismus für gemeinsame Anlagen)? | MiFID II, WpHG, WpPG bzw. Prospekt-VO, [WpIG](https://www.gesetze-im-internet.de/wpig/), [KWG](https://www.gesetze-im-internet.de/kredwg/) — **nicht** MiCAR (`/kapitalmarktrecht:prospektpflicht-pruefung`) |
| Ist er eine **Einlage**, ein **strukturierter Einlage** oder ein **E-Geld** außerhalb der EMT-Definition? | KWG, [ZAG](https://www.gesetze-im-internet.de/zag_2018/) |
| Ist er ein **Investmentvermögen**? | [KAGB](https://www.gesetze-im-internet.de/kagb/) |
| Sonst: digitale Darstellung eines Werts oder Rechts, die mittels Distributed-Ledger-Technologie übertragen und gespeichert werden kann | **MiCAR** |

Die Einordnung erfolgt **funktional** anhand der verbrieften Rechte, nicht anhand der Bezeichnung im Whitepaper. Die BaFin- und ESMA-Verlautbarungen zur Abgrenzung sind heranzuziehen `[unverifiziert – prüfen]` hinsichtlich des jeweiligen Stands.

### 2. Anwendungsbereich und Ausnahmen (Art. 1, 2 MiCAR)

Die Verordnung regelt öffentliche Angebote und die Zulassung zum Handel von Kryptowerten sowie die Erbringung von Kryptowerte-Dienstleistungen. **[§ 1 Abs. 2 KMAG](https://www.gesetze-im-internet.de/kmag/__1.html)** stellt für das deutsche Durchführungsrecht klar: Es gilt für Kryptowerte nach **Art. 3 Abs. 1 Nr. 5** MiCAR und **nicht** für Kryptowerte im Sinne des **Art. 2 Abs. 3 und 4** MiCAR.

Die Bereichsausnahmen des Art. 2 Abs. 3, 4 erfassen unter anderem Kryptowerte, die **einzigartig und nicht fungibel** sind, sowie bestimmte in geschlossenen Netzwerken verwendbare oder als Kundenbindungsinstrument ausgegebene Werte. **Vorsicht:** Die NFT-Ausnahme greift nicht schon deshalb, weil ein Token technisch als NFT ausgegeben wird — entscheidend ist die tatsächliche Einzigartigkeit und fehlende Fungibilität; eine große Serie faktisch austauschbarer Stücke fällt regelmäßig **nicht** darunter. Der Wortlaut des Art. 2 Abs. 3, 4 ist im Einzelfall vollständig durchzugehen und zu zitieren `[unverifiziert – prüfen]`.

### 3. Tokenklasse bestimmen (Art. 3 MiCAR)

| Klasse | Merkmal | Regime |
|---|---|---|
| **Vermögenswertreferenzierter Token (ART)** | soll Wertstabilität durch Bezug auf einen **anderen Wert, ein Recht oder eine Kombination** — auch mehrere amtliche Währungen — wahren | **Titel III**: Zulassung [Art. 16](https://eur-lex.europa.eu/eli/reg/2023/1114/oj), Whitepaper Art. 19, Vermögenswertreserve Art. 36 |
| **E-Geld-Token (EMT)** | soll Wertstabilität durch Bezug auf **eine einzige amtliche Währung** wahren | **Titel IV**: Art. 48 — Emission nur durch **Kreditinstitut oder E-Geld-Institut**; Whitepaper Art. 51 |
| **Sonstiger Kryptowert** | weder ART noch EMT (Utility Token, Zahlungstoken ohne Wertbezug) | **Titel II**: Art. 4 bis 15 |

Die Zuordnung entscheidet über Zulassungserfordernis, Whitepaper-Regime, Reserve- und Rücktauschpflichten. Ein an den Euro gekoppelter Stablecoin ist **EMT** und darf nur von einem Kreditinstitut oder E-Geld-Institut ausgegeben werden — das ist die praktisch folgenreichste Weichenstellung.

### 4. Deutsches Durchführungsrecht (KMAG)

Das **[Kryptomärkteaufsichtsgesetz](https://www.gesetze-im-internet.de/kmag/)** führt die MiCAR durch:

- **[§ 1 KMAG](https://www.gesetze-im-internet.de/kmag/__1.html)** — Ziel und Geltungsbereich; Befugnisse der BaFin nach anderen Vorschriften bleiben unberührt (Abs. 3).
- **[§ 3](https://www.gesetze-im-internet.de/kmag/__3.html)** — Aufgaben der Bundesanstalt; **[§ 4](https://www.gesetze-im-internet.de/kmag/__4.html)** — allgemeine Befugnisse.
- **[§ 5](https://www.gesetze-im-internet.de/kmag/__5.html)** — **sofortige Vollziehbarkeit** von Maßnahmen; das verkürzt den Eilrechtsschutz erheblich und ist in jeder Verteidigungsstrategie einzuplanen.
- **[§ 6](https://www.gesetze-im-internet.de/kmag/__6.html)**, **[§ 7](https://www.gesetze-im-internet.de/kmag/__7.html)** — Zusammenarbeit mit der Deutschen Bundesbank und sonstigen Stellen; **[§ 8](https://www.gesetze-im-internet.de/kmag/__8.html)** — Verschwiegenheit.
- **[§ 9](https://www.gesetze-im-internet.de/kmag/__9.html)** — **Einschreiten gegen unerlaubte Geschäfte**: Die BaFin kann die **sofortige Einstellung des Geschäftsbetriebs** und die **unverzügliche Abwicklung** anordnen — und zwar gegenüber dem Unternehmen, **seinen Gesellschaftern und den Mitgliedern seiner Organe** —, wenn ohne die nach Art. 16 Abs. 1 Buchst. a erforderliche Zulassung ART öffentlich angeboten werden, ohne die nach Art. 48 Abs. 1 UAbs. 1 Buchst. a erforderliche Zulassung E-Geld-Token angeboten werden oder in weiteren dort genannten Fällen. **[§ 10](https://www.gesetze-im-internet.de/kmag/__10.html)** — Verfolgung unerlaubter Geschäfte.
- **[§ 14](https://www.gesetze-im-internet.de/kmag/__14.html)** — Bekanntmachungen und Register.

Die persönliche Adressierbarkeit von Gesellschaftern und Organmitgliedern nach § 9 KMAG ist der schärfste Hebel der Aufsicht und in der Beratung früh zu benennen.

### 5. Folgefragen

- Öffentliches Angebot und Whitepaper → `/krypto-mikar:krypto-whitepaper-angebot`
- Zulassung als Anbieter von Kryptowerte-Dienstleistungen und Übergangsrecht → `/krypto-mikar:casp-zulassung-uebergang`
- Insiderhandel und Marktmanipulation → `/krypto-mikar:krypto-marktmissbrauch`
- Geldwäscherechtliche Pflichten → `/geldwaesche-aml-kyc:kyc-sorgfaltspflichten` bzw. die einschlägige Skill; die Geldtransfer-Verordnung und das GwG treten **neben** die MiCAR.

## Deterministische Berechnung

Der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) macht nur die Arithmetik:

```bash
# Widerspruchs- bzw. Klagefrist gegen eine Maßnahme der BaFin
python -m scripts.legal_calc.cli frist --ereignis 15.09.2026 --menge 1 --einheit monate --land HE

# Antragsfrist im vereinfachten Zulassungsverfahren nach § 50 Abs. 3 KMAG
python -m scripts.legal_calc.cli frist --ereignis 15.09.2026 --menge 3 --einheit monate --land HE
```

Beachte: Maßnahmen nach dem KMAG sind nach § 5 KMAG regelmäßig **sofort vollziehbar**; der Rechtsbehelf hat keine aufschiebende Wirkung.

## Quellen

### Rechtsakte

- Verordnung (EU) 2023/1114 (MiCAR), Art. 1, 2, 3, 4, 16, 36, 48, 59, 143 — [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2023/1114/oj)
- [KMAG](https://www.gesetze-im-internet.de/kmag/) – [§ 1](https://www.gesetze-im-internet.de/kmag/__1.html), [§ 3](https://www.gesetze-im-internet.de/kmag/__3.html), [§ 4](https://www.gesetze-im-internet.de/kmag/__4.html), [§ 5](https://www.gesetze-im-internet.de/kmag/__5.html), [§ 9](https://www.gesetze-im-internet.de/kmag/__9.html), [§ 10](https://www.gesetze-im-internet.de/kmag/__10.html), [§ 14 KMAG](https://www.gesetze-im-internet.de/kmag/__14.html)
- Richtlinie 2014/65/EU (MiFID II) — [EUR-Lex](https://eur-lex.europa.eu/eli/dir/2014/65/oj)
- [KWG](https://www.gesetze-im-internet.de/kredwg/), [WpIG](https://www.gesetze-im-internet.de/wpig/), [KAGB](https://www.gesetze-im-internet.de/kagb/), [ZAG](https://www.gesetze-im-internet.de/zag_2018/), [GwG](https://www.gesetze-im-internet.de/gwg_2017/)

### Kommentare und Literatur

- Maume/Maute, MiCAR, Kommentar `[unverifiziert – prüfen]` hinsichtlich Auflage und Erscheinungsjahr
- Zetzsche/Annunziata u. a. zur Einordnung von Kryptowerten.
- BaFin, Merkblätter und Auslegungshinweise zu Kryptowerten und zur MiCAR.
- EBA- und ESMA-Leitlinien zur Abgrenzung von Finanzinstrumenten und zur Klassifizierung.

### Rechtsprechung

Zur MiCAR und zum KMAG liegt bislang **keine** gefestigte Rechtsprechung vor. Für die Abgrenzung zum Finanzinstrument und zum Einlagengeschäft ist auf die Judikatur zum KWG zurückzugreifen; jede konkrete Entscheidung ist vor Verwendung in juris oder Beck-Online zu verifizieren; ohne Beleg gilt sie als `[unverifiziert – prüfen]`.

## Ausgabeformat

```
MiCAR-EINORDNUNG — <Token / Mandant> — <Datum>

I.   Vorrangprüfung
     Finanzinstrument (MiFID II):     [ja — WpHG/WpIG/KWG, MiCAR nicht anwendbar / nein]
     Einlage / E-Geld außerhalb EMT:  [ja — KWG/ZAG / nein]
     Investmentvermögen:              [ja — KAGB / nein]
     Ergebnis:                        [MiCAR anwendbar / anderes Regime]

II.  Bereichsausnahmen Art. 2 Abs. 3, 4
     Einzigartig und nicht fungibel:  [ja / nein — Serie faktisch austauschbar]
     Geschlossenes Netzwerk / Kundenbindung: [ja / nein]
     § 1 Abs. 2 KMAG:                 [ausgenommen / erfasst]

III. Tokenklasse Art. 3
     Wertbezug:               [eine amtliche Währung / mehrere Werte / keiner]
     Klasse:                  [E-Geld-Token / vermögenswertreferenzierter Token / sonstiger Kryptowert]
     Folge:                   [Titel IV — nur Kreditinstitut oder E-Geld-Institut, Art. 48 /
                               Titel III — Zulassung Art. 16, Reserve Art. 36 /
                               Titel II — Art. 4 bis 15]

IV.  Deutsche Aufsicht
     Zuständig:               BaFin (§§ 3, 4 KMAG)
     Sofortige Vollziehbarkeit § 5 KMAG: zu beachten
     Risiko unerlaubter Geschäfte § 9 KMAG: [Anordnung gegen Unternehmen, Gesellschafter und Organe]

V.   Angrenzende Pflichten
     GwG / Geldtransfer-VO:   <…>
     Prospekt-/Wertpapierrecht: <…>

VI.  Nächste Schritte
     [Whitepaper / Zulassung / Übergangsrecht / Marktmissbrauchs-Compliance]

VII. Risiko: 🟢 / 🟡 / 🔴 <Begründung>
VIII.Quellenverzeichnis
```

## Risiken / typische Fehler

- **MiCAR geprüft, obwohl ein Finanzinstrument vorliegt.** Tokenisierte Aktien, Schuldverschreibungen und Fondsanteile unterfallen MiFID II, WpHG und KWG — nicht der MiCAR.
- **NFT-Ausnahme pauschal bejaht.** Art. 2 Abs. 3, 4 verlangt tatsächliche Einzigartigkeit und fehlende Fungibilität; eine große Serie austauschbarer Stücke fällt regelmäßig darunter **nicht**.
- **EMT und ART verwechselt.** Bezug auf **eine** amtliche Währung macht den Token zum **E-Geld-Token** — mit dem Emittentenvorbehalt des Art. 48 für Kreditinstitute und E-Geld-Institute.
- **Emittentenvorbehalt des Art. 48 übersehen.** Ein an den Euro gekoppelter Stablecoin darf nicht von einer beliebigen Gesellschaft ausgegeben werden.
- **§ 9 KMAG unterschätzt.** Die Anordnung richtet sich auch gegen **Gesellschafter und Organmitglieder** persönlich.
- **Sofortige Vollziehbarkeit nach § 5 KMAG nicht eingeplant.** Der Rechtsbehelf hat keine aufschiebende Wirkung.
- **Einordnung nach der Bezeichnung im Whitepaper vorgenommen** statt funktional nach den verbrieften Rechten.
- **Geldwäscherecht ausgeblendet.** GwG und Geldtransfer-Verordnung treten neben die MiCAR.
- **Rechtsprechung erfunden.** Zu MiCAR und KMAG gibt es sie noch nicht; jede Entscheidung ist zu belegen oder als `[unverifiziert – prüfen]` zu kennzeichnen.
