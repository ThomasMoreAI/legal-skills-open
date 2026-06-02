---
name: packet-builder
title: packet-builder
description: Interactive complaint-packet assembly driven by packet-manifest.yaml — walks through authority, exhibit list, reference appendices, and runs scripts/packet/build.py. Triggers when the user says "build the packet" or when a complaint narrative and exhibit set are ready to compile.
author: EvanOchsner
author_url: https://github.com/EvanOchsner/personal-advocacy-toolkit/tree/main/.claude/skills/packet-builder
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# packet-builder

The builder is manifest-driven: everything authority-, case-, or
jurisdiction-specific lives in `packet-manifest.yaml`. This skill
shepherds that manifest to completeness and then runs the builder.

See `templates/packet-manifests/schema.yaml` for the authoritative
schema, and `examples/maryland-mustang/complaint_packet/packet-manifest.yaml`
for a filled-in synthetic reference.

## When this skill fires

- User says "build the packet" or "compile the complaint."
- Complaint draft exists under `drafts/` and exhibit evidence is
  in place under `evidence/`.
- After the `authorities-finder` run has identified the forum.

## Procedure

1. **Locate or scaffold the manifest.**
   - If `packet-manifest.yaml` exists in the packet directory, load
     it and list which sections are filled.
   - If not, copy `templates/packet-manifests/example-generic-dispute.yaml`
     into place and walk through the sections below.

2. **Fill the manifest header with the user.**
   - `packet.name` — a slug like `maryland-mustang-mia`.
   - `authority` — name, short code, mailing address, intake URL.
     Pulled from `authorities-finder` output; do not retype by
     hand if the skill already found it.
   - `complainant` — name, mailing address, email. For a public
     derivative, use the scrubbed synthetic values.
   - `respondent` — name, role, reference number (claim number,
     case number, policy number).

3. **Complaint narrative.** `complaint.source` points at the
   markdown or docx draft under `drafts/`. `complaint.title` shows
   up in the cover page. Write lawyer-mode per `tone-modes` skill;
   this is outbound.

4. **Exhibit list.** Each exhibit is `{label, title, description,
   source(s), date?}`. Labels are typically A, B, C, ... in the
   order they'll be referenced in the complaint. Sources are paths
   under `evidence/` or `drafts/`. Multiple sources per exhibit are
   fine — the builder concatenates in order.

5. **Reference appendices.** Optional. For policy / regulatory
   compilations that aren't exhibits per se but that the
   complainant wants attached for the reader's reference. Each has
   `{name, title, sources, note}`.

   Sources may live anywhere in the case folder; common locations:
   - `evidence/policy/...` for case-specific governing documents
     produced by the counterparty (e.g., the insurer's policy form
     that applies to the insured).
   - `references/raw/...` or `references/readable/...` for
     third-party authoritative text (statutes, regulations, ToS)
     ingested via the [trusted-sources](../trusted-sources/SKILL.md)
     skill. If a referenced statute / regulation / ToS isn't already
     under `references/`, hand off to `trusted-sources` *before*
     filling this section — drafting against the actual text catches
     paraphrase drift early.

6. **Dry-read the manifest aloud.** Before calling the builder,
   literally read back to the user: "Exhibit A is X, exhibit B is
   Y, exhibit C is Z." This catches reordered labels and missing
   sources faster than debugging the PDF.

7. **Build.**

   ```
   uv run python -m scripts.packet.build path/to/packet-manifest.yaml
   ```

   The builder writes a unified `packet.pdf` plus per-exhibit
   standalone PDFs (for filers who upload one at a time) into
   `packet.output_dir`.

8. **Open the PDF and read it.** The script is a scaffold, not an
   oracle (`tone-modes`). A silent build is not the same as a
   correct packet — check cover page names, exhibit order, and the
   first page of each exhibit.

## Definition of done

`packet-manifest.yaml` validates against the schema, the builder
ran without errors, the merged packet PDF and per-exhibit standalone
PDFs are in `packet.output_dir`, and the user has read the cover
page + first page of each exhibit and confirmed nothing is wrong.

If the user's next move is to publish or hand off the packet
externally (anything beyond the regulator's intake portal), do
**not** declare done — invoke `going-public` first.

If they're filing only with the regulator, hand back to
`pat-workflow`; the workflow ends here unless publication safety
applies.

## Synthetic example

Maryland-Mustang assembles into an 8-part packet against the
Maryland Insurance Administration: complaint narrative + 6
exhibits (A policy forms, B correspondence compilation, C
valuation report, D photographs, E specialist opinion, F
salvage-transfer record) + 1 reference appendix (compiled policy
reference). The full manifest is at
`examples/maryland-mustang/complaint_packet/packet-manifest.yaml`.

## Do not

- Do not hardcode anything in the build script. The builder has
  no case-specific branches; if you need something the schema
  doesn't cover, extend the schema, don't fork the script.
- Do not point a packet source at `evidence/*/raw/`. The raw layer
  is forensic; packets use the `readable/` layer for exhibits.
- Do not ship without the `going-public` check if the packet is
  being published anywhere beyond the regulator's intake.
