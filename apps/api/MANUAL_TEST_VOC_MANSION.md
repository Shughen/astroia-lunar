# Manuel de Test - VoC & Lunar Mansion Fix (P1-BACKEND)

## Résumé des Corrections

**Problème:** Les endpoints `/api/lunar/voc` et `/api/lunar/mansion` renvoyaient 500 au lieu de 422 quand RapidAPI rejetait les payloads.

**Cause racine:**
1. Le payload envoyé à RapidAPI était plat (`date`, `time`, `latitude`, etc.) au lieu d'être nested (`datetime_location`)
2. **RapidAPI attend des composantes datetime séparées** (`year`, `month`, `day`, `hour`, `minute` comme integers), PAS des strings `date`/`time`
3. Les catch-all `except Exception` dans les routes convertissaient toutes les erreurs en 500
4. Le Lunar Mansion n'avait pas de transformation de payload du tout

**Corrections appliquées:**
1. ✅ Transformation automatique du payload plat → nested RapidAPI format pour VoC
2. ✅ Transformation automatique du payload plat → nested RapidAPI format pour Lunar Mansion
3. ✅ **Parsing date/time strings → composantes datetime integers** (year, month, day, hour, minute)
4. ✅ Error handling propre dans routes: HTTPException re-raised, ValueError→422, Exception→500
5. ✅ Logs améliorés avec exc_info=True pour debugging
6. ✅ Tests complets (31 tests, tous passent)

---

## Fichiers Modifiés

| Fichier | Changements |
|---------|------------|
| `services/lunar_services.py` | Ajout `_transform_mansion_to_rapidapi_format()` |
| `routes/lunar.py` | Ajout proper error handling pour VoC et Mansion |
| `tests/test_lunar_services.py` | 7 nouveaux tests Mansion (24→31 tests) |

---

## Tests Unitaires (Automatisés)

**Exécuter les tests:**
```bash
cd apps/api
python -m pytest tests/test_lunar_services.py -v
```

**Résultats attendus:**
```
✅ 31 passed in 0.32s
```

**Tests couverts:**

### VoC (7 tests):
- ✅ Payload valide avec tous les champs → 200
- ✅ Missing date → ValueError
- ✅ Missing time → ValueError
- ✅ Missing latitude → ValueError
- ✅ Missing longitude → ValueError
- ✅ Defaults appliqués (timezone→UTC)
- ✅ RapidAPI 422 → 422 propagé (pas 502!)
- ✅ Transformation payload correcte (datetime_location nested)

### Lunar Mansion (7 tests):
- ✅ Payload valide avec tous les champs → 200
- ✅ Missing date → ValueError
- ✅ Missing time → ValueError
- ✅ Missing latitude → ValueError
- ✅ Missing longitude → ValueError
- ✅ Defaults appliqués (timezone→UTC)
- ✅ RapidAPI 422 → 422 propagé (pas 502!)
- ✅ Transformation payload correcte (datetime_location nested)

---

## Test Manuel - Void of Course (VoC)

### Scénario 1: Payload Valide (Doit fonctionner)

**Payload:**
```bash
curl -X POST http://localhost:8000/api/lunar/voc \
  -H "Content-Type: application/json" \
  -d '{
    "date": "2025-12-31",
    "time": "12:00",
    "latitude": 48.8566,
    "longitude": 2.3522,
    "timezone": "Europe/Paris"
  }'
```

**Réponse attendue:**
- Status: `200 OK`
- Body:
  ```json
  {
    "provider": "rapidapi",
    "kind": "void_of_course",
    "data": {
      "is_void": false,
      "next_void": "2025-12-31T18:30:00Z"
    },
    "cached": false
  }
  ```

**Logs backend:**
```
🌑 Vérification Void of Course - date: 2025-12-31
📡 Appel RapidAPI: POST /api/v3/void-of-course | Payload: {
  'endpoint': '/api/v3/void-of-course',
  'has_subject': False,
  'has_birth_data': False,
  'fields': ['datetime_location']
}
✅ Réponse RapidAPI reçue (status 200, attempt 1)
✅ Void of Course calculé avec succès
```

---

### Scénario 2: Payload Invalide - Missing date (Doit échouer avec 422)

**Payload:**
```bash
curl -X POST http://localhost:8000/api/lunar/voc \
  -H "Content-Type: application/json" \
  -d '{
    "time": "12:00",
    "latitude": 48.8566,
    "longitude": 2.3522
  }'
```

**Réponse attendue:**
- Status: `422 Unprocessable Entity`
- Body:
  ```json
  {
    "detail": {
      "code": "INVALID_PAYLOAD",
      "message": "Champs requis manquants: date",
      "hint": "Vérifiez que date (YYYY-MM-DD), time (HH:MM), latitude, et longitude sont fournis"
    }
  }
  ```

**Logs backend:**
```
❌ Payload invalide pour VoC: Champs requis manquants: date
```

---

### Scénario 3: Payload Invalide - Missing latitude (Doit échouer avec 422)

**Payload:**
```bash
curl -X POST http://localhost:8000/api/lunar/voc \
  -H "Content-Type: application/json" \
  -d '{
    "date": "2025-12-31",
    "time": "12:00",
    "longitude": 2.3522
  }'
```

**Réponse attendue:**
- Status: `422 Unprocessable Entity`
- Body contient: `"Champs requis manquants: latitude"`

---

## Test Manuel - Lunar Mansion

### Scénario 1: Payload Valide (Doit fonctionner)

**Payload:**
```bash
curl -X POST http://localhost:8000/api/lunar/mansion \
  -H "Content-Type: application/json" \
  -d '{
    "date": "2025-12-31",
    "time": "12:00",
    "latitude": 48.8566,
    "longitude": 2.3522,
    "timezone": "Europe/Paris"
  }'
```

**Réponse attendue:**
- Status: `200 OK`
- Body:
  ```json
  {
    "provider": "rapidapi",
    "kind": "lunar_mansion",
    "data": {
      "mansion": {
        "number": 14,
        "name": "Al-Simak",
        "interpretation": "Favorable aux projets créatifs..."
      }
    },
    "cached": false
  }
  ```

**Logs backend:**
```
🏰 Calcul Lunar Mansion - date: 2025-12-31
📤 Transformed Mansion payload for RapidAPI: datetime_location={'date': '2025-12-31', 'time': '12:00', ...}
📡 Appel RapidAPI: POST /api/v3/lunar-mansions | Payload: {
  'endpoint': '/api/v3/lunar-mansions',
  'has_subject': False,
  'has_birth_data': False,
  'fields': ['datetime_location']
}
✅ Réponse RapidAPI reçue (status 200, attempt 1)
✅ Lunar Mansion calculée avec succès
```

---

### Scénario 2: Payload Invalide - Missing time (Doit échouer avec 422)

**Payload:**
```bash
curl -X POST http://localhost:8000/api/lunar/mansion \
  -H "Content-Type: application/json" \
  -d '{
    "date": "2025-12-31",
    "latitude": 48.8566,
    "longitude": 2.3522
  }'
```

**Réponse attendue:**
- Status: `422 Unprocessable Entity`
- Body:
  ```json
  {
    "detail": {
      "code": "INVALID_PAYLOAD",
      "message": "Champs requis manquants: time",
      "hint": "Vérifiez que date (YYYY-MM-DD), time (HH:MM), latitude, et longitude sont fournis"
    }
  }
  ```

**Logs backend:**
```
❌ Payload invalide pour Lunar Mansion: Champs requis manquants: time
```

---

### Scénario 3: Payload Invalide - Missing longitude (Doit échouer avec 422)

**Payload:**
```bash
curl -X POST http://localhost:8000/api/lunar/mansion \
  -H "Content-Type: application/json" \
  -d '{
    "date": "2025-12-31",
    "time": "12:00",
    "latitude": 48.8566
  }'
```

**Réponse attendue:**
- Status: `422 Unprocessable Entity`
- Body contient: `"Champs requis manquants: longitude"`

---

## Scénario 4: API RapidAPI Down (Simulation)

**Action:**
1. Modifier temporairement `.env` avec une mauvaise RAPIDAPI_KEY
2. Envoyer un payload valide à VoC ou Mansion

**Payload test:**
```bash
curl -X POST http://localhost:8000/api/lunar/voc \
  -H "Content-Type: application/json" \
  -d '{
    "date": "2025-12-31",
    "time": "12:00",
    "latitude": 48.8566,
    "longitude": 2.3522
  }'
```

**Réponse attendue (mauvaise API key):**
- Status: `502 Bad Gateway`
- Body:
  ```json
  {
    "detail": {
      "code": "PROVIDER_AUTH_ERROR",
      "message": "Erreur d'authentification avec le fournisseur astrologique",
      "provider_error": {...}
    }
  }
  ```

**Logs backend (avec retries):**
```
⚠️  Erreur 401 de RapidAPI sur /api/v3/void-of-course, retry 1/3 dans 0.52s
⚠️  Erreur 401 de RapidAPI sur /api/v3/void-of-course, retry 2/3 dans 1.08s
❌ Échec définitif après 3 tentatives: 401 - ...
```

---

## Checklist de Validation

Avant de considérer le fix comme validé:

### Tests Automatisés
- [x] Tests unitaires passent (31/31)
- [x] VoC: transformation payload correcte
- [x] VoC: missing fields → ValueError → 422
- [x] VoC: RapidAPI 422 → 422 propagé
- [x] Mansion: transformation payload correcte
- [x] Mansion: missing fields → ValueError → 422
- [x] Mansion: RapidAPI 422 → 422 propagé

### Tests Manuels VoC
- [ ] Payload valide → 200 OK avec données
- [ ] Missing date → 422 avec message clair
- [ ] Missing time → 422 avec message clair
- [ ] Missing latitude → 422 avec message clair
- [ ] Missing longitude → 422 avec message clair
- [ ] RapidAPI 422 → 422 propagé (PAS 500!)
- [ ] RapidAPI 500 → 502 après retries
- [ ] RapidAPI timeout → 504

### Tests Manuels Lunar Mansion
- [ ] Payload valide → 200 OK avec données
- [ ] Missing date → 422 avec message clair
- [ ] Missing time → 422 avec message clair
- [ ] Missing latitude → 422 avec message clair
- [ ] Missing longitude → 422 avec message clair
- [ ] RapidAPI 422 → 422 propagé (PAS 500!)
- [ ] RapidAPI 500 → 502 après retries

### Logs
- [ ] Logs contiennent payload summary (has_subject, fields)
- [ ] Logs avec exc_info=True pour exceptions 500
- [ ] Logs ne contiennent PAS de PII (pas de coords en clair dans les logs d'erreur)

---

## Garanties Fournies

### ✅ Jamais 500 pour erreurs de payload
- Missing fields → 422 avec message explicite
- Invalid format → 422 avec hint
- Validation Pydantic → 422 automatique

### ✅ Jamais 502 pour erreurs client
- 422 de RapidAPI → 422 propagé tel quel
- 400 de RapidAPI → 400 propagé

### ✅ Toujours 502/504 pour erreurs provider
- 401/403 RapidAPI → 502 (auth error)
- 5xx RapidAPI → 502 après retries
- Timeout → 504 après retries

---

## Structure des Payloads Transformés

### Ce que le mobile envoie (flat):
```json
{
  "date": "2025-12-31",
  "time": "12:00",
  "latitude": 48.8566,
  "longitude": 2.3522,
  "timezone": "Europe/Paris"
}
```

### VoC - Format attendu par RapidAPI (transformé):
```json
{
  "datetime_location": {
    "year": 2025,
    "month": 12,
    "day": 31,
    "hour": 12,
    "minute": 0,
    "second": 0,
    "latitude": 48.8566,
    "longitude": 2.3522,
    "timezone": "Europe/Paris"
  }
}
```

### Lunar Mansion - Format attendu par RapidAPI (transformé):
```json
{
  "datetime_location": {
    "year": 2025,
    "month": 12,
    "day": 31,
    "hour": 12,
    "minute": 0,
    "second": 0,
    "latitude": 48.8566,
    "longitude": 2.3522,
    "timezone": "Europe/Paris"
  }
}
```

**Note:**
- Les deux utilisent la même structure `datetime_location`, contrairement à Lunar Return qui utilise `subject.birth_data`.
- **IMPORTANT:** RapidAPI attend des composantes datetime séparées (year, month, day, hour, minute comme integers), PAS des strings date/time.
- La transformation parse automatiquement "YYYY-MM-DD" → year/month/day et "HH:MM" → hour/minute.

---

## Débogage

### Si tests échouent

**Vérifier les imports:**
```bash
cd apps/api
python -c "from services import lunar_services; print(lunar_services.__file__)"
```

**Vérifier la transformation Mansion:**
```python
from services.lunar_services import _transform_mansion_to_rapidapi_format

payload = {
    "date": "2025-12-31",
    "time": "12:00",
    "latitude": 48.8566,
    "longitude": 2.3522
}

result = _transform_mansion_to_rapidapi_format(payload)
print(result)
# Doit afficher: {'datetime_location': {...}}
```

### Si mobile reçoit toujours 500

1. **Vérifier les logs backend** - quel est le vrai message d'erreur ?
2. **Vérifier que le code est à jour** - relancer le backend (`uvicorn --reload`)
3. **Vérifier le payload mobile** - contient-il tous les champs requis ?

### Si erreurs de module non trouvé

```bash
cd apps/api
pip install -e .
# OU
export PYTHONPATH=/Users/remibeaurain/astroia/astroia-lunar/apps/api:$PYTHONPATH
```

---

## Rollback (Si problème critique)

Si le fix cause des problèmes, rollback rapide:

```bash
cd apps/api
git checkout HEAD~1 services/lunar_services.py
git checkout HEAD~1 routes/lunar.py
git checkout HEAD~1 tests/test_lunar_services.py
# Relancer le backend
uvicorn main:app --reload
```

---

## Notes pour la Prod

Avant déploiement:

1. **Vérifier RAPIDAPI_KEY** en production
2. **Activer les logs** (niveau INFO minimum)
3. **Monitorer les 422** - devraient être rares si mobile envoie bon format
4. **Monitorer les 502** - indiquent problème RapidAPI ou quota
5. **Alerter sur timeouts** - pourraient indiquer problème réseau

**Métriques à suivre:**
- Taux de 422 VoC (doit être < 1% si mobile OK)
- Taux de 422 Mansion (doit être < 1% si mobile OK)
- Taux de 502 (doit être < 0.1% en temps normal)
- P99 latency de RapidAPI (doit être < 3s)

---

## Résumé des Changements

### Avant:
- ❌ VoC et Mansion envoyaient payloads plats → RapidAPI 422 "missing datetime_location"
- ❌ Catch-all `except Exception` convertissait tout en 500
- ❌ Impossible de distinguer erreur payload vs erreur provider

### Après:
- ✅ VoC et Mansion transforment payloads plats → nested `datetime_location`
- ✅ Error handling granulaire: HTTPException re-raised, ValueError→422, Exception→500
- ✅ Logs détaillés avec exc_info pour debugging
- ✅ Tests complets (31 tests, tous passent)
- ✅ Garantie: jamais 500 pour payload invalide, toujours 422

---

## Contact

En cas de problème avec ce fix:
- Check logs backend: `/var/log/api/` ou stdout
- Check tests: `pytest tests/test_lunar_services.py -v`
- Check payload transformé dans les logs: "📤 Transformed ... payload for RapidAPI"
