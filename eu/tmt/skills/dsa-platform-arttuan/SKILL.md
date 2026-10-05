---
name: dsa-platform-arttuan
title: DSA Platform
description: Work out which DSA layer you are (intermediary, hosting, platform, marketplace) and build the notice-and-action, statements of reasons and transparency duties that follow
author: ArttuAn
author_url: https://github.com/ArttuAn/eu-compliance-skills/tree/main/skills/dsa-platform
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: tmt
language: en
---

# DSA Platform

The Digital Services Act is layered, and the layer decides the duty list. The
mistake that costs the most is a small team concluding "the DSA is for Big Tech"
and missing that **hosting duties have no size exemption**. If one user can
publish something another user sees, you are a hosting service and you owe
notice-and-action and statements of reasons regardless of headcount.

What the micro and small exemption actually removes is the *online platform*
duties in Section 3 — complaint handling, trusted flaggers, ads transparency,
recommender disclosure. That is a real and significant relief. It is not an
exemption from the DSA.

> **Not legal advice.** Which layer applies, and whether content is illegal, are
> legal judgements. This skill produces the layer analysis, the duty list and the
> mechanisms.

```
  does anyone transmit / cache / store third-party info?
        │ no ──► not an intermediary. Record the exclusion + expires_if.
        ▼ yes
  hosting?  (you store info provided by a recipient)
        │ yes ──► Arts. 16-18  — NO size exemption
        ▼
  online platform?  (you also disseminate it to the public)
        │ yes ──► Section 3 — UNLESS micro/small
        ▼
  marketplace?  ──► trader traceability (Arts. 30-32)
        │
  45M+ monthly active EU recipients ──► VLOP, by Commission designation only
```

## Use this when

- Users can post anything another user can see: comments, reviews, profiles,
  uploads, shared documents, public snippets, a community forum.
- You run a marketplace, an app store, or anything where third parties sell to
  consumers.
- You rank or recommend user content, or run advertising against it.
- Someone asks for your DSA point of contact or transparency report, which
  business customers now do routinely.

**Do not use this when** nothing a user submits is ever visible to another user.
Record it: `expires_if: any feature lets one user publish content another user
can see`. The comment feature, the shared-link feature and the public-profile
feature are the three that flip it, and all three get shipped without anyone
re-running the scoping.

Note that **private messaging between users is still hosting** if you store the
messages — the public-dissemination test separates hosting from *platform*, not
from the DSA.

## Ask first

1. **"Can a user publish, upload or send something that another user sees? List
   every such surface."**
   The layer question. Enumerate: comments, reviews, profile fields, avatars,
   file uploads, shared links, messages, forum posts.
2. **"Is any of it visible to the public, or only to a chosen recipient?"**
   Public dissemination is what turns hosting into an online platform.
3. **"Do third parties sell goods or services to consumers through you?"**
   Marketplace duties: trader traceability, and best-effort verification.
4. **"Headcount and turnover?"**
   Decides Section 3 only.
5. **"Today, how does someone report illegal content, and what happens next?"**
   If the answer is "they email support", that is the finding.
6. **"When you remove content or suspend an account, is the user told why, in a
   way they can challenge?"**
   Art. 17 statements of reasons, and the internal complaint system.
7. **"Do you profile users for advertising or recommendations? Are any of them
   minors?"**
   Arts. 26-28. Two hard prohibitions live here.
8. **"Are you established in the EU? If not, who is your legal representative?"**
   Art. 13 requires a designated legal representative for non-EU providers.

## What the law requires

**Regulation (EU) 2022/2065.** Fully applicable since 17 February 2024. Directly
applicable — no transposition — though enforcement runs through national Digital
Services Coordinators.

### The layers and their duties

| Layer | Who | Core duties |
| --- | --- | --- |
| **All intermediaries** | Mere conduit, caching, hosting | Single point of contact for authorities (Art. 11) and for recipients (Art. 12); legal representative if non-EU (Art. 13); terms and conditions including content-moderation information (Art. 14); transparency reports (Art. 15, **not** micro/small) |
| **Hosting** | You store information provided by a recipient | Notice and action (Art. 16); statement of reasons (Art. 17); report suspicions of criminal offences threatening life or safety (Art. 18) |
| **Online platforms** | Hosting **plus** dissemination to the public | Everything above, plus Section 3 — **micro/small exempt** |
| **Marketplaces** | Platforms allowing distance contracts with traders | Trader traceability (Art. 30), compliance by design (Art. 31), information on illegal products (Art. 32) |
| **VLOP / VLOSE** | 45M+ monthly active EU recipients, **designated by the Commission** | Systemic risk assessment, independent audit, data access, crisis response |

### Section 3, for online platforms above the size threshold

- **Art. 20** internal complaint-handling system, free, for at least six months
  after a decision.
- **Art. 21** out-of-court dispute settlement — users can go to a certified body
  and you must engage.
- **Art. 22** trusted flaggers — their notices get priority.
- **Art. 23** measures against misuse: suspend users who frequently post
  manifestly illegal content, and notifiers who frequently submit manifestly
  unfounded notices. Both directions, with prior warning.
- **Art. 25** no dark patterns: no interface that deceives, manipulates, or
  materially distorts a recipient's ability to make free decisions.
- **Art. 26** advertising transparency: clearly marked, who paid, why this user
  is seeing it. **Art. 26(3): no ads targeted using special-category data.**
- **Art. 27** recommender transparency: the main parameters, in plain language,
  in the T&Cs, plus a way to change them.
- **Art. 28** protection of minors: a high level of privacy, safety and security
  by design, and **no advertising based on profiling where you are aware with
  reasonable certainty the recipient is a minor**.

Arts. 26(3) and 28(2) are prohibitions, not disclosures. They are engineering
constraints in the ad-serving path, not paragraphs in a policy.

### Notice and action, specifically

Art. 16 requires a mechanism that is **electronic, easy to access and
user-friendly**, and a notice must be able to carry: a substantiated explanation
of why the content is illegal, the exact URL, the notifier's name and email
(except for certain offences), and a good-faith statement. A notice with those
elements gives you **actual knowledge**, which is what removes the hosting
liability exemption under Art. 6 — so the timestamp on receipt matters legally.

You must act in a **timely, diligent, non-arbitrary and objective** manner, and
confirm receipt.

## What to produce

**1. The layer analysis**, with the reasoning:

```yaml
dsa:
  layer: hosting                     # intermediary | hosting | platform | marketplace
  layer_reasoning: >
    Users upload documents and share them by link with named recipients. Stored
    on our infrastructure (hosting). Not disseminated to the public, so the
    online-platform duties in Section 3 are not engaged.
  public_dissemination: false
  size_exempt_section_3: true
  size_reasoning: "22 staff, EUR 3.1M turnover - micro/small"
  legal_representative: "not required; established in FI"
  duties: ["Art. 11", "Art. 12", "Art. 14", "Art. 16", "Art. 17", "Art. 18"]
  expires_if: "any surface makes user content visible to the public"
```

**2. The notice-and-action endpoint**, with the required fields and a
timestamped receipt:

```python
@dataclass
class Notice:
    url: str                       # exact location - required
    reason: str                    # substantiated explanation of illegality
    notifier_name: str | None      # may be omitted for certain offences
    notifier_email: str | None
    good_faith: bool
    received_at: datetime          # this timestamp is the actual-knowledge moment

    def complete(self) -> tuple[bool, list[str]]:
        missing = [f for f in ("url", "reason") if not getattr(self, f)]
        if not self.good_faith:
            missing.append("good_faith")
        return not missing, missing
```

Store every notice, including rejected ones, with the decision and its reasoning.
That register is the evidence that you acted diligently and non-arbitrarily.

**3. Statements of reasons.** Every restriction — removal, demotion, demonetisation,
suspension — produces one, to the affected user, containing: the decision and its
scope, the facts relied on, whether automated means were used, the legal or T&Cs
ground, and how to appeal. Online platforms must also submit them to the
Commission's **DSA Transparency Database**.

**4. Ad and recommender constraints, in code:**

```python
def can_target(user, segment) -> tuple[bool, str]:
    if segment.uses_special_category_data:
        return False, "Art. 26(3): ads may not be targeted using Art. 9 GDPR data"
    if user.is_minor_with_reasonable_certainty and segment.uses_profiling:
        return False, "Art. 28(2): no profiling-based ads to minors"
    return True, "ok"
```

A policy document does not implement Arts. 26(3) and 28(2). A function in the
ad-serving path does.

**5. T&Cs that say what the moderation actually is** (Art. 14): the policies,
procedures, tools and human review used, in clear and plain language. If minors
are a target group, in terms they can understand.

**6. A transparency report**, unless micro/small: notices received and acted on,
by category and source; own-initiative moderation; complaints and outcomes;
automated means used and their error rates.

**Every assessment carries a certainty.** Each finding, each applicable or
ruled-out regime, and the headline of the brief carry `certainty` (0–100) — the
honest percent of the assessment that rests on verified sources and confirmed
facts rather than inference, open unknowns and interpretation. Wherever you
state an applicability, a classification, a citation-backed obligation or a
finding, show the percentage **and the single largest reason it is not higher**:
"ruled out NIS2 — certainty 66%: the national transposition was not read".
`references/certainty.md` holds the anchors; the rules that matter here: an
answer graded `UNKNOWN` caps anything resting on it at 70, an unread Directive
transposition caps at 60, a classification pending counsel caps at 50, and a
`100` requires every deciding fact SPECIFIC, every citation verified on EUR-Lex,
every transposition read and every regime screened. Certainty is visibility, not
a free pass — VAGUE stays rejected, an open blocker stays blocked.

## Failure modes

- **"The DSA is for Big Tech."** Hosting duties have no size exemption. The
  comment feature put you in scope.

- **Treating the micro/small exemption as total.** It removes Section 3 only.
  Arts. 11-18 remain.

- **A notice mechanism behind a support email.** Art. 16 requires an electronic,
  easy-to-access, user-friendly mechanism that can carry the specified elements.
  A generic inbox is neither, and it also makes your actual-knowledge timestamp
  unprovable.

- **No statement of reasons.** Content removed, user told nothing, no appeal
  route. Art. 17 breach on every removal, at scale.

- **Arts. 26(3) and 28(2) written as policy.** They are prohibitions in the
  serving path. If the code can target a minor by profile, the policy is not a
  control.

- **Over-removal to be safe.** The DSA also protects recipients: arbitrary
  removal, no reasons, no appeal is itself the breach. Diligent and
  non-arbitrary cuts both ways.

- **Forgetting the legal representative.** A non-EU provider without a
  designated Art. 13 representative has an immediate, easily-checked gap.

- **Assuming VLOP duties apply because you are large.** VLOP status follows a
  Commission designation. Absent one, you are not a VLOP.

## Verify

Follow `references/verification.md`. For this skill specifically:

1. **Tier 0** — install, `--help`, classify a fixture service and emit duties.

2. **Tier 1** — `pytest -q`, offline:

```python
def test_hosting_duties_have_no_size_exemption(brief_small_host):
    duties = classify(brief_small_host).duties
    assert "Art. 16" in duties and "Art. 17" in duties
    assert "Art. 20" not in duties          # Section 3 correctly exempt


def test_private_sharing_is_hosting_not_platform(brief_private_sharing):
    result = classify(brief_private_sharing)
    assert result.layer == "hosting"
    assert result.public_dissemination is False


def test_public_dissemination_makes_it_a_platform(brief_public_feed):
    assert classify(brief_public_feed).layer == "platform"


def test_no_user_content_is_ruled_out_with_an_expiry(brief_no_ugc):
    exclusion = classify(brief_no_ugc).exclusion
    assert "visible to the public" in exclusion["expires_if"] or \
           "another user can see" in exclusion["expires_if"]


def test_notice_requires_url_and_substantiated_reason():
    ok, missing = Notice(url="", reason="bad", good_faith=True,
                         notifier_name=None, notifier_email=None,
                         received_at=now()).complete()
    assert not ok and "url" in missing


def test_receipt_timestamp_is_recorded(notice_endpoint):
    response = notice_endpoint.submit(valid_notice())
    assert response.received_at is not None
    assert notice_endpoint.register[-1].received_at == response.received_at


def test_rejected_notices_are_kept_with_reasoning(notice_endpoint):
    notice_endpoint.reject(valid_notice(), reason="content is not illegal in FI")
    assert notice_endpoint.register[-1].decision_reasoning


def test_every_restriction_emits_a_statement_of_reasons(moderation):
    moderation.remove(content_id="c1", ground="T&Cs 4.2", automated=True)
    sor = moderation.statements[-1]
    for field in ("decision", "facts", "automated_means", "ground", "appeal_route"):
        assert getattr(sor, field) is not None


def test_special_category_targeting_is_refused():
    ok, reason = can_target(adult_user(), segment(uses_special_category_data=True))
    assert not ok and "Art. 26(3)" in reason


def test_profiling_ads_to_minors_are_refused():
    ok, reason = can_target(minor_user(), segment(uses_profiling=True))
    assert not ok and "Art. 28(2)" in reason


def test_non_eu_provider_needs_a_legal_representative(brief_us_host):
    finding = classify(brief_us_host).finding_for("Art. 13")
    assert finding.severity == "condition"


def test_vlop_duties_require_designation(brief_large_platform):
    duties = classify(brief_large_platform).duties
    assert not any("Art. 34" in d for d in duties)      # no designation, no VLOP duties
```

3. **Tier 2** — report: the layer and its reasoning, the duty list, whether the
   notice mechanism accepts every required element, and the median time from
   notice receipt to decision. That median is the number a Digital Services
   Coordinator will ask about.

4. **Tier 3** — submit a notice yourself, from outside, through the published
   mechanism. Time how long it takes to reach a human who can act, and check
   that a statement of reasons actually reaches the affected user. Both usually
   surprise people.

Then tell the user which layer you concluded and why, and that the layer
analysis and any illegality assessment need confirming — you produced the
mechanism, not the judgement.
