/**
 * Store Zustand pour les préférences de notifications (Phase 1.4)
 */

import { create } from 'zustand';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { STORAGE_KEYS } from '../types/storage';
import {
  requestNotificationPermissions,
  cancelAllNotifications,
  scheduleVocNotifications,
  scheduleLunarCycleNotification,
  scheduleMoonPhaseNotifications,
  scheduleMoonSignChangeNotifications,
  scheduleWeeklyJournalReminder,
  markScheduled,
  type VocWindow,
  type LunarReturn,
  type MoonPhaseEvent,
  type MoonSignChange,
} from '../services/notificationScheduler';
import apiClient from '../services/api';

interface NotificationsState {
  // State
  notificationsEnabled: boolean;
  hydrated: boolean;

  // Actions
  loadPreferences: () => Promise<void>;
  setNotificationsEnabled: (enabled: boolean) => Promise<boolean>;
  scheduleAllNotifications: () => Promise<void>;
}

export const useNotificationsStore = create<NotificationsState>((set, get) => ({
  // State initial
  notificationsEnabled: false,
  hydrated: false,

  // Charger les préférences depuis AsyncStorage
  loadPreferences: async () => {
    try {
      const enabled = await AsyncStorage.getItem(STORAGE_KEYS.NOTIFICATIONS_ENABLED);
      set({
        notificationsEnabled: enabled === 'true',
        hydrated: true,
      });
      console.log('[NotificationsStore] ✅ Préférences chargées:', enabled === 'true');
    } catch (error) {
      console.error('[NotificationsStore] ❌ Erreur chargement préférences:', error);
      set({ hydrated: true });
    }
  },

  // Activer/désactiver les notifications
  setNotificationsEnabled: async (enabled: boolean): Promise<boolean> => {
    try {
      if (enabled) {
        // Demander permission système
        const hasPermission = await requestNotificationPermissions();

        if (!hasPermission) {
          console.log('[NotificationsStore] Permission refusée');
          // S'assurer que le toggle reste OFF après refus
          set({ notificationsEnabled: false });
          return false; // Permission refusée
        }

        // Sauvegarder préférence
        await AsyncStorage.setItem(STORAGE_KEYS.NOTIFICATIONS_ENABLED, 'true');
        set({ notificationsEnabled: true });

        // Scheduler toutes les notifications
        await get().scheduleAllNotifications();

        console.log('[NotificationsStore] ✅ Notifications activées');
        return true;
      } else {
        // Annuler toutes les notifications
        await cancelAllNotifications();

        // Sauvegarder préférence
        await AsyncStorage.setItem(STORAGE_KEYS.NOTIFICATIONS_ENABLED, 'false');
        set({ notificationsEnabled: false });

        console.log('[NotificationsStore] ✅ Notifications désactivées');
        return true;
      }
    } catch (error) {
      console.error('[NotificationsStore] ❌ Erreur setNotificationsEnabled:', error);
      return false;
    }
  },

  // Scheduler toutes les notifications intelligentes
  scheduleAllNotifications: async () => {
    try {
      const { notificationsEnabled } = get();

      if (!notificationsEnabled) {
        console.log('[NotificationsStore] Notifications désactivées, skip scheduling');
        return;
      }

      console.log('[NotificationsStore] 🔔 Début scheduling notifications intelligentes...');

      // Annuler anciennes notifications
      await cancelAllNotifications();

      // 1. Scheduler notifications VoC (Pause Lunaire)
      try {
        const vocResponse = await apiClient.get('/api/lunar/voc/status');
        const vocStatus = vocResponse.data;

        if (vocStatus.upcoming && vocStatus.upcoming.length > 0) {
          await scheduleVocNotifications(vocStatus.upcoming as VocWindow[]);
        } else {
          console.log('[NotificationsStore] Aucune fenêtre VoC à venir');
        }
      } catch (vocError) {
        console.error('[NotificationsStore] ❌ Erreur scheduling VoC:', vocError);
      }

      // 2. Scheduler notification cycle lunaire personnel
      try {
        const lunarResponse = await apiClient.get('/api/lunar-returns/current');
        const lunarReturn = lunarResponse.data;

        if (lunarReturn) {
          await scheduleLunarCycleNotification(lunarReturn as LunarReturn);
        } else {
          console.log('[NotificationsStore] Aucun cycle lunaire en cours');
        }
      } catch (lunarError: any) {
        if (lunarError.response?.status !== 404) {
          console.error('[NotificationsStore] ❌ Erreur scheduling cycle lunaire:', lunarError);
        }
      }

      // 3. Scheduler notifications phases lunaires (Nouvelle Lune, Pleine Lune)
      try {
        const phasesResponse = await apiClient.get('/api/lunar/phases');
        const phases = phasesResponse.data;

        if (phases && phases.length > 0) {
          await scheduleMoonPhaseNotifications(phases as MoonPhaseEvent[]);
        } else {
          console.log('[NotificationsStore] Aucune phase lunaire à venir');
        }
      } catch (phasesError: any) {
        // API peut ne pas exister encore - silencieux
        if (phasesError.response?.status !== 404) {
          console.log('[NotificationsStore] Phases lunaires non disponibles');
        }
      }

      // 4. Scheduler notifications changement de signe lunaire
      try {
        const signChangesResponse = await apiClient.get('/api/lunar/sign-changes');
        const signChanges = signChangesResponse.data;

        if (signChanges && signChanges.length > 0) {
          await scheduleMoonSignChangeNotifications(signChanges as MoonSignChange[]);
        } else {
          console.log('[NotificationsStore] Aucun changement de signe à venir');
        }
      } catch (signError: any) {
        // API peut ne pas exister encore - silencieux
        if (signError.response?.status !== 404) {
          console.log('[NotificationsStore] Changements de signe non disponibles');
        }
      }

      // 5. Scheduler rappel journal hebdomadaire
      try {
        await scheduleWeeklyJournalReminder();
      } catch (journalError) {
        console.error('[NotificationsStore] ❌ Erreur scheduling rappel journal:', journalError);
      }

      // Marquer scheduling terminé
      await markScheduled();

      console.log('[NotificationsStore] ✅ Scheduling notifications terminé');
    } catch (error) {
      console.error('[NotificationsStore] ❌ Erreur scheduleAllNotifications:', error);
    }
  },
}));
