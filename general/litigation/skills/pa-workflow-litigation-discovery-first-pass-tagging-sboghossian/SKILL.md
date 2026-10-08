---
name: pa-workflow-litigation-discovery-first-pass-tagging-sboghossian
title: Discovery First-Pass Tagging
description: Use when a litigation team faces a large document set in discovery or disclosure and needs to triage documents efficiently before senior attorney review. Performs automated privilege detection, responsiveness scoring, date filtering, witness-mention extraction, and anomaly flagging — reducing senior review time by 60–80%. Applicable in US discovery, UK/DIFC/ADGM disclosure, and international arbitration document production.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/pa-workflow/pa-workflow-litigation-discovery-first-pass-tagging
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Discovery First-Pass Tagging

## Purpose

Document review is the single largest cost center in complex litigation. This workflow runs a structured first-pass triage on a document corpus, applying five analytical lenses in sequence, and outputs a tagged, scored dataset that human reviewers can work through in priority order — dramatically reducing the time senior attorneys spend on irrelevant or clearly privileged material.

Claim: reduces senior attorney review time by 60–80% on standard commercial litigation discovery sets.

## Inputs

| Input | Required | Notes |
|---|---|---|
| Document corpus | Yes | PDF, email exports (PST/MSG/EML), Word, Excel, image files via OCR |
| Matter description and key issues | Yes | Defines "responsiveness" parameters |
| Key custodians (persons of interest) | Yes | Drives witness mention extraction |
| Date range of interest | Recommended | Narrows irrelevant historical documents |
| Privilege holders (attorneys, in-house counsel) | Yes | Required for privilege detection |
| Opposing party's document requests (if US discovery) | Recommended | Defines responsiveness categories precisely |
| Language(s) of corpus | Optional | Defaults to English; flag for Arabic, French if MENA documents are included |

## Tagging Methodology

### Pass 1 — Privilege detection

Purpose: flag attorney-client privilege and work-product doctrine candidates before any human review.

Detection signals:
- Document is to/from a licensed attorney (in-house or external)
- Subject line or body contains legal opinion, legal advice, litigation strategy references
- Marked "Privileged," "Confidential — Legal," "Attorney-Client Communication"
- Work-product indicators: prepared in anticipation of litigation; mental impressions of counsel

**Auto-redact candidates**: documents where privileged content is embedded in otherwise responsive materials (e.g., an email chain where one attorney response is privileged but the attached contract is responsive).

MENA considerations:
- In-house legal teams in UAE and KSA do not always hold attorney-client privilege under local procedural rules as consistently as common-law jurisdictions. For DIFC/ADGM proceedings, English common-law privilege applies. For UAE onshore / KSA courts, in-house communications may receive less automatic protection — flag for counsel determination.
- Communications in Arabic between legal advisors and clients: same privilege analysis applies; ensure Arabic-language privilege indicators ("سري — اتصال قانوني") are included in detection patterns.

Tag: `PRIVILEGE_CANDIDATE`, `WORK_PRODUCT_CANDIDATE`, `NEEDS_PRIVILEGE_REVIEW`

### Pass 2 — Responsiveness scoring

Score each document 0–100 for relevance to the defined issues:

| Score | Label | Meaning |
|---|---|---|
| 80–100 | HOT | Directly addresses a key issue; must be reviewed first |
| 50–79 | RESPONSIVE | Related to an issue; review in standard queue |
| 20–49 | POTENTIALLY RESPONSIVE | Background or contextual; review if time allows |
| 0–19 | NOT RESPONSIVE | No apparent connection; flag for senior approval before withholding |

Scoring factors:
- Key terms from document requests appear in the document
- Named custodians are authors, recipients, or mentioned
- Document falls within the date range of interest
- Document type is directly relevant (contract, invoice, board resolution, regulatory filing)

### Pass 3 — Date filtering

- Flag documents outside the defined date range for potential exclusion
- Identify documents with suspicious date metadata (creation date after the dispute arose, timestamps that contradict email chain sequence)
- Cluster documents by time period to surface activity spikes (often significant in fraud and corporate disputes)

### Pass 4 — Witness mention extraction

For each custodian in the key persons list:
- Extract every document where the person is named, emailed to/from, or referenced
- Build a per-custodian document index
- Flag documents where the custodian's role appears inconsistent with their stated account

Output: per-witness document package, usable directly by [[pa-workflow-litigation-deposition-binder-builder]].

### Pass 5 — Anomaly flagging

Flag documents that warrant immediate escalation to senior counsel:
- Communications that appear to advise on concealing or destroying evidence
- Documents post-dating the dispute with metadata showing backdating
- References to accounts, entities, or transactions not disclosed in pleadings
- Large attachments that do not match their subject line (potential hidden documentation)
- "Destroy" / "delete" / "do not put in writing" language — evidence-spoliation risk
- Unusual encryption or document protection

## Output

```json
{
  "corpus_summary": {
    "total_documents": 14200,
    "reviewed_by_ai": 14200,
    "privilege_candidates": 340,
    "hot_responsive": 890,
    "responsive": 3100,
    "not_responsive": 9870,
    "anomalies_flagged": 23,
    "languages_detected": ["English", "Arabic", "French"]
  },
  "priority_queue": [
    {
      "doc_id": "DOC-00445",
      "date": "2023-11-12",
      "author": "John Smith",
      "recipients": ["CEO", "CFO"],
      "responsiveness_score": 95,
      "tags": ["HOT", "KEY_CUSTODIAN", "ANOMALY"],
      "anomaly_note": "Subject line says 'Board Update' but body discusses payment diversion — review immediately"
    }
  ],
  "privilege_log_export": "ready for [[pa-workflow-litigation-privilege-log-drafting]]"
}
```

## Output for Human Review

Deliverables to the review team:
1. **Hot stack** (review first): 890 HOT documents in priority order
2. **Privilege log export**: feeds directly into [[pa-workflow-litigation-privilege-log-drafting]]
3. **Anomaly memo**: 23 flagged documents with explanation
4. **Per-custodian packages**: indexed document sets for each key witness
5. **Not-responsive list**: subject to attorney sign-off before withholding

## Jurisdictional Notes

- **US (FRCP)**: Responsive to opposing party's Rule 34 requests. Privilege log required under Rule 26(b)(5). Spoliation sanctions are severe — flag any evidence of deletion immediately.
- **UK / DIFC / ADGM**: Disclosure obligations under CPR Part 31 (UK) or DIFC/ADGM procedural rules. Standard disclosure = documents relied on + adverse documents. Legal professional privilege applies (common-law standard).
- **International Arbitration (IBA Rules)**: Document production is narrower than US discovery; only specifically identified documents or categories. Proportionality is the governing standard. Tagging for relevance and materiality is sufficient; exhaustive production is not expected.
- **UAE onshore / KSA**: Document production is not automatic; courts request specific documents through the proceedings. First-pass tagging is most useful for internal organization and preparing documents for court submission, not open-ended production.

## Limits

- AI-based privilege detection is a triage tool; final privilege determinations must be made by a licensed attorney.
- OCR quality on older or poor-quality scans may reduce detection accuracy — flag low-confidence OCR documents for manual review.
- Multilingual documents (Arabic-English) may require dedicated Arabic-NLP processing for accurate scoring.

## Related Skills

- [[pa-workflow-litigation-privilege-log-drafting]]
- [[pa-workflow-litigation-witness-contradiction-finder]]
- [[pa-workflow-litigation-deposition-binder-builder]]
- [[pa-workflow-litigation-transcript-search-q-and-a-indexing]]
