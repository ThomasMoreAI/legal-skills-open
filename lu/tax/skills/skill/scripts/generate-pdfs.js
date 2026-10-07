#!/usr/bin/env node
/**
 * generate-pdfs.js — Convertit les .md de ./out/ en PDF avec Puppeteer.
 * Suppose que generate-statements.js a déjà tourné.
 */

import fs from "node:fs";
import path from "node:path";
import { marked } from "marked";
import puppeteer from "puppeteer";

const OUT_DIR = "out";
const COMPANY_FILE = "company.json";

const CSS = `
  @page { size: A4; margin: 20mm; }
  body { font-family: Helvetica, Arial, sans-serif; font-size: 10pt; color: #222; }
  h1 { font-size: 18pt; border-bottom: 2px solid #ED2939; padding-bottom: 4pt; }
  h2 { font-size: 13pt; color: #00A1DE; margin-top: 16pt; }
  table { border-collapse: collapse; width: 100%; margin: 8pt 0; }
  th, td { border: 1px solid #ccc; padding: 4pt 6pt; text-align: left; }
  th { background: #f5f5f5; }
  td:nth-child(n+3) { text-align: right; font-variant-numeric: tabular-nums; }
  footer { font-size: 8pt; color: #888; margin-top: 24pt; border-top: 1px solid #eee; padding-top: 6pt; }
`;

async function main() {
  if (!fs.existsSync(OUT_DIR)) {
    console.error(`[ERREUR] ${OUT_DIR}/ n'existe pas. Lancez d'abord 'npm run statements'.`);
    process.exit(1);
  }
  const company = fs.existsSync(COMPANY_FILE) ? JSON.parse(fs.readFileSync(COMPANY_FILE, "utf8")) : {};
  const files = fs.readdirSync(OUT_DIR).filter((f) => f.endsWith(".md"));
  if (files.length === 0) {
    console.error(`[ERREUR] aucun .md dans ${OUT_DIR}/.`);
    process.exit(1);
  }
  const browser = await puppeteer.launch({ args: ["--no-sandbox"] });
  for (const f of files) {
    const md = fs.readFileSync(path.join(OUT_DIR, f), "utf8");
    const html = `<!doctype html><html lang="fr"><head><meta charset="utf-8"><style>${CSS}</style></head><body>${marked.parse(md)}<footer>${company.raisonSociale || ""} — RCS ${company.rcs || ""} — TVA ${company.matriculeTva || ""}</footer></body></html>`;
    const page = await browser.newPage();
    await page.setContent(html, { waitUntil: "networkidle0" });
    const pdf = path.join(OUT_DIR, f.replace(/\.md$/, ".pdf"));
    await page.pdf({ path: pdf, format: "A4", printBackground: true });
    console.log(`[OK] ${pdf}`);
    await page.close();
  }
  await browser.close();
}

main().catch((e) => { console.error(e); process.exit(1); });
