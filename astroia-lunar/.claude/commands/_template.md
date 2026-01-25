---
description: [Description courte en 1 ligne - sera affichée dans la liste des commandes]
---

# Objectif

[2-3 phrases décrivant ce que fait la commande et quand l'utiliser]

# Contexte à Charger

Fichiers à lire pour cette tâche :
- `apps/api/path/to/file.py` — Raison de charger ce fichier
- `apps/api/docs/DOC.md` — Documentation associée

# Rôle

Tu es un [rôle spécialisé]. Tu dois [comportement attendu].

# Contraintes

- JAMAIS : [actions interdites spécifiques]
- TOUJOURS : [actions obligatoires]

# Workflow

1. Première étape
2. Deuxième étape
3. Résultat attendu

# Résultat Attendu

```
Format de sortie attendu
```

# Exemples d'Utilisation

```
/command              → Description action par défaut
/command arg1         → Description avec argument
/command -v arg1      → Description avec flag
```

---

# Notes pour créer une commande

## Bonnes pratiques

- Max 500 tokens par commande
- Fichiers spécifiés par chemin exact (pas de globs `**/*`)
- Maximum 5 fichiers à charger
- Contraintes claires et non ambiguës
- Un objectif unique par commande

## Nommage

- Domaine : `domain/command.md` → `/domain:command`
- Core : `core/command.md` → `/command`

## Structure des dossiers

```
.claude/commands/
├── core/        → Commandes quotidiennes (/test, /commit, /health)
├── lunar/       → Domaine lunar returns
├── natal/       → Domaine natal charts
├── api/         → Développement API
├── db/          → Base de données
└── mobile/      → Mobile (read-only)
```

# v1.0 - 2026-01-25
