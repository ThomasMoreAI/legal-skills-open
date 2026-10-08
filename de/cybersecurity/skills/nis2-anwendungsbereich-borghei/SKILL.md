---
name: nis2-anwendungsbereich-borghei
title: /nis2:nis2-anwendungsbereich
description: Betroffenheitsprüfung und Registrierung nach NIS2 / neuem BSIG – wesentliche und wichtige Einrichtungen Art. 3 NIS2-RL / § 28 BSIG, Sektoren nach Anhang I/II, Größenschwellen sowie Registrierungspflicht §§ 33/34 BSIG. Use when eine Einrichtung klären muss, ob sie unter NIS2 fällt und sich beim BSI registrieren muss.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/nis2/skills/nis2-anwendungsbereich
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: cybersecurity
language: de
---

# /nis2:nis2-anwendungsbereich

## Zweck

Das **NIS2-Umsetzungsgesetz** (in Kraft seit 06.12.2025) hat das BSIG neu gefasst und den Adressatenkreis von rund 2.100 auf etwa 29.000 Einrichtungen erweitert. Wer betroffen ist, ergibt sich aus dem Zusammenspiel von **Sektor** (Anhang I/II zum BSIG), **Größenschwellen** und Einrichtungskategorie. Anders als früher gibt es **keine behördliche Einzelfeststellung** mehr — die Einrichtung muss sich **selbst einstufen** und registrieren. Dieser Skill führt die Betroffenheitsprüfung und die Registrierung durch.

## Eingaben

- Tätigkeit / Sektor der Einrichtung (Energie, Gesundheit, Verkehr, digitale Dienste, Maschinenbau usw.)
- Beschäftigtenzahl, Jahresumsatz, Jahresbilanzsumme
- KRITIS-Status (Betreiber kritischer Anlagen?)
- Qualifizierter Vertrauensdiensteanbieter / DNS / TLD / Cloud / Rechenzentrum?
- Konzernstruktur (verbundene Unternehmen für Schwellenberechnung)

## Sub-Agent-Architektur

Drei gedankliche Rollen. Ein **Sektor-Agent** ordnet die Tätigkeit den Einrichtungstypen aus Anhang I und Anhang II zum BSIG zu. Ein **Schwellen-Agent** prüft die **Größenschwellen** (Beschäftigte, Umsatz, Bilanzsumme) und die Sonderfälle, in denen die Schwelle entfällt. Ein **Registrierungs-Agent** bestimmt die Einrichtungskategorie nach § 28 BSIG und den richtigen Registrierungspfad (§ 33 oder § 34 BSIG) samt Frist. Die finale Einstufung verantwortet die Einrichtung selbst.

## Ablauf

### 1. Sektor-Zuordnung (Anhang I / II BSIG)

- **Anhang I** (hohe Kritikalität): u. a. Energie, Verkehr, Bankwesen, Finanzmarktinfrastruktur, Gesundheit, Trinkwasser, Abwasser, digitale Infrastruktur, IKT-Dienste-Verwaltung, Weltraum.
- **Anhang II** (sonstige kritische Sektoren): u. a. Post/Kurier, Abfall, Chemie, Lebensmittel, verarbeitendes Gewerbe (inkl. Maschinenbau), digitale Dienste, Forschung.

### 2. Größenschwellen (§ 28 BSIG)

| Kategorie | Schwelle |
|---|---|
| **Besonders wichtige Einrichtung** | KRITIS-Betreiber, qualifizierte Vertrauensdiensteanbieter oder Anhang-I-Typ mit ≥ 250 Beschäftigten **oder** > 50 Mio. € Umsatz **und** > 43 Mio. € Bilanzsumme |
| **Wichtige Einrichtung** | Anhang-I-/II-Typ mit ≥ 50 Beschäftigten **oder** > 10 Mio. € Umsatz **und** > 10 Mio. € Bilanzsumme |

- Bei bestimmten Typen (DNS, TLD, qualifizierte Vertrauensdienste, KRITIS) gelten die **Größenschwellen** nicht — Betroffenheit unabhängig von der Größe.
- Terminologie: Die NIS2-RL spricht in Art. 3 von **wesentliche** und **wichtige Einrichtungen**; das BSIG setzt dies als **besonders wichtige** und **wichtige Einrichtungen** um.

### 3. Selbsteinstufung statt Bescheid

- Es ergeht **kein** behördlicher Feststellungsbescheid; die Einrichtung trägt die Darlegungslast ihrer **Selbsteinstufung**.

### 4. Registrierungspflicht (§§ 33/34 BSIG)

- **§ 33 BSIG**: allgemeine **Registrierungspflicht** beim BSI — binnen **drei Monaten** ab Erfüllung der Kriterien.
- **§ 34 BSIG**: besondere Registrierungspflicht für bestimmte Typen (z. B. DNS-Diensteanbieter, TLD-Registries, Cloud-/Rechenzentrumsdienste, CDN), teils mit zusätzlichen Angaben.
- Registrierungsportal des BSI; Aktualisierungspflicht bei Änderungen.

### 5. Folgepflichten

- Mit der Betroffenheit greifen unmittelbar Risikomanagement (§ 30 BSIG), Meldepflichten (§ 32 BSIG) und Leitungspflichten (§ 38 BSIG).

## Risiken / typische Fehler

- **Größenschwellen** falsch berechnet — verbundene Unternehmen und der Wegfall der Schwelle bei Sondertypen (DNS, KRITIS) werden oft übersehen.
- **Registrierungspflicht** verpasst — die Drei-Monats-Frist nach § 33 BSIG läuft automatisch, ohne behördliche Aufforderung.
- **Selbsteinstufung** unterlassen — es gibt keinen Bescheid; wer auf Post vom BSI wartet, ist bereits säumig.
- **Lieferketten**-Betroffenheit verkannt — auch Zulieferer in Anhang-II-Sektoren (z. B. Maschinenbau) können erfasst sein.

## Quellen

### Statute

- [§ 28 BSIG (n.F.)](https://www.gesetze-im-internet.de/bsig_2025/__28.html) — besonders wichtige und wichtige Einrichtungen
- [§ 33 BSIG (n.F.)](https://www.gesetze-im-internet.de/bsig_2025/__33.html) — Registrierungspflicht
- [§ 34 BSIG (n.F.)](https://www.gesetze-im-internet.de/bsig_2025/__34.html) — besondere Registrierungspflicht
- [Richtlinie (EU) 2022/2555 (NIS2)](https://eur-lex.europa.eu/eli/dir/2022/2555/oj) — Art. 3 NIS2-RL, Anhang I / Anhang II

### Sekundärliteratur

- Eckhardt, NIS2, 1. Aufl. 2024
- OpenKRITIS, „NIS2-Umsetzungsgesetz in Deutschland"

## Ausgabeformat

```
NIS2-ANWENDUNGSBEREICH — <Einrichtung> — <Datum>

I.    Sektor-Zuordnung (Anhang I / II)     [Typ / Sektor]
II.   Größenschwellen (§ 28 BSIG)
      Beschäftigte / Umsatz / Bilanz        <Werte>  Schwelle erreicht? [Ja/Nein]
      Sondertyp ohne Schwelle?              [Ja/Nein]
III.  Einrichtungskategorie                 [besonders wichtig / wichtig / nicht betroffen]
IV.   Registrierungspflicht                 [§ 33 BSIG / § 34 BSIG]  Frist: <Datum + 3 Monate>
V.    Folgepflichten                         [§ 30 / § 32 / § 38 BSIG aktiviert]

Selbsteinstufung dokumentiert: <Begründung>
Nächster Schritt: <…>
```
