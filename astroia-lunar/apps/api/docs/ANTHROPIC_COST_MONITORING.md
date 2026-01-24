# Guide Monitoring Coûts Anthropic - Astroia Lunar

**Date** : 2026-01-24
**Version** : 1.0
**Objectif** : Surveiller et optimiser coûts génération Claude Opus 4.5

---

## 📋 Table des Matières

1. [Dashboard Anthropic Console](#dashboard-anthropic-console)
2. [Budget Alerts](#budget-alerts)
3. [Script Monitoring Automatique](#script-monitoring-automatique)
4. [Optimisations Coûts](#optimisations-coûts)
5. [Projection Budgétaire](#projection-budgétaire)

---

## 🎯 Dashboard Anthropic Console

### Accès Dashboard

**URL** : https://console.anthropic.com/settings/cost

**Login** :
1. Email : Compte Anthropic
2. API Organization : Sélectionner organisation

### Métriques Clés Affichées

#### 1. Current Month Spend
- **Utilité** : Dépenses mois en cours (temps réel)
- **Seuil recommandé** : Définir budget mensuel ($100-500 selon users)

#### 2. Usage by Model
- **Opus 4.5** : $X.XX (attendu : ~80-90% si mode par défaut)
- **Sonnet 4.5** : $X.XX (si tests A/B en cours)
- **Autres modèles** : Natal interpretations (Haiku/Sonnet)

#### 3. Prompt Caching Usage
- **Critical** : Doit afficher économie -90%
- **Vérifier** :
  - Cache writes : Nombre de prompts mis en cache
  - Cache reads : Nombre de hits cache
  - Savings : Économie totale ($)

#### 4. Daily Breakdown
- **Utilité** : Détection spikes anormaux
- **Pattern attendu** : Stable ou croissance linéaire (plus d'users)

---

## 🚨 Budget Alerts (Anthropic Console)

### Configuration Alertes

1. **Console** → **Settings** → **Usage & Billing**
2. **Set up budget alerts**

### Alertes Recommandées

#### Alerte 1 : Budget Quotidien

```
Type: Daily spending alert
Threshold: $5.00
Action: Email notification
Recipients: admin@astroia.com
```

**Justification** :
- Budget quotidien normal : $2-3/jour (1,000 users, Opus, caching)
- $5/jour = seuil warning (pic d'activité)

#### Alerte 2 : Budget Mensuel

```
Type: Monthly spending alert
Threshold: $100.00
Action: Email + Slack notification
Recipients: admin@astroia.com, #alerts-prod
```

**Justification** :
- Budget mensuel normal : $60-90/mois (1,000 users, Opus, caching)
- $100/mois = seuil warning (croissance users rapide)

#### Alerte 3 : Budget Critique

```
Type: Monthly spending alert
Threshold: $500.00
Action: Email + PagerDuty + Auto-disable API (via webhook)
Recipients: CTO, On-call engineer
```

**Justification** :
- $500/mois = seuil critique (anomalie ou boucle infinie)
- Auto-disable API pour éviter facture incontrôlée

---

## 🤖 Script Monitoring Automatique

### Installation

Le script `scripts/monitor_anthropic_cost.py` permet de :
- Récupérer coûts quotidiens/mensuels via API Anthropic
- Comparer avec métriques Prometheus (vérification cohérence)
- Alerter si dépassement seuils
- Générer rapport quotidien

### Prérequis

```bash
pip install anthropic python-dotenv requests
```

### Configuration

Ajouter à `.env` :

```bash
# Anthropic Cost Monitoring
ANTHROPIC_API_KEY=sk-ant-...  # Déjà configuré
ANTHROPIC_ORGANIZATION_ID=org_...  # Depuis console Anthropic
COST_ALERT_WEBHOOK=https://hooks.slack.com/services/YOUR/WEBHOOK  # Optionnel
COST_DAILY_THRESHOLD=5.0  # $5/jour
COST_MONTHLY_THRESHOLD=100.0  # $100/mois
```

### Exécution Manuelle

```bash
cd /Users/remibeaurain/astroia/astroia-lunar/apps/api

# Rapport quotidien
python scripts/monitor_anthropic_cost.py --daily

# Rapport mensuel
python scripts/monitor_anthropic_cost.py --monthly

# Export JSON
python scripts/monitor_anthropic_cost.py --export costs.json
```

### Automatisation (Cron)

**Setup cron job quotidien (9h AM)** :

```bash
crontab -e

# Ajouter ligne :
0 9 * * * cd /path/to/astroia-lunar/apps/api && python scripts/monitor_anthropic_cost.py --daily --alert
```

**Logs cron** :
```bash
tail -f /var/log/cron.log | grep anthropic_cost
```

---

## 💡 Optimisations Coûts

### Stratégie 1 : Maximiser Cache Hit Rate

**Objectif** : >70% cache hits après 1 semaine

**Actions** :
1. Vérifier UNIQUE constraint fonctionnel :
   ```sql
   SELECT conname FROM pg_constraint
   WHERE conrelid = 'lunar_interpretations'::regclass
     AND contype = 'u';
   ```

2. Éviter `force_regenerate=True` par défaut

3. Augmenter TTL cache si applicable (actuellement : pas de TTL, cache permanent)

**Impact** :
- Cache hit 0% : $2.00 pour 100 générations Opus
- Cache hit 70% : $0.60 pour 100 générations (économie 70%)

### Stratégie 2 : Tests A/B Opus → Sonnet

**Objectif** : -40% coûts sans perte qualité

**Process** :
1. Suivre `docs/AB_TESTING_GUIDE.md`
2. Générer 100 échantillons Sonnet : `python scripts/ab_test_generate_sample.py --model sonnet --count 100`
3. Analyser qualité : `python scripts/ab_test_analyze.py --sample 20`
4. Décision :
   - Si qualité ≥90% Opus → Switch Sonnet ✅
   - Sinon → Rester Opus ❌

**Impact** :
- Opus : $2.00/mois (1,000 users, caching)
- Sonnet : $1.20/mois (économie $0.80/mois = $9.60/an)
- **5,000 users** : Économie **$4,800/an**

### Stratégie 3 : Hybride Opus/Sonnet

**Objectif** : -20% coûts avec qualité optimale

**Configuration** :
```python
# Dans lunar_interpretation_generator.py
def get_configured_model(subject: str) -> str:
    """Hybrid strategy"""
    if subject == 'full':
        return CLAUDE_MODELS['opus']  # Qualité max pour interprétation complète
    else:
        return CLAUDE_MODELS['sonnet']  # Sonnet pour climate/focus/approach
```

**Impact** :
- Économie ~20-30% vs Opus pur
- Qualité préservée sur `subject='full'` (le plus important)

### Stratégie 4 : Prompt Optimization

**Déjà implémenté** : Prompt Caching (-90%)

**Optimisations additionnelles** :
1. Réduire longueur system message si possible (actuellement ~500 tokens)
2. Utiliser `max_tokens=2000` au lieu de valeur par défaut (économie mineure)

**Impact** :
- Déjà optimal avec Prompt Caching
- Optimisations mineures : <5% économie additionnelle

---

## 📊 Projection Budgétaire

### Hypothèses

- **Modèle** : Claude Opus 4.5
- **Coût/génération** : $0.002 (avec Prompt Caching -90%)
- **Générations/user/mois** : 1 (une consultation lunaire mensuelle)

### Scénario 1 : 1,000 Users Actifs

| Période | Générations | Coût Opus (caching) | Coût Sonnet (caching) | Économie |
|---------|-------------|---------------------|----------------------|----------|
| **Quotidien** | ~33 | $0.07 | $0.04 | $0.03 |
| **Hebdomadaire** | ~230 | $0.46 | $0.28 | $0.18 |
| **Mensuel** | 1,000 | $2.00 | $1.20 | $0.80 |
| **Annuel** | 12,000 | $24.00 | $14.40 | $9.60 |

### Scénario 2 : 5,000 Users Actifs

| Période | Générations | Coût Opus (caching) | Coût Sonnet (caching) | Économie |
|---------|-------------|---------------------|----------------------|----------|
| **Quotidien** | ~165 | $0.33 | $0.20 | $0.13 |
| **Hebdomadaire** | ~1,150 | $2.30 | $1.38 | $0.92 |
| **Mensuel** | 5,000 | $10.00 | $6.00 | $4.00 |
| **Annuel** | 60,000 | $120.00 | $72.00 | $48.00 |

### Scénario 3 : 10,000 Users Actifs (Scale)

| Période | Générations | Coût Opus (caching) | Coût Sonnet (caching) | Économie |
|---------|-------------|---------------------|----------------------|----------|
| **Quotidien** | ~330 | $0.66 | $0.40 | $0.26 |
| **Mensuel** | 10,000 | $20.00 | $12.00 | $8.00 |
| **Annuel** | 120,000 | $240.00 | $144.00 | $96.00 |

### Scénario 4 : Sans Prompt Caching (pour comparaison)

**Impact dramatique** :

| Users | Opus (sans caching) | Opus (avec caching) | Économie caching |
|-------|---------------------|---------------------|------------------|
| 1,000 | $240/an | $24/an | **$216/an (90%)** |
| 5,000 | $1,200/an | $120/an | **$1,080/an (90%)** |
| 10,000 | $2,400/an | $240/an | **$2,160/an (90%)** |

**Conclusion** : Prompt Caching est **critique** (économie 90%)

---

## 🎯 KPIs à Surveiller

### KPI 1 : Coût par User Actif

**Formule** :
```
Coût/user/mois = Coût total mensuel / Nombre users actifs
```

**Cible** :
- Opus (caching) : <$0.005/user/mois
- Sonnet (caching) : <$0.003/user/mois

**Alerte** : Si >$0.01/user/mois → Investiguer (cache hit rate faible?)

### KPI 2 : Taux Utilisation Prompt Caching

**Formule** :
```
Taux caching = Cache reads / (Cache writes + Cache reads) * 100
```

**Cible** : >80%

**Dashboard Anthropic** : Section "Prompt Caching Usage"

**Alerte** : Si <50% → Vérifier configuration system message avec `cache_control`

### KPI 3 : ROI Switch Sonnet

**Formule** :
```
ROI = (Économie annuelle - Coût tests A/B) / Coût tests A/B * 100
```

**Exemple** :
- Économie annuelle : $48/an (5K users)
- Coût tests A/B : $2.40 (200 générations test)
- ROI : 1,900%

**Décision** : Si ROI >500% → Switch Sonnet rentable

### KPI 4 : Coût vs Revenue

**Formule** :
```
Coût/Revenue ratio = Coût Anthropic mensuel / Revenue mensuel * 100
```

**Cible** : <5% (industrie SaaS standard)

**Exemple** :
- Revenue : $5,000/mois (1,000 users × $5/mois)
- Coût Anthropic : $20/mois (Opus, caching)
- Ratio : 0.4% ✅ Excellent

---

## 📈 Alertes & Actions

### Alerte : Coût quotidien >$5

**Gravité** : Warning

**Actions** :
1. Vérifier Prometheus metrics : Pic de générations ?
2. Vérifier cache hit rate : <50% ?
3. Vérifier force_regenerate : Utilisé abusivement ?
4. Investiguer logs : Boucle infinie ?

### Alerte : Coût mensuel >$100

**Gravité** : Critical

**Actions** :
1. **Immédiat** : Switch `LUNAR_LLM_MODE=off` (fallback templates)
2. Investiguer cause root (analytics, logs)
3. Considérer switch Opus → Sonnet temporairement
4. Contact Anthropic support si anomalie API

### Alerte : Prompt Caching <50%

**Gravité** : Warning

**Actions** :
1. Vérifier `cache_control: ephemeral` dans system message
2. Vérifier logs Anthropic dashboard "Prompt caching usage"
3. Contact Anthropic support si caching pas appliqué

---

## 🔗 Ressources

**Anthropic Documentation** :
- Pricing : https://www.anthropic.com/pricing
- Prompt Caching : https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching
- API Reference : https://docs.anthropic.com/en/api

**Astroia Monitoring** :
- Prometheus Metrics : `docs/PROMETHEUS_METRICS.md`
- Grafana Dashboard : `docs/GRAFANA_SETUP.md`
- A/B Testing Guide : `docs/AB_TESTING_GUIDE.md`

**Scripts** :
- Monitor costs : `scripts/monitor_anthropic_cost.py`
- A/B test generation : `scripts/ab_test_generate_sample.py`
- A/B test analysis : `scripts/ab_test_analyze.py`

---

## 📞 Support Anthropic

**Problèmes facturation** :
- Email : billing@anthropic.com
- Console : "Help" → "Contact support"

**Questions techniques** :
- Discord : https://discord.gg/anthropic
- Email : support@anthropic.com

**Vérifier status API** :
- Status page : https://status.anthropic.com

---

**Dernière mise à jour** : 2026-01-24
**Auteur** : Claude Opus 4.5
**Version** : 1.0
