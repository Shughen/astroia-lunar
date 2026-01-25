---
description: Debugger la génération IA Claude Opus pour lunar returns
---

# Objectif

Diagnostiquer spécifiquement les problèmes de génération d'interprétations par Claude Opus 4.5. Focus sur l'API Anthropic, le prompt caching, et les métriques.

# Contexte à Charger

- `apps/api/services/lunar_interpretation_generator.py` — Générateur principal
- `apps/api/services/anthropic_client.py` — Client Anthropic (si existe)
- `apps/api/config.py:50-100` — Config Claude (LUNAR_CLAUDE_MODEL, etc.)
- `apps/api/docs/PROMETHEUS_METRICS.md` — Métriques génération

# Rôle

Tu es un expert intégration Claude API. Tu debugges les problèmes de génération IA : latence, erreurs, qualité des outputs, coûts.

# Configuration Claude

| Variable | Valeur attendue | Description |
|----------|-----------------|-------------|
| `LUNAR_LLM_MODE` | "llm" | Active Claude (vs "template") |
| `LUNAR_CLAUDE_MODEL` | claude-opus-4-5-20251101 | Modèle utilisé |
| `ANTHROPIC_API_KEY` | sk-ant-... | Clé API (NE PAS AFFICHER) |

# Prompt Caching

Le système utilise le Prompt Caching Anthropic pour réduire les coûts de 90% :
- System prompt = cached (stable)
- User prompt = variable (non-cached)

# Métriques à Vérifier

```
lunar_interpretation_generation_total{source="claude"}     → Nombre générations
lunar_interpretation_generation_duration_seconds           → Latence
lunar_interpretation_generation_errors_total               → Erreurs
lunar_interpretation_cache_hits_total                      → Cache DB hits
```

# Workflow Debug

1. **Vérifier config** : `LUNAR_LLM_MODE=llm`, modèle correct
2. **Tester API** : Génération simple avec logs
3. **Analyser latence** : Normal = 2-5s, Lent = >10s
4. **Checker erreurs** : Rate limits, auth, format

# Problèmes Courants

| Symptôme | Cause | Solution |
|----------|-------|----------|
| 401 Unauthorized | API key invalide | Vérifier ANTHROPIC_API_KEY |
| 429 Rate Limited | Trop de requêtes | Ajouter retry/backoff |
| Timeout | Prompt trop long | Réduire contexte |
| Mauvaise qualité | Prompt mal formaté | Revoir system prompt |

# Exemples d'Utilisation

```
/lunar:generation           → Diagnostic complet génération
/lunar:generation latency   → Focus sur les performances
/lunar:generation errors    → Analyser les erreurs récentes
/lunar:generation prompt    → Revoir le prompt system
```

# v1.0 - 2026-01-25
