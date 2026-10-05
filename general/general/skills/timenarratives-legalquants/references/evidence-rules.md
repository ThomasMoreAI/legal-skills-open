# Evidence and attribution rules

## Unit assessment

Every packet unit eligible for semantic review receives exactly one state:

- `used` / `null`
- `read_but_unused` / `not_relevant`
- `excluded_other_actor` / `other_actor`
- `excluded_other_matter` / `other_matter`
- `excluded_non_work` / `non_work`
- `needs_confirmation` / one explicit actor, matter, action, object,
  unsupported-source or unreadable-source question reason

Only `used` units may back atoms. Quoted history, inline resources, divergent
alternatives, unreadable material and terminal failures cannot be promoted by
model judgment.

Conversation assistant, tool, quoted and unknown-role messages, and summary
snapshots, are context only. They cannot support included activity even when
their text says the lawyer completed it. User-role metadata identifies a
message source, not the authorship of everything pasted inside it. Preserve
the original speaker of quoted material. A lawyer's own substantive reasoning
or correction can support that contribution; a generation request alone
cannot establish review, adoption, delivery or completed substantive work.

## Event limbs

An included event requires support for actor, action, object and matter. An
atom references a source unit, exact UTF-8 byte span and span SHA-256; it does
not duplicate the quote. The model supplies the quote in the draft map; the
anchoring script supplies the span and the hash. The validator proves that the span exists and is
bound to the packet, not that the paraphrase is semantically correct.

Keep attribution fields separate:

- `assertedBy`: who authored or asserted the source material;
- `performedByActorId`: who performed the described action;
- `namedTimekeeperActorId`: whose candidate narrative this is;
- `clauseOwnerActorId`: whose output clause is being rendered.

All three actor-ID fields must resolve to the requested target for an included
event, but one field never proves another. At least one supporting `actor` atom
and one supporting `action` atom must come from units whose `sourceAuthor`
equals `assertedBy`, or from units with no parseable author (`sourceAuthor`
null) whose own anchored content carries the attribution — a file note or
memo identifying its author in its text is eligible on the same basis as
authored primary content. A unit whose parsed author differs
from the asserter never supports these limbs. An ancillary object or matter
author is insufficient. A DOCX revision author, an email sender and a note's
self-identification are all documentary assertions requiring the same
semantic and human review; none is authentication.

## Support inheritance

An event is `documentary_supported` only when every essential limb rests on
documentary atoms. If any essential limb rests on a confirmed user note, the
event and its clause are `user_attested`; documentary corroboration remains
visible but does not promote the class. Missing support withholds the event.

A compiler user note remains `user_attested`, `attested` and
`requires_confirmation` through proposal-map validation, bound to the target
actor and its user-note root/container. Exact digest-bound confirmation resolves
that attestation for rendering; it never changes the source class or unlocks a
documentary or divergent-MIME ambiguity.

One event belongs to one workstream and one clause. Split genuinely
cross-cutting activity into supported atomic events; never reuse one event to
inflate two narratives.

Assess distinct actions separately. A supported call remains draftable when
the same message describes revisions in future tense. A colleague's express
account of the target lawyer's work can support attribution; the colleague's
authorship alone is not grounds for withholding. A draft, ownership or a
revision author alone does not establish the target's substantive activity.

User-attested work may lack documentary corroboration; silence is not a
contradiction. An express conflicting attribution requires a factual answer
or withholding of that claim, not generic approval. Account for unsuccessful
or unfinished lawyer activity without promoting it to a completed outcome.
Dates of messages, dates of documents and dates of work are distinct; do not
substitute a known source date for a missing activity date.

The schema proves linkage and declared state, not semantic entailment.
Check that each final verb and claimed outcome stays within the supported
activity. Display material factual additions or changed wording before final
approval, and retain the digest of that displayed map.
