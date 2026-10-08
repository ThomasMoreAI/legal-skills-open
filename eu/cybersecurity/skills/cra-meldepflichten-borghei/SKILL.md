---
name: cra-meldepflichten-borghei
title: /cyber-resilience-act:cra-meldepflichten
description: Steuerung der CRA-Meldepflichten nach Art. 14 VO (EU) 2024/2847 ab dem 11.09.2026 – Abgrenzung aktiv ausgenutzte Schwachstelle gegenüber schwerwiegendem Sicherheitsvorfall, 24-Stunden-Frühwarnung, 72-Stunden-Vollmeldung, Abschlussbericht binnen 14 Tagen bzw. 1 Monat, Einreichung über die einheitliche Meldeplattform an das CSIRT des Mitgliedstaats der Hauptniederlassung bei paralleler Unterrichtung der ENISA, interner Eskalationsprozess und Dokumentation. Use when ein Hersteller einen laufenden Vorfall oder eine ausgenutzte Schwachstelle melden muss oder wenn vor dem 11.09.2026 der Melde- und Eskalationsprozess aufgebaut und gegen NIS2 und DSGVO abgegrenzt wird.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/cyber-resilience-act/skills/cra-meldepflichten
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: cybersecurity
language: de
---

# /cyber-resilience-act:cra-meldepflichten

## Zweck

**Art. 14 CRA** ([VO (EU) 2024/2847](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R2847)) verpflichtet Hersteller von Produkten mit digitalen Elementen, **aktiv ausgenutzte Schwachstellen** und **schwerwiegende Sicherheitsvorfälle** in einer dreistufigen Kaskade zu melden. Die Pflicht gilt ab dem **11.09.2026** und ist damit die erste operative CRA-Pflicht überhaupt — mehr als ein Jahr vor der vollständigen Geltung. Dieser Skill bestimmt, ob ein meldepflichtiges Ereignis vorliegt, berechnet die Fristen, liefert die Meldeinhalte und baut den internen Eskalationsprozess, ohne den die 24-Stunden-Frist praktisch nicht einzuhalten ist.

> **⚠️ Aktualität (Stand 2026-07):** Die Verordnung ist am **10.12.2024 in Kraft** getreten. Die **Meldepflichten gelten ab dem 11.09.2026** — die Frist läuft in sieben Wochen. Seit dem **11.06.2026** gelten die Vorschriften über Konformitätsbewertungsstellen; die vollständige Geltung mit grundlegenden Anforderungen, CE-Kennzeichnung und Konformitätsbewertung folgt erst am **11.12.2027**.
>
> **Die Meldepflicht ist vorgezogen.** Sie greift, bevor die materiellen Produktanforderungen des Anhang I gelten. Ein Hersteller kann also meldepflichtig sein, obwohl seine Produkte die grundlegenden Anforderungen noch nicht erfüllen müssen. Wer auf 2027 plant, verfehlt den relevanten Stichtag um 15 Monate.
>
> **Sanktionsrahmen:** Verstöße gegen die zentralen Hersteller- und Meldepflichten sind mit **bis zu 15 Mio. EUR oder 2,5 % des weltweiten Jahresumsatzes** bewehrt, je nachdem, welcher Betrag höher ist (Art. 64 CRA).

## Eingaben

- Betroffenes Produkt mit Version, Rolle des Mandanten (Hersteller / Verwalter quelloffener Software) und CRA-Einstufung
- Zeitpunkt der **Kenntniserlangung**, minutengenau, mit Beleg (Ticket, Log, Mail)
- Art des Ereignisses: Schwachstelle mit Ausnutzungsnachweis oder Sicherheitsvorfall
- Nachweise für die aktive Ausnutzung (Exploit in freier Wildbahn, Angriffsindikatoren, Meldung eines Forschers, CERT-Hinweis)
- Auswirkungen: betroffene Nutzerzahl, Verfügbarkeit, Vertraulichkeit, Integrität, grenzüberschreitende Wirkung
- Verfügbarkeit eines Sicherheitsupdates oder einer Umgehungslösung und deren Zeitpunkt
- Mitgliedstaat der **Hauptniederlassung** in der Union
- Parallel laufende Pflichtenkreise: NIS2-Einrichtung? Personenbezogene Daten betroffen? DORA-Finanzunternehmen?

## Sub-Agent-Architektur

Drei gedankliche Rollen strukturieren die Bearbeitung, die im Ernstfall parallel und unter Zeitdruck läuft. Ein **Trigger-Prüfer** entscheidet als Erstes und binnen Minuten, ob ein meldepflichtiges Ereignis im Sinne des Art. 14 CRA vorliegt — aktiv ausgenutzte Schwachstelle oder schwerwiegender Sicherheitsvorfall — und hält den Zeitpunkt der Kenntniserlangung als fristauslösendes Ereignis fest. Ein **Fristen-Rechner** leitet daraus die drei Fälligkeiten ab, jeweils mit Datum und Uhrzeit, und überwacht sie bis zum Abschlussbericht. Ein **Melde-Redakteur** formuliert die Inhalte der jeweiligen Stufe adressatengerecht, ohne unnötige Details preiszugeben und ohne die Untersuchung zu präjudizieren. Der Trigger-Prüfer entscheidet im Zweifel **für** die Meldung: Die Frühwarnung ist bewusst niedrigschwellig ausgestaltet und kann in der Vollmeldung korrigiert werden.

## Ablauf

### 1. Meldeauslöser bestimmen ([Art. 14 CRA](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R2847))

Der CRA kennt **zwei getrennte Auslöser**. Sie sind sauber zu unterscheiden, weil die Frist für den Abschlussbericht unterschiedlich läuft.

**a) Aktiv ausgenutzte Schwachstelle.** Eine Schwachstelle in einem Produkt mit digitalen Elementen, für die belastbare Anhaltspunkte bestehen, dass ein Angreifer sie **tatsächlich ausnutzt** — ohne dass der Hersteller sie behoben oder öffentlich gemacht hat. Entscheidend ist die **Ausnutzung**, nicht die Schwere: Eine hoch bewertete, aber nicht ausgenutzte Schwachstelle löst die Meldepflicht nach Art. 14 CRA **nicht** aus; sie fällt in das Schwachstellenmanagement nach Anhang I Teil II.

Typische Anhaltspunkte: Exploit-Code in freier Wildbahn, Angriffsindikatoren aus Kundeninstallationen, Hinweis eines Sicherheitsforschers mit Proof of Concept in Verbindung mit beobachtetem Angriffsverkehr, Aufnahme in einen Katalog bekannt ausgenutzter Schwachstellen.

**b) Schwerwiegender Sicherheitsvorfall.** Ein Sicherheitsvorfall, der die Cybersicherheit des Produkts oder die Fähigkeit des Produkts, die Vertraulichkeit, Integrität oder Verfügbarkeit kritischer oder wesentlicher Funktionen zu schützen, **nachteilig beeinflusst**. Erfasst sind auch Vorfälle in der Entwicklungs- oder Auslieferungsinfrastruktur des Herstellers, soweit sie auf das Produkt durchschlagen — etwa ein kompromittierter Build-Server oder Signaturschlüssel.

> **Im Zweifel melden.** Die Frühwarnung verlangt keine abgeschlossene Analyse. Eine später als nicht meldepflichtig erkannte Frühwarnung ist folgenlos korrigierbar; eine versäumte 24-Stunden-Frist ist es nicht.

### 2. 24-Stunden-Frühwarnung ([Art. 14 CRA](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R2847))

Fällig **innerhalb von 24 Stunden ab Kenntniserlangung**. Fristbeginn ist der Zeitpunkt, zu dem der Hersteller Kenntnis erlangt — **nicht** der Zeitpunkt einer internen Bestätigung, einer Managemententscheidung oder eines abgeschlossenen Forensikberichts.

Inhalt der Frühwarnung, bewusst knapp gehalten:

- Bezeichnung des betroffenen Produkts und der betroffenen Versionen
- Art des Ereignisses: aktiv ausgenutzte Schwachstelle oder schwerwiegender Sicherheitsvorfall
- Erste, vorläufige Einschätzung der Auswirkungen
- Angabe, ob eine Ausnutzung beobachtet wurde und in welchem Umfang
- Betroffene Mitgliedstaaten, soweit bereits absehbar
- Kontaktdaten der verantwortlichen Stelle beim Hersteller

Die Frühwarnung ist **kein** Vorfallsbericht. Vollständigkeit wird nicht verlangt; Verzögerung zugunsten von Vollständigkeit ist der klassische Fehler.

### 3. 72-Stunden-Vollmeldung ([Art. 14 CRA](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R2847))

Fällig **innerhalb von 72 Stunden ab Kenntniserlangung** — die Frist läuft **ab demselben Zeitpunkt** wie die Frühwarnung, nicht ab deren Absendung. Es bleiben faktisch 48 Stunden nach der Frühwarnung.

Inhalt:

- Allgemeine Informationen über Art und Schwere des Ereignisses
- Betroffene Produkte, Versionen und geschätzte Zahl betroffener Nutzer
- Verfügbare Angaben zur Schwachstelle einschließlich Kennung (CVE), soweit vergeben
- Ergriffene und geplante **Korrektur- und Abhilfemaßnahmen**
- Handlungsempfehlungen für Nutzer und Betreiber
- Aktualisierung und ggf. Korrektur der Angaben aus der Frühwarnung

Wo die Untersuchung noch läuft, ist das ausdrücklich zu vermerken. Unsichere Angaben sind als vorläufig zu kennzeichnen, nicht wegzulassen.

### 4. Abschlussbericht — 14 Tage oder 1 Monat ([Art. 14 CRA](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R2847))

Hier trennen sich die beiden Auslöser:

| Auslöser | Frist für den Abschlussbericht | Fristbeginn |
|---|---|---|
| **Aktiv ausgenutzte Schwachstelle** | spätestens **14 Tage** | ab Verfügbarkeit eines **Sicherheitsupdates oder einer Umgehungslösung** |
| **Schwerwiegender Sicherheitsvorfall** | **1 Monat** | ab der **Erstmeldung** (72-Stunden-Meldung) |

Inhalt des Abschlussberichts:

- Beschreibung der Schwachstelle einschließlich Schweregrad und Auswirkungen
- Angaben zu ausnutzenden Akteuren, soweit verfügbar
- Einzelheiten des **bereitgestellten Sicherheitsupdates** oder der Abhilfemaßnahme
- Bei einem Vorfall: Ursache, Verlauf, Schweregrad, Auswirkungen und angewandte Abhilfemaßnahmen
- Ggf. grenzüberschreitende Auswirkungen

Die 14-Tage-Frist ist die praktisch heikelste: Sie knüpft nicht an die Meldung, sondern an die **Verfügbarkeit des Updates** an. Wer den Zeitpunkt der Update-Bereitstellung nicht dokumentiert, kann die Fristwahrung später nicht belegen.

### 5. Meldeweg — einheitliche Meldeplattform, CSIRT und ENISA ([Art. 14, 16 CRA](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R2847))

Gemeldet wird über die **CRA-Einheitliche Meldeplattform** (Single Reporting Platform). Adressat ist das **CSIRT des Mitgliedstaats, in dem der Hersteller seine Hauptniederlassung hat**. Die **ENISA erhält die Information parallel** über die Plattform — eine **gesonderte Meldung an die ENISA ist nicht erforderlich und nicht vorgesehen**.

Praktische Konsequenzen:

- Der Mitgliedstaat der **Hauptniederlassung** ist vorab zu bestimmen und zu dokumentieren; er steuert das zuständige CSIRT. Für Hersteller ohne Unionsniederlassung ist über den Bevollmächtigten zu bestimmen.
- Für Deutschland ist das **BSI** ([bsi.bund.de](https://www.bsi.bund.de/)) die maßgebliche Schnittstelle. `[unverifiziert - prüfen]` Die konkrete Ausgestaltung der deutschen Anbindung an die Plattform sowie die Zuständigkeitsverteilung nach Art. 52 CRA sind zu verifizieren.
- Zugänge, Zertifikate und Berechtigungen für die Plattform sind **vor** dem 11.09.2026 einzurichten und mindestens einmal zu testen. Ein Zugang, der im Ernstfall erst beantragt wird, kostet die 24-Stunden-Frist.
- Der Meldeweg ist auch außerhalb der Geschäftszeiten sicherzustellen; Vorfälle beginnen typischerweise nachts oder am Wochenende.

### 6. Interner Eskalationsprozess für die 24-Stunden-Frist ([Art. 13, 14 CRA](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R2847))

Die 24-Stunden-Frist ist eine **Organisationspflicht**, keine bloße Formalität. Erforderlich ist ein dokumentierter Prozess mit mindestens folgenden Elementen:

1. **Eingangskanäle** bündeln: Support, Sicherheitsforscher über die CVD-Policy, CERT-Hinweise, Monitoring, Lieferantenmeldungen — alle münden in ein Ticket mit Zeitstempel.
2. **Kenntniserlangung definieren und protokollieren**: Wer im Unternehmen Kenntnis erlangt, gilt als Kenntniserlangung des Herstellers. Der Zeitstempel ist unveränderlich festzuhalten.
3. **Triage binnen weniger Stunden** durch eine benannte Rolle mit Vertretungsregelung und 24/7-Erreichbarkeit.
4. **Entscheidungsbefugnis vorverlagern**: Die Freigabe der Frühwarnung darf nicht von der Geschäftsleitung abhängen. Vorab freigegebene Textbausteine und eine klare Freigabematrix.
5. **Rufbereitschaft** und Eskalationsliste mit Erreichbarkeiten, jährlich geprüft.
6. **Übung**: mindestens ein Trockenlauf pro Jahr gegen die Plattform, mit Protokoll.
7. **Verzahnung** mit dem Schwachstellenmanagement nach Anhang I Teil II und mit der Kommunikation an Nutzer.

Die Prozessdokumentation ist zugleich der Entlastungsnachweis gegenüber der Marktüberwachungsbehörde.

### 7. Nutzerinformation, Dokumentation und Abgrenzung zu NIS2 und DSGVO ([Art. 14 CRA](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R2847))

**Nutzerinformation.** Neben der Behördenmeldung sind die betroffenen Nutzer über das Ereignis und erforderlichenfalls über Abhilfemaßnahmen zu unterrichten. Behördenmeldung und Nutzerinformation sind **getrennte Pflichten**; die eine ersetzt die andere nicht.

**Dokumentation.** Zu jedem Ereignis sind aufzubewahren: Zeitpunkt und Beleg der Kenntniserlangung, Triage-Entscheidung mit Begründung, Fristberechnung, Wortlaut aller drei Meldestufen mit Sendenachweis, Zeitpunkt der Update-Bereitstellung, Nutzerinformation, Nachbereitung.

**Abgrenzung — ein Ereignis, mehrere Meldepflichten:**

| Regime | Anknüpfung | Adressat | Fristen |
|---|---|---|---|
| **CRA Art. 14** | **Produkt** mit digitalen Elementen | CSIRT über die einheitliche Meldeplattform, ENISA parallel | 24h / 72h / 14 Tage bzw. 1 Monat |
| **NIS2 Art. 23** | **Einrichtung** in einem erfassten Sektor | zuständige Behörde, in Deutschland das BSI | 24h / 72h / 1 Monat |
| **DSGVO Art. 33** | **personenbezogene Daten** | Aufsichtsbehörde (LfDI/BfDI), ggf. Betroffene nach Art. 34 | 72h |
| **DORA Art. 19** | Finanzunternehmen, **IKT-Vorfall** | zuständige Finanzaufsicht | eigener Fristenlauf |

Ein einziger Vorfall kann alle vier Pflichten gleichzeitig auslösen. Die Meldungen sind **inhaltlich abzustimmen**, aber getrennt abzusetzen; keine Pflicht konsumiert eine andere.

## Quellen

### Statute

- [VO (EU) 2024/2847 (Cyber Resilience Act)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R2847) — Volltext mit Anhängen
- Art. 14 CRA (Meldepflichten der Hersteller — 24 Stunden / 72 Stunden / Abschlussbericht), Art. 13 CRA (Pflichten der Hersteller), Art. 16 CRA (einheitliche Meldeplattform, ENISA) `[unverifiziert - prüfen]`, Art. 52 CRA (Marktüberwachung), Art. 64 CRA (Sanktionen)
- Anhang I Teil II CRA (Schwachstellenbehandlung) — Schnittstelle zur Meldepflicht
- [Art. 23 RL (EU) 2022/2555 (NIS2)](https://eur-lex.europa.eu/eli/dir/2022/2555/oj) — einrichtungsbezogene Meldepflicht
- [Art. 33, 34 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679) — Datenschutzmeldung
- [VO (EU) 2022/2554 (DORA)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32022R2554) — IKT-Vorfallmeldung im Finanzsektor

### Leitlinien

- [Europäische Kommission, Cyber Resilience Act — Meldepflichten und FAQ zur Umsetzung](https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act)
- ENISA, technische Vorgaben zur einheitlichen Meldeplattform
- [BSI — Meldewege und Umsetzung in Deutschland](https://www.bsi.bund.de/)

**Rechtsprechung:** Zum Cyber Resilience Act ist **keine Rechtsprechung ersichtlich** (Stand 07/2026); die Meldepflichten gelten erst ab dem 11.09.2026. Erfahrungswerte aus der DSGVO- und NIS2-Meldepraxis sind allenfalls analog heranzuziehen und ausdrücklich als Analogie zu kennzeichnen.

## Ausgabeformat

```
CRA-MELDUNG — <Vorfall-ID> — <Produkt> — <Datum>

I.    Rolle und Produkt              [Hersteller / OSS-Verwalter; Produkt, Version]
II.   Auslöser (Art. 14 CRA)         [aktiv ausgenutzte Schwachstelle /
                                      schwerwiegender Sicherheitsvorfall / keiner]
      Begründung                     <…>
III.  Kenntniserlangung              <TT.MM.JJJJ, HH:MM> — Beleg: <…>
IV.   Meldekaskade
      24h-Frühwarnung   Frist: <TT.MM. HH:MM>  Status: <abgesetzt / offen>
      72h-Vollmeldung   Frist: <TT.MM. HH:MM>  Status: <…>
      Abschlussbericht  Frist: <14 Tage ab Update / 1 Monat ab Erstmeldung>
V.    Meldeweg                       Einheitliche Meldeplattform →
                                     CSIRT <Mitgliedstaat der Hauptniederlassung>
                                     ENISA erhält parallel — keine Zusatzmeldung
VI.   Inhalte je Meldestufe          <Textbausteine / Verweise>
VII.  Nutzerinformation              [erforderlich? Kanal, Zeitpunkt]
VIII. Parallele Meldepflichten       NIS2 [ja/nein] · DSGVO Art. 33 [ja/nein]
                                     DORA [ja/nein]
IX.   Sanktionsrisiko (Art. 64 CRA)  [bis 15 Mio. EUR / 2,5 %]

Eskalationspfad: <Rolle, Erreichbarkeit, Freigabematrix>
Risikoeinstufung: 🟢 / 🟡 / 🔴
Nächster Schritt: <…>
```

## Risiken / typische Fehler

- **Fristbeginn falsch angesetzt** — die 24 Stunden laufen ab **Kenntniserlangung**, nicht ab interner Bestätigung, Managementfreigabe oder Abschluss der Forensik. Die Verschiebung des Fristbeginns ist der praktisch häufigste und teuerste Fehler.
- **72-Stunden-Frist von der Frühwarnung aus gerechnet** — sie läuft ab **demselben** Zeitpunkt wie die 24-Stunden-Frist. Nach der Frühwarnung verbleiben faktisch 48 Stunden, nicht 72.
- **Abschlussbericht-Fristen vertauscht** — Schwachstelle: **14 Tage ab Verfügbarkeit des Sicherheitsupdates oder der Umgehungslösung**; Vorfall: **1 Monat ab der Erstmeldung**. Die Anknüpfungspunkte sind verschieden.
- **Zeitpunkt der Update-Bereitstellung nicht dokumentiert** — ohne ihn ist die Wahrung der 14-Tage-Frist nicht belegbar.
- **Schwere mit Ausnutzung verwechselt** — Art. 14 CRA knüpft an die **aktive Ausnutzung** an, nicht an einen CVSS-Wert. Eine kritische, aber nicht ausgenutzte Schwachstelle ist nicht nach Art. 14 CRA meldepflichtig, bleibt aber Gegenstand des Schwachstellenmanagements nach Anhang I Teil II.
- **Gesonderte ENISA-Meldung abgesetzt** — die ENISA erhält die Information **parallel** über die einheitliche Meldeplattform. Eine Zusatzmeldung ist weder erforderlich noch vorgesehen.
- **Falsches CSIRT adressiert** — Adressat ist das CSIRT des Mitgliedstaats der **Hauptniederlassung**, nicht des Landes, in dem der Vorfall auftrat.
- **Plattformzugang erst im Ernstfall beantragt** — Zugänge und Berechtigungen sind vor dem **11.09.2026** einzurichten und zu testen.
- **Freigabe an die Geschäftsleitung gebunden** — eine Frühwarnung, die auf eine Vorstandsentscheidung wartet, ist regelmäßig verspätet. Die Freigabebefugnis ist vorzuverlagern.
- **Nutzerinformation vergessen** — Behördenmeldung und Unterrichtung der betroffenen Nutzer sind getrennte Pflichten.
- **Parallelpflichten übersehen** — ein Ereignis kann CRA, NIS2, DSGVO und DORA gleichzeitig auslösen; keine Meldung ersetzt eine andere.
- **Auf 11.12.2027 geplant** — die Meldepflicht gilt bereits ab **11.09.2026**, unabhängig davon, dass die grundlegenden Anforderungen später greifen.
- **⚠️ Artikelnummern ungeprüft übernommen** — insbesondere die Fundstelle zur einheitlichen Meldeplattform ist `[unverifiziert - prüfen]` und vor mandantengerichteter Verwendung am Amtsblatttext der VO (EU) 2024/2847 zu verifizieren.
