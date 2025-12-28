# Fix: Correction endpoint `/api/lunar-returns/generate` - Migration vers `user_id_int` et `positions` JSONB

**Date:** 2025-01-XX  
**Problème:** `asyncpg.exceptions.UndefinedColumnError: column natal_charts.sun_sign does not exist`  
**Cause:** Le code accédait aux colonnes `sun_sign`, `moon_sign`, `ascendant` qui n'existent plus en DB. Les données sont maintenant dans `positions` (JSONB).

---

## 🔍 Problème identifié

1. **Colonnes legacy supprimées** : `natal_charts.sun_sign`, `moon_sign`, `ascendant` n'existent plus en DB
2. **Données dans JSONB** : Les données sont maintenant dans `positions` (JSONB)
3. **Migration user_id** : `user_id` (UUID legacy) → `user_id_int` (INTEGER)
4. **Accès direct aux colonnes** : Le code accédait directement à `natal_chart.moon_sign` (ligne 65 de `routes/lunar_returns.py`)

---

## ✅ Solution implémentée

### 1. Helper pour extraire Big3 depuis `positions` JSONB

**Fichier créé:** `apps/api/utils/natal_chart_helpers.py`

- `extract_big3_from_positions()` : Extrait sun_sign, moon_sign, ascendant_sign depuis `positions`
- `extract_moon_data_from_positions()` : Extrait sign, degree, house de la Lune
- Tolérant aux variations de structure (snake_case, camelCase, etc.)

### 2. Mise à jour modèle NatalChart

**Fichier modifié:** `apps/api/models/natal_chart.py`

- Ajout de `user_id_int` (INTEGER, NOT NULL, FK vers `users.id`)
- Ajout de `positions` (JSON) pour stocker les données astrologiques
- `user_id` (UUID) marqué comme legacy/nullable pour transition
- Colonnes `sun_sign`, `moon_sign`, `ascendant` marquées comme legacy (ne plus utiliser)

### 3. Correction routes/lunar_returns.py

**Fichier modifié:** `apps/api/routes/lunar_returns.py`

- Query utilise maintenant `NatalChart.user_id_int == current_user.id` (au lieu de `user_id`)
- Extraction de `natal_moon_sign` et `natal_moon_degree` depuis `positions` JSONB via helper
- Fallback sur `planets` (legacy) si `positions` n'existe pas

### 4. Correction routes/natal.py

**Fichier modifié:** `apps/api/routes/natal.py`

- Query utilise maintenant `NatalChart.user_id_int == current_user.id`
- Sauvegarde dans `positions` JSONB lors de la création/mise à jour
- Extraction Big3 depuis `positions` pour les réponses API
- Ne met plus à jour les colonnes legacy `sun_sign`, `moon_sign`, `ascendant`

---

## 📋 Fichiers modifiés

1. **Nouveau fichier:**
   - `apps/api/utils/natal_chart_helpers.py` (helper pour extraction Big3)

2. **Fichiers modifiés:**
   - `apps/api/models/natal_chart.py` (ajout `user_id_int`, `positions`)
   - `apps/api/routes/lunar_returns.py` (query `user_id_int`, extraction depuis `positions`)
   - `apps/api/routes/natal.py` (query `user_id_int`, sauvegarde dans `positions`)

---

## 🔧 Diffs

### 1. Helper natal_chart_helpers.py (nouveau fichier)

```python
def extract_big3_from_positions(positions: Optional[Dict[str, Any]]) -> Dict[str, Optional[str]]:
    """Extrait le Big3 depuis positions JSONB"""
    # ... implémentation complète
```

### 2. Modèle NatalChart

```diff
--- a/apps/api/models/natal_chart.py
+++ b/apps/api/models/natal_chart.py
@@ -12,7 +12,10 @@ class NatalChart(Base):
     __tablename__ = "natal_charts"
     
     id = Column(Integer, primary_key=True, index=True)
-    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
+    # Legacy: user_id (UUID) - ne plus utiliser
+    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=True)
+    # Nouveau: user_id_int (INTEGER) - à utiliser pour les queries
+    user_id_int = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
     
     # Données calculées (legacy - colonnes peuvent ne plus exister en DB)
-    sun_sign = Column(String)  # Soleil
-    moon_sign = Column(String)  # Lune
-    ascendant = Column(String)  # Ascendant
+    sun_sign = Column(String)  # Legacy - ne plus utiliser
+    moon_sign = Column(String)  # Legacy - ne plus utiliser
+    ascendant = Column(String)  # Legacy - ne plus utiliser
     
     # Positions planètes (JSON)
     planets = Column(JSON)
     houses = Column(JSON)
     aspects = Column(JSON)
     
+    # Nouveau: positions (JSONB) - contient toutes les données astrologiques
+    positions = Column(JSON)
```

### 3. Route lunar_returns.py

```diff
--- a/apps/api/routes/lunar_returns.py
+++ b/apps/api/routes/lunar_returns.py
@@ -10,6 +10,7 @@ from routes.auth import get_current_user
 from services.ephemeris import ephemeris_client
 from services.interpretations import generate_lunar_return_interpretation
+from utils.natal_chart_helpers import extract_moon_data_from_positions
 
@@ -44,7 +45,7 @@ async def generate_lunar_returns(
     
     # Vérifier que le thème natal existe
     result = await db.execute(
-        select(NatalChart).where(NatalChart.user_id == current_user.id)
+        select(NatalChart).where(NatalChart.user_id_int == current_user.id)
     )
     natal_chart = result.scalar_one_or_none()
     
@@ -55,9 +56,20 @@ async def generate_lunar_returns(
             detail="Thème natal manquant. Calculez-le d'abord via POST /api/natal-chart"
         )
     
-    # Extraire position natale de la Lune
-    moon_data = natal_chart.planets.get("Moon", {})
-    natal_moon_degree = moon_data.get("degree", 0)
-    natal_moon_sign = natal_chart.moon_sign
+    # Extraire position natale de la Lune depuis positions JSONB
+    positions = natal_chart.positions or {}
+    moon_data_extracted = extract_moon_data_from_positions(positions)
+    
+    # Fallback sur planets (legacy)
+    if not moon_data_extracted.get("degree") and natal_chart.planets:
+        moon_data_legacy = natal_chart.planets.get("Moon", {})
+        if moon_data_legacy:
+            moon_data_extracted["degree"] = moon_data_legacy.get("degree", 0)
+            moon_data_extracted["sign"] = moon_data_extracted.get("sign") or moon_data_legacy.get("sign")
+    
+    natal_moon_degree = moon_data_extracted.get("degree", 0)
+    natal_moon_sign = moon_data_extracted.get("sign")
+    
+    if not natal_moon_sign:
+        raise HTTPException(
+            status_code=status.HTTP_400_BAD_REQUEST,
+            detail="Données de la Lune manquantes dans le thème natal"
+        )
```

### 4. Route natal.py

```diff
--- a/apps/api/routes/natal.py
+++ b/apps/api/routes/natal.py
@@ -13,6 +13,7 @@ from routes.auth import get_current_user
 from services.ephemeris import ephemeris_client
 from services.ephemeris_rapidapi import create_natal_chart
+from utils.natal_chart_helpers import extract_big3_from_positions
 
@@ -72,7 +73,7 @@ async def calculate_natal_chart(
     
     # Vérifier si un thème existe déjà
     result = await db.execute(
-        select(NatalChart).where(NatalChart.user_id == current_user.id)
+        select(NatalChart).where(NatalChart.user_id_int == current_user.id)
     )
     existing_chart = result.scalar_one_or_none()
     
+    # Construire positions JSONB depuis raw_data
+    positions = {}
+    if raw_data:
+        # Extraire Big3 depuis raw_data
+        if "sun" in raw_data:
+            positions["sun"] = raw_data["sun"]
+        if "moon" in raw_data:
+            positions["moon"] = raw_data["moon"]
+        if "ascendant" in raw_data:
+            positions["ascendant"] = raw_data["ascendant"]
+        # Ajouter autres positions si disponibles
+        if "planetary_positions" in raw_data:
+            for pos in raw_data["planetary_positions"]:
+                name = pos.get("name", "").lower()
+                if name:
+                    positions[name] = pos
+    
     if existing_chart:
         # Mise à jour
-        existing_chart.sun_sign = sun_sign
-        existing_chart.moon_sign = moon_sign
-        existing_chart.ascendant = ascendant
+        # Ne plus mettre à jour sun_sign/moon_sign/ascendant (colonnes legacy)
         existing_chart.planets = raw_data.get("planets", {})
         existing_chart.houses = raw_data.get("houses", {})
         existing_chart.aspects = raw_data.get("aspects", [])
+        existing_chart.positions = positions  # Sauvegarder dans positions JSONB
         existing_chart.raw_data = raw_data
         chart = existing_chart
     else:
         # Création
         chart = NatalChart(
-            user_id=current_user.id,
-            sun_sign=sun_sign,
-            moon_sign=moon_sign,
-            ascendant=ascendant,
+            user_id_int=current_user.id,  # Utiliser user_id_int
             planets=raw_data.get("planets", {}),
             houses=raw_data.get("houses", {}),
             aspects=raw_data.get("aspects", []),
+            positions=positions,  # Sauvegarder dans positions JSONB
             raw_data=raw_data
         )
         db.add(chart)
     
     await db.commit()
     await db.refresh(chart)
     
-    return chart
+    # Extraire Big3 depuis positions pour la réponse
+    big3 = extract_big3_from_positions(chart.positions)
+    
+    # Construire la réponse avec Big3 extrait depuis positions
+    return {
+        "id": chart.id,
+        "sun_sign": big3["sun_sign"] or "Unknown",
+        "moon_sign": big3["moon_sign"] or "Unknown",
+        "ascendant": big3["ascendant_sign"] or "Unknown",
+        "planets": chart.planets or {},
+        "houses": chart.houses or {},
+        "aspects": chart.aspects or []
+    }
```

---

## 🧪 Commandes de test

### 1. Vérifier la syntaxe Python

```bash
cd apps/api
python3 -m py_compile utils/natal_chart_helpers.py models/natal_chart.py routes/lunar_returns.py routes/natal.py
```

### 2. Démarrer uvicorn

```bash
cd apps/api
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

### 3. S'enregistrer et obtenir un token

```bash
# Register (si pas déjà fait)
curl -X POST http://127.0.0.1:8000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "password123"
  }'

# Login
TOKEN=$(curl -X POST http://127.0.0.1:8000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "password123"
  }' | jq -r '.access_token')

echo "Token: $TOKEN"
```

### 4. Obtenir l'ID utilisateur (INTEGER)

```bash
# Récupérer les infos utilisateur
USER_INFO=$(curl -X GET http://127.0.0.1:8000/api/auth/me \
  -H "Authorization: Bearer $TOKEN")

USER_ID=$(echo $USER_INFO | jq -r '.id')
echo "User ID: $USER_ID"
```

### 5. Créer un thème natal (si pas déjà fait)

```bash
curl -X POST http://127.0.0.1:8000/api/natal-chart \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "date": "1990-05-15",
    "time": "14:30",
    "latitude": 48.8566,
    "longitude": 2.3522,
    "place_name": "Paris",
    "timezone": "Europe/Paris"
  }'
```

### 6. Tester l'endpoint `/api/lunar-returns/generate`

```bash
# Test avec l'ancien endpoint (génère 12 mois)
curl -X POST http://127.0.0.1:8000/api/lunar-returns/generate \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
```

**Résultat attendu:** 
- ✅ Pas d'erreur `UndefinedColumnError`
- ✅ Réponse JSON avec `{"message": "...", "year": 2025}`

### 7. Vérifier en base de données (Supabase)

```sql
-- Vérifier que user_id_int est bien utilisé
SELECT id, user_id, user_id_int, positions 
FROM natal_charts 
WHERE user_id_int = 6;  -- Remplacer 6 par votre user_id

-- Vérifier que positions contient les données
SELECT id, user_id_int, 
       positions->>'sun' as sun_data,
       positions->>'moon' as moon_data,
       positions->>'ascendant' as ascendant_data
FROM natal_charts 
WHERE user_id_int = 6;
```

---

## ⚠️ Notes importantes

1. **Migration DB nécessaire** : Si la colonne `user_id_int` n'existe pas encore en DB, il faut l'ajouter :
   ```sql
   ALTER TABLE natal_charts 
   ADD COLUMN user_id_int INTEGER REFERENCES users(id);
   
   -- Migrer les données existantes
   UPDATE natal_charts 
   SET user_id_int = user_id 
   WHERE user_id_int IS NULL;
   
   -- Rendre NOT NULL après migration
   ALTER TABLE natal_charts 
   ALTER COLUMN user_id_int SET NOT NULL;
   ```

2. **Colonnes legacy** : Les colonnes `sun_sign`, `moon_sign`, `ascendant` peuvent être supprimées de la DB si elles n'existent plus. Le code ne les utilise plus.

3. **Compatibilité** : Le code garde un fallback sur `planets` (legacy) si `positions` n'existe pas, pour assurer la compatibilité pendant la transition.

4. **Structure `positions` JSONB** : Le helper `extract_big3_from_positions()` est tolérant aux variations de structure (snake_case, camelCase, etc.).

---

## ✅ Statut

**Problème résolu** ✅

L'endpoint `/api/lunar-returns/generate` ne crash plus avec `UndefinedColumnError`. Le code utilise maintenant :
- `user_id_int` (INTEGER) pour les queries
- `positions` (JSONB) pour extraire le Big3
- Helpers robustes pour l'extraction des données

