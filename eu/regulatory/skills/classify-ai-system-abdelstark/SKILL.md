---
name: classify-ai-system-abdelstark
title: Interactive mode — asks questions step by step
description: Use when the user asks about EU AI Act risk classification, wants to know what risk tier their AI system falls under, or needs to understand which EU AI Act obligations apply to them. Triggers on questions about AI regulation, compliance classification, prohibited AI practices, GPAI obligations, or high-risk AI systems.
author: AbdelStark
author_url: https://github.com/AbdelStark/eu-ai-act-toolkit/tree/main/skills/classify-ai-system
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: regulatory
language: en
---

You are helping a user classify their AI system under the EU AI Act (Regulation 2024/1689). Use the @eu-ai-act/sdk or the `eu-ai-act` CLI to determine the correct risk tier and applicable obligations.

IMPORTANT: Always remind the user that this tool provides informational guidance only and does NOT constitute legal advice. They should consult qualified legal counsel for definitive compliance determinations.

## Setup

If the user is working in a Node.js project, install the SDK:

```
npm install @eu-ai-act/sdk
```

Alternatively, they can use the CLI directly with npx (no install needed):

```
npx eu-ai-act classify
```

## Gathering Information

Walk the user through the 5-step classification tree by asking targeted questions. Do NOT ask all questions at once — follow the decision tree and stop as soon as a classification is determined.

### Step 1: Prohibited Practices (Article 5)

Ask whether the AI system involves any of these prohibited practices:
- Social scoring by public authorities
- Real-time remote biometric identification in public spaces (by law enforcement, except narrow exceptions)
- Subliminal manipulation techniques that cause harm
- Exploitation of vulnerabilities of specific groups (age, disability, social situation)
- Facial recognition databases built by untargeted scraping
- Emotion inference in workplace or education (except medical/safety)
- Biometric categorization inferring sensitive attributes (race, political opinions, etc.)
- Predictive policing based solely on profiling

If YES to any: the system is classified as **prohibited**. Stop here.

### Step 2: General-Purpose AI (GPAI)

Ask whether the system is a general-purpose AI model (foundation model):
- Is it a model trained on broad data that can be adapted to a wide range of tasks?
- What is the estimated training compute (in FLOPs)? If >= 10^25 FLOPs, it may be GPAI with systemic risk.
- Is the model released under a free/open-source licence?

If YES: classify as **gpai** or **gpai-systemic** (if >= 10^25 FLOPs or designated by the Commission).

### Step 3: High-Risk Pathway A (Annex I)

Ask whether the AI system is a safety component of a product covered by EU harmonisation legislation listed in Annex I (e.g., machinery, toys, medical devices, vehicles, aviation, marine equipment, rail, lifts, pressure equipment, radio equipment, civil aviation).

If YES: classify as **high-risk**.

### Step 4: High-Risk Pathway B (Annex III)

Ask whether the AI system falls into any Annex III category:
- **biometrics** — remote biometric identification, biometric categorization, emotion recognition
- **critical-infrastructure** — safety components of critical infrastructure (water, gas, electricity, transport)
- **education** — access to education, student evaluation, exam proctoring
- **employment** — recruitment, hiring decisions, task allocation, performance monitoring, termination
- **essential-services** — credit scoring, insurance pricing, social assistance eligibility, emergency dispatch
- **law-enforcement** — risk assessment of individuals, polygraphs, evidence evaluation, crime prediction
- **migration** — border control, visa/asylum processing, risk assessment of migrants
- **justice-democracy** — judicial decision-making assistance, dispute resolution, election influence

If YES to any: classify as **high-risk**.

### Step 5: Limited Risk

Ask whether the AI system:
- Interacts directly with natural persons (chatbots, virtual assistants)
- Generates or manipulates synthetic content (deepfakes, AI-generated text/images/audio)
- Performs emotion recognition or biometric categorization (non-prohibited use cases)

If YES: classify as **limited**. Otherwise: classify as **minimal**.

## Using the SDK

Once you have gathered enough information, use the SDK programmatically:

```typescript
import { classify } from '@eu-ai-act/sdk';
import type { ClassificationInput, ClassificationResult } from '@eu-ai-act/sdk';

const result: ClassificationResult = classify({
  // Step 1: Prohibited practices (Article 5) — all required booleans
  socialScoring: false,
  realtimeBiometrics: false,
  subliminalManipulation: false,
  exploitsVulnerabilities: false,
  untargetedFacialScraping: false,
  emotionInferenceWorkplace: false,
  biometricCategorization: false,
  predictivePolicing: false,

  // Step 2: GPAI
  isGPAI: false,
  // gpaiFlops: 1e26,          // optional — systemic risk if >= 10^25
  // isOpenSource: true,        // optional — reduced obligations
  // designatedSystemicRisk: false, // optional

  // Step 3: High-risk Pathway A (Annex I)
  annexIProduct: false,
  // annexIRequiresThirdParty: false, // optional

  // Step 4: High-risk Pathway B (Annex III)
  annexIIICategory: 'employment',  // or null if not applicable
  // Options: 'biometrics' | 'critical-infrastructure' | 'education' | 'employment'
  //   | 'essential-services' | 'law-enforcement' | 'migration' | 'justice-democracy'

  // Step 5: Limited risk triggers
  interactsWithPersons: true,
  generatesSyntheticContent: false,
  emotionRecognition: false,
  biometricCategorizing: false,
});

console.log(result.tier);                // 'high-risk'
console.log(result.articles);            // [6, 9, 10, 11, 12, 13, 14, 15, ...]
console.log(result.enforcementDate);     // '2026-08-02'
console.log(result.conformityAssessment); // 'self' | 'third-party' | 'none'
console.log(result.obligations);         // Obligation[]
console.log(result.reasoning);           // string[] step-by-step explanation
```

## Using the CLI

The CLI provides the same classification via flags:

```bash
# Interactive mode — asks questions step by step
npx eu-ai-act classify

# Direct classification with flags
npx eu-ai-act classify --annex-iii employment --json

# GPAI with systemic risk threshold
npx eu-ai-act classify --gpai --flops 1e25 --json

# GPAI with open-source exemption
npx eu-ai-act classify --gpai --flops 1e24 --open-source --json

# Prohibited practice
npx eu-ai-act classify --social-scoring --json

# Limited risk
npx eu-ai-act classify --interacts-persons --synthetic-content --json
```

## Explaining the Result

After classification, explain to the user:

1. **Tier**: The risk tier (prohibited, high-risk, gpai-systemic, gpai, limited, minimal)
2. **Applicable Articles**: Which specific EU AI Act articles apply to their system
3. **Enforcement Date**: When obligations take effect (prohibited: Feb 2025, GPAI: Aug 2025, high-risk: Aug 2026, limited: Aug 2026)
4. **Conformity Assessment**: Whether they need internal assessment or third-party notified body assessment
5. **Key Obligations**: A summary of what they must do (risk management, data governance, documentation, human oversight, etc.)

## Suggest Next Steps

After classification, suggest:
- "Run `npx eu-ai-act checklist <tier>` to see all compliance obligations for your tier"
- "Run `npx eu-ai-act generate --tier <tier>` to generate compliance documentation templates"
- If high-risk: emphasize the 61 checklist items they need to address
- If GPAI: mention transparency obligations and model card requirements

## Disclaimer

Always end with: "This classification is generated by an automated tool for informational purposes. It does not constitute legal advice. Consult a qualified legal professional for definitive EU AI Act compliance guidance."
