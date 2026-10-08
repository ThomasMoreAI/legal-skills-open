/**
 * Check Supreme Court website for new labor judgments.
 * Creates a GitHub Issue if new judgments are found.
 *
 * Uses the Supreme Court's public search API.
 */

const SC_BASE = 'https://www.supremecourt.or.th';

interface JudgmentSummary {
  caseNumber: string;
  caseYear: string;
  title: string;
  url: string;
}

async function checkSupremeCourt(): Promise<JudgmentSummary[]> {
  // The Supreme Court website has a search form at:
  // https://www.supremecourt.or.th/sc/judgment_search.php
  // We check the RSS feed (if available) or the latest judgments page.
  //
  // For now, we use a simplified approach: check the deka.supremecourt.or.th
  // API for the latest judgments with case_type = แรงงาน

  try {
    // Try the public API endpoint for latest judgments
    const resp = await fetch(`${SC_BASE}/sc/judgment_search.php?keyword=&case_type=1&search=Search`, {
      headers: { 'User-Agent': 'Panya-AI-Legal-Monitor/1.0' },
      signal: AbortSignal.timeout(30000),
    });

    if (!resp.ok) {
      console.log(`Supreme Court fetch failed: HTTP ${resp.status}`);
      console.log('Note: The Supreme Court website may require JavaScript rendering.');
      console.log('Falling back to checking our DB for the latest judgment year...');

      // Fallback: just report what year our latest judgment is from
      const dbUrl = process.env.DATABASE_URL;
      if (dbUrl && dbUrl.startsWith('libsql://')) {
        const token = process.env.TURSO_AUTH_TOKEN || '';
        const countResp = await fetch(`${dbUrl}/v2/pipeline`, {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            requests: [
              { type: 'execute', stmt: { sql: 'SELECT MAX(year) as max_year, COUNT(*) as total FROM judgments WHERE case_type = "แรงงาน"' } },
              { type: 'close' },
            ],
          }),
        });
        if (countResp.ok) {
          const data = await countResp.json();
          const rows = data.results?.[0]?.response?.result?.rows || [];
          if (rows.length > 0) {
            const maxYear = rows[0][0]?.value || 'unknown';
            const total = rows[0][1]?.value || '0';
            console.log(`Latest judgment year in DB: ${maxYear}`);
            console.log(`Total labor judgments in DB: ${total}`);
            console.log(`Current year (BE): ${new Date().getFullYear() + 543}`);
            console.log('To add new judgments, run: bun scripts/fetch_latest_judgments.ts');
          }
        }
      }
      return [];
    }

    // If we got HTML, try to extract judgment links
    const html = await resp.text();
    const judgments: JudgmentSummary[] = [];

    // Look for judgment links in the HTML
    const linkRegex = /href="([^"]*judgment[^"]*)"[^>]*>([^<]+)/gi;
    let match;
    while ((match = linkRegex.exec(html)) !== null) {
      const url = match[1].startsWith('http') ? match[1] : `${SC_BASE}${match[1]}`;
      const title = match[2].trim();
      if (title.length > 5) {
        judgments.push({
          caseNumber: '',
          caseYear: '',
          title,
          url,
        });
      }
    }

    return judgments.slice(0, 10); // Limit to 10
  } catch (e) {
    console.log(`Supreme Court check error: ${e instanceof Error ? e.message : String(e)}`);
    return [];
  }
}

async function createGitHubIssue(judgments: JudgmentSummary[]) {
  const token = process.env.GITHUB_TOKEN;
  if (!token) {
    console.log('GITHUB_TOKEN not set — skipping issue creation');
    return;
  }

  const repo = process.env.GITHUB_REPOSITORY || 'Siriwat08/Panya-AI';
  const dateStr = new Date().toLocaleDateString('th-TH', { year: 'numeric', month: 'long', day: 'numeric' });

  const body = judgments.map((j, i) => {
    return `### ${i + 1}. ${j.title}\n\n🔗 ${j.url}\n`;
  }).join('\n---\n\n');

  const issueBody = `## ⚖️ ฎีกาแรงงานใหม่ — ${dateStr}\n\nพบ ${judgments.length} คดีใหม่ที่น่าสนใจ:\n\n${body}\n\n---\n⚠️ กรุณาตรวจสอบและพิจารณานำเข้าระบบ Panya-AI\n\n_แจ้งโดย Panya-AI Legal Update Monitor_`;

  const resp = await fetch(`https://api.github.com/repos/${repo}/issues`, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json',
      'X-GitHub-Api-Version': '2022-11-28',
    },
    body: JSON.stringify({
      title: `⚖️ ฎีกาแรงงานใหม่ ${judgments.length} คดี — ${dateStr}`,
      body: issueBody,
      labels: ['legal-update', 'supremecourt'],
    }),
  });

  if (resp.ok) {
    const data = await resp.json();
    console.log(`Created issue #${data.number}: ${data.html_url}`);
  } else {
    console.log(`Failed to create issue: ${resp.status}`);
  }
}

// Main
console.log('Checking Supreme Court for new labor judgments...');
const judgments = await checkSupremeCourt();
console.log(`Found ${judgments.length} new judgments`);

if (judgments.length > 0) {
  await createGitHubIssue(judgments);
} else {
  console.log('No new judgments found. Database status reported above.');
}
