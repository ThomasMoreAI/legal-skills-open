---
name: patentverletzung-klage-borghei
title: /patentrecht:patentverletzung-klage
description: Klageschrift-Gerüst für eine Patentverletzung nach §§ 9, 10, 14, 139–142a PatG inkl. Düsseldorfer Praxis – Schutzbereichsbestimmung mit Merkmalsgliederung und Äquivalenzlehre, Anspruchskatalog mit dreifacher Schadensberechnung, Wahl zwischen LG-Patentstreitkammer und UPC. Use when ein Patentinhaber eine Verletzung verfolgen will oder ein Beklagter Klageerwiderung vorbereiten muss.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/patentrecht/skills/patentverletzung-klage
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: ip
language: de
---

# /patentrecht:patentverletzung-klage

## Zweck

Der Skill strukturiert die Patentverletzungsklage nach dem Düsseldorfer Modell: Schutzrechtsbestand → Merkmalsgliederung des Hauptanspruchs → Verletzungstatbestand (Wortlaut / Äquivalenz) → Anspruchskatalog § 139 ff. PatG. Er adressiert zugleich die strategische Forumswahl (LG mit Patentstreitkammer vs. Einheitliches Patentgericht UPC bei EP-Bündelpatenten ohne Opt-out) und die Verjährung § 141 PatG.

## Eingaben

- Schutzrecht (DE-Patent / EP-validiert / Einheitspatent / Gebrauchsmuster) mit Veröffentlichungs-/Erteilungsdaten
- Patentanspruch (Hauptanspruch + relevante Unteransprüche)
- angegriffene Ausführungsform (technische Beschreibung der Verletzungshandlung)
- Verletzungszeitraum (erste Kenntnis, fortlaufende Handlungen, Geltungsbereich)
- bekannte Stand-der-Technik / Nichtigkeitsangriffe
- UPC-Opt-out-Status (bei EP-Bündelpatent)
- bei SEPs: FRAND-Korrespondenz mit Beklagtem (Querverweis kartellrecht)

## Sub-Agent-Architektur

Researcher liefert PatG- und EPÜ-Statute, BGH-X-ZS-Rspr. (insbesondere zu Schutzbereich und Äquivalenz), OLG-Düsseldorf-Serie sowie Kommentarstellen aus Benkard, Kühnen, Mes. Drafter erstellt das Klageschrift-Gerüst inkl. Merkmalsgliederung, Verletzungsbegründung und Anspruchskatalog mit dreifacher Schadensberechnung. Reviewer prüft Verjährung § 141 PatG, Forumwahl, UPC-Opt-out-Status und Sachkundigenvertretung § 143 PatG.

## Ablauf

### 1. Schutzrechtsbestand

- Erteilung in Kraft? **Erloschen** § 20 PatG (Verzicht, Nicht-Zahlung Jahresgebühren), **nichtig** § 22 iVm §§ 81 ff. PatG, **widerrufen** im Einspruch § 59 PatG?
- Bei EP-Bündelpatent: Validierung in DE durchgeführt (§ 65 PatG)? Übersetzung beim DPMA hinterlegt?
- Bei Einheitspatent: Eintragung in das Register für einheitliche Patente?
- Bei Gebrauchsmuster: anhängiges Löschungsverfahren (§ 13 GebrMG)?

### 2. Merkmalsgliederung

Der Hauptanspruch wird in **Merkmale (M1, M2, M3 …)** zerlegt. Jedes Merkmal wird einer Stelle der angegriffenen Ausführungsform gegenübergestellt. Dies ist die zentrale prozessuale Arbeitstechnik und Grundlage der Subsumtion.

### 3. Schutzbereich § 14 PatG / Art. 69 EPÜ

Patentansprüche bestimmen den Schutzbereich; Beschreibung und Zeichnungen sind **Auslegungshilfen**, nicht eigenständige Schutzbereichserweiterung (Art. 69 EPÜ + Auslegungsprotokoll).

**Auslegungsmethodik** (BGH-Linie):

1. Sinngehalt der Patentansprüche aus Sicht des Fachmanns am Prioritätstag
2. Beschreibung und Zeichnungen heranziehen, soweit zur Klärung erforderlich
3. Funktion des Merkmals im Patentgefüge
4. „Was das Patent leistet" — kein eng-grammatisches Verständnis

### 4. Verletzungstatbestand

#### 4.1 Wortlautverletzung (§ 9 PatG)

Alle Merkmale des Hauptanspruchs werden — ggf. unter Auslegung — vom angegriffenen Erzeugnis / Verfahren wortsinngemäß verwirklicht. Verletzungshandlungen § 9 S. 2 PatG: Herstellen, Anbieten, Inverkehrbringen, Gebrauchen, Einführen, Besitzen (Erzeugnispatent); Anwenden bzw. Anbieten zur Anwendung (Verfahrenspatent).

#### 4.2 Äquivalente Verletzung

Wenn ein Merkmal nicht wortsinngemäß, sondern durch ein **abgewandeltes Mittel** verwirklicht ist, prüft die BGH-Trias ([„Schneidmesser I", X ZR 168/00](https://lexetius.com/2002,244); [„Schneidmesser II", X ZR 135/01](https://lexetius.com/2002,243); „Schneidmesser III" `[unverifiziert – prüfen]`):

1. **Gleichwirkung** — abgewandeltes Mittel löst objektiv dasselbe technische Problem mit im Wesentlichen gleicher Wirkung
2. **Auffindbarkeit** — Fachmann konnte das abgewandelte Mittel ohne erfinderische Bemühungen finden
3. **Gleichwertigkeit am Patentanspruch orientiert** — Fachmann zieht die Abwandlung als gleichwertige Lösung in Betracht, ausgerichtet am Wortlaut der Ansprüche

Zusätzlich: keine Patentbeschränkung wegen **Auswahlentscheidung** während der Erteilung (Verzicht durch Anmelder; vgl. BGH [„Okklusionsvorrichtung", X ZR 16/09](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=10.05.2011&Aktenzeichen=X+ZR+16/09)).

#### 4.3 Mittelbare Verletzung § 10 PatG

Lieferung von Mitteln, die sich auf ein wesentliches Element der Erfindung beziehen, an nicht zur Benutzung berechtigte Personen, wenn der Lieferant weiß / es offensichtlich ist, dass diese Mittel zur Benutzung der Erfindung im Inland geeignet und bestimmt sind.

### 5. Anspruchskatalog § 139 ff. PatG

| Anspruch | Norm | Voraussetzung |
|---|---|---|
| **Unterlassung** | § 139 I PatG | Verletzung; **kein Verschulden** erforderlich |
| **Beseitigung** | § 139 I PatG | wie Unterlassung |
| **Schadensersatz** | § 139 II PatG | **Verschulden** (Vorsatz / Fahrlässigkeit; idR fahrlässig durch Marktbeobachtungspflicht) |
| **Bereicherungsausgleich (Restschadensersatz)** | §§ 812 ff. BGB iVm § 141 PatG | nach Verjährung des SE-Anspruchs noch 10 Jahre möglich |
| **Auskunft** | § 140b PatG | Verletzung; Drittinformation |
| **Vernichtung** | § 140a I PatG | Erzeugnisse im Besitz / Eigentum des Verletzers |
| **Rückruf** | § 140a III PatG | aus Vertriebskanälen |
| **Besichtigung** | § 140c PatG | hinreichende Wahrscheinlichkeit; Düsseldorfer Besichtigungsverfahren |
| **Urteilsveröffentlichung** | § 140e PatG | im Verkehrskreis |

### 6. Dreifache Schadensberechnung (§ 139 II PatG)

Wahlrecht des Verletzten:

1. **Konkreter eigener Schaden / entgangener Gewinn** (§ 252 BGB; oft schwer beweisbar)
2. **Herausgabe des Verletzergewinns** — der gesamte mit der Verletzung erzielte Gewinn; kausal auf die Verletzung zurückzuführender Anteil; Anrechnung allgemeiner Geschäftsunkosten umstritten (BGH, Urt. v. 02.11.2000 – I ZR 246/98, BGHZ 145, 366 = GRUR 2001, 329 – „Gemeinkostenanteil", [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=02.11.2000&Aktenzeichen=I%20ZR%20246/98); ergangen zum Geschmacksmusterrecht, im Patentrecht entsprechend angewandt)
3. **Lizenzanalogie** — angemessene Lizenzgebühr, die vernünftige Vertragsparteien vereinbart hätten; übliche Lizenzsätze branchen- und produkttypabhängig

Wahl spätestens bis zum Schluss der mündlichen Verhandlung; **Kombination grundsätzlich unzulässig** (BGH `[unverifiziert]`), Stufenklage § 254 ZPO mit Auskunft § 140b PatG ist üblich.

### 7. Forumswahl und Zuständigkeit

#### 7.1 Nationale LG-Patentstreitkammern (§§ 143–145 PatG)

Konzentrationsverordnungen weisen Patentstreitsachen einigen LG zu (insbesondere LG Düsseldorf, LG Mannheim, LG München I, LG Hamburg, LG Braunschweig). Berufung: jeweiliges OLG (z. B. OLG Düsseldorf). Doppelvertretung (Rechtsanwalt + Patentanwalt) gem. § 143 III PatG zulässig und üblich.

#### 7.2 UPC (Einheitliches Patentgericht)

Seit [01.06.2023](https://www.unified-patent-court.org/) zuständig für:

- **Einheitspatente** (zwingend)
- **EP-Bündelpatente** (validierte EP) während Übergangszeit (7 Jahre + Verlängerung) **nur, wenn kein Opt-out erklärt**

**Strategische Überlegung Kläger:** UPC bietet Verfahren mit Wirkung in allen UPC-Mitgliedstaaten in einem Forum, beschleunigte Verfahrensdauer (12–14 Monate Erstinstanz). Risiko: bei Nichtigkeitsangriff zentral verlierbar. Bei Bündelpatenten ohne Opt-out **Forum-Wahl** des Patentinhabers (UPC oder nationales Gericht).

#### 7.3 Bei SEPs

**FRAND-Einrede** (EuGH [„Huawei/ZTE", C-170/13](https://curia.europa.eu/juris/document/document.jsf?docid=165911&doclang=DE)): SEP-Inhaber muss bestimmten Verhandlungsweg einhalten, sonst kartellrechtliche Einrede gegen Unterlassungsanspruch. Querverweis Plugin `kartellrecht`.

### 8. Verjährung § 141 PatG

- **3 Jahre** ab Schluss des Jahres, in dem Anspruch entstand **und** Anspruchsinhaber von Verletzung und Person des Verletzers Kenntnis hat (§§ 195, 199 BGB analog)
- **10 Jahre** kenntnisunabhängige Höchstfrist
- **Restschadensersatzanspruch** bis 30 Jahre über Bereicherungsrecht (§ 852 BGB analog, BGH, Urt. v. 26.03.2019 – X ZR 109/16, BGHZ 221, 342 = GRUR 2019, 496 – „Spannungsversorgungsvorrichtung", [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=26.03.2019&Aktenzeichen=X%20ZR%20109/16))
- **Dauerverletzung**: jede einzelne Verletzungshandlung lässt eigene Verjährungsfrist laufen

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute

- [§ 9 PatG](https://www.gesetze-im-internet.de/patg/__9.html) (Wirkungen — unmittelbar)
- [§ 10 PatG](https://www.gesetze-im-internet.de/patg/__10.html) (mittelbare Benutzung)
- [§ 14 PatG](https://www.gesetze-im-internet.de/patg/__14.html) (Schutzbereich)
- [§ 139 PatG](https://www.gesetze-im-internet.de/patg/__139.html) (Unterlassung, Schadensersatz)
- [§ 140a PatG](https://www.gesetze-im-internet.de/patg/__140a.html) (Vernichtung, Rückruf)
- [§ 140b PatG](https://www.gesetze-im-internet.de/patg/__140b.html) (Auskunft)
- [§ 140c PatG](https://www.gesetze-im-internet.de/patg/__140c.html) (Besichtigung)
- [§ 141 PatG](https://www.gesetze-im-internet.de/patg/__141.html) (Verjährung)
- [§ 143 PatG](https://www.gesetze-im-internet.de/patg/__143.html), [§ 145 PatG](https://www.gesetze-im-internet.de/patg/__145.html) (Patentstreitsachen)
- [Art. 64 EPÜ](https://www.epo.org/de/legal/epc/2020/a64.html) (Wirkungen EP); [Art. 69 EPÜ + Auslegungsprotokoll](https://www.epo.org/de/legal/epc/2020/a69.html)
- UPC-Übereinkommen, Art. 32 ff. (Zuständigkeit), Art. 83 (Übergangszeit / Opt-out)

### Kommentare

- Scharen, in: Benkard, PatG, 12. Aufl. 2023, § 14 Rn. 1 ff., § 139 Rn. 1 ff.
- Kühnen, Handbuch der Patentverletzung, 16. Aufl. 2024, Kap. A–E (Düsseldorfer Praxis)
- Voß, in: Schulte, PatG, 11. Aufl. 2022, § 139 Rn. 1 ff.
- Rinken, in: Mes, PatG, 5. Aufl. 2020, § 139 Rn. 1 ff.

### Rechtsprechung

1. BGH, [„Schneidmesser I", X ZR 168/00](https://lexetius.com/2002,244) — Äquivalenz-Trias Gleichwirkung
2. BGH, [„Schneidmesser II", X ZR 135/01](https://lexetius.com/2002,243) — Auffindbarkeit
3. BGH, „Schneidmesser III" `[unverifiziert – prüfen in juris/epo.org]` — Gleichwertigkeit am Patentanspruch orientiert
4. BGH, [„Okklusionsvorrichtung", X ZR 16/09](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=10.05.2011&Aktenzeichen=X+ZR+16/09) — Auswahlentscheidung des Anmelders
5. BGH, [„Diglycidverbindung", X ZR 69/10](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=13.09.2011&Aktenzeichen=X+ZR+69/10) — Auslegungsmethodik
6. BGH, Urt. v. 26.03.2019 – X ZR 109/16, BGHZ 221, 342 = GRUR 2019, 496 – „Spannungsversorgungsvorrichtung" — Restschadensersatz § 852 BGB analog, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=26.03.2019&Aktenzeichen=X%20ZR%20109/16)
7. EuGH, Urt. v. 16.07.2015 – [C-170/13, Huawei/ZTE](https://curia.europa.eu/juris/document/document.jsf?docid=165911&doclang=DE) — FRAND
8. OLG Düsseldorf-Serie zur Auskunfts- und Besichtigungspraxis `[unverifiziert – prüfen in juris/epo.org]`

## Ausgabeformat

```
KLAGESCHRIFT (Entwurf) — Patentverletzung
LG <…>, Patentstreitkammer  /  UPC <Lokalkammer/Zentralkammer>

Klägerin:    <…>
Beklagte:    <…>
Aktenzeichen Patent: <DE / EP / EP(UE)-Nr.>

A. Klageanträge
   1. Unterlassung (§ 139 I PatG)
   2. Auskunft (§ 140b PatG)
   3. Schadensersatz dem Grunde nach (§ 139 II PatG) — Wahl der
      Berechnungsmethode nach Auskunft
   4. Vernichtung (§ 140a I PatG)
   5. Rückruf (§ 140a III PatG)
   6. ggf. Urteilsveröffentlichung (§ 140e PatG)

B. Tatbestand
   I.   Parteien
   II.  Klagepatent (Rechtsstand, Veröffentlichung, Erteilung,
        Einspruchsstatus, ggf. Nichtigkeitsverfahren)
   III. Angegriffene Ausführungsform (technische Beschreibung)
   IV.  Verletzungshandlungen (erste Kenntnis, Zeitraum)

C. Rechtliche Würdigung
   I.   Schutzrechtsbestand
   II.  Schutzbereich § 14 PatG
        Merkmalsgliederung Hauptanspruch
        M1 …
        M2 …
        M3 …
   III. Verletzungstatbestand
        1. Wortlautverletzung § 9 PatG
           Subsumtion M1 — M2 — M3 — …
        2. Hilfsweise: äquivalente Verletzung
           (Gleichwirkung — Auffindbarkeit — Gleichwertigkeit)
        3. Ggf. mittelbare Verletzung § 10 PatG
   IV.  Anspruchskatalog § 139 ff. PatG
        – Unterlassung (verschuldensunabhängig)
        – Schadensersatz § 139 II
          • dreifache Berechnung (entgangener Gewinn /
            Verletzergewinn / Lizenzanalogie)
          • Wahl nach Auskunft
        – Auskunft § 140b
        – Vernichtung / Rückruf § 140a
   V.   Verjährung § 141 PatG — drei-Jahres-Frist (gewahrt) /
        Höchstfrist / Restschadensersatzanspruch
   VI.  Forumwahl
        – LG <…> Patentstreitkammer (§§ 143–145 PatG)
        – ggf. UPC: Opt-out-Status geprüft
   VII. Bei SEPs: FRAND-Compliance

D. Beweismittel
   – Patentschrift, Registerauszug
   – angegriffene Ausführungsform (Produktfotos, Datenblätter)
   – Zeugen, Sachverständigengutachten

E. Risiken / offene Punkte
   🟢 / 🟡 / 🔴 mit Begründung
   – Nichtigkeitsangriff erwartbar?
   – Aussetzungsantrag § 148 ZPO?
   – Streitwertfestsetzung

F. Quellenverzeichnis
```

## Beispiele

**Szenario:** Klägerin hält ein erteiltes EP-Bündelpatent ohne UPC-Opt-out, validiert in DE. Beklagte vertreibt seit 14 Monaten ein wortlautidentisches Konkurrenzprodukt. Frage: Klage am LG Düsseldorf oder UPC?

Kurzantwort (🟡): Wortlautverletzung erscheint unproblematisch nachweisbar. **Forumwahl** strategisch: UPC bietet pan-europäischen Unterlassungstitel in einem Verfahren, aber zentrales Nichtigkeits-Risiko; LG Düsseldorf liefert nur DE-Schutz, aber bewährte Verletzungsdoktrin und Trennung Verletzung / Nichtigkeit (Aussetzungspraxis § 148 ZPO). **Verjährung § 141 PatG** ist für 14 Monate gewahrt; **Auskunft § 140b PatG** über Stufenklage § 254 ZPO, Wahl der Schadensberechnung erst nach Auskunft. Bevor Klageerhebung: **Opt-out-Status** im UPC-Register prüfen.

## Risiken / typische Fehler

- **Merkmalsgliederung fehlt oder unsauber** — Subsumtion bricht zusammen.
- **Äquivalenz pauschal** ohne BGH-Trias durchgeprüft — Klage scheitert in Berufung.
- **Auswahlentscheidung während der Erteilung übersehen** (Anmelder hat Variante gestrichen) — Äquivalenzkorridor versperrt.
- **Verjährung § 141 PatG übersehen** — bei Dauerverletzung Tranchen-Verjährung beachten; Restschadensersatzanspruch nutzen.
- **UPC-Opt-out-Status nicht geprüft** — Klage am falschen Forum, Zurückweisung der internationalen Zuständigkeit.
- **Bei SEPs FRAND-Anforderungen nicht eingehalten** — Unterlassungsanspruch entfällt nach EuGH [„Huawei/ZTE", C-170/13](https://curia.europa.eu/juris/document/document.jsf?docid=165911&doclang=DE).
- **Sachkundigenvertretung § 143 III PatG nicht organisiert** — Patentanwalt parallel zum Rechtsanwalt erforderlich.
- **Wahl der Schadensberechnung zu früh festgelegt** — Wahlrecht bis zum Schluss der mündlichen Verhandlung ausnutzen.
