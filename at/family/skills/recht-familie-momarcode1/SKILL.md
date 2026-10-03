---
name: recht-familie-momarcode1
title: /recht familie — Familienrecht (Advisory)
description: Austrian family law analysis — divorce (EheG), alimony/maintenance (Unterhalt), child custody (Obsorge), contact rights (Kontaktrecht), child support (Kindesunterhalt), prenuptial agreements, division of marital property (§§81-98 EheG), and paternity.
author: MoMarcode1
author_url: https://github.com/MoMarcode1/austrian-legal-claude/tree/main/skills/recht-familie
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: at
practice: family
language: de
sources:
- title: Evidence protocol
  path: references/evidence-protocol.md
- title: Ogh case presentation
  path: references/ogh-case-presentation.md
- title: Ris protocol
  path: references/ris-protocol.md
---

# /recht familie — Familienrecht (Advisory)

When the user describes a family law situation (divorce, custody, maintenance, property division, domestic violence, paternity), follow these steps exactly.

---

## Step 1: Gather the Facts

Read everything the user has provided. You need:

1. **Who?** — Parties involved, married or unmarried, children (ages!), nationalities, residence in Austria?
2. **What is the situation?** — Separation, divorce, custody dispute, maintenance claim, property division, domestic violence, paternity question?
3. **Marriage details** — When married, where, any prenuptial agreement (Ehevertrag/Ehepakt)? Duration of marriage? Still living together (gemeinsamer Haushalt)?
4. **Children** — Ages, who are they living with, current Obsorge arrangement, any existing court orders?
5. **Financial situation** — Income of both parties (net monthly), assets, debts, who earns more, who cared for children/household?
6. **Timeline** — When did separation occur? Any pending proceedings? Any urgent threats (Gewalt)?
7. **What does the user want?** — Divorce, custody, maintenance, property division, protection?

If any critical element is missing, ask. Be specific:
> "Wie alt sind die Kinder? Das ist entscheidend fuer die Unterhaltsberechtigung und Obsorge."
> "Wie hoch ist das monatliche Nettoeinkommen beider Ehepartner? Ohne diese Angabe kann der Unterhalt nicht berechnet werden."
> "Liegt ein Ehevertrag oder Ehepakt vor? Das beeinflusst die Vermoegensaufteilung erheblich."

Do NOT begin analysis until you have enough facts.

---

## Step 2: RIS Verification

Before proceeding with analysis, follow the **RIS Verification Protocol** (`references/ris-protocol.md`):
1. Check RIS MCP availability
2. For every § you cite in this analysis, verify current wording via RIS
3. For case law references (OGH), retrieve via RIS Justiz
4. Record verification status for the Quellenstatus block
5. If RIS is unavailable, follow the fallback ladder and flag all affected citations

Search RIS Justiz for relevant OGH-Entscheidungen zu den zentralen Rechtsfragen. Present using format from `references/ogh-case-presentation.md`.

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

Determine which areas of family law are relevant. Multiple areas often overlap — check all of them.

### A: Scheidung (EheG)

#### A1: Einvernehmliche Scheidung (§55a EheG)
- **Voraussetzungen:**
  - Ehe unheilbar zerrüttet
  - Eheliche Lebensgemeinschaft seit mindestens 6 Monaten aufgehoben (§55a Abs 1 EheG)
  - Beide Ehegatten beantragen die Scheidung einvernehmlich
  - Scheidungsvergleich ueber ALLE Folgen (§55a Abs 2 EheG):
    - Aufteilung eheliches Gebrauchsvermoegen und eheliche Ersparnisse
    - Unterhalt zwischen Ehegatten (oder Verzicht)
    - Obsorge fuer gemeinsame minderjaehrige Kinder
    - Kontaktrecht
    - Kindesunterhalt
    - Ehewohnung
- **Zustaendigkeit:** Bezirksgericht (BG) am Wohnsitz
- **Vorteil:** Kein Verschuldensausspruch, schneller, guenstiger

#### A2: Streitige Scheidung

- **Scheidung wegen Verschuldens (§49 EheG)**
  - Schwere Eheverfehlung (Ehebruch, koerperliche Gewalt, psychische Gewalt, Trunksucht, boesliches Verlassen)
  - Die Verfehlung muss die Ehe zerrüttet haben (Kausalzusammenhang)
  - Frist: Klage binnen 6 Monaten ab Kenntnis des Scheidungsgrundes, spaetestens 10 Jahre (§57 EheG)
  - Verzeihung schliesst den Scheidungsgrund aus (§56 EheG)

- **Scheidung wegen Aufhebung der Lebensgemeinschaft (§55 EheG)**
  - Lebensgemeinschaft seit mindestens 3 Jahren aufgehoben
  - Haertefallklausel: Kann verweigert werden, wenn der schuldlose Ehegatte durch die Scheidung besonders hart getroffen wuerde (§55 Abs 3 EheG) — praktisch selten
  - Nach 6 Jahren: Scheidung ohne Haertefallpruefung (§55 Abs 3 letzter Satz EheG)

- **Scheidung wegen anderer Gruende**
  - §50 EheG: Geisteskrankheit (praktisch kaum relevant)
  - §51 EheG: Ansteckende oder ekelerregende Krankheit (praktisch kaum relevant)

- **Verschuldensprinzip:**
  - Gericht spricht Verschulden aus: alleiniges, ueberwiegendes, oder gleichteiliges Verschulden
  - Verschuldensausspruch wirkt sich auf nachehelichen Unterhalt aus (§§66-69 EheG)
  - Alleinverschulden: Unterhaltspflicht des Schuldigen (§66 EheG)
  - Ueberwiegendes Verschulden: Unterhaltspflicht des ueberwiegend Schuldigen (§67 EheG)
  - Gleichteiliges Verschulden: Billigkeitsunterhalt moeglich (§68 EheG)
  - Scheidung ohne Verschulden (§55 EheG): Klaeger gilt als schuldig (§61 Abs 3 EheG) — wichtige Folge fuer Unterhalt!

### B: Unterhalt

#### B1: Ehegattenunterhalt bei aufrechter Ehe (§94 ABGB)
- Grundsatz: Angemessener Unterhalt nach Lebensverhaeltnissen und Leistungsfaehigkeit
- Anspruch auch bei Getrenntleben ohne Scheidung
- Berechnung nach der Prozentwertmethode (OGH-Judikatur):
  - Dem unterhaltsberechtigten Ehegatten stehen **33%** des Nettoeinkommens des Unterhaltspflichtigen zu
  - Abzuege fuer weitere Sorgepflichten (pro Kind ca. 1-3% je nach Alter)
  - Eigeneinkommen des Berechtigten wird angerechnet (Anspannungsgrundsatz)

#### B2: Nachehelicher Unterhalt (§§66-69 EheG)
- **§66 EheG — Alleinverschulden:** Der allein schuldige Teil muss Unterhalt leisten, soweit der andere Teil seinen Unterhalt nicht selbst bestreiten kann
- **§67 EheG — Ueberwiegendes Verschulden:** Der ueberwiegend schuldige Teil muss Unterhalt leisten
- **§68 EheG — Gleichteiliges Verschulden:** Billigkeitsunterhalt — Gericht KANN Unterhalt zusprechen, wenn ein Teil sich nicht selbst erhalten kann und dies der Billigkeit entspricht
- **§69 EheG — Einvernehmliche Scheidung:** Richtet sich nach dem Scheidungsvergleich
- **§69a EheG — Scheidung nach §55 EheG:** Klaeger (der die Zerrüttung "verursacht" hat) zahlt Unterhalt wie bei Alleinverschulden
- **Berechnung:**
  - Prozentwertmethode: **33%** des Nettoeinkommens des Unterhaltspflichtigen
  - Abzuege fuer Sorgepflichten
  - Eigeneinkommen angerechnet
  - Luxusgrenze (Unterhaltsrechtliche Begrenzung): Ca. EUR 4.500-5.000 netto — darueber hinaus kein Anspruch (OGH 3 Ob 178/16w)
  - Anspannungsgrundsatz: Berechtigter muss zumutbare Erwerbstaetigkeit aufnehmen
- **Dauer:** Grundsaetzlich unbefristet, aber Gericht kann befristen (bei kurzer Ehe ohne Kinder, bei Selbsterhaltungsfaehigkeit)
- **Ende:** Wiederverheiratung des Berechtigten (§75 EheG), Tod, Verwirkung durch unwuerdiges Verhalten

#### B3: Kindesunterhalt (§231 ABGB)
- **Anspruchsgrundlage:** §231 ABGB — Beide Eltern tragen zum Unterhalt bei
- **Naturbeitraege:** Der Elternteil, der das Kind betreut und im Haushalt hat, leistet seinen Beitrag durch Betreuung (§231 Abs 2 ABGB)
- **Geldbeitraege:** Der andere Elternteil leistet Geldunterhalt
- **Berechnung — Prozentwertmethode (OGH-Judikatur):**
  - 0-5 Jahre: **16%** des Nettoeinkommens des Unterhaltspflichtigen
  - 6-9 Jahre: **18%**
  - 10-14 Jahre: **20%**
  - ab 15 Jahre: **22%**
  - Abzuege fuer weitere Sorgepflichten (1-3% pro weiteres Kind, 0-3% fuer Ehegatten)
- **Regelbedarfssaetze (jaehrlich angepasst):**
  - Vom BMJ jaehrlich per Erlass festgelegt
  - Dienen als Mindestrichtwert und Grundlage fuer Unterhaltsvorschuss
  - Aktuellen Stand immer ueber RIS oder BMJ prüfen
- **Luxusgrenze (Playboygrenze):**
  - Der Unterhalt ist mit dem 2- bis 2,5-fachen des Regelbedarfs begrenzt (OGH 1 Ob 5/15d)
  - Darueber hinausgehende Beduerfnisse: Sonderbedarf moeglich (z.B. Krankheitskosten, Ausbildung)
- **Sonderbedarf (§231 ABGB):**
  - Nicht im Regelbedarf enthalten: Zahnspange, Brille, Nachhilfe, Schullandwoche, etc.
  - Muss gesondert geltend gemacht werden
  - Anteilig nach Leistungsfaehigkeit beider Eltern
- **Eigeneinkommensanrechnung des Kindes:** Ab Eigenverdienst wird Unterhalt gekuerzt
- **Volljahrige Kinder:** Unterhalt besteht waehrend Ausbildung weiter (§231 ABGB), angemessene Ausbildungsdauer

### C: Obsorge (§§177ff ABGB)

- **Grundsatz: Kindeswohl (§138 ABGB) ist der oberste Masssstab**
  - Kriterien des Kindeswohls (§138 ABGB):
    1. Angemessene Versorgung (Pflege, Erziehung, Beaufsichtigung)
    2. Fuersorge, Geborgenheit, Schutz der koerperlichen und seelischen Integritaet
    3. Wertschaetzung und Akzeptanz durch die Eltern
    4. Foerderung der Anlagen, Faehigkeiten, Neigungen, Entwicklungsmoeglichkeiten
    5. Beruecksichtigung der Meinung des Kindes (je nach Alter und Reife)
    6. Vermeidung der Beeintraechtigung durch Loyalitaetskonflikte
    7. Vermeidung der Gefahr von Gewalt und sonstigem Missbrauch
    8. Verlaessliche Kontakte zu beiden Elternteilen und wichtigen Bezugspersonen
    9. Vermeidung von Veraenderungen der Lebensumstaende (Kontinuitaetsprinzip)

- **Gemeinsame Obsorge (§177 Abs 1 ABGB):**
  - Bei verheirateten Eltern: Automatisch beide Eltern obsorgeberechtigt
  - Nach Scheidung: Gemeinsame Obsorge bleibt aufrecht, sofern nicht anderes beantragt wird
  - Seit KindNamRÄG 2013: Gemeinsame Obsorge ist der Regelfall auch nach Trennung
  - Gericht MUSS gemeinsame Obsorge anordnen, wenn es dem Kindeswohl entspricht

- **Alleinige Obsorge:**
  - Nur wenn gemeinsame Obsorge dem Kindeswohl widerspricht
  - Z.B. bei Gewalt, schwerer Vernachlaessigung, voelligem Kommunikationsversagen
  - Antrag beim BG (Pflegschaftsgericht)

- **Uneheliche Kinder (§177 Abs 2-4 ABGB):**
  - Obsorge zunächst bei der Mutter allein
  - Gemeinsame Obsorge: Durch Vereinbarung der Eltern (§177 Abs 2 ABGB) oder gerichtliche Bestimmung (§177 Abs 3 ABGB)
  - Vater kann Antrag auf gemeinsame Obsorge oder alleinige Obsorge stellen

- **Phase der vorlaeufigen elterlichen Verantwortung (§180 ABGB):**
  - Bei Antrag eines Elternteils auf alleinige Obsorge: Gericht bestimmt vorlaeufig den hauptsaechlich betreuenden Elternteil
  - Dauer: 6 Monate (§180 Abs 1 ABGB)
  - Nach Ablauf: Gericht entscheidet endgueltig
  - Familiengerichtshilfe wird eingeschaltet (§106a AusserStrG)

- **Obsorge und Pflegeeltern/Grosseltern (§184 ABGB):**
  - Obsorge kann auf Pflegeeltern uebertragen werden (§184 ABGB)
  - Grosseltern: Kontaktrecht ja, Obsorge nur in Ausnahmefaellen

### D: Kontaktrecht (§187 ABGB)

- **Grundsatz:** Kontaktrecht ist ein Recht des KINDES auf persoenlichen Verkehr mit beiden Elternteilen
- **§187 ABGB:** Jeder Elternteil und das Kind haben das Recht auf regelmaessigen persoenlichen Kontakt
- **Regelung:** Durch Vereinbarung der Eltern oder durch gerichtliche Festsetzung (BG als Pflegschaftsgericht)
- **Umfang:** Richtet sich nach dem Kindeswohl, dem Alter des Kindes, der Entfernung der Wohnsitze, dem bisherigen Kontaktmuster
- **Typische Regelungen:**
  - Jedes zweite Wochenende (Freitag bis Sonntag)
  - Ein Nachmittag unter der Woche
  - Ferienregelung (halbe Ferien)
  - Feiertage im Wechsel
- **Kontaktrecht Dritter (§188 ABGB):** Grosseltern und andere Bezugspersonen koennen Kontaktrecht beantragen, wenn es dem Kindeswohl dient
- **Einschraenkung/Ausschluss (§187 Abs 2 ABGB):** Kontaktrecht kann eingeschraenkt oder entzogen werden, wenn das Kindeswohl gefaehrdet ist (Gewalt, Missbrauch, Entfuehrungsgefahr)
- **Begleiteter Kontakt (Besuchsbegleitung):** Vom Gericht angeordnet, wenn unbegleiteter Kontakt riskant waere

### E: Aufteilung des ehelichen Gebrauchsvermoegens und der ehelichen Ersparnisse (§§81-98 EheG)

- **Grundsatz (§81 EheG):** Eheliches Gebrauchsvermoegen und eheliche Ersparnisse werden nach Billigkeit aufgeteilt
- **Zeitpunkt:** Aufteilung erfolgt NACH rechtskraeftiger Scheidung
- **Frist: 1 Jahr ab Rechtskraft der Scheidung (§95 EheG) — PRAEEKLUSIVFRIST!**

#### Was wird aufgeteilt:
- **Eheliches Gebrauchsvermoegen (§81 Abs 2 EheG):**
  - Ehewohnung (unabhaengig vom Eigentum!)
  - Hausrat
  - Gemeinsam genutzter PKW
  - Alles, was dem ehelichen Gebrauch diente
- **Eheliche Ersparnisse (§81 Abs 3 EheG):**
  - Waehrend der Ehe angesammelte Wertanlagen (Sparbuecher, Aktien, Lebensversicherungen, Pensionsanwartschaften)
  - Wertzuwachs an vorher eingebrachtem Vermoegen (OGH 1 Ob 104/18w — Wertzuwachs ist aufzuteilen)

#### Was wird NICHT aufgeteilt (§82 EheG):
- Sachen, die ein Ehegatte **in die Ehe eingebracht** hat
- Sachen, die ein Ehegatte von Todes wegen (Erbschaft) **erworben** hat
- Sachen, die ein Ehegatte von einem Dritten **geschenkt** bekommen hat
- Sachen, die dem persoenlichen Gebrauch eines Ehegatten oder der Berufsausuebung dienen
- **ABER:** Ehewohnung und Hausrat koennen IMMER aufgeteilt werden, auch wenn eingebracht oder geerbt (§82 Abs 2 EheG)
- **ABER:** Unternehmen und Unternehmensanteile sind grundsaetzlich nicht aufzuteilen (§82 Abs 1 Z 3 EheG), Ertraege jedoch schon

#### Billigkeitsgrundsatz (§83 EheG):
- Gewicht und Umfang der Beitraege jedes Ehegatten
- Kindererziehung und Haushaltsfuehrung sind gleichwertige Beitraege (§83 Abs 1 EheG)
- Wohl der Kinder ist zu beruecksichtigen
- Schulden werden ebenfalls aufgeteilt (§81 EheG)
- Richtwert: Oft 50:50, aber nicht automatisch — Billigkeitspruefung im Einzelfall

#### Ehewohnung (§§87-90 EheG):
- Kann einem Ehegatten zur Gaenze zugewiesen werden (Wohnungszuweisung)
- Beruecksichtigung des Kindeswohls (wer bleibt mit den Kindern dort?)
- Ausgleichszahlung an den anderen Ehegatten moeglich
- Mietrechte koennen uebertragen werden

### F: Ehevertrag / Ehepakt

- **Guetergemeinschaft (§§1233ff ABGB):**
  - In Oesterreich NICHT der gesetzliche Normalfall (anders als z.B. Deutschland)
  - Gesetzlicher Gueterstand in Oesterreich: **Guetertrennung** waehrend der Ehe
  - Guetergemeinschaft muss per Notariatsakt vereinbart werden
  - Guetergemeinschaft unter Lebenden oder auf den Todesfall moeglich

- **Guetertrennung:**
  - Gesetzlicher Normalfall waehrend aufrechter Ehe
  - Jeder Ehegatte verwaltet sein Vermoegen selbst
  - BEI SCHEIDUNG greift aber das Aufteilungsrecht (§§81-98 EheG) ein!

- **Ehepakt / Ehevertrag:**
  - Muss per Notariatsakt errichtet werden (§1 NZwG iVm §1217 ABGB)
  - Kann Aufteilungsregeln modifizieren
  - Kann Unterhaltsverzicht enthalten (bei einvernehmlicher Scheidung wirksam, bei streitiger Scheidung nur eingeschraenkt)
  - **Grenzen:** Sittenwidrigkeit (§879 ABGB), grobe Benachteiligung, Auswirkungen auf Kindesunterhalt nicht abdingbar

### G: Vaterschaft

- **Eheliche Vaterschaft (§138 ABGB aF / §144 ABGB):**
  - Ehemann der Mutter gilt als Vater des waehrend der Ehe geborenen Kindes
  - Bestreitungsfrist: 2 Jahre ab Kenntnis der Umstaende (§159 ABGB)

- **Anerkennung der Vaterschaft (§145 ABGB):**
  - Persoenliche Erklaerung des Vaters vor dem Standesamt oder Gericht oder in oeffentlicher Urkunde
  - Zustimmung der Mutter bei minderjaehrigem Kind (§145 Abs 2 ABGB)
  - Anfechtung durch das Kind oder den Anerkennenden moeglich (§154 ABGB)

- **Gerichtliche Feststellung der Vaterschaft (§148 ABGB):**
  - Antrag des Kindes (vertreten durch Mutter oder KJH)
  - DNA-Gutachten als Beweismittel
  - Vaterschaft kann auch gegen den Willen des Mannes festgestellt werden
  - Rueckwirkender Unterhaltsanspruch ab Geburt (§231 ABGB)

### H: Schutz vor Gewalt

- **Einstweilige Verfuegung (§382b EO):**
  - Schutz vor Gewalt in Wohnungen
  - Gericht ordnet an: Verlassen der Wohnung, Rueckkehrverbot, Kontaktverbot, Aufenthaltsverbot im Umkreis
  - Antrag beim BG (Familienabteilung)
  - Dauer: Bis zu 6 Monate (§382b Abs 3 EO), verlaengerbar auf 1 Jahr bei Hauptverfahren

- **§382c EO — Schutz vor Gewalt allgemein (nicht nur Wohnung):**
  - Kontaktverbot, Aufenthaltsverbot an bestimmten Orten (Schule, Arbeitsplatz)

- **§382d EO — Schutz vor Eingriffen in die Privatsphäre:**
  - Stalking-Schutz
  - Verbot der Kontaktaufnahme ueber Dritte, Telekommunikation, Social Media

- **Polizeiliches Betretungs- und Annaeherungsverbot (§38a SPG):**
  - Polizei spricht sofort Betretungsverbot aus (14 Tage, verlaengerbar auf 4 Wochen)
  - Anordnung OHNE Gerichtsbeschluss durch Polizei
  - Betroffene Person muss sich an Gewaltschutzzentrum wenden (wird automatisch kontaktiert)
  - Provisorischer Schutz bis einstweilige Verfuegung beantragt werden kann

- **Gewaltschutzzentren:**
  - Kostenlose Beratung und Begleitung fuer Opfer
  - Proaktive Kontaktaufnahme nach polizeilichem Betretungsverbot
  - In jedem Bundesland vertreten

---

## Step 4: Analyze the Specific Situation

Based on the classification from Step 3, analyze systematically. Apply ALL relevant areas.

### For Scheidung:
1. **Einvernehmlich moeglich?** — Sind beide Parteien bereit? 6-Monats-Frist der Aufhebung erfuellt?
2. **Verschuldensfrage** — Welche Eheverfehlungen liegen vor? Wessen Verschulden ueberwiegt?
3. **Auswirkung auf Unterhalt** — Verschuldensausspruch bestimmt den nachehelichen Unterhaltsanspruch
4. **Scheidungsfolgen** — Welche Vereinbarungen muessen getroffen werden?

### For Unterhalt:
1. **Anspruchsgrundlage** — Welcher Unterhaltstatbestand (§94 ABGB, §§66-69 EheG, §231 ABGB)?
2. **Berechnung** — Nettoeinkommen, Prozentwertmethode, Abzuege fuer Sorgepflichten
3. **Anspannungsgrundsatz** — Muss der Berechtigte arbeiten? Zumutbare Erwerbstaetigkeit?
4. **Sonderbedarf** — Gibt es aussergewoehnliche Beduerfnisse (Kinder: Krankheit, Ausbildung)?
5. **Luxusgrenze** — Pruefe Obergrenzen

### For Obsorge:
1. **Kindeswohl-Pruefung (§138 ABGB)** — Alle 9 Kriterien systematisch durchgehen
2. **Bisherige Betreuungssituation** — Wer war Hauptbezugsperson? Kontinuitaetsprinzip!
3. **Elternkompetenz** — Kooperationsfaehigkeit, Bindungstoleranz (Foerderung des Kontakts zum anderen Elternteil)
4. **Kindesmeinung** — Ab ca. 10 Jahren: Kind wird befragt (ab 14: Wille hat hohes Gewicht)
5. **Gefaehrdung** — Gewalt, Vernachlaessigung, Sucht, psychische Erkrankung?

### For Kontaktrecht:
1. **Alter des Kindes** — Bestimmt Umfang und Art des Kontakts
2. **Bisheriges Kontaktmuster** — Was war bisher ueblich?
3. **Entfernung** — Wohnsitze der Eltern
4. **Gefaehrdung** — Gruende fuer Einschraenkung oder begleiteten Kontakt?
5. **Kindeswille** — Aeusserungen des Kindes (altersabhaengig zu gewichten)

### For Vermoegensaufteilung:
1. **Bilanz erstellen** — Was ist eheliches Gebrauchsvermoegen, was eheliche Ersparnisse?
2. **Ausnahmen pruefen (§82 EheG)** — Was wurde eingebracht, geerbt, geschenkt?
3. **Ehewohnung** — Wem gehoert sie? Wer bleibt mit den Kindern?
4. **Beitraege wuerdigen** — Erwerbstaetigkeit UND Haushalt/Kindererziehung
5. **Schulden** — Gemeinsame Schulden, Schulden fuer ehelichen Aufwand
6. **Frist pruefen** — 1 Jahr ab Rechtskraft der Scheidung (§95 EheG)!

### For Gewalt:
1. **Sofortmassnahmen** — Polizei (§38a SPG), einstweilige Verfuegung (§382b EO)
2. **Gewaltschutzzentrum** — Kontakt herstellen
3. **Auswirkung auf andere Verfahren** — Gewalt beeinflusst Verschulden (Scheidung), Obsorge, Kontaktrecht

---

## Step 5: Identify Deadlines and Fristen

**Familienrecht hat mehrere kritische Fristen. Versaeumt man sie, verliert man Ansprueche.**

| Situation | Frist | Grundlage |
|-----------|-------|-----------|
| Aufteilungsantrag nach Scheidung | **1 Jahr** ab Rechtskraft der Scheidung | §95 EheG — PRAEEKLUSIVFRIST! |
| Scheidungsklage wegen Verschuldens | **6 Monate** ab Kenntnis, max. **10 Jahre** | §57 EheG |
| Bestreitung der ehelichen Vaterschaft | **2 Jahre** ab Kenntnis | §159 ABGB |
| Einstweilige Verfuegung bei Gewalt | Sofort beantragen, **14 Tage** nach Betretungsverbot fuer gerichtlichen Antrag | §382b EO |
| Unterhaltsrueckstand | **3 Jahre** Verjährung fuer rueckstaendigen Unterhalt | §1480 ABGB |
| Besitzstörung (Ehewohnung) | **30 Tage** ab Kenntnis | §454 ZPO |

**Flag every deadline within 30 days prominently at the top of the output.**

---

## Step 6: Present Results

```markdown
# Familienrechtliche Analyse

**Sachverhalt:** [2-3 Saetze Zusammenfassung]
**Beteiligte:** [Parteien, Kinder mit Alter]
**Rechtsgebiet(e):** [Scheidung / Unterhalt / Obsorge / Kontaktrecht / Aufteilung / Gewaltschutz]

## Sofort-Warnungen

[Imminent deadlines, Gewaltschutz-Bedarf, drohender Verlust von Anspruechen]

## Analyse

### Scheidung (falls relevant)
**Variante:** Einvernehmlich (§55a EheG) / Streitig (§49/§55 EheG)
**Verschuldenslage:** [Einschaetzung]
**Empfehlung:** [Welcher Weg ist im konkreten Fall vorteilhafter und warum]

### Unterhalt
#### Ehegattenunterhalt
| Parameter | Wert |
|-----------|------|
| Nettoeinkommen Pflichtiger | EUR [x] |
| Prozentwert | 33% |
| Bruttoanspruch | EUR [x] |
| Abzuege Sorgepflichten | EUR [x] |
| Eigeneinkommen Berechtigter | EUR [x] |
| **Netto-Unterhaltsanspruch** | **EUR [x]** |
| Luxusgrenze | Nicht erreicht / Ueberschritten |

#### Kindesunterhalt (pro Kind)
| Kind | Alter | Prozent | Berechnet | Regelbedarf | Anspruch |
|------|-------|---------|-----------|-------------|---------|
| [Name/Nr] | [x] J. | [x]% | EUR [x] | EUR [x] | EUR [x] |

### Obsorge (falls relevant)
**Aktuelle Situation:** [Beschreibung]
**Kindeswohl-Pruefung (§138 ABGB):**
| Kriterium | Elternteil A | Elternteil B |
|-----------|-------------|-------------|
| Versorgung | [Bewertung] | [Bewertung] |
| Geborgenheit | [Bewertung] | [Bewertung] |
| Bindungstoleranz | [Bewertung] | [Bewertung] |
| Kontinuitaet | [Bewertung] | [Bewertung] |
| Kindesmeinung | [falls relevant] | |

**Empfehlung:** [Gemeinsame / Alleinige Obsorge, Begruendung]

### Kontaktrecht (falls relevant)
**Empfohlene Regelung:** [Konkrete Besuchsregelung]
**Begruendung:** [Kindeswohl-basiert]

### Vermoegensaufteilung (falls relevant)
| Vermoegen | Art | Wert | Aufzuteilen? | Begruendung |
|-----------|-----|------|-------------|-------------|
| [Ehewohnung] | Gebrauchsvermoegen | EUR [x] | Ja | §81 EheG |
| [Sparbuch] | Ersparnisse | EUR [x] | Ja | §81 EheG |
| [Erbschaft X] | Eingebracht | EUR [x] | Nein | §82 Abs 1 Z 1 EheG |

**Aufteilungsvorschlag:** [Nach Billigkeitsgrundsatz §83 EheG]

### Gewaltschutz (falls relevant)
**Sofortmassnahmen:** [Polizei, EV, Gewaltschutzzentrum]
**Laufende Schutzmassnahmen:** [Kontaktverbot, Aufenthaltsverbot]

## Fristen-Uebersicht

| Frist | Datum | Handlung erforderlich | Konsequenz bei Versaeumnis |
|-------|-------|----------------------|---------------------------|
| [Aufteilungsantrag] | [Datum] | [Antrag beim BG stellen] | [Anspruchsverlust — Praeklusivfrist!] |

## Empfohlene Strategie

### Prioritaet 1: [Dringendste Massnahme]
- **Was:** [Konkrete Handlung]
- **Bis wann:** [Frist]
- **Begruendung:** [Warum zuerst]

### Prioritaet 2: [Naechste Massnahme]
[Same structure]

### Prioritaet 3: [Weitere Massnahme]
[Same structure]

## Naechste Schritte

- [ ] [Erste konkrete Handlung]
- [ ] [Zweite Handlung]
- [ ] [Dritte Handlung]

## Wichtige Kontakte

- **Rechtsberatung:** Rechtsanwalt fuer Familienrecht (Anwaltspflicht bei LG nicht erforderlich — BG-Verfahren ohne Anwalt moeglich, aber empfohlen)
- **Frauen-/Maennerberatung:** [Je nach Situation]
- **Gewaltschutzzentrum:** [Bundeslandabhaengig]
- **Kinder- und Jugendhilfe (KJH):** Bei Obsorge- und Kontaktrechtsfragen
- **Familienberatungsstelle:** Fuer Mediation und ausssergerichtliche Einigung

## Quellenstatus
| Kategorie | Status | Details |
|-----------|--------|---------|
| RIS MCP | Verfuegbar / Nicht verfuegbar | |
| Gesetze | RIS_VERIFIED / UNVERIFIED | [n] Normen geprueft |
| Judikatur | RIS_VERIFIED / UNVERIFIED | [n] Entscheidungen |
| Pruefdatum | [YYYY-MM-DD] | |

---
**Keine Rechtsberatung.** Diese Analyse dient der rechtlichen Ersteinschaetzung und ersetzt nicht die Beratung durch einen Rechtsanwalt. Bei Familienrechtsverfahren vor dem Bezirksgericht besteht keine Anwaltspflicht, die Hinzuziehung eines Rechtsanwalts fuer Familienrecht wird jedoch dringend empfohlen, insbesondere bei streitiger Scheidung, Obsorgeverfahren und Vermoegensaufteilung.
```

---

## Critical Rules

1. **Kindeswohl (§138 ABGB) is the paramount consideration in ALL matters involving children. Every recommendation must be evaluated through this lens.** Never suggest an arrangement that serves a parent's interest at the expense of the child's wellbeing.
2. **Always cite specific §§** — §55a EheG, §231 ABGB, §177 ABGB. Never "Austrian family law says..." without the exact section.
3. **Fristen beachten** — Die 1-Jahres-Frist fuer den Aufteilungsantrag (§95 EheG) ist eine Praeklusivfrist. Verpasst man sie, ist der Anspruch unwiederbringlich verloren. Immer prominent warnen.
4. **Unterhalt konkret berechnen** — Nicht nur "es besteht ein Anspruch" sagen, sondern mit der Prozentwertmethode eine Zahl nennen. Dafuer braucht man das Nettoeinkommen — danach fragen!
5. **Gewalt immer ernst nehmen** — Bei jedem Hinweis auf haeusliche Gewalt sofort auf §382b EO und §38a SPG hinweisen. Sicherheit geht vor Verfahrensstrategie.
6. **Einvernehmlich > Streitig** — Wenn moeglich, immer zur einvernehmlichen Scheidung raten. Sie ist schneller, guenstiger, und psychisch weniger belastend — besonders fuer Kinder.
7. **Anspannungsgrundsatz erklaeren** — Viele Laien wissen nicht, dass man sich nicht "arm machen" kann, um Unterhalt zu druecken oder zu erhoehen. Das Gericht rechnet mit dem erzielbaren Einkommen.
8. **§82 EheG genau pruefen** — Eingebrachtes, Geerbtes und Geschenktes ist NICHT aufzuteilen — aber der Wertzuwachs KANN aufzuteilen sein (OGH-Judikatur). Die Ehewohnung ist IMMER aufzuteilen, auch wenn eingebracht.
9. **Match user's language** — German in, German out. English in, English out. Statutes always in German form.
10. **Use RIS if connected** — Verify statute citations and OGH case law are current. Regelbedarfssaetze aendern sich jaehrlich — immer aktuellen Stand pruefen.
11. **Mediation empfehlen** — Bei Obsorgekonflikten und Scheidungsfolgenvereinbarungen auf Familienmediation hinweisen. Seit 2013 ist ein Schlichtungsversuch bei Obsorge-Aenderungen ueblich.
12. **Kinder anhoeren** — Ab ca. 10 Jahren muessen Kinder im Obsorgeverfahren gehoert werden. Ab 14 Jahren hat der Kindeswille besonderes Gewicht. Immer darauf hinweisen.
