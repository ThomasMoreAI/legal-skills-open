---
name: recht-verbraucher-momarcode1
title: /recht verbraucher — Verbraucherschutzrecht (Advisory)
description: Austrian consumer protection law — Gewaehrleistung (§§922ff ABGB, §9 KSchG), warranty vs guarantee, distance selling (FAGG), right of withdrawal (Ruecktrittsrecht), unfair contract terms (§6 KSchG), online shopping disputes, and VKI consumer complaints.
author: MoMarcode1
author_url: https://github.com/MoMarcode1/austrian-legal-claude/tree/main/skills/recht-verbraucher
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: at
practice: consumer
language: de
---

# /recht verbraucher — Verbraucherschutzrecht (Advisory)

When the user describes a consumer protection issue — defective goods, online purchase problems, unfair contract terms, withdrawal from distance contracts, or disputes with businesses — follow these steps exactly.

---

## Step 1: Gather the Facts

Read everything the user has provided. You need:

1. **Who are the parties?** — Verbraucher (§1 KSchG) vs. Unternehmer (§1 KSchG)? Both natural persons? Is this a B2C transaction (KSchG applies) or B2B/C2C (KSchG does NOT apply)?
2. **What was purchased?** — Bewegliche Sache, Dienstleistung, digitale Inhalte (§1 VGG), digitale Dienstleistung? Neu oder gebraucht?
3. **How was it purchased?** — Geschaeftslokal, Fernabsatz (§3 FAGG — Internet, Telefon), ausserhalb von Geschaeftsraeumen (§3 FAGG — Haustuergeschaeft)?
4. **When?** — Kaufdatum, Lieferdatum, wann Mangel entdeckt, wann reklamiert? Alle Daten sind fristenrelevant.
5. **What is the problem?** — Mangel bei Lieferung, Mangel spaeter aufgetreten, Nichtlieferung, falsche Ware, Vertragsklausel unfair, Ruecktritt verweigert?
6. **What has the user already done?** — Maengelruege, schriftliche Reklamation, Ruecktrittserklärung, Kontakt mit Haendler/Hersteller?
7. **What does the user want?** — Reparatur, Austausch, Preisminderung, Wandlung (Geld zurueck), Vertragsruecktritt, Schadenersatz?

If critical information is missing, ask. Be specific:
> "Wann wurde die Ware geliefert? Die Gewaehrleistungsfrist beginnt mit der Uebergabe."
> "Haben Sie online bestellt oder im Geschaeft gekauft? Das bestimmt, ob ein 14-taegiges Ruecktrittsrecht besteht."

Do NOT begin analysis until you have enough facts.

---

## Step 2: RIS Verification

Before proceeding with analysis, follow the **RIS Verification Protocol** (`references/ris-protocol.md`):
1. Check RIS MCP availability
2. For every § you cite in this analysis, verify current wording via RIS
3. For case law references (OGH, HG Wien), retrieve via RIS Justiz
4. Record verification status for the Quellenstatus block
5. If RIS is unavailable, follow the fallback ladder and flag all affected citations

---

## Step 2b: Evidence Assessment (if evidence provided)

If the user has provided documents, photos, emails, witness statements, or other evidence, follow the **Evidence Protocol** (`references/evidence-protocol.md`):
1. Classify each piece of evidence by ZPO hierarchy (Urkunden > Zeugen > Sachverstaendige > Augenschein > Parteienvernehmung)
2. Assess Beweiskraft (probative value) of each piece
3. Identify evidence gaps — what is missing to prove the claim?
4. Determine Beweislast — who must prove what in this situation?
5. Recommend what additional evidence to gather
6. Flag any Beweisnotstand or evidence at risk of loss

If no evidence is provided, skip this step.

---

## Step 3: Classify the Situation

Determine which consumer protection area applies. Go through this systematically:

### A: Gewaehrleistung (§§922-933b ABGB, §9 KSchG)

**When:** Die gelieferte Ware/Dienstleistung hat einen Mangel (weicht vom Vertrag ab).

**Grundsatz:** Der Uebergeber (Verkaeufer) haftet dafuer, dass die Sache bei Uebergabe die bedungenen oder gewoehnlich vorausgesetzten Eigenschaften hat (§922 ABGB).

**Mangelarten:**
- **Sachmangel (§922 Abs 1 ABGB):** Ware weicht von der vereinbarten Beschaffenheit ab, oder ist nicht fuer den gewoehnlichen Gebrauch geeignet, oder entspricht nicht dem, was der Verbraucher aufgrund oeffentlicher Aeusserungen (Werbung) erwarten durfte
- **Rechtsmangel (§923 ABGB):** Dritte haben Rechte an der Sache (z.B. Eigentumsansprueche, Pfandrechte)
- **Montagemangel (§922 Abs 3 ABGB):** Fehlerhafte Montage durch Verkaeufer oder fehlerhafte Montageanleitung

**Beweislastumkehr (§924 ABGB — B2C seit 1.1.2022):**
- Innerhalb von **12 Monaten** ab Uebergabe: Mangel wird VERMUTET, bei Uebergabe bereits vorgelegen zu haben → Unternehmer muss beweisen, dass Ware maengelfrei war
- Nach 12 Monaten: Verbraucher muss beweisen, dass Mangel bei Uebergabe bestand
- Ausnahme: Vermutung gilt nicht, wenn sie mit der Art der Sache oder des Mangels unvereinbar ist

**Gewaehrleistungsfristen (§933 ABGB):**

| Gegenstand | Frist | Beginn |
|-----------|-------|--------|
| Bewegliche Sachen (neu) — B2C | **2 Jahre** | Uebergabe (§933 Abs 1 ABGB) |
| Bewegliche Sachen (gebraucht) — B2C | **1 Jahr** (Verkuerzung auf 1 Jahr zulaessig per Vereinbarung, §9 Abs 1 KSchG) | Uebergabe |
| Unbewegliche Sachen | **3 Jahre** | Uebergabe (§933 Abs 1 ABGB) |
| Digitale Leistungen (einmalig) | **2 Jahre** | Bereitstellung (§9 Abs 2 VGG) |
| Digitale Leistungen (fortlaufend) | Waehrend der gesamten Bereitstellungsdauer | Bereitstellungszeitraum |
| B2B (beweglich) | 2 Jahre (abdingbar) | Uebergabe |

**Stufenmodell der Behelfe (§932 ABGB):**

1. **Primaerbehelfe (erste Stufe):**
   - **Verbesserung** (Reparatur) oder **Austausch** (Ersatzlieferung)
   - Wahlrecht liegt beim Verbraucher
   - Verkaeufer kann den vom Verbraucher gewaehlten Behelf nur verweigern, wenn er unmoeglich oder fuer den Verkaeufer im Vergleich zum anderen Behelf mit unverhaeltnismaessig hohem Aufwand verbunden ist (§932 Abs 3 ABGB)
   - Verbesserung/Austausch muss in **angemessener Frist** und **ohne erhebliche Unannehmlichkeiten** erfolgen (§932 Abs 4 ABGB)
   - Keine Kosten fuer den Verbraucher (Transport, Arbeitszeit, Material)

2. **Sekundaerbehelfe (zweite Stufe) — nur wenn Primaerbehelfe scheitern:**
   - **Preisminderung** (§932 Abs 4 ABGB): Herabsetzung des Kaufpreises im Verhaeltnis zum Minderwert
   - **Wandlung** (§932 Abs 4 ABGB): Aufhebung des Vertrags, Rueckgabe der Ware gegen Rueckerstattung des Kaufpreises
   - Wandlung nur bei **nicht geringfuegigem Mangel** (§932 Abs 4 letzter Satz ABGB)

   Voraussetzungen fuer Sekundaerbehelfe:
   - Verbesserung/Austausch unmoeglich oder
   - Verbesserung/Austausch fuer den Verkaeufer unzumutbar (unverhaeltnismaessig) oder
   - Verkaeufer verweigert Verbesserung/Austausch oder
   - Verbesserung/Austausch nicht in angemessener Frist oder
   - Verbesserung/Austausch mit erheblichen Unannehmlichkeiten verbunden oder
   - Verbesserung/Austausch bereits einmal fehlgeschlagen

**Gewaehrleistung bei digitalen Leistungen (VGG — Verbrauchergewaehrleistungsgesetz):**
- §§1ff VGG: Eigenes Regime fuer digitale Inhalte und digitale Dienstleistungen
- Aktualisierungspflicht des Unternehmers (§7 VGG)
- Sonderregeln fuer Vertragsmaessigkeit (§4 VGG)

### B: Garantie vs. Gewaehrleistung (§9b KSchG)

**WICHTIG:** Garantie und Gewaehrleistung sind verschiedene Rechtsgrundlagen.

| | Gewaehrleistung | Garantie |
|--|----------------|----------|
| **Rechtsgrundlage** | Gesetz (§§922ff ABGB) | Vertrag (freiwillig) |
| **Schuldner** | Verkaeufer | Garantiegeber (oft Hersteller) |
| **Inhalt** | Gesetzlich definiert | Richtet sich nach Garantieerklärung |
| **Verhaeltnis** | Unabdingbar im B2C | Zusaetzlich zur Gewaehrleistung |

**§9b KSchG — Garantie-Transparenz:**
- Garantieerklärung muss klar und verstaendlich sein
- Muss auf die gesetzliche Gewaehrleistung hinweisen
- Muss Inhalt und Bedingungen der Garantie angeben (Dauer, raeumlicher Geltungsbereich, Name und Anschrift des Garantiegebers)
- Garantie darf Gewaehrleistungsrechte NICHT einschraenken

### C: Fernabsatz und ausserhalb von Geschaeftsraeumen geschlossene Vertraege (FAGG)

**Anwendungsbereich (§1 FAGG):**
- Vertraege zwischen Unternehmer und Verbraucher
- Geschlossen im Fernabsatz (§3 Z 2 FAGG: online, telefonisch, per Katalog) ODER ausserhalb von Geschaeftsraeumen (§3 Z 1 FAGG: Haustuergeschaefte, Messen)

**Informationspflichten (§§4-5 FAGG):**
- Wesentliche Eigenschaften der Ware/Dienstleistung
- Gesamtpreis einschl. Steuern und Versandkosten
- Zahlungs-, Liefer- und Leistungsbedingungen
- Bestehen des Ruecktrittsrechts und Bedingungen
- Bei digitalen Inhalten: Funktionalitaet, Kompatibilitaet, technische Schutzmassnahmen
- **Button-Loesung (§8 Abs 2 FAGG):** Online-Bestellbutton muss "zahlungspflichtig bestellen" oder gleichwertige Formulierung tragen

**Ruecktrittsrecht (§11 FAGG):**
- **Frist:** 14 Tage (§11 Abs 1 FAGG)
- **Fristbeginn:**
  - Warenlieferung: ab Erhalt der Ware (§11 Abs 2 Z 1 FAGG)
  - Dienstleistung: ab Vertragsschluss (§11 Abs 2 Z 3 FAGG)
  - Digitale Inhalte (nicht auf koerperlichem Datentraeger): ab Vertragsschluss (§11 Abs 2 Z 3 FAGG)
- **Fristverlaengerung bei fehlender Belehrung:** Wenn der Unternehmer nicht ueber das Ruecktrittsrecht belehrt hat: Frist verlaengert sich um 12 Monate (§12 FAGG) → insgesamt max. 12 Monate + 14 Tage
- **Form:** Keine besondere Form erforderlich, aber eindeutige Erklärung (§13 FAGG). Muster-Widerrufsformular muss vom Unternehmer bereitgestellt werden.
- **Ruecksendekosten:** Traegt der Verbraucher, WENN der Unternehmer darauf hingewiesen hat (§15 Abs 3 FAGG). Sonst: Unternehmer traegt die Kosten.
- **Rueckerstattung:** Unternehmer muss innerhalb von 14 Tagen nach Zugang der Ruecktrittserklärung erstatten (§14 Abs 1 FAGG). Darf Rueckerstattung zurueckhalten bis Ware zurueck oder Nachweis der Ruecksendung (§14 Abs 3 FAGG).

**Ausnahmen vom Ruecktrittsrecht (§18 FAGG):**
1. Nach Verbraucher-Spezifikation angefertigte Waren (§18 Abs 1 Z 1 FAGG)
2. Schnell verderbliche Waren (§18 Abs 1 Z 2 FAGG)
3. Versiegelte Waren, die aus Hygiene-/Gesundheitsgruenden nicht zur Rueckgabe geeignet sind, wenn Versiegelung entfernt (§18 Abs 1 Z 4 FAGG)
4. Versiegelte Audio-/Video-/Softwareaufnahmen, wenn entsiegelt (§18 Abs 1 Z 5 FAGG)
5. Zeitungen, Zeitschriften (§18 Abs 1 Z 6 FAGG)
6. Dienstleistungen, wenn vollstaendig erbracht und Verbraucher vorher ausdruecklich zugestimmt hat (§18 Abs 1 Z 11 FAGG)
7. Digitale Inhalte (nicht auf koerperlichem Datentraeger), wenn Bereitstellung mit ausdruecklicher Zustimmung und Kenntnisnahme des Verlusts des Ruecktrittsrechts begonnen hat (§18 Abs 1 Z 13 FAGG)

### D: Klauselkontrolle (§6 KSchG)

**Nichtige Klauseln (§6 Abs 1 KSchG) — absolut verboten:**
- Z 1: Einseitiges Ruecktrittsrecht des Unternehmers
- Z 2: Einseitiges Leistungsaenderungsrecht des Unternehmers ohne wichtigen Grund
- Z 3: Kurzfristige Vertragsbindung des Verbrauchers bei langfristiger Bindung des Unternehmers
- Z 5: Ausschluss oder Einschraenkung der Gewaehrleistung
- Z 9: Verbot der Aufrechnung
- Z 10: Zu kurze Fristen fuer Maengelruege
- Z 14: Beweislastumkehr zum Nachteil des Verbrauchers
- Z 15: Gerichtsstandsklausel ausserhalb des Wohnorts des Verbrauchers
- und weitere Z 1-18

**Kontrolle nach §6 Abs 2 KSchG — relativ verboten (intransparent/ueberraschend):**
- Klauseln, die den Verbraucher benachteiligen und nicht klar/verstaendlich sind

**Kontrolle nach §6 Abs 3 KSchG — geltungserhaltende Reduktion:**
- Findet im oesterreichischen Recht grundsaetzlich NICHT statt
- Nichtige Klausel wird ersatzlos gestrichen, nicht auf zulaessiges Mass reduziert
- OGH-Judikatur bestaetigt dies konsequent

**§879 Abs 3 ABGB — AGB-Inhaltskontrolle:**
- Zusaetzlich zu §6 KSchG: Klauseln in AGB, die einen Teil gröblich benachteiligen (auch B2B!)
- Kontrollmassstab: Dispositives Recht als Leitbild

### E: Produkthaftung (PHG — Produkthaftungsgesetz)

**Anwendungsbereich:**
- Haftung des Herstellers (nicht des Verkaeufers!) fuer Schaeden durch fehlerhafte Produkte (§1 PHG)
- Verschuldensunabhaengige Haftung (Gefaehrdungshaftung)

**Fehlerbegriff (§5 PHG):**
- Produkt bietet nicht die Sicherheit, die berechtigterweise erwartet werden darf
- Beruecksichtigung: Darbietung, vernuenftigerweise erwartbarer Gebrauch, Zeitpunkt des Inverkehrbringens

**Ersatzfaehige Schaeden (§1 PHG):**
- Personenschaeden (Koerperverletzung, Tod)
- Sachschaeden an anderen Sachen als dem fehlerhaften Produkt selbst (Selbstbehalt: €500, §2 PHG)
- NICHT: Schaden am fehlerhaften Produkt selbst (→ das ist Gewaehrleistung)

**Haftende Personen (§§1, 3 PHG):**
- Hersteller, Quasi-Hersteller (Eigenmarke), Importeur in die EU
- Subsidiaer: Lieferant, wenn Hersteller nicht feststellbar (§1 Abs 2 PHG)

**Fristen (§§12-13 PHG):**
- Verjaehrung: 3 Jahre ab Kenntnis von Schaden, Fehler und Hersteller (§12 PHG)
- Absolute Frist: 10 Jahre ab Inverkehrbringen (§13 PHG)

### F: Online-Streitbeilegung (ODR) und VKI

**ODR-Plattform (EU VO 524/2013):**
- Online-Streitbeilegungsplattform der EU fuer grenzueberschreitende Online-Kaeufe
- Unternehmer mit Online-Shop muessen Link zur ODR-Plattform bereitstellen

**Verein fuer Konsumenteninformation (VKI):**
- Fuehrt Musterklagen und Verbandsklagen im Verbraucherinteresse
- Rechtsberatung fuer Konsumenten (teilweise kostenlos fuer AK-Mitglieder)
- VKI-Klagsverband: Kann Unterlassungsklagen gegen rechtswidrige AGB-Klauseln fuehren (§28 KSchG — Verbandsklage)

**Schlichtungsstelle fuer Verbrauchergeschaefte:**
- Alternative Streitbeilegung (§4 AStG — Alternative-Streitbeilegung-Gesetz)
- Zustaendig fuer inlaendische B2C-Streitigkeiten
- Teilnahme fuer Unternehmer grundsaetzlich freiwillig (ausser bei regulierten Branchen wie Energie, Telekom)

---

## Step 4: Apply the Law to the Facts

For the identified situation, analyze systematically:

### Bei Gewaehrleistung:
1. **Liegt ein Mangel vor?** — Abweichung von der vereinbarten oder gewoehnlich vorausgesetzten Beschaffenheit?
2. **Bestand der Mangel bei Uebergabe?** — Beweislastumkehr (§924 ABGB) innerhalb von 12 Monaten?
3. **Ist die Gewaehrleistungsfrist noch offen?** — 2 Jahre (neu), 1 Jahr (gebraucht, B2C vereinbart), 3 Jahre (Immobilien)?
4. **Welche Behelfe stehen zu?** — Primaer (Verbesserung/Austausch) → Sekundaer (Preisminderung/Wandlung)
5. **Schadenersatz zusaetzlich?** — §933a ABGB: Bei Verschulden des Verkaeufers auch Mangelfolgeschaeden

### Bei FAGG-Ruecktritt:
1. **Ist das FAGG anwendbar?** — Fernabsatz oder Haustuergeschaeft? B2C?
2. **Liegt eine Ausnahme nach §18 FAGG vor?**
3. **Ist die 14-Tage-Frist noch offen?** — Fristbeginn pruefen. Bei fehlender Belehrung: 12 Monate + 14 Tage.
4. **Wurde korrekt zurueckgetreten?** — Form, Erklärung
5. **Wer traegt Ruecksendekosten?** — Hat der Unternehmer belehrt?

### Bei Klauselkontrolle (§6 KSchG):
1. **Ist das KSchG anwendbar?** — B2C-Vertrag?
2. **Jede beanstandete Klausel einzeln pruefen** gegen §6 Abs 1 Z 1-18 KSchG
3. **§879 Abs 3 ABGB** — Gröbliche Benachteiligung in AGB?
4. **Transparenzgebot (§6 Abs 3 KSchG)** — Klar und verstaendlich?
5. **Rechtsfolge:** Nichtigkeit der Klausel, KEINE geltungserhaltende Reduktion

---

## Step 5: Present Results

```markdown
# Verbraucherschutzrechtliche Analyse

**Sachverhalt:** [2-3 Saetze Zusammenfassung]
**Rechtsverhaeltnis:** Verbraucher (§1 KSchG) vs. Unternehmer
**Kaufdatum / Lieferdatum:** [Datum]
**Betroffenes Rechtsgebiet:** [Gewaehrleistung / FAGG / KSchG-Klauselkontrolle / PHG / Kombination]

## Rechtliche Beurteilung

### [Hauptfrage — z.B. "Gewaehrleistungsanspruch"]

**Anspruchsgrundlage:** §[x] ABGB / KSchG / FAGG / PHG
**Tatbestandsmerkmale:**
| Voraussetzung | Status | Begruendung |
|--------------|--------|-------------|
| [z.B. Mangel bei Uebergabe] | OK / OFFEN / NICHT ERFUELLT | [Begruendung] |
| [z.B. Frist eingehalten] | OK / OFFEN / NICHT ERFUELLT | [Begruendung] |

**Ergebnis:** [Klare Aussage: Anspruch besteht / besteht voraussichtlich / besteht nicht]

### Zustaendige Behelfe
| Behelf | Zulaessig? | Begruendung |
|--------|-----------|-------------|
| Verbesserung (Reparatur) | Ja/Nein | §932 Abs 2 ABGB |
| Austausch | Ja/Nein | §932 Abs 2 ABGB |
| Preisminderung | Ja/Nein | §932 Abs 4 ABGB — nur wenn Primaerbehelf gescheitert |
| Wandlung | Ja/Nein | §932 Abs 4 ABGB — nur bei nicht geringfuegigem Mangel |
| Schadenersatz | Ja/Nein | §933a ABGB — bei Verschulden |

## Fristen
| Frist | Ablauf | Verbleibend | Status |
|-------|--------|-------------|--------|
| Gewaehrleistung (§933 ABGB) | [Datum] | [x] Monate | OK / KRITISCH / ABGELAUFEN |
| FAGG-Ruecktritt (§11 FAGG) | [Datum] | [x] Tage | OK / KRITISCH / ABGELAUFEN |

## Handlungsempfehlung

### Sofortige Schritte
1. [Erster konkreter Schritt — z.B. "Schriftliche Maengelruege an den Verkaeufer"]
2. [Zweiter Schritt — z.B. "Frist setzen: 14 Tage fuer Verbesserung/Austausch"]
3. [Dritter Schritt]

### Wenn der Haendler nicht reagiert
1. [Eskalation — z.B. "Schlichtungsstelle einschalten"]
2. [Klage bei BG/LG"]

### Anlaufstellen
- **Arbeiterkammer (AK):** Kostenlose Konsumentenberatung fuer AK-Mitglieder
- **VKI:** Verein fuer Konsumenteninformation — Rechtsberatung und Musterklagen
- **Europaeisches Verbraucherzentrum (EVZ):** Bei grenzueberschreitenden Kaeufen innerhalb der EU
- **Schlichtungsstelle fuer Verbrauchergeschaefte:** Alternative Streitbeilegung

## Quellenstatus
| Kategorie | Status | Details |
|-----------|--------|---------|
| RIS MCP | Verfuegbar / Nicht verfuegbar | |
| Gesetze | RIS_VERIFIED / UNVERIFIED | [n] Normen geprueft |
| Judikatur | RIS_VERIFIED / UNVERIFIED | [n] Entscheidungen |
| Pruefdatum | [YYYY-MM-DD] | |

---
Keine Rechtsberatung. Diese Analyse dient der rechtlichen Ersteinschaetzung und ersetzt nicht die Beratung durch einen Rechtsanwalt oder eine Verbraucherberatungsstelle (AK, VKI). Insbesondere bei hohen Streitwerten oder komplexen Sachverhalten wird anwaltliche Vertretung empfohlen.
```

---

## Critical Rules

1. **KSchG nur bei B2C** — Das Konsumentenschutzgesetz gilt NUR fuer Vertraege zwischen Unternehmer und Verbraucher (§1 KSchG). Bei B2B oder C2C gelten nur die allgemeinen ABGB-Regeln. Immer zuerst pruefen.
2. **Gewaehrleistung ≠ Garantie** — IMMER klarstellen, dass Gewaehrleistung (gesetzlich, gegen den Verkaeufer) und Garantie (freiwillig, meist vom Hersteller) verschiedene Rechtsgrundlagen sind. Verbraucher verwechseln das staendig.
3. **Beweislastumkehr: 12 Monate** — Seit 1.1.2022 betraegt die Beweislastumkehr im B2C 12 Monate (§924 ABGB), nicht 6 Monate wie frueher. Aktuelle Rechtslage beachten.
4. **Stufenmodell einhalten** — Der Verbraucher kann NICHT sofort Geld zurueck verlangen (Wandlung). Erst Verbesserung/Austausch, dann Preisminderung/Wandlung. Ausnahme: wenn Primaerbehelf gescheitert, verweigert, oder unzumutbar.
5. **FAGG-Ausnahmen genau pruefen** — §18 FAGG listet viele Ausnahmen vom Ruecktrittsrecht auf. Jede einzelne pruefen, bevor man dem Verbraucher ein Ruecktrittsrecht zusichert.
6. **Keine geltungserhaltende Reduktion** — Im oesterreichischen Recht werden nichtige AGB-Klauseln NICHT auf das zulaessige Mass reduziert, sondern ersatzlos gestrichen. OGH-staendige Rechtsprechung.
7. **Fristen konkret berechnen** — Gewaehrleistungsfrist, FAGG-Ruecktrittsfrist, Verjaehrungsfrist immer mit konkretem Ablaufdatum angeben.
8. **§§ immer mit Gesetzesname** — §922 ABGB, nicht nur "§922". §6 KSchG, nicht nur "§6". §11 FAGG, nicht nur "§11".
9. **Arbeiterkammer-Hinweis** — Bei Verbraucherthemen IMMER auf die kostenlose AK-Konsumentenberatung hinweisen.
10. **Match user's language** — German in = German out. English in = English out. Gesetze immer in deutscher Originalform zitieren.
