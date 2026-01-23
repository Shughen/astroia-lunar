# Vague 1 : Prompts Agents (Référence)

**Date** : 2026-01-23
**Durée** : 2h
**Agents** : 3 (Agent A, Agent B, Agent C)

---

## Agent A (Claude Main) - Sprint 1 Complet

**Status** : ⏳ EN COURS (exécuté automatiquement)

**Tâches** :
- Task 1.2 : Scripts utilitaires agents (45min)
- Task 1.3 : Tests modèles DB (1h30) ⭐
- Task 1.4 : Documentation plan (compléter MIGRATION_PLAN.md) (1h)

**Note** : Task 1.1 (CLAUDE.md) déjà complétée.

---

## Agent B - Task 2.1 (Enrichir Generator)

**Prompt** : Voir conversation principale (23/01/2026 14:30)

**Résumé** :
```markdown
# TASK 2.1 : Enrichir lunar_interpretation_generator.py

Ajouter à `services/lunar_interpretation_generator.py` :
1. Prometheus metrics (5 metrics)
2. Structured logging (structlog)
3. Retry logic (tenacity, 3 attempts)
4. Timeouts (30s max)
5. Error categorization (4 custom exceptions)

Durée : 2h
Priority : ⭐⭐⭐ HIGH

DoD :
- Prometheus metrics exportées
- Logs JSON structurés
- Retry logic testé
- Timeout 30s appliqué
- Tests passent
```

**Lock file** : `.tasks/locks/task_2_1.lock`

---

## Agent C - Task 2.3 (Legacy Wrapper)

**Prompt** : Voir conversation principale (23/01/2026 14:30)

**Résumé** :
```markdown
# TASK 2.3 : Créer Facade Rétrocompatibilité

Créer `services/lunar_interpretation_legacy_wrapper.py` :
- Wrapper load_lunar_interpretation_with_fallback()
- Traduction signature V1 → V2
- Deprecation warnings
- Tests backward compatibility

Durée : 1h30
Priority : ⭐⭐ MEDIUM

DoD :
- Wrapper fonctionnel
- Warnings émis correctement
- Tests passent
- Documentation inline
```

**Lock file** : `.tasks/locks/task_2_3.lock`

---

## Validation Vague 1

Après complétion des 3 agents :

```bash
# 1. Vérifier locks déplacés
ls .tasks/completed/ | grep -E "task_1_[234]|task_2_[13]"
# Expected: 5 files

# 2. Run tests
cd /Users/remibeaurain/astroia/astroia-lunar/apps/api
pytest -q

# 3. Vérifier commits
git log --oneline -5
# Expected: 3+ commits (Agent A, B, C)

# 4. Update sprint_status.json
# Marquer Vague 1 complète, Vague 2 ready
```

---

## Prompts Complets

**Agent B (Task 2.1)** : ~150 lignes
**Agent C (Task 2.3)** : ~120 lignes

Voir conversation principale pour prompts complets copy-paste ready.

---

**Prochaine étape** : Après Vague 1 → Générer prompts Vague 2
