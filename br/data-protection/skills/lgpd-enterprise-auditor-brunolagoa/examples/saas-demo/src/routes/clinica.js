const express = require('express');
const db = require('../db');

const clinicaRouter = express.Router();
const adminRouter = express.Router();

// Agenda do dia, restrita à clínica do usuário autenticado
clinicaRouter.get('/agenda', async (req, res) => {
  const { rows } = await db.query(
    `SELECT a.codigo, a.data_hora, a.observacoes, p.id AS paciente_id, p.nome, p.telefone
       FROM agendamentos a
       JOIN pacientes p ON p.id = a.paciente_id
      WHERE p.clinica_id = $1 AND a.data_hora::date = CURRENT_DATE
      ORDER BY a.data_hora`,
    [req.usuario.clinica]
  );
  res.json(rows);
});

// Correção de dados cadastrais do paciente pela clínica
clinicaRouter.patch('/pacientes/:id', async (req, res) => {
  const { nome, telefone, email } = req.body || {};
  const { rowCount } = await db.query(
    `UPDATE pacientes
        SET nome = COALESCE($1, nome),
            telefone = COALESCE($2, telefone),
            email = COALESCE($3, email)
      WHERE id = $4 AND clinica_id = $5`,
    [nome, telefone, email, req.params.id, req.usuario.clinica]
  );
  if (!rowCount) return res.status(404).json({ erro: 'Paciente não encontrado' });
  res.status(204).end();
});

// Administração da plataforma (equipe AgendaFácil, papel "admin")
adminRouter.get('/clinicas', async (req, res) => {
  const { rows } = await db.query(
    'SELECT id, nome, slug, criado_em FROM clinicas ORDER BY criado_em DESC'
  );
  res.json(rows);
});

adminRouter.get('/metricas', async (req, res) => {
  const { rows } = await db.query(
    `SELECT c.slug, COUNT(a.id) AS agendamentos_30d
       FROM clinicas c
       LEFT JOIN pacientes p ON p.clinica_id = c.id
       LEFT JOIN agendamentos a
              ON a.paciente_id = p.id AND a.criado_em > now() - interval '30 days'
      GROUP BY c.slug`
  );
  res.json(rows);
});

module.exports = { clinicaRouter, adminRouter };
