---
name: cra-anwendungsbereich-borghei
title: /cyber-resilience-act:cra-anwendungsbereich
description: Prüfung, ob ein Produkt in den Anwendungsbereich des Cyber Resilience Act fällt – Produkt mit digitalen Elementen (Art. 3 CRA), Bereichsausnahmen nach Art. 2 CRA (Medizinprodukte, Kraftfahrzeuge, Luftfahrt, Schiffsausrüstung, Verteidigung), Rollenbestimmung als Hersteller, Einführer oder Händler, Verwalter quelloffener Software nach Art. 24 CRA sowie Einstufung als wichtiges Produkt nach Anhang III oder kritisches Produkt nach Anhang IV. Use when ein Unternehmen sein Produktportfolio gegen die VO (EU) 2024/2847 abgleichen, ein CRA-Produktinventar aufbauen oder vor dem 11.09.2026 klären muss, welche Produkte und welche Rolle die Melde- und Herstellerpflichten auslösen.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/cyber-resilience-act/skills/cra-anwendungsbereich
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: cybersecurity
language: de
---

# /cyber-resilience-act:cra-anwendungsbereich

## Zweck

Der Cyber Resilience Act ([VO (EU) 2024/2847](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R2847)) erfasst horizontal alle **Produkte mit digitalen Elementen**, die auf dem Unionsmarkt bereitgestellt werden. Ob ein Produkt erfasst ist, welche Rolle der Mandant einnimmt und in welche Wichtigkeitsklasse das Produkt fällt, entscheidet über das gesamte Pflichtenprogramm — von der Meldepflicht ab dem 11.09.2026 bis zum Konformitätsbewertungsweg ab dem 11.12.2027. Dieser Skill führt die Eingangsprüfung durch und liefert das CRA-Produktinventar.

> **⚠️ Aktualität (Stand 2026-07):** Die Verordnung ist am **10.12.2024 in Kraft** getreten und gilt gestaffelt. Seit dem **11.06.2026** gelten die Vorschriften über Konformitätsbewertungsstellen und notifizierte Stellen. Ab dem **11.09.2026** — in sieben Wochen — greifen die **Meldepflichten** für aktiv ausgenutzte Schwachstellen und schwerwiegende Sicherheitsvorfälle. Erst ab dem **11.12.2027** gilt die Verordnung vollständig, einschließlich der grundlegenden Cybersicherheitsanforderungen, der CE-Kennzeichnung, der Konformitätsbewertung und der technischen Dokumentation.
>
> **Praktische Folge der Staffelung:** Wer das Produktinventar erst 2027 aufbaut, ist bereits bei der Meldepflicht in der Pflichtverletzung. Die Meldepflicht knüpft an das Produkt an — ohne belastbares Inventar ist im Ernstfall nicht in 24 Stunden feststellbar, ob überhaupt gemeldet werden muss.
>
> **Sanktionsrahmen:** Für Verstöße gegen die grundlegenden Cybersicherheitsanforderungen und die zentralen Hersteller- und Meldepflichten **bis zu 15 Mio. EUR oder 2,5 % des weltweiten Jahresumsatzes**, je nachdem, welcher Betrag höher ist (Art. 64 CRA).

## Eingaben

- Produktliste des Mandanten mit technischer Kurzbeschreibung (Hardware, Software, eingebettete Systeme, Firmware)
- Vertriebsweg und Marktzugang (Eigenentwicklung, Zukauf, White Label, Import aus Drittstaat, reiner Weiterverkauf)
- Marke, unter der das Produkt bereitgestellt wird, und Sitz der Rechtsträger
- Verwendete Fremdkomponenten, insbesondere quelloffene Software und deren Herkunft
- Bestehende sektorale Zulassungen oder Konformitätsbewertungen (MDR, Typgenehmigung, Luftfahrtzulassung, Funkanlagenrecht)
- Geplante oder erfolgte Bereitstellung auf dem Unionsmarkt und deren Zeitpunkt
- Angaben zu Fernverarbeitungslösungen, die für die Funktion des Produkts erforderlich sind

## Sub-Agent-Architektur

Drei gedankliche Rollen strukturieren die Analyse. Ein **Scope-Prüfer** klärt, ob überhaupt ein Produkt mit digitalen Elementen im Sinne des Art. 3 CRA vorliegt und ob eine Bereichsausnahme nach Art. 2 CRA greift; er entscheidet zuerst, denn ohne Anwendungsbereich entfällt jede weitere Prüfung. Ein **Rollen-Analyst** bestimmt anschließend, ob der Mandant Hersteller, Bevollmächtigter, Einführer, Händler oder Verwalter quelloffener Software ist, und prüft insbesondere den Rollenwechsel bei Eigenmarke und wesentlicher Veränderung. Ein **Klassifizierungs-Prüfer** ordnet das Produkt sodann der Standardkategorie, den wichtigen Produkten nach Anhang III oder den kritischen Produkten nach Anhang IV zu und leitet daraus den zulässigen Konformitätsbewertungsweg ab. Das Ergebnis der drei Rollen wird in einem einzigen Produktinventar zusammengeführt, das je Produkt Rolle, Klasse, Fristen und Verantwortlichen ausweist.

## Ablauf

### 1. Produkt mit digitalen Elementen? ([Art. 3 CRA](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R2847))

Erfasst ist jedes Software- oder Hardwareprodukt einschließlich seiner Datenfernverarbeitungslösungen, dessen bestimmungsgemäße oder vernünftigerweise vorhersehbare Verwendung eine **direkte oder indirekte Daten­verbindung** zu einem Gerät oder Netz umfasst.

Typische erfasste **Hardware**: Smartphones, Laptops, Smartwatches, Smart-Home-Geräte, Firewalls, Router, Mikroprozessoren, intelligente Messsysteme (Smart Meter). Typische erfasste **Software**: Buchhaltungssoftware, mobile Anwendungen, Computerspiele, Betriebssysteme, Bibliotheken. Der CRA unterscheidet **nicht** zwischen B2B und Verbrauchergeschäft; beide sind erfasst.

Prüfschritte:

a) Enthält das Produkt digitale Elemente (Software oder Firmware), die eigenständig oder eingebettet arbeiten?
b) Besteht eine Datenverbindung — auch mittelbar über ein anderes Gerät oder eine Cloud?
c) Gehört eine **Fernverarbeitungslösung** funktional zum Produkt, sodass das Produkt ohne sie seine Funktion nicht erfüllt? Dann ist sie mitzuprüfen.
d) Wird das Produkt **entgeltlich oder unentgeltlich** im Rahmen einer **Geschäftstätigkeit** auf dem Unionsmarkt bereitgestellt? Unentgeltlichkeit allein befreit nicht.

### 2. Bereichsausnahmen prüfen ([Art. 2 CRA](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R2847))

Ausgenommen sind Produkte, die bereits durch spezielle Unionsrechtsakte gleichwertig geregelt sind, insbesondere:

- **Medizinprodukte und In-vitro-Diagnostika** nach der MDR bzw. IVDR
- **Kraftfahrzeuge** und ihre Systeme nach dem unionalen Typgenehmigungsrecht
- **Zivile Luftfahrt** nach dem einschlägigen Unionsrecht
- **Schiffsausrüstung** nach der Schiffsausrüstungsrichtlinie
- Produkte, die **ausschließlich für Zwecke der nationalen Sicherheit, der Verteidigung oder zur Verarbeitung von Verschlusssachen** entwickelt wurden

`[unverifiziert - prüfen]` Der genaue Zuschnitt der Ausnahmen und die Behandlung von Ersatzteilen sowie von Produkten, die zugleich Hochrisiko-KI-Systeme nach der KI-VO sind, ist am Amtsblatttext des Art. 2 CRA zu verifizieren. Sektorale Zulassung ist **kein** pauschaler Freibrief: Sie befreit nur, soweit die Ausnahme reicht.

Zu dokumentieren ist die Ausnahme **produktbezogen mit Begründung**, nicht pauschal für ein Portfolio.

### 3. Rolle bestimmen ([Art. 13 CRA](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R2847))

| Rolle | Merkmal | Kernpflichten |
|---|---|---|
| **Hersteller** | entwickelt oder lässt entwickeln und vermarktet unter eigenem Namen oder eigener Marke | volles Pflichtenprogramm einschließlich Meldepflicht nach Art. 14 CRA |
| **Bevollmächtigter** | schriftlich beauftragter Vertreter eines Herstellers in der Union | vertraglich übertragene Pflichten, insbesondere Dokumentation und Behördenkontakt |
| **Einführer** | bringt ein Produkt aus einem Drittstaat erstmals auf den Unionsmarkt | Prüf- und Vergewisserungspflichten; Handeln bei Nichtkonformität |
| **Händler** | stellt bereit, ohne Hersteller oder Einführer zu sein | Sorgfaltspflichten; Unterrichtung bei bekannten Risiken |
| **Verwalter quelloffener Software** | unterstützt die Entwicklung freier und quelloffener Software im Rahmen einer Geschäftstätigkeit nachhaltig | abgeschwächtes, eigenes Pflichtenregime (siehe Schritt 4) |

**Rollenwechsel:** Wer ein Produkt unter eigenem Namen oder eigener Marke bereitstellt oder es **wesentlich verändert**, gilt als Hersteller mit dem vollen Pflichtenprogramm. White-Label-Bezug, OEM-Konstellationen, Rebranding und tiefgreifende Firmware-Anpassungen sind die praktisch häufigsten Auslöser. `[unverifiziert - prüfen]` Fundstelle für den Rollenwechsel ist Art. 22 CRA.

### 4. Verwalter quelloffener Software ([Art. 24 CRA](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R2847))

Der CRA schafft für **Open-Source-Stewards** eine eigene, leichtere Kategorie. Erfasst sind juristische Personen, die die Entwicklung freier und quelloffener Software, die für kommerzielle Tätigkeiten bestimmt ist, nachhaltig unterstützen — typischerweise Stiftungen und Foundations.

Abgrenzung:

- **Nicht erfasst:** rein private oder nichtkommerzielle Beitragende ohne Geschäftstätigkeit
- **Verwalter quelloffener Software:** eigenes, reduziertes Regime (Cybersicherheitspolitik, Zusammenarbeit mit Marktüberwachungsbehörden, Meldung nach Maßgabe des Art. 14 CRA)
- **Voller Hersteller:** wer quelloffene Software **monetarisiert** und als Produkt am Markt bereitstellt — die Open-Source-Herkunft befreit dann nicht

Für Unternehmen ist die praktisch wichtigere Frage die **Gegenrichtung**: Wer quelloffene Komponenten in sein Produkt integriert, ist für diese Komponenten als Hersteller verantwortlich. Die Verantwortung wandert nicht mit der Lizenz zum Upstream-Projekt.

### 5. Einstufung nach Wichtigkeitsklassen ([Anhang III und Anhang IV CRA](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R2847))

Der CRA kennt drei Stufen:

- **Standardprodukte** — die große Mehrheit; Konformitätsbewertung grundsätzlich durch interne Kontrolle
- **Wichtige Produkte nach Anhang III**, gegliedert in **Klasse I** und **Klasse II** — Produkte mit erhöhter Cybersicherheitsrelevanz wie Identitäts- und Zugriffsverwaltung, Passwortmanager, Netzwerkschnittstellen, Betriebssysteme, Router, Firewalls, Mikroprozessoren mit sicherheitsbezogenen Funktionen. Klasse II unterliegt dem strengeren Bewertungsweg
- **Kritische Produkte nach Anhang IV** — die kleinste Gruppe mit dem höchsten Anforderungsniveau; für sie kann eine europäische Cybersicherheitszertifizierung verlangt werden

Die Einstufung ist **produkt-, nicht unternehmensbezogen** und je Produkt schriftlich zu begründen. Sie steuert unmittelbar, ob eine notifizierte Stelle einzuschalten ist — und damit die Vorlaufzeit vor dem 11.12.2027.

### 6. Zeitschiene und Bestandsprodukte ([Art. 71 CRA](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R2847))

| Datum | Was gilt |
|---|---|
| 10.12.2024 | Inkrafttreten |
| 11.06.2026 | Vorschriften über Konformitätsbewertungsstellen und notifizierte Stellen |
| **11.09.2026** | **Meldepflichten nach Art. 14 CRA** — 24 Stunden / 72 Stunden / Abschlussbericht |
| 11.12.2027 | vollständige Geltung: grundlegende Anforderungen, CE-Kennzeichnung, Konformitätsbewertung, technische Dokumentation |

Für das Inventar folgt daraus eine **doppelte Zeitachse**: Meldefähigkeit muss zum 11.09.2026 stehen, Konformität zum 11.12.2027. `[unverifiziert - prüfen]` Die Behandlung von Produkten, die vor dem 11.12.2027 in Verkehr gebracht wurden, sowie die Reichweite der Übergangsregelung für wesentliche Änderungen sind am Amtsblatttext zu verifizieren.

### 7. Produktinventar, Zuständigkeiten und deutsche Behördenschnittstelle ([Art. 52 CRA](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R2847))

Ergebnis der Prüfung ist ein **CRA-Produktinventar**, das je Produkt ausweist: Bezeichnung und Version, erfasst ja/nein mit Begründung, Rolle, Klasse nach Anhang III/IV, Unterstützungszeitraum, verantwortliche Person, Meldeweg und Fristen.

Deutsche Schnittstelle ist das **BSI** ([bsi.bund.de](https://www.bsi.bund.de/)). `[unverifiziert - prüfen]` Zur Verzahnung mit der KI-VO: Nach dem KI-MIG ist das BSI notifizierende Behörde für Anhang III Nr. 1 der KI-VO (Biometrie) **nur übergangsweise**, bis die Marktüberwachungsbehörde nach **Art. 52 Abs. 2 CRA** benannt ist; wegen **Art. 52 Abs. 14 CRA** nimmt die nach der KI-VO zuständige Behörde bei überschneidenden Produkten zugleich die CRA-Marktüberwachungsaufgaben wahr. Beide Aussagen sind vor mandantengerichteter Verwendung am promulgierten Gesetzestext und am Amtsblatttext zu prüfen.

## Quellen

### Statute

- [VO (EU) 2024/2847 (Cyber Resilience Act)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R2847) — Volltext mit Anhängen
- Art. 2 CRA (Anwendungsbereich und Ausschlüsse), Art. 3 CRA (Begriffsbestimmungen), Art. 13 CRA (Pflichten der Hersteller), Art. 14 CRA (Meldepflichten), Art. 22 CRA (Rollenwechsel) `[unverifiziert - prüfen]`, Art. 24 CRA (Verwalter quelloffener Software) `[unverifiziert - prüfen]`, Art. 52 CRA (Marktüberwachung), Art. 64 CRA (Sanktionen), Art. 71 CRA (Inkrafttreten und Geltung) `[unverifiziert - prüfen]`
- Anhang III CRA (wichtige Produkte, Klasse I und II), Anhang IV CRA (kritische Produkte), Anhang I CRA (grundlegende Anforderungen)
- [RL (EU) 2022/2555 (NIS2)](https://eur-lex.europa.eu/eli/dir/2022/2555/oj) — Abgrenzung einrichtungsbezogener Pflichten
- [VO (EU) 2024/1689 (KI-VO)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R1689) — Überschneidung bei Hochrisiko-KI-Systemen

### Leitlinien

- [Europäische Kommission, Cyber Resilience Act — Politikseite und FAQ zur Umsetzung](https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act)
- [BSI — Umsetzung des Cyber Resilience Act in Deutschland](https://www.bsi.bund.de/)
- ENISA, Veröffentlichungen zur Umsetzung des CRA

**Rechtsprechung:** Zum Cyber Resilience Act ist **keine Rechtsprechung ersichtlich** (Stand 07/2026). Die materiellen Pflichten gelten überwiegend erst ab dem 11.12.2027. Entscheidungen zu Produktsicherheits- und Produkthaftungsrecht sind allenfalls analog heranzuziehen und ausdrücklich als Analogie zu kennzeichnen.

## Ausgabeformat

```
CRA-ANWENDUNGSBEREICH — PRÜFUNG — <Produkt> — <Datum>

I.    Produkt mit digitalen Elementen?     [ja / nein — Begründung, Art. 3 CRA]
      Fernverarbeitungslösung erfasst?     [ja / nein]
II.   Bereichsausnahme (Art. 2 CRA)        [keine / MDR / Kfz / Luftfahrt / … ]
III.  Rolle                                [Hersteller / Bevollmächtigter /
                                            Einführer / Händler / OSS-Verwalter]
      Rollenwechsel geprüft                [Eigenmarke / wesentliche Änderung]
IV.   Einstufung                           [Standard / Anhang III Klasse I /
                                            Anhang III Klasse II / Anhang IV]
      Konformitätsbewertungsweg            [interne Kontrolle / notifizierte Stelle]
V.    Quelloffene Komponenten              [Liste / Verantwortung beim Mandanten]
VI.   Fristen                              11.09.2026 Meldepflichten
                                           11.12.2027 vollständige Geltung
VII.  Deutsche Behördenschnittstelle       [BSI — Zuständigkeit prüfen]
VIII. Sanktionsrisiko (Art. 64 CRA)        [bis 15 Mio. EUR / 2,5 %]

Risikoeinstufung: 🟢 / 🟡 / 🔴
Empfehlung: <…>
Nächste Schritte: <…>
```

## Risiken / typische Fehler

- **Inventar zu spät aufgebaut** — die Meldepflicht gilt ab **11.09.2026**, nicht erst ab 11.12.2027. Ohne Produktinventar ist im Vorfall nicht binnen 24 Stunden feststellbar, ob eine Meldepflicht besteht.
- **Software unterschätzt** — reine Software ist Produkt mit digitalen Elementen. Buchhaltungssoftware, Apps und Spiele sind erfasst; die Vorstellung, der CRA betreffe nur Hardware, ist der häufigste Anwendungsfehler.
- **Bereichsausnahme pauschal angenommen** — eine sektorale Zulassung nach MDR oder Typgenehmigungsrecht befreit nur, soweit die Ausnahme des Art. 2 CRA reicht, und ist produktbezogen zu begründen.
- **Rollenwechsel übersehen** — White Label, Rebranding und wesentliche Firmware-Änderungen machen Händler und Einführer zum Hersteller mit vollem Pflichtenprogramm einschließlich Meldepflicht.
- **Open-Source-Herkunft als Befreiung missverstanden** — wer quelloffene Komponenten in ein vermarktetes Produkt integriert, haftet dafür als Hersteller. Art. 24 CRA entlastet den Verwalter, nicht den Integrator.
- **Fernverarbeitungslösung ausgeklammert** — funktional notwendige Cloud-Bestandteile gehören zum Produkt und sind mitzuprüfen.
- **Einstufung nach Anhang III nicht begründet** — die Klassenzuordnung steuert den Konformitätsbewertungsweg. Eine unbegründete Einstufung als Standardprodukt kostet im Zweifel die gesamte Vorlaufzeit zur notifizierten Stelle.
- **Unternehmensbezogene statt produktbezogene Prüfung** — der CRA knüpft am Produkt an, NIS2 an der Einrichtung. Beide Prüfungen sind getrennt zu führen.
- **Sanktionsrahmen verwechselt** — Art. 64 CRA sieht bis zu **15 Mio. EUR oder 2,5 %** vor; die Rahmen von KI-VO (3 %) und NIS2 weichen ab.
- **⚠️ Artikelnummern ungeprüft übernommen** — die hier genannten Nummern sind teils `[unverifiziert - prüfen]` und vor mandantengerichteter Verwendung am Amtsblatttext der VO (EU) 2024/2847 zu verifizieren.
