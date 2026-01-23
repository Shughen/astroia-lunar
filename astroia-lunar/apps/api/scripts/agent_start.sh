#!/bin/bash
# Script pour démarrer une tâche agent et créer un lock file
# Usage: ./scripts/agent_start.sh <task_id> <agent_id>

set -e

TASK_ID=$1
AGENT_ID=$2

if [ -z "$TASK_ID" ] || [ -z "$AGENT_ID" ]; then
    echo "Usage: $0 <task_id> <agent_id>"
    echo "Example: $0 task_2_1 agent_A"
    exit 1
fi

LOCK_FILE=".tasks/locks/${TASK_ID}.lock"
SPRINT_STATUS=".tasks/sprint_status.json"
AGENT_REGISTRY=".tasks/agent_registry.json"

# Vérifier si la tâche est déjà lockée
if [ -f "$LOCK_FILE" ]; then
    # Vérifier le heartbeat (timeout 10min = 600s)
    LAST_HEARTBEAT=$(jq -r '.last_heartbeat' "$LOCK_FILE")
    CURRENT_TIME=$(date -u +%s)
    HEARTBEAT_TIME=$(date -jf "%Y-%m-%dT%H:%M:%SZ" "$LAST_HEARTBEAT" +%s 2>/dev/null || echo 0)
    TIME_DIFF=$((CURRENT_TIME - HEARTBEAT_TIME))

    if [ $TIME_DIFF -lt 600 ]; then
        echo "❌ ERROR: Task $TASK_ID is already locked by another agent"
        jq '.' "$LOCK_FILE"
        exit 1
    else
        echo "⚠️  WARNING: Task $TASK_ID lock is stale (>10min), taking over..."
        rm "$LOCK_FILE"
    fi
fi

# Vérifier que la tâche existe dans sprint_status.json
TASK_EXISTS=$(jq -r --arg task_id "$TASK_ID" '.sprints[].tasks[] | select(.id == $task_id) | .id' "$SPRINT_STATUS")
if [ -z "$TASK_EXISTS" ]; then
    echo "❌ ERROR: Task $TASK_ID not found in sprint_status.json"
    exit 1
fi

# Récupérer les informations de la tâche
TASK_NAME=$(jq -r --arg task_id "$TASK_ID" '.sprints[].tasks[] | select(.id == $task_id) | .name' "$SPRINT_STATUS")
ESTIMATED_DURATION=$(jq -r --arg task_id "$TASK_ID" '.sprints[].tasks[] | select(.id == $task_id) | .estimated_duration' "$SPRINT_STATUS")

# Créer le lock file
TIMESTAMP=$(date -u +%Y-%m-%dT%H:%M:%SZ)
cat > "$LOCK_FILE" <<EOF
{
  "task_id": "$TASK_ID",
  "task_name": "$TASK_NAME",
  "agent_id": "$AGENT_ID",
  "status": "in_progress",
  "started_at": "$TIMESTAMP",
  "last_heartbeat": "$TIMESTAMP",
  "estimated_duration": "$ESTIMATED_DURATION"
}
EOF

echo "✅ Task $TASK_ID locked by $AGENT_ID"
echo "📝 Lock file created: $LOCK_FILE"

# Mettre à jour sprint_status.json
jq --arg task_id "$TASK_ID" --arg agent_id "$AGENT_ID" --arg timestamp "$TIMESTAMP" \
  '(.sprints[].tasks[] | select(.id == $task_id)) |= . + {status: "in_progress", assigned_to: $agent_id, started_at: $timestamp}' \
  "$SPRINT_STATUS" > "$SPRINT_STATUS.tmp" && mv "$SPRINT_STATUS.tmp" "$SPRINT_STATUS"

echo "✅ sprint_status.json updated"

# Mettre à jour agent_registry.json
jq --arg agent_id "$AGENT_ID" --arg task_id "$TASK_ID" --arg timestamp "$TIMESTAMP" \
  '(.agents[] | select(.agent_id == $agent_id)) |= . + {current_task: $task_id, status: "active", last_heartbeat: $timestamp}' \
  "$AGENT_REGISTRY" > "$AGENT_REGISTRY.tmp" && mv "$AGENT_REGISTRY.tmp" "$AGENT_REGISTRY"

echo "✅ agent_registry.json updated"
echo ""
echo "🚀 Ready to work on task $TASK_ID"
echo "💡 Run './scripts/agent_heartbeat.sh $TASK_ID' every 5min"
echo "💡 Run './scripts/agent_complete.sh $TASK_ID $AGENT_ID' when done"
