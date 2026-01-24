# Checklist Déploiement Production - Astroia Lunar

**Date création** : 2026-01-24
**Version** : 1.0
**Statut système** : ✅ Sprint 6 terminé - Prêt pour production

---

## ⚠️ État Actuel

**Configuration (development)** :
- ✅ LUNAR_LLM_MODE: `anthropic`
- ✅ LUNAR_CLAUDE_MODEL: `opus`
- ✅ LUNAR_INTERPRETATION_VERSION: `2`
- ✅ ANTHROPIC_API_KEY: configured
- ⚠️ APP_ENV: `development` → À changer en `production`
- ⚠️ DEV_AUTH_BYPASS: `True` → **CRITIQUE** - À changer en `False`

**Validations** :
- ✅ 59 tests passent (35 unitaires + 24 E2E)
- ✅ POC réussi : 10/10 générations Claude Opus 4.5
- ✅ Prompt Caching activé (-90% coûts)
- ✅ Templates DB : 1,728 disponibles (à vérifier en production)

---

## Phase 1 : Préparation (J-7) 📋

### 1.1 Backup Base de Données

```bash
# Backup complet PostgreSQL Supabase
pg_dump $DATABASE_URL > backup_pre_deployment_$(date +%Y%m%d_%H%M%S).sql

# Vérifier taille backup
ls -lh backup_pre_deployment_*.sql
```

**Checklist** :
- [ ] Backup créé et sauvegardé localement
- [ ] Backup uploadé vers stockage cloud (AWS S3, GCS, etc.)
- [ ] Vérifier backup restaurable : `pg_restore --list backup_*.sql`

### 1.2 Tests Complets

```bash
cd /Users/remibeaurain/astroia/astroia-lunar/apps/api

# Run tous les tests
pytest -v

# Vérifier résultat
# Expected: 59 tests passent (484 passed si tous les tests backend)
```

**Checklist** :
- [ ] Tests unitaires : 35+ passent
- [ ] Tests E2E : 24+ passent
- [ ] Aucun test critique failing
- [ ] Coverage ≥ 70% sur services critiques

### 1.3 Validation Anthropic API

```bash
# Tester génération manuelle (1 appel)
python3 scripts/test_claude_generation_poc.py --count 1

# Vérifier coût Anthropic dashboard
# URL: https://console.anthropic.com/settings/cost
```

**Checklist** :
- [ ] Génération réussie (source='claude')
- [ ] Modèle utilisé : `claude-opus-4-5-20251101`
- [ ] Prompt Caching détecté (coût ~$0.002 au lieu de $0.020)
- [ ] Anthropic API Key valide et quota OK

### 1.4 Review Code Sécurité

```bash
# Vérifier aucun secret hardcodé
grep -r "sk-ant-" apps/api/ --include="*.py" || echo "✅ Aucun secret trouvé"
grep -r "ANTHROPIC_API_KEY.*=" apps/api/ --include="*.py" | grep -v "settings\." || echo "✅ OK"

# Vérifier .gitignore
cat .gitignore | grep -E "(.env$|*.key|secrets)" || echo "⚠️ Ajouter .env au .gitignore"
```

**Checklist** :
- [ ] Aucun secret hardcodé dans le code
- [ ] `.env` dans `.gitignore`
- [ ] Aucun fichier sensible tracké par git

### 1.5 Documentation Mise à Jour

**Checklist** :
- [ ] `CLAUDE.md` à jour (version 6.0)
- [ ] `DEPLOYMENT_PRODUCTION.md` lu et compris
- [ ] `AB_TESTING_GUIDE.md` disponible
- [ ] `PROMETHEUS_METRICS.md` disponible

---

## Phase 2 : Configuration Production (J-1) ⚙️

### 2.1 Variables d'Environnement

**Fichier `.env` production** :

```bash
# ===========================================
# GÉNÉRATION LUNAIRE - PRODUCTION
# ===========================================

# MODE GÉNÉRATION (CRITICAL)
LUNAR_LLM_MODE=anthropic           # ✅ Déjà configuré
LUNAR_INTERPRETATION_VERSION=2     # ✅ Déjà configuré

# ANTHROPIC API
ANTHROPIC_API_KEY=sk-ant-...       # ✅ Déjà configuré
LUNAR_CLAUDE_MODEL=opus            # ✅ Déjà configuré (ou sonnet pour tests A/B)

# DATABASE
DATABASE_URL=postgresql+asyncpg://user:pass@host:5432/astroia_lunar
DATABASE_POOL_SIZE=20              # Augmenter pour production
DATABASE_MAX_OVERFLOW=10           # Max overflow connections

# MONITORING ⚠️ À MODIFIER
APP_ENV=production                 # ⚠️ CHANGER de 'development' à 'production'
API_HOST=0.0.0.0
API_PORT=8000

# SÉCURITÉ ⚠️ CRITICAL
SECRET_KEY=<your-production-secret-key>  # ⚠️ Générer nouveau: openssl rand -hex 32
DEV_AUTH_BYPASS=0                        # ⚠️ CRITICAL: CHANGER de 'True' à '0' ou 'false'
```

**Actions** :

```bash
# Générer nouveau SECRET_KEY pour production
openssl rand -hex 32

# Éditer .env sur serveur production
# Modifier APP_ENV=production
# Modifier DEV_AUTH_BYPASS=0
# Copier nouveau SECRET_KEY
```

**Checklist** :
- [ ] `APP_ENV=production` ✅
- [ ] `DEV_AUTH_BYPASS=0` ou `false` ⚠️ **CRITICAL**
- [ ] `SECRET_KEY` régénéré (différent de dev)
- [ ] `DATABASE_POOL_SIZE=20` (production)
- [ ] Toutes les variables validées

### 2.2 Migrations Base de Données

```bash
cd /Users/remibeaurain/astroia/astroia-lunar/apps/api

# Vérifier état actuel
alembic current

# Lister migrations pending
alembic history

# Appliquer migrations
alembic upgrade head
```

**Checklist** :
- [ ] État migrations vérifié
- [ ] Migrations appliquées : `alembic upgrade head`
- [ ] Aucune erreur migration

### 2.3 Vérification Templates DB

```sql
-- Connexion à PostgreSQL Supabase production
psql $DATABASE_URL

-- Vérifier templates disponibles
SELECT COUNT(*) FROM lunar_interpretation_templates;
-- Expected: 1728

-- Vérifier distribution par signe
SELECT moon_sign, COUNT(*) as count
FROM lunar_interpretation_templates
GROUP BY moon_sign
ORDER BY moon_sign;
-- Expected: 12 signes × 144 combinaisons chacun

-- Vérifier indexes
SELECT schemaname, tablename, indexname
FROM pg_indexes
WHERE tablename IN ('lunar_interpretations', 'lunar_interpretation_templates');

-- Vérifier UNIQUE constraint
SELECT conname, contype
FROM pg_constraint
WHERE conrelid = 'lunar_interpretations'::regclass
  AND contype = 'u';
-- Expected: lunar_interpretations_lunar_return_id_subject_version_lang_key
```

**Checklist** :
- [ ] 1,728 templates présents
- [ ] 12 signes avec 144 combinaisons chacun
- [ ] Indexes présents et fonctionnels
- [ ] UNIQUE constraint actif

### 2.4 Configuration Prometheus & Alertes

```bash
# Copier fichier alertes vers serveur Prometheus
scp monitoring/prometheus_alerts.yml user@prometheus-server:/etc/prometheus/rules/

# Recharger configuration Prometheus
curl -X POST http://prometheus-server:9090/-/reload
```

**Vérifier alertes configurées** :
```bash
# Liste des 12 alertes
curl http://prometheus-server:9090/api/v1/rules | jq '.data.groups[0].rules[] | .alert'
```

**Checklist** :
- [ ] `prometheus_alerts.yml` copié vers serveur
- [ ] Prometheus rechargé
- [ ] 12 alertes détectées :
  - [ ] LunarGenerationCostHigh/Critical
  - [ ] LunarGenerationFallbackHigh/Critical
  - [ ] LunarGenerationLatencyHigh/Critical
  - [ ] LunarCacheHitRateLow
  - [ ] LunarGenerationStuck/NoActivity
  - [ ] LunarTemplateFallbackSpike
- [ ] 6 recording rules actifs

---

## Phase 3 : Déploiement (J-Day) 🚀

### 3.1 Deploy Backend

```bash
# Sur serveur production
cd /path/to/astroia-lunar/apps/api

# Pull dernières modifications
git pull origin main

# Installer dépendances
pip install -r requirements.txt

# Appliquer migrations
alembic upgrade head

# Redémarrer API
# Option 1: systemd
sudo systemctl restart astroia-api

# Option 2: manual
pkill -f "uvicorn main:app"
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4 &
```

**Checklist** :
- [ ] Code à jour (git pull)
- [ ] Dépendances installées
- [ ] Migrations appliquées
- [ ] API redémarrée
- [ ] Process running : `ps aux | grep uvicorn`

### 3.2 Smoke Tests

**Health Check** :
```bash
curl https://api.astroia.com/health
# Expected: {"status":"healthy","checks":{"database":"configured","rapidapi_config":"configured"}}
```

**Metrics Endpoint** :
```bash
curl https://api.astroia.com/metrics | grep lunar_
# Expected: 6 métriques lunaires
# - lunar_interpretation_generated_total
# - lunar_interpretation_cache_hit_total
# - lunar_interpretation_fallback_total
# - lunar_interpretation_duration_seconds
# - lunar_active_generations
# - lunar_migration_info
```

**Génération Test (1 user)** :
```bash
# Obtenir JWT token test
curl -X POST https://api.astroia.com/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"test@astroia.com","password":"test123"}'

# Tester génération lunaire
curl -X POST https://api.astroia.com/api/lunar-returns/current \
  -H "Authorization: Bearer $JWT" \
  | jq '.metadata'

# Expected:
# {
#   "source": "claude",
#   "model_used": "claude-opus-4-5-20251101",
#   "version": 2,
#   "generated_at": "2026-01-24T..."
# }
```

**Checklist** :
- [ ] `/health` retourne 200 OK
- [ ] `/metrics` expose 6 métriques lunaires
- [ ] Génération test réussie (source='claude')
- [ ] Metadata complètes présentes

### 3.3 Monitoring Logs (30 minutes)

```bash
# Suivre logs en temps réel
tail -f /var/log/api.log | grep lunar_interpretation

# Filtrer erreurs uniquement
tail -f /var/log/api.log | grep -E "(ERROR|CRITICAL)"
```

**Vérifier logs structurés** :
```json
{
  "event": "lunar_interpretation_generation_started",
  "user_id": 1,
  "lunar_return_id": 123,
  "lang": "fr",
  "timestamp": "2026-01-24T14:30:00Z"
}
{
  "event": "lunar_interpretation_generated",
  "source": "claude",
  "model_used": "claude-opus-4-5-20251101",
  "duration_ms": 11421,
  "timestamp": "2026-01-24T14:30:11Z"
}
```

**Checklist** :
- [ ] Aucune erreur pendant 30 minutes
- [ ] Logs structurés JSON formatés
- [ ] Générations Claude réussies
- [ ] Aucun fallback inattendu

### 3.4 Vérification Coûts (1ère heure)

```bash
# Anthropic Dashboard
# URL: https://console.anthropic.com/settings/cost

# Prometheus query
curl -G http://prometheus:9090/api/v1/query \
  --data-urlencode 'query=sum(increase(lunar_interpretation_generated_total{source="claude"}[1h])) * 0.002'
```

**Checklist** :
- [ ] Coût 1ère heure < $1 (pour <50 users)
- [ ] Prompt Caching détecté (coût ~$0.002/génération)
- [ ] Aucune anomalie de facturation

---

## Phase 4 : Validation Post-Déploiement (J+1) ✅

### 4.1 Métriques 24h

**Cache Hit Rate** :
```promql
sum(rate(lunar_interpretation_cache_hit_total[24h])) /
sum(rate(lunar_interpretation_generated_total[24h])) * 100
```
**Target** : >0% (augmente progressivement)

**Coût Quotidien** :
```promql
sum(increase(lunar_interpretation_generated_total{source="claude"}[24h])) * 0.002
```
**Target** : <$5 pour <500 users

**Taux Fallback** :
```promql
sum(rate(lunar_interpretation_fallback_total[24h])) /
sum(rate(lunar_interpretation_generated_total[24h])) * 100
```
**Target** : <5%

**P95 Latence** :
```promql
histogram_quantile(0.95,
  rate(lunar_interpretation_duration_seconds_bucket{source="claude"}[24h])
)
```
**Target** : <15s

**Checklist** :
- [ ] Cache hit rate >0% (et augmente)
- [ ] Coût quotidien <$5 (pour <500 users)
- [ ] Taux erreur/fallback <5%
- [ ] P95 latence <15s
- [ ] Aucune alerte Prometheus critique

### 4.2 User Feedback

**Checklist** :
- [ ] Aucune plainte qualité interprétations
- [ ] Aucun bug signalé
- [ ] Temps de réponse acceptable (<15s)
- [ ] User satisfaction positive

### 4.3 Rapport Validation

**Créer rapport** :
```markdown
# Rapport Validation Déploiement Production

**Date** : 2026-01-XX
**Durée monitoring** : 24h

## Métriques
- Générations totales : XXX
- Cache hit rate : XX%
- Coût total : $X.XX
- P95 latence : XXs
- Taux fallback : XX%

## User Feedback
- Satisfaction : X/5
- Bugs signalés : X
- Commentaires : [résumé]

## Statut Final
✅ Déploiement VALIDÉ - Production stable

## Actions Suivantes
1. [ ] Monitoring continu
2. [ ] Tests A/B Opus vs Sonnet (semaine 2)
3. [ ] Optimisations si nécessaire
```

**Checklist** :
- [ ] Rapport créé et partagé avec équipe
- [ ] Déploiement validé ✅
- [ ] Documentation CLAUDE.md mise à jour

---

## 🚨 Rollback Plan

### Si problème détecté

**Scénario 1 : Coût trop élevé (>$50/jour)**
```bash
# Désactiver génération Claude immédiatement
# Sur serveur production
sed -i 's/LUNAR_LLM_MODE=anthropic/LUNAR_LLM_MODE=off/' .env
sudo systemctl restart astroia-api

# Vérifier fallback vers templates
curl /api/lunar-returns/current | jq '.metadata.source'
# Expected: "db_template"
```

**Scénario 2 : Erreurs massives**
```bash
# Rollback code
git revert HEAD
git push origin main

# Redeploy
git pull origin main
sudo systemctl restart astroia-api
```

**Scénario 3 : Restaurer DB**
```bash
# Restaurer backup
pg_restore -d $DATABASE_URL backup_pre_deployment_*.sql
```

---

## 📊 Success Criteria

**Déploiement validé si** :
- ✅ 0 downtime
- ✅ >100 générations Claude réussies (24h)
- ✅ Cache hit rate >10% (et augmente)
- ✅ Coût <$5/jour
- ✅ Taux erreur <5%
- ✅ P95 latency <15s
- ✅ User feedback positif
- ✅ Aucune alerte critique Prometheus

**🎉 Si tous les critères validés → Déploiement RÉUSSI**

---

## 📞 Support & Contacts

**Erreurs Claude API** :
- Support Anthropic : support@anthropic.com
- Status page : https://status.anthropic.com

**Monitoring** :
- Prometheus : http://prometheus-server:9090
- Grafana : http://grafana-server:3000
- Anthropic Dashboard : https://console.anthropic.com

**Documentation** :
- Guide déploiement : `docs/DEPLOYMENT_PRODUCTION.md`
- Guide A/B testing : `docs/AB_TESTING_GUIDE.md`
- Métriques Prometheus : `docs/PROMETHEUS_METRICS.md`
- Alertes : `monitoring/prometheus_alerts.yml`

---

**Dernière mise à jour** : 2026-01-24
**Créé par** : Claude Opus 4.5
**Version** : 1.0
