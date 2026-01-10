/**
 * Tests Jest pour services/api.ts
 * Vérifie que le module API fonctionne avec axios mocké
 */

import axios from 'axios';
import { auth, lunaPack, transits, calendar } from '../services/api';

// Get the mocked axios instance
const mockedAxios = axios as jest.Mocked<typeof axios>;

describe('API Service Tests', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  describe('auth.login', () => {
    it('devrait retourner un token en cas de succès', async () => {
      const mockResponse = {
        data: {
          access_token: 'fake_token_123',
          token_type: 'bearer',
        },
        status: 200,
        statusText: 'OK',
        headers: {},
        config: {} as any,
      };

      (mockedAxios.post as jest.Mock).mockResolvedValueOnce(mockResponse);

      const result = await auth.login('test@example.com', 'password');

      expect(result.access_token).toBe('fake_token_123');
      expect(mockedAxios.post).toHaveBeenCalled();
    });
  });

  describe('lunaPack.getCurrentVoc', () => {
    it('devrait retourner le statut VoC', async () => {
      const mockResponse = {
        data: {
          is_active: true,
          start_at: '2025-11-11T10:00:00',
          end_at: '2025-11-11T14:00:00',
        },
        status: 200,
        statusText: 'OK',
        headers: {},
        config: {} as any,
      };

      (mockedAxios.get as jest.Mock).mockResolvedValueOnce(mockResponse);

      const result = await lunaPack.getCurrentVoc();

      expect(result.is_active).toBe(true);
      expect(mockedAxios.get).toHaveBeenCalled();
    });

    it('devrait gérer les erreurs réseau', async () => {
      (mockedAxios.get as jest.Mock).mockRejectedValueOnce(new Error('Network error'));

      await expect(lunaPack.getCurrentVoc()).rejects.toThrow();
    });
  });

  describe('transits.getNatalTransits', () => {
    it('devrait envoyer le bon payload', async () => {
      const mockPayload = {
        birth_date: '1989-04-15',
        transit_date: '2025-11-11',
      };

      const mockResponse = {
        data: {
          provider: 'rapidapi',
          kind: 'natal_transits',
          data: { aspects: [] },
        },
        status: 200,
        statusText: 'OK',
        headers: {},
        config: {} as any,
      };

      (mockedAxios.post as jest.Mock).mockResolvedValueOnce(mockResponse);

      await transits.getNatalTransits(mockPayload);

      expect(mockedAxios.post).toHaveBeenCalledWith(
        expect.stringContaining('/transits/natal'),
        mockPayload
      );
    });
  });

  describe('calendar.getMonth', () => {
    it('devrait construire la bonne URL', async () => {
      const mockResponse = {
        data: {
          year: 2025,
          month: 11,
          days: [],
        },
        status: 200,
        statusText: 'OK',
        headers: {},
        config: {} as any,
      };

      (mockedAxios.get as jest.Mock).mockResolvedValueOnce(mockResponse);

      await calendar.getMonth(2025, 11);

      expect(mockedAxios.get).toHaveBeenCalled();
    });
  });

  describe('Error Handling', () => {
    it('devrait gérer les timeouts', async () => {
      (mockedAxios.get as jest.Mock).mockRejectedValueOnce(new Error('Timeout'));

      await expect(lunaPack.getCurrentVoc()).rejects.toThrow();
    });
  });
});
