# Astroia Lunar – Changelog

Ce document retrace l'historique des commits et l'évolution du projet.

---

## 📝 Derniers Commits

### Dernier commit

```
(local) - feat(api): aspect interpretations v5 - backend & mobile ready
```

### 5 derniers commits

```
(local) - feat(api): aspect interpretations v5 - backend & mobile ready
b622f30 - docs(api): document app crash fix and DB setup for DEV_AUTH_BYPASS
d9f311f - fix(api): correct user_id type handling after UUID→INTEGER migration
996f62c - feat(api): auto-calculate transits when generating new lunar report
d5ceb3b - fix(api): accept integer user_id in transits overview endpoint
```

### Commits Sprint 6 (Janvier 2026)

```
72c12a8 - feat(mobile): loading screen animé + régénération Claude Opus 4.5
21583f9 - feat(docs): guides déploiement production + monitoring complet
f741412 - feat(lunar): switch Opus/Sonnet configurable
786c682 - feat(scripts): ajouter script POC génération Claude
7ad78b5 - feat(lunar): activer Prompt Caching Anthropic (-90% coûts)
```

### Commits Sprint 7 (Janvier 2026)

```
b622f30 - docs(api): document app crash fix and DB setup for DEV_AUTH_BYPASS
d9f311f - fix(api): correct user_id type handling after UUID→INTEGER migration
996f62c - feat(api): auto-calculate transits when generating new lunar report
d5ceb3b - fix(api): accept integer user_id in transits overview endpoint
00702dc - fix(mobile): correct French typo 'Detail' → 'Détail' in waxing gibbous keywords
5ba7b4c - docs(mobile): add app screenshots for Opus 4.5 validation
33f3a58 - fix(api,mobile): corrections pré-publication Lunation v3.0 (T1+T3)
85486fa - fix(mobile): prioritize locale-relevant locations in onboarding autocomplete
9dbd501 - fix(mobile): pre-publication corrections for Lunation v3.0
```

### Commits Sprint 8 (Janvier 2026) - Refonte Aspects v5

```
(local) - feat(api): aspect interpretations v5 - backend & mobile ready
(local) - test(api): add 6 unit tests for aspect v5 parser (6/6 passing)
(local) - feat(mobile): add shadow section in AspectDetailSheet with amber warning
(local) - feat(api): add version parameter to aspect enrichment service
(local) - feat(scripts): add batch generation/validation/insertion scripts
```

---

## 📊 Timeline par Sprint

### Sprint 8 Timeline (En cours) 🔥

- **Début** : 30/01/2026 09h00
- **Status** : 🔄 **BACKEND & MOBILE READY** - En attente génération batches
- **Objectif** : Refonte 130 aspects prioritaires avec Claude Opus 4.5 (v4→v5)
- **Budget estimé** : $10-15 USD
- **Scope** : 10 batches (3 avec A/B test, 7 version A uniquement)

**Problème v4** :
- Textes identiques : "Symbiose puissante, intensité garantie" répété 3×
- Langage technique : "fusion fonctionnelle", "indissociation"
- Conseils non actionnables : "Observer les contextes où..."
- Note Claude Opus 4.5 : 8/20 qualité actuelle

**Réalisations** :
- ✅ Backend v5 complet (parser markdown + versioning + query param)
- ✅ Mobile v5 complet (interface TypeScript + section "Attention" amber warning)
- ✅ Scripts génération/validation/insertion (3 scripts Python)
- ✅ Tests unitaires : 6/6 passés ✨
- ✅ Infrastructure : `data/batches/`, `progress.json`
- ✅ Documentation : `ASPECT_REFONTE_V5.md`
- ⏳ Génération batches : 0/10 (prêt à lancer)

**Format v5** :
```
🌟 Brief (accroche émotionnelle 50-80 chars)
💡 Insight (explication simple, 2-3 phrases)
📋 Concret (3 bullet points vie réelle)
✨ Conseil (action actionnable, 1-2 phrases)
⚠️ Attention (piège à éviter, 1 phrase) ← NOUVEAU
```

**Fichiers modifiés** :
- Backend : `aspect_explanation_service.py`, `routes/natal.py`, `tests/test_aspect_explanation_v5.py`
- Mobile : `types/api.ts`, `components/AspectDetailSheet.tsx`
- Scripts : `generate_aspect_batch.py`, `validate_aspect_batch.py`, `insert_aspect_batch.py`

### Sprint 7 Timeline (Terminé) ✅

- **Début** : 29/01/2026
- **Fin** : 30/01/2026
- **Status** : ✅ **SPRINT 7 COMPLET** (Corrections pré-publication v3.0 + hotfixes)

**Réalisations Sprint 7** :
- Bottom sheet "Aujourd'hui" avec guidance lunaire
- Journal multi-entrées par jour
- Corrections pré-publication v3.0 (6 tickets P0/P1)
- Fix crash app (user_id UUID→INTEGER)
- Fix transits auto-calculés lors génération lunar report
- Fix typo français mobile

### Sprint 6 Timeline (Terminé) ✅

- **Début** : 24/01/2026 14h00 (vérification prérequis)
- **Fin** : 24/01/2026 17h30 (documentation production complète)
- **Durée** : ~3h30
- **Budget** : $0.20 (POC 10 générations)
- **Status** : ✅ **SPRINT 6 COMPLET** (Système génération Claude Opus 4.5 activé)

**Réalisations** :
- Activation génération Claude Opus 4.5 temps réel
- POC validation : 10/10 générations réussies (100%)
- Prompt Caching activé (-90% coûts)
- Monitoring Prometheus complet (6 métriques + 12 alertes)
- A/B test Opus vs Sonnet (décision : Opus 3× plus rapide)
- Loading screen mobile animé
- Tests conditions réelles activés

### Sprint 5 Timeline (Terminé) ✅

- **Début Sprint 5** : 23/01/2026 (Refonte architecture Lunar V1 → V2)
- **Sprint 0 - Foundation** : ✅ TERMINÉ
  - Création modèles LunarInterpretation + LunarInterpretationTemplate
  - Migrations Alembic créées et exécutées
  - Migration 1728 interprétations : pregenerated → lunar_interpretation_templates
  - Service lunar_interpretation_generator.py créé (500 LOC)
  - Documentation LUNAR_ARCHITECTURE_V2.md + MIGRATION_PLAN.md
  - Système coordination multi-agents opérationnel (.tasks/)

- **Vague 1 - Foundation** : ✅ TERMINÉE (3/3 agents terminés)
  - Agent A : Sprint 1 complet (scripts + tests + docs)
  - Agent B : Task 2.1 (generator enrichi - métriques, logs, retry, timeouts)
  - Agent C : Task 2.3 (legacy wrapper V1→V2)

- **Vague 2 - Service Layer** : ✅ TERMINÉE (3/3 agents terminés)
  - Agent A : Task 2.2 (refactor report_builder)
  - Agent B : Task 2.4 (tests generator - 33 tests, 88% coverage)
  - Agent C : Task 4.3 (audit migration - 1728/1728 validés)

- **Vague 3 - API Routes** : ✅ TERMINÉE (3/3 agents terminés)
  - Agent A : Task 3.1 (routes metadata V2)
  - Agent B : Task 3.2 (POST /regenerate)
  - Agent C : Task 3.3 (GET /metadata)

- **Vague 4 - Testing & QA** : ✅ COMPLÈTE (2/3 agents, 1 task reportée)
  - Agent A : Task 3.4 (tests E2E - 11 tests)
  - Agent B : Task 4.1 (tests intégration - 8 tests, 88% coverage)
  - Agent C : Task 4.2 reportée (benchmarks non-critique)

- **Vague 5 - Monitoring & Cleanup** : ✅ COMPLÈTE (3/3 agents terminés)
  - Agent A : Task 5.1 (endpoint /metrics Prometheus - 6 métriques)
  - Agent B : Task 5.2 (docs API_LUNAR_V2.md - 483 lignes)
  - Agent C : Task 5.3+5.4 (cleanup report + CLAUDE.md v5.14)

- **Status** : ✅ **SPRINT 5 TERMINÉ À 100%** 🎉

### Sprint 4 Timeline (Terminé) ✅

- **Début Sprint 4** : 23/01/2026 (Audit DB, identification combinaisons manquantes)

- **Phase 1 - Nettoyage** : ✅ TERMINÉ
  - Audit DB : 1550/1728 (89.7%) confirmé
  - Identification exacte 178 combinaisons manquantes
  - **Nettoyage massif** : 149 fichiers archivés
  - Documentation CLAUDE.md v4.0 mise à jour
  - Tests validés : 484/489 (98.9%)

- **Phase 2 - Génération finale** : ✅ TERMINÉ
  - Génération 178 interprétations directement avec Claude Opus 4.5
  - Insertion complète en DB avec upsert pattern (0 erreur)
  - Vérification finale : 1728/1728 (100%) ✅
  - Commit feat(api) 2af540c

- **Status** : ✅ **SPRINT 4 COMPLET** (Migration V2 100%, ready production)

### Sprint 3 Timeline (Terminé) ✅

- **Début Sprint 3** : 23/01/2026 (Audit état DB, correction documentation)
- **Réalisations** : Génération Gemini complet (144), insertion Pisces (38), Scorpio (72)
- **Fin Sprint 3** : 1550/1728 interprétations (89%), 10/12 signes complets
- **Status** : ✅ **SPRINT 3 COMPLET** (Migration V2 89%, +1 signe)

### Sprint 2 Timeline (Terminé) ✅

- **Début Sprint 2** : Stabilisation backend, cache, auth
- **Mi-Sprint** : Migration Lunar V2, optimisations
- **Fin Sprint 2** : Optimisations performance Phase 1+2, tests 100% OK
- **Status** : ✅ **SPRINT 2 MVP+ COMPLET** (backend stable, optimisé, prêt prod)

---

## 🏗️ Décisions Architecturales Majeures

### 2026-01-24 : Activation Génération Claude Opus 4.5

**Décision** : Activer génération temps réel Claude Opus 4.5 en production

**Contexte** :
- POC validation : 10/10 générations réussies (100%)
- Durée moyenne : 9.94s/génération
- Coût : $0.020/génération (avec Prompt Caching)
- Qualité : Ton chaleureux, structure claire, conseils actionnables

**Alternatives considérées** :
- Sonnet 4.5 : -40% coût mais 3× plus lent (30s) et 3× plus verbeux
- Templates statiques uniquement : Pas de personnalisation

**Résultat** : ✅ Opus 4.5 en production + Prompt Caching (-90% coûts)

### 2026-01-23 : Architecture Lunaire V2

**Décision** : Refonte complète architecture Lunar V1 (statique) → V2 (temporelle)

**Contexte** :
- V1 : Templates statiques pré-générés (1728 fichiers JSON)
- Besoin : Génération à la volée personnalisée + fallbacks robustes

**Architecture V2 (4 couches)** :
1. Layer 1 : Faits astronomiques (immutables)
2. Layer 2 : Narration IA temporelle (régénérable)
3. Layer 3 : Cache application (court terme)
4. Layer 4 : Fallback templates (statiques)

**Résultat** : ✅ Migration 100% complète (1728 templates migrés)

### 2026-01-22 : RLS Supabase Désactivé

**Commit** : `e3531c8`

**Décision** : Désactiver Row Level Security (RLS) côté Supabase

**Contexte** :
- Auth gérée exclusivement par FastAPI (JWT)
- RLS Supabase redondant et complexe à maintenir
- Performance : -10% overhead queries

**Alternatives considérées** :
- RLS Supabase + JWT FastAPI : Redondance
- Auth Supabase uniquement : Moins de contrôle

**Résultat** : ✅ Auth JWT FastAPI only, RLS désactivé

### 2026-01-20 : Uniformisation user_id INTEGER

**Commit** : `4acca51`

**Décision** : Uniformiser `user_id` en INTEGER partout

**Contexte** :
- Incohérence types : UUID vs INTEGER
- Erreurs foreign key constraints
- Migrations complexes

**Résultat** : ✅ user_id INTEGER partout, 0 erreur FK

### 2026-01-18 : Cache Application 1h

**Commit** : `24e06a6`

**Décision** : Cache applicatif TTL 1h pour interprétations

**Contexte** :
- Réduction appels DB répétitifs
- Équilibre fraîcheur/performance

**Alternatives considérées** :
- Cache 24h : Trop long, données stalées
- Cache 15min : Trop court, peu d'impact performance

**Résultat** : ✅ TTL 1h, -40% query count

---

## 📦 Fichiers Majeurs Créés

### Sprint 6 (27 fichiers)

**Documentation Production** :
- `docs/DEPLOYMENT_PRODUCTION.md` (1,091 lignes)
- `monitoring/prometheus_alerts.yml` (287 lignes)
- `docs/AB_TESTING_GUIDE.md` (483 lignes)
- `docs/MCP_SECURE_SETUP.md`
- `GUIDE_TEST_MOBILE.md` (483 lignes)

**Scripts & Tools** :
- `scripts/test_claude_generation_poc.py` (156 lignes)
- `tools/run_ab_test_opus.sh`
- `tools/run_ab_test_sonnet.sh`
- `tools/run_ab_test_analyze.sh`
- `tools/run.sh` (MCP server)
- `tools/mcp-server.js`

**Mobile** :
- `apps/mobile/components/LunarInterpretationLoader.tsx`

### Sprint 5 (15+ fichiers)

**Documentation** :
- `docs/LUNAR_ARCHITECTURE_V2.md`
- `docs/MIGRATION_PLAN.md`
- `docs/API_LUNAR_V2.md` (483 lignes)
- `docs/PROMETHEUS_METRICS.md` (322 lignes)
- `docs/MIGRATION_AUDIT_REPORT.md`

**Services** :
- `services/lunar_interpretation_generator.py` (700 LOC)
- `services/lunar_interpretation_legacy_wrapper.py` (181 LOC)

**Tests** :
- `tests/test_lunar_interpretation_generator.py` (710 LOC)
- `tests/test_lunar_interpretation_v2_model.py`
- `tests/test_lunar_interpretation_legacy_wrapper.py`
- `tests/test_lunar_routes_e2e.py`
- `tests/test_lunar_integration.py`
- `tests/test_metrics_endpoint.py`

**Scripts** :
- `scripts/audit_lunar_migration.py` (185 LOC)
- `scripts/agent_start.sh`
- `scripts/agent_complete.sh`
- `scripts/agent_heartbeat.sh`

### Sprint 4 (13 fichiers archivés)

**Batch files** (8 fichiers) :
- `batch_sprint4_pisces_m4.py`
- `batch_sprint4_pisces_m5.py`
- `batch_sprint4_pisces_m6_m7.py`
- `batch_sprint4_pisces_m8_m9.py`
- `batch_sprint4_pisces_m10_m11_m12.py`
- `batch_sprint4_scorpio_m7_m8.py`
- `batch_sprint4_scorpio_m9_m10.py`
- `batch_sprint4_scorpio_m11_m12.py`

**Scripts insertion** (5 fichiers) :
- `insert_sprint4_pisces_m8_m9.py`
- `insert_sprint4_pisces_m10_m11_m12.py`
- `insert_sprint4_scorpio_m7_m8.py`
- `insert_sprint4_scorpio_m9_m10.py`
- `insert_sprint4_scorpio_m11_m12.py`

---

## 📈 Métriques d'Évolution

### Tests

| Sprint | Passed | Failed | Skipped | Coverage |
|--------|--------|--------|---------|----------|
| Sprint 2 | 476 | 0 | 14 | N/A |
| Sprint 3 | 484 | 5 | 25 | N/A |
| Sprint 4 | 484 | 5 | 25 | 98.9% |
| Sprint 5 | 537 | 0 | 33 | 88% (generator) |
| Sprint 6 | 559 | 0 | 33 | 88% (generator) |

### Interprétations Lunaires DB

| Sprint | Count | Complétude | Signes complets |
|--------|-------|------------|-----------------|
| Sprint 2 | 1440 | 83% | 10/12 |
| Sprint 3 | 1550 | 89% | 10/12 |
| Sprint 4 | 1728 | 100% | 12/12 |
| Sprint 5 | 1728 | 100% | 12/12 |
| Sprint 6 | 1728 + cache temporelle | 100% | 12/12 |

### Performance

| Métrique | Avant (Sprint 1) | Après (Sprint 2+) | Amélioration |
|----------|------------------|-------------------|--------------|
| API calls RapidAPI | 100% | 40-60% | -40-60% |
| Query time DB | 100% | 75-90% | -10-25% |
| Query count | 100% | 50-70% | -30-50% |
| **Total** | 100% | **25-65%** | **35-75%** |

### Coûts Génération IA (Sprint 6)

| Scénario | Sans Prompt Caching | Avec Prompt Caching | Économie |
|----------|---------------------|---------------------|----------|
| 10 générations | $0.20 | $0.02 | **-90%** |
| 100 générations | $2.00 | $0.20 | **-90%** |
| 1,000 users/mois | $20.00 | $2.00 | **-90%** |

---

**Dernière mise à jour** : 2026-01-24
