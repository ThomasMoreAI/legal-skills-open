---
name: gdpr-breach-notification-open-legal-products
title: GDPR Breach Notification
description: 'Run the personal data breach decision tree under GDPR Articles 33-34 and EDPB Guidelines 9/2022: classify the breach, assess risk to rights and freedoms, track the 72-hour notification deadline from awareness, decide on communication to data subjects, and draft the supervisory authority notification, the data subject communication, and the internal register entry. Use when a data leak, ransomware incident, misdirected email, or lost device raises the question of whether and whom to notify. The workflow drafts; the controller or DPO decides and sends.'
author: open-legal-products
author_url: https://github.com/open-legal-products/mike-workflows/tree/main/assistant-workflows/eu-gdpr-pack/gdpr-breach-notification
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: data-protection
language: en
---

# GDPR Breach Notification

In a breach, the clock and the documented reasoning are what matter. This workflow runs a documented decision tree and produces drafts; the decision to notify and the act of sending belong to the controller or DPO. Do not guess - flag missing inputs for the risk assessment as gaps.

## Step 1 - Is it a breach, and which type

A personal data breach is a breach of security leading to accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to personal data (Article 4(12)). Classify it as a confidentiality breach (disclosure or access), an integrity breach (alteration), or an availability breach (loss or destruction). Breaches are often combined - record every type that applies.

## Step 2 - Risk assessment to rights and freedoms

Assess against the factors in EDPB Guidelines 9/2022 (formerly WP250): type of breach; nature, sensitivity, and volume of the data; ease of identifying individuals; severity of consequences (identity theft, financial loss, discrimination, reputational harm); special characteristics of the individuals (children, patients); and the number of individuals affected. Record the outcome as one of three levels: no risk, risk, or high risk.

## Step 3 - Notify the supervisory authority (Article 33) within 72 hours

- The clock starts when the controller becomes aware of the breach, not when the incident occurred. The deadline is 72 hours from awareness. Compute the exact deadline date and time and state it in the draft and the register - do not estimate it.
- Notification is required unless the breach is unlikely to result in a risk to rights and freedoms (Article 33(1)). If not notifying, justify and document the decision.
- If the deadline has passed, notify anyway and state the reasons for the delay (Article 33(1), second sentence).
- Draft the notification to the content required by Article 33(3): nature of the breach with categories and approximate numbers of data subjects and records, DPO contact details, likely consequences, and measures taken or proposed. Notification in phases is allowed (Article 33(4)).

## Step 4 - Communicate to data subjects (Article 34)

If the risk is high, the controller must communicate the breach to the affected individuals without undue delay, in clear and plain language, covering the elements of Article 34(2): description of the breach, DPO contact, likely consequences, and measures. Check the exemptions in Article 34(3): safeguards that render the data unintelligible (such as encryption), subsequent measures that eliminate the high risk, or disproportionate effort - in which case draft a public communication instead.

## Step 5 - Breach register (Article 33(5))

Record every breach in the internal register, including breaches that were not notified: facts, effects, and remedial action. The register is the accountability evidence the supervisory authority will ask for.

## Governance boundary

The workflow runs the decision tree, tracks the 72-hour deadline, and drafts the notification, the data subject communication, and the register entry. A human approves the risk assessment and sends the notification and communications. Sending is never automatic.
