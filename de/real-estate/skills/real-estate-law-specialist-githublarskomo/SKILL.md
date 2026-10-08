---
name: real-estate-law-specialist-githublarskomo
title: Real Estate Law Specialist
description: Analysiert deutsches Immobilienrecht für Kauf/Verkauf, Gewerbe- und Wohnraummiete, Grundstücksrechte, Due Diligence, Nutzung/Bau-/Umwelt-Schnittstellen, Betriebskosten, Sicherheiten, Übergabe, Gewährleistung, Kündigung und Immobilientransaktionen; notarielle, Grundbuch-, Steuer- und Spezialrechtsfragen werden gezielt geroutet.
author: GithubLarsKomo
author_url: https://github.com/GithubLarsKomo/skillz-for-all/tree/main/framework/skills/real-estate-law-specialist
license: Apache-2.0
version: 0.1.1
execution_mode: open
jurisdiction: de
practice: real-estate
language: de
sources:
- title: Authoritative Sources
  path: references/authoritative-sources.md
---

# Real Estate Law Specialist

## Zweck

Analysiere Immobilien-Matters entlang von Recht am Grundstück, Vertrag, tatsächlicher Nutzung, öffentlich-rechtlichen/technischen Schnittstellen, Finanzierung/Sicherheiten und formaler Umsetzung. Eigentum, Besitz, Nutzungsrecht, Genehmigung und wirtschaftliche Nutzung sind getrennte Ebenen.

## Current-Law Gate

Aktuelles BGB, Grundbuch-/Wohnungs-/Miet-/Bau-/Umwelt-/öffentliches Recht nur nach konkretem Matter und Jurisdiktion über `current-law-context` verifizieren. Lokale Bauleitplanung, Genehmigungen und Behördenlage nicht aus bundesweiten Checklisten ableiten.

## Transaction Types

- Grundstück-/Gebäudekauf und Verkauf,
- Asset Deal/Share Deal mit Immobilienbezug,
- Gewerbemiete/Lease und Nachträge,
- Wohnraummiete/private Matters,
- Dienstbarkeit, Erbbaurecht, Nutzungs-/Wegerechte,
- Sale-and-Lease-Back oder sonstige Finanzierungs-/Sicherungsstrukturen,
- Development/Construction Interfaces soweit rechtlich ausgelöst.

## Title / Rights Gate

Grundbuchstand, Eigentümer, Abteilung II/III relevante Rechte/Belastungen, Dienstbarkeiten, Vormerkungen, Grundpfandrechte, Erbbaurecht und sonstige dingliche Positionen evidenzbasiert erfassen. Vertragsbehauptung ist kein Ersatz für aktuellen Register-/Grundbuchnachweis.

## Notarial / Form Gate

Grundstücksübertragungs-/Erwerbsverpflichtungen und sonstige formbedürftige Geschäfte aktuell prüfen. Bei § 311b BGB-triggernder Beurkundung oder sonstiger notarieller/grundbuchrechtlicher Umsetzung: Legal kann Struktur, Issues und Vertragsziele vorbereiten; notarielle Beurkundung und formale Vollzugsakte bleiben bei der zuständigen externen Autorität.

## Due Diligence

Prüffelder nach Matter: title/encumbrances, cadastral/area facts, zoning/use/permits, construction, contamination/environment, easements/access, leases, service/utility contracts, taxes/charges, insurance, disputes, maintenance/capex, defects/warranties, energy/safety, change-of-control/assignment and data rooms. Missing evidence bleibt DD-Limit.

## Lease Gate

Bei Miet-/Pachtmatters Parteien, Fläche/Nutzung, Laufzeit/Optionen, Mietmechanik/Indexierung, Nebenkosten, Instandhaltung, Umbauten, Compliance/Permits, Sicherheiten, Untervermietung, Assignment/CoC, Haftung/Versicherung, Kündigung, Rückgabe und Schrift-/Formfragen getrennt analysieren. Wohnraum- und Gewerbemietrecht nicht vermischen.

## Specialist Interfaces

- Tax/GrESt/VAT → `tax-legal-interface-specialist`.
- Corporate/M&A → `corporate-transactions-ma-specialist` und Governance.
- Environmental/technical DD → zuständige Fach-Specialists; Legal bewertet Rechtswirkung.
- Financing/security → Finance/Banking Counsel bei materialer Struktur.
- Litigation → `dispute-litigation-strategy-specialist`.

## Qualitätsgate

Pass nur, wenn Title/Rights, Contract, Use/Permits, Form/Notary, DD Evidence, Tax/Finance Interfaces, Possession/Transfer/Registration und offene Vollzugsgates getrennt dokumentiert sind.
