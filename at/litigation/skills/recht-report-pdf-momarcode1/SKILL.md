---
name: recht-report-pdf-momarcode1
title: /recht report-pdf -- PDF-Bericht generieren
description: Generates professional PDF reports with risk scores, cost estimates, and recommendations using ReportLab. Austrian law branding.
author: MoMarcode1
author_url: https://github.com/MoMarcode1/austrian-legal-claude/tree/main/skills/recht-report-pdf
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: at
practice: litigation
language: de
---

# /recht report-pdf -- PDF-Bericht generieren

Generates a professional PDF legal report from all previous /recht analysis results in the current conversation. Combines contract review scores, risk analysis, claim identification, evidence evaluation, cost calculations, litigation strategy, and compliance findings into a single branded PDF document.

---

## Step 1: Check Prerequisites

Before anything else, verify that the `reportlab` Python package is available.

Run via Bash tool:
```bash
python3 -c "import reportlab; print(reportlab.Version)"
```

- If this succeeds: proceed to Step 2 (RIS Verification) and then Step 3.
- If this fails with `ModuleNotFoundError`: STOP. Tell the user:

> reportlab ist nicht installiert. Bitte fuehren Sie folgenden Befehl aus:
> ```
> pip3 install reportlab
> ```
> Danach koennen Sie `/recht report-pdf` erneut ausfuehren.

Do NOT proceed without reportlab. Do NOT attempt to install it automatically.

Also verify the PDF generation script exists. Check for `scripts/generate_legal_pdf.py` relative to the project root (the directory containing CLAUDE.md for this project). If it does not exist, tell the user the script is missing and cannot proceed.

---

## Step 2: RIS Verification

Before proceeding with analysis, follow the **RIS Verification Protocol** (`references/ris-protocol.md`):
1. Check RIS MCP availability
2. For every § you cite in this analysis, verify current wording via RIS
3. For case law references, retrieve via RIS Justiz
4. Record verification status for the Quellenstatus block
5. If RIS is unavailable, follow the fallback ladder and flag all affected citations

---

## Step 3: Collect Data from Current Session

Review the ENTIRE current conversation history and gather ALL results from previous /recht commands. You must look for outputs from each of the following sub-commands. For each one found, extract the structured data described below.

### 3a: From /recht review (Vertragspruefung)

Look for:
- **Vertragssicherheits-Score**: the numeric score (0-100) and letter grade (A-F)
- **Risk dashboard counts**: number of critical (rot), important (gelb), and standard (gruen) findings
- **Clause-by-clause analysis**: each analyzed clause with its risk level, identified problem, applicable law reference (paragraph citations), and recommendation
- **Formulierungsvorschlaege**: any suggested replacement text for problematic clauses
- **Document metadata**: document name, document type (Kaufvertrag, Mietvertrag, Arbeitsvertrag, AGB, etc.), parties involved

### 3b: From /recht risks (Risikoanalyse)

Look for:
- **Individual risk entries**: each risk with its severity level (critical/warning/ok), title, detailed description, legal basis (paragraph citations), and financial exposure estimate if provided
- **Risk categories**: contract law risks, consumer protection risks, procedural risks, enforcement risks

### 3c: From /recht claim (Anspruchspruefung)

Look for:
- **Identified claims (Anspruchsgrundlagen)**: each claim type with its legal basis
- **Tatbestandsmerkmale**: the elements required for each claim and whether they are met
- **Einwendungen und Einreden**: defenses and objections available to each side
- **Beweislast**: who bears the burden of proof for each element
- **Verjährung**: limitation periods applicable to each claim

### 3d: From /recht evidence (Beweiswuerdigung)

Look for:
- **Evidence items**: each piece of evidence with its classification per ZPO hierarchy (Urkunden, Zeugen, Sachverstaendige, Augenschein, Parteienvernehmung)
- **Beweiskraft**: assessment of probative value (stark/mittel/schwach)
- **Beweisluecken**: identified gaps in the evidence
- **Beweissicherung recommendations**: suggestions for preserving evidence

### 3e: From /recht costs (Kostenberechnung)

Look for:
- **Streitwert**: the amount in dispute
- **GGG (Gerichtsgebuehrengesetz)**: court fee calculation
- **RATG (Rechtsanwaltstarifgesetz)**: attorney fee calculation
- **Total first instance (Gesamtkosten 1. Instanz)**: combined costs
- **Total with appeal (Gesamtkosten mit Berufung)**: costs including appeal scenario
- **Prozesskostenrisiko**: total financial risk if the case is lost

### 3f: From /recht strategy (Prozessstrategie)

Look for:
- **Recommended strategy**: the primary litigation approach
- **Success probability (Erfolgswahrscheinlichkeit)**: percentage estimate with reasoning
- **Court recommendation**: BG vs LG, which specific court
- **Procedure type**: Mahnverfahren, Klage, einstweilige Verfuegung, etc.
- **Vergleichskorridor**: settlement range recommendation
- **Timeline**: expected duration
- **Next steps**: prioritized action items

### 3g: From /recht compliance (Compliance-Pruefung)

Look for:
- **Compliance score**: overall compliance percentage
- **Framework results**: for each framework checked (KSchG, DSGVO, UGB, etc.), the status and specific violations found
- **Individual violations**: each violation with its paragraph reference and severity

### CRITICAL CHECK

If NO previous /recht analysis results are found anywhere in the conversation, STOP immediately. Tell the user:

> Es wurden keine vorherigen Analyseergebnisse in dieser Sitzung gefunden. Bitte fuehren Sie zuerst eine Analyse durch, z.B.:
> ```
> /recht review vertrag.pdf
> /recht costs 50000
> /recht claim [Sachverhalt]
> ```
> Danach koennen Sie mit `/recht report-pdf` einen PDF-Bericht erstellen.

Do NOT generate a PDF with placeholder or demo data. Every data point in the PDF must come from an actual analysis performed in this conversation.

---

## Step 4: Structure the JSON Data

Assemble all collected data into a single JSON object matching the schema expected by `scripts/generate_legal_pdf.py`. Map the gathered results to the following structure:

```json
{
  "document_name": "<name of the analyzed document, or 'Rechtsanalyse' if general>",
  "document_type": "<Kaufvertrag|Mietvertrag|Arbeitsvertrag|AGB|Dienstvertrag|Werkvertrag|Allgemein>",
  "date": "<current date in DD.MM.YYYY format>",
  "user_party": "<name or role of the user's party, if identified>",

  "score": <0-100 integer from /recht review, or null if not available>,
  "grade": "<A-F grade from /recht review, or null if not available>",

  "risks": {
    "critical": <count of critical findings>,
    "warning": <count of important/warning findings>,
    "ok": <count of standard/ok findings>
  },

  "findings": [
    {
      "level": "critical|warning|ok",
      "title": "<clause name or risk title>",
      "description": "<full description including all paragraph citations, e.g. 'Verstoesst gegen §6 Abs 1 Z 9 KSchG...'>",
      "recommendation": "<recommended action or Formulierungsvorschlag>",
      "law_reference": "<primary paragraph citation, e.g. '§6 Abs 1 Z 9 KSchG'>",
      "financial_exposure": "<estimated financial risk, e.g. 'EUR 5.000-10.000', or null>"
    }
  ],

  "missing_clauses": [
    {
      "clause": "<name of missing clause>",
      "reason": "<why it should be included>",
      "risk": "<consequence of omission>"
    }
  ],

  "compliance": [
    {
      "framework": "<KSchG|DSGVO|UGB|GewO|etc.>",
      "status": "konform|teilweise|nicht konform",
      "violations": ["<specific violation 1>", "<specific violation 2>"]
    }
  ],

  "costs": [
    {"item": "Streitwert", "amount": "<EUR value>"},
    {"item": "Gerichtsgebuehr (GGG)", "amount": "<EUR value>"},
    {"item": "Eigene Anwaltskosten (RATG)", "amount": "<EUR value or range>"},
    {"item": "Gegnerische Anwaltskosten (RATG)", "amount": "<EUR value or range>"},
    {"item": "Gesamtkosten 1. Instanz", "amount": "<EUR value or range>"},
    {"item": "Gesamtkosten mit Berufung", "amount": "<EUR value or range>"},
    {"item": "Prozesskostenrisiko bei Unterliegen", "amount": "<EUR value or range>"}
  ],

  "claims": [
    {
      "type": "<Anspruchsgrundlage, e.g. 'Gewaehrleistung §922 ABGB'>",
      "elements_met": "<summary of which Tatbestandsmerkmale are satisfied>",
      "defenses": "<available Einwendungen>",
      "limitation": "<Verjaehrungsfrist and status>"
    }
  ],

  "evidence": [
    {
      "item": "<evidence description>",
      "type": "<Urkunde|Zeuge|Sachverstaendiger|Augenschein|Parteienvernehmung>",
      "strength": "stark|mittel|schwach",
      "notes": "<assessment notes>"
    }
  ],

  "strategy": {
    "approach": "<recommended litigation approach>",
    "success_probability": "<percentage>",
    "court": "<recommended court>",
    "procedure": "<recommended procedure type>",
    "settlement_range": "<Vergleichskorridor>",
    "timeline": "<expected duration>",
    "next_steps": ["<step 1>", "<step 2>", "<step 3>"]
  },

  "recommendations": [
    {
      "priority": <1-based integer, 1 = highest priority>,
      "action": "<what to do>",
      "clause": "<which clause this relates to, or null>",
      "formulierungsvorschlag": "<suggested replacement text, if applicable, or null>"
    }
  ]
}
```

### Data mapping rules:

1. Only include sections where actual analysis data exists. Omit keys with null/empty values rather than filling them with placeholders.
2. ALL paragraph citations (e.g., "§922 ABGB", "§6 Abs 1 Z 9 KSchG", "§1295 ABGB") from the original analyses MUST be preserved exactly as they appeared. Do not paraphrase or drop legal references.
3. If multiple analyses were run (e.g., both /recht review and /recht risks on the same document), merge their findings. Deduplicate findings that appear in both -- keep the more detailed version.
4. Risk counts in the `risks` object must accurately reflect the actual number of findings at each level, counted from the `findings` array.
5. Sort `recommendations` by priority (1 = most urgent).
6. Sort `findings` by severity: critical first, then warning, then ok.
7. Financial amounts must include "EUR" prefix and use Austrian formatting where possible (e.g., "EUR 5.000" not "EUR 5000").

---

## Step 5: Generate the PDF

### 5a: Write the JSON to a temporary file

Use the Bash tool to write the assembled JSON data to a temporary file. Use the project root directory as the working directory.

```bash
cat > /tmp/recht_report_data.json << 'JSONEOF'
<the complete JSON object from Step 4>
JSONEOF
```

### 5b: Run the PDF generation script

Execute the script with the temp file as input. The script takes two positional arguments: (1) input JSON path, (2) output PDF path.

```bash
python3 scripts/generate_legal_pdf.py /tmp/recht_report_data.json RECHT-BERICHT.pdf
```

Run this from the project root directory (the directory containing `scripts/`).

### 5c: Handle errors

If the script fails:
- **ImportError for reportlab**: Tell the user to install it: `pip3 install reportlab`
- **FileNotFoundError for the script**: Tell the user the script is missing at `scripts/generate_legal_pdf.py`
- **JSON decode error**: There is a bug in the JSON assembly from Step 4. Review and fix the JSON, then retry.
- **Any other error**: Show the full error output to the user and suggest they check the script for compatibility with the data format.

Do NOT silently swallow errors. Always show the user what went wrong.

---

## Step 6: Verify and Report

### 6a: Verify the PDF was created

```bash
ls -la RECHT-BERICHT.pdf
```

Confirm the file exists and has a non-zero size.

### 6b: Report to the user

Tell the user the PDF has been generated. Include:
- The absolute file path to the PDF
- A summary of what the report contains (which analyses were included)
- A reminder about the disclaimer

Example output:

> **PDF-Bericht erstellt:** `[absolute path]/RECHT-BERICHT.pdf`
>
> Der Bericht enthaelt:
> - Vertragssicherheits-Score: 62/100 (Note C)
> - 2 kritische, 3 wichtige, 8 Standard-Befunde
> - Kostenberechnung (Streitwert EUR 50.000)
> - 5 priorisierte Empfehlungen
>
> ## Quellenstatus
> | Kategorie | Status | Details |
> |-----------|--------|---------|
> | RIS MCP | 🟢 Verfügbar / 🔴 Nicht verfügbar | |
> | Gesetze | RIS_VERIFIED / UNVERIFIED | [n] Normen geprüft |
> | Judikatur | RIS_VERIFIED / UNVERIFIED | [n] Entscheidungen |
> | Prüfdatum | [YYYY-MM-DD] | |
>
> **Hinweis:** Dieses Dokument stellt keine Rechtsberatung dar und ersetzt nicht die Beratung durch einen Rechtsanwalt.

---

## Step 7: Clean Up

Remove the temporary JSON file:

```bash
rm -f /tmp/recht_report_data.json
```

---

## Critical Rules

1. **Never generate a PDF without actual analysis data.** If no /recht commands were run in this conversation, refuse and tell the user to run an analysis first. Do not use demo data, placeholder data, or invented findings.

2. **The PDF MUST include the disclaimer on every page.** The `scripts/generate_legal_pdf.py` script adds "Keine Rechtsberatung -- Dieses Dokument ersetzt nicht die Beratung durch einen Rechtsanwalt." as a footer on every page via the `add_footer` function. Do not modify or remove this behavior. If the script is modified, verify the disclaimer is still present.

3. **All paragraph citations must carry through from analysis to PDF.** Every legal reference (e.g., "§6 Abs 1 Z 9 KSchG", "§922 ABGB", "§1295 Abs 1 ABGB") that appeared in the original analysis output MUST appear in the PDF findings. Do not summarize away the legal citations. They are the most important part of each finding.

4. **If multiple analyses were run, combine them into one comprehensive report.** For example, if the user ran `/recht review`, then `/recht costs`, then `/recht strategy`, all three sets of results go into a single PDF. Deduplicate overlapping findings but keep the most detailed version of each.

5. **Report the output file path so the user can find it.** Always provide the absolute path. If the working directory might be ambiguous, use `pwd` to determine it and construct the full path.

6. **If reportlab is not installed, do not fail silently.** Explicitly tell the user what package to install and how (`pip3 install reportlab`). Do not attempt to generate the PDF without reportlab, and do not attempt to install packages on behalf of the user without their confirmation.

7. **Preserve Austrian legal formatting conventions.** Use German-language section headers in the JSON data (the script handles rendering). Use "EUR" for currency, Austrian number formatting with dots as thousands separators (EUR 5.000, not EUR 5,000), and German legal terminology throughout.

---

## Usage Examples

After a full contract review:
```
/recht review mietvertrag.pdf
/recht costs 25000
/recht report-pdf
```

After claim analysis and strategy:
```
/recht claim [Sachverhalt beschreiben]
/recht evidence [Beweismittel auflisten]
/recht strategy [Sachverhalt]
/recht report-pdf
```

Comprehensive analysis:
```
/recht review kaufvertrag.pdf
/recht risks kaufvertrag.pdf
/recht compliance kaufvertrag.pdf
/recht costs 100000
/recht strategy [Sachverhalt]
/recht report-pdf
```

The more /recht analyses you run before generating the PDF, the more comprehensive the report will be.
