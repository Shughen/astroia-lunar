---
description: Debugger les lunar returns et interprétations (token-safe)
---

# Objectif

Diagnostiquer les problèmes de génération/affichage des lunar returns. Analyse la hiérarchie de fallback et identifie les points de blocage.

# Contexte à Charger

**Token-safe** : Ne pas lire les fichiers source complets.

- `apps/api/docs/LUNAR_DEBUG_INDEX.md` — Index debug avec lignes clés (CE FICHIER SUFFIT)
- `apps/api/config.py:90-110` — Config LUNAR_* uniquement (si besoin)

# Rôle

Tu es un expert debugging lunar. Tu utilises l'index de debug pour naviguer sans charger les fichiers volumineux.

# Architecture Fallback (rappel)

```
1. DB Cache (LunarInterpretation)     → Cache hit = retour immédiat
2. Claude Opus 4.5                    → Timeout 30s, 3 retries
3. DB Templates (1728 templates)      → Fallback niveau 2
4. Templates Hardcodés                → Fallback ultime
```

# Contraintes

- JAMAIS : Lire `lunar_returns.py` ou `lunar_interpretation_generator.py` en entier
- JAMAIS : Afficher ANTHROPIC_API_KEY ou autres secrets
- TOUJOURS : Utiliser `LUNAR_DEBUG_INDEX.md` comme référence
- TOUJOURS : Lire uniquement les plages de lignes ciblées si besoin

# Workflow Debug

1. **Charger l'index** : `apps/api/docs/LUNAR_DEBUG_INDEX.md`
2. **Identifier symptôme** dans la table "Erreurs Courantes"
3. **Localiser** la fonction/ligne concernée
4. **Si besoin** : lire UNIQUEMENT la plage de lignes indiquée
5. **Proposer fix** minimal

# Plages de Lecture Autorisées

| Problème | Fichier | Lignes |
|----------|---------|--------|
| Timeout | `services/lunar_interpretation_generator.py` | 362-460 |
| Fallback | `services/lunar_interpretation_generator.py` | 289-356 |
| Cache | `services/lunar_interpretation_generator.py` | 172-211 |
| Lazy gen | `routes/lunar_returns.py` | 517-600 |
| Config | `config.py` | 90-110 |

# Points de Debug Courants

| Symptôme | Cause probable | Solution |
|----------|----------------|----------|
| Timeout | Claude API lent | Vérifier API key, augmenter timeout (ligne 445) |
| Fallback template | Cache miss + Claude fail | Vérifier DB LunarInterpretation |
| 500 error | Exception non catchée | Lire logs structlog |
| Contenu générique | Hardcoded utilisé | Vérifier LUNAR_LLM_MODE=anthropic |

# Config Clés (rappel)

| Variable | Default | Description |
|----------|---------|-------------|
| `LUNAR_LLM_MODE` | "off" | "off" ou "anthropic" |
| `LUNAR_CLAUDE_MODEL` | "opus" | opus/sonnet/haiku |
| Timeout | 30s | Attente max Claude |

# Commandes Debug Rapides

```bash
# Config
grep "LUNAR_" apps/api/.env

# Logs
grep -i "timeout\|fallback" /var/log/api.log | tail -20

# Métriques
curl -s localhost:8000/metrics | grep lunar_interpretation

# Test
curl -s localhost:8000/api/lunar-returns/current | jq .metadata
```

# Exemples d'Utilisation

```
./cmd lunar:debug              → Charge l'index, prêt à debugger
./cmd lunar:debug timeout      → Focus timeout (lire lignes 362-460)
./cmd lunar:debug fallback     → Focus fallback (lire lignes 289-356)
./cmd lunar:debug cache        → Focus cache (lire lignes 172-211)
./cmd lunar:debug config       → Vérifier config.py:90-110
```

# v2.0 - 2026-01-25 (token-safe)
