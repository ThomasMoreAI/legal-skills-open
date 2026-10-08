---
name: cra-schwachstellenmanagement-borghei
title: /cyber-resilience-act:cra-schwachstellenmanagement
description: Aufbau und Prüfung des Schwachstellenmanagements nach Anhang I Teil II VO (EU) 2024/2847 – Politik zur koordinierten Schwachstellenoffenlegung (CVD-Policy), Kontaktstelle und Eingangskanäle für Meldungen, Triage und Bewertung, Behebung durch Sicherheitsupdates, sichere Update-Verteilung mit Signatur, öffentliche Offenlegung behobener Schwachstellen und Security Advisories, Koordinierung mit CSIRT, BSI und CVE-Vergabe sowie die Schnittstellen zur Meldepflicht nach Art. 14 CRA, zu NIS2 und zur reformierten Produkthaftung ab dem 09.12.2026. Use when ein Hersteller eine CVD-Policy einführen, seinen Schwachstellenprozess CRA-fest machen oder eine eingehende Schwachstellenmeldung eines Sicherheitsforschers rechtlich und prozessual behandeln muss.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/cyber-resilience-act/skills/cra-schwachstellenmanagement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: cybersecurity
language: de
---

# /cyber-resilience-act:cra-schwachstellenmanagement

## Zweck

**Anhang I Teil II** des Cyber Resilience Act ([VO (EU) 2024/2847](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R2847)) verlangt vom Hersteller ein funktionierendes Schwachstellenmanagement über den gesamten **Unterstützungszeitraum**: Schwachstellen finden, dokumentieren, unverzüglich beheben, Updates sicher verteilen, behobene Schwachstellen offenlegen und eine **Politik zur koordinierten Schwachstellenoffenlegung (CVD-Policy)** durchsetzen. Dieser Prozess ist zugleich das Nervensystem der Meldepflicht: Ohne ihn wird eine aktiv ausgenutzte Schwachstelle nicht rechtzeitig erkannt, und die 24-Stunden-Frist des Art. 14 CRA ist strukturell nicht einzuhalten.

> **⚠️ Aktualität (Stand 2026-07):** Die Verordnung ist am **10.12.2024 in Kraft** getreten. Ab dem **11.09.2026** greifen die **Meldepflichten** nach Art. 14 CRA; die Anforderungen des Anhang I Teil II gelten mit der vollständigen Geltung ab dem **11.12.2027**.
>
> **Die Reihenfolge ist praktisch umgekehrt.** Zwar wird das Schwachstellenmanagement erst 2027 einklagbar, doch die Meldepflicht ab dem 11.09.2026 setzt es faktisch voraus: Wer keine Eingangskanäle, keine Triage und keine dokumentierte Update-Bereitstellung hat, kann weder die 24-Stunden-Frühwarnung noch den an die Update-Verfügbarkeit anknüpfenden 14-Tage-Abschlussbericht einhalten. Der CVD-Prozess ist daher vor dem 11.09.2026 aufzubauen.
>
> **Schnittstelle Produkthaftung:** Mit der Umsetzung der reformierten Produkthaftungsrichtlinie zum **09.12.2026** wird **Software als Produkt** behandelt; unterlassene Sicherheitsupdates innerhalb des Unterstützungszeitraums können damit unmittelbar haftungsbegründend wirken. `[unverifiziert - prüfen]` Der deutsche Umsetzungsstand ist gesondert zu prüfen.
>
> **Sanktionsrahmen:** Verstöße gegen die grundlegenden Anforderungen einschließlich Anhang I Teil II sind mit **bis zu 15 Mio. EUR oder 2,5 % des weltweiten Jahresumsatzes** bewehrt, je nachdem, welcher Betrag höher ist (Art. 64 CRA).

## Eingaben

- Produktportfolio mit Versionen, Unterstützungszeiträumen und Einstufung aus dem CRA-Produktinventar
- Vorhandene SBOM je Produktversion, Format und Aktualisierungsfrequenz
- Bestehende Prozesse: Eingang von Sicherheitsmeldungen, Triage, Patch-Entwicklung, Release, Kommunikation
- Vorhandene CVD-Policy, `security.txt`, Bug-Bounty-Programm, Kontaktadresse
- Update-Infrastruktur: Signaturverfahren, Verteilkanäle, Rollback, Erreichbarkeit von Offline-Installationen
- Konkrete eingehende Meldung, sofern vorhanden: Melder, Datum, Inhalt, Offenlegungsfrist des Melders
- Parallele Pflichtenkreise: NIS2-Einrichtung? DORA? Produkthaftungsrisiko?

## Sub-Agent-Architektur

Drei gedankliche Rollen strukturieren die Arbeit. Ein **Prozess-Architekt** entwirft und prüft den Ablauf von der Eingangsstelle über Triage und Behebung bis zur Offenlegung und verankert ihn organisatorisch mit Rollen, Vertretung und Erreichbarkeit. Ein **Triage-Analyst** bewertet die einzelne Schwachstelle nach Ausnutzbarkeit, Schwere und Betroffenheit des Portfolios — er entscheidet insbesondere, ob eine **aktive Ausnutzung** vorliegt und damit der Meldeauslöser des Art. 14 CRA erreicht ist, und übergibt in diesem Fall unverzüglich an den Skill `cra-meldepflichten`. Ein **Kommunikations-Redakteur** verantwortet die Außendarstellung: Antwort an den Melder, Nutzerinformation, Security Advisory nach Bereitstellung des Updates und Abstimmung mit CSIRT und CVE-Vergabestelle. Der Triage-Analyst ist der zeitkritische Pfad; seine Entscheidung darf nicht auf die Patch-Entwicklung warten.

## Ablauf

### 1. Politik zur koordinierten Schwachstellenoffenlegung ([Anhang I Teil II CRA](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R2847))

Die **CVD-Policy** ist nach Anhang I Teil II zu **erlassen, durchzusetzen und öffentlich zugänglich zu machen**. Mindestinhalt:

- **Geltungsbereich**: welche Produkte, Versionen und Dienste erfasst sind
- **Meldekanal** mit Kontaktadresse und, wo sinnvoll, Möglichkeit verschlüsselter Übermittlung
- **Reaktionszusagen**: Eingangsbestätigung, erste Rückmeldung, Statusaktualisierungen — jeweils mit Zeitrahmen
- **Offenlegungsmodell**: koordinierte Offenlegung nach Bereitstellung eines Updates; Regelfrist und Umgang mit Fristverlängerung
- **Safe Harbour**: Zusage, gegen gutgläubig handelnde Forschende, die sich an die Policy halten, keine rechtlichen Schritte einzuleiten — insbesondere keine straf- oder zivilrechtliche Verfolgung wegen §§ 202a, 202c, 303a StGB
- **Anerkennung** des Melders (Credit) und Umgang mit Bug-Bounty-Vergütung
- **Ausschlüsse**: was ausdrücklich nicht erfasst ist (etwa Denial-of-Service-Tests in Produktivsystemen, Social Engineering)

Die Policy ist praktisch auffindbar zu machen: über die Produktwebsite, in den Nutzerinformationen nach Anhang II CRA und über eine `security.txt` nach dem einschlägigen Internetstandard.

### 2. Eingangskanal und Erstreaktion ([Anhang I Teil II CRA](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R2847))

Anhang I Teil II verlangt Maßnahmen, die das **Melden von Schwachstellen erleichtern**, einschließlich einer Kontaktadresse.

- **Eine benannte Adresse**, überwacht, mit Vertretungsregelung und Erreichbarkeit auch außerhalb der Geschäftszeiten
- **Automatische Eingangsbestätigung** mit Vorgangsnummer und Zeitstempel — der Zeitstempel ist zugleich Beleg der Kenntniserlangung im Sinne des Art. 14 CRA
- **Keine Abwehrreaktion**: Der erste Kontakt mit einem Sicherheitsforscher entscheidet über den weiteren Verlauf. Juristische Drohungen führen regelmäßig zur unkoordinierten Veröffentlichung
- **Bündelung** aller Kanäle in ein Ticketsystem: Support, Vertrieb, CERT-Hinweise, Lieferantenmeldungen, Monitoring — Schwachstellenmeldungen erreichen das Unternehmen selten über den vorgesehenen Weg
- Weiterleitung an die Triage binnen weniger Stunden, nicht binnen Tagen

### 3. Triage und Bewertung ([Art. 14 CRA](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R2847))

Die Triage beantwortet vier Fragen, und zwar in dieser Reihenfolge:

1. **Betroffenheit** — welche Produkte und Versionen sind betroffen? Diese Frage ist ohne belastbare **SBOM** nicht binnen Stunden zu beantworten.
2. **Reproduzierbarkeit und Schwere** — Verifikation, Bewertung nach einem etablierten Schema (etwa CVSS), Einordnung der Ausnutzbarkeit.
3. **Aktive Ausnutzung?** — bestehen Anhaltspunkte, dass die Schwachstelle **tatsächlich ausgenutzt wird**? Wenn ja, ist der Meldeauslöser des **Art. 14 CRA** erreicht und die 24-Stunden-Frühwarnung läuft ab Kenntniserlangung. Übergabe an `cra-meldepflichten`.
4. **Sofortmaßnahmen** — gibt es eine Umgehungslösung, die Nutzer sofort anwenden können?

> **Trennung zweier Regime.** Eine nicht ausgenutzte Schwachstelle löst **keine** Meldepflicht nach Art. 14 CRA aus, unterliegt aber vollständig den Behandlungspflichten des Anhang I Teil II. Umgekehrt begründet die Meldung an die Behörde keine Erfüllung der Behebungspflicht. Beide Stränge laufen parallel weiter.

Jede Triage-Entscheidung ist mit Begründung und Zeitstempel zu dokumentieren — auch und gerade die Entscheidung **gegen** eine Meldung.

### 4. Behebung und Verteilung von Sicherheitsupdates ([Anhang I Teil II CRA](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R2847))

Anhang I Teil II verlangt die **unverzügliche Behebung**, insbesondere durch Sicherheitsupdates, und **Mechanismen zur sicheren Verteilung**:

- **Unverzüglich** heißt: ohne schuldhaftes Zögern nach Verifikation, nicht im nächsten regulären Release-Zyklus
- **Unentgeltlich** und, soweit technisch möglich, **getrennt von Funktionsupdates**
- **Signatur und Integritätsprüfung** der Updates; sichere Verteilkanäle; Schutz gegen Downgrade
- Möglichkeit **automatischer Installation** mit Abschaltoption für den Nutzer
- **Rollback-Fähigkeit** und getestete Update-Pfade auch für ältere Versionsstände
- **Zeitpunkt der Bereitstellung dokumentieren** — er löst die **14-Tage-Frist** für den Abschlussbericht nach Art. 14 CRA aus und ist ohne Dokumentation später nicht belegbar
- Wo eine Behebung nicht sofort möglich ist: dokumentierte **Umgehungslösung** und Nutzerhinweis

Bei Schwachstellen in **quelloffenen Fremdkomponenten** ist der Hersteller gegenüber seinen Nutzern verantwortlich. Das Warten auf einen Upstream-Fix entlastet nicht; erforderlichenfalls ist selbst zu patchen oder zu mitigieren.

### 5. Öffentliche Offenlegung und Security Advisory ([Anhang I Teil II CRA](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R2847))

Nach Bereitstellung eines Sicherheitsupdates sind Informationen über die **behobene Schwachstelle öffentlich offenzulegen**. Inhalt des Advisory:

- Beschreibung der Schwachstelle und der betroffenen Produkte und Versionen
- **Auswirkungen und Schweregrad**
- Klare Hinweise, wie Nutzer die Schwachstelle beheben — Version, Bezugsquelle, Vorgehen
- Kennung (CVE), soweit vergeben, und Zeitpunkt der Behebung

Die Offenlegung darf **verzögert** werden, solange die Sicherheitsrisiken einer Veröffentlichung die Vorteile überwiegen — etwa weil noch kein Update verfügbar ist. Diese Abwägung ist zu dokumentieren; sie ist eine Ausnahme, kein Regelfall und kein Instrument der Reputationssteuerung.

Die Nutzerinformation nach Art. 14 CRA und das Advisory nach Anhang I Teil II überschneiden sich, sind aber nicht deckungsgleich: Die eine ist vorfallbezogen und geht der Behebung regelmäßig voraus, das andere folgt der Behebung.

### 6. Koordinierung mit CSIRT, BSI und CVE-Vergabe ([Art. 14 CRA](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R2847))

- **CSIRT-Koordinierung**: Bei aktiv ausgenutzten Schwachstellen läuft die Meldung über die einheitliche Meldeplattform an das CSIRT des Mitgliedstaats der Hauptniederlassung; die **ENISA erhält die Information parallel**. Für Deutschland ist das **BSI** ([bsi.bund.de](https://www.bsi.bund.de/)) die maßgebliche Schnittstelle
- **CVE-Kennung** über eine CVE Numbering Authority beantragen — sie ist die gemeinsame Sprache gegenüber Kunden, Behörden und Scannern. Eine eigene CNA-Rolle ist bei größerem Portfolio zu erwägen
- **Mehrparteien-Koordinierung**, wenn eine Schwachstelle in einer weit verbreiteten Komponente mehrere Hersteller betrifft: Zeitplan, gemeinsames Offenlegungsdatum, Embargo-Disziplin
- **Behördliche Nachfragen** und Marktüberwachungsmaßnahmen nach Art. 52 CRA vorbereiten: Der dokumentierte Prozess ist der Entlastungsnachweis

### 7. Schnittstellen zu NIS2, Produkthaftung und Vertragsrecht ([Art. 14, 52 CRA](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R2847))

**NIS2.** Für die eigene Organisation gelten daneben die Risikomanagement- und Meldepflichten der [RL (EU) 2022/2555](https://eur-lex.europa.eu/eli/dir/2022/2555/oj). Der CRA knüpft am **Produkt** an, NIS2 an der **Einrichtung**. Ein Hersteller kann zugleich Adressat beider Regime sein und muss beide Meldewege getrennt bedienen. Zugleich ist der Hersteller Lieferant seiner NIS2-pflichtigen Kunden: Diese verlangen vertraglich Reaktionszeiten, SBOM und Advisory-Zugang.

**Produkthaftung ab 09.12.2026.** Die reformierte Produkthaftungsrichtlinie behandelt **Software als Produkt** unabhängig von der Verkörperung; der Haftungshöchstbetrag der alten Rechtslage entfällt, der Schadensbegriff wird erweitert, und es gelten Offenlegungspflichten sowie widerlegliche Kausalitätsvermutungen. `[unverifiziert - prüfen]` Der deutsche Umsetzungsstand ist gesondert zu prüfen. Praktische Folge: Ein **unterlassenes Sicherheitsupdate innerhalb des Unterstützungszeitraums** kann als Produktfehler zu bewerten sein. CRA-Compliance wird damit zur Haftungsverteidigung; die CRA-Dokumentation ist entsprechend beweisfest zu führen.

**Vertragsrecht und Lieferkette.** Erforderlich sind Zulieferzusagen zu Schwachstellenmeldung, Patch-Bereitstellung und SBOM-Lieferung, die mindestens den eigenen Unterstützungszeitraum abdecken, sowie Regressregelungen. Gegenüber Kunden sind Reaktionszeiten und Advisory-Kanäle sauber zu definieren.

## Quellen

### Statute

- [VO (EU) 2024/2847 (Cyber Resilience Act)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R2847) — Volltext mit Anhängen
- Anhang I Teil II CRA (Anforderungen an die Schwachstellenbehandlung), Anhang I Teil I CRA (Produkteigenschaften), Anhang II CRA (Nutzerinformationen), Anhang VII CRA (technische Dokumentation)
- Art. 13 CRA (Pflichten der Hersteller, Unterstützungszeitraum), Art. 14 CRA (Meldepflichten), Art. 52 CRA (Marktüberwachung), Art. 64 CRA (Sanktionen)
- [RL (EU) 2022/2555 (NIS2)](https://eur-lex.europa.eu/eli/dir/2022/2555/oj) — Art. 21, 23
- [RL (EU) 2024/2853 (Produkthaftung)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024L2853) — Software als Produkt, Umsetzung bis 09.12.2026
- §§ 202a, 202c, 303a StGB — strafrechtlicher Rahmen für Sicherheitsforschung und Grund für die Safe-Harbour-Zusage

### Leitlinien

- [Europäische Kommission, Cyber Resilience Act — Politikseite und FAQ zur Umsetzung](https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act)
- [BSI — koordinierte Schwachstellenoffenlegung und Meldewege](https://www.bsi.bund.de/)
- ENISA, Vorgaben zur Schwachstellenkoordinierung und zur einheitlichen Meldeplattform
- ISO/IEC 29147 (Vulnerability Disclosure) und ISO/IEC 30111 (Vulnerability Handling) als Referenzrahmen

**Rechtsprechung:** Zum Cyber Resilience Act ist **keine Rechtsprechung ersichtlich** (Stand 07/2026). Zur strafrechtlichen Einordnung von Sicherheitsforschung nach §§ 202a, 202c StGB existiert Rechtsprechung, die den CRA jedoch nicht trägt; sie ist gesondert und mit Verifikationsmarker zu recherchieren.

## Ausgabeformat

```
CRA-SCHWACHSTELLENMANAGEMENT — <Produkt / Vorgang> — <Datum>

I.    CVD-Policy (Anhang I Teil II)
      Veröffentlicht / auffindbar        [ja / nein — Fundort]
      Geltungsbereich / Reaktionszusagen […]
      Safe Harbour                       [ja / nein]
      security.txt                       [ja / nein]
II.   Eingangskanal
      Kontaktadresse / Erreichbarkeit    […]
      Eingangsbestätigung + Zeitstempel  […]
III.  Triage
      Betroffene Produkte/Versionen      [SBOM-gestützt? …]
      Schwere / Ausnutzbarkeit           […]
      AKTIVE AUSNUTZUNG?                 [ja → Art. 14 CRA, 24h-Frist läuft
                                          ab <TT.MM. HH:MM> / nein]
IV.   Behebung
      Update / Umgehungslösung           […]
      Zeitpunkt der Bereitstellung       <TT.MM.JJJJ, HH:MM> (löst 14-Tage-Frist)
      Signatur / sichere Verteilung      […]
V.    Offenlegung
      Security Advisory                  [Inhalt, Zeitpunkt]
      CVE-Kennung                        […]
      Verzögerung begründet?             […]
VI.   Koordinierung                      [CSIRT / BSI / CNA / Mehrparteien]
VII.  Schnittstellen                     NIS2 [ja/nein] ·
                                         Produkthaftung ab 09.12.2026 [Risiko]
                                         Lieferkette / Zulieferzusagen […]
VIII. Sanktionsrisiko (Art. 64 CRA)      [bis 15 Mio. EUR / 2,5 %]

Risikoeinstufung: 🟢 / 🟡 / 🔴
Empfehlung: <…>
Nächste Schritte: <…>
```

## Risiken / typische Fehler

- **Keine veröffentlichte CVD-Policy** — Anhang I Teil II verlangt Erlass, Durchsetzung **und** öffentliche Zugänglichkeit. Eine interne Richtlinie genügt nicht.
- **Melder juristisch bedroht** — die Abwehrreaktion gegenüber einem gutgläubigen Sicherheitsforscher führt regelmäßig zur unkoordinierten Veröffentlichung und verkürzt die eigene Reaktionszeit auf null. Safe-Harbour-Zusage aufnehmen.
- **Triage wartet auf den Patch** — die Entscheidung über die **aktive Ausnutzung** und damit über die 24-Stunden-Frist des Art. 14 CRA ist von der Patch-Entwicklung zu entkoppeln.
- **Zeitpunkt der Update-Bereitstellung nicht dokumentiert** — er löst die **14-Tage-Frist** für den Abschlussbericht aus; ohne Dokumentation ist die Fristwahrung nicht belegbar.
- **Nur den vorgesehenen Meldekanal überwacht** — Schwachstellenmeldungen kommen über Support, Vertrieb, soziale Netze und Lieferanten. Alle Kanäle sind zu bündeln.
- **Ohne SBOM triagiert** — die Betroffenheitsfrage ist dann nicht binnen Stunden beantwortbar, und die 24-Stunden-Frist ist strukturell nicht haltbar.
- **Upstream-Fix abgewartet** — bei Schwachstellen in quelloffenen Fremdkomponenten bleibt der Hersteller gegenüber seinen Nutzern verantwortlich; erforderlichenfalls ist selbst zu patchen oder zu mitigieren.
- **Offenlegung dauerhaft verzögert** — die Verzögerung ist eine begründungsbedürftige Ausnahme, kein Instrument der Reputationssteuerung.
- **Advisory ohne Handlungsanweisung** — die Offenlegung muss Nutzern konkret sagen, wie sie die Schwachstelle beheben.
- **Meldung mit Behebung verwechselt** — die Behördenmeldung nach Art. 14 CRA erfüllt die Behebungspflicht nach Anhang I Teil II nicht, und umgekehrt.
- **Produkthaftung ab 09.12.2026 nicht mitgedacht** — ein unterlassenes Sicherheitsupdate innerhalb des Unterstützungszeitraums kann als Produktfehler zu bewerten sein; die CRA-Dokumentation ist beweisfest zu führen.
- **Zulieferzusagen kürzer als der eigene Unterstützungszeitraum** — die Patch-Verfügbarkeit ist vertraglich in die Lieferkette durchzureichen.
- **⚠️ Artikel- und Anhangnummern ungeprüft übernommen** — mehrere Angaben sind `[unverifiziert - prüfen]` und vor mandantengerichteter Verwendung am Amtsblatttext der VO (EU) 2024/2847 zu verifizieren.
