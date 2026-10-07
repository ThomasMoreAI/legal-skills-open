# Case Summary — Example Corpus Manifest

All files in this directory are **synthetic**. Party names, dates, provider
names, Bates numbers, and monetary amounts are fabricated for calibration
purposes. Nothing here is a real case, a real person, or a real medical record.

Two kinds of artifacts are included:

1. **Finished example memos** — showing what a case-summary memo looks like
   with each practice-area playbook applied.
2. **Mini-corpus** — a small set of documents an agent can run the full
   case-summary loop against, to verify that diagnose → map → reduce produces
   output structurally similar to the finished examples.

If you need a real corpus, substitute a redacted matter from your own files.
Do not use real client data to exercise this skill without privilege review.

---

## Finished example memos

| File | Practice area | Playbook loaded | Core skeleton sections exercised | Sibling skills routed (simulated) |
|---|---|---|---|---|
| `memo-pi-tort.md` | Personal injury (premises) | `PLAYBOOK-PI-TORT` | I–X | `deposition-summary` (manager depo); `lien-resolution-summary` (Medicaid) |
| `memo-commercial-contract.md` | Commercial litigation (MSA breach) | `PLAYBOOK-COMMERCIAL-LITIGATION` | I–X | `discovery-summary` (RFP responses) |

Both memos are written *from* the synthetic corpus for PI, and *for* a
hypothetical commercial matter (no corpus shipped for commercial — the memo
itself illustrates the output shape). The intent is: if an agent runs against
`corpus-pi-tort/`, its output should structurally match `memo-pi-tort.md`
(not necessarily in exact wording).

---

## Mini-corpus — `corpus-pi-tort/`

A small premises-liability corpus (slip-and-fall at a grocer). Seven files,
markdown for grep-ability — real corpora would be PDFs. The types and the
signals are representative of what the PI playbook expects.

| # | File | Type | Role in the matter |
|---|---|---|---|
| 1 | `complaint-Rivera-v-Grocer.md` | Pleading | Plaintiff's complaint; claims + prayer |
| 2 | `answer-Grocer.md` | Pleading | Defendant's answer with affirmative defenses |
| 3 | `incident-report-store-0147.md` | Business record | Store's internal incident report |
| 4 | `ems-run-sheet-Rivera.md` | Medical | EMS narrative from scene |
| 5 | `er-record-Rivera-2024-02-15.md` | Medical | ER triage, imaging, discharge |
| 6 | `billing-ledger-Rivera.md` | Damages | Consolidated provider billing ledger |
| 7 | `deposition-excerpt-manager.md` | Testimony | Excerpt: store manager's deposition |

File content is realistic in structure and terminology but fabricated in
specifics. A PDF-based real corpus would also include imaging studies, PT
notes, tax/W-2 records for wage loss, and formal lien correspondence; the
mini-corpus covers the minimum needed to exercise all eight core dimensions
plus the PI playbook's Medical Summary / Damages Itemization / Liens sections.

---

## How to use

**To calibrate an agent:**

1. Point the agent at `corpus-pi-tort/` with this skill loaded.
2. Run through the loop in `SKILL.md`.
3. Compare the generated memo against `memo-pi-tort.md` — section-by-section
   structure should match. Wording will differ; citations should point to
   the same source files for the same claims.
4. Deviations in section coverage (missing sections, misrouted clusters,
   unpopulated playbook inserts) indicate the skill needs adjustment.

**To validate a new playbook:**

1. Write `references/PLAYBOOK-<new-practice-area>.md` per the
   `PLAYBOOK-AUTHORING.md` contract.
2. Assemble a mini-corpus for that practice area (optional but recommended).
3. Run an agent against the corpus. Confirm the new playbook loads, its
   queries fire, and its output sections populate without requiring any
   edits to core reference files.

---

## What is **not** included and why

- **Real client data.** Privilege, PHI, and attorney work-product make real
  data inappropriate for a published example corpus.
- **PDF-format originals.** Markdown is grep-able, version-controllable, and
  easier for an agent to cite by line number during calibration. Production
  skill runs are against PDFs; the skill handles PDFs via the backends
  described in `references/BACKENDS.md`.
- **A commercial mini-corpus.** Deferred to a follow-up pass. Contributing
  one means seeding 5–8 synthetic contract/correspondence documents; the
  finished `memo-commercial-contract.md` illustrates the output shape in the
  meantime.
- **An IP mini-corpus.** Also deferred. `PLAYBOOK-IP-INFRINGEMENT.md` is the
  canonical reference for the output shape until a mini-corpus ships.
