# ✅ Timeline Mobile - Migration vers Rolling - Résumé

## 🎯 Objectif

Faire en sorte que la timeline mobile affiche les 12 prochains retours (rolling) au lieu d'une année fixe, en utilisant le nouvel endpoint `/api/lunar-returns/rolling`.

---

## 📝 Modifications apportées

### 1. `services/api.ts`

**Ajout de la méthode `getRolling()` :**

```typescript
export const lunarReturns = {
  // ... méthodes existantes ...
  
  /**
   * Récupère les 12 prochains retours lunaires (rolling) - idéal pour timeline MVP
   */
  getRolling: async (): Promise<LunarReturn[]> => {
    const response = await apiClient.get('/api/lunar-returns/rolling');
    return response.data;
  },
};
```

**Note :** `getYear()` est conservé pour compatibilité, mais n'est plus utilisé dans la timeline.

---

### 2. `app/lunar-returns/timeline.tsx`

**Changements principaux :**

1. **Remplacement de `getYear(currentYear)` par `getRolling()`**
   ```typescript
   // Avant
   const currentYear = new Date().getFullYear();
   const returns = await lunarReturns.getYear(currentYear);
   
   // Après
   const returns = await lunarReturns.getRolling();
   ```

2. **Tri conservé par `return_date`** (déjà fait)
   - Les retours sont triés par `return_date` ASC
   - Les badges PASSÉ/AUJOURD'HUI/À VENIR sont basés sur `return_date` vs `now`

3. **Empty state amélioré**
   - Si `[]` (liste vide) → affiche "Aucun retour lunaire généré"
   - Bouton "Générer mes retours" appelle `lunarReturns.generate()` directement
   - Après génération, recharge automatiquement la timeline

4. **Gestion d'erreurs**
   - Si 404, ne pas afficher d'erreur (liste vide est normale)
   - Autres erreurs affichées avec `correlation_id`

**Nouveau code :**
```typescript
const [generating, setGenerating] = useState(false);

const handleGenerate = async () => {
  setGenerating(true);
  try {
    await lunarReturns.generate();
    Alert.alert('Succès', 'Retours lunaires générés avec succès ! ✨');
    await loadTimeline(); // Recharger après génération
  } catch (error: any) {
    handleApiError(error);
  } finally {
    setGenerating(false);
  }
};

const renderEmpty = () => (
  <View style={styles.emptyContainer}>
    <Text style={styles.emptyEmoji}>🌙</Text>
    <Text style={styles.emptyText}>Aucun retour lunaire généré</Text>
    <TouchableOpacity
      style={styles.generateButton}
      onPress={handleGenerate}
      disabled={generating}
    >
      {generating ? (
        <ActivityIndicator color={colors.text} />
      ) : (
        <Text style={styles.generateButtonText}>Générer mes retours</Text>
      )}
    </TouchableOpacity>
  </View>
);
```

---

### 3. `app/index.tsx` (Home)

**Aucun changement nécessaire :**
- Home utilise `/next` qui est indépendant de `/rolling`
- Le bloc "Prochain retour lunaire" fonctionne toujours correctement

---

### 4. DEV_AUTH_BYPASS

**Déjà en place :**
- `apiClient` intercepteur ajoute automatiquement `X-Dev-User-Id` si `EXPO_PUBLIC_DEV_AUTH_BYPASS=true`
- Fonctionne pour tous les endpoints, y compris `/rolling`

---

## ✅ Comportement final

### Timeline avec retours :

1. Appelle `GET /api/lunar-returns/rolling`
2. Reçoit jusqu'à 12 retours (triés par `return_date` ASC côté backend)
3. Affiche les retours avec badges :
   - **PASSÉ** (gris) : `return_date < now`
   - **AUJOURD'HUI** (violet) : `return_date === now` (même jour)
   - **À VENIR** (vert) : `return_date > now`

### Timeline sans retours :

1. Appelle `GET /api/lunar-returns/rolling`
2. Reçoit `[]` (liste vide)
3. Affiche empty state avec bouton "Générer mes retours"
4. Au clic : appelle `POST /api/lunar-returns/generate`
5. Recharge automatiquement la timeline après génération

---

## 🧪 Tests

### Test manuel (DEV_AUTH_BYPASS)

```bash
# Backend
cd apps/api
APP_ENV=development DEV_AUTH_BYPASS=true uvicorn main:app --reload --port 8000

# Mobile
cd apps/mobile
EXPO_PUBLIC_DEV_AUTH_BYPASS=true EXPO_PUBLIC_DEV_USER_ID=1 npx expo start
```

**Scénarios à tester :**

1. **Timeline vide** → Empty state → Cliquer "Générer mes retours" → Timeline se remplit avec 12 items
2. **Timeline avec retours** → Affiche 12 items avec badges corrects
3. **Navigation Home → Timeline** → Timeline affiche les 12 rolling retours

---

## 📋 Checklist de validation

- [x] `getRolling()` ajouté dans `api.ts`
- [x] Timeline utilise `getRolling()` au lieu de `getYear()`
- [x] Tri par `return_date` conservé
- [x] Badges PASSÉ/AUJOURD'HUI/À VENIR basés sur `return_date` vs `now`
- [x] Empty state avec bouton "Générer mes retours" qui appelle `generate()`
- [x] Rechargement automatique après génération
- [x] Home (`/next`) non modifié et fonctionnel
- [x] DEV_AUTH_BYPASS fonctionne (déjà en place)

---

**Migration complète et prête pour le MVP !** 🌙✨

