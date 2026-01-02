/**
 * Écran d'accueil principal
 */

import React, { useEffect, useLayoutEffect, useState, useRef, useCallback } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  ActivityIndicator,
  Alert,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import NetInfo from '@react-native-community/netinfo';

// Fallback si LinearGradient n'est pas disponible
const LinearGradientComponent = LinearGradient || (({ colors, style, children, ...props }: any) => {
  // View est déjà importé depuis react-native plus haut
  return <View style={[{ backgroundColor: colors?.[0] || '#1a0b2e' }, style]} {...props}>{children}</View>;
});
import { useRouter, useFocusEffect } from 'expo-router';
import { useTranslation } from 'react-i18next';
import { useAuthStore } from '../stores/useAuthStore';
import { useOnboardingStore } from '../stores/useOnboardingStore';
import { useNotificationsStore } from '../stores/useNotificationsStore';
import { useResetStore } from '../stores/useResetStore';
import { lunarReturns, LunarReturn, isDevAuthBypassActive, getDevAuthHeader } from '../services/api';
import { colors, fonts, spacing, borderRadius } from '../constants/theme';
import { DailyRitualCard } from '../components/DailyRitualCard';
import { setupNotificationTapListener, shouldReschedule } from '../services/notificationScheduler';
import { cleanupGhostFlags } from '../services/onboardingMigration';

export default function HomeScreen() {
  const { t } = useTranslation();
  const router = useRouter();
  const { isAuthenticated } = useAuthStore();
  const onboardingStore = useOnboardingStore();
  const { notificationsEnabled, hydrated, loadPreferences, scheduleAllNotifications } = useNotificationsStore();
  const { isResetting } = useResetStore();
  const [currentLunarReturn, setCurrentLunarReturn] = useState<LunarReturn | null>(null);
  const [isCheckingRouting, setIsCheckingRouting] = useState(true);
  const [isOnline, setIsOnline] = useState(true);
  const routingInFlightRef = useRef(false);

  // Guards de routing : vérifier auth, onboarding et profil complet
  useEffect(() => {
    const checkRouting = async () => {
      // Guard absolu: ne pas router si reset en cours
      if (isResetting) {
        console.log('[INDEX] ⏸️ Reset en cours, skip routing');
        return;
      }

      // Guard absolu: éviter double-run pendant un routing en cours
      if (routingInFlightRef.current) {
        console.log('[INDEX] ⏸️ Routing déjà en cours, skip double-run');
        return;
      }

      // Marquer routing en cours
      routingInFlightRef.current = true;

      try {
        // Migration one-shot: nettoyer flags fantômes AVANT hydratation
        if (!onboardingStore.hydrated) {
          await cleanupGhostFlags();
        }

        // Guard absolu: hydratation BLOQUANTE
        if (!onboardingStore.hydrated) {
          console.log('[INDEX] ⏳ Hydratation en cours...');
          await onboardingStore.hydrate();
          console.log('[INDEX] ✅ Hydratation terminée');
        }

        console.log('[INDEX] 📍 Début checkRouting');
        console.log('[INDEX] 📊 État onboarding:', {
          hasSeenWelcomeScreen: onboardingStore.hasSeenWelcomeScreen,
          hasAcceptedConsent: onboardingStore.hasAcceptedConsent,
          hasCompletedProfile: onboardingStore.hasCompletedProfile,
          hasSeenDisclaimer: onboardingStore.hasSeenDisclaimer,
          hasCompletedOnboarding: onboardingStore.hasCompletedOnboarding,
        });

        // En mode DEV_AUTH_BYPASS, log clair et skip uniquement auth
        const isBypassActive = isDevAuthBypassActive();
        if (isBypassActive) {
          console.log('[INDEX] ⚠️ DEV_AUTH_BYPASS actif');
        }

        // A) Vérifier auth (sauf si DEV_AUTH_BYPASS actif)
        if (!isBypassActive && !isAuthenticated) {
          console.log('[INDEX] → Redirection /login (pas authentifié)');
          router.replace('/login');
          // NE PAS setIsCheckingRouting(false) : garder loader actif pendant redirect
          return;
        }

        // B) Vérifier hasSeenWelcomeScreen
        if (!onboardingStore.hasSeenWelcomeScreen) {
          console.log('[INDEX] → Redirection /welcome');
          router.replace('/welcome');
          return;
        }

        // C) Vérifier consentement RGPD
        if (!onboardingStore.hasAcceptedConsent) {
          console.log('[INDEX] → Redirection /onboarding/consent');
          router.replace('/onboarding/consent');
          return;
        }

        // D) Vérifier profil setup
        if (!onboardingStore.hasCompletedProfile) {
          console.log('[INDEX] → Redirection /onboarding/profile-setup');
          router.replace('/onboarding/profile-setup');
          return;
        }

        // E) Vérifier disclaimer médical
        if (!onboardingStore.hasSeenDisclaimer) {
          console.log('[INDEX] → Redirection /onboarding/disclaimer');
          router.replace('/onboarding/disclaimer');
          return;
        }

        // F) Vérifier onboarding complet (slides)
        if (!onboardingStore.hasCompletedOnboarding) {
          console.log('[INDEX] → Redirection /onboarding');
          router.replace('/onboarding');
          return;
        }

        // Tout est OK → Home
        console.log('[INDEX] ✅ Tous les guards passés → Home');
        setIsCheckingRouting(false);
      } catch (error) {
        console.error('[INDEX] ❌ Erreur dans checkRouting:', error);
        router.replace('/login');
        // NE PAS setIsCheckingRouting(false) : garder loader actif
      } finally {
        // Relâcher le flag in-flight (permet re-run si deps changent)
        routingInFlightRef.current = false;
      }
    };

    checkRouting();
  }, [isAuthenticated, isResetting, onboardingStore.hydrated, router]);

  // Hydratation store notifications au mount
  useEffect(() => {
    if (!hydrated) {
      loadPreferences();
    }
  }, [hydrated, loadPreferences]);

  // Détecter l'état du réseau
  useEffect(() => {
    const unsubscribe = NetInfo.addEventListener(state => {
      setIsOnline(state.isConnected ?? true);
      console.log('[INDEX] 📡 Network state:', state.isConnected ? 'Online' : 'Offline');
    });

    return () => unsubscribe();
  }, []);

  // Setup listener tap notifications au mount
  useEffect(() => {
    const subscription = setupNotificationTapListener((screen: string) => {
      console.log(`[INDEX] Tap notification → ${screen}`);
      router.push(screen as any);
    });

    return () => subscription.remove();
  }, [router]);

  // Charger le cycle lunaire actuel au mount
  useEffect(() => {
    if ((isAuthenticated || isDevAuthBypassActive()) && !isCheckingRouting) {
      loadCurrentLunarReturn();
    }
  }, [isAuthenticated, isCheckingRouting]);

  // Re-scheduler notifications au focus si nécessaire
  useFocusEffect(
    useCallback(() => {
      if ((isAuthenticated || isDevAuthBypassActive()) && !isCheckingRouting) {
        // Re-scheduler notifications si nécessaire (max 1x/24h)
        if (notificationsEnabled && hydrated) {
          (async () => {
            const should = await shouldReschedule();
            if (should) {
              console.log('[INDEX] Re-scheduling notifications (>24h depuis dernier)');
              await scheduleAllNotifications();
            }
          })();
        }
      }
    }, [isAuthenticated, isCheckingRouting, notificationsEnabled, hydrated, scheduleAllNotifications])
  );

  const loadCurrentLunarReturn = async () => {
    try {
      const current = await lunarReturns.getCurrent();
      setCurrentLunarReturn(current);
    } catch (error: any) {
      // Silencieux si 404 (pas de retour pour le mois en cours)
      if (error.response?.status !== 404) {
        console.error('[INDEX] Erreur chargement cycle lunaire:', error);
      }
    }
  };

  // Afficher un loader pendant la vérification du routing
  if (isCheckingRouting && !isDevAuthBypassActive()) {
    return (
      <LinearGradientComponent colors={colors.darkBg} style={styles.container}>
        <View style={styles.center}>
          <ActivityIndicator size="large" color={colors.accent} />
          <Text style={styles.subtitle}>Chargement...</Text>
        </View>
      </LinearGradientComponent>
    );
  }

  // En mode DEV_AUTH_BYPASS, afficher directement le contenu principal
  // Sinon, si pas authentifié, les guards redirigeront vers /login
  if (!isAuthenticated && !isDevAuthBypassActive()) {
    return (
      <LinearGradientComponent colors={colors.darkBg} style={styles.container}>
        <View style={styles.center}>
          <ActivityIndicator size="large" color={colors.accent} />
          <Text style={styles.subtitle}>Redirection...</Text>
        </View>
      </LinearGradientComponent>
    );
  }

  return (
    <LinearGradientComponent colors={colors.darkBg} style={styles.container}>
      <ScrollView contentContainerStyle={styles.scrollContent}>
        {/* Header */}
        <View style={styles.header}>
          <Text style={styles.title}>🌙 Rituel Lunaire</Text>
        </View>

        {/* Carte Mode Hors Connexion (calme, non anxiogène) */}
        {!isOnline && (
          <View style={styles.offlineCard}>
            <Text style={styles.offlineEmoji}>🌙</Text>
            <Text style={styles.offlineTitle}>Mode hors ligne</Text>
            <Text style={styles.offlineText}>
              Ton rituel quotidien et ton journal restent accessibles. Les données viennent du cache local.
            </Text>
          </View>
        )}

        {/* Carte Rituel Quotidien (HERO) */}
        <DailyRitualCard />

        {/* Menu principal MVP : Journal + Réglages uniquement */}
        <View style={styles.grid}>
          <TouchableOpacity
            style={styles.menuCard}
            onPress={() => router.push('/journal')}
          >
            <Text style={styles.menuEmoji}>📖</Text>
            <Text style={styles.menuTitle}>Journal</Text>
            <Text style={styles.menuDesc}>Mes entrées récentes</Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={styles.menuCard}
            onPress={() => router.push('/settings')}
          >
            <Text style={styles.menuEmoji}>⚙️</Text>
            <Text style={styles.menuTitle}>Réglages</Text>
            <Text style={styles.menuDesc}>Infos et paramètres</Text>
          </TouchableOpacity>
        </View>
      </ScrollView>
    </LinearGradientComponent>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  scrollContent: {
    paddingTop: 60,
    paddingHorizontal: spacing.lg,
    paddingBottom: spacing.xl,
  },
  center: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    paddingHorizontal: spacing.xl,
  },
  header: {
    marginBottom: spacing.xl,
    alignItems: 'center',
  },
  emoji: {
    fontSize: 64,
    marginBottom: spacing.md,
  },
  title: {
    ...fonts.h1,
    color: colors.text,
    textAlign: 'center',
    marginBottom: spacing.sm,
  },
  subtitle: {
    ...fonts.body,
    color: colors.textMuted,
    textAlign: 'center',
  },
  button: {
    backgroundColor: colors.accent,
    paddingVertical: spacing.md,
    paddingHorizontal: spacing.xl,
    borderRadius: borderRadius.md,
    marginTop: spacing.xl,
  },
  buttonText: {
    ...fonts.button,
    color: colors.text,
  },
  linkButton: {
    marginTop: spacing.md,
  },
  linkText: {
    ...fonts.body,
    color: colors.accent,
    textDecorationLine: 'underline',
  },
  grid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'space-between',
  },
  menuCard: {
    width: '48%',
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.md,
    padding: spacing.lg,
    marginBottom: spacing.md,
    alignItems: 'center',
  },
  menuEmoji: {
    fontSize: 48,
    marginBottom: spacing.sm,
  },
  menuTitle: {
    ...fonts.h3,
    color: colors.text,
    marginBottom: spacing.xs,
    textAlign: 'center',
  },
  menuDesc: {
    ...fonts.bodySmall,
    color: colors.textMuted,
    textAlign: 'center',
  },
  cycleSummary: {
    backgroundColor: 'rgba(183, 148, 246, 0.05)',
    borderRadius: borderRadius.md,
    padding: spacing.md,
    marginBottom: spacing.lg,
    borderWidth: 1,
    borderColor: 'rgba(183, 148, 246, 0.15)',
  },
  cycleSummaryTitle: {
    ...fonts.body,
    color: colors.text,
    marginBottom: spacing.xs,
  },
  cycleSummaryDetails: {
    ...fonts.bodySmall,
    color: colors.textMuted,
    marginBottom: spacing.sm,
  },
  cycleSummaryLink: {
    paddingVertical: spacing.xs,
  },
  cycleSummaryLinkText: {
    ...fonts.body,
    color: colors.accent,
    fontSize: 14,
  },
  offlineCard: {
    backgroundColor: 'rgba(183, 148, 246, 0.08)',
    borderRadius: borderRadius.md,
    padding: spacing.md,
    marginBottom: spacing.md,
    borderWidth: 1,
    borderColor: 'rgba(183, 148, 246, 0.2)',
  },
  offlineEmoji: {
    fontSize: 24,
    marginBottom: spacing.xs,
  },
  offlineTitle: {
    ...fonts.body,
    color: colors.text,
    marginBottom: spacing.xs,
    fontWeight: '500',
  },
  offlineText: {
    ...fonts.bodySmall,
    color: colors.textMuted,
    lineHeight: 18,
  },
  menuCardDisabled: {
    opacity: 0.5,
  },
  offlineBadge: {
    ...fonts.bodySmall,
    color: colors.accent,
    marginTop: spacing.xs,
    fontSize: 10,
  },
});

