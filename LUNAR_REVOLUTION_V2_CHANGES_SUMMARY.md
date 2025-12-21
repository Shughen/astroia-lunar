# Résumé des modifications V2 - Révolution Lunaire

## 📊 Décisions principales

1. **Contrat V2 stable** : Noms alignés backend/frontend (`lunar_phase`, `significant_aspects`, `dominant_aspect`, `focus`, `suggestions`)
2. **Phase lunaire en 8 phases** : Mapping angle → phase précise (0-44°, 45-89°, etc.)
3. **Filtrage aspects + scoring** : Score numérique (0-100) + sélection dominant par score max
4. **Stratégie DB** : Colonne JSONB `v2_payload` + `v2_version` pour migration progressive
5. **Store Zustand** : Cache par mois format "YYYY-MM" avec TTL 5 minutes

---

## 🔄 Avant/Après des sections modifiées

### 1. Types TypeScript (Contrat V2)

#### ❌ AVANT
```typescript
export type LunarPhase = 'new' | 'waxing' | 'full' | 'waning';

export interface LunarRevolutionV2 {
  // Structure imbriquée
  moon: { sign, sign_emoji, degree, house, house_name };
  phase: { type, name, emoji, description, date? };
  aspects: { major, all, count, dominant? };
  // ...
}
```

#### ✅ APRÈS
```typescript
// 8 phases précises
export type LunarPhase = 
  | 'new_moon' | 'waxing_crescent' | 'first_quarter' | 'waxing_gibbous'
  | 'full_moon' | 'waning_gibbous' | 'last_quarter' | 'waning_crescent';

export interface LunarRevolutionV2 {
  // Champs plats alignés backend
  moon_sign: string;
  moon_degree: number;
  moon_house: number;
  
  // CONTRAT V2: noms stables
  lunar_phase: { type, name, emoji, description, angle };
  significant_aspects: Aspect[];
  dominant_aspect: Aspect | null;
  focus: { theme, house, description, keywords };
  suggestions: { actions, avoid, opportunities };
  // ...
}

export interface Aspect {
  aspect_type: string;  // Pas "type"
  score: number;        // Score numérique 0-100
  // ...
}
```

**Changements clés:**
- ✅ Structure plate (pas imbriquée) pour `moon_sign`, `moon_degree`, `moon_house`
- ✅ `phase` → `lunar_phase` (nom stable)
- ✅ `aspects.major` → `significant_aspects` (liste directe)
- ✅ `aspects.dominant` → `dominant_aspect` (champ séparé)
- ✅ 8 phases au lieu de 4
- ✅ Score numérique ajouté dans `Aspect`

---

### 2. Calcul phase lunaire

#### ❌ AVANT
```python
# 4 phases seulement
if angle < 45 or angle >= 315:
    phase_type = "new"
elif 45 <= angle < 135:
    phase_type = "waxing"
elif 135 <= angle < 225:
    phase_type = "full"
else:
    phase_type = "waning"
```

#### ✅ APRÈS
```python
# 8 phases précises avec mapping angle
if 0 <= angle < 45:
    phase_type = "new_moon"           # 0-44.99°
elif 45 <= angle < 90:
    phase_type = "waxing_crescent"    # 45-89.99°
elif 90 <= angle < 135:
    phase_type = "first_quarter"      # 90-134.99°
elif 135 <= angle < 180:
    phase_type = "waxing_gibbous"     # 135-179.99°
elif 180 <= angle < 225:
    phase_type = "full_moon"          # 180-224.99°
elif 225 <= angle < 270:
    phase_type = "waning_gibbous"     # 225-269.99°
elif 270 <= angle < 315:
    phase_type = "last_quarter"       # 270-314.99°
else:  # 315 <= angle < 360
    phase_type = "waning_crescent"    # 315-359.99°
```

**Changements clés:**
- ✅ 8 phases au lieu de 4
- ✅ Mapping angle précis par tranche de 45°
- ✅ Retourne `angle` dans la structure (pour debug/affichage)

---

### 3. Filtrage aspects + scoring

#### ❌ AVANT
```python
# Tri simple par orbe (plus serré = meilleur)
major_aspects_sorted = sorted(major_aspects, key=lambda a: abs(a.get("orb", 999)))
dominant = major_aspects_sorted[0] if major_aspects_sorted else None
```

#### ✅ APRÈS
```python
# Scoring numérique avec formule
def calculate_aspect_score(aspect):
    base_score = ASPECT_BASE_SCORE[aspect_type]      # 10-30 selon type
    orb_penalty = min(15, orb * 3)                   # Pénalité orbe
    strength_bonus = {"strong": 10, "medium": 5, "weak": 0}[strength]
    return max(0, min(100, base_score - orb_penalty + strength_bonus))

# Tri par score décroissant
significant_aspects_sorted = sorted(
    significant_aspects,
    key=lambda a: a.get("score", 0),
    reverse=True
)
dominant_aspect = significant_aspects_sorted[0]  # Score max
```

**Changements clés:**
- ✅ Score numérique (0-100) au lieu de simple tri par orbe
- ✅ Formule: `score = base_score - orb_penalty + strength_bonus`
- ✅ Tri par score décroissant (meilleur score = plus significatif)
- ✅ Sélection dominant basée sur score max (pas seulement orbe)

---

### 4. Stratégie Base de Données

#### ❌ AVANT
```sql
-- Pas de stratégie explicite
-- Nouveaux champs à ajouter directement dans table
ALTER TABLE lunar_returns ADD COLUMN phase VARCHAR(...);
ALTER TABLE lunar_returns ADD COLUMN focus JSONB;
-- etc. (migrations multiples)
```

#### ✅ APRÈS
```sql
-- Migration unique avec JSONB
ALTER TABLE lunar_returns 
ADD COLUMN v2_version VARCHAR(10) DEFAULT NULL,
ADD COLUMN v2_payload JSONB DEFAULT NULL;

CREATE INDEX idx_lunar_returns_v2_payload_gin 
ON lunar_returns USING GIN(v2_payload);
```

**Structure `v2_payload` JSONB:**
```json
{
  "lunar_phase": { ... },
  "significant_aspects": [ ... ],
  "dominant_aspect": { ... },
  "focus": { ... },
  "suggestions": { ... }
}
```

**Changements clés:**
- ✅ Migration unique (2 colonnes au lieu de multiples)
- ✅ JSONB flexible pour évolution future
- ✅ Index GIN pour recherche rapide
- ✅ `v2_version` pour identifier révolutions V2
- ✅ Anciens champs conservés (compatibilité)

---

### 5. Store Zustand

#### ❌ AVANT
```typescript
// Pas de store défini (à créer)
// Pas de stratégie de cache claire
```

#### ✅ APRÈS
```typescript
interface LunarRevolutionState {
  // Cache par mois (clé: "YYYY-MM")
  cacheByMonth: Record<string, LunarRevolutionV2>;
  lastFetch: Record<string, number>;
  
  fetchForMonth: (month: string) => Promise<void>;  // "YYYY-MM"
  getForMonth: (month: string) => LunarRevolutionV2 | null;
  isStale: (month: string) => boolean;
  clearCache: () => void;
}

// Usage
fetchForMonth("2025-01");  // Format YYYY-MM
getForMonth("2025-01");
```

**Changements clés:**
- ✅ Cache par mois format "YYYY-MM" (pas par cycle_number)
- ✅ TTL 5 minutes (aligné avec autres stores)
- ✅ Validation format mois (regex `^\d{4}-\d{2}$`)
- ✅ Structure `Record<string, LunarRevolutionV2>` pour cache multi-mois

---

### 6. Composant UI (références aux champs)

#### ❌ AVANT
```typescript
// Références à structure imbriquée
<MoonCard 
  sign={revolution.moon.sign}
  house={revolution.moon.house}
  degree={revolution.moon.degree}
/>
<AspectsCard 
  aspects={revolution.aspects.major}
  dominant={revolution.aspects.dominant}
/>
```

#### ✅ APRÈS
```typescript
// Références à champs plats (contrat V2)
<MoonCard 
  sign={revolution.moon_sign}
  house={revolution.moon_house}
  degree={revolution.moon_degree}
/>
<AspectsCard 
  aspects={revolution.significant_aspects}
  dominant={revolution.dominant_aspect}
/>
<FocusCard 
  theme={revolution.focus.theme}
  description={revolution.focus.description}
  keywords={revolution.focus.keywords}
/>
```

**Changements clés:**
- ✅ Accès direct aux champs (pas imbriqué)
- ✅ Noms stables (`lunar_phase`, `significant_aspects`, etc.)
- ✅ `dominant_aspect` séparé (pas dans `aspects.dominant`)

---

## 📝 Résumé des décisions

### ✅ Contrat V2 stable
**Noms alignés backend/frontend:**
- `lunar_phase` (structure avec type, name, emoji, description, angle)
- `significant_aspects` (liste d'aspects filtrés et scored)
- `dominant_aspect` (aspect unique avec score max)
- `focus` (structure avec theme, house, description, keywords)
- `suggestions` (structure avec actions, avoid, opportunities)

### ✅ Phase lunaire en 8 phases
**Mapping angle → phase:**
- 0-44.99° → `new_moon`
- 45-89.99° → `waxing_crescent`
- 90-134.99° → `first_quarter`
- 135-179.99° → `waxing_gibbous`
- 180-224.99° → `full_moon`
- 225-269.99° → `waning_gibbous`
- 270-314.99° → `last_quarter`
- 315-359.99° → `waning_crescent`

### ✅ Filtrage aspects + scoring
**Règles:**
1. Seulement aspects majeurs (conjunction, opposition, trine, square, sextile)
2. Orbe ≤ 5.0°
3. Score = `base_score(type) - orb_penalty(orb) + strength_bonus(strength)` (0-100)
4. Tri par score décroissant
5. Dominant = aspect avec score max

### ✅ Stratégie DB: JSONB v2_payload + v2_version
- Colonnes: `v2_version` (VARCHAR) + `v2_payload` (JSONB)
- Anciens champs conservés (compatibilité)
- Index GIN sur `v2_payload`
- Logique: Si `v2_version` présent → utiliser `v2_payload`, sinon fallback

### ✅ Store Zustand cache par mois YYYY-MM
- Clé: Format "YYYY-MM" (ex: "2025-01")
- Structure: `cacheByMonth: Record<string, LunarRevolutionV2>`
- TTL: 5 minutes
- Actions: `fetchForMonth("YYYY-MM")`, `getForMonth()`, `clearCache()`, `isStale()`

---

## 🎯 Impact sur l'implémentation

### Backend
1. Ajouter fonction `calculate_lunar_phase()` avec 8 phases
2. Ajouter fonction `calculate_aspect_score()` + `filter_significant_aspects()`
3. Migration DB: Ajouter `v2_version` + `v2_payload` JSONB
4. Modifier `calculate_lunar_return()` pour générer payload V2
5. Sauvegarder payload V2 dans `v2_payload` JSONB

### Frontend
1. Créer types TypeScript avec contrat V2 stable
2. Créer store Zustand avec cache par mois YYYY-MM
3. Mapper réponse API (`v2_payload`) → types frontend
4. Mettre à jour composants UI pour utiliser nouveaux noms de champs

### Tests
1. Tests calcul phase (8 phases, tous les angles limites)
2. Tests scoring aspects (formule, tri, sélection dominant)
3. Tests store (cache YYYY-MM, TTL, validation format)
4. Tests intégration (génération complète, sauvegarde JSONB)

