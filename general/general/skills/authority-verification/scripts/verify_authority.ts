#!/usr/bin/env node

type Args = {
  citation: string;
  highlightQuery: string;
  relatedCount: number;
};

function parseArgs(argv: string[]): Args {
  let citation = "";
  let highlightQuery = "holding";
  let relatedCount = 5;

  for (let i = 0; i < argv.length; i += 1) {
    const arg = argv[i];
    if (arg === "--citation") {
      citation = argv[i + 1] ?? "";
      i += 1;
      continue;
    }
    if (arg === "--highlight-query") {
      highlightQuery = argv[i + 1] ?? highlightQuery;
      i += 1;
      continue;
    }
    if (arg === "--related-count") {
      relatedCount = Number.parseInt(argv[i + 1] ?? "5", 10);
      i += 1;
    }
  }

  if (!citation) {
    throw new Error("usage: npx tsx scripts/verify_authority.ts --citation '531 U.S. 98' [--highlight-query holding] [--related-count 5]");
  }

  if (!Number.isFinite(relatedCount) || relatedCount < 1) {
    throw new Error("--related-count must be a positive integer");
  }

  return { citation, highlightQuery, relatedCount };
}

async function main() {
  const apiKey = process.env.CASEDEV_API_KEY;
  if (!apiKey) {
    throw new Error("CASEDEV_API_KEY is required");
  }

  const args = parseArgs(process.argv.slice(2));
  let CasedevModule: typeof import("casedev");
  try {
    CasedevModule = await import("casedev");
  } catch {
    throw new Error("Missing dependency: install with 'npm install casedev' and run with 'npx tsx'");
  }

  const Casedev = CasedevModule.default;
  const client = new Casedev({ apiKey });
  const verification = await client.legal.verify({ text: args.citation });

  const results = [];

  for (const item of verification.citations) {
    const result: Record<string, unknown> = {
      original: item.original,
      status: item.status,
    };

    if (item.status === "verified") {
      result.case = {
        name: item.case.name,
        url: item.case.url,
      };

      const [fullText, similar] = await Promise.all([
        client.legal.fullText({
          url: item.case.url,
          highlightQuery: args.highlightQuery,
          maxCharacters: 12000,
        }),
        client.legal.similar({
          url: item.case.url,
          numResults: args.relatedCount,
        }),
      ]);

      result.highlights = fullText.highlights ?? [];
      result.relatedAuthorities = similar.similarSources.map((source) => ({
        title: source.title,
        url: source.url,
      }));
    }

    if (item.status === "multiple_matches") {
      result.candidates = (item.candidates ?? []).map((candidate) => ({
        name: candidate.name,
        url: candidate.url,
      }));
    }

    results.push(result);
  }

  const report = {
    citation: args.citation,
    summary: {
      total: verification.summary.total,
      verified: verification.summary.verified,
      notFound: verification.summary.notFound,
      multipleMatches: verification.summary.multipleMatches,
    },
    results,
  };

  console.log(JSON.stringify(report, null, 2));
}

main().catch((error) => {
  const message = error instanceof Error ? error.message : String(error);
  console.error(message);
  process.exit(1);
});
