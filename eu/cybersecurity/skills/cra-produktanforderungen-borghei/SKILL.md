---
name: cra-produktanforderungen-borghei
title: /cyber-resilience-act:cra-produktanforderungen
description: Bestimmung der grundlegenden Cybersicherheitsanforderungen nach Anhang I VO (EU) 2024/2847 – Sicherheitseigenschaften des Produkts nach Anhang I Teil I, Anforderungen an die Schwachstellenbehandlung nach Anhang I Teil II, Cybersicherheits-Risikobewertung nach Art. 13 CRA, Software-Stückliste (SBOM), Unterstützungszeitraum und unentgeltliche Sicherheitsupdates, Wahl des Konformitätsbewertungsverfahrens nach Anhang VIII, technische Dokumentation nach Anhang VII, EU-Konformitätserklärung und CE-Kennzeichnung. Use when ein Hersteller vor dem 11.12.2027 eine Gap-Analyse gegen Anhang I durchführt, den Konformitätsbewertungsweg für ein Produkt festlegt oder die technische Dokumentation und die CE-Kennzeichnung vorbereitet.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/cyber-resilience-act/skills/cra-produktanforderungen
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: cybersecurity
language: de
---

# /cyber-resilience-act:cra-produktanforderungen

## Zweck

Ab dem **11.12.2027** darf ein Produkt mit digitalen Elementen nur noch auf dem Unionsmarkt bereitgestellt werden, wenn es die **grundlegenden Cybersicherheitsanforderungen des Anhang I** ([VO (EU) 2024/2847](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R2847)) erfüllt, ein Konformitätsbewertungsverfahren nach **Anhang VIII** durchlaufen hat, über eine technische Dokumentation nach **Anhang VII** verfügt und die **CE-Kennzeichnung** trägt. Dieser Skill führt die Gap-Analyse gegen Anhang I, bestimmt den zulässigen Bewertungsweg und plant die Vorlaufzeit — insbesondere dort, wo eine notifizierte Stelle einzuschalten ist.

> **⚠️ Aktualität (Stand 2026-07):** Die Verordnung ist am **10.12.2024 in Kraft** getreten. Seit dem **11.06.2026** gelten die Vorschriften über Konformitätsbewertungsstellen und notifizierte Stellen — die Infrastruktur für die Bewertung baut sich also gerade erst auf. Ab dem **11.09.2026** greifen die **Meldepflichten** nach Art. 14 CRA. Die hier behandelten materiellen Produktanforderungen gelten ab dem **11.12.2027**.
>
> **Die Reihenfolge täuscht.** Dass die Produktanforderungen zuletzt greifen, macht sie nicht zum letzten Arbeitspaket: Für wichtige Produkte der Klasse II und für kritische Produkte nach Anhang IV ist eine notifizierte Stelle einzuschalten, deren Kapazität begrenzt und deren Vorlaufzeit erheblich ist. Wer 2027 mit der Terminsuche beginnt, verfehlt den Stichtag.
>
> **Harmonisierte Normen:** Der Normungsauftrag zum CRA läuft. `[unverifiziert - prüfen]` Zum Stand 07/2026 ist der Zitierungsstand harmonisierter Normen im Amtsblatt zu verifizieren; ohne Amtsblatt-Zitierung besteht **keine Konformitätsvermutung**. Bestehende Zertifizierungen nach ISO/IEC 27001 oder IEC 62443 sind wiederverwendbare Vorarbeit, aber **kein Konformitätsnachweis** nach dem CRA.
>
> **Sanktionsrahmen:** Verstöße gegen die grundlegenden Cybersicherheitsanforderungen sind mit **bis zu 15 Mio. EUR oder 2,5 % des weltweiten Jahresumsatzes** bewehrt, je nachdem, welcher Betrag höher ist (Art. 64 CRA).

## Eingaben

- Produkt, Version, Architektur und Einsatzkontext; Abgrenzung des Produkts einschließlich Fernverarbeitungslösungen
- CRA-Einstufung aus dem Produktinventar: Standard, wichtiges Produkt Anhang III Klasse I oder II, kritisches Produkt Anhang IV
- Vorhandene Risikobewertung, Bedrohungsmodell und Sicherheitsarchitektur
- Bestandsaufnahme der Fremd- und quelloffenen Komponenten samt Versionen und Lizenzen
- Bestehende Zertifizierungen und Prüfberichte (ISO/IEC 27001, IEC 62443, Common Criteria, Penetrationstests)
- Geplanter **Unterstützungszeitraum** und Update-Infrastruktur (Signatur, Verteilung, Rollback)
- Bestehende Nutzerdokumentation, Sicherheitshinweise, Konfigurationsanleitungen
- Zeitplan bis zum 11.12.2027 und verfügbare interne Kapazität

## Sub-Agent-Architektur

Drei gedankliche Rollen strukturieren die Analyse. Ein **Anforderungs-Analyst** übersetzt Anhang I Teil I und Teil II in eine produktspezifische Anforderungsliste und markiert je Anforderung, ob sie erfüllt, teilweise erfüllt oder offen ist; er stützt sich dabei zwingend auf die Cybersicherheits-Risikobewertung, denn Anhang I gilt **nach Maßgabe des Risikos** und nicht schematisch. Ein **Konformitäts-Architekt** leitet aus der Einstufung nach Anhang III/IV den zulässigen Bewertungsweg nach Anhang VIII ab, prüft die Verfügbarkeit harmonisierter Normen und plant die Einschaltung einer notifizierten Stelle rückwärts vom 11.12.2027. Ein **Dokumentations-Prüfer** stellt die technische Dokumentation nach Anhang VII, die EU-Konformitätserklärung und die Nutzerinformationen zusammen und prüft sie auf Vollständigkeit. Der Anforderungs-Analyst liefert die Grundlage; die beiden anderen Rollen bauen darauf auf.

## Ablauf

### 1. Cybersicherheits-Risikobewertung als Grundlage ([Art. 13 CRA](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R2847))

Der CRA verlangt keine schematische Erfüllung eines Katalogs, sondern die Erfüllung der Anforderungen **auf Grundlage einer Cybersicherheits-Risikobewertung** des konkreten Produkts. Diese Bewertung ist der Anker der gesamten Compliance:

- Sie erfasst bestimmungsgemäße Verwendung **und vernünftigerweise vorhersehbare Fehlanwendung**
- Sie identifiziert Bedrohungen, Angriffsflächen, Schutzziele und Restrisiken
- Sie begründet, welche Anforderungen des Anhang I Teil I in welcher Tiefe anwendbar sind und welche produktbedingt nicht einschlägig sind
- Sie ist **Bestandteil der technischen Dokumentation** nach Anhang VII und über den gesamten Unterstützungszeitraum fortzuschreiben

Eine Anforderung als „nicht anwendbar" zu führen, ist zulässig — aber nur mit dokumentierter Begründung aus der Risikobewertung.

### 2. Anhang I Teil I — Cybersicherheitseigenschaften des Produkts ([Anhang I CRA](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R2847))

Produkte sind so zu konzipieren, zu entwickeln und herzustellen, dass sie **ein dem Risiko angemessenes Cybersicherheitsniveau** gewährleisten und **ohne bekannte ausnutzbare Schwachstellen** bereitgestellt werden. Der Katalog des Anhang I Teil I umfasst insbesondere:

- Bereitstellung mit einer **sicheren Standardkonfiguration** einschließlich der Möglichkeit, den Auslieferungszustand wiederherzustellen
- Schutz vor unbefugtem Zugriff durch geeignete **Authentifizierungs-, Identitäts- und Zugriffsverwaltung**, einschließlich Meldung fehlgeschlagener Zugriffsversuche
- **Vertraulichkeit** gespeicherter, übertragener und verarbeiteter Daten, insbesondere durch Verschlüsselung nach dem Stand der Technik
- **Integrität** von Daten, Befehlen, Programmen und Konfiguration; Meldung unbefugter Veränderungen
- **Datenminimierung** — Verarbeitung nur der für den Zweck erforderlichen Daten
- Schutz der **Verfügbarkeit** wesentlicher Funktionen, auch nach einem Vorfall, sowie Resilienz gegen Überlastungsangriffe
- **Minimierung der Angriffsfläche**, einschließlich externer Schnittstellen
- **Begrenzung von Schadwirkungen** durch Isolierungs- und Segmentierungsmechanismen
- Bereitstellung von **Aufzeichnungs- und Überwachungsfunktionen** (Protokollierung sicherheitsrelevanter Ereignisse), die vom Nutzer aktivierbar sind
- Möglichkeit, Daten und Konfiguration **sicher und vollständig zu löschen und zu übertragen**
- Bereitstellung von **Sicherheitsupdates**, soweit technisch möglich getrennt von Funktionsupdates und mit der Option automatischer Installation nebst Abschaltmöglichkeit

`[unverifiziert - prüfen]` Die genaue Nummerierung und der abschließende Wortlaut der einzelnen Anforderungen sind am Amtsblatttext des Anhang I Teil I zu verifizieren.

### 3. Anhang I Teil II — Anforderungen an die Schwachstellenbehandlung ([Anhang I CRA](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R2847))

Teil II verpflichtet den Hersteller über den gesamten **Unterstützungszeitraum** zu einem funktionierenden Schwachstellenmanagement:

- Schwachstellen und Komponenten **identifizieren und dokumentieren**, einschließlich einer **Software-Stückliste (SBOM)** mindestens für die obersten Abhängigkeiten
- Schwachstellen **unverzüglich beheben**, insbesondere durch Sicherheitsupdates
- **Regelmäßige Tests und Überprüfungen** der Produktsicherheit
- Nach Bereitstellung eines Updates: Informationen über behobene Schwachstellen **öffentlich offenlegen**, mit Beschreibung, Auswirkungen, Schweregrad und Hinweisen zur Behebung
- **Koordinierte Schwachstellenoffenlegung**: Politik durchsetzen und veröffentlichen
- Maßnahmen zur **Erleichterung des Meldens** von Schwachstellen, einschließlich einer Kontaktadresse
- Mechanismen zur **sicheren Verteilung** von Updates, einschließlich Signatur und Integritätsprüfung
- Sicherheitsupdates **unverzüglich und unentgeltlich** bereitstellen, nebst Hinweisen für Nutzer

Die operative Umsetzung behandelt der Skill `cra-schwachstellenmanagement`.

### 4. Software-Stückliste (SBOM) ([Anhang I Teil II CRA](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R2847))

Die **SBOM** ist die praktische Voraussetzung dafür, im Vorfall binnen 24 Stunden beurteilen zu können, ob ein Produkt betroffen ist. Sie verbindet damit die Produktanforderungen unmittelbar mit der Meldepflicht nach Art. 14 CRA.

Anforderungen an die Führung:

- **Maschinenlesbares Format** (etwa SPDX oder CycloneDX), nicht Tabellen in Fließtext
- Mindestens die **obersten Abhängigkeiten**; tiefere Ebenen, soweit risikorelevant
- Je Komponente: Name, Version, Bezugsquelle, Lizenz, eindeutige Kennung
- **Automatisierte Erzeugung im Build-Prozess** statt manueller Pflege; jede ausgelieferte Version erhält ihre SBOM
- Abgleich gegen Schwachstellendatenbanken als laufender Prozess
- Aufbewahrung als Teil der technischen Dokumentation

Die SBOM muss nicht allgemein veröffentlicht werden; sie ist jedoch der Marktüberwachungsbehörde auf Verlangen vorzulegen.

### 5. Unterstützungszeitraum und Sicherheitsupdates ([Art. 13 CRA](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R2847))

Der Hersteller bestimmt den **Unterstützungszeitraum** anhand der erwarteten Nutzungsdauer des Produkts. `[unverifiziert - prüfen]` Der CRA sieht als Regelmaß einen Zeitraum von **mindestens fünf Jahren** vor, sofern die erwartete Nutzungsdauer nicht kürzer ist; die genaue Ausgestaltung ist am Amtsblatttext des Art. 13 CRA zu verifizieren.

Konsequenzen:

- Der Unterstützungszeitraum ist **vor der Bereitstellung** festzulegen, zu begründen und den Nutzern **klar und verständlich** mitzuteilen
- Während des Zeitraums sind Sicherheitsupdates **unverzüglich und unentgeltlich** bereitzustellen
- Sicherheitsupdates sind, soweit technisch möglich, **getrennt von Funktionsupdates** anzubieten; Nutzer dürfen nicht gezwungen werden, Funktionsänderungen zu akzeptieren, um sicher zu bleiben
- Nach Ablauf bereitgestellte Informationen über behobene Schwachstellen bleiben verfügbar zu halten
- Der Zeitraum ist vertraglich in die Lieferkette durchzureichen — sonst endet die Zulieferunterstützung vor der eigenen Pflicht

### 6. Konformitätsbewertung und harmonisierte Normen ([Anhang VIII CRA](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R2847))

Der zulässige Weg folgt der Einstufung aus dem Produktinventar:

| Einstufung | Zulässige Verfahren nach Anhang VIII |
|---|---|
| **Standardprodukt** | interne Kontrolle (Modul A) — Eigenverantwortung des Herstellers |
| **Anhang III Klasse I** | interne Kontrolle, **wenn** eine harmonisierte Norm vollständig angewandt wird; sonst Einschaltung einer notifizierten Stelle |
| **Anhang III Klasse II** | Einschaltung einer **notifizierten Stelle** (EU-Baumusterprüfung Modul B + C oder umfassende Qualitätssicherung Modul H) |
| **Anhang IV (kritisch)** | höchstes Niveau; ggf. europäische Cybersicherheitszertifizierung |

`[unverifiziert - prüfen]` Die Zuordnung der Module zu den Klassen ist am Amtsblatttext des Anhang VIII zu verifizieren.

Planung rückwärts vom **11.12.2027**: Auswahl der notifizierten Stelle, Kapazitätsanfrage, Vorbereitung der technischen Dokumentation, Bewertung, Nachbesserung, Ausstellung. Wo eine notifizierte Stelle erforderlich ist, ist der Termin **jetzt** zu sichern; die Benennung notifizierter Stellen läuft erst seit dem 11.06.2026.

### 7. Technische Dokumentation, Konformitätserklärung und CE-Kennzeichnung ([Anhang VII CRA](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R2847))

**Technische Dokumentation (Anhang VII)** — vor der Bereitstellung zu erstellen, während des Unterstützungszeitraums fortzuschreiben und nach dem Inverkehrbringen mindestens zehn Jahre bzw. für die Dauer des Unterstützungszeitraums aufzubewahren, je nachdem, welcher Zeitraum länger ist. `[unverifiziert - prüfen]` Aufbewahrungsdauer am Amtsblatttext prüfen. Inhalt insbesondere:

- Allgemeine Produktbeschreibung, bestimmungsgemäße Verwendung, Versionen
- Beschreibung von Konzeption, Entwicklung und Herstellung einschließlich Architektur
- **Cybersicherheits-Risikobewertung** nach Art. 13 CRA
- Angewandte harmonisierte Normen oder sonstige technische Spezifikationen
- Prüfberichte zur Verifikation der Anforderungen des Anhang I
- Angaben zum **Unterstützungszeitraum** und zur Schwachstellenbehandlung
- SBOM und Angaben zu den Komponenten

**EU-Konformitätserklärung (Anhang V)** — der Hersteller erklärt die Erfüllung der grundlegenden Anforderungen und übernimmt damit die Verantwortung. Sie ist dem Produkt beizufügen oder bereitzustellen.

**CE-Kennzeichnung** — sichtbar, lesbar und dauerhaft anzubringen; bei Software auf der Begleitdokumentation oder in der Konformitätserklärung. Sie darf erst nach abgeschlossener Konformitätsbewertung angebracht werden.

**Nutzerinformationen (Anhang II)** — Kontaktstelle für Schwachstellenmeldungen, Angaben zum Unterstützungszeitraum, Hinweise zur sicheren Inbetriebnahme, Konfiguration und Außerbetriebnahme.

## Quellen

### Statute

- [VO (EU) 2024/2847 (Cyber Resilience Act)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R2847) — Volltext mit Anhängen
- Art. 13 CRA (Pflichten der Hersteller, Risikobewertung, Unterstützungszeitraum), Art. 14 CRA (Meldepflichten), Art. 52 CRA (Marktüberwachung), Art. 64 CRA (Sanktionen)
- Anhang I Teil I CRA (Cybersicherheitseigenschaften), Anhang I Teil II CRA (Schwachstellenbehandlung), Anhang II CRA (Nutzerinformationen), Anhang III CRA (wichtige Produkte), Anhang IV CRA (kritische Produkte), Anhang V CRA (EU-Konformitätserklärung), Anhang VII CRA (technische Dokumentation), Anhang VIII CRA (Konformitätsbewertungsverfahren)
- [VO (EU) 2019/881 (Cybersecurity Act)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019R0881) — europäische Cybersicherheitszertifizierung

### Leitlinien

- [Europäische Kommission, Cyber Resilience Act — Politikseite und FAQ zur Umsetzung](https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act)
- [BSI — technische Richtlinien und Umsetzungshinweise](https://www.bsi.bund.de/)
- CEN/CENELEC JTC 13 — Normungsauftrag zu den harmonisierten Normen unter dem CRA
- ISO/IEC 29147 und ISO/IEC 30111 als Referenzrahmen; IEC 62443 für industrielle Produkte

**Rechtsprechung:** Zum Cyber Resilience Act ist **keine Rechtsprechung ersichtlich** (Stand 07/2026); die materiellen Anforderungen gelten erst ab dem 11.12.2027. Entscheidungen zum CE-Produktsicherheitsrecht sind allenfalls analog heranzuziehen und ausdrücklich als Analogie zu kennzeichnen.

## Ausgabeformat

```
CRA-PRODUKTANFORDERUNGEN — GAP-ANALYSE — <Produkt/Version> — <Datum>

I.    Einstufung                        [Standard / Anhang III Kl. I /
                                         Anhang III Kl. II / Anhang IV]
II.   Risikobewertung (Art. 13 CRA)     [vorhanden / Lücke — <…>]
III.  Anhang I Teil I — Eigenschaften
      Sichere Standardkonfiguration     [erfüllt / teilweise / offen]
      Zugriffsschutz / Authentifizierung[…]
      Vertraulichkeit / Integrität      […]
      Angriffsflächenminimierung        […]
      Protokollierung                   […]
      Sichere Löschung / Übertragung    […]
      Update-Mechanismus                […]
IV.   Anhang I Teil II — Schwachstellen
      SBOM                              [Format, Tiefe, Automatisierung]
      Behebung / Tests / Offenlegung    […]
      CVD-Policy                        […]
      Sichere Update-Verteilung         […]
V.    Unterstützungszeitraum            [Dauer, Begründung, Kommunikation]
VI.   Konformitätsbewertung (Anhang VIII)[interne Kontrolle /
                                          notifizierte Stelle — Termin <…>]
      Harmonisierte Normen              [Zitierungsstand prüfen]
VII.  Dokumentation
      Technische Dokumentation (Anhang VII) […]
      EU-Konformitätserklärung (Anhang V)   […]
      Nutzerinformationen (Anhang II)       […]
      CE-Kennzeichnung                      […]
VIII. Fristen                           11.12.2027 vollständige Geltung
                                        11.09.2026 Meldepflichten
IX.   Sanktionsrisiko (Art. 64 CRA)     [bis 15 Mio. EUR / 2,5 %]

Risikoeinstufung: 🟢 / 🟡 / 🔴
Empfehlung: <…>
Nächste Schritte: <…>
```

## Risiken / typische Fehler

- **Anhang I schematisch abgearbeitet** — die Anforderungen gelten nach Maßgabe der **Cybersicherheits-Risikobewertung**. Ohne sie ist weder eine Erfüllung noch eine Nichtanwendbarkeit begründbar.
- **Notifizierte Stelle zu spät angefragt** — für **Anhang III Klasse II** und Anhang IV ist eine notifizierte Stelle einzuschalten; die Benennung dieser Stellen läuft erst seit dem 11.06.2026, die Kapazität ist knapp.
- **Harmonisierte Norm als vorhanden unterstellt** — eine Konformitätsvermutung entsteht nur aus im **Amtsblatt zitierten** Normen. ISO/IEC 27001 und IEC 62443 begründen sie nicht.
- **SBOM manuell gepflegt** — eine Tabelle ohne Build-Integration ist im Vorfall wertlos und verhindert die Betroffenheitsbeurteilung binnen 24 Stunden.
- **Unterstützungszeitraum nicht bestimmt oder nicht kommuniziert** — er ist vor der Bereitstellung festzulegen, zu begründen und den Nutzern mitzuteilen.
- **Zulieferer-Support kürzer als der eigene Unterstützungszeitraum** — der Zeitraum ist vertraglich in die Lieferkette durchzureichen.
- **Sicherheitsupdates mit Funktionsupdates gekoppelt** — sie sind, soweit technisch möglich, getrennt und **unentgeltlich** anzubieten.
- **Bereitstellung mit bekannter ausnutzbarer Schwachstelle** — Anhang I Teil I verlangt die Auslieferung **ohne bekannte ausnutzbare Schwachstellen**; ein bekanntes, ungepatchtes Risiko im Auslieferungsstand ist ein Kernverstoß.
- **CE-Kennzeichnung vor abgeschlossener Bewertung** angebracht — unzulässig und selbst sanktionsbewehrt.
- **Technische Dokumentation als Einmalprodukt** behandelt — sie ist über den Unterstützungszeitraum fortzuschreiben.
- **Fernverarbeitungslösung ausgeklammert** — funktional notwendige Cloud-Bestandteile gehören zum Produkt und unterliegen den Anforderungen.
- **⚠️ Anhang- und Artikelnummern ungeprüft übernommen** — mehrere Angaben sind hier `[unverifiziert - prüfen]` und vor mandantengerichteter Verwendung am Amtsblatttext der VO (EU) 2024/2847 zu verifizieren.
