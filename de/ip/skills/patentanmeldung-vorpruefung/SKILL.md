---
name: patentanmeldung-vorpruefung
title: 'Patentanmeldung vorpruefung'
description: Vor-Check der Patentierbarkeit einer Erfindung nach §§ 1–5 PatG / Art. 52, 54, 56 EPÜ – technischer Charakter (auch CII / Software-Grenze § 1 III/IV PatG), Neuheit § 3 PatG mit Neuheitsschonfrist, erfinderische Tätigkeit § 4 PatG nach Aufgabe-Lösungs-Ansatz, gewerbliche Anwendbarkeit § 5 PatG. Use when ein Erfinder oder Anmelder vor der Anmeldung beim DPMA, EPA oder über PCT klären will, ob ein Patent / Gebrauchsmuster aussichtsreich ist und welcher Anmeldeweg sinnvoll ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/patentrecht/skills/patentanmeldung-vorpruefung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: ip
language: de
---

# /patentrecht:patentanmeldung-vorpruefung

## Zweck

Der Skill prüft vor einer Patent- oder Gebrauchsmusteranmeldung, ob die Erfindung die materiellen Schutzvoraussetzungen erfüllt, und empfiehlt einen Anmeldeweg (DPMA, EPA mit Option Einheitspatent, PCT). Er soll vermeidbare Ablehnungen, Einsprüche und Nichtigkeitsangriffe durch frühzeitige Schwachstellenanalyse minimieren.

## Eingaben

- Erfindungsbeschreibung (technisches Problem, Lösung, Ausführungsbeispiele)
- bekannter Stand der Technik (eigene Recherche, fremde Schutzrechte)
- eigene Vorveröffentlichungen (Konferenzbeiträge, Messeauftritte, Publikationen, Webseiten) mit Datum
- gewünschte Schutzländer / Schutzstrategie (DE, EU/EPÜ, ausgewählte Länder, weltweit)
- bestehende Prioritätsanmeldungen (in- und ausländisch)
- bei Arbeitnehmererfindung: ArbnErfG-Stand (Meldung, Inanspruchnahme, Vergütung)

## Sub-Agent-Architektur

Researcher liefert PatG- und EPÜ-Statute, BGH-X-ZS- und EPA-Beschwerdekammer-Rechtsprechung zu Patentierbarkeit (insb. CII, Aufgabe-Lösungs-Ansatz) sowie Kommentarstellen aus Benkard, Schulte, Singer/Stauder. Drafter erstellt das Vorprüfungsgutachten und ein Skelett der Patentanmeldung (Beschreibung, Ansprüche, Zeichnungen) plus Strategie-Memo zum Anmeldeweg. Reviewer prüft, ob alle vier Schutzvoraussetzungen sauber durchgeprüft sind und Neuheitsschonfrist / Prioritätsfristen korrekt adressiert sind.

## Ablauf

### 1. Erfindungsgegenstand abgrenzen

Klärung, **was** die Erfindung ist (Erzeugnis, Verfahren, Verwendung). Bei Software-Anteilen: gibt es einen **technischen Beitrag** im Sinne der EPA-Beschwerdekammern (T 0641/00 „COMVIK" ([EPA-Entscheidungsdatenbank](https://www.epo.org/en/boards-of-appeal/decisions)) `[unverifiziert - prüfen]`) bzw. eine Lösung eines konkreten technischen Problems iSd BGH-Rspr. zu computerimplementierten Erfindungen?

### 2. Ausschlusstatbestände § 1 III, IV PatG / Art. 52 II, III EPÜ

Folgende Gegenstände sind **als solche** nicht patentierbar:

- Entdeckungen, wissenschaftliche Theorien, mathematische Methoden
- ästhetische Formschöpfungen (→ Design)
- Pläne, Regeln, Verfahren für gedankliche Tätigkeiten, Spiele, geschäftliche Tätigkeiten
- Programme für Datenverarbeitungsanlagen
- Wiedergabe von Informationen

Die „als solche"-Klausel ist der Hebel der Praxis. Computerimplementierte Erfindungen sind patentierbar, wenn sie ein **konkretes technisches Problem** mit **technischen Mitteln** lösen (BGH, [„Rentabilitätsermittlung", X ZB 34/03](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=19.10.2004&Aktenzeichen=X+ZB+34/03); BGH, „Logikverifikation", X ZB 11/98 ([dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Text=X+ZB+11/98)); EPA, G 0003/08 ([EPA-Entscheidungsdatenbank](https://www.epo.org/en/boards-of-appeal/decisions)) `[unverifiziert - prüfen]`).

Zusätzliche Ausschlüsse: Pflanzensorten / Tierrassen (§ 2a PatG), Heilbehandlungs- und Diagnoseverfahren am menschlichen / tierischen Körper (§ 2a I Nr. 2 PatG).

### 3. Neuheit § 3 PatG / Art. 54 EPÜ

Stand der Technik = alles, was vor dem Anmelde- bzw. Prioritätstag der Öffentlichkeit zugänglich war (weltweit, beliebige Sprache, beliebiges Medium). Maßstab: was der Fachmann der Vorveröffentlichung **unmittelbar und eindeutig** entnehmen konnte (EPA [G 0001/92](https://www.wipo.int/wipolex/en/judgments/details/2797)).

**Achtung Eigenvorveröffentlichungen.** Konferenzbeiträge, Messeauftritte, Pressemitteilungen, Veröffentlichungen auf der eigenen Website sind neuheitsschädlich.

**Neuheitsschonfrist § 3 V PatG**: 6 Monate vor Anmeldung, **nur** bei offensichtlichem Missbrauch oder anerkannter Ausstellung iSd § 3 V Nr. 2 PatG. **Das EPÜ kennt keine vergleichbare Schonfrist** außer Art. 55 EPÜ (missbräuchlich, anerkannte Ausstellung). Wer das EPA als Weg wählt, verliert die DE-Schonfrist faktisch.

Beim **Gebrauchsmuster (§ 3 GebrMG)** existiert demgegenüber eine **6-monatige Neuheitsschonfrist für eigene Vorveröffentlichungen** — Gebrauchsmuster ist deshalb gelegentlich „Rettungsanker" nach einer Vorveröffentlichung.

### 4. Erfinderische Tätigkeit § 4 PatG / Art. 56 EPÜ

Maßstab: Naheliegen für den Fachmann. EPA-Standard und BGH-Praxis nutzen den **Aufgabe-Lösungs-Ansatz** (problem-solution approach):

1. **Nächstliegender Stand der Technik** auswählen
2. **Objektive technische Aufgabe** formulieren (Unterschied der Erfindung gegenüber nächstliegendem Stand der Technik → technischer Effekt → Aufgabe)
3. **Naheliegen** prüfen: hätte der Fachmann ausgehend vom nächstliegenden Stand der Technik in Erwartung des technischen Effekts die beanspruchte Lösung naheliegend erreicht (could-would-Ansatz)?

Bei **gemischten Erfindungen** (technisch + nicht-technisch, etwa Geschäftsmethode + Computer) zählen nur die zum technischen Beitrag beitragenden Merkmale (EPA „COMVIK", T 0641/00 ([EPA](https://www.epo.org/en/boards-of-appeal/decisions)) `[unverifiziert - prüfen]`).

Beim **Gebrauchsmuster** gilt nur ein **„erfinderischer Schritt"** geringer Schwelle (§ 1 GebrMG) — niedrigere Anforderung als § 4 PatG.

### 5. Gewerbliche Anwendbarkeit § 5 PatG / Art. 57 EPÜ

In der Praxis selten Problem; Hauptfall: Heilbehandlungs- und Diagnoseverfahren (§ 2a I Nr. 2 PatG / Art. 53 c EPÜ). Erzeugnisansprüche („Stoff zur Verwendung in Verfahren X") bleiben patentierbar (zweckgebundener Stoffschutz).

### 6. Anmeldeweg-Strategie

| Weg | Wann sinnvoll |
|---|---|
| **DPMA (nationale Anmeldung)** | Schwerpunkt DE-Markt; kostensensible Anmelder; Strategie „erst DE-Prio, dann EPA / PCT innerhalb 12 Monaten" |
| **EPA (Europäische Anmeldung)** | mehrere EU-/EPÜ-Länder; Möglichkeit, nach Erteilung **Einheitspatent** zu wählen (VO (EU) Nr. 1257/2012) oder klassische Bündelphase mit nationaler Validierung |
| **PCT (Internationale Anmeldung)** | weltweite Strategie; Schiebung der Länderentscheidung auf 30/31 Monate; geeignet wenn Markt-/Lizenzpotential global |
| **Gebrauchsmuster (DPMA)** | Schnellschutz (kein Prüfungsverfahren), bis 10 Jahre Schutz, niedrigere Schwelle „erfinderischer Schritt"; Rettungsanker nach Eigenvorveröffentlichung wegen 6-Monats-Schonfrist § 3 GebrMG; **kein** Schutz für Verfahren (§ 2 Nr. 3 GebrMG) |

**Prioritätsrecht Pariser Übereinkunft (Art. 4):** 12 Monate für Patente, 6 Monate für Gebrauchsmuster ab Ersanmeldung. Innerhalb dieser Frist verschiebt sich der maßgebliche Zeitrang.

### 7. Arbeitnehmererfindung (falls einschlägig)

Bei Diensterfindung (§§ 4, 5 ArbnErfG):

- AN muss die Erfindung dem AG **unverzüglich schriftlich melden** (§ 5 ArbnErfG)
- AG kann die Erfindung **in Anspruch nehmen** (§ 6 ArbnErfG); seit Reform 2009 **Fiktion der Inanspruchnahme**, wenn der AG nicht binnen 4 Monaten freigibt
- Bei Inanspruchnahme: **Vergütungsanspruch** nach § 9 ArbnErfG, idR auf Basis der Vergütungsrichtlinien BMA 1959 (Lizenzanalogie / Anteilsfaktor / wirtschaftliche Verwertbarkeit)
- AG übernimmt Anmeldepflicht (§ 13 ArbnErfG)

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute

- [§ 1 PatG](https://www.gesetze-im-internet.de/patg/__1.html) (Patentfähige Erfindungen, Ausschlüsse III/IV)
- [§ 2, § 2a PatG](https://www.gesetze-im-internet.de/patg/__2.html) (öffentliche Ordnung, Heilbehandlung, Pflanzensorten)
- [§ 3 PatG](https://www.gesetze-im-internet.de/patg/__3.html) (Neuheit, Schonfrist Abs. 5)
- [§ 4 PatG](https://www.gesetze-im-internet.de/patg/__4.html) (erfinderische Tätigkeit)
- [§ 5 PatG](https://www.gesetze-im-internet.de/patg/__5.html) (gewerbliche Anwendbarkeit)
- [§ 35 PatG](https://www.gesetze-im-internet.de/patg/__35.html) (Anmeldung beim DPMA)
- [Art. 52 EPÜ](https://www.epo.org/de/legal/epc/2020/a52.html), [Art. 54 EPÜ](https://www.epo.org/de/legal/epc/2020/a54.html), [Art. 55 EPÜ](https://www.epo.org/de/legal/epc/2020/a55.html), [Art. 56 EPÜ](https://www.epo.org/de/legal/epc/2020/a56.html), [Art. 57 EPÜ](https://www.epo.org/de/legal/epc/2020/a57.html)
- [§ 1 GebrMG](https://www.gesetze-im-internet.de/gebrmg/__1.html), [§ 2 GebrMG](https://www.gesetze-im-internet.de/gebrmg/__2.html), [§ 3 GebrMG](https://www.gesetze-im-internet.de/gebrmg/__3.html)
- [VO (EU) Nr. 1257/2012](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32012R1257) (Einheitspatent)
- Pariser Übereinkunft, Art. 4 (Prioritätsrecht)
- ArbnErfG: [§ 5](https://www.gesetze-im-internet.de/arbnerfg/__5.html), [§ 6](https://www.gesetze-im-internet.de/arbnerfg/__6.html), [§ 9](https://www.gesetze-im-internet.de/arbnerfg/__9.html), [§ 13](https://www.gesetze-im-internet.de/arbnerfg/__13.html)

### Kommentare

- Melullis, in: Benkard, PatG, 12. Aufl. 2023, § 1 Rn. 1 ff., § 3 Rn. 1 ff., § 4 Rn. 1 ff.
- Moufang, in: Schulte, PatG, 11. Aufl. 2022, § 1 Rn. 1 ff.
- Mes, PatG, 5. Aufl. 2020, § 1 Rn. 1 ff., § 4 Rn. 1 ff.
- Singer/Stauder, EPÜ, 8. Aufl. 2022, Art. 52, 54, 56 jeweils Rn. 1 ff.
- Bartenbach/Volz, ArbnErfG, 6. Aufl. 2019, § 6, § 9 jeweils Rn. 1 ff.

### Rechtsprechung

1. EPA, Beschwerdekammer, T 0641/00 „COMVIK" ([EPA-Entscheidungsdatenbank](https://www.epo.org/en/boards-of-appeal/decisions)) `[unverifiziert - prüfen]` (gemischte Erfindungen, technischer Beitrag)
2. EPA, Große Beschwerdekammer, G 0003/08 ([EPA-Entscheidungsdatenbank](https://www.epo.org/en/boards-of-appeal/decisions)) `[unverifiziert - prüfen]` (Programme für Datenverarbeitungsanlagen)
3. EPA, Große Beschwerdekammer, [G 0001/92](https://www.wipo.int/wipolex/en/judgments/details/2797) (öffentliche Zugänglichkeit)
4. BGH, [Urt. v. 22.04.2010 – Xa ZB 20/08](https://dejure.org/dienste/vernetzung/rechtsprechung?Text=Xa+ZB+20/08) „Dynamische Dokumentengenerierung" (CII)
5. BGH, „Logikverifikation", X ZB 11/98 ([dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Text=X+ZB+11/98)); BGH, [„Rentabilitätsermittlung", X ZB 34/03](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=19.10.2004&Aktenzeichen=X+ZB+34/03); BGH, [„Webseitenanzeige", X ZR 121/09](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=24.02.2011&Aktenzeichen=X+ZR+121/09)
6. BGH, [„Olanzapin", X ZR 89/07](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=16.12.2008&Aktenzeichen=X+ZR+89/07) (Neuheit, individualisierte Offenbarung)

## Ausgabeformat

```
GUTACHTEN — Vorprüfung Patentierbarkeit
Anmelder/Erfinder: <anonymisiert>
Gegenstand: <Erfindung in 1–2 Sätzen>

I. Sachverhalt
   - Technischer Bereich
   - Bekannter Stand der Technik
   - Eigene Vorveröffentlichungen mit Datum
   - Gewünschte Schutzländer

II. Frage(n)
   - Patentierbarkeit?
   - Sinnvoller Anmeldeweg?
   - Gebrauchsmuster als Alternative / Doppelanmeldung?

III. Kurzantwort
    🟢 / 🟡 / 🔴 <Einstufung in einem Satz>

IV. Rechtliche Bewertung
    1. Technischer Charakter / Ausschlusstatbestände (§ 1 III/IV PatG, Art. 52 EPÜ)
    2. Neuheit § 3 PatG / Art. 54 EPÜ
       a) Stand der Technik
       b) Eigene Vorveröffentlichungen + Schonfrist
    3. Erfinderische Tätigkeit § 4 PatG / Art. 56 EPÜ (Aufgabe-Lösungs-Ansatz)
       a) Nächstliegender Stand der Technik
       b) Objektive technische Aufgabe
       c) Naheliegen-Prüfung
    4. Gewerbliche Anwendbarkeit § 5 PatG
    5. Ggf. Gebrauchsmuster-Vergleich (§ 1 GebrMG)
    6. Anmeldeweg-Strategie (DPMA / EPA / PCT; Einheitspatent ja/nein)
    7. Ggf. ArbnErfG-Hinweis

V. Skelett Patentanmeldung
   1. Titel
   2. Technisches Gebiet
   3. Stand der Technik
   4. Aufgabe und Lösung (objektive technische Aufgabe)
   5. Ansprüche
      Hauptanspruch (Erzeugnis / Verfahren / Verwendung)
      Unteransprüche (Ausgestaltungen)
   6. Ausführungsbeispiele
   7. Zeichnungen (Verweis)

VI. Risiken / offene Punkte
    - Eigenvorveröffentlichungs-Risiko
    - Anfechtbarkeit der erfinderischen Tätigkeit
    - Sachverständiger / Patentanwalt erforderlich

VII. Quellenverzeichnis
```

## Beispiele

**Szenario:** Start-up hat ein KI-Verfahren entwickelt, das aus Sensordaten einer Werkzeugmaschine Vorhersagen über Werkzeugverschleiß ableitet und die Maschine entsprechend ansteuert. Vor 3 Monaten Vortrag auf Fachkonferenz mit Folien-Veröffentlichung.

Kurzantwort: 🟡 Patentierbarkeit grundsätzlich aussichtsreich, da konkretes technisches Problem (Werkzeugverschleiß / Maschinensteuerung) mit technischen Mitteln gelöst wird (vgl. BGH-Linie zu CII, EPA „COMVIK", T 0641/00 ([EPA](https://www.epo.org/en/boards-of-appeal/decisions)) `[unverifiziert - prüfen]`). **Eigenvorveröffentlichung** ist kritisch: für EPA-Route faktisch neuheitsschädlich (Art. 55 EPÜ greift kaum); für DPMA enge Schonfrist § 3 V PatG. **Empfehlung**: Schnellanmeldung beim DPMA innerhalb der 6-Monats-Schonfrist; parallel Gebrauchsmuster-Abzweig (§ 5 GebrMG) als Rettungsanker; EPA-/PCT-Strategie unter Priorität der DPMA-Anmeldung innerhalb 12 Monaten.

## Risiken / typische Fehler

- **Eigenvorveröffentlichung übersehen** — Konferenzfolien, Webseite, Pitch-Deck zerstören Neuheit weltweit; EPÜ kennt keine Schonfrist außerhalb Art. 55.
- **Aufgabe-Lösungs-Ansatz nicht ausformuliert** — Anmeldung schwächt sich selbst, wenn die objektive technische Aufgabe nicht aus der Beschreibung ableitbar ist.
- **CII-Erfindungen ohne technischen Beitrag** — KI-Algorithmen ohne technische Wirkung außerhalb des Computers fallen unter § 1 III Nr. 3, IV PatG.
- **Gebrauchsmuster als Allheilmittel** — Verfahren sind nicht gebrauchsmusterfähig (§ 2 Nr. 3 GebrMG); kein Erteilungsverfahren, daher Rechtsbestand wackelig.
- **Pariser Prioritätsfrist (12 Monate) versäumt** — Verlust des Zeitrangs für Nachanmeldungen im Ausland.
- **ArbnErfG-Meldung vergessen** — Diensterfindung wird nach Reform 2009 ggf. fingiert in Anspruch genommen; Vergütungsanspruch nach § 9 ArbnErfG bleibt.
- **UPC-Opt-out nicht erwogen** — für validierte EP-Bündelpatente sollte über Opt-out während der Übergangszeit strategisch entschieden werden.
