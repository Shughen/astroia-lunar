-- Migration: Convertir lunar_returns.user_id de UUID vers INTEGER FK -> users.id
-- Contexte: users.id est INTEGER, mais lunar_returns.user_id était UUID
-- Objectif: Aligner lunar_returns.user_id sur users.id (INTEGER)
--
-- Étapes:
-- 1. Vérifier le type actuel de user_id
-- 2. Si UUID, créer user_id_int INTEGER nullable
-- 3. Backfill user_id_int depuis users.id (via correspondance UUID si nécessaire, ou supprimer les données invalides)
-- 4. Ajouter FK + contrainte NOT NULL
-- 5. Supprimer l'ancienne colonne user_id (UUID)
-- 6. Renommer user_id_int -> user_id

-- ============================================
-- ÉTAPE 1: Vérifier le type actuel
-- ============================================
DO $$
DECLARE
    current_type TEXT;
BEGIN
    SELECT data_type INTO current_type
    FROM information_schema.columns
    WHERE table_schema = 'public'
      AND table_name = 'lunar_returns'
      AND column_name = 'user_id';
    
    IF current_type IS NULL THEN
        RAISE NOTICE '⚠️ Colonne user_id n''existe pas dans lunar_returns';
        RETURN;
    END IF;
    
    RAISE NOTICE '📊 Type actuel de lunar_returns.user_id: %', current_type;
    
    -- Si déjà INTEGER, pas besoin de migration
    IF current_type = 'integer' THEN
        RAISE NOTICE '✅ lunar_returns.user_id est déjà INTEGER - pas de migration nécessaire';
        RETURN;
    END IF;
    
    -- Si UUID, on continue la migration
    IF current_type = 'uuid' THEN
        RAISE NOTICE '🔄 Migration nécessaire: UUID -> INTEGER';
    ELSE
        RAISE WARNING '⚠️ Type inattendu: % - migration peut échouer', current_type;
    END IF;
END $$;

-- ============================================
-- ÉTAPE 2: Créer user_id_int INTEGER nullable
-- ============================================
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.columns
        WHERE table_schema = 'public'
          AND table_name = 'lunar_returns'
          AND column_name = 'user_id_int'
    ) THEN
        ALTER TABLE lunar_returns
        ADD COLUMN user_id_int INTEGER;
        
        RAISE NOTICE '✅ Colonne user_id_int ajoutée';
    ELSE
        RAISE NOTICE 'ℹ️ Colonne user_id_int existe déjà';
    END IF;
END $$;

-- ============================================
-- ÉTAPE 3: Backfill user_id_int
-- ============================================
-- Option A: Si on peut mapper UUID -> INTEGER via une table de correspondance
-- Option B: Supprimer les données invalides (plus simple pour DEV)
-- On choisit Option B pour DEV (on supprime les lunar_returns existants)

DO $$
DECLARE
    deleted_count INTEGER;
BEGIN
    -- Supprimer toutes les entrées existantes (elles seront régénérées)
    DELETE FROM lunar_returns;
    GET DIAGNOSTICS deleted_count = ROW_COUNT;
    
    RAISE NOTICE '🗑️  % entrée(s) supprimée(s) de lunar_returns (seront régénérées)', deleted_count;
END $$;

-- ============================================
-- ÉTAPE 4: Ajouter FK + contrainte NOT NULL
-- ============================================
DO $$
BEGIN
    -- Supprimer l'ancienne FK si elle existe
    IF EXISTS (
        SELECT 1 FROM information_schema.table_constraints
        WHERE table_schema = 'public'
          AND table_name = 'lunar_returns'
          AND constraint_name LIKE '%user_id%'
          AND constraint_type = 'FOREIGN KEY'
    ) THEN
        -- Trouver le nom exact de la contrainte
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
        END;
    END IF;
    
    -- Ajouter la nouvelle FK sur user_id_int
    ALTER TABLE lunar_returns
    ADD CONSTRAINT fk_lunar_returns_user_id_int
    FOREIGN KEY (user_id_int) REFERENCES users(id) ON DELETE CASCADE;
    
    RAISE NOTICE '✅ FK ajoutée sur user_id_int';
    
    -- Rendre NOT NULL
    ALTER TABLE lunar_returns
    ALTER COLUMN user_id_int SET NOT NULL;
    
    RAISE NOTICE '✅ user_id_int rendu NOT NULL';
END $$;

-- ============================================
-- ÉTAPE 5: Supprimer l'ancienne colonne user_id (UUID)
-- ============================================
DO $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM information_schema.columns
        WHERE table_schema = 'public'
          AND table_name = 'lunar_returns'
          AND column_name = 'user_id'
          AND data_type = 'uuid'
    ) THEN
        ALTER TABLE lunar_returns
        DROP COLUMN user_id;
        
        RAISE NOTICE '✅ Ancienne colonne user_id (UUID) supprimée';
    ELSE
        RAISE NOTICE 'ℹ️ Colonne user_id (UUID) n''existe pas ou n''est pas UUID';
    END IF;
END $$;

-- ============================================
-- ÉTAPE 6: Renommer user_id_int -> user_id
-- ============================================
DO $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM information_schema.columns
        WHERE table_schema = 'public'
          AND table_name = 'lunar_returns'
          AND column_name = 'user_id_int'
    ) THEN
        ALTER TABLE lunar_returns
        RENAME COLUMN user_id_int TO user_id;
        
        RAISE NOTICE '✅ Colonne user_id_int renommée en user_id';
    ELSE
        RAISE NOTICE 'ℹ️ Colonne user_id_int n''existe pas';
    END IF;
END $$;

-- ============================================
-- Vérification finale
-- ============================================
DO $$
DECLARE
    final_type TEXT;
    is_nullable TEXT;
BEGIN
    SELECT data_type, is_nullable INTO final_type, is_nullable
    FROM information_schema.columns
    WHERE table_schema = 'public'
      AND table_name = 'lunar_returns'
      AND column_name = 'user_id';
    
    IF final_type IS NULL THEN
        RAISE WARNING '❌ Colonne user_id n''existe pas après migration';
    ELSIF final_type = 'integer' AND is_nullable = 'NO' THEN
        RAISE NOTICE '✅ Migration réussie: user_id est INTEGER NOT NULL';
    ELSE
        RAISE WARNING '⚠️ Migration incomplète: user_id type=%, nullable=%', final_type, is_nullable;
    END IF;
END $$;

