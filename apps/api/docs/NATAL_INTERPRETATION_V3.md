# Natal Interpretation v3 - Senior Astrologer Style

## Overview

Version 3 of the natal interpretation prompt implements a "senior astrologer" style with stricter filtering and more professional tone, running in parallel with v2.

## Key Differences: v2 vs v3

| Feature | v2 (Default) | v3 (Senior) |
|---------|--------------|-------------|
| **Style** | Modern, warm, accessible | Professional senior astrologer |
| **Micro-rituel** | ✅ Included | ❌ Removed |
| **Aspects filter** | All aspects, orb ≤3° | Major aspects only (conjunction, opposition, square, trine), orb ≤6° |
| **Length** | 900-1400 chars | 700-1200 chars (shorter, more concise) |
| **Hierarchization** | Equal weight | Sun/Moon/ASC > North Node > others |
| **Behavioral examples** | Encouraged | **Mandatory** (no "tu es quelqu'un de...") |
| **North Node emphasis** | Mentioned | **Highlighted as "life path / zone d'inconfort utile"** |

## Implementation Details

### Files Modified

1. **`services/natal_interpretation_service.py`**
   - Added `find_relevant_aspect_v3()` - filters major aspects with orb ≤6°
   - Added `build_interpretation_prompt_v3_senior()` - v3 prompt template
   - Updated `validate_interpretation_length()` - supports both v2 and v3 ranges
   - Updated `generate_with_sonnet_fallback_haiku()` - version-aware prompt selection
   - Added aspect count logging for v2/v3 comparison

2. **`config.py`**
   - Added `NATAL_INTERPRETATION_VERSION` setting (default=2)

3. **`.env`**
   - Added `NATAL_INTERPRETATION_VERSION=2` with documentation

### Version Switch

Switch between v2 and v3 using environment variable:

```bash
# Use v2 (default - modern style with micro-rituel)
NATAL_INTERPRETATION_VERSION=2

# Use v3 (senior style without micro-rituel)
NATAL_INTERPRETATION_VERSION=3
```

### Major Aspects Filter (v3 only)

v3 accepts **only** these aspects:
- Conjunction (conjonction)
- Opposition (opposition)
- Square (carré)
- Trine (trigone)

**Excluded** (unlike v2):
- Sextile
- Quincunx
- Semi-sextile
- Minor aspects

### Hierarchization (v3)

v3 prioritizes placements:
1. **Pillar**: Sun, Moon, Ascendant (identity foundations)
2. **Life Path**: North Node (emphasized as "zone d'inconfort utile"), South Node
3. **Supporting**: Other planets (Mercury, Venus, Mars, etc.)

### Guard Rails (v3)

1. **No empty output**: If no major aspect ≤6° is available, v3 falls back to key placements interpretation (Sun/Moon/ASC + North Node)
2. **North Node pillar**: Always presented as "chemin de vie / zone d'inconfort utile" when relevant
3. **Behavioral examples mandatory**: No vague "tu es quelqu'un de..." allowed

### Logging & Comparison

The service logs aspect counts for both versions:

```
📊 Aspects disponibles: v2=2 (orb<=3°), v3=5 (majeurs orb<=6°)
```

This allows qualitative comparison between versions.

## Template Structure

### v2 Template (with Micro-rituel)

```markdown
# 🌙 Lune en Bélier
**En une phrase :** ...

## Ton moteur
...

## Ton défi
...

## Maison 5 en Bélier
...

## Micro-rituel du jour (2 min)
- [Action relationnelle]
- [Action corps/respiration]
- [Journal prompt]
```

### v3 Template (without Micro-rituel)

```markdown
# 🌙 Lune en Bélier
**En une phrase :** ...

## Ton moteur
...

## Ton défi
...

## Maison 5 en Bélier
...

(NO Micro-rituel section)
```

## Testing v3

To test v3 locally:

1. Set environment variable:
   ```bash
   export NATAL_INTERPRETATION_VERSION=3
   ```

2. Restart API server:
   ```bash
   uvicorn main:app --reload
   ```

3. Generate interpretation - it will use v3 prompt automatically

4. Check logs for:
   - `✅ Interprétation finale v3: XXX chars`
   - `📊 Aspects disponibles: v2=X, v3=Y`

## Backward Compatibility

✅ **v2 is completely untouched** - no regressions
✅ **Default version is v2** - no breaking changes
✅ **Database uses `version` column** - can store both v2 and v3 interpretations
✅ **Cache works per version** - separate cache for v2 and v3

## Next Steps (Optional Future Enhancements)

- [ ] A/B testing framework to compare user preference
- [ ] JSON output format (mentioned by user, deferred for now)
- [ ] QA step / validation layer (mentioned by user, deferred for now)
- [ ] Analytics dashboard for v2 vs v3 usage metrics

## User Feedback Integration

This implementation was based on user requirements:
- ✅ Keep v2 untouched (backward compatibility)
- ✅ Remove micro-rituel from v3
- ✅ Filter major aspects only with orb ≤6°
- ✅ Hierarchize Sun/Moon/ASC > North Node > others
- ✅ Guard rail: fallback to key placements if no aspects
- ✅ Emphasize North Node as "life path"
- ✅ Keep Markdown format (not JSON initially)
- ✅ Simple switch via environment variable
- ✅ Logging for v2/v3 comparison
