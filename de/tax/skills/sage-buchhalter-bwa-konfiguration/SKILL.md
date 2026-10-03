---
name: sage-buchhalter-bwa-konfiguration
title: Sage Buchhalter BWA
description: 'Für Sage Buchhalter BWA: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Steuerrecht – Steuerberater und Anwälte. Route: sage-buchhalter-bwa-konfiguration.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/steuerrecht-anwalt-und-berater/skills/sage-buchhalter-bwa-konfiguration
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: tax
language: de
sources:
- title: Quellenhygiene
  path: references/quellenhygiene.md
- title: Zitierweise
  path: references/zitierweise.md
---

# Sage Buchhalter BWA

## Fachlicher Anker

- **Normen:** § 6a, § 14 UStG, § 146 AO.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Kernsachverhalt

Sage ist eine internationale ERP- und Buchhaltungsplattform, in Deutschland mit Sage 100, Sage 50 für KMU. Insbesondere bei mittelstaendischen Mandanten haeufig im Einsatz. BWA-Module sind äquivalent zu DATEV/Addison, aber mit anderer Bedienlogik. Steuerberater, die mit Sage-Mandanten arbeiten, brauchen Schnittstellen oder Datenuebernahme.

## Kaltstart-Rueckfragen

1. Welche Sage-Version (Sage 100, Sage 50, Sage Office Line)?
2. Wer betreibt Sage — Mandant selbst oder StB?
3. Welche BWA-Form ist konfiguriert?
4. Welcher Kontenrahmen (SKR 03, SKR 04, individuell)?
5. Welche Schnittstellen zu DATEV (falls vorhanden)?
6. Welche Module aktiv?
7. Welche Mandantenbeguenstigung?
8. Welcher Updates-Stand?

## Workflow

### Phase 1 — System-Setup

- Variante A: Mandant betreibt Sage selbst (Sage 50 Cloud, Sage 100, Sage Office Line); StB erhaelt Lese-Zugriff oder Monats-Export.
- Variante B: StB betreibt Sage als Service-Provider (selten; in der Regel DATEV-Bevorzugung in Kanzleien).
- Konten-Konfiguration: Sage unterstuetzt SKR 03/04 sowie eigene Kontenrahmen; Branchenkontenrahmen über Sage-Vorlagen.

### Phase 2 — BWA-Konfiguration

- Sage-Standard-BWA gliedert ueblicherweise nach Erloesen, variable Kosten, Deckungsbeitrag, Fixkosten, Betriebsergebnis (vergleichbar mit DATEV BWA 01).
- Vorjahresvergleich automatisch bei vorhandener Historie; Planwerte über das Sage-Planungsmodul.
- Anpassung der BWA-Zeilen über `Auswertungen → BWA → Konfiguration` (konkreter Programmpfad variiert je Sage-Version — im Zweifelsfall in der Sage-Onlinehilfe unter "BWA-Konfiguration" nachschlagen).

### Phase 3 — Schnittstellen

- Sage-eRechnung-Modul für XRechnung/ZUGFeRD-Empfang und -Versand (§ 14 UStG; siehe Skill `stb-erechnung-pflicht-b2b-2025-2026`).
- Bank-Anbindung über PSD2-Schnittstelle (HBCI/FinTS) oder Sage Banking.
- Export im DATEV-CSV-Format (DATEV ASCII-Format) über `Stammdaten → Datenexport → DATEV` (Programmpfad version-abhaengig).

### Phase 4 — Datenaustausch mit StB

- Standardisierter Monats-Export aus Sage; Termin- und Format-Vereinbarung schriftlich.
- StB-Seite: Import in DATEV Kanzlei-Rechnungswesen über `Datei → Datenuebernahme → Buchungsstapel`.
- Mapping-Tabelle Sage-Konten zu SKR 03/04 vorab abstimmen — Differenzen sonst pro Monat zu klären.

### Phase 5 — Lohn

- Sage HR / Sage Lohn als separate Module bzw. externes Lohnprogramm (DATEV LODAS, eGecko, etc.).
- Buchungssatz-Schnittstelle zum Hauptbuch (typischerweise monatlicher Buchungsbeleg).
- Bei Mandantenwechsel zu DATEV: Lohn meist parallel migriert (siehe `stb-lohn-mandantenaufnahme-onboarding`).

### Phase 6 — Updates

- Jaehrliche Programm-Updates zum 1. Januar (LSt/SV-Tabellen, USt-Änderungen, AfA-Tabellen).
- Sage Cloud-Versionen: automatische Updates über den Cloud-Anbieter.
- Update-Pflicht aus § 146 AO (Programm muss aktuelle Tabellen abbilden).

## Strategie und Praxis-Tipps

- Bei Sage-Mandanten Datenaustausch standardisieren — CSV-Export ist Standard.
- Datenuebernahme Sage zu DATEV ist Aufwand — Mandantenwechsel sorgfaeltig planen.
- Sage-Schulung über Sage-Akademie.

## Quellen und Updates

Stand: 05/2026.

- Sage Programm- und Bedienungsdokumentation (aktuelle Version prüfen).
- AO § 146 (Update-Pflicht der Buchfuehrungsprogramme).
- Hinweis: konkrete Programmpfade und Modulbezeichnungen können je Sage-Version abweichen; aktuelle Informationen in der Sage-Onlinehilfe prüfen.
