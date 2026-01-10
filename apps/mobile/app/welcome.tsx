/**
 * Écran de bienvenue - Affiché une seule fois au premier lancement
 */

import React from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { useRouter } from 'expo-router';
import { useOnboardingStore } from '../stores/useOnboardingStore';
import { colors, fonts, spacing, borderRadius } from '../constants/theme';
import { goToNextOnboardingStep } from '../services/onboardingFlow';
import { getOnboardingFlowState } from '../utils/onboardingHelpers';

export default function WelcomeScreen() {
  const router = useRouter();
  const onboardingStore = useOnboardingStore();
  const { setWelcomeSeen } = onboardingStore;

  React.useEffect(() => {
    console.log('[WELCOME] ✅ Composant Welcome monté et affiché à l\'écran');
  }, []);

  const handleContinue = async () => {
    console.log('[WELCOME] Bouton "Continuer" cliqué');

    // Marquer le welcome comme vu via le store
    await setWelcomeSeen();
    console.log('[WELCOME] hasSeenWelcomeScreen défini à true via useOnboardingStore');

    // Utiliser le helper centralisé pour naviguer (lit l'état frais depuis Zustand)
    // Pass getOnboardingFlowState to avoid require cycle
    await goToNextOnboardingStep(router, 'WELCOME', getOnboardingFlowState);
  };

  return (
    <LinearGradient colors={colors.darkBg} style={styles.container}>
      <View style={styles.content}>
        {/* Emoji */}
        <View style={styles.emojiContainer}>
          <Text style={styles.emoji}>🌙</Text>
        </View>

        {/* Message simple */}
        <Text style={styles.message}>
          Lunation est un rituel lunaire quotidien.{'\n\n'}
          Chaque jour, découvre la phase de la lune et prends un moment pour écrire, si tu le souhaites.
        </Text>

        {/* Bouton Commencer */}
        <TouchableOpacity
          style={styles.button}
          onPress={handleContinue}
          activeOpacity={0.8}
        >
          <Text style={styles.buttonText}>Commencer</Text>
        </TouchableOpacity>
      </View>
    </LinearGradient>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  content: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    paddingHorizontal: spacing.xl,
    paddingTop: 60,
    paddingBottom: spacing.xl,
  },
  emojiContainer: {
    width: 120,
    height: 120,
    borderRadius: 60,
    backgroundColor: 'rgba(183, 148, 246, 0.15)',
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: spacing.xl,
    shadowColor: colors.accent,
    shadowOffset: { width: 0, height: 8 },
    shadowOpacity: 0.3,
    shadowRadius: 16,
    elevation: 8,
  },
  emoji: {
    fontSize: 64,
  },
  message: {
    ...fonts.body,
    color: colors.text,
    textAlign: 'center',
    lineHeight: 26,
    marginBottom: spacing.xxl,
    paddingHorizontal: spacing.md,
    fontSize: fonts.sizes.md,
  },
  button: {
    backgroundColor: colors.accent,
    paddingVertical: spacing.md,
    paddingHorizontal: spacing.xl * 2,
    borderRadius: borderRadius.md,
    alignItems: 'center',
    shadowColor: colors.accent,
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.3,
    shadowRadius: 8,
    elevation: 4,
  },
  buttonText: {
    ...fonts.button,
    color: colors.text,
    fontSize: fonts.sizes.lg,
  },
});
