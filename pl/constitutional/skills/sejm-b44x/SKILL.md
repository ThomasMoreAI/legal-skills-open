---
name: sejm-b44x
title: Sejm Rzeczypospolitej Polskiej
description: 'Official parliamentary data of the Sejm RP (Polish lower house) from the open API (api.sejm.gov.pl). Database of MPs of the 10th term (X kadencja) (electoral districts, parliamentary clubs, Sejm committees, contact details), detailed voting results (roll-call votes, breakdown of votes by club: for/against/abstained/absent, checking how a given MP voted), the database of druki sejmowe (Sejm prints) and the course of the legislative process (stages of work on bills and resolutions), as well as interpelacje poselskie (MPs'' interpellations) and ministries'' replies. No API keys, 100% official public data. Use whenever the user asks about: "posłowie na Sejm", "kto jest posłem z okręgu X", "jak głosowano w Sejmie nad ustawą Y", "jak głosował poseł Kowalski", "na jakim etapie jest projekt ustawy", "druki sejmowe", "interpelacje poselskie".'
author: b44x
author_url: https://github.com/b44x/ai-polish-skills/tree/dev/skills/sejm
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: pl
practice: constitutional
language: en
tags: [sejm, poslowie, glosowania, druki, proces-legislacyjny, ustawy, interpelacje, prawo, parlament]
sources:
- title: Output
  path: references/output.md
---

# Sejm Rzeczypospolitej Polskiej

Official skill integrating the open Sejm RP API via `scripts/sejm.py`.
Gives AI agents neutral access to official data on MPs, votings,
druki sejmowe (Sejm prints), the legislative process and interpelacje (interpellations). Returns clean JSON on `stdout`.

## Running

Run from the skill directory (or from the repository root path):

| Operating system | Command |
|---|---|
| Linux / macOS | `python3 scripts/sejm.py <command> …` |
| Windows | `py scripts/sejm.py <command> …` (or `python`) |

Zero external libraries (Python 3.8+ standard library).

## Main Use Cases

1. **MPs and committees database:**
   - Searching for MPs from a given electoral district or by surname:
     `python3 scripts/sejm.py mps --district "Gdańsk"`
     `python3 scripts/sejm.py mps --search "Kowalski"`
     `python3 scripts/sejm.py mps --club "PiS"`
   - Checking an MP's details and the committees they sit on:
     `python3 scripts/sejm.py mps --id 133`

2. **Votings and checking a specific MP's vote:**
   - Checking voting results and the breakdown of votes by club (for, against, abstained):
     `python3 scripts/sejm.py voting 1 2`
   - Checking how a specific MP voted in a given voting:
     `python3 scripts/sejm.py voting 1 2 --mp "Hołownia"`
   - Overview of voting topics at the latest posiedzenie (sitting):
     `python3 scripts/sejm.py votings`
     `python3 scripts/sejm.py votings --sitting 1 --search "Wicemarszałków"`

3. **Druki sejmowe and the legislative process:**
   - Looking up a druk sejmowy (Sejm print) by number:
     `python3 scripts/sejm.py prints --number 1`
   - Searching prints by topic:
     `python3 scripts/sejm.py prints --search "podatku"`
   - Checking the stages of work on a bill (whether it was submitted, 1st/2nd/3rd reading, whether it was passed):
     `python3 scripts/sejm.py process 1`

4. **Interpelacje poselskie (MPs' interpellations):**
   - Searching interpellations by topic or by number:
     `python3 scripts/sejm.py interpellations --search "CPK"`
     `python3 scripts/sejm.py interpellations --number 1`

## Commands

| Command | Description | Returned data |
|---|---|---|
| `mps [--search S] [--club C] [--district D]` | List and search MPs | `id`, `firstLastName`, `club`, `districtName`, `email`, `profession` |
| `mps --id <id>` | Full MP details and Sejm committees | `birthDate`, `profession`, `committees` (with the role held) |
| `voting <sitting> <number> [--mp MP]` | Voting details and an MP's vote | `results`, `clubSummary` (votes by club), `mpVote` |
| `votings [--sitting S] [--search Q]` | List of votings at a sitting | `votingNumber`, `date`, `title`, `topic`, `yes`, `no`, `abstain` |
| `prints [--number N] [--search Q]` | Search druki sejmowe | `number`, `title`, `documentDate`, `attachments` |
| `process <print_number>` | Stages of a bill's legislative process | `documentType`, `passed`, `closureDate`, chronological `stages` |
| `interpellations [--number N] [--search Q]` | Interpellations and replies | `number`, `title`, `sentDate`, `fromMpIds`, `replies` |
| `terms` | List of Sejm terms (kadencje I–X) | `terms` (dates, number, `current` flag) |

Detailed description of JSON schemas: [references/output.md](references/output.md).

## Neutrality Rules

- This tool provides objective parliamentary data, not political opinions.
- Do not make evaluations, moral rankings or political interpretations of MPs' behavior.
- Every response should clearly state:
  * Source: **Sejm Rzeczypospolitej Polskiej** (`api.sejm.gov.pl`),
  * Term number (kadencja; default **X kadencja**),
  * Sitting (posiedzenie) number and voting or print number,
  * Date of the event.

## Exit Codes

Clean JSON goes to `stdout`; errors go to `stderr` as `{"error": "...", "type": "..."}`.

| Code | Meaning | Action |
|---|---|---|
| `0` | Success | Process the JSON data |
| `2` | Not found | MP, voting, print or process does not exist |
| `64` | Invalid invocation / validation | Check the command parameters |
| `69` | Sejm RP server / network error | Temporary API problem; try again |
