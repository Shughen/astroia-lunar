# Guide de Tests Manuels - Onboarding Flow

## Prérequis

- App lancée avec `DEV_AUTH_BYPASS=true` dans `.env`
- Backend API accessible (vérifier avec `/debug/selftest`)
- Expo Go ou simulateur iOS/Android

---

## Scénario 1: 1ère Connexion (Nouvel Utilisateur)

### Objectif
Vérifier que le flow onboarding complet fonctionne et que le natal chart est calculé automatiquement.

### Reset Initial
```bash
# Depuis l'app: /settings → "Tout réinitialiser"
# OU depuis le code:
import { useOnboardingStore } from './stores/useOnboardingStore';
import { useNatalStore } from './stores/useNatalStore';

const { reset } = useOnboardingStore.getState();
const { clearChart } = useNatalStore.getState();

await reset();
clearChart();
```

### Étapes

1. **Lancer l'app** → Devrait rediriger vers `/welcome`
   - ✅ Écran "Bienvenue sur Lunation" visible
   - ✅ Bouton "Continuer" présent

2. **Cliquer "Continuer"** → Redirection `/onboarding/profile-setup`
   - ✅ Header "Étape 1/4"
   - ✅ Champs "Prénom" et "Date de naissance"
   - ✅ Info box "Ta date de naissance nous permet..."

3. **Remplir le profil**
   - Saisir prénom: `Marie`
   - Ajuster date: `15/05/1990`
   - Cliquer "Suivant"

4. **Vérifier logs** (console/metro)
   ```
   [PROFILE-SETUP] Profil sauvegardé → { name: 'Marie', birthDate: ... }
   [PROFILE-SETUP] ✅ Natal chart calculé automatiquement
   ```
   - ✅ Natal chart calculé EN BACKGROUND
   - ✅ Pas d'erreur bloquante si API échoue

5. **Redirection `/onboarding/consent`** (Étape 2/4)
   - ✅ Titre "Consentement RGPD"
   - ✅ Checkbox "J'accepte"
   - Cocher + "Suivant"

6. **Redirection `/onboarding/disclaimer`** (Étape 3/4)
   - ✅ Titre "Disclaimer Médical"
   - ✅ Checkbox "J'ai lu et compris"
   - Cocher + "Suivant"

7. **Redirection `/onboarding/cycle-setup`** (Étape 4/4)
   - ✅ Titre "Setup Cycle Menstruel"
   - ✅ Boutons "Passer cette étape" + "Configurer"
   - Cliquer "Passer cette étape"

8. **Redirection `/onboarding`** (Slides Value Proposition)
   - ✅ 4 slides visibles
   - ✅ Bouton "Suivant" entre slides
   - ✅ Bouton "Passer" disponible
   - Cliquer "Suivant" jusqu'au bout

9. **Dernier slide → Cliquer "Commencer"**
   - ✅ Logs: `[OnboardingStore] onboarding_completed = true`
   - ✅ Redirection vers Home

10. **Vérifier Home**
    - ✅ Titre "🌙 Lunation"
    - ✅ Badge DEV_AUTH_BYPASS visible
    - ✅ Natal chart disponible dans store

    **Vérifier dans DevTools/console**:
    ```javascript
    import { useNatalStore } from './stores/useNatalStore';
    console.log(useNatalStore.getState().chart);
    // Doit afficher: { sun_sign: '...', moon_sign: '...', ... }
    ```

### Résultat Attendu
- ✅ Tous les écrans affichés dans l'ordre
- ✅ Natal chart calculé automatiquement après profile-setup
- ✅ Pas d'erreur ou crash
- ✅ Redirection finale vers Home avec données persistées

---

## Scénario 2: 2ème Connexion (Utilisateur Déjà Onboardé)

### Objectif
Vérifier qu'un utilisateur déjà onboardé accède directement au Home.

### Étapes

1. **NE PAS RESET AsyncStorage** (garder l'état du Scénario 1)

2. **Relancer l'app** (force quit + reopen)
   - ✅ **Direct Home** (aucun écran onboarding)
   - ✅ Pas de redirection vers /welcome ou /onboarding/*

3. **Vérifier logs**
   ```
   [INDEX] 🔄 checkRouting() appelé, hydrated=false
   [OnboardingStore] 💧 Hydratation depuis AsyncStorage...
   [OnboardingStore] ✅ Hydraté: {
     hasSeenWelcome: true,
     hasCompletedProfile: true,
     hasAcceptedConsent: true
   }
   [INDEX] ✅ Tous les guards passés, affichage Home
   ```

4. **Vérifier store**
   ```javascript
   import { useOnboardingStore } from './stores/useOnboardingStore';
   console.log(useOnboardingStore.getState());
   // Doit afficher:
   // {
   //   hasSeenWelcomeScreen: true,
   //   hasCompletedProfile: true,
   //   hasAcceptedConsent: true,
   //   hasSeenDisclaimer: true,
   //   hasCompletedOnboarding: true,
   //   hydrated: true
   // }
   ```

5. **Vérifier natal chart toujours présent**
   ```javascript
   import { useNatalStore } from './stores/useNatalStore';
   console.log(useNatalStore.getState().chart);
   // Doit afficher le chart (pas null)
   ```

### Résultat Attendu
- ✅ Aucun écran onboarding affiché
- ✅ Direct Home en < 1 seconde
- ✅ Données persistées (profil + natal)
- ✅ Pas de recalcul natal (déjà en local)

---

## Scénario 3: Reset Onboarding

### Objectif
Vérifier que le reset onboarding fonctionne correctement et relance le flow complet.

### Étapes

1. **Aller dans `/settings`**
   - ✅ Écran Settings affiché
   - ✅ Section "🧪 Debug / Tests"
   - ✅ Bouton "🗑️ Tout réinitialiser"

2. **Cliquer "Tout réinitialiser"**
   - ✅ Alert confirmation "Tu vas réinitialiser welcome, onboarding et thème natal"
   - Cliquer "Tout réinitialiser"

3. **Vérifier logs**
   ```
   [OnboardingStore] 🗑️ Reset onboarding complet
   [OnboardingStore] ✅ Reset terminé, hydrated=false
   [SETTINGS] ✅ Onboarding + Natal réinitialisés
   ```

4. **Alert succès**
   - ✅ "Tout réinitialisé ! Retour au Home pour redémarrer."
   - Cliquer "OK"

5. **Redirection automatique vers Home → `/welcome`**
   - ✅ checkRouting() re-run (car hydrated=false)
   - ✅ Redirection immédiate vers `/welcome`
   - ✅ **PAS DE BOUCLE INFINIE**

6. **Vérifier logs routing**
   ```
   [INDEX] 🔄 checkRouting() appelé, hydrated=false
   [OnboardingStore] 💧 Hydratation depuis AsyncStorage...
   [OnboardingStore] ✅ Hydraté: {
     hasSeenWelcome: false,
     hasCompletedProfile: false,
     hasAcceptedConsent: false
   }
   [INDEX] ✅ Welcome screen non vu → redirection vers /welcome
   ```

7. **Refaire le flow complet**
   - Suivre Scénario 1 étapes 2-10
   - ✅ Tous les écrans réapparaissent
   - ✅ Natal chart recalculé
   - ✅ Redirection finale vers Home

### Résultat Attendu
- ✅ Reset supprime TOUTES les clés onboarding (5/5)
- ✅ Reset clear natal chart
- ✅ Retour automatique sur Home déclenche routing check
- ✅ Redirection immédiate vers /welcome
- ✅ Flow complet recommence (comme 1ère connexion)
- ✅ **AUCUNE BOUCLE** (hasCheckedRoutingRef reset correctement)

---

## Cas d'Erreur à Tester

### Erreur API Natal Chart

**Setup**: Couper le backend ou mettre une mauvaise URL API

**Étapes**:
1. Reset onboarding
2. Compléter profile-setup
3. Vérifier logs:
   ```
   [PROFILE-SETUP] ⚠️ Échec calcul natal (non bloquant): Network Error
   ```
4. ✅ Onboarding continue quand même
5. ✅ Redirection vers consent
6. ✅ Pas d'Alert bloquante

**Résultat**: Le flow onboarding ne doit JAMAIS être bloqué par un échec de calcul natal.

---

### Navigation Sans Stack History

**Setup**: Accéder directement à `/settings` via deep link

**Étapes**:
1. Cliquer "← Retour" dans Settings
2. ✅ router.canGoBack() = false
3. ✅ Fallback: router.replace('/')
4. ✅ Redirection vers Home
5. ✅ **PAS DE WARNING** "GO_BACK was not handled"

---

## Checklist Finale

Après avoir exécuté les 3 scénarios:

- [ ] Scénario 1: 1ère connexion complète, natal chart auto-calculé
- [ ] Scénario 2: 2ème connexion direct Home, pas de recalcul
- [ ] Scénario 3: Reset fonctionne, flow recommence
- [ ] Pas de boucle infinie (logs propres)
- [ ] Pas de warning "GO_BACK was not handled"
- [ ] Natal chart présent après 1ère connexion
- [ ] Natal chart cleared après reset
- [ ] Tests Jest: 31/31 passed
- [ ] TypeScript: 0 errors
- [ ] Logs propres (pas d'erreur console)

---

## Debug Rapide

Si problème, vérifier dans console:

```javascript
// État onboarding
import { useOnboardingStore } from './stores/useOnboardingStore';
console.log('Onboarding:', useOnboardingStore.getState());

// État natal
import { useNatalStore } from './stores/useNatalStore';
console.log('Natal:', useNatalStore.getState().chart);

// AsyncStorage direct
import AsyncStorage from '@react-native-async-storage/async-storage';
AsyncStorage.multiGet([
  'hasSeenWelcomeScreen',
  'onboarding_completed',
  'onboarding_profile',
  'onboarding_consent',
  'onboarding_disclaimer',
]).then(console.log);
```

**Commande reset manuel**:
```javascript
import { useOnboardingStore } from './stores/useOnboardingStore';
import { useNatalStore } from './stores/useNatalStore';

const { reset } = useOnboardingStore.getState();
const { clearChart } = useNatalStore.getState();

await reset();
clearChart();
console.log('✅ Reset manuel terminé');
```
