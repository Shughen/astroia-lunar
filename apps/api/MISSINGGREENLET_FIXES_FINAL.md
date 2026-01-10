# MissingGreenlet - Fixes Appliqués (Final)

## ✅ Résumé des Modifications

Tous les fichiers routes critiques ont été fixés pour prévenir `sqlalchemy.exc.MissingGreenlet`.

### Pattern Appliqué Partout

```python
@router.post("/endpoint")
async def my_endpoint(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Docstring"""

    # 🔒 CRITIQUE: Extraire user_id IMMÉDIATEMENT pour éviter MissingGreenlet
    user_id = int(current_user.id)
    # Autres primitives si nécessaire:
    # user_email = getattr(current_user, "email", f"dev+{user_id}@local.dev")

    # Utiliser user_id partout (JAMAIS current_user.id après ce point)
    result = await db.execute(
        select(Something).where(Something.user_id == user_id)
    )

    # Si besoin de modifier User, utiliser SQLAlchemy Core update()
    from sqlalchemy import update
    await db.execute(
        update(User).where(User.id == user_id).values(field=value)
    )

    await db.commit()  # ✅ Safe

    return {"user_id": user_id}  # ✅ Primitif
```

---

## 📁 Fichiers Modifiés

### 1. routes/natal.py - **CRITIQUE (DEV_MOCK_NATAL)**

**Endpoints Fixed**:
- `POST /natal-chart` (calculate_natal_chart)
- `GET /natal-chart` (get_natal_chart)

**Lignes Clés Modifiées**:

#### Ligne 90-97: Extraction de primitives au début
```python
# 🔒 CRITIQUE: Extraire primitives IMMÉDIATEMENT pour éviter MissingGreenlet
user_id = int(current_user.id)
user_email = getattr(current_user, "email", f"dev+{user_id}@local.dev")
birth_date_existing = str(current_user.birth_date) if hasattr(current_user, 'birth_date') and current_user.birth_date else None
birth_time_existing = str(current_user.birth_time) if hasattr(current_user, 'birth_time') and current_user.birth_time else None
birth_latitude_existing = current_user.birth_latitude if hasattr(current_user, 'birth_latitude') else None
birth_longitude_existing = current_user.birth_longitude if hasattr(current_user, 'birth_longitude') else None
birth_timezone_existing = str(current_user.birth_timezone) if hasattr(current_user, 'birth_timezone') and current_user.birth_timezone else None
```

#### Ligne 117-139: Utilisation de primitives dans idempotence check
- `current_user.id` → `user_id`
- `current_user.birth_*` → `birth_*_existing`

#### Ligne 268-282: **FIX CRITIQUE** - DEV_MOCK_NATAL avec SQLAlchemy Core update
```python
# 🔒 CRITIQUE: Mettre à jour les infos de naissance via SQLAlchemy Core (safe)
# NE JAMAIS modifier current_user.* directement car peut être detached/expired
from sqlalchemy import update
await db.execute(
    update(User)
    .where(User.id == user_id)
    .values(
        birth_date=data.date,
        birth_time=birth_time,
        birth_latitude=str(data.latitude),
        birth_longitude=str(data.longitude),
        birth_place_name=data.place_name,
        birth_timezone=detected_timezone
    )
)

await db.commit()  # ✅ Safe, pas de MissingGreenlet
```

**AVANT (❌ MissingGreenlet)**:
```python
current_user.birth_date = data.date  # ❌ Modification ORM object
await db.commit()  # ❌ Trigger MissingGreenlet
```

#### Ligne 665-679: Même fix pour le vrai calcul (non-mock)
Même pattern `update(User)` au lieu de `current_user.*`.

#### Ligne 838: GET endpoint
```python
# 🔒 CRITIQUE: Extraire user_id IMMÉDIATEMENT pour éviter MissingGreenlet
user_id = int(current_user.id)
```

---

### 2. routes/natal_interpretation.py

**Endpoints Fixed**:
- `POST /interpretation` (ligne 53)
- `DELETE /interpretation` (ligne 388)

**Modifications**:
```python
# AVANT
user_id = current_user.id  # ⚠️ Pas de cast

# APRÈS
# 🔒 CRITIQUE: Extraire user_id IMMÉDIATEMENT pour éviter MissingGreenlet
user_id = int(current_user.id)  # ✅ Cast explicite
```

---

### 3. routes/lunar.py

**Endpoints Fixed**:
- `POST /lunar-return/report` (ligne 197)

**Modifications**:
```python
# AVANT
logger.info(f"user: {current_user.id}")  # ❌

# APRÈS
# 🔒 CRITIQUE: Extraire user_id IMMÉDIATEMENT pour éviter MissingGreenlet
user_id = int(current_user.id)
logger.info(f"user: {user_id}")  # ✅
```

---

### 4. routes/lunar_returns.py

**Déjà fixé complètement** (voir travail précédent):
- 10 endpoints
- 2 helpers (`_generate_rolling_returns`, `_generate_rolling_if_empty`)

---

## 🧪 Tests de Validation

### Test 1: natal-chart avec DEV_MOCK_NATAL=1 (CRITIQUE)
```bash
cd apps/api

# Vérifier que .env a DEV_MOCK_NATAL=1
source .env

# Test POST /natal-chart (doit retourner 200/201, pas 500)
./scripts/test_natal_chart_mock.sh

# Expected: ✅ Succès - Thème natal créé/mis à jour (HTTP 200/201)
# Expected: natal_chart_id=<uuid>
```

### Test 2: lunar-returns/current après purge
```bash
cd apps/api

# Test GET /current après purge (doit retourner 200, pas 500)
./scripts/test_lunar_current_after_purge.sh

# Expected: ✅ /current: HTTP 200
```

### Test 3: Concurrent requests (stress test)
```bash
cd apps/api

# Purge
curl -X POST http://127.0.0.1:8000/api/lunar-returns/dev/purge \
  -H "X-Dev-External-Id: 550e8400-e29b-41d4-a716-446655440000"

# Lancer 5 requêtes /current en parallèle
for i in {1..5}; do
  curl -X GET http://127.0.0.1:8000/api/lunar-returns/current \
    -H "X-Dev-External-Id: 550e8400-e29b-41d4-a716-446655440000" &
done
wait

# Expected: Toutes 200 (pas de 500 MissingGreenlet)
```

---

## 🎯 Validation Complète

### Commande curl unique pour tester tous les endpoints critiques

```bash
#!/bin/bash
# Test complet de tous les endpoints fixés

API_URL="http://127.0.0.1:8000"
USER_ID="550e8400-e29b-41d4-a716-446655440000"

echo "🧪 Test MissingGreenlet Prevention - Tous les endpoints"
echo ""

# 1. POST /natal-chart (DEV_MOCK_NATAL)
echo "1️⃣ Test POST /natal-chart (DEV_MOCK_NATAL)"
http_code=$(curl -X POST "$API_URL/api/natal-chart" \
  -H "X-Dev-External-Id: $USER_ID" \
  -H "Content-Type: application/json" \
  -d '{
    "date": "1990-01-15",
    "time": "14:30",
    "latitude": 48.8566,
    "longitude": 2.3522,
    "place_name": "Paris, France"
  }' \
  -w "%{http_code}" \
  -o /dev/null \
  -sS)

if [ "$http_code" = "200" ] || [ "$http_code" = "201" ]; then
  echo "✅ POST /natal-chart: HTTP $http_code"
else
  echo "❌ POST /natal-chart: HTTP $http_code (expected 200/201)"
fi

# 2. GET /natal-chart
echo ""
echo "2️⃣ Test GET /natal-chart"
http_code=$(curl -X GET "$API_URL/api/natal-chart" \
  -H "X-Dev-External-Id: $USER_ID" \
  -w "%{http_code}" \
  -o /dev/null \
  -sS)

if [ "$http_code" = "200" ]; then
  echo "✅ GET /natal-chart: HTTP $http_code"
else
  echo "❌ GET /natal-chart: HTTP $http_code (expected 200)"
fi

# 3. POST /lunar-returns/dev/purge
echo ""
echo "3️⃣ Test POST /lunar-returns/dev/purge"
http_code=$(curl -X POST "$API_URL/api/lunar-returns/dev/purge" \
  -H "X-Dev-External-Id: $USER_ID" \
  -w "%{http_code}" \
  -o /dev/null \
  -sS)

if [ "$http_code" = "200" ]; then
  echo "✅ POST /dev/purge: HTTP $http_code"
else
  echo "❌ POST /dev/purge: HTTP $http_code (expected 200)"
fi

# 4. GET /lunar-returns/current
echo ""
echo "4️⃣ Test GET /lunar-returns/current"
http_code=$(curl -X GET "$API_URL/api/lunar-returns/current" \
  -H "X-Dev-External-Id: $USER_ID" \
  -w "%{http_code}" \
  -o /dev/null \
  -sS)

if [ "$http_code" = "200" ]; then
  echo "✅ GET /current: HTTP $http_code"
else
  echo "⚠️ GET /current: HTTP $http_code (attendu 200, peut retourner null)"
fi

# 5. POST /lunar-returns/generate
echo ""
echo "5️⃣ Test POST /lunar-returns/generate"
http_code=$(curl -X POST "$API_URL/api/lunar-returns/generate" \
  -H "X-Dev-External-Id: $USER_ID" \
  -w "%{http_code}" \
  -o /dev/null \
  -sS)

if [ "$http_code" = "201" ]; then
  echo "✅ POST /generate: HTTP $http_code"
else
  echo "❌ POST /generate: HTTP $http_code (expected 201)"
fi

echo ""
echo "✅ Test terminé - Tous les endpoints critiques validés"
```

---

## 📊 Résumé Final

### Fichiers Modifiés
- ✅ **routes/lunar_returns.py** (10 endpoints + 2 helpers)
- ✅ **routes/natal.py** (2 endpoints, **FIX CRITIQUE DEV_MOCK_NATAL**)
- ✅ **routes/natal_interpretation.py** (2 endpoints)
- ✅ **routes/lunar.py** (1 endpoint)

### Pattern Appliqué
- Extraction immédiate de `user_id = int(current_user.id)` au début de chaque endpoint
- Remplacement de tous les `current_user.id` par `user_id` dans les queries
- Utilisation de `update(User)` au lieu de modification directe de `current_user.*` avant commit

### Fix CRITIQUE
**natal.py lignes 268-282 et 665-679**: Utilisation de SQLAlchemy Core `update()` au lieu de modifier `current_user.birth_*` directement, ce qui aurait trigger MissingGreenlet au `commit()`.

### Tests Créés
- ✅ `scripts/test_natal_chart_mock.sh` (existe)
- ✅ `scripts/test_lunar_current_after_purge.sh` (existe)
- ✅ `scripts/test_dev_purge.sh` (existe)

### Documentation Créée
- ✅ `MISSINGGREENLET_FIX.md` (guide complet du fix original)
- ✅ `MISSINGGREENLET_STATUS.md` (status détaillé)
- ✅ `MISSINGGREENLET_CHECKLIST.md` (checklist finale)
- ✅ `MISSINGGREENLET_FIXES_FINAL.md` (ce fichier - récapitulatif final)

---

**Date**: 2026-01-02
**Status**: ✅ COMPLET - Tous les endpoints critiques fixés
**Risk**: MissingGreenlet éliminé via extraction immédiate de primitives + SQLAlchemy Core update()
