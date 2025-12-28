# Étape 1 & 2 - Implémentation Fonctions V2 (Phase Lunaire + Scoring Aspects)

**Date:** 2025-01-XX  
**Branche:** `feat/lunar-revolution-v2`  
**Statut:** ✅ Implémenté (non intégré dans calculate_lunar_return)

---

## 📋 Résumé

Implémentation des fonctions pures pour le calcul V2 :
1. **`calculate_lunar_phase()`** : Calcul de la phase lunaire en 8 phases
2. **`calculate_aspect_score()`** : Calcul du score numérique d'un aspect
3. **`filter_significant_aspects()`** : Filtrage et scoring des aspects significatifs

**⚠️ Important:** Ces fonctions ne sont **pas encore intégrées** dans `calculate_lunar_return()`. Elles sont prêtes à être utilisées lors des prochaines étapes.

---

## 📁 Fichier modifié

**Fichier:** `apps/api/services/lunar_return_service.py`

### Position des ajouts

- **`calculate_lunar_phase()`** : Ajoutée après `calculate_lunar_return_period()` (ligne 73)
- **Constantes V2** : Ajoutées après `calculate_lunar_phase()` (lignes 174-185)
- **`calculate_aspect_score()`** : Ajoutée après les constantes (ligne 188)
- **`filter_significant_aspects()`** : Ajoutée après `calculate_aspect_score()` (ligne 230)

---

## 🔧 Fonction 1: `calculate_lunar_phase()`

### Signature

```python
def calculate_lunar_phase(moon_longitude: float, sun_longitude: float) -> Dict[str, Any]
```

### Description

Calcule la phase lunaire en 8 phases basée sur l'angle Soleil-Lune (longitude écliptique 0-360°).

### Mapping angle → phase

| Angle | Phase | Nom français | Emoji |
|-------|-------|--------------|-------|
| 0-44.99° | `new_moon` | Nouvelle Lune | 🌑 |
| 45-89.99° | `waxing_crescent` | Premier croissant | 🌒 |
| 90-134.99° | `first_quarter` | Premier quartier | 🌓 |
| 135-179.99° | `waxing_gibbous` | Gibbeuse croissante | 🌔 |
| 180-224.99° | `full_moon` | Pleine Lune | 🌕 |
| 225-269.99° | `waning_gibbous` | Gibbeuse décroissante | 🌖 |
| 270-314.99° | `last_quarter` | Dernier quartier | 🌗 |
| 315-359.99° | `waning_crescent` | Dernier croissant | 🌘 |

### Retour

```python
{
    "type": "waxing_crescent",           # Type de phase
    "name": "Premier croissant",         # Nom français
    "emoji": "🌒",                       # Emoji
    "description": "Croissance et expansion",  # Description
    "angle": 67.5                        # Angle calculé (0-360°)
}
```

### Exemple d'utilisation

```python
from services.lunar_return_service import calculate_lunar_phase

# Angle = 180° (Pleine Lune)
phase = calculate_lunar_phase(280.0, 100.0)  # moon_longitude - sun_longitude = 180°
assert phase["type"] == "full_moon"
assert phase["angle"] == 180.0
```

---

## 🔧 Fonction 2: `calculate_aspect_score()`

### Signature

```python
def calculate_aspect_score(aspect: Dict[str, Any]) -> int
```

### Description

Calcule un score numérique (0-100) pour un aspect astrologique selon la formule :

```
score = base_score(type) - orb_penalty(orb) + strength_bonus(strength)
```

### Scores de base par type

| Type d'aspect | Score de base |
|---------------|---------------|
| `conjunction` | 30 |
| `opposition` | 25 |
| `square` | 20 |
| `trine` | 15 |
| `sextile` | 10 |

### Pénalité orbe

- Orbe 0° = 0 pénalité
- Orbe 5° = 15 pénalité (maximum)
- Formule : `min(15, orb * 3)`

### Bonus force

| Force | Bonus |
|-------|-------|
| `strong` | +10 |
| `medium` | +5 |
| `weak` | 0 |

### Retour

Score entier entre 0 et 100 (clampé).

### Exemple d'utilisation

```python
from services.lunar_return_service import calculate_aspect_score

aspect = {
    "aspect_type": "trine",
    "orb": 2.0,
    "strength": "strong"
}
score = calculate_aspect_score(aspect)
# score = 15 (base) - 6 (orb_penalty) + 10 (strength_bonus) = 19
```

---

## 🔧 Fonction 3: `filter_significant_aspects()`

### Signature

```python
def filter_significant_aspects(aspects: List[Dict[str, Any]]) -> List[Dict[str, Any]]
```

### Description

Filtre, score et trie les aspects significatifs selon les critères V2.

### Critères de filtrage

1. **Types d'aspects acceptés :** `conjunction`, `opposition`, `trine`, `square`, `sextile`
2. **Orbe maximum :** ≤ 5.0° (valeur absolue)

### Traitement

Pour chaque aspect significatif :
1. Calcule un score via `calculate_aspect_score()`
2. Ajoute le champ `"score"` à l'aspect (modifie le dictionnaire)
3. Trie par score décroissant

### Retour

Liste d'aspects filtrés, avec champ `"score"` ajouté, triée par score décroissant.

### Exemple d'utilisation

```python
from services.lunar_return_service import filter_significant_aspects

aspects = [
    {"aspect_type": "trine", "orb": 2.0, "strength": "strong", "from": "Moon", "to": "Venus"},
    {"aspect_type": "square", "orb": 4.5, "strength": "medium", "from": "Moon", "to": "Mars"},
    {"aspect_type": "sextile", "orb": 6.0, "strength": "weak", "from": "Moon", "to": "Jupiter"},  # Exclu (orbe > 5°)
]

significant = filter_significant_aspects(aspects)
# Retourne 2 aspects (sextile exclu), avec champ "score" ajouté, triés par score décroissant
```

---

## 📊 Constantes ajoutées

```python
# Constantes pour filtrage aspects V2
MAJOR_ASPECT_TYPES = ["conjunction", "opposition", "trine", "square", "sextile"]
ORB_THRESHOLD = 5.0  # Orbe maximum accepté (en degrés)

# Scores de base par type d'aspect (pour calcul score numérique)
ASPECT_BASE_SCORE = {
    "conjunction": 30,
    "opposition": 25,
    "square": 20,
    "trine": 15,
    "sextile": 10
}
```

---

## 🔍 Diff du fichier

```diff
--- a/apps/api/services/lunar_return_service.py
+++ b/apps/api/services/lunar_return_service.py
@@ -71,6 +71,206 @@ def calculate_lunar_return_period(lunar_return_date: datetime) -> tuple[datetim
     return (start_date, end_date)
 
 
+def calculate_lunar_phase(moon_longitude: float, sun_longitude: float) -> Dict[str, Any]:
+    """
+    Calcule la phase lunaire en 8 phases basée sur l'angle Soleil-Lune
+    
+    La phase lunaire est déterminée par l'angle entre le Soleil et la Lune,
+    mesuré en longitude écliptique (0-360°).
+    
+    Mapping angle -> phase:
+    - 0-44.99°     -> new_moon (Nouvelle Lune)
+    - 45-89.99°    -> waxing_crescent (Premier croissant)
+    - 90-134.99°   -> first_quarter (Premier quartier)
+    - 135-179.99°  -> waxing_gibbous (Gibbeuse croissante)
+    - 180-224.99°  -> full_moon (Pleine Lune)
+    - 225-269.99°  -> waning_gibbous (Gibbeuse décroissante)
+    - 270-314.99°  -> last_quarter (Dernier quartier)
+    - 315-359.99°  -> waning_crescent (Dernier croissant)
+    
+    Args:
+        moon_longitude: Longitude écliptique de la Lune (0-360°)
+        sun_longitude: Longitude écliptique du Soleil (0-360°)
+    
+    Returns:
+        Dictionnaire contenant:
+        {
+            "type": str,           # "waxing_crescent"
+            "name": str,           # "Premier croissant"
+            "emoji": str,          # "🌒"
+            "description": str,    # "Croissance et expansion"
+            "angle": float         # Angle en degrés (0-360)
+        }
+    """
+    # Calculer l'angle Soleil-Lune (normalisé 0-360°)
+    # angle = (moon_longitude - sun_longitude) % 360
+    angle = (moon_longitude - sun_longitude) % 360
+    
+    # Mapping angle -> phase (8 phases précises)
+    if 0 <= angle < 45:
+        phase_type = "new_moon"
+        phase_info = {
+            "name": "Nouvelle Lune",
+            "emoji": "🌑",
+            "description": "Nouveau départ, intentions fraîches"
+        }
+    elif 45 <= angle < 90:
+        phase_type = "waxing_crescent"
+        phase_info = {
+            "name": "Premier croissant",
+            "emoji": "🌒",
+            "description": "Croissance et expansion"
+        }
+    elif 90 <= angle < 135:
+        phase_type = "first_quarter"
+        phase_info = {
+            "name": "Premier quartier",
+            "emoji": "🌓",
+            "description": "Action et décision"
+        }
+    elif 135 <= angle < 180:
+        phase_type = "waxing_gibbous"
+        phase_info = {
+            "name": "Gibbeuse croissante",
+            "emoji": "🌔",
+            "description": "Affinage et ajustement"
+        }
+    elif 180 <= angle < 225:
+        phase_type = "full_moon"
+        phase_info = {
+            "name": "Pleine Lune",
+            "emoji": "🌕",
+            "description": "Culmination et révélation"
+        }
+    elif 225 <= angle < 270:
+        phase_type = "waning_gibbous"
+        phase_info = {
+            "name": "Gibbeuse décroissante",
+            "emoji": "🌖",
+            "description": "Récolte et gratitude"
+        }
+    elif 270 <= angle < 315:
+        phase_type = "last_quarter"
+        phase_info = {
+            "name": "Dernier quartier",
+            "emoji": "🌗",
+            "description": "Lâcher-prise et tri"
+        }
+    else:  # 315 <= angle < 360
+        phase_type = "waning_crescent"
+        phase_info = {
+            "name": "Dernier croissant",
+            "emoji": "🌘",
+            "description": "Repos et préparation"
+        }
+    
+    return {
+        "type": phase_type,
+        **phase_info,
+        "angle": round(angle, 2)
+    }
+
+
+# Constantes pour filtrage aspects V2
+MAJOR_ASPECT_TYPES = ["conjunction", "opposition", "trine", "square", "sextile"]
+ORB_THRESHOLD = 5.0  # Orbe maximum accepté (en degrés)
+
+# Scores de base par type d'aspect (pour calcul score numérique)
+ASPECT_BASE_SCORE = {
+    "conjunction": 30,
+    "opposition": 25,
+ "square": 20,
+    "trine": 15,
+    "sextile": 10
+}
+
+
+def calculate_aspect_score(aspect: Dict[str, Any]) -> int:
+    """
+    Calcule un score numérique (0-100) pour un aspect astrologique
+    
+    Le score est calculé selon la formule:
+    score = base_score(type) - orb_penalty(orb) + strength_bonus(strength)
+    
+    - base_score: Score de base selon le type d'aspect (conjunction = 30, opposition = 25, etc.)
+    - orb_penalty: Pénalité basée sur l'orbe (plus l'orbe est grand, plus la pénalité est élevée)
+    - strength_bonus: Bonus selon la force de l'aspect (strong = +10, medium = +5, weak = 0)
+    
+    Le score final est clampé entre 0 et 100.
+    
+    Args:
+        aspect: Dictionnaire contenant:
+            - aspect_type: str (conjunction, opposition, trine, square, sextile)
+            - orb: float (orbe en degrés, valeur absolue)
+            - strength: str ("strong", "medium", "weak")
+    
+    Returns:
+        Score entier entre 0 et 100
+    """
+    aspect_type = aspect.get("aspect_type", "")
+    orb = abs(aspect.get("orb", 999))  # Valeur absolue de l'orbe
+    strength = aspect.get("strength", "medium")
+    
+    # Score de base selon le type d'aspect
+    base_score = ASPECT_BASE_SCORE.get(aspect_type, 0)
+    
+    # Pénalité basée sur l'orbe (orbe 0° = 0 penalty, orbe 5° = 15 penalty max)
+    orb_penalty = min(15, orb * 3)
+    
+    # Bonus selon la force de l'aspect
+    strength_bonus = {"strong": 10, "medium": 5, "weak": 0}.get(strength, 0)
+    
+    # Calcul du score final
+    score = base_score - orb_penalty + strength_bonus
+    
+    # Clamp entre 0 et 100
+    return max(0, min(100, int(score)))
+
+
+def filter_significant_aspects(aspects: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
+    """
+    Filtre, score et trie les aspects significatifs selon les critères V2
+    
+    Critères de filtrage:
+    - Seulement les aspects majeurs: conjunction, opposition, trine, square, sextile
+    - Orbe maximum: ≤ 5.0° (valeur absolue)
+    
+    Pour chaque aspect significatif:
+    - Calcule un score numérique (0-100) via calculate_aspect_score()
+    - Ajoute le champ "score" à l'aspect
+    - Trie par score décroissant
+    
+    Args:
+        aspects: Liste de dictionnaires d'aspects (format de parse_aspects_from_natal_chart)
+                 Chaque aspect contient: from, to, aspect_type, orb, strength, etc.
+    
+    Returns:
+        Liste d'aspects filtrés, avec champ "score" ajouté, triée par score décroissant
+    """
+    # Filtrer aspects majeurs avec orbe acceptable
+    significant_aspects = [
+        aspect for aspect in aspects
+        if aspect.get("aspect_type") in MAJOR_ASPECT_TYPES
+        and abs(aspect.get("orb", 999)) <= ORB_THRESHOLD
+    ]
+    
+    # Calculer et ajouter le score pour chaque aspect significatif
+    for aspect in significant_aspects:
+        aspect["score"] = calculate_aspect_score(aspect)
+    
+    # Trier par score décroissant
+    significant_aspects_sorted = sorted(
+        significant_aspects,
+        key=lambda a: a.get("score", 0),
+        reverse=True
+    )
+    
+    return significant_aspects_sorted
+
+
 async def calculate_planet_positions(
```

---

## ✅ Vérifications effectuées

- [x] Syntaxe Python valide (`py_compile` OK)
- [x] Aucune erreur de linter
- [x] Fonctions pures (pas de dépendances DB/API)
- [x] Commentaires en français
- [x] Respect des spécifications (8 phases, scoring, filtrage)
- [x] Non intégrées dans `calculate_lunar_return()` (comme demandé)

---

## 📝 Message de commit recommandé

```bash
git add apps/api/services/lunar_return_service.py
git commit -m "feat: add V2 phase calculation and aspect scoring functions

- Add calculate_lunar_phase(): 8-phase lunar phase calculation (0-360° angle)
- Add calculate_aspect_score(): numeric scoring (0-100) for aspects
- Add filter_significant_aspects(): filter and score significant aspects
- Add constants: MAJOR_ASPECT_TYPES, ORB_THRESHOLD, ASPECT_BASE_SCORE

Functions are pure (no DB/API dependencies) and ready for integration.
Not yet integrated in calculate_lunar_return() (step 1 & 2 only)."
```

---

## ⚠️ Notes importantes

1. **Longitude absolue requise :** `calculate_lunar_phase()` nécessite les longitudes absolues (0-360°), pas seulement le degré dans le signe (0-30°). Lors de l'intégration, il faudra extraire `absolute_longitude` depuis le `raw_response` de RapidAPI.

2. **Modification in-place :** `filter_significant_aspects()` modifie les dictionnaires d'aspects en ajoutant le champ `"score"`. C'est intentionnel pour éviter de créer de nouvelles structures.

3. **Aspects V1 préservés :** La fonction `filter_significant_aspects()` ne modifie pas la liste d'origine, elle retourne une nouvelle liste filtrée. Les aspects originaux (V1) restent intacts.

---

## 🎯 Prochaines étapes

Lors de l'intégration dans `calculate_lunar_return()` (étapes suivantes) :

1. Extraire `absolute_longitude` depuis `raw_response` pour Moon et Sun
2. Appeler `calculate_lunar_phase(moon_longitude, sun_longitude)`
3. Appeler `filter_significant_aspects(aspects)` pour obtenir les aspects significatifs
4. Sélectionner le dominant (premier de la liste triée)

