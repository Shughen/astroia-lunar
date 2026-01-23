#!/bin/bash
# Script pour mettre à jour le heartbeat d'un lock file
# Usage: ./scripts/agent_heartbeat.sh <task_id>

set -e

TASK_ID=$1

if [ -z "$TASK_ID" ]; then
    echo "Usage: $0 <task_id>"
    echo "Example: $0 task_2_1"
    exit 1
fi

LOCK_FILE=".tasks/locks/${TASK_ID}.lock"

# Vérifier que le lock existe
if [ ! -f "$LOCK_FILE" ]; then
    echo "❌ ERROR: No lock file found for task $TASK_ID"
    echo "💡 Task may have been completed or never started"
    exit 1
fi

# Mettre à jour le heartbeat
TIMESTAMP=$(date -u +%Y-%m-%dT%H:%M:%SZ)
jq --arg timestamp "$TIMESTAMP" '.last_heartbeat = $timestamp' "$LOCK_FILE" > "$LOCK_FILE.tmp" && mv "$LOCK_FILE.tmp" "$LOCK_FILE"

# Récupérer les infos du lock
AGENT_ID=$(jq -r '.agent_id' "$LOCK_FILE")
TASK_NAME=$(jq -r '.task_name' "$LOCK_FILE")
STARTED_AT=$(jq -r '.started_at' "$LOCK_FILE")

# Calculer le temps écoulé
START_EPOCH=$(date -jf "%Y-%m-%dT%H:%M:%SZ" "$STARTED_AT" +%s 2>/dev/null || echo 0)
CURRENT_EPOCH=$(date -u +%s)
ELAPSED_MIN=$(( (CURRENT_EPOCH - START_EPOCH) / 60 ))

echo "💓 Heartbeat updated for task $TASK_ID"
echo "👤 Agent: $AGENT_ID"
echo "📋 Task: $TASK_NAME"
echo "⏱️  Elapsed: ${ELAPSED_MIN} minutes"
echo "🕐 Last heartbeat: $TIMESTAMP"

# Mettre à jour agent_registry.json
AGENT_REGISTRY=".tasks/agent_registry.json"
jq --arg agent_id "$AGENT_ID" --arg timestamp "$TIMESTAMP" \
  '(.agents[] | select(.agent_id == $agent_id)) |= . + {last_heartbeat: $timestamp}' \
  "$AGENT_REGISTRY" > "$AGENT_REGISTRY.tmp" && mv "$AGENT_REGISTRY.tmp" "$AGENT_REGISTRY"
