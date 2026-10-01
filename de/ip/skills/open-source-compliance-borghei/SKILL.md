---
name: open-source-compliance-borghei
title: /it-recht:open-source-compliance
description: 'Prüfung der Open-Source-Compliance in Produkten: urheberrechtliche Nutzungsrechte (§ 31 UrhG), Schutz von Computerprogrammen und zustimmungsbedürftige Verwertung (§ 69a, § 69c UrhG), Copyleft (GPL), Lizenzkette/Software Bill of Materials und Folgen der Lizenzverletzung (Unterlassung, Rückruf, § 97 UrhG). Use when die Verwendung von Open-Source-Komponenten in einem Produkt rechtlich abgesichert wird.'
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/it-recht/skills/open-source-compliance
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: ip
language: de
---

# /it-recht:open-source-compliance

## Zweck

Open-Source-Software ist nicht „rechtefrei": Sie wird unter Lizenzen mit verbindlichen Bedingungen genutzt. Wer eine Bedingung verletzt, verliert die Lizenz und nutzt das Werk dann ohne Erlaubnis — mit urheberrechtlichen Folgen. Dieser Skill inventarisiert die eingesetzten Komponenten, bewertet ihre Lizenzpflichten (insbesondere Copyleft), prüft die Verträglichkeit innerhalb der Lizenzkette und bestimmt die Folgen einer Lizenzverletzung.

## Eingaben

- Produktart und Vertriebsweg (Distribution von Binaries, SaaS-Bereitstellung, eingebettet)
- Liste der eingesetzten OSS-Komponenten samt Lizenzen (sofern vorhanden)
- Software Bill of Materials (SBOM), falls geführt
- geplante Verknüpfung (statisches/dynamisches Linken, Modifikation, reine Nutzung)
- Ziel (Erstfreigabe, Audit, Reaktion auf eine Abmahnung)

## Sub-Agent-Architektur

Drei Rollen greifen ineinander. Ein **Inventar-Agent** erstellt oder prüft die Lizenzkette und das Software Bill of Materials, denn ohne vollständige Komponentenliste ist keine belastbare Aussage möglich. Ein **Lizenzpflichten-Agent** ordnet jeder Komponente ihre Pflichten zu — Namensnennung, Lizenztext, Quelltextangebot, Copyleft-Reichweite — und prüft die Verträglichkeit untereinander. Ein **Risiko-Agent** bewertet schließlich Verletzungslagen und die Rechtsfolgen nach § 97 UrhG. Übergeben werden nur strukturierte Befunde je Komponente; Grundlage ist die jeweils konkrete Lizenz in ihrer einschlägigen Version, nicht eine pauschale „Open-Source"-Annahme.

## Ablauf

### 1. Urheberrechtliche Grundlage (§ 31, § 69a, § 69c UrhG)

Computerprogramme sind nach § 69a UrhG geschützt; ihre Vervielfältigung, Bearbeitung und Verbreitung ist nach § 69c UrhG zustimmungsbedürftig. Die OSS-Lizenz ist die Einräumung einfacher Nutzungsrechte nach § 31 UrhG unter Bedingungen. Werden die Bedingungen eingehalten, ist die Nutzung gestattet; werden sie verletzt, entfällt die Rechtfertigung und es liegt eine Verwertung ohne Nutzungsrecht vor.

### 2. Copyleft und GPL

Permissive Lizenzen (MIT, BSD, Apache 2.0) verlangen im Kern Namensnennung und Lizenzbeifügung. **Copyleft**-Lizenzen wie die **GPL** verlangen darüber hinaus, dass abgeleitete Werke bei Distribution unter derselben Lizenz und mit Zugang zum Quelltext weitergegeben werden (starkes Copyleft GPL, schwächeres LGPL/MPL). Entscheidend ist, ob eine „Distribution" vorliegt und ob durch Linken/Modifikation ein abgeleitetes Werk entsteht — beides bestimmt die Reichweite der Copyleft-Pflicht.

### 3. Lizenzkette und Software Bill of Materials

Die **Lizenzkette** ist über alle transitiven Abhängigkeiten zu erfassen und im **Software Bill of Materials** (SBOM, z. B. SPDX/CycloneDX) zu dokumentieren. Zu prüfen ist die Verträglichkeit der Lizenzen untereinander (z. B. Apache 2.0 mit GPLv2 nur eingeschränkt vereinbar) sowie die Erfüllung aller Weitergabepflichten (Lizenztext, Copyright-Vermerke, Quelltextangebot, Änderungshinweise).

### 4. Folgen der Lizenzverletzung (§ 97 UrhG)

Bei einer **Lizenzverletzung** entfällt die Nutzungsbefugnis rückwirkend; dem Rechtsinhaber stehen aus § 97 UrhG Anspruch auf Unterlassung und Schadensersatz zu, ergänzt um Vernichtungs- und Rückrufansprüche nach § 98 UrhG. Praktisch droht ein Vertriebsstopp des Produkts, bis die Compliance hergestellt ist.

## Risiken

- **Copyleft** unterschätzt: Verlinken/Einbetten einer GPL-Komponente in ein proprietäres, distribuiertes Produkt löst die Pflicht zur Offenlegung des eigenen Quelltexts aus.
- **GPL**-Pflichten bei Distribution missachtet (kein Quelltextangebot, fehlende Lizenzkopie) — die Lizenz entfällt, die Nutzung wird rechtswidrig.
- **Lizenzverletzung** ohne SBOM unentdeckt — transitive Abhängigkeiten mit unverträglichen Lizenzen bleiben verborgen, bis eine Abmahnung kommt.
- **Rückruf** und Vertriebsstopp: Unterlassungs- und Rückrufansprüche (§ 97, § 98 UrhG) können ausgelieferte Produkte betreffen — wirtschaftlich gravierend.
- SaaS-Trugschluss: Auch ohne klassische Distribution können Netzwerk-Copyleft-Lizenzen (AGPL) Offenlegungspflichten auslösen.

## Ausgabeformat

```
OPEN-SOURCE-COMPLIANCE — <Produkt> — <Datum>

I.   Inventar / Lizenzkette            [SBOM vorhanden? ✓/❌ — Format]
II.  Komponenten & Lizenzen            [permissiv / Copyleft (GPL/LGPL/AGPL)]
III. Verträglichkeit                   [✓ / ⚠️ Konflikt: <…>]
IV.  Distribution & Copyleft-Reichweite[Distribution ja/nein — abgeleitetes Werk?]
     Pflichten erfüllt:                [Lizenztext / Quelltext / Namensnennung]
V.   Verletzungslage (§ 97 UrhG)       [keine / Unterlassung / Rückruf-Risiko]

Maßnahmen / Freigabeempfehlung:        <…>
```

## Quellen

- [§ 31 UrhG](https://www.gesetze-im-internet.de/urhg/__31.html), [§ 69a UrhG](https://www.gesetze-im-internet.de/urhg/__69a.html), [§ 69c UrhG](https://www.gesetze-im-internet.de/urhg/__69c.html)
- [§ 97 UrhG](https://www.gesetze-im-internet.de/urhg/__97.html), [§ 98 UrhG](https://www.gesetze-im-internet.de/urhg/__98.html)
- Lizenztexte/Standards: GPLv2/GPLv3, LGPL, AGPL, Apache 2.0, MIT; SBOM-Formate SPDX / CycloneDX
