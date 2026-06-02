---
name: claims-guide
title: Schadenfall-Guide & Entscheidungslogik
description: Schadenfall-Guide und Entscheidungslogik. Leitet Schritt fuer Schritt durch jeden Schadenfall (Unfall, Krankheit, Haftpflicht, Hausrat, Auto, Rechtsschutz, Todesfall, Invaliditaet). Liefert Self-Service-Checklisten, klaert wann und wie melden, welche Nachweise noetig sind, und wie Fristen und Kommunikation laufen. Schweizer Kontext als Standard. Triggert bei Fragen zu Schadenfall, Schadenmeldung, Unfall melden, Versicherung melden, was tun bei Schaden, Schadenformular, Versicherungsfall, Schadenanspruch, Frist versaeumt, Versicherung zahlt nicht, Leistungsablehnung, Einsprache, Schadenregulierung.
author: philippfrenzel
author_url: https://github.com/philippfrenzel/claims-guide/tree/main/skills
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: ch
practice: insurance
language: de
---

# Schadenfall-Guide & Entscheidungslogik

## Overview

Dieser Skill ist ein interaktiver Notfallbegleiter fuer Versicherungsfaelle. Er fuehrt den Nutzer Schritt fuer Schritt durch den Schadenprozess — von der ersten Minute nach dem Ereignis bis zur abgeschlossenen Regulierung. Der Fokus liegt auf klaren Entscheidungsbaeumen: Was tun? Wem melden? Welche Nachweise? Welche Fristen?

**Standardkontext:** Schweiz (VVG, KVG, UVG, OR). Bei anderen Laendern werden die Referenzdaten entsprechend angepasst.

**Companion Skills:**
- **insurance-gap-analysis:** Zeigt nach dem Schadenfall, ob Deckungsluecken bestehen.
- **policy-check:** Hilft bei der Optimierung der Policen nach einem Schadenfall-Erlebnis.
- **scenario-stress-test:** Modelliert die finanziellen Auswirkungen laengerer Schadenfaelle.

**Wichtig:** Dieser Skill ersetzt keine Rechtsberatung. Bei komplexen oder strittigen Faellen immer einen Anwalt oder den Ombudsman der Privatversicherung einschalten. Bei Personenschaeden oder Strafrecht: Rechtsschutzversicherung aktivieren.

## Workflow

Dieser Skill hat einen anderen Aufbau als die uebrigen Finance-Skills. Statt 5 linearer Phasen arbeitet er mit einem Entscheidungsbaum: Der Nutzer beschreibt den Schadenfall, und der Skill leitet ihn durch die passende Route.

---

### Schritt 1 — Schadenfall identifizieren

Ziel: Art des Schadenfalls bestimmen und den richtigen Prozess einleiten.

Frage den Nutzer: **Was ist passiert?**

Ordne den Fall einer Kategorie zu:

| # | Kategorie | Beispiele |
|---|----------|----------|
| A | **Unfall (Person)** | Sturz, Verkehrsunfall, Sportunfall, Arbeitsunfall |
| B | **Krankheit / Arbeitsunfaehigkeit** | Langzeitkrankheit, psychische Erkrankung, Operation |
| C | **Haftpflichtschaden (verursacht)** | Du hast Drittperson/Sache beschaedigt |
| D | **Haftpflichtschaden (erlitten)** | Drittperson hat dich/deine Sache beschaedigt |
| E | **Hausrat / Gebaeudeschaden** | Einbruch, Wasserschaden, Feuer, Sturm, Diebstahl |
| F | **Autounfall / Fahrzeugschaden** | Kollision, Parkschaden, Diebstahl, Wildtier, Hagel |
| G | **Rechtsstreit** | Arbeitsrecht, Mietrecht, Kaufrecht, Nachbarrecht |
| H | **Todesfall** | Verstorbener Angehoeriger (Versicherungsansprueche) |
| I | **Invaliditaet** | Dauerhafte Einschraenkung nach Unfall oder Krankheit |
| J | **Reise** | Annullierung, Gepaeckverlust, Erkrankung im Ausland |
| K | **Anderer Schadenfall** | Cyber-Betrug, Identitaetsdiebstahl, Naturereignis |

Lade `references/swiss-claims-reference.md` als Referenz.

Frage anschliessend:
- **Wann** ist es passiert? (Datum, Uhrzeit)
- **Wo** ist es passiert? (Ort, Land)
- **Wer** ist beteiligt? (Personen, Zeugen)
- **Welche Versicherungen** koennten betroffen sein?
- **Wurde bereits etwas unternommen?** (Polizei, Arzt, Meldung)

---

### Schritt 2 — Sofortmassnahmen-Checkliste

Ziel: Sicherstellen, dass alle dringenden Schritte erledigt sind.

Liefere eine massgeschneiderte Sofortmassnahmen-Checkliste basierend auf der Kategorie:

**A) Unfall (Person):**
```
SOFORT (erste Stunde):
□ Erste Hilfe / Notruf 144 (Notfall) oder Hausarzt
□ Bei Arbeitsunfall: Arbeitgeber informieren
□ Bei Verkehrsunfall: Polizei 117 (bei Personenschaden Pflicht)
□ Unfallstelle sichern / dokumentieren
□ Fotos: Unfallstelle, Verletzungen, Schaeden
□ Zeugen: Namen und Kontaktdaten notieren
□ Europaeisches Unfallprotokoll ausfuellen (bei Autounfall)

INNERT 24 STUNDEN:
□ Arztbesuch (auch bei vermeintlich leichten Verletzungen!)
□ Arbeitsunfaehigkeits-Zeugnis ausstellen lassen
□ Arbeitgeber: Unfallmeldung (UVG-Formular)

INNERT 5 TAGEN:
□ Versicherungsmeldung: UVG (via Arbeitgeber), ev. KTG
□ Schadenmeldung an Haftpflicht (wenn Drittperson beteiligt)
□ Alle Belege sammeln (Arzt, Apotheke, Transport)
```

**B) Krankheit / Arbeitsunfaehigkeit:**
```
SOFORT:
□ Arztbesuch, Diagnose und Arbeitsunfaehigkeits-Zeugnis
□ Arbeitgeber informieren (sofort, gemaess Arbeitsvertrag)

INNERT 3 TAGEN:
□ AUF-Zeugnis an Arbeitgeber senden
□ KTG-Meldung pruefen (Arbeitgeber meldet, oder selbst bei Einzel-KTG)

BEI LAENGERER DAUER (>30 Tage):
□ Regelmaessige Arztbesuche und AUF-Verlaengerungen
□ Case Management (AG oder Versicherung) kooperieren
□ Bei >6 Monaten: IV-Frueherkennung pruefen
□ Bei >12 Monaten: IV-Anmeldung pruefen
```

**C) Haftpflicht (verursacht):**
```
SOFORT:
□ Entschuldigung (menschlich), KEIN Schuldanerkenntnis!
□ Geschaedigte Person: Kontaktdaten austauschen
□ Schaden dokumentieren (Fotos, Zeugen)
□ NICHTS unterschreiben, KEINE Zahlungen leisten

INNERT 48 STUNDEN:
□ Eigene Haftpflichtversicherung melden
□ Schadenhergang schriftlich festhalten (eigene Erinnerung)
□ Fotos und Zeugenangaben der Versicherung senden

WICHTIG:
□ Versicherung regelt den Fall — nicht selbst verhandeln
□ Versicherung prueft: Besteht Haftpflicht? Hoehe des Schadens?
□ Versicherung wehrt auch unberechtigte Forderungen ab (passiver RS)
```

**D) Haftpflicht (erlitten):**
```
SOFORT:
□ Schaden dokumentieren (Fotos, Videos, Zeugen)
□ Kontaktdaten des Verursachers aufnehmen
□ Polizei bei grossen Schaeden oder Streitigkeiten

INNERT 7 TAGEN:
□ Schaden schriftlich beim Verursacher geltend machen
□ Frist setzen (14-30 Tage)
□ Haftpflichtversicherung des Verursachers erfragen
□ Eigene Rechtsschutzversicherung informieren (falls vorhanden)

NACHWEISE SAMMELN:
□ Kostenvoranschlaege / Rechnungen fuer Reparatur
□ Fotos vorher/nachher (falls vorhanden)
□ Wertbelege (Kaufquittungen, Schaetzungen)
□ Aerztliche Zeugnisse (bei Personenschaden)
```

**E) Hausrat / Gebaeuedeschaden:**
```
SOFORT:
□ Notdienst bei akuter Gefahr (Feuerwehr 118, Wasserschaden stoppen)
□ Schaden begrenzen (Schadenminderungspflicht!)
□ NICHTS wegraumen oder reparieren vor Dokumentation
□ Fotos und Videos von ALLEM (uebersicht + Details)
□ Bei Einbruch/Diebstahl: Polizei 117 (Pflicht fuer Versicherung!)

INNERT 24-48 STUNDEN:
□ Versicherung melden (Hausrat und/oder Gebaeudeversicherung)
□ Schadenprotokoll erstellen (was, wann, wie, Wert)
□ Gestohlene/beschaedigte Gegenstaende auflisten

NACHWEISE:
□ Polizeirapport (bei Einbruch/Diebstahl)
□ Kaufbelege / Garantiescheine (falls vorhanden)
□ Fotos der beschaedigten Gegenstaende
□ Kostenvoranschlaege fuer Reparatur/Ersatz
```

**F) Autounfall / Fahrzeugschaden:**
```
SOFORT:
□ Warnblinkanlage, Pannendreieck aufstellen
□ Verletzte versorgen / Notruf 144
□ Polizei 117 bei Personenschaden (Pflicht), Sachschaden (>CHF 2'000 empfohlen)
□ Europaeisches Unfallprotokoll ausfuellen und unterschreiben
□ Kontaktdaten + Versicherung des Gegners aufnehmen
□ Fotos: Unfallstelle, Fahrzeuge, Schaeden, Kennzeichen, Uebersicht
□ Zeugen notieren

INNERT 48 STUNDEN:
□ Eigene Autoversicherung melden
□ Bei Fremdverschulden: Haftpflicht des Gegners kontaktieren
□ Werkstatt-Kostenvoranschlag einholen
□ Mietwagen-Bedarf abklaeren (Nutzungsausfall)

ENTSCHEIDUNG:
□ Eigenverschulden → Kaskoversicherung (falls vorhanden)
□ Fremdverschulden → Haftpflicht des Gegners
□ Parkschaden (unbekannt) → Kasko + Polizeimeldung
□ Wildtier → Teilkasko + Polizei/Wildhut
□ Hagel/Naturereignis → Teilkasko
```

**G) Rechtsstreit:**
```
SOFORT:
□ KEINE Unterschriften, KEINE Anerkennung von Forderungen
□ Fristen in Briefen/Verfuegungen notieren (Einsprachefrist!)
□ Rechtsschutzversicherung anrufen BEVOR eigener Anwalt

INNERT 7 TAGEN:
□ Rechtsschutz-Schadenmeldung
□ Versicherung prueft Deckung und weist Anwalt zu
□ Alle Dokumente chronologisch sammeln

WICHTIG:
□ Rechtsschutzversicherung MUSS vor Anwaltsbeauftragung zustimmen
□ Sonst: Kostenubernahme gefaehrdet
□ Wartefrist bei neuen Policen beachten (90 Tage)
```

**H) Todesfall:**
```
SOFORT (Tag 1-2):
□ Arzt rufen (Todesbescheinigung)
□ Bestattungsunternehmen
□ Zivilstandsamt informieren (Gemeinde)

INNERT 1 WOCHE:
□ Arbeitgeber des Verstorbenen informieren
□ Pensionskasse: Hinterlassenenleistungen anmelden
□ AHV-Zweigstelle: Witwen-/Waisenrente beantragen
□ Lebensversicherungen: Todesfall melden
□ Banken informieren

INNERT 1-3 MONATE:
□ UVG-Hinterlassenenleistung (falls Arbeitsunfall)
□ Saele 3a: Auszahlung an Beguenstigte
□ Erbschein beantragen (beim Bezirksgericht)
□ Steuerverwaltung: Steuererklarung des Verstorbenen
```

**I) Invaliditaet:**
```
FRUEHERKENNUNG (ab 30 Tage Arbeitsunfaehigkeit):
□ Arbeitgeber / IV-Stelle: Frueherfassung melden
□ KTG-Leistungen sicherstellen

IV-ANMELDUNG (ab 6-12 Monate):
□ Anmeldeformular bei kantonaler IV-Stelle
□ Aerztliche Berichte sammeln
□ Arbeitgeber-Bericht
□ Geduld: IV-Verfahren dauert 12-24 Monate

WAEHREND IV-VERFAHREN:
□ KTG laeuft weiter (max. 720 Tage)
□ Eingliederungsmassnahmen der IV mitwirken
□ Regelmaessig Arztbesuche dokumentieren

BEI IV-ENTSCHEID:
□ Verfuegung pruefen (IV-Grad, Rentenhoehe)
□ Bei Ablehnung: Einsprache innert 30 Tagen
□ BVG-Invalidenrente separat bei PK anmelden
□ IV-Zusatzversicherung aktivieren (falls vorhanden)
```

**J) Reise:**
```
ANNULLIERUNG:
□ Reiseveranstalter sofort informieren
□ Arztzeugnis einholen (bei Krankheit als Grund)
□ Reiseversicherung melden mit Belegen

GEPAECKVERLUST:
□ Am Flughafen: PIR-Formular (Property Irregularity Report)
□ Airline-Reklamation innert 21 Tagen (Montrealer Abkommen)
□ Reise-/Hausratversicherung melden

ERKRANKUNG IM AUSLAND:
□ Notfall-Nummer der Krankenversicherung anrufen
□ Arzt aufsuchen, Belege aufbewahren
□ Kostengutsprache bei grosseren Behandlungen
□ Ruecktransport mit Versicherung absprechen
```

---

### Schritt 3 — Schadenmeldung erstellen

Ziel: Den Nutzer beim Erstellen einer vollstaendigen Schadenmeldung unterstuetzen.

**3.1 Universelle Schadenmeldung:**

Hilf dem Nutzer, folgende Informationen zusammenzustellen:

```
SCHADENMELDUNG
==============
Policen-Nr.:        ...
Versicherungsnehmer: ...
Datum/Uhrzeit:       ...
Ort:                 ...

SCHADENHERGANG:
[Chronologische Beschreibung: Was ist passiert, wie ist es passiert,
wer war beteiligt. Sachlich, keine Spekulationen, keine Schuldzuweisung.]

BETEILIGTE PERSONEN:
Name, Adresse, Telefon, Versicherung (falls bekannt)

ZEUGEN:
Name, Adresse, Telefon

SCHADENHOEHE (geschaetzt):
- Sachschaden: CHF ...
- Personenschaden: [Beschreibung]
- Folgekosten: CHF ...

BEILAGEN:
□ Fotos (Anzahl: ...)
□ Polizeirapport (Nr.: ...)
□ Arztzeugnis
□ Kostenvoranschlaege
□ Kaufbelege
□ Europaeisches Unfallprotokoll
□ Weitere: ...

DATUM, UNTERSCHRIFT
```

**3.2 Kommunikationsregeln:**

```
DO:
✓ Sachlich und chronologisch beschreiben
✓ Nur Fakten, keine Vermutungen
✓ Vollstaendig — nichts weglassen
✓ Fristen einhalten
✓ Alles schriftlich (E-Mail oder Brief)
✓ Kopien aller Korrespondenz behalten

DON'T:
✗ Schuldanerkenntnis abgeben
✗ Voreilig Zahlungen leisten
✗ Schadenhoehe aufblaehen (Versicherungsbetrug!)
✗ Schaden verharmlosen
✗ Muendliche Abmachungen ohne schriftliche Bestaetigung
✗ Anwalt beauftragen ohne Rechtsschutz zu informieren
```

---

### Schritt 4 — Regulierungsprozess begleiten

Ziel: Den Nutzer durch den Regulierungsprozess begleiten und bei Problemen helfen.

**4.1 Typischer Ablauf:**

```
ZEITLEISTE SCHADENREGULIERUNG
==============================
Tag 0:    Schadenfall tritt ein
Tag 0-2:  Sofortmassnahmen + Dokumentation
Tag 1-5:  Schadenmeldung an Versicherung
Tag 5-10: Eingangsbestaetigung der Versicherung
Tag 10-30: Schadenprüfung durch Versicherung
           (Ev. Besichtigung durch Experten/Schadensinspektor)
Tag 30-90: Leistungsentscheid
           → Leistung oder (Teil-)Ablehnung

BEI ABLEHNUNG:
Tag 0-30:  Einsprache/Widerspruch (Frist beachten!)
Tag 30-90: Pruefung der Einsprache
           → Ev. Ombudsman einschalten
           → Ev. Rechtsschutz aktivieren (Klage)
```

**4.2 Entscheidungsbaum bei Problemen:**

```
VERSICHERUNG REAGIERT NICHT?
├── Eingangsbestaetigung fehlt (>10 Tage)
│   → Nachfassen per E-Mail + Frist setzen (14 Tage)
├── Keine Antwort auf Nachfrage
│   → Einschreiben mit Frist (14 Tage)
└── Weiterhin keine Antwort
    → Ombudsman oder FINMA-Beschwerde

LEISTUNG ABGELEHNT?
├── Begruendung nachvollziehbar?
│   ├── Ja → Akzeptieren (oder Deckung war tatsaechlich nicht gegeben)
│   └── Nein → Einsprache (schriftlich, mit Begruendung)
├── Leistung zu tief?
│   → Eigene Schaetzung/Gutachten einholen
│   → Differenz begruenden und nachfordern
└── Teilablehnung?
    → Akzeptierten Teil auszahlen lassen
    → Abgelehnten Teil separat anfechten

EINSPRACHE ABGELEHNT?
├── Ombudsman der Privatversicherung einschalten (kostenlos)
├── Rechtsschutzversicherung aktivieren
└── Klage (letztes Mittel)
    → Friedensrichter (bis CHF 2'000 obligatorisch)
    → Bezirksgericht (ab CHF 2'000)
    → Schlichtungsverfahren (Arbeits-/Mietrecht)

VERDACHT AUF UNFAIRE BEHANDLUNG?
├── Allgemeine Versicherungsbedingungen (AVB) selbst lesen
├── Ombudsman konsultieren (neutral, kostenlos)
├── FINMA-Beschwerde (bei systematischem Fehlverhalten)
└── Medien (Kassensturz, Espresso) als letztes Mittel
```

**4.3 Fristen-Uebersicht:**

Erstelle fuer den konkreten Fall eine Fristen-Checkliste:

| Frist | Beschreibung | Datum | Status |
|-------|-------------|-------|--------|
| Schadenmeldung | Innert X Tagen nach Ereignis | ... | □ |
| Einsprache bei Ablehnung | 30 Tage nach Verfuegung (VVG) | ... | □ |
| Einsprache IV/UVG | 30 Tage nach Verfuegung | ... | □ |
| Verjaehrung Forderung | 2 Jahre (VVG) / 5 Jahre (OR) | ... | □ |
| ... | ... | ... | □ |

---

### Schritt 5 — Schadenfall-Dossier Ausgabe

Erstelle ein Schadenfall-Dossier als Markdown:

```markdown
# Schadenfall-Dossier — {Kurzbeschreibung}
*Erstellt am {Datum}*

## Disclaimer
Dieses Dossier ersetzt keine Rechtsberatung. Bei strittigen Faellen,
Personenschaeden oder hohen Streitwerten einen Anwalt oder den
Ombudsman der Privatversicherung einschalten.

## 1. Schadenfall

| Merkmal | Details |
|---------|---------|
| Kategorie | {A-K} |
| Datum/Uhrzeit | ... |
| Ort | ... |
| Beschreibung | ... |
| Beteiligte | ... |
| Zeugen | ... |
| Geschaetzte Schadenhoehe | CHF ... |

## 2. Sofortmassnahmen

| # | Massnahme | Status | Erledigt am |
|---|-----------|--------|------------|
| 1 | ... | □ Offen / ✓ Erledigt | ... |

## 3. Betroffene Versicherungen

| Versicherung | Anbieter | Policen-Nr. | Meldung am | Status |
|-------------|----------|------------|-----------|--------|
| ... | ... | ... | ... | ... |

## 4. Nachweise

| # | Nachweis | Vorhanden | Bemerkung |
|---|---------|-----------|----------|
| 1 | Fotos | □ | ... |
| 2 | Polizeirapport | □ | ... |
| 3 | Arztzeugnis | □ | ... |
| 4 | Kostenvoranschlag | □ | ... |
| 5 | Kaufbelege | □ | ... |

## 5. Schadenmeldung (Entwurf)

{Vorbereitete Schadenmeldung}

## 6. Fristen

| Frist | Beschreibung | Datum | Status |
|-------|-------------|-------|--------|
| ... | ... | ... | □ |

## 7. Regulierungs-Tracker

| Datum | Aktion | Von | Status |
|-------|--------|-----|--------|
| ... | Schadenmeldung gesendet | Ich | ✓ |
| ... | Eingangsbestaetigung | Versicherung | □ |
| ... | Leistungsentscheid | Versicherung | □ |

## 8. Naechste Schritte

1. {Naechste konkrete Aktion}
2. {Weitere Aktion}
3. {Frist beachten: ...}
```

Speichere als `schadenfall-{kategorie}-{datum}.md`.

Optional JSON-Export fuer maschinelle Weiterverarbeitung:

```json
{
  "meta": {
    "erstellt": "YYYY-MM-DD",
    "version": "1.0",
    "typ": "claims-guide"
  },
  "schadenfall": {
    "kategorie": "A-K",
    "datum": "YYYY-MM-DD",
    "ort": "...",
    "beschreibung": "...",
    "schadenhoehe_geschaetzt": 0
  },
  "sofortmassnahmen": [
    {"massnahme": "...", "status": "offen|erledigt", "datum": null}
  ],
  "versicherungen": [
    {"art": "...", "anbieter": "...", "policen_nr": "...", "meldung_datum": null, "status": "offen|gemeldet|in_pruefung|entschieden"}
  ],
  "nachweise": [
    {"art": "fotos", "vorhanden": false, "bemerkung": "..."}
  ],
  "fristen": [
    {"beschreibung": "...", "datum": "YYYY-MM-DD", "status": "offen|erledigt"}
  ],
  "regulierung": [
    {"datum": "YYYY-MM-DD", "aktion": "...", "von": "ich|versicherung", "status": "offen|erledigt"}
  ]
}
```

---

## Wichtige Hinweise

- **Keine Rechtsberatung:** Dieser Skill ersetzt keinen Anwalt. Bei strittigen Faellen, Personenschaeden oder hohen Summen: Professionelle Hilfe holen.
- **Schadenminderungspflicht:** Der Versicherungsnehmer MUSS den Schaden begrenzen (VVG Art. 61). Wer nichts unternimmt, riskiert Leistungskuerzung.
- **Kein Schuldanerkenntnis:** Nie gegenueber Dritten die Schuld anerkennen — das ist Sache der Versicherung.
- **Dokumentation ist alles:** Fotos, Zeugen, Belege — je mehr, desto besser. Lieber zu viel als zu wenig dokumentieren.
- **Fristen sind heilig:** Versaeumte Fristen koennen zum Leistungsverlust fuehren. Im Zweifel sofort handeln.
- **Ombudsman ist kostenlos:** Der Ombudsman der Privatversicherung (ombudsman-assurance.ch) vermittelt kostenlos und neutral.
- **Iterativ:** Der Nutzer kann den Guide jederzeit fuer einen neuen Schadenfall starten.
- **Laenderanpassung:** Bei Nutzern ausserhalb der Schweiz: Rechtliche Grundlagen und Fristen anpassen.
- **Datenschutz:** Alle Daten bleiben lokal. Es werden keine Daten an externe Dienste gesendet.
- **Proaktiv:** Weise den Nutzer auf leicht vergessene Schritte hin (z.B. UVG-Meldung bei Arbeitsunfall, Polizeimeldung bei Diebstahl, Frist fuer Einsprache).
