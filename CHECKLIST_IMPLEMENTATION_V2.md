# Checklist Implémentation V2 - Révolution Lunaire

**Branche:** `feat/lunar-revolution-v2`  
**Objectif:** Implémenter V2 sans casser V1  
**Contrat V2:** `lunar_phase`, `significant_aspects`, `dominant_aspect`, `focus`, `suggestions`, `v2_payload`, `v2_version`

---

## 🔧 Prérequis

```bash
# Vérifier que tu es sur la bonne branche
git branch --show-current  # Doit afficher: feat/lunar-revolution-v2

# Vérifier environnement Python
cd apps/api
python --version  # Doit être Python 3.10+
source venv/bin/activate  # Si venv existe

# Installer dépendances si nécessaire
pip install -r requirements.txt
```

---

## ✅ ÉTAPE 1: Migration Base de Données

**Objectif:** Ajouter colonnes `v2_version` et `v2_payload` à la table `lunar_returns`

### Commandes

```bash
cd apps/api

# Créer la migration Alembic
alembic revision -m "add_v2_columns_to_lunar_returns"
```

### Fichier à modifier

**Fichier:** `apps/api/alembic/versions/XXXXXX_add_v2_columns_to_lunar_returns.py` (nouveau fichier créé par Alembic)

**Contenu à ajouter dans `upgrade()`:**
```python
def upgrade() -> None:
    # Ajouter colonnes V2
    op.add_column('lunar_returns', sa.Column('v2_version', sa.String(10), nullable=True))
    op.add_column('lunar_returns', sa.Column('v2_payload', sa.JSON(), nullable=True))
    
    # Créer index sur v2_version (pour recherche rapide)
    op.create_index(
        'idx_lunar_returns_v2_version', 
        'lunar_returns', 
        ['v2_version'], 
        postgresql_where=sa.text('v2_version IS NOT NULL')
    )
    
    # Index GIN sur v2_payload (pour recherche dans JSON)
    op.create_index(
        'idx_lunar_returns_v2_payload_gin',
        'lunar_returns',
        ['v2_payload'],
        postgresql_using='gin'
    )
```

**Contenu à ajouter dans `downgrade()`:**
```python
def downgrade() -> None:
    op.drop_index('idx_lunar_returns_v2_payload_gin', 'lunar_returns')
    op.drop_index('idx_lunar_returns_v2_version', 'lunar_returns')
    op.drop_column('lunar_returns', 'v2_payload')
    op.drop_column('lunar_returns', 'v2_version')
```

### Appliquer migration

```bash
# Appliquer migration (local/development)
alembic upgrade head

# Vérifier migration appliquée
alembic current
```

### ✅ Critères de Done

- [ ] Migration créée sans erreur
- [ ] Migration appliquée (`alembic current` affiche la nouvelle migration)
- [ ] Colonnes `v2_version` et `v2_payload` existent dans table `lunar_returns` (vérifier via Supabase Dashboard ou psql)

### 📝 Vérification Supabase

Si utilisation Supabase, vérifier dans Supabase Dashboard → Table Editor → `lunar_returns`:
- Colonne `v2_version` (VARCHAR, nullable)
- Colonne `v2_payload` (JSONB, nullable)

**Commit:**
```bash
git add apps/api/alembic/versions/*_add_v2_columns_to_lunar_returns.py
git commit -m "feat: add v2_version and v2_payload columns to lunar_returns"
```

---

## ✅ ÉTAPE 2: Fonction calculate_lunar_phase()

**Objectif:** Calculer phase lunaire en 8 phases basée sur angle Soleil-Lune

### Fichier à modifier

**Fichier:** `apps/api/services/lunar_return_service.py`  
**Position:** Après fonction `calculate_lunar_return_period()` (après ligne 71)

### Code à ajouter

```python
def calculate_lunar_phase(sun_degree: float, moon_degree: float) -> Dict[str, Any]:
    """
    Calcule la phase lunaire en 8 phases basée sur l'angle Soleil-Lune
    
    Mapping angle -> phase:
    - 0-44.99°     -> new_moon
    - 45-89.99°    -> waxing_crescent
    - 90-134.99°   -> first_quarter
    - 135-179.99°  -> waxing_gibbous
    - 180-224.99°  -> full_moon
    - 225-269.99°  -> waning_gibbous
    - 270-314.99°  -> last_quarter
    - 315-359.99°  -> waning_crescent
    """
    angle = (moon_degree - sun_degree) % 360
    
    if 0 <= angle < 45:
        phase_type = "new_moon"
        phase_info = {"name": "Nouvelle Lune", "emoji": "🌑", "description": "Nouveau départ, intentions fraîches"}
    elif 45 <= angle < 90:
        phase_type = "waxing_crescent"
        phase_info = {"name": "Premier croissant", "emoji": "🌒", "description": "Croissance et expansion"}
    elif 90 <= angle < 135:
        phase_type = "first_quarter"
        phase_info = {"name": "Premier quartier", "emoji": "🌓", "description": "Action et décision"}
    elif 135 <= angle < 180:
        phase_type = "waxing_gibbous"
        phase_info = {"name": "Gibbeuse croissante", "emoji": "🌔", "description": "Affinage et ajustement"}
    elif 180 <= angle < 225:
        phase_type = "full_moon"
        phase_info = {"name": "Pleine Lune", "emoji": "🌕", "description": "Culmination et révélation"}
    elif 225 <= angle < 270:
        phase_type = "waning_gibbous"
        phase_info = {"name": "Gibbeuse décroissante", "emoji": "🌖", "description": "Récolte et gratitude"}
    elif 270 <= angle < 315:
        phase_type = "last_quarter"
        phase_info = {"name": "Dernier quartier", "emoji": "🌗", "description": "Lâcher-prise et tri"}
    else:  # 315 <= angle < 360
        phase_type = "waning_crescent"
        phase_info = {"name": "Dernier croissant", "emoji": "🌘", "description": "Repos et préparation"}
    
    return {
        "type": phase_type,
        **phase_info,
        "angle": round(angle, 2)
    }
```

### ✅ Critères de Done

- [ ] Fonction ajoutée sans erreur de syntaxe
- [ ] Tests manuels avec angles limites (0°, 45°, 90°, 135°, 180°, 225°, 270°, 315°)
- [ ] Vérifier que chaque angle retourne la bonne phase

### 🧪 Test manuel

```python
# Dans Python REPL ou script de test
from services.lunar_return_service import calculate_lunar_phase

# Test angle 0° (nouvelle lune)
result = calculate_lunar_phase(100.0, 100.0)  # angle = 0°
assert result["type"] == "new_moon"

# Test angle 90° (premier quartier)
result = calculate_lunar_phase(100.0, 190.0)  # angle = 90°
assert result["type"] == "first_quarter"

# Test angle 180° (pleine lune)
result = calculate_lunar_phase(100.0, 280.0)  # angle = 180°
assert result["type"] == "full_moon"
```

**Commit:**
```bash
git add apps/api/services/lunar_return_service.py
git commit -m "feat: add calculate_lunar_phase function (8 phases)"
```

---

## ✅ ÉTAPE 3: Fonctions scoring et filtrage aspects

**Objectif:** Filtrer aspects significatifs avec scoring numérique

### Fichier à modifier

**Fichier:** `apps/api/services/lunar_return_service.py`  
**Position:** Après fonction `calculate_lunar_phase()` (ajoutée à l'étape 2)

### Constantes à ajouter (en haut du fichier, après imports)

```python
# Constantes pour filtrage aspects V2
MAJOR_ASPECT_TYPES = ["conjunction", "opposition", "trine", "square", "sextile"]
ORB_THRESHOLD = 5.0  # Orbe maximum accepté (en degrés)

# Scores de base par type d'aspect
ASPECT_BASE_SCORE = {
    "conjunction": 30,
    "opposition": 25,
    "square": 20,
    "trine": 15,
    "sextile": 10
}
```

### Fonctions à ajouter

```python
def calculate_aspect_score(aspect: Dict[str, Any]) -> float:
    """
    Calcule un score numérique (0-100) pour un aspect
    Score = base_score(type) - orb_penalty(orb) + strength_bonus(strength)
    """
    aspect_type = aspect.get("aspect_type")
    orb = abs(aspect.get("orb", 999))
    strength = aspect.get("strength", "medium")
    
    base_score = ASPECT_BASE_SCORE.get(aspect_type, 0)
    orb_penalty = min(15, orb * 3)  # Orbe 0° = 0 penalty, orbe 5° = 15 penalty
    
    strength_bonus = {"strong": 10, "medium": 5, "weak": 0}.get(strength, 0)
    score = base_score - orb_penalty + strength_bonus
    
    return max(0, min(100, score))


def filter_significant_aspects(
    all_aspects: List[Dict[str, Any]],
    orb_threshold: float = ORB_THRESHOLD
) -> Dict[str, Any]:
    """
    Filtre, score et classe les aspects significatifs
    Returns: {significant_aspects: List, dominant_aspect: Dict | None}
    """
    # Filtrer aspects majeurs avec orbe acceptable
    significant_aspects = [
        a for a in all_aspects
        if a.get("aspect_type") in MAJOR_ASPECT_TYPES
        and abs(a.get("orb", 999)) <= orb_threshold
    ]
    
    # Calculer score pour chaque aspect
    for aspect in significant_aspects:
        aspect["score"] = calculate_aspect_score(aspect)
    
    # Trier par score décroissant
    significant_aspects_sorted = sorted(
        significant_aspects,
        key=lambda a: a.get("score", 0),
        reverse=True
    )
    
    # Sélectionner dominant (premier = score max)
    dominant_aspect = significant_aspects_sorted[0] if significant_aspects_sorted else None
    
    return {
        "significant_aspects": significant_aspects_sorted,
        "dominant_aspect": dominant_aspect
    }
```

### ✅ Critères de Done

- [ ] Constantes ajoutées
- [ ] Fonctions `calculate_aspect_score()` et `filter_significant_aspects()` ajoutées
- [ ] Test manuel avec aspects fictifs

### 🧪 Test manuel

```python
# Test avec aspects fictifs
aspects = [
    {"aspect_type": "trine", "orb": 2.0, "strength": "strong", "from": "Moon", "to": "Venus"},
    {"aspect_type": "square", "orb": 4.5, "strength": "medium", "from": "Moon", "to": "Mars"},
    {"aspect_type": "sextile", "orb": 6.0, "strength": "weak", "from": "Moon", "to": "Jupiter"},  # Orbe trop grand
]

result = filter_significant_aspects(aspects)
assert len(result["significant_aspects"]) == 2  # Seulement 2 (sextile exclu)
assert result["dominant_aspect"] is not None
assert result["dominant_aspect"]["aspect_type"] == "trine"  # Meilleur score
```

**Commit:**
```bash
git add apps/api/services/lunar_return_service.py
git commit -m "feat: add aspect scoring and filtering functions"
```

---

## ✅ ÉTAPE 4: Fonctions generate_focus() et generate_suggestions()

**Objectif:** Générer focus et suggestions enrichis

### Fichier à modifier

**Fichier:** `apps/api/services/interpretations.py`  
**Position:** À la fin du fichier (après fonction `get_moon_phase_description()`)

### Code à ajouter

```python
def generate_focus(
    moon_house: int,
    moon_sign: str,
    major_aspects: List[Dict[str, Any]]
) -> Dict[str, Any]:
    """
    Génère le focus du mois (thème principal)
    """
    # Base: interprétation maison (déjà définie dans HOUSE_INTERPRETATIONS)
    house_theme = HOUSE_INTERPRETATIONS.get(moon_house, "Ta Lune éclaire un domaine important de ta vie.")
    
    # Extraire thème principal
    theme_parts = house_theme.split(".")[0] if "." in house_theme else house_theme
    theme = theme_parts.strip()
    
    # Keywords basiques selon maison
    keywords_map = {
        1: ["identité", "personnalité", "renouveau"],
        2: ["finances", "valeurs", "ressources"],
        3: ["communication", "apprentissage", "relations"],
        4: ["foyer", "famille", "racines"],
        5: ["créativité", "romance", "plaisir"],
        6: ["santé", "routine", "service"],
        7: ["relations", "partenariats", "équilibre"],
        8: ["transformation", "intimité", "ressources partagées"],
        9: ["expansion", "voyages", "philosophie"],
        10: ["carrière", "ambitions", "réputation"],
        11: ["amitié", "communauté", "projets collectifs"],
        12: ["spiritualité", "repos", "inconscient"],
    }
    keywords = keywords_map.get(moon_house, [])
    
    return {
        "theme": theme,
        "house": moon_house,
        "description": house_theme,
        "keywords": keywords
    }


def generate_suggestions(
    moon_house: int,
    moon_sign: str,
    ascendant_sign: str,
    aspects: List[Dict[str, Any]],
    phase: str
) -> Dict[str, Any]:
    """
    Génère des suggestions actionnables pour le mois
    """
    suggestions = {"actions": [], "avoid": [], "opportunities": []}
    
    # Suggestions basées sur maison
    house_actions_map = {
        1: ["Prends le temps de réfléchir à qui tu es vraiment"],
        2: ["Fais un bilan de tes finances et de tes talents"],
        3: ["Écris, communique, apprends quelque chose de nouveau"],
        4: ["Passe du temps de qualité avec ta famille ou chez toi"],
        5: ["Exprime ta créativité sans retenue, amuse-toi"],
        6: ["Mets en place une nouvelle routine bien-être"],
        7: ["Renforce tes relations importantes, cherche l'harmonie"],
        8: ["Explore tes émotions profondes, transforme-toi"],
        9: ["Planifie un voyage ou inscris-toi à une formation"],
        10: ["Fixe-toi des objectifs professionnels clairs"],
        11: ["Connecte-toi avec ta communauté, innove"],
        12: ["Médite, repose-toi, écoute ton intuition"],
    }
    suggestions["actions"].extend(house_actions_map.get(moon_house, []))
    
    # Suggestions basées sur phase
    if phase == "new_moon":
        suggestions["actions"].append("Plante des intentions pour ce nouveau cycle")
    elif phase == "full_moon":
        suggestions["actions"].append("Célèbre tes accomplissements et lâche prise")
    
    # Suggestions basées sur aspects
    challenging = [a for a in aspects if a.get("aspect_type") in ["square", "opposition"]]
    harmonious = [a for a in aspects if a.get("aspect_type") in ["trine", "sextile", "conjunction"]]
    
    if challenging:
        suggestions["avoid"].append("Évite les décisions impulsives face aux tensions")
    if harmonious:
        suggestions["opportunities"].append("Profite de cette énergie harmonieuse pour avancer")
    
    return suggestions
```

### ✅ Critères de Done

- [ ] Fonctions ajoutées dans `interpretations.py`
- [ ] Test manuel avec différentes maisons
- [ ] Vérifier que focus et suggestions sont générés correctement

### 🧪 Test manuel

```python
from services.interpretations import generate_focus, generate_suggestions

# Test focus
focus = generate_focus(2, "Taurus", [])
assert focus["house"] == 2
assert "finances" in focus["keywords"]

# Test suggestions
suggestions = generate_suggestions(2, "Taurus", "Leo", [], "new_moon")
assert len(suggestions["actions"]) > 0
```

**Commit:**
```bash
git add apps/api/services/interpretations.py
git commit -m "feat: add generate_focus and generate_suggestions functions"
```

---

## ✅ ÉTAPE 5: Intégration dans calculate_lunar_return() - Phase lunaire

**Objectif:** Calculer et ajouter phase lunaire dans le résultat

### Fichier à modifier

**Fichier:** `apps/api/services/lunar_return_service.py`  
**Fonction:** `calculate_lunar_return()`  
**Position:** Après ligne 205 (après extraction sun_position)

### Code à ajouter

```python
# Après ligne 205 (extraction sun_position)
sun_position = next((p for p in positions if p.get("name") == "Sun"), None)

# ✅ AJOUT V2: Calculer phase lunaire
if sun_position and moon_position:
    sun_degree = sun_position.get("degree", 0)
    moon_degree = moon_position.get("degree", 0)
    lunar_phase = calculate_lunar_phase(sun_degree, moon_degree)
else:
    lunar_phase = None
```

### ✅ Critères de Done

- [ ] Code ajouté après extraction sun_position
- [ ] Variable `lunar_phase` disponible pour utilisation suivante
- [ ] Pas d'erreur de syntaxe

**Commit:**
```bash
git add apps/api/services/lunar_return_service.py
git commit -m "feat: integrate lunar_phase calculation in calculate_lunar_return"
```

---

## ✅ ÉTAPE 6: Intégration dans calculate_lunar_return() - Aspects significatifs

**Objectif:** Filtrer et scorer aspects, identifier dominant

### Fichier à modifier

**Fichier:** `apps/api/services/lunar_return_service.py`  
**Fonction:** `calculate_lunar_return()`  
**Position:** Après ligne 208 (après parse aspects)

### Code à ajouter

```python
# Après ligne 208 (parse aspects)
aspects = parse_aspects_from_natal_chart(raw_response) if raw_response else []

# ✅ AJOUT V2: Filtrer et scorer aspects significatifs
aspects_result = filter_significant_aspects(aspects)
significant_aspects = aspects_result["significant_aspects"]
dominant_aspect = aspects_result["dominant_aspect"]
```

### ✅ Critères de Done

- [ ] Code ajouté après parse aspects
- [ ] Variables `significant_aspects` et `dominant_aspect` disponibles
- [ ] Aspects V1 conservés dans variable `aspects` (pour compatibilité)

**Commit:**
```bash
git add apps/api/services/lunar_return_service.py
git commit -m "feat: integrate aspect filtering and scoring in calculate_lunar_return"
```

---

## ✅ ÉTAPE 7: Intégration dans calculate_lunar_return() - Focus et suggestions

**Objectif:** Générer focus et suggestions, construire payload V2

### Fichier à modifier

**Fichier:** `apps/api/services/lunar_return_service.py`  
**Fonction:** `calculate_lunar_return()`  
**Position:** Après ligne 217 (après generate_interpretation_keys) et avant ligne 239 (return result)

### Code à ajouter

```python
# Après ligne 217 (generate_interpretation_keys)
interpretation_keys = generate_interpretation_keys(...)

# ✅ AJOUT V2: Générer focus
from services.interpretations import generate_focus, generate_suggestions

focus = generate_focus(
    moon_position.get("house") if moon_position else None,
    moon_position.get("sign") if moon_position else None,
    significant_aspects
)

# ✅ AJOUT V2: Générer suggestions
suggestions = generate_suggestions(
    moon_position.get("house") if moon_position else None,
    moon_position.get("sign") if moon_position else None,
    ascendant.get("sign") if ascendant else None,
    significant_aspects,
    lunar_phase.get("type") if lunar_phase else None
)

# Avant ligne 239 (return result) - Construction résultat
# ... code existant pour result = { ... }

# ✅ AJOUT V2: Construire payload V2
v2_payload = {
    "lunar_phase": lunar_phase,
    "significant_aspects": significant_aspects,
    "dominant_aspect": dominant_aspect,
    "focus": focus,
    "suggestions": suggestions,
}

# Ajouter champs V2 au résultat (garder V1 pour compatibilité)
result["lunar_phase"] = lunar_phase
result["significant_aspects"] = significant_aspects
result["dominant_aspect"] = dominant_aspect
result["focus"] = focus
result["suggestions"] = suggestions
result["v2_payload"] = v2_payload
result["v2_version"] = "2.0.0"
```

**Note:** Le code existant qui construit `result` (lignes 220-237) doit rester inchangé. Ajouter les champs V2 après.

### ✅ Critères de Done

- [ ] Focus et suggestions générés
- [ ] Payload V2 construit
- [ ] Tous les champs V2 ajoutés au résultat
- [ ] Champs V1 conservés (vérifier que `result` contient toujours moon_sign, moon_house, etc.)

**Commit:**
```bash
git add apps/api/services/lunar_return_service.py
git commit -m "feat: integrate focus, suggestions and v2_payload in calculate_lunar_return"
```

---

## ✅ ÉTAPE 8: Sauvegarde V2 dans Supabase

**Objectif:** Sauvegarder colonnes v2_version et v2_payload dans DB

### Fichier à modifier

**Fichier:** `apps/api/services/lunar_return_service.py`  
**Fonction:** `create_lunar_return()`  
**Position:** Après ligne 275 (dans `lunar_return_data`, avant insertion Supabase)

### Code à ajouter

```python
# Dans create_lunar_return(), après préparation lunar_return_data (ligne 275)
lunar_return_data = {
    "user_id": str(user_id),
    "cycle_number": computed_data["cycle_number"],
    # ... autres champs V1 existants ...
}

# ✅ AJOUT V2: Ajouter colonnes V2 pour Supabase
if computed_data.get("v2_payload"):
    lunar_return_data["v2_payload"] = computed_data["v2_payload"]
if computed_data.get("v2_version"):
    lunar_return_data["v2_version"] = computed_data["v2_version"]
```

### ✅ Critères de Done

- [ ] Colonnes V2 ajoutées dans `lunar_return_data`
- [ ] Code placé avant insertion Supabase (ligne 289)
- [ ] Vérifier que v2_payload est un dict JSON-serializable

**Commit:**
```bash
git add apps/api/services/lunar_return_service.py
git commit -m "feat: save v2_payload and v2_version to Supabase"
```

---

## ✅ ÉTAPE 9: Schema Pydantic (optionnel mais recommandé)

**Objectif:** Ajouter champs V2 dans LunarReturnResponse pour validation

### Fichier à modifier

**Fichier:** `apps/api/schemas/lunar_return.py`  
**Position:** Dans classe `LunarReturnResponse`, après ligne 102 (après `updated_at`)

### Code à ajouter

```python
class LunarReturnResponse(BaseModel):
    # ... champs existants V1 ...
    created_at: datetime
    updated_at: datetime
    
    # ✅ AJOUT V2: Champs V2 optionnels (pour compatibilité)
    v2_version: Optional[str] = None
    v2_payload: Optional[Dict[str, Any]] = None
```

### ✅ Critères de Done

- [ ] Champs V2 ajoutés comme optionnels
- [ ] Pas d'erreur de validation Pydantic
- [ ] Les réponses API peuvent inclure ou non ces champs

**Commit:**
```bash
git add apps/api/schemas/lunar_return.py
git commit -m "feat: add v2_version and v2_payload to LunarReturnResponse schema"
```

---

## ✅ ÉTAPE 10: Tests end-to-end

**Objectif:** Vérifier que V2 fonctionne de bout en bout

### Test API avec curl

```bash
# Démarrage serveur API (dans un terminal)
cd apps/api
uvicorn main:app --reload --port 8000

# Dans un autre terminal: Générer une révolution lunaire
curl -X POST "http://localhost:8000/api/lunar-returns/generate" \
  -H "Content-Type: application/json" \
  -d '{
    "cycle_number": 1,
    "user_id": "VOTRE_USER_ID_UUID"
  }' | jq '.'
```

### ✅ Critères de validation réponse API

La réponse JSON doit contenir:

**Champs V1 (existants, doivent être présents):**
- `moon_sign`, `moon_degree`, `moon_house`
- `ascendant_sign`, `ascendant_degree`
- `sun_sign`, `sun_degree`
- `aspects` (liste complète)
- `interpretation_keys`

**Champs V2 (nouveaux, doivent être présents):**
- `lunar_phase` (object avec `type`, `name`, `emoji`, `description`, `angle`)
- `significant_aspects` (liste d'aspects filtrés avec `score`)
- `dominant_aspect` (object ou null)
- `focus` (object avec `theme`, `house`, `description`, `keywords`)
- `suggestions` (object avec `actions`, `avoid`, `opportunities`)
- `v2_payload` (object contenant tous les champs V2)
- `v2_version` (string "2.0.0")

### Vérification dans Supabase

```sql
-- Dans Supabase SQL Editor
SELECT 
    id,
    cycle_number,
    v2_version,
    v2_payload->>'lunar_phase' as lunar_phase_type,
    jsonb_array_length(v2_payload->'significant_aspects') as significant_aspects_count,
    v2_payload->'focus'->>'theme' as focus_theme
FROM lunar_returns
WHERE v2_version IS NOT NULL
ORDER BY created_at DESC
LIMIT 1;
```

**Résultat attendu:**
- `v2_version` = "2.0.0"
- `lunar_phase_type` = une des 8 phases (ex: "waxing_crescent")
- `significant_aspects_count` = nombre d'aspects filtrés
- `focus_theme` = thème du focus

### Test mobile Expo

```bash
# Dans un terminal
cd apps/mobile

# Démarrer Expo
npx expo start

# Dans l'app mobile, tester:
# 1. Appel API lunarReturns.generate()
# 2. Vérifier que la réponse contient v2_payload
# 3. Vérifier que les champs V1 sont toujours présents
```

**Code de test dans mobile (dans un composant React Native temporaire):**
```typescript
import { lunarReturns } from '@/services/api';

const testV2 = async () => {
  try {
    const response = await lunarReturns.generate({
      cycle_number: 1,
      user_id: 'YOUR_USER_ID'
    });
    
    console.log('V2 fields:', {
      lunar_phase: response.lunar_phase,
      significant_aspects: response.significant_aspects,
      dominant_aspect: response.dominant_aspect,
      focus: response.focus,
      suggestions: response.suggestions,
      v2_payload: response.v2_payload,
      v2_version: response.v2_version
    });
    
    // Vérifier V1 toujours présent
    console.log('V1 fields still present:', {
      moon_sign: response.moon_sign,
      moon_house: response.moon_house,
      aspects: response.aspects
    });
  } catch (error) {
    console.error('Error:', error);
  }
};
```

### ✅ Critères de Done - Tests

- [ ] API répond avec tous les champs V2 présents
- [ ] API répond avec tous les champs V1 présents (compatibilité)
- [ ] v2_payload sauvegardé dans Supabase (colonne JSONB)
- [ ] v2_version = "2.0.0" dans DB
- [ ] Test mobile fonctionne (si applicable)
- [ ] Aucune régression sur endpoints existants

### Vérification finale

```bash
# Vérifier que les tests passent (si tests unitaires existent)
cd apps/api
pytest tests/ -v

# Vérifier que l'API démarre sans erreur
uvicorn main:app --reload --port 8000
# Ouvrir http://localhost:8000/docs
# Tester POST /api/lunar-returns/generate via Swagger UI
```

**Commit final:**
```bash
git add .
git commit -m "feat: complete V2 implementation with all fields and tests"
```

---

## 📋 Checklist finale de validation

### Champs V2 à vérifier dans réponse API

- [ ] `lunar_phase.type` = une des 8 phases (new_moon, waxing_crescent, etc.)
- [ ] `lunar_phase.name` = nom français de la phase
- [ ] `lunar_phase.emoji` = emoji de la phase
- [ ] `lunar_phase.angle` = angle en degrés (0-360)
- [ ] `significant_aspects` = liste avec au moins un aspect ayant `score` (0-100)
- [ ] `dominant_aspect` = aspect avec score le plus élevé (ou null si aucun aspect)
- [ ] `focus.theme` = thème du focus (string)
- [ ] `focus.house` = numéro maison (1-12)
- [ ] `focus.keywords` = liste de keywords
- [ ] `suggestions.actions` = liste de suggestions (au moins 1)
- [ ] `suggestions.avoid` = liste (peut être vide)
- [ ] `suggestions.opportunities` = liste (peut être vide)
- [ ] `v2_payload` = object contenant tous les champs V2 ci-dessus
- [ ] `v2_version` = "2.0.0"

### Champs V1 à vérifier (compatibilité)

- [ ] `moon_sign` = signe de la Lune
- [ ] `moon_house` = maison de la Lune (1-12)
- [ ] `moon_degree` = degré de la Lune
- [ ] `aspects` = liste complète des aspects (non filtrés)
- [ ] `interpretation_keys` = clés d'interprétation V1

### Base de données Supabase

- [ ] Colonne `v2_version` existe et contient "2.0.0"
- [ ] Colonne `v2_payload` existe et contient JSON valide
- [ ] Index `idx_lunar_returns_v2_version` créé
- [ ] Index `idx_lunar_returns_v2_payload_gin` créé

---

## 🚨 En cas de problème

### Rollback migration

```bash
cd apps/api
alembic downgrade -1  # Revenir à la migration précédente
```

### Vérifier logs API

```bash
# Logs doivent montrer les calculs V2
tail -f logs/api.log  # Si logging configuré
```

### Test avec données existantes

```bash
# Vérifier que révolutions V1 existantes fonctionnent toujours
curl -X GET "http://localhost:8000/api/lunar-returns?user_id=USER_ID" | jq '.[0]'
# Doit retourner révolution V1 sans v2_version/v2_payload (normal)
```

---

**Statut:** ✅ Checklist prête pour exécution  
**Branche:** `feat/lunar-revolution-v2`  
**Commits recommandés:** 1 commit par étape (10 commits au total)

