---
name: auskunftsersuchen-art-15-borghei
title: /datenschutzrecht:auskunftsersuchen-art-15
description: Bearbeitung eines DSGVO-Auskunftsersuchens nach Art. 15 DSGVO – Identitätsprüfung, Umfang der Auskunft (Art. 15 Abs. 1 lit. a–h), Datenkopie (Abs. 3), Ausnahmen (Art. 15 Abs. 4; § 34 BDSG), 1-Monats-Frist (Art. 12 Abs. 3 DSGVO). Use when ein betroffener oder ehemaliger Vertragspartner Auskunft über die zu seiner Person verarbeiteten Daten verlangt.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/datenschutzrecht/skills/auskunftsersuchen-art-15
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: data-protection
language: de
---

# /datenschutzrecht:auskunftsersuchen-art-15

## Zweck

Art. 15-Anfragen sind oft Vorbereitung einer Forderung (Schadensersatz Art. 82 DSGVO, Bewerber-Diskriminierung, Mitarbeiterstreit). Dieser Skill prüft Identität, Umfang und Fristen und entwirft eine vollständige, **nicht über- und nicht unterbordige** Antwort.

## Eingaben

- Mandat (Verantwortlicher)
- Anfragender (Identität, Beziehung zum Verantwortlichen)
- Anfragezeitpunkt (Fristbeginn)
- Bekannte Verarbeitungen (CRM, Marketing, HR, Rechnungswesen)
- Vorgeschichte (Bewerbung abgelehnt? Kündigung? Streit?)

## Ablauf

### 1. Identitätsprüfung ([Art. 12 Abs. 6 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679))

Bei begründeten Zweifeln Identitätsnachweis verlangen. Verhältnismäßig: Geburtsdatum + Adresse, nicht Ausweiskopie pauschal (EDPB-Leitlinie 01/2022).

### 2. Fristen ([Art. 12 Abs. 3 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679))

- **1 Monat** ab Eingang, Verlängerung um 2 Monate bei Komplexität (mit Begründung an Betroffenen vor Ablauf des ersten Monats).
- **Eingangsbestätigung** umgehend empfohlen.

### 3. Umfang (Art. 15 Abs. 1 lit. a–h DSGVO)

Auskunft über:

a) Verarbeitungszwecke
b) Kategorien personenbezogener Daten
c) Empfänger / Empfängerkategorien (insb. Drittlandempfänger)
d) Geplante Speicherdauer / Kriterien
e) Recht auf Berichtigung, Löschung, Einschränkung, Widerspruch
f) Beschwerderecht bei Aufsichtsbehörde
g) Herkunft, wenn nicht beim Betroffenen erhoben
h) Automatisierte Entscheidungsfindung / Profiling (Art. 22)

### 4. Datenkopie (Art. 15 Abs. 3 DSGVO)

Kopie aller verarbeiteten Daten, **soweit** sie nicht in den Kreis der Beschränkungen fallen (Art. 15 Abs. 4 DSGVO; § 34 BDSG).

Format: maschinenlesbar oder lesbares PDF; bei elektronischer Anfrage standardmäßig elektronisch.

### 5. Beschränkungen (Art. 15 Abs. 4 DSGVO; [§ 34 BDSG](https://www.gesetze-im-internet.de/bdsg_2018/__34.html))

- Rechte und Freiheiten anderer dürfen nicht beeinträchtigt werden (insb. Geschäftsgeheimnisse, Daten Dritter).
- Spezielle Ausnahmen § 34 Abs. 1 BDSG (Auskunft entgegen RA-Schweigepflicht / Pseudonymisierung / Aufbewahrungs- vs. Löschpflicht).

### 6. Kostenfreiheit / Ausnahmen Art. 12 Abs. 5 DSGVO

Grundsätzlich unentgeltlich. Bei offensichtlich unbegründeten / exzessiven Anträgen: angemessenes Entgelt oder Ablehnung; **Begründungslast** beim Verantwortlichen.

### 7. Sonderfälle Beschäftigtendatenschutz

§ 26 BDSG. Auskunft über interne Bewertungen (Bewerbungsnotizen) ist umstritten — h.M.: ja, soweit nicht Geschäftsgeheimnis. Bei laufendem Arbeitsverhältnis: zusätzliches Beschwerderecht des Betriebsrats nach § 80 BetrVG beachten.

## Quellen

### Statute

- [Art. 15 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679) (Auskunft)
- [Art. 12 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679) (Verfahren)
- [Art. 82 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679) (Schadensersatz)
- [§ 34 BDSG](https://www.gesetze-im-internet.de/bdsg_2018/__34.html) (Beschränkungen)
- [§ 26 BDSG](https://www.gesetze-im-internet.de/bdsg_2018/__26.html) (Beschäftigtendaten)

### Leitlinien

- EDPB-Leitlinie 01/2022 zu Betroffenenrechten – https://edpb.europa.eu/

### Rechtsprechung

- EuGH, Urt. v. 04.05.2023 – C-487/21, NJW 2023, 2186 (Datenkopie weitreichend) `[unverifiziert – prüfen]`
- EuGH, Urt. v. 26.10.2023 – C-307/22, NZA 2023, 1429 (Auskunft im Beschäftigungsverhältnis) `[unverifiziert – prüfen]`
- BAG, Urt. v. 27.04.2021 – 2 AZR 342/20, NZA 2021, 1233 (Bewerber-Auskunft) `[unverifiziert – prüfen]`

## Ausgabeformat

```
DSGVO-AUSKUNFTSERSUCHEN – Antwortentwurf — <Mandat-ID> — <Datum>

I.   Identitätsprüfung               [✅ / ⚠️ Nachweis verlangt]
II.  Fristprüfung                    Eingang: <Datum> | Fristende: <+1 Monat>
III. Umfang (Art. 15 Abs. 1)
     a) Verarbeitungszwecke          <…>
     b) Datenkategorien              <…>
     c) Empfänger                    <…>
     d) Speicherdauer                <…>
     e) Betroffenenrechte            (Standardpassus)
     f) Beschwerderecht              (Standardpassus)
     g) Herkunft                     <…>
     h) Profiling / autom. Entscheidung  <…>

IV.  Datenkopie (Art. 15 Abs. 3)
     Anlage: <Liste>
     Beschränkungen (Art. 15 Abs. 4 / § 34 BDSG):
       - <…>

V.   Offene Punkte
     - <…>

Empfehlung: <…>
```

## Risiken / typische Fehler

- **Frist verpasst** → ggf. Schadensersatz Art. 82 DSGVO, Beschwerde bei Aufsichtsbehörde.
- **Über-Auskunft** → Verletzung Dritter (Art. 15 Abs. 4) → eigene Haftung.
- **Unter-Auskunft** → Wiederholungsersuchen + Schadensersatzandrohung.
- **Identitätsprüfung übersehen** → Datenweitergabe an Unbefugten (Art. 32 DSGVO Verletzung).
- **Geschäftsgeheimnisse** nicht geschwärzt → § 17 UWG / Art. 15 Abs. 4 Verstoß.
