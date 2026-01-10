# Manuel de Test - Lunar Return Report Fix (P1-BACKEND)

## Résumé des Corrections

**Problème:** L'endpoint `/api/lunar/return/report` renvoyait systématiquement 502 au lieu de 422 quand RapidAPI rejetait le payload avec "missing body.subject".

**Cause racine:**
1. Le payload envoyé à RapidAPI était plat (`birth_date`, `latitude`, etc.) au lieu d'être nested (`subject.birth_data`)
2. Les erreurs 422 de RapidAPI étaient systématiquement transformées en 502

**Corrections appliquées:**
1. ✅ Transformation automatique du payload plat → nested RapidAPI format
2. ✅ Mapping erreurs propre: 422→422, 400→400, 401/403→502, 5xx→502, timeout→504
3. ✅ Logs améliorés avec payload summary (sans PII)
4. ✅ Validation des champs requis (birth_date, latitude, longitude)
5. ✅ Tests complets (17 tests, tous passent)

---

## Fichiers Modifiés

| Fichier | Changements |
|---------|------------|
| `services/lunar_services.py` | Ajout transformation payload + validation |
| `services/rapidapi_client.py` | Mapping erreurs propre + logs détaillés |
| `routes/lunar.py` | Gestion ValueError → 422 |
| `tests/test_lunar_services.py` | 8 nouveaux tests (payload invalide, transformation, etc.) |

---

## Tests Unitaires (Automatisés)

**Exécuter les tests:**
```bash
cd apps/api
python -m pytest tests/test_lunar_services.py -v
```

**Résultats attendus:**
```
✅ 17 passed in 0.19s
```

**Tests couverts:**
- ✅ Payload valide avec tous les champs → 200
- ✅ Missing birth_date → ValueError
- ✅ Missing latitude → ValueError
- ✅ Missing longitude → ValueError
- ✅ Invalid birth_date format (15-04-1989) → ValueError
- ✅ Invalid birth_time format (5:30 PM) → ValueError
- ✅ Defaults appliqués (birth_time→12:00, timezone→UTC)
- ✅ RapidAPI 422 → 422 propagé (pas 502!)
- ✅ Transformation payload correcte (subject.birth_data nested)

---

## Test Manuel depuis Mobile

### Prérequis

1. **Backend en local:**
   ```bash
   cd apps/api
   uvicorn main:app --reload --port 8000
   ```

2. **Mobile pointant sur localhost:**
   - `.env` contient `EXPO_PUBLIC_API_URL=http://localhost:8000`
   - Ou sur iOS simulator: `http://localhost:8000`
   - Ou sur Android emulator: `http://10.0.2.2:8000`

3. **Variables d'environnement backend:**
   ```bash
   # apps/api/.env
   RAPIDAPI_KEY=votre_clé_rapidapi
   RAPIDAPI_HOST=best-astrology-api-natal-charts-transits-synastry.p.rapidapi.com
   BASE_RAPID_URL=https://best-astrology-api-natal-charts-transits-synastry.p.rapidapi.com
   ```

---

### Scénario 1: Payload Valide (Doit fonctionner)

**Action mobile:**
1. Aller dans l'onglet "Lunar Returns" (ou appeler directement l'API)
2. Envoyer une requête avec données complètes

**Payload attendu du mobile:**
```json
{
  "birth_date": "1989-04-15",
  "birth_time": "17:55",
  "latitude": 48.8566,
  "longitude": 2.3522,
  "timezone": "Europe/Paris",
  "city": "Paris",
  "country_code": "FR",
  "date": "2025-12-31",
  "month": "2025-12",
  "user_id": 1
}
```

**Vérifications backend:**

1. **Logs backend (terminal):**
   ```
   📝 Génération Lunar Return Report - user: 1, month: 2025-12
   📡 Appel RapidAPI: POST /api/v3/analysis/lunar-return-report | Payload: {
     'endpoint': '/api/v3/analysis/lunar-return-report',
     'has_subject': True,
     'has_birth_data': True,
     'fields': ['subject', 'return_month', 'return_date']
   }
   ✅ Réponse RapidAPI reçue (status 200, attempt 1)
   ✅ Lunar Return Report calculé avec succès
   ```

2. **Réponse mobile:**
   - Status: `200 OK`
   - Body: JSON avec les données du rapport lunaire

**Curl alternatif (si mobile pas dispo):**
```bash
curl -X POST http://localhost:8000/api/lunar/return/report \
  -H "Content-Type: application/json" \
  -d '{
    "birth_date": "1989-04-15",
    "birth_time": "17:55",
    "latitude": 48.8566,
    "longitude": 2.3522,
    "timezone": "Europe/Paris",
    "city": "Paris",
    "country_code": "FR",
    "date": "2025-12-31",
    "month": "2025-12",
    "user_id": 1
  }'
```

---

### Scénario 2: Payload Invalide - Missing birth_date (Doit échouer proprement)

**Action:**
Envoyer un payload sans `birth_date`

**Payload test:**
```bash
curl -X POST http://localhost:8000/api/lunar/return/report \
  -H "Content-Type: application/json" \
  -d '{
    "birth_time": "17:55",
    "latitude": 48.8566,
    "longitude": 2.3522,
    "date": "2025-12-31"
  }'
```

**Réponse attendue:**
- Status: `422 Unprocessable Entity`
- Body:
  ```json
  {
    "detail": {
      "code": "INVALID_PAYLOAD",
      "message": "Champs requis manquants: birth_date",
      "hint": "Vérifiez que birth_date (YYYY-MM-DD), birth_time (HH:MM), latitude, et longitude sont fournis"
    }
  }
  ```

**Logs backend:**
```
❌ Payload invalide: Champs requis manquants: birth_date
```

---

### Scénario 3: Payload Invalide - Wrong date format (Doit échouer proprement)

**Action:**
Envoyer `birth_date` au mauvais format (DD-MM-YYYY au lieu de YYYY-MM-DD)

**Payload test:**
```bash
curl -X POST http://localhost:8000/api/lunar/return/report \
  -H "Content-Type: application/json" \
  -d '{
    "birth_date": "15-04-1989",
    "birth_time": "17:55",
    "latitude": 48.8566,
    "longitude": 2.3522,
    "date": "2025-12-31"
  }'
```

**Réponse attendue:**
- Status: `422 Unprocessable Entity`
- Body contient soit:
  - ValueError local: `"Format birth_date invalide (attendu: YYYY-MM-DD)"`
  - Ou 422 de RapidAPI avec détails sur l'erreur de validation

**Logs backend:**
```
❌ Payload invalide: Format birth_date invalide (attendu: YYYY-MM-DD): 15-04-1989
```
OU (si le parsing passe mais RapidAPI rejette):
```
❌ Unprocessable Entity (422) de RapidAPI sur /api/v3/analysis/lunar-return-report: {...}
```

---

### Scénario 4: API RapidAPI Down (Simulation)

**Action:**
1. Arrêter momentanément la connexion internet
2. OU modifier temporairement `.env` avec une mauvaise RAPIDAPI_KEY
3. Envoyer un payload valide

**Payload test:**
```bash
curl -X POST http://localhost:8000/api/lunar/return/report \
  -H "Content-Type: application/json" \
  -d '{
    "birth_date": "1989-04-15",
    "birth_time": "17:55",
    "latitude": 48.8566,
    "longitude": 2.3522,
    "date": "2025-12-31"
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

**Réponse attendue (timeout réseau):**
- Status: `504 Gateway Timeout`
- Body:
  ```json
  {
    "detail": {
      "code": "PROVIDER_UNAVAILABLE",
      "message": "Timeout provider après 3 tentatives"
    }
  }
  ```

**Logs backend (avec retries):**
```
⚠️  Erreur 401 de RapidAPI sur /api/v3/analysis/lunar-return-report, retry 1/3 dans 0.52s
⚠️  Erreur 401 de RapidAPI sur /api/v3/analysis/lunar-return-report, retry 2/3 dans 1.08s
❌ Échec définitif après 3 tentatives: 401 - ...
```

---

## Checklist de Validation

Avant de considérer le fix comme validé:

- [ ] Tests unitaires passent (17/17)
- [ ] Payload valide → 200 OK avec données
- [ ] Missing birth_date → 422 avec message clair
- [ ] Missing latitude → 422 avec message clair
- [ ] Invalid date format → 422 avec message clair
- [ ] RapidAPI 422 → 422 propagé (PAS 502!)
- [ ] RapidAPI 500 → 502 après retries
- [ ] RapidAPI timeout → 504
- [ ] Logs contiennent payload summary (has_subject, has_birth_data)
- [ ] Logs ne contiennent PAS de PII (pas de birth_date en clair)

---

## Débogage

### Si tests échouent

**Vérifier les imports:**
```bash
cd apps/api
python -c "from services import lunar_services; print(lunar_services.__file__)"
```

**Vérifier la transformation:**
```python
from services.lunar_services import _transform_to_rapidapi_format

payload = {
    "birth_date": "1989-04-15",
    "birth_time": "17:55",
    "latitude": 48.8566,
    "longitude": 2.3522,
    "date": "2025-12-31"
}

result = _transform_to_rapidapi_format(payload)
print(result)
# Doit afficher: {'subject': {'name': 'User', 'birth_data': {...}}, ...}
```

### Si mobile reçoit toujours 502

1. **Vérifier les logs backend** - le payload envoyé contient-il `subject` ?
2. **Vérifier que le code est à jour** - relancer le backend (`uvicorn --reload`)
3. **Vérifier la réponse RapidAPI** - logs montrent-ils le status réel ?

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
git checkout HEAD~1 services/rapidapi_client.py
git checkout HEAD~1 routes/lunar.py
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
- Taux de 422 (doit être < 1% si mobile OK)
- Taux de 502 (doit être < 0.1% en temps normal)
- P99 latency de RapidAPI (doit être < 3s)

---

## Contact

En cas de problème avec ce fix:
- Check logs backend: `/var/log/api/` ou stdout
- Check tests: `pytest tests/test_lunar_services.py -v`
- Check payload transformé dans les logs: "📤 Transformed payload for RapidAPI"
