---
name: recht-exekution-momarcode1
title: /recht exekution — Exekutionsrecht (Procedural)
description: Austrian enforcement and execution law — Exekutionstitel, Exekutionsantrag (EO), Fahrnis- und Forderungsexekution, Oppositionsklage, Impugnationsklage, Raeumungsexekution, Existenzminimum, and personal insolvency procedure.
author: MoMarcode1
author_url: https://github.com/MoMarcode1/austrian-legal-claude/tree/main/skills/recht-exekution
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: at
practice: litigation
language: de
sources:
- title: Ris protocol
  path: references/ris-protocol.md
---

# /recht exekution — Exekutionsrecht (Procedural)

When the user needs to enforce a judgment, defend against execution proceedings, or file for personal insolvency, follow these steps exactly.

---

## Step 1: Read the Facts and Determine the Role

Read everything the user has provided. You need:

1. **Which side?** — Ist der User betreibender Glaeubiger (will vollstrecken) oder Verpflichteter (wird vollstreckt)?
2. **Exekutionstitel vorhanden?** — Welcher Titel? (Urteil, Zahlungsbefehl, Notariatsakt, gerichtlicher Vergleich, Bescheid)
3. **Art der Forderung** — Geldforderung, Raeumung, Herausgabe, Unterlassung?
4. **Hoehe** — Bei Geldforderung: Hauptforderung, Zinsen, Kosten
5. **Vermoegen/Einkommen des Verpflichteten** — Arbeitseinkommen (Lohnpfaendung), Bankkonten (Kontopfaendung), Fahrnisse (bewegliche Sachen), Liegenschaften (Immobilien)?
6. **Was ist bereits passiert?** — Exekutionsantrag gestellt? Exekutionsbewilligung erteilt? Pfaendung durchgefuehrt? Raeumungstermin angesetzt?
7. **Einwendungen?** — Forderung bereits bezahlt? Formfehler im Titel? Unzulaessige Pfaendung? Existenzminimum verletzt?

If critical information is missing, ask:
> "Haben Sie einen rechtskraeftigen Exekutionstitel? Ohne Titel ist keine Exekution moeglich."
> "Werden Sie gepfaendet oder wollen Sie eine Forderung vollstrecken? Das bestimmt die naechsten Schritte."

---

## Step 2: RIS Verification

Before proceeding with analysis, follow the **RIS Verification Protocol** (`references/ris-protocol.md`):
1. Check RIS MCP availability
2. For every § you cite, verify current wording via RIS
3. For case law references (OGH, LG), retrieve via RIS Justiz
4. Record verification status for the Quellenstatus block
5. If RIS is unavailable, follow the fallback ladder and flag all affected citations

---

## Step 3: Classify the Exekutionstitel

**Zulässige Exekutionstitel (§1 EO):**

| Titel | Grundlage | Besonderheiten |
|-------|-----------|----------------|
| Gerichtliches Urteil | §1 Z 1 EO | Rechtskraft + Vollstreckbarkeitsbestaetigung erforderlich |
| Zahlungsbefehl (rechtskraeftig) | §1 Z 1 EO | Nach Ablauf der 4-Wochen-Einspruchsfrist (§252 ZPO) |
| Gerichtlicher Vergleich | §1 Z 5 EO | Sofort vollstreckbar |
| Vollstreckbarer Notariatsakt | §1 Z 17 EO | Schuldner hat sich der Exekution unterworfen (§3 NO) |
| Bescheid (VwG, Verwaltungsbehoerde) | §1 Z 12 EO | Rechtskraeftig und vollstreckbar |
| Europaeischer Zahlungsbefehl | VO 1896/2006 | Grenzueberschreitend, ohne Exequatur |
| Europaeischer Vollstreckungstitel | VO 805/2004 | Unbestrittene Forderungen |
| Schiedsspruch | §1 Z 16 EO | Nach §614 ZPO |

**Vollstreckbarkeitsbestaetigung (§7 EO):**
- Erforderlich fuer Urteile und Zahlungsbefehle
- Wird vom Titelgericht erteilt
- Prueft: Rechtskraft + Ablauf einer allfaelligen Leistungsfrist

---

## Step 4: Determine the Exekutionsart

### A: Forderungsexekution / Lohnpfaendung (§§290ff EO)

**Ablauf:**

1. **Exekutionsantrag (§3 EO)**
   - Beim zustaendigen Bezirksgericht (Wohnsitz des Verpflichteten, §18 EO)
   - Inhalt: Exekutionstitel bezeichnen, Forderung beziffern, Exekutionsart waehlen, Drittschuldner angeben
   - Gerichtsgebuehr: nach GGG

2. **Exekutionsbewilligung (§3a EO)**
   - Gericht prueft NUR formale Voraussetzungen (Titel vorhanden, Antrag formal korrekt)
   - Gericht prueft NICHT, ob die Forderung materiell berechtigt ist oder bereits bezahlt wurde
   - Bewilligung wird dem Verpflichteten UND dem Drittschuldner zugestellt

3. **Pfaendung (§294 EO)**
   - Verbot an den Drittschuldner (Arbeitgeber, Bank), an den Verpflichteten zu zahlen
   - Gebot, den pfaendbaren Betrag an den betreibenden Glaeubiger abzufuehren
   - Drittschuldnererklaerung (§301 EO): Drittschuldner muss innerhalb von 4 Wochen erklaeren, ob und in welcher Hoehe die Forderung besteht

4. **Existenzminimum berechnen (§291a EO, ExGEO)**
   - Unpfaendbarer Grundbetrag laut ExGEO-Tabellen
   - Je Unterhaltspflicht: Erhoehung des Freibetrags
   - Sonderzahlungen (13./14. Gehalt): Eigene Berechnung (§291c EO)
   - **Unpfaendbare Bezuege (§290a EO):**
     - Familienbeihilfe, Kinderbeihilfe
     - Pflegegeld
     - Wohnbeihilfe
     - Reise- und Aufwandsentschaedigungen (soweit kein Einkommen)
     - Gefahrenzulage, Schmutzzulage (teilweise)

5. **Ueberweisung (§303 EO)**
   - Zur Einziehung: Glaeubiger zieht die Forderung ein
   - An Zahlungs statt: Forderung geht auf den Glaeubiger ueber

**Kontopfaendung (§294 EO analog):**
- Bankguthaben koennen gepfaendet werden
- Kontoschutz: Letzte laufende Gehaltszahlung geniesst Pfaendungsschutz in Hoehe des Existenzminimums (§290a Abs 3 EO)

### B: Fahrnisexekution (§§249ff EO)

**Ablauf:**

1. **Exekutionsantrag** — wie oben
2. **Pfaendung durch Gerichtsvollzieher (§253 EO)**
   - Gerichtsvollzieher kommt in die Wohnung/Geschaeftsraeume des Verpflichteten
   - Pfaendung durch koerperliches Ergreifen oder Anbringen eines Pfaendungsprotokolls
   - Pfaendbare Sachen: Wertsachen, Elektronik, Fahrzeuge, Schmuck, etc.
   - **Unpfaendbare Sachen (§251 EO):**
     - Lebensnotwendige Kleidung und Bettwaesche
     - Notwendige Haushaltsgeraete (Herd, Kuehlschrank, Waschmaschine)
     - Arbeitsmittel, die fuer den Beruf erforderlich sind
     - Gegenstände des persönlichen Gebrauchs von geringem Wert
     - Schulbuecher und Lernmittel fuer Kinder
     - Behelfe fuer Koerperbehinderungen
     - Lebensmittelvorraete fuer 4 Wochen
3. **Versteigerung (§§271ff EO)**
   - Veroeffentlichung des Versteigerungstermins
   - Mindestgebot: kein festes Mindestgebot bei Fahrnissen
   - Erlös wird an den Glaeubiger ausgekehrt

### C: Raeumungsexekution (§§349ff EO)

**Wann:** Exekutionstitel lautet auf Raeumung einer Liegenschaft (z.B. nach Kuendigung/Raeumungsklage).

**Ablauf:**

1. **Exekutionsantrag auf Raeumung (§349 EO)**
   - Beim zustaendigen Bezirksgericht
   - Grundlage: Raeumungsurteil oder vergleichbarer Titel

2. **Raeumungstermin**
   - Gericht setzt Termin fest
   - Gerichtsvollzieher fuehrt Raeumung durch
   - Verpflichteter und alle Mitbewohner muessen die Wohnung verlassen
   - Fahrnisse des Verpflichteten werden auf dessen Kosten eingelagert

3. **Aufschiebung (§42 EO)**
   - Verpflichteter kann Antrag auf Aufschiebung stellen
   - Voraussetzungen: drohendes schweres und unwiederbringliches Nachteil (z.B. Obdachlosigkeit bei Familie mit Kindern)
   - Dauer: befristet, bis Alternative gefunden

4. **Raeumungsschutz (§34 MRG)**
   - Bei Mietverhaeltnissen unter dem MRG: Gericht kann Raeumungsfrist gewaehren (bis zu 9 Monate, §34 Abs 2 MRG)
   - Soziale Haertefaelle: verlaengerte Frist moeglich

### D: Liegenschaftsexekution (§§87ff EO, §§133ff EO)

**Zwangsversteigerung (§§133ff EO):**
- Letzte Stufe der Exekution auf eine Liegenschaft
- Exekutionsantrag + Schoenzungswert + Gutachten
- Mindestgebot: 50% des Schaetzwerts bei erster Versteigerung
- Grundbuchsmaessige Eintragung des Versteigerungsvermerks

**Zwangsverwaltung (§§97ff EO):**
- Alternative: Ertrage der Liegenschaft (Mieten) werden zur Schuldentilgung herangezogen
- Zwangsverwalter wird bestellt

---

## Step 5: Rechtsbehelfe des Verpflichteten

### Oppositionsklage (§35 EO) — Einwendung nach Entstehung des Titels

**Wann:** Die Forderung ist NACH Entstehung des Titels erloschen (z.B. bezahlt, aufgerechnet, gestundet, verjaehrt).

**Voraussetzungen:**
- Rechtsmaessiger Exekutionstitel liegt vor
- Einwendungen betreffen Tatsachen, die NACH Entstehung des Titels eingetreten sind (§35 Abs 1 EO)
- Bei gerichtlichem Vergleich/Notariatsakt: auch Einwendungen ueber Tatsachen VOR Titelentstehung (§35 Abs 1 zweiter Satz EO)

**Typische Gruende:**
- Zahlung (Erfuellung)
- Aufrechnung
- Stundungsvereinbarung
- Nachtraegliche Verjaehrung
- Vergleich (aussergerichtlich)
- Schuldnachlass

**Verfahren:**
- Klage beim Titelgericht (§35 Abs 2 EO)
- Gleichzeitig: Antrag auf Aufschiebung der Exekution (§42 Abs 1 Z 5 EO)
- Beweislast beim Verpflichteten

### Impugnationsklage (§36 EO) — Einwendung gegen die Exekutionsbewilligung

**Wann:** Die Exekutionsbewilligung ist FORMELL fehlerhaft (unzulaessige Exekution, kein tauglicher Titel, Vollstreckbarkeit nicht gegeben).

**Typische Gruende:**
- Exekutionstitel ist nicht rechtskraeftig/vollstreckbar
- Exekution gegen die falsche Person gefuehrt
- Vollstreckbarkeitsbestaetigung fehlt oder ist fehlerhaft
- Exekution wurde fuer eine andere als die im Titel ausgesprochene Leistung bewilligt
- Leistungsfrist noch nicht abgelaufen

**Verfahren:**
- Klage beim Exekutionsgericht (§36 Abs 2 EO)
- Frist: 14 Tage ab Kenntnis des Anfechtungsgrundes (§36 Abs 2 EO)
- Gleichzeitig: Antrag auf Aufschiebung (§42 Abs 1 Z 5 EO)

### Aufschiebung der Exekution (§42 EO)

**Gruende fuer Aufschiebung (§42 Abs 1 EO):**
- Z 1: Wiedereinsetzungsantrag gegen den Exekutionstitel
- Z 2: Nichtigkeitsklage oder Wiederaufnahmsklage
- Z 3a: Berufung gegen den Exekutionstitel
- Z 5: Oppositions- oder Impugnationsklage eingebracht
- Z 7: Einstellung beantragt wegen Zahlung/Stundung

**Voraussetzung:** Der Verpflichtete muss glaubhaft machen, dass ihm durch die Fortsetzung der Exekution ein unwiederbringlicher oder schwer zu ersetzender Nachteil droht (§42 Abs 3 EO).

**Sicherheitsleistung:** Gericht kann dem Verpflichteten Sicherheitsleistung auferlegen (§42 Abs 3 EO).

### Einstellung der Exekution (§39 EO)

**Gruende (§39 Abs 1 EO):**
- Z 1: Exekutionstitel aufgehoben
- Z 2: Aufschiebung angeordnet (und Frist abgelaufen ohne dass Klaeger handelt)
- Z 6: Verjaehrung des Exekutionsrechts (30 Jahre, §§39 Abs 1 Z 6, 51 EO)
- Z 8: Verpflichteter leistet Sicherheit
- Z 10: Forderung bezahlt / erloschen

**Antrag auf Einstellung:** Beim Exekutionsgericht, jederzeit waehrend des Exekutionsverfahrens.

---

## Step 6: Privatinsolvenz-Verfahren (fuer Verpflichtete)

Wenn der Verpflichtete zahlungsunfaehig ist und eine Gesamtloesung anstrebt:

### Antrag auf Schuldenregulierungsverfahren (§183 IO)

**Voraussetzungen:**
1. Natuerliche Person (nicht juristische Person — fuer diese: §§66ff IO)
2. Zahlungsunfaehigkeit (§66 IO analog)
3. Gescheiterter aussergerichtlicher Ausgleichsversuch (§183 Abs 1 IO) — Bestaetigung der Schuldnerberatung

**Einzureichende Unterlagen:**
- Vermoegensverzeichnis (§185 Abs 2 IO)
- Glaeubigerverzeichnis (alle Glaeubiger mit Adresse und Forderungshoehe)
- Einkommensnachweise (Lohnzettel, Steuerbescheid)
- Bestaetigung der Schuldnerberatung ueber gescheiterten aussergerichtlichen Ausgleich
- Ggf. Zahlungsplanvorschlag (§193 IO)

### Template: Antrag auf Schuldenregulierungsverfahren

```
An das
Bezirksgericht [Ort] als Insolvenzgericht

[Name, Geburtsdatum, Adresse, SV-Nr. des Antragstellers]

ANTRAG
auf Eroeffnung eines Schuldenregulierungsverfahrens
gemaess §183 Insolvenzordnung

I. ANTRAGSTELLUNG

Der/Die Antragsteller/in stellt den Antrag auf Eroeffnung eines
Schuldenregulierungsverfahrens gemaess §183 IO.

II. ZAHLUNGSUNFAEHIGKEIT

Der/Die Antragsteller/in ist zahlungsunfaehig. Die Gesamtverbindlichkeiten
betragen EUR [Betrag] bei [n] Glaeubigern. Das monatliche Nettoeinkommen
betraegt EUR [Betrag]. Eine Tilgung der Gesamtschulden ist nicht moeglich.

III. AUSSERGERICHTLICHER AUSGLEICHSVERSUCH

Ein aussergerichtlicher Ausgleichsversuch wurde ueber die [Name der
Schuldnerberatungsstelle] durchgefuehrt und ist gescheitert.
Bestaetigung liegt bei (Beilage ./A).

IV. VERMOEGENSVERZEICHNIS (§185 IO)

1. Einkommen:
   - [Quelle]: EUR [Betrag] monatlich netto
   
2. Vermoegenswerte:
   - [Auflistung oder: "Kein verwertbares Vermoegen vorhanden"]

3. Unterhaltspflichten:
   - [Anzahl und Art]

V. GLAEUBIGERVERZEICHNIS

| Nr. | Glaeubiger | Adresse | Forderung (EUR) | Titel? |
|-----|-----------|---------|-----------------|--------|
| 1 | [Name] | [Adresse] | [Betrag] | [Ja/Nein] |
| 2 | [Name] | [Adresse] | [Betrag] | [Ja/Nein] |
| Summe | | | [Gesamtbetrag] | |

VI. ZAHLUNGSPLAN (§193 IO)

[Option A: Zahlungsplanvorschlag]
Den Glaeubigern wird eine Quote von [x]% angeboten, zahlbar in
[monatlichen/vierteljaehrlichen] Raten ueber [x] Jahre.

[Option B: Abschoepfungsverfahren]
Fuer den Fall, dass der Zahlungsplan nicht angenommen wird, wird die
Einleitung des Abschoepfungsverfahrens gemaess §199 IO beantragt.

Beilagen:
./A — Bestaetigung Schuldnerberatung
./B — Einkommensnachweise (letzte 3 Lohnzettel)
./C — Vermögensverzeichnis (detailliert)
./D — [weitere Unterlagen]

[Ort], am [Datum]
[Unterschrift]
```

### Template: Einspruch gegen Zahlungsbefehl

```
An das
Bezirksgericht [Ort]

[Name, Adresse des Einspruchswerbers]
AZ: [Geschaeftszahl]

EINSPRUCH
gegen den Zahlungsbefehl vom [Datum], AZ [Geschaeftszahl],
zugestellt am [Zustelldatum]

Innerhalb offener Frist (§252 Abs 1 ZPO — 4 Wochen ab Zustellung) wird
gegen den oben bezeichneten Zahlungsbefehl

EINSPRUCH

erhoben.

Begruendung:

1. Sachverhalt:
[Darstellung, warum die Forderung nicht besteht oder nicht in dieser
Hoehe — z.B. Bezahlung, Aufrechnung, Gewaehrleistung, Verjaehrung,
Forderung nie entstanden]

2. Rechtliche Begruendung:
[§§-Zitate — z.B. §1412 ABGB (Zahlung), §1438 ABGB (Aufrechnung),
§932 ABGB (Gewaehrleistung), §1489 ABGB (Verjaehrung)]

3. Beweismittel:
- [Zahlungsbeleg / Kontoauszug]
- [Korrespondenz]
- [Zeugen]
- [PV = Parteienvernehmung]

Es wird beantragt, den Zahlungsbefehl aufzuheben.

[Alternativ, wenn Gegenforderung:]
Es wird weiters die Aufrechnung mit einer Gegenforderung in Hoehe von
EUR [Betrag] aus [Rechtsgrund] erklaert (§1438 ABGB).

[Ort], am [Datum]
[Unterschrift]

Beilagen:
./1 — [Bezeichnung]
./2 — [Bezeichnung]
```

---

## Step 7: Present with Timeline and Next Steps

```markdown
# Exekutionsrechtliche Analyse

**Rolle:** [Betreibender Glaeubiger / Verpflichteter]
**Exekutionstitel:** [Art, Datum, Geschaeftszahl]
**Forderung:** EUR [Betrag] (Hauptforderung EUR [x] + Zinsen EUR [x] + Kosten EUR [x])
**Exekutionsart:** [Forderungsexekution / Fahrnisexekution / Raeumung / Liegenschaft]
**Zustaendiges Gericht:** BG [Ort]

## Fristenübersicht
| Frist | Ablauf | Verbleibend | Status |
|-------|--------|-------------|--------|
| Einspruch Zahlungsbefehl (§252 ZPO) | [Datum] | [x] Tage | OK / KRITISCH / ABGELAUFEN |
| Impugnationsklage (§36 EO) | [Datum] | 14 Tage ab Kenntnis | OK / KRITISCH |
| [weitere Fristen] | | | |

## Rechtliche Beurteilung

### Fuer den betreibenden Glaeubiger:
[Welche Exekutionsart ist sinnvoll? Wo ist Vermoegen des Verpflichteten? Kosten/Nutzen?]

### Fuer den Verpflichteten:
[Welche Rechtsbehelfe stehen zur Verfuegung? Oppositionsklage? Impugnationsklage?
Aufschiebung? Ist das Existenzminimum gewahrt?]

### Existenzminimum-Berechnung (bei Lohnpfaendung)
| Position | Betrag |
|----------|--------|
| Nettoeinkommen | EUR [x] |
| Unpfaendbarer Grundbetrag (ExGEO) | EUR [x] |
| + Unterhaltsstaffel ([n] Personen) | EUR [x] |
| = Existenzminimum | **EUR [x]** |
| Pfaendbarer Betrag | **EUR [x]** |

## Empfohlene Vorgehensweise

### Sofort-Massnahmen
1. [z.B. "Einspruch gegen Zahlungsbefehl einlegen — Frist: [Datum]!"]
2. [z.B. "Oppositionsklage einbringen + Aufschiebungsantrag (§42 EO)"]
3. [z.B. "Existenzminimum pruefen — moeglicherweise zu viel gepfaendet"]

### Verfahrensablauf
| Schritt | Frist | Aktion |
|---------|-------|--------|
| 1. [Aktion] | [Frist] | [Details] |
| 2. [Aktion] | [Frist] | [Details] |

## Entwurf des Schriftsatzes
[Konkreten Entwurf hier einfuegen]

## Risiken
- [z.B. "Bei versaeumtem Einspruch wird der Zahlungsbefehl rechtskraeftig"]
- [z.B. "Fahrnisexekution: Gerichtsvollzieher kann kurzfristig erscheinen"]
- [z.B. "Raeumungsexekution: Obdachlosigkeit droht — sofort Aufschiebung beantragen"]

## Anlaufstellen
- **Schuldnerberatung [Bundesland]:** Kostenlose Beratung, Begleitung im Insolvenzverfahren
- **Arbeiterkammer:** Bei Fragen zur Lohnpfaendung
- **Rechtsanwalt:** Bei Oppositions-/Impugnationsklagen dringend empfohlen
- **Bezirksgericht:** Exekutionsantraege, Einsprueche, Insolvenzantraege

## Quellenstatus
| Kategorie | Status | Details |
|-----------|--------|---------|
| RIS MCP | Verfuegbar / Nicht verfuegbar | |
| Gesetze | RIS_VERIFIED / UNVERIFIED | [n] Normen geprueft |
| Judikatur | RIS_VERIFIED / UNVERIFIED | [n] Entscheidungen |
| Pruefdatum | [YYYY-MM-DD] | |

---
Keine Rechtsberatung. Diese Analyse und die Mustervorlagen dienen der rechtlichen Ersteinschaetzung und ersetzen nicht die Beratung durch einen Rechtsanwalt. Exekutionsverfahren sind formstreng — Fehler koennen zum Verlust von Rechten fuehren. Bei Oppositions- und Impugnationsklagen sowie bei Insolvenzantraegen wird anwaltliche Vertretung dringend empfohlen.
```

---

## Critical Rules

1. **Exekutionstitel ist ZWINGENDE Voraussetzung** — Ohne rechtskraeftigen und vollstreckbaren Exekutionstitel (§1 EO) ist KEINE Exekution moeglich. Immer als Erstes pruefen.
2. **Einspruchsfrist Zahlungsbefehl: 4 Wochen** — §252 ZPO. Versaeumnis = Rechtskraft = Exekutionstitel fuer den Glaeubiger. IMMER prominent warnen.
3. **Existenzminimum ist UNANTASTBAR** — Das Existenzminimum (§291a EO, ExGEO) darf NICHT unterschritten werden. Wenn zu viel gepfaendet wird: sofort Antrag auf Herabsetzung oder Einstellung.
4. **Oppositionsklage (§35 EO) vs. Impugnationsklage (§36 EO)** — NICHT verwechseln. Opposition = materielle Einwendungen (bezahlt, aufgerechnet). Impugnation = formelle Einwendungen (Titel unwirksam, falsche Person). Falscher Rechtsbehelf = Abweisung.
5. **Impugnationsklage: 14-Tage-Frist** — §36 Abs 2 EO: 14 Tage ab Kenntnis des Grundes. SEHR KURZ. Sofort handeln.
6. **Aufschiebung GLEICHZEITIG beantragen** — Bei Oppositions- oder Impugnationsklage IMMER gleichzeitig Aufschiebung nach §42 EO beantragen. Sonst laeuft die Exekution weiter.
7. **Unpfaendbare Sachen kennen** — §251 EO: Lebensnotwendige Gegenstaende sind unpfaendbar. Wenn der Gerichtsvollzieher unpfaendbare Sachen pfaendet: sofort Beschwerde.
8. **Schuldnerberatung VOR Insolvenz** — Vor dem Insolvenzantrag MUSS ein aussergerichtlicher Ausgleichsversuch unternommen werden (§183 IO). Schuldnerberatung begleitet diesen Prozess kostenlos.
9. **§§ immer mit Gesetzesname** — §35 EO, §290 EO, §183 IO, §252 ZPO. Nie ohne Gesetzesangabe.
10. **Match user's language** — German in = German out. English in = English out. Gesetze immer in deutscher Originalform zitieren.
