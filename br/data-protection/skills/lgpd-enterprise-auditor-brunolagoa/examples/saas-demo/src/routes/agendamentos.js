const express = require('express');
const db = require('../db');

const router = express.Router();

function idadeEmAnos(dataNascimento) {
  const nascimento = new Date(dataNascimento);
  const hoje = new Date();
  let idade = hoje.getFullYear() - nascimento.getFullYear();
  const mes = hoje.getMonth() - nascimento.getMonth();
  if (mes < 0 || (mes === 0 && hoje.getDate() < nascimento.getDate())) idade -= 1;
  return idade;
}

// Agendamento público, feito pelo próprio paciente na página da clínica
router.post('/', async (req, res) => {
  const { clinica, nome, cpf, telefone, email, dataNascimento, dataHora, observacoes } =
    req.body || {};

  if (!clinica || !nome || !cpf || !telefone || !dataNascimento || !dataHora) {
    return res.status(400).json({ erro: 'Preencha os campos obrigatórios.' });
  }
  if (idadeEmAnos(dataNascimento) < 18) {
    return res.status(422).json({
      erro: 'Agendamentos para menores de 18 anos devem ser feitos diretamente com a clínica.',
    });
  }

  console.log(`[agendamento] novo paciente nome=${nome} cpf=${cpf} email=${email} clinica=${clinica}`);

  const paciente = await db.query(
    `INSERT INTO pacientes (clinica_id, nome, cpf, telefone, email, data_nascimento)
     VALUES ((SELECT id FROM clinicas WHERE slug = $1), $2, $3, $4, $5, $6)
     ON CONFLICT (clinica_id, cpf)
       DO UPDATE SET telefone = EXCLUDED.telefone, email = EXCLUDED.email
     RETURNING id`,
    [clinica, nome, cpf, telefone, email, dataNascimento]
  );

  const agendamento = await db.query(
    `INSERT INTO agendamentos (paciente_id, data_hora, observacoes)
     VALUES ($1, $2, $3)
     RETURNING codigo`,
    [paciente.rows[0].id, dataHora, observacoes || null]
  );

  return res.status(201).json({ codigo: agendamento.rows[0].codigo });
});

// Confirmação exibida ao paciente logo após o agendamento
router.get('/:codigo', async (req, res) => {
  const { rows } = await db.query(
    `SELECT a.*, p.*
       FROM agendamentos a
       JOIN pacientes p ON p.id = a.paciente_id
      WHERE a.codigo = $1`,
    [req.params.codigo]
  );
  if (!rows[0]) return res.status(404).json({ erro: 'Agendamento não encontrado' });
  return res.json(rows[0]);
});

module.exports = router;
