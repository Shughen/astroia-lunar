# 🌟 Interprétations Thème Natal - V2 Complète

**Date:** 2025-12-29
**Version:** 2.0
**Changement majeur:** Refonte complète du prompt + Sonnet + fallback Haiku

---

## 📝 Résumé des Changements

### ✅ Nouveau Template Markdown (Signature Astroia)

```markdown
# {emoji} {Sujet} en {Signe}
**En une phrase :** ...

## Ton moteur
...

## Ton défi
...

## La maison {N} en clair
...

## Micro-rituel du jour (2 min)
- ...
```

### ✅ Modèle Claude

- **Priorité:** Sonnet 3.5 (`claude-3-5-sonnet-20241022`)
- **Fallback:** Haiku (`claude-3-haiku-20240307`) si Sonnet échoue (429, timeout, 5xx)
- **Validation longueur:** 900-1200 chars (max 1400)
- **Retry:** 1x si hors limites avec prompt d'ajustement

### ✅ Cache Key Stable

- **chart_id:** Hash MD5 de `(birth_date, birth_time, lat, lon, timezone, house_system)`
- **SANS** la version du prompt (séparé dans colonne `version`)
- **Cache hit:** `(user_id, chart_id, subject, lang, version=2)`

### ✅ UI Mobile Simplifiée

- **Header:** `{emoji} {Nom}` (ex: "☀️ Soleil")
- **Sous-titre:** `Maison N (description)` (discret)
- **Contenu:** Markdown avec styles custom
- **Bouton "Régénérer":** `force_refresh=true` → bypass cache

---

## 📂 Fichiers Modifiés

### Backend (Python)

#### 1. **`apps/api/services/natal_interpretation_service.py`** ⚠️ **REFACTO COMPLÈTE**

**Nouveau:**
```python
# Version prompt
PROMPT_VERSION = 2

# Fonctions
def build_interpretation_prompt_v2(subject, chart_payload) -> str
def get_house_label_v2(house_num) -> Tuple[str, str]
def find_relevant_aspect(subject, chart_payload) -> Optional[str]
def validate_interpretation_length(text) -> Tuple[bool, int]
async def generate_with_sonnet_fallback_haiku(subject, chart_payload) -> Tuple[str, str]
```

**Supprimé:**
- `build_interpretation_prompt()` (v1)
- `generate_interpretation_with_claude()` (v1)

**Changements clés:**
- Prompt v2 avec template exact (# Ton moteur, # Ton défi, # Maison, # Micro-rituel)
- Sonnet prioritaire, fallback Haiku
- Validation 900-1200 chars, retry 1x si hors limites
- Support 1 aspect max (orb <= 3°)
- Logs: `model_used` = "sonnet" ou "haiku"

---

#### 2. **`apps/api/routes/natal_interpretation.py`** ⚠️ **VERSION 2 + CLEANUP**

**Changements:**
```python
# L20-23: Import PROMPT_VERSION
from services.natal_interpretation_service import (
    generate_with_sonnet_fallback_haiku,
    PROMPT_VERSION
)

# L61: version = PROMPT_VERSION (au lieu de 1)
version = PROMPT_VERSION

# L102-105: Appel Sonnet+fallback
interpretation_text, model_used = await generate_with_sonnet_fallback_haiku(
    subject=request.subject,
    chart_payload=request.chart_payload.model_dump()
)

# L107: Log modèle utilisé
logger.info(f"✅ Interprétation générée avec {model_used} ({len(interpretation_text)} chars)")
```

**Supprimé:**
- Tous les `#region agent log` (L50-86, L95-98, L102-106, L114-130, L142-168, L204-208)
- Code debug temporaire

---

#### 3. **`apps/api/schemas/natal_interpretation.py`** ⚠️ **AJOUT ASPECTS**

**Changement:**
```python
class ChartPayload(BaseModel):
    ...
    aspects: Optional[list] = Field(None, description="Liste des aspects majeurs (max 1 utilisé si orb <= 3°)")
```

---

### Mobile (TypeScript/React Native)

#### 4. **`apps/mobile/utils/natalChartUtils.ts`** ⚠️ **CHART ID STABLE + HOUSE LABELS**

**Changements:**
```typescript
// getChartId: SANS prompt_version, AVEC timezone + house_system
export function getChartId(
  birthDate: string,
  birthTime: string,
  latitude: number,
  longitude: number,
  timezone: string = 'UTC',
  houseSystem: string = 'placidus'
): string {
  const lat = latitude.toFixed(5);
  const lon = longitude.toFixed(5);
  const hs = houseSystem.toLowerCase().trim();
  const data = `${birthDate}|${birthTime}|${lat}|${lon}|${timezone}|${hs}`;
  return CryptoJS.MD5(data).toString();
}

// Nouvelle fonction
export function getHouseLabel(house: number): string {
  const labels: Record<number, string> = {
    1: "identité, apparence",
    2: "ressources, valeurs",
    // ... etc
  };
  return labels[house] || "domaine de vie";
}
```

---

#### 5. **`apps/mobile/components/NatalInterpretationModal.tsx`** ⚠️ **UI V2 + MARKDOWN**

**Changements:**
```tsx
// Import Markdown
import Markdown from 'react-native-markdown-display';
import { getHouseLabel } from '../utils/natalChartUtils';

// Header simplifié
<Text style={styles.title}>
  {emoji} {chartPayload.subject_label}
</Text>
{chartPayload.house && (
  <Text style={styles.houseSubtitle}>
    Maison {chartPayload.house} ({getHouseLabel(chartPayload.house)})
  </Text>
)}

// Contenu Markdown
<Markdown style={markdownStyles}>{interpretation.text}</Markdown>

// Badge version
{interpretation.cached && __DEV__ && (
  <Text style={styles.cachedBadge}>
    ♻️ Depuis le cache (v{interpretation.version})
  </Text>
)}
```

**Styles Markdown:**
- `heading1`: Gold, h2
- `heading2`: Accent, h3
- `paragraph`: Body, text
- `strong`: Gold, 600
- `list_item`: Body, text

---

### Tests

#### 6. **`apps/api/test_natal_interpretation_v2.py`** ⚠️ **NOUVEAU FICHIER**

**Tests:**
1. ✅ Prompt builder v2 (format, sections, aspect)
2. ✅ Validation longueur (900-1400)
3. ✅ House labels
4. ✅ Génération Sonnet + fallback Haiku
5. ✅ Cache DB version 2

---

## 🚀 Commandes de Test

### Backend

```bash
cd apps/api

# Tests v2
python3 test_natal_interpretation_v2.py

# Lancer l'API
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Mobile

```bash
cd apps/mobile

# Installer dépendance Markdown
npm install react-native-markdown-display

# Lancer Expo
npx expo start -c
```

### Tests Manuels

1. **Génération initiale (Sonnet)**
   - Ouvrir app → Thème Natal
   - Cliquer sur ☀️ Soleil
   - Attendre 2-5s (Sonnet)
   - Vérifier format markdown + longueur 900-1200

2. **Cache hit**
   - Re-cliquer sur Soleil
   - Instant (< 500ms)
   - Badge "♻️ Depuis le cache (v2)" visible en dev

3. **Régénération**
   - Cliquer "🔄 Régénérer"
   - Nouvelle génération (Sonnet)
   - Texte peut varier (temperature=0.7)

4. **Fallback Haiku**
   - Simuler échec Sonnet (déconnecter réseau temporairement)
   - Vérifier fallback Haiku dans logs

5. **DB Vérification**
   ```sql
   SELECT id, subject, version, LENGTH(output_text), created_at
   FROM natal_interpretations
   WHERE version = 2
   ORDER BY created_at DESC
   LIMIT 10;
   ```

---

## 🔄 Migration v1 → v2

### Stratégie (Lazy Migration)

✅ **Conserver** les anciennes entrées `version=1`
✅ **Utiliser** `version=2` pour toutes nouvelles générations
✅ **Régénérer** v2 si user clique "Régénérer" sur ancienne interprétation
✅ **Pas de migration bulk** (évite coûts API massifs)

### Requête SQL (Info)

```sql
-- Compter v1 vs v2
SELECT version, COUNT(*) as count
FROM natal_interpretations
GROUP BY version;

-- Total coût potentiel migration v1→v2
SELECT COUNT(*) * 0.015 as estimated_cost_usd
FROM natal_interpretations
WHERE version = 1;
```

**Note:** Sonnet coûte ~$0.015 par interprétation (vs $0.001 Haiku). Ne pas forcer migration bulk.

---

## 📊 Coûts API (Sonnet vs Haiku)

### Sonnet 3.5
- **Input:** ~600 tokens → $0.003
- **Output:** ~400 tokens → $0.012
- **Total:** ~$0.015 par interprétation

### Haiku (Fallback)
- **Input:** ~600 tokens → $0.0002
- **Output:** ~400 tokens → $0.0008
- **Total:** ~$0.001 par interprétation

### Avec Cache
- 1ère génération: $0.015 (Sonnet)
- Clics suivants: $0.00 (cache DB)

**Exemple:** 100 users × 10 placements = 1000 interprétations = **~$15** (puis $0 pour re-clics)

---

## 🐛 Troubleshooting

### ❌ Erreur: "model: claude-3-5-sonnet-20241022 not found"

**Cause:** Compte Anthropic n'a pas accès à Sonnet 3.5
**Solution:** Fallback Haiku s'active automatiquement

### ❌ Erreur: "react-native-markdown-display not found"

**Solution:**
```bash
cd apps/mobile
npm install react-native-markdown-display
```

### ❌ Interprétation trop longue/courte

**Normal:** Le système retry 1x automatiquement
**Si persiste:** Vérifier logs backend (⚠️ Tronquage à 1400)

### ❌ Chart ID différent entre générations

**Vérifier:**
1. Timezone identique ?
2. House system identique ?
3. Lat/lon arrondi 5 décimales ?

---

## ✨ Améliorations Futures (v3)

- [ ] Support multi-langues (EN, ES)
- [ ] Aspects multiples (max 2-3)
- [ ] Streaming Claude (afficher au fur et à mesure)
- [ ] A/B testing prompts (version 2a vs 2b)
- [ ] Analytics (% Sonnet vs Haiku, latence moyenne)
- [ ] Export PDF thème complet

---

## 📝 Résumé des Diffs

```diff
natal_interpretation_service.py
+ PROMPT_VERSION = 2
+ build_interpretation_prompt_v2()
+ get_house_label_v2()
+ find_relevant_aspect()
+ validate_interpretation_length()
+ generate_with_sonnet_fallback_haiku()
- build_interpretation_prompt() [v1]
- generate_interpretation_with_claude() [v1]

natal_interpretation.py (route)
+ version = PROMPT_VERSION
+ generate_with_sonnet_fallback_haiku()
+ model_used log
- #region agent log (tous)

natal_interpretation.py (schema)
+ aspects: Optional[list]

natalChartUtils.ts
+ timezone, houseSystem params
+ getHouseLabel()
- promptVersion param (retiré)

NatalInterpretationModal.tsx
+ import Markdown
+ import getHouseLabel
+ Header simplifié (emoji + nom)
+ Sous-titre Maison
+ Markdown rendering
+ markdownStyles
```

---

## ✅ Checklist Déploiement

- [x] Backend service v2 implémenté
- [x] Route v2 + cleanup logs
- [x] Schémas updated (aspects)
- [x] Mobile utils (chart ID stable + house labels)
- [x] Modal UI v2 (markdown + header simple)
- [x] Tests unitaires v2 créés
- [ ] Installer react-native-markdown-display
- [ ] Exécuter tests v2
- [ ] Lancer API + mobile
- [ ] Tests manuels (Sonnet, cache, fallback)
- [ ] Vérifier DB (version=2)

---

**🎉 Implémentation v2 complète ! Prêt pour tests.**
