# Guide Configuration Grafana - Astroia Lunar

**Date** : 2026-01-24
**Version** : 1.0
**Objectif** : Configurer monitoring visuel avec Grafana pour génération lunaire Claude Opus 4.5

---

## 📋 Prérequis

- ✅ Prometheus configuré et en cours d'exécution
- ✅ Alertes Prometheus importées (`prometheus_alerts.yml`)
- ✅ Endpoint `/metrics` API opérationnel
- ✅ Grafana installé (version 9.0+)

---

## 🚀 Installation Grafana (si nécessaire)

### Option 1 : Docker

```bash
docker run -d \
  --name=grafana \
  -p 3000:3000 \
  -e "GF_SECURITY_ADMIN_PASSWORD=admin" \
  grafana/grafana:latest
```

### Option 2 : Standalone (macOS)

```bash
brew install grafana
brew services start grafana
```

### Option 3 : Standalone (Linux)

```bash
# Ubuntu/Debian
sudo apt-get install -y grafana

# Start service
sudo systemctl start grafana-server
sudo systemctl enable grafana-server
```

**Vérifier installation** :
```bash
curl http://localhost:3000
# Expected: Grafana login page
```

---

## ⚙️ Configuration Prometheus Data Source

### Étape 1 : Se connecter à Grafana

1. Ouvrir navigateur : `http://localhost:3000`
2. Login par défaut :
   - Username: `admin`
   - Password: `admin` (changer au premier login)

### Étape 2 : Ajouter Prometheus comme source

1. **Menu** → **Configuration** → **Data Sources**
2. **Add data source** → **Prometheus**
3. Configurer :
   - **Name** : `Prometheus`
   - **URL** : `http://localhost:9090` (ou IP serveur Prometheus)
   - **Access** : `Server` (default)
   - **Scrape interval** : `15s`
4. **Save & Test** → Doit afficher "Data source is working"

---

## 📊 Import Dashboard Astroia Lunar

### Option 1 : Import via fichier JSON

1. **Menu** → **Dashboards** → **Import**
2. **Upload JSON file** → Sélectionner `monitoring/grafana_dashboard_lunar.json`
3. Configurer :
   - **Name** : `Astroia Lunar - Génération Claude Opus 4.5`
   - **Folder** : `Astroia` (créer si nécessaire)
   - **Prometheus** : Sélectionner data source créée précédemment
4. **Import**

### Option 2 : Import via copier-coller

1. **Menu** → **Dashboards** → **Import**
2. Copier contenu complet de `monitoring/grafana_dashboard_lunar.json`
3. **Load**
4. Configurer (idem Option 1)
5. **Import**

**Vérification** :
- Dashboard affiché avec 14 panels
- Aucune erreur "No data"
- Métriques apparaissent (si API en cours d'exécution)

---

## 📈 Description des Panels

### Row 1 : Vue d'ensemble temps réel

**Panel 1 - Générations par Source (Timeseries)**
- Affiche générations/minute par source (claude, db_temporal, db_template, hardcoded)
- Permet de voir rapidement quel fallback est utilisé
- **Seuils** : >50 req/min (yellow), >100 req/min (red)

**Panel 2 - Coût Quotidien (Stat)**
- Coût estimé dernières 24h (avec Prompt Caching -90%)
- **Seuils** : >$10/jour (yellow), >$50/jour (red, CRITICAL)

**Panel 3 - Cache Hit Rate (Gauge)**
- Pourcentage de générations servies depuis cache DB temporelle
- **Seuils** : <30% (red), 30-70% (yellow), >70% (green)

**Panel 4 - Fallback Rate (Gauge)**
- Pourcentage de générations utilisant fallbacks (templates/hardcoded)
- **Seuils** : <10% (green), 10-20% (yellow), 20-50% (orange), >50% (red)

**Panel 5 - P95 Latence (Gauge)**
- 95ème percentile de durée génération Claude
- **Seuils** : <15s (green), 15-30s (yellow), 30-45s (orange), >45s (red)

### Row 2 : Statistiques 24h

**Panel 6-9 - Compteurs 24h**
- Générations totales
- Générations Claude
- Cache hits
- Fallbacks

### Row 3 : Détails performance

**Panel 10 - Durée Génération (Timeseries)**
- P50, P95, P99 latence Claude
- Permet de détecter dégradations de performance

**Panel 11 - Coût Cumulé (Timeseries)**
- Coût horaire sur 24h (avec caching)
- Permet de tracker budget quotidien

### Row 4 : Diagnostics

**Panel 12 - Générations Actives (Timeseries)**
- Nombre de générations en cours
- **Alerte** : >10 simultanées (possible deadlock)

**Panel 13 - Répartition par Source (Pie Chart)**
- Distribution sources sur 24h
- Permet de voir rapidement si fallbacks dominants

**Panel 14 - Migration Info (Table)**
- Métadonnées migration V2 (version, templates_count, date, architecture)

---

## 🔔 Configuration Alertes Grafana

### Étape 1 : Configurer Notification Channel

1. **Menu** → **Alerting** → **Notification channels**
2. **Add channel**
3. Choisir type :
   - **Slack** : Webhook URL
   - **Email** : SMTP config
   - **PagerDuty** : Integration key
   - **Webhook** : Custom endpoint

Exemple Slack :
```json
{
  "name": "Slack - Astroia Alerts",
  "type": "slack",
  "settings": {
    "url": "https://hooks.slack.com/services/YOUR/WEBHOOK/URL",
    "recipient": "#alerts-prod"
  }
}
```

### Étape 2 : Importer Alertes depuis Prometheus

Les alertes sont déjà configurées dans Prometheus (`prometheus_alerts.yml`).

Grafana affichera automatiquement les alertes Prometheus actives via :
- **Annotations** : Alertes affichées sur les panels
- **Menu** → **Alerting** → **Alert Rules** : Liste complète

**12 Alertes configurées** :
1. LunarGenerationCostHigh/Critical
2. LunarGenerationFallbackHigh/Critical
3. LunarGenerationLatencyHigh/Critical
4. LunarCacheHitRateLow
5. LunarGenerationStuck
6. LunarGenerationNoActivity
7. LunarTemplateFallbackSpike

---

## 🔍 Queries PromQL Utiles

### Coût Total 24h (avec caching)
```promql
sum(increase(lunar_interpretation_generated_total{source="claude"}[24h])) * 0.002
```

### Cache Hit Rate (%)
```promql
(sum(rate(lunar_interpretation_cache_hit_total[5m])) /
sum(rate(lunar_interpretation_generated_total[5m]))) * 100
```

### P95 Latence Claude
```promql
histogram_quantile(0.95,
  rate(lunar_interpretation_duration_seconds_bucket{source="claude"}[5m])
)
```

### Générations par Modèle
```promql
sum by (model) (rate(lunar_interpretation_generated_total{source="claude"}[5m]))
```

### Fallback Rate (%)
```promql
(sum(rate(lunar_interpretation_fallback_total[5m])) /
sum(rate(lunar_interpretation_generated_total[5m]))) * 100
```

---

## 📱 Alertes Recommandées (Grafana)

En complément des alertes Prometheus, configurer alertes Grafana sur :

### Alerte 1 : Coût quotidien élevé

```
Panel: Coût Quotidien Estimé
Condition: WHEN last() OF query(A) IS ABOVE 10
Evaluate every: 5m
For: 10m
Notification: Slack - #alerts-prod
Message: Coût quotidien >$10 - Vérifier cache hit rate et fallback rate
```

### Alerte 2 : Latence critique

```
Panel: P95 Latence
Condition: WHEN last() OF query(A) IS ABOVE 30
Evaluate every: 5m
For: 5m
Notification: PagerDuty - On-call
Message: P95 latence >30s - Investiguer performance Claude API
```

### Alerte 3 : Cache hit rate faible

```
Panel: Cache Hit Rate
Condition: WHEN last() OF query(A) IS BELOW 20
Evaluate every: 15m
For: 2h
Notification: Slack - #alerts-prod
Message: Cache hit rate <20% sur 2h - Vérifier UNIQUE constraint et distribution users
```

---

## 🎨 Personnalisation Dashboard

### Ajouter un panel custom

1. **Dashboard** → **Add panel**
2. **Query** : Entrer PromQL query
3. **Visualization** : Choisir type (Graph, Stat, Gauge, etc.)
4. **Panel options** : Titre, description, seuils
5. **Save**

### Exemples de panels additionnels

**Générations par User (Top 10)** :
```promql
topk(10, sum by (user_id) (increase(lunar_interpretation_generated_total[24h])))
```

**Taux erreur Claude API** :
```promql
sum(rate(lunar_interpretation_fallback_total{type="api_error"}[5m])) /
sum(rate(lunar_interpretation_generated_total[5m])) * 100
```

**Économie Prompt Caching** :
```promql
sum(increase(lunar_interpretation_generated_total{source="claude"}[24h])) * 0.018
# 0.018 = économie par génération ($0.020 - $0.002)
```

---

## 🔄 Variables Dashboard

Ajouter variables pour filtrage dynamique :

### Variable 1 : Time Range

1. **Dashboard settings** → **Variables** → **Add variable**
2. **Type** : `Interval`
3. **Name** : `interval`
4. **Values** : `5m,15m,1h,6h,24h`
5. **Save**

Utiliser dans queries : `[${interval}]`

### Variable 2 : Model Filter

1. **Type** : `Query`
2. **Name** : `model`
3. **Query** : `label_values(lunar_interpretation_generated_total, model)`
4. **Multi-value** : Yes
5. **Include All** : Yes

Utiliser dans queries : `{model=~"$model"}`

---

## 📊 Export & Partage

### Export Dashboard JSON

1. **Dashboard settings** → **JSON Model**
2. **Copy to Clipboard**
3. Sauvegarder dans fichier local

### Créer Snapshot Public

1. **Dashboard** → **Share** → **Snapshot**
2. **Publish to snapshot.raintank.io** (Grafana Cloud)
3. **Expire** : 1 month
4. **Share URL** avec équipe

### Embed Dashboard

```html
<iframe
  src="http://grafana.astroia.com/d/lunar-generation/astroia-lunar?orgId=1&refresh=30s&kiosk"
  width="1200"
  height="800"
  frameborder="0">
</iframe>
```

---

## 🐛 Troubleshooting

### Problème : "No data" sur tous les panels

**Causes possibles** :
1. Prometheus data source mal configuré
2. API `/metrics` endpoint down
3. Métriques lunaires pas encore générées

**Solutions** :
```bash
# Vérifier Prometheus scrape
curl http://localhost:9090/api/v1/targets

# Vérifier métriques disponibles
curl http://localhost:9090/api/v1/label/__name__/values | grep lunar_

# Vérifier API /metrics
curl http://api.astroia.com/metrics | grep lunar_
```

### Problème : Dashboard ne s'affiche pas après import

**Causes possibles** :
1. JSON invalide
2. Prometheus data source name différent

**Solutions** :
1. Vérifier JSON valid : `jq . monitoring/grafana_dashboard_lunar.json`
2. Éditer dashboard → Change data source

### Problème : Alertes ne se déclenchent pas

**Causes possibles** :
1. Notification channel non configuré
2. Seuils jamais atteints
3. Évaluation trop courte

**Solutions** :
1. Test notification : **Notification channels** → **Test**
2. Ajuster seuils alertes
3. Augmenter "For" duration

---

## 📞 Support

**Grafana Documentation** :
- Docs officielles : https://grafana.com/docs/
- PromQL guide : https://prometheus.io/docs/prometheus/latest/querying/basics/

**Astroia Monitoring** :
- Dashboard JSON : `monitoring/grafana_dashboard_lunar.json`
- Alertes Prometheus : `monitoring/prometheus_alerts.yml`
- Métriques doc : `docs/PROMETHEUS_METRICS.md`

---

**Dernière mise à jour** : 2026-01-24
**Auteur** : Claude Opus 4.5
**Version** : 1.0
