---
name: recht-erbe-verfahren
title: /recht erbe-verfahren — Verlassenschaftsverfahren und erbrechtliche Rechtsmittel
description: Austrian probate and inheritance procedure — Verlassenschaftsverfahren (AußStrG §§143ff), Erbantrittserklärung, Erbrechtsklage, Pflichtteilsklage, Testamentsanfechtung, EU-ErbVO cross-border estates, Erbschaftsmediation, and procedural templates for inheritance disputes.
author: MoMarcode1
author_url: https://github.com/MoMarcode1/austrian-legal-claude/tree/main/skills/recht-erbe-verfahren
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: at
practice: trusts-and-estates
language: de
---

# /recht erbe-verfahren — Verlassenschaftsverfahren und erbrechtliche Rechtsmittel

When the user has questions about probate procedure, needs to file an Erbantrittserklärung, wants to challenge a will, claim a Pflichtteil, or has any procedural inheritance question, follow these steps.

---

## Step 1: Read the Facts / Documents

Read everything the user has provided. You need:

1. **What happened?** — Todesfall? Verlassenschaftsabhandlung laeuft? Testament aufgetaucht? Pflichtteil verweigert? Streit unter Erben?
2. **When did the Erblasser die?** — Todesdatum bestimmt den Beginn des Verlassenschaftsverfahrens
3. **Which Bezirksgericht / Notar?** — Zustaendiges BG am letzten Wohnsitz des Erblassers (§105 JN). Gerichtskommissaer (Notar) wurde bereits bestellt?
4. **Which stage of the procedure?** — Todesfallaufnahme? Inventarisierung? Erbantrittserklärung? Einantwortung? Bereits rechtskraeftig?
5. **Any disputes?** — Mehrere Testamente? Streit um Gueltigkeit? Pflichtteilsansprueche? Erbunwuerdigkeit behauptet?
6. **International element?** — Erblasser war Auslaender? Vermoegen im Ausland? Gewoehnlicher Aufenthalt ausserhalb Oesterreichs?

If critical facts are missing, ask. Be specific:
> "Bei welchem Bezirksgericht laeuft das Verlassenschaftsverfahren? Wurde bereits ein Gerichtskommissaer (Notar) bestellt? Das ist wichtig fuer die Zustaendigkeit und den Verfahrensstand."

---

## Step 2: RIS Verification

Before proceeding with analysis, follow the **RIS Verification Protocol** (`references/ris-protocol.md`):
1. Check RIS MCP availability
2. For every § you cite in this analysis, verify current wording via RIS
3. For case law references (OGH), retrieve via RIS Justiz
4. Record verification status for the Quellenstatus block
5. If RIS is unavailable, follow the fallback ladder and flag all affected citations

Search RIS Justiz for relevant OGH-Entscheidungen on disputed inheritance procedure questions. Present using format from `references/ogh-case-presentation.md`.

---

## Step 3: Classify the Procedural Situation

Determine which procedural path applies. Check each option:

### A: Verlassenschaftsverfahren — Regulaerer Ablauf (§§143ff AußStrG)

**Ueberblick ueber das Verlassenschaftsverfahren:**

Das Verlassenschaftsverfahren ist ein **Ausserstreitverfahren** (kein Zivilprozess). Es wird vom **Bezirksgericht** am letzten Wohnsitz des Erblassers gefuehrt (§105 JN) und durch einen **Gerichtskommissaer** (Notar) durchgefuehrt (§1 GKG).

**Ablauf Schritt fuer Schritt:**

| Phase | Was passiert | §§ | Zeitrahmen |
|-------|-------------|-----|-----------|
| 1. Todesfall | Sterbeurkunde wird ausgestellt, Standesamt verstaendigt Gericht | §143 AußStrG | Tage |
| 2. Todesfallaufnahme | Gerichtskommissaer (Notar) erhebt: Vermoegen, Erben, Testamente, Familie | §145 AußStrG | 2-4 Wochen |
| 3. Testamentskundmachung | Vorhandene Testamente werden eroeffnet und kundgemacht | §§149-150 AußStrG | Bei Todesfallaufnahme |
| 4. Inventarisierung | Erfassung aller Aktiva und Passiva, Bewertung | §§165-168 AußStrG | 4-12 Wochen |
| 5. Erbantrittserklärung | Erben geben bedingte oder unbedingte Erbantrittserklärung ab | §§157-159 AußStrG, §§800-801 ABGB | Keine Frist, aber zügig |
| 6. Abhandlung | Gerichtskommissaer prueft Erbrecht, Quoten, Vermächtnis | §§160-164 AußStrG | Variabel |
| 7. Einantwortung | Gericht erlässt Einantwortungsbeschluss — Eigentum geht auf Erben über | §§177-178 AußStrG | Am Ende |
| 8. Grundbuch | Eigentumsumschreibung bei Immobilien auf Basis des Einantwortungsbeschlusses | §33 GBG | Nach Einantwortung |

**Besonderheiten:**
- **Ruhender Nachlass (hereditas iacens):** Zwischen Tod und Einantwortung ist die Verlassenschaft eine eigene Rechtspersoenlickeit (§546 ABGB). Sie kann klagen und verklagt werden.
- **Verlassenschaftskurator (§156 AußStrG):** Wird bestellt, wenn der Nachlass verwaltungsbeduerftig ist und kein Erbe handelt
- **Ueberlassung an Zahlungs statt (§154 AußStrG):** Bei geringfuegigem Nachlass (derzeit unter ca. €5.000) — verkuerztes Verfahren ohne Einantwortung

### B: Erbantrittserklärung (§§157-159 AußStrG, §§800-801 ABGB)

**Die Erbantrittserklärung ist die zentrale Willenserklärung des Erben.**

**Zwei Arten:**

| Art | Wirkung | Haftung | §§ |
|-----|---------|---------|-----|
| **Bedingte** Erbantrittserklärung (mit Vorbehalt der Inventarerrichtung) | Erbe haftet nur bis zum Wert des Nachlasses (pro viribus hereditatis) | Beschraenkt auf Nachlassaktiva | §802 ABGB |
| **Unbedingte** Erbantrittserklärung (ohne Vorbehalt) | Erbe haftet fuer ALLE Nachlassschulden, auch mit eigenem Vermoegen | Unbeschraenkt (cum viribus hereditatis) | §801 ABGB |

**EMPFEHLUNG: IMMER bedingte Erbantrittserklärung abgeben!**
- Es gibt keinen Nachteil der bedingten Erbantrittserklärung, wenn der Nachlass positiv ist
- Bei der unbedingten Erbantrittserklärung riskiert der Erbe, mit seinem Privatvermoegen fuer unbekannte Schulden des Erblassers zu haften
- Die bedingte Erbantrittserklärung erfordert die Errichtung eines Inventars (§166 AußStrG) — Kosten sind ueberschaubar

**Formvorschriften:**
- Muendlich zu Protokoll des Gerichtskommissaers oder schriftlich beim Gericht (§157 Abs 1 AußStrG)
- Muss den Erbrechtstitel angeben: gesetzliches Erbrecht, Testament (mit Datum), Erbvertrag (§157 Abs 1 AußStrG)
- **Keine Frist** fuer die Abgabe — aber das Gericht kann eine Frist setzen (§158 AußStrG)
- **Unwiderruflich** — einmal abgegeben, kann die Erbantrittserklärung nicht zurueckgenommen werden, ausser bei wesentlichem Irrtum

**Widerstreitende Erbantrittserklärungen (§161 AußStrG):**
- Wenn mehrere Personen Erbantrittserklärungen aufgrund verschiedener Titel abgeben (z.B. gesetzlicher Erbe vs. testamentarischer Erbe)
- Gerichtskommissaer kann nicht entscheiden → verweist auf den Rechtsweg (Erbrechtsklage, §161 Abs 1 AußStrG)

### C: Erbrechtsklage / Erbschaftsklage (§§823ff ABGB)

**When:** Streit darueber, WER erbt — z.B. Testament angefochten, gesetzliches Erbrecht streitig.

**Erbrechtsklage (§823 ABGB):**
- Klage auf Herausgabe der Erbschaft oder eines Erbteils
- Klaeger: wer ein besseres Erbrecht behauptet
- Beklagter: wer die Erbschaft besitzt (Erbschaftsbesitzer)
- **Zustaendigkeit:** Bezirksgericht (wenn Streitwert ≤€15.000) oder Landesgericht (wenn >€15.000), §49 JN
- **Verjährung:** 30 Jahre (§1478 ABGB) — unverjaehrbarer Kern fuer dingliche Herausgabeklagen
- **Beweislast:** Klaeger muss sein besseres Erbrecht beweisen

**Erbschaftsklage (§824 ABGB):**
- Richtet sich gegen den Erbschaftsbesitzer (Scheinerbgen)
- Verlangt wird die Herausgabe der Verlassenschaft
- Gutglaeubiger Erbschaftsbesitzer: haftet nur fuer noch vorhandene Bereicherung (§825 ABGB)
- Boesgläubiger Erbschaftsbesitzer: haftet fuer vollen Schaden (§826 ABGB)

### D: Pflichtteilsklage

**When:** Pflichtteilsberechtigter hat seinen Pflichtteil nicht oder nicht vollstaendig erhalten.

**Voraussetzungen:**
1. Klaegers Pflichtteilsberechtigung feststellen (§759 ABGB: Nachkommen, Ehegatte/EP)
2. Pflichtteil wurde durch letztwillige Verfuegung verkuerzt oder entzogen
3. Pflichtteil wurde im Verlassenschaftsverfahren nicht freiwillig erfuellt

**Berechnung des Pflichtteils:**
1. Reiner Nachlass ermitteln (Aktiva - Passiva)
2. Hinzurechnung pflichtteilsrelevanter Schenkungen (§§781-782 ABGB)
3. Gesetzlichen Erbteil berechnen (als gaebe es kein Testament)
4. Haelfte davon = Pflichtteil (§759 ABGB)
5. Abzug: was der Pflichtteilsberechtigte bereits erhalten hat (Vermaechtnis, Schenkung unter Anrechnung)

**Zustaendigkeit:**
- **Streitwert ≤€15.000:** Bezirksgericht (§49 Abs 1 JN)
- **Streitwert >€15.000:** Landesgericht (§49 Abs 1 JN)
- **Oertliche Zustaendigkeit:** Allgemeiner Gerichtsstand des Beklagten (§66 JN) ODER Verlassenschaftsgericht (§77 JN — Gerichtsstand des Erbrechts, solange Verlassenschaftsverfahren laeuft)

**Verjährung (§1487 ABGB):**
- **3 Jahre** ab Kenntnis des Pflichtteilsberechtigten von der Verletzung seines Pflichtteils UND vom Verpflichteten
- **Fristbeginn:** typischerweise ab Kundmachung des Testaments oder Einantwortung
- **Absolute Verjährung:** 30 Jahre ab Tod des Erblassers
- **Achtung bei Schenkungsanrechnung:** Die 3-Jahres-Frist beginnt gesondert fuer Schenkungsergaenzungsansprueche (ab Kenntnis der Schenkung)

**Anwaltspflicht:**
- Beim BG: **keine** Anwaltspflicht (§29 ZPO) — aber empfohlen
- Beim LG: **absolute Anwaltspflicht** (§27 ZPO)

### E: Testamentsanfechtung

**Gruende fuer die Anfechtung eines Testaments:**

| Anfechtungsgrund | §§ ABGB | Wirkung | Beweislast |
|-----------------|---------|---------|------------|
| **Formfehler** (z.B. fehlende Zeugen bei fremdhaendigem Testament) | §§578-582 ABGB | Nichtigkeit | Anfechtender |
| **Testierunfaehigkeit** (Geisteskrankheit, Demenz) | §§566-568 ABGB | Nichtigkeit | Anfechtender (Sachverstaendigengutachten!) |
| **Irrtum** (Motivirrtum, Erklaerungsirrtum) | §572 ABGB | Aufhebung der verfuegten Zuwendung | Anfechtender |
| **Zwang / Drohung** | §573 ABGB | Nichtigkeit | Anfechtender |
| **Arglistige Taeuschung** | §573 ABGB | Nichtigkeit | Anfechtender |
| **Faelschung** | §543 ABGB iVm StGB | Nichtigkeit + Erbunwuerdigkeit | Anfechtender |

**Haeufigste Formfehler:**
1. Fremdhändiges Testament: nicht alle 3 Zeugen waren **gleichzeitig** anwesend (§579 ABGB)
2. Fremdhändiges Testament: Nuncupatio-Klausel fehlt ("Das ist mein letzter Wille") (§579 ABGB)
3. Eigenhändiges Testament: nicht der **gesamte** Text eigenhaendig geschrieben (§578 ABGB)
4. Zeuge ist selbst bedacht oder naher Angehoeriger eines Bedachten (§588 ABGB) — Zuwendung an den Zeugen ist nichtig, nicht das ganze Testament

**Testierunfaehigkeit (§567 ABGB):**
- Haeufigster Fall: Demenz des Erblassers zum Zeitpunkt der Testamentserrichtung
- Beweis: aerztliche Befunde, Zeugenaussagen, Sachverstaendigengutachten (retrospektiv)
- **Beweislast liegt beim Anfechtenden** — es gilt die **Vermutung der Testierfaehigkeit**
- Tipp: Pflegedokumentation, Krankenhausberichte, Medikation als Beweismittel sichern

**Verfahren:**
- Anfechtung im Rahmen des Verlassenschaftsverfahrens oder mittels gesonderter Klage (Erbrechtsklage)
- Bei Verweisung auf den Rechtsweg: Klage beim zustaendigen BG oder LG

### F: Erbschaftsmediation

**Alternative zum Rechtsstreit:**

- Erbschaftsstreitigkeiten eignen sich besonders fuer Mediation, da familiäre Beziehungen betroffen sind
- **Eingetragene Mediatoren** in Oesterreich: Liste beim BMJ (www.mediatorenliste.justiz.gv.at)
- **Kosten:** wesentlich geringer als Gerichtsverfahren (ca. €150-300/Stunde, geteilt)
- **Vorteile:** schneller, vertraulich, erhalt familiäre Beziehungen, flexible Loesungen moeglich
- **Ergebnis:** Mediationsvereinbarung — bei Bedarf notariell beurkunden fuer Vollstreckbarkeit
- **Verjährungshemmung:** Einleitung einer Mediation hemmt die Verjährung (§1494 Abs 2 ABGB)

**Empfehlung:** Mediation vor allem bei:
- Streit unter Geschwistern ueber Nachlassverteilung
- Pflichtteilsstreitigkeiten, wenn Einigung ueber Stundung/Ratenzahlung moeglich
- Unklarheiten ueber Erblasserwillen bei formlosen Aeusserungen
- Betriebsnachfolge mit mehreren Erben

### G: Europaeische Erbrechtsverordnung — Verfahren bei internationalem Bezug (EU-ErbVO)

**Zustaendigkeit (Art 4 EU-ErbVO):**
- Grundsatz: Gerichte des Mitgliedstaats, in dem der Erblasser zum Zeitpunkt seines Todes seinen **gewoehnlichen Aufenthalt** hatte
- Gewoehnlicher Aufenthalt ≠ Staatsbuergerschaft ≠ Meldeadresse
- Subsidiäre Zustaendigkeit (Art 10): wenn gewoehnlicher Aufenthalt in Drittstaat, aber Vermoegen in EU

**Europaeisches Nachlasszeugnis (Art 62ff EU-ErbVO):**
- Dient dem Nachweis der Erbenstellung in anderen EU-Mitgliedstaaten
- Wird vom Verlassenschaftsgericht ausgestellt
- Wirkung: Wird in allen EU-Mitgliedstaaten (ausser Dänemark und Irland) anerkannt
- Ersetzt NICHT die nationale Einantwortung — ist ein zusaetzliches Dokument

**Anwendbares Recht (Art 21 EU-ErbVO):**
- Recht des Staates des gewoehnlichen Aufenthalts des Erblassers
- Rechtswahl (Art 22): Erblasser kann das Recht seiner Staatsangehörigkeit waehlen

---

## Step 4: Check ALL Deadlines (CRITICAL)

Calculate ALL relevant deadlines. Fuer jede:

| Frist | Grundlage | Beginn | Ablauf | Status |
|-------|-----------|--------|--------|--------|
| Pflichtteilsklage | §1487 ABGB | Kenntnis der Verletzung | +3 Jahre | 🟢/🟡/🔴 |
| Pflichtteilsklage (absolut) | §1478 ABGB | Tod des Erblassers | +30 Jahre | 🟢/🟡/🔴 |
| Erbrechtsklage | §1478 ABGB | Tod des Erblassers | +30 Jahre | 🟢/🟡/🔴 |
| Rekurs gegen Einantwortung | §46 AußStrG | Zustellung des Beschlusses | +14 Tage | 🟢/🟡/🔴 |
| Schenkungsmeldepflicht | §121a BAO | Ausfuehrung der Schenkung | +3 Monate | 🟢/🟡/🔴 |
| Stundungsantrag Pflichtteil | §766 ABGB | Im Verlassenschaftsverfahren | Vor Einantwortung | 🟢/🟡/🔴 |

**Fristberechnung (§§125-126 ZPO fuer Streitverfahren, §23 AußStrG fuer Ausserstreitverfahren):**
- Monatsfrist: Ende am gleichen Tag des Folgemonats
- Fällt Ende auf Sa/So/Feiertag → naechster Werktag
- Postaufgabe am letzten Tag genuegt

**Verjährungshemmung und -unterbrechung:**
- Einleitung einer Mediation hemmt die Verjährung (§1494 Abs 2 ABGB)
- Klageerhebung unterbricht die Verjährung (§1497 ABGB)
- Anerkenntnis durch den Schuldner unterbricht die Verjährung (§1497 ABGB)

---

## Step 5: Draft the Appropriate Filing

Based on the classification, draft the relevant Schriftsatz. Always in proper Austrian legal format.

### Bedingte Erbantrittserklärung — Template:

```
An das
Bezirksgericht [Ort]
Abt. [x]

GZ: [Geschaeftszahl des Verlassenschaftsverfahrens, z.B. xA xxx/xxm]

In der Verlassenschaftssache nach [Name des Erblassers], verstorben am [Datum],
zuletzt wohnhaft in [Adresse]

gibt der/die Unterfertigte

[Name, Geburtsdatum, Adresse]

hiermit die

BEDINGTE ERBANTRITTSERKLÄRUNG

unter Vorbehalt der Inventarerrichtung (§802 ABGB) ab.

I. ERBRECHTSTITEL

Der/Die Unterfertigte ist erbberechtigt aufgrund
[VARIANTE 1:] des Gesetzes als [Kind / Ehegatte / etc.] des Erblassers
(gesetzliche Erbfolge, §§730ff ABGB).

[VARIANTE 2:] des eigenhändigen Testaments vom [Datum], in dem der/die
Unterfertigte als [Alleinerbe / Erbe zu x/y] eingesetzt wurde.

[VARIANTE 3:] des Erbvertrages vom [Datum], Notariatsakt des Notars
[Name], GZ [Geschaeftszahl].

II. ERBQUOTE

Die Erbantrittserklärung wird fuer den gesamten Nachlass [bzw. fuer einen
Anteil von x/y des Nachlasses] abgegeben.

III. INVENTARERRICHTUNG

Es wird die Errichtung eines Inventars gemaess §§165ff AußStrG beantragt,
um die Haftung auf den Wert der Nachlassaktiva zu beschraenken (§802 ABGB).

[Ort], am [Datum]

[Unterschrift]
```

### Pflichtteilsklage — Template:

```
An das
[Bezirksgericht / Landesgericht] [Ort]

KLAGE
auf Zahlung des Pflichtteils

Klaeger/in:    [Name, Adresse, Geburtsdatum]
               vertreten durch: [RA Name, Adresse, falls LG]

Beklagte/r:    [Name (Erbe), Adresse]

Streitwert:    €[Betrag]

I. SACHVERHALT

1. Der Erblasser [Name] verstarb am [Datum] in [Ort]. Das Verlassenschafts-
   verfahren wurde/wird beim BG [Ort], GZ [Geschaeftszahl], gefuehrt.

2. Der/Die Kläger/in ist [Kind / Ehegatte / eingetragener Partner] des
   Erblassers und daher pflichtteilsberechtigt gemaess §759 ABGB.

3. Der Erblasser hinterliess ein Testament vom [Datum], in dem er/sie
   den/die Beklagte/n als [Alleinerben / Erben] einsetzte. Der/Die
   Klaeger/in wurde im Testament [nicht bedacht / nur mit einem
   Vermaechtnis in Hoehe von €x bedacht].

4. Der reine Nachlass betraegt nach dem Inventar €[Betrag].
   [Hinzuzurechnende Schenkungen gemaess §§781ff ABGB: €[Betrag].]
   Die Bemessungsgrundlage fuer den Pflichtteil betraegt somit €[Betrag].

5. Der gesetzliche Erbteil des/der Klaeger/in betraegt [Bruch], somit
   belaeuft sich der Pflichtteil (Haelfte des gesetzlichen Erbteils,
   §759 ABGB) auf €[Betrag].

6. [Falls teilweise erfuellt:] Abzueglich der bereits erhaltenen Zuwendung
   von €[x] verbleibt ein offener Pflichtteilsanspruch von €[Betrag].

7. Der/Die Beklagte wurde mit Schreiben vom [Datum] zur Zahlung aufgefordert.
   Eine Zahlung ist bis dato nicht erfolgt.

II. RECHTLICHE BEGRUENDUNG

Der Pflichtteil ist ein schuldrechtlicher Anspruch auf Geld (§761 ABGB).
Der/Die Klaeger/in als [Kind / Ehegatte] des Erblassers ist gemaess §759
ABGB pflichtteilsberechtigt. Der Pflichtteil betraegt die Haelfte des
gesetzlichen Erbteils.

[Bei Schenkungsanrechnung:]
Gemaess §781 ABGB sind Schenkungen an Pflichtteilsberechtigte der
Verlassenschaft zeitlich unbegrenzt hinzuzurechnen. Die Schenkung
an [Name/Beklagten] in Hoehe von €[Betrag] vom [Datum] ist daher
in die Pflichtteilsbemessungsgrundlage einzubeziehen.

[Bei Schenkungen an Dritte:]
Gemaess §782 ABGB sind Schenkungen an Dritte, die innerhalb von 2 Jahren
vor dem Tod des Erblassers erfolgten, hinzuzurechnen. Die Schenkung
vom [Datum] an [Name] faellt in diesen Zeitraum.

III. BEWEIS

1. Verlassenschaftsakt BG [Ort], GZ [Geschaeftszahl]
2. Testament vom [Datum]
3. Inventar der Verlassenschaft
4. Schreiben vom [Datum] (Zahlungsaufforderung)
5. [Schenkungsvertrag vom [Datum]]
6. [Sachverstaendigengutachten zur Bewertung von ...]
7. PV des/der Klaeger/in und des/der Beklagten

IV. ANTRAG

Der/Die Klaeger/in stellt den Antrag, das Gericht moege

1. den/die Beklagte/n schuldig erkennen, dem/der Klaeger/in den Betrag
   von €[Pflichtteilsbetrag] samt 4% Zinsen seit [Todesdatum des
   Erblassers] (§1000 Abs 1 ABGB) binnen 14 Tagen bei sonstiger
   Exekution zu bezahlen;

2. den/die Beklagte/n zum Ersatz der Verfahrenskosten verpflichten.

[Ort], am [Datum]

[Unterschrift (des RA bei LG-Verfahren)]
```

### Rekurs gegen Einantwortungsbeschluss — Template:

```
An das
Bezirksgericht [Ort]
Abt. [x]

GZ: [Geschaeftszahl]

REKURS

gegen den Einantwortungsbeschluss vom [Datum], zugestellt am [Datum]

Rekurswerber/in: [Name, Adresse]

I. ANFECHTUNGSERKLAERUNG

Der Einantwortungsbeschluss vom [Datum] wird [zur Gaenze / hinsichtlich ...]
angefochten.

II. REKURSGRUENDE

[Ausfuehren: Welche Fehler hat das Gericht gemacht?
- Falscher Erbrechtstitel angenommen?
- Erbquoten falsch berechnet?
- Widerstreitende Erbantrittserklärung nicht beruecksichtigt?
- Formfehler des Testaments uebersehen?]

III. ANTRAG

Der/Die Rekurswerber/in beantragt, das Rekursgericht moege

1. den angefochtenen Beschluss aufheben und die Rechtssache an das
   Erstgericht zurueckverweisen;

   [IN EVENTU:]

2. den angefochtenen Beschluss dahingehend abaendern, dass
   [konkretes Begehren].

[Ort], am [Datum]

[Unterschrift]
```

---

## Step 6: Present with Timeline and Next Steps

```markdown
# Verlassenschaftsverfahren — Analyse und Handlungsempfehlung

**Erblasser:** [Name], verstorben am [Datum]
**Zustaendiges Gericht:** BG [Ort], GZ [Geschaeftszahl]
**Gerichtskommissaer:** Notar [Name]
**Verfahrensstand:** [Todesfallaufnahme / Inventar / Erbantrittserklärung / Einantwortung]
**Verfahrensart:** [Regulaer / Pflichtteilsklage / Testamentsanfechtung / Erbrechtsklage]

## Fristenübersicht
| Frist | Ablauf | Verbleibend | Status |
|-------|--------|-------------|--------|
| Pflichtteilsklage (§1487 ABGB) | [Datum] | [x] Jahre/Monate | 🟢/🟡/🔴 |
| Rekurs gegen Beschluss (§46 AußStrG) | [Datum] | [x] Tage | 🟢/🟡/🔴 |
| [weitere Fristen] | [Datum] | [x] | 🟢/🟡/🔴 |

## Sachverhalt
[Zusammenfassung: Was ist passiert, was ist strittig]

## Rechtliche Beurteilung
[Analyse mit §§-Zitaten]
- Erbfolge: [gesetzlich/testamentarisch, welche §§]
- Pflichtteilsansprueche: [Berechnung]
- Formgueltigkeit des Testaments: [Pruefung]
- Relevante OGH-Judikatur

## Empfohlene Vorgehensweise

### Sofort-Massnahmen
1. [z.B. "Bedingte Erbantrittserklärung abgeben"]
2. [z.B. "Inventarerrichtung beantragen"]
3. [z.B. "Pflichtteilsanspruch schriftlich geltend machen"]

### Verfahrensablauf (Timeline)
| Schritt | Frist | Aktion |
|---------|-------|--------|
| 1. Erbantrittserklärung | Umgehend | Beim Gerichtskommissaer |
| 2. Inventarerrichtung | §166 AußStrG | Beantragen |
| 3. Pflichtteilsberechnung | Nach Inventar | Pflichtteil beziffern |
| 4. Einantwortung | Nach Abhandlung | Beschluss des BG |
| 5. ggf. Pflichtteilsklage | 3 Jahre (§1487) | Bei Nichtzahlung |

## Erbantrittserklärung — Empfehlung
| Art | Empfehlung | Begruendung |
|-----|-----------|-------------|
| Bedingt (§802 ABGB) | **EMPFOHLEN** | Haftungsbeschraenkung auf Nachlassvermoegen |
| Unbedingt (§801 ABGB) | NUR wenn Nachlass klar positiv und uebersichtlich | Vollhaftung auch mit eigenem Vermoegen |

## Kosten
| Position | Geschaetzte Kosten | Grundlage |
|----------|-------------------|-----------|
| Gerichtskommissaer (Notar) | €[x] | GKTG |
| Inventarerrichtung | €[x] | GKTG |
| Grunderwerbsteuer (Immobilie) | €[x] | §7 GrEStG |
| Grundbucheintragung | €[x] | §26 GGG |
| RA-Kosten (falls Klage) | €[x] | RATG |
| Gerichtsgebuehr (falls Klage) | €[x] | GGG |

## Erfolgsaussichten (falls Streitverfahren)
| Szenario | Wahrscheinlichkeit | Konsequenz |
|----------|-------------------|------------|
| [z.B. Pflichtteil vollstaendig zugesprochen] | [x]% | €[x] |
| [z.B. Teilweiser Erfolg] | [x]% | €[x] |
| [z.B. Klage abgewiesen] | [x]% | Kosten: €[x] |

## Entwurf des Schriftsatzes
[Hier den konkreten Entwurf einfuegen]

## Risiken
- [z.B. "Verjährung der Pflichtteilsklage droht am [Datum]"]
- [z.B. "Testamentsanfechtung: Beweis der Testierunfaehigkeit ist schwierig"]
- [z.B. "Unbedingte Erbantrittserklärung: unbekannte Schulden moeglich"]

## Alternative: Mediation
[Falls anwendbar: Mediation als Alternative zum Rechtsstreit empfehlen, Kosten-/Zeitersparnis aufzeigen]

## Naechste Schritte
- [ ] [Konkreter erster Schritt mit Datum]
- [ ] [Zweiter Schritt]
- [ ] [Rechtsanwalt/Notar konsultieren fuer ...]

## Quellenstatus
| Kategorie | Status | Details |
|-----------|--------|---------|
| RIS MCP | 🟢 Verfuegbar / 🔴 Nicht verfuegbar | [connection status] |
| Gesetze | RIS_VERIFIED / OFFICIAL_WEB_VERIFIED / UNVERIFIED | [n] Normen geprueft |
| Judikatur | RIS_VERIFIED / OFFICIAL_WEB_VERIFIED / UNVERIFIED | [n] Entscheidungen |
| Pruefdatum | [YYYY-MM-DD] | |

---
⚠️ **Keine Rechtsberatung.** Diese Analyse dient der verfahrensrechtlichen Ersteinschätzung und ersetzt nicht die Beratung durch einen Rechtsanwalt oder Notar. Insbesondere bei Pflichtteilsklagen, Testamentsanfechtung und Erbrechtsstreitigkeiten wird professionelle Rechtsvertretung dringend empfohlen. Aktuelle Gesetze auf [ris.bka.gv.at](https://www.ris.bka.gv.at) pruefen.
```

---

## Critical Rules

1. **IMMER bedingte Erbantrittserklärung empfehlen** — Eine unbedingte Erbantrittserklärung fuehrt zur unbeschraenkten Haftung mit dem Privatvermoegen. Es gibt keinen Vorteil der unbedingten Erbantrittserklärung, wenn der Nachlass positiv ist. Immer zur bedingten raten (§802 ABGB).
2. **Pflichtteilsverjaehrung: 3 Jahre (§1487 ABGB)** — Diese Frist MUSS bei jeder Pflichtteilsfrage prominent angezeigt werden. Versaeumnis ist endgueltig.
3. **Pflichtteil = Geldanspruch** — Der Pflichtteil ist ein reiner Geldanspruch (§761 ABGB), KEIN Anspruch auf Sachen oder Nachlassgegenstaende. Der Pflichtteilsberechtigte wird nicht Miteigentuemer.
4. **Verlassenschaftsverfahren = Ausserstreitverfahren** — AußStrG, NICHT ZPO. Andere Verfahrensregeln, anderer Instanzenzug. Erbrechts- und Pflichtteilsklagen sind hingegen streitige Verfahren (ZPO).
5. **Zustaendigkeit exakt angeben** — BG vs. LG haengt vom Streitwert ab (§49 JN: Grenze €15.000). Verlassenschaftsverfahren ist IMMER beim BG (§105 JN).
6. **Reformatio in peius im Ausserstreitverfahren** — Das Rekursgericht kann im Ausserstreitverfahren auch zum Nachteil des Rekurswerbers entscheiden. Warnung erforderlich.
7. **Rekursfrist im AußStrG: 14 Tage** — Nicht 4 Wochen wie im streitigen Verfahren. §46 Abs 1 AußStrG.
8. **Testamentsanfechtung: Beweislast beim Anfechtenden** — Es gilt die Vermutung der Gueltigkeit und Testierfaehigkeit. Der Anfechtende muss Formfehler oder Testierunfaehigkeit BEWEISEN.
9. **EU-ErbVO bei internationalem Bezug pruefen** — Gewoehnlicher Aufenthalt bestimmt das anwendbare Recht (Art 21 EU-ErbVO). Rechtswahl moeglich (Art 22). Europaeisches Nachlasszeugnis fuer grenzueberschreitende Nachlaesse.
10. **Mediation aktiv empfehlen** — Bei familiären Erbstreitigkeiten ist Mediation oft die bessere Loesung. Kostenguenstiger, schneller, beziehungserhaltend. Verjährungshemmung bei Mediation (§1494 Abs 2 ABGB).
11. **§§ immer mit Gesetzesname** — §157 AußStrG, §759 ABGB, §1487 ABGB, nicht nur "§157" oder "§759".
12. **Use RIS if connected** — Verify procedural provisions, especially AußStrG and ABGB Erbrecht provisions.
13. **Match user's language** — German in → German out. English in → English out. Gesetze immer in deutscher Form.
