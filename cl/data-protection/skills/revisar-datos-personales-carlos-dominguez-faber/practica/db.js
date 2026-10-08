// Esquema y datos de la barberia.
//
// Este archivo tiene errores a proposito. No lo copies a un proyecto real.
// Cada bloque marcado con [SEMBRADO] es una violacion deliberada de la Ley 21.719
// que la clase va a encontrar y arreglar en vivo.

import { DatabaseSync } from 'node:sqlite';
import { mkdirSync, writeFileSync, rmSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const raiz = dirname(fileURLToPath(import.meta.url));
export const CARPETA_DATOS = join(raiz, 'datos');
export const RUTA_DB = join(CARPETA_DATOS, 'barberia.db');
export const RUTA_LOG = join(CARPETA_DATOS, 'app.log');
export const RUTA_CRM = join(CARPETA_DATOS, 'crm-export.json');

mkdirSync(CARPETA_DATOS, { recursive: true });

export const db = new DatabaseSync(RUTA_DB);

db.exec(`
  PRAGMA journal_mode = WAL;

  -- [SEMBRADO 1] Minimizacion (art. 3 c y art. 14 quater).
  -- Para agendar un corte de pelo basta el nombre y un telefono.
  -- Esta tabla pide diecinueve campos, incluidos RUT, direccion,
  -- coordenadas, ingreso mensual y el telefono de un tercero.
  CREATE TABLE IF NOT EXISTS clientes (
    id                        INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre                    TEXT NOT NULL,
    apellido                  TEXT,
    rut                       TEXT,
    email                     TEXT,
    telefono                  TEXT,
    fecha_nacimiento          TEXT,
    direccion                 TEXT,
    comuna                    TEXT,
    lat                       REAL,
    lng                       REAL,
    ocupacion                 TEXT,
    ingreso_mensual           INTEGER,
    foto_url                  TEXT,
    contacto_emergencia_nombre TEXT,
    contacto_emergencia_tel   TEXT,

    -- [SEMBRADO 2] Consentimiento (art. 12 y art. 14 ter k).
    -- Un solo booleano para todas las finalidades juntas, sin fecha,
    -- sin version del texto aceptado y sin forma de retirarlo.
    acepto_todo               INTEGER DEFAULT 1,

    -- [SEMBRADO 3] Supresion (art. 8 y art. 11).
    -- El boton de eliminar cuenta solo mueve esta bandera a 0.
    activo                    INTEGER DEFAULT 1,
    creado_en                 TEXT DEFAULT CURRENT_TIMESTAMP
  );

  -- [SEMBRADO 4] La auditoria guarda el registro completo en JSON,
  -- asi que sobrevive intacta al borrado de la fila original.
  CREATE TABLE IF NOT EXISTS auditoria (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    tabla         TEXT,
    accion        TEXT,
    registro_json TEXT,
    creado_en     TEXT DEFAULT CURRENT_TIMESTAMP
  );

  -- [SEMBRADO 5] Datos de salud en un campo de texto libre (art. 2 y art. 16).
  -- "alergia a tinte" es un dato sensible viviendo en la columna de notas.
  CREATE TABLE IF NOT EXISTS citas (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER,
    fecha      TEXT,
    servicio   TEXT,
    notas      TEXT
  );

  -- [SEMBRADO 6] Decision automatizada sin trazabilidad (art. 8 bis).
  -- Etiqueta al cliente sin guardar que factores pesaron, con que version
  -- del modelo se decidio, ni forma de pedir revision humana.
  CREATE TABLE IF NOT EXISTS scoring (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id  INTEGER,
    puntaje     INTEGER,
    etiqueta    TEXT,
    decidido_en TEXT DEFAULT CURRENT_TIMESTAMP
  );

  -- [SEMBRADO 7] Cola de webhooks con el payload completo hacia un tercero.
  CREATE TABLE IF NOT EXISTS webhooks (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    evento       TEXT,
    destino      TEXT,
    payload_json TEXT,
    enviado_en   TEXT DEFAULT CURRENT_TIMESTAMP
  );
`);

// [SEMBRADO 8] El log de la aplicacion escribe RUT y telefono en texto plano.
export function log(mensaje) {
  const linea = `${new Date().toISOString()} ${mensaje}\n`;
  writeFileSync(RUTA_LOG, linea, { flag: 'a' });
}

// [SEMBRADO 9] Export hacia un CRM externo. Una vez que sale de aqui,
// nadie sabe donde vive ni quien lo borra.
export function exportarACrm() {
  const filas = db.prepare('SELECT * FROM clientes').all();
  writeFileSync(RUTA_CRM, JSON.stringify(filas, null, 2));
  return filas.length;
}

const CLIENTES_DEMO = [
  {
    nombre: 'Camila', apellido: 'Fuentes', rut: '18.402.551-K',
    email: 'camila.fuentes@example.cl', telefono: '+56 9 8123 4567',
    fecha_nacimiento: '1993-04-18', direccion: 'Los Aromos 1240, depto 703',
    comuna: 'Providencia', lat: -33.4265, lng: -70.6102,
    ocupacion: 'Disenadora', ingreso_mensual: 1450000,
    foto_url: 'https://cdn.example.cl/fotos/camila.jpg',
    contacto_emergencia_nombre: 'Rosa Fuentes', contacto_emergencia_tel: '+56 9 7411 2233',
    cita: { fecha: '2026-08-04 10:30', servicio: 'Corte y barba', notas: 'Alergica al tinte con amoniaco' },
    scoring: { puntaje: 34, etiqueta: 'riesgo alto de no asistir' },
  },
  {
    nombre: 'Matias', apellido: 'Rojas', rut: '20.115.883-4',
    email: 'm.rojas@example.cl', telefono: '+56 9 6622 8890',
    fecha_nacimiento: '2000-11-02', direccion: 'Pasaje El Roble 88',
    comuna: 'Nunoa', lat: -33.4569, lng: -70.5975,
    ocupacion: 'Estudiante', ingreso_mensual: 320000,
    foto_url: 'https://cdn.example.cl/fotos/matias.jpg',
    contacto_emergencia_nombre: 'Ana Rojas', contacto_emergencia_tel: '+56 9 5510 4477',
    cita: { fecha: '2026-08-05 16:00', servicio: 'Corte fade', notas: 'Prefiere maquina 2' },
    scoring: { puntaje: 71, etiqueta: 'cliente preferente' },
  },
  {
    nombre: 'Ignacio', apellido: 'Bravo', rut: '16.998.204-1',
    email: 'nacho.bravo@example.cl', telefono: '+56 9 4477 1102',
    fecha_nacimiento: '1988-07-25', direccion: 'Av. Vicuna Mackenna 4520',
    comuna: 'Macul', lat: -33.4890, lng: -70.6011,
    ocupacion: 'Contador', ingreso_mensual: 2100000,
    foto_url: 'https://cdn.example.cl/fotos/ignacio.jpg',
    contacto_emergencia_nombre: 'Paula Bravo', contacto_emergencia_tel: '+56 9 3302 5566',
    cita: { fecha: '2026-08-06 09:00', servicio: 'Afeitado clasico', notas: 'Piel sensible, usa crema medicada' },
    scoring: { puntaje: 12, etiqueta: 'no ofrecer promociones' },
  },
];

export function sembrar() {
  const insertar = db.prepare(`
    INSERT INTO clientes (
      nombre, apellido, rut, email, telefono, fecha_nacimiento, direccion, comuna,
      lat, lng, ocupacion, ingreso_mensual, foto_url,
      contacto_emergencia_nombre, contacto_emergencia_tel
    ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
  `);

  for (const c of CLIENTES_DEMO) {
    const { lastInsertRowid: id } = insertar.run(
      c.nombre, c.apellido, c.rut, c.email, c.telefono, c.fecha_nacimiento,
      c.direccion, c.comuna, c.lat, c.lng, c.ocupacion, c.ingreso_mensual,
      c.foto_url, c.contacto_emergencia_nombre, c.contacto_emergencia_tel,
    );

    db.prepare('INSERT INTO citas (cliente_id, fecha, servicio, notas) VALUES (?,?,?,?)')
      .run(id, c.cita.fecha, c.cita.servicio, c.cita.notas);

    db.prepare('INSERT INTO scoring (cliente_id, puntaje, etiqueta) VALUES (?,?,?)')
      .run(id, c.scoring.puntaje, c.scoring.etiqueta);

    const fila = db.prepare('SELECT * FROM clientes WHERE id = ?').get(id);

    db.prepare('INSERT INTO auditoria (tabla, accion, registro_json) VALUES (?,?,?)')
      .run('clientes', 'alta', JSON.stringify(fila));

    db.prepare('INSERT INTO webhooks (evento, destino, payload_json) VALUES (?,?,?)')
      .run('cliente.creado', 'https://hooks.crm-externo.example/barberia', JSON.stringify(fila));

    log(`alta cliente id=${id} rut=${c.rut} tel=${c.telefono} email=${c.email}`);
  }

  exportarACrm();
  return CLIENTES_DEMO.length;
}

function reiniciar() {
  db.close();
  rmSync(CARPETA_DATOS, { recursive: true, force: true });
  mkdirSync(CARPETA_DATOS, { recursive: true });
}

if (process.argv.includes('--reset')) {
  reiniciar();
  console.log('Datos borrados. Corre "npm run seed" para volver a empezar.');
} else if (process.argv.includes('--seed')) {
  const n = sembrar();
  console.log(`Listo: ${n} clientes cargados en datos/barberia.db`);
  console.log('Ahora corre "npm start" y abre http://localhost:3000');
}
