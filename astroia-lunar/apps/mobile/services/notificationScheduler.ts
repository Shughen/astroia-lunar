/**
 * Service de scheduling des notifications locales intelligentes
 *
 * Notifications supportées :
 * - VoC (Void of Course) : 30 min avant début + au début
 * - Cycle lunaire : début de révolution lunaire personnelle
 * - Phases lunaires : Nouvelle Lune, Pleine Lune (2h avant)
 * - Changement de signe lunaire (2h avant)
 * - Rappel journal hebdomadaire (dimanche 20h)
 *
 * Architecture :
 * - Scheduling local uniquement (pas de push serveur)
 * - Re-scheduling automatique au focus app (max 1x/24h)
 * - Respect des préférences utilisateur via NotificationsStore
 */

import * as Notifications from 'expo-notifications';
import { Platform } from 'react-native';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { STORAGE_KEYS } from '../types/storage';
import i18n from '../i18n';
import { haptics } from './haptics';

// ✅ Notifications activées pour production
export const ENABLE_VOC_NOTIFICATIONS = true;

// Configuration par défaut des notifications
// Inclut un feedback haptic quand une notification arrive en foreground
Notifications.setNotificationHandler({
  handleNotification: async () => {
    // Feedback haptic quand notification reçue en foreground
    haptics.light();

    return {
      shouldShowAlert: true,
      shouldPlaySound: true,
      shouldSetBadge: false, // Pas de badge count pour MVP
      shouldShowBanner: true,
      shouldShowList: true,
    };
  },
});

export interface VocWindow {
  start_at: string;
  end_at: string;
}

export interface LunarReturn {
  id: string;
  return_date: string;
  moon_sign?: string;
  lunar_ascendant?: string;
}

/**
 * Demande la permission système pour les notifications
 * @returns true si permission accordée, false sinon
 */
export async function requestNotificationPermissions(): Promise<boolean> {
  if (!ENABLE_VOC_NOTIFICATIONS) {
    console.log('[Notifications] Feature désactivée (ENABLE_VOC_NOTIFICATIONS = false)');
    return false;
  }

  try {
    const { status: existingStatus } = await Notifications.getPermissionsAsync();

    let finalStatus = existingStatus;

    if (existingStatus !== 'granted') {
      const { status } = await Notifications.requestPermissionsAsync();
      finalStatus = status;
    }

    if (finalStatus !== 'granted') {
      console.log('[Notifications] Permission refusée');
      return false;
    }

    // Android : configurer channel
    if (Platform.OS === 'android') {
      await Notifications.setNotificationChannelAsync('default', {
        name: 'Lunation Notifications',
        importance: Notifications.AndroidImportance.HIGH,
        vibrationPattern: [0, 250, 250, 250],
        lightColor: '#8B7BF7',
      });
    }

    console.log('[Notifications] ✅ Permission accordée');
    return true;
  } catch (error) {
    console.error('[Notifications] ❌ Erreur demande permission:', error);
    return false;
  }
}

/**
 * Configure les permissions de notifications (alias de requestNotificationPermissions)
 * @returns true si permission accordée, false sinon
 */
export async function setupNotificationPermissions(): Promise<boolean> {
  return requestNotificationPermissions();
}

/**
 * Récupère la liste des notifications VoC schedulées
 * @returns Liste des notifications planifiées
 */
export async function getScheduledNotifications(): Promise<Notifications.NotificationRequest[]> {
  if (!ENABLE_VOC_NOTIFICATIONS) {
    console.log('[Notifications] Feature désactivée, aucune notification schedulée');
    return [];
  }

  try {
    const scheduled = await Notifications.getAllScheduledNotificationsAsync();
    console.log(`[Notifications] ${scheduled.length} notifications schedulées`);
    return scheduled;
  } catch (error) {
    console.error('[Notifications] ❌ Erreur récupération notifications:', error);
    return [];
  }
}

/**
 * Annule toutes les notifications VoC schedulées
 * Alias de cancelAllNotifications pour compatibilité API
 */
export async function cancelAllVocNotifications(): Promise<void> {
  return cancelAllNotifications();
}

/**
 * Annule toutes les notifications schedulées
 */
export async function cancelAllNotifications(): Promise<void> {
  if (!ENABLE_VOC_NOTIFICATIONS) {
    console.log('[Notifications] Feature désactivée, aucune notification à annuler');
    return;
  }

  try {
    await Notifications.cancelAllScheduledNotificationsAsync();
    console.log('[Notifications] ✅ Toutes notifications annulées');
  } catch (error) {
    console.error('[Notifications] ❌ Erreur annulation notifications:', error);
  }
}

/**
 * Schedule une notification VoC unique (30 min avant + au début)
 * @param vocWindow Fenêtre VoC à notifier
 */
export async function scheduleVocNotification(vocWindow: VocWindow): Promise<void> {
  if (!ENABLE_VOC_NOTIFICATIONS) {
    console.log('[VoC Notifications] Feature désactivée (ENABLE_VOC_NOTIFICATIONS = false)');
    return;
  }

  try {
    const now = new Date();
    const startDate = new Date(vocWindow.start_at);
    const endDate = new Date(vocWindow.end_at);

    // Skip si fenêtre déjà passée
    if (startDate < now) {
      console.log('[Notifications] Fenêtre VoC déjà passée, skip');
      return;
    }

    let scheduledCount = 0;

    // Notification 30 min avant début VoC
    const preWarning = new Date(startDate.getTime() - 30 * 60 * 1000);
    const preTrigger = preWarning.getTime() - now.getTime();

    if (preTrigger > 0 && preWarning > now) {
      await Notifications.scheduleNotificationAsync({
        content: {
          title: '🌑 Pause Lunaire dans 30 min',
          body: 'La Lune entre bientôt en pause — évite les décisions importantes',
          data: {
            type: 'voc_pre_warning',
            windowId: `${vocWindow.start_at}`,
            screen: '/lunar/voc'
          },
          sound: true,
        },
        trigger: {
          type: Notifications.SchedulableTriggerInputTypes.TIME_INTERVAL,
          seconds: Math.floor(preTrigger / 1000),
        },
      });
      scheduledCount++;
    }

    // Notification début VoC
    const startTrigger = startDate.getTime() - now.getTime();
    if (startTrigger > 0) {
      await Notifications.scheduleNotificationAsync({
        content: {
          title: '🌑 Pause Lunaire active',
          body: `Moment d'introspection jusqu'à ${formatTime(endDate)} — reporte les décisions importantes`,
          data: {
            type: 'voc_start',
            windowId: `${vocWindow.start_at}`,
            screen: '/lunar/voc'
          },
          sound: true,
        },
        trigger: {
          type: Notifications.SchedulableTriggerInputTypes.TIME_INTERVAL,
          seconds: Math.floor(startTrigger / 1000),
        },
      });
      scheduledCount++;
    }

    console.log(`[Notifications] ✅ ${scheduledCount} notifications VoC schedulées pour fenêtre`);
  } catch (error) {
    console.error('[Notifications] ❌ Erreur scheduling VoC:', error);
  }
}

/**
 * Schedule les notifications VoC (début + 30min avant fin)
 * @param vocWindows Liste des fenêtres VoC à venir (48h max)
 */
export async function scheduleVocNotifications(vocWindows: VocWindow[]): Promise<void> {
  if (!ENABLE_VOC_NOTIFICATIONS) {
    console.log('[VoC Notifications] Feature désactivée (ENABLE_VOC_NOTIFICATIONS = false)');
    return;
  }

  try {
    const now = new Date();
    let scheduledCount = 0;

    for (const window of vocWindows) {
      const startDate = new Date(window.start_at);
      const endDate = new Date(window.end_at);

      // Skip si fenêtre déjà passée
      if (startDate < now) {
        continue;
      }

      // Notification début VoC
      const startTrigger = startDate.getTime() - now.getTime();
      if (startTrigger > 0) {
        await Notifications.scheduleNotificationAsync({
          content: {
            title: i18n.t('notifications.vocStart.title'),
            body: i18n.t('notifications.vocStart.body', { endTime: formatTime(endDate) }),
            data: { type: 'voc_start', screen: '/lunar/voc' },
            sound: true,
          },
          trigger: {
            type: Notifications.SchedulableTriggerInputTypes.TIME_INTERVAL,
            seconds: Math.floor(startTrigger / 1000),
          },
        });
        scheduledCount++;
      }

      // Notification 30 min avant fin VoC
      const endWarning = new Date(endDate.getTime() - 30 * 60 * 1000);
      const endTrigger = endWarning.getTime() - now.getTime();

      if (endTrigger > 0 && endWarning > now) {
        await Notifications.scheduleNotificationAsync({
          content: {
            title: i18n.t('notifications.vocEnd.title'),
            body: i18n.t('notifications.vocEnd.body', { endTime: formatTime(endDate) }),
            data: { type: 'voc_end_soon', screen: '/lunar/voc' },
            sound: true,
          },
          trigger: {
            type: Notifications.SchedulableTriggerInputTypes.TIME_INTERVAL,
            seconds: Math.floor(endTrigger / 1000),
          },
        });
        scheduledCount++;
      }
    }

    console.log(`[Notifications] ✅ ${scheduledCount} notifications VoC schedulées`);
  } catch (error) {
    console.error('[Notifications] ❌ Erreur scheduling VoC:', error);
  }
}

/**
 * Schedule la notification de début de cycle lunaire
 * @param lunarReturn Révolution lunaire en cours
 */
export async function scheduleLunarCycleNotification(lunarReturn: LunarReturn): Promise<void> {
  if (!ENABLE_VOC_NOTIFICATIONS) {
    console.log('[Notifications] Feature désactivée, skip cycle lunaire notification');
    return;
  }

  try {
    const now = new Date();
    const cycleStart = new Date(lunarReturn.return_date);

    // Skip si cycle déjà commencé (> 24h passées)
    const hoursSinceStart = (now.getTime() - cycleStart.getTime()) / (1000 * 60 * 60);
    if (hoursSinceStart > 24) {
      console.log('[Notifications] Cycle déjà commencé (>24h), skip notification');
      return;
    }

    // Si cycle commence dans le futur, scheduler notification
    if (cycleStart > now) {
      const trigger = cycleStart.getTime() - now.getTime();

      await Notifications.scheduleNotificationAsync({
        content: {
          title: i18n.t('notifications.newCycle.title'),
          body: i18n.t('notifications.newCycle.body', {
            month: cycleStart.toLocaleDateString('fr-FR', { month: 'long', year: 'numeric' }),
            sign: lunarReturn.moon_sign || '',
            ascendant: lunarReturn.lunar_ascendant || ''
          }),
          data: { type: 'lunar_cycle_start', screen: '/lunar/report' },
          sound: true,
        },
        trigger: {
          type: Notifications.SchedulableTriggerInputTypes.TIME_INTERVAL,
          seconds: Math.floor(trigger / 1000),
        },
      });

      console.log('[Notifications] ✅ Notification cycle lunaire schedulée');
    } else {
      console.log('[Notifications] Cycle déjà commencé, pas de notification');
    }
  } catch (error) {
    console.error('[Notifications] ❌ Erreur scheduling cycle lunaire:', error);
  }
}

/**
 * Vérifie si on doit re-scheduler (dernière fois > 24h)
 * @returns true si re-scheduling nécessaire
 */
export async function shouldReschedule(): Promise<boolean> {
  try {
    const lastScheduled = await AsyncStorage.getItem(STORAGE_KEYS.NOTIFICATIONS_LAST_SCHEDULED_AT);

    if (!lastScheduled) {
      return true; // Jamais schedulé
    }

    const lastScheduledDate = new Date(lastScheduled);
    const now = new Date();
    const hoursSince = (now.getTime() - lastScheduledDate.getTime()) / (1000 * 60 * 60);

    return hoursSince >= 24;
  } catch (error) {
    console.error('[Notifications] ❌ Erreur vérification shouldReschedule:', error);
    return true; // En cas d'erreur, reschedule par sécurité
  }
}

/**
 * Enregistre le timestamp du dernier scheduling
 */
export async function markScheduled(): Promise<void> {
  try {
    await AsyncStorage.setItem(STORAGE_KEYS.NOTIFICATIONS_LAST_SCHEDULED_AT, new Date().toISOString());
  } catch (error) {
    console.error('[Notifications] ❌ Erreur enregistrement lastScheduledAt:', error);
  }
}

/**
 * Formate une date en heure lisible (ex: "14:30")
 */
function formatTime(date: Date): string {
  return date.toLocaleTimeString('fr-FR', {
    hour: '2-digit',
    minute: '2-digit',
  });
}

/**
 * Configure le listener pour les notifications tappées
 * @param onNotificationTap Callback appelé avec le screen à ouvrir
 */
export function setupNotificationTapListener(
  onNotificationTap: (screen: string) => void
): Notifications.Subscription {
  return Notifications.addNotificationResponseReceivedListener((response) => {
    const screen = response.notification.request.content.data.screen as string;
    if (screen) {
      console.log(`[Notifications] Tap notification → ${screen}`);
      onNotificationTap(screen);
    }
  });
}

// ============================================
// NOTIFICATIONS INTELLIGENTES (Whahou #4)
// ============================================

export interface MoonPhaseEvent {
  phase: 'new_moon' | 'first_quarter' | 'full_moon' | 'last_quarter';
  date: string;
  sign?: string;
}

export interface MoonSignChange {
  sign: string;
  enters_at: string;
}

/**
 * Traduit un signe anglais en français
 */
function translateSign(sign: string): string {
  const translations: Record<string, string> = {
    'Aries': 'Bélier',
    'Taurus': 'Taureau',
    'Gemini': 'Gémeaux',
    'Cancer': 'Cancer',
    'Leo': 'Lion',
    'Virgo': 'Vierge',
    'Libra': 'Balance',
    'Scorpio': 'Scorpion',
    'Sagittarius': 'Sagittaire',
    'Capricorn': 'Capricorne',
    'Aquarius': 'Verseau',
    'Pisces': 'Poissons',
  };
  return translations[sign] || sign;
}

/**
 * Schedule les notifications de phases lunaires (Nouvelle Lune, Pleine Lune)
 * @param phases Liste des phases à venir
 */
export async function scheduleMoonPhaseNotifications(phases: MoonPhaseEvent[]): Promise<void> {
  if (!ENABLE_VOC_NOTIFICATIONS) {
    return;
  }

  try {
    const now = new Date();
    let scheduledCount = 0;

    for (const phase of phases) {
      const phaseDate = new Date(phase.date);

      // Skip si phase déjà passée
      if (phaseDate < now) {
        continue;
      }

      // Notification 2h avant la phase
      const preWarning = new Date(phaseDate.getTime() - 2 * 60 * 60 * 1000);
      const preTrigger = preWarning.getTime() - now.getTime();

      if (preTrigger > 0) {
        let title = '';
        let body = '';
        const signFr = phase.sign ? translateSign(phase.sign) : '';

        switch (phase.phase) {
          case 'new_moon':
            title = '🌑 Nouvelle Lune ce soir';
            body = signFr
              ? `Nouvelle Lune en ${signFr} dans 2h — moment idéal pour poser tes intentions`
              : 'Nouvelle Lune dans 2h — moment idéal pour poser tes intentions';
            break;
          case 'full_moon':
            title = '🌕 Pleine Lune ce soir';
            body = signFr
              ? `Pleine Lune en ${signFr} dans 2h — moment de culmination et récolte`
              : 'Pleine Lune dans 2h — moment de culmination et récolte';
            break;
          case 'first_quarter':
            title = '🌓 Premier Quartier';
            body = 'La Lune entre en Premier Quartier — temps d\'action et décisions';
            break;
          case 'last_quarter':
            title = '🌗 Dernier Quartier';
            body = 'La Lune entre en Dernier Quartier — temps de bilan et lâcher-prise';
            break;
        }

        await Notifications.scheduleNotificationAsync({
          content: {
            title,
            body,
            data: {
              type: `moon_phase_${phase.phase}`,
              screen: '/'
            },
            sound: true,
          },
          trigger: {
            type: Notifications.SchedulableTriggerInputTypes.TIME_INTERVAL,
            seconds: Math.floor(preTrigger / 1000),
          },
        });
        scheduledCount++;
      }
    }

    console.log(`[Notifications] ✅ ${scheduledCount} notifications phases lunaires schedulées`);
  } catch (error) {
    console.error('[Notifications] ❌ Erreur scheduling phases lunaires:', error);
  }
}

/**
 * Schedule les notifications de changement de signe lunaire
 * @param signChanges Liste des changements de signe à venir
 */
export async function scheduleMoonSignChangeNotifications(signChanges: MoonSignChange[]): Promise<void> {
  if (!ENABLE_VOC_NOTIFICATIONS) {
    return;
  }

  try {
    const now = new Date();
    let scheduledCount = 0;

    for (const change of signChanges) {
      const changeDate = new Date(change.enters_at);

      // Skip si déjà passé
      if (changeDate < now) {
        continue;
      }

      // Notification 2h avant le changement de signe
      const preWarning = new Date(changeDate.getTime() - 2 * 60 * 60 * 1000);
      const preTrigger = preWarning.getTime() - now.getTime();

      if (preTrigger > 0) {
        const signFr = translateSign(change.sign);

        await Notifications.scheduleNotificationAsync({
          content: {
            title: '🌙 Changement d\'énergie',
            body: `La Lune entre en ${signFr} dans 2h — prépare-toi !`,
            data: {
              type: 'moon_sign_change',
              sign: change.sign,
              screen: '/'
            },
            sound: true,
          },
          trigger: {
            type: Notifications.SchedulableTriggerInputTypes.TIME_INTERVAL,
            seconds: Math.floor(preTrigger / 1000),
          },
        });
        scheduledCount++;
      }
    }

    console.log(`[Notifications] ✅ ${scheduledCount} notifications changement de signe schedulées`);
  } catch (error) {
    console.error('[Notifications] ❌ Erreur scheduling changement de signe:', error);
  }
}

/**
 * Schedule une notification de rappel journal hebdomadaire
 * Tous les dimanches à 20h
 */
export async function scheduleWeeklyJournalReminder(): Promise<void> {
  if (!ENABLE_VOC_NOTIFICATIONS) {
    return;
  }

  try {
    // Trouver le prochain dimanche à 20h
    const now = new Date();
    const nextSunday = new Date(now);
    nextSunday.setDate(now.getDate() + ((7 - now.getDay()) % 7 || 7));
    nextSunday.setHours(20, 0, 0, 0);

    // Si c'est dimanche et avant 20h, utiliser aujourd'hui
    if (now.getDay() === 0 && now.getHours() < 20) {
      nextSunday.setDate(now.getDate());
    }

    const trigger = nextSunday.getTime() - now.getTime();

    if (trigger > 0) {
      // Calculer le numéro de semaine dans le cycle (approximatif)
      const weekNumber = Math.ceil((now.getDate()) / 7);

      await Notifications.scheduleNotificationAsync({
        content: {
          title: '📖 Moment de réflexion',
          body: `Semaine ${weekNumber} de ton cycle — As-tu noté tes observations ?`,
          data: {
            type: 'journal_reminder',
            screen: '/journal'
          },
          sound: true,
        },
        trigger: {
          type: Notifications.SchedulableTriggerInputTypes.TIME_INTERVAL,
          seconds: Math.floor(trigger / 1000),
        },
      });

      console.log('[Notifications] ✅ Rappel journal hebdomadaire schedulé');
    }
  } catch (error) {
    console.error('[Notifications] ❌ Erreur scheduling rappel journal:', error);
  }
}
