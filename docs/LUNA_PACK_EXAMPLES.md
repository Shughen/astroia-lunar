# 🌙 Luna Pack - Exemples d'Utilisation

Ce document contient des exemples pratiques d'utilisation des 3 fonctionnalités du **Luna Pack** (P1).

## 🎯 Fonctionnalités Luna Pack

Le Luna Pack est un trio de fonctionnalités différenciantes basées sur les cycles lunaires :

1. **Lunar Return Report** : Rapport mensuel complet de révolution lunaire
2. **Void of Course (VoC)** : Détection des fenêtres VoC avec alertes
3. **Lunar Mansions (28)** : Système des 28 mansions lunaires

---

## 📡 1. Lunar Return Report

Génère un rapport mensuel complet de révolution lunaire avec analyse détaillée.

### Endpoint
```
POST /api/lunar/return/report
```

### Exemple cURL

```bash
curl -X POST http://localhost:8000/api/lunar/return/report \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": 1,
    "month": "2025-01",
    "birth_date": "1989-04-15",
    "birth_time": "17:55",
    "latitude": 48.8566,
    "longitude": 2.3522,
    "timezone": "Europe/Paris",
    "date": "2025-01-15"
  }'
```

### Réponse attendue

```json
{
  "provider": "rapidapi",
  "kind": "lunar_return_report",
  "data": {
    "moon": {
      "sign": "Taurus",
      "degree": 15.3,
      "house": 2,
      "retrograde": false
    },
    "lunar_ascendant": "Virgo",
    "interpretation": {
      "summary": "Mois favorable aux finances et à la stabilité matérielle...",
      "themes": ["finances", "sécurité", "confort"],
      "challenges": ["rigidité", "possessivité"],
      "opportunities": ["investissements", "économies", "ancrage"]
    },
    "aspects": [
      {
        "planet1": "Moon",
        "planet2": "Venus",
        "aspect": "trine",
        "orb": 2.1,
        "interpretation": "Harmonie affective et créative"
      }
    ]
  },
  "cached": false
}
```

### Sauvegarde en DB

Si `user_id` et `month` sont fournis, le rapport est automatiquement sauvegardé dans la table `lunar_reports`.

### Récupération de l'historique

```bash
curl http://localhost:8000/api/lunar/return/report/history/1
```

---

## 🌑 2. Void of Course (VoC)

Obtient les informations sur les fenêtres Void of Course de la Lune.

### Endpoint
```
POST /api/lunar/voc
```

### Exemple cURL

```bash
curl -X POST http://localhost:8000/api/lunar/voc \
  -H "Content-Type: application/json" \
  -d '{
    "date": "2025-01-15",
    "time": "12:00",
    "latitude": 48.8566,
    "longitude": 2.3522,
    "timezone": "Europe/Paris"
  }'
```

### Réponse attendue

```json
{
  "provider": "rapidapi",
  "kind": "void_of_course",
  "data": {
    "is_void": true,
    "void_of_course": {
      "start": "2025-01-15T10:30:00+01:00",
      "end": "2025-01-15T14:45:00+01:00",
      "moon_sign_from": "Aries",
      "moon_sign_to": "Taurus",
      "last_aspect": {
        "planet": "Mars",
        "aspect": "square",
        "time": "2025-01-15T10:30:00+01:00"
      }
    },
    "recommendation": "Période peu propice aux nouvelles initiatives. Privilégier la réflexion et la consolidation.",
    "next_void": {
      "start": "2025-01-17T08:00:00+01:00",
      "end": "2025-01-17T11:30:00+01:00"
    }
  },
  "cached": false
}
```

### Vérifier le VoC actuel (depuis le cache)

```bash
curl http://localhost:8000/api/lunar/voc/current
```

Réponse si VoC actif :
```json
{
  "is_active": true,
  "start_at": "2025-01-15T10:30:00+01:00",
  "end_at": "2025-01-15T14:45:00+01:00",
  "source": { ... }
}
```

Réponse si pas de VoC actif :
```json
{
  "is_active": false
}
```

---

## 🏰 3. Lunar Mansions (28)

Obtient les informations sur la mansion lunaire du jour (système des 28 mansions).

### Endpoint
```
POST /api/lunar/mansion
```

### Exemple cURL

```bash
curl -X POST http://localhost:8000/api/lunar/mansion \
  -H "Content-Type: application/json" \
  -d '{
    "date": "2025-01-15",
    "time": "12:00",
    "latitude": 48.8566,
    "longitude": 2.3522,
    "timezone": "Europe/Paris"
  }'
```

### Réponse attendue

```json
{
  "provider": "rapidapi",
  "kind": "lunar_mansion",
  "data": {
    "mansion": {
      "number": 7,
      "name": "Al-Dhira (Les Deux Bras)",
      "name_arabic": "الذراع",
      "name_sanskrit": "Punarvasu",
      "degree_start": 93.0,
      "degree_end": 106.43,
      "constellation": "Gemini/Cancer"
    },
    "interpretation": {
      "summary": "Mansion favorable aux nouveaux projets et aux recommencements.",
      "themes": ["renouveau", "expansion", "générosité", "retour aux sources"],
      "favorable_for": [
        "Lancer un nouveau projet",
        "Reprendre contact avec d'anciens amis",
        "Voyager",
        "Enseigner"
      ],
      "unfavorable_for": [
        "Prêter de l'argent",
        "S'engager dans des contrats rigides"
      ],
      "deity": "Aditi (déesse de l'abondance)",
      "element": "Water",
      "nature": "Benefic"
    },
    "current_moon": {
      "longitude": 98.5,
      "sign": "Cancer",
      "degree_in_mansion": 5.5
    }
  },
  "cached": false
}
```

### Récupérer la mansion du jour (depuis le cache)

```bash
curl http://localhost:8000/api/lunar/mansion/today
```

Réponse si mansion en cache :
```json
{
  "date": "2025-01-15",
  "mansion_id": 7,
  "data": { ... },
  "cached": true
}
```

---

## 🧪 Tests Complets

### Script de test rapide (Bash)

```bash
#!/bin/bash

API_URL="http://localhost:8000"

echo "🌙 Test Luna Pack - Astroia Lunar"
echo "=================================="

# Test 1: Lunar Return Report
echo -e "\n1️⃣  Test Lunar Return Report..."
curl -s -X POST "$API_URL/api/lunar/return/report" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": 1,
    "month": "2025-01",
    "birth_date": "1989-04-15",
    "latitude": 48.8566,
    "longitude": 2.3522,
    "date": "2025-01-15"
  }' | jq '.kind, .data.moon.sign'

# Test 2: Void of Course
echo -e "\n2️⃣  Test Void of Course..."
curl -s -X POST "$API_URL/api/lunar/voc" \
  -H "Content-Type: application/json" \
  -d '{
    "date": "2025-01-15",
    "time": "12:00",
    "latitude": 48.8566,
    "longitude": 2.3522
  }' | jq '.kind, .data.is_void'

# Test 3: Lunar Mansion
echo -e "\n3️⃣  Test Lunar Mansion..."
curl -s -X POST "$API_URL/api/lunar/mansion" \
  -H "Content-Type: application/json" \
  -d '{
    "date": "2025-01-15",
    "latitude": 48.8566,
    "longitude": 2.3522
  }' | jq '.kind, .data.mansion.number, .data.mansion.name'

echo -e "\n✅ Tests terminés !"
```

Rendez le script exécutable :
```bash
chmod +x test_luna_pack.sh
./test_luna_pack.sh
```

---

## 📊 Tables de Base de Données

### lunar_reports
Stocke les rapports mensuels par utilisateur.

```sql
SELECT user_id, month, created_at 
FROM lunar_reports 
WHERE user_id = 1 
ORDER BY month DESC;
```

### lunar_voc_windows
Stocke les fenêtres Void of Course.

```sql
SELECT start_at, end_at, 
  (end_at - start_at) as duration
FROM lunar_voc_windows 
WHERE start_at >= NOW() 
ORDER BY start_at 
LIMIT 5;
```

### lunar_mansions_daily
Stocke la mansion du jour (cache).

```sql
SELECT date, mansion_id, 
  data->'mansion'->>'name' as mansion_name
FROM lunar_mansions_daily 
ORDER BY date DESC 
LIMIT 7;
```

---

## 🔍 Endpoints de Cache

### Vérifier le VoC actuel
```bash
curl http://localhost:8000/api/lunar/voc/current
```

### Récupérer la mansion du jour
```bash
curl http://localhost:8000/api/lunar/mansion/today
```

### Historique des rapports d'un utilisateur
```bash
curl http://localhost:8000/api/lunar/return/report/history/1
```

---

## ⚠️ Notes Importantes

### Chemins d'endpoints configurables
Les chemins RapidAPI sont configurables via variables d'environnement :
- `LUNAR_RETURN_REPORT_PATH`
- `VOID_OF_COURSE_PATH`
- `LUNAR_MANSIONS_PATH`

Voir `docs/ENV_CONFIGURATION.md` pour les détails.

### Gestion des erreurs
Tous les endpoints Luna Pack utilisent des **retries automatiques** avec exponential backoff :
- 3 tentatives maximum
- Gestion des erreurs 429 (rate limit) et 5xx (server errors)
- Timeout de 10 secondes par requête

### Consommation API
Chaque appel consomme 1 crédit RapidAPI. Utilisez les endpoints de cache (`/current`, `/today`) pour réduire la consommation.

---

## 🚀 Prochaines Étapes (P2+)

- **Transits** : Croisement avec thème natal et révolutions lunaires
- **Calendar** : Vue calendrier mensuel/annuel des phases et événements lunaires
- **Notifications** : Alertes VoC et événements lunaires importants
- **Rapports PDF** : Génération de rapports mensuels exportables

---

**Fait avec 🌙 par l'équipe Astroia**
