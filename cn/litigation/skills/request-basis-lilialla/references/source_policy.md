# Source Policy

Use these labels:

- `verified_law`: MCP/authoritative current law.
- `case_law_reference`: case-law, guiding case, typical case, judgment.
- `source_extracted`: local OCR/Markdown/JSON extraction.
- `scholarly_reference`: book, article, treatise, lecture note.
- `academic_paper`: paper or academic article proposition.
- `judicial_interpretation`: judicial interpretation candidate; verify version/effect before treating as law.
- `court_guidance`: court guidance, adjudication reference, or similar guidance material.
- `meeting_minutes`: Ninth Civil Minutes or other court/meeting minutes; verify nature, time effect, and scope.
- `user_curated_checklist`: user-maintained checklist or practical issue list.
- `conversion_artifact`: raw conversion output, MinerU JSON, OCR probe, or parser artifact.
- `case_training_sample`: teaching case or sample answer.
- `case_file_claim`: party/client/opponent assertion.
- `evidence_supported`: fact preliminarily supported by evidence.
- `model_inference`: model reasoning.
- `unknown_source`: temporary placeholder when source identity is not yet known; explain in notes.

Use `source_status` for source identity and `verification_status: unverified` for not-yet-checked claims.

Use `ocr_risk: true` when a claim depends on a noisy conversion or table/OCR reconstruction. Statutes, judicial interpretations, court guidance, and meeting minutes may be described as authority candidates, but only become `verified_law` after MCP or authoritative-source verification. Case-law claims must keep search scope, sample limits, comparability, and contrary cases when material.

Verification status:

- `unverified`
- `pending_mcp`
- `mcp_verified`
- `conflict_detected`
- `deprecated`
- `needs_human_review`

Hard bans:

- No verified current-law claim without MCP/authority.
- No court-practice generalization without case-law research.
- No party assertion as found fact.
- No local scholarly source as controlling legal authority.
