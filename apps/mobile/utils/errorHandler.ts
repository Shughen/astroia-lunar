/**
 * Helper pour gérer les erreurs réseau de manière UX-friendly
 * Remplace les messages techniques (502, timeout) par des messages humains
 *
 * Gestion des erreurs RapidAPI:
 * - RAPIDAPI_NOT_SUBSCRIBED (503): "Fonction indisponible en dev (API non activée)"
 * - RAPIDAPI_RATE_LIMIT (429): "Trop de requêtes, réessaie plus tard"
 */

import { Alert } from 'react-native';
import { AxiosError } from 'axios';

/**
 * Extrait le code d'erreur structuré de la réponse API (si présent)
 */
export function getErrorCode(error: any): string | null {
  return error.response?.data?.detail?.code || error.response?.data?.code || null;
}

/**
 * Formate un message d'erreur humain à partir d'une erreur axios/fetch
 */
export function getHumanErrorMessage(error: any): string {
  // Vérifier si l'erreur contient un code structuré
  const errorCode = getErrorCode(error);

  // Erreur RapidAPI: Not Subscribed (API non activée en dev)
  if (errorCode === 'RAPIDAPI_NOT_SUBSCRIBED') {
    return 'Fonction indisponible en dev (API non activée).';
  }

  // Erreur RapidAPI: Rate Limit
  if (errorCode === 'RAPIDAPI_RATE_LIMIT' || error.response?.status === 429) {
    return 'Trop de requêtes. Réessayez dans quelques instants.';
  }

  // Erreur réseau (backend down, timeout, etc.)
  if (error.code === 'ERR_NETWORK' || error.message === 'Network Error') {
    return 'Le service est temporairement indisponible. Vérifiez votre connexion internet.';
  }

  // Erreur de timeout
  if (error.code === 'ECONNABORTED' || error.message?.includes('timeout')) {
    return 'La requête a pris trop de temps. Veuillez réessayer.';
  }

  // Erreur 502 (Bad Gateway) - provider API down
  if (error.response?.status === 502) {
    return 'Le rapport est temporairement indisponible.';
  }

  // Erreur 500 (Internal Server Error)
  if (error.response?.status === 500) {
    return 'Une erreur serveur est survenue. Veuillez réessayer plus tard.';
  }

  // Erreur 503 (Service Unavailable)
  if (error.response?.status === 503) {
    // Si c'est un 503 mais sans code RAPIDAPI_NOT_SUBSCRIBED, c'est un autre type de 503
    if (errorCode !== 'RAPIDAPI_NOT_SUBSCRIBED') {
      return 'Le service est temporairement indisponible.';
    }
    // Sinon, on a déjà géré le cas RAPIDAPI_NOT_SUBSCRIBED ci-dessus
    return 'Fonction indisponible en dev (API non activée).';
  }

  // Erreur 404 (Not Found) - cas spécifique
  if (error.response?.status === 404) {
    return 'Contenu non trouvé.';
  }

  // Message générique pour autres erreurs
  return 'Une erreur est survenue. Veuillez réessayer.';
}

/**
 * Affiche un Alert avec message humain et bouton "Réessayer"
 * @param error - Erreur axios/fetch
 * @param onRetry - Callback appelé si l'utilisateur appuie sur "Réessayer"
 * @param customMessage - Message personnalisé (optionnel, sinon utilise getHumanErrorMessage)
 */
export function showNetworkErrorAlert(
  error: any,
  onRetry?: () => void,
  customMessage?: string
): void {
  const message = customMessage || getHumanErrorMessage(error);
  const errorCode = getErrorCode(error);

  // Vérifier si c'est une erreur "non-retriable" (not subscribed)
  const isNotSubscribed = errorCode === 'RAPIDAPI_NOT_SUBSCRIBED';

  const buttons: any[] = [
    { text: 'OK', style: 'cancel' },
  ];

  // Ne pas afficher "Réessayer" pour les erreurs not subscribed (inutile)
  if (onRetry && !isNotSubscribed) {
    buttons.unshift({
      text: 'Réessayer',
      onPress: onRetry,
      style: 'default',
    });
  }

  Alert.alert(
    'Erreur',
    message,
    buttons,
    { cancelable: true }
  );
}

/**
 * Vérifie si une erreur est une erreur réseau (502, 500, timeout, etc.)
 */
export function isNetworkError(error: any): boolean {
  const status = error.response?.status;
  return (
    status === 502 ||
    status === 500 ||
    status === 503 ||
    error.code === 'ERR_NETWORK' ||
    error.code === 'ECONNABORTED' ||
    error.message === 'Network Error'
  );
}

