/**
 * Helpers pour mode développement
 */

import { FEATURES } from './config';

/**
 * Vérifie si le mode DEV_AUTH_BYPASS est actif
 */
export function isDevAuthBypassActive(): boolean {
  return FEATURES.DEV_AUTH_BYPASS;
}

/**
 * Retourne le user_id de développement
 */
export function getDevUserId(): string {
  return FEATURES.DEV_USER_ID;
}

/**
 * Log en mode dev uniquement
 */
export function devLog(message: string, ...args: unknown[]): void {
  if (FEATURES.DEV_AUTH_BYPASS) {
    console.log(`[DEV] ${message}`, ...args);
  }
}
