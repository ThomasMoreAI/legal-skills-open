(() => {
  "use strict";
  const payload = JSON.parse(document.getElementById("catalog-data").textContent);
  const { catalog, catalog_sha256, base_sha256 } = payload;
  const copy = (value) => JSON.parse(JSON.stringify(value));
  const editable = new Set(["wording", "fields", "guidance", "conditions", "exclusions", "label", "variant"]);
  const reusable = new Set(["new_entry", "replacement", "new_variant", "guidance"]);
  const labels = { pending: "Not decided", accept: "Approved for reuse", reject: "Excluded", defer: "Deferred" };
  const decisionContent = row => ({decision: row.decision, after: row.after});
  const proposals = catalog.proposals.items;
  const sources = new Map(catalog.sources.map((source) => [source.id, source]));
  const rows = proposals.map((proposal) => ({ proposal_id: proposal.id, decision: "pending", after: copy(proposal.after), note: "", action: null }));
  const panels = new Map();
  const tiles = new Map();
  const groups = new Map();
  const fieldPattern = /\{\{([a-z][a-z0-9_]*)\}\}/g;
  const passageTitle = (proposal) => proposal.label || proposal.id.replaceAll(/[-_]/g, " ").replace(/^./, (letter) => letter.toUpperCase());
  function decisionEffect(proposal) {
    const original = proposal.before ? `“${proposal.before.label} · ${proposal.before.variant}”` : "the existing entry";
    return {
      new_entry: "Approval adds a new entry to the library.",
      new_variant: `Approval adds a separate variant and keeps ${original}.`,
      replacement: `Approval replaces ${original} in the next library version.`,
      guidance: `Approval updates the guidance for ${original}; its wording stays the same.`,
    }[proposal.classification] || "This passage stays outside the reusable library.";
  }

  function el(tag, className, text) {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (text !== undefined) node.textContent = text;
    return node;
  }
  function button(text, callback, className = "") {
    const node = el("button", className, text);
    node.type = "button";
    node.addEventListener("click", callback);
    return node;
  }
  function ordered(value) {
    if (Array.isArray(value)) return value.map(ordered);
    if (value && typeof value === "object") return Object.fromEntries(Object.keys(value).sort().map((key) => [key, ordered(value[key])]));
    return value;
  }
  const same = (a, b) => JSON.stringify(ordered(a)) === JSON.stringify(ordered(b));
  async function digest(value) {
    const bytes = new TextEncoder().encode(JSON.stringify(ordered(value)));
    return Array.from(new Uint8Array(await crypto.subtle.digest("SHA-256", bytes)), (byte) => byte.toString(16).padStart(2, "0")).join("");
  }
  function message(text, error = false) {
    const target = document.getElementById("message");
    target.textContent = text;
    target.className = error ? "error" : "";
  }
  function assert(condition, text) {
    if (!condition) throw new Error(text);
  }
  function keys(value, expected, label) {
    assert(value && typeof value === "object" && !Array.isArray(value) && same(Object.keys(value).sort(), expected.split(" ").sort()), `Unexpected or missing ${label} fields.`);
  }
  function validity(entry, proposal) {
    if (!entry) return "This passage has no proposed reusable entry.";
    for (const key of ["label", "variant", "wording", "guidance"]) {
      if (typeof entry[key] !== "string" || !entry[key].trim()) return `Complete the ${key} before approving.`;
    }
    const withoutFields = entry.wording.replace(fieldPattern, "");
    if (withoutFields.includes("{{") || withoutFields.includes("}}")) return "Use matching {{lower_case_field}} placeholders.";
    const names = [...new Set(Array.from(entry.wording.matchAll(fieldPattern), (match) => match[1]))].sort();
    if (!entry.fields || Array.isArray(entry.fields) || typeof entry.fields !== "object" || !same(names, Object.keys(entry.fields).sort())) return "Define each field used in the wording and remove unused fields.";
    if (Object.values(entry.fields).some((value) => typeof value !== "string" || !value.trim())) return "Give every reusable field a description.";
    for (const key of ["conditions", "exclusions"]) {
      if (!Array.isArray(entry[key]) || entry[key].some((value) => typeof value !== "string" || !value.trim())) return `Use nonempty text for ${key}.`;
    }
    if (proposal.classification === "guidance" && entry.wording !== proposal.before.wording) return "This proposal changes guidance only. Keep its wording unchanged, or return it for a wording-change proposal.";
    return "";
  }
  function origin(entry) {
    return entry === null ? null : Object.fromEntries(Object.entries(entry).filter(([key]) => !editable.has(key)));
  }
  async function validateDecisionFile(data, application, allowLegacy = false) {
    keys(data, "kind format_version catalog_id catalog_sha256 base_sha256 purpose rows", "decision file");
    assert(data?.kind === "objection-library-decisions" && (data.format_version === 2 || allowLegacy && data.format_version === 1), "Choose a current objection-library decision file or resume legacy work as a draft.");
    const legacy = data.format_version === 1;
    data = copy(data);
    assert(data.catalog_id === catalog.id && data.catalog_sha256 === catalog_sha256 && data.base_sha256 === base_sha256, "This file belongs to a different catalog or library version. Your current work has been kept.");
    assert(["progress", "application"].includes(data.purpose), "Unknown file purpose.");
    assert(!application || data.purpose === "application", "Progress is not a library-approval export.");
    assert(Array.isArray(data.rows) && data.rows.length === rows.length, "The file must contain every candidate exactly once.");
    const accepted = new Set();
    for (let index = 0; index < proposals.length; index++) {
      const row = data.rows[index];
      const proposal = proposals[index];
      keys(row, "proposal_id decision after note action" + (Object.hasOwn(row, "legacy") ? " legacy" : ""), "candidate");
      assert(row?.proposal_id === proposal.id, "Candidate identities or order do not match this catalog.");
      assert(Object.hasOwn(labels, row.decision) && typeof row.note === "string", "Invalid candidate decision.");
      if (legacy) {row.legacy = {decision: row.decision, action: row.action}; row.decision = "pending"; row.action = null;}
      assert(same(origin(row.after), origin(proposal.after)), "A candidate's identity or source provenance changed. Your current work has been kept.");
      if (row.after !== null) {
        for (const key of ["label", "variant", "wording", "guidance"]) assert(typeof row.after[key] === "string", `Invalid ${key}.`);
        assert(row.after.fields && typeof row.after.fields === "object" && !Array.isArray(row.after.fields) && Object.values(row.after.fields).every((value) => typeof value === "string"), "Invalid reusable fields.");
        for (const key of ["conditions", "exclusions"]) assert(Array.isArray(row.after[key]) && row.after[key].every((value) => typeof value === "string"), `Invalid ${key}.`);
      }
      if (row.decision === "pending") assert(row.action === null, "An undecided candidate cannot carry approval.");
      else {
        keys(row.action, "kind at decision reviewed_content_sha256", "decision action");
        assert(row.action.kind === "individual" && typeof row.action.at === "string" && row.action.at.trim() && row.action.decision === row.decision && row.action.reviewed_content_sha256 === await digest(decisionContent(row)), "A decision no longer matches its recorded disposition or wording. Review it again before applying.");
      }
      if (row.decision === "accept") {
        assert(reusable.has(proposal.classification), "A matter-only or unresolved passage cannot enter the reusable library.");
        const error = validity(row.after, proposal);
        assert(!error, `${proposal.after.label}: ${error}`);
        assert(!accepted.has(row.after.id), "Two approvals change the same entry. Keep one decision pending and reconcile the alternatives.");
        accepted.add(row.after.id);
      }
    }
    if (legacy) {data.format_version = 2; data.purpose = "progress";}
    return data;
  }
  function updateSummary() {
    const count = (state) => rows.filter((row) => row.decision === state).length;
    document.getElementById("progress").textContent = `${count("accept")} approved · ${count("pending")} undecided · ${rows.length} candidates`;
    rows.forEach((row, index) => {
      const tile = tiles.get(index);
      tile.classList.remove("accept", "reject", "defer");
      if (row.decision !== "pending") tile.classList.add(row.decision);
      tile.querySelector(".decision-label").textContent = labels[row.decision];
      tile.querySelector(".tile-title").textContent = row.after?.label || passageTitle(proposals[index]);
      tile.querySelector(".tile-variant").textContent = row.after?.variant || proposals[index].classification.replaceAll("_", " ");
    });
  }
  function changed(index) {
    rows[index].decision = "pending";
    rows[index].action = null;
    updateSummary();
    updatePanelState(index);
  }
  function prettyWording(parent, entry) {
    parent.replaceChildren();
    let start = 0;
    for (const match of entry.wording.matchAll(fieldPattern)) {
      parent.append(document.createTextNode(entry.wording.slice(start, match.index)));
      const token = el("span", "field-token", `[${entry.fields[match[1]] || match[1]}]`);
      parent.append(token);
      start = match.index + match[0].length;
    }
    parent.append(document.createTextNode(entry.wording.slice(start)));
  }
  function updatePanelState(index) {
    const panel = panels.get(index);
    if (!panel) return;
    const row = rows[index];
    const proposal = proposals[index];
    panel.querySelector(".decision-status").textContent = row.decision === "pending" ? "No decision yet. You can approve a subset and return to the rest." : `${labels[row.decision]}. Changes to this entry require a new decision.`;
    panel.querySelector(".decision-status").className = `decision-status ${row.decision}`;
    const approve = panel.querySelector(".approve");
    const error = reusable.has(proposal.classification) ? validity(row.after, proposal) : "";
    if (approve) approve.disabled = !!error || row.decision === "accept";
    panel.querySelector(".editor-error").textContent = error;
    panel.querySelector(".undo").hidden = row.decision === "pending";
    if (row.after) {
      prettyWording(panel.querySelector(".proposed-wording"), row.after);
      panel.querySelector("h3").textContent = row.after.label;
      const use = panel.querySelector(".usage-guidance");
      const open = use.open;
      use.replaceChildren(el("summary", "", "When to use it & limits"), el("p", "guidance", row.after.guidance));
      for (const [key, heading] of [["conditions", "Required conditions"], ["exclusions", "When not to use it"]]) {
        if (row.after[key].length) {
          use.append(el("h4", "", heading));
          const list = el("ul");
          row.after[key].forEach((line) => list.append(el("li", "", line)));
          use.append(list);
        }
      }
      use.open = open;
    }
  }
  async function decide(index, decision) {
    try {
      const row = rows[index];
      if (decision === "accept") {
        assert(reusable.has(proposals[index].classification), "This passage is not a reusable candidate.");
        const error = validity(row.after, proposals[index]);
        assert(!error, error);
      }
      const snapshot = copy(row.after);
      const note = row.note;
      const priorDecision = row.decision, priorAction = row.action;
      const reviewed_content_sha256 = await digest({decision, after: snapshot});
      assert(same(snapshot, row.after) && row.note === note && row.decision === priorDecision && row.action === priorAction, "The entry changed while saving the decision. Review it again.");
      row.decision = decision;
      row.action = { kind: "individual", at: new Date().toISOString(), decision, reviewed_content_sha256 };
      updateSummary();
      updatePanelState(index);
      message(`${row.after?.label || "Passage"}: ${labels[decision].toLowerCase()}. Export your decisions to save them.`);
    } catch (error) { message(error.message, true); }
  }
  function addTextControl(parent, label, value, update, options = {}) {
    const wrap = el("label", "", label);
    const input = el(options.multiline ? "textarea" : "input", options.className || "");
    if (!options.multiline) input.type = "text";
    input.value = value;
    input.addEventListener("input", () => update(input.value));
    wrap.append(input);
    parent.append(wrap);
    return input;
  }
  function makeEditor(index, panel) {
    const row = rows[index];
    const editor = el("div", "candidate-editor");
    editor.hidden = true;
    const fields = el("div", "edit-fields");
    function rebuildFields() {
      fields.replaceChildren();
      for (const [name, value] of Object.entries(row.after.fields)) {
        addTextControl(fields, `Field description: ${name}`, value, (text) => {
          row.after.fields[name] = text;
          changed(index);
        });
      }
    }
    addTextControl(editor, "Proposed reusable wording", row.after.wording, (text) => {
      const previous = row.after.fields;
      row.after.wording = text;
      const names = [...new Set(Array.from(text.matchAll(fieldPattern), (match) => match[1]))];
      row.after.fields = Object.fromEntries(names.map((name) => [name, previous[name] || ""]));
      if (!same(Object.keys(previous), names)) rebuildFields();
      changed(index);
    }, { multiline: true, className: "wording-editor" });
    editor.append(el("p", "muted", "Use {{field_name}} for text that changes between matters. Give each field a readable description below."), fields);
    rebuildFields();
    const guidance = el("details");
    guidance.append(el("summary", "", "Labels & reusable guidance"));
    for (const [key, label] of [["label", "Short label"], ["variant", "Variant description"], ["guidance", "When to use this wording"]]) {
      addTextControl(guidance, label, row.after[key], (text) => { row.after[key] = text; changed(index); }, { multiline: key === "guidance" });
    }
    for (const [key, label] of [["conditions", "Required conditions — one per line"], ["exclusions", "When not to use it — one per line"]]) {
      addTextControl(guidance, label, row.after[key].join("\n"), (text) => { row.after[key] = text.split("\n").map((line) => line.trim()).filter(Boolean); changed(index); }, { multiline: true });
    }
    editor.append(guidance);
    const controls = el("div", "actions");
    controls.append(button("Finish editing", () => { editor.hidden = true; edit.hidden = false; edit.focus(); }), button("Restore proposed entry", () => {
      row.after = copy(proposals[index].after);
      changed(index);
      openPanel(index, false);
    }, "text-button"));
    editor.append(controls);
    const edit = button("Edit proposed entry", () => { editor.hidden = false; edit.hidden = true; editor.querySelector("textarea").focus(); }, "text-button");
    panel.append(edit, editor);
  }
  function sourceEvidence(index, panel) {
    const area = el("section", "source-evidence");
    area.append(el("h4", "", "Source wording & context"));
    const passages = catalog.passages.filter((passage) => passage.proposal_ids.includes(proposals[index].id));
    passages.forEach((passage, position) => {
      const source = sources.get(passage.source_id);
      const details = el("details");
      details.open = position === 0;
      details.append(el("summary", "", `${source.title} · ${passage.locator}`));
      if (passage.request) {
        details.append(el("h5", "source-label", "Source request"), el("p", "source-request", passage.request));
      }
      details.append(el("h5", "source-label", "Exact source passage"));
      details.append(el("blockquote", "source-original", passage.original));
      if (passage.context) {
        const context = el("details", "source-context");
        context.append(el("summary", "", "Read the surrounding response or source note"), el("div", "", passage.context));
        details.append(context);
      }
      details.append(el("p", "locator", `Source file: ${source.file}`));
      area.append(details);
    });
    panel.append(area);
  }
  function closePanel(index, focus = true) {
    const panel = panels.get(index);
    panel?.remove();
    panels.delete(index);
    const tile = tiles.get(index);
    tile.classList.remove("inspecting");
    tile.setAttribute("aria-expanded", "false");
    if (focus) { tile.focus({ preventScroll: true }); tile.scrollIntoView({ block: "nearest" }); }
  }
  function openPanel(index, scroll = true) {
    const group = tiles.get(index).closest(".family");
    for (const [openIndex, panel] of panels) if (panel.parentElement === group) closePanel(openIndex, false);
    const row = rows[index];
    const proposal = proposals[index];
    const panel = el("section", "detail-panel candidate-panel");
    panel.id = `candidate-panel-${index}`;
    panel.setAttribute("aria-labelledby", `candidate-title-${index}`);
    const head = el("div", "detail-head");
    const title = el("h3", "", row.after?.label || passageTitle(proposal));
    title.id = `candidate-title-${index}`;
    head.append(title, button("Close", () => closePanel(index), "detail-close"));
    panel.append(head, el("p", "proposal-reason", proposal.reason));
    if (proposal.before) {
      const prior = el("details", "prior-entry");
      prior.append(el("summary", "", "Current approved entry"), el("p", "library-wording", proposal.before.wording), el("p", "guidance", proposal.before.guidance));
      panel.append(prior);
    }
    if (row.after) panel.append(el("h4", "", "Proposed reusable wording"), el("p", "library-wording proposed-wording"));
    else panel.append(el("p", "warning", "No reusable wording is proposed for this passage yet. Keep it pending, defer or exclude it, or return it with instructions for a reusable candidate to review."));
    panel.append(el("p", "editor-error"));
    const actions = el("div", "decision-actions"); actions.id = `candidate-actions-${index}`;
    actions.append(el("p", "decision-effect", decisionEffect(proposal)));
    if (reusable.has(proposal.classification)) actions.append(button("Approve for reuse", () => decide(index, "accept"), "primary approve"));
    actions.append(button("Defer", () => decide(index, "defer")), button("Exclude", () => decide(index, "reject")), button("Undo decision", () => { changed(index); message("Decision cleared. This entry is not approved for reuse."); }, "text-button undo"));
    panel.append(actions, el("p", "decision-status"));
    const notes = el("details", "curation-note");
    notes.append(el("summary", "", "Add a decision note"));
    const noteLabel = el("label", "", "Decision note");
    const note = el("textarea", "decision-note");
    note.value = row.note;
    note.addEventListener("input", () => { row.note = note.value; changed(index); });
    noteLabel.append(note);
    notes.append(noteLabel);
    panel.append(notes);
    if (row.after) {
      panel.append(el("details", "usage-guidance"));
      if (reusable.has(proposal.classification)) makeEditor(index, panel);
    }
    sourceEvidence(index, panel);
    const back = el("a", "back-to-review", "Back to reuse decision"); back.href = `#candidate-actions-${index}`;
    panel.append(back);
    group.insertBefore(panel, group.querySelector(".tile-grid"));
    panels.set(index, panel);
    tiles.get(index).classList.add("inspecting");
    tiles.get(index).setAttribute("aria-expanded", "true");
    updatePanelState(index);
    if (scroll) panel.scrollIntoView({ block: "nearest" });
  }
  function render() {
    panels.clear();
    tiles.clear();
    groups.clear();
    const main = document.getElementById("catalog");
    main.replaceChildren();
    proposals.forEach((proposal, index) => {
      const family = proposal.after?.family || proposal.before?.family || "Other passages";
      if (!groups.has(family)) {
        const section = el("section", "family");
        const heading = el("div", "family-heading");
        heading.append(el("h2", "", family.replaceAll(/[-_]/g, " ").replace(/^./, (letter) => letter.toUpperCase())));
        const grid = el("div", "tile-grid");
        section.append(heading, grid);
        groups.set(family, grid);
        main.append(section);
      }
      const tile = button("", () => panels.has(index) ? closePanel(index) : openPanel(index), "tile candidate-tile");
      tile.id = `candidate-${index}`;
      tile.dataset.proposal = proposal.id;
      tile.setAttribute("aria-expanded", "false");
      tile.setAttribute("aria-controls", `candidate-panel-${index}`);
      tile.append(el("span", "tile-title"), el("span", "tile-variant"), el("span", "decision-label"));
      groups.get(family).append(tile);
      tiles.set(index, tile);
    });
    updateSummary();
  }
  async function download(purpose) {
    try {
      const data = { kind: "objection-library-decisions", format_version: 2, catalog_id: catalog.id, catalog_sha256, base_sha256, purpose, rows: copy(rows) };
      await validateDecisionFile(data, purpose === "application");
      const url = URL.createObjectURL(new Blob([`${JSON.stringify(data, null, 2)}\n`], { type: "application/json" }));
      const link = el("a");
      link.href = url;
      const safeId = catalog.id.replace(/[^a-zA-Z0-9_-]/g, "-").slice(0, 90) || "library";
      link.download = `${safeId}-${purpose === "progress" ? "progress" : "decisions"}.json`;
      document.body.append(link);
      link.click();
      link.remove();
      setTimeout(() => URL.revokeObjectURL(url), 1000);
      const approved = data.rows.filter((row) => row.decision === "accept").length;
      message(purpose === "progress" ? "Progress downloaded. It is not an instruction to change the library." : `Decisions downloaded: ${approved} approved. Return this file to save the approved subset; the other candidates remain outside the library.`);
    } catch (error) { message(error.message, true); }
  }
  document.getElementById("save").addEventListener("click", () => download("progress"));
  document.getElementById("export").addEventListener("click", () => download("application"));
  document.getElementById("import").addEventListener("change", async (event) => {
    try {
      const file = event.target.files[0];
      if (!file) return;
      const original = JSON.parse(await file.text());
      const data = await validateDecisionFile(original, false, true);
      rows.splice(0, rows.length, ...copy(data.rows));
      render();
      message(original.format_version === 1 ? "Legacy drafts restored. Prior dispositions are retained as history; decide each candidate again before library application." : "Saved decisions restored. Export library decisions when ready to return them.");
    } catch (error) { message(`Could not restore: ${error.message}`, true); }
    finally { event.target.value = ""; }
  });
  const theme = document.getElementById("theme-toggle");
  function syncTheme() {
    const dark = document.documentElement.dataset.theme ? document.documentElement.dataset.theme === "dark" : matchMedia("(prefers-color-scheme: dark)").matches;
    theme.setAttribute("aria-pressed", String(dark));
    theme.textContent = dark ? "Use light theme" : "Use dark theme";
    return dark;
  }
  theme.addEventListener("click", () => { document.documentElement.dataset.theme = syncTheme() ? "light" : "dark"; syncTheme(); });
  matchMedia("(prefers-color-scheme: dark)").addEventListener("change", syncTheme);
  syncTheme();
  document.getElementById("title").textContent = catalog.title;
  document.title = catalog.title;
  document.getElementById("scope").textContent = catalog.scope;
  const notes = document.getElementById("notes");
  notes.append(el("p", "", `${catalog.sources.length} source documents · Library version ${catalog.library.version} · ${catalog.library.entries.length} existing approved entries`));
  const list = el("ul");
  catalog.notes.forEach((note) => list.append(el("li", "", note)));
  notes.append(list);
  render();
})();
