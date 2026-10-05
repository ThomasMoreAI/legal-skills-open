"""Closed unit-assessment disposition/reason matrix."""

from __future__ import annotations

from typing import Any

QUESTION_REASONS = frozenset(
    "actor_unclear matter_unclear action_unclear object_unclear "
    "source_unsupported source_unreadable source_partially_read".split()
)
ASSESSMENT_REASONS: dict[str, frozenset[str | None]] = {
    "used": frozenset({None}),
    "read_but_unused": frozenset({"not_relevant"}),
    "excluded_other_actor": frozenset({"other_actor"}),
    "excluded_other_matter": frozenset({"other_matter"}),
    "excluded_non_work": frozenset({"non_work"}),
    "needs_confirmation": QUESTION_REASONS,
}


def assessment_pair_valid(disposition: Any, reason: Any) -> bool:
    return (
        disposition in ASSESSMENT_REASONS and reason in ASSESSMENT_REASONS[disposition]
    )
