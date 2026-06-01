---
name: consent-audit
title: Consent Audit — Einwilligungspruefung
description: 'Prueft Einwilligungs-Flows auf DSGVO-Konformitaet: DOI-Token-Ablauf, Widerruf-Workflow, Cookie-Banner'
author: Menschlichkeit-Osterreich
author_url: https://github.com/Menschlichkeit-Osterreich/menschlichkeit-oesterreich/tree/main/.claude/plugins/moe-compliance/skills/consent-audit
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: data-protection
language: de
---

# Consent Audit — Einwilligungspruefung

## Zweck

Prueft alle Einwilligungs-Mechanismen der Plattform auf DSGVO-Konformitaet.

## Pruefbereiche

### 1. Newsletter Double-Opt-In (DOI)

**Anforderung (DSGVO Art. 7):**

- Erstanmeldung → Bestaetigungs-Email → Klick auf Link → Eintrag aktiv
- DOI-Token MUSS ablaufen (max. 48h empfohlen)
- Zeitstempel der Einwilligung MUSS gespeichert werden
- Quelle der Einwilligung MUSS dokumentiert werden

**Pruef-Punkte:**

```
□ DOI-Token hat Ablaufzeit
□ Ablaufzeit ist <= 48 Stunden
□ Einwilligungs-Zeitstempel wird gespeichert
□ Einwilligungs-Quelle wird gespeichert (Formular-URL, API-Endpoint)
□ DOI-Email enthaelt klare Handlungsaufforderung
□ Ohne DOI-Bestaetigung wird KEINE Marketing-Email gesendet
```

**Dateien pruefen:**

- `apps/api/app/routers/newsletter.py`
- `apps/api/app/services/mail_service.py`
- `automation/n8n/workflows/onboarding-welcome-series.json`

### 2. Einwilligungswiderruf

**Anforderung (DSGVO Art. 7 Abs. 3):**

- Widerruf muss so einfach sein wie Erteilung
- Widerruf muss dokumentiert werden
- Nach Widerruf: Keine weitere Verarbeitung

**Pruef-Punkte:**

```
□ Abmeldelink in jeder Marketing-Email
□ Abmeldung mit maximal 2 Klicks moeglich
□ Widerruf-Zeitstempel wird gespeichert
□ CRM-Status wird nach Widerruf aktualisiert
□ n8n-Workflows respektieren Widerruf-Status
```

### 3. Cookie-Banner / ePrivacy

**Anforderung (TKG 2021, ePrivacy-Richtlinie):**

- Cookies erst nach Einwilligung setzen (ausser technisch notwendige)
- Granulare Auswahl (nicht nur Accept/Reject)
- Ablehnung muss genauso leicht sein wie Zustimmung

**Pruef-Punkte:**

```
□ Cookie-Banner vorhanden
□ Vor Einwilligung: Keine Marketing/Analytics-Cookies
□ Granulare Kategorien (Notwendig, Statistik, Marketing)
□ "Ablehnen"-Button gleichwertig mit "Akzeptieren"
□ Einwilligung gespeichert und dokumentiert
□ Widerruf jederzeit moeglich (Cookie-Einstellungen)
```

### 4. Kontaktformular

**Anforderung:**

```
□ Datenschutzhinweis beim Formular sichtbar
□ Link auf Datenschutzerklaerung
□ Keine unnuetzen Pflichtfelder (Datensparsamkeit)
□ Daten nur fuer Kontaktbearbeitung verwendet
```

## Output-Format

```
═══════════════════════════════════════
  Consent Audit — [Datum]
═══════════════════════════════════════

  Newsletter DOI:
  ✅ DOI-Flow implementiert
  ❌ Token-Ablauf nicht konfiguriert
  ✅ Zeitstempel gespeichert
  ⚠️ Quelle nicht dokumentiert

  Widerruf:
  ✅ Abmeldelink vorhanden
  ❌ CRM-Status-Update fehlt nach Widerruf

  Cookie-Banner:
  ✅ Banner vorhanden
  ⚠️ "Ablehnen" weniger prominent als "Akzeptieren"

───────────────────────────────────────
  Ergebnis: 2 kritische, 2 Warnungen
═══════════════════════════════════════
```
