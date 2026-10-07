---
name: eu-business-compliance-panyeroa1
title: EU Business Compliance (GDPR & Belgian Law)
description: Check documents for GDPR compliance, analyze data processing agreements, and ensure Belgian business law compliance using Ollama cloud models for intelligent legal analysis.
author: panyeroa1
author_url: https://github.com/panyeroa1/maxpc/tree/main/skills/eu-business-compliance
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: be
practice: data-protection
language: en
---

# EU Business Compliance (GDPR & Belgian Law)

## Description
Check documents for GDPR compliance, analyze data processing agreements, and ensure Belgian business law compliance using Ollama cloud models for intelligent legal analysis.

## Installation

```bash
# Install required dependencies
pip install python-docx pdfminer.six ollama
```

## Configuration

Add to `.env`:
```bash
OLLAMA_CLOUD_URL=https://api.cloud.ollama.com/v1
OLLAMA_CLOUD_API_KEY=your-api-key
PREFERRED_MODEL=llama3-70b-instruct
COMPLIANCE_LANGUAGE=nl  # nl | fr | de | en (auto-detects if not set)
```

## Usage

### Check contract for GDPR compliance
```bash
eu-business-compliance check-gdpr contract.pdf --detailed-analysis --language fr
```

### Analyze data processing agreement
```bash
eu-business-compliance analyze-dpa dpa_agreement.pdf --highlight-risks
```

### Check Belgian business law compliance
```bash
eu-business-compliance check-belgian-law document.docx --business-type bvba
```

### Generate GDPR-compliant cookie policy
```bash
eu-business-compliance generate-cookie-policy --output cookie-policy.md
```

### Scan website for GDPR compliance
```bash
eu-business-compliance scan-website https://example.com --output report.json
```

## Features

- **Multi-language support**: Dutch (Flemish), French, German, English
- **Ollama cloud integration**: Uses intelligent legal analysis
- **Risk scoring**: High/low risk categorization
- **Report generation**: PDF and Markdown outputs
- **Belgian law specifics**: BVBA, NV, SPRL compliance
- **GDPR rights assessment**: Data subject rights verification

## Examples

### Quick GDPR Check
```bash
eu-business-compliance quick-check contract.pdf --risk-score
```

Output shows compliance score, risk areas, and recommendations.

### Generate Privacy Policy
```bash
eu-business-compliance generate-privacy-policy --domain example.be --language nl --output privacy-policy-nl.md
```

## Integration with OpenClaw

Commands are automatically registered as OpenClaw tools:
- `eu-business-compliance check-gdpr`
- `eu-business-compliance analyze-dpa`
- `eu-business-compliance check-belgian-law`
- `eu-business-compliance generate-cookie-policy`
- `eu-business-compliance scan-website`
- `eu-business-compliance quick-check`
- `eu-business-compliance generate-privacy-policy`

## Model Recommendations

For legal analysis, use:
- `llama3-70b-instruct`: Well-balanced for legal documents
- `mistral-large`: Excellent for multilingual legal text
- `mixtral-8x22b`: Best for complex contract analysis

## Belgian Business Types

- BVBA (Besloten Vennootschap met Beperkte Aansprakelijkheid)
- NV (Naamloze Vennootschap)
- SPRL/SPRL-S (Société Privée à Responsabilité Limitée)
- SRL (Société à Responsabilité Limitée)
- SC(BVBA)/SC(SRL) (Société Coopérative)
