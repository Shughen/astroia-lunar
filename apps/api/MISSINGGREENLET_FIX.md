# 🔧 Fix MissingGreenlet - Astroia Lunar API

## 📋 Problème

**Erreur** : `sqlalchemy.exc.MissingGreenlet: greenlet_spawn has not been called; can't call await_only() here`

**Endpoint affecté** : `GET /api/lunar-returns/current`

**Symptôme observé** :
- Mobile appelle `/current` après reset/onboarding
- API renvoie 500 la première fois
- Appel suivant renvoie parfois 200 (race condition)

---

## 🔍 Cause racine (Diagnostic détaillé)

### Séquence du bug

1. **Entrée endpoint** : `current_user` est une instance ORM `User` attachée à la session async
2. **Première query** : `current_user.id` est accessible (chargé en mémoire)
3. **Génération rolling** : Appel `_generate_rolling_if_empty()` → fait un `await db.commit()`
4. **Après commit** : Les attributs de `current_user` sont **expirés** (même avec `expire_on_commit=False`, SQLAlchemy peut marquer certains attributs comme expired dans certains contextes)
5. **Retry logic** : Accès `current_user.id` dans WHERE clause
6. **💥 CRASH** : SQLAlchemy tente un **lazy SELECT synchrone** pour recharger `current_user.id` → `MissingGreenlet`

### Preuve dans les logs

```
[DEBUG] SELECT users.id ... WHERE users.id = $1  # Lazy-load juste avant crash
[ERROR] sqlalchemy.exc.MissingGreenlet: greenlet_spawn has not been called
```

### Pourquoi `expire_on_commit=False` ne suffit pas ?

`expire_on_commit=False` évite l'expiration **automatique** après commit, MAIS :
- SQLAlchemy peut quand même expirer des attributs dans certains cas (detached instance, session fermée, etc.)
- Accès à un attribut après un `commit()` dans une autre session peut trigger un lazy-load
- **Best practice** : Ne jamais dépendre d'un ORM instance après un commit/rollback

---

## ✅ Solution appliquée

### Patch 1 : Extraire `user_id` immédiatement

**Fichier** : `apps/api/routes/lunar_returns.py`

**Ligne 1053** (au début de `get_current_lunar_return`) :
```python
# 🔒 CRITIQUE: Extraire user_id IMMÉDIATEMENT pour éviter MissingGreenlet
# Après un commit/rollback, current_user.id peut déclencher un lazy-load sync
user_id = current_user.id  # Force evaluation NOW avant tout await
```

**Modifications** :
- Remplacé **toutes** les occurrences de `current_user.id` par `user_id` dans l'endpoint
- Total : 7 remplacements (lignes 1063, 1076, 1093, 1136, 1156, 1185, 1197, 1208)

### Patch 2 : Utiliser primitif `int` au lieu d'ORM instance

**Avant** :
```python
result = await db.execute(
    select(LunarReturn).where(LunarReturn.user_id == current_user.id)  # ❌ Lazy-load possible
)
```

**Après** :
```python
user_id = current_user.id  # ✅ Évalué une seule fois au début
result = await db.execute(
    select(LunarReturn).where(LunarReturn.user_id == user_id)  # ✅ Primitif int
)
```

---

## 🧪 Tests de validation

### Test 1 : Script shell (manuel)

```bash
cd apps/api
./scripts/test_lunar_current_after_purge.sh
```

**Expected output** :
```
1️⃣ Purge lunar_returns...
HTTP Status: 200
{ "deleted_count": N, ... }

2️⃣ Appel /current (DB vide → génération rolling attendue)...
HTTP Status: 200
{ "month": "2026-01", "return_date": "2026-01-15T12:00:00Z", ... }

3️⃣ Re-appel /current (devrait utiliser cache/DB)...
HTTP Status: 200
{ "month": "2026-01", ... }

✅ Tests terminés sans erreur 500
```

### Test 2 : Pytest (automatisé)

```bash
cd apps/api
pytest tests/test_lunar_current_missinggreenlet.py -v
```

**Tests inclus** :
1. `test_current_after_purge_no_missinggreenlet` : Purge → /current → 200 (pas de 500)
2. `test_current_concurrent_requests` : 2 appels simultanés → pas de crash

**Expected** :
```
test_lunar_current_missinggreenlet.py::test_current_after_purge_no_missinggreenlet PASSED
test_lunar_current_missinggreenlet.py::test_current_concurrent_requests PASSED
```

### Test 3 : Reproduction bug (curl)

```bash
# Terminal 1: Lancer API
cd apps/api
source .venv/bin/activate
uvicorn main:app --reload

# Terminal 2: Reproduire scénario bug
# Purge
curl -X POST http://127.0.0.1:8000/api/lunar-returns/dev/purge \
  -H "X-Dev-External-Id: 550e8400-e29b-41d4-a716-446655440000"

# GET /current (AVANT fix: 500, APRÈS fix: 200)
curl -X GET http://127.0.0.1:8000/api/lunar-returns/current \
  -H "X-Dev-External-Id: 550e8400-e29b-41d4-a716-446655440000"
```

**Avant fix** :
```json
{
  "detail": "Erreur lors de la récupération de la révolution lunaire en cours"
}
HTTP 500
```

**Après fix** :
```json
{
  "id": 85,
  "month": "2026-01",
  "return_date": "2026-01-15T12:00:00+00:00",
  "lunar_ascendant": "Aries",
  ...
}
HTTP 200
```

---

## 📝 Pattern recommandé (Best practices)

### ✅ DO : Extraire user_id en début d'endpoint

```python
async def my_endpoint(current_user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    user_id = current_user.id  # ✅ Force eval BEFORE any await/commit

    # ... faire des queries avec user_id ...
    result = await db.execute(select(Model).where(Model.user_id == user_id))

    # ... commit ...
    await db.commit()

    # ... utiliser TOUJOURS user_id, jamais current_user.id
    another_result = await db.execute(select(Model).where(Model.user_id == user_id))  # ✅ Safe
```

### ❌ DON'T : Utiliser current_user.id après commit

```python
async def my_endpoint(current_user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Model).where(Model.user_id == current_user.id))  # OK ici

    await db.commit()  # Expire potentiellement current_user

    # ❌ DANGER: Lazy-load possible ici
    another_result = await db.execute(select(Model).where(Model.user_id == current_user.id))
```

---

## 🔍 Autres endpoints à vérifier

Rechercher pattern `current_user.<attr>` après `await db.commit()` dans :

1. **POST /api/lunar-returns** : Génération manuelle lunar return
2. **POST /api/natal-chart** : Calcul thème natal
3. **POST /api/natal-chart/dev/mock** : Mock natal chart
4. Tous les endpoints avec génération lazy / commit

**Commande** :
```bash
cd apps/api/routes
grep -n "current_user\." *.py | grep -A10 "await.*commit"
```

---

## 🎯 Checklist de vérification

- [x] `user_id = current_user.id` au début de `get_current_lunar_return`
- [x] Remplacé toutes les occurrences `current_user.id` → `user_id`
- [x] Test manuel : `./scripts/test_lunar_current_after_purge.sh` → 200
- [x] Test pytest : `pytest tests/test_lunar_current_missinggreenlet.py` → PASSED
- [x] Vérification logs : Plus de `MissingGreenlet` dans les erreurs
- [x] Commit + push : `git commit -m "fix: MissingGreenlet sur /current"`

---

## 📚 Références

- [SQLAlchemy Async Best Practices](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html#preventing-implicit-io-when-using-asyncsession)
- [expire_on_commit documentation](https://docs.sqlalchemy.org/en/20/orm/session_api.html#sqlalchemy.orm.Session.params.expire_on_commit)
- Issue GitHub SQLAlchemy : [Lazy loading in async context](https://github.com/sqlalchemy/sqlalchemy/issues/5811)

---

**Version** : Fix appliqué 2026-01-02
**Commit** : `4325d13`
**Status** : ✅ Résolu et testé
