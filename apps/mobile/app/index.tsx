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
import { lunarReturns, LunarReturn, isDevAuthBypassActive, getDevUserId } from '../services/api';
import { colors, fonts, spacing, borderRadius } from '../constants/theme';
import { DailyRitualCard } from '../components/DailyRitualCard';
import { setupNotificationTapListener, shouldReschedule } from '../services/notificationScheduler';

export default function HomeScreen() {
  const { t } = useTranslation();
  const router = useRouter();
  const { isAuthenticated } = useAuthStore();
  const onboardingStore = useOnboardingStore();
  const { notificationsEnabled, hydrated, loadPreferences, scheduleAllNotifications } = useNotificationsStore();
  const [currentLunarReturn, setCurrentLunarReturn] = useState<LunarReturn | null>(null);
  const [isCheckingRouting, setIsCheckingRouting] = useState(true);
  const [shouldNavigate, setShouldNavigate] = useState<{ route: string } | null>(null);
  const hasCheckedRoutingRef = useRef(false);
  const isMountedRef = useRef(false);
  const [isOnline, setIsOnline] = useState(true);

  // S'assurer que le composant est monté avant de naviguer
  useLayoutEffect(() => {
    isMountedRef.current = true;
    return () => {
      isMountedRef.current = false;
    };
  }, []);

  // Effectuer la navigation une fois que le composant est monté
  useEffect(() => {
    if (shouldNavigate && isMountedRef.current) {
      const timer = setTimeout(() => {
        try {
          router.replace(shouldNavigate.route);
        } catch (error) {
          console.error('[INDEX] Erreur navigation:', error);
        }
      }, 50);
      return () => clearTimeout(timer);
    }
  }, [shouldNavigate, router]);

  // Guards de routing : vérifier auth, onboarding et profil complet
  useEffect(() => {
    console.log('[INDEX] 🔄 checkRouting() appelé, hydrated=', onboardingStore.hydrated, 'hasCompletedOnboarding=', onboardingStore.hasCompletedOnboarding);

    const checkRouting = async () => {
      // Guard absolu: si onboarding complété et déjà checké, JAMAIS re-router
      if (hasCheckedRoutingRef.current && onboardingStore.hasCompletedOnboarding) {
        console.log('[INDEX] ⏭️ Onboarding déjà complété et checké, skip re-check');
        return;
      }

      try {
        // Attendre que le composant soit monté
        while (!isMountedRef.current) {
          await new Promise(resolve => setTimeout(resolve, 10));
        }

        console.log('[INDEX] 📍 Début checkRouting');
        console.log('[INDEX] isAuthenticated =', isAuthenticated);

        // Hydrater l'état onboarding depuis AsyncStorage (UNE SEULE FOIS grâce au guard hydrated)
        await onboardingStore.hydrate();

        // Log de tous les flags après hydratation
        console.log('[INDEX] 📊 État onboarding après hydratation:', {
          hasSeenWelcomeScreen: onboardingStore.hasSeenWelcomeScreen,
          hasCompletedProfile: onboardingStore.hasCompletedProfile,
          hasAcceptedConsent: onboardingStore.hasAcceptedConsent,
          hasSeenDisclaimer: onboardingStore.hasSeenDisclaimer,
          hasCompletedOnboarding: onboardingStore.hasCompletedOnboarding,
          hydrated: onboardingStore.hydrated,
        });

        // En mode DEV_AUTH_BYPASS, log clair et skip uniquement auth (pas welcome)
        const isBypassActive = isDevAuthBypassActive();
        console.log('[INDEX] isBypassActive =', isBypassActive);
        if (isBypassActive) {
          console.log('[INDEX] ⚠️ DEV_AUTH_BYPASS: auth guard skipped (welcome actif)');
        }

        // A) Vérifier auth en premier (sauf si DEV_AUTH_BYPASS actif)
        console.log('[INDEX] 📍 Étape A: Vérification auth (bypass=', isBypassActive, ', auth=', isAuthenticated, ')');
        if (!isBypassActive && !isAuthenticated) {
          console.log('[INDEX] ❌ Pas authentifié → redirection vers /login');
          hasCheckedRoutingRef.current = true;
          setIsCheckingRouting(false);
          setShouldNavigate({ route: '/login' });
          return;
        }
        console.log('[INDEX] ✅ Auth OK (bypassé ou authentifié)');

        // ⚠️ GUARD HARD STOP : Si onboarding est complété, NE JAMAIS rediriger vers welcome/onboarding
        if (onboardingStore.hasCompletedOnboarding) {
          console.log('[INDEX] 🛑 GUARD HARD STOP: hasCompletedOnboarding=true → affichage Home (jamais welcome/onboarding)');
          hasCheckedRoutingRef.current = true;
          setIsCheckingRouting(false);
          // Ne pas naviguer, juste afficher le contenu Home
          return;
        }

        // B) Vérifier hasSeenWelcomeScreen (seulement si onboarding pas complété)
        console.log('[INDEX] 📍 Étape B: Vérification hasSeenWelcomeScreen');
        console.log('[INDEX] hasSeenWelcomeScreen =', onboardingStore.hasSeenWelcomeScreen);

        if (!onboardingStore.hasSeenWelcomeScreen) {
          console.log('[INDEX] ✅ Welcome screen non vu → redirection vers /welcome');
          hasCheckedRoutingRef.current = true;
          setIsCheckingRouting(false);
          setShouldNavigate({ route: '/welcome' });
          return;
        }

        console.log('[INDEX] Welcome déjà vu, continuation du flow');

        // En mode DEV_AUTH_BYPASS, continuer le flow onboarding normalement
        // Le bypass ne concerne QUE l'authentification, pas l'onboarding
        if (isBypassActive) {
          console.log('[INDEX] ⚠️ DEV_AUTH_BYPASS: auth skipped, onboarding flow continues');
        }

        // C) Vérifier profil setup (nom + date de naissance)
        console.log('[INDEX] 📍 Étape C: Vérification profil');
        console.log('[INDEX] hasCompletedProfile =', onboardingStore.hasCompletedProfile);
        if (!onboardingStore.hasCompletedProfile) {
          console.log('[INDEX] ✅ Profil incomplet → redirection vers /onboarding/profile-setup');
          hasCheckedRoutingRef.current = true;
          setIsCheckingRouting(false);
          setShouldNavigate({ route: '/onboarding/profile-setup' });
          return;
        }

        // D) Vérifier consentement RGPD
        console.log('[INDEX] 📍 Étape D: Vérification consentement');
        console.log('[INDEX] hasAcceptedConsent =', onboardingStore.hasAcceptedConsent);
        if (!onboardingStore.hasAcceptedConsent) {
          console.log('[INDEX] ✅ Consentement non accepté → redirection vers /onboarding/consent');
          hasCheckedRoutingRef.current = true;
          setIsCheckingRouting(false);
          setShouldNavigate({ route: '/onboarding/consent' });
          return;
        }

        // E) Vérifier disclaimer médical
        console.log('[INDEX] 📍 Étape E: Vérification disclaimer');
        console.log('[INDEX] hasSeenDisclaimer =', onboardingStore.hasSeenDisclaimer);
        if (!onboardingStore.hasSeenDisclaimer) {
          console.log('[INDEX] ✅ Disclaimer non vu → redirection vers /onboarding/disclaimer');
          hasCheckedRoutingRef.current = true;
          setIsCheckingRouting(false);
          setShouldNavigate({ route: '/onboarding/disclaimer' });
          return;
        }

        // F) Vérifier onboarding complet (slides)
        console.log('[INDEX] 📍 Étape F: Vérification onboarding slides');
        console.log('[INDEX] hasCompletedOnboarding =', onboardingStore.hasCompletedOnboarding);
        if (!onboardingStore.hasCompletedOnboarding) {
          console.log('[INDEX] ✅ Onboarding slides non terminés → redirection vers /onboarding');
          hasCheckedRoutingRef.current = true;
          setIsCheckingRouting(false);
          setShouldNavigate({ route: '/onboarding' });
          return;
        }

        // Tout est OK, afficher le contenu
        console.log('[INDEX] ✅ Tous les guards passés, affichage Home');
        hasCheckedRoutingRef.current = true;
        setIsCheckingRouting(false);
      } catch (error) {
        console.error('[INDEX] Erreur dans checkRouting:', error);
        hasCheckedRoutingRef.current = true;
        setIsCheckingRouting(false);
        // En cas d'erreur, rediriger vers login pour sécurité
        setShouldNavigate({ route: '/login' });
      }
    };

    checkRouting();
  }, [isAuthenticated, router, onboardingStore.hydrated, onboardingStore.hasCompletedOnboarding]);

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

