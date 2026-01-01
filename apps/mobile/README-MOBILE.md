# 📱 Lunation - Application Mobile V1

**Version:** 1.0.0  
**Framework:** Expo SDK 54 + React Native  
**État:** ✅ V1 Complète et Opérationnelle

---

## 🎯 Écrans Créés (8 écrans)

### 1. 🏠 index.tsx - Accueil
Grille des 12 révolutions lunaires avec navigation

### 2. 🌙 lunar/index.tsx - Luna Pack Hub
Interface de test des 3 fonctionnalités Luna Pack

### 3. 📊 lunar/report.tsx - Rapport Lunaire Détaillé
Affichage du rapport mensuel complet

### 4. 🌑 lunar/voc.tsx - Void of Course (NOUVEAU)
- Badge en temps réel "VoC actif" / "Pas de VoC"
- Fenêtres VoC avec heures de début/fin
- Recommandations (à éviter / favorable)
- Refresh automatique toutes les 5 minutes
- Pull-to-refresh manuel

### 5. 📅 calendar/month.tsx - Calendrier Mensuel (NOUVEAU)
- Navigation mois précédent/suivant
- Cards résumé (nouvelles lunes, pleines lunes, éclipses, événements)
- Liste des événements lunaires du mois
- Phases lunaires avec emojis
- Bouton "Mansion du jour"

### 6. 🔄 transits/overview.tsx - Vue d'Ensemble Transits (NOUVEAU)
- Badge niveau d'énergie (Élevé/Modéré/Calme)
- 3-5 insights clés sous forme de bullet points
- Liste des aspects majeurs avec badges colorés :
  - ▲ Trigone (vert)
  - ■ Carré (rouge)
  - ◎ Conjonction (or)
  - ⬡ Sextile (bleu)
  - ◉ Opposition (violet)
- Navigation vers détails

### 7. ⭐ transits/details.tsx - Détails Transit (NOUVEAU)
- Visualisation d'un aspect spécifique
- Interprétation détaillée
- Timing (aspect exact + période d'influence)
- Thèmes associés (badges)
- Recommandations pratiques

### 8. ⚙️ settings/index.tsx - Paramètres (NOUVEAU)
- Toggle notifications VoC
- Ville par défaut
- Code pays par défaut
- Informations version/backend/provider

---

## 🧩 Composants Réutilisables (5 composants)

### 1. ✨ Card.tsx
Composant carte avec 3 variants :
- `default` - Fond violet classique
- `highlighted` - Fond violet accentué
- `dark` - Fond noir profond

**Usage:**
```tsx
<Card variant="highlighted">
  <Text>Contenu</Text>
</Card>
```

### 2. 🏷️ Badge.tsx
Badge avec 5 variants de couleur :
- `success` (vert)
- `warning` (jaune)
- `error` (rouge)
- `info` (bleu/violet)
- `gold` (or)

**Usage:**
```tsx
<Badge label="VoC Actif" emoji="🌑" variant="warning" />
```

### 3. 💀 Skeleton.tsx
Loader skeleton avec animation pulse

**Usage:**
```tsx
<Skeleton width={200} height={20} borderRadius={8} />
```

### 4. 🔍 JsonToggle.tsx
Affichage toggle de JSON brut (debug mode)

**Usage:**
```tsx
<JsonToggle data={responseData} title="Réponse API" />
```

### 5. 🔔 ErrorToast.tsx
Toast d'erreur non intrusif (auto-dismiss 3s)

**Usage:**
```tsx
<ErrorToast
  message="Erreur de chargement"
  visible={showError}
  onDismiss={() => setShowError(false)}
/>
```

---

## 🗄️ Stores Zustand (5 stores)

### 1. useAuthStore.ts (existant)
Authentification et profil utilisateur

### 2. useLunarStore.ts (existant)
Révolutions lunaires

### 3. useTransitsStore.ts (NOUVEAU)
Cache transits avec TTL 5 minutes
```ts
const { transitsData, isStale, setTransits } = useTransitsStore();
```

### 4. useCalendarStore.ts (NOUVEAU)
Cache calendar par mois avec TTL 5 minutes
```ts
const { getCalendar, setCalendar, isStale } = useCalendarStore();
```

### 5. useVocStore.ts (NOUVEAU)
Cache VoC avec TTL 5 minutes
```ts
const { vocData, isStale, setVoc } = useVocStore();
```

**Tous les stores incluent** :
- Cache avec TTL (5 minutes)
- Méthode `isStale()` pour vérifier la fraîcheur
- Gestion loading/error
- Méthode `clear()` pour reset

---

## 🎨 Système de Design

### Palette de Couleurs

```typescript
colors = {
  darkBg: ['#1a0b2e', '#2d1b4e'],      // Dégradé de fond
  cardBg: '#2a1a4e',                    // Cartes
  accent: '#b794f6',                    // Violet lunaire
  gold: '#ffd700',                      // Or mystique
  text: '#ffffff',                      // Texte principal
  textMuted: '#a0a0b0',                 // Texte secondaire
}
```

### Emojis Utilisés

| Type | Emoji | Usage |
|------|-------|-------|
| Phases | 🌑🌓🌕🌗 | Nouvelles/pleines lunes |
| Aspects | ▲■◎⬡◉ | Trigone, carré, conjonction, etc. |
| Status | ✅⚠️❌ | Success, warning, error |
| Features | 🌙🔄📅⚙️ | Lunar, transits, calendar, settings |

---

## 📡 Endpoints Consommés

### Luna Pack
- `GET /api/lunar/voc/current` - VoC actuel
- `GET /api/lunar/mansion/today` - Mansion du jour
- `POST /api/lunar/return/report` - Rapport mensuel

### Transits
- `GET /api/transits/overview/{userId}/{month}` - Vue d'ensemble
- `POST /api/transits/natal` - Transits natals

### Calendar
- `GET /api/calendar/month?year=YYYY&month=MM` - Calendrier mensuel
- `POST /api/calendar/phases` - Phases lunaires
- `POST /api/calendar/events` - Événements spéciaux

### Auth & Natal
- `POST /api/auth/login` - Connexion
- `POST /api/auth/register` - Inscription
- `GET /api/natal-chart` - Thème natal
- `GET /api/lunar-returns` - Liste révolutions

---

## 🧪 Tests

### Tests Jest Créés

**Fichier:** `__tests__/api.test.ts`

**Couverture** :
- ✅ auth.login (succès + erreur 500)
- ✅ lunaPack.getCurrentVoc (succès + erreur réseau)
- ✅ transits.getNatalTransits (payload validation)
- ✅ calendar.getMonth (query params + erreur 404)
- ✅ Error handling (ApiError, timeouts, status codes)

**Lancer les tests** :
```bash
npm test
```

---

## 🚀 Installation et Démarrage

### Installation

```bash
cd apps/mobile
npm install --legacy-peer-deps
```

### Configuration

Créer `.env` :
```env
# URL du backend API (optionnel, avec fallbacks automatiques)
EXPO_PUBLIC_API_URL=http://localhost:8000

# Mode DEV_AUTH_BYPASS (optionnel, pour tester sans login)
EXPO_PUBLIC_DEV_AUTH_BYPASS=true
EXPO_PUBLIC_DEV_USER_ID=1
```

**Notes sur les URLs :**
- Si `EXPO_PUBLIC_API_URL` n'est pas défini :
  - iOS Simulator : utilise automatiquement `http://127.0.0.1:8000`
  - Android Emulator : utilise automatiquement `http://10.0.2.2:8000` (host machine)
  - Autre : `http://localhost:8000` par défaut

**⚠️ IMPORTANT - Connexion réseau sur device réel :**

Si vous utilisez Expo Go sur un téléphone réel (pas un simulateur), `http://127.0.0.1:8000` ou `http://localhost:8000` ne fonctionneront pas. Vous devez utiliser l'IP LAN de votre machine :

1. **Trouver l'IP LAN de votre Mac :**
   ```bash
   # Sur macOS
   ipconfig getifaddr en0
   # ou
   ifconfig | grep "inet " | grep -v 127.0.0.1
   ```
   Exemple de résultat : `192.168.1.42`

2. **Configurer EXPO_PUBLIC_API_URL avec l'IP LAN :**
   ```env
   EXPO_PUBLIC_API_URL=http://192.168.1.42:8000
   ```

3. **Vérifier que le backend écoute sur toutes les interfaces :**
   ```bash
   # Le backend doit écouter sur 0.0.0.0 (pas seulement 127.0.0.1)
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

4. **Vérifier que le firewall autorise les connexions :**
   - macOS : Préférences Système → Sécurité → Pare-feu
   - Autoriser les connexions entrantes pour Python/uvicorn

**Résumé par plateforme :**
- ✅ **iOS Simulator** : `http://127.0.0.1:8000` fonctionne
- ✅ **Android Emulator** : `http://10.0.2.2:8000` fonctionne (fallback automatique)
- ⚠️ **Device réel (Expo Go)** : Utiliser l'IP LAN (ex: `http://192.168.1.42:8000`)

**Mode DEV_AUTH_BYPASS :**
- Active le mode bypass d'authentification JWT en development
- Utilise le header `X-Dev-User-Id` au lieu du token Bearer
- Nécessite que le backend soit lancé avec `DEV_AUTH_BYPASS=true` et `APP_ENV=development`
- Un label discret s'affiche sur l'écran Home pour indiquer le mode actif

### Lancement

```bash
npx expo start
```

Puis scanner le QR code avec **Expo Go** sur votre téléphone.

---

## 🎯 Navigation de l'App

```
/
├── index.tsx                    # Grille 12 mois lunaires
├── onboarding.tsx               # Onboarding initial
│
├── lunar/
│   ├── index.tsx                # Luna Pack hub (test 3 features)
│   ├── report.tsx               # Rapport lunaire détaillé
│   └── voc.tsx                  # Void of Course en temps réel
│
├── lunar-month/
│   └── [month].tsx              # Détail d'un mois spécifique
│
├── transits/
│   ├── overview.tsx             # Vue d'ensemble transits
│   └── details.tsx              # Détails d'un aspect
│
├── calendar/
│   └── month.tsx                # Calendrier mensuel combiné
│
└── settings/
    └── index.tsx                # Paramètres app
```

---

## 🔧 Gestion d'Erreurs

### Stratégie

1. **Try/Catch** systématique dans tous les appels API
2. **ErrorToast** pour erreurs non bloquantes (auto-dismiss 3s)
3. **States d'erreur** dans les écrans avec bouton "Réessayer"
4. **Messages en français** et contextuels

### Exemples d'Erreurs Gérées

- ❌ Erreur réseau (offline)
- ❌ Timeout API (> 30s)
- ❌ Erreur 500 backend
- ❌ Erreur 502 provider RapidAPI
- ❌ Données manquantes (empty states)

---

## ⚡ Optimisations

### Cache avec TTL
- **5 minutes** pour transits, VoC, calendar
- Vérification `isStale()` avant fetch
- Refresh automatique si données périmées

### Pull-to-Refresh
- Disponible sur VoC et Calendar
- Force le refresh même si cache valide

### Polling Intelligent
- VoC : Poll toutes les 5 min si app au premier plan
- Arrêt automatique si app en background

---

## 🎨 UX & Polish

### Loaders
- ✨ Skeleton loaders sur toutes les listes
- 🔄 ActivityIndicator pendant les requêtes
- 💫 Animations subtiles (fade, slide)

### States Vides
- 🌌 Message et emoji pour listes vides
- 💡 Suggestions d'actions

### Dark Mode
- 🌙 Dark by default (dégradé violet/noir)
- Palette mystique cohérente

---

## 📊 Métriques App Mobile

| Métrique | Valeur |
|----------|--------|
| **Écrans créés** | 8 |
| **Composants** | 5 |
| **Stores Zustand** | 5 |
| **Tests Jest** | 15+ assertions |
| **Endpoints consommés** | 12+ |
| **Lignes de code** | ~1500 |

---

## 🐛 Debug Mode

### JsonToggle

Tous les écrans incluent un `<JsonToggle>` en bas pour afficher les réponses JSON brutes.

**Toggle via** : Clic sur "Données Brutes (JSON)"

**Utile pour** :
- Débugger les payloads
- Voir les vraies réponses RapidAPI
- Vérifier le cache

---

## 🔄 Refresh & Cache

### Stratégie de Cache

1. **Premier chargement** : Fetch API
2. **Navigations suivantes** : Utilise le cache si < 5 min
3. **Pull-to-refresh** : Force le fetch
4. **Auto-refresh** : Si `isStale() === true`

### Stores Zustand

Tous les stores implémentent :
```ts
interface StoreState {
  data: any | null;
  lastFetch: number | null;
  isLoading: boolean;
  error: string | null;
  isStale: () => boolean;
  clear: () => void;
}
```

---

## 🎁 Bonus Features

### Notifications VoC (Paramétrable)
- Toggle dans settings pour activer/désactiver
- Notification 5 min avant le début d'une fenêtre VoC
- Rappel à la fin de la fenêtre

### Ville Par Défaut
- Configurée dans settings
- Utilisée pour tous les calculs (mansions, VoC, etc.)
- Évite de ressaisir à chaque fois

---

## 📚 Documentation Générée

Ce README couvre :
- ✅ Architecture complète des écrans
- ✅ Composants réutilisables
- ✅ Stores Zustand avec TTL
- ✅ Stratégie de cache
- ✅ Gestion d'erreurs
- ✅ Tests Jest
- ✅ Navigation
- ✅ Optimisations
- ✅ UX Polish

---

## 🚀 Commandes Rapides

```bash
# Installation
npm install --legacy-peer-deps

# Trouver l'IP LAN (pour device réel)
./scripts/print_lan_ip.sh

# Lancer l'app (avec cache clear recommandé si erreurs)
rm -rf .expo .expo-shared && npx expo start -c

# Lancer les tests
npm test

# Build iOS
npx expo build:ios

# Build Android
npx expo build:android
```

---

## 🔗 Backend API Requis

L'app mobile consomme le backend FastAPI sur `http://localhost:8000`.

**Assurez-vous que le backend tourne** avant de lancer l'app :

**Mode normal (avec JWT) :**
```bash
cd ../api
uvicorn main:app --reload --port 8000
```

**Mode DEV_AUTH_BYPASS (sans login, pour MVP) :**
```bash
cd ../api
APP_ENV=development DEV_AUTH_BYPASS=true uvicorn main:app --reload --port 8000
```

En mode DEV_AUTH_BYPASS :
- L'app envoie le header `X-Dev-User-Id` au lieu du token JWT
- Un label "DEV AUTH BYPASS (user_id=1)" s'affiche sur l'écran Home
- Permet de tester rapidement sans créer de compte / login

---

## 🎉 Conclusion

L'application mobile Lunation V1 est **complète et opérationnelle** avec :
- ✅ 8 écrans navigables
- ✅ 5 composants réutilisables
- ✅ 5 stores Zustand avec cache
- ✅ Thème mystique cohérent
- ✅ Gestion d'erreurs robuste
- ✅ Tests Jest
- ✅ Documentation exhaustive

**Prêt pour les utilisateurs !** 🌙✨

---

**Développé avec 🌙 et ⭐ par l'équipe Lunation**

