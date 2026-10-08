/**
 * Check Ratchakitcha (Royal Gazette) RSS for new laws.
 * Creates a GitHub Issue if new labor/civil/criminal laws are found.
 *
 * RSS source: https://ratchakitcha.soc.go.th/RATCHAKICHA/FEED/RSS
 */

import { stripHtml, truncateText } from '../src/lib/sanitize';

const RSS_URL = 'https://ratchakitcha.soc.go.th/RATCHAKICHA/FEED/RSS';
const KEYWORDS = [
  'แรงงาน', 'คุ้มครองแรงงาน', 'ประกันสังคม', 'เงินทดแทน',
  'ค่าจ้างขั้นต่ำ', 'สหภาพแรงงาน', 'พนักงาน', 'ลูกจ้าง', 'นายจ้าง',
  'คอมพิวเตอร์', 'ข้อมูลส่วนบุคคล', 'PDPA',
  'ประมวลกฎหมายแพ่ง', 'ประมวลกฎหมายอาญา',
];

interface RSSItem {
  title: string;
  link: string;
  pubDate: string;
  description: string;
}

async function fetchRSS(): Promise<RSSItem[]> {
  try {
    const resp = await fetch(RSS_URL, {
      headers: { 'User-Agent': 'Panya-AI-Legal-Monitor/1.0' },
      signal: AbortSignal.timeout(30000),
    });
    if (!resp.ok) {
      console.log(`RSS fetch failed: HTTP ${resp.status}`);
      return [];
    }
    const xml = await resp.text();
    // Parse XML items (simple regex — RSS is well-structured)
    const items: RSSItem[] = [];
    const itemRegex = /<item>([\s\S]*?)<\/item>/gi;
    const titleRegex = /<title>(?:<!\[CDATA\[)?([\s\S]*?)(?:\]\]>)?<\/title>/i;
    const linkRegex = /<link>([\s\S]*?)<\/link>/i;
    const dateRegex = /<pubDate>([\s\S]*?)<\/pubDate>/i;
    const descRegex = /<description>(?:<!\[CDATA\[)?([\s\S]*?)(?:\]\]>)?<\/description>/i;

    let match;
    while ((match = itemRegex.exec(xml)) !== null) {
      const block = match[1];
      const title = titleRegex.exec(block)?.[1]?.trim() || '';
      const link = linkRegex.exec(block)?.[1]?.trim() || '';
      const pubDate = dateRegex.exec(block)?.[1]?.trim() || '';
      const description = descRegex.exec(block)?.[1]?.trim() || '';
      items.push({ title, link, pubDate, description });
    }
    return items;
  } catch (e) {
    console.log(`RSS fetch error: ${e instanceof Error ? e.message : String(e)}`);
    return [];
  }
}

function filterRelevant(items: RSSItem[]): RSSItem[] {
  return items.filter(item => {
    const text = (item.title + ' ' + item.description).toLowerCase();
    return KEYWORDS.some(kw => text.includes(kw));
  });
}

async function createGitHubIssue(items: RSSItem[]) {
  const token = process.env.GITHUB_TOKEN;
  if (!token) {
    console.log('GITHUB_TOKEN not set — skipping issue creation');
    return;
  }

  const repo = process.env.GITHUB_REPOSITORY || 'Siriwat08/Panya-AI';
  const dateStr = new Date().toLocaleDateString('th-TH', { year: 'numeric', month: 'long', day: 'numeric' });

  const body = items.map((item, i) => {
    // Use the CodeQL-safe stripHtml() helper instead of regex-based stripping.
    // The previous `/<[^>]+>/g` pattern was flagged as "Incomplete multi-character
    // sanitization" because it skipped HTML comments, CDATA sections, <script>
    // blocks, and undecoded HTML entities.
    const title = stripHtml(item.title);
    const desc = truncateText(stripHtml(item.description), 200);
    return `### ${i + 1}. ${title}\n\n📅 ${item.pubDate}\n🔗 ${item.link}\n\n> ${desc}\n`;
  }).join('\n---\n\n');

  const issueBody = `## 📢 กฎหมายใหม่จากราชกิจจานุเบกษา — ${dateStr}\n\nพบ ${items.length} ฉบับที่เกี่ยวข้องกับระบบ Panya-AI:\n\n${body}\n\n---\n⚠️ กรุณาตรวจสอบและพิจารณานำเข้าระบบหากจำเป็น\n\n_แจ้งโดย Panya-AI Legal Update Monitor_`;

  const resp = await fetch(`https://api.github.com/repos/${repo}/issues`, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json',
      'X-GitHub-Api-Version': '2022-11-28',
    },
    body: JSON.stringify({
      title: `📢 กฎหมายใหม่ ${items.length} ฉบับ — ${dateStr}`,
      body: issueBody,
      labels: ['legal-update', 'ratchakitcha'],
    }),
  });

  if (resp.ok) {
    const data = await resp.json();
    console.log(`Created issue #${data.number}: ${data.html_url}`);
  } else {
    console.log(`Failed to create issue: ${resp.status} ${await resp.text()}`);
  }
}

// Main
console.log('Checking Ratchakitcha RSS for new laws...');
const items = await fetchRSS();
console.log(`Found ${items.length} total items in RSS feed`);

const relevant = filterRelevant(items);
console.log(`Found ${relevant.length} relevant items`);

if (relevant.length > 0) {
  await createGitHubIssue(relevant);
} else {
  console.log('No relevant new laws found today.');
}
