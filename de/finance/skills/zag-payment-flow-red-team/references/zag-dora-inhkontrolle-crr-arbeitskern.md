# Arbeitskern ZAG, DORA, AnzV, InhKontrollV und CRR

Dieser Arbeitskern verdichtet amtliche Aufsichts- und Gesetzesquellen für Bank-Rechtsabteilungen. Er soll keine Quelle ersetzen, sondern die Skills zwingen, Zahlungsdienste, IKT-Risiken, Anzeigen und Kapitalregeln mit prüfbarer Beleglogik zu bearbeiten.

## Quellenstand und Live-Check

Vor tragenden Aussagen immer die aktuelle Fassung prüfen:

- BaFin-Merkblatt zum Zahlungsdiensteaufsichtsgesetz: Anwendungsbereich, Positivkatalog, Negativkatalog, E-Geld, erlaubte Tätigkeiten, Erlaubnis, Registrierung und Anzeigen.
- BaFin-Aufsichtsmitteilung vom 21.08.2025 zu DORA Artikel 16 und IKT-Drittparteienrisikomanagement.
- Anzeigenverordnung zum KWG in der Fassung mit Änderung vom 25.03.2026.
- Inhaberkontrollverordnung in der Fassung mit Änderung vom 04.02.2026.
- CRR, Verordnung (EU) Nr. 575/2013, nur auf Basis der aktuellen konsolidierten EUR-Lex-Fassung.

## ZAG-Prüfung

### Grundsatz

Das ZAG arbeitet nicht mit einem allgemeinen Nebentätigkeitsprivileg. Ein Zahlungsdienst kann erlaubnis- oder registrierungspflichtig sein, obwohl er nur als Teil eines Handels-, Plattform-, Software-, Karten-, Loyalty-, Token- oder Mobilitätsprodukts erscheint. Entscheidend ist der konkrete Zahlungsfluss: Wer nimmt von wem Geld entgegen, wer kann über Kundengelder verfügen, wer steht gegenüber Zahler oder Zahlungsempfänger als Dienstleister auf, und welche Leistung ist gegenüber dem Kunden versprochen?

### Positivkatalog

Für jedes Geschäftsmodell eine Flow-of-Funds-Tabelle bauen:

| ZAG-Achse | Kernfrage | Typischer Beleg |
| --- | --- | --- |
| Ein- und Auszahlung | Werden Bargeld oder Kontoguthaben auf ein Zahlungskonto gebracht oder von dort abgezogen? | Kontomodell, Kassenprozess, AGB |
| Zahlungsgeschäft | Werden Überweisungen, Lastschriften oder Kartenzahlungen ausgeführt? | Prozessdiagramm, Scheme-Regeln, Zahlungsauftrag |
| Zahlung mit Kredit | Wird die Zahlungsausführung mit Kreditgewährung verbunden? | Kreditvertrag, Limitlogik, Ausfallregel |
| Issuing/Acquiring | Wird ein Zahlungsinstrument ausgegeben oder Händlerakzeptanz organisiert? | Karten-/Walletvertrag, Händlervertrag |
| Finanztransfer | Wird Geld ohne Zahlungskonto des Zahlers oder Empfängers transferiert? | Agentennetz, Bargeldannahme, Empfängerprozess |
| Zahlungsauslösung | Löst ein Dienst für den Nutzer eine Zahlung von dessen Konto aus? | API-Flow, Consent, Redirect, TPP-Rolle |
| Kontoinformation | Werden Zahlungskontodaten aggregiert oder ausgewertet? | AIS-Consent, Dashboard, Datenmodell |
| E-Geld | Wird ein monetärer Wert gegen Geld ausgegeben, gespeichert und bei Dritten akzeptiert? | Wallet, Gutschein-/Token-Logik, Rücktausch |

### Ausnahmen

Ausnahmen eng am tatsächlichen Nutzungsrahmen prüfen. Nicht der Produktname entscheidet, sondern die rechtliche und technische Begrenzung.

| Ausnahme | Red Flag | Dokumentation |
| --- | --- | --- |
| Handelsvertreter | Plattform kann faktisch für beide Seiten verhandeln oder Zahlungen selbst steuern | Agenturvertrag, Vertretungsmacht, Preis- und Abschlussbefugnis |
| Technischer Dienstleister | Dienstleister kommt doch in Besitz von Geld oder steuert Zahlungsentscheidung | Prozess- und Kontozugriff, Treuhandkonto, Rollenbeschreibung |
| Limited Network | Akzeptanzkreis wächst offen, bundesweit oder wie ein allgemeines Zahlungsmittel | Akzeptanzstellenliste, Warenkreis, Schwellenmonitoring |
| Limited Range | Waren-/Dienstleistungskreis ist wirtschaftlich zu breit | Produktkatalog, MCC-/SKU-Mapping |
| Konzerninterne Zahlung | Drittgeschäft oder Kundenbezug rutscht hinein | Konzernstruktur, Nutzerkreis, Vertragskette |
| Kommunikationsnetz | Telko-Ausnahme wird für allgemeine digitale Güter überdehnt | Nutzerlimit, Abrechnung, Leistungsinhalt |

### Arbeitsprodukt

Immer liefern:

1. Zahlungsfluss in Rollen und Konten.
2. Tatbestandsmatrix zu § 1 Abs. 1 Satz 2 ZAG und § 1 Abs. 2 ZAG.
3. Ausnahmeprüfung nach § 2 ZAG mit Red-Team-Sicht der BaFin.
4. Erlaubnis-, Registrierungs- oder Anzeigeweg.
5. Unterlagenliste für BaFin/Bundesbank oder Negativauskunft.
6. Go/No-Go-Empfehlung mit Launch-Auflagen.

## DORA Artikel 16 und IKT-Drittparteien

### Abgrenzung

Artikel 16 DORA ist kein Freibrief. Für bestimmte Finanzunternehmen gilt ein vereinfachter IKT-Risikomanagementrahmen; die Organisation muss trotzdem ein nachvollziehbares, wirksames und dokumentiertes IKT-Risikomanagement betreiben. Die Prüfung beginnt mit der Frage, ob das Finanzunternehmen in den Anwendungsbereich des vereinfachten Rahmens fällt oder dem regulären Rahmen der Artikel 5 bis 15 DORA unterliegt.

### Governance-Prüfung

| Prüfung | Mindestinhalt |
| --- | --- |
| Leitungsorgan | Verantwortlichkeit, Genehmigung wesentlicher Leitlinien, Ressourcen, Eskalation |
| IKT-Risikorahmen | Rollen, Kontrollen, Risikobewertung, Schutzmaßnahmen, Nachverfolgung |
| Assets | Inventar, Kritikalität, Schutzbedarf, Eigentümer, Datenbezug |
| Zugriff | Need-to-use, privilegierte Rechte, Rezertifizierung, Protokollierung |
| Betrieb | Change, Patch, Backup, Wiederanlauf, Incident-Klassifizierung |
| Kontinuität | Szenarien, Tests, Kommunikationspläne, Lessons Learned |
| Drittparteien | Ex-ante-Risikoanalyse, Due Diligence, Vertragsklauseln, Unterauslagerung, Exit |
| Nachweisordner | Register, Beschlüsse, Reports, Verträge, Tests, Maßnahmenstatus |

### DORA-Drittparteienrisiko

Bei IKT-Dienstleistern den gesamten Lebenszyklus prüfen: Auswahl, Due Diligence, Vertrag, Monitoring, Unterauftragnehmer, Konzentrationsrisiko, Vorfall, Exit und Nachmigration. Die Bank darf sich nicht mit schönen Policies begnügen; sie braucht belastbare Kontrollrechte, Datenzugang, Informationsrechte, Auditmöglichkeiten, Notfalllogik und ein realistisches Exit-Szenario.

## AnzV-Anzeigenkalender

Die AnzV operationalisiert KWG-Anzeigen. Praktisch wichtig sind Einreichweg, Beteiligungen, enge Verbindungen, Auslandsbeziehungen, Organpersonen, Auslagerungen, Vergütung und elektronische Einreichung, wenn BaFin oder Bundesbank dies vorgeben. Anzeigen sind nicht nur Legal-Thema: Human Resources, Beteiligungsmanagement, Risk, Compliance, IT, Finance und Vorstandsbüro müssen abgestimmt werden.

### Anzeige-Backlog

| Anlass | Primärfrage | Beleg |
| --- | --- | --- |
| Organperson | Bestellung, Ermächtigung, Änderung, Ende, Fit-and-Proper | CV, Führungszeugnis, Eignungsmatrix, Zeitbudget |
| Bedeutende Beteiligung aktiv | Beteiligung der Bank an anderem Unternehmen | Beteiligungsstruktur, Quote, Geschäftsgegenstand |
| Beteiligung passiv | Veränderung bei Anteilseignern der Bank | Cap Table, Stimmrechte, Kontrollerwerb |
| Auslagerung | Wesentliche Auslagerung oder wichtige Änderung | Vertrag, Risikoanalyse, Registereintrag |
| Auslandsbezug | Tochter, Zweigstelle, enge Verbindung, Drittstaat | Strukturdiagramm, Aufsichtskontakt |
| LEI | Rechtsträgerkennung vorhanden und aktuell | LEI-Nachweis |

## InhKontrollV

Eine bedeutende Beteiligung ist kein normales M&A-Closing-Item. Der Erwerber muss zeigen, wer wirtschaftlich dahintersteht, wie finanziert wird, ob Zuverlässigkeit und Solidität stimmen, ob Geldwäsche-/Sanktionsrisiken bestehen, ob Geschäftsmodell und Aufsichtsfähigkeit leiden und ob die Beteiligung transparent kontrolliert werden kann. Bei komplexen Ketten ist eine lückenlose Beteiligungs- und Kontrollstruktur entscheidend.

### Deal-Check

| Frage | Warum sie praktisch wehtut |
| --- | --- |
| Wer erwirbt unmittelbar und mittelbar? | Treuhand, Fonds, Family Office, SPV und Stimmrechtsabreden können Anzeigeumfang verändern. |
| Welche Schwelle wird erreicht oder überschritten? | 10 %, 20 %, 30 %, 50 % und Kontrolle sauber mit Kapital, Stimmen und Einfluss trennen. |
| Wie ist der Erwerb finanziert? | BaFin/Bundesbank erwarten nachvollziehbare Herkunft und Belastbarkeit der Mittel. |
| Wer kontrolliert nach Closing? | Side Letters, Vetorechte, Governance und wirtschaftliche Abhängigkeiten offenlegen. |
| Ist Englisch ausreichend? | Einreichung kann möglich sein; Übersetzungsanforderungen können die Vollständigkeit verschieben. |

## CRR für Juristen

Die CRR ist kein reines Rechenthema. Legal muss erkennen, wann Verträge, Beteiligungen, Sicherheiten, Garantien, Konzentrationen, Gruppenbeziehungen und Produktstrukturen regulatorische Kapital-, Liquiditäts-, Leverage- oder Großkreditfolgen auslösen.

### Juristische Prüfachsen

| CRR-Achse | Legal-Frage |
| --- | --- |
| Begriffe Art. 4 | Ist die Einheit Institut, Finanzinstitut, Holding, Anbieter von Nebendienstleistungen oder Gruppe verbundener Kunden? |
| Eigenmittel | Wirkt ein Vertrag, Instrument oder Verlust auf CET1/AT1/T2 oder Abzugsposten? |
| Kreditrisiko | Welche Sicherheiten, Garantien, Netting- oder Substitutionslogik wird behauptet? |
| Großkredit | Werden Gegenparteien, wirtschaftliche Abhängigkeiten und Gruppenbildung richtig erfasst? |
| Liquidität | Entstehen Abfluss-, Zufluss-, Besicherungs- oder Kündigungsrisiken? |
| Leverage | Erhöht eine Struktur Bilanz-/Außerbilanzexposure? |
| Offenlegung | Muss die Bank eine Risikoposition, Governance oder Kennzahl intern oder extern erklären? |

## Standardausgabe für Skills

Jeder Skill, der diesen Arbeitskern nutzt, soll mindestens ausgeben:

- `Kurzentscheidung`: erlaubnispflichtig/anzeigepflichtig/prüfpflichtig/kein Treffer mit Begründung.
- `Normenmatrix`: Norm, Tatbestand, Tatsache, Beleg, Lücke, Risiko.
- `Aufsichtsroute`: BaFin, Bundesbank, EZB/SSM, EBA oder interne Gremien.
- `Dokumentenliste`: genau welche Unterlagen fehlen.
- `Red-Team`: stärkstes Gegenargument der Aufsicht.
- `Nächster Schritt`: konkreter Arbeitsauftrag mit Owner und Frist.
