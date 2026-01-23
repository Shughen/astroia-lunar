# Système de Coordination Multi-Agents

## 🎯 Objectif

Permettre à plusieurs agents Claude de travailler en parallèle sur la refonte Lunar V1→V2 sans conflits, avec visibilité temps réel sur l'avancement.

## 📁 Structure

```
.tasks/
├── README.md                  # Ce fichier
├── sprint_status.json         # État global des sprints
├── agent_registry.json        # Agents actifs et leurs tâches
├── locks/                     # Lock files par tâche
│   ├── task_001.lock
│   └── task_002.lock
└── completed/                 # Tâches terminées (archive)
    └── task_001_completed.json
```

## 🔄 Workflow Agent

### 1. Démarrage (Registration)

Quand un agent démarre une tâche :

```bash
# Vérifier disponibilité
cat .tasks/sprint_status.json | jq '.sprints[] | select(.id=="sprint_2")'

# S'enregistrer
echo '{
  "agent_id": "agent_A",
  "task_id": "task_2_1",
  "task_name": "Refactor lunar_interpretation_generator",
  "status": "in_progress",
  "started_at": "'$(date -u +%Y-%m-%dT%H:%M:%SZ)'",
  "estimated_duration": "30min"
}' > .tasks/locks/task_2_1.lock
```

### 2. Pendant le travail (Heartbeat)

Mettre à jour le lock toutes les 5 min :

```bash
# Heartbeat (preuve de vie)
jq '.last_heartbeat = "'$(date -u +%Y-%m-%dT%H:%M:%SZ)'"' \
  .tasks/locks/task_2_1.lock > tmp && mv tmp .tasks/locks/task_2_1.lock
```

### 3. Fin de tâche (Completion)

Marquer comme complétée :

```bash
# Compléter
mv .tasks/locks/task_2_1.lock .tasks/completed/task_2_1_completed.json

# Mettre à jour sprint_status.json
jq '.sprints[1].tasks[] |= if .id == "task_2_1" then .status = "completed" else . end' \
  .tasks/sprint_status.json > tmp && mv tmp .tasks/sprint_status.json
```

## 🚦 Règles de Coordination

### Règle 1 : Vérifier avant de commencer

```python
import json
from pathlib import Path

def can_start_task(task_id: str) -> bool:
    lock_file = Path(f".tasks/locks/{task_id}.lock")
    if lock_file.exists():
        # Vérifier heartbeat (timeout 10min)
        lock = json.loads(lock_file.read_text())
        last_heartbeat = datetime.fromisoformat(lock['last_heartbeat'])
        if (datetime.utcnow() - last_heartbeat).seconds < 600:
            return False  # Agent actif
    return True
```

### Règle 2 : Libérer en cas d'erreur

Si un agent crash, les autres peuvent reprendre après timeout (10min).

### Règle 3 : Communication via status

Les agents lisent `sprint_status.json` toutes les 2min pour voir l'avancement global.

### Règle 4 : Branches Git par sprint

```bash
# Agent A (Sprint 2, Task 1)
git checkout -b sprint2/task-2-1-lunar-interpretation-generator

# Agent B (Sprint 2, Task 2)
git checkout -b sprint2/task-2-2-lunar-report-builder
```

Merge dans `sprint2/integration` avant `main`.

## 📊 Format sprint_status.json

```json
{
  "project": "lunar-v1-to-v2-migration",
  "version": "2.0",
  "last_updated": "2026-01-23T14:30:00Z",
  "sprints": [
    {
      "id": "sprint_1",
      "name": "Infrastructure & Documentation",
      "status": "in_progress",
      "started_at": "2026-01-23T14:00:00Z",
      "estimated_end": "2026-01-23T18:00:00Z",
      "tasks": [
        {
          "id": "task_1_1",
          "name": "Mettre à jour CLAUDE.md",
          "status": "completed",
          "assigned_to": "agent_main",
          "completed_at": "2026-01-23T14:30:00Z"
        },
        {
          "id": "task_1_2",
          "name": "Créer système coordination",
          "status": "in_progress",
          "assigned_to": "agent_main",
          "progress": 80
        }
      ]
    }
  ]
}
```

## 📋 Format agent_registry.json

```json
{
  "agents": [
    {
      "agent_id": "agent_A",
      "current_task": "task_2_1",
      "status": "active",
      "last_heartbeat": "2026-01-23T14:30:00Z",
      "capabilities": ["refactoring", "testing"],
      "performance": {
        "tasks_completed": 3,
        "avg_duration_minutes": 25
      }
    },
    {
      "agent_id": "agent_B",
      "current_task": null,
      "status": "idle",
      "last_heartbeat": "2026-01-23T14:25:00Z"
    }
  ]
}
```

## 🔍 Monitoring

### Dashboard temps réel (CLI)

```bash
# Voir statut global
jq '.sprints[] | {id, name, status, progress: (.tasks | map(select(.status=="completed")) | length) / (.tasks | length) * 100}' \
  .tasks/sprint_status.json

# Voir agents actifs
jq '.agents[] | select(.status=="active")' .tasks/agent_registry.json

# Voir tâches bloquées (timeout)
find .tasks/locks -name "*.lock" -mmin +10
```

### Alertes

Si un lock file > 10min sans heartbeat :
```bash
# Libérer automatiquement
find .tasks/locks -name "*.lock" -mmin +10 -exec rm {} \;
```

## 🎯 Best Practices

1. **Toujours vérifier** `sprint_status.json` avant de commencer
2. **Heartbeat régulier** (toutes les 5min)
3. **Nettoyer** les locks en cas d'arrêt
4. **Documenter** les changements dans les commits
5. **Communiquer** via Slack/Discord si deadlock

## 📚 Exemple d'utilisation

### Scenario : 3 agents parallèles sur Sprint 2

**Agent A** :
```bash
# Démarrer task_2_1
./scripts/agent_start.sh task_2_1 agent_A

# Travailler...
# (heartbeat automatique en background)

# Terminer
./scripts/agent_complete.sh task_2_1 agent_A
```

**Agent B** :
```bash
# Démarrer task_2_2 (parallèle)
./scripts/agent_start.sh task_2_2 agent_B
```

**Agent C** :
```bash
# Essayer task_2_3
./scripts/agent_start.sh task_2_3 agent_C
# Erreur : task_2_3 dépend de task_2_1 (pas complétée)

# Attendre ou prendre task_2_4 (indépendante)
./scripts/agent_start.sh task_2_4 agent_C
```

---

**Version** : 1.0
**Créé** : 2026-01-23
**Auteur** : Claude Code (Sonnet 4.5)
