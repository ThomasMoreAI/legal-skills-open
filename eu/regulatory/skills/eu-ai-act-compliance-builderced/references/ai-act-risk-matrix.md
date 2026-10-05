# EU AI Act Risk Classification Matrix

Source: Regulation (EU) 2024/1689, Annex III

## Quick Assessment

| Your System | Risk Tier | Obligation |
|------------|-----------|------------|
| Social scoring, emotion detection in workplace | **Prohibited** | Cannot deploy |
| Biometric ID, credit scoring, recruitment AI | **High-Risk** | Full conformity assessment |
| Chatbot, content generator, voice synthesis | **Limited** | Transparency disclosure |
| Spam filter, game AI, inventory management | **Minimal** | None specific |

## Annex III High-Risk Categories

1. **Biometrics**: Remote biometric identification, categorization based on biometric data
2. **Critical Infrastructure**: AI managing water, gas, electricity, heating, transport safety
3. **Education**: Admission decisions, assessment of learning outcomes, monitoring of cheating
4. **Employment**: Recruitment, screening, interview evaluation, task allocation, promotion, termination
5. **Essential Services**: Credit scoring, insurance pricing, emergency dispatch prioritization
6. **Law Enforcement**: Evidence reliability assessment, lie detection, crime risk assessment, profiling
7. **Migration**: Polygraph, document authentication, visa/permit processing, risk assessment
8. **Justice**: Fact/law research, sentencing advisory, dispute resolution

## Decision Tree

```
Does your AI system process biometric data?
  YES → Likely HIGH-RISK (Category 1)
  NO ↓
Does it make decisions about people (hiring, credit, education)?
  YES → Likely HIGH-RISK (Categories 3-5)
  NO ↓
Does it interact with humans via chat, voice, or generated content?
  YES → LIMITED RISK (Article 50 transparency)
  NO ↓
→ MINIMAL RISK (no specific obligations)
```

## GPAI (General Purpose AI) Additional Rules

If deploying a foundation model or GPAI:
- Technical documentation on training process
- Copyright policy and training data summary
- Energy consumption reporting
- If "systemic risk" (>10^25 FLOPs): adversarial testing, incident reporting, cybersecurity measures
