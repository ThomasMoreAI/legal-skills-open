#!/usr/bin/env node
// MCP server · SAIJ (Sistema Argentino de Información Jurídica)
// Cero dependencias. Transporte stdio, JSON-RPC 2.0 delimitado por líneas.
// Solo lectura. Fuente: https://www.saij.gob.ar (Ministerio de Justicia, Argentina).
//
// TLS: los sitios .gob.ar sirven una cadena de certificados incompleta. En vez de
// desactivar la verificación (inseguro), este server se lanza con --use-system-ca,
// que usa el almacén de certificados del sistema operativo (contiene el intermedio).
//
// Herramientas:
//   saij_buscar_jurisprudencia { consulta, limite?, pagina? }
//   saij_buscar_legislacion    { consulta, limite?, pagina? }
//   saij_buscar_doctrina       { consulta, limite?, pagina? }
//   saij_documento             { uuid }

const BASE = "https://www.saij.gob.ar";
const UA = "Mozilla/5.0 (compatible; saij-mcp/1.0; +local)";
const FACET = {
  jurisprudencia: "Total|Tipo de Documento/Jurisprudencia",
  legislacion: "Total|Tipo de Documento/Legislación",
  doctrina: "Total|Tipo de Documento/Doctrina",
};

const log = (...a) => process.stderr.write("[saij-mcp] " + a.join(" ") + "\n");

// ---------- HTTP ----------
async function httpGetJson(url) {
  const ctrl = new AbortController();
  const t = setTimeout(() => ctrl.abort(), 30000);
  try {
    const res = await fetch(url, {
      headers: { Accept: "application/json", "User-Agent": UA, "Accept-Language": "es-AR" },
      signal: ctrl.signal,
      redirect: "follow",
    });
    const text = await res.text();
    if (res.status !== 200) throw new Error("HTTP " + res.status + " de SAIJ");
    return JSON.parse(text);
  } finally {
    clearTimeout(t);
  }
}

// ---------- Parseo de abstract ----------
function parseAbstract(raw) {
  try {
    const obj = typeof raw === "string" ? JSON.parse(raw) : raw;
    return obj.document || obj;
  } catch {
    return null;
  }
}

// Coacciona a texto: si es objeto SAIJ ({descripcion|texto|termino|codigo}), lo aplana.
function scalar(v) {
  if (v == null) return "";
  if (typeof v === "object") return scalar(v.descripcion ?? v.texto ?? v.termino ?? v.nombre ?? v.codigo ?? "");
  return String(v);
}

function pick(...vals) {
  for (const v of vals) {
    const s = scalar(v);
    if (s !== "") return s;
  }
  return "";
}

// Limpia el markup interno de SAIJ ([[p]] = párrafo, [[...]] = tags varios).
function limpiar(t) {
  return String(t)
    .replace(/\[\[p\]\]/gi, "\n")
    .replace(/\[\[\/?[a-z0-9 =:_-]*\]\]/gi, " ")
    .replace(/[ \t]+\n/g, "\n")
    .replace(/\n{3,}/g, "\n\n")
    .trim();
}

function firstDate(f) {
  if (!f) return "";
  const s = String(f);
  return s.includes("|") ? s.split("|")[0] + " (y otras)" : s;
}

function voces(content) {
  const d = content?.descriptores?.descriptor;
  if (!d) return [];
  const arr = Array.isArray(d) ? d : [d];
  return arr.map((x) => x?.elegido?.termino).filter(Boolean).slice(0, 8);
}

function summarize(doc, maxTexto) {
  if (!doc) return { titulo: "(sin metadatos)", texto: "" };
  const m = doc.metadata || {};
  const c = doc.content || {};
  const tipo = m["document-content-type"] || "";
  // "fallo": no trae 'titulo'; se compone desde actor + sobre (materia).
  const compuesto = [pick(c.actor), pick(c.sobre)].filter(Boolean).join(" · ");
  const titulo = pick(
    c.titulo, c["titulo-norma"], c["nombre-coloquial"], c.caratula, c.sobre, compuesto,
    c["numero-norma"], "(sin título)"
  );
  const texto = pick(c.texto, c["texto-doc"], c["texto-completo"], c.sintesis, c.sumario, "");
  return {
    tipo,
    titulo,
    numero: pick(c["numero-sumario"], c["numero-interno"], c["numero-norma"], c["numero-fallo"]),
    tipoNorma: pick(c["tipo-norma"]),
    tribunal: pick(c["tipo-tribunal"], c.tribunal, c.organismo),
    jurisdiccion: pick(c?.jurisdiccion?.descripcion, c?.jurisdiccion?.codigo),
    fecha: firstDate(pick(c.fecha, c["fecha-firma"])),
    estado: pick(c?.estado?.descripcion, c.estado),
    voces: voces(c),
    texto: maxTexto ? limpiar(texto).replace(/\s+/g, " ").slice(0, maxTexto) : limpiar(texto),
  };
}

// ---------- Búsqueda ----------
async function buscar(tipo, consulta, limite, pagina) {
  const p = Math.min(Math.max(parseInt(limite) || 8, 1), 25);
  const pag = Math.max(parseInt(pagina) || 1, 1);
  const offset = (pag - 1) * p;
  const url =
    `${BASE}/busqueda?o=${offset}&p=${p}&v=colapsada` +
    `&f=${encodeURIComponent(FACET[tipo])}&q=${encodeURIComponent(consulta)}`;
  const j = await httpGetJson(url);
  const list = j?.searchResults?.documentResultList || [];
  const results = list.map((it) => {
    const s = summarize(parseAbstract(it.documentAbstract), 700);
    return { uuid: it.uuid, url: `${BASE}/${it.uuid}`, ...s };
  });
  return { pagina: pag, porPagina: p, devueltos: results.length, hayMas: results.length === p, results };
}

function renderBusqueda(tipo, consulta, r) {
  if (r.devueltos === 0)
    return `Sin resultados en SAIJ para "${consulta}" (${tipo}, página ${r.pagina}).`;
  const head =
    `SAIJ · ${tipo} · "${consulta}" — página ${r.pagina}, ${r.devueltos} resultado(s)` +
    (r.hayMas ? ` (hay más: pedí pagina=${r.pagina + 1})` : ` (última página)`) +
    `\n`;
  const items = r.results
    .map((x, i) => {
      const n = (r.pagina - 1) * r.porPagina + i + 1;
      const meta = [x.tipoNorma, x.tribunal, x.jurisdiccion, x.fecha, x.estado].filter(Boolean).join(" · ");
      const voc = x.voces.length ? `\n   Voces: ${x.voces.join("; ")}` : "";
      return (
        `${n}. ${x.titulo}` +
        (meta ? `\n   ${meta}` : "") +
        voc +
        (x.texto ? `\n   « ${x.texto}${x.texto.length >= 700 ? "…" : ""} »` : "") +
        `\n   uuid: ${x.uuid}\n   ${x.url}`
      );
    })
    .join("\n\n");
  return (
    head +
    "\n" +
    items +
    `\n\n(Para el texto completo de un ítem: saij_documento con su uuid. ` +
    `Verificá siempre en la fuente antes de citar.)`
  );
}

// ---------- Documento completo ----------
async function documento(uuid) {
  if (!uuid) throw new Error("Falta el parámetro uuid.");
  const url = `${BASE}/view-document?guid=${encodeURIComponent(uuid)}`;
  const j = await httpGetJson(url);
  const doc = parseAbstract(j.data ?? j);
  const s = summarize(doc, 0);
  const meta = [s.tipo, s.tipoNorma, s.tribunal, s.jurisdiccion, s.fecha, s.estado].filter(Boolean).join(" · ");
  const voc = s.voces.length ? `Voces: ${s.voces.join("; ")}\n` : "";
  const texto = s.texto ? s.texto : "(sin texto en el documento)";
  return (
    `SAIJ · Documento ${uuid}\n${s.titulo}\n${meta}\n${voc}Fuente: ${BASE}/${uuid}\n\n${texto}`
  );
}

// ---------- Definición de tools ----------
const searchSchema = {
  type: "object",
  properties: {
    consulta: { type: "string", description: "Términos de búsqueda en lenguaje natural (ej: 'despido discriminatorio')." },
    limite: { type: "integer", description: "Resultados por página (1-25, def. 8).", default: 8 },
    pagina: { type: "integer", description: "Número de página (def. 1).", default: 1 },
  },
  required: ["consulta"],
};

const TOOLS = [
  {
    name: "saij_buscar_jurisprudencia",
    description:
      "Busca jurisprudencia argentina (sumarios y fallos) en SAIJ: sentencias, doctrina judicial, criterios de tribunales nacionales, federales y provinciales. Devuelve título, tribunal, jurisdicción, voces temáticas, un extracto y el uuid para pedir el texto completo.",
    inputSchema: searchSchema,
    handler: (a) => buscar("jurisprudencia", a.consulta, a.limite, a.pagina).then((r) => renderBusqueda("jurisprudencia", a.consulta, r)),
  },
  {
    name: "saij_buscar_legislacion",
    description:
      "Busca legislación argentina en SAIJ: leyes, decretos, resoluciones y normativa nacional y provincial, con su estado de vigencia. Devuelve tipo y número de norma, fecha, estado, un extracto y el uuid.",
    inputSchema: searchSchema,
    handler: (a) => buscar("legislacion", a.consulta, a.limite, a.pagina).then((r) => renderBusqueda("legislación", a.consulta, r)),
  },
  {
    name: "saij_buscar_doctrina",
    description:
      "Busca doctrina jurídica argentina en SAIJ: artículos y análisis de autores sobre instituciones del derecho argentino. Devuelve título, autor/fuente cuando está disponible, un extracto y el uuid.",
    inputSchema: searchSchema,
    handler: (a) => buscar("doctrina", a.consulta, a.limite, a.pagina).then((r) => renderBusqueda("doctrina", a.consulta, r)),
  },
  {
    name: "saij_documento",
    description:
      "Recupera el texto y los metadatos completos de un documento de SAIJ a partir de su uuid (obtenido de las búsquedas). Usar para leer el fallo, la norma o la doctrina completa antes de citarla.",
    inputSchema: {
      type: "object",
      properties: { uuid: { type: "string", description: "El uuid del documento devuelto por una búsqueda." } },
      required: ["uuid"],
    },
    handler: (a) => documento(a.uuid),
  },
];

// ---------- JSON-RPC / MCP stdio ----------
function send(msg) {
  process.stdout.write(JSON.stringify(msg) + "\n");
}
function reply(id, result) {
  send({ jsonrpc: "2.0", id, result });
}
function replyError(id, code, message) {
  send({ jsonrpc: "2.0", id, error: { code, message } });
}

async function handle(msg) {
  const { id, method, params } = msg;
  if (method === "initialize") {
    return reply(id, {
      protocolVersion: params?.protocolVersion || "2024-11-05",
      capabilities: { tools: {} },
      serverInfo: { name: "saij-mcp", version: "1.0.0" },
    });
  }
  if (method === "notifications/initialized" || method === "notifications/cancelled") return; // sin respuesta
  if (method === "ping") return reply(id, {});
  if (method === "tools/list") {
    return reply(id, { tools: TOOLS.map(({ name, description, inputSchema }) => ({ name, description, inputSchema })) });
  }
  if (method === "tools/call") {
    const tool = TOOLS.find((t) => t.name === params?.name);
    if (!tool) return replyError(id, -32602, "Herramienta desconocida: " + params?.name);
    try {
      const text = await tool.handler(params.arguments || {});
      return reply(id, { content: [{ type: "text", text }] });
    } catch (e) {
      log("error en", params?.name, ":", e.message);
      return reply(id, { content: [{ type: "text", text: "Error consultando SAIJ: " + e.message }], isError: true });
    }
  }
  if (id !== undefined) return replyError(id, -32601, "Método no soportado: " + method);
}

let buffer = "";
process.stdin.setEncoding("utf8");
process.stdin.on("data", (chunk) => {
  buffer += chunk;
  let nl;
  while ((nl = buffer.indexOf("\n")) !== -1) {
    const line = buffer.slice(0, nl).trim();
    buffer = buffer.slice(nl + 1);
    if (!line) continue;
    let msg;
    try {
      msg = JSON.parse(line);
    } catch {
      log("línea no-JSON ignorada");
      continue;
    }
    Promise.resolve(handle(msg)).catch((e) => log("handler fatal:", e.message));
  }
});
process.stdin.on("end", () => process.exit(0));
log("SAIJ MCP server listo (stdio).");
