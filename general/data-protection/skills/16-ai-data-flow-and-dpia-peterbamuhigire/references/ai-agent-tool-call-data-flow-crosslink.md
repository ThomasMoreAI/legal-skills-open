# Agent Tool-Call Data Flow Cross-Link

The AI Data Flow and DPIA spec models the data flow of AI features. For agent features, every tool call creates a new data flow that must be in the diagram.

## Agent-specific data flows

| Flow | From | To | Through | Personal data? |
|------|------|-----|----------|------------------|
| Plan generation | user input + agent observations | model provider | model gateway | sometimes (e.g. inbox text) |
| Tool invocation | agent dispatcher | internal API | dispatcher + audit log | depends on tool |
| External tool invocation | agent dispatcher | external API / vendor | dispatcher + audit log | depends on tool |
| Tool result return | external API / vendor | agent | dispatcher (sanitiser + audit log) | depends |
| Episodic memory write | dispatcher | per-tenant memory store | redactor | usually |
| Long-term memory write | dispatcher | per-tenant LT store (opt-in) | redactor | usually; opt-in gate |

## DPIA additions for agent features

Per the DPIA addendum template, add for any agent feature:

- The complete list of tools the agent may call (cross-link to `Action_Catalogue_Spec.md`).
- For each tool with side-effect `write-external`: the recipient party, the DPA in place, the data classes transferred.
- For each tool with side-effect `billing`: the financial regulator scope.
- The memory-tier retention TTLs.
- The audit-log retention per event class.
- The kill-switch behaviour (data minimisation evidence — data flow stops on kill).
- The contestability path.
- The human-final-decision points for irreversible actions.

## When a fresh DPIA is required

- New tool added to an agent feature with `side_effect_class != read`.
- New external sub-processor introduced via a tool.
- Autonomy-level promotion (e.g. L1 → L2 or L2 → L3).
- New tenant region with stricter DPA.

The `dpia-generator` skill (Uganda domain) is invoked for any Uganda-tenant agent processing operation that meets DPPA Regulation 12 triggers.
