# Scripts de Génération Aspects v5

Ce dossier contient les scripts pour générer les interprétations d'aspects v5 avec Claude Opus 4.5.

---

## 📋 Vue d'ensemble

**Objectif** : Remplacer 130 aspects v4 (ton technique) par v5 (ton bienveillant)

**Workflow** :
```
generate_aspect_batch.py → validate_aspect_batch.py → [sélection A/B manuelle] → insert_aspect_batch.py
```

---

## 🛠️ Scripts Disponibles

### 1. generate_aspect_batch.py

Génère un batch d'interprétations avec Claude Opus 4.5.

**Usage** :
```bash
python scripts/generate_aspect_batch.py \
  --batch-number 1 \
  --pairs "sun,venus" "sun,mars" \
  --ab-test \
  --output data/batches/batch_01.json
```

**Arguments** :
- `--batch-number` : Numéro du batch (1-10)
- `--pairs` : Liste de paires planétaires (ex: `"sun,venus" "sun,mars"`)
- `--ab-test` : Générer 2 versions (A et B) pour A/B testing
- `--output` : Fichier de sortie JSON (optionnel, défaut: `data/batches/batch_XX.json`)

**Output JSON** :
```json
{
  "batch_number": 1,
  "generated_at": "2026-01-30T10:30:00Z",
  "pairs": ["sun-venus", "sun-mars"],
  "aspects": [
    {
      "planet1": "sun",
      "planet2": "venus",
      "aspect_type": "conjunction",
      "version_a": {
        "markdown": "...",
        "parsed": {...},
        "tokens": {"prompt": 850, "completion": 420}
      },
      "version_b": {  // Si --ab-test
        "markdown": "...",
        "parsed": {...},
        "tokens": {"prompt": 850, "completion": 450}
      },
      "selected": null,  // À remplir manuellement
      "selection_reason": null
    }
  ],
  "cost_usd": 0.42,
  "total_tokens": 3200
}
```

**Coût estimé** :
- Avec A/B test : ~$0.08 par aspect (2 générations × $0.04)
- Sans A/B test : ~$0.04 par aspect (1 génération)

**Rate limiting** : 2s entre chaque génération (respecte limites Claude Pro)

---

### 2. validate_aspect_batch.py

Valide un batch généré contre les contraintes de qualité.

**Usage** :
```bash
python scripts/validate_aspect_batch.py \
  --input data/batches/batch_01.json \
  --strict \
  --output data/validation_reports/batch_01.txt
```

**Arguments** :
- `--input` : Fichier batch à valider
- `--strict` : Mode strict (bloque si erreurs)
- `--output` : Rapport de validation (optionnel)

**Critères de validation** :

| Critère | Contrainte |
|---------|-----------|
| **Summary** | 50-80 caractères |
| **Manifestation** | 350-650 caractères |
| **Advice** | 100-200 caractères |
| **Shadow** | 80-150 caractères |
| **Jargon** | Blacklist : "symbiose", "indissociation", "contextualiser", "observer" |
| **Format** | Parsing markdown sans erreur |

**Output** :
```
=== Validation Batch 1 ===
✅ 10/10 aspects validés
⚠️ 1 warning : sun_conjunction_mars summary 85 chars (max 80)
❌ 0 erreurs bloquantes

Détails :
- sun_conjunction_venus : PASS (version A)
- sun_conjunction_mars : WARN (version B, summary long)
- sun_opposition_venus : PASS (version A)
...
```

---

### 3. insert_aspect_batch.py

Insère un batch validé dans la base de données.

**Usage** :
```bash
python scripts/insert_aspect_batch.py \
  --batch-file data/batches/batch_01.json \
  --version 5
```

**Arguments** :
- `--batch-file` : Fichier batch à insérer
- `--version` : Version des aspects (5 par défaut)

**Prérequis** :
- ✅ Batch validé avec `validate_aspect_batch.py`
- ✅ Sélection A/B faite dans le JSON (champ `selected: "a"` ou `"b"`)
- ✅ `$DATABASE_URL` définie (connexion Supabase)

**Output** :
```
=== Insertion Batch 1 ===
✅ 10 aspects insérés (version=5, lang=fr)
   - sun_conjunction_venus (version A)
   - sun_conjunction_mars (version B)
   - sun_opposition_venus (version A)
   ...
⏱️ Durée : 1.2s
💰 Coût cumulé : $0.42 USD
📊 Total v5 en BD : 10/130 (7.7%)

✅ Progress.json mis à jour
```

**Upsert** : Si un aspect existe déjà (même planet1/planet2/aspect_type/version/lang), il est mis à jour.

---

## 📊 Plan de Génération

### Batches Prioritaires (1-3) : 35 aspects avec A/B test

**Batch 1** : sun-venus, sun-mars
```bash
python scripts/generate_aspect_batch.py --batch-number 1 --pairs "sun,venus" "sun,mars" --ab-test
```
- 10 aspects (5 types × 2 paires)
- Coût : ~$0.80 USD
- Durée : 30min génération + 15min sélection A/B

**Batch 2** : venus-mars, sun-jupiter
```bash
python scripts/generate_aspect_batch.py --batch-number 2 --pairs "venus,mars" "sun,jupiter" --ab-test
```
- 10 aspects
- Coût : ~$0.80 USD

**Batch 3** : moon-uranus, saturn-uranus, sun-moon
```bash
python scripts/generate_aspect_batch.py --batch-number 3 --pairs "moon,uranus" "saturn,uranus" "sun,moon" --ab-test
```
- 15 aspects (5 types × 3 paires)
- Coût : ~$1.20 USD

### Batches Fréquents (4-10) : 95 aspects version A uniquement

**Batch 4** : sun-mercury, sun-saturn
```bash
python scripts/generate_aspect_batch.py --batch-number 4 --pairs "sun,mercury" "sun,saturn"
```
- 10 aspects (pas de --ab-test)
- Coût : ~$0.40 USD

**Batch 5 à 10** : Aspects solaires, lunaires, Venus/Mars restants
- Total : 85 aspects
- Coût : ~$3.40 USD

**Total** : 130 aspects, $10.40 USD estimé

---

## 🔄 Workflow Complet par Batch

```bash
# 1. Générer
python scripts/generate_aspect_batch.py --batch-number 1 --pairs "sun,venus" "sun,mars" --ab-test

# 2. Valider
python scripts/validate_aspect_batch.py --input data/batches/batch_01.json --strict

# 3. Sélection A/B manuelle
# Éditer data/batches/batch_01.json
# Pour chaque aspect, remplir :
#   "selected": "a",  // ou "b"
#   "selection_reason": "Plus accessible, ton bienveillant"

# 4. Insérer en BD
python scripts/insert_aspect_batch.py --batch-file data/batches/batch_01.json

# 5. Vérifier insertion
psql $DATABASE_URL -c "SELECT COUNT(*) FROM pregenerated_natal_aspects WHERE version=5;"

# 6. Commit Git
git add data/batches/batch_01.json
git commit -m "feat(api): add aspect interpretations batch 1/10 - sun combos P0"
git push origin main
```

---

## 📁 Structure des Fichiers

```
apps/api/
├── scripts/
│   ├── generate_aspect_batch.py       # Génération Claude Opus 4.5
│   ├── validate_aspect_batch.py       # Validation qualité
│   ├── insert_aspect_batch.py         # Insertion BD
│   └── README_ASPECT_V5.md           # Ce fichier
├── data/
│   ├── batches/                      # JSON batches générés
│   │   ├── batch_01.json
│   │   ├── batch_02.json
│   │   └── ...
│   ├── validation_reports/           # Rapports validation
│   │   └── batch_01.txt
│   └── progress.json                 # Tracking progression
└── docs/
    └── ASPECT_REFONTE_V5.md          # Documentation complète
```

---

## 🔧 Configuration

### Variables d'environnement

```bash
# .env
ANTHROPIC_API_KEY=sk-ant-...           # Clé API Anthropic (Claude Opus 4.5)
DATABASE_URL=postgresql://...          # URL Supabase
```

### Dépendances

```bash
pip install anthropic>=0.18.0  # SDK Anthropic
pip install python-dotenv      # Chargement .env
```

---

## 📝 Critères de Sélection A/B

Lors de la sélection manuelle entre versions A et B :

| Critère | Priorité |
|---------|----------|
| **Accessibilité** | ⭐⭐⭐ Plus important (vocabulaire niveau collège) |
| **Conseil actionnable** | ⭐⭐⭐ Action concrète vs vague |
| **Exemples concrets** | ⭐⭐ Vie quotidienne vs abstrait |
| **Ton bienveillant** | ⭐⭐ Ami vs encyclopédie |
| **Longueur résumé** | ⭐ 50-80 caractères idéal |

**Exemple de décision** :
```json
{
  "selected": "b",
  "selection_reason": "Version B plus accessible : storytelling concret vs insight abstrait. Conseil actionnable avec timing ('attends 24h'). Métaphore 'GPS émotionnel' meilleure que 'tension électrique'."
}
```

---

## ⚠️ Notes Importantes

1. **Rate limiting** : Pause 2s entre générations (respecte limites Claude Pro)
2. **Commits réguliers** : Pusher après chaque batch (reprendre travail ailleurs)
3. **Coûts API** : Budget $10-15 total, tracker dans `progress.json`
4. **Vérification BD** : Toujours vérifier insertion avec SQL check
5. **Backup batches** : Garder JSON avant insertion (rollback possible)

---

## 📚 Ressources

- **Documentation complète** : `apps/api/docs/ASPECT_REFONTE_V5.md`
- **Plan détaillé** : `.claude/plans/tidy-bubbling-pearl.md`
- **Tests** : `apps/api/tests/test_aspect_explanation_v5.py`
- **Mobile** : `apps/mobile/components/AspectDetailSheet.tsx`

---

**Dernière màj** : 2026-01-30 | **Auteur** : Claude Sonnet 4.5
