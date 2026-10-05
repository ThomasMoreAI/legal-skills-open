# Documents and folders for work outside chat

The lawyer may attach files, identify existing accessible paths, or point to a matter folder. This supplements the current conversation; it does not replace the lawyer's established account or make chat use compulsory. If the relevant work happened entirely elsewhere, accept the lawyer's brief account and selected material as the starting point.

## Select once, then work

- Naming files selects those files. Naming a folder as context selects its ordinary files and subfolders within that boundary. A runtime source root is containment, not permission to read everything beneath it.
- Do not request access confirmation again where the current request already selects the material. If a broad folder mixes matters, resolve the relevant subfolder or selection before reading bodies. A whole drive, home directory or unrelated project is not a matter folder.
- Use local standard-library adapters first. Host-native access or extraction is the next optional capability; use a firm-selected legal document integration only where explicitly available and authorised. Do not upload client files elsewhere to make the workflow run.
- With a local runtime, use `start_run.py --folder <relative folder>` alongside selected file paths, conversation snapshots and notes. Repeat the option for multiple selected folders; `--folder .` expressly selects the source root. The host supplies these options internally.
- Expansion includes all ordinary files, including hidden files and unsupported formats, in deterministic path order. No symlink, junction or other reparse point is followed, even if it points inside the folder. An unreadable directory or non-ordinary entry stops expansion with a reason; select ordinary files or a narrower folder to continue.
- The packet limit is 30 selected sources in total, including conversations and notes. Enumeration also stops above 1,000 directory entries or 20 nested levels. Do not silently take the first files or increase limits to make a folder fit. Explain the limit and identify a narrower matter subfolder or explicit selection with the lawyer.
- The request freezes the resulting file list. Later-added folder files are not silently included, and this is not a live folder monitor or a complete-workday claim. State the selected scope and any unreadable files. New evidence means a fresh combined packet, map and approval; do not append evidence to an approved map.

## Preserve the evidence

Supported source adapters are strict UTF-8 TXT/Markdown, EML and tracked-change DOCX. Unsupported material is accounted for as unreadable; it is not silently dropped. PDFs, scans and legacy mail containers do not become supported merely because they are in a selected folder. Where the host can produce a faithful supported extract, retain the original selected source as unsupported, preserve the extract's original-source locator and disclose conversion/coverage limits. Never relabel an extract as the lawyer's own attestation. Otherwise use the supported sources and ask only about material missing facts.

Use an appropriate existing local containment root for selected paths; it never expands the selection. For attachments or remote material exposed by the host, preserve original bytes and source identifiers in a private staging area, then run the same compiler. Do not copy a whole folder just to stage a few selected files. A local path that the host cannot access is not evidence; ask for accessible selected files or a short account instead.

Keep the author/editor, message sender, person performing the activity and named lawyer separate. A call note can corroborate the issues discussed without establishing that every recipient attended. Tracked changes can identify an editor without proving that the named lawyer did the underlying analysis. Document silence is “not corroborated”; a contrary account is a conflict requiring resolution.

For example: the chat establishes the lawyer's review of a termination clause; an added attendance note and the lawyer's account establish a separate client call. Retain both activities. An attached revised agreement made by a colleague can supply clause detail, but it cannot add “drafted the revisions” to the lawyer's entry. Do not count a workstream twice because a chat, email and draft describe the same activity.
