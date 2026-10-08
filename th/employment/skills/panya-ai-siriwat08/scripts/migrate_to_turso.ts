#!/usr/bin/env bun
/**
 * Fast migrate local SQLite → Turso using batch transactions
 * Uses Python to dump → loads via libsql batch API (100x faster than one-by-one)
 */

import { createClient } from '@libsql/client'
import { existsSync } from 'fs'
import { join } from 'path'
import { execFileSync } from 'child_process'

const LOCAL_DB = process.argv[2] || '/home/z/my-project/db/custom.db'
const TURSO_URL = process.argv[3] || ''
const TURSO_TOKEN = process.argv[4] || ''

// Use absolute path to python3 to avoid PATH lookup (SonarCloud S4036).
// Allow override via PYTHON_BIN env var; default to /usr/bin/python3 (fixed, unwriteable).
const PYTHON_BIN = process.env.PYTHON_BIN || '/usr/bin/python3'

// Path to the extraction script (sibling of this file)
const EXTRACT_SCRIPT = join(import.meta.dir, '_extract_sqlite.py')

if (!TURSO_URL || !TURSO_TOKEN) {
  console.error('❌ Missing Turso URL or token')
  process.exit(1)
}

if (!existsSync(LOCAL_DB)) {
  console.error(`❌ Local DB not found: ${LOCAL_DB}`)
  process.exit(1)
}

console.log('🔗 Connecting to Turso:', TURSO_URL)
const client = createClient({
  url: TURSO_URL,
  authToken: TURSO_TOKEN,
})

console.log('📡 Testing connection...')
try {
  await client.execute('SELECT 1 as ok')
  console.log('  ✓ Connected')
} catch (e: any) {
  console.error('❌ Connection failed:', e.message)
  process.exit(1)
}

// Step 1: Use Python to dump data to JSON per table (faster + cleaner than SQL dump)
console.log('\n📤 Extracting data from local SQLite via Python...')
console.log(`  Python: ${PYTHON_BIN}`)
console.log(`  Script: ${EXTRACT_SCRIPT}`)

if (!existsSync(EXTRACT_SCRIPT)) {
  console.error(`❌ Extraction script not found: ${EXTRACT_SCRIPT}`)
  process.exit(1)
}

if (!existsSync(PYTHON_BIN)) {
  console.error(`❌ Python not found at: ${PYTHON_BIN}`)
  console.error('   Set PYTHON_BIN env var to your python3 absolute path')
  process.exit(1)
}

let data: any
try {
  // Use absolute path to python3 (no PATH lookup → S4036 safe).
  // Execute external script file (no -c flag → no inline code execution).
  // Pass DB path via env var (no string interpolation → S8701 safe).
  // No shell involved (execFileSync, not execSync → no command injection).
  const result = execFileSync(PYTHON_BIN, [EXTRACT_SCRIPT], {
    maxBuffer: 500 * 1024 * 1024, // 500 MB
    encoding: 'utf-8',
    // Only pass necessary env vars — don't inherit full process.env (S4036).
    env: {
      PANYA_LOCAL_DB: LOCAL_DB,
      HOME: process.env.HOME || '/tmp',
      // Minimal PATH for Python's internal use (e.g., sqlite3 module)
      PATH: '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
    },
  })
  data = JSON.parse(result)
} catch (e: any) {
  console.error('❌ Python extraction failed:', e.message)
  console.error(e.stderr || '')
  process.exit(1)
}

// Step 2: Drop existing tables (clean slate) — careful!
console.log('\n🧹 Dropping existing tables in Turso (clean slate)...')
const dropTables = [
  'case_law_links', 'rag_chunks', 'case_judgments', 'law_sections',
  'laws', 'sources', 'ingestion_log',
  'law_sections_fts', 'case_judgments_fts',
]
for (const t of dropTables) {
  try { await client.execute(`DROP TABLE IF EXISTS ${t};`) } catch (e) {}
}

// Step 3: Create schema (matching Prisma schema — all types as TEXT/INTEGER for SQLite)
console.log('\n🏗 Creating schema...')
const schemaStatements = [
  `CREATE TABLE sources (
    source_id INTEGER PRIMARY KEY,
    source_name TEXT NOT NULL,
    source_type TEXT,
    source_url TEXT,
    description TEXT,
    license TEXT
  );`,
  `CREATE TABLE laws (
    law_id INTEGER PRIMARY KEY,
    law_name_th TEXT NOT NULL,
    law_name_en TEXT,
    year TEXT,
    krisdika_sysid TEXT,
    law_go_th_id TEXT,
    source_url TEXT,
    status TEXT DEFAULT 'pending',
    full_text TEXT,
    notes TEXT,
    category TEXT,
    is_labor_law INTEGER DEFAULT 0
  );`,
  `CREATE TABLE law_sections (
    section_id INTEGER PRIMARY KEY AUTOINCREMENT,
    law_id INTEGER NOT NULL,
    article_key TEXT,
    section_number TEXT,
    section_text TEXT NOT NULL,
    notes TEXT,
    is_cancelled INTEGER DEFAULT 0,
    chapter TEXT,
    is_labor_related INTEGER DEFAULT 0,
    FOREIGN KEY (law_id) REFERENCES laws(law_id)
  );`,
  `CREATE TABLE case_judgments (
    judgment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    case_number TEXT,
    case_year TEXT,
    court TEXT,
    category TEXT,
    category_code TEXT,
    issue_number TEXT,
    law_references TEXT,
    fact TEXT,
    decision TEXT,
    title TEXT,
    source_id INTEGER,
    source_url TEXT,
    license_note TEXT,
    FOREIGN KEY (source_id) REFERENCES sources(source_id)
  );`,
  `CREATE TABLE case_law_links (
    link_id INTEGER PRIMARY KEY AUTOINCREMENT,
    judgment_id INTEGER,
    section_id INTEGER,
    law_id INTEGER,
    law_code TEXT,
    section_ref TEXT
  );`,
  `CREATE TABLE ingestion_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    table_name TEXT,
    record_count INTEGER,
    source_file TEXT,
    notes TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
  );`,
  `CREATE TABLE rag_chunks (
    chunk_id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_type TEXT,
    source_id INTEGER,
    law_id INTEGER,
    section_id INTEGER,
    judgment_id INTEGER,
    chunk_text TEXT,
    chunk_metadata TEXT
  );`,
  `CREATE INDEX idx_sections_law ON law_sections(law_id);`,
  `CREATE INDEX idx_sections_number ON law_sections(section_number);`,
  `CREATE INDEX idx_sections_labor ON law_sections(is_labor_related);`,
  `CREATE INDEX idx_judgments_category ON case_judgments(category);`,
  `CREATE INDEX idx_links_judgment ON case_law_links(judgment_id);`,
  `CREATE INDEX idx_links_section ON case_law_links(section_id);`,
  `CREATE INDEX idx_chunks_type ON rag_chunks(source_type);`,
]
for (const stmt of schemaStatements) {
  try { await client.execute(stmt) } catch (e: any) {
    console.error('  ✗ Schema error:', e.message.slice(0, 100))
  }
}
console.log('  ✓ Schema created')

// Step 4: Insert data in batches using batch API (100x faster)
console.log('\n📦 Inserting data via batch API...')

function escapeValue(v: any): any {
  if (v === null || v === undefined) return null
  if (typeof v === 'number') return v
  if (typeof v === 'boolean') return v ? 1 : 0
  return String(v)
}

const tableInsertOrder = ['sources', 'laws', 'law_sections', 'case_judgments', 'case_law_links', 'ingestion_log', 'rag_chunks']
const BATCH_SIZE = 200

for (const tableName of tableInsertOrder) {
  const tableData = data[tableName]
  if (!tableData || tableData.error || !tableData.rows || tableData.rows.length === 0) {
    console.log(`  ${tableName}: skipped (no data)`)
    continue
  }

  const cols = tableData.columns
  const placeholders = cols.map(() => '?').join(', ')
  const sql = `INSERT INTO ${tableName} (${cols.join(', ')}) VALUES (${placeholders})`

  console.log(`  ${tableName}: ${tableData.rows.length} rows...`)
  let inserted = 0
  let failed = 0

  for (let i = 0; i < tableData.rows.length; i += BATCH_SIZE) {
    const batch = tableData.rows.slice(i, i + BATCH_SIZE)
    const stmts = batch.map((row: any) => ({
      sql,
      args: cols.map((c: string) => escapeValue(row[c])),
    }))

    try {
      await client.batch(stmts, 'write')
      inserted += batch.length
    } catch (e: any) {
      // Try one-by-one for this batch to find the bad row
      for (const stmt of stmts) {
        try {
          await client.execute(stmt)
          inserted++
        } catch (e2: any) {
          failed++
          if (failed <= 3) {
            console.error(`    ✗ Row failed: ${e2.message.slice(0, 100)}`)
          }
        }
      }
    }

    if ((Math.floor(i / BATCH_SIZE) + 1) % 10 === 0) {
      process.stdout.write(`\r    ${inserted}/${tableData.rows.length} inserted (${failed} failed)`)
    }
  }
  console.log(`\r    ✓ ${inserted}/${tableData.rows.length} inserted (${failed} failed)           `)
}

// Step 5: Recreate FTS5 virtual tables
console.log('\n🔍 Creating FTS5 indexes...')
const ftsStatements = [
  `CREATE VIRTUAL TABLE law_sections_fts USING fts5(
    section_text, article_key, law_id UNINDEXED, section_id UNINDEXED,
    content='law_sections', content_rowid='section_id'
  );`,
  `INSERT INTO law_sections_fts(section_text, article_key, law_id, section_id)
   SELECT section_text, COALESCE(article_key, ''), law_id, section_id FROM law_sections;`,
  `CREATE VIRTUAL TABLE case_judgments_fts USING fts5(
    fact, decision, case_number, judgment_id UNINDEXED, category UNINDEXED,
    content='case_judgments', content_rowid='judgment_id'
  );`,
  `INSERT INTO case_judgments_fts(fact, decision, case_number, judgment_id, category)
   SELECT COALESCE(fact,''), COALESCE(decision,''), COALESCE(case_number,''), judgment_id, COALESCE(category,'')
   FROM case_judgments;`,
]
for (const stmt of ftsStatements) {
  try {
    await client.execute(stmt)
    console.log(`  ✓ ${stmt.slice(0, 70).replace(/\n/g, ' ')}...`)
  } catch (e: any) {
    console.log(`  ✗ ${e.message.slice(0, 100)}`)
  }
}

// Step 6: Verify counts
console.log('\n🔍 Verifying final counts...')
const tables = ['sources', 'laws', 'law_sections', 'case_judgments', 'case_law_links', 'rag_chunks']
for (const t of tables) {
  try {
    const r = await client.execute(`SELECT COUNT(*) as n FROM ${t}`)
    console.log(`  ${t}: ${r.rows[0].n}`)
  } catch (e: any) {
    console.log(`  ${t}: ERROR — ${e.message.slice(0, 80)}`)
  }
}

// Step 7: FTS test
console.log('\n🧪 FTS5 test...')
try {
  const r = await client.execute({
    sql: `SELECT s.section_id, s.article_key, snippet(law_sections_fts, 0, '<<', '>>', '...', 20) as snip
          FROM law_sections_fts
          JOIN law_sections s ON s.section_id = law_sections_fts.rowid
          WHERE law_sections_fts MATCH ?
          LIMIT 2`,
    args: ['"ค่าจ้าง"'],
  })
  console.log(`  ✓ FTS returned ${r.rows.length} rows`)
  if (r.rows.length > 0) {
    console.log(`    Example: ${r.rows[0].article_key}`)
  }
} catch (e: any) {
  console.log(`  ✗ FTS test failed: ${e.message.slice(0, 100)}`)
}

console.log('\n🎉 Migration complete!')
client.close()
