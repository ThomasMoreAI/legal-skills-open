---
name: recht-erbe-momarcode1
title: /recht erbe — Erbrechtliche Analyse
description: Austrian inheritance law analysis — intestate succession (gesetzliche Erbfolge), wills (Testament), forced heirship (Pflichtteil), estate procedure (Verlassenschaftsverfahren), gifts inter vivos (Schenkung auf den Todesfall), estate planning, and inheritance disputes.
author: MoMarcode1
author_url: https://github.com/MoMarcode1/austrian-legal-claude/tree/main/skills/recht-erbe
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: at
practice: trusts-and-estates
language: de
---

# /recht erbe — Erbrechtliche Analyse

When the user describes an inheritance situation, presents documents (Testament, Verlassenschaftsabhandlung, Schenkungsvertrag, Pflichtteilsforderung), or asks about Austrian succession law, follow these steps.

---

## Step 1: Read the Facts / Documents

Read everything the user has provided. You need:

1. **Who died (Erblasser)?** — Name, Todesdatum, letzter gewoehnlicher Aufenthalt, Staatsangehörigkeit (relevant für EU-ErbVO)
2. **Family situation at death?** — Ehegatte/eingetragener Partner/Lebensgefährte? Kinder (ehelich, unehelich, adoptiert)? Eltern, Geschwister, Grosseltern noch lebend? Vorvorstorbene Verwandte?
3. **Letztwillige Verfuegungen?** — Testament vorhanden? Eigenhändig oder fremdhändig? Erbvertrag? Vermächtnis? Auflagen?
4. **Vermoegenswerte?** — Immobilien, Bankkonten, Wertpapiere, Unternehmensbeteiligungen, Fahrzeuge, Schmuck, Schulden, Buergschaften?
5. **Schenkungen zu Lebzeiten?** — An wen, wann, welcher Wert? Schenkung auf den Todesfall? Anrechnungsbestimmungen?
6. **What is the user's goal?** — Erbquoten berechnen? Pflichtteil einfordern? Testament errichten? Testament anfechten? Nachlassplanung?

If critical facts are missing, ask. Be specific:
> "Wer sind die gesetzlichen Erben? Gibt es ein Testament? Wurden zu Lebzeiten Schenkungen gemacht? Diese Informationen bestimmen die Erbquoten und allfaellige Pflichtteilsansprueche."

---

## Step 2: RIS Verification

Before proceeding with analysis, follow the **RIS Verification Protocol** (`references/ris-protocol.md`):
1. Check RIS MCP availability
2. For every § you cite in this analysis, verify current wording via RIS
3. For case law references (OGH, LG), retrieve via RIS Justiz
4. Record verification status for the Quellenstatus block
5. If RIS is unavailable, follow the fallback ladder and flag all affected citations

Search RIS Justiz for relevant OGH-Entscheidungen on disputed inheritance law questions. Present using format from `references/ogh-case-presentation.md`.

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

## Step 3: Determine the Applicable Succession Regime

### A: Internationaler Bezug pruefen (EU-ErbVO)

**Europaeische Erbrechtsverordnung (EU) Nr. 650/2012:**
- **Grundregel (Art 21 EU-ErbVO):** Anwendbar ist das Recht des Staates, in dem der Erblasser im Zeitpunkt des Todes seinen **gewoehnlichen Aufenthalt** hatte
- **Rechtswahl (Art 22 EU-ErbVO):** Der Erblasser kann das Recht seiner Staatsangehörigkeit waehlen (muss letztwillig verfuegt werden)
- **Oesterreich-Bezug:** Wenn der Erblasser seinen gewoehnlichen Aufenthalt in Oesterreich hatte UND keine abweichende Rechtswahl getroffen hat → oesterreichisches Erbrecht (ABGB)
- **Europaeisches Nachlasszeugnis (Art 62ff EU-ErbVO):** Fuer grenzueberschreitende Nachlaesse

Wenn kein internationaler Bezug besteht → weiter mit oesterreichischem Erbrecht.

### B: Gesetzliche Erbfolge (§§730ff ABGB) — Parentelensystem

Wenn **kein** gueltiges Testament vorliegt, gilt die gesetzliche Erbfolge nach dem Parentelensystem (Liniensystem):

**1. Parentel (§732 ABGB) — Nachkommen des Erblassers:**
- Kinder erben zu gleichen Teilen
- Vorverstorbenes Kind: dessen Nachkommen treten an seine Stelle (Repraesentation, §733 ABGB)
- Eheliche, uneheliche und adoptierte Kinder sind gleichgestellt (§732 ABGB)

**2. Parentel (§735 ABGB) — Eltern und deren Nachkommen:**
- Beide Elternteile je 1/2
- Vorverstorbener Elternteil: dessen Nachkommen (Geschwister des Erblassers) treten ein
- Halbgeschwister erben nur im Stamm ihres Elternteils

**3. Parentel (§736 ABGB) — Grosseltern und deren Nachkommen:**
- Vier Grosselternteile je 1/4
- Vorverstorbener Grosselternteil: dessen Nachkommen treten ein
- **Achtung (§737 ABGB):** Anwachsung an den anderen Grosselternteil derselben Linie, wenn keine Nachkommen vorhanden

**4. Parentel (§738 ABGB) — Urgrosseltern:**
- Urgrosseltern erben persoenlich, KEINE Repraesentation in der 4. Parentel
- Ueber die 4. Parentel hinaus gibt es KEIN gesetzliches Erbrecht

**Ehegatte / Eingetragener Partner (§744 ABGB):**

| Neben... | Erbquote des Ehegatten | §§ |
|----------|------------------------|----|
| 1. Parentel (Kinder) | 1/3 | §744 Abs 1 ABGB |
| 2. Parentel (Eltern) | 2/3 | §744 Abs 1 ABGB |
| 3. Parentel (Grosseltern) | 2/3 + Anteil vorverstorbener Grosseltern | §744 Abs 2 ABGB |
| 4. Parentel oder keine Verwandten | Gesamte Verlassenschaft | §744 Abs 2 ABGB |

- Eingetragene Partner (EPG) sind Ehegatten gleichgestellt (§537a ABGB iVm EPG)
- **Vorausvermaechtnis des Ehegatten (§745 ABGB):** Recht auf die zum ehelichen Haushalt gehoerenden beweglichen Sachen + Recht, in der Ehewohnung weiter zu wohnen — das ist KEIN Erbteil, sondern ein gesetzliches Vermaechtnis, kommt ZUSAETZLICH zum Erbteil

**Lebensgefaehrte (§748 ABGB):**
- Ausserordentliches Erbrecht: Lebensgefaehrte erbt nur, wenn KEINE gesetzlichen Erben vorhanden sind (subsidiäres Erbrecht)
- Voraussetzung: mindestens 3 Jahre gemeinsamer Haushalt in den letzten 3 Jahren vor dem Tod
- **Kein Pflichtteilsrecht** fuer Lebensgefaehrten
- Lebensgefaehrte hat jedoch ein gesetzliches Vermaechtnis auf Weiterbenützung der Wohnung fuer 1 Jahr (§745 Abs 2 ABGB)

### C: Gewillkuerte Erbfolge — Testament (§§577ff ABGB)

**Testamentsformen:**

| Form | Voraussetzungen | §§ ABGB |
|------|----------------|---------|
| **Eigenhändig** (holographisch) | Gesamter Text + Datum + Unterschrift eigenhaendig geschrieben | §578 ABGB |
| **Fremdhändig** (allographisch) | Schriftlich + 3 gleichzeitig anwesende Zeugen + eigenhändige Nuncupatio ("Das ist mein letzter Wille") + Unterschrift vor Zeugen | §579 ABGB |
| **Notariatsakt** | Vor Notar in Notariatsaktform errichtet | §581 ABGB |
| **Gerichtliches Testament** | Vor Gericht zu Protokoll erklaert | §581 ABGB |
| **Nottestament** (muendlich) | Nur bei naher Todesgefahr, 2 Zeugen, verfaellt nach 3 Monaten wenn Erblasser die Gefahr ueberlebt | §584 ABGB |

**Testamentszeugen (§§587-590 ABGB):**
- Muessen faehig sein: volljaehrig, der Sprache maechtig, nicht blind/taub/stumm (fuer fremdhändige Testamente)
- Duerften NICHT bedacht sein (Befangenheit, §588 ABGB) — Zuwendungen an Zeugen oder deren nahe Angehoerige sind NICHTIG
- Identitaetszeugen vs. Aktszeugen

**Testierfaehigkeit (§§566-568 ABGB):**
- Volljaehrige Personen (ab 18 Jahre) — volle Testierfaehigkeit
- Muendige Minderjaehrige (14-18 Jahre) — nur muendlich vor Gericht oder als Notariatsakt (§569 ABGB)
- Unter 14 Jahre — testierunfaehig
- Geisteskranke oder Personen, die nicht faehig sind, die Bedeutung einer letztwilligen Verfuegung zu verstehen — testierunfaehig (§567 ABGB)

**Testamentsauslegung (§§553-556 ABGB):**
- Wohlwollende Auslegung zugunsten der Aufrechterhaltung (favor testamenti, §553 ABGB)
- Ermittlung des wahren Willens des Erblassers (§553 ABGB)
- Irrtumsanfechtung: §572 ABGB — Motivirrtum und Erklaerungsirrtum

**Widerruf des Testaments (§§713-724 ABGB):**
- Ausdruecklicher Widerruf: durch neues Testament oder Widerrufserklärung (§713 ABGB)
- Konkludenter Widerruf: Vernichtung der Urkunde (§717 ABGB), spaeteres Testament widerspricht frueherem (§713 ABGB)
- **Achtung:** Spaeteres Testament widerruft frueheres nur insoweit, als es diesem widerspricht (§713 ABGB)

### D: Erbvertrag (§§1249ff ABGB)

- **Nur zwischen Ehegatten** (oder eingetragenen Partnern) zulaessig (§1249 ABGB)
- **Notariatsaktpflicht** (§1249 ABGB)
- Maximal 3/4 des Nachlasses koennen per Erbvertrag verfuegt werden — 1/4 muss frei testierbar bleiben (§1253 ABGB)
- Aufhebung: einvernehmlich, durch Scheidung (§1266 ABGB), oder bei Vorliegen von Enterbungsgruenden

### E: Vermaechtnis / Legat (§§647ff ABGB)

- Vermaechtnisnehmer ist KEIN Erbe — hat nur einen schuldrechtlichen Anspruch gegen den Erben auf Herausgabe des vermachten Gegenstands (§647 ABGB)
- **Arten:** Stueckvermaechtnis (bestimmte Sache), Gattungsvermaechtnis, Wahlvermaechtnis, Universalvermaechtnis
- Vermaechtnis darf den Pflichtteil nicht verkuerzen — Kueerzungsrecht der Pflichtteilsberechtigten (§692 ABGB)
- Vorausvermaechtnis des Ehegatten (§745 ABGB) — gesetzliches Vermaechtnis, auch neben testamentarischer Erbfolge

---

## Step 4: Pflichtteilsrecht (§§759ff ABGB)

**DAS ist der haeufigste Streitpunkt im Erbrecht.** Immer systematisch pruefen.

### 4A: Pflichtteilsberechtigte (§759 ABGB)

| Berechtigte | Pflichtteil | §§ |
|-------------|-------------|-----|
| Nachkommen (Kinder, Enkel, etc.) | **Haelfte** des gesetzlichen Erbteils | §759 ABGB |
| Ehegatte / eingetragener Partner | **Haelfte** des gesetzlichen Erbteils | §759 ABGB |
| ~~Eltern~~ | ~~Seit ErbRÄG 2015: KEIN Pflichtteilsrecht mehr~~ | — |
| ~~Lebensgefaehrte~~ | ~~KEIN Pflichtteilsrecht~~ | — |

**Berechnung:**
1. Gesetzlichen Erbteil berechnen (als gaebe es kein Testament)
2. Davon die Haelfte = Pflichtteil
3. Beispiel: Erblasser hinterlässt Ehegatte + 2 Kinder. Gesetzlicher Erbteil Ehegatte: 1/3 → Pflichtteil: 1/6. Gesetzlicher Erbteil je Kind: 1/3 → Pflichtteil je Kind: 1/6.

### 4B: Pflichtteilsbasis — Berechnung des Nachlasswerts

Der Pflichtteil berechnet sich vom **reinen Nachlass** (§764 ABGB):
1. **Aktiva:** Alle Vermoegenswerte zum Todeszeitpunkt (Verkehrswert)
2. **- Passiva:** Schulden des Erblassers, Begräbniskosten, Verfahrenskosten
3. **= Reiner Nachlass**
4. **+ Hinzurechnung von Schenkungen** (§781ff ABGB — siehe Step 4D)
5. **= Bemessungsgrundlage fuer den Pflichtteil**

### 4C: Stundung des Pflichtteils (§766 ABGB)

- Pflichtteil kann auf Antrag des Erben **gestundet** werden
- **Maximal 5 Jahre**, in besonderen Faellen **bis zu 10 Jahre** (§766 Abs 1 ABGB)
- **Verzinsung:** gesetzliche Zinsen (4% p.a., §1000 ABGB) ab dem Tod des Erblassers
- Stundung ist vom Gericht zu bewilligen, wenn die sofortige Zahlung den Erben unbillig hart treffen wuerde (z.B. Immobilie muesste verkauft werden)
- **Ratenzahlung** kann angeordnet werden (§766 Abs 2 ABGB)

### 4D: Schenkungsanrechnung (§§781ff ABGB)

**Schenkungen zu Lebzeiten koennen den Pflichtteil erhoehen!**

**An Pflichtteilsberechtigte (§781 ABGB):**
- Schenkungen an Pflichtteilsberechtigte werden dem Nachlass **zeitlich unbegrenzt** hinzugerechnet
- Bewertung: Wert zum Zeitpunkt der Schenkung, **aufgewertet** auf den Todeszeitpunkt (§788 ABGB)

**An Dritte (§782 ABGB):**
- Schenkungen an Nicht-Pflichtteilsberechtigte werden nur hinzugerechnet, wenn sie innerhalb der **letzten 2 Jahre** vor dem Tod erfolgten
- Danach: abschmelzend (pro Jahr 1/2 weniger? — Nein: die 2-Jahres-Frist ist eine harte Grenze, keine Abschmelzung)

**Schenkung auf den Todesfall (§603 ABGB):**
- Wird wie eine letztwillige Verfuegung behandelt, nicht wie eine Schenkung unter Lebenden
- Ist daher IMMER in die Pflichtteilsberechnung einzubeziehen (keine Fristbeschraenkung)
- Benoetigt Notariatsaktform oder wirkliche Uebergabe

**Ausnahmen von der Anrechnung (§783 ABGB):**
- Schenkungen, die der Erblasser aus sittlicher Pflicht oder Anstandspflicht gemacht hat
- Uebliche Gelegenheitsgeschenke (nicht unverhältnismässig)

### 4E: Pflichtteilsminderung (§776 ABGB)

Der Pflichtteil kann auf die **Haelfte** gemindert werden, wenn:
- Zu **keiner Zeit** ein Naeheverhältnis zwischen Erblasser und Pflichtteilsberechtigtem bestand, wie es zwischen solchen Angehoerigen gewoehnlich besteht
- **ODER** das Naheverhältnis ueber einen laengeren Zeitraum vor dem Tod nicht bestanden hat
- Der Mangel des Naeheverhältnisses darf **nicht vom Erblasser** verursacht worden sein
- Muss letztwillig verfuegt werden (§776 Abs 1 ABGB)
- **Wirkung:** Pflichtteil wird auf 1/4 des gesetzlichen Erbteils (statt 1/2) reduziert

### 4F: Enterbung (§§769-772 ABGB)

**Enterbungsgruende (§770 ABGB):**

| Grund | Beschreibung | §§ |
|-------|-------------|-----|
| 1 | Strafbare Handlung gegen den Erblasser, dessen Ehegatten/Partner, Verwandte in gerader Linie, die nur vorsaetzlich begangen werden kann und mit mehr als 1 Jahr Freiheitsstrafe bedroht ist | §770 Z 1 ABGB |
| 2 | Absichtliche Vereitelung des letzten Willens des Erblassers | §770 Z 2 ABGB |
| 3 | Gegen den Erblasser gerichtete sonstige schwerere strafbare Handlung gegen Leib und Leben oder Freiheit | §770 Z 3 ABGB |
| 4 | Gröbliche Vernachlässigung familienrechtlicher Pflichten gegenueber dem Erblasser | §770 Z 4 ABGB |

- Enterbung muss letztwillig verfuegt werden (§769 ABGB)
- Angabe des Grundes erforderlich (§771 ABGB)
- Beweislast fuer den Enterbungsgrund liegt beim Erben (§771 Abs 2 ABGB)
- **Verzeihung (§772 ABGB):** Hat der Erblasser dem Pflichtteilsberechtigten verziehen, ist die Enterbung unwirksam

### 4G: Erbunwuerdigkeit (§§539-541 ABGB)

Erbunwuerdigkeit tritt **von Gesetzes wegen** ein (nicht durch letztwillige Verfuegung):

- **§540 ABGB:** Wer gegen den Erblasser eine strafbare Handlung nach §770 ABGB begangen hat
- **§541 ABGB:** Wer den Erblasser durch arglistige Tauschung, Zwang oder Drohung zu einer letztwilligen Verfuegung bewogen oder daran gehindert hat
- Der Erbunwuerdige wird behandelt, als waere er vor dem Erblasser verstorben → seine Nachkommen koennen an seine Stelle treten (Repraesentation)
- **Verzeihung (§540 Abs 2 ABGB):** Erbunwuerdigkeit entfaellt bei Verzeihung durch den Erblasser

### 4H: Erbverzicht (§§551-552 ABGB)

- Vertrag zwischen Erblasser und kuenftigem Erben ueber den Verzicht auf das Erbrecht
- **Notariatsaktpflicht** (§551 Abs 1 ABGB)
- Kann auf das gesamte Erbrecht oder nur auf den Pflichtteil verzichtet werden
- Erbverzicht erstreckt sich im Zweifel auch auf die Nachkommen des Verzichtenden (§551 Abs 2 ABGB)
- **Pflichtteilsverzicht** haeufig bei Hofuebergaben, Unternehmensuebergaben, Scheidungsfolgenvereinbarungen
- Verzicht kann entgeltlich oder unentgeltlich erfolgen

---

## Step 5: Erbschaftsteuer und Schenkungsmeldepflicht

### Erbschaftsteuer — ABGESCHAFFT

- In Oesterreich seit **1. August 2008 ABGESCHAFFT** (VfGH-Erkenntnis G 54/06 vom 7.3.2007, Aufhebung des ErbStG)
- Es faellt **KEINE Erbschaftsteuer** an — weder auf Immobilien noch auf Bankguthaben, Wertpapiere, Unternehmensanteile etc.
- **ABER:** Grunderwerbsteuer bei Immobilienuebergang (GrEStG §1 Abs 1 Z 2):
  - **Stufentarif (§7 Abs 1 Z 2 lit a GrEStG):** bei Erwerben im Familienkreis / von Todes wegen: 0,5% bis €250.000, 2% bis €400.000, 3,5% darueber
  - Bemessungsgrundlage: **Grundstueckswert** (nicht Verkehrswert, §4 GrEStG iVm GrBewG)
- **Eintragungsgebuehr Grundbuch:** 1,1% vom Verkehrswert (§26 GGG)

### Schenkungsmeldepflicht (§121a BAO)

- Schenkungen unter Lebenden muessen dem Finanzamt **gemeldet** werden, wenn sie bestimmte Wertgrenzen ueberschreiten
- **Meldepflichtig (§121a Abs 1 BAO):**
  - Schenkungen zwischen Angehoerigen (§25 BAO): wenn Wert **€50.000** innerhalb eines Jahres uebersteigt
  - Schenkungen an andere Personen: wenn Wert **€15.000** innerhalb von 5 Jahren uebersteigt
- **Meldefrist:** 3 Monate ab Ausfuehrung der Schenkung
- **Strafe bei Nichtmeldung:** Finanzordnungswidrigkeit (§49a FinStrG), bis zu 10% des Wertes der Schenkung
- **KEINE Steuer** — es ist nur eine Meldepflicht, keine Steuerpflicht

---

## Step 6: Present Findings

```markdown
# Erbrechtliche Analyse

**Erblasser:** [Name, Todesdatum]
**Anwendbares Recht:** Oesterreichisches Erbrecht (ABGB) [ggf. EU-ErbVO Bezug]
**Letztwillige Verfuegung:** [Testament / Erbvertrag / keines]
**Gesetzliche Erben:** [Auflistung mit Verwandtschaftsgrad]

## Zusammenfassung
[2-3 Saetze: Wer erbt was, Pflichtteilsansprueche, Hauptstreitpunkte]

## Erbfolge

### Gesetzliche Erbfolge (hypothetisch)
| Erbe | Verwandtschaftsgrad | Parentel | Gesetzlicher Erbteil |
|------|--------------------| ---------|---------------------|
| [Name] | [Ehegatte/Kind/etc.] | [1./2./etc.] | [Bruch] |

### Testamentarische Erbfolge (wenn Testament vorhanden)
| Bedachter | Zuwendung | Art |
|-----------|-----------|-----|
| [Name] | [Was/Anteil] | [Erbe/Legat/Auflage] |

## Pflichtteilsberechnung
| Pflichtteilsberechtigter | Gesetzlicher Erbteil | Pflichtteil (1/2) | Schenkungszurechnung | Gesamtanspruch |
|--------------------------|---------------------|-------------------|---------------------|---------------|
| [Name] | [Bruch] | [Bruch] | €[x] | €[x] |

**Bemessungsgrundlage:**
| Position | Betrag |
|----------|--------|
| Aktiva des Nachlasses | €[x] |
| - Passiva (Schulden, Kosten) | -€[x] |
| = Reiner Nachlass | €[x] |
| + Hinzuzurechnende Schenkungen (§§781ff) | +€[x] |
| **= Pflichtteilsbasis** | **€[x]** |

## Steuerliche Aspekte
| Position | Betrag | Grundlage |
|----------|--------|-----------|
| Erbschaftsteuer | **€0 (abgeschafft)** | VfGH G 54/06 |
| Grunderwerbsteuer (falls Immobilie) | €[x] | §7 Abs 1 Z 2 GrEStG |
| Grundbucheintragung | €[x] | §26 GGG |
| Schenkungsmeldepflicht | [ja/nein] | §121a BAO |

## Streitpunkte und Risiken
- [z.B. "Gültigkeit des fremdhändigen Testaments: Waren 3 Zeugen gleichzeitig anwesend?"]
- [z.B. "Pflichtteilsminderung: War das Naeheverhältnis tatsaechlich gestört?"]
- [z.B. "Schenkungsanrechnung: Liegt der Wert der Schenkung ueber der 2-Jahres-Frist?"]

## Handlungsempfehlungen
1. [Konkrete Handlung mit Frist]
2. [Konkrete Handlung]
3. [Rechtsanwalt/Notar konsultieren fuer ...]

## Quellenstatus
| Kategorie | Status | Details |
|-----------|--------|---------|
| RIS MCP | 🟢 Verfuegbar / 🔴 Nicht verfuegbar | [connection status] |
| Gesetze | RIS_VERIFIED / OFFICIAL_WEB_VERIFIED / UNVERIFIED | [n] Normen geprueft |
| Judikatur | RIS_VERIFIED / OFFICIAL_WEB_VERIFIED / UNVERIFIED | [n] Entscheidungen |
| Pruefdatum | [YYYY-MM-DD] | |

---
⚠️ **Keine Rechtsberatung.** Diese Analyse dient der erbrechtlichen Ersteinschätzung und ersetzt nicht die Beratung durch einen Rechtsanwalt oder Notar. Insbesondere bei Testamentserrichtung, Pflichtteilsstreitigkeiten und Verlassenschaftsverfahren wird professionelle Rechtsvertretung empfohlen. Aktuelle Gesetze auf [ris.bka.gv.at](https://www.ris.bka.gv.at) pruefen.
```

---

## Critical Rules

1. **Always cite specific §§ with Gesetzesname** — Never "laut Erbrecht" without §732 ABGB, §759 ABGB, etc.
2. **Erbschaftsteuer ist ABGESCHAFFT** — Seit 2008 gibt es in Oesterreich KEINE Erbschaftsteuer. Niemals behaupten, dass Erbschaftsteuer anfaellt. ABER: Grunderwerbsteuer bei Immobilien und Schenkungsmeldepflicht (§121a BAO) erwaehnen.
3. **Pflichtteil ist IMMER Geldanspruch** — Der Pflichtteil ist ein schuldrechtlicher Anspruch auf Geld, KEIN Anspruch auf Naturalleistung oder Sachuebergabe (§761 ABGB). Der Pflichtteilsberechtigte wird nicht Miteigentuemer.
4. **Eltern haben seit ErbRÄG 2015 KEIN Pflichtteilsrecht mehr** — Nur Nachkommen und Ehegatte/eingetragener Partner sind pflichtteilsberechtigt (§759 ABGB).
5. **Lebensgefaehrte hat KEIN Pflichtteilsrecht** — Nur ausserordentliches gesetzliches Erbrecht bei Fehlen aller gesetzlichen Erben (§748 ABGB) und 1-Jahres-Wohnrecht (§745 Abs 2 ABGB).
6. **Fremdhändiges Testament: 3 Zeugen GLEICHZEITIG anwesend** — §579 ABGB. Nicht 3 Zeugen nacheinander. Haeufigster Formfehler.
7. **Erbvertrag nur zwischen Ehegatten + Notariatsakt** — §1249 ABGB. Ein "Erbvertrag" zwischen Nichtehegatten ist KEIN Erbvertrag im Rechtssinne.
8. **Schenkungen an Pflichtteilsberechtigte: ZEITLICH UNBEGRENZT anrechenbar** — §781 ABGB. Die 2-Jahres-Frist gilt nur fuer Schenkungen an Dritte (§782 ABGB).
9. **Pflichtteilsminderung ≠ Enterbung** — Minderung (§776) erfordert fehlendes Naeheverhältnis, Enterbung (§770) erfordert schwere Verfehlungen. Nicht verwechseln.
10. **Use RIS if connected** — Verify statute citations are current, especially nach ErbRÄG 2015 Aenderungen.
11. **Match user's language** — German in → German out. English in → English out. Gesetze immer in deutscher Form (§732 ABGB).
