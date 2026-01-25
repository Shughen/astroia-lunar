---
description: Créer une migration Alembic
---

# Objectif

Générer une migration de base de données avec Alembic. Assure des migrations safe et réversibles.

# Contexte à Charger

- `apps/api/alembic.ini` — Configuration Alembic
- `apps/api/models/` — Liste des modèles (pour référence)
- Dernière migration dans `apps/api/alembic/versions/` — Pattern à suivre

# Rôle

Tu es un DBA expert. Tu crées des migrations réversibles, tu testes upgrade ET downgrade, tu ne touches jamais aux données prod sans backup.

# Workflow Complet

1. **Modifier le modèle** dans `apps/api/models/<model>.py`
2. **Générer migration** :
   ```bash
   cd apps/api
   alembic revision --autogenerate -m "description_courte"
   ```
3. **Vérifier le fichier généré** dans `alembic/versions/`
4. **Tester upgrade** :
   ```bash
   alembic upgrade head
   ```
5. **Tester downgrade** (réversibilité) :
   ```bash
   alembic downgrade -1
   alembic upgrade head
   ```
6. **Commit** : migration + modèle modifié

# Contraintes

- TOUJOURS : Vérifier migration générée avant apply
- TOUJOURS : Tester downgrade (réversibilité)
- TOUJOURS : Nommer clairement : `add_column_x`, `create_table_y`
- JAMAIS : Modifier données production sans backup
- JAMAIS : Supprimer colonnes avec données sans migration de données

# Bonnes Pratiques

```python
# upgrade()
def upgrade():
    # Ajouter colonne nullable d'abord
    op.add_column('users', sa.Column('new_field', sa.String(100), nullable=True))

    # Migrer données si nécessaire
    # op.execute("UPDATE users SET new_field = 'default' WHERE new_field IS NULL")

    # Rendre non-nullable après si besoin
    # op.alter_column('users', 'new_field', nullable=False)


# downgrade() - TOUJOURS implémenter
def downgrade():
    op.drop_column('users', 'new_field')
```

# Résultat Attendu

```
Migration créée: alembic/versions/abc123_add_user_preferences.py
Upgrade: ✓ OK
Downgrade test: ✓ OK
Re-upgrade: ✓ OK

Prêt à commit.
```

# Exemples d'Utilisation

```
/db:migration "add user preferences"     → Migration nouvelle table
/db:migration "add email to users"       → Migration nouvelle colonne
/db:migration status                     → Voir état migrations
```

# v1.0 - 2026-01-25
