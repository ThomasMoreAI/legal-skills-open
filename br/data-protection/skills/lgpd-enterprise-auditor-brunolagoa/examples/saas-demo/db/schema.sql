-- AgendaFácil — esquema do banco (projeto fictício de demonstração)
CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE clinicas (
  id         SERIAL PRIMARY KEY,
  nome       TEXT NOT NULL,
  slug       TEXT NOT NULL UNIQUE,
  criado_em  TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE usuarios (
  id          SERIAL PRIMARY KEY,
  clinica_id  INTEGER REFERENCES clinicas(id),
  email       TEXT NOT NULL UNIQUE,
  senha_hash  TEXT NOT NULL,
  papel       TEXT NOT NULL CHECK (papel IN ('admin', 'clinica')),
  criado_em   TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE pacientes (
  id               SERIAL PRIMARY KEY,
  clinica_id       INTEGER NOT NULL REFERENCES clinicas(id),
  nome             TEXT NOT NULL,
  cpf              TEXT NOT NULL,
  telefone         TEXT NOT NULL,
  email            TEXT,
  data_nascimento  DATE NOT NULL,
  criado_em        TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE (clinica_id, cpf)
);

CREATE TABLE agendamentos (
  id           SERIAL PRIMARY KEY,
  codigo       UUID NOT NULL DEFAULT gen_random_uuid() UNIQUE,
  paciente_id  INTEGER NOT NULL REFERENCES pacientes(id),
  data_hora    TIMESTAMPTZ NOT NULL,
  observacoes  TEXT, -- motivo da consulta, informado pelo paciente
  criado_em    TIMESTAMPTZ NOT NULL DEFAULT now()
);
