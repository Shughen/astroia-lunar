# Test End-to-End : Lunar Revolution V2 Flow

**Date:** 2025-01-XX  
**Objectif:** Valider le flow complet de génération de révolutions lunaires avec JWT, natal_chart, extraction Big3, et calcul.

---

## 🔍 Flow validé

1. **Authentification JWT** (`POST /api/auth/login`)
2. **Récupération utilisateur** (`current_user` depuis JWT)
3. **Récupération natal_chart** (`NatalChart.user_id_int == current_user.id`)
4. **Extraction Big3** depuis `positions` JSONB
5. **Génération Lunar Return** (12 mois)
6. **Réponse JSON** typée

---

## ✅ Améliorations apportées

### 1. Codes HTTP normalisés
- `404 NOT FOUND` : natal_chart manquant (au lieu de 400)
- `422 UNPROCESSABLE_ENTITY` : données incohérentes (coordonnées, Lune manquante)
- `401 UNAUTHORIZED` : JWT invalide/manquant (via `get_current_user`)

### 2. Logging explicite
Chaque étape clé est loggée avec contexte :
- Début de génération (user_id, email)
- Thème natal trouvé/manquant
- Extraction données Lune (succès/échec)
- Calcul par mois (succès/erreur)
- Commit DB (compteurs)

### 3. Gestion d'erreurs robuste
- Extraction Big3 avec fallback legacy
- Continuation du processus même si un mois échoue
- Compteurs d'erreurs dans la réponse

### 4. Extraction Big3 robuste
- Gère `positions["moon"]["sign"]` ou `positions["Moon"]["sign"]`
- Fallback sur `positions["moon"]["zodiac_sign"]`
- Supporte `positions["angles"]["ascendant"]["sign"]`
- Fallback sur `planets` legacy si `positions` vide

---

## 🧪 Commandes de test

### Prérequis

1. **Démarrer uvicorn** :
```bash
cd apps/api
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

2. **Variables d'environnement** (`.env`):
```bash
DATABASE_URL=postgresql://postgres:password@localhost:5432/astroia_lunar
EPHEMERIS_API_KEY=your_key_here
SECRET_KEY=your_secret_key_here
```

---

### Étape 1 : Créer un utilisateur (ou utiliser un existant)

```bash
# Register
curl -X POST http://127.0.0.1:8000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "password123",
    "birth_date": "1990-05-15",
    "birth_time": "14:30",
    "birth_latitude": 48.8566,
    "birth_longitude": 2.3522,
    "birth_place_name": "Paris, France"
  }'
```

**Réponse attendue :**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

---

### Étape 2 : Login (si utilisateur existe déjà)

```bash
curl -X POST http://127.0.0.1:8000/api/auth/login \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=test@example.com&password=password123"
```

**Réponse attendue :**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

**💡 Astuce :** Stocker le token dans une variable :
```bash
TOKEN=$(curl -s -X POST http://127.0.0.1:8000/api/auth/login \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=test@example.com&password=password123" \
  | jq -r '.access_token')

echo "Token: $TOKEN"
```

---

### Étape 3 : Vérifier l'utilisateur connecté

```bash
curl -X GET http://127.0.0.1:8000/api/auth/me \
  -H "Authorization: Bearer $TOKEN"
```

**Réponse attendue :**
```json
{
  "id": 1,
  "email": "test@example.com",
  "birth_date": "1990-05-15",
  "birth_time": "14:30",
  "birth_place_name": "Paris, France",
  "is_premium": false,
  "created_at": "2025-01-XX..."
}
```

---

### Étape 4 : Créer le thème natal (si pas encore créé)

```bash
curl -X POST http://127.0.0.1:8000/api/natal-chart \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "birth_date": "1990-05-15",
    "birth_time": "14:30",
    "birth_latitude": 48.8566,
    "birth_longitude": 2.3522,
    "timezone": "Europe/Paris"
  }'
```

**Réponse attendue :**
```json
{
  "id": 1,
  "sun_sign": "Taurus",
  "moon_sign": "Pisces",
  "ascendant": "Leo",
  "planets": {...},
  "houses": {...},
  "aspects": [...]
}
```

**⚠️ Important :** Le thème natal doit être créé **avant** de générer les révolutions lunaires.

---

### Étape 5 : Générer les révolutions lunaires

```bash
curl -X POST http://127.0.0.1:8000/api/lunar-returns/generate \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
```

**Réponse attendue (succès) :**
```json
{
  "message": "12 révolution(s) lunaire(s) générée(s)",
  "year": 2025,
  "generated_count": 12,
  "errors_count": 0
}
```

**Réponse attendue (si certaines erreurs) :**
```json
{
  "message": "10 révolution(s) lunaire(s) générée(s)",
  "year": 2025,
  "generated_count": 10,
  "errors_count": 2
}
```

**Codes d'erreur possibles :**
- `401 UNAUTHORIZED` : Token invalide/manquant
- `404 NOT FOUND` : Thème natal manquant
- `422 UNPROCESSABLE_ENTITY` : Coordonnées de naissance manquantes ou données Lune incomplètes

---

### Étape 6 : Récupérer toutes les révolutions lunaires

```bash
curl -X GET http://127.0.0.1:8000/api/lunar-returns/ \
  -H "Authorization: Bearer $TOKEN"
```

**Réponse attendue :**
```json
[
  {
    "id": 1,
    "month": "2025-01",
    "return_date": "2025-01-15T14:32:00",
    "lunar_ascendant": "Taurus",
    "moon_house": 4,
    "moon_sign": "Pisces",
    "aspects": [...],
    "interpretation": "..."
  },
  ...
]
```

---

### Étape 7 : Récupérer une révolution lunaire spécifique

```bash
curl -X GET http://127.0.0.1:8000/api/lunar-returns/2025-01 \
  -H "Authorization: Bearer $TOKEN"
```

**Réponse attendue :**
```json
{
  "id": 1,
  "month": "2025-01",
  "return_date": "2025-01-15T14:32:00",
  "lunar_ascendant": "Taurus",
  "moon_house": 4,
  "moon_sign": "Pisces",
  "aspects": [...],
  "interpretation": "..."
}
```

---

## 🔍 Validation des logs

Dans les logs uvicorn, vous devriez voir :

```
INFO - 🌙 Génération révolutions lunaires - user_id=1, email=test@example.com
INFO - ✅ Thème natal trouvé - natal_chart_id=1
DEBUG - 📊 Extraction données Lune depuis positions JSONB (présent: True)
INFO - ✅ Lune natale extraite - sign=Pisces, degree=28.5
INFO - 📅 Génération pour 12 mois de l'année 2025
INFO - 🔄 Calcul révolution lunaire 2025-01...
INFO - ✅ Calcul réussi pour 2025-01
...
INFO - ✅ Commit DB - 12 révolution(s) générée(s), 0 erreur(s)
```

---

## 🧪 Tests de cas d'erreur

### Test 1 : Natal chart manquant

```bash
# Supprimer le natal_chart en DB (via SQL ou interface)
# Puis appeler generate

curl -X POST http://127.0.0.1:8000/api/lunar-returns/generate \
  -H "Authorization: Bearer $TOKEN"
```

**Réponse attendue :**
```json
{
  "detail": "Thème natal manquant. Calculez-le d'abord via POST /api/natal-chart"
}
```
**Code HTTP :** `404 NOT FOUND`

---

### Test 2 : Token invalide

```bash
curl -X POST http://127.0.0.1:8000/api/lunar-returns/generate \
  -H "Authorization: Bearer invalid_token"
```

**Réponse attendue :**
```json
{
  "detail": "Impossible de valider les identifiants"
}
```
**Code HTTP :** `401 UNAUTHORIZED`

---

### Test 3 : Coordonnées manquantes

```bash
# Modifier user en DB pour mettre birth_latitude/birth_longitude à NULL
# Puis appeler generate

curl -X POST http://127.0.0.1:8000/api/lunar-returns/generate \
  -H "Authorization: Bearer $TOKEN"
```

**Réponse attendue :**
```json
{
  "detail": "Coordonnées de naissance manquantes dans le profil utilisateur"
}
```
**Code HTTP :** `422 UNPROCESSABLE_ENTITY`

---

## 📊 Vérification DB (Supabase)

### Vérifier le natal_chart

```sql
SELECT 
  id,
  user_id_int,
  positions->'moon'->>'sign' as moon_sign,
  positions->'sun'->>'sign' as sun_sign,
  positions->'ascendant'->>'sign' as ascendant_sign
FROM natal_charts
WHERE user_id_int = 1;
```

### Vérifier les révolutions lunaires générées

```sql
SELECT 
  id,
  user_id,
  month,
  lunar_ascendant,
  moon_house,
  moon_sign,
  created_at
FROM lunar_returns
WHERE user_id = 1
ORDER BY month;
```

---

## ✅ Checklist de validation

- [x] JWT authentification fonctionne
- [x] `current_user.id` (INTEGER) est correctement résolu depuis JWT
- [x] `NatalChart.user_id_int` est utilisé pour la requête (pas `user_id` legacy)
- [x] Extraction Big3 depuis `positions` JSONB fonctionne
- [x] Fallback sur `planets` legacy si `positions` vide
- [x] Codes HTTP normalisés (404, 422, 401)
- [x] Logs explicites à chaque étape
- [x] Gestion d'erreurs robuste (continue même si un mois échoue)
- [x] Réponse JSON typée avec compteurs
- [x] Endpoint idempotent (skip si déjà calculé)

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
  }
}
```

**Alternative (angles) :**
```json
{
  "angles": {
    "ascendant": {
      "sign": "Leo",
      "degree": 5.2
    }
  }
}
```

### Endpoint idempotent

Si vous relancez `/api/lunar-returns/generate` avec le même utilisateur, les révolutions déjà calculées sont **skippées** (pas de doublons). Seules les nouvelles sont générées.

---

## 🚀 Prochaines étapes

Une fois ce flow validé, on pourra :
1. Implémenter le calcul V2 (phase lunaire, aspects significatifs, focus, suggestions)
2. Sauvegarder `v2_payload` et `v2_version` en DB
3. Intégrer les endpoints V2 avec le mobile
4. Ajouter le scheduler pour génération automatique

