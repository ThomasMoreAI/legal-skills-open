---
name: recht-verbraucher-verfahren-momarcode1
title: /recht verbraucher-verfahren — Verbraucherschutz-Verfahren (Procedural)
description: Austrian consumer protection procedure — enforcing Gewaehrleistung claims (Maengelruege, Fristsetzung, Klage BG), exercising FAGG withdrawal (form, email, deadline, return costs), Schlichtungsstelle, European Small Claims Procedure, VKI complaints, and online dispute resolution. Includes draft templates for Ruecktrittserklärung and Maengelruege.
author: MoMarcode1
author_url: https://github.com/MoMarcode1/austrian-legal-claude/tree/main/skills/recht-verbraucher-verfahren
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: at
practice: consumer
language: de
sources:
- title: Ris protocol
  path: references/ris-protocol.md
---

# /recht verbraucher-verfahren — Verbraucherschutz-Verfahren (Procedural)

When the user needs to ENFORCE a consumer protection right — file a complaint, exercise withdrawal, draft a Maengelruege, or take legal action against a business — follow these steps exactly.

---

## Step 1: Read the Facts and Determine the Goal

Read everything the user has provided. You need:

1. **What right is to be enforced?** — Gewaehrleistung (Reparatur/Austausch/Preisminderung/Wandlung), FAGG-Ruecktritt, Klausel-Nichtigkeit, Schadenersatz?
2. **What has already happened?** — Muendliche Reklamation? Schriftliche Ruege? Haendler-Reaktion? Fristsetzung?
3. **When?** — Alle relevanten Daten: Kauf, Lieferung, Mangel entdeckt, erste Reklamation, Fristen
4. **Streitwert** — Wie hoch ist der Kaufpreis / der Schaden? Bestimmt Zustaendigkeit (BG bis €15.000, LG darueber) und Anwaltspflicht (LG = Anwaltspflicht)
5. **Beweislage** — Kaufbeleg, Rechnung, E-Mail-Verkehr, Fotos des Mangels, Sachverstaendigengutachten?
6. **Gegnerverhalten** — Reagiert der Haendler? Verweigert er? Ignoriert er?

If critical information is missing, ask:
> "Haben Sie die Reklamation bereits schriftlich an den Haendler gerichtet? Das ist der erste notwendige Schritt."
> "Wie hoch war der Kaufpreis? Das bestimmt, ob das Bezirksgericht oder Landesgericht zustaendig ist."

---

## Step 2: RIS Verification

Before proceeding with analysis, follow the **RIS Verification Protocol** (`references/ris-protocol.md`):
1. Check RIS MCP availability
2. For every § you cite, verify current wording via RIS
3. For case law references, retrieve via RIS Justiz
4. Record verification status for the Quellenstatus block
5. If RIS is unavailable, follow the fallback ladder and flag all affected citations

---

## Step 3: Determine the Procedural Path

### Path A: Gewaehrleistungsanspruch durchsetzen

**Stufe 1: Aussergerichtlich — Maengelruege und Fristsetzung**

1. **Schriftliche Maengelruege** an den Verkaeufer (nicht den Hersteller!)
   - Mangel konkret beschreiben
   - Gewaehrleistung nach §§922ff ABGB geltend machen
   - Konkreten Primaerbehelf waehlen: Verbesserung ODER Austausch
   - Angemessene Frist setzen (in der Regel 14 Tage, bei komplexeren Reparaturen laenger)
   - Per Einschreiben oder E-Mail mit Lesebestaetigung senden
   - Kaufbeleg/Rechnung beilegen (Kopie!)

2. **Wenn Haendler nicht reagiert oder verweigert:**
   - Zweites Schreiben mit Nachfrist (7-14 Tage)
   - Hinweis: "Bei fruchtlosem Fristablauf behalte ich mir Preisminderung/Wandlung gemaess §932 Abs 4 ABGB sowie die gerichtliche Geltendmachung vor."
   - Ankuendigung der AK-/VKI-Einschaltung

3. **Wenn Primaerbehelf scheitert:**
   - Sekundaerbehelf geltend machen (Preisminderung oder Wandlung)
   - Erneut Frist setzen

**Stufe 2: Schlichtung / Alternative Streitbeilegung**

4. **Schlichtungsstelle fuer Verbrauchergeschaefte**
   - Antrag online oder schriftlich: verbraucherrecht.at
   - Zustaendig fuer inlaendische B2C-Streitigkeiten
   - Kostenlos fuer den Verbraucher
   - Teilnahme des Unternehmers grundsaetzlich freiwillig
   - Verfahrensdauer: ca. 90 Tage
   - Ergebnis: Empfehlung (nicht bindend, ausser bei regulierten Branchen)

5. **Arbeiterkammer (AK) — Konsumentenberatung und Rechtsschutz**
   - AK-Mitglieder: kostenlose Rechtsberatung
   - AK kann aussergerichtliche Intervention beim Haendler versuchen
   - AK-Rechtsschutz: Kann bei Erfolgsaussicht Klage finanzieren

6. **Europaeisches Verbraucherzentrum (EVZ)**
   - Bei grenzueberschreitenden Kaeufen innerhalb der EU/EWR
   - Kostenlose Streitschlichtung
   - Kontaktiert die Schwester-Organisation im anderen EU-Land

**Stufe 3: Gerichtlich**

7. **Mahnverfahren (§§244ff ZPO)**
   - Fuer Geldforderungen bis €75.000
   - Antrag auf Zahlungsbefehl (§244 ZPO)
   - Einbringung ueber ERV (Elektronischer Rechtsverkehr) oder formulargemaess bei Gericht
   - Gerichtsgebuehr: nach GGG (deutlich geringer als bei Klage)
   - Gegner hat 4 Wochen fuer Einspruch (§252 ZPO)
   - Ohne Einspruch: Zahlungsbefehl wird rechtskraeftig = Exekutionstitel

8. **Klage (wenn Einspruch oder kein Mahnverfahren)**
   - **Zustaendigkeit:**
     - BG: Streitwert bis €15.000 (§49 Abs 1 JN)
     - LG: Streitwert ueber €15.000 (§49 Abs 1 JN)
     - Wahlgerichtsstand Verbraucher: §14 KSchG — Wohnsitz des Verbrauchers
   - **Anwaltspflicht:** Nur vor dem LG (§27 ZPO). Vor dem BG: Selbstvertretung moeglich
   - **Gerichtsgebuehren:** Nach GGG, abhaengig vom Streitwert
   - **Beweismittel vorbereiten:** Kaufbeleg, Maengelruege (Kopie), Fotos, ggf. Sachverstaendigengutachten

9. **Europaeisches Bagatellverfahren (VO 861/2007)**
   - Fuer grenzueberschreitende Streitigkeiten innerhalb der EU
   - Streitwert bis €5.000
   - Formularbasiert, schriftliches Verfahren
   - Entscheidung ist in allen EU-Mitgliedstaaten vollstreckbar ohne Exequatur

### Path B: FAGG-Ruecktritt ausueben

**Schritt-fuer-Schritt:**

1. **Pruefen: Ist das FAGG anwendbar?**
   - Fernabsatzvertrag oder ausserhalb von Geschaeftsraeumen geschlossen?
   - B2C-Vertrag?
   - Keine Ausnahme nach §18 FAGG?

2. **Pruefen: Ist die Frist noch offen?**
   - 14 Tage ab Warenerhalt / Vertragsschluss (§11 FAGG)
   - Bei fehlender Belehrung: 12 Monate + 14 Tage (§12 FAGG)

3. **Ruecktrittserklärung abgeben**
   - Keine besondere Form erforderlich (§13 Abs 1 FAGG)
   - Empfehlung: Schriftlich (E-Mail oder Brief), eindeutig formuliert
   - Muster-Widerrufsformular verwenden (Anhang I Teil B der RL 2011/83/EU)
   - Absendung innerhalb der Frist genuegt (§13 Abs 2 FAGG — Absendetheorie!)

4. **Ware zuruecksenden**
   - Innerhalb von 14 Tagen nach Ruecktrittserklärung (§15 Abs 1 FAGG)
   - Ruecksendekosten: Verbraucher traegt sie, WENN vorher darauf hingewiesen wurde (§15 Abs 3 FAGG)
   - Ware muss nicht originalverpackt sein, aber in angemessenem Zustand
   - Wertersatz nur bei ueber die Pruefung hinausgehender Benutzung (§15 Abs 4 FAGG)

5. **Rueckerstattung einfordern**
   - Unternehmer muss innerhalb 14 Tagen erstatten (§14 Abs 1 FAGG)
   - Gleiches Zahlungsmittel wie bei Bezahlung (§14 Abs 1 FAGG)
   - Wenn nicht erstattet: Frist setzen, dann Mahnverfahren

### Path C: VKI-Beschwerde und Verbandsklage

1. **VKI-Beschwerde einreichen**
   - Online unter vki.at oder schriftlich
   - Sachverhalt schildern, Belege beilegen
   - VKI prueft, ob Musterprozess gefuehrt wird

2. **VKI-Verbandsklage (§28 KSchG)**
   - VKI kann Unterlassungsklage gegen rechtswidrige AGB-Klauseln fuehren
   - Verbraucher muss nicht selbst klagen
   - Urteil wirkt fuer alle betroffenen Verbraucher

3. **VKI-Sammelklage (Streitgenossenschaft)**
   - VKI buendelt gleichartige Einzelansprueche
   - Verbraucher treten ihre Ansprueche an den VKI ab
   - VKI klagt gebuendelt

---

## Step 4: Draft the Appropriate Document

Based on the situation, draft the passende Vorlage:

### Maengelruege — Template:

```
[Name, Adresse des Verbrauchers]

An
[Name des Haendlers / Unternehmens]
[Adresse]

[Ort], am [Datum]

Per Einschreiben / Per E-Mail an [adresse@haendler.at]

Betreff: Gewaehrleistung — Reklamation wegen Mangel
Rechnungsnr. / Bestellnr.: [Nummer]
Kaufdatum: [Datum]

Sehr geehrte Damen und Herren,

am [Kaufdatum] habe ich bei Ihnen [genaue Bezeichnung der Ware, Modell, Artikelnummer]
zum Preis von EUR [Betrag] erworben. Die Lieferung erfolgte am [Lieferdatum].

Bei der Ware liegt folgender Mangel vor:
[Konkrete und detaillierte Beschreibung des Mangels — was genau funktioniert nicht,
wie aeussert sich der Fehler, seit wann]

Gemaess §§922ff ABGB steht mir ein Gewaehrleistungsanspruch zu. Innerhalb der
gesetzlichen Vermutungsfrist des §924 ABGB wird vermutet, dass der Mangel bereits
bei der Uebergabe vorgelegen hat.

Ich mache daher meinen Anspruch auf [Verbesserung (Reparatur) / Austausch
(Ersatzlieferung)] geltend und setze Ihnen hierfuer eine Frist bis zum [Datum — 
mind. 14 Tage ab Zugang].

Sollte eine [Verbesserung/Austausch] innerhalb dieser Frist nicht erfolgen, behalte
ich mir vor, [Preisminderung / Wandlung (Vertragsaufhebung und Rueckerstattung des
Kaufpreises)] gemaess §932 Abs 4 ABGB geltend zu machen und gegebenenfalls
gerichtliche Schritte einzuleiten.

Bitte bestaetigen Sie den Eingang dieses Schreibens und teilen Sie mir den weiteren
Ablauf mit.

Mit freundlichen Gruessen
[Unterschrift]

Beilagen:
- Kopie der Rechnung / des Kaufbelegs
- [Fotos des Mangels]
```

### FAGG-Ruecktrittserklärung — Template:

```
[Name, Adresse des Verbrauchers]

An
[Name des Unternehmens]
[Adresse]

[Ort], am [Datum]

Per E-Mail an [adresse@unternehmen.at] / Per Einschreiben

Betreff: Ruecktritt vom Vertrag gemaess §11 FAGG (Fern- und Auswärtsgeschäfte-Gesetz)
Bestellnr.: [Nummer]
Bestelldatum: [Datum]
Erhalten am: [Lieferdatum]

Sehr geehrte Damen und Herren,

hiermit erklaere ich gemaess §11 des Fern- und Auswärtsgeschäfte-Gesetzes (FAGG) den
Ruecktritt vom Vertrag ueber den Kauf der folgenden Ware(n):

[Genaue Bezeichnung der Ware(n)]

Bestellt am: [Datum]
Erhalten am: [Datum]
Kaufpreis: EUR [Betrag]

Die Ruecktrittsfrist von 14 Tagen ab Erhalt der Ware (§11 Abs 2 Z 1 FAGG) ist
eingehalten. [Alternativ: Mangels ordnungsgemaesser Belehrung ueber das
Ruecktrittsrecht gilt die verlaengerte Frist gemaess §12 FAGG.]

Ich ersuche um Rueckerstattung des Kaufpreises in Hoehe von EUR [Betrag] innerhalb
der gesetzlichen Frist von 14 Tagen (§14 Abs 1 FAGG) auf folgendes Konto:

IBAN: [IBAN]
BIC: [BIC]

Die Ware wird innerhalb von 14 Tagen an Sie zurueckgesendet (§15 Abs 1 FAGG).

[Falls Unternehmer NICHT ueber Ruecksendekosten belehrt hat:]
Da Sie mich nicht ueber die Pflicht zur Tragung der Ruecksendekosten informiert
haben, gehen diese zu Ihren Lasten (§15 Abs 3 FAGG).

Mit freundlichen Gruessen
[Unterschrift]

Beilagen:
- Kopie der Bestellbestaetigung / Rechnung
```

### Einspruch gegen Zahlungsbefehl (als Verbraucher-Beklagter) — Template:

```
An das
Bezirksgericht [Ort]

[Name, Adresse des Einspruchswerbers]
AZ: [Geschaeftszahl]

EINSPRUCH
gegen den Zahlungsbefehl vom [Datum], AZ [Geschaeftszahl]

Gegen den am [Zustelldatum] zugestellten Zahlungsbefehl wird innerhalb offener Frist
(§252 Abs 1 ZPO — 4 Wochen) Einspruch erhoben.

Begruendung:
[Sachverhalt und rechtliche Begruendung, warum die Forderung nicht besteht —
z.B. Gewaehrleistung, Aufrechnung, Nichtlieferung, Betrug]

Beweismittel:
[Auflistung: Urkunden, Zeugen, etc.]

Es wird beantragt, den Zahlungsbefehl aufzuheben und die Klage abzuweisen.

[Ort], am [Datum]
[Unterschrift]
```

---

## Step 5: Present with Timeline and Next Steps

```markdown
# Verbraucherschutz — Verfahren und naechste Schritte

**Verfahrensart:** [Maengelruege / FAGG-Ruecktritt / Schlichtung / Klage / etc.]
**Gegner:** [Haendler/Unternehmen]
**Streitwert:** EUR [Betrag]
**Kaufdatum:** [Datum]

## Fristenübersicht
| Frist | Ablauf | Verbleibend | Status |
|-------|--------|-------------|--------|
| Gewaehrleistung (§933 ABGB) | [Datum] | [x] Monate | OK / KRITISCH / ABGELAUFEN |
| FAGG-Ruecktritt (§11 FAGG) | [Datum] | [x] Tage | OK / KRITISCH / ABGELAUFEN |
| [weitere relevante Fristen] | [Datum] | | |

## Empfohlene Vorgehensweise

### Phase 1: Aussergerichtlich
| Schritt | Frist | Aktion | Status |
|---------|-------|--------|--------|
| 1. Maengelruege / Ruecktritt | sofort | Schreiben absenden (Entwurf unten) | [ ] |
| 2. Antwort abwarten | +14 Tage | Reaktion des Haendlers | [ ] |
| 3. Nachfrist setzen | bei Nichtreaktion | Zweites Schreiben mit Frist | [ ] |

### Phase 2: Schlichtung (bei Scheitern von Phase 1)
| Schritt | Frist | Aktion |
|---------|-------|--------|
| 4. AK-Beratung | jederzeit | Termin bei AK-Konsumentenberatung |
| 5. Schlichtungsstelle | jederzeit | Antrag bei verbraucherrecht.at |

### Phase 3: Gerichtlich (ultima ratio)
| Schritt | Frist | Aktion |
|---------|-------|--------|
| 6. Mahnverfahren/Klage | vor Verjaehrung | Bei BG [Ort] einbringen |
| 7. Vollstreckung | nach Rechtskraft | Exekutionsantrag |

## Kosteneinschaetzung
| Position | Betrag |
|----------|--------|
| Aussergerichtliche Schritte | EUR 0 (Eigenleistung) |
| AK-Beratung | EUR 0 (fuer Mitglieder) |
| Schlichtungsstelle | EUR 0 |
| Mahnverfahren (GGG) | ca. EUR [x] |
| Klage bei BG (GGG) | ca. EUR [x] |
| Anwaltskosten (RATG) | ca. EUR [x] (nur bei LG zwingend) |

## Entwurf des Schriftsatzes
[Hier den konkreten Entwurf einfuegen — Maengelruege, Ruecktrittserklärung, etc.]

## Quellenstatus
| Kategorie | Status | Details |
|-----------|--------|---------|
| RIS MCP | Verfuegbar / Nicht verfuegbar | |
| Gesetze | RIS_VERIFIED / UNVERIFIED | [n] Normen geprueft |
| Judikatur | RIS_VERIFIED / UNVERIFIED | [n] Entscheidungen |
| Pruefdatum | [YYYY-MM-DD] | |

---
Keine Rechtsberatung. Diese Analyse und die Mustervorlagen dienen der Orientierung und ersetzen nicht die Beratung durch einen Rechtsanwalt oder eine Verbraucherberatungsstelle (AK, VKI). Die Muster muessen an den konkreten Einzelfall angepasst werden. Bei hohen Streitwerten oder komplexen Sachverhalten wird anwaltliche Vertretung dringend empfohlen.
```

---

## Critical Rules

1. **Immer zuerst aussergerichtlich** — Keine Klage empfehlen, bevor nicht mindestens eine schriftliche Maengelruege/Ruecktrittserklärung mit Fristsetzung erfolgt ist.
2. **Fristen konkret berechnen** — FAGG 14 Tage, Gewaehrleistung 2/3 Jahre, Verjaehrung 3 Jahre (§1489 ABGB fuer Schadenersatz). Immer konkretes Ablaufdatum nennen.
3. **Zustaendigkeit korrekt** — BG bis €15.000, LG darueber. Verbrauchergerichtsstand §14 KSchG: Wohnsitz des Verbrauchers. IMMER darauf hinweisen.
4. **Anwaltspflicht beachten** — Vor dem BG: keine Anwaltspflicht (§27 ZPO). Vor dem LG: Anwaltspflicht. Das bestimmt die Kostenstruktur.
5. **FAGG-Ruecktritt: Absendetheorie** — Es genuegt, dass die Ruecktrittserklärung am letzten Tag der Frist ABGESENDET wird (§13 Abs 2 FAGG). NICHT Zugang beim Unternehmer.
6. **Maengelruege ist KEINE Frist** — Im B2C gibt es keine Ruegeverpflichtung wie im UGB (§377 UGB gilt nur fuer Kaufleute). Aber: Rasche Ruege ist dennoch ratsam.
7. **Einschreiben oder E-Mail mit Nachweis** — Immer empfehlen, Zugang nachweisen zu koennen. E-Mail mit Lesebestaetigung oder Einschreiben.
8. **AK-Hinweis in jedem Fall** — Die Arbeiterkammer bietet kostenlose Konsumentenberatung. IMMER als erste Anlaufstelle empfehlen.
9. **§§ immer mit Gesetzesname** — §932 ABGB, §11 FAGG, §14 KSchG, §244 ZPO. Nie ohne Gesetzesangabe.
10. **Match user's language** — German in = German out. English in = English out. Gesetze immer in deutscher Originalform.
