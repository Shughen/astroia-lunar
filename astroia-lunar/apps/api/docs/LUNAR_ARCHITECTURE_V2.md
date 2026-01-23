# Architecture Révolutions Lunaires V2

## 🎯 Vision

Séparation claire entre **faits astronomiques** (immutables) et **narration IA temporelle** (régénérable).

## ❌ Problème de l'architecture V1

La table `pregenerated_lunar_interpretations` traite les révolutions lunaires comme des **configurations statiques réutilisables**, alors qu'elles sont des **événements astronomiques datés et contextuels**.

### Défauts critiques V1

| Problème | Impact |
|----------|--------|
| Pas de temporalité | Impossible de distinguer janvier 2025 de janvier 2026 |
| Pas de contexte astral | Ignore aspects, transits, rétrogradations du mois |
| Confusion faits/narration | Mélange positions (moon_sign) et texte IA |
| Pas user-specific | Interprétations génériques, pas personnalisées |
| Scalabilité compromise | 1728 combinaisons ne couvrent pas les mois futurs |

## ✅ Architecture V2 : 4 Couches

```
┌────────────────────────────────────────────────────────────┐
│ LAYER 1: FAITS ASTRONOMIQUES (Kerykeion/RapidAPI)         │
├────────────────────────────────────────────────────────────┤
│ LunarReturn (existant)                                     │
│ - user_id FK                                               │
│ - return_date (datetime UTC - exact moment révolution)    │
│ - moon_sign, moon_house, lunar_ascendant                   │
│ - aspects, planets, houses (JSONB)                         │
│ - raw_data (RapidAPI response)                             │
│ → Source de vérité immutable                               │
└────────────────────────────────────────────────────────────┘
                         ↓ FK lunar_return_id
┌────────────────────────────────────────────────────────────┐
│ LAYER 2: NARRATION IA TEMPORELLE (Claude Opus 4.5)        │
├────────────────────────────────────────────────────────────┤
│ LunarInterpretation (NOUVEAU)                              │
│ - user_id FK                                               │
│ - lunar_return_id FK (CLEF - lien temporel)                │
│ - subject ('full' | 'climate' | 'focus' | 'approach')      │
│ - version, lang                                            │
│ - input_json (contexte Claude), output_text (narration)    │
│ - weekly_advice (JSONB)                                    │
│ - model_used, created_at                                   │
│ → UNIQUE(lunar_return_id, subject, lang, version)          │
└────────────────────────────────────────────────────────────┘
                         ↓ Agrégation + Format
┌────────────────────────────────────────────────────────────┐
│ LAYER 3: CACHE APPLICATION (FastAPI)                      │
├────────────────────────────────────────────────────────────┤
│ LunarReport (existant)                                     │
│ - report JSON (formaté pour affichage)                     │
│ → Cache purgeable, TTL court                               │
└────────────────────────────────────────────────────────────┘
                         ↓ Fallback si Layer 2 échoue
┌────────────────────────────────────────────────────────────┐
│ LAYER 4: FALLBACK TEMPLATES (Static)                      │
├────────────────────────────────────────────────────────────┤
│ LunarInterpretationTemplate (NOUVEAU)                      │
│ - template_type, moon_sign, moon_house, lunar_ascendant    │
│ - template_text, weekly_advice_template                    │
│ → Templates génériques réutilisables (1728 migrés)         │
└────────────────────────────────────────────────────────────┘
```

## 📊 Modèles SQLAlchemy

### LunarInterpretation (narration temporelle)

```python
class LunarInterpretation(Base):
    __tablename__ = "lunar_interpretations"

    id = Column(UUID, primary_key=True)
    user_id = Column(Integer, FK("users.id"))
    lunar_return_id = Column(Integer, FK("lunar_returns.id"))  # CLEF

    subject = Column(String(50))  # 'full' | 'climate' | 'focus' | 'approach'
    version = Column(Integer, default=2)
    lang = Column(String(10), default='fr')

    input_json = Column(JSONB)   # Contexte complet (traçabilité)
    output_text = Column(Text)   # Interprétation générée
    weekly_advice = Column(JSONB)

    model_used = Column(String(50))  # 'claude-opus-4-5', etc.
    created_at = Column(DateTime(timezone=True))

    # Idempotence
    __table_args__ = (
        Index('unique', 'lunar_return_id', 'subject', 'lang', 'version', unique=True),
    )
```

### LunarInterpretationTemplate (fallback statique)

```python
class LunarInterpretationTemplate(Base):
    __tablename__ = "lunar_interpretation_templates"

    id = Column(UUID, primary_key=True)

    template_type = Column(String(50))  # 'full' | 'climate' | 'focus' | 'approach'
    moon_sign = Column(String(50), nullable=True)
    moon_house = Column(Integer, nullable=True)
    lunar_ascendant = Column(String(50), nullable=True)

    version = Column(Integer, default=2)
    lang = Column(String(10), default='fr')

    template_text = Column(Text)
    weekly_advice_template = Column(JSONB)

    model_used = Column(String(50))
    created_at = Column(DateTime(timezone=True))

    # Idempotence
    __table_args__ = (
        Index('unique', 'template_type', 'moon_sign', 'moon_house',
              'lunar_ascendant', 'version', 'lang', unique=True),
    )
```

## 🔄 Service de Génération

### lunar_interpretation_generator.py

```python
async def generate_or_get_interpretation(
    db: AsyncSession,
    lunar_return_id: int,
    user_id: int,
    subject: str = 'full',
    version: int = 2,
    lang: str = 'fr',
    force_regenerate: bool = False
) -> Tuple[str, Optional[Dict], str, str]:
    """
    Hiérarchie de génération:
    1. LunarInterpretation (DB temporelle) - PRIORITÉ
    2. Génération Claude Opus 4.5 - FALLBACK 1
    3. LunarInterpretationTemplate (DB templates) - FALLBACK 2
    4. Templates hardcodés (CLIMATE_TEMPLATES) - FALLBACK 3

    Returns:
        (output_text, weekly_advice, source, model_used)
    """
```

## 🚀 Avantages V2

| Bénéfice | Détail |
|----------|--------|
| **Architecture saine** | Séparation claire faits vs narration |
| **Temporalité correcte** | Interprétations liées à événements datés |
| **Versionning complet** | A/B testing, rollback, analyse qualité |
| **Traçabilité totale** | input_json stocké pour chaque génération |
| **Scalabilité** | Génération mois futurs (2026-2030+) |
| **Idempotence** | UNIQUE constraint évite duplications |
| **Observabilité** | Logs, métriques, flags response |
| **Réutilisation** | 1728 templates comme fallback |

## 📦 Migration Données

### Étape 1 : Création tables

```sql
-- Migration Alembic 5a1b2c3d4e5f
CREATE TABLE lunar_interpretation_templates (...);

-- Migration Alembic 6b2c3d4e5f6a
CREATE TABLE lunar_interpretations (...);
```

### Étape 2 : Migration données

```sql
-- Migrer 1728 interprétations existantes
INSERT INTO lunar_interpretation_templates (
    template_type, moon_sign, moon_house, lunar_ascendant,
    version, lang, template_text, weekly_advice_template, ...
)
SELECT
    'full' AS template_type,
    moon_sign, moon_house, lunar_ascendant,
    version, lang,
    interpretation_full AS template_text,
    weekly_advice AS weekly_advice_template,
    ...
FROM pregenerated_lunar_interpretations;

-- Renommer ancienne table (backup)
ALTER TABLE pregenerated_lunar_interpretations
    RENAME TO pregenerated_lunar_interpretations_backup;
```

## 🔍 Observabilité

### Flags de réponse

```json
{
  "interpretation": "...",
  "weekly_advice": {...},
  "metadata": {
    "source": "db_temporal" | "claude" | "db_template" | "hardcoded",
    "model_used": "claude-opus-4-5-20251101",
    "version": 2,
    "created_at": "2026-01-23T10:00:00Z",
    "cached": true
  }
}
```

### Logs structurés

```python
logger.info(
    "[LunarInterpretationGenerator] Génération réussie",
    extra={
        'lunar_return_id': 123,
        'user_id': 456,
        'subject': 'full',
        'source': 'claude',
        'model': 'opus-4-5',
        'duration_ms': 1234
    }
)
```

## 📈 Métriques (à implémenter)

```python
# Prometheus counters
lunar_interpretation_generated_total
lunar_interpretation_cache_hit_total
lunar_interpretation_fallback_total

# Histogram
lunar_interpretation_generation_duration_seconds
```

## 🧪 Tests

### Test idempotence

```python
async def test_generate_idempotent():
    # Générer 2 fois
    result1 = await generate_or_get_interpretation(db, lr_id, user_id)
    result2 = await generate_or_get_interpretation(db, lr_id, user_id)

    # Doit retourner la même interprétation (cache)
    assert result1[0] == result2[0]
    assert result1[2] == 'claude'  # Première fois
    assert result2[2] == 'db_temporal'  # Cache hit
```

### Test fallback hiérarchique

```python
async def test_fallback_hierarchy():
    # 1. Sans DB ni Claude → hardcoded
    result = await generate_or_get_interpretation(
        db=None, lunar_return_id=123, user_id=456
    )
    assert result[2] == 'hardcoded'

    # 2. Avec DB mais Claude échoue → db_template
    with mock.patch('services.lunar_interpretation_generator._generate_via_claude', side_effect=APIError):
        result = await generate_or_get_interpretation(
            db=db, lunar_return_id=123, user_id=456
        )
        assert result[2] == 'db_template'

    # 3. Claude réussit → claude
    result = await generate_or_get_interpretation(
        db=db, lunar_return_id=123, user_id=456
    )
    assert result[2] == 'claude'
```

## 📚 Références

- `models/lunar_interpretation.py`
- `models/lunar_interpretation_template.py`
- `services/lunar_interpretation_generator.py`
- `alembic/versions/5a1b2c3d4e5f_create_lunar_interpretation_templates.py`
- `alembic/versions/6b2c3d4e5f6a_create_lunar_interpretations.py`

---

**Version** : 2.0
**Date** : 2026-01-23
**Auteur** : Claude Code (Sonnet 4.5)
