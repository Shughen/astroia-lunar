-- ============================================
-- Vérification UUID pour transits_overview
-- Script de diagnostic (non destructif)
-- ============================================

-- 1. Vérifier le type de la colonne user_id dans transits_overview
SELECT 
    column_name,
    data_type,
    udt_name,
    is_nullable
FROM information_schema.columns
WHERE table_schema = 'public' 
  AND table_name = 'transits_overview'
  AND column_name = 'user_id';

-- Résultat attendu:
-- column_name | data_type | udt_name | is_nullable
-- user_id     | uuid      | uuid     | NO

-- 2. Vérifier le type de la colonne user_id dans transits_events
SELECT 
    column_name,
    data_type,
    udt_name,
    is_nullable
FROM information_schema.columns
WHERE table_schema = 'public' 
  AND table_name = 'transits_events'
  AND column_name = 'user_id';

-- Résultat attendu:
-- column_name | data_type | udt_name | is_nullable
-- user_id     | uuid      | uuid     | NO

-- 3. Vérifier les RLS policies sur transits_overview
SELECT 
    schemaname,
    tablename,
    policyname,
    permissive,
    roles,
    cmd,
    qual,
    with_check
FROM pg_policies
WHERE schemaname = 'public' 
  AND tablename = 'transits_overview'
ORDER BY policyname;

-- Résultat attendu: Au moins une policy avec qual contenant "auth.uid()"

-- 4. Vérifier les RLS policies sur transits_events
SELECT 
    schemaname,
    tablename,
    policyname,
    permissive,
    roles,
    cmd,
    qual,
    with_check
FROM pg_policies
WHERE schemaname = 'public' 
  AND tablename = 'transits_events'
ORDER BY policyname;

-- 5. Compter les lignes dans transits_overview
SELECT 
    COUNT(*) as total_rows,
    COUNT(DISTINCT user_id) as distinct_user_ids,
    MIN(created_at) as oldest_record,
    MAX(created_at) as newest_record
FROM public.transits_overview;

-- 6. Compter les lignes dans transits_events
SELECT 
    COUNT(*) as total_rows,
    COUNT(DISTINCT user_id) as distinct_user_ids,
    MIN(created_at) as oldest_record,
    MAX(created_at) as newest_record
FROM public.transits_events;

-- 7. Vérifier qu'il n'y a pas de Foreign Key vers public.users
SELECT 
    tc.constraint_name,
    tc.table_name,
    kcu.column_name,
    ccu.table_name AS foreign_table_name,
    ccu.column_name AS foreign_column_name
FROM information_schema.table_constraints AS tc
JOIN information_schema.key_column_usage AS kcu
    ON tc.constraint_name = kcu.constraint_name
    AND tc.table_schema = kcu.table_schema
JOIN information_schema.constraint_column_usage AS ccu
    ON ccu.constraint_name = tc.constraint_name
    AND ccu.table_schema = tc.table_schema
WHERE tc.constraint_type = 'FOREIGN KEY'
    AND tc.table_schema = 'public'
    AND tc.table_name IN ('transits_overview', 'transits_events')
    AND kcu.column_name = 'user_id';

-- Résultat attendu: Aucune ligne (pas de FK vers public.users)

-- 8. Vérifier les index sur user_id
SELECT 
    tablename,
    indexname,
    indexdef
FROM pg_indexes
WHERE schemaname = 'public'
    AND tablename IN ('transits_overview', 'transits_events')
    AND indexdef LIKE '%user_id%'
ORDER BY tablename, indexname;

-- Résultat attendu: Index sur user_id pour optimiser les requêtes

-- 9. Exemple de vérification: tester qu'un UUID valide peut être utilisé
-- (Cette requête ne modifie rien, juste une vérification de type)
SELECT 
    '550e8400-e29b-41d4-a716-446655440000'::uuid as test_uuid_valid;

-- 10. Vérifier qu'il n'y a pas de données avec user_id invalide (non-UUID)
-- Cette requête devrait retourner 0 lignes si tout est correct
SELECT 
    id,
    user_id,
    month,
    created_at
FROM public.transits_overview
WHERE user_id IS NULL
   OR user_id::text !~ '^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$';

-- Résultat attendu: 0 lignes (tous les user_id sont des UUID valides)

