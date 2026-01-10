# Analyse & Architecture V2 - Révolution Lunaire

## 📋 Liste des fichiers existants

### Backend (API FastAPI)

#### Routes
- `apps/api/routes/lunar_returns.py` - Endpoints REST pour révolutions lunaires
  - `POST /api/lunar-returns/generate` - Génère une révolution lunaire
  - `GET /api/lunar-returns` - Liste toutes les révolutions
  - `GET /api/lunar-returns/{id}` - Récupère une révolution par ID

#### Services
- `apps/api/services/lunar_return_service.py` - Logique métier principale
  - `calculate_lunar_return_date()` - Calcule la date exacte de révolution
  - `calculate_lunar_return_period()` - Calcule la période (start/end)
  - `calculate_planet_positions()` - Récupère positions via RapidAPI
  - `calculate_lunar_return()` - Fonction principale de calcul
  - `generate_interpretation_keys()` - Génère les clés d'interprétation
  - `create_lunar_return()` - Sauvegarde dans Supabase
  - `list_lunar_returns()` - Liste les révolutions
  - `get_lunar_return_by_id()` - Récupère par ID

- `apps/api/services/interpretations.py` - Générateur d'interprétations textuelles
  - `generate_lunar_return_interpretation()` - Génère texte interprétation
  - `get_moon_phase_description()` - Description phase lunaire
  - `_get_practical_advice()` - Conseils pratiques

- `apps/api/services/natal_reading_service.py` - Parsing positions/aspects
  - `parse_positions_from_natal_chart()` - Parse positions planètes
  - `parse_aspects_from_natal_chart()` - Parse aspects

#### Schémas
- `apps/api/schemas/lunar_return.py` - Modèles Pydantic
  - `LunarReturnGenerateRequest` - Request génération
  - `LunarReturnResponse` - Response complète
  - `UserProfileForLunarReturn` - Profil utilisateur

#### Modèles DB
- `apps/api/models/lunar_return.py` - Modèle SQLAlchemy (si existe)
- Table Supabase: `lunar_returns`

### Frontend Mobile (React Native / Expo)

#### Écrans existants
- `apps/mobile/app/lunar/index.tsx` - Écran Luna Pack (test API)
- `apps/mobile/app/lunar/report.tsx` - Écran détail rapport (mock data)
- `apps/mobile/app/lunar-month/` - Dossier vide (peut-être prévu)

#### Services API
- `apps/mobile/services/api.ts` - Client API
  - `lunarReturns.generate()` - POST /api/lunar-returns/generate
  - `lunarReturns.getAll()` - GET /api/lunar-returns
  - `lunarReturns.getByMonth()` - GET /api/lunar-returns/{month}

#### Stores
- ❌ **Aucun store Zustand pour révolutions lunaires** (à créer)
- Stores existants: `useAuthStore`, `useCalendarStore`, `useVocStore`, `useNatalStore`, `useCycleStore`

---

## 🔄 Flux de données actuel

### 1. Calcul Backend

```
User Request (cycle_number, user_id)
    ↓
routes/lunar_returns.py::generate_lunar_return()
    ↓
Récupération profil depuis Supabase (profiles table)
    ↓
lunar_return_service.py::calculate_lunar_return()
    ├─ calculate_lunar_return_date() → Date exacte révolution
    ├─ calculate_lunar_return_period() → Start/end dates
    ├─ calculate_planet_positions() → Appel RapidAPI
    │   └─ natal_reading_service::parse_positions_from_natal_chart()
    │   └─ natal_reading_service::parse_aspects_from_natal_chart()
    ├─ Extraction: moon_position, sun_position, ascendant
    ├─ generate_interpretation_keys() → Clés interprétation
    └─ Retourne Dict avec toutes les données
    ↓
create_lunar_return() → Sauvegarde Supabase (lunar_returns table)
    ↓
LunarReturnResponse retourné au client
```

### 2. Structure données retournées

```typescript
LunarReturnResponse {
  id: UUID
  user_id: UUID
  cycle_number: number
  start_date: datetime
  end_date: datetime
  
  // Position Lune
  moon_sign: string | null        // "Taurus", "Leo", etc.
  moon_degree: float | null       // 15.5
  moon_house: number | null       // 1-12
  
  // Autres positions
  ascendant_sign: string | null
  ascendant_degree: float | null
  sun_sign: string | null
  sun_degree: float | null
  
  // Données complètes
  planet_positions: {
    positions: Position[],
    raw_response: {}
  }
  
  // Aspects
  aspects: Aspect[]               // [{from, to, aspect_type, orb, strength}]
  
  // Clés interprétation (structure actuelle)
  interpretation_keys: {
    moon: { sign, house, theme },
    ascendant: { sign, theme },
    major_aspects_count: number,
    dominant_theme: string | null
  }
}
```

---

## 📍 Où sont définis les éléments demandés

### ✅ Signe lunaire (`moon_sign`)
- **Calculé**: `lunar_return_service.py::calculate_lunar_return()` ligne 202-224
- **Source**: Extrait de `positions` via RapidAPI (`parse_positions_from_natal_chart`)
- **Stocké**: `LunarReturnResponse.moon_sign` (Supabase: `lunar_returns.moon_sign`)

### ✅ Maison (`moon_house`)
- **Calculé**: Même source que signe lunaire (position Moon → `house`)
- **Stocké**: `LunarReturnResponse.moon_house` (Supabase: `lunar_returns.moon_house`)
- **Interprétation**: `interpretations.py::HOUSE_INTERPRETATIONS` (lignes 26-39)

### ⚠️ Phase (`phase`)
- **État actuel**: ❌ **PAS CALCULÉE** dans le service de révolution lunaire
- **Existe ailleurs**: `calendar_services.py::get_lunar_phases()` pour phases générales
- **Description**: `interpretations.py::get_moon_phase_description()` (lignes 129-143) mais non utilisée
- **Calcul nécessaire**: Basé sur la position du Soleil par rapport à la Lune (nouvelle/pleine/quartiers)

### ✅ Aspects (`aspects`)
- **Calculé**: `natal_reading_service.py::parse_aspects_from_natal_chart()` (lignes 211-266)
- **Source**: RapidAPI response → `chart_data.aspects`
- **Format**: `[{from, to, aspect_type, orb, strength, interpretation}]`
- **Stocké**: `LunarReturnResponse.aspects` (JSONB dans Supabase)

### ⚠️ Focus
- **État actuel**: ❌ **PAS EXPLICITE**, mais implicite via `interpretation_keys`
- **Calculé partiellement**: `generate_interpretation_keys()` ligne 154 (`dominant_theme: None`)
- **Logique implicite**: Basée sur `moon_house` → `HOUSE_INTERPRETATIONS`
- **À enrichir**: Focus devrait être une synthèse maison + aspects majeurs + signe

### ⚠️ Suggestions
- **État actuel**: ❌ **PAS GÉNÉRÉES**
- **Existe**: `interpretations.py::_get_practical_advice()` (lignes 105-126) mais limité
- **Utilisé dans**: `generate_lunar_return_interpretation()` mais pas exposé séparément
- **À créer**: Liste de suggestions actionnables basées sur signe + maison + aspects

---

## 🏗️ Architecture V2 proposée

### 1. Types TypeScript (Frontend) - Contrat V2 stable

```typescript
// apps/mobile/types/lunarReturn.ts

/**
 * Phase lunaire en 8 phases précises
 */
export type LunarPhase = 
  | 'new_moon'           // 0-44° (0-44.99°)
  | 'waxing_crescent'    // 45-89° (45-89.99°)
  | 'first_quarter'      // 90-134° (90-134.99°)
  | 'waxing_gibbous'     // 135-179° (135-179.99°)
  | 'full_moon'          // 180-224° (180-224.99°)
  | 'waning_gibbous'     // 225-269° (225-269.99°)
  | 'last_quarter'       // 270-314° (270-314.99°)
  | 'waning_crescent';   // 315-359° (315-359.99°)

/**
 * Contrat V2 - Structure alignée backend/frontend
 */
export interface LunarRevolutionV2 {
  // Identité
  id: string;
  cycle_number: number;
  start_date: string;
  end_date: string;
  
  // Position Lune
  moon_sign: string;           // "Taurus"
  moon_degree: number;         // 15.5
  moon_house: number;          // 2
  
  // Phase lunaire (CONTRAT: lunar_phase)
  lunar_phase: {
    type: LunarPhase;          // "waxing_crescent"
    name: string;              // "Premier croissant"
    emoji: string;             // "🌒"
    description: string;       // "Croissance et expansion"
    angle: number;             // Angle Soleil-Lune en degrés (0-360)
  };
  
  // Ascendant révolution
  ascendant_sign: string;
  ascendant_degree: number;
  
  // Aspects significatifs (CONTRAT: significant_aspects)
  significant_aspects: Aspect[];  // Aspects majeurs filtrés et scored
  
  // Aspect dominant (CONTRAT: dominant_aspect)
  dominant_aspect: Aspect | null; // Aspect avec score le plus élevé
  
  // Focus du mois (CONTRAT: focus)
  focus: {
    theme: string;             // "Stabilité financière"
    house: number;             // 2
    description: string;       // Texte explicatif du focus
    keywords: string[];        // ["finances", "valeurs", "ressources"]
  };
  
  // Suggestions actionnables (CONTRAT: suggestions)
  suggestions: {
    actions: string[];         // ["Fais un bilan de tes finances", "Investis dans ta stabilité"]
    avoid: string[];           // ["Évite les dépenses impulsives"]
    opportunities: string[];   // ["Période favorable pour investir"]
  };
  
  // Données complètes (gardées pour compatibilité)
  planet_positions?: any;
  all_aspects?: Aspect[];      // Tous les aspects (non filtrés)
  
  // Métadonnées
  v2_version: string;          // "2.0.0"
  generated_at: string;
  provider: string;            // "rapidapi" | "internal"
}

export interface Aspect {
  from: string;                // "Moon"
  to: string;                  // "Venus"
  aspect_type: string;         // "trine" (CONTRAT: aspect_type, pas "type")
  orb: number;                 // 3.2 (orbe en degrés)
  score: number;               // Score numérique (0-100) pour tri
  strength: 'strong' | 'medium' | 'weak';
  interpretation?: string;     // Texte d'interprétation
  emoji?: string;              // Emoji selon type
}
```

### 2. Fonctions de calcul Backend (à ajouter/enrichir)

#### Nouveau: Calcul phase lunaire (8 phases)

```python
# apps/api/services/lunar_return_service.py

def calculate_lunar_phase(
    sun_degree: float,
    moon_degree: float
) -> Dict[str, Any]:
    """
    Calcule la phase lunaire en 8 phases basée sur l'angle Soleil-Lune
    
    Mapping angle -> phase:
    - 0-44.99°     -> new_moon (Nouvelle Lune)
    - 45-89.99°    -> waxing_crescent (Premier croissant)
    - 90-134.99°   -> first_quarter (Premier quartier)
    - 135-179.99°  -> waxing_gibbous (Gibbeuse croissante)
    - 180-224.99°  -> full_moon (Pleine Lune)
    - 225-269.99°  -> waning_gibbous (Gibbeuse décroissante)
    - 270-314.99°  -> last_quarter (Dernier quartier)
    - 315-359.99°  -> waning_crescent (Dernier croissant)
    
    Returns:
        {
            "type": str,           # "waxing_crescent"
            "name": str,           # "Premier croissant"
            "emoji": str,          # "🌒"
            "description": str,    # "Croissance et expansion"
            "angle": float         # Angle en degrés (0-360)
        }
    """
    # Calculer angle Soleil-Lune (normalisé 0-360°)
    angle = (moon_degree - sun_degree) % 360
    
    # Mapping angle -> phase (8 phases précises)
    if 0 <= angle < 45:
        phase_type = "new_moon"
        phase_info = {
            "name": "Nouvelle Lune",
            "emoji": "🌑",
            "description": "Nouveau départ, intentions fraîches"
        }
    elif 45 <= angle < 90:
        phase_type = "waxing_crescent"
        phase_info = {
            "name": "Premier croissant",
            "emoji": "🌒",
            "description": "Croissance et expansion"
        }
    elif 90 <= angle < 135:
        phase_type = "first_quarter"
        phase_info = {
            "name": "Premier quartier",
            "emoji": "🌓",
            "description": "Action et décision"
        }
    elif 135 <= angle < 180:
        phase_type = "waxing_gibbous"
        phase_info = {
            "name": "Gibbeuse croissante",
            "emoji": "🌔",
            "description": "Affinage et ajustement"
        }
    elif 180 <= angle < 225:
        phase_type = "full_moon"
        phase_info = {
            "name": "Pleine Lune",
            "emoji": "🌕",
            "description": "Culmination et révélation"
        }
    elif 225 <= angle < 270:
        phase_type = "waning_gibbous"
        phase_info = {
            "name": "Gibbeuse décroissante",
            "emoji": "🌖",
            "description": "Récolte et gratitude"
        }
    elif 270 <= angle < 315:
        phase_type = "last_quarter"
        phase_info = {
            "name": "Dernier quartier",
            "emoji": "🌗",
            "description": "Lâcher-prise et tri"
        }
    else:  # 315 <= angle < 360
        phase_type = "waning_crescent"
        phase_info = {
            "name": "Dernier croissant",
            "emoji": "🌘",
            "description": "Repos et préparation"
        }
    
    return {
        "type": phase_type,
        **phase_info,
        "angle": round(angle, 2)
    }
```

#### Enrichi: Génération focus

```python
# apps/api/services/interpretations.py

def generate_focus(
    moon_house: int,
    moon_sign: str,
    major_aspects: List[Dict[str, Any]]
) -> Dict[str, Any]:
    """
    Génère le focus du mois (thème principal)
    
    Args:
        moon_house: Maison de la Lune (1-12)
        moon_sign: Signe de la Lune
        major_aspects: Liste des aspects majeurs
    
    Returns:
        {
            "theme": str,
            "house": int,
            "description": str,
            "keywords": List[str]
        }
    """
    # Base: interprétation maison
    house_theme = HOUSE_INTERPRETATIONS.get(moon_house, "")
    
    # Enrichir selon signe
    sign_keywords = _get_sign_keywords(moon_sign)
    
    # Enrichir selon aspects dominants
    aspect_keywords = []
    if major_aspects:
        dominant = max(major_aspects, key=lambda a: a.get("strength") == "strong")
        aspect_keywords = _get_aspect_keywords(dominant.get("type"))
    
    # Synthèse
    keywords = list(set(sign_keywords + aspect_keywords))
    
    return {
        "theme": _extract_theme_from_house(house_theme),
        "house": moon_house,
        "description": house_theme,
        "keywords": keywords
    }
```

#### Nouveau: Génération suggestions

```python
# apps/api/services/interpretations.py

def generate_suggestions(
    moon_house: int,
    moon_sign: str,
    ascendant_sign: str,
    aspects: List[Dict[str, Any]],
    phase: str
) -> Dict[str, Any]:
    """
    Génère des suggestions actionnables pour le mois
    
    Returns:
        {
            "actions": List[str],
            "avoid": List[str],
            "opportunities": List[str]
        }
    """
    suggestions = {
        "actions": [],
        "avoid": [],
        "opportunities": []
    }
    
    # Suggestions basées sur maison
    suggestions["actions"].extend(_get_house_actions(moon_house))
    
    # Suggestions basées sur signe
    suggestions["actions"].extend(_get_sign_actions(moon_sign))
    
    # Suggestions basées sur aspects
    challenging_aspects = [a for a in aspects if a.get("type") in ["square", "opposition"]]
    harmonious_aspects = [a for a in aspects if a.get("type") in ["trine", "sextile", "conjunction"]]
    
    if challenging_aspects:
        suggestions["avoid"].extend(_get_challenging_warnings(challenging_aspects))
    
    if harmonious_aspects:
        suggestions["opportunities"].extend(_get_harmonious_opportunities(harmonious_aspects))
    
    # Suggestions basées sur phase
    if phase == "new":
        suggestions["actions"].append("Plante des intentions pour ce nouveau cycle")
    elif phase == "full":
        suggestions["actions"].append("Célèbre tes accomplissements et lâche prise")
    
    return suggestions
```

#### Enrichi: Filtrage aspects significatifs avec scoring

```python
# apps/api/services/lunar_return_service.py

# Constantes pour filtrage aspects
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

def calculate_aspect_score(aspect: Dict[str, Any]) -> float:
    """
    Calcule un score numérique (0-100) pour un aspect
    
    Score = base_score (type) - orb_penalty (orbe) + strength_bonus (force)
    
    Args:
        aspect: Dict avec aspect_type, orb, strength
    
    Returns:
        Score numérique entre 0 et 100
    """
    aspect_type = aspect.get("aspect_type")
    orb = abs(aspect.get("orb", 999))
    strength = aspect.get("strength", "medium")
    
    # Score de base selon type
    base_score = ASPECT_BASE_SCORE.get(aspect_type, 0)
    
    # Pénalité selon orbe (orbe serré = meilleur)
    # Orbe 0° = 0 penalty, orbe 5° = 15 penalty
    orb_penalty = min(15, orb * 3)
    
    # Bonus selon force
    strength_bonus = {
        "strong": 10,
        "medium": 5,
        "weak": 0
    }.get(strength, 0)
    
    score = base_score - orb_penalty + strength_bonus
    
    # Normaliser entre 0 et 100
    return max(0, min(100, score))


def filter_significant_aspects(
    all_aspects: List[Dict[str, Any]],
    orb_threshold: float = ORB_THRESHOLD
) -> Dict[str, Any]:
    """
    Filtre, score et classe les aspects significatifs
    
    Règles de filtrage:
    1. Seulement aspects majeurs (conjunction, opposition, trine, square, sextile)
    2. Orbe <= orb_threshold (défaut: 5.0°)
    3. Calcul score pour chaque aspect
    4. Tri par score décroissant
    5. Sélection dominant = aspect avec score le plus élevé
    
    Returns:
        {
            "significant_aspects": List[Aspect],  # Aspects filtrés et scored
            "dominant_aspect": Aspect | None       # Aspect avec score max
        }
    """
    # 1. Filtrer aspects majeurs avec orbe acceptable
    significant_aspects = [
        a for a in all_aspects
        if a.get("aspect_type") in MAJOR_ASPECT_TYPES
        and abs(a.get("orb", 999)) <= orb_threshold
    ]
    
    # 2. Calculer score pour chaque aspect
    for aspect in significant_aspects:
        aspect["score"] = calculate_aspect_score(aspect)
    
    # 3. Trier par score décroissant (meilleur score = plus significatif)
    significant_aspects_sorted = sorted(
        significant_aspects,
        key=lambda a: a.get("score", 0),
        reverse=True
    )
    
    # 4. Sélectionner dominant (premier = score max)
    dominant_aspect = significant_aspects_sorted[0] if significant_aspects_sorted else None
    
    return {
        "significant_aspects": significant_aspects_sorted,
        "dominant_aspect": dominant_aspect
    }
```

### 3. Stratégie Base de Données (Migration V2)

```sql
-- Migration: Ajout colonnes V2 dans table lunar_returns

ALTER TABLE lunar_returns 
ADD COLUMN v2_version VARCHAR(10) DEFAULT NULL,
ADD COLUMN v2_payload JSONB DEFAULT NULL;

-- Index pour recherche rapide par version
CREATE INDEX idx_lunar_returns_v2_version ON lunar_returns(v2_version) 
WHERE v2_version IS NOT NULL;

-- Index GIN pour recherche dans v2_payload
CREATE INDEX idx_lunar_returns_v2_payload_gin ON lunar_returns USING GIN(v2_payload);
```

**Structure `v2_payload` (JSONB):**
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

**Logique de sauvegarde:**
- Anciens champs (`moon_sign`, `moon_house`, `aspects`, etc.) → **gardés pour compatibilité**
- Nouveaux champs V2 → **sauvegardés dans `v2_payload` JSONB**
- `v2_version` → **"2.0.0"** quand payload V2 présent
- Lecture: Si `v2_version` présent → utiliser `v2_payload`, sinon fallback ancien format

### 4. Store Zustand avec cache par mois (YYYY-MM)

```typescript
// apps/mobile/stores/useLunarRevolutionStore.ts

import { create } from 'zustand';
import { lunarReturns } from '@/services/api';
import type { LunarRevolutionV2 } from '@/types/lunarReturn';

interface LunarRevolutionState {
  // Cache par mois (clé: "YYYY-MM")
  cacheByMonth: Record<string, LunarRevolutionV2>;
  lastFetch: Record<string, number>;  // Timestamp dernier fetch
  loading: boolean;
  error: string | null;
  
  // Actions
  fetchForMonth: (month: string) => Promise<void>;  // "YYYY-MM"
  getForMonth: (month: string) => LunarRevolutionV2 | null;
  clearCache: () => void;
  isStale: (month: string) => boolean;
}

const TTL = 5 * 60 * 1000; // 5 minutes

export const useLunarRevolutionStore = create<LunarRevolutionState>((set, get) => ({
  cacheByMonth: {},
  lastFetch: {},
  loading: false,
  error: null,
  
  fetchForMonth: async (month: string) => {
    // Format attendu: "YYYY-MM"
    if (!/^\d{4}-\d{2}$/.test(month)) {
      set({ error: `Format mois invalide: ${month}. Attendu: YYYY-MM` });
      return;
    }
    
    // Vérifier cache
    const state = get();
    if (!state.isStale(month) && state.cacheByMonth[month]) {
      return; // Déjà en cache et frais
    }
    
    set({ loading: true, error: null });
    
    try {
      // TODO: Appel API (à adapter selon endpoint réel)
      // Pour l'instant, on suppose un endpoint GET /api/lunar-returns/month/{month}
      const response = await lunarReturns.getByMonth(month);
      
      // Transformer réponse API → LunarRevolutionV2 si nécessaire
      const revolution: LunarRevolutionV2 = response.v2_payload || response;
      
      set((state) => ({
        cacheByMonth: { ...state.cacheByMonth, [month]: revolution },
        lastFetch: { ...state.lastFetch, [month]: Date.now() },
        loading: false,
        error: null,
      }));
    } catch (error: any) {
      set({
        loading: false,
        error: error.message || 'Erreur lors du chargement de la révolution lunaire',
      });
    }
  },
  
  getForMonth: (month: string) => {
    const state = get();
    return state.cacheByMonth[month] || null;
  },
  
  clearCache: () => {
    set({
      cacheByMonth: {},
      lastFetch: {},
      error: null,
    });
  },
  
  isStale: (month: string) => {
    const state = get();
    const lastFetch = state.lastFetch[month];
    if (!lastFetch) return true;
    return Date.now() - lastFetch > TTL;
  },
}));
```

### 5. Composant UI V2 (React Native)

```typescript
// apps/mobile/components/lunarRevolution/LunarRevolutionScreen.tsx

export default function LunarRevolutionScreenV2() {
  const { revolution, loading, error } = useLunarRevolutionStore();
  
  if (loading) return <LoadingState />;
  if (error) return <ErrorState error={error} />;
  if (!revolution) return <EmptyState />;
  
  return (
    <ScrollView>
      {/* Header avec phase et période */}
      <RevolutionHeader 
        cycle={revolution.cycle_number}
        period={{ start: revolution.start_date, end: revolution.end_date }}
        phase={revolution.lunar_phase}
      />
      
      {/* Carte principale: Lune */}
      <MoonCard 
        sign={revolution.moon_sign}
        house={revolution.moon_house}
        degree={revolution.moon_degree}
      />
      
      {/* Aspects significatifs (CONTRAT: significant_aspects) */}
      {revolution.significant_aspects && revolution.significant_aspects.length > 0 ? (
        <AspectsCard 
          aspects={revolution.significant_aspects}
          dominant={revolution.dominant_aspect}
        />
      ) : (
        <NoSignificantAspectsCard />  {/* Gestion cas vide */}
      )}
      
      {/* Focus du mois (CONTRAT: focus) */}
      <FocusCard 
        theme={revolution.focus.theme}
        description={revolution.focus.description}
        keywords={revolution.focus.keywords}
      />
      
      {/* Suggestions actionnables (CONTRAT: suggestions) */}
      <SuggestionsCard 
        actions={revolution.suggestions.actions}
        avoid={revolution.suggestions.avoid}
        opportunities={revolution.suggestions.opportunities}
      />
      
      {/* Focus du mois (CONTRAT: focus) */}
      <FocusCard 
        theme={revolution.focus.theme}
        description={revolution.focus.description}
        keywords={revolution.focus.keywords}
      />
      
      {/* Suggestions actionnables (CONTRAT: suggestions) */}
      <SuggestionsCard 
        actions={revolution.suggestions.actions}
        avoid={revolution.suggestions.avoid}
        opportunities={revolution.suggestions.opportunities}
      />
      
      {/* Suggestions actionnables (NOUVEAU) */}
      <SuggestionsCard 
        actions={revolution.suggestions.actions}
        avoid={revolution.suggestions.avoid}
        opportunities={revolution.suggestions.opportunities}
      />
      
      {/* Interprétation complète */}
      <InterpretationCard 
        summary={revolution.interpretation.summary}
        full={revolution.interpretation.full}
        keyPoints={revolution.interpretation.key_points}
      />
    </ScrollView>
  );
}
```

### 6. Gestion états (loading/error/empty)

```typescript
// apps/mobile/components/lunarRevolution/states.tsx

export function LoadingState() {
  return (
    <View style={styles.centerContainer}>
      <ActivityIndicator size="large" color="#8B7BF7" />
      <Text style={styles.loadingText}>Calcul de ta révolution lunaire...</Text>
    </View>
  );
}

export function ErrorState({ error }: { error: string }) {
  return (
    <View style={styles.centerContainer}>
      <Text style={styles.errorEmoji}>❌</Text>
      <Text style={styles.errorTitle}>Erreur de chargement</Text>
      <Text style={styles.errorText}>{error}</Text>
      <TouchableOpacity onPress={() => refetch()}>
        <Text style={styles.retryButton}>Réessayer</Text>
      </TouchableOpacity>
    </View>
  );
}

export function EmptyState() {
  return (
    <View style={styles.centerContainer}>
      <Text style={styles.emptyEmoji}>🌙</Text>
      <Text style={styles.emptyTitle}>Aucune révolution disponible</Text>
      <Text style={styles.emptyText}>
        Configure ton thème natal pour calculer ta révolution lunaire.
      </Text>
    </View>
  );
}
```

### 7. Gestion "aucun aspect significatif" (sans être vide)

```typescript
// apps/mobile/components/lunarRevolution/NoSignificantAspectsCard.tsx

export function NoSignificantAspectsCard() {
  return (
    <Card variant="highlighted">
      <Text style={styles.cardTitle}>⭐ Aspects ce mois-ci</Text>
      <View style={styles.emptyAspectsContainer}>
        <Text style={styles.emptyAspectsEmoji}>✨</Text>
        <Text style={styles.emptyAspectsTitle}>
          Période d'harmonie lunaire
        </Text>
        <Text style={styles.emptyAspectsText}>
          Ce mois, ta Lune ne forme pas d'aspects majeurs avec les planètes.
          C'est une période de fluidité où tu peux te concentrer sur le{" "}
          <Text style={styles.focusText}>focus de la maison {revolution.focus.house}</Text>{" "}
          sans tensions particulières.
        </Text>
        <Text style={styles.emptyAspectsTip}>
          💡 Profite de cette énergie apaisée pour avancer sereinement.
        </Text>
      </View>
    </Card>
  );
}
```

---

## ✅ Todo List ordonnée (petites PRs/commits)

### Phase 1: Backend - Calcul phase lunaire
- [ ] **PR 1**: Ajouter fonction `calculate_lunar_phase()` dans `lunar_return_service.py`
- [ ] **PR 2**: Intégrer calcul phase dans `calculate_lunar_return()` et sauvegarder dans DB
- [ ] **Tests**: Tests unitaires `calculate_lunar_phase()` (angles 0°, 45°, 135°, 225°, 315°)

### Phase 2: Backend - Génération focus enrichi
- [ ] **PR 3**: Créer fonction `generate_focus()` dans `interpretations.py`
- [ ] **PR 4**: Intégrer `generate_focus()` dans `calculate_lunar_return()`
- [ ] **Tests**: Tests avec différentes maisons + signes + aspects

### Phase 3: Backend - Génération suggestions
- [ ] **PR 5**: Créer fonction `generate_suggestions()` dans `interpretations.py`
- [ ] **PR 6**: Créer helpers `_get_house_actions()`, `_get_sign_actions()`, etc.
- [ ] **PR 7**: Intégrer suggestions dans réponse API
- [ ] **Tests**: Tests suggestions selon différentes configurations

### Phase 4: Backend - Filtrage aspects significatifs
- [ ] **PR 8**: Créer fonction `filter_significant_aspects()` dans `lunar_return_service.py`
- [ ] **PR 9**: Enrichir aspects avec emoji + interprétation textuelle
- [ ] **Tests**: Tests filtrage (aspects majeurs vs mineurs, tri par orbe)

### Phase 5: Backend - Schéma réponse enrichi + DB V2
- [ ] **PR 10**: Mettre à jour `LunarReturnResponse` schema avec champs V2 (lunar_phase, significant_aspects, dominant_aspect, focus, suggestions)
- [ ] **PR 11**: Migration DB - Ajouter colonnes `v2_version` (VARCHAR) et `v2_payload` (JSONB)
- [ ] **PR 12**: Modifier `create_lunar_return()` pour sauvegarder V2 dans `v2_payload`
- [ ] **Tests**: Tests intégration complète end-to-end avec payload V2

### Phase 6: Frontend - Store Zustand avec cache par mois
- [ ] **PR 13**: Créer `apps/mobile/stores/useLunarRevolutionStore.ts`
  - État: `{ cacheByMonth: Record<string, LunarRevolutionV2>, lastFetch, loading, error }`
  - Actions: `fetchForMonth(month: "YYYY-MM")`, `getForMonth()`, `clearCache()`, `isStale()`
  - Cache par mois avec TTL (5 minutes comme autres stores)
- [ ] **Tests**: Tests store (chargement par mois, cache YYYY-MM, erreurs)

### Phase 7: Frontend - Types TypeScript
- [ ] **PR 13**: Créer `apps/mobile/types/lunarReturn.ts` avec types V2
- [ ] **PR 14**: Mapper réponse API → types frontend (fonction de transformation)

### Phase 8: Frontend - Composants UI
- [ ] **PR 15**: Créer `RevolutionHeader` (cycle, période, phase)
- [ ] **PR 16**: Créer `MoonCard` (signe, maison, degré)
- [ ] **PR 17**: Créer `FocusCard` (thème, description, keywords)
- [ ] **PR 18**: Créer `AspectsCard` (liste aspects + dominant)
- [ ] **PR 19**: Créer `NoSignificantAspectsCard` (cas aucun aspect)
- [ ] **PR 20**: Créer `SuggestionsCard` (actions, avoid, opportunities)
- [ ] **PR 21**: Créer `InterpretationCard` (summary, full, key points)
- [ ] **PR 22**: Créer états `LoadingState`, `ErrorState`, `EmptyState`

### Phase 9: Frontend - Écran principal V2
- [ ] **PR 23**: Créer `apps/mobile/app/lunar-month/[month].tsx` (route dynamique)
- [ ] **PR 24**: Intégrer tous les composants dans écran principal
- [ ] **PR 25**: Ajouter navigation mois précédent/suivant
- [ ] **Tests**: Tests snapshot composants + écran

### Phase 10: Intégration & Polish
- [ ] **PR 26**: Connecter store → API → écran
- [ ] **PR 27**: Ajouter analytics (track événements)
- [ ] **PR 28**: Ajouter haptics sur interactions
- [ ] **PR 29**: Tests E2E (chargement révolution, navigation mois)
- [ ] **PR 30**: Documentation utilisateur (README écran)

---

## 🧪 Tests à ajouter/adapter

### Backend (Python/Pytest)

#### Tests unitaires
```python
# tests/services/test_lunar_return_service.py

def test_calculate_lunar_phase():
    """Test calcul phase en 8 phases selon angle Soleil-Lune"""
    # Test new_moon (angle ~0°, ~44°)
    # Test waxing_crescent (angle ~45°, ~89°)
    # Test first_quarter (angle ~90°, ~134°)
    # Test waxing_gibbous (angle ~135°, ~179°)
    # Test full_moon (angle ~180°, ~224°)
    # Test waning_gibbous (angle ~225°, ~269°)
    # Test last_quarter (angle ~270°, ~314°)
    # Test waning_crescent (angle ~315°, ~359°)

def test_generate_focus():
    """Test génération focus selon maison + signe + aspects"""
    # Test maison 2 + Taureau → focus finances
    # Test maison 10 + Capricorne → focus carrière

def test_generate_suggestions():
    """Test génération suggestions"""
    # Test suggestions maison 2
    # Test suggestions avec aspects carrés (avoid)
    # Test suggestions avec aspects harmonieux (opportunities)

def test_filter_significant_aspects():
    """Test filtrage aspects significatifs avec scoring"""
    # Test filtrage aspects majeurs seulement (conjunction, opposition, trine, square, sextile)
    # Test filtrage orbe <= 5.0°
    # Test calcul score (base_score - orb_penalty + strength_bonus)
    # Test tri par score décroissant
    # Test sélection dominant_aspect (score max)
    # Test cas aucun aspect significatif
```

#### Tests d'intégration
```python
# tests/integration/test_lunar_returns_api.py

def test_generate_lunar_return_complete():
    """Test génération complète révolution lunaire V2"""
    # Vérifier présence lunar_phase, significant_aspects, dominant_aspect, focus, suggestions
    # Vérifier sauvegarde dans v2_payload JSONB
    # Vérifier v2_version = "2.0.0"

def test_lunar_return_with_no_significant_aspects():
    """Test cas aucun aspect significatif"""
    # Mock aspects mineurs seulement
    # Vérifier que réponse est valide (pas d'erreur)
```

### Frontend (Jest/React Native Testing Library)

#### Tests composants
```typescript
// __tests__/components/NoSignificantAspectsCard.test.tsx

describe('NoSignificantAspectsCard', () => {
  it('affiche message positif quand aucun aspect', () => {
    // Vérifier rendu avec emoji, titre, texte
  });
  
  it('affiche référence au focus du mois', () => {
    // Vérifier mention maison dans texte
  });
});

describe('LunarRevolutionScreenV2', () => {
  it('affiche LoadingState pendant chargement', () => {});
  it('affiche ErrorState en cas d\'erreur', () => {});
  it('affiche EmptyState si pas de données', () => {});
  it('affiche tous les composants si révolution chargée', () => {});
});
```

#### Tests store
```typescript
// __tests__/stores/useLunarRevolutionStore.test.ts

describe('useLunarRevolutionStore', () => {
  it('charge révolution depuis API pour un mois (YYYY-MM)', () => {});
  it('met en cache par mois avec TTL', () => {});
  it('retourne révolution depuis cache si frais', () => {});
  it('gère erreurs API', () => {});
  it('nettoie cache au clearCache()', () => {});
  it('valide format mois (YYYY-MM)', () => {});
});
```

---

## 📝 Notes importantes

1. **Compatibilité**: Garder compatibilité avec API existante pendant migration (anciens champs conservés)
2. **Performance**: Cache côté frontend (par mois YYYY-MM) + backend pour éviter recalculs
3. **Fallback**: Si phase/focus/suggestions non calculables, utiliser valeurs par défaut
4. **Localisation**: Tous les textes en français (comme demandé)
5. **Accessibilité**: Ajouter labels accessibles sur composants UI
6. **Migration DB**: Nouveaux champs V2 dans `v2_payload` JSONB pour éviter migrations complexes
7. **Versioning**: `v2_version` permet d'identifier les révolutions V2 vs anciennes

---

## 📊 Résumé des décisions V2

### ✅ Contrat V2 stable (noms alignés backend/frontend)
- `lunar_phase` (pas `phase`) → Structure avec type, name, emoji, description, angle
- `significant_aspects` (pas `aspects.major`) → Liste d'aspects filtrés et scored
- `dominant_aspect` (pas `aspects.dominant`) → Aspect unique avec score max
- `focus` → Structure avec theme, house, description, keywords
- `suggestions` → Structure avec actions, avoid, opportunities

### ✅ Phase lunaire en 8 phases précises
- Mapping angle → phase (0-44°=new_moon, 45-89°=waxing_crescent, etc.)
- 8 phases: new_moon, waxing_crescent, first_quarter, waxing_gibbous, full_moon, waning_gibbous, last_quarter, waning_crescent

### ✅ Filtrage aspects + scoring + sélection dominant
- Filtrage: Seulement aspects majeurs (conjunction, opposition, trine, square, sextile) avec orbe ≤ 5.0°
- Scoring: `score = base_score(type) - orb_penalty(orb) + strength_bonus(strength)` (0-100)
- Tri: Par score décroissant
- Dominant: Aspect avec score le plus élevé

### ✅ Stratégie DB: JSONB v2_payload + v2_version
- Colonnes: `v2_version` (VARCHAR) + `v2_payload` (JSONB)
- Anciens champs conservés pour compatibilité
- Index GIN sur `v2_payload` pour recherche rapide
- Logique: Si `v2_version` présent → utiliser `v2_payload`, sinon fallback ancien

### ✅ Store Zustand cache par mois YYYY-MM
- Clé de cache: Format "YYYY-MM" (ex: "2025-01")
- Structure: `cacheByMonth: Record<string, LunarRevolutionV2>`
- TTL: 5 minutes (comme autres stores)
- Actions: `fetchForMonth("YYYY-MM")`, `getForMonth()`, `clearCache()`, `isStale()`

