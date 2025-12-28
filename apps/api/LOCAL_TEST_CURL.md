# 🧪 Guide de test local avec curl

## Prérequis

1. ✅ API backend lancée sur `http://localhost:8000`
2. ✅ Base de données PostgreSQL accessible
3. ✅ Schema sanity check OK au démarrage

---

## 🔐 1. Login et récupérer le token

```bash
# Login (utilise OAuth2PasswordRequestForm = FormData)
TOKEN=$(curl -s -X POST "http://localhost:8000/api/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=test@example.com" \
  -d "password=password123" \
  | python3 -c "import sys, json; print(json.load(sys.stdin)['access_token'])")

echo "Token: ${TOKEN:0:30}..."
```

**Réponse attendue :**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

**Erreurs possibles :**
- `401 Unauthorized` : Email ou mot de passe incorrect
- `500 Internal Server Error` : Problème DB

---

## 🌙 2. Récupérer les 12 retours rolling (timeline mobile)

```bash
curl -X GET "http://localhost:8000/api/lunar-returns/rolling" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" | jq
```

**Avec DEV_AUTH_BYPASS :**
```bash
curl -X GET "http://127.0.0.1:8000/api/lunar-returns/rolling" \
  -H "X-Dev-User-Id: 1" \
  -H "Content-Type: application/json" | jq
```

**Réponse attendue (12 retours) :**
```json
[
  {
    "id": 1,
    "month": "2026-01",
    "return_date": "2026-01-15T12:00:00Z",
    "lunar_ascendant": "Taurus",
    "moon_house": 4,
    "moon_sign": "Aries",
    "interpretation": "..."
  },
  {
    "id": 2,
    "month": "2026-02",
    "return_date": "2026-02-12T14:30:00Z",
    ...
  }
]
```

**Si aucun retour :**
```json
[]
```

**Note :** Cet endpoint retourne les 12 prochains retours à partir de maintenant, idéal pour la timeline mobile MVP sans se soucier des années.

---

## 🌙 3. Récupérer le prochain retour lunaire

```bash
curl -X GET "http://localhost:8000/api/lunar-returns/next" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" | jq
```

**Réponse attendue (si retours générés) :**
```json
{
  "id": 1,
  "month": "2025-01",
  "return_date": "2025-01-15T12:00:00Z",
  "lunar_ascendant": "Taurus",
  "moon_house": 4,
  "moon_sign": "Aries",
  "interpretation": "..."
}
```

**Si aucun retour :**
```json
{
  "detail": "Aucun retour lunaire à venir. Utilisez POST /api/lunar-returns/generate pour générer les retours."
}
```

---

## 📅 4. Récupérer les retours d'une année

```bash
curl -X GET "http://localhost:8000/api/lunar-returns/year/2025" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" | jq
```

**Réponse attendue :**
```json
[
  {
    "id": 1,
    "month": "2025-01",
    "return_date": "2025-01-15T12:00:00Z",
    ...
  },
  {
    "id": 2,
    "month": "2025-02",
    "return_date": "2025-02-12T14:30:00Z",
    ...
  }
]
```

---

## 🚀 5. Générer les retours lunaires

```bash
curl -X POST "http://localhost:8000/api/lunar-returns/generate" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" | jq
```

**Réponse attendue :**
```json
{
  "message": "12 révolution(s) lunaire(s) générée(s)",
  "mode": "rolling",
  "start_date": "2026-01-01T00:00:00+00:00",
  "end_date": "2027-01-01T00:00:00+00:00",
  "months_count": 12,
  "generated_count": 12,
  "errors_count": 0,
  "correlation_id": "123e4567-e89b-12d3-a456-426614174000"
}
```

**Note :** Le mode `rolling` génère 12 retours glissants à partir de maintenant (ou du mois suivant si on est après le 15 du mois), garantissant qu'il y aura toujours un retour à venir pour `/next`. Les retours existants dans la période `[start_date, end_date[` sont automatiquement supprimés avant insertion pour éviter les doublons.

**Erreurs possibles :**
- `404 Not Found` : Thème natal manquant
  ```json
  {
    "detail": {
      "detail": "Thème natal manquant. Calculez-le d'abord via POST /api/natal-chart",
      "step": "fetch_natal_chart",
      "correlation_id": "..."
    }
  }
  ```
- `422 Unprocessable Entity` : Données Lune incomplètes
- `503 Service Unavailable` : Clé API Ephemeris manquante

---

## 📋 Script complet (zsh/bash)

```bash
#!/bin/bash

API_URL="http://localhost:8000"
EMAIL="test@example.com"
PASSWORD="password123"

echo "🔐 1. Login..."
TOKEN=$(curl -s -X POST "$API_URL/api/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=$EMAIL" \
  -d "password=$PASSWORD" \
  | python3 -c "import sys, json; print(json.load(sys.stdin)['access_token'])")

if [ -z "$TOKEN" ] || [ "$TOKEN" = "None" ]; then
  echo "❌ Erreur: impossible de récupérer le token"
  exit 1
fi

echo "✅ Token: ${TOKEN:0:30}..."

echo ""
echo "🌙 2. Rolling 12 retours (timeline)..."
curl -s -X GET "$API_URL/api/lunar-returns/rolling" \
  -H "Authorization: Bearer $TOKEN" | jq

echo ""
echo "🌙 3. Prochain retour lunaire..."
curl -s -X GET "$API_URL/api/lunar-returns/next" \
  -H "Authorization: Bearer $TOKEN" | jq

echo ""
echo "📅 4. Retours année 2025..."
curl -s -X GET "$API_URL/api/lunar-returns/year/2025" \
  -H "Authorization: Bearer $TOKEN" | jq

echo ""
echo "🚀 5. Générer retours (si besoin)..."
curl -s -X POST "$API_URL/api/lunar-returns/generate" \
  -H "Authorization: Bearer $TOKEN" | jq
```

---

## 🐛 Diagnostic des erreurs

### Erreur "Impossible de valider les identifiants"

**Causes possibles :**

1. **Token manquant ou invalide**
   ```bash
   # Vérifier que le token est bien dans le header
   curl -v -X GET "http://localhost:8000/api/lunar-returns/next" \
     -H "Authorization: Bearer $TOKEN"
   ```

2. **Token expiré**
   - Par défaut, les tokens expirent après 7 jours (`ACCESS_TOKEN_EXPIRE_MINUTES=10080`)
   - Relancer le login pour obtenir un nouveau token

3. **Clé SECRET_KEY différente**
   - Vérifier que `SECRET_KEY` dans `.env` correspond à celle utilisée lors de la génération du token
   - Par défaut: `dev-secret-key-change-in-production-min-32-chars`

4. **Format du token incorrect**
   - Le token doit être un JWT valide (3 parties séparées par `.`)
   - Vérifier les logs: `[corr=...] ❌ JWT decode: ...`

5. **User non trouvé en DB**
   - Le `sub` claim du JWT doit correspondre à un `user.id` existant
   - Vérifier les logs: `[corr=...] ❌ User non trouvé en DB: user_id=X`

**Solution :**
- Vérifier les logs du serveur pour voir l'erreur exacte
- Relancer un login pour obtenir un nouveau token
- Vérifier que l'utilisateur existe en DB

---

### Erreur 404 sur `/year/{year}`

**Causes :**

1. **Route non enregistrée** ✅ **CORRIGÉ** : Les endpoints `/next` et `/year/{year}` ont été ajoutés
2. **Préfixe incorrect** : Le router est monté sur `/api/lunar-returns`, donc l'URL complète est `/api/lunar-returns/year/2025`
3. **Route en conflit** : La route `/{month}` peut intercepter `/year/2025` si elle est déclarée avant

**Solution :** ✅ Les routes sont maintenant dans le bon ordre (routes spécifiques avant routes génériques)

---

## ✅ Checklist de validation

- [ ] Login retourne `{access_token, token_type}`
- [ ] Token est un JWT valide (3 parties)
- [ ] `/api/lunar-returns/next` retourne 200 ou 404 (pas 401)
- [ ] `/api/lunar-returns/year/2025` retourne 200 avec liste ou liste vide (pas 404)
- [ ] `/api/lunar-returns/generate` retourne 201 ou erreur structurée avec `correlation_id`
- [ ] Les logs montrent `[corr=...] ✅ Auth réussie` pour chaque requête authentifiée

---

## 🔧 Mode DEV_AUTH_BYPASS (optionnel)

Pour tester sans JWT en development, vous pouvez utiliser le mode `DEV_AUTH_BYPASS` :

1. **Ajouter dans `.env` :**
   ```bash
   DEV_AUTH_BYPASS=true
   APP_ENV=development
   ```

2. **Utiliser le header `X-Dev-User-Id` au lieu du token :**
   ```bash
   curl -X GET "http://localhost:8000/api/lunar-returns/next" \
     -H "X-Dev-User-Id: 1" \
     -H "Content-Type: application/json" | jq
   ```

**Note :** Ce mode fonctionne uniquement si :
- `APP_ENV=development`
- `DEV_AUTH_BYPASS=true`
- L'user_id existe en DB

---

## 📝 Notes

- Le login utilise `application/x-www-form-urlencoded` (pas JSON) car `OAuth2PasswordRequestForm` attend du FormData
- Les endpoints nécessitent un token JWT valide dans le header `Authorization: Bearer <token>`
- Les erreurs sont structurées avec `{detail, step, correlation_id}` pour le debugging
- Les logs incluent des `correlation_id` pour tracer les erreurs JWT

