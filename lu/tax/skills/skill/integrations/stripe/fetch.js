#!/usr/bin/env node
/**
 * fetch.js — Récupère les charges Stripe (multi-comptes + Connect).
 * Sortie : data/transactions/stripe-<account>-<YYYY-MM>.json
 */

import fs from "node:fs";
import path from "node:path";
import Stripe from "stripe";

const COMPANY_FILE = "company.json";
if (!fs.existsSync(COMPANY_FILE)) {
  console.error(`[STRIPE] ${COMPANY_FILE} introuvable.`);
  process.exit(1);
}
const company = JSON.parse(fs.readFileSync(COMPANY_FILE, "utf8"));
const accounts = company.stripe?.accounts || [];
if (accounts.length === 0 && process.env.STRIPE_SECRET) {
  accounts.push({ name: "default", type: "standalone", envVar: "STRIPE_SECRET" });
}

if (accounts.length === 0) {
  console.error("[STRIPE] Aucun compte configuré (ni company.json#stripe.accounts ni STRIPE_SECRET).");
  process.exit(1);
}

function normalize(c, accountName) {
  return {
    id: `stripe-${c.id}`,
    date: new Date(c.created * 1000).toISOString().slice(0, 10),
    libelle: c.description || c.statement_descriptor || `Stripe ${accountName} ${c.id}`,
    montant: c.amount / 100,
    devise: c.currency.toUpperCase(),
    fee: (c.application_fee_amount || 0) / 100,
    statut: c.status,
    client: c.billing_details?.email || c.customer || null,
    categorie: "encaissement_stripe",
  };
}

async function fetchAccount(account) {
  let secret;
  let extraOpts = {};
  if (account.type === "connect") {
    secret = process.env[account.platformEnvVar || "STRIPE_PLATFORM_SECRET"];
    extraOpts = { stripeAccount: account.stripeAccountId };
  } else {
    secret = process.env[account.envVar || "STRIPE_SECRET"];
  }
  if (!secret) {
    console.error(`[STRIPE/${account.name}] clé API absente (${account.envVar || account.platformEnvVar}).`);
    return [];
  }
  const stripe = new Stripe(secret);
  const charges = [];
  for await (const c of stripe.charges.list({ limit: 100 }, extraOpts)) {
    charges.push(normalize(c, account.name));
  }
  return charges;
}

async function main() {
  fs.mkdirSync(path.join("data", "transactions"), { recursive: true });
  const stamp = new Date().toISOString().slice(0, 7);
  for (const account of accounts) {
    console.log(`[STRIPE/${account.name}] récupération...`);
    const txs = await fetchAccount(account);
    const out = path.join("data", "transactions", `stripe-${account.name}-${stamp}.json`);
    fs.writeFileSync(out, JSON.stringify(txs, null, 2));
    console.log(`[STRIPE/${account.name}] ${txs.length} charges -> ${out}`);
  }
}

main().catch((e) => { console.error(e); process.exit(1); });
