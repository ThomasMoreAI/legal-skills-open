---
name: krypto-whitepaper-angebot-borghei
title: /krypto-mikar:krypto-whitepaper-angebot
description: Öffentliches Angebot von Kryptowerten und Kryptowerte-Whitepaper – Angebot sonstiger Kryptowerte Art. 4 und Zulassung zum Handel Art. 5 VO (EU) 2023/1114, Inhalt und Form des Whitepapers Art. 6, Marketingmitteilungen Art. 7, Übermittlung an die zuständige Behörde Art. 8, Veröffentlichung Art. 9, Aktualisierung Art. 12, Widerrufsrecht der Verbraucher Art. 13, Haftung für die Whitepaper-Informationen Art. 15 nebst § 19 KMAG, Sonderregime für vermögenswertreferenzierte Token mit Zulassung Art. 16 und Whitepaper Art. 19 sowie Vermögenswertreserve Art. 36, Sonderregime für E-Geld-Token Art. 48 mit Emittentenvorbehalt und Whitepaper Art. 51, Aussetzung und Untersagung von Angeboten § 15 KMAG, Befugnisse zu Whitepaper und Marketing §§ 16, 17 KMAG. Use when ein Token öffentlich angeboten oder zum Handel zugelassen werden soll oder eine Whitepaper-Haftung im Raum steht.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/krypto-mikar/skills/krypto-whitepaper-angebot
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: finance
language: de
---

# /krypto-mikar:krypto-whitepaper-angebot

## Zweck

Der Skill begleitet ein öffentliches Angebot oder eine Handelszulassung von Kryptowerten: Welches Whitepaper-Regime gilt, was muss darin stehen, wer haftet wofür — und welche Befugnisse hat die BaFin, das Angebot zu stoppen. Er hält die drei Regime auseinander, die je nach Tokenklasse gelten, und behandelt die Haftungsnorm, die in der Beratung regelmäßig unterschätzt wird.

## Eingaben

- Tokenklasse nach vorheriger Einordnung (`/krypto-mikar:micar-anwendungsbereich-token`)
- Angebotsstruktur: Adressatenkreis, Volumen, Gegenleistung, Zeitraum, Vertriebsweg
- Ob eine Zulassung zum Handel auf einer Handelsplattform angestrebt wird
- Whitepaper-Entwurf und Marketingmaterialien
- Emittent bzw. Anbieter: Sitz, Rechtsform, Erlaubnislage
- Zielgruppe: Verbraucher oder ausschließlich qualifizierte Anleger
- Ob bereits eine Übermittlung an die zuständige Behörde erfolgt ist

## Sub-Agent-Architektur

Der Researcher beschafft MiCAR Titel II bis IV, das KMAG und die BaFin-Verlautbarungen zu Whitepaper und Marketing. Der Drafter erstellt oder prüft das Whitepaper entlang der Anforderungen des Art. 6 und formuliert die Haftungsanalyse. Der Reviewer kontrolliert die Regimezuordnung, die Vollständigkeit der Pflichtangaben und ob das Widerrufsrecht des Art. 13 zutreffend behandelt ist.

## Ablauf

### 1. Regime nach Tokenklasse bestimmen

| Tokenklasse | Regime | Kern |
|---|---|---|
| **Sonstige Kryptowerte** | **Titel II**, Art. 4 bis 15 | Whitepaper mit **Übermittlung** an die zuständige Behörde (Art. 8) — **keine Genehmigung** |
| **Vermögenswertreferenzierte Token (ART)** | **Titel III** | **Zulassung** nach Art. 16 erforderlich; Whitepaper Art. 19; Vermögenswertreserve Art. 36 |
| **E-Geld-Token (EMT)** | **Titel IV** | Emission nur durch **Kreditinstitut oder E-Geld-Institut** (Art. 48); Whitepaper Art. 51 |

**Der wichtigste Unterschied:** Bei sonstigen Kryptowerten wird das Whitepaper nach Art. 8 lediglich **übermittelt** — es findet **keine** behördliche Billigung statt wie beim Wertpapierprospekt. Wer dem Markt eine „BaFin-Genehmigung" suggeriert, riskiert zugleich einen Verstoß gegen die Marketingvorgaben.

Bei ART ist demgegenüber eine **echte Zulassung** nach Art. 16 erforderlich; ohne sie greift [§ 9 Abs. 1 Nr. 1 KMAG](https://www.gesetze-im-internet.de/kmag/__9.html) mit der Anordnung der sofortigen Einstellung.

### 2. Öffentliches Angebot und Handelszulassung (Art. 4, 5 MiCAR)

**Art. 4** regelt die Anforderungen an öffentliche Angebote sonstiger Kryptowerte, **Art. 5** die Zulassung zum Handel. Beide knüpfen an die Erstellung, Übermittlung und Veröffentlichung eines Whitepapers an und sehen Ausnahmen vor — etwa für Angebote an einen begrenzten Personenkreis, für unentgeltlich angebotene Kryptowerte oder für bestimmte Kleinemissionen. **Der Ausnahmekatalog ist im Wortlaut vollständig durchzugehen und zu zitieren**; er ist der praktisch wichtigste Gestaltungsspielraum `[unverifiziert – prüfen]`.

Wird die Zulassung zum Handel beantragt, trifft die Pflichten regelmäßig der **Betreiber der Handelsplattform**, wenn kein Anbieter vorhanden ist — die Zuordnung ist vertraglich zu klären.

### 3. Whitepaper: Inhalt und Form (Art. 6 MiCAR)

Das Kryptowerte-Whitepaper muss die Informationen enthalten, die Interessenten eine informierte Anlageentscheidung ermöglichen. Zu den Anforderungen zählen insbesondere:

- Angaben zum **Anbieter bzw. Emittenten** und zu den an der Umsetzung beteiligten Personen;
- Beschreibung des **Projekts** und der Verwendung der eingesammelten Mittel;
- Merkmale des **öffentlichen Angebots** oder der Handelszulassung, einschließlich Anzahl, Preis, Zeichnungsbedingungen;
- **Rechte und Pflichten**, die mit dem Kryptowert verbunden sind;
- Angaben zur zugrunde liegenden **Technologie** und zu den Konsensmechanismen;
- **Risiken**;
- Angaben zu den **nachteiligen Auswirkungen auf das Klima und die Umwelt** des verwendeten Konsensmechanismus.

Formal verlangt Art. 6 unter anderem eine **Erklärung des Leitungsorgans** zur Übereinstimmung mit der Verordnung, eine **Zusammenfassung** mit Warnhinweisen und einen **Datumsvermerk**; das Whitepaper darf **keine Aussagen zum künftigen Wert** enthalten, die nicht die Grenzen des Art. 6 wahren. Der vollständige Pflichtangabenkatalog ist am Wortlaut abzuarbeiten und nicht aus dem Gedächtnis zu rekonstruieren.

### 4. Marketing, Übermittlung, Veröffentlichung, Aktualisierung (Art. 7, 8, 9, 12)

| Norm | Pflicht |
|---|---|
| **Art. 7** | **Marketingmitteilungen** müssen als solche erkennbar, redlich, klar und nicht irreführend sein und mit dem Whitepaper übereinstimmen |
| **Art. 8** | **Übermittlung** des Whitepapers und der Marketingmitteilungen an die zuständige Behörde |
| **Art. 9** | **Veröffentlichung** auf der Website des Anbieters |
| **Art. 12** | **Aktualisierung** bei wesentlichen neuen Umständen |

Die BaFin kann nach **[§ 16 KMAG](https://www.gesetze-im-internet.de/kmag/__16.html)** Befugnisse hinsichtlich des Whitepapers und modifizierter Fassungen ausüben und nach **[§ 17 KMAG](https://www.gesetze-im-internet.de/kmag/__17.html)** gegen **Marketingmitteilungen** vorgehen. Nach **[§ 15 KMAG](https://www.gesetze-im-internet.de/kmag/__15.html)** kann sie ein öffentliches Angebot **aussetzen oder untersagen**; nach **[§ 18](https://www.gesetze-im-internet.de/kmag/__18.html)** und **[§ 30 KMAG](https://www.gesetze-im-internet.de/kmag/__30.html)** marktrelevante Informationen bekannt machen. Auch diese Maßnahmen sind nach [§ 5 KMAG](https://www.gesetze-im-internet.de/kmag/__5.html) **sofort vollziehbar**.

### 5. Widerrufsrecht der Verbraucher (Art. 13 MiCAR)

Verbraucher, die einen sonstigen Kryptowert **unmittelbar vom Anbieter** oder von einem für ihn tätigen Anbieter von Kryptowerte-Dienstleistungen erwerben, haben ein **Widerrufsrecht**. Es gilt **nicht**, wenn der Kryptowert zum Handel auf einer Handelsplattform zugelassen ist. Frist, Beginn und Rechtsfolgen ergeben sich aus Art. 13 und sind im konkreten Angebot am Wortlaut auszuweisen; das Widerrufsrecht ist im Whitepaper und in den Vertragsunterlagen abzubilden `[unverifiziert – prüfen]` hinsichtlich der genauen Fristenlänge.

### 6. Haftung (Art. 15 MiCAR, § 19 KMAG)

**Art. 15** begründet die **Haftung für die im Whitepaper enthaltenen Informationen**: Sind sie **unvollständig, unredlich oder unklar** oder **irreführend**, haften der Anbieter, der Emittent bzw. der Betreiber der Handelsplattform sowie die Mitglieder des Leitungsorgans dem Inhaber gegenüber auf Ersatz des erlittenen Schadens. Der Inhaber muss darlegen, dass er die Entscheidung auf der Grundlage dieser Informationen getroffen hat; eine vertragliche Haftungsbeschränkung ist unwirksam.

**[§ 19 KMAG](https://www.gesetze-im-internet.de/kmag/__19.html)** flankiert dies mit der **Haftung bei fehlendem Kryptowerte-Whitepaper** — dem Fall, dass ein Whitepaper gar nicht erst erstellt wurde. Beide Anspruchsgrundlagen sind nebeneinander zu prüfen und im Ausgabeformat getrennt zu führen.

Für die **Leitungsorgane** bedeutet das eine persönliche Außenhaftung, die in der D&O-Deckung gesondert zu prüfen ist.

## Deterministische Berechnung

Der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) macht nur die Arithmetik; die Fristlängen sind dem Verordnungstext zu entnehmen:

```bash
# Widerrufsfrist nach Art. 13 MiCAR - Länge am Wortlaut prüfen, hier Beispielrechnung
python -m scripts.legal_calc.cli frist --ereignis 03.03.2026 --menge 14 --einheit tage --land HE

# Vorlauf zwischen Übermittlung nach Art. 8 und Angebotsbeginn: 20 Arbeitstage ab 01.02.2026,
# von Hand auszuzählen (VO 1182/71: Übermittlungstag, Sa, So und die ausgegebenen
# Feiertage zählen nicht mit) - der Rechner hat keine Einheit Arbeitstage
python -m scripts.legal_calc.cli feiertage --jahr 2026 --land HE

# Verjährung eines Schadensersatzanspruchs aus Art. 15 MiCAR / § 19 KMAG, §§ 195, 199 BGB
python -m scripts.legal_calc.cli verjaehrung --entstehung 03.03.2026 --kenntnis 03.03.2026
```

## Quellen

### Rechtsakte

- Verordnung (EU) 2023/1114 (MiCAR), Art. 4, 5, 6, 7, 8, 9, 12, 13, 15, 16, 19, 36, 48, 51 — [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2023/1114/oj)
- [KMAG](https://www.gesetze-im-internet.de/kmag/) – [§ 5](https://www.gesetze-im-internet.de/kmag/__5.html), [§ 9](https://www.gesetze-im-internet.de/kmag/__9.html), [§ 15](https://www.gesetze-im-internet.de/kmag/__15.html), [§ 16](https://www.gesetze-im-internet.de/kmag/__16.html), [§ 17](https://www.gesetze-im-internet.de/kmag/__17.html), [§ 18](https://www.gesetze-im-internet.de/kmag/__18.html), [§ 19](https://www.gesetze-im-internet.de/kmag/__19.html), [§ 30 KMAG](https://www.gesetze-im-internet.de/kmag/__30.html)
- [§ 195 BGB](https://www.gesetze-im-internet.de/bgb/__195.html), [§ 199 BGB](https://www.gesetze-im-internet.de/bgb/__199.html)
- Verordnung (EU) 2017/1129 (Prospekt-VO) zur Abgrenzung — [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2017/1129/oj)

### Kommentare und Literatur

- Maume/Maute, MiCAR, Kommentar, Titel II bis IV `[unverifiziert – prüfen]`
- BaFin, Hinweise zum Kryptowerte-Whitepaper und zu Marketingmitteilungen.
- Zur Prospekthaftung als Vergleichsmaßstab: Assmann/Schlitt/von Kopp-Colomb, WpPG/Prospekt-VO.

### Rechtsprechung

Zur Whitepaper-Haftung nach Art. 15 MiCAR und zu § 19 KMAG liegt **keine** Rechtsprechung vor. Als Auslegungshilfe kann die Judikatur zur Prospekthaftung dienen; jede konkrete Entscheidung ist vor Verwendung in juris oder Beck-Online zu verifizieren; ohne Beleg gilt sie als `[unverifiziert – prüfen]`.

## Ausgabeformat

```
KRYPTOWERTE-ANGEBOT / WHITEPAPER — <Mandat> — <Datum>

I.   Regimezuordnung
     Tokenklasse:             [sonstiger Kryptowert / ART / EMT]
     Regime:                  [Titel II Art. 4–15 / Titel III Art. 16, 19, 36 / Titel IV Art. 48, 51]
     Zulassung erforderlich:  [nein — nur Übermittlung Art. 8 / ja Art. 16 / Emittentenvorbehalt Art. 48]

II.  Angebot
     Adressaten:              <Verbraucher / qualifizierte Anleger>
     Ausnahmetatbestand Art. 4/5: [einschlägig — Wortlaut zitiert / nicht einschlägig]
     Handelszulassung:        [beantragt — Pflichtenträger: Anbieter / Plattformbetreiber]

III. Whitepaper Art. 6
     Anbieter/Emittent:       [enthalten / fehlt]
     Projekt und Mittelverwendung: [enthalten / fehlt]
     Angebotsmerkmale:        [enthalten / fehlt]
     Rechte und Pflichten:    [enthalten / fehlt]
     Technologie:             [enthalten / fehlt]
     Risiken:                 [enthalten / fehlt]
     Klima- und Umweltauswirkungen: [enthalten / fehlt]
     Erklärung des Leitungsorgans / Zusammenfassung / Datum: [vorhanden / fehlt]

IV.  Verfahren
     Übermittlung Art. 8:     [erfolgt am <Datum> / offen]  (keine Billigung!)
     Veröffentlichung Art. 9: <Website>
     Marketing Art. 7:        [konform / zu ändern]
     Aktualisierung Art. 12:  <Auslöser>

V.   Widerrufsrecht Art. 13
     Einschlägig:             [ja — Verbraucher, kein Handelsplatz / nein]
     Frist und Belehrung:     <am Wortlaut ausgewiesen>

VI.  Haftung
     Art. 15 MiCAR:           <Anbieter / Emittent / Plattformbetreiber / Leitungsorgan>
     § 19 KMAG (fehlendes Whitepaper): [einschlägig / nein]
     Persönliche Außenhaftung / D&O: <…>

VII. Aufsichtliche Eingriffe
     § 15 KMAG Aussetzung/Untersagung | §§ 16, 17 KMAG Whitepaper und Marketing
     § 5 KMAG: sofort vollziehbar

VIII.Risiko: 🟢 / 🟡 / 🔴 <Begründung>
IX.  Quellenverzeichnis
```

## Risiken / typische Fehler

- **Whitepaper für gebilligt gehalten.** Bei sonstigen Kryptowerten findet nach Art. 8 nur eine **Übermittlung** statt — keine Billigung wie beim Wertpapierprospekt. Entsprechende Werbeaussagen verstoßen gegen Art. 7.
- **ART ohne Zulassung nach Art. 16 angeboten.** Das löst § 9 Abs. 1 Nr. 1 KMAG aus.
- **E-Geld-Token ohne Kreditinstituts- oder E-Geld-Institutseigenschaft ausgegeben** (Art. 48).
- **Klima- und Umweltangaben weggelassen.** Sie gehören zum Pflichtinhalt des Whitepapers.
- **Widerrufsrecht des Art. 13 übersehen** — oder umgekehrt angenommen, obwohl der Kryptowert zum Handel zugelassen ist.
- **Haftung nur nach Art. 15 geprüft.** § 19 KMAG erfasst zusätzlich den Fall des **fehlenden** Whitepapers.
- **Haftung der Leitungsorgane nicht adressiert** und die D&O-Deckung nicht geprüft.
- **Ausnahmetatbestände der Art. 4, 5 aus dem Gedächtnis zitiert** statt am Wortlaut geprüft.
- **Marketingmitteilungen nicht mit dem Whitepaper abgeglichen** (Art. 7).
- **Rechtsprechung erfunden.** Zu MiCAR und KMAG gibt es sie noch nicht; jede Entscheidung ist zu belegen oder als `[unverifiziert – prüfen]` zu kennzeichnen.
