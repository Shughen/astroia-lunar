# Natal Interpretation v4 - Senior Professional Structured Style

## Overview

Version 4 is the production-ready senior astrologer style that replaces v3 (experimental). It implements a structured template based on the professional astrology framework: **Fonction → Signe → Maison → Manifestations → Vigilance**.

## Philosophy

v4 follows a pedagogical approach:
1. **Function First**: Explain what the planet/point does (archetype) before discussing its expression
2. **Coloration**: How the sign modulates this function
3. **Domain**: Where it manifests concretely (house)
4. **Observable Manifestations**: Concrete behavioral patterns (max 3 examples)
5. **Vigilance**: Short, factual pitfall warning (non-mystical)

## Version Comparison

| Feature | v2 (Default) | v3 (Deprecated) | v4 (Senior Pro) |
|---------|--------------|-----------------|-----------------|
| **Status** | ✅ Production | ⚠️ Deprecated | ✅ Production |
| **Style** | Modern, warm, introspective | Senior experimental | Senior professional structured |
| **Micro-rituel** | ✅ Included | ❌ Removed | ❌ Removed |
| **Structure** | Ton moteur / Ton défi | Ton moteur / Ton défi (legacy) | Fonction → Signe → Maison → Manifestations → Vigilance |
| **Aspects filter** | All aspects, orb ≤3° | Major aspects only, orb ≤6° | Major aspects only, orb ≤6° (reuses v3 filter) |
| **Length** | 900-1400 chars | 700-1200 chars | 800-1300 chars (target: 900-1100) |
| **Planet functions** | Implicit | Implicit | **Explicit mapping** (PLANET_FUNCTIONS_V4) |
| **North Node** | Standalone | Standalone | **Treated as NN/NS axis** with opposite context |
| **Lilith** | ✅ Supported | ❌ Rejected (400 error) | ❌ Rejected (400 error) |
| **Tone** | Accessible, warm | Professional | Professional analytical, non-coaching |

## Implementation Details

### Files Modified

1. **`services/natal_interpretation_service.py`** (lines 496-703)
   - Added `PLANET_FUNCTIONS_V4` dictionary - 15 planet/point archetype mappings
   - Added `get_opposite_sign_v4()` - helper for NN/NS axis calculation
   - Added `build_interpretation_prompt_v4_senior()` - v4 prompt template with special NN/NS handling
   - Updated `validate_interpretation_length()` - supports v4 range (800-1300 chars)
   - Updated `generate_with_sonnet_fallback_haiku()` - calls v4 prompt builder when version=4
   - Updated retry logic thresholds for v4 (800-1300 chars, target 900-1100)

2. **`config.py`** (line 71)
   - Updated `NATAL_INTERPRETATION_VERSION` description to include v4
   - Default remains v2 for backward compatibility

3. **`routes/natal_interpretation.py`** (lines 55-61)
   - Lilith validation already in place (rejects Lilith for version ≥3)

### Version Switch

Switch between versions using environment variable:

```bash
# Use v2 (default - modern style with micro-rituel)
NATAL_INTERPRETATION_VERSION=2

# Use v3 (deprecated - experimental senior)
NATAL_INTERPRETATION_VERSION=3

# Use v4 (production - senior professional structured)
NATAL_INTERPRETATION_VERSION=4
```

### Planet Function Mappings (v4)

```python
PLANET_FUNCTIONS_V4 = {
    'sun': 'identité centrale, énergie vitale, volonté',
    'moon': 'besoins émotionnels, sécurité, réactions instinctives',
    'mercury': 'intellect, communication, analyse',
    'venus': 'valeurs, relations, capacité à recevoir',
    'mars': 'action, désir, affirmation',
    'jupiter': 'expansion, sens, optimisme',
    'saturn': 'structure, limites, responsabilité',
    'uranus': 'innovation, liberté, rupture',
    'neptune': 'dissolution, inspiration, transcendance',
    'pluto': 'transformation, pouvoir, régénération',
    'ascendant': 'masque social, façon d\'entrer en contact',
    'midheaven': 'vocation, image publique, accomplissement',
    'north_node': 'chemin de vie, territoire à conquérir',
    'south_node': 'acquis passés, zone de confort',
    'chiron': 'blessure originelle, don de guérison'
}
```

### North Node as Axis (v4 Special Feature)

Unlike v2/v3, v4 treats the North Node and South Node as an **evolutionary axis**, not standalone points.

**When subject = `north_node`:**
- Prompt includes South Node context (opposite sign, opposite house)
- Template has 6 sections: Axe NN/NS → Fonction NN → Coloration → Domaine → Manifestations → Vigilance
- Emphasizes NN = "chemin de vie à développer", NS = "acquis à transcender"

**When subject = `south_node`:**
- Prompt includes North Node context (opposite sign, opposite house)
- Template has 6 sections: Axe NN/NS → Fonction NS → Coloration → Domaine → Manifestations → Vigilance
- Emphasizes NS = "confort familier", NN = "territoire à conquérir"

**Example context injected:**
```
⚠️ AXE D'ÉVOLUTION: Nœud Nord en Verseau (Maison 11) = chemin de vie.
Nœud Sud en Lion (Maison 5) = acquis à transcender.
Traiter l'axe comme dynamique évolutive.
```

### Major Aspects Filter (v4)

v4 reuses `find_relevant_aspect_v3()` - accepts **only** these aspects:
- Conjunction (conjonction)
- Opposition (opposition)
- Square (carré)
- Trine (trigone)

**Excluded:**
- Sextile
- Quincunx
- Semi-sextile
- Minor aspects

**Orb threshold:** ≤6° (stricter than v2's 3°, allows more aspects than v2)

### Guard Rails (v4)

1. **No empty output**: If no major aspect ≤6° available, v4 focuses on Fonction + Signe + Maison
2. **Max 3 behavioral examples**: Concrete, incarnated situations (not vague "tu es quelqu'un de...")
3. **Vigilance: short & factual**: 1-2 phrases, non-mystical, concrete pitfall example
4. **Professional analytical tone**: No coaching, no spiritualization, no health advice
5. **Markdown strict format**: ## headers mandatory
6. **Length validation**: 800-1300 chars (target 900-1100), truncated if needed

## Template Structure

### v4 Template for Standard Planets/Points

```markdown
# 🌙 Lune en Bélier

## 1. Fonction planétaire
[2 phrases : besoins émotionnels, sécurité, réactions instinctives. Expliciter cette fonction archétypale de Lune avant de parler du signe. Qu'est-ce que Lune fait dans un thème ?]

## 2. Coloration par Bélier
[2 phrases : comment Bélier module la fonction de Lune. Exemples comportementaux concrets. Pas de "tu es..."]

## 3. Domaine de vie (Maison 5)
[2 phrases : où Lune en Bélier s'exprime concrètement. Maison 5 = créativité/enfants. Situations réelles. Intégrer aspect comme tension ou soutien si présent.]

## 4. Manifestations observables
[2-3 phrases : patterns comportementaux concrets. Exemples de situations vécues (max 3 exemples). Croiser systématiquement Fonction + Signe + Maison + Aspect.]

## 5. Vigilance
[1-2 phrases : piège typique de Lune en Bélier en Maison 5. Factuel, non mystique. Exemple concret.]
```

### v4 Template for North Node/South Node (Axis)

```markdown
# 🎯 Nœud Nord en Verseau

## 1. L'axe des Nœuds Lunaires
[2 phrases : expliquer que c'est un AXE d'évolution, pas juste un point. Nœud Nord en Verseau = chemin de vie à développer. L'autre pôle (Nœud Sud en Lion) enrichit le sens.]

## 2. Fonction du Nœud Nord
[2 phrases : chemin de vie, territoire à conquérir. Expliciter cette fonction archétypale avant de parler du signe.]

## 3. Coloration Verseau
[2 phrases : comment Verseau module cette fonction. Exemples comportementaux concrets. Pas de "tu es...".]

## 4. Domaine de vie (Maison 11)
[2 phrases : où cet axe se joue concrètement. Maison 11 = amis/communauté. Situations réelles. Intégrer aspect si pertinent.]

## 5. Manifestations observables
[2-3 phrases : patterns comportementaux concrets. Exemples de situations vécues. Dynamique NN/NS : tension entre confort (Lion/Maison 5) et croissance (Verseau/Maison 11).]

## 6. Vigilance
[1-2 phrases : piège typique. Rester bloqué dans le Nœud Sud (zone de confort Lion). Exemple concret.]
```

## Testing v4

### Manual Test (Backend)

1. Set environment variable:
   ```bash
   export NATAL_INTERPRETATION_VERSION=4
   ```

2. Restart API server:
   ```bash
   cd apps/api
   uvicorn main:app --reload
   ```

3. Generate interpretation (example with curl):
   ```bash
   curl -X POST "http://localhost:8000/api/natal-interpretation/generate" \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer YOUR_TOKEN" \
     -d '{
       "subject": "sun",
       "subject_label": "Soleil",
       "sign": "Bélier",
       "house": 1,
       "ascendant_sign": "Bélier",
       "aspects": [
         {"planet1": "sun", "planet2": "mars", "type": "conjunction", "orb": 2.5}
       ]
     }'
   ```

4. Check logs for:
   - `✅ Interprétation finale v4: XXX chars`
   - `📊 Aspects disponibles: v2=X, v3=Y, v4=Y` (v4 uses same filter as v3)

### Unit Tests

v4 reuses v3 tests for aspect filtering and length validation:

```bash
# Run v3 baseline tests (v4 uses same logic)
python -m pytest tests/test_natal_interpretation_v3.py -v

# All 16 tests should pass:
# - 7 aspect filtering tests
# - 5 length validation tests
# - 4 edge case tests
```

**v4-specific validation:**
```python
from services.natal_interpretation_service import validate_interpretation_length

# v4: 800-1300 chars
is_valid, length = validate_interpretation_length("x" * 800, version=4)
assert is_valid is True  # Min boundary

is_valid, length = validate_interpretation_length("x" * 1300, version=4)
assert is_valid is True  # Max boundary

is_valid, length = validate_interpretation_length("x" * 799, version=4)
assert is_valid is False  # Too short

is_valid, length = validate_interpretation_length("x" * 1301, version=4)
assert is_valid is False  # Too long
```

## Backward Compatibility

✅ **v2 is completely untouched** - no regressions
✅ **Default version is v2** - no breaking changes
✅ **Database uses `version` column** - can store v2, v3, and v4 interpretations
✅ **Cache works per version** - separate cache for each version
✅ **v3 deprecated but functional** - still available if needed

## Migration Path

### From v2 to v4 (Recommended)

v2 → v4 is the recommended upgrade path for production users who want:
- Professional analytical tone (less introspective)
- No micro-rituel (focus on interpretation only)
- Explicit planet functions (pedagogical)
- Structured template (predictable format)

**Steps:**
1. Set `NATAL_INTERPRETATION_VERSION=4` in `.env`
2. Restart API server
3. Test with a few sample charts
4. Compare qualitatively with v2 outputs
5. Roll out gradually (cache will prevent duplicates)

### From v3 to v4 (Required)

v3 is deprecated and should be replaced with v4:
- v3 was experimental and had legacy "Ton moteur/défi" structure
- v4 fixes this with proper "Fonction → Signe → Maison" structure
- v4 has same aspect filtering as v3 (major aspects, orb ≤6°)
- v4 has North Node axis handling (v3 didn't)

**Steps:**
1. Set `NATAL_INTERPRETATION_VERSION=4` in `.env`
2. No code changes needed (v3 → v4 is drop-in replacement)
3. Clear v3 cache if desired: `DELETE FROM natal_interpretations WHERE version = 3`

## Troubleshooting

### Issue: v4 outputs are too short (< 800 chars)

**Cause:** Claude may be too concise
**Solution:** Retry logic will automatically request lengthening. If still fails, check target_range in prompt (should be "900-1100")

### Issue: v4 outputs have coaching tone ("tu devrais...")

**Cause:** Prompt constraints not respected
**Solution:** Check prompt template has `INTERDIT: "tu es...", coaching` constraint. May need to adjust temperature or model.

### Issue: North Node interpretation doesn't mention South Node

**Cause:** `is_node` detection failed or opposite context not injected
**Solution:** Check `subject in ['north_node', 'south_node']` condition in `build_interpretation_prompt_v4_senior()`

### Issue: Lilith accepted in v4

**Cause:** Route validation bypassed
**Solution:** Check `routes/natal_interpretation.py` line 55-61 has `if PROMPT_VERSION >= 3` check

## Future Enhancements (Optional)

- [ ] A/B testing framework v2 vs v4 (user preference analytics)
- [ ] JSON output format (structured data instead of markdown)
- [ ] QA validation layer (automatic quality checks before returning)
- [ ] Support for minor aspects in separate v5 (educational mode)
- [ ] Aspect synergy analysis (multiple aspects interaction)

## User Feedback Integration

v4 implementation was based on these requirements:
- ✅ Fix v3 "Ton moteur/défi" legacy structure
- ✅ Explicit planet function mappings (pedagogical)
- ✅ North Node as evolutionary axis (not standalone)
- ✅ Major aspects only, orb ≤6° (reuse v3 filter)
- ✅ Exclude Lilith (route validation)
- ✅ Professional analytical tone (no coaching)
- ✅ Max 3 concrete behavioral examples
- ✅ Short factual vigilance (non-mystical)
- ✅ 800-1300 chars (target 900-1100)
- ✅ Markdown strict format (## headers)
- ✅ Backward compatible (v2 untouched, v3 deprecated)

## Summary

**v4 is the production-ready senior professional style** with:
- Structured pedagogical template (Fonction → Signe → Maison → Manifestations → Vigilance)
- Explicit planet function archetype mappings
- North Node treated as NN/NS evolutionary axis
- Major aspects only (≤6° orb)
- Lilith excluded
- Professional analytical tone (no coaching, no mysticism)
- 800-1300 chars (target 900-1100)
- Backward compatible with v2/v3

**Migration:** v2 → v4 recommended, v3 → v4 required (v3 deprecated)

**Status:** ✅ Ready for production testing (Phase 5 pending)
