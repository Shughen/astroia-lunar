-- Policies RLS recommandées pour lunar_returns et natal_charts
-- 
-- CONTEXTE:
-- - JWT token contient "sub" comme string représentant users.id (INTEGER)
-- - Les policies RLS doivent vérifier user_id (INTEGER) = users.id (INTEGER)
-- - On utilise current_setting('request.jwt.claims', true)::json ->> 'sub' pour extraire le user_id depuis le JWT
--
-- PROBLÈME avec les policies actuelles:
-- - Elles utilisent auth.jwt() ->> 'email' puis font un SELECT pour trouver users.id
-- - C'est inefficace et fragile (email peut changer)
--
-- SOLUTION recommandée:
-- - Extraire directement "sub" du JWT (qui contient déjà users.id)
-- - Comparer directement user_id = (sub::integer)
--
-- ⚠️ NOTE: Ces policies supposent que Supabase/PostgreSQL peut accéder au JWT via request.jwt.claims
-- Si l'app FastAPI n'expose pas le JWT à PostgreSQL, il faut utiliser une approche différente:
-- - Option A: Désactiver RLS et gérer l'accès côté application (recommandé pour FastAPI)
-- - Option B: Utiliser une fonction PostgreSQL personnalisée qui extrait user_id depuis un header HTTP
--
-- Dans notre cas (FastAPI standalone), RLS devrait probablement être DÉSACTIVÉE
-- et l'accès géré côté application via get_current_user() qui vérifie le JWT.

-- ============================================
-- OPTION 1: Policies avec JWT sub (si disponible)
-- ============================================

-- Activer RLS sur les tables
ALTER TABLE natal_charts ENABLE ROW LEVEL SECURITY;
ALTER TABLE lunar_returns ENABLE ROW LEVEL SECURITY;

-- Supprimer les anciennes policies (si elles existent)
DROP POLICY IF EXISTS allow_select_own_rows ON natal_charts;
DROP POLICY IF EXISTS allow_insert_own_rows ON natal_charts;
DROP POLICY IF EXISTS allow_update_own_rows ON natal_charts;
DROP POLICY IF EXISTS allow_delete_own_rows ON natal_charts;

DROP POLICY IF EXISTS allow_select_own_rows ON lunar_returns;
DROP POLICY IF EXISTS allow_insert_own_rows ON lunar_returns;
DROP POLICY IF EXISTS allow_update_own_rows ON lunar_returns;
DROP POLICY IF EXISTS allow_delete_own_rows ON lunar_returns;

-- Policies natal_charts (avec JWT sub)
CREATE POLICY allow_select_own_rows ON natal_charts
    FOR SELECT
    USING (user_id = (current_setting('request.jwt.claims', true)::json ->> 'sub')::integer);

CREATE POLICY allow_insert_own_rows ON natal_charts
    FOR INSERT
    WITH CHECK (user_id = (current_setting('request.jwt.claims', true)::json ->> 'sub')::integer);

CREATE POLICY allow_update_own_rows ON natal_charts
    FOR UPDATE
    USING (user_id = (current_setting('request.jwt.claims', true)::json ->> 'sub')::integer)
    WITH CHECK (user_id = (current_setting('request.jwt.claims', true)::json ->> 'sub')::integer);

CREATE POLICY allow_delete_own_rows ON natal_charts
    FOR DELETE
    USING (user_id = (current_setting('request.jwt.claims', true)::json ->> 'sub')::integer);

-- Policies lunar_returns (avec JWT sub)
CREATE POLICY allow_select_own_rows ON lunar_returns
    FOR SELECT
    USING (user_id = (current_setting('request.jwt.claims', true)::json ->> 'sub')::integer);

CREATE POLICY allow_insert_own_rows ON lunar_returns
    FOR INSERT
    WITH CHECK (user_id = (current_setting('request.jwt.claims', true)::json ->> 'sub')::integer);

CREATE POLICY allow_update_own_rows ON lunar_returns
    FOR UPDATE
    USING (user_id = (current_setting('request.jwt.claims', true)::json ->> 'sub')::integer)
    WITH CHECK (user_id = (current_setting('request.jwt.claims', true)::json ->> 'sub')::integer);

CREATE POLICY allow_delete_own_rows ON lunar_returns
    FOR DELETE
    USING (user_id = (current_setting('request.jwt.claims', true)::json ->> 'sub')::integer);

-- ============================================
-- OPTION 2: Désactiver RLS (recommandé pour FastAPI standalone)
-- ============================================
--
-- Si l'app FastAPI gère l'authentification et l'autorisation côté application
-- (via get_current_user() qui vérifie le JWT), on peut désactiver RLS:
--
-- ALTER TABLE natal_charts DISABLE ROW LEVEL SECURITY;
-- ALTER TABLE lunar_returns DISABLE ROW LEVEL SECURITY;
--
-- C'est plus simple et évite les problèmes de synchronisation JWT entre FastAPI et PostgreSQL.
--
-- ============================================
-- VÉRIFICATION des policies
-- ============================================

-- Lister toutes les policies RLS
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
    AND tablename IN ('natal_charts', 'lunar_returns')
ORDER BY tablename, policyname;

