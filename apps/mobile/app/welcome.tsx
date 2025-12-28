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
import AsyncStorage from '@react-native-async-storage/async-storage';
import { colors, fonts, spacing, borderRadius } from '../constants/theme';

export default function WelcomeScreen() {
  const router = useRouter();

  React.useEffect(() => {
    console.log('[WELCOME] ✅ Composant Welcome monté et affiché à l\'écran');
  }, []);

  const handleContinue = async () => {
    console.log('[WELCOME] Bouton "Continuer" cliqué');
    
    // Marquer le welcome comme vu
    await AsyncStorage.setItem('hasSeenWelcomeScreen', 'true');
    console.log('[WELCOME] hasSeenWelcomeScreen défini à "true"');
    
    // Rediriger vers l'index pour que les guards prennent le relais
    console.log('[WELCOME] Redirection vers /');
    router.replace('/');
  };

  return (
    <LinearGradient colors={colors.darkBg} style={styles.container}>
      <View style={styles.content}>
        {/* Emoji */}
        <View style={styles.emojiContainer}>
          <Text style={styles.emoji}>🌙</Text>
        </View>

        {/* Titre */}
        <Text style={styles.title}>Bienvenue sur Astroia Lunar</Text>
        
        {/* Sous-titre */}
        <Text style={styles.subtitle}>
          Découvre tes révolutions lunaires mensuelles et explore ton thème astrologique
        </Text>

        {/* Bouton Continuer */}
        <TouchableOpacity
          style={styles.button}
          onPress={handleContinue}
          activeOpacity={0.8}
        >
          <Text style={styles.buttonText}>Continuer</Text>
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
  title: {
    ...fonts.h1,
    color: colors.text,
    textAlign: 'center',
    marginBottom: spacing.md,
  },
  subtitle: {
    ...fonts.body,
    color: colors.textMuted,
    textAlign: 'center',
    lineHeight: 24,
    marginBottom: spacing.xxl,
    paddingHorizontal: spacing.md,
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
