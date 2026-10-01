# Pre-Launch-Checkliste

Vor dem Livegang durchgehen. Jeder Befund wird mit Paragraf und Fundstelle gemeldet, nicht als allgemeiner Hinweis. Befunde, die technisch prüfbar sind, werden technisch geprüft — nicht anhand der Absicht beurteilt.

## Technische Prüfung zuerst

Diese vier Schritte liefern die Hälfte aller Befunde und dauern zusammen wenige Minuten:

1. Seite in einem frischen Profil laden, Netzwerk-Tab mitlaufen lassen. Alle Fremddomains notieren, die **vor** einer Consent-Entscheidung kontaktiert werden.
2. Application-Tab: alle Cookies, LocalStorage- und IndexedDB-Einträge vor der Entscheidung erfassen.
3. Volltextsuche über das ganze Projekt inklusive Shop-Systemtexte und E-Mail-Templates nach: `odr`, `Streitbeilegungsplattform`, `TMG`, `RStV`, `BDSG`, `Widerrufsrecht`, `Amtsgericht`, `Landgericht`, `Ihr Team von`.
4. Bestellflow einmal mit Tastatur durchlaufen, ohne Maus.

## Impressum und Offenlegung

- [ ] Von jeder Seite in maximal zwei Klicks, Link heißt "Impressum"
- [ ] Ohne Consent und ohne Login erreichbar
- [ ] Name/Firma, geografische Anschrift, E-Mail plus zweiter Kontaktkanal (§ 5 Abs 1 Z 1–3 ECG)
- [ ] Firmenbuchnummer und Firmenbuchgericht, falls eingetragen (Z 4, § 14 UGB)
- [ ] Aufsichtsbehörde, falls die Tätigkeit ihr unterliegt (Z 5)
- [ ] Kammer, Berufsbezeichnung, Verleihungsstaat, anwendbare Vorschriften mit Zugang (Z 6)
- [ ] UID, falls vorhanden (Z 7)
- [ ] Gewerbewortlaut laut GISA, GISA-Zahl, Gewerbebehörde (§ 63 GewO)
- [ ] Medieninhaber und Herausgeber mit Anschrift (§ 24 Abs 3 MedienG)
- [ ] Offenlegung: verkürzt nach § 25 Abs 5 oder voll nach Abs 2–4, Wahl begründet
- [ ] Bei voller Offenlegung: Beteiligungsverhältnisse inkl. stiller Beteiligungen, Blattlinie
- [ ] DSA-Kontaktstellen, falls Vermittlungsdienst

## Datenschutz

- [ ] Datenschutzerklärung vorhanden, ohne Consent erreichbar
- [ ] Jede Verarbeitung mit Zweck, Rechtsgrundlage, Empfängern, Speicherdauer
- [ ] Berechtigte Interessen konkret benannt, nicht floskelhaft
- [ ] Alle tatsächlich geladenen Dienste aufgeführt — gegen die Netzwerkanalyse abgeglichen
- [ ] Drittlandübermittlungen einzeln mit Grundlage
- [ ] Betroffenenrechte vollständig, Widerrufshinweis vorhanden
- [ ] Österreichische Datenschutzbehörde als Aufsichtsbehörde, korrekte Anschrift
- [ ] Bei Zielgruppe unter 14: § 4 Abs 4 DSG umgesetzt, Elterneinwilligung, kindgerechte Fassung
- [ ] Verarbeitungsverzeichnis, AVV, TOM, Breach-Prozess intern vorhanden (siehe `dsgvo-intern.md`)

## Cookies und Tracking

- [ ] Vor der Entscheidung feuert kein Tracking-Request
- [ ] "Ablehnen" auf erster Ebene, optisch gleichwertig zu "Akzeptieren"
- [ ] Keine vorangekreuzten Kategorien
- [ ] Granulare Auswahl je Zweck möglich
- [ ] Widerruf so einfach wie Erteilung, Link dauerhaft im Footer
- [ ] Cookie-Tabelle vollständig, technisch verifiziert
- [ ] Consent-Protokoll mit Zeitstempel und Bannerversion
- [ ] Google Fonts lokal ausgeliefert oder hinter Consent
- [ ] Maps, Video, Captcha hinter Consent oder mit Klick-zum-Laden

## Shop und Fernabsatz (falls Verkauf)

- [ ] Bestellbutton "zahlungspflichtig bestellen" oder gleichwertig eindeutig (§ 8 FAGG)
- [ ] Bestellübersicht unmittelbar über dem Button
- [ ] Gesamtpreis inkl. Steuern, Versandkosten getrennt und vorab erkennbar (§ 5 Abs 2 ECG, PrAG)
- [ ] Lieferzeitraum konkret
- [ ] Lieferbeschränkungen und Zahlungsmittel zu Beginn des Bestellvorgangs
- [ ] Keine vorangekreuzten Zusatzleistungen (§ 6c KSchG)
- [ ] Korrekturmöglichkeit für Eingabefehler (§§ 9–11 ECG)
- [ ] Vertragsbestätigung per E-Mail auf dauerhaftem Datenträger (§ 7 Abs 3 FAGG)
- [ ] Alle Pflichtinformationen des § 4 Abs 1 FAGG abgedeckt
- [ ] Rabattaussagen mit niedrigstem Preis der letzten 30 Tage belegt

## Rücktritt

- [ ] Belehrung vorhanden, Begriff "Rücktritt" statt "Widerruf"
- [ ] Fristbeginn passend zum Vertragstyp (§ 11 Abs 2 FAGG)
- [ ] Muster-Widerrufsformular nach Anhang I Teil B bereitgestellt und speicherbar
- [ ] Kontaktdaten in der Belehrung vollständig
- [ ] Rücksendekosten geregelt und erwähnt, falls der Verbraucher sie tragen soll
- [ ] Bei digitalen Inhalten mit Sofortzugang: beide Bestätigungen nach § 18 Abs 1 Z 11 als getrennte, nicht vorangekreuzte Checkboxen, mit Zeitstempel gespeichert
- [ ] Keine erfundenen Einschränkungen ("nur ungeöffnet", "nur Originalverpackung")
- [ ] Rücktrittsfunktion nach § 13a FAGG gebaut oder terminiert — **Pflicht ab 01.10.2026 für Verträge, die nach dem 30.09.2026 geschlossen werden** (§ 20 Abs 5 FAGG idF BGBl I 59/2026). Eigene Widerrufsseite, Footer-Link, ohne Login erreichbar, Bestätigungsschaltfläche ausschließlich mit „Widerruf bestätigen" beschriftet, Empfangsbestätigung auf dauerhaftem Datenträger mit Inhalt, Datum und Uhrzeit
- [ ] Verkauf auch nach DE oder FR? Dort gilt die Funktion bereits seit 19.06.2026 — dann nach dem früheren Datum bauen
- [ ] Harmonisierte Gewährleistungs-Mitteilung (Anhang II FAGG) und Haltbarkeitsgarantie-Kennzeichnung (Anhang III FAGG) ab **27.09.2026** eingebaut, § 5a Abs 1 Z 5 und Z 5a KSchG
- [ ] Kein Kündigungsbutton nach deutschem § 312k BGB behauptet oder eingebaut

## Gewährleistung

- [ ] Gewährleistung und Garantie sprachlich sauber getrennt
- [ ] Keine Verkürzung bei Neuware gegenüber Verbrauchern
- [ ] Aktualisierungspflicht adressiert, Zeitraum benannt
- [ ] Bei Garantie: Erklärung auf dauerhaftem Datenträger, Hinweis auf unberührte Gewährleistung

## Marketing

- [ ] Newsletter: getrennte, nicht vorangekreuzte Einwilligung mit konkretem Zweck
- [ ] Double-Opt-In aktiv, Bestätigungsmail werbefrei
- [ ] Einwilligungsnachweis mit Zeitstempel, IP, Textversion
- [ ] Abmeldelink in jeder Aussendung, ein Klick
- [ ] Bestandskundenwerbung: alle drei Voraussetzungen des § 174 Abs 4 TKG 2021 dokumentiert
- [ ] ECG-Liste vor Versand abgeglichen
- [ ] Impressum in Aussendungen
- [ ] Bewertungen: Echtheitsprüfung offengelegt
- [ ] Affiliate- und Kooperationsinhalte gekennzeichnet

## Barrierefreiheit

- [ ] Anwendungsbereich BaFG geprüft
- [ ] Kleinstunternehmen-Status dokumentiert, falls in Anspruch genommen
- [ ] Tastaturdurchlauf der Hauptflows erfolgreich, Fokus sichtbar
- [ ] Kontraste gemessen
- [ ] Formulare mit verknüpften Labels, textliche Fehlermeldungen
- [ ] Screenreader-Test des Bestell- oder Anmeldeflows
- [ ] Barrierefreiheitserklärung veröffentlicht, falls erfasst

## Plattform

- [ ] DSA-Einordnung dokumentiert
- [ ] Meldeweg für rechtswidrige Inhalte, falls Hosting fremder Inhalte
- [ ] Begründungspflicht bei Entfernung umgesetzt
- [ ] Moderationsregeln in den AGB offengelegt

## Streitbeilegung und Sonstiges

- [ ] Kein ODR-Link und keine Erwähnung der EU-Streitbeilegungsplattform, projektweit
- [ ] Schlichtungsstelle genannt, falls Teilnahmeverpflichtung besteht
- [ ] Bildrechte und Lizenznachweise dokumentiert (UrhG)
- [ ] Fremde Marken und Logos nur mit Berechtigung verwendet
- [ ] Keine deutschen Paragrafen und keine deutschen Behörden im Text
- [ ] Alle `[[…]]`-Platzhalter aufgelöst oder ausdrücklich als offen gemeldet
- [ ] Entwurfs-Marker noch vorhanden, solange keine juristische Freigabe erfolgt ist

## Ergebnisformat

Befunde als Tabelle ausgeben, schwerwiegendste zuerst:

| Schwere | Fundstelle | Norm | Befund | Behebung |
|---|---|---|---|---|
| kritisch / hoch / mittel | Datei:Zeile oder URL | § | was fehlt oder falsch ist | konkreter Schritt |

**Kritisch** heißt: Abmahnrisiko, Verwaltungsstrafe oder Unwirksamkeit des Vertrags. Dazu zählen fehlendes Impressum, Tracking ohne Einwilligung, falsch beschrifteter Bestellbutton, fehlende Rücktrittsbelehrung.
