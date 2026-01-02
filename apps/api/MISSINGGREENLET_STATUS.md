# MissingGreenlet Fix - Status Report

## ✅ Completed Files

### 1. routes/lunar_returns.py
**Status**: ✅ COMPLET

**Endpoints Fixed**:
- `POST /generate` - Extraction user_id + birth coords au début
- `GET /` - Extraction user_id au début
- `GET /current` - Extraction user_id au début (déjà fait)
- `GET /current/report` - Extraction user_id au début
- `GET /{lunar_return_id}/report` - Extraction user_id au début
- `GET /next` - Extraction user_id au début
- `GET /rolling` - Extraction user_id au début
- `GET /year/{year}` - Extraction user_id au début
- `GET /{month}` - Extraction user_id au début
- `POST /dev/purge` - Extraction user_id + email + external_id au début

**Helpers Fixed**:
- `_generate_rolling_returns` - Signature changée pour accepter `user_id: int` au lieu de `current_user: User`
- `_generate_rolling_if_empty` - Extraction `user_id = int(current_user.id)` au début

**Pattern Applied**:
```python
# 🔒 CRITIQUE: Extraire user_id IMMÉDIATEMENT pour éviter MissingGreenlet
user_id = int(current_user.id)

# Tous les queries utilisent user_id au lieu de current_user.id
result = await db.execute(
    select(LunarReturn).where(LunarReturn.user_id == user_id)
)
```

---

## ⚠️ Files À Vérifier

### 2. routes/natal.py
**Status**: ⚠️ À FIXER MANUELLEMENT

**Problèmes Identifiés**:

#### Ligne 107-137: Idempotence check
```python
# ❌ PROBLÈME: current_user.id, .birth_date, .birth_time, etc. utilisés AVANT commit
result = await db.execute(
    select(NatalChart).where(NatalChart.user_id == current_user.id)  # ❌
)
existing_chart = result.scalar_one_or_none()

if existing_chart:
    existing_date_str = current_user.birth_date  # ❌ Peut être accessed après await
    existing_time_str = current_user.birth_time  # ❌
    existing_lat = float(current_user.birth_latitude)  # ❌
    existing_lon = float(current_user.birth_longitude)  # ❌
    same_timezone = getattr(current_user, 'birth_timezone', None) == detected_timezone  # ❌
```

**Fix Required**:
```python
@router.post("/natal-chart")
async def calculate_natal_chart(
    data: NatalChartRequest,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """..."""

    # 🔒 CRITIQUE: Extraire TOUTES les primitives IMMÉDIATEMENT
    user_id = int(current_user.id)
    user_email = str(current_user.email) if hasattr(current_user, 'email') and current_user.email else f"dev+{user_id}@local.dev"
    birth_date_existing = str(current_user.birth_date) if hasattr(current_user, 'birth_date') and current_user.birth_date else None
    birth_time_existing = str(current_user.birth_time) if hasattr(current_user, 'birth_time') and current_user.birth_time else None
    birth_latitude_existing = current_user.birth_latitude if hasattr(current_user, 'birth_latitude') else None
    birth_longitude_existing = current_user.birth_longitude if hasattr(current_user, 'birth_longitude') else None
    birth_place_name_existing = str(current_user.birth_place_name) if hasattr(current_user, 'birth_place_name') and current_user.birth_place_name else None
    birth_timezone_existing = str(current_user.birth_timezone) if hasattr(current_user, 'birth_timezone') and current_user.birth_timezone else None

    # Puis utiliser ces primitives partout:
    # - user_id au lieu de current_user.id
    # - birth_date_existing au lieu de current_user.birth_date
    # - birth_time_existing au lieu de current_user.birth_time
    # - etc.
```

#### Ligne 196-197: Logging avec current_user.id
```python
# ❌ PROBLÈME
user_email = getattr(current_user, "email", f"dev+{current_user.id}@local.dev")  # ❌
logger.info(f"... user_id={current_user.id}, email={user_email}")  # ❌
```

**Fix**: Utiliser `user_id` et `user_email` extraits.

#### Ligne 240-266: DEV_MOCK_NATAL - Modification de current_user APRÈS commit
```python
# ❌ PROBLÈME CRITIQUE: Modification d'attributs ORM APRÈS commit
chart = NatalChart(user_id=current_user.id, ...)  # ❌
db.add(chart)

# Mettre à jour les infos de naissance du user
current_user.birth_date = data.date  # ❌ APRÈS db.add() et avant commit()
current_user.birth_time = birth_time  # ❌
current_user.birth_latitude = str(data.latitude)  # ❌
current_user.birth_longitude = str(data.longitude)  # ❌
current_user.birth_place_name = data.place_name  # ❌
current_user.birth_timezone = detected_timezone  # ❌

await db.commit()  # ❌ Commit va trigger MissingGreenlet si current_user lazy-load
```

**Fix**: Charger le vrai User object depuis DB et modifier celui-là:
```python
# Au début de l'endpoint
user_id = int(current_user.id)

# Dans le bloc DEV_MOCK_NATAL
chart = NatalChart(user_id=user_id, ...)  # ✅
db.add(chart)

# Charger le vrai User pour update
from models.user import User
user_result = await db.execute(select(User).where(User.id == user_id))
db_user = user_result.scalar_one_or_none()

if db_user:
    db_user.birth_date = data.date  # ✅
    db_user.birth_time = birth_time  # ✅
    db_user.birth_latitude = str(data.latitude)  # ✅
    db_user.birth_longitude = str(data.longitude)  # ✅
    db_user.birth_place_name = data.place_name  # ✅
    db_user.birth_timezone = detected_timezone  # ✅

await db.commit()  # ✅
```

#### Autres occurrences
**Lignes à fixer**: 558, 569 (même pattern dans update_natal_chart)

---

### 3. routes/natal_interpretation.py
**Status**: ⚠️ À VÉRIFIER

**Occurrences trouvées**: Ligne 53 déjà a `user_id = current_user.id`

**Action**: Vérifier que ce pattern est bien utilisé partout dans le fichier, et que `user_id` est extrait AU DÉBUT de chaque endpoint, PAS au milieu.

---

### 4. routes/lunar.py
**Status**: ⚠️ À VÉRIFIER

**Action**: Scanner le fichier et appliquer le même pattern que lunar_returns.py.

---

## 🎯 Plan d'Action

### Étape 1: Fixer natal.py manuellement
1. Ajouter extraction de primitives au début de `calculate_natal_chart()`
2. Remplacer tous les `current_user.id` par `user_id`
3. Remplacer tous les `current_user.birth_*` par `birth_*_existing`
4. Fixer le bloc DEV_MOCK_NATAL pour charger User depuis DB avant modification
5. Même chose pour `update_natal_chart()` si existe

### Étape 2: Fixer natal_interpretation.py
1. Vérifier que `user_id = int(current_user.id)` est AU DÉBUT de chaque endpoint
2. Remplacer tous les `current_user.id` par `user_id`

### Étape 3: Fixer lunar.py
1. Même pattern que lunar_returns.py
2. Extraction au début de chaque endpoint

### Étape 4: Tests
Créer pytest pour au moins 2 endpoints:
```python
# tests/test_missinggreenlet_prevention.py

async def test_natal_chart_no_missinggreenlet_after_purge():
    """Vérifie que POST /natal-chart ne trigger pas MissingGreenlet après purge"""
    # 1. Purge
    # 2. POST /natal-chart
    # 3. Vérifier 200/201 (pas 500)

async def test_lunar_returns_generate_no_missinggreenlet():
    """Vérifie que POST /lunar-returns/generate ne trigger pas MissingGreenlet"""
    # 1. Purge
    # 2. POST /generate
    # 3. Vérifier 201 (pas 500)
```

### Étape 5: Checklist final
Générer une checklist de tous les endpoints:

```
✅ /api/lunar-returns/generate
✅ /api/lunar-returns/current
✅ /api/lunar-returns/next
✅ /api/lunar-returns/rolling
✅ /api/lunar-returns/dev/purge
⚠️  /api/natal-chart
⚠️  /api/natal/interpretation
⚠️  /api/lunar/*
```

---

## 📋 Pattern à Suivre (DO/DON'T)

### ✅ DO - Extraction immédiate
```python
@router.post("/endpoint")
async def my_endpoint(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Docstring"""

    # 🔒 CRITIQUE: Extraire IMMÉDIATEMENT
    user_id = int(current_user.id)
    user_email = str(current_user.email) if hasattr(current_user, 'email') and current_user.email else None

    # Utiliser user_id partout
    result = await db.execute(
        select(Something).where(Something.user_id == user_id)
    )

    await db.commit()  # ✅ Safe, pas de lazy-load

    return {"user_id": user_id}  # ✅ Primitif
```

### ❌ DON'T - Accès après commit
```python
@router.post("/endpoint")
async def my_endpoint(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Docstring"""

    result = await db.execute(
        select(Something).where(Something.user_id == current_user.id)  # ⚠️ OK ICI
    )

    await db.commit()

    logger.info(f"user_id={current_user.id}")  # ❌ MissingGreenlet après commit!
    return {"user_id": current_user.id}  # ❌ MissingGreenlet après commit!
```

### ❌ DON'T - Modification d'ORM object avant commit
```python
current_user.birth_date = "2000-01-01"  # ❌ Si current_user est detached/expired
await db.commit()  # ❌ MissingGreenlet
```

### ✅ DO - Charger User depuis DB pour modification
```python
user_id = int(current_user.id)  # ✅ Extract immédiatement

# Charger le vrai User
user_result = await db.execute(select(User).where(User.id == user_id))
db_user = user_result.scalar_one_or_none()

if db_user:
    db_user.birth_date = "2000-01-01"  # ✅ Objet attaché
    await db.commit()  # ✅ Safe
```

---

## 🧪 Tests de Non-Régression

### Test 1: /api/lunar-returns/current après purge
```bash
#!/bin/bash
curl -X POST http://127.0.0.1:8000/api/lunar-returns/dev/purge \
  -H "X-Dev-External-Id: 550e8400-e29b-41d4-a716-446655440000"

curl -X GET http://127.0.0.1:8000/api/lunar-returns/current \
  -H "X-Dev-External-Id: 550e8400-e29b-41d4-a716-446655440000"

# Expected: 200 avec null OU 200 avec data (pas 500)
```

### Test 2: /api/natal-chart avec DEV_MOCK_NATAL=1
```bash
#!/bin/bash
source .env  # DEV_MOCK_NATAL=1

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

# Expected: 200/201 (pas 500)
```

---

## 📊 Résumé

- **Fichiers Fixed**: 1/4 (lunar_returns.py ✅)
- **Fichiers À Fixer**: 3/4 (natal.py ⚠️, natal_interpretation.py ⚠️, lunar.py ⚠️)
- **Pattern Appliqué**: Extraction immédiate de primitives au début de chaque endpoint
- **Tests**: À créer (pytest + scripts bash)
- **Documentation**: MISSINGGREENLET_FIX.md (déjà créé), ce fichier STATUS

**Prochaine Étape**: Fixer natal.py manuellement en appliquant le pattern ci-dessus.
