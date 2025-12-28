# Fix: Gestion EPHEMERIS_API_KEY placeholder + Mode Mock DEV

**Date:** 2025-01-XX  
**Problème:** `EPHEMERIS_API_KEY=__TO_FILL_LATER__` était traité comme une vraie valeur, provoquant des erreurs `Illegal header value b'Bearer __TO_FILL_LATER__'`.

---

## ✅ Solution implémentée

### 1. Helper de validation des clés API

**Fichier:** `apps/api/utils/api_key_validator.py`

Détecte les placeholders courants :
- `__TO_FILL_LATER__`
- `TO_FILL_LATER`
- `changeme`
- `xxx`
- `your_key_here`
- `placeholder`
- etc.

**Fonction :** `is_configured_api_key(value: Optional[str]) -> bool`

### 2. Client Ephemeris amélioré

**Fichier:** `apps/api/services/ephemeris.py`

- Validation de la clé avant chaque appel API
- Exception `EphemerisAPIKeyError` si clé invalide
- Support mode mock DEV (si `DEV_MOCK_EPHEMERIS=1`)

### 3. Mode Mock DEV

**Fichier:** `apps/api/utils/ephemeris_mock.py`

Génère des données astrologiques minimales (fake) pour permettre les tests sans clé API :
- Thème natal mock (Sun, Moon, Ascendant calculés approximativement)
- Révolution lunaire mock (basée sur les données natales)

### 4. Route natal.py mise à jour

**Fichier:** `apps/api/routes/natal.py`

- Capture `EphemerisAPIKeyError` et retourne HTTP 503 propre
- Message d'erreur clair suggérant `DEV_MOCK_EPHEMERIS=1`

---

## 🧪 Utilisation

### Option A : Bloquer proprement (production)

Dans `.env` :

```env
# Clé vide ou placeholder → retourne 503
EPHEMERIS_API_KEY=
# ou
EPHEMERIS_API_KEY=__TO_FILL_LATER__
```

**Comportement :**
- `POST /api/natal-chart` → HTTP 503
- Message : "EPHEMERIS_API_KEY missing or placeholder. Configure it to compute natal charts."

### Option B : Mode Mock DEV (développement)

Dans `.env` :

```env
# Clé vide/placeholder + mode mock activé
EPHEMERIS_API_KEY=
DEV_MOCK_EPHEMERIS=1
```

**Comportement :**
- `POST /api/natal-chart` → HTTP 201 (génère des données fake)
- `POST /api/lunar-returns/generate` → HTTP 201 (génère des données fake)
- Logs : "🎭 MODE MOCK DEV - Génération données fake..."

**⚠️ Important :** Les données sont **fake** et ne doivent pas être utilisées en production.

### Option C : Vraie clé API (production)

Dans `.env` :

```env
EPHEMERIS_API_KEY=ta_vraie_cle_ici
```

**Comportement :**
- Appels réels à l'API Ephemeris
- Données réelles calculées

---

## 📝 Test curl

### Test 1 : Clé placeholder (503 attendu)

```bash
# .env: EPHEMERIS_API_KEY=__TO_FILL_LATER__

curl -X POST "http://127.0.0.1:8000/api/natal-chart" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "date": "1990-05-15",
    "time": "14:30",
    "latitude": 48.8566,
    "longitude": 2.3522,
    "place_name": "Paris, France",
    "timezone": "Europe/Paris"
  }' | jq
```

**Réponse attendue :**
```json
{
  "detail": "EPHEMERIS_API_KEY missing or placeholder. Configure it to compute natal charts."
}
```
**Code HTTP :** `503 SERVICE_UNAVAILABLE`

### Test 2 : Mode Mock DEV (201 attendu)

```bash
# .env: EPHEMERIS_API_KEY= + DEV_MOCK_EPHEMERIS=1

curl -X POST "http://127.0.0.1:8000/api/natal-chart" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "date": "1990-05-15",
    "time": "14:30",
    "latitude": 48.8566,
    "longitude": 2.3522,
    "place_name": "Paris, France",
    "timezone": "Europe/Paris"
  }' | jq '{id, sun_sign, moon_sign, ascendant}'
```

**Réponse attendue :**
```json
{
  "id": 1,
  "sun_sign": "Taurus",
  "moon_sign": "Aries",
  "ascendant": "Pisces"
}
```
**Code HTTP :** `201 CREATED`

**Dans les logs :**
```
WARNING - 🎭 MODE MOCK DEV - Génération données fake pour date=1990-05-15 14:30
INFO - ✅ Thème natal calculé via Ephemeris API - clés disponibles: ['sun', 'moon', 'ascendant', ...]
```

---

## 📊 Données Mock générées

### Thème Natal Mock

Basé sur :
- **Sun sign** : Mois de naissance (1→Capricorn, 5→Taurus, etc.)
- **Moon sign** : Jour de naissance (rotation sur 12 signes)
- **Ascendant** : Heure de naissance (rotation sur 12 signes)
- **Degrés** : Calculs approximatifs basés sur jour/heure

**Structure :**
```json
{
  "sun": {
    "sign": "Taurus",
    "degree": 15.48,
    "absolute_longitude": 135.48
  },
  "moon": {
    "sign": "Aries",
    "degree": 17.5,
    "absolute_longitude": 17.5,
    "house": 15
  },
  "ascendant": {
    "sign": "Pisces",
    "degree": 14.5
  },
  "planets": {...},
  "houses": {...},
  "aspects": [...]
}
```

### Révolution Lunaire Mock

Basé sur :
- **Moon sign/degree** : Reprend les données natales
- **Ascendant** : Basé sur le mois cible
- **Return datetime** : 15 du mois à 12:00

---

## ✅ Checklist

- [x] Helper `is_configured_api_key` détecte les placeholders
- [x] Client Ephemeris valide la clé avant appel
- [x] Exception `EphemerisAPIKeyError` levée si clé invalide
- [x] Route natal.py retourne HTTP 503 propre
- [x] Mode mock DEV génère des données minimales
- [x] Mode mock DEV activable via `DEV_MOCK_EPHEMERIS=1`
- [x] Logs explicites (mock vs réel)
- [x] Documentation claire

---

## 🔧 Configuration recommandée

### Développement

```env
# .env (dev)
EPHEMERIS_API_KEY=
DEV_MOCK_EPHEMERIS=1
```

### Production

```env
# .env (prod)
EPHEMERIS_API_KEY=vraie_cle_secrete
DEV_MOCK_EPHEMERIS=0  # ou omis
```

---

## 🚀 Prochaines étapes

Une fois la clé API configurée ou le mode mock activé :
1. ✅ Tester création natal_chart
2. ✅ Tester génération lunar returns
3. → Continuer avec l'implémentation V2

