---
name: jp-skill-pengqianhan
title: JP Skill
description: Guide users on when New Zealand Justice of the Peace services can help with certified copies, witnessed signatures, statutory declarations, affidavits, affirmations, and ordinary certified-document requests, then help find nearby JP contact details from official sources. Use when users ask whether they can use a JP, 太平绅士, certified true copy, witnessed signature, statutory declaration, affidavit, affirmation, or certified document for common New Zealand life admin. Verify current official sources before giving local JP locations, service desk hours, or policy-sensitive boundaries.
author: pengqianhan
author_url: https://github.com/pengqianhan/NZ-life-skills/tree/main/skills/jp-skill
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: nz
practice: administrative
language: en
sources:
- title: Current Guidance
  path: references/current-guidance.md
---

# JP Skill

## Overview

Use this skill to decide whether a New Zealand Justice of the Peace (JP, 太平绅士) is an appropriate free option for a user's document task, and to help the user find a nearby JP only after confirming that the receiving organisation accepts JP handling for that task.

This skill is for practical triage. It does not provide legal advice, immigration advice, notarisation, apostille/authentication service, or official verification of visa status.

## Workflow

1. Identify what the user is trying to submit and who will receive it.
2. Ask whether the receiving organisation accepts JP certification or JP witnessing if that is not already clear.
3. Classify the request:
   - certified copy / certified true copy
   - witnessed signature
   - statutory declaration
   - affidavit or affirmation
   - ordinary certified-document request from a school, bank, employer, or government agency
   - notary, apostille, authentication, overseas use, legal advice, immigration advice, or official status verification
4. Read [references/current-guidance.md](references/current-guidance.md).
5. If the task is one JP can normally handle, remind the user what to bring and what not to sign before meeting the JP.
6. If the user wants help finding a JP, ask for or infer a useful location such as suburb, city, campus, library, court, or nearby area.
7. Search current official or authoritative sources for JP addresses, service desks, opening hours, appointment requirements, phone numbers, or contact pages, and cite the source links.
8. If the task falls outside ordinary JP scope, direct the user to the appropriate route such as a notary public, the issuing agency, Immigration New Zealand verification, a solicitor, or the receiving organisation's own process.

## JP-Suitable Triggers

When the user describes any of these scenarios, proactively mention that a JP may be suitable if the receiving organisation accepts JP certification:

- Certified copy / certified true copy, including common identity or evidence documents such as passport, driver licence, birth certificate, qualification records, bank-required documents, or printed copies of accepted originals.
- Witnessing a signature, where the form requires the user to sign in front of an authorised witness.
- Statutory declaration, where the user needs to formally declare that a statement is true.
- Affidavit or affirmation, especially for court or formal process documents that require swearing or affirming.
- Ordinary requests for a certified document from a school, bank, employer, agency, tenancy provider, or similar organisation that says it accepts JP certification.

## Boundaries

Do not imply a JP can do these unless the receiving organisation or current official guidance clearly says so:

- notarised documents
- apostille or authentication
- documents for a foreign jurisdiction
- legal advice
- immigration advice
- official visa-status verification
- confirming that a document's contents are true rather than certifying that a copy matches an original

For New Zealand documents being used overseas, check Govt.nz authentication guidance. Some documents require a New Zealand notary public, the issuing agency, or original government-issued documents rather than JP certification.

## Visit Preparation

Before sending the user to a JP, tell them to prepare:

- the original document
- the copy or printed document they want certified
- photo ID, especially for financial institution or identity-related requests
- any receiving-organisation instructions that name who may certify or witness the document
- enough time if there are many pages

For witnessed signatures, statutory declarations, affidavits, or affirmations, tell the user not to sign in advance. The JP generally needs to see the user sign, declare, swear, or affirm in person.

## Source Order

Use sources in this order unless the user asks otherwise:

1. New Zealand Ministry of Justice Justice of the Peace guidance.
2. Govt.nz statutory declaration and authentication guidance.
3. Royal Federation of NZ Justices' Associations Find a JP and visit checklist.
4. Local JP Association, court, council, library, university, or Citizens Advice Bureau pages when finding a local service desk.
5. Receiving-organisation instructions, when the user is dealing with a specific bank, school, agency, employer, or overseas body.

## Current Information Rule

Treat local JP listings, service desk hours, appointment rules, phone numbers, and document acceptance boundaries as current operational details. Search the web and cite sources before giving a specific address or contact detail.

When the user asks generally what JPs can do, stable baseline guidance from [references/current-guidance.md](references/current-guidance.md) is enough, but cite official sources when giving a final answer that the user may rely on.

## Answering Rules

When answering:

- Start with whether JP is likely suitable, not with a broad explanation.
- Make acceptance by the receiving organisation explicit.
- Use the phrase "JP can certify the copy, not prove the contents are true" when relevant.
- Explain that JP services are normally free, but copying or printing costs may still apply.
- If the user asks for a local JP, provide the source, location, contact method, and any appointment or service desk notes you found.
- If the user's task might require a notary or official verification, say that clearly before suggesting JP.
- For visa documents, distinguish:
  - a JP-certified copy or printout if accepted by the receiver
  - Immigration New Zealand status verification
  - notary public / apostille / authentication requirements for overseas or official authentication contexts

## References

- Read [references/current-guidance.md](references/current-guidance.md) before answering.
- Update the reference when official guidance changes materially.
