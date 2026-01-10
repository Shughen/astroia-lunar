# Audit Cache - Test Manuel Complet

## Vue d'ensemble

Ce document décrit la procédure de test manuel complète pour valider le système de cache anti-spam réseau sur le Luna Pack. Les tests vérifient que les mécanismes `requestGuard` et `lunarCache` fonctionnent correctement ensemble pour éviter les refetch loops et le spam réseau.

---

## Prérequis

1. **Backend démarré** : L'API doit être accessible
   ```bash
   cd apps/api
   ./start_api.sh
   # OU
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

2. **App mobile démarrée** :
   ```bash
   cd apps/mobile
   expo start -c  # -c pour clear cache
   ```

3. **Terminal pour logs backend** :
   ```bash
   # Suivre les logs backend en temps réel
   tail -f apps/api/logs/api.log | grep -E "(daily-climate|voc|mansion)"
   # OU si pas de fichier log, utiliser les logs uvicorn directement
   ```

---

## Test #1 : Cache Hit Immédiat (T+0 → T+30s)

### Objectif
Vérifier qu'un refocus < 5 min après le premier appel utilise le cache et ne génère **aucun** appel backend.

### Procédure

1. **T+0** : Ouvrir l'app, naviguer vers `/lunar` (Luna Pack)
2. **T+0** : Cliquer sur "Daily Climate" (ou laisser LunarProvider charger automatiquement)
3. **Observer les logs console mobile** :
   ```
   [RequestGuard] 🚀 Fetching: lunar/daily-climate?date=2025-01-15
   [RequestGuard] ✅ Cached: lunar/daily-climate?date=2025-01-15
   ```
4. **Vérifier logs backend** : **1 seul appel** `/api/lunar/daily-climate` doit apparaître
5. **T+30s** : Naviguer ailleurs (ex: `/settings`), puis revenir sur `/lunar`
6. **T+30s** : Cliquer à nouveau "Daily Climate" (ou laisser LunarProvider recharger)
7. **Observer les logs console mobile** :
   ```
   [RequestGuard] ✅ Cache hit: lunar/daily-climate?date=2025-01-15 (age: 30s)
   ```
8. **Vérifier logs backend** : **Aucun nouvel appel** ne doit apparaître

### ✅ Critères d'acceptation

- [ ] T+0 : 1 seul call backend `/api/lunar/daily-climate`
- [ ] T+30s : Cache hit → 0 call backend
- [ ] Logs console montrent "Cache hit" avec age < 5min

---

## Test #2 : Cache Expiré (T+6min)

### Objectif
Vérifier que le cache expire après 5 minutes et qu'un nouveau fetch est lancé.

### Procédure

1. **T+0** : Ouvrir `/lunar`, cliquer "Daily Climate"
2. **Observer** : 1 appel backend, cache créé
3. **Attendre 6 minutes** (ou modifier temporairement le TTL à 10s pour test rapide)
4. **T+6min** : Cliquer à nouveau "Daily Climate"
5. **Observer les logs console mobile** :
   ```
   [RequestGuard] ⏱️ Cache expired: lunar/daily-climate?date=2025-01-15
   [RequestGuard] 🚀 Fetching: lunar/daily-climate?date=2025-01-15
   [RequestGuard] ✅ Cached: lunar/daily-climate?date=2025-01-15
   ```
6. **Vérifier logs backend** : **1 nouvel appel** doit apparaître

### ✅ Critères d'acceptation

- [ ] T+6min : Cache expired → 1 nouveau call backend
- [ ] Cache recréé après le fetch
- [ ] Logs montrent "Cache expired" puis "Fetching"

---

## Test #3 : Déduplication In-Flight (Double Clic Rapide)

### Objectif
Vérifier que 2 appels simultanés (< 1s) sont dédupliqués en 1 seul appel backend.

### Procédure

1. **Ouvrir `/lunar`**
2. **Double clic rapide** (< 1s) sur "Daily Climate" (ou modifier temporairement le code pour appeler 2 fois en parallèle)
3. **Observer les logs console mobile** :
   ```
   [RequestGuard] 🚀 Fetching: lunar/daily-climate?date=2025-01-15
   [RequestGuard] 🔄 Dedup: lunar/daily-climate?date=2025-01-15 (request already in-flight)
   [RequestGuard] ✅ Cached: lunar/daily-climate?date=2025-01-15
   ```
4. **Vérifier logs backend** : **1 seul appel** doit apparaître

### ✅ Critères d'acceptation

- [ ] Double clic rapide → 1 seul call backend
- [ ] Logs montrent "Dedup" pour le 2e appel
- [ ] Les 2 promesses résolvent avec la même valeur

---

## Test #4 : Cache Key Stable (VOC/Mansion/DailyClimate)

### Objectif
Vérifier que les endpoints utilisent uniquement `{date}` dans la cache key (time exclu), évitant les refetch minute par minute.

### Procédure

1. **T+0** : Ouvrir `/lunar`, cliquer "Void of Course"
   - Observer la cache key : `lunar/voc?date=2025-01-15` (pas de time)
2. **T+1min** : Cliquer à nouveau "Void of Course"
   - Observer : Cache hit (même clé, même date)
3. **T+0** : Cliquer "Lunar Mansion"
   - Observer la cache key : `lunar/mansion?date=2025-01-15` (pas de time)
4. **T+1min** : Cliquer à nouveau "Lunar Mansion"
   - Observer : Cache hit (même clé, même date)
5. **T+0** : Cliquer "Daily Climate"
   - Observer la cache key : `lunar/daily-climate?date=2025-01-15` (pas de time)
6. **T+1min** : Cliquer à nouveau "Daily Climate"
   - Observer : Cache hit (même clé, même date)

### ✅ Critères d'acceptation

- [ ] Cache keys ne contiennent **jamais** `time` (uniquement `date`)
- [ ] Refocus après 1min → Cache hit (pas de refetch)
- [ ] Le payload complet (avec time si applicable) est toujours envoyé au backend, mais la cache key ignore time

---

## Test #5 : LunarProvider Anti-Refresh Loop

### Objectif
Vérifier que LunarProvider ne génère **plus jamais** de spam "Skip refresh: timeSinceLastRefresh=0s" en boucle.

### Procédure

1. **Ouvrir l'app** (LunarProvider se monte automatiquement)
2. **Observer les logs console mobile** :
   ```
   [LunarProvider] Cache stale, refreshing in background...
   # OU
   [LunarProvider] Skip refresh: inFlight=true, timeSinceLastRefresh=45s
   ```
3. **Naviguer rapidement** : `/lunar` → `/settings` → `/lunar` → `/settings` (x5)
4. **Observer les logs** : **Aucun spam** de "Skip refresh: timeSinceLastRefresh=0s"
5. **Vérifier logs backend** : Maximum 1-2 appels `/api/lunar/daily-climate` (pas de boucle)

### ✅ Critères d'acceptation

- [ ] Plus jamais de spam "Skip refresh: timeSinceLastRefresh=0s" en boucle
- [ ] Maximum 1-2 appels backend même avec navigation rapide
- [ ] Guards anti-refresh fonctionnent (REFRESH_TTL_MS = 60s)

---

## Test #6 : Stale Cache (lunarCache 1h)

### Objectif
Vérifier que le système `lunarCache` (AsyncStorage) fonctionne avec stale-while-revalidate.

### Procédure

1. **T+0** : Ouvrir l'app, laisser LunarProvider charger
2. **Observer** : Données chargées depuis API ou cache
3. **Fermer l'app complètement** (kill process)
4. **T+2h** : Rouvrir l'app
5. **Observer les logs** :
   ```
   [LunarProvider] Cache stale, refreshing in background...
   ```
6. **Vérifier** : Les données s'affichent immédiatement (cache stale) puis se rafraîchissent en background

### ✅ Critères d'acceptation

- [ ] Cache stale affiché immédiatement (pas de loading)
- [ ] Refresh en background si stale > 1h
- [ ] Pas de refetch si cache < 1h

---

## Commandes Terminal Utiles

### Backend - Suivre les logs en temps réel

```bash
# Option 1 : Si fichier log existe
tail -f apps/api/logs/api.log | grep -E "(daily-climate|voc|mansion)"

# Option 2 : Logs uvicorn directement (si pas de fichier log)
# Les logs apparaissent dans le terminal où uvicorn tourne

# Option 3 : Filtrer par endpoint spécifique
tail -f apps/api/logs/api.log | rg "GET.*daily-climate"
tail -f apps/api/logs/api.log | rg "POST.*voc"
```

### Mobile - Clear cache et redémarrer

```bash
cd apps/mobile
expo start -c  # -c pour clear cache Metro
```

### Vérifier les stats du cache (dans console mobile)

```javascript
// Dans la console Expo
import { getCacheStats } from './utils/requestGuard';
console.log(getCacheStats());
// Output: { cacheSize: 3, inFlightSize: 0 }
```

---

## Logs Attendus (Résumé)

### ✅ Comportement Normal

```
# Premier appel
[RequestGuard] 🚀 Fetching: lunar/daily-climate?date=2025-01-15
[RequestGuard] ✅ Cached: lunar/daily-climate?date=2025-01-15

# Cache hit (< 5min)
[RequestGuard] ✅ Cache hit: lunar/daily-climate?date=2025-01-15 (age: 30s)

# Dedup in-flight
[RequestGuard] 🔄 Dedup: lunar/daily-climate?date=2025-01-15 (request already in-flight)

# Cache expired (> 5min)
[RequestGuard] ⏱️ Cache expired: lunar/daily-climate?date=2025-01-15
[RequestGuard] 🚀 Fetching: lunar/daily-climate?date=2025-01-15

# LunarProvider refresh guard
[LunarProvider] Skip refresh: inFlight=false, timeSinceLastRefresh=45s
```

### ⚠️ Signaux d'Alerte (Problèmes)

```
# Spam réseau (problème)
[RequestGuard] 🚀 Fetching: lunar/daily-climate
[RequestGuard] 🚀 Fetching: lunar/daily-climate  # ⚠️ Pas de dedup !

# Refresh loop (problème)
[LunarProvider] Skip refresh: timeSinceLastRefresh=0s
[LunarProvider] Skip refresh: timeSinceLastRefresh=0s  # ⚠️ En boucle !

# Cache key instable (problème)
[RequestGuard] 🚀 Fetching: lunar/daily-climate?date=2025-01-15&time=10:30
[RequestGuard] 🚀 Fetching: lunar/daily-climate?date=2025-01-15&time=10:31  # ⚠️ Time dans la clé !
```

---

## Checklist Finale

- [ ] **Test #1** : T+0 → T+30s → Cache hit, 0 call backend
- [ ] **Test #2** : T+6min → Cache expired, 1 nouveau call backend
- [ ] **Test #3** : Double clic rapide → Dedup, 1 seul call backend
- [ ] **Test #4** : Cache keys stables (date uniquement, time exclu)
- [ ] **Test #5** : Plus de spam "Skip refresh: timeSinceLastRefresh=0s"
- [ ] **Test #6** : Stale cache fonctionne (lunarCache AsyncStorage)

---

## Dépannage

### Problème : Cache ne s'active pas

**Cause** : Clés de cache instables (payload différent à chaque appel)

**Solution** : Vérifier que `getCacheKey()` génère des clés stables. Les endpoints `voc`, `mansion`, `daily-climate` doivent utiliser uniquement `{date}` dans les params.

### Problème : Refresh loop dans LunarProvider

**Cause** : Dépendances instables dans `loadLunarData` ou `currentDay` qui change

**Solution** : Vérifier que :
- `currentDay` est en `useRef(...).current` (stable)
- `loadLunarData` a des deps `[]` (stable)
- Guards anti-refresh sont actifs (`REFRESH_TTL_MS = 60000`)

### Problème : Cache ne se vide jamais

**Cause** : TTL trop long ou pas de reload

**Solution** :
- Vérifier le TTL dans `services/api.ts` (300000ms = 5min pour daily-climate)
- Appeler `clearAllCache()` au logout si nécessaire

---

## Références

- **requestGuard** : `apps/mobile/utils/requestGuard.ts` (dedup + TTL court terme)
- **lunarCache** : `apps/mobile/services/lunarCache.ts` (persistence long terme)
- **API endpoints** : `apps/mobile/services/api.ts` (lignes 544-644)
- **LunarProvider** : `apps/mobile/contexts/LunarProvider.tsx` (stale-while-revalidate)
- **Documentation générale** : `apps/mobile/TESTS_NETWORK_GUARD.md`
