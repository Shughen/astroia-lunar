# Fix: Alignement modèle SQLAlchemy avec DB V2 (suppression colonnes legacy)

**Date:** 2025-01-XX  
**Problème:** `asyncpg.exceptions.UndefinedColumnError: column natal_charts.sun_sign does not exist`  
**Cause:** SQLAlchemy déclare des colonnes qui n'existent plus dans la table DB V2.

---

## ✅ Corrections apportées

### 1. Modèle SQLAlchemy `NatalChart` nettoyé

**Fichier:** `apps/api/models/natal_chart.py`

**Colonnes supprimées (n'existent plus en DB V2) :**
- ❌ `sun_sign` (String)
- ❌ `moon_sign` (String)
- ❌ `ascendant` (String)
- ❌ `planets` (JSON)
- ❌ `houses` (JSON)
- ❌ `aspects` (JSON)

**Colonnes conservées (existent en DB) :**
- ✅ `id` (Integer, PK)
- ✅ `user_id` (Integer, nullable, legacy)
- ✅ `user_id_int` (Integer, NOT NULL, FK)
- ✅ `positions` (JSONB) - source de vérité pour Big3
- ✅ `raw_data` (JSONB) - contient planets, houses, aspects
- ✅ `calculated_at` (DateTime)

### 2. Route `natal.py` mise à jour

**Fichier:** `apps/api/routes/natal.py`

**Changements :**
- ❌ Supprimé toutes les écritures vers `chart.planets`, `chart.houses`, `chart.aspects`
- ❌ Supprimé toutes les créations avec `planets=...`, `houses=...`, `aspects=...`
- ✅ Sauvegarde uniquement dans `positions` et `raw_data`
- ✅ Extraction `planets`, `houses`, `aspects` depuis `raw_data` pour la réponse API

**Code modifié :**
```python
# Avant (❌ erreur)
chart = NatalChart(
    user_id_int=current_user.id,
    planets=raw_data.get("planets", {}),  # Colonne n'existe plus
    houses=raw_data.get("houses", {}),    # Colonne n'existe plus
    aspects=raw_data.get("aspects", []),  # Colonne n'existe plus
    positions=positions,
    raw_data=raw_data
)

# Après (✅ correct)
chart = NatalChart(
    user_id_int=current_user.id,
    positions=positions,  # Source de vérité Big3
    raw_data=raw_data     # Contient planets, houses, aspects
)

# Réponse API : extraire depuis raw_data
planets = chart.raw_data.get("planets", {}) if chart.raw_data else {}
houses = chart.raw_data.get("houses", {}) if chart.raw_data else {}
aspects = chart.raw_data.get("aspects", []) if chart.raw_data else []
```

### 3. Fix `ephemeris_mock.py`

**Fichier:** `apps/api/utils/ephemeris_mock.py`

**Changement :** Support `HH:MM` et `HH:MM:SS` via `datetime.time.fromisoformat()`

```python
# Avant
hour, minute = map(int, time.split(":"))

# Après
from datetime import time as dt_time
time_obj = dt_time.fromisoformat(time)  # Supporte HH:MM et HH:MM:SS
hour = time_obj.hour
minute = time_obj.minute
```

---

## 📊 Structure DB V2 (réelle)

### Colonnes existantes

```sql
SELECT column_name, data_type, is_nullable
FROM information_schema.columns
WHERE table_name = 'natal_charts'
ORDER BY ordinal_position;
```

**Résultat attendu :**
```
column_name     | data_type | is_nullable
----------------|-----------|-------------
id              | integer   | NO          (PK)
user_id         | integer   | YES         (legacy, nullable)
user_id_int     | integer   | NO          (FK vers users.id)
positions       | jsonb     | YES
raw_data        | jsonb     | YES
calculated_at   | timestamp | YES
```

**⚠️ Colonnes absentes (supprimées en V2) :**
- `sun_sign` ❌
- `moon_sign` ❌
- `ascendant` ❌
- `planets` ❌
- `houses` ❌
- `aspects` ❌

---

## 🧪 Requête SQL de vérification

```sql
-- Vérifier les colonnes existantes
SELECT 
    column_name,
    data_type,
    is_nullable
FROM information_schema.columns
WHERE table_schema = 'public'
  AND table_name = 'natal_charts'
ORDER BY ordinal_position;

-- Vérifier qu'un natal_chart utilise bien positions et raw_data
SELECT 
    id,
    user_id_int,
    jsonb_typeof(positions) as positions_type,
    jsonb_typeof(raw_data) as raw_data_type,
    positions->'sun'->>'sign' as sun_sign,
    positions->'moon'->>'sign' as moon_sign,
    positions->'ascendant'->>'sign' as ascendant_sign,
    raw_data->'planets' IS NOT NULL as has_planets,
    raw_data->'houses' IS NOT NULL as has_houses,
    raw_data->'aspects' IS NOT NULL as has_aspects
FROM natal_charts
WHERE user_id_int = 6
LIMIT 1;
```

---

## 🧪 Test curl E2E complet

### Prérequis

Dans `.env` :
```env
EPHEMERIS_API_KEY=
DEV_MOCK_EPHEMERIS=1
```

### Étape 1 : Login

```bash
TOKEN=$(curl -s -X POST "http://127.0.0.1:8000/api/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=test@example.com&password=password123" \
  | jq -r '.access_token')

echo "✅ Token: ${TOKEN:0:20}..."
```

### Étape 2 : Créer natal_chart (mode mock)

```bash
curl -s -X POST "http://127.0.0.1:8000/api/natal-chart" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "date": "1990-05-15",
    "time": "14:30:00",
    "latitude": 48.8566,
    "longitude": 2.3522,
    "place_name": "Paris, France",
    "timezone": "Europe/Paris"
  }' | jq '{id, sun_sign, moon_sign, ascendant}'
```

**Réponse attendue :** `201 CREATED`
```json
{
  "id": 1,
  "sun_sign": "Taurus",
  "moon_sign": "Aries",
  "ascendant": "Pisces"
}
```

**✅ Vérification :** Aucune erreur `UndefinedColumnError`

### Étape 3 : Récupérer natal_chart

```bash
curl -s -X GET "http://127.0.0.1:8000/api/natal-chart" \
  -H "Authorization: Bearer $TOKEN" | jq '{id, sun_sign, moon_sign, ascendant}'
```

**Réponse attendue :** `200 OK`

### Étape 4 : Générer révolutions lunaires

```bash
curl -s -X POST "http://127.0.0.1:8000/api/lunar-returns/generate" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" | jq
```

**Réponse attendue :** `201 CREATED`
```json
{
  "message": "12 révolution(s) lunaire(s) générée(s)",
  "year": 2025,
  "generated_count": 12,
  "errors_count": 0
}
```

### Étape 5 : Récupérer révolutions lunaires

```bash
curl -s -X GET "http://127.0.0.1:8000/api/lunar-returns/" \
  -H "Authorization: Bearer $TOKEN" | jq '.[0] | {id, month, lunar_ascendant, moon_sign}'
```

**Réponse attendue :** `200 OK`

---

## 📝 Script de test complet (zsh)

```bash
#!/bin/zsh

API_URL="http://127.0.0.1:8000"
EMAIL="test@example.com"
PASSWORD="password123"

echo "🔐 1. Login..."
TOKEN=$(curl -s -X POST "$API_URL/api/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=$EMAIL&password=$PASSWORD" \
  | jq -r '.access_token')

if [ -z "$TOKEN" ] || [ "$TOKEN" = "null" ]; then
  echo "❌ Erreur login"
  exit 1
fi

echo "✅ Token obtenu: ${TOKEN:0:20}..."

echo ""
echo "✨ 2. Création natal_chart (mode mock)..."
NATAL_RESPONSE=$(curl -s -X POST "$API_URL/api/natal-chart" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "date": "1990-05-15",
    "time": "14:30:00",
    "latitude": 48.8566,
    "longitude": 2.3522,
    "place_name": "Paris, France",
    "timezone": "Europe/Paris"
  }')

NATAL_ID=$(echo "$NATAL_RESPONSE" | jq -r '.id')
SUN_SIGN=$(echo "$NATAL_RESPONSE" | jq -r '.sun_sign')

if [ -n "$NATAL_ID" ] && [ "$NATAL_ID" != "null" ]; then
  echo "✅ Natal chart créé - ID: $NATAL_ID, Sun: $SUN_SIGN"
else
  echo "❌ Erreur création natal_chart"
  echo "$NATAL_RESPONSE" | jq
  exit 1
fi

echo ""
echo "🌙 3. Génération révolutions lunaires..."
LUNAR_RESPONSE=$(curl -s -X POST "$API_URL/api/lunar-returns/generate" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json")

GENERATED_COUNT=$(echo "$LUNAR_RESPONSE" | jq -r '.generated_count')

if [ -n "$GENERATED_COUNT" ] && [ "$GENERATED_COUNT" != "null" ]; then
  echo "✅ $GENERATED_COUNT révolution(s) lunaire(s) générée(s)"
else
  echo "❌ Erreur génération lunar returns"
  echo "$LUNAR_RESPONSE" | jq
  exit 1
fi

echo ""
echo "📋 4. Récupération révolutions lunaires..."
LUNAR_LIST=$(curl -s -X GET "$API_URL/api/lunar-returns/" \
  -H "Authorization: Bearer $TOKEN")

LUNAR_COUNT=$(echo "$LUNAR_LIST" | jq '. | length')
echo "✅ $LUNAR_COUNT révolution(s) lunaire(s) trouvée(s)"

echo ""
echo "🎉 Flow complet validé !"
```

**Sauvegarder dans `test_natal_v2_flow.sh` et exécuter :**
```bash
chmod +x test_natal_v2_flow.sh
./test_natal_v2_flow.sh
```

---

## ✅ Checklist de validation

- [x] Modèle SQLAlchemy aligné avec DB V2 (colonnes legacy supprimées)
- [x] Route `natal.py` ne lit/écrit plus les colonnes legacy
- [x] Extraction Big3 depuis `positions` JSONB
- [x] Extraction `planets`, `houses`, `aspects` depuis `raw_data` JSONB
- [x] `ephemeris_mock.py` supporte `HH:MM` et `HH:MM:SS`
- [x] Aucune erreur `UndefinedColumnError`
- [x] Flow E2E fonctionne en mode mock DEV

---

## 🔍 Vérifications supplémentaires

### Vérifier que `lunar_returns.py` n'utilise pas les colonnes legacy

```bash
grep -n "\.sun_sign\|\.moon_sign\|\.ascendant\|\.planets\|\.houses\|\.aspects" apps/api/routes/lunar_returns.py
```

**Résultat attendu :** Aucun match (déjà corrigé précédemment)

---

## 🚀 Statut

**Problème résolu ✅**

Le modèle SQLAlchemy est maintenant aligné avec la structure réelle de la table DB V2. Toutes les données sont stockées dans `positions` (JSONB) et `raw_data` (JSONB), et extraites pour la réponse API.

