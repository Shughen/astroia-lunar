# Audit Backend - Révolution Lunaire V2 (Read-Only)

## 📋 Fichiers analysés

1. ✅ `apps/api/routes/lunar_returns.py` - Routes FastAPI
2. ✅ `apps/api/services/lunar_return_service.py` - Logique métier
3. ✅ `apps/api/schemas/lunar_return.py` - Modèles Pydantic
4. ✅ `apps/api/models/lunar_return.py` - Modèle SQLAlchemy (⚠️ non utilisé actuellement)

---

## 🔍 Analyse détaillée

### 1. Endpoint exact consommé par le mobile

**Route enregistrée :**
```python
# main.py ligne 92
app.include_router(lunar_returns.router, prefix="/api/lunar-returns", tags=["Lunar Returns"])
```

**Endpoints disponibles :**

| Méthode | Path | Handler | Description |
|---------|------|---------|-------------|
| `POST` | `/api/lunar-returns/generate` | `generate_lunar_return()` | Génère et sauvegarde une révolution lunaire |
| `GET` | `/api/lunar-returns` | `get_lunar_returns()` | Liste toutes les révolutions d'un utilisateur |
| `GET` | `/api/lunar-returns/{lunar_return_id}` | `get_lunar_return()` | Récupère une révolution par ID |

**Endpoint utilisé par le mobile (d'après `apps/mobile/services/api.ts`) :**
```typescript
// Ligne 95-98
generate: async () => {
  const response = await apiClient.post('/api/lunar-returns/generate');
  return response.data;
}
```

⚠️ **Note** : Le mobile appelle `/api/lunar-returns/generate` sans paramètres, mais l'endpoint attend un body avec `LunarReturnGenerateRequest` (cycle_number, user_id).

**Schéma Request :**
```python
# schemas/lunar_return.py lignes 11-14
class LunarReturnGenerateRequest(BaseModel):
    cycle_number: int = Field(..., ge=1)  # Numéro du cycle (1, 2, 3, ...)
    user_id: UUID                         # ID de l'utilisateur
```

---

### 2. Fonction centrale de calcul

**Fonction principale :**
```python
# services/lunar_return_service.py lignes 161-241
async def calculate_lunar_return(
    user_profile: UserProfileForLunarReturn,
    cycle_number: int
) -> Dict[str, Any]
```

**Flux de calcul (lignes 175-241) :**

```python
# 1. Calculer la date exacte de la révolution
lunar_return_date = calculate_lunar_return_date(birth_datetime, cycle_number)
start_date, end_date = calculate_lunar_return_period(lunar_return_date)

# 2. Calculer les positions planétaires à la révolution
planet_data = await calculate_planet_positions(
    lunar_return_date,
    user_profile.latitude,
    user_profile.longitude,
    user_profile.timezone
)

# 3. Extraire les données clés de la révolution
moon_position = next((p for p in positions if p.get("name") == "Moon"), None)
sun_position = next((p for p in positions if p.get("name") == "Sun"), None)
ascendant = next((p for p in positions if p.get("name") == "Ascendant"), None)

# 4. Extraire les aspects depuis la réponse RapidAPI
aspects = parse_aspects_from_natal_chart(raw_response) if raw_response else []

# 5. Générer les clés d'interprétation
interpretation_keys = generate_interpretation_keys(
    moon_position.get("sign"),
    moon_position.get("house"),
    ascendant.get("sign"),
    sun_position.get("sign"),
    aspects
)

# 6. Construire le résultat
result = {
    "cycle_number": cycle_number,
    "start_date": start_date.isoformat(),
    "end_date": end_date.isoformat(),
    "moon_sign": moon_position.get("sign"),
    "moon_degree": moon_position.get("degree"),
    "moon_house": moon_position.get("house"),
    "ascendant_sign": ascendant.get("sign"),
    "ascendant_degree": ascendant.get("degree"),
    "sun_sign": sun_position.get("sign"),
    "sun_degree": sun_position.get("degree"),
    "planet_positions": {"positions": positions, "raw_response": raw_response},
    "aspects": aspects,
    "interpretation_keys": interpretation_keys,
}
```

**Fonctions helper utilisées :**
- `calculate_lunar_return_date()` - Ligne 26 (calcule date exacte révolution)
- `calculate_lunar_return_period()` - Ligne 53 (calcule période start/end)
- `calculate_planet_positions()` - Ligne 74 (appel RapidAPI + parsing positions)
- `generate_interpretation_keys()` - Ligne 132 (génère clés interprétation)

---

### 3. Sauvegarde en base de données

**Fonction de sauvegarde :**
```python
# services/lunar_return_service.py lignes 244-315
async def create_lunar_return(user_id: UUID, computed_data: Dict[str, Any]) -> Dict[str, Any]
```

**Base de données :**
- ⚠️ **Supabase directement** (pas SQLAlchemy)
- Client : `get_supabase_client()` depuis `lib.supabase_client`
- Table : `"lunar_returns"` (Supabase)
- Ligne 289 : `supabase.table("lunar_returns").insert(lunar_return_data).execute()`

**Structure données sauvegardées (lignes 260-275) :**
```python
lunar_return_data = {
    "user_id": str(user_id),
    "cycle_number": computed_data["cycle_number"],
    "start_date": computed_data["start_date"],  # ISO string
    "end_date": computed_data["end_date"],      # ISO string
    "moon_sign": computed_data.get("moon_sign"),
    "moon_degree": computed_data.get("moon_degree"),
    "moon_house": computed_data.get("moon_house"),
    "ascendant_sign": computed_data.get("ascendant_sign"),
    "ascendant_degree": computed_data.get("ascendant_degree"),
    "sun_sign": computed_data.get("sun_sign"),
    "sun_degree": computed_data.get("sun_degree"),
    "planet_positions": computed_data.get("planet_positions"),  # JSON/Dict
    "aspects": computed_data.get("aspects"),                    # JSON/List
    "interpretation_keys": computed_data.get("interpretation_keys"),  # JSON/Dict
}
```

**Note importante :** Le modèle SQLAlchemy `models/lunar_return.py` existe mais **n'est pas utilisé**. Le code utilise Supabase directement via `supabase-py`.

**Table Supabase `lunar_returns` (structure supposée d'après le code) :**
- `id` (UUID ou Integer)
- `user_id` (UUID ou Integer)
- `cycle_number` (Integer)
- `start_date` (TIMESTAMP ou VARCHAR)
- `end_date` (TIMESTAMP ou VARCHAR)
- `moon_sign` (VARCHAR)
- `moon_degree` (FLOAT)
- `moon_house` (INTEGER)
- `ascendant_sign` (VARCHAR)
- `ascendant_degree` (FLOAT)
- `sun_sign` (VARCHAR)
- `sun_degree` (FLOAT)
- `planet_positions` (JSONB)
- `aspects` (JSONB)
- `interpretation_keys` (JSONB)
- `created_at` (TIMESTAMP, auto)
- `updated_at` (TIMESTAMP, auto)

---

### 4. Schéma de flux réel

```
┌─────────────────────────────────────────────────────────────────┐
│ Client Mobile                                                   │
│ POST /api/lunar-returns/generate                               │
│ Body: { cycle_number: 1, user_id: UUID }                       │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│ routes/lunar_returns.py::generate_lunar_return()               │
│ - Parse request (LunarReturnGenerateRequest)                    │
│ - Récupère profil depuis Supabase (table "profiles")            │
│ - Construit UserProfileForLunarReturn                           │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│ services/lunar_return_service.py::calculate_lunar_return()      │
│                                                                 │
│ 1. calculate_lunar_return_date()                                │
│    → Date exacte révolution (birth_date + cycle_number * 29.5) │
│                                                                 │
│ 2. calculate_lunar_return_period()                              │
│    → (start_date, end_date)                                     │
│                                                                 │
│ 3. calculate_planet_positions()                                 │
│    → Appel RapidAPI (call_rapidapi_natal_chart)                 │
│    → Parse positions (parse_positions_from_natal_chart)         │
│                                                                 │
│ 4. Extraction données clés                                      │
│    → moon_position, sun_position, ascendant                     │
│                                                                 │
│ 5. Parse aspects                                                │
│    → parse_aspects_from_natal_chart(raw_response)               │
│                                                                 │
│ 6. generate_interpretation_keys()                               │
│    → Clés d'interprétation (structure partielle)                │
│                                                                 │
│ 7. Construction résultat                                        │
│    → Dict avec toutes les données                               │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│ services/lunar_return_service.py::create_lunar_return()         │
│                                                                 │
│ 1. Préparer données pour Supabase                               │
│    → Formatage dates (ISO string)                               │
│                                                                 │
│ 2. Insertion dans Supabase                                      │
│    → supabase.table("lunar_returns").insert().execute()         │
│                                                                 │
│ 3. Retour données créées                                        │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│ routes/lunar_returns.py::generate_lunar_return()                │
│ - Convertit en LunarReturnResponse (Pydantic)                   │
│ - Retourne réponse au client                                    │
└─────────────────────────────────────────────────────────────────┘
```

---

### 5. Points d'injection V2 (sans casser V1)

#### ✅ Point 1: Calcul phase lunaire
**Fichier:** `services/lunar_return_service.py`  
**Fonction:** `calculate_lunar_return()`  
**Ligne:** Après ligne 205 (extraction sun_position)

```python
# Après extraction sun_position (ligne 203)
sun_position = next((p for p in positions if p.get("name") == "Sun"), None)

# ✅ INJECTION V2 ICI
# Ajouter calcul phase lunaire
if sun_position and moon_position:
    sun_degree = sun_position.get("degree", 0)
    moon_degree = moon_position.get("degree", 0)
    lunar_phase = calculate_lunar_phase(sun_degree, moon_degree)
    result["lunar_phase"] = lunar_phase
```

#### ✅ Point 2: Filtrage aspects significatifs + scoring
**Fichier:** `services/lunar_return_service.py`  
**Fonction:** `calculate_lunar_return()`  
**Ligne:** Après ligne 208 (parse aspects)

```python
# Après parse aspects (ligne 208)
aspects = parse_aspects_from_natal_chart(raw_response) if raw_response else []

# ✅ INJECTION V2 ICI
# Filtrer et scorer aspects
aspects_result = filter_significant_aspects(aspects)
result["significant_aspects"] = aspects_result["significant_aspects"]
result["dominant_aspect"] = aspects_result["dominant_aspect"]
# Garder tous les aspects pour compatibilité
result["aspects"] = aspects  # V1 (tous les aspects)
```

#### ✅ Point 3: Génération focus
**Fichier:** `services/lunar_return_service.py`  
**Fonction:** `calculate_lunar_return()`  
**Ligne:** Après ligne 217 (generate_interpretation_keys)

```python
# Après generate_interpretation_keys (ligne 211-217)
interpretation_keys = generate_interpretation_keys(...)

# ✅ INJECTION V2 ICI
# Générer focus enrichi
focus = generate_focus(
    moon_position.get("house") if moon_position else None,
    moon_position.get("sign") if moon_position else None,
    aspects_result["significant_aspects"]  # Utiliser aspects filtrés
)
result["focus"] = focus
```

#### ✅ Point 4: Génération suggestions
**Fichier:** `services/lunar_return_service.py`  
**Fonction:** `calculate_lunar_return()`  
**Ligne:** Après génération focus (point 3)

```python
# Après génération focus
focus = generate_focus(...)

# ✅ INJECTION V2 ICI
# Générer suggestions
suggestions = generate_suggestions(
    moon_position.get("house") if moon_position else None,
    moon_position.get("sign") if moon_position else None,
    ascendant.get("sign") if ascendant else None,
    aspects_result["significant_aspects"],
    lunar_phase.get("type") if lunar_phase else None
)
result["suggestions"] = suggestions
```

#### ✅ Point 5: Construction payload V2
**Fichier:** `services/lunar_return_service.py`  
**Fonction:** `calculate_lunar_return()`  
**Ligne:** Avant ligne 239 (return result)

```python
# Avant return result (ligne 239)

# ✅ INJECTION V2 ICI
# Construire payload V2
v2_payload = {
    "lunar_phase": result.get("lunar_phase"),
    "significant_aspects": result.get("significant_aspects", []),
    "dominant_aspect": result.get("dominant_aspect"),
    "focus": result.get("focus"),
    "suggestions": result.get("suggestions"),
}
result["v2_payload"] = v2_payload
result["v2_version"] = "2.0.0"
```

#### ✅ Point 6: Sauvegarde V2 dans Supabase
**Fichier:** `services/lunar_return_service.py`  
**Fonction:** `create_lunar_return()`  
**Ligne:** Après ligne 274 (avant insertion)

```python
# Après préparation données (ligne 260-275)
lunar_return_data = {
    # ... données V1 existantes
}

# ✅ INJECTION V2 ICI
# Ajouter colonnes V2
if computed_data.get("v2_payload"):
    lunar_return_data["v2_payload"] = computed_data["v2_payload"]
if computed_data.get("v2_version"):
    lunar_return_data["v2_version"] = computed_data["v2_version"]
```

#### ✅ Point 7: Schema Pydantic (optionnel, pour validation)
**Fichier:** `schemas/lunar_return.py`  
**Ligne:** Après `LunarReturnResponse` (ligne 103)

Ajouter champs optionnels pour compatibilité :
```python
class LunarReturnResponse(BaseModel):
    # ... champs existants V1
    
    # Nouveaux champs V2 (optionnels pour compatibilité)
    v2_version: Optional[str] = None
    v2_payload: Optional[Dict[str, Any]] = None
```

---

## 🗄️ Structure Base de Données

### Table Supabase `lunar_returns` (actuelle V1)

**Colonnes existantes :**
- `id` (UUID/Integer, PK)
- `user_id` (UUID/Integer, FK vers profiles)
- `cycle_number` (Integer)
- `start_date` (TIMESTAMP/VARCHAR)
- `end_date` (TIMESTAMP/VARCHAR)
- `moon_sign` (VARCHAR)
- `moon_degree` (FLOAT)
- `moon_house` (INTEGER)
- `ascendant_sign` (VARCHAR)
- `ascendant_degree` (FLOAT)
- `sun_sign` (VARCHAR)
- `sun_degree` (FLOAT)
- `planet_positions` (JSONB)
- `aspects` (JSONB)
- `interpretation_keys` (JSONB)
- `created_at` (TIMESTAMP, auto)
- `updated_at` (TIMESTAMP, auto)

### Migration V2 (à ajouter)

**Nouvelles colonnes :**
```sql
ALTER TABLE lunar_returns 
ADD COLUMN v2_version VARCHAR(10) DEFAULT NULL,
ADD COLUMN v2_payload JSONB DEFAULT NULL;

-- Index pour recherche rapide
CREATE INDEX idx_lunar_returns_v2_version ON lunar_returns(v2_version) 
WHERE v2_version IS NOT NULL;

CREATE INDEX idx_lunar_returns_v2_payload_gin ON lunar_returns 
USING GIN(v2_payload);
```

**Structure `v2_payload` JSONB :**
```json
{
  "lunar_phase": {
    "type": "waxing_crescent",
    "name": "Premier croissant",
    "emoji": "🌒",
    "description": "Croissance et expansion",
    "angle": 67.5
  },
  "significant_aspects": [
    {
      "from": "Moon",
      "to": "Venus",
      "aspect_type": "trine",
      "orb": 2.3,
      "score": 87.5,
      "strength": "strong",
      "interpretation": "...",
      "emoji": "△"
    }
  ],
  "dominant_aspect": {
    "from": "Moon",
    "to": "Venus",
    "aspect_type": "trine",
    "orb": 2.3,
    "score": 87.5,
    "strength": "strong"
  },
  "focus": {
    "theme": "Stabilité financière",
    "house": 2,
    "description": "Tes ressources matérielles...",
    "keywords": ["finances", "valeurs", "ressources"]
  },
  "suggestions": {
    "actions": ["Fais un bilan de tes finances"],
    "avoid": ["Évite les dépenses impulsives"],
    "opportunities": ["Période favorable pour investir"]
  }
}
```

---

## 📝 Plan Phase Backend V2

### Phase 1: Fonctions de calcul V2 (nouvelles fonctions)

**Fichier:** `apps/api/services/lunar_return_service.py`

#### 1.1 Fonction `calculate_lunar_phase()`
- **Ligne:** Ajouter après `calculate_lunar_return_period()` (après ligne 71)
- **Signature:** `def calculate_lunar_phase(sun_degree: float, moon_degree: float) -> Dict[str, Any]`
- **Logique:** Mapping angle → 8 phases (0-44°, 45-89°, etc.)
- **Retour:** `{type, name, emoji, description, angle}`
- **Tests:** Tests unitaires avec angles limites (0°, 45°, 90°, 135°, 180°, 225°, 270°, 315°)

#### 1.2 Fonction `calculate_aspect_score()`
- **Ligne:** Ajouter après `calculate_lunar_phase()`
- **Signature:** `def calculate_aspect_score(aspect: Dict[str, Any]) -> float`
- **Logique:** `score = base_score(type) - orb_penalty(orb) + strength_bonus(strength)`
- **Retour:** Score numérique (0-100)
- **Tests:** Tests avec différents types d'aspects, orbes, forces

#### 1.3 Fonction `filter_significant_aspects()`
- **Ligne:** Ajouter après `calculate_aspect_score()`
- **Signature:** `def filter_significant_aspects(all_aspects: List[Dict[str, Any]], orb_threshold: float = 5.0) -> Dict[str, Any]`
- **Logique:**
  1. Filtrer aspects majeurs (conjunction, opposition, trine, square, sextile)
  2. Filtrer orbe ≤ 5.0°
  3. Calculer score pour chaque aspect
  4. Trier par score décroissant
  5. Sélectionner dominant (score max)
- **Retour:** `{significant_aspects: List, dominant_aspect: Dict | None}`
- **Tests:** Tests filtrage, scoring, tri, sélection dominant

---

### Phase 2: Fonctions d'interprétation V2

**Fichier:** `apps/api/services/interpretations.py` (à créer ou enrichir)

#### 2.1 Fonction `generate_focus()`
- **Signature:** `def generate_focus(moon_house: int, moon_sign: str, major_aspects: List[Dict[str, Any]]) -> Dict[str, Any]`
- **Logique:** Synthèse maison + signe + aspects → focus enrichi
- **Retour:** `{theme, house, description, keywords}`
- **Tests:** Tests avec différentes maisons, signes, aspects

#### 2.2 Fonction `generate_suggestions()`
- **Signature:** `def generate_suggestions(moon_house: int, moon_sign: str, ascendant_sign: str, aspects: List[Dict[str, Any]], phase: str) -> Dict[str, Any]`
- **Logique:** Génération suggestions basées sur maison, signe, aspects, phase
- **Retour:** `{actions: List[str], avoid: List[str], opportunities: List[str]}`
- **Tests:** Tests avec différentes configurations

#### 2.3 Helpers (fonctions privées)
- `_get_house_actions(house: int) -> List[str]`
- `_get_sign_actions(sign: str) -> List[str]`
- `_get_challenging_warnings(aspects: List) -> List[str]`
- `_get_harmonious_opportunities(aspects: List) -> List[str]`

---

### Phase 3: Intégration dans `calculate_lunar_return()`

**Fichier:** `apps/api/services/lunar_return_service.py`  
**Fonction:** `calculate_lunar_return()` (modifier)

#### 3.1 Calcul phase lunaire
- **Ligne:** Après ligne 205 (extraction sun_position)
- **Code:**
```python
# Calculer phase lunaire V2
if sun_position and moon_position:
    sun_degree = sun_position.get("degree", 0)
    moon_degree = moon_position.get("degree", 0)
    lunar_phase = calculate_lunar_phase(sun_degree, moon_degree)
else:
    lunar_phase = None
```

#### 3.2 Filtrage aspects significatifs
- **Ligne:** Après ligne 208 (parse aspects)
- **Code:**
```python
# Filtrer et scorer aspects V2
aspects_result = filter_significant_aspects(aspects)
significant_aspects = aspects_result["significant_aspects"]
dominant_aspect = aspects_result["dominant_aspect"]
```

#### 3.3 Génération focus
- **Ligne:** Après ligne 217 (generate_interpretation_keys)
- **Code:**
```python
# Générer focus V2
focus = generate_focus(
    moon_position.get("house") if moon_position else None,
    moon_position.get("sign") if moon_position else None,
    significant_aspects
)
```

#### 3.4 Génération suggestions
- **Ligne:** Après génération focus
- **Code:**
```python
# Générer suggestions V2
suggestions = generate_suggestions(
    moon_position.get("house") if moon_position else None,
    moon_position.get("sign") if moon_position else None,
    ascendant.get("sign") if ascendant else None,
    significant_aspects,
    lunar_phase.get("type") if lunar_phase else None
)
```

#### 3.5 Construction payload V2
- **Ligne:** Avant ligne 239 (return result)
- **Code:**
```python
# Construire payload V2
v2_payload = {
    "lunar_phase": lunar_phase,
    "significant_aspects": significant_aspects,
    "dominant_aspect": dominant_aspect,
    "focus": focus,
    "suggestions": suggestions,
}

# Ajouter au résultat (garder données V1 pour compatibilité)
result["lunar_phase"] = lunar_phase  # Pour accès direct aussi
result["significant_aspects"] = significant_aspects
result["dominant_aspect"] = dominant_aspect
result["focus"] = focus
result["suggestions"] = suggestions
result["v2_payload"] = v2_payload
result["v2_version"] = "2.0.0"
```

---

### Phase 4: Sauvegarde V2 dans Supabase

**Fichier:** `apps/api/services/lunar_return_service.py`  
**Fonction:** `create_lunar_return()` (modifier)

#### 4.1 Ajout colonnes V2 dans données
- **Ligne:** Après ligne 275 (avant insertion Supabase)
- **Code:**
```python
# Ajouter colonnes V2 pour Supabase
if computed_data.get("v2_payload"):
    lunar_return_data["v2_payload"] = computed_data["v2_payload"]
if computed_data.get("v2_version"):
    lunar_return_data["v2_version"] = computed_data["v2_version"]
```

---

### Phase 5: Migration Base de Données

**Fichier:** Migration Alembic (à créer)

#### 5.1 Créer migration
```bash
alembic revision -m "add_v2_columns_to_lunar_returns"
```

#### 5.2 Contenu migration
```python
def upgrade():
    op.add_column('lunar_returns', sa.Column('v2_version', sa.String(10), nullable=True))
    op.add_column('lunar_returns', sa.Column('v2_payload', postgresql.JSONB(), nullable=True))
    op.create_index('idx_lunar_returns_v2_version', 'lunar_returns', ['v2_version'], 
                    postgresql_where=sa.text('v2_version IS NOT NULL'))
    op.create_index('idx_lunar_returns_v2_payload_gin', 'lunar_returns', ['v2_payload'], 
                    postgresql_using='gin')

def downgrade():
    op.drop_index('idx_lunar_returns_v2_payload_gin', 'lunar_returns')
    op.drop_index('idx_lunar_returns_v2_version', 'lunar_returns')
    op.drop_column('lunar_returns', 'v2_payload')
    op.drop_column('lunar_returns', 'v2_version')
```

⚠️ **Note:** Si utilisation Supabase (pas PostgreSQL direct), créer migration SQL manuellement dans Supabase Dashboard.

---

### Phase 6: Schema Pydantic (optionnel, pour validation)

**Fichier:** `apps/api/schemas/lunar_return.py`

#### 6.1 Ajouter champs V2 optionnels
- **Ligne:** Après ligne 102 (dans `LunarReturnResponse`)
- **Code:**
```python
class LunarReturnResponse(BaseModel):
    # ... champs existants V1
    
    # Champs V2 (optionnels pour compatibilité)
    v2_version: Optional[str] = None
    v2_payload: Optional[Dict[str, Any]] = None
```

---

## 🎯 Ordre d'implémentation recommandé

### Étape 1: Préparation (sans modifier code existant)
1. ✅ Créer migration DB (Phase 5) - Tester migration
2. ✅ Créer tests unitaires pour nouvelles fonctions (Phase 1 + Phase 2)

### Étape 2: Fonctions de calcul V2 (isolées)
3. ✅ Implémenter `calculate_lunar_phase()` (Phase 1.1)
4. ✅ Implémenter `calculate_aspect_score()` (Phase 1.2)
5. ✅ Implémenter `filter_significant_aspects()` (Phase 1.3)
6. ✅ Tests unitaires Phase 1

### Étape 3: Fonctions d'interprétation V2
7. ✅ Implémenter `generate_focus()` (Phase 2.1)
8. ✅ Implémenter `generate_suggestions()` + helpers (Phase 2.2 + 2.3)
9. ✅ Tests unitaires Phase 2

### Étape 4: Intégration dans calcul principal
10. ✅ Modifier `calculate_lunar_return()` - Ajout calcul phase (Phase 3.1)
11. ✅ Modifier `calculate_lunar_return()` - Filtrage aspects (Phase 3.2)
12. ✅ Modifier `calculate_lunar_return()` - Génération focus (Phase 3.3)
13. ✅ Modifier `calculate_lunar_return()` - Génération suggestions (Phase 3.4)
14. ✅ Modifier `calculate_lunar_return()` - Construction payload V2 (Phase 3.5)
15. ✅ Tests intégration `calculate_lunar_return()` complet

### Étape 5: Sauvegarde V2
16. ✅ Modifier `create_lunar_return()` - Ajout colonnes V2 (Phase 4.1)
17. ✅ Tests sauvegarde Supabase avec v2_payload

### Étape 6: Schema (optionnel)
18. ✅ Modifier `LunarReturnResponse` - Ajout champs V2 (Phase 6.1)
19. ✅ Tests validation Pydantic

### Étape 7: Tests end-to-end
20. ✅ Test complet: POST /api/lunar-returns/generate → Vérifier v2_payload dans DB
21. ✅ Test récupération: GET /api/lunar-returns/{id} → Vérifier v2_payload dans réponse
22. ✅ Test compatibilité: Vérifier que données V1 toujours présentes

---

## ✅ Checklist avant implémentation

- [ ] Migration DB créée et testée (ajout colonnes `v2_version`, `v2_payload`)
- [ ] Tests unitaires écrits pour nouvelles fonctions (avant implémentation)
- [ ] Documentation fonction `calculate_lunar_phase()` (8 phases, mapping angle)
- [ ] Documentation fonction `filter_significant_aspects()` (règles filtrage, scoring)
- [ ] Documentation fonction `generate_focus()` (logique synthèse)
- [ ] Documentation fonction `generate_suggestions()` (génération suggestions)
- [ ] Plan de rollback (en cas de problème)
- [ ] Stratégie de déploiement (migration DB avant déploiement code)

---

## 🚨 Points d'attention

1. **Compatibilité V1** : Tous les champs V1 doivent rester présents et fonctionnels
2. **Champs optionnels** : V2 doit être optionnel (v2_version peut être NULL)
3. **Migration Supabase** : Si Supabase, vérifier comment créer migration (peut nécessiter SQL manuel)
4. **Tests** : Tester avec données existantes (révolutions V1 déjà en base)
5. **Performance** : Vérifier que calcul V2 n'ajoute pas trop de latence
6. **Rollback** : Prévoir rollback si v2_payload cause des problèmes

---

## 📊 Résumé des fichiers à modifier

| Fichier | Modifications | Lignes approximatives |
|---------|--------------|----------------------|
| `services/lunar_return_service.py` | Ajouter 3 nouvelles fonctions | Après ligne 71 (calculate_lunar_phase, calculate_aspect_score, filter_significant_aspects) |
| `services/lunar_return_service.py` | Modifier `calculate_lunar_return()` | Lignes 205-239 (ajout calculs V2) |
| `services/lunar_return_service.py` | Modifier `create_lunar_return()` | Ligne 275 (ajout colonnes V2) |
| `services/interpretations.py` | Ajouter 2 nouvelles fonctions | Nouveau fichier ou ajout (generate_focus, generate_suggestions + helpers) |
| `schemas/lunar_return.py` | Modifier `LunarReturnResponse` | Après ligne 102 (champs V2 optionnels) |
| Migration Alembic | Créer nouvelle migration | Nouveau fichier (add_v2_columns_to_lunar_returns) |

**Total:** 6 fichiers (5 modifications + 1 migration)

---

**Document généré le:** Date actuelle  
**Statut:** ✅ Prêt pour validation avant implémentation

