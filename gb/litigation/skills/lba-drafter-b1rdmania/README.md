# lba-drafter

Drafts a Letter Before Action for an England & Wales employment dispute — Employment Tribunal claims (unfair dismissal, discrimination, unlawful deduction) and civil contractual claims (wrongful dismissal, breach of contract) — for a solicitor to review, complete, sign and serve.

## Install

Part of the [claude-for-uk-legal](https://github.com/b1rdmania/claude-for-uk-legal) plugin suite:

```bash
/plugin marketplace add https://github.com/b1rdmania/claude-for-uk-legal
/plugin install uk-employment-legal@claude-for-uk-legal
```

Or install the single skill directly:

```bash
cp -r lba-drafter ~/.claude/skills/lba-drafter
```

## Usage

```
/lba-drafter [claim-type] [--respondent=name]
/lba-drafter unfair-dismissal --respondent="Acme Logistics Ltd"
```

Run it against a matter with the claimant and respondent details, a dated chronology, the heads of claim, and the remedy sought. It returns the finished letter with every unknown value, figure, citation and the limitation date marked for the solicitor to confirm.

## What it does

- Confirms jurisdiction (England & Wales only) and the forum — Employment Tribunal or civil court — and applies the right pre-action framework (ACAS Code for ET claims, Pre-Action Conduct PD for civil claims).
- Surfaces the limitation position — the three-month ET primary limit, ACAS early conciliation stop-the-clock under s.207B ERA 1996, and the inputs needed to calculate the deadline.
- Pleads each head of claim against its statutory or contractual basis, applying the facts to the elements.
- Renders the finished letter — background facts, causes of action, loss and remedy, ACAS Code, costs — ready for solicitor review.
- Marks every uncertain point inline: `[SOLICITOR: confirm X]`, `[TIME LIMIT — confirm ET1 deadline before sending]`, `[SME VERIFY]`, `[CITE NEEDED]`, `[FACT NEEDED]`.

## What it doesn't do

- Give legal advice or substitute for independent legal advice for the claimant.
- Compute or assert a limitation date — date miscalculation is the top employment-litigation malpractice, so the solicitor calculates and confirms it before sending.
- Verify case law — every authority is cited from memory and must be checked against a live source.
- Verify current statutory figures (compensatory cap, week's pay, Vento bands), which change annually.
- Send the letter — the solicitor reviews, completes, signs and serves.
- Advise on without-prejudice settlement strategy — that is the `without-prejudice-drafter` skill.
- Cover Scotland or Northern Ireland.

## Requirements

- Claude Code or Claude Cowork. No MCP connectors required.
- A matter to run against (claimant and respondent details, a dated chronology, heads of claim, remedy sought).

## License

Apache-2.0.
