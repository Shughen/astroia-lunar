-- Migration: Ajouter default gen_random_uuid() pour natal_charts.id
-- Date: 2026-01-02
-- Problème: La colonne natal_charts.id (uuid) n'a pas de default, ce qui cause des erreurs
--           "null value in column "id" violates not-null constraint"
-- Solution: Ajouter server_default gen_random_uuid() pour que la DB génère automatiquement l'UUID

-- Vérifier que l'extension pgcrypto est activée (pour gen_random_uuid)
CREATE EXTENSION IF NOT EXISTS pgcrypto;

-- Ajouter le default à natal_charts.id
ALTER TABLE natal_charts
ALTER COLUMN id SET DEFAULT gen_random_uuid();

-- Vérifier le résultat
-- \d natal_charts
-- La colonne id devrait maintenant avoir: Default | gen_random_uuid()
