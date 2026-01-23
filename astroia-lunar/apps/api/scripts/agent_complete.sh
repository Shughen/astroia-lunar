#!/bin/bash
# Script pour terminer une tâche agent et libérer le lock
# Usage: ./scripts/agent_complete.sh <task_id> <agent_id>

set -e

TASK_ID=$1
AGENT_ID=$2

if [ -z "$TASK_ID" ] || [ -z "$AGENT_ID" ]; then
    echo "Usage: $0 <task_id> <agent_id>"
    echo "Example: $0 task_2_1 agent_A"
    exit 1
fi

LOCK_FILE=".tasks/locks/${TASK_ID}.lock"
COMPLETED_DIR=".tasks/completed"
SPRINT_STATUS=".tasks/sprint_status.json"
AGENT_REGISTRY=".tasks/agent_registry.json"

# Vérifier que le lock existe
if [ ! -f "$LOCK_FILE" ]; then
    echo "❌ ERROR: No lock file found for task $TASK_ID"
    echo "💡 Task may already be completed or was never started"
    exit 1
fi

# Vérifier que c'est le bon agent
LOCK_AGENT=$(jq -r '.agent_id' "$LOCK_FILE")
if [ "$LOCK_AGENT" != "$AGENT_ID" ]; then
    echo "❌ ERROR: Task $TASK_ID is locked by $LOCK_AGENT, not $AGENT_ID"
    exit 1
fi

# Récupérer les informations du lock
STARTED_AT=$(jq -r '.started_at' "$LOCK_FILE")
TIMESTAMP=$(date -u +%Y-%m-%dT%H:%M:%SZ)

# Calculer la durée (approximatif)
START_EPOCH=$(date -jf "%Y-%m-%dT%H:%M:%SZ" "$STARTED_AT" +%s 2>/dev/null || echo 0)
END_EPOCH=$(date -u +%s)
DURATION_MIN=$(( (END_EPOCH - START_EPOCH) / 60 ))

# Créer le fichier de complétion
COMPLETION_FILE="$COMPLETED_DIR/${TASK_ID}_completed.json"
jq --arg completed_at "$TIMESTAMP" --arg duration_min "$DURATION_MIN" \
  '. + {status: "completed", completed_at: $completed_at, duration_minutes: ($duration_min | tonumber)}' \
  "$LOCK_FILE" > "$COMPLETION_FILE"

echo "✅ Task $TASK_ID completed by $AGENT_ID"
echo "⏱️  Duration: ${DURATION_MIN} minutes"
echo "📝 Completion file: $COMPLETION_FILE"

# Supprimer le lock file
rm "$LOCK_FILE"
echo "🔓 Lock file removed"

# Mettre à jour sprint_status.json
jq --arg task_id "$TASK_ID" --arg timestamp "$TIMESTAMP" \
  '(.sprints[].tasks[] | select(.id == $task_id)) |= . + {status: "completed", completed_at: $timestamp}' \
  "$SPRINT_STATUS" > "$SPRINT_STATUS.tmp" && mv "$SPRINT_STATUS.tmp" "$SPRINT_STATUS"

echo "✅ sprint_status.json updated"

# Mettre à jour les statistiques de l'agent
jq --arg agent_id "$AGENT_ID" --arg task_id "$TASK_ID" --arg timestamp "$TIMESTAMP" --arg duration "$DURATION_MIN" \
  '(.agents[] | select(.agent_id == $agent_id)) |=
    . + {
      current_task: null,
      status: "idle",
      performance: {
        tasks_completed: (.performance.tasks_completed + 1),
        avg_duration_minutes: ((.performance.avg_duration_minutes * .performance.tasks_completed + ($duration | tonumber)) / (.performance.tasks_completed + 1)),
        success_rate: 100
      }
    } |
    .history += [{task_id: $task_id, completed_at: $timestamp, duration_min: ($duration | tonumber)}]
  ' \
  "$AGENT_REGISTRY" > "$AGENT_REGISTRY.tmp" && mv "$AGENT_REGISTRY.tmp" "$AGENT_REGISTRY"

echo "✅ agent_registry.json updated"
echo ""
echo "🎉 Task $TASK_ID completed successfully!"
echo "💡 Ready for next task"

# Afficher le progrès global
TOTAL_TASKS=$(jq '[.sprints[].tasks[]] | length' "$SPRINT_STATUS")
COMPLETED_TASKS=$(jq '[.sprints[].tasks[] | select(.status == "completed")] | length' "$SPRINT_STATUS")
PROGRESS=$(( COMPLETED_TASKS * 100 / TOTAL_TASKS ))

echo ""
echo "📊 Global progress: $COMPLETED_TASKS/$TOTAL_TASKS tasks completed ($PROGRESS%)"
