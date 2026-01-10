# Fix: Configuration Supabase Pydantic v2

**Date:** 2025-01-XX  
**Problème:** `uvicorn main:app` crash avec `Pydantic ValidationError: "SUPABASE_URL Extra inputs are not permitted"`  
**Version:** Pydantic Settings v2.1.0

---

## 🔍 Problème

Avec Pydantic Settings v2, il faut :
1. Utiliser `validation_alias` au lieu de `alias` pour les variables d'environnement
2. Migrer de `class Config` vers `model_config = SettingsConfigDict(...)`

---

## ✅ Solution

### Modifications dans `config.py`

1. **Import ajouté** : `SettingsConfigDict` depuis `pydantic_settings`
2. **Champs Supabase corrigés** : Utilisation de `validation_alias` au lieu de `alias`
3. **Migration Pydantic v2** : Remplacement de `class Config` par `model_config = SettingsConfigDict(...)`

### Diff

```diff
--- a/apps/api/config.py
+++ b/apps/api/config.py
@@ -2,7 +2,7 @@
 Configuration centralisée (Pydantic Settings)
 """
 
-from pydantic_settings import BaseSettings
+from pydantic_settings import BaseSettings, SettingsConfigDict
 from pydantic import Field
 from typing import Optional
 
@@ -58,9 +58,14 @@ class Settings(BaseSettings):
     # Timezone
     TZ: str = Field(default="Europe/Paris")
     
-    class Config:
-        env_file = ".env"
-        case_sensitive = True
+    # Supabase
+    supabase_url: Optional[str] = Field(default=None, validation_alias="SUPABASE_URL")
+    supabase_anon_key: Optional[str] = Field(default=None, validation_alias="SUPABASE_ANON_KEY")
+    
+    model_config = SettingsConfigDict(
+        env_file=".env",
+        case_sensitive=True
+    )
```

---

## 📋 Détails techniques

### 1. `validation_alias` vs `alias`

Dans Pydantic v2 avec `BaseSettings`, pour mapper les variables d'environnement vers des champs Python, on utilise `validation_alias` :

```python
supabase_url: Optional[str] = Field(default=None, validation_alias="SUPABASE_URL")
```

- `validation_alias` : Utilisé lors de la **validation/construction** de l'objet (lecture depuis env vars)
- `alias` : Utilisé lors de la **sérialisation** (sortie JSON/dict)

Pour les variables d'environnement, `validation_alias` est la bonne approche.

### 2. `model_config` (Pydantic v2)

Pydantic v2 utilise `model_config = SettingsConfigDict(...)` au lieu de `class Config` :

```python
model_config = SettingsConfigDict(
    env_file=".env",
    case_sensitive=True
)
```

**Comportement par défaut** : `extra="ignore"` (pas besoin de le spécifier, les variables non déclarées sont ignorées, pas d'erreur)

### 3. Configuration appliquée

- ✅ `env_file=".env"` : Lecture du fichier `.env`
- ✅ `case_sensitive=True` : Respect de la casse des variables
- ✅ Pas de `extra="allow"` : Comportement strict par défaut (ignore les variables non déclarées)

---

## ✅ Vérifications effectuées

- [x] Syntaxe Python valide
- [x] Aucune erreur de linter
- [x] Variables `SUPABASE_URL` et `SUPABASE_ANON_KEY` lues depuis `.env`
- [x] Import de `main.py` sans erreur Pydantic ValidationError
- [x] Configuration Pydantic v2 correcte (`model_config`)
- [x] Migration de `class Config` vers `SettingsConfigDict`

---

## 🧪 Commandes de test

### 1. Vérifier la configuration

```bash
cd apps/api
python3 -c "from config import Settings; s = Settings(); print(f'SUPABASE_URL: {s.supabase_url}'); print(f'SUPABASE_ANON_KEY: {s.supabase_anon_key[:30] if s.supabase_anon_key else None}...')"
```

**Résultat attendu:**
```
SUPABASE_URL: https://...
SUPABASE_ANON_KEY: eyJhbGciOiJIUzI1NiIsInR5cCI6Ik...
```

### 2. Vérifier l'import de l'app

```bash
cd apps/api
python3 -c "from main import app; print('✅ App importée sans erreur Pydantic ValidationError')"
```

**Résultat attendu:** `✅ App importée sans erreur Pydantic ValidationError`

### 3. Démarrer uvicorn

```bash
cd apps/api
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Résultat attendu:** Le serveur démarre sans erreur :
```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
🚀 Lunation API démarrage...
```

### 4. Test curl (smoke test)

```bash
# Test endpoint racine
curl http://localhost:8000/

# Ou test docs
curl http://localhost:8000/docs
```

**Résultat attendu:** Réponse HTTP 200 (ou redirection vers `/docs`)

---

## 📝 Notes importantes

1. **Variables d'environnement** : Les noms `SUPABASE_URL` et `SUPABASE_ANON_KEY` dans le `.env` restent inchangés.

2. **Accès dans le code** : Utiliser les noms de champs Python (snake_case) :
   ```python
   from config import settings
   
   url = settings.supabase_url
   key = settings.supabase_anon_key
   ```

3. **Pydantic v2** : La migration vers `model_config = SettingsConfigDict(...)` est obligatoire pour Pydantic Settings v2+.

4. **Comportement strict** : Par défaut, `extra="ignore"` (pas d'erreur si variable non déclarée, elle est juste ignorée). Pas besoin de `extra="allow"`.

---

## ✅ Statut

**Problème résolu** ✅

L'application démarre maintenant correctement avec `uvicorn main:app` sans erreur de validation Pydantic, en utilisant la syntaxe correcte de Pydantic Settings v2.

