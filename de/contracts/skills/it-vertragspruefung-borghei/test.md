---
skill: it-recht/it-vertragspruefung
fact_pattern: |
  Mandantin (mittelständischer Hersteller, 850 EE) plant SaaS-Migration zu
  US-Cloud-Provider (Salesforce). Vertragsdokument enthält: Haftungscap 50.000
  EUR auch bei grober Fahrlässigkeit, kein AVV-Anhang, Drittlandtransfer in
  die USA ohne SCC, einseitiges AGB-Anpassungsrecht des Anbieters, keine
  Datenexport-Garantie nach Vertragsende. Bewertung gewünscht.
must_cite:
  - "§ 305"
  - "§ 307"
  - "§ 309"
  - "Art. 28"
  - "Art. 32"
must_appear:
  - "AGB-Kontrolle"
  - "AVV"
  - "Drittlandtransfer"
  - "SLA"
  - "Datenherausgabe"
  - "Haftung"
  - "Data Act"
  - "12.09.2025"
  - "12.09.2026"
  - "12.01.2027"
  - "Bundesnetzagentur"
  - "Geschäftsgeheimnis"
must_flag:
  - "AVV"
  - "Drittlandtransfer"
  - "Haftungsausschluss"
  - "Vendor Lock-in"
  - "Data Act gar nicht geprüft"
  - "Art. 3 Abs. 1 auf Bestandsprodukte angewandt"
---

# Test — it-vertragspruefung

Struktureller Smoke-Test. AGB-Kontrolle §§ 305 ff. BGB, AVV Art. 28 DSGVO, Drittlandtransfer, SLA, Datenherausgabe und Haftungscap müssen sämtlich behandelt werden.

**Aktualitäts-Assertions (Stand 2026-07).** Der seit **12.09.2025** anwendbare **Data Act** (VO (EU) 2023/2854) muss ein eigener Prüfschritt im Ablauf sein und gilt **unabhängig vom Personenbezug** der Daten.

Die drei Datumsangaben prüfen die zentrale Abgrenzung:

- **12.09.2025** — Anwendungsbeginn des Data Act
- **12.09.2026** — **Art. 3 Abs. 1 (Zugang by design) gilt nur für danach in Verkehr gebrachte vernetzte Produkte.** Für Bestandsprodukte besteht **keine** Nachrüstpflicht; die Bereitstellungspflichten der **Art. 4 und 5** hängen umgekehrt **nicht** an diesem Stichtag. Beide Richtungen des Fehlers muss der Skill benennen.
- **12.01.2027** — vollständiger Wegfall der **Wechselentgelte** (bis dahin nur kostenbasiert reduziert)

Ferner gefordert: der **Geschäftsgeheimnis**-Vorbehalt als Grund für eine Beschränkung der Datenweitergabe — zulässig nur mit Schutzmaßnahmen und dokumentierter Einzelfallbegründung, nicht als Blankoklausel — sowie die **Bundesnetzagentur** als nach dem DADG (BGBl. 29.05.2026) zuständige Behörde.
