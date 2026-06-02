---
name: legalsearchqa-eval
title: legalsearchqa-eval
description: Evaluates a system's ability to retrieve up-to-date legal information from external sources and reason over it to answer multiple-choice legal questions. It probes factual accuracy, uncertainty calibration, and evidence grounding in dynamic legal domains like federal executive orders and tax provisions. Use when the user wants to benchmark on LegalSearchQA, or asks about evaluating this task. Reports Accuracy.
author: qhjqhj00
author_url: https://github.com/qhjqhj00/research-skills-pool/tree/master/skill-factory/output/legalsearchqa-eval
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: general
language: en
---

# legalsearchqa-eval

> L-MARS: Legal Multi-Agent Workflow with Orchestrated Reasoning and Agentic Search — Wang et al. (2025) (arXiv:2509.00761, 2025)

## What this evaluates

Evaluates a system's ability to retrieve up-to-date legal information from external sources and reason over it to answer multiple-choice legal questions. It probes factual accuracy, uncertainty calibration, and evidence grounding in dynamic legal domains like federal executive orders and tax provisions.

## Datasets

- **LegalSearchQA** — total 200; splits: test (200); repo https://github.com/boqiny/L-MARS

## Metrics

- `Accuracy` **(primary)** — range: [0, 1]
  - Fraction of multiple-choice questions answered correctly against expert-annotated ground truth.
- `U-Score` — range: [0, 1]
  - Rule-based uncertainty metric: 0.25*H + 0.20*T + 0.25*(1-C) + 0.15*(1-J) + 0.15*(1-D), where H=hedging, T=temporal vagueness, C=citation sufficiency, J=jurisdictional specificity, D=decisiveness. Ranges [0,1]; lower is better.
- `LLM-as-Judge` — range: categorical (low/moderate/high)
  - GPT-o3 evaluates answers on factual accuracy, evidence grounding, clarity of reasoning, and uncertainty calibration. Each response receives a holistic rating of low, moderate, or high, determined by majority vote.

## Input / output format

**Input**: A legal multiple-choice question referencing 2025 legal status, requiring retrieval from external sources.

**Output**: A multiple-choice answer and a supporting explanation, aggregated into structured JSON.

## Scoring recipe

```python
def compute_metrics(predictions, gold_answers):
    accuracy = sum(1 for p, g in zip(predictions, gold_answers) if p == g) / len(predictions)
    H = measure_hedging(predictions)
    T = measure_temporal_vagueness(predictions)
    C = measure_citation_sufficiency(predictions)
    J = measure_jurisdictional_specificity(predictions)
    D = measure_decisiveness(predictions)
    u_score = 0.25*H + 0.20*T + 0.25*(1-C) + 0.15*(1-J) + 0.15*(1-D)
    judge_ratings = [gpt_o3_judge(q, p) for q, p in zip(questions, predictions)]
    final_rating = mode(judge_ratings)
    return accuracy, u_score, final_rating
```

## Common pitfalls

- U-Score is lower-better, unlike standard accuracy metrics, which can invert interpretation if not explicitly noted.
- Questions explicitly require 2025 legal status, so models relying on pre-2025 training data will fail regardless of reasoning ability.
- LLM-as-Judge uses GPT-o3 for holistic rating rather than exact string matching, requiring careful prompt engineering to avoid bias or inconsistency.

## Evidence (verbatim from paper)

> We employ a comprehensive evaluation framework that combines automated metrics with LLM-based judgment to capture both quantitative and qualitative aspects of LegalSearchQA. Accuracy measures the fraction of multiple choice questions answered correctly against expert-annotated ground truth... We propose U-Score, a rule-based metric for the evaluation of legal QA systems based on uncertainty. It ranges from 0 to 1 (lower is better) and captures reliability across five complementary dimensions... LLM-as-Judge complements these metrics with qualitative ratings using GPT-o3, evaluating answers along four dimensions... Each response is assigned an overall rating of low, moderate, or high, reflecting the holistic quality of legal reasoning.

## Citation

```bibtex
@misc{wang2025lmars,
  title={L-MARS: Legal Multi-Agent Workflow with Orchestrated Reasoning and Agentic Search},
  author={Wang et al. (2025)},
  year={2025},
  note={arXiv:2509.00761}
}
```

- arXiv: 2509.00761
