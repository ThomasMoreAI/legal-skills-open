# Logs and telemetry

A log line carrying a user id, account id, session id, device id or IP address is personal data. Art 5(1)(e) applies to it, Art 30(1)(f) requires a period for it, and Art 17 requests reach it. Log retention is not an infrastructure preference, it is a processing activity that nobody wrote down.

## Three classes, three different arguments

Do not set one period for "logs". The purposes differ, so the maxima differ.

| Class | Contents | Purpose | Typical defensible period | Argument |
|---|---|---|---|---|
| Security / audit | authentication events, authorisation decisions, admin actions, access to sensitive records | detecting and investigating incidents; Art 32 accountability | 6 to 24 months | attacker dwell time and the need to reconstruct an incident after late discovery |
| Application / operational | request logs, error traces, stack traces, performance spans | debugging and availability | 7 to 90 days | after the release cycle has moved on, the line has no debugging value |
| Analytics / product | page views, feature usage, funnels | product decisions | 14 months at raw grain, indefinite in aggregate | the raw event has short marginal value; the aggregate should carry no identifier |

The three classes must be **separately sinkable**. If everything lands in one index with one ILM policy, the security argument drags the whole estate up to two years and Art 5(1)(e) is breached for the other two classes.

## The NIS2 pull, and how to resolve it

Incident-response and regulatory reporting obligations push security-log retention up; storage limitation pushes it down. The resolution is not a compromise number, it is a **split**:

- keep the high-cardinality, identifier-bearing detail for the shorter window that covers realistic investigation
- keep a reduced record — event type, timestamp, coarse actor reference, outcome — for the longer window that covers regulatory reporting
- document the split as the criteria under Art 13(2)(a), because the period genuinely differs by field

`[[UNVERIFIED: whether Directive (EU) 2022/2555 (NIS2) or its national transpositions impose an explicit log-retention period rather than only incident-reporting deadlines. Verify before asserting a NIS2 number in a schedule]]`

Never argue "NIS2 requires it" without the article. Where the obligation is your own security interest rather than a statute, the basis is Art 6(1)(f) and the period comes from your own documented reasoning, not from a directive.

## IP addresses

An IP address is personal data in the hands of a controller that can, by legally available means, obtain the additional information to identify the subscriber. This is the settled position for dynamic addresses under the Breyer line of authority.

`[[UNVERIFIED: exact citation and holding of CJEU C-582/14 Breyer — verify against curia.europa.eu before quoting]]`

Options, in descending order of how much they actually help:

| Technique | Effect | Still personal data? |
|---|---|---|
| Drop the field entirely | best | no |
| Truncate IPv4 to /24 and IPv6 to /48 at ingest | material reduction in identifiability | usually yes, but weakly |
| Keyed hash with a rotating salt, salt not stored with the log | pseudonymisation (Art 4(5)) | yes |
| Unkeyed hash (SHA-256 of the address) | reversible by exhaustive search over 2^32 addresses | yes, trivially |

Truncate **at ingest, in the collector**, not in a downstream job. A downstream job means the full address existed in the buffer, the queue and the raw index, each with its own retention.

Unkeyed hashing of an IP address is not anonymisation and should never be described as such in a privacy notice. The IPv4 space is small enough to enumerate in seconds.

## What must never enter a log

Enforce these at the logging library, not by review:

- card verification codes, full track data, PIN blocks (period zero, see `sector-overlays.md`)
- full PAN, unless the sink is inside the cardholder data environment and rendered unreadable
- passwords, tokens, API keys, session cookies, authorization headers
- Art 9 data (health, biometrics, and anything that reveals them by inference from a URL path)
- full request and response bodies for endpoints that carry personal data

Implement as a serialiser-level redaction list plus a CI check on structured-log field names. Redaction in the log aggregator is too late: the line already crossed the network and landed in the agent's local buffer.

## Sampling and cardinality as a retention control

Reducing what you keep beats deleting what you kept:

- sample successful requests aggressively, keep errors at full rate
- drop the identifier from the metric and keep it only on the trace
- pre-aggregate analytics events into daily counters and expire the raw events, rather than keeping raw events for the aggregate's sake
- do not attach a user id to a metric label; it makes the whole time series personal data with the series' retention

## Deletion and erasure inside a log estate

An Art 17 request against an append-only log store is genuinely hard. The realistic positions:

1. **Time-bound it.** A log store with a hard 30-day ILM delete phase converts the erasure question into a wait, and that is a defensible answer if the period is short and documented.
2. **Index by subject.** If the store supports delete-by-query (Elasticsearch, OpenSearch), you can execute the request — but see `impl-storage.md` for the fact that documents are only marked deleted until segment merge.
3. **Do not put the identifier in.** Log a pseudonymous request id and keep the mapping in a store you can delete from. Erasure then removes the mapping, and the log line stops being attributable.

Option 3 is the only one that scales. Design for it before the estate exists.

## Third-party log sinks

Each of these is a processor holding a full copy with its own default retention, which is almost never the one you chose:

- error tracker (Sentry and equivalents) — captured request payloads, breadcrumbs, user context
- APM and tracing vendor — span attributes, HTTP payload samples
- log aggregation SaaS — retention tier, plus a separate archive tier that survives the retention tier
- session replay — DOM recordings including form field contents
- LLM API provider — prompt and completion logs, with a provider-side abuse-monitoring retention independent of your account setting

Record the configured retention and the vendor's own floor for each in `copy-inventory.md`.

## Checkpoints

- [ ] Security, application and analytics logs are separately routed and separately expired
- [ ] Each class has a written period and a written reason, not a shared default
- [ ] Security-log split into detailed short-window and reduced long-window records, if a long window is claimed
- [ ] IP truncation or dropping happens in the collector, at ingest
- [ ] No unkeyed hash of an IP address is described as anonymisation anywhere
- [ ] Redaction list enforced at the logging library, with a CI check on field names
- [ ] No card verification code, PAN, token or password reachable by a grep over the log estate
- [ ] User ids absent from metric labels
- [ ] Log-store erasure strategy chosen explicitly and documented (time-bound, delete-by-query, or pseudonymous by design)
- [ ] Every third-party sink's configured retention and vendor floor recorded
