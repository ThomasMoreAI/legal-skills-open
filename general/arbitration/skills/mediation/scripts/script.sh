#!/usr/bin/env bash
# mediation — Alternative Dispute Resolution Reference
# Powered by BytesAgain | bytesagain.com | hello@bytesagain.com
set -euo pipefail

VERSION="1.0.0"

cmd_intro() {
    cat << 'EOF'
=== Mediation & Alternative Dispute Resolution ===

Mediation is a structured negotiation process in which a neutral
third party (the mediator) assists disputing parties in reaching
a voluntary, mutually acceptable resolution.

Key Principles:
  Voluntary:        Parties choose to participate and can leave
  Confidential:     Discussions cannot be used in court
  Self-determination: Parties control the outcome (not the mediator)
  Neutral:          Mediator has no stake and no decision-making power
  Interest-based:   Focuses on needs, not legal positions

Mediation vs Litigation vs Arbitration:
  Feature          Mediation     Arbitration    Litigation
  Decision-maker   Parties       Arbitrator     Judge/Jury
  Binding?         If settled    Yes            Yes
  Confidential?    Yes           Usually        No (public)
  Cost             $              $$             $$$
  Duration         Days-weeks    Months         Years
  Relationship     Preserved     Strained       Adversarial
  Flexibility      High          Medium         Low
  Appeal           N/A           Very limited   Yes

Success Rates:
  Commercial mediation: 70-85% settlement rate
  Employment disputes: 60-75%
  Personal injury: 80-90%
  Family/divorce: 50-70%
  Construction: 75-85%

When Mediation Works Best:
  - Ongoing relationship (business partners, neighbors, family)
  - Both parties want resolution (not precedent)
  - Issues are negotiable (money, terms, future conduct)
  - Power imbalance is manageable
  - Emotions need to be acknowledged and processed

When Mediation May NOT Work:
  - One party needs a legal precedent
  - Domestic violence or extreme power imbalance
  - Party is not attending in good faith
  - Criminal matters (though victim-offender mediation exists)
  - Injunctive relief needed urgently
EOF
}

cmd_process() {
    cat << 'EOF'
=== Mediation Process Stages ===

Stage 1 — Pre-Mediation:
  - Mediator selected (agreed by both parties)
  - Confidentiality agreement signed
  - Mediation agreement signed (ground rules)
  - Position statements exchanged (optional)
  - Documents/evidence shared in advance
  - Logistics: date, venue, participants, authority to settle

Stage 2 — Opening Statement (Mediator):
  - Welcome and introductions
  - Explain mediation process and ground rules
  - Emphasize confidentiality and voluntariness
  - Clarify mediator's role (facilitator, not judge)
  - Set agenda and time expectations
  Duration: 10-15 minutes

Stage 3 — Party Opening Statements:
  - Each party presents their perspective uninterrupted
  - Not legal arguments — tell the story, express impact
  - Mediator listens actively, takes notes
  - Other party listens (no interruptions, no rebuttal yet)
  Duration: 10-30 minutes per party

Stage 4 — Joint Discussion:
  - Mediator identifies common ground and key issues
  - Parties respond to each other (facilitated)
  - Clarify misunderstandings
  - Begin exploring interests behind positions
  Duration: 30-60 minutes

Stage 5 — Caucus (Private Sessions):
  - Mediator meets each party separately
  - Confidential — mediator only shares what party permits
  - Reality testing: "What happens if you don't settle?"
  - Explore flexibility, hidden interests, bottom lines
  - Multiple rounds of caucus typical
  Duration: 20-45 minutes per caucus, multiple rounds

Stage 6 — Negotiation/Bargaining:
  - Exchange proposals (shuttle diplomacy via mediator)
  - Bracket negotiation: narrow the gap incrementally
  - Package deals: trade across issues
  - Mediator's proposal: last resort suggestion
  Duration: varies widely

Stage 7 — Agreement/Closure:
  If settled:
    - Draft settlement terms in writing
    - Both parties and counsel review
    - Sign memorandum of understanding
    - Formal agreement drafted by attorneys afterward
  If impasse:
    - Mediator summarizes progress made
    - Identify remaining barriers
    - Schedule follow-up session or next steps
    - Mediation can be reconvened later
EOF
}

cmd_techniques() {
    cat << 'EOF'
=== Mediator Techniques ===

Active Listening:
  - Paraphrase: "So what I hear you saying is..."
  - Reflect emotions: "It sounds like you feel frustrated by..."
  - Summarize: consolidate key points periodically
  - Open questions: "Can you tell me more about...?"
  - Silence: let parties fill the space (powerful tool)

Reframing:
  Transform negative/adversarial statements into neutral/positive
  Before: "They deliberately cheated us on the contract!"
  After:  "You feel the contract terms weren't honored as expected."
  Before: "He's impossible to work with."
  After:  "It sounds like communication has been challenging."
  Purpose: reduce emotional charge, open exploration

Reality Testing:
  Challenge unrealistic expectations in caucus:
  "What do you think a court would award?"
  "How long would litigation take?"
  "What would legal fees cost through trial?"
  "What's your best evidence on this point?"
  "If the judge rules against you, what happens?"
  Purpose: move parties from positions to realistic ranges

BATNA/WATNA Analysis:
  BATNA: Best Alternative To a Negotiated Agreement
    "If you don't settle today, what's your best outcome?"
  WATNA: Worst Alternative To a Negotiated Agreement
    "What's the worst that could happen in court?"
  MLATNA: Most Likely Alternative
    "Realistically, what would probably happen?"
  Purpose: help parties evaluate settlement against alternatives

Bracketing:
  Narrow the negotiation range systematically:
    Round 1: P demands $1M, D offers $100K (range: $900K)
    Round 2: P drops to $750K, D raises to $250K (range: $500K)
    Round 3: P drops to $600K, D raises to $350K (range: $250K)
    Round 4: Settle at $475K
  Mediator helps each side make proportional moves

Mediator's Proposal:
  Last-resort technique when parties are close but stuck
  Mediator privately proposes same number to both sides
  Each party says yes or no confidentially
  If both say yes: deal done
  If one says no: neither party knows the other's answer
  Preserves face — no one "gives in"

Interest Exploration:
  Position: "I want $500,000"
  Interest: "I need to cover medical bills and lost wages"
  Deeper interest: "I want to feel made whole and acknowledged"
  Technique: "Why is that important to you?"
  When interests are uncovered, creative solutions emerge
EOF
}

cmd_types() {
    cat << 'EOF'
=== ADR Spectrum ===

From least to most formal:

1. Negotiation:
   Direct discussion between parties (no third party)
   Cheapest, fastest, most private
   Works when: relationship is functional, stakes manageable
   Risk: power imbalance, emotional escalation

2. Mediation:
   Neutral facilitator, non-binding, voluntary
   Evaluative: mediator gives opinions on merits
   Facilitative: mediator facilitates, no opinion
   Transformative: focuses on empowerment and recognition
   Settlement rate: 70-85%

3. Med-Arb (Mediation-Arbitration):
   Start with mediation, switch to arbitration if no deal
   Same neutral or different neutral for each phase
   Pros: guaranteed resolution in one process
   Cons: parties may withhold info in mediation (fear of arb)

4. Early Neutral Evaluation (ENE):
   Expert gives non-binding assessment of case merits
   Usually 1-2 hour hearing, advisory opinion
   Helps parties calibrate expectations early
   Common in: patent, construction, medical cases

5. Mini-Trial:
   Abbreviated presentation of each side's best case
   Decision-makers (senior execs) observe
   Then negotiate based on what they saw
   Common in: large commercial disputes

6. Arbitration:
   Quasi-judicial process, binding decision
   Arbitrator chosen by parties (or institution)
   Limited discovery, streamlined procedure
   Very limited appeal (vacate only for fraud, bias, misconduct)
   Institutions: AAA, JAMS, ICC, LCIA

7. Online Dispute Resolution (ODR):
   Technology-assisted ADR (video, AI, platforms)
   Examples: eBay Resolution Center, Modria, ICANN UDRP
   Growing rapidly for e-commerce and small claims
   AI-assisted triage and initial resolution

Choosing the Right Method:
  Need precedent?           → Litigation
  Need binding decision?    → Arbitration
  Need relationship?        → Mediation
  Need speed + low cost?    → Mediation > Arbitration
  International dispute?    → Arbitration (enforceable globally)
  Consumer/small claim?     → ODR
EOF
}

cmd_preparation() {
    cat << 'EOF'
=== Mediation Preparation ===

For Parties/Counsel — Before Mediation Day:

1. Analyze Your Case:
   Strengths: what evidence/law favors you
   Weaknesses: what the other side will argue
   Best case outcome (BATNA): what you'd likely get at trial
   Worst case outcome (WATNA): what you'd get if you lose
   Realistic outcome (MLATNA): most probable trial result
   Litigation cost estimate: attorney fees through trial

2. Define Your Interests:
   Why do you want what you want? (beyond money)
   What non-monetary outcomes would help?
   What would closure look like?
   Are there ongoing relationship considerations?

3. Prepare Position Statement (if requested):
   1-3 pages typically
   Brief factual background
   Key issues in dispute
   Your position and supporting reasons
   What you think a fair resolution looks like
   Confidential section: for mediator's eyes only

4. Gather Documents:
   Contract/agreement in dispute
   Key correspondence (emails, letters)
   Financial documents (damages calculation)
   Expert reports (if any)
   Prior settlement discussions (summary only)

5. Authority:
   Ensure decision-maker is present (not just lawyer)
   If corporate: get settlement authority range in advance
   Insurance: adjuster with authority to settle
   "Full authority" means ability to say yes at any reasonable number

6. Logistics:
   Confirm date, time, venue
   Separate rooms for caucuses
   Bring multiple copies of key documents
   Plan for a full day (don't schedule hard stops)
   Bring calculator, authority documents, checkbook

Mediation Brief Outline:
  I.   Introduction (1 paragraph)
  II.  Factual Background (1-2 pages)
  III. Legal Issues (1 page)
  IV.  Damages/Claims (with calculations)
  V.   Settlement Efforts to Date
  VI.  Desired Outcome
  VII. Confidential Section (bottom line, flexibility)
EOF
}

cmd_settlement() {
    cat << 'EOF'
=== Settlement Agreements ===

A mediated settlement agreement is a binding contract once signed.
It must contain all essential terms to be enforceable.

Essential Elements:
  1. Parties (full legal names)
  2. Recitals ("WHEREAS..." — background of dispute)
  3. Settlement terms (specific, measurable obligations)
  4. Payment terms (amount, schedule, method)
  5. Mutual releases (scope of claims released)
  6. Confidentiality clause
  7. Non-disparagement clause (optional but common)
  8. Representations and warranties
  9. Breach/default provisions
  10. Governing law and jurisdiction
  11. Signatures and date

Payment Structures:
  Lump sum:        Full payment within 15-30 days
  Installments:    Monthly/quarterly over defined period
  Structured:      Annuity purchased for long-term payments
  Combination:     Initial lump sum + installments

  Key clause: "Time is of the essence" for payment deadlines
  Default clause: if payment missed, full amount accelerates

Enforceability:
  Most jurisdictions: settlement = enforceable contract
  Some states: can be entered as court judgment (if pending case)
  International: Singapore Convention on Mediation (2020)
    Allows cross-border enforcement of mediated settlements
    Similar to New York Convention for arbitration awards

Tax Considerations:
  Physical injury: generally tax-free (IRC §104)
  Emotional distress: taxable unless linked to physical injury
  Lost wages/income: taxable as ordinary income
  Punitive damages: always taxable
  Attorney fees: complex — may be deductible
  Interest: taxable
  1099 reporting: settlement payments >$600 reported
  Allocation: specify what each dollar is for in the agreement

Confidentiality:
  Standard clause: parties agree not to disclose terms
  Exception: may disclose to attorneys, accountants, tax advisors
  Exception: may disclose if required by law/subpoena
  Remedy for breach: liquidated damages clause recommended
  Note: existence of settlement may be public even if terms are not

Common Pitfalls:
  - Vague language ("reasonable" without defining)
  - Missing deadlines for performance
  - No default/breach remedy specified
  - Failing to address all claims (related and unrelated)
  - Not specifying who pays mediator/legal fees
  - Forgetting tax allocation
  - No integration clause (prior agreements superseded)
EOF
}

cmd_ethics() {
    cat << 'EOF'
=== Mediator Ethics ===

Core Ethical Standards (Model Standards of Conduct — ABA/AAA/ACR):

1. Self-Determination:
   Parties make their own decisions
   Mediator cannot impose a solution
   Mediator cannot coerce or unduly influence
   If party seems unable to participate → address or terminate
   Informed consent: parties understand process and options

2. Impartiality:
   No favoritism, bias, or prejudice
   Disclose any potential conflicts of interest
   If bias develops during mediation → withdraw
   Equal time and attention to both parties
   Perception matters — avoid even appearance of bias

3. Conflicts of Interest:
   Prior relationship with any party → disclose
   Financial interest in outcome → disclose
   Former representation of party → disclose
   Ongoing professional relationship → disclose
   When in doubt: disclose. Let parties decide.

4. Confidentiality:
   Everything said in mediation is confidential
   Caucus communications: confidential unless permission given
   Mediator cannot be compelled to testify about mediation
   Exceptions: threats of harm, child abuse, court order
   Document retention: clarify policy in advance

5. Quality of the Process:
   Maintain competence through training and practice
   Only mediate within areas of competence
   Ensure parties understand the process
   Promote honest communication
   End mediation if it becomes inappropriate

6. Fees and Billing:
   Disclose fee structure before mediation
   Reasonable and clearly stated
   Typically split 50/50 between parties
   Contingency fees prohibited (creates outcome bias)
   Pro bono obligation recognized

Ethical Dilemmas:
  Scenario: One party clearly doesn't understand their legal rights
    Response: Suggest they consult an attorney (don't give legal advice)

  Scenario: You suspect fraud in the settlement
    Response: May withdraw; cannot facilitate fraudulent agreement

  Scenario: Party threatens violence
    Response: Terminate immediately, ensure safety, may report

  Scenario: Child custody — child's interests not represented
    Response: Suggest independent representation for the child

Mediator Certification:
  No universal license required (varies by jurisdiction)
  Common training: 40-hour basic mediation course
  Advanced: 100+ hours for family, commercial, etc.
  Court-approved mediator panels: state-specific requirements
  Organizations: ACR, IMI, CEDR, Singapore Mediation Centre
EOF
}

cmd_checklist() {
    cat << 'EOF'
=== Mediation Readiness Checklist ===

Pre-Mediation:
  [ ] Mediator selected and agreed by both parties
  [ ] Mediation agreement reviewed and signed
  [ ] Confidentiality agreement executed
  [ ] Date, time, venue confirmed
  [ ] Separate caucus rooms arranged
  [ ] Position statement prepared and submitted
  [ ] Key documents assembled and organized

Case Analysis:
  [ ] BATNA calculated (best alternative to settlement)
  [ ] WATNA calculated (worst alternative)
  [ ] MLATNA estimated (most likely alternative)
  [ ] Litigation cost estimated (through trial)
  [ ] Timeline to trial estimated
  [ ] Risk assessment completed (probability × impact)

Authority & Team:
  [ ] Decision-maker will attend in person
  [ ] Settlement authority range approved
  [ ] Insurance carrier notified (if applicable)
  [ ] Adjuster with authority attending (if applicable)
  [ ] Expert available by phone (if needed)
  [ ] All necessary parties included

Negotiation Strategy:
  [ ] Opening demand/offer planned
  [ ] Concession strategy mapped (how many rounds, how much per)
  [ ] Package deal options identified
  [ ] Non-monetary creative solutions brainstormed
  [ ] Bottom line defined (with reasoning)
  [ ] Walk-away point determined

Documentation Ready:
  [ ] Contract/agreement in dispute
  [ ] Damages calculation with supporting docs
  [ ] Key emails/correspondence
  [ ] Expert reports
  [ ] Prior offers/demands chronology
  [ ] Settlement agreement template

Day-Of:
  [ ] Arrive early, settle into room
  [ ] Mobile phones silenced
  [ ] Opening statement prepared (3-5 minutes)
  [ ] Focus on interests, not just positions
  [ ] Listen more than talk in joint session
  [ ] Be candid with mediator in caucus
  [ ] Stay until mediator calls the session
EOF
}

show_help() {
    cat << EOF
mediation v$VERSION — Alternative Dispute Resolution Reference

Usage: script.sh <command>

Commands:
  intro        Mediation overview, principles, comparison
  process      Mediation stages from opening to closure
  techniques   Reframing, reality testing, BATNA, bracketing
  types        ADR spectrum: negotiation to arbitration
  preparation  How to prepare for a mediation session
  settlement   Settlement agreement terms and enforceability
  ethics       Mediator ethical standards and dilemmas
  checklist    Mediation readiness checklist
  help         Show this help
  version      Show version

Powered by BytesAgain | bytesagain.com
EOF
}

CMD="${1:-help}"

case "$CMD" in
    intro)       cmd_intro ;;
    process)     cmd_process ;;
    techniques)  cmd_techniques ;;
    types)       cmd_types ;;
    preparation) cmd_preparation ;;
    settlement)  cmd_settlement ;;
    ethics)      cmd_ethics ;;
    checklist)   cmd_checklist ;;
    help|--help|-h) show_help ;;
    version|--version|-v) echo "mediation v$VERSION — Powered by BytesAgain" ;;
    *) echo "Unknown: $CMD"; echo "Run: script.sh help"; exit 1 ;;
esac
