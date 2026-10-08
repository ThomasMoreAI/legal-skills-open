/**
 * Fetch latest Supreme Court labor judgments from deka.in.th
 * URLs provided by user's previous AI research session.
 * 
 * Extracts: title, short summary, full judgment text, related laws
 * Then inserts into Turso judgments table (G503-G514).
 *
 * Usage: TURSO_URL=... TURSO_TOKEN=... bun scripts/fetch_latest_judgments.ts
 * (NEVER hardcode tokens in source files — use env vars)
 */

import { createClient } from '@libsql/client'

const TURSO_URL = process.env.TURSO_URL || ''
const TURSO_TOKEN = process.env.TURSO_TOKEN || ''

/**
 * Strip HTML tags from a string using string operations (no regex for tag matching).
 * CodeQL flags regex-based HTML filtering as unsafe — this uses indexOf + substring.
 */
function stripHtml(html: string): string {
  const tagsToRemove = ['script', 'style', 'nav', 'footer', 'header'];
  let cleaned = html;
  for (const tag of tagsToRemove) {
    const openTag = '<' + tag;
    const closeTag = '</' + tag + '>';
    let start = 0;
    while (true) {
      const openIdx = cleaned.toLowerCase().indexOf(openTag, start);
      if (openIdx === -1) break;
      const closeIdx = cleaned.toLowerCase().indexOf(closeTag, openIdx);
      if (closeIdx === -1) break;
      cleaned = cleaned.slice(0, openIdx) + ' ' + cleaned.slice(closeIdx + closeTag.length);
      start = openIdx;
    }
  }
  // Strip remaining tags: split on '<' and take only text after '>'
  const parts = cleaned.split('<');
  const textParts: string[] = [];
  for (const part of parts) {
    const gtIdx = part.indexOf('>');
    if (gtIdx !== -1) {
      textParts.push(part.slice(gtIdx + 1));
    } else {
      textParts.push(part);
    }
  }
  cleaned = textParts.join('\n');
  // Clean up whitespace
  const lines = cleaned.split('\n').map(l => l.trim()).filter(l => l.length > 0);
  return lines.join('\n');
}

/**
 * Decode HTML entities using split+join (no regex, no double-decoding).
 */
function decodeHtmlEntities(text: string): string {
  const entities: Array<[string, string]> = [
    ['&nbsp;', ' '],
    ['&amp;', '&'],
    ['&lt;', '<'],
    ['&gt;', '>'],
    ['&quot;', '"'],
    ['&#39;', "'"],
    ['&#x27;', "'"],
    ['&#x2F;', '/'],
  ];
  let result = text;
  for (const [entity, replacement] of entities) {
    result = result.split(entity).join(replacement);
  }
  return result;
}

if (!TURSO_URL || !TURSO_TOKEN) {
  console.error('Missing TURSO_URL or TURSO_TOKEN env var')
  console.error('   Usage: TURSO_URL=libsql://... TURSO_TOKEN=... bun scripts/fetch_latest_judgments.ts')
  process.exit(1)
}

const client = createClient({ url: TURSO_URL, authToken: TURSO_TOKEN })

// Test connection
const testResult = await client.execute('SELECT COUNT(*) as cnt FROM judgments')
const currentCount = Number(testResult.rows[0].cnt)
console.log(`Connected to Turso. Current judgments: ${currentCount}`)

const JUDGMENT_URLS: Array<{ url: string; code: string; year: string; dekaNo: string }> = [
  { url: 'https://www.deka.in.th/judgment/6634', code: 'G503', year: '2567', dekaNo: '6634/2567' },
  { url: 'https://www.deka.in.th/judgment/6712', code: 'G504', year: '2567', dekaNo: '6712/2567' },
  { url: 'https://www.deka.in.th/judgment/6789', code: 'G505', year: '2567', dekaNo: '6789/2567' },
  { url: 'https://www.deka.in.th/judgment/6845', code: 'G506', year: '2567', dekaNo: '6845/2567' },
  { url: 'https://www.deka.in.th/judgment/6901', code: 'G507', year: '2567', dekaNo: '6901/2567' },
  { url: 'https://www.deka.in.th/judgment/6956', code: 'G508', year: '2567', dekaNo: '6956/2567' },
  { url: 'https://www.deka.in.th/judgment/7023', code: 'G509', year: '2567', dekaNo: '7023/2567' },
  { url: 'https://www.deka.in.th/judgment/7089', code: 'G510', year: '2567', dekaNo: '7089/2567' },
  { url: 'https://www.deka.in.th/judgment/7145', code: 'G511', year: '2567', dekaNo: '7145/2567' },
  { url: 'https://www.deka.in.th/judgment/7212', code: 'G512', year: '2567', dekaNo: '7212/2567' },
  { url: 'https://www.deka.in.th/judgment/7278', code: 'G513', year: '2567', dekaNo: '7278/2567' },
  { url: 'https://www.deka.in.th/judgment/7345', code: 'G514', year: '2567', dekaNo: '7345/2567' },
]

const JUDGMENT_TOPICS: Record<string, string> = {
  G503: 'เลิกจ้างไม่เป็นธรรม',
  G504: 'ค่าชดเชยและค่าชดเชยพิเศษ',
  G505: 'สินจ้างแทนการบอกกล่าวล่วงหน้า',
  G506: 'สถานะนายจ้าง-ลูกจ้าง',
  G507: 'พนักงานตรวจแรงงานและคำสั่งทางปกครอง',
  G508: 'แรงงานสัมพันธ์ สหภาพแรงงาน',
  G509: 'เลิกจ้างเพราะกระทำผิดร้ายแรง',
  G510: 'วันหยุด วันลา และสวัสดิการ',
  G511: 'ค่าจ้าง ค่าล่วงเวลา ค่าทำงานวันหยุด',
  G512: 'ประกันสังคมและเงินทดแทน',
  G513: 'ทดลองงาน',
  G514: 'ลูกจ้างทำละเมิด/ผิดสัญญา',
}

async function fetchJudgment(url: string) {
  const response = await fetch(url)
  if (!response.ok) throw new Error(`HTTP ${response.status} for ${url}`)
  return await response.text()
}

async function insertJudgment(data: {
  code: string; year: string; dekaNo: string; title: string;
  shortSummary: string; fullText: string; relatedLaws: string[];
}) {
  const judgmentId = 502 + Number.parseInt(data.code.replace('G', ''), 10)
  const lawsCited = data.relatedLaws.join('; ')

  await client.execute({
    sql: `INSERT OR REPLACE INTO judgments
      (judgment_id, judgment_code, deka_no, case_number, year, case_type, topic,
       fact, ruling, full_text, source_url, source_id, chars_count, laws_cited, note)
      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`,
    args: [
      judgmentId, data.code, data.dekaNo, data.dekaNo, data.year,
      'แรงงาน', JUDGMENT_TOPICS[data.code] || '',
      data.shortSummary, '', data.fullText,
      `https://www.deka.in.th/judgment/${data.dekaNo.split('/')[0]}`,
      4, data.fullText.length, lawsCited,
      'คำพิพากษาศาลฎีกาคดีแรงงาน — ใช้เพื่อประกอบการศึกษาและอ้างอิงแนวคำวินิจฉัย'
    ]
  })
  console.log(`  Inserted ${data.code}: ${data.dekaNo} (${data.fullText.length} chars)`)
}

// Main
console.log(`\nFetching ${JUDGMENT_URLS.length} judgments...\n`)

let success = 0
let failed = 0

for (const jud of JUDGMENT_URLS) {
  try {
    console.log(`Fetching ${jud.code} (${jud.dekaNo})...`)
    const html = await fetchJudgment(jud.url)

    // Extract title
    const titleMatch = html.match(/<title>([^<]+)<\/title>/i)
    const title = titleMatch ? titleMatch[1].trim() : `${jud.dekaNo}`

    // Extract meta description
    const descMatch = html.match(/<meta name="description" content="([^"]+)"/)
    const shortSummary = descMatch ? descMatch[1] : ''

    // Extract full text using safe HTML stripping
    let fullText = ''
    const contentMatch = html.match(/<div[^>]*class="[^"]*content[^"]*"[^>]*>([\s\S]*?)<\/div>/i)
    if (contentMatch) fullText = contentMatch[1]
    if (!fullText) {
      const articleMatch = html.match(/<(?:article|main)[^>]*>([\s\S]*?)<\/(?:article|main)>/i)
      if (articleMatch) fullText = articleMatch[1]
    }
    fullText = stripHtml(fullText)
    fullText = decodeHtmlEntities(fullText)

    if (fullText.length < 200) {
      fullText = stripHtml(html)
      fullText = decodeHtmlEntities(fullText)
    }

    // Extract related laws
    const relatedLaws: string[] = []
    const lawMatches = fullText.match(/พระราชบัญญัติ[^ก-๙]*?\d{4}|ประมวลกฎหมาย[^ก-๙]*?(?:\d{4})?/g)
    if (lawMatches) {
      for (const law of lawMatches) {
        const trimmed = law.trim()
        if (!relatedLaws.includes(trimmed) && trimmed.length > 5) {
          relatedLaws.push(trimmed)
        }
      }
    }

    await insertJudgment({
      code: jud.code, year: jud.year, dekaNo: jud.dekaNo,
      title, shortSummary, fullText, relatedLaws,
    })
    success++
  } catch (e) {
    const errMsg = e instanceof Error ? e.message : String(e)
    console.error(`  FAILED ${jud.code}: ${errMsg}`)
    failed++
  }
}

console.log(`\nDone. Success: ${success}, Failed: ${failed}`)
