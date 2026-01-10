/**
 * requestGuard - Anti-spam réseau avec dedup + TTL
 *
 * 1) Dédup des requêtes en cours (in-flight)
 * 2) Cache des réponses avec TTL configurable
 */

type CacheEntry<T> = {
  data: T;
  timestamp: number;
};

type GuardOptions = {
  /** TTL du cache en ms (default: 60s) */
  ttl?: number;
  /** Si true, force le refetch même si cache valide */
  forceRefresh?: boolean;
  /** Paramètres optionnels pour construire une clé stable */
  params?: Record<string, any>;
  /** Limite max d’entrées en cache (FIFO simple) */
  maxEntries?: number;
};

// ✅ IMPORTANT : scope module (sinon TS “introuvable”)
const cache = new Map<string, CacheEntry<any>>();
const inFlight = new Map<string, Promise<any>>();

export function getCacheKey(key: string, params?: Record<string, any>): string {
  if (!params || Object.keys(params).length === 0) return key;

  const sortedParams = Object.keys(params)
    .sort()
    .map((k) => `${k}=${JSON.stringify(params[k])}`)
    .join("&");

  return `${key}?${sortedParams}`;
}

function evictIfNeeded(maxEntries: number) {
  if (cache.size <= maxEntries) return;

  // FIFO simple: supprimer la 1ère entrée insérée
  const firstKey = cache.keys().next().value as string | undefined;
  if (firstKey) cache.delete(firstKey);
}

export async function guardedRequest<T>(
  key: string,
  fetcher: () => Promise<T>,
  options: GuardOptions = {}
): Promise<T> {
  const { ttl = 60000, forceRefresh = false, params, maxEntries = 100 } = options;
  const cacheKey = getCacheKey(key, params);

  // 1) Cache hit
  if (!forceRefresh) {
    const cached = cache.get(cacheKey);
    if (cached) {
      const age = Date.now() - cached.timestamp;
      if (age < ttl) {
        if (__DEV__) {
          console.log(
            `[RequestGuard] ✅ Cache hit: ${cacheKey} (age: ${Math.round(age / 1000)}s)`
          );
        }
        return cached.data as T;
      }
      cache.delete(cacheKey);
      if (__DEV__) console.log(`[RequestGuard] ⏱️ Cache expired: ${cacheKey}`);
    }
  }

  // 2) Dédup in-flight
  const existing = inFlight.get(cacheKey);
  if (existing) {
    if (__DEV__) console.log(`[RequestGuard] 🔄 Dedup: ${cacheKey} (request already in-flight)`);
    return existing as Promise<T>;
  }

  if (__DEV__) console.log(`[RequestGuard] 🚀 Fetching: ${cacheKey}`);

  // 3) Fetch + cache + cleanup
  const promise = (async () => {
    try {
      const data = await fetcher();

      cache.set(cacheKey, { data, timestamp: Date.now() });
      evictIfNeeded(maxEntries);

      if (__DEV__) console.log(`[RequestGuard] ✅ Cached: ${cacheKey}`);
      return data;
    } catch (err) {
      if (__DEV__) console.error(`[RequestGuard] ❌ Error: ${cacheKey}`, err);
      throw err;
    } finally {
      inFlight.delete(cacheKey);
    }
  })();

  inFlight.set(cacheKey, promise);
  return promise;
}

export function invalidateCache(key: string, params?: Record<string, any>): void {
  const cacheKey = getCacheKey(key, params);
  cache.delete(cacheKey);
  if (__DEV__) console.log(`[RequestGuard] 🗑️ Cache invalidated: ${cacheKey}`);
}

export function clearAllCache(): void {
  cache.clear();
  inFlight.clear();
  if (__DEV__) console.log("[RequestGuard] 🗑️ All cache cleared");
}

export function getCacheStats(): { cacheSize: number; inFlightSize: number } {
  return { cacheSize: cache.size, inFlightSize: inFlight.size };
}
