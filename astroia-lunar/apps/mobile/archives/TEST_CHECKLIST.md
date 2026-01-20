# 📋 Checklist de Test Manuel - 3 Flows Critiques

## 🔧 Prérequis

- [ ] Backend API démarré et accessible (vérifier `http://localhost:8000/health` ou l'URL configurée)
- [ ] App mobile démarrée (Expo Go ou simulateur)
- [ ] Console React Native ouverte (Metro bundler terminal)
- [ ] DevTools réseau activés (si disponible sur la plateforme)

**Variables d'environnement à vérifier :**
- `EXPO_PUBLIC_API_URL` (si défini, vérifier qu'elle pointe vers le backend)
- `EXPO_PUBLIC_DEV_AUTH_BYPASS` (optionnel, pour bypass auth)

---

## 1️⃣ Flow: debug/selftest - Register/Login

### 📍 Navigation
- [ ] Aller sur `/debug/selftest` (route manuelle, non dans la nav principale)
- [ ] Vérifier que l'écran s'affiche avec :
  - [ ] Titre "🧪 Auth Self-Test"
  - [ ] API URL affichée (carte info)
  - [ ] Bouton "Run Auth E2E" visible

### ✅ Test Success Path

**Étape 1 : Health Check**
- [ ] Cliquer sur "Run Auth E2E"
- [ ] Vérifier que "Health Check" passe (✅ vert)
- [ ] **Console logs à vérifier :**
  - `🔗 API BaseURL: ...` (doit afficher l'URL correcte)
  - `[API] Token JWT ajouté...` ou `[API] Mode DEV_AUTH_BYPASS actif...`

**Étape 2 : Register**
- [ ] Vérifier que "Register" passe (✅ vert)
- [ ] Vérifier qu'un token est affiché (truncated, ~40 premiers caractères)
- [ ] **Console logs à vérifier :**
  - `[SELFTEST] Register payload: ...` (sans password)
  - `[SELFTEST] Register endpoint: POST /api/auth/register`
  - `[Auth] Token reçu: ...`
  - `[Auth] Token stocké dans AsyncStorage`
- [ ] **Network à vérifier :**
  - Requête `POST /api/auth/register` avec status `200` ou `201`
  - Response contient `access_token`

**Étape 3 : Login**
- [ ] Vérifier que "Login" passe (✅ vert)
- [ ] Vérifier que le token est mis à jour
- [ ] **Console logs à vérifier :**
  - `[SELFTEST] Login payload: ...` (sans password)
  - `[SELFTEST] Login endpoint: POST /api/auth/login (form-urlencoded)`
  - `[Auth] Token reçu: ...`
- [ ] **Network à vérifier :**
  - Requête `POST /api/auth/login` avec `Content-Type: application/x-www-form-urlencoded`
  - Status `200`
  - Response contient `access_token`

**Étape 4 : Get Me**
- [ ] Vérifier que "Get Me" passe (✅ vert)
- [ ] Vérifier que l'email correspond à celui créé (`test-{timestamp}@selftest.local`)
- [ ] **Console logs à vérifier :**
  - Pas d'erreur `[API] ⚠️ Aucun token trouvé`
- [ ] **Network à vérifier :**
  - Requête `GET /api/auth/me` avec header `Authorization: Bearer {token}`
  - Status `200`
  - Response contient `email` et `id`

### ❌ Test Error Path

**Scénario 1 : Backend non accessible**
- [ ] Arrêter le backend
- [ ] Cliquer sur "Run Auth E2E"
- [ ] **Vérifier que l'app ne crash pas**
- [ ] Vérifier que "Health Check" affiche une erreur lisible :
  - [ ] Message d'erreur visible (pas juste "Error" ou crash)
  - [ ] Détails de l'erreur affichés (ex: "Network error", "ECONNREFUSED")
- [ ] **Console logs à capturer :**
  - Tous les `[SELFTEST]` logs
  - Tous les `[API]` logs
  - Erreurs `console.error`
- [ ] **Network à capturer :**
  - Screenshot de l'erreur réseau (si DevTools disponible)
  - Status code (si disponible)

**Scénario 2 : Erreur 422 (Validation)**
- [ ] Modifier temporairement le code pour envoyer des données invalides
- [ ] Cliquer sur "Run Auth E2E"
- [ ] **Vérifier que l'erreur est lisible :**
  - [ ] Message commence par "422 Validation Error:"
  - [ ] Détails des champs invalides affichés (ex: `- birth_date: required`)
- [ ] **Console logs à capturer :**
  - `[SELFTEST] Register error: { status: 422, ... }`
  - `errorData.detail` complet

**Scénario 3 : Erreur 401 (Login failed)**
- [ ] Utiliser un email/mot de passe incorrect
- [ ] Cliquer sur "Run Auth E2E"
- [ ] **Vérifier que l'erreur est lisible :**
  - [ ] Message commence par "401 Unauthorized:"
  - [ ] Détails de l'erreur affichés
- [ ] **Console logs à capturer :**
  - `[SELFTEST] Login error: { status: 401, ... }`

### 📸 Captures à faire si échec

1. **Screenshot de l'écran** avec l'erreur affichée
2. **Console logs complets** (copier/coller depuis Metro bundler)
3. **Network request/response** (si DevTools disponible) :
   - URL complète
   - Headers (surtout `Authorization` si présent)
   - Request body
   - Response status + body
4. **État de l'app** :
   - L'app crash-t-elle ? (red screen)
   - L'app freeze-t-elle ?
   - L'erreur est-elle affichée mais illisible ?

---

## 2️⃣ Flow: transits/overview - getOverview

### 📍 Prérequis spécifiques
- [ ] **Authentification requise** (sauf si `DEV_AUTH_BYPASS=true`)
- [ ] Vérifier que l'utilisateur est connecté OU que `EXPO_PUBLIC_DEV_AUTH_BYPASS=true` et `EXPO_PUBLIC_DEV_USER_ID=1` (ou ID valide)

### 📍 Navigation
- [ ] Aller sur `/transits/overview`
- [ ] Vérifier que l'écran s'affiche avec :
  - [ ] Header "🔄 Transits du Mois"
  - [ ] Pas de crash au chargement

### ✅ Test Success Path

**Étape 1 : Chargement initial**
- [ ] Vérifier que le loader s'affiche ("Chargement des transits...")
- [ ] Vérifier que les données s'affichent :
  - [ ] Badge "Niveau d'énergie" (Élevé/Modéré/Calme)
  - [ ] Section "💡 Points Clés" (si données disponibles)
  - [ ] Section "⭐ Aspects Majeurs" (si données disponibles)
- [ ] **Console logs à vérifier :**
  - Pas d'erreur `[TransitsOverview] Erreur chargement`
  - Pas d'erreur `Utilisateur non authentifié`
- [ ] **Network à vérifier :**
  - Requête `GET /api/transits/overview/{userId}/{month}` (format: `YYYY-MM`)
  - Header `Authorization: Bearer {token}` présent (sauf si DEV_AUTH_BYPASS)
  - Status `200`
  - Response contient `summary.insights` et `summary.energy_level`

**Étape 2 : Affichage des aspects**
- [ ] Si des aspects sont présents, vérifier :
  - [ ] Badges colorés corrects (▲ Trigone vert, ■ Carré rouge, etc.)
  - [ ] Titre de l'aspect (ex: "Mars square Venus")
  - [ ] Orbe affiché
  - [ ] Interprétation affichée (si disponible)
- [ ] Cliquer sur un aspect
- [ ] Vérifier la navigation vers `/transits/details` (si implémenté)

### ❌ Test Error Path

**Scénario 1 : Non authentifié**
- [ ] Se déconnecter (ou désactiver DEV_AUTH_BYPASS)
- [ ] Aller sur `/transits/overview`
- [ ] **Vérifier que l'erreur est lisible :**
  - [ ] Message "Vous devez être connecté pour voir les transits"
  - [ ] Pas de crash
- [ ] **Console logs à capturer :**
  - `[TransitsOverview] Erreur chargement:` avec détails
  - Message "Utilisateur non authentifié" si présent

**Scénario 2 : Backend non accessible**
- [ ] Arrêter le backend
- [ ] Aller sur `/transits/overview`
- [ ] **Vérifier que l'app ne crash pas**
- [ ] Vérifier que l'erreur est affichée :
  - [ ] Message d'erreur visible
  - [ ] Bouton "Réessayer" présent
- [ ] Cliquer sur "Réessayer"
- [ ] Vérifier que le loader s'affiche
- [ ] **Console logs à capturer :**
  - `[TransitsOverview] Erreur chargement: ...`
  - Message d'erreur réseau complet
- [ ] **Network à capturer :**
  - Status code de l'erreur

**Scénario 3 : Erreur 404 ou 500**
- [ ] Simuler une erreur backend
- [ ] Aller sur `/transits/overview`
- [ ] **Vérifier que l'erreur est lisible :**
  - [ ] Message d'erreur affiché (pas de crash)
  - [ ] Détails de l'erreur (ex: `err.response?.data?.detail`)
  - [ ] Bouton "Réessayer" fonctionne
- [ ] **Console logs à capturer :**
  - `[TransitsOverview] Erreur chargement:` avec `err.response?.status` et `err.response?.data`

**Scénario 4 : Réponse vide**
- [ ] Simuler une réponse `null` ou `{}`
- [ ] Vérifier que l'app gère l'erreur :
  - [ ] Message "Aucune donnée disponible" ou "Réponse vide du serveur"
  - [ ] Bouton "Réessayer" présent
- [ ] **Console logs à capturer :**
  - `[TransitsOverview] Erreur chargement:` avec détails

### 📸 Captures à faire si échec

1. **Screenshot de l'écran** avec l'erreur
2. **Console logs complets** :
   - Tous les `[TransitsOverview]` logs
   - Erreurs `console.error`
3. **Network request/response** :
   - URL complète avec `userId` et `month`
   - Headers (surtout `Authorization`)
   - Response status + body
4. **État de l'app** :
   - Crash ? Freeze ? Erreur affichée ?
5. **État auth** :
   - `isAuthenticated` dans le store
   - Token présent dans AsyncStorage ?
   - DEV_AUTH_BYPASS actif ?

---

## 📊 Où regarder les logs

### Console React Native (Metro Bundler)
- **Terminal où Expo est lancé** (`npx expo start`)
- Chercher les préfixes :
  - `[SELFTEST]` pour selftest
  - `[TransitsOverview]` pour transits
  - `[API]` pour les appels API généraux
  - `[Auth]` pour l'authentification

### Network (si disponible)
- **React Native Debugger** (si activé)
- **Chrome DevTools** (si web ou remote debugging activé)
- **Flipper** (si configuré)
- Sinon, vérifier les logs backend directement

### Backend logs
- **Terminal où l'API est lancée** (uvicorn/fastapi)
- Chercher les requêtes :
  - `POST /api/auth/register`
  - `POST /api/auth/login`
  - `GET /api/auth/me`
  - `GET /api/transits/overview/{userId}/{month}`

---

## 🎯 Checklist finale

### Flow 1: selftest
- [ ] ✅ Success path complet (Health → Register → Login → Get Me)
- [ ] ❌ Error path testé (backend down, 422, 401)
- [ ] 📸 Captures faites si échec

### Flow 2: transits/overview
- [ ] ✅ Success path (chargement + affichage)
- [ ] ❌ Error path testé (non auth, backend down, 404/500, réponse vide)
- [ ] 📸 Captures faites si échec

---

## 📝 Notes importantes

1. **Pas de crash = succès** : Même si une erreur survient, l'app ne doit pas crasher (red screen)
2. **Erreurs lisibles** : Les messages d'erreur doivent être compréhensibles, pas juste "Error" ou des stack traces
3. **Boutons de retry** : Tous les écrans d'erreur doivent avoir un bouton "Réessayer" fonctionnel
4. **Logs détaillés** : Les console.log doivent contenir assez d'infos pour débugger (status codes, messages, payloads)

