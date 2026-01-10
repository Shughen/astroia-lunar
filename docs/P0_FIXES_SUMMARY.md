# P0 Fixes - Lunar API & UI
**Date**: 2026-01-02
**Branche**: feat/mvp-freeze-2026-01-02

## Résumé

Correction de 2 bugs P0 observés en test réel :
1. **P0-1**: `/api/lunar/mansion` tentait INSERT avec `mansion_id=None` → rollback mais 200 OK
2. **P0-2**: `/api/lunar/return/report` log "user: None" → route non protégée

Fixes appliqués de manière minimale (patch chirurgical, zéro scope creep).

---

## P0-1: /api/lunar/mansion - mansion_id=None

### Problème
- La normalisation RapidAPI pouvait retourner `mansion_id=None` (clé `number` manquante)
- La route tentait quand même `INSERT INTO lunar_mansions_daily(mansion_id NOT NULL)`
- PostgreSQL rollback mais API retournait 200 OK
- Logs disaient "sauvegardée" avant commit DB réussi

### Fix appliqué
**Fichier**: `apps/api/routes/lunar.py`

**Changements** (lignes 387-444):
1. Vérifier `mansion_id` AVANT tentative sauvegarde DB
2. Si `mansion_id is None` → retourner **503 Service Unavailable** (JSONResponse)
3. Payload 503:
   ```json
   {
     "status": "unavailable",
     "reason": "missing_mansion_id",
     "date": "YYYY-MM-DD",
     "provider": "rapidapi",
     "message": "Lunar Mansion data temporarily unavailable (provider returned incomplete data)",
     "data": { ...raw_response }
   }
   ```
4. Log debug: liste clés présentes dans `raw_response` et `mansion_data` pour faciliter ajustement normalizer
5. Log "sauvegardée" seulement APRÈS `await db.commit()` réussi
6. Import `from fastapi.responses import JSONResponse` ligne 394

**Tests ajoutés**: `apps/api/tests/test_lunar_mansion_missing_id.py`
- `test_lunar_mansion_missing_mansion_id_returns_503()` : Mock API sans `number` → attend 503
- `test_lunar_mansion_with_valid_mansion_id_returns_200()` : Régression avec `number` valide → attend 200

**Résultat tests**:
```
tests/test_lunar_mansion_missing_id.py::test_lunar_mansion_missing_mansion_id_returns_503 PASSED
tests/test_lunar_mansion_missing_id.py::test_lunar_mansion_with_valid_mansion_id_returns_200 PASSED
```

---

## P0-2: /api/lunar/return/report - Authentication manquante

### Problème
- Route POST `/api/lunar/return/report` n'avait pas `Depends(get_current_user)`
- Log "user: None" visible en production
- API retournait 200 avec données même sans auth
- Normalisation pouvait retourner `moon=None`, `return_date=None`

### Fix appliqué
**Fichier**: `apps/api/routes/lunar.py`

**Changements**:
1. Ligne 25-26: Import `from models.user import User` + `from routes.auth import get_current_user`
2. Ligne 174: Ajout parameter `current_user: User = Depends(get_current_user)`
3. Ligne 198: Log utilise `current_user.id` au lieu de `request.user_id`
4. Docstring ligne 186: "**Authentification requise**: Bearer token ou DEV_AUTH_BYPASS"
5. Docstring ligne 190: Ajout "- 401 si non authentifié"

**Tests ajoutés**: `apps/api/tests/test_lunar_return_auth.py`
- `test_lunar_return_report_without_auth_returns_401()` : Sans token ni bypass → attend 401
- `test_lunar_return_report_with_dev_bypass_succeeds()` : Avec DEV_AUTH_BYPASS + header → attend 200

**Résultat tests**:
```
tests/test_lunar_return_auth.py::test_lunar_return_report_without_auth_returns_401 PASSED
tests/test_lunar_return_report_with_dev_bypass_succeeds PASSED
```

---

## UI Mobile - Suppression affichages "N/A"

### Problème
- Écran Luna Pack (`apps/mobile/app/lunar/index.tsx`) affichait "N/A" pour valeurs manquantes
- Demande: afficher "—" ou "Indisponible" + masquer lignes vides

### Fix appliqué
**Fichier**: `apps/mobile/app/lunar/index.tsx`

**Changements**:
1. Ligne 44: `formatShortDateTime()` retourne `'—'` au lieu de `'N/A'`
2. Lignes 159-188: **Lunar Return Report**
   - Conditionnel `{get(data, 'return_date') ? ... : "—"}`
   - Conditionnel `{get(data, 'moon.sign') ? ... : "—"}`
3. Lignes 233-264: **Lunar Mansion**
   - `{get(data, 'mansion.number') ? ... : "Indisponible pour le moment"}`
   - Masquage ligne `to_mansion.number` si absente

**Résultat**:
- Plus aucun affichage "N/A"
- Valeurs manquantes → "—" ou message clair
- Si API 503 pour mansion → "Indisponible pour le moment" + JSON debug reste accessible

---

## Fichiers modifiés (diff summary)

**Backend** (3 fichiers):
```
M  apps/api/routes/lunar.py           (+65 -28)
A  apps/api/tests/test_lunar_mansion_missing_id.py
A  apps/api/tests/test_lunar_return_auth.py
```

**Mobile** (1 fichier):
```
M  apps/mobile/app/lunar/index.tsx    (+25 -10)
```

---

## Tests - Résultats complets

**Nouveaux tests** (4):
- ✅ `test_lunar_mansion_missing_mansion_id_returns_503`
- ✅ `test_lunar_mansion_with_valid_mansion_id_returns_200`
- ✅ `test_lunar_return_report_without_auth_returns_401`
- ✅ `test_lunar_return_report_with_dev_bypass_succeeds`

**Tests existants** (32):
```
pytest tests/test_lunar_services.py -v
======================= 32 passed, 21 warnings in 0.35s ========================
```

**Total**: ✅ **36 tests passing**, 0 failures

---

## Reproduction manuelle (curl)

### P0-1: Tester mansion_id manquant (nécessite mock API ou cas réel)

**Scénario**: Provider RapidAPI retourne réponse sans `mansion.number`

**curl (dev)**:
```bash
curl -X POST http://localhost:8000/api/lunar/mansion \
  -H "Content-Type: application/json" \
  -H "X-Dev-User-Id: 1" \
  -d '{
    "date": "2025-01-15",
    "time": "12:00",
    "latitude": 48.8566,
    "longitude": 2.3522,
    "timezone": "Europe/Paris"
  }'
```

**Attendu si mansion_id manquant**:
```json
HTTP 503
{
  "status": "unavailable",
  "reason": "missing_mansion_id",
  "date": "2025-01-15",
  "provider": "rapidapi",
  "message": "Lunar Mansion data temporarily unavailable (provider returned incomplete data)",
  "data": { ...raw_response }
}
```

**Attendu si mansion_id présent**:
```json
HTTP 200
{
  "provider": "rapidapi",
  "kind": "lunar_mansion",
  "data": {
    "mansion": {
      "number": 1,
      "name": "Al-Sharatain",
      ...
    }
  },
  "cached": false
}
```

### P0-2: Tester auth requise

**Sans auth (DEV_AUTH_BYPASS=False)**:
```bash
curl -X POST http://localhost:8000/api/lunar/return/report \
  -H "Content-Type: application/json" \
  -d '{
    "birth_date": "1989-04-15",
    "birth_time": "17:55",
    "latitude": 48.8566,
    "longitude": 2.3522,
    "timezone": "Europe/Paris",
    "date": "2025-01-15",
    "month": "2025-01"
  }'
```

**Attendu**: `HTTP 401 Unauthorized`

**Avec DEV_AUTH_BYPASS + header**:
```bash
curl -X POST http://localhost:8000/api/lunar/return/report \
  -H "Content-Type: application/json" \
  -H "X-Dev-User-Id: 1" \
  -d '{ ...same payload }'
```

**Attendu**: `HTTP 200` + log "user: 1" (pas "user: None")

---

## Notes de déploiement

1. **Pas de migration DB requise** (schéma inchangé)
2. **Environnement DEV**: DEV_AUTH_BYPASS continue de fonctionner normalement
3. **Environnement PROD**: Route `/api/lunar/return/report` nécessite token valide
4. **Breaking change**: Clients appelant `/api/lunar/return/report` sans auth → 401 (avant: 200)
5. **Backward compatible**: `/api/lunar/mansion` avec données valides → comportement identique

---

## Prochaines étapes (optionnelles)

1. **Ajuster normalizer** si nouvelles clés RapidAPI détectées (logs debug fournis)
2. **Monitoring 503**: Si taux élevé mansion_id=None → investiguer provider RapidAPI
3. **UI 503 handling**: Afficher message utilisateur si 503 fréquent (actuellement: "Indisponible")

---

**Fin du rapport P0 Fixes**
