---
name: recht-familie-verfahren-momarcode1
title: /recht familie-verfahren — Familienrechtliche Verfahren (Procedural)
description: Austrian family law procedures — consensual and contested divorce proceedings, maintenance applications, custody proceedings (AusserStrG), contact rights applications, domestic violence protection orders (§382b EO), marital property division, and draft templates for Scheidungsvergleich and Unterhaltsantrag.
author: MoMarcode1
author_url: https://github.com/MoMarcode1/austrian-legal-claude/tree/main/skills/recht-familie-verfahren
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: at
practice: family
language: de
sources:
- title: Ris protocol
  path: references/ris-protocol.md
---

# /recht familie-verfahren — Familienrechtliche Verfahren (Procedural)

When the user needs to initiate or respond to a family law proceeding, draft court filings, or understand procedural steps, follow these steps exactly.

---

## Step 1: Read the Situation and Documents

Read everything the user has provided. Extract:

1. **Verfahrensart** — Which proceeding?
   - Einvernehmliche Scheidung (§55a EheG)?
   - Streitige Scheidung (§49 oder §55 EheG)?
   - Unterhaltsantrag (Ehegatten oder Kind)?
   - Obsorgeverfahren?
   - Kontaktrechtsregelung?
   - Einstweilige Verfuegung bei Gewalt (§382b EO)?
   - Aufteilungsverfahren (§§81ff EheG)?
   - Vaterschaftsfeststellung/-bestreitung?

2. **Verfahrensstand** — Was ist bereits passiert?
   - Noch kein Verfahren eingeleitet?
   - Antrag/Klage bereits eingebracht?
   - Beschluss/Urteil erhalten?
   - Rechtsmittel noetig?

3. **Zustaendigkeit** — Welches Gericht?
   - Bezirksgericht (BG) fuer fast ALLE familienrechtlichen Verfahren
   - Konkret: BG am gewoehnlichen Aufenthaltsort des Antragsgegners oder der Kinder

4. **Beteiligte** — Parteien, Kinder (Alter!), Vertreter
5. **Dringende Fristen** — Gibt es ablaufende Fristen?
6. **Vorhandene Dokumente** — Bescheide, Urteile, Vergleiche, Schriftverkehr?

If the Verfahrensart is unclear, ask:
> "Was genau moechten Sie erreichen? Moechten Sie eine Scheidung einleiten, Unterhalt beantragen, oder die Obsorge aendern?"

If critical dates are missing, ask:
> "Wann wurde die Scheidung rechtskraeftig? Die Frist fuer den Aufteilungsantrag (1 Jahr!) laeuft ab diesem Datum."

---

## Step 2: RIS Verification

Before proceeding with analysis, follow the **RIS Verification Protocol** (`references/ris-protocol.md`):
1. Check RIS MCP availability
2. For every § you cite in this analysis, verify current wording via RIS
3. For case law references (OGH), retrieve via RIS Justiz
4. Record verification status for the Quellenstatus block
5. If RIS is unavailable, follow the fallback ladder and flag all affected citations

---

## Step 3: Determine the Correct Proceeding and Procedure

### A: Einvernehmliche Scheidung (§55a EheG)

**Verfahrensart:** Ausserstreitverfahren (AusserStrG)
**Zustaendigkeit:** BG am letzten gemeinsamen gewoehnlichen Aufenthalt, sonst BG des Antragsgegners (§76a JN)
**Anwaltspflicht:** NEIN — kann ohne Anwalt beantragt werden

#### Voraussetzungen pruefen:
1. [ ] Ehe unheilbar zerrüttet
2. [ ] Eheliche Lebensgemeinschaft seit **mindestens 6 Monaten** aufgehoben (§55a Abs 1 EheG)
3. [ ] Beide Ehegatten einig ueber die Scheidung
4. [ ] Scheidungsvergleich ueber ALLE Scheidungsfolgen (§55a Abs 2 EheG):
   - [ ] Aufteilung des ehelichen Gebrauchsvermoegens und der ehelichen Ersparnisse
   - [ ] Ehegattenunterhalt (Hoehe oder Verzicht)
   - [ ] Obsorge fuer gemeinsame minderjaehrige Kinder
   - [ ] Kontaktrecht (Besuchsregelung)
   - [ ] Kindesunterhalt (Hoehe)
   - [ ] Ehewohnung (wer bleibt, wer zieht aus)

#### Ablauf:
1. Gemeinsamer Antrag beim BG + Scheidungsvergleich
2. Gerichtsgebuehr: Pauschalgebuehr nach GGG (TP 12 lit. b GGG) — derzeit EUR 312 (Stand pruefen!)
3. Verhandlung: Mündliche Verhandlung, beide Ehegatten muessen persoenlich erscheinen
4. Gericht prueft den Scheidungsvergleich, insbesondere:
   - Kindeswohl (§138 ABGB) — Gericht muss Vereinbarung ueber Obsorge und Unterhalt genehmigen
   - Kein Ehegatte offensichtlich benachteiligt
5. Bei Zustimmung: Scheidungsbeschluss
6. Rechtskraft: Nach 14 Tagen (wenn kein Rechtsmittel)

#### TEMPLATE: Scheidungsvergleich (§55a EheG)

```
SCHEIDUNGSVERGLEICH

abgeschlossen zwischen den Ehegatten

1.  [Vorname Nachname], geb. am [Datum], wohnhaft in [Adresse]
    (in der Folge "erster Ehegatte")

und

2.  [Vorname Nachname], geb. am [Datum], wohnhaft in [Adresse]
    (in der Folge "zweiter Ehegatte")

betreffend die einvernehmliche Scheidung ihrer am [Datum] vor dem
Standesamt [Ort], Zl. [Zahl], geschlossenen Ehe.

Die Ehegatten stellen fest, dass ihre eheliche Lebensgemeinschaft
seit mehr als sechs Monaten aufgehoben ist und die Ehe unheilbar
zerrüttet ist. Sie beantragen die Scheidung der Ehe im Einvernehmen
gemäß §55a EheG und schließen folgende

                        V E R E I N B A R U N G:

I. EHEGATTENUNTERHALT

[Variante A — Unterhaltsverzicht:]
Beide Ehegatten verzichten wechselseitig und unwiderruflich auf
jeglichen Ehegattenunterhalt. Dieser Verzicht gilt auch für den
Fall geänderter Verhältnisse sowie für den Fall der Not.

[Variante B — Unterhaltspflicht:]
Der [erste/zweite] Ehegatte verpflichtet sich, dem [zweiten/ersten]
Ehegatten einen monatlichen Unterhalt in Höhe von EUR [Betrag]
zu bezahlen, fällig jeweils am Ersten eines jeden Monats im Voraus.
Der Unterhaltsanspruch ist wertgesichert nach dem Verbraucherpreis-
index 2020 (Basismonat: [Monat/Jahr der Vereinbarung]).
Der Unterhaltsanspruch erlischt bei Wiederverheiratung des
Berechtigten oder bei Eingehen einer eingetragenen Partnerschaft.

[Variante C — Einmalzahlung:]
Der [erste/zweite] Ehegatte verpflichtet sich, dem [zweiten/ersten]
Ehegatten eine einmalige Unterhaltsabfindung in Höhe von EUR [Betrag]
zu bezahlen, fällig innerhalb von [x] Wochen nach Rechtskraft der
Scheidung. Mit dieser Zahlung sind sämtliche wechselseitigen
Unterhaltsansprüche abgegolten.

II. OBSORGE FÜR DIE GEMEINSAMEN MINDERJÄHRIGEN KINDER

[Variante A — Gemeinsame Obsorge:]
Die Obsorge für die gemeinsamen minderjährigen Kinder

-   [Vorname Nachname], geb. am [Datum]
-   [Vorname Nachname], geb. am [Datum]

steht beiden Elternteilen gemeinsam zu und bleibt aufrecht.
Der hauptsächliche Aufenthalt der Kinder wird im Haushalt des
[ersten/zweiten] Ehegatten festgelegt (hauptsächlich betreuender
Elternteil gemäß §180 Abs 2 ABGB).

[Variante B — Alleinige Obsorge:]
Die alleinige Obsorge für die gemeinsamen minderjährigen Kinder
wird dem [ersten/zweiten] Ehegatten übertragen.

III. KONTAKTRECHT

Der [erste/zweite] Ehegatte (nicht hauptsächlich betreuender
Elternteil) ist berechtigt und verpflichtet, die Kinder wie folgt
zu sich zu nehmen:

a) Jedes zweite Wochenende von Freitag [Uhrzeit] bis Sonntag [Uhrzeit]
b) [Ein Nachmittag] unter der Woche, [Wochentag], von [Uhrzeit]
   bis [Uhrzeit]
c) Die Hälfte der Schulferien:
   - Sommerferien: [x] Wochen
   - Weihnachtsferien: Im jährlichen Wechsel
   - Semesterferien: Im jährlichen Wechsel
   - Osterferien: Im jährlichen Wechsel
d) Feiertage im jährlichen Wechsel

Die Übergabe erfolgt [Ort/Modalitäten]. Änderungen sind einvernehmlich
und rechtzeitig zu vereinbaren.

IV. KINDESUNTERHALT

Der [erste/zweite] Ehegatte (nicht hauptsächlich betreuender
Elternteil) verpflichtet sich, für die gemeinsamen minderjährigen
Kinder monatlichen Geldunterhalt in folgender Höhe zu bezahlen:

-   [Name], geb. [Datum]:  EUR [Betrag] monatlich
-   [Name], geb. [Datum]:  EUR [Betrag] monatlich

jeweils fällig am Ersten eines jeden Monats im Voraus, auf das
Konto des obsorgeberechtigten/hauptsächlich betreuenden Elternteils.

Die Unterhaltsbeträge sind wertgesichert nach dem Verbraucherpreis-
index 2020. Eine Anpassung an geänderte Verhältnisse (insbesondere
altersbedingte Stufensprünge) bleibt vorbehalten.

V. EHELICHE ERRUNGENSCHAFT — AUFTEILUNG

[Variante A — Konkrete Aufteilung:]

a) Ehewohnung: Die Ehewohnung in [Adresse] wird dem [ersten/zweiten]
   Ehegatten zur alleinigen Nutzung zugewiesen. [Der Mietvertrag wird
   auf den Namen des übernehmenden Ehegatten übertragen. / Das Eigen-
   tum verbleibt beim [Ehegatten], der eine Ausgleichszahlung von
   EUR [Betrag] leistet.]

b) Hausrat: Der Hausrat wurde bereits einvernehmlich aufgeteilt.
   [ODER: Der Hausrat wird wie folgt aufgeteilt: ...]

c) KFZ: [Zuordnung]

d) Eheliche Ersparnisse:
   - Sparguthaben bei [Bank]: Verbleiben beim [Ehegatten]
   - Lebensversicherung [Nr.]: Verbleibt beim [Ehegatten]
   - [Weitere Vermögenswerte]

e) Schulden:
   - Kredit bei [Bank], Nr. [x]: Wird vom [Ehegatten] allein
     getragen, der den anderen im Innenverhältnis schad- und
     klaglos hält.

f) Ausgleichszahlung: Der [erste/zweite] Ehegatte leistet an den
   [zweiten/ersten] Ehegatten eine Ausgleichszahlung von EUR [Betrag],
   fällig innerhalb von [x] Wochen nach Rechtskraft der Scheidung.

[Variante B — Bereits aufgeteilt:]
Die Ehegatten erklären, dass das eheliche Gebrauchsvermögen und
die ehelichen Ersparnisse bereits einvernehmlich aufgeteilt sind.
Wechselseitige Ansprüche bestehen nicht mehr.

VI. VERFAHRENSKOSTEN

Die Kosten des Verfahrens (Pauschalgebühr) werden von beiden
Ehegatten je zur Hälfte getragen.
[ODER: Die Kosten werden vom [Ehegatten] allein getragen.]

VII. SCHLUSSBESTIMMUNGEN

Beide Ehegatten erklären, dass dieser Vergleich ihrem freien Willen
entspricht und sie über die Rechtsfolgen belehrt wurden.
Nebenabreden bestehen nicht.

[Ort], am [Datum]

_________________________          _________________________
[Erster Ehegatte]                  [Zweiter Ehegatte]
```

---

### B: Streitige Scheidung (§§49-55 EheG)

**Verfahrensart:** Streitiges Verfahren (ZPO) — KLAGE, nicht Antrag
**Zustaendigkeit:** BG am letzten gemeinsamen gewoehnlichen Aufenthalt, sonst BG des Beklagten (§76a JN)
**Anwaltspflicht:** NEIN — BG-Verfahren (aber dringend empfohlen!)

#### Scheidungsklage wegen Verschuldens (§49 EheG):

1. **Klageeinbringung** beim zustaendigen BG
2. **Inhalt der Klage:**
   - Parteien (Klaeger, Beklagter)
   - Eheschliessung (Datum, Ort, Standesamt-Zahl)
   - Eheverfehlungen des Beklagten (konkret, mit Datum und Details)
   - Zerrüttung der Ehe als Folge der Eheverfehlungen
   - Klagebegehren: "Die am [Datum] vor dem Standesamt [Ort] geschlossene Ehe wird aus dem Verschulden des Beklagten geschieden."
   - Eventuell: "in eventu aus dem überwiegenden Verschulden des Beklagten"
3. **Verfahrensablauf:**
   - Klagebeantwortung durch Beklagten (Frist: 4 Wochen, §230 ZPO)
   - Vorbereitende Tagsatzung (§258 ZPO)
   - Streitverhandlung: Beweisaufnahme (Zeugen, Urkunden)
   - Urteil mit Verschuldensausspruch
4. **Widerklage:** Beklagter kann Widerklage erheben (eigene Eheverfehlungen des Klaegers behaupten)
5. **Moegliche Ergebnisse:**
   - Scheidung aus alleinigem Verschulden des Beklagten
   - Scheidung aus alleinigem Verschulden des Klaegers (bei Widerklage)
   - Scheidung aus ueberwiegendem Verschulden einer Partei
   - Scheidung aus gleichteiligem Verschulden beider Parteien (§60 Abs 3 EheG)
   - Klageabweisung (keine Zerrüttung oder keine Eheverfehlung)
6. **Gebuehren:** Pauschalgebuehr nach GGG (TP 1 GGG), Streitwert EUR 750 (pauschal fuer Scheidungsklage)

#### Scheidungsklage wegen Aufhebung der Lebensgemeinschaft (§55 EheG):

1. Lebensgemeinschaft seit **mindestens 3 Jahren** aufgehoben
2. Haertefallpruefung (§55 Abs 3 EheG): Beklagter kann einwenden, dass die Scheidung ihn besonders hart traefe (selten erfolgreich)
3. Ab **6 Jahren** Trennung: Keine Haertefallpruefung mehr
4. **ACHTUNG:** Klaeger gilt als schuldig (§61 Abs 3 EheG) — nachehelicher Unterhalt wie bei Alleinverschulden!

#### Uebergang von streitig zu einvernehmlich:
- Jederzeit moeglich! Parteien koennen waehrend des streitigen Verfahrens auf einvernehmliche Scheidung umsteigen
- Empfehlenswert, wenn sich die Parteien einigen koennen — spart Kosten und Nerven

---

### C: Unterhaltsantrag

**Verfahrensart:**
- Kindesunterhalt: Ausserstreitverfahren (AusserStrG)
- Ehegattenunterhalt aufrecht: Streitiges Verfahren (ZPO) — Klage
- Nachehelicher Unterhalt: Streitiges Verfahren (ZPO) — Klage

**Zustaendigkeit:** BG am gewoehnlichen Aufenthalt des Kindes (Kindesunterhalt) oder des Antragsgegners (Ehegattenunterhalt)

#### Kindesunterhalt — Antrag (AusserStrG):

1. **Antrag beim BG (Pflegschaftsgericht)** durch den obsorgeberechtigten Elternteil oder durch das Kind (vertreten durch KJH oder Rechtsanwalt)
2. **Inhalt des Antrags:**
   - Antragsteller (Kind, vertreten durch ...)
   - Antragsgegner (unterhaltspflichtiger Elternteil)
   - Darlegung der Unterhaltspflicht (Abstammung)
   - Beduerfnisse des Kindes (Alter, Ausbildung, besonderer Bedarf)
   - Leistungsfaehigkeit des Unterhaltspflichtigen (Einkommen — soweit bekannt)
   - Konkreter Unterhaltsbetrag
3. **Provisorialantrag (§382a EO):** Bei dringendem Bedarf kann vorlaeufiger Unterhalt beantragt werden
   - Voraussetzung: Bescheinigung der Unterhaltspflicht und des Bedarfs
   - Gericht entscheidet rasch, ohne vollstaendige Beweisaufnahme
   - Provisorialunterhalt gilt bis zur endgueltigen Entscheidung

#### TEMPLATE: Unterhaltsantrag (Kindesunterhalt)

```
An das
Bezirksgericht [Ort]
Familienabteilung

Antragsteller/in:    [Vorname Nachname des Kindes], geb. am [Datum]
                     minderjährig, vertreten durch [Mutter/Vater:
                     Vorname Nachname], [Adresse]

Antragsgegner/in:    [Vorname Nachname], geb. am [Datum]
                     wohnhaft in [Adresse]
                     [Beruf, Arbeitgeber — soweit bekannt]

wegen:               Unterhalt

                     A N T R A G

Der/die Antragsteller/in stellt den

                     A N T R A G,

der/die Antragsgegner/in möge verpflichtet werden, dem/der minder-
jährigen Antragsteller/in ab [Datum] einen monatlichen Unterhalt
in Höhe von EUR [Betrag] zu bezahlen, jeweils am Ersten eines
jeden Monats im Voraus.

                     B E G R Ü N D U N G:

1.  Der/die Antragsteller/in ist das [eheliche/außereheliche] Kind
    des/der Antragsgegner/in. [Nachweis: Geburtsurkunde, Vater-
    schaftsanerkennung, gerichtliche Feststellung]

2.  Der/die Antragsteller/in lebt im Haushalt [der Mutter/des
    Vaters], die/der die Betreuung und Erziehung übernimmt und
    damit den Naturalunterhalt leistet.

3.  Der/die Antragsgegner/in ist daher gemäß §231 ABGB zur
    Leistung von Geldunterhalt verpflichtet.

4.  Der/die Antragsgegner/in ist [Beruf] und erzielt ein monatliches
    Nettoeinkommen von ca. EUR [Betrag]. [ODER: Das Einkommen ist
    dem/der Antragsteller/in nicht bekannt. Es wird die Offenlegung
    des Einkommens beantragt.]

5.  Unter Anwendung der Prozentwertmethode (OGH-Judikatur) ergibt
    sich bei einem Alter des Kindes von [x] Jahren ein Prozentsatz
    von [x]% des Nettoeinkommens, das sind EUR [Betrag].
    [Abzüge für weitere Sorgepflichten: ...]

6.  Der Regelbedarf für ein Kind im Alter von [x] Jahren beträgt
    derzeit EUR [Betrag] (BMJ-Erlass [Jahr]).

7.  [Sonderbedarf: Falls vorhanden, z.B. Krankheitskosten,
    besondere Ausbildungskosten]

BEWEIS:
./1  Geburtsurkunde des/der Antragstellers/in
./2  Meldebestätigung (Hauptwohnsitz bei [Elternteil])
./3  [Vaterschaftsanerkennung / Gerichtsurteil — falls nötig]
./4  [Einkommensnachweise des Antragsgegners — soweit vorhanden]
./5  [Nachweise Sonderbedarf — falls vorhanden]

[ORT], am [DATUM]

                              ________________________
                              [Unterschrift des gesetzlichen Vertreters]


PROVISORIALANTRAG (§382a EO):

Der/die Antragsteller/in stellt weiters den Antrag, dem/der
Antragsgegner/in mittels einstweiliger Verfügung aufzutragen,
vorläufig ab sofort einen monatlichen Unterhalt von EUR [Betrag]
zu bezahlen, bis zur rechtskräftigen Entscheidung über den
Unterhaltsantrag.

Begründung: Der/die Antragsteller/in ist dringend auf den Unterhalt
angewiesen. [Konkrete Darlegung der Dringlichkeit]
```

#### Ehegattenunterhalt — Klage (ZPO):

1. **Unterhaltsklage beim BG** (streitiges Verfahren)
2. Anwaltspflicht: NEIN (BG-Verfahren), aber empfohlen
3. Streitwert: Jahresbetrag des begehrten Unterhalts (§58 JN)
4. Gebuehren: Nach GGG, berechnet nach Streitwert
5. Beweismittel: Einkommensnachweise, Steuerbescheide beider Parteien

---

### D: Obsorgeverfahren (AusserStrG)

**Verfahrensart:** Ausserstreitverfahren (AusserStrG)
**Zustaendigkeit:** BG (Pflegschaftsgericht) am gewoehnlichen Aufenthalt des Kindes (§109 JN)
**Anwaltspflicht:** NEIN

**CRITICAL RULE: Kindeswohl (§138 ABGB) is the paramount consideration in ALL matters involving children. Every recommendation must be evaluated through this lens.**

#### Ablauf eines Obsorgeverfahrens:

1. **Antrag** beim zustaendigen BG
   - Antrag auf gemeinsame Obsorge (§177 ABGB)
   - Antrag auf alleinige Obsorge (§181 ABGB)
   - Antrag auf Aenderung der Obsorge

2. **Familiengerichtshilfe (§106a AusserStrG):**
   - Gericht kann Familiengerichtshilfe beauftragen
   - Erhebungen vor Ort (Hausbesuche)
   - Gespraech mit beiden Elternteilen und dem Kind
   - Bericht an das Gericht mit Empfehlung
   - Dauer: Üblicherweise 2-4 Monate

3. **Kinder- und Jugendhilfe (KJH):**
   - Wird vom Gericht einbezogen
   - Eigene Stellungnahme zum Kindeswohl
   - Kann selbst Antrag auf Obsorgeaenderung stellen (§181 ABGB) bei Kindeswohlgefaehrdung

4. **Kindesanhoerung:**
   - Kind wird ab ca. 10 Jahren persoenlich vom Richter angehoert
   - Ab 14 Jahren: Wille des Kindes hat besonderes Gewicht
   - Kindgerechte Befragung (nicht im Gerichtssaal, sondern in kindgerechter Umgebung)
   - Kind kann sich eines Kinderbeistands bedienen (§104a AusserStrG)

5. **Sachverstaendigengutachten:**
   - Bei komplexen Faellen: Psychologisches Gutachten zur Erziehungsfaehigkeit
   - Kosten: EUR 2.000-5.000+ (kann bei Verfahrenshilfe uebernommen werden)
   - Dauer: 3-6 Monate

6. **Phase der vorlaeufigen elterlichen Verantwortung (§180 ABGB):**
   - Bei Antrag auf Aenderung der Obsorge: Gericht bestimmt vorlaeufig den hauptsaechlich betreuenden Elternteil
   - Dauer: **6 Monate** (§180 Abs 1 ABGB)
   - Waehrend dieser Phase: Familiengerichtshilfe fuehrt Erhebungen durch
   - Nach Ablauf: Endgueltige Entscheidung durch das Gericht

7. **Entscheidung:**
   - Beschluss (nicht Urteil — Ausserstreitverfahren!)
   - Gemeinsame Obsorge mit Festlegung des hauptsaechlichen Aufenthalts
   - ODER alleinige Obsorge fuer einen Elternteil
   - Rekurs (Rechtsmittel) innerhalb von **14 Tagen** (§46 AusserStrG)

---

### E: Kontaktrechtsregelung

**Verfahrensart:** Ausserstreitverfahren (AusserStrG)
**Zustaendigkeit:** BG (Pflegschaftsgericht) am gewoehnlichen Aufenthalt des Kindes (§109 JN)

#### Ablauf:

1. **Antrag beim BG** auf Regelung des Kontaktrechts (§187 ABGB)
2. **Mediation empfohlen:** Gericht kann auf Mediation hinweisen (§107 Abs 3 AusserStrG)
3. **Familiengerichtshilfe:** Kann eingeschaltet werden
4. **Kindesanhoerung:** Je nach Alter
5. **Entscheidung:** Beschluss mit konkreter Regelung (Zeiten, Uebergabe, Ferien)
6. **Begleiteter Kontakt:** Wenn unbegleiteter Kontakt riskant — Besuchsbegleitung durch Familiengerichtshilfe oder anerkannte Einrichtung

#### Durchsetzung bei Verweigerung:
- **Zwangsmittel (§79 AusserStrG):** Geldstrafen gegen den verweigernden Elternteil
- **Beugestrafen** bis EUR 10.000
- **In extremen Faellen:** Aenderung der Obsorge (§181 ABGB)
- **Achtung:** Zwangsweise Vorführung des Kindes ist nur in Ausnahmefaellen zulässig (Kindeswohl!)

---

### F: Einstweilige Verfuegung bei Gewalt (§382b EO)

**Verfahrensart:** Provisorialverfahren (EO)
**Zustaendigkeit:** BG am gewoehnlichen Aufenthalt des Antragstellers (§387 Abs 2 EO) ODER jedes BG, in dessen Sprengel sich der Antragsteller aufhaelt
**Anwaltspflicht:** NEIN
**Gebuehren:** KEINE — gebuehrenfrei fuer Opfer haeuslicher Gewalt

#### Sofortmassnahmen — Schritt fuer Schritt:

1. **Polizei rufen (133):**
   - Polizei spricht Betretungs- und Annaeherungsverbot aus (§38a SPG)
   - Dauer: 14 Tage, verlaengerbar auf 4 Wochen bei Antrag auf EV
   - Polizei informiert automatisch das Gewaltschutzzentrum

2. **Gewaltschutzzentrum:**
   - Nimmt proaktiv Kontakt auf (innerhalb 24-48 Stunden)
   - Kostenlose Beratung und Begleitung
   - Hilft beim Antrag auf einstweilige Verfuegung

3. **Antrag auf einstweilige Verfuegung (§382b EO):**
   - Innerhalb von **14 Tagen** nach dem Betretungsverbot einbringen (damit Schutz nahtlos weitergeht)
   - Antrag beim BG — formlos moeglich, auch muendlich zu Protokoll
   - Keine Gebuehren, kein Anwalt noetig
   - Gericht entscheidet **innerhalb weniger Tage**, ohne Anhoerung des Gegners

4. **Inhalt der EV (§382b EO):**
   - Auftrag, die Wohnung zu verlassen und nicht zurueckzukehren
   - Verbot, sich der Wohnung zu naehern
   - Kontaktverbot (§382c EO)
   - Aufenthaltsverbot an bestimmten Orten: Schule der Kinder, Arbeitsplatz (§382c EO)

5. **Dauer der EV:**
   - Bis zu **6 Monate** (§382b Abs 3 EO)
   - Verlaengerbar auf **1 Jahr**, wenn ein Hauptverfahren (Scheidung, Obsorge) eingeleitet wird

6. **Verstoss gegen die EV:**
   - Strafbar nach §382g EO — Geldstrafe oder Haft bis zu 1 Jahr
   - Polizei kann sofort einschreiten

#### TEMPLATE: Antrag auf einstweilige Verfuegung (§382b EO)

```
An das
Bezirksgericht [Ort]

Antragsteller/in:    [Vorname Nachname], geb. am [Datum]
                     wohnhaft in [Adresse]

Antragsgegner/in:    [Vorname Nachname], geb. am [Datum]
                     wohnhaft in [Adresse]

wegen:               Einstweilige Verfügung zum Schutz vor Gewalt
                     in Wohnungen gemäß §382b EO

                     A N T R A G

auf Erlassung einer einstweiligen Verfügung gemäß §382b EO
[und §382c EO] [und §382d EO]:

Der/die Antragsteller/in stellt den Antrag, dem/der Antragsgegner/in
mittels einstweiliger Verfügung

1.  aufzutragen, die Wohnung in [Adresse] und deren unmittelbare
    Umgebung zu verlassen und das Betreten der Wohnung und deren
    unmittelbarer Umgebung zu verbieten;

2.  das Aufsuchen des/der Antragsteller/in am Arbeitsplatz, in der
    Schule der Kinder, im Kindergarten und an sonstigen bestimmten
    Orten zu untersagen (§382c EO);

3.  jegliche Kontaktaufnahme mit dem/der Antragsteller/in,
    insbesondere telefonisch, per SMS, E-Mail, über soziale Medien
    oder über Dritte, zu verbieten (§382c EO);

und dies bei Exekution durch Geldstrafe oder Haft.

                     B E G R Ü N D U N G:

1.  Der/die Antragsteller/in und der/die Antragsgegner/in sind
    verheiratet [ODER: leben in Lebensgemeinschaft / haben in der
    Vergangenheit in der genannten Wohnung zusammengelebt].

2.  Der/die Antragsgegner/in hat dem/der Antragsteller/in gegenüber
    [körperliche Gewalt ausgeübt / mit körperlicher Gewalt gedroht /
    psychische Gewalt ausgeübt], und zwar:

    [KONKRETE DARSTELLUNG DER GEWALTVORFÄLLE MIT DATUM UND DETAILS]

    Am [Datum] [Beschreibung des Vorfalls].
    Am [Datum] [Beschreibung des weiteren Vorfalls].

3.  Durch diese Handlungen ist das weitere Zusammenleben mit dem/der
    Antragsgegner/in unzumutbar (§382b Abs 1 EO).

4.  [Falls Kinder betroffen:] Die gemeinsamen minderjährigen Kinder
    [Namen, Alter] leben ebenfalls in der Wohnung und sind durch die
    Gewalttätigkeit des/der Antragsgegner/in gefährdet.

5.  [Falls polizeiliches Betretungsverbot besteht:] Die Polizei-
    inspektion [Ort] hat am [Datum] ein Betretungs- und Annäherungs-
    verbot gemäß §38a SPG gegen den/die Antragsgegner/in ausgesprochen,
    welches am [Datum] abläuft. Zur Aufrechterhaltung des Schutzes
    ist die Erlassung einer einstweiligen Verfügung dringend geboten.

BESCHEINIGUNGSMITTEL:
./1  [Polizeiprotokoll / Anzeige]
./2  [Ärztliches Attest / Verletzungsdokumentation]
./3  [Fotos]
./4  [Bestätigung Gewaltschutzzentrum]
./5  [Zeugen: Name, Adresse]
./6  [Betretungsverbot gemäß §38a SPG]

[ORT], am [DATUM]

                              ________________________
                              [Unterschrift]
```

---

### G: Aufteilungsverfahren (§§81ff EheG + AusserStrG)

**Verfahrensart:** Ausserstreitverfahren (AusserStrG)
**Zustaendigkeit:** BG am letzten gemeinsamen gewoehnlichen Aufenthalt der Ehegatten (§76a JN)
**Anwaltspflicht:** NEIN (aber dringend empfohlen bei hohen Vermoegen)

**FRIST: 1 JAHR ab Rechtskraft der Scheidung (§95 EheG) — PRAEEKLUSIVFRIST!**
**Wird diese Frist versaeumt, ist der Anspruch unwiederbringlich verloren!**

#### Ablauf:

1. **Antrag beim BG** auf Aufteilung des ehelichen Gebrauchsvermoegens und der ehelichen Ersparnisse (§81 EheG)
2. **Vermoegensaufstellung:**
   - Eheliches Gebrauchsvermoegen auflisten (Ehewohnung, Hausrat, PKW, etc.)
   - Eheliche Ersparnisse auflisten (Konten, Wertpapiere, Versicherungen)
   - Eingebrachtes, Geerbtes, Geschenktes abgrenzen (§82 EheG)
   - Schulden auflisten
3. **Verfahren:**
   - Gericht fuehrt Ermittlungen durch
   - Sachverstaendige fuer Liegenschaftsbewertung, Unternehmensbewertung
   - Billigkeitspruefung nach §83 EheG
4. **Entscheidung:** Beschluss ueber Aufteilung
   - Zuweisung von Vermoegensgegenstaenden
   - Ausgleichszahlung
   - Uebertragung von Mietrechten
   - Regelung der Ehewohnung
5. **Rekurs:** Innerhalb von **14 Tagen** (§46 AusserStrG)

---

## Step 4: Calculate Deadlines and Costs

### Fristen-Uebersicht

| Verfahren | Frist | Grundlage | Konsequenz bei Versaeumnis |
|-----------|-------|-----------|---------------------------|
| Aufteilungsantrag | **1 Jahr** ab Rechtskraft Scheidung | §95 EheG | Anspruchsverlust (Praeklusivfrist!) |
| Scheidungsklage (Verschulden) | **6 Monate** ab Kenntnis, max. **10 Jahre** | §57 EheG | Scheidungsgrund verfristet |
| Rekurs gegen Beschluss | **14 Tage** | §46 AusserStrG | Beschluss rechtskraeftig |
| Berufung gegen Urteil (Scheidung) | **4 Wochen** | §464 ZPO | Urteil rechtskraeftig |
| EV bei Gewalt | Sofort — **14 Tage** nach Betretungsverbot | §382b EO | Schutzluecke |
| Unterhaltsrueckstand | **3 Jahre** Verjaehrung | §1480 ABGB | Verjaehrte Betraege nicht einklagbar |

### Kostenabschaetzung

| Verfahren | Gebuehr (GGG) | Anmerkung |
|-----------|---------------|-----------|
| Einvernehmliche Scheidung | EUR 312 (TP 12 lit. b) | Stand pruefen! |
| Streitige Scheidung (Klage) | EUR 312 (TP 1, Streitwert EUR 750) | Pauschal |
| Unterhaltsantrag (Kind) | Gebuehrenfrei | §10 GGG — Minderjaehrige befreit |
| Unterhaltsklage (Ehegatte) | Nach Streitwert (Jahresbetrag) | TP 1 GGG |
| Obsorgeverfahren | EUR 290 (TP 12 lit. a) | Stand pruefen! |
| Kontaktrechtsverfahren | EUR 290 (TP 12 lit. a) | Stand pruefen! |
| Aufteilungsverfahren | Nach Streitwert | TP 12 lit. a GGG |
| EV bei Gewalt | **Gebuehrenfrei** | §10 GGG |
| Sachverstaendigengutachten | EUR 2.000-5.000+ | Vom Gericht bestimmt |

**Verfahrenshilfe (§63 ZPO):** Bei geringem Einkommen kann Verfahrenshilfe beantragt werden — befreit von Gebuehren und stellt kostenlosen Anwalt.

---

## Step 5: Present with Templates, Timeline, and Next Steps

```markdown
# Familienrechtliches Verfahren — Analyse

**Verfahrensart:** [Einvernehmliche Scheidung / Streitige Scheidung / Unterhaltsantrag / Obsorgeverfahren / Kontaktrecht / EV / Aufteilung]
**Zustaendiges Gericht:** Bezirksgericht [Ort]
**Anwaltspflicht:** Nein [aber empfohlen bei ...]

## Sofort-Warnungen

[Ablaufende Fristen, Gewaltschutz-Bedarf, Praeklusionsfristen]

## Verfahrensuebersicht

### Voraussetzungen
| Voraussetzung | Status | Details |
|---------------|--------|---------|
| [Voraussetzung 1] | Erfuellt / Fraglich / Nicht erfuellt | [Details] |

### Ablauf — Schritt fuer Schritt

1. **[Schritt 1]** — [Beschreibung, Frist, was zu tun ist]
2. **[Schritt 2]** — [...]
3. **[Schritt 3]** — [...]

### Erforderliche Unterlagen
- [ ] [Dokument 1 — z.B. Heiratsurkunde]
- [ ] [Dokument 2 — z.B. Geburtsurkunden der Kinder]
- [ ] [Dokument 3 — z.B. Einkommensnachweise]
- [ ] [Dokument 4 — z.B. Mietvertrag / Grundbuchauszug]

## Entwurf [Scheidungsvergleich / Unterhaltsantrag / EV-Antrag]

[Template mit konkreten Daten des Nutzers ausgefuellt]

## Kosten

| Position | Betrag | Anmerkung |
|----------|--------|-----------|
| Gerichtsgebuehr | EUR [x] | [Grundlage] |
| Rechtsanwalt (optional) | EUR [x] geschaetzt | [Falls empfohlen] |
| Sachverstaendiger | EUR [x] geschaetzt | [Falls erforderlich] |
| **Gesamt geschaetzt** | **EUR [x]** | |

## Fristen-Uebersicht

| Frist | Datum | Handlung erforderlich | Konsequenz bei Versaeumnis |
|-------|-------|----------------------|---------------------------|
| [Frist 1] | [Datum] | [Handlung] | [Folge] |

## Zeitplan

| Schritt | Geschaetzte Dauer | Anmerkung |
|---------|-------------------|-----------|
| Antrag einbringen | Sofort / bis [Datum] | |
| Erste Verhandlung | ca. 2-4 Monate | |
| Familiengerichtshilfe | ca. 2-4 Monate | [Falls relevant] |
| Entscheidung | ca. 4-12 Monate | |

## Naechste Schritte

- [ ] [Erste konkrete Handlung — z.B. Unterlagen zusammenstellen]
- [ ] [Zweite Handlung — z.B. Antrag beim BG einbringen]
- [ ] [Dritte Handlung — z.B. Rechtsanwalt konsultieren]

## Wichtige Kontakte

- **Bezirksgericht [Ort]:** [Adresse, Oeffnungszeiten]
- **Rechtsanwalt fuer Familienrecht:** [Anwaltssuche unter rechtsanwaelte.at]
- **Gewaltschutzzentrum:** [Bundeslandabhaengig — Telefon]
- **Frauen-/Maennerberatung:** [Je nach Situation]
- **Familienberatungsstelle:** [Fuer Mediation — kostenlos!]
- **Kinder- und Jugendhilfe:** [Bezirkshauptmannschaft / Magistrat]

## Quellenstatus
| Kategorie | Status | Details |
|-----------|--------|---------|
| RIS MCP | Verfuegbar / Nicht verfuegbar | |
| Gesetze | RIS_VERIFIED / UNVERIFIED | [n] Normen geprueft |
| Judikatur | RIS_VERIFIED / UNVERIFIED | [n] Entscheidungen |
| Pruefdatum | [YYYY-MM-DD] | |

---
**Keine Rechtsberatung.** Diese Analyse dient der rechtlichen Ersteinschaetzung und ersetzt nicht die Beratung durch einen Rechtsanwalt. Familienrechtliche Verfahren vor dem Bezirksgericht koennen ohne Anwalt gefuehrt werden, die Hinzuziehung eines Rechtsanwalts fuer Familienrecht wird jedoch dringend empfohlen. Bei geringem Einkommen besteht Anspruch auf Verfahrenshilfe (§63 ZPO). Bei haeuslicher Gewalt bieten die Gewaltschutzzentren kostenlose Beratung und Begleitung.
```

---

## Critical Rules

1. **Kindeswohl (§138 ABGB) is the paramount consideration in ALL matters involving children. Every recommendation must be evaluated through this lens.** Never draft an agreement or filing that prioritizes parental interests over the wellbeing of the child.
2. **Fristen sind entscheidend** — Die 1-Jahres-Praeklusivfrist fuer den Aufteilungsantrag (§95 EheG) ist die gefaehrlichste Frist im Familienrecht. Immer berechnen und prominent warnen.
3. **Gewalt sofort ansprechen** — Bei jedem Hinweis auf Gewalt sofort auf Polizei (133), Betretungsverbot (§38a SPG), einstweilige Verfuegung (§382b EO) und Gewaltschutzzentrum hinweisen. Sicherheit geht vor allem.
4. **Always cite specific §§** — §55a EheG, §231 ABGB, §382b EO. Nie vage auf "das Gesetz" verweisen.
5. **Templates konkret ausfuellen** — Wenn genug Fakten vorliegen, die Templates mit den konkreten Daten des Nutzers ausfuellen, nicht nur das Blankoformular zeigen.
6. **Einvernehmlich bevorzugen** — Immer erst pruefen, ob eine einvernehmliche Loesung moeglich ist. Hinweis auf Mediation und Familienberatungsstellen.
7. **Provisorialunterhalt hinweisen** — Wenn ein Kind dringend Unterhalt braucht und der Unterhaltspflichtige nicht zahlt, auf den Provisorialantrag (§382a EO) hinweisen.
8. **Unterhaltsvorschuss erwaehnen** — Wenn der Unterhaltspflichtige nicht zahlt, auf den Unterhaltsvorschuss (UVG) hinweisen: Antrag beim Pflegschaftsgericht, Staat zahlt vor.
9. **Kosten transparent machen** — Kindesunterhaltsverfahren sind gebuehrenfrei (§10 GGG), Gewaltschutz-EV ebenfalls. Das senkt die Hemmschwelle.
10. **Match user's language** — German in, German out. English in, English out. Statutes always in German form.
11. **Use RIS if connected** — Verify statute citations and OGH case law are current. Gebuehrenbetraege und Regelbedarfssaetze aendern sich — immer aktuellen Stand pruefen.
12. **Verfahrenshilfe hinweisen** — Bei erkennbar geringem Einkommen auf die Moeglichkeit der Verfahrenshilfe (§63 ZPO) hinweisen: Befreiung von Gebuehren und kostenloser Anwalt.
