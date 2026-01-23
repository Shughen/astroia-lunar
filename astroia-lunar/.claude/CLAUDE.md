# Astroia Lunar – Guide Claude Code

## 🎯 Vision & État Actuel

**Projet** : Application d'astrologie mobile spécialisée dans les cycles lunaires et thèmes natals
**Phase** : Sprint 2 MVP+ (stabilisation backend + optimisations)
**Stack** : FastAPI + Expo React Native + PostgreSQL (Supabase) + Anthropic Claude + RapidAPI
**Monorepo** : `apps/api` (backend) + `apps/mobile` (frontend React Native)

**Objectif** : Rendre l'astrologie lunaire accessible à tous avec calculs précis et interprétations IA de qualité.

---

## 📊 État du Sprint 2 (Janvier 2026)

### ✅ Terminé
- Cache application interprétations DB (TTL 1h, commit 24e06a6)
- Authentification JWT routes protégées (tests complets, commit aa7e725)
- Uniformisation `user_id` → INTEGER partout (commit 4acca51)
- Documentation décision RLS Supabase désactivé (commit e3531c8)
- Interprétations lunaires V2 (DB + IA Opus 4.5)
- Validation `SECRET_KEY` au démarrage (commit cd731ea)

### ⚠️ En cours
- **14 tests failing** : 9 VoC cache (async mocking), 2 greenlet errors, 3 autres
- Migration complète vers Lunar V2 (interprétations pré-générées)
- Optimisations frontend mobile

### 🎯 Prochaines priorités
1. Fixer tests VoC cache (async issues)
2. Résoudre greenlet errors (routes/lunar_returns.py)
3. Compléter couverture interprétations pré-générées (signes lunaires)

---

## 🏗️ Architecture Backend (`apps/api`)

### Routes principales (10 fichiers)
```
routes/
├── auth.py                          POST /api/auth/login, /register
├── natal.py                         POST /api/natal-chart (JWT+DEV)
├── natal_reading.py                 POST/GET /api/natal/reading (JWT+DEV)
├── natal_interpretation.py          POST /api/natal/interpretation (JWT)
├── natal_aspect_interpretation.py   POST /api/natal/aspects/enrich (JWT)
├── lunar_returns.py                 POST /api/lunar-returns/current (JWT+DEV)
├── lunar.py                         POST /api/reports/lunar/{month} (JWT)
├── reports.py                       POST /api/reports/lunar/{month} (JWT)
├── transits.py                      GET /api/transits/overview/{month} (JWT)
└── journal.py                       CRUD /api/journal/entries (JWT)
```

### Services critiques (27 fichiers)
```
services/
├── natal_interpretation_service.py   (1335 LOC) Anthropic integration
├── lunar_report_builder.py           (928 LOC) Reports V4 + V2 migration
├── interpretation_cache_service.py   (695 LOC) Cache applicatif
├── voc_cache_service.py              (467 LOC) VoC cache + retry logic
├── rapidapi_client.py                (317 LOC) Best Astrology API client
├── lunar_interpretation_service.py   Interprétations lunaires DB/IA
├── lunar_interpretation_v2_service.py V2 avec fallback templates
├── transits_service.py               Calculs transits
├── daily_climate_service.py          Ambiance journalière
└── ... (18 autres services)
```

### Modèles SQLAlchemy (12 fichiers)
```
models/
User (INTEGER PK)
├── NatalChart (UUID PK, FK user_id INTEGER)
├── LunarReturn (FK user_id INTEGER)
├── TransitsOverview (FK user_id INTEGER)
├── JournalEntry (FK user_id INTEGER)
├── LunarInterpretation (v1, fichiers JSON obsolètes)
├── LunarInterpretationV2 (v2, pré-générées en DB)
└── autres relations...
```

### Intégrations externes

**Anthropic Claude** (natal_interpretation_service.py)
- Modèles : Haiku (rapide), Sonnet (équilibré), Opus 4.5 (haute qualité)
- Usage : Interprétations natal + lunar (si `LUNAR_LLM_MODE=anthropic`)
- Config : `ANTHROPIC_API_KEY`, `NATAL_LLM_MODE=anthropic`

**RapidAPI Best Astrology API** (rapidapi_client.py)
- Endpoints : Natal chart, Lunar returns, Transits, VoC
- Fallback : Swiss Ephemeris local si échec RapidAPI
- Config : `RAPIDAPI_KEY`, retry logic avec exponential backoff

**Supabase PostgreSQL** (database.py)
- Auth désactivée côté Supabase (JWT FastAPI only)
- RLS désactivé (doc commit e3531c8)
- Config : `SUPABASE_URL`, `SUPABASE_KEY`, `SECRET_KEY`

### Configuration (.env)
```bash
# Versions et modes
LUNAR_INTERPRETATION_VERSION=2          # 1 (fichiers) | 2 (DB)
LUNAR_LLM_MODE=off                      # off (templates) | anthropic (Opus)
NATAL_LLM_MODE=anthropic                # anthropic only

# Auth & Dev
DEV_AUTH_BYPASS=true                    # Dev only: skip JWT on some routes
SECRET_KEY=your-secret-key-here         # JWT signing

# External services
ANTHROPIC_API_KEY=sk-ant-...
RAPIDAPI_KEY=...
SUPABASE_URL=https://....supabase.co
SUPABASE_KEY=eyJ...
DATABASE_URL=postgresql://...

# Caching
INTERPRETATION_CACHE_TTL=3600           # 1h cache interprétations
VOC_CACHE_TTL=3600                      # 1h cache VoC
```

---

## 📱 Architecture Mobile (`apps/mobile`)

### Écrans principaux
```
app/
├── index.tsx                        Home (guards + 5 widgets)
├── lunar/report.tsx                 Rapport lunaire V2
├── natal-chart/
│   ├── index.tsx                    Formulaire thème natal
│   └── result.tsx                   Affichage résultats
├── transits/
│   ├── overview.tsx                 Vue mensuelle transits
│   └── details.tsx                  Détails timing/themes/advice
├── journal/
│   ├── index.tsx                    Liste entrées
│   └── [id].tsx                     Détail entrée
├── settings.tsx                     Paramètres utilisateur
└── onboarding/*                     Welcome flow complet
```

### État intégration API
```
✅ Fonctionnel : Auth, Lunar returns, Natal chart, Transits overview, VoC, Journal
⚠️ En cours : Natal interpretations enrichies, Transits details (timing/themes/advice)
```

### Stack technique
```
- Expo ~54.0.30, React Native 0.81.5
- Expo Router v6 (file-based routing)
- Zustand (state management)
- SWR (data fetching + cache)
- Axios (HTTP client)
- TypeScript 5.9.2
- i18n (FR/EN support)
```

---

## ⚠️ Règles Strictes

### Sécurité & Secrets
- ❌ **JAMAIS** modifier `.env`
- ❌ **JAMAIS** afficher/commiter de secrets (API keys, tokens, passwords)
- ❌ **JAMAIS** logger des données utilisateurs réelles

### Workflow Git
- ✅ **Un changement = un commit** (atomicité)
- ✅ Commits clairs et descriptifs (feat/fix/refactor/test/docs)
- ✅ Toujours run `pytest -q` avant commit

### Priorités développement
1. Correctif minimal (fix the bug, don't refactor the world)
2. Tests (ensure it works)
3. Refacto (only if necessary)

### Zones de travail
- ✅ `apps/api` : Modifier librement selon les règles
- ❌ `apps/mobile` : **NE PAS toucher sauf demande explicite**

---

## 🛠️ Commandes Utiles

### Backend (`apps/api`)
```bash
cd apps/api

# Tests
pytest -q                                    # Run all tests (quick mode)
pytest tests/test_X.py -v                    # Run specific test (verbose)
pytest tests/test_X.py::test_func -v         # Run single test function
pytest --lf                                  # Re-run last failures

# Run API
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Database migrations
alembic upgrade head                         # Apply pending migrations
alembic revision --autogenerate -m "msg"     # Create new migration
alembic downgrade -1                         # Rollback last migration

# Scripts utilitaires
python scripts/generate_lunar_interpretations_v2.py
python scripts/insert_all_lunar_interpretations.py
python scripts/cleanup_bad_interpretations.py
```

### Mobile (`apps/mobile`)
```bash
cd apps/mobile

npm start                                    # Start Expo dev server
npm run ios                                  # iOS simulator
npm run android                              # Android emulator
npm run web                                  # Web browser

# Type checking
npx tsc --noEmit                             # Check TypeScript errors
```

### Database
```bash
# Connect to Supabase DB
psql $DATABASE_URL

# Quick queries
psql $DATABASE_URL -c "SELECT COUNT(*) FROM users;"
psql $DATABASE_URL -c "SELECT COUNT(*) FROM lunar_interpretations_v2;"
```

### Git
```bash
git log --oneline -10                        # Recent commits
git status                                   # Check working tree
git diff                                     # See unstaged changes
git diff --staged                            # See staged changes
```

---

## ✅ Definition of Done

### Backend
- ✅ `pytest -q` → 0 failures (actuellement 14 à corriger)
- ✅ `curl http://localhost:8000/health` → 200 OK
- ✅ `curl http://localhost:8000/api/natal/interpretation` (avec JWT) → 200 OK
- ✅ Aucun secret affiché/commité
- ✅ Tests auth OK
- ✅ Code respecte les conventions (type hints, docstrings sur fonctions publiques)

### Mobile
- ✅ App démarre sans crash
- ✅ Écrans principaux accessibles
- ✅ Intégration API fonctionnelle
- ✅ **Aucun changement sauf demande explicite**

### Documentation
- ✅ CLAUDE.md à jour (ce fichier)
- ✅ Commits clairs et atomiques
- ✅ README.md à jour si changements architecturaux

---

## 🚫 Zones Interdites

### JAMAIS modifier/commiter
```
.env
**/*.key
**/secrets*
.claude/settings.json
.claude/settings.local.json
apps/mobile/**  (sauf demande explicite)
```

### JAMAIS afficher
```
ANTHROPIC_API_KEY
RAPIDAPI_KEY
SUPABASE_KEY
SECRET_KEY
DATABASE_URL (si contient password)
Tokens JWT
Données utilisateurs réelles
```

---

## 📚 Références Rapides

### Fichiers critiques
```
apps/api/
├── config.py                                Configuration centralisée
├── main.py                                  Startup + health checks + CORS
├── database.py                              Connexion Supabase
├── services/natal_interpretation_service.py Anthropic integration
├── services/lunar_report_builder.py         Reports V4 + V2 migration
├── services/interpretation_cache_service.py Cache applicatif
└── routes/*.py                              10 fichiers routes

apps/mobile/
├── services/api.ts                          Client API (Axios + interceptors)
├── stores/authStore.ts                      Zustand auth state
└── app/**/*.tsx                             Écrans principaux
```

### Documentation importante
```
apps/api/README.md                           Quick start API
apps/api/docs/README.md                      Index docs techniques
apps/api/docs/PREGENERATED_INTERPRETATIONS_README.md  Interprétations DB
apps/api/docs/MIGRATION_PREGENERATED_TO_DB.md  Migration fichiers → DB
.claude/CLAUDE.md                            Ce fichier
```

### Architecture Decisions
```
- RLS Supabase désactivé (commit e3531c8) : Auth JWT FastAPI only
- user_id uniformisé INTEGER partout (commit 4acca51)
- Cache application 1h pour interprétations (commit 24e06a6)
- Lunar V2 : DB pre-generated + fallback templates (en migration)
```

---

## 🐛 Troubleshooting

### Problème : Tests VoC cache failing (9 tests)
```
Symptôme : AsyncMock issues, tests/test_voc_cache_service.py
Cause : Async mocking complexe avec retry logic
Solution : À investiguer, voir issue #XX
```

### Problème : Greenlet errors (2 tests)
```
Symptôme : greenlet_spawn errors dans routes/lunar_returns.py
Cause : Async context issues
Solution : À investiguer, possiblement lié à SQLAlchemy sessions
```

### Problème : Anthropic 401 Unauthorized
```
Symptôme : API Anthropic retourne 401
Causes possibles :
1. ANTHROPIC_API_KEY manquant/invalide dans .env
2. API key expirée
3. Quota dépassé
Solution : Vérifier .env, tester key avec curl direct
```

### Problème : Mobile ne se connecte pas à l'API
```
Symptôme : Network errors, timeout
Causes possibles :
1. API pas démarrée
2. API écoute sur localhost (pas 0.0.0.0)
3. API_URL incorrect dans mobile
Solution :
- Vérifier API sur http://localhost:8000/health
- Vérifier uvicorn --host 0.0.0.0
- Vérifier services/api.ts → baseURL
```

### Problème : Tests DB connection refused
```
Symptôme : psycopg2.OperationalError
Cause : Tests utilisent SQLite en mémoire, pas PostgreSQL
Solution : Laisser pytest auto-configurer, ne pas override DATABASE_URL
```

### Problème : Import errors (ModuleNotFoundError)
```
Symptôme : Can't import module X
Causes possibles :
1. Pas dans le bon répertoire
2. Dependencies pas installées
Solution :
- cd apps/api && pip install -r requirements.txt
- Vérifier PYTHONPATH si nécessaire
```

---

## 📖 Contexte Historique

### Dernier commit
```
24e06a6 - feat(api): ajouter cache application pour interprétations DB
```

### 5 derniers commits
```
24e06a6 - feat(api): cache application interprétations DB
aa7e725 - test(api): tests authentification routes protégées
e3531c8 - docs(api): documenter décision désactivation RLS Supabase
4acca51 - feat(api): uniformiser user_id transits (UUID → INTEGER)
cd731ea - feat(api): ajouter validation SECRET_KEY au démarrage
```

### Sprint 2 Timeline
- **Début Sprint 2** : Stabilisation backend, cache, auth
- **Mi-Sprint** : Migration Lunar V2, optimisations
- **Actuellement** : Correction tests, complétion interprétations
- **Objectif fin Sprint** : 0 tests failing, Lunar V2 complete

---

## 💡 Tips & Best Practices

### Quand travailler sur le backend
1. Toujours lire le fichier avant de le modifier (use Read tool)
2. Run tests après chaque changement (`pytest -q`)
3. Commit atomique avec message clair
4. Ne pas refactor pendant un fix (focus)

### Quand NE PAS toucher le mobile
- ❌ Sauf demande explicite de l'utilisateur
- ❌ Ne pas "améliorer" le code frontend spontanément
- ❌ Ne pas synchroniser API changes avec mobile automatiquement

### Conventions de commits
```
feat(api): ajouter endpoint X
fix(api): corriger bug Y dans service Z
test(api): ajouter tests pour X
refactor(api): simplifier service Y
docs(api): documenter decision Z
```

### Code style
- Type hints partout (Python 3.11+)
- Docstrings sur fonctions publiques
- Async/await pour I/O operations
- Exception handling avec logs clairs

---

## 🔄 Maintenance de ce fichier (pour Claude)

⚠️ **Instructions pour Claude Code** : Ce fichier doit rester à jour et refléter l'état actuel du projet.

### Triggers de mise à jour automatique

Claude doit **proactivement** mettre à jour CLAUDE.md quand :

1. **Fin de sprint ou milestone majeur**
   - Exemple : "Sprint 2 terminé" → Mettre à jour état, ajouter Sprint 3

2. **Changement architectural majeur**
   - Nouvelle route API, nouveau service critique
   - Nouvelle intégration externe (nouvelle API, nouveau service)
   - Changement modèle de données important

3. **État "tests failing" change significativement**
   - Exemple : "14 tests failing" → "0 tests failing"
   - Nouveau type d'erreur récurrent à ajouter au Troubleshooting

4. **Changement stack technique**
   - Upgrade majeur de dépendances (Expo, FastAPI, etc.)
   - Ajout/retrait de librairie importante

5. **Nouvelle zone interdite ou règle stricte**
   - Nouvelle contrainte de sécurité
   - Nouveau workflow obligatoire

### Sections à maintenir régulièrement

#### Toujours vérifier après un commit important :
- **"État du Sprint 2"** : Terminé/En cours/Priorités
- **"Contexte Historique"** : Derniers commits (garder 5 plus récents)
- **"Troubleshooting"** : Ajouter nouveaux problèmes résolus

#### Tous les 5-10 commits :
- Vérifier que l'architecture décrite correspond toujours à la réalité
- Mettre à jour les counts (routes, services, modèles si changés)
- Rafraîchir la timeline du sprint

### Workflow de mise à jour

Quand un trigger est détecté :

1. **Lire** CLAUDE.md actuel
2. **Identifier** les sections impactées
3. **Mettre à jour** uniquement ce qui a changé (pas de réécriture complète)
4. **Proposer** un commit séparé :
   ```
   docs(claude): mettre à jour CLAUDE.md [section concernée]
   ```

### Détection proactive

Claude doit être attentif aux signaux comme :
- "✅ Tous les tests passent maintenant" → Mettre à jour "14 tests failing"
- "J'ai ajouté une nouvelle route..." → Vérifier si liste routes à jour
- "Le sprint 2 est terminé" → Mettre à jour état + ajouter Sprint 3
- "On n'utilise plus RapidAPI" → Mettre à jour intégrations externes

### Format des mises à jour

- **Atomique** : Un type de changement = un commit CLAUDE.md
- **Concis** : Mettre à jour seulement ce qui change
- **Daté** : Mettre à jour "Dernière mise à jour" en bas du fichier

---

**Dernière mise à jour** : 2026-01-23
**Version** : 2.0 (contexte complet Sprint 2)
