# Configuration Reference

## Mode Selection

### Single-model mode
Both agents use the same model with different system prompts. Agent A is methodical, Agent B is adversarial. Cheaper but shares model blind spots.

Best for: routine checks, internal drafts, quick validation.

### Cross-model mode
Agent A and Agent B use different model providers. Genuinely different training data = different blind spots.

Best for: client-facing work, high-stakes deliverables, anything where shared blind spots are a real risk.

Supported provider combinations (any pair):
- Anthropic (Claude Sonnet, Opus, Haiku)
- OpenAI (GPT-4o, GPT-4.1, o3)
- Google (Gemini 2.5 Pro, Flash)

## Model Recommendations

| Use case | Agent A | Agent B | Why |
|----------|---------|---------|-----|
| Quick routine check | Sonnet | — (single mode) | Cheap, fast |
| Standard review | Sonnet | Sonnet (different persona) | Good balance |
| Cross-model standard | Sonnet | GPT-4o-mini | Different perspectives, low cost |
| High-stakes | Opus | GPT-4.1 | Maximum coverage |
| Budget-conscious cross | Haiku | Flash | Cross-model benefits at minimum cost |

## Depth Levels

### Quick (~30 seconds)
- 5-item core checklist only
- Single pass, no source re-verification
- Good for: emails, short messages, simple scripts

### Standard (~2 minutes)
- Full 12-item checklist
- Type-specific additions applied
- Good for: reports, plans, analysis, code

### Deep (~5 minutes)
- Full 17-item checklist including re-verification
- Adversarial read pass
- Staleness and hedging audits
- Good for: legal filings, financial reports, published content

## Output Formats

### Inline
Text summary in chat. Format:
```
QC Summary: [deliverable name]
✅ X passed | ❌ Y failed | ⚠️ Z need review
[List of fails and reviews with one-line evidence each]
```

### Certificate (PDF)
Full QC certificate with:
- Deliverable identification (name, type, date, author)
- Mode and models used
- Full checklist results with evidence
- Agreement/disagreement matrix
- Items flagged for human review
- Timestamp and agent signatures

### Custom
User provides their own output format or template.
