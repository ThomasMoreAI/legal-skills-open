---
name: recht-miet-verfahren-momarcode1
title: /recht miet-verfahren — Mietrechtliches Verfahren
description: Austrian tenancy law procedures — Schlichtungsstelle proceedings, Mietzinsueberpruefung, Erhaltungsauftrag, gerichtliche Aufkuendigung (§33 MRG), Raeumungsklage, Mietzinsminderung, Abloesrueckforderung (§27 Abs 3 MRG), Mietvertragskuendigung durch Mieter. Includes draft templates for Schlichtungsstellenantrag and Klage.
author: MoMarcode1
author_url: https://github.com/MoMarcode1/austrian-legal-claude/tree/main/skills/recht-miet-verfahren
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: at
practice: litigation
language: de
---

# /recht miet-verfahren — Mietrechtliches Verfahren

When the user wants to enforce tenant or landlord rights, challenge a termination, file for rent review, or take any procedural step in an Austrian tenancy dispute, follow these steps.

---

## Step 1: Gather the Facts

Read everything the user has provided. You need:

1. **What has already happened?** — Received a Kuendigung? Dispute about Mietzinshoehe? Mangel not repaired? Kaution not returned? Abloese paid?
2. **Has the user already taken action?** — Contacted Vermieter/Mieter? Written a letter? Filed anything?
3. **Location** — Which Bundesland and Gemeinde? (Determines if Schlichtungsstelle exists)
4. **Deadlines** — When was a Kuendigung received? When did the Mangel occur? When was the Abloese paid? Is there a court date?
5. **MRG applicability** — Was recht-miet already run? If not, clarify: Vollanwendung, Teilanwendung, or ABGB-only? (Essential for procedure choice)
6. **Financial situation** — Can the user afford a lawyer? Is Verfahrenshilfe needed?
7. **Evidence** — What documents exist? (Mietvertrag, Korrespondenz, Fotos, Betriebskostenabrechnung, Uebergabeprotokoll)

If critical information is missing, ask:
> "Gibt es in Ihrer Gemeinde eine Schlichtungsstelle? In Wien ist die Schlichtungsstelle (MA 50) vorgeschaltet — d.h. Sie muessen dort zuerst hin, bevor Sie zum Bezirksgericht gehen koennen."

---

## Step 2: RIS Verification

Before proceeding with analysis, follow the **RIS Verification Protocol** (`references/ris-protocol.md`):
1. Check RIS MCP availability
2. For every § you cite in this analysis, verify current wording via RIS
3. For case law references (OGH, LGZ Wien), retrieve via RIS Justiz
4. Record verification status for the Quellenstatus block
5. If RIS is unavailable, follow the fallback ladder and flag all affected citations

---

## Step 3: Determine the Correct Procedural Path

### Decision Tree: Where to go?

#### 3A: Schlichtungsstelle vs. Bezirksgericht

**Schlichtungsstelle** (Gemeindeschlichtungsstelle, in Wien: MA 50):

Existiert in: **Wien, Graz, Linz, Salzburg, Innsbruck, Klagenfurt, Leoben, Muerzuschlag, Neunkirchen, Stockerau** (und einige weitere Gemeinden — im Zweifel nachfragen oder pruefen)

**Zwingend vorgeschaltet (§39 Abs 1 MRG):** In Gemeinden, in denen eine Schlichtungsstelle eingerichtet ist, MUSS der Antrag ZUERST bei der Schlichtungsstelle eingebracht werden. Erst wenn:
- die Schlichtungsstelle nicht innerhalb von 3 Monaten entscheidet (§40 Abs 2 MRG), ODER
- eine Partei die Entscheidung der Schlichtungsstelle nicht akzeptiert (Anrufung des Gerichts innerhalb von 4 Wochen, §40 Abs 1 MRG)

kann das Bezirksgericht angerufen werden.

**Keine Schlichtungsstelle:** In Gemeinden ohne Schlichtungsstelle direkt zum Bezirksgericht (§37 MRG).

#### 3B: Zustaendiges Gericht

- **Bezirksgericht** am Ort der gelegenen Sache (§83b JN) — IMMER fuer Mietrechtssachen (egal welcher Streitwert!)
- **Keine Anwaltspflicht** in mietrechtlichen Ausserstreitverfahren nach §37 MRG
- **Anwaltspflicht** bei Raeumungsklagen und Kuendigungsverfahren: ab Streitwert EUR 5.000 (§27 ZPO) — bei Wohnungsmiete wird der Streitwert nach Jahresmietzins berechnet
- **Keine GGG-Gebuehr** fuer Verfahren nach §37 MRG (gebuehrenfrei!)

#### 3C: Wahl des Verfahrenstyps

| Anliegen | Verfahrensart | Rechtsgrundlage | Zustaendigkeit |
|----------|--------------|-----------------|----------------|
| Mietzinsueberpruefung | Ausserstreitverfahren §37 MRG | §37 Abs 1 Z 8 MRG | Schlichtungsstelle / BG |
| Betriebskostenueberpruefung | Ausserstreitverfahren §37 MRG | §37 Abs 1 Z 12 MRG | Schlichtungsstelle / BG |
| Erhaltungsauftrag | Ausserstreitverfahren §37 MRG | §37 Abs 1 Z 2 MRG iVm §6 MRG | Schlichtungsstelle / BG |
| Investitionsersatz | Ausserstreitverfahren §37 MRG | §37 Abs 1 Z 5 MRG | Schlichtungsstelle / BG |
| Abloesrueckforderung | Ausserstreitverfahren §37 MRG | §37 Abs 1 Z 14 MRG iVm §27 Abs 3 MRG | Schlichtungsstelle / BG |
| Kuendigung durch Vermieter | Streitiges Verfahren, gerichtliche Aufkuendigung | §33 MRG, §§560ff ZPO | BG (direkt, keine Schlichtungsstelle) |
| Raeumungsklage | Streitiges Verfahren, Klage | §1118 ABGB | BG |
| Kautionsrueckforderung | Streitiges Verfahren, Klage | §1431 ABGB | BG |
| Mietzinsminderung (Feststellung) | Je nach Konstellation: §37 MRG oder Klage | §1096 ABGB | BG |

---

## Step 4: Procedure-Specific Instructions

### 4A: Mietzinsueberpruefung bei der Schlichtungsstelle

**Wer kann den Antrag stellen?**
- Der Mieter (haeufigster Fall: Mieter vermutet, dass der Mietzins zu hoch ist)
- Aber auch der Vermieter (selten, zur Feststellung der Zulaessigkeit)

**Antragstellung:**
1. Schriftlicher Antrag an die zustaendige Schlichtungsstelle
2. Keine Anwaltspflicht, keine Gebuehrenpflicht
3. Beilagen: Mietvertrag (Kopie), ggf. Betriebskostenabrechnungen, Wohnungsfotos

**Inhalt des Antrags (§37 Abs 3 MRG):**
- Bezeichnung des Mietgegenstands (Adresse, Tuernummer, Groesse)
- Name und Adresse des Vermieters
- Darstellung des Sachverhalts (vereinbarter Mietzins, vermuteter zulaessiger Mietzins)
- Konkreter Antrag (z.B. "Feststellung, dass der gesetzlich zulaessige Hauptmietzins EUR [x] betraegt und der Vermieter die seit [Datum] zu viel bezahlten Betraege zurueckzuzahlen hat")

**Verfahrensablauf:**
1. Schlichtungsstelle stellt dem Vermieter den Antrag zu
2. Muendliche Verhandlung (Vergleichsversuch)
3. Allenfalls Sachverstaendigengutachten (fuer Richtwertmietzins-Berechnung mit Zu-/Abschlaegen)
4. Entscheidung der Schlichtungsstelle
5. Wenn eine Partei nicht einverstanden: Anrufung des Bezirksgerichts innerhalb von 4 Wochen (§40 Abs 1 MRG)

**Rueckforderung:**
- Zuviel bezahlter Mietzins kann fuer die Vergangenheit zurueckgefordert werden
- Verjaehrungsfrist: 3 Jahre ab Faelligkeit der jeweiligen Miete (§1486 Z 4 ABGB)
- ABER: Mietzinsueberpruefungsantrag hemmt die Verjaehrung ab Antragstellung

### 4B: Erhaltungsauftrag (§§3, 6 MRG)

**Voraussetzung:** Vollanwendung des MRG. Mangel, dessen Behebung in die Erhaltungspflicht des Vermieters faellt (§3 MRG).

**Vorgangsweise:**
1. **Mangelanzeige an den Vermieter** (schriftlich, nachweislich — Einschreiben oder E-Mail mit Lesebestaetigung)
   - Konkreten Mangel beschreiben
   - Frist zur Behebung setzen (2-4 Wochen je nach Dringlichkeit)
   - Hinweis auf §3 MRG und die Moeglichkeit, bei Untaetigkeit die Schlichtungsstelle einzuschalten
2. **Bei Untaetigkeit:** Antrag an die Schlichtungsstelle / BG auf Durchfuehrung der Erhaltungsarbeiten (§6 Abs 1 MRG)
3. **Inhalt des Antrags:**
   - Beschreibung des Mangels
   - Nachweis der Anzeige an den Vermieter
   - Antrag auf Auftrag an den Vermieter, die Erhaltungsarbeiten binnen angemessener Frist durchzufuehren
4. **Einstweilige Verfuegung:** Bei Gefahr im Verzug (z.B. Wasserrohrbruch, Schimmelbefall mit Gesundheitsgefaehrdung) kann eine einstweilige Verfuegung beantragt werden

**Thermenersatz (seit 1.1.2024):**
- Bei mitvermieteten Heizthermen, die aelter als 15 Jahre sind, kann der Mieter einen Antrag auf Ersatz durch ein klimafreundliches Heizsystem stellen
- Grundlage: §3 Abs 2 Z 2a MRG (MRG-Novelle 2023)
- Vermieter traegt die Kosten

### 4C: Kuendigungsschutzverfahren (§33 MRG)

**Aus Sicht des Vermieters (gerichtliche Aufkuendigung):**

1. **Vorbereitung:**
   - Kuendigungsgrund aus dem taxativen Katalog des §30 Abs 2 MRG identifizieren
   - Beweise sichern (bei nachteiligem Gebrauch: Protokolle, Fotos, Zeugenaussagen)
   - Bei Zahlungsverzug: Qualifizierte Mahnung mit Nachfristsetzung (§1118 ABGB) — nachweislich!

2. **Gerichtliche Aufkuendigung einbringen (§§560ff ZPO):**
   - Beim zustaendigen Bezirksgericht (Ort der gelegenen Sache)
   - Kuendigungstermin: Monatsletzter (bei Wohnung), bei Geschaeftsraum: Quartalsende
   - Kuendigungsfrist: 1 Monat bei Wohnungen (§560 Abs 1 Z 2 lit e ZPO)
   - Aufkuendigungsschrift muss enthalten: Kuendigungsgrund ausdruecklich angeben, Termin, Antrag auf Uebergabe, Raeumungsantrag fuer den Fall der Nichtuebergabe

3. **Zustellung an den Mieter:** Durch das Gericht

4. **Einwendungen des Mieters:**
   - Frist: 4 Wochen ab Zustellung (§562 ZPO)
   - Erhebt der Mieter KEINE Einwendungen: Kuendigung wird rechtswirksam, Gericht erteilt Vollstreckbarkeitsbestaetigung → Raeumungsexekution moeglich
   - Erhebt der Mieter Einwendungen: Verfahren ueber Berechtigung der Kuendigung → muendliche Verhandlung → Urteil

**Aus Sicht des Mieters (Einwendungen gegen Kuendigung):**

1. **Frist beachten:** 4 Wochen ab Zustellung der Kuendigung — NICHT versaeumen, sonst wird die Kuendigung rechtskraeftig!
2. **Einwendungen formulieren:**
   - Bestreiten des Kuendigungsgrundes (z.B. "Kein nachteiliger Gebrauch, die behaupteten Laermstoerungen sind nicht zutreffend")
   - Vorbringen von Gegenbeweisen
   - Bei Zahlungsverzug: Nachzahlung des Rueckstands vor Schluss der muendlichen Verhandlung (§33 Abs 2 MRG) — Kuendigungsgrund faellt weg, wenn vollstaendig nachbezahlt wird (einschliesslich Zinsen und Kosten)
3. **Verhandlung und Urteil:**
   - Beweisverfahren ueber den Kuendigungsgrund
   - Gericht prueft: Liegt der Kuendigungsgrund tatsaechlich vor?
   - Urteil: Kuendigung fuer rechtswirksam erklaert ODER Kuendigung aufgehoben

### 4D: Raeumungsklage

**Zulaessig wenn:**
- Mietvertrag wurde bereits rechtswirksam beendet (Zeitablauf bei Befristung, wirksame Kuendigung, einvernehmliche Aufhebung) UND der Mieter raeumt nicht
- Titellose Benuetzung (z.B. nach Tod des Mieters ohne Eintrittsberechtigte)
- Fristlose Auflosung nach §1118 ABGB (erheblich nachteiliger Gebrauch oder qualifizierter Zahlungsverzug)

**Vorgangsweise:**
1. Klage beim zustaendigen Bezirksgericht (§49 Abs 2 Z 5 JN)
2. Streitwert: Jahresmietzins (§58 JN) — bestimmt Anwaltspflicht und GGG
3. Gebuehr: nach GGG (Pauschalgebuehr nach Streitwert)
4. Beizufuegende Urkunden: Mietvertrag, Kuendigung (falls erfolgt), Nachweis der Beendigung
5. Raeumungsfrist: Gericht kann Raeumungsfrist von max. 6 Monaten gewaehren (§35 MRG bei Wohnungen im MRG-Bereich)

**ACHTUNG bei §1118 ABGB-Auflosung wegen Zahlungsverzug:**
- Mieter kann bis Schluss der muendlichen Verhandlung 1. Instanz den gesamten Rueckstand nachzahlen (§33 Abs 2 MRG) — dann faellt der Auflösungsgrund weg
- "Qualifizierter" Zahlungsverzug: Mieter hat trotz Mahnung den Rueckstand nicht innerhalb angemessener Frist beglichen
- Raeumungsklage statt Kuendigung bei §1118: Wenn Vermieter aus wichtigem Grund sofort aufloest (ohne Einhaltung der Kuendigungsfrist)

### 4E: Mietzinsminderung geltend machen

**Vorgangsweise fuer den Mieter:**

1. **Mangel dokumentieren** (Fotos, Videos, Datum notieren, Zeugen)
2. **Mangelanzeige an den Vermieter** — schriftlich, nachweislich, mit Beschreibung des Mangels und Aufforderung zur Behebung
3. **Minderung berechnen:**
   - Prozentsatz der Gebrauchsbeeintraechtigung schaetzen (Richtwerte aus OGH-Judikatur, siehe recht-miet Step 4K)
   - Zeitraum der Beeintraechtigung festlegen
   - Minderungsbetrag = Bruttomiete x Minderungsprozentsatz x Monate
4. **Minderung durchsetzen:**
   - **Selbsthilferecht:** Mieter kann den geminderten Mietzins einfach bezahlen (weniger ueberweisen) — ABER: Risiko! Wenn das Gericht die Minderung geringer bewertet, ist der Mieter im Zahlungsverzug
   - **Sicherer Weg:** Vollen Mietzins unter Vorbehalt bezahlen und Rueckforderung bei Schlichtungsstelle/BG beantragen
   - **Alternativ:** Feststellungsantrag bei Schlichtungsstelle/BG ueber den zulaessigen Mietzins waehrend der Mangelperiode
5. **Bei Gesundheitsgefaehrdung:** Recht zur fristlosen Auflosung nach §1117 ABGB (Unbrauchbarkeit)

### 4F: Abloeserueckforderung (§27 Abs 3 MRG)

**Verjaehrungsfrist:** 10 Jahre ab Bezahlung (§27 Abs 3 MRG) — wesentlich laenger als die allgemeine 3-Jahres-Verjaehrung!

**Vorgangsweise:**
1. **Pruefen, ob Abloese verboten war:**
   - An Vormieter oder Vermieter bezahlt?
   - Keine angemessene Gegenleistung (keine tatsaechlichen Investitionen, keine echte Mobeluebernahme)?
   - Im Vollanwendungsbereich des MRG?
2. **Beweissicherung:**
   - Zahlungsbeleg (Ueberweisung, Quittung)
   - Mietvertrag (Hinweise auf Abloese?)
   - Zeugen (Makler? Vormieter?)
   - ACHTUNG: Abloesen werden haeufig bar und ohne Beleg bezahlt — Beweisschwierigkeit!
3. **Antrag bei Schlichtungsstelle / BG:**
   - Ausserstreitverfahren nach §37 Abs 1 Z 14 MRG
   - Antrag auf Rueckzahlung der verbotenen Abloese
   - Rueckzahlungspflichtiger: Wer die Abloese empfangen hat (Vormieter, Vermieter, oder Makler)

4. **Besonderheit Maklerprovisionsrueckforderung (Bestellerprinzip seit 1.7.2023):**
   - Seit 1.7.2023 (§17a MaklerG) zahlt der Besteller (= Auftraggeber) die Provision
   - Wenn der Mieter NACH dem 1.7.2023 eine Maklerprovision gezahlt hat, obwohl der Vermieter den Makler beauftragt hat: Rueckforderung moeglich
   - Verjaehrung: 3 Jahre (§1486 ABGB — nicht die 10-Jahres-Frist des §27 MRG, da MaklerG eigene Grundlage)

### 4G: Mietvertragskuendigung durch den Mieter

#### Unbefristeter Mietvertrag:

- **Kuendigungsfrist:** 1 Monat zum Monatsletzten (§560 Abs 1 Z 2 lit e ZPO) — Standardfall bei Wohnung
- **Abweichende vertragliche Vereinbarung:** Laengere Kuendigungsfristen sind zulaessig (z.B. 3 Monate), aber bei Wohnungen im Vollanwendungsbereich maximal 1 Jahr
- **Form:** Schriftlich, zugang beim Vermieter (Einschreiben empfohlen). ACHTUNG: Der Mietvertrag kann strengere Formvorschriften vorsehen (z.B. "nur per eingeschriebenem Brief"). Im Vollanwendungsbereich des MRG sind uebertriebene Formvorschriften aber unwirksam.
- **Gerichtliche Aufkuendigung durch Mieter:** Bei Wohnungsmieten im MRG-Bereich NICHT erforderlich — einseitige Erklaerung genuegt (im Gegensatz zum Vermieter, der gerichtlich kuendigen muss)

#### Befristeter Mietvertrag:

- **Vollanwendung MRG (§29 Abs 2 MRG):** Mieter kann ab dem 2. Vertragsjahr jederzeit unter Einhaltung einer 3-monatigen Kuendigungsfrist zum Monatsletzten kuendigen
- **Teilanwendung MRG:** KEIN gesetzliches vorzeitiges Kuendigungsrecht. Vorzeitige Kuendigung nur moeglich wenn:
  - Im Mietvertrag ein Kuendigungsrecht fuer den Mieter vereinbart ist (haeufig der Fall, z.B. "Der Mieter kann nach Ablauf des ersten Vertragsjahres unter Einhaltung einer 3-monatigen Kuendigungsfrist kuendigen")
  - Ein wichtiger Grund nach §1117 ABGB vorliegt (Unbrauchbarkeit, Gesundheitsgefaehrdung)
- **Kein MRG:** Nur ausserordentliche Aufloesung nach §1117 ABGB oder einvernehmliche Aufhebung

#### Formvorschriften fuer die Kuendigung:

**Kuendigungsschreiben muss enthalten:**
- Name des Mieters und des Vermieters
- Bezeichnung des Mietgegenstands (Adresse, Tuernummer)
- Erklaerung, dass das Mietverhaeltnis aufgekuendigt wird
- Kuendigungstermin (z.B. "zum 31.8.2026")
- Datum und Unterschrift
- Zustellung: nachweislich (Einschreiben mit Rueckschein oder persoenliche Uebergabe mit Bestaetigung)

---

## Step 5: Draft Templates

### 5A: Muster — Antrag an die Schlichtungsstelle (Mietzinsueberpruefung)

```
An die
Schlichtungsstelle in Mietrechtssachen
[Adresse der zustaendigen Schlichtungsstelle]
[z.B. fuer Wien: MA 50, Gonzagagasse 11, 1010 Wien]

Antragsteller/in:
[Vor- und Nachname]
[Adresse des Mietgegenstands]

Antragsgegner/in (Vermieter/in):
[Vor- und Nachname / Firma]
[Adresse]

ANTRAG
auf Ueberpruefung des Hauptmietzinses gemaess §37 Abs 1 Z 8 MRG

I. Sachverhalt

1. Der/die Antragsteller/in ist Mieter/in der Wohnung
   [Adresse, Stiege, Tuernummer, Geschoss], bestehend aus
   [Anzahl] Zimmern, Kueche, Bad, WC, Vorraum, mit einer
   Nutzflaeche von ca. [x] m2.

2. Der Mietvertrag wurde am [Datum] abgeschlossen
   [befristet bis / unbefristet].

3. Der vereinbarte monatliche Hauptmietzins betraegt EUR [x]
   (exkl. Betriebskosten und USt), das entspricht EUR [x]/m2.

4. Das Haus, in dem sich der Mietgegenstand befindet, wurde
   aufgrund einer vor dem 1.7.1953 erteilten Baubewilligung
   errichtet. Es befinden sich mehr als 2 selbstaendige
   Mietgegenstaende im Haus. Der Mietvertrag unterliegt daher
   der Vollanwendung des MRG.

5. Der/die Antragsteller/in haelt den vereinbarten
   Hauptmietzins fuer ueberhoeht, weil er den nach §16 Abs 2
   MRG zulaessigen Richtwertmietzins uebersteigt.

[Weitere relevante Angaben: Ausstattung, Zustand, Maengel,
Lagezuschlag-Einschaetzung etc.]

II. Antrag

Der/die Antragsteller/in stellt den Antrag, die
Schlichtungsstelle moege feststellen, dass

1. der gesetzlich zulaessige monatliche Hauptmietzins fuer den
   Mietgegenstand [Adresse, Tuernummer] EUR [x] betraegt;

2. der/die Antragsgegner/in schuldig ist, dem/der
   Antragsteller/in die seit [Datum des Mietbeginns / max. 3
   Jahre zurueck] zu viel bezahlten Hauptmietzinsbetraege
   zurueckzuzahlen.

III. Beilagen

- Kopie des Mietvertrags
- [Kontoauszuege / Zahlungsbelege]
- [Fotos des Mietgegenstands]
- [Grundbuchsauszug, falls vorhanden]

[Ort], am [Datum]

[Unterschrift]
[Name des Antragstellers / der Antragstellerin]
```

### 5B: Muster — Einwendungen gegen gerichtliche Aufkuendigung

```
An das
Bezirksgericht [Ort]
[Adresse]

GZ: [Geschaeftszahl des Kuendigungsverfahrens]

Beklagter/Gekuendigter:
[Vor- und Nachname]
[Adresse des Mietgegenstands]

Klaeger/Aufkuendigender:
[Vor- und Nachname / Firma des Vermieters]
[Adresse]

EINWENDUNGEN
gegen die Aufkuendigung vom [Datum]

Innerhalb offener Frist erhebt der/die Beklagte gegen die am
[Zustelldatum] zugestellte Aufkuendigung nachstehende

EINWENDUNGEN:

I. Sachverhalt

1. Der/die Beklagte ist Mieter/in der Wohnung [Adresse,
   Tuernummer] aufgrund des Mietvertrags vom [Datum].

2. Die Aufkuendigung stuetzt sich auf den Kuendigungsgrund
   des §30 Abs 2 Z [x] MRG ([Kuendigungsgrund benennen]).

3. Dieser Kuendigungsgrund liegt nicht vor, weil:
   [Ausfuehrliche Darstellung, warum der Kuendigungsgrund
   nicht erfuellt ist — z.B. kein nachteiliger Gebrauch,
   kein Zahlungsverzug, Eigenbedarf nicht gegeben etc.]

II. Beweis

[Beweisantraege: Urkunden, Zeugen, Parteienvernehmung]
- Mietvertrag vom [Datum] (Beilage ./1)
- [Weitere Urkunden]
- Einvernahme des Zeugen [Name, Adresse]
- Parteienvernehmung des/der Beklagten

III. Antrag

Der/die Beklagte stellt den Antrag, das Gericht moege die
Aufkuendigung vom [Datum] aufheben.

[Ort], am [Datum]

[Unterschrift]
[Name]
```

### 5C: Muster — Kuendigung durch den Mieter

```
[Name des Mieters]
[Adresse des Mietgegenstands]

An
[Name des Vermieters / Hausverwaltung]
[Adresse]

[Ort], am [Datum]

Einschreiben mit Rueckschein

Betrifft: Kuendigung des Mietvertrags ueber
[Adresse des Mietgegenstands, Stiege, Tuernummer]

Sehr geehrte/r [Name],

hiermit kuendige ich das Mietverhaeltnis ueber die oben
bezeichnete Wohnung ordnungsgemaess unter Einhaltung der
[vertraglichen / gesetzlichen] Kuendigungsfrist von
[1 / 3] Monat(en) zum [Datum, Monatsletzter].

[Bei befristetem Vertrag im Vollanwendungsbereich:]
Die Kuendigung erfolgt gemaess §29 Abs 2 MRG (vorzeitiges
Kuendigungsrecht des Mieters nach Ablauf des ersten
Vertragsjahres).

[Bei befristetem Vertrag im Teilanwendungsbereich:]
Die Kuendigung erfolgt gemaess Punkt [x] des Mietvertrags
vom [Datum], der ein vorzeitiges Kuendigungsrecht des
Mieters vorsieht.

Ich ersuche um Vereinbarung eines Termins fuer die
Wohnungsuebergabe und die Erstellung eines
Uebergabeprotokolls.

Gleichzeitig ersuche ich um Rueckzahlung der geleisteten
Kaution in Hoehe von EUR [x] samt aufgelaufener Zinsen
nach ordnungsgemaesser Uebergabe des Mietgegenstands auf
mein Konto:

IBAN: [IBAN]
BIC: [BIC]
Lautend auf: [Name]

Mit freundlichen Gruessen

[Unterschrift]
[Name]
```

### 5D: Muster — Klage auf Kautionsrueckzahlung

```
An das
Bezirksgericht [Ort]
[Adresse]

Klaeger/in:
[Vor- und Nachname]
[Adresse]

Beklagte/r:
[Vor- und Nachname / Firma des Vermieters]
[Adresse]

Streitwert: EUR [Kautionsbetrag + Zinsen]

KLAGE
auf Rueckzahlung der Mietkaution

I. Sachverhalt

1. Der/die Klaeger/in war Mieter/in der Wohnung [Adresse,
   Tuernummer] aufgrund des Mietvertrags vom [Datum]
   (Beilage ./1).

2. Bei Abschluss des Mietvertrags hat der/die Klaeger/in
   eine Kaution in Hoehe von EUR [x] an den/die Beklagte/n
   geleistet (Beilage ./2 — Zahlungsbeleg).

3. Das Mietverhaeltnis endete am [Datum] durch [Kuendigung /
   Zeitablauf / einvernehmliche Aufhebung].

4. Der Mietgegenstand wurde am [Datum] ordnungsgemaess
   zurueckgestellt (Beilage ./3 — Uebergabeprotokoll).

5. Trotz Aufforderung vom [Datum] (Beilage ./4) hat der/die
   Beklagte die Kaution bislang nicht zurueckgezahlt.

6. Es bestehen keine offenen Forderungen des/der Beklagten
   gegen den/die Klaeger/in. Saemtliche Mieten wurden
   bezahlt, der Mietgegenstand wurde in ordnungsgemaeßem
   Zustand (unter Beruecksichtigung der normalen Abnuetzung)
   zurueckgestellt.

II. Rechtliche Begruendung

Die Kaution ist eine Sicherstellung fuer Ansprueche des
Vermieters aus dem Mietverhaeltnis. Nach Beendigung des
Mietverhaeltnisses und ordnungsgemaesser Rueckgabe des
Mietgegenstands ist die Kaution zurueckzuzahlen, wenn keine
berechtigten Gegenforderungen bestehen (§1431 ABGB —
Rueckforderung einer Leistung, deren Rechtsgrund weggefallen
ist; OGH 7 Ob 216/06y).

Die Verzinsung der Kaution gebuehrt dem Mieter, da die
Kaution als Fremdgeld verzinslich anzulegen ist.

III. Beweis

- Mietvertrag vom [Datum] (Beilage ./1)
- Zahlungsbeleg Kaution (Beilage ./2)
- Uebergabeprotokoll vom [Datum] (Beilage ./3)
- Aufforderungsschreiben vom [Datum] (Beilage ./4)
- Parteienvernehmung des/der Klaeger/in

IV. Antrag

Der/die Klaeger/in stellt den Antrag, das Gericht moege
mit Urteil erkennen:

Der/die Beklagte ist schuldig, dem/der Klaeger/in den
Betrag von EUR [Kaution + Zinsen] samt 4% Zinsen seit
[Datum der Faelligkeit — angemessene Frist nach
Uebergabe] binnen 14 Tagen bei sonstiger Exekution
zu bezahlen.

[Ort], am [Datum]

[Unterschrift]
[Name]
```

---

## Step 6: Present Results

```markdown
# Mietrechtliches Verfahren — Analyse

**Sachverhalt:** [2-3 Saetze Zusammenfassung]
**MRG-Anwendungsbereich:** Vollanwendung / Teilanwendung / kein MRG
**Verfahrensart:** [Ausserstreit §37 MRG / Kuendigung / Raeumungsklage / Klage]
**Zustaendigkeit:** [Schlichtungsstelle + BG / BG direkt]

## Verfahrensweg

### Schritt 1: [Erster Verfahrensschritt]
[Konkreter Schritt mit Begruendung und Rechtsgrundlage]

### Schritt 2: [Zweiter Verfahrensschritt]
[Konkreter Schritt]

### Schritt 3: [etc.]

## Zustaendigkeit und Formalia

| Kriterium | Details |
|-----------|---------|
| Zustaendiges Gericht | BG [Ort] |
| Schlichtungsstelle vorgeschaltet? | Ja / Nein |
| Anwaltspflicht | Ja (Streitwert > EUR 5.000) / Nein |
| Gerichtsgebuehr | EUR [x] (GGG) / gebuehrenfrei (§37 MRG) |
| Streitwert | EUR [x] |
| Verfahrensdauer (Erfahrungswert) | ca. [x] Monate |

## Fristen

| Frist | Deadline | Rechtsfolge bei Versaeumung |
|-------|----------|---------------------------|
| [z.B. Einwendungen gegen Kuendigung] | [Datum] | Kuendigung wird rechtskraeftig |
| [z.B. Anrufung des BG gegen Schlichtungsstellenentscheidung] | 4 Wochen ab Zustellung | Entscheidung wird rechtskraeftig |
| [z.B. Verjaehrung Abloesrueckforderung] | 10 Jahre ab Zahlung | Anspruch verjaehrt |

## Erfolgsaussichten

| Faktor | Einschaetzung |
|--------|--------------|
| Rechtslage | [klar / strittig / unklar] |
| Beweislage | [gut / maessig / schwierig] |
| Risiken | [Reformatio in peius? Kostenrisiko?] |
| Gesamteinschaetzung | [Erfolgsaussicht in %] |

## Kostenrisiko

| Kostenposition | Betrag |
|---------------|--------|
| Gerichtsgebuehr (GGG) | EUR [x] |
| Rechtsanwaltskosten (falls erforderlich) | EUR [x] |
| Sachverstaendigengutachten (falls erforderlich) | EUR [x] |
| **Gesamtkosten bei Erfolg** | **EUR [x]** |
| **Gesamtkosten bei Misserfolg (inkl. gegnerische Kosten)** | **EUR [x]** |

## Muster / Entwurf
[Verweis auf das passende Template aus Step 5 oder konkreter Entwurf fuer den Einzelfall]

## Empfehlung

1. [Konkreter erster Schritt]
2. [Konkreter zweiter Schritt]
3. [Empfehlung Mietervereinigung / AK / Rechtsanwalt]

## Quellenstatus
| Kategorie | Status | Details |
|-----------|--------|---------|
| RIS MCP | Verfuegbar / Nicht verfuegbar | [connection status] |
| Gesetze | RIS_VERIFIED / OFFICIAL_WEB_VERIFIED / UNVERIFIED | [n] Normen geprueft |
| Judikatur | RIS_VERIFIED / OFFICIAL_WEB_VERIFIED / UNVERIFIED | [n] Entscheidungen |
| Pruefdatum | [YYYY-MM-DD] | |

---
Keine Rechtsberatung. Diese Analyse dient der verfahrensrechtlichen Orientierung und ersetzt nicht die Beratung durch einen Rechtsanwalt, die Mietervereinigung oder die Arbeiterkammer. Insbesondere bei Kuendigungsschutzverfahren und Raeumungsklagen ist anwaltliche Vertretung dringend empfohlen. Fristen sind zwingend einzuhalten — bei Versaeumung droht Rechtsverlust. Musterantraege und -schriftsaetze muessen auf den Einzelfall angepasst werden.
```

---

## Critical Rules

1. **Schlichtungsstelle ZUERST in Wien und anderen Gemeinden mit Schlichtungsstelle** — §39 Abs 1 MRG: Antrag MUSS zuerst bei der Schlichtungsstelle eingebracht werden. Direkter Gang zum BG ist unzulaessig und fuehrt zur Zurueckweisung. Diese Regel dem User klar kommunizieren.
2. **4-Wochen-Frist bei Einwendungen gegen Kuendigung** — Versaeumung = Kuendigung wird rechtskraeftig = Raeumung. Diese Frist ist existenziell und muss prominent kommuniziert werden.
3. **Nachzahlungsrecht bei Zahlungsverzug (§33 Abs 2 MRG)** — Mieter kann durch Zahlung des gesamten Rueckstands bis Schluss der muendlichen Verhandlung 1. Instanz die Kuendigung/Raeumung abwenden. Dieses Rettungsmittel immer erwaehnen.
4. **Gebuehrenfreiheit bei §37 MRG-Verfahren** — Verfahren nach §37 MRG (Mietzinsueberpruefung, Erhaltungsauftrag, Abloesrueckforderung etc.) sind gebuehrenfrei. Keine GGG-Pauschalgebuehr. Niedrige Kostenschwelle fuer Mieter.
5. **Anwaltspflicht nur bei streitigem Verfahren ueber EUR 5.000** — Ausserstreitverfahren nach §37 MRG: keine Anwaltspflicht. Kuendigung/Raeumungsklage: Anwaltspflicht ab Streitwert EUR 5.000. Klar kommunizieren.
6. **10-Jahres-Verjaehrung bei Abloesrueckforderung** — §27 Abs 3 MRG. Wesentlich laenger als die uebliche 3-Jahres-Frist. Mieter haben oft auch Jahre spaeter noch einen Anspruch.
7. **Vorzeitiges Kuendigungsrecht nur bei Vollanwendung** — §29 Abs 2 MRG gilt NICHT bei Teilanwendung. Bei WEG-Wohnungen und Neubauten muss das vorzeitige Kuendigungsrecht vertraglich vereinbart sein. Haeufiger Fehler.
8. **Mietervereinigung und AK-Beratung empfehlen** — Kostenlose oder guenstige Beratung. Mietervereinigung Wien, AK Wien Mietrechtsberatung, Mieterhilfe Wien (MA 50). In jedem Verfahrensratschlag erwaehnen.
9. **Thermenregelung seit 1.1.2024 erwaehnen** — Bei Erhaltungsanfragen immer die MRG-Novelle 2023 beruecksichtigen.
10. **Match user's language** — German in = German out. English in = English out. Gesetze und Muster immer in deutscher Form.
11. **Reformatio in peius warnen** — Bei Beschwerde gegen Schlichtungsstellenentscheidung oder im Kuendigungsverfahren: Das Gericht kann auch zum Nachteil des Beschwerdefuehrers entscheiden. Risiko klar kommunizieren.
12. **Always cite specific §§** — Nie "laut Mietrecht" ohne §37 Abs 1 Z 8 MRG, §33 Abs 2 MRG, §1118 ABGB etc.
