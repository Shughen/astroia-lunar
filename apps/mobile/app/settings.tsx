/**
 * Écran Réglages (Phase 1.4 MVP)
 *
 * Features :
 * - Toggle notifications (VoC + cycle lunaire)
 * - Informations utilisateur (email, naissance)
 * - Déconnexion
 */

import React, { useState, useEffect } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  Switch,
  Alert,
  Linking,
  Platform,
} from 'react-native';
import { router } from 'expo-router';
import { useTranslation } from 'react-i18next';
import { useAuthStore } from '../stores/useAuthStore';
import { useNotificationsStore } from '../stores/useNotificationsStore';

// DEV ONLY: QA Helper for notifications (null in production)
import DevQASection from '../components/DevQASection';

export default function SettingsScreen() {
  const { t } = useTranslation();
  const { user, logout } = useAuthStore();
  const {
    notificationsEnabled,
    hydrated,
    loadPreferences,
    setNotificationsEnabled,
  } = useNotificationsStore();

  const [isTogglingNotifications, setIsTogglingNotifications] = useState(false);

  useEffect(() => {
    // Charger préférences au mount
    if (!hydrated) {
      loadPreferences();
    }
  }, [hydrated, loadPreferences]);

  const handleNotificationToggle = async (value: boolean) => {
    setIsTogglingNotifications(true);

    try {
      const success = await setNotificationsEnabled(value);

      if (!success && value) {
        // Permission refusée
        Alert.alert(
          t('settings.notifications.permissionRequired'),
          t('settings.notifications.permissionDesc'),
          [
            { text: t('common.cancel'), style: 'cancel' },
            {
              text: t('settings.notifications.openSettings'),
              onPress: () => {
                if (Platform.OS === 'ios') {
                  Linking.openURL('app-settings:');
                } else {
                  Linking.openSettings();
                }
              },
            },
          ]
        );
      } else if (success && value) {
        Alert.alert(
          t('settings.notifications.enabledSuccess'),
          t('settings.notifications.lunarCycleDesc') + ' ' + t('settings.notifications.voidOfCourseDesc'),
          [{ text: 'OK' }]
        );
      }
    } catch (error) {
      console.error('[Settings] Erreur toggle notifications:', error);
      Alert.alert('Erreur', 'Une erreur est survenue. Veuillez réessayer.');
    } finally {
      setIsTogglingNotifications(false);
    }
  };

  const handleLogout = () => {
    Alert.alert('Déconnexion', 'Êtes-vous sûr de vouloir vous déconnecter ?', [
      { text: 'Annuler', style: 'cancel' },
      {
        text: 'Déconnexion',
        style: 'destructive',
        onPress: async () => {
          await logout();
          router.replace('/welcome');
        },
      },
    ]);
  };

  return (
    <ScrollView style={styles.container}>
      {/* Header */}
      <View style={styles.header}>
        <TouchableOpacity style={styles.backButton} onPress={() => router.back()}>
          <Text style={styles.backButtonText}>← Retour</Text>
        </TouchableOpacity>

        <Text style={styles.title}>⚙️ Réglages</Text>
      </View>

      {/* User Info */}
      {user && (
        <View style={styles.section}>
          <Text style={styles.sectionTitle}>Informations</Text>

          <View style={styles.infoRow}>
            <Text style={styles.infoLabel}>Email :</Text>
            <Text style={styles.infoValue}>{user.email}</Text>
          </View>

          {user.birth_date && (
            <View style={styles.infoRow}>
              <Text style={styles.infoLabel}>Date de naissance :</Text>
              <Text style={styles.infoValue}>
                {new Date(user.birth_date).toLocaleDateString('fr-FR')}
              </Text>
            </View>
          )}

          {user.birth_time && (
            <View style={styles.infoRow}>
              <Text style={styles.infoLabel}>Heure de naissance :</Text>
              <Text style={styles.infoValue}>{user.birth_time}</Text>
            </View>
          )}

          {user.birth_place_name && (
            <View style={styles.infoRow}>
              <Text style={styles.infoLabel}>Lieu de naissance :</Text>
              <Text style={styles.infoValue}>{user.birth_place_name}</Text>
            </View>
          )}
        </View>
      )}

      {/* Notifications Settings */}
      <View style={styles.section}>
        <Text style={styles.sectionTitle}>Notifications</Text>

        <View style={styles.settingRow}>
          <View style={styles.settingInfo}>
            <Text style={styles.settingLabel}>Activer les notifications</Text>
            <Text style={styles.settingDescription}>
              Recevoir des rappels pour les fenêtres VoC et les nouveaux cycles lunaires
            </Text>
          </View>

          <Switch
            value={notificationsEnabled}
            onValueChange={handleNotificationToggle}
            disabled={isTogglingNotifications}
            trackColor={{ false: '#2D3561', true: '#8B7BF7' }}
            thumbColor={notificationsEnabled ? '#FFFFFF' : '#A0A0B0'}
            ios_backgroundColor="#2D3561"
          />
        </View>

        {notificationsEnabled && (
          <View style={styles.notificationHint}>
            <Text style={styles.notificationHintEmoji}>✅</Text>
            <Text style={styles.notificationHintText}>
              Vous recevrez des notifications au début des fenêtres VoC et lors des nouveaux cycles
              lunaires.
            </Text>
          </View>
        )}
      </View>

      {/* Actions */}
      <View style={styles.section}>
        <TouchableOpacity style={styles.logoutButton} onPress={handleLogout}>
          <Text style={styles.logoutButtonText}>Déconnexion</Text>
        </TouchableOpacity>
      </View>

      {/* DEV ONLY: QA Tools Section */}
      {__DEV__ && DevQASection && (
        <View style={styles.section}>
          <DevQASection />
        </View>
      )}

      {/* Footer */}
      <View style={styles.footer}>
        <Text style={styles.footerText}>Lunation MVP v1.4</Text>
        <Text style={styles.footerText}>Phase 1.4 : Notifications Push</Text>
      </View>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#0A0E27',
  },
  header: {
    padding: 20,
    paddingTop: 60,
    backgroundColor: '#1A1F3E',
    borderBottomWidth: 2,
    borderBottomColor: '#8B7BF7',
    position: 'relative',
  },
  backButton: {
    position: 'absolute',
    top: 60,
    left: 20,
    zIndex: 10,
  },
  backButtonText: {
    color: '#FFFFFF',
    fontSize: 16,
    fontWeight: '600',
  },
  title: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#FFFFFF',
    textAlign: 'center',
    marginTop: 24,
  },
  section: {
    margin: 16,
    padding: 20,
    backgroundColor: '#1A1F3E',
    borderRadius: 12,
    borderWidth: 1,
    borderColor: '#2D3561',
  },
  sectionTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#8B7BF7',
    marginBottom: 16,
  },
  infoRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginBottom: 12,
  },
  infoLabel: {
    fontSize: 14,
    color: '#A0A0B0',
  },
  infoValue: {
    fontSize: 14,
    fontWeight: '600',
    color: '#FFFFFF',
  },
  settingRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  settingInfo: {
    flex: 1,
    marginRight: 16,
  },
  settingLabel: {
    fontSize: 16,
    fontWeight: '600',
    color: '#FFFFFF',
    marginBottom: 4,
  },
  settingDescription: {
    fontSize: 13,
    color: '#A0A0B0',
    lineHeight: 18,
  },
  notificationHint: {
    flexDirection: 'row',
    marginTop: 16,
    padding: 12,
    backgroundColor: 'rgba(74, 222, 128, 0.1)',
    borderRadius: 8,
    borderWidth: 1,
    borderColor: 'rgba(74, 222, 128, 0.3)',
  },
  notificationHintEmoji: {
    fontSize: 18,
    marginRight: 8,
  },
  notificationHintText: {
    flex: 1,
    fontSize: 13,
    color: '#4ADE80',
    lineHeight: 18,
  },
  logoutButton: {
    backgroundColor: '#FF6B6B',
    padding: 16,
    borderRadius: 8,
    alignItems: 'center',
  },
  logoutButtonText: {
    color: '#FFFFFF',
    fontSize: 16,
    fontWeight: '600',
  },
  footer: {
    padding: 20,
    alignItems: 'center',
  },
  footerText: {
    fontSize: 12,
    color: '#A0A0B0',
    marginBottom: 4,
  },
});
