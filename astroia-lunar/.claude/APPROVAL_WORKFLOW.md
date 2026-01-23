# 🚀 Workflow d'Approval Automatique CLAUDE.md

## ✅ Système Installé - Option 2

Un script semi-automatique pour approuver et commiter rapidement les modifications de CLAUDE.md.

---

## 📖 Utilisation

### Commande Rapide (depuis la racine du projet)
```bash
./claude-md [approve|commit|status]
```

### 3 Commandes Disponibles

#### 1. `./claude-md status` (par défaut)
Affiche le status actuel de CLAUDE.md
```bash
./claude-md status
# ou juste
./claude-md
```

#### 2. `./claude-md approve`
Approuve et stage automatiquement les modifications
```bash
./claude-md approve
```
→ Équivalent à `git add .claude/CLAUDE.md`

#### 3. `./claude-md commit`
Commit automatiquement avec un message généré
```bash
./claude-md commit
```
→ Génère un message de commit propre avec la version actuelle

---

## 🔄 Workflow Complet

### Quand Claude modifie CLAUDE.md :

```bash
# 1. Vérifier les modifications
./claude-md status

# 2. Approuver (stage)
./claude-md approve

# 3. Commiter automatiquement
./claude-md commit

# 4. Push (optionnel)
git push
```

### Ou tout en une fois :
```bash
./claude-md approve && ./claude-md commit && git push
```

---

## 🎯 Cas d'Usage

### Cas 1 : Claude vient de mettre à jour CLAUDE.md
```bash
# Vous acceptez les modifications dans l'éditeur
# Puis en terminal :
./claude-md approve
./claude-md commit
```

### Cas 2 : Vérifier s'il y a des modifications en attente
```bash
./claude-md status
```

### Cas 3 : Approuver + Commiter + Push en une ligne
```bash
./claude-md approve && ./claude-md commit && git push
```

---

## 📁 Fichiers Créés

```
astroia-lunar/
├── claude-md                            # Alias court (racine)
└── .claude/
    ├── hooks/
    │   └── auto-update-claude-md.sh    # Script principal
    ├── APPROVAL_WORKFLOW.md             # Ce guide
    └── CLAUDE_UPDATE_GUIDE.md           # Guide complet (4 options)
```

---

## 🔧 Personnalisation

### Modifier le script
```bash
nano .claude/hooks/auto-update-claude-md.sh
```

### Créer un alias global (optionnel)
Ajoutez à votre `~/.bashrc` ou `~/.zshrc` :
```bash
alias claude-md='~/astroia/astroia-lunar/claude-md'
```
→ Vous pourrez alors utiliser `claude-md` depuis n'importe où

---

## ⚠️ Important

- ✅ Le script **ne bypass pas la validation manuelle de Claude Code**
- ✅ Il simplifie juste le workflow Git après que vous ayez accepté les modifications
- ✅ Vous devez toujours **accepter les modifications dans l'éditeur d'abord**

---

## 🆘 Dépannage

### Le script ne trouve pas CLAUDE.md
```bash
# Vérifier que vous êtes à la racine du projet
pwd
# Doit afficher: /Users/remibeaurain/astroia/astroia-lunar
```

### Permission denied
```bash
chmod +x ./claude-md
chmod +x ./.claude/hooks/auto-update-claude-md.sh
```

### Voir les modifications en détail
```bash
git diff .claude/CLAUDE.md
```

---

**Dernière mise à jour** : 2026-01-23
**Script version** : 1.0
**Auteur** : Claude Sonnet 4.5 (Agent B)
