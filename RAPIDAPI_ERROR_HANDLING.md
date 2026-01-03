# RapidAPI Error Handling & Mock System

## Problème résolu

Les features Luna Pack (VOC, Lunar Mansion, Lunar Return Report) échouaient avec des erreurs RapidAPI :
- **403 Forbidden** : `{"message":"You are not subscribed to this API."}`
- **429 Too Many Requests** : Rate limit dépassé
- Le backend transformait tout en **502 Bad Gateway** avec message générique
- Le mobile affichait "Temporairement indisponible" (trompeur)

## Solution implémentée

### 1. Backend : Codes d'erreur structurés

#### Fichier: `apps/api/services/rapidapi_client.py`

**403 "not subscribed"** → Fallback automatique sur mock :
```python
if is_not_subscribed:
    logger.warning(f"⚠️  RapidAPI not subscribed (403) sur {path} -> fallback sur mock")
    return _get_mock_response(path, payload)
```

**429 Rate Limit** → Retourne 429 avec code structuré :
```python
raise HTTPException(
    status_code=429,
    detail={
        "code": "RAPIDAPI_RATE_LIMIT",
        "message": "Rate limit reached. Try later.",
        "provider_error": error_details
    }
)
```

**Autres erreurs 5xx** → 502 avec code PROVIDER_UNAVAILABLE

### 2. Système de Mock DEV_MOCK_RAPIDAPI

#### Fichier: `apps/api/services/rapidapi_mocks.py`

Génère des mocks déterministes pour :
- **Lunar Mansion** : Mansion 1-28 basée sur hash(date+location)
- **Void of Course** : VoC actif/inactif déterministe avec fenêtres réalistes
- **Lunar Return Report** : Signe lunaire, maison, degré déterministes

**Avantages** :
- ✅ Même input = même output (cohérence UI)
- ✅ Pas de dépendance RapidAPI en dev
- ✅ Tests reproductibles

#### Configuration (.env)

```bash
# Activer le mode mock
DEV_MOCK_RAPIDAPI=true
```

**Comportements** :
1. Si `DEV_MOCK_RAPIDAPI=true` → Mock immédiat (pas d'appel RapidAPI)
2. Si RapidAPI retourne 403 "not subscribed" → Fallback automatique sur mock
3. Sinon → Appel RapidAPI normal

### 3. Mobile : UX améliorée

#### Fichier: `apps/mobile/utils/errorHandler.ts`

**Extraction du code d'erreur structuré** :
```typescript
export function getErrorCode(error: any): string | null {
  return error.response?.data?.detail?.code || error.response?.data?.code || null;
}
```

**Messages explicites** :
- `RAPIDAPI_NOT_SUBSCRIBED` (503) → "Fonction indisponible en dev (API non activée)."
- `RAPIDAPI_RATE_LIMIT` (429) → "Trop de requêtes. Réessayez dans quelques instants."
- Autres erreurs → Messages existants (502, 500, timeout, etc.)

**Bouton "Réessayer" masqué pour erreurs non-retriables** :
```typescript
const isNotSubscribed = errorCode === 'RAPIDAPI_NOT_SUBSCRIBED';
if (onRetry && !isNotSubscribed) {
  // Afficher "Réessayer" uniquement si l'erreur est retriable
}
```

### 4. Tests backend

#### Fichier: `apps/api/tests/test_rapidapi_client.py`

**Nouveaux tests ajoutés** :
- ✅ `test_post_json_403_not_subscribed_fallback_mock` : Fallback sur mock
- ✅ `test_post_json_429_rate_limit_returns_429` : 429 avec code RAPIDAPI_RATE_LIMIT
- ✅ `test_dev_mock_rapidapi_enabled` : Mode mock bypass RapidAPI
- ✅ `test_mock_lunar_return_report` : Structure mock valide

**Lancer les tests** :
```bash
cd apps/api
pytest tests/test_rapidapi_client.py -v
```

## Comment activer le mode mock en dev

### Option 1 : Mode mock permanent (dev sans RapidAPI)

Ajouter dans `apps/api/.env` :
```bash
DEV_MOCK_RAPIDAPI=true
```

### Option 2 : Mode fallback automatique (RapidAPI non souscrit)

Ne rien faire ! Si RapidAPI retourne 403 "not subscribed", le fallback se fait automatiquement.

## Structure des codes d'erreur

| Erreur RapidAPI | Status Backend | Code Structuré | Message Mobile | Réessayer ? |
|-----------------|----------------|----------------|----------------|-------------|
| 403 "not subscribed" | Fallback mock | _mock: true | (Données mock) | N/A |
| 429 Rate Limit | 429 | RAPIDAPI_RATE_LIMIT | "Trop de requêtes..." | ✅ |
| 400 Bad Request | 400 | BAD_REQUEST | "Requête invalide" | ❌ |
| 401 Unauthorized | 502 | PROVIDER_AUTH_ERROR | "Temporairement indisponible" | ✅ |
| 403 Autres | 502 | PROVIDER_FORBIDDEN | "Temporairement indisponible" | ✅ |
| 404 Not Found | 502 | PROVIDER_NOT_FOUND | "Temporairement indisponible" | ❌ |
| 422 Validation | 422 | INVALID_PAYLOAD | "Données invalides" | ❌ |
| 5xx Server Error | 502 | PROVIDER_UNAVAILABLE | "Temporairement indisponible" | ✅ |
| Timeout | 504 | (string) | "Requête trop longue" | ✅ |

## Fichiers modifiés

### Backend
- ✅ `apps/api/services/rapidapi_client.py` - Gestion erreurs + mocks
- ✅ `apps/api/services/rapidapi_mocks.py` - Générateurs de mocks **[NOUVEAU]**
- ✅ `apps/api/config.py` - Flag `DEV_MOCK_RAPIDAPI`
- ✅ `apps/api/.env.example` - Documentation du flag
- ✅ `apps/api/tests/test_rapidapi_client.py` - Tests pour nouvelles features

### Mobile
- ✅ `apps/mobile/utils/errorHandler.ts` - Messages explicites + masquage "Réessayer"

## Logs pour debug

### Backend

**Mode mock activé** :
```
🎭 DEV_MOCK_RAPIDAPI enabled -> using mock for /api/v3/lunar/mansions
🎭 Mock Lunar Mansion: #12 (Al-Zubrah) pour 2025-01-15
```

**Fallback automatique sur mock** :
```
⚠️  RapidAPI not subscribed (403) sur /api/v3/lunar/void-of-course -> fallback sur mock
🎭 Mock Void of Course: Actif pour 2025-01-15
```

**Rate Limit** :
```
❌ Échec définitif après 3 tentatives: 429 - {"message": "Rate limit exceeded"}
```

### Mobile

L'utilisateur verra l'Alert avec le message approprié sans avoir à regarder la console.

## Contraintes respectées

✅ API contract existante inchangée pour les cas OK
✅ Ajout de tests unitaires backend
✅ Pas de dépendances lourdes
✅ Code lisible et commenté
✅ Écran Luna Pack reste navigable même en erreur
✅ Mock déterministe (même input = même output)
✅ Pas de casse du reste de l'app

## Prochaines étapes (optionnelles)

1. **Métriques** : Logger les erreurs RapidAPI dans un système de monitoring
2. **Cache** : Persister les mocks en DB pour éviter régénération
3. **Admin UI** : Ajouter un toggle pour activer/désactiver le mode mock depuis l'interface
4. **Notification** : Alerter l'équipe dev quand RapidAPI retourne 403 en prod

## Contact

Pour toute question sur cette implémentation, consulter :
- Backend : `apps/api/services/rapidapi_client.py` (lignes 122-155, 194-213, 272-310)
- Mocks : `apps/api/services/rapidapi_mocks.py`
- Mobile : `apps/mobile/utils/errorHandler.ts` (lignes 16-112)
