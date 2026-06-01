---
name: er
title: AI4L - Main Skill for Evidence Review Creation and Auditing using @AGENTS
description: AI4L - Main Skill for Evidence Review Creation and Auditing using @AGENTS
author: forever-healthy
author_url: https://github.com/forever-healthy/AI4L/tree/main/.claude/skills/er
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# AI4L - Main Skill for Evidence Review Creation and Auditing using @AGENTS

## General Rules

* Parse the user's input to determine which sub-command to execute
* Set [args] to $ARGUMENTS

* Note the [start_time] when beginning any command, and report the [time_taken] when done

* All generated results go in [creation_dir] as .md files
* Do not edit or modify any files outside [creation_dir]


* Full lines formatted as `line` comments must be ignored when processing commands.


## COMMAND: create {topic}

`Create an evidence review (ER) using the @er-creator agent.`

* If no [args] are given {
  * Report: `usage: /er create {topic}`
  * exit
} otherwise {
  set [topic] to [args]
}

* Report: `create: [topic]`

* @er-creator: `[topic]`
* Wait until the agent finishes

* Report: `filename: [filename]`


## COMMAND: audit {er}

`Audit an ER using the @er-auditor agent.`

* If no [args] are given {
  * Set [target_er] to the newest ER in [creation_dir]
} else {
  * Set [target_er] to [args]
}

* Report: `audit: [target_er]`

* @er-auditor: `[target_er]`
* Wait until the agent finishes and returns the result

* Report: `target_er: [target_er]`
* Report: `pass_rate: [pass_rate]`


## COMMAND: fix {er}

`Audit and fix an ER using the @er-fixer agent.`

* If no [args] are given {
  * Set [target_er] to the newest ER in [creation_dir]
} else {
  * Set [target_er] to [args]
}

* Report: `fix: [target_er]`

* @er-fixer: `[target_er]`
* Wait until the agent finishes and returns the result

* Report: `target_er: [target_er]`
* Report: `pass_rate: [pass_rate]`


## COMMAND: combine {er}

`Create a final QA file from all audits`

* If no [args] are given {
  * Set [target_er] to the newest ER in [creation_dir]
} else {
  * Set [target_er] to [args]
}

* Report: `combine: [target_er]`

* @er-combiner: `[target_er]`
* Wait until the agent finishes and returns the result

* Report `QA file: [new_qa_filename]`

## COMMAND: iterate {er}

`Loops audit/fix cycles up to [max_audits] times until [needed_passes] show 100% pass rate.`

* If no [args] are given {
  * Set [target_er] to the newest ER in [creation_dir]
} else {
  * Set [target_er] to [args]
}

* Report: `iterate: [target_er]`

Initialize {
  * Set [iteration] = 0, [consecutive_passes] = 0
}

Loop while [iteration] < [max_audits] and [consecutive_passes] < [needed_passes]
{
  * @er-fixer: `[target_er]`
  * Wait until the agent finishes and returns the result

  * If the [pass_rate] is 100%, increment [consecutive_passes]; otherwise reset to 0
  * Increment [iteration]

  * Report: "Iteration [iteration]: Pass rate = [pass_rate]% ([consecutive_passes]/[needed_passes] consecutive passes needed)"
}

* @er-combiner: `[target_er]`

If [iteration] < [max_audits] {
  * Return: `status: success`
} else {
  * Return: `status: failed`
}

* Return: `target_er:  [target_er]`
* Return: `iterations: [iteration]`


## COMMAND: full {er}

`A create and multi-pass audit workflow.`

* Execute the "create" command
* Execute the "iterate" command

## COMMAND: compare {intervention}

`Compares all ERs for a given intervention, typically from different AI models or versions, to determine which is strongest based on content quality and the latest QA audit results.`

* If no [args] are given {
  * Set [intervention] to intervention in the frontmatter of the newest ER in [creation_dir]
} else {
  * Set [intervention] to [args]
}

* Report: `compare: [intervention]`

* Compare all ERs in [creation_dir] with a similar [intervention] in their frontmatter
  * Compare the quality of the content
  * Be detailed
  * Take into account the latest "QA.md" for each.

* Present a clear recommendation of which ER is strongest and why.
