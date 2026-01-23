#!/bin/bash
# Script pour approuver automatiquement les modifications de CLAUDE.md par Claude
# Usage: ./.claude/hooks/auto-update-claude-md.sh [approve|commit|status]

set -e

CLAUDE_MD=".claude/CLAUDE.md"
PROJECT_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"

cd "$PROJECT_ROOT"

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

case "${1:-status}" in
    approve)
        echo -e "${BLUE}🔄 Approval automatique des modifications CLAUDE.md...${NC}"

        if git diff --quiet "$CLAUDE_MD" && git diff --cached --quiet "$CLAUDE_MD"; then
            echo -e "${GREEN}✅ Aucune modification en attente${NC}"
            exit 0
        fi

        # Auto-stage les modifications
        git add "$CLAUDE_MD"

        echo -e "${GREEN}✅ CLAUDE.md approuvé et staged${NC}"
        echo -e "${YELLOW}💡 Prochaine étape: git commit ou ./hooks/auto-update-claude-md.sh commit${NC}"
        ;;

    commit)
        echo -e "${BLUE}🔄 Commit automatique de CLAUDE.md...${NC}"

        if git diff --cached --quiet "$CLAUDE_MD"; then
            if git diff --quiet "$CLAUDE_MD"; then
                echo -e "${GREEN}✅ Aucune modification à commiter${NC}"
                exit 0
            else
                echo -e "${YELLOW}⚠️  Fichier non staged. Staging...${NC}"
                git add "$CLAUDE_MD"
            fi
        fi

        # Extraire la version actuelle
        VERSION=$(grep "^\*\*Version\*\*" "$CLAUDE_MD" | sed 's/.*: \([0-9.]*\).*/\1/')

        # Commit avec message auto-généré
        git commit -m "docs(claude): update CLAUDE.md to v${VERSION}

Auto-committed via hook script
$(git diff --cached --stat "$CLAUDE_MD")"

        echo -e "${GREEN}✅ CLAUDE.md commité (version $VERSION)${NC}"
        echo -e "${YELLOW}💡 Prochaine étape: git push${NC}"
        ;;

    status)
        echo -e "${BLUE}📊 Status CLAUDE.md:${NC}"
        echo ""

        # Check unstaged changes
        if ! git diff --quiet "$CLAUDE_MD" 2>/dev/null; then
            echo -e "${YELLOW}📝 Modifications non staged:${NC}"
            git diff --stat "$CLAUDE_MD"
            echo ""
        fi

        # Check staged changes
        if ! git diff --cached --quiet "$CLAUDE_MD" 2>/dev/null; then
            echo -e "${GREEN}✅ Modifications staged:${NC}"
            git diff --cached --stat "$CLAUDE_MD"
            echo ""
        fi

        # Check if nothing changed
        if git diff --quiet "$CLAUDE_MD" && git diff --cached --quiet "$CLAUDE_MD"; then
            echo -e "${GREEN}✅ Aucune modification en attente${NC}"
        fi

        echo ""
        echo -e "${BLUE}Commandes disponibles:${NC}"
        echo "  approve  - Approuver et stage les modifications"
        echo "  commit   - Commiter automatiquement"
        echo "  status   - Afficher ce status"
        ;;

    *)
        echo "Usage: $0 {approve|commit|status}"
        echo ""
        echo "  approve  - Approuve et stage les modifications de CLAUDE.md"
        echo "  commit   - Commit automatiquement les modifications staged"
        echo "  status   - Affiche le status actuel (défaut)"
        exit 1
        ;;
esac
