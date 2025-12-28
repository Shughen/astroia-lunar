/**
 * Écran d'onboarding : Slides de présentation
 */

import React, { useState, useRef, useEffect } from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  ScrollView,
  Dimensions,
  Animated,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Ionicons } from '@expo/vector-icons';
import { useRouter } from 'expo-router';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { colors, fonts, spacing, borderRadius } from '../constants/theme';

const { width } = Dimensions.get('window');

const STEPS = [
    {
      id: 'welcome',
      emoji: '🌙',
      title: 'Bienvenue sur Astroia Lunar',
      subtitle: 'Révolutions Lunaires',
      description: 'Découvre tes révolutions lunaires mensuelles et explore ton thème astrologique.',
    },
    {
      id: 'value1',
      emoji: '⭐',
      title: 'Thème natal précis',
      description: 'Calcule ton thème natal complet avec les positions planétaires exactes.',
    },
    {
      id: 'value2',
      emoji: '🌙',
      title: 'Révolutions lunaires',
      description: 'Suis tes révolutions lunaires mensuelles et découvre comment la lune influence ta vie.',
    },
    {
      id: 'value3',
      emoji: '🔮',
      title: 'Transits planétaires',
      description: 'Explore les transits actuels et leurs influences sur ton quotidien.',
    },
];

export default function OnboardingScreen() {
  const router = useRouter();
  const [currentStep, setCurrentStep] = useState(0);
  const scrollViewRef = useRef(null);
  const fadeAnim = useRef(new Animated.Value(1)).current;

  useEffect(() => {
    console.log('[ONBOARDING] ✅ Composant Onboarding monté, nombre de slides:', STEPS.length);
    console.log('[ONBOARDING] Slide initial:', currentStep, '-', STEPS[currentStep]?.title);
  }, []);

  useEffect(() => {
    if (currentStep >= 0 && currentStep < STEPS.length) {
      console.log('[ONBOARDING] currentStep changé →', currentStep, '-', STEPS[currentStep]?.title);
    }
  }, [currentStep]);

  const handleNext = async () => {
    console.log('[ONBOARDING] 🔘 handleNext appelé');
    console.log('[ONBOARDING]   currentStep =', currentStep);
    console.log('[ONBOARDING]   STEPS.length =', STEPS.length);
    console.log('[ONBOARDING]   STEPS.length - 1 =', STEPS.length - 1);
    console.log('[ONBOARDING]   Condition (currentStep < STEPS.length - 1) =', currentStep < STEPS.length - 1);
    
    if (currentStep < STEPS.length - 1) {
      console.log('[ONBOARDING] ✅ Slide suivant → animation fade out');
      const nextStep = currentStep + 1;
      console.log('[ONBOARDING]   nextStep calculé =', nextStep);
      
      // Fade out
      Animated.timing(fadeAnim, {
        toValue: 0,
        duration: 200,
        useNativeDriver: true,
      }).start(() => {
        console.log('[ONBOARDING] ✅ Fade out terminé → passage au slide', nextStep);
        setCurrentStep(nextStep);
        scrollViewRef.current?.scrollTo({ x: 0, y: 0, animated: false });
        
        // Fade in
        Animated.timing(fadeAnim, {
          toValue: 1,
          duration: 300,
          useNativeDriver: true,
        }).start(() => {
          console.log('[ONBOARDING] ✅ Fade in terminé → slide', nextStep, 'affiché');
        });
      });
    } else {
      // Dernier écran → marquer onboarding comme terminé et aller à Home
      console.log('[ONBOARDING] ✅ Dernier slide détecté → marquage onboarding_completed');
      await AsyncStorage.setItem('onboarding_completed', 'true');
      const check = await AsyncStorage.getItem('onboarding_completed');
      console.log('[ONBOARDING]   onboarding_completed défini =', check);
      console.log('[ONBOARDING]   Redirection vers /');
      router.replace('/');
    }
  };

  const handleSkip = async () => {
    console.log('[ONBOARDING] ⏭️ Skip cliqué → marquage onboarding_completed');
    // Marquer onboarding comme terminé
    await AsyncStorage.setItem('onboarding_completed', 'true');
    console.log('[ONBOARDING] onboarding_completed défini, redirection vers /');
    router.replace('/');
  };

  const currentStepData = STEPS[currentStep];

  return (
    <LinearGradient
      colors={colors.darkBg}
      style={styles.container}
      start={{ x: 0, y: 0 }}
      end={{ x: 1, y: 1 }}
    >
      <SafeAreaView style={styles.safeArea} edges={['top', 'bottom']}>
        {/* Header avec Skip */}
        <View style={styles.header}>
          <TouchableOpacity onPress={handleSkip} style={styles.skipButton}>
            <Text style={styles.skipText}>Passer</Text>
          </TouchableOpacity>
        </View>

        {/* Content */}
        <ScrollView
          ref={scrollViewRef}
          contentContainerStyle={styles.scrollContent}
          showsVerticalScrollIndicator={false}
        >
          <Animated.View style={[styles.content, { opacity: fadeAnim }]}>
            {/* Emoji */}
            <View style={styles.emojiContainer}>
              <Text style={styles.emoji}>{currentStepData.emoji}</Text>
            </View>

            {/* Title */}
            <Text style={styles.title}>{currentStepData.title}</Text>
            
            {/* Subtitle (si existe) */}
            {currentStepData.subtitle && (
              <Text style={styles.subtitle}>{currentStepData.subtitle}</Text>
            )}

            {/* Description */}
            <Text style={styles.description}>{currentStepData.description}</Text>
          </Animated.View>
        </ScrollView>

        {/* Footer avec indicateurs et bouton */}
        <View style={styles.footer}>
          {/* Indicateurs */}
          <View style={styles.indicators}>
            {STEPS.map((_, index) => (
              <View
                key={index}
                style={[
                  styles.indicator,
                  index === currentStep && styles.indicatorActive,
                ]}
              />
            ))}
          </View>

          {/* Bouton Suivant */}
          <TouchableOpacity
            style={styles.nextButton}
            onPress={handleNext}
            activeOpacity={0.8}
          >
            <LinearGradient
              colors={[colors.accent, colors.accentDark]}
              style={styles.nextButtonGradient}
              start={{ x: 0, y: 0 }}
              end={{ x: 1, y: 0 }}
            >
              <Text style={styles.nextButtonText}>
                {currentStep < STEPS.length - 1 ? 'Suivant' : 'Commencer'}
              </Text>
              <Ionicons name="arrow-forward" size={20} color={colors.text} />
            </LinearGradient>
          </TouchableOpacity>
        </View>
      </SafeAreaView>
    </LinearGradient>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  safeArea: {
    flex: 1,
  },
  header: {
    flexDirection: 'row',
    justifyContent: 'flex-end',
    paddingHorizontal: spacing.lg,
    paddingVertical: spacing.md,
  },
  skipButton: {
    paddingVertical: spacing.sm,
    paddingHorizontal: spacing.md,
  },
  skipText: {
    color: 'rgba(255, 255, 255, 0.7)',
    fontSize: fonts.sizes.md,
    fontWeight: '600',
  },
  scrollContent: {
    flexGrow: 1,
    paddingHorizontal: spacing.xl,
  },
  content: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    paddingVertical: spacing.xxl,
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
    fontSize: 32,
    fontWeight: 'bold',
    color: colors.text,
    textAlign: 'center',
    marginBottom: spacing.sm,
    textShadowColor: 'rgba(183, 148, 246, 0.5)',
    textShadowOffset: { width: 0, height: 2 },
    textShadowRadius: 10,
  },
  subtitle: {
    fontSize: 24,
    fontWeight: '600',
    color: colors.accent,
    textAlign: 'center',
    marginBottom: spacing.lg,
    textShadowColor: 'rgba(183, 148, 246, 0.4)',
    textShadowOffset: { width: 0, height: 2 },
    textShadowRadius: 8,
  },
  description: {
    fontSize: fonts.sizes.lg,
    color: 'rgba(255, 255, 255, 0.85)',
    textAlign: 'center',
    lineHeight: 28,
    paddingHorizontal: spacing.md,
    maxWidth: width * 0.8,
  },
  footer: {
    paddingHorizontal: spacing.xl,
    paddingBottom: spacing.lg,
    gap: spacing.lg,
  },
  indicators: {
    flexDirection: 'row',
    justifyContent: 'center',
    gap: spacing.sm,
  },
  indicator: {
    width: 8,
    height: 8,
    borderRadius: 4,
    backgroundColor: 'rgba(255, 255, 255, 0.3)',
  },
  indicatorActive: {
    backgroundColor: colors.accent,
    width: 24,
    shadowColor: colors.accent,
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.6,
    shadowRadius: 4,
  },
  nextButton: {
    borderRadius: borderRadius.lg,
    overflow: 'hidden',
    shadowColor: colors.accent,
    shadowOffset: { width: 0, height: 6 },
    shadowOpacity: 0.4,
    shadowRadius: 12,
    elevation: 8,
  },
  nextButtonGradient: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: spacing.md + 4,
    gap: spacing.sm,
  },
  nextButtonText: {
    color: colors.text,
    fontSize: fonts.sizes.lg,
    fontWeight: 'bold',
  },
});
