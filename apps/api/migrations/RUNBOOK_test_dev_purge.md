# Runbook: Test route POST /api/lunar-returns/dev/purge

## Prérequis

- Backend FastAPI arrêté (ou port 8000 libre)
- Base de données accessible
- Au moins un `lunar_return` existant pour l'utilisateur test (optionnel, pour voir la purge)

---

## Étape 1: Exporter les variables d'environnement

```bash
cd apps/api

# Variables requises
export APP_ENV=development
export DEV_AUTH_BYPASS=1
export ALLOW_DEV_PURGE=1

# Variables optionnelles (si non définies dans .env)
export DATABASE_URL="postgresql://user:password@localhost:5432/astroia_lunar"
export SECRET_KEY="your-secret-key-here"

# Vérifier les exports
echo "APP_ENV=$APP_ENV"
echo "DEV_AUTH_BYPASS=$DEV_AUTH_BYPASS"
echo "ALLOW_DEV_PURGE=$ALLOW_DEV_PURGE"
```

**Résultat attendu**: Les 3 variables affichées avec les bonnes valeurs.

---

## Étape 2: Lancer le backend

```bash
cd apps/api
source .venv/bin/activate  # Si venv existe
uvicorn main:app --reload --port 8000 --host 0.0.0.0
```

**OU** avec le script de démarrage:

```bash
cd apps/api
./start_api.sh
```

**Résultat attendu**: Le serveur démarre et affiche les logs de startup.

---

## Étape 3: Vérifier les logs de démarrage

Dans les logs du serveur, vous devez voir:

```
INFO:     [corr=<uuid>] 🚀 Lunation API démarrage...
INFO:     [corr=<uuid>] 📊 Environment: development
INFO:     [corr=<uuid>] 🔗 Database: <host>:<port>/<database>
INFO:     [corr=<uuid>] ✅ Route DEV /api/lunar-returns/dev/purge activée (ALLOW_DEV_PURGE=1)
INFO:     [corr=<uuid>] ✅ Schema sanity check OK au démarrage
INFO:     Started server process [<pid>]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

**Point critique**: La ligne `✅ Route DEV /api/lunar-returns/dev/purge activée` doit être présente.

---

## Étape 4: Préparer l'ID utilisateur pour le test

En mode `DEV_AUTH_BYPASS`, vous pouvez utiliser:
- Un `user_id` existant en DB (INTEGER)
- Un UUID string (si votre DB utilise UUID)
- Un string arbitraire (ex: `"dev-remi"`)

**Option A: Utiliser un user_id existant**

```bash
# Récupérer un user_id depuis la DB
psql "$DATABASE_URL" -c "SELECT id, email FROM users LIMIT 1;"
# Notez l'id (ex: 42)
```

**Option B: Utiliser un string arbitraire (recommandé pour test)**

```bash
DEV_USER_ID="dev-test-purge"
```

---

## Étape 5: Exécuter la purge (curl)

```bash
# Avec X-Dev-External-Id (pour UUID ou string non-numérique)
curl -X POST http://127.0.0.1:8000/api/lunar-returns/dev/purge \
  -H "X-Dev-External-Id: dev-test-purge" \
  -H "Content-Type: application/json" \
  -v

# OU avec X-Dev-User-Id (si user_id est un INTEGER)
curl -X POST http://127.0.0.1:8000/api/lunar-returns/dev/purge \
  -H "X-Dev-User-Id: 42" \
  -H "Content-Type: application/json" \
  -v
```

**Résultat attendu**: HTTP 200 OK avec un JSON de réponse.

---

## Étape 6: Réponse JSON attendue

### Cas 1: Purge réussie (lunar_returns supprimés)

```json
{
  "message": "Purge effectuée",
  "user_id": 42,
  "user_email": "test@example.com",
  "deleted_count": 12,
  "count_before": 12,
  "count_after": 0,
  "correlation_id": "550e8400-e29b-41d4-a716-446655440000"
}
```

### Cas 2: Purge réussie (DB déjà vide)

```json
{
  "message": "Purge effectuée",
  "user_id": 42,
  "user_email": null,
  "deleted_count": 0,
  "count_before": 0,
  "count_after": 0,
  "correlation_id": "550e8400-e29b-41d4-a716-446655440000"
}
```

### Cas 3: Erreur (route non disponible)

Si `ALLOW_DEV_PURGE` n'est pas activé:

```json
{
  "detail": "Route non disponible (ALLOW_DEV_PURGE non activé)"
}
```

HTTP Status: `404 Not Found`

Si `APP_ENV != "development"`:

```json
{
  "detail": "Route non disponible (uniquement en mode development)"
}
```

HTTP Status: `404 Not Found`

---

## Étape 7: Logs attendus dans le serveur

### Logs de purge réussie

```
INFO:     [corr=<uuid>] 🗑️  DEV Purge lunar returns pour user_id=42 (email=test@example.com)
INFO:     [corr=<uuid>] ✅ Purge terminée: 12 retour(s) supprimé(s) (avant: 12, après: 0)
```

### Logs si route non disponible

Si `ALLOW_DEV_PURGE` non activé:

```
WARNING:  [corr=<uuid>] ⚠️ Tentative d'accès à /dev/purge sans ALLOW_DEV_PURGE
```

Si `APP_ENV != "development"`:

```
WARNING:  [corr=<uuid>] ⚠️ Tentative d'accès à /dev/purge en mode production
```

---

## Étape 8: Vérification post-purge (optionnel)

```bash
# Vérifier que les lunar_returns ont bien été supprimés
psql "$DATABASE_URL" -c "
SELECT COUNT(*) as count
FROM public.lunar_returns
WHERE user_id = 42;
"
```

**Résultat attendu**: `count = 0`

---

## Checklist de validation

- [ ] Variables d'environnement exportées (`APP_ENV`, `DEV_AUTH_BYPASS`, `ALLOW_DEV_PURGE`)
- [ ] Backend lancé et accessible sur `http://127.0.0.1:8000`
- [ ] Log de démarrage: `✅ Route DEV /api/lunar-returns/dev/purge activée`
- [ ] Curl retourne HTTP 200 OK
- [ ] JSON de réponse contient `message`, `user_id`, `deleted_count`, `correlation_id`
- [ ] Logs serveur affichent `🗑️ DEV Purge` et `✅ Purge terminée`
- [ ] `count_after = 0` dans la réponse JSON (si des données existaient)

---

## Commandes rapides (tout-en-un)

```bash
# 1. Setup
cd apps/api
export APP_ENV=development
export DEV_AUTH_BYPASS=1
export ALLOW_DEV_PURGE=1

# 2. Lancer backend (dans un terminal)
source .venv/bin/activate
uvicorn main:app --reload --port 8000 --host 0.0.0.0

# 3. Purge (dans un autre terminal)
curl -X POST http://127.0.0.1:8000/api/lunar-returns/dev/purge \
  -H "X-Dev-External-Id: dev-test-purge" \
  -H "Content-Type: application/json" \
  | jq

# 4. Vérifier logs serveur (dans le terminal 1)
# Chercher: "✅ Route DEV /api/lunar-returns/dev/purge activée"
# Chercher: "🗑️ DEV Purge lunar returns"
# Chercher: "✅ Purge terminée"
```

---

## Dépannage

### Problème: Route retourne 404

**Causes possibles:**
1. `ALLOW_DEV_PURGE` non exporté ou valeur incorrecte
2. `APP_ENV != "development"`
3. Backend pas redémarré après changement d'environnement

**Solution:**
```bash
# Vérifier les variables
echo "APP_ENV=$APP_ENV"
echo "ALLOW_DEV_PURGE=$ALLOW_DEV_PURGE"

# Redémarrer le backend
# (Arrêter avec CTRL+C puis relancer)
```

### Problème: Erreur d'authentification

**Cause:** Header `X-Dev-External-Id` ou `X-Dev-User-Id` manquant ou incorrect

**Solution:**
```bash
# Vérifier que DEV_AUTH_BYPASS=1
echo "DEV_AUTH_BYPASS=$DEV_AUTH_BYPASS"

# Utiliser le bon header selon le type d'ID
# String/UUID → X-Dev-External-Id
# Integer → X-Dev-User-Id
```

### Problème: Logs de démarrage ne montrent pas la route activée

**Cause:** Variable `ALLOW_DEV_PURGE` non lue au démarrage

**Solution:**
```bash
# Vérifier que la variable est bien exportée AVANT le lancement
export ALLOW_DEV_PURGE=1
uvicorn main:app --reload
```

---

## Notes

- La route `/dev/purge` supprime **uniquement** les `lunar_returns` de l'utilisateur courant (celui identifié par le header DEV)
- Les autres utilisateurs ne sont **pas** affectés
- La purge est **irréversible** (pas de soft-delete)
- En production, cette route est **désactivée** (vérification `APP_ENV=development`)

