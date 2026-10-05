# Automation settings

Automatic retrieval starts off. Offer two equal scope choices with no
recommendation and no preselection:

- **Selected projects:** tasks working in chosen folders and their subfolders.
- **All projects:** all tasks where the Wiki hooks are active.

A folder selection is an execution boundary, not permission to read every file
in that folder. Retrieval uses the current prompt to find existing Wiki notes.
A separate worktree outside a selected root must be selected separately.

When enabled, **Bring in relevant notes** searches the wiki as a prompt is
submitted and adds a small relevant set to the task's context.

Show a compact preview: scope, selected folders including subfolders, and the
retrieval state. Use this short notice: “Wiki will bring in relevant notes in
these projects. You can change this or turn it off through Wiki automation
settings.” For All projects say “across your tasks.” Only after the user
approves this preview, save the exact preference lines.

Saving new knowledge is an Add request: “Save the reusable lessons from this
conversation.” Prepare source-grounded proposals for review in the current
turn; never stage or retain the raw conversation.

## Optional command support

Resolve `wiki.py` to `scripts/wiki.py` beside the loaded `SKILL.md` and invoke
that absolute path, keeping the task's working directory. These examples are previews;
append `--yes` only after approval of that scope and retrieval setting:

```text
python3 wiki.py automation --scope projects --project /chosen/project --retrieval on
python3 wiki.py automation --scope all --retrieval on
python3 wiki.py automation
python3 wiki.py automation --project /another/project
python3 wiki.py automation --remove-project /chosen/project
python3 wiki.py automation --retrieval off
```

Repeat `--project` to select multiple roots. Adding and removing roots retains
other selected roots. To remove the last root, turn retrieval off first; then
choose a fresh scope when enabling again. Settings changes require their own
preview approval. Viewing settings is read-only.

Existing confirmed global settings keep their scope until the user changes it.
New enablement requires an explicit scope choice. A missing selected root or
unavailable task folder simply leaves automation inactive for that task.

## Storage and scope enforcement

The retrieval switch and scope selection are confirmed `[wiki]` playbook entries.
All projects is `- [wiki] automatic scope: all`. Selected projects uses
`- [wiki] automatic scope: projects:<sha256>` to select an immutable operational
file at `~/.wiki/automation-scopes/<sha256>.json` (beside the registry if its
location is overridden). That file contains only schema and canonical roots.
The digest binds the exact selection: modifying the file never expands scope.
Project paths stay out of the playbook, wiki notes, history and visual views.
Only the confirmed selection affects behaviour; proposed entries do nothing.

The retrieval hook checks the host's task `cwd` against that selection before
processing content. Paths are resolved, so a sibling with a similar name or a
symlink out of the selected root is outside scope.
