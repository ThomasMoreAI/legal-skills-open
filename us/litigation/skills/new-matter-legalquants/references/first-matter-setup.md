# First-matter workspace setup

Read this reference only when the bounded architecture check returned `not-found` and the user accepts a setup walkthrough, or when the user asks to create or change workspace defaults. Ordinary intake should reuse an established architecture without loading this guide. An `ambiguous` or `unavailable` result requires clarification or access, not a new layout.

## Start by looking, not redesigning

Check only the current workspace, a host-selected matter root whose scope is visible, and locations the user identifies. Look for a matter index or register, existing matter folders, a stable-ID marker or convention, a canonical matter-record template, approved taxonomy or reporting fields, a workspace README or source manifest, and a source-versus-work-product folder convention. Treat what is found as evidence of a possible convention, not permission to mutate it. An empty but clearly marked matter root can be a valid architecture; a populated but unmarked directory is ambiguous. If patterns conflict, multiple candidates exist, or ownership is unclear, show the candidates and ask which is authoritative.

Do not search unrelated client folders, infer firm policy from one matter, or turn a legacy filename into a confirmed rule. A matter-management or document-management system is an optional user-authorized source; inability to access it is `architecture_check: unavailable`, not evidence that no architecture exists. Do not read `lqprofile.md` or `lqplaybook.md` to discover paths or workspace defaults.

## Offer the minimum useful defaults

If there is no architecture, offer a small reusable setup rather than a full knowledge-management project:

1. **Matter root and destination.** The approved local or external location, with its confidentiality and access boundary.
2. **Stable identity.** A collision-safe `matter_id` pattern that does not change when the caption or title changes.
3. **Canonical intake record.** `matter-record.md` using [matter-record-template.md](matter-record-template.md), with field-level provenance and version state.
4. **Matter index.** One compact row per matter: stable ID, title, client or represented entity, posture, lead, status, opened/updated dates, confidentiality, workspace locator, and any visible urgent or preservation flag. Do not put privileged analysis in a portfolio index.
5. **Workspace seam.** Keep the intake record and original-source boundary stable; let `organize-case-docs` create or adapt the detailed source, chronology, proof, discovery, transcript, work-product, and closeout structure after intake.
6. **Matter-local fields.** Add only fields required by the engagement or user, such as insurer, billing, reporting cadence, jurisdiction identifiers, taxonomy, escalation contact, or approved template names.

Defaults govern organization, not legal judgment. They cannot preselect conflicts clearance, engagement, side, authority, deadlines, preservation trigger, privilege, retention, or matter status.

## Preview before creating anything

Show:

- The proposed root and files.
- The ID convention with two fictional examples and its collision handling.
- Index columns and confidentiality boundary.
- Which fields are global workspace defaults and which remain matter-local.
- What existing files, if any, would be left unchanged.
- What `new-matter` will write now and what `organize-case-docs` may offer later.

Ask for explicit approval of the displayed structure and destination. If the user approves only the current matter, create only the current matter record; do not silently create a shared index or template. Never overwrite an existing index, template, or matter folder without an explicit update instruction and a versioned diff.

## Progressive use after setup

On later matters, read the approved index and template from the user-designated workspace, apply their structure, and ask only about ambiguous or missing values. Do not reload this guide or re-offer setup unless the architecture is missing, internally inconsistent, or the user asks to change it.

Reusable behavioral preferences are not workspace fields. They may influence future work only through a confirmed `[new-matter]` line in `lqplaybook.md`; client-confidential facts never belong there.

## Minimal fallback

If the user declines setup, cannot choose a destination, or lacks write capability, return a complete standalone matter record and label it unsaved. The absence of a shared architecture must not block intake or cause the skill to invent one.
