-- Migration SQL pour Supabase
-- Ajout colonnes V2 à la table lunar_returns
-- Script idempotent (peut être exécuté plusieurs fois sans erreur)

-- ============================================
-- 1. Ajouter colonne v2_version (si n'existe pas)
-- ============================================
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 
        FROM information_schema.columns 
        WHERE table_schema = 'public'
        AND table_name = 'lunar_returns' 
        AND column_name = 'v2_version'
    ) THEN
        ALTER TABLE lunar_returns 
        ADD COLUMN v2_version VARCHAR(10) NULL;
        
        RAISE NOTICE '✅ Colonne v2_version ajoutée';
    ELSE
        RAISE NOTICE 'ℹ️ Colonne v2_version existe déjà';
    END IF;
END $$;

-- ============================================
-- 2. Ajouter colonne v2_payload (si n'existe pas)
-- ============================================
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 
        FROM information_schema.columns 
        WHERE table_schema = 'public'
        AND table_name = 'lunar_returns' 
        AND column_name = 'v2_payload'
    ) THEN
        ALTER TABLE lunar_returns 
        ADD COLUMN v2_payload JSONB NULL;
        
        RAISE NOTICE '✅ Colonne v2_payload ajoutée';
    ELSE
        RAISE NOTICE 'ℹ️ Colonne v2_payload existe déjà';
    END IF;
END $$;

-- ============================================
-- 3. Créer index B-tree sur v2_version (filtré, si n'existe pas)
-- ============================================
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 
        FROM pg_indexes 
        WHERE schemaname = 'public'
        AND tablename = 'lunar_returns' 
        AND indexname = 'idx_lunar_returns_v2_version'
    ) THEN
        CREATE INDEX idx_lunar_returns_v2_version 
        ON lunar_returns (v2_version) 
        WHERE v2_version IS NOT NULL;
        
        RAISE NOTICE '✅ Index idx_lunar_returns_v2_version créé';
    ELSE
        RAISE NOTICE 'ℹ️ Index idx_lunar_returns_v2_version existe déjà';
    END IF;
END $$;

-- ============================================
-- 4. Créer index GIN sur v2_payload (si n'existe pas)
-- ============================================
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 
        FROM pg_indexes 
        WHERE schemaname = 'public'
        AND tablename = 'lunar_returns' 
        AND indexname = 'idx_lunar_returns_v2_payload_gin'
    ) THEN
        CREATE INDEX idx_lunar_returns_v2_payload_gin 
        ON lunar_returns 
        USING GIN (v2_payload);
        
        RAISE NOTICE '✅ Index GIN idx_lunar_returns_v2_payload_gin créé';
    ELSE
        RAISE NOTICE 'ℹ️ Index idx_lunar_returns_v2_payload_gin existe déjà';
    END IF;
END $$;

-- ============================================
-- 5. Vérification finale
-- ============================================
DO $$
DECLARE
    v2_version_exists BOOLEAN;
    v2_payload_exists BOOLEAN;
    idx_version_exists BOOLEAN;
    idx_payload_exists BOOLEAN;
BEGIN
    -- Vérifier colonnes
    SELECT EXISTS (
        SELECT 1 FROM information_schema.columns 
        WHERE table_schema = 'public'
        AND table_name = 'lunar_returns' 
        AND column_name = 'v2_version'
    ) INTO v2_version_exists;
    
    SELECT EXISTS (
        SELECT 1 FROM information_schema.columns 
        WHERE table_schema = 'public'
        AND table_name = 'lunar_returns' 
        AND column_name = 'v2_payload'
    ) INTO v2_payload_exists;
    
    -- Vérifier index
    SELECT EXISTS (
        SELECT 1 FROM pg_indexes 
        WHERE schemaname = 'public'
        AND tablename = 'lunar_returns' 
        AND indexname = 'idx_lunar_returns_v2_version'
    ) INTO idx_version_exists;
    
    SELECT EXISTS (
        SELECT 1 FROM pg_indexes 
        WHERE schemaname = 'public'
        AND tablename = 'lunar_returns' 
        AND indexname = 'idx_lunar_returns_v2_payload_gin'
    ) INTO idx_payload_exists;
    
    -- Afficher résumé
    RAISE NOTICE '';
    RAISE NOTICE '========================================';
    RAISE NOTICE 'Résumé de la migration:';
    RAISE NOTICE '========================================';
    RAISE NOTICE 'Colonne v2_version: %', CASE WHEN v2_version_exists THEN '✅ Existe' ELSE '❌ Manquante' END;
    RAISE NOTICE 'Colonne v2_payload: %', CASE WHEN v2_payload_exists THEN '✅ Existe' ELSE '❌ Manquante' END;
    RAISE NOTICE 'Index v2_version: %', CASE WHEN idx_version_exists THEN '✅ Existe' ELSE '❌ Manquant' END;
    RAISE NOTICE 'Index v2_payload (GIN): %', CASE WHEN idx_payload_exists THEN '✅ Existe' ELSE '❌ Manquant' END;
    RAISE NOTICE '========================================';
    
    IF v2_version_exists AND v2_payload_exists AND idx_version_exists AND idx_payload_exists THEN
        RAISE NOTICE '✅ Migration complète et réussie!';
    ELSE
        RAISE WARNING '⚠️ Certains éléments manquent. Vérifiez les messages ci-dessus.';
    END IF;
END $$;

