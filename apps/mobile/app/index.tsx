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
  Modal,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';

// Fallback si LinearGradient n'est pas disponible
const LinearGradientComponent = LinearGradient || (({ colors, style, children, ...props }: any) => {
  // View est déjà importé depuis react-native plus haut
  return <View style={[{ backgroundColor: colors?.[0] || '#1a0b2e' }, style]} {...props}>{children}</View>;
});
import { useRouter, useFocusEffect } from 'expo-router';
import { useAuthStore } from '../stores/useAuthStore';
import { useOnboardingStore } from '../stores/useOnboardingStore';
import { lunarReturns, LunarReturn, isDevAuthBypassActive, getDevUserId } from '../services/api';
import { colors, fonts, spacing, borderRadius } from '../constants/theme';
import { formatDate, getDaysUntil } from '../utils/date';
import { formatAspects, parseInterpretation } from '../utils/astrology-format';
import DailyLunarClimate from '../components/DailyLunarClimate';
import { getMoonPositionWithCache } from '../services/moonPositionCache';
import { getDailyClimateWithCache, DailyClimate, DailyInsight } from '../services/dailyClimateCache';
import { MoonPosition } from '../services/lunarClimate';

// Fonction utilitaire pour obtenir la salutation selon l'heure
const getTimeBasedGreeting = (): string => {
  const hour = new Date().getHours();

  if (hour >= 6 && hour < 12) {
    return 'Bonjour';
  } else if (hour >= 12 && hour < 18) {
    return 'Bon après-midi';
  } else if (hour >= 18 && hour < 24) {
    return 'Bonsoir';
  } else {
    return 'Belle nuit';
  }
};

export default function HomeScreen() {
  const router = useRouter();
  const { isAuthenticated } = useAuthStore();
  const onboardingStore = useOnboardingStore();
  const [nextLunarReturn, setNextLunarReturn] = useState<LunarReturn | null>(null);
  const [loadingNext, setLoadingNext] = useState(false);
  const [generating, setGenerating] = useState(false);
  const [modalVisible, setModalVisible] = useState(false);
  const [isCheckingRouting, setIsCheckingRouting] = useState(true);
  const [shouldNavigate, setShouldNavigate] = useState<{ route: string } | null>(null);
  const hasCheckedRoutingRef = useRef(false);
  const isMountedRef = useRef(false);
  const [moonPosition, setMoonPosition] = useState<MoonPosition | null>(null);
  const [dailyInsight, setDailyInsight] = useState<DailyInsight | null>(null);
  const isLoadingDailyClimateRef = useRef(false);
  const [greeting, setGreeting] = useState(getTimeBasedGreeting());

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

  // Charger daily climate avec cache (appelé au mount initial)
  useEffect(() => {
    // En mode DEV_AUTH_BYPASS, charger même sans authentification
    if ((isAuthenticated || isDevAuthBypassActive()) && !isCheckingRouting) {
      loadNextLunarReturn();
      loadDailyClimate(false); // false = utiliser cache
    }
  }, [isAuthenticated, isCheckingRouting]);

  // Refresh daily climate au focus de l'écran (avec cache quotidien)
  useFocusEffect(
    useCallback(() => {
      // Ne charger que si authentifié et routing vérifié
      if ((isAuthenticated || isDevAuthBypassActive()) && !isCheckingRouting) {
        console.log('[INDEX] 🔄 useFocusEffect: écran Home en focus, refresh daily climate');
        loadDailyClimate(false); // false = utiliser cache si même jour

        // Mettre à jour la salutation au focus
        setGreeting(getTimeBasedGreeting());
      }
    }, [isAuthenticated, isCheckingRouting])
  );

  const loadDailyClimate = async (forceRefresh: boolean = false) => {
    // Éviter les appels concurrents
    if (isLoadingDailyClimateRef.current) {
      console.log('[INDEX] ⏭️ Chargement daily climate déjà en cours, skip');
      return;
    }

    isLoadingDailyClimateRef.current = true;

    try {
      // Essayer de récupérer le climate complet avec insight
      const climate = await getDailyClimateWithCache(forceRefresh);

      if (climate) {
        // Success: climate complet avec insight
        setMoonPosition(climate.moon);
        setDailyInsight(climate.insight);
      } else {
        // Fallback: API failed, utiliser seulement moonPosition
        console.warn('[INDEX] ⚠️ Daily climate API failed, fallback sur moonPosition seul');
        const position = await getMoonPositionWithCache(forceRefresh);
        setMoonPosition(position);
        setDailyInsight(null); // Pas d'insight
      }
    } catch (error) {
      console.error('[INDEX] ❌ Erreur chargement daily climate:', error);
      // Dernier fallback: essayer au moins de charger moonPosition
      try {
        const position = await getMoonPositionWithCache(forceRefresh);
        setMoonPosition(position);
        setDailyInsight(null);
      } catch (fallbackError) {
        console.error('[INDEX] ❌ Erreur fallback moonPosition:', fallbackError);
      }
    } finally {
      isLoadingDailyClimateRef.current = false;
    }
  };

  const loadNextLunarReturn = async () => {
    setLoadingNext(true);
    try {
      const next = await lunarReturns.getNext();
      setNextLunarReturn(next);
    } catch (error: any) {
      console.error('Erreur chargement prochain retour:', error);
      // Ne pas afficher d'erreur si 404 (pas de retours générés)
      if (error.response?.status !== 404) {
        handleApiError(error);
      }
    } finally {
      setLoadingNext(false);
    }
  };

  const handleGenerate = async () => {
    setGenerating(true);
    try {
      await lunarReturns.generate();
      Alert.alert('Succès', 'Révolutions lunaires générées avec succès ! ✨');
      await loadNextLunarReturn();
    } catch (error: any) {
      handleApiError(error);
    } finally {
      setGenerating(false);
    }
  };

  const handleApiError = (error: any) => {
    const errorData = error.response?.data;
    if (errorData?.detail && typeof errorData.detail === 'object') {
      // Format structuré: {detail: "...", step: "...", correlation_id: "..."}
      const message = errorData.detail.detail || errorData.detail;
      const correlationId = errorData.detail.correlation_id;
      Alert.alert(
        'Erreur',
        `${message}${correlationId ? `\n\nRef: ${correlationId}` : ''}`
      );
    } else {
      Alert.alert('Erreur', error.response?.data?.detail || error.message || 'Une erreur est survenue');
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
          <Text style={styles.title}>🌙 Astroia Lunar</Text>
          <Text style={styles.subtitle}>Ton tableau de bord astrologique</Text>
          {isDevAuthBypassActive() && (
            <Text style={styles.devBypassLabel}>
              DEV AUTH BYPASS (user_id={getDevUserId()})
            </Text>
          )}
        </View>

        {/* Salutation temporelle */}
        {moonPosition && (
          <Text style={styles.greeting}>{greeting}</Text>
        )}

        {/* Climat Lunaire du Jour - HERO CARD */}
        {moonPosition && <DailyLunarClimate moonPosition={moonPosition} insight={dailyInsight} />}

        {/* Prochain retour lunaire */}
        <TouchableOpacity
          style={styles.nextLunarReturnCard}
          onPress={() => {
            if (nextLunarReturn) {
              setModalVisible(true);
            }
          }}
          disabled={!nextLunarReturn}
          activeOpacity={nextLunarReturn ? 0.7 : 1}
        >
          <Text style={styles.cardTitle}>Prochaine révolution lunaire</Text>
          {loadingNext ? (
            <View style={styles.loadingContainer}>
              <ActivityIndicator color={colors.accent} />
            </View>
          ) : nextLunarReturn ? (
            <>
              <Text style={styles.returnDate}>{formatDate(nextLunarReturn.return_date)}</Text>
              <Text style={styles.daysUntil}>
                dans {getDaysUntil(nextLunarReturn.return_date)} jour{getDaysUntil(nextLunarReturn.return_date) > 1 ? 's' : ''}
              </Text>
              {nextLunarReturn.moon_sign && (
                <Text style={styles.returnDetails}>
                  Lune en {nextLunarReturn.moon_sign}
                  {nextLunarReturn.lunar_ascendant && ` • Ascendant ${nextLunarReturn.lunar_ascendant}`}
                </Text>
              )}
              <View style={styles.ctaContainer}>
                <TouchableOpacity
                  style={styles.primaryCTA}
                  onPress={(e) => {
                    e.stopPropagation();
                    router.push('/lunar-returns/timeline');
                  }}
                >
                  <Text style={styles.primaryCTAText}>Voir ma timeline</Text>
                </TouchableOpacity>
                <Text style={styles.tapHint}>Tape pour voir les détails</Text>
              </View>
            </>
          ) : (
            <>
              <Text style={styles.emptyText}>
                Aucune révolution lunaire générée pour le moment
              </Text>
              <TouchableOpacity
                style={styles.generateButton}
                onPress={(e) => {
                  e.stopPropagation();
                  handleGenerate();
                }}
                disabled={generating}
              >
                {generating ? (
                  <ActivityIndicator color={colors.text} />
                ) : (
                  <Text style={styles.generateButtonText}>Générer mes révolutions</Text>
                )}
              </TouchableOpacity>
            </>
          )}
        </TouchableOpacity>

        {/* Menu principal */}
        <View style={styles.grid}>
          <TouchableOpacity
            style={styles.menuCard}
            onPress={() => router.push('/natal-chart')}
          >
            <Text style={styles.menuEmoji}>⭐</Text>
            <Text style={styles.menuTitle}>Thème Natal</Text>
            <Text style={styles.menuDesc}>Calcule ton thème natal complet</Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={styles.menuCard}
            onPress={() => router.push('/lunar-returns/timeline')}
          >
            <Text style={styles.menuEmoji}>🌙</Text>
            <Text style={styles.menuTitle}>Mes révolutions</Text>
            <Text style={styles.menuDesc}>Timeline de tes révolutions lunaires</Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={styles.menuCard}
            onPress={() => router.push('/transits/overview')}
          >
            <Text style={styles.menuEmoji}>🔮</Text>
            <Text style={styles.menuTitle}>Transits</Text>
            <Text style={styles.menuDesc}>Transits planétaires actuels</Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={styles.menuCard}
            onPress={() => router.push('/calendar/month')}
          >
            <Text style={styles.menuEmoji}>📅</Text>
            <Text style={styles.menuTitle}>Calendrier</Text>
            <Text style={styles.menuDesc}>Phases lunaires et événements</Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={styles.menuCard}
            onPress={() => router.push('/settings')}
          >
            <Text style={styles.menuEmoji}>⚙️</Text>
            <Text style={styles.menuTitle}>Réglages</Text>
            <Text style={styles.menuDesc}>Profil et paramètres</Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={styles.menuCard}
            onPress={() => router.push('/debug/selftest')}
          >
            <Text style={styles.menuEmoji}>🔧</Text>
            <Text style={styles.menuTitle}>Debug</Text>
            <Text style={styles.menuDesc}>Tests techniques</Text>
          </TouchableOpacity>
        </View>
      </ScrollView>

      {/* Modal détail prochain retour lunaire */}
      <Modal
        visible={modalVisible}
        transparent
        animationType="fade"
        onRequestClose={() => setModalVisible(false)}
      >
        <View style={detailStyles.modalOverlay}>
          <View style={detailStyles.modalContent}>
            <View style={detailStyles.modalHeader}>
              <Text style={detailStyles.modalTitle}>Détail révolution lunaire</Text>
            </View>
            
            <ScrollView 
              style={detailStyles.modalScrollView}
              contentContainerStyle={detailStyles.modalScrollContent}
              showsVerticalScrollIndicator={false}
            >
              {nextLunarReturn && (
                <>
                  {/* Date/Heure */}
                  <View style={detailStyles.detailSection}>
                    <Text style={detailStyles.detailSectionTitle}>Date et heure</Text>
                    <Text style={detailStyles.detailSectionValue}>
                      {formatDate(nextLunarReturn.return_date)}
                    </Text>
                  </View>

                  {/* Ascendant lunaire, signe lunaire, maison */}
                  <View style={detailStyles.detailSection}>
                    <Text style={detailStyles.detailSectionTitle}>Position lunaire</Text>
                    <View style={detailStyles.detailRow}>
                      {nextLunarReturn.lunar_ascendant && (
                        <Text style={detailStyles.detailValue}>
                          Ascendant: <Text style={detailStyles.detailValueHighlight}>{nextLunarReturn.lunar_ascendant}</Text>
                        </Text>
                      )}
                    </View>
                    <View style={detailStyles.detailRow}>
                      {nextLunarReturn.moon_sign && (
                        <Text style={detailStyles.detailValue}>
                          Signe lunaire: <Text style={detailStyles.detailValueHighlight}>{nextLunarReturn.moon_sign}</Text>
                        </Text>
                      )}
                    </View>
                    {nextLunarReturn.moon_house && (
                      <View style={detailStyles.detailRow}>
                        <Text style={detailStyles.detailValue}>
                          Maison: <Text style={detailStyles.detailValueHighlight}>{nextLunarReturn.moon_house}</Text>
                        </Text>
                      </View>
                    )}
                  </View>

                  {/* Aspects */}
                  {nextLunarReturn.aspects && nextLunarReturn.aspects.length > 0 && (
                    <View style={detailStyles.detailSection}>
                      <Text style={detailStyles.detailSectionTitle}>Aspects</Text>
                      {formatAspects(nextLunarReturn.aspects).map((aspect, index) => (
                        <Text key={index} style={detailStyles.aspectItem}>
                          • {aspect}
                        </Text>
                      ))}
                    </View>
                  )}

                  {/* Interprétation */}
                  {nextLunarReturn.interpretation && (
                    <View style={detailStyles.detailSection}>
                      <Text style={detailStyles.detailSectionTitle}>Interprétation</Text>
                      <View style={detailStyles.interpretationContainer}>
                        {parseInterpretation(nextLunarReturn.interpretation).map((para) => (
                          <Text key={`para-${para.index}`} style={detailStyles.interpretationParagraph}>
                            {para.parts.map((part) => (
                              <Text
                                key={part.key}
                                style={[
                                  detailStyles.interpretationText,
                                  part.type === 'bold' && detailStyles.interpretationBold,
                                ]}
                              >
                                {part.content}
                              </Text>
                            ))}
                          </Text>
                        ))}
                      </View>
                    </View>
                  )}
                </>
              )}
            </ScrollView>

            <View style={detailStyles.modalActions}>
              <TouchableOpacity
                style={detailStyles.modalSecondaryButton}
                onPress={() => {
                  setModalVisible(false);
                  router.push('/lunar-returns/timeline');
                }}
              >
                <Text style={detailStyles.modalSecondaryButtonText}>Voir ma timeline</Text>
              </TouchableOpacity>
              <TouchableOpacity
                style={detailStyles.modalCloseButton}
                onPress={() => setModalVisible(false)}
              >
                <Text style={detailStyles.modalCloseButtonText}>Fermer</Text>
              </TouchableOpacity>
            </View>
          </View>
        </View>
      </Modal>
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
  devBypassLabel: {
    ...fonts.bodySmall,
    color: colors.accent,
    textAlign: 'center',
    marginTop: spacing.xs,
    fontSize: 10,
    opacity: 0.7,
  },
  greeting: {
    ...fonts.body,
    color: 'rgba(255, 255, 255, 0.5)',
    fontSize: 14,
    fontWeight: '300',
    marginBottom: spacing.md,
    paddingLeft: spacing.lg,
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
  nextLunarReturnCard: {
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.md,
    padding: spacing.lg,
    marginBottom: spacing.lg,
  },
  cardTitle: {
    ...fonts.h3,
    color: colors.text,
    marginBottom: spacing.md,
  },
  loadingContainer: {
    padding: spacing.md,
    alignItems: 'center',
  },
  returnDate: {
    ...fonts.h2,
    color: colors.accent,
    marginBottom: spacing.xs,
  },
  daysUntil: {
    ...fonts.body,
    color: colors.textMuted,
    marginBottom: spacing.sm,
  },
  returnDetails: {
    ...fonts.bodySmall,
    color: colors.textMuted,
    marginBottom: spacing.md,
  },
  ctaContainer: {
    marginTop: spacing.md,
  },
  primaryCTA: {
    backgroundColor: colors.accent,
    paddingVertical: spacing.md,
    paddingHorizontal: spacing.lg,
    borderRadius: borderRadius.md,
    alignItems: 'center',
    marginBottom: spacing.xs,
  },
  primaryCTAText: {
    ...fonts.button,
    color: colors.text,
    fontSize: fonts.sizes.md,
  },
  tapHint: {
    ...fonts.caption,
    color: colors.textMuted,
    textAlign: 'center',
    fontStyle: 'italic',
  },
  emptyText: {
    ...fonts.body,
    color: colors.textMuted,
    textAlign: 'center',
    marginBottom: spacing.md,
  },
  generateButton: {
    backgroundColor: colors.accent,
    paddingVertical: spacing.md,
    paddingHorizontal: spacing.lg,
    borderRadius: borderRadius.md,
    alignItems: 'center',
  },
  generateButtonText: {
    ...fonts.button,
    color: colors.text,
  },
});

// Styles pour la modal de détail
const detailStyles = StyleSheet.create({
  modalOverlay: {
    flex: 1,
    backgroundColor: 'rgba(0, 0, 0, 0.8)',
    justifyContent: 'center',
    alignItems: 'center',
  },
  modalContent: {
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.md,
    padding: spacing.lg,
    width: '90%',
    maxHeight: '80%',
    flexDirection: 'column',
  },
  modalHeader: {
    marginBottom: spacing.md,
  },
  modalTitle: {
    ...fonts.h2,
    color: colors.text,
  },
  modalScrollView: {
    flexShrink: 1,
    maxHeight: 400,
  },
  modalScrollContent: {
    paddingBottom: spacing.md,
  },
  modalActions: {
    flexDirection: 'row',
    marginTop: spacing.md,
  },
  modalSecondaryButton: {
    flex: 1,
    backgroundColor: colors.cardBg,
    borderWidth: 1,
    borderColor: colors.accent,
    paddingVertical: spacing.md,
    paddingHorizontal: spacing.lg,
    borderRadius: borderRadius.md,
    alignItems: 'center',
    marginRight: spacing.sm,
  },
  modalSecondaryButtonText: {
    ...fonts.button,
    color: colors.accent,
  },
  modalCloseButton: {
    flex: 1,
    backgroundColor: colors.accent,
    paddingVertical: spacing.md,
    paddingHorizontal: spacing.lg,
    borderRadius: borderRadius.md,
    alignItems: 'center',
  },
  modalCloseButtonText: {
    ...fonts.button,
    color: colors.text,
  },
  detailSection: {
    marginBottom: spacing.lg,
  },
  detailSectionTitle: {
    ...fonts.h3,
    color: colors.text,
    marginBottom: spacing.sm,
  },
  detailSectionValue: {
    ...fonts.body,
    color: colors.textMuted,
  },
  detailRow: {
    marginBottom: spacing.xs,
  },
  detailValue: {
    ...fonts.body,
    color: colors.textMuted,
  },
  detailValueHighlight: {
    color: colors.text,
    fontWeight: '600',
  },
  aspectItem: {
    ...fonts.bodySmall,
    color: colors.textMuted,
    marginBottom: spacing.xs,
    marginLeft: spacing.xs,
  },
  interpretationContainer: {
    marginTop: spacing.xs,
  },
  interpretationParagraph: {
    ...fonts.body,
    color: colors.textMuted,
    lineHeight: 24,
    marginBottom: spacing.md,
  },
  interpretationText: {
    ...fonts.body,
    color: colors.textMuted,
  },
  interpretationBold: {
    fontWeight: '600',
    color: colors.text,
  },
});

