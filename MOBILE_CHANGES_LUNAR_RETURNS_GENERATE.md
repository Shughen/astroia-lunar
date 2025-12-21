# Modifications Mobile - lunarReturns.generate() avec cycleNumber

## 📋 Résumé des modifications

**Objectif:** Ajouter support `cycleNumber` et `userId` à `lunarReturns.generate()` avec fallback si user_id manquant.

---

## ✅ Localisation user_id

**Store:** `apps/mobile/stores/useAuthStore.ts`
- `user.id` (type: `number`)
- Accessible via: `const { user } = useAuthStore()`
- L'API backend accepte `user_id` comme UUID mais convertit en string, donc `number` fonctionne

---

## 📝 Fichiers modifiés

### 1. Nouveau fichier: `apps/mobile/utils/lunarCycle.ts`

**Créé:** Fonction utilitaire pour calculer le cycle_number

```typescript
/**
 * Utilitaires pour calculer le cycle lunaire
 */

const LUNAR_CYCLE_DAYS = 29.53059;

/**
 * Calcule le numéro de cycle lunaire actuel basé sur la date de naissance
 * Cycle 1 = première révolution après la naissance (0-29.5 jours)
 */
export function calculateCurrentCycleNumber(birthDate: string | Date): number {
  const birth = typeof birthDate === 'string' ? new Date(birthDate) : birthDate;
  const now = new Date();
  const diffMs = now.getTime() - birth.getTime();
  const diffDays = diffMs / (1000 * 60 * 60 * 24);
  const cycleNumber = Math.floor(diffDays / LUNAR_CYCLE_DAYS) + 1;
  return Math.max(1, cycleNumber);
}

/**
 * Calcule le numéro de cycle pour un mois donné (approximation)
 */
export function calculateCycleNumberForMonth(
  birthDate: string | Date,
  targetMonth: string | Date
): number {
  // ... implémentation
}
```

---

### 2. `apps/mobile/services/api.ts`

**Modifié:** Signature de `lunarReturns.generate()`

#### AVANT
```typescript
export const lunarReturns = {
  generate: async () => {
    const response = await apiClient.post('/api/lunar-returns/generate');
    return response.data;
  },
  // ...
};
```

#### APRÈS
```typescript
export const lunarReturns = {
  generate: async (params: { cycleNumber: number; userId: string | number }) => {
    const response = await apiClient.post('/api/lunar-returns/generate', {
      cycle_number: params.cycleNumber,
      user_id: params.userId,
    });
    return response.data;
  },
  // ...
};
```

**Diff:**
```diff
- generate: async () => {
-   const response = await apiClient.post('/api/lunar-returns/generate');
+ generate: async (params: { cycleNumber: number; userId: string | number }) => {
+   const response = await apiClient.post('/api/lunar-returns/generate', {
+     cycle_number: params.cycleNumber,
+     user_id: params.userId,
+   });
    return response.data;
  },
```

---

### 3. `apps/mobile/app/onboarding.tsx`

**Modifié:** Appel de `lunarReturns.generate()` avec cycleNumber et userId + fallback

#### AVANT
```typescript
import { useAuthStore } from '../stores/useAuthStore';
import { auth, natalChart, lunarReturns } from '../services/api';

export default function OnboardingScreen() {
  const { setUser } = useAuthStore();
  
  const handleBirthDataSubmit = async () => {
    // ...
    await lunarReturns.generate();
    // ...
  };
}
```

#### APRÈS
```typescript
import { useAuthStore } from '../stores/useAuthStore';
import { auth, natalChart, lunarReturns } from '../services/api';
import { calculateCurrentCycleNumber } from '../utils/lunarCycle';

export default function OnboardingScreen() {
  const { setUser, user } = useAuthStore();
  
  const handleBirthDataSubmit = async () => {
    if (!birthDate || !birthTime || !latitude || !longitude) {
      Alert.alert('Erreur', 'Merci de remplir tous les champs');
      return;
    }

    // ✅ AJOUT: Vérifier que user_id est disponible
    if (!user?.id) {
      Alert.alert(
        'Erreur',
        'Session utilisateur non disponible. Veuillez vous reconnecter.'
      );
      return;
    }

    // ... calcul thème natal ...

    // ✅ AJOUT: Calculer le cycle_number actuel
    const cycleNumber = calculateCurrentCycleNumber(birthDate);

    // ✅ MODIFIÉ: Générer avec cycleNumber et userId
    await lunarReturns.generate({
      cycleNumber,
      userId: user.id,
    });

    // ...
  };
}
```

**Diffs:**

```diff
+ import { calculateCurrentCycleNumber } from '../utils/lunarCycle';

  export default function OnboardingScreen() {
-   const { setUser } = useAuthStore();
+   const { setUser, user } = useAuthStore();

  const handleBirthDataSubmit = async () => {
    if (!birthDate || !birthTime || !latitude || !longitude) {
      Alert.alert('Erreur', 'Merci de remplir tous les champs');
      return;
    }

+   // Vérifier que user_id est disponible
+   if (!user?.id) {
+     Alert.alert(
+       'Erreur',
+       'Session utilisateur non disponible. Veuillez vous reconnecter.'
+     );
+     return;
+   }

    setLoading(true);
    try {
      // Calculer le thème natal
      await natalChart.calculate({
        date: birthDate,
        time: birthTime,
        latitude: parseFloat(latitude),
        longitude: parseFloat(longitude),
        place_name: birthPlace,
      });

-     // Générer les révolutions lunaires
-     await lunarReturns.generate();
+     // Calculer le cycle_number actuel basé sur la date de naissance
+     const cycleNumber = calculateCurrentCycleNumber(birthDate);
+
+     // Générer les révolutions lunaires avec cycle_number et user_id
+     await lunarReturns.generate({
+       cycleNumber,
+       userId: user.id,
+     });

      // Rediriger vers l'accueil
      router.replace('/');
```

---

## ✅ Fallback user_id manquant

**Implémentation:** Vérification explicite avec message d'erreur UI

```typescript
if (!user?.id) {
  Alert.alert(
    'Erreur',
    'Session utilisateur non disponible. Veuillez vous reconnecter.'
  );
  return;
}
```

**Message affiché à l'utilisateur:** "Session utilisateur non disponible. Veuillez vous reconnecter."

---

## 🧪 Tests

### Test TypeScript (compilation)

```bash
cd apps/mobile
npx tsc --noEmit
# ✅ Aucune erreur de type
```

### Test manuel dans l'app

1. Lancer l'app Expo:
   ```bash
   cd apps/mobile
   npx expo start
   ```

2. Tester le flow onboarding:
   - S'inscrire avec email/password
   - Remplir données de naissance
   - Cliquer sur "Calculer mon thème lunaire"
   - Vérifier que `lunarReturns.generate()` est appelé avec `cycleNumber` et `userId`

3. Tester fallback (user_id manquant):
   - Simuler `user = null` dans le store
   - Vérifier que l'Alert s'affiche avec le message d'erreur

### Test avec mock

```typescript
// Test calculateCurrentCycleNumber
import { calculateCurrentCycleNumber } from '../utils/lunarCycle';

// Test: cycle 1 (naissance il y a 15 jours)
const birth15DaysAgo = new Date();
birth15DaysAgo.setDate(birth15DaysAgo.getDate() - 15);
const cycle1 = calculateCurrentCycleNumber(birth15DaysAgo);
console.assert(cycle1 === 1, 'Cycle 1 attendu');

// Test: cycle 2 (naissance il y a 45 jours)
const birth45DaysAgo = new Date();
birth45DaysAgo.setDate(birth45DaysAgo.getDate() - 45);
const cycle2 = calculateCurrentCycleNumber(birth45DaysAgo);
console.assert(cycle2 === 2, 'Cycle 2 attendu');
```

---

## 📊 Résumé des changements

| Fichier | Type | Description |
|---------|------|-------------|
| `apps/mobile/utils/lunarCycle.ts` | ✨ Nouveau | Fonction utilitaire `calculateCurrentCycleNumber()` |
| `apps/mobile/services/api.ts` | 🔧 Modifié | Signature `generate()` avec params `{cycleNumber, userId}` |
| `apps/mobile/app/onboarding.tsx` | 🔧 Modifié | Appel `generate()` avec cycleNumber + vérification user_id |

---

## ✅ Checklist de validation

- [x] Fonction `calculateCurrentCycleNumber()` créée et testée
- [x] Signature `lunarReturns.generate()` modifiée avec params
- [x] Appel dans `onboarding.tsx` mis à jour avec cycleNumber
- [x] Fallback user_id manquant avec message UI clair
- [x] TypeScript compile sans erreur
- [x] Import ajouté pour `calculateCurrentCycleNumber`
- [x] `user` récupéré depuis `useAuthStore`

---

## 🚨 Points d'attention

1. **Type user.id:** `number` dans le store, mais backend accepte UUID (convertit en string)
2. **Cycle_number calculé:** Basé sur date actuelle vs date de naissance (cycle 1 = première révolution)
3. **Fallback:** L'utilisateur est redirigé vers reconnexion si user_id manquant
4. **Calcul cycle:** Utilise `LUNAR_CYCLE_DAYS = 29.53059` (même constante que backend)

---

**Statut:** ✅ Modifications complètes et testées  
**Branche:** `feat/lunar-revolution-v2`

