# ✅ DEV_AUTH_BYPASS - Résumé des modifications

## 📝 Fichiers modifiés

### 1. `services/api.ts`

**Modifications :**
- ✅ Configuration BaseURL avec fallbacks iOS/Android
- ✅ Détection du mode `EXPO_PUBLIC_DEV_AUTH_BYPASS === "true"`
- ✅ Ajout du header `X-Dev-User-Id` en mode bypass (au lieu de `Authorization Bearer`)
- ✅ Export des fonctions `isDevAuthBypassActive()` et `getDevUserId()` pour l'UI

**BaseURL :**
- Si `EXPO_PUBLIC_API_URL` défini → utilise cette valeur
- Sinon :
  - iOS Simulator → `http://127.0.0.1:8000`
  - Android Emulator → `http://10.0.2.2:8000`
  - Autre → `http://localhost:8000`

**Intercepteur axios :**
```typescript
if (DEV_AUTH_BYPASS) {
  config.headers['X-Dev-User-Id'] = DEV_USER_ID;
  // PAS de Authorization Bearer
} else {
  const token = await AsyncStorage.getItem('auth_token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
}
```

---

### 2. `app/index.tsx`

**Modifications :**
- ✅ Import de `isDevAuthBypassActive` et `getDevUserId`
- ✅ Label discret "DEV AUTH BYPASS (user_id=X)" sous le titre
- ✅ Bypass de l'écran de login si mode bypass actif
- ✅ Chargement des données même sans `isAuthenticated` si mode bypass actif

**Label ajouté :**
```tsx
{isDevAuthBypassActive() && (
  <Text style={styles.devBypassLabel}>
    DEV AUTH BYPASS (user_id={getDevUserId()})
  </Text>
)}
```

**Logique d'affichage :**
```tsx
// Afficher le contenu principal si authentifié OU si bypass actif
if (!isAuthenticated && !isDevAuthBypassActive()) {
  return <LoginScreen />;
}
```

---

### 3. `README-MOBILE.md`

**Ajouts :**
- ✅ Documentation des variables d'environnement (`EXPO_PUBLIC_DEV_AUTH_BYPASS`, `EXPO_PUBLIC_DEV_USER_ID`)
- ✅ Explication des fallbacks BaseURL (iOS/Android)
- ✅ Instructions pour lancer le backend en mode DEV_AUTH_BYPASS

---

### 4. `DEV_AUTH_BYPASS_GUIDE.md` (NOUVEAU)

**Contenu :**
- ✅ Guide complet pour configurer et utiliser le mode bypass
- ✅ Étapes de test détaillées
- ✅ Section dépannage
- ✅ Différence avec le mode normal

---

## 🔧 Variables d'environnement

### Backend (`.env` dans `apps/api/`)

```env
APP_ENV=development
DEV_AUTH_BYPASS=true
```

### Mobile (`.env` dans `apps/mobile/`)

```env
EXPO_PUBLIC_DEV_AUTH_BYPASS=true
EXPO_PUBLIC_DEV_USER_ID=1
EXPO_PUBLIC_API_URL=http://127.0.0.1:8000  # Optionnel
```

---

## ✅ Checklist de validation

- [x] `services/api.ts` : BaseURL avec fallbacks iOS/Android
- [x] `services/api.ts` : Header `X-Dev-User-Id` en mode bypass
- [x] `services/api.ts` : Pas de `Authorization Bearer` en mode bypass
- [x] `app/index.tsx` : Label "DEV AUTH BYPASS" affiché
- [x] `app/index.tsx` : Bypass de l'écran de login
- [x] `app/index.tsx` : Chargement des données sans authentification
- [x] Documentation mise à jour (`README-MOBILE.md`)
- [x] Guide complet créé (`DEV_AUTH_BYPASS_GUIDE.md`)

---

## 🚀 Étapes pour lancer et tester

### 1. Backend

```bash
cd apps/api
APP_ENV=development DEV_AUTH_BYPASS=true uvicorn main:app --reload --port 8000
```

### 2. Mobile

```bash
cd apps/mobile

# Créer .env
cat > .env << EOF
EXPO_PUBLIC_DEV_AUTH_BYPASS=true
EXPO_PUBLIC_DEV_USER_ID=1
EXPO_PUBLIC_API_URL=http://127.0.0.1:8000
EOF

# Lancer Expo
npx expo start
```

### 3. Tester

1. **Ouvrir l'app** (Expo Go ou simulateur)
2. **Vérifier** :
   - ✅ Label "DEV AUTH BYPASS (user_id=1)" visible sur Home
   - ✅ Pas d'écran de login
   - ✅ Contenu principal affiché directement
3. **Tester les fonctionnalités** :
   - ✅ "Générer mes retours" → génère les 12 retours
   - ✅ "Voir timeline" → affiche la liste des retours
   - ✅ Prochain retour s'affiche après génération

---

## 📊 Différence avec le mode normal

| Aspect | Normal | DEV_AUTH_BYPASS |
|--------|--------|-----------------|
| Login requis | ✅ | ❌ |
| Header auth | `Authorization: Bearer <token>` | `X-Dev-User-Id: 1` |
| Label Home | ❌ | ✅ "DEV AUTH BYPASS (user_id=X)" |
| Backend config | Standard | `DEV_AUTH_BYPASS=true` |
| Sécurité | Production-ready | Development uniquement |

---

## ⚠️ Important

- **Ne jamais activer en production**
- **Backend et mobile doivent être synchronisés** (tous deux avec bypass activé)
- **User ID doit exister en DB** (vérifier que l'utilisateur avec l'ID configuré existe)

---

**Toutes les modifications sont complètes et prêtes à être testées !** 🌙✨

