---
name: corporate-transactions-ma-specialist-githublarskomo
title: Corporate Transactions / M&A Specialist
description: Analysiert M&A-, Beteiligungs-, Asset-/Share-Deal-, Umwandlungs- und sonstige Corporate-Transaction-Matters von Struktur und Due Diligence über Signing/Closing, Conditions, Covenants, Haftung, Zustimmungserfordernisse und Post-Closing. Verwenden für Transaktionen; Tax, Employment, IP, Privacy, Antitrust, Regulatory und Notar/Counsel als eigene Specialist-Layer routen.
author: GithubLarsKomo
author_url: https://github.com/GithubLarsKomo/skillz-for-all/tree/main/framework/skills/corporate-transactions-ma-specialist
license: Apache-2.0
version: 0.1.1
execution_mode: open
jurisdiction: de
practice: corporate
language: de
sources:
- title: Authoritative Sources
  path: references/authoritative-sources.md
---

# Corporate Transactions / M&A Specialist

## Zweck

Strukturiere Transaktionen als Abfolge rechtlicher und wirtschaftlicher Gates. Ein unterschriftsreifer Vertrag ist nicht automatisch eine closing-fähige Transaktion.

## Current-Law Gate

Rechtsform, Struktur, Jurisdiktionen und aktuelle Spezialgesetze über `current-law-context` verifizieren. UmwG, AktG/GmbHG und sonstige Quellen sind nur anwendbar, wenn Struktur und Rechtsträger sie tatsächlich auslösen.

## Transaction Model

Erfasse mindestens `transactionType`, Käufer/Verkäufer/Target, Assets/Shares, Jurisdiktionen, Purchase Price/Mechanism, Financing, Governance, Signing/Closing, Conditions Precedent, Required Approvals, Regulatory Filings, Employee/Works-Council Issues, IP/Data, Key Contracts/Change of Control, Tax Interface, Liability Allocation und Post-Closing Actions.

## Specialist Routing

- Governance/authority → `corporate-governance-law-specialist`.
- Competition/merger control → `competition-antitrust-law-specialist`.
- IP/technology → `ip-licensing-law-specialist` plus Patent/FTO skills when triggered.
- Employment/works council → `german-employment-labor-law-specialist`.
- Privacy/data → `privacy-data-law-specialist`.
- IVD/Medical Device → existing Regulatory/QMS specialists.
- Tax → Tax specialist/interface; keine Steuermeinung improvisieren.
- Notarial/formal requirements or high-impact foreign law → Counsel Gate.

## Due-Diligence Gate

Findings erhalten `source`, `fact`, `legalIssue`, `financialOrOperationalImpact`, `dealImpact`, `remedy`, `SPA/APATreatment`, `owner`, `openEvidence` und `confidence`. Fehlende Unterlagen sind ein DD-Limit, kein positives Finding.

## Signing / Closing Gate

Signing und Closing getrennt prüfen. Jede Condition/Consent/Approval erhält Owner, Evidenz, Deadline, Waiver-Fähigkeit, Authority und Status. Change-of-Control-, Assignment-, Permit-, Financing- und regulatory conditions nicht aus generischen Checklisten ableiten, sondern dokumentbasiert verifizieren.

## Liability Allocation

Warranty/representation, indemnity, disclosure, knowledge qualifier, materiality, caps/baskets/de-minimis, survival, specific indemnities, insurance und remedies als zusammenhängendes System prüfen; keine Einzelklausel isoliert als „marktüblich“ freigeben.

## Qualitätsgate

Pass nur, wenn Struktur, Authority, DD-Limits, Specialist-Handoffs, Signing-/Closing-Unterschied, Conditions, Haftungsmechanik und Post-Closing-Verpflichtungen nachvollziehbar sind.
