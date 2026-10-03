---
name: recht-arbeit-verfahren-momarcode1
title: /recht arbeit-verfahren — Arbeitsrechtliche Verfahren
description: Austrian employment law procedures — Kuendigungsanfechtung (§105 ArbVG), Entlassungsanfechtung, ASG proceedings (ASGG), Kuendigungsentschaedigung, claiming overtime/UEL/KV differentials, einvernehmliche Aufloesung negotiation, discrimination claims (GlBG), and draft templates for Kuendigungsanfechtungsklage.
author: MoMarcode1
author_url: https://github.com/MoMarcode1/austrian-legal-claude/tree/main/skills/recht-arbeit-verfahren
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: at
practice: employment
language: de
sources:
- title: Ris protocol
  path: references/ris-protocol.md
---

# /recht arbeit-verfahren — Arbeitsrechtliche Verfahren

When the user has been terminated, dismissed, or needs to enforce employment law claims through court or other proceedings, follow these steps.

---

## Step 1: Read the Facts / Situation

Gather all relevant information:

1. **What happened?** — Kuendigung, Entlassung, einvernehmliche Aufloesung (angeboten/bereits unterschrieben?), Ansprueche offen?
2. **When?** — Datum der Kuendigung/Entlassung/Beendigung. Wann hat der AN davon erfahren? CRITICAL for Anfechtungsfristen!
3. **Who terminated?** — AG-Kuendigung, AN-Kuendigung, berechtigte/unberechtigte Entlassung, berechtigter/unberechtigter Austritt?
4. **Was there a Betriebsrat?** — §105 ArbVG Anfechtung nur moeglich, wenn BR existiert
5. **Did the BR issue a Stellungnahme?** — Zustimmung, Widerspruch, Schweigen?
6. **What is the employment relationship?** — DV-Beginn, Dauer, Gehalt, KollV, All-in, Kuendigungsfrist
7. **What claims are at stake?** — Kuendigungsentschaedigung, Ueberstunden, Urlaubsersatzleistung, KV-Differenz, Abfertigung?
8. **Evidence available?** — Dienstvertrag, Dienstzettel, Gehaltszettel, Zeitaufzeichnungen, E-Mails, Zeugen?
9. **Has there been discrimination?** — Geschlecht, Alter, Behinderung, ethnische Zugehoerigkeit, Religion, sexuelle Orientierung?
10. **AK-Mitgliedschaft / Gewerkschaftsmitgliedschaft?** — Fuer kostenlose Rechtsvertretung

If the user mentions a Kuendigung with a Betriebsrat, immediately check:
> "Wann wurde die Kuendigung ausgesprochen? Die Anfechtungsfrist betraegt nur 2 Wochen — jeder Tag zaehlt!"

---

## Step 2: RIS Verification

Before proceeding with analysis, follow the **RIS Verification Protocol** (`references/ris-protocol.md`):
1. Check RIS MCP availability
2. For every § you cite in this analysis, verify current wording via RIS
3. For case law references, retrieve via RIS Justiz (OGH Arbeitsrechtssachen — 8 ObA, 9 ObA)
4. Record verification status for the Quellenstatus block
5. If RIS is unavailable, follow the fallback ladder and flag all affected citations

Search RIS Justiz for relevant OGH decisions in Arbeitsrechtssachen.

---

## Step 3: Classify the Procedural Situation

Determine which procedural path applies. Go through each option systematically:

### A: Kuendigungsanfechtung (§105 ArbVG)

**When:** AG hat gekuendigt, es gibt einen Betriebsrat, AN will die Kuendigung anfechten.

**Voraussetzungen:**
- Betriebsrat existiert im Unternehmen (§105 ArbVG gilt nur bei Betrieben mit BR!)
- AG hat BR vorher verstaendigt (§105 Abs 1 ArbVG)
- BR hat Stellungnahme abgegeben (oder Frist ist abgelaufen)

**FRIST: 2 WOCHEN ab Zugang der Kuendigung (§105 Abs 4 ArbVG)!**
- Materiell-rechtliche Frist — NICHT erstreckbar, NICHT wiedereinsetzbar
- Bei BR-Widerspruch: AN ODER BR kann anfechten
- Bei BR-Schweigen oder -Zustimmung: Nur AN selbst kann anfechten, ABER Anfechtungsgruende sind dann auf Motivkuendigung beschraenkt (§105 Abs 4 letzter Satz ArbVG)

**Anfechtungsgruende:**

1. **Motivkuendigung (§105 Abs 3 Z 1 ArbVG):**
   - Beitritt/Taetigkeit in der Gewerkschaft (lit a)
   - Taetigkeit als BR / Kandidatur (lit b)
   - Einberufung der Betriebsversammlung (lit c)
   - Geltendmachung nicht offenbar unberechtigter Ansprueche (lit i) — haeufigster Grund!
   - Beweislast: AN muss Motiv nur **glaubhaft machen** → AG muss beweisen, dass ein anderer Grund vorlag

2. **Sozialwidrigkeit (§105 Abs 3 Z 2 ArbVG):**
   - Kuendigung beeintraechtigt wesentliche Interessen des AN
   - Pruefung in 3 Stufen:
     - Stufe 1: Beeintraechtigung wesentlicher Interessen? (Alter, Arbeitsmarktchancen, Unterhaltspflichten, Dauer des DV, Gesundheit)
     - Stufe 2: AG kann betriebliche Erfordernisse nachweisen? (Rationalisierung, Auftragsrueckgang, Umstrukturierung)
     - Stufe 3: Sozialvergleich — gibt es einen weniger schutzwuerdigen AN fuer den selben Abbau?
   - NUR bei BR-Widerspruch als Anfechtungsgrund zulaessig!
   - OGH 9 ObA 2/03p: "Wesentliche Interessen" — niedrige Schwelle, insb. bei aelteren AN und langer Betriebszugehoerigkeit

**Verfahren:**
- Klage beim Arbeits- und Sozialgericht (ASG) am Sitz des Betriebs (§4 Abs 1 lit a ASGG)
- Kein Anwaltszwang (§40 ASGG)
- Klagebegehren: Rechtsunwirksam-Erklaerung der Kuendigung
- Aufschiebende Wirkung? Grundsaetzlich nein — AN muss waehrend des Verfahrens nicht weiterarbeiten, DV endet zum Kuendigungstermin. ABER: Bei obsiegendem Urteil lebt das DV ex tunc wieder auf → AN bekommt Entgelt fuer die gesamte Verfahrensdauer nachgezahlt!
- Vergleich im Verfahren: Haeufig — AG zahlt Abfindung, AN zieht Klage zurueck

### B: Entlassungsanfechtung / Klage auf Kuendigungsentschaedigung

**Bei unberechtigter Entlassung:**
- AN hat Anspruch auf **Kuendigungsentschaedigung** (§29 AngG): Entgelt bis zum fiktiven Ende bei ordnungsgemaesser AG-Kuendigung (laengste Frist zum naechsten Termin)
- Plus: Urlaubsersatzleistung, aliquote Sonderzahlungen, Abfertigung Alt (wenn anwendbar)
- Klage: Beim ASG am Sitz des Betriebs oder am Wohnort des AN (§4 ASGG)
- Frist: Keine besondere Anfechtungsfrist (anders als §105 ArbVG!), aber 3 Jahre Verjaehrung (§1486 Z 5 ABGB)

**Bei berechtigter Entlassung:**
- AN verliert: Kuendigungsentschaedigung
- AN behaelt: Aliquote Urlaubsersatzleistung (§10 Abs 2 UrlG), Abfertigung Neu (bleibt in BV-Kasse)
- AN verliert: Abfertigung Alt (§23 Abs 7 AngG — bei verschuldeter Entlassung kein Anspruch)

**Strittige Entlassung anfechten:**
- Klage auf Kuendigungsentschaedigung und Feststellung, dass die Entlassung unberechtigt war
- Beweislast fuer Entlassungsgrund: Beim AG (AG muss den Entlassungsgrund beweisen)

### C: ASG-Verfahren — Besondere Verfahrensregeln (ASGG)

**Zustaendigkeit:**
- Sachlich: Arbeits- und Sozialgericht (= Landesgericht als ASG, §2 ASGG)
- Oertlich: Wahlrecht des Klaegers (§4 ASGG):
  - Sitz/Niederlassung des AG (lit a)
  - Ort der Beschaeftigung (lit b)
  - Wohnsitz des AN (wenn AN Klaeger, lit c)

**Besonderheiten des ASGG:**
| Merkmal | Regelung | Rechtsgrundlage |
|---------|----------|-----------------|
| Anwaltspflicht | KEINE (§40 ASGG) — AN kann sich selbst vertreten | §40 ASGG |
| Gerichtsgebuehren | Halbe Gebuehren fuer AN (§§16, 19 GGG iVm TP1 Anm 4) | §80 Abs 2 ASGG |
| Kostenrisiko | Eingeschraenkt: §58 ASGG — Richter kann Kosten maessigen | §58 ASGG |
| Laienrichter | Senate mit je einem fachkundigen Laienrichter der AG- und AN-Seite (§10 ASGG) | §10 ASGG |
| Mitwirkungspflicht | Gericht muss Rechtsbelehrung erteilen (§39 Abs 1 ASGG) | §39 ASGG |
| Neuerungsverbot | Gelockert — auch in der Berufung neue Tatsachen und Beweise (§63 ASGG) | §63 ASGG |
| Gerichtsferien | Hemmen Fristen NICHT in Arbeitsrechtssachen (§§23, 92 ASGG) | §§23, 92 ASGG |

**Kostenrecht im ASG-Verfahren:**
- Halbe Pauschalgebuehr fuer AN (Ermaeigung nach §80 Abs 2 ASGG)
- Streitwert bestimmt die Gebuehr (TP1 GGG)
- Kostenersatzanspruch des Obsiegers, ABER:
  - §58 Abs 1 ASGG: Gericht kann dem AN Kostenersatzpflicht ganz oder teilweise erlassen, wenn Billigkeit es erfordert
  - Praxis: AN traegt selten volle Kosten, auch bei Unterliegen

**Vergleiche:**
- §433a ZPO / §23 ASGG: Praetoischer Vergleich moeglich
- Haeufig in der Praxis — ca. 50-60% der arbeitsrechtlichen Verfahren enden mit Vergleich
- Typische Vergleichsformel: "[x] Bruttomonatsentgelte Abfindung gegen Klagszuruecknahme"

### D: Kuendigungsentschaedigung (§29 AngG)

**Anspruch bei:**
- Unberechtigter Entlassung
- Berechtigtem vorzeitigen Austritt
- Fristwidriger AG-Kuendigung (zu kurze Frist oder falscher Termin)

**Berechnung:**
- Entgelt, das dem AN bis zum fiktiven Ende des DV bei ordnungsgemaesser Kuendigung zugestanden waere
- Fiktives Ende = laengstmoegliche Kuendigungsfrist + naechster Kuendigungstermin
- Umfasst: Grundgehalt + anteilige Sonderzahlungen + regelmaessige Zulagen/Ueberstundenpauschale + Sachbezuege
- Anrechnung: Was der AN in dieser Zeit anderweitig verdient hat oder zu verdienen absichtlich unterlassen hat (Anrechnungspflicht, §29 Abs 2 AngG)

**Beispielberechnung:**
- Entlassung am 15.3., DV seit 8 Jahren
- Kuendigungsfrist: 3 Monate zum Quartalsende (§20 Abs 2 AngG)
- Fiktives Ende bei ordnungsgemaesser Kuendigung am 15.3.: Kuendigungsfrist 3 Monate → muss zum 30.6. enden → ABER naechster Quartalstermin ab 15.3. + 3 Monate = 30.9.
- Kuendigungsentschaedigung: Entgelt 15.3. bis 30.9. = 6,5 Monatsentgelte (+ aliquote SZ)

### E: Ansprueche geltend machen (Ueberstunden, UEL, KV-Differenz)

**Vorgerichtliche Schritte:**
1. Ansprueche schriftlich gegenueber dem AG geltend machen (Einschreiben mit Rueckschein)
2. Frist setzen (14 Tage)
3. AK einschalten — die AK schreibt ein Interventionsschreiben an den AG
4. Oft: AG zahlt nach AK-Intervention

**Klage beim ASG:**
- Leistungsklage auf Zahlung (§226 ZPO)
- Streitwert: Summe aller offenen Ansprueche
- Beweismittel:
  - Ueberstunden: Zeitaufzeichnungen (§26 AZG — AG ist zur Aufzeichnung verpflichtet! Kommt AG dieser Pflicht nicht nach → Beweislastumkehr zugunsten des AN)
  - KV-Differenz: Taetigkeitsbeschreibung, Stelleninserat, Zeugen fuer tatsaechliche Taetigkeit
  - UEL: Lohnzettel, Urlaubskartei

**Verjaehrung:**
| Anspruch | Verjaehrungsfrist | Rechtsgrundlage |
|----------|-------------------|-----------------|
| Ueberstunden | 3 Jahre | §1486 Z 5 ABGB |
| KV-Differenz | 3 Jahre | §1486 Z 5 ABGB |
| Urlaubsersatzleistung | 3 Jahre | §1486 Z 5 ABGB |
| Sonderzahlungen | 3 Jahre | §1486 Z 5 ABGB |
| Abfertigung Alt | strittig: 3 Jahre (hM) / 30 Jahre | §1486 Z 5 oder §1478 ABGB |
| Kuendigungsentschaedigung | 3 Jahre | §1486 Z 5 ABGB |
| Dienstzeugnis | 30 Jahre (keine laufende Forderung) | §1478 ABGB |
| Schadenersatz (Diskriminierung GlBG) | Klage: 1 Jahr bei Beendigung (§15 Abs 1 GlBG), 3 Jahre bei Belaestigung | §15 GlBG |

### F: Einvernehmliche Aufloesung — Verhandlung

**Formvorschriften:**
- Schriftlichkeit empfohlen, aber nicht Formvoraussetzung (Ausnahme: Lehrlinge §15a BAG — Schriftlichkeit + Belehrung ueber Ruecktrittsrecht)
- Besonders geschuetzte AN (Schwangere, Behinderte): Schriftliche Belehrung ueber den Kuendigungsschutz erforderlich + Beratung durch AK/Gericht (§10 Abs 7 MSchG, §8 Abs 4 BEinstG)
- Elternkarenz: Gerichtliche oder AK-Belehrung ueber Rechte (§10 Abs 7 MSchG)

**Was steht dem AN bei einvernehmlicher Aufloesung zu (gesetzlich):**
- Urlaubsersatzleistung fuer offenen Urlaub (§10 UrlG)
- Aliquote Sonderzahlungen (sofern KollV/Vertrag)
- Abfertigung Alt (§23 AngG — einvernehmliche Aufloesung loest Anspruch aus!)
- Abfertigung Neu (§14 BMSVG — Auszahlungsanspruch entsteht)
- Arbeitslosengeld: Sofort, KEINE Sperre (anders als bei AN-Kuendigung: 4 Wochen Sperre, §11 AlVG)

**Verhandlungstipps (sachlich, keine Rechtsberatung):**
- Typische Abfindung: 1-3 Bruttomonatsentgelte als "Goldener Handschlag" (freiwillig, nicht gesetzlich)
- Verhandlungsposition staerker bei: Kuendigungsschutz (Schwangerschaft, Behinderung), langer Betriebszugehoerigkeit, offenen Anspruechen (Ueberstunden), drohender Anfechtung
- Freistellung waehrend der Restlaufzeit: Urlaub verbrauchen vs. Freistellung (Freistellung = Urlaub gilt als verbraucht nur bei ausdruecklicher Vereinbarung)
- **Nicht unter Druck unterschreiben!** AN hat Recht, sich Bedenkzeit zu nehmen und AK/Anwalt zu konsultieren
- Ruecktrittsrecht: Nur bei bestimmten geschuetzten Gruppen (§10 Abs 7 MSchG: innerhalb eines Werktages)

### G: Diskriminierungsklage (GlBG)

**Weg 1: Gleichbehandlungsanwaltschaft (GAW)**
- Kostenlose Beratung und Unterstuetzung
- Kann beim AG intervenieren
- Kann Antrag an die Gleichbehandlungskommission stellen
- Keine Bescheidkompetenz — nur Empfehlungen

**Weg 2: Gleichbehandlungskommission (GBK)**
- Senate fuer die einzelnen Diskriminierungsgruende (§11 GBK/GAW-Gesetz)
- Verfahren: Antrag → Pruefung → Einzelfallpruefung → Ergebnis (Gutachten)
- Nicht bindend, aber aussagekraeftig fuer nachfolgendes Gerichtsverfahren
- Kein Anwaltszwang, kostenlos

**Weg 3: Klage beim ASG (§12 GlBG)**
- Schadenersatz: Materielle und immaterielle Schaeden
- Bei Diskriminierung bei der Begruendung des DV: Mindestens 2 Monatsgehaelter (§12 Abs 1 GlBG)
- Bei Diskriminierung bei Beendigung: Wahlrecht — Anfechtung (DV lebt auf) oder Schadenersatz
- Bei sexueller Belaestigung: Mindestens EUR 1.000 (§12 Abs 11 GlBG)
- **Beweislastumkehr (§12 Abs 12 GlBG):** AN muss Diskriminierung nur glaubhaft machen → AG muss beweisen, dass ein anderer Grund vorlag

**Fristen:**
| Anspruch | Frist | Ab wann | Rechtsgrundlage |
|----------|-------|---------|-----------------|
| Einstellungsdiskriminierung | 6 Monate | Ab Ablehnung | §15 Abs 1 GlBG |
| Diskriminierung bei Beendigung | 14 Tage (Anfechtung) / 6 Monate (Schadenersatz) | Ab Zugang | §15 Abs 1 GlBG |
| Sexuelle Belaestigung | 3 Jahre | Ab Vorfall | §15 Abs 2 GlBG |
| Belaestigung (andere Gruende) | 1 Jahr | Ab Vorfall | §15 Abs 1 GlBG |

---

## Step 4: Check Deadlines

### FRISTEN SIND IM ARBEITSRECHT BESONDERS KURZ — Versaeumnis ist NICHT heilbar!

| Rechtsmittel / Handlung | Frist | Ab wann? | Rechtsgrundlage |
|--------------------------|-------|----------|-----------------|
| Kuendigungsanfechtung (§105 ArbVG) | **2 Wochen** | Ab Zugang der Kuendigung | §105 Abs 4 ArbVG |
| Anfechtung diskriminierende Kuendigung | **14 Tage** | Ab Zugang | §15 Abs 1 GlBG |
| Ruecktritt einvernehmliche Aufloesung (Schwangere) | **1 Werktag** | Ab Abschluss | §10 Abs 7 MSchG |
| Entlassung aussprechen (AG) | **Unverzoegerlich** (wenige Tage) | Ab Kenntnis des Grundes | OGH-Judikatur |
| Geltendmachung Konkurrenzklausel-Verletzung (AG) | **6 Monate** (Vertragsstrafe) | Ab Kenntnis | §37 Abs 1 AngG |
| Klagseinbringung Ueberstunden etc. | **3 Jahre** | Ab Faelligkeit | §1486 Z 5 ABGB |
| Gerichtsferien | Hemmen NICHT (ASG!) | — | §§23, 92 ASGG |

**Pruefschritte:**
1. Relevantes Ereignis-Datum feststellen (Kuendigung, Entlassung, Diskriminierung)
2. Frist berechnen (Kalendertage, nicht Werktage — ausser bei 2-Wochen-Frist §105 ArbVG: auch Kalendertage!)
3. Fristende: Faellt auf Sa/So/Feiertag → naechster Werktag (§125 Abs 2 ZPO)
4. ACHTUNG: Gerichtsferien hemmen im ASG-Verfahren NICHT (§23 Abs 1 ASGG)

**Klar angeben:**
- Ereignisdatum: [Datum]
- Fristende: [Datum]
- Verbleibende Tage: [n]
- Status: Ausreichend Zeit / Eilig (< 5 Tage) / Frist abgelaufen

Wenn die Frist abgelaufen ist:
> "Die Frist fuer die Kuendigungsanfechtung ist leider abgelaufen. Diese Frist ist eine materiell-rechtliche Ausschlussfrist und NICHT erstreckbar. Eine Wiedereinsetzung ist bei §105 ArbVG nach herrschender Meinung nicht moeglich. Pruefen Sie aber, ob andere Ansprueche bestehen (Kuendigungsentschaedigung bei Fristwidrigkeit, offene Entgeltansprueche)."

---

## Step 5: Draft the Klage / Schriftsatz

### A: Kuendigungsanfechtungsklage (§105 ArbVG)

```
An das Arbeits- und Sozialgericht [Ort]

Klaeger/in:    [Vollstaendiger Name]
               [Strasse, PLZ Ort]
               geboren am [Datum]
               SVNR: [Sozialversicherungsnummer]

Beklagte:      [Firmenname]
               [Firmenadresse]
               [FN-Nummer, wenn bekannt]

wegen:         Anfechtung einer Kuendigung (§105 ArbVG)

Streitwert:    EUR [Jahresbruttoentgelt — §10 ASGG:
               fuer die Berechnung der Gerichtsgebuehr]

                    K L A G E
               auf Anfechtung der Kuendigung
                  gemaess §105 ArbVG

I. SACHVERHALT

1.  Der Klaeger / Die Klaegerin ist seit [Eintrittsdatum] bei der
    beklagten Partei als [Taetigkeit] beschaeftigt. Das monatliche
    Bruttoentgelt betraegt EUR [Betrag] (14x jaehrlich).

    Beweis: Dienstvertrag vom [Datum] (Beilage ./A)
            Lohnzettel [Zeitraum] (Beilage ./B)

2.  Im Betrieb der beklagten Partei ist ein Betriebsrat eingerichtet.

    Beweis: PV des Klaegers / der Klaegerin

3.  Mit Schreiben vom [Datum], zugestellt am [Datum], hat die beklagte
    Partei das Dienstverhaeltnis zum [Kuendigungstermin] gekuendigt.

    Beweis: Kuendigungsschreiben vom [Datum] (Beilage ./C)

4.  Der Betriebsrat wurde gemaess §105 Abs 1 ArbVG verstaendigt und
    hat der Kuendigung innerhalb der Fuenftagefrist [widersprochen /
    zugestimmt / keine Stellungnahme abgegeben].

    Beweis: [Stellungnahme des BR (Beilage ./D) /
            PV des Klaegers / der Klaegerin]

5.  Die gegenstaendliche Klage wird innerhalb der zweiwoeichigen
    Anfechtungsfrist des §105 Abs 4 ArbVG eingebracht.

II. ANFECHTUNGSGRUENDE

[VARIANTE 1: Motivkuendigung — §105 Abs 3 Z 1 lit i ArbVG]

6.  Die Kuendigung erfolgte aus dem verpoentem Motiv der
    Geltendmachung nicht offenbar unberechtigter Ansprueche
    durch den Klaeger / die Klaegerin (§105 Abs 3 Z 1 lit i ArbVG).

7.  [Konkrete Darstellung: z.B. "Der Klaeger hat am [Datum]
    gegenueber [Vorgesetztem] die Auszahlung offener Ueberstunden
    in der Hoehe von EUR [Betrag] gefordert. Die Kuendigung wurde
    [x] Tage spaeter ausgesprochen. Der zeitliche Zusammenhang
    begruendet die Vermutung einer Motivkuendigung."]

    Beweis: [E-Mail vom [Datum] (Beilage ./E)
            PV des Klaegers / der Klaegerin
            Zeuge/Zeugin [Name, Adresse]]

[VARIANTE 2: Sozialwidrigkeit — §105 Abs 3 Z 2 ArbVG]

8.  Die Kuendigung beeintraechtigt wesentliche Interessen des
    Klaegers / der Klaegerin im Sinne des §105 Abs 3 Z 2 ArbVG:

    a) [Alter: Der Klaeger ist [x] Jahre alt und hat aufgrund
       seines Alters erheblich eingeschraenkte Chancen am
       Arbeitsmarkt.]

    b) [Betriebszugehoerigkeit: Das Dienstverhaeltnis besteht
       seit [x] Jahren. Der Klaeger hat seinen gesamten
       beruflichen Werdegang bei der beklagten Partei verbracht.]

    c) [Unterhaltspflichten: Der Klaeger ist fuer [x] Kinder
       sorgepflichtig.]

    d) [Gesundheit: Der Klaeger leidet an [Gesundheitseinschraenkung],
       die seine Vermittelbarkeit am Arbeitsmarkt weiter einschraenkt.]

    Beweis: [Beweisanbote]

9.  Betriebliche Erfordernisse, die die Kuendigung rechtfertigen
    wuerden, liegen nicht vor. [Alternativ: Die beklagte Partei
    haette den Klaeger auf einem anderen gleichwertigen Arbeitsplatz
    weiterbeschaeftigen koennen (Sozialvergleich).]

    Beweis: [z.B. Stelleninserate der beklagten Partei (Beilage ./F)
            PV des Klaegers / der Klaegerin]

III. KLAGEBEGEHREN

Der Klaeger / Die Klaegerin stellt daher den

                         A N T R A G,

das Gericht moege die von der beklagten Partei mit Schreiben vom
[Datum] zum [Kuendigungstermin] ausgesprochene Kuendigung fuer
rechtsunwirksam erklaeren.

[Ort], am [Datum]

                         ____________________
                         [Unterschrift]


BEILAGENVERZEICHNIS:
./A  Dienstvertrag vom [Datum]
./B  Lohnzettel [Zeitraum]
./C  Kuendigungsschreiben vom [Datum]
./D  Stellungnahme des Betriebsrats [falls vorhanden]
./E  [Beweismittel zum Motiv]
./F  [Weitere Beweismittel]
```

### B: Klage auf Kuendigungsentschaedigung (§29 AngG)

```
An das Arbeits- und Sozialgericht [Ort]

Klaeger/in:    [Vollstaendiger Name]
               [Strasse, PLZ Ort]

Beklagte:      [Firmenname]
               [Firmenadresse]

wegen:         EUR [Betrag] s.A. (Kuendigungsentschaedigung)

                    K L A G E

I. SACHVERHALT

1.  Der Klaeger / Die Klaegerin war seit [Eintrittsdatum] bei der
    beklagten Partei als [Taetigkeit] beschaeftigt. Das monatliche
    Bruttoentgelt betrug EUR [Betrag] (14x jaehrlich).

2.  Am [Datum] hat die beklagte Partei das Dienstverhaeltnis durch
    Entlassung beendet. [Alternativ: Am [Datum] hat die beklagte
    Partei das Dienstverhaeltnis unter Nichteinhaltung der
    Kuendigungsfrist / des Kuendigungstermins gekuendigt.]

3.  Die Entlassung war unberechtigt, da [Begruendung: kein
    Entlassungsgrund nach §27 AngG vorlag / die Entlassung
    verspaetet ausgesprochen wurde].

II. ANSPRUCH

4.  Bei ordnungsgemaesser Kuendigung durch die beklagte Partei
    haette das Dienstverhaeltnis unter Einhaltung der
    Kuendigungsfrist von [x] Monaten zum [naechster Quartalstermin]
    geendet (§20 Abs 2 AngG).

5.  Dem Klaeger / Der Klaegerin gebührt daher gemaess §29 AngG
    eine Kuendigungsentschaedigung in Hoehe des Entgelts vom
    [Entlassungsdatum] bis [fiktives Kuendigungsende]:

    Grundgehalt:                   EUR [Betrag]
    Aliquote Sonderzahlungen:      EUR [Betrag]
    Regelmaessige Ueberstunden:    EUR [Betrag]
    Sachbezuege:                   EUR [Betrag]
    GESAMT:                        EUR [Betrag]

III. KLAGEBEGEHREN

Die beklagte Partei ist schuldig, dem Klaeger / der Klaegerin
EUR [Betrag] brutto samt 4% Zinsen seit [Datum] binnen 14 Tagen
zu bezahlen.

[Ort], am [Datum]

                         ____________________
                         [Unterschrift]
```

### C: Interventionsschreiben (vorgerichtlich, z.B. ueber AK)

```
[Name des AN]
[Adresse]

An
[Firmenname]
[Firmenadresse]

[Ort], am [Datum]

Betreff: Geltendmachung offener Ansprueche aus dem Dienstverhaeltnis

Sehr geehrte Damen und Herren,

ich war von [Eintrittsdatum] bis [Austrittsdatum] in Ihrem
Unternehmen als [Taetigkeit] beschaeftigt. Ich mache hiermit
folgende offene Ansprueche geltend:

1. Ueberstunden [Zeitraum]: EUR [Betrag] brutto
   (basierend auf [x] Ueberstunden a EUR [Stundensatz] + 50% Zuschlag)

2. Urlaubsersatzleistung: EUR [Betrag] brutto
   ([x] offene Urlaubstage)

3. KV-Differenz [Zeitraum]: EUR [Betrag] brutto
   (korrekte Einstufung: Verwendungsgruppe [x], Stufe [y])

GESAMT: EUR [Betrag] brutto

Ich ersuche um Zahlung des genannten Betrags auf mein Konto
[IBAN] binnen 14 Tagen ab Zugang dieses Schreibens.

Sollte die Zahlung nicht fristgerecht erfolgen, sehe ich mich
gezwungen, meine Ansprueche gerichtlich geltend zu machen.

Mit freundlichen Gruessen

____________________
[Unterschrift]
```

---

## Step 6: Present with Timeline, Costs, and Next Steps

```markdown
# Arbeitsrechtliches Verfahren

**Sachverhalt:** [2-3 Saetze Zusammenfassung]
**Beendigung durch:** [AG-Kuendigung / Entlassung / Einvernehmlich / AN-Kuendigung]
**Beendigungsdatum:** [Datum]
**Verfahrenstyp:** [Kuendigungsanfechtung / Kuendigungsentschaedigung / Leistungsklage / Diskriminierungsklage]

## Fristenlage

| Frist | Fristende | Verbleibend | Status |
|-------|-----------|-------------|--------|
| [z.B. Kuendigungsanfechtung §105 ArbVG] | [Datum] | [n] Tage | Ausreichend / Eilig / Abgelaufen |
| [z.B. Verjaehrung Ueberstunden] | [Datum] | [n] Monate | Ausreichend / Beachten |

## Zustaendiges Gericht und Verfahren

**Gericht:** ASG [Ort]
**Verfahrensart:** [Arbeitsrechtssache gemaess §50 ASGG]
**Anwaltspflicht:** Nein (§40 ASGG)
**Kostenlose Vertretung:** AK / Gewerkschaft

## Ansprueche im Ueberblick

| Anspruch | Rechtsgrundlage | Hoehe (geschaetzt) | Verjaehrung |
|----------|----------------|---------------------|-------------|
| [Kuendigungsentschaedigung] | §29 AngG | EUR [x] brutto | [Datum] |
| [Ueberstunden] | §10 AZG | EUR [x] brutto | [Datum] |
| [Urlaubsersatzleistung] | §10 UrlG | EUR [x] brutto | [Datum] |
| GESAMT | | EUR [x] brutto | |

## Kostenrisiko

| Posten | Betrag (geschaetzt) |
|--------|---------------------|
| Pauschalgebuehr (halbe Gebuehr, §80 ASGG) | EUR [x] |
| Anwaltskosten (falls kein AK-Rechtsschutz) | EUR [x] — [y] |
| Kostenersatz bei Unterliegen | EUR [x] (maessigbar nach §58 ASGG) |
| Kostenersatz bei Obsiegen | EUR [x] (vom AG zu zahlen) |

## Erfolgsaussichten

| Anspruch | Erfolgsaussicht | Begruendung |
|----------|----------------|-------------|
| [Anspruch 1] | Gut / Mittel / Gering | [Kurze Begruendung] |
| [Anspruch 2] | Gut / Mittel / Gering | [Kurze Begruendung] |

## Vergleichskorridor

Realistischer Vergleich: EUR [x] bis EUR [y] brutto
Begruendung: [z.B. "Bei mittlerer Erfolgsaussicht und [x] Monaten Verfahrensdauer ist ein Vergleich in Hoehe von [y] Monatsentgeltern realistisch"]

## Entwurf

[Hier den Entwurf aus Step 5 einfuegen — Klage, Interventionsschreiben, etc.]

## Instanzenzug

1. **ASG (1. Instanz):** Verfahrensdauer ca. 3-12 Monate
2. **OLG (Berufung):** Frist 4 Wochen ab Zustellung des Urteils (§§461ff ZPO). In Arbeitsrechtssachen: §63 ASGG — Neuerungserlaubnis (neue Tatsachen und Beweise)!
3. **OGH (Revision):** Nur bei erheblicher Rechtsfrage (§502 Abs 1 ZPO). In Arbeitsrechtssachen: §46 Abs 1 ASGG — Revision bei Streitwert ueber EUR 5.000 UND erheblicher Rechtsfrage

## Naechste Schritte

1. [Erster konkreter Schritt — z.B. "Sofort AK kontaktieren (Rechtsberatung + Vertretung kostenlos fuer AK-Mitglieder)"]
2. [Zweiter Schritt — z.B. "Klage bis [Fristende] beim ASG [Ort] einbringen"]
3. [Dritter Schritt — z.B. "Alle Unterlagen sichern: Dienstvertrag, Lohnzettel, Zeitaufzeichnungen, E-Mails"]
4. [z.B. "Keine Vereinbarungen mit dem AG ohne vorherige Ruecksprache mit AK/Anwalt unterschreiben"]

## Quellenstatus
| Kategorie | Status | Details |
|-----------|--------|---------|
| RIS MCP | Verfuegbar / Nicht verfuegbar | |
| Gesetze | RIS_VERIFIED / UNVERIFIED | [n] Normen geprueft |
| Judikatur | RIS_VERIFIED / UNVERIFIED | [n] Entscheidungen |
| Pruefdatum | [YYYY-MM-DD] | |

---
Keine Rechtsberatung. Diese Analyse ersetzt nicht die Beratung durch einen Rechtsanwalt oder eine Rechtsanwaeltin. Arbeitnehmer/innen haben Anspruch auf kostenlose Beratung und Vertretung durch die Arbeiterkammer (AK) und ihre Gewerkschaft — insbesondere bei Kuendigungsanfechtungen ist dies dringend zu empfehlen, da die 2-Wochen-Frist keine Fehler verzeiht. Kontaktieren Sie umgehend die AK!
```

---

## Critical Rules

1. **2-Wochen-Frist bei Kuendigungsanfechtung ist HEILIG** — §105 Abs 4 ArbVG: Materiell-rechtliche Ausschlussfrist, nicht erstreckbar, keine Wiedereinsetzung. IMMER als erstes pruefen und prominent warnen. Verpasste Frist = endgueltiger Verlust des Anfechtungsrechts.
2. **Leistungssache vs. Verwaltungssache** — Arbeitsrechtliche Streitigkeiten aus dem DV gehen ans ASG (§50 ASGG), nicht ans BVwG. Verwechslungsgefahr nur bei AMS-Sperren (→ BVwG) oder SV-Pflichtversicherung (→ BVwG).
3. **Gerichtsferien hemmen NICHT am ASG** — §§23, 92 ASGG. Klagefristen laufen auch im Sommer und ueber Weihnachten weiter!
4. **Kein Anwaltszwang am ASG** — §40 ASGG. ABER: AK und Gewerkschaft bieten kostenlose Vertretung — immer darauf hinweisen!
5. **Betriebsrat ist Voraussetzung fuer §105 ArbVG** — Ohne BR keine Kuendigungsanfechtung nach §105 ArbVG. In Betrieben ohne BR: nur Anfechtung wegen Motivkuendigung nach §105 Abs 3 Z 1 ArbVG analogiegestuetzt auf GlBG moeglich, oder allgemeiner Kuendigungsschutz (Schwangerschaft, Behinderung etc.).
6. **Entlassung: Beweislast beim AG** — Der AG muss den Entlassungsgrund beweisen. AN muss nur die Entlassung als solche beweisen.
7. **Kuendigungsentschaedigung: Anrechnung** — §29 Abs 2 AngG: Was der AN anderweitig verdient oder zu verdienen schuldhaft unterlassen hat, wird angerechnet. AN muss sich aktiv um einen neuen Arbeitsplatz bemuehen.
8. **Vergleichspraxis realistisch darstellen** — Ca. 50-60% aller ASG-Verfahren enden mit Vergleich. Vergleichskorridor immer angeben, da die meisten Mandanten wissen wollen, was "realistisch" ist.
9. **AK-Rechtsschutz** — Die AK bietet kostenlose Rechtsberatung und Vertretung vor dem ASG. Gewerkschaftsmitglieder haben zusaetzlich Anspruch auf Rechtsschutz der Gewerkschaft. IMMER darauf hinweisen.
10. **Cite specific §§** — Keine pauschalen Verweise. Immer die exakte Gesetzesstelle angeben (z.B. §105 Abs 3 Z 1 lit i ArbVG, §29 Abs 1 AngG, §12 Abs 12 GlBG).
11. **Match user's language** — German in = German out. English in = English out. Gesetze immer in deutscher Originalform zitieren.
12. **Beweislastumkehr bei Arbeitszeitaufzeichnungen** — §26 AZG verpflichtet den AG zur Fuehrung von Arbeitszeitaufzeichnungen. Kommt der AG dem nicht nach, kehrt sich die Beweislast um — der AN muss Ueberstunden nur glaubhaft machen. Immer pruefen!
13. **Einvernehmliche Aufloesung: Nicht unter Druck unterschreiben** — AN hat kein gesetzliches Ruecktrittsrecht (ausser geschuetzte Gruppen). Warnung: "Unterschreiben Sie nichts ohne AK-Beratung."
14. **Diskriminierung: Sehr kurze Fristen** — Bei diskriminierender Kuendigung betraegt die Anfechtungsfrist nur 14 Tage (§15 Abs 1 GlBG). Immer zusammen mit §105 ArbVG pruefen.
