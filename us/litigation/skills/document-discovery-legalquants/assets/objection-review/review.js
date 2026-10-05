(() => {
  "use strict";
  const payload = JSON.parse(document.getElementById("review-data").textContent);
  const review = payload.review;
  const entries = new Map(review.library.entries.map(e => [e.id, e]));
  const byId = id => document.getElementById(id);
  const copy = data => JSON.parse(JSON.stringify(data));
  const ordered = value => Array.isArray(value) ? value.map(ordered) : value && typeof value === "object" ? Object.fromEntries(Object.keys(value).sort().map(key => [key, ordered(value[key])])) : value;
  const same = (a, b) => JSON.stringify(ordered(a)) === JSON.stringify(ordered(b));
  const digest = async value => Array.from(new Uint8Array(await crypto.subtle.digest("SHA-256", new TextEncoder().encode(JSON.stringify(ordered(value))))), byte => byte.toString(16).padStart(2, "0")).join("");
  const states = {not_reviewed: "Not reviewed", reviewed: "Reviewed", needs_input: "Needs input"};
  const fill = (entry, params) => entry.wording.replace(/\{\{([a-z][a-z0-9_]*)\}\}/g, (_, k) => params[k]);
  const slots = entry => Object.fromEntries(Object.entries(entry.fields).map(([k, v]) => [k, "[" + v + "]"]));
  let serial = 0;
  const makeChoice = (request, entry, params) => ({
    component_id: request.id + ":" + (++serial) + ":" + Date.now(),
    entry_id: entry.id, params: copy(params), wording: fill(entry, params),
    edited: false, scope: "", notes: ""
  });
  let rows = review.requests.map(request => {
    const choices = request.suggestions.filter(s => s.preselected).map(s => makeChoice(request, entries.get(s.entry_id), s.params));
    return {request_id: request.id, state: "not_reviewed", action: null, notes: "", choices, drafts: [...choices]};
  });
  // Disclosure state never becomes an attorney decision.
  const makeViews = () => rows.map(row => {
    const drafts = new Map(row.drafts.map(c => [c.entry_id || c.component_id, c]));
    row.choices = row.choices.map(c => row.drafts.find(d => d.component_id === c.component_id));
    return {open: null, editing: false, notes: false, order: false, context: false, others: false, drafts};
  });
  let views = makeViews();
  let dirty = false, pendingImport = null, saveStatus = "No changes since opening";
  const revisions = new WeakMap();
  const touch = row => {revisions.set(row, (revisions.get(row) || 0) + 1); dirty = true;};
  const reviewedContent = row => ({review_sha256: payload.review_sha256, request_id: row.request_id, choices: copy(row.choices), notes: row.notes});

  function entryTitle(entry) {
    const siblings = review.library.entries.filter(e => e.label === entry.label);
    if (siblings.length === 1) return entry.label;
    if (new Set(siblings.map(e => e.variant)).size === siblings.length) return entry.label + " · " + entry.variant;
    const position = siblings.indexOf(entry);
    // Older libraries can contain indistinguishable variant labels. Do not invent a legal distinction.
    return entry.label + (position ? " · alternative " + (position > 1 ? position : "wording") : "");
  }
  function el(tag, text, className) {
    const node = document.createElement(tag);
    if (text !== undefined) node.textContent = text;
    if (className) node.className = className;
    return node;
  }
  function button(text, fn, className) {
    const b = el("button", text, className); b.type = "button"; b.addEventListener("click", fn); return b;
  }
  function message(text, error = false) {
    byId("message").textContent = text;
    byId("message").className = error ? "error" : "";
    byId("message").setAttribute("role", error ? "alert" : "status");
  }
  function changed(row) {
    if (row.state === "reviewed") row.state = "not_reviewed";
    row.action = null; touch(row); progress();
  }
  async function approve(row, kind) {
    row.choices.forEach(choice => validateChoice(choice, true));
    const snapshot = reviewedContent(row);
    const revision = revisions.get(row);
    const reviewed_content_sha256 = await digest(snapshot);
    if (revision !== revisions.get(row) || !same(snapshot, reviewedContent(row))) throw new Error("Wording changed while recording review. Review this request again.");
    row.state = "reviewed"; row.action = {kind, at: new Date().toISOString(), reviewed_content_sha256}; touch(row);
  }
  // Work on a detached snapshot. Neither export nor batch review may record a
  // partial/stale approval if validation fails or the lawyer edits while hashing.
  async function authorize(record, selectedOnly) {
    for (const row of record.rows) {
      if (row.state !== "not_reviewed" || selectedOnly && !row.choices.length) continue;
      try {row.choices.forEach(choice => validateChoice(choice, true));}
      catch (error) {
        const request = review.requests.find(request => request.id === row.request_id);
        throw new Error(`${request.label}: ${error.message} Complete or deselect the wording, or mark Needs input to leave this request open. Your edits are kept; Save progress can preserve unfinished work.`);
      }
      const reviewed_content_sha256 = await digest(reviewedContent(row));
      row.state = "reviewed";
      row.action = {kind: "batch", trigger: selectedOnly ? "export-selected" : "mark-all", at: new Date().toISOString(), reviewed_content_sha256};
    }
    return record;
  }
  function applyApprovals(record) {
    record.rows.forEach((saved, i) => {
      const row = rows[i];
      if (row.state !== saved.state || !same(row.action, saved.action)) {
        row.state = saved.state; row.action = copy(saved.action); touch(row);
      }
    });
  }
  function progress() {
    const done = rows.filter(r => r.state === "reviewed").length;
    const selected = rows.filter(r => r.state === "not_reviewed" && r.choices.length).length;
    byId("progress").textContent = done + " of " + rows.length + " reviewed" + (selected ? " · " + selected + " selected for export" : "") + " · " + (rows.length - done - selected) + " open";
    byId("save-status").textContent = dirty ? "Changes since the last download request or resume" : saveStatus;
    rows.forEach((row, i) => {
      let incomplete = false;
      try {row.choices.forEach(choice => validateChoice(choice, true));} catch {incomplete = true;}
      const badge = byId("status-" + i);
      if (badge) {
        badge.textContent = row.state === "reviewed" && !row.choices.length ? "Reviewed · no objections" : row.state === "not_reviewed" && row.choices.length ? incomplete ? "Selected · needs completion" : "Selected · included on export" : states[row.state];
        badge.className = "badge " + row.state;
      }
      const action = byId("review-" + i);
      if (action) {
        action.textContent = row.state === "reviewed" ? "Undo review" : "Mark reviewed";
        action.className = row.state === "reviewed" || row.state === "not_reviewed" && row.choices.length ? "text-button" : "primary";
      }
      const link = byId("nav-" + i);
      if (link) {
        link.className = row.state;
        link.textContent = (row.state === "reviewed" ? "✓ " : row.state === "needs_input" ? "! " : "○ ") + review.requests[i].label;
      }
      const preview = byId("wording-preview-" + i);
      if (preview) {
        preview.textContent = row.choices.map(c => c.wording).join("\n\n");
        preview.hidden = !row.choices.length;
        const status = byId("wording-status-" + i);
        status.textContent = row.state === "reviewed" ? row.choices.length ? "Reviewed starting wording. Export for Word authorizes assembly; finish substantive responses in Word." : "Reviewed · no wording selected. Export for Word authorizes assembly; finish substantive responses in Word." : row.choices.length ? "Export for Word accepts this selected wording. No separate review click is needed." : "No wording selected. " + (review.requests[i].suggestions.length ? "Surfaced possibilities remain unchecked. " : "") + "Mark reviewed to confirm none, or leave open for drafting.";
        if (incomplete) status.textContent = "Complete or deselect the unfinished wording, or mark Needs input to leave this request open. Save progress keeps unfinished work.";
        if (row.state === "needs_input") status.textContent = row.choices.length ? "Needs input · wording below is not included until you mark this request reviewed." : "Needs input · no objections selected; review remains open.";
      }
    });
  }
  function field(parent, text, value, multiline, update) {
    const label = el("label", text);
    const input = el(multiline ? "textarea" : "input");
    if (!multiline) input.type = "text";
    input.value = value; input.addEventListener("input", () => update(input.value));
    label.append(input); parent.append(label); return input;
  }
  function disclosure(text, content) {
    const details = el("details"); details.append(el("summary", text), content); return details;
  }
  function showReason(parent, suggestion, entry) {
    const wrap = el("span", undefined, "reason-wrap");
    const id = "reason-" + (++serial);
    const tip = el("span", "For consideration — not a decision to include.\n\nConnection: " + suggestion.rationale + "\n\nBasis: " + suggestion.basis.join("; ") +
      (suggestion.missing.length ? "\n\nCheck before including: " + suggestion.missing.join("; ") : ""), "reason");
    tip.id = id; tip.setAttribute("role", "tooltip");
    const b = button("?", () => {
      const opened = wrap.classList.toggle("open");
      wrap.classList.toggle("dismissed", !opened); b.setAttribute("aria-expanded", String(opened));
    }, "reason-button");
    b.setAttribute("aria-label", "Why " + entryTitle(entry) + "?");
    b.setAttribute("aria-describedby", id); b.setAttribute("aria-expanded", "false");
    b.addEventListener("focus", () => wrap.classList.remove("dismissed"));
    wrap.addEventListener("mouseenter", () => wrap.classList.remove("dismissed"));
    b.addEventListener("keydown", e => {
      if (e.key === "Escape") {
        wrap.classList.remove("open"); wrap.classList.add("dismissed");
        b.setAttribute("aria-expanded", "false");
      }
    });
    wrap.append(b, tip); parent.append(wrap);
  }

  function selectChoice(i, key, entry, suggestion, selected, focusId) {
    const row = rows[i], view = views[i], request = review.requests[i];
    const choice = row.choices.find(c => (c.entry_id || c.component_id) === key);
    if (selected && !choice) {
      const draft = view.drafts.get(key) || makeChoice(request, entry, suggestion?.params || slots(entry));
      if (!view.drafts.has(key)) row.drafts.push(draft);
      view.drafts.set(key, draft); row.choices.push(draft);
    } else if (!selected && choice) {
      view.drafts.set(key, choice);
      row.choices = row.choices.filter(c => c !== choice); view.editing = false;
    }
    changed(row); draw(i, focusId);
  }

  function tile(parent, i, entry, custom) {
    const row = rows[i], view = views[i], request = review.requests[i];
    const key = entry ? entry.id : custom.component_id;
    const choice = row.choices.find(c => (c.entry_id || c.component_id) === key);
    const suggestion = entry && request.suggestions.find(s => s.entry_id === entry.id);
    const title = entry ? entryTitle(entry) : "Custom objection";
    const box = el("div", undefined, "tile" + (choice ? " selected" : "") + (view.open === key ? " inspecting" : ""));
    box.dataset.entry = key;
    const check = el("input"); check.type = "checkbox"; check.checked = Boolean(choice);
    check.id = "choice-" + i + "-" + key;
    check.setAttribute("aria-label", "Select " + title + " for " + request.label);
    check.addEventListener("change", () => selectChoice(i, key, entry, suggestion, check.checked, check.id));
    const name = button(title, () => {
      view.open = view.open === key ? null : key;
      view.editing = false; draw(i, name.id);
      if (view.open) byId("detail-" + i).scrollIntoView({block: "nearest"});
    }, "tile-name");
    name.id = "inspect-" + i + "-" + key;
    name.setAttribute("aria-expanded", String(view.open === key));
    name.setAttribute("aria-controls", "detail-" + i);
    const selectTarget = el("label", undefined, "tile-select"); selectTarget.append(check);
    box.append(selectTarget, name);
    if (suggestion) showReason(box, suggestion, entry);
    const meta = el("div", undefined, "tile-meta");
    if (entry && entry.family) meta.append(el("span", entry.family.replaceAll(/[-_]/g, " "), "ground-type"));
    if (suggestion) meta.append(el("span", "For consideration", "suggested"));
    if (view.open === key) meta.append(el("span", "Inspecting", "inspection-label"));
    if (suggestion?.missing.length) meta.append(el("span", "Check conditions", "condition-label"));
    if (choice?.edited) meta.append(el("span", "Edited"));
    box.append(meta); parent.append(box);
  }

  function detail(parent, i) {
    const row = rows[i], view = views[i], request = review.requests[i];
    if (!view.open) return;
    const entry = entries.get(view.open);
    const choice = row.choices.find(c => (c.entry_id || c.component_id) === view.open);
    const draft = choice || view.drafts.get(view.open);
    const suggestion = entry && request.suggestions.find(s => s.entry_id === entry.id);
    const panel = el("section", undefined, "detail-panel"); panel.id = "detail-" + i;
    panel.setAttribute("aria-label", entry ? entryTitle(entry) + " wording" : "Custom objection wording");
    const head = el("div", undefined, "detail-head");
    const opened = view.open;
    head.append(el("h3", entry ? entryTitle(entry) : "Custom objection"), button("Close", () => {
      view.open = null; view.editing = false; draw(i, "inspect-" + i + "-" + opened);
      byId("inspect-" + i + "-" + opened)?.scrollIntoView({block: "nearest"});
    }, "detail-close"));
    panel.append(head);
    if (suggestion) {
      const assessment = el("section", undefined, "candidate-reason");
      assessment.setAttribute("aria-label", "Why consider this objection");
      assessment.append(el("h4", "For consideration · not included in Word"), el("p", "Connection: " + suggestion.rationale), el("p", "Basis: " + suggestion.basis.join("; "), "muted"));
      if (suggestion.missing.length) assessment.append(el("p", "Check before including: " + suggestion.missing.join("; "), "warning"));
      panel.append(assessment);
    }
    if (entry || draft) {
      const current = draft ? draft.wording : fill(entry, suggestion?.params || slots(entry));
      panel.append(el("h4", "For this request" + (choice ? "" : " · not selected")));
      const proposed = el("p", current, "request-wording"); panel.append(proposed);
      const inclusion = el("label", undefined, "detail-inclusion");
      const select = el("input"); select.type = "checkbox"; select.checked = Boolean(choice);
      select.id = "detail-choice-" + i + "-" + opened;
      select.addEventListener("change", () => selectChoice(i, opened, entry, suggestion, select.checked, select.id));
      inclusion.append(select, document.createTextNode("Include this wording for " + request.label));
      panel.append(inclusion);
      if (choice && !view.editing) panel.append(button("Edit wording", () => {
        view.editing = true; draw(i, "wording-" + i);
      }, "text-button"));
      if (choice && view.editing) {
        const editor = el("div", undefined, "wording-editor");
        const input = field(editor, "Wording to insert (edits apply to this request only)", choice.wording, true, value => {
          choice.wording = value; choice.edited = true; proposed.textContent = value; changed(row);
        });
        input.id = "wording-" + i;
        if (entry && Object.keys(entry.fields).length) {
          const fields = el("div");
          Object.entries(entry.fields).forEach(([key, description]) => {
            field(fields, description, choice.params[key], false, value => {
              choice.params[key] = value;
              if (!choice.edited) {
                choice.wording = fill(entry, choice.params);
                input.value = choice.wording; proposed.textContent = choice.wording;
              }
              changed(row);
            });
          });
          editor.append(disclosure("Drafting fields", fields));
        }
        const actions = el("div", undefined, "detail-actions");
        actions.append(button("Done editing", () => {view.editing = false; draw(i, "inspect-" + i + "-" + opened);}));
        if (entry) actions.append(button("Restore library wording", () => {
          choice.wording = fill(entry, choice.params); choice.edited = false; changed(row); draw(i, "wording-" + i);
        }, "text-button"));
        editor.append(actions); panel.append(editor);
      }
      if (draft?.scope) panel.append(el("p", "Scope note: " + draft.scope, "muted"));
      if (draft?.notes) panel.append(el("p", "Note: " + draft.notes, "muted"));
    }
    if (entry) {
      const canonical = el("div");
      canonical.append(el("p", fill(entry, slots(entry)), "library-wording"));
      if (Object.keys(entry.fields).length) canonical.append(el("p", "Brackets identify drafting fields.", "muted"));
      const comparison = disclosure("Compare library wording", canonical);
      comparison.className = "library-comparison";
      panel.append(comparison);
      const guidance = el("div", undefined, "guidance");
      guidance.append(el("p", entry.guidance));
      for (const [label, values] of [["Use when", entry.conditions], ["Exclusions", entry.exclusions]]) {
        if (values.length) {
          guidance.append(el("h4", label));
          const list = el("ul"); values.forEach(value => list.append(el("li", value))); guidance.append(list);
        }
      }
      guidance.append(el("p", entry.sources.map(s => s.source_id + ": " + s.locator).join("; "), "locator"));
      panel.append(disclosure("When to use & source", guidance));
    }
    parent.append(panel);
  }

  function requestNode(i) {
    const request = review.requests[i], row = rows[i], view = views[i];
    const article = el("article", undefined, "request"); article.id = "request-" + i;
    const head = el("div", undefined, "request-head");
    const badge = el("span", "", "badge"); badge.id = "status-" + i;
    head.append(el("h2", request.label), badge);
    article.append(head, el("p", request.text, "served"));
    const preview = el("section", undefined, "wording-for-word");
    preview.setAttribute("aria-label", "Wording for Word for " + request.label);
    const output = el("div", undefined, "wording-preview"); output.id = "wording-preview-" + i;
    const outputStatus = el("p", undefined, "wording-status"); outputStatus.id = "wording-status-" + i;
    preview.append(el("h3", "Wording for Word"), outputStatus, output);
    article.append(preview);
    const actions = el("div", undefined, "review-actions"); actions.id = "review-actions-" + i;
    const mark = button("Mark reviewed", async () => {
      try {
        if (row.state === "reviewed") {row.state = "not_reviewed"; row.action = null; touch(row);}
        else await approve(row, "individual");
        draw(i, "review-" + i);
      } catch (error) {message(error.message, true);}
    }); mark.id = "review-" + i;
    const secondary = el("div", undefined, "actions");
    secondary.append(button(view.notes ? "Close note" : row.notes ? "Edit note" : "Add note", () => {
      view.notes = !view.notes; draw(i, view.notes ? "notes-" + i : undefined);
    }, "text-button"));
    secondary.append(button("Needs input", () => {row.state = "needs_input"; row.action = null; touch(row); view.notes = true; draw(i, "notes-" + i);}, "text-button"));
    secondary.append(button("Add custom objection", () => {
      const custom = {component_id: request.id + ":custom:" + (++serial) + ":" + Date.now(), entry_id: null, params: {}, wording: "[Draft request-specific objection]", edited: true, scope: "", notes: ""};
      row.choices.push(custom); row.drafts.push(custom); view.drafts.set(custom.component_id, custom);
      view.open = custom.component_id; view.editing = true; changed(row); draw(i, "wording-" + i);
    }, "text-button"));
    if (row.choices.length > 1) secondary.append(button(view.order ? "Close order" : "Arrange wording", () => {
      view.order = !view.order; draw(i);
    }, "text-button"));
    actions.append(mark, secondary); article.append(actions);
    const contextContent = el("div");
    contextContent.append(el("p", request.locator, "locator"));
    request.context_ids.forEach(id => {
      const context = review.context.find(c => c.id === id);
      contextContent.append(el("h4", context.title), el("p", context.text, "context-text"), el("p", context.locator, "locator"));
    });
    const context = disclosure("Request context", contextContent); context.className = "request-context"; context.open = view.context;
    context.addEventListener("toggle", () => {view.context = context.open;});
    article.append(context);
    const families = row.choices.filter(c => c.entry_id).map(c => entries.get(c.entry_id).family);
    if (new Set(families).size < families.length) article.append(el("p", "Multiple wordings from one objection family are selected. Check for overlap.", "warning"));
    if (row.state === "needs_input") article.append(el("p", row.notes || "This request needs input and will remain open when exported.", "warning"));
    article.append(el("p", row.choices.length ? row.choices.length + (row.choices.length === 1 ? " objection selected" : " objections selected") : "No wording selected.", "selection-summary"));
    detail(article, i);
    if (view.notes) {
      const notes = el("div", undefined, "note-editor");
      const input = field(notes, "Review notes — not included in Word", row.notes, true, value => {row.notes = value; changed(row);});
      input.id = "notes-" + i;
      article.append(notes);
    } else if (row.notes && row.state !== "needs_input") article.append(el("p", "Review note (not included in Word): " + row.notes, "muted"));
    if (view.order && row.choices.length > 1) {
      const list = el("ol", undefined, "order-list");
      row.choices.forEach((choice, position) => {
        const li = el("li");
        li.append(el("span", (position + 1) + ". " + (choice.entry_id ? entryTitle(entries.get(choice.entry_id)) : "Custom objection")));
        const actions = el("div", undefined, "actions");
        const move = (delta) => {
          [row.choices[position], row.choices[position + delta]] = [row.choices[position + delta], row.choices[position]];
          changed(row); draw(i);
        };
        const up = button("Move up", () => move(-1)); up.disabled = position === 0;
        const down = button("Move down", () => move(1)); down.disabled = position === row.choices.length - 1;
        actions.append(up, down); li.append(actions); list.append(li);
      });
      article.append(list);
    }
    const suggested = new Set(request.suggestions.map(s => s.entry_id));
    const selected = new Set(row.choices.map(c => c.entry_id).filter(Boolean));
    const mainEntries = Array.from(entries.values()).filter(entry => suggested.has(entry.id) || selected.has(entry.id));
    const otherEntries = Array.from(entries.values()).filter(entry => !suggested.has(entry.id) && !selected.has(entry.id));
    const palette = el("section", undefined, "request-palette");
    palette.append(el("h3", "Possible objections for this request", "palette-title"));
    if (request.candidate_note) palette.append(el("p", "Candidate assessment — " + request.candidate_note, "muted candidate-note"));
    const grid = el("div", undefined, "tile-grid main-choices");
    grid.setAttribute("role", "group"); grid.setAttribute("aria-label", "Objections for " + request.label);
    for (const entry of mainEntries) tile(grid, i, entry);
    for (const [key, custom] of view.drafts) if (!entries.has(key)) tile(grid, i, null, custom);
    if (grid.childElementCount) palette.append(grid);
    else palette.append(el("p", request.candidate_note ? "No primary objection choices are surfaced. Other approved wording remains available below." : "No primary choices were supplied for this request; that alone does not establish that no objection could apply. Inspect the other library objections or request a candidate assessment.", "muted palette-empty"));
    if (otherEntries.length) {
      const otherContent = el("div");
      const otherGrid = el("div", undefined, "tile-grid other-choices");
      otherGrid.setAttribute("role", "group"); otherGrid.setAttribute("aria-label", "Other library objections for " + request.label);
      for (const entry of otherEntries) tile(otherGrid, i, entry);
      otherContent.append(el("p", "Other approved starting wording, in library order. A connection to this request has not been identified in the primary choices; inspect and adapt it if you see one.", "muted"), otherGrid);
      const back = el("a", "Back to wording and review", "back-to-review"); back.href = "#review-actions-" + i;
      otherContent.append(back);
      const other = disclosure("Other library objections (" + otherEntries.length + ")", otherContent);
      other.className = "other-library"; other.open = view.others;
      other.addEventListener("toggle", () => {view.others = other.open;});
      palette.append(other);
    }
    article.append(palette);
    return article;
  }
  function draw(index, focusId) {
    if (index === undefined) byId("requests").replaceChildren(...review.requests.map((_, i) => requestNode(i)));
    else byId("request-" + index).replaceWith(requestNode(index));
    progress();
    if (focusId) byId(focusId)?.focus({preventScroll: true});
  }
  function exportRecord(purpose) {
    const savedRows = rows.map(row => ({...copy(row), selected_ids: row.choices.map(choice => choice.component_id)}));
    return {kind:"objection-selections",format_version:2,purpose,review_id:review.id,review_sha256:payload.review_sha256,source_sha256:review.source.sha256,library_sha256:payload.library_sha256,rows:savedRows};
  }
  function check(ok, text) { if (!ok) throw new Error(text); }
  function validateChoice(c, complete) {
    check(c && typeof c.component_id === "string" && c.component_id, "Missing component identity.");
    check(typeof c.wording === "string" && (!complete || c.wording.trim()) && typeof c.edited === "boolean" && typeof c.scope === "string" && typeof c.notes === "string", complete ? "Complete the selected wording before accepting it." : "Invalid draft wording.");
    check(c.params && typeof c.params === "object" && !Array.isArray(c.params), "Invalid substitutions.");
    if (c.entry_id === null) check(c.edited && Object.keys(c.params).length === 0, "One-off wording has an invalid library origin.");
    else {
      const entry = entries.get(c.entry_id); check(entry, "Unknown library variant.");
      check(same(Object.keys(c.params).sort(), Object.keys(entry.fields).sort()), "Substitution fields do not match.");
      check(Object.values(c.params).every(value => typeof value === "string" && (!complete || c.edited || value.trim())), "Complete empty fields or use visible drafting slots before review.");
      check(c.edited || c.wording === fill(entry, c.params), "Changed wording must be marked as a request-specific edit.");
    }
  }
  async function validate(data, allowLegacy = false) {
    check(data.kind === "objection-selections" && (data.format_version === 2 || allowLegacy && data.format_version === 1), "Unsupported file format.");
    check(["progress", "assembly"].includes(data.purpose), "Unknown export purpose.");
    const legacy = data.format_version === 1;
    const matchingReview = data.review_sha256 === payload.review_sha256 || legacy && review.legacy_review_sha256 && data.review_sha256 === review.legacy_review_sha256;
    check(data.review_id === review.id && matchingReview && data.library_sha256 === payload.library_sha256 && data.source_sha256 === review.source.sha256, "This file belongs to a different or changed source, library, or review.");
    check(Array.isArray(data.rows) && data.rows.length === review.requests.length, "Request list does not match.");
    const result = copy(data);
    const componentIds = new Set();
    for (let i = 0; i < result.rows.length; i++) {
      const row = result.rows[i];
      check(row.request_id === review.requests[i].id && Object.hasOwn(states, row.state), "Request identity or review state does not match.");
      check(typeof row.notes === "string" && Array.isArray(row.choices), "Invalid review notes or choices.");
      if (legacy) {
        row.drafts = copy(row.choices); row.selected_ids = row.choices.map(choice => choice.component_id);
        row.legacy_action = row.action; row.action = null;
        row.state = row.state === "needs_input" ? "needs_input" : "not_reviewed";
      }
      check(Array.isArray(row.drafts) && Array.isArray(row.selected_ids), "Missing saved drafts or selected order.");
      const drafts = new Map(), origins = new Set();
      for (const c of row.drafts) {
        validateChoice(c, false);
        check(!componentIds.has(c.component_id), "Duplicate component identity."); componentIds.add(c.component_id); drafts.set(c.component_id, c);
        if (c.entry_id !== null) {check(!origins.has(c.entry_id), "Duplicate library draft."); origins.add(c.entry_id);}
      }
      check(new Set(row.selected_ids).size === row.selected_ids.length && row.selected_ids.every(id => drafts.has(id)), "Unknown or repeated selected component.");
      check(same(row.choices, row.selected_ids.map(id => drafts.get(id))), "Selected wording differs from its saved draft or order.");
      if (row.state === "reviewed") {
        check(row.action && ["individual", "batch"].includes(row.action.kind) && typeof row.action.at === "string" && row.action.at.trim(), "Missing review action.");
        check(row.action.reviewed_content_sha256 === await digest(reviewedContent(row)), "Wording changed after the recorded review. Review this request again.");
        row.choices.forEach(choice => validateChoice(choice, true));
      } else check(row.action === null, "An unfinished request cannot carry a review action.");
    }
    if (legacy) {result.format_version = 2; result.purpose = "progress"; result.review_sha256 = payload.review_sha256;}
    return result;
  }
  async function download(purpose) {
    try {
      const original = exportRecord(purpose), sourceRows = rows;
      const data = copy(original);
      if (purpose === "assembly") await authorize(data, true);
      await validate(data);
      check(rows === sourceRows && same(original, exportRecord(purpose)), "Work changed during export. Download again to include the latest changes. No new review actions were recorded.");
      const blob = new Blob([JSON.stringify(data, null, 2) + "\n"], {type: "application/json"});
      const url = URL.createObjectURL(blob); const anchor = el("a"); anchor.href = url;
      const stamp = new Date().toISOString().replaceAll(/[:.]/g, "-");
      anchor.download = `${review.id.replace(/[^a-zA-Z0-9_-]/g, "_")}-library-v${review.library.version}-${purpose}-${stamp}.json`;
      document.body.append(anchor); anchor.click(); anchor.remove(); setTimeout(() => URL.revokeObjectURL(url), 10000);
      applyApprovals(data);
      dirty = false; saveStatus = `Download requested: ${anchor.download}`; progress();
      const count = data.rows.filter(row => row.state === "reviewed").length;
      message(purpose === "progress" ? `Progress download requested. Keep the file named below to resume; this does not authorize assembly.` : `Decisions download requested: ${count} reviewed, ${data.rows.length - count} still open. Return the file named below for Word assembly.`);
      return true;
    } catch (error) {message(`Export failed: ${error.message}`, true); return false;}
  }
  function restore(data, fileName, legacy) {
    rows = copy(data.rows); views = makeViews(); dirty = false; pendingImport = null; saveStatus = `Resumed: ${fileName}`;
    byId("pending-import").hidden = true;
    draw(); byId("tools").open = false;
    message(legacy ? `Available edits restored from ${fileName} as a legacy draft. Review requests again before Word assembly; old files cannot restore drafts they omitted.` : `Saved choices and review states restored from ${fileName}.`);
  }

  byId("title").textContent = review.title;
  byId("identity").textContent = review.source.file + " · " + review.requests.length + " requests · Library version " + review.library.version;
  if (review.source_census) {
    const census = review.source_census;
    byId("source-status").textContent = census.comparison.status === "checked" ? "Source compared with the served document." : "Source comparison is partial; inspect the flagged passages below.";
    for (const issue of census.comparison.unresolved || []) byId("source-issues").append(el("li", typeof issue === "string" ? issue : JSON.stringify(issue)));
    for (const gap of census.gaps || []) byId("source-issues").append(el("li", `${gap.locator}: unmapped source material — ${gap.text}`));
  } else byId("source-status").textContent = "Legacy review: source comparison has not been recorded in this page.";
  for (const item of review.context) byId("context-content").append(el("h4", item.title), el("p", item.text, "context-text"), el("p", item.locator, "locator"));
  byId("context-content").append(el("p", "Library: " + review.library.id, "locator"));
  review.requests.forEach((request, i) => {
    const li = el("li"), a = el("a"); a.id = "nav-" + i; a.href = "#request-" + i;
    a.addEventListener("click", () => {byId("index").open = false;});
    li.append(a); byId("navigation").append(li);
  });
  byId("save").addEventListener("click", () => download("progress"));
  byId("export").addEventListener("click", () => {byId("tools").open = false; byId("index").open = false; download("assembly");});
  byId("batch").addEventListener("click", async () => {
    try {
      const original = exportRecord("progress"), sourceRows = rows;
      const data = await authorize(copy(original), false);
      await validate(data);
      check(rows === sourceRows && same(original, exportRecord("progress")), "Work changed while recording review. Try Mark all reviewed again. No new review actions were recorded.");
      applyApprovals(data);
      message("All current choices marked reviewed, including no objections. Requests needing input stay open. Save progress to keep this work, or Export for Word.");
    } catch (error) {message(`No new review actions were recorded. ${error.message}`, true);}
    draw(); byId("tools").open = false;
  });
  let importSerial = 0;
  byId("import").addEventListener("change", async event => {
    const file = event.target.files[0]; if (!file) return;
    const serial = ++importSerial;
    try {
      const original = JSON.parse(await file.text());
      const data = await validate(original, true);
      if (serial !== importSerial) return;
      const candidate = {data, fileName: file.name, legacy: original.format_version === 1};
      if (dirty) {
        pendingImport = candidate;
        byId("pending-import-name").textContent = `${file.name} · ${data.rows.filter(row => row.state === "reviewed").length} reviewed of ${data.rows.length}. Your current unsaved work is still open.`;
        byId("pending-import").hidden = false; byId("tools").open = false;
      } else restore(candidate.data, candidate.fileName, candidate.legacy);
    } catch (error) {message("Import failed; current choices kept: " + error.message, true);}
    event.target.value = "";
  });
  byId("save-before-import").addEventListener("click", () => download("progress"));
  byId("confirm-import").addEventListener("click", () => {if (pendingImport) restore(pendingImport.data, pendingImport.fileName, pendingImport.legacy);});
  byId("cancel-import").addEventListener("click", () => {pendingImport = null; byId("pending-import").hidden = true;});
  window.addEventListener("beforeunload", event => {if (dirty) {event.preventDefault(); event.returnValue = "";}});
  for (const id of ["index", "tools"]) {
    byId(id).addEventListener("toggle", () => {
      if (byId(id).open) byId(id === "index" ? "tools" : "index").open = false;
    });
  }
  document.addEventListener("keydown", event => {
    if (event.key === "Escape") {byId("index").open = false; byId("tools").open = false;}
  });
  document.addEventListener("click", event => {
    for (const id of ["index", "tools"]) if (!byId(id).contains(event.target)) byId(id).open = false;
  });
  const themeToggle = byId("theme-toggle");
  const systemDark = window.matchMedia("(prefers-color-scheme: dark)");
  function syncTheme() {
    const dark = (document.documentElement.dataset.theme || (systemDark.matches ? "dark" : "light")) === "dark";
    themeToggle.textContent = dark ? "Use light theme" : "Use dark theme";
    themeToggle.setAttribute("aria-pressed", String(dark));
  }
  themeToggle.addEventListener("click", () => {
    document.documentElement.dataset.theme = themeToggle.getAttribute("aria-pressed") === "true" ? "light" : "dark"; syncTheme();
  });
  systemDark.addEventListener("change", syncTheme);
  const toolbar = document.querySelector(".toolbar");
  const syncScrollOffset = () => {
    const height = getComputedStyle(toolbar).position === "sticky" ? Math.ceil(toolbar.getBoundingClientRect().height) : 0;
    document.documentElement.style.setProperty("--review-toolbar-height", height + "px");
  };
  if (typeof ResizeObserver !== "undefined") new ResizeObserver(syncScrollOffset).observe(toolbar);
  window.addEventListener("resize", syncScrollOffset);
  syncTheme(); draw(); syncScrollOffset();
})();
