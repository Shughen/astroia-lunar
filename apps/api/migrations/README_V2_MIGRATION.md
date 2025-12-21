# Migration V2 - Révolution Lunaire

## 📋 Description

Migration SQL pour ajouter les colonnes V2 à la table `lunar_returns` dans Supabase.

**Colonnes ajoutées:**
- `v2_version` (VARCHAR(10), NULL) - Version du payload V2 (ex: "2.0.0")
- `v2_payload` (JSONB, NULL) - Payload JSON contenant tous les champs V2

**Indexes créés:**
- `idx_lunar_returns_v2_version` - Index B-tree filtré sur `v2_version` (WHERE v2_version IS NOT NULL)
- `idx_lunar_returns_v2_payload_gin` - Index GIN sur `v2_payload` pour recherche dans JSON

---

## 🚀 Application de la migration

### Dans Supabase Dashboard

1. Ouvrir Supabase Dashboard
2. Aller dans **SQL Editor**
3. Créer une nouvelle requête
4. Copier-coller le contenu de `add_v2_columns_to_lunar_returns.sql`
5. Exécuter la requête
6. Vérifier les messages dans les logs (NOTICE)

### Via psql (si accès direct)

```bash
psql -h YOUR_SUPABASE_HOST -U postgres -d postgres -f add_v2_columns_to_lunar_returns.sql
```

---

## ✅ Vérification après migration

### Vérifier les colonnes

```sql
SELECT 
    column_name, 
    data_type, 
    is_nullable
FROM information_schema.columns
WHERE table_name = 'lunar_returns'
AND column_name IN ('v2_version', 'v2_payload')
ORDER BY column_name;
```

**Résultat attendu:**
```
 column_name | data_type | is_nullable
-------------+-----------+-------------
 v2_payload  | jsonb     | YES
 v2_version  | character varying | YES
```

### Vérifier les indexes

```sql
SELECT 
    indexname, 
    indexdef
FROM pg_indexes
WHERE tablename = 'lunar_returns'
AND indexname IN ('idx_lunar_returns_v2_version', 'idx_lunar_returns_v2_payload_gin')
ORDER BY indexname;
```

**Résultat attendu:**
```
 indexname                          | indexdef
------------------------------------+------------------------------------------
 idx_lunar_returns_v2_payload_gin   | CREATE INDEX ... USING gin (v2_payload)
 idx_lunar_returns_v2_version       | CREATE INDEX ... WHERE (v2_version IS NOT NULL)
```

### Compter les révolutions V2

```sql
SELECT 
    COUNT(*) as total_revolutions,
    COUNT(v2_version) as v2_revolutions,
    COUNT(*) - COUNT(v2_version) as v1_revolutions
FROM lunar_returns;
```

---

## 🔄 Rollback

En cas de problème, utiliser le script de rollback:

```sql
-- Exécuter dans Supabase SQL Editor
-- Fichier: rollback_v2_columns_from_lunar_returns.sql
```

**⚠️ Attention:** Le rollback supprime les colonnes et leurs données. Assurez-vous d'avoir une sauvegarde si nécessaire.

---

## 📊 Structure v2_payload attendue

Après implémentation du code V2, `v2_payload` contiendra:

```json
{
  "lunar_phase": {
    "type": "waxing_crescent",
    "name": "Premier croissant",
    "emoji": "🌒",
    "description": "Croissance et expansion",
    "angle": 67.5
  },
  "significant_aspects": [
    {
      "from": "Moon",
      "to": "Venus",
      "aspect_type": "trine",
      "orb": 2.3,
      "score": 87.5,
      "strength": "strong",
      "interpretation": "...",
      "emoji": "△"
    }
  ],
  "dominant_aspect": {
    "from": "Moon",
    "to": "Venus",
    "aspect_type": "trine",
    "orb": 2.3,
    "score": 87.5,
    "strength": "strong"
  },
  "focus": {
    "theme": "Stabilité financière",
    "house": 2,
    "description": "Tes ressources matérielles...",
    "keywords": ["finances", "valeurs", "ressources"]
  },
  "suggestions": {
    "actions": ["Fais un bilan de tes finances"],
    "avoid": ["Évite les dépenses impulsives"],
    "opportunities": ["Période favorable pour investir"]
  }
}
```

Et `v2_version` sera `"2.0.0"`.

---

## ✅ Caractéristiques du script

- **Idempotent:** Peut être exécuté plusieurs fois sans erreur
- **Sécurisé:** Vérifie l'existence avant création/suppression
- **Informatif:** Affiche des messages NOTICE à chaque étape
- **Vérifié:** Inclut une vérification finale avec résumé

---

## 📝 Notes importantes

1. **Compatibilité V1:** Les colonnes V2 sont NULL par défaut, donc les révolutions V1 existantes continuent de fonctionner
2. **Performance:** Les index sont optimisés (B-tree filtré pour v2_version, GIN pour recherche JSON)
3. **Migration progressive:** Le code V2 peut être déployé progressivement sans casser V1

---

**Date de création:** 2025-01-XX  
**Statut:** ✅ Prêt pour exécution  
**Branche:** `feat/lunar-revolution-v2`

