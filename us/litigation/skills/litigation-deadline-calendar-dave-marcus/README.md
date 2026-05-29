# Litigation Deadline Calendar

A plugin for calendaring litigation and arbitration deadlines from scheduling orders.

## What It Does

Upload a scheduling order PDF, and this plugin will:

1. Ask you for the jurisdiction or arbitration forum (it will never assume)
2. Parse the order and extract all key dates
3. Verify that the applicable procedural rules are still current, and provide source URLs so you can check them yourself
4. Compute backward deadlines (last day to serve discovery, expert disclosures, motion response dates, etc.)
5. Generate an .ics calendar file you can import into Outlook

## Supported Jurisdictions & Forums

**Litigation (built-in rules):**
- Colorado (CRCP) — full Rule 6 time computation, discovery, expert, and motion deadlines
- Federal (FRCP) — including the 3-day e-service addition
- Other states — looked up at runtime from official sources

**Arbitration (built-in rules):**
- AAA Commercial Arbitration Rules
- AAA Employment Arbitration Rules
- JAMS Comprehensive Arbitration Rules
- JAMS Streamlined Arbitration Rules

The skill will always ask which jurisdiction or forum applies. It does not default to any jurisdiction.

## Rule Verification & Sources

Each time the skill runs, it searches for recent rule amendments to confirm the built-in rules are still current. It then provides source URLs to the official rule texts so you can independently verify the deadlines. Sources appear both during the verification step and in the final output alongside the computed deadlines.

## Installation

This plugin installs directly into Claude Cowork from GitHub — no coding required.

**Requirements:** Claude Desktop with Cowork access (included with Pro, Team, and Enterprise plans).

**Step 1: Open Claude Desktop and switch to Cowork**

Launch the Claude Desktop app and click the **Cowork** tab.

**Step 2: Open the Customize menu**

Click **Customize** in the left sidebar.

**Step 3: Add this repository as a marketplace**

Click the **+** button, then select **Add marketplace from GitHub**. Enter this repository URL:

```
https://github.com/djmarcuslaw/litigation-deadline-calculator-claude
```

**Step 4: Install the plugin**

Once the marketplace loads, you'll see the **Litigation Deadline Calendar** plugin listed. Click **Install**.

That's it. The plugin activates automatically — no further setup needed.

## How to Use

Say something like:
- "Calendar the deadlines from this scheduling order"
- "I need to set up deadline tracking for a new case"
- "Parse this scheduling order and give me an .ics file"

The skill will walk you through providing the matter name, jurisdiction/forum, and any attendees to invite.

## Calendar Entry Format

All entries follow the format: **[Matter Name] — [Deadline Description]**

Example: "Smith v. Jones Co. — Last Day to Serve Interrogatories"

## Reminders

Each calendar entry includes automatic reminders at 7 days and 1 day before each deadline.

## Important Disclaimer

These deadlines are computed from the scheduling order and applicable rules. They should be independently verified by counsel. Local rules, judge-specific practices, and amended scheduling orders may affect actual deadlines. This tool is for reference purposes and does not constitute legal advice.

## License

MIT © Dave Marcus 2026

**Non-commercial preferred**: Free for personal, academic, and open-source use. Please don't sell this skill or include it in paid products—link back instead!
