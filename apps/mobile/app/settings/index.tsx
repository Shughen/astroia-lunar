/**
 * Écran des réglages
 * Route : /settings
 */

import React from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  Alert,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { useRouter } from 'expo-router';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { useOnboardingStore } from '../../stores/useOnboardingStore';
import { useNatalStore } from '../../stores/useNatalStore';
import { colors, fonts, spacing, borderRadius } from '../../constants/theme';

export default function SettingsScreen() {
  const router = useRouter();
  const { reset: resetOnboarding } = useOnboardingStore();
  const { clearChart } = useNatalStore();

  const settingsItems = [
    {
      id: 'profile',
      emoji: '👤',
      title: 'Profil',
      description: 'Informations personnelles et préférences',
    },
    {
      id: 'notifications',
      emoji: '🔔',
      title: 'Notifications',
      description: 'Gérer les alertes et notifications',
    },
    {
      id: 'upcoming',
      emoji: '🔮',
      title: 'À venir',
      description: 'Fonctionnalités à venir',
    },
  ];

  const handleItemPress = (itemId: string) => {
    // Placeholder - navigation à implémenter
    console.log(`Navigation vers: ${itemId}`);
  };

  const handleResetWelcome = async () => {
    Alert.alert(
      'Réinitialiser Welcome',
      'Tu vas voir à nouveau l\'écran de bienvenue au prochain lancement.',
      [
        { text: 'Annuler', style: 'cancel' },
        {
          text: 'Réinitialiser',
          style: 'destructive',
          onPress: async () => {
            await AsyncStorage.removeItem('hasSeenWelcomeScreen');
            console.log('[SETTINGS] ✅ hasSeenWelcomeScreen supprimé');
            Alert.alert('Succès', 'Welcome réinitialisé ! Redémarre l\'app pour le voir.');
          },
        },
      ]
    );
  };

  const handleResetOnboarding = async () => {
    Alert.alert(
      'Réinitialiser Onboarding',
      'Tu devras refaire l\'onboarding au prochain lancement.',
      [
        { text: 'Annuler', style: 'cancel' },
        {
          text: 'Réinitialiser',
          style: 'destructive',
          onPress: async () => {
            await AsyncStorage.removeItem('onboarding_completed');
            console.log('[SETTINGS] ✅ onboarding_completed supprimé');
            Alert.alert('Succès', 'Onboarding réinitialisé ! Redémarre l\'app.');
          },
        },
      ]
    );
  };

  const handleResetAll = async () => {
    Alert.alert(
      'Réinitialiser Tout',
      'Tu vas réinitialiser welcome, onboarding et thème natal. Le flow complet recommencera.',
      [
        { text: 'Annuler', style: 'cancel' },
        {
          text: 'Tout réinitialiser',
          style: 'destructive',
          onPress: async () => {
            try {
              // Reset onboarding via store (+ set hydrated=false)
              await resetOnboarding();

              // Clear natal chart
              clearChart();

              console.log('[SETTINGS] ✅ Onboarding + Natal réinitialisés');
              Alert.alert(
                'Succès',
                'Tout réinitialisé ! Retour au Home pour redémarrer.',
                [{ text: 'OK', onPress: () => router.replace('/') }]
              );
            } catch (error: any) {
              Alert.alert('Erreur', error.message || 'Échec reset');
            }
          },
        },
      ]
    );
  };

  return (
    <LinearGradient colors={colors.darkBg} style={styles.container}>
      <ScrollView contentContainerStyle={styles.scrollContent}>
        {/* Header */}
        <View style={styles.header}>
          <TouchableOpacity
            style={styles.backButton}
            onPress={() => router.canGoBack() ? router.back() : router.replace('/')}
          >
            <Text style={styles.backText}>← Retour</Text>
          </TouchableOpacity>
          
          <View style={styles.titleContainer}>
            <Text style={styles.title}>⚙️ Réglages</Text>
            <Text style={styles.subtitle}>Paramètres de l'application</Text>
          </View>
        </View>

        {/* Liste des réglages */}
        <View style={styles.listContainer}>
          {settingsItems.map((item) => (
            <TouchableOpacity
              key={item.id}
              style={styles.settingsItem}
              onPress={() => handleItemPress(item.id)}
            >
              <Text style={styles.itemEmoji}>{item.emoji}</Text>
              <View style={styles.itemContent}>
                <Text style={styles.itemTitle}>{item.title}</Text>
                <Text style={styles.itemDescription}>{item.description}</Text>
              </View>
              <Text style={styles.itemArrow}>→</Text>
            </TouchableOpacity>
          ))}
        </View>

        {/* Section Debug/Reset */}
        <View style={styles.debugSection}>
          <Text style={styles.debugSectionTitle}>🧪 Debug / Tests</Text>
          <Text style={styles.debugSectionSubtitle}>
            Réinitialiser les flags pour tester le flow
          </Text>
          
          <TouchableOpacity
            style={[styles.debugButton, styles.debugButtonWarning]}
            onPress={handleResetWelcome}
          >
            <Text style={styles.debugButtonText}>🔄 Réinitialiser Welcome</Text>
            <Text style={styles.debugButtonSubtext}>
              Supprime hasSeenWelcomeScreen
            </Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={[styles.debugButton, styles.debugButtonWarning]}
            onPress={handleResetOnboarding}
          >
            <Text style={styles.debugButtonText}>🔄 Réinitialiser Onboarding</Text>
            <Text style={styles.debugButtonSubtext}>
              Supprime onboarding_completed
            </Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={[styles.debugButton, styles.debugButtonDanger]}
            onPress={handleResetAll}
          >
            <Text style={styles.debugButtonText}>🗑️ Tout réinitialiser</Text>
            <Text style={styles.debugButtonSubtext}>
              Supprime welcome + onboarding
            </Text>
          </TouchableOpacity>
        </View>
      </ScrollView>
    </LinearGradient>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  scrollContent: {
    padding: spacing.lg,
    paddingTop: 60,
  },
  header: {
    marginBottom: spacing.xl,
  },
  backButton: {
    marginBottom: spacing.md,
  },
  backText: {
    ...fonts.body,
    color: colors.accent,
    fontSize: 16,
  },
  titleContainer: {
    alignItems: 'center',
  },
  title: {
    ...fonts.h1,
    color: colors.text,
    marginBottom: spacing.xs,
  },
  subtitle: {
    ...fonts.body,
    color: colors.textMuted,
  },
  listContainer: {
    gap: spacing.md,
  },
  settingsItem: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.md,
    padding: spacing.lg,
    borderWidth: 1,
    borderColor: 'rgba(183, 148, 246, 0.2)',
  },
  itemEmoji: {
    fontSize: 32,
    marginRight: spacing.md,
  },
  itemContent: {
    flex: 1,
  },
  itemTitle: {
    ...fonts.h3,
    color: colors.text,
    marginBottom: spacing.xs,
  },
  itemDescription: {
    ...fonts.bodySmall,
    color: colors.textMuted,
  },
  itemArrow: {
    ...fonts.body,
    color: colors.accent,
    fontSize: 20,
    marginLeft: spacing.sm,
  },
  debugSection: {
    marginTop: spacing.xxl,
    paddingTop: spacing.xl,
    borderTopWidth: 1,
    borderTopColor: 'rgba(183, 148, 246, 0.2)',
  },
  debugSectionTitle: {
    ...fonts.h3,
    color: colors.text,
    marginBottom: spacing.xs,
  },
  debugSectionSubtitle: {
    ...fonts.bodySmall,
    color: colors.textMuted,
    marginBottom: spacing.lg,
  },
  debugButton: {
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.md,
    padding: spacing.md,
    marginBottom: spacing.md,
    borderWidth: 1,
  },
  debugButtonWarning: {
    borderColor: colors.warning + '40',
  },
  debugButtonDanger: {
    borderColor: colors.error + '40',
  },
  debugButtonText: {
    ...fonts.body,
    color: colors.text,
    fontWeight: '600',
    marginBottom: spacing.xs,
  },
  debugButtonSubtext: {
    ...fonts.bodySmall,
    color: colors.textMuted,
    fontSize: 12,
  },
});

