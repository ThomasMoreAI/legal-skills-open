---
name: wesentlichkeitsanalyse-doppelt-borghei
title: /csrd:wesentlichkeitsanalyse-doppelt
description: Durchführung der doppelten Wesentlichkeitsanalyse nach ESRS 1 §§ 25–53 – Impact Materiality (Auswirkungen des Unternehmens auf Mensch und Umwelt) und Financial Materiality (Risiken/Chancen aus Nachhaltigkeitsthemen für das Unternehmen). Use when ein Unternehmen erstmals CSRD-pflichtig ist oder die jährliche Wesentlichkeitsanalyse aufgesetzt wird.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/csrd/skills/wesentlichkeitsanalyse-doppelt
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: regulatory
language: de
---

# /csrd:wesentlichkeitsanalyse-doppelt

## Zweck

Die doppelte Wesentlichkeit ist der Anker jedes CSRD-Berichts. Themen, die als wesentlich identifiziert werden, lösen die ausführliche Berichtspflicht nach den themenbezogenen ESRS aus (E1–E5, S1–S4, G1). Eine fehlerhafte Wesentlichkeitsanalyse macht den gesamten Bericht angreifbar — und führt zu Prüfungseinschränkungen.

> **⚠️ Aktualität (Stand 2026-07) — vor der Wesentlichkeitsanalyse steht die neue Schwellenprüfung:** Das **Omnibus-I-Paket** ist abgeschlossen. Die **Änderungs-RL (EU) 2026/470** wurde am **26.02.2026** im Amtsblatt veröffentlicht und ist am **18.03.2026** in Kraft getreten; sie **ersetzt** die frühere „Stop-the-Clock"-RL (EU) 2025/794. Die Wellen-Systematik (Wave 1 / Wave 2 / Wave 3) ist als Betroffenheitsmaßstab **überholt**.
>
> - **CSRD-Anwendungsbereich neu:** **> 1.000 Beschäftigte UND > 450 Mio. EUR Nettoumsatz** (kumulativ). Die vom Europäischen Parlament vorgeschlagene Schwelle von 1.750 Beschäftigten wurde **abgelehnt**. Umsetzungsfrist **19.03.2027**.
> - **Wave-1-Rückfall:** Unternehmen, die für das **Geschäftsjahr 2024** berichtet haben, aber die neuen Schwellen nicht erreichen, sind für **GJ 2025 und GJ 2026 nicht berichtspflichtig** (vorbehaltlich nationaler Umsetzung).
> - **Praxisfolge für diese Skill:** Eine doppelte Wesentlichkeitsanalyse ist **erst dann aufzusetzen, wenn die Schwellenprüfung nach neuem Recht positiv ausfällt.** Der teuerste Fehler des Jahres 2026 ist eine vollständige Wesentlichkeitsanalyse für ein Unternehmen, das gar nicht mehr berichtspflichtig ist. Siehe `/csrd:esrs-berichtspflicht`.
> - **ESRS-Überarbeitung läuft noch.** Die Datenpunkt-Struktur und Teile der Wesentlichkeitsvorgaben in ESRS 1 werden voraussichtlich vereinfacht. Verweise auf konkrete Randziffern von ESRS 1 sind daher `[unverifiziert - prüfen]` und gegen die jeweils geltende Fassung der Delegierten VO (EU) 2023/2772 abzugleichen.
> - **Wertschöpfungsketten-Cap:** Datenanfragen an kleinere Geschäftspartner sind auf die gesetzliche Obergrenze begrenzt; diese dürfen weitergehende Anfragen zurückweisen. Stakeholder- und Lieferantenerhebungen sind entsprechend zu dimensionieren.
> - **CSDDD-Inputs verschieben sich:** Die CSDDD-Schwelle liegt nun bei **> 5.000 Beschäftigten UND > 1,5 Mrd. EUR** (Umsetzung 26.07.2028, materielle Pflichten 26.07.2029). LkSG-Risikoanalysen bleiben als Input verfügbar; die BAFA-Berichtseinreichung nach §§ 12, 13 LkSG ist dagegen seit **03.09.2025 eingestellt**.

## Eingaben

- Geschäftsmodell, Wertschöpfungskette (Upstream + Downstream)
- Branche und geographische Tätigkeit
- Bestehende Stakeholder-Befragungen
- Risikomanagement-Output (für Financial Materiality)
- Ergebnis der vorherigen Wesentlichkeitsanalyse (Kontinuitätsprinzip)
- LkSG-Risikoanalyse (Schnittstelle)

## Ablauf

### 0. Vorfrage: Besteht die Berichtspflicht überhaupt noch? (RL (EU) 2026/470)

Vor jedem Methodikschritt ist die **Schwellenprüfung nach neuem Recht** durchzuführen:

- **> 1.000 Beschäftigte UND > 450 Mio. EUR Nettoumsatz** — kumulativ, seit Inkrafttreten der Änderungs-RL (EU) 2026/470 am **18.03.2026**.
- Frühere Berichtspraxis, Wellenzuordnung oder die alte NFRD-Schwelle sind **kein** Betroffenheitsnachweis.
- Fällt das Unternehmen heraus, ist die Wesentlichkeitsanalyse **nicht** gesetzlich geschuldet. Sie kann freiwillig fortgeführt werden (Bankenrating, Kundenanforderungen, Konzernvorgaben) — dann aber ausdrücklich als **freiwillig** zu deklarieren, mit reduziertem Umfang und ohne Prüfungspflicht.
- Ergebnis dieser Vorfrage schriftlich festhalten; Details in `/csrd:esrs-berichtspflicht`.

### 1. Konzept doppelte Wesentlichkeit (ESRS 1 § 25)

Ein Thema ist wesentlich, wenn **mindestens eine** der beiden Perspektiven es erfasst:

- **Impact Materiality (§§ 27–43)** — das Unternehmen hat **tatsächliche oder potenzielle, positive oder negative, kurz- oder langfristige** Auswirkungen auf Menschen oder Umwelt entlang der eigenen Tätigkeit und der Wertschöpfungskette.
- **Financial Materiality (§§ 44–53)** — Nachhaltigkeitsthemen können zu **Risiken** oder **Chancen** führen, die die finanzielle Lage, Performance, Cashflows, Zugang zu Finanzierung oder Kapitalkosten beeinflussen.

### 2. Universal-Themen aus ESRS-Standards

Ausgangsliste der zu prüfenden Themen aus den themenbezogenen ESRS:

| Cluster | ESRS | Thema |
|---|---|---|
| E – Umwelt | ESRS E1 | Klimawandel |
| | ESRS E2 | Umweltverschmutzung |
| | ESRS E3 | Wasser und Meeresressourcen |
| | ESRS E4 | Biologische Vielfalt und Ökosysteme |
| | ESRS E5 | Ressourcennutzung und Kreislaufwirtschaft |
| S – Soziales | ESRS S1 | Eigene Belegschaft |
| | ESRS S2 | Beschäftigte in der Wertschöpfungskette |
| | ESRS S3 | Betroffene Gemeinschaften |
| | ESRS S4 | Verbraucher und Endnutzer |
| G – Governance | ESRS G1 | Geschäftsgebaren |

### 3. Schwellenwerte und Bewertung

- **Schwellenwert** = Punkt, ab dem ein Thema „wesentlich" ist. Festlegung durch das Unternehmen, **mit Begründung**.
- Impact: Schweregrad × (Umfang + Umfang + Umkehrbarkeit) × Wahrscheinlichkeit (bei potenziellen Impacts).
- Financial: Höhe × Wahrscheinlichkeit × Zeithorizont.

### 4. Stakeholder-Einbindung (ESRS 1 § 24)

- **Tatsächliche Stakeholder** (eigene Belegschaft, Lieferanten, Kunden, Investoren, Gemeinden)
- **Stille Stakeholder** für Umwelt-Themen (Natur, künftige Generationen)
- Methoden: Befragung, Workshop, NGO-Konsultation, Datenanbieter-Analyse

### 5. Verzahnung mit anderen Pflichten

- **EU-Taxonomie** (VO (EU) 2020/852) — taxonomiefähige und taxonomiekonforme Aktivitäten/Umsatzanteile
- **LkSG / CSDDD** — Risikoanalyse-Outputs sind Inputs der Wesentlichkeitsanalyse. **Stand 07/2026:** Die LkSG-Risikoanalyse (**§ 5 LkSG**), Präventions-/Abhilfemaßnahmen (§§ 6, 7) und das Beschwerdeverfahren (§ 8) bestehen **unverändert fort** und liefern weiterhin verwertbare Daten; lediglich die **Berichtseinreichung beim BAFA nach §§ 12, 13 LkSG ist seit 03.09.2025 eingestellt** (exekutive Weisung, keine Gesetzesaufhebung). Die **CSDDD**-Schwelle wurde durch Omnibus I auf **> 5.000 Beschäftigte UND > 1,5 Mrd. EUR** angehoben (Umsetzung 26.07.2028, materielle Pflichten 26.07.2029) — für die meisten Mandanten ist die CSDDD damit **kein** kurzfristiger Treiber der Wesentlichkeitsanalyse mehr.
- **Wertschöpfungsketten-Cap** — Datenanfragen an kleinere Geschäftspartner sind auf die gesetzliche Obergrenze beschränkt; diese dürfen darüber hinausgehende Anfragen ablehnen. Erhebungsdesign entsprechend begrenzen.
- **NFRD** (vorherige Berichte) — Kontinuität der Berichterstattung
- **EU-Klimagesetz und Pariser Übereinkommen** — Zielreferenz

### 6. Dokumentation

- Methodik schriftlich beschreiben (ESRS 1 § 53)
- Bewertungsraster mit Skalen
- Stakeholder-Liste
- Ergebnistabelle mit Begründung pro Thema
- Verweise im Bericht (Lagebericht / Nachhaltigkeitsbericht)

### 7. Prüfung

- **Limited Assurance** durch unabhängige Prüfer ab erster Anwendung
- Übergang zu **Reasonable Assurance** geplant (EU-Kommission Roadmap)

## Quellen

### Statute / EU-Rechtsakte

- [RL (EU) 2022/2464 (CSRD, Corporate Sustainability Reporting Directive)](https://eur-lex.europa.eu/eli/dir/2022/2464/oj) — Volltext
- [Delegierte VO (EU) 2023/2772 (ESRS Set 1)](https://eur-lex.europa.eu/eli/reg_del/2023/2772/oj) — ESRS-Standards; **Überarbeitung im Rahmen von Omnibus I läuft** `[unverifiziert - prüfen]`
- **Änderungs-RL (EU) 2026/470 (Omnibus I)** — Amtsblatt 26.02.2026, in Kraft 18.03.2026, Umsetzungsfrist 19.03.2027; ersetzt die Stop-the-Clock-RL (EU) 2025/794. ELI-Fundstelle `[unverifiziert - prüfen]`
- [VO (EU) 2020/852 (EU-Taxonomie)](https://eur-lex.europa.eu/eli/reg/2020/852/oj)
- [Richtlinie (EU) 2024/1760 (CSDDD)](https://eur-lex.europa.eu/eli/dir/2024/1760/oj) — Schwelle i. d. F. Omnibus I: > 5.000 Beschäftigte und > 1,5 Mrd. EUR
- [LkSG](https://www.gesetze-im-internet.de/lksg/) — § 5 (Risikoanalyse) als Input; §§ 12, 13 seit 03.09.2025 nicht mehr vollzogen

### EFRAG-Materialien

- EFRAG IG 1: Materiality Assessment Implementation Guidance
- EFRAG IG 2: Value Chain Implementation Guidance
- EFRAG IG 3: Detailed ESRS Datapoints

### Sekundärliteratur

- IDW PS 980 (Compliance-Management-Systeme; benachbart)
- Behnke / Hoff, CSRD und ESRS, 1. Aufl. 2024
- Beck'sches IFRS-Handbuch (Nachhaltigkeit)

## Ausgabeformat

```
DOPPELTE WESENTLICHKEITSANALYSE — <Unternehmen> — <Berichtsjahr>

0.    Vorfrage Berichtspflicht (RL (EU) 2026/470, in Kraft 18.03.2026)
      Beschäftigte > 1.000?         [Ja / Nein]
      Nettoumsatz > 450 Mio. EUR?   [Ja / Nein]
      Kumulativ erfüllt:            [Ja / Nein]
      Wenn Nein → Analyse ist freiwillig; Umfang reduzieren und als
      freiwillig kennzeichnen. Wave-1-Rückfall GJ 2025/2026: [Ja / Nein]
I.    Methodik
      Impact-Bewertung:  Schweregrad / Umfang / Umkehrbarkeit / Wahrscheinlichkeit
      Financial-Bewertung: Höhe / Wahrscheinlichkeit / Zeithorizont
      Schwellenwert: <begründet>
II.   Stakeholder-Einbindung
      Methoden: <…>
      Stakeholder: <Liste>
III.  Themen-Bewertung
      ESRS  | Impact | Financial | Wesentlich?
      E1    |   …    |    …      |   ja
      E2    |   …    |    …      |   nein
      ...
IV.   Begründung pro wesentliches Thema
      <…>
V.    Verzahnung
      EU-Taxonomie: <…>
      LkSG-Inputs:  <…>
      Vorjahr-Kontinuität: <…>
VI.   Folgepflichten
      Datenpunkte: <Liste mit Modulen aus ESRS>
      Prüfungs-Vorbereitung: <…>

Restrisiko: <…>
Wiedervorlage: jährlich
```

## Risiken / typische Fehler

- **Nur Impact-Bewertung** — Financial Materiality vergessen oder nicht dokumentiert.
- **Schwellenwert ohne Begründung** — Prüfungs-Finding wahrscheinlich.
- **Wertschöpfungskette zu eng** — Downstream-Themen unterschätzt, insb. S4 (Verbraucher).
- **Stakeholder nicht eingebunden** — verstößt gegen ESRS 1 § 24.
- **Kontinuität verletzt** — Änderung der Methodik ohne Begründung gegenüber Vorjahr.
- **LkSG-Outputs ignoriert** — Schnittstelle ungenutzt; doppelte Arbeit.
- **Mandant plant gegen aufgehobenes Recht** — Analyse wird auf Basis der alten Wellen-Systematik oder der Stop-the-Clock-RL (EU) 2025/794 aufgesetzt. Beides ist durch die **Änderungs-RL (EU) 2026/470** (in Kraft 18.03.2026) überholt.
- **Wesentlichkeitsanalyse ohne Berichtspflicht** — der teuerste Fehler: volle Analyse für ein Unternehmen, das nach der neuen Schwelle (**> 1.000 Beschäftigte UND > 450 Mio. EUR**) gar nicht mehr berichtspflichtig ist. Schwellenprüfung ist der Analyse **vorgeschaltet**.
- **Wave-1-Rückfall übersehen** — für GJ 2024 berichtet, jetzt unter der Schwelle: für **GJ 2025 und GJ 2026** besteht keine Pflicht; eine Fortführung ist als freiwillig zu kennzeichnen.
- **ESRS-Randziffern als final zitiert** — die ESRS-Überarbeitung läuft noch; Verweise auf ESRS 1 §§ 25–53 sind mit `[unverifiziert - prüfen]` zu versehen und gegen die geltende Fassung abzugleichen.
- **CSDDD als naher Treiber dargestellt** — die Schwelle liegt jetzt bei > 5.000 Beschäftigten und > 1,5 Mrd. EUR, materielle Pflichten erst ab 26.07.2029.
