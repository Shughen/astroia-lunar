/**
 * Onboarding - Consentement RGPD
 */

import React, { useState } from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  ScrollView,
  Alert,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { SafeAreaView } from 'react-native-safe-area-context';
import { useRouter } from 'expo-router';
import { useOnboardingStore } from '../../stores/useOnboardingStore';
import { colors, fonts, spacing, borderRadius } from '../../constants/theme';

export default function ConsentScreen() {
  const router = useRouter();
  const { setConsentAccepted } = useOnboardingStore();
  const [accepted, setAccepted] = useState(false);

  const handleNext = async () => {
    if (!accepted) {
      Alert.alert(
        'Consentement requis',
        'Pour continuer, veuillez accepter notre politique de confidentialité.'
      );
      return;
    }

    await setConsentAccepted();
    console.log('[CONSENT] Accepté → /onboarding/disclaimer');
    router.push('/onboarding/disclaimer');
  };

  return (
    <LinearGradient colors={colors.darkBg} style={styles.container}>
      <SafeAreaView style={styles.safeArea} edges={['top', 'bottom']}>
        <View style={styles.header}>
          <TouchableOpacity onPress={() => router.back()} style={styles.backButton}>
            <Text style={styles.backText}>←</Text>
          </TouchableOpacity>
          <Text style={styles.headerTitle}>Étape 2/4</Text>
          <View style={{ width: 40 }} />
        </View>

        <ScrollView
          contentContainerStyle={styles.scrollContent}
          showsVerticalScrollIndicator={false}
        >
          <Text style={styles.title}>Données personnelles</Text>
          <Text style={styles.subtitle}>
            Astroia Lunar respecte ta vie privée
          </Text>

          <View style={styles.content}>
            <Text style={styles.paragraph}>
              Tes données astrologiques (date de naissance, lieu, etc.) sont
              utilisées uniquement pour calculer ton thème natal et tes
              révolutions lunaires.
            </Text>
            <Text style={styles.paragraph}>
              Nous ne vendons jamais tes données à des tiers. Tu peux supprimer
              ton compte à tout moment depuis les paramètres.
            </Text>
            <Text style={styles.paragraph}>
              En continuant, tu acceptes notre politique de confidentialité
              (RGPD).
            </Text>
          </View>

          <TouchableOpacity
            style={styles.checkbox}
            onPress={() => setAccepted(!accepted)}
            activeOpacity={0.7}
          >
            <View style={[styles.checkboxBox, accepted && styles.checkboxBoxChecked]}>
              {accepted && <Text style={styles.checkboxCheck}>✓</Text>}
            </View>
            <Text style={styles.checkboxLabel}>
              J'accepte la politique de confidentialité
            </Text>
          </TouchableOpacity>
        </ScrollView>

        <View style={styles.footer}>
          <TouchableOpacity
            style={[styles.nextButton, !accepted && styles.nextButtonDisabled]}
            onPress={handleNext}
            activeOpacity={0.8}
            disabled={!accepted}
          >
            <LinearGradient
              colors={
                accepted
                  ? [colors.accent, colors.accentDark || colors.accent]
                  : ['rgba(100,100,100,0.5)', 'rgba(100,100,100,0.5)']
              }
              style={styles.nextButtonGradient}
            >
              <Text style={styles.nextButtonText}>Suivant</Text>
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
    color: 'rgba(255, 255, 255, 0.7)',
    marginBottom: spacing.xxl,
  },
  content: { gap: spacing.lg },
  paragraph: {
    fontSize: fonts.sizes.md,
    color: 'rgba(255, 255, 255, 0.85)',
    lineHeight: 24,
  },
  checkbox: {
    flexDirection: 'row',
    alignItems: 'center',
    marginTop: spacing.xl,
    gap: spacing.md,
  },
  checkboxBox: {
    width: 24,
    height: 24,
    borderRadius: 4,
    borderWidth: 2,
    borderColor: colors.accent,
    justifyContent: 'center',
    alignItems: 'center',
  },
  checkboxBoxChecked: {
    backgroundColor: colors.accent,
  },
  checkboxCheck: {
    color: colors.text,
    fontSize: 16,
    fontWeight: 'bold',
  },
  checkboxLabel: {
    flex: 1,
    fontSize: fonts.sizes.md,
    color: colors.text,
  },
  footer: {
    paddingHorizontal: spacing.xl,
    paddingBottom: spacing.lg,
  },
  nextButton: {
    borderRadius: borderRadius.lg,
    overflow: 'hidden',
  },
  nextButtonDisabled: {
    opacity: 0.5,
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
