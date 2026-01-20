# ✅ Endpoint GET /api/lunar-returns/rolling - Résumé

## 🎯 Objectif MVP

Créer un endpoint pour la timeline mobile qui affiche les 12 retours "rolling" sans se soucier des années.

---

## 📝 Endpoint créé

### `GET /api/lunar-returns/rolling`

**Comportement :**
- ✅ Auth identique aux autres routes (DEV_AUTH_BYPASS ok)
- ✅ Retourne les 12 prochains lunar_returns à partir de maintenant
- ✅ Fallback si < 12 trouvés : prend les 12 derniers puis tri ASC
- ✅ Retourne `[]` (pas 404) si aucun retour

**Query SQL :**
```sql
-- Essai 1: Les 12 prochains retours >= NOW()
SELECT * FROM lunar_returns
WHERE user_id = current_user.id AND return_date >= NOW()
ORDER BY return_date ASC
LIMIT 12;

-- Fallback: Si < 12, prendre les 12 derniers puis trier ASC
SELECT * FROM lunar_returns
WHERE user_id = current_user.id
ORDER BY return_date DESC
LIMIT 12;
-- Puis trier ASC en Python
```

**Réponse :**
- Liste de `LunarReturnResponse` (même shape que `/year`)
- `[]` si aucun retour (pas 404)
- Logs structurés avec `correlation_id`

---

## 📋 Modifications apportées

### 1. `routes/lunar_returns.py`

**Ajout de l'endpoint :**
```python
@router.get("/rolling", response_model=List[LunarReturnResponse])
async def get_rolling_lunar_returns(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
```

**Logique :**
1. Essayer de récupérer 12 retours avec `return_date >= NOW()`, triés ASC
2. Si < 12 trouvés, fallback sur les 12 derniers (DESC) puis trier ASC
3. Retourner la liste (vide si aucun retour)

**Ordre des routes :**
- ✅ `/rolling` est placé avant `/{month}` pour éviter les conflits
- Ordre final : `/`, `/next`, `/rolling`, `/year/{year}`, `/{month}`

---

### 2. `tests/test_lunar_returns_rolling.py` (NOUVEAU)

**Tests ajoutés :**

1. **`test_rolling_returns_12_after_generate`**
   - Après POST `/generate` → GET `/rolling` retourne 12 items
   - Vérifie que le premier a `return_date >= now` (en théorie, limité par le mock)

2. **`test_rolling_returns_empty_when_no_returns`**
   - Sans retours → `/rolling` renvoie `[]` (pas 404)
   - Vérifie status 200 avec liste vide

---

### 3. `LOCAL_TEST_CURL.md`

**Ajout de la section :**
```bash
## 🌙 2. Récupérer les 12 retours rolling (timeline mobile)

curl -X GET "http://localhost:8000/api/lunar-returns/rolling" \
  -H "Authorization: Bearer $TOKEN" | jq

# Avec DEV_AUTH_BYPASS:
curl -X GET "http://127.0.0.1:8000/api/lunar-returns/rolling" \
  -H "X-Dev-User-Id: 1" | jq
```

---

## ✅ Exemple de réponse

### Avec retours (12 items) :

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
  },
  ... (10 autres)
]
```

### Sans retours :

```json
[]
```

---

## 🔍 Logs structurés

**Exemple de logs :**
```
[corr=abc-123] 🔍 Recherche rolling 12 retours lunaires pour user_id=1
[corr=abc-123] ✅ 12 retour(s) trouvé(s) pour rolling (user_id=1)
```

**Si fallback activé :**
```
[corr=abc-123] ⚠️ Seulement 5 retour(s) à venir trouvé(s), fallback sur les 12 derniers
[corr=abc-123] ⚠️ Premier retour (2025-12-15) est dans le passé (fallback activé car < 12 retours à venir)
```

---

## 🧪 Tests

### Test unitaire

```bash
pytest tests/test_lunar_returns_rolling.py -v
```

### Test E2E (curl)

```bash
# Avec token
curl -X GET "http://localhost:8000/api/lunar-returns/rolling" \
  -H "Authorization: Bearer $TOKEN" | jq

# Avec DEV_AUTH_BYPASS
curl -X GET "http://127.0.0.1:8000/api/lunar-returns/rolling" \
  -H "X-Dev-User-Id: 1" | jq
```

---

## 📋 Checklist de validation

- [x] Endpoint `/rolling` créé et fonctionnel
- [x] Query avec `return_date >= NOW()`, tri ASC, LIMIT 12
- [x] Fallback si < 12 (12 derniers DESC puis tri ASC)
- [x] Retourne `[]` si aucun retour (pas 404)
- [x] Logs structurés avec `correlation_id`
- [x] Tests unitaires ajoutés
- [x] Documentation mise à jour
- [x] Route placée avant `/{month}` pour éviter les conflits
- [x] Trigger `return_date` côté DB non modifié (conservé)

---

## ⚠️ Notes importantes

1. **Pas de 404 :** L'endpoint retourne toujours `[]` si aucun retour (meilleure UX pour le frontend)
2. **Fallback :** Si < 12 retours à venir, on prend les 12 derniers (peut inclure des retours passés)
3. **Ordre des routes :** `/rolling` doit être avant `/{month}` pour éviter que `/{month}` capture `/rolling`
4. **Trigger DB :** `return_date` est toujours calculé par le trigger PostgreSQL (non modifié)

---

**Endpoint prêt pour la timeline mobile MVP !** 🌙✨

