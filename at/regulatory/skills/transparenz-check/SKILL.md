---
name: transparenz-check
title: Transparenz Check — Oesterreichisches Recht
description: Prueft Impressum, Datenschutzerklaerung und Vereinsangaben auf oesterreichische Rechtskonformitaet (ECG § 5, DSGVO Art. 13/14, VerG)
author: Menschlichkeit-Osterreich
author_url: https://github.com/Menschlichkeit-Osterreich/menschlichkeit-oesterreich/tree/main/.claude/plugins/moe-compliance/skills/transparenz-check
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: at
practice: regulatory
language: de
---

# Transparenz Check — Oesterreichisches Recht

## Zweck

Prueft die oeffentlich sichtbaren Rechtsinformationen der Website auf Vollstaendigkeit und Korrektheit.

## 1. Impressum (ECG § 5 + § 14 UGB)

**Pflichtangaben fuer Vereine:**

| Angabe              | Erforderlich | MOe-Wert                              |
| ------------------- | ------------ | ------------------------------------- |
| Vereinsname         | Ja           | Menschlichkeit Oesterreich            |
| Rechtsform          | Ja           | Verein (ZVR)                          |
| ZVR-Nummer          | Ja           | 1182213083                            |
| Sitz                | Ja           | [Adresse pruefen]                     |
| Kontakt-Email       | Ja           | kontakt@menschlichkeit-oesterreich.at |
| Vertretungsbefugnis | Ja           | Obfrau/Obmann                         |
| Vereinszweck        | Empfohlen    | Demokratische Partizipation           |

**Pruefung:** Impressumsseite lesen und gegen Pflichtliste abgleichen.

## 2. Datenschutzerklaerung (DSGVO Art. 13/14)

**Pflichtinhalte:**

```
□ Name und Kontaktdaten des Verantwortlichen
□ Kontaktdaten Datenschutzbeauftragter (falls vorhanden)
□ Zwecke und Rechtsgrundlage der Verarbeitung
□ Berechtigte Interessen (falls Art. 6 Abs. 1 lit. f)
□ Empfaenger oder Kategorien von Empfaengern
□ Uebermittlung in Drittlaender (inkl. Garantien)
□ Speicherdauer oder Kriterien fuer Festlegung
□ Betroffenenrechte (Auskunft, Berichtigung, Loeschung, Einschraenkung, Widerspruch, Datenportabilitaet)
□ Recht auf Beschwerde bei Aufsichtsbehoerde (oesterr. Datenschutzbehoerde)
□ Ob Bereitstellung gesetzlich/vertraglich vorgeschrieben ist
□ Automatisierte Entscheidungsfindung (falls vorhanden)
□ Cookie-Information (Kategorien, Zwecke, Ablaufzeiten)
□ Drittanbieter-Dienste (Analytics, Payment, Social Media)
```

**Oesterreich-spezifisch:**

- Aufsichtsbehoerde: Oesterreichische Datenschutzbehoerde (dsb.gv.at)
- Beschwerderecht explizit erwaehnen

## 3. Weitere Transparenzpflichten

### Newsletter-Anmeldung

```
□ Hinweis auf Datenschutzerklaerung beim Anmeldeformular
□ Angabe des Newsletter-Dienstleisters (falls extern: Mailchimp, Brevo)
□ Abmeldemoeglickeit erwaehnt
```

### Spendenformular

```
□ Datenschutzhinweis beim Formular
□ Angabe des Zahlungsdienstleisters (Stripe, PayPal)
□ Zweck der Datenerhebung (Spendenbescheinigung, Kontakt)
□ Speicherdauer (steuerrechtlich: 7 Jahre BAO)
```

### Forum/Community

```
□ Nutzungsbedingungen vorhanden
□ Hinweis auf Moderationsrichtlinien
□ Datenschutz fuer Nutzerbeitraege geregelt
```

## Ablauf

Je nach Argument:

- `vollstaendig`: Alle 3 Bereiche pruefen
- `schnell`: Nur Impressum-Pflichtangaben
- `datenschutz`: Nur Datenschutzerklaerung
- `impressum`: Nur Impressum

## Output-Format

```
═══════════════════════════════════════
  Transparenz Check — [Modus]
═══════════════════════════════════════

  Impressum (ECG § 5):
  ✅ Vereinsname
  ✅ ZVR-Nummer: 1182213083
  ✅ Kontakt-Email
  ❌ Sitz/Adresse FEHLT
  ⚠️ Vertretungsbefugnis nicht explizit

  Datenschutz (DSGVO Art. 13):
  ✅ 10/13 Pflichtangaben vorhanden
  ❌ Speicherdauer nicht angegeben
  ❌ Drittlaender-Uebermittlung fehlt
  ⚠️ Cookie-Kategorien unvollstaendig

───────────────────────────────────────
  Ergebnis: 2 kritisch, 2 Warnungen
  Empfehlung: Adresse im Impressum ergaenzen,
  Speicherdauer und Drittlaender-Info in DSE aufnehmen
═══════════════════════════════════════
```
