"""Plain-language rendering maps for the exported narratives document.

Machine vocabulary stays in deliverable.json; every enum rendered into
the Markdown maps to a plain-language line here. The "Status: " and
"Support: " prefixes and "### <workstreamId>" headings are stable anchors
relied on by the rendered-output rescanner; only the values are plain.
"""

SCOPE_SENTENCE = (
    "Checked only the sources you selected; this drafts narrative text for review "
    "and does not estimate time, decide billability, or post entries."
)
EMPTY_RESULT_LINE = (
    "No supportable work for the named lawyer was found in the selected sources."
)

STATUS_LINES = {
    "ready_for_user_review": "Status: drafts ready for your review",
    "partial_withheld": (
        "Status: drafts ready for your review - some work is withheld "
        "pending your confirmation"
    ),
    "no_supported_activity": (
        "Status: no supportable work found for the named lawyer in the selected sources"
    ),
    "incomplete": "Status: incomplete - questions remain before drafting",
}

SUPPORT_LINES = {
    "documentary_supported": "Support: documented in the selected sources",
    "user_attested": "Support: based on your express confirmation",
}

REASON_LINES = {
    "actor_unclear": "the sources do not establish who performed this",
    "matter_unclear": "the sources do not tie this to the named matter",
    "action_unclear": "the sources do not establish what was done",
    "object_unclear": "the sources do not establish what this work concerned",
    "source_unsupported": "this source could not back the claim",
    "source_unreadable": "this source could not be read at all",
    "source_partially_read": (
        "part of this source could not be read, so the detail from it was left out"
    ),
}
