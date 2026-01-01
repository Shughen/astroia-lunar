# 🔧 Guide DEV_AUTH_BYPASS - Tester le MVP sans login

## 🎯 Objectif

Permet de tester rapidement l'app mobile avec le backend local **sans créer de compte ni se connecter**, idéal pour le développement et la validation du MVP.

---

## 📋 Prérequis

1. ✅ Backend FastAPI lancé avec `DEV_AUTH_BYPASS=true`
2. ✅ App mobile configurée avec les variables d'environnement
3. ✅ Un utilisateur avec `user_id=1` existe en base de données (ou changer `EXPO_PUBLIC_DEV_USER_ID`)

---

## 🚀 Configuration

### 1. Backend (FastAPI)

Lancer le backend avec les variables d'environnement :

```bash
cd apps/api
APP_ENV=development DEV_AUTH_BYPASS=true uvicorn main:app --reload --port 8000
```

**Vérifier que ça fonctionne :**
```bash
# Devrait retourner 200 avec le header X-Dev-User-Id
curl -X GET "http://localhost:8000/api/lunar-returns/next" \
  -H "X-Dev-User-Id: 1"
```

### 2. Mobile (Expo)

Créer ou mettre à jour `.env` dans `apps/mobile/` :

```env
# URL du backend (optionnel, avec fallbacks automatiques)
EXPO_PUBLIC_API_URL=http://127.0.0.1:8000

# Mode DEV_AUTH_BYPASS
EXPO_PUBLIC_DEV_AUTH_BYPASS=true
EXPO_PUBLIC_DEV_USER_ID=1
```

**Fallbacks automatiques si `EXPO_PUBLIC_API_URL` n'est pas défini :**
- iOS Simulator : `http://127.0.0.1:8000`
- Android Emulator : `http://10.0.2.2:8000`
- Autre : `http://localhost:8000`

---

## ✅ Vérification

### 1. Label sur l'écran Home

Quand le mode DEV_AUTH_BYPASS est actif, un label discret s'affiche sous le titre :

```
🌙 Lunation
Ton tableau de bord astrologique
DEV AUTH BYPASS (user_id=1)
```

### 2. Appels API

En mode DEV_AUTH_BYPASS, tous les appels API incluent automatiquement :
- Header `X-Dev-User-Id: 1` (ou la valeur de `EXPO_PUBLIC_DEV_USER_ID`)
- **PAS** de header `Authorization: Bearer <token>`

### 3. Accès direct au contenu

L'écran Home s'affiche directement **sans écran de login**, même si `isAuthenticated === false`.

---

## 🧪 Étapes de test complètes

### Étape 1 : Lancer le backend

```bash
cd apps/api
APP_ENV=development DEV_AUTH_BYPASS=true uvicorn main:app --reload --port 8000
```

**Attendre :**
- `✅ Schema sanity check passed`
- `Uvicorn running on http://0.0.0.0:8000`

### Étape 2 : Configurer l'app mobile

```bash
cd apps/mobile

# Créer .env si nécessaire
cat > .env << EOF
EXPO_PUBLIC_DEV_AUTH_BYPASS=true
EXPO_PUBLIC_DEV_USER_ID=1
EXPO_PUBLIC_API_URL=http://127.0.0.1:8000
EOF
```

### Étape 3 : Lancer Expo

```bash
npx expo start
```

### Étape 4 : Ouvrir l'app

- Scanner le QR code avec Expo Go (iOS/Android)
- Ou appuyer sur `i` pour iOS Simulator
- Ou appuyer sur `a` pour Android Emulator

### Étape 5 : Valider

1. **Home screen** :
   - ✅ Label "DEV AUTH BYPASS (user_id=1)" visible
   - ✅ Pas d'écran de login
   - ✅ Affichage direct du contenu principal

2. **Prochain retour lunaire** :
   - ✅ Si aucun retour : bouton "Générer mes retours"
   - ✅ Si retours existent : affichage du prochain avec date et jours restants

3. **Générer les retours** :
   - ✅ Cliquer sur "Générer mes retours"
   - ✅ Attendre la génération (peut prendre 30-60 secondes)
   - ✅ Le prochain retour s'affiche automatiquement après génération

4. **Timeline** :
   - ✅ Cliquer sur "Voir timeline"
   - ✅ Liste des 12 retours de l'année en cours
   - ✅ Badges de statut : PASSÉ / AUJOURD'HUI / À VENIR

---

## 🐛 Dépannage

### Erreur "Impossible de valider les identifiants"

**Cause :** Le backend n'a pas `DEV_AUTH_BYPASS=true` ou `APP_ENV=development`.

**Solution :**
```bash
# Vérifier les variables d'environnement du backend
echo $DEV_AUTH_BYPASS  # Devrait être "true"
echo $APP_ENV          # Devrait être "development"
```

### Erreur réseau / timeout

**Causes possibles :**

1. **Backend non lancé** : Vérifier `http://localhost:8000/health`
2. **URL incorrecte** :
   - iOS Simulator : utiliser `http://127.0.0.1:8000` (pas `localhost`)
   - Android Emulator : utiliser `http://10.0.2.2:8000`
3. **Firewall / proxy** : Désactiver temporairement

### Label "DEV AUTH BYPASS" non affiché

**Cause :** `EXPO_PUBLIC_DEV_AUTH_BYPASS` n'est pas défini ou vaut autre chose que `"true"`.

**Solution :**
```bash
# Vérifier dans .env
cat .env | grep DEV_AUTH_BYPASS  # Devrait être "true"

# Redémarrer Expo après modification de .env
# (Expo charge les variables au démarrage)
```

### User non trouvé (404)

**Cause :** L'utilisateur avec `user_id=1` n'existe pas en base de données.

**Solutions :**

1. **Créer l'utilisateur** :
   ```sql
   INSERT INTO users (id, email, hashed_password, created_at)
   VALUES (1, 'dev@test.com', '$2b$12$...', NOW());
   ```

2. **Utiliser un autre user_id** :
   ```env
   EXPO_PUBLIC_DEV_USER_ID=2
   ```

---

## 📝 Différence avec le mode normal

| Aspect | Mode Normal | Mode DEV_AUTH_BYPASS |
|--------|-------------|---------------------|
| **Login requis** | ✅ Oui | ❌ Non |
| **Token JWT** | ✅ Oui (`Authorization: Bearer`) | ❌ Non |
| **Header utilisé** | `Authorization` | `X-Dev-User-Id` |
| **Backend config** | Standard | `DEV_AUTH_BYPASS=true` |
| **Label Home** | ❌ Non | ✅ "DEV AUTH BYPASS (user_id=X)" |
| **Sécurité** | ✅ Production-ready | ❌ Development uniquement |

---

## ⚠️ Important

- **Ne jamais activer en production** : `DEV_AUTH_BYPASS` est uniquement pour le développement local
- **Backend et mobile doivent être synchronisés** : Les deux doivent avoir le mode activé
- **User ID doit exister** : Vérifier que l'utilisateur avec l'ID configuré existe en DB

---

## 🎉 Résultat attendu

Après avoir suivi ces étapes :

1. ✅ L'app s'ouvre directement sur l'écran Home (pas de login)
2. ✅ Le label "DEV AUTH BYPASS" est visible
3. ✅ Les appels API fonctionnent avec le header `X-Dev-User-Id`
4. ✅ Home affiche le prochain retour lunaire (après génération)
5. ✅ Timeline affiche tous les retours de l'année
6. ✅ Génération des retours fonctionne correctement

---

**Développé avec 🌙 par l'équipe Lunation**

