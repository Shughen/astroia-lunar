# 🔧 Fix API locale - Résumé des corrections

## Problèmes identifiés et corrigés

### 1. ❌ Endpoints `/next` et `/year/{year}` manquants

**Problème :** Les endpoints `/api/lunar-returns/next` et `/api/lunar-returns/year/{year}` n'existaient pas dans le code.

**Solution :** Ajout des endpoints dans `routes/lunar_returns.py` :
- `GET /api/lunar-returns/next` : retourne le prochain retour lunaire (>= maintenant)
- `GET /api/lunar-returns/year/{year}` : retourne tous les retours d'une année

**Fichier modifié :** `routes/lunar_returns.py`

---

### 2. ❌ Gestion d'erreur JWT non structurée

**Problème :** Les erreurs JWT renvoyaient simplement "Impossible de valider les identifiants" sans détails.

**Solution :** Ajout de logs structurés avec `correlation_id` pour chaque erreur :
- Token manquant
- Token expiré (`ExpiredSignatureError`)
- Erreur de signature/format (`JWTError`)
- Claim `sub` manquant ou invalide
- User non trouvé en DB

**Fichier modifié :** `routes/auth.py` (fonction `get_current_user`)

---

### 3. ✅ Mode DEV_AUTH_BYPASS ajouté (optionnel)

**Fonctionnalité :** Permet de bypasser l'authentification JWT en development avec le header `X-Dev-User-Id`.

**Configuration :**
- Variable d'environnement : `DEV_AUTH_BYPASS=true`
- Header requis : `X-Dev-User-Id: 1` (user_id)

**Utilisation :**
```bash
# Au lieu de:
curl -H "Authorization: Bearer $TOKEN" ...

# On peut faire (si DEV_AUTH_BYPASS=true et APP_ENV=development):
curl -H "X-Dev-User-Id: 1" ...
```

**Fichiers modifiés :**
- `config.py` : Ajout du champ `DEV_AUTH_BYPASS`
- `routes/auth.py` : Logique de bypass dans `get_current_user`

---

## 📝 Fichiers modifiés

### `routes/lunar_returns.py`

**Ajouts :**
- `GET /next` : Prochain retour lunaire
- `GET /year/{year}` : Retours d'une année

**Ordre des routes :**
1. `POST /generate`
2. `GET /` (tous les retours)
3. `GET /next` ← **NOUVEAU**
4. `GET /year/{year}` ← **NOUVEAU**
5. `GET /{month}` (route générique en dernier)

**Important :** Les routes spécifiques (`/next`, `/year/{year}`) sont déclarées AVANT la route générique `/{month}` pour éviter les conflits.

---

### `routes/auth.py`

**Améliorations :**
- Logs structurés avec `correlation_id` pour chaque erreur JWT
- Distinction entre `ExpiredSignatureError` et autres `JWTError`
- Mode DEV_AUTH_BYPASS avec header `X-Dev-User-Id`
- `oauth2_scheme` avec `auto_error=False` pour permettre le bypass

**Logs ajoutés :**
```python
logger.warning(f"[corr={correlation_id}] ❌ JWT decode: token expiré")
logger.warning(f"[corr={correlation_id}] ❌ JWT decode: 'sub' claim manquant")
logger.warning(f"[corr={correlation_id}] ❌ User non trouvé en DB: user_id={user_id}")
logger.debug(f"[corr={correlation_id}] ✅ Auth réussie: user_id={user_id}, email={user.email}")
```

---

### `config.py`

**Ajout :**
- `DEV_AUTH_BYPASS: bool = Field(default=False, description="...")`

---

## 🧪 Commandes curl complètes

### 1. Login

```bash
TOKEN=$(curl -s -X POST "http://localhost:8000/api/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=test@example.com" \
  -d "password=password123" \
  | python3 -c "import sys, json; print(json.load(sys.stdin)['access_token'])")

echo "Token: ${TOKEN:0:30}..."
```

---

### 2. Prochain retour lunaire

```bash
curl -X GET "http://localhost:8000/api/lunar-returns/next" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" | jq
```

---

### 3. Retours d'une année

```bash
curl -X GET "http://localhost:8000/api/lunar-returns/year/2025" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" | jq
```

---

### 4. Générer les retours

```bash
curl -X POST "http://localhost:8000/api/lunar-returns/generate" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" | jq
```

---

## 🔍 Diagnostic des erreurs

### "Impossible de valider les identifiants"

**Vérifications :**

1. **Vérifier les logs du serveur :**
   ```
   [corr=...] ❌ JWT decode: token expiré
   [corr=...] ❌ JWT decode: 'sub' claim manquant
   [corr=...] ❌ User non trouvé en DB: user_id=X
   ```

2. **Vérifier le format du token :**
   ```bash
   # Un JWT valide a 3 parties séparées par des points
   echo $TOKEN | cut -d'.' -f1-3 | wc -w  # Devrait être 1
   ```

3. **Vérifier que SECRET_KEY correspond :**
   - Le token doit avoir été généré avec la même `SECRET_KEY` que celle utilisée pour le décoder
   - Par défaut: `dev-secret-key-change-in-production-min-32-chars`

4. **Relancer un login pour obtenir un nouveau token :**
   ```bash
   # Si le token est expiré ou invalide, relancer le login
   TOKEN=$(curl -s -X POST "http://localhost:8000/api/auth/login" ...)
   ```

---

### 404 sur `/year/{year}`

**✅ CORRIGÉ :** L'endpoint `/year/{year}` a été ajouté. Il faut utiliser l'URL complète :

```
GET /api/lunar-returns/year/2025
```

**Vérifier :**
```bash
# Vérifier que la route est bien enregistrée
curl -v -X GET "http://localhost:8000/api/lunar-returns/year/2025" \
  -H "Authorization: Bearer $TOKEN"

# Devrait retourner 200 avec une liste (vide ou non), pas 404
```

---

## ✅ Checklist de validation

- [x] Les endpoints `/next` et `/year/{year}` existent
- [x] Les routes sont dans le bon ordre (spécifiques avant génériques)
- [x] Les logs JWT incluent `correlation_id` et la cause exacte
- [x] Le mode DEV_AUTH_BYPASS est disponible (optionnel)
- [x] Les commandes curl fonctionnent avec un token valide

---

## 📚 Documentation

- **Guide de test complet :** `LOCAL_TEST_CURL.md`
- **Endpoints disponibles :** Voir `/docs` (Swagger UI) sur `http://localhost:8000/docs`

