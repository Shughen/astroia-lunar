# Fix: Configuration Supabase dans Pydantic Settings

**Date:** 2025-01-XX  
**Problème:** `uvicorn main:app` crash au démarrage avec `Pydantic ValidationError: "SUPABASE_URL Extra inputs are not permitted"`

---

## 🔍 Problème

Pydantic Settings rejetait les variables d'environnement `SUPABASE_URL` et `SUPABASE_ANON_KEY` présentes dans le `.env` car elles n'étaient pas déclarées dans le modèle `Settings`.

---

## ✅ Solution

Ajout explicite des deux champs manquants dans `Settings` avec des alias pour mapper vers les variables d'environnement.

### Modification dans `config.py`

```python
# Supabase
supabase_url: Optional[str] = Field(default=None, alias="SUPABASE_URL")
supabase_anon_key: Optional[str] = Field(default=None, alias="SUPABASE_ANON_KEY")
```

### Diff

```diff
--- a/apps/api/config.py
+++ b/apps/api/config.py
@@ -58,6 +58,10 @@ class Settings(BaseSettings):
     # Timezone
     TZ: str = Field(default="Europe/Paris")
     
+    # Supabase
+    supabase_url: Optional[str] = Field(default=None, alias="SUPABASE_URL")
+    supabase_anon_key: Optional[str] = Field(default=None, alias="SUPABASE_ANON_KEY")
+    
     class Config:
         env_file = ".env"
         case_sensitive = True
```

---

## 📋 Détails techniques

### 1. Champs ajoutés

- **`supabase_url`** : URL de l'instance Supabase (alias `SUPABASE_URL`)
- **`supabase_anon_key`** : Clé anonyme Supabase (alias `SUPABASE_ANON_KEY`)

### 2. Type et defaults

- Type : `Optional[str]` (peuvent être `None`)
- Default : `None` (optionnels, pour compatibilité)
- Alias : Les noms des variables d'environnement (`SUPABASE_URL`, `SUPABASE_ANON_KEY`)

### 3. Configuration Pydantic

- `env_file = ".env"` : Lecture du fichier `.env` ✅
- `case_sensitive = True` : Respect de la casse ✅
- `extra="ignore"` par défaut dans pydantic-settings : Les variables non déclarées sont ignorées (mais ici elles sont maintenant déclarées) ✅

---

## ✅ Vérifications effectuées

- [x] Syntaxe Python valide
- [x] Aucune erreur de linter
- [x] Variables lues depuis `.env` (testé avec `Settings()`)
- [x] Import de `main.py` sans erreur Pydantic ValidationError
- [x] Aucun autre champ modifié

---

## 🧪 Commandes de test

### 1. Vérifier la configuration

```bash
cd apps/api
python3 -c "from config import Settings; s = Settings(); print(f'SUPABASE_URL: {s.supabase_url}'); print(f'SUPABASE_ANON_KEY: {s.supabase_anon_key[:20]}...')"
```

**Résultat attendu:** Les valeurs depuis le `.env` sont affichées.

### 2. Vérifier l'import de l'app

```bash
cd apps/api
python3 -c "from main import app; print('✅ App importée sans erreur')"
```

**Résultat attendu:** `✅ App importée sans erreur` (pas de ValidationError).

### 3. Démarrer uvicorn

```bash
cd apps/api
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Résultat attendu:** Le serveur démarre sans erreur, affichage :
```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
🚀 Astroia Lunar API démarrage...
```

### 4. Test curl de l'API

```bash
curl http://localhost:8000/docs
```

**Résultat attendu:** Retourne la page Swagger UI.

**Ou tester un endpoint spécifique :**

```bash
curl http://localhost:8000/api/health
# ou
curl http://localhost:8000/
```

---

## 📝 Notes importantes

1. **Variables d'environnement dans `.env`** : Les noms `SUPABASE_URL` et `SUPABASE_ANON_KEY` restent inchangés (comme demandé).

2. **Accès aux valeurs** : Dans le code Python, utiliser :
   ```python
   from config import settings
   
   url = settings.supabase_url  # Nom du champ Python (snake_case)
   key = settings.supabase_anon_key  # Nom du champ Python (snake_case)
   ```

3. **Compatibilité** : Les champs sont optionnels (`Optional[str]` avec `default=None`), donc l'app fonctionne même si les variables ne sont pas définies dans le `.env`.

4. **Aucun refactoring global** : Seulement les 2 lignes ajoutées, aucun autre champ modifié.

---

## ✅ Statut

**Problème résolu** ✅

L'application démarre maintenant correctement avec `uvicorn main:app` sans erreur de validation Pydantic.

