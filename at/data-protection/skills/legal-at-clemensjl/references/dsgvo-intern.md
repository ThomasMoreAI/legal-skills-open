# DSGVO — interne Pflichten

Diese Dokumente gehören nicht auf die Website. Sie werden intern geführt und auf Verlangen der Datenschutzbehörde vorgelegt. Wer nur eine Datenschutzerklärung hat, ist nicht compliant — die Erklärung ist die Außenseite, hier liegt die Substanz.

## Art 30 — Verzeichnis von Verarbeitungstätigkeiten

Pflicht für praktisch jedes Unternehmen. Die Erleichterung für Betriebe unter 250 Beschäftigten greift nur, wenn die Verarbeitung nicht risikobehaftet, nicht regelmäßig und ohne besondere Kategorien erfolgt — bei laufendem Kundenbetrieb ist das nie erfüllt.

Je Verarbeitungstätigkeit zu dokumentieren:

- Name und Kontaktdaten des Verantwortlichen, gegebenenfalls des gemeinsam Verantwortlichen, des Vertreters, des Datenschutzbeauftragten
- Zwecke der Verarbeitung
- Kategorien betroffener Personen
- Kategorien personenbezogener Daten
- Kategorien von Empfängern, einschließlich Empfängern in Drittländern
- gegebenenfalls Drittlandübermittlungen samt Dokumentation geeigneter Garantien
- vorgesehene Löschfristen je Kategorie
- allgemeine Beschreibung der technischen und organisatorischen Maßnahmen

Zusätzlich sinnvoll, auch wenn nicht ausdrücklich gefordert: Rechtsgrundlage je Zweck. Ohne sie ist das Verzeichnis für Auskunftsersuchen und Löschprüfungen nutzlos.

Typische Einträge eines kleinen Online-Betriebs: Website-Betrieb und Logfiles, Kontaktanfragen, Kundenkonto, Bestellabwicklung, Zahlungsabwicklung, Versand, Buchhaltung, Newsletter, Support, Bewerbungen, Analytics.

## Art 28 — Auftragsverarbeitung

Jeder Dienstleister, der in fremdem Auftrag personenbezogene Daten verarbeitet, braucht einen Auftragsverarbeitungsvertrag. Ohne AVV ist die Weitergabe rechtswidrig, unabhängig davon, wie sicher der Dienst technisch ist.

Betroffen sind in der Regel: Hosting, Cloud-Speicher, Mailversand, CRM, Analytics, Support-Tools, Backup, Zahlungsdienstleister (teils als eigene Verantwortliche), Buchhaltungssoftware, KI-Dienste, Entwicklungs- und Wartungsdienstleister mit Datenzugriff.

Mindestinhalte nach Art 28 Abs 3: Gegenstand, Dauer, Art und Zweck, Datenarten, Kategorien betroffener Personen, Weisungsbindung, Vertraulichkeit, Sicherheitsmaßnahmen nach Art 32, Regelungen zu Unterauftragsverarbeitern, Unterstützung bei Betroffenenrechten, Unterstützung bei Art 32 bis 36, Löschung oder Rückgabe nach Vertragsende, Nachweis- und Auditrechte.

Praxis: Liste aller Dienstleister führen, AVV-Status je Eintrag, Ablageort des unterschriebenen Dokuments, Datum der letzten Prüfung, Unterauftragsverarbeiter-Liste des Anbieters beobachten.

## Art 32 — Technische und organisatorische Maßnahmen

Zu dokumentieren, nicht nur zu haben. Struktur, die sich bewährt hat:

- Zutrittskontrolle (physisch)
- Zugangskontrolle (Systemzugang, Authentifizierung, MFA)
- Zugriffskontrolle (Berechtigungskonzept, Least Privilege)
- Weitergabekontrolle (Transportverschlüsselung, TLS-Konfiguration)
- Eingabekontrolle (Protokollierung)
- Verfügbarkeitskontrolle (Backup, Wiederherstellungstests, Recovery-Zeiten)
- Trennungskontrolle (Mandanten, Umgebungen, Test- gegen Produktivdaten)
- Pseudonymisierung und Verschlüsselung im Ruhezustand
- Verfahren zur regelmäßigen Überprüfung und Bewertung

Ein häufiger Befund in kleinen Projekten: Produktivdaten in Entwicklungsumgebungen. Das ist ein TOM-Verstoß und lässt sich nicht durch eine Formulierung in der Datenschutzerklärung heilen.

## Art 33 und 34 — Datenschutzverletzungen

- Meldung an die Datenschutzbehörde **binnen 72 Stunden** ab Kenntnis, außer die Verletzung führt voraussichtlich nicht zu einem Risiko für Rechte und Freiheiten
- Bei voraussichtlich hohem Risiko zusätzlich Benachrichtigung der betroffenen Personen unverzüglich und in klarer Sprache
- **Dokumentationspflicht für jede Verletzung**, auch für die nicht gemeldeten, samt Begründung der Nichtmeldung

Vorbereitet gehört: Wer entscheidet, wer meldet, an welche Adresse, welche Angaben werden erhoben, wo wird protokolliert. 72 Stunden reichen nicht, um diesen Prozess erst zu erfinden. Meldeweg: Datenschutzbehörde, dsb.gv.at.

## Art 35 — Datenschutz-Folgenabschätzung

Erforderlich bei voraussichtlich hohem Risiko, insbesondere bei systematischer umfangreicher Bewertung persönlicher Aspekte einschließlich Profiling, umfangreicher Verarbeitung besonderer Kategorien oder systematischer umfangreicher Überwachung öffentlich zugänglicher Bereiche.

Die österreichische Datenschutzbehörde führt eine Blacklist der Verarbeitungen mit DSFA-Pflicht und eine Whitelist. Beide vor der Beurteilung prüfen.

Praktisch relevante Auslöser in kleinen Projekten: umfangreiche Verarbeitung von Kinderdaten, Tracking über mehrere Dienste hinweg, KI-gestützte Bewertung von Personen, Gesundheitsdaten.

## Art 37 — Datenschutzbeauftragter

Pflicht bei Behörden, bei Kerntätigkeit mit umfangreicher regelmäßiger systematischer Überwachung und bei umfangreicher Verarbeitung besonderer Kategorien. Österreich hat keine zusätzliche Schwelle nach Beschäftigtenzahl eingeführt — anders als Deutschland mit § 38 BDSG. Wer die deutsche 20-Personen-Regel überträgt, liegt falsch.

Freiwillige Bestellung ist möglich; ist sie erfolgt, gelten die Pflichten aus Art 37 bis 39 vollumfänglich.

## Betroffenenrechte — Prozess

- Frist: unverzüglich, spätestens **ein Monat** ab Eingang; Verlängerung um zwei weitere Monate bei Komplexität, mit Begründung innerhalb des ersten Monats
- Identität des Antragstellers prüfen, ohne unnötig zusätzliche Daten zu erheben
- Auskunft nach Art 15 umfasst auch eine Kopie der Daten sowie die Informationen zu Zwecken, Kategorien, Empfängern, Speicherdauer, Rechten, Herkunft und automatisierter Entscheidungsfindung
- Löschbegehren gegen gesetzliche Aufbewahrungspflichten abgleichen (Rechnungen 7 Jahre nach § 132 BAO) — dann Einschränkung statt Löschung
- Unentgeltlich; Entgelt nur bei offenkundig unbegründeten oder exzessiven Anträgen

## Prüfpunkte

- [ ] Verarbeitungsverzeichnis existiert, aktuell, mit Rechtsgrundlagen und Löschfristen
- [ ] Dienstleisterliste vollständig, AVV je Dienstleister unterschrieben und abgelegt
- [ ] Drittlandübermittlungen mit Grundlage dokumentiert
- [ ] TOM schriftlich, Backup-Wiederherstellung tatsächlich getestet
- [ ] Keine Produktivdaten in Test- oder Entwicklungsumgebungen
- [ ] Breach-Prozess definiert, Verantwortliche benannt, Meldeweg bekannt
- [ ] DSFA-Pflicht geprüft, Ergebnis dokumentiert
- [ ] DSB-Pflicht geprüft, Ergebnis dokumentiert
- [ ] Prozess für Betroffenenanfragen mit Fristenüberwachung
- [ ] Löschkonzept, das gesetzliche Aufbewahrungsfristen berücksichtigt
- [ ] Mitarbeiter auf Vertraulichkeit verpflichtet und geschult
