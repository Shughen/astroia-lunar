# Refonte Aspects v5 — Documentation Technique

**Date** : 2026-01-30
**Sprint** : 8
**Statut** : Backend & Mobile ready, génération en attente
**Scope** : 130 aspects prioritaires (90%+ couverture cas réels)
**Budget** : $10-15 USD

---

## 🎯 Objectif

Remplacer les interprétations d'aspects v4 (ton technique, textes identiques) par des interprétations v5 (ton bienveillant, exemples concrets) générées avec Claude Opus 4.5.

### Problèmes v4 identifiés

1. **Textes identiques** : 3 conjonctions affichent "Symbiose puissante, intensité garantie"
2. **Langage technique** : "fusion fonctionnelle", "indissociation"
3. **Conseils non actionnables** : "Observer les contextes où..."
4. **Structure froide** : Wikipédia-style, pas émotionnel
5. **Pas de section "Attention"** : Aucun warning sur les pièges

**Note Claude Opus 4.5** : 8/20 pour la qualité actuelle

---

## 📋 Architecture Technique

### Format Markdown v5

```markdown
# ☌ Conjonction Soleil - Vénus

**En une phrase :** [Accroche émotionnelle 50-80 chars]

## L'énergie de cet aspect

[2-3 phrases expliquant l'interaction planétaire en langage simple]

## Manifestations concrètes

- [Manifestation 1 : vie quotidienne]
- [Manifestation 2 : relations]
- [Manifestation 3 : travail/créativité]

## Conseil pratique

[Action concrète 100-200 chars]

## Attention

[Piège à éviter 80-150 chars]
```

### Changements Backend

**Fichier** : `services/aspect_explanation_service.py`

1. **Parser markdown** : Nouvelle extraction section "Attention" → `shadow`
```python
def parse_markdown_to_copy(markdown_content: str) -> Dict[str, Any]:
    # ... code existant ...

    # Nouvelle section v5
    match = re.search(r"##\s*Attention\s*\n(.+?)(?:\n##|$)", markdown_content, re.DOTALL)
    if match:
        copy['shadow'] = match.group(1).strip()

    return {
        'summary': summary,
        'why': why_bullets,
        'manifestation': manifestation,
        'advice': advice,
        'shadow': shadow  # 🆕 Nouveau champ v5
    }
```

2. **Versioning** : Paramètre `version=5` par défaut
```python
async def enrich_aspects_v4_async(
    aspects: List[Dict[str, Any]],
    planets_data: Dict[str, Any],
    db_session,
    limit: int = 10,
    version: int = 5  # 🆕 Version par défaut
) -> List[Dict[str, Any]]:
```

**Fichier** : `routes/natal.py`

3. **Query parameter** : Sélection version à la demande
```python
@router.post("/natal-chart")
async def calculate_natal_chart(
    data: NatalChartRequest,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
    aspect_version: int = Query(5, ge=2, le=5)  # 🆕 Query param
):
    # Priorité : query param > settings
    version_to_use = aspect_version if aspect_version >= 2 else settings.ASPECTS_VERSION
    aspects = await enrich_aspects_v4_async(raw_aspects, planets, db, limit=10, version=version_to_use)
```

### Changements Mobile

**Fichier** : `types/api.ts`

```typescript
export interface AspectV4 {
  // ... champs existants ...
  copy?: {
    summary: string;
    why: string[];
    manifestation: string;
    advice?: string;
    shadow?: string;  // 🆕 v5 : section "Attention"
  };
}
```

**Fichier** : `components/AspectDetailSheet.tsx`

```tsx
{/* Nouvelle section v5 */}
{aspect.copy.shadow && (
  <View style={[styles.section, styles.shadowSection]}>
    <Text style={styles.sectionTitle}>⚠️ Attention</Text>
    <Text style={styles.shadowText}>{translateAstrologyText(aspect.copy.shadow)}</Text>
  </View>
)}
```

**Styles** :
```typescript
shadowSection: {
  backgroundColor: 'rgba(251, 191, 36, 0.15)', // Amber warning
  borderLeftWidth: 3,
  borderLeftColor: '#f59e0b',
  paddingLeft: 12,
},
shadowText: {
  fontSize: 15,
  lineHeight: 24,
  color: '#fbbf24',
  fontStyle: 'italic',
},
```

---

## 🛠️ Scripts de Génération

### 1. generate_aspect_batch.py

**Responsabilités** :
- Génération avec Claude Opus 4.5 (`claude-opus-4-5-20251101`)
- A/B testing : 2 prompts (Insight vs Storytelling)
- Rate limiting : 2s entre appels
- Tracking coûts API

**Usage** :
```bash
python scripts/generate_aspect_batch.py \
  --batch-number 1 \
  --pairs "sun,venus" "sun,mars" \
  --ab-test \
  --output data/batches/batch_01.json
```

**Prompts A/B** :
- **Version A** : Insight + compréhension (pourquoi ça marche)
- **Version B** : Action + storytelling (comment ça se vit)

**Output** : JSON avec versions A et B, tokens, coût USD

### 2. validate_aspect_batch.py

**Responsabilités** :
- Validation format markdown
- Contraintes longueurs (summary 50-80, manifestation 350-650, etc.)
- Blacklist jargon : "symbiose", "indissociation", "contextualiser", "observer"
- Vérification section "Attention" présente

**Usage** :
```bash
python scripts/validate_aspect_batch.py \
  --input data/batches/batch_01.json \
  --strict
```

### 3. insert_aspect_batch.py

**Responsabilités** :
- Insertion dans `pregenerated_natal_aspects` (version=5)
- Upsert pattern (permet reprendre batch)
- Mise à jour `data/progress.json`
- Transaction atomique par batch

**Usage** :
```bash
python scripts/insert_aspect_batch.py \
  --batch-file data/batches/batch_01.json \
  --version 5
```

---

## 📊 Plan de Génération

### Scope Optimisé : 130 aspects (10 batches)

**Batches prioritaires avec A/B test** (1-3) : 35 aspects
- Batch 1 : sun-venus, sun-mars (10 aspects, $0.80)
- Batch 2 : venus-mars, sun-jupiter (10 aspects, $0.80)
- Batch 3 : moon-uranus, saturn-uranus, sun-moon (15 aspects, $1.20)

**Batches fréquents version A uniquement** (4-10) : 95 aspects
- Batch 4-5 : Aspects solaires restants (30 aspects, $2.40)
- Batch 6-8 : Aspects lunaires (35 aspects, $2.80)
- Batch 9-10 : Venus/Mars avec planètes extérieures (30 aspects, $2.40)

**Total** : 130 aspects, $10.40 USD estimé

### Workflow par Batch

```bash
# 1. Générer
python scripts/generate_aspect_batch.py --batch-number 1 --pairs "sun,venus" "sun,mars" --ab-test

# 2. Valider
python scripts/validate_aspect_batch.py --input data/batches/batch_01.json --strict

# 3. Sélection A/B manuelle (éditer JSON)

# 4. Insérer en BD
python scripts/insert_aspect_batch.py --batch-file data/batches/batch_01.json

# 5. Vérifier
psql $DATABASE_URL -c "SELECT COUNT(*) FROM pregenerated_natal_aspects WHERE version=5;"

# 6. Commit
git add data/batches/batch_01.json
git commit -m "feat(api): add aspect interpretations batch 1/10 - sun combos P0"
git push origin main
```

---

## ✅ Tests

### Tests Unitaires

**Fichier** : `tests/test_aspect_explanation_v5.py` (6 tests)

```bash
cd apps/api
pytest tests/test_aspect_explanation_v5.py -v
```

**Coverage** :
- ✅ `test_parse_markdown_v5_with_shadow` : Parse format v5 complet
- ✅ `test_parse_markdown_v4_backward_compat` : Compatibilité v4
- ✅ `test_parse_markdown_v5_lengths` : Contraintes longueurs
- ✅ `test_enrich_aspects_v5_with_version_param` : Paramètre version accepté
- ✅ `test_markdown_v5_without_shadow_is_valid` : Shadow optionnel
- ✅ `test_markdown_empty_sections` : Robustesse sections manquantes

**Résultat** : 6/6 passés ✨

### Tests E2E

```bash
# Test avec version 5
curl -X POST "http://localhost:8000/api/natal-chart?aspect_version=5" \
  -H "Authorization: Bearer $TOKEN" \
  -d @test_natal_data.json

# Vérifier response
# aspects[0].copy.summary ≠ "Symbiose puissante, intensité garantie"
# aspects[0].copy.shadow présent
```

---

## 📁 Fichiers Modifiés

### Backend (5 fichiers)
- ✅ `services/aspect_explanation_service.py` : Parser v5 + version param
- ✅ `routes/natal.py` : Query param `aspect_version`
- ✅ `scripts/generate_aspect_batch.py` : Génération Claude Opus 4.5
- ✅ `scripts/validate_aspect_batch.py` : Validation qualité
- ✅ `scripts/insert_aspect_batch.py` : Insertion BD avec tracking
- ✅ `tests/test_aspect_explanation_v5.py` : Tests unitaires

### Mobile (2 fichiers)
- ✅ `types/api.ts` : Interface `shadow?: string`
- ✅ `components/AspectDetailSheet.tsx` : Section "⚠️ Attention"

### Infrastructure
- ✅ `data/batches/` : Dossier batches JSON
- ✅ `data/validation_reports/` : Rapports validation
- ✅ `data/progress.json` : Tracking progression (0/130)

---

## 🔄 Rétrocompatibilité

### Fallback v4 → v5

```python
# Si aspect v5 absent en BD → fallback v4
interpretation = await load_pregenerated_aspect_interpretation(
    db_session, planet1, planet2, aspect_type, version=5
)

if not interpretation:
    # Fallback v4 automatique
    interpretation = await load_pregenerated_aspect_interpretation(
        db_session, planet1, planet2, aspect_type, version=2
    )
```

### Rollback v5 → v4

Si problème critique avec v5 :

```python
# routes/natal.py
aspect_version: int = Query(4, ge=2, le=5)  # ← Change default to 4
```

Impact : Utilisateurs récupèrent v4 immédiatement

---

## 📈 Exemple Avant/Après

### V4 (actuel)

```markdown
**En une phrase :** Symbiose puissante, intensité garantie

## Pourquoi ?
- Fusion fonctionnelle
- Indissociation entre identité et valeurs

## Manifestations
Cette conjonction crée une symbiose...

## Conseil
Observer les contextes où cette conjonction s'exprime.
```

**Problèmes** : Jargon, conseil vague, pas de section Attention

### V5 (cible)

```markdown
**En une phrase :** Ton charme magnétique et ta créativité fusionnent naturellement

## L'énergie de cet aspect
Ton identité profonde (Soleil) et tes valeurs relationnelles (Vénus) ne font qu'un.
Les autres te perçoivent comme authentique et attirant.

## Manifestations concrètes
- **Relations harmonieuses** : Les conversations coulent naturellement
- **Créativité débridée** : Envie de créer du beau qui te ressemble
- **Magnétisme social** : Tu attires l'attention sans forcer

## Conseil pratique
Profite de cette énergie pour lancer ce projet créatif qui te trotte dans la tête.

## Attention
Attention à ne pas confondre ce que tu veux avec ce que tu aimes — ils sont
indissociables ce mois-ci.
```

**Améliorations** : Langage accessible, exemples concrets, conseil actionnable, warning piège

---

## 🚀 Prochaines Étapes

1. **Génération Batch 1** : sun-venus, sun-mars avec A/B test
2. **Génération Batch 2** : venus-mars, sun-jupiter avec A/B test
3. **Génération Batch 3** : moon-uranus, saturn-uranus, sun-moon avec A/B test
4. **Génération Batches 4-10** : 95 aspects version A uniquement
5. **Tests E2E production** : Validation avec vrais thèmes nataux

**Durée estimée** : 8h génération + 2h validation + 1h insertion = **11h total**

---

## 📚 Références

- Plan complet : `.claude/plans/tidy-bubbling-pearl.md`
- Tests : `apps/api/tests/test_aspect_explanation_v5.py`
- Scripts : `apps/api/scripts/generate_aspect_batch.py` (et validation/insertion)
- Documentation mobile : `apps/mobile/docs/SCREENS.md`

**Dernière màj** : 2026-01-30 | **Auteur** : Claude Sonnet 4.5
