// AgendaFácil — API (projeto fictício de demonstração; não usar em produção)
require('dotenv').config();
const express = require('express');
const helmet = require('helmet');

const agendamentos = require('../src/routes/agendamentos');
const { clinicaRouter, adminRouter } = require('../src/routes/clinica');
const { login, autenticar, exigirPapel } = require('../src/auth');

const app = express();
app.set('trust proxy', 1);

// Redireciona para HTTPS quando a requisição chega por HTTP atrás do proxy
app.use((req, res, next) => {
  if (process.env.NODE_ENV === 'production' && req.headers['x-forwarded-proto'] !== 'https') {
    return res.redirect(301, `https://${req.headers.host}${req.originalUrl}`);
  }
  return next();
});

// Cabeçalhos de segurança: CSP restritiva e HSTS
app.use(
  helmet({
    contentSecurityPolicy: {
      directives: {
        defaultSrc: ["'self'"],
        scriptSrc: ["'self'"],
        connectSrc: ["'self'"],
        frameAncestors: ["'none'"],
      },
    },
    hsts: { maxAge: 31536000, includeSubDomains: true },
  })
);

app.use(express.json({ limit: '50kb' }));

app.post('/api/login', login);
app.use('/api/agendamentos', agendamentos);
app.use('/api/clinica', autenticar, clinicaRouter);
app.use('/api/admin', autenticar, exigirPapel('admin'), adminRouter);

module.exports = app;

if (require.main === module) {
  const porta = process.env.PORT || 3000;
  app.listen(porta, () => console.log(`AgendaFácil API ouvindo na porta ${porta}`));
}
