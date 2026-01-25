# Lunar Debug Index

Index de référence rapide pour le debugging des lunar returns.
**Usage** : Évite de charger les fichiers source volumineux.

---

## Architecture 4 Couches (Fallback)

```
Request
   │
   ▼
┌──────────────────────────────────────────────────┐
│ 1. DB Cache (LunarInterpretation)                │
│    lunar_interpretation_generator.py:172-211     │
│    → Cache hit = retour immédiat                 │
└──────────────────────────────────────────────────┘
   │ miss
   ▼
┌──────────────────────────────────────────────────┐
│ 2. Claude Opus 4.5 (génération temps réel)       │
│    lunar_interpretation_generator.py:213-271     │
│    → Timeout: 30s, Retry: 3x (2s, 4s, 8s)        │
└──────────────────────────────────────────────────┘
   │ fail
   ▼
┌──────────────────────────────────────────────────┐
│ 3. DB Templates (LunarInterpretationTemplate)    │
│    lunar_interpretation_generator.py:289-322     │
│    → 1728 templates pré-générés                  │
└──────────────────────────────────────────────────┘
   │ miss
   ▼
┌──────────────────────────────────────────────────┐
│ 4. Templates Hardcodés (CLIMATE_TEMPLATES)       │
│    lunar_interpretation_generator.py:324-356     │
│    → Fallback ultime, contenu générique          │
└──────────────────────────────────────────────────┘
```

---

## Configuration Clés

| Variable | Fichier | Ligne | Valeurs |
|----------|---------|-------|---------|
| `LUNAR_LLM_MODE` | config.py | 92 | "off" (default) / "anthropic" |
| `LUNAR_CLAUDE_MODEL` | config.py | 94 | "opus" / "sonnet" / "haiku" |
| `LUNAR_INTERPRETATION_VERSION` | config.py | 93 | 2 (default) |
| Timeout Claude | generator.py | 445 | 30.0 secondes |
| Max retries | generator.py | 363 | 3 tentatives |

---

## Fonctions Critiques (avec lignes)

### lunar_interpretation_generator.py (707 lignes)

| Fonction | Lignes | Rôle |
|----------|--------|------|
| `generate_or_get_interpretation()` | 107-360 | Entry point principal |
| `_call_claude_with_retry()` | 362-386 | Appel Claude + retry |
| `_generate_via_claude()` | 389-460 | Génération IA |
| `_build_prompt()` | 503-590 | Construction prompt |
| `_get_template_fallback()` | 620-663 | Fallback DB templates |
| `_get_hardcoded_fallback()` | 666-706 | Fallback hardcodé |

### lunar_returns.py (1638 lignes)

| Route | Lignes | Rôle |
|-------|--------|------|
| `POST /generate` | 796-874 | Génère 12 mois rolling |
| `GET /current` | 903-1116 | Cycle en cours (lazy gen) |
| `GET /current/report` | 1119-1217 | Rapport mensuel |
| `GET /next` | 1294-1351 | Prochain retour |
| `_generate_rolling_if_empty()` | 517-793 | Auto-génération |

---

## Erreurs Courantes

### Timeout (30s)
```
Fichier: lunar_interpretation_generator.py:456-457
Log: "claude_timeout", timeout_seconds=30
Exception: ClaudeAPIError("Claude API timeout after 30s")
```

### Rate Limit
```
Fichier: lunar_interpretation_generator.py:458-460
Exception: RateLimitError (retry automatique 3x)
```

### Cache Miss + Claude Fail
```
Fichier: lunar_interpretation_generator.py:289
Log: "falling_back_to_db_template"
Métrique: lunar_interpretation_fallback_total{fallback_level="db_template"}
```

### Fallback Hardcodé
```
Fichier: lunar_interpretation_generator.py:325
Log: "falling_back_to_hardcoded_template"
Métrique: lunar_interpretation_fallback_total{fallback_level="hardcoded"}
```

---

## Métriques Prometheus

| Métrique | Labels | Description |
|----------|--------|-------------|
| `lunar_interpretation_generated_total` | source, model, subject | Générations |
| `lunar_interpretation_cache_hit_total` | subject, version | Cache hits |
| `lunar_interpretation_fallback_total` | fallback_level | Fallbacks |
| `lunar_interpretation_duration_seconds` | source, subject | Latence |
| `lunar_active_generations` | - | Générations en cours |

---

## Commandes Debug Rapides

```bash
# Vérifier config
grep "LUNAR_" apps/api/.env

# Logs timeout
grep -i "timeout\|TimeoutError" /var/log/api.log

# Métriques
curl -s localhost:8000/metrics | grep lunar_

# Test endpoint
curl -s localhost:8000/api/lunar-returns/current | jq .
```

---

## Plages à Lire (si nécessaire)

Pour debug approfondi, lire UNIQUEMENT ces plages :

| Problème | Fichier | Lignes |
|----------|---------|--------|
| Timeout | `services/lunar_interpretation_generator.py` | 362-460 |
| Fallback | `services/lunar_interpretation_generator.py` | 289-356 |
| Cache | `services/lunar_interpretation_generator.py` | 172-211 |
| Lazy gen | `routes/lunar_returns.py` | 517-600 |
| Config | `config.py` | 90-110 |

---

**Dernière màj** : 2026-01-25 | **Version** : 1.0
