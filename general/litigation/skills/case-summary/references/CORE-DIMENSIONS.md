# Core Dimensions — Practice-Agnostic

Every case, regardless of practice area, has the eight dimensions below. The agent searches the corpus for each one, cites what it finds, and synthesizes. Practice-area playbooks (`PLAYBOOK-*.md`) specialize these dimensions with domain-specific queries and output sections — they never replace the core.

Use this file as the checklist during the **Map** phase of the loop in `SKILL.md`. For base queries per dimension, see `SEARCH-PLAYBOOK.md`. For the extension contract, see `PLAYBOOK-AUTHORING.md`.

---

## 1. Parties & posture

**What it means:** Who are the real parties in interest, how are they aligned, who represents them, and what is the litigation or transactional posture (pre-suit, filed, discovery, trial, post-judgment, closing, regulatory proceeding).

**Done looks like:** Correct legal names of parties, their role, counsel of record, insurance/indemnity carriers where relevant, current stage of the matter.

**Extension slot:** Playbooks may add party-type columns (e.g., PI: insurer + adjuster; IP: patent owner + licensee + accused infringer; commercial: contracting entities + guarantors).

## 2. Timeline

**What it means:** A chronological spine of material events, with gaps flagged.

**Done looks like:** ISO-dated events, each citing a source object + page. Gaps greater than 30 days in active-matter periods flagged. Ambiguous dates tagged `[VERIFY]` (see `case-chronology/SKILL.md` for the convention).

**Extension slot:** Playbooks may add domain-specific event categories (e.g., PI: incident, treatment, MMI; commercial: formation, breach, notice, cure period; IP: filing, issuance, accused launch, cease-and-desist).

## 3. Evidence inventory

**What it means:** What documents, testimony, physical evidence, and third-party records exist, and what each is good for.

**Done looks like:** Named inventory grouped by evidence type. Each entry cites the object and notes its probative value.

**Extension slot:** Playbooks specify the evidence types that matter for their domain (e.g., PI: medical records, billing, photos, ER reports; commercial: contracts, invoices, communications, payment records; IP: prior art, product specs, marking, laboratory notebooks).

## 4. Claims & legal theories

**What it means:** The causes of action asserted (or assertable), with element-by-element evidence mapping.

**Done looks like:** Each claim listed with governing authority, elements, and a citation to evidence for each element. Elements lacking evidence are flagged.

**Extension slot:** Playbooks supply the element framework (e.g., PI: duty/breach/causation/damages; commercial: formation/performance/breach/damages; IP patent: infringement of each asserted claim element).

## 5. Exposure / remedies

**What it means:** What the plaintiff or moving party stands to recover (or the defendant stands to lose) if the claim succeeds. Not a valuation — a methodology and an evidence map.

**Done looks like:** Categories of relief identified (monetary, injunctive, declaratory, statutory, fee-shifting), each tied to documentary evidence and a computational approach. Ranges are acceptable; gaps are labeled.

**Extension slot:** Playbooks define the categories (e.g., PI: economic + non-economic + punitive; commercial: expectation/reliance/restitution + mitigation; IP: injunction + reasonable royalty + lost profits + willfulness multiplier + fees).

## 6. Defenses

**What it means:** What the opposing party has raised or could raise — affirmative defenses, denials, procedural defenses, and the evidence supporting each.

**Done looks like:** Pleaded defenses listed with the element each attacks, supporting evidence located (or gap flagged), and an assessment of likely strength.

**Extension slot:** Playbooks may emphasize domain-specific defenses (e.g., PI: comparative fault, pre-existing condition; commercial: failure-of-condition, frustration, unclean hands; IP: invalidity, non-infringement, inequitable conduct, laches).

## 7. Procedural status

**What it means:** Deadlines, pending motions, scheduling orders, discovery cutoffs, SOL, and required next acts.

**Done looks like:** A list of pending deadlines with dates and the sources; any SOL / statutory-notice concerns explicitly flagged.

**Extension slot:** Playbooks may add domain-specific pre-filing or pre-suit requirements (e.g., MA Ch. 93A 30-day, TX DTPA 60-day, Markman briefing, PTAB windows).

## 8. Red flags & open threads

**What it means:** Things that weaken the case, expose the client, or remain unresolved — honest assessment, not decoration.

**Done looks like:** A non-empty, attributable list. Each item cites the evidence that raised the flag and suggests the next action (investigate, concede, mitigate).

**Extension slot:** Playbooks contribute domain-specific red flags (e.g., PI: treatment gaps, social media, surveillance, prior claims; commercial: admissions in emails, waiver/estoppel evidence; IP: inventor-assignment gaps, prior public use).

---

## How modules plug in

A playbook module (`PLAYBOOK-<name>.md`) extends one or more of the eight dimensions by:

1. Adding **queries** that specialize the base queries in `SEARCH-PLAYBOOK.md`.
2. Adding **output sections** that slot into the core skeleton in `OUTPUT-TEMPLATE.md`.
3. Adding **quality-checklist items** that get appended to the core checklist.

A playbook must not redefine a core dimension or rename it. If an agent finds that a dimension does not apply to a given matter (e.g., a transactional closing has no "defenses"), it should note the dimension as "N/A — transactional posture" rather than omit it silently.
