# Interprétations Natales Pré-générées

## 📋 Vue d'ensemble

Ce système remplace le message "Interprétation non disponible (mode sans LLM)" par des **interprétations astrologiques réelles**, pré-générées avec Claude Opus 4.5 et sauvegardées dans des fichiers markdown.

**Contrainte clé** : Aucun appel API en runtime, toutes les interprétations sont chargées depuis les fichiers.

---

## 🎯 Objectif

- **Mode LLM OFF** (`NATAL_LLM_MODE=off`) : Les utilisateurs reçoivent des interprétations réelles stockées dans des fichiers markdown
- **Mode LLM ON** (`NATAL_LLM_MODE=anthropic`) : Appels API Claude comme avant (Sonnet + fallback Haiku)
- **Fallback intelligent** : Si fichier manquant, afficher un placeholder propre

---

## 📁 Structure des fichiers

```
apps/api/data/natal_interpretations/
└── v2/                                    # Version moderne avec micro-rituel
    ├── sun/
    │   ├── aquarius_11.md                 # Soleil en Verseau, Maison 11
    │   ├── taurus_2.md                    # etc.
    │   └── ...
    ├── moon/
    │   ├── taurus_2.md                    # Lune en Taureau, Maison 2
    │   └── ...
    ├── mercury/
    │   ├── gemini_3.md                    # Mercure en Gémeaux, Maison 3
    │   └── ...
    ├── venus/
    │   ├── libra_7.md                     # Vénus en Balance, Maison 7
    │   └── ...
    ├── mars/
    │   ├── aries_1.md                     # Mars en Bélier, Maison 1
    │   └── ...
    ├── jupiter/
    │   ├── sagittarius_9.md               # Jupiter en Sagittaire, Maison 9
    │   └── ...
    ├── saturn/
    │   ├── capricorn_10.md                # Saturne en Capricorne, Maison 10
    │   └── ...
    ├── north_node/
    │   ├── aquarius_11.md                 # Nœud Nord en Verseau, Maison 11
    │   └── ...
    └── ...
```

**Nomenclature** : `{subject}/{sign}_{house}.md`
- `subject` : Identifiant planétaire en anglais (sun, moon, mercury, etc.)
- `sign` : Signe en anglais (aries, taurus, gemini, etc.)
- `house` : Numéro de maison (1-12)

---

## 📝 Format des fichiers markdown

Chaque fichier contient :
1. **Frontmatter YAML** avec métadonnées
2. **Contenu markdown** avec le template v2

Exemple : `data/natal_interpretations/v2/sun/aquarius_11.md`

```markdown
---
subject: sun
subject_label: Soleil
sign: Verseau
house: 11
emoji: ☀️
version: 2
lang: fr
length: 1150
---

# ☀️ Soleil en Verseau

**En une phrase :** Tu rayonnes par ton authenticité et ta vision progressiste du collectif.

## Ton moteur
Ton identité centrale vibre à la fréquence de l'innovation et de la liberté. Tu as besoin de sentir que tu contribues à quelque chose de plus grand, que tu apportes une perspective unique qui fait bouger les lignes. L'indépendance intellectuelle est ta source de vitalité.

## Ton défi
Équilibrer ton besoin de détachement rationnel avec la chaleur humaine des liens proches. Parfois, ton refus des conventions peut t'isoler ou te faire paraître distant, même quand tu cherches sincèrement à te connecter.

## Maison 11 en Verseau
Cette énergie s'exprime naturellement dans tes projets collectifs et tes amitiés. Ta vision progressiste trouve ici son terrain d'expression idéal, au service du groupe et des idéaux partagés. Le réseau et la communauté sont tes leviers d'action.

## Micro-rituel du jour (2 min)
- Envoie un message à quelqu'un en exprimant une idée qui te passionne, sans attendre de validation.
- 3 cycles : inspire en visualisant un courant électrique bleu, expire en libérant toute pression de conformité.
- "Où puis-je être plus authentiquement moi aujourd'hui, même si ça surprend ?"
```

---

## 🔧 Architecture technique

### 1. Fonction de chargement

**Fichier** : `apps/api/services/natal_interpretation_service.py`

```python
def load_pregenerated_interpretation(
    subject: str,
    sign: str,
    house: int,
    version: int = 2
) -> Optional[str]:
    """
    Charge une interprétation pré-générée depuis les fichiers markdown

    Args:
        subject: Nom du sujet (sun, moon, etc.)
        sign: Nom du signe en français (Verseau, Taureau, etc.)
        house: Numéro de maison (1-12)
        version: Version du prompt (2 ou 4)

    Returns:
        Texte markdown complet OU None si fichier introuvable
    """
```

**Fonctionnement** :
1. Normalise le signe français → anglais via `SIGN_FR_TO_EN`
2. Construit le chemin fichier : `data/natal_interpretations/v{version}/{subject}/{sign}_{house}.md`
3. Lit le fichier et extrait le markdown (après frontmatter YAML)
4. Retourne le texte OU None si fichier introuvable

### 2. Mapping des signes

```python
SIGN_FR_TO_EN = {
    'bélier': 'aries',
    'belier': 'aries',          # Variante sans accent
    'taureau': 'taurus',
    'gémeaux': 'gemini',
    'gemeaux': 'gemini',        # Variante sans accent
    'cancer': 'cancer',
    'lion': 'leo',
    'vierge': 'virgo',
    'balance': 'libra',
    'scorpion': 'scorpio',
    'sagittaire': 'sagittarius',
    'capricorne': 'capricorn',
    'verseau': 'aquarius',
    'poissons': 'pisces'
}
```

### 3. Intégration dans le service

**Fichier** : `apps/api/services/natal_interpretation_service.py`

La fonction `generate_with_sonnet_fallback_haiku()` a été modifiée :

```python
async def generate_with_sonnet_fallback_haiku(...):
    # Vérifier le mode LLM
    llm_mode = settings.NATAL_LLM_MODE.lower()

    if llm_mode != "anthropic":
        # Mode off : essayer de charger interprétation pré-générée
        pregenerated_text = load_pregenerated_interpretation(...)

        if pregenerated_text:
            return pregenerated_text, "pregenerated"

        # Fallback sur placeholder si fichier manquant
        placeholder_text = generate_placeholder_interpretation(...)
        return placeholder_text, "placeholder"

    # Mode anthropic : appel API Claude (logique existante)
    ...
```

---

## 🚀 Utilisation

### Configuration

Dans `.env` (ou config par défaut) :

```bash
# Mode LLM off : utiliser interprétations pré-générées
NATAL_LLM_MODE=off

# OU

# Mode LLM on : appels API Claude
NATAL_LLM_MODE=anthropic
ANTHROPIC_API_KEY=sk-ant-...
```

### Génération d'interprétations

Les interprétations sont générées **directement avec Claude Code** (Opus 4.5), pas via script Python :

1. Utiliser l'outil `Task` avec `model="opus"` pour générer le texte
2. Sauvegarder dans le fichier markdown approprié avec frontmatter YAML
3. Vérifier la longueur (900-1400 chars pour v2)

**Template de génération** (voir `scripts/generate_natal_interpretations.py` pour référence) :

```python
# Prompt pour Opus 4.5
prompt = f"""Tu es un·e astrologue moderne pour l'app Lunation...

DONNÉES DU THÈME:
- {subject_label} en {sign_label}
- {house_full}

TEMPLATE À SUIVRE (EXACT):
# {emoji} {subject_label} en {sign_label}
**En une phrase :** ...

## Ton moteur
...

## Ton défi
...

## Maison {house} en {sign_label}
...

## Micro-rituel du jour (2 min)
- ...
- ...
- ...

CONTRAINTES STRICTES:
1. LONGUEUR: 900 à 1200 caractères
2. INTERDIT: "tu es quelqu'un de...", prédictions, conseils santé
3. OBLIGATOIRE: Croiser planète + signe + maison
...
"""
```

---

## ✅ Tests

**Fichier** : `apps/api/tests/test_natal_interpretation_pregenerated.py`

Tests disponibles :
- `test_sign_mapping_fr_to_en` : Mapping des signes
- `test_load_pregenerated_*` : Chargement de chaque interprétation
- `test_load_pregenerated_not_found` : Fichier inexistant
- `test_load_pregenerated_case_insensitive` : Casse insensible
- `test_generate_with_fallback_mode_off` : Intégration complète mode off
- `test_generate_with_fallback_mode_off_not_found` : Fallback placeholder
- `test_interpretation_quality` : Qualité (longueur, structure)

**Lancer les tests** :

```bash
cd apps/api
pytest tests/test_natal_interpretation_pregenerated.py -v
```

**Résultat attendu** : 14 tests passent ✅

---

## 📊 Interprétations existantes (v2)

| Sujet | Signe | Maison | Fichier | Statut |
|-------|-------|--------|---------|--------|
| Soleil | Verseau | 11 | `sun/aquarius_11.md` | ✅ |
| Lune | Taureau | 2 | `moon/taurus_2.md` | ✅ |
| Mercure | Gémeaux | 3 | `mercury/gemini_3.md` | ✅ |
| Vénus | Balance | 7 | `venus/libra_7.md` | ✅ |
| Mars | Bélier | 1 | `mars/aries_1.md` | ✅ |
| Jupiter | Sagittaire | 9 | `jupiter/sagittarius_9.md` | ✅ |
| Saturne | Capricorne | 10 | `saturn/capricorn_10.md` | ✅ |
| Nœud Nord | Verseau | 11 | `north_node/aquarius_11.md` | ✅ |

**Total** : 8 interprétations pré-générées

---

## 🔄 Workflow de développement

### Ajouter une nouvelle interprétation

1. **Générer le texte avec Claude Code (Opus 4.5)**
   - Utiliser le template v2
   - Vérifier la longueur (900-1400 chars)
   - Croiser systématiquement planète + signe + maison

2. **Créer le fichier markdown**
   ```bash
   touch apps/api/data/natal_interpretations/v2/{subject}/{sign}_{house}.md
   ```

3. **Ajouter le frontmatter + contenu**
   - Voir exemple ci-dessus

4. **Tester**
   ```bash
   pytest tests/test_natal_interpretation_pregenerated.py::test_load_pregenerated_{subject}_{sign}_{house} -v
   ```

5. **Commit**
   ```bash
   git add apps/api/data/natal_interpretations/v2/{subject}/{sign}_{house}.md
   git commit -m "feat: ajouter interprétation {subject} en {sign} M{house}"
   ```

---

## 🛠️ Maintenance

### Régénérer une interprétation

1. Modifier le fichier markdown directement
2. Ou régénérer avec Claude Code (Opus 4.5)
3. Tester avec `pytest`
4. Commit

### Vérifier la couverture

```bash
# Lister toutes les combinaisons existantes
find apps/api/data/natal_interpretations/v2 -name "*.md" | sort

# Total fichiers
find apps/api/data/natal_interpretations/v2 -name "*.md" | wc -l
```

### Problèmes courants

| Problème | Solution |
|----------|----------|
| Fichier non trouvé | Vérifier le mapping `SIGN_FR_TO_EN` |
| Frontmatter mal parsé | Vérifier `---` au début et `---` après métadonnées |
| Longueur invalide | Régénérer avec contrainte 900-1400 chars |
| Accents dans les signes | Ajouter variante dans `SIGN_FR_TO_EN` |

---

## 📈 Extensions futures

### Court terme (si besoin)
- Ajouter plus d'interprétations pour d'autres combinaisons fréquentes
- Créer un script CLI pour générer en batch avec Claude Code

### Moyen terme
- Étendre à la version v4 (senior professionnel)
- Ajouter support pour les aspects

### Long terme
- Générer les 2160 combinaisons complètes (15 sujets × 12 signes × 12 maisons)
- Système de traduction automatique (EN, ES, etc.)

---

## 📚 Références

- **Service** : `apps/api/services/natal_interpretation_service.py`
- **Route** : `apps/api/routes/natal_interpretation.py`
- **Modèle DB** : `apps/api/models/natal_interpretation.py`
- **Tests** : `apps/api/tests/test_natal_interpretation_pregenerated.py`
- **Config** : `apps/api/config.py` (variable `NATAL_LLM_MODE`)

---

## ✅ Checklist de validation

- [x] Structure de dossiers créée
- [x] 8 interprétations v2 générées avec Opus 4.5
- [x] Fonction `load_pregenerated_interpretation()` implémentée
- [x] Mapping `SIGN_FR_TO_EN` avec variantes sans accents
- [x] Intégration dans `generate_with_sonnet_fallback_haiku()`
- [x] Tests unitaires (14 tests passent)
- [x] Documentation complète
- [x] Mode LLM off par défaut (`NATAL_LLM_MODE=off`)
- [x] Fallback sur placeholder si fichier manquant

---

**Dernière mise à jour** : 2026-01-18
**Version** : 1.0.0
**Statut** : ✅ Production Ready
