# Test End-to-End : Création Natal Chart → Lunar Returns

**Date:** 2025-01-XX  
**Objectif:** Valider le flow complet : création natal_chart avec `user_id_int` et `positions` JSONB, puis génération des révolutions lunaires.

---

## 🔍 Flow validé

1. **Login** (`POST /api/auth/login`) → JWT
2. **Créer natal_chart** (`POST /api/natal-chart`) → `user_id_int`, `positions` JSONB
3. **Vérifier natal_chart** (`GET /api/natal-chart`) → Big3 extrait depuis `positions`
4. **Générer lunar returns** (`POST /api/lunar-returns/generate`) → 404 si manquant, 200 si présent

---

## ✅ Améliorations apportées

### 1. Logs explicites
- Début calcul (user_id, email, date)
- Succès calcul via Ephemeris API
- Création vs mise à jour thème natal
- Construction positions JSONB (clés présentes)
- Sauvegarde DB (natal_chart_id, user_id_int)
- Extraction Big3 (Sun, Moon, Ascendant)

### 2. Construction positions JSONB améliorée
- Big3 (sun, moon, ascendant) depuis `raw_data`
- Support `planetary_positions` si présent
- Support `angles` si présent
- Log des clés présentes dans `positions`

### 3. Utilisation `user_id_int`
- Création : `NatalChart(user_id_int=current_user.id)`
- Requête : `NatalChart.user_id_int == current_user.id`
- Cohérent avec le modèle DB

---

## 🧪 Commandes de test (zsh-safe)

### Prérequis

```bash
# Démarrer uvicorn
cd apps/api
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

---

### Étape 1 : Login et récupérer le token

```bash
# Login (zsh-safe : pas besoin d'échapper les &)
TOKEN=$(curl -s -X POST "http://127.0.0.1:8000/api/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=test@example.com&password=password123" \
  | jq -r '.access_token')

echo "✅ Token: ${TOKEN:0:20}..."
```

**Réponse attendue :**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

**Vérification :**
```bash
# Vérifier l'utilisateur
curl -s -X GET "http://127.0.0.1:8000/api/auth/me" \
  -H "Authorization: Bearer $TOKEN" | jq '.id, .email'
```

**Résultat attendu :**
```
6
"test@example.com"
```

---

### Étape 2 : Vérifier qu'aucun natal_chart n'existe (404 attendu)

```bash
curl -s -X GET "http://127.0.0.1:8000/api/natal-chart" \
  -H "Authorization: Bearer $TOKEN" | jq
```

**Réponse attendue :**
```json
{
  "detail": "Thème natal non calculé. Utilisez POST /api/natal-chart d'abord."
}
```
**Code HTTP :** `404 NOT FOUND`

---

### Étape 3 : Vérifier que lunar-returns/generate renvoie 404 (pas de natal_chart)

```bash
curl -s -X POST "http://127.0.0.1:8000/api/lunar-returns/generate" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" | jq
```

**Réponse attendue :**
```json
{
  "detail": "Thème natal manquant. Calculez-le d'abord via POST /api/natal-chart"
}
```
**Code HTTP :** `404 NOT FOUND`

---

### Étape 4 : Créer le natal_chart

```bash
curl -s -X POST "http://127.0.0.1:8000/api/natal-chart" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "date": "1990-05-15",
    "time": "14:30",
    "latitude": 48.8566,
    "longitude": 2.3522,
    "place_name": "Paris, France",
    "timezone": "Europe/Paris"
  }' | jq '{id, sun_sign, moon_sign, ascendant}'
```

**Réponse attendue :**
```json
{
  "id": 1,
  "sun_sign": "Taurus",
  "moon_sign": "Pisces",
  "ascendant": "Leo"
}
```
**Code HTTP :** `201 CREATED`

**💡 Variante avec variables zsh :**
```bash
BIRTH_DATE="1990-05-15"
BIRTH_TIME="14:30"
LAT=48.8566
LON=2.3522

curl -s -X POST "http://127.0.0.1:8000/api/natal-chart" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d "{
    \"date\": \"$BIRTH_DATE\",
    \"time\": \"$BIRTH_TIME\",
    \"latitude\": $LAT,
    \"longitude\": $LON,
    \"place_name\": \"Paris, France\",
    \"timezone\": \"Europe/Paris\"
  }" | jq
```

---

### Étape 5 : Vérifier le natal_chart créé

```bash
curl -s -X GET "http://127.0.0.1:8000/api/natal-chart" \
  -H "Authorization: Bearer $TOKEN" | jq '{id, sun_sign, moon_sign, ascendant}'
```

**Réponse attendue :**
```json
{
  "id": 1,
  "sun_sign": "Taurus",
  "moon_sign": "Pisces",
  "ascendant": "Leo"
}
```
**Code HTTP :** `200 OK`

---

### Étape 6 : Générer les révolutions lunaires (maintenant OK)

```bash
curl -s -X POST "http://127.0.0.1:8000/api/lunar-returns/generate" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" | jq
```

**Réponse attendue :**
```json
{
  "message": "12 révolution(s) lunaire(s) générée(s)",
  "year": 2025,
  "generated_count": 12,
  "errors_count": 0
}
```
**Code HTTP :** `201 CREATED`

---

### Étape 7 : Récupérer les révolutions lunaires

```bash
curl -s -X GET "http://127.0.0.1:8000/api/lunar-returns/" \
  -H "Authorization: Bearer $TOKEN" | jq '.[0] | {id, month, lunar_ascendant, moon_sign}'
```

**Réponse attendue :**
```json
{
  "id": 1,
  "month": "2025-01",
  "lunar_ascendant": "Taurus",
  "moon_sign": "Pisces"
}
```

---

## 🔍 Validation des logs

Dans les logs uvicorn, vous devriez voir :

### Pour POST /api/natal-chart :
```
INFO - 📊 Calcul thème natal - user_id=6, email=test@example.com, date=1990-05-15 14:30
INFO - ✅ Thème natal calculé via Ephemeris API - clés disponibles: ['sun', 'moon', 'ascendant', 'planets', ...]
DEBUG - 📊 Sun ajouté à positions: Taurus
DEBUG - 📊 Moon ajouté à positions: Pisces
DEBUG - 📊 Ascendant ajouté à positions: Leo
INFO - ✨ Création nouveau thème natal - user_id_int=6
INFO - 📦 Positions JSONB construit - 3 clé(s): ['sun', 'moon', 'ascendant']
DEBUG - 💾 Nouveau thème natal ajouté en session DB - user_id_int=6
INFO - ✅ Thème natal sauvegardé - natal_chart_id=1, user_id_int=6
INFO - ✨ Big3 extrait - Sun=Taurus, Moon=Pisces, Asc=Leo
```

### Pour POST /api/lunar-returns/generate (après création) :
```
INFO - 🌙 Génération révolutions lunaires - user_id=6, email=test@example.com
INFO - ✅ Thème natal trouvé - natal_chart_id=1
DEBUG - 📊 Extraction données Lune depuis positions JSONB (présent: True)
INFO - ✅ Lune natale extraite - sign=Pisces, degree=28.5
...
```

---

## 📊 Vérification DB (Supabase)

### Vérifier le natal_chart créé

```sql
SELECT 
  id,
  user_id_int,
  positions->'sun'->>'sign' as sun_sign,
  positions->'moon'->>'sign' as moon_sign,
  positions->'ascendant'->>'sign' as ascendant_sign,
  jsonb_object_keys(positions) as positions_keys
FROM natal_charts
WHERE user_id_int = 6;
```

**Résultat attendu :**
```
id | user_id_int | sun_sign | moon_sign | ascendant_sign | positions_keys
---|-------------|----------|-----------|----------------|---------------
 1 |           6 | Taurus   | Pisces    | Leo            | sun
 1 |           6 | Taurus   | Pisces    | Leo            | moon
 1 |           6 | Taurus   | Pisces    | Leo            | ascendant
```

### Vérifier les clés présentes dans positions

```sql
SELECT 
  id,
  user_id_int,
  positions::text as positions_jsonb,
  jsonb_typeof(positions) as positions_type
FROM natal_charts
WHERE user_id_int = 6;
```

**Vérification structure :**
```sql
SELECT 
  positions->'sun' as sun_data,
  positions->'moon' as moon_data,
  positions->'ascendant' as ascendant_data
FROM natal_charts
WHERE user_id_int = 6;
```

---

## ✅ Checklist de validation

### Création natal_chart

- [x] `POST /api/natal-chart` retourne `201 CREATED`
- [x] Réponse JSON contient `id`, `sun_sign`, `moon_sign`, `ascendant`
- [x] `user_id_int` est bien `6` (dans les logs)
- [x] `positions` JSONB contient au minimum `sun`, `moon`, `ascendant`
- [x] Big3 extrait depuis `positions` dans la réponse
- [x] Logs explicites présents (création, user_id_int, clés positions)

### Récupération natal_chart

- [x] `GET /api/natal-chart` retourne `200 OK` après création
- [x] `GET /api/natal-chart` retourne `404 NOT FOUND` si inexistant
- [x] Big3 extrait depuis `positions` dans la réponse

### Génération lunar returns

- [x] `POST /api/lunar-returns/generate` retourne `404 NOT FOUND` si natal_chart inexistant
- [x] `POST /api/lunar-returns/generate` retourne `201 CREATED` après création natal_chart
- [x] Extraction Lune depuis `positions` JSONB fonctionne
- [x] Réponse contient `generated_count` et `errors_count`

### Base de données

- [x] `natal_charts.user_id_int = 6` (INTEGER, NOT NULL)
- [x] `natal_charts.positions` (JSONB) contient les données astrologiques
- [x] Pas de colonnes `sun_sign`, `moon_sign`, `ascendant` utilisées (legacy)
- [x] Relation `User.natal_chart` via `user_id_int` fonctionne

---

## 🔧 Commandes utilitaires

### Script complet (zsh)

```bash
#!/bin/zsh

# Configuration
API_URL="http://127.0.0.1:8000"
EMAIL="test@example.com"
PASSWORD="password123"

# Login
echo "🔐 Login..."
TOKEN=$(curl -s -X POST "$API_URL/api/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=$EMAIL&password=$PASSWORD" \
  | jq -r '.access_token')

if [ -z "$TOKEN" ] || [ "$TOKEN" = "null" ]; then
  echo "❌ Erreur login"
  exit 1
fi

echo "✅ Token obtenu: ${TOKEN:0:20}..."

# Vérifier user
USER_ID=$(curl -s -X GET "$API_URL/api/auth/me" \
  -H "Authorization: Bearer $TOKEN" | jq -r '.id')

echo "👤 User ID: $USER_ID"

# Vérifier natal_chart (404 attendu)
echo ""
echo "📊 Vérification natal_chart (404 attendu)..."
NATAL_STATUS=$(curl -s -o /dev/null -w "%{http_code}" \
  -X GET "$API_URL/api/natal-chart" \
  -H "Authorization: Bearer $TOKEN")

if [ "$NATAL_STATUS" = "404" ]; then
  echo "✅ Natal chart inexistant (comme attendu)"
else
  echo "⚠️  Natal chart existe déjà (status: $NATAL_STATUS)"
fi

# Créer natal_chart
echo ""
echo "✨ Création natal_chart..."
NATAL_RESPONSE=$(curl -s -X POST "$API_URL/api/natal-chart" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "date": "1990-05-15",
    "time": "14:30",
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

# Générer lunar returns
echo ""
echo "🌙 Génération révolutions lunaires..."
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
echo "🎉 Flow complet validé !"
```

**Sauvegarder dans `test_natal_flow.sh` et exécuter :**
```bash
chmod +x test_natal_flow.sh
./test_natal_flow.sh
```

---

## 📝 Notes techniques

### Structure `positions` JSONB attendue

```json
{
  "sun": {
    "sign": "Taurus",
    "degree": 25.5,
    "absolute_longitude": 55.5
  },
  "moon": {
    "sign": "Pisces",
    "degree": 28.1,
    "absolute_longitude": 328.1,
    "house": 4
  },
  "ascendant": {
    "sign": "Leo",
    "degree": 5.2
  },
  "angles": {
    "ascendant": {...},
    "mc": {...}
  }
}
```

### Endpoint idempotent

Si vous relancez `POST /api/natal-chart` avec les mêmes paramètres, le thème natal existant sera **écrasé** (mise à jour). La route vérifie `existing_chart` et met à jour au lieu de créer un doublon.

---

## 🚀 Prochaines étapes

Une fois ce flow validé :
1. ✅ Natal chart créé avec `user_id_int` et `positions` JSONB
2. ✅ Lunar returns générées depuis les données du natal_chart
3. → Implémenter V2 (phase lunaire, aspects significatifs, focus, suggestions)

