-- Migration: Convertir natal_charts.user_id de UUID vers INTEGER FK -> users.id
-- Date: 2025-01-XX
-- Contexte: users.id est INTEGER, mais natal_charts.user_id était UUID
-- Objectif: Aligner natal_charts.user_id sur users.id (INTEGER)
--
-- IMPORTANT: Cette migration suppose que natal_charts.id est UUID (PK)
-- et que users.id est INTEGER
--
-- Étapes:
-- 1. Ajouter user_id_int INTEGER nullable
-- 2. Backfill (ou supprimer données existantes en DEV)
-- 3. Ajouter FK + UNIQUE constraints
-- 4. Supprimer user_id UUID
-- 5. Renommer user_id_int -> user_id
-- 6. Rendre user_id NOT NULL (après backfill)

-- ============================================================================
-- ÉTAPE 1: Vérifier l'état actuel
-- ============================================================================

-- Vérifier le type actuel de user_id
SELECT 
    column_name,
    data_type,
    is_nullable
FROM information_schema.columns
WHERE table_schema = 'public' 
  AND table_name = 'natal_charts'
  AND column_name = 'user_id';

-- ============================================================================
-- ÉTAPE 2: Ajouter la nouvelle colonne user_id_int (temporaire)
-- ============================================================================

-- Ajouter user_id_int INTEGER nullable
ALTER TABLE public.natal_charts
ADD COLUMN IF NOT EXISTS user_id_int INTEGER;

-- ============================================================================
-- ÉTAPE 3: Backfill (si possible) ou nettoyer les données existantes
-- ============================================================================

-- Option A: Si environnement DEV, supprimer les lignes existantes
-- (décommenter si vous voulez supprimer les données existantes)
-- DELETE FROM public.natal_charts;

-- Option B: Si vous avez un mapping uuid -> int (ex: table de correspondance)
-- UPDATE public.natal_charts nc
-- SET user_id_int = (SELECT id FROM users WHERE uuid_column = nc.user_id)
-- WHERE EXISTS (SELECT 1 FROM users WHERE uuid_column = nc.user_id);

-- Option C: Laisser NULL (les nouvelles lignes seront créées avec user_id_int)

-- ============================================================================
-- ÉTAPE 4: Ajouter les contraintes
-- ============================================================================

-- Contrainte UNIQUE (1 natal chart par user)
CREATE UNIQUE INDEX IF NOT EXISTS idx_natal_charts_user_id_int_unique 
ON public.natal_charts(user_id_int) 
WHERE user_id_int IS NOT NULL;

-- Contrainte FK vers users.id
ALTER TABLE public.natal_charts
ADD CONSTRAINT fk_natal_charts_user_id_int 
FOREIGN KEY (user_id_int) 
REFERENCES public.users(id) 
ON DELETE CASCADE;

-- ============================================================================
-- ÉTAPE 5: Rendre user_id_int NOT NULL (après backfill)
-- ============================================================================

-- ⚠️ ATTENTION: Ne décommenter que si user_id_int est rempli pour toutes les lignes
-- ALTER TABLE public.natal_charts
-- ALTER COLUMN user_id_int SET NOT NULL;

-- ============================================================================
-- ÉTAPE 6: Supprimer l'ancienne colonne user_id (UUID)
-- ============================================================================

-- Supprimer la contrainte FK ancienne si elle existe
ALTER TABLE public.natal_charts
DROP CONSTRAINT IF EXISTS fk_natal_charts_user_id;

-- Supprimer la contrainte UNIQUE ancienne si elle existe
DROP INDEX IF EXISTS idx_natal_charts_user_id_unique;

-- Supprimer l'ancienne colonne user_id (UUID)
ALTER TABLE public.natal_charts
DROP COLUMN IF EXISTS user_id;

-- ============================================================================
-- ÉTAPE 7: Renommer user_id_int -> user_id (pour simplifier le code)
-- ============================================================================

-- Renommer la colonne
ALTER TABLE public.natal_charts
RENAME COLUMN user_id_int TO user_id;

-- Renommer la contrainte FK
ALTER TABLE public.natal_charts
RENAME CONSTRAINT fk_natal_charts_user_id_int TO fk_natal_charts_user_id;

-- Renommer l'index UNIQUE
ALTER INDEX IF EXISTS idx_natal_charts_user_id_int_unique 
RENAME TO idx_natal_charts_user_id_unique;

-- ============================================================================
-- ÉTAPE 8: Rendre user_id NOT NULL (après backfill et rename)
-- ============================================================================

-- ⚠️ ATTENTION: Ne décommenter que si user_id est rempli pour toutes les lignes
-- ALTER TABLE public.natal_charts
-- ALTER COLUMN user_id SET NOT NULL;

-- ============================================================================
-- ÉTAPE 9: Vérification finale
-- ============================================================================

-- Vérifier le schéma final
SELECT 
    column_name,
    data_type,
    is_nullable,
    column_default
FROM information_schema.columns
WHERE table_schema = 'public' 
  AND table_name = 'natal_charts'
ORDER BY ordinal_position;

-- Vérifier les contraintes
SELECT 
    conname AS constraint_name,
    contype AS constraint_type
FROM pg_constraint
WHERE conrelid = 'public.natal_charts'::regclass
  AND conname LIKE '%user_id%';

