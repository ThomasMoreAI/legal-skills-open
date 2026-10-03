---
name: freedom-to-operate
title: 'Freedom to operate'
description: Freedom-to-Operate-Analyse vor Markteintritt – Recherche relevanter Patente / Gebrauchsmuster (DEPATISnet, esp@cenet, Patentscope), Schutzbereichsbestimmung nach § 14 PatG / Art. 69 EPÜ mit Wortlaut- und Äquivalenzprüfung, Lebensphasen-Analyse (anhängig / erteilt / abgelaufen / nichtig), Handlungsoptionen bei Treffer (Designaround, Lizenz, Nichtigkeitsantrag § 81 PatG, Verzicht, Risiko-Akzeptanz). Use when ein Unternehmen vor Markteintritt klären muss, ob sein Produkt fremde Schutzrechte verletzt.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/patentrecht/skills/freedom-to-operate
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: ip
language: de
---

# /patentrecht:freedom-to-operate

## Zweck

Eine Freedom-to-Operate-Analyse (FTO, „Handlungsfreiheit") prüft, ob ein geplantes Produkt oder Verfahren fremde gewerbliche Schutzrechte verletzt. Sie ist Vorstufe der Verletzungsklage aus Sicht des potenziell Beklagten und Grundlage strategischer Entscheidungen (Designaround, Lizenznahme, Nichtigkeitsangriff). Der Skill liefert die Methodik zur Recherche, Schutzbereichsbestimmung und Handlungsempfehlung — mit klarer Begrenzung („zum Recherchestand X").

## Eingaben

- Produkt / Verfahren (technische Beschreibung, Zielmärkte)
- Zeitplan Markteintritt
- Branche und Technologie-Cluster (für Recherche-Strategie)
- bekannte Konkurrenten / typische Patentinhaber im Feld
- Risikoappetit (Designaround vs. Lizenz vs. Risikoakzeptanz)
- Budget für Recherche und Folgemaßnahmen

## Sub-Agent-Architektur

Researcher liefert PatG- und EPÜ-Statute zu Schutzbereich (§ 14, Art. 69) und Nichtigkeit (§ 81 PatG, Art. 138 EPÜ), BGH-Rspr. zu Äquivalenz, Kommentarstellen aus Benkard, Kühnen, Haedicke/Timmann. Drafter erstellt den FTO-Bericht mit Trefferliste, Schutzbereichsanalyse je Treffer und Handlungsempfehlung. Reviewer prüft Vollständigkeit der Recherche, korrekte Schutzbereichsmethodik und ausdrückliche Begrenzung des FTO-Berichts.

## Ablauf

### 1. Recherchestrategie

| Datenbank | Träger | Reichweite |
|---|---|---|
| **DEPATISnet** | DPMA | DE / international (kostenfrei) |
| **esp@cenet (Espacenet)** | EPA | weltweit, multilinguale Klassifikationssuche (kostenfrei) |
| **Patentscope** | WIPO | PCT-Anmeldungen weltweit (kostenfrei) |
| **DPMAregister** | DPMA | DE-Rechtsstand |
| **EP-Register** | EPA | EP-Verfahrensstand, Einspruch |
| Beck-Online / Mitt. / GRUR | kommerziell | Kommentare, Aufsätze |

Strategien: **Klassifikationssuche** (IPC / CPC), **Stichwortsuche** (mit Synonymen, technischen Begriffen mehrerer Sprachen), **Recherche nach Anmeldern / Erfindern** (Wettbewerber-Monitoring), **Zitatensuche** (Vorwärts-/Rückwärtszitate). Verbindlich: **Recherche-Protokoll** (Datenbanken, Klassifikationen, Stichwörter, Zeitstempel).

### 2. Trefferliste und Triage

Pro Treffer Erfassung:

- Aktenzeichen (DE / EP / WO / Einheitspatent)
- Anmelder / Inhaber
- Anmeldedatum / Veröffentlichungsdatum / Erteilungsdatum
- **Rechtsstand**:
  - **anhängig** (Anmeldung, noch nicht erteilt) — Schutz **erst ab Erteilung**, aber Anspruch auf angemessene Entschädigung ab Veröffentlichung möglich (§ 33 PatG)
  - **erteilt und in Kraft** — voller Schutz § 9 ff. PatG
  - **erteilt, aber Einspruchsverfahren anhängig** — Bestand offen, ggf. Aussetzung von Verletzungsklagen
  - **erloschen** (§ 20 PatG: Verzicht, Nichtzahlung Jahresgebühren) — frei nutzbar
  - **abgelaufen** (Schutzdauer 20 Jahre ab Anmeldung § 16 PatG; Gebrauchsmuster 10 Jahre § 23 GebrMG) — frei nutzbar (Achtung: Verkehrsbezeichnung / unlautere Übernahme)
  - **nichtig** (BPatG / EPA-Beschwerdekammer) — frei nutzbar
  - **validiert / nicht validiert** bei EP-Bündelpatent in Ziellandkreis?
  - **Einheitspatent** mit pan-europäischer Wirkung?
- Hauptanspruch (Volltext) + relevante Unteransprüche

### 3. Schutzbereichsbestimmung (§ 14 PatG / Art. 69 EPÜ)

Je Treffer:

1. **Merkmalsgliederung** des Hauptanspruchs (M1, M2, M3 …)
2. **Auslegung** unter Heranziehung von Beschreibung und Zeichnungen (Funktion der Merkmale aus Sicht des Fachmanns am Prioritätstag)
3. **Wortlautvergleich** mit dem geplanten Produkt / Verfahren — verwirklicht das Produkt jedes Merkmal wortsinngemäß?
4. **Äquivalenzkorridor** (BGH-„Schneidmesser"-Trias: [„Schneidmesser I", X ZR 168/00](https://lexetius.com/2002,244); [„Schneidmesser II", X ZR 135/01](https://lexetius.com/2002,243); „Schneidmesser III" `[unverifiziert – prüfen]`) — kann ein abgewandeltes Merkmal noch als äquivalent gelten?
5. **Akteneinsicht / Erteilungsverfahren** prüfen: hat der Anmelder Merkmale eingegrenzt? (Auswahlentscheidung — versperrt Äquivalenz, BGH [„Okklusionsvorrichtung", X ZR 16/09](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=10.05.2011&Aktenzeichen=X+ZR+16/09))

### 4. Lebensphasen-Logik

| Phase | Risiko für Markteintritt |
|---|---|
| **Anhängige Anmeldung** | mittel — Schutz greift erst bei Erteilung; Beobachtung der Veröffentlichung des Erteilungsbeschlusses; Anspruch § 33 PatG (Entschädigung) ab Veröffentlichung der Anmeldung möglich |
| **Erteilt + in Kraft** | hoch — § 9 ff. PatG voll wirksam; Verletzungsklage möglich |
| **Erteilt + Einspruchsverfahren** | mittel — Bestand wackelt; ggf. Aussetzung; Geltung dennoch bis zur rechtskräftigen Aufhebung |
| **Erteilt + Nichtigkeitsklage anhängig** | mittel-hoch — Verletzung wird verhandelt, Aussetzung § 148 ZPO denkbar |
| **Abgelaufen** | keines — frei nutzbar (ggf. unlauterer Wettbewerb § 4 Nr. 3 UWG zu prüfen, Querverweis `wettbewerbsrecht`) |
| **Erloschen wegen Nichtzahlung** | keines (sofern Wiedereinsetzung § 123 PatG ausgeschlossen) |
| **Nichtig erklärt** | keines — frei nutzbar |

### 5. Handlungsoptionen bei Treffer

Bei einem patentverletzungs-relevanten Treffer fünf Hauptoptionen:

1. **Designaround** — Produkt / Verfahren so modifizieren, dass mindestens **ein Merkmal** weder wortsinngemäß noch äquivalent verwirklicht wird. Saubere FTO-Bestätigung nach Modifikation erforderlich.
2. **Lizenznahme** — aktiv auf Inhaber zugehen (Achtung: schafft Aufmerksamkeit); FRAND-Themen bei SEPs (Querverweis kartellrecht). Lizenzvertrag § 15 PatG; Vertraulichkeit, Auditrechte, Vergütung beachten.
3. **Nichtigkeitsantrag § 81 PatG / Art. 138 EPÜ** — Angriff auf Bestand (mangelnde Patentierbarkeit nach §§ 1–5 PatG, unzulässige Erweiterung, mangelnde Offenbarung). Strategisch: vor oder im Verletzungsverfahren? Aussetzung § 148 ZPO im Verletzungsverfahren bei hinreichend wahrscheinlicher Nichtigkeit.
4. **Einspruch** bei noch laufender 9-Monats-Frist § 59 PatG / Art. 99 EPÜ — günstiger und schneller als Nichtigkeit; weite Einspruchsgründe gemäß Art. 100 EPÜ.
5. **Verzicht auf Markteintritt** / Verschiebung bis Patentablauf — wirtschaftliche Entscheidung.
6. **Risiko-Akzeptanz** mit Patentstreit-Versicherung — selten allein tragfähig; sinnvoll als Ergänzung bei Restrisiko.

### 6. FTO-Bericht-Aufbau und Begrenzung

Pflicht-Hinweis im Bericht:

> Diese FTO-Analyse beruht auf der Recherche in den genannten Datenbanken zum Stand `<Datum>`. Spätere Veröffentlichungen, nicht zugängliche Anmeldungen (Geheimhaltungsfrist, **18-Monats-Frist § 32 V PatG / Art. 93 EPÜ** vor Veröffentlichung) und Verfahrensänderungen können das Ergebnis beeinflussen. Keine Garantie der Vollständigkeit; Re-Check vor Markteintritt empfohlen.

Insbesondere die **18-Monats-Geheimhaltungsfrist** vor Erstveröffentlichung einer Anmeldung bedeutet, dass selbst eine perfekte Recherche „blind" für die letzten 18 Monate gefilter Anmeldungen ist.

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute

- [§ 9 PatG](https://www.gesetze-im-internet.de/patg/__9.html) (Wirkungen)
- [§ 14 PatG](https://www.gesetze-im-internet.de/patg/__14.html) (Schutzbereich)
- [§ 16 PatG](https://www.gesetze-im-internet.de/patg/__16.html) (Schutzdauer 20 Jahre)
- [§ 20 PatG](https://www.gesetze-im-internet.de/patg/__20.html) (Erlöschen)
- [§ 32 PatG](https://www.gesetze-im-internet.de/patg/__32.html) (Offenlegung 18 Monate)
- [§ 33 PatG](https://www.gesetze-im-internet.de/patg/__33.html) (Entschädigung nach Offenlegung)
- [§ 59 PatG](https://www.gesetze-im-internet.de/patg/__59.html) (Einspruch)
- [§ 81 PatG](https://www.gesetze-im-internet.de/patg/__81.html) (Nichtigkeitsklage)
- [§ 22 PatG](https://www.gesetze-im-internet.de/patg/__22.html) (Nichtigkeitsgründe)
- [Art. 69 EPÜ + Auslegungsprotokoll](https://www.epo.org/de/legal/epc/2020/a69.html)
- [Art. 99 EPÜ](https://www.epo.org/de/legal/epc/2020/a99.html), [Art. 100 EPÜ](https://www.epo.org/de/legal/epc/2020/a100.html) (Einspruch)
- [Art. 138 EPÜ](https://www.epo.org/de/legal/epc/2020/a138.html) (Nichtigkeit)
- [§ 23 GebrMG](https://www.gesetze-im-internet.de/gebrmg/__23.html) (Schutzdauer)

### Datenbanken (Recherchequellen, nicht Belegquelle)

- DEPATISnet (DPMA) — https://depatisnet.dpma.de
- Espacenet (EPA) — https://worldwide.espacenet.com
- Patentscope (WIPO) — https://patentscope.wipo.int
- DPMAregister — https://register.dpma.de
- EP-Register — https://register.epo.org

### Kommentare

- Scharen, in: Benkard, PatG, 12. Aufl. 2023, § 14 Rn. 1 ff.
- Kühnen, Handbuch der Patentverletzung, 16. Aufl. 2024, Kap. A (Schutzbereich), Kap. F (Designaround und FTO)
- Haedicke/Timmann, Handbuch des Patentrechts, 2. Aufl. 2020, § 7 (Verletzung), § 9 (Bestandsangriff)

### Rechtsprechung

1. BGH, [„Schneidmesser I", X ZR 168/00](https://lexetius.com/2002,244) und [„Schneidmesser II", X ZR 135/01](https://lexetius.com/2002,243) (Äquivalenz-Trias); „Schneidmesser III" `[unverifiziert – prüfen in juris/epo.org]`
2. BGH, [„Okklusionsvorrichtung", X ZR 16/09](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=10.05.2011&Aktenzeichen=X+ZR+16/09) (Auswahlentscheidung)
3. BGH, [„Diglycidverbindung", X ZR 69/10](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=13.09.2011&Aktenzeichen=X+ZR+69/10) (Auslegung)
4. EPA, [G 0001/92](https://www.wipo.int/wipolex/en/judgments/details/2797) (öffentliche Zugänglichkeit)

## Ausgabeformat

```
FTO-BERICHT
Mandant: <anonymisiert>
Produkt / Verfahren: <Kurzbeschreibung>
Recherchestand: <Datum>
Recherchegebiet: DE / EU / weltweit

I. Recherchemethodik
   - Datenbanken: DEPATISnet, Espacenet, Patentscope, …
   - Klassifikationen (IPC / CPC): <Liste>
   - Stichwörter (DE / EN / FR / …): <Liste>
   - Zeitfenster
   - Begrenzung: 18-Monats-Frist § 32 V PatG (nicht recherchierbare
     Anmeldungen)

II. Trefferliste (priorisiert)
    1. <AZ> — <Inhaber> — Rechtsstand: <…>
       Hauptanspruch (kurz)
       Risiko: 🟢 / 🟡 / 🔴
    2. …

III. Schutzbereichsanalyse je Treffer (priorisiert)
     Treffer 1: <AZ>
       a) Merkmalsgliederung Hauptanspruch
       b) Auslegung (§ 14 PatG / Art. 69 EPÜ)
       c) Wortlautvergleich mit geplantem Produkt
       d) Äquivalenzprüfung (Schneidmesser-Trias)
       e) Lebensphase / Bestandsrisiko
       f) Ergebnis: keine Verletzung / Verletzung wahrscheinlich /
          unklar

IV. Handlungsoptionen
    Treffer 1: <Designaround / Lizenz / Nichtigkeit § 81 PatG /
              Einspruch § 59 PatG / Verzicht / Risikoakzeptanz>
    – Wirtschaftliche Einschätzung
    – Erfolgsaussichten / Zeithorizont / Kosten

V. Gesamtrisikoeinstufung
   🟢 / 🟡 / 🔴 mit Begründung

VI. Empfehlung
    - Konkrete nächste Schritte
    - Re-Check vor Markteintritt: ja / nein, Datum
    - Patentstreit-Versicherung erwägen?

VII. Begrenzung des FTO-Berichts
     "Diese Analyse beruht auf dem Recherchestand vom <Datum>;
      § 32 V PatG-Geheimhaltungsfrist; keine Garantie der
      Vollständigkeit; Re-Check erforderlich."

VIII. Quellenverzeichnis
```

## Beispiele

**Szenario:** Mandantin (Medizingerätehersteller) plant Markteintritt mit neuem chirurgischen Instrument in DE + EU. FTO-Anfrage 6 Monate vor Launch.

Kurzantwort (🟡): Recherche in DEPATISnet, Espacenet, Patentscope; Klassifikation A61B 17/…; Treffer 1 — EP-Bündelpatent eines US-Wettbewerbers, in DE validiert, erteilt vor 4 Jahren, Hauptanspruch erfasst das geplante Produkt wortlautidentisch in M1–M4, M5 (Materialwahl Titan) nur **äquivalent** verwirklicht. **Handlungsoptionen**: (a) Designaround durch Verwendung eines spezifizierten Polymers (verlässt Äquivalenzkorridor); (b) Lizenzanfrage; (c) Nichtigkeitsantrag § 81 PatG, da Stand der Technik (Vorveröffentlichung 1998 in einer Fachzeitschrift) nach Recherche vermutlich neuheitsschädlich war. **Empfehlung**: parallel Designaround konstruktiv vorbereiten und Nichtigkeitsantrag prüfen; Lizenzanfrage nur, wenn beides scheitert (schafft Aufmerksamkeit). Re-Check unmittelbar vor Markteintritt zwingend wegen § 32 V PatG-Geheimhaltungsfrist.

## Risiken / typische Fehler

- **Recherchequalität überschätzt** — 18-Monats-Frist § 32 V PatG bedeutet faktische Blindheit für jüngste Anmeldungen; FTO-Bericht muss das ausdrücklich vermerken.
- **Nur DE-Patente recherchiert** — EP-Bündelpatente mit Validierung in DE, Einheitspatente und Gebrauchsmuster werden übersehen.
- **Schutzbereich nur über Wortlaut bestimmt** — Äquivalenzkorridor übersehen, falsches grünes Licht.
- **Lebensphase nicht geprüft** — abgelaufenes Patent als Risiko, erloschenes Patent mit möglicher Wiedereinsetzung § 123 PatG übersehen.
- **„Klassifikationssuche reicht"** — Synonyme, multilinguale Begriffe, Anmelder-Monitoring fehlen.
- **Lizenzanfrage zu früh** — schafft Aufmerksamkeit, lässt Schadensersatzanspruch des Inhabers ggf. „informiert" iSv § 139 II PatG erscheinen.
- **Einspruchsfrist § 59 PatG / Art. 99 EPÜ versäumt** — günstigste Bestandsangriffsoption nur 9 Monate ab Erteilungsveröffentlichung.
- **FTO-Bericht ohne Begrenzung formuliert** — Haftungsrisiko des Verfassers; Pflicht-Disclaimer einbauen.
