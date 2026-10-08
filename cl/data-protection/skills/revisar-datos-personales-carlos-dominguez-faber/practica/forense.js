// Busca a una persona en todos los rincones del sistema despues de que
// "elimino su cuenta". Este archivo NO tiene errores sembrados: es la
// herramienta que destapa los de los otros.
//
//   node forense.js 18.402.551-K
//   node forense.js Camila

import { readFileSync, existsSync } from 'node:fs';
import { db, RUTA_LOG, RUTA_CRM } from './db.js';

const BUSCADO = process.argv.slice(2).join(' ').trim();

if (!BUSCADO) {
  console.error('Uso: node forense.js <rut, nombre, correo o telefono>');
  console.error('Ejemplo: node forense.js 18.402.551-K');
  process.exit(1);
}

const C = {
  reset: '\x1b[0m', dim: '\x1b[2m', bold: '\x1b[1m',
  rojo: '\x1b[31m', verde: '\x1b[32m', ambar: '\x1b[33m', cyan: '\x1b[36m',
};

const aguja = BUSCADO.toLowerCase();
const contiene = (v) => String(v ?? '').toLowerCase().includes(aguja);
const filaCoincide = (fila) => Object.values(fila).some(contiene);

const hallazgos = [];

function revisar(lugar, articulo, detalle, encontrado, muestra) {
  hallazgos.push({ lugar, articulo, detalle, encontrado, muestra });
}

// 1. La tabla principal
const clientes = db.prepare('SELECT * FROM clientes').all().filter(filaCoincide);
const borrados = clientes.filter((c) => !c.activo);
revisar(
  'Tabla clientes',
  'art. 8 · derecho de supresion',
  borrados.length
    ? 'La cuenta figura como eliminada, pero la fila sigue completa en la base'
    : 'Registro activo',
  clientes.length > 0,
  clientes[0] && `id=${clientes[0].id} · ${clientes[0].nombre} ${clientes[0].apellido} · ${clientes[0].rut} · ${clientes[0].direccion}`,
);

// 2. Auditoria
const auditoria = db.prepare('SELECT * FROM auditoria').all().filter((r) => contiene(r.registro_json));
revisar(
  'Tabla auditoria',
  'art. 8 · derecho de supresion',
  'Guarda una copia integra del registro en JSON, incluida despues del borrado',
  auditoria.length > 0,
  auditoria[0] && `${auditoria.length} evento(s) · ${auditoria[0].registro_json.slice(0, 90)}...`,
);

// 3. Citas: datos de salud en texto libre
const citas = db.prepare(`
  SELECT c.*, cl.nombre, cl.apellido, cl.rut FROM citas c
  JOIN clientes cl ON cl.id = c.cliente_id
`).all().filter(filaCoincide);
revisar(
  'Tabla citas',
  'art. 16 · datos sensibles',
  'Las notas de la cita guardan informacion de salud en texto libre',
  citas.length > 0,
  citas[0] && `"${citas[0].notas}"`,
);

// 4. Scoring
const scoring = db.prepare(`
  SELECT s.*, cl.nombre, cl.apellido, cl.rut FROM scoring s
  JOIN clientes cl ON cl.id = s.cliente_id
`).all().filter(filaCoincide);
revisar(
  'Tabla scoring',
  'art. 8 bis · decisiones automatizadas',
  'Etiqueta a la persona sin guardar los factores, la version del modelo ni quien puede revisarla',
  scoring.length > 0,
  scoring[0] && `"${scoring[0].etiqueta}" · puntaje ${scoring[0].puntaje}`,
);

// 5. Webhooks
const webhooks = db.prepare('SELECT * FROM webhooks').all().filter((r) => contiene(r.payload_json));
revisar(
  'Cola de webhooks',
  'art. 15 bis · encargados',
  'El registro completo ya salio hacia un tercero y esa copia no la controlas',
  webhooks.length > 0,
  webhooks[0] && `${webhooks.length} envio(s) a ${webhooks[0].destino}`,
);

// 6. Log de la aplicacion
let lineasLog = [];
if (existsSync(RUTA_LOG)) {
  lineasLog = readFileSync(RUTA_LOG, 'utf8').split('\n').filter(contiene);
}
revisar(
  'datos/app.log',
  'art. 3 c · proporcionalidad',
  'El log escribe RUT, telefono y correo en texto plano',
  lineasLog.length > 0,
  lineasLog[0]?.slice(0, 100),
);

// 7. Export al CRM
let enCrm = [];
if (existsSync(RUTA_CRM)) {
  try {
    enCrm = JSON.parse(readFileSync(RUTA_CRM, 'utf8')).filter(filaCoincide);
  } catch { /* archivo corrupto, se reporta como no encontrado */ }
}
revisar(
  'datos/crm-export.json',
  'arts. 27 a 29 · transferencia',
  'Copia exportada a un sistema externo, fuera del alcance de tu borrado',
  enCrm.length > 0,
  enCrm[0] && `${enCrm.length} registro(s) · ${enCrm[0].nombre} ${enCrm[0].apellido} · ${enCrm[0].email}`,
);

// ---------- salida ----------

const vivos = hallazgos.filter((h) => h.encontrado);

console.log(`\n${C.bold}Rastreo de "${BUSCADO}"${C.reset}`);
console.log(`${C.dim}Despues de que esta persona uso el boton "eliminar mi cuenta"${C.reset}\n`);

for (const h of hallazgos) {
  const marca = h.encontrado ? `${C.rojo}ENCONTRADO${C.reset}` : `${C.verde}limpio    ${C.reset}`;
  console.log(`  ${marca}  ${C.bold}${h.lugar}${C.reset}  ${C.dim}${h.articulo}${C.reset}`);
  if (h.encontrado) {
    console.log(`              ${h.detalle}`);
    if (h.muestra) console.log(`              ${C.cyan}${h.muestra}${C.reset}`);
  }
  console.log('');
}

const color = vivos.length ? C.rojo : C.verde;
console.log(`${color}${C.bold}Sigue presente en ${vivos.length} de ${hallazgos.length} lugares.${C.reset}`);

if (vivos.length) {
  console.log(`
${C.ambar}La app le dijo a esta persona que sus datos fueron borrados
de forma permanente. No es cierto.${C.reset}

El borrado no es una consulta, es un mapa: hay que recorrer cada
copia que el sistema fue dejando por el camino.
`);
}
