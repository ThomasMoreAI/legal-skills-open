---
name: meldepflicht-24h-borghei
title: /nis2:meldepflicht-24h
description: NIS2-Meldepflichten bei erheblichen Sicherheitsvorfällen – 24-Stunden-Frühwarnung, 72-Stunden-Erstmeldung, Zwischen- und Endbericht (Art. 23 NIS2 / NIS2UmsuCG). Use when ein erheblicher Sicherheitsvorfall vorliegt oder ein Notfallplan für Meldungen an das BSI erstellt wird.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/nis2/skills/meldepflicht-24h
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: cybersecurity
language: de
---

# /nis2:meldepflicht-24h

## Zweck

Die NIS2-Meldepflicht hat **drei kaskadierende Fristen** (24h / 72h / 1 Monat). Eine versäumte Frist ist persönlich haftungsrelevant für die Geschäftsleitung (Art. 20 NIS2). Dieser Skill orchestriert die Meldungen und liefert die Vorlagen.

## Eingaben

- Klassifizierung der Einrichtung (wesentlich / wichtig — Anhang I/II)
- Art des Vorfalls (Cyberangriff / Systemausfall / Datenleck / Lieferkettenvorfall)
- Zeitpunkt der Kenntniserlangung
- Betroffene Dienste und potenzielle grenzüberschreitende Auswirkungen
- Vorab informierte Stellen (BSI, andere Aufsicht, Strafverfolgung)

## Ablauf

### 1. Erheblichkeitsschwelle (Art. 23 Abs. 3 NIS2)

Vorfall ist meldepflichtig, wenn er

- **schwerwiegende Betriebsstörungen** oder **erhebliche finanzielle Verluste** verursacht oder verursachen kann, **oder**
- andere natürliche oder juristische Personen durch erhebliche materielle/immaterielle Schäden betreffen kann.

### 2. 24-Stunden-Frühwarnung

An die zuständige Behörde (in DE: BSI über das Online-Meldeportal), enthält:

- Verdacht auf rechtswidrige oder bösartige Handlung
- Grenzüberschreitende Auswirkungen
- Status: Frühwarnung („Initial notification")

### 3. 72-Stunden-Erstmeldung

Vollständige Vorfallmeldung mit:

- Bewertung der Schwere
- Bewertung des Risikos
- Ggf. Indikatoren der Kompromittierung (IoCs)

### 4. Zwischenbericht

Auf Verlangen der Behörde, **kein** statischer Termin. Sinnvoll bei länger andauernden Vorfällen.

### 5. Endbericht (innerhalb 1 Monat ab Erstmeldung)

- Detaillierte Beschreibung des Vorfalls einschließlich Schweregrad und Auswirkungen
- Art der zugrunde liegenden Bedrohung oder Ursache
- Eingeleitete und laufende Abhilfemaßnahmen
- Ggf. grenzüberschreitende Auswirkungen

### 6. Verzahnung mit DSGVO Art. 33 / 34

Wenn personenbezogene Daten betroffen: **zusätzliche** DSGVO-Meldung an LfDI/BfDI binnen 72 h sowie ggf. Betroffenenbenachrichtigung Art. 34.

### 7. Strafverfolgung

Bei Verdacht auf Cyberstraftat (z. B. §§ 202a, 202c, 303a, 303b StGB): Anzeige an ZAC (Zentrale Ansprechstelle Cybercrime) erwägen.

## Quellen

### Statute

- [Richtlinie (EU) 2022/2555 (NIS2)](https://eur-lex.europa.eu/eli/dir/2022/2555/oj) — Art. 20, 21, 23, Anhang I/II
- NIS2UmsuCG (deutsches Umsetzungsgesetz, im Gesetzgebungsverfahren befindlich Stand 2026-05)
- [BSI – NIS2-Hinweise](https://www.bsi.bund.de/) — Anlaufstelle für die Meldungen
- [Art. 33 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679) für die DSGVO-Verzahnung

### Sekundärliteratur

- Eckhardt, NIS2, 1. Aufl. 2024
- Voigt/Schmitz, Cybersicherheitsrecht, 2. Aufl. 2024

## Ausgabeformat

```
NIS2-MELDUNG — <Vorfall-ID> — <Datum>

I.    Einordnung der Einrichtung    [wesentlich / wichtig]
II.   Erheblichkeit (Art. 23 Abs. 3) [✅ / ❌]
III.  Meldekaskade
      24h-Frühwarnung   Frist: <Datum + 24h>  Status: <abgesetzt / offen>
      72h-Erstmeldung    Frist: <Datum + 72h>  Status: <…>
      Endbericht         Frist: <Datum + 1M>   Status: <…>
IV.   Inhalte je Meldestufe          <Schablonen-Verweise>
V.    DSGVO-Verzahnung               [N/A / 72h-Meldung erforderlich]
VI.   Strafrechtliche Anzeige         [N/A / erwägen — § 202a StGB usw.]

Eskalationspfad: <Geschäftsleitung wann / wie>
Nächster Schritt: <…>
```

## Risiken / typische Fehler

- **24h-Frist** beginnt mit **Kenntniserlangung**, nicht mit "Bestätigung". Verzögerungstaktiken kosten Haftung.
- **Vergessene DSGVO-Verzahnung** bei personenbezogenen Daten — doppelte Meldepflicht.
- **Geschäftsleitung nicht eingebunden** — NIS2 verlangt explizit Schulung und Verantwortlichkeit der Leitung (Art. 20).
- **Lieferantenvorfall ignoriert** — auch Sicherheitsvorfälle bei IT-Dienstleistern können meldepflichtig sein (Art. 21 Abs. 2 lit. d).
- **„Bösartige Handlung" zu zögerlich angekreuzt** — bei Verdacht (nicht erst bei Beweis) ankreuzen.
