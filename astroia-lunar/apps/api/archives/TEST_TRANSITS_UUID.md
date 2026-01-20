# Test Transits Overview avec UUID

## Contexte
Correction de l'erreur `operator does not exist: uuid = integer` en utilisant UUID partout pour `transits_overview.user_id`.

## Configuration requise

### Variables d'environnement

**Mobile (.env):**
```env
EXPO_PUBLIC_DEV_AUTH_BYPASS=true
EXPO_PUBLIC_DEV_USER_ID=550e8400-e29b-41d4-a716-446655440000
```

**API (.env):**
```env
DEV_AUTH_BYPASS=true
APP_ENV=development
```

## Test curl

### 1. Test GET /api/transits/overview/{uuid}/{month} - Succès

```bash
# UUID de test (doit correspondre à EXPO_PUBLIC_DEV_USER_ID)
UUID="550e8400-e29b-41d4-a716-446655440000"
MONTH="2025-01"

# Test avec header X-Dev-User-Id
curl -X GET "http://localhost:8000/api/transits/overview/${UUID}/${MONTH}" \
  -H "X-Dev-User-Id: ${UUID}" \
  -H "Content-Type: application/json" \
  -v

# Vérifier que la réponse ne contient PAS l'erreur "operator does not exist: uuid = integer"
# Si l'erreur apparaît, c'est que le fix n'est pas appliqué correctement
```

### 1b. Test GET /api/transits/overview/{uuid}/{month} - UUID invalide (doit échouer avec 422)

```bash
# Test avec un UUID invalide (doit retourner 422)
INVALID_UUID="not-a-uuid"
MONTH="2025-01"

curl -X GET "http://localhost:8000/api/transits/overview/${INVALID_UUID}/${MONTH}" \
  -H "X-Dev-User-Id: ${INVALID_UUID}" \
  -H "Content-Type: application/json" \
  -v

# Résultat attendu: 422 Unprocessable Entity avec message "value is not a valid uuid"
```

### 2. Test avec un UUID réel de Supabase

Pour obtenir un UUID réel depuis Supabase :

```sql
-- Dans Supabase SQL Editor
SELECT id FROM auth.users LIMIT 1;
```

Puis utiliser cet UUID :

```bash
# Remplacer par un UUID réel de auth.users
UUID="<uuid-reel-de-auth-users>"
MONTH="2025-01"

curl -X GET "http://localhost:8000/api/transits/overview/${UUID}/${MONTH}" \
  -H "X-Dev-User-Id: ${UUID}" \
  -H "Content-Type: application/json" \
  -v
```

### 3. Test POST /api/transits/natal avec user_id UUID

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

## Résultat attendu

### Succès (200 OK)
```json
{
  "id": 1,
  "user_id": "550e8400-e29b-41d4-a716-446655440000",
  "month": "2025-01",
  "summary": {
    "natal_transits": {...},
    "insights": {...},
    "last_updated": "2025-01-15T12:00:00"
  },
  "created_at": "2025-01-15T12:00:00"
}
```

### Erreur si UUID invalide (422)
```json
{
  "detail": [
    {
      "loc": ["path", "user_id"],
      "msg": "value is not a valid uuid",
      "type": "type_error.uuid"
    }
  ]
}
```

### Erreur si pas de données (404)
```json
{
  "detail": "Aucun transits overview trouvé pour user 550e8400-e29b-41d4-a716-446655440000 et mois 2025-01"
}
```

## Vérifications

1. ✅ Le header `X-Dev-User-Id` est bien un UUID string
2. ✅ L'endpoint `/api/transits/overview/{uuid}/{month}` accepte UUID
3. ✅ La requête SQL compare `user_id = UUID` (pas `user_id = integer`)
4. ✅ Les RLS policies fonctionnent avec `auth.uid()` (UUID)
5. ✅ Pas d'erreur `operator does not exist: uuid = integer`
6. ✅ Validation UUID côté mobile avec guard (log clair si invalide)
7. ✅ Pas de jointure/lookup vers `public.users` dans les routes transits

## Vérification DB (non destructive)

Exécuter le script SQL de vérification :

```bash
# Dans Supabase SQL Editor ou psql
psql $DATABASE_URL -f apps/api/scripts/sql/verify_transits_uuid.sql
```

Ou copier-coller le contenu de `apps/api/scripts/sql/verify_transits_uuid.sql` dans Supabase SQL Editor.

### Vérifications attendues :
- ✅ `transits_overview.user_id` est de type `uuid` (pas `integer`)
- ✅ `transits_events.user_id` est de type `uuid` (pas `integer`)
- ✅ RLS policies existent et utilisent `auth.uid()`
- ✅ Pas de Foreign Key vers `public.users`
- ✅ Index sur `user_id` pour performance
- ✅ Tous les `user_id` existants sont des UUID valides

## Logs attendus côté API

```
🔧 DEV_AUTH_BYPASS activé
📥 Header X-Dev-User-Id reçu: 550e8400-e29b-41d4-a716-446655440000
✅ DEV_AUTH_BYPASS: UUID valide reçu - 550e8400-e29b-41d4-a716-446655440000
✅ DEV_AUTH_BYPASS: user mock créé - uuid=550e8400-e29b-41d4-a716-446655440000, email=dev-user-550e8400@dev.local
```

## Notes

- Les RLS policies sur `transits_overview` utilisent `(user_id = auth.uid())` donc `user_id` doit rester UUID
- `users.id` (FastAPI) est Integer, mais `transits_overview.user_id` pointe vers `auth.users.id` (UUID Supabase)
- En mode DEV_AUTH_BYPASS, on propage l'UUID directement sans chercher dans `users` (Integer)

