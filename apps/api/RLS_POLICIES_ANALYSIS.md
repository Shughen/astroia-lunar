# Analyse des policies RLS et recommandations

**Date:** 2025-01-XX  
**Objectif:** Analyser comment `current_user.id` est dérivé du JWT et proposer des policies RLS robustes

---

## 🔍 Analyse de l'authentification

### Comment `current_user.id` est dérivé du JWT

**Fichier:** `routes/auth.py` - fonction `get_current_user()`

```python
payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
user_id_str: str = payload.get("sub")
user_id: int = int(user_id_str)  # Convert string sub to int
```

**Points clés:**
1. Le JWT contient `"sub"` comme **string** représentant `users.id` (INTEGER)
2. La conversion `int(user_id_str)` transforme la string en INTEGER
3. `users.id` est **INTEGER** (pas UUID)
4. L'authentification est gérée côté **FastAPI**, pas PostgreSQL

---

## 📊 Policies RLS actuelles

### Dans `migrate_lunar_returns_user_id_to_int_simple.sql`

```sql
-- Policy SELECT: les utilisateurs peuvent voir leurs propres révolutions lunaires
CREATE POLICY allow_select_own_rows ON lunar_returns
    FOR SELECT
    USING (user_id = (SELECT id FROM users WHERE email = auth.jwt() ->> 'email'));
```

**Problèmes identifiés:**
1. ❌ Utilise `auth.jwt() ->> 'email'` puis fait un `SELECT` pour trouver `users.id`
2. ❌ Inefficace (requête supplémentaire à chaque accès)
3. ❌ Fragile (email peut changer)
4. ❌ Ne correspond pas à la logique FastAPI (qui utilise `sub` directement)

---

## ✅ Recommandation: Utiliser `sub` du JWT directement

### Option 1: Policies avec `current_setting('request.jwt.claims')` (si disponible)

**Hypothèse:** PostgreSQL peut accéder au JWT via `current_setting('request.jwt.claims', true)::json ->> 'sub'`

**Policies recommandées:**

```sql
-- Activer RLS
ALTER TABLE lunar_returns ENABLE ROW LEVEL SECURITY;

-- Supprimer les anciennes policies
DROP POLICY IF EXISTS allow_select_own_rows ON lunar_returns;
DROP POLICY IF EXISTS allow_insert_own_rows ON lunar_returns;
DROP POLICY IF EXISTS allow_update_own_rows ON lunar_returns;
DROP POLICY IF EXISTS allow_delete_own_rows ON lunar_returns;

-- Policies avec JWT sub (cast en INTEGER)
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
```

**Avantages:**
- ✅ Utilise directement `sub` (comme FastAPI)
- ✅ Pas de `SELECT` supplémentaire
- ✅ Plus rapide
- ✅ Aligné avec la logique d'authentification

**Inconvénient:**
- ⚠️ Nécessite que PostgreSQL puisse accéder au JWT (dépend de la configuration Supabase/PostgreSQL)

---

### Option 2: Désactiver RLS (recommandé pour FastAPI standalone)

**Si FastAPI gère déjà l'authentification via `get_current_user()`**, on peut désactiver RLS:

```sql
-- Désactiver RLS
ALTER TABLE lunar_returns DISABLE ROW LEVEL SECURITY;
ALTER TABLE natal_charts DISABLE ROW LEVEL SECURITY;
```

**Avantages:**
- ✅ Plus simple (pas de synchronisation JWT nécessaire)
- ✅ L'authentification est déjà gérée dans FastAPI
- ✅ Pas de risque de désynchronisation entre FastAPI et PostgreSQL
- ✅ Performance légèrement meilleure (pas de vérification RLS)

**Inconvénient:**
- ⚠️ Sécurité uniquement côté application (mais c'est déjà le cas avec FastAPI)

**Recommandation:** **Option 2 (désactiver RLS)** car:
1. L'app FastAPI gère déjà l'authentification via `get_current_user()`
2. Toutes les requêtes passent par FastAPI (pas d'accès direct à la DB)
3. Plus simple à maintenir
4. Évite les problèmes de synchronisation JWT

---

## 🔧 Migration recommandée

### Pour désactiver RLS (Option 2 - recommandé)

**Script SQL:**

```sql
-- Désactiver RLS sur les tables concernées
ALTER TABLE natal_charts DISABLE ROW LEVEL SECURITY;
ALTER TABLE lunar_returns DISABLE ROW LEVEL SECURITY;

-- Vérifier que RLS est désactivé
SELECT tablename, rowsecurity 
FROM pg_tables 
WHERE schemaname = 'public' 
  AND tablename IN ('natal_charts', 'lunar_returns');
-- rowsecurity devrait être 'f' (false)
```

### Pour utiliser JWT sub (Option 1 - si nécessaire)

Voir `scripts/sql/rls_policies_recommended.sql` pour les policies complètes.

---

## 📝 Résumé et action recommandée

### Situation actuelle
- ✅ FastAPI utilise `sub` (string) du JWT → convertit en `int` → `users.id`
- ❌ Policies RLS utilisent `email` → `SELECT` → `users.id` (inefficace et fragile)

### Recommandation finale

**Désactiver RLS** car:
1. FastAPI gère déjà l'authentification
2. Plus simple et plus performant
3. Évite les problèmes de synchronisation

**Script à exécuter:**

```sql
-- Désactiver RLS
ALTER TABLE natal_charts DISABLE ROW LEVEL SECURITY;
ALTER TABLE lunar_returns DISABLE ROW LEVEL SECURITY;

-- Supprimer les anciennes policies (nettoyage)
DROP POLICY IF EXISTS allow_select_own_rows ON natal_charts;
DROP POLICY IF EXISTS allow_insert_own_rows ON natal_charts;
DROP POLICY IF EXISTS allow_update_own_rows ON natal_charts;
DROP POLICY IF EXISTS allow_delete_own_rows ON natal_charts;

DROP POLICY IF EXISTS allow_select_own_rows ON lunar_returns;
DROP POLICY IF EXISTS allow_insert_own_rows ON lunar_returns;
DROP POLICY IF EXISTS allow_update_own_rows ON lunar_returns;
DROP POLICY IF EXISTS allow_delete_own_rows ON lunar_returns;
```

**Si RLS doit absolument être activé** (par ex. pour sécurité Supabase), utiliser Option 1 avec `current_setting('request.jwt.claims')` et `sub`.

