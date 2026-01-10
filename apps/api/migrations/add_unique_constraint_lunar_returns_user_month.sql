-- Migration: Ajout contrainte UNIQUE (user_id, month) sur lunar_returns
-- Protection contre génération concurrente au niveau DB
-- Date: 2025-01-XX

-- Supprimer l'ancienne contrainte si elle existe (au cas où)
ALTER TABLE public.lunar_returns
DROP CONSTRAINT IF EXISTS uq_lunar_returns_user_month;

-- Créer la contrainte UNIQUE sur (user_id, month)
-- Cette contrainte garantit qu'un utilisateur ne peut avoir qu'un seul retour lunaire par mois
-- Protection contre les insertions concurrentes (INSERT ... ON CONFLICT DO NOTHING)
CREATE UNIQUE INDEX IF NOT EXISTS uq_lunar_returns_user_month
ON public.lunar_returns (user_id, month);

-- Vérification: la contrainte doit empêcher les doublons
-- Test (devrait échouer si doublon existe):
-- INSERT INTO public.lunar_returns (user_id, month, return_date, raw_data)
-- VALUES (1, '2024-01', NOW(), '{}');
-- INSERT INTO public.lunar_returns (user_id, month, return_date, raw_data)
-- VALUES (1, '2024-01', NOW(), '{}');  -- Devrait échouer avec "duplicate key value violates unique constraint"

