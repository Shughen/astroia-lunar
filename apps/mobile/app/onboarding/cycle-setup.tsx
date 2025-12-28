/**
 * Onboarding - Setup cycle menstruel (OPTIONNEL)
 * L'utilisateur peut skip cette étape
 */

import React from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  ScrollView,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { SafeAreaView } from 'react-native-safe-area-context';
import { useRouter } from 'expo-router';
import { colors, fonts, spacing, borderRadius } from '../../constants/theme';

export default function CycleSetupScreen() {
  const router = useRouter();

  const handleSkip = () => {
    console.log('[CYCLE-SETUP] Skip → /onboarding (slides)');
    router.push('/onboarding');
  };

  const handleConfigure = () => {
    console.log('[CYCLE-SETUP] Configure → /cycle (page cycle complète)');
    // Pour l'instant, on skip aussi, la config se fera dans l'app principale
    handleSkip();
  };

  return (
    <LinearGradient colors={colors.darkBg} style={styles.container}>
      <SafeAreaView style={styles.safeArea} edges={['top', 'bottom']}>
        <View style={styles.header}>
          <TouchableOpacity onPress={() => router.back()} style={styles.backButton}>
            <Text style={styles.backText}>←</Text>
          </TouchableOpacity>
          <Text style={styles.headerTitle}>Étape 4/4</Text>
          <View style={{ width: 40 }} />
        </View>

        <ScrollView
          contentContainerStyle={styles.scrollContent}
          showsVerticalScrollIndicator={false}
        >
          <Text style={styles.title}>Cycles menstruels</Text>
          <Text style={styles.subtitle}>
            Optionnel - Combine astrologie et cycle
          </Text>

          <View style={styles.content}>
            <Text style={styles.emoji}>📅</Text>
            <Text style={styles.paragraph}>
              Astroia Lunar se concentre principalement sur tes{' '}
              <Text style={styles.bold}>révolutions lunaires</Text>.
            </Text>
            <Text style={styles.paragraph}>
              Si tu veux aussi suivre ton cycle menstruel et voir les
              corrélations avec les astres, tu peux le configurer maintenant
              ou plus tard dans les paramètres.
            </Text>
            <Text style={styles.paragraphSmall}>
              Cette fonctionnalité est totalement optionnelle et respecte ta
              vie privée.
            </Text>
          </View>
        </ScrollView>

        <View style={styles.footer}>
          <TouchableOpacity
            style={styles.skipButton}
            onPress={handleSkip}
            activeOpacity={0.8}
          >
            <Text style={styles.skipButtonText}>Passer cette étape</Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={styles.nextButton}
            onPress={handleConfigure}
            activeOpacity={0.8}
          >
            <LinearGradient
              colors={[colors.accent, colors.accentDark || colors.accent]}
              style={styles.nextButtonGradient}
            >
              <Text style={styles.nextButtonText}>Configurer mon cycle</Text>
            </LinearGradient>
          </TouchableOpacity>
        </View>
      </SafeAreaView>
    </LinearGradient>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1 },
  safeArea: { flex: 1 },
  header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingHorizontal: spacing.lg,
    paddingVertical: spacing.md,
  },
  backButton: { width: 40, height: 40, justifyContent: 'center' },
  backText: { fontSize: 24, color: colors.text },
  headerTitle: {
    color: 'rgba(255, 255, 255, 0.7)',
    fontSize: fonts.sizes.md,
    fontWeight: '600',
  },
  scrollContent: {
    flexGrow: 1,
    paddingHorizontal: spacing.xl,
    paddingBottom: spacing.xl,
  },
  title: {
    fontSize: 32,
    fontWeight: 'bold',
    color: colors.text,
    marginBottom: spacing.sm,
    marginTop: spacing.lg,
  },
  subtitle: {
    fontSize: fonts.sizes.md,
    color: colors.accent,
    marginBottom: spacing.xxl,
  },
  content: {
    gap: spacing.lg,
    alignItems: 'center',
  },
  emoji: {
    fontSize: 64,
    marginBottom: spacing.md,
  },
  paragraph: {
    fontSize: fonts.sizes.md,
    color: 'rgba(255, 255, 255, 0.85)',
    lineHeight: 24,
    textAlign: 'center',
  },
  paragraphSmall: {
    fontSize: fonts.sizes.sm,
    color: 'rgba(255, 255, 255, 0.6)',
    lineHeight: 20,
    textAlign: 'center',
    fontStyle: 'italic',
  },
  bold: {
    fontWeight: 'bold',
    color: colors.accent,
  },
  footer: {
    paddingHorizontal: spacing.xl,
    paddingBottom: spacing.lg,
    gap: spacing.md,
  },
  skipButton: {
    paddingVertical: spacing.md,
    alignItems: 'center',
  },
  skipButtonText: {
    color: 'rgba(255, 255, 255, 0.7)',
    fontSize: fonts.sizes.md,
    fontWeight: '600',
  },
  nextButton: {
    borderRadius: borderRadius.lg,
    overflow: 'hidden',
  },
  nextButtonGradient: {
    paddingVertical: spacing.md + 4,
    alignItems: 'center',
  },
  nextButtonText: {
    color: colors.text,
    fontSize: fonts.sizes.lg,
    fontWeight: 'bold',
  },
});
