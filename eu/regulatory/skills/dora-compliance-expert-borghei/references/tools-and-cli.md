# DORA Tools — Usage & CLI Reference

Full command examples, feature lists, and flag-by-flag reference for the two Python scripts (`dora_readiness_checker.py`, `dora_incident_classifier.py`). Read this when running an assessment, classifying an incident, or scripting the tools into automation.

---

## DORA Readiness Checker

Assesses organizational readiness against all 5 DORA pillars with per-pillar scoring.

```bash
# Generate assessment template
python scripts/dora_readiness_checker.py --template > assessment.json

# Run full readiness assessment
python scripts/dora_readiness_checker.py --config assessment.json

# Assess specific pillars only
python scripts/dora_readiness_checker.py --config assessment.json --pillars 1 3 4 --json

# Generate report with JSON output
python scripts/dora_readiness_checker.py --config assessment.json --output readiness_report.json --json
```

**Features:**
- Assessment against all 5 DORA pillars
- Per-pillar readiness scoring (0–100)
- Overall readiness score
- ICT risk management framework validation
- Incident management readiness check
- Third-party risk management assessment
- Resilience testing program evaluation
- Gap analysis with prioritized remediation recommendations

---

## DORA Incident Classifier

Classifies ICT incidents per DORA criteria and determines reporting obligations.

```bash
# Classify an incident interactively
python scripts/dora_incident_classifier.py --clients-affected 5000 --duration-hours 4 --data-loss yes --services-critical yes --economic-impact 500000

# Classify from JSON input
python scripts/dora_incident_classifier.py --config incident.json --json

# Generate incident notification template
python scripts/dora_incident_classifier.py --config incident.json --generate-template --output notification.json
```

**Features:**
- Incident classification per Article 18 criteria
- Major incident determination
- Reporting deadline calculation (4h initial, 72h intermediate, 1 month final)
- Incident notification template generation
- Severity scoring and impact assessment

---

## Tool Reference

### dora_readiness_checker.py

Assesses organizational readiness against all 5 DORA pillars with per-pillar scoring and gap analysis.

| Flag | Required | Description |
|------|----------|-------------|
| `--config <file>` | Yes (unless `--template`) | Path to JSON assessment configuration file |
| `--template` | No | Generate blank assessment template to stdout |
| `--pillars <nums>` | No | Assess specific pillars only (e.g., `--pillars 1 3 4`) |
| `--json` | No | Output results in JSON format for automation |
| `--output <file>` | No | Export report to specified file path |

**Output:** Overall readiness score (0-100), per-pillar readiness scores, ICT risk management framework validation, incident management readiness, third-party risk assessment, resilience testing evaluation, and prioritized remediation recommendations.

### dora_incident_classifier.py

Classifies ICT incidents per DORA Article 18 criteria and determines reporting obligations.

| Flag | Required | Description |
|------|----------|-------------|
| `--config <file>` | No | Path to JSON incident description file |
| `--template` | No | Generate blank incident input template to stdout |
| `--clients-affected <num>` | No | Number of clients/financial counterparts affected |
| `--duration-hours <num>` | No | Duration of the incident in hours |
| `--data-loss <yes/no>` | No | Whether data loss occurred (availability, integrity, or confidentiality) |
| `--services-critical <yes/no>` | No | Whether critical or important functions were affected |
| `--economic-impact <num>` | No | Estimated economic impact in EUR |
| `--json` | No | Output results in JSON format |
| `--generate-template` | No | Generate incident notification template for competent authority |
| `--output <file>` | No | Export report or template to specified file path |

**Output:** Incident severity scoring per Article 18 criteria, major incident determination, reporting deadline calculation (initial 4h, intermediate 72h, final 1 month), and notification template generation.
