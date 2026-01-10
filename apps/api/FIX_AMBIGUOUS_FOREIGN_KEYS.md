# Fix: Correction AmbiguousForeignKeysError (users ↔ natal_charts)

**Date:** 2025-01-XX  
**Problème:** `sqlalchemy.exc.AmbiguousForeignKeysError: Can't determine join between 'users' and 'natal_charts' ... multiple foreign key paths ... relationship User.natal_chart`  
**Cause:** SQLAlchemy ne peut pas déterminer quelle clé étrangère utiliser entre `user_id` (legacy) et `user_id_int` (nouveau) dans `natal_charts`.

---

## 🔍 Problème identifié

Après avoir ajouté `natal_charts.user_id_int INTEGER NOT NULL` (FK vers `users.id`) tout en gardant le legacy `natal_charts.user_id` (ancienne FK), SQLAlchemy voit deux chemins de clés étrangères possibles et ne peut plus déterminer automatiquement lequel utiliser pour la relation `User.natal_chart`.

---

## ✅ Solution implémentée

### Correction dans `apps/api/models/user.py`

Ajout de `primaryjoin` explicite dans la relation `User.natal_chart` pour forcer l'utilisation de `user_id_int` :

```python
natal_chart = relationship(
    "NatalChart",
    back_populates="user",
    uselist=False,
    primaryjoin="User.id == foreign(NatalChart.user_id_int)"
)
```

**Explication:**
- `primaryjoin` : Spécifie explicitement la condition de jointure SQL
- `foreign(NatalChart.user_id_int)` : Indique à SQLAlchemy d'utiliser la colonne `user_id_int` de la table `natal_charts`
- `User.id == ...` : Jointure sur la clé primaire de `users`

### Vérification côté `NatalChart`

La relation `NatalChart.user` utilise déjà `foreign_keys=[user_id_int]`, ce qui est cohérent :

```python
user = relationship("User", back_populates="natal_chart", foreign_keys=[user_id_int])
```

---

## 📋 Fichiers modifiés

1. **`apps/api/models/user.py`**
   - Ajout import `foreign` depuis `sqlalchemy.orm`
   - Ajout `primaryjoin` explicite dans la relation `natal_chart`

---

## 🔧 Diff

```diff
--- a/apps/api/models/user.py
+++ b/apps/api/models/user.py
@@ -1,7 +1,7 @@
 """Modèle User"""
 
 from sqlalchemy import Column, Integer, String, DateTime, Boolean
-from sqlalchemy.orm import relationship
+from sqlalchemy.orm import relationship, foreign
 from sqlalchemy.sql import func
 from database import Base
 
@@ -28,7 +28,12 @@ class User(Base):
     updated_at = Column(DateTime(timezone=True), onupdate=func.now())
     
     # Relations
-    natal_chart = relationship("NatalChart", back_populates="user", uselist=False)
+    natal_chart = relationship(
+        "NatalChart",
+        back_populates="user",
+        uselist=False,
+        primaryjoin="User.id == foreign(NatalChart.user_id_int)"
+    )
     lunar_returns = relationship("LunarReturn", back_populates="user", cascade="all, delete-orphan")
```

---

## 🧪 Validation

### 1. Vérifier la syntaxe Python

```bash
cd apps/api
python3 -m py_compile models/user.py models/natal_chart.py
```

### 2. Vérifier l'import de l'app (pas d'erreur AmbiguousForeignKeysError)

```bash
cd apps/api
python3 -c "from main import app; print('✅ App importée OK')"
```

**Résultat attendu:** `✅ App importée OK - pas d'erreur AmbiguousForeignKeysError`

### 3. Démarrer uvicorn

```bash
cd apps/api
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

**Résultat attendu:** Le serveur démarre sans erreur `AmbiguousForeignKeysError`

### 4. Tester l'endpoint `/api/auth/login`

```bash
# Test login
curl -X POST http://127.0.0.1:8000/api/auth/login \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=test@example.com&password=password123"
```

**Résultat attendu:** HTTP 200 avec JSON contenant `access_token` :

```json
{
  "access_token": "eyJhbGci...",
  "token_type": "bearer"
}
```

### 5. Test complet avec token (optionnel)

```bash
# Login et récupérer le token
TOKEN=$(curl -s -X POST http://127.0.0.1:8000/api/auth/login \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=test@example.com&password=password123" \
  | jq -r '.access_token')

echo "Token: $TOKEN"

# Tester /api/auth/me
curl -X GET http://127.0.0.1:8000/api/auth/me \
  -H "Authorization: Bearer $TOKEN"
```

**Résultat attendu:** HTTP 200 avec les données utilisateur (y compris `natal_chart` si présent)

---

## 📝 Notes techniques

### Pourquoi `primaryjoin` au lieu de `foreign_keys` ?

- **Côté "many" (NatalChart)** : On utilise `foreign_keys=[user_id_int]` car la clé étrangère est locale
- **Côté "one" (User)** : On utilise `primaryjoin` car on doit référencer une colonne de l'autre table (`NatalChart.user_id_int`)

### Compatibilité avec SQLAlchemy async

La syntaxe `primaryjoin="User.id == foreign(NatalChart.user_id_int)"` est compatible avec SQLAlchemy async. L'expression est évaluée au moment de la configuration des modèles, pas lors de l'exécution des requêtes.

### Relation legacy `user_id`

La colonne legacy `user_id` reste dans le modèle mais n'est plus utilisée par la relation. Elle peut être supprimée de la DB après migration complète des données vers `user_id_int`.

---

## ✅ Statut

**Problème résolu** ✅

L'erreur `AmbiguousForeignKeysError` ne se produit plus. SQLAlchemy utilise maintenant explicitement `natal_charts.user_id_int` pour la relation `User.natal_chart`.

### Vérifications effectuées

- [x] Syntaxe Python valide
- [x] Aucune erreur de linter
- [x] Import de l'app sans erreur `AmbiguousForeignKeysError`
- [x] Relation `User.natal_chart` utilise `user_id_int`
- [x] Relation `NatalChart.user` utilise `user_id_int` (déjà fait précédemment)
- [x] Cohérence entre les deux côtés de la relation

