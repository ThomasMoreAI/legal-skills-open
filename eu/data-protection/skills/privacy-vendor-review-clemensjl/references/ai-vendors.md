# LLM and AI vendors — snapshot

**Snapshot date: 2026-08-05.** Every line was read from the vendor's own legal or documentation page on that date. AI vendor terms change faster than any other category in this skill — several entries below changed within the last three months. **Re-verify before relying on any line, and re-date it.**

Three questions decide an AI integration and none of them is answered by the model's quality: does the vendor train on your inputs by default, how long does it keep them, and where is inference actually executed.

## Consumer tier vs API — the split that causes the incidents

Every major provider trains on consumer-tier inputs by default and does not train on API/business-tier inputs. Routing client or employee data through a personal consumer account is the most common real-world breach in this category, and it is invisible in the vendor's audit trail on your side.

| Product | Training on inputs, default | Source |
|---|---|---|
| ChatGPT Free / Plus / Pro, Codex | **Yes**, opt-out in Settings → Data Controls | `help.openai.com/en/articles/5722486-how-your-data-is-used-to-improve-model-performance` |
| ChatGPT Business / Enterprise / Edu, OpenAI API | No | ibid.; `developers.openai.com/api/docs/guides/your-data` |
| Claude Free / Pro / Max | **Yes** since the 2025 consumer-terms change; users had to choose by 08.10.2025; opting in extends retention to 5 years, declining keeps 30 days | `anthropic.com/news/updates-to-our-consumer-terms` |
| Claude API, Claude for Work (Team/Enterprise), Claude Gov, and Claude via Bedrock/Vertex | No | `privacy.claude.com/en/articles/7996868-…` (last updated 16.03.2026) |
| Google AI Studio / Gemini API, unpaid tier | **Yes** — and human reviewers may read inputs and outputs. **Except in the EEA, Switzerland and the UK**, where the paid-tier no-training regime applies to all services including the free tier | `ai.google.dev/gemini-api/terms` (23.03.2026) |
| Gemini API paid tier, Vertex AI | No | ibid.; Google Cloud Service Specific Terms § 18 |
| Gemini consumer app | **Yes**; a subset of chats is human-reviewed and **human-reviewed chats are retained up to three years even after deletion** | `support.google.com/gemini/answer/13594961` (15.07.2026) |
| Le Chat / Mistral consumer & free | **Yes**, opt-out in account | `legal.mistral.ai/terms/privacy-policy` |
| Mistral commercial | No, except free-subscription users, feedback, moderation-flagged content and Labs Models | `legal.mistral.ai/terms/commercial-terms-of-service` |
| Azure OpenAI / Models sold by Azure | No, and the model provider never sees the data | `learn.microsoft.com/en-us/azure/ai-foundry/responsible-ai/openai/data-privacy` |
| AWS Bedrock | No | `aws.amazon.com/bedrock/faqs/` |

Two traps that survive every "no training" commitment:

- **Thumbs-up/down feedback re-opens training.** OpenAI: submitting feedback may trigger training on that entire conversation even where you opted out. Anthropic: feedback is retained 5 years, de-linked; admins can disable feedback org-wide. If your product surfaces a rating widget, it is a data-protection control, not a UX detail.
- **Safety flagging survives opt-out.** Anthropic's policy states inputs and outputs are used for training where conversations are flagged for safety review or reported.

## Retention and zero-data-retention

| Vendor | Default retention (API) | ZDR available | How obtained | What ZDR does not cover |
|---|---|---|---|---|
| OpenAI | Abuse-monitoring logs up to 30 days | Yes, "Zero Data Retention" | Sales approval, not self-serve; forces `store: false` | **Ineligible endpoints**: `/v1/conversations`, `/v1/chatkit/threads`, `/v1/assistants`, `/v1/threads`, `/v1/vector_stores`, `/v1/files`, `/v1/fine_tuning/jobs`, `/v1/evals`, `/v1/batches`, `/v1/videos` |
| Anthropic | 30 days; flagged content up to 2 years; classification scores up to 7 years; feedback 5 years | Yes, per-organisation | Sales; verify at Settings → Privacy Controls → Data retention period | Safety-classifier results. **And "Covered Models": prompts and outputs for covered models are retained 30 days regardless of a ZDR agreement**, including via Bedrock, Vertex and Microsoft Foundry — `privacy.claude.com/en/articles/15425996-data-retention-practices-for-covered-models` |
| Google Vertex | Not stored beyond what is needed to produce the output (Service Specific Terms § 20(h)); Grounding-with-Search query logs up to 3 days | `[[UNVERIFIED: a "Zero data retention" entry exists in the Vertex data-governance navigation but the page body is client-rendered and could not be read — confirm scope and enablement]]` | — | — |
| Azure OpenAI | Abuse-monitoring store, flagged samples only, in the customer's Azure geography | Yes, "**modified abuse monitoring**" | Microsoft form under Limited Access eligibility | Automated real-time review continues. Verifiable in the resource JSON: `{"name":"ContentLogging","value":"false"}` appears only when logging is off |
| AWS Bedrock | **None by default** — zero data retention and zero operator access are the documented defaults | Default | n/a | Per-model exceptions, see below |
| Mistral | 30 rolling days for abuse monitoring | Yes, "zero retention" | `[[UNVERIFIED: enablement path — self-serve or sales — not stated on the reachable pages]]` | Labs Models permit training |

**AWS Bedrock's exceptions are the gotcha of that platform.** Certain frontier models break the ZDR default: classifier-flagged traffic on some OpenAI models is retained up to 30 days for offline abuse detection, and at least one Anthropic model requires the customer to **opt in to sharing retained traffic with the model provider for abuse detection and potential human review** in order to use the model at all. With cross-region inference enabled, retained inputs and outputs are stored in the **destination** region — not the region you called (`docs.aws.amazon.com/bedrock/latest/userguide/abuse-detection.html`). Verify the model list on that page at review time; it changes with each model launch.

## Region pinning — what actually holds

| Option | EU inference | EU storage | Note |
|---|---|---|---|
| Vertex AI, EU multi-region endpoint `aiplatform.eu.rep.googleapis.com` | Yes | Yes | Strongest documented ML-processing boundary. The **global endpoint is the SDK default in most quickstarts** and gives no residency at all — Google's own docs say so |
| Azure OpenAI, **Regional** deployment | Yes | Yes | **Global** and **DataZone** deployment types forfeit processing locality; batch runs as a Global deployment. EEA deployments have EEA-located abuse reviewers |
| OpenAI API, Europe (EEA+CH) residency, host `eu.api.openai.com` | Yes | At rest | Set **at project creation**, not changeable later. Covers Customer Content only; account, metadata and usage data are processed globally. Non-US regions require a Modified Retention amendment alongside ZDR |
| AWS Bedrock, EU region, cross-region inference disabled | Yes | ZDR default | Enabling cross-region inference moves both processing and any retained data |
| Mistral | Partly | Mixed | French entity and French law, but infrastructure sub-processors are Microsoft (SE, NO), Google (NL, BE, US) and Mistral Compute (FR) |
| **Anthropic direct** | **No EU-only option** | **US** | "data is stored in the US"; only US-only inference exists as an Enterprise control. For EU residency with Claude, the route is Bedrock or Vertex, not the Anthropic API — `privacy.claude.com/en/articles/7996890-…` (15.06.2026) |

## Contracting entity, role and DPA mechanics

| Vendor | EEA contracting entity | Role for API | DPA |
|---|---|---|---|
| OpenAI | **OpenAI Ireland Ltd** (Business Terms effective 01.01.2026) | Processor | Auto-incorporated: Business Terms § 5.3 incorporates the DPA by reference. `openai.com/policies/data-processing-addendum/`, effective 01.01.2026. The Enterprise Privacy page still points to a DPA form — that is a convenience, the incorporation clause controls |
| Anthropic | **Anthropic Ireland, Limited** for EEA, Switzerland and UK | Processor (controller for Free/Pro/Max) | Auto-incorporated into the Commercial Terms. SCC Modules 2 and 3 by reference, Irish governing law, UK and Swiss addenda. Return or delete within 30 days on termination |
| Google Cloud / Vertex | `[[UNVERIFIED: the CDPA text retrieved did not name Google Cloud EMEA Limited — check the signature block of your Cloud Master Agreement]]` | Processor (CDPA § 4.1) | Incorporated into the underlying Cloud agreement |
| Microsoft Azure | Microsoft Products and Services DPA at `aka.ms/DPA` | Processor | Auto-applying |
| AWS | `[[UNVERIFIED from the GDPR Center page; the AWS Customer Agreement contracting-party table names Amazon Web Services EMEA SARL for EMEA customers]]` | Processor | Auto-incorporated: Service Terms § 1.14.1 |
| Mistral | Mistral AI, Paris, RCS 952 418 325; French law, Paris courts | Processor for business use | Incorporated by reference; `[[UNVERIFIED: the DPA URL referenced by Mistral's own Commercial ToS returned 404 at the snapshot date]]` |

## Sub-processor exposure worth knowing

- **OpenAI**: Microsoft (23 regions), **AWS (US)**, Google Cloud, Oracle Cloud, **CoreWeave**, Cloudflare. Human-touch vendors: **TaskUs (Philippines)**, **Accenture (US, Canada, Philippines)**, Cinder Technologies — support, content moderation and moderation tooling. `openai.com/policies/sub-processor-list/`
- **Anthropic**: **Google Cloud, AWS and Microsoft Azure, all listed "worldwide"**; Cloudflare; Stripe; WorkOS; support vendors **Nutun (South Africa)** and **Boldr (Canada)**; Intercom. `trust.anthropic.com/subprocessors`
- **Google Cloud**: Google affiliates in 50+ countries plus Accenture, Cognizant, Deloitte, IBM, Infosys, Tata for support, data labelling and voice transcription. `cloud.google.com/terms/subprocessors` (16.07.2026)
- **Mistral**: Microsoft, Google, Mistral Compute for infrastructure; **Brave (US) for web search, Black Forest Labs (US) for image generation, Merge API (US) for connectors** — enabling those features exports content to the US. `trust.mistral.ai/subprocessors` (05.08.2026)

Human review happens at every provider: safety-flagged content, user-reported content, incident response, and the outsourced moderation vendors above. Record it in the notice; it is not an edge case.

## AI Act interaction — Regulation (EU) 2024/1689 as amended

**The regulation was amended before its general application date.** Regulation (EU) 2026/1744, the "Digital Omnibus on AI", was published in the OJ on **27.07.2026** and entered into force the third day after publication (`eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202601744`). The Commission records the track as: proposal adopted 19.11.2025, political agreement 07.05.2026, in force 27.07.2026 (`digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai`, page updated 03.08.2026).

| Date | Status at 2026-08-05 | Content |
|---|---|---|
| 02.02.2025 | In force | Art 5 prohibited practices; Art 4 AI literacy |
| 02.08.2025 | In force | Chapter V GPAI model obligations, governance, penalties |
| **02.08.2026** | **In force — held to schedule** | General application, including **Art 50 transparency**; AI Office and national authorities take up enforcement |
| Dec 2026 | Ahead | New Art 5 prohibition on AI generating non-consensual intimate imagery and CSAM (new Art 5(1)(ba), (bb)) |
| 02.12.2027 | Ahead — **delayed from 02.08.2026** | Chapter III high-risk regime for Annex III / Art 6(2) systems |
| 02.08.2028 | Ahead — **delayed from 02.08.2027** | Chapter III high-risk regime for Annex I / Art 6(1) product-embedded systems |

**Do not cite `artificialintelligenceact.eu` article pages for dates at present:** its Art 113 and Art 5 texts were still the pre-Omnibus versions at the snapshot date. Use the EUR-Lex consolidated text `CELEX:02024R1689-20260727`.

**Art 50 obligations that bind now:**

- **50(1)** — a system intended to interact directly with natural persons must inform them they are interacting with an AI, unless that is obvious to a reasonably well-informed person.
- **50(2)** — providers of systems generating synthetic audio, image, video or text must mark outputs in a machine-readable format, detectable as artificially generated or manipulated.
- **50(3)** — deployers of emotion-recognition or biometric-categorisation systems must inform the exposed persons.
- **50(4)** — deployers must disclose deepfakes; AI-generated text published to inform the public on matters of public interest must be disclosed **unless** it underwent human review with a natural or legal person holding editorial responsibility.
- **50(5)** — the information must be given clearly and distinguishably **at the latest at the time of the first interaction or exposure**, and must meet accessibility requirements.
- **50(7)** as amended by the Omnibus removed the Commission's obligation to adopt implementing acts on detection and marking, replacing it with facilitation of codes of practice. The marking obligation binds; the technical "how" is not yet standardised.

**GPAI Code of Practice**: published 10.07.2025, confirmed by the Commission and the AI Board as an adequate voluntary tool. Voluntary. Three chapters — Transparency and Copyright for all GPAI providers, Safety and Security only for systemic-risk models. 21 signatories including Amazon, Anthropic, Google, Microsoft, OpenAI, Mistral and Cohere; xAI signed only the Safety and Security chapter. GPAI obligations have bound since 02.08.2025; models placed on the market before that date have until 02.08.2027 (`digital-strategy.ec.europa.eu/en/policies/contents-code-gpai`).

The AI Act sits **beside** the GDPR, not instead of it. An Art 50 chatbot disclosure is not an Art 13 privacy notice and does not replace one.

## Additional review questions for an AI integration

1. Which tier is actually in use — verify against the API key or the account, not against what was procured.
2. Can end users paste anything into the prompt? If yes, Art 9 data is possible and the DPIA test in `dpia.md` almost certainly triggers.
3. Is the output used to make or shape a decision about a person? Then Art 22 and the high-risk classification both need checking.
4. Is retrieval-augmented generation in play? The vector store is a separate data store with its own retention, and at OpenAI it is ZDR-ineligible.
5. Are logs of prompts and completions kept on **your** side? That store is yours to document in the ROPA and to retain-limit.
6. Does the feature disclose the AI interaction at first exposure (Art 50(1)) and mark synthetic output (Art 50(2))?

## Checkpoints

- [ ] Tier confirmed on the account, not assumed from the contract
- [ ] Training default confirmed for that exact tier, on the vendor's own page, with the page date
- [ ] Feedback widgets assessed as a training re-entry path
- [ ] Retention and ZDR status recorded, with the endpoints or models ZDR does **not** cover named
- [ ] Region pinning verified in the actual client configuration — endpoint host, deployment type, inference profile — not in the dashboard's headline
- [ ] Cross-region inference and global/DataZone deployment types explicitly checked and disabled if residency is claimed
- [ ] Sub-processor list retrieved and the human-review vendors noted in the notice
- [ ] Contracting entity confirmed as the EEA entity where one exists
- [ ] DPA incorporation mechanism recorded
- [ ] Art 50(1) disclosure present at first interaction; Art 50(2) marking present for synthetic output
- [ ] No consumer-tier account in the data path
- [ ] Snapshot re-verified and re-dated before approval
