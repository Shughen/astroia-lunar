/**
 * Client API pour backend FastAPI
 */

import axios from 'axios';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { Platform } from 'react-native';
import Constants from 'expo-constants';

// Détection device physique vs simulateur
const isPhysicalDevice = (): boolean => {
  // Expo Go sur device physique : deviceName est défini et n'est pas "Simulator"
  const deviceName = Constants.deviceName;
  if (deviceName) {
    const isSimulator = deviceName.toLowerCase().includes('simulator') || 
                       deviceName.toLowerCase().includes('emulator');
    return !isSimulator;
  }
  // Si deviceName n'est pas disponible, on assume device physique si pas web
  return Platform.OS !== 'web';
};

// Récupération de l'IP LAN depuis Expo debugger (si disponible)
const getLanIPFromExpo = (): string | null => {
  try {
    // Expo peut exposer l'IP du debugger via Constants
    const debuggerHost = Constants.expoConfig?.extra?.debuggerHost;
    if (debuggerHost) {
      // Extraire l'IP depuis debuggerHost (format: "192.168.0.150:8081")
      const match = debuggerHost.match(/^(\d+\.\d+\.\d+\.\d+)/);
      if (match) {
        return match[1];
      }
    }
  } catch (e) {
    // Ignorer les erreurs
  }
  return null;
};

// Configuration BaseURL avec fallbacks selon la plateforme
const getBaseURL = (): string => {
  const envUrl = process.env.EXPO_PUBLIC_API_URL;
  const isPhysical = isPhysicalDevice();
  const lanIP = getLanIPFromExpo();
  
  // Priorité absolue : EXPO_PUBLIC_API_URL si défini
  if (envUrl) {
    // Vérifier si l'URL contient 127.0.0.1 ou localhost sur un device physique
    const isLocalhost = envUrl.includes('127.0.0.1') || envUrl.includes('localhost');
    
    if (isPhysical && isLocalhost) {
      // Sur device physique avec localhost → essayer de remplacer par IP LAN
      if (lanIP) {
        const correctedUrl = envUrl.replace(/127\.0\.0\.1|localhost/, lanIP);
        console.warn(
          `⚠️ EXPO_PUBLIC_API_URL contient localhost sur device physique.\n` +
          `Correction automatique: ${envUrl} → ${correctedUrl}\n` +
          `Si cela ne fonctionne pas, définissez EXPO_PUBLIC_API_URL avec votre IP LAN (ex: http://192.168.0.150:8000)`
        );
        return correctedUrl;
      } else {
        console.error(
          `❌ ACTION REQUIRED: EXPO_PUBLIC_API_URL=${envUrl} contient localhost mais vous êtes sur un device physique.\n` +
          `L'API ne sera pas accessible. Définissez EXPO_PUBLIC_API_URL avec votre IP LAN:\n` +
          `  EXPO_PUBLIC_API_URL=http://192.168.0.150:8000\n` +
          `(Remplacez 192.168.0.150 par l'IP de votre Mac sur le réseau local)`
        );
      }
    }
    
    return envUrl;
  }
  
  // Fallback pour simulateurs/web uniquement
  if (Platform.OS === 'web') {
    return 'http://localhost:8000';
  }
  
  // Sur device physique sans EXPO_PUBLIC_API_URL, essayer IP LAN détectée
  if (isPhysical && lanIP) {
    const fallbackUrl = `http://${lanIP}:8000`;
    console.warn(
      `⚠️ EXPO_PUBLIC_API_URL non défini sur device physique.\n` +
      `Utilisation de l'IP LAN détectée: ${fallbackUrl}\n` +
      `Si cela ne fonctionne pas, définissez EXPO_PUBLIC_API_URL explicitement.`
    );
    return fallbackUrl;
  }
  
  if (Platform.OS === 'ios') {
    // iOS Simulator : localhost fonctionne
    // Device physique : nécessite EXPO_PUBLIC_API_URL avec IP locale
    if (isPhysical) {
      console.error(
        `❌ ACTION REQUIRED: EXPO_PUBLIC_API_URL non défini sur device physique iOS.\n` +
        `Définissez EXPO_PUBLIC_API_URL avec votre IP LAN:\n` +
        `  EXPO_PUBLIC_API_URL=http://192.168.0.150:8000\n` +
        `(Remplacez 192.168.0.150 par l'IP de votre Mac sur le réseau local)`
      );
    }
    return 'http://127.0.0.1:8000';
  }
  
  if (Platform.OS === 'android') {
    // Android Emulator : 10.0.2.2 fonctionne
    // Device physique : nécessite EXPO_PUBLIC_API_URL avec IP locale
    if (isPhysical) {
      console.error(
        `❌ ACTION REQUIRED: EXPO_PUBLIC_API_URL non défini sur device physique Android.\n` +
        `Définissez EXPO_PUBLIC_API_URL avec votre IP LAN:\n` +
        `  EXPO_PUBLIC_API_URL=http://192.168.0.150:8000\n` +
        `(Remplacez 192.168.0.150 par l'IP de votre Mac sur le réseau local)`
      );
    }
    return 'http://10.0.2.2:8000';
  }
  
  // Fallback par défaut
  return 'http://localhost:8000';
};

const API_URL = getBaseURL();

// Log de la baseURL choisie au démarrage (utile pour debug réseau)
console.log(`🔗 API BaseURL: ${API_URL}`);
console.log(`📱 Platform: ${Platform.OS}, Device: ${Constants.deviceName || 'unknown'}, IsPhysical: ${isPhysicalDevice()}`);

const apiClient = axios.create({
  baseURL: API_URL,
  timeout: 30000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Mode DEV_AUTH_BYPASS: détection et configuration
const DEV_AUTH_BYPASS = process.env.EXPO_PUBLIC_DEV_AUTH_BYPASS === 'true';
// EXPO_PUBLIC_DEV_USER_ID doit être un UUID string (ex: "550e8400-e29b-41d4-a716-446655440000")
// Si non défini, on utilise un UUID par défaut pour les tests
const DEV_USER_ID_RAW = process.env.EXPO_PUBLIC_DEV_USER_ID || '550e8400-e29b-41d4-a716-446655440000';

// Validation UUID en dev (guard)
const UUID_REGEX = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i;
const isValidUUID = (str: string): boolean => {
  return UUID_REGEX.test(str);
};

const DEV_USER_ID = (() => {
  if (DEV_AUTH_BYPASS && !isValidUUID(DEV_USER_ID_RAW)) {
    console.error(
      `\n❌ ACTION REQUIRED: EXPO_PUBLIC_DEV_USER_ID n'est pas un UUID valide: "${DEV_USER_ID_RAW}"\n` +
      `Format attendu: "550e8400-e29b-41d4-a716-446655440000"\n` +
      `\nCorrigez votre fichier .env:\n` +
      `  EXPO_PUBLIC_DEV_USER_ID=550e8400-e29b-41d4-a716-446655440000\n` +
      `\nUtilisation d'un UUID par défaut pour éviter les erreurs (cette session uniquement).\n`
    );
    return '550e8400-e29b-41d4-a716-446655440000';
  }
  return DEV_USER_ID_RAW;
})();

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

// Intercepteur de réponse pour logger les erreurs
apiClient.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => {
    // Extraire les informations d'erreur
    const isAxiosError = error.isAxiosError || false;
    const errorCode = error.code || null;
    const errorMessage = error.message || '';
    const status = error.response?.status || null;
    const fullUrl = error.config ? `${error.config.baseURL || API_URL}${error.config.url || ''}` : 'unknown';
    
    // Diagnostic amélioré pour Network Error
    if (errorCode === 'ERR_NETWORK' || errorMessage === 'Network Error') {
      const isPhysical = isPhysicalDevice();
      const baseUrl = error.config?.baseURL || API_URL;
      const hostFromUrl = baseUrl.replace(/^https?:\/\//, '').split(':')[0];
      
      console.error(
        `\n❌ ERREUR RÉSEAU: Impossible de joindre l'API\n` +
        `URL tentée: ${fullUrl}\n` +
        `BaseURL: ${baseUrl}\n` +
        `Platform: ${Platform.OS}, Device: ${Constants.deviceName || 'unknown'}, IsPhysical: ${isPhysical}\n` +
        `\nCauses probables:\n` +
        `1. L'API n'est pas démarrée ou n'écoute pas sur ${baseUrl}\n` +
        `2. ${isPhysical ? `Sur device physique, l'API doit écouter sur 0.0.0.0 (pas seulement 127.0.0.1)` : 'Firewall bloque la connexion'}\n` +
        `3. L'API doit être démarrée avec: uvicorn main:app --reload --host 0.0.0.0 --port 8000\n` +
        `   OU utiliser: cd apps/api && ./start_api.sh\n` +
        `\nVérifiez:\n` +
        `- API démarrée avec --host 0.0.0.0: cd apps/api && uvicorn main:app --reload --host 0.0.0.0 --port 8000\n` +
        `- Test depuis Mac sur IP LAN: curl http://${hostFromUrl}:8000/health\n` +
        `- Test depuis Mac sur localhost: curl http://127.0.0.1:8000/health\n` +
        `- EXPO_PUBLIC_API_URL dans .env: ${process.env.EXPO_PUBLIC_API_URL || 'NON DÉFINI'}\n` +
        `- Si localhost fonctionne mais pas IP LAN → API n'écoute pas sur 0.0.0.0\n`
      );
    }
    
    return Promise.reject(error);
  }
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
   * @param userId ID de l'utilisateur (UUID string)
   * @param month Mois au format YYYY-MM (ex: "2025-01")
   * @param token Token d'authentification (optionnel, sera ajouté automatiquement par l'intercepteur)
   */
  getOverview: async (userId: string, month: string, token?: string) => {
    // Le token est géré automatiquement par l'intercepteur axios
    // On peut le passer explicitement si nécessaire, sinon l'intercepteur le récupère d'AsyncStorage
    try {
      const response = await apiClient.get(`/api/transits/overview/${userId}/${month}`);
      return response.data;
    } catch (error: any) {
      // 404 = pas de transits disponibles (cas normal, pas une erreur)
      if (error.response?.status === 404) {
        return null;
      }
      throw error;
    }
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

