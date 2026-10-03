---
name: dsgvo-email-check
title: DSGVO Email Check
description: 'Validiert Email-Templates auf DSGVO-Pflichtbestandteile: Abmeldelink, Impressum, Datenschutzhinweis, ZVR-Nummer, Base-Template-Vererbung'
author: Menschlichkeit-Osterreich
author_url: https://github.com/Menschlichkeit-Osterreich/menschlichkeit-oesterreich/tree/main/.claude/plugins/moe-compliance/skills/dsgvo-email-check
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: at
practice: regulatory
language: de
---

# DSGVO Email Check

## Zweck

Prueft Email-Templates auf alle rechtlich vorgeschriebenen Bestandteile gemaess DSGVO, ECG und Vereinsgesetz.

## Pflichtbestandteile

### 1. Abmeldelink (DSGVO Art. 7 Abs. 3) — KRITISCH

- Marketing-Emails MUESSEN einen funktionierenden Abmeldelink enthalten
- Formulierung z.B.: "Sie koennen sich jederzeit abmelden: [Link]"
- Link muss auf eine funktionierende Abmeldeseite verweisen
- Pattern: `abmeld|abbestell|opt-out|unsubscribe`

### 2. Impressum (ECG § 5) — KRITISCH

- Vollstaendiger Vereinsname
- Anschrift
- Kontaktmoeglichkeit (Email + optional Telefon)
- ZVR-Nummer
- Pattern: `impressum` oder Link auf Impressumsseite

### 3. Datenschutzhinweis (DSGVO Art. 13) — KRITISCH

- Link auf Datenschutzerklaerung
- URL: `https://www.menschlichkeit-oesterreich.at/datenschutz`

### 4. ZVR-Nummer (Vereinsgesetz § 18) — PFLICHT

- `ZVR: 1182213083` muss in geschaeftlicher Kommunikation angefuehrt werden

### 5. Base-Template-Vererbung — EMPFOHLEN

- Alle Email-Templates SOLLTEN vom Base-Template erben
- Base-Template enthaelt Footer mit allen Pflichtangaben
- Pruefe ob Template eigenstaendigen Footer hat oder Base-Template nutzt

## Pruef-Ablauf

1. Zieldateien identifizieren:

   ```bash
   find . -path '*/templates/email/*' -name '*.html' -o -name '*.mjml'
   ```

2. Jede Datei gegen Checkliste pruefen

3. Ergebnis pro Datei ausgeben

## Output-Format

```
═══════════════════════════════════════
  DSGVO Email Check — [Datum]
═══════════════════════════════════════

  📧 welcome.html
  ✅ Abmeldelink vorhanden
  ✅ Impressum verlinkt
  ✅ Datenschutz verlinkt
  ✅ ZVR-Nummer enthalten
  ✅ Base-Template genutzt
  → Status: KONFORM

  📧 newsletter-campaign.html
  ❌ Abmeldelink FEHLT (DSGVO Art. 7 Abs. 3)
  ✅ Impressum verlinkt
  ❌ Datenschutz FEHLT
  ✅ ZVR-Nummer enthalten
  ⚠️ Kein Base-Template
  → Status: NICHT KONFORM — 2 kritische Maengel

───────────────────────────────────────
  Ergebnis: 5/7 Templates konform
  2 Templates erfordern sofortige Korrektur
═══════════════════════════════════════
```
