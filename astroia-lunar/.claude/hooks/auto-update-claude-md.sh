#!/bin/bash
# Script pour approuver automatiquement les modifications de CLAUDE.md par Claude
# Usage: ./.claude/hooks/auto-update-claude-md.sh [approve|commit|status]

set -euo pipefail

CLAUDE_MD=".claude/CLAUDE.md"
PROJECT_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"

cd "$PROJECT_ROOT"

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Fonction de sécurité: vérifier que seul CLAUDE.md est staged
ensure_only_claude_md_staged() {
    # Liste tous les fichiers staged
    local staged_files
    staged_files=$(git diff --cached --name-only)

    if [ -z "$staged_files" ]; then
        return 0  # Aucun fichier staged, OK
    fi

    # Compter le nombre de fichiers staged
    local staged_count
    staged_count=$(echo "$staged_files" | wc -l | tr -d ' ')

    # Si plus d'un fichier, refuser
    if [ "$staged_count" -ne 1 ]; then
        echo -e "${YELLOW}⚠️  ERREUR DE SÉCURITÉ: D'autres fichiers sont staged!${NC}" >&2
        echo -e "${YELLOW}Fichiers staged actuellement:${NC}" >&2
        echo "$staged_files" | sed 's/^/  - /' >&2
        echo "" >&2
        echo -e "${YELLOW}Ce script ne peut commiter que CLAUDE.md seul.${NC}" >&2
        echo -e "${YELLOW}Utilisez 'git reset HEAD <file>' pour unstage les autres fichiers.${NC}" >&2
        exit 1
    fi

    # Vérifier que le fichier unique finit par CLAUDE.md (support monorepo)
    if ! echo "$staged_files" | grep -q "CLAUDE\.md$"; then
        echo -e "${YELLOW}⚠️  ERREUR DE SÉCURITÉ: Le fichier staged n'est pas CLAUDE.md!${NC}" >&2
        echo -e "${YELLOW}Fichier staged: $staged_files${NC}" >&2
        exit 1
    fi
}

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
        VERSION=$(grep "^\*\*Version\*\*" "$CLAUDE_MD" 2>/dev/null | sed 's/.*: \([0-9.]*\).*/\1/' || echo "")
        if [ -z "$VERSION" ]; then
            VERSION="unknown"
        fi

        # SÉCURITÉ: Vérifier qu'aucun autre fichier n'est staged
        ensure_only_claude_md_staged

        # Créer message de commit via fichier temporaire (plus sûr que -m multi-lignes)
        COMMIT_MSG=$(mktemp)
        trap 'rm -f "$COMMIT_MSG"' EXIT

        cat > "$COMMIT_MSG" <<EOF
docs(claude): update CLAUDE.md to v${VERSION}

Auto-committed via hook script
$(git diff --cached --stat "$CLAUDE_MD")
EOF
        git commit -F "$COMMIT_MSG"

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
