-- Migration SIMPLE: Convertir lunar_returns.user_id de UUID vers INTEGER
-- À exécuter dans Supabase SQL Editor
-- 
-- ⚠️ IMPORTANT: Cette migration est IDEMPOTENTE (peut être exécutée plusieurs fois sans erreur)
-- 
-- Cette migration:
-- 1. Supprime les données existantes (seront régénérées)
-- 2. Supprime les policies RLS qui dépendent de user_id
-- 3. Supprime l'ancienne FK
-- 4. Supprime l'ancienne colonne user_id (UUID) si elle existe
-- 5. Crée la nouvelle colonne user_id (INTEGER NOT NULL) si elle n'existe pas
-- 6. Ajoute la FK vers users.id (ignore si déjà présente)
-- 7. Recrée les policies RLS avec user_id INTEGER
--
-- ⚠️ RÈGLE CRITIQUE: Aligner types DB <-> modèles SQLAlchemy
-- - user_id doit être INTEGER partout (pas UUID)
-- - Vérifier après migration avec: scripts/sql/inspect_core_schema.sql

-- ÉTAPE 1: Supprimer les données existantes
DELETE FROM lunar_returns;
-- (Les données seront régénérées lors du prochain appel à /api/lunar-returns/generate)

-- ÉTAPE 2: Supprimer les policies RLS qui dépendent de user_id
DROP POLICY IF EXISTS allow_select_own_rows ON lunar_returns;
DROP POLICY IF EXISTS allow_insert_own_rows ON lunar_returns;
DROP POLICY IF EXISTS allow_update_own_rows ON lunar_returns;
DROP POLICY IF EXISTS allow_delete_own_rows ON lunar_returns;

-- ÉTAPE 3: Supprimer l'ancienne FK si elle existe
DO $$
DECLARE
    fk_name TEXT;
BEGIN
    SELECT constraint_name INTO fk_name
    FROM information_schema.table_constraints
    WHERE table_schema = 'public'
      AND table_name = 'lunar_returns'
      AND constraint_name LIKE '%user_id%'
      AND constraint_type = 'FOREIGN KEY'
    LIMIT 1;
    
    IF fk_name IS NOT NULL THEN
        EXECUTE format('ALTER TABLE lunar_returns DROP CONSTRAINT IF EXISTS %I', fk_name);
        RAISE NOTICE '✅ Ancienne FK supprimée: %', fk_name;
    END IF;
END $$;

-- ÉTAPE 4: Supprimer l'ancienne colonne user_id (UUID) avec CASCADE pour supprimer les dépendances
-- Idempotent: DROP COLUMN IF EXISTS
ALTER TABLE lunar_returns DROP COLUMN IF EXISTS user_id CASCADE;

-- ÉTAPE 5: Créer la nouvelle colonne user_id (INTEGER NOT NULL)
-- Idempotent: vérifier si la colonne existe déjà avant de créer
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.columns
        WHERE table_schema = 'public'
          AND table_name = 'lunar_returns'
          AND column_name = 'user_id'
          AND data_type = 'integer'
    ) THEN
        ALTER TABLE lunar_returns ADD COLUMN user_id INTEGER NOT NULL;
        RAISE NOTICE '✅ Colonne user_id INTEGER créée';
    ELSE
        RAISE NOTICE '✅ Colonne user_id INTEGER existe déjà - skip';
    END IF;
END $$;

-- ÉTAPE 6: Ajouter la FK vers users.id (idempotent: IF NOT EXISTS)
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.table_constraints
        WHERE table_schema = 'public'
          AND table_name = 'lunar_returns'
          AND constraint_name = 'fk_lunar_returns_user_id'
          AND constraint_type = 'FOREIGN KEY'
    ) THEN
        ALTER TABLE lunar_returns
        ADD CONSTRAINT fk_lunar_returns_user_id
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE;
        RAISE NOTICE '✅ FK fk_lunar_returns_user_id créée';
    ELSE
        RAISE NOTICE '✅ FK fk_lunar_returns_user_id existe déjà - skip';
    END IF;
END $$;

-- ÉTAPE 7: Recréer les policies RLS avec user_id INTEGER
-- Note: Ces policies supposent que auth.uid() retourne un INTEGER (comme users.id)
-- Si auth.uid() retourne un UUID, il faudra adapter les policies

-- Policy SELECT: les utilisateurs peuvent voir leurs propres révolutions lunaires
CREATE POLICY allow_select_own_rows ON lunar_returns
    FOR SELECT
    USING (user_id = (SELECT id FROM users WHERE email = auth.jwt() ->> 'email'));

-- Policy INSERT: les utilisateurs peuvent créer leurs propres révolutions lunaires
CREATE POLICY allow_insert_own_rows ON lunar_returns
    FOR INSERT
    WITH CHECK (user_id = (SELECT id FROM users WHERE email = auth.jwt() ->> 'email'));

-- Policy UPDATE: les utilisateurs peuvent modifier leurs propres révolutions lunaires
CREATE POLICY allow_update_own_rows ON lunar_returns
    FOR UPDATE
    USING (user_id = (SELECT id FROM users WHERE email = auth.jwt() ->> 'email'))
    WITH CHECK (user_id = (SELECT id FROM users WHERE email = auth.jwt() ->> 'email'));

-- Policy DELETE: les utilisateurs peuvent supprimer leurs propres révolutions lunaires
CREATE POLICY allow_delete_own_rows ON lunar_returns
    FOR DELETE
    USING (user_id = (SELECT id FROM users WHERE email = auth.jwt() ->> 'email'));

-- Vérification finale
DO $$
DECLARE
    final_type TEXT;
    nullable_flag TEXT;
BEGIN
    SELECT c.data_type, c.is_nullable INTO final_type, nullable_flag
    FROM information_schema.columns c
    WHERE c.table_schema = 'public'
      AND c.table_name = 'lunar_returns'
      AND c.column_name = 'user_id';
    
    IF final_type = 'integer' AND nullable_flag = 'NO' THEN
        RAISE NOTICE '✅ Migration réussie: user_id est INTEGER NOT NULL';
    ELSE
        RAISE WARNING '⚠️ Migration incomplète: type=%, nullable=%', final_type, nullable_flag;
    END IF;
END $$;

