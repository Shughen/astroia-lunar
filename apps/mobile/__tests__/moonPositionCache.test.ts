/**
 * Tests pour le cache quotidien de position lunaire
 */

import AsyncStorage from '@react-native-async-storage/async-storage';
import { getMoonPositionWithCache, clearMoonPositionCache } from '../services/moonPositionCache';

// Mock getCurrentMoonPosition
jest.mock('../services/moonPosition', () => ({
  getCurrentMoonPosition: jest.fn(() => Promise.resolve({
    sign: 'Gemini',
    degree: 67.5,
    phase: 'Premier Quartier'
  }))
}));

describe('moonPositionCache', () => {
  beforeEach(async () => {
    // Clear cache avant chaque test
    await clearMoonPositionCache();
    jest.clearAllMocks();
  });

  afterEach(async () => {
    await clearMoonPositionCache();
  });

  it('devrait fetcher l\'API au premier appel (cache miss)', async () => {
    const { getCurrentMoonPosition } = require('../services/moonPosition');

    const result = await getMoonPositionWithCache();

    expect(result).toEqual({
      sign: 'Gemini',
      degree: 67.5,
      phase: 'Premier Quartier'
    });

    // Vérifier que l'API a été appelée
    expect(getCurrentMoonPosition).toHaveBeenCalledTimes(1);
  });

  it('devrait utiliser le cache au 2e appel le même jour (cache hit)', async () => {
    const { getCurrentMoonPosition } = require('../services/moonPosition');

    // 1er appel
    const result1 = await getMoonPositionWithCache();
    expect(getCurrentMoonPosition).toHaveBeenCalledTimes(1);

    // 2e appel (cache hit)
    const result2 = await getMoonPositionWithCache();
    expect(result2).toEqual(result1);

    // L'API ne doit PAS être appelée une 2e fois
    expect(getCurrentMoonPosition).toHaveBeenCalledTimes(1);
  });

  it('devrait force refresh si demandé', async () => {
    const { getCurrentMoonPosition } = require('../services/moonPosition');

    // 1er appel
    await getMoonPositionWithCache();
    expect(getCurrentMoonPosition).toHaveBeenCalledTimes(1);

    // 2e appel avec force refresh
    await getMoonPositionWithCache(true);

    // L'API doit être appelée une 2e fois
    expect(getCurrentMoonPosition).toHaveBeenCalledTimes(2);
  });

  it('devrait sauvegarder en AsyncStorage', async () => {
    await getMoonPositionWithCache();

    // Vérifier que les données sont en AsyncStorage
    const cachedDate = await AsyncStorage.getItem('moonPosition_cache_date');
    const cachedData = await AsyncStorage.getItem('moonPosition_cache');

    expect(cachedDate).toBeTruthy();
    expect(cachedData).toBeTruthy();

    const parsed = JSON.parse(cachedData!);
    expect(parsed).toEqual({
      sign: 'Gemini',
      degree: 67.5,
      phase: 'Premier Quartier'
    });
  });

  it('clearMoonPositionCache devrait effacer le cache', async () => {
    // Créer un cache
    await getMoonPositionWithCache();

    let cachedData = await AsyncStorage.getItem('moonPosition_cache');
    expect(cachedData).toBeTruthy();

    // Effacer le cache
    await clearMoonPositionCache();

    // Vérifier que le cache est vide
    cachedData = await AsyncStorage.getItem('moonPosition_cache');
    const cachedDate = await AsyncStorage.getItem('moonPosition_cache_date');

    expect(cachedData).toBeNull();
    expect(cachedDate).toBeNull();
  });
});
