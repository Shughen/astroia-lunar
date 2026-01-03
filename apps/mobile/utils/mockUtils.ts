/**
 * Utilitaires pour détecter et gérer les réponses mock en mode dev
 */

/**
 * Vérifie si une réponse API est en mode mock (DEV_MOCK_RAPIDAPI)
 * 
 * @param resp Réponse API avec structure { provider, kind, data, ... }
 * @returns true si la réponse est mock (data._mock === true)
 */
export function isMockResponse(resp: any): boolean {
  return !!resp?.data?._mock || !!resp?._mock;
}

/**
 * Retourne le libellé du provider à afficher dans l'UI
 * 
 * @param resp Réponse API
 * @returns "mock (dev)" si mock, sinon le provider original
 */
export function getProviderLabel(resp: any): string {
  if (isMockResponse(resp)) {
    return 'mock (dev)';
  }
  return resp?.provider || 'unknown';
}

/**
 * Nettoie un texte d'interprétation en remplaçant les textes mock par un message propre
 * 
 * @param text Texte d'interprétation original
 * @param isMock Si true, retourne toujours le message propre (peu importe le contenu)
 * @returns Texte nettoyé
 */
export function cleanInterpretationText(text: string | undefined | null, isMock: boolean): string {
  // En mode mock, toujours retourner le message propre
  if (isMock) {
    return 'Données de démonstration (mode dev).';
  }
  
  // Sinon, retourner le texte original (trim) ou chaîne vide
  return text ? text.trim() : '';
}

