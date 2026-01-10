# Tests Network Guard - Anti-spam réseau

## Vue d'ensemble

Le système `requestGuard` implémente 2 mécanismes pour éviter le spam réseau :

1. **Déduplication in-flight** : Si une requête identique est déjà en cours → retourne la même Promise
2. **Cache TTL** : Si une requête identique a été faite il y a < TTL → retourne la réponse cachée

---

## Endpoints concernés

| Endpoint | TTL | Dédup | Cache key params | Raison |
|----------|-----|-------|------------------|--------|
| `lunar-returns/current` | 60s | ✅ | N/A | Peu changeant, appelé au mount de plusieurs écrans |
| `lunar/voc` | 5min | ✅ | `{date}` | Cache key stable: time exclu pour éviter refetch minute par minute |
| `lunar/mansion` | 5min | ✅ | `{date}` | Cache key stable: time exclu pour éviter refetch minute par minute |
| `lunar/return/report` | 5min | ✅ | `{date, month}` | Données stables (rapport mensuel) |
| `lunar/daily-climate` | **5min** | ✅ | `{date}` | Cache key stable: time exclu. Daily climate + insights (appelé par LunarProvider) |

**Notes importantes** :

1. **Cache key stability** : Les endpoints `lunar/voc`, `lunar/mansion`, et `lunar/daily-climate` utilisent uniquement `{date}` dans la cache key (le paramètre `time` est exclu). Cela garantit une cache key stable tout au long de la journée, évitant les refetch inutiles chaque minute. Le payload complet (incluant `time` si applicable) est toujours envoyé au backend, mais la cache key ignore ce paramètre pour rester stable.

2. **Double cache system** :
   - **requestGuard** (module-scope Map) : Cache court terme (60s-5min) pour dedup + anti-spam réseau
   - **lunarCache** (AsyncStorage) : Cache long terme (24h, stale après 1h) pour persistence offline
   - Ces 2 systèmes travaillent ensemble : requestGuard empêche les refetch < 5min, lunarCache permet la persistence entre sessions

3. **LunarProvider refresh guards** :
   - Minimum 60s entre 2 background refreshes (via `REFRESH_TTL_MS`)
   - Pas de boucle infinie grâce à `refreshInFlight` ref + `lastRefreshAt` timestamp
   - `loadLunarData` avec deps stables (`[]`) pour éviter re-création à chaque update

---

## Scénarios de test

### 1. Navigation rapide (dédup in-flight)

**Objectif** : Vérifier que les appels doublons rapprochés (<1s) sont dédupliqués

**Steps** :
1. Démarrer l'app
2. Aller sur `/lunar` (Luna Pack)
3. Cliquer rapidement sur "Lunar Mansion" puis "Back" puis "Lunar Mansion" à nouveau (< 1s)
4. Observer les logs console

**Attendu** :
```
[RequestGuard] 🚀 Fetching: lunar/mansion
[RequestGuard] 🔄 Dedup: lunar/mansion (request already in-flight)
[RequestGuard] ✅ Cached: lunar/mansion
```

**Résultat** :
- ✅ 1 seul appel réseau backend
- ✅ Les 2 promesses retournent la même réponse

---

### 2. Re-focus écran (cache TTL)

**Objectif** : Vérifier que le cache TTL empêche les refetch inutiles

**Steps** :
1. Ouvrir `/lunar`, cliquer "Lunar Mansion"
2. Attendre la réponse → Voir "Mansion #12"
3. Naviguer ailleurs (ex: `/settings`)
4. Revenir sur `/lunar` dans les **60 secondes**
5. Cliquer à nouveau "Lunar Mansion"
6. Observer les logs

**Attendu** :
```
[RequestGuard] 🚀 Fetching: lunar/mansion
[RequestGuard] ✅ Cached: lunar/mansion
... (60s plus tard) ...
[RequestGuard] ✅ Cache hit: lunar/mansion (age: 15s)
```

**Résultat** :
- ✅ Pas de 2e appel réseau
- ✅ La réponse vient du cache

---

### 3. Cache expiré (re-fetch après TTL)

**Objectif** : Vérifier que le cache expire correctement

**Steps** :
1. Ouvrir `/lunar`, cliquer "Lunar Mansion"
2. Attendre la réponse
3. Attendre **> 5 minutes** (TTL = 300s pour mansion)
4. Cliquer à nouveau "Lunar Mansion"
5. Observer les logs

**Attendu** :
```
[RequestGuard] 🚀 Fetching: lunar/mansion
[RequestGuard] ✅ Cached: lunar/mansion
... (5min plus tard) ...
[RequestGuard] ⏱️ Cache expired: lunar/mansion
[RequestGuard] 🚀 Fetching: lunar/mansion
[RequestGuard] ✅ Cached: lunar/mansion
```

**Résultat** :
- ✅ Le cache a expiré
- ✅ Un nouveau fetch est lancé

---

### 4. Reload Expo Dev (cache cleared)

**Objectif** : Vérifier que le cache est nettoyé au reload

**Steps** :
1. Ouvrir `/lunar`, cliquer "Lunar Mansion"
2. Reload Expo (secouer device → "Reload")
3. Ouvrir `/lunar`, cliquer "Lunar Mansion"
4. Observer les logs

**Attendu** :
```
[RequestGuard] 🚀 Fetching: lunar/mansion
[RequestGuard] ✅ Cached: lunar/mansion
... (après reload) ...
[RequestGuard] 🚀 Fetching: lunar/mansion  // Cache cleared
[RequestGuard] ✅ Cached: lunar/mansion
```

**Résultat** :
- ✅ Le cache est nettoyé au reload app
- ✅ Un nouveau fetch est lancé

---

### 5. Appels parallèles (dedup multiple)

**Objectif** : Vérifier que plusieurs appels simultanés sont dédupliqués

**Steps** :
1. Modifier temporairement `app/index.tsx` ligne 227 pour appeler `getCurrent()` 3 fois en parallèle :
   ```ts
   Promise.all([
     lunarReturns.getCurrent(),
     lunarReturns.getCurrent(),
     lunarReturns.getCurrent(),
   ]).then(console.log);
   ```
2. Démarrer l'app
3. Observer les logs

**Attendu** :
```
[RequestGuard] 🚀 Fetching: lunar-returns/current
[RequestGuard] 🔄 Dedup: lunar-returns/current (request already in-flight)
[RequestGuard] 🔄 Dedup: lunar-returns/current (request already in-flight)
[RequestGuard] ✅ Cached: lunar-returns/current
```

**Résultat** :
- ✅ 1 seul appel réseau
- ✅ Les 3 promesses résolvent avec la même valeur

---

## Stats de cache (debug)

Pour voir les stats du cache en temps réel, ajouter dans la console :

```ts
import { getCacheStats } from './utils/requestGuard';

console.log(getCacheStats());
// Output: { cacheSize: 3, inFlightSize: 0 }
```

---

## Invalidation manuelle

Si besoin d'invalider le cache après un POST/PUT :

```ts
import { invalidateCache } from './utils/requestGuard';

// Après avoir créé un nouveau retour lunaire
await createLunarReturn(...);
invalidateCache('lunar-returns/current'); // Force refetch next time
```

---

## Clear all cache (logout)

Pour nettoyer tout le cache (ex: lors du logout) :

```ts
import { clearAllCache } from './utils/requestGuard';

// Dans logout()
await auth.logout();
clearAllCache();
```

---

## Logs à surveiller

### ✅ Comportement normal

```
[RequestGuard] 🚀 Fetching: lunar-returns/current
[RequestGuard] ✅ Cached: lunar-returns/current
[RequestGuard] ✅ Cache hit: lunar-returns/current (age: 15s)
[RequestGuard] 🔄 Dedup: lunar/mansion (request already in-flight)
```

### ⚠️ Signaux d'alerte

```
[RequestGuard] ❌ Error: lunar/mansion
// → Erreur réseau, cache non stocké

// Multiple fetches rapprochés sans dedup
[RequestGuard] 🚀 Fetching: lunar-returns/current
[RequestGuard] 🚀 Fetching: lunar-returns/current  // ⚠️ Pas de dedup !
```

Si vous voyez des fetches doublons **sans** logs de dedup, cela signifie que les clés de cache sont différentes (payload différent).

---

## Dépannage

### Problème : Cache ne s'active pas

**Cause** : Clés de cache instables (payload différent à chaque appel)

**Solution** : Vérifier que `getCacheKey()` génère des clés stables. Exemple :

```ts
// ❌ Mauvais : timestamp change à chaque appel
const payload = { date: new Date().toISOString() };

// ✅ Bon : même date = même clé
const payload = { date: '2025-01-15' };
```

### Problème : Cache ne se vide jamais

**Cause** : TTL trop long ou pas de reload

**Solution** :
- Vérifier le TTL dans `services/api.ts`
- Appeler `clearAllCache()` au logout

---

## Production vs Dev

### En dev (`__DEV__ === true`)
- ✅ Logs détaillés dans console
- ✅ Cache stats accessibles
- ✅ Badge MOCK + Provider label visibles

### En prod (`__DEV__ === false`)
- ❌ Pas de logs RequestGuard
- ✅ Cache fonctionne normalement
- ❌ Pas de badge MOCK ni provider label

---

## Métriques (optionnel)

Pour tracker les performances du cache en prod, ajouter analytics :

```ts
// Dans requestGuard.ts
if (!forceRefresh && cached) {
  const age = Date.now() - cached.timestamp;
  if (age < ttl) {
    analytics.track('cache_hit', { key: cacheKey, age });
    return cached.data;
  }
}
```

---

## Checklist finale

- [ ] Vérifier logs dedup pour `lunar-returns/current`
- [ ] Vérifier cache TTL pour Luna Pack (mansion/voc/report/daily-climate)
- [ ] Tester navigation rapide (< 1s) → pas de doublons
- [ ] Tester re-focus après 30s → cache hit
- [ ] Tester re-focus après 5min → cache expired
- [ ] Vérifier que reload Expo nettoie le cache
- [ ] Vérifier qu'en prod, pas de logs RequestGuard
- [ ] **NOUVEAU** : Vérifier qu'il n'y a PLUS de spam "Skip refresh: timeSinceLastRefresh=0s"
- [ ] **NOUVEAU** : Vérifier que getDailyClimate ne refetch pas avant 5min

---

## Références

- **Cache system** :
  - `apps/mobile/utils/requestGuard.ts` (dedup + TTL court terme)
  - `apps/mobile/services/lunarCache.ts` (persistence long terme)
- **Usage** :
  - `apps/mobile/services/api.ts` (lignes 330-353, 519-644)
  - `apps/mobile/contexts/LunarProvider.tsx` (stale-while-revalidate strategy)
- **UX prod** : `apps/mobile/app/lunar/index.tsx` (masquage debug)
- **Tests manuels** : `AUDIT_CACHE_MANUAL_TEST.md` (procédure complète avec logs attendus, à la racine du repo)
