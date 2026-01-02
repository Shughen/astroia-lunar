/**
 * Types et clés AsyncStorage
 */

// Storage Keys
export const STORAGE_KEYS = {
  // Auth
  AUTH_TOKEN: 'auth_token',

  // Onboarding
  HAS_SEEN_WELCOME_SCREEN: 'hasSeenWelcomeScreen',
  ONBOARDING_COMPLETED: 'onboarding_completed',
  ONBOARDING_PROFILE: 'onboarding_profile',
  ONBOARDING_CONSENT: 'onboarding_consent',
  ONBOARDING_DISCLAIMER: 'onboarding_disclaimer',

  // Profile
  BIRTH_DATE: 'birth_date',
  BIRTH_TIME: 'birth_time',
  BIRTH_PLACE: 'birth_place',
  BIRTH_LATITUDE: 'birth_latitude',
  BIRTH_LONGITUDE: 'birth_longitude',

  // Cycle
  LAST_PERIOD_DATE: 'lastPeriodDate',
  AVERAGE_CYCLE_LENGTH: 'averageCycleLength',

  // Daily Ritual
  DAILY_RESONANCE: 'daily_resonance', // {date: "YYYY-MM-DD", value: "yes"|"no"|"maybe"}

  // Notifications (Phase 1.4)
  NOTIFICATIONS_ENABLED: 'notifications_enabled',
  NOTIFICATIONS_LAST_SCHEDULED_AT: 'notifications_last_scheduled_at',

  // Migrations
  MIGRATION_GHOSTFLAGS_DONE: 'migration_ghostflags_done',
} as const;

export type StorageKey = typeof STORAGE_KEYS[keyof typeof STORAGE_KEYS];
