# Cookies, Tracking, Consent

Zwei Ebenen, die getrennt zu prüfen sind:

1. **Zugriff auf das Endgerät** — § 165 Abs 3 TKG 2021 (Umsetzung der ePrivacy-Richtlinie 2002/58/EG). Erfasst jedes Speichern von Informationen auf dem Endgerät und jeden Zugriff darauf, unabhängig davon, ob dabei personenbezogene Daten anfallen. Cookies, LocalStorage, SessionStorage, IndexedDB, Fingerprinting, Pixel, SDK-Kennungen.
2. **Verarbeitung der so erlangten Daten** — DSGVO. Braucht eine eigene Rechtsgrundlage, meist Art 6 Abs 1 lit a.

Beide Ebenen müssen erfüllt sein. Eine Einwilligung nach TKG ersetzt nicht die DSGVO-Grundlage und umgekehrt.

## Einwilligungspflicht und Ausnahme

Einwilligung ist erforderlich, sofern keine Ausnahme greift. Ausgenommen sind Zugriffe, die unbedingt erforderlich sind, um einen vom Nutzer ausdrücklich gewünschten Dienst zu erbringen, sowie solche, die allein der Übertragung einer Nachricht dienen.

**Ohne Einwilligung zulässig (technisch notwendig):**
- Session-ID zur Aufrechterhaltung der Anmeldung
- Warenkorb
- Sprach- und Währungsauswahl, sofern vom Nutzer gesetzt
- Lastverteilung
- Sicherheits-Token, CSRF-Schutz
- Speicherung der Cookie-Entscheidung selbst
- Barrierefreiheits-Einstellungen des Nutzers

**Einwilligungspflichtig:**
- Webanalyse jeder Art, auch anonymisiert, auch selbst gehostet, sobald sie nicht zur Diensterbringung nötig ist
- Conversion- und Retargeting-Pixel
- A/B-Testing-Tools
- Eingebundene Karten, Videos, Schriftarten und Icons, die von einem Fremdserver geladen werden
- Chat-Widgets, sofern nicht vom Nutzer aktiv geöffnet
- Captcha-Dienste Dritter, wenn Alternativen bestehen
- Social-Media-Plugins und Share-Buttons mit Serverkontakt

Die Datenschutzbehörde stellt in ihren Cookie-FAQ klar: für technisch nicht notwendige Cookies ist eine Einwilligung einzuholen, und solche Cookies dürfen nicht vorab gesetzt werden.

## Anforderungen an das Banner

- **Kein Skript vor der Entscheidung.** Kein Tracking-Request darf feuern, bevor der Nutzer aktiv gewählt hat. Das schließt Preloading, Prefetch und DNS-Prefetch auf Trackingdomains ein.
- **"Ablehnen" auf der ersten Ebene, gleich prominent wie "Akzeptieren".** Gleiche Größe, gleicher Kontrast, gleiche Position im Fokusfluss. "Ablehnen" darf nicht als Textlink neben einem farbigen Button stehen.
- **Granular.** Zustimmung je Zweckkategorie muss möglich sein, nicht nur alles oder nichts.
- **Keine Vorauswahl.** Schalter für nicht notwendige Kategorien stehen auf aus.
- **Freiwillig.** Kein Nachteil bei Ablehnung. Cookie-Wall nur als bezahlte Alternative und nur nach eigener Prüfung — rechtlich umstritten, im Zweifel nicht bauen.
- **Widerrufbar, so einfach wie die Erteilung.** Dauerhaft erreichbarer Link "Cookie-Einstellungen" im Footer, der das Banner erneut öffnet.
- **Informiert.** Vor der Entscheidung müssen Zwecke, eingesetzte Dienste, Empfänger und Speicherdauer zugänglich sein.
- **Kein Dark Pattern.** Keine Ermüdungsschleifen, kein wiederholtes Wiederanzeigen nach Ablehnung innerhalb kurzer Zeit, keine irreführende Beschriftung.
- **Nachweisbar.** Consent-Protokoll mit Zeitstempel, Version des Banners, gewählten Kategorien und Consent-String. Die Beweislast trägt der Verantwortliche.

## Cookie-Tabelle

Jede Website braucht eine vollständige Aufstellung. Ermittlung erfolgt technisch, nicht aus der Erinnerung: Seite mit leerem Profil laden, Netzwerk- und Application-Tab auswerten, alle Domains und Speichereinträge erfassen, dann mit Einwilligung wiederholen.

| Name | Anbieter | Zweck | Kategorie | Speicherdauer | Drittland |
|---|---|---|---|---|---|
| `[[name]]` | `[[Anbieter]]` | `[[Zweck]]` | notwendig / Statistik / Marketing | `[[Dauer]]` | ja/nein + Grundlage |

## Häufige Stolpersteine

| Fall | Bewertung |
|---|---|
| Google Fonts vom Google-Server | Endgerätezugriff und IP-Übermittlung; entweder Einwilligung oder Fonts lokal ausliefern. Lokal ist der einfachere Weg. |
| Google Maps iframe | Erst nach Einwilligung laden, davor Platzhalter mit Klick-zum-Laden |
| YouTube-Embed | `youtube-nocookie.com` verringert das Problem, beseitigt es nicht; Zwei-Klick-Lösung |
| reCAPTCHA | Einwilligungspflichtig; Alternativen prüfen (hCaptcha mit EU-Hosting, Honeypot, Rechenaufgabe) |
| Self-hosted Analytics ohne Cookies | Nicht automatisch frei — es kommt darauf an, ob auf das Endgerät zugegriffen wird und ob personenbezogene Daten verarbeitet werden. Einzelfallprüfung, nicht pauschal freigeben. |
| Consent-Banner nach Impressum | Impressum und Datenschutzerklärung müssen ohne Zustimmung erreichbar sein; Banner darf sie nicht blockieren |
| Server-seitiges Tagging | Verlagert die Technik, nicht die Rechtslage |

## Textbaustein für die Datenschutzerklärung

```markdown
## Cookies und ähnliche Technologien

Wir setzen auf dieser Website Cookies und vergleichbare Technologien ein.
Unbedingt erforderliche Technologien nutzen wir auf Grundlage von
§ 165 Abs 3 TKG 2021 ohne Einwilligung, da sie zur Erbringung des von Ihnen
ausdrücklich gewünschten Dienstes notwendig sind.

Alle übrigen Technologien setzen wir nur ein, wenn Sie eingewilligt haben
(§ 165 Abs 3 TKG 2021 in Verbindung mit Art 6 Abs 1 lit a DSGVO). Sie können
Ihre Einwilligung jederzeit mit Wirkung für die Zukunft widerrufen, indem Sie
die [Cookie-Einstellungen](#cookie-settings) öffnen und Ihre Auswahl ändern.

Eine vollständige Aufstellung der eingesetzten Technologien mit Anbieter,
Zweck, Kategorie und Speicherdauer finden Sie in den Cookie-Einstellungen.
```

## Prüfpunkte

- [ ] Mit leerem Profil geladen und Netzwerkverkehr geprüft: vor der Entscheidung nur eigene Domain und notwendige Dienste
- [ ] "Ablehnen" auf erster Ebene, optisch gleichwertig
- [ ] Keine vorangekreuzten Kategorien
- [ ] Widerrufslink dauerhaft im Footer, öffnet das Banner erneut
- [ ] Impressum und Datenschutzerklärung ohne Zustimmung erreichbar
- [ ] Cookie-Tabelle vollständig und technisch verifiziert
- [ ] Consent-Protokollierung aktiv, Aufbewahrung geregelt
- [ ] Banner-Version im Protokoll, damit spätere Änderungen zuordenbar sind
- [ ] Google Fonts lokal oder hinter Consent
