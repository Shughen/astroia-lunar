# ✅ Fix Theme et Network - Résumé des corrections

## 🎯 Problèmes corrigés

1. **Crash `fonts.sizes.xxl` undefined** dans `app/debug/selftest.tsx`
2. **Documentation réseau** pour device réel (Expo Go)

---

## 📝 Modifications apportées

### 1. `constants/theme.ts`

**Problème :** `fonts` n'avait pas de propriétés `size` ni `sizes`.

**Solution :** Ajout d'une échelle de tailles typographiques avec support des deux conventions :

```typescript
// Échelle de tailles typographiques (source unique)
const fontSizes = {
  xs: 12,
  sm: 14,
  md: 16,
  lg: 20,
  xl: 24,
  xxl: 32,
} as const;

export const fonts = {
  // ... styles existants (h1, h2, body, etc.) conservés ...
  
  // Échelle de tailles (source unique)
  sizes: fontSizes,
  // Alias pour compatibilité avec fonts.size.*
  size: fontSizes,
} as const;
```

**Résultat :**
- ✅ `fonts.sizes.*` fonctionne (utilisé dans debug/selftest.tsx)
- ✅ Toutes les tailles attendues existent : xs, sm, md, lg, xl, xxl
- ✅ Les styles existants (h1, h2, body, etc.) sont conservés

---

### 2. Documentation réseau (`README-MOBILE.md`)

**Problème :** Pas de documentation claire pour utiliser l'app sur un device réel (Expo Go) où `127.0.0.1` ne fonctionne pas.

**Solution :** Ajout d'un encart explicatif dans la section Configuration :

**Contenu ajouté :**
- Explication du problème (127.0.0.1 ne fonctionne pas sur device réel)
- Instructions pour trouver l'IP LAN (`ipconfig getifaddr en0`)
- Configuration de `EXPO_PUBLIC_API_URL` avec l'IP LAN
- Vérification que le backend écoute sur `0.0.0.0`
- Vérification du firewall
- Résumé par plateforme (iOS Simulator / Android Emulator / Device réel)

---

### 3. Script helper (`scripts/print_lan_ip.sh`)

**Création d'un script bash** pour automatiser la récupération de l'IP LAN :

```bash
#!/bin/bash
# Script helper pour obtenir l'IP LAN du Mac
# Usage: ./scripts/print_lan_ip.sh
```

**Fonctionnalités :**
- Trouve l'IP LAN (essaye `en0` puis fallback sur première IP non-localhost)
- Affiche l'IP trouvée
- Donne la commande à ajouter dans `.env`
- Rappelle de lancer le backend avec `--host 0.0.0.0`

**Utilisation :**
```bash
cd apps/mobile
./scripts/print_lan_ip.sh
```

---

### 4. Commandes rapides mises à jour

**Ajout dans `README-MOBILE.md` :**
```bash
# Trouver l'IP LAN (pour device réel)
./scripts/print_lan_ip.sh

# Lancer l'app (avec cache clear recommandé si erreurs)
rm -rf .expo .expo-shared && npx expo start -c
```

---

## ✅ Fichiers modifiés

### 1. `constants/theme.ts`

**Changements :**
- Ajout de `fontSizes` constant (source unique)
- Ajout de `fonts.sizes = fontSizes`
- Ajout de `fonts.size = fontSizes` (alias)

**Impact :**
- ✅ Corrige les crashes dans `debug/selftest.tsx` (fonts.sizes.*)
- ✅ Compatible avec le code existant (pas de breaking changes)

---

### 2. `README-MOBILE.md`

**Changements :**
- Ajout section "⚠️ IMPORTANT - Connexion réseau sur device réel"
- Instructions pour trouver l'IP LAN
- Configuration EXPO_PUBLIC_API_URL avec IP LAN
- Vérifications backend (--host 0.0.0.0) et firewall
- Résumé par plateforme
- Commandes rapides mises à jour

---

### 3. `scripts/print_lan_ip.sh` (NOUVEAU)

**Création :**
- Script bash pour trouver l'IP LAN automatiquement
- Permissions exécutables ajoutées
- Utilisation simple : `./scripts/print_lan_ip.sh`

---

## 🔍 Vérifications

### Utilisation de `fonts.sizes.*`

**Fichiers utilisant `fonts.sizes.*` :**
- `app/debug/selftest.tsx` : xxl, sm, lg, md (7 occurrences)

**Résultat :** ✅ Toutes les tailles utilisées existent maintenant dans `fonts.sizes`.

---

## 🚀 Commandes de relance recommandées

### Pour corriger les erreurs de cache Expo :

```bash
cd apps/mobile

# Nettoyer le cache Expo
rm -rf .expo .expo-shared

# Relancer avec cache clear
npx expo start -c
```

### Pour trouver l'IP LAN (device réel) :

```bash
cd apps/mobile
./scripts/print_lan_ip.sh
```

### Configuration `.env` pour device réel :

```env
# Trouver l'IP avec le script ci-dessus, puis :
EXPO_PUBLIC_API_URL=http://192.168.1.42:8000  # Remplacez par votre IP
EXPO_PUBLIC_DEV_AUTH_BYPASS=true
EXPO_PUBLIC_DEV_USER_ID=1
```

### Lancer le backend (important pour device réel) :

```bash
cd apps/api

# Mode DEV_AUTH_BYPASS avec host 0.0.0.0 (accessible depuis le réseau local)
APP_ENV=development DEV_AUTH_BYPASS=true uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

---

## 📋 Checklist de validation

- [x] `fonts.size.*` fonctionne (alias vers `fonts.sizes`)
- [x] `fonts.sizes.*` fonctionne (source unique)
- [x] Toutes les tailles attendues existent (xs, sm, md, lg, xl, xxl)
- [x] Styles existants conservés (h1, h2, body, etc.)
- [x] Documentation réseau ajoutée dans README-MOBILE.md
- [x] Script helper `print_lan_ip.sh` créé et exécutable
- [x] Commandes rapides mises à jour
- [x] Code compile correctement (TypeScript check OK)

---

## ⚠️ Notes importantes

1. **Compatibilité :** Les deux conventions (`fonts.size.*` et `fonts.sizes.*`) fonctionnent grâce à l'alias. Aucun changement requis dans le code existant.

2. **Device réel :** Pour Expo Go sur téléphone, utiliser l'IP LAN (pas `127.0.0.1`). Le script `print_lan_ip.sh` facilite la configuration.

3. **Backend :** Pour accepter les connexions depuis le réseau local, lancer avec `--host 0.0.0.0` (pas seulement `127.0.0.1`).

4. **Firewall :** Vérifier que le pare-feu autorise les connexions entrantes pour Python/uvicorn.

---

**Toutes les corrections sont en place et prêtes à être testées !** 🌙✨

