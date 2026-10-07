---
name: contract-law-reviewer-panyeroa1
title: Contract Law Reviewer
description: Intelligent contract analysis for EU and Belgian business law. Identifies risks, suggests improvements, and ensures legal compliance using Ollama cloud models.
author: panyeroa1
author_url: https://github.com/panyeroa1/maxpc/tree/main/skills/contract-law-reviewer
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: be
practice: contracts
language: en
---

# Contract Law Reviewer

## Description
Intelligent contract analysis for EU and Belgian business law. Identifies risks, suggests improvements, and ensures legal compliance using Ollama cloud models.

## Installation

```bash
pip install python-docx pdfminer.six pypdf2 ollama
```

## Configuration

Add to `.env`:
```bash
OLLAMA_CLOUD_URL=https://api.cloud.ollama.com/v1
OLLAMA_CLOUD_API_KEY=your-api-key
LEGAL_MODEL=llama3-70b-instruct
ALTERNATIVE_MODEL=mistral-large
JURISDICTION=BE  # Belgium
LANGUAGES=nl,fr,de,en
```

## Usage

### Full contract review
```bash
contract-law-reviewer review \
  contract.pdf \
  --contract-type service-agreement \
  --jurisdiction Belgium \
  --output review_report.md \
  --risk-levels high,medium
```

### Risk analysis
```bash
contract-law-reviewer risk-scan \
  agreement.docx \
  --focus-areas payment,liability,tax \
  --score-risks \
  --output risk_matrix.json
```

### Clause extraction
```bash
contract-law-reviewer extract \
  partnership_contract.docx \
  --clauses non-compete,confidentiality,termination \
  --format json
```

### Compare contracts
```bash
contract-law-reviewer compare \
  contract_v1.docx contract_v2.docx \
  --highlight-changes \
  --analyze-impact \
  --output comparison_report.html
```

### Generate contract templates
```bash
contract-law-reviewer template \
  --type nda \
  --jurisdiction Belgium \
  --language nl \
  --entity-type bvba \
  --output nda_template_bvba.docx
```

### Check for unfair clauses
```bash
contract-law-reviewer check-unfair \
  consumer_contract.pdf \
  --jurisdiction Belgium \
  --consumer-law-check \
  --flag-potentially-illegal
```

## Features

- **Belgian Law Focus**: BVBA, NV, SPRL-S specific clauses
- **EU Directives**: Unfair Contract Terms Directive, Consumer Rights Directive
- **Multi-language**: Dutch (Flemish), French, German, English
- **Risk Scoring**: High/medium/low risk categorization
- **Clause Library**: Standard Belgian/EU contract clauses
- **Template Generation**: Ready-to-use templates for Belgian businesses
- **Smart Comparisons**: AI-powered change analysis
- **Legal Research**: Integration with legal databases

## Belgian Contract Types

### Commercial Contracts
- **Services (Dienstverlening/Prestations)**
- **Sales (Verkoop/Vente)**
- **Partnership (Partnerschap/Association)**
- **Distribution (Distributie/Distribution)**

### Corporate Documents
- **Statuten/Statuts** (Articles of Association)
- **Aandeelhoudersovereenkomst/Convention d'Actionnaires** (Shareholders' Agreement)
- **Directieovereenkomst/Convention de Direction** (Management Agreement)

### Employment
- **Arbeidsovereenkomst/Contrat de Travail** (Employment Contract)
- **Consultantovereenkomst/Contrat de Consultant** (Consultant Agreement)
- **Non-concurrentiebeding/Clause de Non-concurrence** (Non-compete)

### Commercial Real Estate
- **Huurovereenkomst/Bail Commercial** (Commercial Lease)
- **Koopovereenkomst/Compromis** (Purchase Agreement)

## Risk Categories

### High Risk
- Unlimited liability clauses
- Unilateral termination without compensation
- Confidentiality without reasonable duration
- Missing governing law clause

### Medium Risk
- Unclear payment terms
- No dispute resolution clause
- Missing data protection compliance
- Ambiguous intellectual property ownership

### Low Risk
- Minor language inconsistencies
- Formatting issues
- Missing definitions for secondary terms

## Examples

### Quick Contract Review
```bash
contract-law-reviewer quick \
  consultant_agreement.pdf \
  --business-type sprl-s \
  --language fr \
  --check-vat-compliance
```

Output shows red/yellow/green issues with explanations and suggested fixes.

### Standard NDA Generation
```bash
contract-law-reviewer generate \
  --type nda \
  --duration 3 \
  --mutual \
  --jurisdiction Antwerp \
  --language nl \
  --entity-type bvba \
  --output nda_mutual_bvba_antwerp.docx
```

### Employment Contract Check
```bash
contract-law-reviewer employment-check \
  employe_contract.pdf \
  --check-compliants-with-belgian-labor-law \
  --seniority-level junior \
  --contract-type fixed-term \
  --output compliance_check.json
```

## Integration with OpenClaw

All commands registered as tools:
- `contract-law-reviewer review`
- `contract-law-reviewer risk-scan`
- `contract-law-reviewer extract`
- `contract-law-reviewer compare`
- `contract-law-reviewer template`
- `contract-law-reviewer check-unfair`
- `contract-law-reviewer quick`
- `contract-law-reviewer generate`
- `contract-law-reviewer employment-check`

## Model Recommendations

- **llama3-70b-instruct**: Best for legal reasoning and contract analysis
- **mistral-large**: Excellent for multi-language legal documents
- **mixtral-8x22b**: Superior for complex contract reviews and risk assessment

All models trained on EU/Belgian legal frameworks and multilingual capabilities.
