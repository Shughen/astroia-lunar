# Fix: Correction erreur "operator does not exist: uuid = integer" pour transits_overview

## Problème
- DB Supabase: `public.transits_overview.user_id` est de type UUID
- RLS policies utilisent `(user_id = auth.uid())` donc `user_id` doit rester UUID
- L'app mobile en DEV_AUTH_BYPASS envoyait `X-Dev-User-Id: 1` (integer)
- Côté API, `user_id` était typé `int` => bind `$1::INTEGER` => crash `uuid = integer`

## Solution implémentée

### 1. Mobile (`apps/mobile/`)

#### `services/api.ts`
- ✅ `EXPO_PUBLIC_DEV_USER_ID` doit maintenant être un UUID string (ex: `"550e8400-e29b-41d4-a716-446655440000"`)
- ✅ Par défaut: UUID de test `550e8400-e29b-41d4-a716-446655440000`
- ✅ `transits.getOverview()` accepte maintenant `userId: string` (UUID) au lieu de `number`

#### `app/transits/overview.tsx`
- ✅ `userId` est maintenant `string` (UUID) au lieu de `number`
- ✅ Conversion depuis `getDevUserId()` qui retourne déjà un UUID string

### 2. API (`apps/api/`)

#### `routes/auth.py`
- ✅ Import `from uuid import UUID`
- ✅ `get_current_user()` traite `X-Dev-User-Id` comme UUID (validation avec `UUID(x_dev_user_id)`)
- ✅ Création d'un `MockUser` avec méthode `get_uuid()` pour propager l'UUID en DEV_AUTH_BYPASS
- ✅ Note: `users.id` (FastAPI) reste Integer, mais `transits_overview.user_id` pointe vers `auth.users.id` (UUID Supabase)

#### `models/transits.py`
- ✅ Import `from sqlalchemy.dialects.postgresql import UUID`
- ✅ `TransitsOverview.user_id`: `Column(Integer, ...)` → `Column(UUID(as_uuid=True), ...)`
- ✅ `TransitsEvent.user_id`: `Column(Integer, ...)` → `Column(UUID(as_uuid=True), ...)`
- ✅ Suppression des relations `ForeignKey("users.id")` car `user_id` pointe vers `auth.users.id` (UUID) et non `public.users.id` (Integer)
- ✅ Suppression des relations `relationship("User", ...)` dans les modèles Transits

#### `models/user.py`
- ✅ Suppression des relations `transits_overviews` et `transits_events` car `user_id` pointe vers `auth.users.id` (UUID) et non `users.id` (Integer)

#### `routes/transits.py`
- ✅ Import `from uuid import UUID`
- ✅ `get_transits_overview(user_id: int, ...)` → `get_transits_overview(user_id: UUID, ...)`
- ✅ `get_user_transits_history(user_id: int, ...)` → `get_user_transits_history(user_id: UUID, ...)`
- ✅ Les requêtes SQLAlchemy comparent maintenant `UUID = UUID` (pas `UUID = INTEGER`)

#### `schemas/transits.py`
- ✅ Import `from uuid import UUID`
- ✅ `NatalTransitsRequest.user_id`: `Optional[int]` → `Optional[UUID]`
- ✅ `LunarReturnTransitsRequest.user_id`: `Optional[int]` → `Optional[UUID]`
- ✅ `TransitsOverviewDB.user_id`: `int` → `UUID`
- ✅ `TransitsEventDB.user_id`: `int` → `UUID`

## Fichiers modifiés

### Mobile
- `apps/mobile/services/api.ts`
- `apps/mobile/app/transits/overview.tsx`

### API
- `apps/api/routes/auth.py`
- `apps/api/models/transits.py`
- `apps/api/models/user.py`
- `apps/api/routes/transits.py`
- `apps/api/schemas/transits.py`

## Tests

Voir `apps/api/TEST_TRANSITS_UUID.md` pour les commandes curl de test.

### Test rapide
```bash
UUID="550e8400-e29b-41d4-a716-446655440000"
MONTH="2025-01"

curl -X GET "http://localhost:8000/api/transits/overview/${UUID}/${MONTH}" \
  -H "X-Dev-User-Id: ${UUID}" \
  -H "Content-Type: application/json" \
  -v
```

## Configuration requise

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

## Notes importantes

1. **Pas de migration DB nécessaire**: La colonne `transits_overview.user_id` est déjà UUID dans Supabase
2. **RLS policies**: Les policies existantes utilisent `(user_id = auth.uid())` et continuent de fonctionner
3. **Pas de drop de tables**: Aucune table n'a été supprimée
4. **Alembic**: Déjà "stamped" sur `9737ece7c259`, pas besoin de nouvelle migration
5. **Relations SQLAlchemy**: Supprimées car `user_id` pointe vers `auth.users.id` (UUID Supabase) et non `public.users.id` (Integer FastAPI)

## Vérifications

- ✅ Le header `X-Dev-User-Id` est bien un UUID string
- ✅ L'endpoint `/api/transits/overview/{uuid}/{month}` accepte UUID
- ✅ La requête SQL compare `user_id = UUID` (pas `user_id = integer`)
- ✅ Les RLS policies fonctionnent avec `auth.uid()` (UUID)
- ✅ Pas d'erreur `operator does not exist: uuid = integer`

