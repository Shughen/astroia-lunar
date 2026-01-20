/**
 * Service Haptics - Feedback tactile pour l'app
 *
 * Fournit des vibrations subtiles pour améliorer l'expérience utilisateur.
 * Les haptics sont automatiquement désactivés sur les plateformes non supportées.
 *
 * Types de feedback:
 * - light: Tap léger (sélection, navigation)
 * - medium: Action confirmée (validation, envoi)
 * - heavy: Action importante (suppression, erreur)
 * - success: Retour positif
 * - warning: Attention requise
 * - error: Erreur/échec
 */

import { Platform } from 'react-native';
import * as Haptics from 'expo-haptics';

// Vérifier si les haptics sont supportés
const isHapticsSupported = Platform.OS === 'ios' || Platform.OS === 'android';

/**
 * Feedback léger - Pour les taps et sélections
 * Utilisé pour: tap sur une carte, sélection d'une planète, navigation
 */
export async function lightTap(): Promise<void> {
  if (!isHapticsSupported) return;

  try {
    await Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Light);
  } catch (error) {
    // Silently fail - haptics not critical
    console.debug('[Haptics] Light tap failed:', error);
  }
}

/**
 * Feedback medium - Pour les actions confirmées
 * Utilisé pour: validation d'un formulaire, envoi de données
 */
export async function mediumTap(): Promise<void> {
  if (!isHapticsSupported) return;

  try {
    await Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Medium);
  } catch (error) {
    console.debug('[Haptics] Medium tap failed:', error);
  }
}

/**
 * Feedback heavy - Pour les actions importantes
 * Utilisé pour: suppression, action irréversible
 */
export async function heavyTap(): Promise<void> {
  if (!isHapticsSupported) return;

  try {
    await Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Heavy);
  } catch (error) {
    console.debug('[Haptics] Heavy tap failed:', error);
  }
}

/**
 * Feedback de succès - Pour les retours positifs
 * Utilisé pour: thème natal calculé, rapport chargé, entrée journal sauvegardée
 */
export async function successFeedback(): Promise<void> {
  if (!isHapticsSupported) return;

  try {
    await Haptics.notificationAsync(Haptics.NotificationFeedbackType.Success);
  } catch (error) {
    console.debug('[Haptics] Success feedback failed:', error);
  }
}

/**
 * Feedback d'avertissement - Pour attirer l'attention
 * Utilisé pour: VoC qui commence, avertissement
 */
export async function warningFeedback(): Promise<void> {
  if (!isHapticsSupported) return;

  try {
    await Haptics.notificationAsync(Haptics.NotificationFeedbackType.Warning);
  } catch (error) {
    console.debug('[Haptics] Warning feedback failed:', error);
  }
}

/**
 * Feedback d'erreur - Pour les échecs
 * Utilisé pour: erreur de connexion, validation échouée
 */
export async function errorFeedback(): Promise<void> {
  if (!isHapticsSupported) return;

  try {
    await Haptics.notificationAsync(Haptics.NotificationFeedbackType.Error);
  } catch (error) {
    console.debug('[Haptics] Error feedback failed:', error);
  }
}

/**
 * Feedback de sélection - Pour les changements d'état
 * Utilisé pour: toggle, changement de valeur
 */
export async function selectionFeedback(): Promise<void> {
  if (!isHapticsSupported) return;

  try {
    await Haptics.selectionAsync();
  } catch (error) {
    console.debug('[Haptics] Selection feedback failed:', error);
  }
}

// Export groupé pour faciliter l'import
export const haptics = {
  light: lightTap,
  medium: mediumTap,
  heavy: heavyTap,
  success: successFeedback,
  warning: warningFeedback,
  error: errorFeedback,
  selection: selectionFeedback,
};

export default haptics;
