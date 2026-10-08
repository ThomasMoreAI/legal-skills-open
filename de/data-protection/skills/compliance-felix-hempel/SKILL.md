---
name: compliance-felix-hempel
title: 'Compliance: $ARGUMENTS'
description: DSGVO + Legal Compliance-Check. Datenschutz, Impressum, Cookie-Consent, Tracking, Drittanbieter-Dienste prüfen. Nur Report mit Findings und Handlungsempfehlungen.
author: Felix-Hempel
author_url: https://github.com/Felix-Hempel/claude-team-skills/tree/main/plugins/claromind/skills/compliance
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: data-protection
language: de
---

# Compliance: $ARGUMENTS

## Argumente parsen

**Projekt:** Alias gemäß `## Projekt-Aliase` in der globalen CLAUDE.md auflösen. Falls kein Alias matched, Argument als absoluten Pfad interpretieren.

Wenn kein Projekt erkennbar: Frage nach Projekt.

---

## WARNUNG

Compliance-Fehler sind TEUER. Falsche Negativbefunde (uebersehene Verstoesse) koennen zu
Bussgeldern, Abmahnungen oder Vertrauensverlust fuehren.

**Regeln:**
1. **Lieber ein False Positive zu viel als ein False Negative** — im Zweifel melden
2. **Keine Auto-Fixes bei Legal-Content** — Rechtstexte brauchen juristische Pruefung
3. **Jedes Finding mit konkreter Rechtsgrundlage** — nicht "sollte man machen", sondern "DSGVO Art. X verlangt Y"
4. **Technische Findings praezise** — Datei, Zeile, was genau geladen wird
5. **Firmendaten als Referenz** — Impressum-Pruefung gegen die echten Daten

---

## Step 0: Kontext laden (PFLICHT)

1. Lies die **CLAUDE.md** des Ziel-Projekts. Extrahiere:
   - Tech-Stack, Framework, Hosting
   - Vorhandene Auth/Session-Mechanismen
   - Bekannte Drittanbieter-Integrationen
2. Lies die Firmendaten aus der Projekt-`CLAUDE.md` bzw. dem Impressum:
   ```
   <Firmenname GmbH>
   <Strasse Nr., PLZ Ort>
   Tel.: <Telefon>
   E-Mail: <info@firma.de>
   Web: <https://firma.de>
   Registergericht: <Amtsgericht Ort>
   Handelsregister: <HRB-Nr.>
   USt-IdNr.: <USt-IdNr.>
   Geschaeftsfuehrer: <Geschäftsführer:in>
   Inhaltlich Verantwortlicher gem. § 18 Abs. 2 MStV: <Geschäftsführer:in>
   ```

---

## Schritt 1: Parallel-Scan (5 Bash-Calls gleichzeitig)

**Bash 1 — Impressum + Datenschutz Seiten:**
```bash
set +e
cd {projekt-pfad}
echo "=== IMPRESSUM/DATENSCHUTZ DATEIEN ==="
find src -iname "*impressum*" -o -iname "*imprint*" -o -iname "*datenschutz*" -o -iname "*privacy*" -o -iname "*legal*" | grep -v node_modules | sort
echo "=== FOOTER KOMPONENTE (Links pruefen) ==="
find src -iname "*footer*" | grep -v node_modules | grep -v ".test."
echo "=== IMPRESSUM INHALT ==="
for f in $(find src -iname "*impressum*" -o -iname "*imprint*" | grep -v node_modules); do
  echo "--- $f ---"
  cat "$f"
  echo ""
done
echo "=== DATENSCHUTZ INHALT ==="
for f in $(find src -iname "*datenschutz*" -o -iname "*privacy*" | grep -v node_modules); do
  echo "--- $f ---"
  cat "$f"
  echo ""
done
```

**Bash 2 — Cookie Consent + CMP:**
```bash
set +e
cd {projekt-pfad}
echo "=== COOKIE/CONSENT KOMPONENTEN ==="
find src -iname "*cookie*" -o -iname "*consent*" -o -iname "*banner*" -o -iname "*cmp*" | grep -v node_modules | grep -v ".test." | sort
echo "=== CONSENT IMPLEMENTIERUNG ==="
grep -rn "cookie\|consent\|CookieBanner\|CookieConsent\|consentManager\|cookiebot\|onetrust\|usercentrics\|klaro" src/ --include="*.ts" --include="*.tsx" --include="*.astro" | grep -v node_modules | grep -v ".test."
echo "=== CONSENT VOR TRACKING? (Script-Loading-Reihenfolge) ==="
grep -rn "googletagmanager\|google-analytics\|gtag\|fbq\|hotjar\|segment\|mixpanel\|plausible\|matomo\|umami\|clarity\|_paq" src/ --include="*.ts" --include="*.tsx" --include="*.astro" --include="*.html" | grep -v node_modules
echo "=== SCRIPT TAGS (async/defer + consent-Logik) ==="
grep -rn "<script\|Script " src/ --include="*.astro" --include="*.tsx" --include="*.html" | grep -v node_modules | grep -v ".test."
echo "=== HEAD/LAYOUT (wo werden Scripts eingebunden?) ==="
find src -iname "*head*" -o -iname "*layout*" -o -iname "*base*" | grep -v node_modules | grep -v ".test." | sort
```

**Bash 3 — Drittanbieter-Dienste + externe Ressourcen:**
```bash
set +e
cd {projekt-pfad}
echo "=== EXTERNE URLS (Third-Party-Dienste) ==="
grep -rn "https://" src/ --include="*.ts" --include="*.tsx" --include="*.astro" --include="*.html" --include="*.css" | grep -v node_modules | grep -v ".test." | grep -v "localhost\|127.0.0.1" | grep -oP 'https://[a-zA-Z0-9.-]+' | sort -u
echo "=== GOOGLE SERVICES ==="
grep -rn "google\|googleapis\|gstatic\|youtube\|youtu\.be\|recaptcha" src/ --include="*.ts" --include="*.tsx" --include="*.astro" --include="*.html" | grep -v node_modules | grep -v ".test."
echo "=== FONT LOADING (extern vs lokal) ==="
grep -rn "fonts\.googleapis\|fonts\.gstatic\|typekit\|fontawesome\|font-face.*url" src/ --include="*.ts" --include="*.tsx" --include="*.astro" --include="*.css" --include="*.html" | grep -v node_modules
echo "=== CDN / EXTERNE SCRIPTS ==="
grep -rn "cdn\.\|unpkg\|jsdelivr\|cdnjs\|cloudflare" src/ --include="*.ts" --include="*.tsx" --include="*.astro" --include="*.html" | grep -v node_modules
echo "=== IFRAME EINBETTUNGEN ==="
grep -rn "<iframe\|<Iframe" src/ --include="*.tsx" --include="*.astro" --include="*.html" | grep -v node_modules
echo "=== SOCIAL MEDIA / EMBEDS ==="
grep -rn "facebook\|twitter\|linkedin\|instagram\|tiktok\|pinterest\|whatsapp" src/ --include="*.ts" --include="*.tsx" --include="*.astro" | grep -v node_modules | grep -v ".test."
```

**Bash 4 — Datenspeicherung + Datenfluesse:**
```bash
set +e
cd {projekt-pfad}
echo "=== LOCAL/SESSION STORAGE ==="
grep -rn "localStorage\|sessionStorage" src/ --include="*.ts" --include="*.tsx" | grep -v node_modules | grep -v ".test."
echo "=== COOKIES IM CODE ==="
grep -rn "document\.cookie\|setCookie\|getCookie\|cookie\.\|js-cookie\|cookies\.\|Astro\.cookies\|request\.cookies" src/ --include="*.ts" --include="*.tsx" --include="*.astro" | grep -v node_modules | grep -v ".test."
echo "=== FORMULARE (Datenerhebung) ==="
grep -rn "<form\|<Form\|onSubmit\|handleSubmit" src/ --include="*.tsx" --include="*.astro" | grep -v node_modules | grep -v ".test."
echo "=== E-MAIL VERSAND ==="
grep -rn "sendMail\|nodemailer\|smtp\|@sendgrid\|mailgun\|postmark\|resend\|email.*send" src/ --include="*.ts" | grep -v node_modules | grep -v ".test."
echo "=== DATEI-UPLOADS ==="
grep -rn "upload\|multer\|formidable\|multipart\|<input.*type.*file" src/ --include="*.ts" --include="*.tsx" | grep -v node_modules | grep -v ".test."
echo "=== LOGGING VON USER-DATEN ==="
grep -rn "console\.log.*user\|console\.log.*email\|console\.log.*name\|console\.log.*password\|console\.log.*token\|console\.log.*session" src/ --include="*.ts" --include="*.tsx" | grep -v node_modules | grep -v ".test."
echo "=== DB: PERSONENBEZOGENE DATEN ==="
grep -rn "email\|name\|phone\|address\|geburt\|birth\|password\|salary\|iban\|health\|religion" db/migrations/*.sql 2>/dev/null | grep -v "^--"
```

**Bash 5 — Meta-Tags + SEO + HTTPS:**
```bash
set +e
cd {projekt-pfad}
echo "=== META TAGS ==="
grep -rn "robots\|noindex\|canonical\|og:\|twitter:\|description\|viewport" src/ --include="*.astro" --include="*.tsx" --include="*.html" | grep -v node_modules | head -20
echo "=== HTTP STATT HTTPS ==="
grep -rn "http://" src/ --include="*.ts" --include="*.tsx" --include="*.astro" --include="*.html" --include="*.css" | grep -v node_modules | grep -v ".test." | grep -v "localhost\|127.0.0.1\|http://www.w3.org\|http://schema.org\|http://xmlns" | head -15
echo "=== ROBOTS.TXT ==="
cat public/robots.txt 2>/dev/null || echo "Keine robots.txt gefunden"
echo "=== SITEMAP ==="
find . -iname "sitemap*" -not -path "*/node_modules/*" | head -5
echo "=== SECURITY HEADERS ==="
grep -rn "Content-Security-Policy\|X-Frame-Options\|X-Content-Type\|Strict-Transport\|Referrer-Policy\|Permissions-Policy" src/ --include="*.ts" --include="*.astro" | grep -v node_modules
echo "=== EXTERNAL LINKS (rel=noopener) ==="
grep -rn "target.*_blank\|target=\"_blank" src/ --include="*.tsx" --include="*.astro" | grep -v node_modules | grep -v ".test."
echo "=== NOOPENER CHECK ==="
grep -rn "target.*_blank" src/ --include="*.tsx" --include="*.astro" | grep -v node_modules | grep -v ".test." | grep -v "noopener"
```

---

## Schritt 2: Compliance-relevante Dateien lesen

Lies JEDE Datei die in den folgenden Kategorien auftaucht (KOMPLETT lesen):

1. **Impressum-Seite** — Inhalt vollstaendig erfassen
2. **Datenschutzerklaerung** — Inhalt vollstaendig erfassen
3. **Cookie-Consent-Komponente** — Implementierung verstehen
4. **Footer-Komponente** — Links zu Impressum/Datenschutz pruefen
5. **Head/Layout** — Welche Scripts werden wo geladen
6. **Config** — Tracking-IDs, API-Keys, Feature-Flags

---

## Schritt 3: DSGVO-Checkliste pruefen

### 3.1 Impressum (TMG § 5 / DDG § 5)

Pruefe den Impressum-Inhalt gegen die hinterlegten Firmendaten:

| Pflichtangabe | Vorhanden? | Korrekt? |
|---------------|-----------|----------|
| Firmenname (<Firmenname GmbH>) | | |
| Rechtsform (GmbH) | | |
| Vertretungsberechtigter (<Geschäftsführer:in>) | | |
| Postanschrift (<Strasse Nr., PLZ Ort>) | | |
| Telefon (<Telefon>) | | |
| E-Mail (<info@firma.de>) | | |
| Registergericht (<Amtsgericht Ort>) | | |
| Handelsregisternummer (<HRB-Nr.>) | | |
| USt-IdNr. (<USt-IdNr.>) | | |
| Inhaltlich Verantwortlicher § 18 Abs. 2 MStV | | |
| Von jeder Seite erreichbar (max 2 Klicks) | | |
| Korrekt benannter Link ("Impressum") | | |

### 3.2 Datenschutzerklaerung (DSGVO Art. 13/14)

| Pflichtangabe | Vorhanden? | Korrekt? |
|---------------|-----------|----------|
| Name + Kontakt des Verantwortlichen | | |
| Kontakt Datenschutzbeauftragter (falls >20 MA mit Datenverarbeitung) | | |
| Zwecke der Verarbeitung | | |
| Rechtsgrundlagen (Art. 6 Abs. 1 DSGVO) | | |
| Empfaenger / Kategorien von Empfaengern | | |
| Drittlandtransfers + Garantien (z.B. USA → EU-US DPF?) | | |
| Speicherdauer / Kriterien | | |
| Betroffenenrechte (Art. 15-21 DSGVO) | | |
| Recht auf Beschwerde bei Aufsichtsbehoerde | | |
| Widerrufbarkeit von Einwilligungen | | |
| Automatisierte Entscheidungsfindung (falls zutreffend) | | |
| Von jeder Seite erreichbar (max 2 Klicks) | | |
| Korrekt benannter Link ("Datenschutz" / "Datenschutzerklaerung") | | |

### 3.3 Cookie Consent (ePrivacy + DSGVO)

| Pruefpunkt | Status |
|------------|--------|
| Cookie-Banner vorhanden | |
| Opt-in VOR Tracking-Scripts (kein Script-Loading vor Consent) | |
| Ablehnen-Button gleichwertig sichtbar (gleiche Groesse, Farbe, Position) | |
| Granulare Auswahl moeglich (nicht nur "alles akzeptieren") | |
| Consent-Widerruf jederzeit moeglich | |
| Consent wird gespeichert (nicht bei jedem Besuch erneut) | |
| Technisch notwendige Cookies OHNE Consent erlaubt | |
| Cookie-Kategorien stimmen mit Datenschutzerklaerung ueberein | |

### 3.4 Drittanbieter-Dienste

Fuer JEDEN gefundenen externen Dienst:

| Dienst | Typ | In DSE erwaehnt? | Consent erforderlich? | Consent implementiert? | Drittlandtransfer? |
|--------|-----|-------------------|----------------------|----------------------|-------------------|
| {z.B. Google Fonts} | CDN/Fonts | | Ja (EuGH C-300/21) | | USA → EU-US DPF? |
| {z.B. YouTube} | Embed | | Ja | | USA → EU-US DPF? |

**Bekannte Consent-Pflichten:**
- **Google Fonts (extern geladen):** Consent-pflichtig seit EuGH-Urteil. Alternative: lokal hosten
- **Google Analytics / gtag:** Consent-pflichtig
- **YouTube Embeds:** Consent-pflichtig, youtube-nocookie.com als Alternative
- **Google Maps:** Consent-pflichtig
- **Meta Pixel / fbq:** Consent-pflichtig
- **Alle US-Dienste:** Drittlandtransfer dokumentieren, EU-US DPF oder SCCs pruefen

### 3.5 Technische Datensicherheit

| Pruefpunkt | Status |
|------------|--------|
| Nur HTTPS (kein Mixed Content) | |
| Security Headers gesetzt (CSP, X-Frame-Options, HSTS) | |
| Externe Links mit rel="noopener noreferrer" | |
| Keine Passwort/Token-Logs in console.log | |
| Keine personenbezogenen Daten in localStorage ohne Notwendigkeit | |
| Datenloeschung moeglich (DSGVO Art. 17 — Recht auf Loeschung) | |
| Datenexport moeglich (DSGVO Art. 20 — Datenportabilitaet) | |

---

## Schritt 4: Findings-Report erstellen

**KEINE Fixes durchfuehren. Nur dokumentieren.**

### Severity-Kriterien

| Severity | Bedeutung | Beispiele |
|----------|-----------|-----------|
| **KRITISCH** | Bussgeldrisiko (DSGVO Art. 83: bis 4% Jahresumsatz) | Tracking ohne Consent, fehlende Datenschutzerklaerung, personenbezogene Daten ohne Rechtsgrundlage |
| **HOCH** | Abmahnrisiko (Wettbewerbsrecht, TMG/DDG) | Unvollstaendiges Impressum, Google Fonts extern ohne Consent, fehlender Cookie-Banner |
| **MITTEL** | Compliance-Luecke ohne unmittelbares Risiko | Drittanbieter nicht in DSE erwaehnt, fehlende Speicherdauer-Angabe, Cookie-Kategorien inkonsistent |
| **NIEDRIG** | Best Practice / Haertung | Fehlende Security Headers, noopener bei externen Links, Datenschutzseite auf noindex |

---

## Schritt 5: Zusammenfassung

```
## Compliance-Check: {Projekt} — {Datum}

### Gesamt-Status: {KRITISCH / WARNUNG / OK}

### Impressum
Status: {✅ Vollstaendig / ⚠️ Unvollstaendig / ❌ Fehlt}
{Falls unvollstaendig: Was fehlt}

### Datenschutzerklaerung
Status: {✅ Vollstaendig / ⚠️ Unvollstaendig / ❌ Fehlt}
{Falls unvollstaendig: Was fehlt}

### Cookie Consent
Status: {✅ Korrekt / ⚠️ Maengel / ❌ Fehlt}
{Kernproblem}

### Drittanbieter-Dienste
Gefunden: {N} | In DSE dokumentiert: {N}/{N} | Consent implementiert: {N}/{N}
{Undokumentierte Dienste auflisten}

### Findings

| # | Severity | Bereich | Problem | Rechtsgrundlage | Handlungsempfehlung |
|---|----------|---------|---------|-----------------|---------------------|
| 1 | KRITISCH | ... | ... | DSGVO Art. X | ... |
| 2 | HOCH | ... | ... | TMG § X / DDG § X | ... |

### Naechste Schritte (nach Prioritaet)

1. **SOFORT (diese Woche):** {KRITISCH-Findings}
2. **ZEITNAH (diesen Monat):** {HOCH-Findings}
3. **GEPLANT:** {MITTEL-Findings}
4. **OPTIONAL:** {NIEDRIG-Findings}

### Hinweis

Dieser Check prueft den CODE, nicht die LIVE-Seite. Fuer eine vollstaendige Pruefung:
- Live-Seite im Browser pruefen (Cookie-Banner-Verhalten, Script-Loading-Reihenfolge)
- Datenschutzerklaerung von einem Juristen pruefen lassen
- Cookie-Scan mit externem Tool (z.B. Cookiebot Scanner, Webbkoll)
```
