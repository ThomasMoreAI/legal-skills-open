---
name: it-sicherheit-meldepflichten-borghei
title: /it-recht:it-sicherheit-meldepflichten
description: Prüfung der IT-Sicherheits- und Meldepflichten von KRITIS-Betreibern und NIS2-Einrichtungen nach dem BSIG (Stand der Technik, Risikomanagement, Vorfallmeldung, Registrierung, Bußgeld). Use when geklärt werden soll, ob eine Einrichtung dem BSIG unterfällt und welche Sicherheits- und Meldepflichten sie treffen.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/it-recht/skills/it-sicherheit-meldepflichten
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: cybersecurity
language: de
---

# /it-recht:it-sicherheit-meldepflichten

## Zweck

Das BSIG verpflichtet Betreiber Kritischer Infrastrukturen sowie — seit Umsetzung der NIS2-Richtlinie — rund 29.500 „besonders wichtige" und „wichtige" Einrichtungen zu technisch-organisatorischen Sicherheitsmaßnahmen nach dem **Stand der Technik** und zu raschen Meldungen erheblicher Sicherheitsvorfälle an das BSI. Dieser Skill ordnet eine konkrete Einrichtung in den Anwendungsbereich ein, bestimmt die geltenden Pflichten und bewertet das Bußgeld- und Haftungsrisiko.

**Rechtslage-Hinweis:** Das NIS2-Umsetzungsgesetz (NIS2UmsuCG) ist am **6.12.2025** in Kraft getreten und hat das BSIG neu gefasst. Die früher in **§ 8a BSIG** (Sicherheit/Stand der Technik) und **§ 8b BSIG** (Meldepflicht zentrale Stelle) geregelten KRITIS-Pflichten finden sich in der Neufassung in **§ 30 BSIG** (Risikomanagement), § 31 BSIG (besondere KRITIS-Anforderungen) und **§ 32 BSIG** (Meldepflichten). Der Skill weist beide Fundstellen aus, weil Altverträge, Audit-Nachweise und ältere Branchenstandards noch auf §§ 8a, 8b BSIG verweisen.

## Eingaben

- Sektor (Energie, Wasser, Gesundheit, Transport, Finanzwesen, digitale Infrastruktur, IKT-Dienstleister, …)
- Unternehmensgröße (Beschäftigte, Jahresumsatz / Bilanzsumme)
- KRITIS-Schwellenwerte erreicht? (KRITIS-Verordnung)
- Bestehende Maßnahmen (ISMS, Zertifizierung, B3S-Branchenstandard)
- Letzter Audit-/Prüfnachweis (Datum)
- Vorliegender oder eingetretener Sicherheitsvorfall (Zeitpunkt, Auswirkung)

## Sub-Agent-Architektur

Die Bearbeitung folgt drei gedanklichen Rollen. Ein **Scoping-Agent** prüft anhand von Sektor, Größe und KRITIS-Schwellen, ob die Einrichtung als KRITIS-Betreiber, als besonders wichtige oder als wichtige Einrichtung gilt (§ 28 BSIG) — diese Einordnung steuert Pflichtenumfang und Bußgeldrahmen. Ein **Pflichten-Agent** mappt die Maßnahmenpflichten (§ 30 BSIG / früher § 8a BSIG), KRITIS-Sonderpflichten (§ 31 BSIG), Melde- (§ 32 BSIG / früher § 8b BSIG), Registrierungs- und Nachweispflichten und gleicht sie mit dem Ist-Stand ab. Ein **Risiko-Agent** bewertet Fristverstöße, fehlende Nachweise und die persönliche Geschäftsleiterhaftung und beziffert das Bußgeldrisiko. Die Rollen arbeiten sequenziell; das Scoping ist Voraussetzung jeder weiteren Bewertung. Bei Aktenzeichen oder Einzelheiten der KRITIS-Verordnung gilt Zero-Fabrication: nicht verifizierte Angaben werden mit `[unverifiziert – prüfen]` markiert.

## Ablauf

### 1. Anwendungsbereich (§ 28 BSIG)

- KRITIS-Betreiber: Anlage erreicht Schwellenwert der KRITIS-Verordnung.
- Besonders wichtige Einrichtung: u. a. große Unternehmen kritischer Sektoren, qualifizierte Vertrauensdiensteanbieter, TLD-Registries, Telekommunikation.
- Wichtige Einrichtung: mittlere Unternehmen erfasster Sektoren (Regel: ab 50 Beschäftigte oder 10 Mio. EUR Umsatz/Bilanzsumme).
- Ergebnis bestimmt Aufsichtsregime (ex ante / reaktiv) und Bußgeldrahmen.

### 2. Risikomanagement / Stand der Technik (§ 30 BSIG, früher § 8a BSIG)

Geeignete, verhältnismäßige und wirksame technische und organisatorische Maßnahmen, u. a.:

- Risikoanalyse- und Sicherheitskonzepte, Konzepte für Kryptografie und Verschlüsselung
- Bewältigung von Sicherheitsvorfällen, Business Continuity / Backup-Management
- Sicherheit der Lieferkette, Zugriffskontrolle, Multi-Faktor-Authentifizierung
- Bewertung der Wirksamkeit (Stand der Technik, einschlägige europäische Normen)

KRITIS-Betreiber: zusätzlich Systeme zur Angriffserkennung und Nachweispflicht alle zwei Jahre (§ 31 BSIG, früher § 8a BSIG Abs. 3).

### 3. Meldepflichten (§ 32 BSIG, früher § 8b BSIG)

Mehrstufiges Meldeschema für erhebliche Sicherheitsvorfälle über das BSI-Portal:

- **Erstmeldung** unverzüglich, spätestens **24 Stunden** nach Kenntnis
- **Folgemeldung** (Bestätigung/Aktualisierung) binnen **72 Stunden**
- **Abschlussbericht** binnen **eines Monats**

Erheblich ist ein Vorfall insbesondere bei schwerwiegender Betriebsstörung oder finanziellen/immateriellen Schäden Dritter.

### 4. Registrierung und Governance

- Registrierungspflicht beim BSI (§ 33 ff. BSIG); Frist nach Inkrafttreten am 6.3.2026 abgelaufen — Neueinrichtungen registrieren sich fristgerecht.
- Geschäftsleiter müssen Risikomaßnahmen billigen, überwachen und sich schulen (§ 38 BSIG); persönliche Verantwortlichkeit.

### 5. Sanktionen (§ 65 BSIG)

- Besonders wichtige Einrichtungen: bis 10 Mio. EUR oder 2 % des weltweiten Jahresumsatzes.
- Wichtige Einrichtungen: bis 7 Mio. EUR oder 1,4 % des Umsatzes.

## Risiken / typische Fehler

- **Verspätete Meldung** — Versäumen der 24-Stunden-Erstmeldung verletzt die Meldepflicht nach § 32 BSIG und ist bußgeldbewehrt.
- **Stand der Technik nicht eingehalten** — veraltete oder nicht dokumentierte Maßnahmen genügen § 30 BSIG (früher § 8a BSIG) nicht.
- **Bußgeld** — Verstöße gegen § 30/§ 32 BSIG lösen den Rahmen des § 65 BSIG aus (bis 2 % Konzernumsatz).
- **Geschäftsleiterhaftung** — unterlassene Billigung/Überwachung der Maßnahmen begründet persönliche Verantwortlichkeit der Leitung (§ 38 BSIG).

## Ausgabeformat

```
IT-SICHERHEIT & MELDEPFLICHTEN — <Einrichtung> — <Datum>

I.    Anwendungsbereich (§ 28 BSIG)
      Einordnung:                 [KRITIS / besonders wichtig / wichtig / nicht erfasst]
      Sektor / Schwelle:          <…>
II.   Risikomanagement (§ 30 BSIG / § 8a BSIG a.F.)
      Stand der Technik:          [✓ / ⚠️ / ❌]   Lücken: <…>
      KRITIS-Nachweis (§ 31):     [aktuell / fällig / fehlt]
III.  Meldepflicht (§ 32 BSIG / § 8b BSIG a.F.)
      24h / 72h / 1 Monat:        [eingehalten / versäumt / N/A]
IV.   Registrierung & Governance
      BSI-Registrierung:          [✓ / 🔴]
      Geschäftsleiterpflichten:   [erfüllt / offen]
V.    Bußgeldrisiko (§ 65 BSIG)
      Rahmen:                     <bis 10 Mio. / 7 Mio. EUR>

Handlungsempfehlung:              <…>
```

## Quellen

- [§ 30 BSIG](https://www.gesetze-im-internet.de/bsig_2025/__30.html), [§ 31 BSIG](https://www.gesetze-im-internet.de/bsig_2025/__31.html), [§ 32 BSIG](https://www.gesetze-im-internet.de/bsig_2025/__32.html), [§ 65 BSIG](https://www.gesetze-im-internet.de/bsig_2025/__65.html) (Neufassung, in Kraft seit 6.12.2025)
- [§ 8a BSIG, § 8b BSIG (a.F.)](https://www.gesetze-im-internet.de/bsig_2009/) — IT-SiG 2.0, weiterhin in Altnachweisen referenziert
- [NIS2-Richtlinie (EU) 2022/2555](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32022L2555)
- KRITIS-Verordnung (BSI-KritisV); B3S-Branchenstandards des BSI
