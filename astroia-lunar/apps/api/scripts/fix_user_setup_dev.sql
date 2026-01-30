-- Script de correction : Setup utilisateur DEV_AUTH_BYPASS
-- Date: 2026-01-30
-- Contexte: Fix app crash 409 "Natal requis" + migration UUID→INTEGER

-- ============================================================
-- ÉTAPE 1: Créer/mettre à jour utilisateur de test (id=1)
-- ============================================================

INSERT INTO users (
    id,
    email,
    birth_date,
    birth_time,
    birth_latitude,
    birth_longitude,
    birth_place_name,
    birth_timezone,
    dev_external_id,
    is_active,
    created_at
)
VALUES (
    1,
    'test@astroia.app',
    '1989-04-15',
    '17:55:00',
    '48.9167',
    '2.5333',
    'Livry-Gargan, Seine-Saint-Denis, France',
    'Europe/Paris',
    '1',
    true,
    NOW()
)
ON CONFLICT (id) DO UPDATE SET
    email = EXCLUDED.email,
    birth_date = EXCLUDED.birth_date,
    birth_time = EXCLUDED.birth_time,
    birth_latitude = EXCLUDED.birth_latitude,
    birth_longitude = EXCLUDED.birth_longitude,
    birth_place_name = EXCLUDED.birth_place_name,
    birth_timezone = EXCLUDED.birth_timezone,
    updated_at = NOW();


-- ============================================================
-- ÉTAPE 2: Migration transits_overview.user_id UUID→INTEGER
-- ============================================================

DO $$
DECLARE
    current_type TEXT;
    fk_name TEXT;
    deleted_count INTEGER;
BEGIN
    -- Vérifier le type actuel de user_id
    SELECT data_type INTO current_type
    FROM information_schema.columns
    WHERE table_schema = 'public'
      AND table_name = 'transits_overview'
      AND column_name = 'user_id';

    RAISE NOTICE 'Type actuel de transits_overview.user_id: %', current_type;

    -- Si déjà INTEGER, pas besoin de migration
    IF current_type = 'integer' THEN
        RAISE NOTICE '✅ transits_overview.user_id est déjà INTEGER';
        RETURN;
    END IF;

    -- Si UUID, on convertit vers INTEGER
    IF current_type = 'uuid' THEN
        RAISE NOTICE '🔄 Migration UUID → INTEGER en cours...';

        -- Supprimer les données existantes (seront régénérées)
        DELETE FROM transits_overview;
        GET DIAGNOSTICS deleted_count = ROW_COUNT;
        RAISE NOTICE '🗑️  % entrée(s) supprimée(s)', deleted_count;

        -- Supprimer l'ancienne FK
        SELECT constraint_name INTO fk_name
        FROM information_schema.table_constraints
        WHERE table_schema = 'public'
          AND table_name = 'transits_overview'
          AND constraint_name LIKE '%user_id%'
          AND constraint_type = 'FOREIGN KEY'
        LIMIT 1;

        IF fk_name IS NOT NULL THEN
            EXECUTE format('ALTER TABLE transits_overview DROP CONSTRAINT IF EXISTS %I', fk_name);
            RAISE NOTICE '✅ FK supprimée: %', fk_name;
        END IF;

        -- Supprimer les index
        DROP INDEX IF EXISTS ix_transits_overview_user_month;

        -- Supprimer l'ancienne colonne user_id (UUID)
        ALTER TABLE transits_overview DROP COLUMN user_id CASCADE;
        RAISE NOTICE '✅ Ancienne colonne user_id (UUID) supprimée';

        -- Créer la nouvelle colonne user_id (INTEGER NOT NULL)
        ALTER TABLE transits_overview ADD COLUMN user_id INTEGER NOT NULL;

        -- Recréer l'index composite
        CREATE INDEX ix_transits_overview_user_month ON transits_overview(user_id, month);

        -- Ajouter la FK vers users.id
        ALTER TABLE transits_overview
        ADD CONSTRAINT fk_transits_overview_user_id
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE;

        RAISE NOTICE '✅ Migration réussie: user_id est maintenant INTEGER NOT NULL';
    ELSE
        RAISE WARNING '⚠️ Type inattendu: % - migration peut échouer', current_type;
    END IF;
END $$;


-- ============================================================
-- ÉTAPE 3: Nettoyer les anciennes données pour user_id=1
-- ============================================================

-- Supprimer l'ancien natal chart (sera régénéré via API)
DELETE FROM natal_charts WHERE user_id = 1;

-- Supprimer les lunar returns existants (seront régénérés)
DELETE FROM lunar_returns WHERE user_id = 1;

-- Supprimer les lunar reports existants
DELETE FROM lunar_reports WHERE user_id = 1;

-- Supprimer les transits overview existants
DELETE FROM transits_overview WHERE user_id = 1;


-- ============================================================
-- ÉTAPE 4: Vérification finale
-- ============================================================

SELECT
    u.id,
    u.email,
    u.birth_date,
    u.birth_time,
    u.birth_place_name,
    (SELECT COUNT(*) FROM natal_charts WHERE user_id = u.id) as natal_charts_count,
    (SELECT COUNT(*) FROM lunar_returns WHERE user_id = u.id) as lunar_returns_count,
    (SELECT COUNT(*) FROM lunar_reports WHERE user_id = u.id) as lunar_reports_count,
    (SELECT COUNT(*) FROM transits_overview WHERE user_id = u.id) as transits_count
FROM users u
WHERE u.id = 1;

-- Note: Après ce script, générer le natal chart via API:
-- curl -X POST -H "Content-Type: application/json" -H "X-Dev-User-Id: 1" \
--   "http://localhost:8000/api/natal-chart" \
--   -d '{"date":"1989-04-15","time":"17:55","latitude":48.9167,"longitude":2.5333,"place_name":"Livry-Gargan, France","timezone":"Europe/Paris"}'
