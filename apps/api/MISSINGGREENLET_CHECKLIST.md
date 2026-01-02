# MissingGreenlet Prevention - Final Checklist

## ✅ Endpoints Fixed (lunar_returns.py)

| Endpoint | Method | Status | Fix Applied |
|----------|--------|--------|-------------|
| `/api/lunar-returns/generate` | POST | ✅ OK | `user_id = int(current_user.id)` + birth coords extraction au début |
| `/api/lunar-returns/` | GET | ✅ OK | `user_id = int(current_user.id)` au début |
| `/api/lunar-returns/current` | GET | ✅ OK | `user_id = int(current_user.id)` au début (fix original) |
| `/api/lunar-returns/current/report` | GET | ✅ OK | `user_id = int(current_user.id)` au début |
| `/api/lunar-returns/{id}/report` | GET | ✅ OK | `user_id = int(current_user.id)` au début |
| `/api/lunar-returns/next` | GET | ✅ OK | `user_id = int(current_user.id)` au début |
| `/api/lunar-returns/rolling` | GET | ✅ OK | `user_id = int(current_user.id)` au début |
| `/api/lunar-returns/year/{year}` | GET | ✅ OK | `user_id = int(current_user.id)` au début |
| `/api/lunar-returns/{month}` | GET | ✅ OK | `user_id = int(current_user.id)` au début |
| `/api/lunar-returns/dev/purge` | POST | ✅ OK | `user_id + email + external_id` extraction au début |

**Helpers Fixed**:
- `_generate_rolling_returns()`: Signature changée pour accepter `user_id: int`
- `_generate_rolling_if_empty()`: Extraction `user_id = int(current_user.id)` au début

---

## ⚠️ Endpoints À Vérifier Manuellement (natal.py)

| Endpoint | Method | Status | Action Requise |
|----------|--------|--------|----------------|
| `/api/natal-chart` | POST | ⚠️ À FIXER | Extraction complète de primitives au début + fix DEV_MOCK_NATAL |
| `/api/natal-chart` | PUT | ⚠️ À VÉRIFIER | Même pattern que POST |

**Problèmes Identifiés**:
1. **Ligne 107-137**: `current_user.id`, `.birth_date`, `.birth_time`, `.birth_latitude`, `.birth_longitude`, `.birth_timezone` utilisés dans idempotence check
2. **Ligne 196-197**: `current_user.id` et `.email` dans logging
3. **Ligne 240-266**: ❌ **CRITIQUE** - Modification de `current_user.birth_*` APRÈS `db.add()` et avant `commit()` (DEV_MOCK_NATAL)
4. **Ligne 558, 569**: Mêmes patterns dans update endpoint

**Fix Requis**:
```python
# Au début de calculate_natal_chart():
user_id = int(current_user.id)
user_email = str(current_user.email) if hasattr(current_user, 'email') and current_user.email else f"dev+{user_id}@local.dev"
birth_date_existing = str(current_user.birth_date) if hasattr(current_user, 'birth_date') and current_user.birth_date else None
birth_time_existing = str(current_user.birth_time) if hasattr(current_user, 'birth_time') and current_user.birth_time else None
birth_latitude_existing = current_user.birth_latitude if hasattr(current_user, 'birth_latitude') else None
birth_longitude_existing = current_user.birth_longitude if hasattr(current_user, 'birth_longitude') else None
birth_place_name_existing = str(current_user.birth_place_name) if hasattr(current_user, 'birth_place_name') and current_user.birth_place_name else None
birth_timezone_existing = str(current_user.birth_timezone) if hasattr(current_user, 'birth_timezone') and current_user.birth_timezone else None

# Puis remplacer partout:
# current_user.id → user_id
# current_user.email → user_email
# current_user.birth_* → birth_*_existing
```

**Fix DEV_MOCK_NATAL (CRITIQUE)**:
```python
# AVANT (❌ MissingGreenlet)
chart = NatalChart(user_id=current_user.id, ...)
db.add(chart)
current_user.birth_date = data.date  # ❌ Modification ORM object
await db.commit()  # ❌ Trigger MissingGreenlet

# APRÈS (✅ Safe)
chart = NatalChart(user_id=user_id, ...)
db.add(chart)

# Charger le vrai User depuis DB pour modification
from models.user import User
user_result = await db.execute(select(User).where(User.id == user_id))
db_user = user_result.scalar_one_or_none()

if db_user:
    db_user.birth_date = data.date  # ✅ Objet attaché
    db_user.birth_time = birth_time
    # ... autres champs

await db.commit()  # ✅ Safe
```

---

## ⚠️ Endpoints À Vérifier (natal_interpretation.py)

| Endpoint | Method | Status | Action Requise |
|----------|--------|--------|----------------|
| Tous les endpoints | * | ⚠️ À VÉRIFIER | Vérifier que `user_id = int(current_user.id)` est AU DÉBUT |

**Note**: Ligne 53 a déjà `user_id = current_user.id`, mais à vérifier:
1. Que c'est `int(current_user.id)` (cast explicite)
2. Que c'est au DÉBUT de l'endpoint (pas au milieu)
3. Que tous les endpoints ont cette extraction

---

## ⚠️ Endpoints À Vérifier (lunar.py)

| Endpoint | Method | Status | Action Requise |
|----------|--------|--------|----------------|
| Tous les endpoints | * | ⚠️ À SCANNER | Scanner et appliquer même pattern que lunar_returns.py |

---

## 🧪 Tests de Non-Régression Requis

### Test 1: pytest (tests/test_missinggreenlet_prevention.py)
```python
async def test_lunar_current_after_purge_no_missinggreenlet():
    """Vérifie que GET /current ne trigger pas MissingGreenlet après purge"""
    # 1. Purge
    # 2. GET /current
    # 3. Assert 200 (pas 500)

async def test_natal_chart_no_missinggreenlet():
    """Vérifie que POST /natal-chart ne trigger pas MissingGreenlet"""
    # 1. POST /natal-chart
    # 2. Assert 200/201 (pas 500)

async def test_lunar_generate_no_missinggreenlet():
    """Vérifie que POST /generate ne trigger pas MissingGreenlet"""
    # 1. Purge
    # 2. POST /generate
    # 3. Assert 201 (pas 500)
```

### Test 2: Bash scripts (déjà créés)
- [x] `apps/api/scripts/test_lunar_current_after_purge.sh` (existe déjà)
- [x] `apps/api/scripts/test_dev_purge.sh` (existe déjà)
- [ ] `apps/api/scripts/test_natal_chart_mock.sh` (à tester après fix)

---

## 📋 Commandes de Test

### 1. Test immédiat (bash)
```bash
cd apps/api

# Source .env avec flags DEV
source .env

# Test 1: Purge + /current (déjà fixed)
./scripts/test_lunar_current_after_purge.sh

# Test 2: Purge seul
./scripts/test_dev_purge.sh

# Test 3: Natal chart mock (après fix)
./scripts/test_natal_chart_mock.sh
```

### 2. Test pytest (quand créés)
```bash
cd apps/api

# Activer venv si besoin
source .venv/bin/activate

# Run tests
pytest tests/test_missinggreenlet_prevention.py -v

# Run tous les tests
pytest tests/ -v
```

### 3. Test complet (API running)
```bash
# Terminal 1: Start API
cd apps/api
source .env
uvicorn main:app --reload

# Terminal 2: Test tous les endpoints
cd apps/api

# Test lunar-returns
curl -X POST http://127.0.0.1:8000/api/lunar-returns/dev/purge \
  -H "X-Dev-External-Id: 550e8400-e29b-41d4-a716-446655440000"

curl -X GET http://127.0.0.1:8000/api/lunar-returns/current \
  -H "X-Dev-External-Id: 550e8400-e29b-41d4-a716-446655440000"

curl -X POST http://127.0.0.1:8000/api/lunar-returns/generate \
  -H "X-Dev-External-Id: 550e8400-e29b-41d4-a716-446655440000"

# Test natal-chart
curl -X POST http://127.0.0.1:8000/api/natal-chart \
  -H "X-Dev-External-Id: 550e8400-e29b-41d4-a716-446655440000" \
  -H "Content-Type: application/json" \
  -d '{
    "date": "1990-01-15",
    "time": "14:30",
    "latitude": 48.8566,
    "longitude": 2.3522,
    "place_name": "Paris, France"
  }'
```

---

## 📊 Résumé Final

### Fichiers Fixed
- ✅ **routes/lunar_returns.py** (10 endpoints + 2 helpers)

### Fichiers À Fixer
- ⚠️ **routes/natal.py** (2 endpoints, **fix CRITIQUE au DEV_MOCK_NATAL**)
- ⚠️ **routes/natal_interpretation.py** (à vérifier)
- ⚠️ **routes/lunar.py** (à scanner)

### Tests À Créer
- ⚠️ `tests/test_missinggreenlet_prevention.py` (3 tests minimum)

### Documentation Created
- ✅ [MISSINGGREENLET_FIX.md](MISSINGGREENLET_FIX.md) - Guide complet du pattern et fix original
- ✅ [MISSINGGREENLET_STATUS.md](MISSINGGREENLET_STATUS.md) - Status détaillé avec exemples de fix
- ✅ [MISSINGGREENLET_CHECKLIST.md](MISSINGGREENLET_CHECKLIST.md) - Ce fichier (checklist finale)

---

## 🎯 Prochaines Étapes Recommandées

### Priority 1: Fix natal.py (CRITIQUE)
Le bloc DEV_MOCK_NATAL modifie `current_user` après `db.add()`, ce qui va trigger MissingGreenlet au `commit()`.

**Action**: Appliquer le pattern "Charger User depuis DB" documenté ci-dessus.

### Priority 2: Vérifier natal_interpretation.py et lunar.py
Scanner ces fichiers et appliquer le pattern d'extraction au début.

### Priority 3: Créer tests pytest
Créer `tests/test_missinggreenlet_prevention.py` avec au moins 3 tests.

### Priority 4: Test complet
Tester tous les endpoints manuellement ou via scripts bash.

---

## ✅ Pattern de Référence (COPY-PASTE)

```python
@router.post("/endpoint")
async def my_endpoint(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Docstring"""

    # 🔒 CRITIQUE: Extraire IMMÉDIATEMENT pour éviter MissingGreenlet
    user_id = int(current_user.id)
    user_email = str(current_user.email) if hasattr(current_user, 'email') and current_user.email else f"dev+{user_id}@local.dev"

    # Utiliser user_id partout (JAMAIS current_user.id après ce point)
    result = await db.execute(
        select(Something).where(Something.user_id == user_id)
    )

    # Si besoin de modifier User, charger depuis DB
    if need_update_user:
        from models.user import User
        user_result = await db.execute(select(User).where(User.id == user_id))
        db_user = user_result.scalar_one_or_none()

        if db_user:
            db_user.some_field = new_value

    await db.commit()  # ✅ Safe, pas de lazy-load

    return {"user_id": user_id}  # ✅ Primitif
```

---

**Date**: 2026-01-02
**Status**: 1/4 files completely fixed, 3/4 files require manual verification/fixing
**Next**: Fix natal.py DEV_MOCK_NATAL block (CRITICAL)
