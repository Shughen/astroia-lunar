# Migration PostgreSQL Local → Supabase

**Date** : 2026-01-24
**Status** : Draft - En attente d'exécution
**Impact** : Base de données complète (users, natal_charts, lunar_returns, etc.)

---

## 📋 Résumé Exécutif

**Objectif** : Migrer toutes les données de PostgreSQL local vers PostgreSQL hébergé sur Supabase

**État actuel** :
- ✅ Une seule base de données (pas de split)
- ✅ PostgreSQL local (localhost:5432)
- ✅ Toutes tables dans une DB unique

**État cible** :
- ✅ PostgreSQL Supabase (cloud hébergé)
- ✅ Même schéma (via Alembic migrations)
- ✅ Auth JWT FastAPI (RLS désactivé)

---

## ⚠️ Prérequis

### 1. Compte Supabase
- [ ] Créer un compte sur [supabase.com](https://supabase.com)
- [ ] Créer un nouveau projet Supabase
- [ ] Noter les credentials :
  - `SUPABASE_URL` : `https://xxxxx.supabase.co`
  - `SUPABASE_ANON_KEY` : Clé API publique (anon/public)
  - `DATABASE_URL` : Connection string PostgreSQL (Settings → Database → Connection String → URI)

### 2. Accès Base Locale
- [ ] PostgreSQL local accessible
- [ ] Credentials DATABASE_URL actuels valides
- [ ] Backup de la base locale créé

### 3. Outils Requis
```bash
# Vérifier installation
psql --version        # PostgreSQL client
pg_dump --version     # Backup tool
python3 --version     # Python 3.10+
pip show alembic      # Migration tool
```

---

## 📊 Inventaire des Données à Migrer

### Tables Core
```
users                                  (Authentification)
natal_charts                           (Thèmes nataux)
lunar_returns                          (Révolutions lunaires)
transits_overviews                     (Transits mensuels)
journal_entries                        (Journal utilisateur)
```

### Tables Interprétations
```
pregenerated_natal_interpretations     (Interprétations natales pré-générées)
lunar_interpretation_templates         (Templates lunaires - 1728 lignes)
lunar_interpretations                  (Interprétations lunaires V2)
natal_readings                         (Lectures natales complètes)
natal_aspect_interpretations           (Aspects enrichis)
```

### Tables Luna Pack
```
lunar_voc_windows                      (Void of Course cache)
lunar_mansions                         (Mansions cache)
lunar_reports                          (Rapports cache)
```

### Tables Alembic
```
alembic_version                        (Versions migrations)
```

**Total estimé** : ~15 tables

---

## 🔄 Stratégies de Migration

### Option 1 : Migration Schema + Data (Recommandée) ⭐

**Avantages** :
- ✅ Contrôle complet du processus
- ✅ Validation à chaque étape
- ✅ Rollback facile

**Étapes** :
1. Créer schéma sur Supabase via Alembic
2. Exporter données locales (pg_dump data-only)
3. Importer données vers Supabase
4. Valider intégrité

**Durée estimée** : 30-60 min

### Option 2 : pg_dump Full (Alternative)

**Avantages** :
- ✅ Simple et rapide
- ✅ Tout en une commande

**Inconvénients** :
- ⚠️ Moins de contrôle
- ⚠️ Difficile à rollback partiellement

---

## 🚀 Procédure de Migration (Option 1 - Recommandée)

### Phase 1 : Préparation (15 min)

#### 1.1 Backup Base Locale
```bash
cd apps/api

# Backup complet (schema + data)
pg_dump "$DATABASE_URL_LOCAL" > backups/backup_local_$(date +%Y%m%d_%H%M%S).sql

# Backup data-only (pour import Supabase)
pg_dump --data-only --no-owner --no-privileges \
  "$DATABASE_URL_LOCAL" > backups/data_only_$(date +%Y%m%d_%H%M%S).sql
```

#### 1.2 Créer Projet Supabase
1. Aller sur [app.supabase.com](https://app.supabase.com)
2. Créer nouveau projet
3. Attendre provisioning (2-3 min)
4. Copier credentials (Settings → Database → Connection String)

#### 1.3 Configuration .env
```bash
# Ajouter dans ../../.env (SANS remplacer DATABASE_URL encore)
SUPABASE_URL=https://xxxxx.supabase.co
SUPABASE_ANON_KEY=eyJhbGc...
DATABASE_URL_SUPABASE=postgresql://postgres:[PASSWORD]@db.xxxxx.supabase.co:5432/postgres
```

### Phase 2 : Création Schéma Supabase (10 min)

#### 2.1 Appliquer Migrations Alembic
```bash
cd apps/api

# Temporairement pointer vers Supabase
export DATABASE_URL="$DATABASE_URL_SUPABASE"

# Appliquer toutes les migrations
alembic upgrade head

# Vérifier version
alembic current
# Expected: 6b2c3d4e5f6a (head) ou la dernière version

# Vérifier tables créées
psql "$DATABASE_URL_SUPABASE" -c "\dt"
# Expected: ~15 tables listées
```

#### 2.2 Désactiver RLS (Important)
```bash
# Exécuter script de désactivation RLS
psql "$DATABASE_URL_SUPABASE" -f scripts/sql/rls_disable.sql

# Vérifier RLS désactivé
psql "$DATABASE_URL_SUPABASE" -c "
SELECT tablename, rowsecurity
FROM pg_tables
WHERE schemaname = 'public'
ORDER BY tablename;
"
# Expected: rowsecurity = false pour toutes tables
```

### Phase 3 : Migration Données (15 min)

#### 3.1 Export Données Locales
```bash
# Data-only dump (sans schema, sans owner)
pg_dump --data-only --no-owner --no-privileges \
  --exclude-table=alembic_version \
  "$DATABASE_URL_LOCAL" > backups/data_migration_$(date +%Y%m%d_%H%M%S).sql
```

#### 3.2 Import vers Supabase
```bash
# Import données
psql "$DATABASE_URL_SUPABASE" < backups/data_migration_YYYYMMDD_HHMMSS.sql

# Vérifier counts
psql "$DATABASE_URL_SUPABASE" -c "
SELECT
  'users' as table_name, COUNT(*) as count FROM users
UNION ALL
SELECT 'natal_charts', COUNT(*) FROM natal_charts
UNION ALL
SELECT 'lunar_returns', COUNT(*) FROM lunar_returns
UNION ALL
SELECT 'lunar_interpretation_templates', COUNT(*) FROM lunar_interpretation_templates
ORDER BY table_name;
"
```

### Phase 4 : Validation (10 min)

#### 4.1 Tests Intégrité
```bash
# Comparer counts local vs Supabase
./scripts/migration/compare_db_counts.sh

# Vérifier FK integrity
psql "$DATABASE_URL_SUPABASE" -c "
SELECT
  conrelid::regclass AS table_name,
  conname AS constraint_name,
  pg_get_constraintdef(oid) AS constraint_definition
FROM pg_constraint
WHERE contype = 'f'
ORDER BY conrelid::regclass::text;
"
```

#### 4.2 Test API
```bash
# Pointer temporairement vers Supabase
export DATABASE_URL="$DATABASE_URL_SUPABASE"

# Démarrer API
uvicorn main:app --reload --port 8000

# Tester endpoints critiques
curl http://localhost:8000/health
curl -H "Authorization: Bearer YOUR_TOKEN" http://localhost:8000/api/natal-chart
curl -H "Authorization: Bearer YOUR_TOKEN" http://localhost:8000/api/lunar-returns/current/report
```

#### 4.3 Run Tests
```bash
# Tests backend
pytest -q
# Expected: 537 passed, 33 skipped
```

### Phase 5 : Bascule Production (5 min)

#### 5.1 Mise à Jour .env
```bash
# Dans ../../.env
# Commenter l'ancienne DATABASE_URL
# DATABASE_URL=postgresql://postgres:password@localhost:5432/astroia_lunar

# Activer Supabase
DATABASE_URL=postgresql://postgres:[PASSWORD]@db.xxxxx.supabase.co:5432/postgres
```

#### 5.2 Redémarrer Services
```bash
# Redémarrer API
# L'API va maintenant utiliser Supabase

# Vérifier logs
tail -f logs/api.log | grep "Database URL"
# Expected: Database host: db.xxxxx.supabase.co
```

#### 5.3 Monitoring Post-Migration
- [ ] Vérifier logs API (pas d'erreurs DB)
- [ ] Tester login mobile
- [ ] Tester génération révolution lunaire
- [ ] Vérifier performance queries

---

## 🔙 Rollback

### Si Problème Détecté

#### Rollback Immédiat (2 min)
```bash
# Dans ../../.env
# Remettre DATABASE_URL locale
DATABASE_URL=postgresql://postgres:password@localhost:5432/astroia_lunar

# Redémarrer API
# L'API repasse sur base locale
```

#### Restaurer Backup (5 min)
```bash
# Si base locale corrompue
psql -c "DROP DATABASE IF EXISTS astroia_lunar;"
psql -c "CREATE DATABASE astroia_lunar;"
psql astroia_lunar < backups/backup_local_YYYYMMDD_HHMMSS.sql
```

---

## 📝 Checklist Post-Migration

### Validation Technique
- [ ] Tous les counts correspondent (local vs Supabase)
- [ ] FK integrity OK
- [ ] Tests pytest passent (537 passed)
- [ ] API démarre sans erreur
- [ ] Logs ne montrent pas d'erreurs DB

### Validation Fonctionnelle
- [ ] Login utilisateur OK
- [ ] Thème natal accessible
- [ ] Révolutions lunaires générées
- [ ] Transits chargés
- [ ] Journal utilisateur accessible
- [ ] VoC status OK

### Performance
- [ ] Latence API < 200ms (moyenne)
- [ ] Queries < 100ms (P95)
- [ ] Pas de N+1 queries

---

## 🚨 Troubleshooting

### Erreur : Connection refused
```bash
# Vérifier que Supabase est accessible
psql "$DATABASE_URL_SUPABASE" -c "SELECT 1;"

# Vérifier firewall/IP whitelist dans Supabase Settings
```

### Erreur : Foreign key violation
```bash
# Désactiver temporairement FK checks
psql "$DATABASE_URL_SUPABASE" -c "SET session_replication_role = 'replica';"

# Re-import
psql "$DATABASE_URL_SUPABASE" < backups/data_migration_*.sql

# Réactiver FK checks
psql "$DATABASE_URL_SUPABASE" -c "SET session_replication_role = 'origin';"
```

### Erreur : Duplicate key violation
```bash
# Truncate toutes tables avant re-import
psql "$DATABASE_URL_SUPABASE" -c "
TRUNCATE users, natal_charts, lunar_returns CASCADE;
"
```

---

## 📊 Timeline Estimée

| Phase | Durée | Total Cumulé |
|-------|-------|--------------|
| Phase 1: Préparation | 15 min | 15 min |
| Phase 2: Création Schéma | 10 min | 25 min |
| Phase 3: Migration Données | 15 min | 40 min |
| Phase 4: Validation | 10 min | 50 min |
| Phase 5: Bascule Prod | 5 min | **55 min** |

**Total** : ~1 heure

---

## 📚 Références

- [Supabase Database Docs](https://supabase.com/docs/guides/database)
- [Alembic Documentation](https://alembic.sqlalchemy.org/)
- [PostgreSQL pg_dump](https://www.postgresql.org/docs/current/app-pgdump.html)
- Decision RLS Désactivé: `archives/RLS_DECISION.md`

---

## ✅ Success Criteria

Migration réussie si **TOUS** les critères sont remplis :

1. ✅ Toutes tables créées sur Supabase (15 tables)
2. ✅ Counts identiques (local == Supabase)
3. ✅ Tests pytest passent (537 passed)
4. ✅ API démarre sans erreur
5. ✅ Mobile se connecte et charge données
6. ✅ Performance acceptable (< 200ms latence)
7. ✅ Backup local conservé et validé

---

**Prêt à migrer ?** Suivez les phases dans l'ordre. En cas de doute, contactez l'équipe avant Phase 5.

**Important** : Garder la base locale intacte pendant 7 jours après migration (période de validation).
