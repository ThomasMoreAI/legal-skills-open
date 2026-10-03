---
name: recht-steuer-verfahren-momarcode1
title: /recht steuer-verfahren — Abgabenverfahren und Rechtsmittel
description: Austrian tax procedure — filing appeals (Beschwerde) against tax assessments, BAO deadlines, Vorlageantrag to BFG, self-disclosure (Selbstanzeige §29 FinStrG), payment deferrals (Stundung/Ratenzahlung), and Bundesfinanzgericht proceedings.
author: MoMarcode1
author_url: https://github.com/MoMarcode1/austrian-legal-claude/tree/main/skills/recht-steuer-verfahren
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: at
practice: tax
language: de
sources:
- title: Ogh case presentation
  path: references/ogh-case-presentation.md
- title: Ris protocol
  path: references/ris-protocol.md
---

# /recht steuer-verfahren — Abgabenverfahren und Rechtsmittel

When the user has received a tax assessment (Bescheid) they want to challenge, needs to file a Selbstanzeige, wants to defer payment, or has any procedural tax question, follow these steps.

---

## Step 1: Read the Facts / Bescheid

Read everything the user has provided. You need:

1. **What document was received?** — Einkommensteuerbescheid, Umsatzsteuerbescheid, Haftungsbescheid, Feststellungsbescheid, Prüfungsbericht?
2. **When was it received (zugestellt)?** — The exact date of Zustellung starts the Beschwerdefrist. If unclear, ask immediately:
   > "Wann wurde Ihnen der Bescheid zugestellt? Das genaue Datum ist entscheidend — die Beschwerdefrist beträgt nur 1 Monat ab Zustellung."
3. **What is wrong with the Bescheid?** — Factual error? Legal error? Missing deductions? Wrong Einkunftsart?
4. **Which Finanzamt issued it?** — Relevant for Zuständigkeit
5. **Is there a Steuerberater involved?** — Affects Zustellvollmacht and Fristen
6. **Financial situation?** — Relevant for Stundung/Ratenzahlung, Aussetzung der Einhebung

If the user mentions unpaid taxes, undeclared income, or fears of Finanzstrafverfahren, immediately assess whether a Selbstanzeige (§29 FinStrG) is relevant — this is time-critical.

---

## Step 2: RIS Verification

Before proceeding with analysis, follow the **RIS Verification Protocol** (`references/ris-protocol.md`):
1. Check RIS MCP availability
2. For every § you cite in this analysis, verify current wording via RIS
3. For case law references (VwGH, BFG), retrieve via RIS Justiz
4. Record verification status for the Quellenstatus block
5. If RIS is unavailable, follow the fallback ladder and flag all affected citations

Search RIS Justiz for relevant BFG-Erkenntnisse and VwGH-Entscheidungen to the specific procedural question. Present using format from `references/ogh-case-presentation.md` (adapted for VwGH/BFG).

---

## Step 3: Classify the Procedural Situation

Determine which procedural path applies. Check each option:

### A: Beschwerde gegen Bescheid (§243 BAO)

**When:** User disagrees with a Bescheid from the Finanzamt.

**Requirements:**
- **Frist:** 1 Monat ab Zustellung (§245 Abs 1 BAO)
  - Fristverlängerung möglich: Antrag VOR Fristablauf (§245 Abs 3 BAO)
  - Fristberechnung: §108 BAO — Samstag, Sonntag, Feiertag → nächster Werktag
- **Form (§250 BAO):**
  - [ ] Bezeichnung des angefochtenen Bescheids
  - [ ] Erklärung, welche Änderungen beantragt werden (Beschwerdepunkte)
  - [ ] Begründung (Darstellung des Sachverhalts + rechtliche Argumentation)
  - [ ] Eventuell: Beweisanträge
- **Einbringung:** schriftlich beim zuständigen Finanzamt (nicht beim BFG!)
- **Aufschiebende Wirkung:** NEIN — Beschwerde hat KEINE aufschiebende Wirkung (§254 BAO). Separat Aussetzung der Einhebung beantragen!

### B: Beschwerdevorentscheidung (§262 BAO)

**What:** Das Finanzamt entscheidet selbst über die Beschwerde.

- Finanzamt kann: vollständig stattgeben, teilweise stattgeben, abweisen, oder den Bescheid auch zum Nachteil des Beschwerdeführers ändern (reformatio in peius möglich per §263 Abs 3 BAO!)
- ⚠️ **Reformatio in peius:** Das Finanzamt darf den Bescheid im Zuge der Beschwerdevorentscheidung auch VERSCHLECHTERN. Dieses Risiko dem User klar kommunizieren.
- Frist für Beschwerdevorentscheidung: keine gesetzliche Frist für das Finanzamt

### C: Vorlageantrag an BFG (§264 BAO)

**When:** User ist mit der Beschwerdevorentscheidung nicht einverstanden.

**Requirements:**
- **Frist:** 1 Monat ab Zustellung der Beschwerdevorentscheidung (§264 Abs 1 BAO)
- **Form:** Antrag auf Vorlage der Beschwerde an das BFG
- **Einbringung:** beim Finanzamt (nicht direkt beim BFG)
- **Inhalt (§264 Abs 1 BAO):**
  - Bezeichnung der Beschwerdevorentscheidung
  - Kann ergänzende Begründung enthalten (empfehlenswert!)
  - Antrag auf mündliche Verhandlung (§274 BAO) — empfehlenswert bei streitigen Sachverhaltsfragen
  - Antrag auf Senatsentscheidung (§272 BAO) — bei grundsätzlicher Bedeutung
- **Wirkung:** Der angefochtene Bescheid tritt wieder in den Stand einer unerledigt offenen Beschwerde

### D: BFG-Verfahren

**Ablauf nach Vorlageantrag:**
1. Finanzamt legt Akten an BFG vor (Vorlagebericht §265 BAO)
2. BFG kann weitere Ermittlungen durchführen
3. Mündliche Verhandlung (wenn beantragt oder vom BFG angeordnet, §274 BAO)
4. Erkenntnis oder Beschluss des BFG (§279 BAO)

**Entscheidungsmöglichkeiten des BFG:**
- Stattgebung (ganz oder teilweise)
- Abweisung
- Zurückverweisung an das Finanzamt (§278 BAO)
- ⚠️ Auch das BFG kann zum Nachteil entscheiden (reformatio in peius)

**Revision an den VwGH (Art 133 Abs 4 B-VG):**
- Nur bei Rechtsfragen von grundsätzlicher Bedeutung (Zulassungsrevision)
- Frist: 6 Wochen ab Zustellung des BFG-Erkenntnisses
- Anwaltspflicht vor dem VwGH (§24 VwGG)
- Oder: außerordentliche Revision wenn BFG Revision nicht zugelassen hat

### E: Selbstanzeige (§29 FinStrG)

**When:** User hat Abgaben hinterzogen oder verkürzt und will straffrei gestellt werden.

**⚠️ ZEITKRITISCH — Selbstanzeige muss VOR Entdeckung erstattet werden!**

**Voraussetzungen für strafbefreiende Wirkung (§29 Abs 1-3 FinStrG):**
1. **Rechtzeitigkeit:** VOR der Tat-Entdeckung durch die Behörde
   - Nicht mehr rechtzeitig wenn: Prüfungsauftrag zugestellt (§29 Abs 3 lit a), Tat bereits entdeckt (§29 Abs 3 lit b), Verfolgungshandlung gesetzt
   - ⚠️ Prüfen: Wurde bereits eine Betriebsprüfung angekündigt? Wurde ein Auskunftsersuchen zugestellt?
2. **Vollständigkeit:** ALLE Verfehlungen müssen offengelegt werden (nicht nur Teile)
   - Betrifft alle Abgabenarten und alle offenen Zeiträume
   - Unvollständige Selbstanzeige = KEINE Strafbefreiung
3. **Darlegung der Verfehlung:** Konkret und nachvollziehbar
   - Welche Abgabe, welcher Zeitraum, welcher Betrag
   - Gegenüberstellung: erklärt vs. tatsächlich
4. **Zahlung (§29 Abs 2 FinStrG):**
   - Verkürzungsbetrag MUSS entrichtet werden
   - Frist: 1 Monat ab Selbstanzeige (bei Abgabenhinterziehung §33 FinStrG)
   - Bei Beträgen >€33.000: Zuschlag 10% (§29 Abs 6 Z 1); >€100.000: 20%; >€250.000: 30%
   - Ratenzahlung möglich, aber nur bei Zahlungsschwierigkeiten mit Antrag

**Abgrenzung der Finanzdelikte:**
| Delikt | §§ FinStrG | Verschulden | Strafrahmen |
|--------|-----------|-------------|-------------|
| Abgabenhinterziehung | §33 | Vorsatz | bis 2x Verkürzungsbetrag |
| Fahrlässige Abgabenverkürzung | §34 | Fahrlässigkeit | bis 1x Verkürzungsbetrag |
| Finanzordnungswidrigkeit | §49 | Vorsatz | bis €5.000 je Tat |
| Abgabenbetrug | §39 | Qualifiziert vorsätzlich | bis 10 Jahre Freiheitsstrafe |

**Formale Anforderungen Selbstanzeige:**
- Schriftlich oder mündlich beim zuständigen Finanzamt
- Empfehlung: IMMER schriftlich, per Einschreiben oder persönlich mit Eingangsbestätigung
- Inhalt muss enthalten: Name, Abgabenart, Zeitraum, konkrete Beträge, berichtigte Erklärung

### F: Aussetzung der Einhebung (§212a BAO)

**When:** Beschwerde eingelegt, User will die strittige Abgabe nicht sofort zahlen müssen.

**Requirements:**
- Beschwerde muss eingebracht sein (oder gleichzeitig eingebracht werden)
- Antrag auf Aussetzung der Einhebung (§212a Abs 1 BAO)
- Aussetzung wird gewährt, wenn: die Beschwerde nicht aussichtslos erscheint
- **Aussetzungszinsen (§212a Abs 9 BAO):** 2% über dem Basiszinssatz pro Jahr. Werden festgesetzt wenn: Beschwerde erfolglos bleibt
- ⚠️ Aussetzung betrifft NUR den strittigen Betrag, nicht die gesamte Abgabenschuld

### G: Stundung und Ratenzahlung (§212 BAO)

**When:** User kann die Abgabenschuld nicht auf einmal zahlen.

**Requirements:**
- **Antrag:** schriftlich beim zuständigen Finanzamt
- **Voraussetzungen (§212 Abs 1 BAO):**
  - Einbringlichkeit nicht gefährdet UND
  - erhebliche Härte für den Abgabepflichtigen
- **Stundungszinsen (§212 Abs 2 BAO):** 2% über dem Basiszinssatz
- **Maximaldauer:** in der Regel max 12 Monate, in Ausnahmefällen länger
- **Ratenzahlung:** konkreten Tilgungsplan vorschlagen (realistisch!)
- Bei Ablehnung: Berufung/Beschwerde gegen den ablehnenden Bescheid möglich

### H: Wiederaufnahme des Verfahrens (§303 BAO)

**When:** Bescheid ist bereits rechtskräftig, aber neue Tatsachen/Beweise aufgetaucht.

**Voraussetzungen (§303 Abs 1 BAO):**
- Neu hervorgekommene Tatsachen oder Beweismittel (nova reperta)
- Die bei rechtzeitigem Vorbringen zu einem anders lautenden Bescheid geführt hätten
- Antrag oder von Amts wegen (§303 Abs 4 BAO)
- **Frist für Antrag:** keine ausdrückliche Frist, aber Verjährung der Abgabenfestsetzung beachten (§207 BAO: 5 Jahre, bei Hinterziehung 10 Jahre)

### I: Säumnisbeschwerde (§284 BAO)

**When:** Das Finanzamt entscheidet nicht innerhalb von 6 Monaten über eine Beschwerde.

**Requirements:**
- 6 Monate seit Einbringung der Beschwerde vergangen (§284 Abs 1 BAO)
- Finanzamt hat keine Beschwerdevorentscheidung erlassen und nicht an BFG vorgelegt
- **Einbringung:** direkt beim BFG
- **Wirkung:** BFG setzt dem Finanzamt eine Frist von max 3 Monaten → bei erneutem Säumnis entscheidet BFG selbst

---

## Step 4: Check ALL Deadlines (CRITICAL)

**⚠️ Fristenversäumnis im Abgabenverfahren ist in der Regel IRREPARABEL.**

Calculate ALL relevant deadlines. For each:

| Frist | Grundlage | Beginn | Ablauf | Status |
|-------|-----------|--------|--------|--------|
| Beschwerde | §245 Abs 1 BAO | Zustellung des Bescheids | +1 Monat | 🟢/🟡/🔴 |
| Vorlageantrag | §264 Abs 1 BAO | Zustellung der BVE | +1 Monat | 🟢/🟡/🔴 |
| VwGH-Revision | Art 133 Abs 4 B-VG | Zustellung des BFG-Erk. | +6 Wochen | 🟢/🟡/🔴 |
| Säumnisbeschwerde | §284 Abs 1 BAO | Einbringung der Beschwerde | +6 Monate | 🟢/🟡/🔴 |
| Selbstanzeige-Zahlung | §29 Abs 2 FinStrG | Erstattung der SA | +1 Monat | 🟢/🟡/🔴 |

**Fristberechnung (§108 BAO):**
- Monatsfrist: Ende am gleichen Tag des Folgemonats (z.B. 15.3. → 15.4.)
- Fällt Ende auf Sa/So/Feiertag → nächster Werktag
- Postaufgabe am letzten Tag genügt (§108 Abs 4 BAO)
- FinanzOnline-Eingabe: bis 24:00 Uhr am letzten Tag

**Wiedereinsetzung in den vorigen Stand (§308 BAO):**
- Möglich bei unvorhergesehener oder unabwendbarer Verhinderung
- Antrag innerhalb von 3 Monaten ab Wegfall des Hindernisses (§308 Abs 3 BAO)
- Gleichzeitig die versäumte Handlung nachholen
- Strenger Maßstab: leichte Fahrlässigkeit schadet bereits bei beruflich vertretenen Parteien

---

## Step 5: Draft the Appropriate Filing

Based on the classification, draft the relevant Schriftsatz. Always in proper Austrian legal format.

### Beschwerde (§250 BAO) — Template:

```
An das
Finanzamt Österreich
[zuständige Dienststelle]

[Name, Adresse, StNr/AbgNr des Beschwerdeführers]

[Ort], am [Datum]

BESCHWERDE
gemäß §243 Bundesabgabenordnung

gegen den Bescheid des Finanzamtes Österreich vom [Datum], zugestellt am [Datum],
betreffend [Einkommensteuer/Umsatzsteuer/...] für das Jahr [Jahr],
StNr: [Steuernummer]

I. ANFECHTUNGSERKLÄRUNG

Der oben bezeichnete Bescheid wird seinem gesamten Inhalt nach [bzw. insoweit als ...]
angefochten.

Es wird beantragt, den angefochtenen Bescheid dahingehend abzuändern, dass
[konkrete Änderung — z.B. "die Einkünfte aus Gewerbebetrieb mit €XX.XXX
statt €YY.YYY festgesetzt werden"].

II. BEGRÜNDUNG

1. Sachverhalt:
[Chronologische Darstellung der relevanten Tatsachen]

2. Rechtliche Beurteilung:
[Argumentation mit §§-Zitaten, warum der Bescheid rechtswidrig ist]

3. Beweis:
[Auflistung der Beweismittel: Beilagen, Zeugen, Sachverständige]

III. ANTRÄGE

1. Der Beschwerde wird stattgegeben und der angefochtene Bescheid wird
   dahingehend abgeändert, dass [konkretes Begehren].

2. Gleichzeitig wird gemäß §212a BAO die Aussetzung der Einhebung des
   strittigen Betrages in Höhe von €[Betrag] beantragt.

[3. Optional: Es wird die Durchführung einer mündlichen Verhandlung
    gemäß §274 BAO beantragt.]

[4. Optional: Es wird die Entscheidung durch den gesamten Senat
    gemäß §272 BAO beantragt.]

Beilagen:
./A — [Bezeichnung]
./B — [Bezeichnung]

[Unterschrift]
```

### Vorlageantrag (§264 BAO) — Template:

```
An das
Finanzamt Österreich
[zuständige Dienststelle]

[Name, Adresse, StNr]

[Ort], am [Datum]

VORLAGEANTRAG
gemäß §264 Bundesabgabenordnung

Gegen die Beschwerdevorentscheidung des Finanzamtes Österreich vom [Datum],
zugestellt am [Datum], betreffend [Abgabenart] für [Zeitraum],
wird der Antrag auf Entscheidung über die Beschwerde durch das
Bundesfinanzgericht gestellt.

Ergänzende Begründung:
[Warum die Beschwerdevorentscheidung unrichtig ist — neue Argumente, Judikatur]

Anträge:
1. Es wird beantragt, der Beschwerde stattzugeben und den Bescheid
   wie beantragt abzuändern.
2. Es wird die Durchführung einer mündlichen Verhandlung beantragt (§274 BAO).
[3. Optional: Senatsentscheidung (§272 BAO)]

[Unterschrift]
```

### Selbstanzeige (§29 FinStrG) — Template:

```
An das
Finanzamt Österreich
[zuständige Dienststelle]

[Name, Adresse, StNr]

[Ort], am [Datum]

SELBSTANZEIGE
gemäß §29 Finanzstrafgesetz

PERSÖNLICH / VERTRAULICH

I. OFFENLEGUNG

Der/Die Unterfertigte legt hiermit offen, dass für folgende Abgaben unrichtige
Erklärungen abgegeben / Erklärungen nicht abgegeben wurden:

| Abgabenart | Zeitraum | Erklärt | Tatsächlich | Verkürzung |
|-----------|----------|---------|-------------|------------|
| [ESt/USt/...] | [Jahr] | €[x] | €[x] | €[x] |

Gesamtverkürzungsbetrag: €[Summe]

II. DARLEGUNG DER VERFEHLUNG

[Konkrete Beschreibung: Was war falsch, warum, welche Umstände]

III. BERICHTIGTE STEUERERKLÄRUNGEN

Berichtigte Erklärungen für die betroffenen Zeiträume sind beigelegt /
werden umgehend nachgereicht.

IV. ZAHLUNG

Der Verkürzungsbetrag in Höhe von €[Betrag] wird innerhalb der Monatsfrist
des §29 Abs 2 FinStrG entrichtet. [Zzgl. Zuschlag gemäß §29 Abs 6 FinStrG
in Höhe von [10/20/30]% = €[Betrag].]

[Alternativ: Es wird um Bewilligung einer Ratenzahlung gemäß §212 BAO
ersucht, da eine sofortige Entrichtung eine erhebliche Härte darstellen
würde. Vorgeschlagener Tilgungsplan: ...]

V. ERKLÄRUNG

Diese Selbstanzeige betrifft sämtliche dem/der Unterfertigten bekannten
Verfehlungen im Zusammenhang mit den genannten Abgaben. Es wird versichert,
dass die Angaben vollständig und richtig sind.

Beilagen:
./1 — Berichtigte Steuererklärung [Abgabenart] [Jahr]
./2 — [Weitere Unterlagen]

[Unterschrift]

HINWEIS: Diese Selbstanzeige wird erstattet, BEVOR eine Entdeckung der Tat
durch die Abgabenbehörde erfolgt ist. Es ist weder ein Prüfungsauftrag
zugestellt noch eine Verfolgungshandlung gesetzt worden.
```

---

## Step 6: Present with Timeline and Next Steps

```markdown
# Steuerverfahren — Analyse und Handlungsempfehlung

**Verfahrensart:** [Beschwerde / Vorlageantrag / Selbstanzeige / Stundung / etc.]
**Betroffener Bescheid:** [Abgabenart, Zeitraum, Datum]
**Zugestellt am:** [Datum]
**Zuständiges Finanzamt:** [Dienststelle]

## ⚠️ Fristenübersicht
| Frist | Ablauf | Verbleibend | Status |
|-------|--------|-------------|--------|
| Beschwerde (§245 BAO) | [Datum] | [x] Tage | 🟢/🟡/🔴 |
| [weitere Fristen] | [Datum] | [x] Tage | 🟢/🟡/🔴 |

## Sachverhalt
[Zusammenfassung: Was ist passiert, was ist strittig]

## Rechtliche Beurteilung
[Analyse: Warum ist der Bescheid fehlerhaft / Was sind die Erfolgsaussichten]
- §§-Zitate
- Relevante BFG/VwGH-Judikatur

## Empfohlene Vorgehensweise

### Sofort-Maßnahmen
1. [z.B. "Beschwerde einreichen bis [Datum]"]
2. [z.B. "Aussetzung der Einhebung beantragen"]

### Verfahrensablauf (Timeline)
| Schritt | Frist | Aktion |
|---------|-------|--------|
| 1. Beschwerde | bis [Datum] | Beim Finanzamt einreichen |
| 2. Aussetzung §212a | gleichzeitig | Antrag stellen |
| 3. Beschwerdevorentscheidung | ca. [x] Monate | Finanzamt entscheidet |
| 4. ggf. Vorlageantrag | 1 Monat nach BVE | An BFG vorlegen |
| 5. BFG-Erkenntnis | ca. [x] Monate | Entscheidung |
| 6. ggf. VwGH-Revision | 6 Wochen nach Erk. | Nur bei Rechtsfrage |

## Erfolgsaussichten
| Szenario | Wahrscheinlichkeit | Konsequenz |
|----------|-------------------|------------|
| Beschwerde erfolgreich | [x]% | Bescheid wird abgeändert, keine Nachzahlung |
| Teilweiser Erfolg | [x]% | Reduktion um ca. €[x] |
| Beschwerde abgewiesen | [x]% | Nachzahlung €[x] + Aussetzungszinsen |

## Entwurf des Schriftsatzes
[Hier den konkreten Beschwerde-/Vorlageantrag-/Selbstanzeige-Entwurf einfügen]

## ⚠️ Risiken
- [z.B. "Reformatio in peius: Finanzamt kann den Bescheid auch verschlechtern"]
- [z.B. "Bei Selbstanzeige: Unvollständigkeit führt zum Verlust der Strafbefreiung"]
- [z.B. "Aussetzungszinsen bei Unterliegen: ca. €[x]"]

## Nächste Schritte
- [ ] [Konkreter erster Schritt mit Datum]
- [ ] [Zweiter Schritt]
- [ ] [Steuerberater/RA konsultieren für ...]

## Quellenstatus
| Kategorie | Status | Details |
|-----------|--------|---------|
| RIS MCP | 🟢 Verfügbar / 🔴 Nicht verfügbar | [connection status] |
| Gesetze | RIS_VERIFIED / OFFICIAL_WEB_VERIFIED / UNVERIFIED | [n] Normen geprüft |
| Judikatur | RIS_VERIFIED / OFFICIAL_WEB_VERIFIED / UNVERIFIED | [n] Entscheidungen |
| Prüfdatum | [YYYY-MM-DD] | |

---
⚠️ **Keine Rechtsberatung.** Diese Analyse dient der verfahrensrechtlichen Ersteinschätzung und ersetzt nicht die Beratung durch einen Steuerberater oder Rechtsanwalt. Insbesondere bei Selbstanzeigen und Finanzstrafverfahren wird dringend anwaltliche Vertretung empfohlen.
```

---

## Critical Rules

1. **Fristen sind HEILIG** — Eine versäumte Beschwerdefrist ist in der Regel endgültig. Immer als erstes die Frist berechnen und prominent anzeigen.
2. **Zustelldatum ist entscheidend** — Die Frist beginnt mit der Zustellung (§97 BAO), nicht mit dem Bescheiddatum. Immer nach dem Zustelldatum fragen.
3. **Aussetzung der Einhebung IMMER mitbeantragen** — Beschwerde hat keine aufschiebende Wirkung. Ohne §212a BAO-Antrag muss trotz Beschwerde gezahlt werden.
4. **Reformatio in peius warnen** — Sowohl Finanzamt (§263 Abs 3 BAO) als auch BFG können den Bescheid zum Nachteil ändern. User MUSS darüber informiert werden.
5. **Selbstanzeige: Vollständigkeit oder nichts** — Eine unvollständige Selbstanzeige ist wertlos und kann sogar schaden. Im Zweifel Steuerberater/RA einschalten BEVOR die Selbstanzeige erstattet wird.
6. **Selbstanzeige: Timing prüfen** — Wenn bereits eine Prüfung angekündigt oder ein Auskunftsersuchen zugestellt wurde, ist es möglicherweise zu spät (§29 Abs 3 FinStrG). Das MUSS geprüft werden.
7. **Beschwerde beim FINANZAMT einreichen, nicht beim BFG** — Häufiger Fehler. Vorlageantrag ebenfalls beim Finanzamt (§264 Abs 1 BAO).
8. **§§ immer mit Gesetzesname** — §245 BAO, nicht nur "§245". §29 FinStrG, nicht nur "§29".
9. **Use RIS if connected** — Verify procedural provisions and deadlines are current.
10. **Match user's language** — German in → German out. English in → English out. Gesetze immer in deutscher Form.
