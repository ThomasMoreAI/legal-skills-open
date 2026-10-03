---
name: pii-scan
title: PII Scan — Personenbezogene Daten erkennen
description: Scannt Dateien und Logs auf personenbezogene Daten (PII) gemaess DSGVO — nutzt PiiSanitizer-Patterns
author: Menschlichkeit-Osterreich
author_url: https://github.com/Menschlichkeit-Osterreich/menschlichkeit-oesterreich/tree/main/.claude/plugins/moe-compliance/skills/pii-scan
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: at
practice: regulatory
language: de
---

# PII Scan — Personenbezogene Daten erkennen

## Zweck

Findet ungeschuetzte PII in Quellcode, Logs, Konfigurationsdateien und Outputs.

## PII-Kategorien (DSGVO Art. 4 Nr. 1)

| Kategorie              | Pattern                                          | Beispiel             |
| ---------------------- | ------------------------------------------------ | -------------------- |
| Email-Adressen         | `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}` | user@example.at      |
| Telefonnummern         | `(\+43\|0)[0-9 /-]{6,}`                          | +43 1 234 5678       |
| IBAN                   | `AT\d{18}`                                       | AT611904300234573201 |
| Sozialversicherungsnr. | `\d{4}[0-3]\d[01]\d{4}`                          | 1234 010190          |
| IP-Adressen            | `\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}`             | 192.168.1.1          |
| Postleitzahl + Ort     | `\b[1-9]\d{3}\b\s+[A-ZÄÖÜ][a-zäöüß]+`            | 1010 Wien            |
| Geburtsdatum           | `\d{2}\.\d{2}\.\d{4}`                            | 15.03.1990           |

## Scan-Bereiche

### Hoechste Prioritaet (MUSS sauber sein)

- `apps/api/app/routers/*.py` — API-Endpoints
- `automation/n8n/workflows/*.json` — n8n-Workflows
- `apps/api/tests/*.py` — Test-Dateien (Fixtures mit echten Daten?)
- `*.log` — Log-Dateien

### Mittlere Prioritaet

- `apps/website/src/**/*.tsx` — Frontend-Code
- `config-templates/` — Konfigurationsvorlagen
- `scripts/*.sh` — Shell-Scripts

### Ausnahmen (nicht scannen)

- `node_modules/`, `.git/`, `__pycache__/`
- `.env` (wird separat geschuetzt)
- Test-Fixtures mit explizit markierten Dummy-Daten

## Referenz: PiiSanitizer

Die autoritative PII-Sanitisierung liegt in:
`apps/api/app/lib/pii_sanitizer.py`

Dieses Modul ist die Single Source of Truth fuer PII-Patterns.
Alle neuen Endpoints MUESSEN den PiiSanitizer in der Middleware nutzen:
`apps/api/app/middleware/pii_middleware.py`

## Ablauf

1. Zielverzeichnis/Glob bestimmen
2. PII-Patterns anwenden
3. Fundstellen mit Kontext (Datei + Zeile) ausgeben
4. **PII-Werte NICHT im Output anzeigen** — nur Typ + Fundstelle

## Output-Format

```
═══════════════════════════════════════
  PII Scan — [Pfad]
═══════════════════════════════════════
  Dateien gescannt: 142

  ❌ apps/api/tests/test_auth.py:45
     → Email-Adresse im Klartext (Test-Fixture)

  ❌ scripts/plesk-sync.sh:12
     → IP-Adresse hartkodiert

  ⚠️ automation/n8n/workflows/crm-sync-members.json:89
     → Feld "email" ohne Sanitisierung weitergereicht

───────────────────────────────────────
  Ergebnis: 3 PII-Fundstellen
  Empfehlung: Test-Fixtures anonymisieren,
  IP in .env verschieben, n8n-Workflow PII-Filter hinzufuegen
═══════════════════════════════════════
```
