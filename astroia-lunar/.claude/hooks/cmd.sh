#!/usr/bin/env bash
#
# Command dispatcher for .claude/commands/
# Usage: cmd.sh <command> [args...]
#
# Examples:
#   cmd.sh test              → loads core/test.md
#   cmd.sh lunar:debug       → loads lunar/debug.md
#   cmd.sh lunar:debug timeout → loads lunar/debug.md with arg "timeout"
#

set -euo pipefail

# Colors (portable macOS/Linux)
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Get script directory (works with symlinks)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
COMMANDS_DIR="${SCRIPT_DIR}/../commands"

# Resolve to absolute path
COMMANDS_DIR="$(cd "${COMMANDS_DIR}" && pwd)"

usage() {
    echo -e "${BLUE}Usage:${NC} ./cmd <command> [args...]"
    echo ""
    echo -e "${BLUE}Examples:${NC}"
    echo "  ./cmd test              → Run tests"
    echo "  ./cmd commit            → Commit with conventions"
    echo "  ./cmd lunar:debug       → Debug lunar returns"
    echo "  ./cmd lunar:debug timeout → Debug with focus on timeout"
    echo "  ./cmd list              → List all commands"
    echo ""
    echo -e "${BLUE}Available commands:${NC}"
    list_commands
    exit 1
}

list_commands() {
    echo ""
    # Core commands (no prefix)
    if [[ -d "${COMMANDS_DIR}/core" ]]; then
        echo -e "${GREEN}Core:${NC}"
        for f in "${COMMANDS_DIR}/core"/*.md; do
            [[ -f "$f" ]] || continue
            name=$(basename "$f" .md)
            # Extract description from YAML frontmatter
            desc=$(grep "^description:" "$f" 2>/dev/null | sed 's/^description: *//' | head -c 50)
            printf "  %-20s %s\n" "$name" "$desc"
        done
    fi

    # Domain commands (prefix:name)
    for domain_dir in "${COMMANDS_DIR}"/*/; do
        [[ -d "$domain_dir" ]] || continue
        domain=$(basename "$domain_dir")
        [[ "$domain" == "core" ]] && continue

        echo -e "${GREEN}${domain}:${NC}"
        for f in "${domain_dir}"*.md; do
            [[ -f "$f" ]] || continue
            name=$(basename "$f" .md)
            [[ "$name" == "_template" ]] && continue
            desc=$(grep "^description:" "$f" 2>/dev/null | sed 's/^description: *//' | head -c 50)
            printf "  %-20s %s\n" "${domain}:${name}" "$desc"
        done
    done
    echo ""
}

# Check arguments
if [[ $# -lt 1 ]]; then
    usage
fi

COMMAND="$1"
shift
ARGS="$*"

# Handle special commands
if [[ "$COMMAND" == "list" ]] || [[ "$COMMAND" == "--list" ]] || [[ "$COMMAND" == "-l" ]]; then
    echo -e "${BLUE}=== Available Commands ===${NC}"
    list_commands
    exit 0
fi

if [[ "$COMMAND" == "help" ]] || [[ "$COMMAND" == "--help" ]] || [[ "$COMMAND" == "-h" ]]; then
    usage
fi

# Map command to file path
if [[ "$COMMAND" == *":"* ]]; then
    # Domain command: lunar:debug → lunar/debug.md
    DOMAIN="${COMMAND%%:*}"
    NAME="${COMMAND#*:}"
    CMD_FILE="${COMMANDS_DIR}/${DOMAIN}/${NAME}.md"
else
    # Core command: test → core/test.md
    CMD_FILE="${COMMANDS_DIR}/core/${COMMAND}.md"
fi

# Check file exists
if [[ ! -f "$CMD_FILE" ]]; then
    echo -e "${RED}Error:${NC} Command '${COMMAND}' not found"
    echo -e "Expected file: ${CMD_FILE}"
    echo ""
    echo -e "Run ${YELLOW}./cmd list${NC} to see available commands"
    exit 1
fi

# Display loaded command
echo -e "${GREEN}=== Loaded Command ===${NC}"
echo -e "${BLUE}File:${NC} ${CMD_FILE}"
if [[ -n "$ARGS" ]]; then
    echo -e "${BLUE}Args:${NC} ${ARGS}"
fi
echo -e "${GREEN}======================${NC}"
echo ""

# Display content (max 220 lines)
head -n 220 "$CMD_FILE"

# If file has more than 220 lines, indicate truncation
TOTAL_LINES=$(wc -l < "$CMD_FILE" | tr -d ' ')
if [[ "$TOTAL_LINES" -gt 220 ]]; then
    echo ""
    echo -e "${YELLOW}... (truncated, ${TOTAL_LINES} total lines)${NC}"
fi

echo ""
echo -e "${GREEN}=== End Command ===${NC}"
