# Fix: Mock Detection dans Luna Pack (Mobile UX)

## Problème identifié

Quand `DEV_MOCK_RAPIDAPI=true` ou fallback sur 403 "not subscribed" :
- ✅ `/api/lunar/voc` : affichait correctement "provider: mock (dev)" + badge MOCK
- ❌ `/api/lunar/mansion` : affichait "provider: rapidapi" + texte brut "Mock interpretation..."
- ❌ `/api/lunar/return/report` : affichait "provider: rapidapi" + texte brut "Mock interpretation..."

**Cause** : Les champs `_mock` et `_reason` étaient perdus dans la normalisation.

## Solution appliquée

### 1. Préservation des méta-champs dans les normalizers

**Fichier** : `apps/api/services/lunar_normalization.py`

#### Changement pour `normalize_lunar_mansion_response` :

```python
# CRITICAL: Preserve mock metadata (if present) so mobile can detect mock responses
# These fields are added by rapidapi_mocks.py when DEV_MOCK_RAPIDAPI=true or fallback on 403
for meta_key in ["_mock", "_reason"]:
    if meta_key in raw_response:
        normalized[meta_key] = raw_response[meta_key]
```

#### Changement pour `normalize_lunar_return_report_response` :

```python
# CRITICAL: Preserve mock metadata (if present) so mobile can detect mock responses
# These fields are added by rapidapi_mocks.py when DEV_MOCK_RAPIDAPI=true or fallback on 403
for meta_key in ["_mock", "_reason"]:
    if meta_key in raw_response:
        normalized[meta_key] = raw_response[meta_key]
```

**Résultat** : Les champs `_mock` et `_reason` passent maintenant à travers la normalisation.

---

### 2. Détection dynamique du provider dans les routes

**Fichier** : `apps/api/routes/lunar.py`

#### Pour les 3 endpoints (mansion, voc, return/report) :

**Avant** :
```python
result = await lunar_services.get_lunar_return_report(payload)

return LunarResponse(
    provider="rapidapi",  # ❌ Hardcodé
    kind="lunar_return_report",
    data=result,
    cached=False
)
```

**Après** :
```python
result = await lunar_services.get_lunar_return_report(payload)

# Détecter si la réponse est un mock (pour mettre le bon provider)
is_mock = result.get("_mock", False)
provider = "mock" if is_mock else "rapidapi"

return LunarResponse(
    provider=provider,  # ✅ Dynamique
    kind="lunar_return_report",
    data=result,
    cached=False
)
```

**Routes modifiées** :
- `POST /api/lunar/return/report` (ligne 215-216, 254)
- `POST /api/lunar/voc` (ligne 320-321, 349)
- `POST /api/lunar/mansion` (ligne 409-410, 475)

---

### 3. Test de non-régression

**Fichier** : `apps/api/tests/test_rapidapi_client.py`

Ajout du test `test_mock_metadata_preserved_after_normalization` :

```python
@pytest.mark.asyncio
async def test_mock_metadata_preserved_after_normalization():
    """Test que les champs _mock et _reason sont préservés après normalisation"""
    from services.lunar_normalization import normalize_lunar_mansion_response

    # Mock response avec metadata
    mock_mansion = {
        "mansion": {"number": 5, "name": "Al-Haq'ah"},
        "_mock": True,
        "_reason": "DEV_MOCK_RAPIDAPI enabled or RapidAPI not subscribed"
    }

    normalized = normalize_lunar_mansion_response(mock_mansion)

    # Vérifier que _mock et _reason sont préservés
    assert normalized.get("_mock") is True
    assert normalized.get("_reason") == "DEV_MOCK_RAPIDAPI enabled or RapidAPI not subscribed"
    assert normalized["mansion"]["number"] == 5
```

---

## Résultat attendu

### Réponse API avec mock activé

```json
{
  "provider": "mock",
  "kind": "lunar_mansion",
  "data": {
    "mansion": {
      "number": 12,
      "name": "Al-Zubrah",
      "interpretation": "Mock interpretation for Al-Zubrah. This is a development mock response."
    },
    "upcoming_changes": [...],
    "_mock": true,
    "_reason": "DEV_MOCK_RAPIDAPI enabled or RapidAPI not subscribed"
  },
  "cached": false
}
```

### UX Mobile

Le mobile peut maintenant détecter le mock via :
1. `response.provider === "mock"` → Affiche "mock (dev)"
2. `response.data._mock === true` → Affiche badge MOCK
3. `response.data._reason` → Pour debug/logging

L'utilitaire `isMockResponse()` (apps/mobile/utils/mockUtils.ts) fonctionne désormais pour toutes les routes.

---

## Tests de validation

### Backend

```bash
cd apps/api
pytest tests/test_rapidapi_client.py::test_mock_metadata_preserved_after_normalization -v
# ✅ PASSED
```

### Validation manuelle (avec DEV_MOCK_RAPIDAPI=true)

```bash
# 1. Activer le mode mock
echo "DEV_MOCK_RAPIDAPI=true" >> .env

# 2. Tester Mansion
curl -X POST http://localhost:8000/api/lunar/mansion \
  -H "Content-Type: application/json" \
  -d '{
    "date": "2025-01-15",
    "time": "12:00",
    "latitude": 48.8566,
    "longitude": 2.3522,
    "timezone": "Europe/Paris"
  }' | jq '.provider, .data._mock'
# Attendu:
# "mock"
# true

# 3. Tester Return Report
curl -X POST http://localhost:8000/api/lunar/return/report \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{
    "birth_date": "1990-01-15",
    "birth_time": "14:30",
    "latitude": 48.8566,
    "longitude": 2.3522,
    "timezone": "Europe/Paris",
    "date": "2025-01-15",
    "month": "2025-01"
  }' | jq '.provider, .data._mock'
# Attendu:
# "mock"
# true
```

### Mobile

1. Activer `DEV_MOCK_RAPIDAPI=true` dans `.env`
2. Relancer l'API
3. Ouvrir `/lunar` dans l'app mobile
4. Cliquer sur "Lunar Mansion" ou "Lunar Return Report"
5. Vérifier que :
   - Provider affiche : `"Provider: mock (dev)"`
   - Badge `MOCK` s'affiche en haut à droite
   - Interprétation affiche : `"Données de démonstration (mode dev)."`

---

## Fichiers modifiés

- ✅ `apps/api/services/lunar_normalization.py` - Préservation `_mock` et `_reason`
- ✅ `apps/api/routes/lunar.py` - Détection dynamique du provider
- ✅ `apps/api/tests/test_rapidapi_client.py` - Test de non-régression + fix test 429

---

## Contraintes respectées

✅ API contract existante inchangée pour les cas OK (prod sans mock)
✅ Pas de casse du reste de l'app
✅ Mock déterministe maintenu
✅ Tests backend ajoutés
✅ Code minimal, lisible, safe

---

## Impact en production

**Aucun impact** :
- En prod, `DEV_MOCK_RAPIDAPI=false` (default)
- RapidAPI ne retourne pas 403 "not subscribed" (clé valide)
- Donc `_mock` et `_reason` ne sont jamais présents dans les réponses
- `provider` reste "rapidapi" comme avant
- Les normalizers ne font rien si `_mock`/`_reason` absents (loop vide)

**Performance** :
- Overhead négligeable : 2 boucles `for meta_key in ["_mock", "_reason"]` (O(1))
- Pas de requête DB supplémentaire
- Pas de calcul lourd

---

## Prochaines étapes (optionnelles)

1. Vérifier que la persistance en DB ne stocke pas `_mock`/`_reason` (si souhaité)
2. Ajouter un indicateur visuel dans l'admin UI pour voir quand mock mode est actif
3. Métriques : Logger combien de fois le fallback mock est utilisé en dev

---

## Contact

Pour questions sur ce patch :
- Backend normalization : `apps/api/services/lunar_normalization.py` (lignes 60-64, 197-201)
- Routes provider detection : `apps/api/routes/lunar.py` (lignes 215-216, 320-321, 409-410)
- Tests : `apps/api/tests/test_rapidapi_client.py` (ligne 346-383)
