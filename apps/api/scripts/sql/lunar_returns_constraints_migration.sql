-- ============================================
-- MIGRATION SAFE: Contraintes et validations pour return_date
-- ============================================
-- 
-- OBJECTIF: Rendre return_date une colonne métier robuste
-- - Contrainte UNIQUE partielle (1 retour/jour max par user)
-- - Migration safe (backfill + validation)
--
-- ⚠️ EXÉCUTER EN ORDRE dans Supabase SQL Editor
-- ============================================

-- ============================================
-- ÉTAPE 1: Vérification pré-migration
-- ============================================
-- Vérifier l'état actuel avant d'appliquer les contraintes

-- Vérifier que return_date n'a pas de NULL
SELECT 
    COUNT(*) AS total_rows,
    COUNT(return_date) AS non_null_rows,
    COUNT(*) FILTER (WHERE return_date IS NULL) AS null_rows
FROM public.lunar_returns;

-- Vérifier s'il y a des doublons (même jour pour un user)
SELECT 
    user_id,
    DATE(return_date) AS return_day,
    COUNT(*) AS count,
    ARRAY_AGG(id) AS ids,
    ARRAY_AGG(return_date) AS dates
FROM public.lunar_returns
GROUP BY user_id, DATE(return_date)
HAVING COUNT(*) > 1;

-- Si cette requête retourne des lignes, il faut résoudre les doublons avant d'ajouter la contrainte UNIQUE


-- ============================================
-- ÉTAPE 2: Backfill return_date depuis raw_data (si nécessaire)
-- ============================================
-- ⚠️ Déjà fait selon le contexte, mais gardé pour référence

-- Mettre à jour les return_date NULL depuis raw_data.return_datetime
UPDATE public.lunar_returns
SET return_date = (
    (raw_data->>'return_datetime')::timestamp AT TIME ZONE 'UTC'
)::timestamptz
WHERE return_date IS NULL
    AND raw_data ? 'return_datetime'
    AND NULLIF(raw_data->>'return_datetime', '') IS NOT NULL;

-- Vérifier qu'il ne reste plus de NULL
SELECT COUNT(*) AS remaining_nulls
FROM public.lunar_returns
WHERE return_date IS NULL;
-- Devrait être 0


-- ============================================
-- ÉTAPE 3: Résoudre les doublons (si nécessaire)
-- ============================================
-- Si des users ont plusieurs retours le même jour, on garde le plus récent

-- Identifier les doublons
WITH duplicates AS (
    SELECT 
        id,
        user_id,
        return_date,
        DATE(return_date) AS return_day,
        ROW_NUMBER() OVER (
            PARTITION BY user_id, DATE(return_date) 
            ORDER BY calculated_at DESC, id DESC
        ) AS rn
    FROM public.lunar_returns
)
SELECT id, user_id, return_date
FROM duplicates
WHERE rn > 1;
-- Si cette requête retourne des lignes, ce sont les IDs à supprimer

-- Supprimer les doublons (garder le plus récent)
-- ⚠️ EXÉCUTER UNIQUEMENT SI DES DOUBLONS EXISTENT
-- DELETE FROM public.lunar_returns
-- WHERE id IN (
--     SELECT id
--     FROM (
--         SELECT 
--             id,
--             ROW_NUMBER() OVER (
--                 PARTITION BY user_id, DATE(return_date) 
--                 ORDER BY calculated_at DESC, id DESC
--             ) AS rn
--         FROM public.lunar_returns
--     ) ranked
--     WHERE rn > 1
-- );


-- ============================================
-- ÉTAPE 4: Ajouter la contrainte NOT NULL (si pas déjà fait)
-- ============================================
-- ⚠️ Déjà fait selon le contexte, mais gardé pour référence

-- ALTER TABLE public.lunar_returns
-- ALTER COLUMN return_date SET NOT NULL;


-- ============================================
-- ÉTAPE 5: Contrainte UNIQUE partielle (1 retour/jour max par user)
-- ============================================
-- Empêche d'avoir deux retours lunaires le même jour pour un même user

-- Supprimer l'ancienne contrainte si elle existe
ALTER TABLE public.lunar_returns
DROP CONSTRAINT IF EXISTS uq_lunar_returns_user_return_day;

-- Créer la contrainte UNIQUE partielle sur (user_id, DATE(return_date))
-- Note: PostgreSQL ne supporte pas directement UNIQUE sur expression avec DATE()
-- On utilise un index unique partiel à la place
CREATE UNIQUE INDEX IF NOT EXISTS uq_lunar_returns_user_return_day
ON public.lunar_returns (user_id, DATE(return_date));

-- Alternative: Si on veut être plus strict et empêcher même les retours dans la même heure
-- CREATE UNIQUE INDEX IF NOT EXISTS uq_lunar_returns_user_return_date
-- ON public.lunar_returns (user_id, return_date);

-- Vérifier que la contrainte fonctionne (devrait échouer si doublon existe)
-- INSERT INTO public.lunar_returns (user_id, month, return_date, raw_data)
-- VALUES (1, '2025-01-01', '2025-01-15T12:00:00+00:00'::timestamptz, '{}'::jsonb);
-- INSERT INTO public.lunar_returns (user_id, month, return_date, raw_data)
-- VALUES (1, '2025-01-02', '2025-01-15T13:00:00+00:00'::timestamptz, '{}'::jsonb);
-- La deuxième insert devrait échouer avec: duplicate key value violates unique constraint


-- ============================================
-- ÉTAPE 6: Vérifications post-migration
-- ============================================

-- Vérifier qu'il n'y a pas de NULL
SELECT 
    COUNT(*) FILTER (WHERE return_date IS NULL) AS null_count
FROM public.lunar_returns;
-- Devrait être 0

-- Vérifier qu'il n'y a pas de doublons
SELECT 
    user_id,
    DATE(return_date) AS return_day,
    COUNT(*) AS count
FROM public.lunar_returns
GROUP BY user_id, DATE(return_date)
HAVING COUNT(*) > 1;
-- Devrait retourner 0 lignes

-- Vérifier que l'index existe
SELECT 
    indexname,
    indexdef
FROM pg_indexes
WHERE tablename = 'lunar_returns'
    AND indexname = 'uq_lunar_returns_user_return_day';

-- Vérifier que le trigger fonctionne (test insert)
-- Le trigger devrait remplir return_date automatiquement depuis raw_data
-- SELECT id, return_date, raw_data->>'return_datetime' AS raw_datetime
-- FROM public.lunar_returns
-- ORDER BY calculated_at DESC
-- LIMIT 5;


-- ============================================
-- ÉTAPE 7: Rollback (si nécessaire)
-- ============================================
-- En cas de problème, supprimer la contrainte

-- DROP INDEX IF EXISTS uq_lunar_returns_user_return_day;

-- Remettre return_date nullable (si nécessaire)
-- ALTER TABLE public.lunar_returns
-- ALTER COLUMN return_date DROP NOT NULL;

