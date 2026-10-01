#!/usr/bin/env bun
import { existsSync } from "node:fs";
import { mkdir, readFile, writeFile } from "node:fs/promises";
import { join } from "node:path";
import { createInterface } from "node:readline/promises";

const DOCUMENT_KEYS = [
	"privacy_policy",
	"terms",
	"cookies",
	"aup",
	"dpa",
	"ccpa_opt_out",
] as const;

type DocumentKey = (typeof DOCUMENT_KEYS)[number];
type YesNoUnknown = "yes" | "no" | "unknown";

interface DataInventoryItem {
	category: string;
	examples?: string;
	source?: string;
	purpose?: string;
	legal_basis?: string;
	recipients?: string;
	retention?: string;
}

interface VendorItem {
	name: string;
	purpose?: string;
	data?: string;
	role?: string;
	locations?: string;
	privacy_url?: string;
}

interface CookieItem {
	name: string;
	provider?: string;
	purpose?: string;
	category?: string;
	duration?: string;
	first_or_third_party?: string;
}

interface CaliforniaConfig {
	applies?: YesNoUnknown;
	sells?: YesNoUnknown;
	shares?: YesNoUnknown;
	uses_sensitive_personal_information?: YesNoUnknown;
	honors_gpc?: YesNoUnknown;
	request_url?: string;
	opt_out_url?: string;
	limit_use_url?: string;
}

interface Config {
	company_name?: string;
	domain?: string;
	contact_email?: string;
	support_email?: string;
	address?: string;
	jurisdiction?: string;
	currency?: string;
	effective_date?: string;
	version?: string;
	service_description?: string;
	features?: string[];
	service_type?: string;
	min_age?: string;
	has_free_tier?: boolean;
	billing_cycle?: string;
	refund_policy?: string;
	refund_days?: string;
	processing_role?: "controller" | "processor" | "both" | "unknown";
	data_inventory?: DataInventoryItem[];
	vendors?: VendorItem[];
	cookies?: CookieItem[];
	uses_cookies?: boolean;
	cookie_categories?: string[];
	cookie_settings_url?: string;
	data_retention_schedule?: string;
	data_retention_days?: string;
	rights_request_process?: string;
	international_transfer_details?: string;
	security_summary?: string[];
	children_position?: string;
	jurisdictions?: string[];
	gdpr_rep_email?: string;
	ccpa_agent_email?: string;
	california?: CaliforniaConfig;
	third_parties?: {
		payment?: string;
		hosting?: string;
		analytics?: string;
		email?: string;
		support?: string;
	};
	documents?: DocumentKey[];
}

interface DocumentDefinition {
	name: string;
	key: DocumentKey;
	default?: boolean;
	condition?: (config: Config) => boolean;
}

interface GeneratedFile {
	filename: string;
	unresolved: string[];
}

const DOCUMENTS: DocumentDefinition[] = [
	{ name: "Privacy Notice", key: "privacy_policy", default: true },
	{ name: "Terms of Service", key: "terms", default: true },
	{
		name: "Cookie Notice",
		key: "cookies",
		condition: (config) => Boolean(config.uses_cookies || config.cookies?.length),
	},
	{ name: "Acceptable Use Policy", key: "aup", default: false },
	{
		name: "Data Processing Agreement",
		key: "dpa",
		condition: (config) => ["processor", "both"].includes(config.processing_role ?? ""),
	},
	{
		name: "California Opt-Out Notice",
		key: "ccpa_opt_out",
		condition: (config) =>
			config.california?.applies === "yes" &&
			(config.california.sells === "yes" || config.california.shares === "yes"),
	},
];

const TEMPLATE_MAP: Record<DocumentKey, string> = {
	privacy_policy: "privacy-policy-global.md",
	terms: "terms-of-service-saas.md",
	cookies: "cookie-policy.md",
	aup: "acceptable-use-policy.md",
	dpa: "data-processing-agreement.md",
	ccpa_opt_out: "ccpa-opt-out-link.md",
};

const OUTPUT_FILENAMES: Record<DocumentKey, string> = {
	privacy_policy: "privacy-notice.md",
	terms: "terms-of-service.md",
	cookies: "cookie-notice.md",
	aup: "acceptable-use-policy.md",
	dpa: "data-processing-agreement.md",
	ccpa_opt_out: "california-opt-out-notice.md",
};

function isDocumentKey(value: string): value is DocumentKey {
	return (DOCUMENT_KEYS as readonly string[]).includes(value);
}

function escapeCell(value: unknown): string {
	return String(value ?? "")
		.replaceAll("|", "\\|")
		.replaceAll("\n", "<br>")
		.trim();
}

function markdownTable(headers: string[], rows: unknown[][], missingLabel: string): string {
	if (rows.length === 0) return `[[REVIEW: ${missingLabel}]]`;
	const header = `| ${headers.join(" | ")} |`;
	const divider = `| ${headers.map(() => "---").join(" | ")} |`;
	const body = rows.map((row) => `| ${row.map(escapeCell).join(" | ")} |`).join("\n");
	return `${header}\n${divider}\n${body}`;
}

function placeholder(label: string, value?: string): string {
	const trimmed = value?.trim();
	return trimmed || `[[REVIEW: SUPPLY ${label}]]`;
}

function unresolvedMarkers(content: string): string[] {
	const tokens = [
		...content.matchAll(/\[[A-Z][A-Z0-9_/-]{2,}\]/g),
		...content.matchAll(/\[\[REVIEW:[^\]]+\]\]/g),
	].map((match) => match[0]);
	return [...new Set(tokens)].sort();
}

class LegalGenerator {
	private readonly outputDir = join(import.meta.dir, "../output");
	private readonly templateDir = join(import.meta.dir, "../templates");
	private config: Config = {};
	private readonly warnings: string[] = [];
	private readonly rl = createInterface({ input: process.stdin, output: process.stdout });

	async loadConfig(path: string): Promise<void> {
		const content = await readFile(path, "utf8");
		const parsed: unknown = JSON.parse(content);
		if (typeof parsed !== "object" || parsed === null || Array.isArray(parsed)) {
			throw new Error("Configuration must be a JSON object");
		}
		this.config = parsed as Config;
		if (this.config.documents) {
			const invalid = this.config.documents.filter((key) => !isDocumentKey(String(key)));
			if (invalid.length > 0) throw new Error(`Unknown document keys: ${invalid.join(", ")}`);
		}
		console.log(`Loaded configuration from ${path}`);
	}

	private async getInput(
		prompt: string,
		options: { required?: boolean; defaultValue?: string } = {},
	): Promise<string> {
		const { required = false, defaultValue } = options;
		const suffix = defaultValue ? ` [${defaultValue}]` : required ? " [required]" : " [optional]";
		while (true) {
			const answer = (await this.rl.question(`${prompt}${suffix}: `)).trim();
			if (answer) return answer;
			if (defaultValue) return defaultValue;
			if (!required) return "";
			console.log("This field is required; do not invent a value.");
		}
	}

	private async getMultiline(prompt: string): Promise<string> {
		console.log(`${prompt} (blank line to finish):`);
		const lines: string[] = [];
		while (true) {
			const line = await this.rl.question("");
			if (!line.trim()) break;
			lines.push(line.trim());
		}
		return lines.join("\n");
	}

	private async getChoice<T extends string>(prompt: string, choices: readonly T[]): Promise<T> {
		console.log(`\n${prompt}`);
		choices.forEach((choice, index) => console.log(`  ${index + 1}. ${choice}`));
		while (true) {
			const answer = await this.rl.question("Enter choice (number): ");
			const index = Number.parseInt(answer.trim(), 10) - 1;
			const choice = choices[index];
			if (choice) return choice;
			console.log(`Enter a number between 1 and ${choices.length}.`);
		}
	}

	private async getYesNo(prompt: string, defaultValue = false): Promise<boolean> {
		const answer = (await this.rl.question(`${prompt} [${defaultValue ? "Y/n" : "y/N"}]: `))
			.trim()
			.toLowerCase();
		if (!answer) return defaultValue;
		return answer === "y" || answer === "yes";
	}

	private async collectInteractiveConfig(): Promise<void> {
		console.log("\nCreate an evidence-based draft. Leave uncertain legal or operational facts blank.");
		this.config.company_name = await this.getInput("Legal entity/company name", {
			required: true,
		});
		this.config.domain = await this.getInput("Canonical website domain", { required: true });
		this.config.contact_email = await this.getInput("Privacy/legal contact email", {
			required: true,
		});
		this.config.support_email = await this.getInput("Support email");
		this.config.address = await this.getMultiline("Legal/business address, if publishable");
		this.config.effective_date = await this.getInput(
			"Intended effective date (for example, 2026-08-01)",
		);
		this.config.jurisdiction = await this.getInput(
			"Proposed governing law/forum (leave blank for counsel)",
		);
		this.config.service_description = await this.getMultiline(
			"Describe the service and intended users",
		);
		this.config.min_age = await this.getInput(
			"Minimum age only if supported by product design and counsel",
		);
		this.config.processing_role = await this.getChoice(
			"Privacy role for customer data (select unknown if not assessed)",
			["controller", "processor", "both", "unknown"] as const,
		);
		this.config.data_retention_schedule = await this.getMultiline(
			"Actual retention schedule by data category, including backups",
		);
		this.config.uses_cookies = await this.getYesNo(
			"Does the deployed product use cookies or similar device storage?",
		);
		this.config.cookie_settings_url = await this.getInput(
			"Cookie/preference settings URL, if implemented",
		);

		const lawSelections: string[] = [];
		for (const [label, key] of [
			["EU GDPR", "gdpr"],
			["UK GDPR/PECR", "uk-gdpr"],
			["Canada privacy law", "pipeda"],
			["Brazil LGPD", "lgpd"],
		] as const) {
			if (await this.getYesNo(`Has applicability of ${label} been assessed as relevant?`)) {
				lawSelections.push(key);
			}
		}
		this.config.jurisdictions = lawSelections;
		const californiaApplies = await this.getChoice(
			"Has CCPA/CPRA applicability been assessed?",
			["yes", "no", "unknown"] as const,
		);
		this.config.california = { applies: californiaApplies };
		if (californiaApplies === "yes") {
			this.config.california.sells = await this.getChoice(
				"Does the assessed practice constitute a sale?",
				["yes", "no", "unknown"] as const,
			);
			this.config.california.shares = await this.getChoice(
				"Does the assessed practice constitute sharing for cross-context behavioral advertising?",
				["yes", "no", "unknown"] as const,
			);
			this.config.california.honors_gpc = await this.getChoice(
				"Does the deployed product honor applicable Global Privacy Control signals?",
				["yes", "no", "unknown"] as const,
			);
			this.config.california.request_url = await this.getInput(
				"California rights request URL",
			);
			this.config.california.opt_out_url = await this.getInput(
				"Do Not Sell or Share URL, if applicable and implemented",
			);
		}

		this.config.third_parties = {
			payment: await this.getInput("Payment processor actually used"),
			hosting: await this.getInput("Hosting provider actually used"),
			analytics: await this.getInput("Analytics provider actually used"),
			email: await this.getInput("Email provider actually used"),
			support: await this.getInput("Support provider actually used"),
		};
		await this.selectDocuments();
	}

	private async selectDocuments(): Promise<void> {
		this.config.documents = [];
		for (const document of DOCUMENTS) {
			const relevant = document.condition ? document.condition(this.config) : true;
			if (!relevant && !document.default) continue;
			if (await this.getYesNo(`Generate ${document.name}?`, document.default ?? true)) {
				this.config.documents.push(document.key);
			}
		}
		if (this.config.documents.length === 0) {
			throw new Error("No documents selected");
		}
	}

	private validateConfiguration(): void {
		for (const [label, value] of [
			["company_name", this.config.company_name],
			["domain", this.config.domain],
			["contact_email", this.config.contact_email],
			["service_description", this.config.service_description],
		] as const) {
			if (!value?.trim()) this.warnings.push(`Missing core field: ${label}`);
		}

		if (!this.config.data_inventory?.length) {
			this.warnings.push("No data inventory supplied; privacy disclosures require manual completion.");
		}
		if (!this.config.vendors?.length) {
			this.warnings.push("No verified vendor/subprocessor inventory supplied.");
		}
		if (!this.config.data_retention_schedule?.trim() && !this.config.data_retention_days) {
			this.warnings.push("No evidence-based retention schedule supplied.");
		}
		if (this.config.documents?.includes("dpa") && !["processor", "both"].includes(this.config.processing_role ?? "")) {
			this.warnings.push("DPA selected without a confirmed processor role.");
		}
		if (this.config.documents?.includes("ccpa_opt_out")) {
			if (this.config.california?.applies !== "yes") {
				this.warnings.push("California opt-out notice selected without confirmed CCPA/CPRA applicability.");
			}
			if (
				this.config.california?.sells !== "yes" &&
				this.config.california?.shares !== "yes"
			) {
				this.warnings.push("California opt-out notice selected without a confirmed sale or sharing practice.");
			}
			if (this.config.california?.honors_gpc !== "yes") {
				this.warnings.push("GPC implementation is not verified as operational.");
			}
		}
	}

	private replacements(): Map<string, string> {
		const retention =
			this.config.data_retention_schedule?.trim() ||
			(this.config.data_retention_days
				? `${this.config.data_retention_days} days (legacy global value; replace with category-specific periods)`
				: undefined);
		const vendors = this.config.vendors ?? [];
		const legacyVendors: VendorItem[] = Object.entries(this.config.third_parties ?? {})
			.filter((entry): entry is [string, string] => Boolean(entry[1]?.trim()))
			.map(([purpose, name]) => ({ name, purpose }));
		const vendorRows = [...vendors, ...legacyVendors];
		const dataInventory = this.config.data_inventory ?? [];
		const cookies = this.config.cookies ?? [];
		const california = this.config.california;

		const dataTable = markdownTable(
			["Category", "Examples", "Source", "Purpose", "Legal basis", "Recipients", "Retention"],
			dataInventory.map((item) => [
				item.category,
				item.examples,
				item.source,
				item.purpose,
				item.legal_basis,
				item.recipients,
				item.retention,
			]),
			"ADD THE VERIFIED DATA INVENTORY",
		);
		const purposeTable = markdownTable(
			["Purpose", "Data", "Legal basis/condition", "Outcome"],
			dataInventory.map((item) => [
				item.purpose,
				item.category,
				item.legal_basis,
				"[[REVIEW: EXPLAIN THE OPERATIONAL OUTCOME]]",
			]),
			"ADD PURPOSES AND APPLICABLE LEGAL BASES",
		);
		const vendorTable = markdownTable(
			["Provider", "Purpose", "Data", "Role", "Locations", "Privacy information"],
			vendorRows.map((vendor) => [
				vendor.name,
				vendor.purpose,
				vendor.data,
				vendor.role,
				vendor.locations,
				vendor.privacy_url,
			]),
			"ADD VERIFIED VENDORS, ROLES, DATA, LOCATIONS, AND LINKS",
		);
		const cookieTable = markdownTable(
			["Technology", "Provider", "Purpose", "Category", "Duration", "Party"],
			cookies.map((cookie) => [
				cookie.name,
				cookie.provider,
				cookie.purpose,
				cookie.category,
				cookie.duration,
				cookie.first_or_third_party,
			]),
			"ADD AN ACTUAL COOKIE AND SIMILAR-TECHNOLOGY INVENTORY",
		);
		const securitySummary = this.config.security_summary?.length
			? this.config.security_summary.map((control) => `- ${control}`).join("\n")
			: "[[REVIEW: DESCRIBE ONLY VERIFIED SECURITY CONTROLS]]";
		const californiaDisclosure = california
			? `Applicability: **${california.applies ?? "unknown"}**  \nSale: **${california.sells ?? "unknown"}**  \nSharing: **${california.shares ?? "unknown"}**  \nSensitive-personal-information limitation relevant: **${california.uses_sensitive_personal_information ?? "unknown"}**  \nGPC operationally honored: **${california.honors_gpc ?? "unknown"}**  \nRights request: ${placeholder("CALIFORNIA RIGHTS REQUEST URL", california.request_url)}  \nOpt-out: ${placeholder("DO NOT SELL OR SHARE URL", california.opt_out_url)}  \nLimit-use request: ${placeholder("LIMIT USE URL IF APPLICABLE", california.limit_use_url)}`
			: "[[REVIEW: ASSESS CCPA/CPRA APPLICABILITY, SALE, SHARING, SENSITIVE DATA, AND GPC BEFORE PUBLISHING]]";

		return new Map([
			["[COMPANY_NAME]", placeholder("LEGAL ENTITY NAME", this.config.company_name)],
			["[DOMAIN]", placeholder("CANONICAL DOMAIN", this.config.domain)],
			["[CONTACT_EMAIL]", placeholder("PRIVACY/LEGAL CONTACT EMAIL", this.config.contact_email)],
			["[SUPPORT_EMAIL]", placeholder("SUPPORT EMAIL", this.config.support_email)],
			["[COMPANY_ADDRESS]", placeholder("COMPANY ADDRESS", this.config.address)],
			["[JURISDICTION]", placeholder("GOVERNING LAW/FORUM AFTER COUNSEL REVIEW", this.config.jurisdiction)],
			["[CURRENCY]", placeholder("CURRENCY", this.config.currency)],
			["[EFFECTIVE_DATE]", placeholder("EFFECTIVE DATE", this.config.effective_date)],
			["[VERSION]", this.config.version?.trim() || "DRAFT"],
			["[SERVICE_DESCRIPTION]", placeholder("SERVICE DESCRIPTION", this.config.service_description)],
			["[MIN_AGE]", placeholder("AGE POSITION AFTER PRODUCT AND LEGAL REVIEW", this.config.min_age)],
			["[RETENTION_PERIOD]", placeholder("RETENTION SCHEDULE", retention)],
			["[RETENTION_SCHEDULE]", placeholder("RETENTION SCHEDULE", retention)],
			["[REFUND_PERIOD]", placeholder("REFUND PERIOD", this.config.refund_days)],
			["[REFUND_POLICY]", placeholder("REFUND POLICY", this.config.refund_policy)],
			["[BILLING_CYCLE]", placeholder("BILLING TERMS", this.config.billing_cycle)],
			["[PAYMENT_PROCESSOR]", placeholder("PAYMENT PROCESSOR", this.config.third_parties?.payment)],
			["[HOSTING_PROVIDER]", placeholder("HOSTING PROVIDER", this.config.third_parties?.hosting)],
			["[ANALYTICS_PROVIDER]", placeholder("ANALYTICS PROVIDER", this.config.third_parties?.analytics)],
			["[EMAIL_PROVIDER]", placeholder("EMAIL PROVIDER", this.config.third_parties?.email)],
			["[SUPPORT_TOOL]", placeholder("SUPPORT PROVIDER", this.config.third_parties?.support)],
			["[GDPR_REP_EMAIL]", placeholder("EU/UK REPRESENTATIVE DETAILS IF REQUIRED", this.config.gdpr_rep_email)],
			["[CCPA_AGENT_EMAIL]", placeholder("CALIFORNIA REQUEST CONTACT", this.config.ccpa_agent_email ?? this.config.contact_email)],
			["[FEATURE_1]", placeholder("FEATURE 1", this.config.features?.[0])],
			["[FEATURE_2]", placeholder("FEATURE 2", this.config.features?.[1])],
			["[FEATURE_3]", placeholder("FEATURE 3", this.config.features?.[2])],
			["[DATA_INVENTORY_TABLE]", dataTable],
			["[PROCESSING_PURPOSE_TABLE]", purposeTable],
			["[VENDOR_TABLE]", vendorTable],
			["[COOKIE_INVENTORY_TABLE]", cookieTable],
			["[CALIFORNIA_DISCLOSURE]", californiaDisclosure],
			["[RIGHTS_REQUEST_PROCESS]", placeholder("RIGHTS REQUEST AND APPEAL PROCESS", this.config.rights_request_process)],
			["[TRANSFER_DETAILS]", placeholder("INTERNATIONAL TRANSFER LOCATIONS AND MECHANISMS", this.config.international_transfer_details)],
			["[SECURITY_SUMMARY]", securitySummary],
			["[CHILDREN_POSITION]", placeholder("CHILDREN/AGE POSITION", this.config.children_position)],
			["[COOKIE_SETTINGS_URL]", placeholder("COOKIE SETTINGS URL", this.config.cookie_settings_url)],
			["[PROCESSING_ROLE]", this.config.processing_role ?? "unknown"],
			["[PROCESSING_DETAILS_TABLE]", dataTable],
			["[SUBPROCESSOR_TABLE]", vendorTable],
			["[TOM_SUMMARY]", securitySummary],
		]);
	}

	private async generateDocument(key: DocumentKey): Promise<{ content: string; unresolved: string[] }> {
		const templatePath = join(this.templateDir, TEMPLATE_MAP[key]);
		if (!existsSync(templatePath)) throw new Error(`Missing template: ${templatePath}`);
		let content = await readFile(templatePath, "utf8");
		for (const [token, value] of this.replacements()) content = content.replaceAll(token, value);

		return { content, unresolved: unresolvedMarkers(content) };
	}

	private async generateAll(): Promise<GeneratedFile[]> {
		await mkdir(this.outputDir, { recursive: true });
		const generated: GeneratedFile[] = [];
		for (const key of this.config.documents ?? []) {
			const { content, unresolved } = await this.generateDocument(key);
			const filename = OUTPUT_FILENAMES[key];
			await writeFile(join(this.outputDir, filename), content, "utf8");
			generated.push({ filename, unresolved });
			console.log(`Generated draft: ${filename}`);
		}
		return generated;
	}

	private async writeReviewReport(files: GeneratedFile[]): Promise<void> {
		const lines = [
			"# Legal Draft Review Report",
			"",
			`Generated: ${new Date().toISOString()}`,
			"",
			"## Configuration Warnings",
			"",
			...(this.warnings.length > 0
				? this.warnings.map((warning) => `- ${warning}`)
				: ["- No generator-level warnings."]),
			"",
			"## Unresolved Markers",
			"",
		];
		for (const file of files) {
			lines.push(`### ${file.filename}`, "");
			lines.push(
				...(file.unresolved.length > 0
					? file.unresolved.map((marker) => `- \`${marker}\``)
					: ["- No syntactic markers found; perform substantive factual and legal review."]),
				"",
			);
		}
		lines.push(
			"## Required Product-to-Policy Tests",
			"",
			"- Verify every SDK, cookie, storage mechanism, data category, purpose, recipient, role, location, and retention rule.",
			"- Test consent and preference withdrawal before and after nonessential technology loads.",
			"- Test access, correction, deletion, export, objection/opt-out, appeal, and identity-verification workflows that are actually offered or required.",
			"- Verify Global Privacy Control handling when California opt-out obligations apply.",
			"- Reconcile trials, renewal, refunds, cancellation, suspension, deletion, and user-content terms with the deployed product.",
			"- Review international-transfer mechanisms, vendor contracts, subprocessors, security statements, age design, regulated data, and incident obligations.",
			"- Obtain qualified counsel review before publication or customer signature.",
			"",
		);
		await writeFile(join(this.outputDir, "REVIEW-REPORT.md"), `${lines.join("\n")}\n`, "utf8");
	}

	async run(configPath?: string): Promise<void> {
		console.log("\nSaaS legal drafting assistant");
		console.log();
		try {
			if (configPath) await this.loadConfig(configPath);
			else await this.collectInteractiveConfig();
			if (!this.config.documents?.length) {
				throw new Error("Configuration must select at least one document");
			}
			this.validateConfiguration();
			const files = await this.generateAll();
			await this.writeReviewReport(files);
			console.log(`\nGenerated ${files.length} draft(s) and REVIEW-REPORT.md in ${this.outputDir}`);
		} finally {
			this.rl.close();
		}
	}
}

if (import.meta.main) {
	try {
		await new LegalGenerator().run(process.argv[2]);
	} catch (error) {
		console.error("\nGeneration failed:", error);
		process.exitCode = 1;
	}
}
