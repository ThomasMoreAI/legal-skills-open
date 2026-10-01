---
name: recht-arbeit-momarcode1
title: /recht arbeit — Arbeitsrechtliche Analyse
description: Austrian employment law analysis — employment contracts, KollV identification and classification, working time (AZG), vacation (UrlG), termination (AngG §20), dismissal protection (ArbVG §105), non-compete (AngG §36), All-in clauses, Abfertigung, parental leave (MSchG/VKG), and discrimination (GlBG).
author: MoMarcode1
author_url: https://github.com/MoMarcode1/austrian-legal-claude/tree/main/skills/recht-arbeit
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: at
practice: employment
language: de
---

# /recht arbeit — Arbeitsrechtliche Analyse

When the user describes an employment law situation and wants to know their rights, obligations, claims, or risks under Austrian law, follow these steps.

---

## Step 1: Gather the Facts

Read what the user has provided. You need:

1. **Employment relationship type** — Angestellte/r (AngG), Arbeiter/in (GewO alt / now mostly AngG since 1.7.2021 Angleichung), freier Dienstnehmer, Werkvertrag, Leiharbeit (AUeG)?
2. **Which side?** — Arbeitnehmer (AN) or Arbeitgeber (AG)? This changes the analysis perspective.
3. **Applicable KollV** — Which Kollektivvertrag applies? Industry/Branche, Fachverband? If unclear, ask:
   > "In welcher Branche sind Sie beschaeftigt? Das ist wichtig, um den anwendbaren Kollektivvertrag zu bestimmen."
4. **Contract details** — Schriftlicher Dienstvertrag vorhanden? Dienstzettel (§2 AVRAG)? All-in-Klausel? Konkurrenzklausel? Probemonat?
5. **Employment duration** — Eintrittsdatum, Vordienstzeiten (relevant fuer Kuendigungsfristen, Urlaub, Abfertigung)
6. **Working time arrangement** — Vollzeit/Teilzeit, Normalarbeitszeit, Gleitzeitvereinbarung, Durchrechnungszeitraum, Ueberstunden?
7. **Remuneration** — Bruttogehalt, Sonderzahlungen (13./14. Gehalt), Zulagen, Praemien, KV-Einstufung
8. **Current issue** — Kuendigung, Entlassung, Ueberstunden, Urlaub, Karenz, Diskriminierung, Dienstzeugnis, etc.?
9. **Betriebsrat** — Gibt es einen Betriebsrat im Unternehmen?
10. **Timeline** — Wann ist was passiert? Gibt es laufende Fristen?

If critical information is missing, ask. Be specific:
> "Seit wann besteht das Dienstverhaeltnis? Das bestimmt die Kuendigungsfrist und den Abfertigungsanspruch."

---

## Step 2: RIS Verification

Before proceeding with analysis, follow the **RIS Verification Protocol** (`references/ris-protocol.md`):
1. Check RIS MCP availability
2. For every § you cite in this analysis, verify current wording via RIS
3. For case law references, retrieve via RIS Justiz (OGH Arbeitsrechtssachen — 8 ObA, 9 ObA)
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

## Step 3: Qualify the Employment Relationship

### A: Echtes Dienstverhaeltnis vs. freier Dienstvertrag vs. Werkvertrag

This is fundamental — the entire analysis depends on it. Apply the OGH criteria:

| Merkmal | Echtes DV | Freier DV | Werkvertrag |
|---------|-----------|-----------|-------------|
| Persoenliche Arbeitsleistung | Ja, persoenlich | Grundsaetzlich persoenlich, Vertretung moeglich | Vertretung frei |
| Weisungsgebundenheit | Ja (persoenlich + sachlich) | Nur sachlich | Nein |
| Eingliederung in Betriebsorganisation | Ja | Teilweise | Nein |
| Arbeitszeit/-ort vorgegeben | Ja | Teilweise | Nein |
| Eigene Betriebsmittel | Nein (AG stellt bereit) | Teilweise | Ja |
| Unternehmerisches Risiko | Nein | Nein | Ja |
| Geschuldete Leistung | Dauerschuld (Arbeitszeit) | Dauerschuld | Werkserfolg |

**Scheinselbstaendigkeit (§539a ASVG):**
- Wenn die tatsaechliche Durchfuehrung des Vertrags dem Bild eines echten DV entspricht, liegt unabhaengig von der Vertragsbezeichnung ein echtes DV vor
- Folge: Nachforderung von SV-Beitraegen (AG-Anteil!), Lohnsteuer, DB/DZ
- OGH: "Der wahre wirtschaftliche Gehalt und nicht die aeussere Erscheinungsform ist massgebend" (§539a Abs 1 ASVG)
- Pruefreihenfolge: Vertragsinhalt → tatsaechliche Durchfuehrung → wirtschaftlicher Gehalt

### B: Angestellte/r oder Arbeiter/in?

Seit 1.7.2021 weitgehend angeglichen (Kuendigungsfristen, Entgeltfortzahlung). Unterschiede bestehen noch bei:
- Anwendbarer KollV
- Teilweise bei Abfertigung Alt (Uebergangsrecht)
- Gewerbeordnung vs. AngG als Rechtsgrundlage

### C: Sonderformen

- **Leiharbeit (AUeG):** Ueberlasser ist Arbeitgeber, aber Beschaeftiger hat Fuersorgepflichten. AN hat Anspruch auf gleiches Entgelt wie vergleichbare Stamm-AN beim Beschaeftiger (§10 Abs 1 AUeG).
- **Teilzeit (§19d AZG):** Diskriminierungsverbot gegenueber Vollzeit-AN. Mehrarbeit nur bei Vereinbarung und mit 25% Zuschlag (§19d Abs 3f AZG), sofern kein Durchrechnungszeitraum.
- **Geringfuegig Beschaeftigte:** Gleiche arbeitsrechtliche Ansprueche (Urlaub, Kuendigungsschutz, KollV-Mindestgehalt) — nur SV-rechtlich anders behandelt.
- **Geschaeftsfuehrer:** Freier Dienstvertrag oder echtes DV? Haengt von der tatsaechlichen Gestaltung ab. GmbH-GF mit >25% Beteiligung: kein ASVG, sondern GSVG.

---

## Step 4: Identify the Applicable Kollektivvertrag (KollV)

### A: Welcher KollV gilt?

1. **Fachverband des Arbeitgebers** bestimmt den anwendbaren KollV (§9 ArbVG)
2. Pruefen: Ist der AG Mitglied der Wirtschaftskammer? → KollV gilt automatisch
3. Satzungserklaerung (§18 ArbVG): KollV kann auch fuer Nicht-Mitglieder gelten
4. Haeuufige KollV:
   - **IT-KV** (Fachverband UBIT): Verwendungsgruppen ST1-ST2 (Spezial), AT (Allgemein)
   - **Handel-KV**: Beschaeftigungsgruppen 1-7
   - **Metallindustrie-KV**: Umfangreich, mit Ist-Lohn-Erhoehungen
   - **Gastgewerbe-KV**: Besondere Arbeitszeitregeln, Trinkgeld-Thematik
   - **Bauindustrie/Baugewerbe-KV**: BUAK-System, Schlechtwetterentschaedigung

### B: KV-Einstufung (Verwendungsgruppe/Beschaeftigungsgruppe)

- Richtige Einstufung anhand der **tatsaechlich ausgeuebten Taetigkeit**, nicht der Vertragsbezeichnung (OGH 9 ObA 91/03w)
- Pruefe: Stimmt die vertragliche Einstufung mit der tatsaechlichen Taetigkeit ueberein?
- Vorrrueckungen: KV regelt Biennalspruenge / Zeitvorrrueckungen
- **KV-Mindestgehalt:** Das tatsaechliche Gehalt (inkl. aller Zulagen, aber exkl. Sonderzahlungen und Ueberstundenpauschale) muss mindestens das KV-Mindestgehalt der richtigen Verwendungsgruppe und Stufe erreichen

### C: KV-Differenzansprueche

Wenn Unterzahlung vorliegt:
- Differenz zwischen IST-Gehalt und KV-Mindestgehalt (inklusive richtiger Einstufung und Vorrrueckung)
- Verjaehrung: 3 Jahre (§1486 Z 5 ABGB)
- Anspruch auch auf Sonderzahlungen in der richtigen Hoehe
- Achtung: Ueberstundenpauschale oder All-in-Aufschlag darf nicht auf das KV-Mindestgehalt angerechnet werden, wenn dadurch das Grundgehalt unter KV faellt

---

## Step 5: Analyse the Specific Issue

Go through all relevant Teilbereiche:

### A: Arbeitszeit (AZG)

**Normalarbeitszeit:**
- §3 AZG: 8 Stunden taeglich, 40 Stunden woechentlich (gesetzlich; KollV kann reduzieren, z.B. 38,5h)
- §4 AZG: Andere Verteilung durch KollV/BV/Einzelvereinbarung moeglich

**Ueberstunden:**
- §6 AZG: Arbeit ueber die Normalarbeitszeit hinaus
- Zuschlag: 50% (§10 Abs 1 AZG); Sonn-/Feiertagsarbeit: 100% (Zuschlag nach KollV pruefen!)
- Hoechstgrenzen: 12 Stunden taeglich / 60 Stunden woechentlich (§7 AZG seit 12-Stunden-Tag-Novelle 2018)
- Durchschnitt ueber 17 Wochen: max. 48 Stunden/Woche (§7 Abs 4 AZG — EU-Arbeitszeitrichtlinie)

**Gleitzeit (§4b AZG):**
- Schriftliche Gleitzeitvereinbarung erforderlich
- Gleitzeitrahmen: max. 13 Stunden taeglich (§4b Abs 4 AZG nach Novelle 2018)
- Gleitzeitperiode: Zeitraum fuer den Durchschnitt
- Ueberstunden erst bei Ueberschreitung der Normalarbeitszeit in der Gleitzeitperiode

**Durchrechnung (§4 Abs 6 AZG):**
- KollV kann Durchrechnungszeitraeume erlauben (z.B. 13 Wochen, 26 Wochen, 52 Wochen)
- Innerhalb des Zeitraums: Ausgleich, keine Ueberstundenzuschlaege
- Ueberstunden erst bei Ueberschreitung am Ende des Durchrechnungszeitraums

**All-in-Klausel:**
- Gesetzlich nicht geregelt, aber durch OGH-Judikatur anerkannt
- **Deckungspruefung:** Jaehrlich pruefen, ob das All-in-Gehalt die tatsaechlich geleisteten Ueberstunden (inkl. 50%/100% Zuschlag) plus das KV-Mindestgehalt abdeckt
- Wenn nicht → Differenzanspruch des AN (3 Jahre Verjaehrung)
- OGH 8 ObA 13/12y: Transparenzgebot — AN muss erkennen koennen, welcher Teil des Gehalts die Normalarbeitszeit und welcher die Ueberstunden abdeckt
- All-in muss im Dienstvertrag klar vereinbart sein

### B: Urlaub (UrlG)

**Anspruch:**
- §2 UrlG: 30 Werktage (= 5 Wochen bei 6-Tage-Woche) pro Arbeitsjahr
- Ab 25 Dienstjahren (inkl. anrechenbare Vordienstzeiten): 36 Werktage (= 6 Wochen)
- Urlaubsjahr = Arbeitsjahr (ab Eintritt), nicht Kalenderjahr

**Vordienstzeiten (§3 UrlG):**
- Anrechenbar: Inlaendische DV (max. 5 Jahre), Selbstaendigkeit (max. 5 Jahre), Studium (max. 5 Jahre), Auslandszeiten nach EuGH-Judikatur
- Seit EuGH C-514/12 (Salzburger Landeskliniken): Diskriminierung durch Beschraenkung auf Inlandszeiten ist unionsrechtswidrig
- Pruefen: Alle Zeiten zusammenrechnen, ob 25-Jahre-Grenze fuer 6. Urlaubswoche erreicht wird

**Verbrauch:**
- Vereinbarung zwischen AG und AN erforderlich (§4 UrlG)
- AG darf Urlaub nicht einseitig anordnen
- AN darf nicht einseitig in Urlaub gehen
- Verfall: 2 Jahre nach Ende des Urlaubsjahres (§4 Abs 5 UrlG)

**Urlaubsersatzleistung (UEL):**
- §10 UrlG: Bei Beendigung des DV — offener Urlaub wird finanziell abgegolten
- Berechnung: Offene Urlaubstage x Tagesentgelt (inkl. Sonderzahlungsanteil, Ueberstundendurchschnitt)
- Aliquotierung: Nur im laufenden Urlaubsjahr aliquot; fruehere Urlaubsjahre: voller Anspruch
- Bei Entlassung aus Verschulden des AN: Nur aliquoter Anspruch fuer laufendes Urlaubsjahr (§10 Abs 2 UrlG)

### C: Kuendigung

#### AG-Kuendigung (§20 AngG — Angestellte):

**Kuendigungsfristen:**

| Dienstjahre | Kuendigungsfrist |
|-------------|-----------------|
| Bis 2 Jahre | 6 Wochen |
| 2-5 Jahre | 2 Monate |
| 5-15 Jahre | 3 Monate |
| 15-25 Jahre | 4 Monate |
| Ab 25 Jahre | 5 Monate |

- Seit 1.10.2021 auch fuer Arbeiter (Angleichung, §1159 ABGB)
- Kuendigungstermin: Quartalsende (31.3., 30.6., 30.9., 31.12.) ODER 15./Letzter des Monats, wenn vertraglich oder per KV vereinbart (§20 Abs 2 AngG)
- KollV pruefen: Oft Kuendigung zum Monatsletzten zulaessig

**AN-Kuendigung (§20 Abs 4 AngG):**
- Frist: 1 Monat zum Monatsletzten (wenn nicht anders vereinbart)
- KollV kann abweichende Regelung vorsehen

#### Entlassung (§27 AngG):

Fristlose Beendigung durch AG bei wichtigem Grund. Taxative Gruende in §27 AngG:
- Z 1: Untreue, Vertrauensmissbrauch
- Z 3: Unfaehigkeit oder Arbeitsunwilligkeit
- Z 4: Trunkenheit, wenn sie die Dienstleistung erheblich beeintraechtigt
- Z 6: Beharrliche Pflichtverletzung

**Achtung:** Entlassung muss **unverzoegerlich** nach Bekanntwerden des Grundes ausgesprochen werden (OGH: idR wenige Tage). Verspaetete Entlassung = unwirksam → gilt als Kuendigung.

#### Vorzeitiger Austritt (§26 AngG):

Fristlose Beendigung durch AN bei wichtigem Grund:
- Z 1: AN kann die Arbeit nicht ohne Schaden fuer Gesundheit fortsetzen
- Z 2: AG erbringt vertragliche Leistungen nicht (Gehalt!)
- Z 3: AG verletzt wesentliche Vertragspflichten

**Folge berechtigter Entlassung/berechtigten Austritts:**
- Wie bei normaler Kuendigung: Urlaubsersatzleistung, Abfertigung (alt), Kuendigungsentschaedigung (§29 AngG)
- Bei **unberechtigter Entlassung:** AN bekommt Kuendigungsentschaedigung = Entgelt bis zum fiktiven Kuendigungsende + UEL + Sonderzahlungen
- Bei **unberechtigtem Austritt:** AN schuldet AG Schadenersatz

### D: Kuendigungsschutz

#### Allgemeiner Kuendigungsschutz (§105 ArbVG):

Nur in Betrieben mit Betriebsrat! Ablauf:
1. AG muss BR vor Kuendigung **verstaendigen** (§105 Abs 1 ArbVG)
2. BR hat 5 Werktage zur Stellungnahme: Zustimmung / Widerspruch / Schweigen
3. AG darf Kuendigung erst nach Ablauf der 5-Tage-Frist aussprechen (oder frueher bei Zustimmung)
4. Bei BR-Widerspruch: AN kann Kuendigung beim ASG **anfechten** (§105 Abs 3 ArbVG) — Frist: 2 Wochen!

Anfechtungsgruende:
- **Motivkuendigung (§105 Abs 3 Z 1 ArbVG):** Kuendigung wegen Beitritt zur Gewerkschaft, Kandidatur als BR, Geltendmachung von Anspruechen, etc.
- **Sozialwidrigkeit (§105 Abs 3 Z 2 ArbVG):** Kuendigung beeintraechtigt wesentliche Interessen des AN, AUSSER AG kann betriebliche Erfordernisse nachweisen UND kein geeigneter Ersatzarbeitsplatz

#### Besonderer Kuendigungsschutz:

| Geschuetzte Gruppe | Rechtsgrundlage | Schutz |
|-------------------|-----------------|--------|
| Schwangere / Muetter bis 4 Monate nach Entbindung | §10 MSchG | Kuendigung und Entlassung nur mit Zustimmung des Gerichts |
| Eltern in Karenz | §10 Abs 3 MSchG, §7 Abs 3 VKG | Kuendigungs- und Entlassungsschutz ab Bekanntgabe bis 4 Wochen nach Ende der Karenz |
| Elternteilzeit | §15n MSchG / §8h VKG | Kuendigungsschutz waehrend der Elternteilzeit |
| Praesenz-/Zivildiener | §12 APSG | Kuendigung waehrend und 1 Monat danach unwirksam |
| Behinderte (Behindertenpass) | §8 BEinstG | Kuendigung nur mit Zustimmung des Behindertenausschusses (nach 4 Jahren im Betrieb oder nach 6 Monaten bei Behinderung > 70%) |
| Betriebsratsmitglieder | §120 ArbVG | Kuendigung und Entlassung nur mit Zustimmung des Gerichts |
| Lehrlinge | §15 BAG | Besonderer Kuendigungsschutz, Mediation |

### E: Konkurrenzklausel (§36 AngG)

Seit 29.12.2015 (Novelle):
- **Entgeltgrenze:** Nur gueltig, wenn das letzte Monatsentgelt (brutto) ueber dem 20-fachen der taeglichen ASVG-Hoechstbeitragsgrundlage liegt. Aktuellen Wert pruefen!
- **Maximale Dauer:** 1 Jahr nach Beendigung des DV (§36 Abs 1 AngG)
- **Entfall bei AG-Kuendigung:** Die Konkurrenzklausel entfaellt, wenn der AG kuendigt (§36 Abs 2 AngG) — AUSSER der AG erklaert sich bereit, waehrend der Dauer der Konkurrenzklausel das volle Entgelt weiterzuzahlen
- **Entfall bei berechtigtem Austritt** des AN
- **Konventionalstrafe:** Richterliches Maessigungsrecht (§37 Abs 2 AngG)
- Ueberpruefung: Ist die Klausel sachlich und oertlich angemessen?

### F: Abfertigung

#### Abfertigung Alt (AngG §23/§23a — DV begonnen vor 1.1.2003):

| Dienstjahre | Abfertigung |
|-------------|-------------|
| 3 Jahre | 2 Monatsentgelte |
| 5 Jahre | 3 Monatsentgelte |
| 10 Jahre | 4 Monatsentgelte |
| 15 Jahre | 6 Monatsentgelte |
| 20 Jahre | 9 Monatsentgelte |
| 25 Jahre | 12 Monatsentgelte |

- Nur bei AG-Kuendigung, einvernehmlicher Aufloesung, berechtigtem Austritt, unberechtigter Entlassung
- NICHT bei AN-Kuendigung (Ausnahmen: Mutterschaft §23a Abs 3 AngG, Inanspruchnahme Pension)
- Berechnung: Letztes Monatsentgelt inkl. Sachbezuege, Provisionen (Durchschnitt), anteilige SZ

#### Abfertigung Neu (BMSVG — DV begonnen ab 1.1.2003):

- AG zahlt 1,53% des monatlichen Entgelts in eine Betriebliche Vorsorgekasse (BV-Kasse) ein (§6 BMSVG)
- Anspruch auf Auszahlung: Nach mindestens 3 Beitragsjahren bei AG-Kuendigung, einvernehmlicher Aufloesung, berechtigtem Austritt, unberechtigter Entlassung (§14 BMSVG)
- Bei AN-Kuendigung: Kein Auszahlungsanspruch, Anwartschaft bleibt aber in der BV-Kasse erhalten und kann spaeter uebertragen oder bei Pensionsantritt ausgezahlt werden
- Wahlrecht: AN kann sich das Guthaben auszahlen lassen (6% Lohnsteuer statt normal) ODER als Rente beziehen ODER in eine Pensionskasse uebertragen (§17 BMSVG)

### G: Elternschaft (MSchG / VKG)

**Mutterschutz (MSchG):**
- Absolutes Beschaeftigungsverbot: 8 Wochen vor und 8 Wochen nach dem errechneten Geburtstermin (§3/§5 MSchG)
- Vorzeitiges Beschaeftigungsverbot: Bei Gefahr fuer Mutter/Kind (aerztliches Attest, §3 Abs 3 MSchG)
- Wochengeld: 100% des durchschnittlichen Nettoentgelts der letzten 3 Monate (§162 ASVG)

**Karenz (MSchG §15 / VKG §2):**
- Anspruch: Bis zum 2. Geburtstag des Kindes
- Teilung zwischen den Elternteilen moeglich (mind. 2 Monate am Stueck)
- Meldepflicht: Spaetestens am Ende des Beschaeftigungsverbots bzw. 3 Monate vor Antritt (§15 Abs 3 MSchG / §3 VKG)
- Kuendigungsschutz: Beginnt mit Bekanntgabe der Karenz (fruehestens 4 Monate vor Antritt) und endet 4 Wochen nach Ende der Karenz

**Elternteilzeit (§15h-15p MSchG / §8-8i VKG):**
- Rechtsanspruch: In Betrieben mit mehr als 20 AN UND DV besteht seit 3 Jahren (§15h Abs 1 MSchG)
- Ohne Rechtsanspruch: Vereinbarung mit AG moeglich (§15i MSchG)
- Dauer: Bis zum 7. Geburtstag des Kindes (Rechtsanspruch) / 8. Geburtstag (Vereinbarung)
- Mindestarbeitszeit: 12 Stunden/Woche
- Verfahren bei Ablehnung: AN kann beim ASG klagen (§15j MSchG)

**Papamonat (Familienzeitbonus, §2 FAMZG):**
- 31 Tage innerhalb der ersten 91 Tage nach Geburt
- AN muss AG 3 Monate vorher informieren (§2 Abs 2 FAMZG)

### H: Gleichbehandlung (GlBG)

**Diskriminierungsverbot (§§3-7 GlBG):**
- Geschlecht, Alter, ethnische Zugehoerigkeit, Religion/Weltanschauung, sexuelle Orientierung
- Umfasst: Begruendung des DV, Entgelt, Befoerderung, Arbeitsbedingungen, Beendigung

**Sexuelle Belaestigung (§6 GlBG):**
- AG hat Fuersorgepflicht — muss bei Belaestigung durch Vorgesetzte/Kollegen/Dritte einschreiten
- AN hat Anspruch auf Schadenersatz gegen Belaestiger und AG (§12 Abs 11 GlBG)

**Einkommenstransparenz:**
- Unternehmen mit mehr als 150 AN muessen alle 2 Jahre einen Einkommensbericht erstellen (§11a GlBG)
- Entgeltgleichheit fuer gleiche/gleichwertige Arbeit (§11 GlBG)

**Beweislastumkehr (§12 Abs 12 GlBG):**
- AN muss Diskriminierung nur **glaubhaft machen** → dann muss AG beweisen, dass ein anderer Grund vorlag

### I: Dienstzeugnis (§39 AngG)

- AN hat **jederzeit** Anspruch auf ein schriftliches Dienstzeugnis (auch waehrend des DV)
- Inhalt: Art und Dauer der Beschaeftigung
- Kein Recht auf "wohlwollendes" Zeugnis, aber keine schaedigenden Formulierungen erlaubt (keine Geheimcodes)
- AG darf keine Angaben aufnehmen, die das Fortkommen des AN erschweren
- Bei Verweigerung: Klage auf Ausstellung (ASG)

### J: Dienstnehmerhaftpflichtgesetz (DHG)

**Maessigung bei leichter Fahrlaessigkeit:**
- §2 DHG: Bei Schaeden, die der AN dem AG im Rahmen der Arbeit zufuegt:
  - Leichte Fahrlaessigkeit: Gericht kann Schadenersatz bis auf Null maessigen
  - Grobe Fahrlaessigkeit: Maessigung moeglich, aber geringer
  - Vorsatz: Keine Maessigung
- Kriterien fuer Maessigung (§2 Abs 2 DHG): Grad des Verschuldens, Art der Taetigkeit, Schadenshoehe, ob Schaden auch durch AN-Fehler entstanden, Entgelthoehe
- **Regressanspruch des AG:** Muss innerhalb von 6 Monaten geltend gemacht werden (§6 DHG)
- DHG gilt auch fuer Schaeden, die AN Dritten zufuegen (§3 DHG): AG muss Dritten ersetzen, kann nur mit Maessigung Regress nehmen

---

## Step 6: Present Results

```markdown
# Arbeitsrechtliche Analyse

**Sachverhalt:** [2-3 Saetze Zusammenfassung]
**Ihre Position:** [Arbeitnehmer/in / Arbeitgeber/in]
**Rechtsverhaeltnis:** [Echtes DV / Freier DV / Werkvertrag]
**Anwendbarer KollV:** [Bezeichnung, Verwendungsgruppe, Stufe]
**Betroffene Rechtsgebiete:** [AZG/UrlG/AngG/MSchG/GlBG/etc.]

## Vertragliche Einordnung

| Merkmal | Ihre Situation | Rechtliche Bewertung |
|---------|---------------|---------------------|
| Vertragstyp | [aus Sachverhalt] | [Qualifikation mit Begruendung] |
| KollV-Einstufung | [Vertraglich: VGr X] | [Korrekt: VGr Y, weil ...] |
| KV-Mindestgehalt | EUR [x] brutto | [Unter-/Ueberzahlung?] |

## Analyse: [Konkretes Problem]

### Rechtslage
[Darstellung der anwendbaren Rechtsnormen mit §§-Zitaten]

### Subsumtion
[Anwendung auf den konkreten Sachverhalt]

### Ansprueche

| Anspruch | Rechtsgrundlage | Hoehe / Dauer | Status |
|----------|----------------|---------------|--------|
| [z.B. Ueberstundennachzahlung] | §10 AZG | EUR [x] (geschaetzt) | Besteht / Fraglich / Verjahrt |
| [z.B. Urlaubsersatzleistung] | §10 UrlG | [x] Tage = EUR [y] | Besteht |
| [z.B. Kuendigungsentschaedigung] | §29 AngG | [x] Monatsentgelte | Besteht |

### Kuendigungsfristen (falls relevant)
| Kuendigungsart | Frist | Termin | Fruehestmoegliches Ende |
|---------------|-------|--------|------------------------|
| AG-Kuendigung | [x] Monate | [Quartalsende/Monatsletzter] | [Datum] |
| AN-Kuendigung | [x] Monat | [Monatsletzter] | [Datum] |

## Risiken und Einwendungen
[Moegliche Gegenargumente, Beweisfragen, Verjaehrung]

## Handlungsbedarf

### Sofortige Schritte
1. [Erster konkreter Schritt — z.B. "Ueberstundenaufzeichnungen sichern"]
2. [Zweiter Schritt]

### Fristen
| Frist | Datum | Konsequenz bei Versaeumung |
|-------|-------|--------------------------|
| [z.B. Kuendigungsanfechtung] | [Datum] | [Verlust des Anfechtungsrechts] |
| [z.B. Verjaehrung Ueberstunden] | [Datum] | [Verlust der aeltesten Ansprueche] |

### Empfehlung
[Konkrete Handlungsempfehlung, priorisiert]

## Quellenstatus
| Kategorie | Status | Details |
|-----------|--------|---------|
| RIS MCP | Verfuegbar / Nicht verfuegbar | |
| Gesetze | RIS_VERIFIED / UNVERIFIED | [n] Normen geprueft |
| Judikatur | RIS_VERIFIED / UNVERIFIED | [n] Entscheidungen |
| Pruefdatum | [YYYY-MM-DD] | |

---
Keine Rechtsberatung. Diese Analyse ersetzt nicht die Beratung durch einen Rechtsanwalt oder eine Rechtsanwaeltin. Arbeitnehmer/innen haben Anspruch auf kostenlose Beratung durch die Arbeiterkammer (AK) und ihre Gewerkschaft. Insbesondere bei Kuendigungsanfechtungen und Entlassungsstreitigkeiten ist die Einhaltung kurzer Fristen entscheidend — kontaktieren Sie umgehend die AK oder einen Rechtsanwalt.
```

---

## Critical Rules

1. **Always cite specific §§** — Never "laut Arbeitsrecht..." without die exakte Gesetzesbestimmung (z.B. §20 Abs 1 AngG, §10 Abs 1 AZG, §2 UrlG).
2. **KollV immer pruefen** — Das KV-Mindestgehalt und die KV-Einstufung sind in fast jedem arbeitsrechtlichen Fall relevant. Wenn der KollV nicht bekannt ist, nachfragen.
3. **All-in-Deckungspruefung** — Wenn eine All-in-Klausel vorliegt, IMMER die Deckungspruefung thematisieren. Dies ist eine der haeufigsten Quellen fuer Nachforderungen.
4. **Kuendigungsfristen UND Kuendigungstermine** — Beide angeben! Die Frist (z.B. 3 Monate) ist nicht dasselbe wie der Termin (z.B. Quartalsende). Ein haeufiger Fehler in der Praxis.
5. **2-Wochen-Frist bei Kuendigungsanfechtung** — Die Anfechtungsfrist nach §105 Abs 4 ArbVG betraegt nur 2 Wochen. Diese Frist ist NICHT erstreckbar. Immer prominent warnen.
6. **Scheinselbstaendigkeit aktiv pruefen** — Bei freien DV und Werkvertraegen immer die tatsaechliche Durchfuehrung hinterfragen. §539a ASVG: Wahrer wirtschaftlicher Gehalt.
7. **Abfertigung Alt vs. Neu unterscheiden** — DV vor 1.1.2003: Abfertigung Alt (§23 AngG). DV ab 1.1.2003: Abfertigung Neu (BMSVG). System nie verwechseln.
8. **Entlassung: Unverzueglichkeit** — Eine Entlassung muss sofort nach Bekanntwerden des Grundes ausgesprochen werden. Verspaetete Entlassung ist unwirksam.
9. **Arbeiterkammer-Hinweis** — Bei AN-Themen IMMER auf die kostenlose Beratung und Vertretung durch AK und Gewerkschaft hinweisen.
10. **Verjaehrung beachten** — Laufende Entgeltansprueche (Ueberstunden, KV-Differenz, Zulagen): 3 Jahre (§1486 Z 5 ABGB). Urlaubsverfall: 2 Jahre (§4 Abs 5 UrlG). Abfertigung Alt: 3 Jahre (strittig, teilweise 30 Jahre nach §1478 ABGB).
11. **Kuendigungsschutz bei Elternschaft explizit pruefen** — Schwangerschaft, Karenz, Elternteilzeit: Kuendigungsschutz beginnt mit Bekanntgabe! §10 MSchG / §7 VKG.
12. **Match user's language** — German in = German out. English in = English out. Gesetze immer in deutscher Originalform zitieren.
13. **Konkurrenzklausel: Entgeltgrenze pruefen** — Seit 29.12.2015 nur gueltig ueber der Entgeltgrenze. Aktuellen Wert der ASVG-Hoechstbeitragsgrundlage heranziehen.
14. **DHG-Maessigung bei Arbeitnehmerhaftung** — Wenn AN dem AG Schaden zufuegt: Immer auf das DHG und die Maessigungsmoeglichkeit bei leichter Fahrlaessigkeit hinweisen.
