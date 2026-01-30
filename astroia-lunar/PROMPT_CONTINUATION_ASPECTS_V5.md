# 🤖 Prompt de Continuation — Génération Aspects V5

**Date** : 2026-01-30
**Contexte** : Refonte aspects astrologiques v5 (130 aspects prioritaires)
**Progression** : 35/130 aspects générés (26.9%), 20/130 insérés (15.4%)
**Objectif** : Continuer la génération des 95 aspects restants

---

## 📋 Contexte du Projet

### Projet : Astroia Lunar
Application d'astrologie lunaire (FastAPI + React Native) qui génère des révolutions lunaires mensuelles et des thèmes nataux.

### Problème Résolu
Remplacement des interprétations d'aspects v4 (textes identiques, jargon technique) par des interprétations v5 (ton bienveillant, exemples concrets, conseils actionnables).

**Exemple transformation** :

**V4 (mauvais)** :
```
# ☌ Conjonction Soleil - Vénus
**En une phrase :** Symbiose puissante, intensité garantie
## Pourquoi ?
- Fusion fonctionnelle
- Indissociation entre identité et valeurs
```

**V5 (cible)** :
```
# ☌ Conjonction Soleil - Vénus
**En une phrase :** Ton charme devient ton super-pouvoir — tu rayonnes sans effort

## L'énergie de cet aspect
Ce mois-ci, ton identité profonde (Soleil) et ce que tu aimes (Vénus) ne font qu'un.
Les gens te sourient plus facilement, les conversations coulent, tu te sens dans ton élément.

## Manifestations concrètes
- **Relations fluides** : Tu trouves les mots justes, les échanges sont chaleureux
- **Créativité magnétique** : Envie de créer du beau qui te ressemble
- **Charisme naturel** : En groupe, tu attires l'attention sans forcer

## Conseil pratique
Lance ce projet créatif qui te trotte dans la tête, ou dis enfin ce que tu repousses.

## Attention
Gare à vouloir plaire à tout prix — ton charme peut te faire dire oui à des choses
qui ne te correspondent pas vraiment.
```

---

## ✅ Ce qui a été fait (Batches 1-3)

### Batch 1 : sun-venus, sun-mars (10 aspects) ✅ INSÉRÉ
- Conjonction, Opposition, Carré, Trigone, Sextile pour chaque paire
- Format v5 validé
- Insérés en BD (version=5, lang=fr)

### Batch 2 : venus-mars, sun-jupiter (10 aspects) ✅ INSÉRÉ
- Améliorations appliquées :
  - Ouvertures variées (exit "Ce mois-ci, ton X et ton Y...")
  - Sextiles différenciés (Venus = relationnel, Mars = action, Jupiter = expansion)
  - Trigones personnalisés
- Insérés en BD

### Batch 3 : moon-uranus, saturn-uranus, sun-moon (15 aspects) ✅ GÉNÉRÉ
- **Status** : Générés mais **pas encore insérés en BD**
- Aspects : moon-uranus (5), saturn-uranus (5), sun-moon (5)
- Qualité : Encore meilleure différenciation, ouvertures très variées

**📊 Progression** : 35/130 aspects générés (26.9%), 20/130 insérés en BD (15.4%)

---

## 🎯 Tâche à Continuer

### Objectif Immédiat
1. **Insérer Batch 3 en BD** (15 aspects)
2. **Générer Batch 4** : sun-mercury, sun-saturn (10 aspects)
3. **Répéter** jusqu'à complétion des 130 aspects

### Batches Restants (7 batches, 95 aspects)

**Batch 4** (P1) : sun-mercury (5 aspects) + sun-saturn (5 aspects) = 10 aspects
**Batch 5** (P1) : sun-uranus (5) + sun-neptune (5) = 10 aspects
**Batch 6** (P1) : sun-pluto (5) + moon-mercury (5) = 10 aspects
**Batch 7** (P1) : moon-venus (5) + moon-mars (5) = 10 aspects
**Batch 8** (P1) : moon-jupiter (5) + moon-saturn (5) = 10 aspects
**Batch 9** (P1) : moon-neptune (5) + moon-pluto (5) = 10 aspects
**Batch 10** (P1) : venus-jupiter (5) + venus-saturn (5) = 10 aspects

---

## 📐 Format v5 à Respecter

### Structure Markdown

```markdown
# [SYMBOLE] [TYPE] [PLANÈTE 1] - [PLANÈTE 2]

**En une phrase :** [Accroche émotionnelle 50-80 caractères]

## L'énergie de cet aspect

[2-3 phrases expliquant l'interaction planétaire en langage simple]

## Manifestations concrètes

- **[Catégorie 1]** : [Exemple concret dans la vie quotidienne]
- **[Catégorie 2]** : [Impact dans les relations]
- **[Catégorie 3]** : [Effet au travail/créativité]

## Conseil pratique

[Action concrète 100-200 caractères, commence par un verbe d'action]

## Attention

[Piège à éviter 80-150 caractères, commence par "Gare à" ou "Attention à"]
```

### Symboles Aspects

- Conjonction : ☌
- Opposition : ☍
- Carré : □
- Trigone : △
- Sextile : ⚹

### Contraintes Strictes

✅ **Ton** : Bienveillant, accessible, inspirant (parle comme un ami qui connaît l'astro)
✅ **Vocabulaire** : Niveau collège, **JAMAIS** : "indissociation", "contextualiser", "observer", "symbiose puissante"
✅ **Exemples** : Concrets et sensoriels ("Ta créativité explose" pas "potentiel créatif activé")
✅ **Longueurs** :
  - Résumé : 50-80 caractères
  - Manifestations : 350-650 caractères total
  - Conseil : 100-200 caractères
  - Attention : 80-150 caractères

✅ **Différenciation** :
  - Chaque aspect doit être unique (pas de copier-coller)
  - Varier les ouvertures (pas toujours "Ce mois-ci...")
  - Personnaliser selon les planètes :
    - **Sun** : identité, volonté, vitalité
    - **Moon** : émotions, besoins, sécurité
    - **Mercury** : intellect, communication, analyse
    - **Venus** : désirs, valeurs, affectivité, créativité, relations
    - **Mars** : action, pulsions, affirmation, courage
    - **Jupiter** : expansion, optimisme, foi, croissance
    - **Saturn** : structure, limites, responsabilités, discipline
    - **Uranus** : ruptures, innovation, indépendance, liberté
    - **Neptune** : imaginaire, dissolution, transcendance
    - **Pluto** : transformation radicale, pouvoir

✅ **Ancrage temporel** : Toujours "ce mois-ci" (cohérent avec révolution lunaire mensuelle)

---

## 🔧 Workflow d'Insertion

### Étape 1 : Générer les Aspects

Pour chaque batch (10 ou 15 aspects), génère les interprétations complètes en respectant le format v5.

**Exemple prompt** :
```
Génère les 10 aspects pour sun-mercury (5 aspects) et sun-saturn (5 aspects)
en respectant le format v5 :
- Conjonction, Opposition, Carré, Trigone, Sextile pour chaque paire
- Ton bienveillant, exemples concrets, conseils actionnables
- Mercury : intellect, communication / Saturn : structure, limites
- Différencier clairement les sextiles et trigones
```

### Étape 2 : Créer le Script d'Insertion

Créer un fichier Python `insert_batch_XX_direct.py` avec cette structure :

```python
#!/usr/bin/env python3
"""
Insertion directe des X aspects du Batch X en base de données (version=5)
Généré manuellement
"""

import sys
import asyncio
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.dialects.postgresql import insert
from models.pregenerated_natal_aspect import PregeneratedNatalAspect
from config import Settings

settings = Settings()

# Les X aspects du Batch X
ASPECTS = [
    {
        "planet1": "planet1_name",
        "planet2": "planet2_name",
        "aspect_type": "conjunction",
        "content": """[MARKDOWN COMPLET ICI]"""
    },
    # ... autres aspects
]


async def insert_batch_XX():
    """Insère les X aspects du Batch X en base de données."""

    print(f"=== Insertion Batch X ({len(ASPECTS)} aspects) ===\n")

    engine = create_async_engine(settings.DATABASE_URL, echo=False)
    async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    inserted_count = 0

    async with async_session() as session:
        async with session.begin():
            for aspect in ASPECTS:
                planet1 = aspect['planet1']
                planet2 = aspect['planet2']
                aspect_type = aspect['aspect_type']
                content = aspect['content']

                # Normaliser en ordre alphabétique
                p1_norm = planet1.lower().strip()
                p2_norm = planet2.lower().strip()
                if p1_norm > p2_norm:
                    p1_norm, p2_norm = p2_norm, p1_norm

                # Upsert
                stmt = insert(PregeneratedNatalAspect).values(
                    planet1=p1_norm,
                    planet2=p2_norm,
                    aspect_type=aspect_type.lower(),
                    version=5,
                    lang='fr',
                    content=content,
                    length=len(content)
                )

                stmt = stmt.on_conflict_do_update(
                    index_elements=['planet1', 'planet2', 'aspect_type', 'version', 'lang'],
                    set_={
                        'content': stmt.excluded.content,
                        'length': stmt.excluded.length,
                    }
                )

                await session.execute(stmt)
                inserted_count += 1

                print(f"  ✓ {p1_norm} {aspect_type} {p2_norm}")

    await engine.dispose()

    print(f"\n✅ {inserted_count} aspects insérés (version=5, lang=fr)")

    # Vérifier le total
    await check_total_in_db()


async def check_total_in_db():
    """Vérifie le nombre total d'aspects v5 en BD."""
    engine = create_async_engine(settings.DATABASE_URL, echo=False)
    async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    async with async_session() as session:
        from sqlalchemy import select, func
        result = await session.execute(
            select(func.count()).select_from(PregeneratedNatalAspect).where(
                PregeneratedNatalAspect.version == 5,
                PregeneratedNatalAspect.lang == 'fr'
            )
        )
        count = result.scalar()

    await engine.dispose()

    print(f"🔍 Vérification BD : {count} aspects version=5 lang=fr")
    print(f"📊 Progression : {count}/130 aspects ({round(count/130*100, 1)}%)")


if __name__ == '__main__':
    asyncio.run(insert_batch_XX())
```

### Étape 3 : Exécuter et Vérifier

```bash
cd apps/api

# Exécuter le script
python scripts/insert_batch_XX_direct.py

# Vérifier en BD
psql $DATABASE_URL -c "SELECT COUNT(*) FROM pregenerated_natal_aspects WHERE version=5;"

# Mettre à jour progress.json manuellement
```

### Étape 4 : Commit Git

```bash
git add scripts/insert_batch_XX_direct.py data/progress.json
git commit -m "feat(api): add aspect interpretations batch X/10 - [paires]

- Insert X aspects ([liste paires])
- Total: XX/130 aspects inserted (XX.X%)
- Method: manual generation"

git push origin main
```

---

## 📚 Fichiers de Référence

### À Lire Absolument

1. **Documentation technique** : `apps/api/docs/ASPECT_REFONTE_V5.md`
   - Architecture complète v5
   - Format markdown détaillé
   - Exemples avant/après

2. **Scripts existants** :
   - `apps/api/scripts/insert_batch_01_direct.py` (Batch 1, 10 aspects)
   - `apps/api/scripts/insert_batch_02_direct.py` (Batch 2, 10 aspects)

3. **Progress tracking** : `apps/api/data/progress.json`

4. **Résumé session** : `RESUME_SESSION_ASPECTS_V5.md`

### Modèles de Référence

**Bon exemple** (Batch 2, Venus Conjonction Mars) :
```markdown
# ☌ Conjonction Vénus - Mars

**En une phrase :** Désir et action fusionnent — ton charisme devient électrique

## L'énergie de cet aspect

Tes envies (Vénus) et ton élan d'action (Mars) ne font qu'un ce mois-ci. Quand tu veux quelque chose, tu passes à l'acte immédiatement. Ta séduction devient directe, presque audacieuse.

## Manifestations concrètes

- **Séduction assumée** : Tu oses faire le premier pas, déclarer tes intentions
- **Créativité passionnée** : Tes projets artistiques ont du feu, de l'intensité
- **Désirs clairs** : Tu sais ce que tu veux et tu ne t'excuses pas

## Conseil pratique

Profite de cette énergie pour initier ce que tu désires vraiment — relation, projet créatif, plaisir.

## Attention

Gare à la pulsion brute — tu pourrais confondre désir et besoin, ou foncer trop vite.
```

---

## 🎯 Prompt de Démarrage

### Pour Insérer le Batch 3 (15 aspects déjà générés)

```
Je continue le projet Astroia Lunar - Refonte Aspects V5.

Contexte : 35 aspects ont été générés (Batches 1-3), mais seuls 20 sont insérés en BD.

Tâche immédiate : Créer le script insert_batch_03_direct.py pour insérer les 15 aspects
du Batch 3 (moon-uranus, saturn-uranus, sun-moon).

Les 15 interprétations complètes sont disponibles dans la conversation précédente
(cherche "Batch 3 complet : 15 aspects générés").

Crée un script Python similaire à insert_batch_02_direct.py avec :
- Les 15 aspects moon-uranus (5), saturn-uranus (5), sun-moon (5)
- Chaque aspect avec son markdown complet
- Fonction d'insertion identique aux batches précédents

Ensuite, exécute le script et vérifie que 35/130 aspects sont en BD.
```

### Pour Générer le Batch 4 (nouveau)

```
Je continue le projet Astroia Lunar - Refonte Aspects V5.

Progression : 35/130 aspects insérés en BD (26.9%)

Tâche : Générer le Batch 4 (10 aspects) : sun-mercury (5 aspects) + sun-saturn (5 aspects)

Planètes à considérer :
- Sun (Soleil) : ton identité, ta volonté, ta vitalité
- Mercury (Mercure) : ton intellect, ta communication, ton analyse
- Saturn (Saturne) : ta structure, tes limites, tes responsabilités

Format v5 requis (voir PROMPT_CONTINUATION_ASPECTS_V5.md pour détails complets) :
- Conjonction, Opposition, Carré, Trigone, Sextile pour chaque paire
- Ton bienveillant, exemples concrets (pas de jargon)
- Ancrage "ce mois-ci"
- Section "Attention" obligatoire
- Différenciation claire : Mercury = mental/communication, Saturn = structure/discipline

Contraintes :
- Résumé 50-80 chars
- Manifestations 350-650 chars
- Conseil 100-200 chars
- Attention 80-150 chars
- Varier les ouvertures (pas toujours "Ce mois-ci...")

Après génération, crée le script insert_batch_04_direct.py.
```

---

## 📊 Suivi de Progression

### État Actuel

| Batch | Paires | Aspects | Statut | BD |
|-------|--------|---------|--------|----|
| 1 | sun-venus, sun-mars | 10 | ✅ Inséré | ✅ |
| 2 | venus-mars, sun-jupiter | 10 | ✅ Inséré | ✅ |
| 3 | moon-uranus, saturn-uranus, sun-moon | 15 | ✅ Généré | ❌ |
| 4 | sun-mercury, sun-saturn | 10 | ⏳ À faire | ❌ |
| 5 | sun-uranus, sun-neptune | 10 | ⏳ À faire | ❌ |
| 6 | sun-pluto, moon-mercury | 10 | ⏳ À faire | ❌ |
| 7 | moon-venus, moon-mars | 10 | ⏳ À faire | ❌ |
| 8 | moon-jupiter, moon-saturn | 10 | ⏳ À faire | ❌ |
| 9 | moon-neptune, moon-pluto | 10 | ⏳ À faire | ❌ |
| 10 | venus-jupiter, venus-saturn | 10 | ⏳ À faire | ❌ |

**Total** : 35/130 générés (26.9%), 20/130 insérés (15.4%)

### Checklist par Batch

Pour chaque batch :
- [ ] Générer les 10-15 interprétations v5
- [ ] Vérifier format (symboles, sections, longueurs)
- [ ] Créer script insert_batch_XX_direct.py
- [ ] Exécuter le script
- [ ] Vérifier count en BD
- [ ] Mettre à jour data/progress.json
- [ ] Commit Git avec message conventionnel
- [ ] Push origin main

---

## 🔍 Points d'Attention

### Erreurs à Éviter

❌ **Jargon technique** : "indissociation", "fusion fonctionnelle", "contextualiser"
❌ **Textes identiques** : Chaque aspect doit être unique
❌ **Conseils vagues** : "Observer les contextes" → Préférer "Lance ce projet maintenant"
❌ **Timing incohérent** : Éviter "cette semaine", "lundi" → Toujours "ce mois-ci"
❌ **Ton encyclopédique** : Éviter le style Wikipédia

### Qualité Attendue

✅ **Différenciation** : Chaque conjonction/opposition/carré/trigone/sextile a sa saveur
✅ **Personnalité planétaire** : Venus ≠ Mars ≠ Jupiter dans les manifestations
✅ **Ouvertures variées** : "Tu le sens", "Tes émotions", "Quelque chose a changé"
✅ **Exemples concrets** : "En réunion", "Avec tes proches", "Sur ton projet"
✅ **Formules mémorables** : "L'opposition demande un pont, pas un camp"

---

## 🎬 Résumé Exécutif

**Objectif** : Compléter la génération et l'insertion de 130 aspects astrologiques v5

**Méthode** : Génération manuelle avec IA (pas d'API Anthropic, $0 USD)

**Format** : Markdown v5 avec 5 sections (énergie, manifestations, conseil, attention)

**Progression** : 35/130 générés, 20/130 insérés

**Prochaine étape** :
1. Insérer Batch 3 (15 aspects moon-uranus, saturn-uranus, sun-moon)
2. Générer Batch 4 (10 aspects sun-mercury, sun-saturn)
3. Répéter jusqu'à 130 aspects

**Durée estimée** : 6-8h pour les 95 aspects restants (7 batches × 1h)

**Documentation** :
- `apps/api/docs/ASPECT_REFONTE_V5.md` (doc technique)
- `RESUME_SESSION_ASPECTS_V5.md` (résumé session)
- `PROMPT_CONTINUATION_ASPECTS_V5.md` (ce fichier)

---

**Dernière màj** : 2026-01-30 19:30 | **Version** : 1.0 | **Statut** : Ready for continuation 🚀
