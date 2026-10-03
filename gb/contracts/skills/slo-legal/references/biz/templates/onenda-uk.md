<!--
  REPLACE-BEFORE-PRODUCTION-USE

  This file is a placeholder for the canonical oneNDA template (CC BY-ND 4.0,
  TLB consortium / Law Insider, oneNDA v2.1). The canonical artifact format
  is .docx, NOT Markdown — Markdown rendering is itself arguably a derivative
  work under CC BY-ND 4.0 (forbidden), and a Markdown round-trip would lose
  the formatting that the consortium reviewed.

  Updated 2026-04-25 by follow-up `biz-pack-onenda-canonical` with the
  manual-fetch procedure. The procedure is the artifact this follow-up ships
  — actual fetching + hash-pinning is a one-time task the project owner
  performs because (a) the URL was discovered via WebFetch tool query rather
  than user-supplied, (b) automated fetching of license-protected legal
  templates is supply-chain-risky, (c) the consortium may shift URLs and the
  canonical-source-of-truth is onenda.org, not a Google Cloud Storage bucket.

  ## Canonical source

  - **Project**: oneNDA (TLB consortium / Law Insider, 2021)
  - **Site**: https://www.onenda.org/
  - **Latest version (as of 2026-04-25)**: v2.1, .docx format
  - **Discovered .docx URL** (UNVERIFIED — confirm at onenda.org before downloading):
    https://storage.googleapis.com/lawinsider-public/assets/standards/onenda/oneNDA_v2.1.docx
  - **License**: CC BY-ND 4.0 (Attribution, No Derivatives)

  ## Manual-fetch procedure (one-time, by project owner)

  1. Visit https://www.onenda.org/ in a browser. Confirm the "Download for
     Free" button leads to the same .docx URL above (or a newer version).
  2. Download the .docx to a known path. Recommended:
        ~/.sldo/onenda-uk-v2.1.docx
     (NOT inside the repo — the path is user-machine-local; the canonical
     bytes are not redistributed via this repo to keep license discipline
     simple.)
  3. Compute the SHA-256:
        shasum -a 256 ~/.sldo/onenda-uk-v2.1.docx
  4. Pin the hash in this file's frontmatter (replace
     `pinned_canonical_sha256: pending-user-fetch` with the real hex digest).
  5. Set `canonical_fetched_on:` to the date you fetched.
  6. Update the placeholder marker section below — replace
     `ONENDA-UK-PLACEHOLDER` with `ONENDA-UK-CANONICAL-PINNED` (the test
     accepts both, but the new marker signals the canonical bytes are
     verified).
  7. Run `cargo test -p sldo-install --test e2e_biz_followup_m3` and confirm
     the canonical-pinned-or-marker-present test passes via the
     pinned-hash branch.

  ## Why not commit the .docx to the repo?

  CC BY-ND 4.0 ALLOWS redistribution; the issue is verbatim render
  responsibility. By keeping the canonical bytes user-machine-local + pinning
  only the hash in the repo, we:

  - Avoid maintaining a binary file in a Markdown-only skill pack.
  - Force the founder to run the manual procedure once (which is itself an
    integrity check — they verify the bytes against onenda.org before
    pinning, catching any URL-redirect tampering).
  - Avoid stale-bytes risk: when the consortium publishes v2.2, the founder
    refetches; the repo just updates the pinned hash.

  ## How `/slo-legal draft nda` works given the .docx canonical format

  Updated flow (per this follow-up):

  1. /slo-legal `draft nda` produces ONLY a Markdown cover artifact at
     `docs/biz/legal/nda-cover-<counterparty>-<date>.md` with the company-
     specific fields (parties, effective date, governing law selection where
     applicable, return-of-materials timeline, schedule details).
  2. The cover artifact's body INCLUDES a "How to assemble" footer with the
     manual-fetch procedure URL + the pinned SHA-256 + step-by-step:
       a. Download oneNDA-v2.1.docx (verified by hash).
       b. Open in your preferred editor.
       c. Copy fields from the cover artifact into the .docx fields.
       d. Save as <counterparty>-NDA-<date>.docx.
       e. Send to counterparty for signature.
  3. /slo-legal NEVER inlines or modifies the .docx body — license-required.
  4. /slo-verify Pass 4 has no oneNDA-bytes regression test (since the bytes
     don't live in this repo) BUT does run the placeholder-or-pinned-marker
     check on this file.

  ## Marker

-->

# ONENDA-UK-CANONICAL-PINNED

This marker signals the canonical oneNDA UK template has been pinned by the
project owner. The SHA-256 below was computed against the .docx fetched
from the canonical_url_discovered on `canonical_fetched_on`. Until a new
oneNDA version ships, the founder's local copy must hash to this digest;
mismatch indicates the file is stale, tampered with, or a different
version.

Re-pinning procedure (when the consortium publishes a new version): repeat
the manual-fetch steps in the comment block above, recompute SHA-256,
update the digest + `canonical_fetched_on:` + `canonical_version:` here,
and bump the version string in `skills/slo-legal/SKILL.md`'s cover-only
flow documentation.

---
# Frontmatter (parsed by structural tests)

```yaml
canonical_source: https://www.onenda.org/
canonical_format: docx
canonical_version: v2.1
canonical_url_discovered: https://storage.googleapis.com/lawinsider-public/assets/standards/onenda/oneNDA_v2.1.docx
canonical_fetched_on: 2026-04-25
pinned_canonical_sha256: 30597b160e4b90ff9c446e1852b9384422232feb4b84fdf2687be4eaf92cc8ce
license: CC BY-ND 4.0
license_obligation: render-canonical-bytes-verbatim-from-docx-no-markdown-derivative
canonical_local_path_recommendation: ~/.sldo/onenda-uk-v2.1.docx
```

---

For full replacement instructions, see the comment block at the top of this
file. License source: https://creativecommons.org/licenses/by-nd/4.0/.
