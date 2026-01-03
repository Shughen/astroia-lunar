/**
 * Tests unitaires pour requestGuard
 * Vérifie le dedup, le cache TTL, et la gestion des params
 */

import { guardedRequest, getCacheKey, invalidateCache, clearAllCache, getCacheStats } from '../requestGuard';

// Mock __DEV__ pour les tests
(global as any).__DEV__ = false;

describe('requestGuard', () => {
  beforeEach(() => {
    // Nettoyer le cache avant chaque test
    clearAllCache();
  });

  describe('getCacheKey', () => {
    it('retourne la clé simple si params absent', () => {
      expect(getCacheKey('test-key')).toBe('test-key');
    });

    it('retourne la clé simple si params vide', () => {
      expect(getCacheKey('test-key', {})).toBe('test-key');
    });

    it('génère des clés différentes pour des params différents', () => {
      const key1 = getCacheKey('x', { a: 1 });
      const key2 = getCacheKey('x', { a: 2 });
      expect(key1).not.toBe(key2);
      expect(key1).toBe('x?a=1');
      expect(key2).toBe('x?a=2');
    });

    it('génère des clés stables pour des params identiques (ordre différent)', () => {
      const key1 = getCacheKey('x', { a: 1, b: 2 });
      const key2 = getCacheKey('x', { b: 2, a: 1 });
      expect(key1).toBe(key2);
    });

    it('gère les valeurs complexes dans params', () => {
      const key = getCacheKey('test', { date: '2025-01-15', month: '2025-01' });
      expect(key).toContain('date');
      expect(key).toContain('month');
      expect(key).toContain('2025-01-15');
    });
  });

  describe('guardedRequest - dedup inflight', () => {
    it('déduplique 2 appels simultanés avec même cacheKey', async () => {
      let fetchCount = 0;
      const fetcher = jest.fn(async () => {
        fetchCount++;
        await new Promise((resolve) => setTimeout(resolve, 10));
        return { data: 'result' };
      });

      // 2 appels simultanés avec même clé
      const promise1 = guardedRequest('test-key', fetcher);
      const promise2 = guardedRequest('test-key', fetcher);

      const [result1, result2] = await Promise.all([promise1, promise2]);

      // Le fetcher ne doit être appelé qu'une seule fois
      expect(fetchCount).toBe(1);
      expect(result1).toEqual({ data: 'result' });
      expect(result2).toEqual({ data: 'result' });
    });

    it('déduplique avec params identiques', async () => {
      let fetchCount = 0;
      const fetcher = jest.fn(async () => {
        fetchCount++;
        return { data: 'result' };
      });

      const params = { date: '2025-01-15', month: '2025-01' };
      const promise1 = guardedRequest('test-key', fetcher, { params });
      const promise2 = guardedRequest('test-key', fetcher, { params });

      await Promise.all([promise1, promise2]);

      expect(fetchCount).toBe(1);
    });

    it('ne déduplique pas si params différents', async () => {
      let fetchCount = 0;
      const fetcher = jest.fn(async () => {
        fetchCount++;
        return { data: 'result' };
      });

      const promise1 = guardedRequest('test-key', fetcher, { params: { date: '2025-01-15' } });
      const promise2 = guardedRequest('test-key', fetcher, { params: { date: '2025-01-16' } });

      await Promise.all([promise1, promise2]);

      expect(fetchCount).toBe(2);
    });

    it('nettoie inFlight même en cas d\'erreur', async () => {
      const fetcher = jest.fn(async () => {
        throw new Error('Test error');
      });

      const promise = guardedRequest('test-key', fetcher);

      await expect(promise).rejects.toThrow('Test error');

      // Vérifier que inFlight est nettoyé
      const stats = getCacheStats();
      expect(stats.inFlightSize).toBe(0);
    });
  });

  describe('guardedRequest - cache TTL', () => {
    beforeEach(() => {
      jest.useFakeTimers();
    });

    afterEach(() => {
      jest.useRealTimers();
    });

    it('retourne le cache si TTL valide', async () => {
      let fetchCount = 0;
      const fetcher = jest.fn(async () => {
        fetchCount++;
        return { data: 'cached' };
      });

      // Premier appel
      const result1 = await guardedRequest('test-key', fetcher, { ttl: 5000 });
      expect(fetchCount).toBe(1);
      expect(result1).toEqual({ data: 'cached' });

      // Deuxième appel immédiat (cache hit)
      const result2 = await guardedRequest('test-key', fetcher, { ttl: 5000 });
      expect(fetchCount).toBe(1); // Pas de nouveau fetch
      expect(result2).toEqual({ data: 'cached' });
    });

    it('refetch si TTL expiré', async () => {
      let fetchCount = 0;
      const fetcher = jest.fn(async () => {
        fetchCount++;
        return { data: `result-${fetchCount}` };
      });

      // Premier appel
      const result1 = await guardedRequest('test-key', fetcher, { ttl: 5000 });
      expect(fetchCount).toBe(1);
      expect(result1).toEqual({ data: 'result-1' });

      // Avancer le temps de 6 secondes (TTL expiré)
      jest.advanceTimersByTime(6000);

      // Deuxième appel (cache expiré, refetch)
      const result2 = await guardedRequest('test-key', fetcher, { ttl: 5000 });
      expect(fetchCount).toBe(2);
      expect(result2).toEqual({ data: 'result-2' });
    });

    it('forceRefresh ignore le cache', async () => {
      let fetchCount = 0;
      const fetcher = jest.fn(async () => {
        fetchCount++;
        return { data: 'result' };
      });

      // Premier appel
      await guardedRequest('test-key', fetcher, { ttl: 5000 });
      expect(fetchCount).toBe(1);

      // Deuxième appel avec forceRefresh
      await guardedRequest('test-key', fetcher, { ttl: 5000, forceRefresh: true });
      expect(fetchCount).toBe(2);
    });
  });

  describe('invalidateCache', () => {
    it('invalide une clé simple', async () => {
      let fetchCount = 0;
      const fetcher = jest.fn(async () => {
        fetchCount++;
        return { data: 'result' };
      });

      // Premier appel (cache)
      await guardedRequest('test-key', fetcher, { ttl: 5000 });
      expect(fetchCount).toBe(1);

      // Invalider
      invalidateCache('test-key');

      // Deuxième appel (refetch car invalidé)
      await guardedRequest('test-key', fetcher, { ttl: 5000 });
      expect(fetchCount).toBe(2);
    });

    it('invalide une clé avec params', async () => {
      let fetchCount = 0;
      const fetcher = jest.fn(async () => {
        fetchCount++;
        return { data: 'result' };
      });

      const params = { date: '2025-01-15' };

      // Premier appel
      await guardedRequest('test-key', fetcher, { ttl: 5000, params });
      expect(fetchCount).toBe(1);

      // Invalider avec params
      invalidateCache('test-key', params);

      // Deuxième appel (refetch)
      await guardedRequest('test-key', fetcher, { ttl: 5000, params });
      expect(fetchCount).toBe(2);
    });

    it('n\'invalide pas si params différents', async () => {
      let fetchCount = 0;
      const fetcher = jest.fn(async () => {
        fetchCount++;
        return { data: 'result' };
      });

      // Premier appel avec params1
      await guardedRequest('test-key', fetcher, { ttl: 5000, params: { date: '2025-01-15' } });
      expect(fetchCount).toBe(1);

      // Invalider avec params2 différents
      invalidateCache('test-key', { date: '2025-01-16' });

      // Deuxième appel avec params1 (cache toujours valide)
      await guardedRequest('test-key', fetcher, { ttl: 5000, params: { date: '2025-01-15' } });
      expect(fetchCount).toBe(1); // Cache hit
    });
  });

  describe('getCacheStats', () => {
    it('retourne les stats correctes', async () => {
      const fetcher = jest.fn(async () => ({ data: 'result' }));

      expect(getCacheStats()).toEqual({ cacheSize: 0, inFlightSize: 0 });

      await guardedRequest('test-key', fetcher);
      const stats = getCacheStats();
      expect(stats.cacheSize).toBe(1);
      expect(stats.inFlightSize).toBe(0);
    });
  });
});

