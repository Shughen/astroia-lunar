# Astroia Lunar MVP - Guide de développement

## 🚀 Démarrage rapide

### Prérequis
- Node.js 18+ / npm
- Python 3.11+
- PostgreSQL 14+
- Expo CLI (`npm install -g expo-cli`)

---

## 📁 Structure du monorepo

```
astroia-lunar/
├── apps/
│   ├── mobile/     # Expo/React Native app
│   └── api/        # FastAPI backend
└── README_MVP.md   # Ce fichier
```

---

## 🔧 Configuration DEV

### 1. API Backend (FastAPI)

**Fichier** : `apps/api/.env`

```env
DATABASE_URL=postgresql://user@localhost:5432/astroia_lunar
SECRET_KEY=<généré via openssl rand -hex 32>
APP_ENV=development

# DEV FLAGS (obligatoires pour le MVP)
DEV_AUTH_BYPASS=1
ALLOW_DEV_PURGE=1
DEV_MOCK_EPHEMERIS=1
DEV_USER_ID=550e8400-e29b-41d4-a716-446655440000

# RapidAPI (si DEV_MOCK_EPHEMERIS=0)
RAPIDAPI_KEY=<votre clé>
RAPIDAPI_HOST=best-astrology-api-natal-charts-transits-synastry.p.rapidapi.com
```

**Lancer l'API** :
```bash
cd apps/api
source .venv/bin/activate  # ou créer venv : python3 -m venv .venv
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Vérifier** : [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

### 2. Mobile App (Expo)

**Fichier** : `apps/mobile/.env`

```env
EXPO_PUBLIC_API_URL=http://192.168.0.150:8000
EXPO_PUBLIC_DEV_AUTH_BYPASS=true
EXPO_PUBLIC_DEV_USER_ID=550e8400-e29b-41d4-a716-446655440000
```

**⚠️ IMPORTANT** : Remplacez `192.168.0.150` par **l'IP LAN de votre Mac** (trouvable via `ifconfig en0 | grep inet`)

**Lancer l'app** :
```bash
cd apps/mobile
npm install
npx expo start
```

Puis scanner le QR code avec Expo Go (iOS/Android).

---

## 🧪 Tests MVP

### Test 1 : Purge dev + création lunar return

```bash
cd apps/api
chmod +x scripts/test_dev_purge.sh
./scripts/test_dev_purge.sh
```

**Expected** :
- 1er appel : `deleted_count: N` (N = nombre de lunar returns existants)
- 2ème appel : `deleted_count: 0` (idempotence OK)

---

### Test 2 : Onboarding flow (mobile)

**Fresh install** :
1. Ouvrir Expo Go
2. Vérifier logs :
   ```
   [INDEX] ⏳ Hydratation en cours...
   [INDEX] ✅ Hydratation terminée
   [INDEX] → Redirection /welcome
   ```
3. Compléter onboarding (welcome → consent → profile → disclaimer → slides)
4. Arriver sur home `🌙 Rituel Lunaire`

**Re-open app** :
1. Kill app (swipe up sur iOS/Android)
2. Relancer
3. Vérifier logs :
   ```
   [INDEX] ✅ Hydraté: hasCompletedOnboarding=true
   [INDEX] ✅ Tous les guards passés → Home
   ```
4. **Attendu** : Pas de retour sur `/welcome`, reste sur home

---

### Test 3 : Purge + refetch (mobile + API)

```bash
# Terminal 1 : Purge API
cd apps/api
./scripts/test_dev_purge.sh

# Terminal 2 : Observer logs mobile
# L'app devrait refetch les lunar returns (vides après purge)
```

---

## 🐛 Troubleshooting

### Problème : "Network Error" sur mobile

**Cause** : `EXPO_PUBLIC_API_URL` pointe sur `localhost` au lieu de l'IP LAN.

**Fix** :
```bash
# 1. Trouver IP LAN
ifconfig en0 | grep "inet " | awk '{print $2}'
# Ex: 192.168.0.150

# 2. Mettre à jour apps/mobile/.env
EXPO_PUBLIC_API_URL=http://192.168.0.150:8000

# 3. Restart Expo
npx expo start --clear
```

---

### Problème : "/dev/purge renvoie 404"

**Cause** : `ALLOW_DEV_PURGE=1` manquant dans `apps/api/.env`.

**Fix** :
```bash
# apps/api/.env
ALLOW_DEV_PURGE=1
DEV_AUTH_BYPASS=1

# Restart API
uvicorn main:app --reload
```

---

### Problème : "Onboarding loop (revient sur /welcome)"

**Cause** : Ancienne version du code (avant patch hydratation Zustand).

**Fix** : Vérifier que [apps/mobile/app/index.tsx](apps/mobile/app/index.tsx#L40-L46) contient :
```ts
const isOnboardingHydrated = useOnboardingStore((state) => state.hydrated);
const hasSeenWelcomeScreen = useOnboardingStore((state) => state.hasSeenWelcomeScreen);
// ... etc (subscribe explicite via selectors)
```

---

## 📊 User DEV standardisé

**UUID unique** : `550e8400-e29b-41d4-a716-446655440000`

**Utilisé par** :
- Mobile : Header `X-Dev-External-Id`
- API : `DEV_USER_ID` env var
- Scripts : curl `-H "X-Dev-External-Id: 550e8400..."`

**Cohérence** : Tous les environnements utilisent le même UUID → même utilisateur dans la DB.

---

## 🎯 Checklist MVP

- [x] DEV_AUTH_BYPASS configuré (mobile + API)
- [x] User UUID standardisé (550e8400...)
- [x] Onboarding hydratation fixée (subscribe Zustand explicite)
- [x] /dev/purge idempotent (200 + deleted_count=0 si vide)
- [x] Fresh install → onboarding complet → home
- [x] Re-open app → reste sur home (pas de loop)
- [x] Purge dev → refetch OK

---

## 🔗 Liens utiles

- API Docs : [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Expo DevTools : Accessible via terminal après `npx expo start`
- Logs mobile : Visible dans Expo DevTools ou `npx expo start --tunnel`

---

## 📝 Notes

- **Ne jamais commiter les `.env`** : Utiliser `.env.example` comme template
- **DEV flags** : Uniquement pour développement local, désactiver en prod
- **Migration AsyncStorage** : Le store gère automatiquement la migration des anciennes clés (`hasSeenWelcome` → `hasSeenWelcomeScreen`)

---

**Version** : MVP v1.0 (2026-01-02)
