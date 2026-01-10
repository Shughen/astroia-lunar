-- Rollback: Supprimer table natal_interpretations
-- Date: 2025-12-29
-- Description: Supprime la table et tous les objets associés (trigger, function, policies)

-- 1) Supprimer les policies RLS
DROP POLICY IF EXISTS "Users can delete their own interpretations" ON public.natal_interpretations;
DROP POLICY IF EXISTS "Users can update their own interpretations" ON public.natal_interpretations;
DROP POLICY IF EXISTS "Users can insert their own interpretations" ON public.natal_interpretations;
DROP POLICY IF EXISTS "Users can view their own interpretations" ON public.natal_interpretations;

-- 2) Supprimer le trigger
DROP TRIGGER IF EXISTS trigger_natal_interpretations_updated_at ON public.natal_interpretations;

-- 3) Supprimer la function
DROP FUNCTION IF EXISTS update_natal_interpretations_updated_at();

-- 4) Supprimer les index (seront supprimés auto avec la table, mais explicité pour clarté)
DROP INDEX IF EXISTS public.idx_natal_interpretations_created_at;
DROP INDEX IF EXISTS public.idx_natal_interpretations_user_chart;
DROP INDEX IF EXISTS public.idx_natal_interpretations_unique;

-- 5) Supprimer la table
DROP TABLE IF EXISTS public.natal_interpretations;
