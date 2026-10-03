---
name: recht-miet-momarcode1
title: /recht miet — Mietrechtliche Analyse
description: Austrian tenancy law analysis — MRG applicability, rent limits (Richtwertmietzins/angemessener Mietzins), Betriebskosten, Befristung, Kuendigungsschutz, Kaution, Erhaltungspflichten, Mietrechtsstreitigkeiten. Covers Vollanwendung, Teilanwendung, and ABGB-only tenancies.
author: MoMarcode1
author_url: https://github.com/MoMarcode1/austrian-legal-claude/tree/main/skills/recht-miet
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: at
practice: real-estate
language: de
sources:
- title: Evidence protocol
  path: references/evidence-protocol.md
- title: Ogh case presentation
  path: references/ogh-case-presentation.md
- title: Ris protocol
  path: references/ris-protocol.md
---

# /recht miet — Mietrechtliche Analyse

When the user describes a tenancy situation, presents a rental contract (Mietvertrag), asks about tenant or landlord rights, or has a dispute related to renting in Austria, follow these steps.

---

## Step 1: Gather the Facts

Read everything the user has provided. You need:

1. **Who is the user?** — Mieter (tenant) or Vermieter (landlord)?
2. **What type of property?** — Wohnung, Geschaeftslokal, Haus, Einzelzimmer, Garagenplatz?
3. **Building details critical for MRG scope:**
   - When was the Baubewilligung granted? (vor/nach 30.6.1953? vor/nach 8.5.1945?)
   - How many self-contained Mietgegenstaende are in the building? (1, 2, or 3+?)
   - Is the building a Neubau (Baubewilligung nach 30.6.1953)?
   - Is it a WEG-Objekt (Eigentumswohnung vermietet)?
   - Is it a gefoerderter Wohnbau (Gemeindebau, Genossenschaftswohnung)?
4. **Contract details:**
   - Written or oral? When concluded?
   - Befristet or unbefristet?
   - Agreed Mietzins (Hauptmietzins + Betriebskosten + USt)?
   - Kaution amount?
   - Any Abloese paid?
5. **What is the problem or question?** — Mietzins too high? Erhaltungspflicht dispute? Kuendigung received? Want to terminate? Betriebskostenabrechnung unclear? Kaution not returned?
6. **Location** — Which Bundesland? (Wien has Schlichtungsstelle, other cities may also have one)

If critical facts are missing, ask. Be specific:
> "Wann wurde die Baubewilligung fuer das Gebaeude erteilt? Das ist entscheidend fuer die Frage, ob das MRG voll, teilweise oder gar nicht anwendbar ist."

---

## Step 2: RIS Verification

Before proceeding with analysis, follow the **RIS Verification Protocol** (`references/ris-protocol.md`):
1. Check RIS MCP availability
2. For every § you cite in this analysis, verify current wording via RIS
3. For case law references (OGH, LGZ Wien as Rekursgericht), retrieve via RIS Justiz
4. Record verification status for the Quellenstatus block
5. If RIS is unavailable, follow the fallback ladder and flag all affected citations

Search RIS Justiz for relevant OGH decisions on the specific tenancy law question (e.g., OGH 5 Ob-Entscheidungen in Mietrechtssachen). Present using format from `references/ogh-case-presentation.md`.

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

## Step 3: Determine MRG Applicability (THE Critical First Question)

**This is the single most important step in any Austrian tenancy analysis.** The entire legal framework depends on whether the MRG applies fully, partially, or not at all. Get this wrong and everything else is wrong.

### Decision Tree: Vollanwendung vs. Teilanwendung vs. kein MRG

Work through this systematically:

### 3A: Complete Exclusion from MRG (§1 Abs 1 MRG — negative Abgrenzung)

The MRG does NOT apply at all to (ABGB §§1090ff only):

- [ ] **Dienstwohnungen** (§1 Abs 2 Z 2 MRG) — Wohnung als Teil des Dienstverhältnisses
- [ ] **Ferienwohnungen** die zu Erholungszwecken befristet vermietet werden (Airbnb-Kurzzeitvermietung)
- [ ] **Heime** (Studentenheime, Seniorenheime) — Heimvertragsgesetz (HeimVG) statt MRG
- [ ] **Pacht** (Unternehmenspacht, §1091 ABGB) — wenn ein lebendes Unternehmen ueberlassen wird, nicht nur Raeumlichkeiten
- [ ] **Leasingverhaeltnisse** ueber Geschaeftsraeumlichkeiten in bestimmten Konstellationen
- [ ] **Ein- und Zweiobjekthaeuser** in denen der Eigentuemer maximal 2 selbstaendige Mietgegenstaende vermietet (§1 Abs 2 Z 5 MRG) — ABER: nur wenn nicht gefoerdert!

### 3B: Teilanwendung des MRG (§1 Abs 4 MRG)

Nur ausgewaehlte Bestimmungen des MRG gelten (va. Kuendigungsschutz §§29-34, NICHT aber Mietzinsbeschraenkung):

- [ ] **Mietgegenstaende in Gebaeuden, die aufgrund einer nach dem 30.6.1953 erteilten Baubewilligung errichtet wurden** (= Neubauten), SOFERN nicht WEG-Objekte
- [ ] **Vermietete Eigentumswohnungen (WEG-Objekte)** — egal wann Baubewilligung, IMMER nur Teilanwendung (§1 Abs 4 Z 2 MRG) — AUSNAHME: Altbau-WEG-Wohnung vor 2002 war Vollmietgegenstand, dann bleibt Vollanwendung (Mietrechtsueberleitung)
- [ ] **Dachbodenausbauten und Zubauten** aufgrund einer nach dem 31.12.2001 erteilten Baubewilligung in einem Altbau (§1 Abs 4 Z 3 MRG)
- [ ] **Gefoerderte Neubauwohnungen** (Wohnbaufoerderung) — Teilanwendung, ABER Mietzinsobergrenzen koennen sich aus Foerderungsvorschriften ergeben

**Bei Teilanwendung gelten:**
- §§14, 16b, 29-36 MRG (Kuendigungsschutz)
- §§37-40 MRG (Verfahrensbestimmungen)
- §46a MRG (Eintrittsrecht im Todesfall)
- NICHT: §§3-5 (Erhaltung), §§15-16 (Mietzinsbeschraenkung), §§21-24 (Betriebskosten), §27 (Abloeseverbot), §10 (Investitionsersatz)

### 3C: Vollanwendung des MRG (§1 Abs 1 und 3 MRG)

Voller MRG-Schutz gilt bei:

- [ ] **Altbauten** — Baubewilligung VOR dem 1.7.1953, mit 3+ selbstaendigen Mietgegenstaenden
- [ ] **Gefoerderte Mietwohnungen** (Gemeindebau, Genossenschaftswohnungen) — egal wann Baubewilligung
- [ ] Altbauwohnungen, die vor Wohnungseigentumsbegruendung (vor 2002) vermietet waren und weiterhin Mietgegenstand sind

**Bei Vollanwendung gelten ALLE MRG-Bestimmungen**, insbesondere:
- Mietzinsbeschraenkungen (§§15-16 MRG)
- Betriebskostenkatalog (§§21-24 MRG)
- Erhaltungspflichten (§§3, 5 MRG)
- Abloeseverbot (§27 MRG)
- Investitionsersatz (§10 MRG)
- Kuendigungsschutz (§§29-36 MRG)

### 3D: Sonderfall Gemeinnuetziger Wohnbau (WGG)

- Wohnungen von gemeinnuetzigen Bauvereinigungen (GBV) — eigenes Regime nach dem WGG (Wohnungsgemeinnuetzigkeitsgesetz)
- Kostendeckungsprinzip (§13 WGG): Mietzins = Grundkostenanteil + Baukostenanteil + EVB + Betriebskosten + Ruecklage
- MRG gilt subsidiAer (§20 WGG)
- Kontrolle durch Revisionsverband
- Eigene Kuendigungsgruende (§13c WGG)

**Present the determination clearly:**
> "Ihr Mietverhaeltnis unterliegt der **Vollanwendung / Teilanwendung / keiner Anwendung** des MRG. Grund: [Baubewilligung vor/nach 1.7.1953 / WEG-Objekt / Neubau / etc.]. Das bedeutet konkret: [Aufzaehlung der anwendbaren Schutzbestimmungen]."

---

## Step 4: Analyze the Specific Legal Question

Based on the MRG applicability determined in Step 3, analyze the user's question. Work through the relevant sub-steps:

### 4A: Mietzins — Zulaessige Mietzinshoehe

**Nur bei Vollanwendung des MRG (§§15-16 MRG):**

#### Richtwertmietzins (§16 Abs 2-4 MRG) — Standardfall bei Altbauwohnungen

Der Richtwertmietzins ist der Regelfall fuer Mietvertraege im Vollanwendungsbereich, die NACH dem 1.3.1994 abgeschlossen wurden.

**Berechnung:**
1. **Richtwert fuer das Bundesland** — wird alle 2 Jahre per Kundmachung des BMJ angepasst (zuletzt per 1.4.2025 — aktuelle Werte via RIS oder Richtwertmietzins-Kundmachung pruefen)
   - Der Richtwert ist der Basismietzins pro m2 fuer eine Normwohnung der Kategorie A
2. **Zu- und Abschlaege (§16 Abs 2 MRG):**
   - Zuschlag fuer: Ausstattung ueber Kategorie A, Lage (Wohnumgebung), Stockwerk, Aufzug, Balkon/Terrasse/Loggia, Kellerabteil, Gartenbenuetzung, Erhaltungszustand, Gemeinschaftsanlagen
   - Abschlag fuer: Ausstattung unter Kategorie A, Erdgeschoss, Laermbeeinflussung, schlechter Erhaltungszustand, fehlender Aufzug ab dem 3. Stock, ungünstiger Grundriss
   - **ACHTUNG:** Zuschlaege duerfen den Richtwert NICHT verdoppeln (OGH-Judikatur zur Begrenzung)
   - Befristungsabschlag: 25% bei befristeten Mietvertraegen (§16 Abs 7 MRG)
   - Lagezuschlag (§16 Abs 3-4 MRG): abhaengig von der Grundkostenziffer des Standorts — fuer Gruenderzeithaeuser in Wien oft der groesste Zuschlagsfaktor

3. **Formel:** Richtwert +/- Zu-/Abschlaege - 25% Befristungsabschlag (wenn befristet) = zulaessiger Hauptmietzins/m2

#### Angemessener Mietzins (§16 Abs 1 MRG) — Ausnahmefall

Gilt statt Richtwertmietzins bei:
- Mietgegenstaende groesser als 130m2 Nutzflaeche
- Mietgegenstaende in Gebaeuden mit nicht mehr als 2 Mietgegenstaenden (die dennoch dem MRG voll unterliegen, z.B. wegen Foerderung)
- Geschaeftsraummieten im Vollanwendungsbereich
- Vermietung eines Mietgegenstands der Kategorie A oder B, der vom Vermieter binnen der letzten 20 Jahre aus dessen eigenen Mitteln zur Gaenze errichtet oder dem Standard einer Ausstattungskategorie A angehoben wurde

**Angemessenheit** wird nach Vergleichswerten (ortsüblicher Mietzins vergleichbarer Mietgegenstaende) bestimmt.

#### Kategoriemietzins (§15a MRG) — Altvertraege

Fuer Mietvertraege, die VOR dem 1.3.1994 abgeschlossen wurden:
- Kategorie A: Brauchbare Wohnung mit WC, Bad/Dusche, Zentralheizung/Etagenheizung, Warmwasser — Kategoriehoechstbetraege per Kundmachung
- Kategorie B: Wie A, aber ohne Zentralheizung
- Kategorie C: Wasser und WC im Inneren, aber ohne zeitgemaesse Badegelegenheit
- Kategorie D: Kein WC und/oder kein Wasser im Inneren der Wohnung
- Betraege werden regelmaessig valorisiert

#### Freier Mietzins (Teilanwendung / kein MRG)

Bei Teilanwendung des MRG und bei reinen ABGB-Mietverhaeltnissen: **keine gesetzliche Mietzinsobergrenze**. Vertragsfreiheit, ABER:
- Wucher (§879 Abs 2 Z 4 ABGB / §1 WucherG): Auffalliges Missverhaeltnis bei Ausnutzung einer Zwangslage
- Laesio enormis (§934 ABGB): analog anwendbar, wenn Mietzins das Doppelte des Verkehrswerts uebersteigt — strittig in der Judikatur

### 4B: Betriebskosten (§§21-24 MRG)

**Nur bei Vollanwendung des MRG.**

#### Taxativer Katalog der Betriebskosten (§21 Abs 1 MRG):

1. Wasserversorgung (Z 1)
2. Eichung und Wartung von Messvorrichtungen fuer Kaltwasser und Warmwasser (Z 1a)
3. Kanalraeumung und Muellabfuhr (Z 2)
4. Schaedlingsbekaempfung (Z 3)
5. Beleuchtung der allgemeinen Teile (Stiegenhaus etc.) (Z 4)
6. Feuerversicherung (Z 5) — nur die Feuerversicherung, nicht Buendelversicherungen!
7. Haftpflicht- und Leitungswasserschadenversicherung (Z 5a)
8. Personenaufzug — Betriebskosten, nicht Erneuerung (Z 6)
9. Allgemeine Rauchfangkehrung (Z 7)
10. Hausreinigung (Z 8)
11. Schneeraeumung (Z 8a)
12. Verwaltungskosten (Z 9) — Hoechstbetrag per Kundmachung
13. Grundsteuer (Z 10)
14. Oeffenliche Abgaben, die von der Liegenschaft zu entrichten sind (Z 11)

**NICHT umlegbare Kosten (haeufige Fehler von Vermietern):**
- Reparaturen und Instandhaltung (= Erhaltung, §3 MRG — Sache des Vermieters)
- Hausbetreuungskosten, die ueber Reinigung und Schneeraeumung hinausgehen
- Rechtsanwaltskosten des Vermieters
- Eigentuemergemeinschafts-Ruecklage bei WEG-Wohnungen
- Versicherungen, die nicht in §21 aufgezaehlt sind (z.B. Rechtsschutzversicherung)

#### Abrechnungspflicht (§21 Abs 3 MRG):

- Vermieter muss jaehrlich bis 30.6. des Folgejahres die Betriebskostenabrechnung legen
- Abrechnungszeitraum: Kalenderjahr (oder abweichendes Wirtschaftsjahr)
- **Einsichtsrecht der Mieter (§21 Abs 4 MRG):** Mieter koennen innerhalb von 6 Monaten nach Auflegung der Abrechnung Einsicht in die Belege nehmen
- Bei Nicht-Abrechnung: Mieter kann Abrechnung bei Schlichtungsstelle/BG erzwingen

#### Verteilungsschluessel:

- Grundsaetzlich nach Nutzflaeche der einzelnen Mietgegenstaende (§17 MRG)
- Abweichende Vereinbarung zulaessig, wenn sachlich gerechtfertigt
- Leerstandsquote: Betriebskosten fuer leerstehende Einheiten traegt der Vermieter

### 4C: Befristung (§29 MRG)

#### Zulaessige Befristung bei Vollanwendung:

- **Mindestdauer:** 3 Jahre (§29 Abs 1 Z 3 lit a MRG)
- Befristung unter 3 Jahren ist NICHTIG — der Vertrag gilt als unbefristet!
- Auslaufen: Mietvertrag endet durch Zeitablauf, ABER Vermieter muss dem Mieter die Nicht-Erneuerung rechtzeitig mitteilen
- **Verlaengerung/Erneuerung:** Wird ein befristeter Vertrag einvernehmlich verlaengert, muss die Verlaengerung wieder mindestens 3 Jahre betragen (§29 Abs 3 MRG)
- Stillschweigende Erneuerung (§1114 ABGB): Wenn Mieter nach Ablauf in der Wohnung bleibt und Vermieter nicht widerspricht, gilt der Vertrag als auf 3 Jahre erneuert (im Vollanwendungsbereich)

#### Vorzeitige Kuendigung durch den Mieter (§29 Abs 2 MRG):

- Ab dem 2. Vertragsjahr (= nach Ablauf des 1. Jahres) kann der Mieter den befristeten Vertrag jederzeit unter Einhaltung einer 3-monatigen Kuendigungsfrist zum Monatsletzten aufkuendigen
- **Achtung:** Gilt nur im Vollanwendungsbereich des MRG! Bei Teilanwendung gibt es dieses vorzeitige Kuendigungsrecht NUR wenn vertraglich vereinbart
- Im Teilanwendungsbereich: §29 Abs 2 MRG gilt NICHT — vorzeitige Kuendigung nur wenn im Vertrag vorgesehen

#### Befristungsabschlag:

- §16 Abs 7 MRG: Bei befristeten Mietvertraegen ist ein Abschlag von 25% auf den Richtwertmietzins vorzunehmen
- Gilt nur im Vollanwendungsbereich und bei Richtwertmietzins

### 4D: Kuendigungsschutz (§§29-36 MRG)

**Gilt bei Vollanwendung UND bei Teilanwendung!**

#### Kuendigung durch den Vermieter — nur aus wichtigem Grund (§30 Abs 2 MRG):

Die Kuendigungsgruende sind TAXATIV (abschliessend aufgezaehlt). Die wichtigsten:

| Kuendigungsgrund | § MRG | Voraussetzungen |
|-----------------|-------|-----------------|
| Qualifiziert nachteiliger Gebrauch | §30 Abs 2 Z 3 | Erheblich nachteilige Verwendung, z.B. schwere Schaeden, stoerend unleidliches Verhalten |
| Zahlungsverzug (qualifiziert) | §30 Abs 2 Z 1 | Trotz Mahnung mit Nachfristsetzung nicht bezahlt; Mieter kann durch Nachzahlung bis zum Schluss der muendlichen Verhandlung Kuendigung abwenden |
| Gaenzliche Weitergabe | §30 Abs 2 Z 4 | Mieter hat den Mietgegenstand zur Gaenze (ohne eigene Nutzung) weitergegeben UND benoetigt ihn nicht dringend |
| Nichtbenuetzung | §30 Abs 2 Z 6 | Wohnung wird nicht regelmaessig zu Wohnzwecken verwendet |
| Eigenbedarf | §30 Abs 2 Z 8-9 | Vermieter benoetigt die Wohnung dringend fuer sich selbst — STRENGE Voraussetzungen, Abwaegung |
| Abbruchsreife | §30 Abs 2 Z 14 | Baubehoerdlich angeordneter Abbruch |
| Wirtschaftliche Verwertung | §30 Abs 2 Z 15 | Sehr restriktiv, Vermieter muss Ersatzwohnung anbieten |

#### Gerichtliche Aufkuendigung (§33 MRG):

- Kuendigung durch den Vermieter MUSS gerichtlich erfolgen (beim zustaendigen Bezirksgericht)
- Kuendigungsfrist: 1 Monat bei Wohnungen, zum Monatsletzten
- Mieter kann Einwendungen innerhalb von 4 Wochen erheben
- Erhebt der Mieter keine Einwendungen, wird die Kuendigung wirksam (Vollstreckbarkeitsbestaetiung)
- Erhebt der Mieter Einwendungen → Verfahren ueber die Rechtmaessigkeit der Kuendigung

#### Ausserordentliche Aufloesungsgruende (ABGB):

- §1117 ABGB: Mieter kann fristlos aufloesen bei Unbrauchbarkeit des Mietgegenstands (Gesundheitsgefaehrdung, schwere Maengel)
- §1118 ABGB: Vermieter kann fristlos aufloesen bei erheblich nachteiligem Gebrauch oder qualifiziertem Zahlungsverzug — korrespondiert mit §30 Abs 2 Z 1 und Z 3 MRG

### 4E: Erhaltungspflichten

#### Vermieter (§3 MRG — Vollanwendungsbereich):

Erhaltungspflicht des Vermieters umfasst:
1. **Allgemeine Teile des Hauses** (Dach, Fassade, Stiegenhaus, Leitungen) — immer
2. **Ernste Schaeden des Hauses** beseitigen — immer
3. **Mietgegenstand** in brauchbarem Zustand erhalten — umfasst:
   - Behebung ernster Schaeden im Inneren der Wohnung
   - Erhaltung der mitvermieteten Heizthermen und Warmwasserbereiter — **SEIT 1.1.2024 (MRG-Novelle 2023):** Vermieter muss Gasthermen, die aelter als 15 Jahre sind, auf eigene Kosten durch klimafreundliche Heizsysteme ersetzen. Reparaturkosten fuer mitvermietete Thermen traegt ebenfalls der Vermieter.
   - Erhaltung mitvermieteter Geraete und Einrichtungen (Einbaukueche, die mitvermietet wurde etc.)
4. **Brandschutzvorschriften und Sicherheitsmassnahmen** einhalten

- Mieter muss Schaeden ANZEIGEN (§8 Abs 1 MRG), sonst Schadenersatzpflicht
- Bei Untaetigkeit des Vermieters: Antrag an Schlichtungsstelle/BG auf Durchfuehrung von Erhaltungsarbeiten (§6 MRG)

#### Mieter (§8 MRG):

- Pflicht zur Wartung und zum pfleglichen Umgang
- Duldungspflicht: Mieter muss Erhaltungsarbeiten und Verbesserungsarbeiten dulden (§8 Abs 2 MRG), Vermieter muss Mietzinsminderung waehrend der Arbeiten gewaehren wenn erhebliche Beeintraechtigung
- Mieter darf Veraenderungen vornehmen (§9 MRG), wenn: verkehrsueblich, dem Stand der Technik entsprechend, auf eigene Kosten, Vermieter hat nicht innerhalb von 2 Monaten schriftlich widersprochen (gilt Zustimmung als erteilt bei privilegierten Aenderungen §9 Abs 1 MRG)

### 4F: Kaution

**Keine ausdrueckliche MRG-Regelung**, daher ABGB und Judikatur:

- **Zulaessige Hoehe:** OGH-Judikatur: Bis zu 6 Bruttomonatsmieten gelten als angemessen, haeufig werden 3 Bruttomonatsmieten vereinbart. Ueberhoeht = §879 ABGB (Sittenwidrigkeit)
- **Verzinsung:** Die Kaution ist als Spareinlage oder vergleichbar sicher und verzinslich anzulegen (§1 Abs 1 MRG iVm allgemeine Grundsaetze). In der Praxis: Sparbuch. Zinsen gebuehren dem Mieter.
- **Rueckgabe:** Bei Vertragsende ist die Kaution (samt Zinsen) zurueckzugeben, ABZUGLICH berechtigter Gegenforderungen des Vermieters (offene Mieten, Schaeden, die ueber normale Abnuetzung hinausgehen)
- **Beweislast:** Vermieter muss nachweisen, dass ein Abzug berechtigt ist
- **Frist:** Rueckgabe innerhalb angemessener Frist nach Rueckstellung des Mietgegenstands — die Judikatur billigt dem Vermieter eine Prueffrist von einigen Wochen zu. Nicht monatelang zurueckhalten.
- **Keine Aufrechnung des Mieters:** Der Mieter darf die letzten Mieten NICHT einfach „mit der Kaution verrechnen" — die Miete ist bis zum Ende des Mietverhaeltnisses zu bezahlen

### 4G: Abloeseverbot (§27 MRG — Vollanwendungsbereich)

- **Verbotene Abloesen (§27 Abs 1 MRG):**
  - Abloesen fuer den Verzicht auf Mietrechte an Vormieter oder Vermieter
  - Abloesen fuer die Zustimmung zum Mietvertrag
  - Zahlungen an den Vermieter oder Vormieter, die ueber den zulaessigen Mietzins hinausgehen
- **Zulaessige Abloesen (§27 Abs 1 letzter Satz MRG):**
  - Abgeltung von tatsaechlich durchgefuehrten Investitionen des Vormieters, die dem Nachmieter zugutekommen (angemessen, nicht ueberhoeht)
  - Uebernahme von Einrichtungsgegenstaenden zum angemessenen Preis
- **Rueckforderung verbotener Abloesen (§27 Abs 3 MRG):** innerhalb von 10 Jahren — siehe recht-miet-verfahren
- **Maklerprovision — Bestellerprinzip (§17a MaklerG, seit 1.7.2023):**
  - Wer den Makler beauftragt, bezahlt die Provision (Erstauftraggeberprinzip)
  - In der Praxis: Wenn der Vermieter den Makler beauftragt, zahlt der Vermieter die Provision
  - Der Mieter zahlt nur dann Provision, wenn ER den Makler selbst beauftragt hat (= Suchauftrag)
  - Gilt fuer Mietvertraege ueber Wohnungen

### 4H: Investitionsersatz (§10 MRG — Vollanwendungsbereich)

- **Privilegierte Aufwendungen (§10 Abs 3 MRG):** z.B. Errichtung einer Zentralheizung, Schallschutzfenster, Badezimmerinstallation — diese MUESSEN bei Mietende ersetzt werden, wenn:
  - Vermieter hat zugestimmt oder nicht fristgerecht widersprochen
  - Investition erhoht den Wohnwert
- **Abschreibung:** Linearer Abzug ueber die Nutzungsdauer (§10 Abs 4 MRG: in der Regel 10 Jahre, bei Heizung, Sanitaerinstallationen etc. 20 Jahre)
- **Nicht privilegierte Aufwendungen (§10 Abs 5 MRG):** nur Ersatz, wenn im Interesse des Vermieters gelegen und dieser zugestimmt hat
- **Geltendmachung:** Spätestens bei Beendigung des Mietverhaeltnisses, idealerweise schriftlich gegenueber dem Vermieter, sonst bei Schlichtungsstelle/BG

### 4I: Eintrittsrecht (§14 MRG)

Bei Tod des Mieters treten folgende Personen in den Mietvertrag ein (Reihenfolge):
1. Ehegattin/Ehegatte, eingetragene/r Partner/in
2. Lebensgefaehrtin/Lebensgefaehrte (mind. 3 Jahre gemeinsamer Haushalt)
3. Verwandte in gerader Linie (Kinder, Enkel, Eltern)
4. Geschwister
- **Voraussetzung:** Dringendes Wohnbeduerfnis und gemeinsamer Haushalt im Zeitpunkt des Todes (§14 Abs 3 MRG)
- Bei Teilanwendung: nur eingeschraenktes Eintrittsrecht (§46a MRG)

### 4J: WEG 2002 — Relevanz fuer Mietrecht

Wenn der Vermieter Eigentuemer einer Eigentumswohnung ist:
- Mietvertrag unterliegt in der Regel der **Teilanwendung** des MRG (§1 Abs 4 Z 2 MRG)
- Betriebskostenkatalog des §21 MRG gilt NICHT — Betriebskosten richten sich nach Vertrag
- Mietzins ist frei vereinbar (keine Richtwertmietzinsbeschraenkung)
- Kuendigungsschutz (§§29-34 MRG) gilt aber trotzdem
- Wohnungseigentuemer zahlt Ruecklage an die Eigentuemergemeinschaft — diese ist NICHT auf den Mieter ueberwaehlbar
- Erhaltungspflichten richten sich nach dem Vertrag und ABGB (§1096 ABGB: Vermieter hat fuer Brauchbarkeit zu sorgen)

### 4K: Mietzinsminderung (§1096 ABGB)

Bei Maengeln des Mietgegenstands hat der Mieter Anspruch auf Mietzinsminderung:
- **Rechtsgrundlage:** §1096 Abs 1 ABGB — gilt auch bei Teilanwendung und bei ABGB-only Mietverhaeltnissen (zwingendes Recht bei Wohnungsmiete!)
- **Ausmass:** richtet sich nach dem Grad der Gebrauchsbeeintraechtigung
  - 100% bei voelliger Unbrauchbarkeit
  - 5-50% bei Teilbeeintraechtigung (Richtwerte aus der Judikatur: Heizungsausfall im Winter ca. 30-50%, undichtes Fenster ca. 5-15%, Laerm durch Bauarbeiten am Haus ca. 10-25%)
- **Anspruch besteht automatisch** (ex lege), nicht erst nach Anzeige — aber Mieter muss Mangel zeitnah anzeigen (§8 Abs 1 MRG), um Schadenersatzansprueche des Vermieters zu vermeiden
- **Keine Verzichtbarkeit im Voraus** bei Wohnungsmiete (§1096 Abs 1 letzter Satz ABGB — zwingend!)

---

## Step 5: Summary and Recommendations

### 5A: Assess the situation

Based on the analysis:
1. **MRG-Anwendungsbereich** klar feststellen
2. **Rechtswidrigkeit** identifizieren (ueberhoeher Mietzins? Unzulaessige Abloese? Mangelhafte Erhaltung?)
3. **Ansprueche quantifizieren** (z.B. Differenz zwischen vereinbartem und zulaessigem Mietzins x Anzahl Monate = Rueckforderungsanspruch)
4. **Dringlichkeit** einschaetzen (laufende Fristen? Kuendigung?)

### 5B: Practical next steps

- Verweise auf recht-miet-verfahren fuer Verfahrensschritte (Schlichtungsstelle, BG-Antrag)
- Immer Mietervereinigung oder Arbeiterkammer-Beratung empfehlen
- Bei Vermietern: Hausverwaltung konsultieren, ggf. OERAG/Rechtsschutzversicherung pruefen

---

## Step 6: Present Results

```markdown
# Mietrechtliche Analyse

**Sachverhalt:** [2-3 Saetze Zusammenfassung]
**Mietgegenstand:** [Wohnung/Geschaeftslokal, Adresse/Lage, Groesse]
**MRG-Anwendung:** Vollanwendung / Teilanwendung / kein MRG (nur ABGB)
**Begruendung MRG-Anwendung:** [Altbau/Neubau, Baubewilligung, WEG, Foerderung etc.]

## Zusammenfassung
[2-3 Saetze: Kernproblem, wichtigste Erkenntnis, Handlungsbedarf]

## Rechtliche Einordnung

| Kriterium | Einordnung |
|-----------|-----------|
| MRG-Anwendungsbereich | Vollanwendung / Teilanwendung / kein MRG |
| Baubewilligung | vor / nach 1.7.1953 |
| Gebaeude | [Altbau / Neubau / WEG / gefoerdert / GBV] |
| Mietvertragstyp | befristet / unbefristet |
| Mietzinsart | Richtwert / angemessen / Kategorie / frei |

## Detailanalyse: [Thema]
[Ausfuehrliche Analyse der konkreten Rechtsfrage mit §§-Zitaten]

## Mietzinsberechnung (falls relevant)
| Position | Betrag/m2 | Gesamt |
|----------|-----------|--------|
| Richtwert [Bundesland] | EUR [x]/m2 | |
| + Lagezuschlag | EUR [x]/m2 | |
| +/- Weitere Zu-/Abschlaege | EUR [x]/m2 | |
| - Befristungsabschlag 25% | -EUR [x]/m2 | |
| **Zulaessiger Hauptmietzins** | **EUR [x]/m2** | **EUR [x]** |
| Vereinbarter Hauptmietzins | EUR [x]/m2 | EUR [x] |
| **Differenz (monatlich)** | | **EUR [x]** |
| **Rueckforderung (x Monate)** | | **EUR [x]** |

## Ansprueche / Rechte

| Anspruch | Rechtsgrundlage | Betrag / Umfang | Durchsetzung |
|----------|----------------|-----------------|--------------|
| [z.B. Mietzinsrueckforderung] | §37 Abs 1 Z 8 MRG | EUR [x] | Schlichtungsstelle / BG |
| [z.B. Erhaltungsantrag] | §6 MRG | Thermentausch | Schlichtungsstelle / BG |
| [z.B. Kautionsrueckforderung] | §1431 ABGB | EUR [x] + Zinsen | Klage beim BG |

## Fristen und Dringlichkeit
| Frist | Datum | Konsequenz bei Versaeumung |
|-------|-------|--------------------------|
| [z.B. Einwendungen gegen Kuendigung] | [Datum] | Kuendigung wird rechtskraeftig |
| [z.B. Mietzinsueberpruefung] | innerhalb 3 Jahre | Verjaehrung der Rueckforderung (§27 Abs 3 MRG: 10 Jahre fuer Abloesen) |

## Naechste Schritte
1. [Konkreter erster Schritt]
2. [Konkreter zweiter Schritt]
3. [Beratung empfehlen: Mietervereinigung / AK / Rechtsanwalt]

## Quellenstatus
| Kategorie | Status | Details |
|-----------|--------|---------|
| RIS MCP | Verfuegbar / Nicht verfuegbar | [connection status] |
| Gesetze | RIS_VERIFIED / OFFICIAL_WEB_VERIFIED / UNVERIFIED | [n] Normen geprueft |
| Judikatur | RIS_VERIFIED / OFFICIAL_WEB_VERIFIED / UNVERIFIED | [n] Entscheidungen |
| Pruefdatum | [YYYY-MM-DD] | |

---
Keine Rechtsberatung. Diese Analyse dient der mietrechtlichen Ersteinschaetzung und ersetzt nicht die Beratung durch einen Rechtsanwalt, die Mietervereinigung oder die Arbeiterkammer. Insbesondere die Mietzinsberechnung (Zu- und Abschlaege zum Richtwert) erfordert in der Praxis ein Sachverstaendigengutachten. Aktuelle Richtwerte und Betriebskostengrenzbetraege auf ris.bka.gv.at pruefen.
```

---

## Critical Rules

1. **MRG-Anwendungsbereich ZUERST klaeren** — Jede Analyse beginnt mit Step 3. Ohne Klaerung der MRG-Anwendbarkeit ist jede weitere Aussage potentiell falsch. Im Zweifel nachfragen: Baubewilligung, WEG-Begruendung, Foerderung, Anzahl Mietgegenstaende.
2. **Vollanwendung vs. Teilanwendung scharf trennen** — Bei Teilanwendung gibt es KEINEN Richtwertmietzins, KEIN Betriebskostenkatalog nach §21 MRG, KEINEN Investitionsersatz nach §10 MRG. Niemals diese Bestimmungen bei Teilanwendung anwenden.
3. **Befristungsabschlag nicht vergessen** — 25% Abschlag bei befristeten Vertraegen im Vollanwendungsbereich (§16 Abs 7 MRG). Wird haeufig uebersehen.
4. **Vorzeitiges Kuendigungsrecht des Mieters bei Befristung** — Nur im Vollanwendungsbereich! Bei Teilanwendung (Neubau, WEG) gibt es KEIN gesetzliches vorzeitiges Kuendigungsrecht (§29 Abs 2 MRG gilt nicht). Muss vertraglich vereinbart sein.
5. **Always cite specific §§** — Nie "laut Mietrecht" ohne §16 Abs 2 MRG, §30 Abs 2 Z 3 MRG, §1096 ABGB etc.
6. **Thermenregelung 2024 beachten** — Seit 1.1.2024 (MRG-Novelle 2023) traegt der Vermieter im Vollanwendungsbereich die Kosten fuer Erhaltung und Ersatz mitvermieteter Heizthermen. Dies ist eine wesentliche Aenderung.
7. **Bestellerprinzip seit 1.7.2023** — §17a MaklerG: Wer den Makler beauftragt, zahlt. Bei Wohnungsmiete keine Provision vom Mieter, wenn Vermieter den Makler beauftragt hat.
8. **Richtwertmietzins erfordert Sachverstaendigen** — Die Berechnung der Zu- und Abschlaege (insb. Lagezuschlag) ist komplex und erfordert in der Praxis haeufig ein Sachverstaendigengutachten. Eigene Berechnungen immer als Schaetzung kennzeichnen.
9. **Verjaehrung bei Mietzinsrueckforderung beachten** — Mietzinsrueckforderung (§37 Abs 1 Z 8 MRG): 3 Jahre allgemeine Verjaehrung. Abloesrueckforderung (§27 Abs 3 MRG): 10 Jahre. Unterschied klar kommunizieren.
10. **Match user's language** — German in = German out. English in = English out. Gesetze immer in deutscher Originalform zitieren (§16 MRG, §1096 ABGB etc.).
11. **Bei Geschaeftsraummiete gesondert pruefen** — Geschaeftsraummiete hat abweichende Regeln (kein Befristungsabschlag, keine vorzeitige Kuendigung durch Mieter, andere Kuendigungsfristen). Nicht automatisch Wohnungsmiete-Regeln anwenden.
12. **Gemeinnuetzigen Wohnbau (WGG) nicht mit MRG verwechseln** — GBV-Wohnungen haben eigene Mietzinsregeln (Kostendeckungsprinzip), eigene Kuendigungsgruende, eigene Kontrollmechanismen. WGG als lex specialis beachten.
