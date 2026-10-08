# 🇹🇭 Panya-AI — Thai Legal AI for Employers

> ฐานข้อมูลกฎหมายไทย + AI ตรวจสัญญา ประเมินความเสี่ยง และสร้างเอกสาร
> ออกแบบมาเพื่อฝั่งนายจ้าง / HR / In-house Legal — citation-first workflow

🔗 **Live:** Vercel deploy (auto from main branch)
🗄️ **Database:** Turso (libSQL) — 78 laws · 12,936 sections · 502 judgments · 615 regulations · 63 templates
🤖 **AI:** OpenRouter Ling-3.0-flash (excellent Thai, ~30s response)

---

## ✨ Features

### 🤖 AI Chat (3-column layout)
- **3-column layout:** Chat / Agent Workflow / Citation Drawer
- **Agent workflow animation:** 5 steps (understand → search laws → search judgments → risk assess → compose)
- **Citation pills:** Click [1] [2] [3] → citation drawer slides in with full text
- **Smart scroll:** Scrolls to top of AI response (not bottom)
- **Mascot features:**
  - 🔄 Direction-aware: mascot turns right when citation panel opens
  - 🧠 Thinking animation: cycles front/left/right during AI processing
  - 🥚 Easter egg: click mascot 3x → turns around with funny message
  - 🫧 Floating mascot in Hero background

### 📄 PDF Document Builder (4-step wizard)
1. **เลือกเทมเพลต** — 63 templates with category filter
2. **กรอกข้อมูล** — Company, employee, signer details
3. **ตรวจดู** — Preview before download
4. **ดาวน์โหลด** — PDF via `/api/templates/pdf`

### 📊 Risk Matrix (5×5)
- Likelihood × Impact grid with 7 pre-loaded scenarios
- Color-coded: green (low) → red (critical)
- Click cell → scenario detail + law reference + "Ask AI"

### 🔍 Contract Analysis
- Paste contract text → AI analyzes for labor law violations
- Red flags with severity badges (ร้ายแรง/ปานกลาง)
- AI summary + recommendations
- Sample contract with 5 problematic clauses

### 📖 Legal Database
- **78 laws** (labor, civil, criminal, business, other)
- **12,936 sections** with FTS5 full-text search
- **502 judgments** from Supreme Court (ฎีกาแรงงาน)
- **615 regulations** (กฎกระทรวง, ประกาศ, ระเบียบ)
- **63 contract templates** (สัญญา, หนังสือเตือน, หนังสือเลิกจ้าง, แบบสปส.)
- **21,361 RAG chunks** for AI retrieval
- **FTS5 indexes** (v2) — search works in Thai

### 🎨 Design
- Navy + Gold premium theme
- IBM Plex Sans Thai + IBM Plex Serif fonts
- Sidebar navigation (collapsible: 264px ↔ 72px)
- Mascot avatar (4 directions: front/back/left/right)
- Typewriter hero with live chat demo
- Employer-side positioning section (6 defense cards)

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Framework | Next.js 16 (Turbopack) |
| Language | TypeScript |
| Styling | Tailwind CSS 4 |
| Database | Turso (libSQL) via Prisma 6 |
| AI | OpenRouter Ling-3.0-flash |
| Search | FTS5 (SQLite full-text search) |
| Fonts | IBM Plex Sans Thai + IBM Plex Serif |
| Deploy | Vercel |
| Repo | GitHub (Siriwat08/Panya-AI) |

---

## 📁 Project Structure

```
src/
├── app/
│   ├── api/          # API routes (ask, search, laws, judgments, etc.)
│   ├── globals.css   # Design tokens + Tailwind
│   ├── layout.tsx    # Font setup + metadata
│   └── page.tsx      # Entry point
├── components/
│   ├── chat/         # AskView (3-column AI chat)
│   ├── contract/     # ContractAnalysisView
│   ├── home/         # Hero (typewriter) + HomeView + LawList
│   ├── judgment/     # JudgmentsView + JudgmentView
│   ├── law/          # LawsView + LawView + SectionView
│   ├── layout/       # Sidebar + Header
│   ├── pdf/          # PdfBuilderView (4-step wizard)
│   ├── risk/         # RiskMatrixView (5×5)
│   ├── search/       # SearchView (laws + sections + judgments + regulations + templates)
│   ├── templates/    # TemplatesView
│   └── ui/           # shadcn/ui components
├── lib/
│   ├── db.ts         # Prisma client (Turso)
│   ├── rag.ts        # RAG retrieval (FTS5 v2)
│   ├── navigation.ts # URL-based SPA navigation
│   ├── types.ts      # TypeScript types
│   └── zai-client.ts # OpenRouter LLM client
└── public/
    ├── mascot/       # 4 mascot images (front/back/left/right)
    └── panya-logo.png
```

---

## 🗄️ Database Schema

- **sources** (9) — Data provenance (krisdika, PyThaiNLP, PBuakhaw, mol, moi)
- **laws** (78) — Thai laws with category, year, full text
- **law_sections** (12,936) — Parsed sections with Thai/Arabic numerals
- **judgments** (502) — Supreme Court judgments with fact/issue/ruling
- **regulations** (615) — Ministerial regulations, announcements, rules
- **contract_templates** (63) — F1-F63 document templates
- **rag_chunks** (21,361) — Text chunks for AI retrieval
- **FTS5 v2** — 4 virtual tables for full-text search

---

## 🚀 Deployment

See [DEPLOYMENT.md](./DEPLOYMENT.md) for detailed setup.

### Quick Start
```bash
npm install
npx prisma generate
npm run dev
```

### Environment Variables
```
DATABASE_URL=libsql://panya-ai-siriwat08.aws-ap-northeast-1.turso.io
TURSO_AUTH_TOKEN=<your-token>
OPENROUTER_API_KEY=<your-key>
```

---

## 📝 License & Data Sources

- **Laws:** สำนักงานคณะกรรมการกฤษฎีกา (Public domain)
- **Judgments:** PBuakhaw/deka_retrival (Academic use only — NOT for commercial use)
- **Regulations:** กระทรวงแรงงาน (Public domain)
- **Code:** Proprietary — หจก.เผ่าปัญญา ทรานสปอร์ต

---

## 🎯 Roadmap

### Done ✅
- Phase 1: AI Prompt + Legal Strategist system prompt
- Phase 2: Design System + Sidebar + Logo + Fonts
- Phase 3: AI Chat 3-column + Typewriter Hero + Employer Section
- Phase 4: PDF Builder Wizard + Risk Matrix + Contract Analysis

### Next
- Law status badges (ใช้บังคับ / ยกเลิก / แก้ไขล่าสุด)
- Latest / Popular / Recommended judgments
- Notes + highlights + export PDF
- Persona-based onboarding (HR / Legal / Executive)
- Contract deviation check (compare with standard template)
- Internal company knowledge ingestion
