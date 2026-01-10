/**
 * Helpers de détection device/platform
 */

import { Platform } from 'react-native';
import Constants from 'expo-constants';

/**
 * Détecte si on est sur un device physique ou simulateur
 */
export function isPhysicalDevice(): boolean {
  const deviceName = Constants.deviceName;
  if (deviceName) {
    const isSimulator =
      deviceName.toLowerCase().includes('simulator') ||
      deviceName.toLowerCase().includes('emulator');
    return !isSimulator;
  }
  // Si deviceName n'est pas disponible, on assume device physique si pas web
  return Platform.OS !== 'web';
}

/**
 * Récupère l'IP LAN depuis Expo debugger (si disponible)
 */
export function getLanIPFromExpo(): string | null {
  try {
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
}

/**
 * Configuration BaseURL avec fallbacks selon la plateforme
 */
export function getBaseURL(defaultUrl: string): string {
  const envUrl = process.env.EXPO_PUBLIC_API_URL;
  const isPhysical = isPhysicalDevice();
  const lanIP = getLanIPFromExpo();

  // Priorité absolue : EXPO_PUBLIC_API_URL si défini
  if (envUrl) {
    // Vérifier si l'URL contient 127.0.0.1 ou localhost sur un device physique
    const isLocalhost =
      envUrl.includes('127.0.0.1') || envUrl.includes('localhost');

    if (isPhysical && isLocalhost && lanIP) {
      // Remplacer localhost par LAN IP pour device physique
      const urlWithLanIP = envUrl.replace(
        /127\.0\.0\.1|localhost/,
        lanIP
      );
      console.log(`[Device] Remplacement localhost par LAN IP: ${urlWithLanIP}`);
      return urlWithLanIP;
    }

    return envUrl;
  }

  // Fallback : URL par défaut
  return defaultUrl;
}
