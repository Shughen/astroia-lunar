/**
 * DEV ONLY - QA Helper for Notifications & Deep Links
 *
 * This component is ONLY visible in __DEV__ mode.
 * Provides quick testing buttons for:
 * - Triggering all 3 notification types (VoC start, VoC end, New cycle)
 * - Canceling all scheduled notifications
 * - Testing deep links navigation
 *
 * CRITICAL: This code must NEVER run in production.
 */

import React, { useState } from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  Alert,
  Platform,
  Linking,
} from 'react-native';
import { router } from 'expo-router';
import * as Notifications from 'expo-notifications';
import i18n from '../i18n';
import { requestNotificationPermissions, cancelAllNotifications } from '../services/notificationScheduler';
import { resetAllUserData } from '../services/resetUserData';
import { useResetStore } from '../stores/useResetStore';

/**
 * Schedule QA test notifications with realistic data
 * T+15s: VoC start
 * T+30s: VoC end
 * T+45s: New cycle
 */
async function scheduleQANotifications() {
  try {
    // Check permissions first
    const hasPermission = await requestNotificationPermissions();

    if (!hasPermission) {
      Alert.alert(
        'Permission Required',
        'Notifications permission not granted. Please enable in device settings.',
        [
          { text: 'Cancel', style: 'cancel' },
          {
            text: 'Open Settings',
            onPress: () => {
              if (Platform.OS === 'ios') {
                Linking.openURL('app-settings:');
              } else {
                Linking.openSettings();
              }
            }
          }
        ]
      );
      console.warn('[DEV QA] Notification permissions not granted');
      return;
    }

    // Cancel any existing scheduled notifications first
    await Notifications.cancelAllScheduledNotificationsAsync();
    console.log('[DEV QA] Canceled existing notifications');

    // Schedule VoC Start (T+15s)
    await Notifications.scheduleNotificationAsync({
      content: {
        title: i18n.t('notifications.vocStart.title'),
        body: i18n.t('notifications.vocStart.body', { endTime: '18:30' }),
        data: { type: 'voc_start', screen: '/lunar/voc' },
        sound: true,
      },
      trigger: {
        type: Notifications.SchedulableTriggerInputTypes.TIME_INTERVAL,
        seconds: 15,
      },
    });
    console.log('[DEV QA] Scheduled VoC Start notification (T+15s)');

    // Schedule VoC End (T+30s)
    await Notifications.scheduleNotificationAsync({
      content: {
        title: i18n.t('notifications.vocEnd.title'),
        body: i18n.t('notifications.vocEnd.body', { endTime: '18:30' }),
        data: { type: 'voc_end_soon', screen: '/lunar/voc' },
        sound: true,
      },
      trigger: {
        type: Notifications.SchedulableTriggerInputTypes.TIME_INTERVAL,
        seconds: 30,
      },
    });
    console.log('[DEV QA] Scheduled VoC End notification (T+30s)');

    // Schedule New Cycle (T+45s)
    await Notifications.scheduleNotificationAsync({
      content: {
        title: i18n.t('notifications.newCycle.title'),
        body: i18n.t('notifications.newCycle.body', {
          month: 'Janvier',
          sign: 'Taureau',
          ascendant: 'Balance'
        }),
        data: { type: 'lunar_cycle_start', screen: '/lunar/report' },
        sound: true,
      },
      trigger: {
        type: Notifications.SchedulableTriggerInputTypes.TIME_INTERVAL,
        seconds: 45,
      },
    });
    console.log('[DEV QA] Scheduled New Cycle notification (T+45s)');

    Alert.alert(
      'QA Notifications Scheduled',
      '3 test notifications scheduled:\n\n' +
      '• T+15s: VoC Start → /lunar/voc\n' +
      '• T+30s: VoC End → /lunar/voc\n' +
      '• T+45s: New Cycle → /lunar/report\n\n' +
      'Tap notifications to test deep links.',
      [{ text: 'OK' }]
    );
  } catch (error) {
    console.error('[DEV QA] Error scheduling test notifications:', error);
    Alert.alert('Error', 'Failed to schedule test notifications. Check console.');
  }
}

/**
 * Cancel all scheduled notifications
 */
async function handleCancelAll() {
  try {
    await cancelAllNotifications();
    console.log('[DEV QA] All notifications canceled');
    Alert.alert('Notifications Canceled', 'All scheduled notifications have been removed.', [{ text: 'OK' }]);
  } catch (error) {
    console.error('[DEV QA] Error canceling notifications:', error);
    Alert.alert('Error', 'Failed to cancel notifications. Check console.');
  }
}


/**
 * DEV QA Section Component
 */
function DevQASection() {
  const [loading, setLoading] = useState(false);
  const { setIsResetting } = useResetStore();

  const handleScheduleQA = async () => {
    setLoading(true);
    await scheduleQANotifications();
    setLoading(false);
  };

  const handleCancel = async () => {
    setLoading(true);
    await handleCancelAll();
    setLoading(false);
  };

  const handleResetUserData = async () => {
    Alert.alert(
      'Reset des Données Locales',
      'Cette action va supprimer toutes les données locales :\n\n' +
      '• Onboarding (welcome, profile, consent, etc.)\n' +
      '• Journal (toutes les entrées)\n' +
      '• Cache lunaire\n' +
      '• Stores (cycle, natal, auth)\n' +
      '• Notifications planifiées\n\n' +
      'Vous serez redirigé vers l\'écran Welcome.',
      [
        { text: 'Annuler', style: 'cancel' },
        {
          text: 'Reset',
          style: 'destructive',
          onPress: async () => {
            setLoading(true);
            try {
              console.log('[DEV QA] 🗑️ Début reset via DevQASection...');
              
              // Reset atomique
              await resetAllUserData();
              
              console.log('[DEV QA] ✅ Reset terminé, navigation vers /welcome...');
              
              // Navigation après reset complet
              router.replace('/welcome');
              
              // Relâcher le flag après un court délai
              setTimeout(() => {
                setIsResetting(false);
                console.log('[DEV QA] ✅ Flag isResetting relâché');
              }, 500);
            } catch (error) {
              console.error('[DEV QA] ❌ Erreur lors du reset:', error);
              setIsResetting(false);
              Alert.alert('Erreur', 'Une erreur est survenue lors du reset. Vérifiez la console.');
            } finally {
              setLoading(false);
            }
          },
        },
      ]
    );
  };

  return (
    <View style={styles.container}>
      <Text style={styles.header}>🔧 DEV QA Tools</Text>
      <Text style={styles.description}>
        Test notifications & deep links
      </Text>

      <TouchableOpacity
        style={[styles.button, styles.primaryButton]}
        onPress={handleScheduleQA}
        disabled={loading}
      >
        <Text style={styles.buttonText}>
          {loading ? 'Scheduling...' : '🔔 Trigger QA Notifications'}
        </Text>
      </TouchableOpacity>

      <TouchableOpacity
        style={[styles.button, styles.secondaryButton]}
        onPress={handleCancel}
        disabled={loading}
      >
        <Text style={styles.buttonText}>
          {loading ? 'Canceling...' : '🚫 Cancel All Notifications'}
        </Text>
      </TouchableOpacity>

      <View style={styles.separator} />

      <TouchableOpacity
        style={[styles.button, styles.dangerButton]}
        onPress={handleResetUserData}
        disabled={loading}
      >
        <Text style={styles.buttonText}>
          {loading ? 'Resetting...' : '🗑️ Reset User Data (Local)'}
        </Text>
      </TouchableOpacity>

      <Text style={styles.hint}>
        Notifications will trigger in 15s, 30s, and 45s. Tap them to test deep links.
      </Text>
      <Text style={styles.hint}>
        Reset clears: onboarding, journal, cache, stores. Redirects to Welcome.
      </Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    marginTop: 24,
    padding: 16,
    backgroundColor: '#2D1B4E',
    borderRadius: 12,
    borderWidth: 2,
    borderColor: '#FF6B6B',
    borderStyle: 'dashed',
  },
  header: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#FF6B6B',
    marginBottom: 4,
  },
  description: {
    fontSize: 14,
    color: '#A0A0B0',
    marginBottom: 16,
  },
  button: {
    padding: 14,
    borderRadius: 8,
    alignItems: 'center',
    marginBottom: 12,
  },
  primaryButton: {
    backgroundColor: '#8B7BF7',
  },
  secondaryButton: {
    backgroundColor: '#4A5568',
  },
  dangerButton: {
    backgroundColor: '#DC2626',
  },
  separator: {
    height: 1,
    backgroundColor: '#4A5568',
    marginVertical: 12,
  },
  buttonText: {
    color: '#FFFFFF',
    fontSize: 15,
    fontWeight: '600',
  },
  hint: {
    fontSize: 12,
    color: '#A0A0B0',
    fontStyle: 'italic',
    textAlign: 'center',
  },
});

// Export null in production, component in dev
export default __DEV__ ? DevQASection : null;
