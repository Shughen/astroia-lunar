-- Rollback SQL pour Supabase
-- Suppression colonnes V2 de la table lunar_returns
-- Script idempotent (peut être exécuté plusieurs fois sans erreur)

-- ============================================
-- 1. Supprimer index GIN sur v2_payload (si existe)
-- ============================================
DO $$
BEGIN
    IF EXISTS (
        SELECT 1 
        FROM pg_indexes 
        WHERE tablename = 'lunar_returns' 
        AND indexname = 'idx_lunar_returns_v2_payload_gin'
    ) THEN
        DROP INDEX idx_lunar_returns_v2_payload_gin;
        RAISE NOTICE '✅ Index idx_lunar_returns_v2_payload_gin supprimé';
    ELSE
        RAISE NOTICE 'ℹ️ Index idx_lunar_returns_v2_payload_gin n''existe pas';
    END IF;
END $$;

-- ============================================
-- 2. Supprimer index B-tree sur v2_version (si existe)
-- ============================================
DO $$
BEGIN
    IF EXISTS (
        SELECT 1 
        FROM pg_indexes 
        WHERE tablename = 'lunar_returns' 
        AND indexname = 'idx_lunar_returns_v2_version'
    ) THEN
        DROP INDEX idx_lunar_returns_v2_version;
        RAISE NOTICE '✅ Index idx_lunar_returns_v2_version supprimé';
    ELSE
        RAISE NOTICE 'ℹ️ Index idx_lunar_returns_v2_version n''existe pas';
    END IF;
END $$;

-- ============================================
-- 3. Supprimer colonne v2_payload (si existe)
-- ============================================
DO $$
BEGIN
    IF EXISTS (
        SELECT 1 
        FROM information_schema.columns 
        WHERE table_name = 'lunar_returns' 
        AND column_name = 'v2_payload'
    ) THEN
        ALTER TABLE lunar_returns 
        DROP COLUMN v2_payload;
        RAISE NOTICE '✅ Colonne v2_payload supprimée';
    ELSE
        RAISE NOTICE 'ℹ️ Colonne v2_payload n''existe pas';
    END IF;
END $$;

-- ============================================
-- 4. Supprimer colonne v2_version (si existe)
-- ============================================
DO $$
BEGIN
    IF EXISTS (
        SELECT 1 
        FROM information_schema.columns 
        WHERE table_name = 'lunar_returns' 
        AND column_name = 'v2_version'
    ) THEN
        ALTER TABLE lunar_returns 
        DROP COLUMN v2_version;
        RAISE NOTICE '✅ Colonne v2_version supprimée';
    ELSE
        RAISE NOTICE 'ℹ️ Colonne v2_version n''existe pas';
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
        WHERE table_name = 'lunar_returns' AND column_name = 'v2_version'
    ) INTO v2_version_exists;
    
    SELECT EXISTS (
        SELECT 1 FROM information_schema.columns 
        WHERE table_name = 'lunar_returns' AND column_name = 'v2_payload'
    ) INTO v2_payload_exists;
    
    -- Vérifier index
    SELECT EXISTS (
        SELECT 1 FROM pg_indexes 
        WHERE tablename = 'lunar_returns' AND indexname = 'idx_lunar_returns_v2_version'
    ) INTO idx_version_exists;
    
    SELECT EXISTS (
        SELECT 1 FROM pg_indexes 
        WHERE tablename = 'lunar_returns' AND indexname = 'idx_lunar_returns_v2_payload_gin'
    ) INTO idx_payload_exists;
    
    -- Afficher résumé
    RAISE NOTICE '';
    RAISE NOTICE '========================================';
    RAISE NOTICE 'Résumé du rollback:';
    RAISE NOTICE '========================================';
    RAISE NOTICE 'Colonne v2_version: %', CASE WHEN v2_version_exists THEN '⚠️ Encore présente' ELSE '✅ Supprimée' END;
    RAISE NOTICE 'Colonne v2_payload: %', CASE WHEN v2_payload_exists THEN '⚠️ Encore présente' ELSE '✅ Supprimée' END;
    RAISE NOTICE 'Index v2_version: %', CASE WHEN idx_version_exists THEN '⚠️ Encore présent' ELSE '✅ Supprimé' END;
    RAISE NOTICE 'Index v2_payload (GIN): %', CASE WHEN idx_payload_exists THEN '⚠️ Encore présent' ELSE '✅ Supprimé' END;
    RAISE NOTICE '========================================';
    
    IF NOT v2_version_exists AND NOT v2_payload_exists AND NOT idx_version_exists AND NOT idx_payload_exists THEN
        RAISE NOTICE '✅ Rollback complet et réussi!';
    ELSE
        RAISE WARNING '⚠️ Certains éléments sont encore présents. Vérifiez les messages ci-dessus.';
    END IF;
END $$;

