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
import AsyncStorage from '@react-native-async-storage/async-storage';
import { useAuthStore } from '../stores/useAuthStore';
import { useOnboardingStore } from '../stores/useOnboardingStore';
import { useNotificationsStore } from '../stores/useNotificationsStore';
import { useResetStore } from '../stores/useResetStore';
import { lunarReturns, LunarReturn, isDevAuthBypassActive, getDevAuthHeader, lunaPack } from '../services/api';
import { colors, fonts, spacing, borderRadius } from '../constants/theme';
import { JOURNAL_STORAGE_KEY } from '../constants/storageKeys';
import { DailyRitualCard } from '../components/DailyRitualCard';
import { VocWidget } from '../components/VocWidget';
import { setupNotificationTapListener, shouldReschedule } from '../services/notificationScheduler';
import { cleanupGhostFlags } from '../services/onboardingMigration';
import { trackEvent } from '../utils/analytics';
import { isProfileComplete } from '../utils/onboardingHelpers';

export default function HomeScreen() {
  const { t } = useTranslation();
  const router = useRouter();
  const { isAuthenticated } = useAuthStore();
  // ⚠️ CRITIQUE: Subscribe explicitement au flag hydrated via selector
  const isOnboardingHydrated = useOnboardingStore((state) => state.hydrated);
  const hasSeenWelcomeScreen = useOnboardingStore((state) => state.hasSeenWelcomeScreen);
  const hasAcceptedConsent = useOnboardingStore((state) => state.hasAcceptedConsent);
  const hasCompletedProfile = useOnboardingStore((state) => state.hasCompletedProfile);
  const hasSeenDisclaimer = useOnboardingStore((state) => state.hasSeenDisclaimer);
  const hasCompletedOnboarding = useOnboardingStore((state) => state.hasCompletedOnboarding);
  const hydrateOnboarding = useOnboardingStore((state) => state.hydrate);
  const resetProfileFlag = useOnboardingStore((state) => state.resetProfileFlag);
  const profileData = useOnboardingStore((state) => state.profileData);

  const { notificationsEnabled, hydrated, loadPreferences, scheduleAllNotifications } = useNotificationsStore();
  const { isResetting } = useResetStore();
  const [currentLunarReturn, setCurrentLunarReturn] = useState<LunarReturn | null>(null);
  const [isCheckingRouting, setIsCheckingRouting] = useState(true);
  const [isOnline, setIsOnline] = useState(true);
  const routingInFlightRef = useRef(false);
  const selfHealExecutedRef = useRef(false); // Guard anti-boucle pour self-heal
  const [dailyClimate, setDailyClimate] = useState<{
    date: string;
    moon: { sign: string; degree: number; phase: string };
    insight: { title: string; text: string; keywords: string[]; version: string };
  } | null>(null);
  const [dailyClimateLoading, setDailyClimateLoading] = useState(false);
  const [alreadyViewedToday, setAlreadyViewedToday] = useState(false);
  const [journalDoneToday, setJournalDoneToday] = useState(false);

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
        if (!isOnboardingHydrated) {
          await cleanupGhostFlags();
        }

        // Guard absolu: hydratation BLOQUANTE
        if (!isOnboardingHydrated) {
          console.log('[INDEX] ⏳ Hydratation en cours...');
          await hydrateOnboarding();
          console.log('[INDEX] ✅ Hydratation terminée');
          // IMPORTANT: Le state sera mis à jour et déclenchera un re-render via subscription
          return; // Sortir immédiatement, le prochain render verra hydrated=true
        }

        console.log('[INDEX] 📍 Début checkRouting');
        console.log('[INDEX] 📊 État onboarding:', {
          hasSeenWelcomeScreen,
          hasAcceptedConsent,
          hasCompletedProfile,
          hasSeenDisclaimer,
          hasCompletedOnboarding,
        });

        // SELF-HEAL: Vérifier et corriger incohérences profil/flags
        // Exécuter une seule fois par session pour éviter boucles infinies
        if (!selfHealExecutedRef.current) {
          const profileIsComplete = isProfileComplete(profileData);
          
          // Cas A: hasCompletedProfile=true mais profil incomplet
          if (hasCompletedProfile && !profileIsComplete) {
            console.log('[SELF_HEAL] ⚠️ Incohérence détectée: hasCompletedProfile=true mais profil incomplet');
            console.log('[SELF_HEAL] Profil actuel:', {
              hasProfileData: !!profileData,
              birthDate: profileData?.birthDate ? 'présent' : 'manquant',
              birthTime: profileData?.birthTime || 'manquant',
              birthPlace: profileData?.birthPlace || 'manquant',
              lat: profileData?.birthLatitude,
              lon: profileData?.birthLongitude,
            });
            console.log('[SELF_HEAL] → Réinitialisation du flag hasCompletedProfile');
            
            await resetProfileFlag();
            selfHealExecutedRef.current = true; // Marquer comme exécuté
            
            // Forcer redirection vers profile-setup
            console.log('[SELF_HEAL] → Redirection vers /onboarding/profile-setup');
            router.replace('/onboarding/profile-setup');
            return;
          }
          
          // Cas B: hasCompletedOnboarding=true mais profil incomplet
          // Ne pas toucher hasCompletedOnboarding mais forcer profile-setup
          if (hasCompletedOnboarding && !profileIsComplete) {
            console.log('[SELF_HEAL] ⚠️ Incohérence détectée: hasCompletedOnboarding=true mais profil incomplet');
            console.log('[SELF_HEAL] → Réinitialisation du flag hasCompletedProfile et redirection');
            
            await resetProfileFlag();
            selfHealExecutedRef.current = true; // Marquer comme exécuté
            
            // Forcer redirection vers profile-setup
            console.log('[SELF_HEAL] → Redirection vers /onboarding/profile-setup');
            router.replace('/onboarding/profile-setup');
            return;
          }
          
          // Si tout est cohérent, marquer comme vérifié pour éviter re-vérifications
          selfHealExecutedRef.current = true;
        }

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
        if (!hasSeenWelcomeScreen) {
          console.log('[INDEX] → Redirection /welcome');
          router.replace('/welcome');
          return;
        }

        // C) Vérifier consentement RGPD
        if (!hasAcceptedConsent) {
          console.log('[INDEX] → Redirection /onboarding/consent');
          router.replace('/onboarding/consent');
          return;
        }

        // D) Vérifier profil setup
        if (!hasCompletedProfile) {
          console.log('[INDEX] → Redirection /onboarding/profile-setup');
          router.replace('/onboarding/profile-setup');
          return;
        }

        // E) Vérifier disclaimer médical
        if (!hasSeenDisclaimer) {
          console.log('[INDEX] → Redirection /onboarding/disclaimer');
          router.replace('/onboarding/disclaimer');
          return;
        }

        // F) Vérifier onboarding complet (slides)
        if (!hasCompletedOnboarding) {
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
  }, [
    isAuthenticated,
    isResetting,
    isOnboardingHydrated,
    hasSeenWelcomeScreen,
    hasAcceptedConsent,
    hasCompletedProfile,
    hasSeenDisclaimer,
    hasCompletedOnboarding,
    hydrateOnboarding,
    resetProfileFlag,
    profileData,
    router,
  ]);

  // Réinitialiser le guard self-heal quand l'hydratation change (pour permettre re-vérification après reset)
  useEffect(() => {
    if (!isOnboardingHydrated) {
      selfHealExecutedRef.current = false;
    }
  }, [isOnboardingHydrated]);

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
      loadDailyClimate();
    }
  }, [isAuthenticated, isCheckingRouting]);

  // Précharger Daily Climate (sans lastViewedDate)
  const loadDailyClimate = async () => {
    if (dailyClimateLoading || dailyClimate) return;
    setDailyClimateLoading(true);
    try {
      const data = await lunaPack.getDailyClimate();
      setDailyClimate(data);
    } catch (error) {
      console.error('[INDEX] Erreur chargement Daily Climate:', error);
    } finally {
      setDailyClimateLoading(false);
    }
  };

  // Gérer le clic sur la carte Daily Climate
  const handleDailyClimatePress = async () => {
    try {
      // Lire lastViewedDate depuis AsyncStorage
      const lastViewedDate = await AsyncStorage.getItem('dailyClimate:lastViewedDate');
      const today = new Date().toISOString().split('T')[0]; // YYYY-MM-DD
      
      // Déterminer firstOfDay
      const firstOfDay = lastViewedDate !== today;
      
      // Écrire lastViewedDate = aujourd'hui
      await AsyncStorage.setItem('dailyClimate:lastViewedDate', today);
      setAlreadyViewedToday(true);
      
      // Track event
      trackEvent({
        name: 'daily_climate_view',
        properties: { firstOfDay, source: 'home' },
      });
      
      // Naviguer vers /lunar?focus=daily_climate
      router.push('/lunar?focus=daily_climate');
    } catch (error) {
      console.error('[INDEX] Erreur lors du clic Daily Climate:', error);
    }
  };

  // Construire le texte prefill pour le journal
  const buildJournalPrefill = (): string => {
    if (!dailyClimate) return '';
    
    const today = new Date().toISOString().split('T')[0]; // YYYY-MM-DD
    const title = dailyClimate.insight.title || 'Daily Climate';
    
    return `${today}\n\n${title}\n\nCe que je ressens aujourd'hui: …\n\nMon intention du jour: …`;
  };

  // Helper pour vérifier si une entrée de journal existe aujourd'hui
  const hasJournalEntryToday = (entries: Array<{ createdAtISO: string }>): boolean => {
    if (!entries || entries.length === 0) return false;
    
    const today = new Date().toDateString();
    return entries.some((entry) => {
      try {
        const entryDate = new Date(entry.createdAtISO);
        return entryDate.toDateString() === today;
      } catch {
        return false;
      }
    });
  };

  // Charger le statut du journal (entrée aujourd'hui ou non)
  const loadJournalStatus = async () => {
    try {
      const stored = await AsyncStorage.getItem(JOURNAL_STORAGE_KEY);
      if (stored) {
        const entries = JSON.parse(stored);
        setJournalDoneToday(hasJournalEntryToday(entries));
      } else {
        setJournalDoneToday(false);
      }
    } catch (error) {
      console.error('[INDEX] Erreur chargement statut journal:', error);
      setJournalDoneToday(false);
    }
  };

  // Gérer le clic sur "Écrire une note"
  const handleWriteNote = () => {
    const hasPrefill = !!dailyClimate;
    
    // Track event (optionnel, console-based)
    console.log('[INDEX] daily_climate_journal_cta', { source: 'home', prefill: hasPrefill });
    
    if (hasPrefill) {
      // Comportement actuel : prefill avec insight du jour
      const prefill = buildJournalPrefill();
      const encodedPrefill = encodeURIComponent(prefill);
      router.push(`/journal?prefill=${encodedPrefill}`);
    } else {
      // Ouvrir Journal vide (sans prefill)
      router.push('/journal');
    }
  };

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
        
        // Vérifier si Daily Climate consulté aujourd'hui
        (async () => {
          try {
            const lastViewedDate = await AsyncStorage.getItem('dailyClimate:lastViewedDate');
            const today = new Date().toISOString().split('T')[0]; // YYYY-MM-DD
            setAlreadyViewedToday(lastViewedDate === today);
          } catch (error) {
            console.error('[INDEX] Erreur vérification lastViewedDate:', error);
          }
        })();

        // Charger le statut du journal
        loadJournalStatus();
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

        {/* Carte Daily Climate Preview */}
        {dailyClimate && (
          <View style={styles.dailyClimateCard}>
            <TouchableOpacity
              onPress={handleDailyClimatePress}
              activeOpacity={0.8}
            >
              <View style={styles.dailyClimateHeader}>
                <Text style={styles.dailyClimateTitle}>🌙 Daily Climate</Text>
                {alreadyViewedToday && (
                  <View style={styles.viewedBadge}>
                    <Text style={styles.viewedBadgeText}>✓ Consulté aujourd'hui</Text>
                  </View>
                )}
              </View>
              
              {/* Meta lune */}
              <Text style={styles.dailyClimateMoon}>
                {dailyClimate.moon.phase} en {dailyClimate.moon.sign}
              </Text>
              
              {/* 3 lignes max de texte */}
              <Text style={styles.dailyClimateText} numberOfLines={3}>
                {dailyClimate.insight.text}
              </Text>
              
              {/* Max 4 keywords */}
              {dailyClimate.insight.keywords && dailyClimate.insight.keywords.length > 0 && (
                <View style={styles.dailyClimateKeywords}>
                  {dailyClimate.insight.keywords.slice(0, 4).map((keyword, idx) => (
                    <View key={idx} style={styles.keywordBadge}>
                      <Text style={styles.keywordText}>{keyword}</Text>
                    </View>
                  ))}
                </View>
              )}
            </TouchableOpacity>
          </View>
        )}

        {/* Widget Void of Course */}
        <VocWidget />

        {/* Bouton "Écrire une note" - toujours disponible */}
        <View style={styles.writeNoteCard}>
          <TouchableOpacity
            style={styles.writeNoteButton}
            onPress={handleWriteNote}
            activeOpacity={0.7}
          >
            <Text style={styles.writeNoteButtonText}>✍️ Écrire une note</Text>
          </TouchableOpacity>
        </View>

        {/* Menu principal MVP : Journal + Thème natal + Rapport + Réglages */}
        <View style={styles.grid}>
          <TouchableOpacity
            style={styles.menuCard}
            onPress={() => router.push('/journal')}
          >
            <View style={styles.menuCardHeader}>
              <Text style={styles.menuEmoji}>📖</Text>
              {journalDoneToday && (
                <View style={styles.journalBadge}>
                  <Text style={styles.journalBadgeText}>✅ Aujourd'hui</Text>
                </View>
              )}
            </View>
            <Text style={styles.menuTitle}>Journal</Text>
            <Text style={styles.menuDesc}>Mes entrées récentes</Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={styles.menuCard}
            onPress={() => {
              if (!isOnline) {
                Alert.alert('Hors ligne', 'Cette fonctionnalité nécessite une connexion Internet.');
                return;
              }
              router.push('/natal-chart');
            }}
            disabled={!isOnline}
          >
            <Text style={styles.menuEmoji}>⭐</Text>
            <Text style={styles.menuTitle}>Thème natal</Text>
            <Text style={styles.menuDesc}>Mon ciel de naissance</Text>
            {!isOnline && <Text style={styles.offlineBadge}>Hors ligne</Text>}
          </TouchableOpacity>

          <TouchableOpacity
            style={styles.menuCard}
            onPress={() => {
              if (!isOnline) {
                Alert.alert('Hors ligne', 'Cette fonctionnalité nécessite une connexion Internet.');
                return;
              }
              router.push('/lunar/report');
            }}
            disabled={!isOnline}
          >
            <Text style={styles.menuEmoji}>🌙</Text>
            <Text style={styles.menuTitle}>Rapport Mensuel</Text>
            <Text style={styles.menuDesc}>Révolution lunaire</Text>
            {!isOnline && <Text style={styles.offlineBadge}>Hors ligne</Text>}
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
  menuCardHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    width: '100%',
    marginBottom: spacing.sm,
    position: 'relative',
  },
  menuEmoji: {
    fontSize: 48,
  },
  journalBadge: {
    position: 'absolute',
    top: -4,
    right: -8,
    backgroundColor: 'rgba(74, 222, 128, 0.2)',
    borderWidth: 1,
    borderColor: '#4ade80',
    borderRadius: 12,
    paddingHorizontal: spacing.xs,
    paddingVertical: 2,
  },
  journalBadgeText: {
    fontSize: 10,
    color: '#4ade80',
    fontWeight: '600',
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
  dailyClimateCard: {
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.md,
    padding: spacing.lg,
    marginBottom: spacing.md,
    borderWidth: 1,
    borderColor: 'rgba(183, 148, 246, 0.1)',
  },
  dailyClimateHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: spacing.sm,
  },
  dailyClimateTitle: {
    ...fonts.h3,
    color: colors.text,
    flex: 1,
  },
  viewedBadge: {
    backgroundColor: 'rgba(74, 222, 128, 0.15)',
    borderWidth: 1,
    borderColor: '#4ade80',
    borderRadius: 4,
    paddingHorizontal: spacing.sm,
    paddingVertical: spacing.xs,
    marginLeft: spacing.sm,
  },
  viewedBadgeText: {
    fontSize: 10,
    color: '#4ade80',
    fontWeight: '600',
  },
  dailyClimateMoon: {
    ...fonts.bodySmall,
    color: colors.accent,
    marginBottom: spacing.sm,
    textTransform: 'uppercase',
    letterSpacing: 0.5,
  },
  dailyClimateText: {
    ...fonts.body,
    color: colors.text,
    lineHeight: 22,
    marginBottom: spacing.sm,
  },
  dailyClimateKeywords: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: spacing.xs,
    marginTop: spacing.xs,
  },
  keywordBadge: {
    backgroundColor: 'rgba(183, 148, 246, 0.15)',
    borderRadius: borderRadius.sm,
    paddingHorizontal: spacing.sm,
    paddingVertical: spacing.xs,
  },
  keywordText: {
    ...fonts.caption,
    color: colors.accent,
    fontSize: 11,
  },
  writeNoteCard: {
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.md,
    padding: spacing.lg,
    marginBottom: spacing.md,
    borderWidth: 1,
    borderColor: 'rgba(183, 148, 246, 0.1)',
  },
  writeNoteButton: {
    paddingVertical: spacing.sm,
    paddingHorizontal: spacing.md,
    backgroundColor: 'rgba(183, 148, 246, 0.15)',
    borderRadius: borderRadius.sm,
    borderWidth: 1,
    borderColor: 'rgba(183, 148, 246, 0.3)',
    alignItems: 'center',
  },
  writeNoteButtonText: {
    ...fonts.body,
    color: colors.accent,
    fontSize: 14,
  },
});

