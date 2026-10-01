---
name: gpai-pflichten-borghei
title: /ki-vo-compliance:gpai-pflichten
description: Prüfung der Pflichten von Anbietern von KI-Modellen mit allgemeinem Verwendungszweck (GPAI) nach Art. 53 KI-VO und der Zusatzpflichten bei systemischem Risiko Art. 55 KI-VO – technische Dokumentation, Urheberrechtsstrategie, Praxisleitfäden (Codes of Practice). Use when ein Anbieter eines GPAI-Modells (Foundation Model) seine Dokumentations-, Transparenz- und Risikopflichten nach der KI-VO bestimmen muss.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/ki-vo-compliance/skills/gpai-pflichten
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: regulatory
language: de
---

# /ki-vo-compliance:gpai-pflichten

## Zweck

KI-Modelle mit allgemeinem Verwendungszweck (General-Purpose AI, **GPAI**) unterliegen einem eigenen Pflichtenregime nach **Art. 53 KI-VO** ([VO (EU) 2024/1689](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R1689)); Modelle mit **systemischem Risiko** treffen zusätzlich die strengeren Pflichten nach **Art. 55 KI-VO**. Die Regeln gelten seit dem 2. August 2025 für neue Modelle. Dieser Skill bestimmt die Anbieterpflichten und prüft die Einstufung als systemisches Risiko.

> **⚠️ Durchsetzung ab 02.08.2026 (Stand 2026-07):** Die GPAI-Pflichten binden Anbieter zwar bereits seit **02.08.2025**, die **Durchsetzungs- und Bußgeldbefugnisse der Kommission** greifen jedoch erst ab dem **02.08.2026** (Art. 113). Das einjährige Schonjahr endet damit. Rahmen: **bis 15 Mio. EUR oder 3 % des weltweiten Jahresumsatzes** (Art. 101).
>
> **Der Digital Omnibus on AI hat die GPAI-Pflichten NICHT verschoben.** Verschoben wurden nur die Hochrisiko-Pflichten (Anhang III → 02.12.2027, Anhang I → 02.08.2028). Der GPAI-Zeitplan bleibt unverändert.
>
> **Altmodelle:** GPAI-Modelle, die **vor dem 02.08.2025** in Verkehr gebracht wurden, müssen Kapitel V erst **bis zum 02.08.2027** erfüllen (**Art. 111 Abs. 3**).

## Eingaben

- Modelltyp und Trainingsumfang (Rechenleistung in FLOP, Datenmenge, Modalitäten)
- Rolle des Mandanten (Anbieter des Modells, nachgelagerter Anbieter, Open-Source-Bereitsteller)
- Vertriebsweg (proprietär, frei lizenziert/Open Source)
- Verwendete Trainingsdaten (urheberrechtlich geschützte Inhalte? TDM-Vorbehalte?)
- Beitritt zu einem Praxisleitfaden (Code of Practice)?

## Sub-Agent-Architektur

Drei gedankliche Rollen strukturieren die Analyse. Ein **Einstufungs-Prüfer** klärt, ob ein GPAI-Modell vorliegt und ob es nach Art. 51 i.V.m. Art. 55 KI-VO als Modell mit systemischem Risiko gilt (Schwellenwert > 10^25 FLOP Trainingsrechenleistung). Ein **Dokumentations-Architekt** stellt die Informations-, Dokumentations- und Urheberrechtspflichten nach Art. 53 KI-VO und Anhang XI/XII zusammen. Ein **Risiko-Analyst** ergänzt bei systemischem Risiko die Zusatzpflichten nach Art. 55 KI-VO. Der Einstufungs-Prüfer entscheidet zuerst über die Modellkategorie, bevor die beiden anderen Rollen ihre Kataloge anwenden.

## Ablauf

### 1. Einordnung als GPAI-Modell

Ein GPAI-Modell zeigt **erhebliche allgemeine Verwendbarkeit** und kann ein breites Spektrum nachgelagerter Aufgaben erfüllen. Reine Forschungs-/Prototyp-Modelle vor Marktbereitstellung sind ausgenommen.

### 2. Grundpflichten aller GPAI-Anbieter (Art. 53 KI-VO)

a) **Technische Dokumentation** des Modells erstellen und aktuell halten (Trainings-/Testverfahren, Bewertungsergebnisse) — mindestens Inhalt nach **Anhang XI**, auf Anfrage an das KI-Büro/Behörden
b) **Informationen für nachgelagerte Anbieter** bereitstellen, die das Modell integrieren (Fähigkeiten und Grenzen) — Inhalt nach **Anhang XII**
c) **Urheberrechtsstrategie**: schriftliche Strategie zur Einhaltung des Unionsrechts, insbesondere zur Beachtung des Rechtsvorbehalts (TDM-Opt-out) nach der DSM-Richtlinie
d) **Zusammenfassung der Trainingsinhalte** öffentlich bereitstellen — die **Vorlage des KI-Büros vom 24.07.2025 ist verbindlich zu verwenden** (nebst Explanatory Notice). Verlangt werden: Art der Inhalte, wesentliche Datenquellen (einschließlich benannter großer öffentlicher Datensätze und, oberhalb einer Größenschwelle, der wichtigsten gecrawlten Domains), lizenzierte/Nutzer-/synthetische Daten sowie Erhebungs- und Verarbeitungsmethoden einschließlich der Maßnahmen zur Beachtung des TDM-Opt-outs. Die Zusammenfassung ist **alle 6 Monate oder bei wesentlicher Änderung fortzuschreiben**.

Für **freie und quelloffene** GPAI-Modelle entfallen nach **Art. 53 Abs. 2** die Pflichten lit. a und b, sofern das Modell unter einer Lizenz bereitgestellt wird, die Zugang, Änderung und Weiterverbreitung erlaubt und die Parameter öffentlich verfügbar sind. **Lit. c und d gelten uneingeschränkt weiter.** Bei systemischem Risiko entfällt die Ausnahme vollständig.

### 3. Modelle mit systemischem Risiko (Art. 55 KI-VO)

Einstufung bei Trainingsrechenleistung **> 10^25 FLOP** (Art. 51 Abs. 2 — widerlegliche Vermutung hoher Wirkfähigkeit) oder durch Benennung der Kommission von Amts wegen bzw. auf qualifizierte Warnung des wissenschaftlichen Gremiums (Art. 51 Abs. 1 lit. b, Kriterien Anhang XIII).

**Mitteilungspflicht Art. 52 Abs. 1:** Der Anbieter muss die Kommission **binnen zwei Wochen** unterrichten, sobald er die Schwelle erreicht oder weiß, dass er sie erreichen wird. Mit der Mitteilung kann er geltend machen, dass trotz Schwellenüberschreitung kein systemisches Risiko besteht.

Zusatzpflichten:

- **Modellbewertung** inkl. adversarialer Tests (Red-Teaming)
- **Bewertung und Minderung systemischer Risiken** auf Unionsebene
- **Meldung schwerwiegender Vorfälle** an das KI-Büro und nationale Behörden
- angemessenes Niveau an **Cybersicherheit** für Modell und physische Infrastruktur

### 4. Praxisleitfäden / Codes of Practice (Art. 56 KI-VO)

Bis zur Verfügbarkeit harmonisierter Normen können Anbieter die Einhaltung über **Praxisleitfäden (Codes of Practice)** nachweisen. Der **GPAI Code of Practice** wurde vom KI-Büro am **10.07.2025** in finaler Fassung veröffentlicht; die erste Unterzeichnerliste folgte am **01.08.2025**. Er gliedert sich in drei Kapitel: **Transparenz** und **Urheberrecht** (alle GPAI-Anbieter) sowie **Safety and Security** (nur Anbieter von Modellen mit systemischem Risiko).

Praxishinweise zur Unterzeichnung:

- Der Beitritt ist **freiwillig**; er begründet keine gesetzliche Konformitätsvermutung im Sinne des Art. 40, sondern erleichtert den Nachweis gegenüber dem KI-Büro.
- **Meta hat nicht unterzeichnet** — der Nachweis ist dort auf anderem Wege zu führen.
- **xAI** hat ausschließlich das Kapitel *Safety and Security* gezeichnet und muss Transparenz und Urheberrecht über „alternative adequate means" belegen.
- Eine **Teilzeichnung einzelner Kapitel ist möglich** und in der Beratung ausdrücklich zu adressieren.
- Die Kommission hat eine **Signatory Taskforce** zur Koordinierung des Compliance-Austauschs eingerichtet.

**Harmonisierte Normen:** Zum Stand 07/2026 ist **keine harmonisierte Norm zur KI-VO im Amtsblatt zitiert**. Nur **prEN 18286** (Qualitätsmanagementsystem, Art. 17) hat am 30.10.2025 die öffentliche Umfrage erreicht. Eine **ISO/IEC-42001-Zertifizierung begründet daher KEINE Konformitätsvermutung** — diese entsteht nach Art. 40 allein aus im Amtsblatt zitierten Normen. ISO/IEC 42001 ist wiederverwendbare Vorarbeit (prEN 18286 Anhang D enthält ein Mapping), kein Ersatz.

### 5. Sanktionen (Art. 101 KI-VO)

Gegen GPAI-Anbieter kann das KI-Büro Geldbußen bis **15 Mio. EUR oder 3 % des weltweiten Jahresumsatzes** verhängen.

## Risiken

- **Falsche Einstufung** — Überschreiten der 10^25-FLOP-Schwelle ohne Anerkennung des systemischen Risikos verletzt Art. 55 KI-VO.
- **Zwei-Wochen-Frist des Art. 52 Abs. 1 versäumt** — die Mitteilung an die Kommission ist fristgebunden und wird regelmäßig übersehen, weil sie vor der eigentlichen Pflichtenerfüllung liegt.
- **Schonjahr verwechselt mit Geltungsbeginn** — die Pflichten gelten seit 02.08.2025; nur die Durchsetzung setzte später ein. Wer erst zum 02.08.2026 mit der Umsetzung beginnt, ist bereits ein Jahr in der Pflichtverletzung.
- **Open-Source-Ausnahme überdehnt** — Art. 53 Abs. 2 befreit nur von lit. a und b. Urheberrechtsstrategie und Trainingsdaten-Zusammenfassung bleiben; bei systemischem Risiko entfällt die Ausnahme ganz.
- **Trainingsdaten-Zusammenfassung ohne die amtliche Vorlage** — die Vorlage ist verbindlich, freie Fassungen genügen nicht; ebenso wird die 6-monatige Fortschreibung übersehen.
- **ISO/IEC 42001 als Konformitätsnachweis missverstanden** — begründet mangels Amtsblatt-Zitierung keine Vermutungswirkung nach Art. 40.
- **Urheberrecht** — fehlende Strategie zur Beachtung des TDM-Vorbehalts verstößt gegen Art. 53 KI-VO; Klagerisiko von Rechteinhabern.
- **Dokumentationslücke** — unvollständige technische Dokumentation nach Anhang XI/XII gegenüber nachgelagerten Anbietern und Behörden.
- **Bußgeldrisiko** — bis 15 Mio. EUR / 3 % nach Art. 101 KI-VO; Durchsetzung ab 02.08.2026.
- **⚠️ Keine amtliche Liste systemischer Modelle unterstellen** — Art. 52 Abs. 6 verpflichtet die Kommission zur Veröffentlichung einer Liste der GPAI-Modelle mit systemischem Risiko. Eine solche Liste ist zum Stand 07/2026 **nicht als Primärquelle auffindbar**. In Sekundärquellen kursierende Aufzählungen konkreter Modelle sind **nicht belegt** und dürfen nicht in mandantengerichtete Ausgaben übernommen werden. `[unverifiziert - prüfen]`

## Ausgabeformat

```
GPAI-PFLICHTEN — PRÜFUNG — <Modell> — <Datum>

I.   GPAI-Modell?                               [ja / nein — Begründung]
II.  Rolle                                      [Anbieter / nachgelagert / Open Source]
III. Grundpflichten (Art. 53 KI-VO)
     Technische Dokumentation (Anhang XI)       [Status <…>]
     Info nachgelagerte Anbieter (Anhang XII)   [Status <…>]
     Urheberrechtsstrategie / TDM               [Status <…>]
     Trainingsdaten-Zusammenfassung             [Status <…>]
IV.  Systemisches Risiko (Art. 55 KI-VO)        [> 10^25 FLOP? / benannt?]
     Zusatzpflichten                            [Red-Teaming / Vorfallmeldung / Cybersicherheit]
V.   Code of Practice (Art. 56 KI-VO)           [beigetreten? <…>]
VI.  Bußgeldrisiko (Art. 101 KI-VO)             [bis 15 Mio. EUR / 3 %]

Empfehlung: <…>
Nächste Schritte: <…>
```

## Quellen

### Statute

- [VO (EU) 2024/1689 (KI-VO / EU AI Act)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R1689) — Volltext mit Anhängen
- Art. 51 KI-VO (Einstufung systemisches Risiko), Art. 53 KI-VO (GPAI-Pflichten), Art. 55 KI-VO (systemisches Risiko), Art. 56 KI-VO (Praxisleitfäden), Art. 101 KI-VO (Geldbußen GPAI), Anhang XI, Anhang XII KI-VO

### Leitlinien

- KI-Büro der EU-Kommission, GPAI Code of Practice (Juli 2025)
- KI-Büro, Vorlage zur Zusammenfassung der Trainingsinhalte

### Sekundärliteratur

- Hilgendorf/Roth-Isigkeit, KI-VO, 1. Aufl. 2024
- BeckOK KI-VO (Online)
