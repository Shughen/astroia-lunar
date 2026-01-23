# 📖 Guide Mise à Jour CLAUDE.md

## 🔒 Limitation Sécurité
Claude Code nécessite **toujours une validation manuelle** pour les modifications de fichiers.
Il n'y a pas de moyen de bypasser ce système pour des raisons de sécurité.

---

## ✅ Solutions Pratiques

### Option 1 : Workflow Recommandé (Le plus simple)
**Quand Claude met à jour CLAUDE.md** :
1. Acceptez ses modifications de code/tests normalement durant le travail
2. À la fin, acceptez **une seule fois** la mise à jour de CLAUDE.md
3. Claude fait toujours un **commit séparé** pour CLAUDE.md

**Avantage** : Aucune configuration, juste 1 clic à la fin

---

### Option 2 : Script Semi-Automatique
**Script créé** : `.claude/hooks/auto-update-claude-md.sh`

**Usage** :
```bash
# Mise à jour simple
./.claude/hooks/auto-update-claude-md.sh

# Avec version et message personnalisés
./.claude/hooks/auto-update-claude-md.sh 5.12 "Vague 5 terminée"
```

**Avantage** : Met à jour automatiquement la date et version

---

### Option 3 : Alias Git (Le plus rapide)
Ajoutez à votre `~/.gitconfig` :

```ini
[alias]
    # Commit rapide CLAUDE.md
    claude-update = !git add .claude/CLAUDE.md && git commit -m \"docs(claude): update CLAUDE.md\"

    # Commit avec message personnalisé
    claude-msg = "!f() { git add .claude/CLAUDE.md && git commit -m \"docs(claude): $1\"; }; f"
```

**Usage** :
```bash
# Simple
git claude-update

# Avec message
git claude-msg "Vague 5 complete"
```

**Avantage** : Ultra-rapide, 1 commande

---

### Option 4 : Hook Pre-Commit (Automatique)
**Créer** : `.git/hooks/pre-commit` (ou utiliser pre-commit framework)

```bash
#!/bin/bash
# Auto-update CLAUDE.md date avant chaque commit

if git diff --cached --name-only | grep -q ".claude/CLAUDE.md"; then
    DATE=$(date +"%Y-%m-%d")
    sed -i '' "s/\*\*Dernière mise à jour\*\* : [0-9-]*/\*\*Dernière mise à jour\*\* : $DATE/" .claude/CLAUDE.md
    git add .claude/CLAUDE.md
fi
```

**Avantage** : Met à jour automatiquement la date à chaque commit

---

## 🎯 Recommandation

**Pour vous** : **Option 1 (Workflow recommandé)**
- Simplicité maximale
- Aucune configuration
- Juste 1 clic de validation quand Claude modifie CLAUDE.md

**Si vous voulez plus d'automatisation** : **Option 3 (Alias Git)**
- Configuration 1 fois
- Utilisation ultra-rapide ensuite

---

## 📝 Notes

- Claude met **toujours CLAUDE.md à jour en dernier**
- Commit séparé des changements de code
- Validation manuelle = sécurité garantie
- Scripts helpers disponibles mais pas de bypass possible

---

**Dernière mise à jour** : 2026-01-23
