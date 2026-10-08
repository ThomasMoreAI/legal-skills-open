# 🚀 Deployment Guide — Vercel + Turso

คู่มือฉบับสมบูรณ์สำหรับ deploy Panya-AI ไปยัง Vercel
พร้อม migration จาก SQLite file → Turso libSQL (เพราะ Vercel serverless ใช้ SQLite file ไม่ได้)

---

## 📋 สารบัญ

1. [Why Turso?](#why-turso)
2. [Prerequisites](#prerequisites)
3. [Step 1 — Push to GitHub](#step-1--push-to-github)
4. [Step 2 — Create Turso Database](#step-2--create-turso-database)
5. [Step 3 — Import Data to Turso](#step-3--import-data-to-turso)
6. [Step 4 — Switch Prisma to libsql](#step-4--switch-prisma-to-libsql)
7. [Step 5 — Deploy to Vercel](#step-5--deploy-to-vercel)
8. [Alternative — Supabase (PostgreSQL)](#alternative--supabase-postgresql)
9. [Troubleshooting](#troubleshooting)

---

## Why Turso?

Vercel serverless functions ไม่มี persistent filesystem — ไฟล์ SQLite ที่ commit ไว้จะ:
- ❌ หายไประหว่าง requests
- ❌ ไม่ sync ระหว่าง instances
- ❌ 22 MB จะถูก load ใหม่ทุก cold start (ช้า)

**Turso** คือทางออกที่ดีที่สุดเพราะ:
- ✅ SQLite-compatible (Prisma schema เปลี่ยนนิดเดียว)
- ✅ Free tier: 500 databases, 9 GB total, 1 billion row reads/month
- ✅ Edge network (low latency ทั่วโลก)
- ✅ Migration ง่ายจาก local SQLite file

---

## Prerequisites

- [GitHub account](https://github.com)
- [Vercel account](https://vercel.com) (free)
- [Turso account](https://turso.tech) (free)
- [Z.AI API key](https://z.ai) (สำหรับ AI RAG features)
- โค้ดนี้ push ขึ้น GitHub เรียบร้อยแล้ว

---

## Step 1 — Push to GitHub

### 1.1 Create new GitHub repository

```bash
# ไปที่ https://github.com/new
# ตั้งชื่อ: panya-ai (หรือชื่อที่ต้องการ)
# เลือก Public หรือ Private ตามต้องการ
# อย่าเลือก "Initialize with README" (เรามีไฟล์เองแล้ว)
# คลิก "Create repository"
```

### 1.2 Initialize git + push

```bash
cd /path/to/panya-ai

# Initialize git
git init
git branch -M main

# Stage ทุกอย่าง (ยกเว้น .gitignored)
git add .

# ตรวจสอบว่าจะ commit อะไรบ้าง — สำคัญ!
git status

# ควรเห็นแค่ไฟล์ใน src/, scripts/, prisma/, และ config files
# ถ้าเห็น node_modules/, .next/, db/custom.db แสดงว่า .gitignore มีปัญหา

# Commit
git commit -m "Initial commit: Panya-AI — Next.js + Prisma + SQLite"

# Add remote + push
git remote add origin https://github.com/<your-username>/panya-ai.git
git push -u origin main
```

### 1.3 ⚠️ สิ่งที่ต้องไม่ commit

ตรวจสอบ `.gitignore` ว่ามีรายการเหล่านี้:
```gitignore
# Database files (regenerate from scripts/rebuild_legal_db.py)
db/
data/
*.sqlite
*.db

# Environment
.env
.env.local
.env.production

# Build artifacts
.next/
node_modules/

# Logs
*.log
dev.log
```

**ห้าม commit:**
- ❌ `db/custom.db` (22 MB — ใหญ่เกิน ใช้ rebuild script แทน)
- ❌ `.env` (มี secrets)
- ❌ `node_modules/`
- ❌ `.next/`

---

## Step 2 — Create Turso Database

### 2.1 Install Turso CLI

```bash
# macOS / Linux
curl -sSfL https://get.tur.so/install.sh | bash

# Windows (PowerShell)
irm https://get.tur.so/install.ps1 | iex

# ตรวจสอบ
turso --version
```

### 2.2 Login + create database

```bash
# Login (เปิด browser ให้)
turso auth login

# Create database (เลือก region ใกล้ผู้ใช้ — sin = Singapore)
turso db create panya-ai --location sin

# รอจนกว่าจะ ready
turso db list
# ควรเห็น:
# NAME             LOCATION  STATUS
# panya-ai     sin       ready
```

### 2.3 Get connection details

```bash
# Get URL (ใช้ใน DATABASE_URL)
turso db show panya-ai --url
# → libsql://panya-ai-<your-account>.turso.io

# Create auth token (ใช้ใน TURSO_AUTH_TOKEN)
turso db tokens create panya-ai
# → <YOUR_TURSO_TOKEN>

# เก็บค่าทั้งสองไว้ — จะใช้ใน Step 5
```

---

## Step 3 — Import Data to Turso

### 3.1 Make sure local DB is up-to-date

```bash
# ถ้ายังไม่ได้ build DB
python scripts/rebuild_legal_db.py
# → outputs to data/thai_legal_db.sqlite

# Copy to prisma location
mkdir -p db
cp data/thai_legal_db.sqlite db/custom.db
```

### 3.2 Export to SQL + import to Turso

```bash
# Method 1: Use sqlite3 to dump + import
sqlite3 db/custom.db .dump > /tmp/thai_law_dump.sql

# ลบบรรทัดที่ Turso ไม่รองรับ (PRAGMA statements, BEGIN TRANSACTION, etc.)
sed -i '/PRAGMA/d; /BEGIN TRANSACTION/d; /COMMIT/d' /tmp/thai_law_dump.sql

# Import to Turso
turso db shell panya-ai < /tmp/thai_law_dump.sql

# ตรวจสอบ
turso db shell panya-ai "SELECT COUNT(*) FROM laws;"
# → 14
turso db shell panya-ai "SELECT COUNT(*) FROM law_sections;"
# → 4441
```

### 3.3 Alternative: Use Turso's official migration tool

```bash
# ถ้าใช้ Turso CLI version ใหม่
turso db shell panya-ai --file db/custom.db
```

### 3.4 ⚠️ Note about FTS5

Turso รองรับ FTS5 แต่ต้อง enable ก่อน:

```bash
turso db shell panya-ai "SELECT * FROM law_sections_fts LIMIT 1;"

# ถ้า error ให้ recreate FTS5 index:
turso db shell panya-ai << 'EOF'
CREATE VIRTUAL TABLE IF NOT EXISTS law_sections_fts USING fts5(
  section_text, article_key, law_id UNINDEXED, section_id UNINDEXED,
  content='law_sections', content_rowid='section_id'
);
INSERT INTO law_sections_fts(section_text, article_key, law_id, section_id)
  SELECT section_text, COALESCE(article_key, ''), law_id, section_id FROM law_sections;
EOF
```

---

## Step 4 — Switch Prisma to libsql

### 4.1 Install libsql adapter

```bash
bun add @prisma/adapter-libsql @libsql/client
# หรือ
npm install @prisma/adapter-libsql @libsql/client
```

### 4.2 Update Prisma schema

Edit `prisma/schema.prisma`:

```prisma
generator client {
  provider = "prisma-client-js"
  previewFeatures = ["driverAdapters"]
}

datasource db {
  provider = "sqlite"
  url      = env("DATABASE_URL")
}
```

> **Note:** `provider` ยังเป็น `sqlite` อยู่ แต่ `url` จะเป็น `libsql://...` แทน `file:...`

### 4.3 Update db.ts to use libsql adapter

Edit `src/lib/db.ts`:

```typescript
import { PrismaClient } from '@prisma/client'
import { PrismaLibSQL } from '@prisma/adapter-libsql'
import { createClient } from '@libsql/client'

const globalForPrisma = globalThis as unknown as {
  prisma: PrismaClient | undefined
}

function createPrismaClient() {
  // ถ้าเป็น Turso (production)
  if (process.env.TURSO_AUTH_TOKEN && process.env.DATABASE_URL?.startsWith('libsql://')) {
    const libsql = createClient({
      url: process.env.DATABASE_URL,
      authToken: process.env.TURSO_AUTH_TOKEN,
    })
    const adapter = new PrismaLibSQL(libsql)
    return new PrismaClient({ adapter })
  }

  // Local dev — ใช้ SQLite file ปกติ
  return new PrismaClient({
    log: process.env.NODE_ENV !== 'production' ? ['query', 'error', 'warn'] : ['error'],
  })
}

export const db = globalForPrisma.prisma ?? createPrismaClient()

if (process.env.NODE_ENV !== 'production') globalForPrisma.prisma = db
```

### 4.4 Regenerate Prisma client

```bash
bun run db:generate
```

### 4.5 Test locally with Turso

```bash
# แก้ .env ชั่วคราว
DATABASE_URL=libsql://panya-ai-<your-account>.turso.io
TURSO_AUTH_TOKEN=<your-token>

# รัน dev server
bun run dev

# ทดสอบ — ถ้าหน้าแรกโหลด + แสดงตัวเลขสถิติ แปลว่าเชื่อมต่อ Turso ได้
```

---

## Step 5 — Deploy to Vercel

### 5.1 Import to Vercel

1. ไปที่ [vercel.com/new](https://vercel.com/new)
2. คลิก **"Import Git Repository"**
3. เลือก GitHub repo `panya-ai` ของคุณ
4. Vercel จะ detect Next.js อัตโนมัติ

### 5.2 Configure Environment Variables

ในหน้า "Configure Project" ให้เพิ่ม Environment Variables:

| Name | Value | Environments |
|------|-------|--------------|
| `DATABASE_URL` | `libsql://panya-ai-<your-account>.turso.io` | Production, Preview, Development |
| `TURSO_AUTH_TOKEN` | `<YOUR_TURSO_TOKEN>` (from Step 2.3) | Production, Preview, Development |
| `Z_AI_API_KEY` | (your Z.AI API key) | Production, Preview, Development |

> ⚠️ อย่า commit `.env` ขึ้น git! ใช้เฉพาะ Vercel dashboard เท่านั้น

### 5.3 Deploy

1. คลิก **"Deploy"**
2. รอ 2-3 นาที (build + deploy)
3. เมื่อเสร็จ Vercel จะให้ URL: `https://panya-ai.vercel.app`
4. คลิกเพื่อเปิดแอป 🎉

### 5.4 Set custom domain (optional)

1. ใน Vercel dashboard → Project → Settings → Domains
2. เพิ่ม custom domain (เช่น `thailaw.yourdomain.com`)
3. ตั้งค่า DNS ตามที่ Vercel บอก

---

## Alternative — Supabase (PostgreSQL)

ถ้าต้องการ PostgreSQL แทน Turso:

### Pros
- ฟีเจอร์เยอะกว่า (Auth, Realtime, Storage)
- Dashboard ที่ใช้ง่ายกว่า
- รองรับ pgvector สำหรับ embeddings

### Cons
- ต้อง migrate Prisma schema (sqlite → postgresql types)
- `BOOLEAN` แทน `INTEGER`
- `TEXT[]` แทน JSON arrays
- FTS5 ไม่มี → ใช้ `pg_trgm` หรือ `tsvector`

### Migration steps (สรุป)

```bash
# 1. Create Supabase project at https://supabase.com
# 2. Get connection string from Project Settings → Database

# 3. Update prisma/schema.prisma
# datasource db {
#   provider = "postgresql"
#   url      = env("DATABASE_URL")
# }
# (ต้องแปลง types ด้วย — BOOLEAN, TEXT[], ฯลฯ)

# 4. Migrate data
bun run db:migrate

# 5. Deploy to Vercel ตาม Step 5 ด้านบน
```

---

## Troubleshooting

### Problem: "Cannot find module '@prisma/adapter-libsql'"
```bash
bun add @prisma/adapter-libsql @libsql/client
bun run db:generate
```

### Problem: FTS5 not working on Turso
```bash
# Recreate FTS5 indexes
turso db shell panya-ai << 'EOF'
DROP TABLE IF EXISTS law_sections_fts;
CREATE VIRTUAL TABLE law_sections_fts USING fts5(
  section_text, article_key, law_id UNINDEXED, section_id UNINDEXED,
  content='law_sections', content_rowid='section_id'
);
INSERT INTO law_sections_fts(section_text, article_key, law_id, section_id)
  SELECT section_text, COALESCE(article_key, ''), law_id, section_id FROM law_sections;
EOF
```

### Problem: Prisma "Transaction API is not allowed"
Turso/libsql มีข้อจำกัดเรื่อง transaction บางอย่าง ใช้ `db.$transaction` ไม่ได้ทุกกรณี

**Fix:** ใช้ `Promise.all` แทน หรือเขียน raw SQL

### Problem: Vercel function timeout (default 10s)
API ที่ช้า (เช่น AI RAG) อาจ timeout

**Fix:**
1. ใน `vercel.json` เพิ่ม:
```json
{
  "functions": {
    "src/app/api/ask/route.ts": {
      "maxDuration": 60
    }
  }
}
```

2. หรือ upgrade เป็น Vercel Pro (60s timeout สำหรับ hobby, 300s สำหรับ Pro)

### Problem: Cold start slow
SQLite file 22 MB → Turso ทุก cold start ต้อง fetch จาก Turso

**Fix:**
- ใช้ Turso's edge replica (read-only copies ใกล้ผู้ใช้)
- Cache hot data ใน memory (LRU cache)
- ลดขนาดข้อมูลที่ไม่จำเป็น (เช่น ลบ `full_text` ของ ป.พ.พ. ที่ว่าง)

### Problem: AI RAG ไม่ทำงานบน Vercel
- ตรวจสอบว่าตั้ง `Z_AI_API_KEY` ใน Vercel env vars แล้ว
- ตรวจสอบ function timeout (AI อาจใช้เวลา > 10s)
- ดู logs ที่ Vercel dashboard → Functions → /api/ask

---

## ✅ Deployment Checklist

ก่อน deploy ให้ตรวจสอบ:

- [ ] โค้ด push ขึ้น GitHub เรียบร้อย
- [ ] `.gitignore` มี `db/`, `data/`, `.env`, `node_modules/`, `.next/`
- [ ] `db/custom.db` ไม่ได้ commit
- [ ] Turso database สร้างแล้ว + data imported
- [ ] `DATABASE_URL` + `TURSO_AUTH_TOKEN` พร้อม
- [ ] `Z_AI_API_KEY` พร้อม (สำหรับ AI features)
- [ ] `prisma/schema.prisma` ใช้ `previewFeatures = ["driverAdapters"]`
- [ ] `src/lib/db.ts` ใช้ libsql adapter
- [ ] `bun run db:generate` ทำงานได้
- [ ] ทดสอบ local กับ Turso แล้ว
- [ ] Vercel project import เรียบร้อย
- [ ] Environment variables ตั้งค่าครบใน Vercel
- [ ] `vercel.json` มี `maxDuration: 60` สำหรับ /api/ask (optional)

หลัง deploy:
- [ ] หน้าแรกโหลดและแสดงตัวเลขสถิติ
- [ ] ค้นหา "ค่าจ้าง" ได้ผลลัพธ์
- [ ] ถาม AI ได้คำตอบพร้อม citations
- [ ] Bookmark ทำงาน (localStorage)

---

## 💰 Cost Estimate

| Service | Free tier | After free |
|---------|-----------|------------|
| Vercel Hobby | 100 GB bandwidth, 100 GB-hours serverless | $20/month (Pro) |
| Turso | 9 GB total, 1B row reads/month | $29/month (Scaler) |
| Z.AI LLM | (verify current pricing) | per-token |
| GitHub | Public unlimited, Private unlimited | $4/month (Pro) |

**สำหรับใช้งานเอง + traffic ไม่มาก → ฟรีทั้งหมด**
