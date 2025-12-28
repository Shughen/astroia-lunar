/**
 * Tests Jest pour services/api.ts
 * Vérifie succès, erreurs 500, timeouts
 */

import { auth, lunarReturns, lunaPack, transits, calendar } from '../services/api';

// Mock global fetch
global.fetch = jest.fn();

describe('API Service Tests', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  describe('auth.login', () => {
    it('devrait retourner un token en cas de succès', async () => {
      (global.fetch as jest.Mock).mockResolvedValueOnce({
        ok: true,
        json: async () => ({
          access_token: 'fake_token_123',
          token_type: 'bearer',
        }),
      });

      const result = await auth.login('test@example.com', 'password');

      expect(result.access_token).toBe('fake_token_123');
      expect(global.fetch).toHaveBeenCalledTimes(1);
    });

    it('devrait throw une erreur en cas de 500', async () => {
      (global.fetch as jest.Mock).mockResolvedValueOnce({
        ok: false,
        status: 500,
        statusText: 'Internal Server Error',
      });

      await expect(auth.login('test@example.com', 'password')).rejects.toThrow();
    });
  });

  describe('lunaPack.getCurrentVoc', () => {
    it('devrait retourner le statut VoC', async () => {
      (global.fetch as jest.Mock).mockResolvedValueOnce({
        ok: true,
        json: async () => ({
          is_active: true,
          start_at: '2025-11-11T10:00:00',
          end_at: '2025-11-11T14:00:00',
        }),
      });

      const result = await lunaPack.getCurrentVoc();

      expect(result.is_active).toBe(true);
      expect(global.fetch).toHaveBeenCalledWith(
        expect.stringContaining('/api/lunar/voc/current'),
        expect.any(Object)
      );
    });

    it('devrait gérer les erreurs réseau', async () => {
      (global.fetch as jest.Mock).mockRejectedValueOnce(new Error('Network error'));

      await expect(lunaPack.getCurrentVoc()).rejects.toThrow();
    });
  });

  describe('transits.getNatalTransits', () => {
    it('devrait envoyer le bon payload', async () => {
      const mockPayload = {
        birth_date: '1989-04-15',
        transit_date: '2025-11-11',
      };

      (global.fetch as jest.Mock).mockResolvedValueOnce({
        ok: true,
        json: async () => ({
          provider: 'rapidapi',
          kind: 'natal_transits',
          data: { aspects: [] },
        }),
      });

      await transits.getNatalTransits(mockPayload);

      expect(global.fetch).toHaveBeenCalledWith(
        expect.stringContaining('/api/transits/natal'),
        expect.objectContaining({
          method: 'POST',
          body: JSON.stringify(mockPayload),
        })
      );
    });
  });

  describe('calendar.getMonth', () => {
    it('devrait construire la bonne URL avec query params', async () => {
      (global.fetch as jest.Mock).mockResolvedValueOnce({
        ok: true,
        json: async () => ({
          year: 2025,
          month: 11,
          days: [],
        }),
      });

      await calendar.getMonth(2025, 11);

      expect(global.fetch).toHaveBeenCalledWith(
        expect.stringContaining('/api/calendar/month?year=2025&month=11'),
        expect.any(Object)
      );
    });

    it('devrait gérer les erreurs 404', async () => {
      (global.fetch as jest.Mock).mockResolvedValueOnce({
        ok: false,
        status: 404,
        statusText: 'Not Found',
      });

      await expect(calendar.getMonth(2025, 13)).rejects.toThrow();
    });
  });

  describe('Error Handling', () => {
    it('devrait throw ApiError avec le bon status code', async () => {
      (global.fetch as jest.Mock).mockResolvedValueOnce({
        ok: false,
        status: 502,
        statusText: 'Bad Gateway',
      });

      try {
        await lunaPack.getCurrentVoc();
      } catch (error: any) {
        expect(error.message).toContain('502');
      }
    });

    it('devrait gérer les timeouts', async () => {
      (global.fetch as jest.Mock).mockImplementationOnce(
        () =>
          new Promise((_, reject) =>
            setTimeout(() => reject(new Error('Timeout')), 100)
          )
      );

      await expect(lunaPack.getCurrentVoc()).rejects.toThrow();
    });
  });
});

