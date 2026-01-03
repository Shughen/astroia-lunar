/**
 * Helpers environnement (dev vs prod)
 */

/**
 * Retourne true si l'app est en mode développement
 * Utilise la variable globale __DEV__ fournie par React Native
 */
export function isDev(): boolean {
  return __DEV__;
}

/**
 * Retourne true si l'app est en mode production
 */
export function isProd(): boolean {
  return !__DEV__;
}
