// Servidor de la barberia. Node puro, sin dependencias.
//
// Igual que db.js, tiene errores a proposito. El mas importante vive
// en la ruta POST /cliente/:id/eliminar.

import { createServer } from 'node:http';
import { db, log, exportarACrm } from './db.js';

const PUERTO = process.env.PORT || 3000;

const esc = (v) => String(v ?? '')
  .replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;')
  .replaceAll('"', '&quot;');

const CSS = `
  * { box-sizing: border-box; }
  body {
    margin: 0; background: #f5f4f1; color: #1b1a17;
    font: 17px/1.55 ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  }
  .wrap { max-width: 860px; margin: 0 auto; padding: 2.5rem 1.5rem 5rem; }
  header { display: flex; align-items: baseline; gap: .8rem; flex-wrap: wrap;
    border-bottom: 2px solid #1b1a17; padding-bottom: 1rem; margin-bottom: 2rem; }
  header h1 { margin: 0; font-size: 1.6rem; letter-spacing: -.01em; }
  header span { color: #6f6a60; font-size: .9rem; }
  h2 { font-size: 1.2rem; margin: 2rem 0 .8rem; }
  a { color: #8a3a1e; }
  .card { background: #fff; border: 1px solid #ddd9d2; border-radius: 6px;
    padding: 1.2rem 1.4rem; margin-bottom: 1rem; }
  .card h3 { margin: 0 0 .3rem; font-size: 1.05rem; }
  .card .sub { color: #6f6a60; font-size: .9rem; }
  table { width: 100%; border-collapse: collapse; font-size: .95rem; }
  td { padding: .45rem .2rem; border-bottom: 1px solid #eeebe6; vertical-align: top; }
  td.k { color: #6f6a60; width: 42%; white-space: nowrap; }
  .pill { display: inline-block; font-size: .75rem; padding: .15em .55em;
    border-radius: 99px; background: #eeebe6; color: #6f6a60; }
  .pill.off { background: #f6dcdc; color: #8a2020; }
  form.danger { margin-top: 1.5rem; }
  button {
    font: inherit; font-size: .95rem; padding: .6rem 1.1rem; border-radius: 5px;
    border: 1px solid #8a2020; background: #8a2020; color: #fff; cursor: pointer;
  }
  button:hover { background: #6f1919; }
  button:focus-visible { outline: 3px solid #1b1a17; outline-offset: 2px; }
  .aviso { background: #e6f2e8; border: 1px solid #b7d8bf; color: #1f5c2e;
    padding: 1rem 1.2rem; border-radius: 6px; margin-bottom: 1.5rem; }
  .aviso b { display: block; margin-bottom: .2rem; }
  label { display: block; margin-bottom: .9rem; font-size: .92rem; }
  label span { display: block; color: #6f6a60; margin-bottom: .25rem; }
  input { font: inherit; width: 100%; padding: .5rem .65rem;
    border: 1px solid #ccc7bf; border-radius: 4px; background: #fff; }
  .cols { display: grid; grid-template-columns: 1fr 1fr; gap: 0 1.2rem; }
  @media (max-width: 620px) { .cols { grid-template-columns: 1fr; } }
  footer { margin-top: 3rem; padding-top: 1rem; border-top: 1px solid #ddd9d2;
    color: #6f6a60; font-size: .85rem; }
`;

const pagina = (titulo, cuerpo) => `<!doctype html>
<html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${esc(titulo)} · Barberia El Corte</title><style>${CSS}</style></head>
<body><div class="wrap">
<header><h1>Barberia El Corte</h1><span>Sistema de citas</span></header>
${cuerpo}
<footer>Proyecto de demostracion para la clase de la Ley 21.719. No usar en produccion.</footer>
</div></body></html>`;

function vistaIndex() {
  const clientes = db.prepare('SELECT * FROM clientes ORDER BY id').all();
  const tarjetas = clientes.map((c) => `
    <div class="card">
      <h3><a href="/cliente/${c.id}">${esc(c.nombre)} ${esc(c.apellido)}</a>
        ${c.activo ? '' : '<span class="pill off">cuenta eliminada</span>'}</h3>
      <div class="sub">${esc(c.rut)} · ${esc(c.telefono)} · ${esc(c.comuna)}</div>
    </div>`).join('');

  return pagina('Clientes', `
    <h2>Clientes registrados</h2>
    ${tarjetas || '<p>No hay clientes. Corre <code>npm run seed</code>.</p>'}
    <p style="margin-top:2rem"><a href="/registro">Registrar un cliente nuevo</a></p>`);
}

function vistaCliente(id) {
  const c = db.prepare('SELECT * FROM clientes WHERE id = ?').get(id);
  if (!c) return null;

  const citas = db.prepare('SELECT * FROM citas WHERE cliente_id = ?').all(id);
  const score = db.prepare('SELECT * FROM scoring WHERE cliente_id = ?').get(id);

  const fila = (k, v) => `<tr><td class="k">${esc(k)}</td><td>${esc(v)}</td></tr>`;

  return pagina(`${c.nombre} ${c.apellido}`, `
    <h2>${esc(c.nombre)} ${esc(c.apellido)}
      ${c.activo ? '' : '<span class="pill off">cuenta eliminada</span>'}</h2>

    <div class="card"><table>
      ${fila('RUT', c.rut)}
      ${fila('Correo', c.email)}
      ${fila('Telefono', c.telefono)}
      ${fila('Fecha de nacimiento', c.fecha_nacimiento)}
      ${fila('Direccion', `${c.direccion}, ${c.comuna}`)}
      ${fila('Coordenadas', `${c.lat}, ${c.lng}`)}
      ${fila('Ocupacion', c.ocupacion)}
      ${fila('Ingreso mensual declarado', `$${Number(c.ingreso_mensual).toLocaleString('es-CL')}`)}
      ${fila('Foto', c.foto_url)}
      ${fila('Contacto de emergencia', `${c.contacto_emergencia_nombre} · ${c.contacto_emergencia_tel}`)}
      ${fila('Acepto terminos', c.acepto_todo ? 'si' : 'no')}
    </table></div>

    <h2>Citas</h2>
    ${citas.map((v) => `<div class="card">
      <h3>${esc(v.fecha)}</h3>
      <div class="sub">${esc(v.servicio)} — ${esc(v.notas)}</div></div>`).join('') || '<p>Sin citas.</p>'}

    <h2>Evaluacion interna</h2>
    <div class="card">
      <h3>${esc(score?.etiqueta ?? 'sin evaluar')}</h3>
      <div class="sub">Puntaje ${esc(score?.puntaje ?? '-')} de 100 · calculado el ${esc(score?.decidido_en ?? '-')}</div>
    </div>

    ${c.activo ? `
    <form class="danger" method="POST" action="/cliente/${c.id}/eliminar">
      <button type="submit">Eliminar mi cuenta y todos mis datos</button>
    </form>` : ''}

    <p style="margin-top:2rem"><a href="/">Volver</a></p>`);
}

function vistaRegistro() {
  const campo = (n, l, t = 'text') =>
    `<label><span>${esc(l)}</span><input type="${t}" name="${n}"></label>`;

  return pagina('Registro', `
    <h2>Agenda tu corte</h2>
    <p class="sub" style="color:#6f6a60">Completa tus datos para reservar.</p>
    <div class="card"><form method="POST" action="/registro"><div class="cols">
      ${campo('nombre', 'Nombre')}
      ${campo('apellido', 'Apellido')}
      ${campo('rut', 'RUT')}
      ${campo('email', 'Correo', 'email')}
      ${campo('telefono', 'Telefono')}
      ${campo('fecha_nacimiento', 'Fecha de nacimiento', 'date')}
      ${campo('direccion', 'Direccion')}
      ${campo('comuna', 'Comuna')}
      ${campo('ocupacion', 'Ocupacion')}
      ${campo('ingreso_mensual', 'Ingreso mensual', 'number')}
      ${campo('contacto_emergencia_nombre', 'Contacto de emergencia')}
      ${campo('contacto_emergencia_tel', 'Telefono de ese contacto')}
    </div>
    <label style="margin-top:.5rem">
      <input type="checkbox" name="acepto_todo" checked style="width:auto;margin-right:.5rem">
      Acepto los terminos, la politica de privacidad, el envio de promociones
      y la comparticion de mis datos con terceros
    </label>
    <button type="submit" style="background:#1b1a17;border-color:#1b1a17">Reservar</button>
    </form></div>
    <p style="margin-top:2rem"><a href="/">Volver</a></p>`);
}

// [SEMBRADO 3, continuacion] Aqui esta el corazon de la demo.
// El boton promete borrar todo. Lo unico que ocurre es un UPDATE de una bandera.
// La fila sigue completa, y sus copias en auditoria, webhooks, el log y el CRM
// ni siquiera se tocan.
function eliminarCuenta(id) {
  db.prepare('UPDATE clientes SET activo = 0 WHERE id = ?').run(id);
  log(`baja logica cliente id=${id}`);
  return pagina('Cuenta eliminada', `
    <div class="aviso">
      <b>Listo, tu cuenta fue eliminada.</b>
      Todos tus datos personales fueron borrados de forma permanente de nuestros sistemas.
    </div>
    <p>Gracias por haber sido parte de Barberia El Corte.</p>
    <p style="margin-top:2rem"><a href="/">Volver al inicio</a></p>`);
}

function crearCliente(datos) {
  const { lastInsertRowid: id } = db.prepare(`
    INSERT INTO clientes (nombre, apellido, rut, email, telefono, fecha_nacimiento,
      direccion, comuna, ocupacion, ingreso_mensual,
      contacto_emergencia_nombre, contacto_emergencia_tel, acepto_todo)
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
  `).run(
    datos.nombre || '', datos.apellido || '', datos.rut || '', datos.email || '',
    datos.telefono || '', datos.fecha_nacimiento || '', datos.direccion || '',
    datos.comuna || '', datos.ocupacion || '', Number(datos.ingreso_mensual) || 0,
    datos.contacto_emergencia_nombre || '', datos.contacto_emergencia_tel || '',
    datos.acepto_todo ? 1 : 0,
  );

  const fila = db.prepare('SELECT * FROM clientes WHERE id = ?').get(id);
  db.prepare('INSERT INTO auditoria (tabla, accion, registro_json) VALUES (?,?,?)')
    .run('clientes', 'alta', JSON.stringify(fila));
  db.prepare('INSERT INTO webhooks (evento, destino, payload_json) VALUES (?,?,?)')
    .run('cliente.creado', 'https://hooks.crm-externo.example/barberia', JSON.stringify(fila));
  log(`alta cliente id=${id} rut=${datos.rut} tel=${datos.telefono} email=${datos.email}`);
  exportarACrm();
  return id;
}

const leerCuerpo = (req) => new Promise((resolve) => {
  let bruto = '';
  req.on('data', (t) => { bruto += t; });
  req.on('end', () => resolve(Object.fromEntries(new URLSearchParams(bruto))));
});

const responder = (res, html, codigo = 200) => {
  res.writeHead(codigo, { 'Content-Type': 'text/html; charset=utf-8' });
  res.end(html);
};

createServer(async (req, res) => {
  const url = new URL(req.url, `http://${req.headers.host}`);
  const ruta = url.pathname;

  if (req.method === 'GET' && ruta === '/') return responder(res, vistaIndex());
  if (req.method === 'GET' && ruta === '/registro') return responder(res, vistaRegistro());

  if (req.method === 'POST' && ruta === '/registro') {
    const id = crearCliente(await leerCuerpo(req));
    res.writeHead(302, { Location: `/cliente/${id}` });
    return res.end();
  }

  const verCliente = ruta.match(/^\/cliente\/(\d+)$/);
  if (req.method === 'GET' && verCliente) {
    const html = vistaCliente(Number(verCliente[1]));
    return html ? responder(res, html) : responder(res, pagina('No encontrado', '<p>Ese cliente no existe.</p>'), 404);
  }

  const borrar = ruta.match(/^\/cliente\/(\d+)\/eliminar$/);
  if (req.method === 'POST' && borrar) {
    return responder(res, eliminarCuenta(Number(borrar[1])));
  }

  responder(res, pagina('No encontrado', '<p>Esa pagina no existe.</p>'), 404);
}).listen(PUERTO, () => {
  console.log(`Barberia El Corte corriendo en http://localhost:${PUERTO}`);
});
