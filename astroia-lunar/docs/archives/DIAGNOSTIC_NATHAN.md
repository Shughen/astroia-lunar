# Diagnostic - Position Lune de Nathan

## Contexte
- **Personne**: Nathan
- **Date de naissance**: 9 février 2001
- **Heure**: 11:30 (heure locale - Bordeaux)
- **Lieu**: Bordeaux (lat=44.8378, lon=-0.5792)
- **Problème rapporté**: La Lune est affichée en Lion dans le thème natal, alors qu'elle devrait être en Vierge selon Astrotheme

## Investigation

### 1. Vérification Swiss Ephemeris (Local)
✅ **Résultat**: Lune en **Virgo** (156.9°)
- Date/heure UTC: 2001-02-09 10:30:00 (11:30 Europe/Paris)
- Position: 6.9° dans le signe de la Vierge
- **Conforme à Astrotheme** ✅

### 2. Vérification RapidAPI
✅ **Résultat**: Lune en **Virgo** (Vir)
- Longitude absolue: 156.9°
- Degré dans le signe: 6.9°
- Maison: 5
- **RapidAPI calcule correctement** ✅

### 3. Recherche du passage Leo → Virgo
Le 9 février 2001, la Lune est en Vierge **TOUTE LA JOURNÉE**:
- 00:00 UTC: 150.26° (Virgo)
- 10:30 UTC (heure de Nathan): 156.90° (Virgo)
- 23:00 UTC: 164.73° (Virgo)

⚠️ **Conclusion**: Pour avoir la Lune en Lion, il faudrait:
- Le 8 février (jour avant)
- OU des données complètement incorrectes

## Cause Racine Probable

L'ancienne entrée en base de données a probablement été calculée avec:
1. **Date incorrecte** (8 février au lieu du 9)
2. **Mauvaises données de naissance** lors de la saisie initiale
3. **Ancienne version du code** avec un bug (corrigé depuis)

## Solution

### Option 1: Recalculer via l'API (Recommandé)

Appeler l'endpoint POST /api/natal-chart avec les bonnes données:

```bash
curl -X POST http://localhost:8000/api/natal-chart \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <TOKEN>" \
  -d '{
    "date": "2001-02-09",
    "time": "11:30",
    "latitude": 44.8378,
    "longitude": -0.5792,
    "place_name": "Bordeaux",
    "timezone": "Europe/Paris"
  }'
```

Cela écrasera l'ancienne entrée en base avec les bonnes données.

### Option 2: Mise à jour manuelle en base (Si nécessaire)

Si l'Option 1 ne fonctionne pas, vérifier et corriger directement en base:

```sql
-- 1. Vérifier l'entrée actuelle
SELECT id, user_id, birth_date, birth_time,
       positions->'moon' as moon_position
FROM natal_charts
WHERE birth_date = '2001-02-09';

-- 2. Si la date est incorrecte (8 février), la corriger
UPDATE natal_charts
SET birth_date = '2001-02-09',
    positions = positions || jsonb_build_object(
      'moon', jsonb_build_object(
        'sign', 'Virgo',
        'degree', 6.9,
        'house', 5
      )
    )
WHERE birth_date = '2001-02-08' AND user_id = <USER_ID>;
```

## Fichiers de test créés

1. `apps/api/scripts/test_nathan_moon.py` - Vérifie la position avec Swiss Ephemeris
2. `apps/api/scripts/test_nathan_rapidapi.py` - Teste l'appel RapidAPI
3. `apps/api/scripts/test_nathan_timezones.py` - Teste différentes timezones
4. `apps/api/scripts/test_moon_leo_virgo.py` - Recherche du passage Leo/Virgo
5. `apps/api/scripts/fix_nathan_moon.py` - Affiche les instructions de correction

## Validation

Après correction, vérifier que:
- ✅ Lune en Vierge (Virgo)
- ✅ Longitude ~156.9°
- ✅ Degré dans le signe ~6.9°
- ✅ Maison 5

## Prochaines étapes

1. **Immédiatement**: Recalculer le thème via l'API (Option 1)
2. **Vérification**: Consulter le thème dans l'app pour confirmer
3. **Si problème persiste**: Vérifier la base de données directement
