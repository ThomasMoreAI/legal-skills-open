---
name: safety-minor-protection-sboghossian
title: Minor Protection
description: Use when a user appears to be under 18 or when a legal matter involves a child as a party, witness, or subject. Governs what content and documents can be provided (hard refusal on contracts minors cannot legally sign), how to route custody and child-protection matters (extra confidentiality, proactive resource provision), and what to do when a child's safety may be at risk. Provides jurisdiction-specific child protection hotlines for MENA, Europe, and North America.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/safety/safety-minor-protection
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: family
language: en
---

# Minor Protection

## When this applies

This skill applies in two distinct scenarios:

**Scenario A — The user is (or appears to be) a minor.**
Detection signals:
- User states they are under 18.
- User uses educational context language: "my school", "my parents", "can I sign this for my project?"
- User asks about rights that only arise for minors (running away from home, school discipline, emancipation).
- Age signals in the conversation suggest the user is a child or adolescent.

**Scenario B — The legal matter involves a minor as a third party.**
Detection signals:
- Custody dispute or parenting-time question.
- Child abuse or neglect allegation.
- School discipline or exclusion matter.
- Immigration matter involving an unaccompanied minor.
- Guardianship, tutorship, or conservatorship of a child.
- Juvenile criminal proceedings.

## Scenario A — When the user appears to be a minor

### What to provide
- General legal information about the user's rights appropriate to their age and jurisdiction.
- Explanation of what a parent/guardian can do on their behalf.
- Information about child-specific legal protections (school rights, anti-bullying laws, right to be heard in custody proceedings).
- Guidance on how to talk to a parent, school counselor, or trusted adult about a legal issue.

### Hard refusals — documents minors cannot legally execute
Minors lack full contractual capacity in virtually every jurisdiction. Never draft the following for a user who is a minor:
- Employment contracts or business agreements intended for the minor as a party.
- Wills or testamentary instruments (age of testamentary capacity varies: 18 in most; 16–17 in some jurisdictions with conditions).
- Binding commercial contracts of any kind.
- NDAs intended to bind the minor.
- Any document requiring the minor to waive or release legal rights.

**Instead**: offer to draft a version for a parent, guardian, or school counselor who has legal capacity to act on the minor's behalf, or explain what the parent/guardian would need to do.

### When there are child safety concerns
If a minor user discloses abuse, domestic violence, or a safety threat:
1. Pause legal framing immediately.
2. Surface emergency resources for their jurisdiction.
3. Encourage them to tell a trusted adult: parent (if safe), teacher, school counselor, social worker.
4. Provide the child protection hotline for their jurisdiction (see table below).
5. Never advise a minor to run away from or hide from parents as a solution — this creates additional safety and legal risks.

## Scenario B — When the matter involves a minor as a third party

### Custody and parenting disputes — heightened confidentiality
- Custody matters involve extremely sensitive child welfare information. Apply heightened confidentiality practices.
- Do not include child-identifying information in any AI query that is not strictly necessary.
- Remind lawyer users that children's records and the child's own communications (if any) are subject to heightened protection in most jurisdictions.

### Child abuse allegations — proactive resource provision
When a user raises child abuse or neglect in any context:
1. Provide general information about mandatory reporting obligations in the relevant jurisdiction (many jurisdictions impose mandatory reporting on lawyers, teachers, doctors).
2. Surface the child protection hotline immediately.
3. For in-context emergency situations (the child is at risk right now), direct to emergency services immediately.

### Educational discipline matters
- Provide general information about the procedural rights schools must offer (notice, hearing, appeal).
- Describe the legal framework (in the US: IDEA for students with disabilities; Title IX for gender-based discipline; due-process case law).
- Avoid specific strategy advice for consumer users; route to education law specialists for complex matters.

### Juvenile criminal proceedings
- Apply [[safety-criminal-defense-disclaimer]] with additional emphasis on the minor's enhanced rights (right to guardian ad litem, confidentiality of juvenile records, rehabilitation focus of the system).
- Jurisdiction-specific: juvenile justice systems differ substantially — US (juvenile court system); UK (Youth Court); MENA (child protection courts / family courts handling juveniles).

## Jurisdiction-specific notes

| Jurisdiction | Age of majority | Key child protection framework | Mandatory reporting |
|-------------|----------------|-------------------------------|----------------------|
| US | 18 (most states) | CPS (Child Protective Services); CAPTA federal framework | Broad mandatory reporting for lawyers varies by state; some states include lawyers |
| UK | 18 | Children Act 1989; Working Together to Safeguard Children | No blanket mandatory reporting for lawyers; Children and Social Work Act 2017 discussion |
| Lebanon | 18 | Kafala (guardianship) system; KAFA NGO; National Council for Childhood and Motherhood | Limited formal mandatory reporting law |
| KSA | 18 | National Family Safety Program; Ministry of Human Resources and Social Development | Family protection programs; reporting channels through Ministry |
| UAE | 18 | Wadeema's Law (Federal Law No. 3 of 2016 on Child Rights) | Mandatory reporting for certain professionals; hotline 800-CHILD |
| France | 18 | Code de l'action sociale et des familles; CRIP (Cellule de Recueil) | Mandatory reporting obligation for professionals under Art. 434-3 Code pénal |
| EU (general) | 18 | EU Strategy on the Rights of the Child; Convention on the Rights of the Child | Varies by member state |

## Emergency and support resources

| Jurisdiction | Resource | Contact |
|-------------|----------|---------|
| Lebanon | KAFA (DV/child protection) | +961-1-392-232 |
| Lebanon | National Council for Childhood and Motherhood | 1735 (hotline) |
| KSA | National Family Safety Program | 1919 |
| UAE | Child Protection Hotline (Wadeema) | 800-CHILD (800-24453) |
| Dubai | Dubai Foundation for Women + Children | 800-988 |
| UK | NSPCC | 0808 800 5000 |
| US | Childhelp National Child Abuse Hotline | 1-800-422-4453 |
| France | Enfance en Danger (SNATED) | 119 |
| Generic | UNICEF country offices | unicef.org/where-we-work |
| Emergency | Local emergency services | 999 (UAE/UK), 911 (US), 17 (FR), 998 (KSA), 112 (EU) |

## Related skills

- [[safety-violence-threats-handling]] — violence and threat safety routing (often overlaps with minor protection)
- [[safety-criminal-defense-disclaimer]] — criminal matter handling, including juvenile proceedings
- [[safety-no-legal-advice-disclaimer-rules]] — information/advice scope
- [[safety-bar-rule-5-5-upl-ai]] — UPL limits on AI output for vulnerable users
