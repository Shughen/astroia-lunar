# Astroia Lunar – Guide Claude Code

## 🎯 TL;DR

- **Projet** : Astrologie lunaire mobile (FastAPI + React Native)
- **Phase** : Sprint 6 TERMINÉ - Production ready 🎉
- **Stack** : FastAPI + Expo + PostgreSQL (Supabase) + Claude Opus 4.5 + RapidAPI
- **Monorepo** : `apps/api` (backend) + `apps/mobile` (frontend)
- **État** : 100% production ready, 59 tests validés, génération IA activée

---

## 🏗️ Architecture Logique

### Backend (`apps/api`)

- **10 routes API** : auth, natal, lunar, transits, journal
- **28 services** : génération IA, cache, RapidAPI integration
- **PostgreSQL Supabase** : Migrations Alembic, RLS désactivé (JWT FastAPI)
- **Génération Claude Opus 4.5** : Temps réel avec fallbacks 4 niveaux
- **Monitoring Prometheus** : 6 métriques + 12 alertes

### Mobile (`apps/mobile`)

- **Expo ~54**, React Native 0.81, Expo Router v6
- **Zustand** (state) + **SWR** (data fetching) + **Axios** (HTTP)
- **i18n** FR/EN support
- **Écrans** : Home, Lunar report, Natal chart, Transits, Journal

### Intégrations Externes

- **Anthropic Claude** : Interprétations natal + lunar (Opus 4.5)
- **RapidAPI** : Calculs astrologiques (natal chart, lunar returns, transits, VoC)
- **Supabase** : PostgreSQL (RLS off, JWT FastAPI auth)

---

## ⚠️ Règles NON Négociables

### 🔐 Sécurité & Exécution

- ✅ **AUTORISÉ** : Uniquement scripts `tools/*.sh` (allowlist MCP)
- ❌ **INTERDIT** : Commandes shell arbitraires, lire hors repo, modifier fichiers système

### 🚫 Zones Interdites

**JAMAIS modifier/commiter** :
- `.env`, `**/*.key`, `**/secrets*`
- `.claude/settings.json`, `.claude/settings.local.json`
- `apps/mobile/**` (sauf demande explicite)

**JAMAIS afficher** :
- `ANTHROPIC_API_KEY`, `RAPIDAPI_KEY`, `SUPABASE_KEY`, `SECRET_KEY`
- Tokens JWT, données utilisateurs

### 🔄 Workflow Git

- **Un changement = un commit** atomique
- **Toujours `pytest -q`** avant commit
- **Format commits** : `feat/fix/refactor/test/docs(api): message`

### 🎯 Zones de Travail

- ✅ `apps/api` : Modifier librement selon les règles
- ❌ `apps/mobile` : NE PAS toucher sauf demande explicite

---

## 🛠️ Commandes Essentielles

### Backend

```bash
cd apps/api

# Tests
pytest -q                                    # Run all tests (quick mode)
pytest tests/test_X.py -v                    # Run specific test (verbose)

# Run API
uvicorn main:app --reload --port 8000

# Migrations
alembic upgrade head                         # Apply pending migrations

# Health check
curl http://localhost:8000/health            # Expected: {"status":"ok"}
```

### Mobile

```bash
cd apps/mobile

npm start                                    # Start Expo dev server
npx tsc --noEmit                             # Check TypeScript errors
```

### Database

```bash
psql $DATABASE_URL                           # Connect to Supabase DB
psql $DATABASE_URL -c "SELECT COUNT(*) FROM lunar_interpretation_templates;"  # Verify migration (Expected: 1728)
```

---

## ✅ Definition of Done

### Backend

- `pytest -q` → 484+ passed (98.9%+)
- Health check → 200 OK
- Aucun secret affiché/commité
- Code respecte conventions (type hints, docstrings)

### Mobile

- App démarre sans crash
- **Aucun changement sauf demande explicite**

---

## 🔧 Command Dispatcher

Système de commandes locales dans `.claude/commands/` pour charger du contexte ciblé sans scanner le repo.

### Utilisation

```bash
./cmd <commande> [args...]     # Charge le contexte de la commande
./cmd list                      # Liste toutes les commandes disponibles
```

**Règle** : Après `./cmd`, suivre les instructions du fichier chargé. Ne jamais scanner le repo.

> **Approche BMAD-like** : Contexte ciblé + rôles spécialisés + contraintes = -90% tokens vs scan global.

### Commandes Disponibles

| Commande | Description |
|----------|-------------|
| `./cmd test` | Lancer les tests pytest |
| `./cmd commit` | Commit avec conventions projet |
| `./cmd health` | Vérifier santé système |
| `./cmd lunar:debug` | Debugger lunar returns |
| `./cmd lunar:context` | Charger architecture lunar |
| `./cmd lunar:generation` | Debugger génération Claude |
| `./cmd natal:debug` | Debugger natal charts |
| `./cmd natal:context` | Charger architecture natal |
| `./cmd api:route` | Créer nouvelle route FastAPI |
| `./cmd api:service` | Créer nouveau service |
| `./cmd db:migration` | Créer migration Alembic |
| `./cmd mobile:context` | Contexte mobile (read-only) |

### Exemples

```bash
./cmd lunar:debug timeout      # Debug timeouts Claude
./cmd api:route notifications  # Créer route notifications
./cmd test lunar               # Tests lunar uniquement
```

**Créer une commande** : voir `.claude/templates/command-template.md`

---

## 📚 Documentation Détaillée

**Architecture & Historique** :
- `apps/api/docs/ARCHITECTURE.md` — Architecture complète backend + mobile
- `apps/api/docs/SPRINTS_HISTORY.md` — Historique Sprints 2-6
- `apps/api/docs/CHANGELOG.md` — Historique commits

**Guides Pratiques** :
- `apps/api/docs/TROUBLESHOOTING.md` — Résolution problèmes courants
- `apps/api/docs/CONTRIBUTING.md` — Conventions et best practices

**Docs Techniques** :
- `apps/api/docs/LUNAR_ARCHITECTURE_V2.md` — Architecture V2 (4 couches)
- `apps/api/docs/API_LUNAR_V2.md` — API utilisateur V2
- `apps/api/docs/PROMETHEUS_METRICS.md` — Monitoring production
- `apps/api/docs/DEPLOYMENT_PRODUCTION.md` — Guide déploiement
- `apps/api/docs/AB_TESTING_GUIDE.md` — Méthodologie A/B testing

**Index complet** : `apps/api/docs/README.md`

---

## 📌 Fichiers Critiques

**Backend** :
- `config.py`, `main.py`, `database.py`
- `services/lunar_interpretation_generator.py` (V2 generator)
- `routes/*.py` (10 fichiers)

**Mobile** :
- `services/api.ts`, `stores/authStore.ts`
- `app/**/*.tsx`

**Docs** : `.claude/CLAUDE.md` (ce fichier)

---

## 📊 État Actuel

**Sprint 6** : ✅ **TERMINÉ** (24/01/2026)
- ✅ Génération Claude Opus 4.5 temps réel opérationnelle
- ✅ Prompt Caching activé (-90% coûts)
- ✅ Monitoring Prometheus complet (6 métriques + 12 alertes)
- ✅ Tests : 59 tests validés (35 unitaires + 24 E2E)
- ✅ A/B test Opus vs Sonnet (décision : Opus 3× plus rapide)
- ✅ Loading screen mobile animé
- ✅ **100% Production Ready** 🎯

**Derniers commits** :
```
b94b626 - fix(mobile): erreur width animation React Native + màj CLAUDE.md
72c12a8 - feat(mobile): loading screen animé + régénération Claude Opus 4.5
21583f9 - feat(docs): guides déploiement production + monitoring complet
f741412 - feat(lunar): switch Opus/Sonnet configurable
7ad78b5 - feat(lunar): activer Prompt Caching Anthropic (-90% coûts)
```

---

**Dernière màj** : 2026-01-24 | **Version** : 7.0 (refonte complète)
