# Alignement UUID Supabase de bout en bout pour Transits

## ✅ Résumé des modifications

### 1. API - Routes Transits

#### `routes/transits.py`
- ✅ `get_transits_overview(user_id: UUID, ...)` - Paramètre `user_id` typé `UUID` (python `uuid.UUID`)
- ✅ `get_user_transits_history(user_id: UUID, ...)` - Paramètre `user_id` typé `UUID`
- ✅ Aucune jointure/lookup vers `public.users` - Les requêtes utilisent directement `user_id` UUID
- ✅ Les requêtes SQLAlchemy comparent `TransitsOverview.user_id == UUID` (pas `== int`)

#### `routes/auth.py` - DEV_AUTH_BYPASS
- ✅ `X-Dev-User-Id` accepté comme UUID string
- ✅ Validation avec `UUID(x_dev_user_id)` - lève `ValueError` si invalide
- ✅ Propagation directe de l'UUID sans lookup dans `public.users`
- ✅ Création d'un `MockUser` avec méthode `get_uuid()` pour compatibilité
- ✅ Logs clairs : UUID valide/invalide

### 2. API - Modèles SQLAlchemy

#### `models/transits.py`
- ✅ `TransitsOverview.user_id = Column(UUID(as_uuid=True), ...)`
- ✅ `TransitsEvent.user_id = Column(UUID(as_uuid=True), ...)`
- ✅ **Pas de ForeignKey** vers `public.users` (user_id pointe vers `auth.users.id` UUID Supabase)
- ✅ **Pas de relationship** vers `User` (les RLS policies gèrent l'accès)

#### `models/user.py`
- ✅ Suppression des relations `transits_overviews` et `transits_events`
- ✅ Commentaire explicatif : user_id pointe vers `auth.users.id` (UUID) et non `users.id` (Integer)

### 3. API - Schémas Pydantic

#### `schemas/transits.py`
- ✅ `NatalTransitsRequest.user_id: Optional[UUID]`
- ✅ `LunarReturnTransitsRequest.user_id: Optional[UUID]`
- ✅ `TransitsOverviewDB.user_id: UUID`
- ✅ `TransitsEventDB.user_id: UUID`

### 4. Mobile

#### `services/api.ts`
- ✅ `EXPO_PUBLIC_DEV_USER_ID` doit être un UUID string
- ✅ **Guard de validation UUID** avec regex et log clair si invalide
- ✅ Fallback vers UUID par défaut si invalide : `550e8400-e29b-41d4-a716-446655440000`
- ✅ `transits.getOverview(userId: string)` - Paramètre typé `string` (UUID)

#### `app/transits/overview.tsx`
- ✅ `userId` est `string` (UUID) au lieu de `number`
- ✅ Conversion depuis `getDevUserId()` qui retourne déjà un UUID string

## 🔍 Vérifications DB (non destructives)

### Script SQL de vérification

Fichier : `apps/api/scripts/sql/verify_transits_uuid.sql`

Exécuter dans Supabase SQL Editor pour vérifier :
1. Type de colonne `user_id` (doit être `uuid`)
2. Existence des RLS policies avec `auth.uid()`
3. Absence de Foreign Key vers `public.users`
4. Index sur `user_id` pour performance
5. Tous les `user_id` existants sont des UUID valides
6. Comptage des lignes

### Commandes de vérification rapide

```sql
-- Vérifier le type de user_id
SELECT column_name, data_type, udt_name
FROM information_schema.columns
WHERE table_schema = 'public' 
  AND table_name = 'transits_overview'
  AND column_name = 'user_id';
-- Attendu: data_type = 'uuid', udt_name = 'uuid'

-- Vérifier les RLS policies
SELECT policyname, qual
FROM pg_policies
WHERE schemaname = 'public' 
  AND tablename = 'transits_overview';
-- Attendu: qual contient "auth.uid()"

-- Vérifier l'absence de FK vers public.users
SELECT tc.constraint_name, tc.table_name
FROM information_schema.table_constraints AS tc
WHERE tc.constraint_type = 'FOREIGN KEY'
    AND tc.table_schema = 'public'
    AND tc.table_name = 'transits_overview'
    AND tc.constraint_name LIKE '%user_id%';
-- Attendu: 0 lignes (pas de FK vers public.users)
```

## 🧪 Tests

### Test curl - Succès (200 OK)

```bash
UUID="550e8400-e29b-41d4-a716-446655440000"
MONTH="2025-01"

curl -X GET "http://localhost:8000/api/transits/overview/${UUID}/${MONTH}" \
  -H "X-Dev-User-Id: ${UUID}" \
  -H "Content-Type: application/json" \
  -v
```

**Vérification critique** : La réponse ne doit **PAS** contenir l'erreur :
```
operator does not exist: uuid = integer
```

Si cette erreur apparaît, le fix n'est pas appliqué correctement.

### Test curl - UUID invalide (422)

```bash
INVALID_UUID="not-a-uuid"
MONTH="2025-01"

curl -X GET "http://localhost:8000/api/transits/overview/${INVALID_UUID}/${MONTH}" \
  -H "X-Dev-User-Id: ${INVALID_UUID}" \
  -H "Content-Type: application/json" \
  -v
```

**Résultat attendu** : `422 Unprocessable Entity` avec message `"value is not a valid uuid"`

### Test curl - POST /api/transits/natal

```bash
UUID="550e8400-e29b-41d4-a716-446655440000"

curl -X POST "http://localhost:8000/api/transits/natal" \
  -H "X-Dev-User-Id: ${UUID}" \
  -H "Content-Type: application/json" \
  -d '{
    "birth_date": "1990-01-01",
    "birth_time": "12:00",
    "birth_latitude": 48.8566,
    "birth_longitude": 2.3522,
    "birth_timezone": "Europe/Paris",
    "transit_date": "2025-01-15",
    "user_id": "'${UUID}'"
  }' \
  -v
```

## 📋 Configuration requise

### Mobile (.env)
```env
EXPO_PUBLIC_DEV_AUTH_BYPASS=true
EXPO_PUBLIC_DEV_USER_ID=550e8400-e29b-41d4-a716-446655440000
```

### API (.env)
```env
DEV_AUTH_BYPASS=true
APP_ENV=development
```

## ✅ Checklist de validation

### API
- [x] Routes transits : `user_id` param type = `UUID` (python `uuid.UUID`)
- [x] Modèles SQLAlchemy : `user_id = UUID(as_uuid=True)`
- [x] Pas de ForeignKey vers `public.users` dans les modèles transits
- [x] Pydantic schemas : `user_id: UUID`
- [x] DEV_AUTH_BYPASS : accepte `X-Dev-User-Id` comme UUID string, valide et propage sans lookup dans `public.users`
- [x] Supprimé toute jointure/lookup sur `public.users` pour transits

### Mobile
- [x] `EXPO_PUBLIC_DEV_USER_ID` est un UUID string
- [x] `transits.getOverview(userId: string)` utilise UUID
- [x] Guard de validation UUID en dev avec log clair si invalide

### DB
- [x] Script SQL de vérification fourni (non destructif)
- [x] Vérification type colonne, RLS policies, count rows

### Tests
- [x] Curl de test avec UUID (header `X-Dev-User-Id` + path param)
- [x] Vérification que l'endpoint ne renvoie plus `operator does not exist: uuid = integer`

## 📝 Notes importantes

1. **Pas de migration DB nécessaire** : La colonne `transits_overview.user_id` est déjà UUID dans Supabase
2. **RLS policies** : Les policies existantes utilisent `(user_id = auth.uid())` et continuent de fonctionner
3. **Pas de drop de tables** : Aucune table n'a été supprimée
4. **Alembic** : Déjà "stamped" sur `9737ece7c259`, pas besoin de nouvelle migration
5. **Relations SQLAlchemy** : Supprimées car `user_id` pointe vers `auth.users.id` (UUID Supabase) et non `public.users.id` (Integer FastAPI)
6. **DEV_AUTH_BYPASS** : Ne fait plus de lookup dans `public.users`, propage directement l'UUID

## 🎯 Résultat final

- ✅ Plus d'erreur `operator does not exist: uuid = integer`
- ✅ Les requêtes SQL comparent `UUID = UUID` (pas `UUID = INTEGER`)
- ✅ Les RLS policies fonctionnent avec `auth.uid()` (UUID)
- ✅ Le code est cohérent avec le schéma DB Supabase
- ✅ Validation UUID côté mobile avec guard et logs clairs
- ✅ Aucune dépendance vers `public.users` pour les transits

