-- Migration: Convertir transits_overview.user_id et transits_events.user_id de UUID vers INTEGER FK -> users.id
-- Date: 2025-01-23
-- Contexte: users.id est INTEGER, mais transits tables utilisaient UUID (legacy Supabase auth.users)
-- Objectif: Aligner transits sur users.id (INTEGER) pour cohérence avec natal_charts et autres tables
--
-- Tables concernées:
-- - transits_overview
-- - transits_events
--
-- Étapes:
-- 1. Ajouter user_id_int INTEGER nullable sur les deux tables
-- 2. Backfill ou supprimer données existantes (DEV)
-- 3. Ajouter FK constraints vers users.id avec CASCADE DELETE
-- 4. Supprimer user_id UUID
-- 5. Renommer user_id_int -> user_id
-- 6. Rendre user_id NOT NULL

-- ============================================================================
-- ÉTAPE 1: Vérifier l'état actuel
-- ============================================================================

-- Vérifier le type actuel de user_id dans transits_overview
SELECT
    column_name,
    data_type,
    is_nullable
FROM information_schema.columns
WHERE table_schema = 'public'
  AND table_name = 'transits_overview'
  AND column_name = 'user_id';

-- Vérifier le type actuel de user_id dans transits_events
SELECT
    column_name,
    data_type,
    is_nullable
FROM information_schema.columns
WHERE table_schema = 'public'
  AND table_name = 'transits_events'
  AND column_name = 'user_id';

-- ============================================================================
-- ÉTAPE 2: Ajouter les nouvelles colonnes user_id_int (temporaires)
-- ============================================================================

-- Ajouter user_id_int INTEGER nullable sur transits_overview
ALTER TABLE public.transits_overview
ADD COLUMN IF NOT EXISTS user_id_int INTEGER;

-- Ajouter user_id_int INTEGER nullable sur transits_events
ALTER TABLE public.transits_events
ADD COLUMN IF NOT EXISTS user_id_int INTEGER;

-- ============================================================================
-- ÉTAPE 3: Backfill (si possible) ou nettoyer les données existantes
-- ============================================================================

-- Option A: Si environnement DEV, supprimer les lignes existantes
-- (décommenter si vous voulez supprimer les données existantes)
-- DELETE FROM public.transits_overview;
-- DELETE FROM public.transits_events;

-- Option B: Si vous avez un mapping uuid -> int via dev_external_id
-- UPDATE public.transits_overview to_
-- SET user_id_int = (SELECT id FROM users WHERE dev_external_id = to_.user_id::text)
-- WHERE EXISTS (SELECT 1 FROM users WHERE dev_external_id = to_.user_id::text);

-- UPDATE public.transits_events te
-- SET user_id_int = (SELECT id FROM users WHERE dev_external_id = te.user_id::text)
-- WHERE EXISTS (SELECT 1 FROM users WHERE dev_external_id = te.user_id::text);

-- Option C: Laisser NULL (les nouvelles lignes seront créées avec user_id_int)

-- ============================================================================
-- ÉTAPE 4: Ajouter les contraintes FK vers users.id
-- ============================================================================

-- Contrainte FK sur transits_overview -> users.id
ALTER TABLE public.transits_overview
ADD CONSTRAINT fk_transits_overview_user_id_int
FOREIGN KEY (user_id_int)
REFERENCES public.users(id)
ON DELETE CASCADE;

-- Contrainte FK sur transits_events -> users.id
ALTER TABLE public.transits_events
ADD CONSTRAINT fk_transits_events_user_id_int
FOREIGN KEY (user_id_int)
REFERENCES public.users(id)
ON DELETE CASCADE;

-- ============================================================================
-- ÉTAPE 5: Recréer les index composites avec user_id_int
-- ============================================================================

-- Créer index composite user_month pour transits_overview avec user_id_int
CREATE INDEX IF NOT EXISTS ix_transits_overview_user_id_int_month
ON public.transits_overview(user_id_int, month);

-- Créer index composite user_date pour transits_events avec user_id_int
CREATE INDEX IF NOT EXISTS ix_transits_events_user_id_int_date
ON public.transits_events(user_id_int, date);

-- ============================================================================
-- ÉTAPE 6: Supprimer les anciennes colonnes user_id (UUID)
-- ============================================================================

-- Supprimer les anciens index sur user_id UUID
DROP INDEX IF EXISTS ix_transits_overview_user_month;
DROP INDEX IF EXISTS ix_transits_overview_user_id;
DROP INDEX IF EXISTS ix_transits_events_user_date;
DROP INDEX IF EXISTS ix_transits_events_user_id;

-- Supprimer les anciennes colonnes user_id (UUID)
ALTER TABLE public.transits_overview
DROP COLUMN IF EXISTS user_id;

ALTER TABLE public.transits_events
DROP COLUMN IF EXISTS user_id;

-- ============================================================================
-- ÉTAPE 7: Renommer user_id_int -> user_id
-- ============================================================================

-- Renommer les colonnes
ALTER TABLE public.transits_overview
RENAME COLUMN user_id_int TO user_id;

ALTER TABLE public.transits_events
RENAME COLUMN user_id_int TO user_id;

-- Renommer les contraintes FK
ALTER TABLE public.transits_overview
RENAME CONSTRAINT fk_transits_overview_user_id_int TO fk_transits_overview_user_id;

ALTER TABLE public.transits_events
RENAME CONSTRAINT fk_transits_events_user_id_int TO fk_transits_events_user_id;

-- Renommer les index
ALTER INDEX IF EXISTS ix_transits_overview_user_id_int_month
RENAME TO ix_transits_overview_user_month;

ALTER INDEX IF EXISTS ix_transits_events_user_id_int_date
RENAME TO ix_transits_events_user_date;

-- Recréer l'index simple sur user_id (après rename)
CREATE INDEX IF NOT EXISTS ix_transits_overview_user_id
ON public.transits_overview(user_id);

CREATE INDEX IF NOT EXISTS ix_transits_events_user_id
ON public.transits_events(user_id);

-- ============================================================================
-- ÉTAPE 8: Rendre user_id NOT NULL (après backfill et rename)
-- ============================================================================

-- ⚠️ ATTENTION: Ne décommenter que si user_id est rempli pour toutes les lignes
-- ALTER TABLE public.transits_overview
-- ALTER COLUMN user_id SET NOT NULL;

-- ALTER TABLE public.transits_events
-- ALTER COLUMN user_id SET NOT NULL;

-- ============================================================================
-- ÉTAPE 9: Vérification finale
-- ============================================================================

-- Vérifier le schéma final de transits_overview
SELECT
    column_name,
    data_type,
    is_nullable,
    column_default
FROM information_schema.columns
WHERE table_schema = 'public'
  AND table_name = 'transits_overview'
ORDER BY ordinal_position;

-- Vérifier le schéma final de transits_events
SELECT
    column_name,
    data_type,
    is_nullable,
    column_default
FROM information_schema.columns
WHERE table_schema = 'public'
  AND table_name = 'transits_events'
ORDER BY ordinal_position;

-- Vérifier les contraintes FK
SELECT
    conname AS constraint_name,
    contype AS constraint_type,
    conrelid::regclass AS table_name
FROM pg_constraint
WHERE conrelid IN ('public.transits_overview'::regclass, 'public.transits_events'::regclass)
  AND conname LIKE '%user_id%';

-- Vérifier les index
SELECT
    tablename,
    indexname,
    indexdef
FROM pg_indexes
WHERE schemaname = 'public'
    AND tablename IN ('transits_overview', 'transits_events')
    AND indexdef LIKE '%user_id%'
ORDER BY tablename, indexname;
