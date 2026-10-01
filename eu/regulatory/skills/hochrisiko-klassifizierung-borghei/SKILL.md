---
name: hochrisiko-klassifizierung-borghei
title: /ki-vo-compliance:hochrisiko-klassifizierung
description: Klassifizierung eines KI-Systems als Hochrisiko-System nach Art. 6 i.V.m. Anhang III KI-VO – Anwendungsbereiche, Ausnahmen Art. 6 Abs. 3, Kennzeichnung als Sicherheitsbauteil Anhang I, Folgepflichten. Use when ein Unternehmen prüft, ob sein KI-System unter die Hochrisiko-Regelungen der KI-VO fällt.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/ki-vo-compliance/skills/hochrisiko-klassifizierung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: regulatory
language: de
---

# /ki-vo-compliance:hochrisiko-klassifizierung

## Zweck

Die Hochrisiko-Klassifizierung entscheidet über die anwendbaren Pflichten der KI-VO: Konformitätsbewertung, Risikomanagement, Datenqualität, Transparenz, menschliche Aufsicht, Logging, Genauigkeit/Robustheit/Cybersicherheit. Eine Fehlklassifizierung kann Bußgelder bis zu **15 Mio. EUR oder 3 % des weltweiten Jahresumsatzes** (Art. 99 Abs. 4 KI-VO) auslösen.

> **⚠️ Geltungsdaten nach dem Digital Omnibus on AI (Stand 2026-07):** Die Hochrisiko-Pflichten sind **verschoben**. Das KI-VO-Vereinfachungspaket wurde vom Europäischen Parlament am **16.06.2026** und vom Rat am **29.06.2026** endgültig angenommen.
>
> | Regelungsbereich | Geltung |
> |---|---|
> | Verbote Art. 5, KI-Kompetenz Art. 4 | 02.02.2025 (gilt) |
> | GPAI Art. 51–55 | 02.08.2025 (gilt) — **nicht verschoben** |
> | **Allgemeine Anwendung + Transparenz Art. 50** | **02.08.2026 — bleibt** |
> | **Hochrisiko Anhang III (Art. 6 Abs. 2, eigenständige Systeme)** | **02.12.2027** (vorher 02.08.2026) |
> | **Hochrisiko Anhang I (Art. 6 Abs. 1, Sicherheitsbauteil)** | **02.08.2028** (vorher 02.08.2027) |
> | Reallabore Art. 57 | 02.08.2027 (vorher 02.08.2026) |
> | Neue Verbote (NCII, CSAM) | 02.12.2026 |
> | Altmodelle GPAI (Art. 111 Abs. 3) | 02.08.2027 |
>
> **Keine pauschale Verschiebung:** Die Klassifizierung ist weiterhin einzelfallbezogen vorzunehmen — verschoben sind die *Pflichtenfolgen*, nicht die Einordnung. Art. 50 greift unabhängig von der Hochrisiko-Einstufung. Amtsblatt-Fundstelle der Änderungsverordnung `[unverifiziert - prüfen]`.

## Eingaben

- Funktion des KI-Systems (Use Case)
- Einsatzbereich (Anhang III prüfen: Biometrie, kritische Infrastruktur, Bildung, Beschäftigung, Zugang zu Diensten, Strafverfolgung, Migration, Justiz, Demokratie)
- Rolle des Mandanten (Anbieter, Betreiber, Importeur, Händler — Art. 3)
- Ist das KI-System Sicherheitsbauteil eines unter Anhang I fallenden Produkts?
- Greift eine Ausnahme nach Art. 6 Abs. 3 (vorbereitende Aufgabe, keine wesentliche Beeinflussung)?

## Ablauf

### 1. Anwendungsbereich der Hochrisiko-Klassifizierung (Art. 6)

Zwei Pfade:

- **Art. 6 Abs. 1** – KI-System ist Sicherheitsbauteil eines unter den in Anhang I gelisteten Harmonisierungsrechtsakten fallenden Produkts (z. B. MaschinenVO, MedizinprodukteVO, Spielzeug).
- **Art. 6 Abs. 2** – KI-System fällt in einen der 8 Anwendungsbereiche von Anhang III.

### 2. Anhang III – die 8 Hochrisikobereiche

1. **Biometrie** – Fernidentifizierung, Emotions-/Kategorisierungssysteme
2. **Kritische Infrastruktur** – Verkehr, Wasser, Gas, Strom, Heizung, digitale Infrastruktur
3. **Bildung & Berufsausbildung** – Zugang/Bewertung/Überwachung
4. **Beschäftigung & Personalmanagement** – Auswahl, Beförderung, Beendigung, Aufgabenzuweisung, Bewertung
5. **Zugang zu wesentlichen Diensten** – Kreditscoring (außer Betrug), Versicherungsrisiko, Notrufpriorisierung
6. **Strafverfolgung**
7. **Migration, Asyl, Grenzkontrolle**
8. **Justiz & demokratische Prozesse**

### 3. Ausnahme Art. 6 Abs. 3

KI-System ist **NICHT** hochrisiko-klassifiziert, wenn es kein erhebliches Risiko für Gesundheit, Sicherheit oder Grundrechte birgt **und** mindestens eine der vier Bedingungen erfüllt:

a) verrichtet eng begrenzte verfahrenstechnische Aufgabe
b) verbessert das Ergebnis einer zuvor abgeschlossenen menschlichen Tätigkeit
c) erkennt Entscheidungsmuster oder Abweichungen ohne Ersatz/Beeinflussung der menschlichen Bewertung
d) verrichtet vorbereitende Aufgabe für eine Bewertung im Sinne von Anhang III

**Profiling natürlicher Personen** ist von der Ausnahme ausgeschlossen — bleibt immer hochrisiko-klassifiziert (Art. 6 Abs. 3 letzter UAbs.).

### 4. Folgepflichten bei Hochrisiko-Einordnung

**Anbieter (Provider):**

- Risikomanagement-System Art. 9
- Daten- und Datengovernance Art. 10
- Technische Dokumentation Art. 11
- Aufzeichnungspflichten / Logging Art. 12
- Transparenz und Bereitstellung von Informationen Art. 13
- Menschliche Aufsicht Art. 14
- Genauigkeit, Robustheit, Cybersicherheit Art. 15
- Qualitätsmanagementsystem Art. 17
- Konformitätsbewertung Art. 43, Anhang VI/VII
- CE-Kennzeichnung, Eintragung in EU-Datenbank Art. 48, 71

**Betreiber (Deployer):**

- Nutzung gemäß Anbieter-Anweisungen Art. 26 Abs. 1
- Menschliche Aufsicht durch geschulte Personen Art. 26 Abs. 2
- Eingabedaten relevant und repräsentativ Art. 26 Abs. 4
- Überwachung des Betriebs Art. 26 Abs. 5
- Aufzeichnungen aufbewahren Art. 26 Abs. 6
- Informationspflichten an Beschäftigte und deren Vertreter Art. 26 Abs. 7
- DPIA-Verzahnung Art. 26 Abs. 9, Art. 27 (Grundrechte-Folgenabschätzung)
- Kennzeichnung gegenüber natürlichen Personen Art. 50 Abs. 3

### 5. Sanktionen Art. 99

- Verbotene Praktiken (Art. 5) → bis 35 Mio. EUR / 7 %
- Verstoß gegen Pflichten Art. 16/Art. 26 etc. → bis 15 Mio. EUR / 3 %
- Falsche Auskunft → bis 7,5 Mio. EUR / 1 %

## Quellen

### Statute

- [VO (EU) 2024/1689 – EU AI Act / KI-VO](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) — Volltext mit Anhängen
- Art. 6, Art. 26, Art. 50, Art. 99, Anhang III KI-VO (siehe Volltext)

### Leitlinien

- EU-Kommission, KI-Definitions-Leitlinien (Februar 2025)
- EU-Kommission, Leitlinien zur Anwendung von Verboten gemäß Art. 5 KI-VO
- Anhang III Use-Case-Verzeichnis der KI-VO

### Sekundärliteratur

- Hilgendorf/Roth-Isigkeit, KI-VO, 1. Aufl. 2024
- Spindler, in: Hofmann-Riem u.a., Handbuch der digitalen Verwaltung
- BeckOK KI-VO (Online)

## Ausgabeformat

```
HOCHRISIKO-KLASSIFIZIERUNG — <System-Bezeichnung> — <Datum>

I.    Rolle Mandant                 [Anbieter / Betreiber / Importeur / Händler]
II.   Anwendungsbereich Anhang III  [Nr. <X> / N/A]
      Begründung: <…>
III.  Sicherheitsbauteil Anhang I   [ja / nein]
IV.   Ausnahme Art. 6 Abs. 3        [a / b / c / d / nicht anwendbar]
      Profiling-Einschränkung: <…>
V.    Ergebnis                       [🟢 nicht hochrisiko / 🔴 HOCHRISIKO]
VI.   Folgepflichten (falls 🔴)
      - Risikomanagement Art. 9      …
      - Datengovernance Art. 10      …
      - …
VII.  Bußgeldrisiko Art. 99          [bis X Mio. EUR / Y %]

Empfehlung: <…>
Nächste Schritte: <…>
```

## Risiken / typische Fehler

- **Ausnahme Art. 6 Abs. 3 fehlinterpretiert** — die Ausnahme greift nur kumulativ mit "kein erhebliches Risiko"; reine Vorbereitung genügt nicht.
- **Profiling übersehen** — Art. 6 Abs. 3 schließt Profiling aus, die Ausnahme greift dann nie.
- **Rolle nicht sauber bestimmt** — Anbieter-/Betreiber-Pflichten unterscheiden sich grundlegend. Self-Build = oft Anbieter UND Betreiber.
- **Überholte Geltungsdaten verwendet** — die Hochrisiko-Pflichten gelten nach dem Digital Omnibus **erst ab 02.12.2027 (Anhang III)** bzw. **02.08.2028 (Anhang I)**. Mandanten, die noch auf den 02.08.2026 hinarbeiten, planen gegen aufgehobenes Recht; umgekehrt ist **Art. 50 zum 02.08.2026 unverändert anwendbar** und wird wegen der Hochrisiko-Verschiebung häufig übersehen.
- **Verschiebung mit Entwarnung verwechselt** — verschoben sind die Pflichtenfolgen, nicht die Klassifizierung. GPAI-Pflichten (Art. 51–55) sind **nicht** verschoben und ab 02.08.2026 bußgeldbewehrt.
- **Nationale Zuständigkeit falsch adressiert** — Marktüberwachungsbehörde ist die **Bundesnetzagentur** (Auffangzuständigkeit, KI-MIG), nicht die Datenschutzaufsicht; für Biometrie in der Strafverfolgung die unabhängige KI-Marktüberwachungskammer. `[unverifiziert - prüfen]`
- **Wechselwirkung mit DSGVO** — Art. 27 KI-VO verlangt eine Grundrechte-Folgenabschätzung zusätzlich zur DPIA Art. 35 DSGVO.
