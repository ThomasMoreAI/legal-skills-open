---
name: ki-vertraege-borghei
title: /it-recht:ki-vertraege
description: 'Gestaltung und Prüfung von Verträgen über KI-Systeme: Leistungsbeschreibung und Gewährleistung (§ 434, § 633, § 327 BGB), Trainingsdaten und Text-und-Data-Mining-Schranke (§ 44b UrhG), Verzahnung mit der KI-VO (Hochrisiko- und Transparenzpflichten) sowie Haftung für KI-Output. Use when ein Vertrag über Beschaffung, Entwicklung oder Nutzung eines KI-Systems gestaltet oder bewertet wird.'
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/it-recht/skills/ki-vertraege
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: contracts
language: de
---

# /it-recht:ki-vertraege

## Zweck

Verträge über KI-Systeme stellen klassische IT-Vertragsmuster vor neue Fragen: probabilistische Outputs entziehen sich der vereinbarten Beschaffenheit, Trainingsdaten werfen Urheberrechtsfragen auf, und die KI-VO verteilt öffentlich-rechtliche Pflichten zwischen Anbieter und Betreiber. Dieser Skill strukturiert die Gestaltung entlang von Leistung und **Gewährleistung** (**§ 434 BGB**, **§ 633 BGB**, **§ 327 BGB**), Rechten an **Trainingsdaten** und Output (**§ 44b UrhG**), den Pflichten aus der KI-VO und der Haftung für fehlerhaften KI-Output.

## Eingaben

- Vertragstyp (Kauf/Lizenz eines KI-Produkts, Werkvertrag KI-Entwicklung, SaaS/„KI-as-a-Service", Datenlieferung)
- Rolle des Mandanten (Anbieter / Betreiber / Datenlieferant)
- Einsatzkontext und KI-VO-Risikoklasse (verbotene Praktik, Hochrisiko, Transparenz, GPAI)
- Herkunft der Trainingsdaten (lizenziert, gescraped, Kundendaten, personenbezogen)
- Zugesicherte Leistungsmerkmale (Genauigkeit, Verfügbarkeit, Bias-Grenzen)
- Vorgesehene Haftungs- und Freistellungsklauseln

## Sub-Agent-Architektur

Die Gestaltung verteilt sich auf vier Rollen. Ein **Leistungs-Agent** übersetzt das KI-Verhalten in eine justiziable Leistungsbeschreibung (Metriken, Testdatensätze, Abnahmekriterien) und ordnet den Vertrag dem richtigen Gewährleistungsregime zu (§ 434 BGB Kauf, § 633 BGB Werk, § 327 BGB digitale Produkte). Ein **Daten-Agent** prüft die Rechtekette der Trainingsdaten, insbesondere die TDM-Schranke und den Nutzungsvorbehalt nach § 44b UrhG, sowie datenschutzrechtliche Rollen. Ein **Compliance-Agent** ordnet das System der KI-VO-Risikoklasse zu und verteilt die Anbieter-/Betreiberpflichten (Hochrisiko, Transparenz) vertraglich. Ein **Haftungs-Agent** gestaltet Haftung, Freistellung und Versicherung für fehlerhaften oder rechtsverletzenden Output. Aktenzeichen werden nicht erfunden; unklare Fundstellen erhalten `[unverifiziert – prüfen]`.

## Ablauf

### 1. Vertragstyp und Gewährleistung

| Konstellation | Recht | Gewährleistung |
|---|---|---|
| Kauf/Dauerlizenz eines KI-Produkts | § 433 ff. BGB | **§ 434 BGB** (Sachmangel, Beschaffenheit) |
| Individuelle KI-Entwicklung | § 631 ff. BGB | **§ 633 BGB** (Werk, Abnahme) |
| KI-as-a-Service / digitales Produkt an Verbraucher | § 327 ff. BGB | **§ 327 BGB** (Aktualisierungspflicht) |

Beschaffenheit präzise vereinbaren: Genauigkeitskennzahlen, Testdatensatz, akzeptable Fehlerquote — sonst Streit über den Mangelbegriff bei probabilistischem Output.

### 2. Trainingsdaten und Rechte (§ 44b UrhG)

- **Text-und-Data-Mining**: § 44b UrhG erlaubt Vervielfältigungen zum TDM, **außer** der Rechteinhaber hat sich die Nutzung wirksam vorbehalten (Opt-out); bei online zugänglichen Werken nur in maschinenlesbarer Form wirksam.
- Wissenschaftliche TDM-Schranke (§ 60d UrhG) für nichtkommerzielle Forschung.
- Vertraglich: Zusicherung der Rechtekette, Freistellung bei Drittrechten, Klärung der Rechte am Output und an Feinabstimmungsdaten.
- Personenbezogene Trainingsdaten: Rollen und Rechtsgrundlage nach DSGVO klären (Schnittstelle zum AVV/Cloud-Skill).

### 3. KI-VO-Verzahnung

- Risikoklasse bestimmen: verbotene Praktik, **Hochrisiko**-KI (Anhang III / Produktsicherheit), Transparenzpflicht-System, GPAI.
- **Transparenzpflichten** (Kennzeichnung KI-Interaktion, synthetische Inhalte) vertraglich zuweisen.
- Bei Hochrisiko-KI: Pflichten zu Risikomanagement, Daten-Governance, technischer Dokumentation, Aufsicht — Verteilung zwischen Anbieter und Betreiber regeln, Informations- und Mitwirkungspflichten verankern.

### 4. Haftung für KI-Output

- Fehlerhafter Output (Falschaussagen/„Halluzination"), diskriminierende Entscheidungen, Rechtsverletzungen Dritter.
- Haftungscap, Ausnahmen (Vorsatz, grobe Fahrlässigkeit, Leib/Leben), Freistellung für IP-Verletzungen durch Trainingsdaten/Output.
- Menschliche Letztkontrolle und Nutzungsgrenzen als Obliegenheit des Betreibers festschreiben.

## Risiken / typische Fehler

- **Halluzination** ohne Regelung — ohne vereinbarte Genauigkeitsmetrik und Letztkontrollpflicht trägt der Betreiber das Risiko fehlerhafter Outputs allein.
- **Opt-out** der Rechteinhaber ignoriert — Training auf Werken trotz wirksamem Nutzungsvorbehalt verletzt § 44b UrhG und begründet Freistellungsansprüche.
- **Hochrisiko-KI** falsch eingeordnet — unterbliebene Zuweisung der KI-VO-Pflichten lässt Compliance-Lücken und Bußgeldrisiken offen.
- **Gewährleistungsausschluss** zu weit — pauschaler Ausschluss für KI-Mängel scheitert an § 434/§ 633 BGB und der AGB-Inhaltskontrolle.

## Ausgabeformat

```
KI-VERTRAG — <Bezeichnung / Rolle> — <Datum>

I.    Vertragstyp & Gewährleistung
      Regime:                     [§ 434 / § 633 / § 327 BGB]
      Leistungsbeschreibung:      [metrisch / unbestimmt]
II.   Trainingsdaten (§ 44b UrhG)
      Rechtekette / Opt-out:      [geprüft / 🔴 offen]
      Output-Rechte:              [geregelt / offen]
III.  KI-VO
      Risikoklasse:               [verboten / Hochrisiko / Transparenz / GPAI]
      Pflichtenverteilung:        [✓ / 🔴]
IV.   Haftung
      Cap / Ausnahmen:            <…>
      Freistellung IP/Output:     [✓ / 🔴]
      Letztkontrolle Betreiber:   [festgeschrieben / fehlt]

Handlungsempfehlung:              <…>
```

## Quellen

- [§ 434 BGB](https://www.gesetze-im-internet.de/bgb/__434.html), [§ 633 BGB](https://www.gesetze-im-internet.de/bgb/__633.html), [§ 327 BGB](https://www.gesetze-im-internet.de/bgb/__327.html) (Gewährleistung / digitale Produkte)
- [§ 44b UrhG](https://www.gesetze-im-internet.de/urhg/__44b.html) (Text und Data Mining), [§ 60d UrhG](https://www.gesetze-im-internet.de/urhg/__60d.html) (Forschung)
- [KI-VO – Verordnung (EU) 2024/1689](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R1689) (Hochrisiko, Transparenz, GPAI)
- [Art. 28 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679) (bei personenbezogenen Trainings-/Eingabedaten)
- Produkthaftungs- und KI-Haftungsregeln (EU) `[unverifiziert – prüfen]`
