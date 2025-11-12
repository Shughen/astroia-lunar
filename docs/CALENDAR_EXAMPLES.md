# 📅 Calendrier Lunaire - Exemples d'Utilisation

Ce document contient des exemples pratiques d'utilisation des fonctionnalités de **Calendrier Lunaire** (P3).

## 🎯 Fonctionnalités Calendrier

Le module Calendrier Lunaire offre:

1. **Lunar Phases** : Phases lunaires précises (nouvelles/pleines lunes, quartiers)
2. **Lunar Events** : Événements spéciaux (éclipses, superlunes, microlunes)
3. **Lunar Calendar Year** : Calendrier complet annuel
4. **Monthly Calendar** : Vue mensuelle combinée (phases + mansions + événements)

---

## 🌓 1. Phases Lunaires

Obtient les dates et heures exactes des phases lunaires pour une période donnée.

### Endpoint
```
POST /api/calendar/phases
```

### Exemple cURL

```bash
curl -X POST http://localhost:8000/api/calendar/phases \
  -H "Content-Type: application/json" \
  -d '{
    "start_date": "2025-01-01",
    "end_date": "2025-01-31",
    "latitude": 48.8566,
    "longitude": 2.3522,
    "timezone": "Europe/Paris"
  }'
```

### Réponse attendue

```json
{
  "provider": "rapidapi",
  "kind": "lunar_phases",
  "data": {
    "phases": [
      {
        "date": "2025-01-13",
        "time": "05:27:00",
        "type": "full_moon",
        "illumination": 100.0,
        "sign": "Cancer",
        "degree": 23.45
      },
      {
        "date": "2025-01-21",
        "time": "12:31:00",
        "type": "last_quarter",
        "illumination": 50.0,
        "sign": "Scorpio",
        "degree": 1.23
      },
      {
        "date": "2025-01-29",
        "time": "12:36:00",
        "type": "new_moon",
        "illumination": 0.0,
        "sign": "Aquarius",
        "degree": 9.12
      }
    ]
  },
  "cached": false
}
```

---

## 🌒 2. Événements Lunaires Spéciaux

Obtient les événements astronomiques remarquables (éclipses, superlunes, etc.).

### Endpoint
```
POST /api/calendar/events
```

### Exemple cURL

```bash
curl -X POST http://localhost:8000/api/calendar/events \
  -H "Content-Type: application/json" \
  -d '{
    "start_date": "2025-01-01",
    "end_date": "2025-12-31",
    "latitude": 48.8566,
    "longitude": 2.3522,
    "event_types": ["eclipse", "supermoon"]
  }'
```

### Réponse attendue

```json
{
  "provider": "rapidapi",
  "kind": "lunar_events",
  "data": {
    "events": [
      {
        "date": "2025-03-14",
        "time": "06:55:00",
        "type": "eclipse",
        "title": "Éclipse lunaire totale",
        "description": "Éclipse totale visible en Europe, Afrique et Asie",
        "magnitude": 1.18,
        "duration_minutes": 65,
        "visibility": {
          "europe": "totale",
          "americas": "partielle",
          "asia": "totale"
        }
      },
      {
        "date": "2025-06-13",
        "time": "22:00:00",
        "type": "supermoon",
        "title": "Superlune de juin",
        "description": "La Lune au périgée, apparaît 14% plus grande",
        "distance_km": 357800,
        "apparent_size": 33.5
      }
    ]
  },
  "cached": false
}
```

---

## 📅 3. Calendrier Annuel

Obtient le calendrier lunaire complet pour une année entière.

### Endpoint
```
POST /api/calendar/year
```

### Exemple cURL

```bash
curl -X POST http://localhost:8000/api/calendar/year \
  -H "Content-Type: application/json" \
  -d '{
    "year": 2025,
    "latitude": 48.8566,
    "longitude": 2.3522,
    "timezone": "Europe/Paris"
  }'
```

### Réponse attendue

```json
{
  "provider": "rapidapi",
  "kind": "lunar_calendar_year",
  "data": {
    "year": 2025,
    "new_moons": 12,
    "full_moons": 13,
    "eclipses": 2,
    "supermoons": 3,
    "micromoons": 2,
    "calendar": [
      {
        "month": "January",
        "new_moon": "2025-01-29",
        "full_moon": "2025-01-13",
        "special_events": []
      },
      {
        "month": "March",
        "new_moon": "2025-03-29",
        "full_moon": "2025-03-14",
        "special_events": ["eclipse"]
      }
    ]
  },
  "cached": false
}
```

---

## 🗓️ 4. Calendrier Mensuel Combiné

Génère un calendrier mensuel avec phases, mansions et événements combinés.

### Endpoint
```
GET /api/calendar/month?year=2025&month=1
```

### Exemple cURL

```bash
curl "http://localhost:8000/api/calendar/month?year=2025&month=1&latitude=48.8566&longitude=2.3522"
```

### Réponse attendue

```json
{
  "year": 2025,
  "month": 1,
  "days": [
    {
      "date": "2025-01-13",
      "day_of_week": "Monday",
      "phases": ["full_moon"],
      "mansion": {
        "id": 12,
        "name": "Al-Sarfah"
      },
      "events": [],
      "lunar_day": 15
    },
    {
      "date": "2025-01-29",
      "day_of_week": "Wednesday",
      "phases": ["new_moon"],
      "mansion": {
        "id": 28,
        "name": "Al-Risha"
      },
      "events": ["supermoon"],
      "lunar_day": 1
    }
  ],
  "summary": {
    "new_moons": 1,
    "full_moons": 1,
    "eclipses": 0,
    "special_events": 1
  }
}
```

---

## 🧪 Tests Complets

### Script de test rapide (Bash)

```bash
#!/bin/bash

API_URL="http://localhost:8000"

echo "📅 Test Calendrier Lunaire - Astroia Lunar"
echo "========================================="

# Test 1: Phases lunaires
echo -e "\n1️⃣  Test Lunar Phases (janvier 2025)..."
curl -s -X POST "$API_URL/api/calendar/phases" \
  -H "Content-Type: application/json" \
  -d '{
    "start_date": "2025-01-01",
    "end_date": "2025-01-31",
    "latitude": 48.8566,
    "longitude": 2.3522
  }' | jq '.kind, .data.phases | length'

# Test 2: Événements lunaires
echo -e "\n2️⃣  Test Lunar Events (année 2025)..."
curl -s -X POST "$API_URL/api/calendar/events" \
  -H "Content-Type: application/json" \
  -d '{
    "start_date": "2025-01-01",
    "end_date": "2025-12-31"
  }' | jq '.kind, .data.events | length'

# Test 3: Calendrier annuel
echo -e "\n3️⃣  Test Lunar Calendar Year (2025)..."
curl -s -X POST "$API_URL/api/calendar/year" \
  -H "Content-Type: application/json" \
  -d '{
    "year": 2025
  }' | jq '.kind, .data.year, .data.new_moons, .data.eclipses'

# Test 4: Calendrier mensuel
echo -e "\n4️⃣  Test Monthly Calendar (janvier 2025)..."
curl -s "$API_URL/api/calendar/month?year=2025&month=1" \
  | jq '.year, .month, .summary'

echo -e "\n✅ Tests terminés !"
```

---

## 📊 Tables de Base de Données

### lunar_phases
Stocke les phases lunaires en cache.

```sql
SELECT date, phase_type, time, illumination/100.0 as illumination_pct
FROM lunar_phases 
WHERE date >= '2025-01-01' AND date < '2025-02-01'
ORDER BY date;
```

### lunar_events
Stocke les événements lunaires spéciaux.

```sql
SELECT date, event_type, title, description
FROM lunar_events 
WHERE date >= NOW() 
ORDER BY date 
LIMIT 10;
```

---

## 🔍 Use Cases

### Trouver la prochaine Nouvelle Lune
```sql
SELECT date, time 
FROM lunar_phases 
WHERE phase_type = 'new_moon' 
  AND date >= CURRENT_DATE 
ORDER BY date 
LIMIT 1;
```

### Lister toutes les éclipses de 2025
```sql
SELECT date, title, description, meta->>'magnitude' as magnitude
FROM lunar_events 
WHERE event_type = 'eclipse' 
  AND EXTRACT(YEAR FROM date) = 2025 
ORDER BY date;
```

### Statistiques mensuelles
```sql
SELECT 
  EXTRACT(MONTH FROM date) as month,
  COUNT(*) FILTER (WHERE phase_type = 'new_moon') as new_moons,
  COUNT(*) FILTER (WHERE phase_type = 'full_moon') as full_moons
FROM lunar_phases 
WHERE EXTRACT(YEAR FROM date) = 2025 
GROUP BY month 
ORDER BY month;
```

---

## ⚠️ Notes Importantes

### Chemins d'endpoints configurables
Les chemins RapidAPI sont configurables via variables d'environnement :
- `LUNAR_PHASES_PATH`
- `LUNAR_EVENTS_PATH`
- `LUNAR_CALENDAR_YEAR_PATH`

Voir `docs/ENV_CONFIGURATION.md` pour les détails.

### Cache automatique
Les phases et événements sont automatiquement mis en cache en DB lors des requêtes. Cela permet:
- Réduction de la consommation API
- Requêtes SQL rapides pour calendriers mensuels
- Analytics et statistiques

### Formats de dates
- Toutes les dates sont au format **ISO 8601** : `YYYY-MM-DD`
- Les heures sont au format **HH:MM:SS**
- Les timezones sont gérées via le paramètre `timezone`

---

**Fait avec 🌙 par l'équipe Astroia**

