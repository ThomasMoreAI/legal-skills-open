#!/usr/bin/env node
/**
 * generate-facture-lux.js — Génère une facture HTML + PDF conforme LU.
 * Lit company.json et un fichier facture.json, sort facture-<num>.pdf dans ./out/.
 *
 * Usage : node scripts/generate-facture-lux.js facture.json
 */

import fs from "node:fs";
import path from "node:path";
import puppeteer from "puppeteer";

function fmt(n) {
  return new Intl.NumberFormat("fr-LU", { style: "currency", currency: "EUR", minimumFractionDigits: 2 }).format(n);
}

async function main() {
  const file = process.argv[2];
  if (!file || !fs.existsSync(file)) {
    console.error("Usage : node scripts/generate-facture-lux.js <facture.json>");
    process.exit(1);
  }
  const company = fs.existsSync("company.json") ? JSON.parse(fs.readFileSync("company.json", "utf8")) : {};
  const f = JSON.parse(fs.readFileSync(file, "utf8"));
  // Fusion company.json -> facture.vendeur si vendeur absent
  if (!f.vendeur) f.vendeur = {
    raisonSociale: company.raisonSociale,
    adresse: company.adresse,
    matriculeTva: company.matriculeTva,
    rcs: company.rcs,
    iban: company.iban,
    bic: company.bic,
  };

  const lignesHtml = (f.lignes || [])
    .map((l) => `<tr><td>${l.libelle}</td><td style="text-align:right">${l.quantite}</td><td style="text-align:right">${fmt(l.puHT)}</td><td style="text-align:right">${fmt(l.quantite * l.puHT)}</td></tr>`)
    .join("");

  const html = `<!doctype html><html lang="fr"><head><meta charset="utf-8"><style>
    @page { size: A4; margin: 20mm; }
    body { font-family: Helvetica, Arial, sans-serif; font-size: 10pt; color: #222; }
    .head { display: flex; justify-content: space-between; margin-bottom: 24pt; }
    .vendeur, .client { width: 45%; }
    h1 { color: #ED2939; font-size: 22pt; margin: 0; }
    table { border-collapse: collapse; width: 100%; margin: 12pt 0; }
    th, td { border: 1px solid #ccc; padding: 5pt 7pt; }
    th { background: #f5f5f5; text-align: left; }
    .totaux { width: 50%; margin-left: auto; }
    .totaux td { border: none; padding: 3pt 7pt; }
    .totaux .ttc { font-weight: bold; border-top: 2px solid #00A1DE; }
    footer { font-size: 8pt; color: #666; margin-top: 24pt; border-top: 1px solid #eee; padding-top: 6pt; }
    .peppol { color: #008751; font-size: 9pt; }
  </style></head><body>
    <h1>FACTURE ${f.numero}</h1>
    <p>Date d'émission : ${f.dateEmission} — Date de livraison : ${f.dateLivraison}</p>
    <div class="head">
      <div class="vendeur"><b>${f.vendeur.raisonSociale}</b><br>${f.vendeur.adresse || ""}<br>RCS : ${f.vendeur.rcs}<br>TVA : ${f.vendeur.matriculeTva}</div>
      <div class="client"><b>Client :</b><br>${f.client.raisonSociale}<br>${f.client.adresse || ""}${f.client.matriculeTva ? `<br>TVA : ${f.client.matriculeTva}` : ""}</div>
    </div>
    <table>
      <thead><tr><th>Libellé</th><th>Quantité</th><th>PU HT</th><th>Total HT</th></tr></thead>
      <tbody>${lignesHtml}</tbody>
    </table>
    <table class="totaux">
      <tr><td>Total HT</td><td style="text-align:right">${fmt(f.totalHT)}</td></tr>
      <tr><td>TVA ${f.tauxTva}%</td><td style="text-align:right">${fmt(f.montantTva)}</td></tr>
      <tr class="ttc"><td>Total TTC</td><td style="text-align:right">${fmt(f.totalTtc)}</td></tr>
    </table>
    <p><b>Modalités de paiement :</b> ${f.modalitesPaiement || "30 jours à compter de la date d'émission"}<br>IBAN : ${f.vendeur.iban || ""} — BIC : ${f.vendeur.bic || ""}</p>
    ${f.peppol?.participantId ? `<p class="peppol">Identifiant Peppol : ${f.peppol.participantId} (e-invoicing B2G conforme loi du 13 décembre 2021).</p>` : ""}
    <footer>Mention TVA : ${f.tauxTva === 0 ? "Exonération TVA — préciser le motif (art. 43, art. 44 LTVA, ou autoliquidation art. 196 directive 2006/112/CE)" : `TVA luxembourgeoise ${f.tauxTva}%`}.<br>En cas de retard, intérêts de retard au taux légal LU + indemnité forfaitaire 40 € (loi du 18 avril 2004 modifiée).</footer>
  </body></html>`;

  fs.mkdirSync("out", { recursive: true });
  const browser = await puppeteer.launch({ args: ["--no-sandbox"] });
  const page = await browser.newPage();
  await page.setContent(html, { waitUntil: "networkidle0" });
  const out = path.join("out", `facture-${f.numero}.pdf`);
  await page.pdf({ path: out, format: "A4", printBackground: true });
  await browser.close();
  console.log(`[OK] ${out}`);
}

main().catch((e) => { console.error(e); process.exit(1); });
