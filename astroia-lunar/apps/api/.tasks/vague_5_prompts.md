# Vague 5 : Monitoring & Cleanup - Prompts Multi-Agents

**Durée estimée** : 2h (parallèle avec 3 agents)
**Prérequis** : Vague 4 COMPLÈTE ✅

---

## 🎯 Vue d'ensemble Vague 5

### Objectif
Finaliser le Sprint 5 avec monitoring production, documentation utilisateur, et nettoyage backup.

### Tâches assignées

| Agent | Tâches | Durée | Dépendances |
|-------|--------|-------|-------------|
| **Agent A** | Task 5.1 : Endpoint /metrics Prometheus | 2h | ✅ Vague 1 (métriques définies) |
| **Agent B** | Task 5.2 : Documentation API V2 utilisateur | 1h30 | ✅ Vague 3 (routes finales) |
| **Agent C** | Task 5.3 + 5.4 : Cleanup backup + CLAUDE.md | 45min | ✅ Vague 4 (validation) |

---

## 🤖 Agent A : Endpoint /metrics Prometheus (2h)

### Contexte
Les métriques Prometheus ont déjà été définies dans `services/lunar_interpretation_generator.py` lors de la Vague 1 (Task 2.1, Agent B). Tu dois maintenant exposer ces métriques via un endpoint `/metrics` pour monitoring production.

### Tâche : Task 5.1 - Implémenter endpoint /metrics

**Fichiers à modifier** :
- `apps/api/main.py` (intégration endpoint)

**Fichiers à créer (optionnel)** :
- `apps/api/services/lunar_metrics.py` (centralisation métriques)

### Instructions détaillées

#### 1. Vérifier métriques existantes

Les métriques suivantes sont déjà définies dans `services/lunar_interpretation_generator.py` :

```python
from prometheus_client import Counter, Histogram, Gauge

lunar_interpretation_generated = Counter(
    'lunar_interpretation_generated_total',
    'Total lunar interpretations generated',
    ['source', 'model', 'subject', 'version']
)

lunar_interpretation_cache_hit = Counter(
    'lunar_interpretation_cache_hit_total',
    'Total cache hits',
    ['subject', 'version']
)

lunar_interpretation_fallback = Counter(
    'lunar_interpretation_fallback_total',
    'Total fallbacks to templates',
    ['fallback_level']
)

lunar_interpretation_duration = Histogram(
    'lunar_interpretation_duration_seconds',
    'Duration of interpretation generation',
    ['source', 'subject'],
    buckets=(0.05, 0.1, 0.5, 1, 2, 5, 10, 30)
)

lunar_active_generations = Gauge(
    'lunar_active_generations',
    'Number of active generations in progress'
)
```

✅ **Validation** : Ces métriques sont déjà créées et utilisées dans le code.

#### 2. Ajouter endpoint /metrics dans main.py

**Fichier** : `apps/api/main.py`

**Modification** :

```python
from prometheus_client import make_asgi_app, Info

# Créer l'app Prometheus ASGI
metrics_app = make_asgi_app()

# Ajouter métrique Info pour tracking migration
lunar_migration_info = Info(
    'lunar_migration',
    'État migration V1 → V2'
)
lunar_migration_info.info({
    'version': '2.0',
    'templates_count': '1728',
    'migration_date': '2026-01-23',
    'architecture': '4_layers'
})

# Monter l'endpoint /metrics
app.mount("/metrics", metrics_app)
```

**Placement** : Juste après la création de l'app FastAPI, avant les routes.

#### 3. Tester l'endpoint /metrics

```bash
# Démarrer l'API
cd apps/api
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Tester endpoint
curl http://localhost:8000/metrics

# Output attendu : métriques Prometheus format texte
# HELP lunar_interpretation_generated_total Total lunar interpretations generated
# TYPE lunar_interpretation_generated_total counter
# lunar_interpretation_generated_total{source="claude",model="opus-4-5",subject="full",version="2"} 42.0
# ...
```

#### 4. (Optionnel) Centraliser métriques dans lunar_metrics.py

Si tu juges utile de séparer les métriques du generator pour meilleure organisation :

**Fichier** : `apps/api/services/lunar_metrics.py`

```python
"""
Centralized Prometheus metrics for Lunar V2 architecture.
"""
from prometheus_client import Counter, Histogram, Gauge, Info

# Counters
lunar_interpretation_generated = Counter(
    'lunar_interpretation_generated_total',
    'Total lunar interpretations generated',
    ['source', 'model', 'subject', 'version']
)

lunar_interpretation_cache_hit = Counter(
    'lunar_interpretation_cache_hit_total',
    'Total cache hits',
    ['subject', 'version']
)

lunar_interpretation_fallback = Counter(
    'lunar_interpretation_fallback_total',
    'Total fallbacks to templates',
    ['fallback_level']
)

# Histograms
lunar_interpretation_duration = Histogram(
    'lunar_interpretation_duration_seconds',
    'Duration of interpretation generation',
    ['source', 'subject'],
    buckets=(0.05, 0.1, 0.5, 1, 2, 5, 10, 30)
)

# Gauges
lunar_active_generations = Gauge(
    'lunar_active_generations',
    'Number of active generations in progress'
)

# Info
lunar_migration_info = Info(
    'lunar_migration',
    'État migration V1 → V2'
)
lunar_migration_info.info({
    'version': '2.0',
    'templates_count': '1728',
    'migration_date': '2026-01-23',
    'architecture': '4_layers'
})
```

**Puis refactorer imports** :
```python
# Dans lunar_interpretation_generator.py
from services.lunar_metrics import (
    lunar_interpretation_generated,
    lunar_interpretation_cache_hit,
    lunar_interpretation_fallback,
    lunar_interpretation_duration,
    lunar_active_generations
)
```

⚠️ **Note** : Cette étape est optionnelle. Les métriques fonctionnent déjà dans le generator.

#### 5. (Optionnel) Dashboard Grafana

Si tu veux créer un dashboard Grafana :

**Fichier** : `apps/api/docs/grafana_dashboard_lunar.json`

**Panels à inclure** :
- Total interprétations générées (par source)
- Cache hit rate (%)
- Fallback rate (%)
- Durée moyenne génération (p50, p95, p99)
- Générations actives (gauge)

**Queries Prometheus** :
```promql
# Cache hit rate
rate(lunar_interpretation_cache_hit_total[5m]) / rate(lunar_interpretation_generated_total[5m]) * 100

# Fallback rate
rate(lunar_interpretation_fallback_total[5m]) / rate(lunar_interpretation_generated_total[5m]) * 100

# Durée p95
histogram_quantile(0.95, lunar_interpretation_duration_seconds_bucket)
```

### Critères de succès

✅ Endpoint `/metrics` accessible et retourne métriques Prometheus
✅ Métriques correctement exportées (format Prometheus texte)
✅ Test manuel avec curl fonctionne
✅ Aucune régression sur tests existants (`pytest -q`)
✅ (Optionnel) Dashboard Grafana créé

### Commandes de validation

```bash
# Test endpoint
curl http://localhost:8000/metrics | grep lunar_

# Run tests
pytest -q

# Vérifier métriques dans logs
tail -f logs/app.log | grep prometheus
```

### Complétion

Une fois terminé, utilise le script de complétion :

```bash
bash scripts/agent_complete.sh task_5_1
```

---

## 🤖 Agent B : Documentation API V2 Utilisateur (1h30)

### Contexte
Les routes Lunar V2 ont été finalisées en Vague 3. Tu dois maintenant créer une documentation complète pour les utilisateurs de l'API (développeurs frontend, partenaires, etc.).

### Tâche : Task 5.2 - Documentation finale utilisateur

**Fichiers à créer** :
- `apps/api/docs/API_LUNAR_V2.md`

**Fichiers à consulter** :
- `apps/api/routes/lunar_returns.py` (routes principales)
- `apps/api/routes/lunar.py` (endpoints V2)
- `apps/api/docs/LUNAR_ARCHITECTURE_V2.md` (contexte architecture)

### Instructions détaillées

#### 1. Structure du document

Le document doit contenir les sections suivantes :

```markdown
# API Lunar V2 - Documentation Utilisateur

## 🎯 Introduction

### Qu'est-ce que l'API Lunar V2 ?
[Description courte de l'API et son objectif]

### Nouveautés V2
- Génération à la volée via Claude Opus 4.5
- Hiérarchie fallback intelligente (4 niveaux)
- Metadata complètes sur chaque réponse
- Idempotence garantie
- Force regenerate disponible

### Breaking changes depuis V1
[Si applicable]

---

## 🚀 Quick Start

### Prérequis
- Compte Astroia avec API key
- Token JWT valide

### Exemple minimal

```bash
# 1. Authentification
curl -X POST https://api.astroia.com/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "***"}'

# 2. Obtenir rapport lunaire
curl -X POST https://api.astroia.com/api/lunar-returns/current/report \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"month": "2026-02"}'
```

---

## 📚 Endpoints

### GET /api/lunar-returns/current/report
[Documentation détaillée]

### POST /api/lunar/interpretation/regenerate
[Documentation détaillée]

### GET /api/lunar/interpretation/metadata
[Documentation détaillée]

---

## 📦 Schémas

### LunarReport
[Schéma JSON complet]

### InterpretationMetadata
[Schéma JSON complet]

---

## 🔄 Migration V1 → V2

### Changements d'API
[Liste des changements]

### Rétrocompatibilité
[Ce qui est préservé]

### Dépréciation
[Ce qui est deprecated]

---

## ❓ FAQ

### Q: Quelle est la différence entre cache DB et génération Claude ?
A: ...

### Q: Comment forcer une nouvelle génération ?
A: ...

---

## 🛠️ Troubleshooting

### Erreur 401 Unauthorized
[Solution]

### Metadata.source = "hardcoded"
[Explication + solution]

---

## 📊 Performance & Limites

### Rate limits
[Si applicable]

### Temps de réponse
- Cache hit (DB temporelle) : <100ms
- Génération Claude : 2-5s
- Fallback template : <200ms
```

#### 2. Exemples curl complets

Pour chaque endpoint, fournis :
- Exemple de requête
- Exemple de réponse (200 OK)
- Exemples d'erreurs (400, 401, 403, 404, 500)

**Exemple GET /metadata** :
```bash
# Requête
curl -X GET https://api.astroia.com/api/lunar/interpretation/metadata \
  -H "Authorization: Bearer $TOKEN"

# Réponse 200
{
  "total_interpretations": 1543,
  "models_used": [
    {"model": "claude-opus-4-5-20251101", "count": 1200, "percentage": 77.8},
    {"model": "template", "count": 343, "percentage": 22.2}
  ],
  "cached_rate": 65.3,
  "last_generated": "2026-01-23T15:42:00Z",
  "cached": true
}

# Réponse 401
{
  "detail": "Not authenticated"
}
```

#### 3. Schémas Pydantic à jour

Extrais les schémas depuis le code et formate-les en JSON Schema :

```python
# Dans routes/lunar.py
class RegenerateInterpretationRequest(BaseModel):
    lunar_return_id: int
    subject: Literal["full", "climate", "focus", "approach"] = "full"

class InterpretationMetadata(BaseModel):
    source: Literal["db_temporal", "claude", "db_template", "hardcoded"]
    model_used: str | None
    subject: str
    regenerated_at: datetime
    forced: bool

class RegenerateInterpretationResponse(BaseModel):
    interpretation: str
    weekly_advice: str | None
    metadata: InterpretationMetadata
```

Converti en JSON Schema pour la doc.

#### 4. Section Migration V1 → V2

**Breaking changes** :
- Aucun (rétrocompatibilité totale via legacy wrapper)

**Nouveaux champs** :
- `metadata` dans toutes les réponses
  - `source` : Indique d'où vient l'interprétation
  - `model_used` : Quel modèle Claude a généré (si applicable)
  - `version` : Version architecture (toujours 2)
  - `generated_at` : Timestamp génération

**Dépréciations** :
- Ancien service V1 (pregenerated_lunar_interpretations) : ⚠️ Deprecated
- Utiliser les nouvelles routes V2 pour bénéficier des améliorations

#### 5. FAQ & Troubleshooting

Réponds aux questions fréquentes :

**Q: Quelle est la différence entre `source: "db_temporal"` et `source: "db_template"` ?**
A: `db_temporal` = interprétation générée précédemment et cachée en DB (idempotence). `db_template` = template statique migré depuis V1 (fallback si génération Claude échoue).

**Q: Comment forcer une nouvelle génération si je ne suis pas satisfait ?**
A: Utilise l'endpoint `POST /api/lunar/interpretation/regenerate` avec `force_regenerate: true`.

**Q: Pourquoi `model_used: null` ?**
A: L'interprétation vient d'un template ou d'un fallback hardcodé (pas générée par Claude).

### Critères de succès

✅ Document complet et structuré
✅ Tous les endpoints V2 documentés
✅ Exemples curl fonctionnels et testés
✅ Schémas JSON à jour
✅ Section migration claire
✅ FAQ répond aux questions fréquentes
✅ Troubleshooting couvre les cas courants

### Commandes de validation

```bash
# Tester tous les exemples curl du document
bash docs/test_api_examples.sh

# Vérifier liens internes
markdown-link-check docs/API_LUNAR_V2.md
```

### Complétion

Une fois terminé, utilise le script de complétion :

```bash
bash scripts/agent_complete.sh task_5_2
```

---

## 🤖 Agent C : Cleanup Backup + CLAUDE.md (45min)

### Contexte
La migration V2 est complète et validée depuis plusieurs vagues. Tu dois maintenant nettoyer la table backup et mettre à jour CLAUDE.md pour marquer le Sprint 5 comme terminé.

### Tâche : Task 5.3 - Cleanup tables backup (15min)

**⚠️ ATTENTION : Opération irréversible sur DB prod**

#### Instructions détaillées

##### 1. Validation finale prod

Avant de supprimer la table backup, vérifie que la prod fonctionne bien avec V2 :

```sql
-- Vérifier générations récentes
SELECT
  COUNT(*) as total_generated,
  COUNT(DISTINCT user_id) as unique_users,
  model_used
FROM lunar_interpretations
WHERE created_at > NOW() - INTERVAL '7 days'
GROUP BY model_used;

-- Expected : Plusieurs utilisateurs, mix de modèles (claude + templates)
```

**Critère de validation** :
- ✅ Au moins 10+ interprétations générées
- ✅ Au moins 3+ utilisateurs uniques
- ✅ Mix de sources (claude + db_template + db_temporal)

##### 2. Créer migration cleanup

```bash
cd apps/api
alembic revision -m "cleanup_backup_lunar_interpretations"
```

**Fichier créé** : `alembic/versions/xxx_cleanup_backup.py`

**Contenu** :
```python
"""cleanup_backup_lunar_interpretations

Revision ID: xxx
Revises: yyy
Create Date: 2026-01-23

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'xxx'
down_revision = 'yyy'
branch_labels = None
depends_on = None

def upgrade():
    """
    Drop backup table pregenerated_lunar_interpretations_backup.

    This table was created during V1 → V2 migration to preserve original data.
    After successful V2 deployment and validation, it is no longer needed.

    WARNING: This operation is IRREVERSIBLE. Ensure V2 is stable before running.
    """
    op.drop_table('pregenerated_lunar_interpretations_backup')

def downgrade():
    """
    Cannot restore backup after cleanup.

    Raises NotImplementedError to prevent accidental downgrade.
    """
    raise NotImplementedError(
        "Cannot restore backup table after cleanup. "
        "If you need to rollback, restore from database backup snapshot."
    )
```

##### 3. Exécuter migration

```bash
# Dry-run (vérifier SQL généré)
alembic upgrade head --sql

# Exécuter migration
alembic upgrade head

# Vérifier table supprimée
psql $DATABASE_URL -c "\dt pregenerated_lunar_interpretations_backup"
# Expected: Did not find any relation named "pregenerated_lunar_interpretations_backup"
```

##### 4. Logger dans MIGRATION_PLAN.md

Ajoute une section "Cleanup Backup" :

```markdown
## Cleanup Backup (23/01/2026)

### Actions
- ✅ Validation prod : 10+ interprétations, 3+ utilisateurs
- ✅ Migration Alembic créée : `xxx_cleanup_backup.py`
- ✅ Table `pregenerated_lunar_interpretations_backup` supprimée
- ✅ Espace DB libéré : ~2MB

### Résultat
Migration V1 → V2 totalement finalisée. Backup table n'est plus accessible.
```

### Tâche : Task 5.4 - Mise à jour CLAUDE.md final (30min)

**Fichier** : `.claude/CLAUDE.md`

#### Instructions détaillées

##### 1. Marquer Sprint 5 complet

Remplace la section Sprint 5 :

```markdown
## 📊 Sprint 5 (Janvier 2026) - ✅ TERMINÉ

### 🎯 Objectifs
1. ✅ Refonte Architecture Lunar V1 → V2
2. ✅ Génération à la volée Claude Opus 4.5
3. ✅ Système multi-agents (3 agents parallèles)
4. ✅ Monitoring production Prometheus

### 📈 État Final (23/01/2026)
- ✅ **Architecture V2** : 4 couches opérationnelles (DB temporelle, Claude, DB templates, hardcoded)
- ✅ **1728 templates migrés** : pregenerated → lunar_interpretation_templates
- ✅ **Service génération** : lunar_interpretation_generator.py avec retry/logs/métriques
- ✅ **Routes API** : GET /current/report, POST /regenerate, GET /metadata
- ✅ **Monitoring** : Endpoint /metrics Prometheus avec 5 métriques
- ✅ **Tests** : 525 passed (100% compatibilité, 88% coverage generator)
- ✅ **Documentation** : API_LUNAR_V2.md complète
- ✅ **Cleanup** : Table backup supprimée

### ✅ Réalisations Sprint 5

**5 Vagues Multi-Agents** :
- ✅ **Vague 1** : Foundation (Agent A, B, C)
- ✅ **Vague 2** : Service Layer (Agent A, B, C)
- ✅ **Vague 3** : API Routes (Agent A, B, C)
- ✅ **Vague 4** : Testing & QA (Agent A, B)
- ✅ **Vague 5** : Monitoring & Cleanup (Agent A, B, C)

**Timeline** :
- Séquentiel estimé : 23h (3 jours)
- Parallèle réalisé : 13h30 (2 jours avec 3 agents)
- **Gain performance : 41%** 🚀

### 🎯 **Sprint 5 : COMPLET** ✅
Migration Lunar V1 → V2 TERMINÉE À 100%, ready pour production
```

##### 2. Mettre à jour "Fichiers critiques"

Ajoute les nouveaux fichiers V2 :

```markdown
### Fichiers critiques
```
apps/api/
├── main.py                                  Endpoint /metrics Prometheus (Vague 5)
├── models/
│   ├── lunar_interpretation.py              🆕 Narration IA temporelle (V2)
│   └── lunar_interpretation_template.py     🆕 Templates fallback (V2)
├── services/
│   ├── lunar_interpretation_generator.py    🆕 Génération V2 (métriques, logs, retry)
│   ├── lunar_interpretation_legacy_wrapper.py   🆕 Wrapper rétrocompatibilité V1→V2
│   ├── lunar_report_builder.py              Reports V4 + V2 integration
│   └── ...
├── routes/
│   ├── lunar_returns.py                     🆕 Metadata V2 exposée
│   └── lunar.py                             🆕 POST /regenerate, GET /metadata
├── docs/
│   ├── LUNAR_ARCHITECTURE_V2.md             🆕 Architecture 4 couches
│   ├── MIGRATION_PLAN.md                    🆕 Plan 5 sprints multi-agents
│   └── API_LUNAR_V2.md                      🆕 Documentation API utilisateur
└── .tasks/                                  🆕 Coordination multi-agents
    ├── vague_1_prompts.md → vague_5_prompts.md
    ├── sprint_status.json
    └── agent_registry.json
```
```

##### 3. Ajouter Troubleshooting V2

Nouvelle section :

```markdown
### ⭐ Problème : Endpoint /metrics ne répond pas

```
Symptôme : HTTP 404 sur /metrics
Causes possibles :
1. Prometheus pas installé (pip install prometheus-client)
2. Endpoint pas monté dans main.py
3. Port firewall bloqué

Solution :
1. Vérifier installation :
   pip show prometheus-client

2. Vérifier main.py :
   grep "make_asgi_app" apps/api/main.py
   grep 'app.mount("/metrics"' apps/api/main.py

3. Test local :
   curl http://localhost:8000/metrics | head -20
```
```

### Critères de succès

**Task 5.3** :
✅ Table backup supprimée
✅ Migration Alembic créée et exécutée
✅ Aucun impact prod
✅ MIGRATION_PLAN.md à jour

**Task 5.4** :
✅ Sprint 5 marqué comme TERMINÉ
✅ Section Architecture V2 complète
✅ Fichiers critiques à jour
✅ Troubleshooting V2 ajouté
✅ Timeline Vagues documentée

### Commandes de validation

```bash
# Vérifier table backup supprimée
psql $DATABASE_URL -c "\dt pregenerated_lunar_interpretations_backup"

# Vérifier CLAUDE.md mis à jour
grep "Sprint 5.*TERMINÉ" .claude/CLAUDE.md

# Vérifier timeline
grep "Vague 5.*COMPLÈTE" .claude/CLAUDE.md
```

### Complétion

Une fois terminé, utilise le script de complétion :

```bash
bash scripts/agent_complete.sh task_5_3
bash scripts/agent_complete.sh task_5_4
```

---

## 📊 Validation Finale Vague 5

### Checklist complète

- [ ] **Agent A** : Endpoint /metrics fonctionne
- [ ] **Agent A** : Tests passent (pytest -q)
- [ ] **Agent B** : API_LUNAR_V2.md complet
- [ ] **Agent B** : Exemples curl testés
- [ ] **Agent C** : Table backup supprimée
- [ ] **Agent C** : CLAUDE.md Sprint 5 TERMINÉ
- [ ] **Global** : Aucune régression (525+ tests passed)
- [ ] **Global** : Sprint 5 lockés comme completed

### Commandes validation globale

```bash
# Tests
cd apps/api
pytest -q

# Endpoint /metrics
curl http://localhost:8000/metrics | grep lunar_

# Table backup
psql $DATABASE_URL -c "\dt pregenerated_lunar_interpretations_backup"

# CLAUDE.md
grep "Sprint 5.*TERMINÉ" .claude/CLAUDE.md
grep "Vague 5.*COMPLÈTE" .claude/CLAUDE.md

# Locks
ls .tasks/locks/  # Doit être vide
ls .tasks/completed/ | grep task_5  # Doit contenir task_5_1, task_5_2, task_5_3, task_5_4
```

---

## 🎉 Félicitations !

Une fois la Vague 5 terminée, le **Sprint 5 sera COMPLET à 100%** ! 🎊

**Migration Lunar V1 → V2 : TERMINÉE** ✨
- 1728 templates migrés
- Architecture 4 couches opérationnelle
- Génération Claude temps réel
- Monitoring Prometheus actif
- Documentation complète
- Tests >500 passing

**Timeline réalisée** :
- Sprint 0 : 2h (Foundation)
- Sprint 1 : 1h30 (Infra & Docs)
- Vague 1 : 2h (Foundation)
- Vague 2 : 2h30 (Service Layer)
- Vague 3 : 1h30 (API Routes)
- Vague 4 : 3h30 (Testing & QA)
- Vague 5 : 2h (Monitoring & Cleanup)
────────────────────────────────────────
**Total : 15h (vs 25h séquentiel = 40% gain)** 🚀

---

**Dernière mise à jour** : 2026-01-23
**Version** : 5.0 (Vague 5 - Monitoring & Cleanup)
