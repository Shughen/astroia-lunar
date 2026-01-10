# Corrections Appliquées - Vérification Pré-V2

**Date:** 2025-01-XX  
**Branche:** `feat/lunar-revolution-v2`

---

## ✅ Résumé

2 corrections minimales ont été appliquées pour garantir la compatibilité mobile ↔ backend :

1. **Schema Pydantic `user_id`**: Accepte maintenant `Union[UUID, int]` (le mobile envoie `number`)
2. **Migration SQL**: Ajout explicite de `table_schema = 'public'` et `schemaname = 'public'` dans les WHERE

---

## 📝 Diff: `apps/api/schemas/lunar_return.py`

```diff
--- a/apps/api/schemas/lunar_return.py
+++ b/apps/api/schemas/lunar_return.py
@@ -1,8 +1,9 @@
 """Schemas Pydantic pour LunarReturn (révolutions lunaires)"""
 
 from pydantic import BaseModel, Field
-from typing import Optional, List, Dict, Any
+from typing import Optional, List, Dict, Any, Union
 from datetime import datetime
 from uuid import UUID
 
 
@@ -12,7 +13,7 @@ class LunarReturnGenerateRequest(BaseModel):
     """Request pour générer une révolution lunaire"""
     cycle_number: int = Field(..., ge=1, description="Numéro du cycle (1, 2, 3, ...)")
-    user_id: UUID = Field(..., description="ID de l'utilisateur")
+    user_id: Union[UUID, int] = Field(..., description="ID de l'utilisateur (UUID ou int)")
```

**Raison:** Pydantic UUID rejette les `int`. Le mobile envoie `user.id` (type `number`). Solution : accepter explicitement `Union[UUID, int]`.

---

## 📝 Diff: `apps/api/migrations/add_v2_columns_to_lunar_returns.sql`

**Changements:** Ajout de `table_schema = 'public'` et `schemaname = 'public'` dans tous les WHERE pour être explicite sur le schéma PostgreSQL.

**Exemples de modifications:**

```diff
--- a/apps/api/migrations/add_v2_columns_to_lunar_returns.sql
+++ b/apps/api/migrations/add_v2_columns_to_lunar_returns.sql
@@ -10,7 +10,8 @@ DO $$
     IF NOT EXISTS (
         SELECT 1 
         FROM information_schema.columns 
-        WHERE table_name = 'lunar_returns' 
+        WHERE table_schema = 'public'
+        AND table_name = 'lunar_returns' 
         AND column_name = 'v2_version'
     ) THEN
```

```diff
@@ -50,7 +51,8 @@ DO $$
     IF NOT EXISTS (
         SELECT 1 
         FROM pg_indexes 
-        WHERE tablename = 'lunar_returns' 
+        WHERE schemaname = 'public'
+        AND tablename = 'lunar_returns' 
         AND indexname = 'idx_lunar_returns_v2_version'
     ) THEN
```

**Nombre total de modifications:** 8 occurrences (4 pour `information_schema.columns`, 4 pour `pg_indexes`)

**Raison:** Meilleure pratique PostgreSQL pour être explicite sur le schéma, évite les conflits si d'autres schémas existent.

---

## ✅ Vérification

**Test schema Pydantic:**
```bash
cd apps/api
python3 -c "from schemas.lunar_return import LunarReturnGenerateRequest; t = LunarReturnGenerateRequest(cycle_number=1, user_id=1); print(f'✅ Accepte int: {t.user_id}')"
# Résultat: ✅ Accepte int: 1
```

**Linter:**
```bash
# Aucune erreur TypeScript/Python détectée
```

---

## 🚀 Commandes Git

```bash
# Commit correction schema
git add apps/api/schemas/lunar_return.py
git commit -m "fix: accept int or UUID for user_id in LunarReturnGenerateRequest

- Mobile envoie user.id (type number)
- Pydantic UUID rejette les int
- Solution: Union[UUID, int] pour compatibilité"

# Commit amélioration migration SQL
git add apps/api/migrations/add_v2_columns_to_lunar_returns.sql
git commit -m "chore: add explicit schema check in migration SQL

- Ajout table_schema = 'public' dans information_schema.columns WHERE
- Ajout schemaname = 'public' dans pg_indexes WHERE
- Meilleure pratique PostgreSQL pour éviter conflits entre schémas"
```

---

## 📊 Tableau de Vérification Final

| Point | État Initial | État Final | Action |
|-------|--------------|------------|--------|
| **A) user_id type** | ⚠️ Mismatch (UUID vs number) | ✅ Corrigé (Union[UUID, int]) | Schema modifié |
| **B) Appel API** | ✅ OK | ✅ OK | Aucune action |
| **C) Calcul cycleNumber** | ✅ OK | ✅ OK | Aucune action |
| **D) Migration SQL** | ✅ OK (idempotent) | ✅ OK + amélioré (schéma explicite) | SQL amélioré |
| **E) Smoke test** | ✅ Prêt | ✅ Prêt | Aucune action |

---

## 🎯 Conclusion

**Toutes les vérifications sont OK. Les corrections minimales nécessaires ont été appliquées.**

✅ **Prêt pour implémentation V2 backend** selon `BACKEND_AUDIT_LUNAR_REVOLUTION_V2.md`

