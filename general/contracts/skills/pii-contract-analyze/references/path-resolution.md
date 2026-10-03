# File Input Handling & Path Resolution

## CRITICAL PRIVACY RULE

Always use `anonymize_file(file_path)` — NEVER extract text yourself and pass it to `anonymize_text`. When you extract text in the conversation, the raw text enters Claude's context window and passes through the API — defeating the purpose of anonymization. With `anonymize_file`, only the file PATH (a short string) goes through the API. The MCP server reads and anonymizes the file locally. PII never leaves the user's machine.

## How to determine the file path — happy path

Just pass what the user gave you. The server auto-resolves:

1. **The input as-given** (`path.resolve`) — if you have a valid absolute path it just works.
2. **`$PII_WORK_DIR/<basename>`** if the user configured a workspace dir.
3. **BFS (depth 4)** of `~/Downloads`, `~/Documents`, `~/Desktop`, `$PII_WORK_DIR` for an unambiguous match.

For most users, passing the filename as they mentioned it is enough. Example:

```
anonymize_file(file_path: "contract.docx")
```

## Fallback for non-standard locations — marker + resolve_path

If `anonymize_file` returns `status: "error"` with `"File not found via auto-search"` or `"Ambiguous filename"` in the hint, the file is either in an uncommon directory OR there are multiple copies. Resolve explicitly:

```bash
MARKER=".pii_marker_$(openssl rand -hex 4)"
touch "/path/visible/to/you/$MARKER"
```

Then:

```
resolve_path(filename: "contract.docx", marker: "$MARKER")
```

That returns `{ host_path, host_dir }` — the absolute path on the host. The marker is auto-deleted. Retry with:

```
anonymize_file(file_path: "<host_path>")
```

The marker+resolve_path tools stay available as a reliability net; auto-BFS handles ~95% of cases.

## `find_file` (secondary fallback)

If `PII_WORK_DIR` is configured and `resolve_path` isn't appropriate (user doesn't want to touch the filesystem), `find_file(filename)` searches just `$PII_WORK_DIR`. Narrower scope than auto-BFS, but useful when auto-BFS returned "ambiguous" and you want to restrict the search to the configured workspace only.

## Using the returned paths

`anonymize_file` returns both absolute and relative forms of output paths:

- `output_path` — absolute host path (e.g. `C:\Users\User\Downloads\foo\pii_shield_X\doc_anonymized.txt`). Works if your environment can reach host paths directly.
- `output_rel_path` — relative to the INPUT file's directory (e.g. `pii_shield_X/doc_anonymized.txt`). Always portable: join with the directory of the path you passed in and you have a file you can `Read`.
- For .docx inputs there's also `docx_output_path` + `docx_output_rel_path` for the `.docx` companion.
- `output_dir` — absolute path to the dedicated per-session subfolder. Put any files YOU create (tracked-changes .docx, memo .docx) inside it.

**Reading rule of thumb**: if in doubt, use `<input_dir>/<output_rel_path>`. It works everywhere.

**Supported input formats**: `.pdf`, `.docx`, `.txt`, `.md`, `.csv`

**DO NOT** extract text yourself using pdfplumber/python-docx/Read and pass it to `anonymize_text`. This leaks PII through the API. The ONLY acceptable use of `anonymize_text` is when the user explicitly pastes text into the chat (in which case PII is already in the conversation).
