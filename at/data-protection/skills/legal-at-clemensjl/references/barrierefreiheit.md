# Barrierefreiheit (BaFG)

Das österreichische **Barrierefreiheitsgesetz (BaFG)** setzt den European Accessibility Act um und gilt seit **28.06.2025**. Es verpflichtet Unternehmen mit B2C-Onlineangeboten, darunter Onlineshops, zur digitalen Barrierefreiheit nach **WCAG 2.1 Level AA**.

Nicht zu verwechseln mit dem Web-Zugänglichkeits-Gesetz (WZG), das öffentliche Stellen betrifft, und nicht mit dem Behindertengleichstellungsgesetz (BGStG), das unabhängig davon Diskriminierungsschutz gewährt und schon vorher galt.

## Anwendungsbereich

Erfasst sind unter anderem:
- Onlineshops und E-Commerce-Dienstleistungen an Verbraucher
- Bankdienstleistungen für Verbraucher
- E-Books und deren Software
- Telekommunikationsdienste
- Personenverkehrsdienste, elektronische Tickets
- bestimmte Hardwareprodukte mit Interaktionsoberfläche

Reine Firmenpräsentationen ohne Vertragsabschlussmöglichkeit sind vom BaFG nicht erfasst. Das BGStG bleibt daneben anwendbar — Barrierefreiheit ist auch dort ein Thema, nur mit anderem Durchsetzungsmechanismus.

## Kleinstunternehmen

Die Ausnahme gilt **nur für Dienstleistungserbringer**, nicht für Hersteller, Importeure oder Händler von Produkten.

Kleinstunternehmen im Sinn des BaFG: weniger als zehn Personen beschäftigt **und** entweder Jahresumsatz höchstens 2 Mio. Euro **oder** Jahresbilanzsumme höchstens 2 Mio. Euro.

Ein Webshop-Betreiber, der Kleinstunternehmen ist und Dienstleistungen erbringt, muss den Shop nicht barrierefrei gestalten. Werden Produkte hergestellt, importiert oder verkauft, greifen vereinfachte, aber keine vollständig befreienden Pflichten. Die Einordnung ist zu dokumentieren, nicht zu behaupten.

Weitere Ausnahmen: unverhältnismäßige Belastung und grundlegende Veränderung der Wesensart der Dienstleistung. Beide erfordern eine dokumentierte Beurteilung, die auf Verlangen der Marktüberwachungsbehörde vorzulegen ist. Sozialministeriumservice ist zuständige Marktüberwachungsbehörde für digitale Barrierefreiheit.

## Technische Anforderungen — WCAG 2.1 AA in der Praxis

Die vier Prinzipien und die Punkte, an denen Projekte real scheitern:

**Wahrnehmbar**
- Textalternativen für alle nicht-textlichen Inhalte; dekorative Bilder mit leerem alt-Attribut
- Untertitel für Videos, Transkripte für Audio
- Kontrastverhältnis mindestens 4.5:1 für Fließtext, 3:1 für Großtext und für Bedienelemente sowie grafische Objekte
- Inhalt bis 200 Prozent skalierbar ohne Funktionsverlust, Reflow bei 320 CSS-Pixeln Breite
- Information nie allein über Farbe transportieren

**Bedienbar**
- Jede Funktion per Tastatur erreichbar, keine Tastaturfallen
- Sichtbarer Fokusindikator, nicht wegdesignt
- Sprungmarke "Zum Inhalt springen"
- Keine Zeitlimits ohne Verlängerungsmöglichkeit
- Kein Inhalt mit mehr als drei Blitzen pro Sekunde
- Sinnvolle Seitentitel, aussagekräftige Linktexte ("mehr erfahren" allein genügt nicht)

**Verständlich**
- `lang`-Attribut gesetzt, Sprachwechsel im Text ausgezeichnet
- Konsistente Navigation und Benennung
- Formularfelder mit sichtbaren, programmatisch verknüpften Labels
- Fehlermeldungen benennen das Feld und den Fehler im Klartext, nicht nur farblich
- Fehlervermeidung bei rechtsverbindlichen Eingaben: Prüf-, Korrektur- oder Bestätigungsmöglichkeit

**Robust**
- Valides, semantisches HTML
- ARIA nur wo nötig und korrekt; falsches ARIA ist schlechter als keines
- Statusmeldungen über Live-Regions für Screenreader
- Getestet mit mindestens einem Screenreader (NVDA unter Windows, VoiceOver unter macOS/iOS)

Automatische Prüfwerkzeuge (axe, Lighthouse, WAVE) finden erfahrungsgemäß nur einen Teil der Verstöße. Tastaturdurchlauf und Screenreader-Test sind nicht ersetzbar.

## Barrierefreiheitserklärung

Erfasste Dienstleister informieren über die Barrierefreiheit der Dienstleistung. Die Erklärung gehört an eine dauerhaft erreichbare Stelle, üblicherweise im Footer neben Impressum und Datenschutz.

```markdown
<!-- ENTWURF – juristisch nicht freigegeben -->
# Erklärung zur Barrierefreiheit

[[Firma]] ist bemüht, [[Website / App]] im Einklang mit dem
Barrierefreiheitsgesetz (BaFG) barrierefrei zugänglich zu machen.

## Stand der Vereinbarkeit
Diese [[Website / App]] ist mit den Anforderungen der WCAG 2.1 Level AA
[[vollständig / teilweise]] vereinbar.

## Nicht barrierefreie Inhalte
[[Konkrete Auflistung mit Begründung und, soweit vorhanden, geplantem
Behebungszeitpunkt. Falls eine Ausnahme wegen unverhältnismäßiger Belastung
geltend gemacht wird, ist die Beurteilung hier zu benennen.]]

## Erstellung dieser Erklärung
Diese Erklärung wurde am [[Datum]] erstellt. Grundlage war
[[Selbstbewertung / externe Prüfung durch …]].
Letzte Überprüfung: [[Datum]]

## Feedback und Kontakt
Barrieren gemeldet werden können an:
[[Name]], [[E-Mail]], [[Telefon]]
Wir antworten innerhalb von [[Frist]].

## Durchsetzungsverfahren
Führt die Rückmeldung nicht zu einer zufriedenstellenden Lösung, kann eine
Beschwerde bei der Marktüberwachungsbehörde eingebracht werden:
Sozialministeriumservice, www.sozialministeriumservice.at
```

## Prüfpunkte

- [ ] Anwendungsbereich geprüft: B2C-Onlineangebot mit Vertragsabschluss?
- [ ] Kleinstunternehmen-Status dokumentiert (Beschäftigte, Umsatz oder Bilanzsumme)
- [ ] Falls Produkte gehandelt werden: Ausnahme greift nicht, Pflichten geprüft
- [ ] Tastaturdurchlauf der Hauptflows ohne Maus erfolgreich
- [ ] Sichtbarer Fokusindikator auf allen interaktiven Elementen
- [ ] Kontraste gemessen, nicht geschätzt
- [ ] Formulare mit verknüpften Labels und textlichen Fehlermeldungen
- [ ] Screenreader-Test des Bestell- oder Anmeldeflows
- [ ] Reflow bei 320 CSS-Pixeln ohne horizontales Scrollen
- [ ] Barrierefreiheitserklärung veröffentlicht und mit Kontaktweg versehen
- [ ] Bei geltend gemachter Unverhältnismäßigkeit: Beurteilung schriftlich vorhanden
