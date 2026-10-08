---
name: eu-taxonomie-borghei
title: /csrd:eu-taxonomie
description: Einordnung von Wirtschaftstätigkeiten nach der Taxonomie-VO (EU) 2020/852 – Taxonomiefähigkeit und Taxonomiekonformität (Art. 3, sechs Umweltziele Art. 9, „Do no significant harm“) sowie Offenlegung der KPI Umsatz/CapEx/OpEx nach Art. 8. Use when ein Unternehmen seine taxonomiefähigen und -konformen Anteile bestimmen oder die Art.-8-Offenlegung vorbereiten muss.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/csrd/skills/eu-taxonomie
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: regulatory
language: de
---

# /csrd:eu-taxonomie

## Zweck

Die **Taxonomie-VO (EU) 2020/852** ist das Klassifikationssystem der EU für ökologisch nachhaltige Wirtschaftstätigkeit. Berichtspflichtige Unternehmen müssen offenlegen, welcher Anteil ihres **Umsatzes**, ihrer Investitionsausgaben (**CapEx**) und Betriebsausgaben (**OpEx**) auf taxonomiefähige bzw. taxonomiekonforme Tätigkeiten entfällt. Die Taxonomie verzahnt sich eng mit der CSRD/ESRS-Berichterstattung. Fehler in der Konformitätsprüfung (insbesondere bei „Do no significant harm“) führen zu Prüfungseinschränkungen und Greenwashing-Vorwürfen.

> **⚠️ Aktualität (Stand 2026-07) — Offenlegungskreis folgt dem verengten CSRD-Anwendungsbereich:** Das **Omnibus-I-Paket** ist abgeschlossen. Die **Änderungs-RL (EU) 2026/470** wurde am **26.02.2026** im Amtsblatt veröffentlicht und ist am **18.03.2026** in Kraft getreten; sie ersetzt die Stop-the-Clock-RL (EU) 2025/794. Umsetzungsfrist **19.03.2027**.
>
> - **Wer offenlegt, richtet sich nach dem CSRD-Anwendungsbereich** — und der ist neu: **> 1.000 Beschäftigte UND > 450 Mio. EUR Nettoumsatz** (kumulativ). Die vom EP vorgeschlagene 1.750-Schwelle wurde **abgelehnt**; die Wellen-Systematik (Wave 1/2/3) ist als Maßstab überholt. Fällt ein Unternehmen aus der CSRD heraus, entfällt regelmäßig auch die **Art.-8-Offenlegung**. Die Schwellenprüfung ist deshalb **vor** jeder Taxonomie-Erhebung neu durchzuführen (`/csrd:esrs-berichtspflicht`).
> - **Wave-1-Rückfall:** Wer für **GJ 2024** offengelegt hat, aber unter den neuen Schwellen liegt, ist für **GJ 2025 und GJ 2026** nicht mehr erfasst (vorbehaltlich nationaler Umsetzung).
> - Die Darstellung der **Art.-8-KPI** wurde durch die **Delegierte VO (EU) 2026/73** (Omnibus-Vereinfachung) geändert; Templates, Schwellen und Befreiungen sind `[unverifiziert - prüfen]` und tagesaktuell an EUR-Lex abzugleichen.
> - **Wertschöpfungsketten-Cap:** Datenanfragen an kleinere Geschäftspartner — etwa zur Ermittlung von CapEx-/OpEx-Anteilen — sind auf die gesetzliche Obergrenze begrenzt; diese dürfen weitergehende Anfragen zurückweisen.
> - Der **Mindestschutz nach Art. 18** verweist weiterhin auf OECD-Leitsätze und UN-Leitprinzipien. Die LkSG-Nachweise bleiben dafür verwertbar: **§ 5 (Risikoanalyse), §§ 6, 7, § 8 LkSG gelten fort**; nur die BAFA-Berichtseinreichung nach §§ 12, 13 LkSG ist seit **03.09.2025** eingestellt.

## Eingaben

- Tätigkeitsportfolio (NACE-Codes, Produkte/Dienstleistungen)
- Finanzdaten: Umsatzerlöse, CapEx, OpEx (mit Kontenzuordnung)
- Bestehende Umwelt-/Klimadaten (Emissionen, Energie, Wasser)
- Ergebnis der doppelten Wesentlichkeitsanalyse (Schnittstelle ESRS E1–E5)
- Vorjahres-Taxonomie-Offenlegung (Kontinuität)

## Sub-Agent-Architektur

Ein **Eligibility-Agent** ordnet jede Tätigkeit den delegierten Rechtsakten zu und bestimmt die **Taxonomiefähigkeit** (eligibility) je Umweltziel. Ein **Alignment-Agent** prüft die **Taxonomiekonformität** in drei Stufen: wesentlicher Beitrag zu mindestens einem Umweltziel, **„Do no significant harm“** gegenüber den übrigen Zielen und Einhaltung des **Mindestschutzes** (minimum safeguards, Art. 18). Ein **KPI-Agent** rechnet die Anteile für **Umsatz**, **CapEx** und **OpEx** und mappt sie in die Offenlegungs-Templates. Ein **Verifikations-Agent** gleicht jede Schwelle und jedes Template gegen EUR-Lex ab und kennzeichnet Unsicheres mit `[unverifiziert - prüfen]`.

## Ablauf

### 0. Vorfrage: Besteht die Offenlegungspflicht noch? (RL (EU) 2026/470)

- Der Kreis der nach **Art. 8 Taxonomie-VO** Offenlegungspflichtigen knüpft an den CSRD-Anwendungsbereich an. Dieser ist seit **18.03.2026** auf **> 1.000 Beschäftigte UND > 450 Mio. EUR Nettoumsatz** (kumulativ) verengt.
- Frühere Offenlegungspraxis oder Wellenzuordnung sind **kein** Nachweis fortbestehender Pflicht.
- **Wave-1-Rückfall** prüfen: für GJ 2024 offengelegt, Schwellen nun nicht erreicht → **GJ 2025 und GJ 2026** ohne Pflicht.
- Ergebnis festhalten, bevor Tätigkeits-Mapping und KPI-Rechnung beginnen — die Datenerhebung ist der teuerste Teil des Prozesses.

### 1. Begriff der nachhaltigen Tätigkeit (Art. 3 Taxonomie-VO)

Nach **Art. 3 Taxonomie-VO** ist eine Tätigkeit ökologisch nachhaltig, wenn sie kumulativ:

1. einen **wesentlichen Beitrag** zu mindestens einem Umweltziel leistet,
2. **kein anderes Umweltziel erheblich beeinträchtigt** („Do no significant harm“, Art. 17),
3. den **Mindestschutz** (Art. 18, u. a. OECD-Leitsätze, UN-Leitprinzipien) wahrt und
4. die technischen Bewertungskriterien der delegierten Rechtsakte erfüllt.

### 2. Sechs Umweltziele (Art. 9 Taxonomie-VO)

**Art. 9 Taxonomie-VO** definiert die sechs Umweltziele:

1. Klimaschutz,
2. Anpassung an den Klimawandel,
3. Wasser- und Meeresressourcen,
4. Kreislaufwirtschaft,
5. Vermeidung und Verminderung der Umweltverschmutzung,
6. Schutz und Wiederherstellung der Biodiversität und der Ökosysteme.

### 3. Taxonomiefähigkeit (eligibility)

- Tätigkeit ist in einem delegierten Rechtsakt **beschrieben** → taxonomiefähig.
- Erste Stufe der Offenlegung: Anteil taxonomiefähiger vs. nicht-fähiger Umsätze/CapEx/OpEx.

### 4. Taxonomiekonformität (alignment)

- Wesentlicher Beitrag + **Do no significant harm** + Mindestschutz + technische Kriterien erfüllt → taxonomiekonform.
- Pro Tätigkeit dokumentieren, welche DNSH-Kriterien geprüft wurden.

### 5. KPI-Berechnung (Art. 8 Taxonomie-VO)

Nach **Art. 8 Taxonomie-VO** und der Delegierten VO (EU) 2021/2178 (i. d. F. (EU) 2026/73) sind drei KPI offenzulegen:

- **Umsatz-KPI** — Anteil taxonomiekonformer Umsatzerlöse,
- **CapEx-KPI** — Anteil taxonomiekonformer Investitionsausgaben,
- **OpEx-KPI** — Anteil taxonomiekonformer Betriebsausgaben.

Doppelzählungen vermeiden; Zähler/Nenner sauber abgrenzen.

### 6. Offenlegung und Verzahnung

- Darstellung in den vorgegebenen Templates; Verbindung zur ESRS-Berichterstattung (E1–E5).
- Konsistenz mit der Wesentlichkeitsanalyse und den Klimadaten herstellen.

## Risiken / typische Fehler

- **Do no significant harm verkürzt** — nur wesentlicher Beitrag geprüft, **Do no significant harm** und Mindestschutz nicht dokumentiert; häufigster Prüfungs-Finding.
- **Taxonomiefähigkeit mit -konformität verwechselt** — fähige als konforme Anteile ausgewiesen; die **Taxonomiekonformität** verlangt zusätzlich DNSH + Mindestschutz.
- **CapEx falsch abgegrenzt** — **CapEx** aus Übergangs-/Anpassungsplänen nicht berücksichtigt oder doppelt gezählt.
- **Template veraltet** — alte Offenlegungsvorlage statt der aktuellen Fassung; Stand `[unverifiziert - prüfen]`.
- **Mindestschutz ignoriert** — Art. 18 (OECD/UN-Leitprinzipien, LkSG-Schnittstelle) nicht geprüft.
- **Greenwashing-Risiko** — überzeichnete Konformitätsquote ohne belastbare technische Kriterien.
- **Mandant plant gegen aufgehobenes Recht** — Offenlegungskreis nach der alten Wellen-Systematik oder der Stop-the-Clock-RL (EU) 2025/794 bestimmt; maßgeblich ist die **Änderungs-RL (EU) 2026/470** (in Kraft 18.03.2026) mit **> 1.000 Beschäftigten UND > 450 Mio. EUR**.
- **Taxonomie-Erhebung ohne Offenlegungspflicht** — vollständiges Tätigkeits-Mapping und KPI-Rechnung für ein Unternehmen aufgesetzt, das aus dem CSRD-Anwendungsbereich herausgefallen ist. Die Schwellenprüfung ist **vorzuschalten**.
- **Wave-1-Rückfall übersehen** — für GJ 2024 offengelegt, für **GJ 2025/2026** nicht mehr erfasst.
- **Datenanfragen über den Cap hinaus** — kleinere Geschäftspartner müssen Anfragen jenseits der gesetzlichen Obergrenze nicht beantworten; ein darauf aufgebautes CapEx-/OpEx-Modell bricht zusammen.
- **Mindestschutz-Nachweis falsch verortet** — Art. 18 stützt sich auf die fortgeltenden LkSG-Pflichten (**§§ 5–8 LkSG**), nicht auf den seit 03.09.2025 nicht mehr einreichbaren BAFA-Bericht.

## Quellen

### EU-Rechtsakte

- [Taxonomie-VO (EU) 2020/852](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32020R0852) — Art. 3, Art. 8, Art. 9, Art. 17, Art. 18
- [Delegierte VO (EU) 2021/2178 (Art.-8-Offenlegung)](https://eur-lex.europa.eu/eli/reg_del/2021/2178/oj) · Delegierte VO (EU) 2026/73 (Vereinfachung) `[unverifiziert - prüfen]`
- [Delegierte VO (EU) 2021/2139 (Klima-Bewertungskriterien)](https://eur-lex.europa.eu/eli/reg_del/2021/2139/oj)

### Schnittstellen

- [RL (EU) 2022/2464 (CSRD)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32022L2464) · ESRS E1–E5
- **Änderungs-RL (EU) 2026/470 (Omnibus I)** — Amtsblatt 26.02.2026, in Kraft 18.03.2026, Umsetzungsfrist 19.03.2027; ersetzt die Stop-the-Clock-RL (EU) 2025/794. ELI-Fundstelle `[unverifiziert - prüfen]`
- [LkSG](https://www.gesetze-im-internet.de/lksg/) / [CSDDD RL (EU) 2024/1760](https://eur-lex.europa.eu/eli/dir/2024/1760/oj) (Mindestschutz Art. 18) — CSDDD-Schwelle i. d. F. Omnibus I: > 5.000 Beschäftigte und > 1,5 Mrd. EUR, materielle Pflichten ab 26.07.2029

## Ausgabeformat

```
EU-TAXONOMIE — <Unternehmen> — <Berichtsjahr>

0.    Offenlegungspflicht (RL (EU) 2026/470, in Kraft 18.03.2026)
      Beschäftigte > 1.000?  [Ja/Nein]   Nettoumsatz > 450 Mio. EUR? [Ja/Nein]
      Kumulativ erfüllt: [Ja/Nein]   Wave-1-Rückfall GJ 2025/2026: [Ja/Nein]
I.    Tätigkeitsmapping
      Tätigkeit | NACE | Umweltziel (Art. 9) | fähig?
II.   Konformitätsprüfung (Art. 3)
      Wesentlicher Beitrag | Do no significant harm | Mindestschutz | techn. Kriterien
III.  KPI (Art. 8)
      Umsatz:  fähig __ %   konform __ %
      CapEx:   fähig __ %   konform __ %
      OpEx:    fähig __ %   konform __ %
IV.   Verzahnung ESRS / Klimadaten
      <…>
V.    Offene Punkte
      <… [unverifiziert - prüfen]>

Restrisiko: <…>
Wiedervorlage: jährlich
```
