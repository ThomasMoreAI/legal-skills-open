"""Apply selected-root filters and propagate descendant dispositions."""

from __future__ import annotations

from packet_core import parse_time


def _filter_source(
    source_type: str, source_time: str | None, filters: dict
) -> tuple[str, str | None]:
    if source_type not in filters["sourceTypes"]:
        return "excluded", "source_type_filter"
    since = parse_time(filters["since"], "filters.since", nullable=True)
    until = parse_time(filters["until"], "filters.until", nullable=True)
    if since is None and until is None:
        return "included", None
    if source_time is None:
        return "filter_indeterminate", "source_time_missing"
    observed = parse_time(source_time, "sourceTime", nullable=False)
    if (since and observed and observed < since) or (
        until and observed and observed > until
    ):
        return "excluded", "time_filter"
    return "included", None


def apply_source_filter(container: dict, root: dict, filters: dict) -> bool:
    disposition, reason = _filter_source(
        container["sourceType"], container["sourceTime"], filters
    )
    container["filterDisposition"] = disposition
    if disposition == "excluded":
        container.update(disposition="excluded", reason=reason)
        if container["containerId"] == root["containerId"]:
            root.update(disposition="excluded", reason=reason)
        return False
    if disposition == "filter_indeterminate":
        container.update(disposition="requiresConfirmation", reason=reason)
        root.update(disposition="requiresConfirmation", reason=reason)
    return True


def apply_selected_source_type_filter(
    container: dict, root: dict, filters: dict
) -> bool:
    if (
        container["parentContainerId"] is not None
        or container["sourceType"] in filters["sourceTypes"]
    ):
        return True
    root.update(disposition="excluded", reason="source_type_filter")
    container.update(
        filterDisposition="excluded",
        disposition="excluded",
        reason="source_type_filter",
    )
    return False


def apply_selected_source_filter(container: dict, root: dict, filters: dict) -> bool:
    if container["parentContainerId"] is not None:
        return True
    return apply_source_filter(container, root, filters)


def propagate_leaf_uncertainty(
    roots: list[dict], containers: list[dict], leaves: list[dict]
) -> None:
    uncertain_roots = {
        container["rootId"]
        for container in containers
        if container["parentContainerId"] is not None
        and container["disposition"] in {"requiresConfirmation", "unreadable"}
    }
    uncertain_roots.update(
        leaf["containerId"].split("-A", 1)[0]
        for leaf in leaves
        if leaf["disposition"] == "unreadable"
    )
    for root in roots:
        if root["rootId"] in uncertain_roots and root["disposition"] == "ready":
            root.update(
                disposition="requiresConfirmation", reason="descendant_unreadable"
            )
