---
name: lawyer-inc-architecture
title: Lawyer Incorporated — System Architecture Map
description: Complete architecture map of the Lawyer Incorporated AI paralegal stack. Five systems, how they interact, what they do, where they live, and how to operate each one. Load this skill whenever working on ANY part of the stack.
author: Whaleylaw
author_url: https://github.com/Whaleylaw/Roscoe-hermes/tree/main/roscoe-state/skills/domain/lawyer-inc-architecture
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: personal-injury
language: en
tags: [lawyer-inc, architecture, hermes, openclaw, gsd, mission-control, firmvault]
---

# Lawyer Incorporated — System Architecture Map

## The Thesis

"The firm as a code repo." Law firm work is repeatable tasks + templates + rules.
Put it into primitives AI agents already excel at (issues, commits, PRs, diffs)
and you get a paralegal system that actually works.

Aaron Whaley is the sole human. Everything else is automated with human-in-the-loop
approval gates at critical points.

---

## The Five Systems

```
┌─────────────────────────────────────────────────────────────────────┐
│                        AARON (Telegram)                             │
│                     Human-in-the-loop owner                         │
└──────────────────────────────┬──────────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────────────┐
│  1. HERMES ("Roscoe")  —  THE ORCHESTRATOR                          │
│     Railway  |  github.com/Whaleylaw/Roscoe-hermes                  │
│                                                                      │
│  Telegram bot + daemon thread. The brain that coordinates everything.│
│  Talks to Aaron. Decides what needs doing. Dispatches to agents.     │
│  Collects results. Routes approvals.                                 │
│                                                                      │
│  ┌─────────────┐  ┌──────────────┐  ┌────────────────────────┐     │
│  │ Gateway     │  │ Daemon       │  │ GSD Bridge             │     │
│  │ (Telegram)  │  │ (heartbeat)  │  │ (Node.js subprocess)   │     │
│  └─────────────┘  └──────┬───────┘  └────────────┬───────────┘     │
│                          │                        │                  │
└──────────────────────────┼────────────────────────┼──────────────────┘
                           │                        │
              ┌────────────┼────────────────────────┼──────────┐
              │            │                        │          │
              ▼            ▼                        ▼          ▼
┌──────────────────┐ ┌──────────────┐ ┌─────────────────┐ ┌──────────────┐
│ 2. GSD           │ │ 3. MISSION   │ │ 4. OPENCLAW     │ │ 5. FIRMVAULT │
│                  │ │    CONTROL   │ │                 │ │              │
│ Project Mgmt     │ │ Dashboard    │ │ Worker Agents   │ │ Case Vault   │
│ Plan Lifecycle   │ │ Agent Fleet  │ │ 7 Specialists   │ │ Workflows    │
│ Task Dispatch    │ │ Task Queue   │ │ on Render       │ │ Skills+Tools │
│                  │ │ Approvals    │ │                 │ │              │
│ gsd-lawyerinc   │ │ Roscoe-MC    │ │ Roscoebot       │ │ FirmVault    │
└──────────────────┘ └──────────────┘ └─────────────────┘ └──────────────┘
```

---

## System 1: HERMES ("Roscoe") — The Orchestrator

**Repo:** github.com/Whaleylaw/Roscoe-hermes (fork of NousResearch/hermes-agent)
**Deployed:** Railway (project: illustrious-enthusiasm, service: Roscoe-hermes)
**Volume:** /opt/data (roscoe-hermes-volume) — persists across rebuilds
**URL:** Telegram bot (no public HTTP endpoint)

### What It Does
- Aaron's primary interface via Telegram
- Orchestrator daemon runs on 60s heartbeat alongside the gateway
- Scans GSD projects for work, dispatches to agents, collects results
- Manages memories, sessions, skills, cron jobs
- Hosts the GSD bridge (Node.js subprocess) for plan lifecycle

### Key Components
- **Gateway** (`gateway/`): Telegram message handler, slash commands
- **Daemon** (`daemon/`): Background orchestration thread
  - `supervisor.py`: Main heartbeat loop
  - `adapters/gsd.py`: GSD project scanner and task source
  - `adapters/openclaw.py`: OpenClaw gateway health + delegation
  - `adapters/mission_control.py`: MC task polling (stub)
  - `gsd_bridge.mjs`: Node.js bridge to gsd-lawyerinc library
- **Config**: `/opt/data/.env` (API keys), `/opt/data/config.yaml` (settings)
- **Entrypoint**: `docker/entrypoint.sh` — symlinks ~/.hermes and ~/.honcho to volume

### Environment Variables
- OPENROUTER_API_KEY — LLM provider
- TELEGRAM_BOT_TOKEN, TELEGRAM_ALLOWED_USERS — Telegram
- HONCHO_API_KEY — Cross-session memory
- GITHUB_TOKEN — Repo access
- DAEMON_ENABLED=true — Activates orchestrator daemon
- DAEMON_HEARTBEAT_SECONDS=60, DAEMON_APPROVAL_ONLY=true
- OPENCLAW_GATEWAY_URL — Points to OpenClaw on Render
- GSD_PROJECTS_DIR=/opt/data/projects, GSD_PACKAGE_DIR=/opt/data/gsd-lawyerinc

### How It Talks to Other Systems
- → **GSD** (Lane 2 only): Imports the Node.js library via gsd_bridge.mjs for ad-hoc projects
- → **OpenClaw**: HTTP health checks + delegation via daemon adapter
- → **Mission Control**: REST API for status visibility and approval routing
- → **FirmVault**: Not direct — Lane 1 runs FirmVault→MC→OpenClaw autonomously
- → **Aaron**: Telegram messages, approval notifications

---

## System 2: GSD (Get Shit Done) — Project Management

**Repo:** github.com/Whaleylaw/gsd-lawyerinc
**Deployed:** Installed on Hermes volume at /opt/data/gsd-lawyerinc
**Projects:** /opt/data/projects (15 active project workspaces)
**Runtime:** Node.js ESM library, called by Hermes daemon

### What It Does
- Structured 7-stage project lifecycle: IDEA → DISCUSS → RESEARCH → PLAN → APPROVE → EXECUTE → VERIFY → SHIP
- Parses PLAN.md files with XML task definitions grouped into waves
- Dispatches tasks to 3 platforms: Paperclip (Render), OpenClaw (relay), Hermes (direct)
- Syncs task status to Mission Control
- Manages STATE.md round-trip (read → mutate → serialize)

### Key Components
- `src/parser.js`: PLAN.md parser (frontmatter, tasks, waves, must-be-true conditions)
- `src/dispatcher.js`: Routes tasks to Paperclip/OpenClaw/Hermes by assignee
- `src/mc-sync.js`: Mission Control API integration (create/update tasks)
- `src/state.js`: STATE.md lifecycle management
- `src/index.js`: Barrel export of all public functions
- `templates/`: Project template files (PROJECT.md, REQUIREMENTS.md, etc.)

### Project Workspace Structure
```
projects/<name>/
  .planning/
    PROJECT.md          # Project spec
    REQUIREMENTS.md     # Requirements
    ROADMAP.md          # Phase roadmap
    STATE.md            # Current lifecycle state
    PLAN.md             # Active plan with tasks
    config.json         # Agent routing, approval gates
    mc-mappings.json    # MC task ID mappings (persisted)
```

### Environment Variables (for dispatch)
- PAPERCLIP_AUTH_EMAIL, PAPERCLIP_AUTH_PASSWORD — Paperclip agent platform
- RELAY_SECRET — OpenClaw relay auth
- MC_API_KEY — Mission Control API

### How It Talks to Other Systems (Lane 2 ONLY — ad-hoc projects)
- ← **Hermes**: Called via gsd_bridge.mjs (poll_project, dispatch_wave, update_status)
- → **OpenClaw**: Sends tasks via relay at relay.lawyerincorporated.com
- → **Paperclip**: Wakeup API at agents.lawyerincorporated.com
- → **Mission Control**: REST API for task sync (GSD projects only, NOT case work)
- GSD does NOT drive FirmVault case workflows. That's Lane 1 (FirmVault→MC direct).

---

## System 3: Mission Control — Dashboard & Agent Fleet

**Repo:** github.com/Whaleylaw/Roscoe-mission-control
**Deployed:** Render (backend: roscoe-mc-backend, DB: PostgreSQL, Redis)
**URL:** https://ops.lawyerincorporated.com
**Auth:** x-api-key header with API_KEY env var; web login via POST /api/auth/login

### What It Does
- Custom Next.js app (v2.0.1), SQLite-powered, self-hosted — NOT Planka
- Web dashboard for monitoring agent fleet, tasks, costs, approvals
- Agent lifecycle management (create, heartbeat, status tracking)
- Task queue: inbox → assigned → in_progress → quality_review → done
- Gateway management — connects to OpenClaw/Roscoebot runtimes
- Aegis approval system — status changes require approval

### Data Model
```
Workspace
  └── Gateway (OpenClaw runtime endpoint)
        └── Agent (worker with identity, heartbeat)
              └── Task (status, priority, assigned agent, metadata)
```

### Key API Endpoints (all /api/ — NOT /api/v1/)
- GET/POST /api/tasks — list/create tasks
- GET /api/tasks/{id} — single task
- PUT /api/tasks — bulk update {tasks: [{id, ...}]} (Aegis approval for status)
- DELETE /api/tasks/{id} — delete task
- GET/POST /api/agents — list/create agents
- GET/POST /api/gateways — list/create gateways
- POST /api/auth/login — web login {username, password}

### Authentication
- API auth: `x-api-key: <API_KEY>` header (the ONLY method for programmatic access)
- Web auth: POST /api/auth/login returns __Host-mc-session cookie
- Rate limit: ~20 req/min — use 2s delay between creates

### How It Talks to Other Systems
- ← **Hermes**: REST API (task polling, status updates, approval routing)
- ← **GSD**: REST API (mc-sync.js creates/updates tasks)
- ↔ **OpenClaw**: WebSocket RPC to gateway (provision agents, send tasks, collect results)
- ← **Aaron**: Web UI at ops.lawyerincorporated.com

---

## System 4: OpenClaw — Worker Agent Runtime

**Repo:** github.com/Whaleylaw/Roscoebot (fork of OpenClaw/OpenClaw)
**Deployed:** Render (service: openclaw, Docker, starter plan)
**URL:** https://openclaw-gateway-dfdi.onrender.com
**Persistent Disk:** /data (1GB — state, workspaces, agent memories)

### What It Does
- Runs 7 specialized paralegal agents as a single gateway process
- Each agent has its own workspace with SOUL.md (system prompt), tools, skills
- Gateway handles incoming tasks, routes to appropriate agent, manages sessions
- Agents execute legal work: drafting, research, analysis, document processing

### The 7 Agents
| ID | Name | Emoji | Role | Phase Coverage |
|---|---|---|---|---|
| lead-triage | Triage | 📋 | Intake screening, conflict check, SOL | Phase 0 |
| intake-setup | Setup | 📂 | File org, DocuSign, LORs, PIP | Phase 0-1 |
| treatment | MedTrack | 🏥 | Medical records, chronology, providers | Phase 2 |
| demand | Demand | 📝 | Damages calc, demand letter drafting | Phase 3 |
| negotiation | Negotiator | 🤝 | Offer eval, counter-strategy, settlement | Phase 4-5 |
| lien-specialist | LienClear | 💰 | Lien ID, PIP waterfall, reduction | Phase 6 |
| litigator | Litigator | ⚖️ | Complaints, discovery, depos, trial | Phase 7 |

### Configuration
- `deployment/agents/openclaw.json`: Full agent config (JSON5)
- `deployment/agents/workspaces/<id>/SOUL.md`: Per-agent system prompt
- `deployment/agents/seed-agents.sh`: Idempotent workspace seeder
- Config path: OPENCLAW_CONFIG_PATH=/etc/secrets/openclaw.json

### Key Environment Variables
- OPENCLAW_GATEWAY_PORT=10000, bind=lan
- OPENCLAW_STATE_DIR=/data/.openclaw
- OPENCLAW_WORKSPACE_DIR=/data/workspace
- OPENCLAW_GATEWAY_TOKEN — Auth for API/WS access
- OPENCLAW_CONFIG_PATH — Points to agent config

### How It Talks to Other Systems
- ← **Mission Control**: WebSocket RPC (agent provisioning, task dispatch, results)
- ← **GSD**: HTTP via relay at relay.lawyerincorporated.com
- ← **Hermes Daemon**: HTTP health checks + delegation
- → **FirmVault**: Agents read/write case vault via git operations

---

## System 5: FirmVault — Case Vault & Legal Knowledge

**Repo:** github.com/Whaleylaw/FirmVault
**Deployed:** GitHub repo (vault IS the deployment — git is the interface)
**Philosophy:** "The firm as a code repo" — every agent action is a commit or PR

### What It Does
- **Case Vault**: 120+ case directories in `cases/<slug>/` with markdown projections
- **Workflow Engine**: 8-phase case lifecycle (PHASE_DAG.yaml) with landmarks and predicates
- **Skills Library**: 42+ legal skills (SKILL.md format) covering the full PI practice
- **Tools Library**: Python tools for document processing, e-signature, legal research, etc.
- **Runtime**: Materializer (cron) + Worker (event-driven) pattern for task automation

### Case Lifecycle (PHASE_DAG.yaml)
```
Phase 0: Onboarding → Phase 1: File Setup → Phase 2: Treatment →
Phase 3: Demand → Phase 4: Negotiation → Phase 5: Settlement →
Phase 6: Lien Resolution → Phase 7: Litigation → Phase 8: Closed
```

Each phase has landmarks (milestones) with predicates that evaluate against the vault.
The materializer identifies unsatisfied landmarks and creates GitHub Issues.
Workers pick up issues, load the appropriate skill, execute, and commit results.

### Directory Structure
```
FirmVault/
  cases/<slug>/              # 120+ case directories
    <slug>.md                # Main case file (frontmatter + sections)
    documents/               # PHI-masked document shadows
    medical/                 # Medical record summaries
    insurance/               # Insurance claim tracking
  skills.tools.workflows/
    Skills/                  # 42+ legal skills (SKILL.md + references/)
    Tools/                   # Python tools organized by domain
    workflows/               # Phase workflows with landmarks
    runtime/                 # Materializer + worker + task templates
  Templates/                 # 73 document templates
  Contacts/                  # Provider/adjuster contact database
```

### Key Skills (mapped to OpenClaw agents)
- Intake: document-intake, police-report-analysis, import-case-documents
- Setup: case-file-organization, docusign-send, lor-generator, pip-application
- Treatment: medical-records-request, medical-chronology-*, liability-analysis
- Demand: demand-letter-generation, damages-calculation, multimedia-evidence-analysis
- Negotiation: offer-evaluation, negotiation-strategy, settlement-statement
- Liens: lien-management, pip-waterfall
- Litigation: complaint-drafting, discovery-drafting/response, deposition-*, trial-*

### Critical Rules
- PHI never lives in the vault — use {{placeholders}} for SSN, DOB, etc.
- Real files live on firm storage — vault has markdown shadows only
- Every agent action = git commit with task_id reference
- DATA_CONTRACT.md is the authoritative file layout specification
- Slug rules: lowercase, apostrophes stripped, & → and, non-alphanum → hyphen

### How It Talks to Other Systems
- ← **OpenClaw agents**: Read/write case vault via git (commits, PRs)
- ← **GSD**: Project workspaces reference FirmVault workflows and skills
- → **GitHub**: The vault IS a git repo — Issues for tasks, PRs for review
- → **Firm Storage**: Real files on Dropbox/Drive, vault has shadows

---

## TWO LANES — The Core Architecture Pattern

The stack runs on TWO PARALLEL LANES. This is the most important design decision.

### Lane 1: FirmVault Case Pipeline (structured legal work)
```
FirmVault engine (cron) → Mission Control → OpenClaw agents → FirmVault commits
```
This lane handles ALL case-related work. The flow:
1. FirmVault's `engine.py` walks open cases, reads PHASE_DAG.yaml + state.yaml
2. Engine identifies unsatisfied landmarks whose preconditions are met
3. `mc_bridge.py push` syncs those tasks to Mission Control as board tasks
4. MC dispatches to the appropriate OpenClaw agent via WebSocket RPC
5. Agent loads the named SKILL.md from FirmVault, executes with FirmVault tools
6. Agent commits results back to FirmVault (git commit/PR)
7. `reconciler.py` audits vault state against recorded state
8. `mc_bridge.py pull` reads MC approved/done tasks, updates state.yaml
9. Engine detects landmark satisfied → evaluates phase transitions → next tasks

This lane is DETERMINISTIC and AUTONOMOUS. The engine decides what needs doing
based on PHASE_DAG rules. Agents execute. Humans approve at gates.
GSD is NOT involved in this lane.

### Lane 2: GSD Ad-Hoc Projects (everything else)
```
Aaron → Hermes → GSD → dispatches to whoever → results
```
This lane handles projects OUTSIDE the structured case pipeline:
- Business development, marketing, infrastructure, research
- One-off legal projects that don't fit the PI case lifecycle
- Tech stack improvements (this very session is a GSD project)
- Anything Aaron wants to plan, track, and execute

GSD provides the 7-stage lifecycle (IDEA→SHIP) with wave-based dispatch
to Paperclip agents, OpenClaw agents, or Hermes itself.

### Why Two Lanes
- **Case work is codified** — PHASE_DAG.yaml defines exactly what happens when.
  It doesn't need flexible project management. It needs a state machine.
- **Everything else is ad-hoc** — Business projects need planning, discussion,
  research, and iteration. GSD provides that structured flexibility.
- **Separation prevents interference** — A GSD project refactoring the website
  never accidentally blocks a demand letter going out.

### Lane 1 Components (FirmVault → MC → OpenClaw)

**engine.py** — Zero side effects. Reads PHASE_DAG.yaml + per-case state.yaml.
Outputs: current phase, satisfied/unsatisfied landmarks, tasks to create,
phase transitions to fire, portfolio-wide summary.

**mc_bridge.py** — Two-way sync between FirmVault engine and Mission Control.
  - `push`: engine.available_work → MC tasks (create new, skip existing)
  - `pull`: MC approved/done tasks → state.yaml updates
  - `sync`: both directions

**reconciler.py** — Audits vault state. Three modes:
  - `audit`: read-only drift detection
  - `backfill`: re-evaluate landmarks from vault evidence
  - `fix`: write corrections to state.yaml

**task_templates/** — 30+ YAML templates that define how engine output maps
to MC tasks (e.g., draft-demand.yaml, request-medical-records.yaml).

**PHASE_DAG.yaml** — The master lifecycle definition. 8 phases, each with
landmarks (milestones) and predicates evaluated against the vault.

### Lane 2 Components (Hermes → GSD → agents)

**gsd-lawyerinc/** — Node.js library on Hermes volume.
**daemon/adapters/gsd.py** — Python adapter in Hermes daemon.
**daemon/gsd_bridge.mjs** — Node.js bridge subprocess.
**projects/** — 15+ ad-hoc project workspaces on Hermes volume.

### How Cases Flow Through Lane 1

1. New case arrives (intake pipeline or Aaron via Telegram)
2. `lead-triage` agent creates `cases/<slug>/` with initial data
3. Engine runs (cron), reads PHASE_DAG, identifies Phase 0 landmarks needed
4. mc_bridge pushes tasks: "sign retainer", "send HIPAA", "file LOR"
5. MC dispatches to `intake-setup` agent via OpenClaw gateway
6. Agent loads `docusign-send` skill, sends documents, commits vault updates
7. Reconciler confirms landmarks satisfied
8. Engine detects Phase 0→1 transition, emits Phase 1 tasks
9. This continues through all 8 phases until case closes

### How Ad-Hoc Projects Flow Through Lane 2

1. Aaron tells Hermes: "Build the new client intake form"
2. Hermes creates GSD project: DISCUSS lifecycle
3. Aaron and Hermes iterate on requirements and plan
4. GSD enters EXECUTE, dispatches wave 1 to openclaw/coder
5. Results come back, Hermes verifies, advances waves
6. Project ships. No case pipeline involvement.

---

## Quick Reference: URLs and Credentials

| System | URL | Auth |
|---|---|---|
| Hermes | Telegram DM | TELEGRAM_BOT_TOKEN |
| GSD | Local library on Hermes | Env vars for dispatch |
| Mission Control | ops.lawyerincorporated.com | LOCAL_AUTH_TOKEN (Render) |
| OpenClaw Gateway | openclaw-gateway-dfdi.onrender.com | OPENCLAW_GATEWAY_TOKEN |
| FirmVault | github.com/Whaleylaw/FirmVault | GITHUB_TOKEN |
| Paperclip | agents.lawyerincorporated.com | PAPERCLIP_AUTH_EMAIL/PASSWORD |
| Relay | relay.lawyerincorporated.com | RELAY_SECRET |

---

## System 6: Law Firm Wiki — Compiled Knowledge Base

**Location:** /opt/data/FirmVault/wiki/
**Architecture:** Karpathy LLM Knowledge Base (raw → compile → wiki → query)
**Schema:** wiki/AGENTS.md
**Compiler:** wiki/scripts/compile.py

### What It Does
- Compiles institutional PI practice knowledge from 21K+ activity logs
- Produces structured concept articles, connection articles, and index
- Maps knowledge to PHASE_DAG phases (0-7)
- Confidence scoring: low (1 case) → medium (2-4) → high (5+)
- Feeds into OpenClaw agent context and Hermes semantic skills

### Current State
- 14 concept articles + 3 connections from initial 3-case compilation
- All "low" confidence — needs more cases compiled to strengthen
- Skill: load `law-firm-wiki-compiler` for operations guide

---

## Pitfalls & Lessons Learned

1. **Railway rebuilds wipe the container filesystem** — ~/.hermes must be symlinked
   to /opt/data on every boot (fixed in entrypoint.sh, commit 452e54db)
2. **OpenClaw on Render defaults to loopback:18789** — must override with
   --port 10000 --bind lan in dockerCommand
3. **GSD credentials were hardcoded** — moved to env vars (PAPERCLIP_AUTH_*,
   RELAY_SECRET, MC_API_KEY)
4. **MC LOCAL_AUTH_TOKEN is auto-generated by Render** — must retrieve from
   dashboard to make API calls
5. **CORS on MC** may need updating (currently set to llm-lawyer.com domains)
6. **FirmVault PHI rules are strict** — agents must NEVER store raw PII,
   only {{placeholders}}
