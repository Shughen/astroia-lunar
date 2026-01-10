/**
 * Utilitaires pour DEV_AUTH_BYPASS
 * Validation et normalisation du DEV_USER_ID
 * Supporte: integer ID, UUID, ou email
 */

let hasWarnedInvalidId = false;

/**
 * Reset le flag de warning (pour les tests uniquement)
 */
export function resetWarningFlag() {
  hasWarnedInvalidId = false;
}

/**
 * Type de header DEV_AUTH_BYPASS déterminé
 */
export type DevAuthHeaderType =
  | { type: 'int'; header: 'X-Dev-User-Id'; value: string }
  | { type: 'uuid'; header: 'X-Dev-External-Id'; value: string }
  | { type: 'email'; header: 'X-Dev-External-Id'; value: string }
  | { type: 'invalid'; header: null; value: null };

/**
 * Valide et détermine le type de header DEV_AUTH_BYPASS à utiliser
 *
 * Règles:
 * - Si entier positif => X-Dev-User-Id (int)
 * - Si UUID valide => X-Dev-External-Id (uuid)
 * - Si email => X-Dev-External-Id (email)
 * - Sinon => invalid
 *
 * @param envValue Valeur depuis process.env.EXPO_PUBLIC_DEV_USER_ID
 * @returns DevAuthHeaderType avec type, header et value
 */
export function getDevAuthHeaderType(envValue: string | undefined): DevAuthHeaderType {
  // Si undefined ou empty
  if (!envValue || envValue.trim() === '') {
    return { type: 'invalid', header: null, value: null };
  }

  const trimmed = envValue.trim();

  // Tentative 1: Vérifier si c'est un entier valide
  const integerMatch = trimmed.match(/^-?\d+$/);
  if (integerMatch) {
    const parsed = parseInt(trimmed, 10);

    if (Number.isFinite(parsed) && parsed > 0) {
      // Retourner la string normalisée (sans zéros de tête)
      return {
        type: 'int',
        header: 'X-Dev-User-Id',
        value: String(parsed)
      };
    }
  }

  // Tentative 2: Vérifier si c'est un UUID valide (format standard 8-4-4-4-12)
  const uuidMatch = trimmed.match(/^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i);
  if (uuidMatch) {
    return {
      type: 'uuid',
      header: 'X-Dev-External-Id',
      value: trimmed.toLowerCase()
    };
  }

  // Tentative 3: Vérifier si c'est un email (simple validation)
  const emailMatch = trimmed.match(/^[^\s@]+@[^\s@]+\.[^\s@]+$/);
  if (emailMatch) {
    return {
      type: 'email',
      header: 'X-Dev-External-Id',
      value: trimmed
    };
  }

  // Valeur invalide: log WARN une seule fois
  if (!hasWarnedInvalidId) {
    console.warn(
      `[DEV_AUTH_BYPASS] ⚠️ EXPO_PUBLIC_DEV_USER_ID invalide: "${envValue}"\n` +
      `Formats acceptés:\n` +
      `  - Entier positif (ex: "1") -> X-Dev-User-Id\n` +
      `  - UUID (ex: "550e8400-e29b-41d4-a716-446655440000") -> X-Dev-External-Id\n` +
      `  - Email (ex: "dev@local.dev") -> X-Dev-External-Id\n` +
      `Aucun header DEV_AUTH_BYPASS ne sera envoyé (fallback API vers dev@local.dev).`
    );
    hasWarnedInvalidId = true;
  }

  return { type: 'invalid', header: null, value: null };
}

/**
 * DEPRECATED: Utiliser getDevAuthHeaderType() à la place
 * Maintenu pour compatibilité backward
 */
export function getDevUserIdHeaderValue(envValue: string | undefined): string | null {
  const result = getDevAuthHeaderType(envValue);
  if (result.type === 'int') {
    return result.value;
  }
  return null;
}
