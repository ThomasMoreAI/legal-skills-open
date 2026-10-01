# Datenschutzerklärung

Rechtsgrundlage sind Art 13 und 14 DSGVO, ergänzt um das österreichische DSG. Die Erklärung ist eine Informationspflicht, kein Vertrag — sie holt keine Einwilligung ein, sie informiert. Einwilligungen werden getrennt eingeholt (Cookie-Banner, Newsletter-Checkbox).

Pflicht besteht, sobald überhaupt personenbezogene Daten verarbeitet werden. Server-Logfiles mit IP-Adresse reichen aus. Es gibt keine Website ohne Datenschutzerklärung.

## Pflichtinhalte nach Art 13 DSGVO (Erhebung beim Betroffenen)

1. Name und Kontaktdaten des Verantwortlichen, gegebenenfalls des Vertreters
2. Kontaktdaten des Datenschutzbeauftragten, falls bestellt
3. **Zwecke jeder Verarbeitung und die jeweilige Rechtsgrundlage**
4. Bei Art 6 Abs 1 lit f: die konkreten berechtigten Interessen, benannt, nicht floskelhaft
5. Empfänger oder Kategorien von Empfängern
6. Absicht der Drittlandübermittlung samt Grundlage (Angemessenheitsbeschluss oder geeignete Garantien) und Hinweis, wo eine Kopie der Garantien erhältlich ist
7. Speicherdauer oder Kriterien für ihre Festlegung
8. Betroffenenrechte: Auskunft, Berichtigung, Löschung, Einschränkung, Datenübertragbarkeit, Widerspruch
9. Bei Einwilligung: Widerrufsrecht mit Wirkung für die Zukunft
10. Beschwerderecht bei der Aufsichtsbehörde
11. Ob die Bereitstellung gesetzlich oder vertraglich vorgeschrieben ist, ob sie für einen Vertragsabschluss erforderlich ist und welche Folgen die Nichtbereitstellung hat
12. Bestehen automatisierter Entscheidungsfindung einschließlich Profiling, aussagekräftige Informationen über die Logik sowie Tragweite und Folgen

Bei Daten, die nicht beim Betroffenen erhoben wurden, gilt zusätzlich Art 14: Kategorien der Daten und Quelle, Information binnen angemessener Frist, längstens einem Monat.

## Aufsichtsbehörde

Österreichische Datenschutzbehörde, Barichgasse 40–42, 1030 Wien, dsb@dsb.gv.at, dsb.gv.at. Diese Adresse gehört in jede Datenschutzerklärung. Nicht die deutsche Landesbehörde nennen.

## Österreichische Abweichungen

**§ 4 Abs 4 DSG — Einwilligungsalter 14.** Werden Dienste der Informationsgesellschaft einem Kind direkt angeboten, ist dessen Einwilligung nach Art 6 Abs 1 lit a DSGVO rechtmäßig, wenn das Kind das 14. Lebensjahr vollendet hat. Darunter muss der gesetzliche Vertreter einwilligen. Art 8 DSGVO sähe 16 vor; Österreich hat die Öffnungsklausel genutzt.

Praktische Folge für Angebote mit Kindern als Zielgruppe:
- Altersabfrage im Anmeldeprozess, nicht als reines Häkchen
- Unter 14: nachvollziehbarer Prozess zur Einholung der Elterneinwilligung, dokumentiert
- Sprache der Erklärung an die Zielgruppe anpassen — Art 12 Abs 1 DSGVO verlangt klare, einfache Sprache, insbesondere bei Kindern. Zweite, kindgerechte Fassung zusätzlich zur juristischen Fassung ist der übliche Weg.
- Kein Profiling zu Werbezwecken gegenüber Kindern

**§ 1 DSG — Grundrecht auf Datenschutz.** Verfassungsrang, gilt auch für juristische Personen. Praktisch relevant bei Interessenabwägungen.

**§ 12 f DSG — Bildverarbeitung.** Eigene Regeln für Videoüberwachung, inklusive Kennzeichnungspflicht und Protokollierung. Betrifft physische Standorte, nicht Websites.

**§ 24 DSG — Beschwerde.** Beschwerdeverfahren vor der DSB.

**§ 62 DSG — Strafbestimmungen.** Verwaltungsstrafen zusätzlich zum Bußgeldregime der DSGVO.

## Typische Verarbeitungen und ihre Rechtsgrundlage

| Verarbeitung | Rechtsgrundlage | Anmerkung |
|---|---|---|
| Server-Logfiles, IT-Sicherheit | Art 6 Abs 1 lit f | Berechtigtes Interesse konkret benennen: Betrieb, Sicherheit, Missbrauchsabwehr |
| Kontaktformular | lit b oder lit f | lit b bei Vertragsanbahnung |
| Kundenkonto | lit b | |
| Bestellabwicklung | lit b | |
| Rechnungsaufbewahrung | lit c | § 132 BAO, 7 Jahre |
| Newsletter | lit a | Einwilligung, Double-Opt-In, siehe `marketing.md` |
| Bestandskundenwerbung per E-Mail | lit f, TKG § 174 Abs 4 | Enge Voraussetzungen, siehe `marketing.md` |
| Analytics, Marketing-Pixel | lit a | Zugriff aufs Endgerät zusätzlich nach TKG § 165 Abs 3 |
| Betrugsprävention | lit f | |
| Bewerbungen | lit b, § 4 DSG | Aufbewahrung nach Absage begrenzen |

Speicherfristen, die praktisch immer auftauchen: Rechnungen und Belege 7 Jahre (§ 132 BAO), Aufzeichnungen mit Grundstücksbezug bis 22 Jahre, allgemeine zivilrechtliche Verjährung 3 Jahre bzw. 30 Jahre bei Ausnahmen.

## Drittlandübermittlung

Jeder US-Dienst ist eine Drittlandübermittlung, auch wenn ein EU-Rechenzentrum gewählt wurde, sobald Zugriff aus den USA möglich ist. Anzugeben sind: Empfänger, Zielland, Grundlage. Für die USA kommt der Angemessenheitsbeschluss zum EU-US Data Privacy Framework nur in Betracht, wenn der konkrete Anbieter zertifiziert ist — das ist zu prüfen und nicht zu unterstellen. Sonst Standardvertragsklauseln plus Transfer Impact Assessment.

**DPF allein trägt seit 29.06.2026 nicht mehr.** An diesem Tag entschied der US Supreme Court in *Trump v. Slaughter*, dass der Kündigungsschutz der FTC-Commissioner verfassungswidrig ist — die FTC kann nicht unabhängig sein. Der Durchführungsbeschluss (EU) 2023/1795 stützt sich auf genau diese Unabhängigkeit: die FTC ist die Aufsichts- und Durchsetzungsbehörde für die DPF-Grundsätze, und unabhängige Aufsicht ist Tatbestandsmerkmal des Art 45 Abs 2 lit b DSGVO. Stand 05.08.2026: noyb hat am 29.06.2026 die Aufhebung beantragt und eine Nichtigkeitsklage angekündigt (nicht bestätigt eingebracht), der EDSA hat am 31.07.2026 die Kommission zur Prüfung aufgefordert, die Kommission hat **nicht** reagiert.

Daraus folgt für die Praxis, nicht für den Text der Erklärung:

- Der Beschluss **gilt** bis zur Aufhebung durch die Kommission oder Nichtigerklärung durch den EuGH. „Das DPF ist gefallen" ist falsch und in einer Datenschutzerklärung ein eigener Fehler.
- Wer sich allein auf DPF stützt, braucht einen **dokumentierten SCC-Fallback** nach Art 46 Abs 2 lit c DSGVO plus Transfer Impact Assessment. Das TIA muss Aufsicht und Rechtsschutz ansprechen — genau die Punkte, die das Urteil schwächt.
- In der Erklärung selbst bleibt es bei Empfänger, Zielland, Grundlage. Die Fallback-Konstruktion gehört ins Verarbeitungsverzeichnis und in den Auftragsverarbeitungsvertrag, nicht in den veröffentlichten Text.

Häufige Kandidaten: Google (Analytics, Fonts, Maps, reCAPTCHA), Meta, Microsoft, Amazon Web Services, Cloudflare, Stripe, Mailchimp, OpenAI, Anthropic, Vercel, Supabase.

## Struktur der Erklärung

```markdown
<!-- ENTWURF – juristisch nicht freigegeben -->
# Datenschutzerklärung

## 1. Verantwortlicher und Kontakt
## 2. Datenschutzbeauftragter            (falls bestellt)
## 3. Überblick über die Verarbeitungen
## 4. Ihre Rechte
## 5. Hosting und Server-Logfiles
## 6. Cookies und ähnliche Technologien   (verweist auf Cookie-Einstellungen)
## 7. Kontaktaufnahme
## 8. Kundenkonto und Bestellabwicklung
## 9. Zahlungsdienstleister
## 10. Newsletter und Direktwerbung
## 11. Webanalyse und Reichweitenmessung
## 12. Eingebundene Dienste Dritter       (Fonts, Maps, Video, Captcha, CDN)
## 13. Social-Media-Präsenzen
## 14. Bewerbungen                        (falls zutreffend)
## 15. Daten von Kindern                  (falls Zielgruppe unter 14)
## 16. Empfänger und Auftragsverarbeiter
## 17. Übermittlung in Drittländer
## 18. Speicherdauer
## 19. Erforderlichkeit der Bereitstellung
## 20. Automatisierte Entscheidungsfindung
## 21. Beschwerderecht bei der Datenschutzbehörde
## 22. Änderungen dieser Erklärung
```

Jeder Abschnitt zu einer konkreten Verarbeitung enthält vier Angaben in dieser Reihenfolge: **welche Daten, wozu, auf welcher Rechtsgrundlage, wie lange.** Fehlt eine davon, ist der Abschnitt unvollständig.

## Textbaustein Betroffenenrechte

```markdown
## Ihre Rechte

Ihnen stehen gegenüber uns folgende Rechte hinsichtlich der Sie betreffenden
personenbezogenen Daten zu:

- Auskunft (Art 15 DSGVO)
- Berichtigung (Art 16 DSGVO)
- Löschung (Art 17 DSGVO)
- Einschränkung der Verarbeitung (Art 18 DSGVO)
- Datenübertragbarkeit (Art 20 DSGVO)
- Widerspruch gegen Verarbeitungen auf Grundlage berechtigter Interessen
  (Art 21 DSGVO); bei Direktwerbung besteht dieses Widerspruchsrecht
  uneingeschränkt

Haben Sie in eine Verarbeitung eingewilligt, können Sie diese Einwilligung
jederzeit mit Wirkung für die Zukunft widerrufen. Die Rechtmäßigkeit der bis
zum Widerruf erfolgten Verarbeitung bleibt unberührt.

Zur Ausübung genügt eine Nachricht an [[E-Mail]].

Unabhängig davon können Sie sich bei einer Aufsichtsbehörde beschweren.
Zuständig ist in Österreich:

Österreichische Datenschutzbehörde
Barichgasse 40–42, 1030 Wien
dsb@dsb.gv.at, www.dsb.gv.at
```

## Prüfpunkte

- [ ] Jede Verarbeitung hat Zweck, Rechtsgrundlage, Empfänger, Speicherdauer
- [ ] Bei lit f ist das berechtigte Interesse konkret benannt, nicht "Verbesserung des Angebots"
- [ ] Alle tatsächlich eingebundenen Dienste sind aufgeführt — Netzwerkanalyse der Seite gegen die Erklärung prüfen, nicht die Erklärung gegen die Absicht
- [ ] Drittlandübermittlungen einzeln benannt mit Grundlage
- [ ] Österreichische DSB als Aufsichtsbehörde
- [ ] Widerrufshinweis bei jeder Einwilligung
- [ ] Bei Kinderzielgruppe: § 4 Abs 4 DSG adressiert, kindgerechte Fassung vorhanden
- [ ] Keine Einwilligungsformulierungen ("Mit der Nutzung erklären Sie sich einverstanden") — das ist keine Einwilligung
- [ ] Kein Verweis auf BDSG oder deutsche Landesbehörden
- [ ] Datum der letzten Änderung
