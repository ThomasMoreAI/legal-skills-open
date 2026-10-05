# Open Knowledge Format v0.2 — pinned excerpts

The Open Knowledge Format (OKF) is an open format for recording knowledge — the context, provenance and curated judgement that surrounds a body of material — as a directory of ordinary markdown files with YAML frontmatter: no schema registry, no central authority, no required tooling, so a bundle can be read in any text editor, opened in Obsidian, and diffed in version control. What it standardises is the small set of conventions that make a continuously maintained corpus self-describing — where a document came from, how far it has been checked, whether it is still current — as optional frontmatter families rather than a fixed taxonomy.

Your wiki is an OKF bundle targeting `okf_version: "0.2"`, declared in the bundle-root `index.md` (§12). The excerpts below were **pinned on 2026-08-19** from the v0.2 specification and are reproduced here so that the conformance check shipped with this skill can be read, audited and reproduced without fetching anything. They are faithful summaries with section numbers, not a replacement: **where this page is silent, the full v0.2 specification governs.**

## Pinned excerpts

- **§4.1 — Frontmatter keys.** `type`, a short string naming the kind of concept, is the only always-required key; a concept carrying just `type` is fully conformant. Type values are not registered centrally, so consumers must tolerate unknown ones, typically by treating them as generic concepts. `title`, `description` (a single summarising sentence), `resource` (a URI for the underlying asset) and `tags` are recommended but optional. Extensions are explicit: producers **MAY** include any additional keys, and "Consumers SHOULD preserve unknown keys when round-tripping and MUST NOT reject documents with unrecognized fields."
- **§5.2 — `generated` and `verified`.** `generated` records how the current content was produced (`by`, an actor, is required within it; `at` is an ISO 8601 datetime marking the last meaningful change). `verified` records who or what has confirmed the content against its sources: a list of `{ by, at }` events, so that a person's sign-off and a scheduled process both survive; "how recently" is the latest `at`. The two are independent — content can change without re-confirmation, and facts can be re-confirmed without regeneration. A single verifier may be written as one `{ by, at }` mapping without the list dash, and consumers **MUST** treat that bare mapping as a one-element list. Actors (§7) are `<producer>/<version>` for tools, `human:<id>` for a person, `process:<id>` for an automated process.
- **§5.3 — Derived trust tiers.** Consumers derive the tier from `verified` and never store it: no `verified` key ⇒ **unverified**; `verified` by non-`human:` actors only ⇒ **machine-confirmed**; `verified` by a `human:<id>` actor ⇒ **human-reviewed**. A concept with no trust frontmatter is still consumable and must not be rejected (§11); tiers are advisory signals, not access control.
- **§5.4 — `status`.** `draft` (not yet reviewed, possibly incomplete), `stable` (ready for consumption), `deprecated` (kept for links and history, no longer current). Absent `status` means `stable`.
- **§5.5 — `stale_after`.** Optional, and an absolute date (`YYYY-MM-DD`) rather than a relative TTL: a concept is stale when `today >= stale_after` — on the date itself, not the day after — which keeps staleness a plain date comparison, independent of when the concept was read.
- **§6.1 — Links.** Concepts link to one another with standard markdown links, either bundle-root-absolute (beginning with `/`, the form the specification recommends) or relative. A link asserts an untyped relationship; its kind is carried by the surrounding prose, not by the link. Consumers **MUST** tolerate broken links: "a link whose target does not exist in the bundle is not malformed; it may simply represent not-yet-written knowledge."
- **§6.2 — Path-valued fields.** `resource`, `sources[].resource` and the computation fields each accept an absolute URL, a bundle-relative path beginning with `/`, or a relative path. A `sources[].resource` may instead be a scope descriptor naming a population the consumer cannot follow, in which case it is not a path.
- **§8 — `index.md`.** May appear in any directory, including the bundle root, and lists that directory's contents to support progressive disclosure. Index files carry **no frontmatter, with one exception**: a bundle-root `index.md` may carry `okf_version` (§12). The body is one or more heading-grouped sections whose entries take the form `* [Title](url) - description`, the description reused from the linked concept's frontmatter. `index.md` and `log.md` are reserved filenames at every level and must not be used for concept documents. Producers may generate an index automatically; consumers may synthesise one when none is present.
- **§9 — `log.md`.** May appear at any level to record the history of changes to that scope: a flat list of date-grouped entries, newest first, under `## YYYY-MM-DD` headings, which **MUST** use ISO 8601 form. Entry text is prose; the leading bold word (`**Update**`, `**Creation**`, `**Deprecation**`) is a convention, not a requirement.
- **§11 — Conformance.** A bundle conforms if (1) every non-reserved `.md` file in the tree contains a parseable YAML frontmatter block, (2) every frontmatter block contains a non-empty `type` field, and (3) every reserved filename (`index.md`, `log.md`) follows §8 and §9 respectively when present. Where the trust, lifecycle and provenance families are present, consumers **MUST** treat a bare `verified` mapping as a one-element list and **MUST NOT** reject a concept for missing any optional family. Everything else is soft guidance: consumers **MUST NOT** reject a bundle because of
  - missing optional frontmatter fields,
  - unknown `type` values,
  - unknown additional frontmatter keys,
  - broken cross-links, or
  - missing `index.md` files.
- **§12 — Declaring the version.** Versions are `<major>.<minor>`: a minor bump adds backward-compatible optional fields and conventions, a major bump may rename required fields or reserved filenames. A bundle may declare the version it targets with `okf_version: "0.2"` in the frontmatter of the bundle-root `index.md` — the only place frontmatter is permitted in an index file. A consumer that does not understand the declared version should attempt best-effort consumption rather than refuse the bundle.

## Where this profile is stricter than the standard

A bundle that breaks one of these five is still valid OKF; it is not a valid wiki, and the conformance check reports it.

- **Type enum.** OKF accepts any `type` value and asks consumers to tolerate unknown ones; this profile admits exactly four — `Legal Insight`, `Checklist`, `Trap`, `Position`.
- **Required-by-type extension keys.** Producer-defined keys are optional under §4.1; here `practice_area`, `jurisdiction`, `document_kind`, `trigger` and `origin` are required on every note, and `pending` may appear only alongside `status: draft`.
- **Document-relative body links.** §6.1 recommends the `/`-rooted form; note bodies use document-relative links (`../traps/silent-subprocessor-lists.md`) instead, because those resolve in editors, in Obsidian and in web views of the wiki, while `/`-rooted links do not. Frontmatter paths stay bundle-root-relative (§6.2).
- **No frontmatter on `log.md`.** §8's exception covers the bundle-root `index.md` only. The log is narration generated from the wiki's history, never a concept: it carries no frontmatter and no `type`.
- **No `.md` under the machine sidecar.** Everything under `wiki/.wiki/` is machine state — history, prior versions, pending suggestions, the vocabulary file — and no `.md` file may exist there, so §11's frontmatter rule can never be triggered by a sidecar file.

## Attribution

The Open Knowledge Format specification is a work of the **knowledge-catalog** project, made available under the **Apache License, Version 2.0**. The excerpts and summaries above are derived from it and are distributed under the same licence; the full licence text follows.

## Apache License, Version 2.0

```
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```
