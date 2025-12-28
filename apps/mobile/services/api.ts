/**
 * Client API pour backend FastAPI
 */

import axios from 'axios';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { Platform } from 'react-native';

// Configuration BaseURL avec fallbacks selon la plateforme
const getBaseURL = (): string => {
  // Priorité absolue : EXPO_PUBLIC_API_URL si défini
  if (process.env.EXPO_PUBLIC_API_URL) {
    return process.env.EXPO_PUBLIC_API_URL;
  }
  
  // Fallback pour simulateurs/web uniquement
  const isWeb = Platform.OS === 'web';
  const isSimulator = Platform.OS === 'ios' || Platform.OS === 'android';
  
  if (isWeb) {
    // Web : localhost fonctionne
    return 'http://localhost:8000';
  }
  
  if (Platform.OS === 'ios') {
    // iOS Simulator : localhost fonctionne
    // Device physique : nécessite EXPO_PUBLIC_API_URL avec IP locale
    console.warn(
      '⚠️ EXPO_PUBLIC_API_URL non défini. ' +
      'Sur device physique iOS, utilisez l\'IP locale de votre Mac (ex: http://192.168.0.150:8000). ' +
      'Fallback localhost utilisé (ne fonctionnera pas sur device physique).'
    );
    return 'http://127.0.0.1:8000';
  }
  
  if (Platform.OS === 'android') {
    // Android Emulator : 10.0.2.2 fonctionne
    // Device physique : nécessite EXPO_PUBLIC_API_URL avec IP locale
    console.warn(
      '⚠️ EXPO_PUBLIC_API_URL non défini. ' +
      'Sur device physique Android, utilisez l\'IP locale de votre machine (ex: http://192.168.0.150:8000). ' +
      'Fallback 10.0.2.2 utilisé (ne fonctionnera pas sur device physique).'
    );
    return 'http://10.0.2.2:8000';
  }
  
  // Fallback par défaut
  return 'http://localhost:8000';
};

const API_URL = getBaseURL();

// Log de la baseURL choisie au démarrage (utile pour debug réseau)
console.log(`🔗 API BaseURL: ${API_URL}`);

const apiClient = axios.create({
  baseURL: API_URL,
  timeout: 30000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Mode DEV_AUTH_BYPASS: détection et configuration
const DEV_AUTH_BYPASS = process.env.EXPO_PUBLIC_DEV_AUTH_BYPASS === 'true';
const DEV_USER_ID = process.env.EXPO_PUBLIC_DEV_USER_ID || '1';

// Intercepteur pour ajouter le token ou le header DEV_AUTH_BYPASS
apiClient.interceptors.request.use(
  async (config) => {
    if (DEV_AUTH_BYPASS) {
      // Mode bypass: utiliser X-Dev-User-Id au lieu du token JWT
      config.headers['X-Dev-User-Id'] = DEV_USER_ID;
      console.log('[API] Mode DEV_AUTH_BYPASS actif, header X-Dev-User-Id:', DEV_USER_ID);
      // Ne PAS envoyer Authorization Bearer en mode bypass
    } else {
      // Mode normal: utiliser le token JWT
      const token = await AsyncStorage.getItem('auth_token');
      if (token) {
        config.headers.Authorization = `Bearer ${token}`;
        console.log('[API] Token JWT ajouté au header Authorization');
      } else {
        console.warn('[API] ⚠️ Aucun token trouvé dans AsyncStorage');
      }
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// Export pour vérifier si le mode bypass est actif
export const isDevAuthBypassActive = () => DEV_AUTH_BYPASS;
export const getDevUserId = () => DEV_USER_ID;

// Export de la fonction getApiUrl pour utilisation dans selftest.tsx
export const getApiUrl = (): string => {
  return API_URL;
};

// === HEALTH ===
export const health = {
  check: async () => {
    const response = await apiClient.get('/health');
    return response.data;
  },
};

// === AUTH ===
export const auth = {
  register: async (email: string, password: string, birthData?: any) => {
    const response = await apiClient.post('/api/auth/register', {
      email,
      password,
      ...birthData,
    });
    const { access_token } = response.data;
    await AsyncStorage.setItem('auth_token', access_token);
    return response.data;
  },

  login: async (email: string, password: string) => {
    // OAuth2PasswordRequestForm attend application/x-www-form-urlencoded
    const params = new URLSearchParams();
    params.append('username', email);
    params.append('password', password);
    
    const response = await apiClient.post('/api/auth/login', params.toString(), {
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    });
    
    const { access_token } = response.data;
    console.log('[Auth] Token reçu:', access_token ? `${access_token.substring(0, 20)}...` : 'null');
    await AsyncStorage.setItem('auth_token', access_token);
    console.log('[Auth] Token stocké dans AsyncStorage');
    
    // Vérifier que le token est bien stocké
    const storedToken = await AsyncStorage.getItem('auth_token');
    console.log('[Auth] Token vérifié après stockage:', storedToken ? `${storedToken.substring(0, 20)}...` : 'null');
    
    return response.data;
  },

  logout: async () => {
    await AsyncStorage.removeItem('auth_token');
  },

  getMe: async () => {
    const response = await apiClient.get('/api/auth/me');
    return response.data;
  },
};

// === NATAL CHART ===
export const natalChart = {
  calculate: async (data: {
    date: string;
    time: string;
    latitude: number;
    longitude: number;
    place_name: string;
    timezone?: string;
  }) => {
    const response = await apiClient.post('/api/natal-chart', data);
    return response.data;
  },

  get: async () => {
    const response = await apiClient.get('/api/natal-chart');
    return response.data;
  },

  // Calcul via RapidAPI (pass-through)
  calculateExternal: async (payload: any) => {
    const response = await apiClient.post('/api/natal-chart/external', payload);
    return response.data;
  },
};

// === LUNAR RETURNS ===
export interface LunarReturn {
  id: number;
  return_date: string; // ISO 8601 timestamptz
  month?: string; // YYYY-MM (legacy)
  moon_sign?: string;
  moon_house?: number;
  lunar_ascendant?: string;
  aspects?: Array<{
    planet1?: string;
    planet2?: string;
    type?: string;
    orb?: number;
    [key: string]: any;
  }>;
  interpretation?: string;
}

export const lunarReturns = {
  /**
   * Récupère le prochain retour lunaire (>= maintenant)
   */
  getNext: async (): Promise<LunarReturn | null> => {
    try {
      const response = await apiClient.get('/api/lunar-returns/next');
      return response.data;
    } catch (error: any) {
      if (error.response?.status === 404) {
        return null;
      }
      throw error;
    }
  },

  /**
   * Récupère tous les retours lunaires d'une année
   */
  getYear: async (year: number): Promise<LunarReturn[]> => {
    const response = await apiClient.get(`/api/lunar-returns/year/${year}`);
    return response.data;
  },

  /**
   * Récupère les 12 prochains retours lunaires (rolling) - idéal pour timeline MVP
   */
  getRolling: async (): Promise<LunarReturn[]> => {
    const response = await apiClient.get('/api/lunar-returns/rolling');
    return response.data;
  },

  /**
   * Génère les 12 révolutions lunaires de l'année en cours
   */
  generate: async (): Promise<void> => {
    await apiClient.post('/api/lunar-returns/generate');
  },
};

// === MENSTRUAL CYCLE ===
export const menstrualCycle = {
  start: async (data: {
    start_date: string;
    end_date?: string;
    cycle_length?: number;
    period_length?: number;
    notes?: string;
    symptoms?: string;
  }) => {
    const response = await apiClient.post('/api/menstrual-cycle/start', data);
    return response.data;
  },

  getCurrent: async () => {
    const response = await apiClient.get('/api/menstrual-cycle/current');
    return response.data;
  },

  getHistory: async (limit: number = 12) => {
    const response = await apiClient.get(`/api/menstrual-cycle/history?limit=${limit}`);
    return response.data;
  },

  update: async (cycleId: number, data: {
    end_date?: string;
    cycle_length?: number;
    period_length?: number;
    notes?: string;
    symptoms?: string;
  }) => {
    const response = await apiClient.put(`/api/menstrual-cycle/${cycleId}`, data);
    return response.data;
  },

  getCorrelation: async () => {
    const response = await apiClient.get('/api/menstrual-cycle/correlation');
    return response.data;
  },
};

// === CALENDAR ===
export const calendar = {
  /**
   * Récupère le calendrier mensuel avec phases lunaires et événements
   * @param year Année (ex: 2025)
   * @param month Mois (1-12)
   * @param latitude Latitude optionnelle (défaut: 48.8566)
   * @param longitude Longitude optionnelle (défaut: 2.3522)
   * @param timezone Timezone optionnelle (défaut: "Europe/Paris")
   */
  getMonth: async (
    year: number,
    month: number,
    latitude?: number,
    longitude?: number,
    timezone?: string
  ) => {
    const params = new URLSearchParams();
    params.append('year', year.toString());
    params.append('month', month.toString());
    if (latitude !== undefined) params.append('latitude', latitude.toString());
    if (longitude !== undefined) params.append('longitude', longitude.toString());
    if (timezone) params.append('timezone', timezone);

    const response = await apiClient.get(`/api/calendar/month?${params.toString()}`);
    return response.data;
  },
};

// === TRANSITS ===
export const transits = {
  /**
   * Récupère la vue d'ensemble des transits pour un utilisateur et un mois
   * @param userId ID de l'utilisateur
   * @param month Mois au format YYYY-MM (ex: "2025-01")
   * @param token Token d'authentification (optionnel, sera ajouté automatiquement par l'intercepteur)
   */
  getOverview: async (userId: number, month: string, token?: string) => {
    // Le token est géré automatiquement par l'intercepteur axios
    // On peut le passer explicitement si nécessaire, sinon l'intercepteur le récupère d'AsyncStorage
    const response = await apiClient.get(`/api/transits/overview/${userId}/${month}`);
    return response.data;
  },

  /**
   * Récupère les transits natals pour une date donnée
   * @param payload Données de naissance et date de transit
   */
  getNatalTransits: async (payload: {
    birth_date: string;
    birth_time?: string;
    birth_latitude?: number;
    birth_longitude?: number;
    transit_date: string;
    [key: string]: any;
  }) => {
    const response = await apiClient.post('/api/transits/natal', payload);
    return response.data;
  },
};

// === LUNAR PACK ===
/**
 * Fonction standalone pour obtenir le rapport de révolution lunaire
 */
export const getLunarReturnReport = async (payload: {
  birth_date: string;
  birth_time: string;
  latitude: number;
  longitude: number;
  timezone: string;
  date: string;
  month?: string;
  [key: string]: any;
}) => {
  const response = await apiClient.post('/api/lunar/return/report', payload);
  return response.data;
};

/**
 * Fonction standalone pour obtenir le statut Void of Course
 */
export const getVoidOfCourse = async (payload: {
  date: string;
  time: string;
  latitude: number;
  longitude: number;
  timezone: string;
  [key: string]: any;
}) => {
  const response = await apiClient.post('/api/lunar/voc', payload);
  return response.data;
};

/**
 * Fonction standalone pour obtenir la mansion lunaire
 */
export const getLunarMansion = async (payload: {
  date: string;
  time?: string;
  latitude: number;
  longitude: number;
  timezone: string;
  [key: string]: any;
}) => {
  const response = await apiClient.post('/api/lunar/mansion', payload);
  return response.data;
};

/**
 * Objet Luna Pack avec méthodes utilitaires
 */
export const lunaPack = {
  /**
   * Récupère le statut Void of Course actuel depuis le cache
   */
  getCurrentVoc: async () => {
    const response = await apiClient.get('/api/lunar/voc/current');
    return response.data;
  },
};

export default apiClient;

