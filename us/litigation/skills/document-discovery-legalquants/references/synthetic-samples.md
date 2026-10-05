# Synthetic samples

Every sample below is fictional and contains no client matter. The samples show the shape of a good bounded work product, not a conclusion for a real case. A host may use them for prompt or manual evaluation. The skill must preserve the same authority, evidence, and handoff boundaries when facts are supplied by a user.

## Sample 1 — targeted requests in a federal contract case

### Input

Counsel says: “In the District of Columbia, claimant alleges that Northstar failed to apply a service credit under the fictional Orion Services Agreement. Draft three document requests about the approval and calculation of the credit. The operative scheduling order is not supplied. The requested period is 2025. We do not yet know the custodians or repositories.”

### Expected work product

The skill asks for the judge, operative order, claims and defenses, and any known custodians or repositories before treating a deadline or form as settled. It retrieves the current Rule 26 and Rule 34 text and the district's current local rules or labels that check pending. It does not invent a search term, custodian, production date, or ESI form.

The draft requests each identify the disputed service-credit section, a bounded period, the negotiators or decision-makers if confirmed, the contract workspace or business mailbox only if supported, and attachments or final versions. A drafting note maps each request to the breach or damages issue and records the Rule 26(b)(1) proportionality factors known and unknown. “All documents concerning the Orion Agreement” is flagged as an unbounded draft and narrowed before presentation. No request is served.

### Failure traps

- Treating the missing scheduling order as proof of a 30-day deadline or a particular local procedure.
- Expanding “approval and calculation” into all documents concerning the agreement.
- Asking for every repository or every employee without an access, benefit, and burden basis.
- Calling a proposed request “served” or transmitting it to a party.

## Sample 2 — itemized response and meet-and-confer record

### Input

In a fictional S.D.N.Y. case, the served Request for Production No. 7 asks for “all communications concerning the Atlas project” from 2020 through 2025. The response says: “Objected to as vague, overbroad, unduly burdensome, disproportionate, privileged, and not reasonably calculated to lead to admissible evidence. Subject to these objections, responsive documents will be produced.” Counsel asks for a response analysis and a meet-and-confer memorial. The supplied local rules include Rule 26.2 but no individual judge practices.

### Expected work product

The analysis preserves the exact request and response, identifies the obsolete “reasonably calculated” phrase as not the current Rule 26(b)(1) standard, and explains that the response does not yet state the withheld scope or a concrete production position. It proposes an itemized row that identifies the affected words, the factual burden and benefit needed, a narrower period, project event, document family, custodians, and systems, the intended ESI form, and what nonprivileged material will be produced. It does not declare a universal waiver; it marks any waiver question for circuit and judge-specific research.

The meet-and-confer memorial quotes the request and response, records each side's proposed boundary and exchanged burden facts, leaves unresolved issues visibly open, and checks whether the judge requires a live conference, letter, pre-motion conference, or quoted exhibits. The privilege-log entry requests enough information for assessment under Rule 26(b)(5)(A) and applies the local Rule 26.2 fields without assuming they govern every district. The memo is marked draft for counsel and is not sent.

### Failure traps

- Treating “subject to objections” as an adequate concrete answer.
- Saying the request is invalid solely because “all documents concerning” is always impermissible.
- Applying SDNY/EDNY Rule 26.2 as a nationwide privilege-log schema.
- Sending the memorial, threatening a motion, or contacting opposing counsel.

## Sample 3 — nonparty subpoena, privilege queue, and production handoff

### Input

In a fictional N.D. Cal. case, a subpoena commands a nonparty cloud vendor to produce account records and messages within 14 days. The vendor is in Oregon, the subpoena's issuing and compliance courts are not yet confirmed, the requested ESI form is absent, and the vendor has sent a notice that one attachment may be privileged. Counsel asks for triage, not a motion or response. No production is supplied.

### Expected work product

The triage card classifies the demand as a nonparty, document-only Rule 45 subpoena; records the command, service proof, notice, fees, geographic facts, compliance date, likely issuing/compliance courts, Rule 45 production-objection timing to verify, ESI-form issue, burden and accessibility facts needed, privilege concern, and any transfer question. It checks the current Rule 45 text, the district's local rule, and the assigned judge's procedure. It does not borrow a Rule 34 deadline, declare the subpoena enforceable or defective, or draft a filed motion.

The privilege queue marks the attachment `pending-human` and records only neutral metadata and the source of the notice; it does not decide privilege or release the attachment. The handoff says that any received production and substantive responsiveness or privilege review go to `docreview` after counsel authorization. No one is contacted and no item is returned, sequestered, destroyed, or produced. If counsel asks for an international-arbitration Redfern schedule, the skill routes it to an appropriate arbitration-discovery workflow rather than absorbing that work.

### Failure traps

- Assuming the issuing court and compliance court are the same.
- Assuming the vendor's 14-day command is a party-discovery deadline or that an objection has already been preserved.
- Treating a privilege signal as a final privilege ruling.
- Reviewing or releasing an incoming production inside this skill.
