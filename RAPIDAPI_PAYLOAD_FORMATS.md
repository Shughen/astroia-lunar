# 📋 Formats de Payload RapidAPI - Validés

**Date de validation:** 11 novembre 2025  
**Source:** Playground RapidAPI officiel

---

## 🎯 Formats Corrects par Endpoint

### 1. ✅ Thème Natal

**Endpoint:** `/api/v3/charts/natal`

```json
{
  "subject": {
    "name": "Test",
    "birth_data": {
      "year": 1989,
      "month": 4,
      "day": 15,
      "hour": 17,
      "minute": 55,
      "timezone": "Europe/Paris",
      "latitude": 48.8566,
      "longitude": 2.3522
    }
  }
}
```

**cURL:**
```bash
curl -X POST http://localhost:8000/api/natal-chart/external \
  -H "Content-Type: application/json" \
  -d '{
    "subject": {
      "name": "Test",
      "birth_data": {
        "year": 1989,
        "month": 4,
        "day": 15,
        "hour": 17,
        "minute": 55,
        "timezone": "Europe/Paris",
        "latitude": 48.8566,
        "longitude": 2.3522
      }
    }
  }'
```

---

### 2. ✅ Lunar Mansions

**Endpoint:** `/api/v3/lunar/mansions`

```json
{
  "datetime_location": {
    "year": 2025,
    "month": 11,
    "day": 11,
    "hour": 19,
    "minute": 30,
    "second": 0,
    "city": "Paris",
    "country_code": "FR"
  },
  "system": "arabian_tropical",
  "days_ahead": 28
}
```

**cURL:**
```bash
curl -X POST http://localhost:8000/api/lunar/mansion \
  -H "Content-Type: application/json" \
  -d '{
    "datetime_location": {
      "year": 2025,
      "month": 11,
      "day": 11,
      "hour": 19,
      "minute": 30,
      "second": 0,
      "city": "Paris",
      "country_code": "FR"
    },
    "system": "arabian_tropical",
    "days_ahead": 28
  }'
```

---

### 3. ⚠️ Lunar Return Report

**Endpoint:** `/api/v3/analysis/lunar-return-report`

**Format attendu (à valider):**
```json
{
  "datetime_location": {
    "year": 2025,
    "month": 1,
    "day": 15,
    "hour": 12,
    "minute": 0,
    "second": 0,
    "city": "Paris",
    "country_code": "FR"
  },
  "birth_data": {
    "year": 1989,
    "month": 4,
    "day": 15,
    "hour": 17,
    "minute": 55,
    "timezone": "Europe/Paris",
    "latitude": 48.8566,
    "longitude": 2.3522
  }
}
```

---

### 4. ⚠️ Void of Course

**Endpoint:** `/api/v3/lunar/void-of-course`

**Format attendu (à valider):**
```json
{
  "datetime_location": {
    "year": 2025,
    "month": 11,
    "day": 11,
    "hour": 19,
    "minute": 30,
    "second": 0,
    "city": "Paris",
    "country_code": "FR"
  },
  "days_ahead": 7
}
```

---

### 5. ⚠️ Natal Transits

**Endpoint:** `/api/v3/charts/natal-transits`

**Format attendu (à valider):**
```json
{
  "subject": {
    "name": "Test",
    "birth_data": {
      "year": 1989,
      "month": 4,
      "day": 15,
      "hour": 17,
      "minute": 55,
      "timezone": "Europe/Paris",
      "latitude": 48.8566,
      "longitude": 2.3522
    }
  },
  "datetime_location": {
    "year": 2025,
    "month": 11,
    "day": 11,
    "hour": 19,
    "minute": 30,
    "second": 0,
    "city": "Paris",
    "country_code": "FR"
  }
}
```

---

## 🔑 Points Clés

### Différences avec le Format Initial

| Ancien Format | Nouveau Format RapidAPI |
|---------------|-------------------------|
| `"date": "YYYY-MM-DD"` | `year`, `month`, `day` séparés |
| `"time": "HH:MM"` | `hour`, `minute`, `second` séparés |
| `latitude`, `longitude` au root | Dans `datetime_location` avec `city` et `country_code` |
| `timezone` | Pas utilisé, remplacé par `city` + `country_code` |

### Structure Standard RapidAPI

Tous les endpoints utilisent la structure **`datetime_location`** :
```json
{
  "datetime_location": {
    "year": int,
    "month": int (1-12),
    "day": int (1-31),
    "hour": int (0-23),
    "minute": int (0-59),
    "second": int (0-59),
    "city": string,
    "country_code": string (ISO code)
  }
}
```

---

## 🛠️ TODO : Adapter les Autres Endpoints

Les formats ci-dessus pour VoC, LR Report, Transits sont **supposés** et doivent être validés dans le Playground RapidAPI.

**Recommandation:** Vérifier chaque endpoint dans le Playground pour obtenir le format exact.

---

**Testez maintenant le cURL Lunar Mansions ci-dessus !** 🚀

