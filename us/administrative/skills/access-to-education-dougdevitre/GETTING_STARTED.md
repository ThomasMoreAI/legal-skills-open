# Getting Started

This guide walks you through setting up **Access to Education** as your personal Missouri K-12 assistant. No coding required.

```mermaid
flowchart LR
    A[Choose Setup Method] --> B[Option A: Claude Code]
    A --> C[Option B: Claude Project]
    A --> D[Option C: Share with Team]
    B --> B1[Install Claude Code] --> B2[Clone Repo] --> B3[Run 'claude']
    C --> C1[Create Account] --> C2[New Project] --> C3[Paste SKILL.md] --> C4[Upload References]
    D --> D1[Set Up Project] --> D2[Share Link]
    B3 --> E[Ask Questions / Use Commands]
    C4 --> E
    D2 --> E
```

---

## Option A: Claude Code (fastest)

Claude Code is a command-line tool that reads this repository automatically.

### Step 1: Install Claude Code

Visit [claude.ai/code](https://claude.ai/code) and follow the install instructions for your platform (Mac, Windows, or Linux).

### Step 2: Clone the repository

Open your terminal and run:

```bash
git clone https://github.com/dougdevitre/access-to-education.git
cd access-to-education
```

### Step 3: Start Claude Code

```bash
claude
```

That's it. Claude reads the `CLAUDE.md` file automatically and becomes your Missouri K-12 navigator. Start asking questions:

```
> What are the graduation requirements in Missouri?
> My child was suspended. What are our rights?
> /retire (I'm 54 with 27 years of service)
> Mi hijo necesita una evaluacion especial. Que hago?
```

---

## Option B: Claude Project (no install needed)

A Claude Project lets you use this in your browser at claude.ai.

### Step 1: Create a Claude account

Go to [claude.ai](https://claude.ai) and sign up or log in.

### Step 2: Create a new Project

1. Click **Projects** in the left sidebar
2. Click **Create Project**
3. Give it a name like "Access to Education"

### Step 3: Set the custom instructions

1. In your project, click **Project Instructions**
2. Open the file `SKILL.md` from this repository (you can [view it on GitHub](https://github.com/dougdevitre/access-to-education/blob/main/SKILL.md))
3. Copy the entire contents and paste it into the instructions box
4. Click Save

### Step 4: Upload reference files

1. Click **Project Knowledge** then **Add Content**
2. Upload these folders from the repository:
   - Everything in `references/` (all subfolders)
   - Everything in `templates/`
   - Everything in `scripts/`
   - Everything in `examples/`
3. You can download the files from GitHub by clicking the green **Code** button > **Download ZIP**

### Step 5: Start chatting

Open a new conversation in your project and ask any Missouri education question. The system will detect your role and respond accordingly.

---

## Option C: Share with your team

### For your school or district

1. Set up a Claude Project (Option B above)
2. Click **Share** on the project
3. Share the link with colleagues -- they'll get the same navigator with all the reference files

### For a department or PLC

Each team can set up their own project. The skill adapts to whoever is asking:
- **Counselors** get graduation audits, college planning checklists, crisis screening tools
- **Specialists** get IEP compliance checks, evaluation timelines, 504 plan templates
- **Administrators** get CSIP builders, compliance calendars, policy drafting tools
- **Teachers** get lesson plan frameworks, PD growth plans, standards references
- **Parents** get rights explanations, letter templates, decision tree walkthroughs

---

## What you can do

### Ask questions in plain language

No special syntax needed. Just ask like you'd ask a colleague:

- "How many credits does my kid need to graduate?"
- "A parent just requested a special ed evaluation. What's my timeline?"
- "We're building our CSIP. Where do I start?"
- "What are the MSHSAA eligibility requirements?"

### Use slash commands for common workflows

| Command | What it does |
|---------|-------------|
| `/start` | Introduction -- tells you what the skill can do for your role |
| `/rights` | Look up parent rights by topic |
| `/letter evaluation-request` | Generate a letter requesting a special education evaluation |
| `/graduation` | Walk through a graduation credit audit |
| `/iep-check` | Review an IEP for compliance |
| `/crisis active-threat` | Get immediate crisis response steps |
| `/comply march` | See what compliance deadlines are due in March |
| `/retire` | Calculate PSRS retirement eligibility |
| `/translate` | Translate content to Spanish |

See `commands/COMMANDS.md` for all 22 commands.

### Generate documents

Ask the skill to create letters, plans, or forms:

- "Write a letter to request my child's school records"
- "Help me build our school safety plan"
- "Draft an AI acceptable use policy for our district"
- "Create a behavior intervention plan"

### Ask in Spanish

The skill responds in Spanish when you write in Spanish. English legal terms are preserved in parentheses so you can use them with the school.

---

## Tips

- **You don't need to say your role every time.** The skill detects it from context. But if answers seem off, say something like "I'm a parent" or "I'm a special ed coordinator."
- **Follow-up questions work.** The skill remembers context within a conversation. After asking about suspension, you can say "he has a 504 plan" and it will adjust.
- **Ask for documents.** If you need a letter, plan, or form, ask for it -- the skill will generate one, not just describe what it should contain.
- **Check the source.** The skill cites Missouri statutes (RSMo), IDEA sections, and DESE guidance. If something seems wrong, check the citation.
- **It's not a lawyer.** The skill gives educational information, not legal advice. For legal strategy, consult an attorney.

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Claude doesn't seem to know about Missouri education | Make sure `SKILL.md` is loaded as custom instructions (Option B) or that you're in the repo directory (Option A) |
| Answers are too generic | Try stating your role: "As a special ed coordinator, ..." |
| A fact seems wrong | Check `LAST_VERIFIED.md` for when that data was last verified. File an issue on GitHub if it's outdated |
| Need a topic not covered | File a "New Topic Request" issue on GitHub |
| Spanish responses are inconsistent | Start your message in Spanish, or say "responde en espanol" |
