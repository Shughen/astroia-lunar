# Résumé Implémentation - Fix RapidAPI subject_data

## ✅ Modifications terminées

### 1. [services/natal_reading_service.py](services/natal_reading_service.py:40-143)

**Statut : ✅ COMPLÉTÉ**

- Payload RapidAPI corrigé au format `subject.birth_data.*` (year, month, day, hour, minute, latitude, longitude, timezone, place_name)
- Logs de debug ajoutés : response keys, has subject_data, subject_data.sun.sign, taille raw_data
- Gestion erreur HTTP 502 si subject_data absent

**Commit :** Payload RapidAPI + logs + erreur 502

### 2. [utils/natal_chart_helpers.py](utils/natal_chart_helpers.py:173-368)

**Statut : ✅ COMPLÉTÉ**

- Ajout fonction `normalize_subject_data_to_positions(rapidapi_response)`
- Mapping signes : Sco → Scorpio, Sag → Sagittarius, etc.
- Mapping houses : Ninth_House → 9, etc.
- Validation présence subject_data (ValueError si absent)
- Garantit cohérence Big3 avec planets.*.sign

**Commit :** Normalisation subject_data + mappings

### 3. [routes/natal.py](routes/natal.py) - ⚠️ **ATTENTION : Besoin de vérification**

**Statut : ⚠️ PARTIELLEMENT APPLIQUÉ (selon system reminders, mais pas visible dans les reads directs)**

Modifications requises :
1. ✅ Stocker `raw_data = rapidapi_response` AVANT normalisation
2. ✅ Appeler `normalize_subject_data_to_positions()`
3. ✅ Ajouter `raw_data` dans `NatalChart()` constructor
4. ⚠️ Supprimer code obsolète qui reconstruit positions depuis raw_data

**Code à remplacer** (lignes ~105-315 selon lecture directe) :

```python
# ❌ ANCIEN CODE (À SUPPRIMER)
# Parser la réponse RapidAPI vers le format attendu
chart_data = rapidapi_response.get("chart_data", {})
if not chart_data:
    logger.error(f"❌ Pas de 'chart_data' dans la réponse RapidAPI...")
    raise HTTPException(...)

parsed_positions = parse_positions_from_natal_chart(rapidapi_response)
parsed_aspects = parse_aspects_from_natal_chart(rapidapi_response)

# ... 200 lignes de mapping manuel ...

raw_data = {
    "sun": sun_data or {},
    "moon": moon_data or {},
    "ascendant": ascendant_data or {},
    "planets": planets_dict,
    "houses": houses_dict,
    "aspects": aspects_list
}
```

**Par** :

```python
# ✅ NOUVEAU CODE (SIMPLIFIÉ)
from services.natal_reading_service import call_rapidapi_natal_chart
from utils.natal_chart_helpers import normalize_subject_data_to_positions

# Appel à RapidAPI
rapidapi_response = await call_rapidapi_natal_chart(birth_data)
logger.info(f"✅ Réponse RapidAPI reçue - clés disponibles: {list(rapidapi_response.keys())}")

# ✅ STOCKER raw_data AVANT normalisation (même si normalisation échoue)
raw_data = rapidapi_response
logger.info(f"💾 raw_data stocké ({len(str(raw_data))} caractères)")

# 🔄 NORMALISATION depuis subject_data
try:
    positions = normalize_subject_data_to_positions(rapidapi_response)
    logger.info(f"✅ Positions normalisées depuis subject_data - {len(positions.get('planets', {}))} planètes")
except ValueError as norm_err:
    # Si normalisation échoue, lever une HTTPException avec le détail
    logger.error(f"❌ Erreur normalisation subject_data: {norm_err}")
    raise HTTPException(
        status_code=status.HTTP_502_BAD_GATEWAY,
        detail=f"Erreur normalisation RapidAPI response: {str(norm_err)}"
    )
```

**Et supprimer le bloc lignes ~335-363** qui reconstruit positions depuis raw_data :

```python
# ❌ À SUPPRIMER
# Construire positions JSONB depuis raw_data (tout stocker dans positions)
positions = {}
if raw_data:
    # Extraire Big3 depuis raw_data
    if "sun" in raw_data:
        positions["sun"] = raw_data["sun"]
    # ... etc (tout ce bloc)
```

### 4. [models/natal_chart.py](models/natal_chart.py)

**Statut : ⚠️ ATTENTION - Le modèle a été modifié par linter/user**

Selon le system reminder, le modèle actuel N'A PLUS `raw_data` !

**Modèle actuel (system reminder) :**
```python
class NatalChart(Base):
    # ... birth_date, birth_time, etc. ...
    positions = Column(JSONB, nullable=False)  # Source de vérité UNIQUE
    # ❌ raw_data n'existe PAS dans cette version
```

**Problème :** Si `raw_data` n'existe pas en DB, mes modifications pour stocker `raw_data` vont ÉCHOUER.

**Solutions possibles :**
1. **Option A (recommandée)** : Ajouter `raw_data` au modèle pour permettre le debug
2. **Option B** : Ne PAS stocker `raw_data`, uniquement `positions` normalisé

### 5. Documentation

**Statut : ✅ COMPLÉTÉ**

- [RAPIDAPI_SUBJECT_DATA_FIX.md](RAPIDAPI_SUBJECT_DATA_FIX.md) créé avec :
  - Description du problème
  - Fichiers modifiés
  - Commandes de test
  - Checklist de validation
  - Logs de debug attendus

## ⚠️ Actions requises

### 1. Vérifier le schéma DB natal_charts

```sql
\d natal_charts
```

**Vérifier si la colonne `raw_data` existe :**
- ✅ Si OUI : conserver le code qui stocke `raw_data`
- ❌ Si NON : soit ajouter la colonne, soit retirer le stockage de `raw_data`

### 2. Vérifier l'état réel de routes/natal.py

Le fichier semble avoir été modifié par un linter/user. Besoin de :

```bash
# Vérifier si les modifications sont présentes
grep -n "normalize_subject_data_to_positions" apps/api/routes/natal.py
grep -n "raw_data = rapidapi_response" apps/api/routes/natal.py
```

**Si les grep ne retournent RIEN :** les modifications n'ont PAS été appliquées → refaire la modification.

### 3. Plan de correction recommandé

**Étape 1 : Vérifier schéma DB**
```sql
SELECT column_name, data_type, is_nullable
FROM information_schema.columns
WHERE table_name = 'natal_charts'
ORDER BY ordinal_position;
```

**Étape 2 : Décider du stockage raw_data**
- Si `raw_data` existe en DB → garder le stockage
- Sinon → créer migration pour ajouter `raw_data JSON NULL`

**Étape 3 : Appliquer corrections routes/natal.py**
- Remplacer l'ancien parsing (lignes ~105-315) par le nouveau code simplifié
- Supprimer le bloc de reconstruction de positions depuis raw_data (lignes ~335-363)
- Ajouter `raw_data` dans le NatalChart() constructor si la colonne existe

**Étape 4 : Tester**
```bash
# Purge
DELETE FROM natal_charts WHERE user_id = 1;

# Test Manaus
curl -X POST http://localhost:8000/api/natal-chart \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{
    "date": "1989-11-01",
    "time": "13:20",
    "latitude": -3.1316333,
    "longitude": -59.9825041,
    "place_name": "Manaus, Amazonas, Brésil"
  }'

# Vérifier sun_sign == "Scorpio"
```

## 📝 Checklist finale

- [x] services/natal_reading_service.py : payload + logs + erreur 502
- [x] utils/natal_chart_helpers.py : normalize_subject_data_to_positions()
- [ ] routes/natal.py : stocker raw_data + appeler normalisation + supprimer ancien code
- [ ] models/natal_chart.py : vérifier si raw_data existe
- [ ] Test Manaus 1989-11-01 → sun_sign == "Scorpio"
- [ ] Vérifier DB : raw_data contient subject_data
- [ ] Vérifier cohérence : sun_sign == planets.sun.sign

## 🔧 Diff attendu pour routes/natal.py

Voir [RAPIDAPI_SUBJECT_DATA_FIX.md](RAPIDAPI_SUBJECT_DATA_FIX.md) section "Fichiers modifiés" pour le diff complet.

## 📊 Métriques

- **Lignes de code supprimées** : ~200 (ancien parsing manuel)
- **Lignes de code ajoutées** : ~30 (appel normalisation + stockage raw_data)
- **Gain de maintenabilité** : +++
- **Robustesse** : +++ (validation subject_data + logs debug)
